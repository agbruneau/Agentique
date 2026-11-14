# Chapitre 7 — Protocoles périphériques

*Question directrice : quels besoins MCP et A2A ne couvrent-ils pas ?*

> **État de référence :** documentation d'AG-UI, d'ANP (jeu de spécifications 1.2) et d'AGNTCY telle que publiée à cette date; brouillon IETF `draft-mpsb-agntcy-slim-03` du 2 novembre 2026; prépublications arXiv dans leur dernière version. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre, sauf [22].

MCP relie un agent à ses outils (chapitre 5). A2A relie un agent à un autre agent (chapitre 6). Quatre besoins au moins restent à découvert : tenir une interface à jour pendant qu'un agent travaille, identifier et trouver un agent sans autorité centrale, faire circuler des messages chiffrés entre plus de deux parties, piloter une ressource physique. Chacun a suscité son protocole.

La thèse de ce chapitre tient en deux constats. Aucun de ces protocoles n'a les garanties de stabilité de MCP ou d'A2A, et un seul, AGNTCY, relève d'une fondation, où l'empreinte de son fondateur reste forte. Et presque tous se présentent comme des compléments : ils enveloppent MCP et A2A, ou s'y adossent, au lieu de les remplacer. Ils s'adoptent donc besoin par besoin, derrière un adaptateur, et jamais comme fondation.

---

## 7.1 AG-UI : la couche agent-utilisateur

### Le besoin

Un agent qui travaille plusieurs minutes produit du texte par fragments, appelle des outils, modifie un état, demande une approbation; l'application qui l'affiche doit suivre tout cela en direct. MCP prévoit bien l'élicitation et l'extension MCP Apps (chapitre 5), mais ces mécanismes vont du serveur d'outils vers l'hôte, non du service qui exécute l'agent vers l'interface de l'utilisateur. Sans standard, chaque application frontale se lie au format de flux d'un cadriciel.

### Le modèle

AG-UI se définit comme un protocole ouvert, léger et fondé sur des événements, qui normalise la connexion entre un agent et une application destinée à l'utilisateur [1]. Sa documentation le situe comme troisième couche, à côté de MCP (agent-outils) et d'A2A (agent-agent).

Le client envoie par HTTP POST une entrée d'exécution (`RunAgentInput`), qui contient les messages, le contexte et la définition des outils offerts par l'interface [2]. Le service répond par un flux d'événements qui met l'affichage à jour. Deux encodages sont documentés pour le client HTTP de référence : des événements SSE en texte et un format binaire plus compact. Le protocole n'impose toutefois aucun transport.

Les événements se répartissent en familles [3] : cycle de vie d'une exécution, messages diffusés par fragments, appels d'outils, gestion d'état, activité, sous-agents, plus des événements spéciaux pour ce qui n'est pas normalisé.

Deux idées ressortent. La première est l'**état partagé** : un instantané (`StateSnapshot`) fixe l'état complet, puis des deltas le modifient par opérations JSON Patch (RFC 6902); si l'interface détecte une incohérence, elle redemande un instantané [3]. La seconde est l'**outil frontal** : c'est l'interface qui déclare des outils, et l'agent qui les appelle. Une confirmation, un formulaire ou une navigation deviennent ainsi des appels d'outils exécutés du côté de l'utilisateur, ce qui donne une forme concrète à l'humain dans la boucle (chapitre 22). Cette approbation locale ne fait toutefois pas preuve : pour une action sensible, seul un octroi du serveur d'autorisation en tient lieu (chapitre 30).

### L'interface générée

AG-UI transporte des événements; il ne dit pas quoi dessiner. MCP Apps (chapitre 5) et A2UI s'en chargent [1]. A2UI décrit l'interface comme des données déclaratives en JSON, jamais comme du code exécutable; l'agent ne peut placer que des composants inscrits par le développeur dans un catalogue [5]. L'application hôte garde ainsi la maîtrise du rendu, et un agent compromis ne peut pas injecter de script.

### Maturité

