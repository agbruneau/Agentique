# Chapitre 13 — L'identité décentralisée : VC, DID et la promesse du portable

*Livre II — Faire confiance : identité, délégation et fabrique de confiance.
Premier mouvement — émettre (ch. 12-18). Deuxième chapitre du mouvement.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé le 27 juillet 2026 sur instruction d'auteur, portes **G-3** et **G-4** alors ouvertes. ⚠ **G-3 a été franchie depuis, le 28 juillet 2026** (PRD v0.14 ; socle consolidé [`socle-consolide.md`](../PRD/socle-consolide.md) v1.2, **159 entrées `S-001`…`S-159`**) : *une porte franchie après coup ne rend pas recevable la pièce écrite avant elle* — elle lui donne le socle contre lequel se relire, ce que la présente passe a fait. **G-4 demeure ouverte**, et le régime de preuve du Livre II reste celui de la **source rédigée non publiable** (PRD §7.2) : le Vol. III déclare lui-même que « rédigé ne vaut pas publiable ». Détail et remontées en clôture, où **R-IV-16 et R-IV-17, ouvertes au ch. 12, valent pour tout le Livre** et ne sont pas rouvertes |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ☑ **Le volet de faits du volet résiduel de G-1 est levé le 28 juillet 2026** ([`gel-2026-07-28-volet-residuel.md`](../PRD/gel-2026-07-28-volet-residuel.md)) : les entrées de socle mobilisées ici ont été **portées à leur source primaire**, et **quatre verdicts de changement portent sur elles — deux seulement atteignent le texte** : la date du rapport d'interopérabilité du § 13.5 (Vol. III F-31) et le décompte de participants du § 13.3 (Vol. III F-83), l'un et l'autre reportés au corps. ⚠ **Les deux autres changent une composante que ce chapitre ne cite pas** — un décompte de participants sur un groupe que l'entrée ne nomme pas (Vol. III F-50) et la révision du brouillon d'architecture WIMSE (entrée héritée H-18), que le § 13.4 date déjà par Vol. III F-86 ; *ne dénombrer que les verdicts qui atteignent le texte ferait passer un relevé pour une couverture.* La spécification SPIFFE-ID du § 13.4 (Vol. III F-87) est **hors domaine**, sans sensibilité temporelle. ⚠ **Instruire n'est pas confirmer et re-dater n'est pas relire** : aucun niveau n'est promu, aucun énoncé n'est reconfronté à sa source. Gels de source : **juin 2026** (Vol. I), **21 juillet 2026** (Vol. III). ⚠ **Ce chapitre est le plus périssable du mouvement** : **trois des cinq documents dont il relève le stade sont en cours de procédure** — la version 2.1 du modèle de données, la version 1.1 des identifiants décentralisés, le brouillon d'architecture WIMSE —, et l'un d'eux avait dépassé sa propre échéance auto-déclarée dès le relevé |
| **Socle mobilisé** | ☑ **Le socle consolidé existe depuis le 28 juillet 2026** (Annexe B, **159 entrées**), G-3 franchie. ⚠ **La pièce continue néanmoins de citer les identifiants sources préfixés de leur volume**, que les deux tables de correspondance résolvent : *les cinquante pièces n'ont pas été re-citées en `S-nnn`* (PRD §7.1). Résolution contre le **Vol. III *Monographie* ch. 3**, dont les entrées **F-30**, **F-31**, **F-32**, **F-49**, **F-50**, **F-79**, **F-80**, **F-81**, **F-82**, **F-83**, **F-86** et **F-87** conservent leurs niveaux d'origine ; et contre le **Vol. I *Monographie* §3.6.4 et §7.4.3**, en régime **[C]** (PRD §7.1). ⚠ **Trois entrées héritées sont en [C], et leur sort diffère** : **H-18** et **H-20** sont **mobilisées** — elles **situent** l'objet, elles ne le portent pas ; **H-19** est **consultée et non mobilisée**, sa matière — le KYA, la *trust fabric* — siégeant au ch. 18. ⚠ **Aucun énoncé n'est central au sens de CA-IV-01**, et le franchissement de G-3 ne l'a pas changé : **aucun vote adversarial n'a été conduit** et **CA-IV-13 n'est pas satisfaite** |
| **Garde-fous balayés** | ⚠ **Règle de comptage, re-mesurée au commit du 28 juillet 2026** : *un cardinal déclaré ici porte sur le **marqueur littéral** de l'identifiant dans le **corps** — en-tête et note de statut exclus* ; les **applications non marquées** ne se dénombrent pas et relèvent du **domaine balayé**, déclaré sans cardinal. **Domaine balayé : les six sections du corps, § 13.0 à § 13.5.** Vol. III — **R-14 : trois marqueurs**, § 13.0, § 13.4 et § 13.5 ; **R-02 : deux marqueurs**, § 13.0 et § 13.4 ; **R-09 (une charte de groupe n'est pas un standard ; les stades se disent à chaque mention) : un marqueur**, § 13.1 ; la clause de stade est en outre reprise **à chaque mention** sans marqueur, aux § 13.1, § 13.3, § 13.4 et § 13.5 — *couverture déclarée, non dénombrée*. **R-01, R-03 à R-08, R-10 à R-13 : zéro marqueur.** Vol. II — **§8.2 (métriques auto-déclarées) : zéro marqueur** ; les métriques des § 13.3 et § 13.5 sont **attribuées à la page qui les affiche**, sans que le renvoi au garde-fou soit écrit ; **PRD Vol. II §8.2.5 (statuts pré-normatifs) : zéro marqueur** ; les stades pré-normatifs sont portés aux § 13.1 et § 13.3. **R-1 à R-8 : zéro marqueur** |
| **Volumétrie cible** | ≈ **4 000 mots** de corps (§ 13.0 à § 13.5), **cible dérivée** de l'enveloppe du Livre (50 000 mots, TOC v0.30) au prorata des sections. ☑ **Décompte publiable depuis G-2** ; **réel : 4 529 mots** par [`PRD/decompte.sh`](../PRD/decompte.sh) — **+13,2 %**, re-mesuré au commit du 28 juillet 2026 (**3 947 mots à la rédaction**, soit −1,3 % ; **4 358 mots** au terme de la première passe de relecture, soit +9,0 %). ⚠ **L'écart vient des constats de re-datation et des bornes versés au corps par les deux passes de relecture, jamais d'un gonflement** — *rien n'a été amputé pour le contenir, D-4 l'interdisant, et une borne coûte des mots là où une coupe en épargne.* ⚠ **Un écart individuel ne se lit pas seul** : la volumétrie du Livre est relevée pièce par pièce au [`README.md`](README.md) du dossier, et c'est elle qui alimente la **décision d'auteur D-4**, ouverte, par la remontée **R-IV-17** du ch. 12 |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.30, entrée du chapitre 13 — l'entrée ne porte aucune note de réalignement : la collation de la décision 14 n'a rien trouvé à borner ici)* — le corpus W3C (VC, DID) fournit le vocabulaire du « passeport d'agent », mais son adoption en entreprise financière reste à démontrer — la distinction promesse/production est le fil.

