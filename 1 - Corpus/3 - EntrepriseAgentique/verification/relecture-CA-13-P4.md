# Contrôle CA-13 — traçabilité de la Partie IX (ch. 27 et ch. 28)

| Champ | Valeur |
|---|---|
| Objet | **CA-13** : chaque composant, chaque contrat entre étages et chaque correspondance réglementaire de la Partie IX est **tracé à une entrée nommée du socle** (H-xx ou F-xx) **ou marqué « Lecture de l'auteur »** dans sa forme exacte (CA-07). **Il n'y a pas de troisième cas.** |
| Pièces contrôlées | [`monographie/09-partie-IX/ch-27-architecture-reference.md`](../monographie/09-partie-IX/ch-27-architecture-reference.md) ; [`monographie/09-partie-IX/ch-28-instanciation-cloture.md`](../monographie/09-partie-IX/ch-28-instanciation-cloture.md) |
| Spécification de référence | **PRD, Annexe B §B.1 à §B.5**, ouverte intégralement — document de **cadrage**, non entrée de socle |
| Date | **22 juillet 2026** |
| Contrôleur | Distinct du rédacteur et des relecteurs adversariaux des deux pièces (CA-14) |
| Méthode | Inventaire exhaustif, puis pour chaque item : **ouverture de l'entrée citée au PRD §7.2, §7.3, §7.8, §7.9, §7.10 ou §7.11** pour constater qu'elle porte l'énoncé, **ou** relevé du marquage CA-07 et de sa forme, **ou** verdict « ni l'un ni l'autre » |
| Périmètre exclu, et il faut le dire | Ce contrôle **n'a rejoué** ni le contrôle de bornage, ni les motifs de balayage du PRD §A.6, ni la relecture de conformité, ni **CA-12**. *Un contrôle de traçabilité n'atteste que la traçabilité.* **Aucune attestation de conformité n'est portée ici.** |
| Résultat | **Trois cas « ni l'un ni l'autre », trois corrigés** — deux au ch. 27, un au ch. 28. **Aucune trace fausse** : toutes les entrées citées portent ce que les pièces leur font porter |

---

## 1. Pourquoi ce contrôle existe, et ce qu'il a effectivement attrapé

Une architecture de référence est le lieu où une inférence se déguise le plus facilement en acquis : **un composant posé dans un schéma a l'air d'exister, et une fonction retirée d'un schéma a l'air de ne pas exister.** Le PRD, Annexe B, spécifie le blueprint ; il ne le fonde pas — c'est un document de cadrage, et aucune de ses cinq sous-sections n'est une entrée de socle.

Les deux pièces avaient déjà subi, avant ce contrôle, **trois passes adversariales** (deux au ch. 27, une au ch. 28, plus un auto-contrôle) et **trente-deux réfutations appliquées**. Les deux fautes du ch. 27 et celle du ch. 28 ont **survécu à toutes**, et pour un motif qui se répète :

- **La faute du ch. 27 est invisible à un lecteur qui compte.** La Vue 1 du §27.2 annonce « six fonctions », exactement le cardinal de la ligne E1 du §27.1 — mais **pas les mêmes six**. Un relecteur qui vérifie le cardinal voit une concordance ; seul un contrôle qui **confronte l'énumération à celle du §B.2** voit la substitution.
- **La faute du ch. 28 est une omission de clause imposée, non une borne débordée.** La clause renforcée de R-07 n'existe qu'à deux endroits du garde-fou (E-23, B-13), ne se déduit d'aucune entrée, et **aucun motif de balayage du PRD §A.6 ne l'attrape**. Seul un parcours des rapprochements un à un la voit manquer.

⚠ **Un constat de méthode qui vaut pour ce qui reste à écrire en P4.** Le ch. 28 a été épargné par la faute bloquante du ch. 27 pour une raison qui n'est pas le mérite : **il reprend le découpage du PRD §B.4 sans le re-couper** — trois transitions, treize gestes, tous conformes à la spécification. Le ch. 27 re-coupe le §B.2 en trois endroits. *Un chapitre qui reprend la découpe du cadrage n'a rien à marquer ; un chapitre qui la refait doit tout marquer, et c'est là que la faute se loge.*

