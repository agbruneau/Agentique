"""Suite de tests automatisés pour le plan directeur ``Compendium/plan.md``.

Vérifie :
- les fonctions unitaires d'hygiène typographique ``fr-CA``, de calibrage et
  d'extraction structurelle, ainsi que l'intégrité des jeux de données sources ;
- l'absence de ``Compendium/.plan_lots`` une fois ``Compendium/plan.md`` assemblé ;
- l'encodage UTF-8 sans BOM, les fins de ligne LF strictes, l'absence de
  placeholders et la conformité intégrale à la charte ``fr-CA`` (§ 5 de ``prd.md``) ;
- la structure complète (``Goal``/``Architecture``/``Tech Stack``/``Spec``,
  6 sections, 9 tâches, 12 parties, 36 fiches chapitres >= 400 mots, 5 annexes,
  ``CA-01``..``CA-22``) et le volume cible ``[25_000, 45_000]`` mots ;
- la couverture à 100 % du MindMap (12 domaines, 36 sous-domaines, 71 familles,
  260 ``THM_*`` et ``canonical_slug``) et des 115 schémas ``SCH-00-01``..``SCH-36-04`` ;
- la validité à 100 % des ancres internes, liens relatifs (dont ``prd.md#...`` et
  bornes ``#Lxxx`` sur ``Corpus/*.md``), tableaux GFM et liens dans les README.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import unquote

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
CARTO_DIR = REPO_ROOT / "Tomes" / "Cartographie"
DONNEES_DIR = CARTO_DIR / "donnees"
OUTILS_DIR = CARTO_DIR / "outils"
COMPENDIUM_DIR = REPO_ROOT / "Compendium"
PLAN_PATH = COMPENDIUM_DIR / "plan.md"
PRD_PATH = COMPENDIUM_DIR / "prd.md"
PLAN_LOTS_DIR = COMPENDIUM_DIR / ".plan_lots"

sys.path.insert(0, str(OUTILS_DIR))
import compiler_prd as cp  # noqa: E402
import extraire_structure as es  # noqa: E402

INDEFINITE_ON_RE = re.compile(r"\b(?:[ldLD]['’])?[oO]n\b")
SYSTEMS_OF_AGENCY_RE = re.compile(r"\bSystems? of Agency\b", re.IGNORECASE)
UNESCAPED_DOLLAR_RE = re.compile(r"(?<!\\)\$")
ASCII_ARROW_RE = re.compile(r"<->|(?<![<=-])->(?![>=])")
ASCII_COMP_RE = re.compile(r"(?<![<>=])(?:<=|>=)(?!=)")
ASCII_LINE_RANGE_RE = re.compile(r"\bL\d+-L?\d+\b")
ENGLISH_PERCENT_RE = re.compile(r"\d+\.\d+\s*%")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:-]+(?:\|[\s:-]+)+\|?\s*$")


def strip_inline_code(line: str) -> str:
    """Retire les segments de code en ligne délimités par un ou plusieurs backticks."""
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == "`":
            j = i
            while j < n and line[j] == "`":
                j += 1
            tick_len = j - i
            close_pat = "`" * tick_len
            k = line.find(close_pat, j)
            while k != -1:
                after = k + tick_len
                before_ok = k == 0 or line[k - 1] != "`"
                after_ok = after == n or line[after] != "`"
                if before_ok and after_ok:
                    break
                k = line.find(close_pat, k + 1)
            if k != -1:
                i = k + tick_len
                continue
        out.append(line[i])
        i += 1
    return "".join(out)


def strip_link_urls(line: str) -> str:
    """Vide les cibles ``(...)`` des liens Markdown tout en conservant le libellé."""
    return re.sub(r"\]\([^)]+\)", "]()", line)


def check_charter_violations(
    lines: list[str],
    code_lines: set[int],
) -> dict[str, list[tuple[int, str]]]:
    """Détecte les écarts à la charte ``fr-CA`` hors blocs de code et spans `` `...` ``."""
    violations: dict[str, list[tuple[int, str]]] = {
        "unescaped_dollars": [],
        "ascii_arrows": [],
        "ascii_comparators": [],
        "ascii_line_ranges": [],
        "systems_of_agency": [],
        "indefinite_on": [],
        "english_decimal_percent": [],
    }
    for lno, raw_ln in enumerate(lines, 1):
        if lno in code_lines:
            continue
        no_inline = strip_inline_code(raw_ln)
        no_urls = strip_link_urls(no_inline)
        no_quotes = re.sub(r"«[^»]*»", "", no_urls)

        if UNESCAPED_DOLLAR_RE.search(no_inline):
            violations["unescaped_dollars"].append((lno, raw_ln[:100]))
        if ASCII_ARROW_RE.search(no_inline):
            violations["ascii_arrows"].append((lno, raw_ln[:100]))
        if ASCII_COMP_RE.search(no_inline):
            violations["ascii_comparators"].append((lno, raw_ln[:100]))
        if ASCII_LINE_RANGE_RE.search(no_inline):
            violations["ascii_line_ranges"].append((lno, raw_ln[:100]))
        if SYSTEMS_OF_AGENCY_RE.search(no_urls):
            violations["systems_of_agency"].append((lno, raw_ln[:100]))
        if INDEFINITE_ON_RE.search(no_quotes):
            violations["indefinite_on"].append((lno, raw_ln[:100]))
        if ENGLISH_PERCENT_RE.search(no_urls):
            violations["english_decimal_percent"].append((lno, raw_ln[:100]))
    return violations


def extract_heading_sections(
    lines: list[str],
    headings: list[tuple[int, int, str]],
    target_level: int,
) -> list[tuple[str, int, int, str]]:
    """Extrait chaque bloc délimité par un titre de niveau ``target_level``."""
    sections: list[tuple[str, int, int, str]] = []
    total = len(lines)
    for idx, (line_no, level, title) in enumerate(headings):
        if level != target_level:
            continue
        end_line = total
        for next_line_no, next_level, _ in headings[idx + 1 :]:
            if next_level <= target_level:
                end_line = next_line_no - 1
                break
        block = "\n".join(lines[line_no - 1 : end_line])
        sections.append((title, line_no, end_line, block))
    return sections


def table_col_count(row_line: str) -> int:
    """Compte le nombre de colonnes d'une ligne de tableau Markdown GFM."""
    stripped = row_line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith("\\|"):
        stripped = stripped[:-1]
    return len(re.split(r"(?<!\\)\|", stripped))