---

## § 13.0 — Introduction : un vocabulaire, et la question de savoir qui l'emploie

Le chapitre précédent a montré une pile héritée qui **s'étire** : des RFC écrits pour un humain au
bout du flux, réemployés pour un mandataire logiciel, et des extensions qui n'ont pas encore le
statut de leurs supports. Une autre voie existe, et elle ne procède pas par étirement : le corpus du
**W3C** — accréditations vérifiables (*verifiable credentials*, VC) et identifiants décentralisés
(*decentralized identifiers*, DID) — propose un vocabulaire conçu d'emblée pour des assertions
portables, vérifiables et détachées de l'annuaire qui les a émises.

C'est de ce vocabulaire que la somme tire les mots du **passeport d'agent**. ⚠ **Et c'est tout ce
qu'elle en tire à ce stade** : le Vol. I, qui porte le terme au titre d'une section, **ne le définit
ni ne le réemploie dans le corps de celle-ci** (Vol. III H-18, **[C]**) — et **le socle n'a extrait
aucun contenu des spécifications que ce chapitre relève**, de sorte que ce qu'elles en diraient est
une **absence de documentation, non un fait négatif vérifié**. ⚠ **La borne est celle du corpus
consulté, non celle du domaine, et elle vaut aux deux échelles** : écrire que le terme ne figure dans
aucune spécification de 2026 serait un quantificateur universel négatif sur un corpus non balayé ;
écrire qu'aucune des spécifications relevées ici ne le définit supposerait ouvert le contenu que le
régime de traçabilité posé plus bas déclare non extrait. C'est un **objet de synthèse** que le
**ch. 16** construit en assemblant une carte signée, une inscription au registre, une chaîne de
mandat et des attestations. Le présent chapitre fournit le lexique ; il ne fournit pas l'objet.

**Le fil du chapitre est une distinction, et il faut la poser avant les faits : promesse contre
production.** Un stade de normalisation dit où en est un texte ; il ne dit pas qui l'emploie. Les
deux registres se confondent d'autant plus aisément que le premier est public, daté et facile à
citer, tandis que le second se mesure mal. Le chapitre les tient séparés section par section : les
stades (§ 13.1), une lacune de couverture assumée sur les profils d'interopérabilité (§ 13.2), les
groupes communautaires et ce que leur statut interdit d'en conclure (§ 13.3), l'articulation avec
l'identité de charge de travail (§ 13.4), et le fossé d'adoption tel que le corpus permet de
l'écrire (§ 13.5).

⚠ **Régime de traçabilité, posé d'entrée parce qu'il commande la lecture.** Le lot d'instruction du
Vol. III a ouvert les quatre documents du W3C le 21 juillet 2026 et en a extrait **le stade et sa
date** ; il n'a extrait **ni le modèle de données, ni les mécanismes de preuve, ni les méthodes de
résolution** que ces documents spécifient. *L'état d'origine se conserve ici, au passé* (décision 17c).
**Le socle ne documentait donc pas le contenu technique du *Verifiable Credentials Data Model* ni de
*Decentralized Identifiers* : absence de documentation, non fait négatif vérifié** (R-14 du Vol. III,
degré 3).

☑ ⚠ **EXTRACTION CONDUITE LE 30 JUILLET 2026 (D-11), et elle porte sur les deux Recommandations
elles-mêmes.** L'arbitrage externe relevait qu'un chapitre intitulé « identité décentralisée : VC et
DID » sans son contenu technique n'honore pas son titre. Les deux documents ont été lus à leur source
ce jour.

**Le modèle de données** — *Verifiable Credentials Data Model 2.0*, Recommandation du W3C. Une
accréditation vérifiable conforme **doit** porter quatre propriétés : **`@context`**, dont le premier
élément **doit** être `https://www.w3.org/ns/credentials/v2` ; **`type`**, dont la valeur **doit**
inclure `VerifiableCredential` ; **`issuer`** ; et **`credentialSubject`**. ⚠ **Un document conforme
doit en outre être *sécurisé par au moins un mécanisme de sécurisation***, ce qui n'est pas une
propriété de plus mais une condition de conformité distincte.

**Les mécanismes de preuve, et leur partition est le fait le plus utile de l'extraction.** La
Recommandation en admet **deux familles, non une** : la **preuve incorporée**, portée par la
propriété **`proof`** — dont les exemples portent `type`, `created`, `verificationMethod`,
`cryptosuite` et `proofValue` —, et la **preuve enveloppante**, où l'accréditation est encapsulée
dans un format JOSE ou COSE. ⚠ **Deux familles de preuve pour un même modèle de données signifie que
deux implémentations conformes peuvent être mutuellement illisibles** : *c'est, transposé au niveau
du justificatif, exactement le constat de conformité ≠ interopérabilité du ch. 3 § 3.4.4*, et le
§ 13.2 le retrouvera du côté des profils.

**Le statut, et il n'est pas dans ce document.** La propriété **`credentialStatus`** existe au modèle
de données, mais *la vérification du statut est renvoyée aux spécifications de mécanisme de
sécurisation* et à une spécification distincte de liste d'état. ⚠ **La révocation n'est donc pas
spécifiée par la Recommandation qui définit l'accréditation** — c'est le versant W3C du constat que
le **tableau 20.1** du ch. 20 dresse pour toute la couche.

**Les identifiants décentralisés** — *Decentralized Identifiers v1.1*, **instantané de recommandation
candidate du 5 mars 2026**, dont le document déclare lui-même qu'il *n'est pas attendu au rang de
Recommandation avant le 5 avril 2026*. ⚠ **Une seule propriété y est obligatoire : `id`.**
`controller`, `verificationMethod`, `authentication`, `service` sont **toutes facultatives**.
**La résolution** est confiée à un composant — le résolveur — qui prend un identifiant et rend un
document ; ⚠ ***la résolution d'une méthode donnée est déclarée hors périmètre de la
spécification*** et renvoyée à un document distinct, chaque méthode définissant ses propres
opérations.

