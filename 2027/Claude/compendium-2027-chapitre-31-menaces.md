# Chapitre 31 — Menaces

*Question directrice : qu'est-ce qui change dans le modèle de menace ?*

> **Version 2 — 11 novembre 2026.** État de référence : OWASP Top 10 for Agentic Applications (9 décembre 2025), OWASP MCP Top 10 (bêta), page Security Best Practices de la spécification MCP `2026-07-28`, cadre MAESTRO de la Cloud Security Alliance (6 février 2025). Les numéros entre crochets renvoient aux sources en fin de chapitre. Toutes ont été lues pour ce chapitre, les articles par leur résumé seulement; [11] à [13] sont des billets. Chapitre audité et révisé le 12 novembre 2026.

Une application classique sépare ce qu'elle exécute de ce qu'elle traite. Le code vient du développeur, les données viennent du monde, et des décennies de pratique (requêtes paramétrées, échappement, validation) servent à empêcher les secondes de devenir le premier. Un agent abolit cette séparation par construction : son programme est un texte, et tout texte qu'il lit peut s'y ajouter.

Trois autres déplacements s'y greffent. L'agent agit avec une autorité déléguée, donc une lecture détournée devient une action. Ses composants (outils, serveurs, autres agents) se choisissent à l'exécution, sur la foi de descriptions en langage naturel. Enfin, il se souvient et il communique, de sorte qu'une compromission persiste et se propage.

Ce chapitre soutient que le modèle de menace change moins par l'apparition de vulnérabilités inédites que par ce déplacement de la frontière de confiance. Aucune source lue ici n'établit qu'on sache empêcher à coup sûr un modèle de langage de suivre une instruction injectée. La sécurité d'un système d'agents se décide donc dans ce qu'un agent détourné peut encore faire, c'est-à-dire dans l'architecture. Les listes de l'OWASP nomment les risques, la modélisation par couches les situe, et les chapitres 29, 30 et 32 décrivent les contrôles.

---

## 31.1 Le modèle de menace agentique

### Ce qui ne change pas

Un serveur MCP reste un service web, et un agent, une charge de travail. La page de sécurité de la spécification MCP en témoigne : presque toutes les attaques qu'elle décrit sont des classiques d'OAuth et du web, soit le délégué confus, le jeton accepté hors de son audience, la falsification de requête côté serveur (SSRF), l'injection de commande à l'ouverture d'une URL et la confusion entre serveurs d'autorisation [4]. Ces failles ne disparaissent pas parce qu'un modèle de langage est dans la boucle. Elles y gagnent un opérateur plus crédule.

### Quatre déplacements

| Hypothèse classique | Ce que l'agent change | Conséquence |
|---|---|---|
| Les données ne s'exécutent pas | Tout texte lu peut être interprété comme une instruction | Injection indirecte (31.4) |
| Le programme fait ce que son code prévoit | Le modèle choisit ses actions, avec l'autorité qu'on lui a déléguée | Un détournement prend la forme d'une action autorisée |
| Les dépendances sont fixées à la construction | Outils et serveurs se découvrent à l'exécution, par leur description | Chaîne d'approvisionnement textuelle et mouvante (31.5) |
| Une requête se termine | La mémoire et les messages entre agents prolongent l'effet | Persistance (31.6) et propagation (31.7) |

Le premier déplacement a été formulé dès février 2023. Greshake et ses coauteurs montrent alors qu'une application intégrant un modèle de langage brouille la ligne entre données et instructions : un attaquant qui n'a aucun accès à l'application y dépose des consignes en les plaçant dans un contenu qu'elle ira chercher [6]. Leur résumé assimile le traitement d'un tel contenu à une exécution de code arbitraire et constate l'absence de parade efficace.

Le deuxième déplacement explique pourquoi les contrôles d'accès ne suffisent pas. Un agent détourné ne franchit aucune barrière : il utilise ses propres droits, avec des jetons valides. Pour le système appelé, rien ne distingue l'appel voulu par l'utilisateur de l'appel dicté par un courriel piégé.

### Un test rapide : la trifecta létale

Simon Willison a proposé en juin 2025 une grille d'une grande économie. Un agent devient dangereux lorsqu'il réunit trois capacités : l'accès à des données privées, l'exposition à du contenu non fiable et la possibilité de communiquer vers l'extérieur [12]. Avec les trois, un contenu piégé peut lui faire lire un secret et l'envoyer à l'attaquant.

