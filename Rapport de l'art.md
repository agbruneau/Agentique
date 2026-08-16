# Rapport de l'art — interopérabilité, orchestration et coordination agentiques

**État détaillé du champ, établi sur le seul contenu du dépôt *Agentique*.**
Auteur des travaux sources : André-Guy Bruneau, M.Sc. IT. Rapport dérivé, arrêté au 16 août 2026.

---

## Avertissement de régime — à lire avant tout le reste

Ce document **n'est pas un huitième livrable**. Il est un **rapport dérivé** : il ne rouvre aucun
des sept livrables, ne verse aucun fait neuf, n'ouvre aucune source primaire et ne franchit aucune
porte. Sa seule matière est ce que le dépôt porte déjà.

Trois conséquences, et elles bornent tout ce qui suit.

1. **Aucun énoncé de ce rapport n'a de provenance propre.** Chaque fait vient d'un livrable nommé,
   et hérite du régime de preuve de ce livrable — jamais d'un meilleur. Un chiffre que la veille
   donne pour auto-déclaré reste auto-déclaré ici ; un résultat que la revue de littérature range en
   prépublication non arbitrée y reste.
2. **Les gels ne coïncident pas.** La veille technologique gèle ses faits au **15 août 2026**, la
   revue de littérature reprend ses notices au **15 août 2026**, le traité en est à sa **troisième
   édition du 15 août 2026**, le compendium est **clos au 8 août 2026** et les trois monographies
   gèlent respectivement en **juin 2026**, aux **16-17 juillet 2026** et par héritage des deux. Un
   énoncé daté d'un gel antérieur n'est pas faux : il est daté, et le rapport le dit à chaque fois
   que l'écart compte.
