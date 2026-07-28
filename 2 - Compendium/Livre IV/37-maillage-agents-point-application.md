# Chapitre 37 — Le maillage d'agents : du *service mesh* au point d'application (PEP/PDP et *zero trust* agentique)

*Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et
synthèse architecturale.
Premier mouvement — appliquer (ch. 37). Chapitre unique du mouvement, et **chapitre d'ouverture du
Livre** : il porte les deux désambiguïsations que le Livre impose à ses neuf autres pièces.*

⚠ **Chapitre issu de la fusion v0.20 du TOC** (décision 11) : il porte **deux mouvements** —
*généalogie et anatomie* (ancien ch. 41), *le maillage comme point d'application* (ancien ch. 42) —
et donc **deux thèses**, conservées intégralement et **jamais fondues en une troisième**.

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé sur instruction d'auteur du 27 juillet 2026, **avant** les portes **G-3**, **G-4** et **G-5** du [PRD](../PRD/PRD.md) §5, et **hors de l'ordre de rédaction** du PRD §6, qui place ce Livre après les Livres I et III. ⚠ **L'écart de portes de ce chapitre est le plus large du compendium à ce jour, et il tient à un cumul plutôt qu'à une porte** : G-4 le conditionne comme premier mouvement du Livre IV, **G-5 conditionne le Livre entier** — l'arbitrage du risque 14 (le harnais), décision d'auteur **D-2**, non prise à la rédaction —, et G-3 n'était pas entamée. La règle cardinale du PRD §5 — *un chapitre écrit sur un socle vide n'est pas un chapitre en avance, c'est une inférence longue* — est **enfreinte et déclarée telle** ; voir la note de statut, § 37.10. ⚠ **Deux états ont bougé depuis, et aucun ne rend la pièce recevable** : **D-2 a été prise le 27 juillet 2026** — *par une autre passe et après cette rédaction* — et **G-3 a été franchie le 28 juillet 2026** (PRD v0.14) ; **G-4 et G-5 demeurent ouvertes**, et *un arbitrage qui suit une infraction la solde, il ne la rattrape pas* |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit pour ce Livre** : **aucun fait périssable de cette pièce n'a été repris à la source primaire**, et ils sont nombreux — statuts de préversion, révisions d'*Internet-Drafts*, dates de disponibilité générale, versions de dépôts publics. Ils sont ceux que les volumes sources portaient **à leur propre gel** : **21 juillet 2026** (Vol. III), **juin 2026** (Vol. I). *Ces gels ne sont pas celui de la somme et ne peuvent en tenir lieu.* |
| **Socle mobilisé** | **Aucune entrée du socle consolidé n'est mobilisée**, et ⚠ **le motif a changé de nature le 28 juillet 2026** : l'Annexe B **existe désormais** — [`socle-consolide.md`](../PRD/socle-consolide.md), **159 entrées `S-001`…`S-159`**, v1.2 —, la porte **G-3 étant franchie** (PRD v0.14). *Cette pièce a été écrite avant elle : elle n'adosse aucun énoncé à la série consolidée, et le re-ancrage de ses identifiants sur `S-nnn` est **dû, non fait*** (remonté à la note de statut, § 37.10). Les énoncés résolvent contre le **Vol. III *Monographie* ch. 22 et ch. 23**, dont les entrées **F-04**, **F-06**, **F-07**, **F-15**, **F-19**, **F-20**, **F-29**, **F-35**, **F-40**, **F-43**, **F-46**, **F-47**, **F-53**, **F-70**, **F-71**, **F-72**, **F-73**, **F-87**, **F-88** et les entrées héritées **H-01**, **H-03**, **H-09**, **H-10**, **H-12**, **H-13**, **H-15**, **H-24**, **H-30**, **H-33** **conservent leurs niveaux d'origine** ; et contre le **Vol. I *Monographie* §1.3.4 et §2.10.3-2.10.4**, qui entre **en [C]** (PRD §7.1). **Une seule entrée du Vol. II est mobilisée, et pour une réserve de formulation plutôt que pour un fait** : **F-01**, qui impose « cadre d'autorisation » et proscrit « sécurisé » (§ 37.2.4). ⚠ **Deux régimes se croisent dans cette pièce, et le second est le plus dur du compendium après la matière neuve** : les ch. 22 et 23 du Vol. III relèvent du régime **« source rédigée non publiable »** (PRD §7.2), qui exige le vote adversarial pour *toute* affirmation issue d'une pièce touchée par une remontée ouverte — **G-4 n'étant pas close, aucun de ces votes n'a eu lieu**. **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | ⚠ **Règle de comptage, décision 16 du TOC** : les cardinaux ci-dessous portent sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — de la première section à la synthèse, **en-tête et note de statut exclus** —, et ils sont **re-mesurés sur le corpus que le commit produit**. ⚠ **Un garde-fou appliqué sans que son identifiant soit écrit voit son DOMAINE déclaré, sans cardinal** (alinéa c) : *le domaine balayé est le corps entier, et les cardinaux antérieurs — qui comptaient les **applications** et non le marqueur — n'étaient re-mesurables par aucune règle écrite.* **Les deux séries sont balayées intégralement, zéros compris.** Vol. III — **R-09 (statut pré-normatif dit à chaque mention) : neuf occurrences**, § 37.2 (trois), § 37.4, § 37.5 (deux), § 37.7, § 37.8 (deux) ; **R-14 (trois degrés d'absence) : sept occurrences**, § 37.1 (trois), § 37.2, § 37.5 (deux), § 37.9 ; **R-02 (qualification par ce que la spécification démontre) : cinq occurrences**, § 37.1 (deux), § 37.2, § 37.4, § 37.5 ; **R-01 (le passeport n'existe dans aucune spécification) : deux occurrences**, § 37.4 et § 37.9 ; **R-04 (« AgentMesh », « plan de contrôle », « ACP » jamais nus) : deux occurrences**, § 37.0 et la synthèse — ⚠ *le garde-fou est appliqué bien au-delà, à chaque emploi des trois termes, sans que son identifiant soit répété : domaine déclaré, corps entier* ; **R-12 (traitement défensif au niveau architectural) : deux occurrences**, § 37.3 et § 37.6 ; **R-13 (échelle d'autonomie jamais nue) : deux occurrences**, § 37.0 et § 37.6 ; **R-03 (« maillage d'agents », terme de fournisseur) : une occurrence**, § 37.1 ; **R-11 (jalons « visés », jamais « fixés ») : une occurrence**, § 37.7. **R-05 à R-08, R-10 : zéro occurrence.** Vol. II — **R-8 (sigle jamais nu, quatre branches) : trois occurrences**, § 37.0, § 37.1 et § 37.2, **toutes renvoyées au siège du ch. 7 § 7.5, aucune reconstruite** ; **métriques et qualifications auto-déclarées (marqueur « auto-déclaré ») : sept occurrences**, § 37.2 (quatre), § 37.3, § 37.5 et la synthèse, chacune attribuée à son éditeur nommé. **R-1 à R-7 : zéro occurrence.** ⚠ **Faux ami déclaré** : « plan de contrôle » figure au § 37.1 au sens du **maillage de services pré-agentique** (ch. 1 § 1.3.4), où il n'est pas le terme que R-13 du Vol. III vise ; le sens visé est déterminable de chaque phrase, comme la tête de Livre l'impose |
| **Volumétrie cible** | ≈ **11 000 mots** de corps (§ 37.0 à la synthèse), **cible dérivée** de l'enveloppe du Livre (**69 000 mots**, TOC v0.25) au prorata des sections et du volume de source consommé — **la plus haute du Livre**, ce chapitre portant **neuf sections pour deux mouvements** et consommant deux chapitres entiers du Vol. III. ⚠ **La leçon du Livre I est appliquée avant la première ligne** : les **dix cibles dérivées du Livre ont été additionnées et valent exactement 69 000** — le Livre I avait dépassé faute que quiconque additionne ses onze dérivations. ☑ **Décompte publiable depuis G-2** ; **réel : mesuré par [`PRD/decompte.sh`](../PRD/decompte.sh) et reporté au [`README.md`](README.md) du Livre**, seule autorité de décompte du volume. ⚠ **D-4 s'applique** : l'écart se documente, **il ne se corrige ni par amputation ni par gonflement** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) **v0.28**, entrée du chapitre 37, premier mouvement — **thèse réalignée en v0.28**, décisions 8 et 14, remontée R-IV-38)* — **le présent ouvrage définit** le maillage d'agents par filiation avec le patron *service mesh* — un plan de données qui médiatise chaque arête, un plan de contrôle qui centralise la politique ; **cette définition est celle de l'ouvrage, et le terme n'en a pas d'autre qui fasse autorité**. La filiation retenue fournit un **instrument de tri par statut** des offres que le Vol. III a ouvertes. ⚠ **Coût déclaré, repris de la source** : elle **n'affirme rien de l'écart entre le discours des fournisseurs et leurs réalisations** — *la forme antérieure, « trie ce que le terme recouvre réellement de ce qu'il recouvre en marketing », affirmait exactement l'énoncé que la source déclare ne pas faire.*

> **Thèse du second mouvement**, citée depuis le TOC **v0.28**, entrée du chapitre 37 *(thèse réalignée en v0.28, décisions 8 et 14 — remontée R-IV-39)* — **Lecture de l'auteur** — le maillage est **un** lieu où le passeport du ch. 16 **pourrait** devenir opposable, **et le seul que la somme instruise** — PEP adossé à un PDP, transposition du *zero trust* au graphe d'agents. ⚠ **Vérifier chaque arête, sans confiance héritée de la topologie, est un principe d'architecture posé par l'ouvrage, non une propriété relevée d'un maillage déployé** — *report d'un bornage que le Vol. III avait fait le 21 juill. 2026 et que le plan n'avait pas suivi.*

⚠ **Les deux thèses citées ci-dessus portaient, à la rédaction, une forme que leur source avait
elle-même bornée — le réalignement est FAIT, et l'histoire de l'écart se conserve** (décision 17 du
TOC, alinéa c). Le balayage avait porté sur **les deux thèses du chapitre**, et **les deux étaient
désalignées** ; le corps a été écrit sous la forme bornée, la thèse était citée verbatim dans sa forme
v0.25 comme le PRD §6 l'exigeait, et les deux écarts avaient été **remontés** (R-IV-38 et R-IV-39,
§ 37.10). ☑ **Les deux remontées sont soldées par l'arbitrage v0.28 du TOC** (décisions 8 et 14), et
**les citations ci-dessus portent désormais la forme réalignée**, reportée **par copie** depuis
l'entrée courante du plan. *Ni la v0.29 ni la v0.30 du TOC ne modifient une thèse de ce Livre.*

- **Premier mouvement — forme antérieure, v0.25** : « le maillage d'agents **est la réinstanciation**,
  au niveau agentique, du patron *service mesh* […] ; cette filiation **trie ce que le terme recouvre
  réellement de ce qu'il recouvre en marketing** ». Le Vol. III n'écrivait pas que le maillage **est**
  une réinstanciation : il écrit que **l'ouvrage le définit** par filiation, que « cette définition est
  celle de l'ouvrage, et le terme n'en a pas d'autre qui fasse autorité ». Et il déclare expressément,
  en coût de sa thèse, qu'elle **« n'affirme rien de l'écart entre le discours des fournisseurs et
  leurs réalisations ; elle affirme un tri par statut, sur cinq offres nommées »**. *Le membre « ce
  qu'il recouvre réellement / ce qu'il recouvre en marketing » était exactement l'énoncé que la source
  déclare ne pas faire.* ☑ **Réalignement porté au plan par R-IV-38.**
