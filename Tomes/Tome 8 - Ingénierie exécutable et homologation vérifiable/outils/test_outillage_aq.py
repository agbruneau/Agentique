# SPDX-License-Identifier: MIT
"""Tests TDD de l'outillage deterministe G1, G3, annexes et assemblage du Tome 8 (Tome 8 - Ingénierie exécutable et homologation vérifiable)."""

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

from _communs import compute_excerpt_sha256  # noqa: E402
from assemble_livre import _postprocess_typst_body, build_deliverables  # noqa: E402
from echantillon_aq import draw_stratified_sample  # noqa: E402
from genere_annexes import build_annexes  # noqa: E402
from verifie_manuscrit import _parse_toc_expectations, check_manuscrit, count_prose_words  # noqa: E402

UNITS_NARRATIVES = [
    "00-liminaire",
    "ch01",
    "ch02",
    "ch03",
    "ch04",
]


def _make_words(prefix: str, count: int) -> str:
    """Genere un paragraphe synthetique coupe en phrases <= 25 mots (majuscule initiale)."""
    tokens = []
    cap_next = False
    for i in range(count):
        base = f"{prefix}mot{i}"
        tok = base.capitalize() if cap_next else base
        cap_next = False
        if (i + 1) % 25 == 0 and i + 1 < count:
            tokens.append(f"{tok}.")
            cap_next = True
        else:
            tokens.append(tok)
    return " ".join(tokens)


def _source_filename(unit_id: str) -> str:
    if unit_id == "00-liminaire":
        return "ch00-sources.md"
    return f"{unit_id}-sources.md"


