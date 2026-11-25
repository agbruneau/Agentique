# Charte éditoriale, narrative et typographique — Tome 7 (v1.3)

Cette charte gouverne tous les agents rédacteurs, réviseurs et lisseurs. Son objectif est d'obtenir un **ouvrage de librairie et de direction fluide, rigoureux et mémorable**, à l'opposé d'un rapport compilatoire ou d'une matrice d'exigences.

---

## 1. Posture et voix d'écriture

1. **Registre** : essai analytique et architectural en **français canadien** soutenu et limpide, directement lisible au Québec, au Canada francophone et en Europe francophone.
2. **Ton** : posé, factuel, incisif et sobre. L'ouvrage défend une thèse claire (la primauté du contrôle déterministe et de la preuve sur la puissance brute des modèles), mais **distingue toujours explicitement** :
   - ce qu'une étude empirique a *mesuré* (en nommant son devis, son statut — article évalué par les pairs ou prépublication — et sa limite);
   - ce qu'une loi ou un régulateur *impose* (en nommant la juridiction et l'échéance);
   - ce qui relève d'une *déduction architecturale*, d'une *heuristique de la collection* (p. ex. la partition 80/20) ou d'une *recommandation de prudence*.
3. **Constats d'absence datés** : toute affirmation négative (« aucune étude ne mesure… », « aucun standard n'existe… ») est rattachée à la date de gel des faits arrêtée au **2 décembre 2026** (`2026-12-02`) et à l'étendue de la recherche qui la fonde.
4. **Échéances postérieures au gel** : les dates de 2027 et au-delà sont écrites comme des échéances à venir (« entrera en vigueur le 1er mai 2027 »), en distinguant une date adoptée d'un jalon seulement annoncé; jamais au passé ni comme un acquis observé.
5. **Scénarios illustratifs (`AO-07`)** : une mise en situation non documentée est introduite comme telle (« Imaginons… », « Scénario illustratif : … »), ne contient aucun chiffre présenté comme mesuré et ne sert jamais de prémisse à une conclusion.
6. **Barre stylistique de référence (pour la boucle `gauntlet-loop`)** : extraits en français, exempts de codes internes, tirés des passages suivants (déclarés dans `manifest.json`) :
   - `3 - Compendium 2027/00 - Ouverture …` — sections `0.1` et `0.2` (récit d'ouverture et enjeux, phrases courtes à moyennes, refus des superlatifs commerciaux);
   - `3 - Compendium 2027/…/Chapitre 48 - Revue de littérature.md` — sections `48.4` et `48.8` (honnêteté épistémique, distinction mesuré / débattu / absent).
   L'essai du DeepMind Institute (copie locale non versionnée dans `sources-locales/`) reste une **source d'inspiration** pour la progression argumentative, mais n'entre pas dans la comparaison à l'aveugle : rédigé en anglais, il serait immédiatement identifiable par le critique.

---

## 2. Architecture interne obligatoire des unités narratives

### 2.1 Unité `00 — Liminaire` (ouverture architecturale de l'ouvrage, `4 200 mots`)

L'unité `00 — Liminaire` ne se limite pas à un avant-propos éditorial : elle pose d'entrée de jeu le **cadre unificateur de l'interopérabilité et de l'orchestration** comme tissu conjonctif de l'entreprise agentique. Elle s'articule en sept éléments obligatoires :

1. **Exergue et ouverture narrative par le réel (`350 à 550 mots`)** : `*Question directrice :*` suivie d'un récit concret — documenté ou explicitement présenté comme scénario illustratif — montrant comment le retrait de l'humain « seul point d'intégration » entre des agents `SaaS` et internes isolés provoque paralysie inter-silos, perte de piste d'audit ou boucle d'appels non bornée.
2. **Six sections analytiques et méthodologiques (`0.1` à `0.6`)** conformes aux intitulés exacts de `toc.md` : rupture d'exécution (`0.1`), les six dimensions de l'interopérabilité et la séparation *qui parle* / *qui en répond* (`0.2`), l'orchestration déterministe comme discipline de retenue (`0.3`), la logique des quatre parties, la règle du maillon le plus élevé et les quatre parcours par mandat (`0.4`), l'hygiène probatoire, la date de gel et le périmètre démontré (`0.5`), puis le colophon d'intégrité 100 % agentique (`0.6`).
3. **Figure inaugurale (`Fig-00`)** commentée dans la prose de `0.2`–`0.3`, synthétisant visuellement les six dimensions d'interopérabilité et le plan d'orchestration déterministe traversés par la confiance et l'économie du résultat.
4. **Tableau synoptique unique (en `0.3`)** contrastant les sept ruptures entre pratiques prototypes héritées (`2024–2025`) et cibles de production d'entreprise (`2027`); le texte précise que ces cibles ne décrivent pas l'état général de la pratique. Aucun autre tableau dans le liminaire (`CA-05`).
5. **Encadré méthodologique (en `0.3`)** intitulé `> **Cinq critères permanents d'évaluation architecturale**` fixant la grille d'analyse appliquée à chaque standard ou patron dans le reste du livre (neutralité de gouvernance, déterminisme des frontières, tolérance aux pannes, coût marginal à l'échelle, coût de sortie).
6. **Ancrage factuel complet** : comme pour les douze chapitres, toute affirmation empirique, normative ou datée du liminaire porte sa référence `[n]` vers `sources/ch00-sources.md` et passe la barrière Wyvern `G2` (`ancrage/ch00-ancrage.md`).
7. **Transition vers la Partie I** : un court paragraphe final, sans encadré « Trois arbitrages », qui conduit le lecteur vers l'industrialisation cognitive.

