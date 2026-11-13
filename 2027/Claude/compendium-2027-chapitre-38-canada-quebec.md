# Chapitre 38 — Canada et Québec

*Question directrice : quel cadre s'applique ici ?*

> **Version 2 — 11 novembre 2026.** État de référence : stratégie fédérale « AI for All » (4 juin 2026), projet de loi C-36 à l'étape de la deuxième lecture, ligne directrice E-23 du BSIF (en vigueur le 1er mai 2027), Énoncé de principes québécois (édition 2025) et guide du MCN sur l'IA agentique (2026). Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [15] sont des pages primaires lues pour ce chapitre, [16] et [17] n'ont pas pu l'être. Chapitre audité et révisé le 12 novembre 2026.

Une entreprise qui déploie des agents au Canada cherche d'abord la loi sur l'IA. Il n'y en a pas, ni fédérale ni québécoise. Le cadre applicable est un empilement : le droit de la protection des renseignements personnels, une ligne directrice sectorielle pour les institutions financières fédérales et, pour les administrations, des instruments administratifs, dont deux guides récents sur l'IA agentique.

Cet empilement a un centre de gravité : la décision automatisée. Or savoir si une décision est « fondée exclusivement sur un traitement automatisé » ne dépend pas du modèle de langage. Cela dépend de l'endroit où un humain intervient, donc de l'orchestration. La conformité se joue donc ici dans l'architecture : points de validation, contenu des journaux, inventaire, trajet des données. Les deux guides publics, sans force obligatoire pour le secteur privé, décrivent le socle de contrôles qu'un donneur d'ordre public ou un régulateur attendra vraisemblablement.

---

## 38.1 Le paysage fédéral : pas de loi sur l'IA, une stratégie

« AI for All », lancée le 4 juin 2026, est une stratégie de cinq ans en trois piliers : bâtir la confiance, créer des occasions, renforcer la souveraineté [1]. Elle vise à faire passer l'adoption de l'IA d'un peu plus de 12 % à 60 % d'ici 2034. Le pilier de la confiance annonce une modernisation des cadres législatifs, une protection accrue des renseignements personnels et un régime de sécurité en ligne. Le communiqué ne nomme aucune loi propre à l'IA. Les agents n'y figurent qu'une fois : des agents « de confiance » promis aux étudiants du postsecondaire.

Le projet de loi C-36, déposé le 15 juin 2026 par le ministre de l'Intelligence artificielle et de l'Innovation numérique, édicte la Loi visant à protéger la vie privée et les données des consommateurs [2][3]. C'est une réforme de la protection des renseignements personnels dans le secteur privé, pas une loi sur l'IA. Au 12 novembre 2026, il est inscrit à l'étape de la deuxième lecture à la Chambre des communes, sans débat consigné ni étude en comité [3].

Quatre éléments du texte de première lecture concernent les agents [4].

- **Une définition large.** Le « système décisionnel automatisé » est une technologie qui sert à « appuyer ou remplacer le jugement de décideurs humains » (art. 2). Un agent qui prépare une décision est visé, pas seulement celui qui la rend seul.
- **Une transparence générale.** L'organisation expliquerait, dans ses politiques, l'usage de ces systèmes pour prédire, recommander ou décider (art. 62).
- **Une explication sur demande.** Si la décision peut avoir des effets juridiques ou une incidence importante comparable, l'individu obtiendrait les types de renseignements utilisés, leur provenance et les principaux facteurs, puis pourrait présenter ses observations à un employé habilité à réviser (art. 63).
- **Une évaluation avant tout transfert hors du Canada** (art. 57).

Le document d'information annonce des sanctions administratives pouvant atteindre 10 millions de dollars ou 3 % des recettes globales brutes, et une nouvelle Commission canadienne de la sécurité numérique et de la protection des données, dotée d'un pouvoir d'ordonnance [2].

C-36 reste un projet : il peut être amendé, et son entrée en vigueur est renvoyée à un décret [4]. Selon le résumé d'une analyse de cabinet non lue en entier, son volet sur l'IA est plus étroit que celui du projet C-27, jamais adopté [16].

---

## 38.2 Secteur public fédéral : décisions automatisées