⚠ **Trois conséquences, et la troisième est celle qui compte pour la thèse du Livre.** *(1)* **Le
régime de preuve du chapitre s'élève partiellement** : le stade et la date restaient le seul acquis,
le **contenu normatif des deux documents est désormais lu** — mais *lu, non collationné
adversarialement*, et **rien n'entre au socle**, le versement relevant d'une passe de socle. *(2)*
⚠ **Aucune qualification cryptographique n'est tirée** : R-02 tient, et *ce qui précède décrit ce que
les documents **spécifient**, jamais ce qu'une implémentation **démontre***. *(3)* ⚠ **L'extraction
mesure l'écart au besoin du passeport du ch. 16, et il est plus large qu'il n'y paraissait** : un
modèle de données à quatre propriétés obligatoires et **deux familles de preuve incompatibles**, un
identifiant à **une seule propriété obligatoire** et une **résolution hors périmètre** — *ce corpus
spécifie un format d'attestation, il ne fournit ni ancrage organisationnel, ni chaînage, ni statut
interrogeable.* **C'est exactement ce que le ch. 17 § 17.6.2 en disait sans l'avoir lu ; la lecture
le confirme, et ce n'est pas rien : une prudence validée par extraction cesse d'être une prudence.**

⚠ **Ce que ce chapitre ne traite pas.** Le socle *zero-trust* pré-agentique et l'identité de charge
de travail au sens de l'infrastructure d'entreprise sont **posés au ch. 3** et n'y sont pas
reconstruits. La **valeur probante** d'une assertion signée est au **ch. 15 § 15.1**. Le versant
*trust fabric* du §7.4.3 du Vol. I — l'admission d'un agent tiers entre organisations — est
**partagé déclaré avec le ch. 18**, qui en prend la moitié institutionnelle ; le § 13.5 n'en prend
que la moitié « adoption ».

## § 13.1 — VC Data Model et DID Core : à quel stade en sont les recommandations

Ce qui est établi sur pièce est l'**état de la voie normative**, à une date, document par document.

| Document | Stade au 21 juillet 2026 | Date du stade | Groupe et voie |
|---|---|---|---|
| *Verifiable Credentials Data Model* v2.0 | **Recommandation** du W3C | 15 mai 2025 | *Verifiable Credentials Working Group*, voie Recommandation (Vol. III F-79, **[B]**) |
| *Verifiable Credentials Data Model* v2.1 | **brouillon de travail** (*Working Draft*) | 11 mai 2026 | même groupe, voie Recommandation (Vol. III F-80, **[B]**) |
| *Decentralized Identifiers* (DID) v1.0 | **Recommandation** du W3C, *errata* signalés | 19 juillet 2022 | **non relevé** (Vol. III F-81, **[B]**) |
| *Decentralized Identifiers* (DID) v1.1 | **instantané de recommandation candidate** | 5 mars 2026 | voie Recommandation (Vol. III F-82, **[A]**) |

: Tableau 13.1 — Quatre documents du W3C, quatre stades, au 21 juillet 2026.

**Trois bornes accompagnent ce tableau et n'en sont pas détachables.** La colonne de droite est
laissée **incomplète** pour les deux documents DID : le rapport de lot ne relève pas leur groupe
éditeur, et *une case remplie de mémoire vaudrait moins qu'une case vide*. La ligne de la
version 2.0 tient d'un relevé de son historique de publication, consulté le 21 juillet 2026, qui **ne
porte aucune entrée postérieure au 15 mai 2025**. Et la mention d'*errata* de la version 1.0 des
identifiants décentralisés est exactement cela — une mention : **leur contenu n'a pas été ouvert**,
ce qui est une **absence de documentation, non un fait négatif vérifié**.

☑ **Reportés à leur source le 28 juillet 2026, les quatre stades tiennent** (volet de faits du volet
résiduel de G-1) : aucune entrée postérieure au 15 mai 2025 à l'historique de la version 2.0
(Vol. III F-79) ; la 2.1 toujours brouillon de travail du 11 mai 2026 (Vol. III F-80) ; la version
1.0 des identifiants décentralisés toujours Recommandation à *errata* signalés — ⚠ **dont le contenu
n'a toujours pas été ouvert** (Vol. III F-81) ; le quatrième, la version 1.1 des identifiants
décentralisés (Vol. III F-82), est repris plus bas, avec l'échéance qu'il a dépassée. ⚠ **Un stade
reconduit n'est pas un stade promu** : les niveaux ne bougent pas, et le tableau garde la date de son
relevé.

**Quatre stades, et ils ne se valent pas** — c'est la discipline que R-09 du Vol. III impose à chaque
mention. La version 2.0 du modèle de données et la version 1.0 des identifiants décentralisés portent
le stade de **Recommandation**, terme du parcours d'un groupe de travail. La version 2.1 porte celui
de **brouillon de travail**, et le document énonce lui-même sa réserve, en langue originale : « It is
inappropriate to cite this document as other than a work in progress » (Vol. III F-80). Le socle en
tire la conséquence prospective, et le chapitre la reprend : **aucune date de passage à un stade
ultérieur n'ayant été relevée, toute affirmation sur l'aboutissement de la 2.1 relève du
SPÉCULATIF**.

Le quatrième stade est le plus instructif, et il tient à lui seul l'argument de la section. La
version 1.1 des identifiants décentralisés est un **instantané de recommandation candidate** daté du
**5 mars 2026**, dont le texte porte son propre engagement : « This Candidate Recommendation is not
expected to advance to Recommendation any earlier than 05 April 2026 ». **Cette date était dépassée
de plus de trois mois au relevé du 21 juillet 2026** — et de près de quatre au 28 juillet suivant,
toujours **sans transition constatée**. Ce que le socle porte ici est un **relevé de la liste des
versions publiées** : seize entrées y figurent, du premier brouillon de travail public du 28 janvier
2025 à cet instantané du 5 mars 2026, et **aucune entrée étiquetée « Proposed Recommendation » ni
« Recommendation »** — hors l'instantané lui-même (Vol. III F-82, **[A]**, votée 3-0).

⚠ **Aucun degré d'absence n'est porté sur ce dernier constat, et c'est délibéré** : le contrôle de
bornage du lot a inscrit l'affirmation en faute de « degré injustifié » et retenu un **relevé de
liste**, non le balayage d'un texte — « fait négatif vérifié » et « degré 1 » y sont interdits tant
que le degré n'a pas été réarbitré. Le même document subordonne par ailleurs ses critères de sortie
de phase à une condition externe : que la spécification *DID Resolution* v0.3 ait satisfait les
siens.

*Une échéance auto-déclarée dépassée sans transition constatée n'autorise, en l'état du socle, aucune
inférence — ni retard, ni présage. Elle interdit seulement de présenter la version 1.1 comme un
standard établi.*

Lecture de l'auteur — ce que le socle établit est le **stade** de quatre documents à une date ; ce
qu'il n'établit pas est leur **contenu**. Il s'ensuit qu'**aucune exigence d'architecture** — format
d'accréditation, méthode de résolution, mécanisme de révocation — ne peut être dérivée de ce
chapitre : le corpus du W3C y entre comme **jalon de normalisation**, non comme spécification lue. *La
distinction n'est pas rhétorique : un dossier de diligence raisonnable qui citerait « la
Recommandation W3C » à l'appui d'une exigence de conception s'appuierait sur un stade et non sur un
texte.*

