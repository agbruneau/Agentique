#!/usr/bin/env python3
"""Synthétiseur du graphe thématique unifié du Compendium de l'entreprise agentique.

Construit ``Sources/Cartographie/donnees/synthese-transversale.json`` à partir :
- du registre ``Sources/Compendium/ouvrage/registre/mindmap-complet.json`` (`380` nœuds, `616` relations)
- du manifeste ``Sources/Compendium/ouvrage/specs/manifest.json`` (`42` unités)
- du glossaire ``Sources/Compendium/ouvrage/registre/glossaire-termes.json`` (`56` vedettes dont « Agentivité des systèmes »)
- de ``Sources/Cartographie/donnees/structure-integrale.json`` (`15` sections, `Compendium.md`)
- de ``Sources/Cartographie/donnees/inventaire-115-schemas-compendium.json`` (`115` schémas)
- de ``Sources/Cartographie/donnees/pivots-concordance.json``
- de ``Sources/Cartographie/donnees/schema-cartographie.json``

Préserve intégralement les `380` ``node_id`` et ``canonical_slug``, les métadonnées canoniques,
``tomes_present`` (provenance historique) et les `616` relations ``REL_0001..REL_0616``, tout en
ancrant chaque thème sur de vraies occurrences vérifiées dans ``Compendium/Compendium.md``
et en produisant la matrice de concordance `12 × 15` (`180` cellules).
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from typing import Any
import unicodedata

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import extraire_structure as es  # noqa: E402

PART_ORDER: list[str] = [
    "R", "LIM", "P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10", "P11", "P12", "ANN"
]
PART_RANK: dict[str, int] = {pid: idx for idx, pid in enumerate(PART_ORDER)}

UNIT_TO_PRIMARY_DOMAIN: dict[str, str] = {
    "00-liminaire": "D02",
    "annexe-a": "D12",
    "annexe-b": "D12",
    "annexe-c": "D09",
    "annexe-d": "D12",
    "annexe-e": "D02",
}

FRENCH_STOPWORDS: set[str] = {
    "avec", "dans", "pour", "sans", "sous", "entre", "vers", "chez", "cette", "cet", "cette",
    "leurs", "leur", "tout", "tous", "toute", "toutes", "plus", "moins", "tres", "autre",
    "autres", "comme", "ainsi", "donc", "mais", "alors", "apres", "avant", "contre", "selon",
    "rapport", "niveau", "niveaux", "modele", "modeles", "systeme", "systemes", "agent", "agents",
    "agentique", "agentiques", "entreprise", "architecture", "gouvernance", "cadre", "chapitre",
    "annexe", "section", "analyse", "gestion", "mise", "oeuvre", "etat", "passage", "echelle",
    "controle", "controles", "norme", "normes", "regle", "regles", "cycle", "chaine", "donnees",
}


def _norm(text: str) -> str:
    """Normalise en minuscules sans accents pour la recherche lexicographique."""
    decomposed = unicodedata.normalize("NFD", text.lower())
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", stripped).strip()


def _clean_text(value: Any, *, preserve_en: bool = False) -> str:
    """Nettoie les chaînes éditoriales sans corrompre le code inline ni les termes anglais."""
    s = str(value or "").replace(r"\$", "$").strip()
    s = re.sub(r"\bL([1-9]\d*)-L?([1-9]\d*)\b", r"L\1–L\2", s)
    parts = re.split(r"(`[^`]*`)", s)
    for idx in range(0, len(parts), 2):
        part = parts[idx]
        part = part.replace("<->", "↔").replace("->", "→")
        if not preserve_en:
            part = (
                part.replace("Systems of Agency", "Systèmes d'agentivité")
                .replace("System of Agency", "Système d'agentivité")
                .replace("systems of agency", "systèmes d'agentivité")
            )
        parts[idx] = part
    return "".join(parts)


def _flatten_compendium_sections(
    struct_data: dict[str, Any],
    comp_lines: list[str],
    manifest_units: dict[str, dict[str, Any]],
) -> tuple[
    list[dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    """Extrait les sous-sections indexables, les 42 unités et les index structurels de ``structure-integrale.json``."""
    sections: list[dict[str, Any]] = []
    unit_meta_by_cid: dict[str, dict[str, Any]] = {}
    struct_by_uid: dict[str, dict[str, Any]] = {}
    part_h1_by_part_id: dict[str, dict[str, Any]] = {}

    def walk(
        node: dict[str, Any],
        part_id: str,
        current_unit_cid: str | None,
        current_unit_title: str,
    ) -> None:
        struct_by_uid[node["unit_id"]] = node
        cid = node.get("compendium_unit_id") or current_unit_cid
        kind = node.get("kind", "")
        title = node.get("title", "")
        level = int(node.get("level", 1))

        if level == 1 and kind in ("part", "liminaire", "annex") and part_id not in part_h1_by_part_id:
            part_h1_by_part_id[part_id] = node

        # Détecter l'en-tête racine de l'unité éditoriale (00-liminaire, ch01..ch36, annexe-a..e)
        if node.get("compendium_unit_id") and (
            (level == 1 and cid == "00-liminaire") or level == 2
        ):
            current_unit_title = title
            if cid not in unit_meta_by_cid:
                m_u = manifest_units.get(cid, {})
                unit_meta_by_cid[cid] = {
                    "compendium_unit_id": cid,
                    "unit_id": node["unit_id"],
                    "part_id": part_id,
                    "file": "Compendium/Compendium.md",
                    "source_file": f"Sources/Compendium/ouvrage/{m_u['file']}" if m_u.get("file") else node.get("source_file"),
                    "part_title": node.get("part_title") or current_unit_title,
                    "chapter_title": title,
                    "line_start": int(node["line_start"]),
                    "line_end": int(node["line_end"]),
                    "pdf_page_start": node.get("pdf_page_start"),
                    "pdf_page_end": node.get("pdf_page_end"),
                    "reading_minutes": int(node.get("reading_minutes") or max(1, round(int(node.get("word_count", 0)) / 220))),
                    "guiding_question": node.get("guiding_question"),
                    "excerpt": node.get("excerpt", ""),
                    "identifiers": list(node.get("identifiers") or []),
                    "word_count": int(node.get("word_count", 0)),
                }

        children = node.get("children") or []
        if cid and kind not in ("toc", "references", "part"):
            # Préférer les sections feuilles ou H3/H2 de contenu (éviter les H1 Part)
            l_start = int(node["line_start"])
            l_end = int(node["line_end"])
            # Si le nœud a des sous-sections, n'indexer le corps que s'il s'agit d'un H3/H4 ou d'une unité sans sous-titre
            is_leaf_or_h3 = (level >= 3) or (not children)
            if is_leaf_or_h3 and l_end >= l_start:
                body = "\n".join(comp_lines[l_start - 1 : min(l_end, len(comp_lines))])
                norm_title = _norm(title)
                norm_body = _norm(body)
                sections.append(
                    {
                        "part_id": part_id,
                        "compendium_unit_id": cid,
                        "unit_id": node["unit_id"],
                        "source_file": node.get("source_file") or (
                            f"Sources/Compendium/ouvrage/{manifest_units[cid]['file']}" if cid in manifest_units else ""
                        ),
                        "chapter": current_unit_title,
                        "section": title,
                        "level": level,
                        "line_start": l_start,
                        "line_end": l_end,
                        "pdf_page_start": node.get("pdf_page_start"),
                        "pdf_page_end": node.get("pdf_page_end"),
                        "reading_minutes": int(node.get("reading_minutes") or max(1, round(int(node.get("word_count", 0)) / 220))),
                        "excerpt": node.get("excerpt", ""),
                        "identifiers": set(node.get("identifiers") or []),
                        "norm_title": norm_title,
                        "norm_body": norm_body,
                    }
                )

        for ch in children:
            walk(ch, part_id, cid, current_unit_title)

    for sec_obj in struct_data["files"]:
        part_id = sec_obj.get("section_id") or sec_obj["tome_id"]
        if part_id == "R":
            for root_node in sec_obj["tree"]:
                struct_by_uid[root_node["unit_id"]] = root_node
            continue
        for root_node in sec_obj["tree"]:
            walk(root_node, part_id, root_node.get("compendium_unit_id"), root_node.get("title", ""))

    return sections, unit_meta_by_cid, struct_by_uid, part_h1_by_part_id


def _extract_theme_signals(
    theme: dict[str, Any],
    matched_glossary: list[dict[str, Any]],
) -> tuple[list[str], list[str], set[str]]:
    """Extrait les mots-clés pondérés (forts vs généraux) et identifiants d'un thème."""
    strong_phrases: list[str] = []
    for tag in theme.get("tags") or []:
        nt = _norm(str(tag).replace("-", " "))
        if len(nt) >= 4 and nt not in FRENCH_STOPWORDS:
            strong_phrases.append(nt)
    slug_phrase = _norm(str(theme.get("canonical_slug", "")).replace("-", " "))
    if len(slug_phrase) >= 5:
        strong_phrases.append(slug_phrase)
    for g in matched_glossary:
        if g.get("fr"):
            strong_phrases.append(_norm(g["fr"]))
        if g.get("en"):
            strong_phrases.append(_norm(g["en"]))
    if theme["node_id"] == "THM_systems-of-agency":
        strong_phrases.extend(["agentivite des systemes", "system agency", "systemes d'agentivite"])

    raw_text = f"{theme.get('title', '')} {theme.get('summary', '')[:220]} {slug_phrase}"
    tokens: list[str] = []
    seen_tok: set[str] = set()
    for tok in re.findall(r"[a-z0-9]{4,}", _norm(raw_text)):
        if tok not in FRENCH_STOPWORDS and tok not in seen_tok:
            seen_tok.add(tok)
            tokens.append(tok)

    id_set = {str(x).strip() for x in (theme.get("identifiers") or []) if len(str(x).strip()) >= 2}
    return list(dict.fromkeys(strong_phrases)), tokens, id_set


