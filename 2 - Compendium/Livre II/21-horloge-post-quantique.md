# Chapitre 21 — L'horloge post-quantique : menace sur la pile identitaire, crypto-agilité et dette de migration

*Livre II — Faire confiance : identité, délégation et fabrique de confiance.
Troisième mouvement — l'horloge post-quantique (ch. 21). **Chapitre unique du mouvement, et dernier
chapitre du Livre.** Chapitre à deux mouvements, issu de la fusion v0.20 des anciens ch. 23 et 24.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — portes **G-3** et **G-4** ouvertes ; instruction d'auteur du 27 juillet 2026. ⚠ **Ce chapitre porte le SIÈGE DE L'HORLOGE pour toute la somme** (§ 21.1) : les ch. 15, 16, 20 et, hors du Livre, les ch. 45 et 49 y renvoient et **ne re-datent aucun jalon**. ⚠ **Il porte aussi le garde-fou le plus mécanique du Livre** : *on écrit « **visée** », jamais « fixée », jamais « ~2030 »* — et le **statut du document** se dit à chaque mention. **R-IV-16 et R-IV-17, ouvertes au ch. 12, valent pour tout le Livre** |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit.** Gels de source : **juin 2026** (Vol. I), **21 juillet 2026** (Vol. III). ⚠ **Une entrée héritée est périmée sur un point précis, et le fait se déclare plutôt qu'il ne se lisse** : les cibles que le Vol. I prêtait à un forum sectoriel **ne se retrouvent dans aucun des deux documents de ce forum**, dans les bornes du balayage du Vol. III (§ 21.7) |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (G-3 ouverte). Résolution contre le **Vol. III *Monographie* ch. 16-18**, dont les entrées **F-01** à **F-07**, **F-10**, **F-36**, **F-38**, **F-40**, **F-46**, **F-52** à **F-55**, **F-59** à **F-63**, **F-87** et les entrées héritées **H-03**, **H-17**, **H-27**, **H-33** conservent leurs niveaux d'origine ; et contre le **Vol. I *Monographie* §7.4.1 et §7.4.4**, en **[C]**. ⚠ **Quatre entrées mobilisées sont en [C]** — F-36, F-55, H-17, H-27, H-33 : elles corroborent, elles ne portent pas. ⚠ **H-27 est une thèse d'un volume antérieur, à attribuer à chaque emploi** : l'invariant qu'elle porte **n'est pas un fait**. **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | Vol. III — **R-11 (jalons « visés », jamais « fixés » ; statut du document porté à chaque mention ; les origines ne se fusionnent pas) : ce chapitre en est le SIÈGE — dix-sept occurrences**, § 21.1 (huit), § 21.4 (trois), § 21.7 (deux), § 21.8 et § 21.9 (trois) ; **R-14 : quatorze occurrences**, dont **douze de degré 3** ; **R-02 : neuf occurrences**, § 21.4 (deux), § 21.5 (cinq) et § 21.6 (deux) ; **R-09 : quatre occurrences** ; **R-01 : trois occurrences**, § 21.3 et § 21.5 ; **R-13 : une occurrence**, § 21.4, l'invariant nommé par ses termes. **R-03 à R-08, R-10, R-12 : zéro occurrence.** Vol. II — **§8.2 : deux occurrences**, § 21.7, la projection de coût attribuée à son auteur, à son millésime et à son périmètre ; **PRD Vol. II §8.2.5 : cinq occurrences** ; **R-1 à R-8 : zéro occurrence** |
| **Volumétrie cible** | ≈ **5 800 mots** de corps (§ 21.0 à § 21.9), **cible dérivée** de l'enveloppe du Livre (50 000 mots, TOC v0.24) au prorata des sections — **neuf sections pour deux mouvements**. ☑ **Décompte publiable depuis G-2** ; **réel : 8 342 mots** par [`PRD/decompte.sh`](../PRD/decompte.sh) — **+43,8 %**, **le plus fort écart du Livre**. ⚠ **La volumétrie du Livre entier est relevée au [`README.md`](README.md) du dossier**, et c'est elle — non les écarts individuels — qui alimente **D-4** par **R-IV-17** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.24, entrée du chapitre 21, premier mouvement)* — toute la fabrique d'émission (ch. 12-18) repose sur des signatures classiques ; les jalons du NIST IR 8547 — dépréciation **visée** pour 2030, retrait **visé** pour 2035 — tombent dans la durée de vie des architectures conçues aujourd'hui, la PQC est donc une contrainte de conception et non une annexe.

---

> **Thèse du second mouvement**, citée depuis le TOC v0.24, entrée du chapitre 21 — la crypto-agilité est l'application des trois premiers termes de l'invariant (découplage, contrat, évolution) à la couche cryptographique ; la dette de migration PQC est réelle mais largement non chiffrée — méthode d'estimation plutôt que chiffre.

⚠ **Deux thèses pour un chapitre : le ch. 21 est issu de la fusion v0.20 des anciens ch. 23 et 24**
(décision 11 du TOC), et les deux entrées y sont conservées **intégralement**.

## § 21.0 — Introduction : la seule échéance datée du Livre

Les six chapitres du premier mouvement ont établi ce qu'une organisation peut **émettre**, et les deux
du deuxième ce qui peut **céder**. Aucun des deux n'a rencontré de **date** : les statuts de
normalisation relevés au ch. 13 sont des stades, les propositions du ch. 18 sont **sans jalon**, et les
trois scénarios du ch. 16 § 16.4 sont **tous PROJETÉS ou SPÉCULATIFS**.

**Ce chapitre est le seul du Livre à porter des échéances datées, et c'est ce qui lui donne sa
fonction.** L'entreprise qui met aujourd'hui des agents en production **arrête des mécanismes
d'identité pour une architecture dont elle attend plusieurs années de service** ; et les mécanismes que
le premier mouvement a examinés **reposent, au grain de la cryptographie, sur des signatures numériques
classiques**.

⚠ **Ce chapitre ne traite pas de la cryptographie post-quantique pour elle-même.** Il établit d'abord
**quelle horloge les documents publics fixent — avec, pour chacun, le statut réel du texte qui la
porte** —, puis examine **ce que cette horloge fait à des artefacts d'identité dont le socle documente
précisément la longévité** (§ 21.3), **ce qui rend un changement d'algorithme possible sans rupture du
contrat** (§ 21.4 à § 21.6), et **ce que coûte le passage** (§ 21.7 à § 21.9).

Lecture de l'auteur — **les deux thèses citées sont des constructions d'auteur.** **Ce que le socle
établit** : le statut d'un document et le libellé de ses jalons (F-59, F-60) ; l'existence d'une
obligation fédérale datée qui s'ancre sur ce même document (F-61) ; l'écart de statut entre les
algorithmes normalisés et le calendrier de retrait (F-62) ; l'absence d'échéance calendaire dans un
rapport sectoriel (F-63) ; et le format cryptographique et les bornes temporelles de trois artefacts
d'identité (F-01, F-03, F-05, F-46, F-53). **Ce qu'il n'établit pas** : que ces jalons **s'appliquent à
la pile identitaire agentique**, ni **quelle durée de service** les architectures conçues en 2026
atteindront, ni qu'une échéance soit **atteignable ou manquée**. ⚠ *Le lot d'instruction le déclare
lui-même : **il fournit l'horloge, non son incidence**.*

## § 21.1 — Les échéances exactes et leurs sources

> ⚠ **SIÈGE DE L'HORLOGE POST-QUANTIQUE POUR TOUTE LA SOMME.** Les jalons, leurs sources et leur statut
> sont **posés ici une seule fois**. Les **ch. 15, 16, 20** et, hors du Livre, les **ch. 45 et 49** y
> renvoient ; **ils ne re-datent aucun jalon, et ne fusionnent aucune origine**. *C'est l'économie de la
> fusion côté horloge, et elle n'a lieu que si ces chapitres s'y tiennent.*

**Trois origines documentaires sont examinées pour leurs dates.** ⚠ **Elles ne relèvent ni du même
auteur, ni du même régime, ni du même périmètre, et les fondre en un calendrier unique — ce que la
littérature de vulgarisation fait couramment — produit un énoncé faux dans les trois cas.** *Elles sont
donc tenues sur trois lignes distinctes, et cette section est le siège de cette discipline pour toute
la somme.*