⚠ **Un agenda hérité circule dans la somme, et il faut dire à quel titre.** L'entrée héritée
**H-18 [C]** porte l'agenda que le Vol. I dressait à son gel de juin 2026 — modèle de données 2.1 en
recommandation candidate à l'horizon 2027, interfaces de cycle de vie en Recommandation en 2028,
`did:webvh` v1.0, *Web Bot Auth*, seconde version du service de noms d'agents (ANS v2). ⚠ **Ces
échéances sont PROJETÉES** : elles viennent d'un agenda dressé par un volume antérieur, **sans engagement daté du
W3C qui les porte**. Un agenda est un **repérage** : il n'établit pas les échéances qu'il liste, et
H-18 étant en **[C]**, aucune de ces dates ne porte ici de fait central.

## § 13.2 — Les profils d'interopérabilité : une lacune de couverture assumée

Le périmètre déclaré du lot d'instruction du Vol. III nommait trois sources : les recommandations
datées du W3C, les chartes des groupes communautaires, et la *Decentralized Identity Foundation*
(DIF). **Le rapport ne porte aucune affirmation sur la DIF.** La section s'écrit donc comme ce qu'elle
est : **une lacune de couverture, déclarée plutôt que comblée**. Le socle ne documente pas les
profils d'interopérabilité de la DIF — **absence de documentation, non fait négatif vérifié**
(degré 3).

Ce que le socle porte de la DIF vient d'un autre lot, dont le siège est le **ch. 18**, et ne concerne
pas les profils d'interopérabilité. Deux entrées y touchent. La première établit que le sigle
**KYA** désigne **au moins deux objets distincts**, chacun documenté par son éditeur : une
spécification communautaire remise à la DIF, et un cadre commercial annoncé le 15 juin 2026
(Vol. III F-49, **[B, degré 3]**). La seconde établit qu'**aucune des propositions consultées n'était
ratifiée ni adoptée** : la spécification remise à la DIF ne l'était pas au 22 juin 2026, et les deux
*Internet-Drafts* consultés sur l'identité d'agent sont des soumissions individuelles non adoptées
par un groupe de travail (Vol. III F-50, **[B, degré 2]**).

⚠ **Ces deux entrées ne sont pas instruites ici** : le **ch. 18 § 18.1 est le siège unique du KYA**
pour toute la somme, et le présent § s'y borne à les nommer pour dire ce que la DIF porte **et ne
porte pas** dans ce corpus. *Le sigle n'est ni défini ni employé ailleurs dans ce chapitre.*

**Un élément a été relevé et délibérément non converti en affirmation, et le motif est celui qui
compte.** Le **cadre d'architecture du portefeuille européen d'identité numérique** porte une matière
directement pertinente pour une section consacrée aux profils d'interopérabilité. Le lot l'a écarté
parce que **la version et la date du document n'étaient attestées que par son adresse**, le corps de
la page n'en affichant aucune ; deux tentatives d'accès à ce corpus figurent parmi les échecs de
source consignés. ⚠ **Le document est nommé, sa substance ne l'est pas** : ni l'objet de sa note, ni
le sens de sa portée ne sont rapportés ici — les rapporter transmettrait ce que le lot a refusé de
retenir, tandis que taire son identité rendrait inexécutable l'instruction qui doit le reprendre.
*Un document dont la version n'est attestée que par son adresse est un document dont on ignore ce
qu'on a lu.*

## § 13.3 — Les Community Groups agentiques du W3C

Le Vol. I avait identifié le signal : il recensait **quatre** groupes communautaires (*Community
Groups*) agentiques, dont trois datés, et posait la règle qui gouverne cette section — **un
*Community Group* n'est pas un *Working Group* : il ne produit pas de Recommandation et n'engage
aucun calendrier normatif** (Vol. III H-20, **[C]**). Le tri prospectif qu'il y attache est double :
l'existence des groupes est PROGRAMMÉE, leur conversion en standards demeure **SPÉCULATIVE**.
⚠ **Les trois statuts de ce tri ne sont pas définis ici** : leur siège est le **ch. 49 § 49.0**, et
ce chapitre les emploie sans les re-poser.

Le lot du Vol. III a ouvert **trois** groupes sur pièce le 21 juillet 2026 : deux que le Vol. I
portait, et un qu'il ne portait pas.

Le premier, le groupe **AI Agent Protocol**, existe depuis le **8 mai 2025** — statut qui, selon les
règles de publication du W3C, **ne place ses travaux ni sur la voie des normes ni au rang de norme du
W3C** (Vol. III F-83, **[B]**), et la clause se répète à chaque mention plutôt que de se poser une
fois en tête de section. Sa charte déclare comme objet, parmi d'autres, un modèle d'identité pour les
agents d'IA, et sa page de participants affichait **254 participants non-présidents** au relevé.
⚠ **Ce nombre est affiché par la plateforme du W3C** : il compte des inscriptions individuelles, non
des organisations contributrices ni une activité rédactionnelle — **donnée auto-déclarée, non
vérifiée indépendamment**, attribuée à cette page à chaque occurrence. ⚠ **Et il a bougé** : la même
page en affichait **260** au 28 juillet 2026, six de plus en sept jours, **sans que la date du
changement s'établisse au jour près** (Vol. III F-83, re-daté au volet résiduel de G-1). *Un décompte
d'inscrits n'est pas une mesure d'adoption ; c'est une mesure d'attention — et un compteur affiché
n'est pas un fait stable.* ⚠ **Aucun document produit par ce groupe n'a été ouvert.**

Le deuxième est celui qui touche le plus directement l'objet de la somme. Un groupe **Agent Identity
Registry Protocol** — groupe communautaire, donc sans production de Recommandation ni calendrier
normatif engagé — a été **proposé le 22 avril 2026**, et ses livrables annoncés comprennent **une
méthode DID et un format d'accréditation d'agent fondé sur les accréditations vérifiables**
(Vol. III F-30, **[B]**) ; **aucun rapport ni brouillon n'était publié** à la date de consultation
(Vol. III F-50, **[B, degré 2]**) — et la page n'en portait **toujours aucun au 28 juillet 2026**,
ni section de rapports, ni brouillon, ni spécification (Vol. III F-30, re-daté). *La distinction
entre annoncé et publié est ici toute la matière : une charte énonce des intentions de production,
non des documents constatés.*

Le troisième, le groupe **Agent Trust Protocol** — même statut, mêmes conséquences —, a été proposé
le **4 juin 2026**, et sa page pose en constat d'ouverture, en langue originale : « Autonomous AI
agents are being deployed at scale with no open standard governing how they prove identity, establish
trust, or protect the privacy of the humans they represent ». ⚠ **Source primaire ouverte hors
socle** : **aucune entrée du socle ne documente ce groupe** — balayage du PRD du Vol. III pour ce
syntagme, zéro occurrence —, et l'énoncé n'est donc pas porté ici comme fait central. *Un groupe qui
se constitue en déclarant l'absence de norme ouverte sur l'identité des agents est une pièce à verser
au dossier du ch. 16 ; il n'est pas la norme qu'il appelle.*

