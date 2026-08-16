## Chapitre 1 — Le socle protocolaire

*Matière : compendium, Livre I, ch. 1, 2, 8, 9, 10 ; `4 - Veille/Veille Technologique.md` ;
`4 - Veille/Revue de littérature.md` ; les deux `README.md` pour les régimes et les gels.*

---

### 1.1 — Ce que ce chapitre tient, de qui, et à quel prix

Trois livrables portent la matière protocolaire, à trois dates et sous trois régimes. Le tableau
ci-dessous conditionne tout ce qui suit : aucun énoncé de ce chapitre ne peut valoir mieux que la
ligne dont il descend.

| Livrable | Gel | Régime hérité | Ce qu'il dit de lui-même |
|---|---|---|---|
| Compendium, Livre I (ch. 1, 2, 8, 9, 10) | gel unique du 27 juillet 2026 ; sources gelées juin 2026 (Vol. I) et 16 juillet 2026 (Vol. II) | **[C]** pour ce qui descend du Vol. I — PRD §7.1 du compendium : la vérification y porte sur les *références*, non sur le contenu des affirmations | « **brouillon de rédaction, non publiable** » ; « aucun énoncé n'est central au sens de **CA-IV-01** » |
| Veille technologique | 15 août 2026 | source primaire rouverte par le rédacteur, **sans ronde adverse à plusieurs votants** pour les éditions d'août (veille, § 2.2, § 10) | métriques d'adoption « toutes auto-déclarées » (veille, § 10) |
| Revue de littérature | 15 août 2026 | notices arXiv : **12 pièces attestées sur 189 (6 %)**, **32 auto-déclarées (17 %)**, **145 sans signe de revue (77 %)** | « le lire comme une part du champ serait circulaire » |

**Un plafond.** L'anatomie de MCP et d'A2A, la pile et la sémantique descendent du compendium, qui les
tient du Vol. I en régime **[C]** : *une porte franchie après coup ne rétroagit pas sur un texte écrit
sans elle* (compendium, ch. 1 § 1.8). Rien ici ne le relève.

**Un écart de dates.** Dix-neuf jours séparent les deux gels, mais la matière protocolaire du
compendium porte celui de *sa source*, juin 2026 — deux mois et demi plus tôt. L'écart est de nature :
le compendium décrit un contrat, la veille décrit un dépôt et une file de demandes de tirage. *Les
deux mesurent le même objet à deux profondeurs, et c'est pour cela qu'ils se contredisent utilement.*

⚠ Les deux bornes du corpus académique — **plafond** du non-arbitré, **plancher** de l'arbitré —
sont posées pour tout le rapport aux liminaires (ch. 0 § 1) ; elles se reportent ici sans
s'améliorer. *Le chiffre reste exact de ce qu'il mesure — la notice — et faux de ce qu'on lui
faisait dire.*

---

### 1.2 — Le passage du déterministe à l'agentique : ce qui ne change pas

Le chapitre 1 du compendium pose le socle **pré-agentique**, une seule fois, sur une thèse économique
avant d'être technique : *l'interopérabilité n'est pas un attribut mais une propriété à maintenir dans
le temps*. Quatre de ses acquis se transportent tels quels.

**L'explosion combinatoire et son remède.** Raccorder *N* systèmes deux à deux peut requérir jusqu'à
*N*(*N*−1)/2 liaisons ; le modèle canonique ramène le coût en 2*N* (compendium, ch. 1 § 1.0.1 et § 1.6.1 — régime
[C]). Le chapitre 8 relève que la couche de contrat agent-outil est **le même geste** transposé à
l'axe vertical : *N*×*M* ramené à *N*+*M* (compendium, ch. 8 § 8.1.1). Le patron a ses pièges — un canonique trop
ambitieux « recouple paradoxalement les parties par sa lenteur de changement ».

**Le couplage ne disparaît pas, il se déplace** (compendium, ch. 1 § 1.3) — la couche agentique le rejoue au
transport de MCP, aux passerelles multi-fournisseurs et au verrouillage inverse.

**La pile canonique est cumulative** — technique, syntaxique, sémantique, organisationnel
(compendium, ch. 1 § 1.1.2). Le compendium y accroche ce qu'il déclare « le constat le plus important du
Livre I » : MCP et A2A opèrent au niveau syntaxique et, partiellement, technique ; ils ne
fournissent aucun mécanisme d'accord sémantique, qu'ils présupposent. Il précise qu'il **ne
l'établit pas** : il le rend seulement *formulable*, l'établissement revenant aux chapitres 8 et 9.

**La gradation des contrats** — syntaxique, sémantique, comportemental (compendium, ch. 1 § 1.1.3.2) — sert de
diagnostic : les Agent Cards sont des **contrats syntaxiques dotés d'une intention sémantique**, et
aucun n'est un contrat comportemental.

S'y ajoute la distinction qui départage promesse et réalisation. Le cube ISO 11354-1:2011 oppose
l'approche **intégrée**, l'**unifiée** (méta-modèle pivot) et la **fédérée** (adaptation à l'exécution,
aucun format imposé). Le compendium écrit que l'**ambition** des protocoles agentiques relève du
fédéré et leur **réalisation de 2026** de l'unifié — schéma d'Agent Card, schéma d'outil —, et qualifie
l'écart : « ce n'est pas un défaut de mise en œuvre : c'est le prix de la vérifiabilité »
(compendium, ch. 1 § 1.2.1). Il pose la distinction et ne tranche pas le classement.

---

### 1.3 — MCP : un contrat réel, et étroit

L'axe agent-outil est un **triangle hôte / client / serveur** en appels de procédure JSON. L'apport
propre à une lecture d'interopérabilité n'est pas les primitives mais la **grille de contrôle** : **outils** contrôlés par le modèle, **ressources** par l'application, **gabarits
d'invite** par l'utilisateur — « une clause du contrat, non un détail d'implémentation » (compendium,
ch. 8 § 8.1.2, tableau 8.1). Trois **primitives client** inversent le sens du dialogue :
échantillonnage, sollicitation, racines. Le compendium en porte lui-même la critique : le
protocole « ne porte pas de couche riche de négociation de capacités ni de confiance établie », et
l'appariement est conforme « au transport et au schéma, non au sens » (compendium, ch. 8 § 8.1.1). *Le contrat est réel
mais étroit : il fixe la forme de l'échange, pas son interprétation.*

