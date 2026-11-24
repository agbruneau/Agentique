#!/usr/bin/env python3
"""Inventorie et vérifie sur disque les 319 diagrammes des Tomes 1 à 8.

Ce script parse les 8 catalogues `README.md` situés dans `Tomes/Tome */Diagrammes/`
(Tomes 1 à 6) et `Tomes/Tome */diagrammes/` (Tomes 7 et 8), vérifie l'existence
réelle de 100 % des sources (`.puml`/`.mmd`), des rendus (`rendus/*.svg` / `.png`)
et des chapitres cibles, rattache chaque figure aux domaines `D01..D12` et génère
`Cartographie/donnees/inventaire-319-diagrammes.json` en LF strict.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[2]
TOMES_DIR = REPO_ROOT / "Tomes"
SYNTHESE_PATH = REPO_ROOT / "Cartographie" / "donnees" / "synthese-transversale.json"
OUTPUT_PATH = REPO_ROOT / "Cartographie" / "donnees" / "inventaire-319-diagrammes.json"

EXPECTED_BY_TOME: dict[str, dict[str, int]] = {
    "T1": {"total": 118, "PlantUML": 63, "Mermaid": 55},
    "T2": {"total": 28, "PlantUML": 25, "Mermaid": 3},
    "T3": {"total": 68, "PlantUML": 68, "Mermaid": 0},
    "T4": {"total": 6, "PlantUML": 6, "Mermaid": 0},
    "T5": {"total": 8, "PlantUML": 8, "Mermaid": 0},
    "T6": {"total": 59, "PlantUML": 56, "Mermaid": 3},
    "T7": {"total": 23, "PlantUML": 20, "Mermaid": 3},
    "T8": {"total": 9, "PlantUML": 7, "Mermaid": 2},
}

DOMAIN_KEYWORDS: dict[str, tuple[str, ...]] = {
    "D01": (
        "lusser",
        "coase",
        "dette cognitive",
        "dette d intention",
        "systems of agency",
        "systeme de travail",
        "economie cognitive",
        "marche agentique",
        "rupture epistemique",
        "inflation de jetons",
        "non-compositionnalite",
        "invariant de la somme",
        "copilote",
        "erosion",
    ),
    "D02": (
        "80/20",
        "harnais",
        "harness",
        "l0-l4",
        "l0 l4",
        "autonomie",
        "hitl",
        "hotl",
        "noyau possede",
        "archimate",
        "togaf",
        "acheter",
        "assembler",
        "construire",
        "cadre en une page",
        "quatre plans",
        "cinq couches",
        "six couches",
        "ambigu_escalade",
        "capacite",
        "invariante",
    ),
    "D03": (
        "mcp",
        "a2a",
        "agntcy",
        "slim",
        "ap2",
        "agent card",
        "agentcard",
        "passerelle",
        "gateway",
        "pep",
        "verrouillage",
        "swagger",
        "streamable http",
        "interoperabilite",
        "eif",
        "lcim",
        "n x m",
        "n + m",
        "decouverte",
        "registre",
    ),
    "D04": (
        "coala",
        "memoire",
        "rag",
        "ontologie",
        "fibo",
        "odcs",
        "rdf",
        "owl",
        "json-ld",
        "acl",
        "patrimonial",
        "erp",
        "sap",
        "mainframe",
        "it/ot",
        "rpa",
        "kv-cache",
        "semantique",
        "contexte",
        "schema",
    ),
    "D05": (
        "orchestration",
        "oo1",
        "oo3",
        "oo4",
        "choregraphie",
        "evenement",
        "cloudevents",
        "asyncapi",
        "saga",
        "temporal",
        "restate",
        "outbox",
        "idempotence",
        "idem-v1",
        "point pivot",
        "compensation",
        "mast",
        "boucle agentique",
        "flux de travail",
        "xagenthopcount",
        "exactement une fois",
        "sobre",
        "sobriete",
    ),
    "D06": (
        "nhi",
        "identite non humaine",
        "spiffe",
        "spire",
        "svid",
        "obo",
        "rfc 8693",
        "dpop",
        "mtls",
        "ciba",
        "fido2",
        "rar",
        "transaction token",
        "http 431",
        "pki",
        "acme",
        "47 jours",
        "post-quantique",
        "pqc",
        "ml-dsa",
        "ml-kem",
        "slh-dsa",
        "did",
        "vlei",
        "oauth",
        "oidc",
        "saml",
        "ssf",
        "caep",
        "secret",
        "delegation cryptographique",
    ),
    "D07": (
        "opa",
        "rego",
        "regle de deux",
        "camel",
        "owasp",
        "asi0",
        "atlas",
        "injection",
        "poisoning",
        "rug pull",
        "mandataire confus",
        "confinement",
        "shadi",
        "microvm",
        "wasi",
        "tee",
        "coupe-circuit",
        "soc",
        "zero-trust",
        "zero trust",
        "hors modele",
        "defense en profondeur",
        "default allow",
    ),
    "D08": (
        "otel",
        "opentelemetry",
        "double couloir",
        "jcs",
        "scitt",
        "evalops",
        "wilson",
        "pass^k",
        "pass k",
        "metamorphique",
        "finops",
        "focus",
        "cpo",
        "cout par resultat",
        "cout complet",
        "b-15",
        "carbone",
        "distillation",
        "slm",
        "burn rate",
        "sre",
        "observabilite",
        "telemetrie",
        "showback",
        "chargeback",
    ),
    "D09": (
        "loi 25",
        "bsif",
        "e-23",
        "b-13",
        "b-10",
        "amf",
        "acvm",
        "31-103",
        "eu ai act",
        "18286",
        "dora",
        "cra",
        "42001",
        "nist",
        "imda",
        "aica",
        "g7",
        "approvisionnement",
        "juridique",
        "reglementaire",
        "prudentiel",
        "efvp",
        "portabilite",
        "clause",
    ),
    "D10": (
        "sectoriel",
        "banque",
        "patrimoine",
        "assurance",
        "retraite",
        "rtr",
        "iso 20022",
        "m-14",
        "m-15",
        "m-16",
        "m-17",
        "m-18",
        "pex",
        "blueprint",
        "c01",
        "c40",
        "boreal",
        "adlc",
        "gitops",
        "anti-patron",
        "canary",
        "shadow",
        "strangler",
        "iap",
        "internal agentic platform",
        "team topologies",
        "bpm",
        "ipaas",
        "souscription",
        "credit",
    ),
    "D11": (
        "prospective",
        "2027-2035",
        "2028-2035",
        "2026-2035",
        "2035",
        "dapp",
        "palier",
        "por-",
        "sig-",
        "vivier junior",
        "competences humaines",
        "ini-043",
        "reprise manuelle",
        "90 jours",
        "180",
        "360",
        "trajectoire adaptative",
        "incertitude",
        "cone d incertitude",
        "urbanisation",
        "ae / as",
        "ae as",
    ),
    "D12": (
        "homologation",
        "cre-ia",
        "exig-",
        "prr-75",
        "prr",
        "bloquant",
        "2027-b001",
        "5 sbb",
        "sbb",
        "trousse",
        "tome 8",
        "div-02",
        "disc-",
        "concordance",
        "wyvern",
        "g0-g5",
        "g0 g5",
        "ca-16",
        "typst",
        "revalidation",
        "peremption",
        "gouvernance du portefeuille",
        "a2a-tck",
    ),
}


def _norm_ascii(text: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9^/+.-]+", " ", ascii_text).strip()


def _sanitize_prose(text: str) -> str:
    """Normalise les flèches ASCII hors backticks et supprime d'éventuels `\\$` littéraux."""
    parts = re.split(r"(`[^`]*`)", text)
    cleaned: list[str] = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            cleaned.append(part)
        else:
            p = part.replace(r"\$", "$")
            p = p.replace("<->", "↔").replace("->", "→")
            cleaned.append(p)
    return "".join(cleaned).strip()


