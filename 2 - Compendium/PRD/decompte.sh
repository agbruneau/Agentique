#!/bin/sh
# Commande de décompte de référence du compendium (Vol. IV) — porte G-2.
#
# Héritée du PRDPlan du Vol. III §1.5 : le tokéniseur est repris tel quel,
# `LC_ALL=C.UTF-8` compris, qui n'est PAS décoratif (en locale `C`, [[:alnum:]]
# ne reconnaît aucun caractère accentué et sous-compte d'environ 1,3 %).
#
# Ce que ce script ajoute au tokéniseur hérité : la DÉLIMITATION DU CORPS,
# qui diffère d'un corpus à l'autre et que la commande du Vol. III ne pouvait
# pas connaître, ayant été écrite pour ses propres pièces.
#
#   Vol. I   — pas d'en-tête tabulaire, pas de section « Notes » : corps entier.
#   Vol. II  — pièces au gabarit du Vol. III : du premier « --- » à « ## Notes ».
#   Vol. III — idem.
#   Vol. IV  — en-tête à cinq champs puis thèse citée ; le corps court du premier
#              « --- » jusqu'à la « Note de statut » hors plan, exclue parce
#              qu'elle se retire à la publication (PRD §6, skill §7).
#
# ⚠ Éprouvé sur les TROIS CORPUS ENTIERS le 27 juillet 2026, jamais sur un
# échantillon — c'est la faute que le Vol. II a payée (commande publiée après
# essai sur deux fichiers pour vingt-neuf, et fausse). Les chiffres attendus
# sont ceux du bloc `--verifier` ci-dessous ; ils reproduisent à l'unité près
# les chiffres publiés par les volumes qui en avaient.
#
# Usage :
#   ./decompte.sh --verifier            # rejoue la validation des trois corpus
#   ./decompte.sh --registre            # oppose le registre de gel à la mesure
#   ./decompte.sh <fichier.md> ...      # décompte des fichiers donnés (Vol. IV)

set -eu

RACINE=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)

# Le tokéniseur hérité, seul et unique. Un mot = un jeton portant au moins une
# lettre ou un chiffre, accents compris.
jetons() {
	tr -s '[:space:]' '\n' | LC_ALL=C.UTF-8 grep -cE '[[:alnum:]]' || true
}

# ⚠ LE `\r` OPTIONNEL DES DEUX MOTIFS N'EST PAS UNE PRÉCAUTION, C'EST UN DÉFAUT
# MESURÉ LE 2 SEPTEMBRE 2026 — et il touchait l'autorité de décompte du volume.
#
# Le `.gitattributes` de la racine impose `eol=lf` et nomme la conséquence d'un
# CRLF : « les sept *.sh du dépôt cessent de se lancer ». La conséquence SECONDE
# n'y était pas écrite, et elle est pire, parce qu'elle est SILENCIEUSE : sur un
# arbre de travail rendu en CRLF — l'état de la machine d'auteur, `core.autocrlf`
# valant `true` —, la ligne de séparation se lit « ---\r » et `/^---$/` ne
# l'apparie plus. Le drapeau `f` ne se lève jamais, `awk` n'émet rien, et le
# script rapporte **0 mot** pour la pièce, SANS ERREUR ET SANS CODE DE RETOUR.
#
# *Une autorité de décompte qui rend zéro sans le dire est pire qu'une autorité
# absente : la seconde arrête la passe, la première la laisse publier un total
# faux.* Le motif tolère donc le `\r`, et la vérification ci-dessous refuse le
# zéro plutôt que de le rapporter.

# Corps d'une pièce au gabarit Vol. II / Vol. III.
corps_monographie() {
	awk '/^---\r?$/{f=1;next} /^## Notes\r?/{exit} /^<!--/{exit} f' "$1"
}

# Corps d'une pièce du compendium : la note de statut hors plan est exclue.
corps_compendium() {
	awk '/^---\r?$/{f=1;next} /Note de statut/{exit} f' "$1"
}

verifier() {
	ecarts=0

	vol1=$(jetons < "$RACINE/1 - Collection/1 - InteroperabiliteAgentique/Monographie.md")
	brut1=$(wc -w < "$RACINE/1 - Collection/1 - InteroperabiliteAgentique/Monographie.md" | tr -d ' ')

	vol2=$(find "$RACINE/1 - Collection/2 - OrchestrationAgentique/monographie" -name '*.md' \
		! -name 'README.md' ! -name '99-registre-gel.md' | sort |
		while IFS= read -r f; do corps_monographie "$f"; done | jetons)

	vol3=$(find "$RACINE/1 - Collection/3 - EntrepriseAgentique/monographie" -name '*.md' \
		! -name 'README.md' ! -name '99-registre-gel.md' | sort |
		while IFS= read -r f; do corps_monographie "$f"; done | jetons)

	# Attendus constatés le 27 juillet 2026. Chacun est un point d'ancrage :
	# s'il bouge, c'est le corpus qui a bougé, et le chiffre publié qui se redate.
	#
	# ⚠ Vol. II REDATÉ le 21 août 2026 : 93 242 → 93 239. Le corpus a bougé, et
	# le script avait raison de le dire. Le commit `659241b` (8 août 2026) a
	# récrit dans trois pièces — § 6.2, § 13.2, glossaire de l'annexe D — les
	# formules qui appelaient l'autonomie encadrée le *titre* de l'ouvrage pour
	# en faire sa *thèse* : trois jetons sont tombés du corps. La correction est
	# éditoriale et juste ; c'est l'ancre qui était périmée, non la prose. Le
	# chiffre d'avant renommage reste lisible à `377f8ca`.
	controle "Vol. I  — Monographie.md, commande de référence" "$vol1" 225258 || ecarts=1
	controle "Vol. I  — Monographie.md, wc -w brut (chiffre publié)" "$brut1" 233257 || ecarts=1
	controle "Vol. II — 29 pièces, commande de référence" "$vol2" 93239 || ecarts=1
	controle "Vol. III— 34 pièces, commande de référence" "$vol3" 160890 || ecarts=1

	total=$((vol1 + vol2 + vol3))
	echo ""
	echo "Agrégat des trois corpus par une commande unique : $total mots."
	echo "⚠ Cet agrégat n'est PAS la volumétrie du compendium : il mesure la"
	echo "  matière source avant déduplication, non le livrable."

	if [ "$ecarts" -eq 0 ]; then
		echo ""
		echo "OK — les quatre points d'ancrage sont tenus."
		return 0
	fi
	echo ""
	echo "ÉCART — un corpus a bougé, ou la délimitation a été modifiée."
	return 1
}