def check_gfm_tables(lines: list[str], code_lines: set[int]) -> int:
    """Vérifie la cohérence du nombre de colonnes de tous les tableaux GFM."""
    tables_checked = 0
    idx = 0
    n = len(lines)
    while idx < n:
        ln_cur = lines[idx]
        if (
            (idx + 1) not in code_lines
            and ln_cur.strip().startswith("|")
            and idx + 1 < n
            and TABLE_SEP_RE.match(lines[idx + 1])
        ):
            tables_checked += 1
            hdr_cols = table_col_count(ln_cur)
            assert table_col_count(lines[idx + 1]) == hdr_cols, (
                f"Séparateur de tableau incohérent à L{idx + 2}"
            )
            row_idx = idx + 2
            while (
                row_idx < n
                and (row_idx + 1) not in code_lines
                and lines[row_idx].strip().startswith("|")
            ):
                assert table_col_count(lines[row_idx]) == hdr_cols, (
                    f"Tableau GFM cassé à L{row_idx + 1} (attendu {hdr_cols} colonnes)"
                )
                row_idx += 1
            idx = row_idx
        else:
            idx += 1
    return tables_checked


def expected_chapter_budget(theme_count: int) -> tuple[int, int, int]:
    """Calcule ``(C, min_words, max_words)`` selon ``C = 3 100 + 190 * t`` (± 8 %)."""
    target = 3100 + 190 * theme_count
    return target, math.ceil(0.92 * target), math.floor(1.08 * target)