Willison note que MCP facilite cette réunion, puisque le protocole encourage à combiner des outils de provenances diverses, et que presque tout outil capable d'une requête sortante peut servir à exfiltrer. Sa recommandation : ne pas réunir les trois dans un même agent.

La grille ne couvre que l'exfiltration. Un agent privé de canal sortant, mais capable de supprimer des enregistrements ou d'approuver un paiement, reste exposé au détournement.

### Qui attaque

Cinq positions d'attaquant ressortent des sources lues : l'auteur d'un contenu que l'agent lira, ne serait-ce qu'une ligne de journal (chapitre 47) [6]; l'éditeur d'un outil ou d'un serveur, malveillant dès l'origine ou devenu tel après approbation [11]; l'utilisateur d'un agent partagé, qui écrit dans une mémoire que d'autres liront (chapitre 14); un autre agent, compromis, usurpé ou adverse, comme la contrepartie d'une négociation (chapitre 45) [2][9]; enfin l'agent lui-même, lorsqu'il s'écarte de son mandat sans attaquant extérieur [2]. Seule la deuxième correspond à ce qu'une équipe de sécurité surveille d'ordinaire dans une chaîne d'approvisionnement.

---

## 31.2 OWASP Top 10 for Agentic Applications

Le projet OWASP GenAI Security a publié cette liste le 9 décembre 2025. La page de la ressource l'attribue au travail de plus de cent experts, chercheurs et praticiens [1]. L'annonce nomme un comité de relecture (NIST, Alan Turing Institute, AI Red Team de Microsoft, entre autres) et rattache la liste au Top 10 des applications LLM et à la taxonomie Agentic AI Threats & Mitigations [2].

| Code | Intitulé | Ce que décrit l'annonce [2] | Traité surtout en |
|---|---|---|---|
| ASI01 | Agent Goal Hijack | Des instructions cachées font d'un assistant un outil d'exfiltration | 31.4 |
| ASI02 | Tool Misuse | L'agent emploie un outil légitime à une fin destructrice | 31.4, chapitre 30 |
| ASI03 | Identity & Privilege Abuse | Des identifiants divulgués font agir l'agent hors de son périmètre | Chapitres 29 et 30 |
| ASI04 | Agentic Supply Chain Vulnerabilities | Les écosystèmes MCP et A2A permettent d'empoisonner des composants à l'exécution | 31.5 |
| ASI05 | Unexpected Code Execution | Le langage naturel ouvre des chemins vers l'exécution de code à distance | 31.4 |
| ASI06 | Memory & Context Poisoning | Une mémoire altérée modifie le comportement longtemps après l'interaction | 31.6, chapitre 14 |
| ASI07 | Insecure Inter-Agent Communication | Des messages usurpés entre agents égarent des groupes entiers | 31.7 |
| ASI08 | Cascading Failures | De faux signaux se propagent dans des chaînes automatisées en s'amplifiant | 31.7, chapitre 21 |
| ASI09 | Human-Agent Trust Exploitation | Des explications assurées amènent un opérateur à approuver une action nuisible | 31.4, chapitre 22 |
| ASI10 | Rogue Agents | Désalignement, dissimulation, action de sa propre initiative | 31.7, chapitre 34 |

**La liste suit le trajet d'une attaque.** ASI01 est l'entrée; ASI02 et ASI05 sont ce que l'attaquant obtient; ASI03 mesure l'étendue des dégâts; ASI06 assure la persistance; ASI07 et ASI08 la propagation. Le tableau se lit comme une chaîne à rompre, pas comme dix problèmes indépendants.

**ASI09 vise l'humain, pas le logiciel.** Un point d'approbation ne protège que si la personne comprend ce qu'elle approuve, et un agent détourné rédige lui-même la justification de l'action qu'on lui a dictée. Le chapitre 30 en tire la conséquence : une approbation n'a de valeur probante que si elle est émise hors de l'agent.

**ASI10 n'exige pas d'attaquant.** Sa cause peut être entièrement interne. Elle relève autant de l'assurance (chapitre 32) et de l'arrêt d'urgence (chapitre 34) que de la sécurité au sens strict.

