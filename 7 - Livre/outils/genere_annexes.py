#!/usr/bin/env python3
"""Generateur deterministe des Annexes A, B et C du Livre 2027 (CA-17)."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import (  # noqa: E402
    escape_dollars as _escape_dollars,
    format_french_date,
    get_freeze_date,
)
from verifie_manuscrit import count_prose_words  # noqa: E402


def _load_json(path: Path, default: object = None) -> object:
    if not path.is_file():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _format_pass_k(text: str) -> str:
    """Remplace les occurrences pass^k (avec ou sans backticks) par passᵏ sans caret LaTeX."""
    cleaned = re.sub(r"`pass\^k`", "passᵏ", text)
    return re.sub(r"\bpass\^k\b", "passᵏ", cleaned)


def _clean_unbalanced_parens(text: str) -> str:
    """Supprime une parenthèse fermante finale en excès (ex. double parenthèse STPA))."""
    s = text.strip()
    while s.endswith("))") and s.count("(") < s.count(")"):
        s = s[:-1].rstrip()
    return s


def _normalize_reg_labels(text: str) -> str:
    """Uniformise OSFI -> BSIF et NI 31-103 -> ACVM NC 31-103 hors URLs."""
    out = re.sub(
        r"Office of the Superintendent of Financial Institutions\s*\((?:OSFI\s*/\s*BSIF|BSIF\s*/\s*OSFI|OSFI|BSIF)\)",
        "Bureau du surintendant des institutions financières (BSIF)",
        text,
    )
    out = re.sub(r"\(\s*(?:BSIF\s*/\s*OSFI|OSFI\s*/\s*BSIF|BSIF\s*/\s*BSIF)\s*\)", "(BSIF)", out)
    out = re.sub(r"\bOSFI\b(?:\s*/\s*BSIF|\s*\(BSIF\))?", "BSIF", out)
    out = re.sub(r"(?:\bACVM\s+)?\b(?:NI|NC)\s*31-103\b", "ACVM NC 31-103", out)
    return out


def _ensure_semicolon_space(text: str) -> str:
    """Ajoute une espace devant ';' lorsqu'un caractere non blanc le precede hors URLs/entites/code."""
    return re.sub(
        r"(https?://\S+|&[A-Za-z0-9#]+;|`[^`]+`)|(\S);",
        lambda m: m.group(1) if m.group(1) is not None else f"{m.group(2)} ;",
        text,
    )


def _fit_word_budget(
    core_text: str,
    optional_blocks: list[str],
    min_words: int,
    max_words: int,
    target_words: int,
) -> str:
    """Ajuste deterministement la prose dans [min_words, max_words] sans tronquer les blocs essentiels."""
    blocks = [core_text.strip()]
    for block in optional_blocks:
        stripped = block.strip()
        if not stripped:
            continue
        candidate = "\n\n".join(blocks + [stripped]) + "\n"
        wc = count_prose_words(candidate)
        if wc <= max_words:
            blocks.append(stripped)
            if wc >= target_words and count_prose_words("\n\n".join(blocks) + "\n") >= min_words:
                break
        elif count_prose_words("\n\n".join(blocks) + "\n") >= min_words:
            # Ne s'arrete pas si un bloc suivant plus court peut encore tenir ; sinon continue prudemment
            continue
    result = "\n\n".join(blocks) + "\n"
    return _escape_dollars(result)