**Première origine : l'institut national de normalisation.** Il **vise** une **dépréciation en 2030**
des mécanismes à clé publique vulnérables au quantique **au niveau de sécurité de 112 bits**, et une
**interdiction en 2035** de ces mêmes mécanismes **tous niveaux de sécurité confondus**. Le projet écrit
littéralement « **Deprecated after 2030** » et « **Disallowed after 2035** » (F-60, **[B]**), dans les
tableaux de deux sections nommées — l'une pour les signatures, l'autre pour l'établissement de clés.
⚠ **Le statut du document n'est pas un détail de procédure** : sa fiche affiche, à la consultation du
21 juillet 2026, **une entrée d'historique unique** de novembre 2024 et **une période de commentaires
publics close en janvier 2025** ; **aucune version finale n'y figure** (F-59, **[B]**, fait négatif
**VÉRIFIÉ** par énumération de l'historique, **borné à cette fiche et à cette date**).

⚠ **Deux précisions décident de la portée de ces deux mots, et l'une comme l'autre s'écrit contre
l'usage courant.** *(1)* Le vocabulaire du projet donne à *deprecated* **un sens qui n'est pas celui
d'une interdiction** : l'algorithme *« may be used, but there is some security risk »*, et **il revient
au propriétaire des données d'examiner ce risque et de décider s'il continue**. *(2)* Le projet
**permet aux normes d'algorithmes de continuer à spécifier des techniques vulnérables jusqu'en 2035**
tout en laissant **des transitions sectorielles plus précoces possibles** (F-60). ⚠ *Un lecteur pressé
lit dans « Disallowed after 2035 » une date d'extinction générale ; **le texte dit l'inverse** — une
borne supérieure à ce que ces normes toléreront, sous laquelle des contraintes sectorielles peuvent
s'installer plus tôt.* ⚠ **La qualification de 2035 en « plafond et non plancher » est portée par le
texte de l'entrée, mais le contrôle de bornage du lot l'a rangée en lecture d'auteur** : elle est
reprise **à ce titre**.

⚠ **Un troisième élément achève de qualifier cette ligne, et il ne figure pas au socle** : le
**véhicule normatif** que le projet désigne pour porter ces échéances est **lui-même à l'état de
projet public initial**, sa période de commentaires étant close depuis décembre 2024. *(Source primaire
ouverte et citée hors socle, non versée.)* ⚠ ***Un projet qui renvoie ses échéances à un second projet
ne devient pas exécutoire par accumulation.***

**Deuxième origine : l'exécutif fédéral américain.** Un décret présidentiel, **signé le 22 juin 2026 et
publié au registre fédéral du 25 juin 2026**, charge le bureau de la gestion et du budget de publier
**sous 90 jours** une directive de migration visant les **actifs de grande valeur** et les systèmes à
impact élevé, **selon le périmètre que le décret définit**, avec échéance au **31 décembre 2030 pour
l'établissement de clés** et au **31 décembre 2031 pour les signatures numériques** (F-61, **[B, degré
1]**). ⚠ **Tri : PROGRAMMÉ** — *engagement daté porté par un texte signé et publié.* Le décret prévoit
en outre la publication d'une **règle proposée** modifiant la réglementation fédérale des acquisitions,
qui viserait les contractants couverts à la même échéance ; ⚠ ***une règle proposée n'est pas une règle
en vigueur**, et le socle n'établit rien de son adoption.*

**La note d'application, du 24 juin 2026, ordonne aux agences d'aligner leur plan de migration sur le
projet « *or successor document* »**, sa note de bas de page renvoyant explicitement à l'adresse du
projet (F-61). ⚠ **C'est le fait qui commande la lecture de cette deuxième ligne : une obligation
fédérale datée s'ancre sur un document qui est encore un projet public initial.** *La clause « ou un
document successeur » est précisément ce qui évite d'en conclure que le projet devient une norme — elle
transfère au futur la désignation du texte qui fera foi.* ⚠ **La note distingue par ailleurs deux
registres qu'il ne faut pas confondre** : **la remise du plan est prescrite au mode obligatoire, sous
120 jours**, tandis que **les cinq phases de son calendrier — dont une phase de migration complète à
horizon 2035 — sont formulées au mode de la recommandation**. *Le tri porte sur l'énoncé prospectif,
non sur le support qui l'imprime* : l'horizon de 2035 est **PROJETÉ**, la remise du plan sous 120 jours
relevant seule du **PROGRAMMÉ**.

⚠ **Périmètre, et il commande la lecture d'un volume canadien.** *Cette obligation vise des agences
fédérales américaines et un ensemble de systèmes que le décret nomme. **Elle ne s'étend d'elle-même ni
aux institutions financières canadiennes, ni à leurs fournisseurs.*** **Le socle ne documente pas
d'instrument canadien équivalent — absence de documentation, non fait négatif vérifié** (degré 3), et
la lacune est déclarée au § 21.8.

**Troisième origine : le secteur financier européen.** Un rapport conjoint de 2026 **ordonne ses
activités de migration par le risque plutôt que par un calendrier daté** : le balayage du texte extrait
de ses 26 pages **ne relève aucune occurrence** des trois chaînes cherchées — les deux millésimes et
l'identifiant du projet de l'institut (F-63, **[B]**, fait négatif **VÉRIFIÉ**, **borné à ces trois
chaînes, à ce fichier et à cette extraction** — ⚠ *ce qui serait rendu en image y échappe*). Un second
document, antérieur, porte au titre le nom d'un forum sectoriel. ⚠ **Le socle ne documente pas de lien
institutionnel entre ce document et le rapport conjoint — degré 3** : *le rattachement des deux textes
est porté par des communiqués que le lot n'a pas pu ouvrir.* ⚠ Ce second document **ne porte pas
davantage d'échéance sectorielle** : ses cinq recommandations sont énoncées **sans date**, et **la seule
échéance datée relevée au balayage est attribuée à l'administration américaine**. *(Source primaire
ouverte et citée hors socle, non versée.)*

| Origine | Ce que le document écrit | Statut réel du document | Périmètre | Tri prospectif |
|---|---|---|---|---|
| Projet de l'institut national (F-59, F-60) | « Deprecated after 2030 » (112 bits) ; « Disallowed after 2035 » (tous niveaux) ; 2035 comme **borne de spécification** — *lecture d'auteur* | **projet public initial** ; **une seule entrée d'historique**, de novembre 2024 ; commentaires clos en janvier 2025 | les normes d'algorithmes de cet institut | **PROJETÉ** — *intention annoncée dans un projet ; tri d'auteur, motivé ci-dessous* |
| Décret et note d'application (F-61) | migration au **31 déc. 2030** (établissement de clés) et au **31 déc. 2031** (signatures) ; alignement des plans sur le projet « **or successor document** » | décret **signé et publié** ; note d'application du 24 juin 2026 | actifs de grande valeur et systèmes fédéraux **américains** à impact élevé ; règle d'acquisition **proposée**, non adoptée | **PROGRAMMÉ** — *engagement daté porté par un texte publié* |
| Rapport sectoriel européen (F-63) et appel à l'action d'un forum (hors socle) — ⚠ **deux documents, lien institutionnel non documenté** | priorisation **par le risque** ; **aucune échéance sectorielle** relevée au balayage ; l'échéance citée dans le second est **attribuée à l'administration américaine** | rapport de praticiens, portant **un avertissement de non-obligation** | secteur financier, **sans force contraignante** | *sans échéance propre à trier* |

: Tableau 21.1 — Trois origines de l'horloge post-quantique, leurs statuts et leurs périmètres, au 21 juillet 2026.

Lecture de l'auteur — **ce que le socle établit** : les jalons figurent **dans un projet** et y sont
formulés **comme une intention** — le texte écrit que l'institut *« intends to »* déprécier (F-60) —,
et **le véhicule normatif censé les porter est lui aussi un projet**. **Ce que le socle n'établit
pas** : **un tri prospectif de ces jalons** — ni F-59 ni F-60 n'en porte. *La lecture proposée est
qu'un engagement institutionnel **annoncé sans être en vigueur** relève du **PROJETÉ**, non du
PROGRAMMÉ.* **Le tri de la deuxième ligne, lui, se déduit du fait** : *un texte signé, publié et
portant des dates est un engagement daté réel.*