Une réserve de méthode : l'annonce illustre plusieurs entrées par des incidents nommés, non vérifiés ici, mais ne donne ni fréquences observées ni critère de classement [2]. Le bilan d'incidents publié par le projet en octobre 2026 n'y supplée pas : ses rattachements aux codes ASI sont des appréciations d'analystes, et il ne se dit ni exhaustif ni officiel [13]. La liste est un vocabulaire issu d'un consensus d'experts. Elle sert à vérifier qu'une analyse n'oublie rien, pas à établir des priorités chiffrées.

---

## 31.3 OWASP MCP Top 10

L'OWASP mène un second projet, propre au protocole. La page du projet le situe en phase 3 sur 5, « Beta Release and Pilot Testing »; la version finale correspond à la phase 4 et aucune date n'est donnée [3]. Les entrées portent le millésime 2025, et la page présente l'ensemble comme un document vivant. On le cite donc comme une bêta.

| Code | Intitulé | Risque résumé [3] | Nature |
|---|---|---|---|
| MCP01 | Token Mismanagement & Secret Exposure | Jetons de longue durée et secrets exposés par la mémoire du modèle ou les journaux | Classique |
| MCP02 | Privilege Escalation via Scope Creep | Des permissions mal définies s'élargissent avec le temps | Classique |
| MCP03 | Tool Poisoning | Un outil compromis, ou sa sortie, injecte un contexte trompeur | Propre aux agents |
| MCP04 | Software Supply Chain Attacks & Dependency Tampering | Une dépendance compromise modifie le comportement ou ouvre une porte dérobée | Classique |
| MCP05 | Command Injection & Execution | L'agent construit et exécute des commandes à partir d'entrées non fiables | Classique, aggravé |
| MCP06 | Prompt Injection via Contextual Payloads | Des instructions cachées dans le texte traité détournent le modèle | Propre aux agents |
| MCP07 | Insufficient Authentication & Authorization | Identités non vérifiées, contrôles d'accès absents | Classique |
| MCP08 | Lack of Audit and Telemetry | Journalisation insuffisante pour enquêter | Classique |
| MCP09 | Shadow MCP Servers | Déploiements non approuvés, hors gouvernance, souvent mal configurés | Organisationnel |
| MCP10 | Context Injection & Over-Sharing | Un contexte partagé ou persistant expose les données d'une tâche à une autre | Propre aux agents |

La colonne « Nature » est une lecture de ce chapitre, non une classification de l'OWASP. Elle fait ressortir que six entrées sur dix sont des problèmes que l'entreprise sait déjà traiter, avec ses outils de gestion des secrets, d'analyse de dépendances et de journalisation. L'effort nouveau se concentre sur MCP03, MCP06 et MCP10, où la charge utile est du texte, et sur MCP09, qui est une question d'inventaire.

### Ce que couvre la spécification, et ce qu'elle ne couvre pas

La page Security Best Practices de la spécification `2026-07-28` complète la liste par le côté du protocole [4]. Elle décrit notamment :

- le **délégué confus** : un serveur MCP mandataire d'une API tierce, qui combine identifiant client statique et enregistrement dynamique, laisse un attaquant obtenir un code d'autorisation sans consentement; il **doit** recueillir un consentement par client avant de relayer;
- le **passage de jeton** : un serveur **ne doit pas** accepter un jeton qui n'a pas été émis pour lui (chapitre 5);
- le **SSRF** lors de la découverte OAuth : un serveur malveillant fait pointer les métadonnées vers une adresse interne; le client **devrait** exiger HTTPS, bloquer les plages privées et valider les redirections;
- le **détournement d'identifiant d'état**, qui remplace le détournement de session des versions antérieures : dans un protocole sans état, le serveur **ne doit pas** tenir la possession d'un identifiant de panier ou de flux pour une authentification, et **devrait** lier chaque identifiant à l'utilisateur tiré du jeton vérifié;
- la **compromission d'un serveur local** (31.5), la validation des URL d'autorisation et la **minimisation des portées**, qui limite le rayon d'action d'un jeton volé (chapitre 30).

Cette page ne contient, dans la version lue, aucune section sur l'empoisonnement d'outil ni sur l'injection de prompt. Le partage est clair : la spécification sécurise le canal et l'autorisation; ce qui circule dans le canal, soit des descriptions, des résultats et des ressources lus par un modèle, reste à la charge de l'hôte et de l'entreprise. Aucun des deux documents ne suffit seul.

