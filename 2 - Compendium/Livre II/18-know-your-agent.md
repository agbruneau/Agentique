# Chapitre 18 — Know Your Agent : la vérification d'agent tiers inter-domaines

*Livre II — Faire confiance : identité, délégation et fabrique de confiance.
Premier mouvement — émettre (ch. 12-18). **Dernier chapitre du mouvement** : il porte la question à la
frontière de l'organisation, là où l'émission cesse d'être un acte interne.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — portes **G-3** et **G-4** ouvertes ; instruction d'auteur du 27 juillet 2026. ⚠ **Ce chapitre porte le SIÈGE UNIQUE du KYA pour toute la somme** (§ 18.1) : les ch. 13 § 13.2, 15 § 15.2.3 et 16 § 16.3 y renvoient et **n'instruisent pas le sigle**. **R-IV-16 et R-IV-17, ouvertes au ch. 12, valent pour tout le Livre** |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit.** Gels de source : **juin 2026** (Vol. I), **21 juillet 2026** (Vol. III). ⚠ **Ce chapitre est le plus dense en objets périssables du mouvement** : neuf chantiers relevés, dont **deux dates d'expiration d'*Internet-Drafts* déjà échues ou proches** au moment où la pièce est écrite, et une ratification annoncée **sans date** |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (G-3 ouverte). Résolution contre le **Vol. III *Monographie* ch. 11**, dont les entrées **F-04**, **F-06**, **F-07**, **F-09**, **F-30**, **F-32**, **F-33** à **F-35**, **F-38**, **F-40**, **F-43**, **F-48** à **F-51**, **F-56**, **F-73**, **F-83**, **F-86**, **F-87** et les entrées héritées **H-19** conservent leurs niveaux d'origine ; et contre le **Vol. I *Monographie* §5.5.4, §3.6.5 et §7.4.3**, en **[C]**. ⚠ **H-19 est en [C]** : l'énoncé « aucun forum n'avait tranché » entre comme **thèse d'un volume antérieur, attribuée et datée de son gel de juin 2026**, non comme fait vérifié. **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | Vol. III — **R-05 (le KYA n'est pas un standard établi ; « terme de marché » est une construction d'auteur, non une formule du Vol. I) : ce chapitre en est le SIÈGE — cinq occurrences**, § 18.0, § 18.1 (trois) et § 18.3 ; **R-09 : onze occurrences**, dont la clause du groupe communautaire **répétée à chaque mention** ; **R-14 : dix occurrences**, dont **huit de degré 3** ; **R-02 : cinq occurrences**, § 18.2 (trois) et § 18.3 (deux) ; **R-03 (« entreprise agentique », jamais une catégorie établie) : une occurrence**, § 18.3 ; **R-13 : une occurrence**, § 18.3, les niveaux de certification jamais confondus avec une échelle d'autonomie. **R-01, R-04, R-06 à R-08, R-10 à R-12 : zéro occurrence.** Vol. II — **§8.2 : une occurrence**, § 18.1, le décompte de participants attribué à la page qui l'affiche ; **PRD Vol. II §8.2.5 : six occurrences** ; **R-1 à R-8 : zéro occurrence** |
| **Volumétrie cible** | ≈ **3 800 mots** de corps (§ 18.0 à § 18.4), **cible dérivée** de l'enveloppe du Livre (50 000 mots, TOC v0.24) au prorata des sections. ☑ **Décompte publiable depuis G-2** ; **réel : 4 202 mots** par [`PRD/decompte.sh`](../PRD/decompte.sh) — **+10,6 %**. ⚠ La volumétrie du Livre est relevée au [`README.md`](README.md) du dossier et alimente **D-4** par **R-IV-17** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.24, entrée du chapitre 18)* — le KYA transpose la logique du KYC — vérifier avant d'admettre — sans l'infrastructure institutionnelle qui rend le KYC possible ; la *trust fabric* inter-entreprises reste privée et fragmentée, et c'est elle qui décide si l'entreprise agentique s'arrête à ses murs.

---

## § 18.0 — Introduction : le point où l'identité cesse d'être interne

Une organisation qui admet chez elle **l'agent d'une autre organisation** prend une décision dont elle
ne maîtrise **ni l'émission, ni le mandant, ni le cycle de vie**. Elle ne peut pas auditer la fabrique
d'identité d'un tiers ; elle ne peut pas révoquer ce qu'elle n'a pas émis ; et elle ne dispose, pour
trancher, que de **ce que le tiers veut bien lui présenter**.

*C'est le point où la question de l'identité cesse d'être interne et devient une question de
frontière.* C'est aussi le point où **le vocabulaire du domaine devance ses institutions**, et le
chapitre commence par poser cet écart plutôt que de l'employer.

