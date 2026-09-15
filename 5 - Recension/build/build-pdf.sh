#!/usr/bin/env bash
# Compose les rendus du dossier — « État de l'art — services financiers.pdf »
# (Vol. VIII, 185 p. à l'écriture de ce script, 186 depuis le 24 août 2026) et sa
# planche « Cinq schémas… .pdf » (7 p.), puis, sur demande, leurs `.html`.
#   Usage : bash build/build-pdf.sh [etat|planche]     # les deux PDF par défaut
#           bash build/build-pdf.sh html               # le .html de la planche
#           SUFFIXE=-essai bash build/build-pdf.sh [cible]   # sans toucher aux livrés
#           SUFFIXE=-essai bash build/build-pdf.sh html-etat # le .html du document long
# Prérequis : Pandoc >= 3.1.7, Typst >= 0.12, police New Computer Modern.
#
# ⚠ Ce script ne fait qu'INSCRIRE au dépôt les commandes qui n'y vivaient
# qu'en prose, dans le README du dossier, à recopier à la main. Elles ne
# changent pas d'un signe, hormis `--css` et `--eol=lf` sur les `.html`.
#
# ☑ LES `.html` SE REFONT DEPUIS LE DÉPÔT SEUL DEPUIS LE 15 SEPTEMBRE 2026 (tâche
# T6.4 du plan d'exécution). Jusque-là ce script ne les couvrait pas, faute de
# feuille versionnée : elle ne survivait qu'embarquée dans le `.html` livré de
# la planche. Elle en est extraite telle quelle dans `build/recension.css` —
# 4 801 octets, ⚠ SANS SAUT DE LIGNE FINAL : en ajouter un change l'octet du
# `.html` rendu. `--eol=lf` : Pandoc écrit en CRLF sous Windows, et le dépôt
# est en LF (`.gitattributes`).
# ⚠ Le `.html` du document long a été détruit le 21 août 2026 sur décision
# d'auteur : `html-etat` refuse d'écrire sans SUFFIXE, pour ne pas le rétablir
# au dossier en silence.
#
# La planche cite cinq figures en chemin relatif (`figures/*.svg`), gravées par
# `python figures/dessine.py` depuis ce dossier : les composer d'ici, jamais
# d'ailleurs.
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

  pandoc "$src" --pdf-engine=typst -o "$out"

  apres="$(pages "$out")"
  echo "Rendu : $out ($apres pages)"
  if [ -n "$avant" ] && [ "$avant" != "$apres" ]; then
    echo "[build] ⚠ pagination : $avant -> $apres pages pour « $out »." >&2
    echo "[build]   Le chiffre est publié au README de ce dossier et à celui de la racine ;" >&2
    echo "[build]   le reporter, ou dire pourquoi il bouge." >&2
  fi
  # La porte du résumé — le seul contrôle qui voie un résumé rogné sous la
  # marge basse, panne que ni Pandoc ni Typst ne signalent. Il vit chez la
  # veille ; ces deux documents partagent son gabarit de page de titre.
  python3 "../3 - Veille/Python/check-resume.py" "$out" || {
    echo "[build] ⚠ le résumé de « $out » déborde son bloc." >&2
    return 1
  }
}

# Les deux commandes `.html` du README, datées du 20 août 2026 : le document long
# se lit SANS `tex_math_dollars` et porte une table des matières que le PDF n'a pas.
html_etat() {
  [ -n "$SUFFIXE" ] || {
    echo "[build] html-etat : le .html du document long a été détruit le 21 août 2026 sur décision d'auteur ;" >&2
    echo "[build]   SUFFIXE=-essai pour le refaire sans le rétablir au dossier." >&2
    exit 2
  }
  pandoc "État de l'art — services financiers.md" -f markdown-tex_math_dollars \
    --standalone --embed-resources --toc --toc-depth=2 --css build/recension.css --eol=lf \
    -o "État de l'art — services financiers${SUFFIXE}.html"
  echo "Rendu : État de l'art — services financiers${SUFFIXE}.html"
}
html_planche() {
  pandoc "Cinq schémas — état de l'art en services financiers.md" \
    --standalone --embed-resources --css build/recension.css --eol=lf \
    -o "Cinq schémas — état de l'art en services financiers${SUFFIXE}.html"
  echo "Rendu : Cinq schémas — état de l'art en services financiers${SUFFIXE}.html"
}

case "${1:-tout}" in
  etat)      composer "État de l'art — services financiers.md" ;;
  planche)   composer "Cinq schémas — état de l'art en services financiers.md" ;;
  tout)      composer "État de l'art — services financiers.md"
             composer "Cinq schémas — état de l'art en services financiers.md" ;;
  html)      html_planche ;;
  html-etat) html_etat ;;
  *)         echo "[build] Argument inconnu : $1 (etat | planche | html | html-etat | rien)" >&2; exit 2 ;;
esac