---

## 31.4 Injection indirecte et détournement d'objectif

### Le mécanisme

L'injection directe vient de l'utilisateur, qui tente de faire dévier le modèle. L'injection indirecte vient d'un tiers : la consigne est déposée dans un contenu que l'agent ira lire pour accomplir une tâche légitime [6]. L'utilisateur est alors la victime, non l'auteur. Dans un agent outillé, le vecteur est le résultat d'un outil : une page récupérée, un courriel, un billet, une ligne de base de données, la réponse d'une API.

Le détournement d'objectif (ASI01) est le résultat recherché. L'agent poursuit, avec ses moyens légitimes, un but qui n'est plus celui de son mandant. Ce que l'attaquant en tire dépend des capacités disponibles : une exfiltration si l'agent lit des données privées et dispose d'un canal sortant, une action non voulue s'il a des outils à effet (ASI02), une exécution de code s'il a un interpréteur (ASI05, MCP05), une persistance s'il écrit en mémoire (ASI06), une approbation obtenue par tromperie s'il présente lui-même la demande (ASI09).

### L'état des défenses

Le banc d'essai AgentDojo réunit 97 tâches réalistes (messagerie, banque en ligne, réservation de voyages) et 629 cas de test de sécurité. Selon ses auteurs, les attaques existantes violent certaines propriétés de sécurité, mais pas toutes, et les modèles de pointe de l'époque échouent à de nombreuses tâches même sans attaque [7]. Le résumé ne publie pas de taux. Il rappelle en revanche que sécurité et utilité se mesurent ensemble : une défense qui empêche l'agent de travailler n'en est pas une.

Willison se dit profondément méfiant envers les produits de garde-fous qui annoncent détecter les attaques, et juge qu'un taux de détection de l'ordre de 95 % serait un échec selon les critères de la sécurité applicative [12]. C'est une opinion de praticien, non une mesure, mais l'argument est structurel : un filtre probabiliste face à un adversaire qui s'adapte ne constitue pas une frontière.

Une prépublication de juin 2025, signée par quatorze auteurs, propose pour cette raison de déplacer la défense du modèle vers la conception : des patrons qui donnent à l'agent une résistance démontrable à l'injection, au prix d'un compromis explicite entre utilité et sécurité que les auteurs analysent sur des études de cas [8]. Le résumé ne nomme pas les patrons, et le texte complet n'a pas été lu. Le chapitre 45 chiffre le coût d'un tel patron, CaMeL, qui sépare flux de contrôle et flux de données : 77 % des tâches d'AgentDojo résolues avec sécurité prouvable, contre 84 % sans défense.

### Ce qu'on peut en tirer

1. **Réduire ce que l'agent peut faire après avoir lu du contenu non fiable.** C'est la mesure qui ne dépend pas du modèle : agents spécialisés, portées étroites, moindre privilège par opération (chapitre 30). L'agent de remédiation qui propose sans exécuter en est un exemple (chapitre 47).
2. **Rompre la trifecta.** Un agent qui lit le web n'a pas accès aux données sensibles; un agent qui y a accès ne peut pas émettre vers une destination arbitraire. Le contrôle des sorties se place à la passerelle (chapitre 24).
3. **Marquer la provenance.** L'hôte devrait présenter le résultat d'un outil comme une donnée et en garder la trace (chapitre 13). Cette mesure réduit le risque sans le supprimer.
4. **Placer l'approbation humaine sur les actions à effet, hors de l'agent.** L'écran d'approbation doit montrer l'action réelle, avec ses arguments complets, et non le résumé qu'en fait l'agent (chapitres 22 et 30).
5. **Détecter, en dernier.** Les filtres d'entrée et de sortie servent de couche supplémentaire et de source de signaux. Ils ne remplacent aucune des quatre mesures précédentes.

---

## 31.5 Chaîne d'approvisionnement : outils empoisonnés, serveurs fantômes

### L'outil empoisonné

