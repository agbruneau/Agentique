#!/usr/bin/env bash
# Compose « Traité.pdf » — le traité sur les systèmes multiagents en essaim.
#   Usage : bash build/build-pdf.sh
#           OUT_PDF=/tmp/essai.pdf bash build/build-pdf.sh   # sans toucher au livré
# Prérequis : Pandoc >= 3.1.7, Typst >= 0.12, police New Computer Modern.
#
# ⚠ Ce script existe parce que la commande n'était écrite NULLE PART au dépôt :
# le README du dossier disait seulement que la chaîne « ne se lance que depuis
# la racine », jamais avec quels arguments, et il fallait la reconstituer.
# Elle est ici, et elle se lance DEPUIS CE DOSSIER : les dix-neuf figures que
# `Traité.md` cite en chemin relatif sont passées de la racine du dépôt à
# `figures/` de ce dossier le 21 août 2026 — `4 - Essais/1 - Traité/figures/`
# depuis la réorganisation du 5 septembre 2026 —, ce qui décloue la chaîne.
#
# Aucun gabarit n'est versionné, et ce n'est pas un manque : tout le réglage —
# géométrie, fontes, redéfinition de `conf`, débord `pad(x: -45pt)` pour les
# figures gravées à 468 pt — vit dans le bloc `header-includes` de la source.
# Graver les figures d'abord si elles ont bougé : `python figures/contenu.py`.
set -euo pipefail
export PYTHONUTF8=1   # Windows : sans quoi les sous-processus encodent en cp1252.

for _t in pandoc typst; do
  command -v "$_t" >/dev/null 2>&1 || { echo "[build] Dépendance manquante : $_t" >&2; exit 1; }
done

DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

SRC="Traité.md"
OUT="${OUT_PDF:-Traité.pdf}"

pages() {
  python3 -c "import sys;from pypdf import PdfReader;print(len(PdfReader(sys.argv[1]).pages))" "$1" 2>/dev/null || echo '?'
}

# ⚠ La pagination est une fonction en escalier : un mot ajouté à la source
# suffit à la faire changer de marche, et le chiffre publié se périme alors en
# silence. On la compare donc avant/après. Ici l'écart AVERTIT sans arrêter —
# aucune instruction d'auteur ne fixe de cible sur ce document, contrairement
# aux mille pages du compendium ; Python/check-traite.py porte le contrôle.
AVANT=''
[ -f "$OUT" ] && AVANT="$(pages "$OUT")"

pandoc "$SRC" --pdf-engine=typst --toc -o "$OUT"

APRES="$(pages "$OUT")"
echo "Rendu : $OUT ($APRES pages)"
if [ -n "$AVANT" ] && [ "$AVANT" != "$APRES" ]; then
  echo "[build] ⚠ pagination : $AVANT -> $APRES pages." >&2
  echo "[build]   Le chiffre est publié au README de ce dossier et à celui de la racine ;" >&2
  echo "[build]   le reporter, ou dire pourquoi il bouge. Mesure : python Python/check-traite.py" >&2
fi
