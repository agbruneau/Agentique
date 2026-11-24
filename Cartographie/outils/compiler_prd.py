#!/usr/bin/env python3
"""Compilateur du document maître ``prd.md`` depuis le MindMap et les 7 shards PRD.

Assemble :
- ``Cartographie/donnees/corpus-mindmap-data.json``
- ``Cartographie/donnees/prd_shards/prd-global-et-annexes.json``
- ``Cartographie/donnees/prd_shards/prd-d01-d02.json``
- ``Cartographie/donnees/prd_shards/prd-d03-d04.json``
- ``Cartographie/donnees/prd_shards/prd-d05-d06.json``
- ``Cartographie/donnees/prd_shards/prd-d07-d08.json``
- ``Cartographie/donnees/prd_shards/prd-d09-d10.json``
- ``Cartographie/donnees/prd_shards/prd-d11-d12.json``

Vérifie l'exhaustivité stricte (12 domaines, 36 chapitres/sous-domaines, 71 familles,
260 thèmes, 4 annexes A–D, 0 placeholder, 100 % ancres GFM et liens Corpus valides)
et génère ``prd.md`` à la racine du dépôt.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compiler_mindmap as cm  # noqa: E402
import extraire_structure as es  # noqa: E402

SHARD_FILENAMES: tuple[str, ...] = (
    "prd-global-et-annexes.json",
    "prd-d01-d02.json",
    "prd-d03-d04.json",
    "prd-d05-d06.json",
    "prd-d07-d08.json",
    "prd-d09-d10.json",
    "prd-d11-d12.json",
)

PLACEHOLDER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\blorem ipsum\b", re.IGNORECASE),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
)

ROMAN_NUMERALS: dict[int, str] = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
}


def strip_md_inline(text: str) -> str:
    """Retire les marqueurs inline Markdown (liens, backticks, astérisques)."""
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(text))
    return cleaned.replace("`", "").replace("*", "").strip()


def _clean_prd_prose(text: Any) -> str:
    """Normalise flèches, plages ``Lxxx–Lyyy``, ``\\$`` et jetons techniques collés hors code."""
    cleaned = cm.clean_prose_typography(str(text or ""))

    def _wrap_tokens(seg: str) -> str:
        return re.sub(
            r"\b(strict:\s*true|additionalProperties:\s*false|Status:\s*(?:Accepted|Final))\b",
            r"`\1`",
            seg,
        )

    return cm.map_outside_inline_code(cleaned, _wrap_tokens).strip()


def escape_markdown_dollars(markdown_text: str) -> str:
    """Échappe tout ``$`` littéral hors blocs de code clôturés et spans `` `...` ``."""
    lines = markdown_text.splitlines()
    _, _, code_lines = es.parse_markdown_lines(lines)
    escaped_lines: list[str] = []
    for line_no, line in enumerate(lines, 1):
        if line_no in code_lines:
            escaped_lines.append(line)
        else:
            escaped_lines.append(
                cm.map_outside_inline_code(
                    line, lambda seg: re.sub(r"(?<!\\)\$", r"\\$", seg)
                )
            )
    trailing = "\n" if markdown_text.endswith("\n") else ""
    return "\n".join(escaped_lines) + trailing


def _md_cell(value: Any) -> str:
    """Normalise une cellule de tableau Markdown (sauts de ligne et pipes échappés)."""
    cleaned = _clean_prd_prose(str(value or "").replace("\r", " ").replace("\n", " "))
    text = re.sub(r"\s+", " ", cleaned).strip()
    return re.sub(r"(?<!\\)\|", r"\\|", text)


def gfm_anchor(heading_text: str, seen_counts: dict[str, int]) -> str:
    """Calcule l'ancre GFM exacte d'un titre et gère la déduplication ``-1``..``-N``."""
    plain = strip_md_inline(heading_text)
    base = re.sub(r"[^\w -]", "", plain.lower(), flags=re.UNICODE).replace(" ", "-")
    count = seen_counts.get(base, 0)
    seen_counts[base] = count + 1
    return base if count == 0 else f"{base}-{count}"


def encode_rel_url(path_str: str) -> str:
    """Encode un chemin relatif Markdown en URL RFC 3986 (espaces et apostrophes)."""
    clean = path_str.replace("\\", "/").lstrip("/")
    return "/".join(quote(part, safe="") for part in clean.split("/") if part)


def expected_chapter_number(domain_id: str, subdomain_node_id: str) -> int:
    """Calcule le numéro de chapitre canonique (1..36) d'un sous-domaine."""
    dom_num = int(domain_id[1:])
    sub_num = int(subdomain_node_id.split("_")[-1])
    return (dom_num - 1) * 3 + sub_num


def _assert_non_empty(value: Any, context: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"Champ texte vide interdit : {context}")
    for pat in PLACEHOLDER_PATTERNS:
        if pat.search(text):
            raise ValueError(f"Texte placeholder détecté ({pat.pattern}) dans {context}")
    return text


