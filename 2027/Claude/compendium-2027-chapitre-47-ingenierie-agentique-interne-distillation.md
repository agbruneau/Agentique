# Chapitre 47 — Ingénierie agentique interne et distillation

*Question directrice : comment sécuriser le code et les données que produisent des agents, automatiser l'exploitation sans s'exposer, et transférer l'intelligence vers de petits modèles ?*

> **Version 2 — 12 novembre 2026.** Date de référence des faits : 11 novembre 2026. État de référence : documentation d'Apache Iceberg (1.12.0), de Project Nessie, de DSPy (3.5) et de vLLM, dépôts Spec Kit, SCIP et Scientist, et sept articles lus par leur résumé. Les numéros entre crochets renvoient aux sources en fin de chapitre, toutes primaires. Plusieurs éléments demandés par le commanditaire n'ont pas de source : ils sont présentés comme des cibles de conception proposées et recensés dans les limites. Chapitre audité et révisé le 12 novembre 2026.

Les chapitres précédents traitent l'agent comme un consommateur des systèmes de l'entreprise. Celui-ci le traite comme un producteur : il écrit du code, des tables, des commandes d'exploitation et les données qui entraîneront son successeur. Chaque production pose la même question : qui vérifie ce qu'un agent a écrit ?

La thèse du chapitre tient en une règle de séparation. Celui qui produit n'est ni celui qui définit le critère ni celui qui publie. Le contrôle se place sur un artefact intermédiaire qu'un humain ou un programme déterministe peut lire : une spécification, une propriété, un contrat de données, une branche, un catalogue d'actions, un jeu d'évaluation.

---

## 47.1 Agents dans le cycle de développement : séparer la spécification de la construction

### Une construction à rattacher

Le couple « Spécificateur / Bâtisseur » n'a pas été retrouvé sous ce nom dans une source publiée. La pratique documentée la plus proche est le développement piloté par la spécification, que GitHub outille dans Spec Kit, trousse à code source ouvert sous licence MIT [1]. Le dépôt la résume : définir quoi construire et pourquoi, puis tirer de la spécification un plan, des tâches et le code.

Le flux minimal enchaîne six commandes : `/speckit-constitution` (principes du projet), `/speckit-specify` (spécification), `/speckit-plan` (choix techniques), `/speckit-tasks` (découpage), `/speckit-implement` (code) et `/speckit-converge` (vérification), les deux dernières se répétant jusqu'à convergence. Le dépôt demande d'exécuter les étapes une à la fois et de relire chaque résultat avant de continuer [1].

Le chapitre 25 rapporte la même structure dans la modernisation de code patrimonial : un expert valide les spécifications avant toute génération, et une erreur de spécification se propage au code.

### Pourquoi séparer

La spécification est le seul artefact qu'un responsable d'affaires peut relire en entier; un diff de plusieurs milliers de lignes, non. Le contrôle humain s'y place.

La séparation répond aussi à un défaut propre aux agents : celui qui écrit le code et ses tests dans le même contexte valide ses propres hypothèses. Le chapitre 34 pose le principe général, selon lequel le modèle propose et une barrière indépendante autorise.

### Une cible de conception proposée

Spec Kit sépare des étapes, pas des identités : un même agent peut les parcourir toutes. La séparation en deux rôles dotés de droits distincts est une extrapolation de ce chapitre, à valider :

- le spécificateur lit le besoin et le code, écrit la spécification et les critères d'acceptation, et n'a aucun droit d'écriture sur le code;
- le bâtisseur lit la spécification, écrit le code, et ne peut modifier ni la spécification ni les tests d'acceptation;
- le passage de l'un à l'autre est un point d'approbation humaine (chapitre 22).

Le chapitre 13 rappelle qu'un fichier de type `AGENTS.md` change le comportement et le coût sans gain de réussite démontré : la séparation doit reposer sur des droits, pas sur une consigne.

---

## 47.2 Donner le code à lire : arbres syntaxiques et index de symboles

