#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de mutation de `check-compendium.py`.

Doctrine du dépôt : *un script de contrôle est du contenu, il se vérifie comme
le reste.* La validation se fait en **deux temps, et le premier n'est pas
facultatif** :

  1. constater ce que le contrôle rend sur le **corpus intact** ;
  2. introduire chaque classe de faute et constater qu'il **la voit**.

*Sans le premier temps, un script cassé « détecte » tout et se croit bon.*

⚠ **Le temps 1 est ici une LIGNE DE BASE ÉPINGLÉE, non un « sortie 0 », et le
motif se déclare plutôt qu'il ne se tait.** Le contrôle trouve **cinq défauts
réels** sur le corpus intact — cinq cardinaux d'en-tête que le corps ne
reproduit pas —, et **la passe qui construit ce script n'a pas mandat de
corriger les pièces**. Trois façons de traiter cela, dont deux sont fausses :
supprimer les cinq contrôles (*un contrôle supprimé est une spécification*), les
rendre déclaratifs (*ils sont réels et corrigeables : les déclarer serait les
enterrer*), ou **épingler la ligne de base et exiger que chaque mutation ajoute
un échec qui n'y figure pas**. C'est la troisième qui est retenue. Elle tient la
propriété que le temps 1 protège : *si le script se casse, il produira plus que
la ligne de base sur le corpus intact, et le harnais le dira.*

☐ **Dette déclarée** : la ligne de base est **retombée à zéro le 28 juillet 2026** — les cinq défauts réels
trouvés au premier passage ont été corrigés sur pièce dans la passe même qui a construit ce contrôle,
plutôt qu'épinglés. *Un contrôle neuf qui naît en échec s'enseigne comme un contrôle qu'on ignore.*
Toute remontée de la ligne de base au-dessus de zéro se déclare ici avec son motif et son échéance
à mesure que les pièces sont corrigées. **Une ligne de base qui ne décroît jamais
est une exemption déguisée.**

Le corpus réel n'est jamais muté : chaque mutation s'applique à une copie
jetable, que `check-compendium.py` lit via la variable `COMPENDIUM_RACINE`.

Usage :  python check-compendium-mutations.py
Sortie 0 si la ligne de base est tenue ET que les mutations sont toutes vues.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(os.environ.get("COMPENDIUM_RACINE", Path(__file__).resolve().parent.parent))
SCRIPT = Path(__file__).resolve().parent / "check-compendium.py"

# La console Windows par défaut est en cp1252 et ne sait pas écrire « ☑ ».
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CH01 = "Livre I/01-interoperabilite-integration-entreprise.md"
CH03 = "Livre I/03-securite-identite-gouvernance.md"
CH05 = "Livre I/05-ancrage-informationnel.md"
CH09 = "Livre I/09-decouverte-registres-pile.md"
CH11 = "Livre I/11-modes-echec-risques-protocolaires.md"
CH26 = "Livre III/26-vide-federal-c27-c36.md"
CH28 = "Livre III/28-valeurs-mobilieres-acvm-11-348.md"
CH42 = "Livre IV/42-matrice-protocoles-exigences.md"
CH46 = "Livre IV/46-instrumentation-feuille-route.md"
REGISTRE = "PRD/registre-gel.md"

# --------------------------------------------------------------------------
# La ligne de base : les cinq défauts réels du corpus au 28 juillet 2026.
# Chacun a été INSTRUIT avant d'être épinglé — corps ouvert, occurrences
# comptées à la main — et aucun n'est un faux positif :
#
#   ch. 32  « R-14 : deux occurrences DU SIGLE » — le corps en porte trois ;
#   ch. 39  « R-02 : zéro occurrence DE L'IDENTIFIANT » — le corps en porte un ;
#   ch. 44  « R-14 : zéro occurrence DE L'IDENTIFIANT » — le corps en porte un ;
#   ch. 48  « R-02 » déclaré à trois, puis repris dans la plage « R-01 à R-08 :
#           zéro occurrence » — l'en-tête se contredit lui-même ;
#   ch. 49  « R-8 : zéro occurrence » — le corps écrit « garde-fou R-8 du Vol. II ».
#
# ⚠ Les trois premiers sont d'autant plus instructifs que leur déclaration NOMME
# le marqueur qu'elle compte (« du sigle », « de l'identifiant ») : *ce sont les
# en-têtes les plus rigoureux du corpus qui sont pris en défaut, parce qu'ils
# sont les seuls dont le cardinal soit opposable.*
# --------------------------------------------------------------------------
LIGNE_DE_BASE = 0


