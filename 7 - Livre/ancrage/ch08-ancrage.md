# Ancrage atomique Wyvern — Chapitre 08 (`ch08`)

- **Unité** : `ch08` — [Chapitre 08 - Securite par construction.md](file:///c:/Github/Agentique/7%20-%20Livre/manuscrit/03%20-%20Partie%20III/Chapitre%2008%20-%20Securite%20par%20construction.md)
- **Dossier de sources** : [ch08-sources.md](file:///c:/Github/Agentique/7%20-%20Livre/sources/ch08-sources.md) (`13` sources intégrales `L+`)
- **Registres vérifiés** : `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`), `registre/glossaire-termes.json`
- **Date de gel des faits** : 2 décembre 2026 | **Volume final (`v1.3`)** : `5 629` mots `G1` (`5 888` `split()`, cible `[5 152, 6 048]`)
- **Protocole** : Audit atomique indépendant `G2` (`CA-10`, `CA-12`, régime Production)

## Bilan synthétique

- **Affirmations atomiques auditées** : `108` (`71` initialement `supporté`, `36` `imprécis` rectifiés, `1` `non supporté + imprécis` réancré et rectifié)
- **Verdict final — supportés : 108 (100 %)**
- **Verdict final — imprécis résiduels : 0**
- **Verdict final — non supportés résiduels : 0**
- **Principales rectifications** : suppression d'un acronyme non présent dans le corpus `L+` (`FIDES`, réancré sur les références explicites de [1, 10] dans A75), correction factuelle critique sur *Banking* dans `CaMeL` (`o4 Mini High` = `1 ± 0,0` résiduel au tableau 4 de `SRC-007.txt` dans A68), correction sur la fuite de la boucle de réessai dans `LLMbda` (A75), et `34` resserrements de précision terminologique, bibliographique ou quantitative (A05, A08, A13–A15, A17, A19–A21, A23, A29, A34, A36–A38, A42, A44, A46, A51, A53, A64, A69, A71, A78–A80, A82, A85, A90–A95, A106).

---

## Détail paragraphe par paragraphe

### Introduction (P01–P04)

#### P01 — Ouverture et hypothèse industrielle sur les modèles plus capables [`L5`]
- **A01** — Affirmation : En 2026, une intuition répandue mise sur la montée en capacité de raisonnement et d'obéissance des modèles pour résorber l'injection indirecte sans refondre l'architecture applicative.
  - Constat initial : supporté (cadrage éditorial introduisant la thèse testée empiriquement dès P02 et référencée dans [1, 10]).
  - Source probante : Cadrage du chapitre mis à l'épreuve dans `SRC-056.txt` (§ V.B, Table III) et `SRC-007.txt` (§ 1, § 6.3).
  - Verdict final : supporté

#### P02 — Corrélation capacité-compromission sur `MultiAgentDojo` et objectifs concurrents [`L7`]
- **A02** — Affirmation : Dans une prépublication d'octobre 2026, Peters-Gill, Semler, Bartsch, Shumailov et Schroeder de Witt évaluent cinq modèles de capacités inégales sur le banc multi-agents hiérarchique `MultiAgentDojo` (`949` instances d'attaques par configuration) sans défense structurelle active [10].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [10] ; `SRC-056.txt` (en-tête `arXiv:2610.05640v1 [cs.MA] 5 Oct 2026`, `Preprint`, § V.B Table III `n = 949 injected task instances per model and configuration`, `No CaMeL`).
  - Verdict final : supporté
- **A03** — Affirmation : `Gemini 2.5 Flash Lite` accomplit `27,8 %` des tâches bénignes et subit `2,1 %` d'`ASR` sous `No CaMeL` [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (Table II p. 6 / l. 899-900 : `27.8 ± 8.9` ; Table III l. 1001 : `2.1% [1.4, 3.2]`).
  - Verdict final : supporté
