# Évaluation académique du dépôt « Agentique »

*Évaluation conduite selon le [`Gabarit d'évaluation académique.md`](<Gabarit%20d%27%C3%A9valuation%20acad%C3%A9mique.md>), version 1.0. Elle est produite par un modèle de langage — Claude Fable 5.1, exécuté comme agent Claude Code sur le poste de l'auteur, à sa demande — et non par un jury humain ; la déclaration du §12 en fixe la portée. Chaque énoncé factuel porte son marqueur : **[L]** lu intégralement, **[E]** échantillonné, **[R]** rejoué, **[S]** confronté à la source externe, **[D]** déclaré par le dépôt et non vérifié.*

## 1. Fiche d'identité

| | |
|---|---|
| **Objet** | dépôt `agbruneau/Agentique`, branche `main`, commit `79ecdcf` du 5 septembre 2026 (« suppression évaluation »), arbre propre à l'ouverture **[R]** |
| **Date de l'évaluation** | 15 septembre 2026 |
| **Évaluateur** | Claude Fable 5.1 (`claude-fable-5-1`), agent Claude Code, à la demande de l'auteur, sur son poste — Windows 11, dossier synchronisé OneDrive |
| **Outils du rejeu** | Python 3.14.7, cargo et rustc 1.98.0, Pandoc 3.11, Typst 0.15.1, Node 24.19.0, wasm-bindgen 0.2.127, pymupdf 1.28.2 **[R]** |
| **Évaluation antérieure** | une `Évaluation académique.md` datée du 5 septembre 2026 a existé au dépôt et a été supprimée le même jour par le commit évalué ; elle a été relue dans l'historique git (`git show 79ecdcf^:"Évaluation académique.md"`) **[L]**. Aucune de ses conclusions n'est reprise ici sans avoir été refaite ; là où les constats coïncident, c'est que la mesure les rend de nouveau. |
| **Durée** | une session de travail, lecture et rejeu compris |

## 2. Verdict en tête

| | |
|---|---|
| **Total** | **75,5 / 100** — bande *Très bien*, à sa borne basse |
| **Catégorie de jury** | **Corrections majeures requises**, avec nouvelle évaluation — plafonnée par trois conditions bloquantes (B1, B2, B3) et une quatrième partiellement remplie (B4), §10 |

Le dépôt est un dossier de recherche d'une ampleur et d'une discipline méthodologique rares pour un auteur seul : dix documents, 3 009 pages rendues, un simulateur de 30 000 lignes qui contredit par la mesure le traité qu'il transpose, et un appareil de contrôle que cette évaluation a rejoué presque entier avec le même verdict que l'auteur. Ce qui le retient sous la barre de l'acceptable pour un jury tient à quatre choses. Aucun énoncé central d'aucune pièce n'a rencontré un relecteur humain nommé : le niveau de preuve le plus élevé du dossier est rendu par des instances d'un modèle de langage, et cette évaluation en est une aussi. Le plus gros livrable, mille pages, se déclare cinquante fois brouillon non publiable tout en comptant parmi les huit. L'appareil affirme une garantie qu'il ne tient pas : un contrôle sort 1 sur un arbre propre, pour une cause que le rejeu a établie. Et l'appareil documentaire, à force de mesurer ses propres octets, recouvre le corps doctrinal qu'il devait garantir. La voie vers l'acceptation est connue et courte à énoncer : un lecteur qui ne soit pas l'auteur, un compendium tranché, trois empreintes réancrées, et une déclaration de contribution par pièce.

## 3. Ce qui a été lu, rejoué, confronté

### 3.1 Lecture

| Pièce | Régime | Sections lues |
|---|---|---|
| `README.md`, `APPAREIL.md`, `LICENSE`, `.gitignore`, `.gitattributes` | **[L]** | entiers |
| `README.md` de `4 - Essais/1 - Traité/`, de `4 - Essais/2 - Article/`, de `0 - Références/` | **[L]** | entiers |
| `README.md` de `1 - Collection/`, `2 - Compendium/`, `3 - Veille/`, `5 - Recension/`, des trois volumes, de `docs/` du traité | **[E]** | plans complets ; sections d'accueil, « Réserves », « État », « Divergences », « Ce qui n'existe pas » |
| Vol. I — `Monographie.md`, `Chapitres/` | **[E]** | résumé, sigles, ch. 3 §3.0 (en entier), ch. 5 §5.0, ch. 7 §7.0, Annexe B §0, `TOC.md`, en-tête méthodologique de la bibliographie du ch. 3 |
| Vol. II — `monographie/` | **[E]** | avant-propos (entier), ch. 6 §6.1-6.2, ch. 13 §13.1, ch. 18 §18.1, fin du ch. 21, annexe A §A.1-A.4, registre de gel |
| Vol. III — `monographie/`, `verification/` | **[E]** | avant-propos, ch. 4 §4.1-4.2, ch. 9 §9.1, fin du ch. 28, annexe A (en-tête), `relecture-CA.md` §1, `theses-P4-confrontation.md` §1 |
| Vol. IV — `2 - Compendium/` | **[E]** | ch. 1 en-tête et §1.0, ch. 50 en-tête, `annexe-bibliographie.md` et `annexe-references.md` (régimes), `PRD.md` §7.2, §11, §16 (entier), `socle-consolide.md` (en-tête), `figures/genere.py` (registre) |
| Vol. V — `Traité.md` | **[E]** | résumé, introduction (entière), §3.1 (entier), §8.1, conclusion (entière), notices 102 à 123 |
| Vol. VI — `Veille Technologique.md` | **[E]** | résumé, protocole de revue, table des quinze passes, synthèse des enceintes, limites, les 25 questions ouvertes |
| Vol. VII — `Revue de littérature.md` | **[E]** | résumé, méthode (entière), physionomie du corpus (entière), confrontation n° 2, conclusion, annexe du corpus arbitré |
| Vol. VIII — `État de l'art — services financiers.md` ; planche `Cinq schémas` | **[E]** ; **[L]** | résumé, plan, « Limites de ce document » et « Conclusion » (entiers), notices 1 à 4, 19, 114, 115 ; planche entière |
| Note SDLC | **[E]** | résumé, plan des dix-huit thèses |
| Article HPC-QPU — `.typ`, `.bib`, `rejeu-politique.py` | **[E]** ; **[L]** | résumé, introduction, contributions, §10.2 (les huit conditions), conclusion ; script entier ; `.bib` partiel |
| Simulateur — `Cargo.toml`, `clippy.toml`, `rust-toolchain.toml`, `.gitignore`, `CLAUDE.md`, `docs/PRD.md`, `docs/decisions.md`, `audit.md` | **[L]** pour les quatre premiers ; **[E]** pour les autres | PRD §0.0-0.1, registre §PRD et §bancs, audit §1-2, CLAUDE.md §1 |
| `NiveauMaturité.html` | **[E]** | texte extrait |
| Historique git | **[R]** | `git log`, `git show`, `git ls-files`, `git cat-file` |

### 3.2 Rejeu de l'appareil

Toutes les commandes ont été exécutées le 15 septembre 2026 depuis le dossier prescrit, `PYTHONUTF8=1` posé sauf mention, `CARGO_TARGET_DIR` hors OneDrive pour `cargo`. L'annexe A donne les sorties abrégées.

| Contrôle | Verdict | Écart avec ce que le dépôt déclare |
|---|---|---|
| `python Python/check-veille.py` | ☑ 0 — 94 sections, 24 tableaux, 25 questions ; 342 définies, 342 citées | aucun |
| `python Python/check-revue.py` | ☑ 0 — 192 ; 12 attestées, 32 auto-déclarées, 145 sans revue sur 189 | aucun |
| `python Python/check-traite.py` | ☑ 0 — 143 p., 123 notices citées, parité 1 551 326 o hors horodatage | aucun |
| `python PRD/check-compendium.py` | ☑ 0 — 50 pièces, **P1-P10, 5 rapports déclaratifs** | `APPAREIL.md` écrit P1-P8 et 3 rapports |
| `python PRD/check-toc.py` | ☑ 0 — **C1-C16** | `APPAREIL.md` écrit C1-C15 |
| `python PRD/check-sieges.py` | ☑ 0 — 26 sièges, S1-S5 | aucun |
| `bash PRD/decompte.sh --verifier` | ☑ 0 — 93 239 / 160 890, agrégat 479 387 | aucun |
| `python build/verifier-piece.py` | ☑ 0 — 50 rendus `.html` conformes | non couvert par `APPAREIL.md` |
| `python figures/genere.py --verifier` | ⚠⚠ **1 — 3 défauts aux figures antérieures** ; sans `PYTHONUTF8`, `UnicodeEncodeError` | `APPAREIL.md` écrit ☑ 0 — **voir §8.1** |
| `python PRD/check-sieges-mutations.py` | ☑ **114** mutations attrapées | `APPAREIL.md` écrit 108 |
| `python PRD/check-toc-mutations.py` | ☑ toutes détectées, M16b comprise | aucun |
| `python PRD/check-compendium-mutations.py` | ☑ **23** mutations vues | `APPAREIL.md` écrit 17 |
| `python rejeu-politique.py` | ☑ 0 — déroulés A et B, table 36/36, gardes | aucun ; réserve au §8.6 |
| `python check-article.py` | ☑ 0 — 77/77, parité 751 989 o hors horodatage, 165 renvois, 10 cardinaux, 8 scores | aucun |
| `python check-article-mutations.py` | ☑ 7 mutations vues | aucun |
| `typst compile article-hpc-qpu.typ` (sortie hors dépôt) | ☑ **752 159 o**, taille exacte du PDF livré | aucun |
| `python Python/check-empaquetage.py` sans `CARGO_TARGET_DIR` | INDÉTERMINÉ, exit 1, comme déclaré | aucun |
| `python Python/check-resume.py` sur les onze PDF composés | ☑ 0 sur dix ; **1 sur l'article**, verdict documenté comme inapplicable ; **« LIMITE : 1,7 pt »** sur `Compendium.pdf`, 0,3 pt sur la planche | l'alerte du Compendium n'est écrite nulle part — §8.5 |
| `python figures/contenu.py` (traité, 19 SVG) | ☑ identiques **modulo fins de ligne** : `git diff --ignore-cr-at-eol` vide, `git diff` plein | « identiques à l'octet » vaut après normalisation LF — §8.3 |
| `python figures/dessine.py` (recension, 5 SVG) | ☑ identiques à l'octet | aucun |
| `python build/assemble.py` (Vol. II et III) | ☑ 38 blocs / 853 Ko et 34 pièces / 1 097 Ko, identiques **modulo fins de ligne** | même réserve — §8.3 |
| `cargo test --workspace --release` | ☑ **470 réussis, 0 échec, 0 ignoré** | aucun |
| `cargo clippy --workspace --all-targets --release` | ☑ 0 | aucun |
| `cargo fmt --all --check` | ☑ 0 ligne | aucun |
| Pages des PDF, `pymupdf` | ☑ 569, 387, 427, 1 000, 143, 144, 59, 186, 7 = **2 922** ; + 49 + 38 = **3 009** | aucun |
| Résolution des 1 996 renvois relatifs des 219 `.md` versionnés | ⚠ **8 morts** : 3 vers `2 - Compendium/audit.md`, **5 vers l'évaluation supprimée** | les 5 sont nés du commit évalué — §8.2 |

**Non rejoué** : les sept `build/build-pdf.sh` (chaîne Pandoc → Typst des volumes, de la veille, de la recension), la construction WASM et `check-empaquetage.py` avec cible, les bancs Node, le binaire `campagne` et les exemples. Ce que ces chaînes produisent n'est donc jugé que sur les PDF livrés.