L'adoption par les cadriciels est large : la documentation et le dépôt listent des intégrations avec Microsoft Agent Framework, Google ADK, AWS Strands Agents, LangChain, CrewAI, Pydantic AI et LlamaIndex, entre autres [1][4]. Une application frontale écrite pour AG-UI peut donc changer de cadriciel d'orchestration sans être réécrite (chapitre 20, section 20.6).

La stabilité est moins assurée :

- La page des événements annonce le retrait des événements `THINKING_*`, remplacés par `REASONING_*`, « à la version 1.0.0 », et liste des événements en brouillon [3]; le dépôt n'affiche aucune version publiée [4]. Le protocole n'aurait donc pas atteint sa version 1.0, par déduction.
- Né d'un partenariat de CopilotKit avec LangChain et CrewAI, le projet n'est rattaché à aucune fondation et ne figure pas parmi les dix projets de l'Agentic AI Foundation [1][4][16].
- La page d'architecture ne dit rien de l'authentification ni de l'autorisation [2]. Le point d'accès est pourtant exposé à un navigateur : il revient à l'entreprise de le placer derrière sa propre couche d'identité (chapitre 30).

---

## 7.2 ANP : identifiants décentralisés et découverte ouverte

### Le besoin

A2A suppose qu'on sait où trouver l'agent distant et qu'un mécanisme d'authentification convenu existe déjà entre les parties. Sur l'internet ouvert, entre deux organisations sans relation préalable, ni l'un ni l'autre n'est acquis. L'Agent Network Protocol (ANP) vise ce cas. Son ambition déclarée est de devenir « le HTTP du web agentique » [7].

### Le modèle

Le livre blanc décrit trois couches [6].

**Identité et communication chiffrée.** Chaque agent porte un identifiant décentralisé (DID) du W3C. ANP définit sa propre méthode, `did:wba`, dérivée de `did:web` : le document DID, hébergé sous un nom de domaine, publie les clés publiques qui servent à vérifier la signature des requêtes. La confiance s'ancre donc dans l'infrastructure existante (DNS, certificats, TLS) plutôt que dans une chaîne de blocs ou un fournisseur d'identité commun [7].

**Méta-protocole.** Deux agents négocient en langage naturel le format de leurs échanges, génèrent le code correspondant, le testent, puis communiquent; le résultat peut être conservé et réutilisé [6].

**Protocoles d'application.** Un agent se décrit par un document JSON-LD qui emploie le vocabulaire schema.org et des termes propres à ANP. La découverte suit deux voies : active, par un point `/.well-known/agent-descriptions` qui renvoie la liste des descriptions d'un domaine; passive, par l'inscription auprès de services de recherche qui indexent ces descriptions [6].

### Maturité

L'index du dépôt donne l'état de chaque spécification du jeu 1.2 [7] : l'authentification par DID, la méthode `did:wba`, son espace de noms, la description et la découverte sont publiées; l'autorisation fondée sur les DID (version 0.7), le méta-protocole et l'adaptation au paiement AP2 sont en brouillon. Un catalogue de messagerie chiffrée de bout en bout est publié; son profil de groupe, fondé sur MLS, reste candidat.

L'autorisation, pièce maîtresse pour une entreprise, manque donc au socle publié. Le dépôt précise que la publication d'une spécification n'établit pas sa prise en charge par un SDK ou un produit; les mises en œuvre citées sont celles de la communauté, AgentConnect et AWiki [7].

Le projet est porté par une « communauté ANP » sous licence Apache 2.0, sans fondation [7]. Le groupe communautaire AI Agent Protocol du W3C, coprésidé par le titulaire du droit d'auteur du livre blanc, liste ce livre blanc parmi ses brouillons (23 mai 2025), suivi de deux documents d'août 2025 [6][8]. Un brouillon de groupe communautaire n'engage pas le W3C (chapitre 11), et aucun travail de normalisation formelle sur ANP n'a été repéré [22].

### Lecture pour l'entreprise