Le chapitre 5 rappelle que la description d'un outil est injectée dans le contexte du modèle. Invariant Labs a montré le 1er avril 2025 ce qu'on peut en faire [11]. Un serveur expose un outil d'addition d'apparence anodine. Sa description contient un bloc d'instructions que l'utilisateur ne voit pas, mais que le modèle lit en entier : lire des fichiers sensibles, en passer le contenu dans un argument annexe, n'en rien dire. Dans la démonstration, l'agent de programmation Cursor lit le fichier de configuration MCP de l'utilisateur et ses clés SSH, puis les transmet au serveur malveillant. La fenêtre de confirmation n'affichait pas l'argument en entier.

Deux variantes du billet comptent davantage pour l'entreprise.

**Le changement après approbation** (*rug pull*). Un serveur se présente proprement à l'installation, puis modifie ses descriptions. L'utilisateur qui l'a approuvé une fois reste exposé. Une approbation ponctuelle ne dit donc rien de l'état du serveur le lendemain. La variante est sortie du laboratoire : selon le bilan de l'OWASP, un serveur MCP proposé en août 2026 par 23 demandes de tirage modifiait ses métadonnées après trois appels pour orienter l'agent vers des clés SSH et des justificatifs infonuagiques; aucune demande n'a été fusionnée [13].

**L'ombrage entre serveurs** (*shadowing*). La description d'un outil malveillant modifie la manière dont l'agent emploie l'outil d'un autre serveur, pourtant fiable. Dans la démonstration, tous les courriels partent vers l'adresse de l'attaquant, quel que soit le destinataire demandé, sans que l'outil malveillant soit jamais appelé. L'isolation entre serveurs que garantit le protocole (chapitre 5) s'arrête au contexte du modèle, où toutes les descriptions se côtoient.

Ces résultats viennent d'un fournisseur d'outils de sécurité, qui recommande en partie ses propres produits. L'OWASP reprend toutefois le risque dans ses deux listes, sous MCP03 et ASI04 [2][3].

### Le serveur local

Un serveur local est un programme téléchargé et exécuté sur le poste, avec les droits de l'hôte. La spécification relève trois voies de compromission : une commande de démarrage malveillante glissée dans une configuration, une charge malveillante dans le serveur lui-même, et l'accès par relecture DNS à un serveur laissé en écoute sur l'adresse locale [4]. Un hôte qui offre une configuration en un clic **doit** afficher la commande exacte, sans troncature, et obtenir une approbation explicite. Il **devrait** exécuter le serveur dans un bac à sable aux privilèges minimaux. La mesure qui limite réellement les dégâts n'est donc qu'une recommandation.

### Le serveur fantôme

MCP09 désigne les serveurs déployés hors de toute gouvernance, souvent avec des réglages par défaut faibles [3]. C'est l'informatique fantôme appliquée aux agents, avec une circonstance aggravante : un serveur local s'installe en une ligne de configuration et hérite aussitôt des accès du poste. Le registre officiel n'aide pas ici, puisqu'il authentifie l'éditeur sans vérifier le code et ignore les serveurs privés (chapitres 5 et 8).

### Contrôles

| Attaque | Moment | Contrôle |
|---|---|---|
| Description empoisonnée | À l'installation | Examen des descriptions complètes avant inscription au registre interne (chapitre 8) |
| Changement après approbation | En exploitation | Épinglage de version et vérification d'une empreinte des définitions [11]; nouvelle approbation à tout changement |
| Ombrage entre serveurs | À l'exécution | Cloisonnement des serveurs par agent; contrôle des flux à la passerelle (chapitre 24) |
| Serveur local malveillant | À l'installation | Liste d'autorisation, affichage de la commande, bac à sable [4] |
| Serveur fantôme | En continu | Inventaire, passage obligé par la passerelle, journalisation (MCP08) |

Le balayage des définitions d'outils par la passerelle, avec empreinte des descriptions et détection des noms voisins, est décrit au chapitre 24.

---

## 31.6 Mémoire et contexte empoisonnés

Une injection ordinaire agit pendant la session où elle est lue. Si l'agent l'écrit dans une mémoire durable, l'instruction survit à la session et se déclenche plus tard, éventuellement pour un autre utilisateur. C'est l'entrée ASI06 de l'OWASP [2].

Trois propriétés distinguent cette menace. Le **délai** sépare la cause de l'effet et complique l'enquête : la trace de l'attaque se trouve dans une session ancienne, peut-être déjà purgée. La **portée** dépasse la victime initiale dès que la mémoire est partagée entre utilisateurs ou entre agents. La **légitimité apparente** fait le reste : ce que l'agent a mémorisé lui revient comme un acquis, non comme un contenu externe.

