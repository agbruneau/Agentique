# Relecture CA-09 — test d'appartenance, Parties VII et VIII

| Champ | Valeur |
|---|---|
| Objet | **CA-09 Périmètre** (PRD **§11**, exigences de qualité et critères d'acceptation) — vérification du **test d'appartenance** du PRD §5.1, **section par section**, sur les Parties VII et VIII |
| Périmètre | **Cinq pièces, vingt sections de niveau 2** : `monographie/07-partie-VII/` — ch. 22 (4 sections), ch. 23 (4) — et `monographie/08-partie-VIII/` — ch. 24 (4), ch. 25 (5), ch. 26 (3). Les cinq pièces ont été **ouvertes intégralement**, corps et Notes |
| Date d'exécution | **22 juillet 2026** |
| Relecteur | Distinct du rédacteur des cinq pièces (CA-14) |
| Résultat | **20 sections examinées, 20 passent** au grain de la section. **Deux développements coupés** au grain du *développement*, mot que le PRD §5.1 emploie : **499 mots retirés**, remplacés par **271 mots** de déclaration de coupe |
| Documents d'autorité consultés | PRD §5.1 (test), §11 (CA-09), §8.6 (degrés d'absence), Annexe A §A.6 (motifs), Annexe C §C.1 et §C.2 (grille) ; PRDPlan §1.5 (commande de décompte), §5.1, §5.3, §5.5, §6 |
| ⚠ Ce que ce rapport n'est pas | **Il ne vaut pas attestation de conformité des pièces.** Il rend compte d'un contrôle de **périmètre**, et d'aucun autre. **CA-12 (R-12, dualité d'usage) demeure due sur les cinq pièces** : un contrôle qui lit ce qu'une section prétend établir ne lit pas ce qu'un passage rendrait exécutable. Aucun décompte de ce rapport ne tient lieu du rejeu §A.6 ordonnancé en P5.2 |

---

## 1. La règle appliquée, et à quel grain

Le PRD §5.1 pose le test en ces termes : un développement de Partie VII ou VIII n'entre dans l'ouvrage que s'il répond à l'une de ces deux questions — *que vérifie-t-il de l'identité ou du mandat d'un agent ?* ou *que produit-il comme preuve opposable sur cette identité ou ce mandat ?* — et « un développement qui ne répond ni à l'une ni à l'autre est **hors périmètre**, quelle que soit sa qualité ». CA-09 en fait un contrôle **section par section**, et impose que toute section qui échoue soit **coupée**, sa coupe **consignée**.

**Deux grains ont donc été appliqués, et l'écart entre eux est le résultat principal de cette passe.**

- **Au grain de la section** — celui que CA-09 nomme —, les vingt sections répondent, et aucune n'est coupée.
- **Au grain du développement** — mot que le PRD §5.1 emploie lui-même, et grain auquel les rédacteurs de deux pièces avaient déjà coupé (routage sémantique et IBM ContextForge au ch. 22 ; statut scindé d'un traçage d'agents au ch. 24) —, **deux développements internes à des sections qui passent ne répondent à aucune des deux questions**. Ils sont coupés.

⚠ **Ce constat est opposable au-delà de cette passe : une section qui passe n'immunise pas ses développements.** Le contrôle prescrit par CA-09 s'arrête à la section ; c'est le grain auquel la dilution ne se voit pas. Les deux coupes opérées ici vivaient toutes deux dans des sections que le test fait passer sans réserve.

**Trois conséquences concrètes du PRD §5.1 ont été traitées comme opposables**, le texte les énonçant « pour n'avoir pas à les rediscuter chapitre par chapitre » : la latence, le coût et la topologie n'entrent qu'au titre des conditions de renversement (ch. 23 §23.4) ; l'observabilité entre par la corrélation trace ↔ chaîne de mandat protocolaire (ch. 24 §24.4) ; l'évaluation entre par la revalidation du passeport après apprentissage (ch. 25 §25.5). Le FinOps agentique, le routage sémantique pour lui-même et le comparatif de cadriciels d'agents sont hors périmètre.