**Trois bornes encadrent ce relevé, et aucune n'est facultative.** *Premièrement*, le lot n'a mené
**aucun inventaire exhaustif** des groupes communautaires du W3C : un groupe agentique supplémentaire
a été repéré en résultat de recherche et **n'a pas été ouvert**. ⚠ *Il ne faut donc jamais écrire que
les groupes communautaires agentiques du W3C sont au nombre de trois* — le relevé porte sur trois
groupes **lus**, non sur la population des groupes existants. *Deuxièmement*, **aucun document produit
par ces groupes n'a été ouvert** : ce que ces textes affirment de la liaison entre un agent et son
organisation reste à instruire. *Troisièmement*, une affirmation portant sur les exigences de
publication auxquelles les rapports de groupe communautaire sont soumis a été **écartée au vote
adversarial, deux réfutations sur trois** ; le chapitre ne la reprend sous aucune forme.

Lecture de l'auteur — le socle établit qu'un groupe communautaire annonce, depuis le 22 avril 2026,
deux livrables dont le vocabulaire recouvre **deux des quatre pièces** du passeport construit au
ch. 16 : une méthode d'identifiant et un format d'accréditation (Vol. III F-30). **Il n'établit ni que
ces livrables existent, ni qu'ils convergent avec l'objet du ch. 16, ni qu'ils aboutiront.** La
convergence est donc **lexicale et constatée**, non technique et non normative. *Elle mérite d'être
suivie ; elle ne fonde rien.*

## § 13.4 — Identité de charge et identité décentralisée : SPIFFE/SPIRE, DID, WIMSE

Deux familles de solutions se disputent l'ancrage de l'identité agentique **sous** le niveau
applicatif, et le Vol. I les oppose en régime **[C]**.

L'**identité de charge de travail** attribue à l'agent une identité d'exécution. SPIFFE et SPIRE
délivrent un identifiant SPIFFE matérialisé par un justificatif à courte durée de vie, permettant une
authentification mutuelle sans secret partagé — profil bien adapté aux agents éphémères que la
découverte à l'exécution fait apparaître et disparaître (Vol. I *Monographie* §3.6.4, **[C]**). Ses
limites, telles que le Vol. I les formule à son gel de juin 2026, tiennent à l'**infrastructure
dédiée** qu'il exige et au **coût de rotation** des certificats. Le groupe de travail **WIMSE** de
l'IETF cherche à généraliser l'identité de charge de travail à des environnements multi-systèmes,
c'est-à-dire au **franchissement de frontières** que requiert l'interopérabilité agentique.

⚠ **Le socle *zero-trust* et le socle IAM pré-agentiques ne sont pas reconstruits ici** : ils sont
**posés au ch. 3** pour toute la somme, et ce chapitre s'y adosse. Ce qui appartient au présent § est
l'**articulation** de deux familles d'ancrage, non le mécanisme de l'une ou de l'autre.

L'**alternative décentralisée** s'appuie sur les identifiants décentralisés du W3C, dont une méthode
portée par un protocole de réseau agentique ancre l'identité dans le Web **sans autorité centrale**,
avec authentification de requêtes signées (Vol. I *Monographie* §3.6.4, **[C]**). *Le compromis est
celui, déjà connu, de la décentralisation contre la gouvernance* : un identifiant décentralisé
supprime l'autorité centrale mais **reporte sur l'écosystème la révocation et la mise à jour**, là où
un serveur d'identité de charge de travail les centralise au prix d'une infrastructure propre.

⚠ **Ce paragraphe entre en régime [C], et la conséquence se tire.** La vérification du Vol. I porte
sur ses **références**, non sur le contenu de ses affirmations : **aucun énoncé de ce § n'est
central**, et l'élévation en [B] supposerait la lecture des sources primaires que le Vol. I cite.

**Ce que le socle propre du Vol. III ajoute, et qui recadre l'opposition.** La spécification
SPIFFE-ID énonce qu'un SVID est considéré valide **s'il a été signé par une autorité du domaine de
confiance de l'identité SPIFFE qu'il porte** (Vol. III F-87, **[B]**). ⚠ **L'énoncé est
intra-domaine par construction** : il ne dit rien de ce qu'une autorité d'un **autre** domaine
devrait faire pour l'accepter. Et ce que cette spécification **démontre** est une vérification de
signature dans un domaine de confiance ; **elle n'énonce pas ce que cette vérification n'établit
pas** — absence de documentation, degré 3 (R-02 et R-14 du Vol. III).

Du côté de l'IETF, le §3.4.11 du document d'architecture de WIMSE — *Internet-Draft* du 6 juillet
2026, expirant le 7 janvier 2027, de visée *Informational*, **section d'architecture et non
prescription protocolaire** — énonce, **du point de vue WIMSE**, que les intermédiaires d'IA sont un
cas particulier de charges de travail déléguées (Vol. III F-86, **[B]** ; établi au **ch. 12
§ 12.1**, non rejoué ici, et **reconduit sans changement** au 28 juillet 2026).

Lecture de l'auteur — les deux familles répondent à des questions différentes, et le chapitre le pose
comme lecture et non comme résultat. **Ce que le socle établit** : le critère de validité d'un SVID,
relatif à un domaine (Vol. III F-87) ; le stade des documents du W3C (Vol. III F-79 à F-82) ;
l'opposition infrastructure-contre-écosystème telle que le Vol. I la formule en **[C]**. **Ce qu'il
n'établit pas** : qu'une famille soit préférable à l'autre, ni qu'elles soient exclusives, ni qu'un
déploiement documenté les combine. *L'identité de charge de travail répond à « d'où ceci s'exécute-t-il
et dans quel domaine » ; l'identité décentralisée répond à « que puis-je présenter hors de ce
domaine ». La question de l'admission inter-domaines, qui est celle du ch. 18, n'est traitée par
aucune des deux.*

## § 13.5 — Le fossé d'adoption : qui vérifie quoi, en production, à date

La thèse du chapitre porte sur une adoption « à démontrer ». L'énoncé qui la soutient est un énoncé
**sur l'état de la documentation**, et il s'écrit au troisième degré d'absence : **le corpus consulté
le 21 juillet 2026 ne documente aucun établissement financier réglementé, nommément désigné,
exploitant en production des accréditations vérifiables du W3C ou des identifiants décentralisés.**
C'est une **absence de documentation, non un fait négatif vérifié** — et elle **ne soutient en aucun
cas** l'énoncé « aucune banque n'emploie ces mécanismes » (R-14 du Vol. III). ⚠ Le lot a par ailleurs
**refusé de combler ce vide par un billet d'éditeur**, conformément à la règle du dépôt : *une lacune
déclarée ne se comble pas par une source de moindre qualité.*

