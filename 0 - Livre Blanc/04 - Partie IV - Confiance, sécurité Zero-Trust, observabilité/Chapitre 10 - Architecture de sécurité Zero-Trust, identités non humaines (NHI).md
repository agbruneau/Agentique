# Chapitre 10 — Architecture de sécurité Zero-Trust, identités non humaines (NHI) et maîtrise des risques

L’ouverture des systèmes d’information aux agents autonomes bouleverse la sécurité périmétrique. Dans une application web déterministe, le code compilé n’emprunte que des chemins prévus et sa surface d’attaque réside dans ses interfaces réseau, ses dépendances et ses droits d’accès. Un `System of Agency` (chapitre 01) rompt ce postulat en plaçant un moteur probabiliste au cœur du plan de décision, alimenté à la fois par des directives privilégiées et par des données externes non fiables — courriels, documents ou retours `MCP` — tout en pouvant agir sur les `Systems of Record` (`SoR`) [204] [205]. Parce qu’un grand modèle de langage ne sépare pas fiablement données et instructions, l’héritage implicite de privilèges ou la confiance accordée au réseau interne transforme une simple lecture documentaire en vecteur d’exfiltration ou de mutation illicite [206] [205] [207].

Appliquer les principes **Zero-Trust** (`NIST SP 800-207`) à l’entreprise agentique impose d’éliminer toute confiance implicite et de vérifier chaque identité, chaque intention et chaque flux à chaque frontière d’exécution [207]. Ce chapitre décline cette exigence selon une double lecture **EA** (*Enterprise Architect* : gouvernance du risque, domaines de confiance, maîtrise du rayon d’impact) et **SA** (*Solution Architect* : attestation cryptographique, délégation OAuth, portes de politiques déterministes et isolation système). Par frontière d’étanchéité, ce chapitre couvre exclusivement la sécurité technique, les identités non humaines (`NHI`) et le contrôle d’accès : l’instrumentation `OpenTelemetry` et les coupe-circuits `SRE` relèvent du chapitre 11, tandis que la conformité réglementaire est traitée au chapitre 12.

## 10.1 Modèle de menaces OWASP Agentic Top 10 : Goal Hijacking, Confused Deputy et injections indirectes

### 10.1.1 De l’OWASP `LLM01` au référentiel `OWASP Top 10 for Agentic Applications` (`ASI01` –`ASI10`)

Les premiers déploiements génératifs ont souvent réduit la sécurité de l’IA à la prévention des contournements directs (*jailbreaks*) saisis par un utilisateur [206]. Si `LLM01:2025` (*Prompt Injection*) demeure le premier risque de l’`OWASP Top 10 for LLM Applications` [206], la planification autonome, la mémoire persistante et les protocoles `MCP` et `A2A` (chapitres 04 et 05) étendent nettement la surface d’exposition [204] [208]. L’initiative `OWASP GenAI Security Project` a donc publié le **OWASP Top 10 for Agentic Applications** (`ASI01` –`ASI10`), qui complète la taxonomie adversariale `NIST AI 100-2 E2025` (évasion, empoisonnement, confidentialité et détournement d’usage), la base `MITRE ATLAS` et le modèle en sept couches `MAESTRO` de la *Cloud Security Alliance* (*Foundation Models*, *Data Operations*, *Agent Frameworks*, *Deployment and Infrastructure*, *Evaluation and Observability*, *Security and Compliance*, *Agent Ecosystem*) [204] [209] [210].

Ces référentiels montrent que les dix risques agentiques s’enchaînent selon une **dynamique d’amplification** [204] [208] :

1. `ASI01` **(*Agent Goal Hijack*) et** `ASI02` **(*Tool Misuse Exploitation*)** amorcent l’attaque : en réorientant la trajectoire décisionnelle, l’adversaire pousse l’agent à appeler des outils légitimes avec des paramètres destructeurs ou hors mandat [204].

2. `ASI03` **(*Identity Privilege Abuse*) et** `ASI04` **(*Agentic Supply Chain Vulnerabilities*)** convertissent la dérive en mouvement latéral via des jetons hérités trop larges ou des serveurs `MCP`, prompts et greffons compromis [204].
3. `ASI05` **(*Unexpected Code Execution*) et** `ASI06` **(*Memory Context Poisoning*)** ancrent l’attaque par exécution de code non confinée ou corruption durable des mémoires et index `RAG` (traitée au chapitre 06) [204].
4. `ASI07` **(*Insecure Inter-Agent Communication*),** `ASI08` **(*Cascading Agent Failures*),** `ASI09` **(*Human-Agent Trust Exploitation*) et** `ASI10` **(*Rogue Agents*)** propagent l’incident sur des canaux `A2A` non authentifiés, trompent les valideurs humains et pérennisent des agents déviants hors contrôle [204] [208].

Les méthodes classiques orientées composants (`STRIDE`) peinent à saisir cette dynamique multi-couches, justifiant `MAESTRO` en complément d’`ASI01` –`ASI10` [209]. Le tableau 10.1 associe chaque catégorie aux verrous Zero-Trust de l’ouvrage.