def _require_assembled_plan() -> tuple[bytes, str, list[str]]:
    if not PLAN_PATH.is_file():
        pytest.skip("Compendium/plan.md pas encore assemblé (en attente des lots)")
    raw_bytes = PLAN_PATH.read_bytes()
    text = raw_bytes.decode("utf-8")
    return raw_bytes, text, text.splitlines()


def test_unit_charter_and_calibration_helpers() -> None:
    seen: dict[str, int] = {}
    anc = cp.gfm_anchor("1. Gouvernance éditoriale (`AO-01` à `AO-08`)", seen)
    assert anc == "1-gouvernance-éditoriale-ao-01-à-ao-08"
    assert "%20" in cp.encode_rel_url("../Tomes/Tome 7 - Gouverner/README.md")

    assert expected_chapter_budget(4) == (3860, 3552, 4168)

    sample = [
        "# Titre",
        "Prose conforme : `->`, `Systems of Agency`, `$HOME`, `on`, « on dit que » et 99,5 % sur `L10-L20`.",
        "Prose avec `` `code` `` et coût de 10\\$ CA.",
        "```python",
        "x = 10  # $ -> <= >= on Systems of Agency 99.5%",
        "```",
        "| Col A | Col B |",
        "|---|---|",
        "| v1 | v2 |",
    ]
    headings, _, code_lines = es.parse_markdown_lines(sample)
    assert len(headings) == 1
    assert code_lines == {4, 5, 6}
    clean_v = check_charter_violations(sample, code_lines)
    assert all(not items for items in clean_v.values()), clean_v
    assert check_gfm_tables(sample, code_lines) == 1

    dirty = [
        "Coût de 10 $ avec flèche -> et <= 5 sur L10-L20.",
        "Les Systems of Agency où l'on observe 99.5 %.",
    ]
    dirty_v = check_charter_violations(dirty, set())
    assert len(dirty_v["unescaped_dollars"]) == 1
    assert len(dirty_v["ascii_arrows"]) == 1
    assert len(dirty_v["ascii_comparators"]) == 1
    assert len(dirty_v["ascii_line_ranges"]) == 1
    assert len(dirty_v["systems_of_agency"]) == 1
    assert len(dirty_v["indefinite_on"]) == 1
    assert len(dirty_v["english_decimal_percent"]) == 1

    broken_table = ["| A | B |", "|---|---|", "| seul |"]
    with pytest.raises(AssertionError, match="Tableau GFM cassé"):
        check_gfm_tables(broken_table, set())


def test_unit_plan_reference_datasets() -> None:
    mm_path = DONNEES_DIR / "corpus-mindmap-data.json"
    cat_path = DONNEES_DIR / "catalogue-schemas-prd.json"
    assert mm_path.is_file() and cat_path.is_file()

    bundle = json.loads(mm_path.read_text(encoding="utf-8"))
    nodes = bundle["nodes"]
    by_id = {n["node_id"]: n for n in nodes}

    domains = [n for n in nodes if n["node_kind"] == "domain"]
    subdomains = [n for n in nodes if n["node_kind"] == "subdomain"]
    families = [n for n in nodes if n["node_kind"] == "family"]
    themes = [n for n in nodes if n["node_kind"] == "theme"]

    assert len(domains) == 12
    assert len(subdomains) == 36
    assert len(families) == 71
    assert len(themes) == 260
    assert len({t["canonical_slug"] for t in themes}) == 260

    total_chapter_words = 0
    for sub in subdomains:
        t_count = sum(len(by_id[fid]["children_ids"]) for fid in sub["children_ids"])
        c_target, _, _ = expected_chapter_budget(t_count)
        total_chapter_words += c_target
    assert total_chapter_words == 161_000

    cat = json.loads(cat_path.read_text(encoding="utf-8"))
    assert len(cat["global_schemas"]) == 4
    assert len(cat["chapter_schemas"]) == 111
    assert len(cat["global_schemas"]) + len(cat["chapter_schemas"]) == 115


