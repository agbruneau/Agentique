# 11 Gouvernance et cycle de vie

Un agent qui agit au nom de l’entreprise relève d’une personne nommée, figure au registre et suit un parcours balisé, de sa proposition à son retrait. Ce chapitre répartit les rôles, fixe la matrice RACI et le modèle opérationnel en étoile, puis définit le registre d’entreprise des agents et des serveurs MCP, les jalons du cycle de vie et le régime des dérogations, dont le régime transitoire des agents existants. Il précise enfin comment le cadre admet, révise et retire les standards de son catalogue.

**À RETENIR**

Trois règles structurent ce chapitre : une personne nommée répond de chaque agent; sans fiche complète au registre, aucun justificatif de production; tout changement significatif rouvre l’évaluation. Les rôles, la matrice RACI, les jalons du cycle de vie et les dérogations organisent l’application de ces trois règles.

## 11.1 Rôles et responsabilités

Cette section nomme les rôles que le cadre mobilise et ce que chacun doit livrer (tableau 43). Le principe est simple : un agent ne répond pas de ses actes (section 3.4); une personne identifiable en répond, et chaque décision du cycle de vie revient à un rôle précis.

Les référentiels convergent sur ce point. Le NIST AI RMF demande que les rôles et responsabilités liés aux risques de l’IA soient documentés (GOVERN 2.1) et que l’intensité de la gestion des risques suive la tolérance au risque de l’organisation (GOVERN 1.3)**[74]**. ISO/IEC 42001 traite des rôles à l’article 5.3 et de l’organisation interne à la mesure A.3 de son annexe A**[395]**. Au Québec, la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1, ci-après « Loi sur le privé »), modifiée par la Loi 25, confie la fonction de responsable de la protection des renseignements personnels (RPRP) à la personne ayant la plus haute autorité, qui peut la déléguer par écrit; la Loi exige aussi des politiques de gouvernance qui précisent les rôles et responsabilités tout au long du cycle de vie des renseignements (art. 3.1 et 3.2)**[56]**. Les organismes publics appliquent les dispositions équivalentes de la Loi sur l’accès : la personne ayant la plus haute autorité y exerce la fonction de responsable de la protection des RP (art. 8), un comité sur l’accès à l’information et la protection des renseignements personnels soutient l’organisme (art. 8.1), et les articles 63.3 (règles de gouvernance) et 63.5 (EFVP) s’appliquent**[56]**.

Microsoft Entra Agent ID distingue, pour chaque agent, un parrain *(sponsor)*, qui porte la responsabilité métier, un propriétaire *(owner)*, qui l’administre techniquement, et un gestionnaire *(manager)*, qui gère le compte utilisateur de l’agent lorsqu’il en a un**[90]**. Le cadre reprend la distinction entre parrain et propriétaire sans dépendre du produit : le propriétaire métier joue le rôle de parrain, le responsable technique celui de propriétaire au sens d’Entra. Dans le cadre, pour un agent, « propriétaire » ne s’emploie jamais seul : on écrit « propriétaire métier » (ou « parrain ») ou « responsable technique ».

*Tableau 43 — Rôles de la gouvernance agentique*

| **Rôle** | **Responsabilités principales** | **Fondement ou remarque** |
| --- | --- | --- |
| Propriétaire métier (parrain) | Répond de la finalité, des résultats et des effets de l’agent; demande son niveau d’autonomie; finance l’agent; atteste périodiquement qu’il est encore requis. | Une personne, jamais une équipe ni un fournisseur. |
| Responsable technique | Conçoit, construit, teste et exploite l’agent; tient à jour sa fiche, son contrat et sa carte d’agent; dirige l’équipe de garde. | Ne peut ni homologuer son propre agent ni valider l’atteinte de ses seuils d’évaluation (EXIG-GOV-03). |
| Équipe d’évaluation | Exécute le jeu d’évaluation et les tests de sécurité d’un agent qu’elle n’a pas construit; établit le rapport d’évaluation (section 10.4). | Désignée pour chaque agent, distincte de son équipe de construction (EXIG-GOV-03); peut relever de l’équipe plateforme. |
| Équipe plateforme | Opère les passerelles, le registre, le catalogue, le traçage, l’outillage d’évaluation, les gabarits et le coupe-circuit global. | Centre du modèle en étoile (section 11.3). |
| Équipe FinOps | Tient la table de conversion des unités des logiciels-services (EXIG-FIN-03); propose les quotas et le plafond mensuel de chaque agent (EXIG-FIN-05); calcule et publie chaque mois l’économie unitaire (EXIG-FIN-10); prépare la revue de valeur (section 11.5) et la décision de refacturation réelle (EXIG-FIN-09). | Section 10.6; peut relever de l’équipe plateforme. |
| Architecture d’entreprise | Tient le cadre et le catalogue des protocoles; approuve les revues d’architecture, que la sécurité réalise (tableau 44); instruit les dérogations. | Gouvernance des standards (section 11.7). |
| Sécurité de l’information | Modèle de menaces; politique des identités et des paliers d’outils; tests d’abus et équipe rouge; réponse aux incidents de sécurité. | Chapitre 9. |
| Risques et conformité | Classe le risque des agents; arrête le niveau d’autonomie, valide l’atteinte des seuils d’évaluation, homologue la mise en production et approuve l’attestation périodique des agents de classe faible ou modérée (tableau 44); vérifie la conformité réglementaire; suit les dérogations et les risques résiduels. | Chapitre 12. |
| Responsable de la protection des RP (RPRP) | Est consulté dès le début de tout projet impliquant des RP; encadre les EFVP; approuve les politiques de gouvernance des RP; dirige le traitement des incidents de confidentialité (choix du cadre). | Loi sur le privé, art. 3.1 à 3.3. |
| Comité d’architecture et des risques agentiques | Arrête le niveau d’autonomie, homologue et approuve l’attestation des agents de classe élevée, et tout niveau N4; accorde les dérogations; décide du retrait anticipé pour un motif de sécurité; approuve le catalogue des protocoles; décide du passage à la refacturation réelle (EXIG-FIN-09); révise le cadre chaque semestre. | Instance décisionnelle du cadre (EXIG-GOV-02). |
| Approbateurs humains | Approuvent ou refusent, sur la base de l’action exacte, les actions que la section 8.4 soumet à approbation. | Personnes compétentes, formées et dotées de l’autorité nécessaire (règlement européen sur l’IA, ou RIA, art. 26). |
| Équipe de garde | Surveille l’agent en production, reçoit les escalades, suspend l’agent au besoin et applique les procédures d’incident. | Joignable pendant les heures d’exploitation déclarées. |

L’exigence relative aux approbateurs s’inspire du règlement européen sur l’IA : le déployeur d’un système à haut risque confie la supervision humaine à des personnes compétentes, formées et dotées de l’autorité nécessaire (art. 26)**[61]**. Pour les systèmes de l’annexe III, cette obligation s’applique à compter du 2 décembre 2027 (2 août 2028 pour ceux de l’annexe I, soit les produits réglementés)**[58]**. Le cadre l’étend à tous les agents, quelle que soit leur classe (EXIG-AUT-15).