def _strip_figure_prefix(raw_caption: str) -> str:
    stripped = re.sub(
        r"^(?:Figure|Fig\.?)\s+[0-9]+(?:\.[0-9]+)?(?:\s*\([^)]*\))?\s*\.?\s*[—–-]\s*",
        "",
        raw_caption.strip(),
    ).strip()
    return stripped or raw_caption.strip()


def _match_synthese_chapter(
    tome_id: str,
    section_label: str,
    chapters_by_tome: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    ns = _norm_ascii(section_label)
    candidates = chapters_by_tome.get(tome_id, [])
    for ch in candidates:
        nc = _norm_ascii(ch["chapter_title"])
        if ns == nc or ns in nc or nc in ns:
            return ch
    m_cnum = re.search(r"(?:chapitre\s+m-|chapitre\s+|^\s*)(\d+)", ns)
    if m_cnum:
        num_tok = m_cnum.group(1).lstrip("0") or "0"
        for ch in candidates:
            nc = _norm_ascii(ch["chapter_title"])
            if re.search(rf"\b(?:chapitre\s+m\s+|chapitre\s+)?0?{num_tok}\b", nc):
                return ch
    raise ValueError(f"Impossible de rattacher la section {section_label!r} ({tome_id}) à synthese-transversale.json")


def _infer_domain_hints(
    title: str,
    raw_caption: str,
    section_label: str,
    matched_chapter: dict[str, Any],
) -> list[str]:
    haystack = _norm_ascii(f"{title} {raw_caption} {section_label}")
    scores: dict[str, int] = {}
    for dom_id, keywords in DOMAIN_KEYWORDS.items():
        score = 0
        for kw in keywords:
            if kw in haystack:
                score += 2 if " " in kw or "-" in kw else 1
        if score > 0:
            scores[dom_id] = score

    primary = matched_chapter.get("primary_domain")
    secondary = matched_chapter.get("secondary_domains") or []

    ranked = sorted(scores.keys(), key=lambda d: (-scores[d], d))
    ordered: list[str] = []
    for d in ranked[:3]:
        if d not in ordered:
            ordered.append(d)
    if primary and primary not in ordered:
        ordered.insert(0, primary)
    if not ordered:
        ordered = [primary] if primary else []
    for sec_d in secondary:
        if len(ordered) < 3 and sec_d not in ordered:
            ordered.append(sec_d)
    if not ordered:
        raise ValueError(f"Aucun domaine inféré pour {title!r}")
    return ordered


def build_inventory() -> dict[str, Any]:
    synthese = json.loads(SYNTHESE_PATH.read_text(encoding="utf-8"))
    chapters_by_tome: dict[str, list[dict[str, Any]]] = {}
    for ch in synthese["chapters"]:
        chapters_by_tome.setdefault(ch["tome_id"], []).append(ch)

    figures: list[dict[str, Any]] = []
    by_tome_summary: dict[str, dict[str, Any]] = {}
    seen_keys: set[tuple[str, str]] = set()
    missing_files: list[str] = []

    tome_dirs = sorted(
        d for d in TOMES_DIR.iterdir()
        if d.is_dir() and re.match(r"^Tome \d+\s+-", d.name)
    )
    if len(tome_dirs) != 8:
        raise RuntimeError(f"Nombre de dossiers Tomes invalide : {len(tome_dirs)} (attendu 8)")

    for tome_dir in tome_dirs:
        m_tome = re.match(r"^Tome (\d+)\s+-", tome_dir.name)
        assert m_tome is not None
        tnum = int(m_tome.group(1))
        tome_id = f"T{tnum}"
        expected_diag_dirname = "Diagrammes" if tnum <= 6 else "diagrammes"
        diag_dir = tome_dir / expected_diag_dirname
        if not diag_dir.is_dir():
            raise RuntimeError(f"Dossier attendu introuvable : {diag_dir}")

        readme_path = diag_dir / "README.md"
        if not readme_path.is_file():
            raise RuntimeError(f"Catalogue introuvable : {readme_path}")

        lines = readme_path.read_text(encoding="utf-8").splitlines()
        table_lines = [ln for ln in lines if ln.lstrip().startswith("|")]
        if len(table_lines) < 3:
            raise RuntimeError(f"Table absente dans {readme_path}")
        data_rows = table_lines[2:]

        rendus_dir = diag_dir / "rendus"
        rendus_by_stem = {p.stem: p for p in rendus_dir.iterdir() if p.is_file()}
        src_on_disk = {p.resolve() for p in diag_dir.iterdir() if p.is_file() and p.suffix in {".puml", ".mmd"}}
        ren_on_disk = {p.resolve() for p in rendus_dir.iterdir() if p.is_file() and p.suffix in {".svg", ".png"}}
        matched_src: set[Path] = set()
        matched_ren: set[Path] = set()

        tome_puml = 0
        tome_mmd = 0

        for row in data_rows:
            cells = [c.strip().replace(r"\|", "|") for c in re.split(r"(?<!\\)\|", row.strip().strip("|"))]
            if len(cells) != 6:
                raise RuntimeError(f"{tome_id}: ligne invalide à {len(cells)} colonnes : {row}")

            if tnum <= 6:
                fig_id, page_str, sec_cell, fmt_cell, src_cell, raw_caption = cells
                ren_cell: str | None = None
                title = _strip_figure_prefix(raw_caption)
            else:
                fig_id, raw_title, sec_cell, fmt_cell, src_cell, ren_cell = cells
                page_str = ""
                raw_caption = raw_title
                title = raw_title

            fig_id = fig_id.strip()
            if (tome_id, fig_id) in seen_keys:
                raise RuntimeError(f"Doublon détecté sur {(tome_id, fig_id)}")
            seen_keys.add((tome_id, fig_id))

            m_sec = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", sec_cell)
            if not m_sec:
                raise RuntimeError(f"{tome_id} {fig_id}: format de section inattendu : {sec_cell}")
            sec_label = _sanitize_prose(m_sec.group(1).strip())
            sec_file = (diag_dir / unquote(m_sec.group(2))).resolve()
            if not sec_file.is_file():
                missing_files.append(str(sec_file))

            m_src = re.search(r"\]\(([^)]+)\)", src_cell)
            if not m_src:
                raise RuntimeError(f"{tome_id} {fig_id}: lien source absent : {src_cell}")
            src_rel_raw = unquote(m_src.group(1))
            src_file = (diag_dir / src_rel_raw).resolve()
            if not src_file.is_file():
                missing_files.append(str(src_file))
            else:
                matched_src.add(src_file)

            fmt_norm = fmt_cell.strip()
            if fmt_norm == "PlantUML" and src_file.suffix == ".puml":
                notation = "PlantUML"
                expected_ext = ".svg"
                tome_puml += 1
            elif fmt_norm == "Mermaid" and src_file.suffix == ".mmd":
                notation = "Mermaid"
                expected_ext = ".png"
                tome_mmd += 1
            else:
                raise RuntimeError(f"{tome_id} {fig_id}: incohérence format {fmt_norm!r} vs {src_file.name!r}")

            if ren_cell is not None:
                m_ren = re.search(r"\]\(([^)]+)\)", ren_cell)
                if not m_ren:
                    raise RuntimeError(f"{tome_id} {fig_id}: lien rendu absent : {ren_cell}")
                ren_file = (diag_dir / unquote(m_ren.group(1))).resolve()
            else:
                stem = Path(src_rel_raw).stem
                prefix = stem.split(" - ")[0]
                cand = rendus_by_stem.get(stem) or rendus_by_stem.get(prefix)
                if cand is None:
                    missing_files.append(str(rendus_dir / f"{prefix}{expected_ext}"))
                    continue
                ren_file = cand.resolve()

            if not ren_file.is_file() or ren_file.suffix != expected_ext:
                missing_files.append(str(ren_file))
            else:
                matched_ren.add(ren_file)

            matched_chapter = _match_synthese_chapter(tome_id, sec_label, chapters_by_tome)
            clean_title = _sanitize_prose(title)
            clean_caption = _sanitize_prose(raw_caption)
            domain_hints = _infer_domain_hints(clean_title, clean_caption, sec_label, matched_chapter)

            page_val: int | str | None = None
            if page_str:
                page_val = int(page_str) if page_str.isdigit() else _sanitize_prose(page_str)

            figures.append(
                {
                    "diagram_uid": f"{tome_id}:{fig_id}",
                    "tome_id": tome_id,
                    "fig_id": fig_id,
                    "title": clean_title,
                    "raw_caption": clean_caption,
                    "notation": notation,
                    "source_path": src_file.relative_to(REPO_ROOT).as_posix(),
                    "rendered_path": ren_file.relative_to(REPO_ROOT).as_posix(),
                    "source_section": sec_label,
                    "source_section_file": sec_file.relative_to(REPO_ROOT).as_posix(),
                    "matched_unit_id": matched_chapter["unit_id"],
                    "page": page_val,
                    "domain_hints": domain_hints,
                }
            )

        if matched_src != src_on_disk:
            raise RuntimeError(f"{tome_id}: écart sources disque vs README : {src_on_disk ^ matched_src}")
        if matched_ren != ren_on_disk:
            raise RuntimeError(f"{tome_id}: écart rendus disque vs README : {ren_on_disk ^ matched_ren}")

        by_tome_summary[tome_id] = {
            "diagram_directory": diag_dir.relative_to(REPO_ROOT).as_posix(),
            "catalog_readme": readme_path.relative_to(REPO_ROOT).as_posix(),
            "total": len(data_rows),
            "PlantUML": tome_puml,
            "Mermaid": tome_mmd,
        }
        exp = EXPECTED_BY_TOME[tome_id]
        if (
            len(data_rows) != exp["total"]
            or tome_puml != exp["PlantUML"]
            or tome_mmd != exp["Mermaid"]
        ):
            raise RuntimeError(
                f"{tome_id}: décompte inattendu ({len(data_rows)}={tome_puml}+{tome_mmd}) vs attendu {exp}"
            )

    if missing_files:
        raise RuntimeError(f"Fichiers manquants sur disque ({len(missing_files)}) : {missing_files[:5]}")

    total_figures = len(figures)
    total_plantuml = sum(1 for f in figures if f["notation"] == "PlantUML")
    total_mermaid = sum(1 for f in figures if f["notation"] == "Mermaid")

    assert total_figures == 319, f"Total attendu 319, obtenu {total_figures}"
    assert total_plantuml == 253, f"PlantUML attendu 253, obtenu {total_plantuml}"
    assert total_mermaid == 66, f"Mermaid attendu 66, obtenu {total_mermaid}"
    assert total_plantuml + total_mermaid == 319
    assert len(missing_files) == 0

    return {
        "schema_version": "1.0.0",
        "lang": "fr-CA",
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generator": "Cartographie/outils/inventorier_diagrammes_tomes.py",
        "totals": {
            "total_figures": total_figures,
            "plantuml_svg": total_plantuml,
            "mermaid_png": total_mermaid,
            "missing_files": 0,
            "by_tome": by_tome_summary,
        },
        "figures": figures,
    }


def _verify_json_hygiene(payload: dict[str, Any], out_path: Path) -> None:
    raw_bytes = out_path.read_bytes()
    assert bytes([13, 10]) not in raw_bytes, f"CRLF détecté dans {out_path}"
    raw_text = raw_bytes.decode("utf-8")
    # Vérifier absence de `\$` et de flèches ASCII hors backticks
    assert r"\$" not in raw_text, f"Séquence \\$ détectée dans {out_path}"
    parts = re.split(r"`[^`]*`", raw_text)
    for part in parts:
        assert "<->" not in part and "->" not in part, f"Flèche ASCII détectée hors backticks dans {out_path}"
    # Re-vérifier chaque fichier disque
    for fig in payload["figures"]:
        assert (REPO_ROOT / fig["source_path"]).is_file(), f"Source introuvable : {fig['source_path']}"
        assert (REPO_ROOT / fig["rendered_path"]).is_file(), f"Rendu introuvable : {fig['rendered_path']}"
        assert (REPO_ROOT / fig["source_section_file"]).is_file(), f"Section introuvable : {fig['source_section_file']}"
        assert fig["domain_hints"], f"domain_hints vide pour {fig['diagram_uid']}"


def main() -> None:
    payload = build_inventory()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(serialized)
    _verify_json_hygiene(payload, OUTPUT_PATH)
    t = payload["totals"]
    print(
        f"Inventaire généré -> {OUTPUT_PATH} : {t['total_figures']} figures "
        f"({t['plantuml_svg']} PlantUML/SVG + {t['mermaid_png']} Mermaid/PNG, 0 manquant)."
    )
    for tid, stats in t["by_tome"].items():
        print(f"  {tid}: {stats['total']} ({stats['PlantUML']} PlantUML + {stats['Mermaid']} Mermaid)")


if __name__ == "__main__":
    main()
