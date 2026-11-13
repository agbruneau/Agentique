# Chapitre 13 — Ingénierie du contexte

*Question directrice : que doit savoir un agent, et à quel moment ?*

> **Version 2 — 11 novembre 2026.** État de référence : spécification Agent Skills telle que publiée sur agentskills.io, extension Skills over MCP au stade bêta, feuille de route MCP du 22 août 2026, annonce de l'AAIF du 22 octobre 2026, prépublications arXiv dans leur version courante à cette date. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre. Les travaux connus seulement par la citation qu'en fait une source lue sont signalés comme tels. Les renvois « chapitre N » ont été vérifiés contre les chapitres rédigés. Chapitre audité et révisé le 12 novembre 2026.

Un modèle de langage ne décide que sur ce qui se trouve dans sa fenêtre de contexte au moment de l'appel. Tout le reste de l'entreprise, ses politiques, ses dossiers, ses conventions, n'existe pour lui que si quelqu'un l'y a placé. Pour un agent qui enchaîne des dizaines d'étapes, cette fenêtre se remplit de résultats d'outils, de journaux et d'états périmés, et la question n'est plus de bien formuler une demande, mais de régler ce que le modèle voit à chaque pas.

La thèse de ce chapitre tient en trois propositions. Le contexte est une ressource finie, dont le rendement décroît : en ajouter n'est jamais gratuit. Les formats ouverts apparus depuis 2025, Agent Skills et AGENTS.md, standardisent l'emballage et le moment du chargement, pas la qualité du contenu, et les mesures publiées montrent qu'un contexte mal choisi coûte plus qu'il ne rapporte. Le contexte doit donc être traité comme un actif d'entreprise : inventorié, versionné, attribué à un propriétaire et évalué.

---

## 13.1 Du prompt au contexte : une discipline

### Ce qui a changé

L'ingénierie de prompt règle la formulation d'une demande dans un échange où l'humain relit chaque réponse et filtre lui-même ce qu'il renvoie au modèle. Dans un agent, ce filtre disparaît. L'orchestrateur assemble à chaque étape les instructions, les définitions d'outils, l'historique, les résultats d'appels, la mémoire et les documents récupérés. C'est cet assemblage, et non la demande initiale, qui détermine la décision.

Une prépublication de mars 2026 propose de nommer ingénierie du contexte la discipline qui gère la composition, le moment, le format et la durée de vie de l'information dans le contexte d'un agent, et la compare à une logistique du savoir en juste-à-temps [1]. Anthropic en donnait dès septembre 2025 une définition voisine : l'ensemble des stratégies qui visent à sélectionner et à maintenir les meilleurs jetons pendant l'inférence, opération répétée à chaque appel et non faite une fois pour toutes [2].

### Une ressource à rendement décroissant

L'argument central est empirique. Une étude de 2023, acceptée par la revue TACL, a montré que la précision d'un modèle varie selon la position de l'information utile dans une longue entrée : elle est meilleure au début et à la fin, plus faible au milieu, y compris pour des modèles conçus pour les longs contextes [3]. Un rapport technique de Chroma, en juillet 2025, étend le constat à 18 modèles : la performance devient moins fiable à mesure que l'entrée s'allonge, même sur des tâches simples, et un seul distracteur suffit à la dégrader [4]. Ce rapport émane d'un éditeur de bases vectorielles; il n'a pas été évalué par des pairs.

Anthropic résume ces observations par l'image d'un budget d'attention : chaque jeton ajouté en consomme une part, et la dégradation est graduelle plutôt que brutale [2]. La conséquence pratique est contre-intuitive pour qui vient de la gestion documentaire : donner « tout ce qui pourrait servir » dégrade la décision.

### Les opérations de base