La révision `2026-07-28` a périmé cette anatomie en bloc, et le compendium l'écrit à côté du texte
qu'elle périme plutôt qu'à sa place. Cinq jalons en moins de deux ans (tableau 8.3 : 2024-11-05,
2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28) ; la cinquième, gelée le 21 mai 2026, ratifiée le
28 juillet 2026 — le lendemain de la rédaction du chapitre —, revalidée le 30 juillet 2026 sur
le journal des changements extrait à sa source :

- **racines**, **échantillonnage** et **journalisation** passent à l'état **déprécié** ; la requête
  serveur-vers-client cède au patron des **requêtes à tours multiples**, le serveur renvoyant un
  résultat typé `input_required` que le client rejoue (compendium, ch. 8 § 8.1.2) ;
- le cœur devient **sans état** : suppression des sessions, de la poignée de main et de la reprise de
  flux ; apparition d'une méthode de découverte (compendium, ch. 8 § 8.1.3) ;
- une **politique de cycle de vie et de dépréciation** est adoptée — *actif*, *déprécié*, *retiré*,
  préavis d'au moins **douze mois** — et s'exerce dans la même révision (compendium, ch. 8 § 8.3.1) ;
- l'**enregistrement dynamique de client** (RFC 7591) est déprécié au profit des documents de
  métadonnées d'identifiant client (compendium, ch. 8 § 8.2.2).

Le fait le plus instructif corrige la lecture d'origine. Le tableau des transports lisait la
trajectoire comme une décroissance monotone du couplage ; la dernière marche « échange un couplage
d'infrastructure contre une obligation de réémission côté client » — un flux rompu perd la requête en
vol. Le couplage ne disparaît pas davantage ici qu'ailleurs : il se déplace vers l'appelant.

La veille confirme la révision toujours courante au 15 août 2026 et ajoute ce que le compendium ne
pouvait pas porter (veille, § 4.1) : les en-têtes `Mcp-Method` et `Mcp-Name` **exigés** sur les POST,
« première concession de la couche commune au plan de contrôle d'*agent mesh* » ; **deux dérogations à
la fenêtre de douze mois**, portées ici toutes les deux parce qu'aucune ne se déduit de l'autre et que
le § 1.8 de ce chapitre en tire la conséquence — **retrait accéléré à quatre-vingt-dix jours sur risque de sécurité
actif**, et **retrait du transport HTTP+SSE trois mois après que la proposition SEP-2596 atteint le
statut *Final*** ; le fait que la révision rompt la compatibilité ; et, le 5 août 2026, la
charte du groupe
*Agents*, qui se donne pour livrable de promouvoir l'extension *Tasks* **dans le protocole de base** —
« mouvement inverse de celui que la révision venait d'opérer, huit jours plus tôt ». *En dix jours, la
frontière du protocole de base bouge deux fois.*

⚠ Une réserve de formulation est tenue partout. Ce protocole est assorti d'un **cadre
d'autorisation**, jamais qualifié de « sécurisé » (réserve F-01 du Vol. II, quatre occurrences
marquées au chapitre 8) — et la veille y arrive autrement : les principes du protocole « ne sont pas
*imposables* au niveau du protocole », l'autorisation OAuth « ne couvre que le transport HTTP ».

---

### 1.4 — A2A : la carte, la tâche, et l'opacité voulue

L'axe agent-agent fixe ses structures en version 1.0 : l'**Agent Card** publiée à un emplacement bien
connu, déclarant identité, capacités et modalités d'interaction ; la **tâche** comme unité de travail
à cycle de vie défini ; la hiérarchie **message / partie / artefact**. Trois consolidations sont
relevées : **signature des cartes** liée au domaine d'origine, **multi-location**, **pluralité de
liaisons de transport** — le protocole « ne réinvente pas la couche de transport » (compendium,
ch. 8 § 8.4.2).

La qualification du compendium est le modèle du genre. Une carte signée **démontre** que la
carte a été émise par le détenteur de la clé associée au domaine déclaré et n'a pas été altérée ; elle
**ne démontre pas** que l'agent se comporte conformément aux capacités déclarées, ni que le domaine
est digne de confiance. *Signer une déclaration l'authentifie ; cela ne la rend pas vraie.*

La veille précise la mécanique et réfute un de ses propres énoncés antérieurs : la
canonicalisation RFC 8785 et les six étapes de vérification sont au niveau **MUST**, seul le
*déclenchement* étant *SHOULD* (annexe, *Énoncés réfutés*). Elle date la lignée : lancement avril
2025, transfert à la Linux Foundation le 23 juin 2025, signature des cartes en v0.3.0 (juillet
2025), v1.0.0 le 12 mars 2026, correctif v1.0.1 le 28 mai 2026, `a2a.proto` élevé en source
normative unique (veille, § 4.2).

Deux traits de conception comptent pour la suite. La **délégation** franchit la frontière
organisationnelle — « le niveau le plus élevé de l'interopérabilité conceptuelle » — sans intégration
préalable. L'**opacité voulue** fait que l'agent distant n'expose ni son raisonnement, ni ses outils,
ni son modèle : « pendant agentique du découplage », dont le compendium signale en lecture d'auteur
la tension — un exploitant tenu de démontrer devant un tiers ne peut pas produire l'état d'un
traitement délégué en bloc à un agent opaque (compendium, ch. 8 § 8.4.3).

La doctrine qui donne son titre au chapitre 8 est attribuée, et l'attribution est le fait. « Dans
les agents, entre les agents » est **déclarée par le projet A2A** dans l'annonce de sa v1.0 ; le
compendium ne dispose d'aucune source établissant que l'autre projet l'a endossée dans ces termes.
⚠ Deux réserves s'y ajoutent : la formule « de nombreux systèmes utilisent les deux » est **refusée
comme métrique** — ni chiffrée, ni datée, ni définie, et émanant du même projet ; et le **verbatim**
que le socle citait n'a pas été retrouvé à sa source le 28 juillet 2026 (compendium, ch. 8 § 8.6.3). *Le fond est
attesté, la citation littérale ne l'est pas.*

Et un critère n'est pas une contrainte. Rien n'empêche de faire transiter par des appels
d'outils ce qui est une délégation entre agents, ou l'inverse ; les **tâches asynchrones** de l'axe
vertical empiètent d'ailleurs sur le terrain de la délégation. La veille y arrive par la gouvernance :
les deux protocoles « vivent sur des **horloges de gouvernance divergentes** », leur complémentarité
« ne s'accompagne d'aucune coordination des calendriers », et *l'intégrateur qui consomme les deux
porte seul le risque de leurs révisions indépendantes* (veille, § 4.2).