**Quatrième constat, et il ferme la section.** ⚠ **Les algorithmes de remplacement, eux, ne sont pas en
projet** : deux normes d'encapsulation de clé et de signature sont **finales, publiées le 13 août
2024** (F-62, **[B]**). ***Les algorithmes sont normalisés ; le calendrier de retrait des algorithmes
classiques ne l'est pas.*** ⚠ **L'asymétrie est le cœur de l'horloge** : *une organisation qui
attendrait « la norme » pour agir attendrait un document dont **rien, dans le corpus consulté, ne date
la finalisation**.* ⚠ **Et un statut final ne vaut pas texte figé** : les fiches des deux normes portent
**l'une et l'autre un avis d'errata** annonçant des corrections dans une révision future — *matière du
§ 21.4.*

⚠ **La lacune du statut réel du projet est ouverte et non close** : **le socle ne documente pas de
calendrier de finalisation — degré 3**, et *il ne s'en déduit rien sur les intentions de l'institut.*

## § 21.2 — *Harvest now, decrypt later* appliqué aux artefacts d'identité longue durée

⚠ **Le socle ne documente pas la collecte anticipée en vue d'un déchiffrement ultérieur — absence de
documentation, non fait négatif vérifié** (degré 3). *Le lot ne l'a pas traitée, et aucune des entrées
mobilisées n'en porte la mécanique ni n'en date la faisabilité.* **La section ne peut donc pas s'écrire
comme un chapitre de fait ; elle s'écrit comme un raisonnement d'architecture appuyé sur des faits qui,
eux, sont établis — et elle dit à quel endroit exact le raisonnement quitte le socle.**

**Ce que le socle établit porte sur la longévité des artefacts, et c'est la variable qui décide.** Trois
faits, tous en **[A]** et tous bornés à la spécification de la carte signée :

- l'**en-tête protégé** énumère trois paramètres obligatoires et un seul facultatif nommé, et **ne
  porte aucun paramètre temporel** — *la signature ne périme que par sa clé* (F-03, degré 1) ;
- la **carte** compte quatorze champs, **dont aucun n'exprime une date d'émission, une expiration, une
  fenêtre de validité ni un indicateur de révocation** (F-05, degré 1) ;
- la **procédure de vérification** ne comporte **aucune étape de contrôle de statut ou de fraîcheur**,
  et la section balayée **ne mentionne aucun dispositif de statut** (F-06) — alors même que
  l'interdiction d'employer une clé expirée ou révoquée est posée **au niveau normatif le plus fort**,
  **sans le moyen de l'établir** (F-07).

**Le contraste avec un artefact voisin est instructif** : les mandats de paiement agentique, eux,
**portent des attributs temporels d'émission et d'échéance** (F-46, **[B]**). ⚠ *Deux artefacts de la
même pile, **deux régimes de péremption** — l'un borné par le temps, l'autre suspendu au statut d'une
clé que la procédure spécifiée ne permet pas d'établir.*

Lecture de l'auteur — **ce que le socle n'établit pas** : *qu'un adversaire collecte aujourd'hui des
artefacts signés, qu'une capacité de cryptanalyse existe ou soit datable, ni qu'un tel artefact
conserve une valeur opérationnelle après la dépréciation de son algorithme.* **La lecture proposée est
la suivante, et elle est réfutable.** *Un artefact d'identité se distingue d'un message chiffré sur un
point : **le risque n'est pas qu'il soit lu plus tard, c'est qu'il soit forgé plus tard**. Un artefact
dont rien ne fixe la fin de validité, et dont le retrait suppose un mécanisme de statut que sa
spécification ne fournit pas, **ne dispose d'aucun moyen documenté d'être sorti de circulation avant
l'horizon de dépréciation de son algorithme**. Le risque de collecte anticipée porte donc, pour cette
classe d'artefacts, **moins sur la confidentialité que sur la non-répudiation rétroactive** : ce qui a
été signé sous un algorithme déprécié **perd, à terme, la capacité d'être opposé**.* ⚠ **Le socle ne
documente ni procédure de re-signature ni horodatage d'appoint pour les mécanismes examinés — degré
3.**

⚠ **Une borne doit être posée sur la date, et elle écarte une fenêtre plutôt qu'elle ne l'invoque.**
Une entrée héritée situe entre 2029 et 2032 la fenêtre d'apparition d'un calculateur quantique
cryptographiquement pertinent, **et le Vol. I trie lui-même cet énoncé SPÉCULATIF** (H-17, **[C]**).
**Une entrée [C] ne porte jamais un fait central** : *cette fenêtre est mentionnée pour être écartée du
raisonnement, non pour l'appuyer.* ⚠ **Ce qui tient sans elle suffit** : les deux jalons publics du
§ 21.1 tombent en 2030-2031 — **PROGRAMMÉ** — et en 2035 — **PROJETÉ** — ; et — Lecture de l'auteur —
*l'horizon de conception d'une pile d'identité d'entreprise n'est vraisemblablement pas plus court.*

## § 21.3 — Inventaire : quels artefacts de la pile agentique cassent, et quand

*Un inventaire de migration se dresse **par artefact, non par produit**.* ⚠ **C'est la colonne de
droite qui dit où une institution ne peut pas encore inscrire de plan.**

| Artefact | Ce que le socle documente de sa cryptographie | Ce qui décide de sa longévité | Ce que le socle ne porte pas — **degré 3**, sauf mention |
|---|---|---|---|
| **Carte d'agent signée** | signature au format JWS ; canonicalisation avant signature ; champ de signatures exclu du contenu signé (F-01, **[A]**) | **aucune borne temporelle** dans l'en-tête protégé (F-03) ; **ni validité ni statut** parmi les quatorze champs (F-05) ; **statut de clé non établissable** (F-06, F-07) | l'ancrage de confiance, la révocation et la gouvernance des clés — **réserve capitale de l'entrée héritée** H-01, **[A]** |
| **Mandats de paiement agentique** | sérialisation SD-JWT, attribut de type **versionné**, version v0.2.0 du 28 avril 2026 (F-46, **[B]**) | attributs temporels d'émission et d'échéance portés par le mandat | **l'agilité du mécanisme de signature sous-jacent** ; le socle ne porte que le format et ses attributs |
| **Certificats et statut** | granularité de la révocation bornée à la période d'émission de la liste ; l'état « good » **ne signifie pas nécessairement** qu'un certificat ait jamais été émis (F-53, **[B]**) | fraîcheur de la liste ou du répondeur ; **un exploitant a arrêté ses répondeurs le 6 août 2025** (F-54, **[B]**) | **toute application de ces textes à un artefact d'identité d'agent** |
| **Entrées de registre gouverné** | brouillon de laboratoire, en-tête du 27 mars 2026 (F-38, **[A]**) ; profil ancré sur SCIM 2.0 (H-03) | quatre états prescrits, ⚠ **sans délai de propagation ni budget de fraîcheur** (F-55, **[C]** : repérage, non fait central) | **tout élément cryptographique du registre lui-même** ; le socle ne porte, pour cet artefact, que des états et un statut de document |
| **Autorisation du protocole agent-outil** | — | la page balayée **ne prescrit aucun mécanisme de révocation** : chaînes absentes, RFC de révocation non citée (F-52, **[B]**, fait négatif **VÉRIFIÉ**, borné à cette page et à cette révision) | ce que **d'autres pages** de la spécification prévoient ; le balayage porte sur **deux pages nommées** |

: Tableau 21.2 — Inventaire de migration par artefact, au 21 juillet 2026.

**Trois enseignements se tirent, et aucun n'exige de date.**

**Le premier porte sur l'agilité.** Dans l'énumération normative de l'en-tête protégé, **un seul
paramètre nomme l'algorithme** (F-03). *Le mécanisme dispose donc d'un point où l'algorithme est
déclaré et peut, à ce titre, changer.* ⚠ **Ce que la spécification démontre est qu'un algorithme est
nommé et que la vérification reconstruit la charge en re-canonicalisant la carte reçue** (F-01,
F-02) ; **elle ne documente ni procédure de transition d'un algorithme à un autre, ni politique
d'acceptation des algorithmes par le vérificateur** (R-02). ⚠ *La capacité de porter plusieurs
signatures est spécifiée pour permettre **la rotation des clés**, mais **aucune procédure de retrait
d'une clé compromise ne l'est*** (F-10, **[B]**) — **la rotation est outillée, le retrait ne l'est
pas.** *L'audit est au § 21.5.*

