# 15 Feuille de route et indicateurs

Ce chapitre ordonne la mise en œuvre du cadre en quatre phases séparées par trois jalons, auxquels s’ajoutent un jalon réglementaire et deux jalons de mise à l’échelle; il la cale sur le calendrier 2027-2030, puis détaille les 90 premiers jours. Il fixe les indicateurs qui permettent au comité d’architecture et des risques agentiques de constater les progrès sur des mesures plutôt que sur des déclarations. Il se termine par les facteurs de succès, puis par les risques de mise en œuvre, chacun assorti de sa parade.

## 15.1 Quatre phases et leurs jalons

La mise en œuvre progresse par phases : chaque phase installe les contrôles dont la suivante a besoin, et l’autonomie accordée aux agents n’augmente qu’une fois ces contrôles en service. La feuille de route est un ordre de planification : le plafond de phase est une condition nécessaire, jamais suffisante, de la hausse d’autonomie, qui exige l’homologation de l’agent (annexe A), et l’exigibilité de chaque contrôle se règle agent par agent, selon les capacités qu’il exerce (EXIG-GOV-16). C’est la logique d’un chantier : on ne monte pas les étages avant d’avoir coulé les fondations.

> **[Figure]**
> - Fondations
> - mois 0 à 3
> - Plateforme
> - mois 3 à 9
> - Industrialisation
> - mois 9 à 18
> - Mise à l’échelle
> - mois 18 et plus
> - Gouvernance Comité, registre Classes de risque, cycle de vie Indicateurs trimestriels, dérogations Cibles chiffrées, revue annuelle
> - Passerelles Pass. modèles Toutes les interactions interdomaines
> - Interopérabilité Inventaire Catalogue, migration MCP Migration des autres intégrations Agents de partenaires
> - Identité et sécurité Fin des clés Identités, jetons délégués Bacs à sable, équipe rouge régulière
> - Observabilité, FinOps Traçage OpenTelemetry Évaluation continue, coût par tâche Routage adaptatif
> - Orchestration Flux durables, approbation Multiagent, sagas et compensation Chorégraphie élargie
> - Conformité EFVP en cours Base de preuves; J2a (annexe III) Certification ISO/IEC 42001
> - Autonomie autorisée N0 et N1 N2, premiers N3 bornés N3 entre domaines, par la passerelle
> - Jalon 1 registre complet,
> - Jalon 2 pilotes homologués,
> - Jalon 3 maturité 3 sur les
> - cinq dimensions
> - Jalon 2a RIA, annexe III,
> - Jalon 4 maturité 4
> - Jalon 5 certificat ISO/IEC 42001
> - Pass. d’agents (P0 à P3)
> - maturité 2, MCP migré comité, dates MCP
> - N4 sur ODD homologué
> - cible 1er nov. 2027
> - EFVP, inventaire E-23

***Figure 28 — Feuille de route : quatre phases et leurs jalons.** Chaque ligne de travail avance d’une phase à l’autre; la dernière ligne indique l’autonomie maximale permise pendant la phase. Les losanges marquent les jalons : le comité constate J1, J2 et J3 avant d’ouvrir la phase suivante, J2a avant l’échéance réglementaire qu’il vise; J4 et J5 mesurent la progression dans la phase Mise à l’échelle. La passerelle d’agents s’ouvre au palier P3, avec l’approbation signée (section 8.5), pendant la phase Plateforme et avant tout agent N2 qui exécute des P3 (tableau 58). Les obligations légales en vigueur (art. 3.3, 12.1 et 17 de la Loi sur le privé) s’appliquent dès l’adoption, quelle que soit la ligne de la figure qui les mentionne. Source : cadre CRE-IA-2026-01 (durées indicatives, à calibrer après l’évaluation de maturité initiale).*

Les durées sont indicatives et se calibrent après l’évaluation de maturité initiale (section 14.2) : une organisation qui exploite déjà une passerelle d’API raccourcira la phase Plateforme; celle qui découvre des dizaines d’agents non inventoriés allongera la phase Fondations. Le troisième jalon marque l’atteinte du niveau 3 de maturité sur les cinq dimensions du chapitre 14, seuil que le cadre retient pour laisser le nombre d’agents croître sans que les risques croissent au même rythme (choix du cadre). Les jalons 4 et 5 donnent à la phase Mise à l’échelle des critères de progression : le niveau 4, qui porte la préparation à la certification ISO/IEC 42001, puis la certification, que le modèle de maturité place au niveau 5 (section 14.3). Le cadre distingue enfin les échéances externes (inventaire E-23, RIA, Loi 25), qui ne bougent pas, des échéances internes à date fixe, comme la migration MCP de l’EXIG-MCP-22, choix du cadre que seul le comité peut déplacer par une révision du cadre (section 1.6).

*Tableau 58 — Phases de mise en œuvre, livrables et autonomie autorisée*