`EXIG-GOV-01` **· DOIT**

**Responsables nommés pour chaque agent**

Chaque agent et chaque serveur MCP inscrits au registre **DOIVENT** avoir un propriétaire métier (parrain) et un responsable technique désignés nommément, ainsi qu’une équipe de garde joignable pendant les heures d’exploitation déclarées. Pour un agent intégré à un logiciel-service ou exploité par un partenaire, le parrain est la personne interne qui répond de son usage et du contrat.

Pourquoi : une responsabilité confiée à « l’équipe » ou au fournisseur n’est exercée par personne; l’OWASP place le retrait inadéquat des identités non humaines, typique des agents orphelins, au premier rang de son NHI Top 10 (NHI1)**[91]**.

`EXIG-GOV-02` **· DOIT**

**Comité d’architecture et des risques agentiques**

L’entreprise **DOIT** constituer un comité d’architecture et des risques agentiques doté d’un mandat écrit qui précise sa composition (au minimum l’architecture d’entreprise, la sécurité de l’information, la fonction risques et conformité, le RPRP ou son délégué, l’équipe plateforme et des représentants des domaines métier), son quorum, ses pouvoirs, dont la décision de passer à la refacturation réelle (EXIG-FIN-09), et la fréquence de ses réunions. Le mandat **DOIT** aussi fixer une procédure d’urgence (décision du président ou d’un sous-comité, ratifiée à la séance suivante), un délai de décision par type de dossier, suivi comme indicateur, et la récusation de tout membre qui a instruit ou préparé le dossier soumis, dont l’architecture d’entreprise pour les dérogations qu’elle instruit. Ses décisions **DOIVENT** être motivées et consignées au registre.

Pourquoi : les décisions qui engagent l’entreprise (niveau N4, agent de classe élevée, dérogation, catalogue des protocoles) exigent une instance qui réunit les expertises et dont les arbitrages laissent une trace vérifiable.

`EXIG-GOV-03` **· NE DOIT PAS**

**Cumul de la préparation et de l’approbation**

Une même personne **NE DOIT PAS** à la fois préparer et approuver une décision du cycle de vie d’un agent. Sont des décisions du cycle de vie : la classification, la fixation du niveau d’autonomie, la validation de l’atteinte des seuils d’évaluation, l’homologation, l’attestation périodique, la dérogation et le retrait. En particulier, le parrain ne fixe ni n’homologue le niveau qu’il demande, et le responsable technique d’un agent ne valide pas l’atteinte de ses seuils d’évaluation, n’homologue pas sa mise en production, n’accorde pas une dérogation qui le vise et n’approuve aucune action de cet agent soumise à approbation (EXIG-AUT-10); l’évaluation est réalisée par une équipe distincte de l’équipe de construction (tableau 43). La confirmation, par le mandant, d’une action qu’il a lui-même demandée (EXIG-AUT-15) n’est pas une décision du cycle de vie.

Pourquoi : la séparation des fonctions est le contrôle le plus simple contre l’erreur et la complaisance; elle donne son sens au « A » de la matrice RACI.

## 11.2 Matrice RACI

Cette section attribue chaque activité du cycle de vie à un rôle qui réalise (R), à un seul rôle qui approuve et répond (A), aux rôles consultés (C) et aux rôles informés (I). Le tiret signifie « non concerné ». La colonne Jalon donne le jalon de la figure 25 que l’activité ferme ou prépare (1 à 6), ou l’étape où elle se déroule; un tiret y désigne une activité continue ou hors du cycle de vie d’un agent. Abréviations des colonnes : PM, propriétaire métier (parrain); RT, responsable technique; PL, équipe plateforme; AE, architecture d’entreprise; SÉC, sécurité de l’information; RC, risques et conformité; RPRP, responsable de la protection des RP; CO, comité d’architecture et des risques agentiques. Un rôle sans colonne (équipe d’évaluation, équipe FinOps) est nommé dans la cellule de l’activité, avec sa lettre.

*Tableau 44 — Matrice RACI du cycle de vie d’un agent*

| **Activité** | **Jalon (figure 25)** | **PM** | **RT** | **PL** | **AE** | **SÉC** | **RC** | **RPRP** | **CO** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Inscrire l’agent au registre | 1 | A | R | C | I | I | I | — | — |
| Classer le risque de l’agent | 1 (réexamen au 2) | R | C | — | C | C | A | C | I |
| Fixer le niveau d’autonomie (le parrain le demande) | 2 | R | R | — | C | C | A | — | I |
| Classer les outils par palier (P0 à P3) | 2 | C | R | C | I | A | C | C | — |
| Concevoir et construire | — (étapes 2 et 3) | C | A, R | C | C | C | I | I | — |
| Revue d’architecture et de sécurité (jalon de l’étape 2) | 2 | I | C | C | A | R | C | C | I |
| Évaluer l’agent et valider l’atteinte des seuils (jalon de l’étape 3; R : équipe d’évaluation) | 3 | I | C | C | — | C | A | I | — |
| Réaliser l’EFVP | 3 (commencée au 2) | A | R | I | I | C | C | C | — |
| Homologuer la mise en production (le parrain la demande; le responsable technique prépare le dossier, il ne décide pas) | 3 (provisoire) et 4 | R | R | C | C | C | A | C | I |
| Exploiter et surveiller | — (étape 5) | I | A, R | R | — | C | I | — | — |
| Gérer un incident | — | I | R | R | I | A | C | C | I |
| Accorder une dérogation | — | R | C | I | R | C | C | C | A (AE par délégation pour la classe faible, EXIG-GOV-15) |
| Attester périodiquement l’agent | 5 | R | C | I | — | I | A | — | — |
| Retirer l’agent | 6 | A (sauf retrait anticipé) | R | R | I | C | I | C | A (retrait anticipé) |
| Établir la preuve de révocation (jalon de l’étape 6) | 6 | I | R | R | — | A | I | — | — |
| Fixer les quotas et le plafond mensuel (EXIG-FIN-05; R : équipe FinOps) | — | A | C | C | — | — | I | — | — |
| Calculer et publier l’économie unitaire (EXIG-FIN-10; A, R : équipe FinOps) | — (étape 5) | I | I | C | — | — | — | — | I |
| Conduire la revue de valeur (section 11.5; R : équipe FinOps) | — (étape 5) | A | R | I | C | — | I | — | I |
| Décider du passage à la refacturation réelle (EXIG-FIN-09; R : équipe FinOps) | — | C | — | C | C | — | C | — | A |
| Réviser le catalogue des protocoles | — | I | I | C | R | C | C | — | A |

Quatre règles complètent la matrice. Pour un agent de classe élevée ou visant le niveau N4, le comité devient A pour le niveau d’autonomie, l’homologation et l’attestation périodique, à la place de la fonction risques et conformité, qui devient C; le propriétaire métier reste R. Dans un organisme public, le comité sur l’accès à l’information et la protection des renseignements personnels (art. 8.1 de la Loi sur l’accès) est C pour l’EFVP

