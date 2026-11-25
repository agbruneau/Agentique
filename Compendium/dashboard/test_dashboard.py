"""Suite de tests automatisés pour le dashboard local du Compendium.

Vérifie :
- le parseur ``parser_plan.py`` sur le vrai ``Compendium/plan.md`` ;
- la sonde disque ``probe_ouvrage()`` sur une usine simulée dans ``tmp_path`` ;
- le serveur HTTP réel ``server.py`` (routes GET, export CSV, bascule POST
  d'une case à cocher en LF strict, rejet des entrées invalides) ;
- l'autonomie hors ligne (zéro CDN) et le rendu JS sous ``Node.js`` de ``index.html``.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

DASHBOARD_DIR = Path(__file__).resolve().parent
REPO_ROOT = DASHBOARD_DIR.parents[1]
PLAN_PATH = REPO_ROOT / "Compendium" / "plan.md"
INDEX_HTML_PATH = DASHBOARD_DIR / "index.html"

sys.path.insert(0, str(DASHBOARD_DIR))
import parser_plan as pp  # noqa: E402
import server as srv_mod  # noqa: E402


def test_parse_real_plan_md_exhaustiveness() -> None:
    payload = pp.build_dashboard_payload(REPO_ROOT, PLAN_PATH)

    assert payload["meta"]["crlf_free"] is True
    assert len(payload["tasks"]) == 9
    assert payload["kpis"]["plan_steps_total"] == 32
    assert len(payload["units"]) == 42
    assert sum(u["target_words"] for u in payload["units"]) == 180_000
    assert len(payload["domains"]) == 12
    assert sum(u["families_count"] for u in payload["units"]) == 71
    assert sum(u["themes_count"] for u in payload["units"]) == 260
    assert len(payload["schemas"]) == 115
    assert len(payload["criteria_ca"]) == 22
    assert len(payload["gates"]) == 6
    assert len(payload["constraints_ao"]) == 8
    assert len(payload["waves"]) == 6
    assert len(payload["risks"]) == 5

    # Vérifier l'enrichissement des fiches chapitres (CH-01..CH-36)
    ch01 = next(u for u in payload["units"] if u["unit_id"] == "CH-01")
    assert ch01["domain_id"] == "D01"
    assert ch01["subdomain_id"] == "SUB_D01_01"
    assert ch01["target_words"] == 4620
    assert len(ch01["families"]) == 2
    assert len(ch01["themes"]) == 8
    assert len(ch01["schema_ids"]) == 3


def test_probe_ouvrage_on_simulated_progress(tmp_path: Path) -> None:
    comp_dir = tmp_path / "Compendium"
    ouvrage = comp_dir / "ouvrage"
    (ouvrage / "specs").mkdir(parents=True)
    (ouvrage / "manuscrit" / "01-partie-i").mkdir(parents=True)
    (ouvrage / "sources").mkdir(parents=True)
    (ouvrage / "ancrage").mkdir(parents=True)
    (ouvrage / "schemas" / "rendus").mkdir(parents=True)
    (ouvrage / "aq").mkdir(parents=True)
    (ouvrage / "livrables").mkdir(parents=True)

    # Copier plan.md dans le dépôt simulé
    plan_copy = comp_dir / "plan.md"
    plan_copy.write_bytes(PLAN_PATH.read_bytes())

    # Simuler 00 - Liminaire conforme (4 000 mots) et CH-01 sous-calibré (502 mots hors code/commentaire)
    (ouvrage / "manuscrit" / "00 - Liminaire.md").write_text(
        "---\ntitle: Liminaire\n---\n\n<!-- commentaire ignoré -->\n" + " ".join(["mot"] * 4000) + "\n",
        encoding="utf-8",
    )
    (ouvrage / "manuscrit" / "01-partie-i" / "ch01-rupture.md").write_text(
        "# Chapitre 01\n\n" + " ".join(["texte"] * 500) + "\n\n```python\nx = 1 + 2\n```\n",
        encoding="utf-8",
    )
    (ouvrage / "sources" / "ch00-sources.md").write_text("# Sources 00\n", encoding="utf-8")
    (ouvrage / "sources" / "ch01-sources.md").write_text("# Sources 01\n", encoding="utf-8")
    (ouvrage / "ancrage" / "ch00-ancrage.md").write_text("Verdict : supporté\nVerdict : supporté\n", encoding="utf-8")
    (ouvrage / "schemas" / "SCH-01-01.puml").write_text("@startuml\nA -> B\n@enduml\n", encoding="utf-8")
    (ouvrage / "schemas" / "rendus" / "SCH-01-01.svg").write_text("<svg></svg>\n", encoding="utf-8")
    (ouvrage / "aq" / "rapports-g0.json").write_text('{"status": "PASS"}\n', encoding="utf-8")
    (ouvrage / "livrables" / "Compendium.pdf").write_bytes(b"%PDF-1.7\n")

    payload = pp.build_dashboard_payload(tmp_path, plan_copy)
    k = payload["kpis"]
    assert payload["ouvrage_exists"] is True
    assert k["words_written"] == 4502
    assert k["units_conforme"] == 1
    assert k["units_started"] == 2
    assert k["sources_done"] == 2
    assert k["ancrages_done"] == 1
    assert k["schemas_sources_done"] == 1
    assert k["schemas_rendered_done"] == 1
    assert k["deliverables_done"] == 1
    assert k["ouvrage_pct"] > 0.0

    lim = next(u for u in payload["units"] if u["unit_id"] == "00 - Liminaire")
    ch01 = next(u for u in payload["units"] if u["unit_id"] == "CH-01")
    assert lim["manuscript_status"] == "conforme"
    assert lim["ancrage_verdicts"] == {"supported": 2, "imprecis": 0, "non_supported": 0}
    assert ch01["manuscript_status"] == "sous_calibre"
    assert ch01["schemas_rendered"] == 1


def test_http_server_endpoints_and_step_toggle(tmp_path: Path) -> None:
    comp_dir = tmp_path / "Compendium"
    comp_dir.mkdir(parents=True)
    plan_copy = comp_dir / "plan.md"
    plan_copy.write_bytes(PLAN_PATH.read_bytes())

    srv = srv_mod.create_server(repo_root=tmp_path, host="127.0.0.1", port=0, plan_path=plan_copy)
    port = srv.server_address[1]
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{port}"

    try:
        with urlopen(f"{base}/") as resp:
            assert resp.status == 200
            html = resp.read().decode("utf-8")
            assert "CompendiumDashboardEngine" in html

        with urlopen(f"{base}/api/health") as resp:
            health = json.loads(resp.read().decode("utf-8"))
            assert health["status"] == "ok"
            assert health["plan_exists"] is True

        with urlopen(f"{base}/api/dashboard") as resp:
            dash = json.loads(resp.read().decode("utf-8"))
            assert dash["kpis"]["plan_steps_total"] == 32
            first_step = dash["tasks"][0]["steps"][0]
            assert first_step["checked"] is False

        # Bascule POST -> checked=True
        req_on = Request(
            f"{base}/api/steps/toggle",
            data=json.dumps({"line_no": first_step["line_no"], "checked": True}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(req_on) as resp:
            res_on = json.loads(resp.read().decode("utf-8"))
            assert res_on["ok"] is True
            assert res_on["dashboard"]["kpis"]["plan_steps_done"] == 1
        assert b"\r\n" not in plan_copy.read_bytes()

        # Retour POST -> checked=False
        req_off = Request(
            f"{base}/api/steps/toggle",
            data=json.dumps({"line_no": first_step["line_no"], "checked": False}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(req_off) as resp:
            res_off = json.loads(resp.read().decode("utf-8"))
            assert res_off["dashboard"]["kpis"]["plan_steps_done"] == 0

        # Rejet 400 sur ligne non-checkbox
        req_bad = Request(
            f"{base}/api/steps/toggle",
            data=json.dumps({"line_no": 1, "checked": True}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with pytest.raises(HTTPError) as exc_info:
            urlopen(req_bad)
        assert exc_info.value.code == 400

        # Export CSV
        with urlopen(f"{base}/api/export/csv") as resp:
            csv_text = resp.read().decode("utf-8-sig")
            lines = csv_text.splitlines()
            assert len(lines) == 43  # en-tête + 42 unités
            assert lines[0].startswith("Unité;Type;Domaine;")
    finally:
        srv.shutdown()
        srv.server_close()
        thread.join(timeout=3)


def test_index_html_offline_and_nodejs_render_smoke() -> None:
    raw = INDEX_HTML_PATH.read_bytes()
    assert b"\r\n" not in raw, "CRLF détecté dans index.html"
    html = raw.decode("utf-8")

    # 100 % hors ligne : aucun script/CSS externe
    assert not re.search(r"<script[^>]+src\s*=", html, re.IGNORECASE)
    assert not re.search(r"<link[^>]+href\s*=\s*[\"']https?://", html, re.IGNORECASE)
    assert not re.search(r"@import\s+url\(", html, re.IGNORECASE)

    node_exe = shutil.which("node")
    if node_exe is None:
        pytest.skip("Node.js non disponible")

    payload = pp.build_dashboard_payload(REPO_ROOT, PLAN_PATH)
    node_script = r"""
    const fs = require("fs");
    const vm = require("vm");
    const html = fs.readFileSync(process.argv[1], "utf8");
    const payload = JSON.parse(fs.readFileSync(0, "utf8"));
    const jsMatch = html.match(/<script>([\s\S]*?)<\/script>/);
    if (!jsMatch) throw new Error("Bloc <script> introuvable");
    const sandbox = { console, Math, Number, String, Boolean, Array, Object, Date, RegExp, JSON, globalThis: {} };
    sandbox.globalThis = sandbox;
    new vm.Script(jsMatch[1], { filename: "dashboard_runtime.js" }).runInNewContext(sandbox);
    const eng = sandbox.CompendiumDashboardEngine;
    if (!eng) throw new Error("CompendiumDashboardEngine non exposé");

    const ov = eng.renderOverviewHtml(payload);
    if (!ov.includes("180\u00a0000") || !ov.includes("D01") || !ov.includes("D12")) {
      throw new Error("Vue Synthèse incomplète");
    }
    const tk = eng.renderTasksHtml(payload, false, "");
    if (!tk.includes("Task 1") || !tk.includes("Task 9")) {
      throw new Error("Vue Pipeline incomplète");
    }
    const un = eng.renderUnitsHtml(payload, { domain: "ALL", type: "ALL", status: "ALL", query: "" });
    if (!un.includes("00 - Liminaire") || !un.includes("CH-36") || !un.includes("Annexe E")) {
      throw new Error("Vue Unités incomplète");
    }
    const sc = eng.renderSchemasHtml(payload, { domain: "ALL", reuse: "ALL", notation: "ALL", disk: "ALL", query: "" });
    if (!sc.includes("SCH-00-01") || !sc.includes("SCH-36-04")) {
      throw new Error("Vue Schémas incomplète");
    }
    const aq = eng.renderAqHtml(payload, { gate: "ALL", query: "" });
    if (!aq.includes("CA-01") || !aq.includes("CA-22") || !aq.includes("Barrière G5")) {
      throw new Error("Vue AQ incomplète");
    }
    const fa = eng.renderFactoryHtml(payload);
    if (!fa.includes("Compendium.pdf") || !fa.includes("AO-08")) {
      throw new Error("Vue Usine incomplète");
    }
    const insp = eng.renderInspectorHtml(payload.units[1], payload);
    if (!insp.includes("FAM_D01_01_01") || !insp.includes("SCH-01-01")) {
      throw new Error("Inspecteur CH-01 incomplet");
    }
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(INDEX_HTML_PATH)],
        input=json.dumps(payload, ensure_ascii=False),
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec Node.js dashboard :\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"