---

## 2. Inventaire du ch. 27 — composants, contrats, correspondances

### 2.1 Les huit principes directeurs (§27.1, PRD §B.1)

| # | Principe | Régime | Trace ouverte et constatée | Verdict |
|---|---|---|---|---|
| 1 | Rien n'entre au maillage sans passeport | **Marqué inférence** | ch. 8 §8.4 ; H-01 [A ; v1.0.1 en B], H-02 [A], H-03 [A, BROUILLON] — les trois portent bien les matières assemblées ; R-01 | ☑ conforme |
| 2 | Une identité vérifiée à l'admission ne dit rien du comportement | **Tracé, thèse attribuée** | **H-25 [C]** — verbatim constaté au PRD §7.3 : « la signature au moment de la publication n'empêche pas une mutation ultérieure du comportement d'un serveur déjà approuvé » ; `Monographie.md` §3.10.3 et §3.10.4 | ☑ conforme |
| 3 | La frontière de confiance est chaque arête | **Tracé, thèse attribuée** | **H-24 [C]** — `Monographie.md` §3.10.1, verbatim constaté ; siège de la formule déclaré en `Synthese Monographie.md` §5.10 (CA-05, CA-10) | ☑ conforme |
| 4 | Une approbation humaine hors chaîne de mandat protocolaire n'est pas un contrôle | **Marqué inférence** | ch. 9 §9.4 ; **H-15/PC3** — construction d'auteur du Vol. II, sans niveau ni F-xx, constatée telle au PRD §7.2 | ☑ conforme |
| 5 | La trace revient au cadre, jamais à l'agent | **Mixte, scission déclarée** | **H-12 [B]** — préprint non révisé, source unique ; verbatim « n'est généralement pas recommandée » constaté ; forme absolue déclarée décision d'architecture (PRD §B.1, point 5) | ☑ conforme |
| 6 | Adaptation et évolution, deux chemins et deux régimes | **Tracé pour la distinction, inférence pour la conséquence** | **H-11 [B]** — « auto-modification scindée en adaptation éphémère et évolution persistante », constaté au PRD §7.2 ; H-15/PC4 | ☑ conforme |
| 7 | Le mécanisme de signature est un contrat versionné | **Marqué inférence** | ch. 17 §17.1 et §17.2 ; H-17 [C], H-27 [C] ; degré 3 en forme imposée sur l'absence de recommandation normative | ☑ conforme |
| 8 | Le confinement borne l'impact sans prévenir la compromission | **Tracé pour les deux termes, inférence pour l'arbitrage** | **H-11 [B]** — opérationnalisation locale des *frames*, paradoxe de confidentialité ; H-15/PC5 ; réserve de lacune 9 reportée | ☑ conforme |

**Décompte re-mesuré sur la colonne de droite : trois inférences pleines (1, 4, 7), trois mixtes (5, 6, 8), deux thèses attribuées (2, 3).** Concorde avec la légende de la pièce et avec son affirmation centrale n° 2.

### 2.2 Les trois étages et leurs fonctions (§27.1)

La ligne « Fonctions » de la table du §27.1 **reproduit fidèlement** les trois listes du PRD §B.2 — vérifié terme à terme :

| Étage | §B.2 | §27.1 | Verdict |
|---|---|---|---|
| E1 | émission, registre, vérification, révocation, chaîne de mandat, admission d'agent tiers | identique (« chaîne de mandat **protocolaire** », qualificatif imposé par PRDPlan §5.5) | ☑ |
| E2 | PEP/PDP par arête, passerelles, politiques, confinement | identique | ☑ |
| E3 | observabilité, évaluation continue, dérive, incident, cycle de vie | identique | ☑ |

