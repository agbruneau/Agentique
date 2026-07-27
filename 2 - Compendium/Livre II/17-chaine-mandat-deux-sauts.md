# Chapitre 17 — La chaîne de mandat et le problème des deux sauts

*Livre II — Faire confiance : identité, délégation et fabrique de confiance.
Premier mouvement — émettre (ch. 12-18). Sixième chapitre du mouvement. **Il ne rend aucun verdict de
grille** : il instruit **Q-C** — *pour qui agis-tu ?* — au lieu de l'appliquer mécanisme par
mécanisme.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — portes **G-3** et **G-4** ouvertes ; instruction d'auteur du 27 juillet 2026. ⚠ **Une section de ce chapitre est en outre rédigée contre une consigne explicite du plan** : le TOC déclare le § 17.5 « **front neuf — aucun des trois volumes ne le porte : sources primaires à établir avant rédaction** », et **ces sources n'ont pas été établies**. Le § 17.5 **expose donc le vide au lieu de le combler**, et ouvre la remontée **R-IV-27**. **R-IV-16 et R-IV-17, ouvertes au ch. 12, valent pour tout le Livre** |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit.** Gels de source : **juin 2026** (Vol. I), **21 juillet 2026** (Vol. III). ⚠ **Une relève du plan porte une date postérieure au gel de sa source** — un document normatif consulté le **26 juillet 2026** — et elle est **reprise comme relève, jamais comme entrée de socle** (§ 17.1) |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (G-3 ouverte). Résolution contre le **Vol. III *Monographie* ch. 9-10**, dont les entrées **F-14**, **F-15**, **F-29**, **F-31**, **F-44** à **F-47**, **F-53**, **F-74** à **F-82**, **F-89** et les entrées héritées **H-01**, **H-06**, **H-12**, **H-19**, **H-28**, **H-29**, **H-33** conservent leurs niveaux d'origine ; et contre le **Vol. I *Monographie* §2.11.2 et §3.6.6**, en **[C]**. ⚠ **Six entrées mobilisées sont en [C]** — F-31, H-19, H-28, H-29, H-33, plus H-15/PC3 du Vol. II, construction d'auteur hors socle factuel : elles **situent**, elles ne portent pas. ⚠ **Le § 17.5 ne mobilise aucun socle** : il n'en a pas. **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | Vol. III — **R-14 : quinze occurrences**, dont **douze de degré 3** — **le plus grand nombre du Livre**, et c'est une conséquence du sujet : *un chapitre qui prend une frontière pour objet écrit surtout des absences* ; **R-02 : sept occurrences**, § 17.1 (quatre), § 17.2, § 17.3 et § 17.6 ; **R-09 : huit occurrences** ; **R-01 : deux occurrences**, § 17.2 et § 17.6 ; **R-12 (traitement défensif au niveau du maillon, aucune recette) : deux occurrences**, § 17.6.1 ; **R-13 : une occurrence**, § 17.4, l'échelle d'autonomie jamais nue. **R-03 à R-08, R-10, R-11 : zéro occurrence.** Vol. II — **§8.2 : une occurrence**, § 17.6.2 ; **R-1 à R-8 : zéro occurrence**. ⚠ **Un faux ami est déclaré** : le « point de contrôle » du glossaire du Vol. II traduit une notion de reprise sur incident et **n'est pas** le « point de contrôle obligatoire » de son ch. 19 ; la collision est **signalée et non résolue** (§ 17.4) |
| **Volumétrie cible** | ≈ **5 700 mots** de corps (§ 17.0 à § 17.6), **cible dérivée** de l'enveloppe du Livre (50 000 mots, TOC v0.24) au prorata des sections — six sections dont une à trois sous-sections. ☑ **Décompte publiable depuis G-2** ; **réel : 6 933 mots** par [`PRD/decompte.sh`](../PRD/decompte.sh) — **+21,6 %** (re-mesuré le 27 juillet 2026 après la passe d'arbitrage, qui a versé au § 17.1 l'extraction du RFC 8693). ⚠ La volumétrie du Livre est relevée au [`README.md`](README.md) du dossier et alimente **D-4** par **R-IV-17** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.25, entrée du chapitre 17)* — la délégation est le maillon faible — les mécanismes instruits par le Vol. III **documentent** qu'un agent *a* une identité, **aucun d'eux ne documente** *au nom de qui* il agit à l'instant t ; au-delà de deux sauts, **aucun des mécanismes instruits ne documente** une traçabilité opposable de bout en bout.
>
> ⚠ **Thèse réalignée au TOC v0.25** (décisions 8 et 14), sur la remontée **R-IV-28** ouverte par cette pièce. **Trois** termes de la forme antérieure tombent ensemble : le verbe « **prouvent** », que **R-02 du Vol. III proscrit** pour un mécanisme cryptographique ; « **presque aucun** », quantificateur sur un corpus non balayé ; et « **aucun mécanisme documenté** », quantificateur universel négatif. **Le corps du chapitre n'a pas changé** : il était écrit aux formes bornées. ⚠ **Le renvoi de tête du TOC vise un document retiré du dépôt** — la *Synthèse* du Vol. I — et son régime est suspendu à la décision d'auteur **D-5**.

---

## § 17.0 — Introduction : ce qui ne se déduit pas d'un identifiant

Le mouvement portait jusqu'ici sur l'**émission** : ce qu'une organisation délivre à un agent pour
qu'il soit reconnaissable. Ce chapitre porte sur **ce qui ne s'en déduit pas**. *Un identifiant
vérifiable répond de ce qu'un agent **est** ; il ne dit ni pour qui cet agent agit, ni depuis quand,
ni jusqu'où.* L'entreprise réglementée, elle, doit pouvoir produire cette seconde réponse devant un
auditeur, et **la produire pour un instant donné** — non pour le moment de l'admission.

⚠ **Règle d'emploi déclarée à l'ouverture, et elle vaut pour tout le chapitre.** La grille du ch. 14
s'applique par mécanisme et ne rend que trois verdicts. **Ce chapitre n'en rend aucun** : il
*instruit* **Q-C** au lieu de l'appliquer. Le motif est au ch. 14 § 14.3 — *Q-C n'a reçu qu'un seul
verdict à l'application-témoin, et encore partiel ; une question à laquelle deux mécanismes sur trois
ne permettent même pas de répondre n'appelle pas un verdict de plus, elle appelle un chapitre.*

Lecture de l'auteur — **la thèse citée en tête est une construction du plan, et deux de ses termes
excèdent ce que le socle établit.** **Ce que le socle établit** : la spécification d'un format de
mandat versionné et de ses attributs temporels (Vol. III F-46, **[B]**) ; la définition d'un attribut
de délégation dans un jeton et l'exclusion explicite de la sécurité de ce jeton hors du périmètre du
même document (F-47, **[A]**) ; le statut pré-normatif d'un mécanisme de propagation de contexte
(F-29, **[A]**). **Ce qu'il n'établit ni ne permet d'écrire** : *(a)* un **classement** des mécanismes
de 2026 — « presque aucun » suppose un balayage qu'aucun rapport de lot ne revendique ; *(b)* qu'un
mécanisme cryptographique « **prouve** » quoi que ce soit, verbe que R-02 proscrit ; *(c)* le
quantificateur universel négatif de la seconde moitié — « aucun mécanisme documenté » —, forme que le
régime des trois degrés d'absence refuse. ⚠ **Le corps de ce chapitre n'emploie aucun des trois**, et
**le Vol. III a lui-même borné les deux thèses correspondantes le 21 juillet 2026** ; l'écart est
remonté (**R-IV-28**), non arbitré ici.

