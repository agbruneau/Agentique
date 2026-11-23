#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Echantillonnage stratifie deterministe pour la barriere G3 du Volume 8 (echantillon_aq.py)."""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Callable

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import ABBREV_DOT_RE, is_markdown_table_block, split_sentences
from verifie_manuscrit import (  # noqa: E402
    _CA_G0_SYNC_RE,
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
    "empirique": 15,
    "juridique": 15,
    "spec_technique": 15,
    "assertions_g0": 15,
}
MIN_ITEMS_PER_UNIT = 8

_ABBREV_DOT_RE = ABBREV_DOT_RE
_DECIMAL_DOT_RE = re.compile(r"(?<=\d)\.(?=\d)")
_G0_EXPLICIT_REF_RE = re.compile(
    r"(?:aq/rapports-g0\.json|execute_g0\.py|G0-EX-CH\d{2}-\d{2}|CA-G0-SYNC)",
    re.IGNORECASE,
)

_EMPIRIQUE_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"%",
        r"\b40,58\b",
        r"\b51,09\b",
        r"\b4,16\b",
        r"\b5/15\b",
        r"\b77\s*%",
        r"\b84\s*%",
        r"\b41\s*%",
        r"\b86,7\s*%",
        r"\b68\s*%",
        r"\b80\s*%",
        r"\bempiriqu",
        r"\bmesur",
        r"\bétude",
        r"\bessais?\b",
        r"\bbancs?\b",
        r"\btrifecta\b",
        r"\bagentdojo\b",
        r"\bmast\b",
        r"\bmap\b",
        r"\blusser\b",
        r"\bcamel\b",
        r"\bpass(?:\^k|ᵏ)(?!\w)",
        r"\btaux\b",
        r"\bcoût",
        r"\boctets?\b",
        r"\blatence",
        r"\brug-?pull\b",
        r"\bdérive\s+silencieuse\b",
        r"\b3\s*309\b",
        r"\b4\s*627\b",
        r"\bcpo\b",
    )
)

_JURIDIQUE_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bloi\s+25\b",
        r"\blq-2021-c25\b",
        r"\bbsif\b",
        r"\bosfi\b",
        r"\be-23\b",
        r"\bb-10\b",
        r"\bb-15\b",
        r"\bamf\b",
        r"\bqc-amf\b",
        r"\bcai\b",
        r"\beu\s+ai\s+act\b",
        r"\bai\s+act\b",
        r"\bdora\b",
        r"\ben\s*18286\b",
        r"\bannexe\s+iii\b",
        r"\bannexe\s+i\b",
        r"\barticle\s+50\b",
        r"\b12\.1\b",
        r"\biso(?:/iec)?\s*42001\b",
        r"\bnon-avis\b",
        r"\bstatut\s+f\b",
        r"\bao-0[15]\b",
        r"\bjuridiqu",
        r"\br[eè]glement",
        r"\bprudentiel",
        r"\blégislat",
        r"\bhomologation\b",
        r"\bcertification\b",
        r"\bsor\b",
        r"\bimputabilit",
        r"\bmandat",
        r"\bconformit",
        r"\bpatrimonial",
    )
)

_SPEC_TECHNIQUE_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bmcp\b",
        r"\b2026-07-28\b",
        r"\bsep-2596\b",
        r"\bsep-3398\b",
        r"\ba2a\b",
        r"\bagentcard\b",
        r"\brfc\s*\d+\b",
        r"\bdraft-[a-z0-9-]+\b",
        r"\bwimse\b",
        r"\bspiffe\b",
        r"\boauth\b",
        r"\bobo\b",
        r"\bdpop\b",
        r"\bciba\b",
        r"\bi-json\b",
        r"\bjws\b",
        r"\bjcs\b",
        r"\bscitt\b",
        r"\bml-dsa\b",
        r"\bslh-dsa\b",
        r"\bfips\s*20[45]\b",
        r"\bir\s*8547\b",
        r"\botel\b",
        r"\bopentelemetry\b",
        r"\bsemantic-conventions-genai\b",
        r"\bcache_write\b",
        r"\bv1\.41\.0\b",
        r"\bfocus\b",
        r"\bjson\s+schema\b",
        r"\b2020-12\b",
        r"\bssf\b",
        r"\bcaep\b",
        r"\bstreamable\s+http\b",
        r"\bcbor-cose\b",
        r"\btransaction\s+tokens?\b",
        r"\barchimate\b",
        r"\bcyclonedx\b",
        r"\bspdx\b",
        r"\btls\b",
    )
)

