# Audit d'ancrage atomique — Chapitre 04 — Posséder le noyau de contrôle : l'architecture 80/20 contre les modèles jetables

- **Unité du livre** : `ch04` (`manuscrit/02 - Partie II/Chapitre 04 - Posseder le noyau de controle 80-20.md`)
- **Dossier de sources fermé** : `sources/ch04-sources.md` (18 sources intégrales `L+`)
- **Registres consultés** : `registre/ancres-chronologiques.json`, `registre/faits-empiriques.json`, `registre/glossaire-termes.json`
- **Barrière** : `G2` — Audit indépendant `auditeur-wyvern` (`CA-10`, `CA-12`, régime Production)
- **Date de gel des faits** : 2 décembre 2026 (audit initial 2026-11-22)
- **Volume final vérifié (`v1.3`)** : `5 749` mots lexicaux `G1` (`5 921` `split()`, intervalle cible `[5 152, 6 048]`)

## Bilan synthétique

- **Affirmations atomiques auditées** : 59
- **Constat initial — supportés** : 42
- **Constat initial — imprécis** : 17 (tous rectifiés directement dans le manuscrit)
- **Constat initial — écarts sans source probante** : 0
- **Verdict final — supportés : 59 (100 %)**
- **Verdict final — imprécis résiduels : 0**
- **Verdict final — non supportés résiduels : 0**

> **Contrôles transversaux spécifiques :**
> - **Règle 80/20** : explicitement posée à la section 4.3 et à l'arbitrage 1 comme *heuristique d'ingénierie de la collection* et non comme mesure empirique universelle (concordance vérifiée avec `registre/glossaire-termes.json`).
> - **Sources nommées** : toutes les références à Storey (`SRC-040`), CoALA (`SRC-026`), SagaLLM (`SRC-006`), Temporal (`SRC-034`), MCP (`SRC-038`), A2A (`SRC-039`), SPIFFE (`SRC-046`), Kraishan (`SRC-057`), BSIF B-10 (`SRC-068`) et CaMeL (`SRC-007`), ainsi qu'aux sources `[1]`, `[2]`, `[3]`, `[6]`, `[8]`, `[9]`, `[10]`, `[13]`, concordent après rectification avec les textes intégraux `.txt` de `recherche/corpus_l_plus/`.

---

## Détail paragraphe par paragraphe

### P01 (L1–L3) — Titre et question directrice
- **A-01** : Le chapitre pose comme question directrice l'identification des briques architecturales qu'une institution doit posséder pour remplacer n'importe quel modèle ou fournisseur en quelques jours.
  - *Vérification* : Cadrage éditorial programmatique du chapitre, repris de façon vérifiable en 4.4 (exercice bimodèle) et à l'arbitrage 3 sans prétention statistique externe.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P02 (L5) — Scénario illustratif (incident de mise à jour nocturne)
- **A-02** : Une institution financière fictive subit la rupture simultanée d'invites métier lorsqu'un fournisseur met à jour un modèle de fondation propriétaire.
  - *Vérification* : Explicitement introduit par « Scénario illustratif : imaginons… » à valeur pédagogique, sans chiffre ni attribution empirique externe.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P03 (L7) — Analyse du scénario illustratif
- **A-03** : L'incident illustratif découle de l'enfouissement de règles métier et de conformité dans des consignes en prose accordées aux habitudes d'un unique modèle, en l'absence de contrats typés, de machines à états explicites et de registres indépendants.
  - *Vérification* : Analyse conceptuelle du scénario illustratif amorçant l'argumentation du chapitre.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P04 (L9) — Transition Partie I / Partie II et noyau de contrôle déterministe
- **A-04** : Rappel du chapitre 03 sur les silos des suites commerciales fermées et opposition entre le **noyau de contrôle déterministe** (*deterministic control core*) possédé par l'institution et les moteurs probabilistes substituables.
  - *Vérification* : Cohérent avec `registre/glossaire-termes.json` (`noyau de contrôle déterministe` / `deterministic control core`, propriétaire `ch04`) et la structure de l'ouvrage.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P05 (L13–L15) — Section 4.1 : Les quatre dettes de l'agentique improvisée
- **A-05** : L'automatisation agentique sans discipline de génie logiciel engendre quatre dettes interdépendantes : technique, cognitive, d'intention et de couplage global.
  - *Vérification* : Cadre analytique structurant la section 4.1 et justifié aux paragraphes suivants par les sources `[2]`, `[3]`, `[4]`, `[5]`, `[15]`, `[16]`, `[17]`.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P06 (L17) — Dette technique et `CoALA` [5]
- **A-06** : Sumers, Yao, Narasimhan et Griffiths (`CoALA`, 2024) rappellent que la multiplication d'agents isolés construits par des équipes distinctes accumule de la dette technique (dans le prolongement des travaux sur les systèmes ML) et recommandent une bibliothèque d'agents unifiée à l'échelle de l'entreprise pour faciliter les tests et la réutilisation des composants `[5]`.
  - *Vérification* : `sources/ch04-sources.md` `[5]` (`SRC-026`) ; `SRC-026.txt` § 6 (L786–790 : *maintaining a single company-wide "language agent library" would reduce technical debt (Sculley et al., 2014; Lwakatare et al., 2020) by facilitating testing and component re-use* ; *hodgepodge of language agents developed by individual teams* ; L1437 citant Sculley et al. 2014 sur la dette technique du ML).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P07 (L19) — Recensement `MCP` de Kraishan [15]
