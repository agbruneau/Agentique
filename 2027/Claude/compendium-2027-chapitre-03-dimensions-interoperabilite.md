# Chapitre 3 — Les dimensions de l'interopérabilité

*Question directrice : à quels niveaux deux agents doivent-ils s'entendre pour coopérer ?*

> **Version 2 — 11 novembre 2026.** État de référence : cadre européen d'interopérabilité de 2017, spécification MCP `2026-07-28`, spécification A2A 1.0, brouillon IETF `draft-ietf-wimse-aims-01` du 2 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [13] sont des pages primaires lues pour ce chapitre, [14] à [16] des prépublications dont seul le résumé a été lu. Les renvois « chapitre N » pointent vers les chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Deux agents qui échangent un message JSON valide n'ont pas pour autant coopéré. L'un peut entendre par « client actif » un client facturé ce trimestre, l'autre un client non résilié. Ils peuvent s'accorder sur le sens et diverger sur celui des deux qui devait valider la commande. Ils peuvent s'accorder sur tout cela sans qu'aucun ait eu le droit d'agir. Le message est passé; la coopération a échoué.

L'intégration d'entreprise connaît ce problème depuis longtemps et l'a découpé en niveaux; ce chapitre adapte ce découpage aux agents et y situe les protocoles de 2026. La thèse tient en trois propositions. Les protocoles standardisent bien les deux niveaux inférieurs, le transport et la forme des messages. Ils confient le niveau sémantique à l'interprétation d'un modèle de langage, ce qui le rend fonctionnel sans le garantir. Ils n'expriment presque rien des deux niveaux supérieurs, l'organisation et le droit, qui restent à la charge de l'entreprise. Or une relation entre agents ne vaut que par son niveau le plus faible.

---

## 3.1 Un cadre à cinq niveaux

### Deux cadres antérieurs

Le cadre européen d'interopérabilité (EIF), publié par la Commission européenne en 2017, décompose l'interopérabilité en quatre couches : juridique, organisationnelle, sémantique et technique [1]. La couche sémantique y couvre à la fois le sens des données et leur syntaxe; sa formule est restée : « what is sent is what is understood ». Le cadre vise les administrations publiques, mais son découpage se transpose sans peine.

Le Levels of Conceptual Interoperability Model (LCIM), issu du monde de la simulation, propose sept niveaux, de l'absence de connexion à l'alignement des modèles conceptuels [2]. Deux de ses idées servent ici. Les niveaux sont cumulatifs, ce qui permet d'employer l'échelle comme modèle de maturité. Et le modèle distingue le sens d'un terme (sémantique) du contexte dans lequel l'information est employée (pragmatique), distinction centrale quand le destinataire est un modèle de langage.

### Le découpage retenu

Cet ouvrage retient cinq niveaux. Il part des quatre couches de l'EIF, sépare la syntaxe du sens comme le fait le LCIM, et joint la confiance au droit. Ce dernier choix est propre à ce chapitre : pour un agent, le droit d'agir doit se prouver par machine, au moment de l'appel, et non seulement se constater dans un contrat.

| Niveau | Question | Objet de l'accord | Ce que fournissent les protocoles en 2026 |
|---|---|---|---|
| Technique | Les parties peuvent-elles se joindre ? | Transport, point d'accès, découverte | Standardisé |
| Syntaxique | Peuvent-elles lire le message ? | Format, schémas, types | Standardisé |
| Sémantique | Comprennent-elles la même chose ? | Sens des termes, contexte, intention | Des descriptions en langage naturel; l'interprétation revient au modèle |
| Organisationnel | Qui fait quoi, qui décide, qui répond ? | Rôles, processus, escalade, imputabilité | Des états de tâche; presque rien d'autre |
| Juridique et de confiance | Ont-elles le droit d'agir, et peut-on le prouver ? | Identité, autorisation, obligations, preuve | Des mécanismes d'authentification; aucune expression des obligations |

### Ce que les agents changent