def executer(racine):
    """(code, sortie) de check-compendium.py sur la racine donnée."""
    r = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env={**dict(os.environ), "COMPENDIUM_RACINE": str(racine)},
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def echecs(sortie):
    """Les lignes d'échec, sans les rapports déclaratifs."""
    lignes, dedans = [], False
    for ligne in sortie.splitlines():
        if ligne.startswith("ÉCHEC —"):
            dedans = True
            continue
        if dedans and ligne.strip():
            lignes.append(ligne.strip())
    return lignes


def compte_rapport(sortie, etiquette):
    """Le cardinal annoncé par un rapport déclaratif, ou -1 s'il est absent."""
    m = re.search(re.escape(etiquette) + r"\]\s*(\d+)", sortie)
    return int(m.group(1)) if m else -1


def copier():
    """Copie jetable du corpus.

    ⚠ `PRD/` en fait partie, et ce n'est pas accessoire : le contrôle y lit le
    socle consolidé (P4) et le registre de gel (P6). Une copie sans `PRD/` ferait
    échouer ces deux contrôles pour absence de fichier, et toutes les mutations
    « passeraient » pour la mauvaise raison.
    """
    tmp = Path(tempfile.mkdtemp(prefix="compendium-mut-"))
    for piece in RACINE.glob("Livre */*.md"):
        cible = tmp / piece.parent.name / piece.name
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(piece, cible)
    (tmp / "PRD").mkdir(exist_ok=True)
    # ⚠ Le TOC entre à la copie depuis l'ajout de P8 : le seuil de J-IV-2 se
    # mesure sur lui, et une copie sans lui rendrait la mutation M8 inopérante.
    for nom in ("socle-consolide.md", "registre-gel.md", "TOC.md"):
        shutil.copy2(RACINE / "PRD" / nom, tmp / "PRD" / nom)
    return tmp


def inserer(chemin, bloc):
    """Insère un bloc DANS le corps de la pièce — jamais après la note de statut.

    `corps()` coupe à la note de statut : un bloc ajouté en fin de fichier ne
    serait pas lu, et la mutation passerait pour non détectée alors qu'elle
    n'aurait pas eu lieu.
    """
    texte = chemin.read_text(encoding="utf-8")
    m = re.search(r"^##\s*§?\s*[\d.]*\s*—?\s*Note de statut", texte, re.M)
    i = m.start() if m else len(texte)
    chemin.write_text(texte[:i] + bloc + texte[i:], encoding="utf-8")


# --- une mutation par classe --------------------------------------------------

def m1_champ_retire(tmp):
    """P1 — une pièce perd le champ « Volumétrie cible » de son en-tête."""
    p = tmp / CH05
    texte = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"^\|\s*\*\*Volumétrie cible\*\*.*\n", "", texte, flags=re.M),
                 encoding="utf-8")


def m2_renvoi_hors_domaine(tmp):
    """P2 — un renvoi interne désigne un chapitre que le plafond de 50 exclut."""
    inserer(tmp / CH09, "\n\nLa suite se lit au ch. 62, qui la reprend en entier.\n")


def m2b_renvoi_a_une_source(tmp):
    """P2, ne-doit-pas-voir — « ch. 62 du Vol. II » désigne une SOURCE.

    ⚠ C'est la moitié du motif qui décide de son utilité : un renvoi marqué d'un
    volume ne se lit pas dans la numérotation du compendium, et le signaler
    pousserait à « corriger » un renvoi exact.
    """
    inserer(tmp / CH09, "\n\nLe ch. 62 du Vol. II traite cette question ailleurs.\n")