| **Phase** | **Livrables principaux** | **Autonomie autorisée** | **Jalon de sortie** |
| --- | --- | --- | --- |
| **Fondations** mois 0 à 3 | Conformité immédiate des agents existants aux obligations légales en vigueur (art. 3.3, 12.1 et 17 de la Loi sur le privé, notamment), sinon suspension; comité mandaté; inventaire et registre, agents fantômes compris, avec le statut « existant inventorié » et la mesure transitoire de cohorte (EXIG-GOV-16); propriétaire métier nommé pour chaque agent; fin des clés d’API partagées entre agents (remplacées par un secret propre par agent au coffre, sous la mesure transitoire de cohorte, en attendant les identités de charge de travail de la phase Plateforme); passerelle de modèles, qui met fin aux appels directs aux fournisseurs; traçage pilote; catalogue initial des protocoles, chaque serveur et client MCP antérieur y étant inscrit avec sa date de migration (EXIG-MCP-22); premier classement des risques; EFVP manquantes faites, les flux qu’elles visent restant suspendus d’ici là; choix des blocs de solution; coupe-circuit testé. | N0 et N1 seulement : pour les agents, lecture et recommandation (N1), outils P0 et P1, aucun effet en écriture; les flux déterministes (N0) restent régis par leurs contrôles habituels. | **Jalon 1** : registre complet (100 % des agents actifs avec une fiche ouverte et un parrain nommé), comité en fonction; chaque serveur et client MCP antérieur à la révision de référence inscrit au catalogue avec sa date de migration (EXIG-MCP-22); aucune clé partagée entre agents et tous les appels de modèles par la passerelle de modèles (tableau 61). |
| **Plateforme** mois 3 à 9 | Passerelle d’agents ouverte aux outils P0 et P1, puis P2, chacun avec sa compensation déclarée et le canal de compensation (EXIG-ORC-17), puis P3, avec l’approbation signée (section 8.5), avant tout agent N2 qui exécute des P3; catalogue d’entreprise MCP et A2A; migration des serveurs et clients MCP en production vers la révision de référence, au plus tard le 28 juillet 2027 (EXIG-MCP-22); identité par agent et jetons délégués; traçage OpenTelemetry de bout en bout et journal d’audit; moteur d’exécution durable; approbation humaine signée, avec files d’approbation priorisées, rotation des approbateurs et indicateurs de la section 8.7; classement des risques et cycle de vie appliqués à tout nouvel agent; outillage de la transparence envers les personnes (section 12.7; les obligations de l’article 12.1 s’appliquent dès l’adoption); index de preuves (EXIG-CON-18); pour une institution financière fédérale, inventaire E-23 complet, avec la cote de risque et l’état de validation de chaque agent et modèle, au 1er mai 2027 (EXIG-CON-12), les validations étant planifiées selon la cote de risque; premiers pilotes. | N2; premiers N3 bornés au sein d’un même domaine, sur décision du comité, pour des agents de classe faible ou modérée. | **Jalon 2** : pilotes homologués selon l’annexe A; niveau 2 de maturité atteint sur les cinq dimensions; aucun serveur ni client MCP d’une révision antérieure à la révision de référence n’est en production (échéance du 28 juillet 2027 au plus tard, EXIG-MCP-22). |
| **Industrialisation** mois 9 à 18 | Migration des autres intégrations existantes au catalogue, dont les dernières intégrations interdomaines encore hors passerelle, que l’EXIG-ARC-01 interdit déjà et que seule la mesure transitoire de l’EXIG-GOV-16 tolère d’ici là; évaluation continue dans la chaîne d’intégration et de livraison continues (CI/CD); enveloppes budgétaires et imputation par centre de coûts; flux multiagents et sagas à plusieurs systèmes (la compensation des outils P2 est livrée dès la phase Plateforme); bacs à sable pour le code généré; équipe rouge au moins annuelle (EXIG-SEC-23); consolidation outillée de l’index de preuves (EXIG-CON-18). | N3 entre domaines, dans la limite du plafond de chaque classe de risque, pour un agent dont tous les appels interdomaines passent par la passerelle d’agents. | **Jalon 2a** (organisations assujetties au RIA) : au plus tard le 1er novembre 2027, voir l’encadré ci-dessous. **Jalon 3** : niveau 3 de maturité sur les cinq dimensions; cibles chiffrées des indicateurs arrêtées pour J4 (section 15.3). |
| **Mise à l’échelle** mois 18 et plus | Chorégraphie événementielle élargie (CloudEvents, AsyncAPI); agents de partenaires; routage adaptatif des modèles; détection de dérive en continu; système de management de l’IA opéré, audit interne, puis audit de certification ISO/IEC 42001; revue du cadre. | N4 sur un domaine d’exploitation (ODD) homologué par le comité (section 8.1), pour des agents de classe faible, sur décision du comité. | **Jalon 4**, vers le mois 36 : niveau 4 sur les cinq dimensions; quatre trimestres consécutifs où au moins 95 % des agents tiennent leurs seuils contractuels et où chaque indicateur du tableau 61, mesuré pour l’entreprise, tient sa cible chiffrée, et, pour chaque incident grave, contention dans le délai et analyse des causes close; audit interne du SMIA réalisé et audit de certification lancé. **Jalon 5**, vers le mois 48 : certificat ISO/ IEC 42001 obtenu; niveau 5 atteint en interopérabilité et en gouvernance; feuille de route suivante adoptée. Ensuite : revue annuelle de maturité. |