Le gouvernement fédéral encadre ses propres systèmes par un instrument administratif, la Directive sur la prise de décisions automatisée du Conseil du Trésor, dont l'outil d'application est l'évaluation de l'incidence algorithmique (EIA) [6]. L'EIA est un questionnaire obligatoire qui classe un système en quatre niveaux d'incidence, de « peu ou pas d'incidence » à « incidence très élevée ». Les exigences de la Directive se resserrent d'un niveau à l'autre.

Selon la page de l'EIA, une première évaluation se fait au début de la conception, une seconde avant la mise en production. L'évaluation est revue quand la fonctionnalité ou la portée du système change. Les résultats sont publiés sur le Portail du gouvernement ouvert.

La règle de revue pèse sur un agent plus que sur un système classique. Brancher un nouvel outil élargit ce que l'agent peut faire; c'est, selon la lecture proposée ici, un changement de portée. Un registre d'outils tenu à jour (chapitre 8) devient alors une pièce de conformité.

Le Secrétariat du Conseil du Trésor publie aussi un Guide sur l'utilisation de l'intelligence artificielle agentive, destiné aux ministères et organismes [5]. La page, datée du 15 septembre 2026, distingue quatre niveaux d'autonomie, de l'assistance à l'autonomie adaptative, et demande de vérifier si le cas d'utilisation est visé par la Directive, sans fixer de seuil. La section 38.5 le compare au guide québécois.

---

## 38.3 Institutions financières : la ligne directrice E-23

La ligne directrice E-23 du Bureau du surintendant des institutions financières (BSIF), sur la gestion du risque de modélisation, a été publiée le 11 septembre 2025 et prend effet le 1er mai 2027 pour toutes les institutions financières fédérales [7][8].

Le texte ne contient ni le mot « agentic » ni le mot « agent » [8]. Il prévoit toutefois que des modèles à autoapprentissage dynamique et à prise de décision autonome pourraient se répandre.

La définition du modèle est volontairement large [7][8] : l'application d'hypothèses ou de techniques statistiques, y compris les méthodes d'IA et d'apprentissage automatique, avec une entrée, un traitement et un résultat. Les attentes ne varient pas selon l'approche algorithmique. Le texte s'organise en trois résultats attendus et douze principes couvrant le cycle de vie complet.

| Attente de E-23 | Portée pour un système d'agents |
|---|---|
| Inventaire : identifiant, propriétaire, origine, cote de risque, usages approuvés, dépendances [8] | Recoupe l'inventaire des agents (chapitre 39) |
| Cote de risque inhérent qui règle l'intensité des contrôles [8] | La cote d'un agent devrait refléter les actions permises, pas seulement le modèle |
| Modèles de tiers cotés individuellement, selon la ligne directrice B-10 [7][8] | Le modèle de langage d'un fournisseur est un modèle de tiers |
| Critères internes de changement important pour un modèle autoapprenant [7] | Question ouverte pour un agent à mémoire persistante (chapitre 14) |
| Approbation avant tout changement [7] | Versions des instructions, des outils et des modèles (chapitre 34) |

La colonne de droite est une lecture, non le texte du BSIF. La cote de risque des usages d'IA générative est laissée au jugement de chaque institution [7].

E-23 ne vise que les institutions de compétence fédérale; les institutions à charte québécoise relèvent d'un autre régulateur.

---

## 38.4 Québec : décisions automatisées dans la Loi 25

Parmi les textes examinés, la seule règle en vigueur qui vise expressément la décision automatisée dans le secteur privé est québécoise. L'article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé, introduit par la Loi 25, impose trois obligations à l'entreprise qui utilise des renseignements personnels pour rendre une décision fondée exclusivement sur un traitement automatisé [9] :

1. en informer la personne, au plus tard au moment où la décision lui est communiquée;
2. lui indiquer, sur demande, les renseignements utilisés, les raisons ainsi que les principaux facteurs et paramètres ayant mené à la décision, et son droit de faire rectifier ces renseignements;
3. lui donner l'occasion de présenter ses observations à un membre du personnel en mesure de réviser la décision.

**La date.** L'article 12.1 est inséré par l'article 110 de la Loi 25. Celui-ci ne figure dans aucune des exceptions de l'article 175, qui fixe l'entrée en vigueur générale au 22 septembre 2023 [9], ce qui tranche entre les sources secondaires.

**La sanction.** Le défaut d'informer la personne ou de lui permettre de présenter ses observations est passible d'une sanction administrative pécuniaire, plafonnée à 10 millions de dollars ou 2 % du chiffre d'affaires mondial [9].

