#!/usr/bin/env bash
# Compose les deux rendus du dossier — « Veille Technologique.pdf » (Vol. VI) et
# « Revue de littérature.pdf » (Vol. VII).
#   Usage : bash build/build-pdf.sh [veille|revue]     # les deux par défaut
#           SUFFIXE=-essai bash build/build-pdf.sh     # sans toucher aux livrés
# Prérequis : Pandoc >= 3.1.7, Typst >= 0.12, police New Computer Modern.
#
# ⚠ Ce script ne fait qu'INSCRIRE au dépôt les deux commandes qui n'y vivaient
# qu'en prose, dans le README du dossier, à recopier à la main. Elles ne
# changent pas d'un signe.
#
# Aucun gabarit n'est versionné, et ce n'est pas un manque : tout le réglage vit
# dans l'en-tête YAML de chaque source, dont un bloc `header-includes` commun
# aux deux qui redéfinit `conf` pour composer lui-même le bloc de titre.
# ☑ Ni l'une ni l'autre source ne porte d'image : aucun chemin relatif à
# résoudre, donc aucune contrainte sur le dossier d'où l'on compose.
set -euo pipefail
export PYTHONUTF8=1   # Windows : sans quoi les sous-processus encodent en cp1252.

for _t in pandoc typst; do
  command -v "$_t" >/dev/null 2>&1 || { echo "[build] Dépendance manquante : $_t" >&2; exit 1; }
done

DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"
SUFFIXE="${SUFFIXE:-}"

pages() {
  python3 -c "import sys;from pypdf import PdfReader;print(len(PdfReader(sys.argv[1]).pages))" "$1" 2>/dev/null || echo '?'
}

# ⚠ La pagination est une fonction en escalier : un mot ajouté à la source
# suffit à la faire changer de marche, et le chiffre publié se périme alors en
# silence. On la compare donc avant/après, en AVERTISSANT sans arrêter — aucune
# instruction d'auteur ne fixe de cible sur ces deux documents.
composer() {
  local src="$1" out avant='' apres
  out="${src%.md}${SUFFIXE}.pdf"
  [ -f "$out" ] && avant="$(pages "$out")"

  pandoc "$src" --pdf-engine=typst --toc -o "$out"

  apres="$(pages "$out")"
  echo "Rendu : $out ($apres pages)"
  if [ -n "$avant" ] && [ "$avant" != "$apres" ]; then
    echo "[build] ⚠ pagination : $avant -> $apres pages pour « $out »." >&2
    echo "[build]   Le chiffre est publié au README de ce dossier et à celui de la racine ;" >&2
    echo "[build]   le reporter, ou dire pourquoi il bouge." >&2
  fi
  # La porte du résumé : le gabarit pose le bloc de titre en flottant NON
  # SÉCABLE, et un résumé trop long se fait rogner sous la marge basse sans que
  # Pandoc ni Typst ne sortent autre chose que 0. Ce contrôle est le seul qui
  # le voie, et il vit déjà dans ce dossier.
  python3 Python/check-resume.py "$out" || {
    echo "[build] ⚠ le résumé de « $out » déborde son bloc — voir Python/check-resume.py." >&2
    return 1
  }
}

case "${1:-tout}" in
  veille) composer "Veille Technologique.md" ;;
  revue)  composer "Revue de littérature.md" ;;
  tout)   composer "Veille Technologique.md"; composer "Revue de littérature.md" ;;
  *)      echo "[build] Argument inconnu : $1 (veille | revue | rien)" >&2; exit 2 ;;
esac