### Règles de progression

- Une phase ne doit pas être ouverte (livrables mis en production, autonomie accrue) avant que le comité ait constaté, sur preuves, le jalon qui la précède. Les travaux préparatoires de la phase suivante peuvent commencer plus tôt, mais aucune hausse d’autonomie n’est permise avant le jalon. Aucun agent n’exerce un palier, un niveau ou une topologie avant que les contrôles qui les conditionnent soient en service et homologués (EXIG-GOV-16).
- Le plafond de la phase se combine avec le plafond de la classe de risque (section 8.1) : le plus strict s’applique. Un agent de classe élevée reste plafonné à N2, même en phase Mise à l’échelle; un agent de classe faible ne dépasse pas N1 tant que le jalon 1 n’est pas franchi.
- Un agent N3 qui agit entre domaines ne doit le faire que par la passerelle d’agents, même avant que la couverture interdomaines atteigne 100 % au jalon 3. Un appel interdomaines qui contourne la passerelle est une non-conformité à l’EXIG-ARC-01 : l’outil visé est retiré à l’agent ou, pour un agent existant inventorié, ramené à la lecture seule (P0 et P1, par des justificatifs en lecture seule chez le système cible) sous la mesure transitoire de l’EXIG-GOV-16, jusqu’à son passage par la passerelle.
- Un agent existant dont le niveau dépasse le plafond de la phase doit être ramené sous ce plafond, par le retrait de ses outils en écriture ou, dès la phase Plateforme, par l’approbation de chacune de ses actions (N2), ou relever de la mesure transitoire de cohorte (EXIG-GOV-16). Cette mesure ne couvre que l’écart entre le plafond de phase et le plafond de classe : un agent au-dessus de son plafond de classe est ramené sous ce plafond ou suspendu sans délai. Elle n’admet aucun point de l’EXIG-GOV-17 ni aucune obligation légale.
- Les travaux qui découlent d’une échéance externe (J2a, inventaire E-23) ou d’une échéance interne à date fixe (migration MCP de l’EXIG-MCP-22, choix du cadre) sont datés par cette échéance, non par la durée des phases; une échéance externe ne bouge pas, une échéance interne ne change que par une révision du cadre (section 1.6). Allonger une phase après l’évaluation initiale ne les reporte pas : ils passent alors en tête de la phase en cours, même s’ils appartiennent à la phase suivante, et le jalon qui précède ne les bloque pas.
- Le comité peut réordonner les travaux d’une phase selon les priorités métier. Il ne doit pas retirer un critère de jalon sans réviser le cadre (section 1.6).

**ATTENTION**

Deux échéances externes et une échéance interne resserrent le calendrier. La ligne directrice E-23 du BSIF, en vigueur le 1er mai 2027 et applicable aux institutions financières fédérales, attend un inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs **[8]**; le cadre y ajoute l’état de validation (EXIG-CON-12) : l’inventaire est complet au jalon 1, puis au 1er mai 2027 avec la cote de risque et l’état de validation de chaque agent et modèle; E-23 ne fixe aucune échéance de validation des modèles existants, et les validations sont planifiées selon la cote de risque. Les serveurs et clients MCP en production doivent avoir migré vers la révision de référence au plus tard le 28 juillet 2027 (EXIG-MCP-22, échéance interne du cadre), avant la fin de la phase Plateforme. Le règlement (UE) 2024/1689, modifié par le règlement (UE) 2026/1744, rend applicables à compter du 2 décembre 2027 les obligations visant les systèmes à haut risque de l’annexe III (au 2 août 2028 pour ceux de l’annexe I) **[57, 58]**; pour une organisation assujettie qui adopte le cadre à l’automne 2026, cette date tombe entre les jalons 2 et 3; les dates qui découlent du règlement (UE) 2026/1744 sont à confirmer sur le texte publié au Journal officiel avant de geler le jalon 2a. Les obligations déjà en vigueur, comme les articles 3.3, 12.1 et 17 de la Loi sur le privé, ne suivent pas le rythme des phases et ne souffrent aucune dérogation (EXIG-GOV-17) : un agent qui n’y satisfait pas est suspendu jusqu’à sa mise en conformité.

**JALON 2A — CONFORMITÉ AU RIA, ANNEXE III**

