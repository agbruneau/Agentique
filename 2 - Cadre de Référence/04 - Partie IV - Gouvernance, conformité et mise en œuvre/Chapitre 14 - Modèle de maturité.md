# 14 Modèle de maturité

Ce chapitre situe l’entreprise sur cinq niveaux de maturité et cinq dimensions, pour mesurer l’écart entre ses pratiques et le cadre. Il fixe la méthode d’évaluation, les preuves attendues et le lien entre la maturité, les jalons et l’autonomie permise, puis relie le modèle à ISO/IEC 42001 et au NIST AI RMF. Il n’ajoute aucune exigence.

## 14.1 Cinq niveaux et cinq dimensions

Cette section définit l’échelle. Chaque niveau, à partir du niveau 2, fixe des critères observables; le niveau 1 est le niveau plancher, sans critère, que décrivent des pratiques typiques. Les niveaux sont cumulatifs : atteindre le niveau 3 suppose de satisfaire aussi aux critères du niveau 2. Les cinq dimensions reprennent les piliers du cadre : interopérabilité (chapitre 6), orchestration et supervision humaine (chapitres 7 et 8), identité et sécurité (chapitre 9), observabilité, évaluation et coûts compris (chapitre 10), et gouvernance (chapitres 11 à 13).

> **[Figure]**
> - 1 Initial
> - Connecteurs ad hoc, clés partagées, aucun inventaire
> - 2 Reproductible
> - Premiers serveurs MCP, identité par agent, traces
> - 3 Défini
> - Catalogue d’entreprise, passerelle, jetons délégués, traçage de bout en bout, cycle de vie à contrôles
> - 4 Géré
> - Multiagent en production, sagas, autorisation fine, évaluation continue, coût
> - 5 Optimisé
> - Confiance vérifiable entre organisations, autonomie ajustée par les
> - Niveau global = dimension la plus faible (interopérabilité, orchestration, identité, observabilité, gouvernance)
> - par tâche, préparation ISO/IEC 42001
> - mesures, revue externe ou ISO/IEC 42001
> - par projet, registre en partie manuel
> - Cible de la feuille de route : 18 mois environ

***Figure 27 — Modèle de maturité en cinq niveaux.** Chaque niveau englobe les précédents; la feuille de route vise le niveau 3, « Défini », en 18 mois environ (durée indicative, à calibrer après l’évaluation initiale). Le niveau global de l’entreprise est celui de sa dimension la plus faible. Source : cadre CRE-IA-2026-01.*

Le passage du niveau 2 au niveau 3 tient d’abord à la portée des pratiques : au niveau 2, à l’exception du registre, de l’identité et de la passerelle de modèles, qui couvrent déjà tous les agents, elles visent surtout les nouveaux agents et les pilotes; au niveau 3, elles forment la norme unique de tout le portefeuille. Le niveau 4 ajoute le pilotage par les mesures; le niveau 5, l’amélioration continue et la confiance étendue aux partenaires.

*Tableau 55 — Niveaux de maturité par dimension*