La règle du maillon le plus élevé (`0.4`) s'énonce en termes de criticité des actions; l'échelle `L0`–`L4` n'est définie qu'au chapitre 01, auquel le liminaire renvoie.

### 2.2 Chapitres `01` à `12` (cinq mouvements par chapitre)

Chaque chapitre (`Ch. 01` à `Ch. 12`) suit cinq mouvements dans un flux continu :

1. **Chapeau et ouverture par le réel (`350 à 550 mots`)** :
   - Une ligne d'exergue sous le titre : `*Question directrice : <question précise du toc.md>*`.
   - Trois à quatre paragraphes narratifs sans sous-titre posant un cas concret, un incident documenté ou un dilemme de direction qui rend palpable l'enjeu du chapitre avant tout concept abstrait.
2. **Quatre sections analytiques numérotées (`X.1` à `X.4`)** :
   - Les titres exacts de `toc.md` sont respectés.
   - Le propos progresse en paragraphes construits (`90 à 180 mots` par paragraphe en moyenne). Les listes à puces ne servent qu'à énumérer des éléments véritablement parallèles (`3 à 5 items` maximum) et représentent **au plus 18 % des lignes du chapitre** (`CA-05`).
3. **Intégration organique des preuves et de la littérature** :
   - Chaque affirmation factuelle, statistique ou réglementaire porte son renvoi bibliographique `[n]` vers la base fermée `sources/chNN-sources.md`.
   - Les auteurs majeurs (Coase, Simon, Leveson, Genewein, Tomašev, Cemri, Debenedetti, Haasnoot, etc.) sont nommés dans la phrase lorsqu'on discute leur idée directrice, plutôt que relégués uniquement derrière un crochet muet (tout auteur primaire bloqué en `statut F` tel que Bainbridge ou Dell'Acqua reste exclu des références probantes).
   - Les citations textuelles sont courtes (au plus `40` mots), placées entre guillemets français `« … »` et suivies de leur renvoi `[n]`.
4. **Figures et tableaux commentés** :
   - Chaque figure assignée au chapitre (`1` ou `2` selon `toc.md`) est annoncée dans le paragraphe qui la précède, suivie de sa légende en italique, puis interprétée en trois à cinq phrases sur ce qu'elle oblige à trancher.
   - Maximum **deux tableaux par chapitre** (`CA-05`), réservés aux comparaisons multidimensionnelles que la prose rendrait confuses.