Pour une organisation assujettie au RIA (section 12.4), le comité constate au plus tard le 1er novembre 2027, sur preuves :

- la liste des agents qui relèvent de l’annexe III, avec l’applicabilité consignée selon l’usage des sorties dans l’Union (EXIG-CON-13);
- pour chacun, la revue de requalification en fournisseur faite (EXIG-CON-15) et, si l’organisation est fournisseur, les obligations du fournisseur en place (section 12.4);
- pour chacun, les obligations du déployeur en place (EXIG-CON-16), dont une conservation des journaux configurée pour au moins six mois (art. 26(6) du RIA; 24 mois pour le journal d’audit, EXIG-OBS-13);
- les preuves référencées à l’index de preuves (EXIG-CON-18).

À compter du 2 décembre 2027, les sorties d’un agent visé qui ne satisfait pas à ces critères ne doivent pas être utilisées dans l’Union, même s’il a été mis en service avant cette date (choix du cadre, plus strict que le régime transitoire de l’art. 111 du RIA). J2a n’ouvre aucune phase et n’accorde aucune autonomie.

### Calage sur le calendrier 2027-2030

Le tableau 59 cale la feuille de route sur une adoption du cadre à l’automne 2026 : évaluation de maturité initiale en novembre 2026, ouverture de la phase Fondations le 1er décembre 2026 (mois 0). Un autre point de départ décale toutes les dates, sauf celles qui découlent d’une échéance externe. L’entreprise refait ce calage après l’évaluation initiale.

*Tableau 59 — Calage indicatif, mois 0 au 1er décembre 2026*

| **Période** | **Phase ou jalon** | **Échéances externes à tenir** |
| --- | --- | --- |
| Déc. 2026 – mi-mars 2027 | Fondations, congés des fêtes compris | — |
| Mi-mars 2027 | **J1** | — (signal de veille, non une échéance : l’ébauche OAuth 2.1 épinglée au catalogue est réépinglée à chaque nouvelle révision; la référence normative reste OAuth 2.0) |
| Mi-mars – fin sept. 2027 | Plateforme, vacances de la construction comprises | Inventaire E-23 le 1er mai 2027; échéance interne de la migration MCP le 28 juillet 2027 (EXIG-MCP-22), à terminer avant les vacances de la construction si l’entreprise les observe |
| Début oct. 2027 | **J2** | — |
| 1er nov. 2027 au plus tard | **J2a** (cible interne du cadre) | RIA, annexe III, le 2 décembre 2027 |
| Oct. 2027 – juin 2028 | Industrialisation | — |
| Début juill. 2028 | **J3** | RIA, annexe I, le 2 août 2028 |
| Juill. 2028 – 2030 | Mise à l’échelle | Examen formel du NIST AI RMF au plus tard en 2028 (révision extraordinaire du cadre, section 1.6) |
| Déc. 2029 | **J4** | — |
| Déc. 2030 | **J5** | — |

Une phase de six mois ou moins qui chevauche une période de congés collectifs (fêtes de fin d’année, vacances de la construction) s’allonge de la durée de cette période, environ deux semaines chacune; le tableau 59 en tient compte. Les durées des phases plus longues et les échéances de J4 et J5 incluent déjà les congés. Les périodes de congés collectifs sont un paramètre de l’entreprise; celles du tableau 59 sont des exemples. Les échéances externes ne bougent pas : l’inventaire E-23 reste exigible le 1er mai 2027. La migration MCP du 28 juillet 2027 est une échéance interne du cadre (EXIG-MCP-22), qui ne change que par une révision du cadre (section 1.6). Le cadre ne prévoit pas de jalon propre à l’annexe I du RIA : un agent intégré à un produit réglementé de l’annexe I (2 août 2028) suit les critères du jalon 2a, que le comité constate au plus tard le 1er juillet 2028.

## 15.2 Les 90 premiers jours

Les « 90 premiers jours » désignent les 13 premières semaines travaillées; ils forment la phase Fondations. Ils ne servent pas à construire de nouveaux agents, mais à rendre visibles et gouvernables ceux qui existent, puis à ouvrir une voie approuvée assez simple pour que personne n’ait intérêt à la contourner. L’inventaire répond aussi à la sous-catégorie GOVERN 1.6 du NIST AI RMF, qui demande des mécanismes d’inventaire des systèmes d’IA **[74]**. Une période de congés collectifs s’ajoute à ces 13 semaines (section 15.1, tableau 60).

*Tableau 60 — Plan des 90 premiers jours (phase Fondations)*