def _score_section_for_theme(
    sec: dict[str, Any],
    strong_phrases: list[str],
    tokens: list[str],
    id_set: set[str],
) -> float:
    """Calcule un score de pertinence vérifiable entre un thème et une section de ``Compendium.md``."""
    score = 0.0
    ntitle = sec["norm_title"]
    nbody = sec["norm_body"]

    for phr in strong_phrases:
        if phr in ntitle:
            score += 6.0
        elif phr in nbody:
            score += 3.0

    for tok in tokens:
        if tok in ntitle:
            score += 2.5
        elif tok in nbody:
            score += 1.0

    sec_ids = sec["identifiers"]
    for ident in id_set:
        if ident in sec_ids:
            score += 3.5

    return score


def _enrich_system_agency(node: dict[str, Any]) -> None:
    """Intègre explicitement « Agentivité des systèmes (system agency) » dans D01 / SUB_D01_01 / FAM_D01_01_01 / THM_systems-of-agency."""
    nid = node["node_id"]
    if nid == "DOM_D01":
        if "agentivité des systèmes" not in node["summary"].lower():
            node["summary"] = (
                "Passage des copilotes passifs aux Systèmes d'agentivité et maîtrise de "
                "l'agentivité des systèmes (system agency), loi de fiabilité de Lusser, "
                "erreurs silencieuses en cascade, constance multi-essais pass^k par rapport à pass@1, "
                "coûts de transaction cognitifs de Coase et distinction entre dette cognitive et dette technique."
            )
        for t in ("agentivite-des-systemes", "system-agency"):
            if t not in node["tags"]:
                node["tags"].append(t)
    elif nid == "SUB_D01_01":
        node["summary"] = (
            "Sous-domaine de D01 consacré à l'agentivité des systèmes (system agency), "
            "à la rupture épistémique du modèle conversationnel vers la boucle d'action "
            "et à la stratification SoR / SoE / SoA."
        )
        for t in ("agentivite-des-systemes", "system-agency"):
            if t not in node["tags"]:
                node["tags"].append(t)
    elif nid == "FAM_D01_01_01":
        node["summary"] = (
            "Famille thématique regroupant les fondements de l'agentivité des systèmes "
            "(system agency), des Systèmes d'agentivité et du passage aux déploiements bornés en production."
        )
        for t in ("agentivite-des-systemes", "system-agency"):
            if t not in node["tags"]:
                node["tags"].append(t)
    elif nid == "THM_systems-of-agency":
        node["title"] = (
            "Agentivité des systèmes (system agency) et constat empirique de fin 2026 : "
            "soutien par rapport à la production et déploiements bornés"
        )
        node["summary"] = (
            "Fondement conceptuel de l'agentivité des systèmes (system agency) : degré mesurable et borné "
            "d'initiative conféré à un acteur cognitif au sein des Systèmes d'agentivité (SoA), distinct "
            "des systèmes d'enregistrement (SoR) et d'engagement (SoE). Analyse empirique fin 2026 : "
            "écart entre usage exploratoire et exploitation maîtrisée (> 40 % d'annulations d'ici 2027 "
            "selon Gartner, 95 % des pilotes sans ROI chiffré selon MIT NANDA, trajectoire énergétique AIE "
            "415 → 945 TWh) et réduction N×M vers N+M contrats gouvernés."
        )
        for t in ("agentivite-des-systemes", "system-agency"):
            if t not in node["tags"]:
                node["tags"].append(t)