> ⚠ **SIÈGE UNIQUE DU KYA POUR TOUTE LA SOMME.** La connaissance de l'agent — *Know Your Agent*, KYA
> — est **posée ici une seule fois**, au § 18.1. Les **ch. 13 § 13.2, ch. 15 § 15.2.3 et ch. 16
> § 16.3** nomment le sigle sans l'instruire et y renvoient ; **ils ne reconstruisent ni son statut, ni
> son inventaire**. C'est l'économie de la fusion sur cette matière, et l'abstention est contrôlée par
> [`PRD/check-sieges.py`](../PRD/check-sieges.py).

**Le statut du terme, posé avant tout usage.** *La connaissance de l'agent **n'est pas un standard
établi** ; les initiatives existantes relèvent du **positionnement fournisseur*** (Vol. I
*Monographie* §5.5.4). ⚠ Et **aucun forum n'avait tranché à juin 2026** quelle instance porterait le
standard — ni l'alliance industrielle, ni le consortium du Web, ni l'organisme international de
normalisation (Vol. III H-19, **[C]**).

⚠ **Deux précisions que la somme doit à sa propre vérification, et elles ne sont pas de forme.**
*Premièrement* : la formule commode « **terme de marché avant d'être terme de norme** » **ne figure
pas au Vol. I** — l'expression y est introuvable —, c'est une **construction d'auteur du Vol. III**.
*Deuxièmement* : H-19 est une entrée de **repérage**, et **une entrée [C] ne porte jamais un fait
central**. L'énoncé « aucun forum n'avait tranché » entre donc ici comme **thèse d'un volume antérieur,
attribuée et datée de son gel**, non comme fait vérifié par la somme. *Ce que le Vol. III a lui-même
relevé au 21 juillet 2026 fait l'objet du § 18.1, et il ne dit pas la même chose.*

Lecture de l'auteur — **la thèse de ce chapitre est une construction d'auteur, et c'est le rapport
d'instruction lui-même qui l'impose** : *aucune des sources consultées n'énonce sous cette forme ce
qui manquerait au dispositif agentique.* **Ce que le socle établit** : l'état, la date et le statut de
**neuf chantiers pré-normatifs** (§ 18.1) ; ce que deux protocoles **remettent à la partie qui admet**
(§ 18.2) ; **trois précédents institutionnels** (§ 18.3). **Ce qu'il n'établit pas** : que la logique
de la connaissance du client soit **transposable** à l'agent ; qu'un dispositif institutionnel soit
**nécessaire** à cette transposition ; qu'aucune organisation n'en ait constitué un **hors des pages
ouvertes**. *Le rapprochement entre ces trois précédents et le vide agentique est une lecture, non un
constat de source.*

⚠ **Ce que ce chapitre ne traite pas.** Le versant **adoption** du fossé entre stade et production est
au **ch. 13 § 13.5**, avec lequel le §7.4.3 du Vol. I est **partagé déclaré** ; le présent chapitre en
prend le versant ***trust fabric***. La **valeur probante** des mécanismes qu'un tiers présente est au
**ch. 15**. La **révocation après admission** est au **ch. 20**. Et l'**assemblage** que l'admission
supposerait est au **ch. 16**.

## § 18.1 — État des propositions KYA

Le Vol. I décrivait, à son gel de juin 2026, des formes « encore concurrentes » et un **verrou
institutionnel** (H-19, **[C]**). *L'instruction du 21 juillet 2026 ne renverse pas ce constat : elle
en change l'échelle.* La situation ne s'est pas décantée, **elle s'est densifiée** — et la densité,
ici, *n'est pas un progrès vers la norme, c'est une multiplication des candidats*.

| Instance | Objet | État relevé au 21 juillet 2026 | Entrée |
|---|---|---|---|
| **Consortium du Web** | Groupe communautaire « Agent Identity Registry Protocol » — *ni voie des normes, ni Recommandation* | proposé le **22 avril 2026** ; livrables annoncés : une méthode d'identifiant décentralisé et un format d'accréditation d'agent ; **36 participants non-présidents** affichés ; **ni rapport ni brouillon publié** | F-30 **[B]** ; F-50 **[B, degré 2]** |
| **Consortium du Web** | Groupe communautaire « AI Agent Protocol » — *même statut* | hébergé depuis le **8 mai 2025** ; charte déclarant un modèle d'identité pour les agents d'IA ; **254 participants non-présidents** affichés ; **aucun document produit n'a été ouvert** | F-83 **[B]** |
| **Fondation d'identité ouverte** | Groupe communautaire « Artificial Intelligence Identity Management » | sa charte place **hors de son périmètre** le développement de protocoles de normalisation mondiaux liés à l'identité des agents, **et renvoie ce travail à un groupe de travail** | **F-48 [A, degré 2]** |
| **Fondation d'identité décentralisée** | Spécification communautaire de connaissance de l'agent | **non ratifiée au 22 juin 2026** : version 1 encore soumise à la relecture du groupe de travail et à l'approbation du comité de pilotage | F-50 **[B, degré 2]** |
| **IETF** | Brouillon d'identité d'agent (soumission individuelle) | déposé le **26 mars 2026**, expirant le **27 septembre 2026** ; **non adopté** par un groupe de travail | F-50 |
| **IETF** | Brouillon de registre d'identité d'agent (soumission individuelle) | déposé le **23 mai 2026**, expirant le **24 novembre 2026** ; **non adopté** par un groupe de travail | F-50 |
| **Institut national de normalisation — centre d'excellence** | Document de concept sur l'identité et l'autorisation des agents logiciels et d'IA | publié le **5 février 2026**, à l'état de **projet public initial** | F-73 **[B]** |
| **Institut national de normalisation — centre d'innovation** | Initiative de normalisation des agents d'IA | annoncée le **17 février 2026** ; troisième axe portant sur la sécurité et l'identité ; **volet identité à l'état de projet de document de concept** | F-56 **[B]** |
| **Fournisseur de sécurité applicative** | Cadre commercial « Know Your Agent » | **annoncé le 15 juin 2026** au sein d'un cadre de sécurité agentique | F-49 **[B, degré 3]** |