| **Semaines** | **Travaux** | **Livrable vérifiable** | **Responsable** |
| --- | --- | --- | --- |
| 1 et 2 | Mandater le comité et nommer ses membres; associer le responsable de la protection des renseignements personnels (art. 3.1 de la Loi sur le privé, modifiée par la Loi 25) **[56]**; lancer l’inventaire des agents internes, des logiciels-services à agents intégrés, des serveurs MCP, des assistants dotés d’outils et des agents de partenaires, y compris les agents fantômes repérés dans les journaux réseau, les consentements OAuth et les consoles des logiciels-services; tout agent découvert reçoit dans les cinq jours ouvrables une fiche minimale et un parrain nommé, faute de quoi il est désactivé (EXIG-GOV-16). | Mandat du comité; inventaire brut | Architecture d’entreprise, sécurité |
| 3 et 4 | Ouvrir une fiche par agent (champs de l’étape Proposition, annexe B), au statut « existant inventorié »; nommer un propriétaire métier pour chacun; faire adopter par le comité la mesure transitoire de cohorte qui vise la liste des agents existants (EXIG-GOV-16); recenser les clés d’API et les comptes de service utilisés par des agents; repérer les décisions fondées exclusivement sur un traitement automatisé (art. 12.1 de la Loi sur le privé), dont l’obligation d’informer s’applique déjà, par des moyens manuels au besoin, sans attendre l’outillage de la phase Plateforme. Pour une institution financière fédérale, marquer à la fiche les agents et les modèles qui relèvent de l’inventaire E-23. | Registre initial; décision de cohorte; liste des agents sans propriétaire métier; inventaire des secrets; liste des décisions visées par l’article 12.1 | Propriétaires métier, équipe plateforme |
| 5 et 6 | Mettre en service la passerelle de modèles et y basculer tous les appels aux fournisseurs; remplacer chaque clé partagée par un secret propre à l’agent, conservé au coffre et injecté à l’exécution, en attendant les identités de charge de travail de la phase Plateforme; ce secret transitoire relève de la mesure transitoire de cohorte (EXIG-GOV-16), sans dérogation agent par agent à l’EXIG-IAM-05. La fuite de secrets, les secrets de longue durée et la réutilisation d’une même identité figurent au Top 10 OWASP des identités non humaines **[91]**. | Aucun appel direct à un fournisseur de modèles; aucune clé partagée entre agents | Équipe plateforme, sécurité |
| 7 et 8 | Instrumenter deux ou trois agents représentatifs avec OpenTelemetry (version épinglée des conventions GenAI, section 10.1), centre de coûts compris; publier le catalogue initial des protocoles (section 6.3) et y inscrire les premiers outils avec leur palier P0 à P3; inscrire chaque serveur et client MCP antérieur à la révision de référence avec sa date de migration, au plus tard le 28 juillet 2027 (EXIG-MCP-22); ouvrir, sur un banc d’essai de l’entreprise, les essais reproductibles des candidats aux blocs de la phase Plateforme (EXIG-APP-03, EXIG-APP-04, EXIG-APP-06). | Traces de bout en bout, du canal au modèle; catalogue initial publié; plan de migration MCP; banc d’essai des candidats ouvert | Équipe plateforme, architecture d’entreprise |
| 9 et 10 | Classer chaque agent inventorié (classe faible, modérée ou élevée) et fixer son plafond d’autonomie; repérer les agents qui traitent des RP ou les communiquent hors du Québec; toute communication hors du Québec sans EFVP (art. 17) est suspendue jusqu’à ce que l’EFVP soit faite, et les EFVP des projets en cours (art. 3.3) sont lancées **[413]**; repérer les agents qui relèvent de l’annexe III du RIA; ramener sous le plafond de phase les agents qui le dépassent. | Classe et plafond inscrits pour tous les agents; flux hors Québec couverts par une EFVP ou suspendus; EFVP des projets en cours lancées; liste des agents visés par l’annexe III | Risques et conformité, responsable de la protection des RP, propriétaires métier |
| 11 | Choisir les blocs de solution de la phase Plateforme (passerelle d’agents, moteur d’exécution durable, registre d’entreprise, qui prolonge le registre initial des semaines 3 et 4) avec la grille de la section 13.4, appliquée aux essais du banc d’essai ouvert aux semaines 7 et 8; les preuves qui supposent un agent pilote (export FOCUS d’un mois, essai de restitution) sont cotées provisoirement sur la démonstration du fournisseur et confirmées au premier pilote de la phase Plateforme; documenter le coupe-circuit, externe à l’agent **[353]**, puis l’exercer sur un agent réel en mesurant le délai de révocation. | Décision de plateforme, avec ses notes provisoires; rapport d’exercice du coupe-circuit | Architecture d’entreprise, équipe plateforme, sécurité |
| 12 et 13 | Mesurer la valeur de référence des indicateurs (tableau 61); tenir la revue du jalon 1; arrêter le plan de la phase Plateforme et choisir les pilotes, en plaçant en tête la migration MCP et, s’il y a lieu, l’inventaire E-23; recaler le tableau 59 sur la date réelle du jalon 1. | Procès-verbal du jalon 1; tableau de bord de référence; calendrier recalé | Comité, architecture d’entreprise |