**Le chapitre se lit en six temps.** Ce que trois mécanismes portent du mandat (§ 17.1) ; le rang que
chacun accorde à la **chaîne** (§ 17.2) ; ce qu'un régime civil du mandat éclaire, et où l'analogie
casse (§ 17.3) ; l'humain comme premier et dernier maillon (§ 17.4) ; **la limite empirique de la
parade humaine, dont le socle n'existe pas** (§ 17.5) ; et le problème des deux sauts, exposé plutôt
que franchi (§ 17.6).

## § 17.1 — Le mandat dans les protocoles

Trois mécanismes documentés portent quelque chose du mandat. *Ils n'en portent ni la même part, ni au
même statut, et les additionner serait la première faute possible de ce chapitre.* ⚠ **Bornage** :
l'énumération est celle des lots d'instruction du Vol. III ; **elle ne prétend recenser ni les
mécanismes du marché, ni ceux qu'aucun lot n'a ouverts.**

**Les mandats du protocole de paiement agentique : un format, une contrainte de vérification, un
ancrage renvoyé au déploiement.** La spécification, en **version v0.2.0 publiée le 28 avril 2026** —
*spécification de projet, non texte normatif d'un organisme de normalisation* —, définit **deux types
de mandats** sérialisés en SD-JWT, porteurs d'un attribut de type **versionné** ainsi que des
attributs temporels d'émission et d'échéance (Vol. III F-46, **[B]**). Le rapport de lot porte deux
éléments que le résumé de l'entrée ne porte pas encore, et qui décident du reste : pour les mandats
dits ouverts, la spécification prévoit un attribut de **confirmation** contenant la clé publique de
l'agent, ainsi que des **champs de portée** — marchands autorisés, ensemble de lignes d'articles. La
contrainte de vérification est explicite dans le texte : « implementations MUST match the exact `vct`
string, including the version suffix ».

⚠ **Ce que cette spécification démontre est donc un format, un jeu d'attributs et une obligation
d'appariement exact du type** ; *elle ne documente pas ce qu'une vérification de mandat établit en
pratique*, puisqu'elle **renvoie l'ancrage de confiance au déploiement** en proposant **deux modèles
alternatifs** — croire l'émetteur du justificatif de l'utilisateur, ou croire directement le
fournisseur d'agent. **R-02 est ici la règle opérante** : *un mécanisme se qualifie par ce que sa
spécification démontre, jamais par ce qu'elle promet.*

⚠ **La divergence de gouvernance de cette spécification est déjà tranchée au ch. 10 et n'est pas
rouverte ici.** Le fait est acquis, daté et consommé par extraction au gel du 27 juillet 2026 ; ce
chapitre n'y revient pas, et **une pièce qui rouvrirait une divergence close en ferait une divergence
ouverte**.

**L'agissement pour le compte d'autrui : la délégation est nommée, le jeton est décliné.** Le
**RFC 8693** définit en sa §4.1 l'attribut d'acteur comme « a means within a JWT to express that
delegation has occurred and identify the acting party to whom authority has been delegated » ; sa §1
place **explicitement hors périmètre** « the specific syntax, semantics, and security characteristics
of the tokens themselves », et **n'impose aucune exigence sur le modèle de confiance du déploiement**
(Vol. III F-47, **[A]**). Le document distingue par ailleurs **délégation** et **usurpation
d'identité** : « With delegation semantics, principal A still has its own identity separate from B ».

⚠ **La conséquence se formule avec prudence** : le mécanisme **nomme** la partie agissante et le
sujet ; *il n'attache à cet attribut aucune assertion sur le consentement du mandant, sur la portée
matérielle du mandat ni sur sa durée* — ces éléments relevant de la politique du serveur
d'autorisation, que la RFC laisse hors de son texte. **Il ne faut donc pas écrire qu'OAuth ne
permettrait pas d'établir le mandant : il ne le spécifie pas, ce qui est autre chose.**

☑ **La relève du plan sur le RFC 8693 est consommée par extraction — 27 juillet 2026, remontée
R-IV-29 close.** Le TOC signalait que le « au nom de qui » **a une spécification normative que la
thèse ne nommait pas**, et demandait l'extraction plutôt que la reprise d'un résumé. Elle a été faite
à la source primaire, **aux deux sièges du document** — éditeur de RFC et *datatracker* de l'IETF —,
sur un texte de la **voie des normes** (*Standards Track*) publié en **janvier 2020**.

**Ce que la spécification démontre**, en ses propres termes. La chaîne de délégation s'exprime **par
imbrication** de l'attribut d'acteur : « A chain of delegation can be expressed by nesting one "act"
claim within another » ; l'acteur courant est le plus extérieur, les acteurs antérieurs forment
« a history trail », et **aucune profondeur maximale n'est spécifiée**.

⚠ **Et l'extraction rapporte davantage que ce que la relève annonçait — dans le sens qui affermit la
thèse de ce chapitre au lieu de la fragiliser.** La même section **exclut expressément les maillons
antérieurs de toute décision d'autorisation** : « the consumer of a token MUST only consider the
token's top-level claims and the party identified as the current actor », les acteurs antérieurs
étant « informational only and […] not to be considered in access control decisions ». *Le RFC 8693
documente donc l'**historique** d'une chaîne et **proscrit** qu'il fasse preuve.*

⚠ **La conséquence se formule exactement, et pas au-delà.** La relève supposait la thèse
« possiblement sous-spécifiée » ; **elle ne l'est pas sur ce point**. La traçabilité opposable de
bout en bout ne manque pas ici **par omission du spécificateur** — elle est **écartée par
prescription**, et pour un motif que le document assume : un vérificateur ne doit pas fonder sa
décision sur des maillons qu'il n'a pas lui-même authentifiés. *Ce qui manque au second saut n'est
donc pas un détail que la spécification aurait négligé, c'est ce qu'elle a délibérément placé hors de
sa portée.* ⚠ **Cette extraction n'entre toujours pas au socle** : c'est la porte **G-3** qui l'y
ferait. Elle cesse seulement d'être un repérage sur résumé — *lire un document à sa source ne le
verse pas ; cela rend seulement le versement possible.* Le **§ 17.1 en est le siège désigné**.

**Les jetons de transaction : un mécanisme de propagation, borné à un domaine de confiance.** Le
document en est, au 21 juillet 2026, à sa **révision -09 du 6 juillet 2026**, expirant le **7 janvier
2027**, à l'état d'appel de dernière relecture du groupe de travail OAuth : *Internet-Draft* en cours,
**non un RFC** (Vol. III F-29, **[A]** ; statut et expiration dits à chaque mention). ⚠ **La date du
7 janvier 2027 est l'expiration automatique du document — PROGRAMMÉE au sens mécanique**, elle ne dit
rien d'une adoption ni d'un calendrier de publication. Son abrégé énonce l'objet et **la clause qui
compte pour ce chapitre est la borne de périmètre** : la propagation vaut **within a trusted
domain**. *Le § 17.6 y revient.*

⚠ **Le socle IAM pré-agentique — dont l'autorisation déléguée fait partie — est posé au ch. 3** et
n'est pas reconstruit ici : ce chapitre s'y adosse, et n'instruit que ce que les trois mécanismes
**ajoutent** au patron hérité.

## § 17.2 — La chaîne de délégation comme objet de première classe

Lecture de l'auteur — **la mise en rang qui suit est une construction de la somme.** **Ce que le socle
établit** : trois faits séparés, un par mécanisme (F-46, **[B]** ; F-47, **[A]** ; F-29, **[A]**).
**Ce qu'il n'établit pas** : un **classement** entre eux — aucun lot n'a balayé de corpus de
mécanismes, et « énoncer la chaîne comme structure propre » est un **critère d'auteur**, non un
attribut documenté.

*Les trois mécanismes se distinguent moins par leur maturité que par le rang qu'ils accordent à la
chaîne.*

