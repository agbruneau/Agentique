# 2 Contexte et enjeux

Les agents d’IA se multiplient plus vite que les règles qui les relient entre eux et aux systèmes de l’entreprise. Ce chapitre dresse l’état des lieux au 27 octobre 2026 à partir de données datées et attribuées, retrace la consolidation des standards ouverts depuis 2024 et nomme les huit enjeux qui motivent le cadre. Il explique enfin pourquoi agir maintenant : les protocoles se sont stabilisés, mais la gouvernance de chaque plateforme s’arrête à sa propre frontière.

## 2.1 Où en est l’entreprise agentique en 2026

Cette section situe le cadre dans les faits. L’entreprise agentique désigne ici une organisation où des agents exécutent une part croissante des processus, aux côtés des personnes et des systèmes existants, sous une supervision humaine proportionnée au risque. Les chiffres qui suivent donnent des ordres de grandeur; ils ne remplacent pas les mesures que chaque organisation tire de son propre registre.

**40 %**

des applications d’entreprise intégreront des agents spécialisés par tâche d’ici la fin de 2026, contre moins de 5 % en 2025 (prévision Gartner, août 2025)

**[1]**

**> 40 %**

des projets d’IA agentique seront annulés d’ici la fin de 2027 (prévision Gartner, juin 2025)

**[3]**

**98 %**

des répondants FinOps gèrent désormais des dépenses d’IA, contre 31 % en 2024 (State of FinOps 2026)

**[10]**

**82 : 1**

identités machines par identité humaine, selon une enquête de fournisseur (CyberArk, avril 2025)

**[11]**

### Une adoption large, une industrialisation encore rare

Les prévisions des analystes décrivent une diffusion rapide. Gartner prévoit que 40 % des applications d’entreprise intégreront des agents spécialisés d’ici la fin de 2026 et que l’IA agentique pourrait représenter environ 30 % des revenus des logiciels d’application d’entreprise d’ici 2035 **[1]**. Le même cabinet anticipe qu’en 2028, au moins 15 % des décisions de travail quotidiennes seront prises de façon autonome par l’IA agentique, contre 0 % en 2024 **[3]**.

Les enquêtes montrent toutefois un écart entre l’expérimentation et la production. Selon l’édition 2025 de l’enquête de McKinsey (novembre 2025; dernière édition dont les résultats détaillés sont publiés à cette adresse), 88 % des répondants disent que leur organisation utilise régulièrement l’IA dans au moins une fonction, mais seulement 39 % déclarent un effet sur le bénéfice avant intérêts et impôts (BAII) à l’échelle de l’entreprise. Si 62 % des organisations au moins expérimentent des agents, 23 % seulement disent déployer à l’échelle un système agentique quelque part dans l’entreprise; dans une fonction d’affaires donnée, cette part ne dépasse pas 10 % **[12]**.

Les plateformes et les protocoles, eux, sont déjà largement diffusés. En mai 2025, Microsoft indiquait que plus de 230 000 organisations, dont 90 % du Fortune 500, avaient déjà utilisé Copilot Studio; il s’agit d’un usage cumulatif, non d’un nombre de déploiements actifs **[13]**. En décembre 2025, selon le projet, le Model Context Protocol (MCP) comptait 10 000 serveurs actifs et plus de 97 millions de téléchargements mensuels de ses trousses de développement **[14]**. En avril 2026, selon la Linux Foundation, le protocole Agent2Agent (A2A) réunissait plus de 150 organisations et était intégré à Azure AI Foundry (nom qu’emploie la Linux Foundation; Microsoft désigne aujourd’hui ce service Microsoft Foundry), à Copilot Studio et à Amazon Bedrock AgentCore **[15]**. Côté dépenses, Menlo Ventures, investisseur du secteur, estime, selon un sondage auprès d’entreprises américaines, que les entreprises ont consacré 37 G$ US à l’IA générative en 2025, soit 3,2 fois plus que les 11,5 G$ US estimés pour 2024 **[16]**.

### Des échecs annoncés et une pression sur les coûts