- **Second mouvement — forme antérieure, v0.25** : « le maillage est **le** lieu où le passeport du
  ch. 16 **devient** opposable […] : vérifier chaque arête, sans confiance héritée de la topologie ».
  Le Vol. III avait **reformulé sa thèse le 21 juillet 2026** (confrontation P4.0, écarts ÉC-05 à
  ÉC-07) : le maillage y est **« *un* lieu où le passeport […] *pourrait* devenir opposable, et le
  seul que cet ouvrage instruise »**, et « vérifier chaque arête » y est un **principe d'architecture
  posé par l'ouvrage, non une propriété relevée d'un maillage déployé**. Le TOC portait encore
  l'article défini et l'indicatif présent. *Ce n'était pas une divergence à arbitrer : c'était un
  report qui n'avait pas été fait.* ☑ **Réalignement porté au plan par R-IV-39.**

---

## § 37.0 — Ouverture : ce que ce Livre applique, et les deux mots qu'il faut désambiguïser d'abord

Les trois Livres qui précèdent ont produit trois choses distinctes et aucune n'est un dispositif. Le
Livre I a posé la couche protocolaire — ce qui parle à quoi, et sous quelles spécifications (ch. 8 à
11). Le Livre II a construit un objet — le **passeport d'agent** du ch. 16 — et l'a laissé sans lieu :
il assemble une carte signée, une inscription au registre, une chaîne de mandat et des attestations,
constate qu'aucune de ces pièces ne fournit aux autres l'ancrage qui leur manque, et renvoie à
**ce chapitre** la seconde moitié de **Q-D** — *que peux-tu faire ?*, quatrième question de la grille
du **ch. 14** —, c'est-à-dire l'**opposabilité** des bornes de privilège au point d'application. Le
Livre III a produit des obligations. Le présent Livre instruit **où tout cela s'applique, se mesure,
se produit et se compose**.

Le chapitre qui l'ouvre est celui du **lieu**. Il ne demande pas ce qu'un agent doit prouver — le
Livre II l'a demandé — mais **où la preuve est exigée, par quoi, et ce qu'il en reste de démontrable
à cet endroit**.

⚠ **Deux désambiguïsations commandent tout le Livre, et elles sont posées ici avant la première
affirmation.**

**Première — « AgentMesh », garde-fou R-04 du Vol. III, branche (f), imposé en tête de Livre.**
« AgentMesh » désigne dans toute la somme le **patron d'infrastructure** : un plan de données qui
médiatise chaque arête du graphe d'interaction, un plan de contrôle qui centralise la politique. Le
terme sert ailleurs dans l'industrie à nommer une **équipe plateforme**, un **produit commercial** et
une **couche de courtage**. La branche (f) a été ouverte parce que la v0.1 du cadrage de ce volume
employait le mot dans deux sens incompatibles à trente lignes d'écart. **Aucune phrase de ce Livre
n'emploie le terme sans que le sens visé soit déterminable d'elle-même.**

**Seconde — « plan de contrôle », garde-fou R-8 du Vol. II.** Le patron décrit ici **comporte** un
plan de contrôle, et le sigle qui l'abrège porte une collision à quatre branches dont **le siège est
au ch. 7 § 7.5**. ⚠ **Ce chapitre n'en reconstruit aucune** : il y renvoie à chaque emploi, comme la
somme l'exige de toute pièce touchant cette matière. *Reconstruire un encadré de désambiguïsation
ailleurs qu'à son siège est la manière la plus sûre de faire diverger les branches.*

⚠ **Et un faux ami est déclaré plutôt que fui.** « Plan de contrôle » au sens du **maillage de
services pré-agentique** — le socle transposable posé au **ch. 1 § 1.3.4** — n'est pas le terme que
R-13 du Vol. III vise. Le § 37.1 l'emploie dans ce sens, et le dit.

**Le chapitre se lit en deux mouvements et neuf temps.** Le premier mouvement établit ce que le
maillage **est** — d'où vient la filiation et ce qu'elle n'autorise pas (§ 37.1), ce que le socle
documente des réalisations (§ 37.2), pourquoi l'arête est devenue la frontière (§ 37.3), ce que la
grille du ch. 14 en dit (§ 37.4). Le second établit ce qu'il **applique** — où se prend et où
s'applique la décision (§ 37.5), quels garde-fous d'exécution s'y logent (§ 37.6), comment le *zero
trust* s'y transpose (§ 37.7), ce qu'il trace de la chaîne de mandat et ce qu'il n'en résout pas
(§ 37.8), et à quelles conditions tout cela est faux (§ 37.9).

⚠ **Ce que le chapitre ne traite pas, dit ici pour qu'on ne le prenne pas pour un oubli.** Le
**routage sémantique** n'y entre pas : la source l'a coupé à son test d'appartenance, faute de
répondre à *que vérifie-t-il de l'identité ou du mandat ?*, et aucune entrée ne le documente. La
**couche de transport** n'y entre pas davantage, coupée au même contrôle le 22 juillet 2026 pour le
même motif. **L'émission** n'y entre pas — elle est au Livre II. Et **l'accord entre agents sous
asynchronie et défaillance partielle** n'y entre pas : la décision d'auteur **D-7 a fermé ce chapitre
à cette matière** le 27 juillet 2026, périmètre assumé et déclaré ; *y ajouter une section rouvrirait
la décision, non le seul chapitre.*

---

# Premier mouvement — Du *service mesh* à l'*agent mesh* : généalogie et anatomie

*Ancien ch. 41 du plan (décision 11 du TOC). Entrée conservée intégralement.*

## § 37.1 — Généalogie et définition : ce que la filiation apporte, ce que le socle en porte

**Avertissement de portée, posé avant la première ligne de généalogie, et repris de la source parce
qu'il commande tout le reste.** Le titre annonce une généalogie ; **le socle n'en porte pas la
source**. Le Vol. III ne documente pas le patron du maillage de services : c'est une **absence de
documentation dans le corpus de cet ouvrage, non un fait négatif vérifié** (R-14 du Vol. III,
degré 3). Le constat est vérifiable sur pièce et il n'est pas anodin — le programme de constitution
de son socle nommait le corpus *service mesh* parmi les sources du lot qui devait l'instruire, et
**aucune des affirmations retenues par ce lot ne porte sur ce corpus**. **La filiation revendiquée
n'hérite donc de rien : elle est *posée*.** Sa valeur est celle d'un instrument d'analyse, jamais
celle d'un fait rapporté.

⚠ **Le compendium hérite pourtant, lui, d'un socle que le Vol. III n'avait pas** — et c'est un cas
de la classe que l'Annexe C du TOC nomme depuis la v0.24. Le **ch. 1 § 1.3.4** pose le maillage de
services pré-agentique : séparation d'un **plan de contrôle**, qui distribue configuration et
politique, et d'un **plan de données** fait de mandataires latéraux (*sidecar proxies*) interceptant
tout le trafic de chaque service ; coût mesurable du modèle latéral ; plans de données alternatifs —
modes ambiants dissociant une couche par nœud du reste, déport dans le noyau du système
d'exploitation ; convergence du routage d'entrée et du trafic est-ouest sous une abstraction
déclarative unique ; et le **maillage d'événements** comme pendant événementiel. ⚠ **Ce n'est pas une
contradiction entre volumes, et le confondre avec une contradiction effacerait l'information qui
compte** : « le socle du Vol. III ne documente pas le *service mesh* » et « le Vol. I le documente »
sont **logiquement compatibles**. C'est une **lacune de couverture**, datée, et l'énoncé du Vol. III
**reste exact dans son périmètre**. La conséquence pratique est double : la filiation est mieux
adossée dans la somme qu'elle ne l'était chez sa source — mais **au régime [C]**, le Vol. I entrant
par ses références et non par le contenu de ses affirmations. *Une filiation adossée en [C] ne porte
toujours aucun fait central.*

### 37.1.1 Le terme, et son statut

« Maillage d'agents » (*agent mesh*) **est un terme de fournisseur avant d'être un terme de norme ;
il n'a pas de définition normative à date** (R-03 du Vol. III). La somme l'emploie au sens que le
Vol. III lui a donné à son siège unique, et **ne le redéfinit pas** :

> un dispositif d'infrastructure interposé sur les interactions d'un parc d'agents — entre agents,
> entre agent et outil, entre agent et service —, composé d'un **plan de données** qui médiatise
> chaque arête du graphe d'interaction et d'un **plan de contrôle** qui en centralise la politique.

⚠ **Convention de lecture pour tout le chapitre** : « plan de contrôle » s'entend ici **au sens
infrastructure**, et il ne s'emploie jamais sans ce qualificatif ou son renvoi (R-8 du Vol. II, dont
les quatre branches siègent au **ch. 7 § 7.5**).

**Deux bornes accompagnent cette définition, et la seconde est celle qu'on perd le plus vite.**
*Première* — l'absence de définition normative est un **degré 3, pas un balayage** : le lot
d'instruction déclare n'avoir rencontré aucune définition normative du terme dans un texte de norme
ouvert **au cours de la passe**, ce qui est une absence de documentation dans le corpus consulté, non
un fait négatif vérifié (R-14 du Vol. III). *Seconde* — **le relevé porte sur l'anglais**.
L'expression française « maillage d'agents » n'a fait l'objet d'aucune recherche distincte : ce que
le socle documente est l'emploi de *agent mesh* chez **deux fournisseurs**, et rien de l'usage
francophone.

### 37.1.2 Ce que le socle documente du terme est une homonymie, constatée sur pièce

« Agent mesh » désigne **deux objets techniquement distincts chez les deux fournisseurs consultés**,
documentés chacun par son éditeur (Vol. III **F-72**, **[B, degré 1]**). Chez **Solo.io**, une
**couche de connectivité** posée par analogie explicite avec le maillage de services, à laquelle le
communiqué de son éditeur — daté du **24 avril 2025** — assigne la sécurité, l'observabilité, le
cloisonnement et les garde-fous : ⚠ **objectifs annoncés par le fournisseur, non propriétés
démontrées** (R-02 du Vol. III). Chez **Solace**, un **cadriciel applicatif multi-agent** bâti sur un
connecteur d'IA propriétaire, une trousse de développement d'agents et le protocole A2A — dépôt
public `SolaceLabs/solace-agent-mesh`, version **1.28.4 du 29 juin 2026**.

⚠ **Trois bornes, et la troisième interdit une conclusion qu'on tire spontanément.** *Un* : les deux
noms d'éditeurs ne figurent pas au libellé de l'entrée de socle qui les agrège ; ils sont pris aux
sources primaires que le lot a ouvertes et citées — *anonymiser un éditeur est une faute au même
titre qu'en recommander un*. *Deux* : **le relevé porte sur deux fournisseurs et n'autorise aucune
clause d'exclusivité** — il ne dresse pas la liste des emplois du terme. *Trois* : **le second objet
n'est pas une réinstanciation du maillage de services**, et la définition posée ci-dessus ne le décrit
pas, ni ne prétend le décrire. *C'est précisément ce que le tri par filiation permet de dire, et
c'est tout ce qu'il permet de dire.*

### 37.1.3 Ce que la généalogie apporte, et ce qu'elle ne prouve pas

Les trois pièces que la filiation nomme — le conteneur adjoint (*sidecar*), la passerelle
(*gateway*), la séparation des deux plans — sont des objets d'ingénierie que **le ch. 1 § 1.3.4
documente et que le socle du Vol. III ne porte pas**. Il en va de même de l'authentification mutuelle
du transport (*mutual TLS*, mTLS). **Aucun énoncé du présent chapitre ne dépend de ces quatre
objets** : ils sont nommés comme l'origine revendiquée d'une analogie, jamais mobilisés comme faits.

**Un seul membre de la généalogie est documenté au socle, et c'est celui qui touche à l'identité** —
ce qui n'est pas une coïncidence mais la conséquence du périmètre du Vol. III. La spécification
d'identité de charge de travail SPIFFE, de statut **« Stable »**, définit l'identité comme un URI
conforme au RFC 3986 composé d'un nom de **domaine de confiance** et d'un **chemin**, et le document
d'identité vérifiable (SVID) comme le mécanisme par lequel une charge de travail **communique** son
identité à une ressource ou à un appelant ; elle énonce qu'un SVID est valide **s'il a été signé par
une autorité du domaine de confiance de l'identité qu'il porte** (Vol. III **F-87**, **[B]**).