Un agent qui explore un dépôt par recherche textuelle confond les homonymes et manque les appels indirects. Deux structures corrigent ce défaut. L'arbre syntaxique abstrait (AST) donne la structure d'un fichier : fonctions, blocs, signatures. L'index de symboles relie les fichiers entre eux : où un symbole est défini, où il est utilisé, qui le met en œuvre.

SCIP (SCIP Code Intelligence Protocol), de Sourcegraph, est un format ouvert pour le second [2] : un protocole indépendant du langage pour indexer du code source, qui alimente l'accès à la définition, la recherche de références et celle des mises en œuvre. Il fournit un schéma Protobuf, un outil en ligne de commande et des liaisons pour Go et Rust, sous licence Apache 2.0. Des indexeurs existent pour Java, Scala, Kotlin, TypeScript, JavaScript, Rust, C, C++, Ruby, Python, C#, Visual Basic, Dart et PHP.

**L'usage par des agents est une inférence** : la page lue parle de navigation dans le code, pas d'agents, et ne chiffre aucun gain.

**L'index s'expose comme un outil borné.** Des outils « définition de X » et « références de X », servis par MCP (chapitre 5), donnent à l'agent une réponse exacte au lieu de fichiers entiers. C'est l'économie de contexte du chapitre 13 appliquée au code.

**La couverture s'arrête où commence le patrimoine.** La liste d'indexeurs lue ne contient ni COBOL ni RPG. Pour ces langages, l'index vient de l'outillage de l'éditeur ou n'existe pas (47.4).

Un index périmé trompe l'agent, qui s'y fie : il se régénère à chaque fusion et se rattache à un commit précis.

---

## 47.3 Vérifier ce qu'un agent écrit : tests par propriétés et tests de mutation

Un agent produit volontiers des tests qui passent, et la couverture de lignes mesure ce que les tests exécutent, pas ce qu'ils détectent. Deux techniques résistent mieux à la complaisance.

### Tests par propriétés

Un test par propriétés énonce un invariant plutôt qu'un exemple : sérialiser puis désérialiser rend l'objet d'origine. Un générateur cherche ensuite des entrées qui le violent.

Une prépublication d'octobre 2025 décrit un agent qui infère des propriétés à partir du code et de la documentation de modules Python, écrit et exécute les tests, puis rédige des rapports de bogue [3]. Sur 100 paquets répandus, 56 % des rapports étaient des bogues valides après revue manuelle, et 32 % méritaient un signalement aux mainteneurs. Parmi les 21 rapports les mieux classés par une grille de priorité, 86 % étaient valides. Les auteurs ont signalé cinq bogues, dont quatre avec un correctif; trois correctifs ont été fusionnés.

La méthode trouve de vrais défauts, mais près d'un rapport sur deux est faux : sans classement ni revue humaine, elle produit du bruit.

### Tests de mutation

Un test de mutation injecte une faute dans le code (un mutant) et vérifie qu'un test échoue. Un mutant qui survit révèle un test absent ou trop faible.

Meta a publié le bilan de son système ACH [4]. ACH génère peu de mutants, ciblés sur une préoccupation précise (la confidentialité) et sur des fautes non détectées, puis les tests qui les tuent. Appliqué à 10 795 classes Kotlin de sept plateformes, il a produit 9 095 mutants et 571 tests. Les ingénieurs ont accepté 73 % des tests proposés. Le point délicat est le mutant équivalent, qui ne change pas le comportement et qu'aucun test ne peut tuer : l'agent de détection atteignait une précision de 0,79 et un rappel de 0,47, portés à 0,95 et 0,96 par un prétraitement simple.

### Le seuil de 85 %

Le seuil « score de mutation ≥ 85 % » n'a pas de source. Le bilan de Meta suggère qu'un score global est le mauvais objet : les mutants équivalents en faussent le dénominateur, et ACH vise des fautes choisies plutôt qu'un pourcentage. Une cible reste utile comme barrière de fusion, à trois conditions : la calculer sur le code modifié, la calibrer par module à partir du score observé avant l'arrivée des agents, et exclure les mutants équivalents reconnus.

