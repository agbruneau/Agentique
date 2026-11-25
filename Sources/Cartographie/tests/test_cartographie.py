"""Suite de tests automatisés pour la cartographie interactive du Compendium Agentique.

Couvre :
- l'extraction structurelle CommonMark stricte des 15 sections du Compendium (`R`, `LIM`, `P01`–`P12`, `ANN`, 42 unités, 401 titres dans `Compendium/Compendium.md`, 8 408 lignes) ;
- l'absence de faux positifs dans les blocs de code clôturés et la couverture des identifiants `SCH-*`, `SRC-*`, `POR-*`, `SIG-*`, `INI-*` ;
- la complétude des 115 schémas compilés du Compendium (`52` PlantUML, `23` Mermaid, `40` SVG) ;
- l'intégrité du graphe transversal (`380` nœuds dont `260` thèmes, `616` relations, `180` cellules de matrice, `56` vedettes glossaire, `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37/37` `G2`, `837` pages PDF) ;
- la suppression définitive de l'ancienne carte `MindMap - Cartographie thématique du Corpus.html` et de `donnees/shards/` ;
- l'échappement sûr du JSON embarqué dans `<script>` et l'autonomie `file://` stricte (`0` CDN / requête réseau) ;
- la validation syntaxique et fonctionnelle DOM complète des `5` vues sous `Node.js`.
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
CARTO_DIR = REPO_ROOT / "Sources" / "Cartographie"
DONNEES_DIR = CARTO_DIR / "donnees"
OUTILS_DIR = CARTO_DIR / "outils"
HTML_PATH = CARTO_DIR / "MindMap - Cartographie thématique du Compendium.html"
OLD_HTML_PATH = CARTO_DIR / "MindMap - Cartographie thématique du Corpus.html"
OLD_SHARDS_DIR = DONNEES_DIR / "shards"

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
# 2. Suppression des artefacts obsolètes & extraction structurelle Compendium
# ---------------------------------------------------------------------------
def test_legacy_corpus_mindmap_and_tome_shards_removed() -> None:
    assert not OLD_HTML_PATH.exists(), f"Ancien fichier HTML encore présent : {OLD_HTML_PATH}"
    assert not OLD_SHARDS_DIR.exists(), f"Ancien dossier shards/ encore présent : {OLD_SHARDS_DIR}"


def test_structure_covers_compendium_15_sections_and_42_units() -> None:
    struct_path = DONNEES_DIR / "structure-integrale.json"
    assert struct_path.is_file()
    data = json.loads(struct_path.read_text(encoding="utf-8"))

    expected_sections = [
        "R", "LIM", "P01", "P02", "P03", "P04", "P05", "P06",
        "P07", "P08", "P09", "P10", "P11", "P12", "ANN",
    ]
    assert data["totals"]["files"] == 15
    assert data["totals"]["sections"] == 15
    assert data["totals"]["compendium_units_mapped"] == 42
    assert data["totals"]["compendium_lines"] == 8408
    assert data["totals"]["compendium_headings"] == 401
    assert len(data["files"]) == 15
    assert [f["tome_id"] for f in data["files"]] == expected_sections

    comp_md_path = REPO_ROOT / "Compendium" / "Compendium.md"
    comp_lines = comp_md_path.read_text(encoding="utf-8").splitlines()
    assert len(comp_lines) == 8408
    _, _, comp_code_lines = es.parse_markdown_lines(comp_lines)

    mapped_units: set[str] = set()
    all_identifiers: set[str] = set()
    total_lines = 0
    total_words = 0
    total_headings = 0
    compendium_headings = 0

    for fmeta in data["files"]:
        md_path = REPO_ROOT / fmeta["file"]
        assert md_path.is_file()
        raw_lines = md_path.read_text(encoding="utf-8").splitlines()
        l_start = int(fmeta["line_start"])
        l_end = int(fmeta["line_end"])
        assert 1 <= l_start <= l_end <= len(raw_lines)
        assert fmeta["line_count"] == l_end - l_start + 1
        flat = _walk_struct_tree(fmeta["tree"])
        assert len(flat) == fmeta["heading_count"]

        for node in flat:
            assert l_start <= node["line_start"] <= node["line_end"] <= l_end
            if fmeta["file"] == "Compendium/Compendium.md":
                assert node["line_start"] not in comp_code_lines, (
                    f"Faux titre dans bloc de code Compendium à L{node['line_start']}"
                )

        if fmeta["tome_id"] != "R":
            compendium_headings += len(flat)
        mapped_units.update(fmeta.get("compendium_units", []))
        all_identifiers.update(fmeta.get("identifiers", []))
        total_lines += fmeta["line_count"]
        total_words += fmeta["word_count"]
        total_headings += len(flat)

    assert len(mapped_units) == 42
    assert compendium_headings == 401
    assert data["totals"]["lines"] == total_lines
    assert data["totals"]["words"] == total_words
    assert data["totals"]["headings"] == total_headings

    # Identifiants pivots extraits (SCH-*, SRC-*, POR-*, SIG-*, INI-*)
    for prefix in ("SCH-", "SRC-", "POR-", "SIG-", "INI-"):
        assert any(ident.startswith(prefix) for ident in all_identifiers), (
            f"Préfixe d'identifiant manquant dans structure-integrale.json : {prefix}"
        )


def test_inventaire_115_schemas_compendium_complete() -> None:
    inv_path = DONNEES_DIR / "inventaire-115-schemas-compendium.json"
    assert inv_path.is_file()
    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    totals = inv["totals"]
    assert totals["figures_count"] == 115
    assert totals["verified_sources_on_disk"] == 115
    assert totals["verified_renders_on_disk"] == 115
    assert totals["verified_compendium_lines"] == 115
    assert totals["verified_source_file_lines"] == 115
    assert totals["by_engine"] == {"mmd": 23, "puml": 52, "svg": 40}

    figs = inv["figures"]
    assert len(figs) == 115
    comp_line_count = len((REPO_ROOT / "Compendium" / "Compendium.md").read_text(encoding="utf-8").splitlines())
    for fg in figs:
        assert (REPO_ROOT / fg["source_path"]).is_file(), f"Source absente : {fg['source_path']}"
        assert (REPO_ROOT / fg["rendered_path"]).is_file(), f"Rendu absent : {fg['rendered_path']}"
        assert (REPO_ROOT / fg["source_file"]).is_file(), f"Manuscrit absent : {fg['source_file']}"
        assert 1 <= int(fg["compendium_md_line"]) <= comp_line_count
        src_lines = len((REPO_ROOT / fg["source_file"]).read_text(encoding="utf-8").splitlines())
        assert 1 <= int(fg["source_file_line"]) <= src_lines


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

    assert len(nodes) == 380
    theme_nodes = [n for n in nodes if n["node_kind"] == "theme"]
    assert len(theme_nodes) == 260
    assert len(relations) == 616
    assert len(chapters) == 42

    node_by_id = {n["node_id"]: n for n in nodes}
    node_by_slug = {n["canonical_slug"]: n for n in nodes if n.get("canonical_slug")}
    valid_rel_types = {rt["type_id"] for rt in schema["relation_types"]}
    expected_domains = {d["domain_id"] for d in schema["domains"]}
    assert expected_domains.issubset({n["domain_id"] for n in theme_nodes})

    for n in nodes:
        assert 0 <= n["depth"] <= 4
        if n["depth"] > 0:
            assert n["parent_id"] in node_by_id

    for rel in relations:
        assert rel["source"] in node_by_id
        assert rel["target"] in node_by_id
        assert rel["source"] != rel["target"]
        assert rel["type"] in valid_rel_types
        assert str(rel.get("justification", "")).strip() != ""

    expected_chap_sections = {
        "LIM", "P01", "P02", "P03", "P04", "P05", "P06",
        "P07", "P08", "P09", "P10", "P11", "P12", "ANN",
    }
    assert {c["tome_id"] for c in chapters} == expected_chap_sections
    for ch in chapters:
        themes_addr = ch.get("themes_addressed", [])
        assert len(themes_addr) >= 1
        assert any(slug in node_by_slug for slug in themes_addr)

    # 100 % des 260 thèmes ont des occurrences vérifiées dans Compendium/Compendium.md
    for n in theme_nodes:
        occs = n.get("occurrences") or []
        assert len(occs) >= 1, f"Thème sans occurrence Compendium : {n['node_id']}"
        for occ in occs:
            assert occ["file"] == "Compendium/Compendium.md", f"Occurrence hors Compendium.md : {occ}"
            assert 1 <= occ["line_start"] <= occ["line_end"] <= 8408
            assert (REPO_ROOT / occ["source_file"]).is_file(), f"source_file absent : {occ['source_file']}"

    # Matrice de concordance 12 x 15 = 180 cellules
    cmat = bundle.get("concordance_matrix") or []
    assert len(cmat) == 180

    # Pivots Compendium (glossaire 56, 135 L+, 27 Statut F, 14 CA-G0-SYNC, 37/37 G2, 837 p.)
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

    gloss = (pivots.get("glossaire_pivot") or {}).get("glossaire_compendium_56") or []
    assert len(gloss) == 56
    assert any(
        str(g.get("fr", "")).lower() == "agentivité des systèmes"
        and str(g.get("en", "")).lower() == "system agency"
        and g.get("chapitre_proprietaire") == "ch01"
        for g in gloss
    )

    comp_g0 = (pivots.get("bilans_aq") or {}).get("compendium_g0_g5") or {}
    assert comp_g0.get("sources_l_plus") == 135
    assert comp_g0.get("statut_f_exclus") == 27
    assert comp_g0.get("ca_g0_sync_count") == 14
    assert comp_g0.get("wyvern_g2_unites_count") == 37
    assert len(pivots.get("faits_empiriques_16") or []) == 16
    assert len(pivots.get("specifications_lplus_57") or []) == 57
    assert len(pivots.get("statut_f_exclus_27") or []) == 27
    assert (pivots.get("collection_metrics") or {}).get("compendium_pdf_pages") == 837

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

    prd = bundle.get("prd") or {}
    assert len(prd.get("parties", [])) == 12
    assert len(prd.get("chapters", [])) == 36
    assert len(prd.get("annexes", [])) == 5
    assert len(prd.get("glossary", [])) == 56
    lookup = prd.get("lookup") or {}
    assert len(lookup.get("node_id_to_prd", {})) == 379
    assert len(lookup.get("slug_to_chapter", {})) == 260
    assert len(lookup.get("domain_to_part", {})) == 12
    assert len(lookup.get("unit_id_to_chapter", {})) == 42


# ---------------------------------------------------------------------------
# 4. Tests du fichier HTML autonome et des liens relatifs Markdown
# ---------------------------------------------------------------------------
def test_html_standalone_no_external_cdn_and_safe_json() -> None:
    assert HTML_PATH.is_file()
    html = HTML_PATH.read_text(encoding="utf-8")

    assert "__MINDMAP_DATA_JSON__" not in html
    assert "__CORPUS_DATA_JSON__" not in html
    assert "__PAGE_TITLE__" not in html
    assert "MindMap - Cartographie thématique du Corpus.html" not in html
    assert 'id="top-compendium-md-link"' in html
    assert 'id="top-compendium-pdf-link"' in html
    assert 'data-c4-tab="glossary_evidence"' in html

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
    assert parsed["totals"]["files"] == 15

    html_without_json = html[: json_match.start(1)] + html[json_match.end(1) :]
    assert not re.search(r"<script[^>]+src\s*=", html_without_json, re.IGNORECASE)
    assert not re.search(r"<link[^>]+href\s*=\s*['\"]?https?://", html_without_json, re.IGNORECASE)
    assert not re.search(r"@import\s+url\(", html_without_json, re.IGNORECASE)
    assert not re.search(r"\bfetch\s*\(", html_without_json)
    assert "http://" not in html_without_json
    assert "https://" not in html_without_json
    assert not re.search(r"\bsynthetise\b", html_without_json, re.IGNORECASE)


def test_markdown_relative_links_valid() -> None:
    md_files = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "Compendium" / "README.md",
        REPO_ROOT / "Tomes" / "README.md",
        REPO_ROOT / "Sources" / "README.md",
        REPO_ROOT / "Sources" / "Compendium" / "README.md",
        REPO_ROOT / "Sources" / "Tomes" / "README.md",
        CARTO_DIR / "README.md",
        REPO_ROOT / "Sources" / "gabarit-pdf" / "README.md",
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

    node_script = r"""
    const fs = require("fs");
    const vm = require("vm");
    const html = fs.readFileSync(process.argv[1], "utf8");
    const jsonMatch = html.match(/<script[^>]*id="corpus-mindmap-data"[^>]*>([\s\S]*?)<\/script>/);
    if (!jsonMatch) throw new Error("JSON embarqué introuvable");
    const data = JSON.parse(jsonMatch[1]);
    const jsMatch = html.match(/<script(?![^>]*type="application\/json")[^>]*>([\s\S]*?)<\/script>/);
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

    if (idx.nodes.length !== 380) throw new Error("Nombre de nœuds != 380: " + idx.nodes.length);
    if (idx.relations.length !== 616) throw new Error("Nombre de relations != 616: " + idx.relations.length);
    if (idx.structFlat.length !== 406) throw new Error("Titres H1-H6 != 406: " + idx.structFlat.length);
    if (!idx.glossaryTerms || idx.glossaryTerms.length !== 56) throw new Error("Glossaire != 56");

    const s1 = eng.searchCorpus(idx, "Lusser", 10);
    if (s1.length === 0) throw new Error("Recherche 'Lusser' vide");
    const s2 = eng.searchCorpus(idx, "EXIG-MCP-15", 10);
    if (s2.length === 0) throw new Error("Recherche 'EXIG-MCP-15' vide");
    const sGloss = eng.searchCorpus(idx, "Agentivité des systèmes", 10);
    if (!sGloss.some(d => d.kind === "glossary")) {
      throw new Error("Ctrl+K 'Agentivité des systèmes' ne remonte aucune vedette glossary");
    }

    const filtered = eng.filterNodesAndRelations(idx, { domain: "D07", section: "P07" });
    if (filtered.matchingNodeIds.size === 0) throw new Error("Filtrage D07+P07 vide");

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
    if (matDom.tomeIds.length !== 15) throw new Error("Matrice sections != 15");
    if (matSub.rows.length !== 36) throw new Error("Matrice sous-domaines != 36");

    const hrefComp = eng.corpusHref("Compendium/Compendium.md", 215);
    if (hrefComp !== "../../Compendium/Compendium.md#L215") throw new Error("Encodage corpusHref invalide: " + hrefComp);

    // Non-régression facettes Horizon
    const horizons = idx.facets.horizons;
    const seenNorm = new Set();
    for (const h of horizons) {
      if (/[\u2013\u2014]/.test(h)) throw new Error("Horizon non normalisé dans facettes: " + h);
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
    const unitHit = eng.resolveStructUnitToPrdTarget(idx, "p01-u0013");
    if (!unitHit || Number(unitHit.chapter_number) !== 2) {
      throw new Error("resolveStructUnitToPrdTarget p01-u0013 invalide: " + JSON.stringify(unitHit));
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
    m_box = re.search(r"\.mm-node-box\s*\{([^}]+)\}", html)
    assert m_box is not None
    assert "stroke:" not in m_box.group(1)
    assert "viewBox" in html
    assert ".mm-toggle-circle{" in html
    assert ".mm-toggle-text{" in html
    assert ".mm-node.dimmed{" in html
    assert ".mm-edge.dimmed{" in html


def test_nodejs_all_five_views_dom_smoke() -> None:
    node_exe = shutil.which("node")
    if node_exe is None:
        pytest.skip("Node.js non disponible dans l'environnement")

    node_script = r"""
    const fs = require("fs");
    const vm = require("vm");
    const fsPath = require("path");
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
        click: () => { (listeners.click || []).forEach(fn => fn({ stopPropagation() {}, preventDefault() {}, currentTarget: el, target: el })); },
        dispatch: (ev) => { (listeners[ev] || []).forEach(fn => fn({ stopPropagation() {}, preventDefault() {}, currentTarget: el, target: el })); },
        querySelector: () => null,
        querySelectorAll: () => [],
        getBoundingClientRect: () => ({ width: 1200, height: 800, left: 0, top: 0 }),
        getBBox: () => ({ x: 0, y: 0, width: 600, height: 400 }),
        closest: () => null,
        cloneNode: () => { const c = makeEl(tag, id); c.value = el.value; c.textContent = el.textContent; c.innerHTML = el.innerHTML; return c; },
        insertBefore: (n) => { children.unshift(n); },
        scrollIntoView() {},
        focus() {}, select() {}, setSelectionRange() {}
      };
      return el;
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
      "prd-toggle-toc-btn", "prd-print-btn", "prd-standalone-link",
      "top-compendium-md-link", "top-compendium-pdf-link", "c4-gloss-search", "c4-gloss-body", "c4-gloss-count"
    ];
    const byId = {};
    for (const id of allIds) byId[id] = makeEl(id.endsWith("-svg") ? "svg" : "div", id);
    byId["corpus-mindmap-data"].textContent = jsonMatch[1];
    byId["f-tome"].setAttribute("data-filter", "section");
    byId["top-compendium-md-link"].setAttribute("href", "../../Compendium/Compendium.md");
    byId["top-compendium-pdf-link"].setAttribute("href", "../../Compendium/Compendium.pdf");

    const viewTabs = ["mindmap", "structure", "synaptic", "concordance", "prd"].map(v => {
      const b = makeEl("button");
      b.setAttribute("data-view", v);
      return b;
    });
    const c4Tabs = ["heatmap", "reconciliations", "timeline", "traceability", "glossary_evidence"].map(t => {
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
      encodeURIComponent, decodeURIComponent, document: documentStub,
      window: { innerWidth: 1400, innerHeight: 900, location: { hash: "" }, addEventListener() {}, print() {} },
      globalThis: {}
    };
    sandbox.globalThis = sandbox;
    new vm.Script(jsMatch[1], { filename: "runtime_all5_smoke.js" }).runInNewContext(sandbox);

    const app = sandbox.CartographieApp;
    const eng = sandbox.CartographieEngine;
    if (!app || !eng) throw new Error("CartographieApp/Engine manquant");

    // 1. Vues 1, 2, 3, 4
    for (const vt of viewTabs.slice(0, 4)) vt.click();
    if (!byId["mm-stats-pill"].textContent.includes("nœuds")) throw new Error("Vue 1 non rendue");
    const hasStLim = byId["st-file-select"].children.some(o => o.value === "LIM" || String(o.textContent).includes("LIM")) || byId["st-file-select"].innerHTML.includes("LIM");
    if (!byId["st-stats-pill"].textContent.includes("titres") || !hasStLim) {
      throw new Error("Vue 2 structure 15 sections/42 unités non rendue");
    }
    if (!byId["sy-stats-pill"].textContent.includes("thèmes")) throw new Error("Vue 3 non rendue");
    const hasFTomeP07 = byId["f-tome"].children.some(o => o.value === "P07" || String(o.textContent).includes("P07")) || byId["f-tome"].innerHTML.includes("P07");
    if (byId["f-tome"].getAttribute("data-filter") !== "section" || !hasFTomeP07) {
      throw new Error("#f-tome[data-filter='section'] sans option Compendium");
    }

    // 5 sous-onglets Vue 4 dont glossary_evidence + filtre #c4-gloss-search
    for (const ct of c4Tabs) ct.click();
    const glossHtml = byId["c4-content"].innerHTML;
    if (!glossHtml.includes("Agentivité des systèmes") || !glossHtml.includes("system agency") || !glossHtml.includes("135")) {
      throw new Error("Sous-onglet glossary_evidence incomplet");
    }
    byId["c4-gloss-search"].value = "Agentivité des systèmes";
    byId["c4-gloss-search"].dispatch("input");
    if (!byId["c4-content"].innerHTML.includes("Agentivité des systèmes") ||
        !byId["c4-content"].innerHTML.includes("<strong>1</strong> / 56 vedettes")) {
      throw new Error("Filtre #c4-gloss-search défaillant");
    }

    // Liens en-tête Compendium
    if (!byId["top-compendium-md-link"].getAttribute("href").includes("Compendium/Compendium.md") ||
        !byId["top-compendium-pdf-link"].getAttribute("href").includes("Compendium/Compendium.pdf")) {
      throw new Error("Liens en-tête Compendium invalides");
    }

    // Non-régression Vue 3 filtrée -> Vue 1 -> Reset -> Vue 3
    viewTabs[2].click();
    byId["f-domain"].value = "D07";
    byId["f-domain"].dispatch("change");
    const d07Count = byId["sy-svg"].children[0].children.length;
    if (d07Count >= 300) throw new Error("Filtrage D07 inefficace: " + d07Count);
    viewTabs[0].click();
    byId["reset-filters-btn"].click();
    viewTabs[2].click();
    const fullCount = byId["sy-svg"].children[0].children.length;
    if (fullCount < 800) throw new Error("Vue 3 désynchronisée après reset hors vue: " + fullCount);

    // 2. Vue 5 PRD Maître intégrée & liens Compendium + SCH-15-03 + Agentivité des systèmes
    app.switchView("concordance");
    if (!byId["export-svg-btn"].disabled) throw new Error("export-svg-btn devrait être désactivé en concordance");
    app.switchView("prd");
    if (!byId["export-svg-btn"].disabled) throw new Error("export-svg-btn devrait être désactivé en prd");
    if (!byId["prd-stats-pill"].textContent.includes("260 thèmes")) {
      throw new Error("Statistiques Vue 5 incomplètes: " + byId["prd-stats-pill"].textContent);
    }

    app.getState().prdMode = "full";
    app.switchView("prd");
    const fullHtml = byId["prd-reader"].innerHTML;
    for (const marker of [
      "Partie I — D01", "Partie XII — D12", "Chapitre 01 —", "Chapitre 36 —",
      "Annexe A —", "Annexe B —", "Annexe C —", "Annexe D —", "Annexe E —",
      "THM_loi-de-lusser", "Panorama visuel directeur", "01.3 Schémas de vulgarisation à intégrer",
      "36.3 Schémas de vulgarisation à intégrer", "237 entrées uniques", "135"
    ]) {
      if (!fullHtml.includes(marker)) throw new Error("Marqueur absent en Vue 5 mode intégral: " + marker);
    }

    // Hygiène DOM Vue 5 (0 backtick hors <code>, 0 **gras**, 0 \$, 0 synthetise)
    const fullNoCode = fullHtml.replace(/<code[^>]*>[\s\S]*?<\/code>/gi, "");
    if (fullNoCode.includes("`")) throw new Error("Backtick brut détecté hors <code> dans Vue 5");
    if (/(^|[\s(>])\*\*[^\s*](?:[^*\n]*?[^\s*])?\*\*(?=[\s.,;:!?<)]|$)/.test(fullNoCode)) {
      throw new Error("**gras** brut détecté dans Vue 5");
    }
    if (fullHtml.includes("\\$")) throw new Error("Literal backslash-dollar dans Vue 5");
    if (/\bsynthetise\b/i.test(fullHtml)) throw new Error("Synthetise sans accent détecté en Vue 5");

    // 115 schémas Compendium + liens ../../Compendium/Compendium.md et ../../Sources/Compendium/ouvrage/schemas/rendus/
    const prdData = JSON.parse(jsonMatch[1]).prd;
    const mmSchemas = (prdData.executive_summary.vulgarization_schemas || []).map(s => s.schema_id)
      .concat(prdData.chapters.flatMap(c => (c.vulgarization_schemas || []).map(s => s.schema_id)));
    if (mmSchemas.length !== 115) throw new Error("MindMap != 115 schémas");
    for (const sid of mmSchemas) {
      if (!fullHtml.includes(sid)) throw new Error("Schéma manquant en Vue 5 MindMap: " + sid);
    }

    const compMdHrefs = Array.from(fullHtml.matchAll(/href="(\.\.\/\.\.\/Compendium\/Compendium\.md[^"]*)"/g), m => m[1]);
    if (compMdHrefs.length < 36) throw new Error("Liens ../../Compendium/Compendium.md insuffisants en Vue 5: " + compMdHrefs.length);
    const compSchemaRendus = Array.from(fullHtml.matchAll(/href="(\.\.\/\.\.\/Sources\/Compendium\/ouvrage\/schemas\/rendus\/[^"#]+)"/g), m => m[1]);
    if (compSchemaRendus.length < 100) throw new Error("Liens ../../Sources/Compendium/ouvrage/schemas/rendus/ insuffisants: " + compSchemaRendus.length);
    for (const rawHref of new Set([...compMdHrefs.map(u => u.split("#")[0]), ...compSchemaRendus])) {
      const diskPath = fsPath.resolve(fsPath.dirname(process.argv[1]), decodeURIComponent(rawHref));
      if (!fs.existsSync(diskPath)) throw new Error("Lien Compendium cassé sur disque: " + diskPath);
    }

    // Inspecteur latéral + saut PRD + Ctrl+K SCH-15-03
    app.getState().prdMode = "targeted";
    app.selectThemeNode("THM_loi-de-lusser", true);
    const inspHtml = byId["inspector-body"].innerHTML;
    if (!inspHtml.includes("insp-goto-prd") ||
        !inspHtml.includes("Schémas compilés du Compendium") ||
        !inspHtml.includes("Occurrences vérifiées dans le Compendium") ||
        !inspHtml.includes("SCH-02-")) {
      throw new Error("Inspecteur thème incomplet");
    }
    app.jumpToPrdByNodeId("THM_loi-de-lusser");
    if (app.getState().activeView !== "prd" || Number(app.getState().prdFocusId) !== 2) {
      throw new Error("Saut thème -> PRD défaillant");
    }
    const mmIdx = eng.buildIndexes(JSON.parse(jsonMatch[1]));
    const schHits = eng.searchCorpus(mmIdx, "SCH-15-03", 10);
    if (!schHits.some(h => h.kind === "prd-schema" && h.id === "SCH-15-03")) {
      throw new Error("searchCorpus('SCH-15-03') n'a pas retourné prd-schema");
    }
    const agHits = eng.searchCorpus(mmIdx, "Agentivité des systèmes", 10);
    if (!agHits.some(h => h.kind === "glossary")) {
      throw new Error("searchCorpus('Agentivité des systèmes') n'a pas retourné glossary");
    }
    app.applyHashNavigation("#sch=SCH-15-03");
    if (app.getState().activeView !== "prd" || Number(app.getState().prdFocusId) !== 15 || app.getState().prdHighlightId !== "SCH-15-03") {
      throw new Error("Hash #sch=SCH-15-03 défaillant dans MindMap");
    }
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(HTML_PATH)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec DOM smoke 5 vues Node.js:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"