| **Niveau** | **Interopérabilité** | **Orchestration et supervision** | **Identité et sécurité** | **Observabilité** | **Gouvernance** |
| --- | --- | --- | --- | --- | --- |
| **1 — Initial** Niveau plancher, sans critère; pratiques typiquement improvisées par chaque équipe | Connecteurs ad hoc, propres à chaque projet | Invites et scripts isolés; logique métier confiée au modèle | Clés d’API et comptes de service partagés | Journaux locaux; coûts inconnus | Aucun inventaire; agents fantômes |
| **2 — Reproductible** Pratiques établies et répétées | Tous les serveurs MCP et toutes les cartes d’agent des pilotes au catalogue, versions épinglées; contrats pour les outils des pilotes | Flux déterministes à étapes agentiques; patron documenté par agent; exécution durable des pilotes; approbation signée de toute action P3 | Identité propre à chaque agent, aucune clé partagée; secrets au coffre; passerelle de modèles; coupe-circuit exercé | Traces OpenTelemetry par projet; journal d’audit des pilotes; coûts suivis par agent | Registre complet, tenu en partie à la main; parrain nommé pour chaque agent; comité en fonction; classes de risque attribuées |
| **3 — Défini** Pratiques normalisées pour tout le portefeuille | Catalogue d’entreprise unique; MCP et A2A pour tout nouvel agent; intégrations existantes migrées | Patrons autorisés et gabarits; moteur d’exécution durable; compensation définie pour chaque étape à effet; plafonds d’itérations; taux d’approbation sans modification suivi par approbateur (section 8.7) | Passerelle d’agents pour tout appel MCP ou A2A et toute action P2 ou P3; jetons délégués; garde-fous communs; bacs à sable; équipe rouge au moins annuelle pour chaque agent de classe modérée ou élevée (EXIG-SEC-23) | Traçage de bout en bout; journal d’audit de toute action P2 et P3; évaluation dans la chaîne CI/CD; enveloppes budgétaires | Cycle de vie à jalons pour tous les agents; aucun justificatif sans fiche complète; dérogations bornées; clauses de réversibilité du chapitre 13 dans tout contrat d’acquisition |
| **4 — Géré** Pratiques pilotées par les mesures | Systèmes clés exposés au catalogue; versions gérées; formats CloudEvents et contrats AsyncAPI des chorégraphies; réutilisation mesurée chaque trimestre (tableau 61) | Multiagent en production là où un gain est mesuré; agents ambiants réautorisés selon la section 8.6; sagas éprouvées par injection de fautes; routage des modèles selon les mesures | Autorisation fine par politiques en code; délai de révocation mesuré en exercice, sous la cible de l’EXIG-IAM-20 | Évaluation continue, production comprise; détection de la dérive; coût par tâche réussie suivi | Indicateurs trimestriels utilisés dans les décisions du comité; préparation à la certification ISO/IEC 42001 |
| **5 — Optimisé** Amélioration continue, confiance étendue aux partenaires | Interopérabilité avec les partenaires; vocabulaire sémantique partagé | Chorégraphie interdomaines; autonomie ajustée selon les mesures, à la hausse comme à la baisse | Confiance vérifiable entre organisations : cartes signées, fédération des identités et de la délégation | Incidents et dérives versés aux jeux d’évaluation; décisions fondées sur la valeur et le risque mesurés | Révision du cadre alimentée par les incidents, les dérogations et la veille (section 11.7); revue externe ou certification ISO/IEC 42001 |

**À RETENIR**

Un niveau de maturité qualifie l’entreprise; un niveau d’autonomie (N0 à N4, section 8.1) qualifie un agent. L’autonomie n’est pas un objectif de maturité : Feng, McDonald et Zhang en font une décision de conception, et Morris et coll. rappellent que le niveau retenu au déploiement n’a pas à être le maximum que permettent les capacités du modèle**[83, 302]**. Une entreprise au niveau 5 peut garder la plupart de ses agents à N1 ou à N2.

## 14.2 Évaluer sa maturité

Cette section fixe la cotation, le calendrier et les preuves admises. Le but est un résultat reproductible, que le cadre mesure au lieu de le supposer : à chaque évaluation de jalon, deux évaluateurs indépendants cotent les mêmes preuves, leur accord est calculé (coefficient kappa), et un désaccord est tranché par le comité et consigné.

### Règles de cotation

- Une dimension atteint un niveau lorsque ses critères, et ceux du niveau inférieur, sont satisfaits dans tout le périmètre qu’ils désignent; un critère qui ne désigne pas son périmètre vise, au niveau 2, les agents des pilotes et, au niveau 3 et au-delà, tous les agents en production.
- Le niveau global est celui de la dimension la plus faible. Une entreprise dotée d’un catalogue exemplaire, mais dont des agents partagent encore des clés d’API, reste au niveau 1 : un incident emprunte le maillon le plus faible.
- Un critère se prouve par des données du registre, des passerelles, des traces et du journal d’audit, comme les indicateurs du tableau 61; une déclaration d’équipe n’est pas une preuve. Pour les critères qui ne se calculent pas automatiquement, l’évaluateur examine les listes de contrôle de l’annexe A d’un échantillon qui comprend tous les agents de classe élevée, tous les agents N4 et au moins 20 % des autres agents de chaque classe, tirés au hasard; le tirage est consigné.