Les propriétés et les mutants ciblés se tirent de la spécification (47.1), pas du code écrit par le bâtisseur. Sinon le test hérite de l'erreur qu'il devait détecter.

---

## 47.4 Moderniser par remplacement graduel et exécution en miroir

Le chapitre 25 décrit le figuier étrangleur : remplacer un système par parties, avec la parité de comportement comme critère de sortie. Reste à établir cette parité.

### L'exécution en miroir

Le terme « Shadow Mirroring » n'a pas été retrouvé dans une source. La pratique qu'il désigne est documentée : exécuter l'ancien et le nouveau chemin sur les mêmes entrées, ne servir que l'ancien, et comparer. La bibliothèque Scientist de GitHub en fixe le vocabulaire [5]. Une expérience oppose un contrôle (le code existant) à un candidat (le nouveau). Le résultat du contrôle est toujours renvoyé. Les deux blocs s'exécutent dans un ordre aléatoire; durées, exceptions du candidat et écarts sont publiés vers un système de mesure.

Ses limites valent au-delà de Ruby [5] :

- la technique n'est sûre que pour du code qui ne modifie pas de données;
- pour les écritures, il recommande d'écrire dans les deux systèmes, puis de comparer à la lecture;
- des données partagées peuvent changer entre les deux exécutions et créer de faux écarts; comparer d'abord le contrôle à lui-même mesure ce bruit;
- la technique ne protège pas d'un candidat lent.

### Sur du code RPG ou COBOL

Le chapitre 25 documente une chaîne d'agents pour COBOL, PL/I et JCL. Aucune source lue ne traite RPG : l'application à ce langage est une extrapolation. Sur un traitement par lots, le miroir devient une exécution parallèle : les deux systèmes traitent le même fichier d'entrée, et les sorties sont rapprochées enregistrement par enregistrement.

Le critère « 30 jours à 0,00 $ d'écart » n'a pas de source. Comme cible de conception, sa forme se défend, sa durée se discute :

- un écart monétaire nul est le bon critère pour un calcul qui fait foi; une tolérance cache des erreurs d'arrondi qui s'accumulent;
- la fenêtre doit couvrir au moins un cycle d'affaires complet, clôture périodique comprise; trente jours couvrent une fin de mois, pas une fin d'exercice;
- chaque écart ignoré est une décision signée, pas un réglage de l'agent.

L'agent écrit le candidat et trie les écarts en proposant une cause. La bascule appartient à un responsable humain, sur la foi d'un rapprochement que l'agent n'a pas produit.

---

## 47.5 Pipelines de données : contrats et patron Write-Audit-Publish

Un agent qui écrit dans une table de production pose le même problème, sans ancien système pour comparer.

**Le contrat.** L'Open Data Contract Standard, en version 3.2.0 selon le chapitre 15 (une 4.0.0 est annoncée), décrit l'entente entre un producteur de données et ses consommateurs. Pour un agent producteur, il joue le rôle de la spécification : il est écrit avant le pipeline, par une autre partie, et les contrôles d'audit en dérivent.

**La zone d'attente.** Le patron Write-Audit-Publish écrit les données à l'écart, les vérifie, puis les publie. Apache Iceberg le met en œuvre par ses branches [6]. Branches et étiquettes y sont des références nommées à des instantanés. Le flux de la branche d'audit tient en cinq étapes :

1. activer la propriété `write.wap.enabled` sur la table;
2. créer une branche à partir d'un instantané;
3. diriger les écritures de la session vers elle par `spark.wap.branch`;
4. valider l'état de la branche, par exemple par des contrôles de qualité;
5. avancer `main` jusqu'à la tête de la branche par la procédure `fast_forward`.

