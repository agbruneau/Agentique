# Chapitre 38 — L'observabilité agentique

*Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et
synthèse architecturale.
Second mouvement — exploiter (ch. 38-40). Premier chapitre du mouvement : il traite la première des
trois capacités que l'exploitation distingue — **voir**.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé sur instruction d'auteur du 27 juillet 2026, **avant** les portes **G-3**, **G-4** et **G-5**, et hors de l'ordre de rédaction du PRD §6. ⚠ **Les remontées R-IV-40 et R-IV-41, ouvertes au ch. 37, valent pour tout le Livre** et ne sont pas rouvertes ici : **G-5 conditionne le Livre entier**, et l'arbitrage du risque 14 (**D-2**) n'est pas pris |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** ([`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ☑ ⚠ **Le volet de faits de G-1 a été levé le 28 juillet 2026 — le LENDEMAIN du gel — et les entrées de ce chapitre en relèvent** ([`gel-2026-07-28-volet-residuel.md`](../PRD/gel-2026-07-28-volet-residuel.md)) : sur les vingt-deux identifiants nommés au champ suivant, **H-15 n'entre pas au socle consolidé** — exclusion déclarée, thèse attribuée et non fait — et des **vingt et un** qui y résolvent, **douze sont ☑ inchangées** (dont **quatre partielles**), **une est ☑ changée** — la conformité annoncée du § 38.2.3 —, **cinq sont ☐ non établies**, faute d'accès ou de source encore au dépôt, et **trois sont sans sensibilité temporelle**. ⚠ **Le gel ne s'avance pas d'un jour pour absorber cette passe** (D-1) : *le chapitre reste daté du 27, et les constats du 28 s'y déclarent comme tels.* ⚠ **Ce chapitre reste celui du Livre où la volatilité coûte le plus** — son objet principal est un corpus **sans version citable**, dont la seule ancre demeure une date de consultation. Gels de source : **21 juillet 2026** (Vol. III), **juin 2026** (Vol. I) ; *ils ne sont pas celui de la somme et ne peuvent en tenir lieu* |
| **Socle mobilisé** | **Aucune entrée du socle consolidé n'est mobilisée** — ⚠ la pièce a été rédigée **avant le franchissement de G-3**, acquis le **28 juillet 2026**, et **elle n'a pas été ré-adossée** à l'[Annexe B](../PRD/socle-consolide.md), qui existe désormais et alloue les identifiants `S-nnn` ; *le socle consolidé n'est plus vide, et cette pièce ne s'y adosse pas encore.* Les énoncés résolvent contre le **Vol. III *Monographie* ch. 24**, dont les entrées **F-64**, **F-65**, **F-66**, **F-74**, **F-75**, **F-76**, **F-77**, **F-78**, **F-89**, **F-90**, **F-91**, **F-95** et les entrées héritées **H-04**, **H-06**, **H-11**, **H-12**, **H-14**, **H-15**, **H-23**, **H-27**, **H-28**, **H-33** **conservent leurs niveaux d'origine** ; et contre le **Vol. I *Monographie* §2.9.6, §3.12.3 et §4.9.1-4.9.2**, qui entre **en [C]**. ⚠ **Ce champ sur-déclarait, et la re-mesure le borne : sur les vingt-deux, DIX-HUIT portent leur identifiant dans le corps, quatre n'en portent aucun.** *(a)* **H-33** y est **appliquée sans son identifiant** — le tri prospectif du § 38.2.3 et du § 38.5, dont le siège est au **ch. 49 § 49.0**. *(b)* **H-23** relève d'une **sortie de périmètre déclarée au § 38.0** — horizon de tâche déléguée au **ch. 40 § 40.3**, fondements de l'évaluation au **ch. 6**. *(c)* **H-27 et H-28 sont déclarées et non mobilisées** ; ce sont aussi **les deux dont la source a été retirée du dépôt** le 22 juillet 2026. ⚠ *Leur retrait de ce champ modifierait le socle déclaré de la pièce : il relève d'une passe de plan, non d'une relecture — l'écart est mesuré et déclaré, non corrigé en silence.* ⚠ **Régime « source rédigée non publiable »** (PRD §7.2) : **G-4 non close, aucun vote adversarial conduit**. **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | ⚠ **Règle de comptage, décision 16 du TOC** : les cardinaux ci-dessous portent sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — de la première section à la synthèse, **en-tête et note de statut exclus** —, et ils sont **re-mesurés sur le corpus que le commit produit**. ⚠ **Un garde-fou appliqué sans que son identifiant soit écrit voit son DOMAINE déclaré, sans cardinal** (alinéa c) : *le domaine balayé est le corps entier, et les cardinaux antérieurs — qui comptaient les **applications** et non le marqueur — n'étaient re-mesurables par aucune règle écrite.* **Les deux séries sont balayées intégralement, zéros compris.** Vol. III — **R-14 (trois degrés d'absence) : quatre occurrences**, § 38.0, § 38.1, § 38.2 et § 38.4 ; **R-09 (statut pré-normatif dit à chaque mention) : deux occurrences**, § 38.3 et § 38.5 ; **R-01 : une occurrence**, § 38.5 ; **R-02 : une occurrence**, § 38.5 ; **R-03 (« AgentOps » terme de fournisseur) : une occurrence**, § 38.0 ; **R-04 : une occurrence**, § 38.1 (homonymie du sigle « APM », héritée et déclarée) ; **R-06 (« attendu par E-23 », jamais « exigé ») : une occurrence**, § 38.4 ; **R-07 (inférence produit ↔ réglementation) : une occurrence**, § 38.4, ⚠ **avec ses deux régimes d'absence distincts, qui ne s'échangent pas**. **R-05, R-08, R-10 à R-13 : zéro occurrence.** Vol. II — **R-7 (instrumentation d'une attente réglementaire par un produit = inférence d'auteur) : une occurrence**, § 38.4, ⚠ **nommé par volume, à ne pas confondre avec R-07 du Vol. III** ; **R-8 (sigle jamais nu) : une occurrence**, § 38.1, **renvoyée au siège du ch. 7 § 7.5** — ⚠ *l'en-tête antérieur la comptait à zéro* ; **métriques et conformités auto-déclarées (marqueur « auto-déclaré ») : une occurrence**, § 38.2, attribuée à son éditeur nommé. **R-1 à R-6 : zéro occurrence.** ⚠ **Faux ami déclaré** : le sigle « APM » sert à **deux objets sans rapport** dans le Vol. III — la supervision des performances applicatives et un manifeste de recherche homonyme ; le syntagme complet est écrit à chaque emploi, jamais le sigle nu |
| **Volumétrie cible** | ≈ **6 000 mots** de corps (§ 38.0 à la synthèse), **cible dérivée** de l'enveloppe du Livre (**69 000 mots**, TOC v0.25) au prorata des cinq sections et du volume de source consommé. ☑ **Décompte publiable depuis G-2** ; **réel reporté au [`README.md`](README.md)** du Livre, mesuré par [`PRD/decompte.sh`](../PRD/decompte.sh). ⚠ **D-4 s'applique** : l'écart se documente, **ni amputation ni gonflement** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) **v0.28**, entrée du chapitre 38 — **thèse réalignée en v0.28**, décisions 8 et 14, remontée R-IV-42)* — l'observabilité agentique dispose d'un **candidat à la standardisation** — les conventions sémantiques GenAI et agents d'OpenTelemetry —, ⚠ **mais leur état interdit de parler d'un socle acquis** : premier des **cinq** échelons de maturité, **aucune version citable**, rupture de dépôt datée. Tracer un *appel* n'est pas tracer une *délégation* : la corrélation trace ↔ chaîne de mandat est le chaînon manquant. ⚠ **« L'AgentOps commence par l'observabilité » est un ordonnancement d'auteur, non un fait** — *aucune entrée n'établit d'ordre entre les capacités d'exploitation.*

