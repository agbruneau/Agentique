#!/usr/bin/env python3
"""Echantillonnage stratifie deterministe pour la barriere G3 (echantillon_aq.py)."""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import ABBREV_DOT_RE, is_markdown_table_block, split_sentences
from verifie_manuscrit import (  # noqa: E402
    _CITATION_REF_RE,
    _INLINE_CODE_RE,
    _MD_IMAGE_RE,
    _MD_LINK_RE,
    _mask_comments_and_biblio,
    _mask_fenced_code_preserving_lines,
    _parse_sources_md,
    _strip_yaml_and_preserve_lines,
    _unit_sources_filename,
)

CATEGORY_QUOTAS = {
    "empirique": 25,
    "juridique": 20,
    "prospectif_technique": 15,
}

_ABBREV_DOT_RE = ABBREV_DOT_RE
_DECIMAL_DOT_RE = re.compile(r"(?<=\d)\.(?=\d)")

_EMPIRIQUE_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"%",
        r"(?<![A-Za-zÀ-ÿ])[gm]\s*\\?\$",
        r"\bempiriqu",
        r"\bmesur",
        r"\bétude",
        r"\bessais?\b",
        r"\brandomis",
        r"\bbancs?\b",
        r"\bcapex\b",
        r"\blusser\b",
        r"\bpass(?:\^k|ᵏ)(?!\w)",
        r"\bmast\b",
        r"\bmap\b",
        r"\bcamel\b",
        r"\bagentdojo\b",
        r"\bstanford\s+hai\b",
        r"\bstatistique\s+canada\b",
        r"\bnoy\b",
        r"\bcui\b",
        r"\bdell'acqua\b",
        r"\bgenewein\b",
        r"\bkim\s+et\s+al\b",
        r"\bcemri\b",
        r"\btaux\b",
        r"\bcoût",
        r"\bproductiv",
        r"\boctets?\b",
        r"\bmédiane",
        r"\benveloppe",
        r"\babandon",
        r"\b40\s*%",
        r"\btrace",
        r"\bdépense",
        r"\bfinops\b",
        r"\bfocus\b",
    )
)

_JURIDIQUE_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bloi\s+25\b",
        r"\bbsif\b",
        r"\bosfi\b",
        r"\be-23\b",
        r"\bb-10\b",
        r"\bb-15\b",
        r"\bamf\b",
        r"\bocri\b",
        r"\bacvm\b",
        r"\beu\s+ai\s+act\b",
        r"\bai\s+act\b",
        r"\bannexe\s+iii\b",
        r"\bannexe\s+i\b",
        r"\barticle\s+50\b",
        r"\b12\.1\b",
        r"\brgpd\b",
        r"\biso(?:/iec)?\s*42001\b",
        r"\bdigital\s+omnibus\b",
        r"\bjuridiqu",
        r"\br[eè]glement",
        r"\bprudentiel",
        r"\blégislat",
        r"\bloi\b",
        r"\bmandat",
        r"\bmandant",
        r"\bimputabilit",
        r"\bsanction",
        r"\brétrofacturation",
        r"\bbanque\s+ouverte\b",
        r"\bpatrimoine",
        r"\bassurance",
        r"\bjuridiction",
        r"\bconformit",
        r"\brévision\s+humaine\b",
        r"\bstatutaire",
        r"\bacte\b",
    )
)

_PROSPECTIF_TECH_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bprospecti",
        r"\btechniqu",
        r"\bpost-quantique",
        r"\bpqc\b",
        r"\bml-dsa\b",
        r"\bslh-dsa\b",
        r"\bnist\b",
        r"\bfips\s+204\b",
        r"\bir\s+8547\b",
        r"\bpki\b",
        r"\btls\b",
        r"\b100\s+jours\b",
        r"\b47\s+jours\b",
        r"\bsc-081v3\b",
        r"\bietf\b",
        r"\brfc\b",
        r"\bwimse\b",
        r"\bspiffe\b",
        r"\boauth\b",
        r"\bdpop\b",
        r"\bciba\b",
        r"\bfido2\b",
        r"\bjcs\b",
        r"\bmcp\b",
        r"\ba2a\b",
        r"\bcloudevents\b",
        r"\bopentelemetry\b",
        r"\bstamp\b",
        r"\bstpa\b",
        r"\bcoala\b",
        r"\bmicrovm\b",
        r"\bwasi\b",
        r"\bsaga\b",
        r"\bidempotence",
        r"\bdapp\b",
        r"\bhaasnoot\b",
        r"\btomašev",
        r"\bcoase\b",
        r"\b2028\b",
        r"\b2029\b",
        r"\b2030\b",
        r"\b2032\b",
        r"\b2035\b",
        r"\bfeuille\s+de\s+route\b",
        r"\bscénari",
        r"\bprotocol",
        r"\bharnais\b",
        r"\btopologie",
    )
)