**Le mot « exclusivement ».** L'article 65.2 de la Loi sur l'accès impose la même règle, dans les mêmes termes, aux organismes publics. La page gouvernementale qui l'explique en donne une lecture utile [10] : la décision est exclusivement automatisée quand elle est prise sans aucune intervention humaine; une intervention mineure, sans répercussion réelle, n'écarte pas l'article; un outil qui remet un rapport à un employé, lequel décide, n'est pas visé. Transposer cette lecture à l'article 12.1 est une analogie, raisonnable vu l'identité des textes.

| | Loi 25, art. 12.1 [9] | Projet de loi C-36 [4] |
|---|---|---|
| Statut | En vigueur depuis le 22 septembre 2023 | Deuxième lecture |
| Déclencheur | Décision exclusivement automatisée | Système qui appuie ou remplace le jugement humain |
| Information | Systématique, au moment de la décision | Explication générale dans les politiques |
| Explication | Sur demande | Sur demande, si effets juridiques ou incidence importante |
| Révision | Observations à un membre du personnel habilité | Observations à un employé habilité |

Trois conséquences d'architecture en découlent.

**La qualification se fait par point de décision.** Un même agent peut préparer dix dossiers sous validation humaine et en trancher un onzième seul. Seul ce dernier déclenche l'article 12.1. Une approbation de pure forme ne protège pas.

**L'explication exige une trace.** Il faut retrouver quels renseignements l'agent a consultés et quels facteurs ont pesé. Le premier relève de la journalisation des appels d'outils (chapitre 33). Le second, plus difficile avec un modèle de langage, plaide pour loger la règle de décision dans un composant déterministe, l'agent se bornant à réunir les faits (chapitre 17).

**La révision exige un chemin.** L'orchestration prévoit une voie de reprise humaine, vers une personne qui a l'autorité de modifier la décision (chapitre 22).

La Loi 25 impose par ailleurs une évaluation des facteurs relatifs à la vie privée (EFVP) pour tout projet d'acquisition, de développement ou de refonte d'un système d'information qui traite des renseignements personnels [9]. Un projet d'agents en est un.

**La conservation et l'effacement.** Les fins accomplies, l'entreprise détruit le renseignement ou l'anonymise, sauf délai légal de conservation (art. 23); conserver ou détruire en contravention à la loi est passible d'une sanction administrative pécuniaire [9]. C-36 prévoirait un retrait sur demande, notamment après le retrait du consentement (art. 54), et une conservation limitée au temps nécessaire, mais suffisante pour répondre à une demande d'explication (art. 52 et 53) [4]. Pour un agent, l'échéance vise la mémoire, les traces, les copies chez les fournisseurs et les données d'entraînement qui en sont tirées (chapitre 47); le chemin d'effacement se conçoit comme à la section 14.6.

---

## 38.5 Administration publique québécoise : guide sur l'IA agentique, Énoncé de principes

Le ministère de la Cybersécurité et du Numérique (MCN) encadre l'usage de l'IA par les organismes publics [11]. Trois instruments se superposent.

**Une déclaration annuelle.** L'arrêté 2024-01 du 28 février 2024 oblige les organismes publics à déclarer chaque année leurs initiatives d'IA [14]. Le portrait qui en résulte recense, au 15 juin 2026, 432 initiatives dans 157 organismes, contre 258 et 83 un an plus tôt. Aucune catégorie n'isole les agents; la catégorie « décision automatisée » compte une seule initiative (chapitre 42).

**Un énoncé de principes.** L'édition 2025 de l'Énoncé est l'annexe de l'arrêté 2025-02 du 3 décembre 2025 [12]. Elle compte douze principes, dont trois visent les systèmes autonomes :

- la responsabilité : l'organisme demeure entièrement responsable des décisions, actions et impacts de ses systèmes, « même lorsque ceux-ci fonctionnent de manière autonome »;
- l'autonomie et la supervision humaine, principe qui nomme l'IA agentique et exige des mécanismes de validation, d'intervention ou d'arrêt;
- la souveraineté numérique (section 38.6).

L'Énoncé s'applique même lorsque l'organisme recourt à des fournisseurs, et l'organisme doit s'assurer que ceux-ci le respectent. Il atteint ainsi l'entreprise privée.