Des trois, le **document d'autorisation d'agent** de la spécification de paiement est celui qui
décrit la chaîne **comme l'objet qu'il spécifie**. Il la formule ainsi — *source primaire ouverte et
citée hors socle par le Vol. III* : « Mandates form a cryptographically verifiable chain from the
original user-approved Mandate through to the closed Mandate used to authorize a particular Verifier's
action. » ⚠ **Le même balayage, borné à ce seul fichier, relève que ce document n'invoque pas OAuth** :
les chaînes correspondantes n'y figurent pas, les références externes relevées étant d'un autre
corpus. ⚠ *Ce constat ne réfute aucune compatibilité : il établit que **ce fichier** ne l'invoque pas,
à cette date.*

Le **RFC 8693**, à l'inverse, traite la chaîne comme un **attribut d'un jeton dont il décline
expressément la sécurité** (F-47). Les **jetons de transaction** nomment eux aussi une chaîne
d'appels, mais **la bornent** : ils la situent **à l'intérieur d'un domaine de confiance** — *ce qui
est précisément la frontière que l'entreprise franchit dès qu'un agent tiers entre en jeu*, objet du
**ch. 18**.

⚠ **Aucun des trois n'est un mécanisme d'émission, et c'est ce qui sépare ce chapitre du § 15.1.** La
carte d'agent signée — dont le socle hérité **ne documente ni l'ancrage de confiance, ni la
révocation, ni la gouvernance des clés** (Vol. III H-01, **[A]**) — porte une **identité**, non un
**mandat**. *Les deux objets se vérifient séparément, et l'un ne se déduit pas de l'autre.*

**Ce que le Vol. I ajoute en régime [C], et qui nomme le patron sans l'établir.** Son §2.11.2 pose que
l'agent en production est une **identité non humaine à part entière**, et que la chaîne multi-saut est
le cœur du problème opérationnel : *un agent qui délègue à un sous-agent ou appelle un outil distant
**ne doit pas transmettre tel quel** le jeton du mandant, sous peine de surface d'attaque et de
privilèges propagés.* L'échange de jetons y répond en émettant, **à chaque saut**, un jeton dérivé à
**portée réduite** et à **audience explicite**, de sorte que chaque maillon ne reçoive que
l'habilitation strictement nécessaire et que la révocation reste granulaire. ⚠ **Régime** : entrée en
**[C]**, *repérage* — **aucun énoncé de ce paragraphe n'est central**, et le patron y entre comme
**thèse d'un volume antérieur, à attribuer**.

Lecture de l'auteur — traiter la chaîne de délégation en **objet de première classe** est une
construction de la somme, non un résultat du socle. **Ce que le socle établit** : un format de mandat
versionné et ses attributs temporels ; un attribut qui exprime qu'une délégation a eu lieu et
identifie la partie agissante ; un mécanisme de propagation pré-normatif, daté et borné à un domaine
de confiance. **Ce qu'il n'établit pas** : *qu'une chaîne ainsi formée soit interrogeable à un instant
quelconque*, ni *qu'un vérificateur situé au troisième maillon puisse remonter au mandant d'origine*,
ni *qu'un mandat révoqué en amont cesse d'être opposable en aval*. ⚠ **L'exigence d'interrogeabilité
à l'instant t vient de la grille du ch. 14, qui est elle-même une construction d'auteur** : ce
chapitre l'instruit, il ne la tire d'aucune source.

⚠ **Ce que les deux volumes antérieurs disent de cette frontière, ils le disent au titre de
repérage.** L'entrée qui recense les verrous de l'admission inter-domaines nomme parmi eux la
**fraîcheur d'autorité à chaque saut** (H-19, **[C]**) ; celle qui porte le front ouvert le formule
ainsi : *« l'identité non humaine et la traçabilité de bout en bout des décisions déléguées au-delà de
deux sauts restent des problèmes ouverts, dont l'urgence croît avec le degré d'autonomie consenti »*
(H-28, **[C]**). **Deux entrées [C] : elles situent la question, elles ne portent aucun fait central.**

⚠ **Une pièce inter-domaines existe, et ce chapitre la signale sans l'exploiter.** Un texte de l'IETF
traite nommément le **chaînage d'identité et d'autorisation entre domaines** — révision **-17 du
19 juillet 2026**, *Internet-Draft* actif du groupe de travail OAuth **soumis à l'IESG pour
publication**, expirant le 20 janvier 2027. ⚠ « **Soumis à l'IESG pour publication** » est un **état
de procédure, non une publication**, et **aucun jalon daté n'est relevé** : le chapitre n'écrit donc
aucune date d'aboutissement. **Son contenu n'a pas été extrait** — consigné au titre du « consulté mais
non retenu », sans affirmation ni citation. *Rien n'est écrit ici de ce que ce document prescrit ou
omet.*

## § 17.3 — Ce que le droit civil du mandat éclaire — et où l'analogie casse

⚠ **Le titre de cette section annonce une confrontation que le socle ne permet pas de conduire, et il
faut le dire avant d'écrire quoi que ce soit d'autre.** **Le socle ne documente pas le droit civil du
mandat — absence de documentation, non fait négatif vérifié** (degré 3). Le rapport du lot
correspondant le déclare lui-même : l'analogie figure parmi ce qu'il **n'a pas instruit**, faute de
source primaire relevant de son périmètre documentaire.

⚠ **Cette section est la seule occurrence de la matière dans toute la somme, et le partage est écrit
au plan** : le **versant québécois du mandat** — ce que le droit positif d'une juridiction donnée
prescrit — est au **ch. 27** ; **l'analyse de la limite de l'analogie** est ici. *Les deux ne se
recouvrent pas, et ce chapitre ne préjuge de rien de ce que le ch. 27 établira.*

**Ce qui peut s'écrire sans ce corpus est d'un autre ordre** : non pas ce que le droit dit, mais **ce
que les mécanismes du § 17.1 portent des attributs qu'un régime de mandat suppose**. *Et c'est là que
la comparaison rend son service, à condition d'être marquée.*

Lecture de l'auteur — **la mise en regard qui suit est une construction d'auteur.** **Ce que le socle
établit** : les mandats du protocole de paiement portent une **durée**, sous la forme d'attributs
temporels (F-46, **[B]**) ; le rapport de lot y ajoute, hors socle, une **portée** — marchands
autorisés, ensemble de lignes d'articles ; l'attribut d'acteur du RFC 8693 **identifie la partie
agissante** mais n'emporte **aucune assertion** sur le consentement du mandant, sur la portée
matérielle du mandat ni sur sa durée (F-47, **[A]**). **Ce qu'il n'établit pas** : *qu'un mandat
protocolaire soit **révocable avant son terme**, ni ce qu'une révocation produit sur les actes déjà
accomplis, ni **qui répond** des actes du mandataire.* ⚠ **Ces trois questions sont celles qu'un régime
civil traite en propre ; le socle n'en porte aucune réponse.**

| Ce qu'un régime de mandat suppose | Ce que les mécanismes du § 17.1 portent | État de la preuve |
|---|---|---|
| Une **durée** du mandat | attributs temporels d'émission et d'échéance (F-46, **[B]**) | établi, borné à ce format |
| Une **portée** matérielle | champs de portée pour les mandats ouverts | **hors socle** — rapport de lot, non versé |
| L'identité du **mandataire agissant** | attribut d'acteur du RFC 8693 (F-47, **[A]**) | établi ; **aucune assertion sur le consentement** |
| La **révocabilité avant terme** | — | **absence de documentation, degré 3** |
| L'effet d'une révocation sur les **actes déjà accomplis** | — | **absence de documentation, degré 3** |
| **Qui répond** des actes du mandataire | — | **absence de documentation, degré 3** |

