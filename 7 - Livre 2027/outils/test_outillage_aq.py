"""Tests TDD de l'outillage deterministe G1, G3, annexes et assemblage du Livre 2027."""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
import sys
import zlib
from pathlib import Path

import pytest

TOOLS_DIR = Path(__file__).resolve().parent
REAL_BOOK_DIR = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from echantillon_aq import draw_stratified_sample  # noqa: E402
from genere_annexes import build_annexes  # noqa: E402
from verifie_manuscrit import check_manuscrit, count_prose_words  # noqa: E402

UNITS_NARRATIVES = [
    "00-liminaire",
    "ch01",
    "ch02",
    "ch03",
    "ch04",
    "ch05",
    "ch06",
    "ch07",
    "ch08",
    "ch09",
    "ch10",
    "ch11",
    "ch12",
]


def _make_words(prefix: str, count: int) -> str:
    """Genere un paragraphe synthetique sans collision n-gramme ni codes bannis."""
    tokens = [f"{prefix}mot{i}" for i in range(count)]
    return " ".join(tokens)


def _source_filename(unit_id: str) -> str:
    if unit_id == "00-liminaire":
        return "ch00-sources.md"
    return f"{unit_id}-sources.md"


def _build_valid_unit_text(unit_meta: dict, extra_body: str = "", include_vigilance: bool = False) -> str:
    """Construit une unite Markdown conforme a CA-01..CA-06 et CA-10."""
    uid = unit_meta["id"]
    figs = unit_meta.get("figures", [])
    fig_lines = "\n".join(
        f"La figure {fid} illustre l'architecture attendue.\n\n![Légende de {fid}](../../diagrammes/rendus/{fid}.svg)\n\nL'analyse de {fid} confirme la séparation requise [1]."
        for fid in figs
    )

    if uid == "00-liminaire":
        head = (
            f"# {unit_meta['title']}\n\n"
            "*Question directrice :* Pourquoi la viabilité tient-elle au tissu conjonctif ?\n\n"
            "L'entreprise agentique relie ses outils et ses superviseurs [1].\n\n"
        )
        sections = (
            "## 0.1 De l'humain intégrateur au tissu conjonctif\n\n"
            "Les îlots applicatifs cèdent la place à des contrats ouverts [1].\n\n"
            "## 0.2 Les six dimensions de l'interopérabilité\n\n"
            "La frontière entre qui parle et qui en répond demeure nette [2].\n\n"
            "## 0.3 Orchestration et discipline de retenue\n\n"
            "| Rupture | Héritage 2024 | Cible 2027 |\n"
            "|---|---|---|\n"
            "| Contrôle | Invite libre | Noyau typé |\n\n"
            "> **Cinq critères permanents d'évaluation architecturale**\n"
            "> 1. Neutralité de gouvernance.\n\n"
            "## 0.4 Progression et règle du maillon le plus élevé\n\n"
            "Quatre parcours guident la lecture selon le mandat [1].\n\n"
            "## 0.5 Hygiène probatoire et date de gel\n\n"
            "La date de gel des faits est fixée au 31 décembre 2026 [2].\n\n"
            "## 0.6 Colophon d'intégrité\n\n"
            "Rédaction et vérification automatisées sur cahier des charges humain [1].\n\n"
            f"{fig_lines}\n\n"
        )
        tail = "Transition vers la première partie de l'ouvrage.\n"
    else:
        num = int(uid[2:])
        head = (
            f"# {unit_meta['title']}\n\n"
            f"*Question directrice : Question du chapitre {num} ?*\n\n"
            f"Le cas concret du chapitre {num} expose un défi d'exploitation [1].\n\n"
        )
        vig_block = ""
        if include_vigilance and uid == "ch10":
            vig_block = (
                "La ligne directrice sur l'IA de l'AMF prévue pour le 1er mai 2027 reste en statut bloqué [2]. "
                "L'Annexe III de l'EU AI Act entrera en application le 2 décembre 2027 selon le calendrier publié [2]. "
                "L'interdiction des rétrofacturations de commissions est fixée au 1er octobre 2028 [3].\n\n"
            )
        if include_vigilance and uid == "ch02":
            vig_block = (
                "Une estimation d'analyste prévoit l'abandon de plus de 40 % des initiatives agentiques d'ici fin 2027 [1]. "
                "La dispersion des tailles de marché atteint une médiane de 15,5 G\\$ US en 2027 [2]. "
                "La loi de Lusser donne une fiabilité composée de 53,9 % sur dix étapes à 94 % [1]. "
                "Les dépenses d'investissement annoncées pour 2026 atteignent 720 à 740 G\\$ US [2].\n\n"
            )
        sections = (
            f"## {num}.1 Première section analytique\n\n"
            f"La mesure empirique établit un écart mesurable sur banc d'essai [1].\n\n"
            f"{vig_block}"
            f"## {num}.2 Deuxième section réglementaire\n\n"
            f"La Loi 25 et le BSIF encadrent l'imputabilité juridique des décisions [2].\n\n"
            f"## {num}.3 Troisième section technique prospective\n\n"
            f"La transition post-quantique ML-DSA et les protocoles IETF WIMSE préparent 2030 [3].\n\n"
            f"## {num}.4 Quatrième section d'application\n\n"
            f"Les contrats de données bornent l'exécution durable des tâches longues [1].\n\n"
            f"{fig_lines}\n\n"
        )
        tail = (
            f"> **Trois arbitrages sans regret — Chapitre {num}**\n"
            "> 1. Exiger des contrats typés.\n\n"
            "Paragraphe final de transition vers le chapitre suivant.\n"
        )

    base = head + sections + (f"{extra_body}\n\n" if extra_body else "") + tail
    cur_words = count_prose_words(base)
    target = unit_meta["target_words"]
    if cur_words < unit_meta["min_words"]:
        needed = target - cur_words
        # Ajouter des paragraphes espaces pour rester sous 18 % de puces et fournir assez de paragraphes a G3
        chunks = []
        per_para = 150
        idx = 0
        while needed > 0:
            take = min(per_para, needed)
            cat_tag = ["mesure empirique de performance [1]", "obligation juridique réglementaire [2]", "norme technique prospective PQC 2030 [3]"][idx % 3]
            body = _make_words(f"{uid}p{idx}", max(1, take - 7))
            chunks.append(f"Paragraphe {idx} portant sur {cat_tag} : {body}.")
            needed -= take
            idx += 1
        base = head + sections + ("\n\n".join(chunks)) + "\n\n" + (f"{extra_body}\n\n" if extra_body else "") + tail
    return base