**Principe de discrimination retenu, et il est écrit ici pour être réfutable.** Un développement passe si ce qu'il borne est **la vérification de l'identité ou du mandat protocolaire d'un agent** — y compris par une réponse négative, une case vide ou une lacune déclarée. Il échoue si ce qu'il borne est **la maturité, le stade commercial ou l'ingénierie d'un produit ou d'une couche pour eux-mêmes**. *Une réponse négative est une réponse ; un état de produit n'en est pas une.*

---

## 2. Relevé section par section — les vingt verdicts

Chaque ligne porte la **phrase de la section** qui fonde le verdict. Les phrases sont citées de la pièce, non résumées.

### 2.1 Chapitre 22 — Du *service mesh* à l'*agent mesh*

| Section | Q1 — ce qu'elle vérifie de l'identité ou du mandat protocolaire | Q2 — la preuve opposable | Verdict |
|---|---|---|---|
| **22.1** | La spécification SPIFFE-ID « définit l'identité SPIFFE comme un URI conforme au RFC 3986 […] et le SVID comme le mécanisme par lequel une charge de travail *communique* son identité » ; « ce que cette spécification démontre est une vérification de signature dans un domaine de confiance » (**F-87, [B]**) | rien en propre — la section établit le substrat hérité, non une preuve produite ici | **PASSE (Q1)** |
| **22.2** | « La documentation d'agentgateway spécifie une politique d'autorisation propre à MCP […] évaluée contre des invocations de méthodes et exposant des champs d'outil, d'invite et de ressource » (**F-71, [B]**) ; A2A « déclare explicitement qu'aucune API normalisée n'est prescrite pour les registres organisés » (**F-43, [B, degré 2]**) | une décision d'autorisation **documentaire**, bornée par un statut pré-version | **PASSE (Q1)** — ⚠ **une coupe interne**, §4.1 |
| **22.3** | « Le ch. 12 §12.2 range chaque attaque selon **le maillon de la chaîne d'identité ou de mandat protocolaire qui cède** » ; un référentiel daté « **énonce** la vérification continue comme la propriété distinctive de l'identité d'agent » (**F-20, [A]**) | aucune — la section le déclare : « le §22.4 seul en rend le verdict opposable » | **PASSE (Q1)** — voir §3.1 |
| **22.4** | les cinq verdicts de la grille du ch. 4, dont « **ne répond pas** » à Q-A et « **répond partiellement** » à Q-D | le tableau daté, avec trois cases vides portant leur **degré 3** | **PASSE (Q1 et Q2)** |

### 2.2 Chapitre 23 — Le maillage comme point d'application

| Section | Q1 | Q2 | Verdict |
|---|---|---|---|
| **23.1** | « une politique d'accès conditionnel ciblant des identités d'agent **ne s'applique pas** au compte d'utilisateur de l'agent, et une politique ciblant "tous les utilisateurs" **n'inclut pas** les identités d'agent » (**F-35, [A, degré 2]**) | l'écart de couverture **déclaré par l'éditeur dans sa propre documentation** — fait négatif **ÉTABLI** | **PASSE (Q1 et Q2)** |
| **23.2** | « l'authentification et l'autorisation — du sujet comme de l'appareil — sont des **fonctions discrètes exécutées avant l'établissement d'une session** » (**F-73, [B]**) ; « les cartes **MAY** être signées, les clients **SHOULD** vérifier au moins une signature avant d'accorder confiance » (**F-04, [A]**) | rien que le socle documente — la section produit un principe d'architecture, et l'écrit | **PASSE (Q1)** |
| **23.3** | « rien dans le relevé n'expose le mandant d'origine ni la portée qu'il a consentie » ; le mécanisme de propagation borne sa portée « … throughout the Call Chain **within a trusted domain** … » | « un dispositif que toute interaction traverse est **structurellement** un producteur de trace non délégué à l'observé » — propriété d'emplacement, marquée « Lecture de l'auteur » | **PASSE (Q1 et Q2)** |
| **23.4** | les cinq conditions de renversement, dont « **il n'y a pas de chaîne à vérifier** » et « la couverture n'est pas totale, et le complément est inconnu » | la **falsifiabilité** de la thèse, chaque condition portant ce qui la rendrait constatable | **PASSE (Q1)** — ⚠ admise **nommément** par le PRD §5.1 ; réserve au §5.2 |