### 3.3 Sources confrontées

Dix références, tirées de six pièces différentes et choisies pour porter chacune un fait que le dossier fait travailler ; aucune ne recoupe les quatre que l'évaluation antérieure avait vérifiées. L'annexe B détaille.

| Résultat | Compte |
|---|---|
| atteintes et **exactes** — titre, auteurs, date, et le fait précis que la pièce leur prête | **9** |
| non atteintes (deux adresses du BSIF essayées, HTTP 404 — adresses de l'évaluateur, non du dossier) | 1 |
| inexactes ou fabriquées | **0** |

## 4. L'objet, décrit par l'évaluateur

Le dépôt instruit une question unique — *comment une entreprise de services financiers canadienne déploie, gouverne et exploite des agents d'IA autonomes sous contrainte réglementaire* — par huit documents qu'il déclare livrables, tous en français, tous composés en PDF par Pandoc et Typst depuis une source Markdown, sauf un **[L]**. Trois monographies forment le triptyque d'origine : le Vol. I pose la théorie mondiale de l'interopérabilité et de l'ingénierie agentique (569 p.), le Vol. II l'orchestration sous droit canadien et la thèse de l'*autonomie encadrée* (387 p.), le Vol. III l'identité, la délégation et la « fabrique de confiance » (427 p.). Un compendium de 1 000 pages exactement les dédoublonne (Vol. IV). Un traité sur les essaims d'agents (143 p., Vol. V) est transposé en simulateur Rust déterministe de 30 488 lignes **[R]**, quatre *crates*, 470 tests. Une veille (144 p.), une revue de littérature (59 p.) et un état de l'art sectoriel (186 p. et une planche de 7 p.) mesurent le champ. S'y ajoutent, hors livrables par décision des `README` et non de l'auteur, une note de veille sur une source unique (49 p.) et une prépublication au gabarit arXiv sur l'ordonnancement de processeurs quantiques (38 p.), hors sujet déclaré **[L]**.

Le tout pèse 585 fichiers et 79,5 Mo à l'index **[R]** — 15 PDF, 219 `.md`, 142 `.svg`, 76 `.rs`, 53 `.html`, 39 `.py`. Les fichiers Markdown versionnés totalisent **3,10 millions de jetons** au compte `\w+` **[R]**, pour une matière source que le dépôt mesure lui-même à 479 387 mots sur les trois volumes **[R]** : le reste est assemblage, compendium, appareil et chronique. L'historique court du 24 juin au 5 septembre 2026, 326 commits — 304 signés de l'auteur, 20 signés `Claude`, 2 sous son identifiant GitHub —, quatre fusions de demandes de tirage, une étiquette `mono-v1.0` **[R]**. La licence est CC BY 4.0 depuis le 21 août 2026, les œuvres de tiers ayant quitté l'index le même jour **[L]**.

Le dossier a une propriété que peu de travaux universitaires possèdent : il se mesure lui-même. Douze contrôles versionnés, trois harnais de validation par mutation, des dates de gel par pièce, des registres de décisions avec condition de réouverture, et une règle — *tout chiffre affiché doit être retrouvé par la mesure, ou l'écart consigné* — que le simulateur applique au traité et retourne contre lui. Il a une seconde propriété, qui est le revers de la première : il consacre à la mesure de ses propres octets, cardinaux et horodatages un soin que le monde qu'il décrit n'a jamais reçu.

## 5. Fiches par pièce

### 5.1 Vol. I — *Interopérabilité agentique en entreprise dans le domaine des services financiers*

| Champ | |
|---|---|
| **Identité** | `1 - Collection/1 - InteroperabiliteAgentique/` ; **569 p.** [R] ; 263 658 jetons dans `Monographie.md` [R] (le dépôt écrit 233 257 mots par `wc -w`) ; socle arrêté à juin 2026 ; sept bibliographies, 1 263 entrées relevées par l'assembleur du compendium [D] |
| **Thèse** | « cette transposition n'abolit pas les acquis de l'intégration d'entreprise : elle les *réinstancie* à un niveau d'abstraction supérieur » (`TOC.md`) ; patron directeur : *autonomie graduée sous contrôle de finalité* (ch. 5) [E] |
| **Méthode déclarée** | « recherche en éventail » puis « vérification adverse de chaque citation sur le web » par bibliographie — ch. 3 : 194 références vérifiées, 165 retenues, 24 corrigées, 3 ajoutées « non re-vérifiées en adverse » [E] ; le PRD du compendium range ses faits en **[C]**, la vérification du volume portant « sur les références et non sur le contenu des affirmations » [L] |
| **Lecture faite** | résumé, sigles, ch. 3 §3.0, ch. 5 §5.0, ch. 7 §7.0, Annexe B §0, `TOC.md`, en-tête de la bibliographie du ch. 3 [E] |
| **Rejeu** | aucun contrôle propre n'existe pour ce volume — `APPAREIL.md` le dit [L] ; pages mesurées [R] ; `build-pdf.sh` non rejoué |
| **Forces** | (1) couverture encyclopédique datée, du LCIM de Tolk et Muguira aux protocoles de 2026, avec une carte de renvois stable entre chapitres (ch. 3 §3.0.2) ; (2) la grille de Yuan *et al.* — communication, syntaxique, sémantique — mobilisée comme fil analytique, et la référence est exacte [S] ; (3) le tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF du ch. 7, instrument prospectif honnête ; (4) une Annexe B d'architecture détaillée de 28 diagrammes, avec ADR, registre des risques, traçabilité ; (5) la désambiguïsation systématique des homonymes (deux « ACP ») |
| **Faiblesses** | (a) aucun script ne garde ce volume : ni appariement des citations, ni pagination, ni parité de rendu ; (b) le régime de preuve est le plus faible des trois volumes et le compendium le rétrograde en **[C]** — ce que le volume lui-même n'écrit pas ; (c) l'Annexe B instancie « intégralement » sur la pile d'un éditeur, IBM, et se déclare « architecture engageante » : c'est un livrable de conseil dans un dossier de recherche, et la neutralité fournisseur y tient à une clause de lecture ; (d) 653 marqueurs ⚠ dans l'assemblage [R], légitimes pour des ressources vivantes, mais qui rendent le volume périssable par construction ; (e) l'article de synthèse et le démonstrateur Go qui l'accompagnaient ont été retirés du dépôt, et des volumes aval les citent encore contre une numérotation sans cible [L] ; (f) `Creator` du PDF en Typst 0.15.0 quand les onze autres sont en 0.15.1 [R], trace d'une chaîne non rejouée depuis |
| **Niveau** | **Très bien** — 78 % |
| **Publiabilité** | se donne « rédaction terminée », finalisation « ne sera pas conduite » ; l'évaluation le tient pour un manuel de référence publiable en l'état comme ouvrage de synthèse, non comme travail de recherche arbitré, faute d'un régime de preuve sur le contenu |

### 5.2 Vol. II — *Orchestration agentique*

| Champ | |
|---|---|
| **Identité** | `1 - Collection/2 - OrchestrationAgentique/` ; **387 p.** [R] ; 93 239 mots de corps par la commande de référence [R] ; gel 16-17 juillet 2026 ; socle de 46 entrées F-01 à F-48 [L] |
| **Thèse** | « sous exigence réglementaire stricte, le processus est imposé de façon déterministe par le cadre, qui invoque les agents ; les agents n'orchestrent pas le processus » — *autonomie encadrée*, « pas une découverte de l'auteur » (avant-propos) [L] |
| **Méthode déclarée** | trois passes d'un « harnais de recherche multi-agents », 324 agents, 384 affirmations extraites, **75 soumises au vote adversarial à trois juges**, 69 confirmées ; niveaux **[A]** vote 3-0 > **[B]** source primaire lue > **[C]** repérage ; incident de la passe 3 déclaré — quatre angles non votés (annexe A) [L] |
| **Lecture faite** | avant-propos, ch. 6 §6.1-6.2, ch. 13 §13.1, ch. 18 §18.1, ch. 21 (journal de clôture), annexe A, registre de gel [E] |
| **Rejeu** | `assemble.py` reproduit `Monographie.md` modulo fins de ligne [R] ; `decompte.sh` tient l'ancre 93 239 [R] ; pages [R] ; F-36 et F-37 confrontés à arXiv, exacts [S] |
| **Forces** | (1) le fait négatif vérifié qui porte le livre — E-23 n'emploie ni « agent » ni « orchestration », vérification mécanique sur le texte intégral — et la discipline qui sépare *fait négatif vérifié* et *absence de documentation au corpus* ; (2) le ch. 13, qui traduit onze exigences canadiennes en cadres d'architecture et dit, ligne par ligne, où la traduction est une inférence d'auteur ; (3) le ch. 18, matrice de quinze croisements protocole × texte, tous vides, et qui explique pourquoi c'est un résultat ; (4) la déclaration que les trois sources de l'autonomie encadrée « ne sont pas indépendantes » — deux partagent une autrice — et la portée exacte qu'il en tire ; (5) 254 marqueurs « Lecture de l'auteur » [R] qui séparent glose et socle |
| **Faiblesses** | (a) 46 entrées de socle pour 387 pages : la densité de preuve est faible, et le vote adversarial n'a touché que 75 affirmations sur 384 ; (b) la hiérarchie **[A]** > **[B]** place un vote de trois instances de modèle au-dessus de la lecture directe d'un texte officiel par l'auteur — l'annexe A le justifie par « ce que l'affirmation a subi », mais ce qu'elle a subi est trois lectures du même modèle, non trois esprits ; (c) la Partie VII instancie sur IBM, « cas documenté », avec la même réserve qu'au Vol. I ; (d) la ligne directrice de l'AMF n'est au socle que par son calendrier — le texte le plus applicable à une institution québécoise n'a pas été lu ; (e) le journal de clôture du ch. 21 porte une réserve de méthode non tranchée sur ses propres décomptes [E] |
| **Niveau** | **Très bien** — 85 % — la pièce la plus rigoureuse du triptyque |
| **Publiabilité** | se donne rédigé, relu adversarialement, clos ; l'évaluation le tient pour publiable après relecture humaine d'un juriste sur les ch. 9 à 13 — c'est la seule pièce du dossier dont la révision se mesure en semaines |

### 5.3 Vol. III — *L'entreprise agentique — la fabrique de confiance*

| Champ | |
|---|---|
| **Identité** | `1 - Collection/3 - EntrepriseAgentique/` ; **427 p.** [R] ; 160 890 mots de corps [R] ; gel 21 juillet 2026 ; socle propre de 98 entrées, hérité de 33 [L] ; 30 rapports sous `verification/` |
| **Thèse** | « la confiance ne se décrète pas, elle se fabrique : émettre une identité, l'appliquer, l'exploiter » (`README.md`) ; grille des cinq questions du ch. 4 — *qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond* — et « aucun des trois mécanismes instruits par ce volume ne répond aux cinq » [E] |
| **Méthode déclarée** | quinze lots de recherche, relecture adversariale par « relecteur distinct du rédacteur » (CA-14), quatorze critères d'acceptation, registre de remontées ; les degrés d'absence 1 à 3 (R-14) ; l'annexe A écrit que « la méthode prescrite et la méthode appliquée ne coïncident pas partout » [E] |
| **Lecture faite** | avant-propos, ch. 4 §4.1-4.2, ch. 9 §9.1, ch. 28 (journal), annexe A, `relecture-CA.md` §1, `theses-P4-confrontation.md` §1 [E] |
| **Rejeu** | `assemble.py` reproduit modulo fins de ligne [R] ; ancre 160 890 tenue [R] ; RFC 9901 confronté, exact [S] |
| **Forces** | (1) la grille des cinq questions, instrument réutilisable, déclarée « construction d'auteur », spécifiée au PRD et **falsifiable** — un mécanisme qui répond aux cinq la réfute ; (2) la lecture de RFC 8693 §1.1 et §4.1 au ch. 9 — la délégation nommée, le jeton décliné — qui refuse d'écrire « OAuth ne permet pas » là où le texte ne spécifie pas ; (3) `theses-P4-confrontation.md`, qui confronte treize thèses au socle *avant* rédaction et découvre huit formes de dérive non prévues ; (4) les trente rapports de vérification, restaurés après suppression accidentelle ; (5) le refus de trancher deux divergences factuelles entre volumes par la chronologie |
| **Faiblesses** | (a) le volume se déclare « rédigé non publiable » et l'est resté à la clôture : quinze remontées ouvertes, dette de vote sur F-92 et F-96 qui « fondent le ch. 26 » ; (b) la « distinction rédacteur / relecteur n'est pas constatable sur disque » — le volume l'écrit lui-même ; le relecteur distinct est une autre instance du même modèle ; (c) l'appareil envahit le corps : 21,2 % des signes de `Monographie.md` sont en gras [R], 543 ⚠, et chaque pièce ouvre sur un tableau d'en-tête où la volumétrie se re-mesure trois fois ; (d) les volumétries dépassent les cibles de 44 à 127 % et l'écart « se documente, il ne se corrige pas par amputation » — règle défendable, mais qui a produit un volume d'un tiers plus long que prévu ; (e) deux corpus cités ont quitté le dépôt et 106 renvois ne résolvent plus [L] ; (f) `commun/faits-partages.md`, annoncé comme source unique de vérité, « n'existe pas et ne sera pas créé » |
| **Niveau** | **Satisfaisant** — 72 % |
| **Publiabilité** | se donne non publiable ; l'évaluation concorde, pour les motifs que le volume nomme, et ajoute que la lisibilité devrait être reprise avant toute relecture externe |

### 5.4 Vol. IV — *Conspectus / Compendium — Interopérabilité et Orchestration en Entreprise Agentique*

| Champ | |
|---|---|
| **Identité** | `2 - Compendium/` ; **1 000 p.** exactement [R] ; 50 chapitres en 5 Livres, en `.md` et en `.html` ; socle consolidé de 159 entrées `S-001` à `S-159` ; bibliographie réunie de 1 154 entrées [D] ; gel unique 27 juillet 2026 [L] |
| **Thèse** | « la somme des trois volumes, dédoublonnée et re-datée à la source » (`README.md` racine) [L] |
| **Méthode déclarée** | sept portes G-1 à G-7, quatorze critères CA-IV, trois régimes de preuve par Livre, quatre contrôles outillés avec harnais de mutation, revalidation datée (ch. 50) [E] |
| **Lecture faite** | `README.md` (en-tête, Appareil, Régimes, angles morts, Horloge), ch. 1 et ch. 50 (en-têtes et §1.0), `PRD.md` §7.2, §11, §16, annexes B et I (régimes), `socle-consolide.md` (en-tête) [E] |
| **Rejeu** | `check-compendium.py`, `check-toc.py`, `check-sieges.py`, `decompte.sh`, `verifier-piece.py` : ☑ 0 [R] ; trois harnais de mutation : ☑ [R] ; `genere.py --verifier` : **⚠⚠ 1** [R], §8.1 ; `check-resume.py` : « LIMITE 1,7 pt » [R], §8.5 |
| **Forces** | (1) l'appareil le plus outillé du dépôt — quatre contrôles, trois harnais qui attrapent 114, 23 et 23 mutations, parité `.md` / `.html` vérifiée ; (2) le socle consolidé, avec 123 entrées à sensibilité temporelle re-datées à la source et classées *inchangée / changée / non établie* ; (3) le protocole de revalidation du ch. 50, **éprouvé de bout en bout** sur la révision protocolaire du 28 juillet 2026 — détection puis réparation ; (4) deux angles morts déclarés plutôt que comblés — le harnais d'exécution, l'accord sous défaillance ; (5) la franchise du PRD §16 : « une dette qu'on cesse de suivre reste une dette ; elle change seulement de nom » |
| **Faiblesses** | (a) **les cinquante pièces se déclarent « Brouillon de rédaction, non publiable »** [R], et le volume compte parmi les huit livrables — condition bloquante B2 ; (b) sept annexes sur neuf « ne seront pas écrites » ; (c) 524 emplois nus de `F-xx` / `H-xx` que la décision D-16 renonce à ré-adosser aux `S-nnn` : la table des faits existe et le corps ne la cite pas ; (d) la cible de **mille pages exactement**, « vérifiée par le script de rendu, qui échoue à 999 comme à 1 001 », est une contrainte de forme prise pour une exigence, et le calage doit être re-mesuré à chaque passe — 16,95 puis 16,98 puis 16,80 pt ; (e) chaque chapitre ouvre sur **7 à 11 Ko d'en-tête** avant la première ligne de corps [R] ; les `README` de Livre composent 24 à 38 % de leurs signes en gras [R] ; (f) le résumé du PDF est à 1,7 pt de la marge basse, et rien ne l'écrit ; (g) trois figures gelées portent une empreinte prise sur des octets CRLF, et le contrôle qui les garde échoue sur l'arbre normalisé ; (h) trois renvois vers `audit.md`, supprimé le 2 septembre, restent morts dans le PRD et le TOC [R] |
| **Niveau** | **Passable** — 55 % comme livrable ; l'appareil seul serait *Très bien* |
| **Publiabilité** | se donne non publiable, cinquante fois ; l'évaluation concorde et pose la question que le dossier évite : un compendium de mille pages dont le socle n'est pas réconcilié est une dette de lecture, pas une somme |

### 5.5 Vol. V — *Traité sur les systèmes multiagents en essaim*

| Champ | |
|---|---|
| **Identité** | `4 - Essais/1 - Traité/Traité.md` ; **143 p.** [R] ; 72 511 mots par `check-traite.py` [R] ; quatrième édition du 2 septembre 2026 ; 8 chapitres, 24 sections, **123 notices**, 19 figures, 13 algorithmes numérotés [L] |
| **Thèse** | « l'architecture gagnante déplace alors la coordination vers un substrat événementiel partagé, durable et ordonné localement, où les agents déposent et lisent des traces plutôt que de négocier des décisions » ; et « il existe entre les deux régimes une frontière identifiable » (résumé) [L] |
| **Méthode déclarée** | « chaque mécanisme y porte son modèle de panne, son hypothèse de synchronisme, son coût en messages et en tours, et la condition sous laquelle il cesse de valoir » ; « un nombre sans provenance y est traité comme une faute de rédaction » ; sources primaires « consultées directement », statut éditorial indiqué [L] |
| **Lecture faite** | résumé, introduction, §3.1, §8.1, conclusion, notices 102-123 [E] |
| **Rejeu** | `check-traite.py` ☑ 0, parité du PDF hors horodatage [R] ; 19 figures regravées, identiques modulo fins de ligne [R] ; notices [119] et [121] confrontées, exactes au chiffre — 90,0 %, φ 0,916, 18 000 missions ; 266 contre 21 ; 18 agents sur 30 [S] |
| **Forces** | (1) la meilleure écriture du dossier : 0,5 % de gras [R], des phrases d'attaque qui portent l'argument (« La transposition conserve la structure de la preuve et casse trois de ses hypothèses ») ; (2) l'algorithme 3.1 comme modèle de la forme exigée — modèle de panne, synchronisme, topologie, coût par tour, coût en tours, quatre modes de défaillance, dont un qui « confond mort et convergence » ; (3) une conclusion qui nomme **six restes** — deux métrologiques, trois théoriques, une impossibilité — et dit lequel a rétréci depuis l'édition précédente ; (4) le ch. 8, qui absorbe une campagne de mesures postérieure et en dresse l'inventaire des sept énoncés dont le domaine de validité change ; (5) la boucle avec le simulateur : « le livre n'a donc pas échangé une ignorance contre une dette : il a proposé, l'auteur a mesuré, et la mesure lui est revenue contre » |
| **Faiblesses** | (a) aucun relecteur externe ; les « deux lecteurs indépendants » du bloc de réglage ont jugé la typographie, non le fond ; (b) le ch. 8 repose sur **une source unique et postérieure** — un rapport de laboratoire sur ses propres modèles, sans comité de lecture, la notice le dit — et sur une prépublication non répliquée [121] ; le traité en tire des révisions de domaine de validité, ce qui est beaucoup pour deux pièces non arbitrées ; (c) le « point de retournement chiffré au chapitre 2 reste donc une illustration arithmétique » — la conclusion le dit, et c'est le résultat le plus cité du livre ; (d) la notice [120] cite le simulateur à « 428 tests, dépôt au 15 août 2026 », valeur périmée, datée mais périmée ; (e) la borne τ < π/(4(n − 1)) est discutée à 0,42 % près d'arrondi (§3.1) — précision louable qui contraste avec l'absence de tout protocole de mesure sur un journal réel |
| **Niveau** | **Très bien** — 86 % ; la pièce la plus aboutie du dossier |
| **Publiabilité** | se donne publié en quatrième édition ; l'évaluation le tient pour **soumissible** à une revue ou à un éditeur universitaire après relecture par deux spécialistes des systèmes répartis — c'est la pièce à porter à l'arbitrage en premier |

### 5.6 Vol. VI — *Veille technologique en entreprise*

| Champ | |
|---|---|
| **Identité** | `3 - Veille/Veille Technologique.md` ; **144 p.** [R] ; 65 905 jetons [R] (42 142 mots hors bibliographie [D]) ; gel 15 août 2026 ; **342 références**, 94 sections, 24 tableaux, 25 questions ouvertes [R] |
| **Thèse** | « l'agent d'entreprise fiable de 2026 est *enveloppé* » ; sept couches implicites, et le déficit de délégation au-delà de deux sauts « n'est plus d'invention, il est d'adoption » (résumé) [L] |
| **Méthode déclarée** | pipeline multi-agents en cinq phases, « exécuté par des agents LLM (Claude, Anthropic) », régime fort — trois vérificateurs chargés de réfuter — et régime faible — contre-vérification individuelle ; **quinze passes** tabulées avec leur régime, du 2 juillet au 15 août ; « revue structurée et vérifiée, non systématique au sens PRISMA » [L] |
| **Lecture faite** | résumé, protocole, table des passes, synthèse des enceintes, limites, questions ouvertes [E] |
| **Rejeu** | `check-veille.py` ☑ 0 [R] ; `check-resume.py` ☑ [R] |
| **Forces** | (1) la table des quinze passes, qui dit pour chaque section quel régime la porte — « les faits ne pèsent donc pas tous le même poids » ; (2) six réfutations de ses propres affirmations porteuses en dix jours, instruites dans leurs sections ; (3) la correction de méthode du 15 août — « un fait négatif de dépôt ne s'établit pas sur la branche par défaut » — et les deux énoncés qui n'y survivent pas ; (4) la cartographie des enceintes de normalisation avec statut normatif réel ; (5) vingt-cinq questions ouvertes qui font programme |
| **Faiblesses** | (a) les trois passes de veille d'août n'ont « aucune ronde adverse » — l'édition qui date le document est au régime le plus faible ; (b) les sources québécoises refusent la consultation automatisée et la veille rétracte une de ses datations — résultat honnête, mais le régulateur du destinataire reste non lu ; (c) 10,4 % de gras [R], que le gabarit de rendu doit corriger à la composition — le document le mesure lui-même ; (d) auto-citation déclarée mais circulaire : les sections 4.12 et 8.4 reposent sur deux corpus du même auteur, dont un démonstrateur retiré du dépôt ; (e) le contrôle a « validé pendant trois éditions ce qu'il ne mesurait pas » (sept titres non détectés) — corrigé, mais le `README` note que le contrôle « réimplémente le comportement de Pandoc, il ne l'interroge pas » |
| **Niveau** | **Très bien** — 80 % |
| **Publiabilité** | se donne publiée ; l'évaluation la tient pour un rapport de veille de qualité professionnelle, citable comme littérature grise datée, non comme revue systématique |

### 5.7 Vol. VII — *Revue de la littérature académique*

| Champ | |
|---|---|
| **Identité** | `3 - Veille/Revue de littérature.md` ; **59 p.** [R] ; 30 787 jetons [R] ; gel 15 août 2026 ; **192 références**, 189 arXiv, 8 tableaux, dix fronts [R] |
| **Thèse** | « douze pièces sur 189 — 6 % — portent une attestation de publication dans leur notice » ; « les 145 restantes, soit 77 % de ce corpus arXiv, ne présentent aucun signe de revue par les pairs » ; et l'interdiction d'en faire une part du champ [L] |
| **Méthode déclarée** | notices reprises à l'API d'exportation d'arXiv les 9 et 15 août ; règle stricte — seuls `journal_ref` ou DOI valent publication ; « ni protocole enregistré au sens PRISMA, ni double codage, ni recherche multi-bases » ; « aucune réplication » [L] |
| **Lecture faite** | résumé, méthode, physionomie, confrontation n° 2, conclusion, annexe du corpus arbitré [E] |
| **Rejeu** | `check-revue.py` ☑ 0 — 12 / 32 / 145 sur 189 [R] |
| **Forces** | (1) le résultat méta, honnête et borné dans les deux sens par une contre-épreuve DBLP / Crossref — « les 145 sont un plafond du non-arbitré, les 12 un plancher de l'arbitré » ; (2) « deux de ces chiffres sont en partie fabriqués par l'instrument, et il faut le dire avant d'en tirer quoi que ce soit » ; (3) la structure par front — *ce que la littérature établit, où elle se contredit, ce qu'elle ne traite pas* ; (4) la confrontation de trois énoncés de la veille, dont deux sortent modifiés ; (5) le suivi des révisions de notices — une pièce qui « a doublé de volume le 10 août » et requalifié ses démonstrations |
| **Faiblesses** | (a) une seule base interrogée, un seul jugement par rétention : la revue le dit, mais une revue de littérature à un codeur n'est pas arbitrable ; (b) le résultat principal porte sur la forme du corpus retenu — il dit peu du champ, et le document le répète cinq fois ; (c) vingt-sept pièces du socle hérité « ne valent ici que comme arrière-plan » — elles gonflent le compte de 192 ; (d) aucune réplication, aucun banc — la revue rapporte ce que les pièces revendiquent |
| **Niveau** | **Très bien** — 78 % |
| **Publiabilité** | se donne publiée ; l'évaluation la tient pour une revue narrative outillée, citable pour son résultat méta, non comme revue systématique |

### 5.8 Vol. VIII — *État de l'art en services financiers*, et la planche *Cinq schémas*

| Champ | |
|---|---|
| **Identité** | `5 - Recension/` ; **186 p.** et **7 p.** [R] ; 92 516 jetons [R] ; gel 20 août 2026 ; **312 références**, 15 sections, 5 figures [D, plan vérifié] |
| **Thèse** | « le débat d'entreprise porte sur le choix de la pile protocolaire, mais dans une coopérative financière régie la pile n'est pas ce qui décide » ; trois surveillants, un socle ; « une plateforme mutualisée est un tiers » (résumé) [L] |
| **Méthode déclarée** | « chaque affirmation confrontée à sa source primaire et datée » ; « aucune mesure de terrain » ; couche québécoise « sur un accès partiel et détourné » — trois HTTP 403 le 20 août 2026, extraction par service tiers non reproductible ; « un fait non atteint en source primaire n'est pas un fait de ce document » [L] |
| **Lecture faite** | résumé, plan, « Limites », « Conclusion », notices 1-4, 19, 114-115 ; planche entière [E] / [L] |
| **Rejeu** | `check-resume.py` ☑ 0 sur les deux PDF, 12,6 et 0,3 pt de dégagement [R] ; `dessine.py` : 5 SVG identiques à l'octet [R] ; `/Title` du PDF long lit « État de lart en services financiers » [R] ; notice [114] confrontée — 30 juin 2026, entrée en vigueur du règlement le 24 août 2026, lancement au T4 [S] |
| **Forces** | (1) le déplacement de la question, du protocole au régime juridique de l'appelant — « le même serveur d'outils est deux objets réglementaires selon l'appelant » ; (2) les cinq exigences d'une chaîne de délégation et les onze mécanismes relevés, « aucun ne remplit trois des cinq colonnes », la seule case pleine étant la *Loi sur la preuve* ; (3) la section « Limites » comme modèle du genre — asymétrie de régime localisée, retrait d'une source [310] rapporté comme fait, portée exclue par ligne d'affaires déclarée ; (4) une conclusion qui parle au décideur en quatre décisions irréversibles, dont « le rail a supprimé votre filet » ; (5) la planche de sept pages, qui explique cinq figures « pour qui n'a pas lu le document » et ne prétend rien démontrer |
| **Faiblesses** | (a) aucune relecture, aucune ronde adverse — le `README` le dit : « rien ici n'est vérifié par un tiers » ; (b) le `/Title` du PDF perd son apostrophe, diagnostic fait au gabarit Pandoc, non corrigé depuis le 22 août [R] ; (c) la notice [19] « brouillée sur toute sa longueur » au PDF, mode mathématique sur `$` — constaté, non corrigé [D] ; (d) doublon [1] / [198], deux numéros pour un document, « déclaré et non résorbé » ; (e) les six auto-citations en tête de bibliographie — veille, revue, traité, compendium — sont « auto-publiées, non arbitrées » et forment le socle de la section 2.3 ; (f) la feuille de style des `.html` n'existe que dans un des deux rendus, aucun fichier ne la porte — le rendu HTML ne se refait pas depuis le dépôt ; (g) **trois PDF « -critique » et « -essai » sont entrés dans ce dossier au commit évalué** et aucun document ne les nomme — §8.2 |
| **Niveau** | **Très bien** — 80 % |
| **Publiabilité** | se donne publié ; l'évaluation le tient pour un rapport sectoriel de haut niveau, directement utile à une institution, dont la partie québécoise devrait être refaite sur les textes officiels avant toute diffusion hors de l'auteur |

### 5.9 Hors livrables — *Note de veille SDLC*

| Champ | |
|---|---|
| **Identité** | `3 - Veille/Note-veille-SDLC-agentique.md` ; **49 p.** [R] ; 26 011 jetons [R] ; 27 août 2026 ; source unique, transcription d'un entretien de 4 h 26 ; dix-huit thèses horodatées, quarante affirmations triangulées [L] |
| **Thèse** | « la rupture y est datée du 24 novembre 2025 et attribuée au harnais, non au modèle » ; recommandation : « séparer explicitement un régime de délégation forte […] d'un régime de délégation encadrée » (résumé) [L] |
| **Méthode déclarée** | lecture intégrale de la transcription, quatre marqueurs épistémiques — *confirmé, probable, hypothèse, à vérifier* [L] |
| **Lecture faite** | résumé, plan des dix-huit thèses [E] |
| **Rejeu** | `check-resume.py` ☑ 0 [R] ; aucun autre contrôle ne l'atteint — le `README` de `3 - Veille/` le dit |
| **Forces** | (1) une source unique traitée comme telle, avec ses cinq biais nommés et le rôle du contradicteur (§3) ; (2) le témoignage borné par son propre contre-exemple — la dérive architecturale sur base établie ; (3) horodatages de la transcription à chaque thèse |
| **Faiblesses** | (a) « la note déclare quatre marqueurs épistémiques et son tableau de triangulation en emploie six » — relevé par le `README`, non corrigé ; (b) bibliographie de trente entrées en puces « qu'aucun renvoi du corps n'apparie » ; (c) sa commande de rendu « se recopie à la main » et n'est pas au script ; (d) le rapport à la question du dossier est ténu — c'est une note de lecture, publiée dans le dossier d'un livrable |
| **Niveau** | **Satisfaisant** — 65 % |
| **Publiabilité** | se donne « document publié et non livrable » ; l'évaluation concorde |

### 5.10 Hors livrables — *Projection de l'état de ressource et délégation multicritère dans une plateforme HPC à processeurs quantiques*

| Champ | |
|---|---|
| **Identité** | `4 - Essais/2 - Article/` ; **38 p.** [R] ; 1 979 lignes de Typst, ~19 200 mots [D] ; v3 du 31 août 2026 ; **77 références**, 8 planches, 20 tableaux, 8 conditions de réfutation [R] |
| **Thèse** | « ce qui manque n'est pas une brique, c'est la chaîne entre elles » ; la *projection de l'état de ressource* comme objet de première classe daté et périssable ; « le travail est documentaire, et il le dit » [L] |
| **Méthode déclarée** | revue en deux strates, 42 sources ancrées affirmation par affirmation, 33 ajoutées par recherche systématique ; passe d'ancrage « dont la trace est publiée » ; « la plateforme n'est pas implémentée », « numériquement non calibrée » ; « le dispositif de qualité a été tenu par une seule personne » [L] |
| **Lecture faite** | résumé, introduction, contributions, §10.2, conclusion ; `rejeu-politique.py` en entier ; `.bib` partiel ; `README.md` entier [E] / [L] |
| **Rejeu** | `rejeu-politique.py` ☑ 0 [R] ; `check-article.py` ☑ 0 [R] ; harnais ☑ 7/7 [R] ; `typst compile` rend **752 159 o**, la taille exacte du PDF livré [R] ; trois références confrontées — @survey, @qihpc (« visionary » y est), et la mention du gabarit —, exactes [S] |
| **Forces** | (1) une prépublication de forme irréprochable : bibliographie close, parité de rendu vérifiée par script, renvois `§` résolus ; (2) huit conditions de réfutation « observables par un tiers », dont deux « exécutables immédiatement, sans matériel », et une qui a « subi — et passé — son premier test lors de la révision » ; (3) une implémentation de référence de 170 lignes qui rejoue les déroulés publiés et ferait échouer une assertion sur toute divergence ; (4) la phrase de méthode la plus juste du dossier : « un taux de couverture élevé mesure alors la cohérence interne d'un travail, non son adéquation à un besoin réel » ; (5) la conclusion : « non pas la certitude d'avoir raison, mais les moyens précis de démontrer qu'il a tort » |
| **Faiblesses** | (a) **hors sujet du dossier**, par décision des `README` et non du PRD ; il aurait sa place dans un dépôt propre, avec les « spécifications de chapitre, registres d'exigences et de décisions, journaux d'ancrage » que le colophon dit « disponibles auprès de l'auteur » et qui ne sont pas ici ; (b) le rejeu n'exerce que trente-cinq cases et demie sur trente-six : la transition (étalonnage, E2) n'implante que la branche conforme, et le commentaire du script le déclare — « RÉF-6 ne porte donc pas sur la requalification en échec » ; les `README` et `APPAREIL.md` écrivent « 36/36 » ; (c) le rejeu est un test de non-régression des exemples de l'auteur, pas une validation ; (d) `check-resume.py` sort 1 sur ce PDF pour un motif étranger au document, et le dépôt doit l'expliquer sur une page — un contrôle qui exige une page d'explication pour être ignoré n'est pas un contrôle ; (e) « tiré d'un mémoire technologique » dont rien n'est versionné : la traçabilité revendiquée s'arrête à la porte du dépôt |
| **Niveau** | **Très bien** — 80 % comme prépublication ; sans note au titre du dossier, dont il n'instruit pas la question |
| **Publiabilité** | se donne prépublication v3 ; l'évaluation la tient pour **soumissible** à un atelier ou une conférence d'ingénierie des systèmes HPC, avec la réserve que la validation est interne |

### 5.11 Le simulateur — `stigmergie-lab`

| Champ | |
|---|---|
| **Identité** | `4 - Essais/1 - Traité/crates/`, `bancs/` ; **30 488 lignes** de Rust dans `crates/` [R], 76 fichiers ; quatre *crates* en chaîne linéaire — `sim-core`, `sim-milieu`, `sim-agents`, `sim-viz` — et deux bancs ; **470 `#[test]`** [R] ; cible `x86_64-pc-windows-gnu` et `wasm32-unknown-unknown` [L] |
| **Thèse** | « tout chiffre affiché doit être retrouvé par la mesure, ou l'écart doit être consigné. Un écart est un défaut du simulateur ou une erreur du traité, et les deux méritent d'être trouvés » (NF-15, `README.md`) [L] |
| **Méthode déclarée** | six phases de PRD avec critères de sortie écrits en tests d'intégration ; déterminisme bit à bit — un fil, RNG semé, `HashMap` interdit par lint, transcendantes par `libm` ; parité natif / WASM mesurée par banc ; registre des décisions à trois provenances [M] / [C] / [R] [L] |
| **Lecture faite** | manifestes et lints en entier ; `docs/PRD.md` §0.0-0.1, `docs/decisions.md`, `audit.md` §1-2, `CLAUDE.md` en-tête [E] |
| **Rejeu** | `cargo test --workspace --release` : **470 réussis, 0 échec, 0 ignoré** ; `cargo clippy` : 0 ; `cargo fmt --check` : 0 [R] ; `check-empaquetage.py` sans cible : INDÉTERMINÉ comme déclaré [R] |
| **Forces** | (1) une discipline de déterminisme rare et **mesurée** : le banc DT1 a établi que six méthodes de `f64` divergent entre cibles et que `mul_add` change de verdict selon la machine de construction — d'où l'interdiction par `clippy.toml`, promue en `deny` au niveau du *workspace* ; (2) les cinq écarts consignés au registre, dont deux **contre le traité** — Φ_c ne sépare pas la conformité de la coordination ; le contrôleur d'élasticité contredit le §7.3 —, et le reclassement daté quand la troisième édition en absorbe deux ; (3) `hors_perimetre()` comme liste vivante affichée à l'écran : ce que le produit ne mesure pas est du code, pas de la prose ; (4) l'audit du 4 septembre, qui trouve un chemin chaud à optimiser bit pour bit et une incohérence documentaire — la rétention créditée d'un gain qu'elle ne produit pas — et l'applique en cinq phases ; (5) `#![deny(missing_docs)]` sur les quatre *crates*, `cargo doc` à 0 |
| **Faiblesses** | (a) **aucune intégration continue** : NF-13 et NF-16 nomment un mécanisme absent ; (b) la cible NF-05 est manquée d'un facteur 40 à 50 — 20 à 25 s simulées par seconde-cœur à n = 1 000 contre 10³ — et l'écart est structurel, Θ(n²) ; (c) seize exigences `EX-V*` sur vingt-trois ont un producteur et **aucun point d'appel** ; cinq mécanismes du milieu ne sont exécutés par aucun scénario ; quatre des cinq mécanismes du ch. 8 du traité « n'y sont appelés par aucun scénario » ; (d) la chaîne dépend du poste de l'auteur : `CARGO_TARGET_DIR` hors OneDrive exigé, chemin `mingw64` écrit en dur dans le `README` sous le profil utilisateur `agbru`, aucune licence propre au sous-projet (le `docs/README.md` l'écrit encore, périmé par la licence de la racine) ; (e) le `repository` du manifeste pointe `agbruneau/Stigmergie`, un dépôt qui n'est pas celui-ci [L] ; (f) les journaux des deux revues adversariales du code ont été retirés du dépôt — « rien n'y était exigé ni garanti », mais un jury lit les traces |
| **Niveau** | **Très bien** — 82 % |
| **Publiabilité** | sans objet ; badges au §10.3 |

