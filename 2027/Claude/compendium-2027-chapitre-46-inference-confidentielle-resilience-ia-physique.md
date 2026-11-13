# Chapitre 46 — Inférence confidentielle, résilience et IA physique

*Question directrice : comment protéger les actifs cognitifs, survivre à la perte d'un fournisseur de modèles ou d'une liaison, et piloter des machines mobiles en sécurité ?*

> **Version 2 — 12 novembre 2026.** Date de référence des faits : 11 novembre 2026. État de référence : documentation d'Intel, de Google Cloud, de NVIDIA et d'AWS, spécification TUF 1.0.37 (8 octobre 2026), ISO 10218-1:2025 et IEC 61508-1:2010 par leur seule page de présentation. Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [14] sont des pages primaires lues pour ce chapitre, [15] n'est connue que par [11]. Les seuils demandés par le commanditaire et restés sans source sont présentés comme des cibles de conception à valider. Chapitre audité et révisé le 12 novembre 2026.

Trois dépendances échappent à l'entreprise agentique : l'exploitant infonuagique qui exécute le modèle, le fournisseur qui le publie, la liaison qui relie un site au reste. Une quatrième s'ajoute quand l'agent pilote une machine : un contrôleur appris, dont personne ne sait prouver le comportement.

La thèse de ce chapitre est que ces quatre cas se traitent de la même façon. La garantie ne vient pas du composant complexe, mais d'un mécanisme plus simple placé autour de lui : une attestation matérielle et une clé détenue, un modèle de secours qualifié d'avance, un quota de droits alloué avant la panne, un contrôleur vérifié. Chacun de ces mécanismes a une limite documentée, que le chapitre nomme.

---

## 46.1 Les états d'un agent et leur localisation

Le chapitre 37 établit que résidence et contrôle juridictionnel sont deux questions, et que l'analyse se fait par composant. Il faut descendre d'un cran : un agent ne garde pas un état, il en garde plusieurs, chez des exploitants différents.

| État | Où il vit d'ordinaire | Protection applicable |
|---|---|---|
| Modèle et configuration : poids, prompts système, catalogue d'outils | Fournisseur de modèles ou site | Signature des artefacts (46.8), attestation (46.2) |
| Contexte en cours d'inférence : prompt, résultats d'outils, caches | Mémoire du serveur d'inférence | Environnement d'exécution de confiance (46.2) |
| Mémoire persistante (chapitre 14) | Fichiers, base vectorielle, graphe; parfois chez le fournisseur de modèles | Chiffrement au repos, clés détenues (46.3) |
| État d'exécution durable (chapitre 18) | Moteur d'exécution | Idem |
| Traces et journaux d'audit (chapitre 33) | Plateforme d'observabilité | Idem |
| Secrets : jetons, clés | Coffre, module matériel de sécurité | Libération sous attestation (46.2, 46.3) |

Cette grille est une proposition, sans source. Le découpage importe moins que la règle qu'il sert : chaque état reçoit un exploitant, une région et un détenteur de clé.

Le géorepérage, soit l'épinglage de chaque état à une région, répond à la résidence. Il ne répond pas au CLOUD Act, dont le critère est le contrôle exercé par le fournisseur et non le lieu du serveur (chapitre 37). Deux leviers techniques réduisent ce qu'un exploitant peut remettre : des clés hors de sa portée et une exécution qu'il ne peut pas lire. Aucun n'est une réponse juridique.

---

## 46.2 Inférence confidentielle : environnements d'exécution de confiance sur processeur et sur GPU

Le chiffrement au repos et en transit laisse la donnée en clair pendant le calcul. Un environnement d'exécution de confiance (TEE) vise cet intervalle.

### Sur processeur

Intel TDX crée des domaines de confiance, des machines virtuelles isolées par le matériel. La mémoire est chiffrée et, selon Intel, opaque pour le fournisseur infonuagique et ses opérateurs; l'attestation confirme que la configuration matérielle et logicielle est celle attendue [1].