**Le deuxième porte sur l'ordre des travaux.** ⚠ *Ce qui décide de la difficulté d'une migration n'est
pas la force de l'algorithme employé, **c'est la capacité à sortir de circulation ce qui a été émis
sous l'ancien**.* **Or c'est le point où quatre des cinq lignes du tableau convergent**, chacune dans
sa borne : la carte signée n'a ni expiration ni indicateur de révocation, et le vérificateur n'a pas le
moyen d'établir le statut d'une clé qu'il lui est pourtant interdit d'employer si elle est révoquée ;
le registre prescrit un état de révocation **sans fixer de délai de propagation** ; l'autorisation du
protocole agent-outil **ne prescrit, sur la page balayée, aucun mécanisme de révocation** ; et le
précédent des certificats converge par sa borne propre. ⚠ **La cinquième fait exception** : les mandats
portent des attributs temporels — *une péremption par le temps, qui n'est pas une révocation mais qui
borne la circulation.* ⚠ **Et le précédent ne console pas** : *là même où la révocation est spécifiée,
sa granularité est bornée à la période d'émission de la liste.* **L'inventaire complet est au ch. 20
§ 20.4** ; il n'est pas refait ici.

Lecture de l'auteur — **ce qu'il n'établit pas** : que ces manques soient **liés entre eux**, qu'ils
tiennent à une **cause commune**, ni qu'ils **empêchent** une migration. *La lecture proposée est
qu'**une migration cryptographique est d'abord une opération de retrait**, et qu'elle ordonne donc les
travaux d'une institution — **instrumenter le retrait avant de choisir l'algorithme de remplacement**.
Elle est réfutable : un mécanisme de retrait spécifié ailleurs, dans un corpus non balayé, la ferait
tomber.*

**Le troisième porte sur l'objet composite.** ⚠ **Le passeport d'agent ne figure dans aucune
spécification de 2026 : c'est un objet de synthèse construit par la somme** (ch. 16). Lecture de
l'auteur — **ce qu'il n'établit pas** : que ces pièces composent un objet unique, ni **qu'une propriété
de migration se transporte d'une pièce à l'assemblage** — *aucune entrée mobilisée ici ne porte sur des
assemblages.* *La lecture proposée est que **la migration de cet assemblage ne vaudra pas mieux que
celle de sa pièce la moins agile**, le tableau montrant que ces pièces n'ont ni le même format, ni le
même régime de péremption, ni le même degré de documentation.*

⚠ **Reste le « quand », que le titre annonce et que le socle ne fournit pas au grain de l'artefact.**
**Le socle ne documente pas l'incidence des jalons post-quantiques sur les artefacts d'identité
agentique — degré 3** ; *le lot le déclare en clôture, et le chapitre ne comble pas ce trou par une
chronologie inventée.* **Ce qui peut s'écrire sans le combler tient en une phrase** : *un artefact que
rien ne borne dans le temps **traverse par construction les deux jalons du § 21.1** — de sorte que la
variable qu'une institution contrôle **n'est pas la date, mais la durée de vie qu'elle consent à ses
propres artefacts**.*

## § 21.4 — Définition opérationnelle et état des recommandations

⚠ **La réponse ne se lit pas dans le socle, et il faut l'écrire avant tout le reste.** **Le socle ne
documente ni définition de la crypto-agilité, ni recommandation portant sur elle — absence de
documentation, non fait négatif vérifié** (degré 3). *Le programme d'instruction nommait pourtant les
« recommandations de crypto-agilité » parmi les objets du lot ; **la clôture du lot énumère six points
couverts, et la crypto-agilité n'est aucun des six**.* **La lacune est déclarée et non comblée.**

**Ce chapitre fait donc trois choses qu'il ne mélange pas** : il **construit** une définition
opérationnelle, marquée comme construction d'auteur ; il **audite** contre elle les mécanismes
d'émission et le mandat, en ne retenant de chacun que **ce que sa spécification démontre** (§ 21.5) ;
et il **propose** des patrons de migration, **constructions d'auteur en totalité** (§ 21.6).

Lecture de l'auteur — **ce que le socle établit** : que l'algorithme de signature est **un paramètre
nommé** dans au moins un mécanisme (F-03) ; qu'un format de mandat porte **un attribut de type
versionné** (F-46) ; que les algorithmes de remplacement sont normalisés tandis que le calendrier de
retrait ne l'est pas (F-62, F-59). **Ce qu'il n'établit pas** : **les trois conditions énoncées
ci-dessous, qui ne sont endossées par aucune source.** *La somme appelle **crypto-agile** un mécanisme
dont la spécification satisfait trois conditions* : **(1)** l'algorithme y est **un paramètre nommé du
contrat**, et non une hypothèse implicite du format — c'est le **découplage** ; **(2)** le contrat porte
**une version vérifiable**, de sorte qu'un vérificateur puisse constater à quel régime il a affaire —
c'est le **contrat** ; **(3)** la spécification documente **le passage d'une valeur du paramètre à la
suivante, retrait de l'ancienne compris** — c'est l'**évolution**. ⚠ *Le quatrième terme de l'invariant,
l'**exploitation**, en fait **une charge qui se réévalue** plutôt qu'un travail qui s'achève* (H-27,
**[C]**, thèse attribuée). ⚠ **La troisième condition est celle qui décide, et c'est contre elle que ce
chapitre doit se tenir en garde** : *une spécification qui ne documente pas cette procédure **n'est pas
convaincue de défaut** — elle est **muette**, et le silence se qualifie à son degré.*

⚠ **L'invariant n'est pas employé nu, et sa forme se cite exactement.** Il est **une thèse d'un volume
antérieur, à attribuer** : *« découplage, contrat, évolution » deviennent « découplage, contrat,
évolution, exploitation »* (H-27, **[C]**). **Une entrée [C] ne porte jamais un fait central** : *elle
fournit ici un cadre, non une preuve*, et **le quatrième terme est refermé au Livre IV**, non invoqué
ici.

**L'état des recommandations, tel que le socle le porte, se résume à un écart de statut** — **algorithmes
normalisés, calendrier de retrait non normalisé** (F-62 ; F-59). *Le § 21.1 en est le siège ; il n'est
pas rejoué.*

⚠ **Deux précisions se rattachent directement à l'objet de ce mouvement, et l'une comme l'autre nuance
ce qu'un statut « final » autorise à croire.** *(1)* **Les fiches des deux normes finales portent
l'une et l'autre un avis d'errata** annonçant des corrections dans une révision future, et l'une porte
en outre une **note de planification** signalant plusieurs points mineurs à corriger. ⚠ **Le socle ne
documente aucune date pour la révision annoncée — degré 3** ; **tri : PROJETÉ** — *intention publiée
sans échéance relevée.* ***Un statut final ne vaut pas texte figé : le paramètre vers lequel on migre
bouge lui aussi, ce qui est un argument pour l'agilité et non contre elle.*** *(2)* **Le véhicule
normatif désigné pour porter les échéances est lui-même à l'état de projet** (§ 21.1) : *le document
institutionnel qui a la transition pour objet est, à la date de consultation, dans le même état que
celui qui la date.*

⚠ **Une clause du dossier réglementaire intéresse la crypto-agilité au niveau où on l'attend le
moins.** La note d'application ordonne aux agences d'aligner leur plan sur le projet **« ou un document
successeur »** (F-61). Lecture de l'auteur — **ce que le socle établit** : le libellé de cette clause.
**Ce qu'il n'établit pas** : l'intention de son rédacteur, ni l'effet de la clause sur un plan
d'agence. *La lecture proposée est que **cette clause est un patron d'agilité appliqué non au format
mais au texte** : une obligation qui s'ancre sur **une classe de documents** plutôt que sur **une
instance** survit au remplacement de l'instance. C'est, transposé à la gouvernance, exactement ce que
la première condition ci-dessus demande d'un format.* **Elle est réfutable** : *un texte d'application
qui nommerait un successeur précis la ferait tomber.*

## § 21.5 — Audit de crypto-agilité des mécanismes d'émission et du mandat

L'audit demande à chaque mécanisme **les trois questions de la définition**, et **il n'en tire que ce
que la spécification démontre**. ⚠ **Trois précautions le bornent, et elles ne sont pas de forme.**
*(1)* **Un mécanisme dont la spécification est muette sur un point reçoit un degré d'absence, non un
verdict défavorable** — *c'est la faute que R-02 proscrit, et c'est elle que ce paragraphe risque à
chaque ligne de son tableau.* *(2)* **Deux des entrées mobilisées sont en [C]** et **ne portent aucune
affirmation centrale**. *(3)* **La dernière ligne ne porte pas sur un mécanisme** : *le passeport
d'agent est un objet de synthèse construit par la somme* — **en auditer la crypto-agilité, c'est
auditer une construction**, et le tableau le dit à sa dernière ligne plutôt que de le taire.