**À RETENIR**

Bloquer les agents sans offrir d’autre voie pousse les employés vers l’IA fantôme *(shadow AI)*, constate Gartner (avril 2026) **[2]**. Dès la sixième semaine, la passerelle de modèles et une inscription rapide au registre offrent une voie approuvée plus simple que le contournement.

## 15.3 Indicateurs

Les indicateurs servent à constater les jalons et à piloter l’autonomie sur des mesures. Ils obéissent à cinq règles du cadre :

- chaque indicateur doit être calculé à partir du registre, des passerelles, des traces et du journal d’audit ou, pour les exercices et les incidents, d’enregistrements horodatés, et non déclaré par les équipes; une donnée qui ne peut pas se calculer ainsi (coût du processus de référence, intervention imprévue) est une donnée attestée, établie par la fonction qui en répond (la finance pour un coût), datée, versée à la fiche et signalée comme telle au tableau 61;

- la valeur de référence est mesurée au jalon 1 pour la couverture du registre, les secrets et la passerelle de modèles, et, pour les autres indicateurs, au premier trimestre qui suit le jalon 1 ou la mise en service de leur source; les indicateurs sont ensuite présentés chaque trimestre au comité, par agent, par domaine et pour l’entreprise;
- les cibles du tableau 61 sont des choix du cadre; le comité peut les ajuster par écrit, avec justification, sauf celles qui reprennent une exigence, qui ne s’écartent que par dérogation (section 11.6) : couverture du registre (EXIG-GOV-07), secrets (EXIG-IAM-05), passerelles (EXIG-ARC-01, EXIG-IAM-17), conformité au catalogue (EXIG-INT-04, EXIG-INT-06, EXIG-MCP-22), traçabilité (EXIG-OBS-11) et couverture de l’évaluation (EXIG-EVA-01); la cible de l’EFVP reprend une obligation légale et ne s’écarte jamais (EXIG-GOV-17);
- à la revue du jalon 3, le comité remplace par une valeur chiffrée chaque cible exprimée comme une tendance (« en baisse », « en hausse »), à partir des séries trimestrielles disponibles; ces valeurs sont les cibles que le jalon 4 vérifie;
- chaque indicateur a un responsable de mesure, nommé par le comité parmi les rôles de la section 11.1; le tableau 61 propose le rôle qui opère la source de la donnée.

*Tableau 61 — Indicateurs de mise en œuvre et cibles proposées*