et pour les incidents de confidentialité. Pour un incident de confidentialité, le cadre confie au RPRP le rôle A pour l’évaluation du préjudice, les avis et l’inscription au registre des incidents prévus aux articles 3.5 à 3.8 de la Loi sur le privé (section 12.8). Enfin, l’équipe de garde exécute, pour le responsable technique, les tâches R de l’exploitation et de la gestion des incidents.

Le classement du risque revient à la fonction risques et conformité plutôt qu’au parrain : celui qui souhaite déployer l’agent propose la classe, une fonction indépendante la tranche. Pour la même raison, le niveau d’autonomie, l’homologation et l’attestation sont arrêtés par la fonction risques et conformité ou par le comité, jamais par le parrain qui les demande, et l’évaluation est faite par une équipe distincte de celle qui construit. De même, la sécurité valide le palier d’un outil, parce que ce palier détermine les contrôles exigés (section 8.3).

`EXIG-GOV-04` **· DOIT**

**Un seul A, des personnes nommées**

Chaque activité du tableau 44 **DOIT** avoir un et un seul rôle A dans chaque cas que le tableau et les règles qui le complètent distinguent (classe de risque élevée ou niveau N4, retrait anticipé, délégation de la dérogation, incident de confidentialité). La fiche de chaque agent **DOIT** nommer les personnes qui tiennent, pour cet agent, les rôles R et A de la matrice, un suppléant pour chaque rôle A, et, pour chaque contrôle d’approbation que calcule l’EXIG-AUT-10, les approbateurs humains (EXIG-AUT-15). Une fiche dont un rôle A est vacant est incomplète, sauf pendant l’intérim de l’EXIG-GOV-09.

Pourquoi : deux « A » diluent la responsabilité, et une matrice sans noms ne sert à rien le jour d’un incident.

## 11.3 Modèle opérationnel en étoile

Cette section fixe la répartition du travail entre une plateforme centrale et les domaines métier (figure 24 et tableau 45). Le cadre retient un modèle en étoile *(hub-and-spoke)* : la plateforme fournit et opère le socle commun; les domaines bâtissent et exploitent leurs agents en libre-service; la sécurité, les risques et la gouvernance encadrent les deux.

Ce choix évite deux échecs connus. Tout centraliser crée un goulot d’étranglement : chaque agent attend une équipe qui ne connaît pas le métier. Tout décentraliser multiplie les passerelles, les registres et les façons de gérer les identités, donc les failles. Dans le modèle en étoile, un contrôle s’écrit une fois dans la plateforme et s’applique partout, tandis que la logique métier reste la propriété des domaines.

> **[Figure]**
> - Sécurité, risques et gouvernance : politiques, audit, approbations
> - Plateforme agentique centrale
> - passerelles, catalogue,
> - registre, gabarits, observabilité, évaluation
> - Finance
> - MCP, agents, budget
> - Ressources humaines
> - MCP, agents, budget
> - Service à la clientèle
> - MCP, agents, budget
> - Opérations TI
> - MCP, agents, budget
> - Approvisionnement
> - MCP, agents, budget
> - Ventes
> - MCP, agents, budget
> - Plateforme centrale — fournit et opère
> - Passerelles de modèles et d’agents, bus d’événements, catalogue et registre, gabarits (SDK, CI/CD, traçage), outillage d’évaluation, tableaux de bord de coûts, coupe-circuit global.
> - Domaines métier — bâtissent et exploitent
> - Serveurs MCP de domaine et logique des agents, classement des outils par palier, jeux d’évaluation métier, budget et imputation, propriétaire nommé et équipe de garde pour chaque agent.
> - Sécurité, risques, gouvernance — encadrent
> - Politiques d’identité, paliers et seuils d’approbation, tests d’abus et d’intrusion, audit des contrôles, dérogations; le comité approuve le niveau N4 et les agents à risque élevé.

***Figure 24 — Modèle opérationnel en étoile.** La plateforme centrale fournit une seule fois les passerelles, le registre, les gabarits et le coupe-circuit; chaque domaine y branche ses serveurs MCP et ses agents; la sécurité, les risques et la gouvernance encadrent l’ensemble. Source : cadre CRE-IA-2026-01; les six domaines sont donnés à titre d’exemple.*

*Tableau 45 — Répartition des responsabilités dans le modèle en étoile*

| **Responsabilité** | **Plateforme centrale** | **Domaines métier** | **Sécurité, risques et gouvernance** |
| --- | --- | --- | --- |
| Passerelles de modèles et d’agents, bus d’événements | R, A : conçoit, opère, sécurise | C : consomme en libre-service | C : audite les contrôles |
| Registre, catalogue d’entreprise et coupe-circuit global | R, A : opère l’outillage | R : tient ses fiches et contrats à jour | C : vérifie la complétude; R : déclenche le coupe-circuit |
| Gabarits d’agents (trousses de développement, CI/CD, traçage) | R, A : fournit et maintient | R : instancie | C : valide les contrôles intégrés |
| Serveurs MCP de domaine et logique des agents | C : accompagne | R, A : développe, teste, exploite | C : impose les tests d’abus |
| Classement des outils par palier | R : inscrit au catalogue | R : propose | A : valide selon la politique des paliers |
| Jeux d’évaluation métier | C : outille la chaîne d’évaluation | R, A : définit les scénarios | C : exige les cas adverses |
| Politiques d’identité et seuils d’approbation | R : applique dans les passerelles | C : décrit les cas métier | A : définit |
| Budget et imputation des coûts | R : mesure et expose les coûts | A : maîtrise son budget | I |

`EXIG-GOV-05` **· DOIT**

**Socle commun obligatoire**

Les domaines métier **DOIVENT** utiliser les passerelles, le registre, le catalogue d’entreprise, la chaîne de traçage et le coupe-circuit fournis par la plateforme. Un domaine **NE DOIT PAS** exploiter de passerelle, de registre ou de catalogue d’entreprise parallèle sans dérogation (section 11.6); une instance de la passerelle déployée au plus près d’un agent, qui partage la politique, le registre des jti et le journal d’audit des autres instances, n’est pas une passerelle parallèle (EXIG-ARC-01).

Pourquoi : un contrôle appliqué en deux endroits finit par diverger; la règle centrale de l’architecture (EXIG-ARC-01) fait passer par la passerelle d’agents, vers une version et une empreinte approuvées, tout appel d’un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3.

`EXIG-GOV-06` **· DEVRAIT**

**Conformité par construction**

La plateforme **DEVRAIT** fournir des gabarits d’agents qui intègrent par défaut l’identité propre de l’agent, la propagation du contexte de trace, les plafonds de coût, de jetons et d’itérations, l’appel aux outils par la passerelle et l’inscription au registre, de sorte que le chemin conforme soit aussi le plus court pour une équipe de domaine.

Pourquoi : un contrôle livré dans le gabarit coûte une fois; un contrôle exigé en revue coûte à chaque agent et se contourne sous la pression des échéances.

## 11.4 Registre d’entreprise des agents et serveurs MCP

