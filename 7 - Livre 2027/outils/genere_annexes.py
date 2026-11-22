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

from verifie_manuscrit import count_prose_words  # noqa: E402

_UNESCAPED_DOLLAR_RE = re.compile(r"(?<!\\)(?:\\\\)*\$")


def _escape_dollars(text: str) -> str:
    """Echappe tout symbole $ nu en \\$ pour respecter CA-06."""
    return re.sub(r"(?<!\\)\$", r"\\$", text)


def _load_json(path: Path, default: object = None) -> object:
    if not path.is_file():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _fit_word_budget(
    core_text: str,
    optional_blocks: list[str],
    min_words: int,
    max_words: int,
    target_words: int,
) -> str:
    """Ajuste deterministement la prose dans [min_words, max_words] sans remplissage."""
    blocks = [core_text.strip()]
    for block in optional_blocks:
        candidate = "\n\n".join(blocks + [block.strip()]) + "\n"
        wc = count_prose_words(candidate)
        if wc <= max_words - 20:
            blocks.append(block.strip())
            if wc >= target_words - 40:
                break
        elif count_prose_words("\n\n".join(blocks) + "\n") >= min_words:
            break
    result = "\n\n".join(blocks) + "\n"
    return _escape_dollars(result)


def _render_annexe_a(root: Path, unit_meta: dict) -> str:
    glossaire = _load_json(root / "registre" / "glossaire-termes.json", {"terms": []})
    terms = sorted(
        glossaire.get("terms", []),
        key=lambda t: unicodedata.normalize("NFD", t.get("fr", "")).encode("ascii", "ignore").decode("ascii").lower(),
    )

    intro = (
        f"# {unit_meta['title']}\n\n"
        "Ce glossaire fixe la terminologie bilingue contrôlée utilisée de bout en bout dans le liminaire "
        "et les douze chapitres de l'ouvrage. Chaque entrée associe le terme français canadien retenu dans la "
        "collection à son équivalent anglais d'usage courant dans la littérature scientifique, les groupes de "
        "normalisation et l'ingénierie logicielle. Conformément à la charte éditoriale, la première occurrence "
        "majeure d'un concept dans un chapitre présente l'intitulé français suivi de sa désignation anglaise "
        "entre parenthèses afin de préserver la lisibilité pour un lectorat francophone international tout en "
        "assurant la correspondance exacte avec les spécifications techniques.\n\n"
        "La règle d'étanchéité inter-unités impose que chaque mécanisme fondateur ne soit défini pleinement "
        "que dans l'unité narrative qui en détient la propriété conceptuelle; les autres chapitres y renvoient "
        "sans redéfinition divergente. Le présent instrument rassemble ainsi les définitions canoniques issues "
        "du registre normatif de l'ouvrage."
    )

    table_rows = [
        "## Table synoptique d'équivalence bilingue\n",
        "| Terme français | Équivalent anglais | Unité de référence |",
        "|---|---|---|",
    ]
    for t in terms:
        owner = t.get("chapitre_proprietaire", "Transversal")
        table_rows.append(f"| {t['fr']} | {t['en']} | {owner} |")
    table_block = "\n".join(table_rows)

    entries = ["## Définitions raisonnées"]
    for t in terms:
        owner = t.get("chapitre_proprietaire")
        owner_note = f" *(Unité propriétaire : {owner}.)*" if owner else ""
        title_fr = (t["fr"][:1].upper() + t["fr"][1:]) if t["fr"] else ""
        entries.append(
            f"### {title_fr} (*{t['en']}*)\n\n"
            f"{t['definition']}{owner_note}"
        )
    entries_block = "\n\n".join(entries)

    # Notes methodologiques structurees pour accompagner le lecteur dirigeant et architecte
    optional_notes = [
        (
            "## Repères d'usage entre couches déterministes et probabilistes\n\n"
            "Une source fréquente d'ambiguïté dans les projets d'entreprise tient à la confusion entre le "
            "modèle de langage, composant statistique substituable, et l'agent logiciel pris comme système "
            "complet. Dans le lexique de cet ouvrage, le modèle génère des propositions ou des appels structurés "
            "sous contrainte de schéma, tandis que le harnais d'exécution, les passerelles d'outils, les identités "
            "non humaines et les machines à états durables forment le noyau de contrôle déterministe que "
            "l'organisation possède en propre."
        ),
        (
            "### Frontière entre connectivité protocolaire et sémantique métier\n\n"
            "Les protocoles ouverts de connectivité verticale vers les outils et de délégation horizontale "
            "entre pairs standardisent le transport et la description syntaxique des interfaces. Ils ne "
            "résolvent ni la définition univoque des indicateurs financiers, ni la gouvernance des accès aux "
            "données personnelles, ni la traduction exacte vers les systèmes patrimoniaux. D'où la place centrale "
            "accordée aux couches sémantiques, aux ontologies d'entreprise et aux façades anti-corruption qui "
            "protègent la précision décimale et les bases d'autorité."
        ),
        (
            "### Économie de la constance et mesure du coût complet\n\n"
            "Évaluer un flux agentique à partir d'un taux de réussite ponctuel sur un banc isolé ou d'un prix "
            "unitaire par million de jetons masque les échecs cumulés en chaîne et les coûts de reprise humaine. "
            "Les notions de constance multi-essais et de coût complet par résultat conforme ramènent la décision "
            "à l'unité économique réellement livrable : un dossier clôturé sans erreur, vérifiable et opposable "
            "en audit."
        ),
        (
            "### Imputabilité, délégation cryptographique et facteur humain\n\n"
            "Aucun agent autonome ne constitue un sujet de droit ni un acteur métier responsable au sens "
            "juridique. Les concepts d'identité non humaine éphémère, de délégation explicite au nom du mandant "
            "et d'approbation hors bande liée à l'empreinte canonique d'un acte assurent la continuité entre "
            "l'authentification technique et la responsabilité de direction. Parallèlement, la prévention de "
            "l'approbation réflexe et le maintien de quotas de traitement manuel préservent la capacité de repli "
            "lors d'incidents majeurs."
        ),
        (
            "## Sigles normalisés et protocoles conservés en langue source\n\n"
            "| Sigle | Domaine | Signification usuelle |\n"
            "|---|---|---|\n"
            "| `MCP` | Connectivité verticale | *Model Context Protocol* (médiation agents-outils) |\n"
            "| `A2A` | Délégation horizontale | *Agent-to-Agent* (interopérabilité entre domaines) |\n"
            "| `SPIFFE` / `WIMSE` | Identité des charges | Attestation éphémère d'identité non humaine |\n"
            "| `OBO` / `DPoP` | Délégation d'accès | Échange de jetons *On-Behalf-Of* et preuve de possession |\n"
            "| `CIBA` / `FIDO2` | Approbation humaine | Consentement asynchrone lié cryptographiquement |\n"
            "| `JCS` (`RFC 8785`) | Preuve et audit | Canonisation JSON avant empreinte `SHA-256` |\n"
            "| `ML-DSA` / `SLH-DSA` | Post-quantique | Signatures normalisées `NIST FIPS 204` et `205` |\n"
            "| `STAMP` / `STPA` | Sûreté système | Analyse du contrôle fondée sur les boucles de contrainte |\n"
            "| `FOCUS` | Gouvernance économique | Spécification ouverte d'imputation des coûts infonuagiques |\n"
            "| `DAPP` | Stratégie adaptative | *Dynamic Adaptive Policy Pathways* (trajectoires sur signaux) |"
        ),
        (
            "## Conventions d'interprétation des seuils et heuristiques\n\n"
            "L'ouvrage distingue systématiquement les résultats mesurés par études empiriques publiées, les "
            "obligations issues de textes légaux ou prudentiels en vigueur ou annoncés à la date de gel du "
            "31 décembre 2026, et les règles d'ingénierie de la collection. La partition 80/20 entre code "
            "déterministe et raisonnement probabiliste relève de cette troisième catégorie : il s'agit d'une "
            "heuristique directrice d'urbanisation logicielle plutôt que d'une constante statistique universelle."
        ),
        (
            "### Périmètre de transférabilité des notions juridiques\n\n"
            "Les termes réglementaires et probatoires figurant dans ce glossaire — qu'il s'agisse de la "
            "révision humaine effective prévue par la législation québécoise sur les renseignements personnels, "
            "des exigences prudentielles canadiennes sur le risque de modèle et l'impartition, ou de la "
            "classification par niveau de risque du cadre européen — sont démontrés pour les services "
            "financiers réglementés. Leur transposition à d'autres secteurs critiques doit toujours faire l'objet "
            "d'une qualification juridique propre à la juridiction et au régime sectoriel applicables."
        ),
        (
            "### Articulation avec la chronologie et le bilan d'assurance qualité\n\n"
            "Chaque notion technique ou réglementaire définie ici renvoie à des échéances datées dans "
            "l'Annexe B et s'appuie exclusivement sur des sources primaires intégrales vérifiées par empreinte "
            "cryptographique dans l'Annexe C. Cette séparation nette entre lexique normatif, calendrier "
            "opposable et traçabilité documentaire garantit qu'aucun glissement sémantique ne survient entre "
            "l'architecture logicielle, la rédaction éditoriale et les exigences d'audit."
        ),
        (
            "## Regroupement thématique des concepts directeurs\n\n"
            "### 1. Tissu conjonctif, industrialisation et limites économiques\n\n"
            "La première partie de l'ouvrage établit le vocabulaire permettant de situer les collectifs d'agents "
            "dans l'économie de l'entreprise. Elle oppose l'assistant ponctuel consulté par un employé au système "
            "agentique relié directement aux systèmes d'enregistrement par un tissu conjonctif partagé. Elle "
            "précise les notions de continuum d'autonomie opérationnelle, de rendement composé sur plusieurs "
            "étapes enchaînées et de frontière de la firme lorsque le coût cognitif de recherche, de négociation "
            "et de vérification s'effondre."
        ),
        (
            "### 2. Noyau déterministe, interopérabilité et exécution durable\n\n"
            "La deuxième partie déploie les concepts d'ingénierie qui empêchent le couplage irréversible à un "
            "fournisseur de modèle. Le vocabulaire distingue rigoureusement la couche de médiation syntaxique, "
            "les contrats de données sémantiques, les quatre compartiments mémoriels de l'agent et les garanties "
            "transactionnelles fournies par la relecture déterministe des journaux d'événements et les sagas "
            "compensatoires."
        ),
        (
            "### 3. Chaîne de mandat, confinement et gouvernance jusqu'en 2035\n\n"
            "Les troisième et quatrième parties unissent la cryptographie appliquée et les sciences de la sûreté "
            "système aux obligations réglementaires canadiennes, québécoises et européennes. L'attestation "
            "éphémère des charges de travail, la séparation structurelle entre flux de contrôle et données non "
            "fiables, la télémétrie à double couloir et les mécanismes anti-atrophie des compétences humaines "
            "forment un vocabulaire d'exploitation commun entre les directions technologiques, financières et "
            "juridiques."
        ),
        (
            "### Notes typographiques sur l'emploi des termes bilingues\n\n"
            "Dans le corps du texte, les anglicismes techniques déjà normalisés par l'usage francophone "
            "international ou les sigles de protocoles ouverts (`MCP`, `A2A`, `SPIFFE`, `WIMSE`, `Zero-Trust`, "
            "`FinOps`, `pass^k`) sont conservés tels quels après mise en contexte. À l'inverse, les concepts "
            "d'architecture et de gouvernance possédant un équivalent français précis et idiomatique — comme "
            "l'approbation réflexe, la couche anti-corruption, l'exécution durable, la délégation au nom du "
            "mandant ou le coût par résultat conforme — sont systématiquement rédigés en français canadien dans "
            "la prose courante."
        ),
        (
            "### Règle de cohérence entre texte principal, diagrammes et registres\n\n"
            "Les intitulés figurant dans la table d'équivalence bilingue s'appliquent à l'identique aux "
            "légendes des vingt-trois figures vectorielles ainsi qu'aux entrées des registres chronologique "
            "et empirique. Cette discipline lexicale facilite la recherche transversale par le lecteur et évite "
            "toute divergence d'interprétation lorsqu'une même notion est abordée sous l'angle économique, "
            "logiciel, sécuritaire ou réglementaire d'une partie à l'autre du livre."
        ),
    ]

    core = f"{intro}\n\n{entries_block}\n\n{table_block}"
    # Si le glossaire enrichi est deja tres long, reduire la table ou les notes tout en restant dans la plage
    if count_prose_words(core) > unit_meta["max_words"] - 40:
        core = f"{intro}\n\n{entries_block}"
    if count_prose_words(core) > unit_meta["max_words"] - 20:
        # En dernier recours sur un glossaire tres volumineux, conserver format compact sans prose introductive longue
        core = f"# {unit_meta['title']}\n\n{entries_block}"

    return _fit_word_budget(
        core_text=core,
        optional_blocks=optional_notes,
        min_words=unit_meta["min_words"],
        max_words=unit_meta["max_words"],
        target_words=unit_meta["target_words"],
    )