⚠ **Ce que cette spécification démontre est une vérification de signature dans un domaine de
confiance** (R-02 du Vol. III). **Elle n'énonce pas** ce que cette vérification n'établit pas — ni
preuve de propriété d'une entité, ni décision d'autorisation : **absence de documentation dans le
corpus, non fait négatif vérifié** (R-14, degré 3). Côté fondation, l'organisme qui héberge le projet
classe SPIFFE et SPIRE au niveau **« Graduated »**, sa page projet datant ce passage du **23 août
2022** pour l'un et du **22 août 2022** pour l'autre (Vol. III **F-88**, **[B]**). ⚠ **Divergence
d'un jour entre deux pages de la même fondation, reproduite telle quelle et non arbitrée** — et
**re-constatée à la source le 28 juillet 2026** (socle consolidé, `S-134`), *la fondation la
reconduisant onze mois après le relevé d'origine sans la corriger ni l'expliquer* ; et « Graduated »
est un **niveau de maturité de fondation**, qui ne mesure ni adoption ni déploiement.

⚠ **Le siège de ce moment de la généalogie est au ch. 3 § 3.3**, où le socle IAM pré-agentique est
posé **une seule fois pour toute la somme**. Ce chapitre l'y renvoie et **ne le reconstruit pas** ; ce
qu'il en retient tient en une phrase : *c'est le substrat d'identité vérifiable que le maillage de
services a légué, et le seul dont la somme dispose au socle.*

### 37.1.4 Ce que la filiation permet de trier — et la formule qui n'est pas écrite

**Lecture de l'auteur** — la filiation fournit un **critère de tri**, et un seul : est un maillage
d'agents au sens de cette somme ce qui présente les deux plans, médiatise les arêtes et centralise la
politique. **Ce que le socle établit** : l'homonymie du terme chez deux éditeurs nommés (F-72,
**[B, degré 1]**) ; l'existence d'une syntaxe d'autorisation par arête dans un mécanisme ouvert
(F-71, **[B]**) ; le tri par statut de trois offres (F-70, **[B]**). **Ce qu'il n'établit pas** :
que les objets ainsi triés se comportent conformément à ce que leurs éditeurs en annoncent, ni qu'un
écart existe entre ce discours et ces réalisations. ⚠ **La formule « ce que le terme recouvre
réellement contre ce qu'il recouvre en marketing » n'est donc pas écrite dans ce chapitre**, et son
absence est le premier effet du réalignement déclaré en tête : *un tri par statut déclaré n'est pas
un démenti de discours commercial, et confondre les deux ferait de la neutralité fournisseur une
posture plutôt qu'une règle.*

## § 37.2 — Anatomie du maillage agentique, à l'état daté

**La règle de cette section est le statut, et il se dit à chaque mention.** Annonce, feuille de
route, préversion et disponibilité générale documentée sont quatre choses différentes ; la
**production attestée par un tiers indépendant** en est une cinquième. Les offres nommées ci-dessous
sont retenues comme **cas d'instanciation documentés par sources primaires, jamais comme
recommandations** — et la neutralité fournisseur **interdit de recommander, non de nommer** : *un
statut non attribué à son éditeur n'est pas revalidable au gel suivant.*

### 37.2.1 Trois offres, trois statuts

Le socle porte trois passerelles ou mandataires d'arête, chacun avec son statut auto-déclaré
(Vol. III **F-70**, **[B]**).

| Objet | Éditeur ou porteur | Statut auto-déclaré, à sa date | Ce que le statut ne dit pas |
|---|---|---|---|
| Passerelle MCP | **Docker**, au titre de « Docker AI Governance » | **réservée sur invitation** — soit une **disponibilité restreinte**, distincte d'une disponibilité générale | rien d'un déploiement constaté |
| **Amazon Bedrock AgentCore** (dont *Gateway* et *Identity*) | **AWS** | **généralement disponible depuis le 13 octobre 2025**, dans neuf régions nommées | disponibilité générale **annoncée par le fournisseur**, non déploiement constaté par un tiers |
| **agentgateway**, mandataire ouvert | projet déclaré de la **Linux Foundation** | **v1.4.0-alpha.2, signalée pré-version** ; dernière publication non marquée pré-version : **v1.3.1 du 22 juin 2026** | qu'une syntaxe pré-version soit un contrat stable |

: Tableau 37.1 — Les trois offres portées par le socle du Vol. III, avec leurs statuts auto-déclarés au 21 juillet 2026. ⚠ **Chaque qualification est celle de son éditeur, nommé** ; aucune n'a fait l'objet d'une vérification indépendante.

⚠ **L'un des trois statuts a bougé depuis le gel, et il se date plutôt qu'il ne se réécrit.** La
re-datation à la source primaire conduite au titre du **volet résiduel de G-1** — 28 juillet 2026,
socle consolidé v1.2, entrée **`S-116`** — enregistre que la **version 1.4.0 du mandataire ouvert a
été publiée le 27 juillet 2026 et n'y est pas signalée pré-version** : elle y est à la fois la
publication la plus récente et la plus récente stable. **Le tableau ci-dessus conserve l'état du
21 juillet 2026**, qui est celui du socle sur lequel ce chapitre est écrit ; ⚠ **ce que le constat
périme est la citation du numéro et de la date, non le tri lui-même** — *un tri par statut reste un
tri par statut quand un statut change*. ⚠ **La réserve de pré-version que les § 37.2.2, § 37.4 et
§ 37.5.1 reprennent porte donc cette date**, et elle ne s'écrit nulle part au présent intemporel.

⚠ **Deux clauses d'exclusivité auto-déclarées ne sont pas reprises** : celle que la page produit
d'AWS énonce sur elle-même, et celle du fichier de présentation d'`agentgateway`. Aucun balayage ne
permet de les établir, et **elles restent attribuées à leur auteur**.

⚠ **La colonne qui manque est celle qui compte, et elle est vide.** Le socle **ne documente aucun
maillage d'agents en production attestée par un tiers indépendant** : c'est une **absence de
documentation dans le corpus, non un fait négatif vérifié** (R-14 du Vol. III, degré 3). Le rapport
du lot qualifie lui-même cette colonne d'absence de documentation, et le déclare faute de passe
dédiée.

⚠ **Trois écarts de cardinal et de vocabulaire sont hérités, déclarés, et non résolus ici.** *Un* :
la thèse du Vol. III annonce « cinq réalisations », là où la répartition constatée en nomme **six** —
l'écart tient à un protocole de transport à l'état de brouillon, rangé ou non parmi les offres selon
la convention de comptage. *Deux* : la même thèse appelle la production « la **quatrième** catégorie
du tri », alors que le rapport la traite comme le **troisième degré** d'un tri à trois. *Trois* : la
**disponibilité restreinte**, seul statut sous lequel la passerelle de Docker se laisse ranger, ne
figure ni dans le tri à trois degrés ni dans les quatre statuts du cadrage. **La somme écrit les
statuts tels que les sources les portent et ne tranche aucun des trois** : *un cardinal ne se recopie
jamais, il se re-mesure* — et ces trois-là se re-mesureront à la collation de fond (G-4).

### 37.2.2 Ce qu'un mandataire d'arête spécifie, et à quel titre

La documentation du mandataire ouvert spécifie une **politique d'autorisation propre à MCP**, écrite
en *Common Expression Language* (CEL), **évaluée contre des invocations de méthodes** et exposant des
champs d'**outil**, d'**invite** et de **ressource** (Vol. III **F-71**, **[B]**).

⚠ **Trois bornes, inséparables de l'énoncé.** *Un* : c'est ce que la documentation **décrit**, non un
comportement démontré ni évalué indépendamment (R-02 du Vol. III). *Deux* : **au 21 juillet 2026**,
la publication la plus récente d'`agentgateway` — le mandataire nommé au § 37.2.1 — est signalée
**pré-version** (F-70), *la syntaxe existe et sa stabilité n'est pas déclarée* (R-09) ; ⚠ **cette
borne porte sa date, et le § 37.2.1 enregistre ce qui a bougé depuis**. *Trois* : **l'énumération des
champs n'est pas exhaustive**, le contrôle de bornage du lot ayant retiré la clause d'exclusivité de
l'affirmation d'origine — **aucun fait négatif ne se dérive de cette liste**, et le § 37.4 en tire la
conséquence.

### 37.2.3 Le courtage : A2A normalise le chemin et décline le registre

Le protocole A2A, lancé par **Google en avril 2025** et transféré à la **Linux Foundation en juin
2025**, a pour première spécification stable sa **v1.0**, son dernier correctif **v1.0.1 datant du
28 mai 2026** (Vol. III **H-01**, **[A ; ligne v1.0.1 en B]**). Sa documentation définit un chemin de
découverte normalisé, énumère **trois stratégies** — URI bien connue, registres organisés,
configuration directe — et **déclare explicitement qu'aucune API normalisée n'est prescrite pour les
registres organisés** (Vol. III **F-43**, **[B, degré 2]**).

⚠ **Le degré compte et se dit** : c'est un **fait négatif ÉTABLI, degré 2** — porté par une réserve
de la documentation du projet lui-même, non par un balayage du texte normatif de la spécification.
**Le siège de ce constat est le ch. 9**, qui l'instruit ; ce qui appartient ici est sa **conséquence
d'anatomie** : un maillage qui fournit un courtage le fait **sans API de registre normalisée par ce
protocole**. ⚠ **L'énoncé plus large « le courtage n'est pas dans le protocole » n'est pas
soutenu** — la source le déclare expressément de son propre relevé.

Un service d'annuaire concurrent prend l'option inverse et se spécifie par un ***Internet-Draft* de
soumission individuelle**, à sa révision **02 du 6 juillet 2026** : **travaux émergents, non une norme
ratifiée** (R-09 du Vol. III). ⚠ **Une question héritée reste ouverte et n'est pas comblée ici** :
l'intitulé complet de la composante « ACP » d'un projet de fondation, et son identité ou non avec le
protocole ACP fusionné dans A2A, ne sont **caractérisés par aucune entrée** (Vol. III **H-10**,
**[C]** ; lacune 8 de son PRD). **Conséquence opposable** : ces deux emplois du sigle **ne sont jamais
agrégés**, et **le siège de la désambiguïsation est au ch. 7 § 7.5** — quatre branches, R-8 du Vol. II
—, que ce chapitre ne reconstruit pas.

### 37.2.4 Datation, et une échéance qui pèse sur cette section

MCP est une interface client-serveur JSON-RPC 2.0 dotée d'un **cadre d'autorisation** fondé sur
OAuth, dont la gouvernance a été transférée **en décembre 2025** à l'Agentic AI Foundation (Vol. III
**H-09**, **[A]**). ⚠ **« Cadre d'autorisation », jamais « sécurisé »** : la forme est imposée par la
réserve F-01 du Vol. II, et le ch. 8 en est le siège.

Une **révision majeure** — protocole sans état, retrait de l'en-tête de session — est **annoncée au
brouillon**, et **sa date n'est pas confirmée à la source** : la revalidation d'ouverture du Vol. III
a établi la substance et non la date. La somme écrit donc « annoncé au brouillon » et **jamais une
date de publication** (R-09). ⚠ **Aucune conséquence n'en est tirée ici** : ce que cette révision
changerait pour un mandataire d'arête n'est documenté par aucune entrée, et **l'inférer serait
exactement la faute que la somme prend pour objet**.

⚠ **Et une échéance de péremption pèse sur ce paragraphe, datée du lendemain du gel.** Le registre du
gel unique enregistre la ratification de cette révision au **28 juillet 2026** — soit **le lendemain
de la date de gel de la somme**. *Le gel ne s'avance pas d'un jour pour l'absorber* ; la
re-datation est due, et elle est due au ch. 8 avant de l'être ici.

