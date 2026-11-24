"""Suite de tests automatisés pour la cartographie interactive du Corpus Agentique.

Couvre :
- l'extraction structurelle CommonMark stricte des 9 fichiers Markdown de ``Corpus/`` ;
- l'absence de faux positifs dans les blocs de code clôturés (dont Tome 3) ;
- l'intégrité du graphe transversal (12 domaines, 8 types de relations, 0 arête cassée, 0 chapitre orphelin) ;
- l'échappement sûr du JSON embarqué dans ``<script>`` et l'autonomie ``file://`` stricte (0 CDN / requête réseau) ;
- la validité de tous les liens relatifs URL-encodés ;
- la validation syntaxique (``vm.Script``) et fonctionnelle sous ``Node.js`` sur le vrai HTML compilé.
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

REPO_ROOT = Path(__file__).resolve().parents[3]
CARTO_DIR = REPO_ROOT / "Compendium" / "Cartographie"
DONNEES_DIR = CARTO_DIR / "donnees"
OUTILS_DIR = CARTO_DIR / "outils"
HTML_PATH = CARTO_DIR / "MindMap - Cartographie thématique du Corpus.html"

sys.path.insert(0, str(OUTILS_DIR))
import compiler_mindmap as cm  # noqa: E402
import extraire_structure as es  # noqa: E402


def _walk_struct_tree(nodes: list[dict]) -> list[dict]:
    out: list[dict] = []
    for n in nodes:
        out.append(n)
        out.extend(_walk_struct_tree(n.get("children", [])))
    return out


# ---------------------------------------------------------------------------
# 1. Tests unitaires du parseur CommonMark et de l'échappement HTML/JS
# ---------------------------------------------------------------------------
def test_commonmark_fenced_code_strict_parser() -> None:
    sample = [
        "# Vrai titre 1",
        "```python",
        "# commentaire python",
        "## faux titre",
        "```",
        "````markdown",
        "```bash",
        "# commentaire dans bloc imbriqué 4 backticks",
        "```",
        "# encore dans le bloc 4 backticks",
        "````",
        "~~~yaml",
        "# commentaire tilde",
        "~~~ non-fermeture car info",
        "# toujours dans tilde",
        "~~~~",
        "## Vrai titre 2 ###",
        "### C#",
        "    # bloc indenté 4 espaces ignoré",
        "#hashtag_sans_espace",
    ]
    headings, blocks, _ = es.parse_markdown_lines(sample)
    assert headings == [
        (1, 1, "Vrai titre 1"),
        (17, 2, "Vrai titre 2"),
        (18, 3, "C#"),
    ]
    assert len(blocks) == 3
    assert blocks[1].fence_length == 4
    assert blocks[2].fence_char == "~"


def test_commonmark_backtick_info_string_cannot_contain_backticks() -> None:
    sample = [
        "```foo`bar",
        "# Vrai titre car ligne précédente est du texte inline",
    ]
    headings, blocks, _ = es.parse_markdown_lines(sample)
    assert len(blocks) == 0
    assert headings == [(2, 1, "Vrai titre car ligne précédente est du texte inline")]


def test_script_json_escaping_safety() -> None:
    payload = {"text": "</script><script>alert(1)</script><!--x-->\u2028\u2029"}
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    escaped = cm.escape_json_for_script(raw)
    assert "</" not in escaped
    assert "<!--" not in escaped
    assert "\u2028" not in escaped
    assert "\u2029" not in escaped
    assert json.loads(escaped) == payload


# ---------------------------------------------------------------------------
# 2. Tests d'extraction sur les 9 fichiers réels de Corpus/
# ---------------------------------------------------------------------------
def test_structure_covers_all_9_corpus_files_accurately() -> None:
    struct_path = DONNEES_DIR / "structure-integrale.json"
    assert struct_path.is_file()
    data = json.loads(struct_path.read_text(encoding="utf-8"))

    assert data["totals"]["files"] == 9
    assert len(data["files"]) == 9

    expected_tomes = ["R", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
    assert [f["tome_id"] for f in data["files"]] == expected_tomes

    total_lines = 0
    total_words = 0
    total_headings = 0
    for fmeta in data["files"]:
        md_path = REPO_ROOT / fmeta["file"]
        assert md_path.is_file()
        raw_text = md_path.read_text(encoding="utf-8")
        assert fmeta["line_count"] == len(raw_text.splitlines())
        assert fmeta["word_count"] == len(raw_text.split())
        flat = _walk_struct_tree(fmeta["tree"])
        assert len(flat) == fmeta["heading_count"]
        total_lines += fmeta["line_count"]
        total_words += fmeta["word_count"]
        total_headings += len(flat)

    assert data["totals"]["lines"] == total_lines
    assert data["totals"]["words"] == total_words
    assert data["totals"]["headings"] == total_headings
    assert total_headings >= 4000


def test_tome3_code_fence_hash_lines_excluded() -> None:
    struct_path = DONNEES_DIR / "structure-integrale.json"
    data = json.loads(struct_path.read_text(encoding="utf-8"))
    t3 = next(f for f in data["files"] if f["tome_id"] == "T3")
    t3_heading_lines = {n["line_start"] for n in _walk_struct_tree(t3["tree"])}

    forbidden_code_hash_lines = {
        2632,
        3436,
        4890,
        4895,
        4900,
        4907,
        15867,
        15876,
        16733,
        16740,
        16741,
        16742,
        16928,
        17590,
    }
    assert t3_heading_lines.isdisjoint(forbidden_code_hash_lines)


# ---------------------------------------------------------------------------
# 3. Tests d'intégrité du graphe transversal et du bundle compilé
# ---------------------------------------------------------------------------
def test_bundle_graph_referential_and_coverage_integrity() -> None:
    bundle_path = DONNEES_DIR / "corpus-mindmap-data.json"
    assert bundle_path.is_file()
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    schema = bundle["schema"]
    nodes = bundle["nodes"]
    relations = bundle["relations"]
    chapters = bundle["chapters"]

    node_by_id = {n["node_id"]: n for n in nodes}
    node_by_slug = {n["canonical_slug"]: n for n in nodes if n.get("canonical_slug")}
    valid_rel_types = {rt["type_id"] for rt in schema["relation_types"]}
    expected_domains = {d["domain_id"] for d in schema["domains"]}

    # 12 domaines couverts
    theme_nodes = [n for n in nodes if n["node_kind"] == "theme"]
    assert len(theme_nodes) >= 200
    assert expected_domains.issubset({n["domain_id"] for n in theme_nodes})

    # Hiérarchie 5 niveaux sans nœud orphelin
    for n in nodes:
        assert 0 <= n["depth"] <= 4
        if n["depth"] > 0:
            assert n["parent_id"] in node_by_id

    # 0 arête cassée, 0 auto-boucle, type canonique, justification non vide
    assert len(relations) >= 400
    for rel in relations:
        assert rel["source"] in node_by_id
        assert rel["target"] in node_by_id
        assert rel["source"] != rel["target"]
        assert rel["type"] in valid_rel_types
        assert str(rel.get("justification", "")).strip() != ""

    # 0 chapitre sans thème rattaché & 9 fichiers couverts
    assert len(chapters) >= 250
    covered_tomes = {c["tome_id"] for c in chapters}
    assert covered_tomes == {"R", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"}
    for ch in chapters:
        themes_addr = ch.get("themes_addressed", [])
        assert len(themes_addr) >= 1
        assert any(slug in node_by_slug for slug in themes_addr)

    # Validité des plages de lignes sur chaque occurrence
    line_limits = {f["file"]: f["line_count"] for f in bundle["structure"]["files"]}
    for n in theme_nodes:
        for occ in n.get("occurrences", []):
            assert occ["file"] in line_limits
            assert 1 <= occ["line_start"] <= occ["line_end"] <= line_limits[occ["file"]]

    # Pivots de concordance (5 discordances, DIV-02, chronologie, traçabilité)
    pivots = bundle["pivots"]
    assert pivots["div_02"] is not None
    assert len(pivots["reconciliations"]) == 5
    assert len(pivots["timeline"]) == 86
    assert len(pivots["traceability_matrix"]) == 237
    assert len({x["id"] for x in pivots["traceability_matrix"]}) == 237
    assert pivots.get("matrix_totals") == {
        "unique_entries": 237,
        "tome8_executable_tests": 95,
        "shared_ids_merged": 30,
    }
    bundle_raw = bundle_path.read_text(encoding="utf-8")
    assert r"\$" not in bundle_raw
    assert "AE <-> AS" not in bundle_raw
    for jf in sorted(DONNEES_DIR.rglob("*.json")):
        assert b"\r\n" not in jf.read_bytes(), f"CRLF résiduel dans {jf}"

    def _has_backtick_key(obj: object) -> list[str]:
        bad: list[str] = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if "`" in str(k):
                    bad.append(str(k))
                bad.extend(_has_backtick_key(v))
        elif isinstance(obj, list):
            for it in obj:
                bad.extend(_has_backtick_key(it))
        return bad

    pivots_raw = json.loads((DONNEES_DIR / "pivots-concordance.json").read_text(encoding="utf-8"))
    assert not _has_backtick_key(pivots_raw), "Clé littérale avec backtick dans pivots-concordance.json"
    prd_web_path = DONNEES_DIR / "prd-web-data.json"
    if prd_web_path.is_file():
        assert bundle["prd"] == json.loads(prd_web_path.read_text(encoding="utf-8"))
    assert b"\r\n" not in HTML_PATH.read_bytes(), "CRLF détecté dans MindMap HTML"

    # Intégration PRD Web (Vue 5 & lookup 379 nœuds + 290 unit_id)
    prd = bundle.get("prd") or {}
    assert len(prd.get("parties", [])) == 12
    assert len(prd.get("chapters", [])) == 36
    assert len(prd.get("annexes", [])) == 5
    lookup = prd.get("lookup") or {}
    assert len(lookup.get("node_id_to_prd", {})) == 379
    assert len(lookup.get("slug_to_chapter", {})) == 260
    assert len(lookup.get("domain_to_part", {})) == 12
    assert len(lookup.get("unit_id_to_chapter", {})) >= 250


# ---------------------------------------------------------------------------
# 4. Tests du fichier HTML autonome et des liens relatifs Markdown
# ---------------------------------------------------------------------------
def test_html_standalone_no_external_cdn_and_safe_json() -> None:
    assert HTML_PATH.is_file()
    html = HTML_PATH.read_text(encoding="utf-8")

    assert "__CORPUS_DATA_JSON__" not in html
    assert "__PAGE_TITLE__" not in html

    # Extraction de la partie hors JSON embarqué pour vérifier l'absence de CDN/fetch/@import
    json_match = re.search(
        r'<script[^>]*id="corpus-mindmap-data"[^>]*>([\s\S]*?)</script>', html
    )
    assert json_match is not None
    embedded_raw = json_match.group(1)
    assert "</" not in embedded_raw
    assert "<!--" not in embedded_raw
    assert "\u2028" not in embedded_raw
    assert "\u2029" not in embedded_raw
    assert 'data-view="prd"' in html
    assert "5 · PRD Maître" in html
    parsed = json.loads(embedded_raw)
    assert parsed["totals"]["files"] == 9

    html_without_json = html[: json_match.start(1)] + html[json_match.end(1) :]
    assert not re.search(r"<script[^>]+src\s*=", html_without_json, re.IGNORECASE)
    assert not re.search(r"<link[^>]+href\s*=\s*['\"]?https?://", html_without_json, re.IGNORECASE)
    assert not re.search(r"@import\s+url\(", html_without_json, re.IGNORECASE)
    assert not re.search(r"\bfetch\s*\(", html_without_json)
    assert "http://" not in html_without_json
    assert "https://" not in html_without_json


def test_markdown_relative_links_valid() -> None:
    md_files = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "Corpus" / "README.md",
        REPO_ROOT / "Compendium" / "README.md",
        CARTO_DIR / "README.md",
    ]
    link_re = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
    for md_path in md_files:
        assert md_path.is_file()
        content = md_path.read_text(encoding="utf-8")
        checked = 0
        for raw_target in link_re.findall(content):
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = (md_path.parent / unquote(raw_target)).resolve()
            assert target_path.exists(), f"Lien cassé dans {md_path}: {raw_target}"
            checked += 1
        assert checked >= 2


# ---------------------------------------------------------------------------
# 5. Validation syntaxique et smoke-test fonctionnel Node.js sur le vrai HTML
# ---------------------------------------------------------------------------
def test_nodejs_syntax_and_functional_smoke() -> None:
    node_exe = shutil.which("node")
    if node_exe is None:
        pytest.skip("Node.js non disponible dans l'environnement")

    node_script = """
    const fs = require("fs");
    const vm = require("vm");
    const html = fs.readFileSync(process.argv[1], "utf8");
    const jsonMatch = html.match(/<script[^>]*id="corpus-mindmap-data"[^>]*>([\\s\\S]*?)<\\/script>/);
    if (!jsonMatch) throw new Error("JSON embarqué introuvable");
    const data = JSON.parse(jsonMatch[1]);
    const jsMatch = html.match(/<script(?![^>]*type="application\\/json")[^>]*>([\\s\\S]*?)<\\/script>/);
    if (!jsMatch) throw new Error("Bloc JS introuvable");

    const sandbox = {
      console, Set, Map, Object, Array, Math, String, Number, Boolean, Date, RegExp, JSON,
      encodeURIComponent, globalThis: {}
    };
    sandbox.globalThis = sandbox;
    new vm.Script(jsMatch[1], { filename: "mindmap_runtime.js" }).runInNewContext(sandbox);

    const eng = sandbox.CartographieEngine;
    if (!eng) throw new Error("CartographieEngine non exposé");
    const idx = eng.buildIndexes(data);
    idx.schema = data.schema || {};

    if (idx.nodes.length < 300) throw new Error("Nombre de nœuds insuffisant: " + idx.nodes.length);
    if (idx.relations.length < 400) throw new Error("Nombre de relations insuffisant: " + idx.relations.length);
    if (idx.structFlat.length < 4000) throw new Error("Titres H1-H6 insuffisants: " + idx.structFlat.length);

    const s1 = eng.searchCorpus(idx, "Lusser", 10);
    if (s1.length === 0) throw new Error("Recherche 'Lusser' vide");
    const s2 = eng.searchCorpus(idx, "EXIG-MCP-15", 10);
    if (s2.length === 0) throw new Error("Recherche 'EXIG-MCP-15' vide");

    const filtered = eng.filterNodesAndRelations(idx, { domain: "D07", tome: "T8" });
    if (filtered.matchingNodeIds.size === 0) throw new Error("Filtrage D07+T8 vide");

    const nA = idx.nodes.find(n => n.canonical_slug === "loi-de-lusser");
    const nB = idx.nodes.find(n => n.canonical_slug === "trousse-executable-tome-8");
    const pathRes = eng.findShortestPath(idx, nA.node_id, nB.node_id, idx.relations, false);
    if (!pathRes.found || pathRes.hops.length === 0) throw new Error("Plus court chemin A->B introuvable");

    const visDepth1 = new Set(idx.nodes.filter(n => n.depth <= 1).map(n => n.node_id));
    const bundles = eng.projectRelationsToVisible(idx.relations, visDepth1, idx.nodeById);
    if (bundles.length === 0) throw new Error("Projection sur ancêtre visible vide");

    const matDom = eng.computeConcordanceMatrix(idx, "domain");
    const matSub = eng.computeConcordanceMatrix(idx, "subdomain");
    if (matDom.rows.length !== 12) throw new Error("Matrice domaines != 12");
    if (matSub.rows.length < 30) throw new Error("Matrice sous-domaines < 30");

    const href = eng.corpusHref("Corpus/Tome 2 - Cadre normatif et exigences d'architecture.md", 709);
    if (!href.startsWith("../../Corpus/") || !href.includes("%27") || !href.endsWith("#L709")) throw new Error("Encodage href invalide: " + href);

    // Non-régression facettes Horizon (normalisation demi-cadratin et exclusion du nœud racine)
    const horizons = idx.facets.horizons;
    const seenNorm = new Set();
    for (const h of horizons) {
      if (/[\\u2013\\u2014]/.test(h)) throw new Error("Horizon non normalisé dans facettes: " + h);
      if (seenNorm.has(h)) throw new Error("Doublon horizon: " + h);
      seenNorm.add(h);
      const resH = eng.filterNodesAndRelations(idx, { horizon: h });
      if (resH.matchingNodeIds.size === 0) throw new Error("Filtre horizon vide pour: " + h);
    }
    if (eng.filterNodesAndRelations(idx, { horizon: "2023–2035" }).matchingNodeIds.size === 0) {
      throw new Error("Filtre 2023–2035 (en-dash) vide");
    }

    // Fonctions pures Vue 5 PRD & indexation recherche PRD
    const pHash = eng.parseLocationHash("#view=prd&ch=05&thm=loi-de-lusser");
    if (pHash.view !== "prd" || pHash.ch !== "05" || pHash.thm !== "loi-de-lusser") {
      throw new Error("parseLocationHash invalide: " + JSON.stringify(pHash));
    }
    const prdHit = eng.resolveNodeToPrdTarget(idx, "THM_loi-de-lusser");
    if (!prdHit || Number(prdHit.chapter_number) !== 2) {
      throw new Error("resolveNodeToPrdTarget THM_loi-de-lusser invalide: " + JSON.stringify(prdHit));
    }
    const unitHit = eng.resolveStructUnitToPrdTarget(idx, "r-u0001");
    if (!unitHit || !unitHit.chapter_number) {
      throw new Error("resolveStructUnitToPrdTarget r-u0001 vide");
    }
    const prdFilt = eng.computePrdFilterState(idx, { domain: "D07" });
    if (!prdFilt.active || prdFilt.matchingChapters.size !== 3) {
      throw new Error("computePrdFilterState D07 != 3 chapitres: " + prdFilt.matchingChapters.size);
    }
    const sPrdCh = eng.searchCorpus(idx, "Chapitre 05", 15);
    if (!sPrdCh.some(d => d.kind === "prd-chapter")) {
      throw new Error("searchCorpus ne remonte aucun prd-chapter");
    }
    const sPrdAnn = eng.searchCorpus(idx, "Annexe B", 15);
    if (!sPrdAnn.some(d => d.kind === "prd-annexe")) {
      throw new Error("searchCorpus ne remonte aucune prd-annexe");
    }
    const d07Themes = eng.collectDescendantThemeIds(idx, "DOM_D07");
    if (d07Themes.length < 15 || !d07Themes.every(tid => idx.nodeById[tid].domain_id === "D07")) {
      throw new Error("collectDescendantThemeIds DOM_D07 invalide: " + d07Themes.length);
    }
    if (eng.normalizePrdExecId("1") !== "exec-01" || eng.normalizePrdExecId("sec-3") !== "exec-03") {
      throw new Error("normalizePrdExecId invalide");
    }
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(HTML_PATH)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec Node.js:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"