L'architecture elle-même — le fait que ces trois étages composent — est **marquée** au §27.1 avec la forme imposée du degré 3, et l'énoncé est borné aux entrées et sections citées depuis la réfutation 16 de la seconde relecture. ☑

Les cellules « ce que les chapitres établissent » ont été vérifiées entrée par entrée : **F-04, F-05, F-06, F-07, F-09, F-38, F-40, F-41, F-42, F-43, F-46, F-47, F-50** (E1) ; **F-35, F-70, F-71, F-72, F-73** (E2) ; **F-74, F-75, F-76, F-77, F-93, F-96, F-97** (E3). **Toutes portent ce que la cellule leur fait porter**, y compris les deux entrées dont le libellé ne nomme pas les éditeurs (F-70, F-72) et dont la pièce déclare explicitement reprendre les noms du **ch. 23 §23.1** — vérifié à ce chapitre, qui les prend aux sources primaires du lot L-13 et les date. ☑

### 2.3 Les trois contrats inter-étages (§27.1)

| Contrat | Régime | Trace | Verdict |
|---|---|---|---|
| E1 → E2 : passeport vérifiable + chaîne de mandat protocolaire interrogeable à *t* | **Marqué inférence** (encadré CA-07 global) | R-01 ; ch. 8 §8.4 ; ch. 9 §9.2 ; **F-29 [A]** bornée à la révision, la date et l'état, la clause « within a trusted domain » étant portée hors socle et reprise du ch. 10 §10.1 | ☑ conforme |
| E2 → E3 : décision d'autorisation par arête + trace corrélée | **Tracé sur le premier terme, lacune déclarée sur le second** | **F-71 [B]**, **F-70 [B]**, R-02 ; **lacune 21** cas 2 ; **F-95 [B, degré 1]** ; ch. 24 §24.4 | ☑ conforme |
| E3 → E1 : signal de revalidation | **Marqué inférence** — « construction d'auteur en totalité » | ch. 26 §26.2, vérifié : le chapitre porte le même marquage à son ouverture | ☑ conforme |
| Boucle E3 → E1 comme thèse d'architecture | **Marqué inférence** | **H-27 [C]**, verbatim de l'invariant à quatre termes constaté au PRD §7.3, `Synthese Monographie.md` §10.3 ; réfutabilité énoncée | ☑ conforme |

### 2.4 Les trois vues (§27.2) — **cas « ni l'un ni l'autre » n° 1**

| Vue | Éléments posés par la pièce | Éléments du PRD §B.2 | Écart |
|---|---|---|---|
| Vue 1 (E1) | émettre, **ancrer**, inscrire, vérifier, révoquer, admettre — **six** | émission, registre, vérification, révocation, **chaîne de mandat**, admission — **six** | **Substitution** : ancrage ajouté, chaîne de mandat protocolaire retirée |
| Vue 2 (E2) | point de décision, point d'application, passerelle + une relation | PEP/PDP, passerelles, politiques, **confinement** | **Dédoublement** du couple PEP/PDP ; **confinement absent** |
| Vue 3 (E3) | observer, évaluer, détecter la dérive, répondre à l'incident — **quatre** + flèche | observabilité, évaluation, dérive, incident, **cycle de vie** — **cinq** | **Cycle de vie absent** |

**Verdict : ni tracé, ni marqué.** Le contenu de chaque case des trois tables est tracé — c'est ce que les deux relectures avaient vérifié —, mais **le découpage lui-même** ne l'était pas : ni entrée du socle, ni marquage CA-07, alors qu'il s'écarte de la spécification que le §27.1 venait de reproduire fidèlement. Le cardinal identique de la Vue 1 (six, comme E1) rendait la substitution invisible à la relecture.