| **Indicateur** | **Définition** | **Cible proposée** | **Fréquence** | **Responsable de mesure (proposé)** |
| --- | --- | --- | --- | --- |
| Couverture du registre | Part des agents actifs, déclarés ou découverts, qui ont une fiche à jour au registre | 100 % | Mensuelle | Équipe plateforme |
| Découverte d’agents hors registre | Nombre d’agents découverts hors registre par trimestre, et délai entre leur première trace ou leur premier consentement OAuth et leur inscription | En baisse; inscription en cinq jours ouvrables au plus (EXIG-GOV-16) | Trimestrielle | Équipe plateforme |
| Agents sans secret partagé | Part des agents qui s’authentifient avec un justificatif qui leur est propre, sans clé partagée ni compte d’une personne | 100 % au jalon 1 | Mensuelle | Sécurité de l’information |
| Couverture des passerelles | Dans tout environnement autre qu’un poste de développement individuel, part des appels de modèles, de tous les appels MCP et A2A, quel que soit le domaine, de tous les accès à une ressource d’un autre domaine et de toutes les actions P2 et P3 qui passent par la passerelle de modèles ou d’agents (portée de l’EXIG-ARC-01 et de l’EXIG-IAM-17); seules les fonctions locales P0 et P1 dispensées par ces exigences sont exclues du dénominateur | Modèles : 100 % au jalon 1; MCP, A2A, accès à un autre domaine, P2 et P3 : 100 % des nouveaux agents dès leur homologation, 100 % des agents existants au jalon 3 (mesure transitoire de l’EXIG-GOV-16 d’ici là) | Mensuelle | Équipe plateforme |
| Conformité au catalogue | Part des intégrations d’agents qui utilisent un protocole et une version inscrits au catalogue | 100 % des nouveaux agents; serveurs et clients MCP en production : 100 % sur la révision de référence au 28 juillet 2027; 100 % des agents existants au jalon 3 | Trimestrielle | Architecture d’entreprise |
| Traçabilité | Part des actions à effet (P2 et P3) rattachées à une trace complète, à leur mandant et à une entrée du journal d’audit | 100 % dès l’ouverture des outils P2 et P3 à la passerelle d’agents (phase Plateforme) : aucun effet sans journal d’audit (EXIG-OBS-11, non dérogeable) | Mensuelle | Équipe plateforme |
| Couverture de l’évaluation | Part des agents en production dont le jeu de référence s’exécute dans la chaîne CI/CD et atteint ses seuils (section 10.4) | 100 % des nouveaux agents dès la mise en service de la chaîne CI/CD (phase Industrialisation; d’ici là, forme minimale déclarée à la fiche, annexe A); 100 % des agents existants au jalon 3 (mesure transitoire de cohorte d’ici là) | Trimestrielle | Équipe d’évaluation |
| Réussite des tâches | Tâches réussies sans intervention humaine imprévue (escalade que le contrat d’agent ne prévoit pas; donnée attestée), sur le total des tâches, par agent | Seuil fixé au contrat d’agent | Mensuelle | Responsable technique de chaque agent |
| Escalade humaine | Part des tâches renvoyées à une personne | Fourchette fixée au contrat d’agent; tout écart s’analyse | Mensuelle | Responsable technique de chaque agent |
| Approbation sans modification | Par approbateur et par file : part des demandes approuvées telles quelles, avec le temps de réponse médian | Seuil d’alerte fixé par cas d’usage; tout écart marqué par rapport à la norme s’analyse | Mensuelle | Équipe plateforme (EXIG-AUT-21) |
| Incidents agentiques | Nombre d’incidents par gravité (S1 à S4, attribuée par la fonction risques et conformité, section 12.8), avec les délais de détection et de contention | Taux d’incidents graves par millier de tâches, chiffré au jalon 3; pour chaque incident grave, contention dans le délai et analyse des causes close; délais en baisse | Trimestrielle | Risques et conformité |
| Délai de révocation en exercice | Temps écoulé entre la décision d’arrêter un agent et le refus de son dernier appel, dans tous les systèmes, mesuré lors de l’exercice trimestriel de l’EXIG-SEC-26 et décomposé en délai de refus aux passerelles et en exposition résiduelle des systèmes sans révocation active (durée de vie maximale des jetons qu’ils acceptent, EXIG-IAM-15) | Cible fixée par l’entreprise (EXIG-IAM-20), proposée à 15 minutes, puis en baisse; liste des systèmes sans révocation active publiée | Trimestrielle | Sécurité de l’information |
| Délai d’intégration | Temps écoulé entre l’inscription d’une demande de branchement d’un outil déjà inscrit au catalogue et le premier appel réussi de l’agent vers cet outil, relevé dans les traces | En baisse d’un trimestre à l’autre, puis valeur chiffrée au jalon 3 | Trimestrielle | Équipe plateforme |
| Réutilisation | Nombre moyen d’agents consommateurs par outil du catalogue | En hausse, puis valeur chiffrée au jalon 3 | Trimestrielle | Équipe plateforme |
| Coût par tâche réussie | Coût total imputé (inférence, outils, quote-part de la plateforme) divisé par le nombre de tâches réussies, en dollars canadiens; la quote-part est suivie à part, et l’arrêt d’un pilote se décide sur le coût marginal, hors quote-part | Inférieur au coût du processus de référence sans agent (donnée attestée); écart chiffré au jalon 3 | Mensuelle | Équipe FinOps |
| EFVP à jour | Part des agents traitant des RP dont l’EFVP couvre la version en production | 100 % des nouveaux agents dès leur homologation (EXIG-CON-04); 100 % des agents existants au jalon 1, les flux visés restant suspendus d’ici là (tableau 58) | Trimestrielle | Responsable de la protection des RP |

La cible proposée de 15 minutes pour la révocation est un choix du cadre, que l’entreprise ajuste en fixant son propre délai maximal (EXIG-IAM-20, seule source de la cible). Le délai de refus aux passerelles et l’exposition résiduelle d’un système sans révocation active sont deux grandeurs distinctes : un jeton émis juste avant la désactivation reste utilisable jusqu’à son expiration chez un tel système. C’est pourquoi l’EXIG-IAM-15 borne à la cible la durée de vie des jetons destinés à ces systèmes, ou ne les rend joignables que par la passerelle. La cible de révocation concrétise la sous-catégorie MANAGE 2.4 du NIST AI RMF, qui demande des mécanismes pour désengager ou désactiver un système dont le comportement s’écarte de l’usage prévu **[74]**. Le coût par tâche réussie est d’abord présenté en refacturation indicative *(showback)*, modèle que recommande la FinOps Foundation **[407]**; le passage à la refacturation réelle relève du comité (EXIG-FIN-09).

**ATTENTION**

Un indicateur ne se lit jamais seul. Un taux d’escalade très bas peut signifier qu’un agent tranche des cas qu’il devrait renvoyer. Un taux élevé d’approbation sans modification, joint à des temps de réponse très courts, peut signaler une approbation machinale : l’Infocomm Media Development Authority (IMDA) de Singapour recommande de surveiller ces deux signaux **[76]**. Une cible déclenche une analyse; elle ne sert pas à récompenser une équipe.

## 15.4 Facteurs de succès et risques de mise en œuvre