Les écritures restent hors de l'historique principal jusqu'à la dernière étape. Le schéma de la table, en revanche, vaut pour toutes les branches : une branche n'isole pas un changement de schéma [6].

**Plusieurs tables.** La page d'Iceberg décrit des branches par table. Project Nessie, catalogue transactionnel pour lacs de données, se présente comme un contrôle de version des données inspiré de Git, avec transactions et visibilité inter-tables, et fonctionne avec les tables Iceberg [7]. C'est l'option quand la publication doit porter sur plusieurs tables à la fois.

Pour un agent, le patron se traduit en droits. L'agent écrit sur une branche et nulle part ailleurs. L'audit est un programme déterministe tiré du contrat, que l'agent ne peut pas modifier. La publication est un droit distinct, détenu par le pipeline ou par un humain. Cette lecture est une inférence, comme l'usage d'ODCS pour les agents au chapitre 15.

---

## 47.6 Exploitation : remédiation automatisée et injection par les journaux

Le chapitre 34 gradue l'autonomie d'un agent d'exploitation. Cette section développe un risque qu'il ne fait que signaler (34.6) : les journaux que l'agent lit pour diagnostiquer sont du contenu non fiable, au sens du chapitre 31.

### Deux démonstrations

Une prépublication d'avril 2026, LogJack, mesure l'injection indirecte par des journaux infonuagiques contre des agents de débogage [8]. Le banc d'essai compte 42 charges dans cinq catégories de journaux; huit modèles sont évalués. Quand l'agent est invité à corriger, le taux d'exécution littérale de la commande injectée va de 0 % à 86,2 % selon le modèle. Une consigne de ne rien exécuter ramène la plupart des modèles à 0 %, mais l'un d'eux exécute encore dans 30 % des essais. Une charge de téléchargement et d'exécution de code réussit sur six modèles sur huit. Les garde-fous des trois grands fournisseurs infonuagiques échouent pour l'essentiel : l'un n'intercepte qu'une des 32 charges évaluées, un autre aucune, alors que tous deux détectent ces charges présentées isolément. Certains modèles retirent la partie manifestement malveillante, puis exécutent le reste.

Une seconde prépublication, d'août 2025, montre que l'attaquant n'a besoin d'aucune connaissance préalable du système visé [9]. Il envoie des requêtes qui provoquent des erreurs; celles-ci produisent une télémétrie plausible mais fausse, qui oriente l'agent vers une action nuisible qu'il croit optimale. La défense proposée, AIOpsShield, assainit la télémétrie en tirant parti de sa structure et de la faible place qu'y occupe le contenu fourni par l'utilisateur. Le résumé la dit fiable, sans chiffre.

### Ce qui en découle

Quiconque peut envoyer une requête à un service exposé peut écrire dans ses journaux. Un agent de remédiation réunit alors une variante de la trifecta du chapitre 31, qui remplace le canal sortant par la capacité d'agir : contenu non fiable, accès privilégié, droit d'exécuter. Les mesures qui tiennent sont architecturales :

- **séparer le diagnostic de l'action** : l'agent qui lit les journaux propose; il n'exécute pas;
- **borner l'action** : la remédiation se choisit dans un catalogue de procédures paramétrées, jamais sous forme de commande libre; une commande lue dans un journal ne figure dans aucun catalogue;
- **assainir en amont** : ne transmettre à l'agent que les champs structurés et isoler les champs libres;
- **ne pas compter sur le filtre** : les deux sources montrent des garde-fous de contenu contournés ou inadaptés.

Ces prépublications, dont l'une d'un auteur unique, établissent que l'attaque est possible, pas sa fréquence en production.

---

## 47.7 Boucle de données et optimisation de prompts

La boucle de données (*data flywheel*) est le circuit par lequel les traces de production deviennent des exemples, puis des prompts ou des modèles améliorés, qui produisent de nouvelles traces.

### Trois risques à l'entrée de la boucle