☑ **Elle a été faite depuis, et son résultat se consigne sans rien verser** — volet résiduel de
**G-1**, 28 juillet 2026, entrée **`S-001`** du socle consolidé : la révision annoncée **est servie
comme révision courante à cette date**, et *la péremption que l'entrée avait datée est advenue*.
⚠ **Le constat porte sur la bascule, jamais sur le contenu** : la revalidation en bloc est **ouverte
et non exécutée**, le texte de la révision neuve n'a pas été extrait, et **ce qu'elle changerait pour
un mandataire d'arête n'est pas mieux documenté qu'avant**. *Le siège de la re-datation demeure le
ch. 8.*

## § 37.3 — Ce que l'arête change : la non-compositionnalité de la sûreté

**La prémisse est une thèse d'un volume antérieur, et elle s'attribue.** Le Vol. I écrit qu'« un
agent sûr et un outil sûr, une fois composés, ne donnent pas un système sûr ; la sûreté n'est pas une
propriété compositionnelle », et que « la frontière de confiance n'est plus le périmètre d'un système
mais *chaque arête* du graphe d'interaction » ; son corollaire pose qu'« un modèle de menace agentique
doit raisonner sur le graphe de composition, pas sur l'inventaire des composants » (Vol. III **H-24**,
**[C]** ; Vol. I *Monographie* §3.10.1).

⚠ **Trois précautions, et elles ne sont pas rhétoriques.** *Le niveau* — H-24 entre en **[C]** : la
vérification du Vol. I porte sur ses références, non sur le contenu de ses affirmations. Elle entre
donc comme **thèse d'un volume antérieur, à attribuer**, et **aucune affirmation centrale de ce
chapitre ne s'y adosse comme à un acquis**. *Le siège* — la formule vit à plusieurs endroits du
Vol. I sous trois formes, dont l'une dans un fichier **retiré du dépôt le 22 juillet 2026** ; **le
verbatim n'est revendiqué que sur la forme longue de la *Monographie***, seule que le socle porte mot
pour mot, et les autres sièges sont **nommés et non cités**. *La portée* — c'est un énoncé
d'architecture, non un résultat expérimental.

**Ce que le Livre II en a fait, et pourquoi le maillage en découle.** Le **ch. 19** range chaque
attaque selon **le maillon de la chaîne d'identité ou de mandat qui cède** — traitement défensif
exclusif, au niveau architectural (R-12 du Vol. III). Le **ch. 20** oppose la vérification à
l'admission et la **vérification continue**, et en borne l'acquis à un **énoncé attribué** : un
rapport d'un projet de sécurité applicative, version **2.01**, daté de **juin 2026**, **énonce** la
vérification continue comme la propriété distinctive de l'identité d'agent (Vol. III **F-20**,
**[A]**). ⚠ **Deux réserves accompagnent l'entrée et se reportent** : la formule est celle de ce
rapport, **à sa date et à sa version, non un consensus du domaine** ; et le rapport reprend par
ailleurs des métriques auto-déclarées d'éditeur, **dont aucune n'est reprise ici**. Le **ch. 17**
localise, lui, l'endroit où chaque mécanisme instruit perd le fil de la délégation.

Lecture de l'auteur — le maillage n'est pas une couche ajoutée par commodité d'exploitation, mais la
**conséquence architecturale** d'une frontière de confiance déplacée sur chaque arête : *si la
propriété à préserver n'est pas locale à un composant, le lieu où l'on peut agir n'est pas le
composant, c'est l'arête.* **Ce que le socle établit** : la thèse de non-compositionnalité, portée
par un volume antérieur et attribuée (H-24, **[C]**) ; l'existence d'un mécanisme d'autorisation par
arête doté d'une syntaxe documentée (F-71, **[B]**) ; le tri par statut de trois offres (F-70,
**[B]**). **Ce qu'il n'établit pas** : que ce mécanisme réponde à cette prémisse — ⚠ **aucune entrée
ne met les deux en rapport** —, ni qu'un maillage couvre l'ensemble des arêtes d'un graphe, ni qu'une
couverture partielle préserve quoi que ce soit.

**Une conséquence de méthode, et elle borne tout ce qui suit.** Si la frontière est l'arête, la
question « ce mécanisme est-il sûr ? » cesse d'être bien formée ; elle devient **« que vérifie cette
arête, et qu'en reste-t-il de démontrable ? »**. C'est exactement l'objet de la grille du ch. 14, et
c'est pourquoi le § 37.4 l'applique plutôt que de conclure par un jugement.

## § 37.4 — La grille du ch. 14 appliquée au maillage : ce qu'il vérifie, ce qu'il transporte, ce qu'il ignore

**Trois règles d'emploi commandent ce qui suit, et elles sont reprises du ch. 14 sans être
redécidées.** *Un* : la grille s'applique **par mécanisme, et non par produit** — ce qui est jugé ici
est l'**autorisation par arête telle que le socle la documente** (F-71), non les offres du § 37.2,
dont le tri porte sur des statuts et non sur des capacités. *Deux* : **trois verdicts seulement**, et
**aucun quatrième verdict de complaisance**. *Trois* : là où le corpus est muet, **la case reste vide
et porte son degré** — ce n'est pas une note intermédiaire donnée au mécanisme, c'est **l'état de la
preuve** qui est déclaré.

**Q-A — qui es-tu ?** Q-A demande un identifiant **stable, vérifiable, résistant à l'usurpation et
révocable**, c'est-à-dire quelque chose que le mécanisme **produit**. Le mécanisme documenté **ne
répond pas** : ce que F-71 établit est l'évaluation d'une politique contre des invocations de
méthodes, **non** une émission, une vérification cryptographique ou une révocation. ⚠ **Ce verdict
est un constat de répartition des rôles, non un défaut** : l'émission est l'objet du Livre II, et le
maillage n'a jamais prétendu s'en charger. ⚠ **Et il est falsifiable** : une entrée établissant qu'un
maillage émet, vérifie ou révoque un identifiant le renverse.

**Q-B — qui t'a créé ?** *Case vide, degré 3.* **Le socle ne documente pas ce qu'un maillage établit
de la chaîne de provenance d'un agent ni de son ancrage de confiance** — absence de documentation, non
fait négatif vérifié. L'ancrage est le verrou que le **ch. 15** a localisé pour la carte signée et que
le **ch. 9** a retrouvé du côté du courtage ; rien du lot d'instruction ne le reprend.

**Q-C — pour qui agis-tu ?** *Case vide, degré 3.* Q-C exige une chaîne de mandat **interrogeable à
l'instant *t***. ⚠ **Aucun fait négatif ne se dérive de l'énumération des champs de F-71** : le
contrôle de bornage a retiré la clause d'exclusivité, et la liste est **explicitement non
exhaustive** — écrire que la politique ne porterait aucun attribut de mandat **restaurerait la clause
que le contrôle a supprimée**. Ce qui est déclaré est l'état de la preuve, et rien d'autre. Le § 37.8
instruit ce que le maillage peut en tracer ; le **ch. 17** formule la question de recherche que le
Livre II laisse ouverte.

**Q-D — que peux-tu faire ?** **Répond partiellement**, et c'est la seule question sur laquelle le
socle porte un élément positif. Le mécanisme documenté **est** un point de passage, et il y évalue des
règles écrites contre des invocations de méthodes (F-71, **[B]**). **Trois réserves bornent le
partiel.** *Un* : c'est ce que la documentation **décrit**, non ce qu'une mise en œuvre démontre
(R-02). *Deux* : la publication la plus récente est **pré-version** (F-70) — *une syntaxe
pré-version n'est pas un contrat stable* (R-09). *Trois* : **la couverture d'un graphe entier
d'arêtes n'est établie par aucune entrée**, et la réserve de couverture mobilisée ici vient d'un autre
dossier — l'écart déclaré par **Microsoft** entre ses deux plans d'identité d'agent (Vol. III
**F-35**, **[A]**, fait négatif **ÉTABLI**, degré 2), repris au § 37.5.

**Q-E — qui en répond ?** *Case vide, degré 3.* **Le socle ne documente pas ce qu'un maillage produit
d'imputabilité traçable jusqu'à une personne ou une entité juridique.** La question est instruite
ailleurs — par le droit au **Livre III**, et par la trace aux **ch. 38** et **ch. 39**.

| | Q-A *qui es-tu* | Q-B *qui t'a créé* | Q-C *pour qui agis-tu* | Q-D *que peux-tu faire* | Q-E *qui en répond* |
|---|---|---|---|---|---|
| **Autorisation par arête** (mécanisme documenté par F-71) | **ne répond pas** — évaluation d'une politique, non production, vérification ni révocation d'un identifiant | *case vide, degré 3* | *case vide, degré 3* — l'énumération des champs est **non exhaustive** : aucun négatif ne s'en dérive | **partiellement** — bornes explicites au point de passage ; documentation et non démonstration, mécanisme **pré-version**, couverture du graphe non établie (F-70, F-71) | *case vide, degré 3* |

: Tableau 37.2 — Application de la grille du ch. 14 au mécanisme d'autorisation par arête, au 21 juillet 2026. Toutes les entrées citées appartiennent au socle du Vol. III.

**Décompte re-mesuré sur le tableau : deux verdicts rendus sur cinq cases** — un « ne répond pas », un
« répond partiellement » — **et trois cases où le corpus consulté est muet**. Le mécanisme ne répond
**complètement à aucune** des cinq questions ; ⚠ **cela ne confirme pas la thèse du ch. 14 et ne la
réfute pas** : sa portée est bornée aux trois mécanismes que son § 14.2 nomme, et ce mécanisme-ci
n'en est pas.

**Ce que l'application ajoute est d'un autre ordre, et c'est le résultat du chapitre.** Elle montre
que le maillage **déplace** les questions plutôt qu'il n'y répond : il n'ajoute de réponse propre que
sur Q-D, et sur les quatre autres **il évalue sans produire**. ⚠ **La formule plus large « il consomme
ce que l'émission a produit » n'est pas écrite ici** : elle s'appuierait sur un élément hors socle, et
le constat tient sans elle.

⚠ **Et il faut nommer ce que le maillage ne vérifie pas, parce que c'est le pivot du Livre.** **Le
passeport d'agent ne figure dans aucune spécification à date : c'est un objet de synthèse construit
par la somme** en assemblant carte signée, inscription au registre, chaîne de mandat et attestations
(R-01 du Vol. III ; siège **ch. 16**). **Aucune entrée n'établit qu'un maillage vérifie un tel
objet**, et ce chapitre n'en dérive rien. Ce qu'il vérifie, à ce jour et dans le corpus ouvert, est
une politique d'autorisation ; ce qu'il transporte n'est documenté par aucune entrée ; **ce qu'il
ignore est tout ce que les cases vides déclarent.**

---

# Second mouvement — Le maillage comme point d'application : PEP/PDP et *zero trust* agentique

*Ancien ch. 42 du plan (décision 11 du TOC). Entrée conservée intégralement.*

Lecture de l'auteur — **marquage porté à l'ouverture du mouvement, sa thèse étant une construction de
la somme.** **Ce que le socle établit** : qu'une autorisation par arête possède une syntaxe
documentée dans un mécanisme ouvert (F-71, **[B]**), dont la publication la plus récente est signalée
pré-version (F-70, **[B]**) ; qu'un écart de couverture entre deux plans d'identité est déclaré par
l'éditeur lui-même (F-35, **[A, degré 2]**) ; que le socle normatif du *zero trust* date d'août 2020
et que sa déclinaison agentique est un document de concept à l'état de projet public initial (F-73,
**[B]**). **Ce qu'il n'établit pas** : qu'un maillage vérifie un passeport, ni qu'un dispositif de ce
type couvre l'ensemble des arêtes d'un graphe, ni qu'un moteur de politique généraliste y soit
raccordé. *Rendre le passeport opposable est ce que ce mouvement propose ; ce n'est pas ce qu'il
constate.*

⚠ **Une convention de vocabulaire, posée avant la première affirmation parce qu'elle n'est adossée à
aucune entrée.** Le couple **point d'application de politique** (*policy enforcement point*, PEP) et
**point de décision de politique** (*policy decision point*, PDP) est employé ici comme **vocabulaire
de travail**. **Le socle ne documente pas la définition normative de ces deux termes** — absence de
documentation, non fait négatif vérifié : l'entrée qui porte le socle normatif du *zero trust* verse
deux propositions et **ne verse ni l'un ni l'autre sigle**.