Premier changement : l'accord sémantique n'est plus fixé à la conception. Dans une intégration classique, un développeur lit la documentation et code la correspondance une fois pour toutes. Avec un agent, un modèle lit une description en langage naturel et décide à l'exécution. Une synthèse historique décrit ce déplacement comme le passage d'une sémantique portée par les données à une sémantique portée par les modèles [14]. L'accord devient probabiliste.

Second changement : les agents agissent. Un système qui ne fait que lire tolère une ambiguïté d'organisation ou de droit. Un agent qui commande, paie ou modifie un dossier ne la tolère pas. Les niveaux supérieurs, longtemps traités en fin de projet, deviennent des conditions préalables.

---

## 3.2 Technique et syntaxique : transport, formats, schémas

### Se joindre

Au niveau technique, deux parties conviennent d'un transport et d'une manière de se trouver. MCP définit deux transports, Streamable HTTP et stdio (chapitre 5). A2A sépare explicitement trois couches : un modèle de données canonique, exprimé en Protocol Buffers; des opérations abstraites, indépendantes du transport; et des liaisons concrètes vers JSON-RPC, gRPC et HTTP+JSON, auxquelles peuvent s'ajouter des liaisons sur mesure [6]. Le point d'accès se découvre par un document publié à une adresse convenue ou par un registre (chapitre 8).

### Se lire

Au niveau syntaxique, les parties conviennent de la forme des messages. MCP décrit chaque outil par un schéma d'entrée en JSON Schema, dialecte 2020-12 par défaut, et par un schéma de sortie facultatif. Quand ce dernier existe, le serveur doit s'y conformer et le client devrait valider le résultat [5]. A2A type le contenu échangé en parties (texte, fichier, données structurées) et laisse chaque compétence déclarer les types de média qu'elle accepte et produit [6].

| | MCP | A2A | ANP |
|---|---|---|---|
| Transport | Streamable HTTP, stdio (chapitre 5) | JSON-RPC, gRPC, HTTP+JSON [6] | HTTP [3] |
| Modèle de données | JSON-RPC; JSON Schema 2020-12 [5] | Protocol Buffers comme forme canonique [6] | Document de description en JSON-LD, vocabulaire Schema.org [7] |
| Unité décrite | Outil : nom, description, schémas [5] | Compétence : identifiant, nom, description, étiquettes [6] | Interface structurée ou en langage naturel [7] |
| Extension | Extensions négociées (chapitre 5) | Extensions identifiées par URI et versionnées [6] | Non examiné |

Un relevé de 2025 compare ces protocoles, ainsi qu'ACP, depuis absorbé par A2A (chapitre 6) [3]. Qualitatif et antérieur aux versions actuelles de MCP et d'A2A, il vaut par sa grille de lecture plus que par son état des lieux.

### Ce qui résiste encore

**Le schéma de sortie est facultatif.** Un outil MCP peut renvoyer du texte libre. C'est alors le modèle qui l'analyse, et l'accord syntaxique glisse vers le niveau sémantique.

**Versions et extensions fragmentent.** Dans A2A, un changement incompatible d'une extension exige un nouvel identifiant, et un agent ne doit pas se rabattre de lui-même sur une version antérieure [6]. La règle est saine, mais deux agents conformes au même protocole peuvent ne pas se comprendre s'ils ne partagent pas les mêmes extensions.

Ces deux niveaux relèvent désormais du choix de produit plus que de la conception. MCP et A2A sont hébergés par la même fondation [13]; la partie II les détaille.

---

## 3.3 Sémantique : sens partagé et intention

### Le schéma dit la forme, pas le sens

Un schéma déclare qu'un paramètre `status` est une chaîne de caractères. Il ne dit pas ce qu'est un client actif. Dans MCP, ce sens tient dans le champ `description`, du texte fait pour être lu [5]. Dans A2A, une compétence se décrit par un nom, une description, des étiquettes et, au besoin, des exemples [6]. Dans les deux cas, le contrat sémantique est une phrase, et son interprète est un modèle.

Ce choix a un avantage réel : il supprime le coût qui a freiné les générations précédentes. Le relevé de 2025 rappelle que la gestion d'ontologies de FIPA-ACL était assez lourde pour en limiter l'adoption [3] (chapitre 2). Un agent peut désormais employer un outil qu'il n'a jamais vu.

