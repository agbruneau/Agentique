#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de mutation de `check-sieges.py`.

Doctrine du dépôt : *un script de contrôle est du contenu, il se vérifie comme le
reste.* La validation se fait en **deux temps, et le premier n'est pas facultatif** :

  1. constater que le contrôle **passe** sur le corpus intact ;
  2. introduire chaque classe de faute et constater qu'il **échoue**.

Sans le premier temps, un script cassé « détecte » tout et se croit bon.

Le corpus réel n'est jamais muté : chaque mutation s'applique à une copie jetable,
que `check-sieges.py` lit via la variable `COMPENDIUM_RACINE`.

Usage :  python check-sieges-mutations.py
Sortie 0 si le contrôle passe intact ET attrape les cinq mutations.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ⚠ La racine du corpus est paramétrable depuis la v0.26, et le motif est un fait
# de terrain : deux passes de rédaction peuvent tourner en parallèle, et le temps 1
# du harnais — « le contrôle passe-t-il sur le corpus intact ? » — n'est
# interprétable que sur le corpus que la passe courante COMMITTE. Sans cette
# variable, un écart introduit par une passe voisine non committée rend tout le
# harnais inutilisable, donc ignoré. Par défaut : le corpus réel.
RACINE = Path(os.environ.get("COMPENDIUM_RACINE", Path(__file__).resolve().parent.parent))
SCRIPT = Path(__file__).resolve().parent / "check-sieges.py"

# La console Windows par défaut est en cp1252 et ne sait pas écrire « ☑ ».
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CH03 = "Livre I/03-securite-identite-gouvernance.md"
CH06 = "Livre I/06-multi-agents-evaluation-surete.md"
CH07 = "Livre I/07-genealogie-gouvernance.md"
CH08 = "Livre I/08-anatomie-mcp-a2a.md"
CH41 = "Livre IV/41-fabrique-agents.md"
CH43 = "Livre IV/43-architecture-reference-couches.md"
CH45 = "Livre IV/45-blueprint-instancie-cycle-de-vie.md"
CH48 = "Livre V/48-semantique-effet-idempotence-compensation.md"
CH49 = "Livre V/49-horizon-frontiere-connaissance-verifiable.md"
CH50 = "Livre V/50-peremption-protocole-revalidation.md"


def executer(racine):
    """Retourne (code, sortie) de check-sieges.py sur la racine donnée."""
    r = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env={**dict(__import__("os").environ), "COMPENDIUM_RACINE": str(racine)},
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def copier():
    """Copie jetable du corpus : les pièces seules suffisent au contrôle."""
    tmp = Path(tempfile.mkdtemp(prefix="sieges-mut-"))
    for livre in RACINE.glob("Livre *"):
        shutil.copytree(livre, tmp / livre.name)
    return tmp


# --- les cinq mutations, une par contrôle -------------------------------------

def m1_marqueur_retire(tmp):
    """S2 — un siège perd son marqueur : plus personne ne sait qu'il en est un."""
    p = tmp / CH07
    p.write_text(p.read_text(encoding="utf-8")
                 .replace("SIÈGE DU GARDE-FOU R-8 POUR TOUTE LA SOMME",
                          "Encadré de désambiguïsation"), encoding="utf-8")


def m2_signature_recopiee(tmp):
    """S4 — une autre pièce reconstruit l'encadré au lieu d'y renvoyer."""
    p = tmp / CH06
    faux = ("\n\n| | Objet | Statut |\n| --- | --- | --- |\n"
            "| **(a)** | l'ACP protocolaire | fusionné |\n"
            "| **(b)** | l'Agentic Control Plane du consortium | annoncé |\n"
            "| **(c)** | l'expression employée par un éditeur | commercial |\n"
            "| **(d)** | la composante ACP de la couche d'infrastructure | non établie |\n"
            "\n: Tableau 6.9 — Les quatre branches.\n")
    texte = p.read_text(encoding="utf-8")
    coupe = texte.index("## § 6.3")
    p.write_text(texte[:coupe] + faux + texte[coupe:], encoding="utf-8")