Gartner prévoit que plus de 40 % des projets d’IA agentique seront annulés d’ici la fin de 2027 en raison de coûts croissants, d’une valeur d’affaires incertaine ou de contrôles des risques inadéquats. Le cabinet dénonce aussi l’étiquetage agentique abusif *(agent washing)*, soit des produits existants rebaptisés « agentiques » : seuls quelque 130 des milliers de fournisseurs qui se disent agentiques le seraient réellement **[3]**.

La gestion des dépenses d’IA entre déjà dans la pratique FinOps. Selon le rapport State of FinOps 2026 (1 192 répondants; l’échantillon change d’une édition à l’autre, si bien que la série n’est qu’indicative), 98 % des répondants FinOps gèrent des dépenses d’IA, contre 63 % en 2025 et 31 % en 2024, et la gestion des coûts de l’IA est la première compétence à développer **[10]**. La forme même du système pèse sur la facture : selon les mesures d’Anthropic sur son système de recherche multiagent, un agent consomme environ 4 fois plus de jetons qu’une conversation, et un système multiagent environ 15 fois plus **[17]**. Le choix du patron d’orchestration est donc aussi une décision économique (section 7.1 et section 10.5).

### Une surface de risque qui s’élargit

Selon IBM et le Ponemon Institute (juillet 2025), parmi les organisations étudiées, qui ont toutes subi une violation, 13 % ont déclaré une violation touchant un modèle ou une application d’IA; parmi elles, 97 % n’avaient pas de contrôles d’accès propres à l’IA. Les organisations où l’IA fantôme *(shadow AI)* est répandue ont payé en moyenne 670 000 $ US de plus par violation, et une organisation étudiée sur cinq a subi une violation attribuable à cette IA non gouvernée **[18]**. L’édition 2026 établit le coût moyen mondial d’une violation à 4,99 M$ US (hausse de 12 %) et recommande, pour les agents, des contrôles d’accès dynamiques fondés sur l’identité et appliqués en continu à l’exécution **[19]**.

Les identités non humaines dépassent déjà largement les identités humaines. Dans l’enquête 2025 de CyberArk (2 600 décideurs de 20 pays, dont le Canada; dernière édition dont ce ratio est publiquement vérifié), on compte 82 identités non humaines (« identités machines » selon CyberArk) par identité humaine; 68 % des répondants déclarent que leur organisation manque de contrôles de sécurité des identités pour l’IA **[11]**. Face à la prolifération des agents, Gartner (avril 2026) recommande six mesures, dont un inventaire centralisé qui inclut les agents fantômes, et observe que bloquer les agents pousse les employés vers l’IA fantôme **[2]**.

**ATTENTION**

Les chiffres de Gartner sont des prévisions, et ses enquêtes ne publient ni leur population ni leur méthode; ceux de McKinsey et de la FinOps Foundation proviennent d’enquêtes; ceux d’IBM (étude menée par le Ponemon Institute pour IBM), de CyberArk, de Microsoft et d’Anthropic viennent de fournisseurs qui ont un intérêt dans le sujet; l’estimation de Menlo Ventures vient d’un investisseur du secteur; ceux de MCP et d’A2A sont déclarés par les projets eux-mêmes. Le cadre n’en tire aucune exigence chiffrée. Il exige plutôt que chaque organisation mesure ses propres valeurs (agents inscrits, identités non humaines, coût par tâche réussie) à partir de son registre et de sa télémétrie (section 10.6, section 11.4 et chapitre 15).

## 2.2 La consolidation des standards ouverts

En deux ans, les échanges entre agents et outils, puis entre agents, sont passés de protocoles lancés par des éditeurs à des projets sous gouvernance neutre. Le tableau 5 retrace les jalons, vérifiés sauf mention contraire, qui fondent les choix du catalogue des protocoles (section 6.3).

*Tableau 5 — Chronologie vérifiée de la consolidation des standards agentiques (novembre 2024 à octobre 2026)*