ANP pousse cette logique le plus loin : sa spécification recommande que tout agent offre une interface en langage naturel [7].

### Trois façons de mal se comprendre

**Un mot, deux sens.** Aucun protocole ne garantit que deux serveurs donnent le même sens à « revenu » ou à « client ». L'ambiguïté commence au nom : dans MCP, l'unicité d'un nom d'outil ne vaut qu'à l'intérieur d'un serveur, et c'est au client ou à la passerelle de lever les collisions [5]. L'accord sur le vocabulaire relève d'une couche sémantique gouvernée (chapitre 12).

**Un sens, deux contextes.** Un agent peut comprendre chaque terme et ignorer ce que l'autre sait déjà. C'est le niveau pragmatique du LCIM [2]. A2A pose en principe que des agents coopèrent sans accéder à l'état interne, à la mémoire ni aux outils de l'autre [6]. Cette opacité protège; elle oblige aussi à transmettre explicitement tout le contexte utile (chapitre 13).

**Une tâche, deux intentions.** Dans sa version 2, tirée de sept cadriciels sur plus de 200 tâches, la taxonomie MAST range 36,94 % des échecs observés dans le désalignement entre agents; l'absence de demande de clarification en représente à elle seule 11,65 % [8]. La version 3 déplace ces parts (chapitre 21). Une prépublication nomme ce phénomène « divergence d'intention sémantique » et propose un intergiciel pour le détecter. Son résumé rapporte une précision de détection de 27,9 %, obtenue sur des exécutions simulées selon le chapitre 21, ce qui situe la maturité de ce type de remède [15].

### Une interopérabilité obtenue, non garantie

L'accord sémantique entre agents fonctionne parce que les modèles interprètent bien. Quand ils interprètent mal, rien ne le signale. Une erreur syntaxique produit un rejet; une erreur sémantique produit un résultat plausible et faux. Ce niveau demande donc ses propres contrôles : vocabulaire de référence, schémas de sortie, jeux d'essai d'interprétation.

---

## 3.4 Organisationnelle : processus, rôles, imputabilité

Pour l'EIF, l'interopérabilité organisationnelle consiste à aligner les processus, les responsabilités et les attentes d'organisations qui poursuivent un but commun [1]. Transposée aux agents, la question devient : qui fait quoi, qui décide, quand faut-il s'arrêter, et qui répond du résultat.

### Ce qu'en disent les protocoles

Peu de choses. A2A offre le vocabulaire le plus riche, sous la forme d'états de tâche : soumise, en cours, terminée, échouée, annulée, rejetée, plus deux états d'interruption, l'attente d'une entrée et l'attente d'une autorisation [6]. C'est un embryon de processus partagé. Deux agents s'entendent sur le fait qu'une tâche peut être refusée ou suspendue; ils ne s'entendent pas sur les conditions qui l'exigent.

Une prépublication du 30 juin 2026 a mesuré cet écart [4]. Ses auteurs lisent les spécifications de cinq protocoles (MCP, A2A, ACP, ANP et ERC-8004) et cotent six capacités de gouvernance.

| Capacité | Cote sur les cinq protocoles |
|---|---|
| Appartenance à une communauté d'agents | Partielle pour A2A, ACP et ERC-8004; absente ailleurs |
| Délibération | Partielle pour ACP; absente ailleurs |
| Vote | Absente partout |
| Préservation de la dissidence | Absente partout |
| Escalade vers un humain | Absente partout |
| Audit rejouable | Partiel pour MCP et ERC-8004; absent ailleurs |

Aucune capacité n'obtient la cote « prise en charge », pour aucun protocole. Les auteurs en concluent que la gouvernance est une couche d'architecture manquante au-dessus des protocoles, et non une fonction à leur ajouter.

Trois réserves s'imposent. L'étude cote ce que les spécifications encodent, pas ce qu'on peut bâtir dessus. La cote « partielle » relève du jugement, sans mesure d'accord entre évaluateurs. Enfin, l'analyse porte sur le schéma MCP de novembre 2025 : la cote partielle de MCP en audit s'appuyait sur l'état de session, supprimé en juillet 2026 (chapitre 5), et sur les métadonnées des résultats. Cette cote serait à refaire; c'est une déduction de ce chapitre.

