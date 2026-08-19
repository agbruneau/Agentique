# Audit — `État de l'art.md` et `État de l'art.pdf`

Audit du 19 août 2026, mené sur la source, le rendu (127 pages, texte extrait
intégralement, huit pages recomposées en PNG pour inspection visuelle), la chaîne
`build/rendre-recension.py`, le gabarit, le filtre `accentuation.lua`, les deux figures et le
`README.md` du dossier. Les chemins cités vers les autres dossiers du dépôt ont été vérifiés en
existence seulement — leur contenu n'a pas été rouvert, conformément au statut de rapport dérivé.

☑ **Les dix-huit anomalies ont été corrigées le même jour**, et chaque tâche porte ci-dessous ce qui
a été fait, la voie retenue quand l'audit en offrait plusieurs, et la vérification qui la clôt. Le
PDF est recomposé — **128 pages**. ⚠ **Une dix-neuvième anomalie a été trouvée pendant l'exécution
et n'est pas corrigée** : elle est consignée en A9, hors du périmètre de cette passe.

*Ce que cette passe n'a pas fait, et ne pouvait pas faire* : aucune des sept sources n'a été
rouverte, aucun énoncé du rapport n'a été révisé sur le fond. Elle répare des renvois, des cardinaux,
des chemins et un rendu. *Réparer un renvoi n'est pas rouvrir un livrable.*

---

## A. Anomalies de fond — le PDF ou le MD porte un énoncé faux ou cassé

### A1. Formule du plancher d'exploration corrompue au PDF ☑