def test_plan_encoding_hygiene_and_charter() -> None:
    raw_bytes, plan_text, plan_lines = _require_assembled_plan()

    assert not PLAN_LOTS_DIR.exists(), "Compendium/.plan_lots doit être supprimé après assemblage"
    assert not raw_bytes.startswith(b"\xef\xbb\xbf"), "BOM UTF-8 détecté dans Compendium/plan.md"
    assert b"\r\n" not in raw_bytes, "Séquences CRLF détectées dans Compendium/plan.md"
    assert "\ufffd" not in plan_text, "Caractère de remplacement U+FFFD détecté dans Compendium/plan.md"

    for pat in cp.PLACEHOLDER_PATTERNS:
        bad_lines = [
            (idx, ln[:100])
            for idx, ln in enumerate(plan_lines, 1)
            if pat.search(ln)
            and not (
                pat.pattern == r"\bTBD\b"
                and "ligne directrice B-15 du BSIF" in ln
                and "SRC-067" in ln
            )
        ]
        assert not bad_lines, f"Placeholder détecté dans plan.md ({pat.pattern}) : {bad_lines[:3]}"

    _, _, code_lines = es.parse_markdown_lines(plan_lines)
    violations = check_charter_violations(plan_lines, code_lines)
    for key, hits in violations.items():
        assert not hits, f"Violation charte fr-CA ({key}) dans plan.md : {hits[:5]}"


def test_plan_structure_and_volume() -> None:
    _, plan_text, plan_lines = _require_assembled_plan()

    word_count = len(plan_text.split())
    assert 25_000 <= word_count <= 45_000, f"Volume hors plage [25 000, 45 000] : {word_count} mots"

    for token in ("Goal", "Architecture", "Tech Stack", "Spec"):
        assert token in plan_text, f"Jeton de cadrage manquant dans plan.md : {token}"

    headings, _, _ = es.parse_markdown_lines(plan_lines)
    h2_titles = [t for _, lvl, t in headings if lvl == 2]
    h3_titles = [t for _, lvl, t in headings if lvl == 3]
    h4_titles = [t for _, lvl, t in headings if lvl == 4]

    for sec_num in range(1, 7):
        assert any(t.startswith(f"{sec_num}. ") for t in h2_titles), (
            f"Section H2 manquante : ## {sec_num}."
        )

    h3_sections = extract_heading_sections(plan_lines, headings, 3)
    task_sections = [s for s in h3_sections if re.match(r"^Task [1-9]\b", s[0])]
    assert len(task_sections) == 9, f"Attendu 9 tâches ### Task 1..9, trouvé {len(task_sections)}"
    for task_num in range(1, 10):
        matched = [s for s in task_sections if re.match(rf"^Task {task_num}\b", s[0])]
        assert len(matched) == 1, f"Tâche manquante ou dupliquée : ### Task {task_num}"
        _, _, _, task_block = matched[0]
        assert "**Files:**" in task_block, f"**Files:** manquant dans Task {task_num}"
        assert "**Interfaces:**" in task_block, f"**Interfaces:** manquant dans Task {task_num}"
        checkboxes = re.findall(r"^\s*-\s+\[\s\]\s+", task_block, flags=re.MULTILINE)
        assert len(checkboxes) >= 3, (
            f"Moins de 3 cases '- [ ]' dans Task {task_num} ({len(checkboxes)})"
        )

    parties_h3 = [t for t in h3_titles if re.match(r"^Partie [IVX]+\b", t)]
    assert len(parties_h3) == 12, f"Attendu 12 Parties I..XII, trouvé {len(parties_h3)}"
    for dom_idx in range(1, 13):
        roman = cp.ROMAN_NUMERALS[dom_idx]
        assert any(re.match(rf"^Partie {roman}\b", t) for t in parties_h3), (
            f"Titre ### Partie {roman} manquant"
        )

    fiche_sections = extract_heading_sections(plan_lines, headings, 4)
    ch_fiches = [s for s in fiche_sections if re.match(r"^Fiche CH-\d{2}\b", s[0])]
    assert len(ch_fiches) == 36, f"Attendu 36 fiches CH-01..CH-36, trouvé {len(ch_fiches)}"
    for ch_num in range(1, 37):
        matched = [s for s in ch_fiches if re.match(rf"^Fiche CH-{ch_num:02d}\b", s[0])]
        assert len(matched) == 1, f"Fiche manquante ou dupliquée : #### Fiche CH-{ch_num:02d}"
        _, _, _, fiche_block = matched[0]
        fiche_words = len(fiche_block.split())
        assert fiche_words >= 400, (
            f"Fiche CH-{ch_num:02d} trop courte : {fiche_words} mots (< 400)"
        )

    for letter in ("A", "B", "C", "D", "E"):
        assert any(f"Annexe {letter}" in t for t in h3_titles), (
            f"Sous-section ### pour Annexe {letter} manquante"
        )
        assert f"Annexe {letter}" in plan_text

    for ca_num in range(1, 23):
        assert f"CA-{ca_num:02d}" in plan_text, f"Critère d'acceptation manquant : CA-{ca_num:02d}"