AMD SEV chiffre la mémoire d'une machine virtuelle. SEV-SNP y ajoute une protection contre un hyperviseur malveillant, notamment le rejeu de données et le remappage de mémoire, et un rapport d'attestation peut être demandé à tout moment [2].

Dans les deux cas, l'unité protégée est la machine virtuelle entière : l'application n'est pas réécrite, mais tout le système invité entre dans la base de confiance.

### Sur GPU

NVIDIA Confidential Computing étend la frontière au GPU, en s'appuyant sur SEV ou TDX : les données des charges accélérées sont chiffrées en cours d'usage et isolées de l'hyperviseur [2]. NVIDIA décrit trois modalités, soit machine nue, machine virtuelle et conteneur, et précise que leurs garanties ne sont pas interchangeables [3].

### Une preuve, pas une politique

NVIDIA le formule nettement : l'attestation fournit une preuve pour une décision de confiance, elle ne remplace pas la politique qui gouverne la libération des secrets [3]. Un service courtier de clés ne remet les secrets qu'après évaluation de la preuve. Il revient à l'entreprise d'écrire cette politique : quelles mesures, quelles versions de micrologiciel, quel vérificateur.

La même page ajoute que ces frontières ne protègent pas d'elles-mêmes les données de l'utilisateur final contre le propriétaire du modèle [3]. Un TEE écarte l'exploitant de l'infrastructure; celui qui fournit le code exécuté à l'intérieur reste de confiance.

### Limites documentées

NVIDIA écrit que ses frontières n'éliminent ni les risques du matériel partagé ou de l'interconnexion, ni les risques physiques, ni les canaux auxiliaires [3]. Google ne prête à TDX qu'une défense contre des formes limitées d'attaques par accès physique à la mémoire [2].

L'attaque TEE.fail en donne la mesure. Un interposeur placé sur le bus mémoire DDR5 exploite le caractère déterministe du chiffrement. Ses auteurs disent avoir extrait la clé qui permet de forger des attestations TDX acceptées par la bibliothèque de vérification d'Intel, et les clés privées ECDSA d'OpenSSL exécuté dans une machine virtuelle SEV-SNP. Les rapports d'attestation du GPU, ajoutent-ils, ne sont pas liés à la machine virtuelle et peuvent être relayés depuis un autre matériel. Le montage coûterait moins de 1 000 $. Intel et AMD tiennent ces attaques pour hors de leur modèle de menace, et AMD ne prévoit pas de mise à jour de son micrologiciel; seule la sécurité physique du serveur y répond [4].

Un TEE déplace donc la confiance : des logiciels et des administrateurs de l'exploitant vers le fabricant de la puce et la garde physique des serveurs. Or, cette garde appartient à l'exploitant. Contre un exploitant contraint par la loi, un TEE élève le coût de l'accès sans le rendre impossible. Le calcul confidentiel entre plusieurs parties relève du chapitre 45.

---

## 46.3 Maîtrise des clés

La documentation d'AWS sur les magasins de clés externes décrit le modèle Hold Your Own Key (HYOK) [5]. Le matériel de clé reste dans un gestionnaire externe que le client possède : module matériel de sécurité (HSM) physique ou virtuel, ou gestionnaire logiciel. AWS KMS ne lui parle jamais directement; un mandataire fourni par le client relaie chaque requête. Les données sont chiffrées deux fois, par AWS puis par la clé externe.

| Propriété | Conséquence |
|---|---|
| Le client coupe l'accès | Le chiffré devient indéchiffrable; coupure définitive, il est irrécupérable |
| Double chiffrement | AWS ne déchiffre pas sans la clé externe; le client ne déchiffre pas hors d'AWS, même avec sa clé |
| Responsabilité | Disponibilité, durabilité et latence des opérations de clé passent au client |
| Exception | Les clés de données mises en cache par un service fonctionnent jusqu'à l'expiration du cache |