: Tableau 17.1 — Ce qu'un régime de mandat suppose, ce que les mécanismes portent, au 21 juillet 2026.

**La révocation est le point où la comparaison rend le plus, et il n'est pas nécessaire de sortir du
socle pour le montrer.** Le précédent des infrastructures à clés publiques **n'offre pas ce qu'on lui
prête** : le RFC 7009 ne fait de l'invalidation des jetons d'accès qu'une **recommandation** ; le
RFC 5280 borne la granularité de la révocation à la **période d'émission de la liste** — *jusqu'à une
heure, un jour ou une semaine* ; et le RFC 6960 énonce que l'état « good » **ne signifie pas
nécessairement** que le certificat ait jamais été émis (Vol. III F-53, **[B]**). ⚠ *Un régime qui
laisse la révocation à une recommandation et sa fraîcheur à une période d'émission ne fournit pas, au
vérificateur du troisième maillon, de quoi savoir si le mandat qu'il honore est encore en vigueur.*
**L'inventaire complet est au ch. 20 § 20.4** ; il est cité ici **pour ce qu'il retire à l'analogie**,
non pour ce qu'il établit du droit.

## § 17.4 — L'humain, premier et dernier maillon

Lecture de l'auteur — **cette section est une construction d'auteur en totalité, et elle porte son
marquage à l'ouverture.** **Ce que le socle établit** : une obligation légale de révision par une
personne, dans un texte daté et en vigueur (F-89, **[B]** ; H-06, **[B]**) ; l'existence d'un **point
d'arrêt humain** comme **thèse d'un volume antérieur**, à attribuer et non à recevoir comme fait ; le
format et les attributs des mandats (F-46, **[B]**). **Ce qu'il n'établit pas** : qu'une approbation
humaine **doive** s'inscrire dans une chaîne de mandat, ni qu'une approbation non inscrite soit sans
valeur, ni qu'une **typologie des points d'intervention humaine** existe dans une source. *La
condition probatoire énoncée ci-dessous est la proposition de la somme ; le lecteur peut la refuser
sans qu'aucun fait cité ne tombe.*

**L'humain occupe deux positions dans la chaîne, et la somme soutient qu'elles se traitent par le même
instrument.** En **amont**, il est le **mandant** : l'origine de l'autorité que l'agent invoque. En
**aval**, il est le **réviseur** : celui devant qui une décision automatisée doit pouvoir être
reprise.

**Des deux positions, l'aval est celle que le socle adosse à un texte de droit.** L'article 12.1 de la
loi provinciale sur la protection des renseignements personnels dans le secteur privé impose à qui
rend une décision « **fondée exclusivement sur un traitement automatisé** » d'en informer la personne
concernée au plus tard au moment où elle l'informe de la décision, puis, **à sa demande**, de
l'informer de **trois choses** — les renseignements personnels utilisés, « des raisons, ainsi que des
principaux facteurs et paramètres, ayant mené à la décision », et « de son droit de faire rectifier
les renseignements personnels utilisés ». S'y ajoute, **dans un alinéa distinct**, l'occasion de
présenter ses observations à **un membre du personnel en mesure de réviser la décision** (F-89,
**[B]**, texte extrait de la source officielle ; cette entrée **corrige** une énumération héritée qui
omettait le droit de rectification).

⚠ **Le siège de cet article est le ch. 27**, qui cartographie les lectures sans les trancher ; ce qui
appartient ici est **le point de raccord avec la chaîne** : *la loi désigne une **personne en mesure
de réviser**, et le texte extrait n'y attache **aucune prescription sur la trace** que cette révision
laisse.* ⚠ **On n'écrit jamais « la révision de l'article 12.1 »** : le flux outille **un point d'arrêt
humain**, et la formule imposée ne se relâche pas.

**La position amont est nommée par une thèse du Vol. II et non par une source** : le **point d'arrêt
humain** figure parmi les cinq points de contrôle obligatoires de son ch. 19, où il porte lui-même le
marquage « Lecture de l'auteur ». *Il entre donc ici comme thèse d'un volume antérieur, à prolonger et
à attribuer, jamais comme acquis.* ⚠ **Collision terminologique héritée, signalée et non résolue** :
le glossaire du Vol. II réserve « point de contrôle » à la traduction d'une notion de reprise sur
incident, et « point de contrôle obligatoire » y désigne autre chose.

**Ce que le Vol. I ajoute en régime [C] : l'interaction elle-même devient un objet à négocier.** Son
§3.6.6 pose que la confiance ne se joue pas seulement entre systèmes mais **à l'interface où un humain
valide, corrige ou consent** — quand demander une validation, par quelle modalité, à quel point du
flux insérer le contrôle, comment recueillir un consentement granulaire. Trois mécanismes datés y
instrumentent cet axe : une primitive de **sollicitation structurée** introduite dans une révision du
protocole agent-outil, qui transforme l'interaction en primitive du protocole plutôt qu'en hors-bande
applicatif ; une extension d'**interfaces interactives en bac à sable** dont les actions transitent
par **le même chemin d'audit et de consentement** que les appels d'outils — *préservant la propriété
de traçabilité au lieu d'ouvrir un canal latéral non gouverné* ; et un **schéma d'événements**
normalisé entre frontal et dorsal agentique. ⚠ **Régime et statut** : entrée en **[C]**, et l'une des
trois extensions relevait, au gel du Vol. I, d'une **révision candidate non publiée comme stable** —
*sa présentation reste conditionnelle*.

⚠ **Le socle ne documente pas de typologie des patrons d'interaction humain-agent — absence de
documentation, degré 3.** ⚠ **Et les patrons que le plan nommait relèvent d'un corpus d'appui dont la
filiation a été retirée** : *marqueur conditionnel de réouverture, jamais une source.* La section s'en
tient donc à ce que les deux entrées permettent, et **déclare le reste plutôt que de l'emprunter**.

**Reste le fait qui donne à cette section son urgence**, et il vient de la spécification même dont le
§ 17.1 a détaillé les mandats. La version publiée le 28 avril 2026 se présente elle-même ainsi —
*source primaire ouverte et citée hors socle* : « This is the second release of AP2. It focuses on
providing Human Not Present flows. » ⚠ **Le mécanisme qui formalise le mandat est donc, dans sa
version courante, orienté vers les flux sans présence humaine.** *Ce n'est pas un défaut de la
spécification : c'est l'énoncé de ce qu'elle traite, et il indique où l'approbation humaine doit être
portée **par autre chose que la présence**.*

**La proposition de la somme tient en une phrase.** *Une approbation humaine qui ne s'inscrit pas dans
la chaîne de mandat — qui ne porte ni identifiant du mandant, ni horodatage, ni portée, ni lien
vérifiable vers le mandat qu'elle autorise — n'est pas un contrôle : c'est un rituel, et il est
indistinguable, dans un journal, d'une absence de contrôle.* Le corollaire est également d'auteur :
**un point d'arrêt humain se conçoit comme un acte de délégation daté et signé**, versé à la chaîne au
même titre que les maillons machine, et **non comme un événement d'interface**.

⚠ **Le socle ne porte cette proposition ni ne la contredit.** Ce qu'il fournit, ce sont **deux des
attributs qui la rendraient vérifiable** — un horodatage d'émission et une échéance (F-46) — et
**l'obligation légale qui la rend opposable devant un tiers** (F-89). ⚠ **Et l'échelle d'autonomie que
le ch. 14 § 14.4 croise avec la grille ne s'emploie jamais nue** : trois échelles homonymes coexistent
au Vol. I, et seuls le cardinal et la numérotation les discriminent.

## § 17.5 — Le biais d'automatisation et la supervision de façade