Le chapitre 14 décrit les attaques démontrées en recherche ou observées sur le terrain, dont l'empoisonnement d'une mémoire partagée par simple conversation, et les contrôles d'architecture correspondants.

Le contexte, plus éphémère, pose un problème voisin. MCP10 vise les contextes partagés ou persistants qui exposent les données d'une tâche ou d'un utilisateur à un autre [3]. Sa variante au niveau du protocole est le détournement d'identifiant d'état (31.3) : un serveur qui se contente de la possession d'un identifiant ouvre l'état d'un utilisateur à quiconque l'obtient ou le devine [4].

Quatre questions cadrent un fonds de mémoire dans le modèle de menace : qui peut y écrire, qui le lira, combien de temps vit une entrée, et comment la retirer une fois l'empoisonnement constaté. Une mémoire qu'on ne peut ni attribuer ni purger est une compromission qu'on ne peut pas clore.

---

## 31.7 Menaces propres au multi-agents

Les appuis de cette section sont minces : des entrées de liste, une démonstration en laboratoire et un programme de recherche. Aucune ne mesure la fréquence de ces attaques en production.

### Ce que disent les sources

L'OWASP réserve trois entrées à la pluralité des agents : ASI07, ASI08 et ASI10 [2].

La prépublication Prompt Infection (octobre 2024) démontre une injection qui se réplique d'un agent à l'autre, à la manière d'un virus informatique. Les auteurs rapportent que les systèmes multi-agents y sont très vulnérables, même lorsque les agents ne partagent pas toutes leurs communications. Ils proposent un marquage des messages produits par un modèle (*LLM Tagging*), qui réduit la propagation lorsqu'il est combiné à d'autres protections [9]. Le résumé ne donne aucun chiffre.

Un article collectif de vingt-quatre auteurs, révisé en avril 2026, plaide pour un champ distinct, la sécurité multi-agents [10]. Il nomme des menaces qui n'existent pas à l'échelle d'un agent : la collusion secrète, les attaques coordonnées en essaim, la diffusion rapide par effet de réseau des atteintes à la vie privée, de la désinformation, des contournements et de l'empoisonnement de données, et la dispersion d'une attaque entre plusieurs agents pour échapper à la surveillance. Selon le résumé, ces menaces dépassent les cadres habituels de la cybersécurité et de la sûreté de l'IA.

### Ce qui est structurellement nouveau

**La confiance devient transitive.** Dans un pipeline, la sortie d'un agent est l'entrée du suivant. Si le premier a lu un contenu piégé, le deuxième reçoit l'instruction d'une source qu'il tient pour interne. La frontière entre contenu fiable et non fiable se perd dès le premier relais.

**L'autorité s'additionne.** Un agent à faible privilège qui peut solliciter un agent à privilège élevé hérite, en pratique, des droits du second. C'est le délégué confus transposé entre agents, et la raison pour laquelle l'autorité doit se réduire le long d'une chaîne de délégation (chapitre 30).

**Aucun composant ne voit l'attaque entière.** Une action répartie entre plusieurs agents peut être anodine à chaque étape et nuisible dans son ensemble. Le contrôle action par action atteint ici sa limite (chapitre 32).

**L'erreur se propage comme l'attaque.** ASI08 ne suppose pas d'adversaire. Les cascades sont celles que le chapitre 21 analyse sous l'angle de la fiabilité; la sécurité y ajoute l'hypothèse d'un déclencheur volontaire.

### Contrôles disponibles

Faute de défenses éprouvées, les mesures raisonnables sont des transpositions : authentifier chaque agent avant de traiter son message (chapitres 6 et 29); traiter le message d'un pair comme un contenu non fiable, y compris à l'intérieur de l'organisation; borner le nombre de relais; prévoir un coupe-circuit par agent et par flux (chapitre 34); corréler les traces entre agents pour reconstituer une chaîne après coup (chapitre 33). Entre organisations, le chapitre 45 ajoute la préférence pour des messages structurés, qui restreint l'espace d'un canal caché.

---

## 31.8 Modélisation par couches

### MAESTRO

Les listes disent quoi craindre, pas où chercher. Le cadre MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome), publié par Ken Huang sur le site de la Cloud Security Alliance le 6 février 2025, propose une décomposition en sept couches [5].