AWS avertit que, pour la plupart des charges, le risque accru pour la disponibilité et la performance dépasse le bénéfice de sécurité perçu. L'éditeur conseille, si possible, un aller-retour réseau de 35 millisecondes ou moins entre sa région et le gestionnaire externe [5].

**HYOK est un levier de révocation, pas une barrière pendant le traitement.** Dans le flux décrit, la clé de données en clair est remise au service qui chiffre l'objet [5]. Le service voit donc la donnée, comme le relève le chapitre 37. D'où l'intérêt de combiner clés détenues et TEE : la clé n'est libérée qu'à une charge attestée.

**HYOK n'est pas la portabilité.** Le chiffré ne se relit pas ailleurs.

**HYOK crée une dépendance de liaison.** Un agent dont la mémoire dépend d'un gestionnaire de clés injoignable s'arrête avec lui (46.5).

---

## 46.4 Continuité cognitive : perte du fournisseur de modèles

Trois pertes se distinguent.

| Perte | Préavis | Ce que montre la source lue |
|---|---|---|
| Retrait planifié d'un modèle | Annoncé | Anthropic s'engage à un préavis d'au moins 60 jours pour un modèle publié; passé la date, les requêtes échouent [6] |
| Changement de la surface d'API | Annoncé, par version | La version d'API `2026-10-21` supprime `temperature`, `top_p` et `top_k` : erreur 400. Les versions antérieures les refusent déjà sur Claude 4.7 et suivants, hors valeur par défaut [6] |
| Panne ou rupture : incident, litige, sanction | Aucun | Pas de source lue; hypothèse de planification |

La même page précise que les plateformes exploitées par des partenaires, Amazon Bedrock et l'offre gérée par Google Cloud, fixent leur propre calendrier de retrait [6]. Un même modèle n'a donc pas le même cycle de vie selon le canal d'achat. Comme un nouveau modèle peut refuser un paramètre, le secours se qualifie avec les appels réels.

### Deux horloges

Le NIST définit l'objectif de délai de reprise (RTO) comme la durée totale pendant laquelle les composants d'un système peuvent rester en phase de reprise avant que la mission de l'organisation en souffre [7]. « Reprise cognitive » n'est pas un terme normalisé : c'est l'application de ce délai à la fonction que remplit le modèle.

Rétablir un point d'accès ne rétablit pas un comportement. Un modèle de remplacement répond autrement aux mêmes prompts et aux mêmes outils. Changer de modèle, c'est changer le code d'exécutions en cours (chapitre 18), et le modèle est une unité de changement soumise à une barrière de rejeu (chapitre 34). La reprise a donc deux horloges : le temps de rerouter, à la passerelle (chapitres 24 et 44), et le temps de requalifier, par une suite d'évaluation (chapitre 33). La seconde n'est courte que si le travail est fait d'avance.

### Mesures proposées

- **Un modèle de secours qualifié d'avance**, par classe de tâche, chez un autre exploitant, et autohébergé pour les classes critiques. La qualification se refait à chaque changement de l'un des deux modèles.
- **L'état hors du fournisseur** : mémoire, journal d'exécution et traces. Une bascule ne perd alors que les caches (chapitre 13).
- **Un mode dégradé écrit** : autonomie réduite (chapitre 22), actions irréversibles suspendues, travail mis en file.
- **Un exercice de bascule périodique**, seul moyen de connaître le délai réel.

Le seuil demandé, « RTO inférieur à 15 minutes », n'a pas de source. Il n'est plausible que pour le reroutage vers un modèle déjà qualifié. C'est une cible de conception, à fixer par classe de tâche et à valider par exercice. Le volet contractuel de la sortie relève du chapitre 27.

---

## 46.5 Fonctionner déconnecté : périphérie et données répliquées sans conflit

Une usine, un navire, un véhicule ou un magasin perd sa liaison. Le site doit se dégrader, non s'arrêter. Quatre dépendances sont à couper d'avance :

