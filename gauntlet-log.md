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

### M8 — critique (A = barre, B = Agentique)
- **Verdict : B.** La note dit ce qu'elle est et ce qu'elle ne garantit pas ; `check-synthese.py` rejoué à 0 ; sections citées conformes aux signets PDF des volumes ; une trentaine d'affirmations rouvertes tiennent au chiffre et à la date. La barre : aperçus sans source ni niveau de certitude, portées grossies (`pd-overview.md:29`).
- **Écart retenu (B)** : le 91,8 % de « L'essentiel » étiqueté « individuel » alors que sa source est une prépublication non révisée, quand le 40,55 %, de même régime, est « sans revue ». Relevés en plus : douze brouillons présentés comme un compte (la source dit un plancher) ; « supervision humaine démontrée nulle part » étiquetée « attestée » sur une seule notice ; audit du 8 août qui ne somme plus à 269 ; « aucune de ces échéances » étendu de quatre à six lignes ; désaccord interne du Vol. VI (400 M / un demi-milliard) non signalé.
- Suite : victoire à l'aveugle, mais les écarts sont des fautes d'exactitude dans un livrable de recherche : **reprise du même bâtisseur** (pas d'agent neuf) pour les corriger, sans nouveau critique — le lissage final vérifiera.
- Coût : 246 k jetons, 39 appels, 8 min.

## Vague B — phase 4
| Morceau | Tâches | Critique |
|---|---|---|
| **M7a — Pages d'accueil** | T4.1, T4.2, T4.4 ; discordances de comptes relevées sur M4 | à l'aveugle |
| **M7b — En-têtes du compendium** | T4.3, T4.5 | à l'aveugle |

## CI de la vague A
- Run `34993444546` sur `5cdb5bb` : **rouge** sur une étape, `decompte.sh --verifier` (Linux et Windows) — Vol. II à 93 939 jetons contre une ancre à 93 239. Cause : l'annexe A § A.9 et la note d'avant-propos ajoutées par M6 (T5.4), qui n'avait pas rejoué ce script. Ajout voulu, ancre périmée : redatée selon la convention du script (`0fdb21b`), `APPAREIL.md` suit. Fait par l'orchestrateur.

### M8 — reprise (même bâtisseur)
- Écarts du critique corrigés, tous confirmés à la relecture des sources ; élargi au 41,6 % et à la taxonomie MAST (même régime). Contrôle : [5] exige le régime des notices arXiv, nouveau [8] sur les sommes et parts ; 26 mutations.
- Rejoué par l'orchestrateur : `check-synthese.py` → 0 (huit contrôles), harnais → 26 au verdict attendu, 21 pages. Commit local `Note de synthèse : régime…`, poussé après la fin de la CI en cours.
- Coût : 805 k jetons cumulés (reprise : 22 appels, 9 min).
- CI verte au run `34993788011` sur `0fdb21b` : six tâches ; la parité de la note de synthèse et `check-vol1.py` tiennent sous Linux et Windows.
- CI verte au run `34995160645` sur `5d2b221` (reprise de la note).

### M7a — bâtisseur
- Déclaré : T4.1 (11 `JOURNAL.md` ; 6 057 lignes reçues, 5 821 identiques à l'octet, 236 ne diffèrent que par une cible de lien ; 3 570 phrases d'origine toutes retrouvées), T4.2 (18 `README` de 22 à 40 lignes, gras 0,9 à 2,9 %, aucun ⚠ ni ☑, statut D-18 conservé, quatre discordances de comptes résorbées), T4.4 (`check-lisibilite.py`, 15 mutations, deux étapes de CI) — fermées ; 37 contrôles et harnais à 0.
- Contrôles adaptés à la nouvelle forme, avec harnais : `check-toc.py` (C14), `check-article.py` (cardinaux, lus une seule fois), `reporter-volumetrie.py` (site 3, sans harnais, éprouvé sur copie).
- Coût : 686 k jetons, 177 appels, 49 min.

### M7a — critique (A = Agentique, B = barre)
- **Verdict : A.** Toutes les pages d'accueil tiennent en 30 à 40 lignes sur un même plan (objet, statut, par où entrer, refaire, journal) ; 361 liens relatifs sur 18 `README`, 0 rompu ; pages des 12 PDF, 470 tests, 30 rapports, 46 entrées, 159 entrées de socle, D-17 / D-18 vérifiés ; renvois vers les journaux et l'historique conformes. La barre : racine de 1 442 lignes dont 1 308 de contributeurs, sans état ni reconstruction, affirmations d'accueil fausses.
- **Écart retenu (A)** : `4 - Essais/1 - Traité/README.md:6` dit « deux » écarts contre le traité, alors que le registre cité (`docs/decisions.md:152`) en compte trois ; le reclassement n'est qu'au journal. Mineur : `4 - Essais/` n'a ni `README` ni `JOURNAL.md`.
- Suite : victoire, le morceau sort de la boucle. L'écart va au lissage.
- Coût : 153 k jetons, 27 appels, 6 min.

### M7b — bâtisseur
- Déclaré : **T4.5 fermée** — dégagement du résumé de +1,7 à +21,5 pt (notices des Livres I, II, V raccourcies, marge basse 26 → 33 mm) ; 1 000 pages tenues après re-mesure du pas (17,03 pt), les notes de collation de 14 pièces, absentes du HTML, ne s'imprimant plus.
- Déclaré : **T4.3 non fermée sur son seuil** — « premier `---` ≤ 8 lignes » est hors d'atteinte : un tableau Markdown de cinq rangées prend sept lignes, et la forme du PRD §6 (situation, tableau, thèse) place le premier `---` entre les lignes 16 et 21 (16 à 58 avant). **Défaut du critère du plan**, que l'orchestrateur a rédigé. Tient : cinq rangées exactement dans les 50 têtes, statut « archive de travail (D-18) », têtes de 425 248 à 104 394 octets (−75,5 %), 530 lignes retirées retrouvées mot pour mot en « Note de statut », corps identique à l'octet, `.html` régénérés identiques.
- Contrôles renforcés : P1 (forme de tête), P5 (tête contre détail), P6 (mesure publiée) ; `check-sieges.py` relit le bloc déplacé ; `reporter-volumetrie.py` adapté ; harnais à 30 et 115 mutations.
- Coût : 673 k jetons, 158 appels, 59 min.

### Vague B — contrôles rejoués par l'orchestrateur avant commit
- 20 commandes à 0 : `check-renvois.py` (238 `.md`, 2 770 renvois, 0 mort) et son harnais ; `check-lisibilite.py` et son harnais ; `check-compendium.py` (30 mutations), `check-sieges.py` (115), `check-toc.py` et harnais ; `decompte.sh --verifier` ; `genere.py --verifier` ; `check-article.py` (9 mutations) ; `check-veille.py`, `check-revue.py`, `check-synthese.py` ; `check-resume.py` sur `Compendium.pdf` (+21,5 pt) ; `check-traite.py` ; `check-vol1.py` ; `appareil.yml` analysé. `verifier-piece.py` laissé à la CI (Pandoc 3.11).
- Commit `fc33db1` poussé (phase 4).

## Vague C
- **M9 — Résumés en anglais** (T7.1, dont la recomposition du PDF du Vol. II que le critique de M6 a relevée) : lancé. Pas de critique à l'aveugle (la barre, anglophone, ne compare pas une traduction) ; la fidélité des résumés sera confrontée au français par la passe de lissage finale.
- **T7.3** (étiquette `corpus-v1.0`, DOI) : hors d'atteinte — suppose la re-clôture, donc la phase 5, et le compte Zenodo de l'auteur.
- **T7.4** (Git LFS) : **différée et soumise à l'auteur**. Le plan la place « à partir de la re-clôture » ; l'appliquer aujourd'hui ferait passer par LFS tous les PDF recomposés par M9, et la CI, qui doit alors extraire les objets LFS à chaque passage sur deux systèmes, consommerait le quota de bande passante LFS du compte GitHub.

### M7b — critique (A = barre, B = Agentique)
- **Verdict : B.** Chaque pièce donne son état en cinq rangées dès la tête ; têtes concordantes avec la mesure (`decompte.sh` et `--registre`, 50/50), le registre de gel (50/50), les `README` de Livre (5/5), D-18 ; détail en fin de pièce identique à la tête d'avant `fc33db1` (50/50). La barre : aucun régime d'état par pièce, pièces inachevées signalées en pied ou pas du tout.
- **Écart retenu (B)** : l'état n'existe que dans le `.md` — le rendu retire la tête (`build/rendre-piece.py:17-19`) : 49 `.html` sur 50 et le `Compendium.pdf` de 1 000 pages ne disent nulle part, en tête, qu'il s'agit d'une archive non publiable ; des paragraphes d'appareil rendus renvoient à une « thèse citée ci-dessus » absente (ch. 19, 25, 27, 48, 49). Mineurs : ch. 01 à v0.23 contre un TOC à v0.36 ; « −1,3 % » là où le calcul donne −0,6 %.
- Suite : victoire, mais l'écart touche B2 (un PDF non publiable qui ne le dit pas) : **reprise du même bâtisseur**, sans agent neuf.
- Coût : 181 k jetons, 47 appels, 10 min.
- CI verte au run `35000614181` sur `fc33db1` (phase 4), dont `verifier-piece.py` sous Pandoc 3.11 et `check-lisibilite.py`.

### M7b — reprise (même bâtisseur)
- Statut au rendu : rangée « Statut » en tête des 50 pièces rendues, avis du volume en p. 2 du PDF ; `verifier-piece.py` [4] l'exige (8 mutations). Renvois « ci-dessus » : antérieurs (`5cdb5bb`), tenus par la thèse rendue. Défaut trouvé : Pandoc lisait [A]/[B]/[C] comme des citations (754 crochets effacés), corrigé. Mineurs v0.23 et −1,3 % : relevés datés, non corrigés, motif écrit.
- **Décision soumise à l'auteur** : le gabarit porte une consigne du 30 juillet 2026, « aucun statut au colophon » (régime D-10) ; l'avis est hors colophon et n'ajoute aucune page, mais l'auteur dit s'il rouvre la consigne.
- Rejoué par l'orchestrateur : pymupdf → 1 000 p., avis en p. 2, « non publiable » × 53 ; `check-compendium.py`, `check-sieges.py`, `check-toc.py`, `genere.py --verifier`, `check-resume.py`, `check-renvois.py` → 0. `decompte.sh --verifier` en échec sur l'arbre de travail à cause des modifications en cours de M9 au Vol. I (signalé à M9) ; tenu sur HEAD.
- Coût : 779 k jetons cumulés (reprise : 77 appels, 26 min).
- CI verte au run `35004194048` sur `8e2feab` (statut au rendu du compendium ; `verifier-piece.py` [4] sous Pandoc 3.11).

### M9 — bâtisseur
- Déclaré : résumé anglais sous le français dans dix documents (Vol. I, II, III, V, VI, VII, VIII, note SDLC, note de synthèse, article), page « Abstract » après la page de titre, sans folio (sources YAML) ou en chiffres romains (Vol. I-III) — aucun folio cité ne bouge ; Vol. II recomposé avec l'échelle [H] > [A-i]. Exclus : la planche et `NiveauMaturité.html` (sans résumé français), le compendium (consigne), le mémoire de 1997 (pièce déposée).
- `decompte.sh` : le résumé sort du périmètre mesuré (Vol. I par `inject-pagination.py`), ancres inchangées. `check-traite.py` : `MOTS_REF` recalé avec note datée. Nouvelles empreintes SHA-256 dans `RELECTURE.md`.
- Non tenu : `check-resume.py` sur l'article (1 avant comme après ; inapplicable déclaré, folio arXiv sous la marge). Note de synthèse à 22 p., borne haute de son critère.
- Rejoué par l'orchestrateur : pymupdf → Abstract en p. 2 ou 3 des neuf PDF, pages 571 / 390 / 428 / 144 / 145 / 60 / 187 / 22 / 50, 7 « A-i » au Vol. II ; `check-resume.py` → 0 sur les huit applicables ; batterie de 17 contrôles et harnais → 0 (renvois 2 794 / 0 mort, lisibilité, compendium, `decompte.sh`, `genere.py`, veille, revue, synthèse et 26 mutations, traité, article et 9 mutations, rejeu 37/37, Vol. I et 5 mutations).
- Coût : 577 k jetons, 160 appels, 50 min.