| Mécanisme | Où l'algorithme est déclaré, et ce que la spécification en **démontre** | Ce que le socle ne porte pas sur son changement — **degré 3** pour chaque cellule | Trace |
|---|---|---|---|
| **Carte d'agent signée** (v1.0.0) | un paramètre **obligatoire** de l'en-tête protégé nomme l'algorithme, parmi trois imposés et un seul facultatif nommé (F-03, **[A, degré 1]**) ; **la charge n'est pas transportée** et le vérificateur la **reconstruit** par re-canonicalisation (F-01 ; F-02, **[A]**) | procédure de transition d'un algorithme à un autre ; politique d'acceptation par le vérificateur ; **existence d'un profil cryptographique obligatoire ou d'une liste fermée** — *le lot déclare n'avoir recherché aucun profil de ce type* | ch. 15 § 15.1.1, § 15.1.4 |
| **Rotation sur ce même mécanisme** | plusieurs signatures **MAY** coexister « to support key rotation » ; **c'est le seul dispositif de rotation** que la section prévoie (F-10, **[B]**) | **procédure de retrait d'une clé compromise** ; emploi du dispositif pour une transition d'**algorithme** plutôt que de **clé** | ch. 15 § 15.1.3 ; ch. 20 § 20.4 |
| **Mandat de paiement agentique** (v0.2.0) | sérialisation et **attribut de type versionné** (F-46, **[B]**) ; la spécification impose **l'appariement exact de la chaîne de type, suffixe de version compris** | mécanisme de retrait d'un mandat ; procédure de passage d'une version de type à la suivante ; **régime de compatibilité entre deux versions** | ch. 17 § 17.1 ; ch. 20 § 20.4 |
| **Identité de charge de travail** | la spécification énonce qu'un justificatif est **considéré valide s'il a été signé par une autorité du domaine de confiance** de l'identité qu'il porte (F-87, **[B]**) | **tout élément d'algorithme, de profil ou de transition** ; le profil et la version mis en œuvre chez un fournisseur ne sont pas documentés sur la page consultée | ch. 3 (socle) ; ch. 15 § 15.2.2 ; **F-36, [C]**, corroboration seule |
| **Registre gouverné** | **deux champs obligatoires** du profil d'agent (F-40, **[B]**, borné à ces deux champs) ; ce que le document décrit par là est **un régime de champs et d'invalidation**, et il **ne démontre par ce seul fait aucune propriété cryptographique** (R-02) ; côté annuaire, l'adressage par contenu est **présenté** comme fondant l'intégrité, **sans démonstration** (F-55, **[C, degré 1]**) | la présence ou l'absence d'un élément cryptographique **parmi les autres champs du schéma** — *le socle ne porte pas l'inventaire complet* ; la fonction de hachage employée et sa substituabilité ; ⚠ le balayage porte sur une **révision supplantée, non rebalayée** | ch. 15 § 15.3.1, § 15.3.2 |
| **Passeport d'agent** | *néant* — **objet de synthèse sans spécification**, donc **sans contrat porteur d'un paramètre d'algorithme** | **le socle ne documente pas d'objet composé de ces quatre pièces** | ch. 16, ouverture |

: Tableau 21.3 — Audit de crypto-agilité, mécanisme par mécanisme, au 21 juillet 2026 — ce que chaque spécification démontre, et ce que le socle ne porte pas.

**Deux résultats se dégagent, et ils tirent en sens contraire.**

**Le premier est favorable, et il faut le borner tout de suite.** La carte signée dispose d'un point où
l'algorithme est déclaré, **et ce point est obligatoire** (F-03). *Comme la charge n'est pas
transportée et que le vérificateur la reconstruit à partir de la carte reçue, **un changement de valeur
de ce paramètre n'oblige pas à changer le format de l'artefact**.* ⚠ **Ce que la spécification démontre
est donc qu'un algorithme est nommé par signature et que la vérification est reproductible à partir du
document ; elle ne documente ni la procédure de passage d'un algorithme à un autre, ni la politique par
laquelle un vérificateur accepte ou refuse une valeur** (R-02). ⚠ *La spécification illustre d'ailleurs
ce paramètre par **deux valeurs données en exemple**, sans liste fermée, et le lot déclare expressément
n'avoir recherché **aucun profil cryptographique obligatoire** — **il ne faut pas conclure de ces deux
exemples à une restriction**.*

⚠ **Une qualification du rapport de lot n'est pas reprise ici, et le motif est déclaré.** Ce rapport
écrit, à l'adresse de ce chapitre, que « la crypto-agilité de la carte est **structurellement
présente** ». ⚠ **Cette qualification excède ce que le lot a balayé** : *elle porte sur ce que le
mécanisme **permettrait**, non sur ce que la spécification **démontre**, et le rapport déclare lui-même
n'avoir recherché aucun profil obligatoire.* **Elle n'est ni une affirmation votée, ni une entrée de
socle. Le chapitre retient le fait positif et borné, et laisse le reste au degré 3.**

**Le second est défavorable, et il porte sur la version plutôt que sur l'algorithme.** Le mandat est,
des mécanismes relevés, **le seul dont le contrat soit explicitement versionné** : l'attribut de type
porte sa version, et la spécification **exige que les mises en œuvre apparient la chaîne exacte,
suffixe compris** (F-46). *La deuxième condition de la définition est donc satisfaite — mais elle l'est
d'une manière qui **déplace le coût**.*

Lecture de l'auteur — **ce qu'il n'établit pas** : ce qu'il advient d'un vérificateur confronté à une
version qu'il ne connaît pas, ni qu'aucun régime de compatibilité n'existe ailleurs dans la
spécification. *La lecture proposée est qu'**un appariement exact transforme le changement de version
en bascule coordonnée plutôt qu'en transition progressive** : émetteurs et vérificateurs doivent changer
ensemble, ou la vérification échoue.* ***Une version explicite rend le changement détectable ; elle ne
le rend pas graduel.***

⚠ **Reste le constat qui vaut pour le tableau entier, et il s'écrit à la formule imposée plutôt qu'en
généralité.** **Le socle ne documente, pour aucun des mécanismes inventoriés dans ce paragraphe, de
procédure de transition d'un algorithme à un autre — absence de documentation, non fait négatif
vérifié.** *L'énoncé porte sur les six lignes du tableau et sur elles seules ; il ne dit rien des
mécanismes qu'aucun lot n'a ouverts, ni des sections que les lots déclarent n'avoir pas atteintes.*

## § 21.6 — Patrons de migration sans rupture de la chaîne de confiance

Lecture de l'auteur — **ce paragraphe entier est une construction d'auteur, et le marquage se porte à
son ouverture.** **Ce que le socle établit** : le dispositif de signatures multiples et son objet
déclaré (F-10), le régime temporel des mandats (F-46), l'énumération de l'en-tête protégé et l'absence
de validité dans la carte (F-03, F-05), et la clause d'ancrage sur un document successeur (F-61). **Ce
qu'il n'établit pas** : **qu'il existe des patrons de migration, qu'ils soient au nombre de quatre, ni
qu'aucun d'eux préserve une chaîne de confiance.** ⚠ **Le socle ne documente aucun patron de migration
cryptographique — degré 3.** *Ce qui suit est proposé par la somme et adossé, patron par patron, à ce
que le socle porte ; chacun est assorti de ce qui le réfuterait.*

**Patron 1 — la coexistence de signatures pendant la transition.** *Le véhicule structurel existe* :
plusieurs signatures **MAY** être portées par une même carte, et la spécification en déclare l'objet —
*la rotation des clés* (F-10) ; et le paramètre d'algorithme est déclaré dans l'en-tête protégé de
**chaque** signature (F-03) — **il est donc porté au grain de la signature, non au grain de la carte**.
⚠ **Ce que le socle n'établit pas est précisément l'emploi visé** : *le dispositif est spécifié pour la
rotation des **clés**, et **le socle ne documente pas son emploi pour une transition d'algorithme** —
degré 3.* **Ce qui le réfuterait** : *une clause restreignant les signatures multiples à une même
valeur du paramètre.* ⚠ **Et une limite en borne d'avance la portée** : les cartes **MAY** être signées
et les clients **SHOULD** vérifier (F-04) — *un régime facultatif ne permet pas d'imposer une
transition, il permet de l'offrir.*