**Correction opérée** — un marquage **« Lecture de l'auteur »** dans sa forme exacte est posé **avant la Vue 1** : il nomme les trois écarts un par un, trace l'ancrage à **F-09 [B]** pour ce que le socle en documente, déclare ce que le socle établit et ce qu'il n'établit pas, et renvoie les trois éléments écartés à leur siège — contrat de E1 vers E2 (§27.1), **ch. 25 §25.3** (siège du confinement, vérifié : « La réponse à incident agentique : révoquer, confiner, imputer »), **ch. 25** (cycle de vie, dont c'est le titre : « Le cycle de vie opérationnel »). Réfutabilité écrite : le lecteur peut substituer le découpage du §B.2 sans qu'aucune cellule ne tombe.

### 2.5 Points d'intégration avec l'existant (§27.3)

Vérifiés un à un ; **tous tracés, aucune trace fausse** : **F-86 [B]** (verbatim WIMSE constaté, trois bornes reportées), **F-85 [B]**, **F-27 [B]**, **F-84 [B]** (les trois bornes de régime — §E du rapport L-01, hors plafond, ni vote ni bornage — sont bien au socle et sont reportées), **F-28 [B, degré 1]**, **F-41**, **F-42**, **F-87 [B]** (forme du degré 3 que l'entrée écrit elle-même, restituée en entier), **F-88 [B]** (divergence d'un jour reproduite non arbitrée), **F-33**, **F-34**, **F-35**, **F-37**, **H-02**, **F-74**, **F-75**, **F-76**, **F-77**, **F-78**. ☑

### 2.6 La correspondance réglementaire (§27.3) — **cas « ni l'un ni l'autre » n° 2**

| Exigence | Statut du lien, avant contrôle | Vérification R-07 | Verdict |
|---|---|---|---|
| **E-23** | Inférence d'auteur **+ clause renforcée** sur watsonx.governance (H-14, degré 2) + degré 3 pour les autres | Conforme, et c'est le modèle | ☑ |
| Ligne directrice IA de l'AMF | Inférence d'auteur | Pas de clause renforcée — **correct**, elle est réservée à E-23 et B-13 | ☑ |
| Loi 25, art. 12.1 | Inférence d'auteur | idem | ☑ |
| Avis ACVM 11-348 | Inférence d'auteur | idem | ☑ |
| **Cadre bancaire** | « **Attente réglementaire — ne rien anticiper** », **seule** | **Aucun marquage d'inférence sur le rapprochement** | ✗ **corrigé** |
| Jalons post-quantiques | Inférence d'auteur + R-11 | idem | ☑ |

**Verdict : ni tracé, ni marqué.** Le rapprochement « E2 : passerelles conformes au standard à venir ↔ exigence de norme technique unique » est une correspondance composant ↔ exigence réglementaire, et **R-07 n'admet aucune exception** — la règle d'ouverture du tableau écrit elle-même « sans exception ». « Attente réglementaire » qualifie **la prudence due à un texte non publié** ; ce n'est pas un **statut du lien**. Les deux se cumulent, l'un ne tient pas lieu de l'autre.

⚠ **Ce cas n'est pas celui que la réfutation 7 de la première relecture avait traité.** Celle-ci avait corrigé un **décompte** démenti par la colonne (« six inférences » alors que la colonne en portait cinq) ; elle n'avait pas posé la question du **statut** de la sixième ligne. Le décompte était exact ; c'est la colonne qui était incomplète.

**Correction opérée** — le marquage « Inférence d'auteur » est ajouté **devant** le statut d'attente, avec la mention que le second s'y **ajoute** au lieu de s'y substituer. **Légende** et **affirmation centrale n° 6** refaites sur la colonne. Le journal de la première relecture, point (7), est **conservé intact** : son constat décrivait exactement la colonne d'alors.

### 2.7 Le modèle de maturité (§27.4) et l'organisation (§27.5)

- **§27.4** — marquage CA-07 à l'ouverture, « construction d'auteur en totalité » ; **H-31 [C] non élevable** cité en thèse attribuée ; **R-13 dans sa forme complète** (fichier, section, cardinal *et* numérotation ; « copilote » jamais seul) — vérifié contre PRD §8.1. Les vingt cellules du tableau tracées ou déclarées vides. ☑
- **§27.5** — tableau déclaré « **intégralement en inférence d'auteur** », avec la précision que les traces citées portent sur les **objets** opérés et jamais sur l'attribution du rôle. Les sept rôles vérifiés : **F-01, F-04, F-05, F-06, F-07, F-09, F-11, F-19, F-21, F-35, F-38, F-40, F-43, F-65, F-66, F-70, F-71, F-89, F-93, F-97, F-98, H-04, H-06** — toutes portent ce que la cellule leur fait porter. Le rapprochement registre ↔ inventaire d'E-23 y porte **R-07 et la forme complète du degré 3**. ☑

---

## 3. Inventaire du ch. 28 — parcours, contraintes-pivots, péremption

### 3.1 Le découpage du parcours (§28.1 à §28.3)

**Conforme au PRD §B.4, sans re-coupe** — vérifié terme à terme :

| Transition | §B.4 | Pièce | Verdict |
|---|---|---|---|
| Naissance | enregistrement, émission du passeport, admission au maillage | trois actes : inscrire, émettre, admettre | ☑ |
| Vie | délégations, vérifications par arête, traces, évaluations continues, renouvellements, migration post-quantique | six gestes : déléguer, vérifier par arête, tracer, évaluer, renouveler, migrer | ☑ |
| Mort | révocation, cascade, retrait du maillage, archivage probatoire | quatre gestes, ordre identique | ☑ |

C'est ce qui dispense la pièce du marquage que le ch. 27 devait porter.

### 3.2 Les composants du parcours

Toutes les traces vérifiées à l'ouverture des entrées. **Aucune trace fausse.** Points de contrôle notables :

- **F-12 [B]** porte bien la date du 12 mars 2026 pour A2A v1.0.0 ☑
- **F-07 [A]** porte bien « obligation posée au **niveau normatif le plus fort** » — la qualification est **au libellé de l'entrée**, non un superlatif d'auteur ; l'étai textuel siège au **ch. 5 §5.3** (« Révocation et durée de vie »), vérifié sur pièce, et **non au §5.4** que le correctif reçu pointait. La réfutation D de la relecture avait déjà rectifié ce renvoi ☑
- **F-52 [B, degré 1]** porte bien les deux pages MCP et le protocole nommé ☑
- **F-26 [B]** porte bien les quatre identifiants et la dette de vote ; la pièce les cite en repérage seul, aucune affirmation centrale ne s'y adosse (CA-01) ☑
- **F-48 [A, degré 2]** : « **global** » et la **clause de renvoi à un groupe de travail** sont au socle et sont restitués (réfutation F) ☑
- **F-71 [B]** : le libellé s'arrête aux trois champs ; la pièce écrit la borne et ne restaure pas la formule que le **ch. 22 §22.4** déclare deux fois refuser (réfutations A et B) ☑
- **H-32 [C]** porte bien les cinq sous-domaines, les quatre contraintes-pivots et la nature fictive du cas ☑

### 3.3 Les correspondances réglementaires (§28.1 et §28.4) — **cas « ni l'un ni l'autre » n° 3**

Le tableau du §28.4 porte une déclaration R-07 **globale** en ouverture — « toute correspondance entre un composant d'architecture et une exigence réglementaire est une inférence d'auteur, sans exception ». Elle couvre les cinq lignes. ☑

**Ce qui manquait est la clause renforcée**, que R-07 impose **pour E-23 et B-13 seulement** :

| Endroit | Rapprochement posé | Clause renforcée | Verdict |
|---|---|---|---|
| **§28.1** | schéma de registre ↔ inventaire attendu par E-23 | **absente** | ✗ **corrigé** |
| **§28.4**, ligne E-23 | registre ↔ inventaire ; E1 inscription, E3 surveillance | **absente** | ✗ **corrigé** |
| §28.4, ligne B-10/B-13 | **aucun rapprochement proposé** ; la pièce le déclare et renvoie la clause à watsonx.governance | sans objet, déclaré | ☑ |
| §28.4, lignes AMF, Loi 25, résidence | hors E-23/B-13 | non due — **ne pas généraliser** | ☑ |

**Correction opérée aux deux endroits**, dans la forme que le socle autorise et **pas au-delà** : nominativement sur **watsonx.governance**, produit d'IBM, dont l'éditeur ne revendique aucune conformité et dont aucune source ne documente le lien — **fait négatif ÉTABLI**, degré 2, constaté à **H-14 [B]** ; et **au degré 3 dans sa forme imposée** pour les quatre dispositifs de registre, avec l'interdiction de généraliser écrite au corps. C'est exactement ce que le **ch. 27 §27.3 et §27.5** portent aux deux endroits où il fait le même rapprochement : *la pièce-sœur tenait la règle à côté d'elle.*

### 3.4 Les événements de péremption (§28.6)

Huit événements, chacun tracé et portant son tri prospectif (CA-11) ou l'abstention motivée. Vérifiés : **F-69, H-08, H-18, F-80, F-82, F-85, F-75, F-76, F-77, F-74, F-21, F-59, F-60, F-61, F-63, F-52, H-04, F-68, F-66, F-29**. ☑

- Le quatrième événement porte la **forme amendée de R-08** : l'absence est **bornée à l'usurpation du justificatif propre d'un agent**, F-21 établissant que des incidents d'identité non humaine sont publics et datés. ☑
- Le sixième (révision MCP) **n'attribue aucun tri** et motive l'abstention par l'absence de date à la source. ☑ — abstention correcte au regard de H-33.

---

## 4. Ce qui n'a pas pu être tranché, et qui est remonté

1. **Deux dispositions du PRD sont en tension sur la sixième correspondance réglementaire.** **R-07** (PRD §8.1) écrit « toute correspondance produit ↔ réglementation », sans exception ; **§B.3** donne à la ligne « cadre bancaire » le statut « Attente réglementaire — ne rien anticiper » **dans la colonne « Statut du lien »**, c'est-à-dire à la place où les cinq autres lignes portent « Inférence d'auteur ». La correction retenue est **cumulative** — les deux statuts coexistent, l'un qualifiant le lien, l'autre la prudence due au texte à venir — parce que c'est la seule qui ne contredit aucune des deux dispositions. ⚠ **Arbitrer laquelle prime relève de l'auteur** (PRDPlan §5.3) : **remonté, non tranché.**

2. **Le §27.2 emploie « mandat protocolaire » là où F-93 borne son balayage à la chaîne exacte « delegation ».** Le **libellé de F-93** porte lui-même « de mandat », sans qualificatif, et le ch. 26 §26.1 comme le ch. 24 rendent la même substitution. La pièce est donc **fidèle à son entrée** ; c'est le **libellé de l'entrée** qui nomme « mandat » un balayage conduit sur « delegation ». **Aucune correction opérée dans les pièces** — amender un libellé de socle est un acte de socle (PRD §7.10). **Remonté.**

3. **Le §27.3 annonce « trois existants » et en traite quatre.** L'intitulé pose « un système de gestion des identités et des accès, une chaîne d'observabilité, et […] des cadres » ; le corps développe **quatre** blocs — IAM, identité de charge de travail, annuaires commerciaux, observabilité — puis écrit « L'identité de charge de travail est le seul des **trois** existants… », désignant par « trois existants » un ensemble auquel elle n'appartient pas. **La clause d'exclusivité est correctement bornée** (« constat borné aux entrées mobilisées par cette section ») ; seul le **référent du cardinal** est fautif. **Hors périmètre de CA-13 — signalé, non corrigé.**

4. **Le §28.3 écrit une attestation de portée sur sa propre application de R-12** : « Le maillon qui cède est identifié au niveau architectural, **et c'est tout ce qui est écrit ici** ». La seconde proposition est une certification par la pièce de sa propre conformité à R-12, forme que la passe **CA-12** du 21 juillet 2026 a retirée ailleurs (ch. 15 §15.3, attestation auto-délivrée). ⚠ **R-12 est contrôlé par CA-12 seul, et la relecture CA-12 de P4 reste due** : **hors périmètre de CA-13 — signalé, non corrigé.**

5. **Le ch. 25 publie à son en-tête +99,6 % là où la commande de PRDPlan §1.5 mesure +94,6 % sur disque** (6 421 mots pour une cible de 3 300). Le constat a été fait parce que le relevé de rang du ch. 27 devait être refait ; il **porte sur une pièce hors du périmètre de ce contrôle** et n'y a donc pas été corrigé. ⚠ *Un écart publié à un en-tête n'est pas une mesure.* **Signalé.**

6. **Le renvoi `../../doc/TOC.md` des deux pièces ne résout plus** : la gouvernance vit sur disque sous `prd/` au 22 juillet 2026. Les deux pièces le déclarent déjà (ch. 27 remontée 12, ch. 28 remontée 11) et refusent de le corriger seules. **Constat reconduit, non corrigé** — c'est une passe de dépôt sur trente-quatre pièces.

7. **Aucune ligne de registre de gel n'est portée par ce contrôle.** Le registre porte encore « Gabarit » pour les pièces des Parties VII à IX, dont les deux contrôlées. Les volumétries à y inscrire, mesurées le 22 juillet 2026 après ce contrôle : **ch. 27 — 10 648 mots, cible 5 500, +93,6 %** ; **ch. 28 — 10 991 mots, cible 5 500, +99,8 %**. **Remonté à la passe qui rassemblera les pièces.**

---

## 5. Effets de ce contrôle sur les deux pièces

| Pièce | Corps avant | Corps après | Delta | Nature du delta |
|---|---|---|---|---|
| ch. 27 | 10 276 | **10 648** | **+372** | marquage d'inférence (§27.2), marquage et légende (§27.3), affirmations centrales |
| ch. 28 | 10 820 | **10 991** | **+171** | clause imposée de R-07 rendue aux deux endroits |
| **Bloc Partie IX** | 21 096 | **21 639** pour 11 000 — **+96,7 %** | **+543** | **aucune matière ajoutée** |

Décomptes par la commande de PRDPlan §1.5 (`LC_ALL=C.UTF-8`), exécutée sur les **vingt-neuf pièces portant un corps** au 22 juillet 2026, chacune confrontée à la **cible du registre de gel** et non à l'écart publié à son en-tête. ⚠ **Relevé horodaté et périssable** : les pièces d'appareil de P4 s'écrivent concurremment — l'avant-propos est entré au domaine entre deux mesures de la même journée.

Autres décomptes re-mesurés et corrigés dans les pièces : **ch. 27** — marquages « Lecture de l'auteur » au corps, douze → **treize** (quatorzième occurrence = énoncé de la règle CA-13, non un marquage) ; renvois de section distincts, trente-six → **trente-sept** (`ch. 25 §25.3` entré par le marquage) ; rang de volumétrie, second → **troisième**. **Ch. 28** — rang de volumétrie : **premier des vingt-neuf**, clause de rang posée là où l'état antérieur déclarait n'en poser aucune.

---

## 6. Ce que ce contrôle ne dit pas

- Il **ne vaut pas attestation de conformité** des deux pièces, à CA-13 ni à quoi que ce soit d'autre. Il dit ce qui a été inventorié, ce qui a été ouvert, et ce qui a été corrigé.
- Il **ne couvre que les composants, les contrats et les correspondances réglementaires**. Le contrôle de bornage, les motifs du PRD §A.6, la relecture de conformité et **CA-12** restent dus.
- Il **n'a modifié aucune entrée du socle, aucun document de gouvernance, aucune autre pièce** (PRDPlan §5.2 point 6 ; §5.3).
- Il **ne clôt aucune lacune, n'arbitre aucune divergence, ne rouvre aucun lot.**