| **Date** | **Jalon** | **Portée pour l’entreprise** |
| --- | --- | --- |
| 25 nov. 2024 | Anthropic annonce le Model Context Protocol (MCP), norme ouverte de raccordement des agents aux outils et aux données **[20]** | Naissance du standard vertical agent → outil |
| 9 avr. 2025 | Google annonce le protocole Agent2Agent (A2A) avec plus de 50 partenaires **[21]** | Premier protocole agent → agent largement appuyé |
| 23 juin 2025 | A2A est confié à la Linux Foundation; plus de 100 entreprises l’appuient **[22]** | Gouvernance neutre de l’axe horizontal |
| 29 juill. 2025 | La Linux Foundation accueille AGNTCY, lancé par Cisco en mars 2025 avec LangChain et Galileo **[23]** | Briques de découverte, d’identité et de messagerie, toujours hors de l’Agentic AI Foundation (AAIF) au 27 octobre 2026 |
| Août 2025 | L’Agent Communication Protocol (ACP) d’IBM fusionne dans A2A **[24]** | Un protocole concurrent de moins entre agents |
| 8 sept. 2025 | Lancement du registre officiel MCP en préversion **[25]** | Découverte publique; les serveurs privés restent à la charge de l’entreprise |
| Sept. 2025 | Google publie l’Agent Payments Protocol (AP2, 16 septembre); OpenAI et Stripe publient l’Agentic Commerce Protocol (29 septembre) **[26, 27]** | Le commerce agentique démarre en ordre dispersé |
| 9 déc. 2025 | La Linux Foundation crée l’Agentic AI Foundation (AAIF), cofondée par Anthropic, Block et OpenAI; MCP, goose et AGENTS.md en sont les projets fondateurs **[4]**. Le même jour, l’Open Worldwide Application Security Project (OWASP) publie son Top 10 des applications agentiques **[28]** | MCP passe sous gouvernance neutre; un référentiel commun des menaces apparaît |
| 12 mars 2026 | Publication d’A2A 1.0.0, première version stable; correctif 1.0.1 le 28 mai 2026 **[29, 30]** | Base contractuelle stable pour les cartes d’agent |
| 4 juin 2026 | agentgateway (créé par Solo.io, à la Linux Foundation depuis août 2025) devient un projet de l’AAIF **[31, 32]** | Passerelle ouverte pour MCP, A2A et les modèles |
| 28 juill. 2026 | Publication de la révision MCP 2026-07-28 : protocole sans état et cycle de vie formel des fonctionnalités **[33, 34]** | Exploitation à grande échelle; dépréciations à planifier |
| 17 août 2026 | A2A est annoncé comme projet de l’AAIF au stade « Growth » **[5, 35]** | MCP et A2A relèvent de la même fondation |
| 9 sept. 2026 | Envoy AI Gateway, renommé Agent Router, rejoint l’AAIF **[36]** | Autre option ouverte de passerelle de modèles et d’outils |
| 12 oct. 2026 | Cisco propose AGNTCY à l’AAIF (proposition n° 57, sans décision au 27 octobre 2026) **[37]** | AGNTCY reste un projet de la Linux Foundation, candidat à l’AAIF |
| 22 oct. 2026 | L’AAIF annonce quatre nouveaux projets et en héberge désormais dix **[38]** | Écosystème en expansion, à suivre chaque trimestre |

### Ce que la consolidation règle

Les deux axes principaux d’interaction relèvent désormais d’une même fondation neutre. Le guide officiel d’A2A les distingue clairement : MCP relie un agent à des outils et à des ressources dont les entrées et les sorties sont définies, souvent sans état; A2A relie des agents autonomes, potentiellement opaques, qui raisonnent et conservent un état au fil d’échanges à plusieurs tours **[39]**. Les règles d’évolution deviennent aussi prévisibles : depuis la révision 2026-07-28, une fonctionnalité MCP dépréciée reste dans la spécification au moins douze mois avant de pouvoir être retirée, sauf retrait accéléré pour un risque de sécurité actif (avis de sécurité publié ou exploitation documentée), avec un préavis d’au moins 90 jours **[34]**. Pour l’entreprise, le choix d’un protocole n’est plus un pari sur un seul éditeur; il reste une dépendance envers le calendrier de la fondation, que le catalogue des protocoles absorbe.