_UNIT_CATEGORY_PRIOR = {
    "00-liminaire": "prospectif_technique",
    "ch01": "empirique",
    "ch02": "empirique",
    "ch03": "empirique",
    "ch04": "prospectif_technique",
    "ch05": "prospectif_technique",
    "ch06": "empirique",
    "ch07": "prospectif_technique",
    "ch08": "empirique",
    "ch09": "empirique",
    "ch10": "juridique",
    "ch11": "juridique",
    "ch12": "prospectif_technique",
}

_VIGILANCE_MATCHERS = (
    ("vig_amf_2027", lambda s: "amf" in s and ("2027" in s or "mai" in s or "ligne directrice" in s or "bloqué" in s)),
    ("vig_abandon_40", lambda s: "40 %" in s and ("abandon" in s or "2027" in s or "analyste" in s)),
    ("vig_marche_dispersion", lambda s: ("marché" in s or "périmètre" in s) and any(k in s for k in ("dispersion", "15,5", "7,8", "17,3", "46,0"))),
    ("vig_annexe_iii", lambda s: "annexe iii" in s and ("ai act" in s or "2027" in s or "décembre" in s)),
    ("vig_retrofacturation", lambda s: "rétrofacturation" in s or ("commission" in s and "2028" in s)),
)


def _classify_claim(text: str, unit_id: str) -> str:
    scores = {
        "empirique": sum(1 for pat in _EMPIRIQUE_PATTERNS if pat.search(text)),
        "juridique": sum(1 for pat in _JURIDIQUE_PATTERNS if pat.search(text)),
        "prospectif_technique": sum(1 for pat in _PROSPECTIF_TECH_PATTERNS if pat.search(text)),
    }
    best_score = max(scores.values())
    if best_score == 0:
        return _UNIT_CATEGORY_PRIOR.get(unit_id, "empirique")
    tied = [cat for cat, sc in scores.items() if sc == best_score]
    if len(tied) == 1:
        return tied[0]
    prior = _UNIT_CATEGORY_PRIOR.get(unit_id, "empirique")
    return prior if prior in tied else tied[0]


def _split_sentences(paragraph: str) -> list[str]:
    protected = _DECIMAL_DOT_RE.sub("<DOT>", paragraph)
    return [part.replace("<DOT>", ".") for part in split_sentences(protected)]


def _extract_unit_claims(root: Path, unit_meta: dict) -> list[dict]:
    uid = unit_meta["id"]
    upath = root / unit_meta["file"]
    if not upath.is_file():
        return []

    raw = upath.read_text(encoding="utf-8")
    body, _ = _strip_yaml_and_preserve_lines(raw)
    body = _mask_comments_and_biblio(body)
    body = _mask_fenced_code_preserving_lines(body)

    sname = _unit_sources_filename(uid)
    spath = root / "sources" / sname
    src_map = _parse_sources_md(spath) if spath.is_file() else {}

    claims: list[dict] = []
    p_idx = 0
    for block in re.split(r"\n\s*\n", body):
        stripped = block.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or is_markdown_table_block(stripped):
            continue
        if stripped.startswith("![") and stripped.endswith(")"):
            continue
        p_idx += 1
        para_loc = f"{uid}:P{p_idx:03d}"
        flat = re.sub(r"\s+", " ", stripped)

        s_idx = 0
        for sent in _split_sentences(flat):
            sent_clean = _MD_LINK_RE.sub(r"\1", _MD_IMAGE_RE.sub("", _INLINE_CODE_RE.sub("", sent)))
            refs: list[int] = []
            for m in _CITATION_REF_RE.finditer(sent_clean):
                for part in m.group(1).split(","):
                    refs.append(int(part.strip()))
            if not refs:
                continue
            s_idx += 1
            claim_loc = f"{para_loc}:S{s_idx:02d}"
            unique_refs = sorted(set(refs))
            source_ids = [src_map[r] for r in unique_refs if r in src_map and src_map[r]]
            claims.append(
                {
                    "claim_loc": claim_loc,
                    "paragraph_loc": para_loc,
                    "unit": uid,
                    "category": _classify_claim(sent, uid),
                    "text": sent,
                    "refs": unique_refs,
                    "source_ids": source_ids,
                    "vigilance_mandatory": False,
                }
            )
    return claims


