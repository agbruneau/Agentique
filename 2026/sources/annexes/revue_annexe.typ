#import "tpl.typ": *
#show: annexe-setup.with(first-page: 60)

= Annexe : reprise du 29 octobre 2026

Les 189 notices arXiv du corpus ont été reprises à l’API d’exportation du dépôt le 29 octobre 2026, soixante-quinze jours après la reprise du 15 août : 189 demandées, 189 obtenues, aucune retirée ni devenue introuvable. Mêmes champs — titre, auteurs, version courante, dates de dépôt et de dernière révision, `journal_ref`, DOI, `comment` —, même règle de partage (2.2). Aucune passe neuve n’a été conduite : aucune pièce n’est versée au corpus, dont le corps reste gelé au 15 août 2026. Cette annexe dit ce qui a bougé dans les notices, ce que cela change aux énoncés de la revue, et corrige quatre erreurs relevées à la relecture (tableau 11). Une vérification de forme la précède : les titres, dates de dépôt, versions et dates de révision portés par la bibliographie concordent tous avec l’historique des notices ; seuls deux titres ont changé depuis, par révision.

== Le régime de preuve au 29 octobre

#legende(9)[Régimes de preuve des 189 pièces déposées sur arXiv, aux reprises du 15 août et du 29 octobre 2026, d’après les notices de l’API du dépôt. Les parts portent sur ce corpus et sur ce que la notice déclare, non sur le champ.]

#tableau((2.4fr, 0.8fr, 0.6fr, 0.8fr, 0.6fr),
  ([Régime], [15 août 2026], [Part], [29 octobre 2026], [Part]),
  [Publication attestée en notice (`journal_ref` ou DOI)], [12], [6 %], [16], [8 %],
  [Acceptation autodéclarée (champ de commentaire)], [32], [17 %], [34], [18 %],
  [Aucun signe de revue par les pairs], [145], [77 %], [139], [74 %],
  [Total], [189], [100 %], [189], [100 %],
)

Seize notices ont bougé en soixante-quinze jours (tableau 9) : quatorze par une version nouvelle, deux par le seul ajout d’une référence de publication, [11] et [116]. Quatre pièces passent au régime attesté : [11] (_Journal of Information Security and Applications_, 2026, article 104645, au champ `journal_ref` et par DOI), du socle hérité ; [67] (DOI des actes de l’AAAI, 10.1609/aaai.v40i42.40895) et [70] (DOI de l’ACM, 10.1145/3847352.3848090), du front de la sécurité ; [116] (actes d’IMNS 2026, IEEE, au champ `journal_ref` et par DOI), de la couche transactionnelle. Deux passent à l’acceptation autodéclarée : [119] (« Accepted to EC 2026 ») et [164] (« EMNLP 2026 Main Accepted »). Aucune ne régresse.

La part du non-arbitré baisse de trois points, et elle baisse par la mise à jour des notices, non par l’arrivée de pièces arbitrées. Elle reste un plafond (17) : les quatre pièces dont la passe de contrôle avait trouvé la publication — [92], [102], [107] et [124] — ne la déclarent toujours pas. Quant à la stabilité des textes, 99 pièces sur 189 en sont encore à leur version initiale, soit 52 % contre 54 %, et 137 ont leur version courante datée de 2026. Quatorze révisions en dix semaines : 7 % du corpus (environ 2,8 % par mois), soit un rythme nettement inférieur aux 15 % observés sur le seul mois de juin à la section 3.1.

Ce que le corpus arbitré en retient. Le tableau 8 compterait désormais seize pièces. Deux des six fronts qu’il donnait pour vides en sortent — la sécurité, par [67] et [70], et la couche transactionnelle, par [116] —, et l’un des six résultats qu’il disait sans appui attesté en reçoit un : que le mandat signé ne soit pas le point de rupture repose en partie sur [116], désormais publié. Au front de la chorégraphie et de l’essaim, [164] rejoint [162] et [172] parmi les acceptations annoncées au seul champ de commentaire (13). Restent sans pièce attestée l’identité et la délégation, les systèmes multi-agents, l’évaluation, la chorégraphie et l’essaim ; et le résultat le plus décisif du front de la sécurité, que les scores de défense ne survivent pas à l’adversaire adaptatif [71], n’en a toujours aucune.

== Les révisions qui touchent un chiffre cité

#legende(10)[Les sept révisions du 15 août au 29 octobre 2026 dont le résumé a changé, avec ce que la revue en cite et ce que porte le résumé courant.]

#tableau((0.75fr, 0.85fr, 1.75fr, 2.45fr),
  ([Réf. (section)], [Version], [Cité par la revue (15 août)], [Résumé courant (29 octobre)]),
  [[67] (5.1, 5.3)], [v1 → v2, 29 sept.], [1 312 cas de test ; 72,8 % de succès sur o1-mini ; refus inférieur à 3 %], [1 348 cas de test ; 72,8 % et moins de 3 % inchangés],
  [[70] (5.2)], [v3 → v4, 28 sept.], [« Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration » ; de 85-100 % à 0-5 %], [titre devenu « Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents » ; chiffres inchangés],
  [[71] (5.1, tableau 7)], [v2 → v3, 28 sept.], [trois suites, cinq modèles ; une défense à 0 % remonte à 28 % au global et à 64 % sur les tâches à action déléguée], [titre devenu « AutoDojo: A Generative Benchmark for Evaluating Prompt Injection Defenses in LLM Agents » ; dix défenses, cinq modèles, six suites sur AgentDojo et AgentDyn ; « static benchmarks often significantly overestimate defense efficacy » ; les chiffres 0 %, 28 % et 64 % ne figurent plus au résumé],
  [[127] (10.1)], [v2 → v3, 31 août], [moins de 6 % de surcoût], [de 5,2 à 6,6 % de coût de débit incrémental, sur une mesure refaite ; comparaison avec le SDK de Temporal ajoutée],
  [[134] (10.2, 15.2)], [v2 → v3, 16 août], [langage de protocole ; « empirical evaluation is future work »], [théorème de correction mécanisé en Lean 4 ; gain de 14 à 22 points sur SWE-bench Verified, évalué par les auteurs ; soumission annoncée à ACM TOSEM, qui ne compte pas],
  [[160] (13.1)], [v1 → v3, 4 oct.], [+10,5 points sur SWE-bench Verified, coût par tâche réduit de moitié], [jusqu’à 17,5 points et 2,49 fois plus rapide, sur Terminal-Bench 4.0, DeepSWE et SWE-bench Verified ; le coût par tâche ne figure plus au résumé],
  [[164] (13.2)], [v2 → v3, 30 août], [(F+1)-robustesse sur le graphe], [formulation du résumé retouchée (borne de (F+1)-robustesse inchangée) ; acceptation à EMNLP 2026 annoncée au commentaire],
)

