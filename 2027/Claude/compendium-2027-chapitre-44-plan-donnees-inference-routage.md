# Chapitre 44 — Plan de données d'inférence et routage cognitif

*Question directrice : comment réduire la latence et le coût d'inférence à grande échelle sans perdre en précision sur les tâches complexes ?*

> **Version 2 — 12 novembre 2026.** Date de référence des faits : 11 novembre 2026. État de référence : documentation d'agentgateway (« latest »), dépôt d'Agent Router, site de la Gateway API Inference Extension, llm-d 1.0. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [8] et [15] sont des pages de projets, [9] à [13] des prépublications, dont quatre lues par leur seul résumé. Les renvois « chapitre N » pointent vers la table des matières du compendium. Chapitre audité et révisé le 12 novembre 2026.

Un agent appelle un modèle à chaque tour et relit chaque fois presque tout ce qui précède : dans le banc d'essai du chapitre 40, plus de 97 % des jetons sont relus, non produits. À grande échelle, la facture et le délai d'un système agentique se décident donc dans la couche qui achemine ces appels. Le chapitre 24 traitait la passerelle du trafic d'outils; celui-ci traite le trafic vers les modèles.

Deux décisions se prennent sur ce chemin, le choix du modèle et le choix de la réplique, et elles n'obéissent pas aux mêmes signaux. La seconde se standardise sur Kubernetes et ne touche pas à la qualité des réponses; la première reste un pari, que les routeurs mesurés gagnent sur les requêtes faciles et perdent sur les difficiles. Enfin, presque tous les gains chiffrés publiés viennent des projets eux-mêmes.

---

## 44.1 De la passerelle d'API au plan de données d'inférence

Une passerelle d'API répartit des requêtes à peu près équivalentes entre des répliques interchangeables. L'inférence rompt les deux hypothèses.

Les requêtes ne se valent pas : leur coût se compte en jetons, et la réponse est un flux dont la durée dépend de ce que le modèle produit. Les répliques non plus : un serveur de modèles garde en mémoire l'état calculé pour les préfixes déjà vus, de sorte qu'une réplique peut répondre bien plus vite qu'une autre à la même requête (section 44.4). S'ajoute une décision qu'une passerelle d'API ne prenait pas : choisir le modèle, ce qui engage la qualité du résultat.

La Gateway API Inference Extension nomme ce déplacement : elle étend une passerelle conforme à Gateway API en « passerelle d'inférence », dotée d'un routage et d'un équilibrage de charge conscients du modèle [6].

| Décision | Question | Signaux | Effet sur la qualité |
|---|---|---|---|
| Choix du modèle | Quel modèle, avec quel effort de raisonnement ? | Classe de tâche, attributs de la requête, score de difficulté | Direct |
| Choix de la réplique | Quel serveur, parmi ceux qui servent ce modèle ? | État du cache, file d'attente, adaptateurs chargés | Nul : même modèle, même contexte |

« Routage cognitif », expression du commanditaire absente des sources lues, désigne ici la première ligne du tableau; la seconde relève de l'ordonnancement.

---

## 44.2 Passerelles et routeurs ouverts

| Projet | Foyer | Rôle |
|---|---|---|
| agentgateway [3][4][5] | Agentic AI Foundation (AAIF) [1] | Passerelle pour MCP, A2A et l'inférence |
| Agent Router [2] | AAIF [1] | Passerelle d'IA bâtie sur Envoy |
| Gateway API Inference Extension [6] | Projet officiel de Kubernetes | Interface entre passerelle et serveurs de modèles |
| llm-d [7][8] | CNCF, stade Sandbox | Pile de service d'inférence distribuée |

**agentgateway.** Côté modèles, la passerelle se place entre les applications et les fournisseurs, avec une interface unifiée, des garde-fous, des contrôles de coût et une télémétrie OpenTelemetry [3]. La pièce centrale est le *modèle virtuel* : un nom présenté au client, que la passerelle résout vers un modèle concret selon l'une de quatre stratégies [4] : pondérée, par basculement entre cibles classées par priorité, conditionnelle (expression `when` sur la requête) ou par appel externe (*callout*), où un service HTTP reçoit la requête et renvoie le modèle à utiliser.

La quatrième ancre un routage par difficulté : la documentation donne en exemple un service qui note la complexité du prompt. La réponse du service peut aussi réécrire des champs de la requête, dont `reasoning_effort`. Si le service tombe, la passerelle rejette la requête par défaut (`failClosed`, code 503) ou l'envoie à un modèle de repli. La documentation ne mentionne ni routage par coût ni classificateur intégré : l'intelligence du choix reste à fournir [4].

