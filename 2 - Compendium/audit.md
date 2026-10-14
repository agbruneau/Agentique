# Audit approfondi — *Compendium* (Volume IV)

**Date de l'audit** : 14 octobre 2026
**État du dépôt audité** : `corpus-v1.0` — commit `8b2cf08dcca6f0adf3dd7fb6c76664407b9ea2c9` (16 septembre 2026, clôture en l'état par décision `D-19`)
**Périmètre audité** : Intégralité du répertoire [`2 - Compendium/`](.) — 50 chapitres répartis en 5 livres (`333 416` mots de corps), 6 pages d'accueil (`README.md`), `JOURNAL.md`, 2 annexes (`annexe-bibliographie.md`, `annexe-references.md`), 8 pièces de gouvernance (`PRD/*.md`), 9 scripts de vérification et de décompte (`PRD/*.py`, `PRD/*.sh`), 8 scripts et gabarits de fabrication (`build/*`), 8 modules et manifeste du programme de figures (`figures/*`, 118 fichiers `.svg`), 50 rendus `.html` autonomes et l'archive paginée [`Compendium.pdf`](Compendium.pdf) (1 000 pages, `13 022 826` octets)
**Méthode** : Lecture intégrale (`[L]`) de 100 % des 50 chapitres, des annexes, des pièces de gouvernance et des scripts ; exécution directe (`[R]`) de l'ensemble de la chaîne de vérification, de mutation et de décompte ; confrontation externe (`[S]`) aux sources primaires normatives, réglementaires et académiques au **14 octobre 2026**
**Document compagnon** : [`Évaluation académique.md`](Évaluation%20académique.md) (évaluation universitaire de niveau doctoral selon le [`Gabarit d'évaluation académique.md`](../Gabarit%20d'évaluation%20académique.md) v1.0)

---

## Synthèse exécutive et bilan chiffré

Le *Compendium* (Volume IV du corpus *Agentique*) constitue une somme architecturale, protocolaire et réglementaire d'une ampleur et d'une réflexivité méthodologique exceptionnelles : **50 chapitres**, **5 livres**, **333 416 mots de corps** (pour une cible nominale de `344 500 ± 15 %`, soit **−3,2 %**), **26 sièges de non-redondance** vérifiés mécaniquement à travers les 50 pièces, **1 154 entrées bibliographiques uniques** fusionnées depuis le Volume I, **159 entrées au socle consolidé** (`S-001` à `S-159`), et **118 figures vectorielles SVG** (dont 115 gravées par programme déclaratif sans dépendance externe). L'ouvrage a été clos en l'état le 16 septembre 2026 par la décision **`D-19`** en tant qu'*archive de recherche et d'architecture non destinée à la publication* (`D-18`).

L'audit approfondi mené au **14 octobre 2026** — soit **28 jours après la clôture du dépôt (`16 septembre 2026`)**, **42 jours après la passe de revalidation partielle (`2 septembre 2026`)** et **79 jours après le gel initial du socle (`27 juillet 2026`)** — met au jour quatre ordres de constats majeurs que la clôture du 16 septembre 2026 a laissés ouverts ou que l'écoulement du calendrier jusqu'au 14 octobre 2026 a fait basculer :

1. **Deux échecs d'exécution (`EXIT 1`) dans l'outillage de vérification et deux bogues silencieux dans les scripts de gouvernance (`[R]`)** :
   - [`build/verifier-piece.py`](build/verifier-piece.py) et [`build/verifier-piece-mutations.py`](build/verifier-piece-mutations.py) échouent (`code 1`) sur deux pièces ([`Livre II/14-grille-cinq-questions.html`](Livre%20II/14-grille-cinq-questions.html) l. 677 et [`Livre IV/37-maillage-agents-point-application.html`](Livre%20IV/37-maillage-agents-point-application.html) l. 740) en raison d'une dérive de Pandoc (`3.12.1` vs `3.1.11`) sur les tables à 6 colonnes dont la ligne de séparation excède 72 caractères (`<table style="width:99%;">` contre `<table style="width:100%;">`), faute de l'option `--columns=1000` dans [`build/rendre-piece.py`](build/rendre-piece.py) (**`A-B1`**).
   - [`PRD/decompte.sh`](PRD/decompte.sh) exécuté selon la commande prescrite par [`README.md`](README.md) (`bash PRD/decompte.sh --verifier`) échoue (`code 1`, `Vol. I wc -w brut : 241260` au lieu de `233257`), car la ligne 70 invoque `wc -w` sans le préfixe `LC_ALL=C` appliqué à la ligne 37 (**`A-B2`**).
   - [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py) a mis à jour le bandeau résumé de 5 lignes en tête des 50 chapitres le 15 septembre 2026, mais a laissé dans l'« En-tête de rédaction » en pied de presque tous les chapitres soit un **double pourcentage hybride** accolant le décompte du 2 septembre 2026 à l'écart en pourcentage du 28 juillet 2026 (40 chapitres sur 50), soit l'ancien nombre de mots d'avant la gravure des figures (ch. 10, 31, 35, 40, 42) (**`A-M1`**).
   - [`PRD/check-compendium.py`](PRD/check-compendium.py#L166-L168) comporte un bogue de sous-chaîne dans le contrôle `P3` (`"Vol. II" in "Vol. III"` évalué à `True`), faussant l'identification automatique des pièces mixtes (**`A-M3`**).

2. **Péremption calendaire intégrale sous `CA-IV-04` au 14 octobre 2026 et faille méthodologique de la revalidation IETF du 2 septembre 2026 (`[S]`)** :
   - La fenêtre de validité de 30 jours ouverte par [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) a **expiré le 2 octobre 2026** (depuis 12 jours au 14 octobre 2026) : plus aucun chapitre à haute sensibilité temporelle ne satisfait [`CA-IV-04`](PRD/PRD.md) (**`A-B3`**).
   - La passe du 2 septembre 2026 a vérifié les brouillons IETF sur des URL d'archive immuables (`archive/id/draft-...-00.txt`), qui renvoient éternellement `HTTP 200` même lorsqu'un brouillon est remplacé ou adopté par un groupe de travail. La confrontation directe au Datatracker IETF (`[S]`) révèle que **`draft-klrc-aiagent-auth-00`** (`S-085`, ch. 18 et ch. 50 Événement 10) est passé en `-03` le 6 juillet 2026, a été **adopté par le groupe de travail IETF WIMSE le 9 septembre 2026** et a été **remplacé par `draft-ietf-wimse-aims-00` le 15 septembre 2026** (veille du commit `corpus-v1.0` !), tandis que **`draft-ietf-oauth-v2-1-16`** a été publié le **2 septembre 2026** sans que son numéro `-16` soit reporté au ch. 3 (`§ 3.2.1`) et que **`draft-klrc-wimse-ai-agents-00`** (ch. 12 `§ 12.5`) est **expiré depuis le 1er septembre 2026** (**`A-B4`**).
   - Depuis le **1er octobre 2026**, le calendrier est entré dans le **`T4 2026`**, fenêtre cible conditionnelle du rail de paiement en temps réel canadien (**RTR**, `S-027` / `F-29`). Le compte à rebours de « trente-huit jours » du [`ch. 33 § 33.3`](Livre%20III\33-iso-20022-lynx-rtr.md) et la consultation de 30 jours ouverte le 24 août 2026 sont désormais révolus, tandis que le [`ch. 36 § 36.2.7`](Livre%20III\36-prospective-ap2-rails-canadiens.md) écrit encore au futur que le *By-law no 10* *« doit entrer en vigueur le 24 août 2026 »*, contredisant frontalement le chapitre 33 (**`A-B5`**).

3. **Cinq contradictions internes majeures au Livre II (`D-11`) et deux divergences texte ↔ figures SVG au Livre V (`[L]`)** :
   - La passe d'enrichissement documentaire du 30 juillet 2026 (`D-11`) a greffé des extractions primaires en `[A]` dans les chapitres 13, 16, 17, 20 et 21 **sans purger les paragraphes adjacents**, engendrant cinq contradictions internes directes : W3C VC 2.0 / DID 1.1 simultanément extraits en `§ 13.0` et déclarés « non établis » en `§ 13.1` et en synthèse ; deux `Tableau 16.2` distincts dans le chapitre 16 ; une **4e piste** ajoutée sous le titre `### 17.6.2 Trois pistes...` et conclue par *« aucune des trois »* ; une **10e rangée** (`RFC 7662`) ajoutée au `Tableau 20.1` mais commentée comme *« La onzième rangée »* ; et la feuille de route canadienne `ITSM.40.001` extraite en `§ 21.8` alors que `§ 21.9` affirme toujours que le socle est exclusivement américain (**`A-B6`**).
   - Dans [`figures/contenu5.py`](figures/contenu5.py), la [`Figure 49.0`](figures/f-49-00-cone-incertitude.svg) grave le libellé **`ANNONCÉ`** au lieu du terme canonique **`PROJETÉ`** (employé 45 fois dans le ch. 49 et son siège), et la [`Figure 50.4`](figures/f-50-04-carte-fraicheur.svg) mentionne encore les **« onze événements »** du `Tableau 50.1` au lieu de **quatorze** (**`A-B7`**).

4. **Huit verrous structurels de gouvernance et de preuve hérités de la clôture en l'état (`D-16` / `D-19`)** :
   - Portes `G-4` (fond du Vol. III non publiable), `G-5` (couche d'exécution / harnais `D-2`), `G-6` (matière neuve sans socle des ch. 41, 47 et 48 sous `D-3`/`D-8`) et `G-7` non franchies ; lot transversal `D-9` sur le biais d'automatisation non instruit (affectant les ch. 17, 25, 27 et 40) ; préalable normatif `R-IV-101` sur ArchiMate 4 (`doc C260`) non exécuté (bloquant les ch. 44 et 45) ; préimpressions de la relève `v0.11` lues au seul résumé au ch. 36 (`R-IV-99`) ; et non-réadossement des chapitres aux identifiants `S-001`..`S-159` (`CA-IV-01`, `P3` = 524 emplois nus de `F-xx`/`H-xx` sur 26 pièces mixtes, `P4` = 23 citations de `F-92`, `F-96`, `H-15`).

### Tableau récapitulatif des constats par sévérité

| Catégorie | Code | Nombre | Description synthétique |
| :--- | :---: | :---: | :--- |
| **Bloquants** | `A-B1` à `A-B7` | **7** | 2 échecs de scripts (`verifier-piece.py`, `decompte.sh`), expiration `CA-IV-04` au 2 oct. 2026, obsolescence IETF WIMSE (`draft-ietf-wimse-aims-00`), entrée dans le `T4 2026` du RTR + contradiction ch. 33/36, 5 contradictions internes `D-11` au Livre II, 2 divergences texte ↔ SVG au Livre V |
| **Majeurs** | `A-M1` à `A-M12` | **12** | Bogue du double `%` dans `reporter-volumetrie.py` (50 ch.), troncature des garde-fous par `T4.3` (8 ch.), bogue `P3` dans `check-compendium.py`, 6e recomposition PDF non journalisée + foliotage à `6 mm`, `PRD.md` périmé, `annexe-references.md` désynchronisée (4 `S-nnn`), comptes à rebours 1er mai 2027 et seuil de 90 jours du ch. 35 dépassés, thèse du ch. 8 altérée, `S5` erroné au ch. 31, contradictions de re-datation aux ch. 37/39, contradiction `Tableau 50.1` l. 10, déficit de −37 %/−40 % aux ch. 47–48 |
| **Mineurs** | `A-m1` à `A-m14` | **14** | `echantillon.template` figé au 31 juill., en-têtes `TOC v0.35`, renvois résiduels à `avant-propos` et aux annexes retirées, périphrases d'anonymisation survivantes (décision 18), omissions `T4.3`/`D-16` aux ch. 40 et 41, coquilles ponctuelles (`de de`, doublon l. 15 ch. 3), etc. |
| **Dettes gouvernance (`D-19`)** | `A-D1` à `A-D8` | **8** | Portes `G-4`, `G-5`, `G-6`, `G-7` non franchies, lot `D-9` ouvert (ch. 17/25/27/40), préalable `R-IV-101` ArchiMate 4 C260 non exécuté (ch. 44–45), non-réadossement `S-nnn` (`CA-IV-01`), critères `CA-IV-11`/`12`/`13` et `annexe-bibliographie.md` limitée au Vol. I |
| **TOTAL** | — | **41** | **33 anomalies techniques, documentaires ou calendaires + 8 dettes structurelles de gouvernance actées sous `D-19`** |

---

## 1. Audit de l'appareil de vérification, de décompte et de fabrication (`[R]` / `[L]`)

### 1.1 Exécution intégrale du harnais de vérification (`[R]`)

Les 14 commandes constituant l'appareil de contrôle du *Compendium* et du dépôt parent ont été rejouées (`[R]`) le 14 octobre 2026 sur l'arbre `corpus-v1.0` (`8b2cf08`) :

| # | Commande exécutée (`[R]`) | Code sortie | Résultat observé | Statut |
| :-: | :--- | :-: | :--- | :-: |
| 1 | `python PRD/check-toc.py` | `0` | `OK — tous les contrôles passent (C1-C16).` | **PASS** |
| 2 | `python PRD/check-toc-mutations.py` | `0` | `OK — les 25 mutations sont toutes attrapées (M1-M16b).` | **PASS** |
| 3 | `python PRD/check-sieges.py` | `0` | `OK — les 26 sièges tiennent sur 50 pièces (S1-S5).` | **PASS** |
| 4 | `python PRD/check-sieges-mutations.py` | `0` | `OK — les 115 mutations sont toutes attrapées (M1-M12).` | **PASS** |
| 5 | `python PRD/check-compendium.py` | `0` | `OK — les 50 pièces tiennent (P1-P10), 5 rapport(s) déclaratif(s).` | **PASS** *(avec bogue P3 `A-M3`)* |
| 6 | `python PRD/check-compendium-mutations.py` | `0` | `OK — les 30 mutations sont toutes attrapées.` | **PASS** |
| 7 | `python PRD/reporter-volumetrie.py --verifier` | `0` | `OK — 333 416 mots de corps, les trois sites concordent.` | **PASS** *(en-tête haut seul, `A-M1`)* |
| 8 | `bash PRD/decompte.sh --registre` | `0` | `OK — les cinquante lignes du registre tiennent contre la mesure.` | **PASS** |
| 9 | `bash PRD/decompte.sh --verifier` | **`1`** | `ÉCART Vol. I wc -w brut : 241260 (attendu 233257)` (`0` avec `LC_ALL=C`) | **FAIL (`A-B2`)** |
| 10 | `python build/verifier-piece.py` | **`1`** | `2 divergence(s) sur 50 pièce(s)` (`ch. 14` l. 677, `ch. 37` l. 740) | **FAIL (`A-B1`)** |
| 11 | `python build/verifier-piece-mutations.py` | **`1`** | `ÉCHEC — le temps 1 doit passer avant de muter.` (sortie 1) | **FAIL (`A-B1`)** |
| 12 | `python build/assemble-bibliographie.py --verifier` | `0` | `OK — 1154 entrées uniques, 109 doublons fondus.` | **PASS** |
| 13 | `python figures/genere.py --verifier` | `0` | `[figures] 118 figures du volume : 115 gravées sur 49 pièces, 3 antérieures vérifiées à l'empreinte` | **PASS** |
| 14 | `python ../Python/check-renvois.py` & `check-lisibilite.py` & `check-resume.py Compendium.pdf` | `0` | `0 renvoi mort` ; `18 pages d'accueil OK` ; `degagement +21.5 pt [OK]` | **PASS** |

### 1.2 Analyse détaillée des défaillances et bogues d'outillage

#### Constat `A-B1` (Bloquant) — Échec de `build/verifier-piece.py` et `build/verifier-piece-mutations.py` (code 1) sur 2 pièces HTML
- **Preuve (`[R]`, `[L]`)** : L'exécution de `python build/verifier-piece.py` retourne le code `1` avec deux écarts :
  1. [`Livre II/14-grille-cinq-questions.html`](Livre%20II/14-grille-cinq-questions.html#L677) (`Tableau 14.2`, l. 677) : le fichier `.html` commité contient `<table style="width:100%;">` suivi de 6 colonnes `<col style="width: 16%" />`, tandis que la régénération par [`build/rendre-piece.py`](build/rendre-piece.py#L46-L62) sous Pandoc `3.12.1` produit `<table style="width:99%;">`.
  2. [`Livre IV/37-maillage-agents-point-application.html`](Livre%20IV/37-maillage-agents-point-application.html#L740) (`Tableau 37.2`, l. 740) : même écart exact (`<table style="width:100%;">` dans le fichier commité le 15 septembre 2026 lors du commit `8e2feab`, contre `<table style="width:99%;">` à la vérification).
- **Cause racine** : Dans [`Livre II/14-grille-cinq-questions.md`](Livre%20II\14-grille-cinq-questions.md) et [`Livre IV/37-maillage-agents-point-application.md`](Livre%20IV\37-maillage-agents-point-application.md), les tableaux `14.2` et `37.2` sont les deux seuls tableaux à **6 colonnes** du volume dont la ligne de séparation Markdown (`| :--- | ... |`) dépasse la largeur par défaut de 72 colonnes de Pandoc (`--columns=72`). Pandoc convertit alors la table en `pipe_table` à largeurs relatives (`6 × 16 % = 96 %`, arrondi à `width:99%` par Pandoc `3.12.1` contre `width:100%` par Pandoc `3.1.11`). Par répercussion, [`build/verifier-piece-mutations.py`](build/verifier-piece-mutations.py) échoue dès son Temps 1.
- **Correctif** : Ajouter `"--columns=1000"` à l'invocation de `pandoc` dans [`build/rendre-piece.py`](build/rendre-piece.py#L48), puis régénérer les 50 `.html`.

#### Constat `A-B2` (Bloquant) — Échec de `bash PRD/decompte.sh --verifier` sans `LC_ALL=C`
- **Preuve (`[R]`, `[L]`)** : La page d'accueil [`2 - Compendium/README.md`](README.md) prescrit d'exécuter `bash PRD/decompte.sh --verifier`. Rejouée telle quelle sous l'environnement standard (`fr_CA.UTF-8` / `C.UTF-8`), la commande échoue (`code 1`) :
  `ÉCART Vol. I wc -w brut : 241260 (attendu 233257)`.
- **Cause racine** : Dans [`PRD/decompte.sh`](PRD/decompte.sh#L37), la fonction `jetons()` fixe explicitement `LC_ALL=C.UTF-8`, mais la ligne 70 (`v1_brut=$(wc -w < "$VOL1" | tr -d ' ')`) exécute `wc -w` sous la locale de l'appelant. Or le Volume I contient des milliers d'espaces insécables (`U+00A0`) : en locale UTF-8, `wc -w` traite `U+00A0` comme un séparateur de mots (`241 260`), alors que la valeur de référence `233 257` a été enregistrée sous `LC_ALL=C` (où `0xC2 0xA0` n'est pas un espace ASCII).
- **Correctif** : Préfixer la ligne 70 de [`PRD/decompte.sh`](PRD/decompte.sh#L70) par `LC_ALL=C` (`v1_brut=$(LC_ALL=C wc -w < "$VOL1" | tr -d ' ')`).

#### Constat `A-M1` (Majeur) — Désynchronisation généralisée des décomptes et double pourcentage hybride dans l'« En-tête de rédaction » des 50 chapitres
- **Preuve (`[L]`)** : Chaque chapitre comporte deux blocs de métadonnées : un `En-tête résumé` de 5 lignes en tête de fichier (ajouté le 15 septembre 2026, `T4.3`) et un `### En-tête de rédaction` complet en fin de note de statut. Lors des passes des 2 et 15 septembre 2026, [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py) a mis à jour le bandeau supérieur mais a corrompu ou omis de mettre à jour la ligne `Volumétrie :` de l'en-tête inférieur dans la quasi-totalité des chapitres :
  - **Double pourcentage hybride dans 40 chapitres sur 50** (ex. ch. 1 à 9, 11, 12 à 21, 22 à 30, 32 à 34, 36, etc.) : la regex de `reporter-volumetrie.py` a remplacé l'ancien nombre de mots par celui du 2 septembre 2026 tout en laissant subsister entre parenthèses **l'ancien pourcentage d'écart du 28 juillet 2026** ! Exemples flagrants :
    - [`Livre I/09-orchestration-multi-agents.md`](Livre%20I\09-decouverte-registres-pile.md) : l'en-tête supérieur (l. 9) affiche `5 599 mots (cible ≈ 7 000 mots, −20,0 %)`, mais l'en-tête inférieur (l. 761) affiche `5 599 mots de corps (l'en-tête et la présente note de statut exclus), soit −28,0 % sous la cible dérivée de ≈ 7 000 mots (5 041 mots à la dépose du 27 juillet 2026, avant les ajouts de la passe du 30 juillet 2026)` (`−28,0 %` est le ratio de `5 041 / 7 000`, pas de `5 599 / 7 000` !).
    - [`Livre II/16-passeport-identite-agentique.md`](Livre%20II\16-passeport-agent.md) : affiche `5 523 mots (+9,8 % sur la cible dérivée de ≈ 4 500 mots)` alors que `5 523 / 4 500 = +22,7 %` (`+9,8 %` correspondait aux `4 943` mots du 28 juillet).
    - [`Livre II/21-horloge-post-quantique.md`](Livre%20II\21-horloge-post-quantique.md) : affiche `9 724 mots (+55,8 % sur la cible dérivée de ≈ 5 800 mots)` alors que `9 724 / 5 800 = +67,7 %` (`+55,8 %` correspondait aux `9 036` mots du 28 juillet).
  - **Ancien nombre de mots du 2 septembre 2026 (avant l'insertion des figures SVG du 15 septembre) laissé intact dans l'en-tête inférieur de 5 chapitres** :
    - [`ch. 10`](Livre%20I\10-transaction-infrastructure.md) : `7 548 mots (+7,8 %)` en bas vs `7 584 mots (+8,3 %)` en haut.
    - [`ch. 31`](Livre%20III\31-vertical-financier-durcisseurs.md) : `9 279 mots (+9,2 %)` en bas vs `9 334 mots (+9,8 %)` en haut.
    - [`ch. 35`](Livre%20III\35-etudes-de-cas-production-canadienne.md) : `9 091 mots (+51,5 %)` en bas vs `9 121 mots (+52,0 %)` en haut.
    - [`ch. 40`](Livre%20IV\40-indicateurs-agentops-finops.md) : `6 075 mots (−6,5 %)` en bas vs `6 105 mots (−6,1 %)` en haut (et omission complète du paragraphe `✎ Renvoi daté, repointé le 15 septembre 2026` en `§ 40.7`).
    - [`ch. 42`](Livre%20IV\42-matrice-protocoles-exigences.md) : `7 089 mots (+1,3 %)` en bas vs `7 110 mots (+1,6 %)` en haut.
- **Cause racine** : [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py) ne vérifie en mode `--verifier` que le bandeau supérieur de 5 lignes, `PRD/README.md` et `README.md`, en ignorant la ligne `Volumétrie :` de l'`### En-tête de rédaction` en fin de pièce.

#### Constat `A-M2` (Majeur) — Troncature des réserves `F-xx` et `§ 8.2` dans la ligne `Garde-fous balayés` de l'en-tête résumé (8 chapitres)
- **Preuve (`[L]`)** : Le générateur de l'en-tête résumé en 5 lignes (15 septembre 2026, `T4.3`) n'a extrait que les identifiants `R-1`..`R-8` et `R-01`..`R-14`, omettant systématiquement les garde-fous de forme `réserve F-01`, `réserve F-06`, `réserve F-09`, `réserve F-25`, `réserve F-37` et `§ 8.2` pourtant déclarés dans l'`### En-tête de rédaction` en fin des mêmes fichiers :
  - **Livre I** : [`ch. 8`](Livre%20I\08-anatomie-mcp-a2a.md) (omet `réserve F-01`, `réserve F-06`), [`ch. 9`](Livre%20I\09-decouverte-registres-pile.md) (omet `réserve F-06`, `réserve F-37`), [`ch. 10`](Livre%20I\10-transaction-infrastructure.md) (omet `réserve F-01`, `réserve F-25`), [`ch. 11`](Livre%20I\11-modes-echec-risques-protocolaires.md) (omet `§ 8.2`, `réserve F-01`).
  - **Livre IV** : [`ch. 39`](Livre%20IV\39-cycle-de-vie-operationnel.md) (omet `réserve F-37`), [`ch. 42`](Livre%20IV\42-matrice-protocoles-exigences.md) (omet `réserve F-09`, `réserve F-01`), [`ch. 43`](Livre%20IV\43-architecture-reference-couches.md) (omet `réserve F-37`, `réserve F-01`), [`ch. 44`](Livre%20IV\44-formalisation-archimate.md) (omet `réserve F-09`, `réserve F-01`).

#### Constat `A-M3` (Majeur) — Bogue de détection des chapitres mixtes dans `PRD/check-compendium.py` (`P3`)
- **Preuve (`[L]`)** : Dans [`PRD/check-compendium.py`](PRD/check-compendium.py#L166-L168), la détection d'un chapitre mixte (combinant les socles des Volumes II et III) est codée ainsi :
  ```python
  has_ii = any("Vol. II" in b for b in vols)
  has_iii = any("Vol. III" in b for b in vols)
  ```
  Comme la chaîne `"Vol. II"` est un préfixe strict de `"Vol. III"`, `has_ii` vaut **`True`** dès que `has_iii` vaut `True` ! Ce bogue, déjà signalé dans la note de statut du [`ch. 18 § 18.8`](Livre%20II\18-know-your-agent.md) pour le TOC, n'a jamais été corrigé dans `check-compendium.py`.
- **Correctif** : Remplacer `"Vol. II" in b` par `re.search(r"Vol\.\s+II(?!I)", b)`.

#### Constat `A-M4` (Majeur) — Sixième recomposition de `Compendium.pdf` (15 sept. 2026) non documentée dans `JOURNAL.md` et `PRD.md`, foliotage à `6,0 mm` et tension `D-10` vs `D-18`
- **Preuve (`[L]`, `[R]`)** :
  1. **Recomposition silencieuse du 15 septembre 2026** : Le commit `fc33db1` (15 septembre 2026) a abaissé dans [`build/compendium.template`](build/compendium.template#L70-L71) le pas de grille de `PAS = 16.80pt` à **`PAS = 16.675pt`** (et `INTER = 7.59pt`) pour absorber les 115 figures SVG nouvellement gravées tout en maintenant [`Compendium.pdf`](Compendium.pdf) à exactement **1 000 pages** (`13 022 826` octets). Or ni [`JOURNAL.md`](JOURNAL.md) ni [`PRD/PRD.md`](PRD/PRD.md) (§ 14.3 et § 18.2) n'enregistrent cette sixième recomposition : tous deux décrivent encore la 5e recomposition du 2 septembre 2026 (`PAS = 16.80pt`, `13 177 629` octets).
  2. **Foliotage et titres courants sous le seuil d'impression physique (`6,0 mm < 6,35 mm`)** : Dans [`build/compendium.template`](build/compendium.template#L64-L82), `M_HAUT = 18mm`, `M_BAS = 18mm`, `header-ascent: 12mm` et `footer-descent: 12mm` placent le titre courant et le folio à exactement **`6,0 mm`** du bord physique de la feuille (`6,5 × 9,25 po`), soit sous la marge non imprimable standard des presses (`0,25 po = 6,35 mm`).
  3. **Tension non résolue entre `D-10` et `D-18` sur la page de titre et le colophon** : Le commentaire des lignes 585–587 de [`build/compendium.template`](build/compendium.template#L585-L587) documente ouvertement le compromis du 15 septembre 2026 (`M7b`) : un bandeau `D-18` a été inséré en tête de la table des matières (p. `i`) et sous chaque titre de chapitre (`#let statut`), mais la page de titre (p. `I`) et le colophon final (l. 567–571) restent dépourvus de toute mention d'archive non publiable par fidélité à la décision `D-10` du 30 juillet 2026 (`PRD.md` § 15.4).

#### Constat `A-m1` (Mineur) — Gabarit `build/echantillon.template` figé au 31 juillet 2026
- **Preuve (`[L]`)** : [`build/echantillon.template`](build/echantillon.template) n'a reçu aucune des mises à jour typographiques des 9 août, 2 septembre et 15 septembre 2026 (`M_HAUT = 24mm` au lieu de `18mm`, `PAS = 17pt`, macro `#let figure-svg(chemin)` à 1 seul argument incompatible avec les appels à 2 arguments générés par `assemble.py`, absence de `#let statut(body)`).

---

## 2. Audit de la gouvernance, du plan et du socle documentaire (`PRD/`, `annexe-*.md`)

### 2.1 État des portes `G-1` à `G-7`, des décisions `D-1` à `D-19` et des critères `CA-IV-01` à `CA-IV-14`

L'architecture de gouvernance du *Compendium* repose sur 7 portes (`G-1` à `G-7`), 19 décisions du dépositaire (`D-1` à `D-19`) et 14 critères d'acceptation (`CA-IV-01` à `CA-IV-14`). L'audit complet de [`PRD/PRD.md`](PRD/PRD.md) (v0.20) établit qu'au 14 octobre 2026 :
- **Portes franchies (partiellement ou complètement)** : `G-1` (franchie sur les 123 entrées initiales le 28 juillet 2026, mais **volet résiduel sur les chapitres des Livres III et IV non exécuté**), `G-2` (franchie le 28 juillet 2026 par `socle-consolide.md` v1.0), `G-3` (franchie le 28 juillet 2026 en v0.28 du TOC), `G-4` (volet de forme franchi en v0.30, mais **volet de fond non franchi** : le Volume III reste « rédigé non publiable » avec 6 remontées ouvertes `R-G-48`, `R-G-49`, `R-G-50`, `R-G-52`, `R-G-55`, `R-G-57`).
- **Portes non franchies** : **`G-5`** (balayage du Livre IV pour déclarer le risque 14 / couche d'exécution non comblé après `D-2`), **`G-6`** (clôture des lots de matière neuve des ch. 41, 47 et 48 sous `D-3` et `D-8`), **`G-7`** (vérification finale avant publication : `CA-IV-01` à `CA-IV-14`).
- **Bilan exact des 14 critères d'acceptation (`CA-IV-01` à `CA-IV-14`) au 14 octobre 2026** :
  - **4 critères pleinement satisfaits** : `CA-IV-02` (qualification systématique des `Lecture de l'auteur`), `CA-IV-03` (0 dette de vote adversarial dans les 159 `S-nnn`, mais 23 citations résiduelles de `F-92`/`F-96`/`H-15` signalées par `P4`), `CA-IV-08` (registre de gel au ch. 50), `CA-IV-14` (parité des 56 thèses entre `TOC.md` v0.36 et les 50 chapitres, à la réserve de la citation anonymisée du ch. 8 `A-M8`).
  - **2 critères partiellement satisfaits** : `CA-IV-06` (volumétrie globale à `−3,2 %` dans `± 15 %`, mais 23 chapitres sur 50 hors de la tolérance individuelle de `± 15 %` de leur cible dérivée), `CA-IV-07` (les 26 sièges passent `S1`–`S5`, mais 2 « sièges de fait » invoqués dans la prose du Livre IV — `ch. 38 § 38.4` et `ch. 39 § 39.2.3` — ne sont pas inscrits dans `check-sieges.py`).
  - **8 critères non satisfaits** : **`CA-IV-01`** (ré-adossement aux `S-nnn` écarté par `D-16`), **`CA-IV-04`** (revalidation de moins de 30 jours **expirée le 2 octobre 2026**), **`CA-IV-05`** (clôture du Vol. III non exécutée), **`CA-IV-09`** (5 lots du ch. 41 non ouverts), **`CA-IV-10`** (lots `L1`–`L3` des ch. 47–48 non clos), **`CA-IV-11`** (pas de relecture tierce sur la dualité défensive/offensive des ch. 19–20), **`CA-IV-12`** (blueprint du ch. 45 auto-vérifié sans tiers et bloqué par `R-IV-101`), **`CA-IV-13`** (homogénéité terminologique et stylistique incomplète : survivance des périphrases de la décision 15 et des préfixes `Vol. II/III F-xx`).

### 2.2 Anomalies dans les pièces de gouvernance et les annexes

#### Constat `A-M5` (Majeur) — Cardinaux de mutations, version du TOC et liste des chapitres « hors corpus bibliographique » périmés dans `PRD/PRD.md` v0.20
- **Preuve (`[L]`, `[R]`)** :
  1. **Cardinaux des harnais de mutations (§ 9, l. 221–246 et § 18.3, l. 634)** : [`PRD/PRD.md`](PRD/PRD.md) déclare encore **`24`** mutations pour `check-toc-mutations.py`, **`114`** pour `check-sieges-mutations.py`, **`23`** pour `check-compendium-mutations.py` et **`6`** pour `verifier-piece-mutations.py`, alors que le commit `fc33db1` du 15 septembre 2026 les a portées respectivement à **`25`**, **`115`**, **`30`** et **`8`** (total de **178 mutations** contre 167 affichées dans `PRD.md`).
  2. **Version courante du TOC (§ 6, l. 73)** : [`PRD/PRD.md`](PRD/PRD.md) écrit encore *« la version courante étant la v0.32 au 8 août 2026 »*, alors que [`PRD/TOC.md`](PRD/TOC.md) est en **v0.36** (2 septembre 2026).
  3. **Omission du chapitre 31 dans la liste des chapitres portant les affirmations « hors corpus bibliographique » (§ 7.1, l. 117)** : [`PRD/PRD.md`](PRD/PRD.md) affirme que les 12 occurrences du Volume I ch. 5 déclarées « hors corpus bibliographique du chapitre, à sourcer à la rédaction » atterrissent uniquement dans les **chapitres 30, 34 et 36** (`R-IV-97`). Or la vérification intégrale du Livre III (`[L]`) montre que le **[`chapitre 31 (§ 31.3.2)`](Livre%20III\31-vertical-financier-durcisseurs.md)** porte lui aussi l'une de ces 12 occurrences (sur la règle SEC 17a-4 / stockage WORM) et le déclare dans son en-tête de rédaction (l. 1106).

#### Constat `A-M6` (Majeur) — Désynchronisation entre `PRD/socle-consolide.md` v1.2 et `annexe-references.md` sur quatre entrées (`S-001`, `S-027`, `S-032`, `S-131`)
- **Preuve (`[L]`)** : Lors de la passe du 2 septembre 2026 (`D-16`), [`PRD/socle-consolide.md`](PRD/socle-consolide.md) a été porté en v1.2 pour acter les changements de `revalidation-2026-09-02.md`, mais [`annexe-references.md`](annexe-references.md) n'a pas été resynchronisée sur quatre entrées :
  1. **`S-001`** ([`annexe-references.md`](annexe-references.md) vs [`socle-consolide.md`](PRD/socle-consolide.md)) : l'annexe donne encore l'état gelé au 27 juillet 2026 (`dernière version numérotée antérieure : 2025-11-25`) sans la mise à jour du 2 septembre 2026 (`changement partiel — billet d'étape SEPs du 2026-07-28`).
  2. **`S-027`** ([`annexe-references.md`](annexe-references.md) vs [`socle-consolide.md`](PRD/socle-consolide.md)) : l'annexe omet l'entrée en vigueur effective du *By-law no 10* (DORS/2026-133) le 24 août 2026 et l'ouverture de la consultation de 30 jours.
  3. **`S-032`** ([`annexe-references.md`](annexe-references.md) vs [`socle-consolide.md`](PRD/socle-consolide.md)) : l'annexe écrit encore `période de commentaires de 30 jours ouverte jusqu'au 26 août 2026` au lieu d'acter sa clôture le 26 août 2026 sans publication en Partie II de la *Gazette du Canada*.
  4. **`S-131`** ([`annexe-references.md`](annexe-references.md) vs [`socle-consolide.md`](PRD/socle-consolide.md)) : l'annexe ne mentionne pas la dépréciation de LangGraph v0.x et la publication de v1.0 actées le 2 septembre 2026.

#### Constats `A-m2` et `A-m3` (Mineurs) — En-têtes `TOC v0.35` et renvois résiduels aux pièces hors domaine (`avant-propos`, Annexes C/E/F/H)
- **Preuve (`[L]`)** :
  - `A-m2` : [`PRD/registre-gel.md`](PRD/registre-gel.md) et [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) mentionnent encore `TOC.md v0.35` au lieu de `v0.36`.
  - `A-m3` : Bien que la décision 26 du 2 septembre 2026 ait retiré `avant-propos.md` et les `Annexes A à H` du domaine de livraison, deux chapitres renvoient encore le lecteur à l'avant-propos sans note corrective : [`ch. 1 § 1.0.2`](Livre%20I\01-interoperabilite-integration-entreprise.md) (*« le contrat de lecture posé par l'avant-propos »*) et [`ch. 31`](Livre%20III\31-vertical-financier-durcisseurs.md) (*« L'avant-propos de la somme et l'ouverture du premier chapitre ont posé le principe »*). De même, les corps des ch. 43, 45, 49 et 50 contiennent encore des renvois vers les `Annexes C, E, F, H`, neutralisés uniquement par un avertissement générique en fin de pièce.

---

## 3. Audit de péremption calendaire et confrontation aux sources primaires externes (`[S]`) au 14 octobre 2026

### 3.1 Expiration de la fenêtre de 30 jours de `CA-IV-04` (`A-B3`)

Le critère d'acceptation [`CA-IV-04`](PRD/PRD.md) et le protocole du [`chapitre 50 (§ 50.3)`](Livre%20V\50-peremption-protocole-revalidation.md) stipulent qu'*« aucun chapitre à haute sensibilité temporelle (signalé comme tel dans son en-tête du plan) n'est publié sans une passe de revalidation datée de moins de trente jours »*. La pièce [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) (§ 6.1) énonçait en conséquence :
> *« La présente passe, datée du **2 septembre 2026**, vaut donc pour une publication antérieure au **2 octobre 2026** sur le périmètre qu'elle couvre. »*

Au **14 octobre 2026** (+42 jours depuis le 2 septembre 2026, soit **12 jours après l'expiration du 2 octobre 2026**), **la validité temporelle de la passe du 2 septembre 2026 est intégralement échue** : 0 chapitre sur les 21 chapitres à haute sensibilité temporelle ne satisfait plus `CA-IV-04`.

### 3.2 Faille méthodologique de `revalidation-2026-09-02.md` sur les brouillons IETF et état réel sur le Datatracker (`A-B4`, `[S]`)

L'audit du script implicite et du tableau de [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) révèle un **vice méthodologique critique** : pour vérifier le 2 septembre 2026 si les brouillons IETF (`S-083`, `S-084`, `S-085`) avaient évolué depuis le 27 juillet 2026, la passe a interrogé les **URL d'archive figées à la révision `-00`** (`https://www.ietf.org/archive/id/draft-klrc-aiagent-auth-00.txt`, etc.). Or, sur l'infrastructure de l'IETF, une URL `/archive/id/draft-...-00.txt` est une archive historique immuable qui renvoie `HTTP 200` à perpétuité, même lorsque le brouillon a connu trois révisions, a été adopté par un groupe de travail ou a changé de nom !

La confrontation directe aux pages `https://datatracker.ietf.org/doc/...` le 14 octobre 2026 (`[S]`) révèle cinq écarts factuels majeurs :

| Brouillon / Identifiant | État déclaré dans le *Compendium* (`corpus-v1.0`) | État réel vérifié sur le Datatracker IETF au 14 oct. 2026 (`[S]`) | Impact sur le *Compendium* |
| :--- | :--- | :--- | :--- |
| **`draft-klrc-aiagent-auth`** (`S-085`, `ch. 18 § 18.1`, `ch. 50` Évén. 10) | Cité en révision **`-00`** (26 mars 2026), *« aucun groupe de travail rattaché »*, échéance au **27 septembre 2026** ; déclaré **`INCHANGÉ`** le 2 sept. 2026 | Passé en **`-01`**, **`-02`**, puis **`-03`** dès le **6 juillet 2026** (avant même le gel du 27 juillet !) ; **adopté par le WG IETF WIMSE le 9 septembre 2026** ; **remplacé par `draft-ietf-wimse-aims-00`** (*AI Identity Management System*) publié le **15 septembre 2026** (échéance 19 mars 2027) | **Faux négatif majeur dès le gel initial et lors du 2 sept. 2026** : la thèse du ch. 18 selon laquelle ce brouillon individuel n'est rattaché à aucun WG est **réfutée depuis les 9–15 septembre 2026** |
| **`draft-ietf-oauth-v2-1`** (`ch. 3 § 3.2.1`, `R-IV-04`) | Le corps cite **`draft-ietf-oauth-v2-1-15`** (échéance **3 septembre 2026**) ; une note du 2 sept. 2026 dit qu'il a été renouvelé avant échéance sans donner le nouveau numéro | **`draft-ietf-oauth-v2-1-16`** publié le **2 septembre 2026** (193 pages, actif ; jalon du WG OAuth : `Dec 2026 — Submit OAuth 2.1 to IESG for publication as Proposed Standard`) | Le corps du [`ch. 3 § 3.2.1`](Livre%20I\03-securite-identite-gouvernance.md) cite toujours la révision `-15` expirée le 3 septembre 2026 |
| **`draft-klrc-wimse-ai-agents-00`** (`ch. 12 § 12.5` l. 280, `TOC.md` l. 877) | Cité en révision **`-00`** (publiée le 28 février 2026, expiration le **1er septembre 2026**) ; omis du `Tableau 50.1` et de `revalidation-2026-09-02.md` | **Expiré le 1er septembre 2026** (depuis **43 jours** au 14 octobre 2026), non renouvelé sous ce nom (absorbé dans le chantier WIMSE AIMS) | Brouillon cité au présent au [`ch. 12 § 12.5`](Livre%20II\12-heritage-standards-etires.md) alors qu'il était déjà expiré la veille de la passe du 2 septembre 2026 |
| **`draft-ietf-wimse-workload-creds`** (`S-084`, `ch. 13`, `ch. 50` Évén. 9) | Cité en révision **`-00`** (17 avril 2026, échéance **19 octobre 2026**, soit à J+5 du 14 oct.) ; déclaré **`INCHANGÉ`** le 2 sept. 2026 sur l'URL `-00.txt` | Révision **`-01`** publiée fin juin / juillet 2026 (repoussant l'échéance à décembre 2026 / janvier 2027), en cours de convergence avec `RFC 9334` (RATS) au sein du WG WIMSE | Échéance du 19 octobre 2026 inscrite au `Tableau 50.1` (Événement 9) caduque faute d'avoir interrogé le Datatracker |
| **`draft-drake-agent-identity-registry-03`** (`ch. 18 Tableau 18.1`, `ch. 50` Évén. 10) | Cité en révision **`-03`** (23 mai 2026, échéance **24 novembre 2026**) ; revalidé le 2 sept. 2026 | Toujours en **`-03`** (individuel), arrive à expiration dans **41 jours** (le 24 novembre 2026) | Surveillance active requise avant le 24 novembre 2026 ; contradiction interne à la ligne 10 du `Tableau 50.1` (`A-M11`) |

### 3.3 Entrée dans le `T4 2026` du RTR (1er octobre 2026) et contradiction frontale entre les chapitres 33 et 36 (`A-B5`, `[S]`)

- **Ouverture effective de la fenêtre cible du `T4 2026`** : Depuis le **1er octobre 2026**, le calendrier se situe **à l'intérieur du quatrième trimestre 2026 (`T4 2026`)**, fenêtre cible conditionnelle d'entrée en service et de reprise des essais sectoriels du système de paiement en temps réel (**RTR**) de Paiements Canada (`S-027` / `F-29`). En conséquence :
  1. Le compte à rebours du [`ch. 33 § 33.3`](Livre%20III\33-iso-20022-lynx-rtr.md) (*« Trente-huit jours séparent l'entrée en vigueur du cadre statutaire de l'ouverture de la fenêtre d'essais »* entre le 24 août et le 1er octobre 2026) est désormais **entièrement écoulé**.
  2. La consultation publique de 30 jours ouverte par Paiements Canada le 24 août 2026 sur les règles d'accès élargi est **close depuis le ~23 septembre 2026**.
- **Contradiction interne directe entre le chapitre 33 et le chapitre 36** : Lors de la passe du 2 septembre 2026 (`D-16`), le [`chapitre 33 (§ 33.3)`](Livre%20III\33-iso-20022-lynx-rtr.md) et le [`chapitre 50 (Tableau 50.1, Événement 2)`](Livre%20V\50-peremption-protocole-revalidation.md) ont été mis à jour pour acter que le *By-law no 10* (`DORS/2026-133`) est **entré en vigueur le 24 août 2026**. En revanche, le [`chapitre 36 (§ 36.2.7, l. 305)`](Livre%20III\36-prospective-ap2-rails-canadiens.md) a été oublié et affirme toujours au futur :
  > *« Le règlement administratif correspondant — le By-law no 10 — a été enregistré sous la référence DORS/2026-133 et **doit entrer en vigueur le 24 août 2026**. »*

### 3.4 État au 14 octobre 2026 des 14 événements de péremption du `Tableau 50.1` et des échéances connexes (`A-M7`, `[S]`)

| Évén. (`Tableau 50.1`) | Horizon déclaré au Compendium | État dans `corpus-v1.0` (2 / 15 sept. 2026) | État réel vérifié au 14 octobre 2026 (`[S]`) |
| :---: | :--- | :--- | :--- |
| **1. BSIF E-23 & AMF LD IA** (`S-009`, `S-023`) | **1er mai 2027** (`PROGRAMMÉ`) | Compte à rebours figé dans le texte à **« 9 mois et 4 jours (278 jours) »** (ch. 25, 26, 46) ; date AMF laissée à « avril 2026 » (HTTP 403) | Il ne reste plus que **199 jours (6 mois et 17 jours)** avant le 1er mai 2027. La date exacte de publication de la LD IA de l'AMF est confirmée au **7 avril 2026** (`[S]`). |
| **2. RTR — *By-law no 10* et `T4 2026`** (`S-027`, `F-29`) | **24 août 2026** / **`T4 2026`** | Entrée en vigueur du 24 août actée au ch. 33 (mais oubliée au ch. 36 l. 305) ; `T4 2026` traité au futur | **Nous sommes dans le `T4 2026` depuis 14 jours** ; la consultation de 30 jours ouverte le 24 août est close depuis le ~23 septembre 2026 (`A-B5`). |
| **3. Cadre bancaire canadien (C-15 / L.C. 2026, ch. 6)** (`S-032`, `S-033`) | **Fin août 2026** (consultation) / **2026-2027** | Clôture des commentaires le 26 août 2026 actée au ch. 32 ; absence d'organisme de normalisation technique vérifiée | Toujours en attente de publication finale en Partie II de la *Gazette du Canada* au 14 octobre 2026 ; aucune désignation d'organisme technique (`[S]`). |
| **4. *Digital Omnibus on AI* `COM(2025) 836`** (`ch. 30`) | **2 août 2026** / **T3–T4 2026** | Resté en `[C]` non revalidé ; le ch. 30 l. 105 écrit encore *« entre en vigueur à partir du 2 août 2026 »* | La date du **2 août 2026** est dépassée de 73 jours ; les négociations de trilogue sur le report des systèmes à haut risque (déc. 2027 / août 2028) se poursuivent au T4 2026 (`[S]`). |
| **5. PQC — `NIST IR 8547` & `ITSM.40.001`** (`S-096`..`S-098`) | **2026–2029** (`PROJETÉ`) | `NIST IR 8547` toujours en *Initial Public Draft* au 2 sept. 2026 | Toujours en *Initial Public Draft* au 14 oct. 2026 ; mais l'échéance à **+90 jours** (20 sept. 2026) des directives OMB sous l'EO 14412 (`S-107`, ch. 21) est **dépassée de 24 jours** (`[S]`). |
| **6. MCP — feuille de route** (`S-001`..`S-003`) | **Continu 2026–2027** | Billet SEPs du `2026-07-28` acté en note (ch. 3, 6, 8) sans refonte du corps | Spécification stable toujours millésimée `2025-11-25` ; travaux SEPs 2026 en cours sur les flux asynchrones, `.well-known` et la gouvernance (`[S]`). |
| **7. A2A — v0.3 → v1.0** (`S-004`, `S-005`) | **Continu 2026–2027** | Déclaré inchangé au 2 sept. 2026 (`v0.3.0` + jalon RC v1.0) | Toujours en lignée `v0.3.x` / RC `v1.0` sous gouvernance Linux Foundation au 14 octobre 2026 (`[S]`). |
| **8. OpenTelemetry GenAI** (`S-121`..`S-124`) | **Continu 2026–2027** | Toujours `Development` au 2 sept. 2026 | Toujours au statut `Development` (versions `v1.37`–`v1.40`) au 14 octobre 2026 (`[S]`). |
| **9. `draft-ietf-wimse-workload-creds`** (`S-084`) | **19 octobre 2026** (`PROGRAMMÉ`) | Déclaré `INCHANGÉ` en `-00` sur l'URL d'archive | L'échéance du `-00` (19 oct. 2026) est à **J+5**, mais la révision **`-01`** a déjà pris le relais sur le Datatracker (`A-B4`, `[S]`). |
| **10. 3 brouillons d'identité d'agent** (`S-085`, `ch. 18`) | **27 sept. 2026**, **24 nov. 2026**, **15 janv. 2027** | `draft-sharif-01` mis à jour (27 févr. 2027), mais `draft-klrc-aiagent-auth-00` laissé au 27 sept. 2026 | **Échéance du 27 sept. 2026 dépassée** ; `draft-klrc-aiagent-auth` est devenu **`draft-ietf-wimse-aims-00`** (WG WIMSE) dès le 15 sept. 2026 (`A-B4`, `[S]`). |
| **11. Cinquième horloge — harnais d'exécution** (`D-2`) | **2026–2027** (`SPÉCULATIF`) | Lots `J-IV-6` / `J-IV-7` non exécutés | Toujours non instruit au socle consolidé. |
| **12. Six cadriciels d'orchestration** (`S-012`, `S-030`, `S-031`, `S-116`, `S-130`, `S-131`) | **Continu 2026–2027** | LangGraph `v1.0` et `agentgateway v1.4.0` actés en note, mais corps des ch. 23, 37 et 39 non mis à jour | Coexistence contradictoire entre le corps (« pré-version ») et les notes de re-datation (`v1.4.0` / `v1.0`) aux ch. 23, 37 et 39 (`A-M10`). |
| **13. Vide fédéral canadien C-27 → C-36** (`ch. 26`) | **2026–2027** (`PROJETÉ`) | Non re-vérifié le 2 sept. 2026 (`RA-R2`) | Projet de loi C-36 toujours en examen parlementaire sans sanction royale ni entrée en vigueur au 14 octobre 2026 (`[S]`). |
| **14. Avis ACVM 11-348** (`ch. 28`) | **2026–2028** (`SPÉCULATIF`) | Non extrait en source primaire (`[C]`, `RA-R2`) | Aucun règlement contraignant n'a remplacé l'Avis 11-348 au 14 octobre 2026 (`[S]`). |

À ces 14 événements s'ajoute le **seuil d'obsolescence trimestriel (90 jours)** auto-déclaré par le [`chapitre 35 (§ 35.10, l. 852)`](Livre%20III\35-etudes-de-cas-production-canadienne.md) pour les dix études de cas d'institutions financières canadiennes (collectées les 16–17 juillet 2026) : ce seuil de 90 jours est **atteint exactement le 14 octobre 2026**.

---

## 4. Audit analytique et contradictoire Livre par Livre et Chapitre par Chapitre (`[L]`)

### 4.1 Livre I — *Fondations protocolaires et d'intégration* (Chapitres 1 à 11)

#### 4.1.1 Tableau métrique et structurel des chapitres 1 à 11 (`[L]`)

| Ch. | Fichier | Mots corps | Cible | Écart | `§` / `###` | Tab. | Fig. SVG | `Lecture` (corps/tot.) | Remontées `R-IV-*` | Sièges posés |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **1** | [`01-interoperabilite-integration-entreprise.md`](Livre%20I\01-interoperabilite-integration-entreprise.md) | `5 147` | `6 000` | `−14,2 %` | 7 / 13 | 4 | 3 | 12 / 14 | `R-IV-01`, `R-IV-02` | `§ 1.4` (ESB/SOA) |
| **2** | [`02-representation-connaissances-web-semantique.md`](Livre%20I\02-donnees-semantique-ontologies.md) | `6 883` | `7 000` | `−1,7 %` | 10 / 16 | 1 | 3 | 10 / 13 | `R-IV-03` | — |
| **3** | [`03-fondations-protocolaires-web.md`](Livre%20I\03-securite-identite-gouvernance.md) | `6 878` | `6 000` | `+14,6 %` | 7 / 25 | 2 | 2 | 12 / 14 | `R-IV-04` | — |
| **4** | [`04-architectures-evenementielles-agents.md`](Livre%20I\04-ingenierie-systemes-agentiques.md) | `6 600` | `6 000` | `+10,0 %` | 9 / 21 | 2 | 2 | 23 / 24 | `R-IV-05`, `R-IV-06` | — |
| **5** | [`05-ingenierie-contexte.md`](Livre%20I\05-ancrage-informationnel.md) | `6 123` | `6 500` | `−5,8 %` | 9 / 17 | 4 | 2 | 17 / 22 | `R-IV-07`, `R-IV-08` | `§ 5.3` (chiffres empiriques) |
| **6** | [`06-model-context-protocol.md`](Livre%20I\06-multi-agents-evaluation-surete.md) | `7 338` | `8 000` | `−8,3 %` | 12 / 22 | 3 | 3 | 12 / 14 | — | `§ 6.1` (architecture MCP) |
| **7** | [`07-agent-to-agent.md`](Livre%20I\07-genealogie-gouvernance.md) | `7 444` | `8 000` | `−7,0 %` | 11 / 25 | 2 | 3 | 14 / 16 | `R-IV-09`, `R-IV-10` | `§ 7.1` (A2A), `§ 7.5` (quatre états) |
| **8** | [`08-anatomie-mcp-a2a.md`](Livre%20I\08-anatomie-mcp-a2a.md) | `7 464` | `8 500` | `−12,2 %` | 9 / 18 | 6 | 2 (`+3` ant.) | 22 / 25 | — | `§ 8.1` (11 dimensions) |
| **9** | [`09-orchestration-multi-agents.md`](Livre%20I\09-decouverte-registres-pile.md) | `5 599` | `7 000` | `−20,0 %` | 8 / 12 | 4 | 2 | 20 / 22 | `R-IV-11` | — |
| **10** | [`10-protocoles-emergents-convergence.md`](Livre%20I\10-transaction-infrastructure.md) | `7 584` | `7 000` | `+8,3 %` | 11 / 17 | 6 | 1 | 15 / 17 | `R-IV-12` | — |
| **11** | [`11-modes-echec-risques-protocolaires.md`](Livre%20I\11-modes-echec-risques-protocolaires.md) | `6 195` | `6 500` | `−4,7 %` | 9 / 14 | 1 | 2 | 12 / 14 | `R-IV-13` | `§ 11.2` (Promptware Kill Chain) |
| **Tot.** | **Livre I (11 chapitres)** | **`73 255`** | **`76 500`** | **`−4,2 %`** | **102 / 200** | **35** | **25 (+3)** | **169 / 195** | **`R-IV-01` à `13`** | **7 sièges** |

#### 4.1.2 Constats spécifiques au Livre I

1. **Constat `A-M8` (Majeur) — Citation non verbatim et anonymisée de la thèse directrice en tête du chapitre 8 contredisant sa propre note de statut** :
   - Dans [`Livre I/08-anatomie-mcp-a2a.md`](Livre%20I\08-anatomie-mcp-a2a.md), la thèse en exergue écrit :
     *« La formule "dans les agents, entre les agents" — doctrine de complémentarité déclarée par l'un des deux projets — [...] »* (en anonymisant `MCP` et `A2A`), alors que [`PRD/TOC.md`](PRD/TOC.md) écrit : *« La formule "MCP dans les agents, A2A entre les agents" — doctrine de complémentarité déclarée par le projet A2A — [...] »*, et que la note de statut du même chapitre ([`§ 8.8`, l. 882](Livre%20I\08-anatomie-mcp-a2a.md)) affirme pourtant : *« la thèse est citée telle quelle en tête de pièce »* ! (`check-compendium.py` `P2` ne l'a pas détecté car il ne compare que les 60 derniers caractères de la thèse).
2. **Désynchronisation des en-têtes de rédaction (`A-M1` et `A-M2`)** :
   - Les chapitres 1 à 9 et 11 affichent tous en pied de pièce l'ancien pourcentage du 28 juillet 2026 à côté du nombre de mots du 2 septembre 2026 ; le [`chapitre 10`](Livre%20I\10-transaction-infrastructure.md) affiche encore `7 548 mots (+7,8 %)` au lieu de `7 584 mots (+8,3 %)` ; les chapitres 8, 9, 10 et 11 ont leur ligne `Garde-fous balayés` tronquée en tête de fichier.
3. **Survivances d'anonymisation de la décision 15 malgré la décision 18 (`A-m4`)** :
   - Exemples : *« le protocole d'outillage étudié au chapitre suivant »* ([`ch. 5 § 5.5`](Livre%20I\05-ancrage-informationnel.md) pour MCP), *« un protocole voisin à trois primitives »* ([`ch. 7 § 7.3`](Livre%20I\07-genealogie-gouvernance.md) pour MCP), *« un cadre d'analyse de cabinet publié à l'automne 2025 »* ([`ch. 9 § 9.1`](Livre%20I\09-decouverte-registres-pile.md) pour McKinsey/QuantumBlack), *« un grand fournisseur d'infrastructure en nuage »* ([`ch. 10 § 10.6`](Livre%20I\10-transaction-infrastructure.md)), et les *« dix-huit fournisseurs »* tus en [`ch. 11 § 11.7.1`](Livre%20I\11-modes-echec-risques-protocolaires.md).
4. **Coquille typographique mineure au chapitre 3 (`A-m6`)** :
   - Dans [`Livre I/03-fondations-protocolaires-web.md`](Livre%20I\03-securite-identite-gouvernance.md), la citation de la thèse double la ponctuation finale : `JSON-RPC 2.0..*`.

---

### 4.2 Livre II — *Identité, sécurité et confiance* (Chapitres 12 à 21)

#### 4.2.1 Tableau métrique et structurel des chapitres 12 à 21 (`[L]`)

| Ch. | Fichier | Mots corps | Cible | Écart | `§` / `###` | Tab. | Fig. SVG | `Lecture` (corps/tot.) | Remontées `R-IV-*` | Sièges posés |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **12** | [`12-heritage-standards-etires.md`](Livre%20II\12-heritage-standards-etires.md) | `7 972` | `6 500` | `+22,6 %` | 12 / 8 | 2 | 2 | 9 / 11 | `R-IV-14`, `15` | `§ 12.1` (six standards) |
| **13** | [`13-identite-decentralisee-verifiable.md`](Livre%20II\13-identite-decentralisee-vc-did.md) | `5 373` | `5 500` | `−2,3 %` | 8 / 6 | 2 | 2 | 9 / 12 | `R-IV-16` à `18` | `§ 13.4` (asymétrie DID/VC) |
| **14** | [`14-grille-cinq-questions.md`](Livre%20II\14-grille-cinq-questions.md) | `5 408` | `5 000` | `+8,2 %` | 10 / 2 | 4 | 2 | 12 / 17 | `R-IV-19`, `20` | `§ 14.1` (cinq questions) |
| **15** | [`15-cycle-de-vie-delegation-tracabilite.md`](Livre%20II\15-emettre-carte-annuaires-registres.md) | `7 089` | `6 500` | `+9,1 %` | 10 / 4 | 3 | 3 | 12 / 14 | `R-IV-21`, `22` | — |
| **16** | [`16-passeport-identite-agentique.md`](Livre%20II\16-passeport-agent.md) | `5 523` | `4 500` | `+22,7 %` | 9 / 3 | 3* | 2 | 10 / 12 | `R-IV-23` à `25` | `§ 16.1` (passeport 4 pièces) |
| **17** | [`17-delegation-chaine-responsabilite.md`](Livre%20II\17-chaine-mandat-deux-sauts.md) | `6 880` | `5 500` | `+25,1 %` | 10 / 13 | 2 | 2 | 12 / 16 | `R-IV-26` à `29` (`+76`) | `§ 17.5` (coupe-circuit) |
| **18** | [`18-chantiers-normalisation-identite.md`](Livre%20II\18-know-your-agent.md) | `5 322` | `4 800` | `+10,9 %` | 10 / 2 | 3 | 2 | 6 / 10 | `R-IV-30`, `31` | `§ 18.1` (neuf chantiers) |
| **19** | [`19-surface-attaque-agentique.md`](Livre%20II\19-taxonomie-attaques-identite-delegation.md) | `7 781` | `6 500` | `+19,7 %` | 10 / 16 | 2 | 3 | 8 / 11 | `R-IV-32`, `33` | — |
| **20** | [`20-controles-architecture-securitaire.md`](Livre%20II\20-usurpation-revocation-boucle-defensive.md) | `8 318` | `6 500` | `+28,0 %` | 10 / 15 | 2 | 2 | 9 / 11 | `R-IV-34`, `35` | — |
| **21** | [`21-horloge-post-quantique.md`](Livre%20II\21-horloge-post-quantique.md) | `9 724` | `5 800` | `+67,7 %` | 12 / 13 | 4 | 2 | 13 / 16 | `R-IV-36`, `37` | `§ 21.1` (horloge PQC) |
| **Tot.** | **Livre II (10 chapitres)** | **`69 390`** | **`57 100`** | **`+21,5 %`** | **101 / 82** | **27** | **22** | **100 / 130** | **`R-IV-14` à `37`** | **7 sièges** |

*\*Note : le chapitre 16 compte 3 tableaux numérotés `Tableau 16.1`, `Tableau 16.2` et `Tableau 16.2` par suite d'une collision de numérotation (`A-B6.2`).*

#### 4.2.2 Constat `A-B6` (Bloquant) — Cinq contradictions internes majeures introduites au Livre II par la passe d'enrichissement `D-11` du 30 juillet 2026

Lors de la passe du 30 juillet 2026 (`D-11`), des compléments documentaires de première main (`[A]`) ont été greffés dans les chapitres 13, 16, 17, 20 et 21 pour combler des lacunes du Volume III, **mais les sections adjacentes rédigées le 27 juillet 2026 n'ont pas été purgées des constats d'absence qu'elles formulaient**, créant cinq contradictions internes flagrantes :

1. **`A-B6.1` — Chapitre 13 (`§ 13.0` vs `§ 13.1`, `Synthèse` et `§ 13.6`)** :
   - Le [`§ 13.0` (l. 56–103)](Livre%20II\13-identite-decentralisee-vc-did.md), ajouté le 30 juillet 2026, extrait en régime `[A]` la structure technique complète de **W3C Verifiable Credentials Data Model v2.0** (15 mai 2025, `credentialSubject`, `issuer`, `validFrom`/`validUntil`, `credentialStatus` Bitstring Status List, trois mécanismes de sécurisation JOSE / Data Integrity / SD-JWT) et de **W3C Decentralized Identifiers v1.1** (19 mai 2026, syntaxe `did:method:specific-id`, quatre opérations CRUD, résolution en trois temps).
   - Or le [`§ 13.1` (l. 172)](Livre%20II\13-identite-decentralisee-vc-did.md) affirme toujours que le socle *« n'en établit pas davantage la teneur technique »*, la [`Synthèse` (l. 425)](Livre%20II\13-identite-decentralisee-vc-did.md) répète que *« Le contenu technique de W3C DID v1.1 et de W3C VC Data Model 2.0 [...] n'est pas établi par le socle »*, et la note de statut ([`§ 13.6`, l. 492](Livre%20II\13-identite-decentralisee-vc-did.md)) maintient que *« la structure interne d'un document DID et d'une attestation vérifiable VC 2.0 [...] ne sont pas repris »* !
2. **`A-B6.2` — Chapitre 16 (collision de deux `Tableau 16.2`)** :
   - La sous-section [`### 16.1.1` (l. 147)](Livre%20II\16-passeport-agent.md), ajoutée le 30 juillet 2026, introduit un **`Tableau 16.2`** (*Ancrage des quatre pièces du passeport dans les vocabulaires W3C VC 2.0 et DID v1.1*) sans renuméroter le **`Tableau 16.2`** préexistant du [`§ 16.4` (l. 382)](Livre%20II\16-passeport-agent.md) (*Ce que le passeport d'identité agentique apporte aux cinq questions*). Le chapitre 16 comporte ainsi deux tableaux distincts portant le même numéro `Tableau 16.2`.
3. **`A-B6.3` — Chapitre 17 (`§ 17.6.2` : « Trois pistes » qui en comptent quatre)** :
   - Dans [`Livre II/17-delegation-chaine-responsabilite.md`](Livre%20II\17-chaine-mandat-deux-sauts.md), le titre [`### 17.6.2` (l. 483)](Livre%20II\17-chaine-mandat-deux-sauts.md) annonce *« Trois pistes documentées — et pourquoi aucune ne suffit seule »* et le `Tableau 17.2` (l. 557) s'intitule *« Trois pistes documentées pour la chaîne de responsabilité »*. Or la passe du 30 juillet 2026 y a ajouté aux lignes 525–555 une **quatrième piste** (*Une quatrième piste documentée : l'atténuation par caveats — Macaroons, Biscuit et GNAP `RFC 9635`*) ainsi qu'une 4e ligne au `Tableau 17.2`, tandis que le paragraphe de clôture (l. 562) conclut toujours : *« aucune des **trois** n'a été conçue pour répondre... »* !
4. **`A-B6.4` — Chapitre 20 (`§ 20.4` : une 10e rangée appelée « La onzième rangée »)** :
   - Dans [`Livre II/20-controles-architecture-securitaire.md`](Livre%20II\20-usurpation-revocation-boucle-defensive.md), le `Tableau 20.1` comptait initialement **9 rangées** de contrôles (niveaux 1 à 5). La passe du 30 juillet 2026 y a ajouté `RFC 7662` (*OAuth 2.0 Token Introspection*) en **10e rangée** (l. 291), mais le paragraphe de commentaire ajouté aux lignes 328–337 l'appelle **« La onzième rangée »** et évoque **« les dix rangées d'origine »** !
5. **`A-B6.5` — Chapitre 21 (`§ 21.8` vs `§ 21.9` sur la feuille de route canadienne `ITSM.40.001`)** :
   - Le [`§ 21.8` (l. 637–698)](Livre%20II\21-horloge-post-quantique.md), enrichi le 30 juillet 2026, extrait en `[A]` les jalons canadiens du Centre canadien pour la cybersécurité (`ITSM.40.001`, mai 2025 : plans de migration au 1er avril 2026, priorité haute fin 2031, ensemble des systèmes fin 2035) et note explicitement (l. 637) que cet ajout *« renverse une lecture du § 21.9 »*. Mais le [`§ 21.9` (l. 739)](Livre%20II\21-horloge-post-quantique.md) n'a pas été corrigé et affirme toujours : *« Cette lecture se heurte toutefois à une limite du socle : les sources primaires qui établissent l'horloge post-quantique sont exclusivement fédérales américaines [...] Le chapitre ne comble pas la lacune canadienne »* !

---

### 4.3 Livre III — *Orchestration, gouvernance et conformité* (Chapitres 22 à 36)

#### 4.3.1 Tableau métrique et structurel des chapitres 22 à 36 (`[L]`)

| Ch. | Fichier | Mots corps | Cible | Écart | `§` / `###` | Tab. | Fig. SVG | `Lecture` (corps/tot.) | Remontées `R-IV-*` | Sièges posés |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **22** | [`22-options-orchestration-paradigme-apm.md`](Livre%20III\22-options-orchestration-paradigme-apm.md) | `5 590` | `8 500` | `−34,2 %` | 8 / 7 | 4 | 3 | 12 / 16 | `R-IV-76` à `78` | `§ 22.1` (OO1–OO4), `§ 22.2` (APM) |
| **23** | [`23-cadriciels-orchestration-etat-art.md`](Livre%20III\23-frameworks-orchestration-entreprise.md) | `5 376` | `9 500` | `−43,4 %` | 9 / 4 | 2 | 2 | 6 / 9 | `R-IV-79`, `80` | — |
| **24** | [`24-patrons-conception-agentiques.md`](Livre%20III\24-passage-echelle-entreprise.md) | `6 783` | `9 000` | `−24,6 %` | 9 / 17 | 4 | 3 | 16 / 18 | `R-IV-81` à `84` | — |
| **25** | [`25-ligne-directrice-e23-bsif.md`](Livre%20III\25-e23-risque-modele.md) | `6 247` | `7 500` | `−16,7 %` | 9 / 5 | 2 | 3 | 9 / 11 | `R-IV-85` | — |
| **26** | [`26-loi-25-vide-federal-canadien.md`](Livre%20III\26-vide-federal-c27-c36.md) | `5 801` | `8 500` | `−31,8 %` | 8 / 6 | 3 | 3 | 13 / 15 | `R-IV-86`, `87` | — |
| **27** | [`27-ligne-directrice-ia-amf.md`](Livre%20III\27-quebec-amf-article-12-1.md) | `5 829` | `6 500` | `−10,3 %` | 9 / 2 | 4 | 2 | 9 / 12 | `R-IV-88` | — |
| **28** | [`28-avis-11-348-acvm.md`](Livre%20III\28-valeurs-mobilieres-acvm-11-348.md) | `5 696` | `5 500` | `+3,6 %` | 9 / 3 | 3 | **0** | 8 / 11 | `R-IV-89`, `90` | — |
| **29** | [`29-pont-frames-deterministes.md`](Livre%20III\29-pont-frames-deterministes.md) | `7 089` | `6 000` | `+18,2 %` | 6 / 8 | 2 | 3 | 14 / 16 | `R-IV-91` | `§ 29.4.1` (test 3 conditions) |
| **30** | [`30-maillage-reglementaire-normalisation.md`](Livre%20III\30-maillage-reglementaire-normalisation.md) | `7 596` | `8 000` | `−5,0 %` | 8 / 18 | 2 | 2 | 9 / 11 | `R-IV-92`, `93` | — |
| **31** | [`31-vertical-financier-durcisseurs.md`](Livre%20III\31-vertical-financier-durcisseurs.md) | `9 334` | `8 500` | `+9,8 %` | 6 / 16 | 1 | 3 | 23 / 24 | `R-IV-94`, `95` | **6 sièges** (`31.1.1`, `31.1.2`, `31.1.4`, `31.2.6`, `31.3.4`, `31.4.3`) |
| **32** | [`32-cadre-bancaire-consommateur.md`](Livre%20III\32-cadre-bancaire-consommateur.md) | `7 338` | `6 000` | `+22,3 %` | 7 / 7 | 2 | 2 | 12 / 14 | — | — |
| **33** | [`33-iso-20022-lynx-rtr.md`](Livre%20III\33-iso-20022-lynx-rtr.md) | `6 912` | `6 500` | `+6,3 %` | 8 / 6 | 2 | 2 | 11 / 13 | `R-IV-96` | — |
| **34** | [`34-sous-domaines-financiers.md`](Livre%20III\34-sous-domaines-financiers.md) | `7 148` | `8 000` | `−10,6 %` | 7 / 16 | 1 | 2 | 16 / 17 | `R-IV-97` | `§ 34.2.2` (grille P&C) |
| **35** | [`35-etudes-de-cas-canadiennes.md`](Livre%20III\35-etudes-de-cas-production-canadienne.md) | `9 121` | `6 000` | `+52,0 %` | 12 / 16 | 1 | 2 | 6 / 7 | `R-IV-98`, `110`–`112` | — |
| **36** | [`36-prospective-ap2-rails-canadiens.md`](Livre%20III\36-prospective-ap2-rails-canadiens.md) | `7 340` | `6 000` | `+22,3 %` | 7 / 15 | 2 | 3 | 22 / 24 | `R-IV-99` | — |
| **Tot.** | **Livre III (15 chapitres)** | **`103 200`** | **`110 000`** | **`−6,2 %`** | **122 / 146** | **35** | **35** | **186 / 218** | **`R-IV-76` à `99`, `110`–`112`** | **10 sièges** |

#### 4.3.2 Constats spécifiques au Livre III

1. **Constat `A-M9` (Majeur) — Désynchronisation du chapitre 31 sur l'état du contrôle `S5` de trois de ses six sièges** :
   - Le [`chapitre 31`](Livre%20III\31-vertical-financier-durcisseurs.md) pose 6 sièges pour toute la somme. Lors de la passe du 2 septembre 2026 (`D-16`), [`PRD/check-sieges.py`](PRD/check-sieges.py#L228-L273) a **réarmé le contrôle `S5` (renvoi explicite exigé)** sur les trois sièges où il était initialement désactivé (`§ 31.1.1` patron d'irréversibilité, `§ 31.1.2` risque systémique, `§ 31.3.4` principe des quatre-yeux) grâce à des déclencheurs qualifiés.
   - Or le texte du chapitre 31 n'a pas été mis à jour et affirme toujours à quatre endroits ([`§ 31.1.1` l. 66](Livre%20III\31-vertical-financier-durcisseurs.md), [`§ 31.1.2` l. 126](Livre%20III\31-vertical-financier-durcisseurs.md), [`§ 31.3.4` l. 568](Livre%20III\31-vertical-financier-durcisseurs.md) et [`§ 31.6` l. 1041](Livre%20III\31-vertical-financier-durcisseurs.md)) que le contrôle `S5` y est **désactivé** (*« dont le contrôle mécanique de renvoi est désactivé dans le script de vérification »*), contredisant directement [`PRD/check-sieges.py`](PRD/check-sieges.py) !
2. **Infraction nommée à la décision `D-9` sur les chapitres 25 et 27 (`A-D2`)** :
   - La décision `D-9` interdisait de rédiger les sections des chapitres 25 (BSIF E-23) et 27 (AMF LD IA) qui dépendent du lot d'instruction du `§ 17.5` sur le biais d'automatisation avant la clôture de ce lot. Les chapitres 25 et 27 ont néanmoins été rédigés le 28 juillet 2026 alors que le lot était ouvert (infraction actée en `PRD.md` § 8).
3. **Incomplétude de la table de traduction `Tableau 29.1` sous l'article 12.1 de la Loi 25 (`R-IV-91`, condition (d) de `G-3`)** :
   - Dans [`Livre III/29-pont-frames-deterministes.md`](Livre%20III\29-pont-frames-deterministes.md), deux éléments légaux de l'article 12.1 de la Loi 25 — le **droit de rectification** des renseignements utilisés et l'exigence d'un **alinéa distinct** dans la politique de confidentialité — n'ont pas de ligne dans le `Tableau 29.1`, qui ne couvre que 6 obligations sur 8.
4. **Absence d'extraction des textes intégraux au chapitre 36 (`R-IV-99`) et au chapitre 24 (`R-IV-81`)** :
   - Au [`ch. 36 § 36.5`](Livre%20III\36-prospective-ap2-rails-canadiens.md), les quatre préimpressions de la relève `v0.11` (dont *AgentBound*, *SkillFortify*, * Zero-Trust Agentic Packaging*) n'ont été lues qu'à partir de leurs résumés d'indexation ; au [`ch. 24 § 24.8`](Livre%20III\24-passage-echelle-entreprise.md), l'article canonique de Dean & Barroso (2013, *The Tail at Scale*) est nommé mais non extrait.

---

### 4.4 Livre IV — *Architecture de référence et exploitation* (Chapitres 37 à 46)

#### 4.4.1 Tableau métrique et structurel des chapitres 37 à 46 (`[L]`)

| Ch. | Fichier | Mots corps | Cible | Écart | `§` / `###` | Tab. | Fig. SVG | `Lecture` (corps/tot.) | Remontées `R-IV-*` | Sièges posés |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **37** | [`37-maillage-agents-point-application.md`](Livre%20IV\37-maillage-agents-point-application.md) | `7 636` | `7 500` | `+1,8 %` | 8 / 12 | 2 | 3 | 12 / 13 | `R-IV-38` à `41` (+1) | — |
| **38** | [`38-observabilite-agentique.md`](Livre%20IV\38-observabilite-agentique.md) | `6 608` | `7 500` | `−11,9 %` | 8 / 11 | 2 | 2 | 7 / 8 | `R-IV-42` à `44` | — *(siège de fait § 38.4)* |
| **39** | [`39-cycle-de-vie-operationnel.md`](Livre%20IV\39-cycle-de-vie-operationnel.md) | `6 542` | `6 500` | `+0,6 %` | 8 / 7 | 1 | 2 | 7 / 12 | `R-IV-45` à `47` (+3) | — *(siège de fait § 39.2.3)* |
| **40** | [`40-indicateurs-agentops-finops.md`](Livre%20IV\40-indicateurs-agentops-finops.md) | `6 105` | `6 500` | `−6,1 %` | 8 / 12 | 2 | 2 | 12 / 14 | `R-IV-48` à `50` | — |
| **41** | [`41-fabrique-agents-gouvernee.md`](Livre%20IV\41-fabrique-agents.md) | `4 503` | `6 000` | `−25,0 %` | 10 / 0 | 2 | 2 | 12 / 15 | `R-IV-51` à `53` | — |
| **42** | [`42-matrice-protocoles-exigences.md`](Livre%20IV\42-matrice-protocoles-exigences.md) | `7 110` | `7 000` | `+1,6 %` | 7 / 8 | 2 | 2 | 10 / 12 | `R-IV-54` à `56` (+1) | — |
| **43** | [`43-architecture-reference-6-couches.md`](Livre%20IV\43-architecture-reference-couches.md) | `6 786` | `8 000` | `−15,2 %` | 8 / 13 | 2 | 3 | 12 / 14 | `R-IV-57` à `59` | `§ 43.1`, `§ 43.3`, `§ 43.5` (`S5=None`) |
| **44** | [`44-formalisation-archimate.md`](Livre%20IV\44-formalisation-archimate.md) | `6 303` | `8 500` | `−25,8 %` | 11 / 13 | 2 | 3* | 1 / 1 | `R-IV-100` à `102` | `§ 44.6` (conformité traçable) |
| **45** | [`45-blueprint-instancie-cycle-de-vie.md`](Livre%20IV\45-blueprint-instancie-cycle-de-vie.md) | `6 126` | `10 000` | `−38,7 %` | 17 / 0 | 2 | 3 | 18 / 21 | `R-IV-103` à `106` (+1) | `§ 45.6` (organisation fabrique) |
| **46** | [`46-instrumentation-feuille-route.md`](Livre%20IV\46-instrumentation-feuille-route.md) | `3 004` | `3 000` | `+0,1 %` | 5 / 9 | 2 | 2 | 6 / 8 | `R-IV-107` à `109` | — |
| **Tot.** | **Livre IV (10 chapitres)** | **`60 723`** | **`70 500`** | **`−13,9 %`** | **90 / 85** | **19** | **24** | **97 / 118** | **`R-IV-38`–`59`, `100`–`109`** | **5 sièges** |

*\*Note : les 3 fichiers SVG du chapitre 44 (`f-44-00`, `f-44-01`, `f-44-08`) gravent en planches composites les 19 schémas ArchiMate (1 grille + 8 patrons + 9 paires d'anti-patrons).*

#### 4.4.2 Constats spécifiques au Livre IV

1. **Constat `A-M10` (Majeur) — Contradictions internes entre le corps et les notes de re-datation aux chapitres 37 et 39 (alors que le chapitre 40 a mis à jour son corps)** :
   - Au [`ch. 37 § 37.2.2` (l. 122–135)](Livre%20IV\37-maillage-agents-point-application.md) et au [`ch. 39 § 39.3` (l. 285–303)](Livre%20IV\39-cycle-de-vie-operationnel.md), le corps affirme que `agentgateway` (Linux Foundation, `S-116` / `F-70`) est en **« pré-version »**, suivi immédiatement d'un encadré de re-datation signalant qu'il est passé en version stable **`v1.4.0`** le 27 juillet 2026 !
   - De même, au [`ch. 39 § 39.1` (l. 105–113)](Livre%20IV\39-cycle-de-vie-operationnel.md), le corps affirme que Langfuse (`S-142` / `F-98`) évalue les agents selon **« neuf dimensions »**, suivi d'un encadré signalant que la source primaire n'en établit que **quatre** (*exactitude, pertinence, fidélité au contexte, justesse*) — alors même que le [`ch. 40 § 40.1.3` (l. 104)](Livre%20IV\40-indicateurs-agentops-finops.md) a directement intégré les **quatre dimensions** dans son corps le 2 septembre 2026 !
2. **Double blocage des chapitres 41 (`G-6`/`D-8`) et 44–45 (`R-IV-101`) (`A-D3`, `A-D4`)** :
   - Le [`chapitre 41`](Livre%20IV\41-fabrique-agents.md) (`4 503` mots, `−25,0 %`) est composé à 100 % de matière neuve sans aucune entrée au socle consolidé (5 lots d'instruction ouverts, 0 fait versé) et présente un adossement circulaire avec les chapitres 39 et 47 (`R-IV-53`).
   - Les [`chapitres 44`](Livre%20IV\44-formalisation-archimate.md) (`−25,8 %`) et [`45`](Livre%20IV\45-blueprint-instancie-cycle-de-vie.md) (`−38,7 %`) sont bloqués par la non-exécution du préalable `R-IV-101` (`J-IV-5`) : le mécanisme `Specialization + stéréotype + Profiles` et la liste des ~30 % d'éléments retirés par **ArchiMate 4 (The Open Group, doc C260 du 27 avril 2026)** n'ont jamais été re-vérifiés sur le document C260, et l'intégralité du ch. 44 repose sur le régime `[C]` (0 entrée sur ArchiMate parmi les 159 `S-nnn`).
3. **Anonymisation paradoxale du portefeuille IBM au chapitre 45 (`A-m4`) et omissions d'appareil aux chapitres 40 et 41 (`A-m5`)** :
   - Dans [`Livre IV/45-blueprint-instancie-cycle-de-vie.md`](Livre%20IV\45-blueprint-instancie-cycle-de-vie.md), bien que l'éditeur **IBM** soit nommé dans le titre et l'ouverture, le `Tableau 45.2` et les flux `§ 45.11`–`45.13` taisent tous les noms commerciaux des produits (*API Connect*, *App Connect Enterprise*, *IBM MQ 9.4*, *watsonx Orchestrate*, *Granite*, *watsonx.governance*) sous des périphrases génériques, et le `§ 45.12` dé-nomme **Lynx** et **ISO 20022** (*« le rail de grande valeur »*, *« la norme de messagerie financière »*) à rebours de la décision 18 !
   - Le [`ch. 40 § 40.7`](Livre%20IV\40-indicateurs-agentops-finops.md) est le seul chapitre du Livre IV où le paragraphe `✎ Renvoi daté, repointé le 15 septembre 2026` (`T4.3`) a été omis, laissant aux lignes 541 et 675 une plainte obsolète sur l'ancien décompte `5 564 mots`. Le [`ch. 41 § 41.9`](Livre%20IV\41-fabrique-agents.md) omet l'encadré `STATUT ARRÊTÉ LE 2 SEPTEMBRE 2026` dans sa note de statut.

---

### 4.5 Livre V — *Prospective, limites et péremption* (Chapitres 47 à 50), Annexes et Programme de figures

#### 4.5.1 Tableau métrique et structurel des chapitres 47 à 50 (`[L]`)

| Ch. | Fichier | Mots corps | Cible | Écart | `§` / `###` | Tab. | Fig. SVG | `Lecture` (corps/tot.) | Remontées `R-IV-*` | Sièges posés |
| :-: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **47** | [`47-artefact-livre-provenance-mise-en-service.md`](Livre%20V\47-artefact-livre-provenance-mise-en-service.md) | `5 033` | `8 000` | **`−37,1 %`** | 10 / 7 | 1 | 2 | 12 / 16 | `R-IV-60` à `64` | — |
| **48** | [`48-semantique-effet-idempotence-compensation.md`](Livre%20V\48-semantique-effet-idempotence-compensation.md) | `4 807` | `8 000` | **`−39,9 %`** | 8 / 6 | 2 | 2 | 9 / 11 | `R-IV-65` à `67` | `§ 48.1` (sémantique d'effet) |
| **49** | [`49-horizon-frontiere-connaissance-verifiable.md`](Livre%20V\49-horizon-frontiere-connaissance-verifiable.md) | `11 088` | `8 400` | **`+32,0 %`** | 16 / 23 | 1 | 3 | 18 / 20 | `R-IV-68` à `72` | `§ 49.0` (tri prospectif), `§ 49.6` (verrou sémantique) |
| **50** | [`50-peremption-protocole-revalidation.md`](Livre%20V\50-peremption-protocole-revalidation.md) | `5 920` | `6 000` | `−1,3 %` | 7 / 7 | 4 | 3 | 5 / 6 | `R-IV-73` à `75` | `§ 50.4` (registre de gel) |
| **Tot.** | **Livre V (4 chapitres)** | **`26 848`** | **`30 400`** | **`−11,7 %`** | **41 / 43** | **8** | **10** | **44 / 53** | **`R-IV-60` à `75`** | **4 sièges** |

#### 4.5.2 Constats spécifiques au Livre V, aux Annexes et au Programme de figures (`figures/`)

1. **Constat `A-B7` (Bloquant) — Deux divergences factuelles entre le texte du Livre V et les figures SVG gravées dans `figures/contenu5.py`** :
   - **`A-B7.1` — `Figure 49.0` (`figures/f-49-00-cone-incertitude.svg`, générée par [`figures/contenu5.py` l. 81](figures/contenu5.py#L81))** : la bande médiane du cône d'incertitude 2027–2032 porte le titre **`ANNONCÉ`**, alors que le siège du [`ch. 49 § 49.0.1` (l. 64)](Livre%20V\49-horizon-frontiere-connaissance-verifiable.md) et les **45 occurrences** dans le chapitre 49 imposent la triade canonique **`PROGRAMMÉ` / `PROJETÉ` / `SPÉCULATIF`** (zéro occurrence du mot `ANNONCÉ` dans le chapitre 49 !).
   - **`A-B7.2` — `Figure 50.4` (`figures/f-50-04-carte-fraicheur.svg`, générée par [`figures/contenu5.py` l. 176](figures/contenu5.py#L176))** : le bloc central de la carte de fraîcheur écrit *« Le tableau 50.1 ordonne les **onze** événements susceptibles de périmer… »*, alors que le `Tableau 50.1` et le texte du chapitre 50 ont été portés de **onze à quatorze événements** le 2 septembre 2026 (`D-16`) !
2. **Constat `A-M11` (Majeur) — Contradiction interne à la ligne 10 du `Tableau 50.1` (`ch. 50 § 50.2`, l. 114)** :
   - Dans [`Livre V/50-peremption-protocole-revalidation.md`](Livre%20V\50-peremption-protocole-revalidation.md), la **3e colonne** (*Signaux d'alerte*) enregistre la revalidation du 2 septembre 2026 (`draft-sharif-openid-agent-identity` passé en `-01` jusqu'au **27 février 2027**), mais la **4e colonne** (*Ce qui se refait*) de la même ligne n'a pas été mise à jour et affirme encore que deux lignes du `Tableau 18.1` reposent sur des documents expirant les **27 septembre et 24 novembre 2026** !
3. **Constat `A-M12` (Majeur) — Déficit volumétrique massif (−37,1 % et −39,9 %) et publication bloquée des chapitres 47 et 48 sous `D-3` / `G-6`** :
   - Rédigés le 27 juillet 2026 avant l'instruction des lots de matière neuve `L1` (artefact livré : SPDX 3.0, CycloneDX 1.7, SLSA v1.2, Sigstore), `L2` (idempotence d'effet agentique) et `L3` (compensation / sagas en contexte probabiliste), les chapitres 47 (`5 033` mots vs `8 000`) et 48 (`4 807` mots vs `8 000`) substituent des « contrats d'instruction » à l'analyse de fond. Même l'instruction partielle de `L1` le 30 juillet 2026 (`D-11`) est restée cantonnée dans une note d'attente au [`§ 47.0.1` (l. 50–86)](Livre%20V\47-artefact-livre-provenance-mise-en-service.md) sans vote adversarial ni refonte des `§ 47.2` et `§ 47.6`. De même, la « cinquième horloge » du [`§ 47.8.1`](Livre%20V\47-artefact-livre-provenance-mise-en-service.md) (harnais d'exécution, `D-2`) n'a jamais été confrontée aux chapitres 37 à 40 (`J-IV-7`).

---

## 5. Registre consolidé et numéroté des constats d'audit

### 5.1 Constats bloquants (`A-B1` à `A-B7`)

| ID | Fichier(s) et ligne(s) | Description et preuve (`[L]` / `[R]` / `[S]`) | Correctif prescrit |
| :---: | :--- | :--- | :--- |
| **`A-B1`** | [`build/rendre-piece.py`](build/rendre-piece.py#L48), [`Livre II/14-grille-cinq-questions.html`](Livre%20II/14-grille-cinq-questions.html#L677), [`Livre IV/37-maillage-agents-point-application.html`](Livre%20IV/37-maillage-agents-point-application.html#L740) | `python build/verifier-piece.py` et `verifier-piece-mutations.py` échouent (`code 1`) : `<table style="width:99%;">` généré par Pandoc 3.12.1 vs `<table style="width:100%;">` commité sur les `Tableau 14.2` et `Tableau 37.2` (6 colonnes `16 %`). (`[R]`) | Ajouter `"--columns=1000"` à l'appel `pandoc` dans `build/rendre-piece.py` et régénérer les `.html`. |
| **`A-B2`** | [`PRD/decompte.sh`](PRD/decompte.sh#L70), [`README.md`](README.md) | `bash PRD/decompte.sh --verifier` échoue (`code 1`) sans `LC_ALL=C` (`241260` vs `233257` mots bruts sur le Vol. I), la l. 70 n'appliquant pas `LC_ALL=C`. (`[R]`) | Préfixer `wc -w` par `LC_ALL=C` à la ligne 70 de `PRD/decompte.sh`. |
| **`A-B3`** | [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md), [`Livre V/50-peremption-protocole-revalidation.md`](Livre%20V\50-peremption-protocole-revalidation.md) | Expiration complète le **2 octobre 2026** de la validité de 30 jours (`CA-IV-04`) de la passe du 2 septembre 2026 (+42 jours écoulés au 14 octobre 2026). (`[L]`, `[S]`) | Exécuter une passe complète de revalidation datée du 14 octobre 2026 sur les 21 chapitres à haute sensibilité temporelle. |
| **`A-B4`** | [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md), [`ch. 3 § 3.2.1`](Livre%20I\03-securite-identite-gouvernance.md), [`ch. 12 § 12.5`](Livre%20II\12-heritage-standards-etires.md), [`ch. 18 § 18.1`](Livre%20II\18-know-your-agent.md), [`ch. 50 § 50.2`](Livre%20V\50-peremption-protocole-revalidation.md) | Interrogation d'URL d'archives immuables (`-00.txt`) le 2 sept. 2026 ayant masqué : (1) le passage de `draft-klrc-aiagent-auth` en `-03` (6 juill. 2026), son adoption WG WIMSE (9 sept. 2026) et son remplacement par **`draft-ietf-wimse-aims-00`** (15 sept. 2026) ; (2) la publication de **`draft-ietf-oauth-v2-1-16`** (2 sept. 2026) ; (3) l'expiration de `draft-klrc-wimse-ai-agents-00` (1er sept. 2026) ; (4) le passage de `draft-ietf-wimse-workload-creds` en `-01`. (`[S]`) | Interroger `datatracker.ietf.org/doc/...` ; mettre à jour `S-084`, `S-085`, `ch. 3`, `ch. 12`, `ch. 13`, `ch. 18` (`Tableau 18.1`) et `ch. 50` (`Tableau 50.1`). |
| **`A-B5`** | [`Livre III/33-iso-20022-lynx-rtr.md`](Livre%20III\33-iso-20022-lynx-rtr.md), [`Livre III/36-prospective-ap2-rails-canadiens.md`](Livre%20III\36-prospective-ap2-rails-canadiens.md), [`Livre V/50-peremption-protocole-revalidation.md`](Livre%20V\50-peremption-protocole-revalidation.md) | Entrée dans le **`T4 2026`** (depuis le 1er oct. 2026) pour le RTR (`S-027`/`F-29`), rendant caducs le décompte de « 38 jours » du `ch. 33 § 33.3` et la consultation de 30 jours du 24 août ; contradiction frontale avec `ch. 36 § 36.2.7` l. 305 qui écrit encore au futur *« doit entrer en vigueur le 24 août 2026 »*. (`[L]`, `[S]`) | Aligner `ch. 36 § 36.2.7` sur `ch. 33 § 33.3` et actualiser l'état du RTR à l'intérieur du `T4 2026`. |
| **`A-B6`** | [`ch. 13`](Livre%20II\13-identite-decentralisee-vc-did.md), [`ch. 16`](Livre%20II\16-passeport-agent.md), [`ch. 17`](Livre%20II\17-chaine-mandat-deux-sauts.md), [`ch. 20`](Livre%20II\20-usurpation-revocation-boucle-defensive.md), [`ch. 21`](Livre%20II\21-horloge-post-quantique.md) | **5 contradictions internes majeures** laissées par la passe `D-11` du 30 juillet 2026 au Livre II : (1) VC 2.0 / DID 1.1 extraits en `§ 13.0` mais dits « non établis » en `§ 13.1`, `Synthèse` et `§ 13.6` ; (2) deux `Tableau 16.2` au ch. 16 ; (3) 4e piste sous `### 17.6.2 Trois pistes...` et conclusion *« aucune des trois »* ; (4) 10e rangée du `Tableau 20.1` appelée *« La onzième rangée »* ; (5) `ITSM.40.001` extrait en `§ 21.8` mais `§ 21.9` dit le socle exclusivement US. (`[L]`) | Purger les phrases caduques en `ch. 13` et `ch. 21`, renuméroter le second tableau en `Tableau 16.3`, passer `ch. 17 § 17.6.2` à « Quatre pistes », et corriger « onzième/dix » en « dixième/neuf » au `ch. 20 § 20.4`. |
| **`A-B7`** | [`figures/contenu5.py`](figures/contenu5.py#L81) (l. 81 et l. 176), [`figures/f-49-00-cone-incertitude.svg`](figures/f-49-00-cone-incertitude.svg), [`figures/f-50-04-carte-fraicheur.svg`](figures/f-50-04-carte-fraicheur.svg) | **2 divergences texte ↔ SVG** au Livre V : `Figure 49.0` affiche **`ANNONCÉ`** au lieu de **`PROJETÉ`** (siège `ch. 49 § 49.0`) ; `Figure 50.4` affiche **« onze événements »** au lieu de **« quatorze événements »** (`Tableau 50.1`). (`[L]`) | Remplacer `"ANNONCÉ"` par `"PROJETÉ"` (l. 81) et `"onze événements"` par `"quatorze événements"` (l. 176) dans `figures/contenu5.py`, puis relancer `python figures/genere.py`. |

### 5.2 Constats majeurs (`A-M1` à `A-M12`)

| ID | Fichier(s) et ligne(s) | Description et preuve (`[L]` / `[R]` / `[S]`) | Correctif prescrit |
| :---: | :--- | :--- | :--- |
| **`A-M1`** | [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py), 45 chapitres sur 50 (pied de note de statut) | Désynchronisation entre le bandeau résumé supérieur et l'`### En-tête de rédaction` inférieur : 40 chapitres affichent un pourcentage hybride (`mots_2_sept` + `%_28_juillet`), et 5 chapitres (`ch. 10, 31, 35, 40, 42`) affichent encore l'ancien nombre de mots d'avant le 15 sept. 2026. (`[L]`) | Étendre `PRD/reporter-volumetrie.py` pour mettre à jour et vérifier simultanément la ligne `Volumétrie :` de l'`### En-tête de rédaction` inférieur. |
| **`A-M2`** | `ch. 8, 9, 10, 11, 39, 42, 43, 44` (ligne 8, `En-tête résumé`) | La ligne `Garde-fous balayés` du bandeau résumé en tête de 8 chapitres omet `réserve F-01`, `réserve F-06`, `réserve F-09`, `réserve F-25`, `réserve F-37` et `§ 8.2` pourtant déclarés en pied de pièce. (`[L]`) | Élargir l'extracteur des garde-fous aux réserves `F-xx` et `§ 8.2` et régénérer les 8 bandeaux. |
| **`A-M3`** | [`PRD/check-compendium.py`](PRD/check-compendium.py#L166-L168) | Dans `P3`, `"Vol. II" in b` matche `"Vol. III"` par sous-chaîne, classant à tort tout chapitre du Vol. III comme ayant une source au Vol. II. (`[L]`) | Utiliser `re.search(r"Vol\.\s+II(?!I)", b)` dans `PRD/check-compendium.py`. |
| **`A-M4`** | [`build/compendium.template`](build/compendium.template#L64-L82), [`JOURNAL.md`](JOURNAL.md), [`PRD/PRD.md`](PRD/PRD.md) | 6e recomposition PDF du 15 sept. 2026 (`PAS = 16.675pt`, `13 022 826` o.) non consignée dans `JOURNAL.md` ni `PRD.md` ; foliotage à `6,0 mm` du bord (`< 6,35 mm`) ; page de titre et colophon sans mention d'archive (`D-10` vs `D-18`). (`[L]`) | Consigner la 6e recomposition dans `JOURNAL.md` et `PRD.md` ; réduire `header-ascent`/`footer-descent` à `11mm` (`7,0 mm` du bord). |
| **`A-M5`** | [`PRD/PRD.md`](PRD/PRD.md) (§ 6 l. 73, § 7.1 l. 117, § 9 l. 221–246, § 18.3 l. 634) | `PRD.md` affiche encore `TOC v0.32`, omet le `ch. 31 (§ 31.3.2)` de la liste des chapitres portant les 12 occurrences « hors corpus bibliographique », et affiche `24 / 114 / 23 / 6` mutations au lieu de `25 / 115 / 30 / 8`. (`[L]`, `[R]`) | Mettre à jour les quatre passages de `PRD/PRD.md`. |
| **`A-M6`** | [`annexe-references.md`](annexe-references.md) (l. 31, 57, 62, 166) vs [`PRD/socle-consolide.md`](PRD/socle-consolide.md) | `S-001`, `S-027`, `S-032` et `S-131` dans `annexe-references.md` n'intègrent pas les amendements du 2 septembre 2026 portés dans `socle-consolide.md` v1.2. (`[L]`) | Aligner les 4 lignes d'`annexe-references.md` sur `PRD/socle-consolide.md` v1.2 et ajouter un contrôle de parité dans `check-compendium.py`. |
| **`A-M7`** | `ch. 25, 26, 27, 30, 31, 34, 35, 42, 46` | Comptes à rebours vers le 1er mai 2027 figés à « 9 mois et 4 jours (278 j) » alors qu'il reste **199 jours (~6,5 mois)** au 14 oct. 2026 ; date AMF confirmée au **7 avril 2026** (`[S]`) ; seuil de 90 jours du `ch. 35 § 35.10` atteint le 14 oct. 2026 ; dates dépassées (2 août 2026 AI Act, août 2026 GA, 20 sept. 2026 EO 14412, oct. 2026 FSB) encore au futur. (`[L]`, `[S]`) | Actualiser les comptes à rebours et les temps verbaux des échéances d'août–octobre 2026 ; intégrer la date du 7 avril 2026 pour `S-023`/`S-113`. |
| **`A-M8`** | [`Livre I/08-anatomie-mcp-a2a.md`](Livre%20I\08-anatomie-mcp-a2a.md) (l. 15 et l. 882) | La thèse en tête du ch. 8 anonymise `MCP` et `A2A` (*« dans les agents, entre les agents — doctrine [...] déclarée par l'un des deux projets »*) tout en affirmant en `§ 8.8` l. 882 la citer *« telle quelle »* depuis `TOC.md`. (`[L]`) | Rétablir en l. 15 du ch. 8 le texte exact de `PRD/TOC.md` l. 154 et vérifier l'égalité intégrale dans `check-compendium.py` `P2`. |
| **`A-M9`** | [`Livre III/31-vertical-financier-durcisseurs.md`](Livre%20III\31-vertical-financier-durcisseurs.md) (l. 66, 126, 568, 1041) | Le ch. 31 déclare encore en 4 endroits que `S5` est désactivé sur les sièges `§ 31.1.1`, `§ 31.1.2` et `§ 31.3.4`, alors que `PRD/check-sieges.py` l'y a réarmé le 2 septembre 2026. (`[L]`, `[R]`) | Mettre à jour les 4 occurrences dans `31-vertical-financier-durcisseurs.md` pour refléter le réarmement de `S5`. |
| **`A-M10`** | [`ch. 37 § 37.2.2`](Livre%20IV\37-maillage-agents-point-application.md), [`ch. 39 § 39.1 & § 39.3`](Livre%20IV\39-cycle-de-vie-operationnel.md) | Le corps des ch. 37 et 39 maintient des états démentis (« pré-version » pour `agentgateway`, « neuf dimensions » pour Langfuse) contredits par leurs propres encadrés adjacents (`v1.4.0` stable, `4 dimensions`), alors que le ch. 40 a corrigé son corps. (`[L]`) | Intégrer `v1.4.0` et `quatre dimensions` directement dans le corps des ch. 37 et 39, comme fait au ch. 40 `§ 40.1.3`. |
| **`A-M11`** | [`Livre V/50-peremption-protocole-revalidation.md`](Livre%20V\50-peremption-protocole-revalidation.md) (`Tableau 50.1`, ligne 10) | La 3e colonne acte la revalidation du 2 sept. 2026 (`draft-sharif-01` au 27 févr. 2027), mais la 4e colonne affirme encore que deux lignes du ch. 18 expirent les 27 sept. et 24 nov. 2026. (`[L]`) | Harmoniser la 4e colonne de la ligne 10 du `Tableau 50.1` avec l'état réel sur le Datatracker (`draft-ietf-wimse-aims-00` et `draft-drake-03`). |
| **`A-M12`** | [`Livre V/47-artefact-livre-provenance-mise-en-service.md`](Livre%20V\47-artefact-livre-provenance-mise-en-service.md), [`Livre V/48-semantique-effet-idempotence-compensation.md`](Livre%20V\48-semantique-effet-idempotence-compensation.md) | Déficits volumétriques de **−37,1 %** (`5 033 / 8 000` mots) au ch. 47 et **−39,9 %** (`4 807 / 8 000` mots) au ch. 48, rédigés sans socle sous `D-3` (lots `L1`–`L3` non clos, `G-6` ouverte). (`[L]`) | Voter et verser `L1` au socle, instruire `L2` et `L3`, et développer le corps des `§ 47.2`, `§ 47.6`, `§ 48.2` et `§ 48.3`. |

### 5.3 Constats mineurs (`A-m1` à `A-m14`) et dettes structurelles de gouvernance (`A-D1` à `A-D8`)

- **Constats mineurs (`A-m1` à `A-m14`)** :
  - `A-m1` : [`build/echantillon.template`](build/echantillon.template) figé au 31 juillet 2026 (`PAS = 17pt`, macro `#figure-svg` à 1 argument).
  - `A-m2` : [`PRD/registre-gel.md`](PRD/registre-gel.md) et [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) référençant `TOC.md v0.35` au lieu de `v0.36`.
  - `A-m3` : Renvois résiduels à `avant-propos` aux [`ch. 1 § 1.0.2` (l. 40)](Livre%20I\01-interoperabilite-integration-entreprise.md) et [`ch. 31` (l. 38)](Livre%20III\31-vertical-financier-durcisseurs.md) ainsi qu'aux `Annexes C, E, F, H` retirées par la décision 26.
  - `A-m4` : Survivance de périphrases d'anonymisation de la décision 15 (pourtant révoquée par la décision 18 du 30 juillet 2026) aux ch. 1, 2, 5, 7, 8, 9, 10, 11, 12, 17, 19, 24, 30, 31, 34, 36, 37, 38 (`Tableau 38.2` sur les produits IBM), 39 (`Langfuse`, incident `Drift/Salesforce`), 43 (`§ 43.6`) et 45 (`Tableau 45.2` produits IBM, `CIBC` en `§ 45.11`, `Lynx` et `ISO 20022` en `§ 45.12`).
  - `A-m5` : Omission du paragraphe `✎ Renvoi daté, repointé le 15 septembre 2026` (`T4.3`) au seul [`ch. 40 § 40.7` (l. 665)](Livre%20IV\40-indicateurs-agentops-finops.md) et omission de l'encadré `STATUT ARRÊTÉ LE 2 SEPTEMBRE 2026` dans la note de statut du [`ch. 41 § 41.9` (l. 413)](Livre%20IV\41-fabrique-agents.md).
  - `A-m6` : Double point final `JSON-RPC 2.0..*` dans la thèse du [`ch. 3` (l. 15)](Livre%20I\03-securite-identite-gouvernance.md).
  - `A-m7` : Répétition `de de` dans [`Livre II/15-cycle-de-vie-delegation-tracabilite.md` (l. 201)](Livre%20II\15-emettre-carte-annuaires-registres.md) (*« dépourvu de de tout jeton »*).
  - `A-m8` : Accord fautif *« La seconde garde-fou »* (pour *Le second garde-fou*) dans [`Livre III/24-patrons-conception-agentiques.md` (l. 458)](Livre%20III\24-passage-echelle-entreprise.md).
  - `A-m9` : Coquille *« d'une jalon »* dans [`Livre IV/46-instrumentation-feuille-route.md` (l. 390)](Livre%20IV\46-instrumentation-feuille-route.md) et *« s'écarte avec la cible »* au [`ch. 44 § 44.10` (l. 694)](Livre%20IV\44-formalisation-archimate.md).
  - `A-m10` : Deux « sièges de fait » invoqués dans la prose du Livre IV (`ch. 38 § 38.4` et `ch. 39 § 39.2.3`) non inscrits dans [`PRD/check-sieges.py`](PRD/check-sieges.py).
  - `A-m11` : Plafond de la plage `R-IV-100` à `R-IV-109` ayant laissé **6 remontées non numérotées** dans le Livre IV (1 au ch. 37, 3 au ch. 39, 1 au ch. 42, 1 au ch. 45).
  - `A-m12` : Sur-déclaration d'assignation de 10 entrées au [`ch. 45 § 45.16` (l. 782)](Livre%20IV\45-blueprint-instancie-cycle-de-vie.md) (`Vol. II F-02, F-05, F-09, F-16, F-27, F-34, F-35, F-43, F-48` et `Vol. III H-13` : 0 occurrence au corps).
  - `A-m13` : Le [`chapitre 28`](Livre%20III\28-valeurs-mobilieres-acvm-11-348.md) est l'unique chapitre sur 50 à ne comporter **aucune figure SVG** (`0` figure gravée).
  - `A-m14` : Dans [`PRD/socle-consolide.md`](PRD/socle-consolide.md) (`S-048` à `S-053`), 6 entrées héritées de la *Synthèse* supprimée du Volume I conservent un chemin source vers un fichier qui n'existe plus.
- **Dettes structurelles de gouvernance actées lors de la clôture en l'état (`D-19`) (`A-D1` à `A-D8`)** :
  - `A-D1` : Porte `G-4` non franchie sur le fond (dépendance au Volume III « rédigé non publiable », 6 remontées `R-G-*` ouvertes affectant les Livres II, III et IV).
  - `A-D2` : Lot `D-9` sur le biais d'automatisation (`ch. 17 § 17.5`) non instruit, affectant les ch. 17, 25, 27 et 40 (`R-IV-49`).
  - `A-D3` : Porte `G-6` ouverte sur le chapitre 41 (`D-8`, 5 lots non ouverts, 0 fait au socle) et sur les chapitres 47–48 (`D-3`, lots `L1`–`L3` non clos).
  - `A-D4` : Préalable normatif `R-IV-101` (`J-IV-5`) sur ArchiMate 4 (`doc C260` du 27 avril 2026) non exécuté et 100 % du ch. 44 en `[C]` (`R-IV-102`), bloquant les ch. 44 et 45.
  - `A-D5` : Porte `G-5` non franchie (`D-2` : couche d'exécution / harnais logée en 5e horloge au ch. 47 § 47.8.1 sans balayage du Livre IV `J-IV-7`).
  - `A-D6` : Non-réadossement des chapitres aux identifiants `S-001`..`S-159` (`CA-IV-01` écarté par `D-16` : `P3` = 524 emplois nus de `F-xx`/`H-xx` sur 26 pièces mixtes ; `P4` = 23 citations de `F-92`, `F-96`, `H-15`).
  - `A-D7` : Absence de relecture tierce sur la dualité défensive/offensive des ch. 19–20 (`CA-IV-11`) et sur le blueprint du ch. 45 (`CA-IV-12`).
  - `A-D8` : [`annexe-bibliographie.md`](annexe-bibliographie.md) limitée aux 1 154 entrées du Volume I (absence de fusion des bibliographies des Volumes II et III documentée en `§ I.2`).

---

## 6. Synthèse de l'évaluation académique universitaire

Conformément à la demande, une évaluation académique universitaire complète de niveau **doctoral de référence** a été établie dans le document compagnon **[`Évaluation académique.md`](Évaluation%20académique.md)**, en stricte conformité avec le [`Gabarit d'évaluation académique.md`](../Gabarit%20d'évaluation%20académique.md) (v1.0). En voici le profil de notation pondéré et le verdict :

| Code | Dimension du barème académique | Poids | Note / 20 | Pondéré |
| :---: | :--- | :---: | :---: | :---: |
| **`D1`** | Rigueur scientifique et exactitude factuelle | 20 % | **14,5 / 20** | `2,90` |
| **`D2`** |Qualité, fraîcheur et traçabilité du sourçage primaire | 15 % | **14,0 / 20** | `2,10` |
| **`D3`** | Cohérence architecturale et consistance inter-modules | 15 % | **15,5 / 20** | `2,325` |
| **`D4`** | Originalité de la thèse et valeur ajoutée analytique | 15 % | **17,5 / 20** | `2,625` |
| **`D5`** | Opérationnalisation, reproductibilité et outillage | 15 % | **17,0 / 20** | `2,55` |
| **`D6`** | Qualité rédactionnelle, pédagogique et typographique | 10 % | **16,0 / 20** | `1,60` |
| **`D7`** | Lucide épistémique, gouvernance des limites et réflexivité | 10 % | **19,0 / 20** | `1,90` |
| **TOTAL** | **Note globale pondérée** | **100 %** | **`16,00 / 20`** (`80,0 %`) | **Mention *Très Bien* (`A-`)** |

- **Verdict académique retenu** : **Acceptation avec révisions mineures à modérées** (*en tant qu'archive de recherche et d'architecture `corpus-v1.0` sous `D-18`/`D-19`*) — **Révisions majeures requises** dans l'hypothèse d'une levée ultérieure de `D-18` en vue d'une publication éditoriale ou normative externe.
- Voir [`Évaluation académique.md`](Évaluation%20académique.md) pour les sept fiches analytiques détaillées (§ 4.1 à § 4.7), la confrontation aux sources externes (§ 6), les forces et faiblesses majeures (§ 7 et § 8) et la feuille de route de remédiation (§ 10).

---

## 7. Plan d'exécution et de remédiation chiffré

Pour résorber les 33 anomalies techniques, documentaires et calendaires (`A-B1` à `A-B7`, `A-M1` à `A-M12`, `A-m1` à `A-m14`) sans même rouvrir les chantiers de gouvernance gelés par `D-19`, puis — optionnellement — instruire la levée de `D-18`, quatre phases ordonnées sont prescrites :

### Phase 1 — Réparation immédiate des scripts en échec et des divergences SVG (`~0,5 jour`)
1. **`A-B1`** : Ajouter `"--columns=1000"` dans [`build/rendre-piece.py`](build/rendre-piece.py#L48) et régénérer `14-grille-cinq-questions.html` et `37-maillage-agents-point-application.html`.
2. **`A-B2`** : Préfixer la ligne 70 de [`PRD/decompte.sh`](PRD/decompte.sh#L70) par `LC_ALL=C`.
3. **`A-B7`** : Corriger `"ANNONCÉ"` → `"PROJETÉ"` (l. 81) et `"onze événements"` → `"quatorze événements"` (l. 176) dans [`figures/contenu5.py`](figures/contenu5.py#L81) et exécuter `python figures/genere.py`.
4. **`A-M3`** : Corriger la détection de `"Vol. II"` dans [`PRD/check-compendium.py`](PRD/check-compendium.py#L166).
- **Critère de sortie Phase 1 (`[R]`)** : `verifier-piece.py`, `verifier-piece-mutations.py`, `bash PRD/decompte.sh --verifier` (sans préfixe d'environnement) et `figures/genere.py --verifier` retournent tous **`0`**.

### Phase 2 — Purge des contradictions internes (`D-11`, ch. 8, ch. 31, ch. 36, ch. 37/39, ch. 50) (`~1 jour`)
1. **`A-B6`** : Résorber les 5 contradictions internes des chapitres 13 (`§ 13.1`, `Synthèse`, `§ 13.6`), 16 (renuméroter le second `Tableau 16.2` en `Tableau 16.3`), 17 (`§ 17.6.2` « Quatre pistes »), 20 (`§ 20.4` « dixième rangée / neuf rangées ») et 21 (`§ 21.9` sur la lacune canadienne).
2. **`A-B5` & `A-M11`** : Corriger le futur caduc du [`ch. 36 § 36.2.7` (l. 305)](Livre%20III\36-prospective-ap2-rails-canadiens.md) sur le 24 août 2026 et la 4e colonne de la ligne 10 du [`Tableau 50.1`](Livre%20V\50-peremption-protocole-revalidation.md).
3. **`A-M8`, `A-M9`, `A-M10`** : Rétablir la thèse verbatim au [`ch. 8` (l. 15)](Livre%20I\08-anatomie-mcp-a2a.md) ; corriger les 4 mentions erronées de `S5` désactivé au [`ch. 31`](Livre%20III\31-vertical-financier-durcisseurs.md) ; intégrer `agentgateway v1.4.0` et les `4 dimensions` de Langfuse dans le corps des [`ch. 37`](Livre%20IV\37-maillage-agents-point-application.md) et [`ch. 39`](Livre%20IV\39-cycle-de-vie-operationnel.md).
- **Critère de sortie Phase 2 (`[R]`)** : `check-toc.py`, `check-sieges.py`, `check-compendium.py` et `decompte.sh --registre` retournent **`0`** après mise à jour des décomptes.

### Phase 3 — Resynchronisation des métadonnées, des annexes et de la passe calendaire au 14 octobre 2026 (`~1,5 jour`)
1. **`A-M1` & `A-M2`** : Corriger [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py) pour synchroniser les `### En-tête de rédaction` en pied des 50 chapitres et rétablir les réserves `F-xx` / `§ 8.2` en tête des 8 chapitres tronqués.
2. **`A-M4`, `A-M5`, `A-M6`, `A-m1`–`A-m14`** : Mettre à jour [`PRD/PRD.md`](PRD/PRD.md), [`JOURNAL.md`](JOURNAL.md), [`annexe-references.md`](annexe-references.md) (`S-001`, `S-027`, `S-032`, `S-131`) et [`build/echantillon.template`](build/echantillon.template), et purger les coquilles et périphrases d'anonymisation résiduelles.
3. **`A-B3`, `A-B4`, `A-M7`** : Produire `PRD/revalidation-2026-10-14.md` en interrogeant directement le Datatracker IETF (`draft-ietf-wimse-aims-00`, `draft-ietf-oauth-v2-1-16`, `draft-ietf-wimse-workload-creds-01`), intégrer la date du **7 avril 2026** pour la LD IA de l'AMF (`S-023`), et actualiser l'ouverture du `T4 2026` du RTR et le compte à rebours vers le 1er mai 2027.

### Phase 4 (Optionnelle, hors clôture `D-19`) — Levée des verrous de publication (`G-4`, `G-5`, `G-6`, `G-7`) (`~10 à 15 jours`)
- Clôture des 6 remontées du Volume III (`G-4`), instruction du lot `D-9` sur le biais d'automatisation (`ch. 17, 25, 27, 40`), vérification de C260 ArchiMate 4 (`R-IV-101`, `ch. 44–45`), instruction et vote adversarial des lots de matière neuve des chapitres 41 (`D-8`) et 47–48 (`D-3`, `L1`–`L3`), et ré-adossement intégral aux identifiants `S-001`..`S-159` (`CA-IV-01`).