**Un guide sur l'IA agentique.** Le Guide sur l'utilisation responsable de l'intelligence artificielle agentique, daté de 2026, n'ajoute pas un cadre; il applique les cadres existants aux systèmes capables d'agir [13]. Son idée centrale : plus un système peut agir, accéder à des outils et enchaîner des étapes, plus les exigences de gouvernance, de supervision, de traçabilité et de contrôle des coûts s'élèvent.

Un agent ne se retient pas par défaut : il faut d'abord écarter l'amélioration de processus, l'automatisation classique et l'assistant sans capacité d'action. Le guide prévoit un parcours d'autorisation en trois étapes — filtrer le cas d'usage, vérifier la préparation du pilote, puis celle de la production — et des premiers pilotes internes, réversibles et assortis d'un plafond budgétaire.

Il cite le guide fédéral, avec lequel il converge.

| Contrôle | Guide fédéral [5] | Guide québécois [13] |
|---|---|---|
| Accès | Lecture seule par défaut; liste courte d'opérations | Moindre privilège; l'agent ne peut élargir ses permissions |
| Validation humaine | Avant toute opération qui modifie l'état d'un système, sauf effet minime et réversible | Avant toute action à incidence significative; jamais symbolique |
| Journaux | Horodatés : outils, opérations, autorisations; hors de portée de l'agent | Reconstitution complète, coûts compris; hors de portée de l'agent |
| Arrêt | Interrupteur d'urgence indépendant | Arrêt et retour au mode manuel prévus dès la conception |
| Inventaire | Identifiants clairs pour les agents | Registre des agents; gestion des versions |
| Coûts | Non traités en propre | Plafond de consommation |
| Protocoles | Aucune mention de MCP ni d'A2A | Aucune mention de MCP ni d'A2A |

Aucun des deux guides ne prescrit de protocole. Ils énoncent des exigences de résultat; les satisfaire au moyen de MCP, d'une passerelle ou d'un plan de contrôle reste une décision d'architecture (chapitres 5, 23 et 24). Le guide québécois demande toutefois, pour un système multi-agents, de documenter l'orchestration, les rôles, les transferts et les validations humaines.

---

## 38.6 Souveraineté et partenariats

Le chapitre 37 distingue la résidence des données du contrôle juridictionnel. Les textes d'ici touchent les deux.

**Au fédéral, une politique d'offre.** Le troisième pilier d'« AI for All » promet des fondations souveraines — calcul, infonuagique, connectivité, données, talent — et un supercalculateur public d'IA [1]. L'État y est présenté comme client d'ancrage des entreprises canadiennes. Le communiqué annonce une Sovereign Technology Alliance et fait état de douze partenariats internationaux, dont l'Union européenne. Il chiffre des cibles de croissance et d'emploi, pas le budget des programmes.

**Au Québec, un principe opposable aux organismes publics.** Le douzième principe de l'Énoncé leur demande de réduire leur dépendance envers les fournisseurs étrangers, de garder le plus possible le contrôle des modèles, des données et des infrastructures, et de favoriser, lorsque possible, des fournisseurs québécois ou canadiens offrant des solutions hébergées au Québec [12]. La note de tendances du MCN de juillet 2026 prévoit que l'hébergement des données, l'origine des modèles, la réversibilité contractuelle et la dépendance aux fournisseurs deviendront des critères de décision explicites [15].

**Dans le secteur privé, une obligation d'évaluation.** L'article 17 de la loi québécoise sur le secteur privé exige une EFVP avant de communiquer un renseignement personnel à l'extérieur du Québec, ou d'y confier son traitement [9]. L'évaluation tient compte du régime juridique de l'État de destination; la communication suppose une protection adéquate et une entente écrite. C-36 prévoirait une évaluation analogue (art. 57) [4].

Un système d'agents multiplie les trajets à évaluer : l'inférence chez un fournisseur de modèles, ou chez un autre quand un routeur bascule (chapitre 44), l'appel d'un serveur MCP distant, la délégation à l'agent d'un partenaire (chapitre 45), l'exportation de traces vers une plateforme d'observabilité. L'EFVP d'un agent se dresse donc à partir de la carte de ses états et de ses flux (chapitre 46), et un outil ou une route ajoutés peuvent ouvrir un nouveau trajet. L'inférence confidentielle et les clés détenues par l'entreprise sont des mesures de protection à y faire valoir.

---

## 38.7 Conséquences pour les entreprises