⚠ **La thèse portait, à la rédaction, deux formes que sa source avait elle-même bornées — le
réalignement est FAIT, et l'histoire de l'écart se conserve** (décision 17 du TOC, alinéa c). **Forme
antérieure, v0.25** : « l'AgentOps commence par l'observabilité, **dont le socle de standardisation
est** les conventions sémantiques GenAI/agents d'OpenTelemetry ». *Premièrement*, « **dont le socle de
standardisation est** » : le Vol. III avait reformulé sa thèse le 21 juillet 2026 et écrit exactement
l'inverse — **« leur état interdit de parler d'un socle acquis »**, les deux fichiers agentiques
relevés étant au **premier des cinq échelons** de maturité et **aucune version ne leur étant
citable**. *Deuxièmement*, « **l'AgentOps commence par l'observabilité** » était déclaré par la source
elle-même comme **un ordonnancement d'auteur, non un fait** : aucune entrée n'établit un ordre entre
les capacités d'exploitation. **Le corps a été écrit sous la forme bornée** et l'écart avait été
**remonté** (R-IV-42, § 38.6). ☑ **La remontée est soldée par l'arbitrage v0.28 du TOC** (décisions 8
et 14), et **la citation ci-dessus porte la forme réalignée**, reportée **par copie** depuis l'entrée
courante du plan — ☑ **re-collationnée caractère par caractère contre le TOC v0.30, identique**.
*Ni la v0.29 ni la v0.30 ne modifient une thèse du Livre : la v0.30 déclare 50 chapitres, cinq
livres, enveloppes, thèses et tables détaillées **strictement inchangés**, et n'enregistre au plan
que le franchissement de G-3.*

⚠ **Un second désalignement porte sur la ligne de sections du plan, et il est de fait daté** — voir
§ 38.2.1 et la remontée **R-IV-43**.

---

## § 38.0 — Introduction : ce que « voir » veut dire quand l'observé est un mandataire

Le ch. 37 s'est arrêté sur un constat qu'il ne pouvait pas dépasser : un dispositif que toute
interaction traverse est **structurellement un producteur de trace non délégué à l'observé** —
propriété d'emplacement, non de qualité —, et **la clé qui rattacherait cette trace au mandat
autorisant l'action tracée manque**. Ce chapitre reprend le dossier à cet endroit exact.

**Le mouvement *exploiter* distingue trois capacités, et celui-ci en traite une seule.** Voir
(ch. 38) ; boucler — évaluer, détecter la dérive, répondre à l'incident (ch. 39) ; mesurer un parc
(ch. 40). ⚠ **La frontière avec le ch. 40 passe entre l'instrument et l'indicateur** : ce chapitre
décrit ce que les conventions d'instrumentation **nomment et rattachent** — segments (*spans*),
attributs, événements ; le ch. 40 examine **ce qu'elles comptent et ce qu'elles ne comptent pas**.

**Le terme qui nomme la discipline est un terme de fournisseur, et il se pose ici à son siège
hérité.** Le Vol. III écrit qu'« AgentOps » n'a **pas de définition normative à date** (R-03 du
Vol. III) et l'emploie au sens de : *la discipline d'exploitation qui maintient vérifiable, dans la
durée, l'identité et le mandat d'un parc d'agents — par ce qu'elle observe, par ce qu'elle consigne
et par le signal de revalidation qu'elle renvoie à l'émetteur.* **La somme reprend cette définition
et ne la redéfinit pas.** ⚠ **Le statut du terme est posé par décision de cadrage, non par un
relevé** : **aucun balayage n'a porté sur son emploi commercial**, et **le socle ne documente aucun
homonyme commercial d'« AgentOps »** — absence de documentation, non fait négatif vérifié (R-14 du
Vol. III, degré 3). *L'ouvrage emploie le terme au sens de la discipline et le déclare ; il n'affirme
pas qu'un produit du même nom existe.*

⚠ **Ce que le chapitre ne traite pas, dit ici pour qu'on ne le prenne pas pour un oubli.** Le **coût
par jeton** n'y entre pas : le test d'appartenance ne le retient à aucun titre, et le FinOps agentique
est au **ch. 40 § 40.6**. L'**horizon de tâche déléguée** n'y entre pas : il est au **ch. 40 § 40.3**,
en partage déclaré avec le **ch. 49**. Le **non-déterminisme** n'y entre pas : il ne répond ni à ce
qu'il vérifie de l'identité ou du mandat, ni à ce qu'il en produit comme preuve opposable, et **aucune
entrée ne le caractérise**. Les **fondements de l'évaluation** ne sont pas ici : ils restent au
**ch. 6**, et le Vol. I *Monographie* §2.9 n'est pas repris par ce chapitre — **seul son §2.9.6 y
arrive, en seule affectation**.

**Le chapitre se lit en cinq temps.** D'où vient la filiation et où l'agent la déborde (§ 38.1) ; ce
que le corpus d'instrumentation est réellement, à sa date (§ 38.2) ; ce qui traverse une frontière
d'agents (§ 38.3) ; quand la trace devient pièce (§ 38.4) ; et pourquoi la corrélation manque
(§ 38.5).

## § 38.1 — De l'APM à l'AgentOps : ce que l'observabilité classique couvre et où l'agent la déborde

### 38.1.1 Une homonymie à poser avant toute filiation

⚠ **Le sigle « APM » sert à deux objets sans rapport dans le Vol. III, et la somme hérite de
l'homonymie.** Le cadrage en fait le point de départ de la filiation de l'AgentOps — « de l'APM à
l'AgentOps » —, où il désigne la **supervision des performances applicatives** (*application
performance monitoring*). Le même sigle nomme, au socle hérité, un **manifeste de recherche**
homonyme dont le siège est aux **ch. 22** et **ch. 39** (Vol. III **H-11**, **[B]**).

⚠ **Le socle ne documente le développé d'aucun des deux sigles** : absence de documentation, non
fait négatif vérifié (R-14 du Vol. III, degré 3). La lecture retenue — que le premier désigne la
supervision des performances applicatives — est une **lecture de l'auteur**, et **le syntagme
complet s'écrit à chaque emploi plutôt que le sigle nu**. C'est la discipline que R-04 du Vol. III
applique à « ACP » et que R-8 du Vol. II applique au plan de contrôle, dont le siège est au **ch. 7
§ 7.5**. ⚠ **Aucun garde-fou nouveau n'est créé** — la somme applique les deux séries héritées et
**n'en ouvre pas de troisième** (PRD §8).

### 38.1.2 Ce que la supervision des performances applicatives couvre

**Le socle du Vol. III n'en porte aucune définition, aucun historique et aucune capacité** : absence
de documentation, non fait négatif vérifié (degré 3). **La filiation posée est donc un choix de
cadrage, pas un résultat d'instruction**, et ce chapitre ne s'autorise d'elle **aucune propriété
transférée**.

⚠ **Le compendium hérite pourtant, ici encore, d'une couverture que le Vol. III n'avait pas — et
elle ne comble rien.** Le **ch. 3 § 3.4.5** pose le socle pré-agentique du traçage réparti — norme
W3C de contexte de trace, cadre d'instrumentation, conventions sémantiques —, et le Vol. I
*Monographie* décrit en §2.9.6 la boucle *production → jeux d'évaluation → amélioration →
production* qui transforme l'évaluation d'un audit ponctuel en processus continu. ⚠ **C'est une
lacune de couverture couverte, non comblée** : le Vol. I entre en **[C]** — sa vérification porte
sur ses références, non sur le contenu de ses affirmations —, et *une entrée [C] ne porte jamais un
fait central.* Les deux énoncés — « le socle du Vol. III ne documente pas la supervision des
performances applicatives » et « le Vol. I la décrit » — sont **logiquement compatibles**, et
l'énoncé du Vol. III **reste exact dans son périmètre**.