## § 37.5 — PEP et PDP agentiques : où se prend et où s'applique la décision d'autorisation

Une politique d'autorisation suppose trois choses : **un endroit où la décision se prend**, **un
endroit où elle s'applique**, et **un vocabulaire dans lequel elle s'écrit**. Le socle documente le
troisième sur **un** mécanisme ; il ne caractérise les deux premiers que par le **statut** des
dispositifs qui les instancieraient, et laisse le reste hors de son corpus.

### 37.5.1 Le vocabulaire existe, et il est borné

Le mandataire d'infrastructure ouvert du § 37.2 spécifie une politique d'autorisation **propre au
protocole MCP**, écrite en CEL, évaluée contre des invocations de méthodes et exposant des champs
d'outil, d'invite et de ressource (Vol. III **F-71**, **[B]**). Les **trois bornes du § 37.2.2 valent
ici sans être reprises** : documentation et non démonstration (R-02) ; **pré-version** (R-09) ;
énumération non exhaustive.

⚠ **Une quatrième borne est propre à cette section, et elle est de portée** : la politique est
**propre à MCP**, et le relevé **ne dit rien de ce qu'elle ferait d'un échange conduit sous un autre
protocole** — A2A, notamment, dont le § 37.2.3 vient d'établir qu'il normalise le chemin de découverte
sans prescrire d'API de registre.

### 37.5.2 Ce que le socle ne porte pas ici est aussi net que ce qu'il porte

**Aucune entrée ne rattache un moteur de politique généraliste à une passerelle d'agents.** Le
rapport du lot est explicite sur ce point et sur sa raison : un moteur de politique déclaratif de
fondation a été vérifié comme projet **gradué depuis le 29 janvier 2021**, mais **aucun lien
documentaire entre ce moteur et une passerelle MCP n'a été ouvert**, et rien n'en est affirmé —
*relevé hors socle, cité comme tel, non versé*. Le volet d'autorisation externe par politique
déclarative d'une offre commerciale n'a pas davantage été ouvert. **Le lien entre un PDP généraliste
et un PEP agentique n'est donc pas documenté par le socle** : absence de documentation, non fait
négatif vérifié (R-14, degré 3).

⚠ **Et cette absence est celle que la somme rencontre au moment exact où l'encadrement devrait
devenir opposable.** Le Livre III produit des *frames* normatifs ; ce chapitre produit un point
d'application ; **rien au socle ne documente le langage dans lequel les premiers s'écrivent pour être
évalués par le second**. *Un PDP sans langage de décision est une architecture sans instrument.* Le
plan porte une **relève** sur ce point — un langage déclaratif de politique, inspiré de Datalog et
étendu aux documents structurés — mais **elle n'entre pas au socle** : elle est un **repérage [C] à
instruire à la source primaire**, et son instruction relève de **G-1**, non de ce chapitre.

### 37.5.3 Le point d'application, quand il existe, peut ne pas couvrir ce qu'on croit

**Le fait le plus instructif de cette section ne vient pas d'une passerelle mais d'un annuaire, et il
est versé au plus haut niveau du Vol. III.** La documentation de **Microsoft Entra Agent ID** porte
une **réserve explicite d'absence de couverture entre les deux plans d'identité d'agent** : une
politique d'accès conditionnel ciblant des identités d'agent **ne s'applique pas** au compte
d'utilisateur de l'agent, et une politique ciblant « tous les utilisateurs » **n'inclut pas** les
identités d'agent (Vol. III **F-35**, **[A, degré 2]**).

⚠ **Le degré compte** : l'absence est énoncée par l'éditeur dans **sa propre liste des configurations
non prises en charge** — **fait négatif ÉTABLI**, non vérifié par balayage. Le **ch. 15** en tire la
qualification que ce chapitre reprend sans l'élargir : c'est un **écart de point d'application**, non
une nuance de licence. *Un identifiant qui n'est pas unique au point d'application ne répond qu'à
moitié à « qui es-tu » — et une politique qui n'atteint qu'un plan sur deux n'oppose qu'à moitié.*

Un second constat de la même famille est consigné **hors socle** : d'après sa page de documentation,
un service de gestion d'API du **même éditeur** déclare prendre en charge les **outils** MCP mais
**ni les ressources ni les invites**, et exclure ces capacités de ses espaces de travail — *relevé
hors socle, source primaire nommée et datée, non versée*. ⚠ **Il va dans le même sens sans constituer
une corroboration indépendante** — même éditeur, autre produit —, et **aucun verdict ne s'y adosse**.

### 37.5.4 Ce que le point d'application devrait lire, et que rien ne le documente lisant

Les bornes de privilège d'un agent sont **déclarées ailleurs**. Un brouillon de laboratoire range
`toolAccessList` — qui énumère les outils et serveurs invocables — et `permissionBoundaries` — qui
porte les limites de portée — parmi les **champs obligatoires** de son schéma de profil d'agent
(Vol. III **F-40**, **[B]**), le périmètre de ce brouillon étant celui d'un document de laboratoire et
**non d'une norme ratifiée** (Vol. III **H-03**, **[A, statut BROUILLON]** ; R-09). Le protocole A2A,
lui, normalise la découverte et **déclare qu'aucune API de registre n'est prescrite** (F-43,
**[B, degré 2]**).

**Déclarer une borne et l'opposer sont deux actes distincts** — la distinction a son siège au
**ch. 14 § 14.2**, et le **ch. 16** l'a renvoyée ici. Le premier acte a un siège documenté ; le second
aurait besoin que le point d'application **sache où lire le premier**. ⚠ **Le socle ne documente aucun
mécanisme par lequel un point d'application agentique lirait les bornes de privilège déclarées au
registre** : absence de documentation, non fait négatif vérifié (R-14, degré 3).

Lecture de l'auteur — **ce que le socle établit** : une syntaxe d'autorisation par arête, documentaire
et bornée à un protocole (F-71) ; trois statuts d'offre, **tous auto-déclarés** (F-70) ; un écart de
couverture entre deux plans d'identité chez un éditeur nommé (F-35). **Ce qu'il n'établit pas** :
qu'un PEP couvre l'ensemble des arêtes d'un graphe, ni qu'un PDP généraliste s'y raccorde, ni qu'un
point d'application lise les bornes qu'un registre déclare. La lecture proposée est que **la question
opérante n'est pas l'existence d'un point d'application, mais sa couverture** : *un dispositif dont on
ne peut pas énumérer les arêtes qu'il ne médiatise pas ne fournit pas d'opposabilité — il fournit une
opposabilité partielle dont le complément est inconnu.* Elle se réfute par la production d'un relevé
de couverture, et **le socle n'en porte aucun**.

## § 37.6 — Garde-fous d'exécution au grain de l'arête

⚠ **Partage déclaré avec le ch. 6, et il est déclaré aux deux bouts.** Le ch. 6 § 6.5 **pose** les
référentiels, les patrons de défense architecturale et les garde-fous d'exécution ; **ce chapitre les
applique au grain de l'infrastructure**, et **ne les reconstruit pas**. *Le modèle de menace et les
vecteurs d'attaque ne sont ni là ni ici : ils sont au ch. 19, en entier.*

**Ce que l'arête permet, et que le composant ne permettait pas.** Les patrons posés au ch. 6 cherchent
tous à rétablir une **séparation de privilège hors du modèle** — un modèle privilégié qui ne voit
jamais le contenu non fiable, un interpréteur qui extrait le flux de contrôle et de données pour lui
appliquer des politiques explicites, une règle de non-cumul bornant à deux les trois propriétés
dangereuses d'une même session. **Trois de ces patrons présupposent un endroit où l'invariant
s'évalue**, et le chapitre présent nomme cet endroit : *un dispositif que toute interaction traverse
est structurellement le lieu où un invariant de non-cumul devient vérifiable ailleurs que dans le
code de l'agent.*

Lecture de l'auteur — **ce que le socle établit** : l'existence de ces patrons et de leurs invariants,
au régime **[C]** du Vol. I ; l'existence d'une syntaxe d'autorisation évaluée à l'arête (F-71,
**[B]**). **Ce qu'il n'établit pas** : qu'un maillage évalue effectivement l'un de ces invariants —
⚠ **aucune entrée ne met les deux en rapport**, et la liste des champs exposés par la seule syntaxe
ouverte ne comporte rien qui désigne une session, une provenance de contenu ou un niveau de confiance.
*L'arête est le lieu où ces invariants pourraient s'évaluer ; qu'un dispositif les y évalue n'est
documenté nulle part.*

**Ce que le grain de l'arête ne change pas, en revanche, est le point cardinal du ch. 6, et il se
répète ici parce qu'il se perd vite.** Ces garde-fous sont des **mesures de réduction de risque dont
l'efficacité est partielle et mesurable** : le patron d'extraction du flux de contrôle ne résout
par construction qu'environ **deux tiers** des scénarios de son banc d'évaluation — **proportion
indicative, dépendante du banc, attribuée à Debenedetti et coll. (2025), qui la rapportent sur le
banc AgentDojo**, comme le **ch. 6 § 6.5** l'écrit et sans que ce chapitre l'y reconstruise —, et la
règle de non-cumul ne vaut qu'à **l'intérieur d'une session**, sans protéger contre une attaque
répartie sur plusieurs. ⚠ **Déplacer ces garde-fous à l'arête ne relève aucune de ces deux bornes** :
une couche imparfaite évaluée à un meilleur endroit reste une couche imparfaite. *La défense en
profondeur empile des couches insuffisantes précisément parce qu'aucune ne suffit* — et c'est la raison pour laquelle **aucune
action irréversible ne dépend d'une seule couche**, principe posé au ch. 6 et instancié au ch. 45.

**La chaîne d'approvisionnement des outils appelle ses propres contrôles** — vérification de
provenance, épinglage de version, **admission par passerelle**. ⚠ **Le troisième est le seul qui
relève de ce chapitre**, et il se borne : la passerelle admet ce qui se présente, elle ne dit rien de
**ce qui l'a produit**. La **barrière de certification** qui décide de ce qui *peut* se présenter est
au **ch. 41 § 41.4** ; la **provenance des composants** est au **ch. 47**. *Ni l'une ni l'autre n'est
reconstruite ici*, et le ch. 41 relève par ailleurs d'un régime de preuve que ce chapitre n'a pas
(matière neuve, risque 16 du TOC).

⚠ **Traitement défensif, au niveau architectural** (R-12 du Vol. III) : ce paragraphe expose des
**mécaniques**, jamais une recette d'exploitation, et aucune configuration reproductible n'y figure.
⚠ **R-13 du Vol. III** : aucune échelle d'autonomie n'est nommée nue dans cette section — la seule
mention de graduation renvoie au **ch. 43 § 43.5**, où les trois échelles homonymes du Vol. I sont
distinguées par leur cardinal et leur numérotation.

## § 37.7 — *Zero trust* transposé : de « jamais confiance au réseau » à « jamais confiance au graphe »

**Le socle normatif est ancien, et le chapitre s'appuie dessus plutôt qu'il ne l'excuse.** Le
document de référence de l'architecture de confiance zéro, publié en **août 2020**, pose que
l'authentification et l'autorisation — du sujet comme de l'appareil — sont des **fonctions discrètes
exécutées avant l'établissement d'une session** vers une ressource d'entreprise, et que **la
protection porte sur les ressources et non sur les segments de réseau** (Vol. III **F-73**, **[B]**).

**Ces deux propositions sont exactement ce que la transposition reprend** : la seconde déplace la
frontière hors du périmètre réseau, la première fait de la vérification **un préalable et non un
acquis**. ⚠ **Et la borne est portée par le lot lui-même** : ce document est de 2020 et **ne traite
pas des agents logiciels autonomes** ; toute transposition agentique est une **construction
d'auteur**, non un contenu de ce document.