### Ce qu’elle ne règle pas

La convergence reste partielle. AGNTCY n’est pas un projet de l’AAIF, et le commerce agentique demeure fragmenté entre l’Agentic Commerce Protocol d’OpenAI et de Stripe, AP2, dont le don à la FIDO Alliance a été annoncé le 28 avril 2026 (transfert effectif non établi à la fin d’octobre 2026), et l’Universal Commerce Protocol (UCP), porté par Google et des détaillants; l’AAIF a d’ailleurs ouvert un groupe de travail sur le commerce agentique **[40, 41]**. L’admission à l’AAIF suit un processus formel : un projet n’est officiel qu’une fois son admission approuvée et annoncée **[42]**. Enfin, le registre officiel MCP demeure en préversion, ne prend pas en charge les serveurs privés et recommande aux entreprises d’héberger leur propre registre MCP privé **[43]**. Le catalogue d’entreprise reste donc une responsabilité interne (section 6.8 et section 11.4); la veille sur les protocoles émergents est traitée à la section 6.9.

**À RETENIR**

Les protocoles disent comment les agents se parlent. Ils ne disent ni qui a le droit d’agir, ni ce qui doit être journalisé, ni combien une tâche peut coûter. Ces règles relèvent de l’entreprise : c’est l’objet du présent cadre.

## 2.3 Huit enjeux qui motivent le cadre

Sans règles communes, chaque équipe recrée ses connecteurs, ses accès et ses contrôles, et l’entreprise perd la vue d’ensemble. Le premier enjeu, la prolifération des intégrations, est le plus visible; la figure 2 l’illustre.

> **[Figure]**
> - Sans cadre commun
> - Chaque agent a ses connecteurs : N × M intégrations
> - Agent RH
> - Agent ventes
> - Agent TI
> - Agent finance
> - ERP
> - CRM
> - Entrepôt
> - SaaS
> - 4 × 5 = 20 connecteurs propriétaires
> - Avec le cadre
> - Protocoles communs et catalogue : N + M contrats
> - Agent RH
> - Agent ventes
> - Agent TI
> - Agent finance
> - Passerelle et catalogue
> - MCP · A2A
> - MCP · ERP
> - MCP · CRM
> - MCP · Entrepôt
> - MCP · SaaS
> - SGED MCP · SGED
> - 4 + 5 = 9 contrats réutilisables, un point d’application

***Figure 2 — Du maillage N × M aux contrats communs N + M.** À gauche, chaque agent possède ses propres connecteurs vers chaque système : quatre agents et cinq systèmes exigent vingt intégrations, chacune avec sa sécurité. À droite, chaque agent et chaque système publient un seul contrat derrière la passerelle et le catalogue : neuf contrats réutilisables, soumis à un point d’application unique, les autorisations restant fixées par couple agent-outil. Source : élaboration du cadre CRE-IA-2026-01; exemple illustratif.*

Anthropic présente MCP comme un protocole unique qui remplace des connecteurs sur mesure et fragmentés **[20]**; l’expression « N × M » est une vulgarisation de ce bénéfice, non un énoncé de la spécification. Le calcul illustre l’ordre de grandeur : 50 agents et 200 systèmes représentent au plus 10 000 intégrations point à point, maximum théorique que la pratique n’atteint pas, contre 250 contrats. Le gain n’existe toutefois que si le catalogue est unique; des catalogues multiples recréent le maillage N × M au niveau de la gouvernance. Le tableau 6 présente les huit enjeux et la réponse que le cadre leur apporte.

*Tableau 6 — Huit enjeux, leurs symptômes et la réponse du cadre*

