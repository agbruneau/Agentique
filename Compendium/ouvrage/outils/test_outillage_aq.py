# SPDX-License-Identifier: MIT
"""Tests TDD de l'outillage déterministe G1, G3, annexes et assemblage du Compendium."""

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
REPO_ROOT = REAL_BOOK_DIR.parent.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from _communs import compute_excerpt_sha256, get_freeze_date  # noqa: E402
from assemble_livre import (  # noqa: E402
    _clean_residual_livrables,
    _normalize_image_paths,
    build_deliverables,
)
from echantillon_aq import draw_stratified_sample  # noqa: E402
from genere_annexes import build_annexes  # noqa: E402
from verifie_manuscrit import check_manuscrit, count_prose_words  # noqa: E402

DOMAINS = [f"D{i:02d}" for i in range(1, 13)]


def _make_words(prefix: str, count: int) -> str:
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
    owner_terms: list[str] | None = None,
    synced_excerpt_block: str = "",
) -> str:
    uid = unit_meta["id"]
    figs = unit_meta.get("figures", [])
    fig_blocks = []
    for fid in figs:
        ext = fig_ext_map.get(fid, "svg")
        fig_blocks.append(
            f"Le schéma `{fid}` illustre l'architecture visée [1].\n\n"
            f"![Légende de {fid}](../../schemas/rendus/{fid}.{ext})\n\n"
            f"*Figure {fid} — Schéma synthétique pour {fid} [1].*"
        )
    fig_lines = "\n\n".join(fig_blocks)
    gloss_note = f"Notions propriétaires : {', '.join(owner_terms)} [1].\n\n" if owner_terms else ""

    if uid == "00-liminaire":
        head = (
            f"# {unit_meta['title']}\n\n"
            "*Question directrice : Comment un Système d'agentivité passe-t-il du prototype à la production homologuée ?*\n\n"
            "Le présent ouvrage applique la doctrine hybride 80/20 sous clause `non-avis` (`AO-05`) [1].\n\n"
        )
        sections = (
            "## 0.1 Problématique industrielle et loi de Lusser\n\n"
            "La mesure empirique vérifie 40,58 % de dérive MCP sur 8 900 serveurs [1].\n\n"
            "## 0.2 Doctrine hybride 80/20 et harnais déterministe\n\n"
            "| Discordance | Option A | Convention Compendium |\n"
            "|---|---|---|\n"
            "| `DISC-05` | 2025-11-25 | 2026-07-28 |\n\n"
            "*Tableau 0.1 — Synthèse des discordances [1].*\n\n"
            "## 0.3 Topologie des 12 domaines et 616 interrelations\n\n"
            "> **Cinq critères permanents d'évaluation et de preuve exécutable**\n"
            "> 1. Fidélité à la source ouverte épinglée.\n\n"
            "## 0.4 Gouvernance duale AE ↔ AS\n\n"
            "Les Systèmes d'agentivité séparent l'exosquelette déterministe du cœur cognitif [1].\n\n"
            "## 0.5 Cadre réglementaire 2023–2035 et gel du 2 décembre 2026\n\n"
            "La date de gel est arrêtée au 2 décembre 2026 ; la clause non-avis encadre le référentiel [2]. "
            "La révision MCP SEP-3398 attendue le 30 mars 2027 reste isolée par adaptateur [2].\n\n"
            f"{gloss_note}{fig_lines}\n\n"
        )
        tail = "Transition vers la première partie du Compendium [1].\n"
    else:
        num = int(uid[2:])
        owned_slugs = unit_meta.get("owned_concepts", [])
        slugs_line = (
            f"Périmètre exclusif : {', '.join(f'`{s}`' for s in owned_slugs)} [1].\n\n"
            if owned_slugs
            else ""
        )
        vig_extra = ""
        if uid == "ch04":
            vig_extra = (
                "La dérive silencieuse d'outils MCP atteint 40,58 % sur 8 900 serveurs [1]. "
                "L'adaptateur isole SEP-2596 et SEP-3398 attendue le 30 mars 2027 ainsi que a2a-tck 1.0.0.alpha3 [3]. "
                "Le renvoi au Tableau 47.3 sur CycloneDX 1.7 évite tout doublon tandis que RFC 9334 reste Informational [3].\n\n"
            )
        elif uid == "ch07":
            vig_extra = (
                "La révision SEP-3398 attendue le 2027-03-30 complète le socle MCP vérifié [3].\n\n"
            )
        elif uid == "ch17":
            vig_extra = (
                "Le calcul de h = SHA-256(JCS(...)) reprend C.5 et C.6 avec RFC 9964 et Transaction Tokens sur HTTP 431 [3]. "
                "Les signatures ML-DSA-65 mesurent 3 309 octets et ML-DSA-87 atteignent 4 627 octets [3].\n\n"
            )
        elif uid == "ch20":
            vig_extra = (
                "La règle Rego impose default allow := false avec opa test à 100 % sur vecteurs négatifs [3]. "
                "Sur AgentDojo, CaMeL résout 77 % contre 84 % sans défense [1].\n\n"
            )
        elif uid == "ch22":
            vig_extra = (
                "Le mappage OTel v1.41.0 vers semantic-conventions-genai couvre 85 attributs dont cache_write [3].\n\n"
            )
        elif uid == "ch25":
            vig_extra = (
                "La ligne directrice BSIF E-23 entre en vigueur le 2027-05-01 sans portée d'avis [2].\n\n"
            )
        elif uid == "ch35":
            vig_extra = (
                "La règle EXIG-EVA-03 impose une borne de Wilson à 95 % inférieure à p avec au moins 3/p essais indépendants [1]. "
                "Les vecteurs OWASP SRC-055 L+ remplacent genai.owasp.org classé en statut F [2].\n\n"
            )

        head = (
            f"# {unit_meta['title']}\n\n"
            f"*Question directrice : Comment le chapitre {num} garantit-il la conformité déterministe ?*\n\n"
            f"Les Systèmes d'agentivité mobilisent ici un contrôle vérifiable [1].\n\n"
        )
        sections = (
            f"## {num}.1 Résumé\n\n"
            f"La mesure empirique vérifie 40,58 % de dérive sur banc ouvert [1]. {vig_extra}\n\n"
            f"## {num}.2 Descriptif du contenu ciblé\n\n"
            f"La Loi 25 et la ligne directrice BSIF E-23 fixent la conformité non-avis au 1er mai 2027 [2].\n\n"
            f"### {num}.2.1 Premier volet normatif\n\n"
            f"Les standards RFC 8785, JCS et A2A v1.0.1 cadrent les échanges épinglés [3].\n\n"
            f"### {num}.2.2 Second volet exécutable\n\n"
            f"Le contrôle CI `execute_g0.py` valide `EXIG-SEC-06` et `OPA` `default allow := false` en `G0` [1].\n\n"
            f"{slugs_line}"
            f"{synced_excerpt_block}"
            f"{gloss_note}"
            f"## {num}.3 Schémas de vulgarisation\n\n"
            f"{fig_lines}\n\n"
        )
        tail = (
            f"> **Trois invariants exécutables — Chapitre {num}**\n"
            "> 1. Exiger des contrats typés vérifiés en `G0`.\n\n"
            "Paragraphe de transition vers la suite du traité [1].\n"
        )

    base = head + sections + tail
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
        base = head + sections + ("\n\n".join(chunks)) + "\n\n" + tail
    return base