- **le modèle**, par un modèle local plus petit, au besoin distillé (chapitres 28, 44 et 47);
- **les clés**, puisqu'un gestionnaire externe injoignable bloque le déchiffrement, hors clés en cache [5];
- **l'identité**, puisque les jetons expirent (chapitre 29);
- **les garde-fous et l'arrêt d'urgence**, qui doivent s'appliquer sur place : l'arrêt à la passerelle ou par révocation des jetons (chapitre 34) ne joint plus le site.

Le seuil demandé de « 72 heures » d'autonomie n'a pas de source. La durée de survie n'est pas une constante : elle se déduit du plus court de plusieurs délais, soit la validité des jetons et des certificats, la capacité du journal local et l'épuisement des quotas décrits ci-dessous. Elle se calcule par site et se vérifie par essai.

### Des invariants sans coordination

Pendant la coupure, le site et le centre modifient les mêmes données. Les types de données répliqués sans conflit (CRDT) font converger des modifications concurrentes sans coordination. Leur limite est connue : la cohérence à terme ne suffit pas à faire respecter un invariant numérique sur l'ensemble des répliques [8].

Le Bounded Counter de Balegas et de ses coauteurs lève cette limite [8]. L'écart entre la valeur d'un compteur et sa borne est traité comme un ensemble de droits d'exécution, répartis entre les répliques. Une opération consomme les droits locaux. S'ils manquent, elle échoue, ou la réplique en obtient d'une autre. Pendant une partition, les droits s'utilisent des deux côtés; seul leur transfert est impossible. Les auteurs rapportent, sur Riak, une latence nettement inférieure à celle d'une cohérence forte.

### Transposition proposée

Toute ressource bornée qu'un agent déconnecté peut consommer se répartit en droits avant la coupure : stock, budget de dépense, nombre d'actions d'une classe. Le site agit sans demander, dans sa part. Sa part épuisée, l'opération échoue sur place au lieu de violer l'invariant. En contrepartie, le centre ne récupère pas les droits d'un site silencieux.

L'autonomie déconnectée reçoit ainsi une borne indépendante du modèle : une limite écrite seulement dans un prompt n'est pas une limite (chapitre 22). À la reconnexion, le journal local se synchronise; les conflits qu'aucun type répliqué ne couvre se règlent par compensation (chapitre 18).

---

## 46.6 Robotique : ROS 2 et DDS

ROS 2 retient DDS et son protocole RTPS comme standards de communication [9]. L'article de conception de 2014 en donne les raisons : une découverte distribuée, sans le nœud maître de ROS 1; un modèle publication-abonnement; des réglages de qualité de service; une aptitude au temps réel embarqué. DDS y est un détail de mise en œuvre, masqué par l'API de ROS [9].

### La sécurité n'est pas activée par défaut

Aucune fonction de sécurité de DDS n'est active par défaut dans ROS 2 [10]. Une fois la sécurité activée par `ROS_SECURITY_ENABLE`, ROS 2 emploie trois modules de DDS-Security : l'authentification, par une paire de clés et un certificat X.509 signé par une autorité; le contrôle d'accès, par deux fichiers XML signés, l'un pour la gouvernance du domaine, l'autre pour les permissions du participant; le chiffrement authentifié AES-GCM. Une enclave regroupe ces fichiers.

La variable `ROS_SECURITY_STRATEGY` doit valoir `Enforce` pour qu'un processus refuse de démarrer sans ses fichiers. Toute autre valeur donne le mode permissif, qui démarre sans sécurité s'ils manquent [10].

### Conséquences pour un agent

Ce qui suit est une proposition, prolongée du chapitre 28.

- **L'adaptateur est un participant DDS.** Il reçoit sa propre enclave, limitée aux sujets nécessaires : lire la télémétrie, publier des objectifs, jamais des commandes d'actionneur.
- **Le mode `Enforce` est obligatoire** sur un robot joignable par un agent. Le mode par défaut échoue ouvert.
- **Deux sauts, deux sécurités.** L'autorisation de MCP (chapitre 5) ne protège pas le domaine DDS, ni l'inverse.
- **L'agent reste hors de la boucle de commande.** Il dépose un objectif; planification et commande restent dans des nœuds ROS 2.