def draw_stratified_sample(
    root: Path,
    seed: int,
    exclude_ids: set[str] | None = None,
) -> list[dict]:
    """Tire de facon deterministe 60 enonces stratifies (25/20/15, >= 2 par unite narrative)."""
    root = Path(root)
    excluded = set(exclude_ids or set())
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    narrative_units = [u for u in manifest["units"] if u["kind"] in {"frontmatter", "chapter"}]
    unit_order = {u["id"]: idx for idx, u in enumerate(narrative_units)}

    all_claims: list[dict] = []
    for u in narrative_units:
        all_claims.extend(_extract_unit_claims(root, u))

    eligible = [
        c
        for c in all_claims
        if c["claim_loc"] not in excluded and c["paragraph_loc"] not in excluded
    ]

    rng = random.Random(seed)
    rem_cat = dict(CATEGORY_QUOTAS)
    selected: list[dict] = []
    used_claims: set[str] = set()
    used_paras: set[str] = set()
    unit_counts: Counter[str] = Counter()

    def _add_item(item: dict, is_vig: bool = False) -> None:
        chosen = dict(item)
        chosen["vigilance_mandatory"] = is_vig
        selected.append(chosen)
        used_claims.add(chosen["claim_loc"])
        used_paras.add(chosen["paragraph_loc"])
        rem_cat[chosen["category"]] -= 1
        unit_counts[chosen["unit"]] += 1

    # Passe 1 : inclure d'office les 5 points de vigilance de prd.md § 7 quand exclude_ids est vide
    if not excluded:
        for _, matcher in _VIGILANCE_MATCHERS:
            matches = [
                c
                for c in eligible
                if c["claim_loc"] not in used_claims
                and rem_cat[c["category"]] > 0
                and matcher(c["text"].lower())
            ]
            if not matches:
                continue
            unseen_para = [c for c in matches if c["paragraph_loc"] not in used_paras]
            pool = unseen_para if unseen_para else matches
            rng.shuffle(pool)
            _add_item(pool[0], is_vig=True)

    # Etape 2 : garantir >= 2 items par unite narrative (unites les plus contraintes d'abord)
    def _unit_avail_count(uid: str) -> int:
        return sum(1 for c in eligible if c["unit"] == uid and c["claim_loc"] not in used_claims)

    ordered_units = [u["id"] for u in narrative_units]
    rng.shuffle(ordered_units)
    ordered_units.sort(key=_unit_avail_count)

    for uid in ordered_units:
        while unit_counts[uid] < 2:
            avail = [
                c
                for c in eligible
                if c["unit"] == uid and c["claim_loc"] not in used_claims and rem_cat[c["category"]] > 0
            ]
            if not avail:
                raise ValueError(
                    f"Enonces sources insuffisants pour atteindre >= 2 dans l'unite {uid} "
                    f"(quotas restants : {rem_cat})"
                )
            unseen = [c for c in avail if c["paragraph_loc"] not in used_paras]
            pool = unseen if unseen else avail
            max_rem = max(rem_cat[c["category"]] for c in pool)
            top_pool = [c for c in pool if rem_cat[c["category"]] == max_rem]
            rng.shuffle(top_pool)
            _add_item(top_pool[0])

    # Etape 3 : completer les quotas 25 empiriques, 20 juridiques, 15 prospectifs/techniques
    for cat in ("empirique", "juridique", "prospectif_technique"):
        while rem_cat[cat] > 0:
            avail = [
                c
                for c in eligible
                if c["category"] == cat and c["claim_loc"] not in used_claims
            ]
            if not avail:
                raise ValueError(
                    f"Enonces sources insuffisants pour la categorie '{cat}' "
                    f"(manque {rem_cat[cat]} item(s))"
                )
            unseen = [c for c in avail if c["paragraph_loc"] not in used_paras]
            pool = unseen if unseen else avail
            min_ucount = min(unit_counts[c["unit"]] for c in pool)
            balanced = [c for c in pool if unit_counts[c["unit"]] == min_ucount]
            rng.shuffle(balanced)
            _add_item(balanced[0])

    selected.sort(key=lambda c: (unit_order.get(c["unit"], 99), c["claim_loc"]))
    return selected


def _load_exclusions(path: Path | None) -> set[str]:
    if path is None:
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("items", data.get("sample", [])) if isinstance(data, dict) else data
    excluded: set[str] = set()
    if isinstance(items, list):
        for it in items:
            if isinstance(it, str):
                excluded.add(it)
            elif isinstance(it, dict):
                if it.get("claim_loc"):
                    excluded.add(str(it["claim_loc"]))
                if it.get("paragraph_loc"):
                    excluded.add(str(it["paragraph_loc"]))
    return excluded


def main() -> int:
    parser = argparse.ArgumentParser(description="Tirage stratifie G3 de 60 enonces sources.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du livre")
    parser.add_argument("--seed", type=int, required=True, help="Graine deterministe (ex. 202701, 202702)")
    parser.add_argument("--exclude", type=Path, default=None, help="JSON d'items/paragraphes a exclure")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Fichier JSON de sortie")
    args = parser.parse_args()

    exclude_ids = _load_exclusions(args.exclude)
    sample = draw_stratified_sample(args.root, seed=args.seed, exclude_ids=exclude_ids)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(sample, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK : {len(sample)} enonces tires (seed={args.seed}) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