**Une illustration, et elle est présentée comme telle.** Le rapport d'interopérabilité du modèle de
données v2.0, publié sur le dépôt du groupe de travail du W3C, énumère **dix implémentations**, dont
aucun intitulé ne porte la dénomination d'une banque, d'un assureur ou d'une infrastructure de marché
financier (Vol. III F-31, **[C, degré 1]**). ⚠ **Cette entrée est en [C]** : elle ne porte pas le
propos de la section. Ses **deux bornes sont plus instructives que son résultat**. D'une part, le
relevé porte sur des **intitulés**, non sur la nature des organisations : une implémentation peut
être exploitée pour le compte d'un établissement financier sans figurer sous son nom. D'autre part,
une suite de tests ne recense que ses **participants volontaires** — *elle mesure qui a bien voulu se
soumettre à une épreuve d'interopérabilité publique, pas qui déploie.*

⚠ **Sa date, elle, a changé, et le changement enseigne plus que le chapitre.** L'entrée portait un
rapport daté du **19 juillet 2026** ; le document consulté le 28 juillet suivant porte en tête
**26 juillet 2026**. **Le fait négatif tient intégralement** — dix implémentations, aucun intitulé
financier, degré et niveau inchangés : *la portée du changement est la date seule.* ⚠ **Et cette date
n'est pas une date de publication** : le rapport est **régénéré à chaque exécution de la suite de
tests**, de sorte que toute date portée sur lui sera périmée à l'exécution suivante **sans qu'aucun
fait ait changé**. *Un horodatage d'exécution cité comme une date de publication est une péremption
que rien ne signale* — le chapitre n'en porte donc plus aucune.

**Un contrepoint existe, et il vient d'un champ voisin.** Le cadre de gouvernance de l'écosystème
vLEI de la GLEIF, dans sa version du **25 mars 2026**, désigne son socle technique par « Technical
Requirements Part 1: KERI Infrastructure » et déclare avoir été construit en conformité avec les
normes et recommandations de la *Trust over IP Foundation* (Vol. III F-32, **[B]**). ⚠ **Borne
explicite** : le fait porte sur **les intitulés des documents contrôlés et sur la phrase de
filiation**, tels qu'affichés sur la page consultée. *Il ne s'ensuit pas que le vLEI exclue le modèle
du W3C* : le contenu de la seconde partie des exigences techniques n'a pas été ouvert, et **un
intitulé n'est pas un contenu**. ☑ **Reporté à sa source le 28 juillet 2026, le cadre ne porte
aucune version postérieure au 25 mars 2026** (Vol. III F-32).

La *Bank of Japan Review* **2026-E-6**, du **10 avril 2026**, figure au dossier, et il faut dire à
quel titre exactement. ⚠ **Elle n'est portée par aucune entrée du socle** : seule sa page de
présentation a pu être lue, son texte intégral n'ayant pas pu être extrait. Cette page situe l'emploi
des accréditations vérifiables en finance **au registre de l'exploration** ; **la qualification n'est
donc pas portée ici comme fait**, et l'affirmation n'est pas centrale. ⚠ **L'attributeur est nommé
plutôt qu'abrégé en « une revue de banque centrale »** : la parade de péremption couvre les
dénominations commerciales et les versions, **jamais l'attributeur d'une affirmation** (décision 15
du TOC). La revue porte enfin la réserve d'usage de son éditeur, en langue originale : « Views
expressed are those of the author(s) and do not necessarily reflect those of the Bank. »

⚠ **Six échecs de source bornent ce chapitre autant que ses résultats**, et ils sont exposés au même
titre : la fiche de la norme **ISO 17442-3** relative au vLEI, inaccessible ; le glossaire du cadre
de gouvernance vLEI, introuvable ; deux accès au **cadre d'architecture du portefeuille européen
d'identité numérique**, l'un introuvable et l'autre redirigé hors de son hôte ; le texte intégral de
la *Bank of Japan Review* 2026-E-6, récupéré mais non extractible ; une section du processus des
groupes communautaires du W3C, consultée sans que la phrase recherchée soit restituée. *Chacun retire
quelque chose au chapitre.* ⚠ **Les identifiants sont portés parce qu'ils conditionnent la reprise** :
*un échec de source dont on tait l'identité rend inexécutable l'instruction qui doit le solder*
(décision 15 du TOC). L'existence d'une norme ISO relative au vLEI, en particulier, n'est établie que
par une **source secondaire** — la revue ci-dessus, qui en porte le numéro — et **n'a pas été retenue
comme affirmation** : le numéro figure ici comme **identifiant d'une source à instruire**, jamais
comme fait.

Lecture de l'auteur — ce que le socle établit est un **écart entre deux registres** : d'un côté,
quatre documents du W3C dont deux portent le stade de Recommandation depuis 2022 et 2025
(Vol. III F-79, F-81) ; de l'autre, un relevé d'implémentations où aucun intitulé financier
n'apparaît (Vol. III F-31, **[C]**) et un corpus qui ne documente aucun déploiement en production
nommément désigné. **Ce que le socle n'établit pas, c'est la cause de cet écart** — ni immaturité des
spécifications, ni prudence réglementaire, ni discrétion des exploitants ne peuvent être invoquées,
aucune n'étant documentée. La seule construction retenue est **comparative**, et elle tient au
contrepoint du vLEI : là où un écosystème financier a effectivement produit un dispositif
d'accréditation opérant, ce qu'il a ajouté au vocabulaire technique est un **cadre de gouvernance
nommé, versionné et adossé à une filiation déclarée** (Vol. III F-32). *L'hypothèse que la pièce
manquante côté agentique soit institutionnelle plutôt que lexicale demeure une hypothèse, et le socle
ne la démontre pas.*

⚠ **Cette hypothèse a un siège, et ce n'est pas ici.** Elle est instruite au **ch. 18 § 18.3**, sur
trois précédents de fédération, et le §7.4.3 du Vol. I qui la nourrit est **partagé déclaré** entre ce
chapitre et le ch. 18. Le présent § en prend le versant **adoption** ; le ch. 18 en prend le versant
***trust fabric***. *Le partage est écrit à la table de couverture du TOC, et ni l'un ni l'autre ne
reconstruit la moitié de l'autre.*

### Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Le lexique du passeport, et sa borne.** Les mots — accréditation vérifiable, identifiant
   décentralisé, méthode, résolution — viennent d'ici ; **leur contenu technique n'y est pas
   établi**. Le **ch. 16** assemble l'objet avec ce vocabulaire et **sans** ce contenu, et il le dit.
2. **Le stade n'est pas l'adoption.** Deux Recommandations et zéro déploiement financier nommément
   documenté coexistent sans contradiction. Les **ch. 15 et 18** rencontrent la même dissociation sur
   d'autres corpus ; elle est posée ici une fois.