### Pourquoi ce niveau pèse

MAST range 41,77 % des échecs observés dans les défauts de spécification : consignes, rôles, conditions d'arrêt. Ses auteurs soutiennent que nombre d'échecs tiennent à la conception de l'organisation et à la coordination plutôt qu'aux limites des agents pris un à un [8]. Un protocole impeccable ne corrige pas une répartition des rôles mal pensée (chapitre 21).

Le cadre de gouvernance de Singapour pour l'IA agentique, dans sa version 1.5 du 20 mai 2026, aborde ce niveau de front [9]. L'organisation qui déploie des agents et les humains qui les supervisent restent imputables de leurs actions. Le cadre demande d'établir des chaînes d'imputabilité à l'intérieur de l'organisation et envers les autres acteurs de la chaîne de valeur : développeurs de modèles, fournisseurs de plateformes, hôtes de serveurs MCP ou d'outils externes.

Le document rapporte la stratégie de confinement de MSD, adoptée parce que les cadres d'interopérabilité sont encore naissants : les fonctions agentiques des logiciels de tiers restent par défaut limitées à leur propre écosystème [9].

L'accord organisationnel s'écrit donc hors protocole : dans l'orchestrateur (partie IV), dans la politique d'autonomie (chapitre 22) et dans la gouvernance interne (chapitre 39).

---

## 3.5 Juridique et de confiance

L'EIF définit l'interopérabilité juridique comme la capacité d'organisations soumises à des cadres juridiques différents à travailler ensemble [1]. Pour des agents, ce niveau réunit deux questions : qui est l'autre partie et que peut-elle faire; quelles obligations naissent de l'échange.

### La confiance : des mécanismes, pas une garantie

Les protocoles fournissent ici des briques. Dans A2A, un agent déclare dans sa carte les schémas de sécurité qu'il accepte (clé d'API, authentification HTTP, OAuth 2.0, OpenID Connect, TLS mutuel) et peut signer cette carte au format JWS [6]. La signature reste toutefois facultative, et l'autorisation, une fois l'appelant authentifié, relève des politiques propres du serveur. L'autorisation est de même facultative dans MCP (chapitre 5). Deux agents conformes peuvent donc se parler sans qu'aucun ait vérifié l'autre.

À l'IETF, le groupe de travail WIMSE porte un document intitulé AI Identity Management System, dont la révision 01 date du 2 novembre 2026 [10]. Il ne définit aucun protocole nouveau : il compose l'architecture WIMSE et la famille OAuth 2.0. L'agent y est une charge de travail dotée d'un identifiant unique et de justificatifs de courte durée. Entre domaines, ce sont des jetons, porteurs de revendications définies, qui traversent les frontières, et non des politiques : chaque domaine évalue la sienne. L'interopérabilité de confiance exige donc un format de preuve commun, pas un langage de politique commun. Le document reste un brouillon à visée informative (chapitres 29 et 30).

### Le droit : hors du protocole

Aucun des protocoles d'agents lus ne permet d'exprimer une obligation : limite de responsabilité, finalité permise d'une donnée, juridiction, durée de conservation. Ces termes vivent dans des contrats et des politiques que l'agent ne lit pas. Le cadre de Singapour en tire une conséquence pratique : préciser par contrat la répartition des obligations avec les tiers, exiger d'eux de la transparence, une authentification propre à chaque agent et la journalisation des appels d'outils, et, à défaut, réduire la portée du cas d'usage [9]. Hors de ces protocoles, ODRL exprime une politique d'usage et le Dataspace Protocol en fait un accord entre organisations, sans en garantir l'application une fois les données copiées (chapitre 45).

Un document de travail d'avril 2026 sur le droit européen applicable aux agents fait de l'inventaire complet des actions externes de l'agent, de ses flux de données et des systèmes connectés la première tâche de conformité d'un fournisseur, selon son résumé [16]. Un registre et des traces devraient le fournir (chapitres 8 et 33); les cadres sont traités aux chapitres 35 à 38.

### Une normalisation inachevée