**Constat.** [État de l'art.md](État%20de%20l%27art.md) (§ 6.2) écrit
`(φ_min/φ_max)^α·(η_min/η_max)^β`. Pandoc appariait les deux `^` (extension `superscript`) et le PDF
composait `α·(η_min/η_max)` **en exposant**, β restant sur la ligne — la borne du § 6.2 était
mathématiquement fausse au rendu (page composée 81). Vérifié visuellement et reproduit sur la
chaîne.

**Tâche.**
- [x] `build/rendre-recension.py` : `-f markdown-raw_html` → `-f markdown-raw_html-superscript-subscript`,
  avec le motif écrit en commentaire à l'appel. `pass^k` (§ 3.8) est inchangé.
  ☑ *Vérifié au folio 82 du PDF recomposé, au rendu PNG : la formule tient sur la ligne de base.*

### A2. Page de titre : « quatre gels » contre « sept gels » ☑

**Constat.** Le gabarit portait en sous-titre « sept livrables, **quatre gels** qui ne coïncident
pas » ; le corps écrit trois fois « **sept gels** étalés sur dix semaines », et le tableau des
livrables en dénombre sept. La page de titre contredisait le rapport qu'elle ouvre.

**Tâche.**
- [x] `build/recension.template` : sous-titre corrigé en « sept gels qui ne coïncident pas ».
  ☑ *Vérifié à la page de titre du PDF recomposé.*

### A3. Neuf renvois vers un « ch. 0 § 4 » qui n'existait plus ☑

**Constat.** L'Ouverture ne comptait que trois sections ; neuf renvois visaient « ch. 0 § 4 ». La
passe du 17 août avait supprimé les sections de régime. Le `README.md` affirmait que « le régime
qu'ils visaient se lit au tableau 0.2 » — inexact pour une partie du contenu visé : les **cardinaux
de la revue** (12 attestées, 32 autodéclarées, 145 sans revue), le **plafond/plancher** du corpus
académique et la distinction **régime fort / régime faible** de la veille ne figuraient ni au tableau
ni ailleurs dans l'Ouverture.

**Tâche — voie A retenue** (réintroduction, plutôt que repointage) :
- [x] Un **§ 4 — Le régime des sources, et ce qu'il interdit** est réintroduit à l'ouverture,
  condensé des §§ 4 à 6 du brouillon `chapitres/00-liminaires.md` : régime du compendium (hors
  portes, CA-IV-01, CA-IV-11 et CA-IV-13, matière du Vol. I en [C]) ; deux régimes de la veille et
  absence de ronde adverse aux passes d'août ; trois classes de la revue avec leurs deux bornes ;
  rejeu du traité et sa portée d'un livrable sur sept.
- [x] La phrase du § 3 « Trois remarques closent cette ouverture » devient « closent ce tableau », le
  § 4 lui succédant.
- [x] `README.md` : la réserve est déplacée en « soldé », et son affirmation inexacte sur le tableau
  est déclarée comme telle plutôt que supprimée.
  ☑ *Les neuf renvois ont été repris un à un contre le contenu du nouveau § 4 : les neuf aboutissent.*
  ⚠ *Le § 4 est un condensé, non une copie : `chapitres/` porte encore les sept sections d'origine et
  n'a pas été repris — la divergence du brouillon reste déclarée aux Réserves.*

### A4. Épilogue : « registre d'identité » pour le registre d'attributs d'observabilité ☑

**Constat.** Le constat 2 du sommaire exécutif écrivait « sur soixante-trois attributs du **registre
d'identité**, aucun ne décrit une chaîne de délégation… ». Les soixante-trois attributs sont ceux du
registre d'attributs `gen_ai.*` des conventions sémantiques d'observabilité, tel que le rapport les
nomme partout ailleurs (ch. 3 § 3.9, ch. 5 § 5.2, ch. 8 § 8.4). *C'est précisément parce que ce
registre n'est pas un registre d'identité que le fait négatif porte.*

**Tâche.**
- [x] Corrigé en « registre d'observabilité ».
  ☑ *Vérifié au folio 120 du PDF. L'unique « registre d'identité » restant est celui du ch. 2 § 2.3
  — le registre d'identité d'agents proposé au W3C —, qui est le bon objet.*

### A5. § 8.10 / § 8.11 : décompte incohérent des déplacements de frontière ☑

**Constat.** Le § 8.10 pose **six** déplacements dont aucun ne bute sur une impossibilité, plus un
**septième hors liste** qui, lui, y bute. Le § 8.11 écrivait « Cinq **des six** déplacements
possibles ne demandent aucune découverte ; **un seul bute sur une impossibilité** », ce qui rangeait
l'impossibilité *dans* les six.

**Tâche.**
- [x] § 8.11 corrigé : « **Six des sept** déplacements possibles ne demandent aucune découverte ; **le
  septième** bute sur une impossibilité ». ☑ *Vérifié au folio 119 du PDF.*

### A6. Lien mort en tête de source : `gauntlet-log.md` ☑

**Constat.** `[journal](gauntlet-log.md)` — le fichier a quitté le dossier le 17 août (649 lignes,
conservées dans l'historique git). Le lien pointait dans le vide. Ce paragraphe précède le premier
`##` et ne passe pas au PDF : l'anomalie était propre au MD.

**Tâche — troisième voie retenue** (retrait plutôt que restauration) :
- [x] Le lien est retiré et remplacé par l'énoncé de ce qui lui est arrivé : le journal est nommé,
  sa sortie du dossier datée, et sa survie dans le seul historique `git` déclarée.
  *Restaurer le fichier aurait défait une décision du 17 août ; le rapport nomme l'état plutôt que de
  le réparer.*

### A7. Renvoi erroné au sommaire exécutif : « (ch. 7 § 7.10) » pour les métriques d'éditeurs ☑

**Constat.** La puce « Les métriques d'éditeurs » renvoyait à « (ch. 7 § 7.10) » pour trois faits —
décomptes d'éditeurs jamais vérifiés, rapports payants, chiffre de marché inattribuable — établis aux
**§ 7.3** et **§ 7.11**. Le § 7.10 n'en porte aucun.

**Tâche.**
- [x] Renvoi corrigé en « (ch. 7 § 7.3, § 7.11) ». ☑ *Vérifié au folio 123 du PDF.*

### A8. Chemin mort : `bancs/nf05-debit/VERDICT.md` ☑

**Constat.** Le § 6.3 citait `bancs/nf05-debit/VERDICT.md` comme siège du verdict NF-05. Le dossier
`3 - Traité/bancs/` **a été supprimé en entier le 17 août 2026** (commit `20cc1ae`), le même jour que
la sortie de `gauntlet-log.md`. Contrôle sur l'historique : le PRD du traité
(`3 - Traité/docs/PRD.md`) survit et porte la réserve NF-05 — *de l'ordre de dix à quinze secondes
simulées par seconde-cœur à n = 1 000, écart structurel en Θ(n²), cible à refaire sur la mesure* —,
mais **les quatre chiffres détaillés que le rapport cite** (599 à *n* = 64, 61 à *n* = 256, 15,2 à
*n* = 1 000, blocage à *n* = 12 500) **ne se retrouvent nulle part dans le dépôt courant** : ils
n'existaient que dans le verdict supprimé.

**Tâche.**
- [x] La citation est repointée sur `3 - Traité/docs/PRD.md`, réserve NF-05 — la source qui survit.
- [x] Les quatre chiffres détaillés portent désormais leur réserve, écrite à l'endroit où ils sont
  cités et à la doctrine du rapport lui-même (ch. 1 § 1.7) : *ils ne sont pas devenus faux, ils sont
  devenus invérifiables autrement que par l'historique `git`, et c'est un état différent qui doit se
  dire.*
  ☑ *Vérifié au folio 84 du PDF.* ⚠ *Le PRD du traité porte lui-même un lien mort vers ce verdict —
  constat hors périmètre de cet audit, qui ne vise que la recension.*

### A9. ⚠ Le § 8.8 revendique un rang que le § 7.1 refuse de revendiquer — **non corrigé**

**Constat, trouvé pendant l'exécution et non pendant l'audit.** Le ch. 7 § 7.1 pose une réserve
explicite sur le rang de la passe du 15 juillet 2026 : *« La prose du § 2.2 [de la veille] ne compte
que trois passes à soumettre tout leur lot à la ronde adverse — les 2, 7 et 13 juillet — et n'y range
pas celle du 15 »*, les deux énoncés du livrable ne pouvant être exacts ensemble, et il conclut :
*« Ce rapport ne tranche pas et ne se réclame donc d'aucun rang. »* Or le ch. 8 § 8.8 écrit que cette
matière *« vient de la passe du 15 juillet 2026, **l'une des trois seules du livrable à soumettre
tout son lot à une ronde adverse** »* — **et cite le ch. 7 § 7.1 comme source**. Le § 8.8 revendique
exactement l'appartenance dont le § 7.1 déclare ne pas se réclamer, et l'appuie sur le paragraphe qui
la refuse.

C'est la même espèce d'anomalie que A5 : une incohérence interne entre deux sections, dans le
chapitre dont la fonction est de borner les sept autres.

**Tâche — laissée à l'auteur, hors du périmètre de cette passe.**
- [ ] Reformuler le § 8.8 pour qu'il retienne ce que la ligne porte sans son appartenance — par
  exemple : « la passe du 15 juillet 2026, que le tableau des quinze passes porte adverse à trois
  votants, avec la réserve de rang que le ch. 7 § 7.1 pose et ne lève pas ». *Le § 4 réintroduit à
  l'ouverture par A3 a été écrit sous cette forme prudente, pour ne pas propager la revendication.*

---

## B. Anomalies d'appareil — numérotation, légendes, style

### B1. Légende du tableau des cinq écarts sans étiquette ☑

**Constat.** La légende du tableau des cinq écarts (§ 6.5) était la seule des quatre sans étiquette
« Tableau N.M » : elle échappait au gras appliqué par la chaîne (`RE_LEGENDE`) et au décompte du
`README.md`.

**Tâche.**
- [x] La légende devient « **Tableau 6.1** — Les cinq écarts consignés… ».
- [x] Le renvoi « le tableau du § 6.5 de ce chapitre » (§ 6.3) devient « le tableau 6.1 ».
- [x] `README.md` : décompte porté à 9 tableaux dont quatre numérotés.
  ☑ *Vérifié au folio 86 du PDF, au rendu PNG : l'étiquette est en gras comme les trois autres.*

### B2. « Tableau 0.2 » sans « Tableau 0.1 » ☑

**Constat.** La numérotation des tableaux commençait à 0.2, le tableau des sept gels ayant été retiré
le 17 août. Le `README.md` déclarait que renuméroter « aurait cassé les renvois » — il n'y en avait
que trois, plus une mention portée par la figure 0.1.

**Tâche — première voie retenue** (renumérotation, plutôt que réintroduction du tableau retiré, dont
le contenu est déjà porté par la colonne « Gel » du tableau des livrables) :
- [x] « Tableau 0.2 » → « **Tableau 0.1** », légende et trois renvois.
- [x] `figures/contenu.py` : la mention portée par la figure 0.1 suit, et **les SVG ont été
  régénérés** — contrôle fait, une seule ligne change, la figure 0.2 est intacte.
- [x] Le § 4 réintroduit par A3 renvoie au tableau sous son nouveau numéro.
  ☑ *Vérifié : cinq occurrences de « tableau 0.1 » au PDF, zéro de « 0.2 ».*

### B3. Style des titres de sections : chapitre 1 seul avec tiret ☑

**Constat.** Les huit sections du chapitre 1 s'écrivaient « 1.1 — Titre » ; toutes les autres « N.M
Titre ». L'écart était visible dans la table des matières.

**Tâche.**
- [x] Les huit titres sont repris. ☑ *Vérifié à la table des matières du PDF : plus aucun tiret.*

### B4. Citations du compendium non étiquetées ☑

**Constat.** Quelques renvois au compendium restaient nus et se confondaient avec la numérotation
propre du rapport (ch. 7 § 7.1 et § 7.11) ; inversement, un renvoi du ch. 1 § 1.7 désignait le
rapport lui-même immédiatement après un renvoi au compendium dans la même parenthèse.

**Tâche.**
- [x] Les sept renvois nus du ch. 7 portent désormais « compendium, » ou le possessif qui les y
  rattache.
- [x] Au ch. 1 § 1.7, « ch. 4 § 4.12 pour l'instruction » devient « ch. 4 § 4.12 **de ce rapport**
  pour l'instruction ».

### B5. Gel du Vol. II : « 16 juillet » contre « 16-17 juillet » ☑

**Constat et contrôle.** Le `README.md` du Vol. II porte : *Gel de l'information — 16 juillet 2026
(22 pièces) · 17 juillet 2026 (7 pièces)*. La forme globale exacte est donc « 16-17 juillet 2026 ».

**Tâche.**
- [x] Les deux occurrences qui désignent **le gel du volume** sont uniformisées (ch. 1 § 1.1,
  ch. 1 § 1.7).
- [x] ⚠ **Les deux autres occurrences de « 16 juillet 2026 » sont laissées telles quelles**, contrôle
  fait : ce sont des **faits datés** et non des énoncés de gel — le correctif du 16 juillet 2026 au
  ch. 4 § 4.8, et le fait négatif « au 16 juillet 2026, aucun organisme n'a été désigné » au
  ch. 4 § 4.9. *Les uniformiser aurait falsifié deux dates de fait.*

### B6. Marqueurs ☑ et ✎ non traités par la règle d'accentuation ☑

**Constat.** `accentuation.lua` retire les 127 « ⚠ » mais laisse passer les 6 « ☑ » et 3 « ✎ »,
composés hors famille — le défaut exact que la règle reproche au « ⚠ ».

**Tâche — seconde voie retenue** (déclarer la survie, plutôt que l'étendre la règle) :
- [x] Le motif est écrit dans `accentuation.lua` et au `README.md` : *le fondement de la règle est
  une **densité**, non une famille de fontes* — quatre ⚠ par page sur mille pages ne signalent plus
  rien ; six ☑ et trois ✎ pour 128 pages, soit un par quatorze pages, sont à un tout autre ordre et
  portent chacun un état que la prose ne redit pas. La note pose sa propre condition de révision :
  *si leur nombre croissait d'un ordre de grandeur, c'est la mesure qui trancherait.*
  ☑ *Contrôle sur le PDF recomposé : 0 ⚠, 6 ☑, 3 ✎ — conforme à ce que la note déclare.*

---

## C. Anomalies de documentation — `README.md` du dossier

### C1. « 54 215 mots de corps » ☑

**Constat et contrôle.** Le décompte de référence du dépôt
([`2 - Compendium/PRD/decompte.sh`](../2%20-%20Compendium/PRD/decompte.sh) — un mot = un jeton
portant au moins une lettre ou un chiffre, accents compris) appliqué au corps, c'est-à-dire à tout ce
qui suit le premier `##` et passe donc au PDF, rend **50 655 mots**. `wc -w` sur le même corps rend
52 118. Ni l'un ni l'autre ne donne 54 215.

**Tâche.**
- [x] Le `README.md` porte le chiffre du décompte de référence, **la commande qui le produit et la
  délimitation du corps**, plus le chiffre de `wc -w` en regard — *les deux mesurent deux choses*.

### C2. « 3 tableaux » ☑

**Constat.** Le rapport porte **9 tableaux**, dont quatre légendés et numérotés après B1.

**Tâche.**
- [x] `README.md` : « **9 tableaux** dont quatre numérotés (0.1, 6.1, 8.1, E.1) ».
- [x] Les autres cardinaux du `README.md` sont repris sur la même passe : **91 sections** (90 avant
  le § 4), **128 pages** (127 avant), et la ligne d'historique du 17 août est datée pour ne pas
  contredire le nouveau décompte.

---

## D. Vérifié sans anomalie

Pour donner sa portée à l'audit, ce qui a été contrôlé et tient :

- **Chaîne et structure.** Numérotation des chapitres contiguë (1–8) ; 10 pièces, 91 sections,
  0 sous-sous-section ; bandeaux OUVERTURE / CHAPITRE N / ÉPILOGUE tous présents au PDF ; table des
  matières complète ; en-têtes courants corrects ; métadonnées PDF (titre, auteur, Typst 0.15.1)
  exactes ; PDF synchrone avec le MD.
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
  aboutissent, aux exceptions traitées en A3, A7 et A9 ; les renvois croisés du § 8.7 correspondent
  au contenu visé.
- **Chemins du dépôt** : tous re-contrôlés après correction — les sept fichiers et dossiers des
  livrables, les douze fichiers de `3 - Traité/crates/`, les deux SVG. *Aucun chemin mort ne subsiste
  dans la source.*

**Limites de l'audit.** Les livrables sources (`1 - Corpus`, `2 - Compendium`, `3 - Traité`,
`4 - Veille`) n'ont pas été rouverts : les renvois « compendium, ch. N § … », « veille, § … » et
« revue, § … » n'ont été vérifiés ni en existence ni en contenu, et les cardinaux externes
(pages, références, entrées de socle F-xx/S-xxx) sont pris tels que portés. Le cardinal
« F-01…F-48 (46 entrées) » n'a pas pu être arbitré de l'intérieur (48 numéros pour 46 entrées —
plausible si deux entrées sont retirées ; à confirmer contre le Vol. II si souhaité).

---

## Ce qui a été touché

| Fichier | Ce qui change |
|---|---|
| [`État de l'art.md`](%C3%89tat%20de%20l%27art.md) | A3 à A8, B1 à B5 — un § 4 neuf à l'ouverture, quatre énoncés corrigés, deux chemins repris, une numérotation, huit titres, neuf renvois étiquetés |
| [`État de l'art.pdf`](%C3%89tat%20de%20l%27art.pdf) | recomposé — **128 pages** |
| `build/rendre-recension.py` | A1 — extensions `superscript` et `subscript` désactivées, motif en commentaire |
| `build/recension.template` | A2 — sous-titre de la page de titre |
| `build/accentuation.lua` | B6 — la survie de `☑` et `✎` déclarée et motivée |
| `figures/contenu.py` | B2 — la mention du tableau suit la renumérotation |
| `figures/f-00-1-echelle.svg` | B2 — **régénéré** ; `f-00-2-rupture.svg` inchangé |
| [`README.md`](README.md) | C1, C2 — cardinaux repris et méthode de décompte nommée ; les réserves soldées passent en « soldé », celles qui tiennent restent |

⚠ **Ce que la passe n'a pas touché.** Aucun énoncé de fond, aucune source, aucun chiffre hérité d'un
livrable. `chapitres/` n'a pas été repris et diverge davantage qu'avant — *il n'est plus lu, et c'est
ce qui rend la divergence inoffensive, pas ce qui la rend fausse.* Et **A9 reste ouverte** : elle
demande une décision d'auteur sur un énoncé, non une réparation d'appareil.