Ce que le chapitre peut établir se trouve du côté de l'instrument : les conventions sémantiques
ouvertes par le Vol. III déclarent **sept attributs d'outil** au premier échelon de maturité
(Vol. III **F-77**, **[B]**), et rattachent l'exécution d'un outil à un segment dont la **forme
prescrite** est `execute_tool {gen_ai.tool.name}` — *relevé hors socle, cité comme tel*. ⚠ **Le verbe
prescriptif de la spécification est « SHOULD », non « MUST »** : le nom de segment est **recommandé,
non imposé**, et la borne ne se détache pas de l'énoncé.

### 38.1.3 Où l'agent déborde, et le débordement qui appartient à la somme

**L'unité que l'instrument sait nommer est une opération** : une invocation, un appel d'outil, une
session. L'entrée la plus explicite du socle sur ce point est bornée à trois fichiers et vaut d'être
citée **pour sa lettre plutôt que pour sa portée** : la métrique de durée d'invocation d'agent mesure
« a single **in-process** agent invocation » (Vol. III **F-91**, **[B]** ; siège **ch. 40 § 40.1**).
⚠ **Une invocation en processus n'est ni une délégation, ni une chaîne de mandat, ni un parc.**

**L'entreprise, elle, n'a pas de question sur l'invocation : elle a une question sur le mandataire.**
Savoir qu'un appel a duré trois secondes ne dit ni qui l'a émis, ni pour le compte de qui, ni sous
quelle borne de privilège — c'est-à-dire ni **Q-A** (« qui es-tu ? »), ni **Q-B** (« qui t'a
créé ? »), ni **Q-C** (« pour qui agis-tu ? », qui exige une chaîne de mandat **interrogeable à
l'instant *t***), ni **Q-D** (« que peux-tu faire ? », qui exige des bornes **opposables au point
d'application**). *La grille du ch. 14 s'applique ici en lecture inversée : elle ne rend pas un
verdict, elle nomme ce que l'instrument ne peut pas produire.*

Lecture de l'auteur — **ce que le socle établit** : sept attributs d'outil au premier échelon (F-77,
**[B]**) ; le grain déclaré d'une métrique d'invocation, **borné à l'exécution en processus** (F-91,
**[B]**). **Ce qu'il n'établit pas** : ce que couvre la supervision des performances applicatives,
ni qu'une discipline nommée « AgentOps » existe comme catégorie constituée, ni qu'elle procède de
celle-là. La lecture proposée est que **le débordement qui appartient à la somme n'est ni celui du
volume ni celui du non-déterminisme, mais celui du sujet** : *l'instrument nomme une opération,
l'entreprise doit répondre d'un mandataire, et la distance entre les deux est exactement ce que les
§ 38.2 à § 38.5 mesurent.* ⚠ **Le lecteur peut refuser cette lecture sans qu'aucun des faits cités
ne tombe.**

## § 38.2 — État des conventions sémantiques OpenTelemetry pour l'IA générative et les agents

### 38.2.1 La première chose à écrire est ce qu'on ne peut pas écrire

**La formule « conventions OpenTelemetry version X du [date] » est inécrivable**, et elle l'est pour
une raison précise : **il n'y a pas de version à citer**. Les conventions sémantiques (*semantic
conventions*) pour l'IA générative ont quitté le dépôt principal pour un **dépôt dédié**, par une
**rupture déclarée dans la version v1.42.0 du 12 juin 2026** (Vol. III **F-74**, **[B]**). Ce dépôt
dédié ne porte, au 21 juillet 2026, **ni publication ni étiquette**, et la section « Schema URL » de
son fichier de présentation ne contient que le mot « TODO » : **aucun numéro de version qui lui soit
propre n'est citable** (Vol. III **F-75**, **[B, degré 2]** — **fait négatif ÉTABLI**, fondé sur
l'interrogation des ressources d'énumération du dépôt et sur la lecture intégrale de son fichier de
présentation, **non sur un balayage exhaustif du projet**).

⚠ **Cette absence ne s'étend pas au-delà de sa borne** : elle n'établit pas que le projet n'ait aucun
mécanisme de versionnage ailleurs — une numérotation par instantané, une URL de schéma générée à la
construction ou les millésimes du dépôt principal dont il dépend demeurent possibles et **n'ont pas
été balayés**.

**La seule forme fidèle est donc descriptive** : *les conventions sémantiques GenAI d'OpenTelemetry,
telles que portées par leur dépôt dédié au 21 juillet 2026, à l'état* Development *et sans version
publiée*. Les deux seules ancres temporelles disponibles sont **la date de consultation** et **celle
de la rupture qui a créé le dépôt**.

⚠ **Le plan du compendium porte ici une forme et une ancre que le socle du Vol. III réfute, et le
désalignement est remonté plutôt que corrigé.** La ligne de sections du TOC annonce pour cette
section un « statut exact des conventions — **stable/expérimental** — à dater au gel », **alternative
binaire que F-76 réfute** (voir § 38.2.2) ; et sa datation v0.7 ancre les conventions sur un millésime
d'**avril 2026** du dépôt principal, **antérieur de deux mois à la rupture du 12 juin 2026** qui les
en a sorties. *Une ancre de version antérieure au déplacement qui l'a périmée relève exactement de la
classe de défaut que le § 38.2.3 documente chez un éditeur.* Remontée **R-IV-43**.

### 38.2.2 L'échelle de maturité, et il faut la nommer

L'échelle applicable **aux groupes de conventions sémantiques** compte **cinq échelons** —
`development`, `alpha`, `beta`, `release_candidate`, `stable` —, le niveau `development` étant présumé
en l'absence de déclaration (Vol. III **F-76**, **[B]**).

⚠ **Nommer l'échelle n'est pas une précaution de style** : une **seconde échelle, distincte**,
s'applique aux signaux des bibliothèques clientes, et c'est vraisemblablement d'elle que venait
l'échelle à trois échelons qu'une revalidation antérieure du Vol. III avait portée — elle-même
corrective d'une alternative binaire déjà fausse. *Une correction non vérifiée à la source n'est
qu'une seconde erreur*, et le Vol. III s'est trompé **deux fois** sur cette échelle avant de la lire.
**La somme écrit l'échelle réelle et déclare l'écart avec son propre plan.**

### 38.2.3 Le statut relevé, et son périmètre

Deux fichiers agentiques du dépôt dédié ont été ouverts et affichent en tête « **Status**:
[Development] » ; les **quatre attributs d'agent**, les **deux de conversation**, les **sept d'outil**
et les **quatre d'évaluation** relevés portent tous `stability: development` (Vol. III **F-77**,
**[B]**).

⚠ **Deux marquages sont distincts et ne se fusionnent pas** : le statut « Development » d'un
**document** et la valeur `stability: development` d'un **attribut**. ⚠ **Et les deux relevés ne
portent pas sur les mêmes fichiers** : le statut de document est relevé sur les deux documents
ouverts, les attributs sont déclarés au registre et dans les documents de segments et d'événements.
⚠ **Le relevé de statut porte sur ces deux fichiers et ne documente pas le statut des autres documents
du dépôt.**

Deux autres documents portent le même statut de document, et le socle les nomme : un document de
métriques, qui en définit **douze** (Vol. III **F-90**, **[B]**), et un document de jonction ouvert
**sur sa seule section de métriques** (Vol. III **F-95**, **[B, degré 1]**) — *celui-là même dont le
§ 38.5 établit que le volet de corrélation n'a pas été instruit.*

⚠ **Le cardinal du répertoire est hors socle et se cite comme tel** : le répertoire compte **onze
fichiers**, dont **six ont été ouverts au moins en partie et cinq ne l'ont pas été** — *relevé porté
par le rapport de lot, non versé au socle*. **Aucun constat ne vaut pour les cinq fichiers non
ouverts.**