## 6. Évaluation transversale

### C1 — Problématique, positionnement et unité du programme — 10

**Constats.** La question est une, énoncée en une phrase en tête du `README.md`, et les huit livrables la citent ou la déclinent [L]. Le positionnement — Canada-Québec, coopérative financière, triple tutelle AMF / BSIF / OCRI — est un créneau que l'état de l'art établit non couvert : « aucune source consultée n'établit de lien documenté entre un protocole d'agents et une exigence sectorielle canadienne » [E]. Le fil « découplage, contrat, évolution » du Vol. I, la thèse de l'autonomie encadrée du Vol. II et la fabrique de confiance du Vol. III s'enchaînent, et le Vol. III écrit d'où il vient : de deux verrous que les volumes précédents nomment et laissent hors périmètre [E]. Deux des dix documents publiés n'instruisent pas la question — l'article, par son objet ; la note, par sa source unique —, et le compte des livrables a changé trois fois sans décision d'auteur : le dépôt l'écrit [L]. Le programme s'est fait par accrétion — dix documents en 74 jours, quatorze réouvertures d'un dépôt « clos » — plutôt que par plan.

**Appréciation.** L'unité est réelle au niveau des thèses ; elle est fragile au niveau du dossier, où le critère d'appartenance est fixé après coup par les pages d'accueil. Un jury demanderait qui décide de ce qui est dans le dossier, et le dossier répond : « le compte se renverse d'un mot de sa part ».