La prépublication reprend de LangChain quatre opérations sur le contexte : écrire (consigner hors de la fenêtre), sélectionner (récupérer ce qui est pertinent), compresser (condenser l'historique) et isoler (restreindre ce que chaque sous-agent voit) [1]. Pour les tâches longues, Anthropic décrit trois techniques qui les combinent [2] :

- la **compaction**, qui résume une conversation proche de la limite et repart du résumé;
- la **prise de notes structurée**, où l'agent consigne son avancement dans un fichier qu'il relit plus tard (chapitre 14);
- les **sous-agents**, qui explorent chacun dans une fenêtre propre et ne renvoient qu'un résumé condensé à l'agent principal (chapitre 16).

### Réserves

L'auteure de la prépublication marque elle-même trois limites [1] : la frontière avec l'assemblage antérieur de récupération, de mémoire et d'orchestration n'est pas nette; les conflits entre sources se règlent au cas par cas; la qualité d'un contexte se mesure mal sans test comparatif. C'est un texte de synthèse d'une seule auteure, non évalué par des pairs : il sert ici de cadre, pas de preuve.

---

## 13.2 Critères de qualité

La même prépublication propose cinq propriétés qu'un contexte de production devrait satisfaire [1]. Elle précise que cette taxonomie est « de travail » et non canonique, et que les deux dernières ne figurent pas explicitement dans les publications des fournisseurs.

| Critère | Énoncé | Défaillance typique | Levier principal |
|---|---|---|---|
| Pertinence | Seulement ce qui est nécessaire à l'étape en cours | Distraction, information utile noyée au milieu | Sélection, chargement à la demande |
| Suffisance | Tout ce qu'il faut pour décider sans deviner | Invention de faits plausibles | Récupération, vérification avant d'agir |
| Isolation | Chaque sous-agent ne voit que son propre contexte | Fuite entre rôles, décisions sur des données non prévues | Fenêtres séparées, filtrage entre agents |
| Économie | Le minimum de jetons et de réassemblages à qualité égale | Coût et latence qui croissent avec le nombre d'étapes | Compression, cache, chargement sélectif |
| Provenance | Chaque élément est traçable : système d'origine, date, niveau de confiance | Décision erronée impossible à expliquer | Métadonnées d'origine, journalisation |

### Des critères en tension

Pertinence et suffisance tirent en sens opposé : la première retranche, la seconde ajoute. Le bon contexte est, selon la formule de l'auteure, le minimum suffisant pour la décision. L'économie aggrave la tension; l'auteure y voit un faux dilemme, le coût d'une erreur dépassant de loin celui des jetons épargnés [1]. C'est une interprétation, non un résultat mesuré.

L'isolation relève autant du contrôle que de la sécurité. L'auteure rapporte, d'après son propre système de conformité, qu'un agent coordonnateur n'a pas besoin des détections brutes d'un agent spécialisé, seulement d'un verdict et d'un degré de confiance [1]. Le même principe, appliqué aux droits plutôt qu'à l'information, donne l'autorité réduite des sous-agents (chapitre 30).

La provenance est le critère le moins outillé. Sans elle, ni l'audit d'une décision ni le débogage ne sont possibles : on sait que l'agent s'est trompé, pas quel fragment l'y a conduit. Les traces distribuées en fournissent le support technique (chapitre 33).

### Comment un contexte se dégrade

La prépublication complète ces critères par quatre modes de dégradation, repris d'une taxonomie de Drew Breunig que ce chapitre ne connaît que par cette citation [1] :

- l'**empoisonnement** : une erreur entre dans le contexte et se reproduit à chaque étape suivante;
- la **distraction** : l'historique accumulé prend le pas sur le raisonnement, et l'agent répète ses actions passées;
- la **confusion** : une information non pertinente est utilisée parce qu'elle est présente;
- le **conflit** : des éléments accumulés se contredisent.

L'empoisonnement délibéré, par un tiers, relève du modèle de menace (chapitre 31). Les trois autres modes sont des défauts de conception ordinaires, que l'on corrige en amont de la fenêtre.

---

## 13.3 Agent Skills : le savoir-faire portable

### Le format

Agent Skills est un format ouvert pour emballer du savoir procédural. Une *skill* est un dossier qui contient au minimum un fichier `SKILL.md` : un en-tête YAML, puis des instructions en Markdown sans contrainte de forme [5][6]. Deux champs sont obligatoires : `name` (64 caractères au plus, minuscules, chiffres et traits d'union, identique au nom du dossier) et `description` (1 024 caractères au plus), qui doit dire ce que fait la skill et quand s'en servir. Des sous-dossiers conventionnels accueillent des scripts exécutables, des documents de référence et des gabarits.

```markdown
---
name: revue-contrat
description: Vérifie un contrat fournisseur selon la grille juridique interne. À utiliser quand un contrat ou une clause est soumis pour revue.
---
```

L'intérêt du format tient à son mode de chargement, la divulgation progressive, en trois niveaux [6] :

1. **Métadonnées** (environ 100 jetons) : nom et description de chaque skill, chargés au démarrage.
2. **Instructions** (moins de 5 000 jetons recommandés) : le corps de `SKILL.md`, chargé quand la skill est activée.
3. **Ressources** : scripts et références, lus seulement si la tâche l'exige.

Un agent peut ainsi garder de nombreuses skills à portée pour une empreinte minime. La spécification recommande de tenir `SKILL.md` sous 500 lignes et de ne pas enchaîner les renvois sur plus d'un niveau. Tout repose sur la description : c'est elle qui détermine si le modèle active la skill au bon moment.

### La gouvernance

Le format a été conçu par Anthropic, puis publié comme standard ouvert [5]. Le 22 octobre 2026, Anthropic l'a donné à l'Agentic AI Foundation, qui héberge désormais dix projets [7][22]. Selon le billet de la fondation, la spécification est sous licences Apache 2.0 et CC BY 4.0, et un comité de pilotage technique formé de mainteneurs de plusieurs organisations, siégeant à titre individuel, en oriente l'évolution [8]. Le même billet avance plus de 70 plateformes d'agents compatibles, sans méthode exposée, et plus d'un million de skills publiées en sept mois, d'après le registre skills.sh, non consulté.

### La distribution par MCP

L'extension Skills over MCP (`io.modelcontextprotocol/skills`) permet à un serveur MCP d'exposer des skills à côté de ses outils [9][10]. Elle est au stade bêta, sans destination déclarée (stable ou cœur du protocole), bien que sa proposition, SEP-2640, soit au statut Final. Trois traits intéressent l'architecte :

- le serveur publie pour chaque skill un **manifeste complet**, avec l'URI, la taille et l'empreinte SHA-256 de chaque fichier; l'hôte doit vérifier chaque fichier avant usage et restreindre les lectures au manifeste;
- l'hôte **ne doit pas** récupérer les fichiers avant d'en avoir besoin, ce qui inscrit la divulgation progressive dans le protocole;
- le contenu d'une skill est une **entrée non fiable** : l'exécution de code et les permissions qu'elle demande exigent une approbation explicite, liée au manifeste et révoquée dès qu'un fichier change.

L'identité d'une skill est le couple formé du serveur d'origine et de l'URI; le nom n'est qu'une étiquette, non unique. La page de l'extension précise que la prise en charge par les SDK et les hôtes est encore en cours de mise en œuvre [10][21].

### Ce que disent les mesures

Une prépublication, SkillsBench, évalue 87 tâches dans huit domaines, avec et sans skills, sur 18 configurations de modèle et de harnais [11]. Les skills rédigées et vérifiées par des humains font passer le taux de réussite moyen de 33,9 % à 50,5 %. Trois résultats nuancent ce gain :

- les skills **générées par l'agent lui-même** font moins bien que l'absence de skill, sur les trois configurations testées;
- 13 tâches sur 87 se dégradent avec les skills;
- une documentation exhaustive n'apporte presque rien (+0,7 point), contre +19 points pour des skills compactes, et des skills ciblées d'au plus trois modules font mieux que des ensembles plus vastes.

Les auteurs reconnaissent qu'une part du gain peut venir du simple ajout de contexte. Les tâches sont exécutées en terminal, dans des conteneurs, et le résultat ne se transpose pas d'emblée à des processus d'affaires.

Côté risque, une autre prépublication a analysé 31 132 skills tirées de deux places de marché : 26,1 % présentent au moins un motif de vulnérabilité, et celles qui embarquent des scripts sont environ deux fois plus exposées que les autres [12]. Une skill est à la fois une instruction et du code; elle entre dans la chaîne d'approvisionnement (section 31.5).

---

## 13.4 AGENTS.md et fichiers de contexte : des preuves mitigées

### Un format minimal

AGENTS.md se présente comme un « README pour agents » : un fichier Markdown ordinaire, sans champ obligatoire, où un dépôt consigne ses commandes de construction et de test, ses conventions et ses consignes de sécurité [13]. Dans un monodépôt, chaque paquet peut avoir le sien; le fichier le plus proche du fichier modifié l'emporte, et une consigne explicite de l'utilisateur prime sur tout. Le format est l'un des trois projets fondateurs de l'AAIF [7]. Son site revendique plus de 60 000 projets ouverts utilisateurs et une vingtaine d'agents de programmation compatibles.

À la différence d'une skill, ce fichier est chargé d'office, en entier, à chaque session : c'est du contexte permanent, d'où l'enjeu de son efficacité.

Une étude empirique de 2 303 fichiers de ce type, dans 1 925 dépôts, montre qu'ils évoluent comme du code de configuration, par petits ajouts fréquents, et deviennent difficiles à lire [14]. Les procédures de test (75,9 %), les détails de mise en œuvre (70,8 %) et l'architecture (68,1 %) dominent; la sécurité (14,8 %) et la performance (14,5 %) sont rarement abordées.

### Deux études, deux mesures

| | Gloaguen et coll. [15] | Lulla et coll. [16] |
|---|---|---|
| Question | Le fichier aide-t-il à résoudre la tâche ? | Le fichier rend-il l'agent plus rapide ? |
| Protocole | 300 tâches SWE-bench Lite avec fichiers générés; 138 tâches de 12 dépôts avec fichiers rédigés par les développeurs | 124 demandes de tirage dans 10 dépôts, avec et sans le fichier |
| Agents | Claude Code, Codex, Qwen Code | Codex seulement |
| Réussite | Fichiers générés : −0,5 et −2 points, non significatifs. Fichiers de développeurs : +2,4 points, non significatif | Non mesurée (contrôle manuel de 50 exécutions) |
| Coût et durée | Coût d'inférence en hausse de plus de 20 % en moyenne | Durée médiane en baisse de 28,64 %, jetons de sortie de 16,58 %; jetons totaux en légère hausse |
| Portée | Python seulement | Petites modifications seulement |

Les deux résultats ne se contredisent qu'en apparence : l'un mesure l'exactitude, l'autre la vitesse sans vérifier l'exactitude. Lus ensemble, ils disent qu'un fichier de contexte modifie nettement le comportement de l'agent, sans amélioration démontrée du résultat.

Le mécanisme est instructif. La première étude constate que les agents suivent bien les instructions : un outil mentionné dans le fichier est utilisé en moyenne 1,6 fois par tâche, contre moins de 0,01 fois sinon [15]. Les fichiers provoquent plus de tests, plus d'exploration, plus de raisonnement, donc plus de coût. Les vues d'ensemble du dépôt, très répandues, ne réduisent pas le nombre d'étapes nécessaires pour trouver les bons fichiers. Les auteurs recommandent de renoncer pour l'instant aux fichiers générés automatiquement, de limiter les fichiers rédigés à la main à ce que la documentation ne dit pas déjà, soit les conventions inhabituelles, et de tester tout fichier avant de l'adopter.

Ces deux études portent sur des agents de programmation; rien de comparable n'a été trouvé pour des agents d'affaires. L'extrapolation est raisonnable, le mécanisme ne dépendant pas du domaine, mais reste une extrapolation.

---

## 13.5 Découverte progressive et économie de contexte

### Le coût des catalogues

Les définitions d'outils sont du contexte permanent, au même titre qu'un fichier AGENTS.md. Un hôte branché sur de nombreux serveurs MCP charge toutes leurs descriptions avant la première demande. Anthropic rapporte, d'après ses mesures internes, un exemple de cinq serveurs et 58 outils qui consomment environ 55 000 jetons avant le début de la conversation [18]. Le second poste est celui des résultats intermédiaires : chaque résultat d'outil traverse la fenêtre, parfois deux fois quand le modèle doit le recopier dans l'appel suivant [17].

### Trois mécanismes

**La recherche d'outils.** Le modèle ne reçoit qu'un outil de recherche et ne charge la définition complète que des outils trouvés. Anthropic annonce, toujours d'après ses essais internes, une réduction de 85 % des jetons consommés et une meilleure précision dans le choix de l'outil [18].

**L'exécution de code.** Les outils sont présentés comme des fichiers dans une arborescence; l'agent écrit du code qui les appelle, filtre les données dans l'environnement d'exécution et ne renvoie au modèle que le résultat utile [17]. Le billet cite un cas où la consommation passe d'environ 150 000 à 2 000 jetons. La contrepartie est explicite : il faut un environnement d'exécution isolé, avec limites de ressources et surveillance, ce qui ajoute une charge d'exploitation et une surface de sécurité.

**La divulgation à étages.** C'est le principe des skills (section 13.3) : un index léger en permanence, le détail à la demande.

Ces chiffres sont ceux d'un fournisseur, sur ses propres cas; aucune évaluation indépendante n'a été lue.

### Dans le protocole

MCP ne fixe pas encore de mécanisme. La feuille de route d'août 2026 lance un effort consacré à la découverte progressive : définir un mécanisme expérimental, côté serveur, par lequel un client apprend les outils et ressources au fur et à mesure de ses besoins, avec une interaction définie avec le cache [19]. D'ici là, la découverte progressive est une propriété de l'hôte ou de la passerelle, non du protocole (chapitres 5 et 24).

### Le cache, contrainte de conception

L'économie de contexte ne se réduit pas à charger moins. Les fournisseurs de modèles facturent moins cher les préfixes déjà traités. Dans l'API de Claude, par exemple, le préfixe est mis en cache dans l'ordre outils, système, messages; une lecture au cache coûte un dixième du prix d'entrée de base sur la plupart des modèles, jusqu'à un quarantième sur certains, et modifier une définition d'outil invalide tout le cache [20].

Il en résulte une tension de conception. Charger les outils à la demande réduit la fenêtre, mais tout changement au début du préfixe annule le bénéfice du cache. Un contexte bien construit place donc en tête ce qui est stable (politiques, outils de base, index des skills) et à la fin ce qui varie. La révision de juillet 2026 de MCP recommande pour cette raison aux serveurs de renvoyer leurs outils dans un ordre déterministe (chapitre 5); une passerelle qui filtre le catalogue selon l'appelant réduit cet effet (chapitre 24). Côté exploitant, le préfixe stable conditionne aussi le cache KV et le routage (chapitre 44). Le chiffrage de ces arbitrages relève du chapitre 40.

### Préchargé ou juste-à-temps

Le chargement à la demande a son propre coût : l'agent explore, donc il est plus lent, et il peut ne pas trouver. Anthropic décrit la pratique courante comme hybride : un petit noyau préchargé, le reste récupéré par des outils de recherche au fil de la tâche [2]. Le noyau doit rester petit, et la section 13.4 dit pourquoi.

---

## 13.6 Le contexte comme actif gouverné

Si le contexte détermine le comportement, celui qui le rédige programme l'agent. Les skills, les fichiers de consignes, les prompts système et les descriptions d'outils sont donc des artefacts de production, et non de la documentation.

**Les gérer comme du code.** L'étude des fichiers de contexte montre qu'ils évoluent déjà ainsi, sans en avoir la discipline [14]. Il leur faut un dépôt, des versions, une revue, un propriétaire nommé. Une skill ou une consigne sans propriétaire dérive, et l'agent continue de lui obéir. Une consigne ne remplace pas un droit : la séparation des rôles entre agents repose sur des permissions (chapitre 47).

**Tester avant d'adopter.** Les trois évaluations lues convergent sur la méthode : comparer la même tâche avec et sans l'artefact [11][15][16]. C'est le seul moyen de distinguer un contexte utile d'un contexte coûteux. Cette comparaison s'intègre à l'évaluation continue (chapitre 33).

**Contrôler l'origine.** L'extension Skills over MCP fournit des briques : manifeste avec empreintes, identité liée au serveur, approbation révoquée au moindre changement [10]. Elles garantissent la cohérence avec ce que le serveur publie, pas la confiance dans le contenu, la spécification le précise. L'approbation d'une skill tierce relève du même processus que celle d'un serveur MCP : registre interne et revue de sécurité (chapitres 8 et 31).

**Ne pas confondre format portable et comportement portable.** Le format Agent Skills est commun, mais le champ `allowed-tools` est expérimental et les scripts dépendent de l'environnement d'exécution de chaque hôte [6]. Une skill écrite pour un agent doit être réévaluée sur un autre (chapitre 27).

**Remonter à la source.** La prépublication qui sert de cadre à ce chapitre place deux niveaux au-dessus du contexte : l'ingénierie de l'intention, qui encode les priorités et les arbitrages de l'organisation, et l'ingénierie de spécification, qui convertit politiques et procédures en un corpus lisible par machine [1]. Le modèle n'est pas validé empiriquement. Il pointe toutefois un obstacle réel : les politiques d'entreprise vivent dans des PDF et des usages, et aucun format de contexte n'y change rien tant qu'elles n'ont pas été formalisées. Ce travail appartient à la gouvernance du vocabulaire et à la gouvernance interne (chapitres 12 et 39).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Contexte permanent (prompt système, fichier de consignes) | Court; seulement ce que l'agent ne peut pas déduire : conventions inhabituelles, interdits, commandes | Tâche étroite et stable, où un test avec et sans montre un gain |
| Vue d'ensemble d'un dépôt ou d'un domaine | Ne pas en fournir | Documentation absente ou inaccessible à l'agent |
| Fichier de consignes généré automatiquement | Ne pas l'adopter sans test | Gain mesuré sur les tâches propres à l'organisation |
| Savoir-faire procédural | Skill au format Agent Skills, compacte, rédigée et vérifiée par un humain | Procédure qui tient en quelques lignes : l'inscrire dans le contexte permanent |
| Taille d'une skill | Ciblée, au plus trois modules | — |
| Skills de tiers | Revue de sécurité et registre interne avant usage; scripts traités comme du code tiers | Skill sans script, d'un éditeur approuvé |
| Distribution des skills | Dépôt versionné interne | Skills over MCP si hôtes et serveurs la prennent en charge, en acceptant son statut bêta |
| Grand catalogue d'outils | Découverte à la demande à l'hôte ou à la passerelle | Petit parc d'outils : chargement complet, préfixe stable |
| Résultats d'outils volumineux | Filtrage hors de la fenêtre (code exécuté, sous-agent) | Pas d'environnement d'exécution isolé : résumé par l'outil lui-même |
| Ordre du contexte | Stable en tête, variable à la fin, pour préserver le cache | — |
| Travail multi-agents | Fenêtres séparées; seul un résumé remonte | Tâche courte : un seul agent (chapitre 16) |
| Adoption d'un artefact de contexte | Évaluation avec et sans, puis versionnage et propriétaire nommé | — |

---

## Points à retenir

- Le contexte est une ressource finie à rendement décroissant. La performance d'un modèle baisse quand l'entrée s'allonge, et la position de l'information compte.
- Cinq critères servent de grille : pertinence, suffisance, isolation, économie, provenance. Ils viennent d'une prépublication de synthèse et restent une taxonomie de travail.
- Agent Skills standardise un emballage et un chargement en trois niveaux. Le format est passé sous la gouvernance de l'AAIF le 22 octobre 2026.
- Des skills rédigées par des humains améliorent nettement les résultats dans le seul banc d'essai lu; celles que l'agent génère lui-même les dégradent, et la documentation exhaustive n'apporte presque rien.
- Les fichiers de type AGENTS.md changent le comportement des agents et augmentent le coût, sans gain de réussite démontré. La preuve se limite aux agents de programmation.
- Un agent obéit à ce qu'il lit. Chaque ligne de contexte permanent est une instruction exécutée à chaque session, et se paie.
- La découverte progressive des outils relève aujourd'hui de l'hôte ou de la passerelle. MCP en a fait un chantier, sans mécanisme normatif à ce jour.
- Réduire le contexte et préserver le cache sont deux objectifs qui peuvent se contrarier; l'ordre du contexte les concilie.
- Skills, consignes et descriptions d'outils sont des artefacts de production : versions, propriétaire, revue de sécurité, test avec et sans.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [V. V. Vishnyakova — Context Engineering: From Prompts to Corporate Multi-Agent Architecture (arXiv 2603.09619, v2)](https://arxiv.org/pdf/2603.09619) — prépublication.
2. [Anthropic — Effective context engineering for AI agents (29 septembre 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — billet de fournisseur.
3. [Liu et coll. — Lost in the Middle: How Language Models Use Long Contexts (TACL, arXiv 2307.03172)](https://arxiv.org/abs/2307.03172) — résumé lu.
4. [Chroma — Context Rot: How Increasing Input Tokens Impacts LLM Performance (14 juillet 2025)](https://www.trychroma.com/research/context-rot) — rapport technique d'éditeur.
5. [Agent Skills — vue d'ensemble](https://agentskills.io/home)
6. [Agent Skills — spécification](https://agentskills.io/specification)
7. [AAIF — annonce de quatre nouveaux projets (22 octobre 2026)](https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects)
8. [AAIF — billet sur Agent Skills (22 octobre 2026)](https://aaif.io/blog/agent-skills-sharing-team-expertise-across-ai-agents)
9. [MCP — vue d'ensemble des extensions](https://modelcontextprotocol.io/extensions/overview.md)
10. [MCP — extension Skills](https://modelcontextprotocol.io/extensions/skills/overview.md)
11. [Li et coll. — SkillsBench (arXiv 2602.12670, v4)](https://arxiv.org/abs/2602.12670) — prépublication; résumé et première partie du texte lus.
12. [Liu et coll. — Agent Skills in the Wild (arXiv 2601.10338)](https://arxiv.org/abs/2601.10338) — prépublication; résumé lu.
13. [AGENTS.md — site du format](https://agents.md/)
14. [Chatlatanagulchai et coll. — Agent READMEs (arXiv 2511.12884, v2)](https://arxiv.org/abs/2511.12884) — prépublication; résumé lu.
15. [Gloaguen et coll. — Evaluating AGENTS.md (arXiv 2602.11988, v3)](https://arxiv.org/abs/2602.11988) — prépublication; résumé et texte lus.
16. [Lulla et coll. — On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents (arXiv 2601.20404, v2)](https://arxiv.org/abs/2601.20404) — prépublication; résumé et texte lus.
17. [Anthropic — Code execution with MCP (4 novembre 2025)](https://www.anthropic.com/engineering/code-execution-with-mcp) — billet de fournisseur.
18. [Anthropic — Advanced tool use (24 novembre 2025)](https://www.anthropic.com/engineering/advanced-tool-use) — billet de fournisseur, mesures internes.
19. [MCP — feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
20. [Claude — documentation du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
21. [MCP — matrice de prise en charge des extensions](https://modelcontextprotocol.io/extensions/client-matrix.md)
22. [AAIF — projets](https://aaif.io/projects)

Sources secondaires : aucune page secondaire n'a été lue. Les travaux suivants ne sont connus que par la citation qu'en fait [1] : les quatre opérations de LangChain, la taxonomie de dégradation de Drew Breunig, le modèle de délégation de Tomasev et coll.

## Limites de ce chapitre

- **Mode de lecture.** La plupart des pages ont été lues par un outil d'extraction; seuls [1], [6], [9], [10], [19] et [21] l'ont été mot à mot. L'audit du 12 novembre 2026 a relu [3], [7] à [11], [15] et [20] : les chiffres principaux de [11] (v4) et la hausse de coût de [15] (v3) sont confirmés par leurs résumés; les autres chiffres de [11], [15] et [16] restent à recontrôler sur les tableaux des articles.
- **Niveau de preuve.** Le cadre repose sur une prépublication d'une seule auteure [1]. Les cinq études empiriques ([11], [12], [14] à [16]) sont des prépublications, dont trois ne portent que sur des agents de programmation.
- **Chiffres de fournisseurs.** Les gains de jetons de la section 13.5 viennent de billets d'Anthropic, sans reproduction indépendante; les chiffres d'adoption sont ceux des promoteurs des formats; le tarif du cache est celui d'un seul fournisseur.
- **Détails non tranchés.** Un écart entre l'introduction et un tableau de [15] a été relevé; seule la valeur du tableau est reprise. La matrice [21] n'a pas permis de décompte fiable. Les « modules » de [11] peuvent désigner des skills ou des parties de skill. La version de [3] publiée dans TACL n'a pas été lue.
- **Connaissance générale.** La description de la fenêtre de contexte et le rapprochement avec la génération augmentée par récupération en relèvent.
- **Périmètre.** La section 13.4 se limite à AGENTS.md.