⚠ **Cette section n'a pas de socle, et elle ne peut pas en avoir un au moment où elle est écrite.**
Le TOC v0.24 la déclare **front neuf** en toutes lettres : *aucun des trois volumes ne la porte,
sources primaires à établir **avant rédaction***. La porte **G-1** dont relèverait cette constitution
**n'a pas été ouverte pour le Livre II** — son volet résiduel est explicitement dû —, et
**l'instruction d'auteur du 27 juillet 2026 n'a versé aucune source pour cette matière**.

**La section expose donc le vide, et refuse de le combler.** *Il serait aisé d'écrire ici deux pages
plausibles sur le tamponnage et le paradoxe de l'explicabilité ; ce serait exactement la faute que la
somme prend pour objet.* Trois motifs l'interdisent, et le troisième est le plus fort.

1. **Le régime de preuve du volume l'interdit.** Le PRD pose que toute affirmation factuelle centrale
   est adossée à une entrée du socle consolidé ou à une source primaire nouvelle de qualité
   équivalente (CA-IV-01). Il n'y a ici **ni l'une ni l'autre**.
2. **La règle du dépôt l'interdit.** *Aucune lacune déclarée d'un volume ne se comble par une source
   de moindre qualité.* Une section écrite de mémoire sur une littérature qu'on n'a pas ouverte est
   la source de moindre qualité par excellence.
3. **Et une construction d'auteur produite à l'endroit exact où le socle est muet est celle
   qu'aucune relecture ne peut réfuter, faute de fait auquel la confronter.** *C'est le motif que le
   Vol. III oppose à lui-même au terme de son ch. 10, et il vaut ici mot pour mot.*

**Ce qui peut s'écrire sans socle est ce qui rend la lacune instruisible**, et c'est le seul contenu
que cette section porte.

**L'objet de la section, formulé pour instruction.** Deux phénomènes distincts sont visés par le plan,
et ils ne se confondent pas. Le premier est **le tamponnage** : le mode d'échec par lequel une
révision humaine formellement présente cesse d'exercer un discernement, l'approbateur validant par
défaut ce que le système propose. Le second est **le paradoxe de l'explicabilité** : l'hypothèse
qu'une justification **mieux rédigée** augmente la **déférence** du réviseur plutôt que son
discernement — *plus l'explication est convaincante, moins elle est contestée, indépendamment de sa
justesse.*

⚠ **Ni l'un ni l'autre n'est établi ici, à aucun degré.** Le socle des trois volumes n'en porte
**aucune occurrence** : c'est une **absence de documentation dans le corpus de la somme, non un fait
négatif vérifié** — et il ne s'ensuit **ni** que ces phénomènes soient documentés ailleurs, **ni**
qu'ils ne le soient pas.

**Pourquoi cette lacune est structurante, et pour quel Livre.** Lecture de l'auteur — *ce que le socle
établit* : l'article 12.1 ouvre l'occasion d'être entendu par **un membre du personnel en mesure de
réviser** (F-89, **[B]**) ; la ligne directrice prudentielle **attend** une surveillance visant
nommément la prise de décision autonome et la reparamétrisation autonome (Vol. III F-65, **[B]** ;
H-04). *Ce qu'il n'établit pas* : **que cette révision humaine soit effective**. ⚠ **La parade sur
laquelle reposent l'article 12.1 (ch. 27) et la supervision attendue par E-23 (ch. 25) est une parade
humaine, et sa limite empirique n'est documentée nulle part dans la somme.** *Un cadre réglementaire
dont la parade est un humain qui révise suppose que cet humain révise ; et c'est précisément ce que le
socle ne dit pas.*

⚠ **Ce n'est pas un argument contre ces cadres, et il ne faut pas le lire ainsi.** C'est un **angle
mort déclaré** du même ordre que ceux que les risques du plan nomment : *la somme prescrit un point
d'arrêt humain (§ 17.4) et le Livre III en fera une condition de conformité, sans qu'aucune entrée
n'établisse à quelles conditions un point d'arrêt humain arrête effectivement quelque chose.*

**Question formulée pour instruction**, avec son corpus et son critère de clôture :
*existe-t-il une littérature revue par les pairs établissant, sur des systèmes de décision assistée
en contexte professionnel, (a) la prévalence de la validation par défaut d'une recommandation
automatisée, et (b) l'effet de la qualité rédactionnelle d'une justification sur le taux de
contestation de cette recommandation ?* **Corpus à ouvrir** : la littérature d'ergonomie cognitive et
de facteurs humains sur la confiance dans l'automatisation ; les études d'aide à la décision clinique
et aéronautique ; les travaux d'évaluation des interfaces d'explicabilité. **Critère de clôture** :
au moins un résultat **revu par les pairs**, avec son protocole, sa population et sa taille d'effet —
*et non une revue de littérature secondaire, ni un billet d'éditeur.* **La question reste ouverte ;
aucune inférence n'est proposée ici.**

## § 17.6 — Le problème des deux sauts

### 17.6.1 Pourquoi deux sauts : où chaque mécanisme perd le fil

**D'où vient le nombre, et ce qu'il vaut.** Le « deux sauts » **n'est pas une mesure** : c'est la
formulation d'un front ouvert par le Vol. I (H-28, **[C]**), qui range par ailleurs le verrou parmi
les dominants de la strate entreprise (H-29, **[C]**). ⚠ **Deux entrées de repérage : elles situent la
question, elles ne portent aucun fait central.** *Aucune entrée du socle propre ne compte de sauts,
n'en fixe le seuil, ni ne définit le terme.*

Faute de définition héritée, le chapitre en emploie une **et la déclare** : **un saut de délégation
est le transfert, d'un détenteur à un autre, de l'autorité d'agir pour le compte d'un mandant
d'origine.** Le premier saut mène du mandant au premier mandataire ; le deuxième mène de celui-ci à un
troisième acteur, **qui n'a jamais été en présence du mandant**. *C'est cette configuration, et non un
décompte, qui est examinée.*

**Le mandat protocolaire perd le fil à l'ancrage.** Ce que la spécification **démontre** est un format
et un jeu d'attributs (F-46, **[B]**). Ce qu'elle **laisse au déploiement** — l'obligation
d'appariement exact du type, la remise de l'ancrage de confiance, les deux modèles alternatifs —
**n'est pas porté par le socle** : ces éléments vivent dans le rapport de lot, et sont attribués ici à
ce titre. ⚠ *La vérifiabilité de la chaîne est celle de sa **sérialisation** ; l'autorité à laquelle un
vérificateur situé loin du mandant doit se fier reste une **décision de déploiement**.*

**Le mécanisme d'échange perd le fil au périmètre qu'il s'est lui-même donné.** Le RFC 8693 définit
l'attribut qui exprime la délégation, et **place explicitement hors périmètre** la sécurité des jetons
(F-47, **[A]**). ⚠ **Ce que ce texte prévoit ou tait de la composition de plusieurs délégations
successives n'est pas documenté par le socle — degré 3.** *Il ne s'ensuit ni qu'une telle composition
soit prévue, ni qu'elle ne le soit pas.*

**Le mécanisme de propagation perd le fil à la frontière du domaine — et c'est lui qui l'écrit.** La
clause décisive de son abrégé est **within a trusted domain** : *le mécanisme borne son propre
périmètre à un domaine de confiance.* L'entreprise franchit cette frontière **dès qu'un agent tiers
entre en jeu** — objet du **ch. 18 § 18.2**, dont l'établissement est que, **du côté du protocole
agent-agent et de lui seul**, l'admission d'un agent tiers **ne dispose d'aucun plancher normatif**.