def m3_identifiants_nus(tmp):
    """P3 — deux identifiants de socle employés sans leur volume.

    ⚠ P3 est **déclaratif** : cette mutation ne doit pas produire un échec mais
    faire **croître le cardinal rapporté**. Un rapport dont le nombre ne bouge
    pas quand la matière bouge ne mesure rien.
    """
    inserer(tmp / CH42, "\n\nLes entrées F-77 et H-31 corroborent ce point sans le porter.\n")


def m4_identifiant_de_socle_inconnu(tmp):
    """P4 — un `S-nnn` que le socle consolidé n'alloue pas."""
    inserer(tmp / CH46, "\n\nCe constat s'adosse à l'entrée S-999 du socle consolidé.\n")


def m4b_identifiant_source_inconnu(tmp):
    """P4 — un `F-xx` qui ne résout contre aucune des deux tables."""
    inserer(tmp / CH46, "\n\nLe Vol. III F-99 documente le point à sa source.\n")


def m8_toc_identifiant_pendant(tmp):
    """P8 — le TOC cite un identifiant de socle que l'Annexe B ne connaît pas.

    C'est le seuil de **J-IV-2** que cette mutation éprouve : *« 100 % des F-xx
    cités par le TOC résolvent contre l'Annexe B »*. On insère le renvoi dans la
    **zone vivante** du fichier — après le dernier titre de livre, avant les
    journaux —, puisque les rangées d'historique et les journaux sont gelés et
    hors domaine par construction.

    ⚠ L'identifiant doit être RÉELLEMENT inconnu des deux tables : le premier
    jet employait « Vol. II F-77 », qui existe au socle du Vol. III — *la
    mutation ne mutait rien, et le harnais l'a dit.* Les séries s'arrêtent à
    `F-48` (Vol. II) et `F-98` (Vol. III) : `F-99` est hors des deux.
    """
    p = tmp / "PRD" / "TOC.md"
    texte = p.read_text(encoding="utf-8")
    ancre = "## Annexes"
    assert ancre in texte, "ancre de mutation introuvable dans le TOC"
    p.write_text(texte.replace(
        ancre, "Renvoi de contrôle : le Vol. III F-99 fonde ce point.\n\n" + ancre, 1),
        encoding="utf-8")


def m8b_exclusion_declaree(tmp):
    """P8 — une exclusion DÉCLARÉE résout, et ne doit produire aucun échec.

    ⚠ C'est le *ne-doit-pas-voir* qui protège la décision de lecture de P8 :
    `F-92` est **connue et non versée** (dette de vote). Un contrôle qui la
    compterait pendante **punirait la déclaration de l'exclusion** — et
    enseignerait à ne pas la déclarer, ce qui est l'inverse de ce que
    l'Annexe B doit produire.
    """
    p = tmp / "PRD" / "TOC.md"
    texte = p.read_text(encoding="utf-8")
    ancre = "## Annexes"
    p.write_text(texte.replace(
        ancre, "Renvoi de contrôle : le Vol. III F-92 porte sa dette de vote.\n\n" + ancre, 1),
        encoding="utf-8")


def m5_cardinal_fausse(tmp):
    """P5 — un cardinal d'en-tête qui ne se re-mesure plus au corps.

    Le ch. 3 déclare « R-11 … : une occurrence », et son corps en porte une.
    Passer la déclaration à zéro la rend **ancrée** — donc opposable — et fausse.
    """
    p = tmp / CH03
    texte = p.read_text(encoding="utf-8")
    neuf = texte.replace("**R-11 (jalons NIST « visés », jamais « fixés ») : une occurrence**",
                         "**R-11 (jalons NIST « visés », jamais « fixés ») : zéro occurrence**")
    assert neuf != texte, "la déclaration R-11 du ch. 3 a changé de forme"
    p.write_text(neuf, encoding="utf-8")