L'initiative du NIST sur les standards d'agents n'annonce pas de profil d'interopérabilité à la date de sa mise à jour du 9 novembre 2026 [11], et le groupe communautaire du W3C sur les protocoles d'agents n'a publié que des brouillons, dont le livre blanc d'ANP, sans rapport final [12]. La synthèse historique déjà citée conclut que le progrès dépend désormais davantage de l'infrastructure sociotechnique que de la conception des protocoles [14]. Le chapitre 11 suit ces instances.

---

## 3.6 Grille de maturité d'interopérabilité

La grille qui suit sert de repère dans tout l'ouvrage (annexe C). C'est une proposition construite à partir des cadres cités, non un instrument validé empiriquement.

| Niveau | 0 — Ad hoc | 1 — Déclaré | 2 — Vérifié | 3 — Gouverné |
|---|---|---|---|---|
| Technique | Connecteurs sur mesure | Protocole standard, version déclarée | Conformité testée | Passerelle, politique de versions et de dépréciation |
| Syntaxique | Texte libre | Schémas d'entrée publiés | Schémas d'entrée et de sortie validés des deux côtés | Schémas versionnés, compatibilité testée avant publication |
| Sémantique | Descriptions libres | Descriptions normalisées, glossaire | Termes rattachés à un vocabulaire de référence; jeux d'essai d'interprétation | Vocabulaire gouverné, dérive mesurée |
| Organisationnel | Aucun responsable désigné | Propriétaire et rôle pour chaque agent | Règles d'escalade et points d'approbation testés | Classes de décision, piste d'audit rejouable, revue périodique |
| Juridique et de confiance | Clés partagées | Identité propre à chaque agent, portées limitées | Délégation tracée, cartes signées et vérifiées, contrats couvrant les tiers | Preuve opposable, révocation centralisée, obligations cartographiées |

Trois règles d'usage l'accompagnent.

**On évalue une relation, pas une entreprise.** L'unité d'analyse est le couple agent-outil ou agent-agent. Une même organisation aura des relations au stade 3 et d'autres au stade 0.

**Le score est celui du niveau le plus faible.** La règle reprend le principe cumulatif du LCIM [2]. Une relation au stade 3 sur le plan technique et au stade 0 sur le plan organisationnel est une relation de stade 0 : elle fonctionne, et personne n'en répond.

**La cible dépend du risque.** Une lecture interne sans effet peut se contenter du stade 1. Une action à effet externe, ou toute relation qui traverse une frontière d'organisation, demande au moins le stade 2 sur toutes les lignes, organisation et droit compris. Le stade 3 se justifie pour les actions irréversibles (chapitre 18) et les secteurs réglementés.

La grille fait ressortir le déséquilibre typique de 2026. Les protocoles amènent presque sans effort au stade 1 sur les deux premières lignes; le stade 2 n'y demande que des tests de conformité et des schémas de sortie. Les trois autres lignes restent au stade 0 tant que l'entreprise n'a rien décidé.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Cadre d'analyse | Cinq niveaux, évalués relation par relation | Parc d'un seul éditeur : les deux premiers niveaux sont acquis d'office |
| Transport et format | Protocoles ouverts : MCP vers les outils, A2A entre agents | Protocole sectoriel imposé (chapitre 7) |
| Schémas | Entrée et sortie, validées des deux côtés | Outil exploratoire dont le résultat est lu par un humain |
| Sens des termes | Descriptions rattachées au vocabulaire d'entreprise | Domaine étroit, un seul propriétaire de données |
| Interface en langage naturel | En repli; interface structurée pour toute action à effet | Découverte et exploration |
| Rôles et escalade | Définis hors protocole, dans l'orchestrateur et la politique | — |
| Agents de tiers | Confinés à leur écosystème, ouverture au cas par cas | Relation sous contrat, identité par agent et journaux disponibles |
| Identité | Une identité par agent, rattachée à un responsable humain | — |
| Cible de maturité | Fixée selon le risque; le score est le niveau le plus faible | — |

---

## Points à retenir