_ASSERTIONS_G0_PATTERNS = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bexecute_g0\b",
        r"\brapports-g0\.json\b",
        r"\bexit\s+0\b",
        r"\bg0\b",
        r"\bopa\b",
        r"\brego\b",
        r"default\s+allow\s*:=\s*false",
        r"\bcouverture\s+négative\b",
        r"\ba2a-tck\b",
        r"\bacvp\b",
        r"\bsrc-055\b",
        r"\bca-g0-sync\b",
        r"\bg0-ex-ch\d{2}-\d{2}\b",
        r"\bexig-[a-z]+-\d+\b",
        r"\bprr(?:-75)?\b",
        r"\b2027-b001\b",
        r"\bsbb\b",
        r"\bc01[–-]c40\b",
        r"\bidem-v1\b",
        r"\btransactional\s+outbox\b",
        r"\bcompensationchannel\b",
        r"\bwilson\b",
        r"\b3/p\b",
        r"\bhttp\s*431\b",
        r"\bo\(sauts\)\b",
        r"\bo\(1\)\b",
        r"\bpytest\b",
        r"\brequirements\.lock\b",
        r"\bdecimal\b",
        r"\bieee-754\b",
        r"\bimds\b",
        r"network:\s*none",
        r"\bmock\s+mcp\b",
        r"\bmétamorphiqu",
        r"\bambigu_escalade\b",
        r"\bheadermismatch\b",
    )
)

_DEFAULT_UNIT_CATEGORY_PRIOR = {
    "00-liminaire": "spec_technique",
    "ch01": "spec_technique",
    "ch02": "spec_technique",
    "ch03": "assertions_g0",
    "ch04": "assertions_g0",
}

_DEFAULT_VIGILANCE_SPECS: tuple[tuple[str, str], ...] = (
    ("vig_mcp_sep_a2a", r"(?:sep-3398|sep-2596|1\.0\.0\.alpha3|v1\.1\.0-rc)"),
    ("vig_otel_genai", r"(?=.*v1\.41\.0)(?:.*semantic-conventions-genai|.*cache_write|.*85)"),
    ("vig_rfc9964_tx_tokens", r"(?:rfc\s*9964|transaction\s+tokens?|http\s*431)"),
    ("vig_wilson_3p", r"(?:exig-eva-03|wilson|3/p)"),
    ("vig_statut_f_src055", r"(?:src-055|lq-2021-c25|genai\.owasp\.org|lautorite\.qc\.ca|statut\s+f)"),
    ("vig_aibom_rfc9334_c5c6", r"(?:rfc\s*9334|cyclonedx|aibom|tableau\s*47\.3|\bc\.5\b|\bc\.6\b)"),
    ("vig_opa_default_deny", r"(?:default\s+allow\s*:=\s*false|ind[eé]finie?.*rego|opa\s+test.*100\s*%)"),
)


def _load_priors_and_vigilances(
    manifest: dict | None,
) -> tuple[dict[str, str], list[tuple[str, Callable[[str], bool]]]]:
    priors = dict(_DEFAULT_UNIT_CATEGORY_PRIOR)
    if isinstance(manifest, dict) and isinstance(manifest.get("unit_category_prior"), dict):
        for k, v in manifest["unit_category_prior"].items():
            if v in CATEGORY_QUOTAS:
                priors[str(k)] = str(v)

    matchers: list[tuple[str, Callable[[str], bool]]] = []
    raw_vigs = (manifest or {}).get("vigilance_matchers")
    if isinstance(raw_vigs, list) and raw_vigs:
        for item in raw_vigs:
            if not isinstance(item, dict):
                continue
            vid = str(item.get("id", "vig"))
            pat_str = str(item.get("pattern", ""))
            if not pat_str:
                continue
            pat = re.compile(pat_str, re.IGNORECASE)
            matchers.append((vid, lambda s, _p=pat: bool(_p.search(s))))
    if not matchers:
        for vid, pat_str in _DEFAULT_VIGILANCE_SPECS:
            pat = re.compile(pat_str, re.IGNORECASE)
            matchers.append((vid, lambda s, _p=pat: bool(_p.search(s))))
    return priors, matchers


