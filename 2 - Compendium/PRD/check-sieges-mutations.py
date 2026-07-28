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

import importlib.util
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
    """Copie jetable du corpus : les pièces seules suffisent au contrôle.

    ⚠ Seuls les `.md` sont copiés. `check-sieges.py` ne lit rien d'autre, et la
    table est passée à vingt-six sièges : recopier les `.html` à chaque mutation
    multipliait la durée du harnais par cinq pour aucun contrôle de plus — *un
    harnais trop lent est un harnais qu'on cesse d'exécuter.*
    """
    tmp = Path(tempfile.mkdtemp(prefix="sieges-mut-"))
    for piece in RACINE.glob("Livre */*.md"):
        cible = tmp / piece.parent.name / piece.name
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(piece, cible)
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


# --- le balayage générique, une mutation par classe et par siège --------------
#
# ⚠ Les onze mutations ci-dessus sont ÉCRITES À LA MAIN, et elles le restent :
# chacune reproduit une faute plausible dans la forme du corpus — une table
# recopiée dans un chapitre voisin, un renvoi remplacé par « plus haut » —, et
# plusieurs consignent une faute réellement commise. Elles ne se remplacent pas.
#
# Ce qu'elles ne font pas, c'est COUVRIR : la table est passée de trois à
# vingt-six sièges, et écrire à la main quatre mutations par siège produirait
# une centaine de fonctions dont la plupart diraient la même chose. Le balayage
# ci-dessous les dérive de la table elle-même, uniformément.
#
# ⚠ Ce que cette dérivation coûte, et il faut le dire : une mutation dérivée de
# la table éprouve que le contrôle LIT bien ce que la table déclare — que le
# marqueur est trouvable, que la signature résout, qu'une copie ailleurs est
# vue, qu'un déclencheur sans renvoi échoue. Elle n'éprouve PAS que la table
# déclare la bonne chose : une signature ancrée sur un terme nu passerait ce
# balayage tout en étant bruyante. *Le jugement sur ce qu'un siège interdit de
# refaire reste au commentaire du siège ; le balayage ne le remplace pas.*

# ⚠ Le dépôt n'a pas de `.gitignore` : importer le contrôle y déposerait un
# `PRD/__pycache__/` non versionné à chaque exécution du harnais. Un outil de
# contrôle ne salit pas l'arbre de travail qu'il contrôle.
sys.dont_write_bytecode = True

_SPEC = importlib.util.spec_from_file_location("check_sieges", SCRIPT)
CS = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(CS)


def _inserer(chemin, bloc):
    """Insère un bloc DANS le corps de la pièce — jamais après la note de statut.

    `corps()` coupe à la note de statut : un bloc ajouté en fin de fichier ne
    serait pas lu, et la mutation passerait pour non détectée alors qu'elle
    n'aurait pas eu lieu.
    """
    texte = chemin.read_text(encoding="utf-8")
    coupe = CS.FIN_DE_CORPS.search(texte)
    i = coupe.start() if coupe else len(texte)
    chemin.write_text(texte[:i] + bloc + texte[i:], encoding="utf-8")


def _lignes_de_signature(tmp, siege):
    """Les lignes du siège qui portent sa signature, prêtes à être recopiées."""
    corps = CS.corps((tmp / siege["fichier"]).read_text(encoding="utf-8"))
    lignes = []
    for motif in siege["signature"]:
        m = re.search(motif, corps, re.M)
        if m is None:
            raise AssertionError(f"signature introuvable dans son siège : {siege['id']}")
        debut = corps.rfind("\n", 0, m.start()) + 1
        fin = corps.find("\n", m.end())
        lignes.append(corps[debut:fin if fin != -1 else len(corps)])
    return lignes


def _texte_declencheur(tmp, siege):
    """Un fragment réel qui résout contre le déclencheur, replié sur une ligne."""
    candidats = [tmp / siege["fichier"]] + sorted(tmp.glob("Livre */[0-9][0-9]-*.md"))
    for p in candidats:
        m = re.search(siege["declencheur"], CS.corps(p.read_text(encoding="utf-8")))
        if m:
            return re.sub(r"\s+", " ", m.group(0))
    raise AssertionError(f"déclencheur introuvable dans tout le corpus : {siege['id']}")


def _cible(tmp, siege, interdits=()):
    """Une pièce de la copie qui n'est pas le siège et ne résout aucun interdit."""
    for p in sorted(tmp.glob("Livre */[0-9][0-9]-*.md")):
        if p == tmp / siege["fichier"]:
            continue
        corps = CS.corps(p.read_text(encoding="utf-8"))
        if any(re.search(m, corps, re.M) for m in interdits if m):
            continue
        return p
    raise AssertionError(f"aucune pièce cible disponible : {siege['id']}")


def _g_s2(siege):
    def muter(tmp):
        p = tmp / siege["fichier"]
        texte = p.read_text(encoding="utf-8")
        neuf = re.sub(siege["marqueur"], "Encadré ordinaire", texte, flags=re.M)
        assert neuf != texte, f"marqueur introuvable : {siege['id']}"
        p.write_text(neuf, encoding="utf-8")
    return muter


def _g_s3(siege):
    def muter(tmp):
        p = tmp / siege["fichier"]
        texte = p.read_text(encoding="utf-8")
        neuf = re.sub(siege["signature"][0], "— forme changée —", texte, flags=re.M)
        assert neuf != texte, f"signature[0] introuvable : {siege['id']}"
        p.write_text(neuf, encoding="utf-8")
    return muter


def _g_s4(siege):
    def muter(tmp):
        bloc = "\n\n" + "\n".join(_lignes_de_signature(tmp, siege)) + "\n"
        _inserer(_cible(tmp, siege), bloc)
    return muter


def _g_s5(siege):
    def muter(tmp):
        fragment = _texte_declencheur(tmp, siege)
        cible = _cible(tmp, siege, interdits=(siege["declencheur"], siege["renvoi"]))
        _inserer(cible, f"\n\nUne pièce avale évoque {fragment} sans renvoyer à son siège.\n")
    return muter


def _balayage():
    """Une mutation par classe et par siège, dérivée de la table.

    S5 n'est dérivé que pour les sièges dont il est ARMÉ : muter un siège à
    `renvoi: None` produirait une mutation qu'aucun contrôle ne peut attraper,
    donc un faux échec du harnais. Les sièges à S5 désactivé restent couverts
    par S2, S3 et S4 — c'est exactement ce que « à moitié contrôlé » veut dire.
    """
    sortie = []
    for siege in CS.SIEGES:
        nom = siege["section"]
        sortie.append((f"G {nom} — S2, marqueur retiré", _g_s2(siege), "[S2]"))
        sortie.append((f"G {nom} — S3, signature périmée", _g_s3(siege), "[S3]"))
        sortie.append((f"G {nom} — S4, signature recopiée ailleurs", _g_s4(siege), "[S4]"))
        if siege["renvoi"] is not None:
            sortie.append((f"G {nom} — S5, matière touchée sans renvoi", _g_s5(siege), "[S5]"))
    return sortie


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
] + _balayage()


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