: Tableau 18.1 — Neuf chantiers, six organisations, zéro texte ratifié, au 21 juillet 2026.

⚠ **Tri prospectif des trois énoncés futurs du tableau.** Les deux **dates d'expiration** des
*Internet-Drafts* sont **PROGRAMMÉES au sens strict** : elles découlent mécaniquement de la règle des
six mois et sont affichées par le registre ; **elles n'annoncent aucun résultat de normalisation**. La
**ratification** de la version 1 de la spécification communautaire est **PROJETÉE** : prévision
attribuée à son organisme, millésimée du 22 juin 2026, **sans date annoncée** et **non revérifiée**
entre cette date et le relevé — degré 3 pour cet intervalle.

**Neuf lignes, six organisations, et aucune ligne ne porte un texte ratifié ni adopté.** ⚠ **La borne
de cet énoncé est celle de l'entrée qui le porte** : F-50 couvre la spécification non ratifiée au
22 juin 2026, les **deux** *Internet-Drafts* consultés, et le groupe communautaire correspondant sans
rapport ni brouillon publié — c'est un **fait négatif ÉTABLI**, degré 2, *porté par la réserve
explicite des sources elles-mêmes, non par un balayage exhaustif du champ*. **Il ne dit rien d'un texte
qui existerait hors de ces pages.**

**Quatre observations se dégagent, et la dernière est un refus.**

**Le statut d'un groupe communautaire se répète à chaque mention, il ne se pose pas une fois pour
toutes.** *Un groupe communautaire n'est pas un groupe de travail* : ses travaux ne sont **ni sur la
voie des normes ni au rang de norme**, il **ne produit pas de Recommandation** et **n'engage aucun
calendrier normatif** (F-83). Les deux groupes du tableau sont donc, ensemble, **un indicateur
d'activité et non un jalon de normalisation** : le premier annonce des livrables **sans en avoir
publié**, le second déclare un objet d'identité dans sa charte **sans qu'aucune de ses productions ait
été ouverte**. ⚠ Le décompte de **254 participants** est **affiché par la plateforme** : il compte des
**inscriptions individuelles**, non des organisations contributrices ni une activité rédactionnelle, et
il est **attribué à cette page à chaque occurrence**.

**L'instance qui a compilé le livre blanc de référence décline la normalisation, et elle le fait par
écrit.** C'est **la seule entrée du lot à porter le niveau [A]** : la charte place **hors de son
périmètre** le développement de protocoles de normalisation **mondiaux** liés à l'identité des agents,
**et renvoie ce travail à un groupe de travail** de l'organisme ou d'une organisation en liaison
(F-48, **[A, degré 2]**). ⚠ **Les deux moitiés de l'énoncé comptent également** : la première établit
que cette instance **ne conduit pas elle-même** ce travail ; la seconde **interdit d'en conclure à un
renoncement** — *le socle décrit un aiguillage, pas un abandon.* ⚠ Le livre blanc lui-même **n'est pas
au socle** du Vol. III : *source primaire ouverte et citée hors socle*, et son versement est remonté.

**Le nom lui-même n'est pas stable.** Au 21 juillet 2026, « Know Your Agent » désigne **au moins deux
objets distincts, documentés chacun par son propre éditeur** : une spécification communautaire, et un
cadre commercial annoncé le 15 juin 2026 (F-49, **[B, degré 3]**). ⚠ **L'énoncé dit « au moins deux »
et ne porte aucune clause d'exclusivité.** ⚠ Le communiqué du second **ne qualifie pas le statut de
disponibilité** du cadre : ni disponibilité générale, ni préversion, ni feuille de route datée n'y
figurent, et le cadre **n'est rattaché à aucune spécification publiée** — *annonce et disponibilité
générale documentée sont deux choses différentes.* ⚠ **Aucun lien de dépendance, de compatibilité ou
de filiation entre les deux objets n'a été recherché** : absence de documentation, degré 3. Une
**troisième occurrence** du même nom, datée du 4 février 2026, est signalée par une source secondaire
dont l'instruction **n'a pas pu localiser le document primaire** ; elle est consignée comme **échec de
source** et **ne porte aucun énoncé**.