ANP résout un problème que l'entreprise n'a pas à l'interne : elle possède un fournisseur d'identité et un registre (chapitre 8). Le protocole devient pertinent à la frontière, là où des agents de plusieurs organisations se rencontrent sans tiers commun; le chapitre 45 examine une autre racine pour ce cas, l'identité légale vLEI.

Réserve propre à ce chapitre sur le méta-protocole : un format négocié à l'exécution et du code généré à la volée se concilient mal avec la gestion du changement et la piste d'audit.

---

## 7.3 AGNTCY : annuaire, messagerie, schémas

AGNTCY ne propose pas un protocole de plus entre deux agents, mais une infrastructure ouverte pour l'« internet des agents » : découverte, vérification des capacités, communication sécurisée [9]. Cisco l'a ouvert en mars 2025, puis l'a confié à la Linux Foundation le 29 juillet 2025, avec Dell Technologies, Google Cloud, Oracle et Red Hat comme autres membres formateurs [10]. Il est distinct de l'Agentic AI Foundation, autre foyer de la Linux Foundation, qui héberge MCP et A2A mais pas AGNTCY [16] (chapitre 11).

Selon le communiqué, AGNTCY interopère avec A2A et MCP et rend leurs agents et serveurs découvrables dans ses annuaires [10].

**OASF** (Open Agentic Schema Framework) décrit un agent par des compétences et des domaines tirés de taxonomies, et s'étend par modules. Une organisation peut héberger son propre serveur de schémas et y ajouter des extensions privées. La documentation prévient que le schéma est appelé à évoluer [11].

**Agent Directory**, en version 1.0 depuis le 19 février 2026, est un annuaire distribué, sans opérateur central, où les fiches sont adressées par leur contenu et peuvent être signées; un serveur MCP ou un agent A2A s'y importe au format OASF [12]. Le chapitre 8 (section 8.5) compare ce modèle aux registres centralisés et fédérés.

**SLIM** (Secure Low-Latency Interactive Messaging) répond à une limite de forme. Un client MCP parle à un seul serveur, et une délégation A2A lie deux agents; ni l'un ni l'autre ne décrit une conversation à plusieurs. SLIM offre l'envoi point à point, l'envoi à un groupe et l'appel de procédure, y compris vers plusieurs destinataires, sur gRPC en flux (HTTP/2 ou WebSocket), sans courtier central [13][14]. Le chiffrement de bout en bout repose sur MLS (RFC 9420), appliqué à la couche de session : un nœud de routage compromis ne peut pas lire les messages. L'identité entre organisations s'appuie sur une fédération SPIRE.

La spécification est un brouillon IETF individuel, signé par quatre auteurs de Cisco, de catégorie informative et non adopté par un groupe de travail; sa révision 03 date du 2 novembre 2026 et expire le 6 mai 2027 [14]. Le brouillon présente SLIM comme un plan de données et une couche de session pour A2A et MCP, un transport et non un concurrent, sans détailler comment ces protocoles s'y projettent.

**Identity** attribue à chaque agent ou serveur MCP un identifiant adossé à un justificatif vérifiable, l'Agent Badge, selon les modèles DID et Verifiable Credentials du W3C [15]. Le composant réutilise les identités émises par les fournisseurs en place (chapitre 29).

**Lecture pour l'entreprise.** Les composants s'adoptent séparément. L'annuaire et OASF intéressent une organisation qui fédère plusieurs registres; SLIM, celle qui a besoin de conversations de groupe chiffrées entre domaines de confiance distincts. Dans les deux cas, l'empreinte d'un seul fournisseur reste forte : auteurs du brouillon, serveur de schémas hébergé, instance publique de l'annuaire [11][12][14].

---

## 7.4 Protocoles sectoriels : l'exemple agent-instrument

Un relevé des protocoles d'agents distingue les protocoles généralistes des protocoles propres à un domaine [21]. Le Lab Agent Protocol (LAP), prépublié le 2 juin 2026 par cinq auteurs, illustre la seconde catégorie et montre ce qu'un domaine physique exige de plus [17]. Il reprend la structure d'A2A (pairs, découverte préalable, cycle de vie des tâches).