**Patron 2 — l'hybride comme mesure temporaire, et non comme état stable.** Le projet de l'institut
énonce que, lorsqu'elles sont employées, **les solutions hybrides sont « typically expected to be
temporary measures that lead to a second transition »** vers des outils n'employant que des algorithmes
post-quantiques. *(Source citée à la réserve d'une affirmation versée, que le texte de l'entrée ne
reprend pas.)* **Le patron consiste donc à compter deux transitions et non une.** ⚠ **Réserve portée par
le lot et reprise telle quelle** : *le projet **ne dit pas** que les modes hybrides restent admis
au-delà de 2035, et lui prêter cette autorisation serait lui faire dire ce qu'il n'écrit pas.* **Tri de
la seconde transition : PROJETÉ.** **Ce qui le réfuterait** : *une révision du document abandonnant
l'hybride, ou en faisant un régime cible.*

**Patron 3 — la brièveté de l'artefact plutôt que sa révocation.** *Un artefact dont la durée de vie
est bornée migre par son renouvellement ordinaire : il n'y a rien à retirer, seulement à cesser
d'émettre.* Le socle documente ce régime **pour les mandats**, qui portent leurs attributs temporels
(F-46) ; en corroboration seulement, l'identité d'agent d'un fournisseur repose sur des certificats
**de vingt-quatre heures** (F-36, **[C]** — *repérage, non fait central ; cas documenté, jamais
recommandation*). ⚠ **Le patron est indisponible pour la carte signée** : *elle ne porte aucun paramètre
temporel dans son en-tête protégé (F-03) et aucun champ de validité ni de statut parmi ses quatorze
(F-05, **[A, degré 1]**) — **elle ne périme que par sa clé**, dont le ch. 15 § 15.1.3 établit que le
statut n'est pas établissable.* **Ce qui le réfuterait** : *une prescription de fraîcheur portée par
une section normative non ouverte — et le ch. 15 § 15.1.3 en nomme deux, restées inaccessibles par
troncature.*

**Patron 4 — l'ancrage sur une classe de document plutôt que sur une instance.** Le § 21.4 l'a relevé au
niveau de la gouvernance : *une obligation qui vise un document « **ou un document successeur** » ne
devient pas caduque au remplacement du document* (F-61). **Transposé au format, le patron consiste à
faire pointer un artefact vers un profil nommé et versionné plutôt que vers un algorithme littéral.**
⚠ **Le socle ne documente, pour aucun des mécanismes du § 21.5, l'existence d'un tel profil — degré
3** ; *le lot déclarant, pour la carte signée, n'en avoir recherché aucun.* **Ce qui le réfuterait** :
*la publication d'un profil cryptographique obligatoire pour l'un de ces mécanismes.*

**Ce qu'aucun de ces quatre patrons ne règle, et qui décide de l'ordre des travaux.** ⚠ *Une migration
est une opération de **retrait** autant que d'ajout, et c'est le point où les entrées mobilisées
s'arrêtent.* **La rotation est outillée, le retrait ne l'est pas** (F-10) ; **l'inventaire de la
révocation est au ch. 20 § 20.4**, qui en dégage trois formes — *le silence, l'interdiction sans le
moyen, l'état sans la fraîcheur.* S'y ajoute ce que le § 21.2 a déclaré : **ni procédure de re-signature
ni horodatage d'appoint — degré 3**.

**Reste à nommer la rupture que le titre vise.** ⚠ ***Une chaîne de confiance ne se rompt pas au moment
où l'algorithme change : elle se rompt lorsqu'un vérificateur ne peut plus établir, pour un artefact
déjà émis, sous quel régime il l'a été.***

Lecture de l'auteur — **ce qu'il n'établit pas** : qu'une chaîne de confiance se rompe, ni qu'une
migration l'expose. *La lecture proposée est que **la crypto-agilité et la révocabilité sont la même
propriété vue de deux côtés** : un mécanisme qui ne sait pas retirer ce qu'il a émis **ne peut pas
achever une migration** — il peut seulement en ajouter une couche.* **Elle est réfutable** : *un
mécanisme documentant une transition d'algorithme sans dispositif de retrait la ferait tomber.*

## § 21.7 — Ce que les études de coût publiées couvrent (et ne couvrent pas)

Le lot a cherché des études de coût de migration. ⚠ **Il en a ouvert une**, et l'énoncé de ce résultat
**porte sa borne dans sa formulation même** : *la seule étude de coût commanditée par une autorité
publique **que cette passe a ouverte**.* ⚠ **Le lot déclare expressément n'avoir mené aucun balayage de
la littérature sur ce point, et refuse d'en tirer une affirmation d'unicité** — *les chiffres circulant
dans la presse spécialisée n'ont pas été instruits et ne sont pas rapportés.*