def _create_populated_compendium(tmp_path: Path) -> Path:
    donnees_src = REPO_ROOT / "Tomes" / "Cartographie" / "donnees"
    mm_src = json.loads((donnees_src / "corpus-mindmap-data.json").read_text(encoding="utf-8"))
    cat_src = json.loads((donnees_src / "catalogue-schemas-prd.json").read_text(encoding="utf-8"))

    book_dir = tmp_path / "Compendium" / "ouvrage"
    trousse_dir = tmp_path / "Tomes" / "Tome 8 - Ingénierie exécutable et homologation vérifiable" / "trousse"
    corpus_dir = tmp_path / "Corpus"
    corpus_dir.mkdir(parents=True, exist_ok=True)
    corpus_file = corpus_dir / "Tome 1 - Confiance protocolaire et encadrement financier.md"
    corpus_file.write_text(
        "# Tome 1\n\n"
        "Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application.\n"
        "Une phrase du corpus interne servant de témoin pour la détection exacte de douze mots consécutifs.\n",
        encoding="utf-8",
    )

    shutil.copytree(REAL_BOOK_DIR / "specs", book_dir / "specs")
    manifest_path = book_dir / "specs" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["internal_corpus_paths"] = ["../../Corpus/Tome 1 - Confiance protocolaire et encadrement financier.md"]
    manifest["stylistic_benchmarks_for_gauntlet"] = []
    manifest["stylistic_benchmark_sections"] = {}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")

    # Trousse minimale avec les 14 extraits requis par synced_excerpts_catalog
    (trousse_dir / "schemas").mkdir(parents=True, exist_ok=True)
    (trousse_dir / "harness_proto").mkdir(parents=True, exist_ok=True)
    (trousse_dir / "authz_pqc_audit").mkdir(parents=True, exist_ok=True)
    (trousse_dir / "policies_opa").mkdir(parents=True, exist_ok=True)
    (trousse_dir / "policy_saga").mkdir(parents=True, exist_ok=True)
    (trousse_dir / "evalops_prr").mkdir(parents=True, exist_ok=True)

    synced_excerpts = {}
    sample_lines = ["def synced_demo() -> str:", '    return "OK"']
    for item in manifest["synced_excerpts_catalog"]:
        eid = item["id"]
        rel = item["source_path"]
        p = trousse_dir / rel
        if item.get("is_full_file"):
            content_lines = ['{"$schema": "https://json-schema.org/draft/2020-12/schema", "type": "object"}']
            p.write_text("\n".join(content_lines) + "\n", encoding="utf-8", newline="\n")
            lines_rng = "1-1"
            sha = compute_excerpt_sha256(content_lines)
            lc = 1
        else:
            content = (
                "# SPDX-License-Identifier: MIT\n"
                f"# CA-G0-SYNC-BEGIN:{eid}\n"
                + "\n".join(sample_lines)
                + f"\n# CA-G0-SYNC-END:{eid}\n"
            )
            if p.is_file():
                prev = p.read_text(encoding="utf-8")
                start_ln = len(prev.splitlines()) + 2
                p.write_text(prev + f"# CA-G0-SYNC-BEGIN:{eid}\n" + "\n".join(sample_lines) + f"\n# CA-G0-SYNC-END:{eid}\n", encoding="utf-8", newline="\n")
            else:
                start_ln = 3
                p.write_text(content, encoding="utf-8", newline="\n")
            lines_rng = f"{start_ln}-{start_ln + 1}"
            sha = compute_excerpt_sha256(sample_lines)
            lc = 2
        synced_excerpts[eid] = {
            "unit": item["unit"],
            "source_path": f"Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/{rel}",
            "lines": lines_rng,
            "line_count": lc,
            "sha256": sha,
        }

    aq_dir = book_dir / "aq"
    aq_dir.mkdir(parents=True)
    g0_report = {
        "schema_version": "1.0.0",
        "executed_at": "2026-12-02T12:00:00Z",
        "freeze_date": "2026-12-02",
        "platform": {"os": "windows", "python_version": "3.14.10", "opa_version": "1.22.4", "opa_sha256": "a" * 64},
        "overall_status": "PASS",
        "exit_code": 0,
        "spdx_check": {"license_target": "MIT", "checked_files": 50, "checked_packages": 18, "violations": [], "passed": True},
        "lockfile_check": {"path": "requirements.lock", "sha256": "b" * 64, "all_hashes_pinned": True, "passed": True},
        "schema_validation": {"schemas_checked": 21, "strict_violations": [], "passed": True},
        "opa_check": {"files_checked": 3, "missing_default_deny": [], "coverage_pct": 100.0, "tests_passed": 45, "tests_failed": 0},
        "pytest_check": {"passed": 83, "failed": 0, "skipped": 0, "modules": {"test_all": 83}},
        "third_party_vectors": {
            "rfc8785": {"passed": True, "file_count": 20},
            "nist_acvp": {"passed": True, "file_count": 12},
            "a2a_tck": {"passed": True, "file_count": 5},
            "owasp_src055": {"passed": True, "file_count": 13},
        },
        "synced_excerpts": synced_excerpts,
    }
    (aq_dir / "rapports-g0.json").write_text(json.dumps(g0_report, indent=2), encoding="utf-8", newline="\n")

    # Sources L+ couvrant D01..D12 (3 par domaine = 36)
    lplus_dir = book_dir / "recherche" / "corpus_l_plus"
    lplus_dir.mkdir(parents=True)
    sources_entries = []
    for i in range(1, 37):
        sid = f"SRC-{i:03d}"
        dom = DOMAINS[(i - 1) % 12]
        txt_rel = f"recherche/corpus_l_plus/{sid}.txt"
        txt_path = book_dir / txt_rel
        content = f"Texte intégral primaire {sid} pour {dom}. Normes vérifiées au 2 décembre 2026.\n" * 4
        txt_path.write_text(content, encoding="utf-8", newline="\n")
        digest = hashlib.sha256(txt_path.read_bytes()).hexdigest()
        sources_entries.append({
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
            "research_axes": [dom],
            "local_txt_path": txt_rel,
            "sha256": digest,
            "byte_length": len(content.encode("utf-8")),
            "word_count": len(content.split()),
        })

    (book_dir / "recherche" / "manifeste-sources-sha256.json").write_text(
        json.dumps({"protocol_id": "MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0", "freeze_date": "2026-12-02", "metadata_only_pct": 0.0, "sources": sources_entries}, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (book_dir / "recherche" / "registre-statut-f.json").write_text(
        json.dumps({"freeze_date": "2026-12-02", "blocked": []}, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )

    # 7 registres JSON SSOT
    reg_dir = book_dir / "registre"
    reg_dir.mkdir(parents=True)
    (reg_dir / "mindmap-complet.json").write_text(
        json.dumps({"registry_version": "1.0.0", "freeze_date": "2026-12-02", "nodes": mm_src["nodes"], "relations": mm_src["relations"], "domains": mm_src["domains"]}, ensure_ascii=False),
        encoding="utf-8",
        newline="\n",
    )
    (reg_dir / "ancres-chronologiques.json").write_text(
        json.dumps({
            "registry_version": "1.0.0",
            "freeze_date": "2026-12-02",
            "anchors": [
                {"key": "2027-03-30-MCP-SEP-3398", "date": "2027-03-30", "nature": "Revision", "jurisdiction": "International", "label": "SEP-3398", "chapters": ["ch07"], "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"},
                {"key": "2027-05-01-BSIF-E23-AMF", "date": "2027-05-01", "nature": "Prudentiel", "jurisdiction": "Canada", "label": "BSIF E-23", "chapters": ["ch25"], "statut_preuve": "l_plus", "source_l_plus_id": "SRC-002"},
            ],
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (reg_dir / "faits-empiriques.json").write_text(
        json.dumps({
            "registry_version": "1.0.0",
            "freeze_date": "2026-12-02",
            "facts": [
                {"id": "FACT-MCP-DRIFT-4058", "metric": "Dérive MCP", "value": "40,58 %", "source": "Corpus", "owner_chapter": "ch07", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"},
            ],
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (reg_dir / "glossaire-termes.json").write_text(
        json.dumps({
            "registry_version": "1.0.0",
            "freeze_date": "2026-12-02",
            "terms": [
                {"fr": f"terme normatif {i}", "en": f"normative term {i}", "definition": "Définition.", "chapitre_proprietaire": f"ch{(i % 36) + 1:02d}"}
                for i in range(12)
            ],
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (reg_dir / "specifications-lplus.json").write_text(
        json.dumps({
            "registry_version": "1.0.0",
            "freeze_date": "2026-12-02",
            "specs": [{"spec_id": "RFC-8785", "title": "JCS", "version_or_tag": "RFC 8785", "maturity_status": "FINAL_STANDARD", "license_spdx": "IETF-Trust", "source_l_plus_id": "SRC-001", "sha256": sources_entries[0]["sha256"], "statut_preuve": "l_plus", "modules_trousse": ["harness_proto"], "adapter_boundary": None}],
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (reg_dir / "matrice-exig-prr-c40.json").write_text(
        json.dumps({
            "registry_version": "1.0.0",
            "freeze_date": "2026-12-02",
            "mappings": [{"id": "EXIG-SEC-06", "family": "EXIG", "criticality": "BLOQUANT", "owner_chapter": "ch20", "trousse_module": "policies_opa", "implementation_symbol": "rule_of_two.allow", "rego_rule": "trousse.policy.rule_of_two.allow", "pytest_nodeid": "tests/test_policy_saga.py::test_rule_of_two", "third_party_vector_suite": "owasp_src055", "corpus_anchor": "Tome 2"}],
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    (reg_dir / "concordance-taxonomies.json").write_text(
        json.dumps({
            "registry_version": "1.0.0",
            "freeze_date": "2026-12-02",
            "concordances": [
                {"discordance_id": f"DISC-0{i}", "topic": f"Discordance {i}", "volume_variants": [{"volume": "T6", "definition": "A", "corpus_ref": "T6"}, {"volume": "T7", "definition": "B", "corpus_ref": "T7"}], "canonical_vol8_choice": f"Choix {i}", "liminaire_section": "0.2", "rationale": "Arbitrage."}
                for i in range(1, 6)
            ],
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )

    # 37 bases sources
    src_dir = book_dir / "sources"
    src_dir.mkdir(parents=True)
    for u in manifest["units"]:
        if u["kind"] in {"frontmatter", "chapter"}:
            uid = u["id"]
            sname = "ch00-sources.md" if uid == "00-liminaire" else f"{uid}-sources.md"
            (src_dir / sname).write_text(
                f"# Sources — {uid}\n\nDate de gel des faits : 2 décembre 2026\n\n"
                "### [1] SRC-001 — Source empirique\nRésumé vérifié.\n\n"
                "### [2] SRC-002 — Source réglementaire\nRésumé vérifié.\n\n"
                "### [3] SRC-003 — Source technique\nRésumé vérifié.\n",
                encoding="utf-8",
                newline="\n",
            )

    # 115 schémas + rendus
    sch_dir = book_dir / "schemas"
    rendus_dir = sch_dir / "rendus"
    rendus_dir.mkdir(parents=True)
    puml_nodes = "\n".join(f'rectangle "Bloc {i}" as N{i}' for i in range(1, 7))
    mmd_edges = "\n".join(f'  N{i}["Noeud {i}"] --> N{i + 1}["Noeud {i + 1}"]' for i in range(1, 6))
    svg_stub = '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="240">' + "".join(f'<rect id="n{i}" data-node="true" x="{i*10}" y="10" width="8" height="8"/>' for i in range(6)) + "</svg>"
    fig_ext_map = {}
    for fmeta in manifest["figures"]:
        fid = fmeta["id"]
        eng = fmeta["engine"]
        if eng == "puml":
            fig_ext_map[fid] = "svg"
            (sch_dir / f"{fid}.puml").write_text(f"@startuml\n{puml_nodes}\nN1 --> N6\n@enduml\n", encoding="utf-8", newline="\n")
            (rendus_dir / f"{fid}.svg").write_text(svg_stub, encoding="utf-8", newline="\n")
        elif eng == "mmd":
            fig_ext_map[fid] = "png"
            (sch_dir / f"{fid}.mmd").write_text(f"flowchart TD\n{mmd_edges}\n", encoding="utf-8", newline="\n")
            (rendus_dir / f"{fid}.png").write_bytes(_make_valid_png_bytes())
        else:
            fig_ext_map[fid] = "svg"
            (sch_dir / f"{fid}.svg").write_text(svg_stub, encoding="utf-8", newline="\n")
            (rendus_dir / f"{fid}.svg").write_text(svg_stub, encoding="utf-8", newline="\n")

    # Copier aussi les fichiers Cartographie nécessaires à Annexe E si besoin (optionnel, testé via fallback)
    gloss_terms = json.loads((reg_dir / "glossaire-termes.json").read_text(encoding="utf-8"))["terms"]
    terms_by_owner: dict[str, list[str]] = {}
    for t in gloss_terms:
        terms_by_owner.setdefault(t["chapitre_proprietaire"], []).append(t["fr"])

    synced_ch04 = (
        f'<!-- CA-G0-SYNC id="G0-EX-CH01-02" path="Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/pipeline.py" lines="{synced_excerpts["G0-EX-CH01-02"]["lines"]}" sha256="{synced_excerpts["G0-EX-CH01-02"]["sha256"]}" -->\n'
        "```python\n" + "\n".join(sample_lines) + "\n```\n\n"
    )

    for u in manifest["units"]:
        if u["kind"] in {"frontmatter", "chapter"}:
            out = book_dir / u["file"]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                _build_valid_unit_text(
                    u,
                    fig_ext_map=fig_ext_map,
                    owner_terms=terms_by_owner.get(u["id"], []),
                    synced_excerpt_block=synced_ch04 if u["id"] == "ch04" else "",
                ),
                encoding="utf-8",
                newline="\n",
            )

    build_annexes(book_dir)
    return book_dir


@pytest.fixture()
def tmp_compendium(tmp_path: Path) -> Path:
    return _create_populated_compendium(tmp_path)


def test_communs_prioritizes_protocole_mlr_compendium(tmp_path: Path) -> None:
    specs_dir = tmp_path / "specs"
    specs_dir.mkdir(parents=True)
    (specs_dir / "protocole-mlr-2027.json").write_text(json.dumps({"freeze_date": "2026-11-11"}), encoding="utf-8")
    (specs_dir / "protocole-mlr-compendium.json").write_text(json.dumps({"freeze_date": "2026-12-02"}), encoding="utf-8")
    assert get_freeze_date(tmp_path) == "2026-12-02"


def test_clean_populated_compendium_passes_strict(tmp_compendium: Path) -> None:
    assert check_manuscrit(tmp_compendium, sources_only=True) == []
    assert check_manuscrit(tmp_compendium, strict=True) == []


def test_compendium_budget_and_owned_concepts(tmp_compendium: Path) -> None:
    ch01 = tmp_compendium / "manuscrit" / "01 - Partie I" / "Chapitre 01.md"
    ch02 = tmp_compendium / "manuscrit" / "01 - Partie I" / "Chapitre 02.md"
    # Provoquer sous-calibrage CA-01 sur ch01 et collision CA-21 (slug de ch01 dupliqué en ch02)
    ch01.write_text("# Chapitre 01\n\n*Question directrice : Q ?*\n\nTexte trop court [1].\n", encoding="utf-8", newline="\n")
    ch02_txt = ch02.read_text(encoding="utf-8")
    ch02.write_text(
        ch02_txt.replace("Périmètre exclusif :", "Périmètre exclusif : `echanges-intentions-contrats-probabilistes`,", 1),
        encoding="utf-8",
        newline="\n",
    )

    errors = check_manuscrit(tmp_compendium, strict=True)
    assert any("CA-01" in e for e in errors)
    assert any("CA-21" in e for e in errors)


def test_compendium_fr_ca_hygiene_and_ca_g0_sync(tmp_compendium: Path) -> None:
    ch04 = tmp_compendium / "manuscrit" / "02 - Partie II" / "Chapitre 04.md"
    orig = ch04.read_text(encoding="utf-8")
    # Injecter violations CA-22 (on, Systems of Agency, 99.5 %, ->, <=, $ nu) et CA-G0-SYNC (divergence 1 octet)
    dirty = orig.replace('return "OK"', 'return "NOK"', 1).replace(
        "Paragraphe 0",
        "Dans les Systems of Agency, l'on observe <= 5 et 99.5 % -> coût 10 $ [1]. Paragraphe 0",
        1,
    )
    ch04.write_text(dirty, encoding="utf-8", newline="\n")

    errors = check_manuscrit(tmp_compendium, strict=True, unit_id="ch04")
    assert any("CA-22" in e and "Systèmes d'agentivité" in e for e in errors)
    assert any("CA-22" in e and "on" in e.lower() for e in errors)
    assert any("CA-06" in e for e in errors)
    assert any("CA-G0-SYNC" in e for e in errors)


def test_ao03_allows_compendium_ids_and_rejects_raw_markers_outside_ch36(tmp_compendium: Path) -> None:
    ch05 = tmp_compendium / "manuscrit" / "02 - Partie II" / "Chapitre 05.md"
    txt = ch05.read_text(encoding="utf-8")
    txt = txt.replace(
        "Paragraphe 0",
        "Les codes EXIG-SEC-06, CAP-046, ADR-001, POR-001, PRR, PEX-001, C01–C40, SBB, SCH-05-01, INI-043, SIG-001, DIV-02 et DISC-01..DISC-05 sont admis, mais [S] et [L+] restent bannis hors CH-36 [1]. Paragraphe 0",
        1,
    )
    ch05.write_text(txt, encoding="utf-8", newline="\n")
    errors = check_manuscrit(tmp_compendium, strict=True, unit_id="ch05")
    for allowed in ("EXIG-SEC-06", "CAP-046", "ADR-001", "POR-001", "PEX-001", "SCH-05-01", "INI-043", "SIG-001", "DIV-02", "DISC-01"):
        assert not any(allowed in e for e in errors)
    assert any("CA-02" in e and "[S]" in e for e in errors)
    assert any("CA-02" in e and "[L+]" in e for e in errors)


def test_disjoint_148_item_stratified_samples(tmp_compendium: Path) -> None:
    s1 = draw_stratified_sample(tmp_compendium, seed=20270901, exclude_ids=set())
    excluded = {x["claim_loc"] for x in s1} | {x["paragraph_loc"] for x in s1}
    s2 = draw_stratified_sample(tmp_compendium, seed=20270902, exclude_ids=excluded)

    assert len(s1) == 148 and len(s2) == 148
    assert {x["claim_loc"] for x in s1}.isdisjoint({x["claim_loc"] for x in s2})
    assert {x["paragraph_loc"] for x in s1}.isdisjoint({x["paragraph_loc"] for x in s2})

    for sample in (s1, s2):
        for cat in ("empirique", "juridique", "spec_technique", "assertions_g0"):
            assert sum(1 for x in sample if x["category"] == cat) == 37
        narrative_ids = ["00-liminaire"] + [f"ch{i:02d}" for i in range(1, 37)]
        assert all(sum(1 for x in sample if x["unit"] == u) >= 4 for u in narrative_ids)


def test_genere_annexes_5_units_deterministic_and_ca17(tmp_compendium: Path) -> None:
    out1 = build_annexes(tmp_compendium, dry_run=True)
    out2 = build_annexes(tmp_compendium, dry_run=True)
    assert len(out1) == 5
    assert out1 == out2

    manifest = json.loads((tmp_compendium / "specs" / "manifest.json").read_text(encoding="utf-8"))
    for u in manifest["units"]:
        if u["kind"] == "annex":
            p = tmp_compendium / u["file"]
            wc = count_prose_words(p.read_text(encoding="utf-8"))
            assert u["min_words"] <= wc <= u["max_words"], f"{u['id']}: {wc}"

    ann_a = tmp_compendium / "manuscrit" / "13 - Annexes" / "Annexe A - Tracabilite MindMap et socle probatoire.md"
    ann_a.write_text(ann_a.read_text(encoding="utf-8") + "\nÉdition manuelle interdite.", encoding="utf-8", newline="\n")
    errors = check_manuscrit(tmp_compendium, strict=True)
    assert any("CA-17" in e for e in errors)


def test_assemble_livre_clean_and_normalize_sch_paths(tmp_compendium: Path) -> None:
    liv = tmp_compendium / "livrables"
    liv.mkdir(parents=True, exist_ok=True)
    for fn in ("Compendium.md", "Compendium.html", "Compendium.pdf", "temp.typ", "temp.tmp", "stray.html"):
        (liv / fn).write_text("stub", encoding="utf-8")

    _clean_residual_livrables(tmp_compendium)
    remaining = sorted(p.name for p in liv.iterdir())
    assert remaining == ["Compendium.html", "Compendium.md", "Compendium.pdf"]

    sample_md = "![S1](../../schemas/rendus/SCH-00-01.svg) ![S2](SCH-00-04.png)"
    fig_map = {"SCH-00-01": "svg", "SCH-00-04": "png"}
    norm_md = _normalize_image_paths(sample_md, fig_map, prefix="../schemas/rendus")
    assert norm_md == "![S1](../schemas/rendus/SCH-00-01.svg) ![S2](../schemas/rendus/SCH-00-04.png)"
    norm_typ = _normalize_image_paths(sample_md, fig_map, prefix="/Compendium/ouvrage/schemas/rendus")
    assert norm_typ == "![S1](/Compendium/ouvrage/schemas/rendus/SCH-00-01.svg) ![S2](/Compendium/ouvrage/schemas/rendus/SCH-00-04.png)"


def test_12gram_ignores_quoted_statute_titles_only(tmp_compendium: Path) -> None:
    ch04 = tmp_compendium / "manuscrit" / "02 - Partie II" / "Chapitre 04.md"
    orig = ch04.read_text(encoding="utf-8")

    quoted = orig.replace(
        "Paragraphe 0",
        "La loi citée est « Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application » [1]. Paragraphe 0",
        1,
    )
    ch04.write_text(quoted, encoding="utf-8", newline="\n")
    assert not any("CA-03" in e for e in check_manuscrit(tmp_compendium, strict=True, unit_id="ch04"))

    unquoted = orig.replace(
        "Paragraphe 0",
        "Selon la Loi sur la protection des renseignements personnels dans le secteur privé du Québec et ses règlements d'application, la preuve est requise [1]. Paragraphe 0",
        1,
    )
    ch04.write_text(unquoted, encoding="utf-8", newline="\n")
    assert any("CA-03" in e for e in check_manuscrit(tmp_compendium, strict=True, unit_id="ch04"))


def test_g2_gate_rejects_unresolved_unsupported_claims(tmp_compendium: Path) -> None:
    ancrage_dir = tmp_compendium / "ancrage"
    ancrage_dir.mkdir(parents=True, exist_ok=True)
    for i in range(37):
        aname = f"ch{i:02d}-ancrage.md"
        if i == 1:
            content = (
                f"# Journal d'ancrage {aname}\n\n"
                "- **Passe G2 initiale (supportés) :** 3\n"
                "- **Verdict final — supportés :** 3 / 4 (75,0 %)\n\n"
                "- `C01-01` — Verdict : supporté\n"
                "- `C01-02` — Verdict : non supporté\n"
            )
        elif i == 2:
            content = (
                f"# Journal d'ancrage {aname}\n\n"
                "- **Passe G2 initiale (supportés) :** 3\n"
                "- **Verdict final — supportés :** 3 / 4 (75,0 %)\n\n"
                "- `C02-01` — Verdict : supporté\n"
                "- `C02-02` — Verdict : imprécis\n"
            )
        else:
            content = (
                f"# Journal d'ancrage {aname}\n\n"
                "- **Passe G2 initiale (supportés) :** 4\n"
                "- **Verdict final — supportés :** 4 / 4 (100,0 %)\n\n"
                "- `C00-01` — Verdict : supporté\n"
            )
        (ancrage_dir / aname).write_text(content, encoding="utf-8", newline="\n")

    errors = check_manuscrit(tmp_compendium, strict=True)
    assert any("CA-12" in e and "non supporté" in e for e in errors)
    assert any("CA-12" in e and "imprécis" in e for e in errors)

    # Une fois les deux journaux résolus à 100 % supporté et les annexes resynchronisées, G1 strict passe sans erreur
    for idx in (1, 2):
        aname = f"ch{idx:02d}-ancrage.md"
        (ancrage_dir / aname).write_text(
            f"# Journal d'ancrage {aname}\n\n"
            "- **Passe G2 initiale (supportés) :** 3\n"
            "- **Verdict final — supportés :** 4 / 4 (100,0 %)\n"
            "- Non supportés : 0\n"
            "- Imprécis : 0\n\n"
            f"- `C{idx:02d}-01` — Verdict : supporté\n",
            encoding="utf-8",
            newline="\n",
        )
    build_annexes(tmp_compendium)
    assert check_manuscrit(tmp_compendium, strict=True) == []