**Et l'identité elle-même ne se revérifie pas en chemin.** La carte signée pose au niveau normatif le
plus fort que les clés expirées ou révoquées **MUST NOT** servir à la vérification, **sans fournir de
mécanisme** permettant au client d'établir cette expiration ou cette révocation (F-07, **[A]** ; siège
au ch. 15 § 15.1.3, inventaire au ch. 20 § 20.4). ⚠ **L'interdiction porte sur la clé, non sur la
carte** — borne de l'entrée, et *elle change ce qu'un vérificateur aval peut en tirer.*

**Ce que la littérature d'attaque nomme, et qui est le même point vu de l'autre côté.** Le corpus de
techniques adverses range parmi ses entrées l'invocation d'outils par un agent : *un agent peut
disposer d'outils inaccessibles aux utilisateurs, de sorte que l'abus de l'accès à l'agent confère des
privilèges supérieurs* (F-14, **[A]**) ; **le maillon qui cède n'est pas l'authentification de
l'agent, mais l'absence de réduction de portée entre mandant et mandataire.** La contre-mesure
correspondante pose la condition inverse : *un agent agissant pour un utilisateur ne doit pas recevoir
de permissions que cet utilisateur n'a pas* (F-15, **[A]**). ⚠ **Traitement défensif** : la mécanique
est exposée **au niveau du maillon**, l'identifiant de technique est cité, et **aucune recette n'est
reproduite** ; le siège de la taxonomie est le **ch. 19**. ⚠ *Ces deux entrées énoncent une **condition
d'atténuation** ; elles ne décrivent pas le mécanisme qui l'appliquerait à un maillon situé au-delà du
premier.*

Lecture de l'auteur — **ce que le socle établit** : quatre **périmètres déclarés**, chacun par sa
source. **Ce qu'il n'établit pas** : que ces quatre périmètres **se composent** en une frontière
unique, ni qu'ils se referment **au deuxième saut**. *La lecture proposée est que la perte ne se
produit pas à un rang numéroté, mais **au premier changement de régime** — lorsque le vérificateur
cesse d'être celui qui a ancré le mandat, ou cesse d'appartenir au domaine où le contexte se propage.
Sous cette lecture, « deux sauts » nomme le premier cas de figure où ce changement devient inévitable,
non un seuil mesuré.*

### 17.6.2 Trois pistes, et ce que le socle établit de chacune

⚠ **Le terme « limites démontrées » mérite d'être borné avant d'écrire quoi que ce soit** : **aucune
des trois pistes n'a fait l'objet d'une démonstration** au sens où R-02 l'entend. *Ce que le socle
porte, ce sont des **statuts datés** et des **périmètres déclarés*** — ce qui suffit à situer chaque
piste, et ne suffit pas à la réfuter.

| Piste | Ce que le socle établit | Le périmètre déclaré, et ce qui n'est pas documenté |
|---|---|---|
| **Jetons imbriqués** | l'attribut d'acteur exprime qu'une délégation a eu lieu et identifie la partie agissante (F-47, **[A]**) ; jetons de transaction en révision -09 du 6 juillet 2026, en appel de dernière relecture (F-29, **[A]**) | le RFC 8693 **exclut** la sécurité du jeton (F-47) ; l'abrégé des jetons de transaction **borne** la chaîne à un domaine de confiance. **La composition sur plus d'un saut : absence de documentation, degré 3** |
| **Accréditations vérifiables chaînées** | modèle de données v2.0, Recommandation du 15 mai 2025, historique sans entrée postérieure (F-79, **[B]**) ; v2.1 en brouillon de travail du 11 mai 2026 (F-80, **[B]**) ; identifiants décentralisés v1.1 à l'instantané de recommandation candidate du 5 mars 2026 (F-82, **[A]**) | le corpus documenté est celui d'un **format d'attestation**, non d'un mécanisme de chaînage de mandat. L'aboutissement de la v2.1 est **SPÉCULATIF**. **Un mécanisme de chaînage pour la délégation multi-saut : degré 3** |
| **Journalisation corrélée** | conventions sémantiques pour l'IA générative déplacées vers un dépôt dédié par une rupture déclarée du 12 juin 2026 (F-74, **[B]**) ; échelle de maturité **des groupes de conventions** à cinq échelons (F-76, **[B]**) ; deux fichiers agentiques relevés au **premier échelon** (F-77, **[B]**) | le dépôt dédié ne porte **ni publication ni étiquette**, et son adresse de schéma indique « TODO » : **aucun numéro de version propre n'est citable** (F-75, **[B, degré 2]**). **La corrélation d'une trace avec une chaîne de mandat : degré 3** |

: Tableau 17.2 — Trois pistes pour la traçabilité multi-saut, leur statut et leur périmètre déclaré, au 21 juillet 2026.

**Première piste — imbriquer les jetons.** Les deux textes qui la portent **posent eux-mêmes leur
borne** : l'un **exclut** de son champ la sécurité du jeton qui porte la délégation, l'autre **borne**
la propagation du contexte à un domaine de confiance. Un troisième texte de l'IETF traite nommément le
chaînage **entre domaines** : il a été **repéré, son contenu n'a pas été extrait** (§ 17.2).

**Deuxième piste — chaîner les accréditations vérifiables.** Le corpus est daté, et son état ne se
résume pas à un adjectif (siège : **ch. 13 § 13.1**, non rejoué ici). ⚠ **Ce qui appartient à ce
paragraphe est l'écart entre l'objet documenté et l'objet cherché** : *ce corpus spécifie un format
d'attestation ; le socle ne documente pas de mécanisme par lequel des accréditations s'enchaîneraient
pour porter une délégation d'un maillon au suivant — degré 3.* ⚠ Deux constats **bornent la piste sans
la fermer** : un groupe communautaire annonce parmi ses livrables une méthode d'identifiant et un
format d'accréditation d'agent (F-30, **[B]**) — mais **un groupe communautaire ne produit pas de
Recommandation et n'engage aucun calendrier**, et ce groupe n'avait **publié ni rapport ni brouillon**
au relevé (F-50) ; et le rapport d'interopérabilité du modèle de données énumère dix implémentations
dont **aucun intitulé** ne désigne un acteur financier — ⚠ *fait négatif borné aux intitulés, non à la
nature des organisations*, entrée en **[C]**, corroboration seule (F-31).

**Troisième piste — corréler les journaux.** Le relevé est d'une autre nature que les deux
précédents : *il ne décrit pas ce qu'une spécification prescrit, mais l'état d'un jeu de conventions
d'instrumentation.* ⚠ **Une conformité annoncée peut pointer un millésime périmé** : la documentation
d'un éditeur nommé énonce sa conformité par référence à un millésime du **dépôt principal** publié le
25 août 2025, **antérieur au déplacement** (F-78, **[B]**). *Le siège de ce dossier est le ch. 38 ; il
n'est pas instruit ici.* ⚠ **Deux réserves achèvent de borner la piste** : le rapport de lot **déclare
lui-même** n'avoir pas ouvert le document du dépôt dédié qu'il désigne comme **la pièce de jonction de
cette corrélation**, et qualifie ce manque de **lacune la plus coûteuse** du lot ; et le cadre
empirique hérité du Vol. II enseigne que **la journalisation confiée aux agents « n'est généralement
pas recommandée »** (H-12, **[B]**) — ⚠ *source unique, préimpression non révisée par les pairs, sans
reproduction indépendante*, réserve que le socle porte expressément.

Lecture de l'auteur — **le classement des trois pistes en un ordre de promesse n'est pas proposé.**
**Ce que le socle établit** : trois objets documentés de nature différente — un attribut de jeton et
un mécanisme de propagation pré-normatif, un format d'attestation avec son historique, un jeu de
conventions au premier échelon de son échelle et sans version citable. **Ce qu'il n'établit pas** :
qu'aucune des trois ne puisse porter une traçabilité multi-saut, ni qu'une combinaison des trois y
parviendrait. *La lecture proposée est qu'**aucune des trois n'a été conçue pour l'objet cherché** —
deux spécifient autre chose, la troisième **observe** au lieu d'**attester** — et que les traiter en
solutions candidates suppose une transposition dont personne n'a écrit les conditions.*