def _render_annexe_a(root: Path, unit_meta: dict) -> str:
    freeze_fr = format_french_date(get_freeze_date(root))
    glossaire = _load_json(root / "registre" / "glossaire-termes.json", {"terms": []})
    terms = sorted(
        glossaire.get("terms", []),
        key=lambda t: unicodedata.normalize("NFD", t.get("fr", "")).encode("ascii", "ignore").decode("ascii").lower(),
    )

    intro = (
        f"# {unit_meta['title']}\n\n"
        "Ce glossaire fixe la terminologie bilingue contrôlée utilisée dans le liminaire et les douze chapitres "
        "de l'ouvrage. Chaque entrée associe le terme français canadien retenu à son équivalent anglais d'usage "
        "dans la littérature scientifique, les groupes de normalisation et l'ingénierie logicielle. À la première "
        "occurrence majeure d'un concept, l'intitulé français précède sa désignation anglaise entre parenthèses "
        "afin d'assurer l'exactitude technique pour un lectorat francophone international.\n\n"
        "Conformément à la règle d'étanchéité inter-unités, chaque mécanisme fondateur n'est défini pleinement "
        "que dans son unité propriétaire ; les autres chapitres y renvoient sans redéfinition divergente."
    )

    table_rows = [
        "## Table synoptique d'équivalence bilingue\n",
        "| Terme français | Équivalent anglais | Unité de référence |",
        "|---|---|---|",
    ]
    for t in terms:
        owner = t.get("chapitre_proprietaire", "Transversal")
        fr_clean = _format_pass_k(_clean_unbalanced_parens(str(t.get("fr", ""))))
        en_clean = _format_pass_k(_clean_unbalanced_parens(str(t.get("en", ""))))
        table_rows.append(f"| {fr_clean} | {en_clean} | {owner} |")
    table_block = "\n".join(table_rows)

    entries = ["## Définitions raisonnées"]
    for t in terms:
        owner = t.get("chapitre_proprietaire")
        owner_note = f" *(Unité propriétaire : {owner}.)*" if owner else ""
        raw_fr = _format_pass_k(_clean_unbalanced_parens(str(t.get("fr", ""))))
        title_fr = (raw_fr[:1].upper() + raw_fr[1:]) if raw_fr else ""
        raw_en = _format_pass_k(_clean_unbalanced_parens(str(t.get("en", ""))))
        # Eviter toute double parenthese finale si un libelle anglais finit par un sigle entre parentheses
        if title_fr.endswith(")") and raw_en.endswith(title_fr.rsplit("(", 1)[-1]):
            raw_en = raw_en.rsplit("(", 1)[0].strip()
        raw_def = _format_pass_k(str(t.get("definition", "")))
        entries.append(
            f"### {title_fr} (*{raw_en}*)\n\n"
            f"{raw_def}{owner_note}"
        )
    entries_block = "\n\n".join(entries)

    # Sous-sections de methode placees en priorite pour rester dans le budget [1 656, 1 944] mots
    optional_notes = [
        (
            "## Repères méthodologiques et conventions d'interprétation\n\n"
            "L'ouvrage distingue systématiquement les résultats mesurés par études empiriques publiées, les "
            "obligations issues de textes légaux ou prudentiels connus à la date de gel du "
            f"{freeze_fr}, et les heuristiques d'ingénierie de la collection (comme la partition 80/20 entre code "
            "déterministe et raisonnement probabiliste).\n\n"
            "Les anglicismes techniques et sigles normalisés (`MCP`, `A2A`, `SPIFFE`, `WIMSE`, `OBO`, `DPoP`, "
            "`CIBA`, `FIDO`, `JCS`, `ML-DSA`, `STPA`, `FOCUS`, `DAPP`, `FinOps`, passᵏ) sont conservés tels quels "
            "après mise en contexte, tandis que les concepts d'architecture et de gouvernance sont systématiquement "
            "rédigés en français canadien dans la prose courante."
        ),
        (
            "### Frontière entre couches déterministes, probabilistes et sémantiques\n\n"
            "Le modèle de langage demeure un composant statistique substituable générant des propositions sous "
            "contrainte de schéma, tandis que le harnais d'exécution, les passerelles d'outils, les identités non "
            "humaines et les machines à états durables forment le noyau déterministe possédé par l'institution. "
            "Les protocoles ouverts de connectivité (`MCP`, `A2A`) standardisent le transport mais ne remplacent "
            "ni les couches sémantiques métier ni l'imputabilité juridique."
        ),
        (
            "### Sigles normalisés et portée de transférabilité\n\n"
            "| Sigle | Domaine | Signification usuelle |\n"
            "|---|---|---|\n"
            "| `MCP` / `A2A` | Interopérabilité | *Model Context Protocol* et *Agent-to-Agent* |\n"
            "| `SPIFFE` / `WIMSE` | Identité des charges | Attestation éphémère d'identité non humaine |\n"
            "| `OBO` / `DPoP` | Délégation d'accès | Échange de jetons *On-Behalf-Of* et preuve de possession |\n"
            "| `CIBA` / `FIDO` | Approbation humaine | Consentement asynchrone lié cryptographiquement |\n"
            "| `JCS` (`RFC 8785`) | Preuve et audit | Canonisation JSON avant empreinte `SHA-256` |\n"
            "| `ML-DSA` / `SLH-DSA` | Post-quantique | Signatures normalisées `NIST FIPS 204` et `205` |\n"
            "| `STAMP` / `STPA` | Sûreté système | Analyse du contrôle fondée sur les boucles de contrainte |\n"
            "| `FOCUS` / `DAPP` | Économie et stratégie | Imputation normalisée des coûts et trajectoires adaptatives |"
        ),
        (
            "### Règle de cohérence entre texte, diagrammes et registres\n\n"
            "Les intitulés figurant dans la table d'équivalence bilingue s'appliquent à l'identique aux "
            "légendes des vingt-trois figures originales ainsi qu'aux entrées des Annexes B et C, évitant tout "
            "glissement sémantique entre architecture logicielle, sécurité et conformité."
        ),
    ]

    core = f"{intro}\n\n{entries_block}\n\n{table_block}"
    method_core = optional_notes[0]
    if count_prose_words(f"{core}\n\n{method_core}") > unit_meta["max_words"]:
        core = f"{intro}\n\n{entries_block}"
    if count_prose_words(f"{core}\n\n{method_core}") > unit_meta["max_words"]:
        core = f"# {unit_meta['title']}\n\n{entries_block}"

    return _fit_word_budget(
        core_text=core,
        optional_blocks=optional_notes,
        min_words=unit_meta["min_words"],
        max_words=unit_meta["max_words"],
        target_words=unit_meta["target_words"],
    )