**Et le refus : une jonction que le socle ne fait pas, et que le chapitre ne fera donc pas.** Deux
entrées datent, à douze jours d'écart, deux pièces d'un même organisme national de normalisation — une
initiative annoncée le 17 février 2026 dont le volet identité est à l'état de projet de document de
concept (F-56), et un document de concept publié le 5 février 2026 à l'état de projet public initial
(F-73). ⚠ **Le socle ne documente pas si ces deux pièces désignent le même document — absence de
documentation, non fait négatif vérifié.** *Les deux lignes sont donc portées séparément, et le lecteur
qui a besoin de la réponse doit l'établir lui-même.*

⚠ **La question de l'instance porteuse reste ouverte, et deux constats de rapport la bornent sans être
versés.** Aucune des pages consultées **ne désigne un forum unique** ; et la page du groupe
communautaire de registre y **annonce une coordination avec quatre autres instances**. *Ces deux
constats ne sont versés à aucune entrée et ne portent aucune affirmation centrale ; leur versement est
remonté.* ⚠ **Le relevé n'établit pas non plus qu'aucune désignation ne soit intervenue hors des
sources ouvertes** — degré 3.

## § 18.2 — Admettre un agent tiers : ce que les protocoles remettent à celui qui décide

*Admettre est un acte, et un acte a un contenu vérifiable ou n'en a pas.* La question de cette section
est donc étroite : **quand un agent se présente à la frontière d'une organisation qui ne l'a pas émis,
que celle-ci reçoit-elle, et que doit-elle produire elle-même ?**

⚠ **La grille du ch. 14 n'est pas appliquée ici** : le chapitre appartient au mouvement qui *instruit*
Q-C plutôt que de porter un verdict mécanisme par mécanisme (ch. 17 § 17.0).

**La découverte est spécifiée ; l'admission ne l'est pas.** Le protocole agent-agent normalise la
découverte d'un agent — chemin conventionnel, trois stratégies documentées — et **déclare
explicitement qu'aucune interface de registre n'est prescrite** (F-43, **[B, degré 2]**). ⚠ **L'écart
est structurant** : *trouver un agent et décider de l'admettre sont deux opérations distinctes, et la
spécification outille la première en renvoyant la seconde à celui qui la prend.* Le service d'annuaire
de l'autre écosystème est, lui, spécifié par un *Internet-Draft* de **soumission individuelle**, à sa
révision -02 du 6 juillet 2026 (F-43) — **statut pré-normatif, non une norme ratifiée**.

**La vérification de signature est facultative des deux côtés.** Les cartes d'agent **MAY** être
signées ; les clients **SHOULD** vérifier au moins une signature avant d'accorder confiance (F-04,
**[A]**). ⚠ **La conséquence est à écrire sans atténuation, parce qu'elle décide de ce qu'une
organisation peut inscrire dans un dossier de diligence raisonnable : une chaîne entièrement conforme
peut ne comporter aucune signature apposée ni aucune vérification effectuée.** *L'admission d'un agent
tiers ne dispose donc, **du côté de ce protocole et de lui seul**, d'aucun plancher normatif — elle en
dispose d'un du côté de la politique interne de l'organisation qui admet, et c'est elle qui devra
l'écrire.*

**L'ancrage, qui est le cœur du problème inter-domaines, est renvoyé hors du protocole.** La
récupération de la clé passe par deux paramètres, ou depuis un magasin de clés de confiance que les
clients **MAY** maintenir — **facultatif et non spécifié** (F-09, **[B]**). *Une partie de confiance
qui reçoit l'agent d'un tiers doit donc **constituer elle-même** le lien entre une signature et une
autorité qu'elle tient pour légitime : c'est très exactement la fonction qu'une infrastructure de
fédération assume ailleurs* (§ 18.3).