### 17.6.3 Question de recherche formulée pour instruction

**Ce que ce chapitre produit n'est pas une réponse : c'est une question instruisible.** *La distinction
est la thèse du Livre appliquée à lui-même — un ouvrage qui prend la traçabilité pour objet et comble
ses trous par construction se réfute lui-même.*

⚠ **La lacune est ouverte et non instruite** : *existe-t-il un mécanisme documenté par lequel un
vérificateur situé au-delà du premier maillon établisse, à l'instant où il agit, l'identité du mandant
d'origine, la portée du mandat et sa validité courante ?* **Aucune passe de recherche n'a été
conduite** — le lot du mandat déclare le problème hors de son périmètre, et le lot vers lequel il
renvoie a porté sur la vérification d'agent tiers, non sur la délégation multi-saut. **Sources à
retrouver** : le texte de l'IETF sur le chaînage entre domaines, dont le contenu reste non extrait ;
les dispositions de propagation d'état des spécifications de registre dans leurs révisions courantes ;
les mécanismes d'atténuation de portée entre maillons, que la contre-mesure du § 17.6.1 pose **en
condition sans les documenter**.

Lecture de l'auteur — **la décomposition qui suit est une construction de la somme.** **Ce que le
socle établit** : les quatre périmètres déclarés du § 17.6.1 et les trois états de piste du § 17.6.2.
**Ce qu'il n'établit pas** : que ces cinq sous-questions soient les bonnes, ni qu'elles épuisent le
problème, ni qu'une réponse à chacune **composerait** une réponse à l'ensemble — *c'est précisément la
présomption de composition que la non-compositionnalité de la sûreté invite à traiter avec méfiance*
(siège : **ch. 37 § 37.3**). *Elles valent comme programme, non comme résultat.*

1. **L'atténuation.** Un mécanisme documenté impose-t-il que la portée d'un mandat **décroisse**, ou
   au moins ne croisse pas, d'un maillon au suivant ? *Corpus* : textes de l'IETF sur le chaînage
   entre domaines, spécifications de mandat, langages de politique. *Critère de clôture* : un énoncé
   **normatif** nommant la portée transmise, cité et daté — **non une atténuation posée en principe**.
2. **La fraîcheur.** Un vérificateur au-delà du premier maillon dispose-t-il d'un moyen documenté
   d'établir qu'un mandat amont est **encore en vigueur** à l'instant où il agit ? *Corpus* :
   mécanismes de révocation et de statut, dispositions de propagation d'état des registres. *Critère*
   : un **budget de fraîcheur** ou un **délai de propagation** écrit dans un texte. ⚠ Le Vol. I nommait
   déjà ce verrou (H-19, **[C]**, repérage seul) ; le **ch. 20 § 20.6** établit que le socle n'en
   documente pas la cascade.
3. **L'ancrage transitif.** Lorsque l'ancrage de confiance est renvoyé au déploiement, **quelle règle
   documentée** permet à un vérificateur d'accepter l'ancrage retenu par un maillon amont qu'il ne
   connaît pas ? *Corpus* : modèles de confiance des spécifications de mandat, précédents
   institutionnels de fédération (**ch. 18 § 18.3**). *Critère* : une **procédure écrite**, non un
   modèle laissé au choix de l'intégrateur.
4. **La preuve.** Que faut-il produire, et sous quelle forme, pour qu'une chaîne de mandat soit
   **opposable devant un tiers** — auditeur, régulateur, contrepartie ? *Corpus* : cadres de
   conformité du Livre III, journalisation probatoire du **ch. 38**. *Critère* : l'énoncé, par une
   source, de **ce qui fait d'une trace une preuve** — le socle n'en porte aucun à date.
5. **L'imputabilité.** Au troisième maillon, **qui répond de l'acte** ? La cinquième question de la
   grille appelle une imputabilité traçable jusqu'à une personne ou une entité juridique. *Corpus* :
   régimes de responsabilité, obligations de révision humaine. *Critère* : le **rattachement documenté**
   d'un acte de maillon terminal à une entité juridique nommée.

**Ce que le chapitre refuse de faire, et pourquoi il l'écrit.** *Il serait aisé de proposer ici un
dispositif — un jeton portant la chaîne complète, un registre interrogeable à chaque saut, une
accréditation par maillon.* **Trois motifs l'interdisent.** Le premier : *l'absence de mécanisme
documenté n'est pas une preuve d'impossibilité, et elle n'est pas davantage un mandat de conception.*
Le second : **le passeport d'agent est déjà un objet de synthèse construit par la somme** (ch. 16) ;
en ajouter un second, non assemblé de pièces documentées, reviendrait à **fabriquer le standard que la
somme prétend décrire**. Le troisième est de méthode, et il est le même qu'au § 17.5 : *une
construction d'auteur produite à l'endroit exact où le socle est muet est celle qu'aucune relecture ne
peut réfuter.*

**Reste ce que le chapitre peut affirmer, et qui n'est pas rien.** La frontière est **localisée** :
elle passe là où le vérificateur cesse d'être celui qui a ancré le mandat, ou cesse d'appartenir au
domaine où le contexte se propage. Elle est **datée**. Et elle est **instruisible** : *les cinq
questions ci-dessus nomment leur corpus et leur critère de clôture, ce qui les distingue d'un constat
d'ignorance.*

### Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **La définition du saut de délégation**, déclarée faute d'être héritée. Les **ch. 18, 20 et 21** la
   citent ; aucun ne la redéfinit.
2. **La localisation de la frontière** : *au premier changement de régime*, non à un rang numéroté.
   C'est ce qui transforme « deux sauts » d'un décompte en un critère.
3. **Le point d'arrêt humain comme acte de délégation daté et signé** — proposition de la somme, qui
   descend au **ch. 27** et au **ch. 25** comme condition, et qui **suppose** ce que le § 17.5 déclare
   non établi.
4. **Cinq questions instruisibles**, avec leur corpus et leur critère de clôture. Le **ch. 49** les
   reprendra à l'état final des lacunes.
5. ⚠ **Et un legs négatif, qui est le plus important** : le § 17.5 **n'a pas de socle**, et la parade
   sur laquelle le Livre III fonde deux de ses obligations n'a **aucune limite empirique documentée
   dans la somme**.

---

## § 17.7 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui est enfreint.** Portes **G-3** et **G-4** ; volet résiduel de **G-1** non instruit ; ordre de
rédaction du PRD §6. ⚠ **Et une consigne explicite du plan est enfreinte** : le § 17.5 est déclaré
**front neuf, sources primaires à établir avant rédaction**, et il a été rédigé **sans elles** — voir
**R-IV-27**. Instruction d'auteur du 27 juillet 2026.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ **Et le § 17.5 est un cas à part dans tout le
   Livre** : il ne mobilise **aucune entrée**, à aucun niveau. *Il ne s'agit pas d'un énoncé faible,
   mais d'une section qui n'en porte aucun.*
2. **Les décomptes sont publiables** (G-2). Écart de **+18,3 %** ; la volumétrie du Livre alimente
   **D-4** par **R-IV-17**.
3. **Les renvois « ch. N » vers les Livres III à V sont des renvois de plan** : **ch. 25**, **ch. 27**,
   **ch. 37 § 37.3**, **ch. 38** et **ch. 49**. ⚠ Deux d'entre eux sont **structurants** — le ch. 27
   est le **siège du versant québécois du mandat**, dont ce chapitre déclare ne pas préjuger, et le
   ch. 25 porte la supervision dont le § 17.5 déclare la limite non documentée. Les renvois vers les
   **ch. 3, 10** résolvent contre du texte ; ceux vers les **ch. 13, 14, 15, 16, 18, 19, 20, 21**
   résolvent contre du texte au terme de la présente passe.
