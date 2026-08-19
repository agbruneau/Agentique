# Audit — `État de l'art.md` et `État de l'art.pdf`

Audit du 19 août 2026, mené sur la source, le rendu (127 pages, texte extrait
intégralement, huit pages recomposées en PNG pour inspection visuelle), la chaîne
`build/rendre-recension.py`, le gabarit, le filtre `accentuation.lua`, les deux figures et le
`README.md` du dossier. Les chemins cités vers les autres dossiers du dépôt ont été vérifiés en
existence seulement — leur contenu n'a pas été rouvert, conformément au statut de rapport dérivé.

Chaque anomalie porte sa tâche de correction. Quatre des anomalies (A6, A7, B1, B2) sont déjà
déclarées aux Réserves du `README.md` comme « constatées, non corrigées » ; elles sont reprises ici
avec leur tâche, la décision de les corriger malgré la clôture du dépôt appartenant à l'auteur.

---

## A. Anomalies de fond — le PDF ou le MD porte un énoncé faux ou cassé

### A1. Formule du plancher d'exploration corrompue au PDF

**Constat.** [État de l'art.md:1554](État%20de%20l%27art.md) écrit
`(φ_min/φ_max)^α·(η_min/η_max)^β`. Pandoc apparie les deux `^` (extension `superscript`) et le PDF
compose `α·(η_min/η_max)` **en exposant**, β restant sur la ligne — la borne du § 6.2 est
mathématiquement fausse au rendu (PDF, page composée 81). Vérifié visuellement et reproduit sur la
chaîne.

**Tâche.**
- [ ] Dans `build/rendre-recension.py` (appel pandoc, ligne 164), remplacer
  `"markdown-raw_html"` par `"markdown-raw_html-superscript-subscript"`. Correctif testé : les
  carets restent littéraux et `pass^k` (ligne 967) est inchangé. Recomposer et revérifier la
  page 81.

### A2. Page de titre : « quatre gels » contre « sept gels »

**Constat.** Le gabarit (`build/recension.template`, ligne 470) porte en sous-titre « sept
livrables, **quatre gels** qui ne coïncident pas » ; le corps écrit trois fois « **sept gels**
étalés sur dix semaines » ([lignes 1853, 2199, 2315](État%20de%20l%27art.md:1853)), et le
`README.md` (ligne 47) aussi. Le tableau 0.2 dénombre bien sept gels. La page de titre contredit le
rapport qu'elle ouvre.

**Tâche.**
- [ ] Corriger le sous-titre du gabarit en « sept gels qui ne coïncident pas » (ou reformuler),
  puis recomposer.

### A3. Neuf renvois vers un « ch. 0 § 4 » qui n'existe plus — et un contenu réellement absent

**Constat.** L'Ouverture compte trois sections (§ 1–3) ; neuf renvois visent « ch. 0 § 4 »
([lignes 206, 788, 880, 882, 993, 1119, 1154, 1621, 1661](État%20de%20l%27art.md:206)). La passe du
17 août a supprimé les sections de régime (le brouillon `chapitres/00-liminaires.md` en avait
sept). Le `README.md` (Réserves) affirme que « le régime qu'ils visaient se lit au tableau 0.2 » —
c'est inexact pour une partie du contenu visé : les **cardinaux de la revue** (12 attestées, 32
autodéclarées, 145 sans revue), le **plafond/plancher** du corpus académique et la distinction
**régime fort / régime faible** de la veille, tous annoncés « posés aux liminaires », ne figurent
ni au tableau 0.2 ni ailleurs dans l'Ouverture. Ils survivent seulement dans les chapitres qui les
répètent (ch. 1 § 1.1, ch. 3 intro).