Cette section définit le registre, inventaire faisant autorité de tous les agents et serveurs MCP de l’entreprise. On ne gouverne pas ce qu’on ne voit pas : le registre est la condition de tous les autres contrôles.

Le NIST AI RMF, d’application volontaire, prévoit des mécanismes d’inventaire des systèmes d’IA, dotés de ressources selon les priorités de risque (GOVERN 1.6)**[74]**. Pour les institutions financières fédérales, la ligne directrice E-23 du BSIF, en vigueur le 1er mai 2027, attend un inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs, et une cote de risque qui détermine l’intensité de la gouvernance**[8]**. Le registre du cadre répond à ces deux attentes : il couvre les agents tiers et consigne les modèles utilisés.

### Contenu et états de la fiche

Chaque agent et chaque serveur MCP a une fiche, dont le gabarit complet figure à l’annexe B. Elle consigne au minimum l’identification et la version; le parrain, le responsable technique, l’équipe de garde et les approbateurs; la finalité et les mandants autorisés; la classe de risque et le niveau d’autonomie approuvés; les outils appelés et leurs paliers; les modèles et leurs versions; les données touchées et la présence de RP; l’identité et les portées; les résultats d’évaluation; le budget et les plafonds; l’état de cycle de vie, les dates de revue et les dérogations en vigueur. Le niveau d’autonomie inscrit tient lieu, à l’interne, de « certificat d’autonomie » tel que le conçoivent Feng, McDonald et Zhang (qui le font délivrer par un tiers) : un plafond valable pour une configuration donnée**[83]**. Seul le registre, interrogé par la passerelle, fait foi; la carte d’agent n’en donne qu’une copie informative.

La fiche passe par sept états : « proposé », « en conception », « en construction », « pilote », « production », « suspendu » et « retiré ». Seuls les états « pilote » et « production » permettent d’obtenir des justificatifs d’exécution en production; l’entrée en pilote avec des justificatifs de production ou des données réelles est une mise en production (EXIG-GOV-08). La sortie de l’état « suspendu » ramène la fiche à l’état qu’elle avait, sur décision consignée. Un agent placé en quarantaine (EXIG-GOV-10) reçoit d’office une fiche minimale à l’état « suspendu », et « désactiver » un agent, au sens du cadre, c’est le faire passer à l’état « suspendu ». Un agent en exploitation à l’adoption du cadre porte en outre la mention « existant inventorié » (EXIG-GOV-16).

### Registre et catalogue

Le registre répond aux questions « qui, quoi, pourquoi et avec quel risque »; le catalogue d’entreprise (section 6.8) répond à « par quel contrat et dans quelle version ». Les deux partagent l’identifiant de l’agent ou du serveur, ce qui permet à la passerelle de vérifier à chaque appel l’état de la fiche et la version épinglée du contrat. Le registre est donc sur le chemin critique de chaque appel : son objectif de disponibilité, la

durée de validité de la copie que tient chaque passerelle et le comportement en cas de registre injoignable relèvent de l’EXIG-ORC-18 (seuls les appels P0 passent sur une copie échue, la liste de suspension voyage par un canal signé indépendant du plan de contrôle, et les compensations entrent dans une file persistée). Le registre d’entreprise est distinct du registre officiel MCP : celui-ci, en préversion depuis le 8 septembre 2025, ne contient que des métadonnées de serveurs publics, ne prend pas en charge les serveurs privés et recommande aux entreprises d’opérer leur propre sous-registre**[25, 43]**. Il peut servir de source de découverte, jamais de registre d’entreprise.

### Exemples de mise en œuvre

Plusieurs produits couvrent une partie du rôle; ce sont des exemples non limitatifs, à l’état du 27 octobre 2026. Microsoft Agent 365, en disponibilité générale depuis le 1er mai 2026, offre un registre et des contrôles comme le blocage des agents non gérés**[46]**. Amazon Bedrock AgentCore Registry tient un catalogue gouverné d’agents, de serveurs MCP, d’outils et de compétences, avec un flux de publication, de revue et d’approbation**[102]**. Azure API Center sert de registre privé pour découvrir les serveurs MCP d’une organisation**[108]**. ServiceNow a annoncé le 5 mai 2026 l’extension de son AI Control Tower à la découverte des actifs d’IA déployés, au moyen de 30 nouvelles intégrations et à un coupe-circuit**[47]**.

**ATTENTION**

Un registre de plateforme voit d’abord les agents de sa propre plateforme. Au 1er mai 2026, la synchronisation du registre d’Agent 365 avec Amazon Bedrock et Google Cloud était en préversion publique, et les actions de cycle de vie sur les agents infonuagiques tiers étaient annoncées comme à venir**[46]**. Le registre d’entreprise est donc un rôle d’architecture alimenté par plusieurs sources. La suspension d’un agent dont l’entreprise contrôle l’exécution s’applique à la passerelle d’agents; celle d’un agent intégré à un logiciel-service passe par le mécanisme d’arrêt propre que décrit sa fiche (EXIG-ARC-02), jamais par la seule console de son éditeur.

`EXIG-GOV-07` **· DOIT**

**Inventaire complet**

Le registre **DOIT** inventorier tout agent et tout serveur MCP qui agit dans le périmètre de l’entreprise, qu’il soit développé à l’interne, intégré à un logiciel-service ou exploité par un partenaire, avec une fiche conforme à l’annexe B, y compris les modèles utilisés et leurs versions. Le contenu de la fiche fait foi pour l’agent : en cas d’écart entre la fiche et une autre source (catalogue, carte d’agent, configuration), le registre corrige l’autre source ou suspend l’agent; seule fait exception la valeur d’un palier ou d’un seuil, que le catalogue fixe et que la fiche ne peut que rendre plus stricte (EXIG-AUT-13). Un agent intégré à un logiciel-service relève en outre de l’EXIG-ARC-02 : sa fiche **DOIT** décrire un mécanisme d’arrêt indépendant de la passerelle (désactivation au fournisseur d’identité, révocation des consentements OAuth, CAEP ou SSF, clause de l’EXIG-APP-06), éprouvé lors de l’exercice de l’EXIG-SEC-26.

Pourquoi : le NIST AI RMF range les logiciels, données et composants de tiers parmi les risques à gouverner (GOVERN 6.1 et 6.2)**[74]**; un agent tiers absent du registre échappe à toute revue.

`EXIG-GOV-08` **· NE DOIT PAS**

**Sans fiche, aucun justificatif**

Une identité d’agent ou de serveur MCP **NE DOIT PAS** recevoir de justificatif valide en production tant que sa fiche n’a pas été approuvée complète et n’est pas à l’état « pilote » ou « production », sauf la mesure transitoire de l’EXIG-GOV-16; pendant l’intérim de l’EXIG-GOV-09, la fiche reste réputée complète. L’entrée en pilote avec des justificatifs de production ou des données réelles est