⚠ **Le socle pré-agentique du *zero trust* reste au ch. 3 § 3.3 et n'est pas reconstruit ici** :
c'est le siège du socle IAM pour toute la somme, et ce chapitre n'en reprend que ce que la
transposition mobilise.

**La déclinaison agentique existe comme document et non comme norme.** Le document consacré à
l'identité et à l'autorisation des agents logiciels et d'IA, publié le **5 février 2026**, est un
document de concept à l'état de **projet public initial** (*Initial Public Draft*), la clôture des
commentaires étant portée au **2 avril 2026** (Vol. III **F-73**, **[B]** ; R-09, statut dit à chaque
mention). ⚠ **Jalons « visés », jamais « fixés »** (R-11 du Vol. III), et le statut du document se
porte à chaque mention.

⚠ **Le tri prospectif ne porte pas sur l'existence du document**, qui est un **fait constaté et
daté**, mais sur ce que ce document annonce (Vol. III **H-33**, **[C]**, instrument de méthode et non
fait). ⚠ **Les trois statuts du tri — PROGRAMMÉ, PROJETÉ, SPÉCULATIF — ne sont pas définis ici : leur
siège pour toute la somme est au ch. 49 § 49.0**, et ce chapitre s'y **renvoie sans le reconstruire**.
Le tri du rapport de lot classe la prospective en **PROJETÉ** — le document annonce l'intention
de lancer un projet de démonstration, **sans engagement daté de livraison constaté**. L'aboutissement
en spécification demeure **SPÉCULATIF**, aucune source ouverte ne portant de jalon en ce sens. ⚠ **La
thèse du Vol. III écrit pour sa part « la transposition est PROGRAMMÉE pour le document » : l'écart
entre ce tri et celui du rapport de lot est hérité, déclaré chez sa source, et non tranché ici.**

**Ce que la transposition emprunte au Vol. I est une thèse, et elle s'attribue.** L'architecture de
solutions du Vol. I traite la plateforme d'agents non comme un dispositif à gouverner après coup mais
comme un **plan de contrôle obligatoire** couplé à une dorsale d'intégration, et en résume la logique
en une phrase : *l'agent prépare ; un humain ou un contrôle déterministe engage l'irréversible ; toute
action transite par un point d'application de politique unique ; tout actif décisionnel est un modèle
inventorié* (Vol. III **H-30**, **[C]**). ⚠ **Entrée de repérage, thèse d'un volume antérieur, datée
de son gel de juin 2026 et attribuée à lui : elle ne porte aucun fait central de ce chapitre**, et le
Vol. I l'instancie ailleurs sur des produits nommés, **instanciation que la somme ne reprend pas — le
principe seul**. ⚠ **Qualificatif obligatoire** : « plan de contrôle **obligatoire** » est le syntagme
du Vol. I ; le « plan de contrôle » de ce chapitre est celui **au sens infrastructure**. Les quatre
branches de la collision siègent au **ch. 7 § 7.5** ; *le Vol. III signale un emploi supplémentaire
que sa propre table ne range dans aucune branche, et il ne l'y agrège pas d'autorité — la somme fait
de même.*

**Le moindre privilège par délégation est la seconde moitié de la transposition, et le socle en donne
la condition sans en donner le mécanisme.** Un référentiel de sécurité applicative énonce que, sans
identité propre et gouvernée, un agent opère dans un **écart d'attribution qui rend le moindre
privilège inapplicable** — « Without a distinct, governed identity of its own, an agent operates in an
attribution gap that makes enforcing true least privilege impossible » (Vol. III **F-19**, **[A]**) ;
un référentiel de techniques adverses pose le plafond correspondant — **un agent agissant pour un
utilisateur ne doit pas recevoir de permissions que cet utilisateur n'a pas** (Vol. III **F-15**,
**[A]**). ⚠ **Prescription de configuration, non mécanisme démontré** : ces deux entrées énoncent une
**condition d'atténuation** et **ne décrivent aucun dispositif qui l'appliquerait**.

Lecture de l'auteur — **ce que le socle établit** : deux propositions d'un document d'août 2020
(F-73) ; le statut pré-normatif de sa déclinaison agentique (F-73) ; l'écart d'attribution (F-19) ; le
plafond de privilège (F-15) ; le caractère **facultatif** de la signature des cartes et
**recommandé** de leur vérification (Vol. III **F-04**, **[A]** — siège **ch. 15**). **Ce qu'il
n'établit pas** : que « jamais confiance au graphe » soit une propriété d'un maillage déployé, ni
qu'un dispositif quelconque réalise la vérification continue que F-20 nomme. La lecture proposée est
que la transposition est **régulière au sens de son texte d'origine** — *un document qui pose la
vérification en fonction discrète préalable se transpose sans distorsion à des arêtes plutôt qu'à des
sessions* — **et non attestée au sens du terrain**. ⚠ *Les deux énoncés se tiennent ensemble ; les
confondre serait présenter un principe comme un relevé.*

**Enfin, ce que la transposition doit suppléer est daté et borné.** Une chaîne conforme au protocole
A2A peut ne comporter **aucune signature apposée ni aucune vérification effectuée** : les cartes
**MAY** être signées, les clients **SHOULD** vérifier au moins une signature avant d'accorder
confiance (F-04, **[A]**). *Une posture qui refuse la confiance héritée de la topologie doit donc
fournir elle-même, à chaque arête, ce que le protocole rend facultatif.*

## § 37.8 — Le maillage et la chaîne de mandat protocolaire

Le **ch. 17** a localisé la frontière : elle ne passe pas à un rang numéroté de sauts, mais **au
premier changement de régime** — lorsque le vérificateur cesse d'être celui qui a ancré le mandat, ou
cesse d'appartenir au domaine où le contexte se propage. La question de cette section est étroite et
se pose au point d'application : **que voit-il de cette chaîne, et que peut-il en produire ?**

### 37.8.1 Ce qu'il voit est énumérable, et l'énumération est le résultat

Les champs que la seule syntaxe d'autorisation par arête ouverte par le Vol. III expose sont ceux
d'une **invocation** : outil, invite, ressource (F-71, **[B]**).

Lecture de l'auteur — **ce que le socle établit** : ces trois catégories de champs, telles que la
documentation du mandataire les décrit. **Ce qu'il n'établit pas** : qu'un champ quelconque de cette
politique **désigne une position dans une chaîne de délégation**. La lecture proposée est qu'un point
d'application qui évalue **ce qui est invoqué** évalue l'**action demandée à cette arête**, et que
rien dans le relevé n'expose **le mandant d'origine ni la portée qu'il a consentie**. Le **ch. 17**
pose de son côté que porter une identité et porter un mandat sont **deux objets qui se vérifient
séparément**, et que l'un ne se déduit pas de l'autre ; *ce que la politique relevée expose n'est ni
l'un ni l'autre.*

### 37.8.2 Ce qu'il ne peut pas suppléer se lit sur trois entrées, et aucune ne dépend du maillage

*Premièrement* — **le mécanisme de propagation borne lui-même son périmètre**. Ce que le socle
établit de lui est son **statut et sa date** : la spécification de jetons de transaction est à sa
révision **-09 du 6 juillet 2026**, expirant le **7 janvier 2027**, à l'état de dernier appel de son
groupe de travail — ***Internet-Draft* en cours, non un RFC** (Vol. III **F-29**, **[A]** ; R-09). La
**clause de périmètre**, elle, est une source primaire citée **hors socle** : la propagation vaut « …
throughout the Call Chain **within a trusted domain** … ». **Le mécanisme borne donc lui-même sa
portée à un domaine de confiance** — frontière que l'entreprise franchit **dès qu'un agent tiers entre
en jeu**.

*Deuxièmement* — **le mécanisme qui nomme la délégation décline le jeton qui la porte**. Le RFC 8693
définit en sa §4.1 l'attribut `act` comme le moyen d'exprimer qu'une délégation a eu lieu et
d'identifier la partie agissante, et place explicitement **hors périmètre**, en sa §1, la syntaxe, la
sémantique et les caractéristiques de sécurité des jetons eux-mêmes (Vol. III **F-47**, **[A]**).
⚠ **Le ch. 17 § 17.1 a repris cette spécification à la source primaire au titre de G-1, et
l'extraction rapporte plus que la relève n'annonçait** : la spécification **exclut** les maillons
antérieurs de toute décision d'autorisation. *Le renvoi se fait au ch. 17, qui en est le siège ; ce
chapitre n'en reconstruit pas l'extraction.*

*Troisièmement* — **le format de mandat spécifié laisse au déploiement ce dont un vérificateur aval
aurait besoin** : deux types sérialisés en SD-JWT, attribut de type versionné, attributs temporels,
version **v0.2.0 du 28 avril 2026**, **spécification de projet et non texte normatif d'un organisme de
normalisation** (Vol. III **F-46**, **[B]** ; R-09).

**Un point d'application ne crée pas une chaîne que le protocole ne transporte pas.**

### 37.8.3 La fraîcheur est le second manque, et il est du même ordre

La section pertinente de la spécification A2A v1.0.0 **ne mentionne ni liste de révocation, ni
répondeur de statut, ni chaîne de certificats, ni délai de re-validation**, et sa procédure de
vérification en six étapes ne comporte **aucune étape de contrôle de statut ou de fraîcheur**
(Vol. III **F-06**, **[A, degré 1]**) — ⚠ **fait négatif VÉRIFIÉ, borné au balayage de cette seule
section** ; le même texte pose pourtant, au niveau normatif le plus fort, que **les clés expirées ou
révoquées MUST NOT servir à la vérification** (Vol. III **F-07**, **[A]**).

⚠ **Le précédent des infrastructures à clés publiques n'offre pas le secours qu'on lui prête** :
l'invalidation des jetons d'accès n'y est qu'une **recommandation**, la granularité d'une liste de
révocation est **bornée à sa période d'émission**, et l'état « good » d'un répondeur **ne signifie pas
nécessairement qu'un certificat ait jamais été émis** (Vol. III **F-53**, **[B]**). La propagation
d'un retrait le long d'une chaîne est traitée au **ch. 20**, qui l'écrit au **degré 3** et **ne la
comble pas**.

**Un point d'application ne peut pas vérifier une fraîcheur dont aucun mécanisme ne lui fournit le
moyen.**

### 37.8.4 Ce qu'il peut produire, en revanche, est une trace