**Et ce que la vérification peut établir est lui-même borné.** La section balayée ne mentionne **ni
liste de révocation, ni répondeur de statut, ni chaîne de certificats, ni délai de re-validation**, et
sa procédure en six étapes **ne comporte aucune étape de contrôle de statut ou de fraîcheur** (F-06,
**[A]**, fait négatif **VÉRIFIÉ**, degré 1, borné à cette seule section). ⚠ **La borne n'est pas
décorative** : une section normative que le lot **n'a pas pu ouvrir** pourrait porter des exigences de
fraîcheur — **absence de documentation, degré 3**. Le même texte pose pourtant, au niveau normatif le
plus fort, que les clés expirées ou révoquées **MUST NOT** servir à la vérification, **sans mécanisme**
permettant au client de l'établir (F-07, **[A]**). ⚠ *Ce que ce mécanisme démontre est la vérification
d'une signature ; il ne documente pas le moyen d'en établir la **validité courante*** (R-02). L'objet
propre de cette asymétrie est le **ch. 20 § 20.4**.

**La validité, quand elle est définie, l'est à l'intérieur d'un domaine.** Un justificatif d'identité
de charge de travail est **considéré valide s'il a été signé par une autorité du domaine de confiance
de l'identité qu'il porte** (F-87, **[B]**). ⚠ **L'énoncé est intra-domaine par construction** : *il ne
dit rien de ce qu'une autorité d'un autre domaine devrait faire pour l'accepter.* ⚠ Le socle de cette
famille d'identité est **posé au ch. 3** et n'est pas reconstruit ici. Du côté de l'IETF, une section
d'architecture — **brouillon en cours, non prescription protocolaire** — range les intermédiaires
d'IA parmi les charges de travail déléguées (F-86, **[B]** ; établi au ch. 12 § 12.1).

**Le registre, lui, décrit ce qu'il faudrait inscrire, non ce qu'il faudrait vérifier.** La
spécification de registre — **brouillon de laboratoire** (F-38, **[A]**) — range parmi les champs
obligatoires de son profil d'agent la liste des outils invocables et les bornes de portée (F-40,
**[B]**). ⚠ *Ce sont des déclarations de champs, non des propriétés démontrées* (R-02). L'instruction
complète est au **ch. 15 § 15.3.1**.

**Un dernier constat, interne cette fois, mesure la difficulté à sa juste échelle.** La documentation
d'un éditeur porte une **réserve explicite d'absence de couverture entre les deux plans d'identité
d'agent** de son propre produit (F-35, **[A]**, degré 2). ⚠ **C'est un écart de point d'application à
l'intérieur d'une seule location.** *Si la couverture n'est pas assurée dans un locataire unique, la
question de savoir ce qu'un tiers peut en inférer de l'extérieur ne se pose même pas dans les mêmes
termes.*

Lecture de l'auteur — **ce que le socle établit** : la découverte est spécifiée et le registre décliné
(F-43) ; signature et vérification sont facultative et recommandée (F-04) ; l'ancrage est renvoyé hors
protocole (F-09) ; le statut d'une clé n'est pas établissable par les moyens décrits dans la **seule
section balayée** (F-06, F-07) ; la validité d'un justificatif est définie **relativement à un
domaine** (F-87) ; deux plans d'identité coexistent sans recouvrement dans un produit donné (F-35).
**Ce qu'il n'établit pas** : que ces constats **se composent** en une difficulté d'admission
inter-domaines — *aucune entrée du socle ne raisonne sur la composition.* **La lecture proposée** —
*l'admission d'un agent tiers est intégralement à la charge de celui qui admet, et les mécanismes de
2026 lui fournissent des pièces sans lui fournir de procédure* — **est une construction d'auteur, et
elle se refuse sans qu'aucun des faits cités ne tombe.**

## § 18.3 — Fédérations de confiance : ce que trois précédents portent d'institutionnel

Lecture de l'auteur — **le KYC ne repose pas sur une technique ; il repose sur des institutions qui
rendent la technique opposable.** **Trois précédents documentés** permettent de nommer ces institutions
sans les inventer — et ⚠ **deux des trois ne sont pas des textes réglementaires**, *ce qui interdit de
réduire la question à une affaire de législateur.*

**Le précédent réglementaire.** Un règlement européen institue deux dispositifs à l'appui de la
confiance transfrontalière : un **audit des prestataires de services de confiance qualifiés au moins
tous les vingt-quatre mois, à leurs frais, par un organisme d'évaluation de la conformité** ; et
**l'établissement, la tenue et la publication par chaque État membre de listes de confiance** des
prestataires qualifiés (F-51, **[B]**). ⚠ **Trois bornes, et elles décident de ce que ce paragraphe
autorise.** Le texte cité est celui du **règlement de base**, et **les modifications apportées par sa
révision n'ont pas été vérifiées sur ces deux articles précis** — degré 3. Le règlement **ne vise pas
les agents logiciels** : *toute transposition au domaine agentique est une lecture d'auteur, non un
constat du texte.* Et les deux articles décrivent **une procédure institutionnelle** — un audit
périodique, une liste publiée — **non une propriété de sécurité démontrée** (R-02).