**Les traces contiennent des données sensibles.** Le chapitre 33 rappelle que le contenu des échanges est exclu de la télémétrie par défaut. La boucle exige ce contenu : elle le lit par référence, sous contrôle d'accès, après masquage. Les exemples qui en sont tirés suivent les règles de conservation et d'effacement (chapitre 38).

**Un modèle mémorise ce qu'il a vu.** Carlini et ses coauteurs proposent une méthode pour mesurer le risque qu'un modèle génératif mémorise involontairement des séquences rares de ses données d'entraînement [10]. Cette mémorisation, concluent-ils, est persistante et difficile à éviter; ils extraient des secrets, tels des numéros de carte de crédit, de modèles non protégés, et appliquent la méthode à Smart Compose, entraîné sur des courriels. Les « canaris » en sont l'instrument : des séquences artificielles uniques, glissées dans le jeu d'entraînement, dont on mesure ensuite l'exposition dans le modèle. Ce canari n'est pas le déploiement canari du chapitre 34. Il s'insère à chaque cycle d'affinage; s'il ressort, la publication est bloquée.

**La boucle recycle les injections.** Une trace contient le contenu que l'agent a lu, y compris hostile (47.6). Promue en exemple, elle devient une instruction permanente.

### L'optimisation de prompts

L'optimiseur MIPROv2 de DSPy (chapitre 20) ajuste conjointement les instructions et les exemples d'un programme [11]. Il procède en trois temps : il exécute le programme sur des exemples d'entraînement et garde les sorties correctes comme démonstrations candidates; un modèle rédige des instructions candidates à partir d'un résumé des données, du code et de ces démonstrations; une optimisation bayésienne cherche la meilleure combinaison sur un nombre fixé d'essais. Une métrique et un jeu d'entraînement sont obligatoires.

Deux conséquences. La métrique devient le critère de fait : un optimiseur exploite ses faiblesses, d'où l'étalonnage contre des étiquettes humaines demandé au chapitre 33. Et les démonstrations retenues sont des extraits du jeu d'entraînement placés dans le prompt : si ce jeu vient de la production, une donnée de client peut se retrouver dans chaque appel. Le jeu d'optimisation se filtre donc comme un jeu d'entraînement, et le prompt produit passe la barrière de rejeu du chapitre 34.

---

## 47.8 Distillation vers de petits modèles

Distiller, c'est entraîner un petit modèle (l'élève) sur les sorties d'un grand (l'enseignant), pour une tâche étroite. Les motifs sont le coût, la latence et la maîtrise du lieu d'exécution (chapitres 37, 40, 44 et 46).

Au chapitre 17, Qwen3-14B, guidé par un plan structuré, passe de 83,3 % à 95,5 % de précision des appels d'outils une fois affiné sur des exemples distillés (prépublication, scénario de ressources humaines). La pratique reste minoritaire : 14 des 20 études de cas du chapitre 4 n'ajustent aucun poids. Avant d'entraîner, un optimiseur de prompts peut déjà adapter le programme au petit modèle (47.7, chapitre 20).

### Les briques sourcées

**LoRA** gèle les poids du modèle et entraîne de petites matrices de rang faible insérées dans chaque couche [12]. L'article de 2021 rapporte, sur GPT-3, environ 10 000 fois moins de paramètres entraînables et trois fois moins de mémoire de processeur graphique, sans latence ajoutée à l'inférence, pour une qualité égale ou supérieure à l'affinage complet sur les modèles testés.

**DPO** apprend des préférences : des paires où une sortie est jugée meilleure qu'une autre [13]. Il remplace la chaîne en deux étapes de l'apprentissage par renforcement à partir de retours humains par une simple perte de classification, que les auteurs disent stable et légère.