| Situation | Textes à considérer | Force |
|---|---|---|
| Entreprise qui traite des renseignements personnels au Québec | Loi 25 : art. 12.1, art. 17, EFVP [9] | Loi en vigueur |
| Entreprise de compétence fédérale ou active hors Québec | LPRPDE, régime actuel; C-36 s'il est adopté [3][4] | Projet à surveiller |
| Institution financière fédérale | E-23, avec B-10 pour les tiers [7][8] | Attentes du régulateur au 1er mai 2027 |
| Fournisseur d'un organisme public québécois | Énoncé de principes et guide [12][13] | Indirecte, contractuelle |
| Fournisseur d'un ministère fédéral | Directive, EIA et guide [5][6] | Indirecte, contractuelle |

Quatre dispositions valent dans presque tous les cas.

1. **Classer chaque point de décision.** Pour chaque agent, établir s'il rend, à l'égard d'une personne, une décision sans intervention humaine réelle.
2. **Journaliser pour expliquer.** Les journaux reconstituent les renseignements consultés, les outils appelés et les validations humaines, et restent hors de portée de l'agent.
3. **Tenir un inventaire unique.** Un registre des agents, avec propriétaire, finalité, systèmes connectés, niveau d'autonomie et cote de risque, sert à la fois le guide québécois, E-23 et la gouvernance interne (chapitre 39).
4. **Cartographier les flux sortants.** Chaque fournisseur de modèle, serveur distant et agent tiers est un destinataire à évaluer.

Les obligations étrangères s'ajoutent à ce cadre sans le remplacer (chapitre 35). Quant à savoir qui répond des actes d'un agent (chapitre 36), l'Énoncé québécois et les deux guides tranchent pour l'administration : l'organisme demeure responsable.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Référentiel de contrôles, faute de loi sur l'IA | Socle commun des guides fédéral et québécois | Secteur doté d'un cadre plus strict, comme E-23 |
| Décision visant une personne | Validation humaine réelle avant la décision | Automatisation complète assumée : appliquer l'article 12.1 en entier |
| Logique de décision | Composant déterministe; l'agent réunit les faits | Aucune décision individuelle en jeu |
| Première mise en œuvre | Pilote interne, réversible, plafonné | Encadrement renforcé et validation spécialisée |
| Inférence et outils hors Québec | EFVP préalable et entente écrite | Aucun renseignement personnel dans le flux |
| Marché public québécois | Hébergement au Québec, fournisseur québécois ou canadien | Justification documentée par l'organisme |
| Institution financière fédérale | Agents inscrits à l'inventaire E-23 dès maintenant | — |
| Ajout d'un outil à un agent | Réévaluation du risque et de l'EFVP | Outil sans accès à des données ni à des actions sensibles |
| Mémoire et traces d'un agent | Durée fixée par finalité, puis destruction ou anonymisation | Délai de conservation imposé par une loi |

---

## Points à retenir

