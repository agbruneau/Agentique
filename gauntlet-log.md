# Journal de boucle — plan d'exécution, phases 0 à 2

*Append-only. Ouvert le 15 septembre 2026. Objet : exécuter les phases 0, 1 et 2 de
« Plan d'exécution — évaluation académique.md ». Décisions d'auteur appliquées : DA-1 (a), DA-5 (a).
Barre : dépôt `the-turing-way/the-turing-way` au commit `7b7c9a5` (2026-09-04), clone partiel
sans images. Plafond : douze agents, passe de lissage comprise. Verdict à l'aveugle, A/B d'ordre
alterné, un écart par tour.*

## Découpage

| Morceau | Tâches | Dimension jugée | Équivalent chez la barre |
|---|---|---|---|
| **M1 — Appareil rejouable** | T0.2, T0.3, T0.4, T0.5, T0.9, T1.1 à T1.4 | contrôles versionnés, branchés en CI, capables d'attraper une régression ; arbre propre après rejeu | `.github/workflows/`, `lychee.toml`, `tests/` |
| **M2 — Portes d'entrée** | T0.1, T0.6, T0.7, T1.5 | un tiers sait ce que le dépôt porte, dans quel état, ce qui est vérifié ; chaque chiffre est vrai à la date | `README.md`, `ways_of_working.md`, `release-workflow.md` |
| **M3 — Attribution et traçabilité** | T0.8, T2.1, T2.2, T2.3 | qui a fait quoi, humains, outils et agents ; ce qui a été retiré se retrouve | `.all-contributorsrc`, `CITATION.cff`, `.zenodo.json`, `GOVERNANCE_ROLES.md`, `CODEOWNERS` |

Fichiers partagés : `README.md` (M2, M3), `2 - Compendium/PRD/PRD.md` (M2 pour D-17, M3 pour les
renvois `audit.md`). Édition par remplacement exact seulement.

## Tour 1

### M3 — bâtisseur
- Déclaré : T0.8, T2.1, T2.2, T2.3 fermées (à juger sur l'artefact, pas sur ce compte rendu).
- Découvertes déclarées : 173 commits sur 328 co-signés par cinq modèles (le plan disait 20) ; huit journaux de boucle supprimés (le plan disait deux) ; `audit.md` supprimé trois fois (`60e1b99`, `f6183bf`, `982ef3a`).
- Coût : 456 k jetons, 136 appels d'outil, 41 min.

### M3 — critique (A = barre, B = Agentique)
- **Verdict : B.** Rejeux du critique sur B : totaux d'attribution exacts (328 commits), 58/58 commandes `git show` d'`ARCHIVES.md`, 47/47 commits de suppression, 7/8 empreintes exactes. Sur A : attribution déclarative, deux divergences entre sources, un lien mort.
- **Écart retenu (B)** : les deux registres ne sont pas suivis par git (`??`), `HEAD:README.md` porte encore « d'une seule main », et aucun contrôle ne les protège de la péremption (CONTRIBUTIONS.md:197-198 l'admet).
- Défauts mineurs relevés : `ARCHIVES.md:128` (ordre des empreintes contre la colonne Pièce, une relecture omise) ; `ARCHIVES.md:117` et `LICENSE:44-45` disent « avant » la licence alors que retrait et licence tiennent au même commit `696bcac`.
- Suite : victoire à l'aveugle, le morceau sort de la boucle. Le suivi git relève d'un commit, que l'orchestrateur ne fait pas sans l'accord de l'auteur ; les mineurs d'`ARCHIVES.md` vont à la passe de lissage ; `LICENSE` n'est pas touché (texte juridique, rapporté à l'auteur).
- Coût : 149 k jetons, 23 appels, 5 min.

### M2 — bâtisseur
- Déclaré : T0.1, T0.6, T0.7 fermées ; **T1.5 non fermée** (badge posé, flux jamais exécuté faute de push).
- Déclaré aussi : `APPAREIL.md` réécrit sur rejeux du jour (8 h 43 – 9 h 20) ; table « État au 15 septembre 2026 » en tête du `README.md` ; chiffres au présent périmés corrigés (467 → 470 tests, 7 diapositives et non 9, lignes Rust, mots du traité).
- Signalé : en-tête du PRD du compendium encore « CLOS ET FINAL » sans D-17 (hors périmètre) ; `verifier-piece.py` sort 1 sans Pandoc dans le `PATH` ; collision de fichiers d'outillage dans `r1/` avec un autre bâtisseur (aucune sortie citée n'en dépend, déclaré).
- Coût : 439 k jetons, 154 appels, 47 min.