**Le service multi-adaptateurs** existe dans vLLM [14]. Plusieurs adaptateurs LoRA sont servis sur un seul modèle de base (`--enable-lora`, `--lora-modules`); la requête choisit l'adaptateur par son champ `model`, et `max_loras` borne le nombre d'adaptateurs actifs dans un lot. Le chargement à chaud, activé par `VLLM_ALLOW_RUNTIME_LORA_UPDATING`, est possible, mais la documentation avertit qu'il comporte des risques de sécurité et ne doit pas servir en production hors d'un environnement isolé et de confiance.

### La recette demandée

Aucune source lue ne décrit « Multi-LoRA (SFT + DPO) » comme une méthode nommée. C'est une composition de ces briques, présentée ici comme cible de conception à valider :

| Étape | Donnée | Produit |
|---|---|---|
| Affinage supervisé (SFT) | Sorties de l'enseignant, validées par l'évaluation | Un adaptateur par tâche |
| Préférences (DPO) | Paires issues des corrections humaines ou d'un juge étalonné | L'adaptateur, raffiné |
| Service | Un modèle de base, plusieurs adaptateurs | Routage par tâche; l'ordonnanceur voit les adaptateurs chargés (chapitre 44) |

### Quatre précautions

- **L'élève hérite des erreurs de l'enseignant.** Seules les sorties vérifiées entrent dans le jeu d'entraînement; l'élève se mesure sur le banc interne du chapitre 33, pas contre l'enseignant.
- **Un repli reste nécessaire** vers le grand modèle, hors de la tâche apprise (chapitre 44).
- **Un adaptateur est un artefact de chaîne d'approvisionnement.** Il se signe (chapitre 46), se versionne avec le modèle de base auquel il est lié, et se charge au démarrage plutôt qu'à chaud.
- **Les droits sur les sorties de l'enseignant se vérifient.** Les conditions d'utilisation des fournisseurs de modèles n'ont pas été lues pour ce chapitre.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Rôles de développement | Spécification et construction séparées par des droits, approbation humaine entre les deux | Prototype jetable |
| Lecture du code | Index de symboles exposé par outils bornés | Petit dépôt, ou langage sans indexeur |
| Tests écrits par l'agent | Propriétés et mutants tirés de la spécification | Code sans invariant exprimable : exemples relus par un humain |
| Barrière de mutation | Seuil calibré par module, sur le code modifié | Jamais un seuil global unique |
| Parité d'un remplacement | Exécution en miroir, écart nul, un cycle d'affaires complet | Écritures : double écriture et comparaison à la lecture |
| Écriture de données | Branche, audit déterministe tiré du contrat, publication distincte; catalogue transactionnel si plusieurs tables | Table d'exploration non partagée |
| Remédiation | Journaux tenus pour non fiables; l'agent propose, l'action vient d'un catalogue | Boucle fermée selon l'échelle du chapitre 34 |
| Boucle de données | Masquage, canaris de mémorisation, filtrage des injections | — |
| Prompts | Optimiseur si métrique étalonnée et exemples filtrés | Sinon, prompts rédigés et versionnés |
| Petit modèle | Adaptateur par tâche, chargé au démarrage, avec repli | Tâche ouverte ou rare : grand modèle |

---

## Points à retenir

- Une même règle traverse le chapitre : l'agent qui produit ne définit pas le critère et ne publie pas. Le contrôle se place sur un artefact intermédiaire lisible.
- Le développement piloté par la spécification est une pratique outillée. La séparation en deux rôles à droits distincts en est une extrapolation, à valider.
- Un agent qui génère des tests par propriétés trouve de vrais bogues, mais près d'un rapport sur deux est faux dans la seule étude lue. Les tests de mutation ciblés ont un bilan industriel publié; aucun seuil global, dont celui de 85 %, n'a de source.
- L'exécution en miroir n'est sûre que pour du code qui ne modifie pas de données. Les écritures exigent une double écriture et une comparaison à la lecture.
- Le patron Write-Audit-Publish existe nativement dans Iceberg par table; la publication de plusieurs tables demande un catalogue transactionnel comme Nessie.
- Les journaux sont une surface d'injection démontrée, que les garde-fous de contenu testés n'arrêtent pas. La parade est un catalogue d'actions bornées.
- La boucle de données réinjecte ce que la production a vu : données personnelles, secrets et injections. Elle se filtre et se teste par des canaris.
- LoRA, DPO et le service multi-adaptateurs sont documentés séparément. Leur assemblage en recette de distillation n'est décrit par aucune source lue.

