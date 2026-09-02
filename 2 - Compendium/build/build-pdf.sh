#!/usr/bin/env bash
# Compose « Compendium.pdf » — les 50 pieces des cinq Livres, au gabarit Springer.
#   Usage : bash build/build-pdf.sh
# Prerequis : Pandoc >= 3.1.7, Typst >= 0.12, python3, police Times New Roman.
#
# Le compendium n'a PAS de pipeline FESP : les trois copies du FESP appartiennent
# aux Vol. I, II et III. Celui-ci est propre au volume et n'en derive pas.
set -euo pipefail
export PYTHONUTF8=1   # Windows : sinon les sous-processus encodent en cp1252 et plantent sur ⚠.

for _t in pandoc typst python3; do
  command -v "$_t" >/dev/null 2>&1 || { echo "[build] Dependance manquante : $_t" >&2; exit 1; }
done
typst fonts 2>/dev/null | grep -qi "times new roman" || \
  echo "[build] Avertissement : « Times New Roman » introuvable ; repli Liberation / Libertinus Serif." >&2

DIR="$(cd "$(dirname "$0")/.." && pwd)"
# Gabarit et sortie parametrables : la refonte du 31 juillet 2026 se compose a
# cote du rendu courant tant qu'elle n'est pas validee sur mesures.
#   GABARIT=springer OUT_PDF=/tmp/essai.pdf bash build/build-pdf.sh
GABARIT="${GABARIT:-compendium}"
# Le nom canonique porte une majuscule, comme `Compendium.html` : l'index git a ete
# normalise sur le disque le 8 aout 2026. Une minuscule ici produirait un SECOND
# fichier sur un systeme sensible a la casse, au lieu de remplacer le rendu versionne.
OUT="${OUT_PDF:-$DIR/Compendium.pdf}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Les figures sont copiees DANS la racine Typst : `typst compile --root "$TMP"`
# refuse tout chemin qui en sort, et les pieces les referencent en `../figures/`
# depuis leur dossier de Livre — c'est `assemble.py` qui rabat le chemin.
[ -d "$DIR/figures" ] && cp -r "$DIR/figures" "$TMP/"

python3 "$DIR/build/assemble.py" "$TMP/compendium.md"
# `accentuation.lua` porte la regle d'accentuation du corps — le gras de
# proposition rendu au romain, le ⚠ retire, une saillance par sous-section. Elle
# opere sur l'ARBRE et non sur le texte : voir l'en-tete du filtre pour le motif.
pandoc "$TMP/compendium.md" -f markdown-raw_html --template="$DIR/build/$GABARIT.template" \
       --lua-filter="$DIR/build/accentuation.lua" -t typst -o "$TMP/doc.typ"
sed -i 's/align(center)\[#table/align(left)[#table/g' "$TMP/doc.typ"
# Pandoc pose un `table.hline()` explicite sous la rangee de tete. Le gabarit
# dessine deja toutes les frontieres de rangee, et cette ligne explicite se
# superpose a la sienne en 0,5 pt -- ce qui EFFACE le filet de 1 pt que les deux
# modeles Springer portent sous leur rangee de tete. On la retire.
sed -i 's/^\( *\)table\.hline(),$/\1/' "$TMP/doc.typ"
typst compile --root "$TMP" "$TMP/doc.typ" "$OUT"

OUT_NATIVE="$(cygpath -w "$OUT" 2>/dev/null || echo "$OUT")"
PAGES="$(python3 -c "import sys;from pypdf import PdfReader;print(len(PdfReader(sys.argv[1]).pages))" "$OUT_NATIVE" 2>/dev/null || echo '?')"
echo "Rendu : $OUT ($PAGES pages)"

# ---- porte de pagination ----
# ⚠ MILLE PAGES EXACTEMENT est une instruction d'auteur du 9 aout 2026, et le
# chiffre se VERIFIE au build au lieu de se constater : la pagination est une
# fonction en escalier, et un mot ajoute a une piece suffit a la faire changer
# de marche. Sans cette porte, la cible se perdrait au premier commit suivant,
# en silence.
# La porte ne vaut que pour le rendu CANONIQUE : un essai (`OUT_PDF=...`) ou le
# gabarit `springer` compose une maquette qui n'a pas cette cible.
CIBLE=1000
if [ "$GABARIT" = compendium ] && [ "$OUT" = "$DIR/Compendium.pdf" ]; then
  if [ "$PAGES" = '?' ]; then
    # ⚠ ECHEC et non avertissement (2 septembre 2026). La forme anterieure
    # degradait la porte en avertissement quand `pypdf` manquait : le rendu
    # canonique s'ecrivait alors sans que la cible ait ete verifiee, et
    # l'avertissement se perdait dans la sortie du build. *Une porte qui ne
    # s'execute pas doit faire echouer le build, sinon elle enseigne qu'on peut
    # composer sans elle* — c'est la meme doctrine que le `renvoi: None` de
    # `check-sieges.py` : une desactivation se declare, elle ne se subit pas.
    echo "[build] ECHEC : pypdf introuvable, la cible de $CIBLE pages n'a PAS pu etre verifiee." >&2
    echo "[build]   Le PDF est ecrit, sa conformite n'est pas etablie." >&2
    echo "[build]   Installer la dependance : python3 -m pip install -r build/requirements.txt" >&2
    exit 1
  elif [ "$PAGES" -ne "$CIBLE" ]; then
    echo "[build] ECHEC : $PAGES pages rendues, $CIBLE attendues. Le PDF est ecrit, il n'est pas conforme." >&2
    echo "[build]   Le calage se prend sur PAS dans build/compendium.template, et sur lui seul :" >&2
    echo "[build]   17,00 pt donne 1001 pages, 16,95 pt en donne 1000, 16,90 pt en donne 999." >&2
    echo "[build]   Ne pas compenser sur le corps de 13 pt ni sur le bloc de 157,0 mm : ils sont releves." >&2
    exit 1
  fi
fi
