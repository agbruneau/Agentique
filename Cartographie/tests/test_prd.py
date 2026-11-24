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
import sys
from urllib.parse import unquote

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
CARTO_DIR = REPO_ROOT / "Cartographie"
DONNEES_DIR = CARTO_DIR / "donnees"
OUTILS_DIR = CARTO_DIR / "outils"
PRD_PATH = REPO_ROOT / "prd.md"

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


def test_prd_links_in_readmes_valid() -> None:
    if not PRD_PATH.is_file():
        pytest.skip("prd.md pas encore compilé")
    for md_path in (REPO_ROOT / "README.md", CARTO_DIR / "README.md"):
        content = md_path.read_text(encoding="utf-8")
        assert "prd.md" in content, f"Lien vers prd.md manquant dans {md_path}"
        for raw_target in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)", content):
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = (md_path.parent / unquote(raw_target)).resolve()
            assert target_path.exists(), f"Lien cassé dans {md_path}: {raw_target}"