---

## Sources

Pages primaires lues le 12 novembre 2026 :

1. [GitHub — Spec Kit](https://github.com/github/spec-kit)
2. [Sourcegraph — SCIP Code Intelligence Protocol](https://github.com/sourcegraph/scip)
3. [Maaz et coll. — Agentic Property-Based Testing, arXiv:2510.09907](https://arxiv.org/abs/2510.09907) — résumé
4. [Foster et coll. — Mutation-Guided LLM-based Test Generation at Meta, arXiv:2501.12862](https://arxiv.org/abs/2501.12862) — résumé
5. [GitHub — Scientist](https://github.com/github/scientist)
6. [Apache Iceberg — Branching and Tagging](https://iceberg.apache.org/docs/latest/branching/)
7. [Project Nessie — accueil](https://projectnessie.org/)
8. [Shah — LogJack, arXiv:2604.15368](https://arxiv.org/abs/2604.15368) — résumé
9. [Pasquini et coll. — When AIOps Become « AI Oops », arXiv:2508.06394](https://arxiv.org/abs/2508.06394) — résumé
10. [Carlini et coll. — The Secret Sharer, arXiv:1802.08232](https://arxiv.org/abs/1802.08232) — résumé
11. [DSPy — MIPROv2](https://dspy.ai/current/api/optimizers/MIPROv2/)
12. [Hu et coll. — LoRA, arXiv:2106.09685](https://arxiv.org/abs/2106.09685) — résumé
13. [Rafailov et coll. — Direct Preference Optimization, arXiv:2305.18290](https://arxiv.org/abs/2305.18290) — résumé
14. [vLLM — LoRA Adapters](https://docs.vllm.ai/en/latest/features/lora.html)

Aucune source secondaire n'est citée. Les faits repris d'autres chapitres reposent sur leurs sources, non relues ici.

## Limites de ce chapitre

- **Éléments demandés sans source.** « Spécificateur / Bâtisseur », « Shadow Mirroring » et « Multi-LoRA (SFT + DPO) » n'ont pas été retrouvés comme termes ou méthodes publiés; ils sont rattachés à des pratiques voisines et présentés comme cibles de conception. Les seuils « ≥ 85 % » et « 30 jours à 0,00 $ d'écart » n'ont aucune source. Rien n'a été lu sur RPG. « Data Flywheel » n'a pas de définition sourcée.
- **Audit du 12 novembre 2026.** [1], [2], [4], [6], [8], [9], [11] et [14] relus : faits confirmés, l'attaque de [9] et le comptage de [8] précisés. Renvois vérifiés, dont ceux vers le chapitre 44.
- **Canaris.** Le résumé lu de l'article de Carlini ne décrit ni les canaris ni la métrique d'exposition; leur description vient de la connaissance générale du texte complet.
- **Connaissance générale.** Les définitions de l'AST, du test par propriétés, du test de mutation et de la distillation, l'exécution parallèle sur traitement par lots et le rôle de `max_loras`, absent de la page de vLLM, ne viennent pas d'une page lue.
- **Articles.** Les sept articles n'ont été lus que par leur résumé. [3], [8] et [9] sont des prépublications.
- **Versions.** Iceberg 1.12.0 et DSPy 3.5 sont tirés de la navigation des sites (DSPy 3.5.0 selon le chapitre 20); Nessie, vLLM et Spec Kit n'affichent aucune version courante, et Spec Kit ne décrit pas les artefacts de chaque étape.
- **Aucune mesure** n'a été lue sur le gain d'un index de symboles pour un agent, ni sur un élève distillé par la recette décrite.