**Le précédent industriel.** Une alliance industrielle documente deux dispositifs qu'elle exploite
elle-même : un **programme de certification confié à des laboratoires accrédités**, assorti de niveaux
de sécurité, et un **service de métadonnées** dont les parties de confiance téléchargent un fichier
signé contenant les données de registre des modèles certifiés (F-51, **[B]**). ⚠ **Ces niveaux de
certification d'authentificateur ne se confondent avec aucune des trois échelles d'autonomie du
Vol. I**, et notamment pas avec la graduation à quatre niveaux préfixés d'une lettre, *qui mesure tout
autre chose* — l'homonymie est déclarée au **ch. 14 § 14.4**. ⚠ Le mécanisme est ici encore **qualifié
par ce que l'alliance documente comme procédure**, non par une propriété démontrée : *les pages
consultées ne présentent aucune démonstration cryptographique.* ⚠ **La procédure de retrait ou de
révocation d'une entrée du service de métadonnées n'apparaît pas** dans les deux pages relevées :
**absence de documentation, degré 3**. ⚠ Ces pages **ne portent ni version ni date de publication
affichées** — *ressource vivante, à rejouer avant toute reprise.*

**Un troisième précédent, hors du champ agentique et hors du champ réglementaire.** Le cadre de
gouvernance d'un écosystème d'identifiants d'entités juridiques, dans sa version du **25 mars 2026**,
s'adosse à un socle technique nommé et se déclare conforme aux recommandations d'une fondation de
confiance (F-32, **[B]**). ⚠ Il est retenu **comme matière de comparaison** : *il montre qu'une
infrastructure de confiance vérifiable peut se doter d'un cadre de gouvernance publié sans attendre un
texte législatif.* **Le socle n'établit aucun lien entre ce cadre et l'identité des agents**, et le
chapitre n'en tire donc **aucune transposition**. *Son versant adoption est au ch. 13 § 13.5.*

**Ce que ces pièces ont en commun ne va pas jusqu'au triplet.** *Seule la première le porte en
entier* — une autorité désignée qui évalue, un rythme d'évaluation inscrit, une liste consultable ; la
deuxième documente **l'autorité et la liste sans le rythme** ; la troisième, **la seule publication
d'un cadre**.

| Précédent | Autorité qui évalue | Rythme inscrit | Liste publiée | Nature du texte |
|---|---|---|---|---|
| **Réglementaire** | organisme d'évaluation de la conformité | **oui** — au moins tous les vingt-quatre mois | **oui** — listes de confiance par État membre | règlement ; **ne vise pas les agents logiciels** |
| **Industriel** | laboratoires accrédités par l'alliance | *non relevé* | **oui** — service de métadonnées signé | programme d'alliance ; **procédure, non propriété démontrée** |
| **Hors champ agentique** | *non relevé* | *non relevé* | *non relevé* | **cadre de gouvernance publié et versionné** |

: Tableau 18.2 — Trois précédents de fédération et ce que chacun porte d'institutionnel, au 21 juillet 2026.

Lecture de l'auteur — **ce que le socle établit** : les deux dispositifs du précédent réglementaire,
les deux du précédent industriel, le cadre de gouvernance publié du troisième ; et, du côté agentique,
qu'**aucune des propositions consultées n'est ratifiée ni adoptée** (F-50) et que l'instance qui a
compilé le livre blanc **renvoie la normalisation à un groupe de travail plutôt que de la conduire**
(F-48). **Ce qu'il n'établit pas** : qu'un organisme d'évaluation, un rythme d'audit inscrit ou une
liste de confiance publiée **fassent défaut** au domaine agentique **au-delà des pages ouvertes**.
⚠ *Aucune source consultée n'énonce ce manque sous cette forme ; le constat est **borné aux pages
effectivement ouvertes, et de degré 3 au-delà*** — **écrire que ces dispositifs n'existent pas serait
la faute que R-14 proscrit.** *La lecture proposée est celle-ci : la connaissance de l'agent n'est pas
d'abord bloquée par un problème cryptographique, elle est bloquée par **l'absence d'une instance qui
réponde de la vérification** — et c'est le sens qu'il faut donner au **verrou institutionnel plus que
technique** que le Vol. I nommait à son gel* (H-19, **[C]**, thèse attribuée).

⚠ **Trois pièces qui commandent cette question n'ont pas été instruites, et la lacune est déclarée** :
la **révision** du règlement européen et le portefeuille d'identité numérique qu'elle porte, **non
ouverts**, alors qu'ils postdatent le texte cité ; l'**organisme international de normalisation**, sur
lequel **aucune recherche n'a été menée**, alors que le Vol. I le nomme parmi les forums n'ayant pas
tranché ; et les composantes d'identité de l'un des écosystèmes, **non instruites par ce lot**. *La
question reste ouverte ; aucune inférence n'est proposée.*

