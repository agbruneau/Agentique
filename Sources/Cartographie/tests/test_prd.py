"""Suite de tests automatisés pour le document maître ``prd.md`` et son compilateur.

Vérifie :
- les fonctions unitaires de ``compiler_prd.py`` (ancres GFM, numérotation 1..36, encodage URL) ;
- la compilation sur fixture synthétique et le rejet strict des placeholders/omissions ;
- l'exhaustivité du vrai ``Sources/Compendium/prd.md`` (12 domaines D01–D12, 36 chapitres 01–36,
  71 familles, 260 thèmes, 5 annexes A–E, 115 schémas Compendium, unicité, zéro placeholder/mojibake) ;
- l'ancrage exclusif sur le Compendium (0 lien vers `Tomes/` dans les tableaux d'ancrages ou `corpus_anchors`) ;
- la validité à 100 % de toutes les ancres internes ``#slug`` via parseur CommonMark strict ;
- la validité à 100 % de tous les liens relatifs vers ``Compendium/``, ``Sources/Compendium/`` et les READMEs ;
- l'application Web autonome ``PRD - Référentiel directeur de l'entreprise agentique.html`` sous Node.js.
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
PRD_PATH = REPO_ROOT / "Sources" / "Compendium" / "prd.md"
PRD_WEB_DATA_PATH = DONNEES_DIR / "prd-web-data.json"
PRD_WEB_HTML_PATH = CARTO_DIR / "PRD - Référentiel directeur de l'entreprise agentique.html"
MINDMAP_HTML_PATH = CARTO_DIR / "MindMap - Cartographie thématique du Compendium.html"
MINDMAP_HTML_ENCODED = "MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html"
OLD_MINDMAP_NAME = "MindMap - Cartographie thématique du Corpus.html"
OLD_MINDMAP_ENCODED = "MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html"
PRD_WEB_ENCODED = "PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html"

sys.path.insert(0, str(OUTILS_DIR))
import compiler_prd as cp  # noqa: E402
import extraire_structure as es  # noqa: E402


def test_unit_gfm_anchor_and_chapter_numbering() -> None:
    seen: dict[str, int] = {}
    a1 = cp.gfm_anchor("Chapitre 01 — Rupture épistémique & `Systèmes d'agentivité`", seen)
    a2 = cp.gfm_anchor("Chapitre 01 — Rupture épistémique & `Systèmes d'agentivité`", seen)
    assert a1 == "chapitre-01--rupture-épistémique--systèmes-dagentivité"
    assert a2 == f"{a1}-1"

    assert cp.expected_chapter_number("D01", "SUB_D01_01") == 1
    assert cp.expected_chapter_number("D01", "SUB_D01_03") == 3
    assert cp.expected_chapter_number("D12", "SUB_D12_03") == 36
    assert "%27" in cp.encode_rel_url("Sources/Compendium/ouvrage/manuscrit/02 - Architecture d'entreprise.md")
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
        "annexes": 5,
        "schemas": 115,
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
        pytest.skip("Sources/Compendium/prd.md pas encore compilé")

    bundle = json.loads((DONNEES_DIR / "corpus-mindmap-data.json").read_text(encoding="utf-8"))
    raw_bytes = PRD_PATH.read_bytes()
    assert not raw_bytes.startswith(b"\xef\xbb\xbf"), "BOM UTF-8 détecté dans prd.md"
    assert b"\r\n" not in raw_bytes, "Séquences CRLF détectées dans prd.md"
    prd_text = PRD_PATH.read_text(encoding="utf-8")
    prd_lines = prd_text.splitlines()

    # 0 mojibake / placeholder / dict Python brut (hors mention réglementaire BSIF B-15 SRC-110/SRC-067)
    for pat in cp.PLACEHOLDER_PATTERNS:
        bad_lines = [
            (idx, ln)
            for idx, ln in enumerate(prd_lines, 1)
            if pat.search(ln)
            and not (pat.pattern == r"\bTBD\b" and "ligne directrice B-15 du BSIF" in ln and ("SRC-110" in ln or "SRC-067" in ln))
        ]
        assert not bad_lines, f"Placeholder détecté dans prd.md ({pat.pattern}) : {bad_lines[:3]}"
    assert not re.search(r"\{'[A-Za-z0-9_]+'\s*:", prd_text), "Dict Python brut détecté dans prd.md"
    assert "\ufffd" not in prd_text

    # Présence explicite de Agentivité des systèmes et zéro occurrence System(s) of Agency
    assert "Agentivité des systèmes" in prd_text
    assert "**Sections Compendium** : —" not in prd_text, "Sections Compendium vides (—) dans prd.md"
    assert "Systems of Agency" not in prd_text
    assert "System of Agency" not in prd_text
    assert OLD_MINDMAP_NAME not in prd_text and OLD_MINDMAP_ENCODED not in prd_text
    assert MINDMAP_HTML_ENCODED in prd_text

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

    parties_h2 = [t for t in h2_titles if t.startswith("Partie ")]
    annexes_h2 = [t for t in h2_titles if t.startswith("Annexe ")]
    assert len(parties_h2) == 12
    assert len(annexes_h2) == 5
    assert len(set(parties_h2)) == 12
    assert len(set(annexes_h2)) == 5

    assert cp.PANORAMA_HEADING in h3_titles
    chapters_h3 = [t for t in h3_titles if re.match(r"^Chapitre \d{2} — ", t)]
    assert len(chapters_h3) == 36
    assert len(set(chapters_h3)) == 36
    for i in range(1, 37):
        assert any(t.startswith(f"Chapitre {i:02d} — ") for t in chapters_h3)
        assert f"{i:02d}.1 Résumé" in h4_titles
        assert f"{i:02d}.2 Descriptif du contenu ciblé" in h4_titles
        assert f"{i:02d}.3 Schémas de vulgarisation à intégrer" in h4_titles

    fam_h5 = [t for t in h5_titles if re.match(r"^\d{2}\.2\.\d+ ", t)]
    assert len(h5_titles) == 71
    assert len(fam_h5) == 71

    for node in bundle["nodes"]:
        kind = node["node_kind"]
        if kind in ("domain", "subdomain", "family"):
            assert node["node_id"] in prd_text, f"Identifiant MindMap manquant dans prd.md : {node['node_id']}"
        elif kind == "theme":
            assert node["node_id"] in prd_text, f"Thème manquant dans prd.md : {node['node_id']}"
            assert node["canonical_slug"] in prd_text, f"Slug manquant dans prd.md : {node['canonical_slug']}"

    # 0 lien vers Tomes/ dans les tableaux d'ancrages (**Ancrages dans le Compendium** / *Ancrages directs*)
    in_anchor_table = False
    for idx, line in enumerate(prd_lines, 1):
        if line.strip().startswith("**Ancrages dans le Compendium**"):
            in_anchor_table = True
            continue
        if in_anchor_table:
            if line.strip().startswith("|"):
                assert "Tomes/" not in line, f"Lien Tomes/ interdit dans tableau d'ancrage L{idx} : {line}"
            elif line.strip() != "":
                in_anchor_table = False
        if "*Ancrages directs*" in line:
            assert "Tomes/" not in line, f"Lien Tomes/ interdit dans *Ancrages directs* L{idx} : {line}"

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

    assert internal_checked >= 1000
    assert file_checked >= 1500
    assert len(re.findall(r"\]\([^)]*Compendium/Compendium\.md", prd_text)) >= 500
    assert len(re.findall(r"\]\([^)]*ouvrage/manuscrit/", prd_text)) >= 140
    assert len(re.findall(r"\]\([^)]*ouvrage/schemas/rendus/", prd_text)) >= 115

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

    # Exhaustivité Annexe B & Annexe D
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
    assert "`135`" in ann_d_text and "`27`" in ann_d_text

    # Hygiène typographique stricte
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

    # Annexe C : 77 jalons consolidés sans doubles parenthèses DAPP
    ann_c_idx = next(i for i, ln in enumerate(prd_lines) if ln.startswith("#### Jalons chronologiques consolidés"))
    assert "77 jalons" in prd_lines[ann_c_idx]
    ann_c_rows = []
    for ln in prd_lines[ann_c_idx + 4 :]:
        if not ln.startswith("|"):
            break
        date_cell = ln.split("|")[1].strip().strip("`")
        assert "((" not in date_cell and "))" not in date_cell, f"Parenthèses doubles DAPP dans date Annexe C : {ln}"
        ann_c_rows.append(ln)
    assert len(ann_c_rows) == 77

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

    # Annexe E : 115 schémas de vulgarisation et concordance 319 figures
    assert "## Annexe E — " in prd_text
    assert any(ln.startswith("#### Catalogue directeur intégral des 115 schémas") for ln in prd_lines)
    ann_e_cat_idx = next(i for i, ln in enumerate(prd_lines) if ln.startswith("#### Catalogue directeur intégral des 115 schémas"))
    ann_e_sch_ids: list[str] = []
    for ln in prd_lines[ann_e_cat_idx + 4 :]:
        if not ln.startswith("|"):
            break
        ann_e_sch_ids.append(ln.split("|")[1].strip().strip("`"))
    assert len(ann_e_sch_ids) == 115
    assert len(set(ann_e_sch_ids)) == 115

    assert not re.search(r"\bsynthetise\b", prd_text, re.IGNORECASE), "Synthetise sans accent détecté dans prd.md"
    ann_e_block = prd_text.split("## Annexe E — ", 1)[1]
    ann_e_stats = ann_e_block.split("#### Répartition des schémas de vulgarisation", 1)[0]
    assert not re.findall(r"\d+\.\d+\s*%", ann_e_stats), f"Point décimal anglais dans Annexe E : {re.findall(r'\d+\.\d+\s*%', ann_e_stats)}"
    assert len(re.findall(r"\d+,\d+\s+%", ann_e_stats)) >= 27


def test_inventaire_319_diagrammes_et_catalogue_115_schemas() -> None:
    import jsonschema

    inv_path = DONNEES_DIR / "inventaire-319-diagrammes.json"
    cat_path = DONNEES_DIR / "catalogue-schemas-prd.json"
    schema_path = DONNEES_DIR / "schema-prd-vulgarisation.json"
    shards_dir = DONNEES_DIR / "prd_schemas_shards"
    assert inv_path.is_file() and cat_path.is_file() and schema_path.is_file()
    for p in (inv_path, cat_path, schema_path):
        assert b"\r\n" not in p.read_bytes(), f"CRLF dans {p}"

    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    figs = inv.get("figures") or []
    assert len(figs) == 319
    assert sum(1 for f in figs if f.get("notation") == "PlantUML") == 253
    assert sum(1 for f in figs if f.get("notation") == "Mermaid") == 66
    for fg in figs:
        assert (REPO_ROOT / fg["source_path"]).is_file(), f"Source absente : {fg['source_path']}"
        assert (REPO_ROOT / fg["rendered_path"]).is_file(), f"Rendu absent : {fg['rendered_path']}"

    val_schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(val_schema)
    shard_files = sorted(shards_dir.glob("schemas-*.json"))
    assert len(shard_files) == 7
    for sf in shard_files:
        assert b"\r\n" not in sf.read_bytes(), f"CRLF dans {sf}"
        sdata = json.loads(sf.read_text(encoding="utf-8"))
        errs = list(validator.iter_errors(sdata))
        assert not errs, f"Erreur Draft202012Validator dans {sf}: {errs[0].message}"

    cat_raw = cat_path.read_text(encoding="utf-8")
    cat = json.loads(cat_raw)
    assert r"\$" not in cat_raw
    assert not re.search(r"\bsynthetise\b", cat_raw, re.IGNORECASE), "Synthetise sans accent détecté dans catalogue-schemas-prd.json"
    all_sch = list(cat["global_schemas"]) + list(cat["chapter_schemas"])
    assert len(cat["global_schemas"]) == 4
    assert len(cat["chapter_schemas"]) == 111
    assert len(all_sch) == 115
    assert cat["summary_stats"]["chapters_covered_count"] == 36
    assert cat["summary_stats"]["families_covered_count"] == 71
    assert cat["summary_stats"]["unique_themes_vulgarized_count"] == 260
    assert cat["tome_figures_coverage"]["unique_linked_figures_count"] == 267
    for sc in all_sch:
        cfig = sc.get("compendium_figure") or {}
        assert (REPO_ROOT / cfig["rendered_path"]).is_file()
        assert (REPO_ROOT / cfig["source_path"]).is_file()
        for fg in sc.get("linked_tome_figures") or []:
            assert (REPO_ROOT / fg["source_path"]).is_file()
            assert (REPO_ROOT / fg["rendered_path"]).is_file()


def test_prd_links_in_readmes_valid() -> None:
    if not PRD_PATH.is_file():
        pytest.skip("prd.md pas encore compilé")
    assert PRD_WEB_ENCODED in PRD_PATH.read_text(encoding="utf-8")
    assert MINDMAP_HTML_ENCODED in PRD_PATH.read_text(encoding="utf-8")
    all_readmes = (
        REPO_ROOT / "README.md",
        REPO_ROOT / "Compendium" / "README.md",
        REPO_ROOT / "Tomes" / "README.md",
        REPO_ROOT / "Sources" / "README.md",
        REPO_ROOT / "Sources" / "Compendium" / "README.md",
        REPO_ROOT / "Sources" / "Tomes" / "README.md",
        CARTO_DIR / "README.md",
        REPO_ROOT / "Sources" / "gabarit-pdf" / "README.md",
    )
    prd_required_readmes = {
        REPO_ROOT / "README.md",
        REPO_ROOT / "Compendium" / "README.md",
        REPO_ROOT / "Tomes" / "README.md",
        REPO_ROOT / "Sources" / "Compendium" / "README.md",
        CARTO_DIR / "README.md",
    }
    for md_path in all_readmes:
        content = md_path.read_text(encoding="utf-8")
        assert b"\r\n" not in md_path.read_bytes(), f"CRLF détecté dans {md_path}"
        assert OLD_MINDMAP_NAME not in content and OLD_MINDMAP_ENCODED not in content, (
            f"Référence obsolète à MindMap Corpus dans {md_path}"
        )
        assert MINDMAP_HTML_ENCODED in content, f"Lien MindMap Compendium manquant dans {md_path}"
        assert PRD_WEB_ENCODED in content, f"Lien PRD Web manquant dans {md_path}"
        if md_path in prd_required_readmes:
            assert "prd.md" in content, f"Lien vers prd.md manquant dans {md_path}"
        for raw_target in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)", content):
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = (md_path.parent / unquote(raw_target)).resolve()
            assert target_path.exists(), f"Lien cassé dans {md_path}: {raw_target}"

    carto_readme = (CARTO_DIR / "README.md").read_text(encoding="utf-8")
    prd_text = PRD_PATH.read_text(encoding="utf-8")
    prd_lines_cnt = len(prd_text.splitlines())
    prd_words_cnt = len(prd_text.split())
    mm_bytes = MINDMAP_HTML_PATH.stat().st_size
    pw_bytes = PRD_WEB_HTML_PATH.stat().st_size
    assert f"`{prd_lines_cnt:,}".replace(",", " ") in carto_readme
    assert f"`{prd_words_cnt:,}".replace(",", " ") in carto_readme
    assert f"`{mm_bytes:,}".replace(",", " ") in carto_readme
    assert f"`{pw_bytes:,}".replace(",", " ") in carto_readme
    assert "`77` jalons" in carto_readme
    assert "`237` entrées uniques" in carto_readme
    assert "`115`" in carto_readme


def test_prd_web_data_json_and_parity() -> None:
    assert PRD_WEB_DATA_PATH.is_file()
    data = json.loads(PRD_WEB_DATA_PATH.read_text(encoding="utf-8"))
    assert len(data["executive_summary"]["sections"]) == 5
    assert len(data["executive_summary"].get("vulgarization_schemas") or []) == 4
    assert data["executive_summary"]["sections"][3]["kpi_table"] is not None
    assert len(data["parties"]) == 12
    assert len(data["chapters"]) == 36
    assert all(len(ch.get("parts_present") or []) >= 1 for ch in data["chapters"]), "parts_present vide sur un chapitre PRD"
    assert len(data["annexes"]) == 5
    assert [a["annexe_code"] for a in data["annexes"]] == ["A", "B", "C", "D", "E"]
    assert all(ch.get("schemas_anchor") and len(ch.get("vulgarization_schemas") or []) >= 1 for ch in data["chapters"])
    assert sum(len(ch["vulgarization_schemas"]) for ch in data["chapters"]) == 111
    assert data["meta"]["annexes_count"] == 5
    assert data["meta"]["schemas_count"] == 115
    assert data["meta"]["tome_figures_count"] == 319

    # Ancres de chapitres exclusivement sur Compendium/Compendium.md ou Sources/Compendium/ouvrage/manuscrit/ (0 Tomes/)
    for ch in data["chapters"]:
        anchors_list = ch.get("targeted_content", {}).get("corpus_anchors", [])
        assert any(a.get("file") == "Compendium/Compendium.md" for a in anchors_list), (
            f"Chapitre {ch.get('chapter_number')} sans ancre Compendium.md"
        )
        for anchor in anchors_list:
            f_val = str(anchor.get("file", ""))
            assert f_val == "Compendium/Compendium.md" or f_val.startswith("Sources/Compendium/ouvrage/manuscrit/"), (
                f"Ancre hors Compendium : {anchor}"
            )
            assert "Tomes/" not in f_val, f"Ancre Tomes/ résiduelle : {anchor}"

    # Glossaire 56 vedettes & socle probatoire
    glossary = data.get("glossary") or []
    assert len(glossary) == 56
    assert any(
        str(g.get("fr", "")).lower() == "agentivité des systèmes"
        and str(g.get("en", "")).lower() == "system agency"
        for g in glossary
    )

    ann_e = next(a for a in data["annexes"] if a["annexe_code"] == "E")
    assert len(ann_e["catalogue_all"]) == 115
    assert len(ann_e["tome_inventory_summary"]["figures"]) == 319

    fams = [f for ch in data["chapters"] for f in ch["targeted_content"]["families_and_themes"]]
    thms = [t for f in fams for t in f["themes_targeted"]]
    assert len(fams) == 71
    assert len(thms) == 260

    ann_b = next(a for a in data["annexes"] if a["annexe_code"] == "B")
    ann_c = next(a for a in data["annexes"] if a["annexe_code"] == "C")
    ann_d = next(a for a in data["annexes"] if a["annexe_code"] == "D")
    assert len(ann_b["tensions"]) == 67
    assert len(ann_c["reconciliations"]) == 5
    assert len(ann_c["timeline"]) == 77
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
    assert len(data["lookup"]["unit_id_to_chapter"]) == 42


def test_prd_web_standalone_html_and_nodejs_smoke() -> None:
    assert PRD_WEB_HTML_PATH.is_file()
    raw_bytes = PRD_WEB_HTML_PATH.read_bytes()
    assert not raw_bytes.startswith(b"\xef\xbb\xbf"), "BOM UTF-8 détecté dans PRD Web HTML"
    assert b"\r\n" not in raw_bytes, "CRLF détecté dans PRD Web HTML"
    html = PRD_WEB_HTML_PATH.read_text(encoding="utf-8")
    assert "__PRD_DATA_JSON__" not in html
    assert OLD_MINDMAP_NAME not in html and OLD_MINDMAP_ENCODED not in html
    assert 'id="prd-open-mindmap-link"' in html
    assert 'id="prd-glossary-btn"' in html
    assert '<a class="skip-link" href="#prd-main">' in html
    assert ".skip-link" in html
    assert 'id="prd-active-filters-strip"' in html
    m_rnav = re.search(r"\.reading-nav\s*\{([^}]+)\}", html)
    assert m_rnav is not None and "position: sticky" in m_rnav.group(1)
    assert "tome-concordance-details" in html
    m_print_fn = re.search(r"function\s+preparePrdForPrint\s*\(\)\s*\{([\s\S]*?)\n\s{6}\}", html)
    assert m_print_fn is not None and "details.tome-concordance-details" in m_print_fn.group(1)
    assert not PRD_WEB_DATA_PATH.read_bytes().startswith(b"\xef\xbb\xbf") and b"\r\n" not in PRD_WEB_DATA_PATH.read_bytes()
    assert not (CARTO_DIR / "README.md").read_bytes().startswith(b"\xef\xbb\xbf") and b"\r\n" not in (CARTO_DIR / "README.md").read_bytes()

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
    assert len(parsed["glossary"]) == 56

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
    const fsPath = require("path");
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
    if (idx.parties.length !== 12 || idx.chapters.length !== 36 || idx.annexes.length !== 5) {
      throw new Error("Cardinaux index PrdWebEngine invalides");
    }
    if (!idx.glossary || idx.glossary.length !== 56) {
      throw new Error("Glossaire PrdWebEngine != 56");
    }

    const sHits = eng.searchPrd(idx, "Lusser", 10);
    if (sHits.length === 0) throw new Error("searchPrd('Lusser') vide");
    const sGloss = eng.searchPrd(idx, "Agentivité des systèmes", 10);
    if (!sGloss.some(h => h.kind === "glossary")) {
      throw new Error("searchPrd('Agentivité des systèmes') ne remonte pas le glossaire");
    }
    const fRes = eng.filterPrd(idx, { domain: "D07" });
    if (!fRes.active || fRes.counts.chapters !== 3) {
      throw new Error("filterPrd D07 invalide: " + JSON.stringify(fRes.counts));
    }
    const mmUrl = eng.mindmapHref("mindmap", "THM_loi-de-lusser");
    if (!mmUrl.includes("MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html#view=mindmap&node=THM_loi-de-lusser")) {
      throw new Error("mindmapHref invalide: " + mmUrl);
    }
    const parsedThm = eng.parseHash("#thm=loi-de-lusser", idx);
    if (!parsedThm || parsedThm.kind !== "chapter" || Number(parsedThm.chapterNumber) !== 2) {
      throw new Error("parseHash #thm=loi-de-lusser invalide: " + JSON.stringify(parsedThm));
    }
    const parsedGloss = eng.parseHash("#glossary", idx);
    if (!parsedGloss || parsedGloss.kind !== "glossary") {
      throw new Error("parseHash #glossary invalide: " + JSON.stringify(parsedGloss));
    }
    const parsedChFull = eng.parseHash("#ch=15&mode=full", idx);
    if (!parsedChFull || parsedChFull.kind !== "chapter" || Number(parsedChFull.chapterNumber) !== 15 || parsedChFull.mode !== "full") {
      throw new Error("parseHash #ch=15&mode=full invalide: " + JSON.stringify(parsedChFull));
    }
    const parsedModeOnly = eng.parseHash("#mode=full", idx);
    if (!parsedModeOnly || parsedModeOnly.mode !== "full") {
      throw new Error("parseHash #mode=full invalide: " + JSON.stringify(parsedModeOnly));
    }
    if (eng.targetToHash({ kind: "chapter", chapterNumber: 15 }, "full") !== "#ch=15&mode=full") {
      throw new Error("targetToHash mode=full invalide");
    }
    const corpUrl = eng.corpusHref("Compendium/Compendium.md", 215);
    if (corpUrl !== "../../Compendium/Compendium.md#L215") {
      throw new Error("corpusHref PRD Web invalide: " + corpUrl);
    }

    const toc = eng.renderTocHtml(idx, "", { tocExpanded: new Set(), target: { kind: "exec" } }, { active: false });
    if (!toc.html || toc.count < 12 || !toc.html.includes("Glossaire")) throw new Error("renderTocHtml incomplet");
    const fullHtml = eng.renderContentHtml(idx, { mode: "full", target: { kind: "exec" }, filters: {}, highlightQuery: "" }, { active: false, counts: { themes: 260, chapters: 36, parties: 12 } });
    for (const marker of [
      "Partie I", "Partie XII", "Chapitre 01", "Chapitre 36",
      "Annexe A", "Annexe D", "Annexe E", "THM_loi-de-lusser",
      "Panorama visuel directeur", "01.3 Schémas de vulgarisation à intégrer", "36.3 Schémas de vulgarisation à intégrer",
      "SCH-00-01", "SCH-15-03", "SCH-36-03", "135"
    ]) {
      if (!fullHtml.includes(marker)) throw new Error("Contenu mode intégral PrdWebEngine incomplet: " + marker);
    }
    const allSchemaIds = (data.executive_summary.vulgarization_schemas || []).map(s => s.schema_id)
      .concat(data.chapters.flatMap(c => (c.vulgarization_schemas || []).map(s => s.schema_id)));
    if (allSchemaIds.length !== 115) throw new Error("Nombre de schémas != 115: " + allSchemaIds.length);
    for (const sid of allSchemaIds) {
      if (!fullHtml.includes(sid)) throw new Error("Schéma manquant dans PRD Web fullHtml: " + sid);
    }
    if (!fullHtml.includes("prd-glossary-table")) {
      throw new Error("Mode intégral PRD Web omet le glossaire #prd-glossary-table");
    }
    if (!fullHtml.includes('class="reading-nav"')) {
      throw new Error("Mode intégral PRD Web omet .reading-nav");
    }
    if (!fullHtml.includes('<details class="tome-concordance-details"')) {
      throw new Error("Mode intégral PRD Web omet <details class=\"tome-concordance-details\">");
    }
    const prdSchemaImgs = Array.from(fullHtml.matchAll(/<img[^>]+src="(\.\.\/\.\.\/Sources\/Compendium\/ouvrage\/schemas\/rendus\/[^"]+)"/g), m => m[1]);
    if (prdSchemaImgs.length !== 115) {
      throw new Error("Prévisualisations <img> des 115 schémas manquantes dans PRD Web: " + prdSchemaImgs.length);
    }

    const compMdHrefs = Array.from(fullHtml.matchAll(/href="(\.\.\/\.\.\/Compendium\/Compendium\.md[^"]*)"/g), m => m[1]);
    if (compMdHrefs.length < 36) throw new Error("Trop peu de liens ../../Compendium/Compendium.md dans PRD Web: " + compMdHrefs.length);
    const compRendus = Array.from(fullHtml.matchAll(/href="(\.\.\/\.\.\/Sources\/Compendium\/ouvrage\/schemas\/rendus\/[^"#]+)"/g), m => m[1]);
    if (compRendus.length < 100) throw new Error("Trop peu de liens rendus Compendium dans PRD Web: " + compRendus.length);
    for (const rawHref of new Set([...compMdHrefs.map(u => u.split("#")[0]), ...compRendus])) {
      const diskPath = fsPath.resolve(fsPath.dirname(process.argv[1]), decodeURIComponent(rawHref));
      if (!fs.existsSync(diskPath)) throw new Error("Lien Compendium cassé sur disque: " + diskPath);
    }

    // Mode glossaire ciblé (#glossary) + table #prd-glossary-table
    const glossHtml = eng.renderContentHtml(idx, { mode: "targeted", target: { kind: "glossary" }, filters: {}, highlightQuery: "" }, { active: false, counts: { themes: 260, chapters: 36, parties: 12 } });
    for (const gm of ['id="prd-glossary"', 'id="prd-glossary-table"', "Agentivité des systèmes", "system agency", "ch01", "135", "27", "37/37"]) {
      if (!glossHtml.includes(gm)) throw new Error("Rendu glossaire #prd-glossary incomplet: " + gm);
    }

    const noCodeTags = fullHtml.replace(/<code[^>]*>[\s\S]*?<\/code>/gi, "");
    if (noCodeTags.includes("`")) throw new Error("Backtick brut détecté hors <code> dans PRD Web HTML");
    if (/(^|[\s(>])\*\*[^\s*](?:[^*\n]*?[^\s*])?\*\*(?=[\s.,;:!?<)]|$)/.test(noCodeTags)) {
      throw new Error("**gras** brut détecté dans PRD Web HTML");
    }
    if (fullHtml.includes("\\$")) throw new Error("Literal backslash-dollar dans PRD Web HTML");
    if (/\bsynthetise\b/i.test(fullHtml)) throw new Error("Synthetise sans accent détecté dans PRD Web HTML");

    // Smoke mountApp avec stub DOM léger et hash #glossary puis #part=part-07
    const stubEls = {};
    const makeStubEl = (id) => ({
      id, textContent: "", innerHTML: "", value: "", style: {},
      classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
      setAttribute(k, v) { this["attr_" + k] = v; },
      getAttribute(k) { return this["attr_" + k] ?? null; },
      appendChild(){}, addEventListener(){}, scrollIntoView(){}, focus(){}, querySelector: () => null, querySelectorAll: () => []
    });
    for (const k of [
      "prd-web-data", "prd-global-title", "prd-global-meta", "prd-kpi-strip",
      "prd-content", "prd-toc-tree", "prd-toc-count", "prd-open-mindmap-link",
      "prd-filter-summary", "prd-glossary-btn"
    ]) {
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
    const appInst = eng.mountApp(docStub, { location: { hash: "#glossary" }, addEventListener(){} });
    if (!appInst || appInst.getState().target.kind !== "glossary" || !stubEls["prd-content"].innerHTML.includes("prd-glossary-table")) {
      throw new Error("mountApp smoke #glossary échoué");
    }
    if (!String(stubEls["prd-open-mindmap-link"].getAttribute("href") || "").includes("MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html")) {
      throw new Error("#prd-open-mindmap-link ne pointe pas vers MindMap Compendium: " + stubEls["prd-open-mindmap-link"].getAttribute("href"));
    }

    // Non-régression : mountApp honore #ch=15&mode=full et ensureVisible lève les filtres bloquants sur thème et partie
    const appFull = eng.mountApp(docStub, { location: { hash: "#ch=15&mode=full" }, addEventListener(){} });
    if (appFull.getState().mode !== "full" || Number(appFull.getState().target.chapterNumber) !== 15) {
      throw new Error("mountApp n'a pas honoré #ch=15&mode=full: " + JSON.stringify(appFull.getState()));
    }
    appFull.getState().mode = "targeted";
    appFull.getState().filters.role = "AE";
    appFull.navigateToTarget({ kind: "chapter", chapterNumber: 1, focusKind: "thm", focusId: "raisonnement-inference-limites-planification" }, { ensureVisible: true });
    if (appFull.getState().filters.role !== "" || !stubEls["prd-content"].innerHTML.includes("THM_raisonnement-inference-limites-planification")) {
      throw new Error("ensureVisible n'a pas levé le filtre Rôle=AE masquant le thème ciblé");
    }
    appFull.getState().filters.domain = "D07";
    appFull.navigateToTarget({ kind: "part", domainId: "D01" }, { ensureVisible: true });
    if (appFull.getState().filters.domain !== "" || !stubEls["prd-content"].innerHTML.includes("Partie I")) {
      throw new Error("ensureVisible n'a pas levé le filtre Domaine=D07 masquant Partie I");
    }

    // Régression E2E : repliage #prd-filters-toggle-btn avec fCount > 0 et resize 1440 -> 390 -> 1440
    const makeInteractiveEl = (id) => {
      const classes = new Set();
      const listeners = Object.create(null);
      const el = {
        id, textContent: "", innerHTML: "", value: "", style: {},
        classList: {
          add(c) { classes.add(c); },
          remove(c) { classes.delete(c); },
          toggle(c, force) {
            if (force === undefined) {
              if (classes.has(c)) { classes.delete(c); return false; }
              classes.add(c); return true;
            }
            if (force) classes.add(c); else classes.delete(c);
            return Boolean(force);
          },
          contains(c) { return classes.has(c); }
        },
        setAttribute(k, v) { el["attr_" + k] = String(v); },
        getAttribute(k) { return el["attr_" + k] ?? null; },
        appendChild(){}, scrollIntoView(){}, focus(){}, querySelector: () => null, querySelectorAll: () => [],
        addEventListener(type, fn) { (listeners[type] = listeners[type] || []).push(fn); },
        trigger(type, ev = {}) { (listeners[type] || []).forEach(fn => fn(Object.assign({ target: el, preventDefault(){}, stopPropagation(){} }, ev))); }
      };
      return el;
    };
    const interactiveEls = {};
    for (const k of [
      "prd-web-data", "prd-global-title", "prd-global-meta", "prd-kpi-strip",
      "prd-content", "prd-toc-tree", "prd-toc-count", "prd-open-mindmap-link",
      "prd-filter-summary", "prd-glossary-btn", "prd-filters-toggle-btn",
      "prd-filter-bar", "prd-filter-autonomy", "prd-reset-filters-btn",
      "prd-toc", "prd-toc-toggle-btn", "prd-toc-backdrop", "prd-main"
    ]) {
      interactiveEls[k] = makeInteractiveEl(k);
    }
    interactiveEls["prd-web-data"].textContent = jsonMatch[1];
    const docInteractive = {
      documentElement: makeInteractiveEl("html"),
      body: makeInteractiveEl("body"),
      getElementById: (id) => interactiveEls[id] || null,
      createElement: (tag) => makeInteractiveEl(tag),
      addEventListener(){}, querySelector: () => null, querySelectorAll: () => []
    };
    const winListeners = Object.create(null);
    const winInteractive = {
      innerWidth: 1440,
      location: { hash: "#ch=01" },
      addEventListener(type, fn) { (winListeners[type] = winListeners[type] || []).push(fn); },
      trigger(type) { (winListeners[type] || []).forEach(fn => fn({})); }
    };
    const app2 = eng.mountApp(docInteractive, winInteractive);
    if (!app2 || !app2.getState().tocOpen || app2.getState().filtersOpen !== false || !interactiveEls["prd-filter-bar"].classList.contains("collapsed") || interactiveEls["prd-filters-toggle-btn"].getAttribute("aria-expanded") !== "false" || interactiveEls["prd-filters-toggle-btn"].classList.contains("active")) {
      throw new Error("État initial desktop 1440px invalide (filtersOpen doit être false par défaut)");
    }
    interactiveEls["prd-filters-toggle-btn"].trigger("click");
    if (app2.getState().filtersOpen !== true || interactiveEls["prd-filter-bar"].classList.contains("collapsed") || interactiveEls["prd-filters-toggle-btn"].getAttribute("aria-expanded") !== "true") {
      throw new Error("Ouverture #prd-filters-toggle-btn sans filtre échouée");
    }
    interactiveEls["prd-filter-autonomy"].value = "L2";
    interactiveEls["prd-filter-autonomy"].trigger("change", { target: { value: "L2" } });
    interactiveEls["prd-filters-toggle-btn"].trigger("click");
    if (app2.getState().filtersOpen !== false || !interactiveEls["prd-filter-bar"].classList.contains("collapsed") || interactiveEls["prd-filters-toggle-btn"].getAttribute("aria-expanded") !== "false") {
      throw new Error("Repliage #prd-filters-toggle-btn impossible avec filtre actif sur desktop");
    }
    interactiveEls["prd-filters-toggle-btn"].trigger("click");
    if (app2.getState().filtersOpen !== true || interactiveEls["prd-filter-bar"].classList.contains("collapsed")) {
      throw new Error("Réouverture #prd-filters-toggle-btn avec filtre actif échouée");
    }
    interactiveEls["prd-reset-filters-btn"].trigger("click");
    interactiveEls["prd-filters-toggle-btn"].trigger("click");
    if (app2.getState().filtersOpen !== false || !interactiveEls["prd-filter-bar"].classList.contains("collapsed")) {
      throw new Error("Repliage #prd-filters-toggle-btn après reset échoué");
    }
    winInteractive.innerWidth = 390;
    winInteractive.trigger("resize");
    if (app2.getState().tocOpen !== false || !interactiveEls["prd-toc"].classList.contains("collapsed") || interactiveEls["prd-toc-backdrop"].classList.contains("open")) {
      throw new Error("Resize 1440->390 a laissé le tiroir TDM ou le voile ouvert");
    }
    interactiveEls["prd-toc-toggle-btn"].trigger("click");
    if (!app2.getState().tocOpen || !interactiveEls["prd-toc-backdrop"].classList.contains("open")) {
      throw new Error("Ouverture manuelle du tiroir TDM sur 390px échouée");
    }
    winInteractive.innerWidth = 1440;
    winInteractive.trigger("resize");
    if (!app2.getState().tocOpen || interactiveEls["prd-toc"].classList.contains("collapsed") || interactiveEls["prd-toc-backdrop"].classList.contains("open") || app2.getState().filtersOpen !== false) {
      throw new Error("Resize 390->1440 invalide (filtersOpen doit rester false sans filtre actif)");
    }
    winInteractive.innerWidth = 390;
    winInteractive.trigger("resize");
    if (app2.getState().tocOpen !== false || interactiveEls["prd-toc-backdrop"].classList.contains("open")) {
      throw new Error("Second resize 1440->390 a laissé le tiroir TDM ou le voile ouvert");
    }
    interactiveEls["prd-main"].scrollTop = 240;
    interactiveEls["prd-main"].trigger("scroll");
    if (!interactiveEls["prd-main"].classList.contains("is-scrolled")) {
      throw new Error("Classe .is-scrolled manquante après scrollTop > 160");
    }
    interactiveEls["prd-main"].scrollTop = 0;
    interactiveEls["prd-main"].trigger("scroll");
    if (interactiveEls["prd-main"].classList.contains("is-scrolled")) {
      throw new Error("Classe .is-scrolled persistante à scrollTop === 0");
    }
    """

    proc = subprocess.run(
        [node_exe, "-e", node_script, str(PRD_WEB_HTML_PATH)],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, f"Échec Node.js PRD Web:\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"