Le contrôle des deux contrats est le point où la veille corrige le plus le compendium — et
elle-même. Le compendium pose, au gel de juin 2026, que la **certification par un tiers
indépendant** « n'existe qu'à l'état d'amorce » (compendium, ch. 9 § 9.5.3). La veille réfute deux de ses
propres éditions antérieures (veille, § 4.5, § 7.5 ; annexe, *Énoncés réfutés*) : « aucune suite de
conformité publique » est faux — `modelcontextprotocol/conformance` existe depuis le 10 juillet 2025,
`a2a-tck` depuis mai 2025 — et « dépôt immobile » l'est aussi : *un fait négatif de dépôt ne s'établit
pas sur la branche par défaut*. ⚠ Ce qui reste vrai est plus précis : ce
sont des suites gouvernées par le projet même qu'elles vérifient, aucune certification n'en
découle, et elles vérifient le protocole, non la sécurité — rien n'y teste l'atténuation d'un
mandat, la validation d'un émetteur ou la révocation. Une exception : depuis le 28 juillet 2026, une
proposition MCP *Standards Track* n'atteint le statut final que si un scénario a été versé à la suite
de conformité — « **premier dispositif du corpus qui subordonne la normativité à la testabilité** ».

Ce que « conforme » et « interopérable » nomment n'est pas la même chose, et le compendium en donne
l'instrument. La distinction est posée au ch. 3 § 3.4.3 du compendium — la **conformité** atteste qu'une
implémentation respecte une spécification ; l'**interopérabilité**, que deux implémentations
« échangent et utilisent **effectivement** » ce qu'elles s'échangent — et le ch. 9 § 9.5.1 du compendium en tire du
**Vol. I *Monographie* §3.12.1** une **pyramide d'évaluation à trois étages** (tableau 9.4 —
régime [C]) :

| Étage | Ce qu'il mesure | Nature |
|---|---|---|
| Conformité protocolaire | un message est-il valide ? une transition d'état légale ? | **déterministe et automatisable** |
| Interopérabilité entre implémentations | deux implémentations distinctes du même protocole se comprennent-elles ? | déterministe, plus coûteux |
| Bancs de tâches inter-agents | la collaboration produit-elle le résultat attendu ? | **intrinsèquement non déterministe** |

Aucun étage ne subsume le suivant : *franchir la poignée de main n'implique pas l'accord
sémantique sur l'intention.* C'est ce qui situe exactement les deux suites de conformité du paragraphe
précédent — elles tiennent le **premier étage**, et l'attestation par un tiers, qui validerait le
second au sens mesurable, « n'existe qu'à l'état d'amorce » (compendium, ch. 9 § 9.5.3). Le compendium ajoute le test le
plus propre à l'interopérabilité agentique : la **négociation** de version et de capacités, où il
s'agit de vérifier **rétrocompatibilité et dégradation gracieuse** lorsque deux pairs n'annoncent pas
le même jeu de fonctionnalités — enjeu qui *devient crucial* avec le cœur sans état et le cadre
d'extensions, puisqu'un client doit pouvoir interagir avec un serveur ignorant une extension sans
rompre l'échange. S'y ajoutent les **tests aller-retour**, qui éprouvent la fidélité de traduction
d'un message franchissant la frontière entre deux écosystèmes — « première mesure concrète, quoique
partielle », de la fidélité de transfert d'intention. ⚠ Le sommet, lui, porte son degré : aucun banc
standardisé véritablement inter-fournisseurs ne s'impose à juin 2026, gel de la source, et c'est une
**absence de documentation au sens de R-14**, non un fait négatif vérifié.

---

### 1.5 — La sémantique : le niveau que la pile présuppose

La thèse du chapitre 2 tient en une phrase, que le chapitre 9 reprend **par copie** :
« l'interopérabilité sémantique — accord sur le sens, pas seulement sur le format — est le niveau que
les protocoles agentiques **présupposent** et que **peu savent établir** ». La forme bornée prime :
« peu savent établir » affirme moins que « ne fournissent pas » (compendium, ch. 9 § 9.4).

Le socle formel existe et il est ancien (compendium, ch. 2 § 2.3 — régime [C], aucune entrée du socle
consolidé ne couvrant le périmètre de ce chapitre) : RDF, dont deux graphes hétérogènes fusionnent
par simple union de triplets pourvu qu'ils partagent des identifiants ; RDFS, SKOS et OWL 2 pour
l'inférence ; JSON-LD comme pont vers les API existantes ; SPARQL et sa fédération ; SHACL comme
contrat sémantique vérifiable aux points d'échange. La confusion « qui se paie le plus cher » y est
nommée : OWL sert l'**inférence** sous monde ouvert, SHACL la **validation** sous monde clos ; les
confondre produit des contrôles qui ne se déclenchent jamais. ⚠ Et la borne de la couche syntaxique
est posée au même endroit : une garantie de compatibilité de schéma n'est pas une garantie de sens —
« une même colonne *montant* qui passe des dollars aux cents satisfait toutes les règles et casse ses
consommateurs » (compendium, ch. 2 § 2.1.5) —, ce que les registres n'attrapent pas relevant d'une **absence de
documentation** au sens de R-14, non d'un fait négatif vérifié.

Au plan agentique, le diagnostic vient d'une grille à trois plans appliquée à **dix-huit protocoles**
(Yuan et coll., 2026, cités au ch. 9 § 9.4.1 du compendium) : maturité correcte en communication et en syntaxe,
pauvreté en mécanismes de clarification, d'alignement et de vérification du sens, repoussés vers
la couche applicative. Le compendium en tire l'écart décisif : la description d'un outil est du
**texte libre lu par le modèle à l'inférence** ; le schéma type la forme, « c'est la prose descriptive
— non vérifiable et non contraignante — qui porte le sens de l'opération et son effet réel » (compendium, ch. 9 § 9.4.2).
*La description est à la fois le contrat d'interopérabilité de l'outil et son point de vulnérabilité.*

La revue fait passer ce constat de « défi ouvert » à résultat mesuré. Sur 856 outils de
103 serveurs MCP, **97,1 %** des descriptions portent au moins un défaut et **56 % n'énoncent pas
clairement leur objet** ; les enrichir **ne gagne que 5,85 points médians de succès**, **allonge
l'exécution de 67,46 %** et **régresse dans 16,67 % des cas**. Sur 19 200 paires description/code
issues de 2 214 serveurs réels, **9,93 %** sont incohérentes, « sans qu'aucun mécanisme du protocole
ne vérifie que la description reflète l'implémentation » (*Les protocoles d'interopérabilité*).
⚠ Ces pièces relèvent du corpus arXiv dont 77 % ne portent aucun signe de revue par les pairs à leur
notice. *Le remède mesuré coûte donc plus de deux tiers de latence pour six points de succès, et se
retourne une fois sur six : ce n'est pas un correctif, c'est un arbitrage.*