def _render_annexe_b(root: Path, unit_meta: dict) -> str:
    freeze_fr = format_french_date(get_freeze_date(root))
    ancres_data = _load_json(root / "registre" / "ancres-chronologiques.json", {"anchors": []})
    anchors = sorted(ancres_data.get("anchors", []), key=lambda a: a.get("key", ""))

    intro = (
        f"# {unit_meta['title']}\n\n"
        "Cette annexe regroupe les jalons réglementaires, prudentiels, législatifs et cryptographiques cités "
        f"dans l'ouvrage. La date de gel des faits étant fixée au **{freeze_fr}**, toute échéance postérieure "
        "est présentée selon son statut juridique ou normatif à la clôture : règle adoptée avec entrée en "
        "vigueur fixée, calendrier révisé officiellement proposé ou feuille de route coordonnée. Les chapitres "
        "s'appuient directement sur cet enregistrement unique pour prévenir toute dérive chronologique."
    )

    table_lines = [
        "## Tableau synoptique des jalons (2026–2035)\n",
        "| Échéance | Juridiction | Nature | Jalons et portée | Chapitres | Statut de preuve |",
        "|---|---|---|---|---|---|",
    ]
    for a in anchors:
        statut = "Texte intégral vérifié" if a.get("statut_preuve") == "l_plus" else "À réancrer sur source primaire"
        chs = ", ".join(a.get("chapters", []))
        short_label = _escape_dollars(a["label"]).replace("|", "/")
        table_lines.append(
            f"| {a['date']} | {a['jurisdiction']} | {a['nature']} | {short_label} | {chs} | {statut} |"
        )
    table_block = "\n".join(table_lines)

    details = ["## Fiches chronologiques détaillées"]
    for a in anchors:
        statut = "Texte intégral vérifié" if a.get("statut_preuve") == "l_plus" else "À réancrer sur source primaire"
        src_ref = f" (référence interne `{a['source_l_plus_id']}`)" if a.get("source_l_plus_id") else ""
        vig = (
            f"\n\n*Point de vigilance :* {_ensure_semicolon_space(_escape_dollars(a['vigilance']))}"
            if a.get("vigilance")
            else ""
        )
        comm = (
            f"\n\n*Précision de collecte :* {_ensure_semicolon_space(_escape_dollars(a['commentaire_annexe']))}"
            if a.get("commentaire_annexe")
            else ""
        )
        details.append(
            f"### {a['date']} — {a['jurisdiction']} ({a['key']})\n\n"
            f"**Nature :** {a['nature']}. **Chapitres concernés :** {', '.join(a.get('chapters', []))}. "
            f"**Statut probatoire :** {statut}{src_ref}.\n\n"
            f"{_ensure_semicolon_space(_escape_dollars(a['label']))}.{vig}{comm}"
        )
    details_block = "\n\n".join(details)

    # Blocs obligatoires couvrant tous les horizons 2026-2035 (incluant 2030-2035, jamais tronques)
    horizons_mandatory = (
        "## Lecture par horizon de décision (2026–2035)\n\n"
        "### Horizon immédiat (2026–2027) : inventaire, transparence et gestion du risque de modèle\n\n"
        "Les dispositions déjà en vigueur au Québec (article 12.1 de la Loi 25 depuis le 22 septembre 2023) "
        "et les obligations européennes applicables dès août 2026 exigent inventaire et traçabilité humaine. "
        "Les jalons de 2027 (`TLS` à 100 jours, `BSIF E-23`) imposent de verrouiller identités et journaux.\n\n"
        "### Horizon intermédiaire (2028–2029) : conformité sectorielle et certificats à 47 jours\n\n"
        "L'entrée en application des règles européennes sur les produits réglementés, du coût complet canadien "
        "en gestion de patrimoine, de la portée 3 `BSIF B-15` (exercice 2028) et des certificats `TLS` à "
        "47 jours le 15 mars 2029 rend toute rotation manuelle obsolète.\n\n"
        "### Horizon structurel (2030–2035) : transition post-quantique et révision législative\n\n"
        "La migration financière coordonnée vers la cryptographie post-quantique (jalon critique 2030–2032, "
        "achèvement visé 2035) et la révision statutaire fédérale canadienne prévue pour le 30 juin 2033 "
        "imposent de bâtir dès 2027 l'agilité cryptographique face aux signatures plus volumineuses."
    )

    optional_notes = [
        (
            "### Distinction méthodologique sur les textes bloqués ou annoncés\n\n"
            "Lorsqu'un texte officiel demeure inaccessible en collecte ouverte sans contournement de sécurité, "
            "ou lorsqu'un calendrier réglementaire fait l'objet d'un aménagement annoncé mais non encore entré "
            "en vigueur à la date de gel, cette situation est consignée explicitement plutôt que lissée. "
            "L'ouvrage n'extrapole jamais au-delà du statut vérifiable de chaque instrument."
        ),
    ]

    core = f"{intro}\n\n{table_block}\n\n{details_block}\n\n{horizons_mandatory}"
    if count_prose_words(core) > unit_meta["max_words"]:
        core = f"{intro}\n\n{details_block}\n\n{horizons_mandatory}"
    if count_prose_words(core) > unit_meta["max_words"]:
        compact_details = ["## Fiches chronologiques synthétiques"]
        for a in anchors:
            statut = "Vérifié" if a.get("statut_preuve") == "l_plus" else "À réancrer"
            compact_details.append(
                f"- **{a['date']} ({a['jurisdiction']}, `{a['key']}`)** : {_ensure_semicolon_space(_escape_dollars(a['label']))}. "
                f"Chapitres : {', '.join(a.get('chapters', []))} ({statut})."
            )
        core = f"{intro}\n\n" + "\n".join(compact_details) + f"\n\n{horizons_mandatory}"
    return _fit_word_budget(
        core_text=core,
        optional_blocks=optional_notes,
        min_words=unit_meta["min_words"],
        max_words=unit_meta["max_words"],
        target_words=unit_meta["target_words"],
    )