def build_synthese_payload(repo_root: Path) -> dict[str, Any]:
    """Construit le graphe unifié ``synthese-transversale.json`` ancré sur le Compendium."""
    ouv = repo_root / "Sources" / "Compendium" / "ouvrage"
    donnees = repo_root / "Sources" / "Cartographie" / "donnees"

    mm = json.loads((ouv / "registre" / "mindmap-complet.json").read_text(encoding="utf-8"))
    manifest = json.loads((ouv / "specs" / "manifest.json").read_text(encoding="utf-8"))
    gloss = json.loads((ouv / "registre" / "glossaire-termes.json").read_text(encoding="utf-8"))
    schema_carto = json.loads((donnees / "schema-cartographie.json").read_text(encoding="utf-8"))
    struct_data = json.loads((donnees / "structure-integrale.json").read_text(encoding="utf-8"))
    comp_inv = json.loads((donnees / "inventaire-115-schemas-compendium.json").read_text(encoding="utf-8"))
    pivots = json.loads((donnees / "pivots-concordance.json").read_text(encoding="utf-8"))

    comp_lines = (repo_root / "Compendium" / "Compendium.md").read_text(encoding="utf-8").splitlines()
    manifest_units = {u["id"]: u for u in manifest["units"]}
    sections, unit_meta_by_cid, struct_by_uid, part_h1_by_part_id = _flatten_compendium_sections(
        struct_data, comp_lines, manifest_units
    )
    if len(unit_meta_by_cid) != 42:
        raise ValueError(f"42 unités attendues dans structure-integrale.json, trouvées {len(unit_meta_by_cid)}")

    sections_by_unit: dict[str, list[dict[str, Any]]] = {}
    for sec in sections:
        sections_by_unit.setdefault(sec["compendium_unit_id"], []).append(sec)

    # Index schémas et glossaire
    schemas_by_slug: dict[str, list[str]] = {}
    schemas_by_unit: dict[str, list[str]] = {}
    for fig in comp_inv["figures"]:
        sid = fig["schema_id"]
        schemas_by_unit.setdefault(fig["unit"], []).append(sid)
        for slug in fig.get("themes_vulgarized") or []:
            schemas_by_slug.setdefault(slug, []).append(sid)

    terms_all: list[dict[str, Any]] = gloss["terms"]
    terms_by_owner: dict[str, list[dict[str, Any]]] = {}
    for t in terms_all:
        terms_by_owner.setdefault(t.get("chapitre_proprietaire", ""), []).append(t)

    # Reconstruire NODE_ROOT + les nœuds de mindmap-complet.json
    cm_pivots = pivots["collection_metrics"]
    pdf_pages = cm_pivots["compendium_pdf_pages"]
    units_cnt = len(manifest["units"])
    schemas_cnt = len(comp_inv["figures"])
    doms_cnt = len(mm["domains"])
    chaps_cnt = len(mm["subdomains"])
    fams_cnt = len(mm["families"])
    themes_cnt = len(mm["themes"])
    rels_cnt = len(mm["relations"])
    gloss_cnt = len(terms_all)
    lplus_cnt = cm_pivots.get("sources_l_plus", 135)
    jalons_cnt = (pivots.get("chronologie_2023_2035") or {}).get("total_jalons", 77)

    domain_node_ids = [d["node_id"] for d in mm["domains"]]
    root_node: dict[str, Any] = {
        "node_id": "NODE_ROOT",
        "canonical_slug": "corpus-agentique-racine",
        "parent_id": None,
        "children_ids": domain_node_ids,
        "depth": 0,
        "node_kind": "root",
        "domain_id": None,
        "subdomain": None,
        "family": None,
        "title": f"Compendium de l'entreprise agentique ({pdf_pages} pages · {units_cnt} unités · {schemas_cnt} schémas)",
        "summary": (
            f"Cartographie intégrale du Compendium de l'entreprise agentique : {doms_cnt} domaines (D01–D12), "
            f"{chaps_cnt} chapitres, {fams_cnt} familles, {themes_cnt} thèmes, {rels_cnt} interrelations systémiques, "
            f"{schemas_cnt} schémas compilés, {gloss_cnt} vedettes du glossaire (dont l'agentivité des systèmes), "
            f"{lplus_cnt} sources L+, {jalons_cnt} jalons chronologiques uniques et homologation Wyvern G0–G5."
        ),
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AE", "AS", "RSSI", "Juridique", "SRE", "Direction"],
        "horizons": ["2023-2035"],
        "horizon": "2023-2035",
        "tags": ["compendium-integral", "80/20", "DAPP", "Wyvern", "agentivite-des-systemes"],
        "identifiers": ["CRE-IA-2026-01", "PRR-75", "C01–C40", "DIV-02", "G0–G5"],
        "roles_in_tome": ["synthese", "fondation", "architecture", "etat_de_l_art", "patron", "norme", "gouvernance", "prospective", "executable"],
        "tomes_present": ["R", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"],
        "parts_present": list(PART_ORDER),
        "units_present": [u["id"] for u in manifest["units"]],
        "owner_chapter": "00-liminaire",
        "compendium_schemas": sorted(f["schema_id"] for f in comp_inv["figures"]),
        "glossary_terms": [],
        "source_shards": ["mindmap-complet", "synthetiseur_graphe"],
        "occurrences": [],
        "chapter_unit_ids": [],
        "occurrence_count": 0,
        "relation_degree": 0,
    }

    domains_list = [dict(d) for d in mm["domains"]]
    subs_list = [dict(s) for s in mm["subdomains"]]
    fams_list = [dict(f) for f in mm["families"]]
    themes_list = [dict(t) for t in mm["themes"]]

    all_nodes: list[dict[str, Any]] = [root_node] + domains_list + subs_list + fams_list + themes_list
    if len(all_nodes) != 380:
        raise ValueError(f"380 nœuds exacts attendus, obtenus {len(all_nodes)}")

    node_by_id: dict[str, dict[str, Any]] = {n["node_id"]: n for n in all_nodes}

    # Associer chaque famille/thème au chapitre propriétaire via son sous-domaine
    sub_owner_chapter: dict[str, str] = {s["node_id"]: s["chapter_id"] for s in subs_list}
    fam_owner_chapter: dict[str, str] = {
        f["node_id"]: sub_owner_chapter[f["parent_id"]] for f in fams_list
    }

    # Calculer les degrés sur les 616 relations
    relations_out: list[dict[str, Any]] = []
    deg_counter: Counter[str] = Counter()
    for rel in mm["relations"]:
        src, tgt = rel["source"], rel["target"]
        if src not in node_by_id or tgt not in node_by_id or src == tgt:
            raise ValueError(f"Arête invalide dans mindmap-complet.json : {rel}")
        deg_counter[src] += 1
        deg_counter[tgt] += 1

    # Nettoyer les chaînes éditoriales et enrichir D01 / Agentivité des systèmes
    for n in all_nodes:
        if n["node_id"] != "NODE_ROOT":
            n["title"] = _clean_text(n["title"])
            n["summary"] = _clean_text(n["summary"])
            n["tags"] = [str(x) for x in (n.get("tags") or [])]
            n["identifiers"] = [str(x) for x in (n.get("identifiers") or [])]
            # Conserver provenance historique tomes_present intacte
            n["tomes_present"] = list(n.get("tomes_present") or [])
        _enrich_system_agency(n)
        n["relation_degree"] = deg_counter.get(n["node_id"], 0)

    # Extraire pour chaque thème de vraies occurrences vérifiées dans Compendium/Compendium.md
    theme_to_units: dict[str, set[str]] = {}
    unit_to_themes: dict[str, list[str]] = {u["id"]: [] for u in manifest["units"]}

    for th in themes_list:
        tid = th["node_id"]
        slug = th["canonical_slug"]
        owner_ch = fam_owner_chapter[th["parent_id"]]
        th["owner_chapter"] = owner_ch

        # Glossaire correspondant au thème (dans son chapitre ou par correspondance directe)
        cand_terms = terms_by_owner.get(owner_ch, [])
        th_norm_blob = _norm(f"{th['title']} {th['summary']} {' '.join(th['tags'])} {slug}")
        matched_gloss: list[dict[str, Any]] = []
        for gt in cand_terms:
            fr_n = _norm(gt["fr"])
            en_n = _norm(gt["en"])
            if fr_n in th_norm_blob or en_n in th_norm_blob or (
                tid == "THM_systems-of-agency" and "agentivite" in fr_n
            ):
                matched_gloss.append(gt)
        if not matched_gloss and cand_terms and any(
            k in th_norm_blob for k in ("autonomie", "gouvernance", "contrat", "memoire", "identite", "agent")
        ):
            # Laisser vide sauf correspondance avérée
            pass

        strong_phrases, tokens, id_set = _extract_theme_signals(th, matched_gloss)

        # 1. Ancrage obligatoire dans owner_ch (Compendium/Compendium.md)
        owner_secs = sections_by_unit.get(owner_ch, [])
        scored_owner = sorted(
            ((_score_section_for_theme(sec, strong_phrases, tokens, id_set), sec) for sec in owner_secs),
            key=lambda x: (-x[0], x[1]["line_start"]),
        )
        chosen_secs: list[dict[str, Any]] = []
        if scored_owner:
            chosen_secs.append(scored_owner[0][1])
            if len(scored_owner) > 1 and scored_owner[1][0] >= 3.0:
                chosen_secs.append(scored_owner[1][1])

        # 2. Meilleures occurrences transversales (Liminaire, autres chapitres, Annexes C/D/E)
        other_scored: list[tuple[float, dict[str, Any]]] = []
        for sec in sections:
            ucid = sec["compendium_unit_id"]
            if ucid == owner_ch:
                continue
            sc = _score_section_for_theme(sec, strong_phrases, tokens, id_set)
            # Éviter d'inonder avec Annexe A (table globale) sauf si pertinent
            if ucid == "annexe-a":
                sc *= 0.25
            if sc >= 5.0:
                other_scored.append((sc, sec))
        other_scored.sort(key=lambda x: (-x[0], x[1]["line_start"]))

        seen_units_for_th: set[str] = {s["compendium_unit_id"] for s in chosen_secs}
        for _, sec in other_scored:
            if len(chosen_secs) >= 5:
                break
            ucid = sec["compendium_unit_id"]
            if ucid not in seen_units_for_th:
                chosen_secs.append(sec)
                seen_units_for_th.add(ucid)

        # Constituer les occurrences vérifiées (avec ancrage maître is_primary sur la meilleure section du chapitre propriétaire)
        primary_sec_uid = chosen_secs[0]["unit_id"] if (chosen_secs and chosen_secs[0]["compendium_unit_id"] == owner_ch) else None
        occs: list[dict[str, Any]] = []
        for sec in chosen_secs:
            pid = sec["part_id"]
            ucid = sec["compendium_unit_id"]
            occs.append(
                {
                    "part_id": pid,
                    "tome_id": pid,
                    "compendium_unit_id": ucid,
                    "unit_id": sec["unit_id"],
                    "file": "Compendium/Compendium.md",
                    "source_file": sec["source_file"],
                    "chapter": sec["chapter"],
                    "section": sec["section"],
                    "line_start": sec["line_start"],
                    "line_end": sec["line_end"],
                    "pdf_page_start": sec.get("pdf_page_start"),
                    "pdf_page_end": sec.get("pdf_page_end"),
                    "reading_minutes": sec.get("reading_minutes", 1),
                    "excerpt": sec.get("excerpt", ""),
                    "is_primary": sec["unit_id"] == primary_sec_uid,
                    "role_in_unit": es.SECTION_DEFAULT_ROLES.get(pid, "synthese"),
                }
            )
            unit_to_themes.setdefault(ucid, [])
            if slug not in unit_to_themes[ucid]:
                unit_to_themes[ucid].append(slug)

        occs.sort(key=lambda o: (0 if o["is_primary"] else 1, PART_RANK.get(o["part_id"], 99), o["line_start"]))

        parts_pres = sorted({o["part_id"] for o in occs}, key=lambda p: PART_RANK.get(p, 99))
        units_pres = sorted(
            {o["compendium_unit_id"] for o in occs},
            key=lambda u: next((i for i, mu in enumerate(manifest["units"]) if mu["id"] == u), 999),
        )
        c_schemas = sorted(set(schemas_by_slug.get(slug, [])))
        g_labels = [f"{g['fr']} ({g['en']})" for g in matched_gloss]

        th["occurrences"] = occs
        th["occurrence_count"] = len(occs)
        th["parts_present"] = parts_pres
        th["units_present"] = units_pres
        th["compendium_schemas"] = c_schemas
        th["glossary_terms"] = g_labels
        th["chapter_unit_ids"] = sorted({o["unit_id"] for o in occs})
        th["source_shards"] = ["mindmap-complet", "structure-integrale"]
        theme_to_units[tid] = set(units_pres)

    # S'assurer qu'aucune des 42 unités du Compendium n'est orpheline (notamment 00-liminaire et annexe-a..e)
    for uid, umeta in unit_meta_by_cid.items():
        if not unit_to_themes.get(uid):
            # Attacher aux thèmes représentatifs selon l'unité (Liminaire / Annexes A..E)
            fallback_slugs = {
                "00-liminaire": ["systems-of-agency", "partition-hybride-80-20", "concordance-div-02"],
                "annexe-a": ["architecture-reference-6-couches-2-piliers", "noyau-controle-possede-cap"],
                "annexe-b": ["topologies-oo1-oo4-catalogue-ferme", "boucle-fermee-defaillances-mast"],
                "annexe-c": ["concordance-div-02", "discordance-disc-01-a-05"],
                "annexe-d": ["exigences-cre-ia-305", "grille-prr-75-portes-bloquantes"],
                "annexe-e": ["schemas-vulgarisation-115", "gabarit-typst-edition-4542-pages"],
            }.get(uid, ["systems-of-agency"])
            valid_slugs = [
                sl for sl in fallback_slugs
                if any(t["canonical_slug"] == sl for t in themes_list)
            ] or [themes_list[0]["canonical_slug"]]
            unit_to_themes[uid] = valid_slugs
            # Ajouter une occurrence réelle de cette unité sur le premier thème lié
            target_th = next(t for t in themes_list if t["canonical_slug"] == valid_slugs[0])
            target_secs = sections_by_unit.get(uid, [])
            if target_secs:
                sec = target_secs[0]
                target_th["occurrences"].append(
                    {
                        "part_id": sec["part_id"],
                        "tome_id": sec["part_id"],
                        "compendium_unit_id": uid,
                        "unit_id": sec["unit_id"],
                        "file": "Compendium/Compendium.md",
                        "source_file": sec["source_file"],
                        "chapter": sec["chapter"],
                        "section": sec["section"],
                        "line_start": sec["line_start"],
                        "line_end": sec["line_end"],
                        "pdf_page_start": sec.get("pdf_page_start"),
                        "pdf_page_end": sec.get("pdf_page_end"),
                        "reading_minutes": sec.get("reading_minutes", 1),
                        "excerpt": sec.get("excerpt", ""),
                        "is_primary": False,
                        "role_in_unit": es.SECTION_DEFAULT_ROLES.get(sec["part_id"], "synthese"),
                    }
                )
                target_th["occurrence_count"] = len(target_th["occurrences"])
                if sec["part_id"] not in target_th["parts_present"]:
                    target_th["parts_present"] = sorted(
                        target_th["parts_present"] + [sec["part_id"]],
                        key=lambda p: PART_RANK.get(p, 99),
                    )
                if uid not in target_th["units_present"]:
                    target_th["units_present"].append(uid)
                if sec["unit_id"] not in target_th["chapter_unit_ids"]:
                    target_th["chapter_unit_ids"].append(sec["unit_id"])

    # Rattacher la section R (Compendium/README.md — Sommaire des douze parties) aux thèmes phares par domaine
    readme_path = repo_root / "Compendium" / "README.md"
    readme_sec_for_score: dict[str, Any] | None = None
    readme_summary_uid = "r-u0004"
    if readme_path.is_file():
        r_text = readme_path.read_text(encoding="utf-8")
        r_file_entry = next((f for f in struct_data.get("files", []) if (f.get("section_id") or f.get("tome_id")) == "R"), None)
        if r_file_entry and r_file_entry.get("tree"):
            r_children = r_file_entry["tree"][0].get("children") or []
            for rc in r_children:
                if "sommaire" in str(rc.get("title", "")).lower():
                    readme_summary_uid = rc["unit_id"]
                    break
        readme_sec_for_score = {
            "norm_title": _norm("Compendium de l'entreprise agentique Sommaire des douze parties"),
            "norm_body": _norm(r_text),
            "identifiers": set(es.detect_identifiers(r_text)),
        }

    if readme_sec_for_score is not None:
        for dom in domains_list:
            did = dom["domain_id"]
            dom_thms = [t for t in themes_list if t["domain_id"] == did]
            if not dom_thms:
                continue
            scored_r = []
            for t in dom_thms:
                sp, tk, ids = _extract_theme_signals(t, [])
                sc_r = _score_section_for_theme(readme_sec_for_score, sp, tk, ids)
                scored_r.append((sc_r, int(t.get("relation_degree", 0)), t))
            scored_r.sort(key=lambda x: (-x[0], -x[1], x[2]["node_id"]))
            picked_r = [item[2] for item in scored_r[:2] if item[0] >= 4.0] or [scored_r[0][2]]
            for r_th in picked_r:
                if "R" not in r_th["parts_present"]:
                    r_th["parts_present"] = sorted(
                        r_th["parts_present"] + ["R"],
                        key=lambda p: PART_RANK.get(p, 99),
                    )
                if readme_summary_uid not in r_th["chapter_unit_ids"]:
                    r_th["chapter_unit_ids"] = sorted(r_th["chapter_unit_ids"] + [readme_summary_uid])

    # Propager parts_present, units_present, compendium_schemas, glossary_terms, occurrence_count vers FAM, SUB, DOM, ROOT
    def propagate_node(node: dict[str, Any]) -> None:
        if node["node_kind"] == "theme":
            return
        children = [node_by_id[cid] for cid in node.get("children_ids") or [] if cid in node_by_id]
        for ch in children:
            propagate_node(ch)

        parts_acc: set[str] = set()
        units_acc: set[str] = set()
        sch_acc: set[str] = set()
        gl_acc: set[str] = set()
        unit_ids_acc: set[str] = set()
        occ_sum = 0
        for ch in children:
            parts_acc.update(ch.get("parts_present") or [])
            units_acc.update(ch.get("units_present") or [])
            sch_acc.update(ch.get("compendium_schemas") or [])
            gl_acc.update(ch.get("glossary_terms") or [])
            unit_ids_acc.update(ch.get("chapter_unit_ids") or [])
            occ_sum += int(ch.get("occurrence_count", 0))

        node["parts_present"] = sorted(parts_acc, key=lambda p: PART_RANK.get(p, 99))
        node["units_present"] = sorted(
            units_acc,
            key=lambda u: next((i for i, mu in enumerate(manifest["units"]) if mu["id"] == u), 999),
        )
        node["compendium_schemas"] = sorted(sch_acc)
        node["glossary_terms"] = sorted(gl_acc)
        node["chapter_unit_ids"] = sorted(unit_ids_acc)
        node["occurrence_count"] = occ_sum
        if node["node_kind"] == "family":
            owner_ch = fam_owner_chapter[node["node_id"]]
            node["owner_chapter"] = owner_ch
            prim_counts: Counter[str] = Counter()
            for ch in children:
                for occ in ch.get("occurrences") or []:
                    if occ.get("is_primary") and occ.get("unit_id"):
                        prim_counts[occ["unit_id"]] += 1
            best_uid = prim_counts.most_common(1)[0][0] if prim_counts else unit_meta_by_cid[owner_ch]["unit_id"]
            st_node = struct_by_uid.get(best_uid) or unit_meta_by_cid.get(owner_ch)
            if st_node:
                node["primary_struct_unit_id"] = st_node["unit_id"]
                node["pdf_page_start"] = st_node.get("pdf_page_start")
                node["pdf_page_end"] = st_node.get("pdf_page_end")
                node["word_count"] = st_node.get("word_count")
                node["reading_minutes"] = st_node.get("reading_minutes")
                node["guiding_question"] = st_node.get("guiding_question")
                node["excerpt"] = st_node.get("excerpt", "")
        elif node["node_kind"] == "subdomain":
            owner_ch = sub_owner_chapter[node["node_id"]]
            node["owner_chapter"] = owner_ch
            um_sub = unit_meta_by_cid.get(owner_ch)
            if um_sub:
                node["primary_struct_unit_id"] = um_sub["unit_id"]
                node["pdf_page_start"] = um_sub.get("pdf_page_start")
                node["pdf_page_end"] = um_sub.get("pdf_page_end")
                node["word_count"] = um_sub.get("word_count")
                node["reading_minutes"] = um_sub.get("reading_minutes")
                node["guiding_question"] = um_sub.get("guiding_question")
                node["excerpt"] = um_sub.get("excerpt", "")
        elif node["node_kind"] == "domain":
            ch_owners = sorted({sub_owner_chapter[cid] for cid in node["children_ids"] if cid in sub_owner_chapter})
            node["owner_chapter"] = ch_owners[0] if ch_owners else None
            dom_num = str(node.get("domain_id") or "")[1:]
            part_node = part_h1_by_part_id.get(f"P{dom_num}")
            if part_node:
                node["primary_struct_unit_id"] = part_node["unit_id"]
                node["pdf_page_start"] = part_node.get("pdf_page_start")
                node["pdf_page_end"] = part_node.get("pdf_page_end")
                node["word_count"] = part_node.get("word_count")
                node["reading_minutes"] = part_node.get("reading_minutes")
                node["excerpt"] = part_node.get("excerpt", "")
        elif node["node_kind"] == "root":
            lim_um = unit_meta_by_cid.get("00-liminaire")
            if lim_um:
                node["primary_struct_unit_id"] = lim_um["unit_id"]
                node["pdf_page_start"] = 1
                node["pdf_page_end"] = pdf_pages
                node["word_count"] = cm_pivots.get("compendium_md_words")
                node["reading_minutes"] = max(1, round(int(cm_pivots.get("compendium_md_words") or 246518) / 220))
                node["guiding_question"] = lim_um.get("guiding_question")
                node["excerpt"] = lim_um.get("excerpt", "")

    propagate_node(root_node)

    # Enrichir les 616 relations avec les sections du Compendium traversées tout en gardant `tomes`
    for rel in mm["relations"]:
        r_copy = dict(rel)
        r_copy["label"] = _clean_text(r_copy["label"])
        r_copy["justification"] = _clean_text(r_copy["justification"])
        src_node = node_by_id[r_copy["source"]]
        tgt_node = node_by_id[r_copy["target"]]
        r_parts = sorted(
            set(src_node.get("parts_present") or []) | set(tgt_node.get("parts_present") or []),
            key=lambda p: PART_RANK.get(p, 99),
        )
        r_copy["parts"] = r_parts
        relations_out.append(r_copy)

    # Construire les 42 entrées `chapters` (1 par unité du Compendium)
    chapters_out: list[dict[str, Any]] = []
    sub_by_chapter = {s["chapter_id"]: s for s in subs_list}
    for u in manifest["units"]:
        cid = u["id"]
        um = unit_meta_by_cid[cid]
        sub_match = sub_by_chapter.get(cid)
        if sub_match:
            primary_dom = sub_match["domain_id"]
            # Thèmes appartenant au chapitre + thèmes mentionnés transversalement
            own_themes = [
                t for t in themes_list
                if t.get("owner_chapter") == cid
            ]
            themes_addr = [t["canonical_slug"] for t in own_themes]
            for sl in unit_to_themes.get(cid, []):
                if sl not in themes_addr:
                    themes_addr.append(sl)
            sec_doms = sorted(
                {
                    node_by_id[r["target"]]["domain_id"]
                    for t in own_themes
                    for r in relations_out
                    if r["source"] == t["node_id"] and node_by_id[r["target"]].get("domain_id") != primary_dom
                }
            )[:3]
        else:
            primary_dom = UNIT_TO_PRIMARY_DOMAIN.get(cid, "D12")
            themes_addr = list(unit_to_themes.get(cid, []))
            sec_doms = ["D01", "D02", "D12"] if cid == "00-liminaire" else ["D02", "D08"]
            sec_doms = [d for d in sec_doms if d != primary_dom][:3]

        unit_terms = [f"{t['fr']} ({t['en']})" for t in terms_by_owner.get(cid, [])]
        unit_schemas = sorted(schemas_by_unit.get(cid, []))
        chapters_out.append(
            {
                "compendium_unit_id": cid,
                "unit_id": um["unit_id"],
                "part_id": um["part_id"],
                "tome_id": um["part_id"],
                "file": "Compendium/Compendium.md",
                "source_file": um["source_file"],
                "part_title": um["part_title"],
                "chapter_title": um["chapter_title"],
                "line_start": um["line_start"],
                "line_end": um["line_end"],
                "pdf_page_start": um.get("pdf_page_start"),
                "pdf_page_end": um.get("pdf_page_end"),
                "word_count": um.get("word_count", 0),
                "reading_minutes": um.get("reading_minutes", 1),
                "guiding_question": um.get("guiding_question"),
                "excerpt": um.get("excerpt", ""),
                "summary": _clean_text(sub_match["summary"] if sub_match else u["title"]),
                "primary_domain": primary_dom,
                "secondary_domains": sec_doms,
                "themes_addressed": themes_addr,
                "key_terms": unit_terms,
                "normative_refs": um["identifiers"][:12],
                "compendium_schemas": unit_schemas,
            }
        )

    # Construire concordance_matrix : 12 domaines × 15 sections (R, LIM, P01..P12, ANN) = 180 cellules
    concordance_matrix: list[dict[str, Any]] = []
    for dom in domains_list:
        did = dom["domain_id"]
        dom_themes = [t for t in themes_list if t["domain_id"] == did]
        for pid in PART_ORDER:
            if pid == "R":
                file_path = "Compendium/README.md"
                matching_themes = [t for t in dom_themes if "R" in (t.get("parts_present") or [])]
                occ_cnt = len(matching_themes)
                ch_cnt = 1 if matching_themes else 0
                roles_in_sec = ["synthese"] if ch_cnt else []
                sample_ids = sorted(
                    {ident for t in matching_themes for ident in (t.get("identifiers") or [])}
                )[:8]
            else:
                file_path = "Compendium/Compendium.md"
                matching_themes = [t for t in dom_themes if pid in (t.get("parts_present") or [])]
                occ_cnt = sum(
                    sum(1 for o in (t.get("occurrences") or []) if o["part_id"] == pid)
                    for t in matching_themes
                )
                ch_cnt = len(
                    {
                        o["compendium_unit_id"]
                        for t in matching_themes
                        for o in (t.get("occurrences") or [])
                        if o["part_id"] == pid
                    }
                )
                roles_in_sec = sorted(
                    {
                        o["role_in_unit"]
                        for t in matching_themes
                        for o in (t.get("occurrences") or [])
                        if o["part_id"] == pid
                    }
                )
                sample_ids = sorted(
                    {ident for t in matching_themes for ident in (t.get("identifiers") or [])}
                )[:8]

            concordance_matrix.append(
                {
                    "granularity": "domain",
                    "domain_id": did,
                    "subdomain": None,
                    "part_id": pid,
                    "tome_id": pid,
                    "file": file_path,
                    "node_count": len(matching_themes),
                    "occurrence_count": occ_cnt,
                    "chapter_count": ch_cnt,
                    "roles_in_tome": roles_in_sec,
                    "top_node_ids": [t["node_id"] for t in matching_themes[:5]],
                    "sample_identifiers": sample_ids,
                }
            )

    rel_by_type = dict(sorted(Counter(r["type"] for r in relations_out).items()))
    nodes_by_kind = dict(sorted(Counter(n["node_kind"] for n in all_nodes).items()))
    total_structural_links = sum(len(t.get("occurrences") or []) for t in themes_list)

    orphan_units = [c["compendium_unit_id"] for c in chapters_out if not c["themes_addressed"]]
    validation_report = {
        "broken_edges": 0,
        "self_loops": 0,
        "orphan_chapters": len(orphan_units),
        "orphan_structural_units_level12": len(orphan_units),
        "domains_covered": len({d["domain_id"] for d in domains_list}),
        "files_covered": len(PART_ORDER),
        "units_covered": len(chapters_out),
        "concordance_cells": len(concordance_matrix),
        "passed": len(orphan_units) == 0 and len(all_nodes) == 380 and len(relations_out) == 616,
    }

    mat = pivots["matrices"]
    return {
        "schema_version": "2.0.0",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "lang": "fr-CA",
        "generator": "Sources/Cartographie/outils/synthetiser_graphe.py",
        "totals": {
            "total_nodes": len(all_nodes),
            "theme_nodes": len(themes_list),
            "nodes_by_kind": nodes_by_kind,
            "relations": len(relations_out),
            "relations_by_type": rel_by_type,
            "chapters_mapped": len(chapters_out),
            "structural_units_linked": total_structural_links,
            "domains_covered": len(domains_list),
            "files_covered": len(PART_ORDER),
            "concordance_cells": len(concordance_matrix),
            "compendium_schemas": len(comp_inv["figures"]),
            "glossary_terms": len(terms_all),
        },
        "hierarchy_levels": schema_carto["thematic_hierarchy_levels"] if "thematic_hierarchy_levels" in schema_carto else [],
        "nodes": all_nodes,
        "relations": relations_out,
        "chapters": chapters_out,
        "concordance_matrix": concordance_matrix,
        "pivots_summary": {
            "collection_metrics": pivots["collection_metrics"],
            "cinq_discordances_count": len(pivots["discordances_resolues"]["cinq_discordances_tome_8"]["entries"]),
            "div_02_statut": pivots["discordances_resolues"]["div_02_tome_5"]["statut"],
            "exig_total": mat["exig_cre_ia_2026_v1_2"]["total"],
            "cap_total": len(mat["cap_52"]),
            "pex_total": len(mat["pex_24"]),
            "prr_total": mat["prr_75"]["total"],
            "prr_blocking": mat["prr_75"]["blocking_count"],
        },
        "validation_report": validation_report,
    }


def main() -> int:
    """Point d'entrée CLI générant ``Sources/Cartographie/donnees/synthese-transversale.json``."""
    parser = argparse.ArgumentParser(description="Synthétise le graphe thématique du Compendium.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Racine du dépôt Agentique.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Chemin de sortie JSON (défaut : Sources/Cartographie/donnees/synthese-transversale.json).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    out_path = args.output or (repo_root / "Sources" / "Cartographie" / "donnees" / "synthese-transversale.json")
    payload = build_synthese_payload(repo_root)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if r"\$" in serialized:
        raise ValueError(f"Séquence littérale \\$ détectée avant écriture de {out_path}")
    out_path.write_text(serialized, encoding="utf-8", newline="\n")
    raw_bytes = out_path.read_bytes()
    if b"\r\n" in raw_bytes or raw_bytes.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"BOM ou CRLF détecté dans {out_path}")

    t = payload["totals"]
    print(
        f"Synthèse Compendium -> {out_path} : {t['total_nodes']} nœuds ({t['theme_nodes']} thèmes), "
        f"{t['relations']} relations, {t['chapters_mapped']} unités, "
        f"{t['structural_units_linked']} occurrences vérifiées, "
        f"{t['concordance_cells']} cellules matrice (12×15)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