La veille tranche la question du vocabulaire par examen direct des spécifications : la réponse est
non (veille, § 4.9). Dans A2A v1.0, les `tags` de l'*AgentSkill* ne sont « qu'un ensemble de mots-clés », et
« taxonomy », « ontology », « schema.org » et « JSON-LD » sont **absents de toute la spécification**.
L'**unique taxonomie normalisée vérifiée** est l'OASF d'AGNTCY — dix-huit catégories de premier
niveau, trois niveaux, champ de compétences obligatoire —, opérationnalisée par l'annuaire `dir`.
Trois observations la bornent : **aucun commit au dépôt OASF depuis le 21 juillet 2026** ; aucune
référence à sa taxonomie dans un autre protocole du corpus ; et la surface de découverte qui a le
plus crû emploie des étiquettes libres. *Le vocabulaire normalisé existe ; le premier annuaire venu ne
l'emploie pas* — le registre MCP officiel assumant ce refus, sa recherche par sous-chaîne étant
déclarée « intentionally simple ».

La voie de sortie que le compendium examine déplace le problème plutôt qu'elle ne le résout, et il
l'écrit. Confier la réconciliation sémantique au modèle lui-même — apparier dynamiquement deux
vocabulaires plutôt que définir *a priori* un schéma pivot — offre flexibilité, tolérance aux
désalignements de surface et absence de canonique à maintenir. Ses risques sont d'une autre nature :
**hallucination d'alignement** — une correspondance **plausible mais fausse** —, **non-déterminisme de
la médiation**, et **dette technique déplacée du schéma vers les invites**, plus difficile à
versionner et à auditer (compendium, ch. 9 § 9.4.4 — régime [C]). La position tenue vient du **Vol. I
*Monographie* §3.5.4**, et le compendium la reprend « comme une position, jamais comme un fait » :
*la médiation par modèle complète, mais ne remplace pas, l'interopérabilité sémantique formelle.*
Cette **synthèse neuro-symbolique** — un raisonnement **contraint par l'ontologie** — est argumentée
par **Tuan et Sanyal (2026)**, dans une architecture où le raisonnement neuronal opère sous la
contrainte d'une ontologie de domaine : la couche formelle stabilise le contrat, la couche neuronale
absorbe l'évolution. ⚠ Deux bornes l'accompagnent, aux formes du corpus. Au sens de **R-02**, un
appariement produit par modèle **démontre une plausibilité lexicale** et **ne démontre pas une
équivalence sémantique**. Et que la fiabilité de ces appariements n'ait **aucune mesure établie hors
bancs dédiés** est une **absence de documentation au sens de R-14**. *Le débat oppose deux régimes de
garantie — la médiation purement neuronale maximise le rappel au prix de la précision vérifiable,
l'architecture contrainte par l'ontologie borne l'espace des alignements admissibles — et la question
ouverte n'est pas l'architecture, c'est la mesure* : comment propager une garantie de correction à
travers une chaîne de délégations probabilistes.

Le chapitre 2 clôt son parcours par un renversement qui appartient à ce dossier. Adosser la
génération augmentée à un **graphe structuré** extrait des sources plutôt qu'à un index vectoriel plat
(**Edge et coll., 2024** ; ch. 2 § 2.4 du compendium — régime [C]) rend trois choses : **réduction des
hallucinations** par ancrage sur des entités et relations attestées, **traçabilité** de chaque
assertion aux nœuds et arêtes qui la fondent, et — le seul volet que le socle établit — l'**ontologie
comme garde-fou**, un schéma de classes et de relations imposé qui circonscrit l'espace des
inférences admissibles. Le compendium borne aussitôt : la **hiérarchie des trois volets** et leur
réemploi en aval sont donnés comme **lecture d'auteur**, non établis. *Jusqu'ici la sémantique servait
à ce que deux systèmes se comprennent ; ici elle sert à borner ce qu'un système a le droit de
conclure* — le contrat de sens cesse d'être un instrument de coopération pour devenir un instrument
de contrainte.

---

### 1.6 — Découvrir, nommer, résoudre : UDDI rejoué, et la portabilité

La proposition organisatrice du chapitre 9 contredit une lecture naturelle : la nouveauté ne tient pas
à la découverte prise isolément — l'intégration d'entreprise la pratique depuis longtemps — mais au
**couplage indissociable de la découverte, de l'identité et de la confiance** (compendium, ch. 9 § 9.1). Trois moments
sont à ne pas confondre : **découverte**, **sélection**, **résolution**. La difficulté se concentre
au deuxième : les capacités étant décrites en langage naturel assorti de schémas, la sélection devient
un **appariement sémantique, intrinsèquement probabiliste**, qui « ne peut, en l'état des protocoles,
s'appuyer sur aucune garantie déterministe d'adéquation ».

La récurrence historique est le fil de la section, et elle est bornée. Les annuaires UDDI publics
ont été retirés dès 2006 (compendium, ch. 1 § 1.3.1.2) ; le pendule est revenu vers des catalogues gouvernés ; les
registres d'agents prolongent la récurrence. Le compendium en tire deux propositions — *la découverte
sous curation surpasse le tout-dynamique*, *la fédération surpasse la centralisation* — et les
qualifie aussitôt : **inférées d'une récurrence observée, non démontrées**, soit une absence de
documentation au sens de R-14 (compendium, ch. 9 § 9.1.1). Suivent les modes d'échec propres au registre : description
mensongère, typosquattage, appropriation d'espace de noms, registre empoisonné, point unique de
défaillance recréé — contre lesquels *signer une carte mensongère produit une carte mensongère
authentifiée*. La veille en fournit la démonstration par l'incident — la version 1.8.1 du registre MCP
officiel corrige une **prise de contrôle d'espace de nommage d'organisation exploitable via
`github.io`** — et par la procédure : la normalisation du chaînon a été **tentée et refusée**, BoF
GARR écartée le 22 mai 2026 (veille, § 7.3).