def _make_valid_png_bytes(width: int = 220, height: int = 160) -> bytes:
    def _chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack("!I", len(data)) + tag + data + struct.pack("!I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack("!IIBBBBB", width, height, 8, 6, 0, 0, 0)
    raw_scanlines = b"".join(b"\x00" + (b"\x1b\x36\x5d\xff" * width) for _ in range(height))
    idat = zlib.compress(raw_scanlines)
    return b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", idat) + _chunk(b"IEND", b"")


def _build_valid_unit_text(
    unit_meta: dict,
    fig_ext_map: dict[str, str],
    toc_unit: dict | None = None,
    owner_terms: list[str] | None = None,
    extra_body: str = "",
    synced_excerpt_block: str = "",
    include_vigilance: bool = False,
) -> str:
    """Construit une unite Markdown Vol. 8 conforme a CA-01..CA-10, CA-20 et toc.md."""
    uid = unit_meta["id"]
    figs = unit_meta.get("figures", [])
    fig_blocks = []
    for fid in figs:
        fnum = int(fid[4:])
        ext = fig_ext_map.get(fid, "svg")
        fig_blocks.append(
            f"La figure {fid} illustre l'architecture attendue.\n\n"
            f"![Légende de {fid}](../../diagrammes/rendus/{fid}.{ext})\n\n"
            f"*Figure {fnum} — Schéma synthétique pour {fid} [1].*"
        )
    fig_lines = "\n\n".join(fig_blocks)

    import re as _re

    def _strip_bt(s: str) -> str:
        return _re.sub(r"`([^`]+)`", r"\1", s)

    qd_val = _strip_bt((toc_unit or {}).get("qd") or f"Question du chapitre {uid} ?")
    raw_subs = (toc_unit or {}).get("subs") or {}
    subs_map = {k: _strip_bt(v) for k, v in raw_subs.items()}
    gloss_note = f"Notions propriétaires : {', '.join(owner_terms)} [1].\n\n" if owner_terms else ""

    if uid == "00-liminaire":
        head = (
            f"# {unit_meta['title']}\n\n"
            f"*Question directrice : {qd_val}*\n\n"
            "Le scénario illustratif du liminaire expose le passage de la prose au contrat exécutable G0 [1].\n\n"
        )
        sections = (
            f"## 0.1 {subs_map.get('0.1', 'Du référentiel normatif à l exigence de preuve exécutable')}\n\n"
            "Les volumes antérieurs forment une carte de repérage complétée par des validateurs G0 [1].\n\n"
            f"## 0.2 {subs_map.get('0.2', 'Table canonique de passage et résolution des cinq discordances inter-volumes')}\n\n"
            "| Discordance | Option A | Convention Volume 8 |\n"
            "|---|---|---|\n"
            "| MCP | 2025-11-25 | 2026-07-28 |\n\n"
            "*Tableau 0.1 — Synthèse canonique des discordances [1].*\n\n"
            f"## 0.3 {subs_map.get('0.3', 'Architecture bicéphale du Tome 8 : manuel concis et trousse exécutable trousse/')}\n\n"
            "> **Cinq critères permanents d'évaluation et de preuve exécutable**\n"
            "> 1. Fidélité à la source ouverte épinglée.\n\n"
            f"## 0.4 {subs_map.get('0.4', 'Logique des deux parties, quatre modules Python/OPA et parcours de lecture par rôle')}\n\n"
            "Quatre parcours guident la lecture selon le rôle [1].\n\n"
            f"## 0.5 {subs_map.get('0.5', 'Hygiène probatoire au gel du 2 décembre 2026, vecteurs tiers et frontière hors modèle DC-P12')}\n\n"
            "La date de gel est arrêtée au 2 décembre 2026 sur doublures hors modèle [2]. "
            "La révision MCP SEP-3398 attendue le 30 mars 2027 reste isolée par adaptateur [2].\n\n"
            f"## 0.6 {subs_map.get('0.6', 'Colophon d intégrité 100 % agentique G0–G5 et clause non-avis (AO-05)')}\n\n"
            "La clause non-avis encadre le banc G0 et exclut les portails OWASP fermés au profit de SRC-055 [2, 3].\n\n"
            f"{gloss_note}"
            f"{fig_lines}\n\n"
        )
        tail = "Transition vers la première partie du manuel.\n"
    else:
        num = int(uid[2:])
        head = (
            f"# {unit_meta['title']}\n\n"
            f"*Question directrice : {qd_val}*\n\n"
            f"Le cas concret du chapitre {num} expose un défi d'ingénierie exécutable [1].\n\n"
        )
        vig_block = ""
        if include_vigilance and uid == "ch01":
            vig_block = (
                "La dérive silencieuse d'outils MCP atteint 40,58 % sur 8 900 serveurs [1]. "
                "L'adaptateur isole SEP-2596 et SEP-3398 attendue le 30 mars 2027 ainsi que a2a-tck 1.0.0.alpha3 [3]. "
                "Le renvoi au Tableau 47.3 sur CycloneDX 1.7 évite tout doublon tandis que RFC 9334 reste Informational [3].\n\n"
            )
        elif include_vigilance and uid == "ch02":
            vig_block = (
                "Le calcul de h = SHA-256(JCS(...)) reprend C.5 et C.6 avec RFC 9964 et Transaction Tokens sur HTTP 431 [3]. "
                "Les signatures ML-DSA-65 mesurent 3 309 octets et ML-DSA-87 atteignent 4 627 octets [3]. "
                "Le mappage OTel v1.41.0 vers semantic-conventions-genai couvre 85 attributs dont cache_write [3].\n\n"
            )
        elif include_vigilance and uid == "ch03":
            vig_block = (
                "La règle Rego impose default allow := false avec opa test à 100 % sur vecteurs négatifs [3]. "
                "Sur AgentDojo, CaMeL résout 77 % contre 84 % sans défense et laisse un résidu de 5/15 trifecta [1].\n\n"
            )
        elif include_vigilance and uid == "ch04":
            vig_block = (
                "La règle EXIG-EVA-03 impose une borne de Wilson à 95 % inférieure à p avec au moins 3/p essais indépendants [1]. "
                "Les vecteurs OWASP SRC-055 L+ remplacent genai.owasp.org classé en statut F [2].\n\n"
            )
        sections = (
            f"## {num}.1 {subs_map.get(f'{num}.1', 'Section 1')}\n\n"
            f"La mesure empirique vérifie 40,58 % de dérive sur banc ouvert [1].\n\n"
            f"{vig_block}"
            f"## {num}.2 {subs_map.get(f'{num}.2', 'Section 2')}\n\n"
            f"La Loi 25 et la ligne directrice BSIF E-23 fixent la conformité non-avis au 1er mai 2027 [2].\n\n"
            f"## {num}.3 {subs_map.get(f'{num}.3', 'Section 3')}\n\n"
            f"Les standards RFC 8785, JCS et A2A v1.0.1 cadrent les échanges épinglés [3].\n\n"
            f"## {num}.4 {subs_map.get(f'{num}.4', 'Section 4')}\n\n"
            f"Le contrôle CI execute_g0.py valide EXIG-SEC-06 et OPA default allow := false en G0 [1].\n\n"
            f"{synced_excerpt_block}"
            f"{gloss_note}"
            f"{fig_lines}\n\n"
        )
        tail = (
            f"> **Trois invariants exécutables — Chapitre {num}**\n"
            "> 1. Exiger des contrats typés vérifiés en G0.\n\n"
            "Paragraphe final de transition vers la suite du manuel.\n"
        )

    base = head + sections + (f"{extra_body}\n\n" if extra_body else "") + tail
    cur_words = count_prose_words(base)
    target = unit_meta["target_words"]
    if cur_words < unit_meta["min_words"]:
        needed = target - cur_words
        chunks = []
        per_para = 110
        idx = 0
        strata_tags = [
            "mesure empirique 40,58 % sur banc [1]",
            "obligation juridique Loi 25 et BSIF E-23 non-avis [2]",
            "spécification technique RFC 8785 MCP JCS [3]",
            "assertion CI execute_g0.py EXIG-SEC-06 OPA default allow := false [1]",
        ]
        while needed > 0:
            take = min(per_para, needed)
            tag = strata_tags[idx % 4]
            body = _make_words(f"{uid}p{idx}", max(1, take - 10))
            chunks.append(f"Paragraphe {idx} traitant de {tag} : {body}.")
            needed -= take
            idx += 1
        base = head + sections + ("\n\n".join(chunks)) + "\n\n" + (f"{extra_body}\n\n" if extra_body else "") + tail
    return base


def _create_populated_vol8(
    tmp_path: Path,
    include_vigilance: bool = True,
    book_name: str = "Tome 8 - Ingénierie exécutable et homologation vérifiable",
) -> Path:
    """Cree un depot Tome 8 complet valide (avec sous-repertoire trousse/) dans tmp_path/Tomes/<book_name>."""
    tomes_dir = tmp_path / "Tomes"
    corpus_dir = tmp_path / "Corpus"
    tomes_dir.mkdir(parents=True, exist_ok=True)
    corpus_dir.mkdir(parents=True, exist_ok=True)
    book_dir = tomes_dir / book_name
    trousse_dir = book_dir / "trousse"
    corpus_file = corpus_dir / "Tome 1 - Confiance protocolaire et encadrement financier.md"
    corpus_file.write_text(
        "# Compendium\n\n"
        "Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application.\n"
        "Une phrase du corpus interne servant de temoin pour la detection exacte de douze mots consecutifs.\n",
        encoding="utf-8",
    )

    shutil.copytree(REAL_BOOK_DIR / "specs", book_dir / "specs")
    (book_dir / "README.md").write_text("# Manuel Vol. 8\n", encoding="utf-8")
    shutil.copy2(REAL_BOOK_DIR / ".gitignore", book_dir / ".gitignore")
    shutil.copytree(REAL_BOOK_DIR / "sources-locales", book_dir / "sources-locales")

    manifest_path = book_dir / "specs" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["internal_corpus_paths"] = ["../../Corpus/Tome 1 - Confiance protocolaire et encadrement financier.md"]
    manifest["stylistic_benchmarks_for_gauntlet"] = []
    manifest["stylistic_benchmark_sections"] = {}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # Trousse minimale et extrait CA-G0-SYNC reel pour ch01
    (trousse_dir / "harness_proto").mkdir(parents=True)
    excerpt_lines = [
        "def run_eight_steps(payload: dict) -> str:",
        "    # Etape deterministe de validation stricte",
        "    if not isinstance(payload, dict):",
        '        return "AMBIGU_ESCALADE"',
        '    return "OK"',
    ]
    (trousse_dir / "harness_proto" / "pipeline.py").write_text(
        "# SPDX-License-Identifier: MIT\n"
        "# CA-G0-SYNC-BEGIN:G0-EX-CH01-02\n"
        + "\n".join(excerpt_lines)
        + "\n# CA-G0-SYNC-END:G0-EX-CH01-02\n",
        encoding="utf-8",
        newline="\n",
    )
    ex_sha = compute_excerpt_sha256(excerpt_lines)
    aq_dir = book_dir / "aq"
    aq_dir.mkdir(parents=True)
    g0_report = {
        "schema_version": "1.0.0",
        "executed_at": "2026-12-02T12:00:00Z",
        "freeze_date": "2026-12-02",
        "platform": {
            "os": "Windows",
            "python_version": "3.14.10",
            "opa_version": "1.22.4",
            "opa_sha256": "a" * 64,
        },
        "overall_status": "PASS",
        "exit_code": 0,
        "spdx_check": {
            "license_target": "MIT",
            "checked_files": 18,
            "checked_packages": 17,
            "violations": [],
            "passed": True,
        },
        "lockfile_check": {
            "path": "requirements.lock",
            "sha256": "b" * 64,
            "all_hashes_pinned": True,
            "passed": True,
        },
        "schema_validation": {
            "schemas_checked": 10,
            "strict_violations": [],
            "passed": True,
        },
        "opa_check": {
            "files_checked": 3,
            "missing_default_deny": [],
            "coverage_pct": 100.0,
            "tests_passed": 12,
            "tests_failed": 0,
        },
        "pytest_check": {
            "passed": 45,
            "failed": 0,
            "skipped": 0,
            "modules": {"test_harness_proto": 15, "test_authz_pqc_audit": 15, "test_evalops_prr": 15},
        },
        "third_party_vectors": {
            "rfc8785": {"passed": True, "file_count": 20},
            "nist_acvp": {"passed": True, "file_count": 12},
            "a2a_tck": {"passed": True, "file_count": 5},
            "owasp_src055": {"passed": True, "file_count": 13},
        },
        "synced_excerpts": {
            "G0-EX-CH01-02": {
                "unit": "ch01",
                "source_path": f"{book_name}/trousse/harness_proto/pipeline.py",
                "lines": "3-7",
                "line_count": 5,
                "sha256": ex_sha,
            }
        },
    }
    (aq_dir / "rapports-g0.json").write_text(json.dumps(g0_report, indent=2), encoding="utf-8")

    # Corpus L+ reel couvrant RQ1..RQ6
    lplus_dir = book_dir / "recherche" / "corpus_l_plus"
    lplus_dir.mkdir(parents=True)
    rqs = ["RQ1", "RQ2", "RQ3", "RQ4", "RQ5", "RQ6"]
    sources_entries = []
    for i in range(1, 13):
        sid = f"SRC-{i:03d}"
        txt_rel = f"recherche/corpus_l_plus/{sid}.txt"
        txt_path = book_dir / txt_rel
        content = f"Texte integral primaire {sid}. Normes et mesures verifiees au 2 décembre 2026.\n" * 5
        txt_path.write_text(content, encoding="utf-8", newline="\n")
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
    for rq in rqs:
        for s in sources_entries:
            if rq not in s["research_axes"] and len([x for x in sources_entries if rq in x["research_axes"]]) < 6:
                s["research_axes"].append(rq)

    (book_dir / "recherche" / "manifeste-sources-sha256.json").write_text(
        json.dumps(
            {
                "protocol_id": "MLR-PRISMA-SCR-MANUEL-VOL8-2027-V1.0",
                "freeze_date": "2026-12-02",
                "metadata_only_pct": 0.0,
                "sources": sources_entries,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (book_dir / "recherche" / "registre-statut-f.json").write_text(
        json.dumps({"freeze_date": "2026-12-02", "blocked": []}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 6 registres (3 herites + 3 nouveaux SSOT)
    reg_dir = book_dir / "registre"
    reg_dir.mkdir(parents=True)
    (reg_dir / "ancres-chronologiques.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0.0",
                "freeze_date": "2026-12-02",
                "anchors": [
                    {
                        "key": "2027-03-30-MCP-SEP-3398",
                        "date": "2027-03-30",
                        "nature": "Revision attendue",
                        "jurisdiction": "International",
                        "label": "Révision MCP SEP-3398 attendue",
                        "chapters": ["ch01"],
                        "statut_preuve": "l_plus",
                        "source_l_plus_id": "SRC-001",
                    },
                    {
                        "key": "2027-05-01-BSIF-E23-AMF",
                        "date": "2027-05-01",
                        "nature": "Prudentiel",
                        "jurisdiction": "Canada",
                        "label": "Entrée en vigueur BSIF E-23",
                        "chapters": ["ch02"],
                        "statut_preuve": "l_plus",
                        "source_l_plus_id": "SRC-002",
                    },
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (reg_dir / "faits-empiriques.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0.0",
                "freeze_date": "2026-12-02",
                "facts": [
                    {
                        "id": "FACT-MCP-DRIFT-4058",
                        "metric": "Dérive silencieuse MCP",
                        "value": "40,58 %",
                        "source": "Corpus MCP",
                        "owner_chapter": "ch01",
                        "statut_preuve": "l_plus",
                        "source_l_plus_id": "SRC-001",
                    },
                    {
                        "id": "FACT-PQC-SIGNATURE-SIZE",
                        "metric": "Tailles ML-DSA",
                        "value": "ML-DSA-65 : 3 309 octets ; ML-DSA-87 : 4 627 octets",
                        "source": "NIST FIPS 204",
                        "owner_chapter": "ch02",
                        "statut_preuve": "l_plus",
                        "source_l_plus_id": "SRC-003",
                    },
                    {
                        "id": "FACT-CAMEL-RESIDUAL",
                        "metric": "CaMeL AgentDojo",
                        "value": "77 % contre 84 % sans défense",
                        "source": "arXiv:2503.18813v2",
                        "owner_chapter": "ch03",
                        "statut_preuve": "l_plus",
                        "source_l_plus_id": "SRC-004",
                    },
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (reg_dir / "glossaire-termes.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0.0",
                "freeze_date": "2026-12-02",
                "terms": [
                    {
                        "fr": f"terme normatif {i}",
                        "en": f"normative term {i}",
                        "definition": "Définition déterministe de référence pour le Volume 8.",
                        "chapitre_proprietaire": UNITS_NARRATIVES[i % 5],
                    }
                    for i in range(12)
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (reg_dir / "specifications-lplus.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0.0",
                "freeze_date": "2026-12-02",
                "specs": [
                    {
                        "spec_id": "RFC-8785",
                        "title": "JSON Canonicalization Scheme (JCS)",
                        "version_or_tag": "RFC 8785",
                        "maturity_status": "FINAL_STANDARD",
                        "license_spdx": "IETF-Trust",
                        "source_l_plus_id": "SRC-001",
                        "sha256": sources_entries[0]["sha256"],
                        "statut_preuve": "l_plus",
                        "modules_trousse": ["harness_proto"],
                        "adapter_boundary": None,
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (reg_dir / "matrice-exig-prr-c40.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0.0",
                "freeze_date": "2026-12-02",
                "mappings": [
                    {
                        "id": "EXIG-SEC-06",
                        "family": "EXIG",
                        "criticality": "BLOQUANT",
                        "owner_chapter": "ch03",
                        "trousse_module": "policies_opa",
                        "implementation_symbol": "rule_of_two.allow",
                        "rego_rule": "trousse.policy.rule_of_two.allow",
                        "pytest_nodeid": "tests/test_policy_saga.py::test_rule_of_two",
                        "third_party_vector_suite": "owasp_src055",
                        "corpus_anchor": "Tome 2 - Cadre normatif et exigences d'architecture.md L4385",
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (reg_dir / "concordance-taxonomies.json").write_text(
        json.dumps(
            {
                "registry_version": "1.0.0",
                "freeze_date": "2026-12-02",
                "concordances": [
                    {
                        "discordance_id": f"DISC-0{i}",
                        "topic": f"Discordance {i}",
                        "volume_variants": [
                            {"volume": "Vol. 6", "definition": "Option A", "corpus_ref": "Vol6"},
                            {"volume": "Vol. 7", "definition": "Option B", "corpus_ref": "Vol7"},
                        ],
                        "canonical_vol8_choice": f"Choix canonique {i}",
                        "liminaire_section": "0.2",
                        "rationale": "Arbitrage unifié Volume 8.",
                    }
                    for i in range(1, 6)
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    glossaire_data = json.loads((reg_dir / "glossaire-termes.json").read_text(encoding="utf-8"))
    terms_by_owner: dict[str, list[str]] = {}
    for t in glossaire_data["terms"]:
        terms_by_owner.setdefault(t["chapitre_proprietaire"], []).append(t["fr"])

    src_dir = book_dir / "sources"
    src_dir.mkdir(parents=True)
    for uid in UNITS_NARRATIVES:
        sname = _source_filename(uid)
        (src_dir / sname).write_text(
            f"# Sources — {uid}\n\n"
            "Date de gel des faits : 2 décembre 2026\n\n"
            "### [1] SRC-001 — Etude empirique primaire\nRésumé vérifié sur texte intégral.\n\n"
            "### [2] SRC-002 — Texte réglementaire primaire\nRésumé vérifié sur texte intégral.\n\n"
            "### [3] SRC-003 — Spécification technique primaire\nRésumé vérifié sur texte intégral.\n",
            encoding="utf-8",
        )

    # 9 figures (7 puml, 2 mmd)
    diag_dir = book_dir / "diagrammes"
    rendus_dir = diag_dir / "rendus"
    rendus_dir.mkdir(parents=True)
    puml_nodes = "\n".join(f'rectangle "Bloc {i}" as N{i}' for i in range(1, 11))
    mmd_edges = "\n".join(f'  N{i}["Noeud {i}"] --> N{i + 1}["Noeud {i + 1}"]' for i in range(1, 10))
    fig_ext_map = {f["id"]: ("svg" if f["engine"] == "puml" else "png") for f in manifest["figures"]}
    for fmeta in manifest["figures"]:
        fid = fmeta["id"]
        if fmeta["engine"] == "puml":
            (diag_dir / f"{fid}.puml").write_text(f"@startuml\n{puml_nodes}\nN1 --> N10\n@enduml\n", encoding="utf-8")
            (rendus_dir / f"{fid}.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="180"><rect width="10" height="10"/></svg>',
                encoding="utf-8",
            )
        else:
            (diag_dir / f"{fid}.mmd").write_text(f"flowchart TD\n{mmd_edges}\n", encoding="utf-8")
            (rendus_dir / f"{fid}.png").write_bytes(_make_valid_png_bytes())

    toc_expectations = _parse_toc_expectations(book_dir)
    synced_block_ch01 = (
        f'<!-- CA-G0-SYNC id="G0-EX-CH01-02" path="{book_name}/trousse/harness_proto/pipeline.py" lines="3-7" sha256="{ex_sha}" -->\n'
        "```python\n"
        + "\n".join(excerpt_lines)
        + "\n```\n\n"
    )
    for u in manifest["units"]:
        if u["kind"] in {"frontmatter", "chapter"}:
            out = book_dir / u["file"]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                _build_valid_unit_text(
                    u,
                    fig_ext_map=fig_ext_map,
                    toc_unit=toc_expectations.get(u["id"]),
                    owner_terms=terms_by_owner.get(u["id"], []),
                    synced_excerpt_block=synced_block_ch01 if u["id"] == "ch01" else "",
                    include_vigilance=include_vigilance,
                ),
                encoding="utf-8",
            )

    build_annexes(book_dir)
    return book_dir


@pytest.fixture()
def tmp_vol8(tmp_path: Path) -> Path:
    return _create_populated_vol8(tmp_path, include_vigilance=True)


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
        "Liste brute de cinquante mots completement exclus du decompte officiel.\n"
        "<!-- BIBLIOGRAPHIE_BRUTE_FIN -->\n\n"
        "Deux mots finaux.\n"
    )
    assert count_prose_words(sample) == 15


def test_clean_populated_vol8_passes_strict(tmp_vol8: Path) -> None:
    assert check_manuscrit(tmp_vol8, sources_only=True) == []
    assert check_manuscrit(tmp_vol8, strict=True) == []


def test_ca02_allows_tech_ids_and_rejects_raw_audit_markers(tmp_vol8: Path) -> None:
    ch01 = tmp_vol8 / "manuscrit" / "01 - Partie I" / "Chapitre 01 - Harnais deterministe et mediation protocolaire.md"
    txt = ch01.read_text(encoding="utf-8")
    txt = txt.replace(
        "Paragraphe 0",
        "Les identifiants EXIG-SEC-06, CAP-046, ADR-001, POR-001 et PRR-75 sont permis, "
        "mais [L+], [S] et Classe 1 restent interdits [1].\n\n"
        "Un montant de 15,5 G$ est non echappe ici [1]. Paragraphe 0",
        1,
    )
    ch01.write_text(txt, encoding="utf-8")

    errors = check_manuscrit(tmp_vol8, strict=True, unit_id="ch01")
    assert not any("EXIG-SEC-06" in e or "CAP-046" in e or "ADR-001" in e or "POR-001" in e or "PRR-75" in e for e in errors)
    assert any("CA-02" in e and "[L+]" in e for e in errors)
    assert any("CA-02" in e and "[S]" in e for e in errors)
    assert any("CA-02" in e and "Classe" in e for e in errors)
    assert any("CA-06" in e for e in errors)


def test_ca_g0_sync_rejects_drift_over_40_lines_and_missing_anchor(tmp_vol8: Path) -> None:
    ch01 = tmp_vol8 / "manuscrit" / "01 - Partie I" / "Chapitre 01 - Harnais deterministe et mediation protocolaire.md"
    orig = ch01.read_text(encoding="utf-8")

    # 1. Divergence d'un seul caractere dans le bloc synchronise
    drifted = orig.replace('return "OK"', 'return "NOK"', 1)
    ch01.write_text(drifted, encoding="utf-8")
    errs_drift = check_manuscrit(tmp_vol8, strict=True, unit_id="ch01")
    assert any("CA-G0-SYNC" in e and "SHA-256" in e for e in errs_drift)

    # 2. Bloc de > 40 lignes sans ancre
    big_block = "\n```python\n" + "\n".join(f"x_{i} = {i}" for i in range(42)) + "\n```\n"
    ch01.write_text(orig + big_block, encoding="utf-8")
    errs_40 = check_manuscrit(tmp_vol8, strict=True, unit_id="ch01")
    assert any("CA-G0-SYNC" in e and "40 lignes" in e for e in errs_40)
    assert any("CA-G0-SYNC" in e and "sans balise" in e for e in errs_40)
    ch01.write_text(orig, encoding="utf-8")

    # 3. Bloc de code dans 00-liminaire strictement interdit
    lim = tmp_vol8 / "manuscrit" / "00 - Liminaire.md"
    lim.write_text(lim.read_text(encoding="utf-8") + "\n```python\na = 1\n```\n", encoding="utf-8")
    errs_lim = check_manuscrit(tmp_vol8, strict=True, unit_id="00-liminaire")
    assert any("CA-G0-SYNC" in e and "interdit" in e for e in errs_lim)


def test_dollar_math_rejected_and_backslash_math_accepted(tmp_vol8: Path) -> None:
    ch02 = tmp_vol8 / "manuscrit" / "01 - Partie I" / "Chapitre 02 - Identite non humaine, PQC et double couloir.md"
    txt = ch02.read_text(encoding="utf-8")
    txt = txt.replace(
        "Paragraphe 0",
        "Formule valide \\(0{,}94^{10}\\) ici.\n\nFormule rejetee $0{,}94^{10}$ ici.\n\nParagraphe 0",
        1,
    )
    ch02.write_text(txt, encoding="utf-8")

    errors = check_manuscrit(tmp_vol8, strict=True)
    assert any("CA-06" in e and "$0{,}94" in e for e in errors)
    assert not any("CA-06" in e and "\\(0{,}94" in e for e in errors)


def test_two_seeds_produce_disjoint_60_items_across_4_strata(tmp_vol8: Path) -> None:
    s1 = draw_stratified_sample(tmp_vol8, seed=20270801, exclude_ids=set())
    excluded = {x["claim_loc"] for x in s1} | {x["paragraph_loc"] for x in s1}
    s2 = draw_stratified_sample(tmp_vol8, seed=20270802, exclude_ids=excluded)

    assert len(s1) == 60 and len(s2) == 60
    assert {x["claim_loc"] for x in s1}.isdisjoint({x["claim_loc"] for x in s2})
    assert {x["paragraph_loc"] for x in s1}.isdisjoint({x["paragraph_loc"] for x in s2})

    for sample in (s1, s2):
        for cat in ("empirique", "juridique", "spec_technique", "assertions_g0"):
            assert sum(1 for x in sample if x["category"] == cat) == 15
        assert all(sum(1 for x in sample if x["unit"] == u) >= 8 for u in UNITS_NARRATIVES)

    assert draw_stratified_sample(tmp_vol8, seed=20270801, exclude_ids=set()) == s1
    s1_text = " ".join(x["text"].lower() for x in s1)
    assert "sep-3398" in s1_text or "1.0.0.alpha3" in s1_text
    assert "wilson" in s1_text or "3/p" in s1_text
    assert "default allow := false" in s1_text


def test_ca05_enforces_3_tables_and_25_pct_bullets(tmp_vol8: Path) -> None:
    ch03 = tmp_vol8 / "manuscrit" / "02 - Partie II" / "Chapitre 03 - Politiques OPA hors modele et Sagas.md"
    orig3 = ch03.read_text(encoding="utf-8")

    three_tables = (
        "\n\n*Tableau 3.1 — Premier.*\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
        "\n*Tableau 3.2 — Deuxieme.*\n\n| C | D |\n|---|---|\n| 3 | 4 |\n"
        "\n*Tableau 3.3 — Troisieme.*\n\n| E | F |\n|---|---|\n| 5 | 6 |\n"
    )
    ch03.write_text(orig3 + three_tables, encoding="utf-8")
    assert check_manuscrit(tmp_vol8, strict=True, unit_id="ch03") == []

    fourth_table = "\n\n*Tableau 3.4 — Quatrieme.*\n\n| G | H |\n|---|---|\n| 7 | 8 |\n"
    ch03.write_text(orig3 + three_tables + fourth_table, encoding="utf-8")
    errs_tab = check_manuscrit(tmp_vol8, strict=True, unit_id="ch03")
    assert any("CA-05" in e and "tableaux" in e for e in errs_tab)

    many_bullets = "\n" + "\n".join(f"- Puce {i}" for i in range(180))
    ch03.write_text(orig3 + many_bullets, encoding="utf-8")
    errs_bul = check_manuscrit(tmp_vol8, strict=True, unit_id="ch03")
    assert any("CA-05" in e and "puces" in e for e in errs_bul)


def test_genere_annexes_pre_post_qa_and_ca17(tmp_vol8: Path) -> None:
    annex_a = tmp_vol8 / "manuscrit" / "03 - Annexes" / "Annexe A - Socle L-plus, statut F et journal Wyvern.md"
    annex_b = tmp_vol8 / "manuscrit" / "03 - Annexes" / "Annexe B - Tracabilite, vecteurs tiers et bilan AQ.md"

    assert 1380 <= count_prose_words(annex_a.read_text(encoding="utf-8")) <= 1620
    assert 1380 <= count_prose_words(annex_b.read_text(encoding="utf-8")) <= 1620

    anc_dir = tmp_vol8 / "ancrage"
    anc_dir.mkdir()
    for uid in UNITS_NARRATIVES:
        sname = "ch00-ancrage.md" if uid == "00-liminaire" else f"{uid}-ancrage.md"
        (anc_dir / sname).write_text(
            f"# Ancrage {uid}\n\nVerdict final : 10 / 10 (100 %) supporté, 0 non supporté.\n",
            encoding="utf-8",
        )
    aq_dir = tmp_vol8 / "aq"
    s1 = draw_stratified_sample(tmp_vol8, seed=20270801, exclude_ids=set())
    (aq_dir / "recollation-seed-20270801.json").write_text(json.dumps(s1, ensure_ascii=False), encoding="utf-8")
    (aq_dir / "recollation-seed-20270801.md").write_text("# Recollation 1\n\nScore final : 60/60 (100 %).\n", encoding="utf-8")
    (aq_dir / "gauntlet-log.md").write_text("# Gauntlet\n\n5/5 unites validees.\n", encoding="utf-8")

    build_annexes(tmp_vol8)
    annex_b_text = annex_b.read_text(encoding="utf-8")
    assert "60/60" in annex_b_text
    assert 1380 <= count_prose_words(annex_b_text) <= 1620
    assert check_manuscrit(tmp_vol8, strict=True) == []

    annex_a.write_text(annex_a.read_text(encoding="utf-8") + "\nAjout manuel interdit.", encoding="utf-8")
    errors = check_manuscrit(tmp_vol8, strict=True)
    assert any("CA-17" in e for e in errors)


def _run_tool_script(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    py_flags = ["-B"] if sys.dont_write_bytecode else []
    return subprocess.run(
        [sys.executable, *py_flags, str(script), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def _populate_qa_logs(book_dir: Path) -> Path:
    aq_dir = book_dir / "aq"
    aq_dir.mkdir(exist_ok=True)
    anc_dir = book_dir / "ancrage"
    anc_dir.mkdir(exist_ok=True)

    for uid in UNITS_NARRATIVES:
        aname = "ch00-ancrage.md" if uid == "00-liminaire" else f"{uid}-ancrage.md"
        (anc_dir / aname).write_text(
            f"# Ancrage {uid}\n\nVerdict final : 100 % supporté (0 non supporté).\n",
            encoding="utf-8",
        )

    (aq_dir / "recollation-seed-20270801.md").write_text("# Passe 1\n\nScore final : 60/60.\n", encoding="utf-8")
    (aq_dir / "recollation-seed-202702.md" if False else aq_dir / "recollation-seed-20270802.md").write_text(
        "# Passe 2\n\nScore final : 60/60.\n",
        encoding="utf-8",
    )
    (aq_dir / "gauntlet-log.md").write_text("# Gauntlet\n\n5/5 unites validees.\n", encoding="utf-8")
    (aq_dir / "rapport-lissage-et-visuel.md").write_text("# Lissage et visuel\n\n0 defaut.\n", encoding="utf-8")
    return aq_dir


def test_cli_echantillon_assemble_and_check_deliverables_end_to_end(tmp_vol8: Path) -> None:
    aq_dir = _populate_qa_logs(tmp_vol8)

    echantillon_script = TOOLS_DIR / "echantillon_aq.py"
    p1_json = aq_dir / "recollation-seed-20270801.json"
    p2_json = aq_dir / "recollation-seed-20270802.json"

    r1 = _run_tool_script(echantillon_script, "--root", str(tmp_vol8), "--seed", "20270801", "-o", str(p1_json))
    assert r1.returncode == 0, r1.stderr
    r2 = _run_tool_script(
        echantillon_script,
        "--root",
        str(tmp_vol8),
        "--seed",
        "20270802",
        "--exclude",
        str(p1_json),
        "-o",
        str(p2_json),
    )
    assert r2.returncode == 0, r2.stderr

    build_annexes(tmp_vol8)
    r_asm = _run_tool_script(TOOLS_DIR / "assemble_livre.py", "--root", str(tmp_vol8), "--all")
    assert r_asm.returncode == 0, r_asm.stderr

    livrables = tmp_vol8 / "livrables"
    consolidated_dir = tmp_vol8.parent.parent / "Corpus"
    md_out = consolidated_dir / "Tome 8 - Ingénierie exécutable et homologation vérifiable.md"
    html_out = livrables / "Tome 8 - Ingénierie exécutable et homologation vérifiable.html"
    assert md_out.is_file()
    assert 'title: "Tome 8 — Ingénierie exécutable et homologation vérifiable"' in md_out.read_text(encoding="utf-8")
    assert (consolidated_dir / "Tome 8 - Ingénierie exécutable et homologation vérifiable.pdf").read_bytes().startswith(b"%PDF-")
    assert [p.name for p in livrables.iterdir()] == ["Tome 8 - Ingénierie exécutable et homologation vérifiable.html"]
    html_txt = html_out.read_text(encoding="utf-8")
    html_flat = " ".join(html_txt.split())
    assert "<figcaption>" not in html_txt
    assert "<title>Tome 8 — Ingénierie exécutable et homologation vérifiable</title>" in html_flat
    assert '<h1 class="title">Tome 8 — Ingénierie exécutable et homologation vérifiable</h1>' in html_flat
    assert "Tome 8 — Tome 8" not in html_flat

    r_chk = _run_tool_script(
        TOOLS_DIR / "verifie_manuscrit.py",
        "--root",
        str(tmp_vol8),
        "--strict",
        "--check-deliverables",
    )
    assert r_chk.returncode == 0, f"STDOUT:\n{r_chk.stdout}\nSTDERR:\n{r_chk.stderr}"

    # Echec G0 ou absence recollation 20270802 bloque --check-deliverables
    (aq_dir / "recollation-seed-20270802.md").unlink()
    errs = check_manuscrit(tmp_vol8, strict=True, check_deliverables=True)
    assert any("CA-14" in e for e in errs)


def test_12gram_ignores_quoted_statute_titles_and_matches_real_corpus(tmp_vol8: Path) -> None:
    ch04 = tmp_vol8 / "manuscrit" / "02 - Partie II" / "Chapitre 04 - Banc EvalOps hermetique et 24 portes PRR.md"
    orig = ch04.read_text(encoding="utf-8")

    quoted = orig.replace(
        "Paragraphe 0",
        "La loi citee est « Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application » [1]. Paragraphe 0",
        1,
    )
    ch04.write_text(quoted, encoding="utf-8")
    assert not any("CA-03" in e for e in check_manuscrit(tmp_vol8, strict=True, unit_id="ch04"))

    unquoted = orig.replace(
        "Paragraphe 0",
        "Selon la Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application, l'audit est requis [1]. Paragraphe 0",
        1,
    )
    ch04.write_text(unquoted, encoding="utf-8")
    assert any("CA-03" in e for e in check_manuscrit(tmp_vol8, strict=True, unit_id="ch04"))

    from verifie_manuscrit import _CorpusIndex

    real_manifest = json.loads((REAL_BOOK_DIR / "specs" / "manifest.json").read_text(encoding="utf-8"))
    idx = _CorpusIndex.build(REAL_BOOK_DIR, real_manifest["internal_corpus_paths"])
    phrase = "Loi sur la protection de la vie privée des consommateurs et la Loi"
    assert idx.find_collisions(f"{phrase}.\n", "probe.md")
    assert idx.find_collisions(f"« {phrase} » [1].\n", "probe.md") == []


def test_typst_postprocess_math_commas_and_links() -> None:
    raw = (
        "#emph[Figure 1 — Legende officielle]\n\n"
        "Prix 15,5 \\$ US et 20 \\$ CA, calcul $0\\,94^(10)$ -> 100 % et 3 309 o.\n\n"
        "`DeterministicHarness` et `StreamableHttpAdapter`.\n\n"
        "= Bibliographie classée des sources intégrales vérifiées\n<bibliographie>\n"
        '- #link("https://example.org/a-b/c") — `https://blocked.org/p-q`\n'
    )
    out = _postprocess_typst_body(raw)
    assert "#align(center)" in out and "Figure 1" in out
    assert '$0","94^(10)$' in out
    assert "15,5\u00a0\\$\u00a0US" in out
    assert "20\u00a0\\$\u00a0CA" in out
    assert "100\u00a0%" in out and "3\u00a0309\u00a0o" in out
    assert " → " in out
    assert "`DeterministicHarness` et `StreamableHttpAdapter`." in out
    assert (
        '#link("https://example.org/a-b/c")[#text(hyphenate: false)[#("https://example.\u200borg/\u200ba-\u200bb/\u200bc")]]'
        in out
    )
    assert "`https://blocked.\u200borg/\u200bp-\u200bq`" in out


def test_typst_postprocess_tables_camelcase_decimals_and_apostrophes() -> None:
    raw = (
        "#figure(\n"
        "  align(center)[#table(\n"
        "    columns: 3,\n"
        "    align: (auto,right,center,),\n"
        "    table.header([ID], [Énoncé], [Code],),\n"
        "    table.hline(),\n"
        "    [`CH03-001`], [Flux d’approvisionnement], [`OpaStaticCheckError`, `rétrocompatibilité` et `0.0089`],\n"
        "  )]\n"
        "  , kind: table\n"
        "  )\n\n"
        "#emph[Tableau 2.2 — Matrice courte.]\n"
    )
    out = _postprocess_typst_body(raw)
    assert "align: (left,right,center,)" in out
    assert "columns: (" in out
    assert "d’\u200bapprovisionnement" in out
    assert "`Opa\u200bStatic\u200bCheck\u200bError`" in out
    assert "`rétrocompati\u200bbilité`" in out
    assert "`0.0089`" in out
    assert "#block(width: 100%, breakable: false)[" in out
    assert "Tableau 2.2" in out


def test_dynamic_book_stem_purges_residual_html_and_aligns_deliverables(tmp_path: Path) -> None:
    custom_book = _create_populated_vol8(tmp_path, include_vigilance=True, book_name="8 - Titre Test")
    aq_dir = _populate_qa_logs(custom_book)
    s1 = draw_stratified_sample(custom_book, seed=20270801, exclude_ids=set())
    excluded = {x["claim_loc"] for x in s1} | {x["paragraph_loc"] for x in s1}
    s2 = draw_stratified_sample(custom_book, seed=20270802, exclude_ids=excluded)
    (aq_dir / "recollation-seed-20270801.json").write_text(json.dumps(s1, ensure_ascii=False), encoding="utf-8")
    (aq_dir / "recollation-seed-20270802.json").write_text(json.dumps(s2, ensure_ascii=False), encoding="utf-8")
    build_annexes(custom_book)

    livrables = custom_book / "livrables"
    livrables.mkdir(parents=True, exist_ok=True)
    stray_ancien = livrables / "ancien.html"
    stray_ancien.write_text("<html><body>ancien</body></html>", encoding="utf-8")

    outputs = build_deliverables(custom_book, make_md=True, make_html=True, make_pdf=True)
    consolidated_dir = custom_book.parent.parent / "Corpus"
    expected_md = consolidated_dir / "8 - Titre Test.md"
    expected_pdf = consolidated_dir / "8 - Titre Test.pdf"
    expected_html = livrables / "8 - Titre Test.html"

    assert outputs["md"] == expected_md and expected_md.is_file()
    assert outputs["pdf"] == expected_pdf and expected_pdf.is_file() and expected_pdf.read_bytes().startswith(b"%PDF-")
    assert outputs["html"] == expected_html and expected_html.is_file()
    assert not stray_ancien.exists()
    assert [p.name for p in livrables.iterdir()] == ["8 - Titre Test.html"]
    assert check_manuscrit(custom_book, strict=True, check_deliverables=True) == []