**Agent Router.** Le README lève une ambiguïté : Envoy AI Gateway est devenu Agent Router, projet de l'AAIF. Code, mainteneurs, licence Apache 2.0, CRD, commande `aigw` et images restent inchangés [2]. Le projet expose une API compatible avec celle d'OpenAI devant une vingtaine de fournisseurs hébergés, de l'inférence autohébergée et des serveurs MCP, et centralise justificatifs, routage, quotas et basculement. Son premier étage assure l'authentification et la limitation globale de débit; le second règle l'accès aux modèles autohébergés, avec un sélecteur de point d'accès.

**Gateway API Inference Extension.** Ce projet ne route rien lui-même : il définit le contrat. Une ressource `InferencePool` désigne un ensemble de points d'accès qui exécutent un serveur de modèles; l'Endpoint Picker (EPP) y choisit le meilleur pour chaque requête. Le site publie une référence d'API `v1` à côté de `v1alpha1`, et cite Envoy Gateway, kgateway et GKE Gateway parmi les passerelles étendues [6].

**llm-d.** Fondé par Red Hat, Google Cloud, IBM Research, CoreWeave et NVIDIA, entré à la CNCF en mars 2026, le projet a publié le 20 octobre 2026 une version 1.0 qui stabilise son API de configuration [8][15]. Son routeur se déclare conforme à l'extension d'inférence; son moteur par défaut est vLLM [7], SGLang étant aussi validé en 1.0 [8].

Les deux passerelles de l'AAIF délèguent le choix de la réplique à un sélecteur externe [2][5]. Le site de l'extension réserve son EPP léger aux tests de conformité et renvoie la production vers un EPP existant, tel celui de llm-d [6]. Passerelle et ordonnanceur se choisissent donc séparément.

---

## 44.3 Arbitrage à trois paliers : petit modèle, grand modèle, calcul au moment de l'inférence

L'échelle à trois paliers vient du commanditaire; aucune source lue ne la présente comme un schéma unique. C'est ici une cible de conception, assemblée à partir de trois lignes de recherche.

### Du petit au grand modèle : routeur ou cascade

Le **routeur** décide avant l'appel (chapitre 16). RouteLLM entraîne, sur des données de préférences humaines, des routeurs qui choisissent entre un modèle fort et un modèle faible. Son résumé annonce des coûts réduits de plus de moitié dans certains cas, sans perte de qualité sur ses bancs d'essai, et une tenue des routeurs quand la paire de modèles change [9].

La **cascade** décide après. FrugalGPT apprend quelles combinaisons de modèles employer selon la requête. Son résumé annonce jusqu'à 98 % de réduction de coût à performance égale au meilleur modèle de l'époque [10].

Ces prépublications de 2023 et 2024 rapportent les chiffres de leurs auteurs, sur des modèles depuis remplacés. Par construction, le routeur ajoute peu de délai mais se trompe sans le savoir, tandis que la cascade paie un double appel pour chaque requête escaladée.

### Le troisième palier est un autre axe

Le calcul au moment de l'inférence (*test-time compute*) consiste à dépenser plus de calcul sur une requête sans changer de modèle. Snell et ses coauteurs en étudient deux formes, la recherche guidée par un modèle vérificateur et l'ajustement adaptatif de la distribution de sortie; leur résumé en tire trois constats [11] :

- l'efficacité de chaque approche varie fortement selon la difficulté du prompt;
- une allocation adaptative, requête par requête, est plus de quatre fois plus efficace qu'une base de type « meilleur de N »;
- à calcul égal, un petit modèle ainsi aidé peut dépasser un modèle quatorze fois plus gros, mais seulement sur les problèmes où il obtient déjà un taux de succès non négligeable.

Le troisième palier n'est donc pas un échelon au-dessus du grand modèle, mais un second axe, l'effort, qui se combine à la taille. Un problème hors de portée d'un modèle ne se rattrape pas par l'effort.

### Ce que montre une mesure indépendante

RouterArena, plateforme de l'Université Rice, compare douze routeurs, trois commerciaux et neuf ouverts ou universitaires, sur 8 400 requêtes réparties en neuf domaines et trois niveaux de difficulté [13].