def test_plan_mindmap_and_schemas_coverage() -> None:
    _, plan_text, plan_lines = _require_assembled_plan()

    bundle = json.loads((DONNEES_DIR / "corpus-mindmap-data.json").read_text(encoding="utf-8"))
    cat = json.loads((DONNEES_DIR / "catalogue-schemas-prd.json").read_text(encoding="utf-8"))

    nodes = bundle["nodes"]
    by_id = {n["node_id"]: n for n in nodes}

    for dom_num in range(1, 13):
        assert f"D{dom_num:02d}" in plan_text, f"Domaine manquant : D{dom_num:02d}"

    for node in nodes:
        kind = node["node_kind"]
        if kind in ("subdomain", "family"):
            assert node["node_id"] in plan_text, f"Nœud MindMap manquant : {node['node_id']}"
        elif kind == "theme":
            assert node["node_id"] in plan_text, f"Thème manquant : {node['node_id']}"
            assert node["canonical_slug"] in plan_text, (
                f"Slug canonique manquant : {node['canonical_slug']}"
            )

    all_schemas = list(cat["global_schemas"]) + list(cat["chapter_schemas"])
    assert len(all_schemas) == 115
    for sc in all_schemas:
        assert sc["schema_id"] in plan_text, f"Schéma manquant dans plan.md : {sc['schema_id']}"

    headings, _, _ = es.parse_markdown_lines(plan_lines)
    h2_sections = extract_heading_sections(plan_lines, headings, 2)
    sec1_block = next(b for t, _, _, b in h2_sections if t.startswith("1. "))
    for g_sc in cat["global_schemas"]:
        assert g_sc["schema_id"] in sec1_block, (
            f"Schéma global {g_sc['schema_id']} absent de la section 1"
        )

    fiche_sections = extract_heading_sections(plan_lines, headings, 4)
    fiche_by_ch: dict[int, str] = {}
    for title, _, _, block in fiche_sections:
        m = re.match(r"^Fiche CH-(\d{2})\b", title)
        if m:
            fiche_by_ch[int(m.group(1))] = block

    schemas_by_ch: dict[int, list[str]] = {i: [] for i in range(1, 37)}
    for sc in cat["chapter_schemas"]:
        schemas_by_ch[int(sc["chapter_number"])].append(sc["schema_id"])

    subdomains = [n for n in nodes if n["node_kind"] == "subdomain"]
    for sub in subdomains:
        ch_num = cp.expected_chapter_number(sub["domain_id"], sub["node_id"])
        block = fiche_by_ch[ch_num]
        assert sub["node_id"] in block, f"{sub['node_id']} absent de Fiche CH-{ch_num:02d}"
        for fid in sub["children_ids"]:
            assert fid in block, f"{fid} absent de Fiche CH-{ch_num:02d}"
            for tid in by_id[fid]["children_ids"]:
                tnode = by_id[tid]
                assert tnode["canonical_slug"] in block, (
                    f"Slug {tnode['canonical_slug']} absent de Fiche CH-{ch_num:02d}"
                )
        for sid in schemas_by_ch[ch_num]:
            assert sid in block, f"Schéma {sid} absent de Fiche CH-{ch_num:02d}"