| **Enjeu** | **Symptôme sans cadre** | **Réponse du cadre** |
| --- | --- | --- |
| 1. Prolifération des intégrations | N agents × M systèmes = N × M connecteurs propriétaires à maintenir et à sécuriser | Protocoles communs et catalogue d’entreprise unique (PRIN-01, PRIN-02; section 6.3 et section 6.8) |
| 1. Logique métier confiée au modèle | Routage, calculs et règles d’affaires laissés au raisonnement probabiliste : dérives, boucles, résultats non reproductibles | Flux déterministe autour du modèle et patron le plus simple qui suffit (PRIN-08; chapitre 7) |
| 1. Silos d’agents | Les agents de plateformes différentes ne peuvent pas se déléguer de tâches; les mêmes capacités sont bâties plusieurs fois | Carte d’agent, protocole A2A et catalogue d’entreprise comme source de découverte (PRIN-01, PRIN-02; section 6.6 et section 6.8) |
| 1. Accès excessifs et identités non humaines | Comptes de service partagés, clés d’API statiques, droits larges et permanents; impossible de savoir quel agent a agi | Identité propre à chaque agent, délégation par jeton, moindre privilège et moindre agence (PRIN-03; chapitre 9) |
| 1. Décisions non traçables | Impossible d’expliquer une action ou de remonter la chaîne mandant → agent → outil | Traçage de bout en bout et journal d’audit chaîné et ancré (PRIN-06; section 10.1 et section 10.3) |
| 1. Effets non maîtrisés et coûts | Boucles, actions irréversibles sans approbation, factures d’inférence imprévisibles | Niveaux d’autonomie N0 à N4, paliers d’outils P0 à P3, compensation et enveloppes budgétaires (PRIN-04, PRIN-05; chapitre 8 et section 10.6) |
| 1. Agents fantômes | Agents créés hors inventaire, sans parrain nommé ni moyen de révocation | Registre obligatoire, aucun jeton de production sans fiche complète et à jour, cycle de vie contrôlé (PRIN-10; chapitre 11) |
| 1. Obligations légales | Renseignements personnels (RP) traités sans évaluation; décisions automatisées non divulguées; incidents impossibles à reconstituer | Évaluation des facteurs relatifs à la vie privée (EFVP), transparence, droit à la révision et gestion des incidents (PRIN-06, PRIN-10; chapitre 12) |

Ces enjeux se présentent rarement isolément. Prenons un agent créé dans un logiciel-service par une équipe métier, hors inventaire, qui utilise un compte de service partagé pour mettre à jour un système financier sans approbation humaine et sans laisser de trace exploitable. À lui seul, il réunit les enjeux 4, 5, 6 et 7. C’est pourquoi le cadre traite ensemble l’identité, la passerelle, le registre et le traçage, plutôt que comme des chantiers séparés.

## 2.4 Pourquoi un cadre commun maintenant

Trois évolutions convergent en 2026 et rendent un cadre commun à la fois possible et nécessaire.

### La gouvernance native s’arrête à la frontière de chaque plateforme

Des éditeurs de passerelles soutiennent que la gouvernance native d’une plateforme ne se transfère pas aux autres : selon TrueFoundry, une règle de prévention des fuites de données d’un écosystème ne s’applique pas à l’agent d’un autre; selon MuleSoft, la gouvernance native d’un nuage devient insuffisante dès que plusieurs environnements d’exécution coexistent **[44, 45]**. Ces fournisseurs ont un intérêt commercial dans la thèse; il s’agit d’un argument d’architecture, non d’un constat mesuré. Les faits publiés vont néanmoins dans le même sens. Microsoft Agent 365, en disponibilité générale depuis le 1er mai 2026, offre un registre et des contrôles comme le blocage des agents non gérés, mais sa synchronisation avec Amazon Bedrock et Google Cloud est en préversion et les actions de cycle de vie sur les agents infonuagiques de tiers sont seulement annoncées **[46]**. ServiceNow a annoncé le 5 mai 2026 l’extension de son AI Control Tower pour découvrir et gouverner l’IA déployée dans n’importe quel système **[47]**. Chaque éditeur propose son plan de contrôle; une entreprise qui exploite plusieurs plateformes en aura plusieurs, et la couverture de l’ensemble de ses agents par un seul d’entre eux reste à démontrer.