Selon ses auteurs, un instrument de laboratoire n'est ni un outil sans état ni un agent pair. Ses opérations consomment des réactifs et durent des minutes ou des heures, peuvent blesser ou endommager, exigent un accès exclusif, et produisent des résultats qui n'ont de sens qu'avec une unité, une référence d'étalonnage et une incertitude.

LAP y répond par quatre primitives : une `InstrumentCard` signée, qui décrit capacités, limites physiques, classe de sécurité et réversibilité; une réservation, bail exclusif renouvelé par battement, qui empêche deux agents de piloter le même appareil; une barrière de sécurité, jeton de confirmation d'un opérateur lié à l'instrument, à la capacité et à l'empreinte des paramètres, à usage unique; un `MeasurementResult` typé, avec unités, étalonnage, incertitude, provenance et signature.

Deux choix de conception dépassent le laboratoire. Le langage naturel n'entre que par une méthode, `intent.resolve`, qui renvoie une proposition que l'agent doit confirmer par une soumission explicite. Et LAP ne remplace pas les standards d'appareils : SiLA 2 et OPC UA restent sous le protocole, encapsulés dans un agent d'instrument.

D'après le texte intégral, LAP est une spécification de conception en version 0.1, sans mise en œuvre de référence ni évaluation empirique [17]. Ses auteurs reconnaissent des limites : une fiche signée peut sous-déclarer une classe de sécurité, et un opérateur lassé peut approuver machinalement.

L'intérêt pour l'entreprise tient donc au patron, non au protocole. Réservation exclusive, approbation liée aux paramètres exacts et résultat typé avec provenance se transposent à toute ressource dont l'usage est irréversible : une ligne de production (chapitre 28), un virement, une mise en production. Le chapitre 18 traite la compensation quand l'irréversibilité n'est pas totale; le chapitre 46, les machines mobiles, où la sûreté tient à un contrôleur vérifié.

---

## 7.5 Propositions de recherche et critères de jugement

### Deux propositions types

**TEA** (Tool-Environment-Agent) traite outils, environnements et agents comme des ressources versionnées, dotées d'un cycle de vie explicite [18]. Ses auteurs jugent que MCP et A2A gèrent mal ce cycle de vie. Le score de 89,04 % rapporté sur le jeu de test GAIA (version 6, 28 mai 2026) mesure toutefois AgentOrchestra, le cadriciel bâti sur TEA, non l'interopérabilité; et TEA y apparaît comme une abstraction interne, sans spécification publique ni mise en œuvre indépendante. Le besoin, versionner ce qu'un agent consomme, est réel; la réponse, un cadriciel.

**L'analyse des lacunes de gouvernance** examine cinq protocoles (MCP, A2A, ACP, ANP et ERC-8004) selon six dimensions, dont le vote, l'escalade humaine et l'audit [19]. Ses auteurs concluent à une couche manquante au-dessus des standards actuels (chapitre 11).

### Un sigle, trois protocoles

Le sigle ACP désigne trois choses dans ce compendium : l'Agent Communication Protocol d'IBM, absorbé par A2A (chapitre 6); l'Agentic Commerce Protocol (chapitre 10); et l'Agent Context Protocol, sous-protocole de TEA [18]. La collision illustre le rythme des propositions, plus rapide que celui de leur consolidation.

### Sept questions

Les relevés universitaires comparent les protocoles : le premier par leurs modes d'interaction, leur découverte et leur sécurité [20], le second par sept critères, dont la sécurité, la fiabilité et l'interopérabilité [21]. Ces axes décrivent un protocole sans dire s'il faut l'adopter; la grille suivante, synthèse de ce chapitre, vise cette décision.