| Couche | Nom | Exemples de menaces [5] | Chapitres liés |
|---|---|---|---|
| 7 | Agent Ecosystem | Agent usurpé, registre ou découverte manipulés | 6, 8 |
| 6 | Security and Compliance (transversale) | Agents de sécurité empoisonnés, contournés ou compromis | 32 |
| 5 | Evaluation and Observability | Métriques manipulées, outils de surveillance compromis, évitement de la détection | 33 |
| 4 | Deployment and Infrastructure | Images de conteneur compromises, attaques sur l'orchestrateur, déni de service | 34 |
| 3 | Agent Frameworks | Bibliothèques compromises, portes dérobées, dépendances | 20 |
| 2 | Data Operations | Empoisonnement, exfiltration, pipelines de récupération compromis | 14, 15 |
| 1 | Foundation Models | Exemples adverses, vol de modèle, portes dérobées, inférence d'appartenance | — |

Selon l'auteur, les méthodes établies (STRIDE, PASTA, LINDDUN) ne saisissent ni l'autonomie ni les risques entre agents, comme la collusion [5].

Son apport le plus utile est la notion de **menace inter-couches**, qui passe d'une couche aux autres : attaque d'approvisionnement, mouvement latéral, élévation de privilège, fuite de données, cascade de désalignement entre agents [5]. L'empoisonnement d'outil s'y prête : il entre par l'écosystème (couche 7) et agit par les données de contexte (couche 2).

La méthode compte six étapes : décomposer le système selon les couches, modéliser les menaces de chaque couche, repérer les menaces inter-couches, évaluer le risque, planifier les mesures, puis mettre en œuvre et surveiller [5].

### Mode d'emploi

Les trois instruments de ce chapitre ne sont pas concurrents. La trifecta est un test rapide, à appliquer à chaque agent et à chaque ajout d'outil. Les listes de l'OWASP servent de liste de vérification en fin d'analyse. La décomposition par couches structure l'atelier de modélisation et répartit les responsabilités entre les équipes qui possèdent chaque couche.

Deux réserves demeurent. MAESTRO est un cadre publié sous forme de billet par un auteur, et non une norme; aucune évaluation indépendante n'a été lue pour ce chapitre. Et une modélisation vieillit vite quand les outils se découvrent à l'exécution : elle doit être reprise à chaque changement du catalogue d'outils, pas seulement à chaque version de l'application.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Hypothèse sur le contenu lu par l'agent | Non fiable, y compris les résultats d'outils et les messages d'autres agents | Contenu produit par un système interne maîtrisé, sans entrée d'un tiers |
| Combinaison de capacités | Jamais données privées, contenu non fiable et canal sortant dans un même agent | Canal sortant restreint à une liste de destinations fixes |
| Défense contre l'injection | Limitation des capacités et approbation hors agent; filtres en complément | Filtres seuls : aucun cas |
| Admission d'un serveur MCP | Examen des descriptions, épinglage, registre interne; nouvelle approbation à tout changement de définition | Serveur interne dont le code est maîtrisé : examen allégé |
| Serveur local sur un poste | Liste d'autorisation et bac à sable | Poste de développement isolé, sans secrets |
| Mémoire durable | Écriture restreinte, provenance conservée, purge possible | Mémoire de session, détruite à la fin |
| Messages entre agents | Authentifiés et traités comme non fiables | — |
| Référentiel de menaces | OWASP Agentic Top 10 comme vocabulaire; MCP Top 10 en complément, cité comme bêta | Référentiel sectoriel imposé |
| Méthode de modélisation | Par couches, reprise à chaque changement du catalogue d'outils | Agent unique sans outil à effet : test de la trifecta |

---

## Points à retenir