**Une conséquence pratique se dégage, et elle est le motif pour lequel ce chapitre existe.** Une
institution qui veut admettre l'agent d'un partenaire **aujourd'hui** ne peut pas déléguer sa décision
à un cadre externe : **aucune des propositions consultées n'est ratifiée ni adoptée** (F-50, degré 2,
borné à ses trois composantes). *Elle doit donc **écrire son propre régime d'admission** — quelles
autorités d'émission elle reconnaît, à quelle fréquence elle les réévalue, et ce qu'elle fait
lorsqu'une signature ne peut pas être rattachée à un ancrage qu'elle contrôle* (F-09). ⚠ **Ce régime
est une construction privée** ; il n'est opposable qu'à ceux qui y consentent **par contrat** ; et
**il ne compose pas avec celui du partenaire suivant**.

*C'est en ce sens, et en ce sens seulement, que « l'entreprise agentique » — terme de fournisseur avant
d'être terme de norme, dont la définition d'auteur a son siège unique à l'avant-propos de la somme —
s'arrête à ses murs : non parce qu'une frontière technique l'y contraint, mais parce qu'aucune des
instances relevées au § 18.1 n'a pris en charge, à la date de gel, ce qu'elle aimerait cesser de
vérifier elle-même.* ⚠ **Cette borne n'est pas une précaution de style** : le socle **ne documente ni
l'existence ni l'absence** d'un tel dispositif hors des pages ouvertes — **degré 3**.

## § 18.4 — Relève à instruire : l'agent mutable prive la réputation de son ancrage

⚠ **Cette section porte une relève du plan, et non un fait.** Une **préimpression révisée en mai
2026** soutient que les architectures d'agents à **poids, invites et mémoire mutables** n'offrent pas
la **persistance d'identité** que tout mécanisme de réputation présuppose : *l'objet vérifié à
l'admission peut cesser d'être l'objet admis.*

⚠ **Régime, et il est le plus bas de tout le Livre.** **Préimpression non révisée par les pairs,
résumé seul consulté** : c'est un **repérage [C]**, **jamais un fait**. *Le texte intégral n'a pas été
ouvert ; rien de ce que sa construction démontrerait, de son modèle de menace ou de ses hypothèses
n'est établi ici* — **absence de documentation, degré 3**. ⚠ **Et le régime de preuve du Livre II
l'interdit doublement** : le PRD range les relèves parmi les **repérages qui n'entrent au socle
consolidé qu'après extraction de la source primaire en G-1**, et **cette extraction n'a pas eu lieu**.

**Ce qui peut néanmoins s'écrire, c'est la portée que la thèse aurait si elle tenait**, et c'est le
seul contenu que cette section porte.

Lecture de l'auteur — **si la thèse tient, elle pèse sur trois endroits de la somme, et pas seulement
sur l'admission.** *(1)* Sur la **cinquième question de la grille** (ch. 14) : une imputabilité
traçable suppose que l'entité à laquelle on impute **soit restée la même**. *(2)* Sur la
**révocation** (ch. 20) : on ne révoque pas utilement l'identifiant d'un objet dont la substance a
changé sans que l'identifiant bouge — *c'est le versant « identité » de ce que le ch. 20 § 20.1
instruit sous l'angle du retournement d'un serveur d'outils.* *(3)* Sur l'**admission** elle-même
(§ 18.2) : *un régime d'admission privé, écrit par celui qui admet, vérifie un objet à un instant ; si
cet objet est mutable, le verdict ne dit rien de l'instant suivant.* ⚠ **Ce que le socle établit** :
rien de la thèse. **Ce qu'il n'établit pas** : tout le reste — *y compris qu'elle soit fausse.*

⚠ **La relève est portée ici et n'est consommée nulle part.** Son instruction relève de **G-1**, volet
résiduel, et son critère de clôture est celui que le PRD impose aux préimpressions : **extraction du
texte intégral**, et **niveau plafonné tant qu'aucune révision par les pairs n'est constatée**. *Aucun
énoncé du présent chapitre ne s'y adosse.*

### Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Le siège unique du KYA**, avec son statut de terme, ses neuf chantiers et son fait négatif établi
   de degré 2. Les **ch. 13, 15 et 16** y renvoient ; **aucun ne le reconstruit**.
2. **Le partage entre spécifié et remis.** *La découverte est spécifiée ; l'admission ne l'est pas.*
   Le **ch. 20 § 20.2** le prolonge dans le temps — *la vérification à l'admission ne protège pas
   contre la dérive après admission.*
3. **Les trois précédents institutionnels et leur triplet incomplet** — autorité, rythme, liste. Le
   **ch. 16 § 16.3** les nomme comme dispositifs de reconnaissance mutuelle ; **ils sont instruits
   ici**.
4. **La conclusion qui décide de la portée du Livre.** *Une institution qui admet aujourd'hui écrit son
   propre régime, opposable par contrat seulement, et qui ne compose pas avec celui du partenaire
   suivant.* C'est ce que le **ch. 21 § 21.5** retrouvera sous l'angle cryptographique, et ce que le
   **ch. 37** rencontrera au point d'application.