**C'est le seul apport que ce chapitre revendique de son propre chef, et deux thèses y convergent —
toutes deux attribuées.** Le Vol. II range parmi ses cinq **points de contrôle obligatoires** que la
**trace d'instance soit produite par le cadre** et non par l'agent (Vol. III **H-15**, construction
d'auteur du Vol. II, **sans niveau ni F-xx** ; siège **ch. 43 § 43.3**). Un manifeste de recherche sur
l'encadrement de l'orchestration enseigne de son côté que **la journalisation confiée aux agents
« n'est généralement pas recommandée »** (Vol. III **H-12**, **[B]**) — ⚠ **préimpression non révisée
par les pairs, source unique, sans reproduction indépendante**, réserve que le socle porte
expressément.

Lecture de l'auteur — **ce que le socle établit** : ces deux énoncés, l'un comme thèse d'un volume
antérieur, l'autre comme recommandation graduée d'une préimpression. **Ce qu'il n'établit pas** :
qu'un point d'application par arête soit le cadre qu'ils appellent, ni qu'une trace ainsi produite
soit **corrélable** à une chaîne de mandat. La lecture proposée est qu'un dispositif que toute
interaction traverse est **structurellement** un producteur de trace **non délégué à l'observé** —
*propriété d'emplacement, non de qualité* —, et elle se réfute par la production d'un maillage dont la
trace est fournie par les agents.

⚠ **La clé de jointure manque, et elle manque au socle, pas à ce chapitre.** Par quelle clé
documentée une trace produite au point d'application se rattache-t-elle au **mandat qui autorisait
l'action tracée** ? **Aucune passe de recherche n'a été conduite** sur ce point : absence de
documentation, non fait négatif vérifié. **Le siège de cette question est au ch. 38 § 38.5**, qui la
traite comme **le chaînon manquant** de l'observabilité — *tracer un appel n'est pas tracer une
délégation*. Ce chapitre ne fait que constater qu'il **produit l'objet dont la corrélation manque**.

**Ce que le maillage ne résout pas tient donc en une phrase, et elle est bornée.** Il **ne crée pas**
la chaîne que les mécanismes ne transportent pas (F-29, F-46, F-47), il **ne vérifie pas** la
fraîcheur dont aucun texte ne lui fournit le moyen (F-06, F-07, F-53), et il **ne corrèle pas** ce que
nulle passe n'a instruit. Ce qu'il déplace, c'est le **lieu de l'échec** : d'un ensemble d'agents qui
se font mutuellement confiance vers **un point unique où l'insuffisance devient visible et
journalisable**. *Déplacer un défaut là où on le voit n'est pas le corriger ; c'est la condition pour
pouvoir en rendre compte* — et c'est aussi ce qui fait du même point une vulnérabilité, objet de la
section suivante.

## § 37.9 — Coûts, latence, complexité, point de défaillance : les conditions qui renverseraient ce chapitre

**Cette section a une fonction et une seule** : la latence, le coût et la topologie d'un maillage
n'entrent dans la somme **qu'au titre des conditions qui renverseraient ce que le chapitre avance**,
jamais comme sujet d'ingénierie. ⚠ **Elles sont à écrire comme telles, non comme réserves de style** :
*un chapitre qui ne peut pas être renversé n'affirme rien.*

**Le coût se déclare avant de se discuter.** **Le socle ne documente aucune mesure de latence, aucun
coût d'exploitation et aucune donnée de disponibilité d'un maillage d'agents** : absence de
documentation, non fait négatif vérifié (R-14, degré 3). Le lot d'instruction n'avait pas cet objet à
son périmètre, et **sept échecs de source** y sont consignés — dont la page produit d'une offre de
maillage, renvoyée en HTTP 404, et la vue d'ensemble d'un service d'annuaire, non récupérée. **Aucune
inférence de coût n'est donc proposée ici**, et l'argument de cette section repose sur des propriétés
**structurelles documentées**, non sur des grandeurs mesurées.

⚠ **Le ch. 1 § 1.3.4 porte, lui, un coût mesuré — et il ne se transpose pas.** Le modèle latéral du
maillage de services fait traverser deux mandataires à chaque saut, ce qui a motivé l'émergence des
plans de données alternatifs. **Ce coût est celui du maillage de services, pas du maillage
d'agents** : le transposer reviendrait à traiter la filiation comme un fait rapporté alors que le
§ 37.1 vient d'établir qu'elle est **posée**. *La grandeur reste au ch. 1, l'analogie ne la
transporte pas.*

**Cinq conditions renverseraient ce que ce chapitre avance, et chacune est traçable.**

| # | Condition | Ce qui l'ancre | Ce qui la rendrait constatable |
|---|---|---|---|
| **1** | **La couverture n'est pas totale, et le complément est inconnu** | écart de couverture entre deux plans d'identité **déclaré par l'éditeur** (**F-35**, [A, degré 2]) ; réserve de couverture MCP d'un service du même éditeur (relevé hors socle) | un **relevé d'arêtes non médiatisées** dans un déploiement donné. ⚠ Si le complément reste inconnu, *une opposabilité partielle de part inconnue ne vaut pas mieux, en dossier de diligence raisonnable, qu'une absence déclarée* |
| **2** | **Le seul mécanisme ouvert n'aboutit pas** | la syntaxe d'autorisation par arête est portée par **un** mécanisme, dont la publication la plus récente est **pré-version** (**F-71**, **F-70**) | l'abandon de la série ou son expiration sans publication stable. Le chapitre perdrait **sa seule syntaxe citable** et n'aurait plus qu'un principe |
| **3** | **Le point d'application unique devient le point de défaillance** | le principe emprunté fait transiter **toute action par un point d'application unique** (**H-30**, [C], thèse attribuée, datée de juin 2026) | une indisponibilité documentée, ou une mesure de disponibilité. ⚠ **Le socle n'en porte aucune** (degré 3) : *la condition est posée, elle n'est pas instruite* |
| **4** | **Il n'y a pas de chaîne à vérifier** | la chaîne de mandat n'est pas établie interrogeable à l'instant *t* (ch. 17) ; la propagation est **bornée à un domaine de confiance** (§ 37.8.2) ; la frontière passe au **premier changement de régime** (ch. 17) | la vérification par arête se réduirait à **l'authentification du porteur immédiat**. Le maillage resterait utile — il ne serait plus le lieu où une chaîne de mandat devient opposable, **et la thèse du second mouvement tomberait** |
| **5** | **Un autre dispositif produit l'opposabilité sans maillage** | la somme n'a instruit **qu'un** lieu d'application, et le déclare (thèse du second mouvement, réalignée) | la documentation d'un mécanisme rendant une chaîne opposable **sans point d'application médian** — par exemple une preuve portée par le mandat lui-même, vérifiable de bout en bout. La thèse ne serait pas fausse : elle serait **non nécessaire**, ce qui suffit à la renverser comme thèse |

: Tableau 37.3 — Les cinq conditions de réfutation du chapitre 37, avec leur ancrage et leur critère de constatation. ⚠ Une condition de réfutation **n'est pas un énoncé sur le futur** : ce tableau ne porte aucun tri prospectif.

⚠ **Trois de ces cinq conditions sont déjà partiellement réalisées, et le chapitre le dit plutôt que
d'attendre qu'on le lui oppose.** La **première** l'est chez un éditeur nommé, au niveau [A] et au
degré 2 (F-35). La **deuxième** l'est au sens du statut : le mécanisme est en pré-version au
21 juillet 2026 (F-70). La **quatrième** l'est au sens du socle : **aucune entrée n'établit
l'interrogeabilité de la chaîne de mandat à l'instant *t***, et les ch. 17 et 20 écrivent au **degré
3** les deux absences voisines — le chaînage d'accréditations pour la délégation, et la révocation en
cascade.

Lecture de l'auteur — **ce que le socle établit** : les cinq ancrages de la colonne centrale, chacun
avec son niveau et sa borne. **Ce qu'il n'établit pas** : que ces cinq conditions **épuisent** les
manières dont la thèse pourrait être fausse, ni qu'elles soient **indépendantes** les unes des autres.
La lecture proposée est que la thèse de ce chapitre est **conditionnelle par construction** : elle
avance qu'un point d'application par arête est le lieu où l'opposabilité d'un mandat *pourrait* se
constituer, et **l'état du socle est que ce lieu existe comme syntaxe, pas comme dispositif attesté**.
⚠ *Un lecteur qui refuse la thèse ne perd aucun des faits cités* — c'est la propriété que R-01 du
Vol. III protège, et elle vaut ici comme au ch. 16.

## Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur, conformément à la
table détaillée du TOC.*

1. **Les deux désambiguïsations du Livre.** « AgentMesh » au sens du **patron d'infrastructure**
   (R-04 branche (f) du Vol. III) ; « plan de contrôle » **jamais nu**, quatre branches au **ch. 7
   § 7.5**. Les **ch. 38 à 46** les appliquent sans les redécider, et **aucun ne reconstruit
   l'encadré**.
2. **La définition du maillage d'agents, et son statut de définition.** Elle est **posée**, non
   héritée : le socle du Vol. III ne documente pas le patron dont elle se réclame. ⚠ **Ce que la
   somme y ajoute est un adossement en [C] par le ch. 1 § 1.3.4** — *une lacune de couverture
   couverte, jamais comblée.*
3. **Le tri par statut, et ce qu'il ne dit pas.** Annonce, feuille de route, préversion,
   disponibilité générale documentée — les quatre statuts du cadrage —, et une **cinquième colonne
   vide**, la production attestée par un tiers. ⚠ **La disponibilité restreinte, seul statut sous
   lequel l'une des trois offres se laisse ranger, n'appartient à aucune des deux nomenclatures
   héritées** (§ 37.2.1) : *l'écart est légué tel quel, il n'est pas tranché ici*. Le **ch. 45**
   instancie un portefeuille réel sous le même régime de statuts datés ; il hérite de cette colonne
   vide.
4. **Le point d'application comme lieu, et la couverture comme question opérante.** Le **ch. 41
   § 41.4** en fait la barrière d'admission d'un parc, le **ch. 43 § 43.3** en fait un point de
   contrôle obligatoire, le **ch. 45 § 45.8** l'instancie à la naissance d'un agent. ⚠ *Aucun ne
   redémontre que la question opérante est la couverture, et non l'existence.*
5. **Le maillage comme producteur de trace non délégué à l'observé.** C'est le seul apport propre du
   chapitre, et il est **d'emplacement, non de qualité**. Le **ch. 38** en reçoit l'objet et **y
   trouve le chaînon manquant** — la corrélation trace ↔ chaîne de mandat.
6. **Les cinq conditions de réfutation.** Elles sont posées ici pour tout le mouvement *appliquer* ;
   le **ch. 41 § 41.6** en écrit l'homologue pour la fabrique, **sous la même exigence** — des
   conditions, pas des réserves de style.

⚠ **Ce que le chapitre ne lègue pas.** Il ne lègue **aucun fait sur le coût, la latence ou la
disponibilité** d'un maillage : le **ch. 40** ne trouvera ici aucune grandeur à reprendre. Il ne lègue
**aucune propriété démontrée** — seulement des syntaxes documentées et des statuts auto-déclarés. Et
il ne lègue **pas la couche d'exécution** : le **harnais** qui héberge la boucle de l'agent **n'a de
chapitre nulle part dans la somme**. ⚠ **D-2 a été prise depuis, et elle borne le risque 14 sans le
combler** — *sections dans l'existant, sans chapitre neuf*, le plafond de cinquante interdisant d'en
ouvrir un sans fusion ; les deux points d'atterrissage reconnus sont le **ch. 47 § 47.8.1** et le
**ch. 50 § 50.2**. ⚠ **Elle l'a été le 27 juillet 2026, par une autre passe et après cette
rédaction** : *ce chapitre a été écrit avant la porte qu'elle conditionne, et l'arbitrage qui a suivi
solde l'infraction sans la rattraper.*

---

## § 37.10 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée, conformément à la règle d'escalade du PRD
(Annexe A) : *un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il **remonte**.*

**Ce qui est enfreint.** Portes **G-3** (refonte du socle, non entamée), **G-4** (collation de fond
contre le Vol. III rédigé, volet de fond dû — *préalable déclaré du premier mouvement de ce Livre*) et
**G-5** (arbitrage du risque 14, décision d'auteur **D-2**, non prise — *porte qui conditionne le
Livre IV entier*) ; **volet résiduel de G-1** non instruit pour ce Livre ; **ordre de rédaction du
PRD §6**, qui place les Livres I et III avant celui-ci et le premier mouvement du Livre IV en
troisième position. Instruction d'auteur du **27 juillet 2026**.

1. **Aucun énoncé n'est central au sens de CA-IV-01 — et le motif a changé sans que la conclusion
   change.** À la rédaction, le socle consolidé comptait **zéro entrée** ; ☑ **il en compte 159
   depuis le 28 juillet 2026**, la porte **G-3 étant franchie** (Annexe B, v1.2). Les identifiants
   cités ici résolvent néanmoins contre les socles **des volumes sources**, préfixés de leur volume
   comme le PRD §6 l'exige, et **le re-ancrage sur la série `S-nnn` reste dû**. ⚠ **La centralité
   n'est pas acquise pour autant** : l'Annexe B se déclare elle-même **constituée et non arbitrée**
   — *aucun vote adversarial n'y a été conduit, aucun énoncé n'y a été confronté à sa source
   primaire* —, et le régime « source rédigée non publiable » (PRD §7.2) exige ce vote sur chaque
   affirmation issue d'une pièce du Vol. III touchée par une remontée ouverte. **Six des quinze
   remontées ouvertes du Vol. III touchent la matière du Livre II ; leur relevé n'a pas été refait
   pour ce Livre-ci.**
2. **Les décomptes sont publiables** (G-2 franchie). Le réel est mesuré par `decompte.sh` et reporté
   au [`README.md`](README.md) du Livre. ⚠ **D-4 s'applique** : l'écart se documente, **l'amputation
   est interdite**.
3. **Les renvois « ch. N » : état FINAL de la passe, et non ordre d'écriture.** ⚠ *La forme
   antérieure de ce point photographiait l'instant où cette pièce a été écrite et déclarait « ne
   sont pas rédigés : ch. 41, ch. 43 et ch. 45 » — alors que **la même passe les a écrits
   ensuite** ; elle est corrigée ici sur l'état que le commit produit.* **Les dix chapitres du
   Livre IV (ch. 37 à 46) sont rédigés**, comme le sont les **cinquante chapitres des cinq
   Livres** : *tous les renvois « ch. N » de cette pièce résolvent donc contre du texte.* ⚠ **Ce
   qui reste vrai de la forme antérieure, et qui est daté** : à l'heure où ce chapitre a été
   écrit, n'étaient rédigés ni le ch. 47 du Livre V, ni les chapitres du Livre III au-delà du ch.
   26, non plus que les ch. 41, ch. 43 et ch. 45 — *les renvois qui les visent ont été posés comme
   renvois de plan et n'ont pas été re-vérifiés contre le texte paru après eux.* ⚠ **Et « résoudre
   contre du texte » ne vaut pas recevabilité** : *le texte visé est lui-même un brouillon hors
   portes.*
4. **Les huit cases vides ou verdicts de degré 3 du § 37.4 et des sections suivantes sont des états
   de preuve, non des verdicts** ; elles se rempliront ou non selon ce que G-3 et G-4 versent, **et
   pas selon ce qu'une relecture jugera plausible**.
5. **CA-IV-13 n'est pas satisfaite** — aucune relecture par un relecteur distinct du rédacteur.
   L'obligation est déclarée insatisfaisable en l'état au PRD §11, **D-6 ne fournissant pas de
   tiers** ; *arbitrer n'est pas relire, et se relire soi-même n'est pas être relu.*

**Remontées ouvertes par ce chapitre — et leur issue, soldée le 27 juillet 2026 :**

⚠ **Chaque remontée porte ci-dessous son issue**, portée là où elle fait foi — au TOC pour un
réalignement de plan, au PRD pour une décision d'auteur ou un domaine de porte, à l'appareil pour une
dette d'outillage. *Le tableau consolidé des trente-deux issues du Livre vit au
[`README.md`](README.md) ; il n'est pas repris ici.* ⚠ **Une remontée close ne rend pas la pièce
recevable** : *elle veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée.*

- **R-IV-38 — non bloquante, de thèse, et déjà tranchée à la source (premier mouvement).** La thèse
  citée porte « cette filiation trie **ce que le terme recouvre réellement de ce qu'il recouvre en
  marketing** ». Le Vol. III déclare expressément, **en coût de sa propre thèse**, qu'elle
  « n'affirme rien de l'écart entre le discours des fournisseurs et leurs réalisations ; elle affirme
  un tri par statut, sur cinq offres nommées ». La thèse du plan **affirme donc exactement l'énoncé
  que sa source déclare ne pas faire**. S'y ajoute que la source écrit « le présent ouvrage
  **définit** » là où le plan écrit « le maillage **est** » — *une définition posée présentée comme un
  constat*. **Demande remontée** : réalignement au titre des **décisions 8 et 14** du TOC. ⚠ **Ce
  n'est pas une divergence à arbitrer, c'est un report qui n'a pas été fait.**
  ☑ **Issue, 27 juillet 2026** — **TOC, décisions 8 et 14** — thèse réalignée : la source
  **définit** par filiation, elle n'affirme pas que le maillage **est** une réinstanciation ; ⚠
  **et le membre « ce qu'il recouvre réellement / en marketing » tombe** — *la source déclare en
  coût de sa thèse qu'elle n'affirme rien de cet écart*. **La citation en tête de cette pièce
  porte la forme réalignée** (décision 17 du TOC).
- **R-IV-39 — non bloquante, de thèse, et déjà tranchée à la source (second mouvement).** La thèse
  citée porte « le maillage **est le** lieu où le passeport du ch. 16 **devient** opposable ». Le
  Vol. III a **reformulé cette thèse le 21 juillet 2026** (confrontation P4.0, écarts ÉC-05 à ÉC-07)
  en « **un** lieu où le passeport […] **pourrait** devenir opposable, et le seul que cet ouvrage
  instruise », et y a ajouté que « vérifier chaque arête » est un **principe d'architecture posé par
  l'ouvrage, non une propriété relevée d'un maillage déployé**. Le TOC porte encore l'article défini
  et l'indicatif. **Demande remontée** : réalignement au titre des **décisions 8 et 14**.
  ☑ **Issue, 27 juillet 2026** — **TOC, décisions 8 et 14** — « **le** lieu où le passeport
  **devient** opposable » devient « **un** lieu où il **pourrait** le devenir, et le seul que
  l'ouvrage instruise » ; *report que la source avait fait le 21 juill. 2026 et que le plan
  n'avait pas suivi*. **La citation en tête de cette pièce porte la forme réalignée** (décision
  17 du TOC).
