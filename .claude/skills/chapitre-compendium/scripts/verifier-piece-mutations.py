#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validation par mutation de `verifier-piece.py`.

    python verifier-piece-mutations.py "2 - Compendium/Livre I/01-interoperabilite-integration-entreprise"

Copie la pièce dans un répertoire temporaire, constate d'abord que le contrôle **passe** sur la
copie intacte, puis introduit une faute à la fois et vérifie que le contrôle **échoue** — et qu'il
échoue sur le bon contrôle, pas par accident.

Les deux constats comptent, et le premier plus que le second : un script cassé « détecte » toutes
les mutations sans rien contrôler du tout. Sortie 0 si le script est sain, 1 sinon.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
VERIFIEUR = os.path.join(ICI, "verifier-piece.py")


def _remplacer_une_fois(texte, motif, remplacement):
    """Remplace la première occurrence d'un motif regex ; lève si le motif est introuvable, pour
    qu'une mutation devenue inapplicable se signale au lieu de passer pour un succès."""
    nouveau, n = re.subn(motif, remplacement, texte, count=1)
    if n == 0:
        raise RuntimeError("mutation inapplicable : motif introuvable — %s" % motif)
    return nouveau


# Chaque mutation : (identifiant, contrôle attendu, cible, fonction de transformation).
MUTATIONS = [
    ("M1a", "[1]", "html", None),  # suppression pure du .html, traitée à part
    ("M1b", "[1]", "html",
     lambda s: _remplacer_une_fois(s, r'<a href="[^"]*\.md">Version Markdown</a>',
                                   '<a href="ailleurs.txt">Version Markdown</a>')),
    ("M2a", "[2]", "html",
     lambda s: _remplacer_une_fois(s, r"</section>", "")),
    ("M2b", "[2]", "html",
     lambda s: _remplacer_une_fois(s, r'<h2 id="s11">', '<h2 id="s11-renomme">')),
    ("M3a", "[3]", "html",
     lambda s: _remplacer_une_fois(
         s, r"<style>", '<link rel="stylesheet" href="https://exemple.invalid/a.css">\n<style>')),
    ("M3b", "[3]", "html",
     lambda s: _remplacer_une_fois(
         s, r"<style>", '<link rel="canonical" href="https://exemple.invalid/">\n<style>')),
    ("M4a", "[4]", "html",
     lambda s: _remplacer_une_fois(s, r'<html lang="fr-CA">', "<html lang=\"fr\">")),
    ("M4b", "[4]", "html",
     lambda s: _remplacer_une_fois(s, r"\n  hyphens: auto;", "")),
    ("M5", "[5]", "html",
     lambda s: _remplacer_une_fois(s, r'<p class="legende">', "<p>")),
    ("M6a", "[6]", "md",
     lambda s: _remplacer_une_fois(s, r"\*\*Volumétrie cible\*\*", "**Longueur**")),
    ("M6b", "[6]", "html",
     lambda s: _remplacer_une_fois(s, r"<dt>Garde-fous balayés</dt>", "<dt>Garde-fous</dt>")),
    ("M7", "[7]", "md",
     lambda s: _remplacer_une_fois(s, r"\]\(\.\./PRD/TOC\.md\)", "](../PRD/ABSENT.md)")),
]


def _executer(base):
    r = subprocess.run([sys.executable, VERIFIEUR, base], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main(argv):
    if len(argv) != 2:
        print("usage: verifier-piece-mutations.py <chemin de la pièce, sans extension>")
        return 2
    source = argv[1]
    for suffixe in (".md", ".html"):
        if source.endswith(suffixe):
            source = source[: -len(suffixe)]

    if not (os.path.isfile(source + ".md") and os.path.isfile(source + ".html")):
        print("pièce introuvable : %s.{md,html}" % source)
        return 2

    original = {
        "md": open(source + ".md", encoding="utf-8").read(),
        "html": open(source + ".html", encoding="utf-8").read(),
    }
    nom = os.path.basename(source)
    dossier_source = os.path.dirname(os.path.abspath(source))

    echecs = []
    with tempfile.TemporaryDirectory() as tmp:
        # La pièce renvoie vers ../PRD/… : reconstituer l'arborescence pour que le contrôle [7]
        # soit significatif plutôt que faussement en échec.
        travail = os.path.join(tmp, "Livre")
        os.makedirs(travail)
        parent_reel = os.path.dirname(dossier_source)
        for voisin in ("PRD", "CLAUDE.md", "README.md"):
            src = os.path.join(parent_reel, voisin)
            dst = os.path.join(tmp, voisin)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            elif os.path.isfile(src):
                shutil.copy2(src, dst)
        # Le README du dossier de la pièce est cité par le .md ; le recopier aussi.
        for fichier in os.listdir(dossier_source):
            if fichier.endswith(".md") and fichier.startswith("README"):
                shutil.copy2(os.path.join(dossier_source, fichier), travail)

        base = os.path.join(travail, nom)

        def ecrire(contenu):
            for ext in ("md", "html"):
                with open("%s.%s" % (base, ext), "w", encoding="utf-8") as f:
                    f.write(contenu[ext])

        # --- constat préalable : le contrôle passe sur la copie intacte -------------
        ecrire(original)
        code, sortie = _executer(base)
        if code != 0:
            print("Constat préalable ÉCHOUÉ — le contrôle ne passe pas sur la pièce intacte.")
            print("Sans ce constat, toute mutation « détectée » ne prouve rien.\n")
            print(sortie)
            return 1
        print("Constat préalable : le contrôle passe sur la pièce intacte -> OK\n")

        # --- mutations ---------------------------------------------------------------
        for ident, attendu, cible, transformer in MUTATIONS:
            contenu = dict(original)
            if transformer is None:
                ecrire(contenu)
                os.remove(base + ".html")  # M1a : rendu manquant
            else:
                try:
                    contenu[cible] = transformer(contenu[cible])
                except RuntimeError as e:
                    echecs.append("%s : %s" % (ident, e))
                    continue
                ecrire(contenu)

            code, sortie = _executer(base)
            if code == 0:
                echecs.append("%s : mutation NON détectée (le contrôle passe quand même)" % ident)
            elif attendu not in sortie:
                echecs.append("%s : détectée, mais pas par le contrôle %s — sortie : %s"
                              % (ident, attendu, sortie.strip().splitlines()[1:2]))
            else:
                print("  %-4s %s détectée par %s" % (ident, cible.ljust(4), attendu))

    print()
    if echecs:
        for e in echecs:
            print("  ÉCHEC %s" % e)
        print("\n%d mutation(s) non détectée(s) : le contrôle n'est pas validé." % len(echecs))
        return 1
    print("%d mutations, toutes détectées par le contrôle attendu." % len(MUTATIONS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