- Le Canada n'a pas de loi sur l'IA. « AI for All » annonce des lois sur la vie privée et la sécurité en ligne, pas un régime propre aux agents.
- Le projet de loi C-36, non adopté, réforme la protection des renseignements personnels; sa définition du système décisionnel automatisé couvre aussi les systèmes qui appuient une décision.
- L'article 12.1 de la loi québécoise sur le secteur privé est en vigueur depuis le 22 septembre 2023 : information, explication sur demande, révision par une personne habilitée.
- Le caractère « exclusivement » automatisé d'une décision est une propriété de l'orchestration. Une validation de pure forme ne le fait pas disparaître.
- E-23 prend effet le 1er mai 2027. Elle ne nomme pas les agents, mais sa définition du modèle et ses attentes d'inventaire et de cote de risque s'y appliquent sans peine.
- Les guides fédéral et québécois convergent : moindre privilège, validation humaine avant toute action à effet, journaux hors de portée de l'agent, arrêt, inventaire.
- Aucun de ces textes ne mentionne MCP ni A2A. Ils fixent des résultats, pas des moyens.
- L'Énoncé québécois s'étend aux fournisseurs des organismes publics et fait de la souveraineté numérique un critère de choix.
- Chaque appel d'un agent qui transmet un renseignement personnel hors Québec est une communication à évaluer au préalable. Ce qu'il conserve, mémoire et traces comprises, se détruit ou s'anonymise une fois la fin accomplie.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Premier ministre du Canada — lancement d'« AI for All »](https://www.pm.gc.ca/en/news/news-releases/2026/06/04/prime-minister-carney-launches-ai-all-canadas-new-national-artificial)
2. [ISDE — document d'information sur C-36](https://www.canada.ca/fr/innovation-sciences-developpement-economique/nouvelles/2026/06/document-dinformation--le-gouvernement-du-canada-presente-un-projet-de-loi-visant-a-proteger-la-vie-privee-des-canadiens-a-lere-numerique.html)
3. [LEGISinfo — C-36](https://www.parl.ca/legisinfo/fr/projet-de-loi/45-1/c-36)
4. [C-36 — texte de première lecture](https://www.parl.ca/DocumentViewer/fr/45-1/projet-loi/C-36/premiere-lecture) — première moitié lue.
5. [Canada — Guide sur l'utilisation de l'IA agentive](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/innovations-gouvernementales-numeriques/utilisation-responsable-ai/guide-utilisation-intelligence-artificielle-agentive.html)
6. [Canada — Évaluation de l'incidence algorithmique](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/innovations-gouvernementales-numeriques/utilisation-responsable-ai/evaluation-incidence-algorithmique.html)
7. [BSIF — lettre d'accompagnement de E-23](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027-letter)
8. [BSIF — ligne directrice E-23 (2027)](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027)
9. [Loi 25 — L.Q. 2021, chapitre 25](https://www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/fr/2021/2021C25F.PDF)
10. [Québec — Décision fondée exclusivement sur un traitement automatisé](https://www.quebec.ca/gouvernement/travailler-gouvernement/normes-gouvernance-pratiques-internes/protection-des-renseignements-personnels/technologie-et-droit-a-la-protection-des-renseignements-personnels/decision-traitement-automatise)
11. [Québec — Utilisation responsable de l'IA](https://www.quebec.ca/gouvernement/numerique/intelligence-artificielle-administration-publique/utilisation-responsable-intelligence-artificielle)
12. [MCN — Énoncé de principes, édition 2025](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/cybersecurite_numerique/Publications/Strategie_IA/Enonce_IA.pdf)
13. [MCN — Guide sur l'IA agentique](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/cybersecurite_numerique/Intelligence_artificielle/GU_IA_Agentique.pdf)
14. [Québec — Portrait des utilisations de l'IA](https://www.quebec.ca/gouvernement/numerique/intelligence-artificielle-administration-publique/portrait)
15. [MCN — Grandes tendances numériques, juillet 2026](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/cybersecurite_numerique/Transformation_numerique/DOC_tendances_numerique_juillet_2026.pdf)

Sources non lues :

16. [Blakes — réforme fédérale](https://www.blakes.com/fr-ca/perspectives/nouvelle-tentative-du-canada-pour-reformer-le-cadre-federal-de-protection-des-renseignements-personn/) — résumé de recherche seulement.
17. [Directive sur la prise de décisions automatisée](https://www.tbs-sct.canada.ca/pol/doc-fra.aspx?id=32592) — requête rejetée par le serveur.

## Limites de ce chapitre

- La Directive fédérale [17] n'a pas pu être lue, même à l'audit. Son champ d'application, ses exigences par niveau et sa date ne sont pas décrits; la section 38.2 repose sur la page de l'EIA.
- Les pages web [1] à [8], [10], [11] et [14] ont été lues au moyen d'un outil d'extraction automatique, sans recollationnement des citations. Les documents [9], [12], [13] et [15] ont été lus en texte intégral. [1], [3], [4], [5], [8] et [9] ont été relus à l'audit du 12 novembre 2026.
- Seule la première moitié du texte de C-36 a été lue; les sanctions viennent du document ministériel [2]. Le sort du projet C-27 vient de la connaissance générale et d'un résumé de recherche [16], comme la mention de la LPRPDE en 38.7, dont le régime d'effacement n'est pas décrit.
- L'article 12.1 est cité d'après le texte sanctionné de 2021, la version codifiée étant inaccessible; les modifications ultérieures n'ont pas été vérifiées. Aucune décision ni ligne directrice de la Commission d'accès à l'information n'a été lue.
- L'encadrement des institutions financières à charte québécoise et le droit des autres provinces ne sont pas traités.
- Le guide québécois ne porte pas de date plus précise que 2026, et celle du guide fédéral est la date sans libellé affichée sur sa page. Les lectures proposées en 38.2, 38.3, 38.4 et 38.6 sont des inférences, non des positions des autorités.