- Le changement central est le déplacement de la frontière de confiance : tout texte lu par un agent peut agir comme une instruction, et l'agent agit avec une autorité déléguée.
- Les vulnérabilités classiques demeurent. Six des dix entrées de l'OWASP MCP Top 10 et presque toute la page de sécurité de la spécification MCP en relèvent.
- Aucune source lue n'établit de parade fiable à l'injection au niveau du modèle. La défense qui tient est architecturale : limiter ce qu'un agent détourné peut faire.
- La trifecta létale (données privées, contenu non fiable, canal sortant) est le test le plus rapide à appliquer à un agent.
- La description d'un outil est une surface d'attaque. Elle peut changer après approbation, ce qu'une campagne d'août 2026 a fait hors laboratoire, et influencer l'usage des outils d'un autre serveur.
- La spécification MCP sécurise le canal et l'autorisation, pas le contenu. L'empoisonnement d'outil et l'injection restent à la charge de l'hôte et de l'entreprise.
- La mémoire transforme une injection en compromission durable. Un fonds qu'on ne peut ni attribuer ni purger ne permet pas de clore un incident.
- Les menaces multi-agents (propagation, collusion, cascades) sont nommées et démontrées en laboratoire, mais ni mesurées en production ni dotées de défenses éprouvées.
- L'OWASP Top 10 for Agentic Applications est un vocabulaire de consensus, l'OWASP MCP Top 10 une bêta, MAESTRO un cadre d'auteur. Aucun n'est une norme.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [OWASP Top 10 for Agentic Applications for 2026 — page de la ressource](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
2. [OWASP GenAI Security Project — annonce du 9 décembre 2025](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
3. [OWASP MCP Top 10 — page du projet](https://owasp.org/www-project-mcp-top-10/)
4. [Security Best Practices — spécification MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices.md)
5. [Cloud Security Alliance — Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
6. [Greshake et coll. — Not what you've signed up for (arXiv 2302.12173)](https://arxiv.org/abs/2302.12173) — résumé.
7. [Debenedetti et coll. — AgentDojo (arXiv 2406.13352)](https://arxiv.org/abs/2406.13352) — résumé.
8. [Beurer-Kellner et coll. — Design Patterns for Securing LLM Agents against Prompt Injections (arXiv 2506.08837)](https://arxiv.org/abs/2506.08837) — résumé.
9. [Lee et Tiwari — Prompt Infection (arXiv 2410.07283)](https://arxiv.org/abs/2410.07283) — résumé.
10. [Schroeder de Witt et coll. — Open Challenges in Multi-Agent Security (arXiv 2505.02077)](https://arxiv.org/abs/2505.02077) — résumé.

Sources secondaires (billets lus en entier) :

11. [Invariant Labs — MCP Security Notification: Tool Poisoning Attacks, 1er avril 2025](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) — billet de fournisseur.
12. [Simon Willison — The lethal trifecta for AI agents, 16 juin 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — billet de praticien.
13. [OWASP GenAI Security Project — GenAI and Agentic AI Exploit Roundup Q3 2026, 8 octobre 2026](https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/) — bilan d'incidents, lu le 12 novembre 2026 par résumé.

## Limites de ce chapitre

- Le document complet de l'OWASP Top 10 for Agentic Applications n'a pas été lu. Les intitulés ASI01 à ASI10 et leur description viennent de l'annonce [2]; les mesures d'atténuation que propose le document ne sont pas rapportées. L'avertissement de la table des matières n'est donc levé qu'en partie.
- Les pages détaillées de chaque entrée de l'OWASP MCP Top 10 n'ont pas été lues; le tableau de 31.3 résume la page du projet.
- Les cinq articles sont cités d'après leur résumé. Les patrons de [8], la méthode de [9] et la taxonomie de [10] ne sont pas décrits faute de lecture du texte.
- Aucun incident n'a été vérifié à sa source. La campagne d'août 2026 (31.5) est rapportée d'après [13], qui s'appuie sur un billet de Pillar Security non lu. Les chiffres de CaMeL (31.4) sont repris du chapitre 45.
- La page [1] affiche, sans description, une ressource « Securing Agentic Applications V2 » datée du 10 novembre 2026. Elle n'a pas été lue.
- Les positions d'attaquant de 31.1, la lecture en trajet d'attaque de 31.2, la colonne « Nature » de 31.3, l'ordre des mesures de 31.4, les traits et les contrôles de 31.7 et les tableaux de contrôles sont des synthèses de ce chapitre. Les analogies avec les requêtes paramétrées et l'informatique fantôme viennent de la connaissance générale.
- Aucun chiffre de prévalence ni de taux de succès d'attaque n'est cité, faute de source lue qui en donne. Les appuis de 31.7 restent minces.
- Audit du 12 novembre 2026 : [1] à [4], [8], [10] et [12] relus à la source. Ils confirment le texte, sauf le résumé de MCP01, corrigé.