une mise en production : elle exige la classification définitive (EXIG-CON-01), l’EFVP s’il y a des RP (EXIG-CON-04), l’exercice d’équipe rouge pour les classes modérée et élevée (EXIG-SEC-23) et une homologation provisoire bornée au niveau du pilote (annexe A). La passerelle d’agents et la passerelle de modèles **DOIVENT** refuser tout appel d’une identité dont la fiche n’est pas à l’état « pilote » ou « production ». Seules en sont exceptées les compensations déclarées au catalogue d’étapes inscrites comme exécutées, qui passent par le canal de compensation, sous l’identité de compensation de l’orchestrateur (EXIG-ORC-17).

Pourquoi : lier l’émission des justificatifs à l’état du registre transforme l’inventaire en contrôle d’accès; un agent non inscrit ne peut rien faire.

`EXIG-GOV-09` **· DOIT**

**Fiche à jour ou agent suspendu**

La fiche **DOIT** être mise à jour avant la mise en œuvre de tout changement qui en modifie le contenu. Un agent dont l’attestation périodique est échue, ou dont un rôle A est vacant depuis plus de 30 jours, **DOIT** passer à l’état « suspendu » (suspension administrative, section 11.5) jusqu’à sa régularisation; le registre avertit le parrain 30 jours avant l’échéance de l’attestation. Pendant le délai de 30 jours, le suppléant nommé à la fiche (EXIG-GOV-04), ou à défaut un intérim désigné par le comité, tient le rôle vacant, et la fiche reste réputée complète. Le délai de 30 jours est un choix du cadre.

Pourquoi : une fiche périmée donne une fausse assurance; la suspension rend le coût de la négligence visible pour le parrain plutôt que pour la sécurité.

`EXIG-GOV-10` **· DOIT**

**Détection des agents hors registre**

L’équipe plateforme **DOIT**, au moins chaque mois, rapprocher le registre de sources indépendantes (journaux des passerelles, identités d’agents du fournisseur d’identité, inventaires des logiciels-services, facturation des fournisseurs de modèles) et placer en quarantaine tout agent découvert hors registre jusqu’à son inscription (EXIG-GOV-16) ou son retrait. La quarantaine comprend, selon le type d’agent : la création d’office d’une fiche minimale à l’état « suspendu »; le refus de ses appels aux passerelles; la désactivation de son identité au fournisseur d’identité et la révocation de ses consentements OAuth; pour un agent intégré à un logiciel-service, la mise en œuvre du mécanisme d’arrêt de l’EXIG-ARC-02. La fréquence mensuelle est un choix du cadre.

Pourquoi : les agents fantômes naissent hors des processus; seul un rapprochement avec ce que les systèmes observent réellement les fait apparaître. Certaines plateformes facilitent ce rapprochement : depuis juillet 2026, Copilot Studio crée automatiquement une identité Entra Agent ID pour chaque nouvel agent**[48]**.

## 11.5 Cycle de vie et jalons

Cette section découpe la vie d’un agent en six étapes, chacune fermée par un jalon du cycle de vie qui laisse une preuve au registre; le terme écarte la confusion avec le point de contrôle d’une exécution durable (section 7.4). L’intensité des contrôles suit la classe de risque : un agent de classe faible franchit les mêmes portes qu’un agent de classe élevée, avec des preuves plus légères.

> **[Figure]**
> - 1
> - Proposition
> - 2
> - Conception
> - 3
> - Construction
> - 4
> - Pilote
> - 5
> - Production
> - 6
> - Retrait
> - ÉTAPES
> - Cas d’usage, valeur attendue, propriétaire
> - métier nommé
> - Classe de risque, niveau
> - d’autonomie, patron,
> - contrats, EFVP
> - Gabarits de plateforme,
> - jeu de référence, tests de sécurité
> - Périmètre et durée Surveillance, évaluation
> - continue, gestion des changements
> - Révocation des identités,
> - retrait du catalogue,
> - archivage, avis
> - Fiche au registre
> - état « proposé »
> - Revue d’architecture
> - et de sécurité
> - Seuils d’évaluation
> - atteints
> - Homologation
> - (annexe A)
> - Preuve de révocation
> - Changement de modèle, d’invite, d’outil, de protocole ou de population visée réévaluation
> - bornés, du niveau
> - inférieur au visé
> - JALONS DU CYCLE DE VIE
> - Attestation périodique
> - (12 mois; 6 si élevé)
> - →

***Figure 25 — Cycle de vie d’un agent et jalons.** Chaque étape se termine par un jalon du cycle de vie consigné au registre; le pilote d’un agent qui vise N3 ou N4 commence au niveau inférieur et se termine au niveau visé (EXIG-GOV-11); en production, un changement significatif renvoie l’agent aux étapes de conception, d’évaluation et de pilote, dans la mesure du changement. Source : cadre CRE-IA-2026-01.*

1. **Proposition.** Le parrain décrit le cas d’usage, la valeur attendue, l’autonomie maximale envisagée et le parcours de décision. La fonction risques et conformité attribue la classe de risque sur cette base, avant tout plafonnement (EXIG-CON-01). Jalon du cycle de vie : fiche inscrite à l’état « proposé », avec la classe approuvée.
2. **Conception.** L’équipe prépare, sous le plafond de la classe (EXIG-CON-02, section 12.1), le niveau d’autonomie visé, que la fonction risques et conformité arrête (tableau 44), ainsi que le patron d’orchestration (chapitre 7), les contrats et la carte d’agent (section 6.8). Si la conception change l’autonomie maximale envisagée ou le parcours de décision, la fonction risques et conformité réexamine la classe. S’il y a des RP, l’EFVP commence ici : la Loi sur le privé l’exige pour tout projet d’acquisition, de développement ou de refonte d’un système d’information impliquant des RP, et le RPRP est consulté dès le début (art. 3.3)**[56]**. Jalon du cycle de vie : revue d’architecture et de sécurité (tableau 44).
3. **Construction et évaluation.** L’agent est bâti sur les gabarits de la plateforme, avec son jeu d’évaluation et ses tests de sécurité (section 9.9). Jalon du cycle de vie : atteinte des seuils d’évaluation validée par une équipe distincte de l’équipe de construction (section 10.4), fiche complète et, s’il y a des RP, EFVP terminée (EXIG-CON-04); pour les classes modérée et élevée, exercice d’équipe rouge (EXIG-SEC-23); homologation provisoire, bornée au niveau du pilote, selon la grille de l’annexe A (EXIG-GOV-08).
4. **Pilote.** Périmètre, population et durée sont bornés. Le pilote d’un agent qui vise N3 ou N4 commence au niveau immédiatement inférieur et se termine au niveau visé, sous surveillance renforcée (EXIG-GOV-11). Jalon du cycle de vie : homologation selon la grille d’homologation (annexe A), qui confirme l’homologation provisoire pour la production complète.
5. **Production.** Surveillance, évaluation continue et gestion des changements. La revue de valeur (EXIG-FIN-10) réunit le parrain, le responsable technique et l’équipe FinOps; elle conclut à la poursuite, à la reconception ou au retrait de l’agent, et sa décision est consignée au registre. Jalon du cycle de vie : attestation périodique (EXIG-GOV-13), préparée par le parrain et approuvée par la fonction risques et conformité, ou par le comité pour la classe élevée (tableau 44), tous les 12 mois, tous les 6 mois pour la classe élevée.
6. **Retrait.** Révocation des identités, retrait du catalogue, avis aux consommateurs et archivage. Jalon du cycle de vie : preuve de révocation au registre, établie par l’équipe plateforme et validée par la sécurité (tableau 44).