### Calendrier et conduite

Une première évaluation précède la phase Fondations et calibre les durées de la feuille de route (section 15.1); faute de registre, elle s’appuie sur une découverte outillée (journaux du fournisseur d’identité et de facturation, trafic sortant vers les fournisseurs de modèles), recalibrée au jalon 1. Avant la constitution du comité (tableau 60, semaines 1 et 2), le parrain de direction de la feuille de route (section 15.4) arrête cette évaluation initiale, et le comité la ratifie à sa première séance. Une évaluation a lieu ensuite à chaque jalon : le jalon 2 exige le niveau 2 sur les cinq dimensions, le jalon 3 le niveau 3 (tableau 58). Après le jalon 3, l’entreprise refait l’évaluation chaque année, par autoévaluation selon les tableaux 55 et 56; l’évaluation des jalons 4 et 5 est conduite par l’architecture d’entreprise.

L’architecture d’entreprise conduit l’évaluation avec les fonctions qui répondent de chaque dimension; le comité en arrête le résultat, comme il constate les jalons. Ce résultat donne le niveau de chaque dimension, ses preuves et le plan d’action qui comble les écarts; le recul d’une dimension sous le niveau du dernier jalon franchi ramène les agents concernés au plafond de la phase correspondante, sauf dérogation bornée (section 11.6), et un indicateur du tableau 61 hors cible déclenche la réévaluation de la dimension sans attendre l’évaluation annuelle. Une phase peut livrer des capacités d’un niveau supérieur : la phase Industrialisation livre des flux multiagents et des sagas, dont l’exploitation éprouvée (gain mesuré, essais par injection de fautes) relève du niveau 4 en orchestration, alors que le jalon 3 ne vérifie que le niveau 3.

### Preuves attendues

Le tableau 56 résume les preuves attendues par niveau de maturité.

*Tableau 56 — Preuves attendues par niveau de maturité*

| **Niveau** | **Exemples de preuves** |
| --- | --- |
| 2 — Reproductible | Couverture du registre à 100 %; aucun agent sans justificatif propre; tous les appels de modèles par la passerelle; catalogue publié; traces des pilotes; rapport d’exercice du coupe-circuit; pilotes homologués selon l’annexe A. |
| 3 — Défini | Conformité au catalogue et couverture des passerelles à 100 % (appels MCP et A2A, actions P2 et P3), agents existants compris; traçabilité de toutes les actions P2 et P3; couverture de l’évaluation à 100 %; jalons du cycle de vie consignés pour chaque agent (EXIG-GOV-11); rapports d’équipe rouge; déclaration d’applicabilité (ISO/IEC 42001, 6.1.3) si l’entreprise vise la certification. |
| 4 — Géré | Séries trimestrielles d’indicateurs et décisions du comité qui s’y appuient; délai de révocation mesuré en exercice sous la cible; alertes de dérive traitées; coût par tâche réussie comparé au processus de référence; audit interne du système de management de l’IA. |
| 5 — Optimisé | Révisions du cadre motivées par les incidents et les mesures; rapport de revue externe ou certificat ISO/ IEC 42001; ententes avec des partenaires; contributions aux standards ouverts. |

**ATTENTION**

Le modèle mesure l’avancement; il ne suspend aucune exigence. Tout nouvel agent est homologué selon l’annexe A, quel que soit le niveau de l’entreprise; les agents existants sont ramenés en conformité selon le régime transitoire de l’EXIG-GOV-16, sous les plafonds de phase et jamais au-delà du plafond de leur classe.

### Maturité et autonomie permise