- Aucun routeur n'arrive en tête sur toutes les mesures.
- Les routeurs commerciaux ne font pas nécessairement mieux que les ouverts. Deux d'entre eux, Not Diamond et Azure Model Router, atteignent la même précision, 68,0 % et 68,1 %, pour 9,34 $ et 0,54 $ par millier de requêtes.
- Les routeurs reconnaissent mal les cas où un modèle moins cher suffit.
- La plupart dépassent 89 % de précision sur les requêtes faciles et tombent souvent sous 10 % sur les difficiles.
- La robustesse aux reformulations et aux fautes de frappe est faible chez les routeurs commerciaux comme chez les universitaires fondés sur BERT.

Ce banc d'essai porte sur des questions isolées. Dans une boucle d'agent, une erreur à une étape se propage aux suivantes (chapitre 21), et un mauvais aiguillage coûte davantage. Le chapitre 40 donne un ordre de grandeur sur une tâche documentaire : coût réduit de moitié, 1,7 point de F1 perdu.

Trois règles en découlent. Le routage s'active par classe de tâche, non globalement. Une requête de classe inconnue va au palier supérieur. Le routeur est lui-même un composant à évaluer, y compris sa sensibilité à la forme de la requête.

---

## 44.4 Latence : délai du premier jeton, débit et cache KV

Trois grandeurs décrivent la latence d'un appel. Le délai du premier jeton (*time to first token*, TTFT) court de l'envoi de la requête au début de la réponse; il comprend l'attente en file et le traitement de l'entrée. Le délai entre jetons (ITL) et le débit en jetons par seconde décrivent la génération. Un agent interactif est jugé sur le TTFT, un traitement par lots sur le débit.

Ni llm-d [8] ni la page d'OpenTelemetry sur les métriques d'IA générative, déplacée vers un dépôt non lu [14], ne définissent ces termes : une entreprise fixe sa définition dans son schéma interne (chapitre 33).

### Le cache KV

Pendant le traitement de l'entrée, le serveur calcule pour chaque jeton un état d'attention, dit état KV. S'il le conserve, une requête qui commence par le même préfixe n'a pas à le recalculer. Les prompts se répètent beaucoup : consignes de domaine, exemples d'usage d'outils, contexte long [12]. C'est le mécanisme que les fournisseurs vendent sous le nom de cache de prompts (chapitres 13 et 40), avec la même condition : le stable en tête, le variable à la fin.

La difficulté tient au lieu : le cache vit dans la mémoire d'une réplique. Preble note que les travaux antérieurs sur la réutilisation de l'état KV se limitaient à un seul GPU, alors que le service en production est distribué [12]. Une répartition aveugle disperse les tours d'une même conversation et annule le gain. Envoyer chaque requête là où son préfixe réside surcharge en revanche les répliques populaires. Preble optimise conjointement réutilisation et équilibrage.

llm-d ajoute deux techniques [7][8]. Le délestage hiérarchisé déplace l'état KV vers la mémoire centrale ou le disque au lieu de le perdre. La désagrégation sépare le traitement de l'entrée, limité par le calcul, de la génération, limitée par la mémoire, sur des serveurs distincts.

---

## 44.5 Ordonnancement conscient du cache sur Kubernetes

### La chaîne

La passerelle, conforme à Gateway API, consulte l'EPP par le protocole de traitement externe d'Envoy; l'EPP choisit un point d'accès de l'`InferencePool` d'après les métriques et les capacités des serveurs de modèles, par exemple l'état du cache de préfixes et les adaptateurs LoRA disponibles [6], qui portent les petits modèles spécialisés (chapitre 47). Dans agentgateway, le choix revient dans l'en-tête `x-gateway-destination-endpoint` [5].

Le routeur de llm-d applique une séquence filtrer, noter, choisir, fondée sur des métriques en temps réel, l'affinité de cache et des politiques. Il vise les succès de cache par une technique heuristique ou par un index qui suit, par événements, l'état du cache de tous les serveurs [7]. La version 1.0 ajoute une qualité de service multilocataire et un service « conscient des agents » : routage par session, ordonnancement par priorité de tour, état de l'API Responses conservé entre les tours [8].

### Les gains annoncés