La suspension se distingue du retrait. Elle est réversible et prend deux formes. La suspension de sécurité est immédiate : c’est le coupe-circuit, que le NIST rattache aux mécanismes permettant de supplanter, désengager ou désactiver un système dont le comportement s’écarte de l’usage prévu (MANAGE 2.4)**[74]**; elle refuse tout nouvel appel de l’agent (EXIG-IAM-20). La suspension administrative, qui suit une attestation échue, un rôle A vacant ou une dérogation échue (EXIG-GOV-09 et EXIG-GOV-16), bloque les nouvelles tâches seulement, après avis aux consommateurs connus. Ni l’une ni l’autre ne bloque les compensations des sagas en cours, qui passent par le canal de compensation (EXIG-ORC-17). Le retrait est définitif et planifié. Le délai maximal de suspension se fixe selon l’EXIG-IAM-20 et s’éprouve à l’exercice trimestriel de l’EXIG-SEC-26; dans Microsoft Entra Agent ID, par exemple, désactiver le gabarit *(agent identity blueprint)* bloque d’un coup toutes les identités qui en dérivent**[92]**.

`EXIG-GOV-11` **· DOIT**

**Jalons du cycle de vie consignés**

Un agent **DOIT** franchir dans l’ordre les six jalons du cycle de vie de la figure 25. Seules dérogent à l’ordre les transitions suivantes, chacune consignée avec sa preuve : l’abandon, de tout état vers « retiré »; la suspension, de tout état vers « suspendu », et le retour à l’état antérieur; la réévaluation (EXIG-GOV-12), de « production » vers les jalons de conception, d’évaluation et de pilote. Chaque passage est consigné au registre avec la date, le décideur désigné par le tableau 44, qui y tient un seul rôle A, et les preuves (rapport d’évaluation, EFVP, résultats des tests de sécurité, grille d’homologation de l’annexe A). Le pilote d’un agent qui vise N3 ou N4 **DEVRAIT** s’exécuter d’abord au niveau immédiatement inférieur, puis, en dernière étape, au niveau visé sous surveillance renforcée.

Pourquoi : une décision sans trace ne peut être ni auditée ni contestée; le registre devient le dossier de preuve de l’agent.

`EXIG-GOV-12` **· DOIT**

**Réévaluation sur changement significatif**

Les changements suivants **DOIVENT** déclencher une réévaluation de la classe de risque et du niveau d’autonomie, achevée avant leur mise en service : changement du modèle servi, y compris derrière un alias (valeur de `gen_ai.response.model`), ou de sa version; modification de l’invite système; ajout ou retrait d’un outil, ou passage d’un outil à un palier supérieur; nouvelle version majeure d’un contrat ou d’un protocole; changement des propriétés [A], [B] ou [C] de la règle de deux (section 9.6), de la mémoire, du corpus de récupération ou du juge d’évaluation (section 10.4); nouvelle population visée ou nouvelle finalité; modification du domaine d’exploitation (ODD); nouvelle catégorie ou nouvelle source de données, notamment de RP; changement de fournisseur ou de lieu de traitement des données; révision d’une taxonomie de menaces retenue (EXIG-SEC-02), appréciée au plus chaque semestre pour MITRE ATLAS; incident grave (section 12.8) ou dérive détectée par l’évaluation continue. Cette liste est la seule qui fasse foi; les autres listes du cadre y renvoient. La réévaluation reprend les jalons de conception, d’évaluation et de pilote dans la mesure du changement. Si le changement ne peut attendre, l’ancienne version reste en service; à défaut, l’agent est suspendu jusqu’à la fin de la réévaluation. Aucune voie ne permet de fonctionner au-dessus du plafond de la classe réévaluée.

Pourquoi : le niveau d’autonomie vaut pour une configuration donnée; Feng, McDonald et Zhang prévoient le renouvellement du certificat d’autonomie à chaque changement de l’agent ou de son environnement**[83]**, et la ligne directrice E-23 du BSIF déclenche une revue indépendante lors de modifications des modèles ou des données**[8]**.

**EXEMPLE**

Un agent de rapprochement de factures fournisseurs de classe modérée, homologué au niveau N3, utilise un modèle dont le fournisseur annonce une nouvelle version. La passerelle de modèles conserve la version épinglée pendant que l’équipe rejoue le jeu d’évaluation sur la nouvelle; la fonction risques et conformité confirme la classe, puis approuve la bascule que le parrain demande, consignée au registre. Si les seuils ne sont pas atteints, l’agent reste sur l’ancienne version. Si le fournisseur retire la version épinglée, l’agent passe au modèle de repli homologué (section 7.8) ou est suspendu à la date du retrait; le préavis contractuel de l’EXIG-APP-13 laisse le temps de l’un ou de l’autre. La rétrogradation à N2 n’est admise que si l’approbation humaine compense le défaut constaté : elle ne corrige pas une erreur de qualité, qu’elle ferait seulement présenter aux approbateurs (section 8.7). Dans une institution financière fédérale, la bascule suit en outre la revue indépendante prévue par E-23.

`EXIG-GOV-13` **· DOIT**

**Attestation périodique du parrain**

Le parrain **DOIT** attester au registre, au moins tous les 12 mois et tous les 6 mois pour un agent de classe élevée, que l’agent est encore requis et que sa finalité, ses mandants, ses portées, sa classe et son niveau d’autonomie restent exacts. L’équipe plateforme **DOIT** revoir chaque trimestre la liste des agents sans parrain actif, sans fiche à jour ou inactifs, et faire passer à l’état « suspendu » ceux qui ne sont pas régularisés. La présente exigence est la seule source du traitement des agents orphelins; l’EXIG-IAM-07 ne s’y ajoute que pour la révocation de leurs justificatifs. L’attestation est approuvée par la fonction risques et conformité, ou par le comité pour la classe élevée (EXIG-GOV-03).

Pourquoi : Microsoft recommande de faire attester par les parrains, tous les 6 à 12 mois, que chaque agent est encore requis, et de revoir chaque trimestre les agents orphelins**[92]**; les périodicités de 12 mois et de 6 mois, inscrites dans la plage que recommande Microsoft, et la revue trimestrielle sont des choix du cadre.

`EXIG-GOV-14` **· DOIT**

**Retrait vérifiable**

Le retrait d’un agent **DOIT** comprendre : la révocation de toutes ses identités, justificatifs et jetons, propagée aux passerelles et aux fournisseurs dans le délai fixé selon l’EXIG-IAM-20 (EXIG-IAM-07); un avis aux consommateurs connus au moins 60 jours avant la fin du service, sauf retrait anticipé pour un motif de sécurité, décidé par le comité et précédé d’une suspension de sécurité (EXIG-INT-14, EXIG-INT-18); le retrait de ses entrées au catalogue; l’archivage de ses journaux d’audit et de ses versions selon les durées de conservation applicables; l’archivage ou la destruction de ses mémoires selon la politique de conservation; une preuve de révocation inscrite au registre. Le préavis de 60 jours est celui de l’EXIG-INT-14, qui en porte le fondement.