5. **Clôture décisionnelle (`250 à 400 mots`)** :
   - Un encadré unique intitulé `> **Trois arbitrages sans regret — Chapitre X**` condensant trois décisions actionnables pour la direction et l'architecture.
   - Un court paragraphe final assurant le passage logique vers le chapitre suivant.

---

## 3. Liste noire mécanique (contrôlée automatiquement par `verifie_manuscrit.py`)

Toute apparition dans le liminaire ou les chapitres `01` à `12` des motifs suivants (déclarés dans `forbidden_prose_regexes` de `manifest.json`) déclenche un échec immédiat de la barrière `G1` :

### 3.1 Identifiants matriciels internes hérités des volumes 1 à 6 (`CA-02`)
- Préfixes interdits : `\bCAP-\d{3}\b`, `\bEXIG-[A-Z]+-\d{2}\b`, `\bPOR-\d{3}\b`, `\bANC-\d{3}\b`, `\bINI-\d{3}\b`, `\bPEX-\d{2}\b`, `\bSIG-\d{3}\b`, `\bADR-\d{3}\b`, `\bPRR\b`, `\bDIV-\d{2}\b`.
- Classifications internes non définies pour le lecteur : `\bClasse [1-6]\b`, `\bStade [0-4]\b`, `\bPalier [1-3]\b`.
- Marqueurs bruts d'audit entre crochets : `\[S\]`, `\[D\]`, `\[A\]`, `\[M\]`, `\[N\]`, `\[L\+\]`. *(Le statut des preuves s'exprime en français clair dans la phrase et est codifié uniquement dans l'Annexe C.)*

### 3.2 Formules creuses et tics de génération (`charte` anti-remplissage)
- Expressions bannies : *« Dans un monde en constante évolution »*, *« À l'ère du numérique »*, *« Il convient de souligner que »*, *« Force est de constater que »*, *« En conclusion, nous avons vu que »*, *« changement de paradigme révolutionnaire »*, *« synergie holistique »*.

### 3.3 Défauts relevés par les barrières éditoriales (`G4`, `G5`), non mécanisables
- Titres à deux-points empilés au-delà d'un seul sous-segment explicatif.
- Transitions génériques interchangeables d'un chapitre à l'autre.

---

## 4. Règles linguistiques, mathématiques et typographiques

1. **Terminologie bilingue contrôlée** : employer systématiquement les termes de `registre/glossaire-termes.json`. À la première occurrence majeure d'un concept technique dans un chapitre, donner le terme français suivi de l'équivalent anglais entre parenthèses s'il éclaire l'usage de l'industrie — p. ex. *identité non humaine (`Non-Human Identity`, `NHI`)*, *exécution durable (`Durable Execution`)*, *coût par résultat conforme (`Cost per Compliant Outcome`)*.
2. **Montants monétaires, symboles `$` et formules (`CA-06`)** :
   - Échapper systématiquement chaque symbole dollar littéral en `\$` dans le Markdown (`15,5 G\$ US`, `25 M\$ CA`, `1 000 \$ US`).
   - Toujours préciser la devise (`\$ CA`, `\$ US` ou `€`) et utiliser l'espace insécable ou fine selon le gabarit `Typst`.
   - Écrire toute formule mathématique en `\(...\)` (en ligne) ou `\[...\]` (en display), jamais entre `$`. La compilation `Pandoc` se fait avec `-f markdown-tex_math_dollars+tex_math_single_backslash` : la première option neutralise les `$`, la seconde active les formules en barre oblique inverse, désactivées par défaut dans `Pandoc` (vérifié sur `pandoc 3.14`).
3. **Conventions des figures (`CA-08`)** :
   - Au plus `14` nœuds par diagramme (idéalement `10 à 14`) pour garantir une lisibilité immédiate sur format livre imprimé (`6 × 9 po` ou `Lettre`).
   - Distinction visuelle constante (trait plein épais / teinte sobre) pour la **frontière déterministe possédée** face aux **composants probabilistes substituables** (trait pointillé).
   - Légendes et libellés intégralement en français canadien (hors identifiants de protocoles normalisés comme `MCP`, `A2A`, `SPIFFE`, `OAuth 2.0`, `SHA-256`).