def _classify_claim(
    text: str,
    unit_id: str,
    unit_priors: dict[str, str] | None = None,
    has_g0_anchor: bool = False,
) -> str:
    priors = unit_priors or _DEFAULT_UNIT_CATEGORY_PRIOR
    scores = {
        "empirique": sum(1 for pat in _EMPIRIQUE_PATTERNS if pat.search(text)),
        "juridique": sum(1 for pat in _JURIDIQUE_PATTERNS if pat.search(text)),
        "spec_technique": sum(1 for pat in _SPEC_TECHNIQUE_PATTERNS if pat.search(text)),
        "assertions_g0": sum(1 for pat in _ASSERTIONS_G0_PATTERNS if pat.search(text)) + (2 if has_g0_anchor else 0),
    }
    best_score = max(scores.values())
    if best_score == 0:
        return priors.get(unit_id, "empirique")
    tied = [cat for cat, sc in scores.items() if sc == best_score]
    if len(tied) == 1:
        return tied[0]
    prior = priors.get(unit_id, "empirique")
    return prior if prior in tied else tied[0]


def _split_sentences(paragraph: str) -> list[str]:
    protected = _DECIMAL_DOT_RE.sub("<DOT>", paragraph)
    return [part.replace("<DOT>", ".") for part in split_sentences(protected)]


def _extract_unit_claims(
    root: Path,
    unit_meta: dict,
    unit_priors: dict[str, str] | None = None,
) -> list[dict]:
    uid = unit_meta["id"]
    upath = root / unit_meta["file"]
    if not upath.is_file():
        return []

    raw = upath.read_text(encoding="utf-8")
    body_raw, _ = _strip_yaml_and_preserve_lines(raw)

    # Reperer les ancres CA-G0-SYNC par numero de ligne avant masquage des commentaires
    sync_anchors_by_line: dict[int, str] = {}
    for lidx, raw_ln in enumerate(body_raw.splitlines()):
        m_sync = _CA_G0_SYNC_RE.search(raw_ln)
        if m_sync:
            sync_anchors_by_line[lidx] = m_sync.group(1)

    body = _mask_comments_and_biblio(body_raw)
    body = _mask_fenced_code_preserving_lines(body)

    sname = _unit_sources_filename(uid)
    spath = root / "sources" / sname
    src_map = _parse_sources_md(spath) if spath.is_file() else {}

    claims: list[dict] = []
    p_idx = 0
    cursor = 0
    for block in re.split(r"\n\s*\n", body):
        block_start_pos = body.find(block, cursor)
        block_start_line = body[:block_start_pos].count("\n") if block_start_pos >= 0 else 0
        block_end_line = block_start_line + block.count("\n")
        if block_start_pos >= 0:
            cursor = block_start_pos + len(block)

        stripped = block.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or is_markdown_table_block(stripped):
            continue
        if stripped.startswith("![") and stripped.endswith(")"):
            continue

        nearby_excerpts = [
            eid
            for ln, eid in sync_anchors_by_line.items()
            if (block_start_line - 4) <= ln <= (block_end_line + 4)
        ]

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

            has_g0_ref = bool(_G0_EXPLICIT_REF_RE.search(sent)) or (
                bool(nearby_excerpts) and any(p.search(sent) for p in _ASSERTIONS_G0_PATTERNS)
            )
            if not refs and not has_g0_ref:
                continue

            s_idx += 1
            claim_loc = f"{para_loc}:S{s_idx:02d}"
            unique_refs = sorted(set(refs))
            source_ids = [src_map[r] for r in unique_refs if r in src_map and src_map[r]]
            if has_g0_ref and "aq/rapports-g0.json" not in source_ids:
                source_ids.append("aq/rapports-g0.json")
            cat = _classify_claim(sent, uid, unit_priors=unit_priors, has_g0_anchor=has_g0_ref)
            if not unique_refs and has_g0_ref:
                cat = "assertions_g0"
            item: dict = {
                "claim_loc": claim_loc,
                "paragraph_loc": para_loc,
                "unit": uid,
                "category": cat,
                "text": sent,
                "refs": unique_refs,
                "source_ids": source_ids,
                "vigilance_mandatory": False,
            }
            if nearby_excerpts:
                item["g0_excerpt_ids"] = sorted(set(nearby_excerpts))
            claims.append(item)
    return claims