Pourquoi : le NIST AI RMF demande des processus de déclassement sécuritaire (GOVERN 1.7)**[74]**, le livre blanc de l’OpenID Foundation recommande un retrait formel propagé, par exemple par une opération SCIM DELETE**[311]**, et les événements CAEP permettent de diffuser la révocation aux parties concernées**[344]**.

## 11.6 Dérogations

Cette section encadre les exceptions au cadre. Une dérogation est une exception écrite, temporaire et compensée; elle n’est jamais une permission tacite. Sans dérogations, un cadre trop rigide pousse les équipes vers des agents fantômes; sans discipline, les dérogations vident le cadre de son contenu.

Une demande de dérogation contient au minimum :

- l’identifiant de chaque exigence visée et le ou les agents ou composants (passerelle, registre, serveur MCP, gabarit) concernés;

- la justification : pourquoi la conformité est impossible ou disproportionnée maintenant;
- le risque résiduel et son effet sur la classe de risque;
- les mesures compensatoires, par exemple un niveau d’autonomie abaissé, une approbation humaine ajoutée, un plafond de coût réduit ou une surveillance renforcée;
- la durée, la date d’échéance et le plan de retour à la conformité;
- le demandeur, les avis reçus et le décideur.

`EXIG-GOV-15` **· DOIT**

**Demande et décision écrites**

Toute dérogation **DOIT** être demandée par écrit, avec le contenu minimal ci-dessus, par le parrain de l’agent visé ou, pour une dérogation qui vise un composant, par le responsable de ce composant ou du domaine, instruite par l’architecture d’entreprise avec l’avis de la sécurité, de la fonction risques et conformité et, s’il y a des RP, du RPRP, puis accordée ou refusée par le comité. Le comité **PEUT** déléguer à l’architecture d’entreprise les dérogations qui visent un agent de classe faible, pour 90 jours au plus (choix du cadre), à la condition que la décision soit prise par une personne autre que celle qui a instruit la demande. La dérogation est inscrite au registre et visible dans la fiche de chaque agent ou composant visé. Une mesure transitoire de cohorte (EXIG-GOV-16) tient lieu de dérogation pour les agents existants qu’elle vise.

Pourquoi : une exception accordée oralement ne se retrouve ni à l’audit ni à l’échéance; la délégation pour la classe faible évite d’engorger le comité.

`EXIG-GOV-16` **· DOIT**

**Durée bornée**

Une dérogation **DOIT** porter une date d’échéance d’au plus six mois. Elle **PEUT** être renouvelée une seule fois, par décision du comité, sur présentation d’un plan de retour à la conformité mis à jour. À l’échéance, l’exigence s’applique de nouveau; si l’agent n’y satisfait pas, il passe à l’état « suspendu » (suspension administrative, section 11.5). Le registre **DOIT** avertir le parrain 30 jours avant l’échéance. Une mesure transitoire de cohorte n’est pas soumise à cette durée : son échéance est liée à un jalon (EXIG-GOV-16). Ces durées sont des choix du cadre.

Pourquoi : une exception sans échéance devient la règle; une exception qu’on veut renouveler plusieurs fois signale plutôt une règle à revoir, ce que tranche la révision semestrielle du cadre (section 1.6).

`EXIG-GOV-17` **· NE DOIT PAS**

**Dérogation à une exigence non dérogeable**

Une dérogation **NE DOIT PAS** autoriser : un niveau d’autonomie NX; l’exécution d’une action P3 sans approbation humaine hors bande (EXIG-AUT-09); l’usurpation d’identité au lieu de la délégation (section 9.3); le relais d’un jeton reçu (EXIG-IAM-12); l’exploitation d’un agent sans fiche complète au registre ou sans parrain nommé, hormis la fiche minimale d’un existant inventorié (EXIG-GOV-16); le dépassement du plafond d’autonomie de la classe de risque (EXIG-CON-02); l’autorisation au-delà de N2 d’un agent qui atteint les seuils de la règle d’or (EXIG-AUT-07); l’exposition simultanée d’un agent à du contenu non fiable, à des systèmes sensibles ou des données privées et à un canal d’envoi sans le retrait de l’EXIG-SEC-06; l’exploitation d’un agent sans journal d’audit (EXIG-OBS-11); ou le manquement à une obligation légale ou réglementaire. Cette liste est la seule qui fasse foi; la grille de l’annexe A en est la projection point par point.

Pourquoi : ces règles protègent contre des dommages irréversibles, dont l’exfiltration est le type, ou contre une responsabilité légale que l’entreprise ne peut pas écarter par une décision interne.

**Régime transitoire et exigibilité (application des EXIG-GOV-16 et EXIG-GOV-17).** (a) Aucun agent **NE DOIT** exercer un palier, un niveau d’autonomie ou une topologie avant que les contrôles qui les conditionnent soient en service et homologués : aucun outil P2 sans compensation déclarée et canal de compensation (EXIG-ORC-17); aucun outil P3 tant que la passerelle ne vérifie pas le jeton d’approbation (EXIG-AUT-12); aucun appel interdomaines hors de la passerelle d’agents, sous la seule tolérance du point (c). (b) Chaque point de la grille de l’annexe A est exigible dès que l’agent exerce la capacité qu’il vise (tout agent, P2 et plus, P3, N3 et plus, interdomaine, multiagent), quelle que soit la phase de la feuille de route; les obligations légales et les points de l’EXIG-GOV-17 sont exigibles immédiatement. (c) Un agent en exploitation à l’adoption du cadre, ou découvert ensuite hors registre, reçoit le statut « existant inventorié » : une fiche minimale (champs de l’étape Proposition, annexe B) et un parrain nommé dans les cinq jours ouvrables qui suivent sa découverte, faute de quoi il est désactivé. Le comité **PEUT** placer une liste de tels agents sous une mesure transitoire de cohorte, par une seule décision dont l’échéance est liée à un jalon de la feuille de route (chapitre 15), et non au délai de l’EXIG-GOV-16. Cette mesure permet l’émission de justificatifs sur la base de la fiche minimale; elle n’admet aucun point de l’EXIG-GOV-17 ni aucune obligation légale, ne couvre jamais un dépassement du plafond de la classe, et limite les appels qui contournent encore la passerelle aux paliers P0 et P1, par des justificatifs en lecture seule chez le système cible. (d) Une échéance externe (loi, autorité) ne bouge pas; une échéance du cadre, comme la migration MCP de l’EXIG-MCP-22, ne change que par une révision du cadre (section 1.6). Le registre est complet lorsque 100 % des agents actifs ont une fiche ouverte et un parrain nommé. Pourquoi : la feuille de route ordonne le travail, mais un contrôle n’existe que lorsqu’il est en service; sans régime de transition, l’annexe B refuserait tout jeton aux agents existants, et la transition reposerait sur des centaines de dérogations instruites une à une.