| Catégorie OWASP | Mécanisme de menace | Vecteur dominant | Contrôle Zero-Trust principal | Renvoi |
| --- | --- | --- | --- | --- |
| `ASI01` *Goal Hijack* | Détournement d’objectif [204] | Injection indirecte [204] [205] | `CaMeL`, `Txn-Token`, `AIDR` [211] [212] [213] | `10.1`, `10.3`, ch. `07` |
| `ASI02` *Tool Misuse* | Abus d’outils légitimes [204] | Paramètres/chaînes non bornés [204] | `Intent Gate` (`OPA` /`Cedar`), `RAR` [214] [215] | `10.3`, ch. `04` |
| `ASI03` *Identity Abuse* | Abus de droits hérités [204] | *Token passthrough*, secrets statiques [216] [217] | `SPIFFE` /`SPIRE`, `OAuth OBO`, `DPoP` [218] [219] [220] | `10.2`, `10.3` |
| `ASI04` *Supply Chain* | Composants tiers piégés [204] | Serveurs `MCP`/prompts non vérifiés [204] | `AISPM` (`AI-BOM`), registre curé [221] [213] | `10.4`, ch. `04` –`05` |
| `ASI05` *Code Execution* | Exécution de code arbitraire [204] | Code généré hors bac à sable [208] | `Firecracker`, `Kata`, `gVisor`, `Wasmtime` [222] [223] [224] | `10.4`, ch. `03` |
| `ASI06` *Memory Poisoning* | Corruption de mémoire/`RAG` [204] | Documents piégés persistants [204] [205] | Provenance, filtres d’écriture, `ACL` [221] [211] | `10.1`, ch. `06` |
| `ASI07` *Inter-Agent Comm.* | Usurpation et rejeu `A2A` [204] | Canaux sans `mTLS` ni signature [204] | `X.509-SVID`, fédération, `WIMSE` [218] [225] [226] | `10.2`, ch. `05` |
| `ASI08` *Cascading Failures* | Propagation en cascade [204] | Boucles sans plafond de délégation [204] | Chaîne `act[]`, coupe-circuit `AIDR` [219] [213] | `10.3`, `10.4`, ch. `08`, `11` |
| `ASI09` *Trust Exploitation* | Tromperie d’opérateur `HITL` [204] | Prose persuasive sans preuve [204] | Seuils déterministes `Intent Gate` [221] [227] | `10.3`, ch. `01` |
| `ASI10` *Rogue Agents* | Agent compromis autonome [204] | Dérive persistante non détectée [204] | Corrélation `AIDR`, révocation `SVID` [225] [213] | `10.2`, `10.4` |

*Tableau 10.1 — Cartographie des dix risques OWASP Agentic AI (*`ASI01` *–*`ASI10`*) vers les contrôles techniques Zero-Trust.*

### 10.1.2 Injections indirectes et problème du *Confused Deputy* cognitif

L’injection indirecte, caractérisée par Greshake et al. [205], alimente la plupart des détournements `ASI01` [204]. Contrairement à l’injection directe saisie par l’appelant, l’injection indirecte dissimule des directives dans les ressources consultées par l’agent : pages web, courriels, documents malveillants ou retours d’outils façonnés [204] [205]. Parce que le modèle traite consigne système, requête et données externes dans une même séquence de jetons sans frontière matérielle code/données, une chaîne externe peut être interprétée comme une instruction prioritaire [206] [205] [228].

Cette indistinction réactive le problème du **Confused Deputy** (mandataire confus) [221]. L’agent agit comme un intermédiaire autorisé sur des outils internes (`CRM`, messagerie, dépôts de code) tout en ingérant des contenus non authentifiés [221] [205]. Des incidents sans clic (*zero-click*) sur des assistants de messagerie ont montré qu’un simple document ou courriel piégé peut conduire l’agent à extraire des données internes puis à les exfiltrer par un appel légitime [204] [205]. La faille est architecturale : tant que l’autorité reste attachée à la session sans contrôle du flot d’information, toute lecture non fiable contamine les actions aval [205] [211].

### 10.1.3 Défenses architecturales par conception : *Instruction Hierarchy* et séparation contrôle/données (`CaMeL`)

Les injonctions défensives dans le prompt système cèdent systématiquement devant des attaques adaptatives [206] [228]. Une défense robuste combine renforcement statistique du modèle et séparation déterministe dans l’`Agent Harness` [221] [228] [211].

Côté modèle, la **hiérarchie d’instructions** (*Instruction Hierarchy*) de Wallace et al. [228] entraîne le `LLM` à prioriser les consignes système privilégiées face aux requêtes utilisateurs et aux textes tiers de rang

inférieur [228]. Toutefois, cette propriété demeure probabiliste et n’offre aucune garantie formelle [206] [228] [211].

Pour atteindre une protection **par conception**, l’architecture **CaMeL** (*Defeating Prompt Injections by Design*) de Debenedetti et al. [211] isole strictement flot de contrôle et flot de données :

1. **Extraction privilégiée du flot de contrôle** : depuis la requête fiable seule — sans exposer le modèle aux données externes brutes — une couche privilégiée extrait le graphe de contrôle et de flux de données fixant quels outils seront invoqués et comment circuleront les résultats [211].
2. **Quarantaine des données non fiables** : les contenus externes (courriels, pages web) sont analysés par un modèle isolé privé d’accès direct aux outils ou à la modification du plan ; même compromis par injection indirecte, il ne peut altérer le flot du programme [211].
3. **Capacités et contrôle de provenance** : une couche d’exécution associe à chaque donnée sa provenance et vérifie des politiques de capacités avant chaque appel d’outil, bloquant toute exfiltration de données privées vers des flux non autorisés [211].

### 10.1.4 Double lecture EA / SA

Pour l’**EA**, `ASI01` –`ASI10` démontre que le risque croît multiplicativement avec l’autonomie, l’ouverture des sources ingérées et l’étendue des privilèges accordés aux connecteurs [204] [209]. L’EA doit proscrire en production le couplage direct entre lectures externes ouvertes et écritures `SoR` sans médiation déterministe [204] [221]. Pour le **SA**, toute sortie `LLM` et toute donnée tierce restent non fiables par défaut : il faut séparer l’analyse de données non fiables du flot de contrôle (`CaMeL` ou graphes déterministes du chapitre 03) et externaliser l’autorisation hors de la fenêtre contextuelle [206] [211].