- **R-IV-40 — BLOQUANTE pour le Livre IV entier, de gouvernance.** La porte **G-5** conditionne
  « Livre IV et premier mouvement du Livre V » (PRD §5) : l'arbitrage du **risque 14** — la couche
  d'exécution, le harnais — est une décision d'auteur (**D-2**) **non prise**. Ce chapitre a été
  rédigé malgré cela, sur instruction d'auteur, et **le § 37.6 est le lieu exact où le manque se
  voit** : la chaîne d'approvisionnement des outils appelle une admission par passerelle, mais *ce
  qui exécute effectivement l'appel après l'admission n'est traité par aucun chapitre*. **Demande
  remontée** : que **D-2 soit prise** — chapitre neuf sous plafond, sections dans l'existant, ou
  périmètre assumé et déclaré. ⚠ **La règle d'escalade veut qu'une remontée bloquante interdise de
  lancer le chapitre qu'elle bloque** : elle est ouverte **après** la rédaction, non avant, et
  *l'infraction est consignée plutôt que rattrapée par l'arbitrage qui la suivra*.
  ☑ **Issue, 27 juillet 2026** — **close sur constat — D-2 EST PRISE**, *sections dans l'existant,
  sans chapitre neuf*, le plafond de cinquante interdisant d'en ouvrir un sans fusion. ⚠ **Mais
  elle l'a été par une AUTRE passe et APRÈS cette rédaction** : *le Livre a été écrit avant G-5,
  et l'arbitrage ne rattrape pas l'infraction — il la solde.*
- **R-IV-41 — non bloquante, de cardinal hérité.** Le Vol. III porte **trois écarts non résolus** sur
  le tri des statuts (§ 37.2.1) : cinq réalisations contre six objets relevés ; la production comme
  « quatrième catégorie » contre « troisième degré » d'un tri à trois ; la **disponibilité
  restreinte**, qui ne figure dans aucune des deux nomenclatures. Les trois sont **déclarés chez leur
  source et non tranchés**. **Demande remontée** : que la **collation de fond (G-4)** les inscrive à
  son domaine, le compendium n'ayant pas à re-trancher un écart de cardinal de son volume source —
  *mais un cardinal hérité non tranché qui traverse une somme y devient un cardinal de la somme.*
  ☑ **Issue, 27 juillet 2026** — **PRD, domaine de G-4** — les trois écarts de cardinal hérités
  (cinq réalisations contre six objets ; quatrième catégorie contre troisième degré ;
  disponibilité restreinte hors nomenclature) entrent au domaine de la collation de fond ; ⚠ *le
  compendium ne re-tranche pas un cardinal de son volume source.*
- **Remontée de relecture, 28 juillet 2026 — non bloquante, d'appareil. ⚠ Sans identifiant alloué,
  et le motif se déclare** : la série `R-IV-nn` est **partagée**, une autre passe y puise au moment
  où celle-ci écrit, et **le PRD §13 interdit d'y puiser sans allocation préalable** — *deux passes
  parallèles y ont déjà alloué dix numéros deux fois.* **Objet** : la porte **G-3 a été franchie le
  28 juillet 2026** et le socle consolidé existe (**159 entrées `S-001`…`S-159`**), alors que cette
  pièce adosse ses énoncés aux socles des **volumes sources**. **Demande remontée** : que le
  **re-ancrage des identifiants sur la série `S-nnn`** soit conduit en **une passe unique sur les
  cinquante pièces**, contre les deux tables de correspondance de l'Annexe B, et non pièce par
  pièce — *cinquante rédacteurs traduisant chacun ses renvois produiraient cinquante conventions.*
  ⚠ **Trois faits de re-datation touchent cette pièce et sont déjà consignés dans son corps** : la
  bascule de révision du § 37.2.4 (`S-001`), le changement de statut du mandataire ouvert au
  § 37.2.1 (`S-116`), et la reconduction telle quelle de la divergence d'un jour du § 37.1.3
  (`S-134`).

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.28** — § 37.1 à
§ 37.9, dans l'ordre exact, les deux mouvements séparés et chacun sous son ancien titre —, *table que
ni la v0.29 ni la v0.30 ne modifient*, et le
§ 37.0 est une introduction de chapitre et de Livre. ⚠ **Une déviation d'intitulé est fondée et se
déclare** (décision 8, reprise en décision 15 alinéa c) : le § 37.9 **allonge** le titre du plan
— « Coûts, latence, complexité, point de défaillance » — de « : les conditions qui renverseraient ce
chapitre », *parce que la section est le lieu des conditions de réfutation et que le plan ne le dit
pas.* Les **deux tables de couverture sont
respectées**, y compris leurs deux régimes propres : Vol. I *Monographie* §1.3.4 en **arrivée**
(déclinaison agentique, le socle transposable restant scindé au ch. 1) et §2.10.3-2.10.4 en **partage
déclaré** avec le ch. 6, *appliqués ici et posés là-bas, sans reconstruction*. Les **coupes de la
source sont reconduites et déclarées** — transport et routage sémantique, coupés au test
d'appartenance du Vol. III, **ne sont pas rétablis** ; la fermeture du chapitre à l'accord entre
agents sous défaillance (**D-7**) est **tenue**, aucune section n'y touchant. Les **deux sièges que
ce chapitre touche sans les reconstruire** portent leur renvoi : l'encadré à quatre branches du
**ch. 7 § 7.5** et le socle IAM du **ch. 3 § 3.2-3.3**. ⚠ **Cardinaux re-mesurés au commit du 28 juillet 2026, sur le marqueur littéral et sur le corps seul** (décision 16 du TOC) ; *les cardinaux antérieurs comptaient les applications du garde-fou et n'étaient re-mesurables par aucune règle écrite.* Les **trois degrés d'absence** portent leur degré **à chaque énoncé négatif du
corps — domaine déclaré, sans cardinal** (alinéa c) ; le marqueur littéral « degré 3 » y compte
**quinze occurrences**, et **aucune n'est écrite comme un fait négatif vérifié**. Les **sept
qualifications auto-déclarées** sont attribuées à leur éditeur **nommé**, à chaque occurrence. Les
**neuf marquages « Lecture de l'auteur » du corps** sont suivis de ce que le socle établit et
n'établit pas — ⚠ *le marqueur compte une dixième occurrence dans le domaine, portée par la thèse du
second mouvement, qui la cite depuis le TOC et n'est donc pas un marquage de cette pièce.* Enfin,
**aucun siège neuf n'est posé par ce chapitre** : il n'ajoute rien à la table `SIEGES` de
[`check-sieges.py`](../PRD/check-sieges.py), et c'est un résultat — *un chapitre
d'application qui poserait un siège aurait probablement reconstruit celui d'un autre.*