### 2.3 Chapitre 24 — L'observabilité agentique

| Section | Q1 | Q2 | Verdict |
|---|---|---|---|
| **24.1** | « Savoir qu'un appel a duré trois secondes ne dit ni qui l'a émis, ni pour le compte de qui, ni sous quelle borne de privilège — c'est-à-dire ni **Q-A** […] ni **Q-C** […] ni **Q-D** » | aucune — et la section le dit en cartographiant l'écart sur la grille du ch. 4 | **PASSE (Q1)**, par réponse négative |
| **24.2** | « les quatre attributs d'agent, les deux de conversation, les sept d'outil et les quatre d'évaluation relevés par le lot portent tous `stability: development` » (**F-77, [B]**) ; l'échelle compte **cinq** échelons (**F-76, [B]**) | « **aucun numéro de version qui lui soit propre n'est citable** » (**F-75, [B], degré 2**) — ce qui borne la valeur probante de tout attribut d'identité porté par une trace | **PASSE (Q1)** — ⚠ **passage le plus disputé de la passe**, §5.1 |
| **24.3** | ce que la ligne directrice E-23 **attend** — « autonomous decision making, autonomous re-parametrization » (**H-04**, **F-65, [B]**) — et ce que l'art. 12.1 **impose** de restituer (**F-89, [B]**) | « une trace ne devient une pièce que si son producteur est distinct de l'objet qu'elle décrit, et si elle rattache l'événement consigné à une identité et à un mandat protocolaire que quelqu'un d'autre a émis » | **PASSE (Q1 et Q2)** |
| **24.4** | « **Aucune entrée n'établit que cet identifiant soit celui d'un registre d'agents au sens du ch. 7, ni qu'il soit émis, ni qu'il soit vérifiable** » | la **lacune 21** déclarée au cas 2 — l'absence de clé de jointure, exposée et non comblée | **PASSE (Q1 et Q2)** — section nommée par le PRD §5.1 comme point d'entrée |

### 2.4 Chapitre 25 — Le cycle de vie opérationnel

| Section | Q1 | Q2 | Verdict |
|---|---|---|---|
| **25.1** | « une évaluation conduite en production est ce qui **daterait un verdict que le mécanisme d'admission ne date pas** » (**F-03**, **F-05, [A, degré 1]**) | un résultat d'évaluation consignable dans un format nommé, dont l'écart au sujet est le résultat (**F-97**, **F-98, [B]**) | **PASSE (Q1 et Q2)** |
| **25.2** | « le comportement d'un agent change **sans qu'aucun de ses artefacts d'identité ne change** » ; le type décrivant un outil ne porte « ni version, ni empreinte cryptographique, ni signature » (**F-52, [B, degré 1]**) | le constat que la dérive que les cadres nomment n'est pas instrumentée par le seul relevé versé au socle (**H-12, [B]**) | **PASSE (Q1)** |
| **25.3** | « Expired or revoked keys **MUST NOT** be used for verification » posé « sans aucun mécanisme permettant au client d'établir l'expiration ou la révocation » (**F-07, [A]**, **F-06, [A, degré 1]**) | une révocation de masse datée et son périmètre (**F-21, [A]**) ; un écart de couverture déclaré (**F-35**) | **PASSE (Q1 et Q2)** — ⚠ **une coupe interne**, §4.2 |
| **25.4** | « **quel mandat protocolaire et quelles bornes de privilège étaient en vigueur au moment d'une action donnée** » | « c'est une question de **preuve opposable** avant d'être une question d'outillage : sans elle, un dossier de diligence raisonnable porte un état courant et jamais un état daté » | **PASSE (Q1 et Q2)** — arbitrage demandé par la pièce, §3.2 |
| **25.5** | « si un agent modifie son propre comportement, que devient la vérification dont il a fait l'objet ? » — l'adaptation éphémère et l'évolution persistante distinguées (**H-11, [B]**) | l'absence de mécanisme de revalidation, écrite au **degré 3** ; le passeport « n'assemble que des pièces datées à leur émission » | **PASSE (Q1 et Q2)** — section nommée par le PRD §5.1 comme point d'entrée |