La mise en garde de la section 3.1 se vérifie une seconde fois : une pièce citée peut changer de chiffre sans changer de numéro. Deux cas pèsent. [71] porte, au corps de cette revue et à son tableau 7, le résultat décisif du front de la sécurité ; sa version courante ne l’énonce plus au résumé et en élargit le dispositif. La conclusion qualitative — les bancs statiques surestiment les défenses — tient et s’étend ; le chiffre, lui, ne vaut plus que pour la v2. [127] franchit la borne que la section 10.1 lui prêtait : « moins de 6 % » devient « 5,2 à 6,6 % ». Les sept autres révisions laissent leur résumé inchangé — [42], [109], [113], [118], [119], [186] et [191] —, [113] n’ajustant que son commentaire : la version condensée y fait désormais cinq pages, acceptée à l’ACM AI Summit 2026.

== Le contrôle refait

La requête « conformance checking » AND « LLM » de la section 10.3 rend huit entrées au lieu de sept. L’entrée supplémentaire, arXiv:2606.18425, déposée le 16 juin 2026, y entre par sa v2 du 8 septembre : elle confronte un flot de travail généré à sa propre spécification, non une trace d’agent autonome à un modèle de processus. Aucun dépôt n’est postérieur au 15 août. La lacune tient.

== Les trois énoncés de la veille au 29 octobre

La revue a laissé à la veille quatre faits qu’elle porte seule (17). La reprise du 29 octobre de la même veille [260] — auto-citation déclarée — les rouvre ; aucun verdict de la section 15 n’en est déplacé.

*Délégation (15.1).* Le groupe WIMSE de l’IETF a adopté le 15 septembre 2026 un premier document agentique, AIMS, informationnel, sans protocole neuf ni chaîne à N sauts ; des douze brouillons de délégation que relève la veille, aucun n’est adopté et deux ont expiré. « Normalisé » reste faux. Le déficit d’adoption a cessé d’être total ; il n’a pas cessé d’être un déficit d’adoption.

*Orchestration (15.2).* Camunda 8.10 expose les processus BPMN déployés comme outils MCP, et aucun protocole n’a adopté de formalisme de processus. Le mouvement vient encore de l’industrie, côté moteur : la section 15.2 avait prévu ce cas, qui confirme le verdict au lieu de l’infirmer. Aucune pièce du corpus ne mesure l’adoption d’un formalisme agentique par un moteur.

*Observabilité (15.3).* Le registre GenAI d’OpenTelemetry compte 85 attributs au 29 octobre, contre 63 au 15 août, tous en développement ; aucun ne décrit de chaîne de mandat, et les propositions d’identité et d’autorisation d’agent restent ouvertes. L’énoncé tient, et l’arbitrage porte toujours, comme l’écrivait la section 15.3, sur l’émission et la liaison, non sur la nomenclature.

== Errata de la relecture du 29 octobre

#legende(11)[Errata de l’édition du 15 août 2026. « Corps » : corrigé à sa place ; « annexe » : corrigé ici seulement.]

#tableau((0.3fr, 1.0fr, 2.0fr, 2.1fr, 0.65fr),
  ([N#super[o]], [Où], [Erreur], [Correction], [Traitement]),
  [1], [12, introduction], [« quatre mesures, dont deux arbitrées »], [une seule pièce attestée sur ce front, [158] (tableau 8) ; [155] et [156], acceptations autodéclarées, sont une position et une architecture, non des mesures : « dont une arbitrée »], [corps],
  [2], [tableau 8 et réf. [59]], [« MSR “26 »], [« MSR ’26 » — le champ `journal_ref` porte `MSR '26`], [corps],
  [3], [7.2 (tableau 4), 14.3], [onze constructions d’auteurs et quatre évaluations indépendantes font quinze pièces sur quatorze ; « les exceptions étant exactement les pièces concluant au non-avantage »], [[92], qui propose son propre cadre de discussion (résumé de sa notice) et conclut au non-avantage, est compté des deux côtés ; les exceptions sont trois des quatre pièces concluant au non-avantage], [corps (14.3) ; annexe (tableau 4)],
  [4], [18], [« Ce corpus peut seulement dire où regarder — et sur les trois énoncés soumis, elle l’a fait »], [le sujet est la revue : « la revue l’a fait »], [corps],
)

== Ce que cette reprise n’a pas fait

Aucune passe neuve sur les dix fronts : les dépôts du 15 août au 29 octobre 2026 ne sont ni lus ni versés, et la passe de contrôle sur DBLP, Crossref et OpenAlex n’a pas été refaite. Le corpus a donc soixante-quinze jours de retard sur le dépôt ; cette annexe en date les notices, non le champ.