| Ce que le socle établit du corpus, au 21 juillet 2026 | Entrée (Vol. III) | Borne portée par l'entrée |
|---|---|---|
| Déplacement vers un dépôt dédié, **rupture déclarée en v1.42.0 du 12 juin 2026** | **F-74**, [B] | — |
| **Aucune publication, aucune étiquette**, « Schema URL » à « TODO » | **F-75**, [B, degré 2] | deux ressources et cette date ; **n'établit pas** l'absence de tout versionnage ailleurs |
| Échelle **des groupes de conventions** : **cinq échelons**, `development` présumé par défaut | **F-76**, [B] | une **seconde échelle, distincte**, régit les signaux des bibliothèques clientes |
| Deux fichiers agentiques au statut de document *Development* ; attributs d'agent, de conversation, d'outil et d'évaluation en `stability: development` | **F-77**, [B] | **ces deux fichiers seuls** ; statut de document ≠ stabilité d'attribut |
| Un troisième document au même statut, **douze métriques** relevées | **F-90**, [B] | ce fichier seul |
| Un quatrième document au même statut, ouvert **sur ses seules métriques** | **F-95**, [B, degré 1] | volet de corrélation **non instruit** (§ 38.5) |
| Une **conformité annoncée** pointant un millésime que le dépôt nommé **n'a jamais émis** | **F-78**, [B] — ⚠ **☑ changée au 28 juill. 2026** | **un éditeur, une page, cette date** — aucune généralisation ; *la qualification d'origine, « millésime du dépôt principal », est tombée* |

: Tableau 38.1 — État daté des conventions sémantiques d'OpenTelemetry pour l'IA générative et les agents, tel que le socle du Vol. III le porte au 21 juillet 2026 — et, à la dernière ligne, tel que l'instruction du 28 juillet 2026 l'a re-daté.

**Ce que devient « conforme aux conventions OpenTelemetry » dans ces conditions.** **Une conformité
annoncée peut pointer un millésime que le dépôt qu'elle nomme n'a jamais émis.** Au relevé du
21 juillet 2026, la documentation produit d'un éditeur nommé — **Datadog** — énonçait sa conformité
par référence à un millésime du **dépôt principal publié le 25 août 2025**, soit **antérieur au
déplacement du 12 juin 2026** (Vol. III **F-78**, **[B]**). ⚠ **L'instruction du 28 juillet 2026 a
rouvert cette page, et la qualification est tombée** : le syntagme de conformité y est **identique
au mot près**, mais **son ancre pointe le dépôt dédié**, où **le dépôt principal n'apparaît en lien
nulle part** ([`socle-consolide.md`](../PRD/socle-consolide.md), entrée `S-124`, **☑ changée**). ⚠
**La date de ce changement n'est pas établie** — la page ne porte aucune date de révision
exploitable, et *rien n'exclut que l'ancre pointât déjà le dépôt dédié au relevé d'origine.* ⚠ **Le
fait que la qualification servait ne tombe pas avec elle : il se durcit.** Le millésime annoncé
désigne désormais le dépôt dont le Vol. III établit, en **F-75**, qu'il **ne porte ni publication ni
étiquette** — *la conformité annoncée ne pointe plus un millésime périmé, elle pointe un numéro que
le dépôt nommé n'a jamais émis.* ⚠ **La donnée est auto-déclarée** par cet éditeur, à sa page et à
sa date, et **n'a fait l'objet d'aucune vérification indépendante**. La même page prescrit une
variable d'environnement dont l'intitulé qualifie ces conventions d'**expérimentales** — *indice de
vocabulaire, non de statut*. ⚠ **Ce constat est borné à un éditeur** : il fournit **une occurrence,
pas une mesure**, et ne soutient **aucun énoncé sur une discontinuité générale** entre le dépôt
dédié et les implémentations.

⚠ **Le Vol. I porte de son côté une conséquence d'ingénierie, en [C], et elle recoupe ce constat sans
l'établir** : un déploiement prudent **active explicitement l'option de stabilité sémantique et
anticipe des ruptures de schéma**, et le patron de mise en œuvre fait converger **deux couches
distinctes vers un seul collecteur** — l'observabilité spécialisée des appels de modèle et
l'infrastructure de supervision générale — *de manière à corréler une dérive de comportement avec une
saturation de ressource*. **Le critère d'architecture qu'il pose est l'unification** : *un agent
d'entreprise ne doit pas créer un silo d'observabilité parallèle.* ⚠ **Repérage [C], non fait
central** : la somme le cite comme thèse d'un volume antérieur, à attribuer.

Lecture de l'auteur — **ce que le socle établit** : une date de rupture ; une absence de version
citable **bornée à deux ressources** ; une échelle nommée à cinq échelons ; un statut de document
relevé sur **quatre fichiers**, dont deux nommés ; un cas d'éditeur pointant un millésime que le
dépôt qu'il nomme n'a pas émis. **Ce qu'il n'établit pas** : **que ces conventions soient le seul
candidat existant** — aucun balayage de candidats concurrents n'a été conduit, et *une exclusivité
posée sur un corpus non balayé est la forme même que R-14 du Vol. III proscrit* —, ni qu'elles
progresseront sur leur échelle, ni ce que portent les cinq fichiers non ouverts. La lecture proposée
est que **le premier échelon d'une échelle de cinq, sans version publiée, est un objet qu'on cite par
sa date de consultation et non par son numéro** — et que **toute architecture d'observabilité qui s'y
adosse hérite de cette volatilité**. ⚠ Le passage de ces conventions à un échelon supérieur est
**SPÉCULATIF** : **aucun jalon daté n'est relevé**, et
aucune date d'aboutissement n'est écrite ici sous aucun des trois tris.

## § 38.3 — Propagation de trace à travers les frontières d'agents

*← Vol. I* Monographie *§3.12.3 — **arrivée**, prélevée au ch. 9, qui garde le reste du §3.12 et
déclare la sortie à son bout. Le socle pré-agentique du traçage réparti reste au **ch. 3 § 3.4.5** et
n'est pas reconstruit ici.*

⚠ **Cette section entre en [C] de bout en bout**, et c'est la seule du chapitre dans ce cas : sa
matière vient **entièrement** du Vol. I, dont le socle du Vol. III ne porte aucun équivalent. *Aucun
énoncé n'y est central, et aucun ne le deviendra sans lecture de la source primaire que le Vol. I
cite.*

**Le seul fait propre à l'interopérabilité est la propagation du contexte de trace à travers la
frontière protocolaire.** Lorsqu'un agent client délègue une tâche à un serveur d'outils ou à un agent
distant, **la continuité de la trace ne survit que si le contexte de traçage traverse l'appel** : le
segment du serveur s'imbrique alors sous celui du client, et **la chaîne d'exécution reste
reconstituable de bout en bout malgré le franchissement d'une frontière organisationnelle**. La norme
de contexte de trace du W3C fournit le mécanisme — un en-tête véhicule l'identité de trace d'un saut à
l'autre —, ⚠ **son niveau 2 étant à un stade de recommandation candidate, la version stable demeurant
le niveau 1** (statut dit à la mention, R-09 du Vol. III).

**La difficulté propre à l'agentique tient à l'asynchronie.** Les tâches confiées à des processus de
traitement et les tâches différées rompent **la corrélation parent-enfant synchrone**, ce qui impose
de **propager puis de raviver le contexte de trace au moment où un résultat différé est récupéré** —
faute de quoi le segment asynchrone **se détache de sa trace d'origine**.

⚠ **Et la reconstruction inter-organisationnelle se heurte à une contrainte que l'ingénierie ne
tranche pas.** Lorsque des segments transitent par des **juridictions différentes**, l'unicité de la
trace devient **une contrainte d'architecture, et non un simple réglage** — la résidence des données
est traitée au **Livre III**, et ce chapitre ne fait que nommer le point de collision.