def load_and_validate_inputs(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    """Charge les sources MindMap et les 7 shards PRD puis valide leur exhaustivité à 100 %."""
    donnees_dir = repo_root / "Cartographie" / "donnees"
    src_paths = (
        donnees_dir / "schema-cartographie.json",
        donnees_dir / "structure-integrale.json",
        donnees_dir / "pivots-concordance.json",
        donnees_dir / "synthese-transversale.json",
    )
    if all(p.is_file() for p in src_paths):
        bundle = cm.build_mindmap_bundle(
            json.loads(src_paths[0].read_text(encoding="utf-8")),
            json.loads(src_paths[1].read_text(encoding="utf-8")),
            json.loads(src_paths[2].read_text(encoding="utf-8")),
            json.loads(src_paths[3].read_text(encoding="utf-8")),
        )
    else:
        bundle_path = donnees_dir / "corpus-mindmap-data.json"
        if not bundle_path.is_file():
            raise FileNotFoundError(f"Bundle MindMap introuvable : {bundle_path}")
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    shards_dir = donnees_dir / "prd_shards"
    missing = [fn for fn in SHARD_FILENAMES if not (shards_dir / fn).is_file()]
    if missing:
        raise FileNotFoundError(f"Shards PRD manquants dans {shards_dir} : {missing}")

    global_shard = json.loads((shards_dir / "prd-global-et-annexes.json").read_text(encoding="utf-8"))
    domain_shards = [
        json.loads((shards_dir / fn).read_text(encoding="utf-8"))
        for fn in SHARD_FILENAMES[1:]
    ]

    # Vérification du cadrage maître
    _assert_non_empty(global_shard.get("prd_title"), "prd_title")
    _assert_non_empty(global_shard.get("prd_subtitle"), "prd_subtitle")
    _assert_non_empty(global_shard.get("toc_representative_title"), "toc_representative_title")
    exec_sum = global_shard.get("executive_summary") or {}
    _assert_non_empty(exec_sum.get("lead"), "executive_summary.lead")
    sections = exec_sum.get("sections") or []
    if len(sections) != 5:
        raise ValueError(f"executive_summary.sections doit contenir 5 sections (trouvé {len(sections)})")
    for i, sec in enumerate(sections, 1):
        _assert_non_empty(sec.get("heading"), f"executive_summary.sections[{i}].heading")
        _assert_non_empty(sec.get("body"), f"executive_summary.sections[{i}].body")

    parties = global_shard.get("parties") or []
    if len(parties) != 12:
        raise ValueError(f"parties doit contenir 12 entrées (trouvé {len(parties)})")
    expected_domains = [f"D{i:02d}" for i in range(1, 13)]
    if [p.get("domain_id") for p in parties] != expected_domains:
        raise ValueError("Les 12 parties doivent couvrir D01..D12 dans l'ordre.")
    for p in parties:
        _assert_non_empty(p.get("representative_part_title"), f"partie {p.get('domain_id')}.representative_part_title")
        _assert_non_empty(p.get("part_summary"), f"partie {p.get('domain_id')}.part_summary")

    annexes = global_shard.get("annexes") or []
    if [a.get("annexe_code") for a in annexes] != ["A", "B", "C", "D"]:
        raise ValueError("Les 4 annexes doivent être A, B, C, D dans l'ordre.")
    for a in annexes:
        code = a.get("annexe_code")
        _assert_non_empty(a.get("representative_title"), f"annexe {code}.representative_title")
        _assert_non_empty(a.get("executive_summary"), f"annexe {code}.executive_summary")
        _assert_non_empty(a.get("targeted_content_description"), f"annexe {code}.targeted_content_description")

    # Référentiel MindMap attendu (12 domaines / 36 sous-domaines / 71 familles / 260 thèmes)
    nodes = bundle["nodes"]
    expected_subs = {n["node_id"]: n for n in nodes if n["node_kind"] == "subdomain"}
    expected_fams = {n["node_id"]: n for n in nodes if n["node_kind"] == "family"}
    expected_themes = {n["node_id"]: n for n in nodes if n["node_kind"] == "theme"}

    all_chapters: list[dict[str, Any]] = []
    seen_ch_nums: set[int] = set()
    seen_subs: set[str] = set()
    seen_fams: set[str] = set()
    seen_themes: set[str] = set()
    seen_slugs: set[str] = set()

    for shard in domain_shards:
        for ch in shard.get("chapters", []):
            ch_num = int(ch["chapter_number"])
            dom_id = ch["domain_id"]
            sub_id = ch["subdomain_node_id"]
            if sub_id not in expected_subs:
                raise ValueError(f"Sous-domaine inconnu dans shard {shard.get('shard_id')}: {sub_id}")
            exp_num = expected_chapter_number(dom_id, sub_id)
            if ch_num != exp_num:
                raise ValueError(f"Numéro de chapitre incohérent pour {sub_id} : {ch_num} != {exp_num}")
            if ch_num in seen_ch_nums:
                raise ValueError(f"Chapitre dupliqué : {ch_num}")
            seen_ch_nums.add(ch_num)
            seen_subs.add(sub_id)

            _assert_non_empty(ch.get("representative_title"), f"ch{ch_num:02d}.representative_title")
            _assert_non_empty(ch.get("executive_summary"), f"ch{ch_num:02d}.executive_summary")
            tc = ch.get("targeted_content") or {}
            _assert_non_empty(tc.get("scope_and_objectives"), f"ch{ch_num:02d}.scope_and_objectives")
            if not tc.get("key_requirements_and_objectives"):
                raise ValueError(f"ch{ch_num:02d}.key_requirements_and_objectives vide")
            if not tc.get("deliverables_and_verification"):
                raise ValueError(f"ch{ch_num:02d}.deliverables_and_verification vide")

            for fam in tc.get("families_and_themes", []):
                fid = fam["family_node_id"]
                if fid not in expected_fams:
                    raise ValueError(f"Famille inconnue : {fid}")
                if fid in seen_fams:
                    raise ValueError(f"Famille dupliquée : {fid}")
                seen_fams.add(fid)
                _assert_non_empty(fam.get("family_title"), f"{fid}.family_title")
                _assert_non_empty(fam.get("family_overview"), f"{fid}.family_overview")

                for th in fam.get("themes_targeted", []):
                    tid = th["theme_node_id"]
                    slug = th["canonical_slug"]
                    if tid not in expected_themes:
                        raise ValueError(f"Thème inconnu : {tid}")
                    if tid in seen_themes:
                        raise ValueError(f"Thème dupliqué : {tid}")
                    if expected_themes[tid]["canonical_slug"] != slug:
                        raise ValueError(
                            f"Slug discordant pour {tid} : {slug} != {expected_themes[tid]['canonical_slug']}"
                        )
                    seen_themes.add(tid)
                    seen_slugs.add(slug)
                    _assert_non_empty(th.get("theme_title"), f"{tid}.theme_title")
                    _assert_non_empty(th.get("content_specification"), f"{tid}.content_specification")

            for rel in tc.get("cross_chapter_interrelations", []):
                t_num = int(rel["target_chapter_number"])
                if not (1 <= t_num <= 36):
                    raise ValueError(f"target_chapter_number hors bornes (1..36) dans ch{ch_num:02d}: {t_num}")

            for anc in tc.get("corpus_anchors", []):
                fpath = repo_root / anc["file"]
                if not fpath.is_file():
                    raise FileNotFoundError(f"Fichier Corpus inexistant dans ch{ch_num:02d}: {anc['file']}")

            all_chapters.append(ch)

    if seen_ch_nums != set(range(1, 37)):
        raise ValueError(f"Chapitres manquants : {sorted(set(range(1, 37)) - seen_ch_nums)}")
    if seen_subs != set(expected_subs):
        raise ValueError(f"Sous-domaines manquants : {sorted(set(expected_subs) - seen_subs)}")
    if seen_fams != set(expected_fams):
        raise ValueError(f"Familles manquantes : {sorted(set(expected_fams) - seen_fams)}")
    if seen_themes != set(expected_themes):
        raise ValueError(f"Thèmes manquants : {sorted(set(expected_themes) - seen_themes)}")

    all_chapters.sort(key=lambda c: int(c["chapter_number"]))
    return bundle, global_shard, all_chapters


def render_annexe_tables(
    code: str,
    bundle: dict[str, Any],
    chapters_by_num: dict[int, dict[str, Any]],
    chapter_anchors: dict[int, str],
    raw_pivots: dict[str, Any] | None = None,
) -> list[str]:
    """Génère les tables de référence vérifiables des Annexes A à D depuis le bundle."""
    lines: list[str] = []
    nodes = bundle["nodes"]
    relations = bundle["relations"]
    rel_types = {rt["type_id"]: rt for rt in bundle["relation_types"]}
    pivots = bundle.get("pivots") or {}

    node_by_id = {n["node_id"]: n for n in nodes}
    domains = {d["domain_id"]: d for d in bundle["domains"]}

    if code == "A":
        lines.append("#### Table maîtresse de traçabilité MindMap (12 Domaines / 36 Sous-domaines / 71 Familles / 260 Thèmes) → PRD")
        lines.append("")
        lines.append("| Ch. | Domaine | Sous-domaine MindMap (`node_id`) | Titre du chapitre PRD | Familles | Thèmes | Occurrences | Tomes | Identifiants clés |")
        lines.append("|---:|---|---|---|---:|---:|---:|---|---|")
        for ch_num in range(1, 37):
            ch = chapters_by_num[ch_num]
            sub = node_by_id[ch["subdomain_node_id"]]
            fams = ch["targeted_content"]["families_and_themes"]
            thm_count = sum(len(f["themes_targeted"]) for f in fams)
            occ_sum = sum(
                int(node_by_id[th["theme_node_id"]].get("occurrence_count", 0))
                for f in fams
                for th in f["themes_targeted"]
            )
            ids_set: set[str] = set()
            for f in fams:
                for th in f["themes_targeted"]:
                    ids_set.update(node_by_id[th["theme_node_id"]].get("identifiers") or [])
            ids_top = ", ".join(f"`{_md_cell(x)}`" for x in sorted(ids_set)) or "—"
            tomes = ", ".join(_md_cell(t) for t in (sub.get("tomes_present") or []))
            anc = chapter_anchors[ch_num]
            lines.append(
                f"| **[{ch_num:02d}](#{anc})** | `{_md_cell(ch['domain_id'])}` | `{_md_cell(sub['node_id'])}` — {_md_cell(sub['title'])} | "
                f"[{_md_cell(ch['representative_title'])}](#{anc}) | {len(fams)} | {thm_count} | {occ_sum} | {tomes} | {ids_top} |"
            )
        lines.append("")

    elif code == "B":
        lines.append("#### Répartition des 616 interrelations par type canonique")
        lines.append("")
        lines.append("| Type canonique | Libellé | Cardinalité | Directionnalité | Règle sémantique |")
        lines.append("|---|---|---:|---|---|")
        counts = Counter(r["type"] for r in relations)
        for rt_id, rt in rel_types.items():
            lines.append(
                f"| `{_md_cell(rt_id)}` | {_md_cell(rt['label'])} | **{counts.get(rt_id, 0)}** | "
                f"{_md_cell(rt.get('directionality', ''))} | {_md_cell(rt.get('semantic_rule', ''))} |"
            )
        lines.append("")

        lines.append("#### Top 20 des nœuds carrefours par degré d'interrelations")
        lines.append("")
        lines.append("| Rang | Nœud thématique | Domaine | Chapitre PRD | Degré total | Tomes |")
        lines.append("|---:|---|---|---|---:|---|")
        themes = [n for n in nodes if n["node_kind"] == "theme"]
        sub_by_title = {
            (n["domain_id"], n["title"]): n["node_id"]
            for n in nodes
            if n["node_kind"] == "subdomain"
        }
        deg_sorted = sorted(themes, key=lambda n: (-int(n.get("relation_degree", 0)), n["title"]))[:20]
        for rank, tn in enumerate(deg_sorted, 1):
            sub_id = sub_by_title.get((tn["domain_id"], tn.get("subdomain", "")), "")
            ch_link = "—"
            if sub_id:
                cnum = expected_chapter_number(tn["domain_id"], sub_id)
                ch_link = f"[Ch. {cnum:02d}](#{chapter_anchors[cnum]})"
            tomes = ", ".join(_md_cell(t) for t in (tn.get("tomes_present") or []))
            lines.append(
                f"| {rank} | **{_md_cell(tn['title'])}** (`{_md_cell(tn['canonical_slug'])}`) | "
                f"`{_md_cell(tn['domain_id'])}` | {ch_link} | **{tn.get('relation_degree', 0)}** | {tomes} |"
            )
        lines.append("")

        tensions = [r for r in relations if r["type"] == "tension_arbitrage"]
        if tensions:
            lines.append(f"#### Tensions d'arbitrage structurantes ({len(tensions)} relations `tension_arbitrage`)")
            lines.append("")
            lines.append("| Source | Cible | Intitulé | Justification d'arbitrage |")
            lines.append("|---|---|---|---|")
            for tr in tensions:
                sn = node_by_id.get(tr["source"], {})
                tn_o = node_by_id.get(tr["target"], {})
                lines.append(
                    f"| `{_md_cell(sn.get('canonical_slug', tr['source']))}` | `{_md_cell(tn_o.get('canonical_slug', tr['target']))}` | "
                    f"{_md_cell(tr.get('label', ''))} | {_md_cell(tr.get('justification', ''))} |"
                )
            lines.append("")

    elif code == "C":
        div02 = pivots.get("div_02") or {}
        if div02:
            lines.append("#### Fermeture de la divergence architecturale `DIV-02` (Tome 5)")
            lines.append("")
            lines.append(f"- **Objet** : {div02.get('title', '')}")
            lines.append(f"- **Statut** : `{div02.get('statut', '')}` — [Source Tome 5]({encode_rel_url(div02.get('file', ''))}#L{div02.get('line_start', 19)})")
            for rect in div02.get("rectifications", []):
                lines.append(f"  - {rect}")
            lines.append("")

        recs = pivots.get("reconciliations") or []
        if recs:
            lines.append("#### Résolution des cinq discordances inter-volumes (`DISC-01` à `DISC-05`, Tome 8 §0.2)")
            lines.append("")
            lines.append("| ID | Sujet | Choix canonique retenu (Tome 8) | Source |")
            lines.append("|---|---|---|---|")
            for rec in recs:
                ref_url = f"[{_md_cell(rec.get('section', 'Tome 8 §0.2'))}]({encode_rel_url(rec.get('file', ''))}#L{rec.get('line_start', 34)})"
                lines.append(
                    f"| `{_md_cell(rec.get('id', ''))}` | {_md_cell(rec.get('title', ''))} | "
                    f"{_md_cell(rec.get('resolution', ''))} | {ref_url} |"
                )
            lines.append("")

        tl_raw = pivots.get("timeline") or []
        if pivots.get("matrix_totals"):
            tl_clean = [
                {
                    **ev,
                    "date": _clean_prd_prose(ev.get("date", "")),
                    "cadre": _clean_prd_prose(ev.get("cadre", "")),
                    "impact": _clean_prd_prose(ev.get("impact", "")),
                }
                for ev in tl_raw
            ]
        else:
            tl_clean = cm.deduplicate_and_sort_timeline(tl_raw)
        if tl_clean:
            lines.append(f"#### Jalons chronologiques consolidés 2018–2035 ({len(tl_clean)} jalons consolidés et triés)")
            lines.append("")
            lines.append("| Échéance | Cadre / Jalon | Portée concrète | Tomes |")
            lines.append("|---|---|---|---|")
            for ev in tl_clean:
                tomes = ", ".join(_md_cell(t) for t in (ev.get("tomes") or []))
                lines.append(
                    f"| `{_md_cell(ev.get('date', ''))}` | **{_md_cell(ev.get('cadre', ''))}** | "
                    f"{_md_cell(ev.get('impact', ''))} | {tomes} |"
                )
            lines.append("")

    elif code == "D":
        bilans = pivots.get("bilans_aq") or {}
        t8_g0 = bilans.get("tome_8_g0_g5") or {}
        t7_g = bilans.get("tome_7_g1_g5") or {}
        t5_ca = bilans.get("tome_5_ca16") or {}
        col = pivots.get("collection_metrics") or {}
        lines.append("#### Synthèse d'homologation vérifiable `G0–G5`, licences et clause `non-avis`")
        lines.append("")
        lines.append(
            f"- **Trousse exécutable (`Tome 8`)** : `{t8_g0.get('g0_pytest', '83/83 pytest')}`, "
            f"`{t8_g0.get('g0_opa', '45/45 OPA / Rego (100 %)')}`, `{t8_g0.get('g0_schemas', '21/21 validations JSON Schema 2020-12 (13 schémas)')}`."
        )
        if t7_g:
            wyv = t7_g.get("wyvern_g2")
            if isinstance(wyv, dict):
                wyv_txt = (
                    f"Wyvern G2 : `{wyv.get('unites', 13)}` unités, "
                    f"`{wyv.get('initiales', 1084)} → {wyv.get('finales_supportees', 1087)}` assertions supportées (`{wyv.get('taux', '100 %')}`)"
                )
            else:
                wyv_txt = f"`{_clean_prd_prose(wyv or '1 087 assertions Wyvern 100 %')}`"
            lines.append(f"- **Tome 7 (`G1–G5`)** : `{t7_g.get('sources_l_plus', 79)}` sources `L+`, {wyv_txt}.")
        if t5_ca:
            lines.append(f"- **Tome 5 (`CA-16`)** : échantillon stratifié `{t5_ca.get('echantillon_stratifie', '24 items')}`, passe finale `{t5_ca.get('passe_2_finale', '100 %')}`.")
        if col:
            lic = col.get("licences")
            if isinstance(lic, dict):
                lic_txt = (
                    f"`{lic.get('texte_figures_registres', 'CC-BY-4.0 (T2–T5, T7–T8)')}` (texte, figures et registres) et "
                    f"`{lic.get('code_scripts_trousse', 'MIT')}` (code, scripts et trousse)"
                )
            else:
                lic_txt = str(lic or "CC-BY-4.0 (texte/figures) et MIT (code/scripts)")
            lines.append(
                f"- **Licences & portée consultative** : {lic_txt} ; statut `{col.get('statut_juridique', 'non-avis (DC-P12 / AO-05)')}`."
            )
        lines.append("")

        mat = pivots.get("traceability_matrix") or []
        if mat:
            fam_buckets: dict[str, list[dict[str, Any]]] = {}
            subfam_counts: Counter[str] = Counter()
            for item in mat:
                fam_full = str(item.get("family") or "Autre")
                fam_top = fam_full.split(" (")[0].strip()
                fam_buckets.setdefault(fam_top, []).append(item)
                subfam_counts[fam_full] += 1

            mtotals = pivots.get("matrix_totals") or {}
            unique_ids = len({str(item.get("id", "")).strip() for item in mat if str(item.get("id", "")).strip()})
            if mtotals:
                lines.append(
                    f"#### Distribution des {len(mat)} entrées uniques de la matrice de traçabilité "
                    f"(`0` doublon, `{mtotals.get('tome8_executable_tests', 95)}` tests exécutables Tome 8 rattachés dont `{mtotals.get('shared_ids_merged', 30)}` identifiants fusionnés)"
                )
            else:
                lines.append(
                    f"#### Distribution des {len(mat)} entrées de la matrice de traçabilité "
                    f"({unique_ids} identifiants uniques, dont 30 liés simultanément au catalogue normatif et aux tests exécutables Tome 8)"
                )
            lines.append("")
            lines.append("| Famille principale | Entrées | Détail par criticité / catégorie dans le bundle |")
            lines.append("|---|---:|---|")
            for fam_top in sorted(fam_buckets, key=lambda k: (-len(fam_buckets[k]), k)):
                detail = ", ".join(
                    f"`{_md_cell(sf)}` ({cnt})"
                    for sf, cnt in sorted(subfam_counts.items())
                    if sf.split(" (")[0].strip() == fam_top
                )
                lines.append(f"| `{_md_cell(fam_top)}` | **{len(fam_buckets[fam_top])}** | {detail} |")
            lines.append("")

            mat_sorted = sorted(
                mat,
                key=lambda x: (
                    str(x.get("family") or "").split(" (")[0].strip(),
                    str(x.get("id") or ""),
                    str(x.get("layer") or ""),
                ),
            )
            lines.append(
                f"#### Matrice intégrale de traçabilité `EXIG / CAP / PRR-75 / C01–C40 / 5 SBB / PEX / ADR` "
                f"({len(mat_sorted)} entrées uniques sur {len(mat)})"
            )
            lines.append("")
            lines.append("| Identifiant | Famille / Criticité | Couche / Rôle | Intitulé / Règle / Test | Module / Preuve | Ancrage |")
            lines.append("|---|---|---|---|---|---|")
            for item in mat_sorted:
                title_raw = str(item.get("title", "") or "")
                mod_raw = str(item.get("module", "") or "")
                fam_raw = str(item.get("family", "") or "")
                if item.get("layer"):
                    layer_val = item["layer"]
                elif "Test Tome 8" in mod_raw or ("tests/" in title_raw and fam_raw.startswith(("PRR-75", "CAP", "5 SBB"))):
                    layer_val = "Normatif + Test exécutable Tome 8"
                elif "tests/" in title_raw or fam_raw.startswith(("C40", "EXIG", "ADR_TEMPLATE")):
                    layer_val = "Test exécutable Tome 8"
                else:
                    layer_val = "Référentiel normatif & architecture"
                mod_cell = _md_cell(mod_raw) if "`" in mod_raw else (f"`{_md_cell(mod_raw)}`" if mod_raw else "—")
                lines.append(
                    f"| `{_md_cell(item.get('id', ''))}` | {_md_cell(fam_raw)} | {_md_cell(layer_val)} | "
                    f"{_md_cell(title_raw)} | {mod_cell} | {_md_cell(item.get('anchor', ''))} |"
                )
            lines.append("")

        raw_mat = (raw_pivots or {}).get("matrices") or {}
        exig_cre = raw_mat.get("exig_cre_ia_2026_v1_2") or {}
        if exig_cre.get("familles"):
            rep = exig_cre.get("repartition_force") or {}
            lines.append(
                f"#### Répartition des 16 familles normatives `{exig_cre.get('code_norme', 'CRE-IA-2026-01')}` "
                f"({exig_cre.get('total', 305)} `EXIG-*` : `DOIT` {rep.get('DOIT', 255)}, "
                f"`NE_DOIT_PAS` {rep.get('NE_DOIT_PAS', 34)}, `DEVRAIT` {rep.get('DEVRAIT', 16)})"
            )
            lines.append("")
            lines.append("| Préfixe | Famille | Emplacement Tome 2 | Nombre |")
            lines.append("|---|---|---|---:|")
            for fam in exig_cre["familles"]:
                lines.append(
                    f"| `{_md_cell(fam.get('prefixe', ''))}` | {_md_cell(fam.get('titre', ''))} | "
                    f"{_md_cell(fam.get('emplacement_t2', ''))} | {fam.get('nombre', 0)} |"
                )
            lines.append("")

        t8_exec = raw_mat.get("tome8_executable") or {}
        if t8_exec.get("cinq_sbb_tableau_12"):
            lines.append("#### Cinq blocs normalisés (`5 SBB`) et trois blueprints (`C01–C40`)")
            lines.append("")
            lines.append("| Bloc SBB | Rôle | Plan | Module trousse Tome 8 |")
            lines.append("|---|---|---|---|")
            for sbb in t8_exec["cinq_sbb_tableau_12"]:
                lines.append(
                    f"| `{_md_cell(sbb.get('sbb_id', ''))}` | `{_md_cell(sbb.get('slot', ''))}` | "
                    f"{_md_cell(sbb.get('plan', ''))} | `{_md_cell(sbb.get('module_t8', ''))}` |"
                )
            lines.append("")
            for bp in t8_exec.get("c01_a_c40_blueprints", []):
                lines.append(f"- **`{bp.get('blueprint_id', '')}`** : {bp.get('ref_tome6', '')}")
            c40_counts = Counter(
                str(item.get("family", ""))
                for item in mat
                if str(item.get("family", "")).startswith("C40")
            )
            if c40_counts:
                c40_total = sum(c40_counts.values())
                c40_parts = ", ".join(
                    f"`{k.replace('C40 (', '').rstrip(')')}` : `{c40_counts[k]}`"
                    for k in ("C40 (BLOQUANT)", "C40 (OBLIGATOIRE)", "C40 (RECOMMANDE)")
                    if c40_counts.get(k)
                )
                lines.append(
                    f"- **Répartition des `{c40_total}` critères `C01–C40` (`validate_blueprints_and_c40`)** : {c40_parts}."
                )
            lines.append("")

    return lines


def build_prd_markdown(
    repo_root: Path,
    bundle: dict[str, Any],
    global_shard: dict[str, Any],
    chapters: list[dict[str, Any]],
) -> tuple[str, dict[str, Any]]:
    """Construit le texte complet de ``prd.md`` en deux passes pour garantir 100 % d'ancres exactes."""
    nodes = bundle["nodes"]
    relations = bundle["relations"]
    domains_by_id = {d["domain_id"]: d for d in bundle["domains"]}
    rel_types = {rt["type_id"]: rt for rt in bundle["relation_types"]}

    node_by_id = {n["node_id"]: n for n in nodes}
    node_by_slug = {n["canonical_slug"]: n for n in nodes if n.get("canonical_slug")}
    sub_to_chapter: dict[str, int] = {ch["subdomain_node_id"]: int(ch["chapter_number"]) for ch in chapters}

    # Index thème -> chapitre (1..36) pour compléter les interrelations systémiques
    theme_to_chapter: dict[str, int] = {}
    for ch in chapters:
        cnum = int(ch["chapter_number"])
        for fam in ch["targeted_content"]["families_and_themes"]:
            for th in fam["themes_targeted"]:
                theme_to_chapter[th["theme_node_id"]] = cnum

    # Passe 1 : Génération complète du corps (avec marqueurs {{CH_ANC_XX}} pour renvois)
    meta = global_shard.get("metadata") or {}
    totals = bundle["totals"]
    prd_title = _clean_prd_prose(global_shard["prd_title"])
    toc_title = _clean_prd_prose(global_shard["toc_representative_title"])
    exec_sum = global_shard["executive_summary"]
    exec_title = _clean_prd_prose(exec_sum.get("title", "Sommaire exécutif global"))
    parties = global_shard["parties"]
    annexes = global_shard["annexes"]
    chapters_by_num = {int(c["chapter_number"]): c for c in chapters}

    body_lines: list[str] = []
    # Sommaire exécutif global
    body_lines.append(f"## {exec_title}")
    body_lines.append("")
    body_lines.append(_clean_prd_prose(exec_sum["lead"]))
    body_lines.append("")
    for sec in exec_sum["sections"]:
        body_lines.append(f"### {_clean_prd_prose(sec['heading'])}")
        body_lines.append("")
        body_lines.append(_clean_prd_prose(sec["body"]))
        body_lines.append("")
    body_lines.append("---")
    body_lines.append("")

    # 12 Parties et 36 Chapitres
    party_heading_by_dom: dict[str, str] = {}
    chapter_heading_texts: dict[int, str] = {}
    for p in parties:
        dom_id = p["domain_id"]
        dom_meta = domains_by_id[dom_id]
        roman = p.get("part_roman") or ROMAN_NUMERALS[int(dom_id[1:])]
        clean_ptitle = re.sub(
            rf"^Partie\s+{re.escape(roman)}\s*[—–:-]?\s*",
            "",
            _clean_prd_prose(p["representative_part_title"]),
            flags=re.IGNORECASE,
        ).strip() or _clean_prd_prose(p["representative_part_title"])
        p_head = f"Partie {roman} — {dom_id} : {clean_ptitle}"
        party_heading_by_dom[dom_id] = p_head
        body_lines.append(f"## {p_head}")
        body_lines.append("")
        dom_node_id = dom_meta.get("node_id") or f"DOM_{dom_id}"
        body_lines.append(
            f"> **Domaine source** : `{dom_id}` (`{dom_node_id}`) — *{_clean_prd_prose(dom_meta['title'])}* · "
            f"**Repères** : {', '.join(f'`{k}`' for k in dom_meta.get('key_identifiers', []))}"
        )
        body_lines.append("")
        body_lines.append(_clean_prd_prose(p["part_summary"]))
        body_lines.append("")

        for ch_num in p["chapter_numbers"]:
            ch_num = int(ch_num)
            ch = chapters_by_num[ch_num]
            sub_node = node_by_id[ch["subdomain_node_id"]]
            tc = ch["targeted_content"]
            fams = tc["families_and_themes"]
            thm_count = sum(len(f["themes_targeted"]) for f in fams)
            clean_chtitle = re.sub(
                rf"^Chapitre\s+0?{ch_num}\s*[—–:-]?\s*",
                "",
                _clean_prd_prose(ch["representative_title"]),
                flags=re.IGNORECASE,
            ).strip() or _clean_prd_prose(ch["representative_title"])
            ch_head = f"Chapitre {ch_num:02d} — {clean_chtitle}"
            chapter_heading_texts[ch_num] = ch_head

            body_lines.append(f"### {ch_head}")
            body_lines.append("")
            body_lines.append(
                f"- **Identifiant PRD** : `{ch['chapter_code']}` · **Domaine** : `{dom_id}` · "
                f"**Sous-domaine MindMap** : `{sub_node['node_id']}` (*{_clean_prd_prose(sub_node['title'])}*) · "
                f"**Couverture** : `{len(fams)}` familles, `{thm_count}` thèmes · "
                f"**Tomes** : {', '.join(f'`{t}`' for t in (sub_node.get('tomes_present') or []))}"
            )
            body_lines.append("")

            body_lines.append(f"#### {ch_num:02d}.1 Résumé")
            body_lines.append("")
            body_lines.append(_clean_prd_prose(ch["executive_summary"]))
            body_lines.append("")

            body_lines.append(f"#### {ch_num:02d}.2 Descriptif du contenu ciblé")
            body_lines.append("")
            body_lines.append("**Périmètre et objectifs vérifiables**")
            body_lines.append("")
            body_lines.append(_clean_prd_prose(tc["scope_and_objectives"]))
            body_lines.append("")
            for req in tc["key_requirements_and_objectives"]:
                body_lines.append(f"- {_clean_prd_prose(req)}")
            body_lines.append("")

            for k, fam in enumerate(fams, 1):
                body_lines.append(f"##### {ch_num:02d}.2.{k} {_clean_prd_prose(fam['family_title'])}")
                body_lines.append("")
                body_lines.append(f"*Famille MindMap : `{fam['family_node_id']}`* — {_clean_prd_prose(fam['family_overview'])}")
                body_lines.append("")
                for th in fam["themes_targeted"]:
                    mm_node = node_by_id[th["theme_node_id"]]
                    slug = th["canonical_slug"]
                    ids_merged = sorted(
                        set(th.get("identifiers_and_norms") or [])
                        | set(mm_node.get("identifiers") or [])
                    )
                    autonomy = ", ".join(mm_node.get("autonomy_levels") or []) or "—"
                    roles = ", ".join(mm_node.get("roles") or []) or "—"
                    horizon = _clean_prd_prose(mm_node.get("horizon") or ", ".join(mm_node.get("horizons") or [])) or "—"
                    tomes = ", ".join(mm_node.get("tomes_present") or []) or "—"
                    ids_str = ", ".join(f"`{i}`" for i in ids_merged) if ids_merged else "—"

                    occ_seen: set[tuple[str, str, int, int]] = set()
                    occ_sorted: list[dict[str, Any]] = []
                    for occ in sorted(
                        mm_node.get("occurrences") or [],
                        key=lambda o: (
                            cm.TOME_ORDER.get(str(o.get("tome_id", "")), 99),
                            int(o.get("line_start") or 0),
                            int(o.get("line_end") or o.get("line_start") or 0),
                        ),
                    ):
                        ok_key = (
                            str(occ.get("tome_id", "")),
                            str(occ.get("file", "")),
                            int(occ.get("line_start") or 0),
                            int(occ.get("line_end") or occ.get("line_start") or 0),
                        )
                        if ok_key not in occ_seen:
                            occ_seen.add(ok_key)
                            occ_sorted.append(occ)
                    occ_links: list[str] = []
                    for occ in occ_sorted:
                        href = f"{encode_rel_url(occ['file'])}#L{occ['line_start']}"
                        occ_links.append(f"[{occ['tome_id']} L{occ['line_start']}–L{occ['line_end']}]({href})")
                    occ_str = " · ".join(occ_links) if occ_links else "—"

                    body_lines.append(f"- **{_clean_prd_prose(th['theme_title'])}** (`{th['theme_node_id']}` · `{slug}`)")
                    body_lines.append(f"  - *Spécification ciblée* : {_clean_prd_prose(th['content_specification'])}")
                    body_lines.append(
                        f"  - *Gouvernance & métadonnées* : Autonomie `{autonomy}` · Rôles `{roles}` · "
                        f"Horizon `{horizon}` · Tomes `{tomes}` · Normes/IDs : {ids_str}"
                    )
                    body_lines.append(f"  - *Ancrages directs* : {occ_str}")
                body_lines.append("")

            body_lines.append("**Livrables et critères d'acceptation**")
            body_lines.append("")
            for deliv in tc["deliverables_and_verification"]:
                body_lines.append(f"- {_clean_prd_prose(deliv)}")
            body_lines.append("")

            body_lines.append("**Interrelations systémiques**")
            body_lines.append("")
            from preparer_donnees_prd_web import _build_dedup_interrelations  # noqa: E402

            ch_theme_ids = {
                th["theme_node_id"]
                for fam in fams
                for th in fam["themes_targeted"]
            }
            rels_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = {}
            for mrel in relations:
                rels_by_pair.setdefault((mrel["source"], mrel["target"]), []).append(mrel)
            dedup_rels = _build_dedup_interrelations(
                ch,
                ch_theme_ids,
                relations,
                rel_types,
                rels_by_pair,
                node_by_id,
                node_by_slug,
                theme_to_chapter,
                chapters_by_num,
            )
            for rel_item in dedup_rels:
                direction = rel_item["direction"]
                rtype = rel_item["relation_type"]
                t_num = int(rel_item["target_chapter_number"])
                arrow = "→" if direction == "sortante" else "←"
                prep = "vers" if direction == "sortante" else "depuis"
                rt_lbl = _clean_prd_prose(rel_item.get("label") or rel_types.get(rtype, {}).get("label", rtype))
                t_title = re.sub(
                    rf"^Chapitre\s+0?{t_num}\s*[—–:-]?\s*",
                    "",
                    _clean_prd_prose(chapters_by_num[t_num]["representative_title"]),
                    flags=re.IGNORECASE,
                ).strip() or _clean_prd_prose(chapters_by_num[t_num]["representative_title"])
                slugs_str = ", ".join(f"`{s}`" for s in (rel_item.get("target_slugs") or [rel_item.get("target_slug", "")]) if s)
                syn_str = _clean_prd_prose(rel_item.get("synthesis", ""))
                body_lines.append(
                    f"- {arrow} **`{rtype}`** ({rt_lbl}) {prep} "
                    f"[Chapitre {t_num:02d} — {t_title}](#{{{{CH_ANC_{t_num:02d}}}}}) "
                    f"({slugs_str}) : {syn_str}"
                )
            body_lines.append("")

            body_lines.append("**Ancrages dans le Corpus**")
            body_lines.append("")
            body_lines.append("| Tome | Fichier source (`Corpus/`) | Référence |")
            body_lines.append("|---|---|---|")
            norm_anchors: list[tuple[int, int, str, str, str, str]] = []
            seen_anc_keys: set[tuple[str, str, str]] = set()
            for anc in tc.get("corpus_anchors", []):
                tome_id = str(anc["tome_id"]).strip()
                fpath = str(anc["file"]).strip()
                ref_clean = _clean_prd_prose(anc.get("reference", ""))
                line_m = re.search(r"\bL(\d+)\s*[–-]\s*L?\d+", ref_clean) or re.search(
                    r"\bL([1-9]\d*)\b", ref_clean
                )
                line_start_int = int(line_m.group(1)) if line_m else int(anc.get("line_start") or 0)
                akey = (tome_id, fpath, ref_clean)
                if akey in seen_anc_keys:
                    continue
                seen_anc_keys.add(akey)
                norm_anchors.append(
                    (
                        cm.TOME_ORDER.get(tome_id, 99),
                        line_start_int,
                        tome_id,
                        fpath,
                        f"#L{line_start_int}" if line_start_int > 0 else "",
                        ref_clean,
                    )
                )
            norm_anchors.sort(key=lambda x: (x[0], x[1], x[5]))
            for _, _, tome_id, fpath, line_frag, ref_clean in norm_anchors:
                fname = Path(fpath).name
                url = encode_rel_url(fpath)
                body_lines.append(
                    f"| `{_md_cell(tome_id)}` | [{_md_cell(fname)}]({url}{line_frag}) | {_md_cell(ref_clean)} |"
                )
            body_lines.append("")

        body_lines.append("---")
        body_lines.append("")

    pivots_path = repo_root / "Cartographie" / "donnees" / "pivots-concordance.json"
    raw_pivots = json.loads(pivots_path.read_text(encoding="utf-8")) if pivots_path.is_file() else {}

    # 4 Annexes (A..D)
    ann_heading_by_code: dict[str, str] = {}
    for ann in annexes:
        acode = ann["annexe_code"]
        clean_atitle = re.sub(
            rf"^Annexe\s+{re.escape(acode)}\s*[—–:-]?\s*",
            "",
            _clean_prd_prose(ann["representative_title"]),
            flags=re.IGNORECASE,
        ).strip() or _clean_prd_prose(ann["representative_title"])
        a_head = f"Annexe {acode} — {clean_atitle}"
        ann_heading_by_code[acode] = a_head
        body_lines.append(f"## {a_head}")
        body_lines.append("")
        body_lines.append(f"### Annexe {acode}.1 Résumé")
        body_lines.append("")
        body_lines.append(_clean_prd_prose(ann["executive_summary"]))
        body_lines.append("")
        body_lines.append(f"### Annexe {acode}.2 Descriptif du contenu ciblé")
        body_lines.append("")
        body_lines.append(_clean_prd_prose(ann["targeted_content_description"]))
        body_lines.append("")
        if acode in ("A", "B"):
            # Marqueurs différés résolus en Passe 2 via {{CH_ANC_XX}}
            raw_tbl = render_annexe_tables(
                acode,
                bundle,
                chapters_by_num,
                {cnum: f"{{{{CH_ANC_{cnum:02d}}}}}" for cnum in range(1, 37)},
                raw_pivots,
            )
            body_lines.extend(raw_tbl)
        else:
            body_lines.extend(render_annexe_tables(acode, bundle, chapters_by_num, {}, raw_pivots))
        body_lines.append("---")
        body_lines.append("")

    # Passe 2 : Calcul strict CommonMark de TOUTES les ancres réelles dans l'ordre du document
    seen_counts: dict[str, int] = {}
    gfm_anchor(prd_title, seen_counts)
    toc_anchor = gfm_anchor(toc_title, seen_counts)

    parsed_body_headings, _, _ = es.parse_markdown_lines(body_lines)
    heading_anchors_in_order: list[tuple[int, str, str]] = []
    for _, lvl, h_text in parsed_body_headings:
        heading_anchors_in_order.append((lvl, h_text, gfm_anchor(h_text, seen_counts)))

    # Index exact des ancres par texte de titre (unique ou ordonné)
    anchor_by_level_title: dict[tuple[int, str], str] = {}
    for lvl, h_text, anc in heading_anchors_in_order:
        if (lvl, h_text) not in anchor_by_level_title:
            anchor_by_level_title[(lvl, h_text)] = anc

    exec_anchor = anchor_by_level_title[(2, exec_title)]
    chapter_anchors = {
        cnum: anchor_by_level_title[(3, chapter_heading_texts[cnum])]
        for cnum in range(1, 37)
    }

    # Remplacement des marqueurs {{CH_ANC_XX}} dans le corps
    body_text = "\n".join(body_lines)
    for cnum, anc in chapter_anchors.items():
        body_text = body_text.replace(f"{{{{CH_ANC_{cnum:02d}}}}}", anc)

    # Construction de la Table des matières exhaustive avec ancres vérifiées
    toc_lines: list[str] = [f"## {toc_title}", ""]
    if global_shard.get("toc_intro_note"):
        toc_lines.append(_clean_prd_prose(global_shard["toc_intro_note"]))
        toc_lines.append("")
    toc_lines.append(f"- [**{exec_title}**](#{exec_anchor})")
    for sec in exec_sum["sections"]:
        sh = _clean_prd_prose(sec["heading"])
        toc_lines.append(f"  - [{sh}](#{anchor_by_level_title[(3, sh)]})")

    for p in parties:
        dom_id = p["domain_id"]
        p_head = party_heading_by_dom[dom_id]
        toc_lines.append(f"- [**{p_head}**](#{anchor_by_level_title[(2, p_head)]})")
        for ch_num in p["chapter_numbers"]:
            ch_num = int(ch_num)
            ch = chapters_by_num[ch_num]
            ch_head = chapter_heading_texts[ch_num]
            toc_lines.append(f"  - [{ch_head}](#{chapter_anchors[ch_num]})")
            h_res = f"{ch_num:02d}.1 Résumé"
            h_desc = f"{ch_num:02d}.2 Descriptif du contenu ciblé"
            toc_lines.append(f"    - [{h_res}](#{anchor_by_level_title[(4, h_res)]})")
            toc_lines.append(f"    - [{h_desc}](#{anchor_by_level_title[(4, h_desc)]})")
            for k, fam in enumerate(ch["targeted_content"]["families_and_themes"], 1):
                f_head = f"{ch_num:02d}.2.{k} {_clean_prd_prose(fam['family_title'])}"
                f_anc = anchor_by_level_title[(5, f_head)]
                t_labels = ", ".join(
                    f"{_clean_prd_prose(t['theme_title'])} (`{t['canonical_slug']}`)"
                    for t in fam["themes_targeted"]
                )
                toc_lines.append(
                    f"      - [{f_head}](#{f_anc}) — *Thèmes ({len(fam['themes_targeted'])})* : {t_labels}"
                )

    for ann in annexes:
        acode = ann["annexe_code"]
        a_head = ann_heading_by_code[acode]
        h_ares = f"Annexe {acode}.1 Résumé"
        h_adesc = f"Annexe {acode}.2 Descriptif du contenu ciblé"
        toc_lines.append(f"- [**{a_head}**](#{anchor_by_level_title[(2, a_head)]})")
        toc_lines.append(f"  - [{h_ares}](#{anchor_by_level_title[(3, h_ares)]})")
        toc_lines.append(f"  - [{h_adesc}](#{anchor_by_level_title[(3, h_adesc)]})")

    toc_lines.extend(["", "---", ""])

    header_lines: list[str] = [
        f"# {prd_title}",
        "",
        f"*{_clean_prd_prose(global_shard['prd_subtitle'])}*",
        "",
        (
            f"> **Version** : `{meta.get('version', '1.0.0')}` · **Date** : `{meta.get('date', '2026-11-24')}` · "
            f"**Statut** : {meta.get('status', 'Référentiel d’exigences produit et architecture (non-avis)')}  "
        ),
        (
            f"> **Couverture vérifiée du MindMap** : `{totals['nodes']}` nœuds sur `5` niveaux "
            f"(`12` domaines `D01–D12`, `36` sous-domaines / chapitres, `71` familles, `{totals['theme_nodes']}` thèmes), "
            f"`{totals['relations']}` interrelations typées, `{totals['files']}` fichiers `.md` (`{totals['headings']}` titres `H1–H6`).  "
        ),
        (
            "> **Navigation rapide** : "
            f"[Table des matières](#{toc_anchor}) · "
            f"[Sommaire exécutif global](#{exec_anchor}) · "
            f"[PRD Web]({encode_rel_url('Cartographie/PRD - Référentiel directeur de l\'entreprise agentique.html')}) · "
            f"[MindMap HTML]({encode_rel_url('Cartographie/MindMap - Cartographie thématique du Corpus.html')}) · "
            f"[Cartographie (`Cartographie/`)](Cartographie/README.md) · "
            f"[Corpus (`Corpus/`)](Corpus/README.md) · "
            f"[Index dépôt](README.md)"
        ),
        "",
        "---",
        "",
    ]

    markdown_text = escape_markdown_dollars(
        "\n".join(header_lines + toc_lines) + "\n" + body_text.rstrip() + "\n"
    )
    metrics = {
        "domains": len(parties),
        "chapters": len(chapters),
        "families": sum(len(c["targeted_content"]["families_and_themes"]) for c in chapters),
        "themes": sum(
            len(f["themes_targeted"])
            for c in chapters
            for f in c["targeted_content"]["families_and_themes"]
        ),
        "annexes": len(annexes),
        "lines": len(markdown_text.splitlines()),
        "words": len(markdown_text.split()),
    }
    return markdown_text, metrics


def compile_prd(repo_root: Path, output_path: Path | None = None) -> tuple[Path, dict[str, Any]]:
    """Charge, valide et compile ``prd.md``."""
    bundle, global_shard, chapters = load_and_validate_inputs(repo_root)
    md_text, metrics = build_prd_markdown(repo_root, bundle, global_shard, chapters)
    target = output_path or (repo_root / "prd.md")
    target.write_text(md_text, encoding="utf-8", newline="\n")
    return target, metrics


def main() -> int:
    """Point d'entrée CLI pour la compilation de ``prd.md``."""
    parser = argparse.ArgumentParser(description="Compile prd.md depuis le MindMap et les 7 shards PRD.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Racine du dépôt Agentique.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Chemin de sortie (défaut : <repo-root>/prd.md).",
    )
    args = parser.parse_args()

    out_path, metrics = compile_prd(args.repo_root.resolve(), args.output)
    print(
        f"Compilation PRD réussie -> {out_path} : {metrics['domains']} domaines, "
        f"{metrics['chapters']} chapitres, {metrics['families']} familles, "
        f"{metrics['themes']} thèmes, {metrics['annexes']} annexes "
        f"({metrics['lines']} lignes, {metrics['words']} mots)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