Le décompte de serveurs est l'endroit où la veille est la plus utile, et son enseignement porte
sur l'instrument. Le compendium écrivait, au gel de sa source, que l'écosystème « dépasse les dix
mille serveurs publics » (compendium, ch. 8 § 8.3.2). La veille recalcule par pagination exhaustive du registre
officiel le 15 août 2026 : avec le filtre `version=latest`, **21 767 enregistrements** dont
**21 520 actifs et 247 dépréciés** ; sans filtre, **73 072** — « l'écart entre 2 000 et *plus de
10 000* qui traînait dans la littérature n'était pas une querelle de sources, c'était une querelle de
curseur » (veille, § 6.3). Trois bornes du même auteur l'accompagnent : ce sont des **enregistrements
auto-publiés**, jamais des serveurs vérifiés en exploitation ; le nombre est « daté à l'heure, non à
la journée » ; et un audit dynamique indépendant du 31 juillet 2026 annonce **plus de 21 000 instances
détectables**, **même ordre de grandeur** par une méthode distincte — « le premier recoupement
indépendant dont dispose ce domaine ».

⚠ Le compendium range ces protocoles dans une matrice, et l'instrument porte sa propre date de
péremption au front. Reprise du **Vol. I *Monographie* §3.7.5** à l'état de juin 2026
(compendium, ch. 9 § 9.2.5, tableau 9.3 — régime [C]), elle croise axe couvert, statut de maturité, gouvernance et
usage recommandé, et son en-tête déclare qu'elle **se périme en bloc** : *c'est un instantané, non un
classement durable*, et *ce qui est marqué candidat ou expérimental ne doit pas être déployé comme
acquis*. Sept lignes y tiennent les neuf de la source, par deux regroupements et aucun retrait —
la couche commerciale pour deux spécifications, la couche agent-humain pour deux également, cette
dernière retenant le statut le plus prudent des deux.

| Protocole | Axe | Statut | Gouvernance | Usage recommandé |
|---|---|---|---|---|
| Agent-outil | vertical | production ; révision stable, **candidate à venir** | fondation dédiée | socle pour exposer outils et ressources ; adopter la révision datée stable, traiter le cœur sans état comme cible |
| Agent-agent | horizontal | production ; version 1.0 stable, écosystème large | fondation faîtière | standard de fait pour la délégation ; combiner avec le précédent |
| Décentralisé | horizontal + identité | **émergent** ; conditionné à la maturité de son socle d'identité | communauté et groupe de normalisation | topologies pair-à-pair et négociation de méta-protocole ; horizon ≈ 2027 |
| Règlement (mandat) | économique | **émergent** ; version préliminaire | fondation distincte du reste de la pile | couche de mandat vérifiable ; suivre la trajectoire |
| Règlement (machine-natif) | économique | émergent **à traction réelle** | fondation dédiée | micropaiements ; la plus forte traction de production de sa couche |
| Commerce (paiement) | commercial | émergent ; spécification **mouvante** | consortium d'éditeurs | achat agentique ; à suivre par révision datée |
| Interface agent-humain | agent-humain | **expérimental** | fondation dédiée / communauté | validation et interfaces riches ; hors production critique |

⚠ Le jalon d'adoption qui l'accompagne est **auto-déclaré et attribué** : **plus de 150 organisations
de soutien au 9 avril 2026** pour l'axe agent-agent, rapporté par la Linux Foundation, qui gère le
protocole — *soutien n'est pas production*. La logique de décision qu'en tire le compendium tient en
trois temps : les deux axes principaux constituent le socle minimal d'un système interopérable de
production ; la couche agent-humain s'ajoute dès qu'un point de validation ou une interface riche est
requis ; la couche de règlement, segment le moins stabilisé et à gouvernance distincte du reste de
la pile, n'intervient que pour les cas commerciaux — les protocoles marqués émergents appelant
une veille active plutôt qu'un engagement architectural irréversible. ⚠ *Et la péremption annoncée
est déjà advenue sur une ligne au moins* : la ligne agent-outil porte « révision stable, candidate à
venir » et traite le cœur sans état comme **cible**, quand le § 1.3 de ce chapitre le donne pour courant depuis le
28 juillet 2026. L'instrument reste exact à sa date ; il ne l'est plus à celle de ce chapitre, et
c'est très exactement ce que son en-tête annonçait.

La portabilité porte le paradoxe le plus net. L'interface *Chat Completions* d'OpenAI
s'est imposée comme norme de fait sans qu'aucun organisme ne l'ait spécifiée ; elle découple
l'application du fournisseur, et cette même portabilité « instaure un verrouillage inverse — non plus
à un fournisseur mais à un **schéma** », dont l'évolution « échappe à tout contrat public » (compendium, ch. 9 § 9.3.1).
Le compendium signale la relève : dépréciation de l'*Assistants API* annoncée le 26 août 2025,
retrait fixé au 26 août 2026 — onze jours après le gel de la veille, qui ne pouvait donc pas en
constater l'exécution. Il n'a pas versé cette échéance à son tableau des événements datés et a
**ouvert une remontée** : *un rédacteur ne complète pas un cardinal contrôlé, il remonte.* Deux
manques sont enfin nommés au même rang que les acquis (compendium, ch. 9 § 9.3.4) : **aucun format d'agent portable et
neutre**, **aucune portabilité de l'état et de l'exécution durable**. *La définition voyage ;
l'exécution, elle, reste captive.*

---

### 1.7 — La transaction et l'infrastructure : où l'interopérabilité devient responsabilité

Le chapitre 10 décompose sa thèse avant de l'employer : que la transaction agentique soit
l'aboutissement financier de la pile est une **lecture d'auteur** ; qu'AGNTCY soit une couche
d'infrastructure et non un concurrent est un **positionnement déclaré du projet**. *Aucune des deux
n'est un fait établi.*

Ce que le compendium établit, et ce qu'il refuse d'écrire. AP2 a été annoncé le 16 septembre
2025 comme protocole compagnon de l'axe agent-agent ; le communiqué de la Linux Foundation du
9 avril 2026 donne **plus de soixante organisations** déclarant leur soutien, dont **sept
nommées** — réseaux de paiement et émetteurs. ⚠ Chiffre auto-déclaré, que la re-datation du 28 juillet
2026 n'a pas retrouvé à sa page source : *un décompte qu'on ne retrouve plus à sa source n'est pas
devenu faux ; il est devenu invérifiable, ce qui est un état différent et qui doit se dire.* ⚠ Le compendium déclare en outre ne pas pouvoir écrire l'**anatomie
technique** d'AP2 — ni structure des messages, ni mécanique de mandat, ni modèle de preuve d'intention
au socle du Vol. II, degré 3 — et « s'y refuse plutôt que d'emprunter à une connaissance non tracée »
(compendium, ch. 10 § 10.1.4).