def _make_valid_png_bytes(width: int = 16, height: int = 16) -> bytes:
    """Genere un PNG RGBA valide minimal en stdlib pure."""
    def _chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack("!I", len(data)) + tag + data + struct.pack("!I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack("!IIBBBBB", width, height, 8, 6, 0, 0, 0)
    raw_scanlines = b"".join(b"\x00" + (b"\x1b\x36\x5d\xff" * width) for _ in range(height))
    idat = zlib.compress(raw_scanlines)
    return b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", idat) + _chunk(b"IEND", b"")


def _create_populated_book(tmp_path: Path, include_vigilance: bool = True) -> Path:
    """Cree un depot complet valide en memoire sur disque dans tmp_path."""
    book_dir = tmp_path / "7 - Livre 2027"
    corpus_dir = tmp_path / "0 - MD"
    corpus_dir.mkdir(parents=True)
    corpus_file = corpus_dir / "1 - Compendium 2026.md"
    corpus_file.write_text(
        "# Compendium\n\n"
        "Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application.\n"
        "Une phrase du corpus interne servant de temoin pour la detection exacte de douze mots consecutifs.\n",
        encoding="utf-8",
    )

    shutil.copytree(REAL_BOOK_DIR / "specs", book_dir / "specs")
    shutil.copytree(REAL_BOOK_DIR / "registre", book_dir / "registre")

    manifest_path = book_dir / "specs" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["internal_corpus_paths"] = ["../0 - MD/1 - Compendium 2026.md"]
    manifest["stylistic_benchmarks_for_gauntlet"] = []
    manifest["stylistic_benchmark_sections"] = {}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # Corpus L+ reel avec empreintes SHA-256 exactes couvrant RQ1..RQ6
    lplus_dir = book_dir / "recherche" / "corpus_l_plus"
    lplus_dir.mkdir(parents=True)
    rqs = ["RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "RQ6"]
    sources_entries = []
    for i in range(1, 13):
        sid = f"SRC-{i:03d}"
        txt_rel = f"recherche/corpus_l_plus/{sid}.txt"
        txt_path = book_dir / txt_rel
        content = f"Texte integral primaire {sid}. Mesures, normes et dates verifiees jusqu'au 31 decembre 2026.\n" * 5
        txt_path.write_text(content, encoding="utf-8")
        digest = hashlib.sha256(txt_path.read_bytes()).hexdigest()
        assigned_rqs = [rqs[(i - 1) % 6], rqs[i % 6]]
        sources_entries.append(
            {
                "source_id": sid,
                "category": "empirique" if i % 3 == 1 else ("juridique" if i % 3 == 2 else "technique"),
                "peer_reviewed": True,
                "title": f"Source primaire {sid}",
                "authors": "Auteur Test",
                "year": 2026,
                "publication_date": "2026-10-15",
                "venue_or_issuer": "Open Archive",
                "identifier": f"arXiv:2610.{1000+i:05d}",
                "url": f"https://arxiv.org/abs/2610.{1000+i:05d}",
                "status": "L+",
                "metadata_only": False,
                "aacods_score": 11.0,
                "research_axes": sorted(set(assigned_rqs)),
                "local_txt_path": txt_rel,
                "sha256": digest,
                "byte_length": len(content.encode("utf-8")),
                "word_count": len(content.split()),
            }
        )
    # Assurer >= 6 etudes sur chaque RQ1..RQ6
    for idx, rq in enumerate(rqs):
        for s in sources_entries:
            if rq not in s["research_axes"] and len([x for x in sources_entries if rq in x["research_axes"]]) < 6:
                s["research_axes"].append(rq)

    manifeste_sources = {
        "protocol_id": "MLR-PRISMA-SCR-LIVRE-2027-V1.2",
        "freeze_date": "2026-12-31",
        "metadata_only_pct": 0.0,
        "sources": sources_entries,
    }
    (book_dir / "recherche" / "manifeste-sources-sha256.json").write_text(
        json.dumps(manifeste_sources, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (book_dir / "recherche" / "registre-statut-f.json").write_text(
        json.dumps({"blocked": []}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Registres passes en statut_preuve = "l_plus"
    ancres_path = book_dir / "registre" / "ancres-chronologiques.json"
    ancres = json.loads(ancres_path.read_text(encoding="utf-8"))
    for idx, a in enumerate(ancres["anchors"]):
        a["statut_preuve"] = "l_plus"
        a["source_l_plus_id"] = f"SRC-{(idx % 12) + 1:03d}"
        a["label"] = a["label"].replace("25 M$ CA", "25 M\\$ CA")
    ancres_path.write_text(json.dumps(ancres, ensure_ascii=False, indent=2), encoding="utf-8")

    faits_path = book_dir / "registre" / "faits-empiriques.json"
    faits = json.loads(faits_path.read_text(encoding="utf-8"))
    for idx, f in enumerate(faits["facts"]):
        f["statut_preuve"] = "l_plus"
        f["source_l_plus_id"] = f"SRC-{(idx % 12) + 1:03d}"
    faits_path.write_text(json.dumps(faits, ensure_ascii=False, indent=2), encoding="utf-8")

    # 13 dossiers sources/chNN-sources.md
    src_dir = book_dir / "sources"
    src_dir.mkdir(parents=True)
    for uid in UNITS_NARRATIVES:
        sname = _source_filename(uid)
        (src_dir / sname).write_text(
            f"# Sources — {uid}\n\n"
            "Date de gel des faits : 31 décembre 2026\n\n"
            "### [1] SRC-001 — Etude empirique primaire\nRésumé vérifié sur texte intégral.\n\n"
            "### [2] SRC-002 — Texte réglementaire primaire\nRésumé vérifié sur texte intégral.\n\n"
            "### [3] SRC-003 — Spécification technique primaire\nRésumé vérifié sur texte intégral.\n",
            encoding="utf-8",
        )

    # 23 rendus de figures factices valides
    rendus_dir = book_dir / "diagrammes" / "rendus"
    rendus_dir.mkdir(parents=True)
    for fmeta in manifest["figures"]:
        fid = fmeta["id"]
        if fmeta["engine"] == "puml":
            (rendus_dir / f"{fid}.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50"><rect width="10" height="10"/></svg>',
                encoding="utf-8",
            )
        else:
            (rendus_dir / f"{fid}.png").write_bytes(_make_valid_png_bytes())

    # Ecriture des 13 unites narratives
    for u in manifest["units"]:
        if u["kind"] in {"frontmatter", "chapter"}:
            out = book_dir / u["file"]
            out.parent.mkdir(parents=True, exist_ok=True)
            extra = ""
            if u["id"] == "ch01":
                extra = "La croissance annuelle du calcul atteint au moins 10× par an (~1,5× matériel, ~3× inférence, ~2,5× dépenses) [1]. En août 2026 (2026-08), l'article 50 de l'EU AI Act entre en application [2]."
            elif u["id"] == "ch06":
                extra = "L'étude MAP observe 68 % d'agents à au plus 10 étapes et 16 cas sur 20 en flux structuré [1]. La taxonomie MAST mesure 41 % à 86,7 % d'échecs sur 1 600 traces et 7 cadriciels (14 modes) [1]."
            elif u["id"] == "ch07":
                extra = "Les certificats TLS passeront à 100 jours le 15 mars 2027 et à 47 jours le 15 mars 2029, avant la fenêtre post-quantique G7 2030–2035 [3]."
            elif u["id"] == "ch08":
                extra = "Sur le banc AgentDojo, CaMeL résout 77 % des tâches contre 84 % sans défense [1]."
            elif u["id"] == "ch09":
                extra = "La ligne directrice B-15 (portée 3) vise fin 2028 [2]."
            elif u["id"] == "ch10":
                extra = (
                    "L'article 12.1 de la Loi 25 est en vigueur dès 2026 (sanctions jusqu'à 25 M\\$ CA ou 4 %) [2]. "
                    "La ligne directrice E-23 du BSIF entre en vigueur le 1er mai 2027, et l'Annexe I de l'EU AI Act le 2 août 2028 [2]. "
                    "La révision statutaire des lois financières canadiennes est prévue le 30 juin 2033 [2]."
                )
            elif u["id"] == "ch11":
                extra = "Selon Stanford HAI 2026, l'emploi des développeurs de 22 à 25 ans recule de près de 20 % [1]."
            elif u["id"] == "ch12":
                extra = "Les signatures ML-DSA-65 atteignent 3 309 octets (~52×) et ML-DSA-87 4 627 octets (~72×) face aux 64 octets elliptiques [3]."
            out.write_text(_build_valid_unit_text(u, extra_body=extra, include_vigilance=include_vigilance), encoding="utf-8")

    # Generer les 3 annexes deterministes
    build_annexes(book_dir)
    return book_dir


@pytest.fixture()
def tmp_book(tmp_path: Path) -> Path:
    return _create_populated_book(tmp_path, include_vigilance=True)


def test_word_count_excludes_yaml_biblio_code_and_urls() -> None:
    sample = (
        "---\n"
        "title: Titre ignore dans YAML\n"
        "author: Auteur ignore\n"
        "---\n\n"
        "Voici l'analyse architecturale de [l'architecture ouverte](https://example.org/tres/longue/url/avec/des/mots) "
        "et une référence nue https://autre-exemple.org/chemin/long ainsi que <https://encadree.org/test>.\n\n"
        "```python\n"
        "def ignored_code_block_words():\n"
        "    return 'plusieurs mots dans un bloc de code cloture'\n"
        "```\n\n"
        "~~~\n"
        "autre bloc tilde ignore\n"
        "~~~\n\n"
        "<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->\n"
        "Liste brute de cinquante mots completement exclus du decompte officiel de l annexe C.\n"
        "<!-- BIBLIOGRAPHIE_BRUTE_FIN -->\n\n"
        "Deux mots finaux.\n"
    )
    # Prose attendue : "Voici l'analyse architecturale de l'architecture ouverte et une référence nue ainsi que Deux mots finaux."
    # = 15 mots
    assert count_prose_words(sample) == 15


def test_clean_populated_book_passes_strict(tmp_book: Path) -> None:
    assert check_manuscrit(tmp_book, sources_only=True) == []
    assert check_manuscrit(tmp_book, strict=True) == []


def test_forbidden_codes_and_unescaped_dollars_detected(tmp_book: Path) -> None:
    ch01 = tmp_book / "manuscrit" / "01 - Partie I" / "Chapitre 01 - Apres le copilote, l industrialisation cognitive.md"
    txt = ch01.read_text(encoding="utf-8")
    txt = txt.replace(
        "Paragraphe 0",
        "Conformement a CAP-001 et Classe 1 [1], le budget atteint 15,5 G$ US. Paragraphe 0",
        1,
    )
    ch01.write_text(txt, encoding="utf-8")

    errors = check_manuscrit(tmp_book, strict=True)
    assert any("CA-02" in e for e in errors)
    assert any("CA-06" in e for e in errors)


def test_dollar_math_rejected_and_backslash_math_accepted(tmp_book: Path) -> None:
    ch02 = tmp_book / "manuscrit" / "01 - Partie I" / "Chapitre 02 - L epreuve des mesures.md"
    txt = ch02.read_text(encoding="utf-8")
    txt = txt.replace(
        "Paragraphe 0",
        "Formule valide \\(0{,}94^{10}\\) ici.\n\nFormule rejetee $0{,}94^{10}$ ici.\n\nParagraphe 0",
        1,
    )
    ch02.write_text(txt, encoding="utf-8")

    errors = check_manuscrit(tmp_book, strict=True)
    assert any("CA-06" in e and "$0{,}94" in e for e in errors)
    assert not any("CA-06" in e and "\\(0{,}94" in e for e in errors)


def test_12gram_ignores_quoted_statute_titles_only(tmp_book: Path) -> None:
    ch10 = tmp_book / "manuscrit" / "04 - Partie IV" / "Chapitre 10 - Le laboratoire reglemente.md"
    orig = ch10.read_text(encoding="utf-8")

    # Cas 1 : segment <= 40 mots entre guillemets francais suivi de [1] -> DOIT passer
    quoted = orig.replace(
        "Paragraphe 0",
        "La loi citee est « Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application » [1]. Paragraphe 0",
        1,
    )
    ch10.write_text(quoted, encoding="utf-8")
    errors_quoted = check_manuscrit(tmp_book, strict=True, unit_id="ch10")
    assert not any("CA-03" in e or "Loi sur la protection" in e for e in errors_quoted)

    # Cas 2 : meme titre de loi long NON guillemete et NON cite -> DOIT echouer CA-03
    unquoted = orig.replace(
        "Paragraphe 0",
        "Selon la Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application, l'audit est requis [1]. Paragraphe 0",
        1,
    )
    ch10.write_text(unquoted, encoding="utf-8")
    errors_unquoted = check_manuscrit(tmp_book, strict=True, unit_id="ch10")
    assert any("CA-03" in e for e in errors_unquoted)

    # Cas 3 : entre guillemets mais SANS renvoi [n] -> DOIT echouer CA-03
    no_ref = orig.replace(
        "Paragraphe 0",
        "Texte repris : « Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application » sans renvoi. Paragraphe 0",
        1,
    )
    ch10.write_text(no_ref, encoding="utf-8")
    errors_no_ref = check_manuscrit(tmp_book, strict=True, unit_id="ch10")
    assert any("CA-03" in e for e in errors_no_ref)


def test_registry_accuracy_ca07_detects_numeric_and_date_drift(tmp_book: Path) -> None:
    # Derives chiffrees (Lusser 53,9 % -> 48,2 %) et temporelle (BSIF E-23 1er mai 2027 -> 1er juin 2027)
    ch02 = tmp_book / "manuscrit" / "01 - Partie I" / "Chapitre 02 - L epreuve des mesures.md"
    txt2 = ch02.read_text(encoding="utf-8").replace("53,9 %", "48,2 %")
    ch02.write_text(txt2, encoding="utf-8")

    ch10 = tmp_book / "manuscrit" / "04 - Partie IV" / "Chapitre 10 - Le laboratoire reglemente.md"
    txt10 = ch10.read_text(encoding="utf-8").replace("1er mai 2027", "1er juin 2027")
    ch10.write_text(txt10, encoding="utf-8")

    errors = check_manuscrit(tmp_book, strict=True)
    ca07_errors = [e for e in errors if "CA-07" in e]
    assert len(ca07_errors) >= 2


def test_two_seeds_produce_disjoint_60_item_samples(tmp_book: Path) -> None:
    s1 = draw_stratified_sample(tmp_book, seed=202701, exclude_ids=set())
    excluded = {x["claim_loc"] for x in s1} | {x["paragraph_loc"] for x in s1}
    s2 = draw_stratified_sample(tmp_book, seed=202702, exclude_ids=excluded)

    assert len(s1) == 60
    assert len(s2) == 60
    assert {x["claim_loc"] for x in s1}.isdisjoint({x["claim_loc"] for x in s2})
    assert {x["paragraph_loc"] for x in s1}.isdisjoint({x["paragraph_loc"] for x in s2})

    for sample in (s1, s2):
        assert sum(1 for x in sample if x["category"] == "empirique") == 25
        assert sum(1 for x in sample if x["category"] == "juridique") == 20
        assert sum(1 for x in sample if x["category"] == "prospectif_technique") == 15
        assert all(sum(1 for x in sample if x["unit"] == u) >= 2 for u in UNITS_NARRATIVES)

    # Determinisme et points de vigilance prd.md § 7 en passe 1
    assert draw_stratified_sample(tmp_book, seed=202701, exclude_ids=set()) == s1
    s1_text = " ".join(x["text"].lower() for x in s1)
    assert "amf" in s1_text
    assert "40 %" in s1_text
    assert "annexe iii" in s1_text
    assert "rétrofacturation" in s1_text


def test_sources_only_catches_sha256_and_metadata_only_and_date(tmp_book: Path) -> None:
    manifeste_path = tmp_book / "recherche" / "manifeste-sources-sha256.json"
    m = json.loads(manifeste_path.read_text(encoding="utf-8"))
    m["metadata_only_pct"] = 5.0
    m["sources"][0]["sha256"] = "0" * 64
    m["sources"][1]["publication_date"] = "2027-02-01"
    m["sources"][2]["status"] = "F"
    manifeste_path.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")

    errors = check_manuscrit(tmp_book, sources_only=True)
    assert any("METADATA_ONLY" in e or "metadata_only_pct" in e for e in errors)
    assert any("CA-09" in e or "sha256" in e.lower() for e in errors)
    assert any("2026-12-31" in e or "gel" in e.lower() for e in errors)
    assert any("statut F" in e or "status" in e for e in errors)


def test_genere_annexes_pre_post_qa_and_ca17(tmp_book: Path) -> None:
    # Avant peuplement de ancrage/ et aq/, les 3 annexes sont deja dans les bornes et sans $ nu
    annex_a = tmp_book / "manuscrit" / "05 - Annexes" / "Annexe A - Glossaire raisonne.md"
    annex_b = tmp_book / "manuscrit" / "05 - Annexes" / "Annexe B - Chronologie consolidee 2026-2035.md"
    annex_c = tmp_book / "manuscrit" / "05 - Annexes" / "Annexe C - Methodologie et bilan d assurance qualite.md"

    assert 1656 <= count_prose_words(annex_a.read_text(encoding="utf-8")) <= 1944
    assert 1104 <= count_prose_words(annex_b.read_text(encoding="utf-8")) <= 1296
    assert 920 <= count_prose_words(annex_c.read_text(encoding="utf-8")) <= 1080

    # Peupler ancrage/ et aq/ puis regenerer
    anc_dir = tmp_book / "ancrage"
    anc_dir.mkdir()
    for uid in UNITS_NARRATIVES:
        sname = "ch00-ancrage.md" if uid == "00-liminaire" else f"{uid}-ancrage.md"
        (anc_dir / sname).write_text(
            f"# Ancrage {uid}\n\nTotal : 10 / 10 (100 %) supporté, 0 non supporté.\n",
            encoding="utf-8",
        )
    aq_dir = tmp_book / "aq"
    aq_dir.mkdir()
    s1 = draw_stratified_sample(tmp_book, seed=202701, exclude_ids=set())
    (aq_dir / "recollation-seed-202701.json").write_text(json.dumps(s1, ensure_ascii=False), encoding="utf-8")
    (aq_dir / "recollation-seed-202701.md").write_text("# Recollation 1\n\nScore : 60/60 (100 %).\n", encoding="utf-8")
    (aq_dir / "gauntlet-log.md").write_text("# Gauntlet\n\n" + "\n".join(UNITS_NARRATIVES), encoding="utf-8")

    build_annexes(tmp_book)
    annex_c_text = annex_c.read_text(encoding="utf-8")
    assert "60/60" in annex_c_text or "60 / 60" in annex_c_text
    assert 920 <= count_prose_words(annex_c_text) <= 1080
    assert check_manuscrit(tmp_book, strict=True) == []

    # Modification manuelle hors registre -> CA-17 echoue
    annex_a.write_text(annex_a.read_text(encoding="utf-8") + "\nAjout manuel interdit.", encoding="utf-8")
    errors = check_manuscrit(tmp_book, strict=True)
    assert any("CA-17" in e for e in errors)


def test_assemble_livre_generates_md_html_pdf(tmp_book: Path) -> None:
    assemble_script = TOOLS_DIR / "assemble_livre.py"
    res = subprocess.run(
        [sys.executable, str(assemble_script), "--root", str(tmp_book), "--all"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert res.returncode == 0, f"STDERR:\n{res.stderr}\nSTDOUT:\n{res.stdout}"
    livrables = tmp_book / "livrables"
    md_out = livrables / "7 - Livre 2027.md"
    html_out = livrables / "7 - Livre 2027.html"
    pdf_out = livrables / "7 - Livre 2027.pdf"
    assert md_out.is_file() and md_out.stat().st_size > 1000
    assert html_out.is_file() and "<html" in html_out.read_text(encoding="utf-8")
    assert pdf_out.is_file() and pdf_out.read_bytes().startswith(b"%PDF-")


def test_12gram_rejects_long_quote_over_40_words_and_matches_real_corpus(tmp_book: Path) -> None:
    # Un segment > 40 mots entre guillemets meme suivi de [1] reste rejete
    corpus_file = tmp_book.parent / "0 - MD" / "1 - Compendium 2026.md"
    long_50 = " ".join(f"termeunique{i}" for i in range(50))
    corpus_file.write_text(
        corpus_file.read_text(encoding="utf-8") + f"\n{long_50}.\n",
        encoding="utf-8",
    )
    ch03 = tmp_book / "manuscrit" / "01 - Partie I" / "Chapitre 03 - Les nouvelles frontieres de la firme.md"
    ch03.write_text(
        ch03.read_text(encoding="utf-8").replace("Paragraphe 0", f"« {long_50} » [1]. Paragraphe 0", 1),
        encoding="utf-8",
    )
    errors = check_manuscrit(tmp_book, strict=True, unit_id="ch03")
    assert any("CA-03" in e for e in errors)

    # Verification directe sur le vrai corpus 0 - MD du depot
    from verifie_manuscrit import _CorpusIndex

    real_manifest = json.loads((REAL_BOOK_DIR / "specs" / "manifest.json").read_text(encoding="utf-8"))
    idx = _CorpusIndex.build(REAL_BOOK_DIR, real_manifest["internal_corpus_paths"])
    phrase = "Loi sur la protection de la vie privée des consommateurs et la Loi"
    assert idx.find_collisions(f"{phrase}.\n", "probe.md")
    assert idx.find_collisions(f"« {phrase} » [1].\n", "probe.md") == []


def test_ca04_ca05_ca10_negative_cases(tmp_book: Path) -> None:
    # CA-04 : absence de Question directrice, sous-section, encadre, figure
    ch04 = tmp_book / "manuscrit" / "02 - Partie II" / "Chapitre 04 - Posseder le noyau de controle 80-20.md"
    bad_ch04 = ch04.read_text(encoding="utf-8")
    bad_ch04 = bad_ch04.replace("*Question directrice :", "*Question :", 1)
    bad_ch04 = bad_ch04.replace("## 4.2", "## Section B", 1)
    bad_ch04 = bad_ch04.replace("> **Trois arbitrages sans regret", "> **Synthese", 1)
    bad_ch04 = bad_ch04.replace("Fig-08", "Schema-X")
    # CA-05 : > 2 tableaux et > 18 % puces
    extra_tables = (
        "\n| A | B |\n|---|---|\n| 1 | 2 |\n\n"
        "| C | D |\n|---|---|\n| 3 | 4 |\n\n"
        "| E | F |\n|---|---|\n| 5 | 6 |\n\n"
    )
    many_bullets = "\n".join(f"- Puce {i}" for i in range(120))
    # CA-10 : renvoi orphelin [99]
    ch04.write_text(bad_ch04 + extra_tables + many_bullets + "\nAffirmation orpheline [99].\n", encoding="utf-8")

    errors = check_manuscrit(tmp_book, strict=False, unit_id="ch04")
    assert any("CA-04" in e and "Question directrice" in e for e in errors)
    assert any("CA-04" in e and "4.2" in e for e in errors)
    assert any("CA-04" in e and "Trois arbitrages" in e for e in errors)
    assert any("CA-04" in e and "Fig-08" in e for e in errors)
    assert any("CA-05" in e and "tableaux" in e for e in errors)
    assert any("CA-05" in e and "puces" in e for e in errors)
    assert any("CA-10" in e and "[99]" in e for e in errors)


def test_genere_annexes_with_30_enriched_glossary_terms(tmp_book: Path) -> None:
    gloss_path = tmp_book / "registre" / "glossaire-termes.json"
    gloss = json.loads(gloss_path.read_text(encoding="utf-8"))
    while len(gloss["terms"]) < 30:
        idx = len(gloss["terms"]) + 1
        gloss["terms"].append(
            {
                "fr": f"concept gouvernance {idx}",
                "en": f"governance concept {idx}",
                "definition": (
                    "Définition normative précise encadrant la séparation des contrôles déterministes, "
                    "la traçabilité cryptographique et la supervision humaine effective en production."
                ),
                "chapitre_proprietaire": f"ch{(idx % 12) + 1:02d}",
            }
        )
    gloss_path.write_text(json.dumps(gloss, ensure_ascii=False, indent=2), encoding="utf-8")
    outputs = build_annexes(tmp_book)
    annex_a = tmp_book / "manuscrit" / "05 - Annexes" / "Annexe A - Glossaire raisonne.md"
    wc = count_prose_words(outputs[annex_a])
    assert 1656 <= wc <= 1944
    assert check_manuscrit(tmp_book, strict=True) == []


def test_cli_echantillon_and_check_deliverables_end_to_end(tmp_book: Path) -> None:
    aq_dir = tmp_book / "aq"
    aq_dir.mkdir(exist_ok=True)
    anc_dir = tmp_book / "ancrage"
    anc_dir.mkdir(exist_ok=True)

    for uid in UNITS_NARRATIVES:
        aname = "ch00-ancrage.md" if uid == "00-liminaire" else f"{uid}-ancrage.md"
        (anc_dir / aname).write_text(
            f"# Ancrage {uid}\n\nVerdict final : 100 % supporté (0 non supporté).\n",
            encoding="utf-8",
        )

    echantillon_script = TOOLS_DIR / "echantillon_aq.py"
    p1_json = aq_dir / "recollation-seed-202701.json"
    p2_json = aq_dir / "recollation-seed-202702.json"

    r1 = subprocess.run(
        [sys.executable, str(echantillon_script), "--root", str(tmp_book), "--seed", "202701", "-o", str(p1_json)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert r1.returncode == 0, r1.stderr
    r2 = subprocess.run(
        [
            sys.executable,
            str(echantillon_script),
            "--root",
            str(tmp_book),
            "--seed",
            "202702",
            "--exclude",
            str(p1_json),
            "-o",
            str(p2_json),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert r2.returncode == 0, r2.stderr

    (aq_dir / "recollation-seed-202701.md").write_text("# Passe 1\n\nResultat : 60/60.\n", encoding="utf-8")
    (aq_dir / "recollation-seed-202702.md").write_text("# Passe 2\n\nResultat : 60/60.\n", encoding="utf-8")
    (aq_dir / "gauntlet-log.md").write_text("# Gauntlet\n\n13/13 unites validees.\n", encoding="utf-8")
    (aq_dir / "rapport-lissage-et-visuel.md").write_text("# Lissage et visuel\n\n0 defaut.\n", encoding="utf-8")

    # Regenerer annexes C avec les vraies metriques aq/ et ancrage/, puis assembler les livrables
    build_annexes(tmp_book)
    r_asm = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "assemble_livre.py"), "--root", str(tmp_book), "--all"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert r_asm.returncode == 0, r_asm.stderr

    r_chk = subprocess.run(
        [
            sys.executable,
            str(TOOLS_DIR / "verifie_manuscrit.py"),
            "--root",
            str(tmp_book),
            "--strict",
            "--check-deliverables",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert r_chk.returncode == 0, f"STDOUT:\n{r_chk.stdout}\nSTDERR:\n{r_chk.stderr}"

    # L'absence de recollation-seed-202702.md doit faire echouer --check-deliverables
    (aq_dir / "recollation-seed-202702.md").unlink()
    errs = check_manuscrit(tmp_book, strict=True, check_deliverables=True)
    assert any("CA-14" in e for e in errs)