def m3_renvoi_retire(tmp):
    """S5 — une pièce touche la matière du siège sans plus y renvoyer."""
    p = tmp / CH08
    texte = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"ch\.\s*7\s*§\s*7\.5", "plus haut", texte), encoding="utf-8")


def m4_signature_perimee(tmp):
    """S3 — le siège change de forme : sa signature ne le voit plus, ni une copie."""
    p = tmp / CH07
    texte = p.read_text(encoding="utf-8")
    p.write_text(texte.replace("| **(d)** |", "| **(4)** |"), encoding="utf-8")


def m5_siege_absent(tmp):
    """S1 — la pièce qui porte un siège disparaît du corpus."""
    (tmp / CH03).unlink()


def m6_taxonomie_effet_recopiee(tmp):
    """S4 — le siège de la sémantique d'effet reconstruit dans une autre pièce.

    La faute que le versement du Livre V a pour objet d'empêcher : quatre pièces
    renvoient au ch. 48 « qui en est le siège » ; il suffit qu'une seule refasse
    la table des trois classes pour que l'économie de la fusion tombe.
    """
    p = tmp / CH50
    faux = ("\n\n| Classe d'effet | Ce qu'une reprise produit |\n| --- | --- |\n"
            "| **Lecture** | rien |\n"
            "| **Écriture** | un doublon |\n"
            "| **Engagement** | un second engagement |\n"
            "\n: Tableau 50.2 — Les trois classes d'effet.\n")
    texte = p.read_text(encoding="utf-8")
    coupe = texte.index("## § 50.3")
    p.write_text(texte[:coupe] + faux + texte[coupe:], encoding="utf-8")


def m7_marqueur_tri_retire(tmp):
    """S2 — le siège du tri prospectif perd son marqueur.

    Il était déclaré au plan depuis la v0.16 SANS jamais porter le mot dans une
    pièce, faute de pièce : c'est exactement l'état que ce contrôle interdit de
    reproduire.
    """
    p = tmp / CH49
    p.write_text(p.read_text(encoding="utf-8")
                 .replace("SIÈGE DU TRI PROSPECTIF POUR TOUTE LA SOMME",
                          "Orientation méthodologique"), encoding="utf-8")


def m8_definition_tri_recopiee(tmp):
    """S4 — les trois définitions du tri recopiées dans une autre pièce.

    ⚠ Mutation de la garde `renvoi: None` : elle prouve que désactiver S5 pour un
    siège ne désactive PAS S4. Un siège hors contrôle de reconstruction serait un
    siège non versé.
    """
    p = tmp / CH48
    faux = ("\n\nLe tri se rappelle : **PROGRAMMÉ** désigne un engagement daté réel, "
            "**PROJETÉ** une prévision d'analyste ou d'institution, **SPÉCULATIF** "
            "un pari de recherche ou un scénario.\n")
    texte = p.read_text(encoding="utf-8")
    coupe = texte.index("## § 48.2")
    p.write_text(texte[:coupe] + faux + texte[coupe:], encoding="utf-8")


def m9_table_points_controle_recopiee(tmp):
    """S4 — la table des cinq points de contrôle obligatoires recopiée ailleurs.

    ⚠ Seconde mutation de la garde `renvoi: None` — le siège des points de
    contrôle a S5 désactivé, et cette mutation prouve que S4 reste armé. C'est
    aussi la classe de faute que le ch. 41 a réellement commise au premier
    passage, sur un AUTRE siège : réutiliser la forme d'un siège pour une table
    voisine.
    """
    p = tmp / CH45
    faux = ("\n| # | Point |\n|---|---|\n"
            "| **PC1** | l'événement de décision |\n"
            "| **PC2** | la trace d'instance |\n"
            "| **PC3** | le point d'arrêt humain |\n"
            "| **PC4** | la séparation adaptation / évolution |\n"
            "| **PC5** | le confinement local |\n"
            "\n: Tableau 45.9 — Les cinq points, redits.\n")
    texte = p.read_text(encoding="utf-8")
    coupe = texte.index("## § 45.7")
    p.write_text(texte[:coupe] + faux + texte[coupe:], encoding="utf-8")


