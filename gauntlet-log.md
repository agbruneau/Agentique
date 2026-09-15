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