---

## § 18.5 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui est enfreint.** Portes **G-3** et **G-4** ; volet résiduel de **G-1** non instruit ; ordre de
rédaction du PRD §6. Instruction d'auteur du 27 juillet 2026.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ **Et le § 18.4 est d'un régime encore plus
   bas** : préimpression, résumé seul consulté, **repérage [C]** — *il ne porte aucun énoncé du tout,
   et la pièce l'écrit.*
2. **Les décomptes sont publiables** (G-2). Écart de **+10,6 %** ; la volumétrie du Livre alimente
   **D-4** par **R-IV-17**.
3. **Les renvois « ch. N » vers les Livres III à V sont des renvois de plan** : **ch. 37**. Les renvois
   vers le **ch. 3** résolvent contre du texte ; ceux vers les **ch. 12, 13, 14, 15, 16, 17, 20, 21**
   résolvent contre du texte au terme de la présente passe.
4. **Un siège neuf est posé par cette pièce** — le KYA (§ 18.0) — et **il n'est contrôlé par aucun
   outil au moment où elle est écrite** : voir **R-IV-24**, ouverte au ch. 15, dont le versement est
   opéré à la clôture de la passe.

**Remontées ouvertes par ce chapitre :**

- **R-IV-30 — non bloquante, de couverture de source, et elle vise le siège lui-même.** Le siège du
  KYA est **partagé entre deux volumes** : le Vol. I *Monographie* §5.5.4 est déclaré « **SIÈGE unique
  du KYA** » au plan, et le Vol. III ch. 11 en porte l'instruction datée. ⚠ **Les deux ne disent pas la
  même chose, et l'écart est daté** : le Vol. I pose le statut du terme et le verrou institutionnel à
  son gel de **juin 2026** ; le Vol. III relève **neuf chantiers et six organisations** au **21 juillet
  2026** et conclut que *la situation ne s'est pas décantée, elle s'est densifiée*. ⚠ **Ce n'est pas
  une contradiction** — c'est un **état daté qui a évolué** —, mais *un siège dont la matière est
  portée par un volume et l'instruction par un autre est un siège dont la forme n'est pas décidable*.
  **Demande remontée** : que le plan **désigne explicitement** lequel des deux textes le siège du § 18.1
  reprend, et à quel régime — le Vol. I étant en **[C]** et le Vol. III sous **G-4 ouverte**.
- **R-IV-31 — non bloquante, de cardinal.** Le titre du chapitre source annonce « **neuf chantiers, six
  organisations, zéro texte ratifié** », et le tableau 18.1 les porte. ⚠ **Le cardinal « neuf » est
  fragile de deux façons** : *(a)* deux des neuf lignes reposent sur des *Internet-Drafts* dont les
  dates d'expiration — **27 septembre 2026** et **24 novembre 2026** — sont **postérieures au gel mais
  antérieures à toute publication vraisemblable de la somme** ; *(b)* une ligne — le cadre commercial —
  est une **annonce sans statut de disponibilité**, et le socle déclare **au moins deux objets** sous ce
  nom, sans clause d'exclusivité. **Demande remontée** : que le cardinal soit **re-mesuré au gel de
  publication** plutôt que repris, et que le titre porte sa date. ⚠ *Un cardinal annoncé en toutes
  lettres ne se met pas à jour tout seul — c'est le premier risque du plan.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.24** — § 18.1 à § 18.4,
dans l'ordre exact —, et le § 18.0 est une introduction de chapitre. La **table de couverture est
respectée pour ses quatre lignes**, y compris le **partage déclaré du §7.4.3 du Vol. I avec le ch. 13**
: le versant **adoption** reste au ch. 13 § 13.5, le versant ***trust fabric*** est ici, et **ni l'un
ni l'autre ne reconstruit la moitié de l'autre**. Le **siège unique du KYA est posé et marqué**
(§ 18.0). Le **socle IAM et l'identité de charge de travail restent au ch. 3**. L'**inventaire de la
révocation reste au ch. 20 § 20.4** ; la **valeur probante reste au ch. 15** ; l'**assemblage reste au
ch. 16**. **Aucun verdict de grille n'est rendu.** Les **dix occurrences de R-14** portent leur degré,
dont **huit au degré 3**. Les **onze occurrences de R-09** répètent la clause du groupe communautaire
**à chaque mention** plutôt que de la poser une fois en tête. Le **décompte de participants est
attribué à la page qui l'affiche**. Les **niveaux de certification du § 18.3 ne sont confondus avec
aucune échelle d'autonomie**. Et les **six occurrences de « Lecture de l'auteur »** sont suivies de ce
que le socle établit et n'établit pas — dont **le § 18.3 entier**, marqué à l'ouverture.