**Niveau : Très bien, 80 % — 8,0 / 10.**

### C2 — État de l'art et maîtrise de la littérature — 10

**Constats.** Six bibliographies closes dans les deux sens et gardées par script — 342, 192, 312, 123, 77, et les 159 entrées du socle consolidé [R]. Les classiques du domaine sont lus à la source : Fischer-Lynch-Paterson, Gilbert-Lynch, Halpern-Moses, Chandy-Lamport, Alon-Matias-Szegedy, Flajolet, Axelsson dans le traité [E] ; Austin, Searle, Finin, FIPA, Singh dans le Vol. I [E] ; RFC 6749, 7591, 8693, 8615, 9901 dans les Vol. I et III [E]. Neuf références confrontées à la source sur neuf atteintes sont exactes au fait précis que la pièce leur prête [S]. La revue mesure le régime d'arbitrage de son propre corpus et le borne par contre-épreuve [E]. Réserves : la matière repose sur des prépublications et des spécifications vivantes, et le dossier le date à chaque occurrence ; la revue interroge une seule base ; trois entrées de la bibliographie du ch. 3 du Vol. I sont « non re-vérifiées en adverse » [E] ; le ch. 8 du traité repose sur une source unique postérieure ; l'auto-citation est massive — six entrées en tête de l'état de l'art, toutes « auto-publiées, non arbitrées » [E].