> **Arbitrage EA / SA** — Ne jamais utiliser le prompt système, la hiérarchie d’instructions entraînée ou la fenêtre contextuelle d’un `LLM` comme frontière de sécurité [206] [228]. L’`EA` impose l’analyse de menaces `OWASP ASI01–ASI10` et `CSA MAESTRO` avant homologation et interdit le raccordement direct entre sources externes non fiables et mutations `SoR` [204] [209]. Le `SA` isole les flux non fiables du flot de contrôle (`CaMeL` ou workflow typé) et confie la prévention du *Confused Deputy* à des identités attestées et des portes de politiques déterministes [221] [211].

## 10.2 Identités non humaines (NHI) cryptographiques : attestation de workload SPIFFE/SPIRE et SVID éphémères

### 10.2.1 Crise des identités non humaines et taxonomie `OWASP NHI Top 10`

L’entreprise agentique multiplie les **identités non humaines** (`NHI`) : orchestrateurs, agents spécialisés, serveurs `MCP` et travailleurs durables exigent chacun une identité propre auprès des passerelles, modèles et `SoR` [221] [216]. Contrairement aux utilisateurs humains rattachés à un annuaire `RH` et à la `MFA`, ces charges sont créées, mises à l’échelle et recyclées dynamiquement sur Kubernetes ou des plateformes sans serveur [216].

Le référentiel `OWASP Non-Human Identities Top 10` (`NHI1:2025` –`NHI10:2025`) montre pourquoi les clés API et secrets statiques échouent [216] :

1. **Secrets persistants et fuites (**`NHI2`**,** `NHI7`**)** : les clés statiques en variables d’environnement ou fichiers de configuration n’expirent pas, fuient dans les dépôts ou traces et restent exploitables longtemps après fuite [216].
2. **Réutilisation et opacité (**`NHI9`**,** `NHI10`**)** : partager un compte de service entre agents ou humains détruit l’imputabilité, empêche l’isolement d’un agent déviant (`ASI10`) et banalise l’usage humain de comptes machines [204] [216].
3. **Sur-privilèges et dérive (**`NHI1`**,** `NHI5`**,** `NHI6`**,** `NHI8`**)** : l’absence de révocation automatique au retrait d’un agent, les rôles infonuagiques trop larges et la perméabilité entre environnements créent des vecteurs de déplacement latéral [216].

Selon `NIST SP 800-207`, l’identité d’un agent doit éliminer le secret statique initial (*secret zero*) au profit d’une attestation cryptographique dynamique du runtime [207] [216] [218].

### 10.2.2 Standard `SPIFFE`, architecture `SPIRE` et attestation à deux étages

Le standard CNCF **SPIFFE** (*Secure Production Identity Framework for Everyone*) et son implémentation **SPIRE** (*SPIFFE Runtime Environment*) automatisent cette attestation [218] [225]. Chaque charge reçoit un **SPIFFE ID** — URI normalisée `spiffe://<trust-domain>/<workload-identifier>` (ex. `spiffe://entreprise.ca/finance/facturation`) — rattaché à un *Trust Domain* et prouvé par un **SVID** (*SPIFFE Verifiable Identity Document*) vérifiable grâce au *Trust Bundle* public [218].

`SPIRE` articule un **SPIRE Server** central (registre d’enregistrements et autorité de signature) et un **SPIRE Agent** par nœud selon une **attestation à deux étages**, illustrée à la figure 10.1 [225] :

1. **Attestation du nœud (*Node Attestation*)** : au démarrage, le `SPIRE Agent` s’authentifie auprès du `SPIRE Server` via des greffons *Node Attestors* exploitant les preuves de l’infrastructure hôte, obtenant son `Node SVID` et le jeu d’enregistrements associés [225].
2. **Attestation de la charge (*Workload Attestation*)** : le processus appelant contacte la **SPIFFE Workload API** sur une socket de domaine Unix locale, sans secret initial [225]. Des greffons *Workload Attestors* interrogent le noyau et l’orchestrateur pour vérifier les **sélecteurs** du processus face aux règles enregistrées avant signature d’un `SVID` éphémère [225].

La spécification `SPIFFE` précise toutefois que cette garantie suppose l’isolation locale entre charges sur un même nœud afin qu’un processus compromis ne dérobe pas les justificatifs d’un voisin [218], justifiant le couplage direct avec les bacs à sable de la section `10.4`.