---

## 46.7 Sûreté fonctionnelle : un contrôleur vérifié autour du contrôleur appris

### L'architecture Simplex

Lui Sha part d'un constat : certains composants, dont l'exactitude est impossible ou impraticable à vérifier, sont inévitables. Son principe, « employer la simplicité pour maîtriser la complexité » [15], garantit les propriétés critiques par un logiciel simple et une architecture appropriée [11].

Simplex applique ce principe à la commande. Un sous-système de haute performance, complexe et susceptible d'erreurs résiduelles, propose les commandes. Un sous-système de haute assurance, simple, garantit la sûreté. Une logique de décision examine la marge de stabilité qui résulterait de chaque commande : celle qui pourrait mener à l'instabilité est toujours rejetée, les autres reçoivent le bénéfice du doute. Il suffit donc de savoir si l'état résultant reste dans l'enveloppe, non si la commande est correcte [11].

Sha cite la commande de vol du Boeing 777 : le contrôleur normal doit rester dans l'enveloppe de stabilité d'un contrôleur secondaire fondé sur les lois de commande du Boeing 747 [11].

L'architecture ne vaut que si trois propriétés sont vérifiées [11] :

- **protection** : les fautes du composant complexe ne peuvent pas corrompre le composant simple ni la logique de décision;
- **ponctualité** : le composant simple s'exécute dans ses contraintes de temps;
- **tolérance aux fautes** : il fonctionne malgré toutes les fautes du modèle retenu.

### Trois étages

Transposée, l'architecture donne trois étages. L'agent fixe des objectifs. Le contrôleur appris, par exemple une politique neuronale de mouvement, tient la place du sous-système de haute performance. Le contrôleur vérifié et la logique de décision bornent ce qu'il peut faire. Ni l'agent ni le contrôleur appris ne peuvent modifier l'enveloppe. Le chapitre 28 concluait que la sûreté reste hors de portée de tout agent : Simplex indique où tracer cette frontière quand un composant appris entre dans la commande. Une logique de décision exécutée dans le même processus que la politique apprise manque à l'exigence de protection.

### Les normes

L'ISO 10218-1:2025, troisième édition, publiée en février 2025, remplace celle de 2011. Elle fixe les exigences de sécurité du robot industriel, traité comme une quasi-machine; l'intégration relève de l'ISO 10218-2 [12]. L'IEC 61508-1:2010, deuxième édition, couvre les systèmes électriques, électroniques et électroniques programmables qui exécutent des fonctions de sécurité. Elle sert à élaborer les normes sectorielles et s'applique en leur absence [13].

Rien n'établit ici que Simplex confère la conformité à l'un ou à l'autre : c'est un patron d'architecture, non une voie de certification.

---

## 46.8 Chaîne de mise à jour

Un robot ou un site en périphérie reçoit des poids, des adaptateurs (chapitre 47), des prompts, des catalogues d'outils, des politiques et du micrologiciel. Ce sont les unités de changement du chapitre 34, livrées à distance.

The Update Framework (TUF), en version 1.0.37, sécurise un système de mise à jour sans définir de format de paquet ni effectuer l'installation [14]. Quatre rôles se partagent la confiance.

| Rôle | Ce qu'il signe | Clé |
|---|---|---|
| `root` | Les clés des autres rôles | Hors ligne, très protégée |
| `targets` | Les métadonnées des fichiers cibles; peut déléguer | Hors ligne |
| `snapshot` | La liste des versions courantes des métadonnées | Hors ligne |
| `timestamp` | L'empreinte du `snapshot`, pour détecter le rejeu | En ligne; sa compromission pose un risque minimal |