**Appréciation.** La maîtrise de la littérature est celle d'un spécialiste ; la connaissance de son statut — arbitré, prépublié, vivant — est meilleure que dans la plupart des travaux arbitrés du champ. Ce qui manque est ce qu'aucune passe ne peut fournir : une littérature établie sur un objet qui a trois ans.

**Niveau : Très bien, 85 % — 8,5 / 10.**

### C3 — Méthodologie et régime de preuve — 15

**Constats.** Les niveaux **[A]** / **[B]** / **[C]** sont définis, appliqués et portés « à la première mobilisation de chaque entrée » [E] ; les trois degrés d'absence séparent *fait négatif vérifié*, *fait négatif établi* et *absence de documentation* [E] ; 485 marqueurs « Lecture de l'auteur » séparent glose et socle dans les Vol. II et III [R] ; la règle NF-15 fait du simulateur un instrument de réfutation du traité, et cinq écarts sont consignés [L] ; l'article énonce huit conditions de réfutation, dont une exécutable par script [R] ; le protocole de revalidation du ch. 50 a été éprouvé sur un événement survenu [E] ; les limites sont écrites avant les résultats dans la revue, l'état de l'art et l'article [E]. Ce qui retient : le niveau **[A]** est un « vote adversarial à trois juges » rendus par des instances d'un modèle de langage, placé **au-dessus** de la lecture directe d'une source primaire par l'auteur — l'annexe A du Vol. II le justifie, et la justification ne tient pas devant un jury, parce que trois lectures d'un même modèle ne sont pas trois observateurs ; la boucle traité ↔ simulateur ↔ PRD ↔ revue ↔ état de l'art est fermée sur un auteur et ses instances ; le seul « arbitrage externe » du dossier — `eval.html`, 30 juillet 2026 — est produit par un modèle, et le dépôt lui dénie toute autorité ; CA-IV-11 et CA-IV-13 — relecture par un tiers — sont « dérogés, non satisfaits » pour la totalité du compendium, et la « distinction rédacteur / relecteur n'est pas constatable sur disque » au Vol. III [L]. **La présente évaluation ne change rien à cela : elle est une instance de plus.**

**Appréciation.** La méthode est explicite, appliquée avec constance et retournée contre le dossier lui-même — c'est ce qu'un jury attend, et il le trouve rarement. Elle a une seule faiblesse, et elle est structurelle : personne d'extérieur n'est entré dans la boucle. La hiérarchie **[A]** > **[B]** est le symptôme le plus visible de cette fermeture.

**Niveau : Très bien, 80 % — 12,0 / 15.**

### C4 — Qualité, vérification et traçabilité des sources — 10

**Constats.** Neuf sur neuf exactes à la source [S] ; appariement cité ↔ défini gardé par cinq scripts [R] ; les notices portent identifiant, version, date de révision et statut d'arbitrage [E] ; les sources vivantes portent ⚠ et leur date de consultation [E] ; le retrait d'une source [310] est rapporté comme fait plutôt que dissimulé [E] ; les œuvres de tiers ont quitté l'index avant que la licence ne les couvre [L]. Réserves : la couche québécoise de trois documents repose sur une extraction tierce non reproductible [E] ; le doublon [1] / [198] et la notice [19] brouillée de l'état de l'art [D] ; le Vol. I n'a aucun contrôle propre [L] ; le `/Title` d'un PDF est mutilé [R] ; les auto-citations forment une part du socle de la section 2.3 de l'état de l'art [E].

**Appréciation.** La traçabilité des sources est exemplaire là où elle est outillée, et déclarée là où elle ne l'est pas. Aucun signe de référence fabriquée ou déformée.

**Niveau : Très bien, 85 % — 8,5 / 10.**

### C5 — Résultats, contribution et originalité — 15