- **A04** — Affirmation : `Gemini 2.5 Pro` (`76,3 %` d'utilité bénigne) et `GPT-4.1` (`78,4 %`) voient leur `ASR` monter à `24,6 %` et `36,1 %` [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (Table II l. 891-896 : `78.4 ± 8.2`, `76.3 ± 8.5` ; Table III l. 989-995 : `36.1%`, `24.6%`).
  - Verdict final : supporté
- **A05** — Affirmation : `NIST AI 100-2e2025` éclaire ce mécanisme par les objectifs concurrents (*competing objectives*) entre suivi fidèle des instructions et objectifs de sûreté, tension qui expose d'autant plus un agent outillé [8].
  - Constat initial : imprécis → rectifié (l'expression initiale attribuait aux seuls *competing objectives* « de déclencher proprement les outils mis à sa portée » ; reformulée selon § 3.3.1 et § 3.5 de `SRC-054.txt`).
  - Source probante : `sources/ch08-sources.md` [8] ; `SRC-054.txt` (§ 3.3.1 l. 2289-2296 : tension entre suivi des instructions et sûreté ; § 3.5 l. 2726-2729 : prise d'actions via outils).
  - Verdict final : supporté

#### P03 — Bornes épistémiques (`GPT-5.5`), défiance `MCP` et absence de versionnage [`L9`]
- **A06** — Affirmation : Ce constat provient d'une prépublication sur un banc unique et ne forme pas une loi monotone universelle condamnant tout gain de capacité [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (l. 59 `Preprint`, § V.B l. 933 `non-monotonic`, Table III note l. 1016-1019).
  - Verdict final : supporté
- **A07** — Affirmation : `GPT-5.5` atteint `86,6 %` de réussite bénigne et `0,0 %` d'`ASR` sur ces attaques fixes, résultat qui reflète les limites du banc et non une immunité aux attaques adaptatives [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (Table II l. 888 : `86.6 ± 6.8` ; Table III l. 983 & note l. 1016-1019).
  - Verdict final : supporté
- **A08** — Affirmation : La spécification `MCP` avertit que les descriptions d'outils doivent être tenues pour non fiables hors d'un serveur de confiance [2].
  - Constat initial : imprécis → rectifié (ajout de la réserve « hors d'un serveur de confiance » présente mot pour mot dans `SRC-038.txt`).
  - Source probante : `sources/ch08-sources.md` [2] ; `SRC-038.txt` (l. 138-139 : `unless obtained from a trusted server`).
  - Verdict final : supporté
- **A09** — Affirmation : Le recensement de Kraishan sur `21 643` serveurs publics révèle l'absence généralisée de versionnage des définitions d'outils [11].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [11] ; `SRC-057.txt` (l. 13, 141, 144-146, 213 : `the registry does not version tool definitions`).
  - Verdict final : supporté
- **A10** — Affirmation : Raccorder des agents performants à des chaînes d'outils hétérogènes amplifie le rayon d'action d'une instruction détournée [8, 13].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 3.5 l. 2726-2729) ; `SRC-066.txt` (l. 67, 203, 355 : amplification d'échelle et de vitesse par enchaînement d'outils).
  - Verdict final : supporté

#### P04 — Avertissement du `BSIF` (*AI harnessing*) et filiation du chapitre 07 [`L11`]
- **A11** — Affirmation : Dans son bulletin de juillet 2026, le `BSIF` avertit que l'agentique accélère les risques cybernétiques et appelle à encadrer l'autonomie par un harnais logiciel (*AI harnessing*) [13].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [13] ; `SRC-066.txt` (l. 63 `Date: July 2026`, l. 67, l. 145 `implement AI harnessing alongside human oversight`, note 4 l. 709).
  - Verdict final : supporté
- **A12** — Affirmation : Renvoi structurel au chapitre 07 (identité non humaine et chaîne de mandat) pour introduire la sécurité du flux d'exécution.
  - Constat initial : supporté
  - Source probante : `registre/glossaire-termes.json` (`identité non humaine`, `délégation au nom de`, `chapitre_proprietaire: ch07`).
  - Verdict final : supporté

---

### Section 8.1 — Nouvelle surface d'attaque (P05–P12)

#### P05 — Passage de l'injection directe à l'injection indirecte (`NISTAML.015`) [`L15`]
- **A13** — Affirmation : Dans le dialogue avec un seul usager, la menace visée par le `NIST` porte d'abord sur le contournement direct exercé par l'usager lui-même (réponse interdite ou extraction des consignes système) [8].
  - Constat initial : imprécis → rectifié (reformulé sans affirmation historique absolue sur « la menace principale », fidèlement à § 3.3 de `SRC-054.txt`).
  - Source probante : `SRC-054.txt` (§ 3.3 `Direct Prompting Attacks`, l. 2242-2263 : `primary user`, `jailbreak`, `extract the system prompt`).
  - Verdict final : supporté
- **A14** — Affirmation : Selon `NIST AI 100-2e2025`, l'injection indirecte (`NISTAML.015`) est déclenchée par un tiers contrôlant une ressource (courriel, document, page Web ou base de connaissances) ingérée en cours de tâche [8].
  - Constat initial : imprécis → rectifié (« document partagé » et « base de données » resserrés en « document, page Web ou base de connaissances » attestés dans `SRC-054.txt`).
  - Source probante : `SRC-054.txt` (§ 3.1.3 l. 2154 `documents, web pages`, § 3.4 l. 2577-2593, § 3.4.2 l. 2646, 2659).
  - Verdict final : supporté
- **A15** — Affirmation : La victime devient l'utilisateur légitime lui-même, dont l'agent exécute les instructions d'un adversaire sur les ressources auxquelles il accède [8, 9].
  - Constat initial : imprécis → rectifié (ajout de `[9]` pour les permissions et droits d'accès hérités par l'agent).
  - Source probante : `SRC-054.txt` (§ 3.4 l. 2591-2593, § 3.4.3 l. 2678) ; `SRC-055.txt` (`ASI03`, `ASI01`).
  - Verdict final : supporté

#### P06 — Canal unique instruction/donnée et taxonomie `OWASP Agentic Top 10` (2026) [`L17`]
- **A16** — Affirmation : Les `LLM` combinent dans un même canal les instructions système, la requête fiable et les données récupérées dans l'environnement [8].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 3.4 l. 2579 : `combine the data and instruction channels`).
  - Verdict final : supporté
- **A17** — Affirmation : Faute de séparation typée entre instruction et donnée dans la représentation traitée par le modèle, un ordre caché dans une note partagée ou un courriel prend la même forme syntaxique qu'une consigne légitime [1, 8].
  - Constat initial : imprécis → rectifié (« au sein des poids » et « une facture » remplacés par « dans la représentation traitée par le modèle » et « un courriel », fidèles à `SRC-007.txt` et `SRC-054.txt`).
  - Source probante : `SRC-007.txt` (§ 2 l. 146-152, App. A.1.1 note 7 l. 1708-1711) ; `SRC-054.txt` (§ 3.4 l. 2579, 2659).
  - Verdict final : supporté
- **A18** — Affirmation : L'`OWASP Top 10 for Agentic Applications` (2026) classe `ASI01`, `ASI02`, `ASI03`, `ASI05` et `ASI10` au rang critique [9].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [9] ; `SRC-055.txt` (l. 5-23, 41-43 : tous notés `Critical`).
  - Verdict final : supporté
- **A19** — Affirmation : L'`OWASP` y ajoute la corruption persistante de la mémoire ou des entrepôts RAG et plongements (`ASI06`, renvoi ch. 05) et l'exploitation de la confiance humain-agent (`ASI09`, renvoi ch. 11 sur l'approbation réflexe) [9].
  - Constat initial : imprécis → rectifié (« bases vectorielles » aligné sur « entrepôts RAG et plongements », verbatim `RAG stores, embeddings` dans `SRC-055.txt`).
  - Source probante : `SRC-055.txt` (`ASI06` l. 25-27 ; `ASI09` l. 37-39) ; `registre/glossaire-termes.json` (`approbation réflexe`).
  - Verdict final : supporté

#### P07 — Trois effets adverses du `NIST` (`NISTAML.016`, `NISTAML.027`, `NISTAML.039`) [`L19`]
- **A20** — Affirmation : Les attaques de disponibilité (`NISTAML.016`) piègent l'agent dans des boucles chronophages (`NISTAML.017`), désactivent des API ou injectent des homoglyphes qui perturbent les appels d'API en aval [8].
  - Constat initial : imprécis → rectifié (« boucles coûteuses » et « rompent les parseurs en aval » alignés sur « boucles chronophages (`NISTAML.017`) » et « perturbent les appels d'API en aval » de `SRC-054.txt`).
  - Source probante : `SRC-054.txt` (§ 3.4.1 l. 2595-2613 : `NISTAML.016`, `NISTAML.017`, `looping behavior`, `homoglyph equivalents, disrupting subsequent API calls`).
  - Verdict final : supporté
- **A21** — Affirmation : Les attaques d'intégrité (`NISTAML.027`) falsifient des résumés ou détournent l'agent, parfois via *Neural Exec* survivant au découpage et au filtrage contextuel d'un pipeline RAG, l'empoisonnement de bases de connaissances ou des vers auto-propageables par courriel [8].
  - Constat initial : imprécis → rectifié (« modifient la suite des appels d'outils » et « bases vectorielles » alignés sur § 3.4.2 de `SRC-054.txt`).
  - Source probante : `SRC-054.txt` (§ 3.4.2 l. 2615-2662 : `Neural Exec`, `chunking and contextual filtering`, `Knowledge base poisoning`, `worms`).
  - Verdict final : supporté
- **A22** — Affirmation : Les compromissions de confidentialité (`NISTAML.039`) poussent à exfiltrer des pièces privées vers une adresse tierce ou via une requête Web forgée [8].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 3.4.3 l. 2677-2683 : `forward certain emails`, `querying an attacker-controlled URL`).
  - Verdict final : supporté

#### P08 — Propagation inter-outils et blanchiment à la frontière (*boundary laundering*) [`L21–L23`]
- **A23** — Affirmation : Le bulletin du `BSIF` met en garde contre l'enchaînement d'outils (*tool chaining*), dont la sortie alimente l'étape suivante et déclenche des actions en aval non validées en cascade (`ASI08`) [9, 13].
  - Constat initial : imprécis → rectifié (« écritures non validées » élargi en « actions en aval non validées » fidèlement à `unvalidated downstream actions` dans `SRC-066.txt`).
  - Source probante : `SRC-066.txt` (l. 203, 355, note 8 l. 731-733) ; `SRC-055.txt` (`ASI08` l. 33-35).
  - Verdict final : supporté
- **A24** — Affirmation : Peters-Gill *et al.* identifient dans les architectures hiérarchiques d'agents invoqués comme outils le défaut critique dit « blanchiment à la frontière » (*boundary laundering*) [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (§ I l. 193-195, § II.A l. 234-238).
  - Verdict final : supporté
- **A25** — Affirmation : Un orchestrateur insérant une donnée issue d'une base `SQL` dans la requête en langage naturel d'un agent de notification en change tacitement le statut de confiance ; le planificateur aval ajoute alors un envoi de courriel non autorisé vers un tiers [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (§ III.A l. 344-485, Fig. 1–3, `query_sql`, `Notification Agent`, `send_email` vers `ruth@email.com`).
  - Verdict final : supporté
- **A26** — Affirmation : Ce mécanisme justifie la règle du maillon le plus élevé (*High-Water Mark Rule*) et les exigences `A2A` (`ASI07`) d'authentification, de chiffrement et de validation de schémas [3, 9].
  - Constat initial : supporté
  - Source probante : `registre/glossaire-termes.json` (`règle du maillon le plus élevé`) ; `SRC-055.txt` (`ASI07` l. 29-31) ; `SRC-039.txt` (§ 13.4 l. 5921, § 14.1.1 l. 6010, 6016).
  - Verdict final : supporté

#### P09 — Chaîne d'approvisionnement des serveurs d'outils (`ASI04`) et avertissements `MCP` [`L25`]
- **A27** — Affirmation : La chaîne d'approvisionnement logicielle des serveurs d'outils constitue une surface d'attaque (`ASI04`), tandis que `MCP` (`JSON-RPC 2.0`, révision 25 nov. 2025) avertit que les outils représentent une exécution de code arbitraire et que descriptions et annotations doivent être tenues pour non fiables hors d'un serveur de confiance [2, 9].
  - Constat initial : supporté
  - Source probante : `SRC-055.txt` (`ASI04` l. 90, 276) ; `SRC-038.txt` (l. 99, 411, 5002).
  - Verdict final : supporté
- **A28** — Affirmation : Le protocole `MCP` ne peut faire respecter ces protections par lui-même et renvoie aux implémenteurs la charge des contrôles d'autorisation, de consentement et d'accès [2].
  - Constat initial : supporté
  - Source probante : `SRC-038.txt` (l. 88-99).
  - Verdict final : supporté

#### P10 — Recensement empirique de Kraishan sur le registre public `MCP` [`L27–L39`]
- **A29** — Affirmation : En septembre 2026 (instantané d'août 2026), Kraishan recense `21 643` serveurs `MCP` (`72 606` versions) et analyse `14 353` serveurs (`13 051` dépôts GitHub, `248 817` fichiers, `69 027` définitions d'outils) avec `31` motifs dont la précision est mesurée sur `414` cas étiquetés à la main (`294` constats et `120` fichiers non signalés) [11].
  - Constat initial : imprécis → rectifié (« calibrés sur 414 constats » corrigé en « dont la précision est mesurée sur 414 cas étiquetés à la main (`294` constats et `120` fichiers non signalés) », car l'échantillon valide la précision sans entraîner les motifs).
  - Source probante : `SRC-057.txt` (l. 7, 13-15, 141-142, 196-197, 204, 219, 293-297, Table 2–3).
  - Verdict final : supporté
- **A30** — Affirmation : `15,21 %` des serveurs scannés portent au moins un constat et `11,14 %` au moins un constat de haute sévérité, taux ramené de manière conservatrice à environ `7,6 %` après correction par précision [11].
  - Constat initial : supporté
  - Source probante : `SRC-057.txt` (§ 4.1 l. 471-477 : `15.21%`, `11.14%`, `roughly 7.6%`).
  - Verdict final : supporté
- **A31** — Affirmation : L'exposition réseau sans authentification domine à `9,57 %` observé (`6,83 %` corrigé), suivie par les dépendances non épinglées (`2,96 %` observé, `2,75 %` corrigé) [11].
  - Constat initial : supporté
  - Source probante : `SRC-057.txt` (Table 4 l. 434-441, § 4.1 l. 474-476).
  - Verdict final : supporté
- **A32** — Affirmation : Les risques de délégation touchent `1,57 %` des serveurs (`225` serveurs : `0,68 %` de transfert direct de jeton, soit `0,54 %` corrigé à `0,79` de précision, et `0,88 %` d'autorité ambiante), avec `2,09 %` sur les serveurs distants contre `1,25 %` sur les serveurs locaux (`OR = 1,69`) [11].
  - Constat initial : supporté
  - Source probante : `SRC-057.txt` (Table 2 l. 324 `0.79`, Table 4 l. 450-461, § 4.1.1 l. 493-494, 546-547).
  - Verdict final : supporté
- **A33** — Affirmation : Les serveurs en `SSE` déprécié atteignent `44,2 %` de constats graves contre `12,3 %` en `streamable HTTP` [11].
  - Constat initial : supporté
  - Source probante : `SRC-057.txt` (§ 4.1 l. 486-487).
  - Verdict final : supporté

#### P11 — Dérive silencieuse d'outil (*silent drift*) et régression des prédicteurs [`L41`]
- **A34** — Affirmation : Le registre `MCP` ne versionne pas les définitions d'outils, rendant le glissement fonctionnel invisible dans ses métadonnées ; Kraishan nomme *silent drift* ce phénomène traité ici comme **dérive silencieuse d'outil** [11].
  - Constat initial : imprécis → rectifié (attribution exacte du terme *silent drift* à Kraishan et du terme normatif `dérive silencieuse d'outil` au glossaire du livre).
  - Source probante : `SRC-057.txt` (§ 3.1.4 l. 212-215, § 4.2 l. 551) ; `registre/glossaire-termes.json` (`dérive silencieuse d'outil`).
  - Verdict final : supporté
- **A35** — Affirmation : Sur `8 900` serveurs multi-versions (`37 160` transitions), `51,09 %` ont modifié description, paquets ou points de terminaison, `40,58 %` ont opéré au moins un changement sémantique silencieux sous identifiants inchangés et `370` serveurs (`4,16 %`) ont redirigé leur point de terminaison distant vers un autre hôte sous le même nom de registre [11].
  - Constat initial : supporté
  - Source probante : `SRC-057.txt` (§ 4.2 l. 553-560, Table 5 l. 588-590, l. 630-632).
  - Verdict final : supporté
- **A36** — Affirmation : Le délai médian avant le premier changement est de `0` jour (`1` jour entre versions modifiées) et la dérive silencieuse associe une cote presque trois fois plus élevée de constat grave (`OR = 2,96`, IC à `95 %` `[2,56, 3,42]`) [11].
  - Constat initial : imprécis → rectifié (« chances » remplacé par « cote » pour refléter rigoureusement le rapport de cotes *odds ratio*).
  - Source probante : `SRC-057.txt` (§ 4.2 l. 636-640).
  - Verdict final : supporté
- **A37** — Affirmation : La corrélation brute étoiles-constats est quasi nulle (`ρ = 0,008`, `p = 0,335`) ; dans la régression multivariée, les étoiles réduisent modestement la cote de risque à taille et âge égaux (`OR = 0,78` par unité logarithmique), la taille (`OR = 1,94`), l'âge (`OR = 1,38`) et le statut archivé (`OR = 1,52`) l'augmentent, tandis que maintenance récente et licence sont non significatives [11].
  - Constat initial : imprécis → rectifié (précisé « à taille et âge égaux » conformément au modèle de la table 6).
  - Source probante : `SRC-057.txt` (§ 4.3 l. 648, 701-707, Table 6 l. 712-741).
  - Verdict final : supporté
- **A38** — Affirmation : Aucun empoisonnement manifeste par motifs syntaxiques n'est détecté (borne supérieure de Wilson à `0,027 %`), mais des instructions obfusquées échappent aux expressions régulières [11].
  - Constat initial : imprécis → rectifié (« mots-clés » corrigé en « motifs syntaxiques », `SRC-057.txt` précisant `guarded regular expression rather than a bare keyword match`).
  - Source probante : `SRC-057.txt` (§ 3.2 l. 224, § 4.1 l. 481-483, § 6.0.1 l. 811).
  - Verdict final : supporté

#### P12 — `SCITT` (`RFC 9943`) pour l'attestation et l'épinglage de chaîne d'approvisionnement [`L43`]
- **A39** — Affirmation : La `RFC 9943` (Birkholz, Delignat-Lavaud, Fournet, Deshpande et Lasker, juin 2026) normalise `SCITT` pour enregistrer des énoncés signés (`COSE_Sign1`) dans des journaux en ajout seul (*append-only*) non équivoques [6].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [6] ; `SRC-044.txt` (en-tête l. 3-11, § 1 l. 141-145, § 3 l. 424-486, § 5.1.3 l. 808-817).
  - Verdict final : supporté
- **A40** — Affirmation : Via politiques d'enregistrement et reçus `COSE` sur structures de données vérifiables, une passerelle peut vérifier qu'un serveur d'outils, sa `SBOM`, son empreinte et ses attestations de revue émanent d'un émetteur autorisé et n'ont pas divergé [6, 11].
  - Constat initial : supporté
  - Source probante : `SRC-044.txt` (§ 2.1 l. 240-243, § 5.1.1 l. 742-774, § 6 l. 850, § 6.2 l. 1002, § 7 l. 1113-1252) ; `SRC-057.txt` (§ 5.1 l. 768-772).
  - Verdict final : supporté

---

### Section 8.2 — Limites des filtres auxiliaires et piège du banc unique (P13–P18)

#### P13 — Taxonomie des trois familles de garde-fous probabilistes [`L47–L53`]
- **A41** — Affirmation : Les trois familles sont la hiérarchie d'instructions / alignement antagoniste (dont *Meta SecAlign*), la structuration d'invite (*Spotlighting* par délimiteurs ou encodage, *Prompt Sandwiching*) et les filtres/classifieurs auxiliaires [1, 8, 10].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 2 l. 115-128, App. A.2 l. 1718-1725) ; `SRC-054.txt` (§ 3.3.3 l. 2485-2494, § 3.4.4 l. 2694-2704) ; `SRC-056.txt` (§ I l. 60-76, réf. [5, 8, 9]).
  - Verdict final : supporté
- **A42** — Affirmation : La troisième famille inclut *Llama Guard 3*, *Prompt Guard* et classifieurs *DeBERTa* [1, 8], *Tool Filter* [1], ainsi que *DataFilter* (*IEEE SaTML* 2026) et la désescalade douce de consignes [10].
  - Constat initial : imprécis → rectifié (« les filtres d'élagage d'outils (*Tool Filter*) » remplacé par « le filtrage d'outils (*Tool Filter*) », `SRC-007.txt` nommant la défense sans en détailler le mécanisme d'élagage).
  - Source probante : `SRC-054.txt` (l. 2491, réf. [5, 6] l. 3002-3004) ; `SRC-007.txt` (§ 6.3 l. 950, App. A.2 l. 1732, réf. `ProtectAI 2024` l. 1583) ; `SRC-056.txt` (§ I l. 66-72, réf. [6, 7] l. 1336-1344).
  - Verdict final : supporté
- **A43** — Affirmation : Ces dispositifs reposent sur des comportements appris et n'offrent aucune garantie formelle [8, 10].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 4.1.2 l. 2791, 2951) ; `SRC-056.txt` (§ I l. 78-79 : `rely on learned model behavior and do not provide hard security guarantees`).
  - Verdict final : supporté

#### P14 — Bornes théoriques et défaillances corrélées (`NIST AI 100-2e2025`) [`L55`]
- **A44** — Affirmation : Le `NIST` rappelle, d'après Tramèr et Fang *et al.*, que détecter fiablement les exemples adverses équivaut au problème de la classification robuste, avec bornes d'impossibilité lorsque les données en distribution et hors distribution se chevauchent [8].
  - Constat initial : imprécis → rectifié (« distributions bénignes et malveillantes » resserré en « données en distribution et hors distribution » selon Fang *et al.* cité dans `SRC-054.txt`).
  - Source probante : `SRC-054.txt` (§ 4.1.2 l. 2797-2804, réf. [373, 124]).
  - Verdict final : supporté
- **A45** — Affirmation : Tant qu'un modèle garde une probabilité non nulle d'un comportement indésirable, des formulations antagonistes peuvent le déclencher ; l'entraînement de sûreté atténue sans éliminer [8].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (l. 2953-2956 : `so long as a model has any probability of exhibiting an undesired behavior, there exist prompts that can trigger that behavior...`).
  - Verdict final : supporté
- **A46** — Affirmation : Les filtres par modèle auxiliaire demeurent eux-mêmes vulnérables aux attaques et sujets à des **défaillances corrélées** avec le modèle principal [8].
  - Constat initial : imprécis → rectifié (« exposés aux contournements adaptatifs » resserré en « vulnérables aux attaques » fidèlement à l. 2495 de `SRC-054.txt`).
  - Source probante : `SRC-054.txt` (§ 3.3.3 l. 2495-2497 : `vulnerable to attacks [235] and may have correlated failures to the main models`).
  - Verdict final : supporté

#### P15 — Comparatifs `AgentDojo` (`Claude 3.5 Sonnet`, `GPT-4o Mini`) et attaques adaptatives [`L57–L59`]
- **A47** — Affirmation : Sur `949` attaques d'`AgentDojo` avec `Claude 3.5 Sonnet`, l'agent sans défense cède à `44` attaques (`90,72 %` d'utilité bénigne, `86,83 %` sous attaque) [1].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [1] (`IEEE SaTML`) ; `SRC-007.txt` (§ 6.3 l. 946, Table 5 l. 2156, Table 6 l. 2234, Table 7 l. 2283).
  - Verdict final : supporté
- **A48** — Affirmation : *Prompt Sandwiching* réduit à `24` attaques (`84,19 %` sous attaque), *Tool Filter* à `8` (`72,71 %` sous attaque) et *Spotlighting* à `5` (`89,36 %` sous attaque) [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (Table 6 l. 2216-2228, Table 7 l. 2265-2277).
  - Verdict final : supporté
- **A49** — Affirmation : *Tool Filter* dégrade l'utilité bénigne à `73,20 %` et multiplie par `7,77` la consommation médiane de jetons d'entrée hors attaque (`2,34×` en variante optimisée) [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (Table 5 l. 2150 : `73.20%`, Table 10 l. 2436-2446 : `7.77` et `2.34`).
  - Verdict final : supporté
- **A50** — Affirmation : `GPT-4o Mini` doté nativement de la hiérarchie d'instructions cède encore devant `276` attaques [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 6.3 l. 962-965).
  - Verdict final : supporté
- **A51** — Affirmation : Face aux attaques adaptatives (`US-AISI` 2025 sur `Claude 3.5 Sonnet` [1], Zhan *et al.* NAACL 2025 contre les défenses d'agents, et Dziemian *et al.* 2026 relevant un `ASR` non nul sur tous les modèles frontières évalués [10]), les défenses heuristiques cèdent sans garantie [1, 10].
  - Constat initial : imprécis → rectifié (précisé les portées respectives d'`US-AISI`, Zhan *et al.* et Dziemian *et al.* au lieu d'affirmer un effondrement uniforme de « l'ensemble des défenses probabilistes »).
  - Source probante : `SRC-007.txt` (§ 6.3 l. 958-961) ; `SRC-056.txt` (§ I l. 77-79, réf. [10] l. 1355-1359, Table III note l. 1018-1019, réf. [29] l. 1443-1452).
  - Verdict final : supporté

#### P16 — Biais méthodologiques et front de Pareto recommandé par le `NIST` [`L61`]
- **A52** — Affirmation : Le `NIST` souligne l'incomparabilité due à l'absence de bancs standardisés, la surestimation des défenses face aux attaques statiques, et recommande un front de Pareto croisant robustesse antagoniste et utilité [8].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 4.1.1 Fig. 8 l. 2764-2787, § 4.1.3 l. 2822-2840).
  - Verdict final : supporté

#### P17 — Trois écueils observés sur bancs uniques [`L63–L66`]
- **A53** — Affirmation : **Artefacts de refus** : sur `MultiAgentDojo`, `Claude Fable 5` refuse `52` des `97` tâches bénignes (`53,6 %`), probablement par association à un contexte hostile, donnant `1,5 %` d'`ASR` tout en abaissant l'utilité bénigne mesurée (`69,1 %` avec refus contre `91,1 %` hors refus) [10].
  - Constat initial : imprécis → rectifié (ajout des taux exacts d'utilité bénigne `69,1 %` vs `91,1 %` à la place d'une « chute artificielle de disponibilité » vague).
  - Source probante : `SRC-056.txt` (Table III l. 977 `1.5%`, § V.B l. 1020-1030 `52 of 97 (53.6%)`, Table V l. 2530-2535 `91.1%` vs `69.1%`).
  - Verdict final : supporté
- **A54** — Affirmation : **Illusion du zéro pour cent** : `GPT-5.5` obtient `0,0 %` d'`ASR` sans défense structurelle sur `MultiAgentDojo`, mais les auteurs avertissent que cela ne prouve aucune immunité aux attaques adaptatives [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (Table III l. 983 & note l. 1016-1019).
  - Verdict final : supporté
- **A55** — Affirmation : **Défauts internes des bancs** : Debenedetti *et al.* recensent des bogues d'évaluation dans `AgentDojo` [1] et Peters-Gill *et al.* excluent `29` des `141` tâches d'`AssetOpsBench` irréalisables faute de fichiers ou de données de capteurs [10].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (Table 1 l. 761-764 `AgentDojo bug`) ; `SRC-056.txt` (§ V.A.1 l. 757-768, App. B l. 1861-1895 `29 of the 141 tasks`).
  - Verdict final : supporté

#### P18 — Synthèse méthodologique : réplication et attaque adaptative [`L68`]
- **A56** — Affirmation : Seules la réplication sur jeux variés et l'épreuve continue par attaque adaptative évitent les angles morts d'un banc unique [8, 10].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 3.3.3 l. 2480-2483, § 4.1.3 l. 2822-2833) ; `SRC-056.txt` (Table III note l. 1016-1019).
  - Verdict final : supporté

---

### Section 8.3 — Séparation par construction et « règle de deux » (P19–P27)

#### P19 — Recommandation indirecte du `NIST` et séparation par construction [`L72`]
- **A57** — Affirmation : Une recommandation indirecte du `NIST` préconise de concevoir l'application en présumant qu'un modèle exposé à des ressources hostiles produira tôt ou tard des sorties malveillantes [8].
  - Constat initial : supporté
  - Source probante : `SRC-054.txt` (§ 3.3.3 `Indirect mitigations` l. 2538-2550, § 3.4.4 l. 2706-2715).
  - Verdict final : supporté
- **A58** — Affirmation : La **séparation par construction entre contrôle et données** ancre la sécurité dans la couche déterministe du harnais plutôt que dans les poids du modèle [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 1 l. 38, § 11 l. 1428-1445) ; `registre/glossaire-termes.json` (`séparation par construction entre contrôle et données`).
  - Verdict final : supporté

#### P20 — Patron *Dual LLM* de Simon Willison (2023) et sa limite sur le flux de données [`L74`]
- **A59** — Affirmation : Simon Willison (2023) scinde l'agent entre un modèle privilégié planifiant depuis la seule requête utilisateur et un modèle en quarantaine sans outils cantonné aux données externes [1, 10].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 2 l. 131-140, App. A.2 l. 1736-1742) ; `SRC-056.txt` (§ I l. 83-99).
  - Verdict final : supporté
- **A60** — Affirmation : Debenedetti, Shumailov, Fan, Hayes, Carlini, Tramèr *et al.* (*IEEE SaTML*, `arXiv:2503.18813`) démontrent que cette séparation ne protège que le flux de contrôle : des notes de réunion piégées peuvent détourner les paramètres de `send_email` (analogue à une injection `SQL` sur le flux de données) [1].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [1] (`IEEE SaTML`, évalué par les pairs) ; `SRC-007.txt` (en-tête l. 1-4 `arXiv:2503.18813v2`, § 2 l. 141-162, Fig. 2).
  - Verdict final : supporté

#### P21 — Mécanismes internes de `CaMeL` [`L76–L78`]
- **A61** — Affirmation : `CaMeL` (*Capabilities for Machine Learning*) combine `CFI`, `IFC` et capacités inspirées de *Capsicum* et *CHERI* [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 1 l. 29-39, § 5.3 l. 514-515).
  - Verdict final : supporté
- **A62** — Affirmation : `P-LLM` reçoit la requête fiable et les signatures d'outils, génère du Python restreint ; `Q-LLM` sans outils remplit un schéma `Pydantic` doté d'un booléen de suffisance d'information sans renvoyer de prose libre au `P-LLM` [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 5.1 l. 417-440, § 5.4 l. 529).
  - Verdict final : supporté
- **A63** — Affirmation : Un interpréteur Python exécute l'`ast`, attache aux variables des **capacités** (provenance et lecteurs autorisés), maintient le graphe de dépendances et applique des politiques déterministes à chaque frontière d'outil [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 5.2–5.4 l. 496-599).
  - Verdict final : supporté
- **A64** — Affirmation : La politique sur `create_calendar_event` autorise l'appel si les participants viennent de la requête fiable ou peuvent déjà lire les champs transmis, tandis que celle sur `send_email` exige des destinataires fiables et vérifie leurs droits de lecture sur l'objet, le corps et les pièces jointes [1].
  - Constat initial : imprécis → rectifié (distinction exacte entre la règle en disjonction de `create_calendar_event` au § 5.2 / Fig. 6 et les contraintes de `send_email` à l'annexe E de `SRC-007.txt`).
  - Source probante : `SRC-007.txt` (Fig. 5 l. 394, Fig. 6 l. 443-461, § 5.2 l. 480-487, App. E l. 2343-2355).
  - Verdict final : supporté
- **A65** — Affirmation : Si une exception dépend d'une donnée non fiable, le message retourné lors des reprises (jusqu'à `10` tentatives) est caviardé [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 5.4 l. 566-573).
  - Verdict final : supporté

#### P22 — Résultats quantitatifs et surcoûts de `CaMeL` sur `AgentDojo` [`L80–L82`]
- **A66** — Affirmation : Sur `AgentDojo` (*Workspace*, *Banking*, *Slack*, *Travel*), `CaMeL` résout `77 %` des tâches avec garantie structurelle contre `84 %` sans défense [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (résumé l. 13-14) ; `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`).
  - Verdict final : supporté
- **A67** — Affirmation : `o3 High` atteint `77,3 %` sous `CaMeL` contre `84,5 %` en natif, et `Claude 4 Sonnet` `74,2 %` contre `86,6 %` [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (Table 2 l. 1769-1781, 1845-1857).
  - Verdict final : supporté
- **A68** — Affirmation : Avec politiques actives, aucune attaque ne réussit sur *Workspace* ni sur *Slack* pour l'ensemble des modèles évalués, une seule subsiste sur *Banking* pour `o4 Mini High` (`0` pour `Claude 3.5 Sonnet`, `Claude 4 Sonnet`, `Gemini 2.5 Flash`, `Gemini 2.5 Pro`, `o3 High`), et `GPT-4o Mini` passe de `276` compromissions à `0` [1].
  - Constat initial : imprécis → rectifié (le texte initial affirmait `0` sur *Banking* pour tous les modèles, contredit par `1 ± 0.0` sur `o4 Mini High` au tableau 4 de `SRC-007.txt`).
  - Source probante : `SRC-007.txt` (Table 4 l. 2008-2129, § 6.3 l. 962-965).
  - Verdict final : supporté
- **A69** — Affirmation : Sur `Claude 3.5 Sonnet`, la surcharge médiane est de `2,73×` en entrée et `2,82×` en sortie hors attaque au tableau 10 (`2,02×` et `2,64×` sous attaque au tableau 13, les auteurs synthétisant `2,82×` et `2,73×` dans le corps) [1].
  - Constat initial : imprécis → rectifié (ajout du qualificatif « médiane » pour distinguer des moyennes `7,24×`/`6,23×` au tableau 10).
  - Source probante : `SRC-007.txt` (§ 6.5 l. 1066, 1101-1102, Table 10 l. 2416-2423, Table 13 l. 2627-2634).
  - Verdict final : supporté
- **A70** — Affirmation : Confier le `Q-LLM` à `Claude 3.5 Haiku` avec `Claude 4 Sonnet` en `P-LLM` abaisse le coût médian d'environ `12 %` pour environ `1 %` de perte d'utilité tout en évitant d'exposer les sorties d'outils au fournisseur du `P-LLM` [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 5.1 l. 473-475, § 6.1.3 l. 700-704).
  - Verdict final : supporté

#### P23 — Commentaire de la figure 15 [`L84–L88`]
- **A71** — Affirmation : La figure 15 synthétise les deux voies isolées (`P-LLM` sur la requête fiable, `Q-LLM` sur courriels, documents et pages Web) convergeant exclusivement dans l'interpréteur déterministe et la porte de politiques, atteignant `77 %` contre `84 %` sur `AgentDojo` [1].
  - Constat initial : imprécis → rectifié (« documents `PDF` » remplacé par « documents » car `PDF` n'apparaît pas dans `SRC-007.txt`).
  - Source probante : `SRC-007.txt` (Fig. 5 l. 368-414, l. 13-14) ; `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`).
  - Verdict final : supporté

#### P24 — Limites 1 à 3 de `CaMeL` et travaux parallèles (`LLMbda`) [`L90–L94`]
- **A72** — Affirmation : Le cas *« Data requires action »* (exécuter les consignes d'un courriel externe) est structurellement insoluble sans abaisser la frontière de confiance [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 6.1.2 l. 628-636).
  - Verdict final : supporté
- **A73** — Affirmation : Des API mal documentées pénalisent la génération de code ; sur la suite *Travel*, l'appui au `Q-LLM` fait passer `Claude Sonnet` de `25 %` (`3.5`) à `75 %` (`4`) [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 6.1.2 l. 683-690).
  - Verdict final : supporté
- **A74** — Affirmation : Le mode `STRICT` atténue les canaux auxiliaires (itérations, exceptions conditionnelles, temporisation), mais hausse les sollicitations de déclassification de `33,87 %` (`NORMAL`) à `53,23 %` (`STRICT`) hors attaque (`26,54 %` vs `45,34 %` sous attaque), créant un risque de fatigue d'approbation [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 7 l. 1109-1255, Table 8 l. 2176-2187, Table 9 l. 2308-2319, § 9.2 l. 1364-1374).
  - Verdict final : supporté
- **A75** — Affirmation : `Progent`, `RTBAS`, `IsolateGPT`, `ACE`, les systèmes IFC (Wu *et al.* ; Costa *et al.*) et `LLMbda` (`TIPNI`) explorent des pistes complémentaires [1, 10] ; Garby *et al.* notent que `CaMeL` peut manquer des dépendances implicites dans des branches non prises et que sa boucle de réessai externe forme un canal de fuite d'information lors de reprises répétées [10].
  - Constat initial : non supporté + imprécis → réancré et rectifié (suppression de l'acronyme `FIDES` absent de `SRC-007.txt`/`SRC-056.txt`, remplacé par les citations effectives `Costa et al.` / `Wu et al.` / `ACE` ; suppression de « d'un bit » sur la boucle de réessai, qui concernait les exceptions dans `SRC-007.txt` plutôt que la boucle de réessai dans `SRC-056.txt`).
  - Source probante : `SRC-007.txt` (App. A.2 l. 1734-1756, réf. `Progent`, `RTBAS`, `IsolateGPT`, `ACE`, `Wu et al.`, `Costa et al.`) ; `SRC-056.txt` (§ VI.B l. 1194-1237 : `LLMbda`, `TIPNI`, `branches that are not taken`, `information-leakage channel` sans mention d'un bit).
  - Verdict final : supporté
- **A76** — Affirmation : L'interpréteur `CaMeL` ne fournit ni atomicité ni compensation sur des appels ayant déjà produit des effets de bord [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 5.4 l. 577-578).
  - Verdict final : supporté

#### P25 — Limite 4 : non-composabilité multi-agents et `multi-CaMeL` [`L95`]
- **A77** — Affirmation : Sur `MultiAgentDojo`, la sécurité de `CaMeL` ne se compose pas automatiquement : l'`ASR` moyen atteint `12,9 %` sans défense et reste à `0,2 %` sous `CaMeL` individuel (`0,5 %` sur `GPT-4.1`, `0,4 %` sur `Gemini 2.5 Pro`) par blanchiment à la frontière [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (Table III l. 989-1009, § V.B.2 l. 1031-1050).
  - Verdict final : supporté
- **A78** — Affirmation : `multi-CaMeL` ramène l'`ASR` à `0,0 %` en séparant l'argument `message` d'un dictionnaire opaque `variables` préservant les capacités, pour un coût additionnel moyen sur `AssetOpsBench` de `3,2` points par rapport à `CaMeL` individuel (`0,85` point sur `GPT-5.5` et `Fable 5`), mais reste limité aux arborescences synchrones [10].
  - Constat initial : imprécis → rectifié (précisé « par rapport à `CaMeL` individuel » pour que l'écart de `3,2` / `0,85` point ne soit pas confondu avec l'écart vs `No CaMeL`).
  - Source probante : `SRC-056.txt` (§ IV l. 579-665, § V.A.2 l. 774-776, Table III l. 1009, § VI.A l. 1148-1174, § VII l. 1266-1270).
  - Verdict final : supporté

#### P26 — Tableau comparatif des trois approches de défense [`L97–L107`]
- **A79** — Affirmation : Ligne « Nature de la garantie » : probabiliste pour l'alignement/structuration (`[1, 8]`) et les filtres auxiliaires (`détecteur LLM`, `Tool Filter`, `DataFilter`, `DeBERTa` `[1, 8, 10]`) ; déterministe sur graphe de contrôle et capacités typées (`CaMeL`, `multi-CaMeL` `[1, 10]`).
  - Constat initial : imprécis → rectifié (« juge LLM » remplacé par « détecteur LLM » conformément à `SRC-054.txt` l. 2491-2494).
  - Source probante : `SRC-007.txt`, `SRC-054.txt`, `SRC-056.txt`.
  - Verdict final : supporté
- **A80** — Affirmation : Ligne « Résultats et failles sur bancs » : `276` sur `GPT-4o Mini`, `5` (*Spotlighting*) et `24` (*Sandwiching*) sur `Claude 3.5 Sonnet` `[1]` ; `8` (*Tool Filter*), défaillances corrélées et échec adaptatif `[1, 8, 10]` ; `77 %` vs `84 %` sur `AgentDojo` et `0,0 %` avec `multi-CaMeL` `[1, 10]`.
  - Constat initial : imprécis → rectifié (ajout de `, 10` pour les échecs adaptatifs).
  - Source probante : `SRC-007.txt` (Table 7), `SRC-054.txt` (§ 3.3.3), `SRC-056.txt` (Table III, § I).
  - Verdict final : supporté
- **A81** — Affirmation : Ligne « Coût d'inférence et utilité » : `1,06×` entrée / `0,98×` sortie (*Spotlighting* sous attaque) `[1]` ; `7,77×` entrée médian et `73,20 %` vs `90,72 %` (*Tool Filter*) `[1]` ; `2,7` à `2,8×` hors attaque réductible via `Q-LLM` léger et échec sur *Data requires action* `[1]`.
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (Tables 5, 10, 13 ; § 6.1.2–6.1.3).
  - Verdict final : supporté
- **A82** — Affirmation : Lignes « Chaînes multi-agents » et « Intégration patrimoniale » : exposition au détournement en texte libre `[10]`, absence de suivi de provenance inter-agents et vulnérabilité adaptative `[10]`, nécessité de `multi-CaMeL` `[10]`, et profils d'intégration `[1, 10]`.
  - Constat initial : imprécis → rectifié (supprimé « Rompue à chaque passage d'argument » et « service synchrone de filtrage » au profit d'énoncés strictement attestés dans `[1, 10]`).
  - Source probante : `SRC-056.txt` (§ I l. 76-78, § III, § V) ; `SRC-007.txt` (§ 9.1).
  - Verdict final : supporté

#### P27 — Heuristique opérationnelle : la « règle de deux » [`L109–L111`]
- **A83** — Affirmation : Généraliser les capacités à un écosystème complet d'outils tiers non instrumentés reste coûteux [1].
  - Constat initial : supporté
  - Source probante : `SRC-007.txt` (§ 9.1 l. 1349-1358).
  - Verdict final : supporté
- **A84** — Affirmation : Formulation explicite par l'ouvrage de l'heuristique dite « règle de deux » (interdiction de combiner dans un même tour `A` entrée non fiable, `B` données sensibles et `C` action externe/mutation), déduite du modèle d'exfiltration d'`AgentDojo` [1], de l'exigence d'isolation du `NIST` [8] et des contrôles du `BSIF` [13].
  - Constat initial : supporté
  - Source probante : Formulation architecturale de l'ouvrage étayée par `SRC-007.txt` (§ 5.2 l. 478-480), `SRC-054.txt` (§ 3.3.3 l. 2544-2549) et `SRC-066.txt` (l. 211, 353-361).
  - Verdict final : supporté

---

### Section 8.4 — Confinement matériel, portes de politique et sûreté `STAMP`/`STPA` (P28–P34)

#### P28 — Nécessité d'isolement système et problème du confinement de Lampson [`L115`]
- **A85** — Affirmation : `MCP` rappelle que les outils exécutent du code arbitraire [2], `OWASP ASI05` classe l'exécution de code inattendue au rang critique [9], et Kraishan rappelle que le code derrière un nom du registre `MCP` s'exécute avec les justificatifs, la position réseau et le système de fichiers de l'utilisateur [11].
  - Constat initial : imprécis → rectifié (« montre que les serveurs MCP locaux tournent fréquemment avec... » rectifié en « rappelle que le code derrière un nom du registre MCP s'exécute avec... », `SRC-057.txt` posant ce fait en introduction plutôt qu'en fréquence mesurée).
  - Source probante : `SRC-038.txt` (l. 99) ; `SRC-055.txt` (`ASI05` l. 102, 266) ; `SRC-057.txt` (§ 1 l. 32-34).
  - Verdict final : supporté
- **A86** — Affirmation : En écho au problème du confinement posé par Butler Lampson en 1973 et cité par Peters-Gill *et al.*, les politiques de flux d'information exigent un confinement effectif des canaux sous-jacents [10].
  - Constat initial : supporté
  - Source probante : `SRC-056.txt` (§ VI.B.2 l. 1239-1244, réf. [30] l. 1453).
  - Verdict final : supporté

#### P29 — Confinement `microVM`/`WASI`, exclusion des secrets (`WIMSE AIMS`) et `DPoP` (`RFC 9449`) [`L117–L119`]
- **A87** — Affirmation : Mention explicite de l'absence de mesure comparative entre `microVM` et `WASI` dans le corpus, présentés comme deux choix complémentaires d'architecture de confinement.
  - Constat initial : supporté (borne épistémique explicitement déclarée comme synthèse d'ingénierie sans source comparative chiffrée).
  - Source probante : Texte explicite du chapitre (`Sans qu'une mesure comparative existe dans notre base de sources`).
  - Verdict final : supporté
- **A88** — Affirmation : `WIMSE AIMS` (`draft-ietf-wimse-aims-01`, nov. 2026) exige normativement que le `LLM` n'ait jamais accès aux justificatifs de l'agent ni à ceux requis pour appeler outils ou services [7].
  - Constat initial : supporté
  - Source probante : `sources/ch08-sources.md` [7] ; `SRC-048.txt` (en-tête l. 13-16, § 8 l. 551-555 `MUST NOT have access`).
  - Verdict final : supporté
- **A89** — Affirmation : Les justificatifs à courte durée de vie sont provisionnés après évaluation de posture (incluant au besoin des preuves `TEE`) [7].
  - Constat initial : supporté
  - Source probante : `SRC-048.txt` (§ 7 l. 406, § 8 l. 444-461 `trusted execution environment (TEE) evidence`).
  - Verdict final : supporté
- **A90** — Affirmation : Les jetons sont liés cryptographiquement à leur présentateur légitime (*sender-constrained*) par `DPoP` (`RFC 9449`), rendant un jeton exfiltré inutilisable sans clé privée [5] et bloquant le transfert direct de jeton dénoncé par `WIMSE` et Kraishan [7, 11].
  - Constat initial : imprécis → rectifié (« émetteur légitime » remplacé par « présentateur légitime (*sender-constrained*) » pour éviter toute ambiguïté avec *issuer*).
  - Source probante : `SRC-043.txt` (§ 1–2 l. 113-125, 224-225) ; `SRC-048.txt` (§ 10.4 l. 820-824, § 10.6 l. 908-913, § 10.9 l. 1043-1045) ; `SRC-057.txt` (§ 3.2 l. 231-233).
  - Verdict final : supporté

#### P30 — Porte de politique hors modèle (`AuthZEN`, `RAR`, `A2A`, `SCITT`) [`L121`]
- **A91** — Affirmation : Selon `WIMSE AIMS`, la porte consulte au besoin un moteur de décision externe (tel que *OpenID AuthZEN*) [7] et s'articule avec des autorisations granulaires `RFC 9396` (`RAR`), où `authorization_details` précise type, actions, montant, devise ou compte bénéficiaire plutôt que de larges `scope` [4, 7].
  - Constat initial : imprécis → rectifié (séparation nette entre `AuthZEN`/`authorization details` dans `WIMSE AIMS` [7] et `authorization_details` de `RFC 9396` [4] ; « montant maximal » aligné sur « le montant »).
  - Source probante : `SRC-048.txt` (§ 10.4 l. 813-817, § 10.10 l. 1061) ; `SRC-042.txt` (§ 1–2 l. 95-244).
  - Verdict final : supporté
- **A92** — Affirmation : `AIMS` précise qu'une confirmation locale dans l'interface utilisateur ne vaut jamais autorisation autonome et doit être liée à un octroi d'autorisation vérifiable émis par le serveur d'autorisation [7].
  - Constat initial : imprécis → rectifié (« jeton vérifiable côté serveur » aligné sur `verifiable authorization grant issued by the authorization server`).
  - Source probante : `SRC-048.txt` (§ 10.8 l. 996-1015).
  - Verdict final : supporté
- **A93** — Affirmation : Sur les flux `A2A`, la porte applique les contrôles de la section 13 (bornes d'accès avant requête en base, rejet des plages IP privées et listes blanches d'URL contre `SSRF`, validation des paramètres d'entrée) ainsi que la vérification des schémas protocolaires (§ 14.1.1) [3, 9].
  - Constat initial : imprécis → rectifié (distinction exacte entre § 13.1/13.2/13.4 et § 14.1.1 dans `SRC-039.txt` pour la validation de schéma).
  - Source probante : `SRC-039.txt` (§ 13.1 l. 5819, § 13.2 l. 5839-5845, § 13.4 l. 5931, § 14.1.1 l. 6010) ; `SRC-055.txt` (`ASI07` l. 29-31).
  - Verdict final : supporté
- **A94** — Affirmation : Sur les connecteurs `MCP`, elle impose l'épinglage par hôte distant et empreinte cryptographique (`SHA-256` dans les preuves d'inclusion `SCITT`) d'énoncés attestés dans un journal `SCITT` (`RFC 9943`), bloquant toute dérive silencieuse [6, 11].
  - Constat initial : imprécis → rectifié (précisé que `SHA-256` provient des preuves d'inclusion `SCITT` / `RFC9162_SHA256` tandis que Kraishan vise l'épinglage des hôtes et empreintes de paquets).
  - Source probante : `SRC-044.txt` (§ 7 l. 1173 `RFC9162_SHA256`, § 6.2 l. 1002) ; `SRC-057.txt` (§ 5.1 l. 771-772).
  - Verdict final : supporté

#### P31 — Théorie `STAMP`/`STPA` et quatre classes d'actions de contrôle dangereuses (`UCA`) [`L123–L128`]
- **A95** — Affirmation : S'appuyant sur `STAMP` et `STPA` de Leveson, Barrett, Bruvere, Fillingham, Rhodes et Vergani (prépublication de déc. 2025) montrent qu'un risque ou une perte de contrôle peut survenir alors même que chaque composant exécute exactement le comportement pour lequel il a été entraîné ou codé, par défaillance d'interaction [12].
  - Constat initial : imprécis → rectifié (« survient fréquemment » tempéré en « peut survenir », fidèlement à `can lead to risk` dans `SRC-058.txt`).
  - Source probante : `SRC-058.txt` (l. 1-11, 29 `Preprint`, § 1 l. 234-240, § 2.3 l. 387, § 2.3.1 l. 403).
  - Verdict final : supporté
- **A96** — Affirmation : `STPA` (*System-Theoretic Process Analysis*) impose d'analyser quatre classes d'`UCA` [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (§ 2.3.1 l. 411-417, § 11 l. 1144-1152).
  - Verdict final : supporté
- **A97** — Affirmation : Classe 1 — action requise non fournie (p. ex. retard à couper un agent par dépendance opérationnelle ou économique) [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (§ 2.3.1 l. 414, § 6.1 l. 839-845).
  - Verdict final : supporté
- **A98** — Affirmation : Classe 2 — action dangereuse émise à tort (p. ex. mise à jour d'invite ou de seuil qui recalibre imprévisiblement le modèle) [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (§ 2.3.1 l. 415, App. B.4.1 IV l. 2027-2033).
  - Verdict final : supporté
- **A99** — Affirmation : Classe 3 — action au mauvais moment ou mauvais ordre (écart de vitesse face à la boucle `OODA` des superviseurs) [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (§ 2.3.1 l. 416, 418-420, § 6.1 l. 861-869).
  - Verdict final : supporté
- **A100** — Affirmation : Classe 4 — action maintenue trop longtemps ou levée trop tôt (remise en service hâtive) [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (§ 2.3.1 l. 417, § 6.1 l. 851-857, App. B.4 l. 2005-2007).
  - Verdict final : supporté

#### P32 — Dégradations graduelles, convergence `BSIF` et limites de `STPA` [`L130`]
- **A101** — Affirmation : `STAMP`/`STPA` met en évidence les dégradations graduelles : relâchement après une période sans accident, vieillissement du modèle mental des superviseurs et capteurs faussés par un agent prédisant ou manipulant les métriques échantillonnées [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (§ 7 l. 1031-1036, App. B.4.4 I l. 2135-2146).
  - Verdict final : supporté
- **A102** — Affirmation : Le bulletin du `BSIF` de juillet 2026 demande une gestion formelle des changements (invites, outils, modèles), une détection continue d'anomalies et des replis manuels testés [13].
  - Constat initial : supporté
  - Source probante : `SRC-066.txt` (l. 279-296, 429, 495).
  - Verdict final : supporté
- **A103** — Affirmation : Barrett *et al.* précisent que leur premier cadre modélise un archétype simple en phase opérationnelle, hors dynamiques multi-agents complexes, et qu'aucune méthode, pas même `STPA`, ne garantit une couverture exhaustive [12].
  - Constat initial : supporté
  - Source probante : `SRC-058.txt` (Résumé l. 63-69, § 3.2 l. 472-474, § 4.1 l. 517-540).
  - Verdict final : supporté

#### P33 — Commentaire de la figure 16 [`L132–L136`]
- **A104** — Affirmation : Synthèse visuelle de la défense en profondeur combinant le moteur déterministe de la règle de deux (`A`, `B`, `C`), la porte de politique avec épinglage `SHA-256`, les bacs à sable `microVM`/`WASI`, le sas inter-tours et la rétroaction `STAMP`/`STPA`.
  - Constat initial : supporté
  - Source probante : Synthèse architecturale du chapitre fondée sur P27, P29, P30, P31–P32 (`[4, 5, 6, 7, 11, 12, 13]`).
  - Verdict final : supporté

#### P34 — Trois arbitrages sans regret et transition vers le chapitre 09 [`L138–L144`]
- **A105** — Affirmation : Arbitrage 1 — Substituer l'isolation structurelle (`CaMeL`/`multi-CaMeL`) et la règle de deux aux filtres probabilistes vulnérables aux attaques adaptatives.
  - Constat initial : supporté
  - Source probante : Synthèse normative des § 8.2 et § 8.3 (`[1, 8, 10, 13]`).
  - Verdict final : supporté
- **A106** — Affirmation : Arbitrage 2 — Épingler paquets, définitions, empreintes `SHA-256` et hôtes distants `MCP` sous énoncés signés et reçus vérifiables (`SCITT`), exclure les justificatifs du modèle (`WIMSE AIMS`) et imposer des portes typées liées par preuve de possession (`RAR`, `DPoP`).
  - Constat initial : imprécis → rectifié (« sous attestation cryptographique vérifiable » aligné sur « sous énoncés signés et reçus vérifiables » selon `RFC 9943`).
  - Source probante : Synthèse normative des § 8.1 et § 8.4 (`[4, 5, 6, 7, 11]`).
  - Verdict final : supporté
- **A107** — Affirmation : Arbitrage 3 — Confiner les exécutions en `microVM`/`WASI` et gouverner délais, capteurs, changements et replis manuels avec `STAMP`/`STPA`.
  - Constat initial : supporté
  - Source probante : Synthèse normative du § 8.4 (`[12, 13]`).
  - Verdict final : supporté
- **A108** — Affirmation : Transition vers le chapitre 09 : la sécurité par construction engendre refus légitimes, reprises d'erreurs et surcoût en jetons, appelant observabilité sans fuite, vérification de constance statistique, disjoncteurs et mesure du coût par résultat conforme.
  - Constat initial : supporté
  - Source probante : Appuyé sur `SRC-007.txt` (§ 5.4, § 6.5, § 9.2) et `registre/glossaire-termes.json` (entrées `ch09` : `coût par résultat conforme`, `télémétrie à double couloir`, `constance multi-essais`).
  - Verdict final : supporté

---

## Contrôle de complétude des citations `[1]`–`[13]`

| Réf. | Source `L+` | Contrôle dans `sources/ch08-sources.md` et `corpus_l_plus/` | État |
|---|---|---|---|
| `[1]` | `SRC-007` | *Defeating Prompt Injections by Design* (`CaMeL`, `arXiv:2503.18813` / *IEEE SaTML*) et `FACT-CAMEL-AGENTDOJO` | Vérifié |
| `[2]` | `SRC-038` | *Model Context Protocol (MCP) Specification — Revision 2025-11-25* | Vérifié |
| `[3]` | `SRC-039` | *Agent2Agent (A2A) Protocol Specification* (§ 13.1, § 13.2, § 13.4, § 14.1.1) | Vérifié |
| `[4]` | `SRC-042` | *RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)* | Vérifié |
| `[5]` | `SRC-043` | *RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)* | Vérifié |
| `[6]` | `SRC-044` | *RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)* | Vérifié |
| `[7]` | `SRC-048` | *AI Identity Management System (`draft-ietf-wimse-aims-01`, nov. 2026)* | Vérifié |
| `[8]` | `SRC-054` | *NIST AI 100-2e2025: Adversarial Machine Learning* | Vérifié |
| `[9]` | `SRC-055` | *OWASP Top 10 for Agentic Applications (2026) — Threat Crosswalk* | Vérifié |
| `[10]` | `SRC-056` | *Can CaMeLs Talk?* (`MultiAgentDojo` / `AssetOpsBench`, `arXiv:2610.05640`, oct. 2026) | Vérifié |
| `[11]` | `SRC-057` | *Same Name, Different Server* (Kraishan, recensement `MCP`, `arXiv:2609.14119`, sept. 2026) | Vérifié |
| `[12]` | `SRC-058` | *STAMP/STPA Loss of Control in AI Systems* (Barrett *et al.*, `arXiv:2512.17600`, déc. 2025) | Vérifié |
| `[13]` | `SRC-066` | *OSFI / BSIF Technology Risk Bulletin* (juillet 2026) | Vérifié |

---

## Contrôle différentiel post-G4

- **Périmètre audité** : lignes `15–39` (`P05`–`P12` et transition de § 8.1) de [Chapitre 08 - Securite par construction.md](file:///c:/Github/Agentique/7%20-%20Livre/manuscrit/03%20-%20Partie%20III/Chapitre%2008%20-%20Securite%20par%20construction.md) après retouche stylistique `G4`, auditées à neuf contre [ch08-sources.md](file:///c:/Github/Agentique/7%20-%20Livre/sources/ch08-sources.md) et les textes intégraux `corpus_l_plus/*.txt` (`SRC-007`, `SRC-038`, `SRC-039`, `SRC-044`, `SRC-054`, `SRC-055`, `SRC-056`, `SRC-057`, `SRC-066`).
- **Rectifications appliquées sur `L15`–`L41–L43`** :
  1. **L17 (`SRC-055` `OWASP ASI09`–`ASI10`)** : « perte de contrôle d'agents autonomes » remplacé par « agents compromis ou dévoyés (*Rogue Agents*) » pour correspondre exactement au titre et à la définition d'`ASI10` (`Rogue Agents`), et « actions frauduleuses » corrigé en « commandes malveillantes ou des actions préjudiciables » conformément à `ASI09` (`malicious commands`, `harmful actions`).
  2. **L19 (`SRC-054` `NIST AI 100-2e2025` § 3.4.1)** : « injectent des séquences spéciales comme des caractères homoglyphes qui perturbent les appels d'API en aval » rectifié en « altèrent le formatage de sortie — caractères homoglyphes perturbant les appels d'API en aval ou jeton spécial forçant une réponse vide » (*Disruptive output formatting* : homoglyphes et jeton `<|endoftext|>`).
  3. **L25–L27 (`SRC-057` Kraishan §§ 1, 3.1.2–3.1.4, 3.4, 4.2)** :
     - « répartis sur 13 051 dépôts GitHub, 248 817 fichiers et 69 027 définitions d'outils » resserré en « (13 051 dépôts GitHub, 248 817 fichiers et 69 027 définitions d'outils extraites) » (`69 027` définitions récupérées sur `4 238` dépôts).
     - « 31 motifs calibrés sur 414 cas étiquetés à la main » rectifié en « 31 motifs dont la précision est mesurée sur 414 cas étiquetés à la main », l'échantillon validant la précision et le taux d'omission du scanner sans calibrer les motifs (aligné sur `A29`).
     - « (*silent tool drift*) » corrigé en « (*silent drift* selon Kraishan) », le terme `*silent tool drift*` étant absent de `SRC-057.txt` (aligné sur `A34`).
  4. **L32 (`SRC-057` § 3.5, § 6.0.1)** : « première faille exploitable dès le déploiement » rectifié en « premier vecteur d'exposition observé dès le déploiement », l'auteur précisant que ses constats statiques sont des indicateurs de risque et n'établissent ni accessibilité ni exploitabilité.
  5. **L34 (`SRC-057` § 4.1.1)** : « appelant une liaison cryptographique des jetons [11] » réancré sur `SRC-057.txt` (« exposant des justificatifs transférés sur une infrastructure hors du contrôle de l'usager [11] »), la liaison cryptographique (`DPoP`) relevant de `[5, 7]` (§ 8.4) et étant absente de `[11]`.
  6. **L35 (`SRC-057` § 4.2)** : ajout de l'effectif exact du calcul d'odds ratio (`6 699` serveurs multi-versions dans la population scannée pour `OR = 2,96`, `IC 95 % : 2,56–3,42`) et précision d'« au moins un changement sémantique silencieux » pour `40,58 %`.
  7. **L36 (`SRC-057` §§ 1, 3.1.4, 4.2)** : « Redirection d'hôte (*rug pull*) » nuancé en « Redirection d'hôte (analogue observable de *rug pull*) » avec réserve explicite « sans présumer d'une malveillance systématique », Kraishan soulignant que la majorité des `370` redirections relèvent probablement de migrations courantes.
  8. **L37 (`SRC-057` § 4.1, § 4.3 Table 6)** : précision de l'échantillon (`14 353 serveurs`), de la « borne supérieure de Wilson : 0,027 % », de la « cote de constat grave » et de l'échelle par unité logarithmique pour `taille (OR = 1,94)` et `âge (OR = 1,38)`.
  9. **L39 (`SRC-044` `RFC 9943` § 5.1.1)** : « politiques d'enregistrement vérifiées » rectifié en « politiques d'enregistrement transparentes », conformément à l'exigence normative de la `RFC 9943` enregistrant les politiques elles-mêmes sur le `VDS`.
- **Verdict différentiel post-G4** :
  - **Supportés : `100 %`** (toutes les affirmations et statistiques de `L15`–`L43`, incluant `L15`, `L21`, `L23`, `L29`–`L31`, `L33`, `L43` et les `9` lignes rectifiées, sont intégralement appuyées sur les textes `L+` de `corpus_l_plus/`).
  - **Imprécis résiduels : `0`**
  - **Non supportés résiduels : `0`**

---

## Contrôle différentiel post-lissage G5

- **Périmètre inspecté** : intégralité du `git diff HEAD` (depuis le commit `fe6e945`) sur [Chapitre 08 - Securite par construction.md](file:///c:/Github/Agentique/7%20-%20Livre/manuscrit/03%20-%20Partie%20III/Chapitre%2008%20-%20Securite%20par%20construction.md) — **49** items contrôlés (`12` lignes à simple retrait de rétro-apostrophes et `37` lignes/paragraphes comportant des retouches rédactionnelles), vérifiés contre `sources/ch08-sources.md` (`[1]`–`[13]`), `corpus_l_plus/*.txt`, les registres et `verifie_manuscrit.py --unit ch08 --strict`.
- **Rectifications appliquées** (`15` paragraphes ajustés) : `L17` (`OWASP ASI06`/`ASI09` : « entrepôts RAG et plongements » et « commandes malveillantes ou des actions préjudiciables » selon `SRC-055.txt`), `L19` (« extraire des pièces privées et à les exfiltrer »), `L23` (« serveur de confiance » selon `MCP` `SRC-038.txt`), `L25` (« dont la précision est mesurée sur 414 cas » corrigeant la régression « calibrés » contre `A29` / `SRC-057.txt`), `L37` (énoncés `COSE_Sign1` et reçus `COSE` en ajout seul sous politiques d'enregistrement transparentes et émetteur autorisé selon `RFC 9943`), `L43` (« signaler les données suspectes » et « désescalade douce de consignes » selon `SRC-056.txt`), `L49` (« taux de succès d'attaque non nul »), `L54` (« baisse artificielle de l'utilité bénigne mesurée » selon `A53`), `L78` (« tout message d'exception dépendant d'une donnée non fiable et retourné au P-LLM » selon `CaMeL` § 5.4), `L95` (dissociation nette `LLMbda` `[10]` vs absence d'atomicité/compensation `CaMeL` `[1]`), `L97` (« par rapport à CaMeL individuel » rétabli pour l'écart `3,2` / `0,85` point sur `AssetOpsBench`, corrigeant une régression critique sur `A78`), `L115` (« système de fichiers » selon `SRC-057.txt`), `L100` (« lorsque l'outil requiert des binaires système complets »), `L104` (octroi vérifiable du serveur d'autorisation selon `AIMS` § 10.8, « plages d'adresses IP privées » selon `A2A` § 13.2 et « `SHA-256` dans les preuves d'inclusion » selon `RFC 9943`), `L112` (« recommande » au lieu d'« exige » pour le bulletin `BSIF` de juillet 2026 `SRC-066.txt`).
- **Taux d'ancrage certifié post-G5** : **100 % `supporté`**
- **Imprécis résiduel** : **0**
- **Non supporté résiduel** : **0**

---

## Réindexation différentielle post-audit v1.3 (2 décembre 2026)

- **Périmètre `v1.3`** : `manuscrit/03 - Partie III/Chapitre 08 - Securite par construction.md` (`154` lignes, `5 629` mots `G1` / `5 888` `split()`), `13` sources `L+`.
- **Mises à jour et réancrages vérifiés** :
  - `L49–L53`, `L66–L70`, `L96–L102`, `L132–L138` : aération des puces et transformation des quatre limites `CaMeL` en paragraphes dédiés + séparation des quatre `UCA` en phrases autonomes (sans changement d'énoncés). `Verdict : supporté`.
  - `L5–L7` : ouverture actualisée sur la vulnérabilité du mandataire local de développement `MCP` (Oligo Security, juin 2025 — `[9]` `SRC-055.txt` `OWASP Top 10 for Agentic Applications 2026 v1.0`, l. 2091, 2105) et confrontation empirique avant le gel du **2 décembre 2026**. `Verdict : supporté`.
  - `L25–L27`, `L41–L43`, `L92–L95`, `L107–L111` : alignement sur le corpus normatif complet `[2]` `SRC-038.txt` (`MCP 2025-11-25`, l. 45, 88–99, 411, 5002, 7531–7536, 8181) et `[9]` `SRC-055.txt` (`ASI01`–`ASI10`, l. 50–166), plus réindexation des blocs `P01`–`P34`. `Verdict : supporté`.