4. **Une relève porte une date postérieure au gel de sa source** (§ 17.1, document consulté le
   26 juillet 2026) : elle est reprise **comme relève**, jamais comme entrée de socle, et **n'appuie
   aucun énoncé**.

**Remontées ouvertes par ce chapitre :**

- **R-IV-27 — BLOQUANTE pour la publication du § 17.5, et structurante pour le Livre III.** Le TOC
  déclare cette section **front neuf** et exige que ses **sources primaires soient établies avant
  rédaction** ; elles ne l'ont pas été, et la section **expose le vide au lieu de le combler**.
  ⚠ **La conséquence excède ce chapitre** : la section est la **limite empirique de la parade** sur
  laquelle reposent l'art. 12.1 (**ch. 27**) et la supervision attendue par E-23 (**ch. 25**). *Un
  cadre dont la parade est un humain qui révise suppose que cet humain révise ; la somme le suppose et
  ne l'établit pas.* **Demande remontée** : ouverture d'un **lot d'instruction dédié** avec le corpus
  et le critère de clôture que le § 17.5 formule, **avant** la rédaction du Livre III — faute de quoi
  deux chapitres du Livre III s'appuieront sur une parade dont la somme déclare elle-même ne rien
  savoir. ⚠ **Le rédacteur n'écrit pas la section sur une littérature qu'il n'a pas ouverte** :
  c'est le seul geste qui rendrait la lacune invisible.
- **R-IV-28 — non bloquante, de thèse ; quatrième occurrence d'une même classe.** La thèse du ch. 17
  au TOC v0.24 porte **trois termes** que le Vol. III a **lui-même bornés le 21 juillet 2026** : le
  verbe « **prouvent** », que R-02 proscrit ; le classement « **presque aucun** », quantificateur sur
  un corpus non balayé ; et « **aucun mécanisme documenté** », quantificateur universel négatif que le
  régime des trois degrés refuse. Ses thèses rectifiées portent « aucun des mécanismes **instruits par
  ce volume** ne documente ». **Le TOC du compendium porte encore les formes larges.** La pièce cite
  la thèse verbatim et écrit son corps aux formes bornées. **Demande remontée** : la **passe de
  réalignement systématique** déjà demandée en R-IV-25 — *quatre thèses du Livre II sur dix portent une
  forme que leur source a corrigée après coup, et c'est exactement l'objet du volet de fond de G-4.*
- **R-IV-29 — non bloquante, de siège.** Le § 17.1 est désigné par le TOC comme le **siège de la
  relève sur le RFC 8693**, dont le plan dit qu'elle rend la thèse « **possiblement sous-spécifiée,
  non fausse** ». ⚠ **Or une relève n'entre pas au socle, et un siège de relève n'est pas un siège de
  fait** : la pièce l'a donc portée **comme relève**, sans qu'aucun énoncé ne s'y adosse. **Demande
  remontée** : que **G-1** consomme cette relève **par extraction** — la RFC est un document de la voie
  des normes, publiquement accessible, et son extraction est **le moins coûteux des versements que le
  Livre appelle**. *Tant qu'elle n'est pas faite, la thèse du chapitre reste sous-spécifiée et la pièce
  l'écrit.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.24** — § 17.1 à § 17.6,
avec ses trois sous-sections, dans l'ordre exact —, et le § 17.0 est une introduction de chapitre. La
**table de couverture est respectée pour ses cinq lignes**, y compris la cinquième, qui déclare le
§ 17.5 **socle à constituer** : *la pièce l'a laissé à constituer plutôt que de le simuler.* **Aucun
verdict de grille n'est rendu**, conformément à la règle d'emploi 5 : le chapitre **instruit Q-C**. La
**divergence de gouvernance de la spécification de paiement n'est pas rouverte** : elle reste tranchée
au **ch. 10**. Le **socle IAM reste au ch. 3** ; l'**inventaire de la révocation au ch. 20 § 20.4** ;
la **taxonomie des attaques au ch. 19** ; le **versant québécois du mandat au ch. 27**. Les **quinze
occurrences de R-14** portent leur degré, dont **douze au degré 3**. Les **sept occurrences de R-02**
énoncent ce que le mécanisme démontre **et** ne démontre pas. Le **traitement défensif du § 17.6.1**
est tenu **au niveau du maillon**, identifiants cités, **aucune recette reproduite**. La **collision
terminologique du Vol. II est signalée et non résolue**. Et les **dix occurrences de « Lecture de
l'auteur »** sont suivies de ce que le socle établit et n'établit pas — dont **une section entière**,
le § 17.4, marquée à l'ouverture.


---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-27 — close par la décision d'auteur D-9, neuve : lot d'instruction ouvert, blocage
  maintenu.** ⚠ **L'issue de D-7 — périmètre assumé et déclaré — a été examinée et écartée**, et le
  motif est la différence entre les deux cas : le risque 15 nommait une matière que la somme **ne
  prescrit pas**, quand ici **deux chapitres du Livre III prescriront une parade — l'humain qui
  révise — dont ce § 17.5 est la limite empirique**. *Un cadre dont la parade est un humain qui révise
  suppose que cet humain révise ; assumer le périmètre reviendrait à prescrire la parade en déclarant
  ne rien savoir de son efficacité.* **Le lot reprend le corpus et le critère de clôture que le
  § 17.5 formule** — la pièce les a écrits plutôt que d'écrire la section, et c'était le seul geste
  admissible. ⚠ **Le blocage tient et il est nommé** : les **ch. 25 et 27 ne se lancent pas** avant
  clôture. ⚠ **Et rien n'est effacé** : la section a été rédigée contre une consigne explicite du
  plan ; *l'arbitrage qui suit une infraction ne la rattrape pas.*
- **R-IV-28 — close par réalignement du plan (TOC v0.25, décisions 8 et 14).** Les **trois** termes
  tombent ensemble : « prouvent » (proscrit par **R-02**), « presque aucun » (quantificateur sur un
  corpus non balayé) et « aucun mécanisme documenté » (quantificateur universel négatif). **Le corps
  n'a pas changé** : il était écrit aux formes bornées.
- **R-IV-29 — close par consommation de la relève, PAR EXTRACTION à la source primaire** (G-1,
  27 juillet 2026, aux deux sièges du document). ⚠ **Et l'extraction a établi l'inverse de ce que la
  relève supposait.** Le plan tenait la thèse pour « possiblement sous-spécifiée » ; la RFC **exclut
  expressément** les maillons antérieurs de toute décision d'autorisation, les donnant pour
  *informational only*. *La traçabilité opposable de bout en bout n'y manque pas par omission : elle y
  est écartée par prescription.* Le § 17.1 nomme désormais la RFC, son statut et cette clause —
  *taire une spécification normative qui donne raison à la thèse serait le même défaut que la taire
  quand elle la contredit.* ⚠ **L'extraction n'entre pas au socle** : c'est **G-3** qui l'y ferait.

⚠ **Ce que la clôture ne change pas.** Les portes **G-3** et **G-4** demeurent ouvertes : le socle
consolidé compte **zéro entrée**, l'Annexe B n'existe pas, la collation de fond contre le Vol. III
rédigé n'est pas conduite, et **aucun énoncé de cette pièce n'est central au sens de CA-IV-01**.
**CA-IV-13 n'est pas satisfaite** — aucune relecture par un relecteur distinct du rédacteur. Cette
pièce reste un **brouillon non publiable**. *Zéro remontée ouverte ne veut pas dire pièce recevable :
cela veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée.*