**Constats.** Contributions identifiables et défendables : (1) la grille des cinq questions et le résultat qu'aucun des onze mécanismes relevés n'en remplit trois [E] ; (2) le fait négatif vérifié sur E-23 et la matrice vide des quinze croisements [E] ; (3) le traité — treize algorithmes portant chacun modèle de panne, synchronisme, coût et condition de validité, une frontière à deux axes, six restes nommés [E] ; (4) la transposition exécutable comme méthode de réfutation d'un traité — cinq écarts, deux retournés contre la source [L] ; (5) le déplacement de la question sectorielle du protocole au régime juridique de l'appelant [E] ; (6) la projection de l'état de ressource et sa machine d'états totale, hors sujet mais réelle [E] ; (7) le modèle de maturité en six paliers de `NiveauMaturité.html` [E]. Ce qui limite : **aucune contribution n'a été soumise à un arbitrage humain** ; l'autonomie encadrée est déclarée empruntée, l'apport étant son transport au Canada « comme un raisonnement, non comme une déduction » [L] ; le compendium est une somme, non une matière neuve, et il se déclare brouillon ; **aucune donnée de terrain** — « aucune source consultée n'établit qu'une coopérative financière canadienne exploite aujourd'hui un système multi-agents en production sur un processus régi » [E] ; le seul code exécutable mesure un monde clos, « aucun modèle de langage appelé » [L] ; le résultat le plus cité du traité « reste une illustration arithmétique » [L] ; la seule campagne empirique mobilisée sur des agents de langage est d'un tiers, non arbitrée, et sur ses propres modèles [S].

**Appréciation.** Le dossier raisonne sur des spécifications, des textes et des modèles ; il n'observe aucun système. Ses contributions sont des instruments — grilles, matrices, transpositions, conditions de réfutation — plus que des résultats, et des instruments non éprouvés hors de la main qui les a faits. C'est le critère où l'écart entre l'ambition et l'établi est le plus grand.

**Niveau : Satisfaisant, 70 % — 10,5 / 15.**

### C6 — Artefacts, reproductibilité et appareil de vérification — 15

**Constats.** Rejoué avec le même verdict que l'auteur : 470 tests, clippy 0, rustfmt 0, cinq contrôles de document à 0, quatre harnais de mutation intacts, la recomposition de l'article à l'octet, la parité du traité hors horodatage, les pages des onze PDF au chiffre du `README` [R]. Rejoué avec un verdict **différent** : `genere.py --verifier` sort 1 — trois empreintes gelées ne correspondent pas aux fichiers, pour une cause établie au §8.1 [R] ; la chaîne plante sans `PYTHONUTF8` [R] ; les graveurs et assembleurs écrivent en CRLF sous Windows, et « identique à l'octet » n'est vrai qu'après normalisation [R] ; huit renvois morts, dont cinq nés du commit évalué [R]. Non rejoué : sept chaînes Pandoc, la construction WASM, les bancs. Dépendances au poste : `CARGO_TARGET_DIR`, `mingw64` sous un profil nommé, polices, versions épinglées [L]. Aucune intégration continue [L]. 76 Mo de PDF versionnés sans LFS [R]. La feuille de style des `.html` de la recension n'est pas versionnée [L].

**Appréciation.** L'appareil est d'un niveau que peu de dépôts de recherche atteignent, et il a une faiblesse propre aux appareils que personne d'autre n'exécute : il valide ce que la machine de l'auteur produit. Le premier tiers qui l'a rejoué sur un arbre normalisé a trouvé un contrôle en échec. La leçon est celle que le dépôt écrit lui-même à propos d'un autre contrôle : « une ancre qui vise ce que le contrôle ne regarde pas cesse de tester sans que rien le signale ».

**Niveau : Très bien, 80 % — 12,0 / 15.**

### C7 — Structure, cohérence et économie du corpus — 10

**Constats.** La carte du dépôt et la table « par où entrer, selon le temps qu'on a » sont de bonnes pratiques [L] ; la réorganisation du 5 septembre a simplifié l'arbre [L]. Mais : **3,10 millions de jetons** de Markdown versionné pour 479 387 mots de matière source [R] — la même matière existe en pièces, en `Monographie.md` assemblé, en compendium `.md`, en compendium `.html`, et se reprend sous trois angles dans la veille, la revue et l'état de l'art ; un lecteur rencontre MCP, A2A, E-23 et l'article 12.1 quatre à cinq fois. Les numérotations se croisent — huit documents I à VIII, cinq dossiers 1 à 5, « Vol. IV » pour le compendium, « Vol. V » pour un traité rangé sous `4 - Essais/` [L]. Le plus gros livrable est un brouillon déclaré. Les en-têtes de chapitre du compendium pèsent 7 à 11 Ko avant le corps [R]. La chronique des réouvertures occupe la tête de quatre `README` et se corrige elle-même : « ce paragraphe a écrit […] et c'était faux » revient dans presque chaque page d'accueil [L]. Deux documents hors livrables vivent dans les dossiers des livrables [L].

**Appréciation.** Le dossier n'a pas d'économie : il additionne sans jamais soustraire, et la règle « une phrase datée garde son fait » — défendable pour un registre — est appliquée aux pages d'accueil, qui deviennent des registres. Le lecteur paie le prix de la traçabilité de l'auteur.

**Niveau : Satisfaisant, 60 % — 6,0 / 10.**

### C8 — Rédaction et communication scientifique — 10

**Constats.** Deux registres. Le **corps doctrinal** est écrit dans un français précis et dense : le traité compose 0,5 % de ses signes en gras [R] et se lit comme un cours de cycles supérieurs ; l'avant-propos et le ch. 13 du Vol. II, le ch. 4 du Vol. III, la conclusion de l'état de l'art tiennent l'argument sur la longueur [E]. L'**appareil** est illisible par saturation : 24 à 38 % de signes en gras dans les `README` de Livre, 32,5 % dans le PRD du compendium, 21,2 % dans l'assemblage du Vol. III [R] ; 686 ⚠ dans le TOC du compendium, 334 dans son PRD, 145 dans le `README` de la veille [R] ; des phrases de six lignes, une négation systématique — « ce que X n'est pas » —, des tirets cadratins par milliers [R]. Le dossier le sait : le gabarit de rendu **mesure** la densité de gras et rend au romain ce qui dépasse quatorze cadratins — « à ces densités le gras ne signale plus, il tache » [L]. Aucun résumé en anglais ; aucun DOI ; l'étiquette `mono-v1.0` ne marque pas l'état clos [R].

**Appréciation.** Le dossier contient un très bon livre, deux bons volumes et trois rapports utiles, enveloppés dans un appareil qui les cache. Un jury lit d'abord les pages d'accueil ; ici, elles sont l'endroit du dossier le plus difficile à lire.

**Niveau : Satisfaisant, 60 % — 6,0 / 10.**

### C9 — Intégrité intellectuelle, attribution et gouvernance — 5

**Constats.** Décisions d'auteur numérotées, datées, motivées, avec condition de réouverture — D-1 à D-16 au compendium, DT1 à DT14 au simulateur [E] ; licence CC BY 4.0 posée et œuvres de tiers sorties avant qu'elle ne les couvre [L] ; assistance par agents déclarée — avertissement du `README` de `1 - Collection/`, annexes de méthode, pipeline « Claude, Anthropic » nommé dans la veille [E] ; `git log` signe `Claude` sur vingt commits qui rédigent les onze chapitres du Livre I du compendium et le rapport d'état de l'art [R] ; le `README` de la racine écrit « les textes sont d'une seule main » [L]. Trois rapports `audit.md`, deux journaux de boucle et l'évaluation du 5 septembre ont été **supprimés** du dépôt, leurs constats « portés ailleurs » [R]. Le dernier commit supprime une évaluation que le `README` continue d'annoncer à 78 / 100 [R].

**Appréciation.** La responsabilité éditoriale est bien d'une seule main ; la rédaction ne l'est pas, et la phrase du `README` doit le dire. La suppression des pièces d'audit est cohérente avec une règle du dépôt — ce qu'elles ont produit de durable est au PRD et aux registres —, mais un jury lit les traces, pas seulement les conclusions, et une trace supprimée est une trace qu'il ne peut plus lire.

**Niveau : Très bien, 80 % — 4,0 / 5.**

## 7. Tableau de notation

| # | Critère | Poids | Niveau | Part | Score |
|---|---|---|---|---|---|
| C1 | Problématique, positionnement, unité | 10 | Très bien | 80 % | 8,0 |
| C2 | État de l'art et littérature | 10 | Très bien | 85 % | 8,5 |
| C3 | Méthodologie et régime de preuve | 15 | Très bien | 80 % | 12,0 |
| C4 | Sources : qualité, vérification, traçabilité | 10 | Très bien | 85 % | 8,5 |
| C5 | Résultats, contribution, originalité | 15 | Satisfaisant | 70 % | 10,5 |
| C6 | Artefacts, reproductibilité, appareil | 15 | Très bien | 80 % | 12,0 |
| C7 | Structure, cohérence, économie | 10 | Satisfaisant | 60 % | 6,0 |
| C8 | Rédaction et communication | 10 | Satisfaisant | 60 % | 6,0 |
| C9 | Intégrité, attribution, gouvernance | 5 | Très bien | 80 % | 4,0 |
| | **Total** | **100** | | | **75,5** |

Par pièce : Vol. I 78 %, Vol. II 85 %, Vol. III 72 %, Vol. IV 55 %, Vol. V 86 %, Vol. VI 80 %, Vol. VII 78 %, Vol. VIII 80 %, note 65 %, article 80 % (hors dossier), simulateur 82 %.

## 8. Constats neufs sur l'appareil

Ce que le rejeu a trouvé et que le dépôt n'écrit pas.

### 8.1 `genere.py --verifier` sort 1 sur l'arbre normalisé, et la cause est établie

Le registre `ANTERIEURES` de `2 - Compendium/figures/genere.py` gèle trois figures que le programme ne regrave pas à une empreinte SHA-256 [L]. Sur l'arbre évalué, les trois empreintes calculées ne correspondent pas aux trois attendues, et le contrôle sort 1 [R]. Les fichiers n'ont pas bougé depuis le 31 juillet 2026, le registre a été écrit le 21 août [R]. **La cause :** les trois empreintes attendues sont exactement celles du contenu des fichiers **avec fins de ligne CRLF** — `sed 's/$/\r/' | sha256sum` rend `e82d87c7412a…`, `7bc70d30bcee…`, `6b51f826a50b…`, les trois valeurs du registre [R]. Le 21 août, le disque de l'auteur portait ces fichiers en CRLF, `core.autocrlf=true` étant son réglage ; la règle `* text=auto eol=lf` posée le même jour dans `.gitattributes` normalise l'arbre en LF ; le registre a gelé les octets d'avant la règle. Le contrôle valait 0 ce jour-là et vaut 1 sur tout arbre conforme à `.gitattributes`, dont un clone. Personne ne l'a vu depuis : `APPAREIL.md` porte le ☑ 0 du 21 août, et l'évaluation du 5 septembre s'est arrêtée au plantage `UnicodeEncodeError` que la console cp1252 provoque sur le premier ⚠ — plantage que ce rejeu reproduit [R]. **Condition bloquante B3 remplie.**

### 8.2 Le commit évalué a cassé cinq renvois et versionné trois fichiers que rien ne décrit

`79ecdcf` supprime `Évaluation académique.md`, son `.html` et `gauntlet-log.md`, et **ajoute** trois PDF sous `5 - Recension/` : `Cinq schémas […]-critique.pdf`, `Cinq schémas […]-essai.pdf` (221 816 o chacun, la taille du PDF livré) et `État de l'art […]-critique.pdf` (2 065 255 o, contre 2 065 064 pour le PDF livré) [R]. Aucun `README` ne les nomme [R]. Le journal supprimé les explique : ils sont les sorties d'une boucle bâtisseur / critique conduite le 5 septembre sur la mise à jour de la documentation, dont le critique a rejeté le premier tour pour avoir « falsifié un relevé daté » en réécrivant le chemin d'une expérience du 21 août [L, historique]. Le `README` de la racine et `APPAREIL.md` renvoient encore **cinq fois** à l'évaluation supprimée, et la table « Par où entrer » en fait sa deuxième ligne, à « 78 / 100 » [R]. Par le critère de clôture que le dépôt s'est donné — « dernier jour où une pièce est entrée au dépôt » —, ces trois PDF portent la clôture au 5 septembre, ce que la page dit d'ailleurs pour d'autres pièces qui n'y sont plus.