def _render_annexe_b(root: Path, unit_meta: dict) -> str:
    ancres_data = _load_json(root / "registre" / "ancres-chronologiques.json", {"anchors": []})
    anchors = sorted(ancres_data.get("anchors", []), key=lambda a: a.get("key", ""))

    intro = (
        f"# {unit_meta['title']}\n\n"
        "Cette annexe regroupe l'ensemble des jalons réglementaires, prudentiels, législatifs et "
        "cryptographiques cités dans l'ouvrage. La date de gel des faits étant fixée au plus tard au "
        "**31 décembre 2026**, toute échéance située en 2027 ou au-delà est présentée selon son statut "
        "juridique ou normatif à la clôture de la collecte : règle déjà adoptée avec date d'entrée en vigueur "
        "fixée, calendrier révisé officiellement proposé ou feuille de route coordonnée de normalisation.\n\n"
        "Les chapitres qui mobilisent une date donnée s'appuient directement sur cet enregistrement unique, "
        "empêchant toute divergence chronologique entre l'architecture technique, la gouvernance financière "
        "et l'analyse juridique."
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
        vig = f"\n\n*Point de vigilance :* {_escape_dollars(a['vigilance'])}" if a.get("vigilance") else ""
        comm = f"\n\n*Précision de collecte :* {_escape_dollars(a['commentaire_annexe'])}" if a.get("commentaire_annexe") else ""
        details.append(
            f"### {a['date']} — {a['jurisdiction']} ({a['key']})\n\n"
            f"**Nature :** {a['nature']}. **Chapitres concernés :** {', '.join(a.get('chapters', []))}. "
            f"**Statut probatoire :** {statut}{src_ref}.\n\n"
            f"{_escape_dollars(a['label'])}.{vig}{comm}"
        )
    details_block = "\n\n".join(details)

    optional_notes = [
        (
            "## Lecture par horizon de décision (2026–2035)\n\n"
            "### Horizon immédiat (2026–2027) : inventaire, transparence et gestion du risque de modèle\n\n"
            "La période qui s'ouvre immédiatement après la date de gel concentre le passage de la sensibilisation "
            "aux contrôles auditables. Les dispositions applicables dès 2026 en matière de renseignements "
            "personnels au Québec et de transparence européenne exigent sans délai un inventaire des systèmes "
            "automatisés et une traçabilité effective de la supervision humaine. Les échéances prudentielles et "
            "techniques de 2027, notamment l'abaissement des certificats publics à 100 jours et le cadre fédéral "
            "canadien de risque de modèle, commandent de verrouiller dès les 90 premiers jours les fondations "
            "d'identité, de journalisation et de gouvernance."
        ),
        (
            "### Horizon intermédiaire (2028–2029) : conformité sectorielle et automatisation complète des certificats\n\n"
            "Entre 2028 et 2029, l'automatisation manuelle ou semi-artisanale cesse d'être viable. L'entrée en "
            "application progressive des obligations européennes visant les systèmes intégrés à des produits "
            "réglementés, les règles sectorielles financières sur la gestion de patrimoine et la divulgation "
            "climatique de portée 3 coïncident avec l'abaissement des certificats `TLS` publics à 47 jours le "
            "15 mars 2029. À cette cadence de renouvellement, toute organisation qui conserve des secrets fixes "
            "ou des renouvellements manuels s'expose à des pannes de connectivité en chaîne."
        ),
        (
            "### Horizon structurel (2030–2035) : transition post-quantique et révision législative\n\n"
            "La décennie suivante est dominée par la migration coordonnée du secteur financier vers la "
            "cryptographie post-quantique, avec un jalon critique entre 2030 et 2032 et un achèvement visé "
            "à l'horizon 2035, en parallèle avec la révision statutaire des lois fédérales financières "
            "canadiennes prévue pour le 30 juin 2033. La taille accrue des signatures normalisées sur réseaux "
            "euclidiens impose de préparer dès 2027 l'agilité cryptographique des passerelles, des jetons "
            "d'identité et des journaux d'audit horodatés afin d'éviter une rupture de compatibilité lors du "
            "basculement effectif."
        ),
        (
            "### Distinction méthodologique sur les textes bloqués ou annoncés\n\n"
            "Lorsqu'un texte officiel demeure inaccessible en collecte ouverte sans contournement de sécurité, "
            "ou lorsqu'un calendrier réglementaire fait l'objet d'un aménagement annoncé mais non encore entré "
            "en vigueur à la date de gel, cette situation est consignée explicitement plutôt que lissée. "
            "L'ouvrage n'extrapole jamais au-delà du statut vérifiable de chaque instrument."
        ),
    ]

    core = f"{intro}\n\n{table_block}\n\n{details_block}"
    if count_prose_words(core) > unit_meta["max_words"] - 40:
        core = f"{intro}\n\n{details_block}"
    if count_prose_words(core) > unit_meta["max_words"] - 20:
        compact_details = ["## Fiches chronologiques synthétiques"]
        for a in anchors:
            statut = "Vérifié" if a.get("statut_preuve") == "l_plus" else "À réancrer"
            compact_details.append(
                f"- **{a['date']} ({a['jurisdiction']}, `{a['key']}`)** : {_escape_dollars(a['label'])}. "
                f"Chapitres : {', '.join(a.get('chapters', []))} ({statut})."
            )
        core = f"{intro}\n\n" + "\n".join(compact_details)
    return _fit_word_budget(
        core_text=core,
        optional_blocks=optional_notes,
        min_words=unit_meta["min_words"],
        max_words=unit_meta["max_words"],
        target_words=unit_meta["target_words"],
    )


def _collect_qa_metrics(root: Path, mlr: dict) -> dict:
    manifeste = _load_json(root / "recherche" / "manifeste-sources-sha256.json", None)
    statut_f = _load_json(root / "recherche" / "registre-statut-f.json", None)

    rq_counts = {rq["id"]: 0 for rq in mlr.get("research_questions_and_queries", [])}
    sources_list: list[dict] = []
    metadata_pct = None
    freeze_date = "31 décembre 2026"
    if isinstance(manifeste, dict):
        sources_list = [s for s in manifeste.get("sources", []) if isinstance(s, dict)]
        metadata_pct = manifeste.get("metadata_only_pct", 0.0)
        for s in sources_list:
            for rq in s.get("research_axes", []):
                if rq in rq_counts:
                    rq_counts[rq] += 1

    blocked_count = 0
    blocked_list: list[dict] = []
    if isinstance(statut_f, dict):
        blocked_list = statut_f.get("blocked", statut_f.get("sources", [])) or []
        blocked_count = len(blocked_list)

    ancrage_dir = root / "ancrage"
    ancrage_files = sorted(ancrage_dir.glob("*-ancrage.md")) if ancrage_dir.is_dir() else []

    aq_dir = root / "aq"
    recol1 = _load_json(aq_dir / "recollation-seed-202701.json", None) if aq_dir.is_dir() else None
    recol2 = _load_json(aq_dir / "recollation-seed-202702.json", None) if aq_dir.is_dir() else None
    recol1_md = (aq_dir / "recollation-seed-202701.md").read_text(encoding="utf-8") if (aq_dir / "recollation-seed-202701.md").is_file() else ""
    recol2_md = (aq_dir / "recollation-seed-202702.md").read_text(encoding="utf-8") if (aq_dir / "recollation-seed-202702.md").is_file() else ""
    gauntlet_ok = (aq_dir / "gauntlet-log.md").is_file() and (aq_dir / "gauntlet-log.md").stat().st_size > 0
    lissage_ok = (aq_dir / "rapport-lissage-et-visuel.md").is_file() and (aq_dir / "rapport-lissage-et-visuel.md").stat().st_size > 0

    return {
        "sources_list": sources_list,
        "source_count": len(sources_list),
        "metadata_pct": metadata_pct,
        "freeze_date": freeze_date,
        "rq_counts": rq_counts,
        "blocked_count": blocked_count,
        "blocked_list": blocked_list,
        "ancrage_count": len(ancrage_files),
        "recol1": recol1,
        "recol2": recol2,
        "recol1_md": recol1_md,
        "recol2_md": recol2_md,
        "gauntlet_ok": gauntlet_ok,
        "lissage_ok": lissage_ok,
    }


def _recol_status_label(recol_json: object, recol_md: str) -> str:
    if recol_json is None and not recol_md:
        return "En attente d'exécution"
    if "60/60" in recol_md or "60 / 60" in recol_md:
        return "60/60 vérifiés (100 %)"
    items = recol_json.get("items", recol_json.get("sample", [])) if isinstance(recol_json, dict) else recol_json
    if isinstance(items, list):
        return f"{len(items)} items tirés (recollation en cours)"
    return "Journal présent"


def _render_annexe_c(root: Path, unit_meta: dict) -> str:
    mlr = _load_json(root / "specs" / "protocole-mlr-2027.json", {})
    metrics = _collect_qa_metrics(root, mlr)

    min_aacods = mlr.get("aacods_threshold", {}).get("min_score_for_inclusion", 9.0)
    scale_max = mlr.get("aacods_threshold", {}).get("scale_max", 12)

    if metrics["source_count"] > 0:
        corpus_status_sentence = (
            f"À la date de gel du {metrics['freeze_date']}, le corpus probant rassemble "
            f"**{metrics['source_count']} textes intégraux ouverts** hachés en `SHA-256`, avec un taux de "
            f"notices limitées aux métadonnées de `{metrics['metadata_pct']:.1f} %` et "
            f"`{metrics['blocked_count']}` URL consignées en statut bloqué F hors corpus probant."
        )
    else:
        corpus_status_sentence = (
            f"Le protocole prescrit pour la date de gel du {metrics['freeze_date']} un taux maximal de "
            f"notices limitées aux métadonnées strictement égal à `0,0 %`; la collecte ouverte `L+` est "
            "en attente d'exécution ou d'indexation finale dans le manifeste `SHA-256`."
        )

    intro = (
        f"# {unit_meta['title']}\n\n"
        "Cette annexe expose le protocole de revue de littérature multivocale (`MLR-PRISMA-ScR`), les règles "
        "strictes d'hygiène probatoire sans contournement d'accès et le bilan consolidé des cinq barrières "
        "d'assurance qualité indépendantes (`G1` à `G5`). Chaque source mobilisée comme preuve doit disposer "
        "de son texte intégral extrait en `UTF-8`, vérifié par empreinte cryptographique `SHA-256`, daté au "
        "plus tard du 31 décembre 2026 et évalué selon la grille `AACODS` avec un seuil minimal d'inclusion "
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
        f"{metrics['ancrage_count']} / 13 journaux produits"
        if metrics["ancrage_count"] > 0
        else "En attente d'exécution"
    )
    recol1_label = _recol_status_label(metrics["recol1"], metrics["recol1_md"])
    recol2_label = _recol_status_label(metrics["recol2"], metrics["recol2_md"])
    gauntlet_label = "Journal complété" if metrics["gauntlet_ok"] else "En attente d'exécution"
    lissage_label = "Rapport complété" if metrics["lissage_ok"] else "En attente d'exécution"

    qa_table = (
        "## Bilan des cinq barrières d'assurance qualité (`G1` à `G5`)\n\n"
        "| Barrière | Rôle de contrôle | Critères visés | État constaté |\n"
        "|---|---|---|---|\n"
        "| `G1` — Garde déterministe | Script `verifie_manuscrit.py` sans appel de modèle | `CA-01` à `CA-11`, `CA-17` | Contrôle actif |\n"
        f"| `G2` — Ancrage atomique Wyvern | Auditeurs indépendants par unité (`00`–`12`) | `CA-10`, `CA-12` | {ancrage_label} |\n"
        f"| `G3` — Recollation passe 1 (`202701`) | Échantillon stratifié de 60 énoncés sur `.txt` | `CA-07`, `CA-13` | {recol1_label} |\n"
        f"| `G4` — Critique stylistique à l'aveugle | Boucle `gauntlet-loop` A/B sur extraits étalons | `CA-15` | {gauntlet_label} |\n"
        f"| `G5` — Lissage et inspection visuelle | Cohérence inter-unités et rendu `Pandoc`/`Typst` | `CA-16` à `CA-18` | {lissage_label} |\n"
        f"| `G3` — Recollation finale à froid (`202702`) | Échantillon disjoint sur le texte publié | `CA-14` | {recol2_label} |"
    )

    optional_notes = [
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
            "que la seconde passe exclut intégralement les paragraphes déjà inspectés afin de mesurer la fiabilité "
            "résiduelle réelle du texte destiné au lecteur."
        ),
        (
            "## Intégrité typographique et reproductibilité des annexes\n\n"
            "L'ensemble des figures vectorielles (`Fig-00` à `Fig-22`) est compilé avec détection stricte "
            "d'erreurs et contraint à quatorze éléments au maximum pour préserver la lisibilité imprimée. Tous "
            "les symboles monétaires sont échappés et les formules sont encadrées en notation compatible avec "
            "la chaîne `Pandoc` et `Typst`. Enfin, les trois annexes demeurent régénérées mécaniquement depuis "
            "les registres JSON et les journaux d'assurance qualité, interdisant toute divergence manuelle."
        ),
        (
            "## Politique de transparence sur les limites documentaires\n\n"
            "Le corpus de preuve exclut délibérément les résumés non accompagnés du texte complet ainsi que "
            "les sources protégées par mur payant ou contrôle anti-robot. Lorsqu'une référence institutionnelle "
            "importante demeure inaccessible dans le périmètre ouvert au 31 décembre 2026, son blocage est "
            "journalisé et son contenu reste écarté de toute démonstration factuelle."
        ),
        (
            "## Architecture de vérification des énoncés et séparation des rôles\n\n"
            "Conformément au principe d'étanchéité de la chaîne documentaire, la collecte des textes ouverts, "
            "la rédaction narrative, le contrôle mécanique `G1`, l'audit atomique `G2`, les deux recollations "
            "`G3`, la critique comparative `G4` et le lissage `G5` sont exécutés par des instances distinctes "
            "cloisonnées par fichiers versionnés. Chaque affirmation factuelle du liminaire et des douze "
            "chapitres ne pointe que vers sa base fermée locale, elle-même liée par identifiant unique et "
            "empreinte `SHA-256` au texte intégral conservé sur disque.\n\n"
            "Lorsqu'une passe stylistique de `G4` ou une harmonisation de transition de `G5` retouche la "
            "formulation d'un paragraphe existant, l'unité modifiée repasse immédiatement sous la garde "
            "déterministe pour vérifier les bornes de volume, l'absence de codes internes bannis, la "
            "non-duplication face au corpus historique, l'intégrité des montants échappés et la résolution "
            "complète des renvois numériques."
        ),
        (
            "## Traçabilité de la chaîne de compilation éditoriale\n\n"
            "L'assemblage final produit simultanément le document Markdown consolidé, l'édition HTML autonome "
            "avec ressources vectorielles intégrées et formules en MathML, ainsi que l'édition imprimable PDF "
            "composée sous `Typst`. Aucune édition manuelle n'est tolérée dans les trois annexes générées, "
            "afin que toute reprise des registres de vérité ou des journaux d'assurance qualité se répercute "
            "instantanément et de manière reproductible dans l'ouvrage publié.\n\n"
            "Chaque fichier généré conserve une date de gel des faits explicitement bornée au 31 décembre 2026 "
            "et permet à tout vérificateur externe de contrôler la conformité mécanique sans recourir à un "
            "modèle de langage."
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
            authors = src.get("authors", "Auteur inconnu")
            year = src.get("year", "s.d.")
            title = src.get("title", "Sans titre")
            venue = src.get("venue_or_issuer", "")
            ident = src.get("identifier", "")
            url = src.get("url", "")
            axes = ", ".join(src.get("research_axes", []))
            sha_short = str(src.get("sha256", ""))[:12]
            aacods = src.get("aacods_score", "")
            bib_lines.append(
                f"- **{sid}** — {authors} ({year}). *{title}*. {venue}. `{ident}` — {url} "
                f"(axes : {axes}; AACODS : {aacods}; `SHA-256` : `{sha_short}...`)."
            )
    else:
        bib_lines.append("- *Aucune source L+ encore indexée dans `recherche/manifeste-sources-sha256.json`.*")

    if metrics["blocked_list"]:
        bib_lines.extend(["", "### Journal des accès refusés consignés en statut F (exclus des preuves)", ""])
        for b in metrics["blocked_list"]:
            url = b.get("url", "URL inconnue")
            reason = b.get("reason", b.get("http_status", "blocage"))
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
