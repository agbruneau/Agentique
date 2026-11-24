"""Suite de tests automatisés pour le document maître ``prd.md`` et son compilateur.

Vérifie :
- les fonctions unitaires de ``compiler_prd.py`` (ancres GFM, numérotation 1..36, encodage URL) ;
- la compilation sur fixture synthétique et le rejet strict des placeholders/omissions ;
- l'exhaustivité du vrai ``prd.md`` (12 domaines D01–D12, 36 chapitres 01–36, 71 familles,
  260 thèmes, 4 annexes A–D, unicité des titres/résumés, zéro placeholder/mojibake) ;
- la validité à 100 % de toutes les ancres internes ``#slug`` via parseur CommonMark strict ;
- la validité à 100 % de tous les liens relatifs vers ``Corpus/`` et la documentation du dépôt.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
CARTO_DIR = REPO_ROOT / "Cartographie"
DONNEES_DIR = CARTO_DIR / "donnees"
OUTILS_DIR = CARTO_DIR / "outils"
PRD_PATH = REPO_ROOT / "prd.md"
PRD_WEB_DATA_PATH = DONNEES_DIR / "prd-web-data.json"
PRD_WEB_HTML_PATH = CARTO_DIR / "PRD - Référentiel directeur de l'entreprise agentique.html"

sys.path.insert(0, str(OUTILS_DIR))
import compiler_prd as cp  # noqa: E402
import extraire_structure as es  # noqa: E402


def test_unit_gfm_anchor_and_chapter_numbering() -> None:
    seen: dict[str, int] = {}
    a1 = cp.gfm_anchor("Chapitre 01 — Rupture épistémique & `Systems of Agency`", seen)
    a2 = cp.gfm_anchor("Chapitre 01 — Rupture épistémique & `Systems of Agency`", seen)
    assert a1 == "chapitre-01--rupture-épistémique--systems-of-agency"
    assert a2 == f"{a1}-1"

    assert cp.expected_chapter_number("D01", "SUB_D01_01") == 1
    assert cp.expected_chapter_number("D01", "SUB_D01_03") == 3
    assert cp.expected_chapter_number("D12", "SUB_D12_03") == 36
    assert "%27" in cp.encode_rel_url("Corpus/Tome 2 - Cadre normatif et exigences d'architecture.md")
    assert cp._md_cell("a | b\nc  d") == r"a \| b c d"
    assert cp._md_cell(r"a \| b") == r"a \| b"


def test_unit_placeholder_rejection() -> None:
    with pytest.raises(ValueError, match="placeholder"):
        cp._assert_non_empty("Ceci est un TODO à compléter", "test_ctx")
    with pytest.raises(ValueError, match="vide"):
        cp._assert_non_empty("   ", "test_ctx")


def test_unit_build_prd_markdown_end_to_end_on_real_bundle() -> None:
    global_path = DONNEES_DIR / "prd_shards" / "prd-global-et-annexes.json"
    if not global_path.is_file():
        pytest.skip("prd-global-et-annexes.json absent")
    bundle = json.loads((DONNEES_DIR / "corpus-mindmap-data.json").read_text(encoding="utf-8"))
    global_shard = json.loads(global_path.read_text(encoding="utf-8"))
    nodes = bundle["nodes"]
    by_id = {n["node_id"]: n for n in nodes}

    synth_chapters = []
    for sub in sorted((n for n in nodes if n["node_kind"] == "subdomain"), key=lambda x: (x["domain_id"], x["node_id"])):
        cnum = cp.expected_chapter_number(sub["domain_id"], sub["node_id"])
        fams = []
        for fid in sub["children_ids"]:
            fnode = by_id[fid]
            thms = []
            for tid in fnode["children_ids"]:
                tnode = by_id[tid]
                thms.append({
                    "theme_node_id": tid,
                    "canonical_slug": tnode["canonical_slug"],
                    "theme_title": tnode["title"],
                    "content_specification": tnode["summary"],
                    "identifiers_and_norms": tnode.get("identifiers", []),
                })
            fams.append({
                "family_node_id": fid,
                "family_title": fnode["title"],
                "family_overview": fnode["summary"],
                "themes_targeted": thms,
            })
        synth_chapters.append({
            "chapter_number": cnum,
            "chapter_code": f"CH-{cnum:02d}",
            "domain_id": sub["domain_id"],
            "subdomain_node_id": sub["node_id"],
            "representative_title": sub["title"],
            "executive_summary": sub["summary"],
            "targeted_content": {
                "scope_and_objectives": sub["summary"],
                "key_requirements_and_objectives": ["Exigence vérifiable de test."],
                "families_and_themes": fams,
                "deliverables_and_verification": ["Critère vérifiable de test."],
                "cross_chapter_interrelations": [],
                "corpus_anchors": [],
            },
        })
    synth_chapters.sort(key=lambda x: x["chapter_number"])
    md_text, metrics = cp.build_prd_markdown(REPO_ROOT, bundle, global_shard, synth_chapters)
    assert metrics == {
        "domains": 12,
        "chapters": 36,
        "families": 71,
        "themes": 260,
        "annexes": 4,
        "lines": metrics["lines"],
        "words": metrics["words"],
    }
    assert "Annexe A — Annexe A" not in md_text
    headings, _, _ = es.parse_markdown_lines(md_text.splitlines())
    seen: dict[str, int] = {}
    anchors = {cp.gfm_anchor(t, seen) for _, _, t in headings}
    for anc in re.findall(r"\]\(#([^)]+)\)", md_text):
        assert anc in anchors, f"Ancre cassée dans fixture PRD : #{anc}"


def test_prd_compiled_exhaustiveness_and_anchors() -> None:
    if not PRD_PATH.is_file():
        pytest.skip("prd.md pas encore compilé (en attente des shards PRD)")

    bundle = json.loads((DONNEES_DIR / "corpus-mindmap-data.json").read_text(encoding="utf-8"))
    prd_text = PRD_PATH.read_text(encoding="utf-8")
    prd_lines = prd_text.splitlines()

    # 0 mojibake / placeholder / dict Python brut (hors mention réglementaire BSIF B-15 SRC-067)
    for pat in cp.PLACEHOLDER_PATTERNS:
        bad_lines = [
            (idx, ln)
            for idx, ln in enumerate(prd_lines, 1)
            if pat.search(ln)
            and not (pat.pattern == r"\bTBD\b" and "ligne directrice B-15 du BSIF" in ln and "SRC-067" in ln)
        ]
        assert not bad_lines, f"Placeholder détecté dans prd.md ({pat.pattern}) : {bad_lines[:3]}"
    assert not re.search(r"\{'[A-Za-z0-9_]+'\s*:", prd_text), "Dict Python brut détecté dans prd.md"
    assert "\ufffd" not in prd_text

    # Extraction stricte CommonMark de TOUS les titres H1..H6 de prd.md
    headings, _, code_lines = es.parse_markdown_lines(prd_lines)
    assert len(headings) > 150

    seen: dict[str, int] = {}
    heading_anchors: set[str] = set()
    h2_titles: list[str] = []
    h3_titles: list[str] = []
    h4_titles: list[str] = []
    h5_titles: list[str] = []
    for _, lvl, title in headings:
        anc = cp.gfm_anchor(title, seen)
        heading_anchors.add(anc)
        if lvl == 2:
            h2_titles.append(title)
        elif lvl == 3:
            h3_titles.append(title)
        elif lvl == 4:
            h4_titles.append(title)
        elif lvl == 5:
            h5_titles.append(title)

    # 12 Parties + 4 Annexes + TDM + Sommaire exécutif
    parties_h2 = [t for t in h2_titles if t.startswith("Partie ")]
    annexes_h2 = [t for t in h2_titles if t.startswith("Annexe ")]
    assert len(parties_h2) == 12
    assert len(annexes_h2) == 4
    assert len(set(parties_h2)) == 12
    assert len(set(annexes_h2)) == 4

    # 36 Chapitres uniques + 36 Résumés + 36 Descriptifs + 71 Familles
    chapters_h3 = [t for t in h3_titles if re.match(r"^Chapitre \d{2} — ", t)]
    assert len(chapters_h3) == 36
    assert len(set(chapters_h3)) == 36
    for i in range(1, 37):
        assert any(t.startswith(f"Chapitre {i:02d} — ") for t in chapters_h3)
        assert f"{i:02d}.1 Résumé" in h4_titles
        assert f"{i:02d}.2 Descriptif du contenu ciblé" in h4_titles

    fam_h5 = [t for t in h5_titles if re.match(r"^\d{2}\.2\.\d+ ", t)]
    assert len(fam_h5) == 71

    # Couverture 100 % des 12 domaines, 36 sous-domaines, 71 familles et 260 thèmes du MindMap
    for node in bundle["nodes"]:
        kind = node["node_kind"]
        if kind in ("domain", "subdomain", "family"):
            assert node["node_id"] in prd_text, f"Identifiant MindMap manquant dans prd.md : {node['node_id']}"
        elif kind == "theme":
            assert node["node_id"] in prd_text, f"Thème manquant dans prd.md : {node['node_id']}"
            assert node["canonical_slug"] in prd_text, f"Slug manquant dans prd.md : {node['canonical_slug']}"

    # Validation 100 % des ancres internes #slug et liens relatifs dans prd.md (hors code)
    line_counts_cache: dict[Path, int] = {}
    md_link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    internal_checked = 0
    file_checked = 0
    for idx, line in enumerate(prd_lines, 1):
        if idx in code_lines:
            continue
        for target in md_link_re.findall(line):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                anc = target[1:]
                assert anc in heading_anchors, f"Ancre interne cassée à prd.md L{idx} : #{anc}"
                internal_checked += 1
            else:
                rel_part, _, frag = target.partition("#")
                target_path = (PRD_PATH.parent / unquote(rel_part)).resolve()
                assert target_path.exists(), f"Lien relatif cassé à prd.md L{idx} : {target}"
                if frag.startswith("L") and frag[1:].isdigit():
                    ln = int(frag[1:])
                    if target_path not in line_counts_cache:
                        line_counts_cache[target_path] = len(target_path.read_text(encoding="utf-8").splitlines())
                    assert 1 <= ln <= line_counts_cache[target_path], (
                        f"Numéro de ligne hors bornes à prd.md L{idx} : {target}"
                    )
                file_checked += 1

    assert internal_checked >= 200
    assert file_checked >= 200

    # Cohérence du nombre de colonnes de tous les tableaux Markdown GFM (hors blocs de code)
    def _table_col_count(row_line: str) -> int:
        stripped = row_line.strip()
        if stripped.startswith("|"):
            stripped = stripped[1:]
        if stripped.endswith("|") and not stripped.endswith("\\|"):
            stripped = stripped[:-1]
        return len(re.split(r"(?<!\\)\|", stripped))

    sep_re = re.compile(r"^\s*\|?[\s:-]+(?:\|[\s:-]+)+\|?\s*$")
    tables_checked = 0
    idx_line = 0
    while idx_line < len(prd_lines):
        ln_cur = prd_lines[idx_line]
        if (
            (idx_line + 1) not in code_lines
            and ln_cur.strip().startswith("|")
            and idx_line + 1 < len(prd_lines)
            and sep_re.match(prd_lines[idx_line + 1])
        ):
            tables_checked += 1
            hdr_cols = _table_col_count(ln_cur)
            assert _table_col_count(prd_lines[idx_line + 1]) == hdr_cols, (
                f"Séparateur incohérent à prd.md L{idx_line + 2}"
            )
            row_idx = idx_line + 2
            while row_idx < len(prd_lines) and (row_idx + 1) not in code_lines and prd_lines[row_idx].strip().startswith("|"):
                assert _table_col_count(prd_lines[row_idx]) == hdr_cols, (
                    f"Tableau Markdown cassé à prd.md L{row_idx + 1} (attendu {hdr_cols} colonnes)"
                )
                row_idx += 1
            idx_line = row_idx
        else:
            idx_line += 1
    assert tables_checked >= 40

    # Exhaustivité Annexe B (toutes les tensions d'arbitrage) & Annexe D (toutes familles + C01–C40)
    expected_tensions = sum(1 for r in bundle["relations"] if r["type"] == "tension_arbitrage")
    t_idx = next(
        i for i, ln in enumerate(prd_lines) if ln.startswith("#### Tensions d'arbitrage structurantes")
    )
    t_rows = []
    for ln in prd_lines[t_idx + 4 :]:
        if not ln.startswith("|"):
            break
        t_rows.append(ln)
    assert len(t_rows) == expected_tensions

    ann_d_pos = prd_text.index("## Annexe D — ")
    ann_d_text = prd_text[ann_d_pos:]
    for expected_tok in ("C40 (", "PEX (", "EXIG (", "CAP (", "PRR-75 (", "5 SBB (", "ADR_TEMPLATE ("):
        assert expected_tok in ann_d_text, f"Famille absente de l'Annexe D : {expected_tok}"
    assert "40` critères `C01–C40`" in ann_d_text
    assert "`BLOQUANT` : `18`" in ann_d_text
    assert "`OBLIGATOIRE` : `15`" in ann_d_text
    assert "`RECOMMANDE` : `7`" in ann_d_text

    # Phase 2 : Hygiène typographique, LF strict, 0 troncature, parité Annexe C & D
    assert b"\r\n" not in PRD_PATH.read_bytes(), "Séquences CRLF détectées dans prd.md"
    for bad_trunc in ("*(+", "28 autres non listées", "L'extrait ci-dessus"):
        assert bad_trunc not in prd_text, f"Troncature résiduelle dans prd.md : {bad_trunc}"
    assert r"\\$" not in prd_text, r"Double-échappement \\$ détecté dans prd.md"
    assert "Thème local" not in prd_text, "Préfixe hétérogène 'Thème local' dans Interrelations"

    bad_dollars: list[tuple[int, str]] = []
    bad_arrows: list[tuple[int, str]] = []
    bad_ranges: list[tuple[int, str]] = []
    bad_backticks_tok: list[tuple[int, str]] = []
    for lno, raw_ln in enumerate(prd_lines, 1):
        if lno in code_lines:
            continue
        no_inline = re.sub(r"`[^`]+`", "", raw_ln)
        if re.search(r"(?<!\\)\$", no_inline):
            bad_dollars.append((lno, raw_ln[:80]))
        if "<->" in no_inline or re.search(r"(?<![<=-])->(?![>=])", no_inline):
            bad_arrows.append((lno, raw_ln[:80]))
        if re.search(r"\bL\d+-L?\d+\b", no_inline):
            bad_ranges.append((lno, raw_ln[:80]))
        for kw in ("strict: true", "additionalProperties: false", "Status: Accepted", "Status: Final"):
            if kw in no_inline:
                bad_backticks_tok.append((lno, kw))
        for bad_acc in ("(reglementation)", "(marche)"):
            assert bad_acc not in no_inline, f"Accent manquant à L{lno} : {bad_acc}"
    assert not bad_dollars, f"$ non échappé hors code dans prd.md : {bad_dollars[:3]}"
    assert not bad_arrows, f"Flèche ASCII ->/<-> hors code dans prd.md : {bad_arrows[:3]}"
    assert not bad_ranges, f"Plage Lxxx-Lyyy sans tiret demi-cadratin dans prd.md : {bad_ranges[:3]}"
    assert not bad_backticks_tok, f"Jeton technique sans backticks dans prd.md : {bad_backticks_tok[:3]}"

    # Annexe C : 86 jalons consolidés sans doubles parenthèses DAPP
    ann_c_idx = next(i for i, ln in enumerate(prd_lines) if ln.startswith("#### Jalons chronologiques consolidés"))
    assert "86 jalons" in prd_lines[ann_c_idx]
    ann_c_rows = []
    for ln in prd_lines[ann_c_idx + 4 :]:
        if not ln.startswith("|"):
            break
        date_cell = ln.split("|")[1].strip().strip("`")
        assert "((" not in date_cell and "))" not in date_cell, f"Parenthèses doubles DAPP dans date Annexe C : {ln}"
        ann_c_rows.append(ln)
    assert len(ann_c_rows) == 86

    # Annexe D : 237 entrées uniques sans identifiant dupliqué
    ann_d_mat_idx = next(i for i, ln in enumerate(prd_lines) if ln.startswith("#### Matrice intégrale de traçabilité"))
    assert "237 entrées uniques" in prd_lines[ann_d_mat_idx]
    ann_d_ids: list[str] = []
    for ln in prd_lines[ann_d_mat_idx + 4 :]:
        if not ln.startswith("|"):
            break
        first_cell = ln.split("|")[1].strip().strip("`")
        ann_d_ids.append(first_cell)
    assert len(ann_d_ids) == 237
    assert len(set(ann_d_ids)) == 237


def test_prd_links_in_readmes_valid() -> None:
    if not PRD_PATH.is_file():
        pytest.skip("prd.md pas encore compilé")
    assert "PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html" in PRD_PATH.read_text(encoding="utf-8")
    for md_path in (REPO_ROOT / "README.md", CARTO_DIR / "README.md", REPO_ROOT / "Corpus" / "README.md"):
        content = md_path.read_text(encoding="utf-8")
        assert b"\r\n" not in md_path.read_bytes(), f"CRLF détecté dans {md_path}"
        assert "prd.md" in content, f"Lien vers prd.md manquant dans {md_path}"
        assert "PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html" in content, f"Lien PRD Web manquant dans {md_path}"
        for raw_target in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)", content):
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = (md_path.parent / unquote(raw_target)).resolve()
            assert target_path.exists(), f"Lien cassé dans {md_path}: {raw_target}"

    # Parité exacte des métriques documentées dans Cartographie/README.md
    carto_readme = (CARTO_DIR / "README.md").read_text(encoding="utf-8")
    prd_text = PRD_PATH.read_text(encoding="utf-8")
    prd_lines_cnt = len(prd_text.splitlines())
    prd_words_cnt = len(prd_text.split())
    mm_bytes = (CARTO_DIR / "MindMap - Cartographie thématique du Corpus.html").stat().st_size
    pw_bytes = PRD_WEB_HTML_PATH.stat().st_size
    assert f"`{prd_lines_cnt:,}".replace(",", " ") in carto_readme
    assert f"`{prd_words_cnt:,}".replace(",", " ") in carto_readme
    assert f"`{mm_bytes:,}".replace(",", " ") in carto_readme
    assert f"`{pw_bytes:,}".replace(",", " ") in carto_readme
    assert "`86` jalons" in carto_readme
    assert "`237` entrées uniques" in carto_readme


def test_prd_web_data_json_and_parity() -> None:
    assert PRD_WEB_DATA_PATH.is_file()
    data = json.loads(PRD_WEB_DATA_PATH.read_text(encoding="utf-8"))
    assert len(data["executive_summary"]["sections"]) == 5
    assert data["executive_summary"]["sections"][3]["kpi_table"] is not None
    assert len(data["parties"]) == 12
    assert len(data["chapters"]) == 36
    assert len(data["annexes"]) == 4

    fams = [f for ch in data["chapters"] for f in ch["targeted_content"]["families_and_themes"]]
    thms = [t for f in fams for t in f["themes_targeted"]]
    assert len(fams) == 71
    assert len(thms) == 260

    ann_b = next(a for a in data["annexes"] if a["annexe_code"] == "B")
    ann_c = next(a for a in data["annexes"] if a["annexe_code"] == "C")
    ann_d = next(a for a in data["annexes"] if a["annexe_code"] == "D")
    assert len(ann_b["tensions"]) == 62
    assert len(ann_c["reconciliations"]) == 5
    assert len(ann_c["timeline"]) == 86
    assert len(ann_d["matrix_all"]) == 237
    assert len({x["id"] for x in ann_d["matrix_all"]}) == 237
    assert ann_d.get("matrix_totals") == {
        "unique_entries": 237,
        "tome8_executable_tests": 95,
        "shared_ids_merged": 30,
    }
    raw_web_json = PRD_WEB_DATA_PATH.read_text(encoding="utf-8")
    assert r"\$" not in raw_web_json
    prd_text = PRD_PATH.read_text(encoding="utf-8")
    prd_lines = prd_text.splitlines()
    prd_headings, _, _ = es.parse_markdown_lines(prd_lines)
    assert data["meta"]["line_count"] == len(prd_lines)
    assert data["meta"]["word_count"] == len(prd_text.split())
    assert data["meta"]["heading_count"] == len(prd_headings)
    assert ann_d["blueprints_c40"]["c40_breakdown"] == {
        "total": 40,
        "BLOQUANT": 18,
        "OBLIGATOIRE": 15,
        "RECOMMANDE": 7,
    }
    assert len(data["lookup"]["node_id_to_prd"]) == 379
    assert len(data["lookup"]["slug_to_chapter"]) == 260
    assert len(data["lookup"]["domain_to_part"]) == 12
    assert len(data["lookup"]["unit_id_to_chapter"]) >= 250


def test_prd_web_standalone_html_and_nodejs_smoke() -> None:
    assert PRD_WEB_HTML_PATH.is_file()
    assert b"\r\n" not in PRD_WEB_HTML_PATH.read_bytes(), "CRLF détecté dans PRD Web HTML"
    html = PRD_WEB_HTML_PATH.read_text(encoding="utf-8")
    assert "__PRD_DATA_JSON__" not in html

    json_match = re.search(
        r'<script[^>]*id="prd-web-data"[^>]*>([\s\S]*?)</script>', html
    )
    assert json_match is not None
    embedded_raw = json_match.group(1)
    assert "</" not in embedded_raw
    assert "<!--" not in embedded_raw
    assert "\u2028" not in embedded_raw
    assert "\u2029" not in embedded_raw
    parsed = json.loads(embedded_raw)
    assert len(parsed["chapters"]) == 36

    html_without_json = html[: json_match.start(1)] + html[json_match.end(1) :]
    assert not re.search(r"<script[^>]+src\s*=", html_without_json, re.IGNORECASE)
    assert not re.search(r"@import\s+url\(", html_without_json, re.IGNORECASE)
    assert not re.search(r"\bfetch\s*\(", html_without_json)
    assert "http://" not in html_without_json
    assert "https://" not in html_without_json

    node_exe = shutil.which("node")
    if node_exe is None:
        pytest.skip("Node.js non disponible dans l'environnement")

    node_script = r"""
    const fs = require("fs");
    const vm = require("vm");
    const html = fs.readFileSync(process.argv[1], "utf8");
    const jsonMatch = html.match(/<script[^>]*id="prd-web-data"[^>]*>([\s\S]*?)<\/script>/);
    const jsMatch = html.match(/<script(?![^>]*type="application\/json")[^>]*>([\s\S]*?)<\/script>/);
    if (!jsonMatch || !jsMatch) throw new Error("Blocs JSON/JS introuvables dans PRD Web HTML");

    const sandbox = {
      console, Set, Map, Object, Array, Math, String, Number, Boolean, Date, RegExp, JSON,
      encodeURIComponent, decodeURIComponent, globalThis: {}
    };
    sandbox.globalThis = sandbox;
    new vm.Script(jsMatch[1], { filename: "prd_web_runtime.js" }).runInNewContext(sandbox);

    const eng = sandbox.PrdWebEngine;
    if (!eng) throw new Error("PrdWebEngine non exposé");
    const data = JSON.parse(jsonMatch[1]);
    const idx = eng.buildIndexes(data);
    if (idx.parties.length !== 12 || idx.chapters.length !== 36 || idx.annexes.length !== 4) {
      throw new Error("Cardinaux index PrdWebEngine invalides");
    }

    const sHits = eng.searchPrd(idx, "Lusser", 10);
    if (sHits.length === 0) throw new Error("searchPrd('Lusser') vide");
    const fRes = eng.filterPrd(idx, { domain: "D07" });
    if (!fRes.active || fRes.counts.chapters !== 3) {
      throw new Error("filterPrd D07 invalide: " + JSON.stringify(fRes.counts));
    }
    const mmUrl = eng.mindmapHref("mindmap", "THM_loi-de-lusser");
    if (!mmUrl.includes("MindMap%20-") || !mmUrl.includes("#view=mindmap&node=THM_loi-de-lusser")) {
      throw new Error("mindmapHref invalide: " + mmUrl);
    }
    const parsedThm = eng.parseHash("#thm=loi-de-lusser", idx);
    if (!parsedThm || parsedThm.kind !== "chapter" || Number(parsedThm.chapterNumber) !== 2) {
      throw new Error("parseHash #thm=loi-de-lusser invalide: " + JSON.stringify(parsedThm));
    }
    const corpUrl = eng.corpusHref("Corpus/Tome 2 - Cadre normatif et exigences d'architecture.md", 709);
    if (!corpUrl.includes("%27") || !corpUrl.endsWith("#L709")) {
      throw new Error("corpusHref PRD Web invalide: " + corpUrl);
    }

    const toc = eng.renderTocHtml(idx, "", { tocExpanded: new Set(), target: { kind: "exec" } }, { active: false });
    if (!toc.html || toc.count < 12) throw new Error("renderTocHtml insuffisant");
    const fullHtml = eng.renderContentHtml(idx, { mode: "full", target: { kind: "exec" }, filters: {}, highlightQuery: "" }, { active: false, counts: { themes: 260, chapters: 36, parties: 12 } });
    for (const marker of ["Partie I", "Partie XII", "Chapitre 01", "Chapitre 36", "Annexe A", "Annexe D", "THM_loi-de-lusser"]) {
      if (!fullHtml.includes(marker)) throw new Error("Contenu mode intégral PrdWebEngine incomplet: " + marker);
    }
    // Phase 2 : Zéro backtick brut hors <code>, 0 **gras** brut, 0 \$ littéral, 0 <em> brisé sur gen_ai.*
    const noCodeTags = fullHtml.replace(/<code[^>]*>[\s\S]*?<\/code>/gi, "");
    if (noCodeTags.includes("`")) throw new Error("Backtick brut détecté hors <code> dans PRD Web HTML");
    if (/(^|[\s(>])\*\*[^\s*](?:[^*\n]*?[^\s*])?\*\*(?=[\s.,;:!?<)]|$)/.test(noCodeTags)) {
      throw new Error("**gras** brut détecté dans PRD Web HTML");
    }
    if (/<strong>\s*et tests\//i.test(fullHtml)) {
      throw new Error("Glob specs/** transformé en <strong> par erreur");
    }
    if (fullHtml.includes("\\$")) throw new Error("Literal backslash-dollar dans PRD Web HTML");
    if (/<em>[^<]*gen_ai\.[^<]*<\/em>/i.test(fullHtml)) throw new Error("<em> brisé autour de gen_ai.* dans PRD Web HTML");

    const inlineSample = eng.renderInlineMd("attributs gen_ai.* et *Cost-per-Outcome* + `strict: true`");
    if (!inlineSample.includes("gen_ai.* et <em>Cost-per-Outcome</em>") || !inlineSample.includes("<code")) {
      throw new Error("renderInlineMd défaillant sur gen_ai.* : " + inlineSample);
    }
    const hSec02 = eng.parseHash("#sec=02", idx);
    if (!hSec02 || hSec02.kind !== "exec" || hSec02.sectionId !== "exec-02") {
      throw new Error("parseHash #sec=02 invalide: " + JSON.stringify(hSec02));
    }
    const hPart07 = eng.parseHash("#part=part-07", idx);
    if (!hPart07 || hPart07.kind !== "part" || hPart07.domainId !== "D07") {
      throw new Error("parseHash #part=part-07 invalide: " + JSON.stringify(hPart07));
    }

    // Smoke mountApp avec stub DOM léger et hash #part=part-07
    const stubEls = {};
    const makeStubEl = (id) => ({
      id, textContent: "", innerHTML: "", value: "", style: {},
      classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
      setAttribute(k, v) { this["attr_" + k] = v; },
      getAttribute(k) { return this["attr_" + k] ?? null; },
      appendChild(){}, addEventListener(){}, scrollIntoView(){}, focus(){}, querySelector: () => null, querySelectorAll: () => []
    });
    for (const k of ["prd-web-data", "prd-global-title", "prd-global-meta", "prd-kpi-strip", "prd-content", "prd-toc-tree", "prd-toc-count", "prd-open-mindmap-link", "prd-filter-summary"]) {
      stubEls[k] = makeStubEl(k);
    }
    stubEls["prd-web-data"].textContent = jsonMatch[1];
    const docStub = {
      documentElement: makeStubEl("html"),
      body: makeStubEl("body"),
      getElementById: (id) => stubEls[id] || null,
      createElement: (tag) => makeStubEl(tag),
      addEventListener(){}, querySelector: () => null, querySelectorAll: () => []
    };
    const appInst = eng.mountApp(docStub, { location: { hash: "#part=part-07" }, addEventListener(){} });
    if (!appInst || appInst.getState().target.domainId !== "D07" || !stubEls["prd-content"].innerHTML.includes("Partie VII")) {
      throw new Error("mountApp smoke #part=part-07 échoué");
    }
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(PRD_WEB_HTML_PATH)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec Node.js PRD Web:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"