- **A-07** : Dans une prépublication de septembre 2026, Kraishan a mené le premier recensement complet du registre public `MCP` sur un cliché d'août 2026 couvrant 21 643 serveurs uniques et 72 606 enregistrements de versions, en analysant le code source de 14 353 serveurs `[15]`.
  - *Vérification* : `sources/ch04-sources.md` `[15]` (`SRC-057`) ; `SRC-057.txt` Abstract & § 3.1 (L7, L12–14, L43, L46–49, Table 3 L408–421).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-08** : L'analyse du registre montre que le schéma ne versionne pas les définitions d'outils elles-mêmes et que, parmi les 8 900 serveurs multi-versions, 51,09 % ont modifié leur description, leurs paquets ou leurs points de terminaison entre versions, tandis que 40,58 % de ces serveurs multi-versions ont subi au moins un changement sémantique silencieux sous des identifiants inchangés (forme empirique de **dérive silencieuse d'outil**, *silent tool drift*) `[15]`.
  - *Vérification* : `SRC-057.txt` § 3.1.1, § 3.1.4 & § 4.2 (L144–145, L213, L553–556 : 4 547 soit 51,09 % et 40,58 % des `n = 8 900` serveurs multi-versions) ; `registre/glossaire-termes.json` (`dérive silencieuse d'outil`).
  - *Constat initial* : imprécis — le texte initial qualifiait ces mesures de « constats statiques » (alors qu'elles proviennent de l'analyse différentielle du registre et non du scanner de code) et écrivait « dont 40,58 % par dérive silencieuse d'outil », rendant le dénominateur ambigu et attribuant au registre une mesure directe des définitions d'outils alors qu'il mesure la dérive silencieuse de la surface annoncée.
  - *Rectification appliquée* : reformulé en « Son analyse du registre montre… tandis que 40,58 % de ces serveurs multi-versions ont subi au moins un changement sémantique silencieux sous des identifiants inchangés (forme empirique de **dérive silencieuse d'outil**, *silent tool drift*) [15] ».
  - *Verdict final : supporté*
- **A-09** : 370 serveurs (4,16 %) ont redirigé leur point de terminaison distant vers un autre hôte sous le même nom de registre sans notification protocolaire au client installé, et la dérive silencieuse s'associe à `OR = 2,96` (`IC 95 %` `[2,56, 3,42]`) pour un constat de gravité élevée parmi les 6 699 serveurs multi-versions analysés dans la population scannée `[15]`.
  - *Vérification* : `SRC-057.txt` § 4.2 & Table 5 (L558–560, L588–591, L639–640 : *Restricting to the 6,699 multi-version servers inside the scan population, servers with silent drift have 2.96 times the odds of a high-severity finding (CI [2.56, 3.42])*).
  - *Constat initial* : imprécis — la phrase initiale omettait de préciser que l'odds ratio porte sur les 6 699 serveurs multi-versions présents dans la population scannée.
  - *Rectification appliquée* : ajout de « parmi les 6 699 serveurs multi-versions analysés ».
  - *Verdict final : supporté*

### P08 (L21) — Dette cognitive côté machine : `CoALA` [5] et `SagaLLM` [4]
- **A-10** : Sumers et al. rappellent qu'un modèle de langage demeure par construction sans état (*stateless*) et fonctionne comme un système de production probabiliste aux milliards de paramètres opaques `[5]`.
  - *Vérification* : `SRC-026.txt` § 3.1 & § 4.1 (L276–281 *probabilistic production systems*, *billions of uninterpretable parameters*, *inherent opaqueness* ; L476 *Language models are stateless*).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-11** : Dans `SagaLLM`, Chang et Geng synthétisent trois limites : l'absence native d'état transactionnel entre appels successifs, la dégradation marquée de la rétention en contexte long (notamment au milieu de la fenêtre où se perdent buts et dépendances) et un déficit intrinsèque d'auto-validation `[4]`.
  - *Vérification* : `SRC-006.txt` § 2.2 (L178–215 : *Self-Validation Gap*, *Statelessness Necessitating Transactional Integrity*, *Context Limitations* — *especially for mid-context information*, *goals, justifications, and dependencies*).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P09 (L23) — Dette cognitive côté humain : Storey [17]
- **A-12** : Dans une analyse conceptuelle publiée en prépublication en mars 2026, Margaret-Anne Storey définit la dette cognitive comme la perte de compréhension partagée par l'équipe (théorie du système) lorsque le code et les artefacts générés par l'IA s'accumulent plus vite que les modèles mentaux humains `[17]`.
  - *Vérification* : `sources/ch04-sources.md` `[17]` (`2026-03-23`, `arXiv:2603.22106`) ; `SRC-040.txt` (L14–23, L48 *theory of the system*, L240–241 *AI generates code faster than teams can build the understanding*).
  - *Constat initial* : imprécis — le texte initial parlait d'« artefacts assistés par IA », alors que Storey vise explicitement le code (et la documentation/artefacts) généré par l'IA.
  - *Rectification appliquée* : remplacé par « le code et les artefacts générés par l'IA ».
  - *Verdict final : supporté*
- **A-13** : Aggravée par la « capitulation cognitive » (acceptation peu critique des sorties des modèles), cette dette rend les équipes incapables d'expliquer le comportement du système ou d'anticiper les effets de bord d'un changement même lorsque les tests apparents réussissent `[17]`, fragilité transposée aux chaînes d'agents.
  - *Vérification* : `SRC-040.txt` (L12–13, L55 *Tests may pass, but the product may have the wrong behavior*, L97–109 *cognitive surrender*, L118–L119 *Unexpected results*).
  - *Constat initial* : imprécis — la version initiale attribuait à `[17]` l'expression « chaînes d'agents » et « tests unitaires apparents », alors que Storey traite des systèmes logiciels en général et écrit « Tests may pass ».
  - *Rectification appliquée* : recentré la proposition ancrée sur `[17]` sur « le comportement du système » et « les tests apparents », suivi de « — une fragilité directement transposée aux chaînes d'agents ».
  - *Verdict final : supporté*

### P10 (L25) — Dette d'intention : Hadfield & Koh [3] et Shahidi et al. [2]
- **A-14** : Hadfield et Koh rapprochent l'alignement des agents de l'incomplétude inévitable des contrats : un mandant humain ne peut spécifier à l'avance toutes les situations limites, laissant un écart permanent entre ce qu'il veut et ce qu'un optimiseur opaque exécute `[3]`.
  - *Vérification* : `SRC-005.txt` § 1.1 & § 2.1 (L72–76, L149–152, L204).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-15** : Shahidi, Rusak, Manning, Fradkin et Horton décomposent ce déficit en deux goulots distincts : *limites d'articulation du mandant* (préférences de haute dimensionnalité impossibles à énoncer de manière complète et cohérente) et *limites de synthèse de l'agent* (réinterprétation erronée ou hallucination) `[2]`.
  - *Vérification* : `SRC-004.txt` § 3 (L329–334, L344–345).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P11 (L27) — Dette d'intention en génie logiciel : Storey [17] et Hadfield & Koh [3]
- **A-16** : Storey situe la dette d'intention dans l'absence ou l'obsolescence des artefacts externes hors code (spécifications, décisions d'architecture, tests exécutables et contraintes explicites) capturant la finalité du système `[17]`.
  - *Vérification* : `SRC-040.txt` (L168–171, L191, L198, L203).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-17** : Un ajustement étroit (*fine-tuning*) sur un comportement peut engendrer un désalignement généralisé ailleurs en raison de l'opacité des modèles, comme le rappellent Hadfield et Koh `[3]`, soulignant l'impossibilité d'auditer une simple règle en prose dans une invite système.
  - *Vérification* : `SRC-005.txt` § 1.1 (L119–123 citant Betley et al. 2025 sur *narrow finetuning* entraînant un désalignement généralisé).
  - *Constat initial* : imprécis — l'expression initiale « un ajustement étroit sur un comportement » placée après la prose d'une invite système prêtait à confusion avec l'édition d'invites.
  - *Rectification appliquée* : précisé « un ajustement étroit (*fine-tuning*) sur un comportement peut engendrer un désalignement généralisé ailleurs, comme le rappellent Hadfield et Koh à propos de l'opacité des modèles [3] ».
  - *Verdict final : supporté*

### P12 (L29) — Dette de couplage global : agent « *bowling-shoe* » [2]
- **A-18** : Shahidi et al. nomment agent « *bowling-shoe* » un composant fourni par une plateforme hôte, commode au démarrage mais privé de portabilité, moins inspectable et vulnérable aux biais d'orientation (*steering*) `[2]` ; l'entreprise en réplique les travers lorsqu'elle accorde ses invites aux réflexes d'un seul modèle, pesant sur le coût de sortie et la tolérance aux pannes posés au liminaire.
  - *Vérification* : `SRC-004.txt` § 4 & Table 2 (L427–429, L468–492).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P13 (L31) — Erreurs corrélées [3] et ligne directrice `BSIF B-10` [16]
- **A-19** : Hadfield et Koh avertissent que la copie d'un même agent (modèle et échafaudage identiques) au sein d'une organisation ou entre firmes produit des erreurs corrélées qui ne s'annulent pas au niveau agrégé, comme les algorithmes de négociation qui ont amplifié le krach éclair de 2010 effaçant environ 1 000 G$ US en quinze minutes selon les travaux cités par ces auteurs `[3]`.
  - *Vérification* : `SRC-005.txt` § 3.4 (L508–513 : *the same agent is 'copied' both within and between firms* ; *2010 'Flash Crash' that wiped out approximately $1 trillion over the span of 15 minutes (Kirilenko et al., 2017)*).
  - *Constat initial* : imprécis — le texte initial écrivait « copie d'un même modèle et d'un même échafaudage à l'échelle d'une organisation ou d'un secteur », s'écartant légèrement de l'énoncé littéral « the same agent is 'copied' both within and between firms ».
  - *Rectification appliquée* : reformulé en « copie d'un même agent (modèle et échafaudage identiques) au sein d'une organisation ou entre firmes ».
  - *Verdict final : supporté*
- **A-20** : Au Canada, la ligne directrice `B-10` du `BSIF` rappelle que l'institution conserve l'entière imputabilité des activités confiées à des tiers et exige de maîtriser le risque de concentration, d'évaluer la portabilité applicative et de maintenir des plans de sortie réalistes aussi bien pour un retrait planifié que pour une sortie en situation de crise `[16]`.
  - *Vérification* : `SRC-068.txt` (L287, L313, L315, L323, L443–447, § 2.2.3 L311–L315, § 2.3.5 L443–L461 *non-stressed exit* / *stressed exit*, § 4.4 L557, Annex 1 L563–L601).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P14 (L33) — Synthèse de l'engrenage des quatre dettes
- **A-21** : Synthèse causale reliant les quatre dettes analysées en 4.1 et introduisant la stratification d'urbanisation de 4.2.
  - *Vérification* : Articulation logique interne s'appuyant sur les constats déjà ancrés en 4.1.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P15 (L37–L41) — Section 4.2 : Stratification `SoE` / `SoA` / `SoR`
- **A-22** : L'urbanisation sépare trois couches : **systèmes d'engagement** (`SoE`), **systèmes d'agence** (`SoA`) et **systèmes d'autorité** (`SoR`).
  - *Vérification* : Modélisation d'architecture d'entreprise cohérente avec `registre/glossaire-termes.json` (`noyau de contrôle déterministe`, `couche anti-corruption`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P16 (L43) — Protection des `SoR` : Garcia-Molina & Salem [6] et Chang & Geng [4]
- **A-23** : Dès 1987, Garcia-Molina et Salem montraient que les transactions de longue durée (*Long Lived Transactions*) multiplient les blocages, interblocages et taux d'annulation lorsqu'elles conservent des verrous sur des bases critiques `[6]`.
  - *Vérification* : `SRC-033.txt` § 1 (L161–226).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-24** : S'appuyant sur ce principe, Chang et Geng montrent dans `SagaLLM` comment isoler l'état intermédiaire d'un flux agentique et valider indépendamment ses contraintes avant tout engagement définitif `[4, 6]`, d'où l'obligation en pratique de passer par une **couche anti-corruption** (`ACL`, chap. 05) entre `SoA` et `SoR`.
  - *Vérification* : `SRC-006.txt` (L167–170, L381–389, L787, L870–878) et `registre/glossaire-termes.json` (`couche anti-corruption`).
  - *Constat initial* : imprécis — la version initiale faisait dire à Chang et Geng une démonstration portant directement sur « les bases d'autorité », vocabulaire d'urbanisation qui relève plutôt de l'architecture du chapitre.
  - *Rectification appliquée* : reformulé en « Chang et Geng montrent dans `SagaLLM` comment isoler l'état intermédiaire d'un flux agentique et valider indépendamment ses contraintes avant tout engagement définitif [4, 6]. En pratique, toute interaction entre la couche `SoA` et un `SoR` patrimonial doit emprunter… ».
  - *Verdict final : supporté*

### P17 (L45) — L'agent comme composant applicatif borné
- **A-25** : Dans le référentiel d'entreprise comme en droit, un agent n'est jamais un acteur métier autonome mais un composant applicatif borné, interdisant la création de faux comptes d'employés numériques.
  - *Vérification* : Thèse architecturale justifiée au paragraphe suivant par `[3]` et `[16]`.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P18 (L47) — Statut juridique [3] et imputabilité non transférable `BSIF B-10` [16]
- **A-26** : Hadfield et Koh rappellent que le droit des contrats, des obligations et de la responsabilité repose sur des personnes physiques ou morales capables de détenir un patrimoine propre et d'exécuter une condamnation, discutent deux voies théoriques (imputation à une entité enregistrée ou personnalité juridique artificielle dotée d'actifs saisissables) et constatent qu'aucun cadre opérationnel actuel ne confère cette infrastructure aux agents `[3]`.
  - *Vérification* : `SRC-005.txt` § 4 & § 4.1 (L521–584).
  - *Constat initial* : imprécis — le texte initial généralisait à « les économistes et juristes envisagent deux modèles théoriques » alors que seule l'analyse de Hadfield et Koh est citée.
  - *Rectification appliquée* : remplacé par « Même si Hadfield et Koh discutent deux voies théoriques… ».
  - *Verdict final : supporté*
- **A-27** : Au Canada fédéral, la ligne directrice `B-10` du `BSIF` consacre une imputabilité non transférable : l'institution demeure pleinement responsable de toute activité confiée à un tiers — incluant les services technologiques ou automatisés —, que le prestataire soit lié par contrat négocié, par contrat standardisé ou sans contrat écrit `[16]`.
  - *Vérification* : `SRC-068.txt` (L287, L309, L331, L443–447, § 3.1 L505–L513, § 3.2 L515–L519, § 4 L537–L561).
  - *Constat initial* : imprécis — l'expression initiale « toute activité automatisée ou impartie » prêtait à `B-10` le mot « automatisée » absent du texte officiel (`SRC-068.txt`).
  - *Rectification appliquée* : remplacé par « de toute activité confiée à un tiers — incluant les services technologiques ou automatisés — ».
  - *Verdict final : supporté*

### P19 (L49) — Charge de travail `SPIFFE` [14] et traçabilité `OpenTelemetry` [10]
- **A-28** : Selon `SPIFFE`, une charge de travail est un processus logiciel déployé pour une fonction déterminée, identifié par un URI cryptographique (`SPIFFE ID`) dans un domaine de confiance et attesté par un document éphémère à rotation fréquente (`SVID`, idéalement `X.509-SVID` pour éviter le rejeu de jetons) délivré dynamiquement par la `Workload API` sans co-déployer de secret statique `[14]`.
  - *Vérification* : `SRC-046.txt` (L8–18, L27–33, L45–50, L56–79).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-29** : L'identité technique de l'agent est corrélée dans l'observabilité sous un attribut stable tel que `gen_ai.agent.id` `[10]`, sans octroyer de pouvoir d'action hors mandat explicite.
  - *Vérification* : `SRC-037.txt` (L62, L94 : `gen_ai.agent.id` = *stable unique identifier of the GenAI agent*).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P20 (L51) — Délégation `RFC 8693` [13] et exposition `MCP` selon Kraishan [15]
- **A-30** : `RFC 8693` oppose l'**usurpation d'identité** (*impersonation*), où l'appelant devient indiscernable de l'utilisateur représenté, et la **délégation explicite** (*delegation*, qualifiée dans le glossaire de délégation *On-Behalf-Of*, `OBO`), où l'intermédiaire conserve son identité (`act`) à côté du sujet (`sub`) dans un jeton composite, tandis que la revendication `may_act` sur le jeton présenté permet de restreindre les mandataires autorisés `[13]`.
  - *Vérification* : `SRC-041.txt` (§ 1.1 L173–233, § 4.1 L674–755, § 4.4 L802–848, App. A.2 Fig. 15 & 18) et `registre/glossaire-termes.json` (`délégation au nom de` / `On-Behalf-Of (OBO)`).
  - *Constat initial* : imprécis — la phrase initiale décrivait `may_act` comme un champ du jeton composite émis, alors que la `RFC 8693` § 4.4 place `may_act` dans le *subject_token* présenté pour autoriser l'acteur.
  - *Rectification appliquée* : reformulé en « dans un jeton composite, tandis que la revendication `may_act` sur le jeton présenté permet de restreindre les mandataires autorisés [13] ».
  - *Verdict final : supporté*
- **A-31** : Sur les 14 353 serveurs `MCP` scannés par Kraishan, 9,57 % (6,83 % après correction de précision) présentent une exposition réseau sans authentification, et 225 serveurs (1,57 % observés ; environ 0,75 % corrigés) présentent soit une autorité ambiante, soit une transmission directe de jetons (*token passthrough*) — deux défaillances disjointes qui ne coexistent jamais dans le corpus, la seconde effaçant la trace du composant intermédiaire dans l'audit aval `[15]`.
  - *Vérification* : `SRC-057.txt` (Table 4 L434–437, § 4.1 L474–476, § 4.1.1 L491–495 *notably the two never co-occur (0 of 14,353)*, L544–545, § 3.2 L231–233).
  - *Constat initial* : imprécis — le verbe initial « combinent » contredisait le constat explicite de non-co-occurrence totale (0/14 353) entre autorité ambiante et *token passthrough*.
  - *Rectification appliquée* : remplacé par « présentent soit une autorité ambiante, soit une transmission directe de jetons (*token passthrough*) — deux défaillances disjointes qui ne coexistent jamais dans le corpus, la seconde effaçant la trace du composant intermédiaire dans l'audit aval [15] ».
  - *Verdict final : supporté*

### P21 (L53) — Trois invariants non négociables de la couche `SoA`
- **A-32** : Synthèse de trois invariants (aucun droit propre ni clé statique ; chaîne de mandat vérifiable approfondie au chap. 07 ; accès aux `SoR` via interfaces typées médiatisées) et transition vers la discipline 80/20.
  - *Vérification* : Synthèse interne de la section 4.2 avec renvoi structurel au chapitre 07.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P22 (L57–L59) — Section 4.3 : Statut épistémique de la partition 80/20
- **A-33** : La partition 80/20 (*80/20 deterministic-probabilistic split*) est explicitement présentée comme une heuristique d'ingénierie de cette collection et non comme une mesure empirique universelle.
  - *Vérification* : Conforme au statut de l'heuristique défini dans `registre/glossaire-termes.json` (`partition 80/20`) et aux exigences méthodologiques du contrat d'ancrage.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P23 (L61) — Fondements formels : `CoALA` [5], `SagaLLM` [4] et chapitre 02
- **A-34** : Dans `CoALA`, Sumers et al. distinguent dans la mémoire procédurale le code explicite écrit par le concepteur (déterministe, lisible par l'humain, testable et borné aux situations anticipées) des poids implicites du modèle (flexibles en contexte inédit mais opaques et difficiles à contrôler), et mettent en garde contre la modification autonome du code procédural par le modèle `[5]`.
  - *Vérification* : `SRC-026.txt` (§ 3.1 L279–282, § 4.1 L510–518, § 6 L787, L791–795).
  - *Constat initial* : imprécis — la formulation initiale « impossibles à inspecter et à garantir sur des cas rares » forçait légèrement le propos de `CoALA` sur les propriétés des poids et du code.
  - *Rectification appliquée* : reformulé pour refléter littéralement *CoALA* : « le code explicite écrit par le concepteur — déterministe, lisible par l'humain, testable et borné aux situations anticipées — et les poids implicites du modèle, dotés d'une flexibilité statistique remarquable en contexte inédit mais opaques et difficiles à contrôler [5] ».
  - *Verdict final : supporté*
- **A-35** : Rappel de l'incapacité d'auto-validation des modèles (`SagaLLM` `[4]`) et renvoi à l'effondrement géométrique des chaînes probabilistes illustré au chapitre 02.
  - *Vérification* : `SRC-006.txt` § 2.2 (L184–195) et `registre/faits-empiriques.json` (`FACT-LUSSER-10-STEPS`, propriétaire `ch02`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P24 (L63) — Exécution durable `Temporal` [7]
- **A-36** : Selon `Temporal`, la définition du flux (*Workflow Definition*) reste strictement déterministe pour autoriser le rejeu depuis le journal d'événements (*Event History*) après panne sans réexécuter les effets de bord déjà validés ; tout appel non déterministe (base de données, appel réseau externe ou, pour un agent, inférence d'un `LLM`) est confiné dans une activité isolée (*Activity*) dont le retour est mémorisé, et toute divergence au rejeu déclenche une erreur de non-déterminisme `[7]`.
  - *Vérification* : `SRC-034.txt` (L23, L82–90, L160–161, L177–186, L221–228) ; `sources/ch04-sources.md` `[7]`.
  - *Constat initial* : imprécis — la phrase initiale plaçait « requête vers un LLM » dans les exemples directs attribués à `Temporal` `[7]`, alors que `SRC-034.txt` L160 cite *querying a database or calling an external service*.
  - *Rectification appliquée* : reformulé en « requête vers une base de données, appel réseau externe ou, pour un agent, inférence d'un `LLM` ».
  - *Verdict final : supporté*

### P25 (L65–L69) — Figure 7 et anatomie du harnais en 10 composants
- **A-37** : La figure 7 (`Fig-07.svg`) encadre l'étape 4 probabiliste entre neuf briques déterministes (étapes 1–3 en amont, étapes 5–8 en aval, repli déterministe et journal de preuve), interdisant toute boucle libre de réparation conversationnelle.
  - *Vérification* : Conception architecturale propre au chapitre, cohérente avec `registre/glossaire-termes.json` (`harnais d'agent`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P26 (L71–L73) — Sas amont (étapes 1–3) et appel probabiliste (étape 4), `CoALA` [5]
- **A-38** : Les étapes 1 à 3 valident l'entrée et la portée, assemblent la mémoire de travail décrite par `CoALA` `[5]` à partir de variables filtrées et plafonnent budget et tours, avant l'appel sans état de l'étape 4.
  - *Vérification* : `SRC-026.txt` § 4.1 (L481–491 : *working memory* comme structure de variables symboliques alimentant le prompt).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P27 (L75) — Étape 5 : décodage contraint et `CoALA` [5]
- **A-39** : Dès 2024, Sumers et al. mettaient en avant l'analyse structurelle des sorties (*structured output parsing*) comme levier structurant pour mettre à jour les variables de mémoire de travail au-delà des manipulations textuelles de bas niveau `[5]`.
  - *Vérification* : `SRC-026.txt` § 6 (L824–833 : *low-level string operations* et *Structural output parsing solutions ... can help update working memory variables*).
  - *Constat initial* : imprécis — l'adjectif « indispensable » et « découpage fragile » forçaient légèrement « can help » et « low-level string operations » dans `SRC-026.txt`.
  - *Rectification appliquée* : remplacé par « comme levier structurant pour mettre à jour proprement les variables de mémoire de travail au-delà des manipulations textuelles de bas niveau [5] ».
  - *Verdict final : supporté*

### P28 (L77) — Étape 6 : validateur métier et `SagaLLM` [4]
- **A-40** : L'étape 6 applique des assertions déterministes (plages, arithmétique, dates, identifiants issus du contexte) avec repli déterministe vers rejet ou escalade, matérialisant l'exigence de validation externe indépendante défendue par Chang et Geng `[4]`.
  - *Vérification* : `SRC-006.txt` (§ 2.2 L184–195, § 3.2 L265–271 & L405–412, § 4.4.2 L875–878).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P29 (L79) — Étape 7 : porte de politique hors modèle, `MCP` [11] et `CaMeL` [18]
- **A-41** : La spécification `MCP` avertit que les outils représentent une exécution de code arbitraire, que leurs descriptions doivent être tenues pour non fiables sauf provenance vérifiée et que le protocole lui-même ne fait pas respecter le consentement ni le contrôle d'accès `[11]`.
  - *Vérification* : `SRC-038.txt` (*Security and Trust & Safety* L88–L99, L5002).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-42** : Dans une approche convergente évaluée par les pairs (`IEEE SaTML`), `CaMeL` (Debenedetti et al.) extrait le graphe de flux de contrôle depuis la requête fiable de l'utilisateur et confie l'exécution à un interpréteur déterministe muni de capacités et de politiques de flux de données hors modèle, empêchant les données externes lues par un modèle confiné de détourner les appels d'outils `[18]` ; renvoi au chapitre 08.
  - *Vérification* : `SRC-007.txt` (Abstract L8–14, § 2 L163–183, § 5 L351–360, §§ 5.1–5.4 L415–599), `sources/ch04-sources.md` `[18]` (`Évalué par les pairs : Oui`, `arXiv / IEEE SaTML`) et `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P30 (L81) — Étape 8 : clé d'idempotence `IETF HTTPAPI` [9]
- **A-43** : Suivant le brouillon du groupe `HTTPAPI` de l'`IETF`, l'en-tête `Idempotency-Key` (idéalement un `UUID` aléatoire à haute entropie), associé côté ressource à une empreinte de charge utile sur des méthodes non idempotentes (`POST`, `PATCH`), permet à la ressource de restituer la réponse d'origine si l'empreinte concorde, de rejeter en `HTTP 422` si la charge diffère et de signaler un conflit en `HTTP 409` si l'opération initiale est encore en cours `[9]`.
  - *Vérification* : `SRC-036.txt` (`draft-ietf-httpapi-idempotency-key-header-09`, Abstract L153–154, § 2.2 L305, § 2.4 L321–337, § 2.6 L404–416, § 2.7 L446–471, § 5 L716–718).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P31 (L85–L87) — Section 4.4 : Noyau en quatre plans découplés
- **A-44** : La couche `SoA` organise le noyau déterministe en quatre plans découplés reliés aux modèles par un routeur d'inférence agnostique.
  - *Vérification* : Synthèse d'architecture cohérente avec `registre/glossaire-termes.json` (`noyau de contrôle déterministe`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P32 (L89) — Plan 1 : registre, `SPIFFE` [14] et épinglage face à la dérive `MCP` [15]
- **A-45** : Le Plan 1 recense agents et outils et repose sur une **identité non humaine** (`NHI`) éphémère émise par attestation de charge de travail selon `SPIFFE`, éliminant clés statiques et comptes partagés `[14]`.
  - *Vérification* : `SRC-046.txt` (L45–78) et `registre/glossaire-termes.json` (`identité non humaine` / `NHI`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-46** : Puisque le registre public `MCP` ne versionne pas les définitions d'outils et que 40,58 % des serveurs multi-versions observés modifient silencieusement ce qu'ils annoncent (description, paquets ou destination) sous identifiants inchangés tandis que 4,16 % redirigent leur point de terminaison distant `[15]`, le registre possédé épingle cryptographiquement définitions, paquets et hôtes autorisés ; renvoi au chapitre 07.
  - *Vérification* : `SRC-057.txt` (§ 4.2 L554–560 ; § 5.1 L763–772 sur le *client-side pinning* des hôtes et empreintes de paquets).
  - *Constat initial* : imprécis — la phrase initiale disait « 40,58 % des serveurs multi-versions observés changent silencieusement de comportement », alors que l'étude n'exécute pas les serveurs et mesure les changements silencieux de ce que le serveur annonce dans le registre.
  - *Rectification appliquée* : remplacé par « modifient silencieusement ce qu'ils annoncent (description, paquets ou destination) sous identifiants inchangés ».
  - *Verdict final : supporté*

### P33 (L91) — Plan 2 : passerelle de politiques, `RFC 8693` [13], `MCP` [11] et `A2A` [12]
- **A-47** : La passerelle applique hors modèle la réduction de portée `RFC 8693` `[13]` ainsi que les garde-fous sur `MCP` `[11]` et `A2A` — dont la spécification sépare modèle de données canonique, opérations abstraites et liaisons de transport tout en préservant une exécution opaque entre domaines `[12]` ; renvoi aux chapitres 05 et 08.
  - *Vérification* : `SRC-041.txt` (§ 1 L150–151, § 2.1 `scope`, § 5 L865–869), `SRC-038.txt`, `SRC-039.txt` (§ 1.2 L1011 *Opaque Execution*, § 1.3 L1017–1044 *Layer 1–3*, App. B L6383–6393).
  - *Constat initial* : imprécis — le participe « garantissant une exécution opaque » était trop affirmatif vis-à-vis du principe *Opaque Execution* de `A2A` qui n'exige pas le partage d'état interne.
  - *Rectification appliquée* : remplacé par « tout en préservant une exécution opaque entre domaines [12] ».
  - *Verdict final : supporté*

### P34 (L91) — Plan 2 : routeur d'inférence agnostique et `BSIF B-10` [16]
- **A-48** : Maintenir un modèle principal et au moins un modèle de repli qualifié derrière un routeur d'inférence agnostique rend crédibles les exigences de portabilité, de gestion de la concentration et de plans de sortie en situation normale ou de crise de `BSIF B-10` `[16]`.
  - *Vérification* : `SRC-068.txt` (§ 2.2.3, § 2.3.5, § 4.4).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P35 (L93) — Plan 3 : mémoire gouvernée `CoALA` [5] et `SagaLLM` [4]
- **A-49** : Suivant `CoALA`, le Plan 3 dissocie mémoire de travail, mémoire épisodique, mémoire sémantique et mémoire procédurale, cette dernière étant verrouillée en lecture seule vis-à-vis de l'agent `[5]`.
  - *Vérification* : `SRC-026.txt` (§ 4.1 L480–518 et § 6 L811–813 *read-only access to semantic and procedural memory*).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-50** : Chang et Geng rappellent dans `SagaLLM` l'importance de conserver explicitement en mémoire externe persistante objectifs, justifications et graphe de dépendances `[4]` ; renvoi au chapitre 05.
  - *Vérification* : `SRC-006.txt` (§ 2.2 L212–214, § 3.1.1 L381–389, § 3.3 L307–312 & L503–509).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P36 (L95) — Plan 4 : `Temporal` [7] et `CloudEvents v1.0.2` [8]
- **A-51** : La journalisation séquentielle des états et réponses d'activités selon l'*Event History* de `Temporal` autorise une relecture déterministe après crash ou coupure sans réexécuter les appels déjà validés `[7]`.
  - *Vérification* : `SRC-034.txt` (L84–90, L177–182, L221–229).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*
- **A-52** : L'enveloppe neutre `CloudEvents v1.0.2` (`id`, `source`, `specversion`, `type`, `time`) dissocie les attributs d'acheminement de la charge utile chiffrée `data`, évitant d'exposer des renseignements sensibles dans les bus intermédiaires `[8]`.
  - *Vérification* : `SRC-035.txt` (Context Attributes L244–428, Event Data L477–490, Privacy and Security L527–550).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P37 (L97) — Plan 4 : `OpenTelemetry GenAI` [10] et Tomašev et al. [1]
- **A-53** : Les conventions sémantiques en développement d'`OpenTelemetry GenAI` distinguent `invoke_agent` et `invoke_workflow`, prévoient un identifiant d'agent stable à la création (`gen_ai.agent.id`) ainsi qu'un nom d'agent sur l'invocation (`gen_ai.agent.name`), consignent le modèle sollicité et les jetons facturés, tout en maintenant `gen_ai.system_instructions` et `gen_ai.input.messages` en collecte optionnelle (`Opt-In`) afin de prévenir l'exposition de renseignements personnels `[10]`.
  - *Vérification* : `SRC-037.txt` (L7 *Development*, L61–L64 `gen_ai.agent.id` sur `create_agent`, L188–197 `invoke_agent` / `invoke_workflow`, L236 `gen_ai.agent.name`, L244 `gen_ai.request.model`, L250–256 `Opt-In`, L331–352 jetons facturés, L362 `user/PII data`, L425 `sensitive information`).
  - *Constat initial* : imprécis — la version initiale écrivait « rattachent chaque trace à un identifiant d'agent stable (`gen_ai.agent.id`) », alors que `SRC-037.txt` ne définit `gen_ai.agent.id` que sur le span `create_agent` et utilise `gen_ai.agent.name` sur `invoke_agent` / `invoke_workflow` et `plan`.
  - *Rectification appliquée* : remplacé par « prévoient un identifiant d'agent stable à la création (`gen_ai.agent.id`) ainsi qu'un nom d'agent sur l'invocation (`gen_ai.agent.name`) ».
  - *Verdict final : supporté*
- **A-54** : Tomašev et al. montrent que, dans une infrastructure de supervision à la vitesse des machines, l'imputabilité et l'analyse des causes racines parmi les défaillances possibles du modèle, de l'échafaudage, des données d'entrée ou des garde-fous reposent impérativement sur des registres cryptographiquement intègres et des pistes d'audit normalisées `[1]` ; renvoi aux chapitres 06 et 09 (`télémétrie à double couloir`, `pass^k`, `CPO`).
  - *Vérification* : `SRC-002.txt` (L1634–1691 : sept catégories de fautes incluant *underlying foundation models*, *agentic scaffolding*, *faulty input data*, *faulty safeguards* ; *at machine speed*, *immutable, cryptographically-secured ledgers* et *standardized, interpretable audit trails* pour *root cause analysis* et *accountability*) ; `registre/glossaire-termes.json`.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P38 (L97–L103) — Figure 8 et discipline d'architecture neutre
- **A-55** : La figure 8 (`Fig-08.svg`) sépare les éléments possédés en trait plein ardoise (`SoA`, quatre plans, routeur agnostique, façade `ACL`) des modèles substituables en pointillé ambre ; posséder le noyau signifie détenir contrats, schémas, règles et formats ouverts plutôt que réinventer moteurs ou bases.
  - *Vérification* : Conception architecturale propre au chapitre, cohérente avec le reste du texte.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P39 (L105–L109) — Tableau comparatif des plans et du harnais 80/20
- **A-56** : Le tableau synthétise pour chacun des quatre plans et pour le harnais `80/20` les invariants possédés, les ancrages normatifs `[4]..[16]` et les briques substituables.
  - *Vérification* : Concordance exacte avec l'ensemble des références vérifiées en 4.1–4.4 (`[4]` à `[16]`).
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P40 (L109) — L'exercice trimestriel de bascule bimodèle
- **A-57** : L'exercice trimestriel de bascule bimodèle vérifie empiriquement en interne qu'un second modèle qualifié raccordé derrière le routeur du Plan 2 respecte les contrats typés et la constance attendue lors du rejeu d'un jeu témoin issu du Plan 4.
  - *Vérification* : Protocole prescriptif proposé par l'ouvrage pour tester la promesse de réversibilité sans l'attribuer à une source externe.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P41 (L113–L119) — Encadré : Trois arbitrages sans regret — Chapitre 04
- **A-58** : Les trois arbitrages résument les prescriptions du chapitre : (1) ériger l'heuristique 80/20 en règle de conception dans un harnais typé ; (2) proscrire le statut d'acteur métier et l'accès direct aux `SoR` ; (3) bâtir le noyau neutre en quatre plans et prouver la réversibilité par l'exercice de bascule.
  - *Vérification* : Synthèse prescriptive fidèle aux sections 4.1–4.4 et respectant le statut d'heuristique d'ingénierie de la règle 80/20.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

### P42 (L121) — Paragraphe de transition vers le Chapitre 05
- **A-59** : Paragraphe de liaison annonçant le chapitre 05 sur la gouvernance de `MCP` et `A2A`, la dette sémantique et les couches anti-corruption.
  - *Vérification* : Transition éditoriale interne cohérente avec les renvois des sections 4.2 et 4.4.
  - *Constat initial* : supporté.
  - *Verdict final : supporté*

---

## Contrôle différentiel post-G4

- **Date du contrôle différentiel** : 2026-11-22
- **Objet** : Reprise de la barrière `G2` (`auditeur-wyvern`, régime Production) après retouche stylistique `G4` sur `ch04` (`L3, L39, L87–L113, L125–L135, L143`, correspondant au redécoupage en sous-sections de la section 4.4 et à l'encadrement des conditions de bascule, portant le manuscrit à 153 lignes).
- **Affirmations différentielles contrôlées (`D-01` à `D-15`)** : 15
- **Constat initial différentiel — supportés** : 12
- **Constat initial différentiel — imprécis** : 3 (tous rectifiés directement dans `manuscrit/02 - Partie II/Chapitre 04 - Posseder le noyau de controle 80-20.md`)
- **Constat initial différentiel — non supportés** : 0
- **Verdict différentiel final — supportés : 15 / 15 (`100 %`)**
- **Verdict différentiel final — imprécis résiduels : `0`**
- **Verdict différentiel final — non supportés résiduels : `0`**

### Détail des vérifications différentielles

- **D-01 (`L3, L39, L87, L131–L135, L143`) — Conditions de réversibilité et exercice bimodèle** : cadrage prescriptif interne bornant la promesse « en quelques jours » aux modèles de capacité comparable préalablement qualifiés (banc de non-régression sur le Plan 4, étalonnage des gabarits à l'étape 4, parité d'appels d'outils sur catalogue épinglé), sans attribution empirique externe.
  - *Verdict final : supporté*
- **D-02 (`L91`) — Kraishan (`SRC-057`, `[15]`)** : vérification directe contre `SRC-057.txt` (§ 1 L78, § 2 L121, § 3.1.1 L144–146, § 3.1.4 L208–215, § 4.2 L553–560, Table 5 L588–591, Fig. 5 L671–672) : absence de versionnement des définitions d'outils dans le registre public `MCP`, `40,58 %` des `8 900` serveurs multi-versions modifiant silencieusement description, paquets ou destination sous identifiants inchangés, et `4,16 %` (`370` serveurs) redirigeant leur point de terminaison distant.
  - *Verdict final : supporté*
- **D-03 (`L93`) — `SPIFFE` (`SRC-046`, `[14]`)** : vérification directe contre `SRC-046.txt` (L8–79) : identité de charge de travail non humaine (`NHI`) éphémère sans co-déploiement de secret statique via l'`API Workload` et les `SVID`.
  - *Verdict final : supporté*
- **D-04 (`L93`) — Épinglage contre la dérive `MCP` (`SRC-057`, `[15]`)** :
  - *Constat initial* : imprécis — la retouche `G4` écrivait « épingle cryptographiquement l'empreinte des définitions, des paquets et des hôtes autorisés [15] », attribuant à `[15]` l'empreinte d'hôtes et de définitions alors que `SRC-057.txt` (§ 5.1, L769–772) recommande le versionnement des définitions d'outils et l'épinglage des hôtes de points de terminaison et des empreintes de paquets (*pinning of endpoint hosts and package digests*).
  - *Rectification appliquée (`L93`)* : « Face à la dérive silencieuse documentée par Kraishan [15], ce registre versionne les définitions d'outils et épingle cryptographiquement leurs empreintes, celles des paquets ainsi que les hôtes autorisés. »
  - *Verdict final : supporté*
- **D-05 (`L97`) — Passerelle manquante, `MCP` (`SRC-038`, `[11]`) et `BSIF B-10` (`SRC-068`, `[16]`)** :
  - *Constat initial* : imprécis — la formulation `G4` « expose des appels d'outils `MCP` hétérogènes [11] » accolait l'adjectif « hétérogènes » à la citation du standard `MCP` (`SRC-038.txt`, L30, L46, L161–169), lequel fournit une intégration normalisée mais n'impose pas à lui seul le contrôle d'accès ni la médiation. La mention des plans de sortie exigés par `BSIF B-10` concorde avec `SRC-068.txt` (§ 2.3.5 L443–L461).
  - *Rectification appliquée (`L97`)* : « gère sans médiation uniforme ses appels d'outils `MCP` [11] ».
  - *Verdict final : supporté*
- **D-06 (`L99`) — Passerelle aval (`RFC 8693` `SRC-041` `[13]`, `MCP` `SRC-038` `[11]`, `A2A` `SRC-039` `[12]`)** : vérification directe contre `SRC-041.txt` (§ 1.1 L199–233, § 2.1, § 4.2, § 5 L863–869), `SRC-038.txt` (L46–88) et `SRC-039.txt` (§ 1.2 L1011 *Opaque Execution*, § 1.3 L1039–1043 *Canonical Data Model* / *Abstract Operations* / *Protocol Bindings*, App. B L6389).
  - *Verdict final : supporté*
- **D-07 (`L99`) — Routeur agnostique amont et `BSIF B-10` (`SRC-068`, `[16]`)** : vérification directe contre `SRC-068.txt` (`Cloud portability` L313, § 4.4 L557, Annex 1 L563–L601 ; `Concentration risk` L315, § 2.2.3 L311–L315 ; `Exit plan` `non-stressed` / `stressed` L323, § 2.3.5 L445–L453).
  - *Verdict final : supporté*
- **D-08 (`L105`) — Fragilité mémorielle (`SagaLLM` `SRC-006` `[4]`, `CoALA` `SRC-026` `[5]`)** : vérification directe contre `SRC-006.txt` (§ 2.2 L205–214, § 6 L1574–1579) et `SRC-026.txt` (§ 4.1 L516–518, § 6 L879).
  - *Verdict final : supporté*
- **D-09 (`L105`) — Taxonomie `CoALA` (`SRC-026`, `[5]`)** :
  - *Constat initial* : imprécis — la retouche `G4` « Suivant la taxonomie cognitive `CoALA` établie par Sumers et ses coauteurs, ce plan dissocie strictement quatre registres externes [5] » prêtait à `CoALA` l'étiquette « registres externes », alors que `SRC-026.txt` (§ 4 L438–445, § 4.1 L476–480, § 6 L944–958) qualifie ces quatre modules de mémoires *internes* de l'agent (extérieures au `LLM` sans état, mais opposées à l'environnement externe). Le verrouillage en lecture seule de la mémoire procédurale est conforme à § 6 L812–813.
  - *Rectification appliquée (`L105`)* : « quatre registres de mémoire hors modèle [5] ».
  - *Verdict final : supporté*
- **D-10 (`L105`) — Mémoire persistante `SagaLLM` (`SRC-006`, `[4]`)** : vérification directe contre `SRC-006.txt` (§ 2.2 L212–214, § 3.1.1 L381–389, § 3.1.2 L391–394, § 5.1 L1187) sur la conservation externe persistante des objectifs, justifications et graphe de dépendances.
  - *Verdict final : supporté*
- **D-11 (`L111`) — `Temporal` (`SRC-034`, `[7]`)** : vérification directe contre `SRC-034.txt` (L27, L82–90, L160–163, L177–186, L217–229) sur le rejeu déterministe depuis l'*Event History* après panne ou coupure réseau sans réexécuter les activités déjà validées.
  - *Verdict final : supporté*
- **D-12 (`L111`) — `CloudEvents v1.0.2` (`SRC-035`, `[8]`)** : vérification directe contre `SRC-035.txt` (L1, L5, L101, L158–160, L248–333, L416, L538–549) sur les attributs d'acheminement (`id`, `source`, `specversion`, `type`, `time`) dissociés de la charge utile chiffrée `data`.
  - *Verdict final : supporté*
- **D-13 (`L113`) — `OpenTelemetry GenAI` (`SRC-037`, `[10]`)** : vérification directe contre `SRC-037.txt` (L7 *Development*, L62 `gen_ai.agent.id` à la création, L188–197 `invoke_agent` / `invoke_workflow`, L236 `gen_ai.agent.name`, L244 `gen_ai.request.model`, L250–251 & L331–352 jetons facturés, L68 & L252 & L256 `Opt-In` pour `gen_ai.system_instructions` et `gen_ai.input.messages`, L362 & L425 protection `PII`).
  - *Verdict final : supporté*
- **D-14 (`L113`) — Supervision à la vitesse des machines (`SRC-002`, `[1]`)** : vérification directe contre `SRC-002.txt` (L1661–1691) sur les registres cryptographiquement intègres et les pistes d'audit normalisées nécessaires à l'imputabilité et à l'analyse des causes racines.
  - *Verdict final : supporté*
- **D-15 (`L129`) — Ligne « Harnais 80/20 » du tableau comparatif (`[4]`, `[5]`, `[6]`)** : vérification directe contre `SRC-026.txt` (L829–831), `SRC-006.txt` (L877) et `SRC-033.txt` (transactions compensatoires).
  - *Verdict final : supporté*

---

## Contrôle différentiel post-lissage G5

- **Date et portée** : 2026-11-22 — Audit différentiel indépendant `auditeur-wyvern` (`git diff HEAD` depuis `fe6e945`) sur `ch04` (`36` éléments différentiels contrôlés : `22` lignes de retrait mécanique de rétro-apostrophes vérifiées exactes sur sigles/identifiants et `14` blocs substantiels `L5`, `L19`, `L43`, `L49`, `L51`, `L63`, `L81`, `L91`, `L99`, `L105`, `L111`, `L113`, `L126–L127`, `L126–L127`).
- **Primaires `L+` vérifiés** : `SRC-002.txt` (`[1]`), `SRC-006.txt` (`[4]`), `SRC-026.txt` (`[5]`), `SRC-034.txt` (`[7]`), `SRC-035.txt` (`[8]`), `SRC-036.txt` (`[9]`), `SRC-037.txt` (`[10]`), `SRC-038.txt` (`[11]`), `SRC-039.txt` (`[12]`), `SRC-041.txt` (`[13]`), `SRC-046.txt` (`[14]`), `SRC-057.txt` (`[15]`), `SRC-068.txt` (`[16]`), ainsi que `sources/ch04-sources.md` et le renvoi au chapitre 08 (`L19`, `L103`).
- **Rectifications appliquées dans le manuscrit (`5`)** :
  1. `L49` (`SPIFFE` `SRC-046.txt`, `OpenTelemetry` `SRC-037.txt`) : retiré le qualificatif « locale » absent de `SRC-046.txt` devant `API Workload`, rétabli « document éphémère » (contre le rejeu de jetons) et « sous un attribut stable tel que `gen_ai.agent.id` ».
  2. `L51` (`RFC 8693` `SRC-041.txt` § 4.4, `Kraishan` `SRC-057.txt` § 4.1.1) : rétabli « sur le jeton présenté » pour `may_act` et la disjonction explicite (« soit une autorité ambiante, soit un transfert direct de jetons ») dont la seconde seule efface la trace en aval.
  3. `L63` (`Temporal` `SRC-034.txt` L160) : rétabli la démarcation « ou, pour un agent, inférence LLM » afin de ne pas attribuer l'exemple LLM à la documentation `Temporal` `[7]`.
  4. `L81` (`Idempotency-Key` `SRC-036.txt` § 2.2, § 2.4) : rétabli le caractère recommandé de l'UUID aléatoire à haute entropie et optionnel côté ressource (`MAY`) de l'empreinte de charge utile.
  5. `L113` (`OpenTelemetry GenAI` `SRC-037.txt` L62/L236, `Tomašev et al.` `SRC-002.txt` L1678–1683) : rétabli la distinction `gen_ai.agent.id` (création) vs `gen_ai.agent.name` (invocation) et dissocié les spans `OpenTelemetry` `[10]` des registres cryptographiquement intègres et pistes d'audit normalisées exigés par `[1]`.
- **Verdict différentiel final post-G5** : `36 / 36` items (`100 %` `supporté`), **`0` imprécis résiduel**, **`0` non supporté résiduel**, aucun tableau ajouté ni supprimé, aucune collision `CA-03` ni motif `CA-02`.

---

## Réindexation différentielle post-audit v1.3 (2 décembre 2026)

- **Périmètre `v1.3`** : `manuscrit/02 - Partie II/Chapitre 04 - Posseder le noyau de controle 80-20.md` (`145` lignes, `5 749` mots `G1` / `5 921` `split()`), `18` sources `L+`.
- **Permutation `Fig-07` / `Fig-08` et réancrages vérifiés** :
  - `L63–L69` (`A-37`) : la figure 7 (`Fig-07.svg`) porte désormais l'anatomie du harnais d'agent 80/20 en huit étapes autour de l'inférence probabiliste (`§ 4.3`). `Verdict : supporté`.
  - `L113–L119` (`A-55`) : la figure 8 (`Fig-08.svg`) porte l'architecture cible en quatre plans séparant `SoE`, noyau possédé et modèles substituables (`§ 4.4`), suivie du `Tableau 4.1` (`L121–L131`). `Verdict : supporté`.
  - Mise à jour des sources révisées `SRC-037.txt` (`OpenTelemetry GenAI SemConv`, `[10]`, l. 7, 61–64, 640), `SRC-038.txt` (`MCP` complet, `[11]`, l. 45, 88–99, 411, 5002) et `SRC-068.txt` (`B-10`, `[16]`, l. 399–445). `Verdict : supporté`.