> **[Figure]**
> - Nœud / Infra hôte (Kernel & Orchestrateur)
> - SPIRE Server (Trust Domain A)
> - SPIRE Agent (Socket Unix locale)
> - Agent Harness &
> - Envoy SDS
> - Pair Domaine B (Trust Bundle B)
> - Nœud / Infra hôte (Kernel & Orchestrateur)
> - SPIRE Server (Trust Domain A)
> - SPIRE Agent (Socket Unix locale)
> - Agent Harness &
> - Envoy SDS
> - Pair Domaine B (Trust Bundle B)
> - 1. Attestation du nœud (Node Attestation — sans secret statique)
> - 1 Collecte preuve d'infrastructure (Node Attestor plugin)
> - 2 Preuve vérifiable du nœud
> - 3 Attestation de nœud (authentification automatique)
> - 4 Node SVID signé + cache des enregistrements
> - 2. Attestation de charge de travail (Workload API / SDS)
> - 5 Connecte socket Unix locale (SPIFFE Workload API / SDS)
> - 6 Inspecte sélecteurs du processus (Workload Attestors)
> - 7 Sélecteurs confirmés
> - 8 X.509-SVID éphémère (mTLS) + JWT-SVID / WIT-SVID + Trust Bundle
> - Rotation continue en mémoire via SDS : aucune clé privée ni jeton écrit sur disque (NHI7 éliminé).
> - 3. Authentification inter-domaines et fédération
> - 9 Échange SPIFFE Bundle Endpoint (Trust Bundles publics A <-> B)
> - 10 Requête mTLS (X.509-SVID) ou WIMSE WIT / JWT-SVID
> - 1 1 Vérifie SPIFFE ID (spiffe://domaine-a/agent/facturation) contre Trust Bundle A
> - 12 Canal authentifié établi

*Fig. 37. – Cycle d’attestation SPIFFE/SPIRE à deux étages, délivrance de SVID éphémères et fédération de domaines de confiance pour charges agentiques*

### 10.2.3 `SVID` éphémères, intégration `Envoy SDS`, fédération et `IETF WIMSE`

Les justificatifs `SVID` se renouvellent en continu sans redémarrage applicatif selon des profils complémentaires [218] [225] :

- **Le** `X.509-SVID` inscrit le `SPIFFE ID` dans l’extension *Subject Alternative Name* (`URI SAN`) d’un certificat X.509 à vie brève pour établir des liaisons `mTLS` [218] [229]. Couplé comme fournisseur *Secret Discovery Service* (`SDS`) au mandataire **Envoy**, le `SPIRE Agent` diffuse certificats, clés privées et *Trust Bundles* exclusivement en mémoire vive sans jamais écrire sur disque, supprimant `NHI2` et protégeant les échanges `A2A` (`ASI07`) [204] [216] [229].

- **Le** `JWT-SVID` encode le `SPIFFE ID` dans la revendication `sub` d’un jeton signé `JWT` destiné aux appels de couche 7 traversant des passerelles terminant le `TLS` [218] [225]. Jetons au porteur par nature, ils requièrent une vie très brève et une audience (`aud`) strictement ciblée [218].
- **L’architecture** `IETF WIMSE` **et le** `WIT-SVID` : la spécification `draft-ietf-wimse-arch` dissocie la preuve cryptographique de l’identité de charge — *Workload Identity Token* (`WIT`, auquel correspond le profil `WIT-SVID` dans SPIFFE/SPIRE) ou certificat accompagné d’une preuve de possession — de la propagation du contexte utilisateur ou transactionnel [225] [226].

Entre grappes ou organisations partenaires (chapitre 05), `SPIRE` fédère les domaines via des *SPIFFE Bundle Endpoints* échangeant leurs *Trust Bundles* publics sans secret partagé [225]. En cas de dérive (`ASI10`), retirer l’entrée d’enregistrement dans `SPIRE` interrompt le renouvellement et permet le blocage immédiat dans `Envoy` /`OPA` [225] [229].

### 10.2.4 Double lecture EA / SA

Pour l’**EA**, `SPIFFE` /`SPIRE` unifie les identités machines au-dessus des fournisseurs infonuagiques et résorbe les dix risques `OWASP NHI` [216] [218]. L’EA gouverne le découpage des *Trust Domains* (isolation hors-production et production, `NHI8`) et le nommage unique des `SPIFFE ID` (`NHI9`) [216] [218]. Pour le **SA**, le couple `SPIRE` + `Envoy SDS` élimine les secrets sur disque, sécurise le plan transport `A2A` (`ASI07`) et lie l’identité aux sélecteurs immuables du runtime [204] [225] [229].

> **Arbitrage EA / SA** — Interdire toute clé API statique et tout secret longue durée (`NHI7`) pour authentifier des agents, passerelles `MCP` ou travailleurs durables [216] [218]. L’`EA` impose la séparation des *Trust Domains* par environnement (`NHI8`) et l’unicité des `SPIFFE ID` par rôle (`NHI9`) [216] [218]. Le `SA` déploie `SPIRE` avec attestation à deux étages, privilégie `X.509-SVID` via `Envoy SDS` en `mTLS` interne et utilise des jetons liés par preuve de possession (`WIMSE` /`DPoP`) en couche 7 [225] [229] [226].

## 10.3 Autorisation dynamique : OAuth 2.0 On-Behalf-Of (RFC 8693), downscoping et Intent Gates (OPA/Cedar)

### 10.3.1 Le piège de l’héritage de privilèges et la délégation bornée

Authentifier un agent par `SPIFFE` n’indique ni pour quel utilisateur humain il agit ni quelles limites bornent sa requête [226] [219]. Sans délégation dynamique, deux anti-patrons exposent au risque `ASI03` (*Identity Privilege Abuse*) [204] :

1. **Le compte technique omnipotent** : l’agent accède aux `SoR` sous ses propres privilèges transversaux, transformant toute injection indirecte en *Confused Deputy* sur l’ensemble des comptes clients [204] [221] [216].
2. **Le relais passif de jeton (*token passthrough*)** : l’agent transmet directement le jeton `OAuth 2.0` de l’utilisateur vers les serveurs `MCP` ou API aval. Ce jeton porte des portées et audiences trop larges, exploitables par un serveur tiers compromis (`ASI04`) sans traçabilité de l’agent [204] [217]. La spécification **MCP Authorization** (révision `2025-11-25`) interdit explicitement ce *token passthrough* : chaque serveur `MCP` HTTP opère en serveur de ressources `OAuth 2.1` (`PKCE`, `RFC 9728`, `RFC 8414`) et doit valider que le jeton lui est spécifiquement destiné [217].

L’architecture cible sépare ainsi l’**usurpation** (*impersonation*) de la **délégation explicite bornée**, qui préserve l’imputabilité conjointe tout en réduisant les droits à chaque saut (*downscoping*) [219] [212].

### 10.3.2 Chaîne protocolaire IETF : `RFC 8693`, `RFC 8707`, `RFC 9449` (`DPoP`), `RFC 9396` et `Transaction Tokens`

La délégation multi-sauts sécurisée combine cinq standards complémentaires de l’IETF [219] [230] [214] [220] [212] :

1. **Échange *On-Behalf-Of* (**`RFC 8693`**) et *downscoping*** : l’agent soumet le jeton entrant (`subject_token`) et sa propre preuve attestée (`actor_token`) au *Security Token Service* (`STS`) via le type `token-exchange` [225] [219]. Le `STS` émet un jeton réduit à l’intersection des droits de l’utilisateur et de la tâche (*downscoping*), portant le sujet en `sub` et l’agent dans la revendication `act` (*Actor*), imbriquée à chaque saut pour préserver la lignée complète et encadrable par `may_act` [219].
2. **Ancrage d’audience par *Resource Indicators* (**`RFC 8707`**)** : le paramètre `resource` désigne l’URI canonique unique du serveur `MCP` ou de la passerelle cible [230] [217]. Le `STS` fige `aud` sur cette cible, empêchant le rejeu transversal d’un jeton d’un service vers un autre [230] [217].
3. **Contrainte cryptographique par** `DPoP` **(**`RFC 9449`**)** : pour neutraliser le vol de jetons en couche 7 lorsque le `mTLS` (`RFC 8705`) ne traverse pas les mandataires, `DPoP` lie le jeton d’accès à une clé privée détenue par l’agent via la confirmation `cnf.jkt` (empreinte `JWK` SHA-256) et exige une preuve signée dans l’en-tête HTTP `DPoP` à chaque requête [220].
4. **Mandats fins** `RFC 9396` **(**`RAR`**) et *Transaction Tokens*** : face aux actions risquées (`ASI02`), la norme `RFC 9396` remplace les portées plates par un objet JSON structuré `authorization_details` précisant action, ressource et plafonds quantitatifs [214]. En interne, les **Transaction Tokens** (`draft-ietf-oauth-transaction-tokens`) émis par un *Transaction Token Service* (`TTS`) propagent un jeton bref à contexte **immuable** (`Txn-Token`) sur toute la chaîne d’appels, empêchant toute dérive d’intention (*Goal Drift*) entre sous-agents [212].

La figure 10.2 synthétise ce mécanisme de délégation et d’interception.

> **[Figure]**
> - Utilisateur / SoE
> - Agent Orchestrateur
> - (SVID + clé DPoP)
> - STS / Serveur OAuth (RFC 8693, 8707, 9396)
> - MCP Gateway (PEP) & Intent Gate (PDP)
> - System of Record
> - (API / SoR cible)
> - Utilisateur / SoE Agent Orchestrateur
> - (SVID + clé DPoP)
> - STS / Serveur OAuth (RFC 8693, 8707, 9396)
> - MCP Gateway (PEP) & Intent Gate (PDP)
> - System of Record
> - (API / SoR cible)
> - 1. Requête initiale et échange On-Behalf-Of (downscoping)
> - 1 Requête avec jeton OAuth (portée initiale large)
> - 2
> - Token Exchange (RFC 8693) subject_token + actor_token (SVID) + resource (RFC 8707) + DPoP (RFC 9449) + authorization_details (RFC 9396)
> - 3 Jeton OBO lié DPoP + Txn-Token (sub: user, act: agent, aud: mcp-gw, portée réduite et plafond RAR)
> - 2. Contrôle déterministe par Intent Gate (OPA / Cedar)
> - 4 POST /mcp tools/call (Authorization: DPoP + preuve HTTP, outil et paramètres conformes)
> - 5 Vérifie signature JWT, audience RFC 8707, preuve DPoP et chaîne act[]
> - 6 Évalue politique OPA/Cedar (PDP) : Principal, Action, Resource, Context
> - 7 Exécution bornée et idempotente (Txn-Token propagé en audit)
> - 8 200 OK (confirmation)
> - 9 Réponse MCP filtrée
> - 3. Rejet déterministe d'une dérive par injection indirecte (ASI01/ASI03)
> - 10 tools/call injecté (outil exclu ou paramètre hors plafond)
> - 1 1 Intent Gate (forbid / deny) : portée ou contrainte RFC 9396 violée
> - 12 403 Forbidden / Escalade HITL + Alerte AIDR (aucun appel SoR)

*Fig. 38. – Séquence d’autorisation dynamique : échange OAuth 2.0 OBO (RFC 8693 + RFC 8707 + DPoP), downscoping multi-sauts et évaluation par Intent Gate*

### 10.3.3 *Intent Gates* déterministes : *Policy-as-Code* avec `OPA/Rego` et `Cedar`

Même muni d’un jeton OBO lié par `DPoP`, un agent victime d’une injection ou d’une hallucination peut déclencher une opération abusive dans son périmètre nominal [204] [231]. L’**Intent Gate** interpose un contrôle déterministe *Policy-as-Code* hors du `LLM`, devant la `MCP Gateway` (chapitre 04) et les passerelles `A2A` (chapitre 05) [221] [231]. Selon `NIST SP 800-207`, la passerelle agit en *Policy Enforcement Point* (`PEP`) interrogeant un *Policy Decision Point* (`PDP`) qui rend un verdict `allow`, `deny` ou `escalate_hitl` [207] [227] [231]. Le tableau 10.2 compare les deux moteurs dominants :

- `OPA` **/** `Rego` (`CNCF`) : moteur généraliste inspiré de Datalog évaluant des règles sur documents JSON (`input` et `data` en mémoire) [227]. Intégré à `Envoy` et `SPIRE`, il exprime des règles contextuelles riches — profondeur `act[]`, fenêtres horaires, seuils d’escalade `HITL` (`ASI09`) — en imposant explicitement `default allow := false` car une règle non satisfaite vaut *indéfini* [229] [227].
- `Cedar` (notamment dans `Amazon Bedrock AgentCore Policy`) : langage typé structuré autour de `Principal`, `Action`, `Resource` et `Context`, séparant strictement les politiques du code applicatif [215] [231]. Il combine refus par défaut, modèle `permit` /`forbid`, validation contre le schéma d’outils et vérification par raisonnement automatisé (*automated reasoning*) pour repérer avant déploiement toute règle trop permissive ou contradictoire [215] [231].

| Critère architectural | `OPA` / `Rego` (CNCF) | `Cedar` (ex. `AgentCore Policy`) | Arbitrage de sélection |
| --- | --- | --- | --- |
| Modèle d’évaluation | Datalog généraliste sur JSON (`input` /`data`) [227] | Typé par schéma (`Principal`, `Action`, `Resource`, `Context`) [215] [231] | `OPA` pour infra transversale ; `Cedar` pour autorisation fine d’outils |
| Défaut de sécurité | Indéfini ; exige `default allow := false` [227] | Refus par défaut et modèle `permit` /`forbid` [215] [231] | `Cedar` limite les erreurs d’omission sur les garde-fous critiques |
| Validation en amont | Tests unitaires `Rego` [227] | Validation schéma + raisonnement automatisé [215] [231] | `Cedar` lorsqu’une analyse formelle de permissivité est requise |
| Logique contextuelle | Très riche (chaîne `act[]`, temps, données externes) [227] | Structurée autour d’entités et d’attributs typés [215] | `OPA` pour croiser quotas, graphe de délégation et contexte multi-sauts |
| Intégration plateforme | `Kubernetes`, `Envoy SDS + SPIRE`, passerelles `MCP` [229] [227] | Moteur embarquable, `AgentCore Gateway` [215] [231] | Selon l’ancrage Kubernetes ou géré de la plateforme (ch. 13) |

*Tableau 10.2 — Comparaison architecturale des moteurs d’Intent Gate : OPA/Rego contre Cedar.*

### 10.3.4 Double lecture EA / SA

Pour l’**EA**, la délégation bornée élimine les comptes techniques permanents sur les `SoR`, rattache chaque mutation à l’initiateur humain et à la lignée `act[]`, et déplace les plafonds métier impératifs des prompts vers un patrimoine *Policy-as-Code* auditable [221] [219] [227] [215]. Pour le **SA**, le verrouillage repose sur l’interdiction du *token passthrough* [217], le couplage `RFC 8693` + `RFC 8707` + `DPoP` (`RFC 9449`) [219] [230] [220], la propagation immuable par `Txn-Token` [212] et l’interception synchrone par `OPA` /`Cedar` avec escalade `HITL` sur seuils `RFC 9396` [214] [231].

> **Arbitrage EA / SA** — Interdire tout compte de service omnipotent et tout relais passif de jeton (*token passthrough*) dans les chaînes multi-agents et serveurs `MCP` [216] [217]. L’`EA` impose la traçabilité `(sub, act[])`, le *downscoping* par tâche et le versionnement des règles impératives dans des `Intent Gates` déterministes [219] [227] [215]. Le `SA` assemble `OAuth 2.0 OBO` (`RFC 8693`), `RFC 8707`, `DPoP` (`RFC 9449`), `Transaction Tokens` contre le *Goal Drift*, et `OPA` /`Cedar` devant la `MCP Gateway` avec escalade `HITL` sur les bornes `RFC 9396` [214] [220] [212] [231].

## 10.4 Confinement d’exécution (microVM, gVisor, WASM), protection PII et postures AISPM/AIDR

### 10.4.1 Confinement système des outils à risque et du code généré (`ASI05`)

Le chapitre 03 a posé l’usage de `SHADI` et de `Agent Sandbox` / `SandboxWarmPool` face aux conteneurs `runc` nus. Il reste à examiner la mécanique de sécurité de ces technologies devant l’exécution de code arbitraire (`ASI05`) et la cohabitation multi-locataires [204] [218]. Un conteneur Linux ordinaire repose sur des espaces de noms, `cgroups` et filtres `seccomp` partageant un même noyau hôte écrit en C [223] : une faille dans l’API d’appels système permet l’évasion vers l’hôte et le vol des `SVID` voisins [218] [223]. Trois régimes durcis répondent à ces contraintes, comparés au tableau 10.3 et arbitrés à la figure 10.3 :

1. **MicroVM matérielles (**`Firecracker` **et** `Kata Containers`**)** : `Firecracker` isole chaque charge sous l’hyperviseur Linux `KVM` avec un noyau invité minimal et des périphériques virtio restreints (`Net`, `Block`, `Vsock` avec limitation de débit I/O) [222]. Le processus `VMM` est confiné en production par `jailer` via `chroot`, `cgroups`, espaces de noms PID/réseau et abandon de privilèges `UID` /`GID` [222]. Avec un noyau minimal et 128 Mio de RAM, un hôte de 36 cœurs crée jusqu’à 5 microVM par cœur et par seconde (180/s) [222]. Pour préserver la compatibilité avec les images `OCI` et l’interface `CRI` Kubernetes, **Kata Containers** exécute les conteneurs dans des microVM à noyau dédié via `Firecracker`, `Cloud-Hypervisor` ou `QEMU` [232].
2. **Noyau applicatif en espace utilisateur (**`gVisor`**)** : `gVisor` (`runsc`) interpose le noyau applicatif `Sentry`, écrit en `Go` (mémoire sûre), qui intercepte et traite en espace utilisateur la majorité des appels système Linux du conteneur [223]. Les accès fichiers passent par un mandataire cloisonné distinct, `Gofer`, via `LISAFS` (ou `Directfs`) [223]. Cette couche réduit drastiquement la surface exposée au noyau hôte C sans exiger `KVM`, au prix d’un surcoût sur les charges intensives en I/O ou appels système [223].
3. **Isolation par capacités et mémoire linéaire (**`Wasmtime` **et** `Component Model`**)** : pour les extensions de passerelle, validateurs ou scripts *Code Mode* (chapitre 04) compilables en WebAssembly, `Wasmtime` procure une isolation logicielle stricte [224]. La pile d’appels demeure inaccessible au code invité, les
  pointeurs sont vérifiés en bornes dans une mémoire linéaire dotée par défaut d’une **zone de garde de 2 Go**, les sauts de contrôle sont typés et aucun appel système brut n’est exposé (*zero ambient authority*) [224]. Grâce au **Component Model** et aux interfaces `WIT` **/**`WASI`, l’hôte n’accorde que des capacités explicitement liées (répertoires pré-ouverts, requêtes HTTP ciblées) [224].

| Régime d’isolation | Frontière de sécurité | Composants clés | Compatibilité | Compromis performance | Usage agentique cible |
| --- | --- | --- | --- | --- | --- |
| `runc` durci | Noyau hôte partagé (`namespaces` /`seccomp`) | `containerd`, `AppArmor` | Totale (OCI Linux) | Surcoût minimal | Outils internes déterministes sans code généré |
| `gVisor` **(**`runsc`**)** | Noyau applicatif `Go` en espace utilisateur [223] | `Sentry` + `Gofer` (`LISAFS`) [223] | Élevée (OCI standard, sans KVM) [223] | Surcoût sur I/O et syscalls intensifs [223] | Interpréteurs Python/Node et `MCP` multi-locataires sans KVM |
| `Firecracker` **/** `Kata` | Hyperviseur `KVM` + noyau invité dédié [222] [232] | `VMM` + `jailer` ; `Kata CRI` [222] [232] | Totale (binaires ou OCI via Kata) [232] | Jusqu’à 5 microVM/cœur/s (128 Mio RAM) [222] | Code arbitraire (`ASI05`), navigation isolée, charges critiques |
| `Wasmtime` **/** `WASI` | Mémoire linéaire bornée + capacités `WIT` [224] | Garde 2 Go, `Component Model` [224] | Code compilable `.wasm` (Rust, Go, JS) [224] | Très haute densité, démarrage rapide | Scripts `Code Mode`, filtres en ligne, greffons `MCP` |

*Tableau 10.3 — Matrice comparative d’architecture et de sécurité des régimes de confinement d’exécution agentique.*

> **[Figure]**
> - Outil ou code invoqué par l'agent après passage Intent Gate (OPA / Cedar)
> - Exécution de code arbitraire, binaire natif ou multi-locataires hostile ?
> - oui non — appel d'API métier déterministe
> - Charge compatible OCI standard sans réécriture en Wasm ?
> - oui non — greffon / parseur compilable
> - Exigence d'isolation matérielle (KVM et noyau invité dédié) ?
> - oui non — pas de KVM ou forte densité
> - Firecracker / Kata Containers MicroVM + Jailer (chroot, cgroups) Jusqu'à 5 microVM/cœur/s (128 Mio RAM)
> - gVisor (runsc) Noyau Sentry en Go + proxy Gofer Surface noyau hôte réduite sans VM
> - Wasmtime / Component Model (WASI) Mémoire linéaire bornée (garde 2 Go) Zero ambient authority (interfaces WIT)
> - Conteneur durci + Proxy Egress Non-root, seccomp, FS lecture seule Blocage réseaux privés / métadonnées (anti-SSRF)
> - Appliquer filtrage PII (Presidio / NeMo) et remonter traces vers AIDR

*Fig. 39. – Arbre de décision architectural pour la sélection du confinement d’exécution (Wasmtime, gVisor, Firecracker/Kata) et du niveau d’Intent Gate*

### 10.4.2 Filtrage réseau sortant et protection `PII` au fil de l’eau

L’isolation de calcul doit être doublée d’un mandataire réseau sortant (*egress proxy*) à refus par défaut, bloquant les requêtes vers les réseaux internes, les points de métadonnées d’infrastructure et les domaines externes non homologués contre les attaques **SSRF** et l’exfiltration [221] [205]. En parallèle, le transit des données sensibles dans les invites, retours `MCP` et journaux impose un filtrage des données personnelles (`PII`) en ligne [221] [233] [234] :

1. **Détection et dé-identification configurable (**`Presidio`**)** : le cadriciel ouvert **Presidio** (*Data Privacy Stack*) associe reconnaissance d’entités nommées (`NER`), expressions régulières, sommes de contrôle et contexte multilingue pour localiser puis anonymiser, masquer, hacher ou chiffrer par opérateurs configurables les entités `PII` avant inférence, appel d’outil ou journalisation [233].
2. **Garde-fous synchrones (**`NeMo Guardrails` **et** `API Intercept`**)** : **NVIDIA NeMo Guardrails** orchestre de manière programmable des contrôles sur les entrées, sorties, passages `RAG` et appels d’outils en s’appuyant notamment sur `Presidio` pour bloquer ou caviarder les fuites avant transmission au modèle [234]. À la passerelle, des interfaces telles que **Prisma AIRS API Intercept** inspectent synchronement requêtes, réponses et flux `MCP` selon des profils déclarés pour masquer les données sensibles, bloquer les URL malveillantes et contrer injections ou attaques sur bases de données [235].

### 10.4.3 Boucle continue `AISPM` et `AIDR` : inventaire, posture et réponse en temps réel

Pour pallier le *Shadow AI* et les attaques graduelles réparties sur plusieurs tours, l’architecture Zero-Trust relie deux boucles continues [236] [213] [235], représentées à la figure 10.4 :

- **L’AISPM (*AI Security Posture Management*)** assure l’inventaire et la prévention continue : découverte des agents, modèles, assistants `SaaS`, bases vectorielles et serveurs `MCP` pour maintenir une nomenclature `AI-BOM`, détection des `NHI` sur-privilégiées (`NHI5`), des secrets exposés (`NHI2`) et des dérives de configuration face aux référentiels **OWASP AI Exchange** et **ASI01–ASI10** avant exécution [204] [236] [213].
- **L’AIDR (*AI Detection and Response*)** surveille l’exécution en temps réel : elle corrèle l’ensemble de la trajectoire — invites, contextes récupérés, appels `MCP`, accès mémoire, échanges `A2A`, `SPIFFE ID` et lignée `act[]` — afin d’identifier une dérive comportementale ou une exfiltration multi-étapes (`ASI01` /`ASI08` /`ASI10`) [213] [235]. En cas d’incident, l’`AIDR` déclenche une réponse automatisée : blocage à l’`Intent Gate`, suspension du workflow, suppression de l’enregistrement `SPIRE` bloquant le renouvellement du `SVID` et mise en quarantaine du bac à sable [225] [213] [235].

Cette télémétrie sécuritaire alimente directement la pile `OpenTelemetry GenAI` et les coupe-circuits `SRE` décrits au chapitre 11 [221] [213].

> **[Figure]**
> - Plan de gouvernance et
> - d'identité
> - [system]
> - Plan d'exécution Zero-Trust (Data Plane)
> - [system]
> - Confinement, cibles et
> - détection runtime
> - [system]
> - «container» AISPM & AI-BOM
> - [Posture continue]
> - Inventaire Shadow AI, audit NHI et serveurs MCP
> - «container» SPIRE Server & STS
> - [Identité & Jetons]
> - Attestation SPIFFE, OAuth OBO et Txn-Tokens
> - «container» Agent Harness (CaMeL)
> - [Flots séparés]
> - Séparation contrôle/données
> - et étiquettes provenance
> - «container» MCP Gateway & Intent
> - Gate [OPA Rego / Cedar (PEP/PDP)]
> - Validation DPoP/RFC 8707,
> - politiques et anti-SSRF
> - «container» AI Gateway & Filtre PII
> - [Presidio / NeMo / AIRS]
> - Masquage PII en ligne,
> - blocage injections
> - «container» Confinement d'exécution
> - [Firecracker / gVisor / Wasm]
> - Isolation noyau/capacités pour code et outils risqués
> - «external_system» Systems of Record &
> - Outils
> - ERP, CRM, dépôts internes
> - «external_system» Modèles d'inférence
> - LLM cloud ou souverain
> - «container» Plateforme AIDR
> - [Détection & Réponse]
> - Corrélation trajectoires, coupe-circuit et révocation
> - Durcit posture
> - et catalogue
> - Délivre SVID et jetons OBO
> - Requêtes outils
> - signées DPoP
> - Appels modèles
> - sous contrôle
> - Délègue code et outils risqués
> - Appels bornés et idempotents
> - Inférence sans PII (données masquées)
> - Télémétrie décisions
> - Alertes PII/injections
> - Révoque SVID sur dérive ASI10

*Fig. 40. – Architecture Zero-Trust de défense en profondeur d’un domaine agentique : AISPM pré-déploiement, AI Gateway PII, Agent Harness CaMeL, Intent Gate, confinement et AIDR*

En pratique, cette boucle fermée unifie les contrôles préventifs recensés par l’`OWASP AI Exchange` — contrôle des données entrantes, limitation des comportements indésirables et durcissement d’infrastructure — avec la réponse active sur les trajectoires [236] [213]. Au lieu de traiter la sécurité des agents comme un pare-feu périmétrique isolé, la combinaison `AISPM` + `AIDR` relie en permanence l’inventaire des identités machines, les politiques déterministes et les journaux d’exécution [213] [235].

### 10.4.4 Double lecture EA / SA

Pour l’**EA**, le couple `AISPM` /`AIDR` et le masquage `PII` matérialisent la maîtrise du risque : le portefeuille maintient un `AI-BOM` vérifié, borne l’exposition des données personnelles aux modèles tiers et garantit un arrêt ciblé des agents déviants (`ASI10`) [204] [233] [213]. L’EA arbitre aussi le compromis économique entre microVM `Firecracker` /`Kata` pour le code non fiable et haute densité `Wasmtime` /`gVisor` [222] [223] [224] [232]. Pour le **SA**, la défense en profondeur interdit `runc` nu sur les exécutions de code, verrouille l’egress anti-`SSRF`, applique `Presidio` /`NeMo` avant sortie vers modèles ou journaux et connecte l’`AIDR` à la révocation `SPIRE` /`OAuth` [225] [223] [233] [234] [213] [235].

> **Arbitrage EA / SA** — Imposer une défense en profondeur unissant confinement adapté au risque, filtrage `PII` /egress en ligne et boucle continue `AISPM` /`AIDR` [222] [233] [213]. L’`EA` proscrit tout agent absent de l’`AI-BOM` de l’`AISPM`, exige le masquage ou chiffrement `PII` avant appel vers un modèle tiers externe, et impose un arrêt d’urgence ciblé contre `ASI10` [233] [213]. Le `SA` bannit `runc` nu pour l’exécution de code (`ASI05`) au profit de `Firecracker` /`Kata`, `gVisor` ou `Wasmtime` /`WASI`, verrouille les sorties réseau anti-`SSRF` et raccorde l’`AIDR` à la révocation des identités `SPIFFE` /`OBO` [225] [222] [223] [224] [213].

## Synthèse et transition

La sécurité d’une entreprise agentique ne repose ni sur un périmètre réseau statique ni sur la discipline sémantique des modèles de langage. En combinant la modélisation `OWASP ASI01–ASI10` et la séparation contrôle/données (`CaMeL`) avec des identités attestées sans secret statique (`SPIFFE` /`SPIRE`), une délégation `OAuth 2.0 OBO` bornée (`RFC 8693`, `RFC 8707`, `DPoP`, `RFC 9396`, `Txn-Tokens`), des `Intent Gates` déterministes (`OPA` /`Cedar`), le confinement système (`Firecracker`, `gVisor`, `Wasmtime`), le filtrage `PII` et la boucle `AISPM` /`AIDR`, l’architecture Zero-Trust maîtrise techniquement le rayon d’impact cognitif.

Chaque requête génère désormais des preuves cryptographiques corrélées (`SPIFFE ID`, `act[]`, `Txn-Token`) et des décisions de politiques exploitables. Le **chapitre 11** expose comment instrumenter ces trajectoires dans `OpenTelemetry GenAI`, automatiser la validation `EvalOps` et piloter les coupe-circuits `SRE`, avant que le **chapitre 12** n’inscrive ces garanties techniques dans les cadres réglementaires et économiques `FinOps`.