def m6_registre_desaligne(tmp):
    """P6 — la volumétrie du registre ne concorde plus avec l'en-tête de la pièce."""
    p = tmp / REGISTRE
    texte = p.read_text(encoding="utf-8")
    neuf = texte.replace("| 11 000 | 10 724 |", "| 11 000 | 12 000 |")
    assert neuf != texte, "la ligne du ch. 1 a changé de forme au registre"
    p.write_text(neuf, encoding="utf-8")


def m6b_ligne_manquante(tmp):
    """P6 — une pièce n'a plus de ligne au registre de gel."""
    p = tmp / REGISTRE
    texte = p.read_text(encoding="utf-8")
    neuf = re.sub(r"^\| 28 \|.*\n", "", texte, flags=re.M)
    assert neuf != texte, "la ligne 28 du registre a changé de forme"
    p.write_text(neuf, encoding="utf-8")


def m6c_date_de_gel_divergente(tmp):
    """P6 — la date de gel du registre ne concorde plus avec l'en-tête."""
    p = tmp / REGISTRE
    texte = p.read_text(encoding="utf-8")
    lignes = texte.splitlines(keepends=True)
    for i, l in enumerate(lignes):
        if l.startswith("| 26 |"):
            lignes[i] = l.replace("27 juillet 2026", "22 juillet 2026")
            break
    else:
        raise AssertionError("ligne 26 introuvable au registre")
    p.write_text("".join(lignes), encoding="utf-8")


def m7_formulation_proscrite(tmp):
    """P7 — la forme « exigé par E-23 », que le PRD §8 proscrit."""
    inserer(tmp / CH26, "\n\nLa tenue d'un inventaire est exigée par E-23 depuis l'origine.\n")


def m7b_quatre_reports(tmp):
    """P7 — « quatre reports », que R-4 du Vol. II proscrit."""
    inserer(tmp / CH28, "\n\nLe rail temps réel a connu quatre reports successifs.\n")


def m7c_jalon_fixe(tmp):
    """P7 — un jalon du NIST dit « fixé », que R-11 du Vol. III proscrit."""
    inserer(tmp / CH11, "\n\nLes jalons de dépréciation sont fixés à 2030 et à 2035.\n")


def m7d_mcp_securise(tmp):
    """P7 — MCP dit « sécurisé », que la réserve F-01 proscrit."""
    inserer(tmp / CH01, "\n\nMCP porte un cadre d'autorisation sécurisé fondé sur OAuth.\n")


def m7e_mention_metalinguistique(tmp):
    """P7, ne-doit-pas-voir — la pièce CITE la forme proscrite pour la proscrire.

    ⚠ **C'est la moitié décisive du motif.** Le corpus énonce ses formulations
    imposées en nommant la forme fautive, tantôt entre guillemets, tantôt en
    emphase markdown — et **quatre pièces sur cinquante** étaient dans ce cas au
    premier passage. Un motif qui les signalerait ferait échouer les pièces les
    plus rigoureuses du corpus : *un contrôle bruyant est un contrôle ignoré.*
    Les deux formes réellement employées sont éprouvées ensemble.
    """
    inserer(tmp / CH26,
            "\n\nOn écrit « attendu par E-23 », jamais « exigé par E-23 ». "
            "Et les jalons sont **visés**, jamais fixés — ce sont *quatre cibles "
            "successives*, non quatre reports. MCP porte un **cadre** "
            "d'autorisation, jamais dit *sécurisé*.\n")