Les règles de progression du chapitre 15 font de la maturité une condition de l’autonomie (tableau 58) : N2 et les premiers N3 bornés après le jalon 1; N3 entre domaines après le jalon 2, donc au niveau 2 de maturité, pour un agent dont tous les appels interdomaines passent déjà par la passerelle d’agents; N4 après le jalon 3, donc au niveau 3 sur les cinq dimensions, pour un agent de classe faible, sur un domaine d’exploitation (ODD) certifié, c’est-à-dire homologué par le comité (section 8.1), et sur décision du comité. Le plafond de phase est une condition nécessaire, jamais suffisante : la hausse effective exige l’homologation de l’agent (annexe A). Le plafond de la classe de risque s’applique en plus, et le plus strict l’emporte.

## 14.3 Lien avec la certification ISO/IEC 42001 et le NIST AI RMF

Cette section situe le modèle par rapport aux deux référentiels présentés à la section 12.5. Le modèle est un instrument interne de pilotage, qui ne donne lieu à aucune certification.

Le NIST AI RMF, d’application volontaire, propose des profils temporels : un profil actuel *(Current Profile)* décrit la gestion présente de l’IA, un profil cible *(Target Profile)* les résultats nécessaires pour atteindre les objectifs de gestion des risques. Leur comparaison révèle des écarts que des plans d’action comblent; le NIST ne prescrit aucun gabarit de profil**[74, 448]**. L’évaluation de maturité suit cette logique; pour en tirer un profil au sens du NIST, l’entreprise rattache ses critères aux sous-catégories pertinentes, dont celles du tableau 57.

ISO/IEC 42001:2023 est au contraire une norme d’exigences certifiable par tierce partie, par des organismes conformes à ISO/IEC 17021-1 et à ISO/IEC 42006:2025**[451]**. Norme de système de management, elle encadre des processus, du contexte de l’organisation (article 4) jusqu’à l’amélioration (article 10)**[395]**. Le cadre situe donc la préparation à la certification au niveau 4, qui ajoute aux processus du niveau 3 une évaluation des performances fondée sur des mesures, et la certification au niveau 5. La déclaration d’applicabilité, qui rattache les exigences du cadre aux mesures de l’annexe A de la norme (section 12.5), accompagne le traitement des risques de l’article 6.1.3 : c’est un livrable du niveau 3 pour l’entreprise qui vise la certification, et le niveau 4 en vérifie la tenue.

*Tableau 57 — Correspondance indicative entre niveaux de maturité, ISO/IEC 42001 et NIST AI RMF*

| **Niveau** | **ISO/IEC 42001:2023** | **NIST AI RMF 1.0** |
| --- | --- | --- |
| 2 — Reproductible | Politique d’IA (5.2), rôles (5.3); premières appréciations des risques (6.1.2) | GOVERN 1.6 (inventaire), 2.1 (rôles); MANAGE 2.4 (coupe-circuit) |
| 3 — Défini | Planification et fonctionnement appliqués à tous les agents (6.1.2 à 6.1.4, article 8); mesures A.5, A.6.2.8 et A.10 | GOVERN 1.7 (déclassement), 6.1 (tiers); MAP 3.5 (supervision humaine); MEASURE 2.7 (sécurité et résilience) |
| 4 — Géré | Évaluation des performances, audit interne et revue de direction (article 9); mesure A.6.2.6 (exploitation et surveillance) | MEASURE 2.4 (surveillance en production), 3.1 (risques émergents); MANAGE 4.1; profils actuel et cible comparés |
| 5 — Optimisé | Amélioration (article 10); certification par tierce partie | Profils revus à chaque révision du cadre |

Interprétation du cadre, établie à partir de NIST AI 100-1 et du catalogue d’ISO/IEC 42001**[74, 395]**.

Le cadre admet une certification ISO/IEC 42001 comme revue externe de la dimension Gouvernance; elle n’atteste toutefois pas, à elle seule, les quatre autres : la norme encadre des processus, sans prescrire de protocole, de passerelle ni de format de trace. À l’inverse, un niveau élevé de maturité n’établit ni la certification ni la conformité à la Loi 25 ou au RIA, qui s’apprécient obligation par obligation (chapitre 12).