| Question | Indice favorable | Signal d'alerte |
|---|---|---|
| Le besoin est-il hors de portée de MCP et d'A2A ? | Une interaction qu'ils n'expriment pas : groupe, flux d'interface, ressource exclusive | Une fonction qu'une extension MCP pourrait porter (chapitre 5) |
| Compose-t-il avec l'existant ? | Il enveloppe ou transporte MCP et A2A | Il redéfinit outils et agents à sa façon |
| Qui tient la plume ? | Fondation neutre, processus de proposition écrit | Un seul éditeur, un seul auteur |
| La stabilité est-elle promise ? | Versions, politique de dépréciation, tests de conformité | Publications non datées, conformité « tolérante » |
| Existe-t-il des mises en œuvre indépendantes ? | Deux au moins, interopérables | Le SDK des auteurs seulement |
| La sécurité est-elle spécifiée ? | Authentification et autorisation dans le texte | Renvoi implicite à l'intégrateur |
| Peut-on en sortir ? | Confinement derrière un adaptateur ou une passerelle | Types du protocole répandus dans le code métier |

Appliquée aux cas du chapitre, la grille tranche : AG-UI réussit sur le besoin, la composition et les mises en œuvre, mais pas sur la gouvernance ni la sécurité. ANP et AGNTCY répondent à des besoins réels avec une maturité inégale selon les pièces. LAP et TEA sont des idées à suivre.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Flux entre agent et interface | AG-UI derrière une couche d'authentification interne; approbations sensibles adossées à un octroi du serveur d'autorisation (chapitre 30) | Interface fournie par la plateforme d'agents : garder son canal natif |
| Interface générée par l'agent | Format déclaratif à catalogue fermé (A2UI) ou MCP Apps | Jamais de code produit par l'agent sans bac à sable |
| Version d'AG-UI | Épingler le SDK; isoler les types d'événements dans un module | — |
| Identité entre organisations | Fournisseur d'identité et fédération existants (chapitre 29) | Contreparties sans tiers commun : comparer vLEI (chapitre 45) et `did:wba`, à l'essai |
| Méta-protocole d'ANP | Ne pas l'adopter en production | Recherche et prototypes |
| Découverte entre registres | Registre interne à interface standard (chapitre 8) | Fédération de plusieurs entités : évaluer Agent Directory et OASF |
| Messagerie entre agents | A2A sur HTTP | Groupes chiffrés de bout en bout entre domaines de confiance : SLIM, à l'essai |
| Ressource physique ou irréversible | Réservation, approbation liée aux paramètres, résultat typé, mis en œuvre comme outils MCP | — |
| Nouveau protocole proposé | Refus tant que les sept questions n'ont pas de réponse | Besoin sectoriel sans substitut : adoption confinée et réversible |

---

## Points à retenir

- MCP et A2A laissent quatre besoins à découvert : flux vers l'interface, identité sans autorité centrale, messagerie de groupe chiffrée, pilotage de ressources physiques.
- AG-UI est largement pris en charge par les cadriciels; sa gouvernance reste hors fondation, et sa documentation d'architecture est muette sur l'authentification.
- A2UI et MCP Apps traitent le rendu, AG-UI le transport. Décrire l'interface comme des données tirées d'un catalogue fermé est la mesure de sécurité qui compte.
- ANP publie un socle d'identité et de découverte fondé sur les DID, mais son autorisation et son méta-protocole sont en brouillon; son seul ancrage institutionnel est un groupe communautaire du W3C, sans portée normative.
- AGNTCY est une infrastructure autour de MCP et d'A2A. Son annuaire est en version 1.0; sa messagerie SLIM repose sur un brouillon IETF individuel sans statut normatif.
- LAP n'a aucune mise en œuvre, mais son patron (réservation, approbation liée aux paramètres, résultat typé) vaut pour toute action irréversible.
- Les propositions de recherche signalent de vraies lacunes (cycle de vie, gouvernance collective) sans fournir de standard.
- Un protocole périphérique s'adopte pour un besoin précis, derrière un adaptateur, après examen de sa gouvernance, de sa stabilité et de ses mises en œuvre indépendantes.

---

## Sources

Pages primaires lues le 11 novembre 2026; [3], [4], [7], [8], [14] et [16] à [18] relues à l'audit, le 12 novembre :