def draw_stratified_sample(
    root: Path,
    seed: int,
    exclude_ids: set[str] | None = None,
) -> list[dict]:
    """Tire de facon deterministe 60 enonces stratifies (4 x 15 dont assertions_g0, >= 8 par unite narrative)."""
    root = Path(root)
    excluded = set(exclude_ids or set())
    manifest = json.loads((root / "specs" / "manifest.json").read_text(encoding="utf-8"))
    narrative_units = [u for u in manifest["units"] if u["kind"] in {"frontmatter", "chapter"}]
    unit_order = {u["id"]: idx for idx, u in enumerate(narrative_units)}
    unit_priors, vigilance_matchers = _load_priors_and_vigilances(manifest)

    all_claims: list[dict] = []
    for u in narrative_units:
        all_claims.extend(_extract_unit_claims(root, u, unit_priors=unit_priors))

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

    # Passe 1 : inclure d'office les 7 points de vigilance de prd.md § 7 quand exclude_ids est vide
    if not excluded:
        for _, matcher in vigilance_matchers:
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

    # Etape 2 : garantir >= 8 items par unite narrative (unites les plus contraintes d'abord)
    def _unit_avail_count(uid: str) -> int:
        return sum(
            1
            for c in eligible
            if c["unit"] == uid and c["claim_loc"] not in used_claims and rem_cat[c["category"]] > 0
        )

    ordered_units = [u["id"] for u in narrative_units]
    rng.shuffle(ordered_units)
    ordered_units.sort(key=_unit_avail_count)

    for uid in ordered_units:
        while unit_counts[uid] < MIN_ITEMS_PER_UNIT:
            avail = [
                c
                for c in eligible
                if c["unit"] == uid and c["claim_loc"] not in used_claims and rem_cat[c["category"]] > 0
            ]
            if not avail:
                raise ValueError(
                    f"Enonces sources insuffisants pour atteindre >= {MIN_ITEMS_PER_UNIT} dans l'unite {uid} "
                    f"(actuel={unit_counts[uid]}, quotas restants={rem_cat})"
                )
            unseen = [c for c in avail if c["paragraph_loc"] not in used_paras]
            pool = unseen if unseen else avail
            max_rem = max(rem_cat[c["category"]] for c in pool)
            top_pool = [c for c in pool if rem_cat[c["category"]] == max_rem]
            rng.shuffle(top_pool)
            _add_item(top_pool[0])

    # Etape 3 : completer les quotas 15 empiriques, 15 juridiques, 15 spec_technique, 15 assertions_g0
    for cat in ("empirique", "juridique", "spec_technique", "assertions_g0"):
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
    parser = argparse.ArgumentParser(description="Tirage stratifie G3 de 60 enonces sources (4 x 15, Volume 8).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Racine du manuel")
    parser.add_argument("--seed", type=int, required=True, help="Graine deterministe (ex. 20270801, 20270802)")
    parser.add_argument("--exclude", type=Path, default=None, help="JSON d'items/paragraphes a exclure")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Fichier JSON de sortie")
    args = parser.parse_args()

    exclude_ids = _load_exclusions(args.exclude)
    sample = draw_stratified_sample(args.root, seed=args.seed, exclude_ids=exclude_ids)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(sample, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"OK : {len(sample)} enonces tires (seed={args.seed}) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