def m10_renvoi_organisation_fabrique_retire(tmp):
    """S5 — le ch. 41 cesse de renvoyer au siège de l'organisation de la fabrique.

    C'est le SEUL des trois sièges du Livre IV dont S5 soit armé, et le seul
    endroit du corpus où l'omission de renvoi sur cette matière soit détectable.
    Le § 41.7 doit renvoyer au ch. 45 ; l'en priver doit échouer.
    """
    p = tmp / CH41
    texte = p.read_text(encoding="utf-8")
    p.write_text(texte.replace("ch. 45", "le chapitre voisin"), encoding="utf-8")


def m11_trois_echelles_recopiees(tmp):
    """S4 — la table des trois échelles d'autonomie recopiée ailleurs.

    Troisième garde de `renvoi: None`. Ce que le siège interdit n'est pas le mot
    « maturité » — que sept pièces emploient à bon droit — mais le départage des
    trois échelles homonymes par leur cardinal et leur numérotation.
    """
    p = tmp / CH45
    faux = ("\nRappel des trois échelles : l'**échelle à quatre paliers non "
            "numérotés**, le **continuum à six niveaux numérotés** de 0 à 5, et la "
            "**graduation à quatre niveaux préfixés** L.\n")
    texte = p.read_text(encoding="utf-8")
    coupe = texte.index("## § 45.8")
    p.write_text(texte[:coupe] + faux + texte[coupe:], encoding="utf-8")


MUTATIONS = [
    ("M1  S2 — marqueur de siège retiré", m1_marqueur_retire, "[S2]"),
    ("M2  S4 — signature du siège recopiée ailleurs", m2_signature_recopiee, "[S4]"),
    ("M3  S5 — renvoi au siège retiré", m3_renvoi_retire, "[S5]"),
    ("M4  S3 — signature périmée contre son propre siège", m4_signature_perimee, "[S3]"),
    ("M5  S1 — pièce porteuse du siège absente", m5_siege_absent, "[S1]"),
    ("M6  S4 — taxonomie de la sémantique d'effet recopiée", m6_taxonomie_effet_recopiee, "[S4]"),
    ("M7  S2 — marqueur du siège du tri prospectif retiré", m7_marqueur_tri_retire, "[S2]"),
    ("M8  S4 — définitions du tri recopiées (garde `renvoi: None`)",
     m8_definition_tri_recopiee, "[S4]"),
    ("M9  S4 — table des cinq points de contrôle recopiée (garde `renvoi: None`)",
     m9_table_points_controle_recopiee, "[S4]"),
    ("M10 S5 — renvoi au siège de l'organisation de la fabrique retiré",
     m10_renvoi_organisation_fabrique_retire, "[S5]"),
    ("M11 S4 — table des trois échelles recopiée (garde `renvoi: None`)",
     m11_trois_echelles_recopiees, "[S4]"),
]


def main():
    print("Temps 1 — le contrôle passe-t-il sur le corpus intact ?")
    code, sortie = executer(RACINE)
    if code != 0:
        print("  ☐ NON. Le corpus est en écart ; aucune mutation n'est interprétable.")
        print("    " + sortie.strip().replace("\n", "\n    "))
        return 1
    print(f"  ☑ OUI — {sortie.strip()}")

    print("\nTemps 2 — chaque classe de faute est-elle attrapée ?")
    echecs = 0
    for nom, muter, attendu in MUTATIONS:
        tmp = copier()
        try:
            muter(tmp)
            code, sortie = executer(tmp)
            if code != 0 and attendu in sortie:
                print(f"  ☑ {nom}")
            elif code != 0:
                print(f"  ☐ {nom} — échoue, mais pas sur {attendu} : contrôle voisin déclenché")
                echecs += 1
            else:
                print(f"  ☐ {nom} — NON DÉTECTÉE (sortie 0)")
                echecs += 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if echecs:
        print(f"\nÉCHEC — {echecs} mutation(s) sur {len(MUTATIONS)} non attrapée(s).")
        return 1
    print(f"\nOK — passe intact, et attrape les {len(MUTATIONS)} mutations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