### 2.5 Chapitre 26 — Les indicateurs de l'AgentOps

| Section | Q1 | Q2 | Verdict |
|---|---|---|---|
| **26.1** | « la seule référence d'agent est `gen_ai.agent.name`, "Human-readable name of the GenAI agent provided by the application" » — donc « **les métriques relevées agrègent par nom lisible, non par identifiant stable** » (**F-92, [B, degré 1]**, ⚖ vote dû) | aucune, et c'est le résultat : « une clé d'agrégation qui peut légitimement manquer n'est pas un dénominateur » (**F-94, [B]**) | **PASSE (Q1)**, par réponse négative — réserve au §5.3 |
| **26.2** | chacune des quatre grandeurs est définie par ce qu'elle vérifierait de l'identité ou du mandat protocolaire — « part des actions tracées **et** rattachées à une identité émise et à un mandat protocolaire » | la colonne de droite énonce, grandeur par grandeur, ce qui manque pour qu'un indicateur se calcule — dénominateur, clé de jointure, bornes de mesure, horodatage exportable | **PASSE (Q1 et Q2)** |
| **26.3** | « les deux compteurs d'appels comptent les appels **directs** de l'agent, les appels de sous-agents […] étant **attribués séparément** » — donc « une chaîne de délégation n'est **pas reconstituable par sommation** » (**F-96, [B, degré 1]**, ⚖ vote dû) | la **lacune 7** déclarée au cas 2 : une grandeur d'horizon serait la preuve de la portée d'un mandat protocolaire, et le corpus ouvert documente l'obstacle | **PASSE (Q1 et Q2)** |

---

## 3. Les deux sections que les pièces désignaient elles-mêmes comme à trancher

Deux rédacteurs ont demandé l'arbitrage plutôt que de l'anticiper. Les deux verdicts sont rendus ici, avec leur motif.

### 3.1 Ch. 22 §22.3 — **PASSE**, et il faut dire par quoi

La pièce écrivait : « **Si le contrôle CA-09 juge que la prémisse ne répond littéralement ni à l'une ni à l'autre des deux questions de PRD §5.1, la section est coupée et sa coupe consignée** », et rangeait ce point en tête de ce que le contrôle devrait trancher.

**La section passe, sur la première question.** Elle ne passe **pas** par la thèse de non-compositionnalité de la sûreté, qui est une entrée **[C]** attribuée à un volume antérieur (**H-24** ; `Monographie.md` §3.10.1 pour le verbatim, siège déclaré en `Synthese Monographie.md` §5.10) et que **CA-01 interdit de faire porter une affirmation centrale**. Elle passe par son **troisième paragraphe**, qui établit ce qui doit être vérifié : le maillon de la chaîne d'identité ou de mandat protocolaire qui cède (ch. 12 §12.2), la vérification continue **énoncée** comme propriété distinctive de l'identité d'agent par un référentiel daté (**F-20, [A]**, *State of Agentic AI Security and Governance* v2.01, juin 2026, OWASP Gen AI Security Project), et l'endroit où chaque mécanisme perd le fil de la délégation (ch. 10 §10.1).

⚠ **La borne est portée ici parce qu'elle est fragile** : privée de ce paragraphe, la section ne répondrait plus à aucune des deux questions, et la coupe se rouvrirait. Une reprise ultérieure qui l'allégerait doit le savoir.

### 3.2 Ch. 25 §25.4 — **PASSE**, et la minceur n'est pas le critère

La remontée (d) de la pièce demandait d'arbitrer la place de la section, « la réponse [qu'elle] apporte [étant] réelle mais […] **la plus mince des cinq** », et concédait que le contrôle « pourrait légitimement la réduire ou la couper ».

**La section passe, et sur les deux questions.** Elle demande « quel mandat protocolaire et quelles bornes de privilège étaient en vigueur au moment d'une action donnée » (première question) et pose elle-même que « c'est une question de preuve opposable avant d'être une question d'outillage » (seconde). Elle déclare en outre au **degré 3** l'absence de définition de « GitOps » appliqué à un parc d'agents et n'en développe aucun outillage.