**Tâche** (une des deux voies) :
- [ ] **Voie A (recommandée)** — réintroduire à l'Ouverture un « § 4 — Le régime des sources »
  condensé (régimes fort/faible de la veille, absence de ronde adverse aux passes d'août,
  cardinaux 12/32/145 avec plafond et plancher, règle d'héritage), matière récupérable de
  `chapitres/00-liminaires.md` §§ 4–6 ; les neuf renvois redeviennent exacts sans être touchés.
- [ ] **Voie B** — repointer les neuf renvois vers « ch. 0 § 3, tableau 0.2 » et enrichir la
  colonne « Régime de preuve » du tableau pour qu'elle porte réellement tout ce que les renvois
  visent.
- [ ] Dans les deux cas, mettre à jour la réserve correspondante du `README.md`.

### A4. Épilogue : « registre d'identité » pour le registre d'attributs d'observabilité

**Constat.** Le constat 2 du sommaire exécutif ([ligne 2215](État%20de%20l%27art.md:2215)) écrit
« sur soixante-trois attributs du **registre d'identité**, aucun ne décrit une chaîne de
délégation… ». Les soixante-trois attributs sont ceux du **registre d'attributs** `gen_ai.*` des
conventions sémantiques d'observabilité (OpenTelemetry), tel que le rapport les nomme lui-même
(ch. 3 § 3.9 « registre d'attributs », ch. 5 § 5.2, ch. 8 § 8.4). L'étiquette « registre
d'identité » est un contresens — c'est précisément parce que ce registre **n'est pas** un registre
d'identité que le fait négatif porte.

**Tâche.**
- [ ] Corriger en « du registre d'attributs d'observabilité » (ou formulation équivalente), puis
  recomposer.

### A5. § 8.10 / § 8.11 : décompte incohérent des déplacements de frontière

**Constat.** Le § 8.10 pose **six** déplacements dont aucun ne bute sur une impossibilité, plus un
**septième hors liste** (l'accord sous asynchronie) qui, lui, bute sur une impossibilité
([lignes 2139–2167](État%20de%20l%27art.md:2139)). Le § 8.11 écrit : « Cinq **des six**
déplacements possibles ne demandent aucune découverte ; **un seul bute sur une impossibilité** »
([ligne 2183](État%20de%20l%27art.md:2183)) — ce qui range l'impossibilité **dans** les six,
contredisant la structure du § 8.10. Le sixième point du § 8.10 (l'instrument) reste par ailleurs
non couvert par la phrase « cinq sont des actes d'adoption, de conception mineure ou de lecture ».

**Tâche.**
- [ ] Harmoniser : soit « Six des sept déplacements possibles ne demandent aucune découverte ; le
  septième bute sur une impossibilité », soit refondre le décompte du § 8.10 pour que les deux
  sections comptent la même chose.

### A6. Lien mort en tête de source : `gauntlet-log.md`

**Constat.** [Ligne 15](État%20de%20l%27art.md:15) : `[journal](gauntlet-log.md)` — le fichier a
quitté le dossier le 17 août (649 lignes, conservées dans l'historique git ; réserve déclarée au
`README.md`). Le lien pointe dans le vide. Ce paragraphe précède le premier `##` et ne passe pas au
PDF : l'anomalie est propre au MD.

**Tâche** (une des trois) :
- [ ] Restaurer `gauntlet-log.md` depuis l'historique git ;
- [ ] ou repointer la phrase vers l'historique (« au journal, conservé dans l'historique git du
  dépôt ») sans lien ;
- [ ] ou retirer le lien. Mettre à jour la réserve du `README.md` en conséquence.

### A7. Renvoi erroné au sommaire exécutif : « (ch. 7 § 7.10) » pour les métriques d'éditeurs

**Constat.** La puce « Les métriques d'éditeurs » ([ligne 2273](État%20de%20l%27art.md:2273))
renvoie à « (ch. 7 § 7.10) » pour trois faits — décomptes d'éditeurs jamais vérifiés, rapports
payants, chiffre de marché inattribuable — qui sont établis aux **§ 7.3** (inattribuable, rapports
payants) et **§ 7.11** (jamais rouverts/vérifiés). Le § 7.10 ne porte aucun de ces trois faits.

**Tâche.**
- [ ] Corriger le renvoi en « (ch. 7 § 7.3, § 7.11) », puis recomposer.

### A8. Chemin mort : `bancs/nf05-debit/VERDICT.md`

**Constat.** [Ligne 1570](État%20de%20l%27art.md:1570) cite `bancs/nf05-debit/VERDICT.md` comme
siège du verdict NF-05. Ni `3 - Traité/bancs/` ni aucun `VERDICT.md` n'existent dans le dépôt ; le
banc NF-05 vit à `3 - Traité/crates/sim-agents/examples/banc_nf05.rs`. Tous les autres chemins
cités par le chapitre 6 (`determinisme.rs`, `scenario_b.rs`, `stigmergie.rs`, `campagne.rs`,
`usl.rs`, `scenario_d.rs`, `cascade.rs`, `gouvernance.rs`, `sortie_phase_2/3/4/6.rs`,
`docs/decisions.md`) existent.

**Tâche.**
- [ ] Vérifier si le fichier a été déplacé ou supprimé côté `3 - Traité/` (historique git) ;
  corriger la référence vers le siège actuel du verdict, ou noter sa disparition à la manière de la
  réserve sur `gauntlet-log.md`.

---

## B. Anomalies d'appareil — numérotation, légendes, style

### B1. Légende du tableau des cinq écarts sans étiquette « Tableau 6.1 »

**Constat.** La légende [ligne 1596](État%20de%20l%27art.md:1596) (« : Les cinq écarts
consignés… ») est la seule des quatre légendes du rapport sans étiquette « Tableau N.M » : elle
échappe au gras appliqué par la chaîne (`RE_LEGENDE`) et au décompte « 3 tableaux » du `README.md`.
Au PDF, elle rend une légende non numérotée là où les trois autres portent leur étiquette en gras.

**Tâche.**
- [ ] Préfixer « Tableau 6.1 — » à la légende ; ajuster le renvoi textuel « le tableau du § 6.5 de
  ce chapitre » ([ligne 1572](État%20de%20l%27art.md:1572)) en « tableau 6.1 » si souhaité ; porter
  le décompte du `README.md` à 4 tableaux numérotés (voir C2).

### B2. « Tableau 0.2 » sans « Tableau 0.1 »

**Constat.** La numérotation des tableaux commence à 0.2 (réserve déclarée au `README.md` : le
tableau des sept gels a été retiré à la passe du 17 août, et renuméroter « aurait cassé les renvois »).
Les renvois vers le 0.2 sont au nombre de **trois** ([lignes 1854, 2081,
2316](État%20de%20l%27art.md:1854)) — la renumérotation est triviale.

**Tâche** (une des deux) :
- [ ] Renuméroter « Tableau 0.2 » en « Tableau 0.1 » ([ligne 147](État%20de%20l%27art.md:147)) et
  reprendre les trois renvois ;
- [ ] ou, si la voie A de A3 réintroduit le tableau des gels retiré, le numéroter 0.1 et le trou se
  referme de lui-même. Mettre à jour la réserve du `README.md`.

### B3. Style des titres de sections : chapitre 1 seul avec tiret

**Constat.** Les huit sections du chapitre 1 s'écrivent « 1.1 — Titre » ; toutes les autres
(ch. 0, 2 à 8) s'écrivent « N.M Titre » sans tiret. L'écart est visible dans la table des matières
du PDF (p. ii).

**Tâche.**
- [ ] Retirer le « — » des huit titres du chapitre 1 ([lignes 184, 212, 246, 297, 382, 465, 546,
  700](État%20de%20l%27art.md:184)), puis recomposer.

### B4. Citations du compendium non étiquetées, ambiguës avec les chapitres du rapport

**Constat.** La convention du rapport est « (compendium, ch. N § …) ». Quelques renvois au
compendium restent nus et se confondent avec la numérotation propre du rapport :
- [ligne 1651](État%20de%20l%27art.md:1651) : « du ch. 3 § 3.4.5 », « du ch. 38 », « des ch. 3
  § 3.4.3 et 9 § 9.5 » ;
- [ligne 1653](État%20de%20l%27art.md:1653) : « (ch. 4 § 4.4.3) », « (ch. 6 § 6.3.3) » ;
- [ligne 1655](État%20de%20l%27art.md:1655) : « du ch. 3 § 3.4.3 », « du ch. 9 § 9.5.3 » ;
- [ligne 1783](État%20de%20l%27art.md:1783) : « (ch. 9 § 9.5.2) », « (ch. 1 § 1.5.2) ».
Inversement, [ligne 630](État%20de%20l%27art.md:630), « ch. 4 § 4.12 pour l'instruction » désigne
le rapport lui-même immédiatement après « compendium, ch. 30 § 30.1.1 » dans la même parenthèse.

**Tâche.**
- [ ] Préfixer « compendium, » aux renvois nus listés ; à la ligne 630, écrire « § 4.12 de ce
  rapport » ; puis recomposer.

### B5. Gel du Vol. II : « 16 juillet » contre « 16-17 juillet »

**Constat.** Le tableau 0.2 ([ligne 140](État%20de%20l%27art.md:140)) et la
[ligne 1342](État%20de%20l%27art.md:1342) écrivent « 16-17 juillet 2026 » ; les
[lignes 192, 564 et 1087](État%20de%20l%27art.md:192) écrivent « 16 juillet 2026 ».

**Tâche.**
- [ ] Uniformiser (ou vérifier dans `2 - Compendium` si le gel couvre deux jours et si les faits
  cités aux lignes 192/564/1087 sont datés du 16 précisément — auquel cas laisser et ne rien
  faire).

### B6. Marqueurs ☑ et ✎ non traités par la règle d'accentuation

**Constat.** `accentuation.lua` retire les 127 « ⚠ » (aucun ne survit au PDF — vérifié) mais
laisse passer les 6 « ☑ » et 3 « ✎ », composés hors famille (Segoe UI Symbol dans un texte en
Constantia) — le défaut exact que la règle reproche au « ⚠ ». Les glyphes sont incorporés (pas de
tofu), la question est de cohérence d'appareil seulement.

**Tâche.**
- [ ] Décider : soit étendre la règle à ☑/✎ (les retirer ou les traiter), soit déclarer leur survie
  voulue dans le commentaire de `accentuation.lua` et au `README.md` (ils sont rares — un par
  quatorze pages — et porteurs de sens : « revérifié », « correction »).

---

## C. Anomalies de documentation — `README.md` du dossier

### C1. « 54 215 mots de corps »

**Constat.** Le recompte (`wc -w` sur tout ce qui suit le premier `##`) donne **51 583 mots**
(51 754 fichier entier) — écart d'environ 2 600 mots (~5 %) avec le README (ligne 45).

**Tâche.**
- [ ] Recompter avec l'outil d'origine (probablement `2 - Compendium/PRD/decompte.sh`) et corriger
  le README, ou documenter la méthode de décompte à côté du chiffre.

### C2. « 3 tableaux »

**Constat.** Le rapport porte **9 tableaux** (lignes 138, 191, 361, 510, 592, 648, 1589, 1815,
2253), dont 3 légendés numérotés (0.2, 8.1, E.1) et 1 légendé non numéroté (les cinq écarts, voir
B1). « 3 tableaux » (README ligne 45) ne décrit ni l'un ni l'autre décompte sans précision.

**Tâche.**
- [ ] Écrire « 9 tableaux dont 3 numérotés » (4 après B1), ou préciser « 3 tableaux légendés ».

---

## D. Vérifié sans anomalie

Pour donner sa portée à l'audit, ce qui a été contrôlé et tient :

- **Chaîne et structure.** Numérotation des chapitres contiguë (1–8) ; 10 pièces, 90 sections,
  0 sous-sous-section ; bandeaux OUVERTURE / CHAPITRE N / ÉPILOGUE tous présents au PDF ; table des
  matières complète (i–iii) ; en-têtes courants corrects ; 127 pages, métadonnées PDF (titre,
  auteur, Typst 0.15.1) exactes ; PDF synchrone avec le MD (mêmes horodatages, contenu échantillonné
  concordant).
- **Rendu.** Aucun reste de balisage Markdown au PDF ; les 127 « ⚠ » retirés conformément à la
  règle ; figures 0.1 et 0.2 présentes, rendues, avec légendes (et « syntaxique » y est bien
  orthographié — une suspicion de coquille à la rastérisation a été infirmée sur le SVG source) ;
  glyphes spéciaux (Θ, γ, φ, Φ_c, ℓ₉₉, ⁻³, →, ──) servis par les fontes incorporées (Constantia,
  Corbel, Segoe UI Symbol, Libertinus, DejaVu Mono) ; tableaux larges (matrice § 1.6, tableau 10.2,
  8.1, E.1) sans débordement, en-têtes répétés aux sauts de page ; légendes uniformément placées
  au-dessus des tableaux.
- **Arithmétique interne.** 12 + 32 + 145 = 189 et les pourcentages (6/17/77 %) ; 21 520 + 247 =
  21 767 ; plage [51-173] = 123 pièces et 67/123 = 54 % ; 91 + 10 + 22 = 123 entrées ;
  5 + 3 + 1 = 9 contraintes sur 11 entrées ; 12 + 4 = 16 métriques ; π/396 = 7,933 × 10⁻³ et
  l'écart de 0,42 % ; √(0,95/0,001) ≈ 30,8 ; −13,1 % et −9,6 % de volumétrie ; 18 mois et 21 jours
  (6 janv. 2025 → 27 juill. 2026) ; 5 mois 12 jours et 3 mois 1 jour (fusion ACP) ; 90 jours après
  le 28 juillet = fin octobre 2026 ; amplitude Φ_c 0,055 = 18 × 0,003 ; R-G-43…57 = 15 ;
  n = 16 = 64/4. Les décomptes croisés entre chapitres (90 %/φ = 0,916, douze brouillons,
  vingt-sept brouillons, 63 attributs, quatre oracles sur quinze, 3 391 cas / 79 catégories)
  concordent d'une occurrence à l'autre.
- **Renvois internes** (échantillon étendu) : les renvois « ch. N § N.M » internes au rapport
  aboutissent, à l'exception des cas A3 et A7 ; « ch. 0 § 1/2/3 » existent ; les renvois croisés du
  § 8.7 correspondent au contenu visé.
- **Chemins du dépôt** : tous les chemins cités existent, sauf A8 ; `figures/` complet ; les deux
  SVG référencés présents (la chaîne échouerait sinon — vérifié dans le script).

**Limites de l'audit.** Les livrables sources (`1 - Corpus`, `2 - Compendium`, `3 - Traité`,
`4 - Veille`) n'ont pas été rouverts : les renvois « compendium, ch. N § … », « veille, § … » et
« revue, § … » n'ont été vérifiés ni en existence ni en contenu, et les cardinaux externes
(pages, références, entrées de socle F-xx/S-xxx) sont pris tels que portés. Le cardinal
« F-01…F-48 (46 entrées) » (ligne 140) n'a pas pu être arbitré de l'intérieur (48 numéros pour 46
entrées — plausible si deux entrées sont retirées ; à confirmer contre le Vol. II si souhaité).

---

## Ordre de correction suggéré

1. **A1** (formule fausse au rendu — une ligne dans la chaîne) ;
2. **A2, A4, A7** (énoncés faux ou contresens visibles au PDF — trois retouches ponctuelles) ;
3. **A5** (incohérence de décompte ch. 8) ;
4. **A3** (renvois fantômes — la seule tâche de fond) ;
5. **A6, A8** (liens et chemins morts) ;
6. **B1–B6** (appareil) ;
7. **C1–C2** (README) ;
8. Recomposer le PDF une seule fois à la fin (`python "5 - Recension/build/rendre-recension.py"`)
   et revérifier les pages 81 (formule), 1 (titre), ii (table des matières) et 120–124 (épilogue).