# nom, mutation, attendu, genre :
#   « echec »   — l'étiquette doit apparaître dans un échec NEUF ;
#   « rapport » — le cardinal du rapport déclaratif doit CROÎTRE ;
#   « muet »    — la mutation ne doit produire AUCUN échec neuf.
MUTATIONS = [
    ("M8  P8 — le TOC cite un identifiant que l'Annexe B ne connaît pas",
     m8_toc_identifiant_pendant, "[P8]", "echec"),
    ("M8b P8 — une exclusion déclarée résout (F-92)", m8b_exclusion_declaree, "[P8]", "muet"),
    ("M1  P1 — champ d'en-tête retiré", m1_champ_retire, "[P1]", "echec"),
    ("M2  P2 — renvoi « ch. 62 » hors du domaine 1-50", m2_renvoi_hors_domaine, "[P2]", "echec"),
    ("M2b P2 — « ch. 62 du Vol. II » désigne une source", m2b_renvoi_a_une_source, "[P2]", "muet"),
    ("M3  P3 — identifiants de socle nus (rapport)", m3_identifiants_nus, "[P3", "rapport"),
    ("M4  P4 — « S-999 » non alloué par le socle", m4_identifiant_de_socle_inconnu, "[P4]", "echec"),
    ("M4b P4 — « F-99 » hors des deux tables", m4b_identifiant_source_inconnu, "[P4]", "echec"),
    ("M5  P5 — cardinal d'en-tête faussé", m5_cardinal_fausse, "[P5]", "echec"),
    ("M6  P6 — volumétrie du registre désalignée", m6_registre_desaligne, "[P6]", "echec"),
    ("M6b P6 — pièce sans ligne au registre", m6b_ligne_manquante, "[P6]", "echec"),
    ("M6c P6 — date de gel divergente", m6c_date_de_gel_divergente, "[P6]", "echec"),
    ("M7  P7 — « exigé par E-23 »", m7_formulation_proscrite, "[P7]", "echec"),
    ("M7b P7 — « quatre reports »", m7b_quatre_reports, "[P7]", "echec"),
    ("M7c P7 — jalon NIST « fixé »", m7c_jalon_fixe, "[P7]", "echec"),
    ("M7d P7 — MCP « sécurisé »", m7d_mcp_securise, "[P7]", "echec"),
    ("M7e P7 — mention métalinguistique légitime", m7e_mention_metalinguistique, "[P7]", "muet"),
]


def main():
    print("Temps 1 — que rend le contrôle sur le corpus intact ?")
    code, sortie = executer(RACINE)
    base = echecs(sortie)
    base_p3 = compte_rapport(sortie, "[P3 — DÉCLARATIF")
    if len(base) != LIGNE_DE_BASE:
        print(f"  ☐ {len(base)} échec(s) pour une ligne de base de {LIGNE_DE_BASE}.")
        print("    Le corpus a bougé, ou le script s'est cassé — aucune mutation")
        print("    n'est interprétable tant que l'écart n'est pas instruit.")
        for e in base:
            print(f"    {e}")
        return 1
    print(f"  ☑ ligne de base tenue — {LIGNE_DE_BASE} défauts réels, connus et épinglés ;")
    print(f"    {base_p3} emplois nus rapportés par P3.")

    print("\nTemps 2 — chaque classe de faute est-elle vue ?")
    manques = 0
    for nom, muter, attendu, genre in MUTATIONS:
        tmp = copier()
        try:
            muter(tmp)
            _, sortie = executer(tmp)
            neufs = [e for e in echecs(sortie) if e not in base]
            if genre == "rapport":
                vu = compte_rapport(sortie, attendu + " — DÉCLARATIF") > base_p3
                verdict = "cardinal en hausse" if vu else "cardinal inchangé"
            elif genre == "muet":
                vu = not neufs
                verdict = "aucun échec neuf" if vu else f"échec indu : {neufs[0][:70]}"
            else:
                vu = any(attendu in e for e in neufs)
                verdict = "vue" if vu else ("aucun échec neuf" if not neufs
                                            else f"échec voisin : {neufs[0][:70]}")
            print(f"  {'☑' if vu else '☐'} {nom} — {verdict}")
            manques += 0 if vu else 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if manques:
        print(f"\nÉCHEC — {manques} mutation(s) sur {len(MUTATIONS)} non vue(s).")
        return 1
    print(f"\nOK — ligne de base tenue, et les {len(MUTATIONS)} mutations sont vues.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