⚠ **Couper sur la minceur du socle plutôt que sur la question aurait été la faute symétrique de la dilution.** Le socle y est mince ; la réponse ne l'est pas. *Le critère est la question.*

---

## 4. Les deux coupes opérées

### 4.1 Ch. 22 §22.2 — le développement du **transport** (SLIM, `L13-A5`)

| | |
|---|---|
| Ce qui est coupé | Le paragraphe « **Le transport : une pièce nommée par le découpage, et non versée au socle** » — description de `draft-mpsb-agntcy-slim-02` comme couche de transport pour A2A et MCP, combinant gRPC sur HTTP/2 et HTTP/3 avec un chiffrement de bout en bout par MLS, son expiration au 8 janvier 2027, sa qualification pré-normative, et la reprise de **H-10** rangeant AGNTCY parmi les couches d'infrastructure |
| Volumétrie | **227 mots**, mesurés par la commande de PRDPlan §1.5. Remplacés par **164 mots** de déclaration de coupe |
| Motif | Une couche de messagerie et son chiffrement **ne disent rien de ce qui est vérifié de l'identité ou du mandat protocolaire d'un agent** et **n'en produisent aucune preuve opposable**. Transporter un protocole qui véhicule une identité n'est pas vérifier une identité |
| Ce qui rend la coupe nette | La pièce l'écrivait elle-même : « **aucun énoncé central du volume ne s'y adosse** ». C'est le motif exact — mot pour mot — de la coupe d'IBM ContextForge opérée par la seconde relecture adversariale de la même pièce. *Deux relevés au même profil, un coupé et l'autre non, n'est pas un arbitrage : c'est une inconséquence* |
| L'objection écartée | « Le découpage le nomme au titre de l'anatomie. » Le §22.2 refuse déjà cette objection pour le routage sémantique, dans la même section : **le découpage nomme, il n'admet pas** |
| Matière conservée ailleurs | **Non.** `L13-A5` n'est versée à aucune entrée du socle ; elle demeure au rapport [`lot-L-13-maillage.md`](lot-L-13-maillage.md), où le contrôle ne touche à rien. **La demande de versement portée en remontée (1) de la pièce est retirée**, au motif déjà appliqué à ContextForge |
| Effets de bord traités | **H-33** retirée de l'en-tête et du bloc « Entrées mobilisées » — sa seule mobilisation au corps était le tri de cette expiration ; **la pièce ne porte plus aucun énoncé sur le futur, donc plus aucun tri prospectif** (CA-11 re-mesuré : **zéro capture de tri**, contre une). Marqueurs de niveau re-mesurés : **17** contre 19 (**3 [A], 8 [B], 6 [C]**). Mentions relevant de R-09 : **trois** par lecture, contre quatre. R-14 avec `-i` : **42**, inchangé. CA-03 : **13**, inchangé |

⚠ **La coupe défait un correctif de la relecture adversariale du 22 juillet 2026** — son point (4) avait ajouté le tri **PROGRAMMÉE au sens mécanique** sur cette expiration. Le correctif était juste ; il portait sur un développement que le périmètre n'admet pas. *Corriger une faute dans un passage hors périmètre reste une correction ; elle ne rend pas le passage admissible.*

### 4.2 Ch. 25 §25.3 — le **stade commercial des outils de triage** (F-58)

