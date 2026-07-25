# -*- coding: utf-8 -*-
"""check-toc.py — contrôles de publication du TOC du Vol. IV (La somme agentique).

Reconstruction du 23 juillet 2026 (le script historique des passes v0.3-v0.6 est
introuvable au dépôt — constat v0.7, reconduit v0.8-v0.11). Domaine : chapitres
1-57, dix livres I-X, conformément au protocole du CLAUDE.md du dossier.

Sortie 0 si tout passe, 1 sinon. À exécuter avant toute publication de TOC.md.

Zones gelées (exemptées des contrôles de motifs, jamais des lectures) :
  - rangées « | Historique » du bandeau ;
  - sections de journal (## Corrections apportées / ## Révision / ## Actualisation).
Les spans entre guillemets « … » sont retirés avant les contrôles de motifs :
la décision 7 et le champ Contrôles citent les formes fautives en exemple.

Faux positifs neutralisés (ne pas « simplifier » ces exemptions) :
  - les mentions historiques « Livre XI/XII/XIII » annotées d'un marqueur de
    correspondance (v0.8, v0.9, ancien…, aujourd'hui, entrée en, depuis la)
    sont légitimes en zone normative (Nature, décisions 9-10, risques 1 et 13) ;
  - l'enveloppe des annexes (~89 000 mots) n'est pas en fin d'en-tête : elle
    est délibérément hors de la somme contrôlée des enveloppes de tête (305) ;
  - « R-0N » (deux chiffres) est la série du Vol. III, auto-nommante — seul le
    « R-N » à un chiffre sans « Vol. II » à portée est indécidable (contrôle 11
    historique) ;
  - « PEAS », « OO1-OO4 », etc. ne matchent aucun motif : aucune exclusion requise.
"""

import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOC = HERE / "TOC.md"
CONSPECTUS = HERE / "README.md"   # vue synoptique dérivée (le « conspectus »), renommée README.md
if not CONSPECTUS.exists():        # layout PRD/ : le README (conspectus) vit à la racine du dossier
    CONSPECTUS = HERE.parent / "README.md"

N_CHAPTERS = 57
BOOKS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
ROMAN_OK = set(BOOKS)
ENVELOPE_SUM = 305          # 301 corps + 4 avant-propos (enveloppes de tête)
ANNEX_ENVELOPE = 89
TOTAL_HIGH = 394            # 305 + 89
VOL3_TOC_REFS = 11          # « onze renvois » — décision 7 (re-mesuré 23 juill. 2026)
LACUNES = [f"§10.{i}" for i in range(1, 12)]   # onze lacunes du PRD Vol. II
CORPUS_CONSUMERS = [15, 18, 44, 47, 49, 50]     # + Annexe G, contrôlée à part
RELEVE_V10 = [20, 21, 22, 26, 43, 44, 52, 53, 54, 55, 57]
RELEVE_V11 = [9, 19, 40, 44, 55]
JOURNAL_RELEVES = {"v0.10": 8, "v0.11": 6}
CORRESPONDENCE_MARKERS = re.compile(
    r"ancien|anciennement|aujourd'hui|entrée en|depuis la|v0\.8|v0\.9|→")

failures = []


def fail(control, msg):
    failures.append(f"[{control}] {msg}")


def strip_guillemets(text):
    """Retire les spans « … » et `…` : citations d'exemples fautifs et formes
    de référence de la décision 7 — des méta-mentions, pas des renvois."""
    text = re.sub(r"«[^«»]*»", "«»", text)
    return re.sub(r"`[^`]*`", "``", text)


def load():
    lines = TOC.read_text(encoding="utf-8").splitlines()
    frozen = [False] * len(lines)
    in_journal = False
    for i, line in enumerate(lines):
        if re.match(r"^## (Corrections apportées en|Révision|Actualisation) v0\.\d+", line):
            in_journal = True
        elif line.startswith("## Risques"):
            in_journal = False
        elif line.startswith("# ") and in_journal:
            in_journal = False
        if in_journal or line.startswith("| Historique"):
            frozen[i] = True
    return lines, frozen


def sentence_segments(text):
    """Segmente en phrases après masquage des points non terminaux (« Vol. II »,
    « §8.4 », « ch. 19 », mois abrégés) — sans quoi la segmentation couperait la
    mention de volume de son garde-fou et fabriquerait des faux positifs."""
    text = text.replace("Vol. III", "VOL3").replace("Vol. II", "VOL2").replace("Vol. I", "VOL1")
    text = re.sub(r"(?<=\d)\.(?=\d)", "_", text)
    text = re.sub(r"\b(ch|art|juill|janv|févr|avr|sept|oct|nov|déc)\.", r"\1_", text)
    return re.split(r"[.;]", text)