Le chapitre 10 porte le seul cas du corpus où deux volumes ne disent pas la même chose. Le
Vol. II, gelé au 16 juillet 2026, ne documente aucun transfert de gouvernance d'AP2 ; le Vol. I, gelé
en juin 2026 — donc **antérieur** —, porte le transfert à la FIDO Alliance le 28 avril 2026, en
**v0.2**. Le compendium refuse d'arbitrer : « le socle du Vol. II ne documente pas X » et « le Vol. I
documente X » sont **logiquement compatibles**, le premier décrivant un corpus de sources, le second
un événement ; les deux entrées « coexistent sans arbitrage » au socle consolidé.

La veille y ajoute ce qui manquait : ce que le transfert a produit. AP2 est le *seul* transfert
agentique vers un organisme de normalisation établi (veille, § 5). Or **aucun commit sur sa branche principale
depuis le 29 avril 2026**, spécification inchangée et muette sur la FIDO, laquelle ne publie rien
sur ses deux groupes agentiques depuis l'annonce du 28 avril. *Trois mois et demi de silence des
deux côtés du transfert* — d'où la formule qui vaut pour toute la couche : « la migration
institutionnelle dit qui tient la plume, non si quelqu'un écrit ». Le contraste est symétrique : x402,
mis sous fondation le 2 avril 2026 (compendium, ch. 10 § 10.3.4), est celui qui bouge — et « c'est le
protocole qui bouge qui se fait trouer » : du 29 juillet au 13 août 2026, **cinq correctifs de
sécurité**, dont trois touchant l'encaissement, aucun n'ayant fait l'objet d'un avis formel
(veille, § 4.8). ⚠ Le site de sa fondation **refuse la connexion chiffrée au 15 août 2026**, ses quarante
membres étant déclarés **invérifiables**.

La couverture des deux livrables ne s'emboîte pas. Le compendium porte MPP, lancé le 18 mars
2026 (compendium, ch. 10 § 10.3.4) ; la veille le déclare, au 15 août 2026, « absent de toutes les éditions
antérieures » (veille, § 4.8). *La fraîcheur d'un gel ne prédit pas la couverture.*

Sous ces protocoles, les réseaux de cartes ont étagé plutôt que remplacé, et le compendium en donne
le tableau daté (compendium, ch. 10 § 10.3.3, tableau 10.2 — régime [C]). Même régime que la matrice du
§ 1.6 de ce chapitre, et il est déclaré tel à sa source : *instantané, ni classement ni recommandation, se périme en
bloc*.

| Initiative | Porteur | Date | Mécanique, telle que les sources la portent |
|---|---|---|---|
| Protocole d'agent de confiance (TAP) | un réseau de cartes, avec un fournisseur d'infrastructure de périphérie | 14 octobre 2025 | signe l'identité de l'agent dans des en-têtes HTTP, au moyen des signatures de message HTTP normalisées et d'une mécanique d'authentification de robot, sur clés à courbe elliptique |
| Paiement d'agent et jetons agentiques | un second réseau de cartes | 2025 | prolonge l'infrastructure de tokenisation existante, le jeton étant lié à un périmètre marchand et à un consentement |
| Groupe de travail paiements de la fondation d'authentification | coprésidé par les deux réseaux de cartes | 2026 | bâtit sur **AP2** et sur un cadre d'**intention vérifiable** |
| Authentification de robot par le web | un fournisseur d'infrastructure de périphérie, en cours de spécification à l'organisme de normalisation d'Internet | en cours, 2026 | l'agent signe ses requêtes par les signatures de message HTTP et publie sa clé publique sous un chemin de découverte normalisé |

Deux lectures s'en tirent, et elles ne pèsent pas pareil. *(1)* La convergence institutionnelle est
documentée : que le groupe de travail paiements soit coprésidé par les deux réseaux et bâtisse sur
AP2 confirme par une seconde voie ce que le transfert de gouvernance disait déjà — deux voies
indépendantes mènent au même constat, et c'est ce qui lui donne son poids. *(2)* Le mécanisme
transversal est une primitive, pas une garantie. Une signature de requête permet à un commerçant de
distinguer un agent identifiable d'un trafic automatisé indistinct et d'appliquer une politique
différenciée à la frontière ; elle ne rend le trafic ni légitime ni sûr — *une requête signée est
attribuable*, et l'attribution est un cadre d'autorisation, jamais une propriété de sécurité
(réserve F-01).