| Technique | Gain annoncé | Configuration et base | Attribution |
|---|---|---|---|
| Routage conscient du cache | Débit de sortie triplé, TTFT deux fois plus court | Llama 3.1 70B, quatre AMD MI300X; contre un tourniquet | Tesla et Red Hat |
| Ordonnancement par latence prédite (expérimental) | TTFT et ITL réduits de 40 % | GPU NVIDIA; contre les heuristiques | Google |
| Désagrégation | Jusqu'à 70 % de jetons par seconde en plus | GPT-OSS, NVIDIA B200; contre vLLM seul | AWS |
| Désagrégation | Débit accru de 10 à 30 % | Deux modèles, AMD MI300X; même infrastructure | Oracle |

Ces chiffres, tirés du README de llm-d [8], viennent du projet et de ses contributeurs; la première base, le tourniquet, est la plus faible possible. Les deux mesures de désagrégation divergent : le gain se mesure sur sa propre charge. Le site de l'extension affirme que l'équilibrage conscient du serveur de modèles « a fait ses preuves », sans chiffre ni auteur [6].

Preble annonce une latence moyenne de 1,5 à 14,5 fois meilleure et une latence au 99e centile de 2 à 10 fois meilleure que celle de systèmes de l'état de l'art, sur des charges réelles et deux modèles ouverts [12]. Mais les auteurs y évaluent leur propre système, qui n'est pas llm-d : la prépublication confirme le principe, pas les chiffres des produits. Aucune évaluation indépendante de llm-d ou de l'extension d'inférence n'a été trouvée.

### Points d'exploitation

Le mode autonome d'agentgateway, où la passerelle accompagne l'EPP en processus voisin, convient à une charge mono-locataire ou liée à une tâche; il ne prend pas en charge `InferencePool` [5]. Par défaut, la passerelle n'accepte de l'EPP que des adresses de points d'accès locaux connus (`validated`). Le mode `passthrough` accepte aussi des noms d'hôtes : un EPP global peut alors viser d'autres grappes, et la surface atteignable s'élargit d'autant.

L'EPP devient un composant critique du chemin de requête; llm-d range la haute disponibilité du routeur parmi ses fonctions d'exploitation [8].

---

## 44.6 Mesurer le compromis entre coût et qualité

L'unité de mesure reste celle du chapitre 40 : le coût par résultat réussi, non le coût par jeton. Un routage qui divise la facture et dégrade le taux de réussite peut augmenter ce coût.

RouterArena fournit une grille en cinq dimensions, transposable à une évaluation interne [13] : précision des réponses, coût réel d'inférence, optimalité du routage (le modèle correct le moins cher a-t-il été choisi ?), robustesse aux perturbations de forme et latence de la décision. Son score combine précision et coût, ce dernier pondéré par défaut à 0,1; ce poids est un choix de politique, à régler sur le coût de l'erreur par classe de tâche.

La méthode proposée ici, à valider, prolonge celle du chapitre 33.

1. Rejouer un échantillon de traces internes sur chaque palier, par classe de tâche.
2. Mesurer pour chaque classe la part des cas où le palier inférieur suffit; n'activer le routage que là où elle est élevée et l'erreur tolérable.
3. Suivre en production le taux d'escalade et l'adéquation du modèle, indicateur de la FinOps Foundation (chapitre 40).
4. Réévaluer à chaque changement de modèle ou de routeur.

Pour la latence, le TTFT, le débit et le taux de succès du cache se mesurent par classe de tâche, à la médiane et au 99e centile, contre la configuration en place et non contre un tourniquet. Ces mesures alimentent les budgets de coût, de délai et de qualité par classe de tâche (chapitre 23).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Premier levier | Cache de préfixe, chez le fournisseur ou sur ses serveurs | — |
| Choix du modèle | Règle explicite par classe de tâche | Service de notation par appel externe, si les traces montrent une part élevée de requêtes faciles |
| Classe inconnue ou routeur en panne | Palier supérieur; rejet ou modèle de repli qualifié d'avance (chapitre 46) | Tâche sans enjeu : palier inférieur |
| Calcul au moment de l'inférence | Réservé aux classes où le modèle réussit déjà en partie | Problème hors de portée : changer de modèle |
| Inférence autohébergée | `InferencePool` et EPP derrière une passerelle conforme | Charge mono-locataire : mode autonome |
| Ordonnancement | Conscient du cache et de la charge | Charges sans préfixe partagé : charge seule |

---

## Points à retenir

