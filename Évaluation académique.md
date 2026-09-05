# Évaluation académique du dépôt « Agentique »

**Objet évalué :** le dépôt `agbruneau/Agentique` à l'état du 4 septembre 2026 (commit `69eeee2`, branche `main`, arbre propre).
**Date de l'évaluation :** 5 septembre 2026.
**Cadre :** évaluation d'un corpus de recherche autonome, au niveau attendu d'un dossier de recherche de cycles supérieurs (mémoire de maîtrise étendu ou dossier d'habilitation), en science et génie informatiques. La grille est celle d'un jury : problématique, méthode, sources, contribution, artefacts, structure, rédaction, gouvernance.

**Ce que ce document n'est pas :** une relecture de fond des 3 000 pages. Les huit livrables, les deux documents hors livrables et le code ont été lus par échantillonnage raisonné (en-têtes, chapitres pivots, conclusions, registres de décisions, bibliographies), et l'appareil de contrôle a été **rejoué** plutôt que cru.

---

## 1. Note globale

| | |
|---|---|
| **Note** | **78 / 100** |
| **Verdict** | *Travail de recherche de très haute tenue méthodologique, d'une ampleur exceptionnelle pour un auteur seul, non publiable en l'état : révision majeure requise avant toute diffusion arbitrée.* |

Le dépôt se distingue par une chose rare : **il rend ses propres énoncés réfutables et les réfute lui-même**. Un simulateur exécutable contredit le traité qu'il transpose, une revue de littérature mesure que 77 % de son corpus n'est pas arbitré, un état de l'art déclare deux faits négatifs qui conditionnent sa lecture. Ce qui le retient sous la barre du publiable tient en trois points : **aucune validation humaine externe**, le plus gros livrable (1 000 pages) se déclare lui-même brouillon, et **l'appareil a fini par étouffer le contenu**.

---

## 2. Critères et pondération

| # | Critère | Poids | Note | Pondéré |
|---|---|---|---|---|
| 1 | Problématique et positionnement | 10 | 8,5 | 8,5 |
| 2 | Rigueur méthodologique et régime de preuve | 15 | 13 | 13 |
| 3 | Qualité et vérification des sources | 15 | 12,5 | 12,5 |
| 4 | Contribution scientifique et originalité | 15 | 11 | 11 |
| 5 | Artefacts logiciels et reproductibilité | 15 | 12,5 | 12,5 |
| 6 | Cohérence et structure du corpus | 10 | 6,5 | 6,5 |
| 7 | Qualité rédactionnelle et communication | 10 | 6 | 6 |
| 8 | Gouvernance du projet et intégrité intellectuelle | 10 | 8 | 8 |
| | **Total** | **100** | | **78** |

---

## 3. Ce qui a été mesuré pour cette évaluation

Toutes les commandes ci-dessous ont été exécutées le 5 septembre 2026 sur l'arbre de travail, avec `CARGO_TARGET_DIR` hors de OneDrive.

| Contrôle | Résultat |
|---|---|
| `cargo test --workspace --release` | **470 réussis, 0 échec** — concorde avec le `README.md` |
| `cargo clippy --workspace --all-targets --release` · `cargo fmt --all --check` | 0 et 0 |
| `python rejeu-politique.py` (6 - Article) | 0 — déroulés A et B, table 36/36, RÉF-6 non déclenchée |
| `python check-article.py` | 0 — 77 entrées / 77 citées, parité du rendu hors horodatage |
| `python Python/check-veille.py` · `check-revue.py` | 0 et 0 — 342/342 et 192 appariées |
| `python PRD/check-compendium.py` · `check-toc.py` · `check-sieges.py` | 0, 0, 0 — 50 pièces, C1-C16, 26 sièges ; 5 rapports déclaratifs |
| `bash PRD/decompte.sh --verifier` | 0 — quatre ancres tenues |
| `python Python/check-traite.py --sans-parite` | 0 — 143 p., 123 notices citées |
| `python figures/genere.py --verifier` | ⚠ **plantage** `UnicodeEncodeError` (console cp1252, caractère ⚠) — voir §6 |
| `python Python/check-empaquetage.py` sans `CARGO_TARGET_DIR` | INDÉTERMINÉ, comme déclaré |
| Vérification de quatre références arXiv de l'article à la source (`2604.20912`, `2603.10970`, `2604.14955`, `2606.09182`) | **Les quatre existent** ; titres, premiers auteurs et dates concordent |
| Historique git | 323 commits, 49 jours (24 juin – 4 sept. 2026), 301 signés par l'auteur, 20 par `Claude`, 4 fusions de PR |

---

## 4. Commentaires par critère

### 4.1 Problématique et positionnement — 8,5 / 10

La question est unique, énoncée en une phrase et tenue sur huit documents : *comment une entreprise de services financiers canadienne déploie, gouverne et exploite des agents d'IA autonomes sous contrainte réglementaire.* Le positionnement est précis — Canada-Québec, coopérative financière régie, triple tutelle AMF / BSIF / OCRI —, et c'est un créneau que la littérature internationale ne couvre pas. Le fil « découplage, contrat, évolution » du Vol. I et la thèse de l'**autonomie encadrée** du Vol. II donnent au corpus une colonne vertébrale.

Deux réserves. L'article HPC-QPU est **hors sujet**, le dépôt le dit lui-même ; il aurait sa place dans un dépôt distinct. La note de veille SDLC instruit une source unique et n'ajoute rien à la question posée.

### 4.2 Rigueur méthodologique et régime de preuve — 13 / 15

C'est le point fort du dépôt, et il est remarquable :

- **Niveaux de preuve explicites** `[A]` / `[B]` / `[C]`, degrés d'absence 1 à 3, dates de gel par pièce, protocole de revalidation (ch. 50) **éprouvé de bout en bout** sur un événement survenu.
- **Règle NF-15** du traité : *tout chiffre affiché doit être retrouvé par la mesure, ou l'écart consigné.* Cinq écarts consignés, dont deux absorbés par la source et un qui retourne un énoncé du traité (Φ_c ne sépare pas la conformité de la coordination). **Le code réfute le texte** ; c'est la forme la plus honnête de la recherche.
- Résultats négatifs déclarés et non dissimulés : quinze croisements protocole × texte canadien sans lien documenté ; NF-05 manquée d'un facteur 50 à 80 ; critère de sortie de la phase 6 « refait sur la mesure ».
- Les limites sont écrites *avant* les résultats (Revue : ni PRISMA, ni double codage, ni réplication ; Recension : accès aux textes de l'AMF par extraction tierce non reproductible).

Ce qui retient la note :

- Le niveau `[A]` — « vote adversarial à trois juges » — est rendu par **des instances d'un modèle de langage**, non par des relecteurs humains. Le dépôt le reconnaît (« des convergences entre rapports ne sont pas des convergences entre esprits indépendants ») mais continue de placer `[A]` *au-dessus* de `[B]`, la lecture directe d'une source primaire par l'auteur. Pour un jury, c'est l'inverse qui vaut.
- La boucle traité ↔ simulateur est **fermée sur un seul auteur** : le traité (3ᵉ éd.) absorbe les mesures du simulateur, le registre reclasse, la 4ᵉ édition date le reclassement. Rien d'externe n'entre dans la boucle.

### 4.3 Qualité et vérification des sources — 12,5 / 15

- Cinq bibliographies **closes dans les deux sens** et gardées par script (342, 192, 312, 123, 77). Notices avec DOI, arXiv, version, date de révision, statut d'arbitrage.
- Spot-check de quatre références arXiv de 2026 : **toutes réelles et exactes**. Aucun signe de référence fabriquée.
- Sources primaires réglementaires (E-23, B-10, E-21, Loi 25, règlement RTR, RFC 8693, SD-JWT RFC 9901) citées à leur texte et non par intermédiaire.
- La Revue mesure l'arbitrage de son corpus et **borne son propre résultat** par une contre-passe DBLP / Crossref. C'est exemplaire.

Réserves :

- Le champ est jeune : la matière repose sur des prépublications et des spécifications vivantes ; le dépôt le sait et le date, mais la péremption est réelle et rapide.
- Le Vol. I n'a **aucun contrôle propre** ; sa vérification bibliographique a été faite par des agents et trois entrées y sont marquées « non re-vérifiées ».
- **Auto-citation** massive et déclarée : l'état de l'art cite la veille, la revue, le traité et le compendium comme sources `[1]`-`[5]` « auto-publiées, non arbitrées », avec un doublon `[1]` / `[198]` non résorbé.
- La notice `[19]` du PDF de l'état de l'art est **brouillée** (mode mathématique sur `$`), constaté et non corrigé.

### 4.4 Contribution scientifique et originalité — 11 / 15

Contributions identifiables et défendables devant un jury :

1. **La grille des cinq questions** (qui est l'agent, pour qui, chaque saut autorisé, révocation, preuve à cinq ans) et le résultat qu'aucun des onze mécanismes relevés n'en remplit trois — un instrument d'analyse réutilisable.
2. **Le fait négatif vérifié** que E-23 n'emploie ni « agent » ni « orchestration », et le vide entre protocoles et droit canadien : un résultat modeste mais solide et daté.
3. **Le traité sur les essaims** : 143 pages, 13 algorithmes portant chacun modèle de panne, synchronisme, coût en messages et en tours, condition de validité — une forme rare dans la littérature de vulgarisation savante. La conclusion nomme six restes (deux métrologiques, trois théoriques, une impossibilité).
4. **La transposition exécutable comme méthode de réfutation** : le simulateur déterministe (parité natif/WASM mesurée au bit) est en soi une contribution méthodologique.
5. Le modèle de maturité en six paliers (technico-syntaxique → agentique), synthétique et communicable.

Ce qui limite la contribution :

- **Aucune contribution n'a été soumise à un arbitrage humain externe.** Tout reste « auto-publié, non arbitré », et le dépôt le sait.
- L'autonomie encadrée « n'est pas une découverte de l'auteur » (avant-propos du Vol. II) ; l'apport est le transport au Canada, présenté honnêtement comme un raisonnement.
- Le Compendium (Vol. IV) est une **somme dédoublonnée**, non une matière neuve, et se déclare « brouillon non publiable » sur ses cinquante pièces.
- L'article HPC-QPU est « documentaire », « numériquement non calibré », conduit « sans partenaire, sans contradicteur externe et sans accès expérimental » ; son script de rejeu rejoue les exemples de l'auteur — c'est un test de non-régression, pas une validation.

### 4.5 Artefacts logiciels et reproductibilité — 12,5 / 15

Vérifié : **470 tests verts, clippy et rustfmt à 0**. Le simulateur (31 000 lignes de Rust, quatre crates en chaîne linéaire) est d'une qualité d'ingénierie élevée : un seul fil, RNG semé unique, `HashMap` interdit par lint, transcendantes par `libm` avec banc DT1 qui a **mesuré** la divergence natif/WASM au lieu de la supposer, `#![deny(missing_docs)]` et `broken_intra_doc_links` sur les quatre crates, critères de sortie de phase écrits comme tests d'intégration, listes vivantes `hors_perimetre()` affichées à l'écran.

L'appareil documentaire est du même niveau : douze contrôles, trois harnais de **validation par mutation** (108 à 114 mutations), figures regravées « identiques à l'octet », assemblages reproduits à l'octet, parité de rendu vérifiée pour le traité et l'article.

Défauts, tous réels :

- **Aucune intégration continue.** NF-13 et NF-16 nomment un mécanisme que le dépôt ne contient pas ; aucun contrôle ne résout un lien markdown (243 renvois morts ont existé sans qu'aucun script le voie).
- `figures/genere.py --verifier` **plante** sur une console Windows cp1252 : les autres scripts font `sys.stdout.reconfigure(encoding="utf-8")`, celui-ci non. Défaut mineur, mais c'est précisément le genre que le harnais de mutation ne voit pas.
- NF-05 manquée d'un facteur 50 à 80 ; **dix mécanismes n'ont aucun appelant** ; l'interface s'arrête aux scénarios A et B ; seize exigences `EX-V*` sur vingt-trois n'ont pas de point d'appel.
- La chaîne de rendu dépend d'un poste précis : `CARGO_TARGET_DIR` hors OneDrive, mingw-w64 WinLibs, polices nommées, Pandoc + Typst à versions données. Quatre `build-pdf.sh` n'ont **pas été rejoués** par l'auteur ; les `.html` de la Recension ne se refont pas depuis le dépôt seul (feuille de style non versionnée).
- Le `/Title` du PDF de l'état de l'art perd son apostrophe, diagnostic fait, non corrigé ; 76 Mo de PDF versionnés sans LFS.

### 4.6 Cohérence et structure du corpus — 6,5 / 10

La carte du dépôt est claire, la table « par où entrer selon le temps qu'on a » est une bonne pratique. Mais :

- **La redondance est massive.** Vol. I (233 000 mots), Vol. II (93 000), Vol. III (161 000), puis le Compendium qui les dédoublonne (332 000), puis la Veille, la Revue et l'État de l'art qui reprennent MCP / A2A / ANP, E-23, l'AMF et la Loi 25 sous trois angles. Un lecteur rencontre la même matière **quatre à cinq fois**. Le tout pèse 2,8 millions de mots de markdown, sources doublées comprises.
- Les numérotations se contredisent : « huit documents » I à VIII au README, « Vol. IV » pour le compendium, six dossiers numérotés 1 à 6, « Vol. V » pour le traité qui vit dans `3 - Traité/`. Le compte des livrables est lui-même déclaré « constat, pas décision », et il a changé trois fois.
- Le plus gros livrable est un brouillon : cinquante pièces au statut « **Brouillon de rédaction, non publiable** », dont les énoncés « n'ont pas été ré-résolus contre les identifiants S-nnn » — le dépôt écarte explicitement ce ré-adossement (D-16). Un compendium de 1 000 pages dont le socle n'est pas réconcilié est une dette, pas une somme.
- Deux documents hors livrables vivent dans les dossiers des livrables.

### 4.7 Qualité rédactionnelle et communication — 6 / 10

Deux registres cohabitent, et ils ne se valent pas.

**Le corps doctrinal** — chapitres des monographies, sections du traité, corps de la veille — est écrit dans un français précis, dense, avec des phrases d'attaque efficaces (« La transposition conserve la structure de la preuve et casse trois de ses hypothèses »). Le §3.1 du traité, lu en entier, tient le niveau d'un cours de cycles supérieurs. Le sommaire exécutif de l'état de l'art est directement utilisable par un décideur.

**L'appareil** — README, en-têtes de pièces, registres — est devenu **illisible**. Le README de la racine consacre l'essentiel de ses 350 lignes à des décomptes d'octets remesurés, à des corrections de corrections et à des chroniques de redatation ; chaque en-tête de chapitre du compendium fait une page de ⚠ et de ☑ avant la première ligne de contenu. Le style — négation systématique (« ce que X n'est pas »), gras à haute densité, tirets cadratins en cascade, phrases de six lignes — est reconnu par l'auteur lui-même (le gabarit **mesure** 10,7 % de signes en gras et les rend au romain). *L'appareil qui devait garantir le contenu l'a recouvert.*

### 4.8 Gouvernance du projet et intégrité intellectuelle — 8 / 10

Points forts : registre des décisions avec provenance `[M]` / `[C]` / `[R]` et condition de réouverture ; décisions d'auteur numérotées et datées (D-1 à D-16) ; licence CC BY 4.0 posée et **œuvres de tiers sorties de l'index** avant qu'elle ne les couvre ; usage d'agents LLM **déclaré** dans les annexes de méthode (harnais multi-agents, votes, rapport d'arbitrage `eval.html` dont l'autorité est explicitement niée).

Réserves :

- Le README affirme « **les textes sont d'une seule main** », quand `git log` montre vingt commits signés `Claude` qui rédigent les onze chapitres du Livre I du compendium et le rapport de l'état de l'art. La responsabilité est bien d'une seule main ; la rédaction, non. Un jury attend une déclaration de contribution par document, non une mention dispersée dans les annexes.
- Le dépôt est « **clos et final** » depuis le 8 août 2026 et a été **rouvert une douzaine de fois** depuis. La clôture n'est pas crédible comme état ; elle l'est comme intention. L'unique étiquette `mono-v1.0` ne marque pas l'état clos.
- 49 jours de calendrier pour 3 000 pages et 31 000 lignes de Rust : la cadence est celle d'une production assistée, et la relecture humaine n'a pas pu suivre au même rythme — c'est la cause commune des réserves des §4.2 et §4.7.

---

## 5. Critiques de fond

1. **Le niveau `[A]` est survendu.** Trois juges LLM qui échouent à réfuter une affirmation n'établissent pas ce qu'un relecteur humain compétent établit. Reclasser `[A]` en `[A-auto]` et exiger un `[A-humain]` pour tout énoncé central.
2. **La boucle est fermée.** Traité, simulateur, PRD, revue et état de l'art se citent mutuellement et sont d'une même main ; le seul arbitrage externe (30 juillet 2026) est lui-même produit par des instances d'un modèle. Aucun énoncé du corpus n'a rencontré un contradicteur humain identifié.
3. **Le compendium contredit le corpus.** Il se veut la somme, il se déclare brouillon, et la décision D-16 renonce à réconcilier ses énoncés avec son propre socle. Il faudrait soit l'achever, soit le retirer du compte des livrables.
4. **La métrologie de l'appareil a pris le pas sur la métrologie de l'objet.** Le dépôt mesure ses octets, ses cardinaux et ses horodatages avec une rigueur que l'objet lui-même — le débit d'un essaim réel, la corrélation des fautes d'une flotte, un déploiement bancaire réel — n'a jamais reçue. Le traité le dit : « ce que le livre laisse ouvert n'est pas une théorie manquante mais une métrologie manquante ». Elle manque toujours.
5. **Aucune donnée empirique de terrain.** L'état de l'art le déclare : aucune source n'établit qu'une coopérative financière canadienne exploite un système multi-agents en production. Le corpus raisonne sur des spécifications et des textes, jamais sur un système observé.

---

## 6. Bonifications recommandées

Par ordre de rendement pour la note.

| # | Bonification | Effet attendu |
|---|---|---|
| 1 | **Soumettre le traité** — le livrable le plus abouti — à une revue arbitrée ou à deux relecteurs humains nommés, et publier leurs rapports | Ouvre la boucle ; seule action qui change le statut « non arbitré » |
| 2 | **Réécrire les README** : 40 lignes d'accueil par dossier, la chronique des passes déplacée dans un `JOURNAL.md` ; retirer ⚠/☑ et le gras de la prose d'accueil | Lisibilité ; c'est ce qu'un lecteur voit en premier |
| 3 | **Trancher le compendium** : le réconcilier (`S-nnn` ré-adossés, statut « publiable ») ou le sortir du compte des livrables et le déclarer archive de travail | Cohérence du corpus |
| 4 | **Intégration continue** (GitHub Actions) : `cargo test/clippy/fmt`, les douze contrôles, un résolveur de liens markdown | NF-13 et NF-16 tenues ; les 243 renvois morts ne reviennent plus |
| 5 | **Déclaration de contribution** par document (auteur humain / agents LLM / relecteurs), au modèle CRediT, et harmoniser « d'une seule main » | Intégrité de l'attribution |
| 6 | Fusionner Veille, Revue et État de l'art en un seul document à trois parties, ou publier une note de synthèse de 20 pages qui les remplace pour le lecteur pressé | Redondance divisée par trois |
| 7 | Corrections locales : `sys.stdout.reconfigure` dans `genere.py` ; versionner la feuille CSS ; échapper les `$` de la notice `[19]` ; post-traiter le `/Title` ; contrôle propre au Vol. I | Défauts connus soldés |
| 8 | Brancher les dix mécanismes sans appelant dans un scénario ou les retirer ; refaire NF-05 sur la mesure (index de lecture par partition ou cible revue) | Le code livré cesse de déclarer absent ce qu'il contient |
| 9 | Article HPC-QPU : implanter la branche de non-conformité d'`etalonnage/E2`, calibrer sur des données publiques d'étalonnage, sortir l'article du dépôt | Une des huit conditions de réfutation devient réellement exécutable |
| 10 | Étiquette `corpus-v1.0` sur l'état clos, DOI Zenodo, Git LFS pour les PDF, résumés en anglais | Citabilité et pérennité |

---

## 7. Projets futurs suggérés

Chacun part d'un reste que le corpus a lui-même nommé.

1. **Mesurer le débit d'un essaim réel.** Rejouer la loi d'échelle universelle (σ, κ) sur un Kafka instrumenté avec cinquante à mille agents ; c'est le premier reste du traité et la campagne que le simulateur ne peut pas remplacer.
2. **Mesurer la corrélation des fautes d'une flotte d'agents LLM.** Étendre le φ = 0,916 sur 18 000 missions à plusieurs modèles et plusieurs fournisseurs, avec hypothèse pré-enregistrée ; publier l'estimateur.
3. **Décomposer Φ_c.** Construire un modèle nul (trace mélangée) qui sépare la corrélation due au milieu de celle due à la fonction de décision ; c'est l'écart le plus fécond des cinq.
4. **Démontrer la borne spectrale du graphe biparti agents/partitions** — le seul reste purement théorique, publiable seul.
5. **Prototype de chaîne de mandat opposable.** Implanter les cinq questions (carte d'agent signée, `act` de RFC 8693, jetons de transaction, révocation) et l'éprouver contre E-23, la Loi 25 et la *Loi sur la preuve* avec un juriste ; c'est le trou central du corpus.
6. **Étude empirique auprès d'institutions financières canadiennes** (entretiens semi-dirigés, dix à quinze organisations) pour établir ce qu'aucune source ne documente : l'existence, ou non, de systèmes multi-agents en production sur un processus régi.
7. **Un article court tiré du traité** (12 pages, AAMAS, DEBS ou Middleware) : la transposition exécutable comme méthode de réfutation d'un traité — c'est la contribution méthodologique la plus originale, et elle tient en un article.
8. **Réplication indépendante de l'appareil** par un tiers sur une autre machine et un autre système : le dépôt affirme la reproductibilité à l'octet ; personne d'autre que l'auteur ne l'a constatée.
9. **Revalidation semestrielle automatisée** du socle `S-nnn` selon le protocole du ch. 50, avec rapport de péremption généré — le corpus se périme en semaines, l'outil existe, il manque la cadence.
10. **Banc de conformité E-23 pour systèmes agentiques** : un inventaire de modèles exécutable qui énumère ce qu'un cadre peut invoquer avant l'exécution, livré comme outil ouvert aux institutions fédérales avant le 1ᵉʳ mai 2027.

---

## 8. Conclusion du jury

Le dépôt est **un objet de recherche sérieux, d'une discipline méthodologique supérieure à la plupart des travaux arbitrés du même champ**, et il est en même temps **prisonnier de sa propre méthode** : tout y est daté, mesuré, consigné, sauf le monde qu'il décrit, et personne d'autre que son auteur ne l'a lu. La note de 78 récompense la rigueur et la franchise ; elle sanctionne l'absence de contradicteur humain, un livrable central inachevé, et une communication que l'appareil a rendue opaque. La voie la plus courte vers 90 est connue de l'auteur, qui l'a écrite lui-même à la conclusion du traité : *une métrologie manquante* — et un lecteur qui ne soit pas lui.