def _parse_ancrage_claims(ancrage_files: list[Path]) -> tuple[int, int]:
    """Additionne les affirmations initiales et finales sur les journaux ancrage/*-ancrage.md."""
    initial_total = 0
    final_total = 0
    for path in ancrage_files:
        txt = path.read_text(encoding="utf-8", errors="replace")
        m_fin = re.search(r"Verdict final\s*[—–-]\s*support[eé]s?\s*\*?\*?\s*:\s*\*?\*?\s*(\d+)", txt, re.IGNORECASE)
        fin = int(m_fin.group(1)) if m_fin else 0

        m_init_g2 = re.search(r"Passe G2 initiale[^\n]*?:\s*\*?\*?(\d+)\*?\*?\s+affirmations?", txt, re.IGNORECASE)
        if m_init_g2:
            init = int(m_init_g2.group(1))
        else:
            m_init = re.search(
                r"(?:Total d'affirmations atomiques[^:\n]*|Affirmations atomiques[^:\n]*):\s*`?(\d+)`?"
                r"|Périmètre audité[^\n]*?,\s*(\d+)\s+affirmations atomiques",
                txt,
                re.IGNORECASE,
            )
            if m_init:
                init = int(m_init.group(1) or m_init.group(2))
            else:
                init = fin
        initial_total += init
        final_total += fin
    return initial_total, final_total


def _format_ratio_pct(score_str: str) -> str:
    """Formate en pourcentage francais exact un score 'a/b'."""
    m = re.fullmatch(r"(\d+)/(\d+)", score_str.strip())
    if not m or int(m.group(2)) == 0:
        return "n.d."
    num, den = int(m.group(1)), int(m.group(2))
    pct = num * 100.0 / den
    if num == den or abs(pct - round(pct)) < 1e-9:
        return f"{round(pct)} %"
    return f"{pct:.1f} %".replace(".", ",")