Lecture de l'auteur — **ce que le socle établit** : rien qui vienne du socle consolidé, auquel cette
pièce n'est pas adossée ; ce que la somme mobilise ici est un **repérage [C] du Vol. I**, à
attribuer. **Ce qu'il n'établit pas** : que la propagation du contexte de trace transporte **quoi que
ce soit du mandat** sous lequel l'appel est fait — ⚠ *c'est exactement la question que le § 38.5 pose
et ne referme pas, et il faut noter qu'elle se pose ici **une première fois**, sur un mécanisme dont
le Vol. I documente le fonctionnement sans documenter son contenu sémantique.* La lecture proposée
est que **la propagation résout la continuité et non l'imputation** : *une trace recollée de bout en bout établit
qu'un même fil d'exécution a traversé n sauts, jamais sous quelle autorité il les a traversés.*

## § 38.4 — La journalisation probatoire : quand la trace devient pièce de conformité

**Une trace d'exécution est produite pour diagnostiquer. Une pièce de conformité est produite pour
être opposée.** Le passage de l'une à l'autre n'est pas un changement de format : c'est **un
changement de régime de production**, et le socle en documente exactement un aspect.

### 38.4.1 Qui produit la trace

Le cadre empirique hérité enseigne que **la journalisation confiée aux agents « n'est généralement
pas recommandée »** (Vol. III **H-12**, **[B]**) — *reprise en substance, non verbatim revendiqué*.
⚠ **Trois réserves voyagent avec cette entrée et ne s'en détachent pas** : **source unique**,
**préimpression non révisée par les pairs**, **sans reproduction indépendante**. Le même cadre
relève par ailleurs que, de ses cinq propriétés d'évaluation, **quatre reçoivent une instrumentation
et l'autonomie n'en reçoit aucune** — *constat d'une préimpression, non propriété établie du
domaine.*

Le Vol. II en tire, **sous marquage d'auteur**, le point de contrôle par lequel **la trace d'instance
est produite par le cadre** et non par l'agent — l'un des cinq **points de contrôle obligatoires**
dont **le siège est au ch. 43 § 43.3** (Vol. III **H-15**, construction d'auteur du Vol. II, **sans
niveau ni identifiant de fait**). ⚠ **Ce ne sont pas des faits de socle** : les cinq portent le
marquage « Lecture de l'auteur » dans leur volume d'origine et entrent ici comme **thèses d'un volume
antérieur, à attribuer**, jamais comme acquis. ⚠ **Collision terminologique héritée, signalée et non
résolue** : le glossaire du Vol. II réserve « point de contrôle » à la traduction de *checkpointing*,
où « point de contrôle obligatoire » désigne autre chose.

Lecture de l'auteur — la somme en fait un **principe absolu** — *la trace revient au cadre, jamais à
l'agent* — et **la forme absolue est une décision d'architecture, non la reprise d'une recommandation
graduée d'une préimpression**. ⚠ **La distinction n'est pas rhétorique : elle décide de ce qu'une
institution peut inscrire à son dossier.**

### 38.4.2 Ce que la trace devrait porter pour valoir pièce, et ce que le socle en dit

**La ligne directrice E-23 du BSIF est fondée sur des principes.** Ses **douze énoncés numérotés sont
au *should*** — balayage du corps de la version anglaise en rendu HTML, **sans occurrence de *must*,
*OSFI expects* ni *we expect*** (Vol. III **F-64**, **[B, degré 1]**). ⚠ **Deux bornes** : l'Appendice
n'a pas été extrait, et le volet français n'a pas été balayé par ce lot. **On écrit donc
« attendu par E-23 », « les attentes d'E-23 », jamais « exigé par E-23 » ni « E-23 impose »** (R-06 du
Vol. III, dont le siège est au **ch. 25**).

⚠ **Et la forme porte sa propre condition, que le socle attache à cette formulation même** : le modal
est celui du texte (F-64), de sorte qu'écrire « E-23 attend » n'est admissible **qu'au titre du
document d'information de l'éditeur** — celui du **11 septembre 2025**, dont le socle constate qu'il
porte une formule **absente du corps de la ligne directrice** en rendu HTML anglais (Vol. III
**F-66**, **[B, degré 1]**). La ligne directrice, elle, **énonce ce que l'institution *devrait*
faire** (Vol. III **F-65**, **[B]**).

**Ce que ce texte énonce touche directement la matière de ce chapitre** : une **surveillance
continue** visant nommément la prise de décision autonome et la re-paramétrisation autonome, et une
**documentation de modèle** — ⚠ **jamais « fiche de modèle » : zéro occurrence dans les deux langues**
(Vol. III **H-04**, **[A/B mixte]** ; **F-65**, **[B]**).

**Et ici s'arrête ce que le socle autorise.** ⚠ **Le socle ne documente pas que la ligne directrice
E-23, que la ligne directrice de l'AMF sur l'utilisation de l'intelligence artificielle ou que l'un
quelconque des autres cadres canadiens instruits par le Livre III prescrivent une trace d'exécution,
un journal, une durée de conservation ou un format de restitution** : absence de documentation, non
fait négatif vérifié (R-14 du Vol. III, degré 3).

**Un troisième texte est plus exigeant sur le contenu, et sans ambiguïté de modalité.**
L'**article 12.1** de la loi québécoise sur la protection des renseignements personnels dans le
secteur privé **impose** à qui rend une décision « fondée exclusivement sur un traitement
automatisé » d'en informer la personne concernée, puis, **à sa demande**, de l'informer de trois
choses — les renseignements personnels utilisés, « des raisons, ainsi que des principaux facteurs et
paramètres, ayant mené à la décision », et son droit de faire rectifier ces renseignements ; s'y
ajoute, **dans un alinéa distinct**, l'occasion de présenter ses observations à un membre du personnel
**en mesure de réviser la décision** (Vol. III **F-89**, **[B]** ; **H-06**, **[B]** ; siège
**ch. 27**).

⚠ **Restituer des facteurs et des paramètres suppose de les avoir consignés au moment de la décision,
et de savoir laquelle.** *C'est le point où une trace cesse d'être un instrument de diagnostic.*
⚠ **Et la forme imposée tient** : le dispositif **outille un point d'arrêt humain**, **jamais la
révision de l'article 12.1** — le **ch. 45 § 45.11** le reprend à l'identique pour son premier flux.

### 38.4.3 Ce que le Vol. I ajoute, en [C], et ce qu'il n'ajoute pas

Le Vol. I pose de son côté un **critère d'architecture** pour la journalisation probatoire :
**l'infalsifiabilité** — journaux en mode ajout seul, **chaînage cryptographique reliant chaque entrée
à la précédente**, horodatage fiable, conservation alignée sur des normes reconnues —, et rappelle
qu'au-delà de la conformité **ces propriétés conditionnent l'admissibilité en preuve**, la piste
d'audit devenant l'élément central d'un litige et devant pouvoir faire l'objet d'un gel de pièces.
⚠ **Le Vol. I y ajoute la condition qui décide de tout** : *sans attribution fiable, un journal
infalsifiable ne prouve qu'une séquence anonyme d'actions* — l'attribution exacte d'une action à
l'agent qui l'a posée, et au mandant humain dont il tient son autorité, **repose sur l'identité non
humaine et la chaîne de délégation**.

⚠ **Repérage [C], et la conséquence est double.** *Un* : **aucun de ces critères n'est central au sens
de CA-IV-01**, et leur élévation en [B] passerait par la lecture des sources primaires que le Vol. I
cite — travail de **G-1**, non de ce chapitre. *Deux* : **c'est une couverture partielle d'une relève
du plan, et il faut écrire laquelle.** Le TOC porte pour cette section une **relève v0.10** —
une préimpression adverse posant que **la propriété porteuse d'un environnement d'exécution agentique
n'est pas la richesse de la trace mais la détection de la divergence entre l'action effectuée et son
enregistrement d'audit**, et proposant le **journal chaîné par empreintes** comme parade. ⚠ **Le
Vol. I documente la parade, en [C] ; il ne documente pas la thèse.** *Une parade décrite ne vaut pas
la propriété qu'on lui prête*, et la relève **reste un repérage [C] à instruire à la source
primaire** — elle n'entre pas au socle, et son instruction relève de G-1. ⚠ **Le versant *effet* est
au ch. 48**, ⚠ *rédigé depuis, par une passe concurrente du même jour, et **hors portes comme celle-ci** : le renvoi résout contre du texte, non contre une pièce recevable.*