# Confrontation du registre de gel À LA MESURE ELLE-MÊME.
#
# ⚠ Ajouté le 2 septembre 2026, et le motif est une lacune de contrôle, non un
# confort. Le contrôle P6 de `check-compendium.py` oppose le `Réel` du registre
# au `Réel` de l'en-tête de la pièce — DEUX COPIES DU MÊME CHIFFRE. Il passe
# donc tant que les deux dérivent ENSEMBLE, et c'est ce qui s'est produit : les
# vingt-six en-têtes qui publient leur mesure étaient périmés de +1 à +772 mots
# le 2 septembre 2026, P6 vert du premier au dernier jour.
#
# Le contrôle manquant ne pouvait pas vivre dans `check-compendium.py` : y
# porter un tokéniseur créerait une SECONDE AUTORITÉ de décompte, c'est-à-dire
# une divergence qui attend. Il vit donc ici, dans l'autorité elle-même, qui
# se confronte à ce que le dépôt déclare d'elle.
#
# Usage : ./decompte.sh --registre
registre() {
	reg="$RACINE/2 - Compendium/PRD/registre-gel.md"
	if [ ! -f "$reg" ]; then
		echo "ÉCART — registre-gel.md introuvable."
		return 1
	fi
	ecarts=0
	vus=0
	# Chaque rangée numérotée du registre : on en tire le fichier et la colonne
	# `Réel`, on mesure le fichier, on oppose. L'espace de milliers est retiré.
	while IFS='|' read -r _ _ _ fichier _ _ _ reel _; do
		chemin=$(printf '%s' "$fichier" | sed -n 's/.*(\.\.\/\([^)]*\)).*/\1/p' |
			sed 's/%20/ /g')
		[ -n "$chemin" ] || continue
		piece="$RACINE/2 - Compendium/$chemin"
		if [ ! -f "$piece" ]; then
			printf '  ☐ %-52s FICHIER INTROUVABLE\n' "$chemin"
			ecarts=1
			continue
		fi
		declare=$(printf '%s' "$reel" | tr -cd '0-9')
		mesure=$(corps_compendium "$piece" | jetons)
		vus=$((vus + 1))
		if [ "$declare" -ne "$mesure" ]; then
			printf '  ☐ %-52s %8d  (registre : %d)\n' \
				"$(basename "$chemin")" "$mesure" "$declare"
			ecarts=$((ecarts + 1))
		fi
	done <<EOF
$(grep -E '^\| [0-9]+ \|' "$reg")
EOF

	echo ""
	if [ "$vus" -ne 50 ]; then
		echo "ÉCART — $vus rangées lues, cinquante attendues."
		return 1
	fi
	if [ "$ecarts" -eq 0 ]; then
		echo "OK — les cinquante lignes du registre tiennent contre la mesure."
		return 0
	fi
	echo "ÉCART — $ecarts ligne(s) du registre ne reproduisent plus la mesure."
	echo "  Un corps a bougé sans que le registre suive, ou l'inverse. La passe"
	echo "  due re-mesure les cinquante en-têtes ET le registre au même commit."
	return 1
}

controle() {
	if [ "$2" -eq "$3" ]; then
		printf '  ☑ %-52s %8d\n' "$1" "$2"
		return 0
	fi
	printf '  ☐ %-52s %8d  (attendu %d)\n' "$1" "$2" "$3"
	return 1
}

if [ "$#" -eq 0 ]; then
	sed -n '2,25p' "$0" | sed 's/^# \{0,1\}//'
	exit 2
fi

if [ "$1" = "--verifier" ]; then
	verifier
	exit $?
fi

if [ "$1" = "--registre" ]; then
	registre
	exit $?
fi

ecarts=0
for f in "$@"; do
	n="$(corps_compendium "$f" | jetons)"
	# ⚠ Le zéro se refuse, il ne se rapporte pas. Une pièce du compendium fait
	# des milliers de mots ; zéro ne signifie jamais « pièce vide », il signifie
	# « la délimitation du corps a échoué » — séparateur introuvable, fichier
	# absent, ou fin de ligne que le motif n'apparie pas. *Rapporter ce zéro
	# comme une mesure, c'est laisser une passe publier un total faux.*
	if [ "$n" -eq 0 ]; then
		printf '  ECART  %s : corps vide — la delimitation a echoue, ce n est pas une mesure.\n' "$f" >&2
		ecarts=1
		continue
	fi
	printf '%8d  %s\n' "$n" "$f"
done
exit "$ecarts"