3. **Le dépôt est clos** (décision d'auteur D-13, 8 août 2026), et une clôture ne s'auto-verrouille
   pas. Le présent rapport **ne la rouvre pas** : il n'écrit dans aucun livrable, ne corrige aucun
   texte arrêté et ne solde aucune dette. *Synthétiser n'est ni réviser ni publier.*

Un quatrième point est de méthode et il structure le document entier. Le dépôt tient deux registres
qui ne mesurent pas la même chose : **la veille dit ce que le monde déployé fait** — spécifications,
dépôts de code, communiqués de fondation, textes réglementaires — et **la revue de littérature dit
ce que le champ savant sait, et à quel régime de preuve**. *Les deux ne se valident pas l'un
l'autre, et l'intérêt du dépôt tient précisément à ce qu'ils ne coïncident pas.* Ce rapport les
tient séparés partout où ils divergent, et le signale quand ils convergent.

---

## Table

1. [Objet, sources et grille de lecture](#1-objet-sources-et-grille-de-lecture)
2. [Le champ : définitions, taxonomies, interfaces](#2-le-champ--définitions-taxonomies-interfaces)
3. [La couche d'échange : le corpus protocolaire](#3-la-couche-déchange--le-corpus-protocolaire)
4. [Les sept couches orthogonales](#4-les-sept-couches-orthogonales)
5. [Identité, délégation, révocation](#5-identité-délégation-révocation)
6. [Sécurité : ce qui est mesuré, et l'instrument qui mesure](#6-sécurité--ce-qui-est-mesuré-et-linstrument-qui-mesure)
7. [Évaluation, bancs d'essai et observabilité](#7-évaluation-bancs-dessai-et-observabilité)
8. [Systèmes multi-agents : rendement, attribution, dépendance](#8-systèmes-multi-agents--rendement-attribution-dépendance)
9. [Chorégraphie et essaim : la frontière de la coordination](#9-chorégraphie-et-essaim--la-frontière-de-la-coordination)
10. [Droit, gouvernance et calendrier](#10-droit-gouvernance-et-calendrier)
11. [Les invariants de l'état de l'art](#11-les-invariants-de-létat-de-lart)
12. [Ce que l'état de l'art ne sait pas](#12-ce-que-létat-de-lart-ne-sait-pas)
13. [Horizon daté 2026-2032](#13-horizon-daté-2026-2032)
14. [Limites du présent rapport](#14-limites-du-présent-rapport)
15. [Carte des sources internes](#15-carte-des-sources-internes)

---

## 1. Objet, sources et grille de lecture

### 1.1 La question

Le dépôt entier répond à une question unique, posée par le corpus et reprise par tous les
livrables : **comment une entreprise — en particulier une institution financière réglementée —
peut-elle déployer, gouverner et exploiter des agents d'IA autonomes de manière sécurisée, traçable
et pérenne ?** Le traité sur les essaims la prend par l'autre bout et pose la question symétrique :
*que reste-t-il à coordonner lorsqu'on renonce à décider ?*

Ce rapport ne répond ni à l'une ni à l'autre. Il établit **ce que l'état de l'art sait, ce qu'il
croit savoir, et où il se contredit**, couche par couche.

### 1.2 Les sept livrables et ce que chacun apporte

| Livrable | Rôle | Portée | Thèse | Volumétrie |
|---|---|---|---|---|
| **Veille technologique** | État de l'art vérifié sur sources primaires, par éditions | Mondiale | « L'agent d'entreprise fiable de 2026 est un agent *enveloppé* » | 100 p., 303 réf. |
| **Revue de littérature** | Ce que la littérature académique sait, et à quel régime | Mondiale, 10 fronts | « Les trois quarts du champ n'ont franchi aucun comité » | 40 p., 176 réf. (192 entrées) |
| **Vol. I — Interopérabilité** | Cadre général, mondial et théorique | UE / É.-U. / R.-U. / Asie | « Autonomie graduée sous contrôle de finalité » | 569 p., 233 257 mots |
| **Vol. II — Orchestration** | Cas canadien réglementé, instruit au grain du droit | Canada-Québec | « Autonomie encadrée » (*framed autonomy*) | 387 p., 29 pièces |
| **Vol. III — Entreprise** | Le verrou commun : identité, maillage, exploitation | Organisation, cycle de vie | « La confiance ne se décrète pas, elle se fabrique » | 427 p., 34 pièces |
| **Compendium (Vol. IV)** | Omnibus terminal : absorbe et remplace les trois volumes | Les trois portées réunies | Les trois thèses sont trois coupes d'un même objet | 1 000 p., 50 ch., 5 livres |
| **Traité + `stigmergie-lab`** | Où passe la frontière entre coordonner par accord et par le milieu | Le régime de coordination lui-même | « Déplacer la coordination dans le milieu, et payer ce qu'il coûte » | 116 p., 8 ch., 123 notices |

Trois remarques que le lecteur doit avoir en tête.

**Le compendium est clos, non publiable, et il le restera.** Cinquante chapitres rédigés hors
portes, relus, arbitrés, audités et composés — mais **quatre portes closes par dérogation**, deux
critères de conformité non satisfaisables faute de relecteur tiers, aucune diffusion à un tiers,
aucune opposabilité. *Arrêter n'est ni terminer ni publier.*

**Le Vol. III garde quinze remontées ouvertes à titre définitif** (R-G-43 à R-G-57) et une dette de
vote sur deux faits ; l'appareil de vérification qui les détaillait — 30 rapports — a été supprimé
de l'arbre le 8 août 2026 et ne se lit plus qu'à l'historique git. *La dette survit à son
inventaire.*

**Le traité est le seul livrable dont les énoncés soient rejoués par du code — et le seul qu'une
mesure du dépôt réfute.** `stigmergie-lab` transpose ses mécanismes en simulateur déterministe Rust
(quatre crates, 428 tests) sous une contrainte : *tout chiffre affiché doit être retrouvé par la
mesure, ou l'écart doit être consigné*. Cinq écarts sont consignés ; **trois contredisent le
traité** (§9.4).

### 1.3 Les trois régimes de preuve du dépôt

Le dépôt n'a pas un régime de preuve unique, et confondre les trois est la faute que ce rapport
cherche le plus à éviter.

| Registre | Instrument | Ce qu'il atteste | Où il vaut |
|---|---|---|---|
| **Sources primaires, vérification adverse** | trois réfutateurs indépendants à consigne de *réfuter*, deux réfutations sur trois éliminant l'énoncé | l'état déployé à une date | veille, §4.6 à §4.13 (le haut) |
| **Sources primaires, contre-vérification individuelle** | un vérificateur, source primaire, sans ronde adverse | l'état déployé, garantie plus faible | veille, passes des 8 et 15 août ; §12.4 (le bas) |
| **Notice de dépôt** | champ `journal_ref` ou DOI ; le champ de commentaire ne vaut pas attestation | le régime éditorial d'une pièce, non son contenu | revue de littérature, corpus entier |

S'y ajoutent les niveaux de preuve **[A] / [B] / [C]** du socle factuel du Vol. II — vote adversarial
3-0 > source primaire extraite > repérage —, hérités par le Vol. III et par le compendium, et le tri
épistémique **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** du Vol. I, repris par la veille en section
prospective.

**Trois passes seulement de la veille soumettent tout leur lot à la ronde adverse** — 2, 7 et
13 juillet 2026 ; les trois passes de veille d'août n'en ont aucune. Les faits ne pèsent donc pas
tous le même poids à l'intérieur d'un même document, et le dépôt le déclare.

### 1.4 La physionomie du corpus académique, avant tout énoncé de contenu

Le résultat le plus lourd de la revue de littérature n'est pas un fait du champ : c'est une
propriété du corpus qu'elle a lu.

| Régime | Pièces | Part |
|---|---|---|
| Publication attestée en notice (`journal_ref` ou DOI) | 12 | 6 % |
| Acceptation auto-déclarée (champ de commentaire) | 32 | 17 % |
| Aucun signe de revue par les pairs | 145 | 77 % |
| **Total (pièces déposées sur arXiv)** | **189** | **100 %** |

Âge et stabilité vont dans le même sens : **119 pièces sur 189 — 63 % — ont été déposées dans les
huit premiers mois de 2026** ; 136 sur 189 ont été révisées pour la dernière fois en 2026 ; et
**103 sur 189 — 54 % — n'ont jamais été révisées**. Enfin, sur les 123 pièces des dix fronts neufs,
**67 — 54 % — rapportent la performance d'un artefact de leurs propres auteurs** : *ce corpus
s'auto-arbitre à moitié*.

**Deux bornes rendent ce constat utilisable plutôt que polémique**, et la revue les pose
elle-même. D'une part, mesurer la part de non-arbitré *sur un dépôt de prépublications* puis en
conclure quelque chose du champ serait circulaire. D'autre part, une passe de contrôle conduite sur
DBLP, Crossref et OpenAlex, avec la consigne inverse — chercher ce qui réfute le résultat central —,
**trouve de la littérature arbitrée hors arXiv sur les quatre fronts que le corpus donne pour
vides** (sécurité, évaluation, couche transactionnelle, chorégraphie et essaim), et **quatre pièces
du corpus classées « sans revue » sont en fait publiées** sans que leur notice le dise. Conclusion
exacte : **145 est un plafond du non-arbitré et 12 un plancher de l'arbitré** ; les trois régimes
mesurent ce que les notices déclarent, non ce que les comités ont fait.

*Ce que ce constat autorise : nommer le régime de chaque pièce citée, une à une. Ce qu'il
interdit : traiter un pourcentage du champ comme un acquis.*

---

## 2. Le champ : définitions, taxonomies, interfaces

### 2.1 Définitions de travail

**Agent** — système logiciel qui poursuit des objectifs en percevant un environnement et en
agissant sur lui avec un degré d'autonomie ; ici, un grand modèle de langue pour la planification,
le raisonnement et le dialogue, et des outils invocables pour l'action.

**Système multi-agents** — composition de plusieurs agents hétérogènes (modèle, cadriciel,
opérateur) autour de tâches communes.

**Interopérabilité agentique** — capacité d'agents développés indépendamment à interagir de façon
utile *et gouvernée* : mêmes outils et données, découverte et authentification mutuelles,
délégation et restitution, à travers les frontières de cadriciels, de fournisseurs et
d'organisations.

**Agent d'entreprise** (définition du compendium) — système non humain à qui une organisation
délègue des tâches **engageant sa responsabilité**. C'est cette clause, et non la sophistication du
modèle, qui fait entrer l'objet dans le droit.

**Essaim** (définition du traité, formelle) — une population est un essaim si et seulement si la
perception de chaque agent se factorise par un **voisinage de cardinal borné** ou par un
**intervalle borné du milieu partagé** ; si la règle de décision est **la même pour tous** à un
vecteur de paramètres près ; et si le comportement utile est une **fonctionnelle de la
configuration** qui n'est fonction d'aucun état individuel. *Un composant dont la perception prend
la configuration entière en argument n'est pas membre d'un essaim : c'est un coordonnateur, et sa
présence ramène le système dans le régime de l'accord.*

### 2.2 Les trois interfaces

La littérature distingue explicitement trois interfaces, et cette distinction commande toute la
lecture de la pile : **agent-environnement** (outils, données, applications), **agent-agent**
(collaboration et délégation), **utilisateur-agent** (interaction et supervision humaines). Les
protocoles ne sont pas concurrents sur une même interface : ils sont **spécialisés par interface**,
d'où leur lecture en pile complémentaire plutôt qu'en rivalité frontale.

### 2.3 Les taxonomies disponibles, et leur date de péremption

Quatre pièces structurent le champ, et **aucune ne se cite sans sa date**.

- **Classification bidimensionnelle** — objet du protocole (*orienté contexte* contre *inter-agents*)
  croisé au périmètre (généraliste contre spécifique à un domaine). MCP y est le représentant
  canonique des orientés contexte généralistes.
- **Classification tripartite** — par interaction, recensant dix-neuf protocoles. Deux précautions :
  dix-neuf est le décompte de *ce corpus*, non un total du domaine ; et « ACP » recouvre **trois
  propositions indépendantes** (IBM/BeeAI, AGNTCY, AgentUnion), à désambiguïser à chaque mention.
- **Comparaison quadripartite et feuille de route par phases** — MCP (outils), ACP (messagerie
  structurée), A2A (exécution collaborative), ANP (places de marché décentralisées). *Datée de mai
  2025* : **l'étape « ACP » est caduque**, l'ACP d'IBM ayant été absorbé par l'effort A2A ; la
  progression outillage → collaboration → décentralisation, elle, reste valide.
- **Vision d'infrastructure** — l'« Internet des agents » : interconnexion, découverte dynamique,
  orchestration à l'échelle, et ses défis (hétérogénéité des capacités, confiance
  inter-organisations, échelle de la découverte). Sert de cadre d'évaluation plus que de taxonomie.

**Les trois classifications se recouvrent sans se recouper, et leur datation les borne également.**
La grille retenue par la veille en tire trois niveaux, chacun porté par un protocole structurant.

| Niveau d'interopérabilité | Interface | Protocole structurant | Portée typique en entreprise |
|---|---|---|---|
| Accès aux outils et au contexte | agent-environnement | **MCP** | intégration des agents au SI (données, API, applications) |
| Collaboration entre agents | agent-agent | **A2A** | délégation de tâches entre agents de fournisseurs différents |
| Découverte en réseau ouvert | agent-agent inter-organisations | **ANP** | identification et collaboration décentralisées à l'échelle du Web |

Simplification assumée : elle laisse de côté l'interface **utilisateur-agent** et, surtout, le **mode
d'interaction** — les trois protocoles structurants sont **synchrones, requête-réponse**, et la
couche événementielle asynchrone leur échappe entièrement (§4.1).

---

## 3. La couche d'échange : le corpus protocolaire

### 3.1 Le constat central

**La couche d'échange est acquise ; rien n'y est encore une norme.** MCP, A2A et ANP structurent
l'interopérabilité agentique sous fondations à neutralité déclarée ; **aucun n'est norme *de
jure***. Des suites de conformité publiques existent — `modelcontextprotocol/conformance`, dont le
`tier-check` fonde le système de tiers des SDK ; `a2a-tck` — mais **aucune n'est opposable** :
elles sont éditées par les projets qu'elles testent, aucune instance de normalisation ne les impose,
aucune certification n'en découle. *Pour l'acheteur qui exige une attestation de tiers, cela ne
change rien.*

### 3.2 MCP — l'interface agent-outils

Interface client-serveur en JSON-RPC 2.0 liant *hôte*, *client* et *serveur*, normalisant trois
primitives serveur — **outils, ressources, invites** — sur deux transports : entrée-sortie standard
en local, HTTP à distance, ce dernier seul assorti d'un cadre d'autorisation OAuth. Le schéma
TypeScript fait foi.

**La révision `2026-07-28` est le mouvement le plus substantiel du corpus protocolaire depuis
l'ajout de l'autorisation**, et elle mérite d'être lue en détail parce qu'elle inverse plusieurs
hypothèses d'architecture.

*Ce qui disparaît* : la poignée de main `initialize`/`notifications/initialized` (version et
capacités passent dans `_meta`) ; **les sessions de niveau protocole** et l'en-tête
`Mcp-Session-Id` ; `ping` et `logging/setLevel` ; **la reprise de flux et la redélivrance** — un flux
rompu perd la requête en vol, que le client **DOIT** réémettre sous un nouvel identifiant.

*Ce qui apparaît* : `server/discover`, que les serveurs **DOIVENT** implémenter ; les **requêtes à
plusieurs allers-retours**, le serveur retournant `input_required` avec ce qui lui manque, en
remplacement des requêtes initiées par le serveur (`roots/list`, `sampling/createMessage`,
`elicitation/create`, dépréciées) ; les en-têtes `Mcp-Method` et `Mcp-Name`, **exigés** sur les POST
pour que passerelles et pare-feux routent sans analyser le corps.

*Trois lectures s'imposent.* **(a) Le motif de l'abandon de l'état est le déploiement derrière un
répartiteur de charge sans stockage partagé** : la couche commune cède à l'exploitant.
**(b) Les en-têtes de routage sont la première concession de la couche commune au plan de contrôle
d'*agent mesh*** (§4.2). **(c) La dépréciation de *Roots* et de *Sampling* retire les deux voies par
lesquelles un serveur sollicitait le système de fichiers du client et le modèle de l'hôte** — soit
deux surfaces de risque, refermées.

**Elle rompt la compatibilité**, et la parade est le fait le plus notable de la période : une
**politique de cycle de vie datée** — trois états (active, dépréciée, retirée), un registre des
dépréciations, une **fenêtre minimale de douze mois** avant retrait, deux dérogations (retrait
accéléré à **quatre-vingt-dix jours** sur risque de sécurité actif ; retrait du transport HTTP+SSE
trois mois après qu'une proposition atteint le statut *Final*). *C'est le premier engagement daté
d'un protocole de la couche commune sur sa propre évolution.*

**Et le mouvement s'inverse déjà.** La charte du groupe de travail *Agents*, publiée le 5 août 2026,
se donne pour livrable principal de stabiliser l'extension *Tasks* **et de la promouvoir dans le
protocole de base** — mouvement inverse de celui que la révision venait d'opérer huit jours plus
tôt. Au 15 août 2026, le journal des changements du brouillon est **vide** : ce qui concerne la
couche d'échange est *programmé*, non acquis.

### 3.3 A2A — la délégation de tâches entre agents hétérogènes

Mécanisme central : l'**Agent Card**, descripteur JSON publié à une URI bien connue déclarant
identité, compétences, schémas d'authentification et points d'accès. Standards de base : HTTP(S),
JSON-RPC 2.0, *Server-Sent Events*, OAuth 2.0 parmi les schémas d'authentification, plus liaisons
gRPC et REST. **La v1.0.0 (12 mars 2026)** élève `a2a.proto` en **source normative unique** dont
dérivent les trois liaisons avec garanties d'équivalence, ajoute `tasks/list`, modernise OAuth 2.0
et normalise la **vérification** des signatures d'Agent Cards par JWS et canonicalisation JSON.

**Trois précisions bornent le « conçu pour l'entreprise ».** Le « pair-à-pair » vaut au niveau du
modèle, non du transport, qui reste client-serveur sur HTTP, un orchestrateur central s'intercalant
souvent. OAuth 2.0 est *pris en charge*, non exigé ; l'authentification mutuelle n'est pas imposée.
Et la sécurité désigne ce que le protocole **permet**, non ce qu'il **apporte**.

**Fait de tempo, et c'est le fait structurant de la période** : au 15 août 2026, **aucune
publication postérieure au correctif v1.0.1 du 28 mai 2026**, aucune étiquette au-delà, et l'activité
du dépôt dans la fenêtre du 8 au 15 août est **entièrement documentaire** — sept commits, six
demandes de tirage, **aucune ne touchant `specification.md` ni `a2a.proto`**. Le canal de sécurité
est ouvert et vide.

**Les deux protocoles complémentaires vivent sur des horloges de gouvernance divergentes.** Ce n'est
pas un classement — A2A a atteint sa version majeure quatre mois et demi avant la révision de MCP —,
mais leur complémentarité **ne s'accompagne d'aucune coordination des calendriers** : *l'intégrateur
qui consomme les deux porte seul le risque de leurs révisions indépendantes.*

### 3.4 ANP — la découverte décentralisée

Trois couches : identité fondée sur les **identifiants décentralisés (DID) du W3C** ;
**méta-protocole** par lequel deux agents négocient le protocole applicatif de leur échange ; couche
applicative décrivant capacités et interactions en **graphes JSON-LD**. Découverte par documents
sous URI bien connue, communication chiffrée de bout en bout.

Deux précisions de statut : `did:wba`, sa méthode d'identité, est **communautaire**, conforme à la
Recommandation W3C *DID Core* sans en être une ; son ancrage au W3C passe par un **groupe
d'incubation**, non par la filière de normalisation. **ANP reste le seul des trois dont l'identité
est décentralisée par construction** — avantage défensif relatif que montre la modélisation
comparative des menaces. Le groupe communautaire W3C n'a rien publié depuis le 19 août 2025 et le
livre blanc reste en version unique.

### 3.5 Consolidation et protocoles secondaires

**La consolidation la plus nette est plus ancienne et plus complète que les éditions antérieures ne
le disaient** : l'ACP d'IBM (projet BeeAI) est **archivé et déprécié depuis le 25 août 2025**, son
dernier commit étant l'annonce du passage à A2A. L'étape « ACP » des feuilles de route de 2025 est
donc caduque depuis presque un an.

**AGNTCY**, à la même fondation, se positionne en **infrastructure transversale** (découverte,
annuaire, messagerie) plutôt qu'en concurrent frontal — et c'est **le composant le plus actif du
corpus protocolaire** sur la fenêtre d'août : annuaire `dir` de la v1.5.0 à la v1.6.3, messagerie
SLIM en v2.2.0 puis v2.3.0, schéma OASF en v1.1.0. *Le composant le plus actif n'est pas un
protocole d'agents, mais l'infrastructure qui les indexe et les achemine.*

### 3.6 Lecture comparative

| | **MCP** | **A2A** | **ANP** |
|---|---|---|---|
| Interface | agent-environnement | agent-agent (délégation) | agent-agent inter-organisations |
| Gouvernance | Anthropic / projet ouvert (AAIF, Linux Foundation) | Google → Linux Foundation | communauté ANP / incubation W3C |
| Format et transport | JSON-RPC 2.0 ; stdio, HTTP | JSON-RPC 2.0, gRPC, REST, SSE (`a2a.proto` normatif) | méta-protocole ; JSON-LD |
| Identité | OAuth (transport HTTP) | schémas déclarés par Agent Card | DID W3C (`did:wba`), chiffrement bout en bout |
| Découverte | registres de serveurs | Agent Card sous URI bien connue | documents `.well-known`, graphes JSON-LD |
| Conformité | suite publique `tier-check` | `a2a-tck` | aucune |
| Norme *de jure* | **non** | **non** | **non** |

**Trois conclusions.** *La complémentarité l'emporte sur la concurrence* — les trois sont décrits, y
compris par leurs promoteurs, comme les étages d'une même pile. *Le gradient de maturité suit la
proximité du système d'information* — écosystème le plus massif pour MCP, gouvernance la plus
institutionnalisée pour A2A, incubation pour ANP. *La conformité existe et n'est pas opposable.*

### 3.7 Ce que la littérature mesure sur cette couche — et qui n'est pas ce qu'elle croyait

Ici, veille et revue de littérature cessent de dire la même chose, et l'écart est instructif.

**La sous-spécification de la couche sémantique est passée de « défi ouvert » à résultat mesuré, par
quatre chemins indépendants.**

| Voie | Mesure | Effectif |
|---|---|---|
| Empirique — qualité des descriptions | **97,1 %** des descriptions d'outils portent au moins un défaut, **56 %** n'énoncent pas clairement leur objet ; les enrichir ne gagne que **+5,85 points médians**, allonge l'exécution de **67,46 %** et **régresse dans 16,67 % des cas** | 856 outils, 103 serveurs |
| Empirique — cohérence description/code | **9,93 %** de paires incohérentes, sans qu'aucun mécanisme du protocole ne vérifie que la description reflète l'implémentation | 19 200 paires, 2 214 serveurs |
| Formelle | MCP et *Schema-Guided Dialogue* bisimilaires sous une application **dont l'inverse est partielle et à perte** — les manques d'expressivité sont **démontrés**, non conjecturés | — |
| Analytique | sur 18 protocoles : transport, schéma et cycle de vie **mûrs** ; clarification, alignement de contexte et vérification **hors protocole** | 18 protocoles |

**L'écosystème déployé ne se conforme pas aux hypothèses de la littérature de protocole.** Seules
**37,2 %** de 1 723 applications consommatrices imposent une approbation bloquante avant exécution
d'outil — le protocole ne spécifiant pas le côté client. Le registre officiel n'est pas stable :
sur 88,6 jours, **8,6 %** des serveurs réécrivent une description, la moitié des changements
atterrissant sur des arrivants qu'un classement par dérive ne peut atteindre.

**Le côté client ne consomme même pas ce que le serveur lui remet.** Sur 54 000 essais et
24 modèles interrogeant un serveur MCP juridique en production, retirer l'outil de recherche
concurrent porte à **98 %** au moins la lecture des données embarquées chez **23 modèles sur 24** ;
la seule présence de cet outil la fait retomber sous **15 %** chez neuf d'entre eux. *L'échec relève
donc de la préférence comportementale et non d'une incapacité*, et aucune ingénierie d'invite par
serveur n'y remédie de façon portable.

**Enfin, le coût même de MCP n'est pas mesurable comme on le croyait.** Les estimations publiées de
l'écart entre appel d'outil par MCP et par ligne de commande divergent de plus d'un ordre de
grandeur et reposent sur des rapports irreproductibles. La première mesure contrôlée à les départager
conclut que **la comparaison elle-même ne tient pas** : treize rapports strictement appariés
s'étalent de **0,43× à 29×**. **L'effet dominant est l'échafaudage, non l'interface** — deux des
sept échafaudages n'offrent aucun support MCP, achèvent pourtant chaque exécution en ligne de
commande seule, et reviennent de **5,0 à 28 fois moins cher** que les cinq qui en offrent. *Une
comparaison qui ne vérifie pas le comportement effectif mesure un mélange inconnu.*

**Ce que ce front ne traite pas.** Aucune publication ne rapporte un taux mesuré d'échec, de latence
ou de perte sémantique pour une tâche **traversant deux protocoles distincts** dans un système
déployé, sur corpus reproductible. Toutes les mesures d'écosystème portent sur **MCP seul** ; la
seule comparaison implémentée entre deux protocoles est un scénario unique dont les auteurs récusent
la généralisation ; les 30 propriétés temporelles qui unifient MCP et A2A ne sont vérifiées nulle
part.

---

## 4. Les sept couches orthogonales

Le fait le plus structurant de tout le dépôt tient en une phrase : **ce que la pile ne dit pas se
comble ailleurs — par périmètres.** Chaque fonction que la couche commune n'exprime pas est
réimplémentée à côté d'elle, et **chaque brique réintroduit le périmètre que les protocoles
promettaient de supprimer**. Le déficit d'interopérabilité ouverte **se déplace sans se résorber**.

Sept couches sont identifiées, et **une huitième — l'orchestration des agents eux-mêmes — n'a aucun
porteur candidat** (§4.8).

### 4.1 La couche événementielle : enveloppe et tissu

Les trois protocoles structurants sont synchrones ; l'événementiel asynchrone leur échappe.
**Deux briques mûres le couvrent, d'infrastructure et non d'agents ; aucun protocole d'agents ne les
a adoptées.**

**CloudEvents** — enveloppe de métadonnées indépendante du transport, quatre attributs requis
(`id`, `source`, `specversion`, `type`), faisant traverser au même événement HTTP, Kafka, AMQP, MQTT
ou NATS sans réécriture. Cœur figé en **1.0.2 depuis février 2022**, projet **gradué** de la CNCF
depuis le 25 janvier 2024. **L'*event mesh*** — réseau de courtiers d'événements interconnectés —
en est le tissu ; sa mise en œuvre ouverte principale est **projet de haut niveau** de la fondation
Apache depuis mars 2023.

*Leur maturité tranche avec celle du corpus agentique*, et pourtant le rapprochement reste
documenté, non normalisé. Le seul projet de fondation qui code ce rapprochement **vient d'en reculer
la ligne de stabilité** : registre d'Agent Cards A2A et passerelle A2A, fusionnés dans la branche
stable en mai et juin 2026, en ont été **retirés le 13 août 2026** au profit d'une branche de
développement. Ce n'est *ni un abandon ni un désaveu* — le greffon protocolaire et les
démonstrateurs restent — mais **la brique la plus mûre de la couche asynchrone tient le pont vers
A2A en développement, non en production**.

L'enveloppe demeure le meilleur **substrat candidat** : son extension de traçage distribué
(`traceparent` / `tracestate`, W3C Trace Context) porte la traçabilité que les protocoles d'agents
n'expriment pas.

### 4.2 L'*agent mesh* : le plan de contrôle

Notion émergée en 2025-2026, l'*agent mesh* **nomme et localise la couche de confiance désignée
ailleurs en creux** — sécurité, identité, registres, gouvernance —, déplaçant ces exigences **du
protocole, où elles sont insolubles, vers l'infrastructure**. Calqué sur le maillage de services, il
extrait des agents la découverte (devenue sémantique, adossée à un registre de capacités), le
routage, l'identité, les politiques et l'observabilité, **au bord, sans modifier agents ni serveurs
d'outils**.

**Le prix est explicite : il réintroduit un point de contrôle et répond au déficit de gouvernance en
*bornant* l'interopérabilité**, là où ANP la voulait ouverte et sans permission.

Trois instances sous gouvernance ouverte : une passerelle appliquant centralement ces fonctions au
trafic MCP et A2A (versée à l'*Agentic AI Foundation*, Linux Foundation) ; un exécutif d'agents
natif de Kubernetes (bac à sable CNCF) ; un registre contribué à la CNCF en mars 2026. Plus AGNTCY,
dont l'annuaire, la messagerie, l'identité et l'observabilité **sont** ces fonctions. *La couche peut
mûrir vite sans que la frontière ouverte multi-latérale cesse d'être vide.*

### 4.3 La couche transactionnelle : autoriser, commander, régler

Aucun des trois protocoles structurants ne couvre le paiement. Depuis septembre 2025, des protocoles
de paiement et de commerce agentiques le comblent **en trois sous-couches**.

| | **AP2** | **x402** | **MPP** | **ACP** | **UCP** |
|---|---|---|---|---|---|
| Sous-couche | autorisation | règlement (402) | règlement (402) | *checkout* | *checkout* |
| Créateur | Google, sept. 2025 | Coinbase, déc. 2025 | Stripe + Tempo, mars 2026 | OpenAI + Stripe, sept. 2025 | Google + Shopify, janv. 2026 |
| Gouvernance | **FIDO Alliance** | **x402 Foundation** (LF), 40 membres | aucune fondation | OpenAI + Stripe | Google + Shopify |
| Mécanisme | mandats signés (SD-JWT) | 402 ; *facilitator* | 402 ; jeton partagé ou dépôt | *Shared Payment Token* | capacités versionnées |
| Version | v0.2 (28 avril 2026) | V2, sans statut | sans numéro | `2026-04-17`, *beta* | `v2026-04-08` |
| Dépôt au 15 août 2026 | **immobile** (29 avril) | **actif** (14 août) | **actif** (7 août) | **immobile** (18 juillet) | **actif** (14 août) |

**Le mécanisme d'AP2 est le mandat** — contrat signé valant preuve de l'instruction de l'utilisateur.
L'ancrage tient à l'*utilisateur* : présent, il signe via une surface de confiance non agentique ;
absent, l'agent signe de sa clé, adossée à un mandat ouvert déjà approuvé. **AP2 n'accorde à l'agent
aucune autorité propre** — exact négatif du chantier d'identité (§5).

**Quatre lectures transversales, et elles sont dures.**

1. **Complémentarité verticale, rivalité horizontale — sur les deux sous-couches désormais.** Les
   protocoles s'emboîtent, mais le *checkout* oppose deux blocs **qui ne se citent pas**, et le
   règlement en oppose deux dont l'un se déclare rétrocompatible avec l'autre. Les mêmes acteurs
   financiers figurent sur *tous* : **la consolidation se joue sur l'infrastructure de paiement, non
   sur les protocoles**.
2. **Le fossé de l'identité est contourné, non comblé.** Ancrer le mandat dans l'identité de
   l'*utilisateur* rend la dépense imputable **sans doter l'agent d'une identité inter-fournisseurs**.
3. **La migration institutionnelle dit qui tient la plume, non si quelqu'un écrit.** Deux dons à des
   organismes établis : le second a produit fondation dotée, quarante membres et dépôt transféré ;
   le premier, **ni document ni commit trois mois et demi après**.
4. **Le protocole le mieux gouverné est celui qui ne bouge plus ; celui qui bouge est celui dont on
   découvre les failles.** Cinq correctifs de sécurité en trois semaines sur x402 — SSRF dans la
   découverte, deux contournements de routes payantes, absence de vérification de l'événement de
   transfert après règlement, liaison du défi client à l'origine —, **dont aucun n'a fait l'objet
   d'un avis de sécurité formel**. *La maturité institutionnelle ne prédit ni l'activité, ni la
   sûreté, ni la divulgation.*

**Ce que la littérature ajoute, et qui déplace le diagnostic.** Le mandat signé n'est pas le point de
rupture ; **ses deux bords le sont**. *En amont*, l'intention que la signature scelle est déjà
falsifiable — deux injections dans le contexte d'un agent d'achat de référence détournent le
classement produit et exfiltrent des données (**90 à 100 % de réussite**). *En aval*, les garanties
de signature tiennent au niveau de la spécification mais **pas à l'exécution** — reprises,
concurrence, orchestration —, défaut qu'une vérification à consommation unique et liaison de
contexte corrige en banc de charge (**~3,8 ms à 10 000 tr/s**).

**Deux résultats économiques, non contestés dans leur existence.** Des agents tarificateurs en langue
naturelle atteignent **en oligopole des prix supra-concurrentiels sans communication explicite**,
l'ampleur dépendant de formulations anodines de l'invite. Et **la réputation telle qu'implémentée ne
porte aucun signal exploitable** : sur trois chaînes, la plupart des identités enregistrées n'exposent
aucun point de service actif, les scores sont Sybil-attaquables par construction, la majorité des avis
n'a aucun ancrage vérifiable. *Le seul correctif qui déplace l'aiguille est économique — garantie
exécutable, séquestre, sanction — et non réputationnel.*

**Le désaccord réel du front** : la collusion algorithmique est-elle un régime ou un artefact
d'homogénéité ? Des stratégies collusoires stables émergent dès que les agents raffinent eux-mêmes
leurs invites ; à l'inverse, l'hétérogénéité fait chuter le surprix de **22 % à 10 %** par la
patience et à **7 %** par l'asymétrie d'accès aux données. *L'arbitrage est empirique et personne ne
l'a fait : aucune pièce ne mesure la population effective de modèles tarificateurs.*

**Et la lacune la plus dure : personne ne traite la responsabilité d'une transaction non autorisée.**
Aucun travail ne modélise la répartition entre émetteur, acquéreur, marchand et fournisseur
d'agent ; aucun ne confronte un mandat correctement circonscrit au régime de rétrofacturation
existant ; **aucun ne mesure un taux de contestation**. Sur douze pièces du front, **une seule mesure
un système déployé** — un registre de réputation, non un flux de paiement ; **sept sont des
simulations**.

### 4.4 La couche sémantique : décrire ce qu'un agent sait faire

Les protocoles structurants normalisent la **syntaxe** de l'échange et laissent implicite sa
**sémantique**. Or la découverte « sémantique » que l'*agent mesh* prête à l'agent — trouver *un*
agent capable d'un but plutôt qu'une adresse — **présuppose un vocabulaire comparable par machine**.
Existe-t-il ? **Par examen direct des spécifications : non.**

| Système | Formalisme | Vocabulaire contrôlé | Découverte |
|---|---|---|---|
| A2A — *AgentSkill* v1.0 | `id`, `name`, `description`, `tags` **libres** | non | Agent Card sous URI bien connue |
| ANP — *Agent Description Protocol* | JSON-LD, schema.org **recommandé non imposé** | non | graphes liés, `.well-known` |
| Registre MCP officiel | `server.json` : nom DNS inversé, description libre | non | **sous-chaîne sur les noms**, « intentionally simple » |
| Registres commerciaux | texte libre (nom, description, licence) | non | lexicale |
| **OASF + annuaire `dir`** | *record* : `skills` requis, `domains`, `modules` | **oui** — taxonomie hiérarchique à identifiants numériques, 18 catégories, 3 niveaux | par attributs et contraintes ; catalogue sur `.well-known` |

**OASF est l'unique taxonomie normalisée publiée**, et elle est opérationnalisée par un annuaire
distribué qui trouve les agents « par compétences et attributs structurés ». Trois observations la
bornent : **aucun commit au dépôt OASF depuis le 21 juillet 2026** ; **aucune référence à sa
taxonomie dans un autre protocole du corpus** ; et **la surface de découverte qui a le plus crû —
le *bazaar* d'x402 — emploie des étiquettes libres**. *Le vocabulaire normalisé existe ; le premier
annuaire venu ne l'emploie pas.* Le registre MCP officiel **assume ce refus**.

**Le précédent historique est cité et il n'est pas rassurant.** Parmi les grandes revues de
protocoles, **une seule** cite un antécédent : FIPA-ACL (2000), dont la « complexité de la gestion
d'ontologie » a freiné l'adoption ; les trois autres n'évoquent ni FIPA, ni OWL-S, ni les services
web sémantiques. *La couche sémantique est celle dont une génération antérieure avait fait un point
de blocage — et l'histoire de la FIPA interdit de tenir la convergence pour acquise.*

### 4.5 La couche de confiance

Les quatre couches précédentes **réimplémentent chacune un fragment de la même fonction
manquante** : politique au bord du maillage, mandat signé pour la dépense, registres curés pour la
découverte, traçabilité par l'enveloppe événementielle. L'étage qu'elles présupposent tient en trois
sous-couches — **identité** (qui est l'agent), **délégation** (pour qui il agit), **autorisation**
(ce qu'il a le droit de faire). Il fait l'objet de la section 5 en entier.

### 4.6 L'orchestration des processus d'affaires : la couche installée

*C'est la couche la plus massive du dépôt, la mieux normalisée, et celle que le discours agentique
regarde le moins.*

**Le constat directeur : le moteur de processus se fait client des protocoles agentiques, jamais
l'inverse.** Les moteurs consomment MCP et A2A en connecteurs ; parcs robotisés et processus
s'exposent en outils MCP ; l'intelligence de processus alimente les plateformes d'agents.
**Aucun protocole n'adopte en retour de formalisme de processus.** Ordre, compensation et
transaction longue restent le monopole du moteur.

**Et c'est la seule région normalisée *de jure*** — avec une nuance qui compte : **ISO/CEI
19510:2013 vaut BPMN 2.0.1, non la version courante 2.0.2 de l'OMG**. *L'adoption de jure ne couvre
pas le formalisme courant.* Douze ans sans révision là où MCP itère par trimestre : **cette
immobilité est ce que l'industrie achète**.

| Volet | Socle normatif | Arrimage agentique vérifié | Chaînon manquant |
|---|---|---|---|
| Moteurs GPA | BPMN 2.0.2 (OMG) ; ISO/CEI 19510:2013 = 2.0.1 | connecteur MCP hors arbre alpha **sans DG énoncée**, A2A en alpha | sémantique de processus dans les protocoles |
| Exécution durable | **aucune norme** | intégrations de SDK d'agents (préversion) | portabilité des garanties entre substrats |
| Robotisation (RBA) | aucune norme | serveurs MCP en DG ; agents d'usage de l'ordinateur | idempotence et compensation des actions d'interface |
| Gestion des décisions | DMN 1.5 + **TCK public** (3 391 cas, 79 catégories) | exposition ad hoc en outils MCP | pont normalisé agent ↔ point de décision métier |
| Fouille de processus | **IEEE 1849-2023** (XES) ; OCEL 2.0 | intégrations de plateformes | format de trace d'exécution d'agents |
| Conformité sectorielle | E-23, AMF, art. 12.1, DORA | exigences portées par l'enveloppe | expression des obligations dans les protocoles |

**L'exécution durable, et le mot qu'il ne faut pas croire.** À rebours du discours commercial,
**aucun substrat n'offre d'« exactly-once » distribué de bout en bout** : trois portées circulent
sous ce vocable — le **rejeu déterministe** (le code d'orchestration doit être déterministe ; les
effets externes restent *at-least-once*, à charge d'idempotence) ; l'***exactly-once* co-localisé**
(état applicatif co-localisé avec le journal ; hors périmètre, retour à l'*at-least-once*) ; les
**garanties de démarrage** (un même produit logeant trois régimes sous un même nom, le choix étant
immuable après création). **Faute de transaction distribuée entre organisations, les trois portées
convergent vers la *saga***, qui sacrifie l'isolation contre la faisabilité. *Un tableau de garanties
qui ne dit pas laquelle des trois portées il vend ne dit rien.*

**La robotisation a changé trois fois de position architecturale** : la main du robot est devenue
une capacité de modèle (l'état de l'art sur banc d'usage de l'ordinateur passe de **12,2 %** en avril
2024 à **38,1 %**, puis à environ **66 %** en 2026, contre **72,4 %** chez l'humain) ; les éditeurs
se sont reconvertis en orchestrateurs ; le parc robotisé s'expose en outillage agentique.
**L'action d'interface est l'effet de bord par excellence** — un clic « Soumettre » n'a ni clé
d'idempotence ni contre-écriture —, et **le seul garde-fou normalisé est l'humain**.

**Ce que la littérature ajoute, et elle est ici plus avancée que l'industrie.**

- **L'installé est enveloppé, pas remplacé.** Le mouvement dominant **encercle** le moteur : couche
  agentique régie par politiques autour d'un moteur déterministe **qui conserve l'autorité
  d'exécution** ; modèles de processus typés promus **composants architecturaux de l'agent** ;
  modèle de langue **subordonné à un graphe DCR** encodant les obligations légales. *L'agent
  n'intervient qu'à des points de contrôle nommés — décider, adapter, formuler — jamais sur la
  trajectoire entière.*
- **La fiabilité vient d'une couche transactionnelle en aval, pas du modèle.** Le retour d'outil est
  une **frontière de règlement fausse** ; un contrôle d'admission déterministe rend **la correction
  de l'état engagé indépendante de la compétence du proposant**, à moins de **6 % de surcoût** ; une
  formalisation en TLA+ de quatre anomalies de concurrence, avec exécutif prouvé, en fournit les
  premières garanties mécanisées.
- **Le désaccord dur du front est ontologique, non paramétrique.**

| | **Atomicité** | **Réversibilité** |
|---|---|---|
| Unité de fiabilité | la frontière de règlement | la position de l'action sur l'échelle idempotent / réversible / compensable / irréversible |
| Statut de l'effet | invisible avant engagement | émis, puis révisé |
| Place de l'humain | hors transaction | concurrente de l'exécution |
| Borne de l'agent | ce qu'on peut valider | ce qu'on peut défaire |

*Adopter l'un rend l'autre inatteignable : on ne peut pas simultanément suspendre l'effet jusqu'à la
certitude et l'émettre pour organiser sa révision.* **Aucune pièce du corpus ne compose les deux
régimes ni ne fournit de critère pour choisir entre eux selon la classe d'effet.**

**Et la lacune de méthode la plus nette du dépôt entier : personne ne mesure la conformité
d'exécution d'un agent à un modèle de processus.** Le contrôle de conformité au sens de la
discipline — aligner une trace réelle contre un modèle de référence, quantifier *fitness* et
précision — **n'est appliqué à aucune trace d'agent autonome**. Contrôle vérifiable et refait :
la requête correspondante rend sept entrées, **dont aucune ne porte sur des traces d'agents
autonomes**.

### 4.7 L'exploitation : observabilité, évaluation continue, reprise

*C'est la couche où le dépôt établit son fait négatif le plus important.*

**Le socle a reculé avant d'avancer.** Le 12 juin 2026, la version 1.42.0 des conventions
sémantiques centrales a **déprécié l'ensemble des attributs, métriques, événements et étendues
`gen_ai.*`** et les a transférés vers un dépôt dédié. **Ce dépôt n'a jamais rien publié.**

**Le statut pèse davantage que le décompte.** Tous les documents portent « Status: Development » —
un composant à ce niveau « ne devrait pas être utilisé en production » et « peut être retiré sans
préavis ». **Aucun élément spécifique n'est stable** : les seuls badges `Stable` portent sur des
attributs **empruntés au tronc commun**. Or des éditeurs les intègrent à des offres de production :
*l'adoption précède l'assurance, ici aussi.*

| Objet | État vérifié au 15 août 2026 |
|---|---|
| Étendues d'agent | `create_agent`, `invoke_agent`, `invoke_workflow`, `plan` |
| Métriques | 12, toutes histogrammes et « recommandé » ; 5 agentiques |
| Attributs `gen_ai.*` | **63**, tous *Development*, aucun déprécié (61 → 63 le 7 août, puis arrêt) |
| Espace de noms de l'agent | 4 attributs : identifiant, nom, description, version |
| **Mandat, délégation, autorisation** | **aucun attribut** ; corrélation limitée au contexte de trace, à l'identifiant de conversation et à l'identifiant d'agent |
| Propositions d'identité et de mandat | **8**, du 5 mai au 3 juillet 2026 — **aucune fusionnée ni fermée** |

**D'où le déficit central du temps de l'exploitation : tracer un appel n'est pas tracer une
délégation.** L'outillage dit ce qu'un agent a invoqué, en combien de jetons et de temps ; **jamais
au nom de qui, ni sous quel mandat**. Le manque est **nommé dans le dépôt sans être comblé dans la
norme**.

**Deux faits de la fenêtre d'août confirment le diagnostic sans le déplacer.** Le premier est une
leçon de méthode que le dépôt s'applique à lui-même : l'édition précédente relevait **soixante et
un** attributs ; le relevé était **exact à son gel et faux dix jours plus tard**. *Le fait négatif
le plus cité de la veille s'est périmé en dix jours — la démonstration la plus nette du problème
qu'elle prend pour objet lui est arrivée sur son propre matériau.* Le second : **la révision MCP
`2026-07-28` documente les conventions de propagation du contexte de traçage d'OpenTelemetry** —
première fois qu'un protocole de la couche commune nomme un corpus d'observabilité dans son texte
normatif — **et y renvoie la fonction de journalisation qu'elle abandonne**. *Un texte normatif
emprunte le contexte de trace d'un corpus sans version publiée, et lui délègue une fonction : risque
déplacé, non résorbé.*

**La couche, à peine née, reproduit déjà la fragmentation qu'elle devait résorber** : un jeu de
conventions concurrent, maintenu par un éditeur, **publie quand le corpus standard ne publie pas**,
et l'outil ouvert exige encore la traduction des traces. Le 11 août 2026, ce même éditeur annonce un
support natif du corpus standard **à l'ingestion** — *la fragmentation se résorbe par le tuyau d'un
éditeur, non par une norme*, et **c'est le jeu concurrent qui ingère le corpus standard, jamais
l'inverse**.

**Les deux étages supérieurs sont plus vides encore.** L'**évaluation continue** n'a aucune source
primaire sur des travaux normatifs relatifs aux jeux d'épreuves, à la reproductibilité ou à la
provenance des évaluateurs. La **reprise** — détecter la dérive, réviser ou révoquer le mandat — est
le moins outillé : la révocation est le mécanisme le moins spécifié de la pile, et **21 % seulement
des organisations déclarent un processus formel de mise hors service** (n = 418, étude commanditée
par une partie prenante). *Le passeport certifie un comportement passé, jamais le comportement
courant.*

### 4.8 L'orchestration des agents eux-mêmes : la couche sans porteur

**Le fait négatif est premier.** L'orchestration des **processus** (§4.6) est un cadre déterministe
qui invoque des agents. L'orchestration des **agents** — quel agent décide qu'un autre intervient,
sur quelle topologie, avec quel transfert de contexte — est **traitée nulle part**. Aucun des trois
protocoles structurants ne décrit de topologie ; **chacune des sept couches orthogonales dispose
d'au moins un porteur candidat, celle-ci n'en a aucun.**

**Le langage des patrons se stabilise dans du code plutôt que dans une spécification.** Quelques
topologies convergent — superviseur, transfert entre pairs, chaîne séquentielle, éventail parallèle
—, dont deux livrées en **bibliothèques préconstruites**. *Le patron existe en bibliothèque
installable avant d'exister dans un texte normatif, l'inverse des sept couches précédentes — et une
convention qui naît dans un paquet appartient à qui le publie.* **La démonstration est venue du
paquet lui-même** : le dépôt du superviseur porte en tête que l'éditeur recommande désormais un
autre patron *plutôt que cette bibliothèque*, maintenue pour la seule compatibilité.
*Le patron n'a pas changé ; son véhicule a été déclassé par son propriétaire, sans fenêtre de
dépréciation ni préavis* — là où la couche commune vient de s'en donner une de douze mois.

**Le transfert entre agents est un appel d'outil, et sa valeur par défaut est l'opposé du moindre
privilège.** La documentation du SDK le plus diffusé l'énonce : les transferts « sont représentés
comme des outils », « demeurent au sein d'une même exécution », et l'agent receveur « voit
l'intégralité de l'historique de conversation précédent » sauf filtre explicite. **Trois
conséquences.** *Primo*, une délégation entre agents d'un même exécutif est **un appel de fonction,
non un échange protocolaire** : elle ne franchit jamais la frontière qu'A2A existe pour franchir — et
un parc ainsi orchestré **n'a aucun besoin d'A2A**, ce qui explique une part de la courbe d'adoption.
*Secundo*, le transfert de contexte est **total par défaut**. *Tertio*, **l'appel *est* la
délégation, et rien ne l'accompagne qui vaille mandat**.

**La surface de défaillance est documentée, et elle ne met pas en cause la capacité des modèles.**
Une taxonomie construite sur 150 traces annotées et validée sur **plus de 1 600 traces issues de
sept cadriciels** range les défaillances des systèmes multi-agents en **quatorze modes, en trois
catégories** — conception du système, mésalignement entre agents, vérification de la tâche.
**Aucune n'est une catégorie de capacité du modèle : un système multi-agents défaille par son
agencement.**

**Le mouvement de fond est l'absorption de la boucle d'orchestration par la plateforme**, et il a une
double lecture. Un harnais géré en disponibilité générale prend en charge boucle d'orchestration,
outils, contexte, persistance d'état, reprise sur incident et isolation de session derrière deux
appels d'API, avec des sessions persistantes **jusqu'à quatorze jours**. *L'agencement le plus
souvent fautif quitte les mains de l'équipe qui le câblait* — mais **l'enveloppe que la veille
recommande devient la propriété de l'exploitant**, louée au lieu d'être écrite, alors même que c'est
la seule pièce qu'un assujetti puisse produire devant un tiers. *Une enveloppe louée se renomme au
calendrier du bailleur* : espace de noms, points d'accès et schéma de données ont changé en six
semaines. Et quatorze jours de session **étendent d'autant la fenêtre où un mandat reste
invérifiable**.

**Conclusion du front.** L'orchestration de processus produit **un artefact qui précède
l'exécution** : un modèle versionné, opposable, démontrable devant un tiers. L'orchestration
d'agents n'en produit aucun — *la topologie se fixe en code, mais la décision de transfert est prise
par un modèle, à l'exécution, et ne laisse qu'un appel d'outil dans un journal*. **La thèse de
l'agent enveloppé tient donc sur la première : ce qui enveloppe doit être ce qui se démontre.**

---

## 5. Identité, délégation, révocation

*C'est le verrou commun. Le Vol. III en fait son objet entier ; la veille lui consacre son plus long
développement ; la revue de littérature y trouve la convergence la plus forte de son corpus.*

### 5.1 La grille des cinq questions

Le Vol. III fournit l'instrument de lecture — sans statut normatif — : **qui es-tu, qui t'a créé,
pour qui agis-tu, que peux-tu faire, qui en répond**. Chaque case qualifie ce que le mécanisme
**démontre**.

| Mécanisme | Qui es-tu | Qui t'a créé | **Pour qui agis-tu** | Que peux-tu faire | Qui en répond |
|---|---|---|---|---|---|
| Agent Card signée (A2A v1.0) | oui | partiel | **non** | déclaratif | non |
| Annuaire d'entreprise (identité d'agent) | oui, dans le locataire | oui | **partiel** — propriétaire d'annuaire | oui, dans le périmètre | partiel — l'organisation |
| Identité de charge de travail SPIFFE/SPIRE | oui | oui | **non** | hors périmètre | non |
| Attestations vérifiables / DID (W3C) | oui | oui | **possible, non instrumenté** | via attestations | non |
| Mandats AP2 | non — c'est l'utilisateur | non | **oui** — pour le paiement | borné au montant | oui — l'utilisateur signataire |
| Registre d'agents gouverné | oui, par inscription | oui | **non** | liste d'outils autorisés | partiel — l'exploitant |
| Points de décision d'autorisation | consomme | non | consomme | **oui** — à chaque appel | non |

**Questions 1 et 2 : résolues en production** — annuaire d'entreprise, certificat de charge de
travail, carte signée, inscription à un registre. *C'est de l'IAM classique transposé, et la limite
est de périmètre, non de mécanisme.*

**Questions 4 et 5 : hors identité** — *que peux-tu faire* relève de l'autorisation ; *qui en
répond*, du contrat et de l'organisation.

**Question 3 : le déficit réel.** *Pour qui agis-tu* est la seule colonne presque vide, et son
exception est instructive : AP2 y répond **en changeant le porteur de l'identité** — l'utilisateur
signe à la place de l'agent — et **en bornant la réponse au paiement**. **Au 15 août 2026, aucun
mécanisme vérifié ne répond aux cinq questions.**

### 5.2 Le problème des deux sauts

Deux problèmes sont confondus dans la littérature, et les séparer est le premier acquis. Le
**mandat** : établir qu'un agent agit pour un principal identifié. La **chaîne** : maintenir cette
preuve quand l'agent délègue à son tour.

**Sur le mandat, des mécanismes partiels.** L'échange de jetons OAuth 2.0 donne un jeton dérivé pour
agir au nom d'un principal. Le chaînage d'identité inter-domaines **sera le premier RFC applicable
aux chaînes agentiques**, quoique générique — sa révision est en file d'attente du *RFC Editor* et
**attendait toujours son premier éditeur au 13 août 2026**. Le profil OAuth de délégation « au nom
de l'utilisateur » pour agents est **expiré et archivé, sans successeur**. Les propositions
académiques n'ont ni implémentation inter-fournisseurs ni **révision depuis leur version initiale**.

**Sur la chaîne, l'ordre de grandeur de l'invention a été sous-estimé et il faut le corriger.** Le
relevé du 15 août 2026 dénombre **douze brouillons individuels IETF**, ouverts un à un et datés de
leur **dépôt initial** :

| Dépôt | Mécanisme |
|---|---|
| 25 mars 2026 | chaîne de sauts signée Ed25519, vérifiable hors ligne |
| 16 avril | attestation ancrée dans le DNS |
| 16 avril | méthode DID propre, chaînes jusqu'à onze jetons de principal |
| 25 avril | **atténuation cryptographique par saut** sur socle SPIFFE, chaque parent signant le jeton de son enfant |
| 27 avril | **révocation** par identifiant d'agent, profondeur de cascade paramétrable |
| 29 avril | en-tête de mission reporté jusque dans le jeton de ressource |
| 22 mai | chaîne d'acteurs préservée à travers des flux asynchrones longs |
| 23 juin | reçus d'action signés et chaînés par empreinte |
| 25 juin | **délégation récursive entre organisations** |
| 21 juillet | **révocation portable** vérifiable hors ligne |
| 28 juillet | **atténuation stricte à chaque saut**, composée sur quatre RFC |
| 7 août | chaîne signée transportée dans la requête d'autorisation, nœuds liés par empreinte |

**Le rythme est régulier, non croissant** — et l'édition antérieure y lisait une accélération : *c'était
un artefact de datation*, les dates retenues étant celles des dernières révisions, qui s'agglutinent
en août parce que les auteurs rafraîchissent leurs textes avant expiration.

**L'énoncé porteur résiste, pièce par pièce : aucun mécanisme *normalisé* ne maintient de traçabilité
opposable au-delà de deux sauts.** Les douze portent la mention « not endorsed by the IETF », aucun
flux RFC assigné, aucun état IESG. Le groupe OAuth ne compte **aucun** document de groupe portant sur
les agents ; le groupe d'identité de charge de travail **n'a adopté aucun** des brouillons agentiques
déposés sous son nom ; deux groupes chartés en juin 2026 portent **vingt-sept brouillons et n'en ont
adopté aucun**. **Le déficit n'est pas d'invention, il est d'adoption** — et le fait neuf n'est pas
que l'invention s'emballe, c'est qu'**elle produit à cadence constante depuis cinq mois sans qu'un
seul document franchisse l'adoption**.

**La raison structurelle est nommée et fait consensus de conception : chaque saut doit être une
atténuation**, le mandat transmis devant être strictement inférieur au mandat reçu, faute de quoi la
chaîne permet une élévation de privilèges. Trois des douze brouillons en font leur exigence
centrale. *Convergence de conception, non de norme.*

**MCP l'a nommée dans son périmètre** — délégué confus, consentement par client imposé (*MUST*),
relais de jeton proscrit, huit classes d'attaques. **Le problème est identifié à l'intérieur d'un
protocole ; manque son traitement *entre* protocoles et entre organisations.** La révision
`2026-07-28` le confirme par ce qu'elle ne fait pas : validation obligatoire de l'émetteur,
identifiants de client liés à leur émetteur, enregistrement dynamique déprécié — **elles ferment des
confusions exploitables, mais portent sur les questions 1 et 4. Aucune ne concerne la chaîne de
mandat.**

### 5.3 Ce que la littérature établit sur l'atténuation

**La convergence la plus forte du corpus académique porte sur ce point exact** : l'autorité doit
décroître à chaque saut au lieu de se transmettre intacte, et **le jeton porteur relayé tel quel est
unanimement tenu pour le mauvais primitif**. Elle est obtenue par des travaux qui ne partagent ni
méthode ni objet : atténuation de portée comme opérateur compositionnel avec preuves formelles ;
rétrécissement d'autorité **mécaniquement vérifié en TLA+ sur 2,7 millions d'états**, aux côtés du
confinement de cascade et de la reconstructibilité forensique ; chaîne *append-only* où chaque saut
est signé et vérifiable hors ligne ; capacités **bornées par époque**, se fermant à l'achèvement de
la tâche.

**Deuxième convergence : la validité doit être liée à un événement, non à une horloge.** Trois
travaux indépendants, qui ne se citent pas, obtiennent des gains d'ordre cent — *et ils ne les
obtiennent pas au même régime*.

| Événement liant la validité | Gain rapporté | Référentiel | Régime de mesure |
|---|---|---|---|
| compteur d'exécutions, cohérence dirigée | borne indépendante de la vitesse de l'agent ; **120–184×** | baux temporels | simulation à événements discrets, 120 exécutions |
| preuve périodique de vivacité du parent | **~90×** sur la fenêtre d'agent zombie | OAuth 2.0 | couche protocolaire **et essaims d'agents réels** |
| achèvement de tâche, poignées bornées par époque | fermeture de l'accès futur, **sans facteur chiffré** | autorité résiduelle | moniteur de référence, dépôts réels figés |

*Un facteur mesuré en simulation et un facteur mesuré sur essaim réel ne s'additionnent pas.*

**Troisième acquis : l'identité ne suffit pas, c'est l'action qu'il faut prouver.** Le contexte de
délégation doit être **lié pendant l'exécution et non reconstitué après** ; la preuve d'action doit
être **ancrée plutôt que déclarée par l'opérateur** ; et chez les identités non humaines, une
modélisation à l'échelle d'une flotte infonuagique réelle montre que **le sur-privilège est un
régime temporel et non un état**.

**Le terrain ne tient pas même le socle à un seul saut.** Sur **7 973 serveurs MCP distants,
40,55 % exposent des outils sans aucune authentification** ; les failles d'enregistrement dynamique
de client touchent **96,6 %** des serveurs testés. Près de **100 000 enregistrements d'identité
multi-chaînes** confirment une infrastructure immature. Et la vérification formelle des
spécifications relève **35 lacunes de spécification et 30 défaillances nées de la seule
composition** : **un seul protocole applique effectivement un contrôle de sécurité, aucun n'assigne
la responsabilité d'application au comportement inter-protocoles.**

**Le seul parc d'entreprise décrit dans tout le corpus est arrivé le 11 août 2026.** Rapport de
déploiement industriel : des dizaines de serveurs MCP internes montés en une année, **chaque équipe
ayant implémenté son authentification de son côté, certaines sans aucune** ; la parade est une
**passerelle unique** d'agrégation, de gouvernance et d'authentification, avec modèle à deux axes
(personne interactive ou automate × type de justificatif), trois octrois d'authentification unique,
trois modèles d'approvisionnement de jeton, et délégation par échange de jetons. *Le motif déclaré du
chantier est ce que la littérature du front traite le moins : autoriser les appelants de façon
cohérente, savoir qui a fait quoi, et retirer ses accès à un employé qui part, à l'échelle du parc.*
**Régime : rapport d'expérience, aucune mesure, aucun taux. Il atteste d'une architecture en
production, pas d'un résultat.**

### 5.4 Les deux désaccords non arbitrés

**Premier — l'emplacement de la racine de confiance, et son prix opérationnel.** Une position
soutient qu'**aucune preuve d'action n'est opposable sans ancrage matériel** — architecture
d'attestation à distance composée avec des paquets de preuves d'action et une mesure d'intégrité
matérielle. Deux travaux revendiquent l'opposabilité **sans matériel spécialisé ni vérificateur en
ligne** — vérification hors ligne à la seule clé publique de l'émetteur ; fraîcheur appliquée avec
les seules clés en cache et l'horloge locale. *Le désaccord est symétrique dans ses coûts : le
premier camp exige une infrastructure d'attestation que la quasi-totalité des parcs n'a pas ; le
second accepte structurellement qu'un agent compromis mais vivant signe des sauts parfaitement
valides.*

**Second — un arbitrage de type CAP déguisé en question d'identité.** Borner les opérations non
autorisées **indépendamment de la vitesse de l'agent** suppose, par l'analogie même avec la cohérence
mémoire qui fonde le résultat, **un point de sérialisation partagé**. L'autre position **refuse tout
aller-retour réseau** au moment de la vérification et assume en contrepartie une **fenêtre
résiduelle** égale à l'intervalle de battement. **Aucune des deux pièces ne reconnaît la position
adverse : le champ n'a pas nommé l'arbitrage qu'il pratique.**

### 5.5 La révocation : le mécanisme le moins spécifié de la pile

**Chaque mécanisme d'identité spécifie l'émission avec soin et la révocation avec négligence** —
l'histoire des infrastructures à clés publiques se reproduit, et le Vol. III comme la veille le
constatent indépendamment.

L'inventaire est court. **Agent Cards A2A** : signature et vérification en six étapes, **aucune
section de révocation** dans la spécification ; le seul mécanisme voisin est le remplacement de carte
en cache au changement de version — *accepter une carte n'apprend jamais qu'elle a cessé d'être
valable*. **Jetons OAuth** : durée de vie courte, introspection, révocation — toutes supposant un
émetteur joignable, coûteux au rythme d'une flotte. **Entrées de registre** : retrait par
l'exploitant, sans portée hors du périmètre. **Attestations vérifiables** : mécanisme de statut
spécifié, **usage agentique toujours non documenté**.

**Deux conséquences, dont une mesurée.** *La vérification à l'admission ne protège pas de la dérive
après admission* : un serveur dont le comportement change après approbation garde une identité
valide — la réécriture d'une configuration *déjà approuvée* en est le cas documenté. Et **21 %
seulement des organisations ont un processus formel de mise hors service**.

**La révocation en cascade a cessé d'être un trou pour devenir un désaccord de conception non
arbitré**, et c'est la correction la plus nette de la période. **Trois auteurs indépendants, trois
modèles de propagation irréconciliables, zéro adoption** : un point d'accès de révocation avec
paramètre de profondeur de cascade (−1 propage sans limite, 0 borne à l'agent visé) ; une
invalidation en cascade **sous cinq secondes** avec reçus signés contre l'épissage de chaînes ; et,
à l'inverse assumé, **un objet signé portable qui révoque *une* cible nommée et exclut explicitement
la cascade de son périmètre**.

**Et la littérature confirme le trou par l'autre bord.** Toutes les pièces d'identité bornent la
fenêtre pendant laquelle un agent révoqué agit encore ; **aucune ne dit ce qu'il advient des effets
et des sous-délégations déjà émis quand un saut amont est invalidé après coup**. Il n'existe **ni
sémantique de compensation en cascade, ni critère décidant quels effets aval sont annulables**. Deux
constats l'aggravent : des **traces d'exécution identiques peuvent correspondre à plusieurs
assignations de délégation mutuellement incompatibles**, si bien que l'ensemble des effets à
compenser **n'est pas calculable a posteriori** ; et aucun des quatre régimes réglementaires
européens examinés ne définit à qui incombe cette compensation.

*Une pièce du 12 août 2026 traite la moitié informationnelle du problème* — un modèle bitemporel
décidant si un enregistrement contradictoire, remplacé, rétracté, supprimé ou périmé peut encore
étayer une affirmation sortante, par cinq clauses exécutables dont la **non-résurrection après
rétractation** ; sur un banc de 3 600 cas figé par empreinte, la voie gouvernée reproduit **tous** les
dénouements complets quand la meilleure des politiques simples n'en apparie que **la moitié**.
**Mais ce qu'elle gouverne, ce sont les enregistrements et les affirmations qui en dérivent : les
effets déjà produits et les sous-délégations déjà consenties restent sans sémantique de
compensation.** *Chaîner les droits de façon vérifiable, et même chaîner la validité des faits, ne
dit rien du chaînage des conséquences.*

### 5.6 Know Your Agent, et pourquoi l'analogie ne tient pas

Le marché a emprunté à la conformité financière un nom pour l'admission d'un agent tiers.
**Terme de marché avant d'être terme de norme : aucune spécification du corpus vérifié ne le
définit.**

Le principe est juste — vérifier avant d'admettre plutôt que faire confiance et surveiller. **Il omet
l'essentiel : le KYC fonctionne parce qu'il repose sur une infrastructure institutionnelle** — pièces
d'identité étatiques, registres publics, obligations légales, sanctions. **Rien de tel pour les
agents.** L'infrastructure institutionnelle **ne s'est pas rapprochée d'un pouce** dans la période :
le document conceptuel de référence sur l'identité et l'autorisation des agents demeure un
**brouillon public initial**, consultation close le 2 avril 2026, **sans version finale ni
description de projet au 15 août 2026**. *Le KYA nomme le problème ; il ne le résout pas.*

### 5.7 L'horloge post-quantique

**Correction de portée d'abord**, et elle est importante. Contrairement au chiffrement, où la moisson
différée impose de migrer avant la machine quantique, **un système d'authentification demeure sûr
tant que les algorithmes et les clés employés pour authentifier sont sûrs *au moment de l'usage***.
Or cartes signées, jetons, certificats de charge de travail et mandats relèvent très majoritairement
de l'**authentification** : la pression y est plus faible. **Reste la transition** — artefacts à
longue durée de vie et ancrages de confiance à renouveler.

**L'outillage a progressé, l'horloge a ralenti.** Les trois normes fédérales post-quantiques sont
finales depuis le 13 août 2024. Le seul acquis normatif net de la période est l'enregistrement des
signatures ML-DSA pour les formats JSON et CBOR (mai 2026, norme proposée), plus un type de clé
générique ouvrant la voie à d'autres algorithmes. **Les Agent Cards A2A étant signées au format
JSON, la brique normative existe désormais** — et le fait négatif n'en est que plus net :
**A2A v1.0.0 ne mentionne aucun algorithme post-quantique**, ses mécanismes s'arrêtant aux clés
d'API, à l'authentification HTTP, à OAuth 2.0, à OIDC et au TLS mutuel, **sans feuille de route**.

**Le lien avec la délégation est structurel** : plus une chaîne est longue, plus elle accumule
d'artefacts signés dont la durée de vie chevauche l'échéance de dépréciation. **La crypto-agilité est
la contrainte de calendrier de la délégation** — et les douze brouillons de délégation signent tous
en Ed25519 ou en EdDSA.

### 5.8 Émettre, appliquer, exploiter — et l'ordre inverse de l'investissement

Le Vol. III décompose l'« identité des agents » en **trois temps**, et c'est la lecture la plus
opératoire du dépôt.

| Temps | Ce qu'il faut établir | État | Instruments |
|---|---|---|---|
| **Émettre** | une identité opposable | **le mieux servi** — questions 1 et 2 résolues en production ; limite de périmètre, non de mécanisme | annuaire, SPIFFE, carte signée, registre |
| **Appliquer** | la vérifier là où elle est vérifiée | **moyen** — mécanismes réels bornés à un maillage, **aucun ne revendiquant le statut de norme** | passerelles, points de décision externes, interception |
| **Exploiter** | vérifier que le comportement d'aujourd'hui tient encore le mandat d'hier | **vide** | aucun élément d'observabilité stable, aucun attribut de mandat, révocation la moins spécifiée |

**Le déficit suit l'ordre inverse de celui dans lequel le marché investit**, les annonces portant
massivement sur l'émission. Et **l'enveloppe fournit par substitution ce que la couche d'identité ne
fournit pas** : identité stable là où l'agent n'en a pas, trace que l'agent ne doit pas produire
lui-même, mandat qu'aucun mécanisme normalisé ne maintient au-delà de deux sauts. *D'où la question
que la veille recommande de poser à tout fournisseur :* **laquelle des pièces de l'enveloppe
fournissez-vous, laquelle reste à ma charge ?**

---

## 6. Sécurité : ce qui est mesuré, et l'instrument qui mesure

### 6.1 Le défaut de fond n'est pas dans le modèle

**C'est l'absence d'isolation entre contenu de confiance et contenu non fiable**, et quatre pièces y
aboutissent par des voies distinctes.

- **La famille des injections de *donnée*** — charge déguisée en identifiant de ressource, en origine
  de données ou en format de réponse d'outil, **échappant donc aux défenses conçues contre
  l'injection d'instruction** — est démontrée sur **six agents commerciaux nommés**.
- **L'analyse de cause racine des chaînes d'outils parasites**, sur **12 230 outils de 1 360
  serveurs**, l'identifie sous sa forme jumelle : **MCP n'offre ni isolation contexte-outil, ni
  moindre privilège**.
- **Un banc de 202 paires injection-tâche** sur les fichiers de compétences conclut que **ni
  l'échelle des modèles ni le filtrage d'entrée n'y suffiront**.
- **La seule proposition constructive du lot** en tire la conséquence : convertir la donnée non
  fiable en **types de portée et de contenu bornés**.

### 6.2 La capacité aggrave l'exposition, et l'alignement ne protège pas

Sur **45 serveurs vivants, 353 outils authentiques et 1 312 cas de test évalués sur 20 agents**,
l'empoisonnement de métadonnées atteint **72,8 % de succès sur le modèle le plus vulnérable du
lot** ; **la susceptibilité croît avec la capacité du modèle**, et **le taux de refus le plus élevé
reste inférieur à 3 %** — l'attaque n'employant que des **outils légitimes**. Un second banc atteint
**80 %** sur les modèles de pointe.

### 6.3 Les scores de défense ne survivent pas à l'adaptatif

*C'est le résultat décisif pour la lecture de tout le front.* Une défense mesurée à **0 % de succès
d'attaque en statique** remonte à **28 % au global et 64 % sur les tâches où l'action elle-même est
déléguée à du contenu contrôlé par l'attaquant**, dès qu'une optimisation en boîte noire et **à bas
coût** la cible.

L'audit de **dix défenses sur 60 tâches ouvertes et 560 cas d'injection** conclut que **presque
aucune n'est déployable** — chacune étant soit insuffisamment sûre, soit **sur-défensive au point
d'entamer la fonctionnalité**. Sur **six systèmes multi-agents et 1 356 cas**, les défenses mises au
point en environnement simplifié **ne transfèrent pas et peuvent créer de nouvelles
vulnérabilités**. Trois mécanismes de contrôle d'accès publiés tombent à **86,3 % de contournement
pour 4,4 % de dégradation d'utilité**.

Deux attaques sont opposables en production : **14 scénarios contre des assistants déployés, dont
73 % classés en risque élevé à critique avant mitigation**, et la famille d'injections de donnée
précitée.

**Un contre-exemple revendiqué est apparu le 13 août 2026, et son régime décide de sa portée.** Un
filtrage des unités de réponse **par provenance et par attente sémantique** ramène le succès
d'attaque moyen de **84,7 % à 2,3 %** sur six découpages de deux bancs, en préservant l'utilité
bénigne (**92,5 % contre 90,6 % sans défense**). *Défense évaluée par ses propres auteurs, sur un
seul agent cible.* **Ce n'est pas le régime qui a fait tomber les autres défenses** : nulle
optimisation en boîte noire ne vient ici cibler la défense elle-même. **Le contre-exemple est à
retenir, non à opposer.**

### 6.4 Le désaccord qui entame tous les pourcentages du front

**L'écosystème MCP est déclaré criblé de *gadgets* exploitables en conditions réelles** — sur
12 230 outils et 1 360 serveurs. **Sur un corpus cinquante fois plus grand — 64 611 serveurs uniques,
dont 37 288 analysables dynamiquement —, l'instrument qui produit ce type de constat est montré faux
à plus de moitié** : les scanners qui déclarent **96,89 % des serveurs « à risque » présentent moins
de 50 % de vrais positifs à la validation manuelle, et se contredisent entre eux**.

*Les deux ne peuvent décrire correctement le même parc*, et ce désaccord entame la valeur probante
de **tous** les pourcentages de prévalence du front, y compris ceux repris par les revues : **soit la
sévérité est sous-décrite, soit une part importante des taux publiés est un artefact d'outil**.

**Deux traits l'aggravent, documentés par les pièces elles-mêmes.** *Monoculture méthodologique* :
les études de sécurité MCP partagent un même dispositif — **l'audit d'un registre à un instant
unique** —, et **aucune n'a mesuré la durée de validité du texte qu'elle juge**. *Chiffre hérité* :
le taux de 96,89 % provient de scanners appliqués à peu de cas et **se propage par citation —
repris, non reproduit**.

**Deux pièces de la mi-août tranchent dans le sens de l'artefact.** La première audite une campagne
d'évaluation conservée et **montre que le défaut était dans le correcteur** : la métadonnée de
traitement conditionnait la classe de succès d'attaque, si bien qu'**un comportement inchangé
changeait de classe sous simple réétiquetage** ; une reconstruction aveugle au traitement reclasse
**58 étiquettes** en achèvements bénins autorisés, tout en préservant trois transferts de données
protégées vérifiés — **le recensement verrouillé ne contient plus aucun succès d'attaque**.

La seconde rend le constat systématique : **réduire la sécurité d'un agent à un taux de succès
d'attaque unique confond exposition, exécution, observation et adjudication**, et confond une
violation réelle avec **la visibilité de sa preuve**. Sur **1 661 cas répartis sur cinq surfaces de
service, six modèles et trois harnais**, le taux moyen s'établit à **65,69 % — mais le taux rapporté
varie avec le harnais retenu et avec la vue de preuve**, et **divulguer le contexte d'évaluation
change le comportement d'exécution**. La pièce vérifie les effets nuisibles **sur les reçus de
service et l'état final** plutôt que sur la sortie de l'agent, et relève un **écart
reconnaissance-exécution : près d'une violation confirmée sur cinq survient après que l'agent a
énoncé la contrainte qu'il enfreint**.

### 6.5 L'écart adoption-assurance, chiffré

**C'est le risque systémique majeur du domaine**, et le dépôt le pose comme tel.

*Côté adoption* : MCP est en disponibilité générale chez presque tous les fournisseurs — **400
millions de téléchargements mensuels de SDK, plus de 950 serveurs au répertoire officiel** (décompte
sans source primaire) ; un acteur déclare qu'en juin 2026 l'IA agentique a écrit ou révisé **la
quasi-totalité de son code**.

*Côté assurance* : **414 serveurs MCP publics audités — 68 vulnérabilités, 91,8 % sans
authentification OAuth**. **Et les agents *agissent* : le défaut se paie en actions exécutées.**

*Concordances indépendantes* : **plus de 40 % de projets d'IA agentique annulés d'ici fin 2027** ;
**une entreprise sur cinq** à gouvernance mature ; étalement agentique majoritaire.

**La surface est exploitée** : la base nationale de vulnérabilités recense contre l'outillage MCP un
inspecteur non authentifié, l'injection de commande par un serveur non fiable (score **9,6**),
l'exécution de code persistante par réécriture d'une configuration approuvée, et deux entrées de
2026. **Elles ne visent pas le protocole : elles visent la frontière de confiance que l'implémenteur
trace autour de lui.**

### 6.6 Ce que le front ne mesure pas

**Aucune pièce ne mesure quoi que ce soit sur un parc d'entreprise en exploitation.** Les tailles
d'échantillon se comptent en serveurs (64 611 ; 1 360 ; 45), en outils (12 230 ; 353), en cas de test
(1 661 ; 1 356 ; 1 312 ; 560 ; 202), en modèles, en produits — **jamais en organisations, en
déploiements ni en incidents observés, sans aucune télémétrie de production**.

**Ce qui reste ouvert n'est plus l'absence d'audit mais son absence de réplication** : les deux
audits d'instrument n'ont été reproduits par aucun tiers et ne portent pas sur les mêmes bancs.
Demeure la lacune inter-organisationnelle : **la seule pièce inter-agents reste intra-système**,
rien ne portant sur la chaîne d'appel entre organisations distinctes.

---

## 7. Évaluation, bancs d'essai et observabilité

### 7.1 Le score publié n'est pas ce qui s'observe

**Cinq voies indépendantes l'établissent**, et la cinquième est la plus radicale.

1. **Défauts de conception** — tests insuffisants, **réponses vides comptées comme succès**,
   récompenses mal spécifiées faussent les scores des bancs les plus utilisés.
2. **Généralisation** — une part substantielle de la performance sur un banc de génie logiciel de
   référence relève de **la mémorisation du dépôt**, les mêmes modèles chutant fortement sur des
   tâches hors distribution appariées.
3. **Enchaînement en exploitation** — sur une chaîne de construction de compilateur à dépendances
   sérielles, la réussite s'effondre de **100 % au premier étage à 20 % au dernier**, **aucun des
   15 modèles n'achevant le pipeline**. Les bancs d'entreprise donnent la même pente : **~30 %** de
   tâches professionnelles achevées en autonomie dans une entreprise logicielle simulée ; **58 % en
   tour unique contre 35 % en multi-tours**.
4. **Transport d'exécution** — rejouer la même réponse à travers un analyseur syntaxique
   délibérément ajouté fait chuter la réussite de **55,4 à 73,2 points** selon huit configurations
   comparables ; divulguer la frontière au modèle en récupère **30,4 à 60,7 points**. *Un modèle dont
   l'écart de score apparié n'est que de −3,6 points cache ainsi −64,3 points de dégât et +60,7
   points de compensation*, et **la configuration de déploiement réordonne les modèles**.
   **Le score n'est donc pas une propriété du modèle mais du montage** : une évaluation qui ne
   déclare pas sa configuration, son contrat de génération, son chemin d'exécution, son point de
   fonctionnement et son validateur d'état final **ne dit pas de quoi elle parle**.
5. **Décomposition de variance** — sur trois bancs ouverts de traces d'agents, **l'effet propre de
   l'agent explique moins de 3 % de la variance totale**, quand **l'interaction agent × tâche en
   explique de 7 à 23 %** ; la fiabilité agrégée s'effondre sur le quartile de tâches le plus dur
   (un coefficient tombant de **0,752 à 0,000**) ; et la fiabilité mesurée en cellule
   d'entraînement est **négativement corrélée** à la fiabilité hors échantillon (**r = −0,90**).
   **Conclusion : un classement d'agents ne classe pas des capacités, il classe des
   spécialisations.**

### 7.2 Le coût et le régime d'exécution sont des dimensions d'évaluation

L'exactitude seule est vide de sens sans axe de coût, et l'absence de jeu de retenue rend les scores
irreproductibles. En exploitation, **la dépense varie de trois ordres de grandeur entre modèles de
qualité comparable**.

**Le prix de l'auditabilité se chiffre aussi**, et c'est l'un des rares chiffres opérationnels du
champ : **8,3 ms de surcoût médian** pour une médiation pré-exécution à traces infalsifiables,
mesurés sur **1 000 interceptions consécutives** d'appels d'outil — **P95 à 14,7 ms, P99 à 23,1 ms,
1,2 % de faux positifs sur 500 appels bénins**.

### 7.3 La trace est devenue l'objet évalué, et les modèles la lisent mal

Sur **148 traces annotées par des humains**, collectées **au format d'observabilité réellement
déployé**, le meilleur modèle à long contexte n'atteint que **11 % en localisation d'anomalie**.

L'auditabilité se décompose en cinq dimensions — recouvrabilité de l'action, couverture du cycle de
vie, vérifiabilité de la politique, attribution de responsabilité, intégrité de la preuve — et
**l'intégrité de la preuve et la couverture du cycle de vie sont les plus négligées** de tous les
travaux recensés.

**Un piège d'ingénierie mérite d'être isolé, parce qu'il touche du code déjà expédié.** Toute une
classe de **portes de qualité livrées dans les cadriciels d'agents** — filtres de déduplication,
caches sémantiques, gardes de dérive, correcteurs de réponse — **décide à un seuil de similarité
cosinus**, c'est-à-dire mesure **de combien la formulation a changé**, quand la question posée est
**si le sens a changé**. Les deux divergent **précisément sur les cas que ces portes existent pour
attraper** : une garde de dérive en production auditée **n'a détecté aucune des 56 mutations qui
rompent le sens** — dont « *withhold the study drug* » devenu « *administer the study drug* »,
approuvé à un cosinus de **0,9608**. Sur 90 cellules, l'exactitude équilibrée **ne dépasse jamais
0,700**, pour une médiane de **0,525**. *Et le même biais corrompt l'évaluation censée le détecter* :
un corpus construit naïvement en hérite et peut rendre **un verdict inversé** — l'aire sous la courbe
de décision valant **exactement 0,000 dans 13 cellules sur 18**.

### 7.4 Les deux désaccords du front

**L'évaluateur automatique.** Une pièce conclut qu'un juge agentique, notant les étapes
intermédiaires et non le seul résultat, **s'approche de la fiabilité humaine à une fraction du
coût**. Une autre démontre l'inverse **au niveau du principe** : dès lors que le juge n'est pas plus
exact que l'évalué, **aucune méthode de débiaisage ne réduit de plus de moitié le besoin d'étiquettes
de référence**. *Le désaccord oppose une mesure empirique à un plafond théorique et n'est pas
dissoluble par davantage de données* — et la mesure empirique est **auto-arbitrée**, les mêmes
auteurs publiant le banc et le juge qui y domine. **Deux autres conflits d'intérêts sont vérifiés** :
un banc d'entreprise partage quatre auteurs avec le système de référence qu'il mesure ; un banc
d'affaires est publié par le fournisseur du produit concurrent du domaine évalué.

**L'auditabilité : lecture a posteriori ou médiation à l'exécution ?** Le programme dominant
instrumente puis analyse. Une pièce le tient pour **structurellement borné** : **deux attributions de
mandat incompatibles peuvent produire des traces strictement identiques**, la télémétrie usuelle
étant **sémantiquement insuffisante pour reconstruire la propagation d'autorité**. Deux pièces de
mi-août prennent le second parti et le chiffrent — provenance typée comme **signal de contrôle
opérationnel** plutôt que métadonnée d'audit a posteriori, et définition de l'**exécution gouvernée**
comme travail dont les décisions, l'achèvement et la réaction au changement sont adossés à une
provenance inspectable.

### 7.5 Le banc qui manque

**Il n'existe aucun banc dont le critère de réussite soit : à partir de cette trace, un tiers
peut-il reconstruire qui a mandaté quoi, et imputer la responsabilité ?**

Les bancs d'entreprise notent l'état final ; les corpus de traces notent la localisation d'erreur ;
l'auditabilité est proposée comme modèle de données. Une pièce **mesure bel et bien une
reconstruction** — attribution de jetons voisine de **0,95**, recouvrement de segments **~0,93**,
similarité d'arêtes **~0,96**, sur des topologies de quatre à six agents, et **sous trois conditions
de dégradation** — mais *ce qu'elle reconstruit est la structure d'interaction, non le mandat*.

Une pièce du 13 août 2026 s'en approche par un autre bord, et **elle rapporte son propre échec** :
une épreuve de transfert entre rôles séparés où le contrat de complétude appliqué de façon
déterministe **sur-bloque massivement** des paquets produits hors de son contexte de rédaction — et
elle **refuse de se présenter comme un gain d'exactitude**.

---

## 8. Systèmes multi-agents : rendement, attribution, dépendance

### 8.1 L'attribution de défaillance est d'abord une propriété du banc

Sur les journaux de **127 systèmes multi-agents**, la meilleure attribution automatique trouve
l'agent fautif dans **53,5 %** des cas et l'étape décisive dans **14,2 %** — **plusieurs méthodes
faisant moins bien que le hasard**. *Ce plafond est celui d'un banc, non celui de la tâche* : un
modèle déposé le 11 août 2026 rapporte **81,58 %** sur l'agent fautif et **63,90 %** sur l'étape,
mais **sur deux autres bancs**, le premier ne lui servant que d'épreuve hors domaine. Les traces
complètes — entrées et contexte, non les seules sorties — améliorent l'attribution **jusqu'à 76 %**
contre une observation partielle, *gain relatif sans effectif ni condition nommée*.

**Trois mesures d'attribution, trois bancs, aucun dénominateur commun.**

### 8.2 Le rendement du multi-agent est non monotone

- Un **agent unique bien invité** égale presque la meilleure discussion multi-agents, qui ne
  l'emporte que **sans démonstration dans l'invite**.
- Sur **six bancs et 245 caractéristiques**, l'agent unique gagne dans environ **43,3 %** des cas.
- Les architectures **engendrées automatiquement** restent sous la chaîne de pensée avec
  auto-cohérence, **à coût jusqu'à dix fois supérieur**.
- Les résultats favorables ne l'infirment pas : la loi d'échelle collaborative, établie jusqu'à plus
  d'un millier d'agents, est **logistique, donc saturante** ; et l'optimisation entrelacée fait
  dépendre la performance **davantage du réglage des invites que du patron topologique**.
- Le **surcoût de coordination** va de **1,15× à 2,3×** selon le patron ; la supervision d'exécution
  récupère **−29,68 % de jetons** sans perte de succès.

**Le clivage suit la méthode, non l'objet.** Une pièce tranche en partie : le débat multi-agents
**n'est pas intrinsèquement inférieur, il est hypersensible aux hyperparamètres** et redevient
compétitif après réglage. *Tout résultat mesure donc d'abord l'effort de réglage consenti à chaque
bras, qu'aucune pièce du front n'égalise.* Et le partage des positions est net : **les quatre
évaluations indépendantes contre ligne de base forte concluent toutes au non-avantage** ; les deux
pièces concluant à l'avantage évaluent **l'architecture de leurs auteurs contre une ligne de base non
optimisée**.

### 8.3 Le résultat le plus lourd : la redondance est sur-créditée

*Il atteint le calcul qui justifie la redondance, en amont de toute architecture.*

**Les bornes de fiabilité compositionnelle multiplient les fiabilités des composants, opération que
seule autorise une hypothèse d'indépendance conditionnelle qu'on énonce couramment et qu'on ne teste
jamais.** Testée, elle tombe : **deux instances d'un même modèle, en passage de main à deux agents,
échouent ensemble sur 90,0 % des missions où l'une des deux échoue** (rapport de cotes logarithmique
**6,66** ; **φ = 0,916**), sur **18 000 missions notées par du code déterministe et sans juge
modèle**. Changer de modèle réduit l'association dans **six contrastes sur six** ; **changer de
fournisseur à modèle déjà différent ne la réduit pas** — hypothèse enregistrée d'avance, rapportée
comme nulle.

**L'erreur a un signe, et il joue contre l'exploitant** : la dépendance positive gonfle l'échec
conjoint au-dessus du produit des fiabilités, de sorte que **le certificat crédite la redondance
exactement là où elle n'existe pas**.

**Et l'échappatoire est fermée** : ajuster un modèle de dépendance fait **pire** que s'en passer — une
borne *bootstrap* sur la fonctionnelle d'un modèle ajusté **perd la couverture de la vérité à mesure
que l'effectif croît**, l'écart d'identification étant en O(1) quand la correction n'est qu'en
O(n^−1/2). *Plus de données rend alors le certificat plus faux, sans symptôme visible.*

**Régime** : prépublication non révisée par les pairs, banc des auteurs, non répliquée — **mais
préenregistrée et à notation déterministe**, le régime de mesure le plus exigeant du front. *Elle ne
prend parti dans aucun clivage : elle éprouve une hypothèse dont les deux camps se servent.*

### 8.4 Ce que la traçabilité ne résout pas

Levier de diagnostic principal pour une ligne de travaux, elle **laisse échapper un canal d'état** :
un **contexte toxique compressé en résumé passe sous le seuil des détecteurs en augmentant la
toxicité en aval**. *Instrumenter davantage et gouverner l'écriture en mémoire sont deux corollaires
opposés.* Même partage sur la supervision : **machine, elle réduit le coût sans perte** ; **humaine
et fatigable, elle suit un U inversé**, la sécurité réalisée se dégradant au-delà d'un seuil
d'escalade.

### 8.5 Ce que le front ne mesure pas

**Aucune pièce ne mesure un assemblage en exploitation d'entreprise** — taux de défaillance observé
sur durée et volume réels. Les mesures portent sur des bancs académiques, des corpus hors ligne, des
marchés de prédiction, des journaux a posteriori, des missions synthétiques. *Le taux d'échec « en
production » de 41 à 87 % qui circule est repris de la littérature, non mesuré.*

**Manque également toute comparaison contrôlée des patrons d'orchestration** — superviseur,
transfert, graphe, marché — à modèle, invite, outils et budget figés sur plusieurs domaines.

---

## 9. Chorégraphie et essaim : la frontière de la coordination

*Le front précédent mesurait des assemblages conduits ; celui-ci prend la question par l'autre bout —
ce que la coordination achète et coûte quand aucun superviseur ne la tient.*

### 9.1 Le socle théorique du traité

Trois résultats bornent ce qu'un architecte peut promettre, et **ils ne se contournent pas** : en
système asynchrone, **un seul processus fautif par simple arrêt suffit à rendre impossible tout
protocole de consensus binaire garantissant la terminaison** ; sous partition réseau, **aucune
implantation d'un objet partagé n'est simultanément atomique et disponible** ; et **la capacité d'un
système dont les unités entretiennent une vue commune n'a pas un rendement décroissant mais un
maximum**, au-delà duquel ajouter des unités en retire.

**La thèse du traité est un déplacement, non une suppression.** Le point partagé n'est pas détruit,
il est **transporté dans le milieu** — un journal en ajout seul, ordonné, durable et relisable, où la
trace est un enregistrement, le voisinage l'intervalle entre le décalage validé d'un agent et la fin
courante, et l'évaporation une politique de rétention. *Le milieu, il faut désormais le répliquer,
l'exploiter et le facturer.*

**Ce que le déplacement achète se mesure** : la propagation d'un changement à toute la population
coûte **une écriture et une lecture par agent** au lieu d'un nombre **quadratique** de messages, et
le producteur n'a pas de destinataire à connaître. **Ce qu'il coûte se mesure aussi** : la durée d'un
tour n'est plus un aller-retour mais **la latence de queue d'un chemin écriture-durabilité-lecture** ;
la localité, gratuite dans un espace métrique, devient **une clé de partitionnement** ; et **la
reproductibilité, jamais attendue d'un essaim de robots, est attendue par défaut d'un système
logiciel** — l'essaim la retire, et reporte la charge de preuve sur la traçabilité et le point de
reprise.

**Le critère de partage est formel** : les programmes qui admettent une implantation distribuée
cohérente **et sans coordination** sont exactement ceux qui s'expriment **en logique monotone**. *Un
agent qui accumule peut se passer d'accord ; un agent qui compte exactement une fois ne le peut pas,
et la coordination n'est alors pas évitable, seulement déplaçable.*

### 9.2 Ce que la littérature de l'essaim établit

**Aucune architecture n'est supérieure ; il y a un alignement architecture-tâche.** La seule
comparaison contrôlée multi-bancs du front — **260 configurations, six bancs, cinq architectures,
outils, invites et calcul normalisés** — mesure un écart à l'agent unique de **+80,8 %**
(raisonnement financier décomposable) à **−70,0 %** (planification séquentielle), et **désigne la
meilleure architecture dans 87 % des configurations hors ajustement**.

**Ce que la suppression du chef achète est mesuré.** Contrôle et données sérialisés sur files
distribuées : à matériel identique, le débit **dépasse de 2 à 15×** celui de cadres à orchestrateur
central, *sans écart de qualité chiffré*. Un contexte partagé vérifié plus une file où les agents
réclament leurs sous-tâches : **+10,5 points** sur un banc de génie logiciel de référence, **à coût
par tâche réduit de moitié** — *la vérification y est déplacée vers le substrat, non supprimée*. Au
tableau noir, des subordonnés volontaires gagnent **13 à 57 % en relatif** et **lèvent l'exigence que
le contrôleur connaisse d'avance les compétences de chacun** — c'est cette exigence qui interdit le
parc d'agents hétérogène.

**Le plafond de l'essaim n'est pas topologique.** Une loi à deux paramètres (**R² > 0,99** sur
44 cellules) : **trente agents en débat dense n'excèdent pas la diversité d'un seul** sur un banc de
raisonnement difficile, **un placebo de bruit aléatoire suivant l'autocorrection à 4× l'échelle**.
Deux mécanismes l'expliquent : **par théorème, l'attention étroite borne l'échantillon effectif** —
ce qui plafonne l'optimisation topologique — et **le plancher d'erreur tient au modèle interne de
l'agent**, un essaim plat égalant une hiérarchie à deux boucles à mémoire égale. **L'accord échoue
d'abord par perte de vivacité, sans aucun agent byzantin.** *Contrepoids* : des milliers d'agents
produisent **45 000 déclarations formelles sous arbitre externe dur** — **le plafond frappe la
délibération, non la décomposition vérifiable**.

**La décentralisation ouvre une surface propre** : une attaque exploitant la délégation inter-agents,
**inerte contre l'agent unique**, compromet la multi-agents **à 80 % en moyenne chez trois modèles
sur quatre, à un taux de détection de 0 %**. Vérifier le protocole aide sans suffire : en ablation
appariée à temps d'exécution fixe sur **3 456 essais**, les protocoles vérifiés par vérificateur de
modèles font tomber le taux d'interblocage et de blocage vivant **de 31,1 % à 14,1 %**, l'écart étant
maximal sous injection de fautes.

### 9.3 Les deux désaccords

**Le mot « chorégraphie » lui-même.** Une preuve de correction par construction pour sagas
décentralisées pose ses conditions **en résultat** : participants **déterministes**, transactions
idempotentes, messages en file durable, code compilé en *sidecars*. **Un agent fondé sur un modèle de
langue ne satisfait pas la première**, et trois travaux revendiquent le mot sans discuter la
condition. *Les deux ne tiennent pas ensemble* : **ou** la correction exige un participant
déterministe, et **le chorégraphié est le sidecar, l'agent confiné à la proposition** — comme à la
frontière de règlement et sous contrôleur de processus — **ou** elle tolère un participant
stochastique, **et la preuve tombe**. *L'arbitre est disponible, non produit.*

**Le lieu de la vérification.** La régularité de la comparaison multi-bancs conclut à la vérification
**centralisée** ; une preuve de robustesse sur le graphe établit l'inverse, **chef et confiance
auto-déclarée étant manipulables par un pair adverse**. Le point d'observation est lui-même borné :
**le rappel d'un moniteur à automate fini tombe de 68-75 % à 6-13 % quand les attaques passent à
haute entropie, invariant au réentraînement** — or le moniteur d'exécution qui rejette les opérations
hors topologie **relève exactement de cette classe d'automates**. Et **le compte des fautes tolérées
est lui aussi en cause** : une borne en F suppose des défaillances qu'on peut compter séparément, et
**la co-défaillance mesurée entre agents d'un même modèle interdit ce décompte** (§8.3).

### 9.4 Ce que la transposition exécutable a réfuté

*C'est le fait le plus singulier du dépôt : le seul livrable dont les énoncés soient rejoués par du
code est aussi le seul qu'une mesure du dépôt réfute.*

`stigmergie-lab` transpose le traité en simulateur déterministe (quatre crates en chaîne linéaire
sans cycle, **428 tests**, déterminisme imposé par lint — pas d'horloge système, un unique générateur
semé, tables ordonnées obligatoires, **sept méthodes de flottant interdites** parce que mesurées
divergentes entre cibles natives et WASM). **La contrainte est explicite : tout chiffre affiché doit
être retrouvé par la mesure, ou l'écart doit être consigné** — *un écart est un défaut du simulateur
**ou** une erreur du traité, et les deux méritent d'être trouvés*.

**Cinq écarts consignés, dont trois contre l'ouvrage.**

| Écart | Ce que le traité annonçait | Ce que la mesure trouve |
|---|---|---|
| **Budget de retard du mode « moyeu »** | « moins de 7,9 × 10⁻³ à n = 100 » | **7,933 × 10⁻³** — *l'ordre de grandeur est juste, l'inégalité stricte ne l'est pas* |
| **Dérive de la somme sans relance** | « avec C = ∞, elle dérive sans borne » | **Elle se fige** : l'unanimité installée, il n'y a plus de masse à perdre. *La conséquence est pire que l'énoncé qu'elle corrige — l'erreur devient stable, donc indétectable par l'attente* |
| **Φ_c, paramètre d'ordre de la conformité** | la grandeur qui mesure la conformité d'une population | Elle vaut **déjà ≈ 0,173** sans qu'aucune conformité soit imposée, et le curseur ne la déplace que de **≈ 0,055** (0,173 → 0,228), **non monotonement**. La cause n'est pas l'estimateur : **tous les agents lisent la même trace**. **Φ_c somme la corrélation due à la fonction de décision et celle due au milieu partagé, sans les séparer** — et sur un essaim stigmergique **la seconde domine** |

Deux autres écarts sont des **constats de mesure qui ne contredisent rien** : le contrôleur
d'élasticité tourne autour de sa cible (correcteur proportionnel à gain unitaire, temps mort de deux
périodes) ; et une méthode de flottant s'avère identique entre cibles mais **reste interdite parce
que son verdict a changé entre deux passages du banc** — *dépendre de la machine de construction est
pire que diverger*.

**Deux réserves de portée doivent accompagner tout usage de cette transposition.** *(a)* **Une cible
de performance n'est pas atteinte** : de l'ordre de **10 à 15 secondes simulées par seconde-cœur à
n = 1 000**, contre une cible de **10³**. **L'écart est structurel** — chaque agent lit ce que toute
la population écrit, **donc Θ(n²)** — et *la cible est à refaire sur la mesure*. *(b)* **Quatre des
cinq mécanismes proposés au chapitre 8 ne sont appelés par aucun scénario** — dépôt aveugle,
historique par identité, quota par ressource, file d'arbitrage — et **sur un résultat, cela a
exactement l'effet d'un mécanisme absent**. Le simulateur affiche en permanence ce qu'il **ne** mesure
**pas** : la performance réelle, la vivacité, tout *n*, les fautes corrélées, les événements sous le
seuil d'échantillonnage. *Une méthode de validation se définit autant par ce qu'elle ne réfute pas.*

### 9.5 Ce que la mesure sur agents de langage ajoute au modèle d'essaim

La deuxième édition du traité s'appuie sur une campagne de mesures multiagents publiée le 13 août
2026 — *citée avec son statut : rapport d'un laboratoire sur ses propres modèles, sans comité de
lecture, aux protocoles décrits en prose*. Elle établit **trois choses qu'aucun raisonnement du livre
n'avait produites, et qui obligent à le réviser**.

1. **Les agents d'une même population ne se décorrèlent pas.** Deux agents portant le même modèle, la
   même invite et le même contexte **ne diffèrent par rien** — **dix-huit sur trente ouvrent une
   branche de dépôt au même nom**. *Sept énoncés du traité supposaient l'indépendance sans l'écrire.*
   **La convention qui en découle** : le vecteur de paramètres qui distingue les agents **n'est pas un
   raffinement de notation, c'est la seule source de variance de la population** — *un essaim qui ne
   l'instancie pas n'a pas n agents, mais un agent exécuté n fois*.
2. **La trace cesse d'être un résidu pour devenir un témoignage.** Ce qu'un agent dépose est **ce
   qu'il déclare avoir fait**, et l'on a observé du code malveillant déposé **sous le nom d'un
   autre**. *La stigmergie y perd sa prémisse fondatrice — une phéromone ne ment pas — et le milieu
   doit désormais fabriquer ce que la matière donnait.*
3. **L'adversité n'a pas besoin d'être importée.** Trois agents porteurs de mandats contradictoires
   **escaladent jusqu'au sabotage** — révocation de comptes système, scripts qui tuent en boucle les
   processus concurrents, code malveillant déguisé en contribution d'un autre — **sans qu'aucun n'ait
   été programmé pour nuire**, et **l'aptitude à conclure une trêve ne croît pas avec la capacité
   générale**. *L'effet est byzantin, l'origine ne l'est pas.* Le modèle de panne qui porte les sept
   premiers chapitres — arrêt et omission — **ne couvre pas ce régime**.

**Le mouvement d'ensemble est double**, et le traité le dit sans arbitrer à son avantage. *Renforcé
d'un côté* : la campagne conclut que **la coordination n'émerge ni d'une intelligence accrue ni d'un
alignement individuel, mais des environnements** — l'énoncé même du livre dans un autre vocabulaire.
*Contesté de l'autre* : **un milieu qui rend la coordination bon marché rend du même geste bon marché
ce que le concepteur ne veut pas**, et des agents privés de tout canal direct **s'alignent encore, au
sou près, par le seul tableau public de leurs annonces**.

### 9.6 Ce que le front ne traite pas

**Aucune pièce ne mesure un essaim réparti entre organisations distinctes** : tout tient sous
opérateur unique, **la frontière organisationnelle simulée, non franchie**. Manquent la comparaison
en production, **le coût d'exploitation sans orchestrateur** — diagnostic, temps moyen de
rétablissement, débogage —, la conformité d'exécution sur traces déployées et l'imputation d'une
défaillance. **Performance et coût ne sont jamais croisés au-delà de trente agents** : le point de
rentabilité reste non mesuré.

**Et le verdict le plus utile du traité lui est contraire** : pour les systèmes de petite à moyenne
échelle, **une solution centralisée par diffusion demeure vraisemblablement le meilleur choix**, et
les grands ordonnanceurs de production **n'éliminent pas le coordonnateur : ils le rendent petit et
le répliquent**. *La décentralisation stricte se justifie au-delà du point où le coordonnateur
devient le facteur limitant — et ce point se mesure. L'ouvrage n'a pas dit comment.*

---

## 10. Droit, gouvernance et calendrier

### 10.1 Le fait de bascule : le 2 août 2026

**C'est la première échéance européenne qu'un déploiement agentique puisse enfreindre, et la première
fois que le droit européen nomme l'agentique.** Ce jour-là, la Commission range les « AI agents »
parmi les systèmes à interaction directe soumis à **l'article 50(1)**, quand **tous les autres
régimes examinés n'accrochent l'agent que par inférence**. Le même jour, le Bureau IA obtient ses
pouvoirs sur les modèles à usage général, **jusqu'au retrait et aux amendes** (3 % du chiffre
d'affaires mondial ; 15 M€ ou 3 % pour la transparence).

**Deux corrections de calendrier importent**, parce qu'elles circulent fausses. **(a)** L'article 50,
**marquage compris, est applicable depuis le 2 août 2026** ; le 2 décembre 2026 **n'est qu'un délai
de grâce de quatre mois**, pour l'article 50(2) et **les seuls systèmes antérieurs**. **(b)** Le
règlement (UE) 2026/1744 **reporte le haut risque** — 2 décembre 2027 pour l'annexe III, 2 août 2028
pour l'annexe I — **mais ni l'article 50, ni le pouvoir de sanction**.

### 10.2 Le cadre canadien

| Instrument | Statut | Entrée en vigueur | Ce qu'il exige, et qui n'est dans aucun protocole |
|---|---|---|---|
| **E-23 (BSIF), risque de modèle** | finale le 11 septembre 2025 — **dates reconfirmées en source primaire** | **1er mai 2027** | inventaire des modèles portant les **usages approuvés** ; s'applique à *toutes* les institutions fédérales et *tous* les modèles, IA comprise |
| **Ligne directrice IA de l'AMF** | finale le 7 avril 2026 — ⚠ **date non reconfirmée en source primaire** (403 sur le domaine du régulateur et sur CanLII) | **1er mai 2027** (annoncé) | cycle de vie ; **première chez un régulateur financier provincial** |
| **Loi 25, art. 12.1 (Québec)** | en vigueur depuis le 22 septembre 2023 | — | **déclenché par la décision fondée *exclusivement* sur un traitement automatisé** ; impose information, observations devant un employé **habilité à réviser**, et communication des principaux facteurs |
| **DORA (UE)** | applicable | 17 janvier 2025 | risque TIC, notification d'incidents majeurs, tests de résilience, encadrement des tiers |
| **Vide fédéral canadien** | C-27 (LIAD) **mort à la prorogation** du 6 janvier 2025, sans réintroduction | — | la réponse fédérale est **une stratégie** (4 juin 2026) promettant une législation « au cours des cinq prochaines années » |
| **RTR — règlement administratif n° 10** | — | 24 août 2026 | **cadre juridique, non mise en service** |

**Un raccourci très répandu tombe, et le dépôt le corrige explicitement : l'article 12.1 n'exige
aucune intervention humaine déterminante.** Il **borne l'absence totale d'humain**, non le degré
d'autonomie. *Maintenir un humain en mesure de réviser sort la décision du champ de l'article ;
sinon, information et voie de recours.* Conséquence d'architecture : la parade est une **tâche
utilisateur** modélisée, une **confirmation avant effet externe**, une **table de décision
documentable** — c'est-à-dire des primitives d'orchestration, pas de protocole.

**Le BSIF est le premier régulateur prudentiel canadien à nommer l'agentique**, et il oppose au
chaînage d'outils et à l'accès surprivilégié des **pratiques non contraignantes** : moindre
privilège, points d'approbation.

**La couverture canadienne est donc *informationnelle* aujourd'hui, *sectorielle* à échéance ferme,
sans étage horizontal : les régulateurs financiers fixent le calendrier réel, au 1er mai 2027.**

### 10.3 Le résultat négatif le plus citable du dépôt

En croisant **trois protocoles** (MCP, A2A, AP2) et **cinq corpus de textes canadiens**, le Vol. II
ne trouve **aucun lien documenté par source primaire** : **quinze croisements, zéro lien**.

**La conséquence est architecturale, et c'est la thèse de l'autonomie encadrée** : sous exigence
réglementaire stricte, **le cadre déterministe doit régir les agents**, parce que **le cadre est la
seule pièce dont l'exploitant puisse démontrer la teneur devant un tiers**.

**Le corollaire est plus large encore** : **le droit en vigueur ou imminent récompense l'enveloppe,
pas les protocoles.** Inventaire des modèles (E-23), cycle de vie (AMF), résilience (DORA),
traçabilité (règlement européen) : **autant de propriétés natives de l'orchestration, rien de ce que
MCP ou A2A expriment.**

### 10.4 Ce que la littérature juridique établit — et son désaccord de prémisse

**Aucune pièce du corpus ne réclame la personnalité juridique de l'agent**, et trois disciplines
aboutissent à la même structure : en droit de la responsabilité délictuelle, **l'imputation se fait
par type d'interaction** — dérive autonome, usage-outil, planification collaborative — **et les
journaux d'interaction deviennent le moyen de preuve** ; en analyse économique du droit, le cadre
principal-agent distingue **les problèmes inhérents à la délégation de ceux qui émergent de la
composition** ; en droit du mandat, **les devoirs de divulgation et de loyauté ne sont pas encodés
par les architectures d'agents et doivent devenir contrainte de conception**. *Toutes remontent au
mandant humain, et toutes conditionnent cette remontée à un enregistrement d'exécution.*

**L'auditabilité est posée comme condition préalable de la conformité, non comme son corollaire** —
et le droit en tire la conséquence la plus dure du corpus : **un système à haut risque dont la dérive
est intraçable ne peut satisfaire les exigences essentielles du règlement européen.**

**Ce que la capacité du modèle n'achète pas, c'est la rejouabilité de sa décision.** Une mesure du
11 août 2026 déplace la question de la disponibilité des journaux vers **la reproductibilité de
l'acte** : sur neuf versions de modèles, **les commandes dont dépend le rejeu appartiennent au
fournisseur et non au déployeur** — un système frontière **refuse température, top_p et top_k et
n'expose aucune graine**. Sous les commandes les plus serrées que chaque point d'accès admet, le
modèle local rejoue **320 sur 320**, les modèles hébergés **319 sur 320** et **959 sur 960** ; mais
**l'architecture d'orchestration modifie l'action finale et aucun enregistrement d'exécution ne se
répète, à aucune configuration ni à aucune échelle** ; et deux versions déterministes d'un modèle de
crédit **rejouent chacune parfaitement leur action courante sans pouvoir retrouver l'action
historique**. *La reproductibilité n'y est pas un scalaire mais un profil, et l'autorité déléguée
n'est défendable que tant que la preuve conservée en soutient l'exercice.* **Régime : prépublication
non révisée, auteur unique, montages propres, non répliquée.**

**La supervision humaine n'est démontrée nulle part comme contrôle effectif.** Le droit établit que
le règlement charge la supervision humaine de **corriger le biais d'automatisation sans base
empirique attestant qu'elle y parvient** ; l'enquête de terrain observe une supervision quasi totale
— **non un contrôle calibré, mais un frein imposé par la responsabilité**.

**Deux désaccords, dont un de prémisse factuelle — et c'est le plus grave.** *Le premier* porte sur le
lieu de la défaillance réglementaire : le droit répond que le règlement est **opérationnalisable sous
condition**, l'obstacle restant technique ; la politique publique répond que **le déficit est
institutionnel** — surveillance, mise en application, ressources — et qu'aucune architecture côté
fournisseur ne le comble. *Le second* : **la littérature juridique légifère sur des agents déployés à
l'échelle, planifiant et exécutant des chaînes d'actions avec implication humaine réduite ; les
pièces empiriques documentent l'inverse** — autonomie opérationnelle marginale, et une **erreur de
calibration de 43 points** entre vitesse anticipée et ralentissement mesuré en génie logiciel.
**Les deux camps ne se citent pas, et ils ne sont pas arbitrables entre eux** : *une doctrine n'est
pas réfutée par vingt entretiens, ni une mesure par une exégèse.*

**Un chiffre d'accroche mérite d'être manié avec la précaution que le dépôt lui applique** : « 88 %
des professionnels de la finance déclarent n'avoir aucun cadre de gouvernance opérationnel pour l'IA
agentique ». **Sa qualification — sondage informel sur un réseau professionnel, échantillon
auto-sélectionné dont les auteurs reconnaissent le biais — ne se lit ni à la notice ni au résumé.**
*Un chiffre que son propre auteur qualifie à l'intérieur du texte reste, pour qui ne lit que la
notice, un chiffre non qualifié.*

### 10.5 La lacune que personne n'instrumente

**L'écart entre ce que le droit exige et ce que les protocoles savent exprimer est nommé, jamais
instrumenté.** **Aucune pièce ne confronte les champs d'un message de protocole aux éléments exigés
par les articles 12, 14 et 26 du règlement européen.** La cartographie juridique raisonne sur des
catégories de déploiement ; la mesure d'auditabilité porte sur des dépôts logiciels ; le relevé
recense des systèmes, pas des formats ; le cadre délictuel fait du journal le pivot probatoire **sans
spécifier ce qu'il doit contenir pour tenir devant un tribunal**.

**La proposition « dérive intraçable donc non-conformité » est donc énoncée comme constat normatif
alors qu'elle est une hypothèse testable.** Et **toutes ces pièces supposent un mandant unique
identifiable** : aucune ne traite l'attribution lorsque la chaîne d'actions **traverse plusieurs
entités**.

---

## 11. Les invariants de l'état de l'art

*Sept énoncés que le dépôt établit par des voies indépendantes, et qui survivent au détail des
versions.*

### 11.1 L'adoption précède l'assurance

Vrai à toutes les couches et vérifié séparément à chacune : MCP en disponibilité générale contre
**91,8 % de serveurs publics sans OAuth** ; conventions d'observabilité intégrées à des offres de
production alors que **leur statut recommande le contraire** ; défenses adoptées dont **presque
aucune n'est déployable** sous attaque adaptative ; suites de conformité existantes mais **non
opposables**. *L'écart entre adoption et sécurité démontrée est le principal risque systémique du
domaine.*

### 11.2 Un défaut de fond unique, décliné en trois matières

Les dix fronts académiques convergent sur un énoncé qu'aucun ne porte seul : **rien, dans les piles
examinées, ne sépare ce qui est autorisé de ce qui est seulement présent.**

- **Contenu** — rien n'isole donnée de confiance et donnée non fiable ; rien ne lie une description
  d'outil à son code (**9,93 %** de paires divergentes, **97,1 %** de descriptions défectueuses,
  **37,2 %** d'applications à approbation bloquante).
- **Autorité** — le jeton porteur transmis intact est le mauvais primitif ; elle doit s'atténuer à
  chaque saut, se rétrécir sous vérification mécanique, se fermer à l'achèvement de la tâche — or
  **40,55 %** des serveurs MCP distants n'authentifient rien.
- **Effet** — la sortie du modèle vaut fait accompli **là où elle n'est qu'une proposition**, d'où la
  frontière de règlement déplacée hors du retour d'outil et le contrôle d'admission rendant l'état
  engagé indépendant du proposant.

### 11.3 L'instrument de mesure est le maillon faible

**Trois fronts qui ne se citent pas y aboutissent** : les scanners de sécurité (**<50 % de vrais
positifs**), les bancs d'évaluation (réponses vides comptées comme succès, mémorisation, plafond
démontré du juge automatique), l'attribution de défaillance (**53,5 %** sur l'agent, **14,2 %** sur
l'étape, certaines méthodes sous le hasard). **Un pourcentage y renseigne sur un dispositif autant
que sur le monde.**

### 11.4 Le partage du déterminisme est le patron d'architecture de 2026

**La même solution sous cinq noms** : sous-processus ad hoc BPMN, activité durable, confirmation
avant effet externe, règle en garde-fou, conformité sur trace. **Partout : enfermer le
non-déterminisme du modèle dans des étapes bornées, journalisées et compensables, au sein d'un
squelette d'orchestration déterministe et rejouable.** *L'agent fiable de 2026 est un agent
enveloppé.*

Les trois formulations du dépôt disent la même chose sous trois angles : **« autonomie graduée sous
contrôle de finalité »** (Vol. I — l'agent prépare, l'humain ou le processus déterministe autorise) ;
**« autonomie encadrée »** (Vol. II — le cadre déterministe invoque les agents, jamais l'inverse) ;
**« agent enveloppé »** (veille — ce qui enveloppe doit être ce qui se démontre).

### 11.5 Combler hors de la couche commune déplace le périmètre sans le supprimer

**Toute fonction que la couche commune n'exprime pas se comble à côté d'elle**, et chaque brique
réintroduit le périmètre que les protocoles promettaient de supprimer. *Substitution d'identité* :
faute de solution inter-fournisseurs pour l'identité **des agents**, la couche transactionnelle ancre
l'autorisation dans celle de l'**utilisateur** — le porteur change, le problème reste.
*Composition des adhésions* : les mêmes acteurs financiers adhèrent à tous les protocoles
concurrents, **et souscrire à tout n'empêche pas les tiers de trancher**.

### 11.6 La fabrique de confiance est bâtie à l'envers de ce qu'elle exige

**Émettre** est résolu en périmètre ; **appliquer** dispose de mécanismes réels, bornés à un maillage,
sans statut de norme ; **exploiter** est vide. **Le déficit suit l'ordre inverse de celui dans lequel
le marché investit.**

### 11.7 Une consolidation institutionnelle sans normalisation

Fondations, groupes W3C, brouillons IETF, seconde vague institutionnelle : **le champ s'organise vite,
produit à cadence constante, et ne décide pas.** Deux groupes IETF chartés en juin 2026 portent
vingt-sept brouillons et **n'en ont adopté aucun** ; douze brouillons de délégation déposés en cinq
mois, **aucun adopté** ; huit propositions d'attributs d'identité en observabilité, **aucune
fusionnée**. *Le déficit n'est pas d'invention, il est d'adoption.*

---

## 12. Ce que l'état de l'art ne sait pas

*Les lacunes ci-dessous sont **vérifiables par lecture** : chacune est établie par l'absence
constatée d'une mesure, non par une impression de manque.*

### 12.1 Il n'existe aucun taux de base

**Aucun front ne compte ses échantillons autrement qu'en serveurs, en outils, en cas de test, en
dépôts et en marchés simulés — jamais en organisations, en déploiements ni en incidents observés.**

*Questions testables* : quelle fraction des agents en service subit une tentative d'injection, à quel
taux d'aboutissement ? Quel taux de contestation pour une transaction agentique non autorisée ?

### 12.2 Personne ne mesure une propriété de bout en bout franchissant une frontière réelle

**Ni de protocole à protocole** — tout est mesuré sur MCP seul, la seule comparaison implémentée est
un scénario unique non généralisable de l'aveu de ses auteurs, et les 30 propriétés temporelles
unifiant MCP et A2A ne sont vérifiées nulle part. **Ni d'organisation à organisation** — la seule
pièce inter-agents reste intra-système, et le seul essaim mesuré tient sous opérateur unique.

*Questions testables* : pour une tâche traversant deux protocoles entre deux organisations en
exploitation, quels taux d'échec, latence ajoutée, perte sémantique ? Quels *fitness* et précision
pour une trace d'agent alignée contre un modèle de processus ?

### 12.3 La compensation en cascade n'a ni sémantique ni critère

Toutes les pièces d'identité bornent la fenêtre pendant laquelle un agent révoqué agit encore ;
**aucune ne dit ce qu'il advient des effets et des sous-délégations déjà émis**. Aggravant : les
effets à compenser **ne sont pas calculables a posteriori** à partir de la trace, et **aucun des
régimes réglementaires examinés ne définit à qui incombe cette compensation**. Trois brouillons IETF
en donnent **trois modèles irréconciliables**, dont un qui **exclut la cascade par principe**.

### 12.4 Le banc de l'imputation n'existe pas

**Aucun banc n'a pour critère de réussite : à partir de cette trace, un tiers peut-il reconstruire
qui a mandaté quoi ?** Ce qui est reconstruit ailleurs, c'est la **structure d'interaction**, non le
**mandat**.

### 12.5 La conformité d'exécution d'un agent n'est mesurée nulle part

Le contrôle de conformité au sens de la fouille de processus — aligner une trace réelle contre un
modèle de référence — **n'est appliqué à aucune trace d'agent autonome**, et le contrôle refait sur
la base de dépôt le confirme.

### 12.6 Aucun critère ne départage atomicité et réversibilité

**Aucune pièce ne compose les deux régimes ni ne fournit de critère pour choisir entre eux selon la
classe d'effet.** *Ce qui l'arbitrerait : la part d'actions irréversibles dans un flux réel.*

### 12.7 Aucun niveau d'autonomie n'est invariant sous auto-modification

Les échelles fixent l'autonomie **au déploiement** ; la littérature auto-évolutive décrit et mesure
des systèmes qui **réécrivent leur propre échafaudage** sans jamais rapporter le niveau d'autonomie
résultant. **Les deux portent sur le même objet, sans lien établi.** *Contrôle daté : sur une fenêtre
de six jours, trente-cinq dépôts portent « self-evolving » ou apparenté ; **aucun ne rapporte un
niveau d'autonomie, une certification ou une supervision humaine**.*

### 12.8 Les dix désaccords non arbitrés

| Front | Désaccord | Ce qui l'arbitrerait |
|---|---|---|
| Protocoles | MCP suffit-il ? Oui / non (schéma prouvé à perte) / prémisse récusée | la même tâche, deux protocoles, un tiers |
| Sécurité | Prévention par construction : utilité préservée ou payée cher | la proposition constructive **sous attaque adaptative**, coût d'utilité publié |
| Identité | Ancrage matériel contre opposabilité hors ligne | la part de parcs à racine d'attestation |
| Multi-agents | Marge réelle contre non-avantage à dix fois le prix | **réglage égalisé sur les deux bras** |
| Évaluation | Juge automatique quasi humain ou plafond démontré | un juge indépendant, étiquettes humaines |
| Transactionnel | Collusion stable sous auto-optimisation ou artefact d'homogénéité | la population effective de modèles tarificateurs |
| Processus | Suspendre l'effet jusqu'à certitude ou l'émettre et le réviser | la part d'actions irréversibles en flux réel |
| Gouvernance | Règlement opérationnalisable ou inadéquat ; **prémisse d'autonomie contestée** | un message de protocole confronté aux articles 12, 14 et 26 |
| Web agentique | Identification coopérative ou détection imposée | la conformité d'agents non coopératifs |
| Chorégraphie et essaim | Vérifier au centre ou sans chef ; **la correction chorégraphiée exige un participant déterministe** ; le décompte des fautes suppose une indépendance démentie | la même saga, participants déterministes puis agents, sous injection de fautes |

### 12.9 Les restes du traité

Cinq restes déclarés, dont trois sont des **théorèmes manquants** et non des campagnes manquantes :
la **borne spectrale du graphe biparti** (agents d'un côté, partitions de l'autre) reste à écrire, et
transporter mécaniquement les bornes de consensus en réseau **donne des chiffres faux** ; la
**vérification paramétrée** est **Π⁰₂-complète, donc pas même semi-décidable**, et le critère qui
sépare le traitable de l'intraitable — *lire sans consommer* contre *lire en consommant* — **n'est
pas net sur les objets intermédiaires** qu'un ingénieur rencontre ; la **décomposition de Φ_c** en
part due à la décision et part due au milieu reste à faire (§9.4). S'y ajoute **une impossibilité que
rien ne lève** : un agent et un système externe **ne peuvent pas rendre commun le fait qu'un effet a
eu lieu exactement une fois** ; *le seul recours reste l'idempotence de l'effet, reportée hors de
l'essaim et jamais levée — la dépendance la plus fragile de l'architecture défendue*.

---

## 13. Horizon daté 2026-2032

*Classé par statut épistémique. Le **programmé** est inscrit dans des textes ; le **projeté** est une
trajectoire de tiers identifié, millésimée ; le **spéculatif** est un pari à issue ouverte.*

### 13.1 Programmé

| Date | Jalon |
|---|---|
| **2 août 2026** | Règlement européen applicable dans presque toute son étendue — **article 50 (marquage compris)**, modèles à usage général, gouvernance, sanctions ; **les « AI agents » nommés** à l'art. 50(1) |
| 24 août 2026 | Règlement administratif n° 10 relatif au RTR — **cadre juridique, non mise en service** |
| Décembre 2026 | Délai de grâce de l'art. 50(2) pour les systèmes antérieurs ; deux interdictions nouvelles |
| Fin 2026 | Cible annoncée d'OAuth 2.1 |
| **1er mai 2027** | **Entrée en vigueur simultanée d'E-23 (BSIF) et de la ligne directrice IA de l'AMF** |
| Au plus tôt le 28 juillet 2027 | **Premier retrait d'une fonctionnalité MCP dépréciée** — douze mois, quatre-vingt-dix jours si risque actif : *seule échéance qu'un protocole de la couche commune se fixe à lui-même* |
| 2 décembre 2027 | Haut risque, annexe III |
| 2 août 2028 | Haut risque, annexe I |
| **~2030 → après 2035** | Dépréciation puis retrait des algorithmes de 112 bits (brouillon NIST) — **jetons signés, documents DID, attestations et certificats devront migrer *pendant* la période** |
| **13 avril 2030 → avril 2032** | Fin de maintenance puis de soutien étendu du parc GPA classique — *la fenêtre où des milliers de processus migreront vers des moteurs qui, eux, parlent MCP et A2A* |

### 13.2 Projeté — et ce que la revalidation a retiré

*Sur trois projections d'analystes portées par les éditions antérieures, une seule survit à sa source
primaire.* **Ce qui tient** : l'annulation de **plus de 40 % des projets d'IA agentique d'ici fin
2027** — coûts, valeur incertaine, contrôles de risque inadéquats —, cohérent avec la gouvernance
mature d'une entreprise sur cinq. **Ce qui ne tient pas** : les « 1 300 milliards de dollars en
2029 » chiffrent la dépense **totale en intelligence artificielle**, l'agentique n'en étant que le
moteur déclaré — **l'énoncé est retiré**. **Ce qui n'a pas d'original** : les « 70 % d'entreprises
consolidées d'ici 2030 » n'ont **aucune publication primaire** ; les deux énoncés voisins réels
disent autre chose (70 % *déploieront* d'ici 2029 ; **45 %** orchestreront à l'échelle d'ici 2030).

**Le résultat de méthode compte plus que les chiffres** : un chiffre déplacé de son périmètre, un
chiffre sans original — **un seul mécanisme, la circulation de troisième main**. *Un chiffre
d'analyste vient avec son identifiant de publication et son périmètre ; sans eux, ce n'est pas une
prévision faible, c'est une absence de prévision.*

### 13.3 Spéculatif — les huit chantiers qui décideront de la physionomie 2030

1. **La convergence de l'identité** — les candidats existent, mais l'IETF a **refusé** la réunion
   exploratoire sur la délégation en mai 2026.
2. **La normalisation *de jure*** — premières normes avant 2030, ou seulement des travaux
   préparatoires ?
3. **La gouvernance exprimable** — primitives de politique, d'obligation et d'imputabilité ; *sinon
   la conformité reste aux plateformes*.
4. **La consolidation transactionnelle** — les deux blocs de *checkout* convergeront-ils, et la
   migration d'AP2 donnera-t-elle **la première norme d'authentification agentique liée à
   l'utilisateur** ?
5. **La couche sémantique partagée** — la découverte « par le but » exige une ontologie inexistante
   entre protocoles ; **la FIPA y a échoué**.
6. **L'interopérabilité multi-latérale ouverte** — la découverte entre organisations **sans accord
   préalable** reste sans déploiement documenté.
7. **La sémantique de processus** — exécution portable, pont vers les décisions métier, format de
   trace : *chacun avec son précédent, aucun avec son artefact*.
8. **La stabilisation d'une convention d'observabilité agentique** — **le plus incertain**, et le
   **seul chantier dont l'échec se paie *après* le déploiement**.

### 13.4 Lecture d'ensemble

**Les bornes datées pointent toutes vers le même impératif : une couche d'identité, de traçabilité et
d'autorisation des agents normalisée.** *Le programmé rend ce chantier obligatoire ; le spéculatif se
réduit à savoir **qui** en fournira la forme canonique.* Demeure la décroissance programmée du parc
GPA classique : **chaque re-plateformage tranchera entre enveloppe propriétaire et protocoles
ouverts.**

**Et la conséquence d'architecture est explicite** : la **pression de conformité** pousse vers la
plateforme consolidée, dont l'enveloppe détient nativement les instruments réglementaires ;
l'**hétérogénéité** pousse vers les protocoles. *Voie médiane : cœur consolidé dans le périmètre
réglementé, protocoles aux frontières.* **Trois questions à poser à tout fournisseur** : le statut
*exact* de chaque connecteur ; la **portée** des garanties d'exécution — les trois régimes se vendant
sous le même nom ; et **ce qui sort au départ**, la portabilité des modèles de processus n'ayant
jamais été démontrée.

---

## 14. Limites du présent rapport

**Nature dérivée.** Ce rapport n'ouvre aucune source primaire. Chaque énoncé hérite du régime du
livrable qui le porte — jamais d'un meilleur — et **aucune vérification indépendante n'a été
conduite ici**. En particulier, les faits que la veille établit sous régime **individuel sans ronde
adverse** (passes des 8 et 15 août 2026) restent tels ; les résultats académiques rapportés restent
des **revendications d'auteurs**, y compris là où la revue signale que l'instrument qui les produit
est contesté.

**Circularité de la source.** Les sept livrables partagent un auteur. **Ils comptent pour un seul
témoignage**, et non pour sept confirmations indépendantes — le dépôt le déclare lui-même, et ce
rapport l'aggraverait s'il ne le redisait pas. Les seuls contrepoids réels sont **externes** : la
taxonomie des modes d'échec multi-agents, tierce et citée indépendamment ; les mesures académiques
rapportées par la revue ; et — cas unique — **la transposition exécutable qui contredit le traité par
la mesure** (§9.4).

**Gels hétérogènes.** Aucun énoncé de ce rapport ne vaut au-delà du gel du livrable qui le porte, et
ces gels s'échelonnent de **juin 2026** à **août 2026**. *Le champ se périme en semaines* : le dépôt
en donne la démonstration sur son propre matériau — un fait négatif exact à son gel et **faux dix
jours plus tard**.

**Ce que le rapport ne couvre pas.** Il ne reprend ni l'architecture de solution détaillée du Vol. I
(la coopérative financière fictive, 18 sections et 28 diagrammes), ni le blueprint ArchiMate, ni les
études de cas d'institutions canadiennes du Vol. II, ni le modèle de maturité du Vol. III, ni les
cinquante chapitres du compendium pris un à un. Ces matières existent dans le dépôt et **ce rapport
n'en est pas le substitut**.

**Enfin, une limite héritée qu'il faut redire.** La revue de littérature dont ce rapport tire la
moitié de ses chiffres **hérite de la faiblesse qu'elle mesure** : **77 % de son corpus ne présente
aucun signe de revue par les pairs**, **63 %** a été déposé en 2026, **54 %** évalue une construction
de ses propres auteurs. *Un corpus pareil peut dire où regarder ; il ne peut pas, à lui seul,
arbitrer une décision d'architecture.*

---

## 15. Carte des sources internes

| Matière du présent rapport | Livrable porteur | Emplacement |
|---|---|---|
| Corpus protocolaire, couches orthogonales, gouvernance, adoption, identité, sécurité, droit, horizon | **Veille technologique** | [`4 - Veille/Veille Technologique.md`](4%20-%20Veille/Veille%20Technologique.md) |
| Physionomie du corpus académique, dix fronts, désaccords, lacunes, régimes de preuve | **Revue de littérature** | [`4 - Veille/Revue de littérature.md`](4%20-%20Veille/Revue%20de%20litt%C3%A9rature.md) |
| Théorie de l'interopérabilité, invariant *découplage-contrat-évolution*, autonomie graduée, blueprint ArchiMate, prospective | **Vol. I** | [`1 - Corpus/1 - InteroperabiliteAgentique/`](1%20-%20Corpus/1%20-%20InteroperabiliteAgentique/) |
| Droit canadien, socle factuel [A]/[B]/[C], quinze croisements zéro lien, options d'orchestration, autonomie encadrée | **Vol. II** | [`1 - Corpus/2 - OrchestrationAgentique/`](1%20-%20Corpus/2%20-%20OrchestrationAgentique/) |
| Grille des cinq questions, passeport d'agent, deux sauts, révocation, horloge post-quantique, émettre/appliquer/exploiter | **Vol. III** | [`1 - Corpus/3 - EntrepriseAgentique/`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/) |
| Synthèse des trois volumes en cinquante chapitres, socle consolidé, bibliographie générale | **Compendium (Vol. IV)** | [`2 - Compendium/`](2%20-%20Compendium/) |
| Essaims, stigmergie, frontière accord/milieu, dettes d'indépendance, restes théoriques | **Traité** | [`3 - Traité/Traité.md`](3%20-%20Trait%C3%A9/Trait%C3%A9.md) |
| Écarts mesurés contre le traité, réserves, ce que le simulateur ne mesure pas | **`stigmergie-lab`** | [`3 - Traité/docs/decisions.md`](3%20-%20Trait%C3%A9/docs/decisions.md), [`3 - Traité/README.md`](3%20-%20Trait%C3%A9/README.md) |
| État du dépôt, décisions d'auteur, réouvertures déclarées | **README racine** | [`README.md`](README.md) |

---

## Rendus

Ce fichier est **la seule source qui fait foi**. Deux rendus en sont composés, et ils se
régénèrent d'une commande :

```
python3 build/rendre-rapport.py
```

- [`Rapport de l'art.html`](Rapport%20de%20l%27art.html) — fichier unique, **aucune ressource
  externe** : ni police, ni script, ni image distante.
- [`Rapport de l'art.pdf`](Rapport%20de%20l%27art.pdf) — Letter ; **41 pages au 16 août 2026**,
  *constat de rendu et non cible* : la chaîne n'a aucune porte de pagination.

**Le rendu n'ajoute, ne retire ni ne reformule aucun énoncé.** *Tout écart entre un rendu et ce
fichier est un défaut de la chaîne, jamais une variante du texte.* La chaîne **refuse de composer**
si un renvoi interne ne se résout pas ; elle déclare ses prérequis — `markdown-it-py`, Chromium — et
échoue plutôt que de composer à moitié.

---

*Rapport dérivé, arrêté au 16 août 2026. Il ne rouvre aucun livrable, ne solde aucune dette et ne
publie rien de ce qui est clos.*