### 38.4.4 Le garde-fou, et le socle y est dissymétrique — ne pas généraliser

**Le rapprochement entre un outil d'observabilité et une attente réglementaire est une inférence
d'auteur** (R-07 du Vol. III ; ⚠ **et R-7 du Vol. II pour l'instrumentation d'E-23 par un produit de
gouvernance nommé — deux garde-fous distincts sur le même geste, nommés par volume, dont la confusion
était précisément indécidable au renvoi nu**). **Sans exception d'usage illustratif.**

Le socle porte **deux produits du même éditeur et deux régimes d'absence différents** (Vol. III
**H-14**, **[B]**), ⚠ **et les deux formules ne s'échangent pas**.

| Produit nommé | Régime d'absence | Ce que cela veut dire exactement |
|---|---|---|
| Un produit de **gouvernance de modèles** | **fait négatif ÉTABLI, degré 2** | **l'éditeur ne revendique aucune conformité**, et aucune source ne documente le lien avec E-23 — *on a cherché, et on a consigné une réserve* |
| Un produit d'**observabilité d'agents et de modèles**, **en préversion publique** (statut dit à la mention) | **absence de documentation, degré 3** | **le socle est muet** sur E-23 pour ce produit — *on n'a rien* |

: Tableau 38.2 — Les deux régimes d'absence portés par le socle du Vol. III sur le lien entre outil d'observabilité et attente réglementaire. ⚠ **L'un ne se déduit pas de l'autre**, et aucun ne se généralise au-delà du produit qu'il nomme.

⚠ **Les deux produits sont nommés dans leur volume source**, où ils sont des **cas d'instanciation
documentés, jamais des recommandations** ; la somme les désigne ici par leur fonction, **parade de
péremption que la décision 15 du TOC maintient pour les dénominations commerciales** — ⚠ *la
réserve, elle, reste attachée à l'objet que la source nomme et ne se généralise à rien.* La somme
reprend le régime et **ne recommande pas davantage**.

⚠ **Le statut de préversion, lui, n'a pas pu être re-constaté.** L'instruction du 28 juillet 2026 a
porté cette entrée à sa source et **l'hôte de l'éditeur a refusé l'accès** : rien n'a été rouvert,
pas même le statut annoncé de l'offre d'observabilité (`S-042`, **☐ non établie**). *L'entrée n'est
pas infirmée : elle est non re-datée, ce qui est un état et non un doute* — et **les deux régimes
d'absence du tableau ci-dessus n'en dépendent pas et restent entiers**.

## § 38.5 — Corréler la trace au passeport : l'identité comme clé de jointure

⚠ **Le passeport d'agent ne figure dans aucune spécification à date : c'est un objet de synthèse
construit par la somme**, en assemblant la carte signée (**ch. 15**), l'inscription au registre
(**ch. 15 § 15.3**), la chaîne de mandat (**ch. 17**) et les attestations de conformité — R-01 du
Vol. III ; **siège ch. 16**. *Corréler une trace « au passeport » désigne donc une jonction entre un
objet observé et un objet construit*, et le chapitre l'écrit ainsi plutôt que de laisser croire à un
raccordement entre deux artefacts existants.

**Pourquoi cette section est décisive.** C'est **par elle que l'observabilité entre dans la somme** :
non par le panorama des plateformes, mais par la **corrélation trace ↔ chaîne de mandat**. Les
sections précédentes décrivent un instrument ; celle-ci demande **ce que l'instrument produit comme
preuve opposable** sur l'identité et le mandat d'un agent. **La réponse du socle est courte, et elle
se donne en trois constats bornés.**

**Premier constat — une clé existe comme attribut, sans que rien ne la rattache à un émetteur.** Le
registre d'attributs du dépôt dédié définit **quatre attributs d'agent** — dont un identifiant
d'agent — et **deux attributs de conversation**, tous en `stability: development` (Vol. III **F-77**,
**[B]** ; *l'identité nominative des attributs est portée par le rapport de lot et non versée au
socle*). ⚠ **Aucune entrée n'établit que cet identifiant soit celui d'un registre d'agents au sens du
ch. 15, ni qu'il soit émis, ni qu'il soit vérifiable** : le socle documente **un nom de champ dans un
fichier de modèle, à son premier échelon de maturité**. **Ce qu'un attribut d'identifiant démontre est
qu'un producteur de télémétrie peut renseigner une chaîne** ; il ne documente **ni son unicité à
l'échelle d'une organisation, ni son ancrage, ni sa révocation** (R-02 du Vol. III).

**Deuxième constat — l'interrogeabilité de la chaîne de mandat n'est établie ni par le socle ni par
les chapitres qui la portent, et ce n'est pas l'observabilité qui l'a perdue.** Le **ch. 17** le pose
sur les trois mécanismes du mandat : le socle n'établit pas qu'une chaîne ainsi formée soit
interrogeable à un instant quelconque, ni qu'un vérificateur situé au troisième maillon puisse
remonter au mandant d'origine, ni qu'un mandat révoqué en amont cesse d'être opposable en aval.
⚠ **C'est un non-établissement, non un fait négatif** : ces trois énoncés sont rangés sous « ce qu'il
n'établit pas », et **aucun balayage n'a été conduit qui permettrait de conclure à l'inverse**. Le
**ch. 16** les reprend à l'identique dans la même colonne de sa table des quatre pièces.

**Troisième constat — la pièce de jonction existe, elle est nommée, et elle n'a pas été ouverte sur ce
point.** Un document du dépôt dédié est désigné comme **la pièce de jonction** de cette section :
propagation de contexte par les en-têtes du § 38.3, portés dans un champ de métadonnées de la
requête. **Le lot d'instruction déclare ne pas l'avoir ouvert** et qualifie ce manque de **lacune la
plus coûteuse du lot** ; le lot complémentaire l'a ouvert **sur sa seule section de métriques** —
quatre métriques supplémentaires, toutes des histogrammes, statut de document *Development* — et
déclare que **son volet de corrélation demeure non instruit** (Vol. III **F-95**, **[B, degré 1]**).
⚠ **Rien n'est affirmé ici de ce que ce document prescrit ou omet.**

> **État de la recherche — la corrélation entre trace d'exécution et chaîne de mandat.** **Question**
> : par quel mécanisme un contexte de trace se propage-t-il à travers un appel d'agent, et ce
> mécanisme transporte-t-il quoi que ce soit du **mandat sous lequel l'appel est fait** ? **État** :
> lacune ouverte le 21 juillet 2026 chez sa source ; **aucune passe de recherche n'a été conduite** —
> le lot n'a pas ouvert le document, le lot complémentaire ne l'a ouvert que sur ses métriques.
> **Corpus à ouvrir** : le document `docs/gen-ai/mcp.md` du dépôt
> `open-telemetry/semantic-conventions-genai`, branche `main`, sur son volet de propagation de
> contexte — `traceparent`, `tracestate` et `baggage` dans le champ `_meta`. ⚠ **L'identifiant de la
> source est écrit** : *un critère de clôture qui désigne son corpus par sa fonction est
> inexécutable* (décision 15 du TOC, alinéa b-iii ; identité du fichier portée par le Vol. III
> *Monographie* §24.4, **hors socle**). **Critère de clôture** : que le volet soit extrait à la
> source primaire et que la présence ou l'absence d'un identifiant de chaîne de mandat exportable y
> soit constatée. ⚠ **La question reste ouverte ; aucune inférence n'est proposée ici.**