Le titre de cette section n'est pas décoratif, et le chapitre 10 pose les trois questions qu'aucun
message valide ne résout (compendium, ch. 10 § 10.4.1) : **qui est le commerçant de référence**, le rôle juridique qui
porte la vente — *les montages observés le conservent généralement tel quel* ; **comment trancher un
litige ou un impayé contesté** lorsque l'acheteur n'était pas présent ; **comment garantir la
non-répudiation** d'une transaction déclenchée par une machine. C'est là que le Livre boucle sur
son propre invariant : les chapitres précédents établissent que l'accord de protocole ne fait pas la
compréhension ; celui-ci, que *la compréhension ne fait pas l'imputation* — trois agents peuvent
parfaitement se comprendre et laisser un litige sans destinataire. La réponse documentée est le
**mandat tokenisé comme couche de preuve opposable** : la chaîne *intention → panier → paiement*,
signée et horodatée, rattache une transaction contestée à un consentement antérieur du mandant.
⚠ La réserve F-01 « mord ici plus qu'ailleurs » : un mandat signé *prouve qu'un consentement a été
émis, pas qu'il était éclairé, ni que l'agent qui l'a sollicité était intègre*. ⚠ Au plan
réglementaire, le compendium déclare son propre paragraphe le plus faible du chapitre : le
**Règlement (UE) 2024/1689** encadre notamment les modèles à usage général — obligations applicables
depuis août 2025, mise en conformité générale jusqu'au 2 août 2027 —, énoncé qui résout contre
le **Vol. I *Monographie* §3.9.5**, donc en **[C]**, central en aucune de ses parties : *une date
réglementaire reprise d'un volume à un autre ne devient pas vérifiée par le trajet*. ✎ La
re-vérification a eu lieu ailleurs qu'ici, et la seconde échéance ne tient pas : au régime de la
veille du 15 août 2026, le règlement **s'applique depuis le 2 août 2026** dans presque toute son
étendue — article 50, modèles à usage général, gouvernance et sanctions —, seul le haut risque
étant reporté, et le 2 août 2027 n'est, au compendium même, qu'une période de grâce documentaire
pour les modèles mis sur le marché avant le 2 août 2025, non une mise en conformité générale
(veille, § 8.1 ; compendium, ch. 30 § 30.1.1 ; ch. 4 § 4.12 pour l'instruction). ⚠ Et les sources
ne documentent aucun régime de litige propre à la transaction agentique — *absence de
documentation, R-14 degré 3*. Une preuve technique n'a de valeur que devant une procédure qui
l'admet, et l'existence de cette procédure n'est pas établie.

Le seul protocole de cette couche qui soit mort documente ce qu'un architecte achète réellement.
L'ACP protocolaire est lancé le 17 mars 2025 en version pré-alpha, d'abord conçu comme extension
de l'axe agent-outil, et confié à la fondation faîtière dès ce mois-là ; un billet du 28 mai 2025
affiche l'ambition d'en faire *le HTTP de la communication entre agents* ; la fusion dans l'axe
agent-agent est actée le 29 août 2025 — cinq mois et douze jours après le lancement,
trois mois et un jour après le billet doctrinal (compendium, ch. 10 § 10.5.1, tableau 10.3 ; intervalles
calculés à partir des seules dates portées par les sources). **Garde-fou R-1, le risque
terminologique le plus élevé du corpus source** : l'ACP protocolaire ne doit **jamais** être présenté
comme un standard vivant — son développement actif a cessé, et il ne subsiste qu'à travers le
protocole absorbant et des adaptateurs. Ce que la fusion enseigne tient en une distinction que les
dossiers de risque de tiers font rarement :

| Risque | Ce qu'il vise | Ce que la gouvernance neutre en fait, dans ce cas |
|---|---|---|
| **Le protocole peut mourir** | la pérennité de la spécification | **rien** — le développement a cessé malgré la fondation |
| **L'utilisateur peut être abandonné** | la continuité d'exploitation de qui l'avait adopté | actifs versés, adaptateurs, guides de migration |

⚠ La lecture qui l'accompagne est bornée d'un cran, et le compendium la borne lui-même : les sources
établissent les faits de la transition — actifs versés, adaptateurs livrés, guides de migration
fournis, *gestes d'une transition organisée et non ceux d'un projet qu'on éteint* — et n'établissent
pas que la gouvernance en soit la cause. *Une corrélation entre neutralité et transition ordonnée,
observée sur un cas, n'est pas un mécanisme.* Reste la formule, donnée pour lecture d'auteur : *un
architecte n'achète pas la survie d'un protocole ; il achète une sortie ordonnée si le protocole ne
survit pas.*

Et le même dossier porte l'unique péremption de prescription que le corpus mesure au calendrier.
L'article de synthèse de la période — **Ehtesham et coll., arXiv 2505.02279, mai 2025** — prescrivait
une **adoption séquentielle en quatre temps** : agent-outil, puis ACP protocolaire, puis agent-agent,
puis décentralisé. La fusion du 29 août 2025 a vidé la deuxième étape moins de quatre mois après la
publication. L'énoncé exact est plus fort qu'une péremption de contenu : *ce n'est pas qu'une
meilleure séquence soit apparue, c'est que l'un des quatre termes a cessé d'exister comme objet à
adopter* — une feuille de route dont une étape s'évanouit n'est pas à réviser, elle est sans objet sur
ce segment ; une institution qui aurait bâti sa feuille de route sur ce document au printemps 2025
aurait, à l'été, investi dans une étape devenue sans objet. ⚠ **Régime de préimpression, réserve
F-06** : la source n'est pas révisée par les pairs, et elle est reprise **à titre de jalon
historiographique, jamais comme guidance**. Le refus de généraliser est explicite au même endroit :
*une prescription protocolaire s'est périmée plus vite qu'un cycle budgétaire* — dans ce cas au
moins, « un cas ne fait pas une cadence ».

Sur AGNTCY, les deux livrables se rejoignent en changeant de registre. Le compendium établit
l'ouverture en mars 2025, le placement sous fondation le 29 juillet 2025 et un communiqué du même
jour donnant **plus de soixante-cinq entreprises** — auto-déclaré, jamais retrouvé à sa page source.
Il ajoute un refus : les sources n'en disent pas davantage — « ni spécification, ni statut de
maturité, ni version » —, et *une couche d'infrastructure dont on ne connaît ni la version ni le
statut n'est pas évaluable* (compendium, ch. 10 § 10.2.2). La veille comble ce vide par le dépôt : annuaire `dir` de la
v1.5.0 du 17 juin 2026 à la v1.6.3 du 7 août 2026, SLIM en v2.3.0 le 13 août (veille, § 4.4) — d'où un
constat que le compendium ne pouvait pas former : *le composant le plus actif du corpus protocolaire
n'est pas un protocole d'agents mais l'infrastructure qui les indexe et les achemine.*

Le verrou de la couche est nommé identiquement par les trois livrables. Le compendium cite *Debi
et coll., Whispers of Wealth, 2026*, qui soumet AP2 à une injection d'invite : « la signature des
mandats ne neutralise pas l'amont » — *un agent dont l'intention est détournée signera un mandat
malveillant parfaitement valide*. ⚠ Il borne aussitôt : ni la **fréquence de ce mode d'échec
en production**, ni le moindre **incident public daté** qui l'instancie ne sont établis — degré 3. *Un
mode d'échec démontré en laboratoire et un mode d'échec observé en exploitation sont deux faits, et un
seul des deux est ici acquis.* La revue y arrive autrement — deux injections dans le contexte d'un
agent d'achat de référence détournent le classement produit et exfiltrent des données (90 à 100 % de
réussite) — et ⚠ mesure sa propre indigence : sur les douze pièces du front, une seule porte sur un
système déployé, et aucune ne mesure de transaction réelle à valeur réelle (*La couche
transactionnelle*). La veille en tire la conséquence institutionnelle : faute de solution
inter-fournisseurs pour l'identité **des agents**, AP2 et la FIDO ancrent l'autorisation dans celle de
l'**utilisateur** — « le porteur change, le problème reste » (veille, § 9.5).

---

### 1.8 — Ce que le champ a réglé, ce qu'il n'a pas réglé

**Réglé** — au sens où un contrat existe, est daté, et se vérifie. L'axe agent-outil est un fait
accompli d'écosystème : la veille le mesure à « près d'un demi-milliard de téléchargements mensuels »
de SDK, en signalant que deux publications primaires du 28 juillet 2026 — le projet et son
fondateur — « mesurent la même grandeur et divergent d'un quart, le même jour » (veille, § 6.3, § 9.2). La
consolidation institutionnelle est réelle : le compendium date la fusion de l'ACP protocolaire dans
A2A au 29 août 2025 (compendium, ch. 8 § 8.5.1), la veille corrigeant sa propre datation pour établir l'archivage au
25 août 2025 (veille, § 4.4).