Les données publiques invitent à la prudence : selon Gartner (juin 2025), plus de 40 % des projets d’IA agentique seront annulés d’ici la fin de 2027 en raison de coûts croissants, d’une valeur d’affaires incertaine ou de contrôles des risques inadéquats **[3]**. Les facteurs suivants visent directement ces trois causes.

### Facteurs de succès

1. **Un parrainage de direction et un comité qui décide.** Un comité seulement consultatif ne peut ni constater les jalons ni accorder les dérogations.
2. **La plateforme avant la multiplication des agents.** Gartner (avril 2026) estime qu’une entreprise moyenne du Fortune 500 aura plus de 150 000 agents en usage d’ici 2028, contre moins de 15 en 2025 **[2]**. Cet ordre de grandeur prospectif **[467]** laisse prévoir qu’un contrôle agent par agent ne tiendra pas : passerelles, catalogue et gabarits doivent précéder la croissance.
3. **Une gouvernance proportionnée.** Selon Gartner (mai 2026), appliquer la même gouvernance à tous les agents mènera à des échecs, et 40 % des entreprises rétrograderont ou désactiveront des agents autonomes d’ici 2027 à cause de lacunes révélées seulement après des incidents en production **[95]**. Le cadre gradue donc les contrôles selon la classe de risque, le niveau d’autonomie et le palier d’outil (sections 8.4 et 12.1).
4. **Commencer simple.** Anthropic recommande la solution la plus simple possible **[6]**; une architecture multiagent consomme de 3 à 10 fois plus de jetons qu’un agent unique selon [275] **[275]**, et environ 3,75 fois selon les mesures d’Anthropic (environ 15 fois une conversation contre environ 4 fois pour un agent) **[17]**. Les premiers pilotes retiennent un flux déterministe ou un agent unique outillé.
5. **Mesurer la valeur dès le pilote.** Chaque pilote compare son coût par tâche réussie à celui du processus de référence; un pilote qui ne fait pas mieux s’arrête ou se redéfinit.
6. **Concevoir la supervision au lieu de la présumer.** Le biais d’automatisation touche les novices comme les experts et ne se prévient pas par la seule formation **[314]**. Les files d’approbation, les seuils et les indicateurs de la section 8.7 font partie des livrables de la phase Plateforme.

### Risques et parades

Le tableau 62 synthétise les principaux risques de mise en œuvre, leurs signes avant-coureurs et leurs parades.

*Tableau 62 — Risques de mise en œuvre, signes avant-coureurs et parades*

| **Risque** | **Signe avant-coureur** | **Parade prévue par le cadre** |
| --- | --- | --- |
| Abandon faute de valeur démontrée | Pilotes sans processus de référence ni coût par tâche | Indicateur de valeur obligatoire à la fiche; arrêt des pilotes non concluants |
| Plateforme centrale devenue goulot | Délai d’intégration en hausse; contournements | Modèle en étoile et libre-service par gabarits (section 11.3) |
| Prolifération et IA fantôme | Agents découverts hors registre; consentements OAuth inconnus | Inventaire continu; voie approuvée simple; désactivation des agents sans fiche |
| Gouvernance uniforme | Mêmes contrôles pour un agent N1 et un agent N3; files d’approbation saturées | Contrôles gradués par classe, par niveau et par palier (section 8.4) |
| Approbation machinale | Taux élevé d’approbation sans modification; temps de réponse très courts | Files priorisées par risque, regroupement, rotation des approbateurs (section 8.7) |
| Instabilité des standards | Nouvelle révision de MCP; conventions GenAI d’OpenTelemetry encore au niveau Development | Versions épinglées au catalogue; révision trimestrielle (section 11.7) |
| Migration MCP manquée | Serveurs ou clients MCP antérieurs encore en production à trois mois de l’échéance du 28 juillet 2027; serveurs sans date de migration au catalogue | Plan de migration dès la phase Fondations; migration en tête de la phase Plateforme; critère du jalon 2 (EXIG-MCP-22) |
| Phase Plateforme allongée | Livrables de la phase en retard sur le calendrier recalé; jalon 2 qui glisse au-delà d’octobre 2027 | Travaux datés par leur échéance externe (règles de progression); travaux réglementaires en tête de phase; réordonnancement par le comité |
| Verrouillage par une plateforme | Extensions propriétaires; données ou mémoires non exportables | Clauses contractuelles du chapitre 13 |
| Dérive des coûts | Coût par tâche en hausse; boucles qui atteignent leurs plafonds | Enveloppes budgétaires et routage frugal (section 10.6) |
| Échéance réglementaire manquée | Agent à haut risque dont la mise en service est prévue à compter du 2 décembre 2027; EFVP non commencée; inventaire E-23 sans état de validation à l’approche du 1er mai 2027 | Jalon J2a; inventaire E-23 complet en phase Plateforme; priorité dans chaque phase; évaluation d’impact unifiée (section 12.9) |