## 11.7 Gouvernance des standards

Cette section fixe la façon dont le cadre fait évoluer son catalogue des protocoles et standards (section 6.3). Les standards agentiques changent de trimestre en trimestre : sans processus explicite, chaque annonce de fournisseur devient une décision d’architecture improvisée.

Le Cadre européen d’interopérabilité rappelle que l’interopérabilité est régulièrement perturbée par les changements législatifs, organisationnels et technologiques, et qu’elle exige des procédures de gestion du changement**[157]**. Les exemples récents le confirment. La révision 2026-07-28 de MCP a introduit une politique de cycle de vie à trois états (Active, Deprecated, Removed) : une fonctionnalité dépréciée reste au moins douze mois dans la spécification, ou au moins 90 jours en cas de retrait accéléré pour un risque de sécurité actif (avis de sécurité publié ou exploitation documentée)**[34, 196]**. Les conventions sémantiques GenAI d’OpenTelemetry sont au niveau de stabilité Development et peuvent changer sans processus de dépréciation**[181, 188]**. OAuth 2.1 demeure un Internet-Draft**[176]**.

Chaque statut du catalogue emporte une conséquence de gouvernance. « Adopter » désigne le choix par défaut des nouveaux projets. « Évaluer » autorise des pilotes bornés, avec une date de décision. « Surveiller » limite le standard à la veille et aux essais hors production, sans données réelles. « Contenir » laisse un usage existant en production derrière un adaptateur jusqu’à l’échéance de son plan de sortie daté, et interdit tout nouvel usage. « Suspendu », prononcé pour un motif de sécurité, fait cesser immédiatement le service par la passerelle (EXIG-INT-06).

`EXIG-GOV-18` **· DOIT**

**Révision trimestrielle du catalogue**

L’architecture d’entreprise **DOIT** réviser le catalogue des protocoles au moins chaque trimestre et soumettre les changements de statut à l’approbation du comité. Chaque changement est daté et motivé; une dépréciation ou un retrait s’accompagne d’un plan de migration dont l’échéance précède la fin

de la fenêtre de dépréciation annoncée par le standard. Une révision extraordinaire **DOIT** avoir lieu, dans les 15 jours ouvrables (choix du cadre), dès qu’un standard au statut « Adopter » ou « Contenir » publie une version incompatible, une dépréciation, un retrait accéléré ou un correctif de sécurité; une simple annonce de date relève de la révision trimestrielle (section 1.6). Pour les statuts « Évaluer » et « Surveiller », les signaux de veille de l’EXIG-INT-23 s’appliquent, et un avis de sécurité visant un standard au statut « Évaluer » suspend les pilotes qui l’emploient jusqu’à la révision. Un composant sans politique de dépréciation, comme les conventions GenAI d’OpenTelemetry, est épinglé et soumis à un test de non-régression à chaque nouvelle version.

Pourquoi : une fenêtre de dépréciation de douze mois ne protège que l’organisation qui la voit venir et planifie sa migration dès l’annonce.

`EXIG-GOV-19` **· DOIT**

**Critères d’admission d’un standard**

Un standard **DOIT** satisfaire aux six critères suivants, propres au cadre, pour obtenir le statut « Adopter » :

- spécification publique, versionnée et assortie d’une politique de compatibilité et de dépréciation (pour une RFC, le mécanisme Obsoletes et Updates en tient lieu);
- gouvernance neutre ou multipartite (organisme de normalisation ou fondation), et non celle d’un seul fournisseur;
- statut final ou stable (RFC, Recommandation du W3C, version ou révision publiée comme stable); un brouillon, un composant de niveau expérimental ou un composant sans politique de dépréciation n’est admis qu’avec une réserve inscrite au catalogue, qui lève les critères 1 et 3, porte une date de réexamen et l’épingle à une version précise, adossée à un standard publié ou à un mécanisme stable; une extension MCP s’apprécie extension par extension selon son stade (Experimental : non admise; Beta : admise avec réserve; Stable : admise);
- au moins deux mises en œuvre indépendantes, ou une suite de tests de conformité exécutable dans la chaîne d’intégration et épinglée à une étiquette; tant qu’une suite est en préversion (alpha), ses résultats sont consignés et ne sont bloquants que pour les tests restés stables pendant deux versions;
- modèle de sécurité documenté, compatible avec le chapitre 9;
- licence ouverte, sans redevance.

Pourquoi : ces critères écartent les annonces prématurées. L’AAIF, par exemple, n’admet un projet qu’au terme d’un processus formel (proposition publique, triage, recommandation du comité technique, approbation du conseil d’administration, puis formalités juridiques et intégration technique avec la Linux Foundation); une proposition déposée ne suffit pas**[42, 263]** (section 6.9).

`EXIG-GOV-20` **· DOIT**

**Veille désignée et usage encadré**

L’architecture d’entreprise **DOIT** désigner une personne chargée de la veille pour chaque organisme qui fait évoluer un standard du catalogue, au minimum l’AAIF (projets et groupes de travail), l’IETF (groupes OAuth et WIMSE), OpenTelemetry, le W3C, le NIST (son *Center for AI Standards and Innovation*, CAISI, et son *National Cybersecurity Center of Excellence*, NCCoE), l’OWASP GenAI Security Project, l’OpenID Foundation, la CNCF, l’OpenAPI Initiative et AsyncAPI. La fonction risques et conformité **DOIT** de même désigner une personne chargée de la veille réglementaire (CAI, Commissariat à la protection de la vie privée du Canada, BSIF, AMF, Autorités canadiennes en valeurs mobilières (ACVM), Parlement du Canada et Assemblée nationale, Commission européenne). Un protocole, un standard ou une extension

**NE DOIT PAS** être utilisé avec des données réelles, même en pilote, s’il ne figure pas au catalogue au statut « Évaluer » (pilotes seulement) ou « Adopter » ou, pour un usage existant, au statut « Contenir » avec un plan de sortie daté. Le statut « Surveiller » n’admet que des essais sans données réelles, et le statut « Suspendu » aucun usage.

Pourquoi : les pratiques d’identité et de sécurité des agents ne sont pas stabilisées. L’AAIF anime huit groupes de travail, dont identité et confiance, observabilité et traçabilité, gouvernance et alignement réglementaire**[40]**; le CAISI du NIST a lancé le 17 février 2026 l’AI Agent Standards Initiative**[411]**; le groupe WIMSE de l’IETF voit se multiplier les brouillons individuels sur la délégation entre agents**[336]**.

L’entreprise PEUT participer aux consultations publiques et aux groupes de travail pour faire valoir ses besoins; le NCCoE du NIST a, par exemple, publié le 29 septembre 2026 la synthèse des commentaires de plus de 600 intervenants sur son document de réflexion consacré à l’identité et à l’autorisation des agents**[338]**. Le cadre lui-même est révisé chaque semestre par le comité : les dérogations accordées, les incidents et les résultats de la veille alimentent cette révision, et le chapitre 14 situe ces pratiques dans le modèle de maturité.
