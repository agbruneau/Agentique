#!/usr/bin/env bash
# Compose « compendium.pdf » — les 50 pieces des cinq Livres, au gabarit Springer.
#   Usage : bash build/build-pdf.sh
# Prerequis : Pandoc >= 3.1.7, Typst >= 0.12, python3, police Palatino Linotype.
#
# Le compendium n'a PAS de pipeline FESP : les trois copies du FESP appartiennent
# aux Vol. I, II et III. Celui-ci est propre au volume et n'en derive pas.
set -euo pipefail
export PYTHONUTF8=1   # Windows : sinon les sous-processus encodent en cp1252 et plantent sur ⚠.

for _t in pandoc typst python3; do
  command -v "$_t" >/dev/null 2>&1 || { echo "[build] Dependance manquante : $_t" >&2; exit 1; }
done
typst fonts 2>/dev/null | grep -qi "palatino linotype" || \
  echo "[build] Avertissement : « Palatino Linotype » introuvable ; repli Book Antiqua / Libertinus." >&2

DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$DIR/compendium.pdf"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python3 "$DIR/build/assemble.py" "$TMP/compendium.md"
pandoc "$TMP/compendium.md" -f markdown-raw_html --template="$DIR/build/springer.template" \
       -t typst -o "$TMP/doc.typ"
sed -i 's/align(center)\[#table/align(left)[#table/g' "$TMP/doc.typ"
# Pandoc donne des colonnes EGALES a toute table de tuyaux : la grille des 159
# entrees de l'annexe y perdait sa colonne « Objet », reduite au septieme de la
# justification. Les trois tables a sept colonnes du document sont ses trois
# bandes ; elles sont les seules, et le motif ne vaut que pour elles.
sed -i 's/columns: (14\.29%, 14\.29%, 14\.29%, 14\.29%, 14\.29%, 14\.29%, 14\.29%)/columns: (10%, 15%, 9%, 10%, 11%, 8%, 37%)/g' "$TMP/doc.typ"
typst compile --root "$TMP" "$TMP/doc.typ" "$OUT"

OUT_NATIVE="$(cygpath -w "$OUT" 2>/dev/null || echo "$OUT")"
echo "Rendu : $OUT ($(python3 -c "import sys;from pypdf import PdfReader;print(len(PdfReader(sys.argv[1]).pages))" "$OUT_NATIVE" 2>/dev/null || echo '?') pages)"
