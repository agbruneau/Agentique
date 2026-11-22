# Audit d'ancrage atomique — Chapitre 05 (`ch05`)

- **Unité** : `ch05`
- **Manuscrit vérifié** : [Chapitre 05 - Connecter sans s enfermer.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/manuscrit/02%20-%20Partie%20II/Chapitre%2005%20-%20Connecter%20sans%20s%20enfermer.md)
- **Dossier de sources** : [ch05-sources.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/sources/ch05-sources.md)
- **Registres vérifiés** : [ancres-chronologiques.json](file:///c:/Github/Agentique/7%20-%20Livre%202027/registre/ancres-chronologiques.json), [faits-empiriques.json](file:///c:/Github/Agentique/7%20-%20Livre%202027/registre/faits-empiriques.json), [glossaire-termes.json](file:///c:/Github/Agentique/7%20-%20Livre%202027/registre/glossaire-termes.json)
- **Date de gel des faits** : 31 décembre 2026
- **Auditeur indépendant** : `auditeur-wyvern` (barrière `G2` — `CA-10`, `CA-12`, régime Production)

## Bilan synthétique final

- Total d'affirmations atomiques actives : 63
- Verdict final — supportés : 63 (100 %)
- Verdict final — imprécis résiduels : 0
- Verdict final — non supportés résiduels : 0
- Constats initiaux avant rectification : 42 supporté, 21 imprécis (tous rectifiés dans le manuscrit), 0 non supporté.

---

## Détail paragraphe par paragraphe

### Titre, Question directrice, Scénario illustratif et Ouverture (lignes 1–11)

- **`A-05-01`** (Lignes 5–9 — *Scénario illustratif* : assise technique `MCP` / `JSON-RPC` et silos)
  - *Affirmation* : Le scénario illustratif (explicitement posé comme fictionnel via « *Scénario illustratif.* Imaginons... ») s'appuie sur le transport `JSON-RPC` de `MCP`, le coût d'attention des centaines de schémas injectés dans le contexte et le risque de silos fermés déjà examiné au Chapitre 03.
  - *Vérification* : `ch05-sources.md` `[7]`, `SRC-038.txt` (l. 54, 73 : `JSON-RPC 2.0`), `SRC-057.txt` (l. 91–92 : injection des descriptions dans le contexte), `SRC-004.txt` (l. 427–429 : *lock-in* des plateformes).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-02`** (Ligne 11 — Thèse quadripartite du chapitre)
  - *Affirmation* : L'interopérabilité durable dissocie la médiation verticale vers les outils, la délégation horizontale et événementielle entre domaines opaques, la gouvernance sémantique du sens métier et la protection des mémoires comme du patrimoine transactionnel.
  - *Vérification* : `registre/glossaire-termes.json` (`interopérabilité verticale et horizontale`, `couche sémantique métier`, `couche anti-corruption`), `SRC-038.txt`, `SRC-039.txt` (Annexe B), `SRC-035.txt`, `SRC-026.txt`, `SRC-033.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 5.1 — Connectivité verticale aux outils (`MCP`)

#### Paragraphe 1 (Ligne 15 — Définition et rôles `MCP`)

- **`A-05-03`** (Ligne 15)
  - *Affirmation* : La révision du 25 novembre 2025 de `MCP` répond à un besoin d'économie d'intégration, là où le raccordement d'un LLM aux sources documentaires et interfaces applicatives exigeait auparavant des intégrations particulières.
  - *Vérification* : `ch05-sources.md` `[7]` (`MCP-SPEC-2025-11-25`) et `SRC-038.txt` (l. 27–31, 66–67).
  - Constat initial : imprécis (l'énoncé initial « chaque application dotée d'un grand modèle de langage maintenait des adaptateurs propriétaires pour chaque source documentaire et chaque interface applicative » généralisait de façon excessive sans appui direct dans `SRC-038.txt`). Rectifié en « raccorder un grand modèle de langage à des sources documentaires ou à des interfaces applicatives exigeait des intégrations particulières ».
  - Verdict final : supporté.

- **`A-05-04`** (Ligne 15)
  - *Affirmation* : Inspiré du *Language Server Protocol* (`LSP`), `MCP` définit un protocole fondé sur `JSON-RPC 2.0` et des sessions avec maintien d'état entre trois rôles (`Host`, `Client`, `Server`).
  - *Vérification* : `SRC-038.txt` (l. 54–75 : `JSON-RPC 2.0`, `Hosts`, `Clients`, `Servers`, `Language Server Protocol`, `Stateful connections`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-05`** (Ligne 15)
  - *Affirmation* : Les serveurs `MCP` exposent `Resources`, `Prompts` et `Tools`, et peuvent demander aux clients `Sampling`, `Roots` et `Elicitation`.
  - *Vérification* : `SRC-038.txt` (l. 81–95).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 2 (Ligne 17 — Maturité et limites de sécurité de `MCP`)

- **`A-05-06`** (Ligne 17)
  - *Affirmation* : À la date de gel du 31 décembre 2026, le registre public `MCP` ne remonte qu'à septembre 2025.
  - *Vérification* : `SRC-057.txt` (l. 142 : « publication dates spanning September 2025 to August 2026 » ; l. 400 : « earliest version record ... dates to September 2025 »).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-07`** (Ligne 17)
  - *Affirmation* : Le corpus ouvert `L+` retenu ne renferme aucune étude empirique évaluée par les pairs mesurant la fiabilité ou les coûts d'exploitation de `MCP` en production bancaire ou industrielle.
  - *Vérification* : `ch05-sources.md` (`[7]` spécification non évaluée par les pairs ; `[13]` prépublication arXiv non évaluée par les pairs sur le registre public) et `registre/faits-empiriques.json` (aucun fait sur la fiabilité ou les coûts d'exploitation de `MCP` en production).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-08`** (Ligne 17)
  - *Affirmation* : La spécification `MCP` énonce que les outils représentent une capacité d'exécution arbitraire, que leurs descriptions et annotations doivent être considérées comme non fiables (*untrusted*) hors serveur de confiance, que l'hôte doit recueillir le consentement explicite de l'utilisateur avant toute invocation et que le protocole lui-même ne peut pas imposer ces garanties.
  - *Vérification* : `SRC-038.txt` (l. 135–142, 161).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 3 (Ligne 19 — Anti-patron *Swagger-to-MCP*)

- **`A-05-09`** (Ligne 19)
  - *Affirmation* : Le raccourci *Swagger-to-MCP* projette un pour un chaque point de terminaison `REST` ou procédure distante en outil `MCP`, confondant le développeur humain hors ligne avec un agent qui charge signatures et descriptions dans son contexte pour choisir ses actions à l'exécution.
  - *Vérification* : `SRC-057.txt` (l. 91–92 : « the client forwards tool descriptions into the model's context »), `SRC-026.txt` (l. 873–877).
  - Constat initial : imprécis (« de nombreuses équipes appliquent... » avançait une fréquence d'adoption non mesurée dans les sources). Rectifié en présentation du raccourci mécanique *Swagger-to-MCP* sans quantification empirique.
  - Verdict final : supporté.

#### Paragraphe 4 (Ligne 21 — Coûts d'espace d'actions et sous-documentation des sorties)

- **`A-05-10`** (Ligne 21)
  - *Affirmation* : La comparaison contrôlée entre convertisseurs automatiques et façades dédiées relève encore, fin 2026, d'une déduction d'ingénierie plutôt que d'une mesure publiée.
  - *Vérification* : `ch05-sources.md` et `registre/faits-empiriques.json` (aucune étude comparative contrôlée *Swagger-to-MCP* vs `ACI`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-11`** (Ligne 21)
  - *Affirmation* : Dans `CoALA` (*Transactions on Machine Learning Research*), Sumers *et al.* soulignent qu'un espace d'actions étendu complique directement la décision de l'agent et recommandent de n'exposer que le plus petit espace d'actions nécessaire à la tâche.
  - *Vérification* : `SRC-026.txt` (l. 1, 873–877) et `ch05-sources.md` `[4]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-12`** (Ligne 21)
  - *Affirmation* : Sur `AgentDojo`, Debenedetti *et al.* montrent que la sous-documentation des structures de sortie d'API constitue la première cause d'échec de `CaMeL` sur la suite voyage : `13` des `20` tâches bénignes échouent avec `Claude 3.5 Sonnet` faute de schéma de retour permettant de rédiger l'analyse avant exécution.
  - *Vérification* : `SRC-007.txt` (§ 6.1.2, l. 622–624, 683–690 ; Table 1, l. 716–760 : `13` `Underdocumented API` sur `20` tâches Travel, `5` correctes soit `25 %`) et `ch05-sources.md` `[3]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-13`** (Ligne 21)
  - *Affirmation* : Dans `multi-CaMeL`, Peters-Gill *et al.* doivent d'abord enrichir l'ensemble des descriptions d'outils avec leurs schémas de retour complets avant de pouvoir évaluer le système, et relèvent sur `AssetOpsBench` un défaut de substitution non contrôlée de portée (*unchecked scope substitution*) : lorsqu'une donnée manque pour l'actif ou la plage temporelle demandée, un sous-agent renvoie des données d'un périmètre voisin sans que l'agent parent pré-planifié détecte la violation de contrainte.
  - *Vérification* : `SRC-056.txt` (§ V, l. 701–715 ; § V-C2, l. 1130–1137) et `ch05-sources.md` `[12]`.
  - Constat initial : imprécis (le texte initial disait « compléter manuellement » — absent de `SRC-056.txt` — et écrivait « l'outil renvoie des données d'un périmètre voisin sans lever d'erreur », alors que `SRC-056.txt` § V-C2 attribue ce renvoi à un sous-agent et le défaut de détection au programme pré-planifié du parent). Rectifié fidèlement à § V et § V-C2.
  - Verdict final : supporté.

#### Paragraphe 5 et liste des cinq disciplines `ACI` (Lignes 23–29)

- **`A-05-14`** (Lignes 23–29)
  - *Affirmation* : Les cinq disciplines `ACI` sont alignées sur la partition `80/20` du Chapitre 04, déclarent un schéma de sortie complet et documenté conformément aux leçons de `CaMeL` et `multi-CaMeL` (l'`ACI` proscrivant les paramètres libres et paginant les retours volumineux), refusent la substitution silencieuse de portée (`[12]`), séparent consultation/simulation/mutation (Ch. 08) et minimisent l'espace d'actions actif (`[4]`).
  - *Vérification* : `registre/glossaire-termes.json` (`partition 80/20`), `SRC-007.txt` (l. 683–690), `SRC-056.txt` (l. 709–715, 1130–1137), `SRC-026.txt` (l. 877).
  - Constat initial : imprécis (la rédaction initiale « Conformément aux leçons de CaMeL et de multi-CaMeL [3, 12], chaque outil déclare son schéma JSON de sortie, proscrit les paramètres libres et pagine côté serveur... » pouvait attribuer le format JSON et la pagination serveur à `[3, 12]`). Rectifié en scindant la leçon de `[3, 12]` (schéma de sortie complet et documenté) et la discipline propre de l'`ACI`.
  - Verdict final : supporté.

#### Paragraphe 6 (Ligne 31 — Recensement Kraishan, prévalence)

- **`A-05-15`** (Ligne 31)
  - *Affirmation* : Obada Kraishan a réalisé en août 2026 (prépublication de septembre 2026) le premier recensement exhaustif du registre public `MCP` : `21 643` serveurs, `72 606` versions depuis septembre 2025, code source de `14 353` serveurs (`13 051` dépôts, `248 817` fichiers) et étalonnage sur `414` cas annotés manuellement (`294` alertes signalées et `120` fichiers non signalés).
  - *Vérification* : `SRC-057.txt` (l. 7, 12–15, 43, 46–52, 141–142, 196–197, 293–297 ; Table 3, l. 405–429).
  - Constat initial : imprécis (« 414 constats annotés manuellement » omettait que 120 des 414 cas étaient des fichiers non signalés servant à estimer le taux d'omission en § 3.4). Rectifié pour détailler `294` alertes et `120` fichiers non signalés.
  - Verdict final : supporté.

- **`A-05-16`** (Ligne 31)
  - *Affirmation* : `15,2 %` des serveurs scannés (`2 183` sur `14 353`) présentent au moins une alerte et `11,1 %` une alerte de sévérité élevée (`~7,6 %` après correction statistique de précision).
  - *Vérification* : `SRC-057.txt` (l. 16–17, 62–64, 471–478).
  - Constat initial : imprécis (« Un serveur scanné sur sept (15,2 %) » donnait une fraction approximative absente de `SRC-057.txt`, où 15,21 % dépasse 1/7 = 14,29 %). Rectifié en « `15,2 %` des serveurs scannés (`2 183` sur `14 353`) ».
  - Verdict final : supporté.

- **`A-05-17`** (Ligne 31)
  - *Affirmation* : L'exposition réseau sans authentification domine (`9,57 %` observé, `6,83 %` corrigé : écoute sur toutes les interfaces, `CORS` ouvert ou authentification désactivée), devant les dépendances non épinglées (`2,96 %` observé, `2,75 %` corrigé), les requêtes sortantes non validées de type `SSRF` (`1,33 %` observé, `0,95 %` corrigé) et le transfert aveugle de jetons appelants (`0,68 %` observé, `0,54 %` corrigé à `0,79` de précision).
  - *Vérification* : `SRC-057.txt` (Table 2, l. 321–325 ; Table 4, l. 430–465 ; § 4.1, l. 474–478).
  - Constat initial : imprécis (la formulation antérieure « devant les dépendances non épinglées ... et le transfert aveugle de jetons » omettait le 3e rang en Table 4, `Unvalidated fetch / SSRF` à `1,33 %` brut / `0,95 %` corrigé). Rectifié pour respecter l'ordre exact de la Table 4.
  - Verdict final : supporté.

- **`A-05-18`** (Ligne 31)
  - *Affirmation* : Les serveurs utilisant l'ancien transport `SSE` déprécié affichent `44,2 %` d'alertes graves contre `12,3 %` en HTTP diffusion (*streamable HTTP*).
  - *Vérification* : `SRC-057.txt` (§ 4.1, l. 486–487 : `44.2% (136 of 308) against 12.3% for streamable HTTP`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 7 (Ligne 33 — Recensement Kraishan, dérive silencieuse et prédicteurs)

- **`A-05-19`** (Ligne 33)
  - *Affirmation* : Sur les `8 900` serveurs multi-versions (`37 160` transitions), `51,1 %` ont modifié ce qu'ils annoncent entre deux publications, `40,6 %` ont opéré un changement sémantique silencieux sans changer d'identifiant, et `370` serveurs (`4,2 %`) ont redirigé leur point d'accès distant vers un autre hôte sous le même nom de registre — trace observable d'un *rug pull*, bien que nombre de cas relèvent de migrations ordinaires.
  - *Vérification* : `SRC-057.txt` (l. 18–21, 552–559, 630–632).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-20`** (Ligne 33)
  - *Affirmation* : Le délai médian avant la première modification est de `0` jour (`1` jour entre versions modifiées), et les serveurs affectés par une dérive silencieuse affichent un rapport de cotes de `2,96` (IC `95 %` `[2,56, 3,42]`) de contenir une alerte de sévérité élevée.
  - *Vérification* : `SRC-057.txt` (§ 4.2, l. 636–641 : `2.96 times the odds of a high-severity finding`).
  - Constat initial : imprécis (disait « faiblesse critique » alors que les trois bandes de gravité de Kraishan sont `high`, `medium`, `low`). Rectifié en « alerte de sévérité élevée ».
  - Verdict final : supporté.

- **`A-05-21`** (Ligne 33)
  - *Affirmation* : Le registre ne versionne aucune des `69 027` définitions d'outils extraites du code, si bien qu'une altération de description injectée dans le contexte du modèle échappe au modèle de données du registre.
  - *Vérification* : `SRC-057.txt` (l. 144–145, 204, 212–214, 763–765).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-22`** (Ligne 33)
  - *Affirmation* : Les étoiles GitHub offrent une protection faible (`OR = 0,78` par unité logarithmique), annulée par la taille du code (`OR = 1,94`) et l'ancienneté du dépôt (`OR = 1,38`).
  - *Vérification* : `SRC-057.txt` (l. 70, 701–705 ; Table 6, l. 712–729).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 8 (Ligne 35 — Passerelle de médiation `MCP`)

- **`A-05-23`** (Ligne 35)
  - *Affirmation* : Prescription d'une passerelle de médiation `MCP` possédée avec registre interne épinglé assurant quatre verrous déterministes (épinglage cryptographique d'intégrité, validation stricte `ACI`, rejet du transfert passif de jetons au profit de la délégation du Ch. 07, enregistrement vers le double couloir du Ch. 09), sur la base du recensement `[13]`.
  - *Vérification* : `SRC-057.txt` (§ 5.1–5.2, l. 769–780) et `registre/glossaire-termes.json` (`dérive silencieuse d'outil`, `télémétrie à double couloir`).
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 5.2 — Délégation horizontale (`A2A`) et bus d'événements (`CloudEvents`)

#### Paragraphes 1–2 (Lignes 39–41 — Périmètre et complémentarité `A2A` / `MCP`)

- **`A-05-24`** (Ligne 39)
  - *Affirmation* : La spécification *Agent2Agent* (`A2A`), hébergée par la *Linux Foundation*, couvre le palier horizontal de collaboration avec des domaines autonomes sans qu'ils exposent leur mécanisme interne.
  - *Vérification* : `ch05-sources.md` `[8]` (`Linux Foundation / A2A Project`) et `SRC-039.txt` (l. 975, 1011, 6389).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-25`** (Ligne 41)
  - *Affirmation* : L'annexe comparative d'`A2A` distingue `MCP` (le « comment faire » vertical vers outils/ressources) d'`A2A` (le « comment déléguer » horizontal entre pairs opaques), un serveur `A2A` pouvant utiliser `MCP` en coulisse sans dévoiler ses outils internes.
  - *Vérification* : `SRC-039.txt` (`Appendix B. Relationship to MCP`, l. 6383–6393).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 3 (Ligne 43 — Architecture et mécanismes `A2A 1.0.0`)

- **`A-05-26`** (Ligne 43)
  - *Affirmation* : Dans sa version `1.0.0`, `A2A` s'organise en trois couches : modèle de données canonique en `Protocol Buffers` (`Task`, `Message`, `AgentCard`, `Part`, `Artifact`, extensions), opérations abstraites (`SendMessage`, `SendStreamingMessage`, `GetTask`, `ListTasks`, `CancelTask`, `SubscribeToTask`, gestion des notifications push par *webhook*) et trois liaisons équivalentes (`JSON-RPC 2.0`, `gRPC`, `HTTP+JSON/REST`).
  - *Vérification* : `SRC-039.txt` (l. 961, 1015–1057, 1125–1657, 3297–3358, 4491–5489).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-27`** (Ligne 43)
  - *Affirmation* : La découverte passe par l'`AgentCard` JSON (`/.well-known/agent-card.json` ou catalogue curé, avec variante étendue réservée aux clients authentifiés), signable en `JWS` (`RFC 7515`) après canonisation `JCS` (`RFC 8785`).
  - *Vérification* : `SRC-039.txt` (§ 8.2, l. 4169–4177 ; § 3.1.11 / § 13.3, l. 1621, 5879 ; § 8.4, l. 4205–4380).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-28`** (Ligne 43)
  - *Affirmation* : `A2A` est conçu pour des tâches longues asynchrones (avec mode bloquant par défaut ou retour immédiat via `returnImmediately`), selon un cycle d'états incluant `TASK_STATE_AUTH_REQUIRED`, la diffusion continue par *Server-Sent Events* et les *webhooks* durcis contre les attaques `SSRF` par rejet des adresses IP privées.
  - *Vérification* : `SRC-039.txt` (§ 3.2.2, l. 1716–1727 ; § 3.3.3, l. 1928–1931 ; § 4.1.3, l. 2273 ; § 3.5.2 / § 9 / § 11 ; § 13.2, l. 5839–5844).
  - Constat initial : imprécis (affirmait « l'exécution est asynchrone par défaut », en contradiction directe avec § 3.2.2 l. 1723 : « Operations are blocking by default » lorsque `return_immediately` est faux ou omis). Rectifié en précisant que le protocole est conçu pour des tâches longues asynchrones avec mode bloquant par défaut ou retour immédiat via `returnImmediately`.
  - Verdict final : supporté.

- **`A-05-29`** (Ligne 43)
  - *Affirmation* : `A2A` porte un identifiant de routage multi-locataires (`tenant`) recopié dans les requêtes lorsqu'il est déclaré sur l'interface, et exige le chiffrement `TLS` (`1.3+` recommandé) en production.
  - *Vérification* : `SRC-039.txt` (§ 3.1.3, l. 1205 ; § 4.4.6, l. 2841 ; § 8.3.2, l. 4203 ; § 7.1 & § 13.4, l. 4051, 5921–5923).
  - Constat initial : imprécis (mentionnait un « identifiant de cloisonnement multi-locataires (tenant) vérifié dans les messages », alors que la spécification le définit comme identifiant de routage opaque recopié par le client et interprété par le serveur). Rectifié pour refléter la sémantique exacte de § 4.4.6 et § 8.3.2.
  - Verdict final : supporté.

#### Paragraphe 4 (Ligne 45 — `CloudEvents v1.0.2`)

- **`A-05-30`** (Ligne 45)
  - *Affirmation* : `CloudEvents v1.0.2` (CNCF) dissocie les attributs de contexte obligatoires (`id`, `source`, `specversion`, `type` — recommandé avec préfixe DNS inversé) et optionnels (`datacontenttype`, `dataschema`, `subject`, `time`) de la charge utile `data`, permettant le routage en mode structuré `JSON` ou en mode binaire sur `HTTP`, `AMQP`, `MQTT` ou `Kafka` sans désérialiser le contenu applicatif.
  - *Vérification* : `SRC-035.txt` (l. 1, 35, 129–138, 158–160, 244–429, 472–475) et `ch05-sources.md` `[15]`.
  - Constat initial : imprécis (« `type` préfixé en DNS inversé » confondait recommandation `SHOULD` et attribut `REQUIRED`, et « format JSON » ne distinguait pas explicitement le mode structuré). Rectifié en « `type` — recommandé avec préfixe DNS inversé » et « en mode structuré `JSON` ou en mode binaire ».
  - Verdict final : supporté.

- **`A-05-31`** (Ligne 45)
  - *Affirmation* : `CloudEvents` fixe un seuil minimal de transfert garanti à `64 Ko` par les intermédiaires et recommande de placer dans `data` un lien résolu sur demande plutôt que des documents volumineux, préservant un contrôle d'accès différencié et une divulgation sélective.
  - *Vérification* : `SRC-035.txt` (`Size Limits`, l. 510–525).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphes 5–6 et Figure 09 (Lignes 47–53)

- **`A-05-32`** (Lignes 47–53)
  - *Affirmation* : Description de la Figure 09 (règle de passage unique par l'enveloppe déterministe, rejet du *Swagger-to-MCP* du scénario introductif, enchaînement `MCP`/`ACI`, couche sémantique, validateur décimal exact, `ACL`, `CloudEvents` et passerelle `A2A`).
  - *Vérification* : `registre/glossaire-termes.json` (`interopérabilité verticale et horizontale`, `couche sémantique métier`, `couche anti-corruption`), `SRC-038.txt`, `SRC-039.txt`, `SRC-035.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 7 et quatre exigences de gouvernance (Lignes 55–60)

- **`A-05-33`** (Ligne 55)
  - *Affirmation* : Tout comme `MCP`, `A2A` reste jeune et sans mesure publiée de tenue en production à la date de gel du 31 décembre 2026.
  - *Vérification* : `ch05-sources.md` (`[8]` spécification de juin 2026 sans étude empirique de production) et `registre/faits-empiriques.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-34`** (Ligne 57 — Exigence 1)
  - *Affirmation* : À la section `7.6.4`, `A2A` stipule qu'il ne définit ni la portée, ni la représentation, ni la durée de validité, ni la révocation des autorisations associées à `TASK_STATE_AUTH_REQUIRED`, justifiant en finance l'usage de `OAuth 2.0 Rich Authorization Requests` (`RFC 9396`, champ `authorization_details`) et de la chaîne cryptographique d'identité du Ch. 07.
  - *Vérification* : `SRC-039.txt` (§ 7.6.4, l. 4151–4156) et `SRC-042.txt` (l. 15–16, 162–204).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-35`** (Ligne 58 — Exigence 2)
  - *Affirmation* : Dans `A2A` (§ 3.3.1), la déduplication par `messageId` reste optionnelle (`MAY`) sans saga compensatoire transversale ; `CloudEvents` fournit `(source, id)` sans orchestrer l'idempotence d'exécution ni prévenir les boucles d'écho ; la passerelle doit donc imposer `Idempotency-Key` à empreinte vérifiée (`HTTP 422`) et les sagas durables du Ch. 06.
  - *Vérification* : `SRC-039.txt` (§ 3.3.1, l. 1810), `SRC-035.txt` (l. 251–254), `SRC-036.txt` (§ 2.4, § 2.7 l. 446–447), `SRC-033.txt`, `SRC-006.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-36`** (Ligne 59 — Exigence 3)
  - *Affirmation* : La section *Privacy and Security* de `CloudEvents v1.0.2` avertit que les attributs de contexte voyagent en clair et peuvent être inspectés et journalisés par tout intermédiaire, le chiffrement de `data` demeurant à la charge des parties.
  - *Vérification* : `SRC-035.txt` (`Privacy and Security`, l. 527–549).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-37`** (Ligne 60 — Exigence 4, thèse de *Can CaMeLs Talk?*)
  - *Affirmation* : Dans `Can CaMeLs Talk?` (octobre 2026), James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov et Christian Schroeder de Witt démontrent que l'isolation individuelle par `CaMeL` ne protège pas le collectif lors de délégations en raison du « blanchiment de frontière » (*boundary laundering*), où une injection contenue dans les données d'un agent amont est réécrite dans l'instruction confiée à un agent aval.
  - *Vérification* : `SRC-056.txt` (l. 1–38, 105, 184–224, 477–490) et `ch05-sources.md` `[12]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-38`** (Ligne 60 — Exigence 4, mesures sur `MultiAgentDojo`)
  - *Affirmation* : Sur `MultiAgentDojo` (`949` instances d'attaque par modèle), le taux moyen de succès d'attaque passe de `12,9 %` sans défense à `0,2 %` avec isolation individuelle (`0,5 %` sur `GPT-4.1`, `0,4 %` sur `Gemini 2.5 Pro`), et ne tombe à `0,0 %` qu'avec `multi-CaMeL` qui sépare physiquement le canal des instructions fiables d'un canal de variables opaques conservant leur provenance.
  - *Vérification* : `SRC-056.txt` (Table III, l. 968–1014 ; § V-B, l. 1031–1060 ; § IV, l. 564–667).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-39`** (Ligne 60 — Exigence 4, représentation dans `A2A`)
  - *Affirmation* : Bien qu'`A2A` distingue dans ses unités `Part` les champs `text` et `data` (anciennement `TextPart` et `DataPart`), imposer cette séparation de provenance à la passerelle incombe entièrement à l'architecte.
  - *Vérification* : `SRC-039.txt` (§ 4.1.6, l. 2341–2385 ; Annexe A.2.1, l. 6240–6261).
  - Constat initial : imprécis (mentionnait uniquement les anciens noms `TextPart` et `DataPart` de v0.3.x sans citer l'objet `Part` unifié et ses champs `text`/`data` de la v1.0.0). Rectifié pour refléter la v1.0.0 tout en rappelant les dénominations héritées.
  - Verdict final : supporté.

#### Tableau de répartition contractuelle (Lignes 62–69)

- **`A-05-40`** (Lignes 62–69)
  - *Affirmation* : Le tableau synthétise sans dérive les capacités, manques de gouvernance et garde-fous pour les quatre couches (`MCP`, `A2A`, `CloudEvents`, couche sémantique/`ACL`), avec toutes les références `[7, 8, 12, 13, 15]` conformes au corps de section.
  - *Vérification* : `SRC-038.txt`, `SRC-057.txt`, `SRC-039.txt`, `SRC-056.txt`, `SRC-035.txt`, `ch05-sources.md`.
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 5.3 — Dette sémantique, contrats de données et bilan de littérature

#### Paragraphe 1 (Ligne 73 — Axiome du Liminaire et exemples sémantiques)

- **`A-05-41`** (Ligne 73)
  - *Affirmation* : Rappel de l'axiome directeur du Liminaire selon lequel on n'orchestre durablement que ce qui est interopérable et sémantiquement aligné, illustré par la différence entre transfert syntaxique `JSON` valide et sens métier univoque.
  - *Vérification* : `registre/glossaire-termes.json` (`tissu conjonctif agentique`, `couche sémantique métier`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 2 (Ligne 75 — Modèle de triple dette de Storey)

- **`A-05-42`** (Ligne 75)
  - *Affirmation* : En mars 2026, Margaret-Anne Storey formalise un modèle de triple dette en génie logiciel : dette technique (dans le code), dette cognitive (érosion de la compréhension partagée / « théorie du système » de Peter Naur) et dette d'intention (absence ou vieillissement des artefacts externes capturant objectifs, contraintes non fonctionnelles et justifications).
  - *Vérification* : `SRC-040.txt` (l. 14, 18–23, 48, 62–63, 70, 156–160, 168–171, 191, 215–221) et `ch05-sources.md` `[9]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-43`** (Ligne 75)
  - *Affirmation* : L'IA générative peut parfois réduire la dette technique apparente tout en accélérant les dettes cognitive et d'intention ; Storey rattache la « dette de contexte » (*context debt*) à la dette d'intention lorsque registres de décisions, `DDD`/langage ubiquitaire et spécifications `BDD` restent implicites ou périmés, conduisant les agents à produire des sorties syntaxiquement irréprochables qui ratent l'intention métier, optimisent de mauvais critères ou réclament des clarifications.
  - *Vérification* : `SRC-040.txt` (l. 29–30, 55, 160–161, 180–190, 198–206, 235–241).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 3 (Ligne 77 — Analyse économique de Shahidi *et al.*)

- **`A-05-44`** (Ligne 77)
  - *Affirmation* : Dans le document de travail `NBER` de novembre 2025, Peyman Shahidi, Gili Rusak, Benjamin S. Manning, Andrey Fradkin et John J. Horton analysent les limites d'articulation du mandant (*principal's articulation limits*) et les limites de synthèse de l'agent (*agent's synthesis limits*), montrant que dans des contextes à haute dimensionnalité, de minuscules imprécisions initiales se propagent et altèrent la décision finale.
  - *Vérification* : `SRC-004.txt` (l. 1–32, 328–347) et `ch05-sources.md` `[1]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-45`** (Ligne 77)
  - *Affirmation* : Un agent *bowling-shoe* fourni par une plateforme exploite directement ses signaux privilégiés et intégrations internes au prix d'un enfermement et d'un risque d'orientation vers les intérêts de la plateforme, contrairement à un agent *bring-your-own* sur API publiques.
  - *Vérification* : `SRC-004.txt` (l. 418–493, Table 2).
  - Constat initial : imprécis (l'expression « la sémantique privée de l'éditeur » ne figurait pas dans `SRC-004.txt`). Rectifié en « les signaux privilégiés et les intégrations internes de la plateforme ».
  - Verdict final : supporté.

#### Paragraphe 4 (Ligne 79 — Trois constats empiriques et normatifs)

- **`A-05-46`** (Ligne 79)
  - *Affirmation* : Dans l'évaluation originale de `CaMeL` sur `AgentDojo`, l'absence de schémas de retour documentés provoque `13` échecs sur `20` tâches bénignes de la suite voyage avec `Claude 3.5 Sonnet`, obligeant même les générations ultérieures de modèles à compenser en déléguant l'analyse des retours au modèle confiné `Q-LLM`.
  - *Vérification* : `SRC-007.txt` (§ 6.1.2, l. 683–690 ; Table 1, l. 716–760).
  - Constat initial : imprécis (« par du décodage auxiliaire » prêtait à confusion avec le décodage contraint, alors que `SRC-007.txt` l. 687 décrit le recours au `Q-LLM` pour parser les retours non documentés). Rectifié en « en déléguant l'analyse des retours au modèle confiné `Q-LLM` ».
  - Verdict final : supporté.

- **`A-05-47`** (Ligne 79)
  - *Affirmation* : Dans `multi-CaMeL`, Peters-Gill *et al.* documentent sur `AssetOpsBench` (`112` tâches retenues après retrait de `29` tâches irréalisables sur `141`) les échecs par substitution non contrôlée de portée : lorsqu'une donnée manque pour l'actif ou la plage de dates demandée, un sous-agent retourne des données voisines et l'orchestrateur pré-planifié poursuit son raisonnement sur un faux périmètre sans détecter la violation.
  - *Vérification* : `SRC-056.txt` (l. 746, 757–768, 1130–1137, 1881).
  - Constat initial : imprécis (omettait le total initial de `141` tâches et attribuait le mécanisme à « faute de contraintes de contrat univoques » plutôt qu'au fait que le programme pré-planifié ne détecte pas le changement de portée renvoyé par le sous-agent). Rectifié fidèlement au texte de `SRC-056.txt`.
  - Verdict final : supporté.

- **`A-05-48`** (Ligne 79)
  - *Affirmation* : La norme `RFC 9396` de l'IETF montre pourquoi de simples chaînes `scope` ne suffisent plus pour autoriser un virement précis et recourt à des objets JSON fortement typés (`authorization_details`), validables contre des schémas lisibles par machine (`JSON Schema`) et adossés à des espaces de noms par URI résistants aux collisions.
  - *Vérification* : `SRC-042.txt` (l. 95–108, 267–270, 1183–1189).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphes 5–6 (Lignes 81–88 — Bilan honnête et quatre actifs sémantiques)

- **`A-05-49`** (Ligne 81)
  - *Affirmation* : Au gel du 31 décembre 2026, aucune étude empirique contrôlée ni expérience randomisée dans le corpus ouvert consulté ne chiffre l'écart de fiabilité ou de ROI entre orchestration sur API brutes et orchestration adossée à une couche sémantique gouvernée ; la primauté de la sémantique est explicitement qualifiée de déduction architecturale étayée par `[9]`, `[3, 12]` et `[10]`.
  - *Vérification* : `ch05-sources.md` et `registre/faits-empiriques.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-50`** (Lignes 83–88)
  - *Affirmation* : Quatre actifs déterministes pour posséder la couche sémantique : ontologie et langage ubiquitaire gouvernés (`[9]`), couche métrique unifiée, contrats de données complets (`[3, 12]`) et artefacts d'intention versionnés (`[9]`).
  - *Vérification* : `SRC-040.txt`, `SRC-056.txt`, `SRC-007.txt`, `registre/glossaire-termes.json` (`couche sémantique métier`).
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 5.4 — Quatre mémoires (`CoALA`), conformité `Loi 25` et couches anti-corruption (`ACL`)

#### Paragraphes 1–6 (Lignes 96–105 — Taxonomie `CoALA` et défense des mémoires)

- **`A-05-51`** (Lignes 96–101)
  - *Affirmation* : Un modèle de langage pris seul demeure sans état (*stateless*) ; le cadre `CoALA` (Sumers, Yao, Narasimhan, Griffiths), issu des sciences cognitives et des architectures symboliques (dont `Soar` et la tradition d'Anderson et Lebiere / `ACT-R`), distingue mémoire de travail, mémoire épisodique, mémoire sémantique et mémoire procédurale (poids du modèle et code explicite déterministe).
  - *Vérification* : `SRC-026.txt` (l. 15–16, 186, 189, 476–518) et `ch05-sources.md` `[4]`.
  - Constat initial : imprécis (le sigle `ACT-R` provenait de la synthèse de `ch05-sources.md` `[4]` alors que `SRC-026.txt` cite nommément `Soar` et `Anderson and Lebiere, 2003`). Rectifié pour mentionner explicitement `Soar` et `Anderson et Lebiere / ACT-R`.
  - Verdict final : supporté.

- **`A-05-52`** (Ligne 103)
  - *Affirmation* : Dans l'exemple de Sumers *et al.*, l'agent a accès lecture/écriture à la mémoire épisodique et lecture seule sur les mémoires sémantique et procédurale ; écrire dans la mémoire procédurale comporte un danger élevé d'erreurs ou de détournement des intentions du concepteur ; la contrôlabilité distingue mémoire interne gouvernée et environnement externe non fiable.
  - *Vérification* : `SRC-026.txt` (l. 516–518, 810–813, 953–956).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-53`** (Ligne 105)
  - *Affirmation* : La taxonomie `NIST AI 100-2e2025` (mars 2025) documente l'empoisonnement des bases `RAG` par *PoisonedRAG* (réponses manipulées sur des requêtes ciblées) et *Phantom* (un seul document empoisonné induisant divers objectifs adverses), ainsi que les déclencheurs *Neural Exec* survivant au découpage en blocs (*chunking*) et au filtrage contextuel.
  - *Vérification* : `SRC-054.txt` (l. 2547–2548, 2642–2651).
  - Constat initial : imprécis (fusionnait *PoisonedRAG* et *Phantom* sous « où un seul document injecté manipule les réponses sur des requêtes ciblées »). Rectifié pour attribuer exactement les requêtes ciblées à *PoisonedRAG* et le document unique à *Phantom*.
  - Verdict final : supporté.

- **`A-05-54`** (Ligne 105)
  - *Affirmation* : Le `NIST` rappelle qu'aucun filtre ou détecteur actuel ne garantit l'immunité contre les injections indirectes sur sources non fiables et recommande le cloisonnement des privilèges entre modèles et des interfaces bien définies ; `A2A` (§ 13.1) prescrit que les contrôles d'autorisation s'exécutent avant toute requête en base susceptible de révéler l'existence de ressources hors portée.
  - *Vérification* : `SRC-054.txt` (l. 2706–2715) et `SRC-039.txt` (§ 13.1, l. 5819).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphes 7–9 et Figure 10 (Lignes 107–113 — Désapprentissage et `Loi 25`)

- **`A-05-55`** (Ligne 107)
  - *Affirmation* : Sumers *et al.* notent que la suppression sélective (« désapprentissage ») reste très peu étudiée chez les agents de langage ; tant le `NIST` que `Shahidi et al.` rappellent la difficulté technique du désapprentissage dans les poids d'un modèle, le `NIST` relevant des attaques par inversion capables d'extraire des données supposément effacées par des méthodes de désapprentissage.
  - *Vérification* : `SRC-026.txt` (l. 631–632), `SRC-054.txt` (l. 1771–1778, 2557–2561) et `SRC-004.txt` (l. 803–804).
  - Constat initial : imprécis (restreignait les attaques par inversion `[328]` au « désapprentissage approximatif » alors que `SRC-054.txt` l. 2561 évoque les « unlearning methods »). Rectifié en « par des méthodes de désapprentissage ».
  - Verdict final : supporté.

- **`A-05-56`** (Ligne 107)
  - *Affirmation* : La `Loi 25` (`LQ 2021, c. 25`) est en vigueur dès 2026 au Québec pour les traitements automatisés : l'article `12.1` impose d'aviser l'individu visé au plus tard lors de la communication d'une décision reposant entièrement sur un traitement automatisé de renseignements personnels, de divulguer sur requête les renseignements exploités, raisons et principaux facteurs/paramètres déterminants, de permettre de demander la rectification des données utilisées et de soumettre ses observations à un employé habilité à réviser la décision ; l'article `11` exige au moins un an de conservation suivant la décision ; l'article `23` impose la destruction ou l'anonymisation irréversible pour des fins sérieuses et légitimes après accomplissement des finalités ; les articles `90.12` et `91` plafonnent les sanctions administratives à `10 M$ CA` ou `2 %` du chiffre d'affaires mondial et les amendes pénales à `25 M$ CA` ou `4 %`.
  - *Vérification* : `SRC-063.txt` (l. 1499–1503, 1542–1555, 1777–1788, 2283–2287, 2328–2333, 2489–2525) et `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`).
  - Constat initial : imprécis (raccourcis sur l'étendue du droit de rectification — qui vise les renseignements personnels utilisés — et sur les conditions d'anonymisation de l'art. 23). Rectifié fidèlement aux articles 11, 12.1 et 23 de `SRC-063.txt` tout en évitant la collision 12-gramme avec les synthèses antérieures du dépôt (`CA-03`).
  - Verdict final : supporté.

- **`A-05-57`** (Lignes 109–113 — Figure 10)
  - *Affirmation* : Description du cloisonnement des quatre compartiments `CoALA`, du filtre d'accès en amont, du sas anti-empoisonnement en écriture et de la purge planifiée conforme à la `Loi 25`.
  - *Vérification* : `SRC-026.txt`, `SRC-054.txt`, `SRC-063.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphes 10–13 (Lignes 117–123 — Protection du patrimoine transactionnel par `ACL`)

- **`A-05-58`** (Ligne 119)
  - *Affirmation* : En 1987, Hector Garcia-Molina et Kenneth Salem montrent pourquoi les transactions de longue durée ne peuvent maintenir des verrous exclusifs sans dégrader la disponibilité et multiplier les interblocages ; Chang et Geng (`SagaLLM`) montrent que face aux perturbations temporelles, des modèles de pointe (`Claude 3.7`, `DeepSeek R1`, `GPT-4o`) perdent le contexte et réécrivent rétroactivement l'historique.
  - *Vérification* : `SRC-033.txt` (l. 160–226) et `SRC-006.txt` (l. 1359–1422, 1562–1581).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-59`** (Ligne 119)
  - *Affirmation* : Une `ACL` déterministe traduit les requêtes `ACI` en transactions locales brèves $T_1, \dots, T_n$ dotées de compensations $C_1, \dots, C_{n-1}$, et impose la clé d'idempotence en normalisation à l'IETF (`Idempotency-Key` en `UUID` aléatoire, couplée au client et à une empreinte de charge utile avec rejet `HTTP 422` si divergence et `HTTP 409` si concurrence).
  - *Vérification* : `SRC-033.txt` (l. 440–448), `SRC-006.txt` (l. 671), `SRC-036.txt` (§ 2.2, § 2.4, § 2.7 l. 446–470, § 5 l. 730–733), `registre/glossaire-termes.json` (`couche anti-corruption`, `clé d'idempotence transactionnelle`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-60`** (Ligne 121)
  - *Affirmation* : Les flottants binaires IEEE 754 introduisent des écarts d'arrondi incompatibles avec l'arithmétique décimale exacte des cœurs patrimoniaux ; suivant l'exemple explicite d'initiation de paiement de la norme `OAuth 2.0 Rich Authorization Requests` (`RFC 9396`, `"amount": "123.50"`, `"currency": "EUR"`), l'`ACL` valide et transporte exclusivement des types décimaux exacts.
  - *Vérification* : `SRC-042.txt` (l. 119–122, 192–195).
  - Constat initial : imprécis (présentait `RFC 9396` comme « norme financière » et invoquait la liaison REST d'`A2A` `[8]` comme modèle de chaînes décimales comptables, alors que § 11.5 d'`A2A` ne vise que les *query parameters* HTTP GET/DELETE). Rectifié en requalifiant `RFC 9396` et en supprimant la référence abusive à `[8]`.
  - Verdict final : supporté.

- **`A-05-61`** (Ligne 123)
  - *Affirmation* : La sortie technique du *screen scraping* s'impose pour quatre raisons : fragilité visuelle, absence de schéma de retour structuré (cause documentée dans `CaMeL` `[3]`), impossibilité d'appliquer `Idempotency-Key` `HTTP` (`[6]`), exposition aux injections indirectes (`[11]`) et mesures de blocage juridique, contractuel ou technique (contentieux, `robots.txt`, conditions restrictives, limitation de débit) relevées par Shahidi *et al.* (`[1]`).
  - *Vérification* : `SRC-007.txt` (§ 6.1.2), `SRC-036.txt` (§ 1–2), `SRC-054.txt` (§ 3.4, l. 2058), `SRC-004.txt` (Table 2 l. 452 ; § 7.4 l. 807–810).
  - Constat initial : imprécis (attribuait aux plateformes des mesures visant spécifiquement « l'émulation de navigation humaine » alors que `SRC-004.txt` évoque contentieux, `robots.txt`, conditions d'utilisation et *throttling* face à l'accès des agents, ceux-ci émulant la navigation humaine pour y faire face). Rectifié d'après `SRC-004.txt`.
  - Verdict final : supporté.

---

### Encadré des trois arbitrages sans regret et Transition (Lignes 125–131)

- **`A-05-62`** (Lignes 125–129)
  - *Affirmation* : Les trois arbitrages sans regret récapitulent fidèlement les prescriptions établies aux sections 5.1 à 5.4 (proscription de *Swagger-to-MCP* au profit d'`ACI` + passerelle épinglée ; primauté de la couche sémantique, des décimales exactes et de l'`ACL` ; cloisonnement des quatre mémoires `CoALA` conforme à la `Loi 25`).
  - *Vérification* : `SRC-038.txt`, `SRC-057.txt`, `SRC-042.txt`, `SRC-039.txt`, `SRC-035.txt`, `SRC-036.txt`, `SRC-026.txt`, `SRC-063.txt`, `registre/glossaire-termes.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **`A-05-63`** (Ligne 131)
  - *Affirmation* : Transition vers le Chapitre 06 soumettant l'orchestration multi-agents aux lois d'échelle à budget de calcul constant, à l'exécution durable et aux sagas à point pivot.
  - *Vérification* : `registre/glossaire-termes.json` (`exécution durable`, `saga à point pivot`, `effet Ringelmann multi-agents`), `registre/faits-empiriques.json` (`FACT-MAP-STUDY`, `FACT-MAST-FAILURES`).
  - Constat initial : supporté.
  - Verdict final : supporté.

---

## Contrôle différentiel post-G4

- **Périmètre vérifié** : retouche stylistique `G4` sur [Chapitre 05 - Connecter sans s enfermer.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/manuscrit/02%20-%20Partie%20II/Chapitre%2005%20-%20Connecter%20sans%20s%20enfermer.md), lignes `15–35` (et ligne `37`, correspondant à l'ancienne ligne `35` après scission de l'ancien paragraphe `21` en `L21` et `L23`, ce qui décale de `+2` les numéros de lignes à partir de `L23`).
- **Sources primaires `L+` comparées directement** : `SRC-038.txt`, `SRC-026.txt`, `SRC-007.txt`, `SRC-056.txt`, `SRC-057.txt` (plus `ch05-sources.md`).
- **Bilan différentiel post-G4 (`L15–L35` / `L37`)** :
  - Affirmations réauditées (`A-05-03` à `A-05-23`) : `21` sur `21` (`100 %` `supporté`)
  - Écarts factuels détectés dans `L15–L35` : `0` (aucune retouche requise au manuscrit)
  - Imprécis résiduel : `0`
  - Non supporté résiduel : `0`
  - Bilan global maintenu pour `ch05` : `63` / `63` `supporté` (`100 %`), `0` imprécis résiduel, `0` non supporté résiduel.

### Détail de la vérification différentielle (`L15–L35`, + `L37`)

1. **`L15` — Protocole `MCP` (`SRC-038.txt`, `A-05-03` à `A-05-05`)** : vérifié contre `SRC-038.txt` (`l. 27–31`, `54–75`, `81–95`) et `ch05-sources.md` `[7]` (`MCP-SPEC-2025-11-25`) — économie d'intégration, `JSON-RPC 2.0`, sessions avec maintien d'état (`Stateful connections`), inspiration `LSP`, trois rôles (`Hosts`, `Clients`, `Servers`), fonctionnalités serveur (`Resources`, `Prompts`, `Tools`) et sollicitations client (`Sampling`, `Elicitation`). Verdict : `supporté`.
2. **`L17` — Jeunesse du registre et limites de gouvernance `MCP` (`SRC-057.txt`, `SRC-038.txt`, `A-05-06` à `A-05-08`)** : vérifié contre `SRC-057.txt` (`l. 142`, `400` : registre public remontant à septembre 2025), `ch05-sources.md` (aucune étude empirique évaluée par les pairs sur la fiabilité ou les coûts d'exploitation en production bancaire ou industrielle) et `SRC-038.txt` (`l. 135–142`, `161` : capacité d'exécution arbitraire, descriptions/annotations *untrusted* hors serveur de confiance, consentement explicite requis par l'hôte, non-imposition au niveau du protocole). Verdict : `supporté`.
3. **`L19` et `L21` — Anti-patron *Swagger-to-MCP* et absence d'étude comparative contrôlée (`A-05-09`, `A-05-10`)** : vérifié contre `SRC-057.txt` (`l. 91–92`), `SRC-026.txt` (`l. 873–877`) et `ch05-sources.md`. Verdict : `supporté`.
4. **`L23` — `CoALA`, `CaMeL` (`13/20`) et `multi-CaMeL` / `AssetOpsBench` (`SRC-026.txt`, `SRC-007.txt`, `SRC-056.txt`, `A-05-11` à `A-05-13`)** :
   - `CoALA` (`[4]`) : vérifié contre `SRC-026.txt` (`l. 1`, `873–877`) — publication dans *Transactions on Machine Learning Research*, complexité décisionnelle accrue d'un espace d'actions étendu et préférence pour le plus petit espace d'actions nécessaire à la tâche. Verdict : `supporté`.
   - `CaMeL` (`[3]`) : vérifié contre `SRC-007.txt` (`§ 6.1.2`, `l. 622–624`, `683–690` ; `Table 1`, `l. 716–760`, `769` ; `Table 2`, `l. 1761–1882`) — `13` échecs sur `20` tâches bénignes de la suite voyage (`Travel`) classés `Underdocumented API` avec `Claude 3.5 Sonnet` (`5/20` correctes, soit `25 %`), faute de pouvoir observer le format de sortie et rédiger l'analyse avant exécution. Verdict : `supporté`.
   - `multi-CaMeL` et `AssetOpsBench` (`[12]`) : vérifié contre `SRC-056.txt` (`§ V`, `l. 701–715` ; `§ V-C2`, `l. 1130–1137`) — enrichissement préalable de tous les outils avec des schémas de retour complets avant évaluation ; substitution non contrôlée de portée (*unchecked scope substitution*) sur `AssetOpsBench` où un sous-agent renvoie un périmètre voisin faute de donnée exacte sur l'actif ou la plage temporelle sans que l'agent parent pré-planifié détecte la violation. Verdict : `supporté`.
5. **`L25–L31` — Cinq disciplines `ACI` (`A-05-14`, ex-`L23–L29`)** : vérifié contre `SRC-007.txt` (`l. 683–690`), `SRC-056.txt` (`l. 709–715`, `1130–1137`) et `SRC-026.txt` (`l. 877`). Verdict : `supporté`.
6. **`L33` — Recensement Kraishan, prévalence et transports (`SRC-057.txt`, `A-05-15` à `A-05-18`, ex-`L31`)** : vérifié contre `SRC-057.txt` (`l. 3`, `7`, `12–17`, `43`, `46–52`, `62–64`, `141–142`, `196–197`, `293–296`, `309–325`, `405–465`, `471–478`, `485–487`, `544–545`) — snapshot d'août 2026 et prépublication de septembre 2026 (`12`/`15` sept. 2026), `21 643` serveurs, `72 606` versions depuis septembre 2025, `14 353` serveurs scannés (`13 051` dépôts, `248 817` fichiers), `414` cas annotés (`294` alertes signalées et `120` fichiers non signalés) ; `15,2 %` (`2 183 / 14 353`) avec au moins une alerte et `11,1 %` avec alerte de sévérité élevée (`~7,6 %` corrigé) ; exposition réseau sans authentification (`9,57 %` observé, `6,83 %` corrigé), dépendances non épinglées (`2,96 %` observé, `2,75 %` corrigé), `SSRF` (`1,33 %` observé, `0,95 %` corrigé), transfert aveugle de jetons appelants (`0,68 %` observé, `0,54 %` corrigé à `0,79` de précision) ; `SSE` déprécié à `44,2 %` contre `12,3 %` en *streamable HTTP*. Verdict : `supporté`.
7. **`L35` — Instabilité silencieuse, non-versionnement des outils et prédicteurs (`SRC-057.txt`, `A-05-19` à `A-05-22`, ex-`L33`)** : vérifié contre `SRC-057.txt` (`l. 18–22`, `70–71`, `144–145`, `204`, `208`, `212–214`, `552–559`, `630–641`, `701–705`, `712–729`, `763–765`) — `8 900` serveurs multi-versions (`37 160` transitions), `51,1 %` de changements annoncés, `40,6 %` de changements sémantiques silencieux sans changement d'identifiant, `370` serveurs (`4,2 %`) redirigeant leur point d'accès distant vers un autre hôte sous le même nom de registre ; délai médian `0` jour (`1` jour entre versions modifiées) ; `OR = 2,96` (`IC 95 % : 2,56 à 3,42`) d'alerte de sévérité élevée ; `69 027` définitions d'outils extraites non versionnées par le registre ; étoiles GitHub (`OR = 0,78`), taille du code (`OR = 1,94`) et ancienneté du dépôt (`OR = 1,38`). Verdict : `supporté`.
8. **`L37` — Passerelle de médiation `MCP` (`A-05-23`, ex-`L35`)** : vérifié contre `SRC-057.txt` (`§ 5.1–5.2`, `l. 769–780`). Verdict : `supporté`.