Chaque rôle exige un seuil de signatures; compromettre moins de clés que le seuil ne doit pas compromettre les clients. La spécification énumère les attaques visées, dont le retour à une version antérieure, le gel indéfini, l'assemblage de métadonnées qui n'ont jamais coexisté et l'installation arbitraire. Une attaque parée doit échouer, même si le client reste incapable de se mettre à jour [14].

**Des délégations par nature d'artefact.** Celui qui signe un prompt n'est pas celui qui signe l'enveloppe de sûreté d'un robot. Délégations et seuils expriment cette séparation.

**Un retour arrière publié comme une nouvelle version.** Le client refuse toute métadonnée dont le numéro de version est inférieur à celui qu'il tient pour fiable [14]. Le retour arrière de version (chapitre 34) se livre donc comme une version neuve au contenu ancien.

**Une règle pour le site déconnecté.** Coupé du dépôt, un site ne distingue pas un gel d'une panne. Il poursuit sur la version vérifiée et n'installe rien. Des métadonnées expirées bloquent la mise à jour, non l'exécution [14] : elles ne bornent pas la durée de survie (46.5).

TUF vérifie ce qui est distribué; l'attestation vérifie ce qui s'exécute (46.2). Aucun des deux ne dit que le modèle se comporte bien (chapitre 33).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Inventaire des états | Un exploitant, une région et un détenteur de clé par état | Aucun cas |
| Inférence sur données réglementées | Modèle autohébergé ou fournisseur sous contrôle local (chapitre 37) | TEE avec GPU attesté si l'accès physique de l'exploitant est un risque accepté |
| Libération des clés | Sous attestation, selon une politique écrite par l'entreprise | Charge sans donnée sensible |
| Clés HYOK | Réservées aux classes de données qui l'exigent | Charges tolérantes à une perte de disponibilité |
| Modèle de secours | Qualifié d'avance, délai mesuré par exercice | Tâches différables : mise en file |
| Site déconnecté | Modèle, garde-fous et arrêt d'urgence locaux; durée de survie calculée | Site sans action physique ni transaction : arrêt acceptable |
| Ressources bornées hors ligne | Droits préalloués | Ressource non critique : réconciliation après coup |
| Accès d'un agent à ROS 2 | Enclave propre, mode `Enforce`, objectifs seulement | Simulation |
| Contrôleur appris | Enveloppe vérifiée, isolée, hors de portée de l'agent | Aucun cas en présence de personnes |
| Mises à jour | Métadonnées signées par rôles, clé racine hors ligne | Prototype isolé |

---

## Points à retenir

- Un agent garde plusieurs états chez plusieurs exploitants. Le géorepérage règle la résidence, pas le contrôle.
- Un TEE retire de la base de confiance les logiciels et les administrateurs de l'exploitant. Il n'en retire ni le fabricant de la puce ni celui qui tient physiquement le serveur.
- L'attestation est une preuve. La politique de libération des secrets reste à écrire, et elle revient à l'entreprise.
- HYOK donne la révocation, au prix de la disponibilité. Il ne protège pas la donnée pendant le traitement et ne rend pas le chiffré portable.
- La perte d'un modèle se prépare par un modèle de secours qualifié d'avance. Rerouter peut tenir en minutes; requalifier, non.
- Hors ligne, l'autonomie se borne par des droits alloués avant la coupure, non par un prompt.
- ROS 2 n'active aucune sécurité par défaut, et son mode permissif échoue ouvert.
- Simplex place la sûreté dans un composant simple et vérifié, isolé du composant appris. Ce n'est pas une certification.
- Les seuils de 15 minutes et de 72 heures n'ont pas de source : ce sont des cibles à mesurer.

---

## Sources

Pages primaires lues le 12 novembre 2026 :