Cette étude est un **rapport de juillet 2024 au législateur fédéral américain**, prescrit par une loi
de préparation à la cybersécurité quantique. Selon ce rapport, un bureau de la présidence déclare que
**le coût total, à l'échelle du gouvernement, de la migration des systèmes d'information prioritaires
entre 2025 et 2035 s'établirait à environ 7,1 milliards de dollars de 2024**. ⚠ **Cette donnée est
auto-déclarée** — *elle est produite à partir des estimations remises par les agences elles-mêmes* —
**et n'a fait l'objet d'aucune vérification indépendante** ; le rapport porte lui-même sa réserve
d'incertitude — *« a high, but expected, level of uncertainty »* — et **impose une mise à jour
annuelle**. ⚠ **Tri : PROJETÉ** — *projection d'une institution, avec sa source nominative, son
millésime et son périmètre, **jamais un coût constaté**.* *(Source primaire ouverte et citée hors
socle, non versée ; le chapitre n'écrit donc nulle part que « le socle porte » ce chiffre.)*

⚠ **Le périmètre de ce chiffre est ce qui décide de son usage, et il est étroit sur quatre plans.** Il
porte sur les **systèmes fédéraux civils prioritaires** des États-Unis, entre 2025 et 2035 ; **les
systèmes de sécurité nationale en sont exclus** ; il ne porte **ni sur une entreprise, ni sur une
institution financière, ni sur une juridiction canadienne** ; et **il ne porte pas davantage sur la
couche identitaire agentique** — *le lot déclare n'avoir rien instruit sur l'application de ces jalons
aux signatures de cartes, aux chaînes de mandat ou aux jetons.* ⚠ ***Un chiffre dont le périmètre exclut
l'objet de la somme ne devient pas applicable parce qu'on le divise.***

**Le déplacement européen : de l'échéance vers le risque.** Deux documents prennent la question par
l'autre bout, et **leur intérêt tient moins à ce qu'ils chiffrent qu'à ce qu'ils ne chiffrent pas**. Le
rapport conjoint de 2026 **ordonne ses activités par le risque plutôt que par un calendrier daté**
(F-63, **[B, degré 1]**), et **porte son propre avertissement de non-obligation** — *c'est un document
de praticiens, non un acte d'autorité*. Le second n'énonce **aucune échéance calendaire propre au
secteur** : ses cinq recommandations sont **sans date**, et la seule échéance datée relevée est
**attribuée à l'administration américaine**. ⚠ *Réserve : la date de publication de ce second document
n'a pas pu être établie sur une page de son éditeur.*

⚠ **Ce relevé a une conséquence directe sur l'héritage, et elle est désagréable : une entrée héritée est
périmée sur ce point** (F-63). Le Vol. I prête à un forum sectoriel des cibles propres ; **la source
primaire ouverte par la passe n'en porte pas**, dans les bornes de son balayage. ⚠ ***Une cible
attribuée à un forum qui ne l'énonce pas est exactement ce que R-11 proscrit en interdisant de
fusionner des jalons d'origines distinctes.***

Lecture de l'auteur — **ce que le socle établit** : que le rapport européen ne porte aucune des trois
chaînes relevées, et que le balayage hors socle du second n'y relève aucune échéance sectorielle. **Ce
qu'il n'établit pas** : **par quel chemin l'entrée héritée en est venue à prêter ces cibles à ce
forum**. *Tout au plus se constate-t-il que deux des millésimes concernés sont les deux échéances du
décret ; **aucune source du socle ne relie ce texte à l'entrée héritée**.* ⚠ ***Seul l'écart est
documenté ; sa provenance ne l'est pas, et la somme ne la reconstitue pas.***

⚠ **Le versant du Vol. I, en [C], ajoute un verrou d'ingénierie que le socle propre ne porte pas.** Son
§7.4.4 nomme **deux propriétés qui s'opposent** — *la longévité requise d'un justificatif d'autorité et
la nature jetable d'une identité d'agent instanciée pour une tâche* — et une **soutenabilité de
performance non établie** : *les signatures et échanges post-quantiques, dont les tailles d'artefacts
sont sensiblement accrues, doivent être soutenus sur des charges éphémères à fort débit de poignées de
main, profil de trafic caractéristique des flottes d'agents.* ⚠ **Régime** : entrée en **[C]**, et le
Vol. I trie lui-même ce verrou **SPÉCULATIF** ; *aucune mesure publique ne le valide à son gel, et
aucun énoncé de ce paragraphe n'est central.*

## § 21.8 — Méthode d'inventaire pour une institution

*Puisqu'aucun nombre n'est transposable, ce qui se transmet est une méthode.* Lecture de l'auteur —
**elle est construite ici, et elle est une construction d'auteur en totalité.** **Ce que le socle
établit** : les quatre contraintes du § 21.1 et du § 21.4. **Il n'établit pas de méthode d'inventaire,
pas de nomenclature d'artefacts, pas de pondération de risque, pas d'ordre de grandeur de charge.**
*Les cinq relevés qui suivent sont proposés par la somme ; **ils ne sont endossés par aucune source**.*

*Le point de départ n'est pas une liste d'algorithmes mais **une liste d'artefacts qui portent une
signature ou un établissement de clés** dans la chaîne d'identité et de mandat.* **Le § 21.3 en dresse
l'inventaire ; ce paragraphe propose ce qu'il faut relever sur chacun.**

1. **Le mécanisme et ses paramètres.** *Quel algorithme, quelle longueur de clé, quel niveau de sécurité
   déclaré.* ⚠ **C'est le seul relevé pour lequel les jalons publiés fournissent une grille directement
   applicable** : le projet écrit « Deprecated after 2030 » au niveau 112 bits et « Disallowed after
   2035 » tous niveaux confondus (F-60).
2. **La durée de vie de ce que l'artefact protège.** *Un jeton d'accès de dix minutes et une chaîne de
   mandat archivée dix ans ne portent pas le même risque devant la même échéance.* **C'est le relevé qui
   décide de l'ordre de traitement**, et c'est la logique que le rapport sectoriel met en avant en
   croisant le risque quantique et le temps de migration (F-63).
3. **L'autorité qui peut faire tourner la clé.** *Qui la détient, selon quelle procédure, avec quel
   délai constaté.* ⚠ ***Un artefact dont l'autorité de rotation n'est pas identifiée n'est pas migrable
   à échéance : il est à re-gouverner d'abord.***
4. **Le régime qui lie l'artefact — s'il en existe un.** ⚠ **C'est ici que la discipline de R-11 se
   paie.** Les jalons relevés viennent de **quatre origines distinctes qui ne se fusionnent pas** : le
   projet de l'institut, **qui vise sans prescrire** ; le décret, **qui fixe des échéances pour le
   périmètre fédéral qu'il définit** ; la note d'application, **qui échelonne** ; et une cible générale
   citée par le projet lui-même — *cette quatrième origine est **hors socle**, et son versement est
   remonté.* **Le relevé consiste à nommer laquelle des quatre s'applique, à quel titre et sur quel
   périmètre.** ⚠ *La confrontation ne se saute pas au motif que l'exploitant est canadien* : le décret
   charge par ailleurs de publier une **règle proposée** d'acquisition visant les contractants couverts
   — *une règle proposée n'est ni une règle en vigueur ni une obligation constatée, et son périmètre se
   lit avant de conclure.*
5. **L'agilité du contrat qui porte l'artefact.** *Le mécanisme de signature est-il un paramètre
   versionné du contrat, ou une hypothèse câblée ?* **C'est l'objet du § 21.5, et c'est le relevé qui
   transforme une migration en changement de configuration plutôt qu'en réécriture.**

⚠ **Ce que la méthode interdit.** *(1)* **Dériver une charge d'entreprise d'un agrégat fédéral** : *le
rapport projette un coût pour un périmètre nommé, et ce périmètre exclut ce que la somme prend pour
objet.* *(2)* **Convertir une échéance en obligation** : *« Deprecated » n'est pas une interdiction — le
projet écrit lui-même que l'algorithme peut être employé et que la décision revient au propriétaire des
données* (F-60).

⚠ **Reste ce qui ne se relève pas, et qui doit être écrit plutôt que comblé.** **Le socle ne documente
ni le coût unitaire de migration d'un artefact d'identité d'agent, ni aucun ordre de grandeur de charge
applicable à un parc d'entreprise — degré 3.** ***Le chapitre ne propose donc aucun ratio, aucune
fourchette et aucune règle de trois — et ce refus est le résultat de la passe, non un pis-aller.***

⚠ **Une lacune est ouverte ici et elle est la plus coûteuse du chapitre pour un volume canadien** :
*quelles échéances les autorités canadiennes énoncent-elles, et sous quel régime ?* **Aucune passe de
recherche n'a été conduite** — le lot déclare n'avoir rien instruit hors du couple États-Unis / Union
européenne, **et signale lui-même que cette lacune est la plus coûteuse de celles qu'il laisse.**
*Sources à retrouver : les publications de l'autorité nationale de cybersécurité et les travaux du
groupe de travail sectoriel canadien, dont le rapport précise que **la mention ne repose que sur des
communiqués de presse** — le sigle comptant **zéro occurrence** dans le texte extrait du rapport
européen.* **La question reste ouverte ; aucune inférence n'est proposée.**

## § 21.9 — Fenêtre d'action 2026-2029 : le calendrier inverse

Lecture de l'auteur — **la fenêtre qui donne son titre à ce paragraphe est une construction de la
somme**, développée et bornée en fin de section. *Le socle porte des échéances datées ; **il ne porte
aucun délai de mise en œuvre applicable à une institution**.*

*Un calendrier de migration ne se lit pas dans le sens de la lecture. **Il se lit à rebours**, depuis
la date la plus contraignante qui s'applique réellement à l'institution, en remontant vers l'instant
présent.* ⚠ **Encore faut-il savoir laquelle des dates publiées s'applique — et le socle établit
qu'elles ne sont ni de même nature, ni de même force, ni de même statut** (§ 21.1).

**Trois lectures se tirent du tableau du § 21.1, et deux d'entre elles sont des constructions
d'auteur : la première seule est un fait.**

**La première est un fait, et c'est le cœur de l'horloge** : *les algorithmes de remplacement sont
normalisés depuis le 13 août 2024, tandis que le calendrier de retrait demeure, à la fiche consultée, à
l'état de projet public initial* (F-62 ; F-59). ⚠ ***Une institution n'attend donc rien du côté de ces
deux primitives — elle attend du côté des dates.***

**La deuxième appelle une lecture, et elle est contre-intuitive.** Le projet écrit que ses normes
d'algorithmes **peuvent** continuer de spécifier des techniques vulnérables jusqu'en 2035, et annonce
que **des guides propres à une application pourront imposer des transitions plus précoces** (F-60).
Lecture de l'auteur — *2035 y fonctionne donc **comme un plafond et non comme un plancher**.* **Ce
qu'il n'établit pas** : que 2035 vaille plafond **pour un exploitant donné**, ni qu'un guide sectoriel
plus précoce existe pour la couche agentique. ⚠ ***Une institution qui lirait 2035 comme sa propre
échéance lirait le plafond d'un autre.***

⚠ **Conformément à R-11** : l'institut **vise** une dépréciation en 2030 au niveau de sécurité de
112 bits et une interdiction en 2035 tous niveaux confondus, **dans un document à l'état de projet
public initial** — *aucune de ces deux lignes n'est formulée en obligation, et **un jalon de cet
institut n'est pas une obligation légale**.*

**La troisième est une lecture d'auteur, et elle porte la borne de droite du titre.** Lecture de
l'auteur — **ce que le socle établit** : une date d'obligation applicable à un périmètre fédéral
américain nommé, le 31 décembre 2030 pour l'établissement de clés (F-61) ; que l'institut vise 2030 et
2035 **dans un projet** ; et que la clause « ou un document successeur » **est précisément ce qui
empêche ce projet de devenir la norme sur laquelle une obligation se fonderait**. **Ce qu'il n'établit
pas** : **aucun délai de conception, aucun cycle de renouvellement d'infrastructure, aucune durée de
migration d'un parc — degré 3.** *La fenêtre **2026-2029** est donc une construction de la somme : elle
borne à droite l'intervalle qui précède la première échéance datée du socle, et **elle vaut ce que vaut
l'hypothèse — non sourcée — qu'un parc d'agents ne se migre pas dans l'année de son échéance**.*
⚠ ***Le lecteur qui juge cette hypothèse fausse doit refaire le calcul, non ajuster le résultat.***

**Ce que le calendrier inverse produit concrètement n'est pas un plan de migration : c'est un ordre de
travaux.** Lecture de l'auteur — *les artefacts **dont l'autorité de rotation n'est pas identifiée**
passent en premier, parce qu'ils ne sont pas migrables tant qu'ils ne sont pas gouvernés — et **cette
gouvernance est un travail d'identité, pas de cryptographie**. Viennent ensuite les artefacts **dont le
contrat n'expose pas son mécanisme de signature comme un paramètre versionné** (§ 21.5). Viennent en
dernier **les artefacts agiles**, dont la migration est un changement de configuration à échéance.*

⚠ **C'est aussi le point où le quatrième terme de l'invariant hérité trouve une application littérale**
(H-27, **[C]**, thèse attribuée) : ***une dette de migration n'est pas un problème d'architecture qu'on
résout une fois ; c'est une charge d'exploitation qui se réévalue à chaque révision du document qui
porte l'horloge*** — et ce document est, à la date de gel, **un projet** (F-59). ⚠ **Aucun calendrier de
finalisation n'a été relevé — degré 3** ; *il ne s'en déduit rien sur les intentions de l'institut.*

**Ce que ce chapitre refuse d'écrire, et pourquoi il le déclare.** *(1)* Il **ne convertit pas** en coût
unitaire, en ratio ou en fourchette d'entreprise la projection de coût du § 21.7 : *le périmètre du
chiffre exclut l'objet.* *(2)* Il **n'attribue aucune échéance sectorielle** au forum dont le balayage
n'en relève aucune. *(3)* Il **ne présente aucun des quatre jalons comme liant d'office une institution
canadienne** : *les périmètres que le socle porte sont fédéraux et américains, et le rattachement
éventuel d'un exploitant à l'un d'eux **se constate, il ne se présume pas**.* *(4)* Et il **ne comble
pas la lacune canadienne par transposition d'un calendrier étranger** — ⚠ ***un calendrier qu'on
transpose devient, en trois citations, une échéance.***

### Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Le siège de l'horloge** (§ 21.1), avec ses trois origines **qui ne se fusionnent pas** et le statut
   réel de chaque texte. Les **ch. 45 et 49** y renvoient ; **aucun ne re-date un jalon**.
2. **La formulation imposée** : « **visée** », jamais « fixée », jamais un ordre de grandeur approché ;
   et **le statut du document porté à chaque mention**. *C'est le garde-fou le plus mécanique du Livre,
   et le plus facile à casser d'inadvertance.*
3. **La définition opérationnelle de la crypto-agilité en trois conditions**, marquée construction
   d'auteur, et **le constat que sa troisième condition n'est satisfaite par aucun mécanisme
   inventorié**.
4. **Le renversement qui ferme le Livre** : ***la crypto-agilité et la révocabilité sont la même
   propriété vue de deux côtés.*** Le **ch. 20 § 20.4** avait établi l'asymétrie émission/révocation ;
   le § 21.6 en montre le coût à l'échéance.
5. ⚠ **Et un legs négatif, qui est celui du Livre entier** : *la fabrique d'émission des ch. 12 à 18
   repose sur des signatures classiques, et **aucun de ses mécanismes ne documente comment en sortir**.*

---

## § 21.10 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui est enfreint.** Portes **G-3** et **G-4** ; volet résiduel de **G-1** non instruit ; ordre de
rédaction du PRD §6. Instruction d'auteur du 27 juillet 2026.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ **Et ce chapitre est celui du Livre où
   l'écart entre la précision apparente et le régime de preuve est le plus grand** : *il porte des dates
   au quantième, des libellés verbatim et des numéros de section — et **tout cela résout contre un socle
   que G-3 n'a pas refondu et que G-4 n'a pas collationné**.*
2. **Les décomptes sont publiables** (G-2). Écart de **+43,8 %** — **le plus fort du Livre** ; **la volumétrie du Livre entier**
   alimente **D-4** par **R-IV-17**.
3. **Les renvois « ch. N » vers les Livres III à V sont des renvois de plan** : **ch. 45** et
   **ch. 49**. Les renvois vers le **ch. 3** résolvent contre du texte ; ceux vers les **ch. 15, 16, 17,
   20** résolvent contre du texte au terme de la présente passe.
4. **Une entrée héritée est déclarée périmée sur un point précis** (§ 21.7), **et la pièce ne la corrige
   pas** : *c'est le socle propre du Vol. III qui le porte, et la correction relève de **G-3**.*

**Remontées ouvertes par ce chapitre :**

- **R-IV-36 — non bloquante, et elle constate qu'une relève du plan est déjà consommée à la source.**
  Le TOC porte, pour ce chapitre, une relève « **à instruire à la source primaire** » : *des instruments
  fédéraux américains de juin 2026 — décret exécutif et directive — alignant les systèmes fédéraux sur
  les jalons de 2030 et 2035, ce qui rendrait l'échéance opposable outre-frontière.* ⚠ **Or ces deux
  instruments sont **déjà au socle du Vol. III**, versés en F-61 avec leurs dates, leur périmètre et
  leur tri** — le § 21.1 les porte à ce titre. **Demande remontée** : que **G-1** enregistre cette
  relève comme **consommée par la source elle-même**, plutôt que comme due. ⚠ *La relève n'est pas
  fausse : elle est **datée d'avant l'instruction du Vol. III**, et le plan ne l'a pas rapprochée de son
  propre socle.* **Le constat vaut au-delà** : *une relève du plan et une entrée de socle peuvent porter
  le même objet sans que rien ne les rapproche — c'est un défaut de collation, et il est du ressort du
  volet de fond de G-4.*
- **R-IV-37 — non bloquante, de siège et de formulation.** Le TOC assigne à ce chapitre **le siège de
  l'horloge** et le garde-fou R-11, mais **le siège du statut PROJETÉ de la normalisation du passeport
  est au ch. 16 § 16.4**, et **le tri prospectif lui-même** — les trois statuts et leur définition — est
  posé au **Vol. I §7.0.2**, hérité en **[C]** et **sans siège désigné dans la somme**. ⚠ *Trois
  chapitres du Livre II trient donc des énoncés prospectifs contre une définition qu'aucun d'eux ne
  porte, et qu'aucun contrôle ne vérifie.* **Demande remontée** : **désignation d'un siège unique du tri
  prospectif** — vraisemblablement au Livre I, où il est déjà employé —, et **versement du siège de
  l'horloge à la table de [`PRD/check-sieges.py`](../PRD/check-sieges.py)**, avec les trois autres
  sièges que ce Livre pose (voir **R-IV-24**, ouverte au ch. 15).

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.24** — § 21.1 à § 21.9,
dans l'ordre exact, les deux mouvements dans leur ordre —, et le § 21.0 est une introduction de
chapitre. Les **deux tables de couverture sont respectées pour leurs cinq lignes**. Le **siège de
l'horloge est posé et marqué** (§ 21.1). Le **socle IAM et l'identité de charge de travail restent au
ch. 3** ; l'**inventaire de la révocation reste au ch. 20 § 20.4** ; l'**assemblage du passeport reste
au ch. 16** ; le **quatrième terme de l'invariant reste refermé au Livre IV**. ⚠ **Les dix-sept
occurrences de R-11 portent la formulation imposée** : *« visée », jamais « fixée »*, **aucun ordre de
grandeur approché n'est écrit**, le **statut du document est dit à chaque mention**, et **les quatre
origines de jalons ne sont fusionnées à aucun endroit**. Les **quatorze occurrences de R-14** portent
leur degré, dont **douze au degré 3**. Les **neuf occurrences de R-02** énoncent ce que la spécification
démontre **et** ne démontre pas — dont le **refus explicite de reprendre la qualification de
« crypto-agilité structurellement présente »** que le rapport de lot proposait. La **projection de coût
est attribuée à son auteur, à son millésime et à son périmètre à chacune de ses deux occurrences**, et
**aucun ratio n'en est dérivé**. Enfin, les **quinze occurrences de « Lecture de l'auteur »** sont
suivies de ce que le socle établit et n'établit pas — dont **deux paragraphes entiers**, le § 21.6 et
le § 21.8, marqués à l'ouverture.