3. **Ce qu'un groupe communautaire n'est pas.** Ni voie des normes, ni Recommandation, ni calendrier
   engagé. Les **ch. 16 § 16.4** et **ch. 18 § 18.1** citent des groupes communautaires ; ils
   n'auront pas à re-poser la clause.
4. **Le contrepoint institutionnel du vLEI.** Un cadre de gouvernance publié, versionné, à filiation
   déclarée, produit hors du champ agentique. Le **ch. 18 § 18.3** en fait l'un de ses trois
   précédents ; le présent chapitre l'introduit comme **matière de comparaison**, jamais comme
   transposition.

---

## § 13.6 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée (PRD, Annexe A).

**Ce qui est enfreint.** À la rédaction, le 27 juillet 2026 et sur instruction d'auteur : portes
**G-3** (socle consolidé à zéro entrée) et **G-4** (volet de fond de la collation contre le Vol. III
rédigé) ; volet résiduel de **G-1** non instruit ; ordre de rédaction du PRD §6. ⚠ **Deux de ces
trois écarts sont levés depuis, et le troisième ne l'est pas** : le **volet de faits de G-1** est levé
le 28 juillet 2026, **G-3 est franchie** le même jour (PRD v0.14), **G-4 demeure ouverte**. *Une porte
franchie après la pièce ne rétroagit pas sur elle* — elle rend la relecture possible, et la présente
passe l'a conduite.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** Les faits du Vol. III conservent leur niveau
   sous G-4 ouverte ; ceux du Vol. I entrent en **[C]**, et **deux entrées héritées mobilisées ici
   sont elles-mêmes en [C]** — H-18, H-20 : elles situent, elles ne portent pas. **H-19 est consultée
   et non mobilisée**, sa matière siégeant au ch. 18. ⚠ **Le franchissement de G-3 n'élève aucun
   niveau** : aucun vote adversarial n'a été conduit, et **CA-IV-13 reste insatisfaite**.
2. **Les décomptes sont publiables** (G-2). Écart de **+13,2 %** sur la cible dérivée, re-mesuré au
   commit du 28 juillet 2026 ; l'écart du Livre alimente **D-4** par la remontée **R-IV-17** du
   ch. 12, et n'est corrigé nulle part — *ni par amputation, ni par gonflement*.
3. **Les renvois de ce chapitre, et à quoi ils résolvent.** Le renvoi interne au **Livre I** — ch. 3 —
   résout contre du texte ; ceux vers les **ch. 12, 15, 16, 18 et 21** résolvent contre le texte du
   Livre II ; le renvoi au **ch. 49 § 49.0**, siège du tri prospectif, résout contre le texte du
   Livre V. ⚠ **Tous résolvent contre des brouillons hors portes**, aucun contre une pièce recevable.
4. **Les faits périssables du socle ONT été repris à leur source le 28 juillet 2026**, et ce chapitre
   est celui du Livre où la conséquence était la plus lourde : **trois des cinq documents dont il
   relève le stade sont en cours de procédure**, et l'un d'eux avait dépassé son échéance
   auto-déclarée dès le relevé du 21 juillet 2026. **Quatre verdicts de changement portent sur ses
   entrées ; deux seulement atteignent son texte** — une date de rapport et un décompte d'inscrits,
   l'un et l'autre reportés au corps —, les **deux autres** frappant une composante qu'il ne cite
   pas : un décompte de participants sur un groupe que l'entrée ne nomme pas (Vol. III F-50) et la
   révision du brouillon d'architecture WIMSE (entrée héritée H-18), que le § 13.4 date déjà par
   Vol. III F-86.
   ⚠ **Ce qui reste dû n'est pas la datation mais la confrontation** : *instruire la date d'une entrée
   n'est pas confronter son énoncé à sa source*, et **aucun énoncé de ce chapitre n'a subi cette
   épreuve**. *Un stade est un fait daté du jour où on l'a lu.*

**Remontées ouvertes par ce chapitre :**

- **R-IV-18 — non bloquante, de couverture de source, et de la classe nommée par R-IV-12 à R-IV-14.**
  Le Vol. III déclare au **degré 3** ne pas documenter les profils d'interopérabilité de la DIF
  (§ 13.2) et n'avoir extrait **aucun contenu technique** des quatre documents du W3C (§ 13.1). Or le
  **Vol. I *Monographie* §3.6.3 et §3.6.4** — texte rédigé d'un autre volume de la somme, et **l'une
  des sources de la ligne Fusion de ce chapitre** — décrit ce contenu : le modèle de données des
  accréditations vérifiables comme brique de preuve, la méthode d'identifiant ancrée au Web avec
  authentification de requêtes signées, la distinction entre le justificatif qui établit *qui est
  l'agent* et celui qui établit *ce qu'il a le droit de faire*. ⚠ **Ce n'est pas une contradiction** :
  l'énoncé du Vol. III porte sur **son** corpus et reste exact dans son périmètre. ⚠ **Et cela ne
  comble pas la lacune** : les faits du Vol. I entrent en **[C]**, et une entrée [C] ne porte jamais
  un fait central. **Demande remontée** : que la collation de fond (**G-4**) qualifie cette lacune
  comme *couverte au régime [C] par le Vol. I, à instruire à la source primaire pour élévation*, et
  non comme une absence de matière. C'est la **quatrième occurrence** de cette classe ; l'Annexe C du
  TOC l'écrit désormais en règle, et la présente remontée en fournit un cas de plus plutôt qu'une
  demande de règle nouvelle.