Et le compendium tire du premier engagement daté d'un protocole sur sa propre évolution la seule
conséquence qu'il déclare opposable à une institution réglementée — mais elle est conditionnelle, et
ce chapitre porte cinq sections plus haut ce qui la conditionne. L'énoncé du compendium est que le
préavis de douze mois place le premier retrait possible **après juillet 2027**, soit **au-delà du
1ᵉʳ mai 2027** que l'horloge du corpus prend pour pivot (compendium, ch. 8 § 8.3.1 — régime [C], revalidé sur
source primaire le 30 juillet 2026). Il ne vaut que pour les dépréciations qu'aucune dérogation ne
saisit. La veille porte les deux dérogations à la même phrase que le plancher (veille, § 4.1) : retrait
accéléré à quatre-vingt-dix jours sur risque de sécurité actif, et retrait du transport HTTP+SSE
trois mois après que SEP-2596 atteint le statut *Final*. Comptés depuis la ratification du 28 juillet
2026, quatre-vingt-dix jours placent le premier retrait dérogatoire possible fin octobre 2026 —
calcul de ce chapitre sur les seules dates portées par la veille —, soit plus de six mois *avant* le
pivot ; et la seconde dérogation ne se borne pas du tout, son horloge démarrant à un **statut de
proposition dont aucune date n'est fixée**. *Le plancher réel n'est donc pas de douze mois : il est de
douze mois par défaut, de quatre-vingt-dix jours sous risque de sécurité actif, et indéterminé pour un
transport dont le compte à rebours commence à un événement non daté.* ⚠ La veille elle-même tient
les deux faits ensemble sans les arbitrer : son tableau d'échéances inscrit « **au plus tôt le
28 juillet 2027**, premier retrait d'une fonctionnalité MCP dépréciée — douze mois, quatre-vingt-dix
jours si risque actif » (veille, § 12.1), *un « au plus tôt » assorti de son exception dans la même ligne*. Ce
qu'une institution réglementée peut opposer est donc une **prévisibilité conditionnelle, non une
date** — et la conséquence pratique est inverse de celle qu'on lit d'ordinaire : *le seul engagement
daté du corpus protège contre la dépréciation ordinaire, c'est-à-dire contre le cas qui ne presse
pas.*

**Non réglé** — en trois degrés d'ignorance, comme le corpus s'y astreint.

*Établi comme manquant.* Aucun vocabulaire de capacités commun ne relie MCP, A2A, ANP, les registres
commerciaux et OASF (veille, § 4.9, par examen direct des spécifications) ; aucune conformité n'est
opposable par un tiers (veille, § 4.5, § 7.5) ; la sémantique reste repoussée vers la couche applicative
(compendium, ch. 9 § 9.4.1). Et le constat le plus net est le plus daté : au **15 août 2026, aucun
protocole d'interopérabilité agentique n'est une norme *de jure***, AP2 compris — deux groupes
communautaires du W3C à **zéro Recommandation et zéro livrable**, l'un sans activité depuis juin
2025 ; à l'IETF, DAWN et DMSC, chartrés en juin 2026, portent ensemble **vingt-sept brouillons et pas
un seul document adopté** (veille, § 5, § 4.10). *Le seul indicateur qui bouge dans les deux groupes
du W3C est le nombre d'inscrits.*

*Absence de documentation, degré 3 — que le corpus s'interdit de durcir.* Aucun format d'agent
portable et neutre (compendium, ch. 9 § 9.3.4) ; aucun banc inter-fournisseurs (compendium, ch. 9 § 9.5.3) ; aucune réponse
protocolaire au verrou sémantique (compendium, ch. 8 § 8.2.3) ; aucune anatomie technique d'AP2 au socle
(compendium, ch. 10 § 10.1.4). ⚠ Dans les quatre cas la formule est la même, et tenue : *le socle n'en recense
aucun, ce qui n'établit pas qu'il n'en existe pas.*

*Non vérifié, donc fait de personne.* La veille en publie la liste, « la section qui rend les autres
croyables » : le site de la fondation x402 refuse la connexion chiffrée ; la page *Agentic AI* de la
FIDO ne porte aucune date, si bien que le fait négatif « aucune spécification agentique publiée »
repose sur une absence de mention ; **trente références** du périmètre identité et délégation n'ont
été rouvertes à aucun des deux tours, leur état au 15 août 2026 étant déclaré « **inconnu**, non
*inchangé* » (annexe, *Ce qui n'a pas pu être vérifié*). *Une entrée qu'une re-datation laisse
inchangée n'en est pas confirmée.*

Trois faits de méthode s'imposent enfin. L'auto-arbitrage du corpus de la revue — 54 % des pièces
rapportant la performance d'un artefact de leurs propres auteurs — est instruit au ch. 3 § 3.9 ; ce
qui appartient à ce chapitre est que la revue range le front des protocoles parmi ses deux fronts les
moins auto-arbitrés, à 4 sur 13, le minimum revenant à la gouvernance avec 2 sur 11
(revue, *Proposer n'est pas prouver*) : *ce corpus s'auto-arbitre à moitié.* **L'instrument de mesure est le maillon faible** — les scanners MCP
et leur taux de faux positifs, mesurés au ch. 3 § 3.9 : *un pourcentage y renseigne sur un
dispositif autant que sur le monde.* Et la
lacune que ce chapitre ne peut pas combler : aucune publication ne rapporte un taux mesuré d'échec,
de latence ou de perte sémantique pour une tâche traversant deux protocoles distincts dans un système
déployé — la seule comparaison implémentée entre deux protocoles est un scénario unique dont les
auteurs récusent la généralisation, et la seule mesure contrôlée du coût oppose MCP à une ligne de
commande, ses treize rapports appariés s'étalant de **0,43× à 29×**.

Le socle protocolaire est donc **syntaxiquement acquis, sémantiquement présupposé,
institutionnellement consolidé et normativement vide** — et la formule du chapitre 1 du compendium en
reste la lecture la plus exacte : *le couplage ne disparaît pas, il se déplace*, ici du produit vers
le schéma, du protocole vers l'exploitant, et du contrat vers l'intégrateur qui consomme deux horloges
de gouvernance indépendantes.
