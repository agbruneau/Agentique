#!/usr/bin/env bash
# Compose « compendium.pdf » — les 50 pieces des cinq Livres, au gabarit Springer.
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
OUT="${OUT_PDF:-$DIR/compendium.pdf}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python3 "$DIR/build/assemble.py" "$TMP/compendium.md"
pandoc "$TMP/compendium.md" -f markdown-raw_html --template="$DIR/build/$GABARIT.template" \
       -t typst -o "$TMP/doc.typ"
sed -i 's/align(center)\[#table/align(left)[#table/g' "$TMP/doc.typ"
# Pandoc pose un `table.hline()` explicite sous la rangee de tete. Le gabarit
# dessine deja toutes les frontieres de rangee, et cette ligne explicite se
# superpose a la sienne en 0,5 pt -- ce qui EFFACE le filet de 1 pt que les deux
# modeles Springer portent sous leur rangee de tete. On la retire.
sed -i 's/^\( *\)table\.hline(),$/\1/' "$TMP/doc.typ"
typst compile --root "$TMP" "$TMP/doc.typ" "$OUT"

OUT_NATIVE="$(cygpath -w "$OUT" 2>/dev/null || echo "$OUT")"
echo "Rendu : $OUT ($(python3 -c "import sys;from pypdf import PdfReader;print(len(PdfReader(sys.argv[1]).pages))" "$OUT_NATIVE" 2>/dev/null || echo '?') pages)"