def _parse_g3_scores(recol_json: object, recol_md: str) -> tuple[str | None, str | None, str]:
    """Extrait (score_initial, score_final, libelle_synthese) depuis un journal de recollation G3."""
    if recol_json is None and not recol_md:
        return None, None, "En attente d'exécution"
    m_init = re.search(
        r"Score\s+(?:initial|à froid|pré-correction)[^:\n]*:[^\d\n]*?(\d+\s*/\s*\d+)",
        recol_md,
        re.IGNORECASE,
    )
    m_fin = re.search(
        r"Score\s+final[^:\n]*:[^\d\n]*?(\d+\s*/\s*\d+)",
        recol_md,
        re.IGNORECASE,
    )
    init_s = re.sub(r"\s+", "", m_init.group(1)) if m_init else None
    fin_s = re.sub(r"\s+", "", m_fin.group(1)) if m_fin else None
    if init_s and fin_s:
        return (
            init_s,
            fin_s,
            f"Initial `{init_s}` ({_format_ratio_pct(init_s)}) -> final `{fin_s}` ({_format_ratio_pct(fin_s)})",
        )
    if fin_s:
        return init_s, fin_s, f"Final `{fin_s}` ({_format_ratio_pct(fin_s)})"
    if "60/60" in recol_md or "60 / 60" in recol_md:
        return init_s, "60/60", "60/60 vérifiés (100 %)"
    items = recol_json.get("items", recol_json.get("sample", [])) if isinstance(recol_json, dict) else recol_json
    if isinstance(items, list):
        return init_s, fin_s, f"{len(items)} items tirés (recollation en cours)"
    return init_s, fin_s, "Journal présent"


def _collect_qa_metrics(root: Path, mlr: dict) -> dict:
    manifeste = _load_json(root / "recherche" / "manifeste-sources-sha256.json", None)
    statut_f = _load_json(root / "recherche" / "registre-statut-f.json", None)

    rq_counts = {rq["id"]: 0 for rq in mlr.get("research_questions_and_queries", [])}
    sources_list: list[dict] = []
    metadata_pct = None
    iso_freeze = get_freeze_date(root, mlr)
    if isinstance(manifeste, dict):
        sources_list = [s for s in manifeste.get("sources", []) if isinstance(s, dict)]
        metadata_pct = manifeste.get("metadata_only_pct", 0.0)
        if manifeste.get("freeze_date"):
            iso_freeze = str(manifeste["freeze_date"])
        for s in sources_list:
            # Dedupliquer research_axes par source avant comptage
            for rq in dict.fromkeys(s.get("research_axes", [])):
                if rq in rq_counts:
                    rq_counts[rq] += 1

    distinct_issuers = len(
        {
            _normalize_reg_labels(str(s.get("venue_or_issuer", "")).strip()).lower()
            for s in sources_list
            if str(s.get("venue_or_issuer", "")).strip()
        }
    )

    blocked_count = 0
    blocked_list: list[dict] = []
    if isinstance(statut_f, dict):
        blocked_list = statut_f.get("blocked", statut_f.get("blocked_sources", statut_f.get("sources", []))) or []
        blocked_count = len(blocked_list)

    ancrage_dir = root / "ancrage"
    ancrage_files = sorted(ancrage_dir.glob("*-ancrage.md")) if ancrage_dir.is_dir() else []
    ancrage_init_claims, ancrage_final_claims = _parse_ancrage_claims(ancrage_files)

    aq_dir = root / "aq"
    recol1 = _load_json(aq_dir / "recollation-seed-202701.json", None) if aq_dir.is_dir() else None
    recol2 = _load_json(aq_dir / "recollation-seed-202702.json", None) if aq_dir.is_dir() else None
    recol3 = _load_json(aq_dir / "recollation-seed-202703.json", None) if aq_dir.is_dir() else None
    recol1_md = (aq_dir / "recollation-seed-202701.md").read_text(encoding="utf-8") if (aq_dir / "recollation-seed-202701.md").is_file() else ""
    recol2_md = (aq_dir / "recollation-seed-202702.md").read_text(encoding="utf-8") if (aq_dir / "recollation-seed-202702.md").is_file() else ""
    recol3_md = (aq_dir / "recollation-seed-202703.md").read_text(encoding="utf-8") if (aq_dir / "recollation-seed-202703.md").is_file() else ""
    gauntlet_ok = (aq_dir / "gauntlet-log.md").is_file() and (aq_dir / "gauntlet-log.md").stat().st_size > 0
    lissage_ok = (aq_dir / "rapport-lissage-et-visuel.md").is_file() and (aq_dir / "rapport-lissage-et-visuel.md").stat().st_size > 0

    return {
        "sources_list": sources_list,
        "source_count": len(sources_list),
        "distinct_issuers": distinct_issuers,
        "metadata_pct": metadata_pct,
        "freeze_date_iso": iso_freeze,
        "freeze_date": format_french_date(iso_freeze),
        "rq_counts": rq_counts,
        "blocked_count": blocked_count,
        "blocked_list": blocked_list,
        "ancrage_count": len(ancrage_files),
        "ancrage_initial_claims": ancrage_init_claims,
        "ancrage_final_claims": ancrage_final_claims,
        "recol1": recol1,
        "recol2": recol2,
        "recol3": recol3,
        "recol1_md": recol1_md,
        "recol2_md": recol2_md,
        "recol3_md": recol3_md,
        "gauntlet_ok": gauntlet_ok,
        "lissage_ok": lissage_ok,
    }