### 8.3 « Identique à l'octet » s'entend après normalisation

`figures/contenu.py` du traité et les deux `build/assemble.py` écrivent leurs sorties en mode texte Python, donc en CRLF sous Windows ; `git diff` montre 19 SVG et deux `Monographie.md` modifiés, `git diff --ignore-cr-at-eol` ne montre rien, et git avertit que « CRLF will be replaced by LF » [R]. La reproductibilité à l'octet que `APPAREIL.md` affirme est vraie du contenu indexé, non des fichiers produits ; un tiers qui compare avec `cmp` sur Windows voit vingt et un fichiers différents. `figures/dessine.py` de la recension n'a pas ce défaut [R]. Le correctif est d'une ligne par script — `open(…, "w", newline="\n")`.

### 8.4 `APPAREIL.md` est en retard sur ses propres contrôles, et le dit à moitié

Cinq écarts entre la page et la mesure : P1-P8 et 3 rapports déclaratifs contre **P1-P10 et 5** ; C1-C15 contre **C1-C16** ; 108 mutations contre **114** ; 17 contre **23** ; 467 tests contre **470** [R]. La page reconnaît trois de ces cinq écarts en citant l'évaluation du 5 septembre — et cite pour cela un fichier que le commit suivant a supprimé.

### 8.5 Le résumé du compendium est à 1,7 pt d'être rogné

`check-resume.py` sort 0 sur `Compendium.pdf` avec le message « LIMITE : 1,7 pt de dégagement seulement. Toute reprise du résumé le fera déborder » [R]. Le risque que ce contrôle existe pour attraper — un résumé rogné sans que Pandoc ni Typst le signalent — est à un mot de se produire sur le plus gros livrable, et aucune page du dépôt ne porte cette alerte.

### 8.6 Le rejeu de l'article exerce trente-cinq cases et demie sur trente-six

`rejeu-politique.py` vérifie que la table de transitions est **totale** — trente-six cases renseignées — et c'est exact [R]. Mais la case (étalonnage, E2) n'implante que la branche « → D si conforme » et aucune assertion n'exerce « sinon → G » ; le script le déclare en commentaire, « relevé par l'audit du 2 septembre 2026 ; à lever » [L]. Les `README` et `APPAREIL.md` écrivent « 36/36 » sans cette réserve.

### 8.7 Constats mineurs

- Le manifeste du simulateur déclare `repository = "https://github.com/agbruneau/Stigmergie"`, un autre dépôt [L].
- `docs/README.md` du traité écrit qu'« aucune licence n'est déclarée à ce jour », phrase périmée depuis le 21 août [L].
- Le `README` du simulateur écrit un chemin `mingw64` sous `C:\Users\agbru\…` — un prérequis lié au poste, présenté comme commande [L].
- `Monographie.pdf` du Vol. I porte `Creator: Typst 0.15.0`, les onze autres PDF 0.15.1 : sa chaîne n'a pas été rejouée depuis la montée de version [R].
- `1 - Collection/README.md` mentionne l'évaluation supprimée une fois [R].
- Trois renvois vers `2 - Compendium/audit.md` restent morts dans `PRD.md` et `TOC.md`, ce que `APPAREIL.md` relève et laisse [R].

## 9. Critiques de fond

1. **La boucle est fermée, et le dossier a inversé l'ordre des preuves pour la fermer.** Traité, simulateur, PRD, veille, revue, état de l'art et compendium se citent mutuellement, sont d'une même main, et ont été vérifiés par des instances d'un même modèle. Le niveau **[A]** — trois juges de modèle qui échouent à réfuter — est placé au-dessus de **[B]** — l'auteur lit le texte officiel. Pour un jury, c'est l'inverse qui vaut, et c'est le seul point où la méthode du dossier est **fausse** plutôt qu'incomplète. Reclasser **[A]** en « vérifié par instances » et réserver le niveau le plus élevé à une relecture humaine nommée rétablirait l'ordre. La présente évaluation, produite par un modèle, n'apporte pas ce que le dossier n'a pas.

2. **Le compendium contredit le dossier qu'il résume.** Mille pages qui se déclarent cinquante fois brouillon, sept annexes qui « ne seront pas écrites », 524 renvois nus qu'une décision refuse de ré-adosser — et le volume compte parmi les huit. Soit il est une archive de travail et sort du compte ; soit il est un livrable et se termine. La cible de mille pages exactement, vérifiée au *build*, mesure l'un des rares chiffres du dépôt qui n'a aucune signification.

3. **L'appareil a recouvert le corps.** Le dossier consacre à ses octets, cardinaux, horodatages et fins de ligne une rigueur que son objet — un essaim réel, une flotte d'agents, un processus régi en production — n'a jamais reçue. Le traité le dit de lui-même : « ce que le livre laisse ouvert n'est donc pas une théorie manquante mais une métrologie manquante ». Elle manque toujours, et les 3,1 millions de jetons de Markdown ne la remplacent pas.

4. **Aucun système n'est observé.** Le dossier raisonne sur des spécifications, des textes normatifs et un simulateur de monde clos qui n'appelle aucun modèle de langage. La seule campagne empirique sur des agents de langage qu'il mobilise est d'un tiers, sans arbitrage, sur ses propres modèles. L'état de l'art le déclare : aucune source n'établit qu'une coopérative canadienne exploite un système multi-agents sur un processus régi. Le dossier ne sait donc pas si l'objet qu'il décrit existe.

5. **La traçabilité par suppression.** Trois `audit.md`, deux journaux de boucle, l'évaluation du 5 septembre, un démonstrateur, un article de synthèse : le dépôt retire les pièces et garde leurs conclusions dans des registres. La règle est cohérente ; son effet est qu'un jury ne peut plus lire comment une conclusion a été atteinte, et que des renvois du corps visent le vide. Un dépôt qui atteste des octets ne devrait pas retirer les pièces qui les ont produits.

6. **La péremption court plus vite que la revalidation.** Les gels vont de juin à septembre 2026 sur un champ qui « se périme par trimestres » ; le protocole du ch. 50 existe et a été éprouvé une fois ; aucune cadence n'est fixée, et le dépôt est « clos ». Dans six mois, une part des faits du Vol. I sera fausse sans qu'aucun contrôle le dise.

## 10. Verdict, conditions, badges

### 10.1 Conditions bloquantes

| | État | Constat |
|---|---|---|
| **B1** — relecteur humain | **remplie** | aucun relecteur humain nommé sur aucune pièce ; CA-IV-11 et CA-IV-13 dérogés ; « la distinction rédacteur / relecteur n'est pas constatable sur disque » [L] |
| **B2** — livrable non publiable | **remplie** | les cinquante pièces du Vol. IV se déclarent « Brouillon de rédaction, non publiable » ; le Vol. III se déclare « rédigé non publiable » ; tous deux comptent parmi les huit [R] |
| **B3** — contrôle en échec non documenté | **remplie** | `genere.py --verifier` sort 1 sur l'arbre normalisé ; `APPAREIL.md` écrit ☑ 0 [R] |
| **B4** — attribution par pièce | **partiellement** | assistance déclarée globalement ; aucune déclaration de contribution par pièce ; « les textes sont d'une seule main » contredit par vingt commits signés `Claude` [R] |

### 10.2 Verdict

**Corrections majeures requises, avec nouvelle évaluation.** Le total de 75,5 placerait le dossier en corrections mineures ; trois conditions bloquantes le plafonnent. Aucune ne demande de réécrire une pièce : elles demandent un lecteur, une décision et deux correctifs.

### 10.3 Badges

| Artefact | Disponible | Fonctionnel | Réutilisable | Résultats reproduits |
|---|---|---|---|---|
| Simulateur `stigmergie-lab` | ☑ dépôt public, CC BY 4.0 ; ⚠ aucun DOI, aucune étiquette propre | ☑ 470 tests, clippy 0, fmt 0 [R] | ◐ documentation excellente ; prérequis liés au poste — `CARGO_TARGET_DIR`, `mingw64` sous profil nommé, cible `windows-gnu` épinglée | ◐ tests et lints reproduits ; tailles WASM, bancs et NF-05 non re-mesurés ici |
| Chaînes documentaires | ☑ | ◐ cinq contrôles, quatre harnais, Typst et assemblages rejoués ; sept chaînes Pandoc non rejouées | ◐ sensibles aux fins de ligne et à l'encodage de console ; feuille de style non versionnée | ◐ pages et tailles retrouvées ; trois empreintes gelées en défaut |

## 11. Corrections requises, bonifications, projets futurs

### 11.1 Corrections requises

| # | Correction | Ce qu'elle lève |
|---|---|---|
| R1 | Faire lire le traité (Vol. V) et les ch. 9 à 13 du Vol. II par **deux relecteurs humains nommés** — un spécialiste des systèmes répartis, un juriste du droit financier canadien —, et verser leurs rapports au dépôt | **B1** ; ouvre la boucle ; seule action qui change le statut « non arbitré » |
| R2 | Trancher le Vol. IV : le sortir du compte des livrables comme archive de travail, ou le porter à l'état publiable — ré-adossement des 524 renvois aux `S-nnn`, relecture des cinquante pièces ; dire de même pour le Vol. III | **B2** ; rend le compte des livrables et l'état des pièces cohérents |
| R3 | Réancrer les trois empreintes `ANTERIEURES` sur les octets LF, ou hacher après normalisation des fins de ligne ; ajouter `sys.stdout.reconfigure(encoding="utf-8")` à `genere.py` ; écrire `newline="\n"` dans `contenu.py` et les deux `assemble.py` ; rejouer `APPAREIL.md` | **B3** ; « identique à l'octet » redevient vrai sur tout poste |
| R4 | Une **déclaration de contribution par pièce** — auteur, agents de modèle et leur rôle, relecteurs, outils — au modèle CRediT adapté ; corriger « d'une seule main » en « d'une seule responsabilité » | **B4** |
| R5 | Réparer le commit `79ecdcf` : les cinq renvois vers l'évaluation supprimée, la ligne « 78 / 100 » de la table d'entrée, les trois PDF « -critique / -essai » — les documenter ou les retirer —, et redater la clôture si le critère du dépôt l'exige | cohérence de l'arbre évalué ; les mesures du §8.2 |

### 11.2 Bonifications, par rendement