- Deux agents doivent s'entendre à cinq niveaux : technique, syntaxique, sémantique, organisationnel, juridique et de confiance. Le découpage adapte le cadre européen d'interopérabilité et le LCIM.
- Les protocoles de 2026 règlent les deux premiers niveaux. Ils relèvent désormais du choix de produit.
- Le niveau sémantique repose sur des descriptions en langage naturel interprétées par un modèle. L'accord est probabiliste, et son échec ne produit pas de message d'erreur.
- Le niveau organisationnel est presque absent des protocoles : ils savent suspendre une tâche, pas dire quand ni vers qui escalader.
- Une analyse de cinq protocoles ne trouve aucune capacité de gouvernance pleinement prise en charge. C'est une prépublication, fondée sur la lecture de spécifications antérieures à juillet 2026.
- Le niveau juridique reste hors des protocoles d'agents. Les mécanismes de confiance existent, mais sont facultatifs.
- Entre domaines, ce sont des jetons qui circulent, pas des politiques : il faut un format de preuve commun, non un langage de politique commun.
- Une relation vaut par son niveau le plus faible. La grille de maturité s'applique relation par relation, avec une cible fixée par le risque.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Cadre européen d'interopérabilité — COM(2017) 134, annexe 2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52017DC0134)
2. [The Levels of Conceptual Interoperability Model: Applying Systems Engineering Principles to M&S (arXiv 0908.0191)](https://arxiv.org/abs/0908.0191)
3. [A survey of agent interoperability protocols (arXiv 2505.02279v2)](https://arxiv.org/html/2505.02279v2)
4. [Governance Gaps in Agent Interoperability Protocols (arXiv 2606.31498)](https://arxiv.org/html/2606.31498)
5. [MCP — Outils, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)
6. [A2A — spécification](https://a2a-protocol.org/latest/specification/)
7. [ANP — Agent Description Protocol (ANP-07, version 1.2)](https://agent-network-protocol.com/specs/agent-description.html)
8. [Why Do Multi-Agent LLM Systems Fail? — MAST (arXiv 2503.13657v2)](https://arxiv.org/html/2503.13657v2)
9. [IMDA — Model AI Governance Framework for Agentic AI, version 1.5 (20 mai 2026, mise à jour le 5 juin 2026)](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)
10. [IETF — draft-ietf-wimse-aims-01, AI Identity Management System](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/)
11. [NIST — AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
12. [W3C — AI Agent Protocol Community Group](https://www.w3.org/community/agentprotocol/)
13. [Agentic AI Foundation — projets](https://aaif.io/projects)

Prépublications dont seul le résumé a été lu :

14. [From Multi-Agent Systems and the Semantic Web to Agentic AI: A Unified Narrative of the Web of Agents (arXiv 2507.10644)](https://arxiv.org/abs/2507.10644)
15. [Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems (arXiv 2604.16339)](https://arxiv.org/abs/2604.16339)
16. [AI Agents Under EU Law (arXiv 2604.04604)](https://arxiv.org/abs/2604.04604)

Sources secondaires : la carte thématique du compendium et le chapitre 6, pour l'absorption d'ACP par A2A.

## Limites de ce chapitre

- Le découpage en cinq niveaux, le rattachement de la confiance au droit et la grille de maturité sont des constructions de ce chapitre; la grille n'a été éprouvée sur aucun cas.
- La plupart des pages ont été lues par un outil d'extraction qui les résume; les formulations normatives d'A2A et de l'EIF sont rapportées, non citées.
- Lectures partielles : environ les quatre cinquièmes de la spécification A2A [6], la première moitié de l'article MAST [8]. L'audit du 12 novembre 2026 a relu [4], [5], [9] (passages cités), [12] et le résumé de [8]; il n'a pas relu les règles d'extension et de signature d'A2A.
- Les sources [14] à [16] ne sont connues que par leur résumé.
- La réserve sur la cote d'audit de MCP dans [4] est une déduction de ce chapitre.
- La colonne ANP du tableau de la section 3.2 repose en partie sur le relevé [3], antérieur à l'état actuel du protocole. ISO/IEC 19941 n'a pas été consulté.
- L'exemple du « client actif » est illustratif; aucune donnée d'adoption n'est citée.