1. [Intel — Trust Domain Extensions (TDX), vue d'ensemble](https://www.intel.com/content/www/us/en/developer/tools/trust-domain-extensions/overview.html)
2. [Google Cloud — Confidential VM overview](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)
3. [NVIDIA — Confidential Computing Overview](https://docs.nvidia.com/confidential-computing/overview)
4. [TEE.fail — page des auteurs de l'attaque](https://tee.fail/)
5. [AWS KMS — External key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html)
6. [Anthropic — Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
7. [NIST — glossaire, Recovery Time Objective](https://csrc.nist.gov/glossary/term/recovery_time_objective)
8. [Balegas et coll. — Extending Eventually Consistent Cloud Databases for Enforcing Numeric Invariants, arXiv 1503.09052](https://arxiv.org/abs/1503.09052)
9. [ROS 2 Design — ROS on DDS (W. Woodall, 2014, modifié en 2019)](https://design.ros2.org/articles/ros_on_dds.html)
10. [ROS 2 Design — ROS 2 DDS-Security integration (K. Fazzari, 2019, modifié en 2020)](https://design.ros2.org/articles/ros2_dds_security.html)
11. [Lui Sha — Integrate Mixed-Criticality Components with Formalized Architectural Patterns, 2008](https://www2.ee.washington.edu/research/nsl/aar-cps/LuiSha-20081015223039.pdf)
12. [ISO 10218-1:2025 — page de présentation](https://www.iso.org/standard/73933.html)
13. [IEC 61508-1:2010 — page de présentation](https://webstore.iec.ch/en/publication/5515)
14. [The Update Framework — spécification 1.0.37](https://theupdateframework.github.io/specification/latest/)

Source secondaire, non lue :

15. L. Sha, « Using Simplicity to Control Complexity », *IEEE Software*, juillet-août 2001 — citée d'après [11], sans lien vérifié.

## Limites de ce chapitre

- **Éléments demandés sans source.** « Six substrats d'état », « RTO < 15 min » et « 72 h » n'ont été retrouvés nulle part : la grille de 46.1 et les deux seuils sont des propositions.
- **CLOUD Act.** Le texte n'a pas été relu; le chapitre s'en remet au chapitre 37. Aucune source lue ne dit ce qu'un tribunal peut exiger d'un exploitant de TEE.
- **AMD et HYOK.** La documentation d'AMD n'a pas pu être chargée : SEV-SNP est décrit d'après Google Cloud [2] et TEE.fail [4]. Les équivalents HYOK d'Azure et de Google n'ont pas été lus.
- **NVIDIA et TEE.fail.** Seule la vue d'ensemble de NVIDIA a été lue : ni matrice de compatibilité, ni mécanique du lien entre processeur et GPU, ni mesure de surcoût. TEE.fail est décrite d'après la page de ses auteurs; l'article et les avis d'Intel et d'AMD n'ont pas été lus.
- **Relecture d'audit.** L'audit a relu [2] à [6] et [14], par un outil qui en restitue le contenu : chiffres, versions et citations confirmés, sauf « analyseur logique exclu », que [4] ne dit pas. [12] a refusé l'accès; édition et date sont confirmées par des résultats de recherche.
- **ROS 2.** La documentation courante était inaccessible. [9] et [10] sont des articles de conception de 2014 et de 2019; l'état des distributions actuelles n'est pas vérifié.
- **Normes.** ISO 10218 et IEC 61508, payantes, ne sont connues que par leur page de présentation. Niveaux d'intégrité, exigences logicielles et apprentissage automatique ne sont pas abordés.
- **Connaissance générale** : la définition des CRDT, l'inclusion du système invité dans la base de confiance, l'écart de comportement entre deux modèles.
- **Propositions de ce chapitre**, non éprouvées : les mesures de 46.4, le calcul de la durée de survie et la transposition du Bounded Counter, les conséquences de 46.6, les trois étages de 46.7, les applications de TUF.
- **Pannes de fournisseurs.** Aucun rapport d'incident n'a été lu, seulement la politique de retrait d'un fournisseur [6].
- **Renvois** vérifiés à l'audit. L'arrêt d'urgence local (46.5) est une proposition qui prolonge le chapitre 34.