- **R-IV-19 — non bloquante, de partage déclaré.** Le §7.4.3 du Vol. I est **partagé déclaré** entre
  le § 13.5 et le **ch. 18 § 18.3** (table de couverture du TOC). Le partage a été respecté — versant
  *adoption* ici, versant *trust fabric* au ch. 18 —, mais **le TOC ne dit pas où passe la ligne** :
  il nomme le partage sans en fixer le critère. Le présent chapitre a tranché par un critère
  d'auteur — *ce qui se mesure en déploiements reste ici, ce qui se mesure en institutions va au
  ch. 18* —, et le déclare plutôt que de le taire. **Demande remontée** : que le critère soit écrit
  au TOC, ou que le partage soit remplacé par une affectation unique. ⚠ **Un partage sans critère est
  une double revendication qui ne se voit pas** : c'est la classe que le TOC a déjà rencontrée sur
  les lignes Fusion citant un intervalle, et qu'**aucun contrôle outillé n'attrape**.

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.30** — § 13.1 à
§ 13.5, dans l'ordre exact —, et le § 13.0 est une introduction de chapitre, non une section de plan.
La **table de couverture est respectée pour ses six lignes**, y compris ses trois **hors périmètre**
déclarés : §7.4.1 et §7.4.4 du Vol. I partent au **ch. 21**, §7.4.2 au **ch. 16**, et **aucun des
trois n'est repris ici**. Le **socle IAM et le socle *zero-trust* ne sont pas reconstruits** : ils
restent au **ch. 3**, auquel le § 13.0 et le § 13.4 renvoient. Le **siège du KYA n'est pas
anticipé** : le § 13.2 nomme les deux entrées de la DIF sans instruire le sigle, dont le siège unique
est le **ch. 18 § 18.1**. Les **trois marqueurs de R-14** portent leur degré. Le **marqueur unique de
R-09** ouvre une discipline reprise **à chaque mention** sur le domaine balayé — la clause du groupe
communautaire y est répétée plutôt que posée une fois en tête —, et *cette reprise se déclare sans se
dénombrer*. Les **deux métriques auto-déclarées** — le décompte de participants, l'énumération
d'implémentations — sont attribuées à la page qui les affiche, **à chacune de leurs occurrences**. Le
**siège du tri prospectif est renvoyé, non reconstruit** : le § 13.3 emploie les statuts et nomme le
**ch. 49 § 49.0**, sans en re-poser les définitions. Et les **quatre marqueurs de « Lecture de
l'auteur »**, aux § 13.1, § 13.3, § 13.4 et § 13.5, sont suivis de ce que le socle établit et
n'établit pas.

⚠ **Passe de relecture du 28 juillet 2026 — ce qu'elle a changé, et ce qu'elle n'a pas touché.** Elle
a *(a)* **borné un quantificateur universel négatif** du § 13.0 — « le passeport d'agent ne figure
dans aucune spécification de 2026 » portait sur un corpus non balayé, et l'énoncé est ramené aux
spécifications que le chapitre relève ; *(b)* **reporté au corps les deux verdicts de re-datation**
qui atteignent le texte de la pièce (§ 13.3 et § 13.5) et ses **sept constats de reconduction** (§ 13.1 pour
quatre, § 13.3, § 13.4 et § 13.5 pour un chacun) ; *(c)* **corrigé la date du rapport
d'interopérabilité** et retiré la seule date que le chapitre portait sur un document régénéré à
chaque exécution ; *(d)* **aligné le renvoi au siège du tri prospectif** ; *(e)* **corrigé les
déclarations d'en-tête** — F-86 mobilisée et non déclarée, H-19 déclarée mobilisée et seulement
consultée, un cardinal de stades faux, trois versions du TOC périmées, le décompte re-mesuré, et
l'état des portes réaligné aux trois champs qui le portaient. ⚠ **Elle n'a ni ouvert ni renuméroté de
remontée** : *deux plages de remontées ne se
rapprochent par aucun instrument versionné*, et une passe qui relit cinquante pièces en parallèle
alloue des numéros qu'elle ne peut pas voir. Les écarts relevés hors de cette pièce — dont
**l'intitulé « Table des matières détaillée du chapitre 14 » sous l'entrée du chapitre 13** au TOC —
sont **remontés hors du fichier**, jamais corrigés ici.

⚠ **Contre-relecture du 28 juillet 2026 — ce qu'elle a repris à la passe précédente.** Elle a
*(a)* **rectifié un cardinal faux** : la passe précédente déclarait **deux** verdicts de re-datation
touchant la pièce là où **quatre** portent sur des entrées qu'elle mobilise (Vol. III F-31 et F-83,
qui atteignent le texte ; Vol. III F-50 et l'entrée héritée H-18, qui n'atteignent aucun énoncé
cité) — *un cardinal se re-mesure sur le domaine entier, non sur la part qui se voit* ;
*(b)* **replacé sous son degré** l'énoncé borné du § 13.0 — ramener « aucune spécification de 2026 »
aux seules spécifications relevées ici corrigeait le quantificateur mais laissait une **affirmation
sur le contenu de documents que le socle déclare non extraits**, ce que la même section interdit
quatre paragraphes plus bas ; *(c)* **complété une énumération de quatre stades qui n'en nommait que
trois** au § 13.1 ; *(d)* **appliqué la décision 15 aux trois attributions que la pièce
anonymisait** — la *Bank of Japan Review* 2026-E-6, la norme ISO 17442-3 et le cadre d'architecture
du portefeuille européen d'identité numérique : *la parade de péremption couvre les dénominations
commerciales et les versions, jamais l'attributeur d'une affirmation ni l'identifiant d'une source
qu'un lot doit instruire.* ⚠ **Elle n'a ouvert aucune remontée, pour le motif de la passe
précédente**, et n'a touché ni le TOC, ni le PRD, ni le conspectus. ⚠ **Elle ne satisfait pas
davantage CA-IV-13** : *une seconde passe du même appareil n'est pas une seconde personne.*


---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-18 — close par entrée au registre de l'Annexe C (TOC v0.25), troisième table.** La lacune du
  Vol. III sur le **contenu technique du corpus W3C** et les profils d'interopérabilité est qualifiée
  *couverte au régime **[C]** par le Vol. I, à instruire à la source primaire pour élévation*. ⚠ **Le
  mot « couverte » est le seul admissible, et il ne veut pas dire « comblée »** : les faits du Vol. I
  entrent en [C], et *une entrée [C] ne porte jamais un fait central*. **Rien n'est corrigé au
  Vol. III** — son énoncé porte sur **son** corpus et reste exact dans son périmètre.
- **R-IV-19 — close par écriture du critère au TOC v0.25, aux deux tables de couverture.** Le partage
  du §7.4.3 du Vol. I entre ce chapitre et le **ch. 18 § 18.3** porte désormais sa ligne de partage :
  ***ce qui se mesure en déploiements reste ici, ce qui se mesure en institutions va au ch. 18***.
  C'est le critère que cette pièce avait appliqué et déclaré ; il est **repris tel quel** au plan, non
  réinventé. ⚠ **Ce qui est réparé n'est pas le partage mais son invisibilité** : *un partage sans
  critère est une double revendication qui ne se voit pas*, et **aucun contrôle outillé ne l'attrape**
  — les deux renvois sont valides isolément.

⚠ **Ce que la clôture ne change pas — état au 28 juillet 2026.** **G-3 est franchie** et l'Annexe B
existe (159 entrées) ; **G-4 demeure ouverte** — la collation de fond contre le Vol. III rédigé n'est
pas conduite —, **aucun vote adversarial n'a porté sur les entrées mobilisées ici**, et **aucun
énoncé de cette pièce n'est central au sens de CA-IV-01**. **CA-IV-13 n'est pas satisfaite** : la
relecture du 28 juillet 2026 a été conduite **par le même appareil que la rédaction**, et *une lacune
de socle se comble par une source ; celle-ci ne se comble que par une seconde personne.* Cette pièce
reste un **brouillon non publiable**. *Zéro remontée ouverte ne veut pas dire pièce recevable : cela
veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée.*