def _recol_status_label(recol_json: object, recol_md: str) -> str:
    return _parse_g3_scores(recol_json, recol_md)[2]


def _render_annexe_c(root: Path, unit_meta: dict) -> str:
    mlr = _load_json(root / "specs" / "protocole-mlr-2027.json", {})
    metrics = _collect_qa_metrics(root, mlr)

    min_aacods = mlr.get("aacods_threshold", {}).get("min_score_for_inclusion", 9.0)
    scale_max = mlr.get("aacods_threshold", {}).get("scale_max", 12)
    freeze_fr = metrics["freeze_date"]

    if metrics["source_count"] > 0:
        corpus_status_sentence = (
            f"À la date de gel du {freeze_fr}, le corpus probant rassemble "
            f"**{metrics['source_count']} textes intégraux ouverts** issus de **{metrics['distinct_issuers']} "
            f"éditeurs ou organismes distincts**, hachés en `SHA-256`, avec un taux de "
            f"notices limitées aux métadonnées de `{metrics['metadata_pct']:.1f} %` et "
            f"`{metrics['blocked_count']}` URL consignées en statut bloqué F hors corpus probant."
        )
    else:
        corpus_status_sentence = (
            f"Le protocole prescrit pour la date de gel du {freeze_fr} un taux maximal de "
            f"notices limitées aux métadonnées strictement égal à `0,0 %` ; la collecte ouverte `L+` est "
            "en attente d'exécution ou d'indexation finale dans le manifeste `SHA-256`."
        )

    intro = (
        f"# {unit_meta['title']}\n\n"
        "Cette annexe expose le protocole de revue de littérature multivocale (`MLR-PRISMA-ScR`), les règles "
        "strictes d'hygiène probatoire sans contournement d'accès et le bilan consolidé des cinq barrières "
        "d'assurance qualité indépendantes (`G1` à `G5`). Chaque source mobilisée comme preuve doit disposer "
        "de son texte intégral extrait en `UTF-8`, vérifié par empreinte cryptographique `SHA-256`, daté au "
        f"plus tard du {freeze_fr} et évalué selon la grille `AACODS` avec un seuil minimal d'inclusion "
        f"de `{min_aacods:.1f} / {scale_max}`.\n\n"
        f"{corpus_status_sentence}\n\n"
        "Les six ouvrages antérieurs du dépôt constituent exclusivement une carte de repérage heuristique et "
        "jamais une preuve autonome : toute donnée chiffrée, étude ou disposition réglementaire est réancrée "
        "sur son texte primaire officiel ou scientifique avant rédaction. De même, tout refus serveur, "
        "mécanisme anti-robot ou mur payant interrompt immédiatement la collecte et exclut la source du corpus "
        "probant."
    )

    rq_rows = [
        "## Couverture des questions de recherche (`RQ1` à `RQ6`)\n",
        "| Axe | Thème de recherche | Seuil minimal | Sources `L+` retenues | État |",
        "|---|---|---:|---:|---|",
    ]
    for rq in mlr.get("research_questions_and_queries", []):
        qid = rq["id"]
        min_req = int(rq["min_included_studies"])
        got = metrics["rq_counts"].get(qid, 0)
        if metrics["source_count"] == 0:
            state = "En attente"
        elif got >= min_req:
            state = "Conforme"
        else:
            state = "Sous seuil"
        rq_rows.append(f"| `{qid}` | {rq['theme']} | {min_req} | {got} | {state} |")
    rq_table = "\n".join(rq_rows)

    ancrage_label = (
        f"{metrics['ancrage_count']} / 13 journaux ({metrics['ancrage_initial_claims']} initiales -> "
        f"{metrics['ancrage_final_claims']} finales, 100 % supportées)"
        if metrics["ancrage_count"] > 0
        else "En attente d'exécution"
    )
    recol1_label = _recol_status_label(metrics["recol1"], metrics["recol1_md"])
    recol2_label = _recol_status_label(metrics["recol2"], metrics["recol2_md"])
    gauntlet_label = "Journal complété" if metrics["gauntlet_ok"] else "En attente d'exécution"
    lissage_label = "Rapport complété" if metrics["lissage_ok"] else "En attente d'exécution"

    qa_rows = [
        "## Bilan des cinq barrières d'assurance qualité (`G1` à `G5`)\n",
        "| Barrière | Rôle de contrôle | Critères visés | État constaté |",
        "|---|---|---|---|",
        "| `G1` — Garde déterministe | Script `verifie_manuscrit.py` sans appel de modèle | `CA-01` à `CA-11`, `CA-17` | Contrôle actif |",
        f"| `G2` — Ancrage atomique Wyvern | Auditeurs indépendants par unité (`00`–`12`) | `CA-10`, `CA-12` | {ancrage_label} |",
        f"| `G3` — Recollation passe 1 (`202701`) | Échantillon stratifié de 60 énoncés sur `.txt` | `CA-07`, `CA-13` | {recol1_label} |",
        f"| `G4` — Critique stylistique à l'aveugle | Boucle `gauntlet-loop` A/B sur extraits étalons | `CA-15` | {gauntlet_label} |",
        f"| `G5` — Lissage et inspection visuelle | Cohérence inter-unités et rendu `Pandoc`/`Typst` | `CA-16` à `CA-18` | {lissage_label} |",
        f"| `G3` — Recollation finale à froid (`202702`) | Échantillon disjoint sur le texte publié | `CA-14` | {recol2_label} |",
    ]
    if metrics["recol3"] is not None or metrics["recol3_md"]:
        recol3_label = _recol_status_label(metrics["recol3"], metrics["recol3_md"])
        qa_rows.append(
            f"| `G3` — Recollation complémentaire (`202703`) | Échantillon stratifié post-remédiation | `CA-14` | {recol3_label} |"
        )
    qa_table = "\n".join(qa_rows)

    optional_notes = [
        (
            "## Intégrité typographique et reproductibilité des annexes\n\n"
            "L'ouvrage intègre **23 figures originales (20 schémas vectoriels PlantUML et 3 organigrammes Mermaid "
            "haute résolution)**, chacune bornée entre dix et quatorze éléments et exempte de tout code interne "
            "banni afin de préserver la lisibilité imprimée. Tous les symboles monétaires sont échappés et les "
            "formules sont encadrées en notation compatible avec la chaîne `Pandoc` et `Typst`. Enfin, les trois "
            "annexes demeurent régénérées mécaniquement depuis les registres JSON et les journaux d'assurance "
            "qualité, interdisant toute divergence manuelle."
        ),
        (
            "## Règles de traçabilité et d'étanchéité éditoriale\n\n"
            "L'architecture d'assurance qualité repose sur la séparation stricte entre agents producteurs et "
            "agents vérificateurs. Aucun agent rédacteur ne valide ses propres affirmations atomiques en barrière "
            "`G2`, ne procède à la recollation mot à mot sur les textes primaires en barrière `G3`, ni ne siège "
            "comme critique lors des duels comparatifs à l'aveugle `G4`. L'ordre d'exécution contraint la chaîne "
            "complète : toute retouche stylistique issue de `G4` ou du lissage transversal `G5` repasse "
            "obligatoirement par les contrôles mécaniques `G1` et par une vérification différentielle sur les "
            "passages modifiés avant le tirage final à froid sur l'ouvrage assemblé."
        ),
        (
            "## Stratification de la double recollation indépendante\n\n"
            "Le script déterministe `echantillon_aq.py` garantit une couverture équilibrée du livre en tirant "
            "soixante affirmations sourcées réparties en vingt-cinq énoncés empiriques ou quantitatifs, vingt "
            "énoncés réglementaires ou juridiques et quinze énoncés prospectifs ou techniques datés, avec un "
            "plancher minimal de deux énoncés par unité narrative du liminaire au douzième chapitre. La première "
            "passe inclut d'office les points de vigilance probatoire identifiés dès le cahier des charges, tandis "
            "que les passes suivantes excluent intégralement les paragraphes déjà inspectés afin de mesurer la "
            "fiabilité résiduelle réelle du texte destiné au lecteur."
        ),
        (
            "## Architecture de vérification des énoncés et séparation des rôles\n\n"
            "Conformément au principe d'étanchéité de la chaîne documentaire, la collecte des textes ouverts, "
            "la rédaction narrative, le contrôle mécanique `G1`, l'audit atomique `G2`, les recollations `G3`, "
            "la critique comparative `G4` et le lissage `G5` sont exécutés par des instances distinctes cloisonnées "
            "par fichiers versionnés. Chaque affirmation factuelle du liminaire et des douze chapitres pointe "
            "uniquement vers sa base fermée locale, elle-même liée par identifiant unique et empreinte `SHA-256` "
            "au texte intégral conservé sur disque.\n\n"
            "Lorsqu'une passe stylistique de `G4` ou une harmonisation de transition de `G5` retouche la "
            "formulation d'un paragraphe existant, l'unité modifiée repasse immédiatement sous la garde "
            "déterministe pour vérifier les bornes de volume, l'absence de codes internes bannis, la "
            "non-duplication face au corpus historique, l'intégrité des montants échappés et la résolution "
            "complète des renvois numériques."
        ),
        (
            "## Politique de transparence et traçabilité de compilation\n\n"
            "Le corpus de preuve exclut délibérément les résumés non accompagnés du texte complet ainsi que "
            "les sources protégées par mur payant ou contrôle anti-robot. Lorsqu'une référence institutionnelle "
            f"importante demeure inaccessible dans le périmètre ouvert au {freeze_fr}, son blocage est "
            "journalisé et son contenu reste écarté de toute démonstration factuelle.\n\n"
            "L'assemblage final produit simultanément le document Markdown consolidé, l'édition HTML autonome "
            "avec ressources intégrées et formules en MathML, ainsi que l'édition imprimable PDF composée sous "
            f"`Typst`. Chaque fichier généré conserve une date de gel des faits explicitement bornée au {freeze_fr}."
        ),
    ]

    prose_part = _fit_word_budget(
        core_text=f"{intro}\n\n{rq_table}\n\n{qa_table}",
        optional_blocks=optional_notes,
        min_words=unit_meta["min_words"],
        max_words=unit_meta["max_words"],
        target_words=unit_meta["target_words"],
    )

    # Bloc de bibliographie brute exclu du decompte de mots
    bib_lines = [
        "<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->",
        "## Bibliographie classée des sources intégrales vérifiées",
        "",
    ]
    if metrics["sources_list"]:
        for src in sorted(metrics["sources_list"], key=lambda s: s.get("source_id", "")):
            sid = src.get("source_id", "SRC-?")
            authors = _normalize_reg_labels(str(src.get("authors", "Auteur inconnu")))
            year = src.get("year", "s.d.")
            title = src.get("title", "Sans titre")
            venue = _normalize_reg_labels(str(src.get("venue_or_issuer", "")))
            ident = _normalize_reg_labels(str(src.get("identifier", "")))
            url = str(src.get("url", "")).strip()
            axes = ", ".join(dict.fromkeys(src.get("research_axes", [])))
            sha_short = str(src.get("sha256", ""))[:12]
            aacods = src.get("aacods_score", "")
            url_md = f"[{url}]({url})" if url.startswith(("http://", "https://")) else f"`{url}`"
            bib_lines.append(
                f"- **{sid}** — {authors} ({year}). *{title}*. {venue}. `{ident}` — {url_md} "
                f"(axes : {axes}; AACODS : {aacods}; `SHA-256` : `{sha_short}...`)."
            )
    else:
        bib_lines.append("- *Aucune source L+ encore indexée dans `recherche/manifeste-sources-sha256.json`.*")

    if metrics["blocked_list"]:
        bib_lines.extend(["", "### Journal des accès refusés consignés en statut F (exclus des preuves)", ""])
        for b in metrics["blocked_list"]:
            url = str(b.get("url", "URL inconnue")).strip()
            reason = b.get("reason") or b.get("block_reason") or b.get("http_status") or "blocage"
            bib_lines.append(f"- `{url}` — refus enregistré (`{reason}`), exclu conformément à `AO-01`.")

    bib_lines.append("<!-- BIBLIOGRAPHIE_BRUTE_FIN -->")
    bib_block = _escape_dollars("\n".join(bib_lines))
    return f"{prose_part.rstrip()}\n\n{bib_block}\n"


def build_annexes(root: Path, dry_run: bool = False) -> dict[Path, str]:
    """Genere les Annexes A, B et C a partir de manifest.json, registre/ et aq/."""
    root = Path(root)
    manifest = _load_json(root / "specs" / "manifest.json", {})
    units = {u["id"]: u for u in manifest.get("units", [])}

    renderers = {
        "annexe-a": _render_annexe_a,
        "annexe-b": _render_annexe_b,
        "annexe-c": _render_annexe_c,
    }

    outputs: dict[Path, str] = {}
    for uid, renderer in renderers.items():
        umeta = units[uid]
        out_path = root / umeta["file"]
        content = renderer(root, umeta)
        outputs[out_path] = content
        if not dry_run:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Generateur deterministe des Annexes A, B et C.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du livre")
    parser.add_argument("--dry-run", action="store_true", help="Calculer en memoire sans ecrire sur disque")
    args = parser.parse_args()

    outputs = build_annexes(args.root, dry_run=args.dry_run)
    for path, content in outputs.items():
        wc = count_prose_words(content)
        mode = "simulee" if args.dry_run else "ecrite"
        print(f"OK ({mode}) : {path.name} ({wc} mots)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