⚠ **Une seconde source s'est périmée pendant que cette lacune restait ouverte, et l'événement est
advenu au lendemain du gel.** La révision majeure de la spécification agent-outil — protocole sans
état, retrait de l'en-tête de session — était, au gel du 27 juillet 2026, **annoncée au brouillon**
pour le jour suivant, **sa date n'étant pas confirmée à la source** (R-09 du Vol. III) ; *aucun des
trois statuts du tri prospectif ne lui était alors attribuable, le **PROGRAMMÉ exigeant un
engagement daté réel*** (siège **ch. 49 § 49.0**). ☑ ⚠ **L'instruction du 28 juillet 2026 a constaté
à la source que la page de spécification courante sert cette révision et que l'index documentaire du
site ne connaît qu'elle** ([`gel-2026-07-28-volet-residuel.md`](../PRD/gel-2026-07-28-volet-residuel.md),
entrée `S-001`, **☑ changée**) : *la péremption annoncée est advenue, et un événement advenu ne se trie plus au
prospectif.* ⚠ **Ce qui a été constaté est la mise en service de la révision, non son contenu** —
*le protocole sans état et le retrait de l'en-tête de session n'ont pas été rouverts* —, et **la
revalidation en bloc des sections du ch. 8 qui portent cette matière reste ouverte, non exécutée**.
**Un mécanisme de corrélation adossé à une notion de session est, par construction, exposé à cette
révision** ; ⚠ **le socle ne documente pas son incidence sur la propagation de contexte** : absence
de documentation, non fait négatif vérifié.

Lecture de l'auteur — **et c'est la clôture du chapitre, marquée en totalité.** **Ce que le socle
établit** : quatre attributs d'agent et deux de conversation définis au premier échelon (F-77) ; un
document de jonction nommé, **ouvert sur ses seules métriques** (F-95). **Ce qu'il n'établit pas** :
que la chaîne de mandat soit interrogeable à l'instant *t* — **non-établissement**, jamais une absence
établie ; qu'une **clé de jointure** existe entre une trace et un mandat, ni qu'elle soit propagée, ni
qu'un vérificateur puisse la contrôler. La lecture proposée est que **l'identité serait la clé de
jointure de l'observabilité agentique, et que rien dans le corpus ouvert ne la constitue** : d'un côté
un identifiant d'agent **qui n'est rattaché à aucun émetteur**, de l'autre une chaîne de mandat **dont
l'interrogeabilité n'est établie par aucune entrée**. ⚠ **Le chaînon manquant n'est donc pas un
mécanisme qu'il faudrait mieux chercher : c'est une lacune ouverte, et le chapitre l'expose plutôt
qu'il ne la comble.** *L'exposer est le résultat ; la combler par inférence serait la faute que la
somme prend pour objet.*

## Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **La définition d'« AgentOps », et son statut de définition.** Terme de fournisseur, **sans
   définition normative**, repris du Vol. III à son siège. Les **ch. 39, 40 et 41** l'emploient sans
   le redéfinir. ⚠ *Et l'homonymie du sigle « APM » est posée ici une fois* : le syntagme complet
   s'écrit à chaque emploi, dans tout le Livre.
2. **L'état daté du corpus d'instrumentation, et la manière de le citer.** Premier échelon d'une
   échelle de **cinq**, **aucune version citable**, ancre unique = date de consultation. ⚠ **Le
   ch. 40 hérite de cet état pour les métriques qu'il dénombre**, et **le ch. 46** pour son inventaire
   de jalons externes — *aucun ne le redémontre.* ⚠ **Le cardinal se lit au ch. 40 § 40.1.2, qui le
   re-mesure : SEIZE** — douze au document de métriques (F-90), quatre au document de jonction (F-95),
   *que le § 38.5 mentionne lui-même* ; **il n'est pas cité ici sous sa valeur partielle.**
3. **La distinction instrument / indicateur.** Ce chapitre nomme et rattache ; **le ch. 40 compte**.
   La frontière est posée ici pour les deux.
4. **Le régime de la trace probatoire.** Producteur distinct de l'observé ; infalsifiabilité en [C] ;
   ⚠ **et la condition qui décide de tout — *sans attribution fiable, un journal infalsifiable ne
   prouve qu'une séquence anonyme d'actions*.** Le **ch. 45 § 45.10** le reprend à l'archivage
   probatoire ; le **ch. 39 § 39.3** à l'imputation d'incident.
5. **Les deux régimes d'absence sur le lien produit ↔ réglementation.** *Fait négatif établi* et
   *absence de documentation* **ne s'échangent pas**. Le **ch. 45 § 45.4** rencontre la même
   distinction sur un portefeuille entier ; le **ch. 46** sur une instrumentation candidate.
6. **La lacune de corrélation, exposée et non comblée.** C'est **le legs négatif du chapitre**, et le
   plus opposable : *l'identité serait la clé de jointure, et rien ne la constitue.* Le **ch. 41
   § 41.5** en dépend — une boucle de réémission suppose de savoir **quel agent** l'indicateur
   condamne.

⚠ **Ce que le chapitre ne lègue pas.** Aucune **mesure** : les métriques relevées ne sont pas comptées
ici, elles le sont au **ch. 40 § 40.1.2**, *qui en dénombre seize*. Aucun **verdict de grille** : la grille du ch. 14 y sert en
lecture inversée, à nommer ce que l'instrument ne produit pas. Et **aucune propriété démontrée d'un
outil nommé** — *deux produits sont cités, deux régimes d'absence sont déclarés, et rien n'est
recommandé.*

---

## § 38.6 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée (PRD, Annexe A).

**Ce qui est enfreint.** Portes **G-3**, **G-4** (préalable déclaré de ce mouvement) et **G-5**
(conditionne le Livre entier, **D-2** non prise) ; **volet résiduel de G-1** ; **ordre de rédaction
du PRD §6**. Instruction d'auteur du **27 juillet 2026**. ⚠ **Deux de ces portes ont bougé depuis,
et l'infraction n'en est pas rattrapée** : **G-3 est franchie** et le **volet de faits de G-1 est
levé**, l'un et l'autre le **28 juillet 2026** — *un franchissement qui suit une infraction la
solde, il ne la rattrape pas*, et **cette pièce n'a pas été ré-adossée au socle consolidé**. **G-4
et G-5 restent entières.**

1. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ **Ce chapitre était le plus exposé du
   mouvement à l'ouverture de G-1** : son objet principal est un corpus **sans version citable**,
   dont le socle du Vol. III ne fixait l'état qu'au 21 juillet 2026. ☑ **Les entrées de ce chapitre
   ont été portées à leur source primaire le 28 juillet 2026** et l'exposition s'est vérifiée :
   **une entrée a changé** — la conformité annoncée du § 38.2.3 —, et **une source annoncée au
   brouillon est entrée en service** (§ 38.5). ⚠ **Le résidu se cite avec le franchissement** :
   **cinq entrées demeurent ☐ non établies**, dont deux dont la source a été **retirée du dépôt**,
   et *re-datée ne veut pas dire confirmée.* **Rien de cela ne rend un énoncé central** : le régime
   de preuve du chapitre est inchangé.
2. **Les décomptes sont publiables** (G-2) ; le réel est reporté au [`README.md`](README.md) du
   Livre.
3. **Les renvois « ch. N » : état FINAL de la passe, et non ordre d'écriture.** ⚠ *La forme
   antérieure de ce point photographiait l'instant où cette pièce a été écrite et déclarait « ne
   sont pas rédigés : ch. 41, ch. 43 et ch. 45 » — alors que **la même passe les a écrits
   ensuite** ; elle est corrigée ici sur l'état que le commit produit.* **Les dix chapitres du
   Livre IV (ch. 37 à 46) sont rédigés**, comme le sont les **cinquante chapitres des cinq
   Livres** : *tous les renvois « ch. N » de cette pièce résolvent donc contre du texte.* ⚠ **Ce
   qui reste vrai de la forme antérieure, et qui est daté** : à l'heure où ce chapitre a été
   écrit, n'étaient rédigés ni les ch. 48 et 49 du Livre V, ni les chapitres du Livre III au-delà
   du ch. 26 — dont le ch. 25, siège de R-06, et le ch. 27, siège de l'article 12.1 —, non plus
   que les ch. 41, ch. 43 et ch. 45 — *les renvois qui les visent ont été posés comme renvois de
   plan et n'ont pas été re-vérifiés contre le texte paru après eux.* ⚠ **Et « résoudre contre du
   texte » ne vaut pas recevabilité** : *le texte visé est lui-même un brouillon hors portes.*