1. [AG-UI — introduction](https://docs.ag-ui.com/introduction)
2. [AG-UI — architecture](https://docs.ag-ui.com/concepts/architecture)
3. [AG-UI — événements](https://docs.ag-ui.com/concepts/events)
4. [AG-UI — dépôt GitHub](https://github.com/ag-ui-protocol/ag-ui)
5. [A2UI — site du projet](https://a2ui.org/)
6. [ANP — livre blanc, version 1.2](https://agent-network-protocol.com/specs/white-paper.html)
7. [ANP — dépôt GitHub et index des spécifications](https://github.com/agent-network-protocol/AgentNetworkProtocol)
8. [W3C — AI Agent Protocol Community Group](https://www.w3.org/community/agentprotocol/)
9. [AGNTCY — documentation](https://docs.agntcy.org/)
10. [Linux Foundation — accueil du projet AGNTCY, 29 juillet 2025](https://www.linuxfoundation.org/press/linux-foundation-welcomes-the-agntcy-project-to-standardize-open-multi-agent-system-infrastructure-and-break-down-ai-agent-silos)
11. [AGNTCY — Open Agentic Schema Framework](https://docs.agntcy.org/oasf/open-agentic-schema-framework/)
12. [AGNTCY — Agent Directory v1.0, 19 février 2026](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)
13. [SLIM — vue d'ensemble](https://slim.agntcy.org/latest/slim/slim-overview/)
14. [IETF — draft-mpsb-agntcy-slim-03](https://datatracker.ietf.org/doc/draft-mpsb-agntcy-slim/)
15. [AGNTCY Identity — introduction](https://spec.identity.agntcy.org/docs/intro)
16. [Agentic AI Foundation — projets](https://aaif.io/projects)
17. [LAP: An Agent-to-Instrument Protocol for Autonomous Science (arXiv 2606.03755v1)](https://arxiv.org/html/2606.03755) — texte intégral lu en partie; résumé relu
18. [AgentOrchestra et le protocole TEA (arXiv 2506.12508)](https://arxiv.org/abs/2506.12508) — résumé de la v6 et texte de la v5, lu en partie
19. [Governance Gaps in Agent Interoperability Protocols (arXiv 2606.31498)](https://arxiv.org/abs/2606.31498) — résumé
20. [A survey of agent interoperability protocols (arXiv 2505.02279)](https://arxiv.org/abs/2505.02279) — résumé
21. [A Survey of AI Agent Protocols (arXiv 2504.16736)](https://arxiv.org/abs/2504.16736) — résumé

Source secondaire :

22. Plan initial du compendium, version 3 (11 novembre 2026), section « Reste à confirmer »

## Limites de ce chapitre

- Les sources [17], [18], [19], [20] et [21], d'abord connues par leur seul résumé, ont été relues au-delà du résumé le 14 novembre 2026, par un outil qui en rend des extraits; les écarts relevés sont corrigés dans le texte.
- Les pages ont été lues par un outil d'extraction qui les condense; les citations sont des traductions.
- LAP et TEA n'ont été lus qu'en partie, [19] à [21] par leur résumé seulement. La version 0.1 de LAP et l'absence de mise en œuvre viennent du texte intégral, non du résumé relu. Les cinq protocoles de [19] sont repris des chapitres 3 et 11.
- A2UI n'est connu que par la page d'accueil de son site [5].
- AG-UI : spécification et pages de sécurité non lues. La version 1.0 non atteinte reste une déduction; le silence sur l'authentification ne vaut que pour la page d'architecture et le dépôt.
- ANP : spécifications non lues; leur contenu vient du livre blanc et de l'index du dépôt. La coprésidence du groupe W3C par le titulaire du droit d'auteur du livre blanc n'a pas été revérifiée.
- Réserve levée à l'audit : le rôle de couche de session de SLIM, confirmé par la page du brouillon [14]. Non relue : la liste des membres formateurs d'AGNTCY [10].
- Aucune donnée d'adoption en entreprise n'est citée. Les sept questions, les lectures « pour l'entreprise » et la grille de décision sont des synthèses de ce chapitre.