- Le plan de données d'inférence prend deux décisions : le modèle, puis la réplique. Seule la première engage la qualité.
- agentgateway et Agent Router, tous deux à l'AAIF, délèguent le choix de la réplique à un sélecteur externe. Agent Router est l'ancien Envoy AI Gateway.
- L'interface `InferencePool` et EPP sépare le choix de la passerelle de celui de l'ordonnanceur; llm-d en est une mise en œuvre parvenue à la version 1.0.
- L'échelle à trois paliers est une cible de conception, non un schéma établi. Le calcul au moment de l'inférence est un axe d'effort, utile là où le modèle réussit déjà en partie.
- Dans la seule comparaison indépendante lue, aucun routeur ne domine; la plupart échouent sur les requêtes difficiles, et beaucoup changent de choix devant une simple reformulation.
- Le cache KV est le cache de prompts vu du côté de l'exploitant. Son gain dépend d'un préfixe stable et d'un routage qui sait où le préfixe réside.
- Les gains chiffrés de l'ordonnancement conscient du cache et de la désagrégation viennent de llm-d et de ses contributeurs. Une prépublication universitaire confirme le principe, pas ces chiffres.
- Le routage s'active par classe de tâche, après rejeu de traces internes, et se juge au coût par résultat réussi.

---

## Sources

Pages primaires lues le 12 novembre 2026 :

1. [Agentic AI Foundation — projets](https://aaif.io/projects)
2. [Agent Router — README du dépôt](https://github.com/theagentrouter/agent-router)
3. [agentgateway — documentation LLM](https://agentgateway.dev/docs/standalone/latest/llm/)
4. [agentgateway — modèles virtuels](https://agentgateway.dev/docs/standalone/latest/documentation/llm/virtual-models/)
5. [agentgateway — routage d'inférence](https://agentgateway.dev/docs/standalone/latest/documentation/llm/inference/)
6. [Gateway API Inference Extension — page d'accueil](https://gateway-api-inference-extension.sigs.k8s.io/)
7. [llm-d — architecture](https://llm-d.ai/docs/architecture)
8. [llm-d — README du dépôt](https://github.com/llm-d/llm-d)
9. [Ong et coll. — RouteLLM (arXiv 2406.18665)](https://arxiv.org/abs/2406.18665) — prépublication; résumé seulement.
10. [Chen, Zaharia et Zou — FrugalGPT (arXiv 2305.05176)](https://arxiv.org/abs/2305.05176) — prépublication; résumé seulement.
11. [Snell et coll. — Scaling LLM Test-Time Compute Optimally (arXiv 2408.03314)](https://arxiv.org/abs/2408.03314) — prépublication; résumé seulement.
12. [Srivatsa et coll. — Preble (arXiv 2407.00023)](https://arxiv.org/abs/2407.00023) — prépublication; résumé seulement.
13. [Lu et coll. — RouterArena (arXiv 2510.00202, version 3)](https://arxiv.org/html/2510.00202v3) — prépublication; texte lu.
14. [OpenTelemetry — métriques d'IA générative](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/) — page déplacée, sans contenu.
15. [llm-d — billets de version](https://llm-d.ai/blog/tags/releases) — extrait du billet de la version 1.0.

Sources secondaires : aucune. Le banc d'essai financier et l'indicateur de la FinOps Foundation sont repris du chapitre 40.

## Limites de ce chapitre

- Les pages ont été lues au moyen d'un outil qui en restitue un résumé. L'audit a relu [1], [2], [4], [6], [8], [12] et [13] : les chiffres cités y sont confirmés, sans recoupement sur le texte brut.
- « Routage cognitif » et l'échelle à trois paliers n'ont pas de source identifiée. Aucun texte lu ne définit « petit modèle » (SLM).
- Les définitions du TTFT, de l'ITL et du cache KV, leur rapprochement avec le cache de prompts et la comparaison entre routeur et cascade viennent de la connaissance générale.
- Le billet de publication de llm-d 1.0 n'a été lu que par son extrait [15]; le README ne rattache pas ses chiffres à cette version. Le statut de l'API `v1` de l'extension d'inférence n'est pas précisé par son site.
- La prise en charge de l'extension d'inférence par Agent Router est déduite de son sélecteur de point d'accès; le README ne cite ni `InferencePool` ni le contributeur d'origine.
- Les pages d'agentgateway sur les contrôles de coût, l'observabilité et les bancs d'essai n'ont pas été lues.
- RouterArena porte sur des questions isolées et des modèles de 2023 à 2025. Aucune mesure indépendante de routage sur des trajectoires d'agents n'a été trouvée.
- Les renvois aux chapitres 13, 16, 21, 23, 24, 33, 40, 46 et 47 ont été vérifiés; aucune contradiction n'a été relevée.