4. **La lacune de corrélation du § 38.5 est exposée, non comblée**, et sa question instruisible est
   formulée avec son corpus et son critère de clôture. ⚠ **Elle n'est pas rédigée** : *le seul geste
   admissible sur un front dont le plan déclare le socle non constitué est d'exposer le vide.*
5. **CA-IV-13 n'est pas satisfaite** — aucune relecture par un relecteur distinct du rédacteur
   (PRD §11).

**Remontées ouvertes par ce chapitre :**

- **R-IV-42 — non bloquante, de thèse, et déjà tranchée à la source.** La thèse du ch. 38 au TOC
  v0.25 porte « **dont le socle de standardisation est** les conventions sémantiques GenAI/agents
  d'OpenTelemetry ». Le Vol. III a **reformulé sa thèse le 21 juillet 2026** (confrontation P4.0,
  écarts ÉC-08 à ÉC-10) et écrit que **« leur état interdit de parler d'un socle acquis »** :
  premier des cinq échelons, aucune version citable, rupture de dépôt datée. S'y ajoute que «
  l'AgentOps commence par l'observabilité » est déclaré **par la source elle-même** comme un
  **ordonnancement d'auteur, non un fait**. **Demande remontée** : réalignement au titre des
  **décisions 8 et 14** du TOC. ⚠ **Ce n'est pas une divergence à arbitrer, c'est un report qui n'a
  pas été fait.** ☑ **Issue, 27 juillet 2026** — **TOC, décisions 8 et 14** — « dont **le socle de
  standardisation est** » tombe : *la source écrit que **leur état interdit de parler d'un socle
  acquis*** ; et « l'AgentOps commence par l'observabilité » est déclaré **ordonnancement
  d'auteur**. **La citation en tête de cette pièce porte la forme réalignée** (décision 17 du TOC).
- **R-IV-43 — non bloquante, de fait daté et de forme, portant sur la LIGNE DE SECTIONS du plan et
  non sur sa thèse.** Deux défauts distincts au même endroit. *(a)* La ligne annonce un « statut
  exact des conventions — **stable/expérimental** — à dater au gel » : **cette alternative binaire
  est réfutée par le socle**, l'échelle des groupes de conventions comptant **cinq échelons** (Vol.
  III F-76). Le Vol. III déclare ce même écart chez lui, contre son propre cadrage. *(b)* La
  datation v0.7 de la ligne ancre les conventions sur un millésime du **dépôt principal d'avril
  2026**, alors que F-74 établit leur **sortie de ce dépôt le 12 juin 2026** par une rupture
  déclarée, et que F-75 établit qu'**aucune version n'est citable** pour le dépôt qui les porte
  désormais. ⚠ **L'ancre du plan est donc antérieure au déplacement qui l'a périmée — exactement le
  défaut que ce chapitre documente chez un éditeur au § 38.2.3.** **Demande remontée** :
  réalignement de la ligne de sections (décision 8), et **inscription de la relève v0.7
  correspondante au domaine de G-1** pour reprise à la source primaire. ☑ **Issue, 27 juillet 2026**
  — **TOC** (ligne de sections) **et PRD** (domaine de G-1) — l'alternative binaire
  *stable/expérimental* est **réfutée par l'échelle à cinq échelons** ; ⚠ **et l'ancre de version du
  plan est antérieure de deux mois au déplacement qui l'a périmée** — *exactement le défaut que le
  § 38.2.3 documente chez un éditeur.*
- **R-IV-44 — non bloquante, de qualification de relève.** Le TOC porte au § 38.4 une **relève
  v0.10** posant que la propriété porteuse d'un environnement
  d'exécution agentique est la **détection de la divergence entre l'action effectuée et son
  enregistrement d'audit**, avec le **journal chaîné par empreintes** pour parade. ⚠ **Le Vol. I
  documente la parade, en [C]** (*Monographie* §4.9.2 : ajout seul, chaînage cryptographique,
  horodatage, admissibilité) — **il ne documente pas la thèse**. **Demande remontée** : que la
  relève soit **scindée à son point d'atterrissage** — le volet *parade* est couvert en [C] et
  relève de l'Annexe C au titre des lacunes de couverture, le volet *thèse* reste un repérage [C]
  entier à instruire en G-1. ⚠ *Une relève partiellement couverte qu'on laisse entière se paie deux
  fois : une fois en instruction inutile, une fois en couverture non déclarée.* ☑ **Issue, 27
  juillet 2026** — **TOC, Annexe C** — la relève v0.10 est **scindée à son point d'atterrissage** :
  *le volet **parade** est **couvert en [C]** par le Vol. I et entre à la troisième table des
  lacunes de couverture ; le volet **thèse** reste un repérage [C] entier, au domaine de G-1.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.28** — § 38.1 à
§ 38.5, dans l'ordre exact —, et le § 38.0 est une introduction de chapitre. La **table de couverture
est respectée pour ses quatre lignes**, y compris ses trois régimes propres : Vol. I *Monographie*
§2.9.6 en **seule affectation** — *le ch. 6 ne la conserve pas* —, §3.12.3 **prélevé au ch. 9**, qui
déclare la sortie à son bout, et §4.9.1-4.9.2 en **condensé**. La **sortie de périmètre est
reconduite** : le Vol. I *Monographie* §2.9 **n'est pas repris ici**, ses fondements restant au
ch. 6. Les **coupes de la source sont reconduites** — coût par jeton, horizon de tâche,
non-déterminisme, panorama des plateformes : **aucune n'est rétablie**. ⚠ **Cardinaux re-mesurés au
commit du 28 juillet 2026, sur le marqueur littéral et sur le corps seul** (décision 16 du TOC) ;
*les cardinaux antérieurs comptaient les applications du garde-fou et n'étaient re-mesurables par
aucune règle écrite.* Les **trois degrés d'absence** portent leur degré **à chaque énoncé négatif du
corps — domaine déclaré, sans cardinal** (alinéa c) ; le marqueur littéral « degré 3 » y compte
**cinq occurrences**, et ⚠ **les deux régimes du tableau 38.2 sont écrits comme deux régimes
distincts, jamais échangés**. La **conformité auto-déclarée du § 38.2 — une occurrence du marqueur «
auto-déclaré »** — est attribuée à son éditeur nommé. ⚠ **Le marqueur « Lecture de l'auteur » compte
six occurrences, et elles ne sont pas de même nature — la forme antérieure de cette phrase les
déclarait toutes six « suivies de ce que le socle établit et n'établit pas », ce que la re-mesure
réfute** : **quatre** ouvrent le diptyque *ce que le socle établit / ce qu'il n'établit pas*
(§ 38.1.3, § 38.2.3, § 38.3, § 38.5) ; les **deux** du § 38.4.1 sont l'une la **mention** du
marquage que les cinq points de contrôle portent dans leur volume d'origine, l'autre une
**décision d'architecture** qui nomme ce que la source gradue et ce que la somme absolutise.
*Toutes six déclarent la construction ; quatre seulement en bornent le socle.* **Aucun siège neuf
n'est posé** ; les deux sièges touchés — l'encadré du **ch. 7 § 7.5** et les points de contrôle
obligatoires du **ch. 43 § 43.3** — portent leur renvoi, et *le second visait, à la rédaction, un
chapitre non encore
écrit ; **le ch. 43 est rédigé au terme de la passe**, et le renvoi résout contre du texte — voir le
point 3 ci-dessus.*