| | |
|---|---|
| Ce qui est coupé | Le développement « **L'outillage de cette fonction est par ailleurs daté et inégal : trois éditeurs, trois stades** » — préversion et disponibilité générale partielle chez le premier, disponibilité générale chez le deuxième, annonce sans date chez le troisième —, ses deux qualifications de degré et sa clause d'attribution |
| Volumétrie | **272 mots**. Remplacés par **107 mots** de déclaration de coupe |
| Motif | Un tri par éditeur de dates de disponibilité et de préversion **ne dit rien de ce qui est vérifié de l'identité ou du mandat protocolaire d'un agent** et **n'en produit aucune preuve opposable**. C'est le motif que le ch. 24 §24.2 a lui-même retenu pour couper le statut scindé d'un traçage d'agents (`L14-A9`) |
| Ce qui n'est **pas** coupé | La phrase qui précède — « **et les répondants sont eux-mêmes des agents** » — et les **deux modèles d'identité** du *Microsoft Security Copilot Phishing Triage Agent*, dont l'un est déclaré incompatible avec Privileged Identity Management et le laissez-passer d'accès temporaire (**F-57, [A]**). Ce développement-là répond à la première question, et il reste entier |
| Matière conservée ailleurs | **Oui, et intégralement.** Le siège de F-58 est le **ch. 15 §15.1**, en Partie V — **hors du champ de CA-09** —, où l'entrée est mobilisée avec ses trois bornes : attribution nominative à chaque éditeur, refus explicite de qualifier au degré 1 le constat portant sur le troisième, interdiction d'en déduire un énoncé sur « le marché ». *Ce qui a été coupé n'est pas le fait, c'est sa reprise dans une partie où il ne répond à aucune des deux questions* |
| Effets de bord traités | **F-58** retirée de l'en-tête et du bloc « Entrées mobilisées » ; les trois sources hors socle `L10-A6`, `L10-A8`, `L10-A9` sorties avec elle (**trois** hors socle au lieu de six) ; **demande de versement (g) retirée pour cette pièce et maintenue pour le ch. 15** ; composition « ch. 15 §15.1 » retirée de l'inventaire ; coupe (b) du relevé de coupes corrigée, elle retenait encore « le statut daté des offres » ; remontée (j) maintenue avec son motif |
| Décomptes de balayage re-mesurés | R-14 avec `-i` : **51** contre 52. CA-03 : **17** contre 20 — et **35** contre 40 en relevé réel, formes fléchies comprises. CA-11 : **58** contre 59, la trentième occurrence de [B] étant celle de F-58 |

---

## 5. Ce que le contrôle a examiné **sans** couper — et les arguments contraires, écrits

Un contrôle qui ne consigne que ses coupes ne se laisse pas réfuter. Les trois cas ci-dessous ont été retenus **contre** un argument sérieux, reproduit ici pour que l'auteur puisse renverser le verdict.

### 5.1 Ch. 24 §24.2 — la conformité annoncée d'un éditeur (**F-78**) : **maintenue**, et c'est la décision la plus étroite de la passe

**L'argument pour couper.** Le paragraphe établit qu'une documentation produit de **Datadog** « énonce sa conformité par référence à un millésime du **dépôt principal** publié le 25 août 2025, antérieur au déplacement du 12 juin 2026 ». Pris littéralement : il ne vérifie rien de l'identité ni du mandat protocolaire d'un agent, et n'en produit aucune preuve opposable. **La même pièce a coupé le cas Microsoft Foundry avec exactement cette phrase.** La symétrie est réelle, et une passe qui coupe l'un sans couper l'autre doit s'en expliquer.

**Le motif du maintien.** Les deux cas ne bornent pas le même objet. Le cas coupé bornait **le stade commercial d'un produit** — quelles catégories d'agents sont tracées à quel statut. Le cas maintenu borne **la citabilité de la version de l'instrument** : il établit que la formule « conforme aux conventions OpenTelemetry » ne désigne aucun état déterminé, et c'est l'objet même de la section, laquelle existe pour dire qu'« il n'y a pas de version à citer ». Or l'instrument en question est celui qui porte les quatre attributs d'agent dont le §24.4 fait sa clé de jointure manquante. **Retirer ce paragraphe laisserait le lecteur croire qu'une conformité annoncée fixe le millésime des attributs d'identité qu'il consommera.**

⚠ **La décision est déclarée étroite, et son coût est nommé** : F-78 n'est mobilisée qu'ici dans tout le volume ; la couper ferait d'une entrée versée une entrée orpheline. **Ce coût n'a pas fondé le maintien** — une entrée orpheline est un problème de socle, non un motif d'appartenance —, mais il est consigné pour que l'arbitrage de l'auteur en dispose. **Point porté aux remontées.**

### 5.2 Ch. 23 §23.4 — l'encadré de lacune sur le **coût d'exploitation** : **maintenu**, sa formulation remontée

Le PRD §5.1 admet cette section **nommément**, et n'y fait entrer latence, coût et topologie qu'« au titre des conditions qui renverseraient » ce que le chapitre avance. Le corps s'y tient : il déclare au **degré 3** l'absence de toute mesure et n'en infère rien.

