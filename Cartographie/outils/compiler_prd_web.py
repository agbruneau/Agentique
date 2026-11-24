#!/usr/bin/env python3
"""Compilateur de la page web autonome dédiée au PRD maître du Corpus Agentique.

Assemble :
- ``Cartographie/donnees/prd-web-data.json`` (produit par ``preparer_donnees_prd_web.py``)
- ``Cartographie/outils/template_prd_web.html``

Valide le contrat JSON minimal attendu (12 parties, 36 chapitres, 71 familles,
260 thèmes, 4 annexes A–D, table ``lookup``), échappe de façon sûre le JSON
embarqué pour ``<script type="application/json">``, vérifie l'autonomie hors ligne
stricte (zéro URL ``http://`` ou ``https://`` hors bloc JSON) et génère :
- ``Cartographie/PRD - Référentiel directeur de l'entreprise agentique.html``
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

PAGE_TITLE = "PRD — Référentiel directeur de l'entreprise agentique"
DEFAULT_HTML_NAME = "PRD - Référentiel directeur de l'entreprise agentique.html"


def escape_json_for_script(json_str: str) -> str:
    """Échappe une chaîne JSON pour injection sûre dans un bloc ``<script>`` HTML.

    - ``</`` -> ``<\\/`` (évite toute fermeture prématurée de ``</script>``)
    - ``<!--`` -> ``\\u003c!--`` (évite l'ouverture de commentaire HTML)
    - U+2028 / U+2029 -> ``\\u2028`` / ``\\u2029`` (séparateurs de ligne JS)
    """
    return (
        json_str.replace("</", "<\\/")
        .replace("<!--", "\\u003c!--")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def validate_prd_web_payload(payload: dict[str, Any]) -> dict[str, int]:
    """Vérifie la complétude structurelle du contrat ``prd-web-data.json``."""
    required_top = ("meta", "executive_summary", "parties", "chapters", "annexes", "lookup")
    missing = [key for key in required_top if key not in payload]
    if missing:
        raise ValueError(f"Clés racine manquantes dans prd-web-data.json : {missing}")

    exec_sections = (payload.get("executive_summary") or {}).get("sections") or []
    parties = payload.get("parties") or []
    chapters = payload.get("chapters") or []
    annexes = payload.get("annexes") or []
    lookup = payload.get("lookup") or {}

    if len(exec_sections) != 5:
        raise ValueError(f"executive_summary.sections attendu=5, trouvé={len(exec_sections)}")
    if len(parties) != 12:
        raise ValueError(f"parties attendu=12, trouvé={len(parties)}")
    if len(chapters) != 36:
        raise ValueError(f"chapters attendu=36, trouvé={len(chapters)}")
    if [a.get("annexe_code") for a in annexes] != ["A", "B", "C", "D"]:
        raise ValueError("annexes doit contenir exactement A, B, C, D dans l'ordre.")

    family_count = 0
    theme_count = 0
    interrelation_count = 0
    for ch in chapters:
        tc = ch.get("targeted_content") or {}
        fams = tc.get("families_and_themes") or []
        family_count += len(fams)
        for fam in fams:
            theme_count += len(fam.get("themes_targeted") or [])
        interrelation_count += len(tc.get("cross_chapter_interrelations") or [])

    if family_count != 71:
        raise ValueError(f"Nombre de familles attendu=71, trouvé={family_count}")
    if theme_count != 260:
        raise ValueError(f"Nombre de thèmes attendu=260, trouvé={theme_count}")

    node_map = lookup.get("node_id_to_prd") or {}
    if not node_map:
        raise ValueError("lookup.node_id_to_prd ne doit pas être vide.")

    return {
        "exec_sections": len(exec_sections),
        "parties": len(parties),
        "chapters": len(chapters),
        "families": family_count,
        "themes": theme_count,
        "annexes": len(annexes),
        "chapter_interrelations": interrelation_count,
        "lookup_nodes": len(node_map),
    }


def _load_prd_payload(repo_root: Path, data_path: Path | None) -> dict[str, Any]:
    """Charge ``prd-web-data.json`` ou le construit via ``preparer_donnees_prd_web`` si absent."""
    donnees_dir = repo_root / "Cartographie" / "donnees"
    target_json = data_path or (donnees_dir / "prd-web-data.json")
    if target_json.is_file():
        return json.loads(target_json.read_text(encoding="utf-8"))

    if data_path is not None:
        raise FileNotFoundError(f"Fichier de données PRD introuvable : {target_json}")

    outils_dir = Path(__file__).resolve().parent
    if str(outils_dir) not in sys.path:
        sys.path.insert(0, str(outils_dir))
    try:
        import preparer_donnees_prd_web as prep  # type: ignore
    except ImportError as exc:
        raise FileNotFoundError(
            f"Données PRD introuvables ({target_json}) et module preparer_donnees_prd_web absent."
        ) from exc
    return prep.build_prd_web_payload(repo_root)


def compile_prd_web(
    repo_root: Path,
    output_html: Path | None = None,
    data_path: Path | None = None,
) -> tuple[Path, dict[str, Any]]:
    """Compile la page HTML autonome ``Cartographie/PRD - Référentiel directeur de l'entreprise agentique.html``."""
    outils_dir = repo_root / "Cartographie" / "outils"
    template_path = outils_dir / "template_prd_web.html"
    if not template_path.is_file():
        raise FileNotFoundError(f"Gabarit HTML PRD introuvable : {template_path}")

    payload = _load_prd_payload(repo_root, data_path)
    metrics = validate_prd_web_payload(payload)

    template_html = template_path.read_text(encoding="utf-8")
    if template_html.count("__PRD_DATA_JSON__") != 1:
        raise ValueError(
            "Le marqueur __PRD_DATA_JSON__ doit apparaître exactement une fois dans template_prd_web.html"
        )
    if "__PAGE_TITLE__" not in template_html:
        raise ValueError("Le marqueur __PAGE_TITLE__ est absent de template_prd_web.html")

    minified_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    safe_json = escape_json_for_script(minified_json)

    for forbidden in ("</", "<!--", "\u2028", "\u2029"):
        if forbidden in safe_json:
            raise ValueError(f"Séquence dangereuse résiduelle dans le JSON échappé : {forbidden!r}")

    compiled_html = template_html.replace("__PAGE_TITLE__", PAGE_TITLE).replace(
        "__PRD_DATA_JSON__", safe_json, 1
    )

    if "__PRD_DATA_JSON__" in compiled_html or "__PAGE_TITLE__" in compiled_html:
        raise ValueError("Marqueur non substitué dans le HTML compilé.")

    # Vérification stricte de l'autonomie hors ligne hors bloc JSON
    m_json = re.search(
        r'<script[^>]*id="prd-web-data"[^>]*>([\s\S]*?)</script>', compiled_html
    )
    if m_json is None:
        raise ValueError("Bloc <script id='prd-web-data'> introuvable après compilation.")
    html_outside_json = compiled_html[: m_json.start(1)] + compiled_html[m_json.end(1) :]
    forbidden_patterns: tuple[tuple[str, str], ...] = (
        (r"https?://", "URL http(s)://"),
        (r"<script[^>]+src\s*=", "<script src=...>"),
        (r"<link[^>]+href\s*=\s*['\"]?(?:https?:)?//", "<link href=//...>"),
        (r"\b(?:src|href)\s*=\s*['\"]?\s*//", "attribut src/href relatif protocole //"),
        (r"@import\s+(?:url\s*\(|['\"]\s*(?:https?:)?//)", "@import externe"),
        (r"\bfetch\s*\(", "appel fetch()"),
    )
    for regex, label in forbidden_patterns:
        if re.search(regex, html_outside_json, re.IGNORECASE):
            raise ValueError(f"Référence réseau ou URL externe interdite détectée hors bloc JSON : {label}")

    html_out = output_html or (repo_root / "Cartographie" / DEFAULT_HTML_NAME)
    html_out.write_text(compiled_html, encoding="utf-8", newline="\n")
    metrics["html_bytes"] = html_out.stat().st_size
    return html_out, metrics


def main() -> int:
    """Point d'entrée CLI pour compiler la page web autonome du PRD."""
    parser = argparse.ArgumentParser(
        description="Compile la page HTML autonome dédiée au PRD maître."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Racine du dépôt Agentique.",
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=None,
        help="Chemin optionnel vers prd-web-data.json.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Chemin de sortie HTML optionnel.",
    )
    args = parser.parse_args()

    out_path, metrics = compile_prd_web(
        args.repo_root.resolve(),
        output_html=args.output.resolve() if args.output else None,
        data_path=args.data.resolve() if args.data else None,
    )
    print(
        f"Compilation PRD Web réussie -> {out_path} ({metrics['html_bytes']} octets) : "
        f"{metrics['parties']} parties, {metrics['chapters']} chapitres, "
        f"{metrics['families']} familles, {metrics['themes']} thèmes, "
        f"{metrics['annexes']} annexes, {metrics['lookup_nodes']} nœuds indexés."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