def test_plan_anchors_links_and_tables() -> None:
    _, _, plan_lines = _require_assembled_plan()
    assert PRD_PATH.is_file(), "Compendium/prd.md introuvable pour validation des fragments"

    headings, _, code_lines = es.parse_markdown_lines(plan_lines)
    seen: dict[str, int] = {}
    heading_anchors = {cp.gfm_anchor(title, seen) for _, _, title in headings}

    prd_lines = PRD_PATH.read_text(encoding="utf-8").splitlines()
    prd_headings, _, _ = es.parse_markdown_lines(prd_lines)
    prd_seen: dict[str, int] = {}
    prd_anchors = {cp.gfm_anchor(title, prd_seen) for _, _, title in prd_headings}
    prd_resolved = PRD_PATH.resolve()

    line_counts_cache: dict[Path, int] = {}
    internal_checked = 0
    file_checked = 0

    for idx, line in enumerate(plan_lines, 1):
        if idx in code_lines:
            continue
        for target in MD_LINK_RE.findall(line):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                anc = target[1:]
                assert anc in heading_anchors, f"Ancre interne cassée à plan.md L{idx} : #{anc}"
                internal_checked += 1
            else:
                rel_part, _, frag = target.partition("#")
                target_path = (PLAN_PATH.parent / unquote(rel_part)).resolve()
                assert target_path.exists(), f"Lien relatif cassé à plan.md L{idx} : {target}"
                if frag:
                    if frag.startswith("L") and frag[1:].isdigit():
                        ln = int(frag[1:])
                        if target_path not in line_counts_cache:
                            line_counts_cache[target_path] = len(
                                target_path.read_text(encoding="utf-8").splitlines()
                            )
                        assert 1 <= ln <= line_counts_cache[target_path], (
                            f"Numéro de ligne hors bornes à plan.md L{idx} : {target}"
                        )
                    elif target_path == prd_resolved:
                        assert frag in prd_anchors, (
                            f"Fragment prd.md introuvable à plan.md L{idx} : {target}"
                        )
                file_checked += 1

    assert internal_checked >= 60, f"Trop peu de liens d'ancres internes : {internal_checked}"
    assert file_checked >= 150, f"Trop peu de liens relatifs vérifiés : {file_checked}"

    tables_checked = check_gfm_tables(plan_lines, code_lines)
    assert tables_checked >= 3, f"Trop peu de tableaux GFM vérifiés : {tables_checked}"


def test_plan_links_in_readmes_valid() -> None:
    _require_assembled_plan()
    plan_resolved = PLAN_PATH.resolve()

    for md_path in (
        REPO_ROOT / "README.md",
        COMPENDIUM_DIR / "README.md",
        CARTO_DIR / "README.md",
    ):
        assert md_path.is_file(), f"README manquant : {md_path}"
        assert b"\r\n" not in md_path.read_bytes(), f"CRLF détecté dans {md_path}"
        content = md_path.read_text(encoding="utf-8")

        points_to_plan = False
        for raw_target in MD_LINK_RE.findall(content):
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            rel_part, _, _ = raw_target.partition("#")
            target_path = (md_path.parent / unquote(rel_part)).resolve()
            assert target_path.exists(), f"Lien cassé dans {md_path} : {raw_target}"
            if target_path == plan_resolved:
                points_to_plan = True
        assert points_to_plan, f"Lien valide vers Compendium/plan.md manquant dans {md_path}"