def test_html_css_specificity_and_svg_export_styles() -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    # .mm-node-box ne doit pas écraser l'attribut stroke par une règle CSS générique
    m_box = re.search(r"\.mm-node-box\s*\{([^}]+)\}", html)
    assert m_box is not None
    assert "stroke:" not in m_box.group(1)
    assert 'viewBox' in html
    assert '.mm-toggle-circle{' in html
    assert '.mm-toggle-text{' in html
    assert '.mm-node.dimmed{' in html
    assert '.mm-edge.dimmed{' in html


def test_nodejs_all_four_views_dom_smoke() -> None:
    node_exe = shutil.which("node")
    if node_exe is None:
        pytest.skip("Node.js non disponible dans l'environnement")

    node_script = r"""
    const fs = require("fs");
    const vm = require("vm");
    const html = fs.readFileSync(process.argv[1], "utf8");
    const jsonMatch = html.match(/<script[^>]*id="corpus-mindmap-data"[^>]*>([\s\S]*?)<\/script>/);
    const jsMatch = html.match(/<script(?![^>]*type="application\/json")[^>]*>([\s\S]*?)<\/script>/);

    function makeEl(tag, id) {
      const listeners = {};
      const attrs = {};
      const children = [];
      const classes = new Set();
      const el = {
        tagName: (tag || "DIV").toUpperCase(),
        id: id || "",
        textContent: "",
        innerHTML: "",
        value: "",
        checked: false,
        style: {},
        children,
        classList: {
          add: c => classes.add(c),
          remove: c => classes.delete(c),
          toggle: (c, f) => { if (f === undefined) { if (classes.has(c)) classes.delete(c); else classes.add(c); } else if (f) classes.add(c); else classes.delete(c); },
          contains: c => classes.has(c),
        },
        setAttribute: (k, v) => { attrs[k] = String(v); },
        getAttribute: k => attrs[k] ?? null,
        appendChild: c => { children.push(c); return c; },
        removeChild: c => { const i = children.indexOf(c); if (i >= 0) children.splice(i, 1); },
        get firstChild() { return children[0] || null; },
        addEventListener: (ev, fn) => { (listeners[ev] = listeners[ev] || []).push(fn); },
        click: () => { (listeners.click || []).forEach(fn => fn({ stopPropagation() {}, preventDefault() {}, currentTarget: el, target: el })); },
        dispatch: (ev) => { (listeners[ev] || []).forEach(fn => fn({ stopPropagation() {}, preventDefault() {}, currentTarget: el, target: el })); },
        querySelector: () => null,
        querySelectorAll: () => [],
        getBoundingClientRect: () => ({ width: 1200, height: 800, left: 0, top: 0 }),
        getBBox: () => ({ x: 0, y: 0, width: 600, height: 400 }),
        closest: () => null,
        cloneNode: () => makeEl(tag, id),
        insertBefore: (n) => { children.unshift(n); },
        focus() {}, select() {}, setSelectionRange() {}
      };
      return el;
    }

    const byId = {};
    for (const id of [
      "corpus-mindmap-data", "mm-svg", "mm-stage", "mm-zoom-label", "st-svg", "st-stage", "st-zoom-label",
      "sy-svg", "sy-stage", "sy-zoom-label", "canvas-tooltip", "kpi-strip", "f-tome", "st-file-select",
      "f-domain", "f-autonomy", "f-role", "f-horizon", "f-rel", "mm-legend-grid", "path-start", "path-end",
      "filter-summary", "inspector", "inspector-body", "mm-stats-pill", "st-list-pane", "st-stats-pill",
      "sy-stats-pill", "path-results", "c4-content", "global-search", "search-dropdown", "export-svg-btn",
      "export-json-btn", "theme-toggle-btn", "reset-filters-btn", "mm-expand-all-btn", "mm-collapse-all-btn",
      "mm-toggle-edges-btn", "mm-xray-btn", "mm-expand-linked-btn", "st-toggle-list-btn",
      "st-expand-chapters-btn", "st-collapse-tomes-btn", "sy-reheat-btn", "path-find-btn", "path-swap-btn",
      "path-clear-btn", "path-directed", "inspector-toggle-btn", "mm-legend-toggle"
    ]) {
      byId[id] = makeEl(id.endsWith("-svg") ? "svg" : "div", id);
    }
    byId["corpus-mindmap-data"].textContent = jsonMatch[1];

    const viewTabs = ["mindmap", "structure", "synaptic", "concordance"].map(v => {
      const b = makeEl("button");
      b.setAttribute("data-view", v);
      return b;
    });
    const c4Tabs = ["heatmap", "reconciliations", "timeline", "traceability"].map(t => {
      const b = makeEl("button");
      b.setAttribute("data-c4-tab", t);
      return b;
    });

    const documentStub = {
      readyState: "complete",
      documentElement: makeEl("html"),
      body: makeEl("body"),
      activeElement: null,
      getElementById: id => byId[id] || null,
      createElement: tag => makeEl(tag),
      createElementNS: (ns, tag) => makeEl(tag),
      addEventListener() {},
      querySelectorAll: sel => sel === ".view-tab" ? viewTabs : (sel === "[data-c4-tab]" ? c4Tabs : [])
    };
    const sandbox = {
      console, Set, Map, Object, Array, Math, String, Number, Boolean, Date, RegExp, JSON,
      encodeURIComponent, document: documentStub, window: { innerWidth: 1400, innerHeight: 900, addEventListener() {} }, globalThis: {}
    };
    sandbox.globalThis = sandbox;
    new vm.Script(jsMatch[1], { filename: "runtime_dom_smoke.js" }).runInNewContext(sandbox);

    for (const vt of viewTabs) vt.click();
    for (const ct of c4Tabs) ct.click();

    if (!byId["mm-stats-pill"].textContent.includes("nœuds")) throw new Error("Vue 1 non rendue");
    if (!byId["st-stats-pill"].textContent.includes("titres")) throw new Error("Vue 2 non rendue");
    if (!byId["sy-stats-pill"].textContent.includes("thèmes")) throw new Error("Vue 3 non rendue");
    if (byId["c4-content"].innerHTML.length < 1000) throw new Error("Vue 4 vide");

    // Non-régression bug #1 : Vue 3 filtrée -> Vue 1 -> Reset -> retour Vue 3 doit rendre tous les nœuds
    viewTabs[2].click(); // synaptic
    byId["f-domain"].value = "D07";
    byId["f-domain"].dispatch("change");
    const d07Count = byId["sy-svg"].children[0].children.length;
    if (d07Count >= 300) throw new Error("Filtrage D07 inefficace: " + d07Count);

    viewTabs[0].click(); // mindmap
    byId["reset-filters-btn"].click();
    viewTabs[2].click(); // synaptic
    const fullCount = byId["sy-svg"].children[0].children.length;
    if (fullCount < 800) throw new Error("Vue 3 désynchronisée après reset hors vue: " + fullCount);
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(HTML_PATH)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec DOM smoke Node.js:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"


def test_nodejs_view5_prd_and_bidirectional_bridge() -> None:
    node_exe = shutil.which("node")
    if node_exe is None:
        pytest.skip("Node.js non disponible dans l'environnement")

    node_script = r"""
    const fs = require("fs");
    const vm = require("vm");
    const html = fs.readFileSync(process.argv[1], "utf8");
    const jsonMatch = html.match(/<script[^>]*id="corpus-mindmap-data"[^>]*>([\s\S]*?)<\/script>/);
    const jsMatch = html.match(/<script(?![^>]*type="application\/json")[^>]*>([\s\S]*?)<\/script>/);

    function makeEl(tag, id) {
      const listeners = {};
      const attrs = {};
      const children = [];
      const classes = new Set();
      return {
        tagName: (tag || "DIV").toUpperCase(),
        id: id || "",
        textContent: "",
        innerHTML: "",
        value: "",
        checked: false,
        disabled: false,
        scrollTop: 0,
        style: {},
        children,
        classList: {
          add: c => classes.add(c),
          remove: c => classes.delete(c),
          toggle: (c, f) => { if (f === undefined) { if (classes.has(c)) classes.delete(c); else classes.add(c); } else if (f) classes.add(c); else classes.delete(c); },
          contains: c => classes.has(c),
        },
        setAttribute: (k, v) => { attrs[k] = String(v); },
        getAttribute: k => attrs[k] ?? null,
        appendChild: c => { children.push(c); return c; },
        removeChild: c => { const i = children.indexOf(c); if (i >= 0) children.splice(i, 1); },
        get firstChild() { return children[0] || null; },
        addEventListener: (ev, fn) => { (listeners[ev] = listeners[ev] || []).push(fn); },
        click: () => { (listeners.click || []).forEach(fn => fn({ stopPropagation() {}, preventDefault() {}, currentTarget: this, target: this })); },
        dispatch: (ev) => { (listeners[ev] = listeners[ev] || []); listeners[ev].forEach(fn => fn({ stopPropagation() {}, preventDefault() {}, currentTarget: this, target: this })); },
        querySelector: () => null,
        querySelectorAll: () => [],
        getBoundingClientRect: () => ({ width: 1200, height: 800, left: 0, top: 0 }),
        getBBox: () => ({ x: 0, y: 0, width: 600, height: 400 }),
        closest: () => null,
        cloneNode: () => makeEl(tag, id),
        insertBefore: (n) => { children.unshift(n); },
        scrollIntoView() {},
        focus() {}, select() {}, setSelectionRange() {}
      };
    }

    const allIds = [
      "corpus-mindmap-data", "mm-svg", "mm-stage", "mm-zoom-label", "st-svg", "st-stage", "st-zoom-label",
      "sy-svg", "sy-stage", "sy-zoom-label", "canvas-tooltip", "kpi-strip", "f-tome", "st-file-select",
      "f-domain", "f-autonomy", "f-role", "f-horizon", "f-rel", "mm-legend-grid", "path-start", "path-end",
      "filter-summary", "inspector", "inspector-body", "mm-stats-pill", "st-list-pane", "st-stats-pill",
      "sy-stats-pill", "path-results", "c4-content", "global-search", "search-dropdown", "export-svg-btn",
      "export-json-btn", "theme-toggle-btn", "reset-filters-btn", "mm-expand-all-btn", "mm-collapse-all-btn",
      "mm-toggle-edges-btn", "mm-xray-btn", "mm-expand-linked-btn", "st-toggle-list-btn",
      "st-expand-chapters-btn", "st-collapse-tomes-btn", "sy-reheat-btn", "path-find-btn", "path-swap-btn",
      "path-clear-btn", "path-directed", "inspector-toggle-btn", "mm-legend-toggle",
      "prd-toc-pane", "prd-toc-filter", "prd-toc-count", "prd-toc-list", "prd-reader", "prd-stats-pill",
      "prd-toggle-toc-btn", "prd-print-btn", "prd-standalone-link"
    ];
    const byId = {};
    for (const id of allIds) byId[id] = makeEl(id.endsWith("-svg") ? "svg" : "div", id);
    byId["corpus-mindmap-data"].textContent = jsonMatch[1];

    const viewTabs = ["mindmap", "structure", "synaptic", "concordance", "prd"].map(v => {
      const b = makeEl("button");
      b.setAttribute("data-view", v);
      return b;
    });

    const documentStub = {
      readyState: "complete",
      documentElement: makeEl("html"),
      body: makeEl("body"),
      activeElement: null,
      getElementById: id => byId[id] || null,
      createElement: tag => makeEl(tag),
      createElementNS: (ns, tag) => makeEl(tag),
      addEventListener() {},
      querySelectorAll: sel => sel === ".view-tab" ? viewTabs : []
    };
    const sandbox = {
      console, Set, Map, Object, Array, Math, String, Number, Boolean, Date, RegExp, JSON,
      encodeURIComponent, decodeURIComponent, document: documentStub,
      window: { innerWidth: 1400, innerHeight: 900, location: { hash: "" }, addEventListener() {}, print() {} },
      globalThis: {}
    };
    sandbox.globalThis = sandbox;
    new vm.Script(jsMatch[1], { filename: "view5_dom_smoke.js" }).runInNewContext(sandbox);

    const app = sandbox.CartographieApp;
    if (!app) throw new Error("CartographieApp non exposé");

    // 1. Export SVG désactivé sur concordance ET prd, réactivé sur mindmap
    app.switchView("concordance");
    if (!byId["export-svg-btn"].disabled) throw new Error("export-svg-btn devrait être désactivé en concordance");
    app.switchView("prd");
    if (!byId["export-svg-btn"].disabled) throw new Error("export-svg-btn devrait être désactivé en prd");
    if (!byId["prd-stats-pill"].textContent.includes("260 thèmes")) {
      throw new Error("Statistiques Vue 5 incomplètes: " + byId["prd-stats-pill"].textContent);
    }
    if (!byId["prd-toc-list"].innerHTML.includes("Partie XII")) {
      throw new Error("TDM Vue 5 incomplète");
    }

    // 2. Mode Document intégral : 12 parties, 36 chapitres, 71 familles, 260 thèmes, 4 annexes
    app.getState().prdMode = "full";
    app.switchView("prd");
    const fullHtml = byId["prd-reader"].innerHTML;
    for (const marker of [
      "Partie I — D01", "Partie XII — D12", "Chapitre 01 —", "Chapitre 36 —",
      "Annexe A —", "Annexe B —", "Annexe C —", "Annexe D —",
      "THM_loi-de-lusser", "Tensions d'arbitrage structurantes (62 relations tension_arbitrage)"
    ]) {
      if (!fullHtml.includes(marker)) throw new Error("Marqueur absent en Vue 5 mode intégral: " + marker);
    }

    // Phase 2 : Hygiène DOM Vue 5 (0 backtick hors <code>, 0 **gras**, 0 \$, 0 <em> brisé sur gen_ai.*, 237 entrées Annexe D)
    const fullNoCode = fullHtml.replace(/<code[^>]*>[\s\S]*?<\/code>/gi, "");
    if (fullNoCode.includes("`")) throw new Error("Backtick brut détecté hors <code> dans Vue 5");
    if (/(^|[\s(>])\*\*[^\s*](?:[^*\n]*?[^\s*])?\*\*(?=[\s.,;:!?<)]|$)/.test(fullNoCode)) {
      throw new Error("**gras** brut détecté dans Vue 5");
    }
    if (/<strong>\s*et tests\//i.test(fullHtml)) {
      throw new Error("Glob specs/** transformé en <strong> par erreur");
    }
    if (fullHtml.includes("\\$")) throw new Error("Literal backslash-dollar dans Vue 5");
    if (/<em>[^<]*gen_ai\.[^<]*<\/em>/i.test(fullHtml)) throw new Error("<em> brisé autour de gen_ai.* dans Vue 5");
    if (!fullHtml.includes("237 entrées uniques")) throw new Error("Matrice Annexe D 237 entrées absente en Vue 5");
    const eng = sandbox.CartographieEngine;
    const inlineChk = eng.prdInlineHtml("gen_ai.* et *Cost-per-Outcome* + `strict: true` 10 M\\$ CA L10-L20 A -> B C <-> D");
    if (!inlineChk.includes("gen_ai.* et <em>Cost-per-Outcome</em>") || !inlineChk.includes("10 M$ CA") || !inlineChk.includes("A → B") || !inlineChk.includes("C ↔ D")) {
      throw new Error("prdInlineHtml MindMap défaillant: " + inlineChk);
    }

    // 3. Filtres multi-facettes sur Vue 5 & état vide D01+L0+RSSI (Vue 5 + Vue 3)
    byId["f-domain"].value = "D07";
    byId["f-domain"].dispatch("change");
    if (!byId["prd-stats-pill"].textContent.includes("3 / 36 chapitres")) {
      throw new Error("Filtrage D07 inopérant en Vue 5: " + byId["prd-stats-pill"].textContent);
    }
    byId["f-domain"].value = "D01";
    byId["f-autonomy"].value = "L0";
    byId["f-role"].value = "RSSI";
    byId["f-role"].dispatch("change");
    if (!byId["prd-stats-pill"].textContent.startsWith("0 / 36 chapitres · 0 / 260 thèmes")) {
      throw new Error("computePrdFilterState incohérent sur D01+L0+RSSI: " + byId["prd-stats-pill"].textContent);
    }
    if (!byId["prd-reader"].innerHTML.includes("empty-state")) {
      throw new Error("Empty state manquant en Vue 5 sur filtre 0 thème");
    }
    app.switchView("synaptic");
    if (byId["sy-stats-pill"].textContent !== "0 thème · 0 arête") {
      throw new Error("Vue 3 devrait afficher '0 thème · 0 arête' sans fallback 260: " + byId["sy-stats-pill"].textContent);
    }
    byId["f-domain"].value = "";
    byId["f-autonomy"].value = "";
    byId["f-role"].value = "";
    byId["f-domain"].dispatch("change");
    app.switchView("prd");

    // 4. Pont bidirectionnel Inspecteur -> PRD & hash deep-linking & lien dynamique #prd-standalone-link
    app.getState().prdMode = "targeted";
    app.selectThemeNode("THM_loi-de-lusser", true);
    if (!byId["inspector-body"].innerHTML.includes("insp-goto-prd")) {
      throw new Error("Bouton 'Lire dans le PRD' absent de l'inspecteur thème");
    }
    app.jumpToPrdByNodeId("THM_loi-de-lusser");
    if (app.getState().activeView !== "prd" || Number(app.getState().prdFocusId) !== 2 || app.getState().prdHighlightId !== "THM_loi-de-lusser") {
      throw new Error("Saut thème -> PRD défaillant");
    }
    if (!String(byId["prd-standalone-link"].getAttribute("href") || "").includes("#thm=THM_loi-de-lusser")) {
      throw new Error("Lien dynamique prd-standalone-link non synchronisé: " + byId["prd-standalone-link"].getAttribute("href"));
    }

    app.applyHashNavigation("#view=prd&sec=1");
    if (app.getState().activeView !== "prd" || app.getState().prdFocusKind !== "exec" || app.getState().prdHighlightId !== "exec-01") {
      throw new Error("Hash #view=prd&sec=1 non normalisé: " + app.getState().prdHighlightId);
    }
    if (!byId["prd-reader"].innerHTML.includes('prd-highlight" data-prd-eid="exec-01"')) {
      throw new Error("Section exec-01 non mise en surbrillance sur #view=prd&sec=1");
    }
    app.applyHashNavigation("#view=prd&annexe=B");
    if (app.getState().activeView !== "prd" || app.getState().prdFocusKind !== "annexe" || app.getState().prdFocusId !== "B") {
      throw new Error("Hash #view=prd&annexe=B défaillant");
    }
    app.getState().syEgo = "1";
    app.applyHashNavigation("#view=synaptic&node=DOM_D07");
    const d07CenterId = app.getState().syLastCenterId;
    const d07Domain = (JSON.parse(jsonMatch[1]).nodes.find(n => n.node_id === d07CenterId) || {}).domain_id;
    if (d07Domain !== "D07") {
      throw new Error("Hash #view=synaptic&node=DOM_D07 centré hors D07: " + d07CenterId + " (" + d07Domain + ")");
    }
    const d07SyText = byId["sy-stats-pill"].textContent;
    if (!byId["sy-stats-pill"].textContent.includes("thèmes") || d07SyText.startsWith("11 thèmes")) {
      throw new Error("Vue synaptique ego DOM_D07 invalide: " + d07SyText);
    }
    app.applyHashNavigation("#view=synaptic&node=THM_loi-de-lusser");
    if (app.getState().activeView !== "synaptic" || app.getState().selectedId !== "THM_loi-de-lusser") {
      throw new Error("Hash #view=synaptic&node=... défaillant");
    }
    if (byId["export-svg-btn"].disabled) throw new Error("export-svg-btn resté désactivé en synaptic");

    // 5. Phase C2.c : 115 schémas, Panorama SCH-00, 01.3..36.3, Annexe E, Inspecteur & recherche SCH-* + liens ../Tomes/
    const prdData = JSON.parse(jsonMatch[1]).prd;
    if (!prdData || !prdData.meta || prdData.meta.annexes_count !== 5 || prdData.meta.schemas_count !== 115) {
      throw new Error("Méta PRD schémas/annexes invalide dans MindMap");
    }
    app.getState().prdMode = "full";
    app.switchView("prd");
    const fullWithSchemas = byId["prd-reader"].innerHTML;
    for (const marker of [
      "Panorama visuel directeur", "01.3 Schémas de vulgarisation à intégrer",
      "36.3 Schémas de vulgarisation à intégrer", "Annexe E —",
      "Inventaire complet des 319 figures des Tomes 1 à 8"
    ]) {
      if (!fullWithSchemas.includes(marker)) throw new Error("Marqueur C2.c manquant en Vue 5 MindMap: " + marker);
    }
    const mmSchemas = (prdData.executive_summary.vulgarization_schemas || []).map(s => s.schema_id)
      .concat(prdData.chapters.flatMap(c => (c.vulgarization_schemas || []).map(s => s.schema_id)));
    if (mmSchemas.length !== 115) throw new Error("MindMap != 115 schémas");
    for (const sid of mmSchemas) {
      if (!fullWithSchemas.includes(sid)) throw new Error("Schéma manquant en Vue 5 MindMap: " + sid);
    }
    const mmTomeHrefs = Array.from(fullWithSchemas.matchAll(/href="(\.\.\/\.\.\/Tomes\/[^"#]+)"/g), m => m[1]);
    if (mmTomeHrefs.length < 600) throw new Error("Liens ../../Tomes/ insuffisants en Vue 5 MindMap: " + mmTomeHrefs.length);
    const fsPath = require("path");
    for (const rawHref of new Set(mmTomeHrefs)) {
      const diskPath = fsPath.resolve(fsPath.dirname(process.argv[1]), decodeURIComponent(rawHref));
      if (!fs.existsSync(diskPath)) throw new Error("Lien ../../Tomes/ cassé en Vue 5 MindMap: " + diskPath);
    }

    // Inspecteur latéral : Schémas de vulgarisation PRD rattachés
    app.selectThemeNode("THM_loi-de-lusser", true);
    if (!byId["inspector-body"].innerHTML.includes("Schémas de vulgarisation PRD") || !byId["inspector-body"].innerHTML.includes("SCH-02-")) {
      throw new Error("Section Schémas PRD absente de l'inspecteur thème");
    }

    // Recherche Ctrl+K sur SCH-15-03 + hash #sch=SCH-15-03
    const mmIdx = eng.buildIndexes(JSON.parse(jsonMatch[1]));
    const schHits = eng.searchCorpus(mmIdx, "SCH-15-03", 10);
    if (!schHits.some(h => h.kind === "prd-schema" && h.id === "SCH-15-03")) {
      throw new Error("searchCorpus('SCH-15-03') n'a pas retourné prd-schema");
    }
    app.applyHashNavigation("#sch=SCH-15-03");
    if (app.getState().activeView !== "prd" || Number(app.getState().prdFocusId) !== 15 || app.getState().prdHighlightId !== "SCH-15-03") {
      throw new Error("Hash #sch=SCH-15-03 défaillant dans MindMap");
    }
    if (!String(byId["prd-standalone-link"].getAttribute("href") || "").includes("#sch=SCH-15-03")) {
      throw new Error("prd-standalone-link non synchronisé sur #sch=SCH-15-03");
    }

    // #138 : 0 'Synthetise', virgules décimales françaises et boutons GLOBAL/Panorama -> exec-panorama en Vue 5 Annexe E
    if (/\bsynthetise\b/i.test(fullWithSchemas)) {
      throw new Error("Synthetise sans accent détecté en Vue 5 MindMap");
    }
    app.applyHashNavigation("#view=prd&annexe=E");
    const annEHtml = byId["prd-reader"].innerHTML;
    if (/\bsynthetise\b/i.test(annEHtml)) {
      throw new Error("Synthetise sans accent détecté dans Annexe E Vue 5 MindMap");
    }
    if (!annEHtml.includes('data-prd-jump-exec="exec-panorama">GLOBAL</button>') ||
        !annEHtml.includes('data-prd-jump-exec="exec-panorama">Panorama</button>')) {
      throw new Error("Boutons GLOBAL/Panorama Annexe E ne pointent pas vers exec-panorama");
    }
    const annEDistSlice = annEHtml.split("Répartition par Domaine")[1].split("Catalogue directeur intégral")[0];
    if (annEDistSlice.includes('data-prd-jump-sch="SCH-00-01">GLOBAL</button>') ||
        annEDistSlice.includes('data-prd-jump-sch="SCH-00-01">Panorama</button>')) {
      throw new Error("Boutons GLOBAL/Panorama de Répartition pointent encore vers SCH-00-01");
    }
    const annEStatsSlice = annEHtml.split("Synthèse statistique des 115 schémas")[1].split("Répartition par Domaine")[0];
    if (/\d+\.\d+\s*%/.test(annEStatsSlice)) {
      throw new Error("Pourcentage avec point décimal anglais détecté dans Annexe E Vue 5 MindMap");
    }
    if ((annEStatsSlice.match(/\d+,\d+\s+%/g) || []).length < 27) {
      throw new Error("Pourcentages avec virgule française incomplets dans Annexe E Vue 5 MindMap");
    }
    app.applyHashNavigation("#view=prd&sec=exec-panorama");
    if (app.getState().activeView !== "prd" || app.getState().prdFocusKind !== "exec" || app.getState().prdHighlightId !== "exec-panorama") {
      throw new Error("Navigation exec-panorama défaillante en Vue 5 MindMap");
    }
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(HTML_PATH)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec Vue 5 DOM smoke Node.js:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"