### M1 — bâtisseur
- Déclaré : T0.2, T0.3, T0.4, T0.5, T0.9, T1.3, T1.4 fermées ; T1.2 fermée localement (Windows et WSL Ubuntu, arbre intégré M1+M2+M3 ; revert d'essai d'une figure gelée → rouge) ; **T1.1 non fermée** (cargo validé sous Windows, chaîne gnu, jamais compilé sous Linux).
- Élargi : `newline="\n"` sur les 46 écritures texte du dépôt, pas les trois nommées ; `reconfigure` sur 30 scripts ; harnais `check-renvois-mutations.py` (15 mutations).
- Défauts révélés par le rejeu Linux, contournés dans le flux : `decompte.sh` dépend de la locale ; `reporter-volumetrie.py` lance le bash de WSL sous Windows ; `Traité.pdf` embarque des polices du poste.
- Couplage : le commit qui porte le flux doit porter T0.8 (M3), sinon `check-renvois.py` est rouge.
- Coût : 474 k jetons, 205 appels, 56 min.

### M2 — critique (A = barre, B = Agentique)
- **Verdict : B.** Le tableau daté de `README.md:9-13` répond à « quoi, dans quel état, vérifié comment, non vérifié » ; 20 affirmations rejouées sur B tiennent sur 22 (pages, 470 tests, 2 079 renvois / 0 mort, `genere.py --verifier` → 0, contrôles du compendium, D-17). La barre porte des procédures périmées (`release-workflow.md:12`, `ways_of_working.md:15`).
- **Écart retenu (B)** : la chronique datée de `README.md:15-252` se déchiffre plus qu'elle ne se lit (⚠⚠⚠, corrections de corrections, trois dates de clôture) — relève de la phase 4, hors périmètre de cette boucle. Deux affirmations au présent fausses à la date : `README.md:77-82` dit le `/Author` de l'article « non corrigé » et présent « sur sept » PDF, alors que `05fcc84` l'a corrigé et que huit le portent ; `README.md:342` donne 24 pièces à `bancs/`, `git ls-files` en rend 12.
- Suite : victoire à l'aveugle, le morceau sort de la boucle. Les deux affirmations fausses vont à la passe de lissage, par incise d'ancrage (phrases datées) ; la lisibilité de la chronique reste à la phase 4.
- Coût : 153 k jetons, 29 appels, 7 min.

### M1 — critique (A = Agentique, B = barre)
- **Verdict : A.** 31 étapes de `appareil.yml` rejouées à la main sur un clone de l'arbre de travail (`autocrlf=false`) : toutes rc=0 ; `cargo fmt --check` rc=0 (clippy et `cargo test` non rejoués, durée). Injections toutes vues : renvoi cassé, +1 octet sur un SVG gelé, CRLF, horodatage dans un générateur (garde « arbre propre »), plancher à 469 tests. Chez la barre : contrôle de taille qui ne peut pas échouer (`tests/test-file-size.sh:15`), étapes en mode push jamais exécutées, `fail: false` sur les liens externes.
- **Écart retenu (A)** : l'appareil n'est pas versionné — `git ls-files .github Python` → 0 — et aucun runner GitHub n'a rendu de verdict (`APPAREIL.md:60`). Se ferme par un commit et un push, que l'orchestrateur ne fait pas sans l'accord de l'auteur.
- Suite : victoire à l'aveugle, le morceau sort de la boucle.
- Coût : 164 k jetons, 54 appels, 12 min.

### Bilan du tour 1
Trois victoires à l'aveugle sur trois ; la boucle sort par victoire, sans second tour. Les trois écarts retenus convergent : **rien n'est commité ni poussé**, donc rien n'existe pour un tiers qui clone, et T1.1 / T1.5 ne se ferment qu'au premier passage réel du flux. Agents consommés : 6 sur 12, plus la passe de lissage.

