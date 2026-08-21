#!/usr/bin/env bash
# Compose les deux rendus du dossier — « État de l'art — services financiers.pdf »
# (Vol. VIII, 185 p.) et sa planche « Cinq schémas… .pdf » (7 p.).
#   Usage : bash build/build-pdf.sh [etat|planche]     # les deux par défaut
#           SUFFIXE=-essai bash build/build-pdf.sh     # sans toucher aux livrés
# Prérequis : Pandoc >= 3.1.7, Typst >= 0.12, police New Computer Modern.
#
# ⚠ Ce script ne fait qu'INSCRIRE au dépôt les deux commandes qui n'y vivaient
# qu'en prose, dans le README du dossier, à recopier à la main. Elles ne
# changent pas d'un signe.
#
# ⚠ CE QU'IL NE COUVRE PAS, ET C'EST DÉCLARÉ : les deux rendus `.html`. Leur
# commande prend `--css <feuille>`, et **aucune feuille de style n'est
# versionnée** — celle de la planche ne survit qu'embarquée dans le `.html`
# livré. Le `.html` du document long, lui, a été détruit le 21 août 2026 sur
# décision d'auteur. *Un rendu dont une entrée manque au dépôt ne se rejoue pas ;
# le dire vaut mieux que d'écrire une commande qui échouera.*
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
  python3 "../4 - Veille/Python/check-resume.py" "$out" || {
    echo "[build] ⚠ le résumé de « $out » déborde son bloc." >&2
    return 1
  }
}

case "${1:-tout}" in
  etat)    composer "État de l'art — services financiers.md" ;;
  planche) composer "Cinq schémas — état de l'art en services financiers.md" ;;
  tout)    composer "État de l'art — services financiers.md"
           composer "Cinq schémas — état de l'art en services financiers.md" ;;
  *)       echo "[build] Argument inconnu : $1 (etat | planche | rien)" >&2; exit 2 ;;
esac