def chapter_bodies(lines):
    """{n: texte de l'entrée du chapitre n (titre inclus, jusqu'au titre suivant)}"""
    bodies, current, buf = {}, None, []
    for line in lines:
        m = re.match(r"^### Chapitre (\d+) ", line)
        if m:
            if current is not None:
                bodies[current] = "\n".join(buf)
            current, buf = int(m.group(1)), [line]
        elif line.startswith("# ") or line.startswith("## "):
            if current is not None:
                bodies[current] = "\n".join(buf)
                current, buf = None, []
        elif current is not None:
            buf.append(line)
    if current is not None:
        bodies[current] = "\n".join(buf)
    return bodies


def main():
    lines, frozen = load()
    text = "\n".join(lines)
    norm_lines = [(i, l) for i, l in enumerate(lines) if not frozen[i]]
    norm_text = "\n".join(l for _, l in norm_lines)
    norm_clean = strip_guillemets(norm_text)
    bodies = chapter_bodies(lines)

    # C1 — chapitres 1-57 contigus et uniques
    nums = [int(m.group(1)) for m in re.finditer(r"^### Chapitre (\d+) ", text, re.M)]
    if nums != list(range(1, N_CHAPTERS + 1)):
        fail("C1", f"chapitres non contigus/uniques 1-{N_CHAPTERS} : {nums}")

    # C2 — dix livres I-X dans l'ordre
    books = re.findall(r"^# LIVRE ([IVX]+) ", text, re.M)
    if books != BOOKS:
        fail("C2", f"livres attendus {BOOKS}, trouvés {books}")

    # C3 — enveloppes de tête : somme 305, forme réservée, total 394
    envs = [int(m.group(1).replace(" ", ""))
            for m in re.finditer(r"~(\d+) 000 mots\)\*", norm_text)]
    if sum(envs) != ENVELOPE_SUM:
        fail("C3", f"somme des enveloppes de tête = {sum(envs)}, attendu {ENVELOPE_SUM} ({envs})")
    if len(envs) != 11:
        fail("C3", f"{len(envs)} enveloppes de tête trouvées, attendu 11 (10 livres + avant-propos)")
    if f"~{ANNEX_ENVELOPE} 000 mots" not in norm_text:
        fail("C3", "enveloppe des annexes (~89 000 mots) absente")
    if ENVELOPE_SUM + ANNEX_ENVELOPE != TOTAL_HIGH:
        fail("C3", "arithmétique 305 + 89 != 394")
    if not re.search(r"369\s?000[–-]394\s?000", norm_text):
        fail("C3", "fourchette « 369 000–394 000 » absente des zones normatives")
    # forme ~N 000 mots hors ligne d'en-tête (en-tête = ligne italique *(...)* ou titre #)
    for i, l in norm_lines:
        if re.search(r"~\d+ 000 mots", l) and not (
                l.startswith("#") or l.startswith("*(") or "*(" in l):
            fail("C3", f"ligne {i+1} : forme « ~N 000 mots » hors enveloppe de tête")

    # C4 — aucun renvoi « ch. N » hors 1-57 (fichier entier)
    for m in re.finditer(r"\bch\. (\d+)", text):
        n = int(m.group(1))
        if not 1 <= n <= N_CHAPTERS:
            fail("C4", f"renvoi pendant « ch. {n} »")

    # C5 — aucun numéral de livre hors I-X en zone normative, sauf correspondance annotée
    for i, l in norm_lines:
        for m in re.finditer(r"\bLivres? ([IVX]+(?:[-,][IVX]+)*)\b", strip_guillemets(l)):
            for token in re.split(r"[-,]", m.group(1)):
                if token and token not in ROMAN_OK and not CORRESPONDENCE_MARKERS.search(l):
                    fail("C5", f"ligne {i+1} : « Livre {token} » hors I-X sans marqueur de correspondance")

    # C6 — renvoi « Vol. III § » sans document nommé (décision 7)
    for i, l in norm_lines:
        if re.search(r"(?<!du )Vol\. III §", strip_guillemets(l)):
            fail("C6", f"ligne {i+1} : « Vol. III § » nu — nommer TOC/PRD/PRDPlan (décision 7)")

    # C7 — « Vol. II Annexe B » sans document nommé (contrôle 17 historique).
    # Le contexte est borné à la ligne courante : un ancrage « .{40} » ne
    # franchirait pas un début de ligne et raterait toute occurrence précoce.
    for m in re.finditer(r"Vol\. II Annexe B", norm_clean):
        ctx = norm_clean[max(0, m.start() - 60):m.start()].rsplit("\n", 1)[-1]
        if "Monographie" not in ctx and "PRD" not in ctx:
            fail("C7", f"« Vol. II Annexe B » sans document nommé : …{ctx[-50:]}⟨ici⟩")

    # C8 — R-N à un chiffre sans « Vol. II » à portée de phrase, dans un chapitre
    # consommant le Vol. III (contrôle 11 historique)
    for n, body in bodies.items():
        if "Vol. III" not in body:
            continue
        for seg in sentence_segments(strip_guillemets(body)):
            for m in re.finditer(r"\bR-(\d)\b(?!\d)", seg):
                if "VOL2" not in seg:
                    fail("C8", f"ch. {n} : « R-{m.group(1)} » nu (chapitre mixte, décision 7)")

    # C9 — registre des onze lacunes : complétude et portage effectif
    reg_rows = {}
    for l in lines:
        m = re.match(r"^\s*\|\s*(§10\.\d+)\s*\|.*\|\s*(.*)\|\s*$", l)
        if m:
            reg_rows[m.group(1)] = m.group(2)
    missing = [x for x in LACUNES if x not in reg_rows]
    extra = [x for x in reg_rows if x not in LACUNES]
    if missing or extra:
        fail("C9", f"registre Annexe C : manquantes {missing}, inattendues {extra}")
    for lac, cell in reg_rows.items():
        porters = [int(x) for x in re.findall(r"ch\. (\d+)", cell)]
        if porters and not any(lac in bodies.get(p, "") for p in porters):
            fail("C9", f"lacune {lac} : aucun des chapitres désignés ({porters}) ne la nomme")

    # C10 — mention « corpus d'appui » dans chaque consommateur déclaré
    for n in CORPUS_CONSUMERS:
        if "corpus d'appui" not in bodies.get(n, ""):
            fail("C10", f"ch. {n} : consommateur déclaré sans mention « corpus d'appui »")
    annexe_g = re.search(r"\*\*Annexe G — .*", text)
    if not annexe_g or "corpus d'appui" not in annexe_g.group(0):
        fail("C10", "Annexe G : mention « corpus d'appui » absente")

    # C11 — marques de relève et décomptes des journaux v0.10/v0.11
    for version, chapters in (("v0.10", RELEVE_V10), ("v0.11", RELEVE_V11)):
        for n in chapters:
            if not re.search(r"relèves? " + re.escape(version), bodies.get(n, ""), re.I):
                fail("C11", f"ch. {n} : marque « relève {version} » absente")
    for version, expected in JOURNAL_RELEVES.items():
        m = re.search(r"^## (?:Actualisation|Révision) " + re.escape(version) + r".*?(?=^## |\Z)",
                      text, re.M | re.S)
        if not m:
            fail("C11", f"journal {version} introuvable")
            continue
        count = len(re.findall(r"^\*\*\d+\.", m.group(0), re.M))
        if count != expected:
            fail("C11", f"journal {version} : {count} relèves numérotées, {expected} annoncées au bandeau")

    # C12 — cardinal en toutes lettres des renvois nommés au Vol. III (décision 7 : onze)
    refs = len(re.findall(r"Vol\. III \*TOC\* §", strip_guillemets(norm_text)))
    if refs != VOL3_TOC_REFS:
        fail("C12", f"{refs} renvois « Vol. III *TOC* §N.x » en zone normative, "
                    f"le cardinal annoncé (onze = {VOL3_TOC_REFS}) est périmé — re-mesurer et reporter")

    # C13 — cardinal « 57 chapitres » cohérent en zone normative
    for m in re.finditer(r"\b(\d\d) chapitres", norm_text):
        n = int(m.group(1))
        if 40 <= n <= 99 and n != N_CHAPTERS:
            fail("C13", f"« {n} chapitres » en zone normative (attendu {N_CHAPTERS})")

    # C14 — alignement du conspectus : version identique, ou mention explicite
    # « retard déclaré » en tête. Le mot « retard » seul ne suffit pas — la
    # rangée Régénération du conspectus l'emploie dans l'énoncé de la règle
    # elle-même, ce qui neutraliserait le contrôle.
    m = re.search(r"^\| Version\s*\|\s*\*\*0\.(\d+) —", text, re.M)
    toc_version = f"v0.{m.group(1)}" if m else None
    if toc_version is None:
        fail("C14", "version du TOC introuvable au bandeau")
    elif CONSPECTUS.exists():
        ctext = CONSPECTUS.read_text(encoding="utf-8")
        src = re.search(r"^\| Source \|.*?\*\*(v0\.\d+)\*\*", ctext, re.M)
        head = "\n".join(ctext.splitlines()[:15]).lower()
        if (not src or src.group(1) != toc_version) and "retard déclaré" not in head:
            fail("C14", f"Conspectus non aligné sur {toc_version} et sans « retard déclaré » en tête")

    if failures:
        print(f"ÉCHEC — {len(failures)} défaut(s) :")
        for f_ in failures:
            print("  " + f_)
        return 1
    print("OK — tous les contrôles passent (C1-C14).")
    return 0


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.exit(main())