## Passe de lissage
- Coutures corrigées : `/Author` de l'article et `bancs/` (12 fichiers suivis) par incises datées dans `README.md` ; `ARCHIVES.md:117,128` (commit `696bcac`, ordre des empreintes, relecture manquante) ; D-17 dans l'en-tête du PRD et du TOC du compendium ; défauts déclarés par M1 portés à `APPAREIL.md` ; mentions « non commité » périmées après `78ebf9c` (commit de l'auteur, 10 h 02).
- Signalé sans correction : premier passage de la CI (run `34978980074`) en échec — parité de `check-article.py` sous Linux et Windows ; `cargo test` sous PowerShell côté Windows ; `LICENSE:44-45` porte « avant » ; bandeaux « clos et final » sans D-17 dans cinq `README` de volumes ; « pas d'intégration continue » au présent dans trois documents du traité ; `gauntlet-log.md` absent de la carte du `README`.
- Contrôles rejoués sur `78ebf9c` + lissage : `check-renvois.py` (2 079 renvois, 0 mort), son harnais (16), `check-compendium.py`, `check-toc.py`, `check-sieges.py`, `genere.py --verifier`, deux harnais, `check-resume.py` × 10 — tous 0.
- Coût : 344 k jetons, 85 appels, 24 min. Total de la boucle : 7 agents sur 12, ≈ 2,18 M jetons.

---

# Suite — « tout compléter » (15 septembre 2026, après-midi)

*L'auteur demande l'exécution complète du plan. Portée retenue : correctif de la CI, phases 3, 4
et 6, la part de la phase 5 qu'aucun tiers n'exige (T5.1 consigne, T5.4 échelle), T7.1, T7.2 et
T7.4. Hors d'atteinte : la relecture elle-même (T5.2, T5.3), l'étiquette `corpus-v1.0` et le DOI
(T7.3, après re-clôture et compte Zenodo de l'auteur). Écart assumé au plan : T7.1 et T7.2
passent avant la phase 5, que le plan leur faisait attendre. Phase 8 : décidée au verdict de la
phase 4. Plafond annoncé : environ 20 agents. Pushes sur `main` autorisés par l'auteur pour ce
plan. Barre inchangée : `the-turing-way/the-turing-way`. Les tâches à critère binaire (CI, phase 6,
T7.4) n'ont pas de critique à l'aveugle : l'orchestrateur rejoue leurs critères.*

## Correctif de la CI — `7ad9e44`
- Cause 1 (vérifiée) : la parité des PDF comparait les octets hors dates, mais pas les positions du xref, qu'une date UTC plus courte décale ; reproduite localement par la mutation M2c (rouge sur le comparateur de `e6eec1d`, verte sur le correctif), corrigée dans `check-article.py` et `check-traite.py`.
- Cause 2 (lue au journal) : `defaults.run` de la tâche Simulateur sans `shell` → PowerShell sous Windows ; `shell: bash` ajouté.
- Fait par l'orchestrateur, sans agent.

## Vague A — bâtisseurs
| Morceau | Tâches | Critique |
|---|---|---|
| **M4 — Livrables tranchés** | T3.1 (a), T3.2, T3.3 ; bandeaux « clos et final » sans D-17 ; `gauntlet-log.md` à la carte du `README` | à l'aveugle |
| **M5 — Corrections locales** | T6.1 à T6.7 (T6.8 : DA-6 (b), rien) ; « pas d'intégration continue » au présent dans trois documents du traité | critères rejoués par l'orchestrateur |
| **M6 — Préparer la relecture** | T5.1 (consigne ; relecteurs à nommer par l'auteur, DA-4), T5.4 | à l'aveugle |
| **M8 — Note de synthèse** | T7.2, variante note | à l'aveugle |
- **CI verte** au run `34986482375` sur `7ad9e44` : les six tâches (Documents, Renvois, Simulateur × Linux, Windows). T1.1 et T1.5 se ferment : premier passage réel du flux, badge vert.

### M6 — bâtisseur
- Déclaré : T5.4 fermée — échelle [H] > [A-i] > [B] > [C] aux PRD des Vol. II, III, IV ; conditions de passage en [H] écrites une fois (PRD Vol. II §7) ; annexe A §A.9 du Vol. II ; 46 + 131 entrées vérifiées sans changement de niveau, aucune en [H] ; motif CA-11 du Vol. III adapté, mêmes lignes relevées sur 34 pièces.
- Déclaré : T5.1 non fermée — `RELECTURE.md` écrit (pièces remises avec SHA-256, pages imprimées, 9 + 7 énoncés à réfuter, gabarit de rapport, registre d'envoi) ; relecteurs à nommer (DA-4) et accusés de réception hors d'atteinte.
- Laissé : `Monographie.pdf` du Vol. II non recomposé (porte l'ancienne échelle) → à reprendre avec T7.1 ; « [A] » dans des `README` de M4.
- Coût : 507 k jetons, 140 appels, 43 min.

### M6 — critique (A = Agentique, B = barre)
- **Verdict : A.** `RELECTURE.md` dit quoi lire (pièces, correspondance folio / page PDF), quoi réfuter (T-1..T-9, V-1..V-7), comment rendre et sous quelles déclarations (indépendance, modèles de langage) ; empreintes, folios, bornes de parties et renvois rejoués sans écart ; niveaux appliqués à des entrées réelles conformes. La barre : guide générique de relecture, aucune déclaration d'outils, aucune valeur de l'approbation pour le lecteur.
- **Écart retenu (A)** : le `Monographie.pdf` du Vol. II que reçoivent le relecteur et le lecteur porte encore l'ancienne échelle (0 « A-i » sur 387 pages) ; la réforme n'existe qu'en source. Mineur : `CONTRIBUTIONS.md:196` écrit « [A] » sans incise.
- Suite : victoire, le morceau sort de la boucle. La recomposition du PDF du Vol. II rejoint T7.1 (vague C) ; le mineur va au lissage.
- Coût : 153 k jetons, 27 appels, 6 min.

### M4 — bâtisseur
- Déclaré : T3.1 (compendium « archive de travail, hors compte », section « Les sept livrables » avec registre statut / réserve / décision), T3.2 (bandeau du Vol. III en 9 lignes, R-G-43 à R-G-57, dette F-92/F-96 ; anciens bandeaux conservés mot pour mot en chronique), bandeaux D-17 (20 dans 13 `README`), carte du `README` — fermés ; 40 critères rejoués.
- **Écart au libellé du plan, déclaré** : T3.3 ouvre une décision **D-18** (« le compte des livrables est fixé par D-18 à sept »), D-17 disant ne prendre aucune des DA ; D-18 range hors compte la note SDLC, l'article, `NiveauMaturité.html`, l'appareil et la note de synthèse — **déduit de DA-2, non tranché par l'auteur**.
- Signalé : le Vol. I a été recomposé par M5 pendant la passe (569 → 570 p.) ; totaux de pages retirés de ses phrases, pagination tenue par la table détaillée.
- Coût : 424 k jetons, 186 appels, 52 min.

### M8 — bâtisseur
- Déclaré : critère tenu — `3 - Veille/Note de synthèse.md` et `.pdf`, 20 pages, 50 notices listées et citées, 200 renvois de section avec niveau de preuve ; `check-synthese.py` (sept contrôles, dont parité et 339 chiffres retrouvés dans les sections citées) et son harnais (22 mutations) sortent 0 ; étape de CI rejouée localement.
- Limites déclarées par le contrôle lui-même : un chiffre remplacé par un autre présent dans la même section, une paraphrase fausse sans chiffre ne sont pas vus. Parité sous Linux non mesurée avant la CI.
- Coût : 746 k jetons, 151 appels, 51 min.

### M4 — critique (A = barre, B = Agentique)
- **Verdict : B.** Un statut d'une ligne par document publié, avec « Fixé par » (D-18), retrouvé à l'identique dans les 14 `README` de dossier et de volume ; comptes rejoués concordants (8 PDF, 11 paginations, 50 pièces « non publiable », 15 remontées). La barre : versions citables discordantes entre `CITATION.cff`, `README.md`, `cite.md`, `release-drafter.yml` et les `README` traduits.
- **Écart retenu (B)** : le compte des documents publiés hors livrables ne concorde pas — « deux » à `README.md:9`, quatre au tableau `README.md:181-184` et à D-18, « trois » à la carte (`README.md:361-367`) et à `3 - Veille/README.md:18` ; `1 - Collection/1 - InteroperabiliteAgentique/README.md:18` dit encore le compendium « quatrième livrable » sans date ; `PRD.md:918` borne les décisions « de D-1 à D-17 ».
- Suite : victoire, le morceau sort de la boucle. Les discordances passent à la phase 4 (réécriture des `README`) comme contrainte, puis au lissage.
- Coût : 172 k jetons, 34 appels, 5 min.

### M5 — critères rejoués par l'orchestrateur
- T6.1 : `/Title` = « État de l’art en services financiers », `Creator: Typst 0.15.1`, 186 p. — tenu.
- T6.2 : `$` échappés en source ; au PDF, la notice [19] se lit « actif de 510,2 G$ » (p. 120) — tenu.
- T6.3 : `check-resume.py` → OK, dégagement +12,6 pt — tenu (fusion [1]/[198] déclarée, non recomptée).
- T6.5 : `check-vol1.py` → 0 ; harnais → 5 mutations vues — tenu.
- T6.6 : Vol. I `Creator: Typst 0.15.1`, **570 p.** (et non 569, redaté) — tenu ; cause du saut de page non isolée (bibliographie, p. 379).
- T6.7 : `rejeu-politique.py` → 37/37 ; `check-article.py` → 0 avec contrôle [6] ; harnais → 9 mutations vues — tenu.
- T6.4 : non rejoué (exige Pandoc) ; déclaré identique à l'octet pour la planche.
- Globaux : `check-renvois.py` → 227 `.md`, 2 184 renvois, 0 mort ; `appareil.yml` analysé.
- Signalés par M5, hors périmètre : `4 - Essais/1 - Traité/README.md:392` (« pas d'intégration continue ») ; `3 - Veille/README.md` dit l'état de l'art « cassé » ; harnais de l'article : une mutation compte comme vue quel que soit le contrôle qui échoue.
- Coût du bâtisseur : 546 k jetons, 257 appels, 56 min.