Exemple concret : un agent de Copilot Studio délègue par A2A une vérification à un agent Agentforce, qui met à jour un dossier dans ServiceNow par MCP. Les trois plateformes prennent en charge ces protocoles (pour ServiceNow, un serveur MCP en disponibilité générale, ainsi que A2A et MCP par l’AI Agent Fabric) **[48, 49, 50, 51]**, mais la demande traverse trois registres, trois moteurs de politiques et trois journaux. Le mandant, l’identifiant de trace et les plafonds de la tâche doivent pourtant la suivre de bout en bout. Gartner recommande en ce sens une structure unifiée et en couches de supervision et d’exécution des agents, pour étendre l’IA agentique en sécurité (résumé public du 3 août 2026; le détail des trois couches, réservé aux clients, n’est pas vérifié) **[52]**. Le cadre place ce point de contrôle neutre au point d’entrée des interfaces de l’entreprise : passerelle d’agents, identité et registre (chapitre 5 et section 9.4). Il ne tient que si les systèmes de l’entreprise ne sont joignables que par la passerelle; un agent qui s’exécute chez l’éditeur d’un logiciel-service relève des contrôles compensatoires de l’EXIG-ARC-21.

### Le risque de verrouillage s’est déplacé des protocoles vers les plateformes

Avec MCP et A2A sous gouvernance neutre, le risque ne tient plus au choix du protocole, mais à ce que les plateformes conservent : extensions propriétaires, définitions d’orchestration, mémoires, identités et unités de facturation. Depuis juillet 2026, par exemple, Copilot Studio crée automatiquement une identité Microsoft Entra Agent ID pour chaque nouvel agent, sans possibilité de désactivation au niveau de l’environnement **[48]**. Chaque éditeur a aussi ses propres unités : les crédits Copilot, qui servent à facturer l’usage, chez Microsoft; chez Salesforce, les crédits Flex, qui servent à facturer l’usage, et les « Agentic Work Units », qui mesurent l’activité agentique livrée sans être une unité de facturation **[53, 54, 55]**. Le cadre exige donc que l’entreprise garde la propriété de sa logique d’orchestration, de ses contrats d’outils et de sa mémoire (PRIN-09), et qu’elle l’inscrive dans ses contrats d’approvisionnement (sections 13.1 et 13.3).

### Les obligations se précisent

Le contexte réglementaire ne laisse plus de place à l’improvisation. La Loi 25 (L.Q. 2021, c. 25) est en vigueur pour l’essentiel depuis le 22 septembre 2023, et entièrement depuis le 22 septembre 2024, date de sa dernière étape, le droit à la portabilité. Depuis le 22 septembre 2023, elle exige notamment, dans les cas prévus, l’évaluation des facteurs relatifs à la vie privée (EFVP) et encadre les décisions fondées exclusivement sur un traitement automatisé **[7, 56]**. Le règlement (UE) 2024/1689 sur l’intelligence artificielle (RIA) s’applique de façon générale depuis le 2 août 2026 aux organisations qui relèvent de son champ d’application (art. 2), y compris hors de l’Union lorsque les sorties d’un système y sont utilisées, et, selon le calendrier que publie la Commission européenne, le règlement modificatif (UE) 2026/1744 porte au 2 décembre 2027 l’application aux systèmes à haut risque de l’annexe III, date à confirmer par la relecture de ce règlement au Journal officiel (annexe H) **[57, 58]**. Au fédéral, la ligne directrice E-23 du Bureau du surintendant des institutions financières (BSIF), en vigueur le 1er mai 2027 pour les institutions financières fédérales, attend un inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs **[8]**. Pour y répondre, une organisation a besoin d’un inventaire, d’une classification des risques et de traces conservées au moment des faits, faute de pouvoir les reconstituer après coup (chapitre 12).

**À RETENIR**

Le cadre ne choisit pas de plateforme. Il fixe ce qui reste sous le contrôle de l’entreprise, quelle que soit la plateforme : contrats, identités, passerelle, traces, registre et budgets. Ces règles s’imposent plus facilement à quelques dizaines d’agents qu’à des milliers : c’est maintenant qu’il faut les poser.
