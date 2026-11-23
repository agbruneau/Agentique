# SPDX-License-Identifier: MIT
"""Suite de tests automatises du gabarit PDF partage (gabarit-pdf/)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pymupdf
import pytest

GABARIT_DIR = Path(__file__).resolve().parent
REPO_ROOT = GABARIT_DIR.parent
if str(GABARIT_DIR) not in sys.path:
    sys.path.insert(0, str(GABARIT_DIR))

from compile_pdf import (  # noqa: E402
    CATALOG_PATH,
    TEMPLATE_PATH,
    compile_markdown_to_pdf,
    compile_volume,
    get_volume_config,
    load_catalog,
)
from postprocess_typst import postprocess_typst_body  # noqa: E402
from preprocess_md import (  # noqa: E402
    inject_rendered_diagrams,
    preprocess_markdown,
)


def _assert_book_page_geometry(pdf_path: Path) -> pymupdf.Document:
    doc = pymupdf.open(pdf_path)
    assert len(doc) >= 4
    r = doc[0].rect
    assert abs(r.width / 72.0 - 6.14) < 0.02, f"Largeur inattendue: {r.width / 72.0:.3f}in"
    assert abs(r.height / 72.0 - 9.21) < 0.02, f"Hauteur inattendue: {r.height / 72.0:.3f}in"
    return doc


def test_catalog_covers_all_eight_volumes_and_sources_exist() -> None:
    assert TEMPLATE_PATH.is_file()
    assert CATALOG_PATH.is_file()
    catalog = load_catalog()
    vols = catalog["volumes"]
    assert [v["id"] for v in vols] == [str(i) for i in range(1, 9)]

    for v in vols:
        src = REPO_ROOT / v["source_md"]
        pdf = REPO_ROOT / v["default_pdf"]
        assert src.is_file(), f"Markdown manquant pour volume {v['id']}: {src}"
        assert pdf.is_file(), f"PDF de reference manquant pour volume {v['id']}: {pdf}"
        assert v["title"].strip()
        assert v["author"].strip()

    assert get_volume_config("8")["slug"] == "8 - Manuel"
    assert get_volume_config("8 - Manuel")["id"] == "8"
    assert get_volume_config("memoire")["id"] == "5"
    with pytest.raises(KeyError):
        get_volume_config("99 - inexistant")


def test_preprocess_markdown_all_eight_volumes_structure() -> None:
    expected_starts = {
        "1": "# Présentation des cinq livres",
        "2": "# Historique des versions",
        "3": "# À propos de cette édition",
        "4": "# Liminaire",
        "5": "# Liminaire",
        "6": "# Liminaire",
        "7": "# Liminaire",
        "8": "# Liminaire",
    }
    for vid, expected_prefix in expected_starts.items():
        cfg = get_volume_config(vid)
        src = REPO_ROOT / cfg["source_md"]
        clean, _ = preprocess_markdown(
            src.read_text(encoding="utf-8"),
            repo_root=REPO_ROOT,
            md_source_path=src,
            options=cfg,
        )
        assert clean.startswith(expected_prefix), f"Vol {vid} commence par: {clean[:80]!r}"
        assert "\n# Table des matières\n" not in "\n" + clean, f"TDM statique residuelle dans Vol {vid}"

        # Verifier que toutes les images referencees existent sous REPO_ROOT
        for img_rel in re.findall(r"!\[[^\]]*\]\((/[^)\n]+)\)", clean):
            assert (REPO_ROOT / img_rel.lstrip("/")).is_file(), f"Image introuvable Vol {vid}: {img_rel}"


def test_inject_rendered_diagrams_inserts_without_duplication(tmp_path: Path) -> None:
    rendus = tmp_path / "Diagrammes" / "rendus"
    rendus.mkdir(parents=True)
    (rendus / "Figure-01.0 - Intro.svg").write_text("<svg/>", encoding="utf-8")
    (rendus / "Figure-01.0 - Intro.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    (rendus / "Fig-02 - Flux.png").write_bytes(b"\x89PNG\r\n\x1a\n")

    md = (
        "Paragraphe initial.\n\n"
        "***Figure 1.0** — Premier schema.*\n\n"
        "![Deja present](/Diagrammes/rendus/Fig-02 - Flux.png)\n\n"
        "*Fig. 2. – Second schema.*\n"
    )
    out, count = inject_rendered_diagrams(md, rendus, tmp_path)
    assert count == 1
    assert "![Figure 1.0](/Diagrammes/rendus/Figure-01.0 - Intro.svg)\n\n***Figure 1.0**" in out
    assert out.count("Fig-02 - Flux.png") == 1


def test_postprocess_typst_covers_all_collection_conventions() -> None:
    raw = (
        "#emph[#strong[Figure 1.0] — Schema Vol 1]\n\n"
        "#emph[Fig. 2. – Schema Vol 3 a 6]\n\n"
        "#emph[Figure 3 — Schema Vol 7 et 8]\n\n"
        "Cout 15,5 \\$ US, 20 \\$ CA, 100 %, 3 309 o, $0\\,94^(10)$ -> 5 - Memoire et 8 - Manuel.\n\n"
        "#figure(\n"
        "  align(center)[#table(\n"
        "    columns: 2,\n"
        "    align: (auto,right,),\n"
        "    table.header([ID], [Details],),\n"
        "    [`CH01-01`], [Flux d’authentification `OpaStaticCheckError`],\n"
        "  )]\n"
        "  , kind: table\n"
        "  )\n\n"
        "#emph[Tableau 1 — Synthese courte.]\n\n"
        '#box(image("/8 - Manuel/diagrammes/rendus/Fig-01.svg", alt: "Schema"))\n\n'
        "= Bibliographie générale consolidée\n"
        '- #link("https://example.org/a-b/c")\n'
    )
    out = postprocess_typst_body(raw)
    assert out.count("#align(center)") == 4
    assert '$0","94^(10)$' in out
    assert "15,5\u00a0\\$\u00a0US" in out
    assert "20\u00a0\\$\u00a0CA" in out
    assert "100\u00a0%" in out and "3\u00a0309\u00a0o" in out
    assert "5\u00a0-\u00a0Memoire" in out and "8\u00a0-\u00a0Manuel" in out
    assert '#box(image("/8 - Manuel/diagrammes/rendus/Fig-01.svg"' in out
    assert " → " in out
    assert "d’\u200bauthentification" in out
    assert "`Opa\u200bStatic\u200bCheck\u200bError`" in out
    assert "#block(width: 100%, breakable: false)[" in out
    assert "#set par(justify: false, leading: 0.56em, spacing: 0.45em)" in out
    assert (
        '#link("https://example.org/a-b/c")[#text(hyphenate: false)[#("https://example.\u200borg/\u200ba-\u200bb/\u200bc")]]'
        in out
    )


def test_compile_synthetic_showcase_all_features(tmp_path: Path) -> None:
    long_code = "\n".join(f"line_{i:02d} = 'valeur_deterministe_{i:02d}'" for i in range(1, 66))
    long_quote = "\n>\n".join(
        f"> Paragraphe d'encadre numero {i} verifiant la coupure de page propre sans debordement sur plusieurs lignes de prose technique detaillee."
        for i in range(1, 32)
    )
    md = (
        "# Liminaire — Synthèse de validation\n\n"
        "Texte de démonstration avec 99,5 % de précision et 15,5 $ CA -> `DeterministicHarness`.\n\n"
        "> Encadré court avec `code_inline` sur fond blanc.\n\n"
        "# Livre I — Coopérer\n\n"
        "## 1 · Premier chapitre numéroté\n\n"
        "| Colonne A | Colonne B | Statut |\n"
        "|---|---|---|\n"
        "| `EXIG-01` | Contrôle d'authentification `OpaStaticCheckError` | Conforme |\n\n"
        "*Tableau 1.1 — Vérification de tableau.*\n\n"
        "```python\n"
        f"{long_code}\n"
        "LINE_65_SENTINEL = True\n"
        "```\n\n"
        "# Partie II — Encadrés longs\n\n"
        "## Chapitre 02 — Pagination des citations longues\n\n"
        f"{long_quote}\n\n"
        "# Annexes — Références\n\n"
        "## Annexe A — Bibliographie\n\n"
        "### Bibliographie classée des sources intégrales vérifiées\n\n"
        "- <https://example.org/spec/agentic-reference-2027>\n"
    )

    # 1. Avec badge de licence
    pdf_with_badge = tmp_path / "showcase-badge.pdf"
    compile_markdown_to_pdf(
        md,
        pdf_with_badge,
        {
            "title": "Ouvrage de démonstration",
            "subtitle": "Validation intégrale du gabarit partagé",
            "author": "André-Guy Bruneau, M.Sc IT",
            "pub_date": "janvier 2027",
            "freeze_date": "2 décembre 2026",
            "license_badge": "CC BY 4.0",
            "numbered_h2_chapters": True,
        },
        typst_root=REPO_ROOT,
    )
    doc = _assert_book_page_geometry(pdf_with_badge)
    full_text = " ".join("\n".join(page.get_text() for page in doc).replace("’", "'").split())
    assert "CC BY 4.0" in doc[0].get_text()
    assert "Table des matières" in doc[2].get_text()
    assert "line_01" in full_text and "LINE_65_SENTINEL" in full_text
    assert "Paragraphe d'encadre numero 31" in full_text
    doc.close()

    # 2. Sans badge de licence (ex. Vol 1 et Vol 6)
    pdf_no_badge = tmp_path / "showcase-nobadge.pdf"
    compile_markdown_to_pdf(
        md,
        pdf_no_badge,
        {
            "title": "Ouvrage sans badge",
            "subtitle": "Vérification de l'omission propre du badge",
            "author": "André-Guy Bruneau, M.Sc IT",
            "pub_date": "novembre 2026",
            "license_badge": None,
            "numbered_h2_chapters": True,
        },
        typst_root=REPO_ROOT,
    )
    doc2 = _assert_book_page_geometry(pdf_no_badge)
    assert "CC BY 4.0" not in doc2[0].get_text()
    doc2.close()


def test_compile_volume_safety_guard() -> None:
    with pytest.raises(ValueError, match="--in-place"):
        compile_volume("8")


def test_compile_real_volume_8_matches_reference(tmp_path: Path) -> None:
    out_pdf = tmp_path / "8 - Manuel.pdf"
    compile_volume("8", output_path=out_pdf)
    doc = _assert_book_page_geometry(out_pdf)
    ref_doc = pymupdf.open(REPO_ROOT / "0 - PDF-MD" / "8 - Manuel.pdf")
    try:
        assert abs(len(doc) - len(ref_doc)) <= 2, f"Ecart pages Vol 8: {len(doc)} vs ref {len(ref_doc)}"
        cover_txt = " ".join(doc[0].get_text().replace("’", "'").split())
        assert "Ingénierie exécutable de l'entreprise agentique" in cover_txt
        assert "CC BY 4.0" in cover_txt
        title_txt = " ".join(doc[1].get_text().replace("\u00a0", " ").split())
        assert "8 - Manuel/" in title_txt and "trousse/" in title_txt
        assert "Table des matières" in doc[2].get_text()
    finally:
        doc.close()
        ref_doc.close()


def test_compile_real_volume_5_full_legacy_volume(tmp_path: Path) -> None:
    out_pdf = tmp_path / "5 - Memoire.pdf"
    compile_volume("5", output_path=out_pdf)
    doc = _assert_book_page_geometry(out_pdf)
    try:
        assert len(doc) >= 80
        cover_txt = " ".join(doc[0].get_text().split())
        assert "Interopérabilité et Orchestration en Entreprise Agentique" in cover_txt
        assert "Table des matières" in doc[2].get_text()
    finally:
        doc.close()


@pytest.mark.parametrize("vid", ["1", "2", "3", "4", "6", "7"])
def test_compile_real_volume_excerpts_all_structural_variants(vid: str, tmp_path: Path) -> None:
    cfg = get_volume_config(vid)
    src = REPO_ROOT / cfg["source_md"]
    # Prendre un extrait substantiel (debut du volume : preambule + premiers chapitres)
    excerpt_lines = src.read_text(encoding="utf-8").splitlines(keepends=True)[:450]
    excerpt_md = "".join(excerpt_lines)
    # Fermer un eventuel bloc de code coupe a la ligne 450
    if excerpt_md.count("```") % 2 == 1:
        excerpt_md += "\n```\n"

    out_pdf = tmp_path / f"vol-{vid}-excerpt.pdf"
    compile_markdown_to_pdf(
        excerpt_md,
        out_pdf,
        cfg,
        md_source_path=src,
        typst_root=REPO_ROOT,
    )
    doc = _assert_book_page_geometry(out_pdf)
    try:
        assert cfg["title"].split()[0] in doc[0].get_text()
        assert "Table des matières" in doc[2].get_text()
    finally:
        doc.close()