⚠ **La question écrite dans l'encadré de lacune, elle, est formulée en question d'ingénierie** : « quelles latences, quels coûts et quelle disponibilité un maillage d'agents introduit-il entre deux agents qui, sans lui, communiqueraient directement ? » — sans rattachement à la condition qu'elle sert. **L'encadré n'est pas coupé** : la troisième condition du tableau (« le point d'application unique devient le point de défaillance ») a besoin d'une mesure de disponibilité pour être constatable, et la lacune est ce qui la rend falsifiable. **La reformulation de la question — l'ancrer explicitement à la condition 3 — est remontée, non opérée** (PRDPlan §5.3).

### 5.3 Ch. 26 §26.1 — le paragraphe des **deux catalogues d'éditeurs** : **maintenu par son résultat, non par son inventaire**

Le paragraphe nomme onze évaluateurs chez un éditeur, dont cinq en préversion déclarée, et quatre mesures chez un autre. Pris comme inventaire, il tomberait sous la coupe (c) que la pièce déclare elle-même — « le panorama des plateformes ». Il passe par ce qu'il établit : « **aucun identifiant n'est commun aux trois** » (**F-98, [B]**), c'est-à-dire qu'aucune clé d'identité ne traverse les instruments ouverts par ce volume, et que « ce que le corpus ouvert offre de plus proche d'un indicateur de mandat protocolaire » mesure une **capacité** et non une conformité.

⚠ **La borne est fragile de la même manière qu'au §22.3** : le jour où l'inventaire survivrait à son résultat, il deviendrait le panorama que la pièce range hors périmètre.

---

## 6. Ce que le contrôle **n'a pas pu trancher**

Ces points excèdent le mandat d'un contrôle de périmètre. Ils sont **relevés, non opérés** (PRDPlan §5.3), et aucun n'a été corrigé dans les pièces.

1. **Le grain de CA-09 lui-même.** Le critère prescrit un contrôle « section par section » ; le PRD §5.1 parle de « développement ». **Les deux coupes de cette passe vivaient dans des sections qui passent** — au grain prescrit, aucune n'aurait été trouvée. Décider si CA-09 doit désormais nommer le grain du développement relève du cadrage, et la question se reposera à l'identique sur les Parties IX et sur l'appareil.

2. **F-78 deviendrait orpheline si le §24.2 était réduit** (voir §5.1). L'arbitrage — maintenir le paragraphe, ou couper et accepter une entrée de socle qu'aucune pièce ne mobilise — appartient à l'auteur.

3. **Redondance entre le ch. 25 §25.1 et le ch. 26 §26.1**, non traitée parce qu'elle n'est pas un défaut de périmètre. Les deux sections développent **F-97** et **F-98** dans des termes très proches — onze évaluateurs, cinq en préversion, « Prohibited Actions » mesurant une capacité, aucun identifiant commun entre trois sources —, alors que le ch. 24 pose que « toute la matière des seize métriques relevées par le lot complémentaire L-14b relève du ch. 26 §26.1 ». **Les deux passent le test** ; savoir si l'une doit renvoyer à l'autre plutôt que redévelopper est une décision de découpage.

4. **Reformulation de la question de l'encadré de lacune du ch. 23 §23.4** (voir §5.2).

5. **Les énumérations de capacités produit du ch. 24 §24.3**, à l'intérieur du paragraphe portant R-07 du présent volume — « Evaluation Studio, Risk Atlas agentique, inventaire par défaut » d'une part, « découverte automatique des agents, des modèles et des dépendances, évaluations *LLM-as-a-judge*, visibilité par tâche » d'autre part. **Le paragraphe passe** : sa fonction est de poser que le rapprochement entre un outil d'observabilité et une attente réglementaire est une **inférence d'auteur**, et de distinguer deux régimes d'absence — **degré 2** pour l'un, **degré 3** pour l'autre. ⚠ **Les listes de fonctions, elles, n'y sont pas nécessaires** : elles nomment les produits au-delà de ce que le garde-fou exige. Réduire une énumération à l'intérieur d'une phrase excède le grain d'un contrôle de périmètre ; le point est signalé.

6. **Les demandes de versement retirées ne préjugent pas de l'instruction.** Le retrait de la demande sur `L13-A5` signifie que **les Parties VII et VIII** n'en ont pas l'usage, non que le transport ne mérite pas d'être instruit. Si un autre siège le veut, l'arbitrage revient à l'auteur.

7. **Deux entrées demeurent sous dette de vote** (**F-92** et **F-96**, PRD §7.11 et §A.4) et portent le marqueur ⚖ à chacune de leurs mobilisations. Le contrôle de périmètre ne l'instruit pas ; il constate que le ch. 26 §26.1 et §26.3 passent **sans que l'une ou l'autre porte seule un énoncé**, ce qui est la parade que la pièce déclare.

---

## 7. Volumétrie re-mesurée après coupe

Mesures par la **seule commande de référence** du volume (PRDPlan §1.5, `LC_ALL=C.UTF-8`), exécutées sur le corps des cinq pièces après application de toutes les modifications. **Les cinq en-têtes ont été alignés sur ces valeurs.**

| Pièce | Avant | Après | Écart | Cible | Écart à la cible |
|---|---|---|---|---|---|
| ch. 22 | 5 539 | **5 476** | **−63** | ~3 500 | +56,5 % |
| ch. 23 | 6 035 | **6 047** | +12 | ~3 500 | +72,8 % |
| ch. 24 | 5 367 | **5 367** | 0 | ~3 400 | +57,8 % |
| ch. 25 | 6 586 | **6 427** | **−159** | ~3 300 | +94,8 % |
| ch. 26 | 5 073 | **5 073** | 0 | ~3 300 | +53,7 % |
| **Total** | **28 600** | **28 390** | **−210** | **17 000** | **+67,0 %** |

**Les deux hausses sont des corrections d'attestation, non des ajouts de matière** : les ch. 23 et 25 annonçaient dans leur corps une relecture CA-09 « qui reste due », énoncé devenu faux le jour où elle a eu lieu. Coût : 12 et 6 mots.

⚠ **Le bilan des deux coupes se lit ainsi : 499 mots retirés, 271 mots de déclaration de coupe écrits à leur place.** *Consigner une coupe coûte les deux tiers de ce qu'elle retire.* C'est le prix de sa traçabilité, et il explique pourquoi une passe de périmètre ne réduit pas une volumétrie autant qu'on l'attendrait — ce que le rédacteur du ch. 22 avait anticipé en écrivant que la relecture allonge une pièce plutôt qu'elle ne la raccourcit.

⚠ **L'écart à la cible n'est pas corrigé par cette passe et ne doit pas l'être** : il vient des bornes portées (arbitrage **R-G-39**), et les 499 mots retirés ici le sont pour **périmètre**, non pour volume. *Amputer une borne et couper un hors-périmètre sont deux gestes opposés qui produisent le même chiffre.*

---

## 8. Ce que ce contrôle ne dit pas

- **Il ne certifie aucune pièce.** Il constate qu'au 22 juillet 2026, vingt sections répondent à l'une au moins des deux questions du PRD §5.1, et que deux développements n'y répondaient pas.
- **Il ne supplée pas CA-12**, due sur les cinq pièces : un contrôle de périmètre lit ce qu'une section prétend établir ; il ne lit pas ce qu'un passage rendrait exécutable. **R-12 du présent volume n'a pas de motif de balayage** et n'est contrôlable par aucun décompte.
- **Il ne rejoue pas les bilans §A.6.** Les décomptes re-mesurés au §4 portent sur les seuls motifs que les coupes ont déplacés, sur les seules pièces coupées. Le rejeu exhaustif des trente-quatre pièces demeure ordonnancé en **P5.2**.
- **Il n'arbitre aucune remontée**, n'ouvre ni ne clôt aucune lacune, ne verse aucune entrée au socle, et ne modifie aucun document de gouvernance.
- ⚠ **Il ne vaut que pour l'état des pièces à cette date.** Toute reprise ultérieure des deux paragraphes signalés comme fragiles — ch. 22 §22.3 troisième paragraphe, ch. 26 §26.1 résultat des deux catalogues — rouvre la coupe que ce contrôle a écartée.