1. **Intégration continue** — `cargo test / clippy / fmt`, les cinq contrôles de document, les quatre harnais, un résolveur de renvois Markdown et un contrôle de fins de ligne, sur Linux et Windows : NF-13 et NF-16 tenues, et le §8.1 ne se reproduit plus.
2. **Réécrire les pages d'accueil** : quarante lignes par dossier, la chronique datée dans un `JOURNAL.md`, les ⚠ et le gras hors de la prose d'accueil ; ramener chaque en-tête de chapitre du compendium à un tableau de cinq lignes, le reste en note de fin — c'est ce qu'un lecteur voit en premier.
3. **Fusionner** veille, revue et état de l'art en un document à trois parties, ou publier une note de synthèse de vingt pages qui les remplace pour le lecteur pressé : la redondance divisée par trois.
4. **Citabilité** : résumés en anglais, DOI Zenodo sur un état étiqueté `corpus-v1.0`, Git LFS pour les 76 Mo de PDF.
5. **Corrections locales** : post-traiter le `/Title` de l'état de l'art ; échapper les `$` de la notice [19] ; résorber le doublon [1] / [198] ; versionner la feuille de style ; un contrôle propre au Vol. I ; condenser le résumé du compendium de deux lignes.
6. **Traité** : donner en annexe le protocole de mesure de σ et κ sur un journal réel ; brancher les quatre mécanismes du ch. 8 dans un scénario ou les retirer du code livré.
7. **Article** : donner au rejeu un verdict d'étalonnage en entrée pour exercer « sinon → G » ; sortir l'article dans un dépôt propre, avec les artefacts du mémoire que le colophon annonce.
8. **Séparer l'appareil du corpus** — deux dépôts, ou un dossier `appareil/` — pour que le lecteur du corpus ne voie pas les octets.

### 11.3 Projets futurs

Chacun part d'un reste que le dossier nomme.

1. **Mesurer le débit d'un essaim réel** sur un journal Kafka instrumenté, cinquante à mille agents, et retrouver σ et κ — premier reste du traité, celui que le simulateur « ne peut pas remplacer ».
2. **Mesurer la corrélation des fautes d'une flotte** multi-modèles et multi-fournisseurs, hypothèse pré-enregistrée, en étendant le φ = 0,916 de [121] — troisième reste du traité.
3. **Décomposer Φ_c** par un modèle nul à trace mélangée qui sépare la corrélation du milieu de celle de la décision — l'écart le plus fécond des cinq (DT14).
4. **Démontrer la borne spectrale du graphe biparti agents / partitions** — quatrième reste, le seul purement théorique, publiable seul.
5. **Prototyper une chaîne de mandat opposable** — carte d'agent signée, `act` de RFC 8693, mandats SD-JWT, révocation — et l'éprouver contre E-23, la Loi 25 et la *Loi sur la preuve* avec un juriste : la question Q-C du Vol. III et le §7.8 de l'état de l'art.
6. **Une étude empirique** auprès de dix à quinze institutions financières canadiennes, entretiens semi-dirigés, pour établir ce qu'aucune source ne documente : l'existence de systèmes multi-agents en production sur un processus régi.
7. **Un article court** — douze pages, AAMAS, DEBS ou Middleware — sur la transposition exécutable comme méthode de réfutation d'un traité : la contribution méthodologique la plus originale du dossier tient en un article.
8. **Un banc de conformité E-23 pour systèmes agentiques** — l'inventaire énumérable avant exécution que le ch. 13 du Vol. II déduit —, livré comme outil ouvert avant le 1er mai 2027.
9. **La revalidation semestrielle automatisée** du socle `S-nnn` selon le ch. 50, avec rapport de péremption généré : l'outil existe, la cadence manque.
10. **La réplication indépendante de l'appareil** sur Linux et macOS, par un tiers : le §8.1 et le §8.3 montrent que le dépôt n'a été exécuté que sur le poste qui l'a produit.

## 12. Déclaration de l'évaluateur

Cette évaluation est produite par **Claude Fable 5.1**, modèle de langage d'Anthropic, exécuté comme agent Claude Code sur le poste de l'auteur, à sa demande, le 15 septembre 2026, sur le commit `79ecdcf`. Elle a lu ce que le §3.1 nomme, rejoué ce que le §3.2 nomme, consulté ce que l'annexe B nomme, et rien d'autre : les 3 009 pages n'ont pas été lues en entier, et les fiches disent ce qui l'a été.

**Ce qu'elle n'est pas.** Ni un jury institutionnel, ni un arbitrage de revue, ni la relecture humaine que la condition B1 exige — elle est une instance de plus du dispositif que le dossier emploie déjà, et son verdict sur B1 s'applique à elle-même. Elle n'a pas d'indépendance vis-à-vis de l'auteur, qui l'a commandée et sur la machine duquel elle a tourné ; elle a en revanche accès à tout l'arbre, à l'historique, et à la possibilité d'exécuter, ce qu'un jury humain n'a pas d'ordinaire.

**Conflits.** Le modèle qui évalue est de la même famille que celui dont les commits signent vingt entrées de l'historique et dont les pipelines ont produit les socles. L'évaluation a été conduite sans lire ces pipelines et en rejouant l'appareil au lieu de le croire ; elle ne peut exclure un biais de familiarité avec la forme des textes.

**Limites.** Sept chaînes de rendu PDF, la construction WASM et les bancs n'ont pas été rejoués. Une référence sur dix n'a pas été atteinte, par une adresse de l'évaluateur. Les niveaux et les parts du §6 sont des jugements ; les constats qui les fondent sont marqués et vérifiables.

---

## Annexe A — Commandes exécutées et sorties abrégées

Toutes depuis le dossier indiqué, le 15 septembre 2026, `PYTHONUTF8=1` sauf mention.

```
[3 - Veille]        python Python/check-veille.py            -> 0 ; 94 sections, 24 tableaux, 25 QO ; 342/342
[3 - Veille]        python Python/check-revue.py             -> 0 ; 192 ; 12 / 32 / 145 sur 189 arXiv
[4 - Essais/1]      python Python/check-traite.py            -> 0 ; 143 p., 72 511 mots, 19 fig., 123/123, parité 1 551 326 o
[4 - Essais/1]      python Python/check-empaquetage.py       -> 1 INDÉTERMINÉ (CARGO_TARGET_DIR absent), comme déclaré
[4 - Essais/1]      python figures/contenu.py                -> 19 SVG ; git diff : 19 M ; --ignore-cr-at-eol : vide
[4 - Essais/1]      cargo test --workspace --release         -> 470 passed, 0 failed, 0 ignored
[4 - Essais/1]      cargo clippy --workspace --all-targets --release -> 0
[4 - Essais/1]      cargo fmt --all --check                  -> 0 ligne
[4 - Essais/2]      python rejeu-politique.py                -> 0 ; « table de transitions (36/36) … RÉF-6 non déclenchée »
[4 - Essais/2]      python check-article.py                  -> 0 ; 77/77 ; parité 751 989 o ; 165 renvois ; 10 cardinaux ; 8 scores
[4 - Essais/2]      python check-article-mutations.py        -> 0 ; 7 mutations vues
[4 - Essais/2]      typst compile article-hpc-qpu.typ <hors dépôt> -> 752 159 o (livré : 752 159 o)
[2 - Compendium]    python PRD/check-compendium.py           -> 0 ; 50 pièces (P1-P10), 5 rapports déclaratifs
[2 - Compendium]    python PRD/check-toc.py                  -> 0 ; C1-C16
[2 - Compendium]    python PRD/check-sieges.py               -> 0 ; 26 sièges (S1-S5)
[2 - Compendium]    bash PRD/decompte.sh --verifier          -> 0 ; 93 239 / 160 890 ; agrégat 479 387
[2 - Compendium]    python build/verifier-piece.py           -> 0 ; 50 .html conformes
[2 - Compendium]    python figures/genere.py --verifier      -> 1 ; « 3 défaut(s) aux figures antérieures »
                    idem sans PYTHONUTF8                     -> UnicodeEncodeError: 'charmap' codec … '\u26a0'
                    sed 's/$/\r/' figures/<f>.svg | sha256sum -> e82d87c7412a… / 7bc70d30bcee… / 6b51f826a50b… (= registre)
[2 - Compendium]    python PRD/check-sieges-mutations.py     -> 0 ; 114 mutations attrapées
[2 - Compendium]    python PRD/check-toc-mutations.py        -> 0 ; toutes détectées (M16b -> C16)
[2 - Compendium]    python PRD/check-compendium-mutations.py -> 0 ; 23 mutations vues
[1 - Collection/2]  python build/assemble.py                 -> 38 blocs, 853 Ko ; diff CRLF seul
[1 - Collection/3]  python build/assemble.py                 -> 34 pièces, 1 097 Ko ; diff CRLF seul
[5 - Recension]     python figures/dessine.py                -> 5 SVG ; git diff : vide
[racine]            check-resume.py sur 11 PDF               -> 0 ×10 ; article 1 (documenté) ; Compendium « LIMITE 1,7 pt »
[racine]            pymupdf : pages                          -> 569 387 427 1000 143 144 59 186 7 | 49 38 | 146 | 7 7 186
[racine]            résolution des renvois (219 .md)         -> 1 996 relatifs, 8 morts (3 audit.md, 5 Évaluation académique)
[racine]            git log --format=%an | sort | uniq -c    -> 304 André-Guy Bruneau, 20 Claude, 2 agbruneau ; 326 commits
[racine]            git ls-files | wc -l ; somme des blobs   -> 585 ; 79 469 238 o
```

L'arbre a été remis dans son état d'ouverture après les rejeux qui écrivent (`git checkout --` sur les fichiers régénérés) ; `git status` est vide hors les deux fichiers de cette évaluation.

## Annexe B — Références confrontées à leur source

Consultées le 15 septembre 2026.

| Pièce | Référence | Source consultée | Verdict |
|---|---|---|---|
| Traité [121] | Bhardwaj, Singh, Bhardwaj, *Agent Behavioral Contracts II*, arXiv:2608.12895 | `arxiv.org/abs/2608.12895` | ☑ 13 août 2026 ; « 90.0 % of the missions on which either fails », « phi 0.916 », « 18,000 missions » — au chiffre |
| Traité [119] | Anthropic, Frontier Red Team, *Patterns and problems in emerging multiagent systems* | `anthropic.com/research/multiagent-systems` | ☑ 13 août 2026 ; 266 contre 21 vulnérabilités ; 18 agents sur 30, même nom de branche ; dilemme du prisonnier — au fait |
| Vol. II F-36 | Calvanese *et al.*, *Agentic Business Process Management: A Research Manifesto*, arXiv:2603.18916 | `arxiv.org/abs/2603.18916` | ☑ 19 mars 2026 ; 18 auteurs ; « framed autonomy » au résumé |
| Vol. II F-37 | Rinderle-Ma *et al.*, *Design and Implementation of Agentic Orchestrations…*, arXiv:2606.31518 | `arxiv.org/abs/2606.31518` | ☑ 30 juin 2026 ; les six auteurs cités |
| Vol. III F-46 | RFC 9901, SD-JWT | `rfc-editor.org/rfc/rfc9901` | ☑ *Selective Disclosure for JSON Web Tokens*, Proposed Standard, 2025 |
| Vol. I ch. 3 | Yuan *et al.*, *Beyond Message Passing*, arXiv:2604.02369 | `arxiv.org/abs/2604.02369` | ☑ 30 mars 2026 ; trois couches — communication, syntaxique, sémantique — au résumé |
| Article @survey | Döbler, Jattana, arXiv:2507.03540 | `arxiv.org/abs/2507.03540` | ☑ 4 juillet 2025 ; 107 publications |
| Article @qihpc | Raj, Sai, Simmhan, Chard, Buyya, arXiv:2604.19814 | `arxiv.org/abs/2604.19814` | ☑ 17 avril 2026 ; « a visionary architectural framework » au résumé — le mot que l'article lui prête |
| État de l'art [114] | Paiements Canada, 30 juin 2026 | `payments.ca/critical-milestone-…` | ☑ règlement et règles en vigueur le 24 août 2026 ; lancement au T4 2026 |
| Vol. II F-09 | BSIF, ligne directrice E-23, entrée en vigueur 1er mai 2027 | deux adresses `osfi-bsif.gc.ca` | ✗ **non atteinte** — HTTP 404 sur les deux ; adresses de l'évaluateur ; fait non vérifié ici |
