#!/usr/bin/env python3
"""Verification mecanique de coherence du dossier amont `7 - Livre 2027/specs/`."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import DEFAULT_FREEZE_DATE, format_french_date, french_date_regex, parse_iso_date


def _parse_fr_int(raw: str) -> int | None:
    digits = re.sub(r"[\s\u00a0\u202f]+", "", raw.strip())
    return int(digits) if digits.isdigit() else None


def _norm_tokens(text: str) -> set[str]:
    cleaned = re.sub(r"[`*_«»\"'’():;,.!?/\\—–-]+", " ", text.lower())
    return {tok for tok in cleaned.split() if len(tok) >= 4}


def _check_freeze_date_coherence(
    book_dir: Path,
    mlr: dict,
    mlr_raw: str,
    manifest_raw: str,
    prd_text: str,
    charte_text: str,
    toc_text: str,
    ancres_raw: str,
    faits_raw: str,
    glossaire_raw: str,
    ancres: dict,
    faits: dict,
    glossaire: dict,
    statut_f: dict | None,
    statut_f_raw: str,
) -> list[str]:
    errors: list[str] = []
    freeze_date = mlr.get("freeze_date")
    if not isinstance(freeze_date, str) or freeze_date != DEFAULT_FREEZE_DATE:
        errors.append(
            f"Date de gel freeze_date attendue = {DEFAULT_FREEZE_DATE} dans protocole-mlr-2027.json, trouve = {freeze_date!r}"
        )
    target_freeze = freeze_date if isinstance(freeze_date, str) and parse_iso_date(freeze_date) else DEFAULT_FREEZE_DATE

    window_end = mlr["time_window"]["primary"].split("/")[-1].strip()
    if parse_iso_date(window_end) is None or window_end > target_freeze:
        errors.append(f"Fenetre MLR posterieure a la date de gel ({target_freeze}) : {window_end}")

    freeze_fr = format_french_date(DEFAULT_FREEZE_DATE)
    freeze_re = french_date_regex(DEFAULT_FREEZE_DATE)
    for label, text in (("prd.md", prd_text), ("charte-editoriale.md", charte_text)):
        if not freeze_re.search(text):
            errors.append(f"Date de gel officielle ({freeze_fr}) absente de {label}")

    stale_re = re.compile(r"(?:2026-12-31|31\s+d[eé]cembre\s+2026)", re.IGNORECASE)
    for label, raw in (
        ("protocole-mlr-2027.json", mlr_raw),
        ("manifest.json", manifest_raw),
        ("prd.md", prd_text),
        ("charte-editoriale.md", charte_text),
        ("toc.md", toc_text),
        ("ancres-chronologiques.json", ancres_raw),
        ("faits-empiriques.json", faits_raw),
        ("glossaire-termes.json", glossaire_raw),
        ("registre-statut-f.json", statut_f_raw),
    ):
        if raw and stale_re.search(raw):
            errors.append(f"Ancienne date de gel (2026-12-31 / 31 decembre 2026) encore presente dans {label}")

    for label, payload in (
        ("ancres-chronologiques.json", ancres),
        ("faits-empiriques.json", faits),
        ("glossaire-termes.json", glossaire),
        ("registre-statut-f.json", statut_f),
    ):
        if isinstance(payload, dict):
            fd = payload.get("freeze_date") or payload.get("date_gel")
            if fd is not None and fd != DEFAULT_FREEZE_DATE:
                errors.append(f"freeze_date divergent dans {label} : {fd!r} != {DEFAULT_FREEZE_DATE}")

    return errors


def _validate_toc_concordance(
    toc_text: str,
    units: list[dict],
    wb: dict,
    declared_figs: dict[str, dict],
) -> list[str]:
    errors: list[str] = []
    narrative_units = [u for u in units if u["kind"] in {"frontmatter", "chapter"}]
    unit_by_id = {u["id"]: u for u in units}

    # 1. Vue synoptique : budgets & figures par unite + Total
    synoptic_match = re.search(
        r"##\s+Vue synoptique des volumes\s+(.*?)(?=\n---|\n##\s+)",
        toc_text,
        re.DOTALL,
    )
    if not synoptic_match:
        errors.append("Section 'Vue synoptique des volumes' absente de toc.md")
    else:
        seen_synoptic_ids: set[str] = set()
        found_total = False
        for line in synoptic_match.group(1).splitlines():
            stripped = line.strip()
            if not stripped.startswith("|") or stripped.startswith("|---") or stripped.startswith("| Unité"):
                continue
            cols = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cols) < 5:
                continue
            key_cell, _title_cell, target_cell, range_cell, figs_cell = cols[:5]
            key_clean = key_cell.strip("`").strip()
            uid: str | None = None
            if key_clean == "00":
                uid = "00-liminaire"
            elif re.match(r"^Ch\.\s*(\d{2})$", key_clean):
                uid = f"ch{re.match(r'^Ch\.\s*(\d{2})$', key_clean).group(1)}"
            elif re.match(r"^Annexe\s+([ABC])$", key_clean):
                uid = f"annexe-{re.match(r'^Annexe\s+([ABC])$', key_clean).group(1).lower()}"
            elif key_clean == "**Total**":
                found_total = True
                tot_val = _parse_fr_int(target_cell.strip("*"))
                if tot_val != wb["total_target"]:
                    errors.append(f"Total toc.md ({tot_val}) != manifest total_target ({wb['total_target']})")
                m_rng = re.match(r"\*\*([\d\s\u00a0\u202f]+)\s*[–-]\s*([\d\s\u00a0\u202f]+)\*\*", range_cell)
                if m_rng:
                    rmin, rmax = _parse_fr_int(m_rng.group(1)), _parse_fr_int(m_rng.group(2))
                    if (rmin, rmax) != (wb["total_min"], wb["total_max"]):
                        errors.append(
                            f"Plage totale toc.md ({rmin}, {rmax}) != manifest ({wb['total_min']}, {wb['total_max']})"
                        )
                continue

            if uid and uid in unit_by_id:
                seen_synoptic_ids.add(uid)
                u = unit_by_id[uid]
                t_val = _parse_fr_int(target_cell)
                if t_val != u["target_words"]:
                    errors.append(
                        f"Budget Vue synoptique {uid} ({t_val}) != manifest ({u['target_words']})"
                    )
                m_rng = re.match(r"([\d\s\u00a0\u202f]+)\s*[–-]\s*([\d\s\u00a0\u202f]+)", range_cell)
                if m_rng:
                    rmin, rmax = _parse_fr_int(m_rng.group(1)), _parse_fr_int(m_rng.group(2))
                    if (rmin, rmax) != (u["min_words"], u["max_words"]):
                        errors.append(
                            f"Plage Vue synoptique {uid} ({rmin}, {rmax}) != manifest ({u['min_words']}, {u['max_words']})"
                        )
                if u["kind"] in {"frontmatter", "chapter"}:
                    syn_figs = re.findall(r"Fig-\d{2}", figs_cell)
                    if syn_figs != u.get("figures", []):
                        errors.append(
                            f"Figures Vue synoptique {uid} ({syn_figs}) != manifest ({u.get('figures', [])})"
                        )

        missing_syn = [u["id"] for u in units if u["id"] not in seen_synoptic_ids]
        if missing_syn:
            errors.append(f"Unites absentes de Vue synoptique dans toc.md : {missing_syn}")
        if not found_total:
            errors.append("Ligne **Total** absente de Vue synoptique dans toc.md")

    # 2. Detail contractuel : 13 unites, 13 QD, 54 sous-sections, 13 Proprietaire exclusif, 23 figures ordonnees
    unit_heading_re = re.compile(
        r"^(?:###\s+`00`\s+—\s+Liminaire\s+—\s+|####\s+Chapitre\s+(\d{2})\s+—\s+)(.+?)\s+\(([\d\s\u00a0\u202f]+)\s+mots\)\s*$",
        re.MULTILINE,
    )
    matches = list(unit_heading_re.finditer(toc_text))
    found_unit_blocks: dict[str, tuple[str, int, str]] = {}
    for idx, m in enumerate(matches):
        ch_num = m.group(1)
        uid = "00-liminaire" if ch_num is None else f"ch{ch_num}"
        short_title = m.group(2).strip()
        budget = _parse_fr_int(m.group(3)) or 0
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(toc_text)
        found_unit_blocks[uid] = (short_title, budget, toc_text[start:end])

    total_qd = 0
    total_owners = 0
    all_subs: list[str] = []
    detail_fig_order: list[str] = []

    for nu in narrative_units:
        uid = nu["id"]
        if uid not in found_unit_blocks:
            errors.append(f"Bloc detaille de {uid} absent de toc.md")
            continue
        _short_title, budget, block = found_unit_blocks[uid]
        if budget != nu["target_words"]:
            errors.append(f"Budget detaille toc.md de {uid} ({budget}) != manifest ({nu['target_words']})")

        qd_matches = re.findall(r"(?m)^-\s+\*\*Question directrice\*\*\s*:\s*\S+", block)
        if not qd_matches:
            errors.append(f"Question directrice absente pour {uid} dans toc.md")
        total_qd += len(qd_matches)

        owner_matches = re.findall(r"(?m)^-\s+\*\*Propriétaire exclusif\*\*\s*:\s*\S+", block)
        if not owner_matches:
            errors.append(f"Proprietaire exclusif absent pour {uid} dans toc.md")
        total_owners += len(owner_matches)

        prefix = "0" if uid == "00-liminaire" else str(int(uid[2:]))
        unit_subs = re.findall(r"(?m)^-\s+\*\*(\d+\.\d+)\*\*\s+\S+", block)
        expected_subs = [f"{prefix}.{i}" for i in range(1, (7 if uid == "00-liminaire" else 5))]
        if unit_subs != expected_subs:
            errors.append(f"Sous-sections {uid} dans toc.md ({unit_subs}) != attendu ({expected_subs})")
        all_subs.extend(unit_subs)

        fig_line_m = re.search(r"(?m)^-\s+\*\*Figures?\*\*\s*:\s*(.+)$", block)
        if not fig_line_m:
            errors.append(f"Ligne Figures absente pour {uid} dans toc.md")
        else:
            fig_line = fig_line_m.group(1)
            unit_detail_figs = re.findall(r"`(Fig-\d{2})`", fig_line)
            if unit_detail_figs != nu.get("figures", []):
                errors.append(
                    f"Figures detaillees {uid} dans toc.md ({unit_detail_figs}) != manifest ({nu.get('figures', [])})"
                )
            detail_fig_order.extend(unit_detail_figs)

            for fid, desc in re.findall(r"`(Fig-\d{2})`\s*\((.+?)\)(?=;|\.\s*$|\s*$)", fig_line):
                if fid in declared_figs:
                    man_tokens = _norm_tokens(declared_figs[fid]["title"])
                    toc_tokens = _norm_tokens(desc)
                    overlap = len(man_tokens & toc_tokens)
                    if overlap < 2 and len(man_tokens) >= 3:
                        errors.append(
                            f"Titre {fid} divergent entre manifest.json et toc.md : '{declared_figs[fid]['title']}' vs '{desc}'"
                        )

    if total_qd != 13:
        errors.append(f"Nombre de Questions directrices dans toc.md = {total_qd}, attendu = 13")
    if total_owners != 13:
        errors.append(f"Nombre de sections Proprietaire exclusif dans toc.md = {total_owners}, attendu = 13")
    if len(all_subs) != 54:
        errors.append(f"Nombre total de sous-sections dans toc.md = {len(all_subs)}, attendu = 54")
    expected_figs = [f"Fig-{i:02d}" for i in range(23)]
    if detail_fig_order != expected_figs:
        errors.append(
            f"Ordre global des figures dans toc.md ({detail_fig_order}) != Fig-00..Fig-22"
        )

    return errors


def validate_specs(book_dir: Path) -> list[str]:
    errors: list[str] = []
    specs_dir = book_dir / "specs"
    reg_dir = book_dir / "registre"

    required_files = [
        book_dir / "README.md",
        book_dir / "sources-locales" / "README.md",
        specs_dir / "prd.md",
        specs_dir / "toc.md",
        specs_dir / "charte-editoriale.md",
        specs_dir / "manifest.json",
        specs_dir / "protocole-mlr-2027.json",
        specs_dir / "contrat-aq.md",
        specs_dir / "plan-production-aq.md",
        reg_dir / "ancres-chronologiques.json",
        reg_dir / "faits-empiriques.json",
        reg_dir / "glossaire-termes.json",
    ]
    for path in required_files:
        if not path.is_file():
            errors.append(f"Fichier requis manquant : {path}")
    if errors:
        return errors

    try:
        manifest_raw = (specs_dir / "manifest.json").read_text(encoding="utf-8")
        mlr_raw = (specs_dir / "protocole-mlr-2027.json").read_text(encoding="utf-8")
        ancres_raw = (reg_dir / "ancres-chronologiques.json").read_text(encoding="utf-8")
        faits_raw = (reg_dir / "faits-empiriques.json").read_text(encoding="utf-8")
        glossaire_raw = (reg_dir / "glossaire-termes.json").read_text(encoding="utf-8")
        manifest = json.loads(manifest_raw)
        mlr = json.loads(mlr_raw)
        ancres = json.loads(ancres_raw)
        faits = json.loads(faits_raw)
        glossaire = json.loads(glossaire_raw)
    except json.JSONDecodeError as exc:
        return [f"JSON invalide : {exc}"]

    statut_f_path = book_dir / "recherche" / "registre-statut-f.json"
    statut_f_raw = ""
    statut_f: dict | None = None
    if statut_f_path.is_file():
        statut_f_raw = statut_f_path.read_text(encoding="utf-8")
        try:
            loaded_sf = json.loads(statut_f_raw)
            if isinstance(loaded_sf, dict):
                statut_f = loaded_sf
            else:
                errors.append("registre-statut-f.json doit contenir un objet JSON")
        except json.JSONDecodeError as exc:
            errors.append(f"registre-statut-f.json invalide : {exc}")
    elif (book_dir / "recherche").is_dir():
        errors.append(f"Fichier requis manquant : {statut_f_path}")

    # 0. Credit d'auteur fixe par l'auteur, identique dans manifest.json et prd.md
    credit = manifest.get("author_credit", "").strip()
    if not credit:
        errors.append("author_credit absent de manifest.json")
    elif credit not in (specs_dir / "prd.md").read_text(encoding="utf-8"):
        errors.append(f"author_credit non reproduit a l'identique dans prd.md : {credit}")

    # 1. Validation des budgets de mots et des bornes +-8 %
    wb = manifest["word_budget"]
    tol = wb["tolerance_pct"] / 100.0
    units = manifest["units"]
    unit_ids = [u["id"] for u in units]
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("Identifiants d'unites dupliques dans manifest.json")

    sum_total = sum(u["target_words"] for u in units)
    sum_narrative = sum(u["target_words"] for u in units if u["kind"] in {"frontmatter", "chapter"})
    sum_annexes = sum(u["target_words"] for u in units if u["kind"] == "annex")

    if sum_total != wb["total_target"]:
        errors.append(f"Somme des unites ({sum_total}) != total_target ({wb['total_target']})")
    if sum_narrative != wb["narrative_target"]:
        errors.append(f"Somme narrative ({sum_narrative}) != narrative_target ({wb['narrative_target']})")
    if sum_annexes != wb["annexes_target"]:
        errors.append(f"Somme annexes ({sum_annexes}) != annexes_target ({wb['annexes_target']})")

    exp_tot_min = math.ceil(wb["total_target"] * (1.0 - tol))
    exp_tot_max = math.floor(wb["total_target"] * (1.0 + tol))
    if wb["total_min"] != exp_tot_min or wb["total_max"] != exp_tot_max:
        errors.append(
            f"Bornes globales invalides : ({wb['total_min']}, {wb['total_max']}) "
            f"attendu ({exp_tot_min}, {exp_tot_max})"
        )

    for u in units:
        exp_min = math.ceil(u["target_words"] * (1.0 - tol))
        exp_max = math.floor(u["target_words"] * (1.0 + tol))
        if u["min_words"] != exp_min or u["max_words"] != exp_max:
            errors.append(
                f"Bornes invalides pour {u['id']} : ({u['min_words']}, {u['max_words']}) "
                f"attendu ({exp_min}, {exp_max})"
            )

    # 2. Validation des unites narratives (liminaire + 12 chapitres), concepts possedes et figures
    chapters = [u for u in units if u["kind"] == "chapter"]
    narrative_units = [u for u in units if u["kind"] in {"frontmatter", "chapter"}]
    if len(chapters) != 12:
        errors.append(f"Nombre de chapitres attendu = 12, trouve = {len(chapters)}")
    if len(narrative_units) != 13:
        errors.append(f"Nombre d'unites narratives attendu = 13, trouve = {len(narrative_units)}")

    owned_all: list[str] = []
    for nu in narrative_units:
        owned = nu.get("owned_concepts", [])
        if not owned:
            errors.append(f"Unite narrative {nu['id']} sans owned_concepts")
        owned_all.extend(owned)
    if len(owned_all) != len(set(owned_all)):
        errors.append("Collision dans owned_concepts entre plusieurs unites narratives")

    expected_fig_ids = [f"Fig-{i:02d}" for i in range(23)]
    manifest_fig_ids = [f["id"] for f in manifest["figures"]]
    declared_figs = {f["id"]: f for f in manifest["figures"]}
    if len(declared_figs) != 23 or manifest_fig_ids != expected_fig_ids:
        errors.append(
            f"Figures attendues exactement dans l'ordre Fig-00..Fig-22 (23), trouve = {manifest_fig_ids}"
        )

    assigned_figs = [fid for u in units for fid in u.get("figures", [])]
    if sorted(assigned_figs) != sorted(declared_figs.keys()):
        errors.append("Desaccord entre les figures assignees aux unites et la table figures de manifest.json")
    elif assigned_figs != expected_fig_ids:
        errors.append(
            f"Ordre des figures assignees aux unites divergent de Fig-00..Fig-22 : {assigned_figs}"
        )
    for fid, fmeta in declared_figs.items():
        if not str(fmeta.get("title", "")).strip():
            errors.append(f"Titre manquant pour {fid} dans manifest.json")
        if fmeta.get("engine") not in {"puml", "mmd"}:
            errors.append(f"Moteur invalide pour {fid} dans manifest.json : {fmeta.get('engine')!r}")
        unit_obj = next((u for u in units if u["id"] == fmeta["unit"]), None)
        if unit_obj is None or fid not in unit_obj.get("figures", []):
            errors.append(f"Figure {fid} mal rattachee a l'unite {fmeta['unit']}")

    # 3. Validation des regex interdites et de l'existence du corpus interne
    for pattern in manifest["forbidden_prose_regexes"]:
        try:
            re.compile(pattern)
        except re.error as exc:
            errors.append(f"Regex interdite invalide `{pattern}` : {exc}")

    for rel_path in manifest["internal_corpus_paths"] + manifest["stylistic_benchmarks_for_gauntlet"]:
        resolved = (book_dir / rel_path).resolve()
        if not resolved.is_file():
            errors.append(f"Chemin de corpus interne introuvable : {rel_path} -> {resolved}")

    for rel_path in manifest.get("stylistic_benchmark_sections", {}):
        if rel_path not in manifest["stylistic_benchmarks_for_gauntlet"]:
            errors.append(f"Section etalon hors des etalons declares : {rel_path}")

    # 4. Validation du protocole MLR et des axes RQ1..RQ6
    rq_ids = {rq["id"] for rq in mlr["research_questions_and_queries"]}
    if rq_ids != {"RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "RQ6"}:
        errors.append(f"Axes RQ attendus RQ1..RQ6, trouves : {sorted(rq_ids)}")
    if mlr["strict_access_policy"]["max_metadata_only_pct_in_included_corpus"] != 0.0:
        errors.append("Le plafond METADATA_ONLY du protocole MLR doit etre strictement 0.0 %")

    prd_text = (specs_dir / "prd.md").read_text(encoding="utf-8")
    charte_text = (specs_dir / "charte-editoriale.md").read_text(encoding="utf-8")
    aq_text = (specs_dir / "contrat-aq.md").read_text(encoding="utf-8")
    toc_text = (specs_dir / "toc.md").read_text(encoding="utf-8")

    errors.extend(
        _check_freeze_date_coherence(
            book_dir=book_dir,
            mlr=mlr,
            mlr_raw=mlr_raw,
            manifest_raw=manifest_raw,
            prd_text=prd_text,
            charte_text=charte_text,
            toc_text=toc_text,
            ancres_raw=ancres_raw,
            faits_raw=faits_raw,
            glossaire_raw=glossaire_raw,
            ancres=ancres,
            faits=faits,
            glossaire=glossaire,
            statut_f=statut_f,
            statut_f_raw=statut_f_raw,
        )
    )

    gitignore_path = book_dir / ".gitignore"
    gitignore = gitignore_path.read_text(encoding="utf-8") if gitignore_path.is_file() else ""
    if "sources-locales/*" not in gitignore or "!sources-locales/README.md" not in gitignore:
        errors.append(".gitignore doit exclure sources-locales/* (sauf README.md) : copies sous droit d'auteur")

    for nu in narrative_units:
        if not nu.get("research_axes"):
            errors.append(f"Unite narrative {nu['id']} sans research_axes")
        for rq in nu.get("research_axes", []):
            if rq not in rq_ids:
                errors.append(f"Axe inconnu {rq} dans {nu['id']}")

    # 5. Validation des registres, du contrat du Liminaire, de toc.md et des criteres CA-01..CA-18
    chapter_id_set = {ch["id"] for ch in chapters}
    narrative_id_set = {nu["id"] for nu in narrative_units}
    for anchor in ancres["anchors"]:
        for ch_ref in anchor["chapters"]:
            if ch_ref not in chapter_id_set:
                errors.append(f"Ancre {anchor['key']} pointe vers un chapitre inconnu : {ch_ref}")
    for fact in faits["facts"]:
        if fact["owner_chapter"] not in chapter_id_set:
            errors.append(f"Fait {fact['id']} pointe vers un chapitre inconnu : {fact['owner_chapter']}")
    for entry in [*faits["facts"], *ancres["anchors"]]:
        if entry.get("statut_preuve") not in {"a_reancrer", "l_plus"}:
            errors.append(f"Entree de registre sans statut_preuve valide : {entry.get('id', entry.get('key'))}")

    terms = glossaire.get("terms", [])
    if len(terms) < 12:
        errors.append("Glossaire initial trop court (< 12 termes)")
    seen_terms_fr: set[str] = set()
    for term in terms:
        fr_val = str(term.get("fr", "")).strip()
        en_val = str(term.get("en", "")).strip()
        def_val = str(term.get("definition", "")).strip()
        owner = term.get("chapitre_proprietaire")
        if not fr_val or not en_val or not def_val:
            errors.append(f"Entree incomplete dans glossaire-termes.json : {fr_val or '<vide>'}")
        if owner not in narrative_id_set:
            errors.append(f"Terme '{fr_val}' avec chapitre_proprietaire inconnu : {owner!r}")
        low_fr = fr_val.lower()
        if low_fr in seen_terms_fr:
            errors.append(f"Terme duplique dans glossaire-termes.json : {fr_val}")
        seen_terms_fr.add(low_fr)

    if statut_f is not None:
        blocked_entries = statut_f.get("blocked", statut_f.get("blocked_sources"))
        if not isinstance(blocked_entries, list):
            errors.append("registre-statut-f.json doit contenir une liste 'blocked'")
        else:
            for idx, entry in enumerate(blocked_entries):
                if not isinstance(entry, dict):
                    errors.append(f"Entree statut-F #{idx} invalide")
                    continue
                if entry.get("status") != "F":
                    errors.append(f"Entree statut-F sans status=='F' : {entry.get('url')}")
                if entry.get("included_in_evidence") is not False:
                    errors.append(f"Entree statut-F doit avoir included_in_evidence==False : {entry.get('url')}")
                if not str(entry.get("url", "")).strip():
                    errors.append(f"Entree statut-F #{idx} sans url")
                if not str(entry.get("reason") or entry.get("block_reason") or "").strip():
                    errors.append(f"Entree statut-F sans motif (reason/block_reason) : {entry.get('url')}")

    for sub in ("**0.1**", "**0.2**", "**0.3**", "**0.4**", "**0.5**", "**0.6**"):
        if sub not in toc_text:
            errors.append(f"Sous-section du Liminaire {sub} absente de toc.md")

    # Concordance des intitules manifest.json <-> toc.md (partie apres le premier tiret cadratin)
    for u in units:
        short_title = u["title"].split(" — ", 1)[-1]
        if short_title not in toc_text:
            errors.append(f"Intitule de {u['id']} absent de toc.md : {short_title}")

    errors.extend(_validate_toc_concordance(toc_text, units, wb, declared_figs))

    # Les intitules de toc.md sont recopies dans le manuscrit : aucun `$` non echappe (CA-06)
    for lineno, line in enumerate(toc_text.splitlines(), start=1):
        if re.search(r"(?<!\\)\$", line):
            errors.append(f"Symbole $ non echappe dans toc.md (ligne {lineno})")

    for idx in range(1, 8):
        ao_id = f"AO-{idx:02d}"
        if ao_id not in prd_text:
            errors.append(f"Anti-objectif {ao_id} absent de prd.md")

    for idx in range(1, 19):
        ca_id = f"CA-{idx:02d}"
        if ca_id not in prd_text:
            errors.append(f"Critere {ca_id} absent de prd.md")
    for idx in range(0, 23):
        fig_id = f"Fig-{idx:02d}"
        if fig_id not in toc_text:
            errors.append(f"Figure {fig_id} absente de toc.md")
    for gate in ("G1", "G2", "G3", "G4", "G5"):
        if gate not in aq_text:
            errors.append(f"Barriere {gate} absente de contrat-aq.md")

    return errors


def main() -> int:
    book_dir = Path(__file__).resolve().parent.parent
    errors = validate_specs(book_dir)
    if errors:
        print("ECHEC de verification des specifications amont :", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(
        "OK : Specifications amont valides (v1.3 : 16 unites = 74 000 mots, Liminaire 0.1-0.6 + 12 chapitres, "
        "23 figures Fig-00..Fig-22, RQ1-RQ6, AO-01..AO-07, CA-01..CA-18, intitules concordants, "
        "registres avec statut de preuve et chemins internes verifies)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
