# Plan d'exécution — mise en œuvre de l'évaluation académique du 15 septembre 2026

*Ce plan transforme les constats (§8), les corrections requises (§11.1) et les bonifications (§11.2)
de l'[`Évaluation académique.md`](<%C3%89valuation%20acad%C3%A9mique.md>) en tâches ordonnées,
chacune avec son critère d'acceptation vérifiable. Il ne planifie pas les projets futurs (§11.3) :
ce sont des travaux de recherche, pas des corrections. Il est une proposition ; six décisions
d'auteur le conditionnent, et elles sont nommées en premier.*

✎ *État d'exécution au 15 septembre 2026, commit `730c68e`, CI verte : décisions DA-1 à DA-7
prises le jour même aux défauts, sauf DA-6 en (b) ; DA-4 reste ouverte. Phases 0 à 4 et 6, T5.4,
T7.1 et T7.2 exécutées ; D-17 rouvre le dépôt et D-18 fixe le compte des livrables. T5.1 à T5.3
attendent les relecteurs, T7.3 et T7.4 la re-clôture ; la phase 8 n'est pas entreprise, sa
condition n'étant pas remplie. Le détail, tâche par tâche et verdict par verdict, est au
[journal de boucle](gauntlet-log.md).*

## 0. Régime du plan

| Règle | Application |
|---|---|
| **Une tâche = un critère d'acceptation exécutable** | chaque ligne porte la commande ou le constat sur pièce qui la ferme ; « fait » se lit à la sortie, pas au récit — c'est la règle CA-IV-14 du dépôt, retournée sur le plan |
| **Rien ne se ferme par amputation d'un fait daté** | une phrase qui date un fait garde l'ancien nom ; seuls les renvois actifs et les commandes bougent — règle du dépôt, et leçon du journal de boucle du 5 septembre |
| **Toute passe rouvre la clôture et le déclare** | le PRD §16.4.5 l'exige ; la première tâche du plan est d'ouvrir une décision d'auteur qui le fasse une fois pour toutes |
| **Effort** | en jours-personne de l'auteur (j-p), estimés, arrondis au demi-jour ; les tâches qui exigent un tiers portent « tiers » et un délai calendaire au lieu d'un effort |
| **Qui** | **A** l'auteur seul ; **A+I** l'auteur avec ses instances de modèle, sous les règles du dépôt ; **T** un tiers humain nommé |
| **Priorité** | **P0** lève une condition bloquante de l'évaluation ; **P1** rendement élevé sur le verdict ; **P2** correction locale ; **P3** consolidation |

## 1. Décisions d'auteur requises avant d'exécuter

Aucune n'est prise ici ; le plan propose une option par défaut et dit ce qu'elle coûte.

| # | Décision | Options | Défaut proposé | Ce qu'il conditionne |
|---|---|---|---|---|
| **DA-1** | Réouverture du dépôt clos | *(a)* une décision **D-17** rouvre le dépôt pour la durée du plan, avec date de re-clôture ; *(b)* chaque passe déclare sa propre réouverture | **(a)** — une réouverture déclarée une fois vaut mieux que quatorze chroniques | toutes les phases |
| **DA-2** | Sort du Vol. IV | *(a)* **archive de travail** : sort du compte des livrables, reste au dépôt, `README` le dit ; *(b)* **achèvement** : ré-adossement des 524 renvois aux `S-nnn`, relecture des 50 pièces, levée des dérogations | **(a)** — (b) est une passe de rédaction de plusieurs semaines sur un volume que le dossier lui-même dit non réconcilié | B2 ; phase 3 ; toutes les tables de comptes |
| **DA-3** | Statut du Vol. III | *(a)* livrable **sous réserve déclarée** — les quinze remontées et la dette de vote listées en tête ; *(b)* même sort que le Vol. IV | **(a)** — le volume est complet, relu, et ses réserves sont écrites | B2 ; phase 3 |
| **DA-4** | Relecteurs humains | qui, sur quoi, avec quel budget ; un spécialiste des systèmes répartis sur le traité, un juriste du droit financier canadien sur les ch. 9 à 13 du Vol. II | à nommer | B1 ; phase 5 |
| **DA-5** | Les trois PDF `-critique` / `-essai` de `5 - Recension/` | *(a)* retirer de l'index ; *(b)* garder et documenter comme sorties d'une boucle bâtisseur / critique | **(a)** — ce sont des rendus de travail ; ce qu'ils ont produit est dans les `README` réécrits | phase 0 |
| **DA-6** | L'article HPC-QPU | *(a)* dépôt propre, avec les artefacts du mémoire que le colophon annonce ; *(b)* reste sous `4 - Essais/2 - Article/` | **(a)** — il n'instruit pas la question du dossier, et son dépôt d'origine porte ce que le lecteur voudra vérifier | phase 6, T6.8 |
| **DA-7** | Git LFS pour les PDF | *(a)* migration de l'historique (`git lfs migrate`, réécrit tous les SHA) ; *(b)* LFS à partir de maintenant seulement ; *(c)* rien | **(b)** — (a) casse tous les renvois `commit` du dossier, qui sont des faits datés | phase 7, T7.4 |

## 2. Phases et tâches

### Phase 0 — Remise en état de l'arbre évalué *(P0, 1,5 j-p, aucune dépendance)*

Ferme les constats §8.1 à §8.7 et la correction R5. Tout se rejoue depuis le dossier indiqué.

| # | Tâche | Source | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|---|
| T0.1 | Ouvrir **D-17** au PRD du compendium (annexe A) : réouverture pour exécution du plan, date de re-clôture, périmètre | DA-1 | la décision est au PRD, datée, avec sa condition de réouverture ; `check-toc.py` et `check-compendium.py` sortent 0 | 0,5 | A |
| T0.2 | Réancrer les trois empreintes `ANTERIEURES` de `figures/genere.py` sur les octets LF — ou hacher après `.replace(b"\r\n", b"\n")` pour rendre le registre indifférent aux fins de ligne | §8.1, R3 | `python figures/genere.py --verifier` → **0** sur l'arbre normalisé **et** sur une copie repassée en CRLF | 0,5 | A |
| T0.3 | Ajouter `sys.stdout.reconfigure(encoding="utf-8")` à `figures/genere.py` — et à tout script du dépôt qui imprime ⚠ ☑ et ne l'a pas | §8.1 | `python figures/genere.py --verifier` sort **0 sans `PYTHONUTF8`** sur console cp1252 ; `grep -L reconfigure` sur les `.py` qui contiennent `⚠` rend vide | 0,25 | A |
| T0.4 | Écrire `newline="\n"` aux `open(…, "w")` de `4 - Essais/1 - Traité/figures/contenu.py`, `1 - Collection/2 -…/build/assemble.py`, `1 - Collection/3 -…/build/assemble.py` | §8.3, R3 | rejouer les trois ; `git status --porcelain` **vide** sans `--ignore-cr-at-eol` | 0,25 | A |
| T0.5 | Appliquer **DA-5** aux trois PDF de `5 - Recension/` | §8.2, R5 | `git ls-files | grep -c 'critique\|essai\.pdf'` → 0, ou un paragraphe du `README` de `5 - Recension/` les nomme avec leur provenance | 0,25 | A |
| T0.6 | Réaligner `README.md` et `APPAREIL.md` de la racine sur l'arbre : la ligne « 78 / 100 » de la table d'entrée pointe la nouvelle évaluation à son total ; les cinq renvois résolvent ; la mention de la clôture porte la date que le critère du dépôt donne | §8.2, R5 | résolveur de renvois sur les `.md` de la racine → 0 mort ; la table d'entrée cite « 75,5 / 100 » et le `Gabarit` | 0,5 | A |
| T0.7 | Mettre `APPAREIL.md` au niveau du rejeu du 15 septembre : P1-P10 et 5 rapports, C1-C16, 114 et 23 mutations, 470 tests, `verifier-piece.py` et `check-article*.py` aux tableaux, l'alerte « LIMITE 1,7 pt » du Compendium, la réserve « 35,5 / 36 » du rejeu | §8.4, §8.5, §8.6 | chaque chiffre de la page est celui d'une commande rejouée le jour de la passe, et la page dit la date | 0,5 | A |
| T0.8 | Corriger les trois renvois morts vers `2 - Compendium/audit.md` (PRD ×2, TOC ×1) par un renvoi au commit `60e1b99` qui l'a supprimé | §8.7 | résolveur sur les 219 `.md` → **0 mort** | 0,25 | A |
| T0.9 | Constats mineurs : `repository` du `Cargo.toml` → ce dépôt ; phrase « aucune licence » de `docs/README.md` du traité ; chemin `mingw64` du `README` sous une variable `$WINLIBS` et non sous `C:\Users\agbru` | §8.7 | `grep -c Stigmergie Cargo.toml` → 0 ; `grep -c 'aucune n.est déclarée' docs/README.md` → 0 ; `grep -c 'Users.agbru' README.md` → 0 | 0,25 | A |

**Sortie de phase** : les dix-neuf contrôles du §3.2 de l'évaluation rejoués sortent 0, sauf `check-resume.py` sur l'article et `check-empaquetage.py` sans cible, tous deux documentés ; `git status` propre ; B3 levée.

### Phase 1 — Intégration continue *(P1, 2 j-p, dépend de la phase 0)*

Ferme la bonification 1 ; tient NF-13 et NF-16 ; empêche le §8.1 de se reproduire.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T1.1 | `.github/workflows/appareil.yml` — matrice `ubuntu-latest` × `windows-latest` : `cargo test / clippy / fmt --check` depuis `4 - Essais/1 - Traité/` avec `CARGO_TARGET_DIR` hors arbre | le flux est vert sur les deux systèmes au premier commit qui le porte | 0,75 | A |
| T1.2 | Même flux : les cinq contrôles de document, les quatre harnais de mutation, `verifier-piece.py`, `genere.py --verifier`, `rejeu-politique.py`, `check-article.py`, `decompte.sh --verifier`, chacun depuis son dossier, `PYTHONUTF8=1` | vert ; un `git revert` d'essai sur une figure gelée fait échouer le flux | 0,5 | A |
| T1.3 | Contrôle de renvois Markdown versionné — `Python/check-renvois.py` à la racine, règle de l'évaluation : cibles relatives décodées, blocs et *spans* de code exclus | sort 0 sur l'arbre ; harnais : un renvoi cassé injecté est vu | 0,5 | A |
| T1.4 | Contrôle de fins de ligne : `git ls-files --eol | grep -c 'w/crlf'` → 0, en tâche du flux | vert | 0,25 | A |
| T1.5 | Badge de statut du flux en tête du `README.md` ; `APPAREIL.md` dit que les contrôles tournent en CI et lesquels ne tournent pas encore (chaînes Pandoc, WASM, bancs) | le badge est vert ; la liste des non-couverts est écrite | 0,25 | A |

**Sortie de phase** : NF-13 et NF-16 du PRD du simulateur passent de « mécanisme absent » à « tenu par le flux » ; un tiers voit le verdict sans exécuter.

### Phase 2 — Attribution et gouvernance *(P0, 1,5 j-p, indépendante)*

Ferme B4 et la critique de fond n° 5.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T2.1 | `CONTRIBUTIONS.md` à la racine : une ligne par pièce — auteur humain, agents de modèle et leur rôle (recherche, rédaction, relecture, vérification), relecteurs humains (aucun à ce jour), outils — au modèle CRediT adapté ; les vingt commits signés `Claude` y sont rattachés à leurs pièces | chaque document publié a sa ligne ; `git log --author=Claude --name-only` ne rend aucun fichier absent du tableau | 0,75 | A |
| T2.2 | Remplacer « les textes sont d'une seule main » par une phrase exacte — responsabilité éditoriale unique, rédaction assistée déclarée en `CONTRIBUTIONS.md` — dans `README.md` de la racine et là où la formule se répète | `grep -rc "d'une seule main" --include=*.md .` → 0 hors les citations datées | 0,25 | A |
| T2.3 | Traçabilité des pièces supprimées : un `ARCHIVES.md` qui liste chaque pièce sortie du dépôt — trois `audit.md`, deux journaux de boucle, l'évaluation du 5 septembre, le démonstrateur, l'article de synthèse — avec le commit qui la contient et la commande `git show` qui la relit | chaque ligne se rejoue ; les renvois du corps qui visaient ces pièces pointent la ligne | 0,5 | A |

### Phase 3 — Trancher les livrables *(P0, 1 j-p avec DA-2 (a) ; plusieurs semaines avec (b) ; dépend de DA-2, DA-3)*

Ferme B2 et la critique de fond n° 2.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T3.1 | Appliquer **DA-2** : *(a)* le `README` du compendium ouvre sur « archive de travail, hors compte des livrables », la table des huit documents de la racine passe à sept et le dit, la décision est au PRD ; *(b)* passe de ré-adossement `F-xx`/`H-xx` → `S-nnn` sur les cinquante pièces, `check-compendium.py` gagne un contrôle P11 « aucun `F-xx` nu au corps », relecture des cinquante pièces au régime CA-IV-13 | *(a)* le compte est le même dans les dix-huit `README` (`grep -c 'huit documents'` → 0 hors faits datés) ; *(b)* P11 → 0 et les cinquante en-têtes ne portent plus « non publiable » | (a) 0,5 ; (b) 15 à 25 | A / A+I |
| T3.2 | Appliquer **DA-3** au Vol. III : bandeau de tête qui liste les quinze remontées ouvertes et la dette de vote comme réserves de lecture, en dix lignes, à la place des chroniques | le bandeau tient sur un écran ; `remontees-gouvernance.md` reste la source et le bandeau y renvoie | 0,5 | A |
| T3.3 | Mettre le compte des livrables sous décision d'auteur : une ligne au PRD — « le compte des livrables est fixé par D-17 à N ; toute entrée ou sortie passe par une décision » | la phrase « constat, pas décision » disparaît des `README` hors faits datés | 0,25 | A |

### Phase 4 — Lisibilité de l'appareil *(P1, 6 à 8 j-p, dépend des phases 0 et 3)*

Ferme la bonification 2 et la critique de fond n° 3 ; agit sur C7 et C8, les deux critères à 60 %.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T4.1 | Un `JOURNAL.md` par dossier numéroté qui reçoit, sans les réécrire, les chroniques datées des `README` — réouvertures, redatations, corrections de corrections | `diff` ligne à ligne : aucune phrase de chronique perdue ; les `README` n'en portent plus | 2 | A+I |
| T4.2 | Réécrire les dix-huit `README.md` à **quarante lignes au plus** : ce que le dossier porte, par où entrer, comment refaire, où est le journal ; aucun ⚠ ni ☑ dans la prose d'accueil ; gras réservé aux titres courants | `wc -l` ≤ 40 par `README` ; densité de gras < 5 % ; ⚠ → 0 hors tables de contrôle | 2 | A+I |
| T4.3 | En-têtes des cinquante pièces du compendium ramenés à un tableau de **cinq lignes** — statut, gel, socle, garde-fous, volumétrie —, le reste déplacé en « Note de statut » en fin de pièce | `awk` sur la position du premier `---` : ≤ 8 lignes ; `check-compendium.py` et `verifier-piece.py` → 0 après régénération des `.html` | 1,5 | A+I |
| T4.4 | `Python/check-lisibilite.py` à la racine : densité de gras, compte de ⚠, longueur des `README`, avec seuils ; en CI | sort 0 sur l'arbre réécrit ; harnais : un `README` de 41 lignes est vu | 0,5 | A |
| T4.5 | Résumé du `Compendium.pdf` condensé de deux lignes ; recomposition ; calage re-mesuré | `check-resume.py` → dégagement ≥ 12 pt ; 1 000 p. tenues ou la cible est retirée du script sur décision | 0,5 | A |

**Sortie de phase** : un lecteur ouvre n'importe quel `README` et lit ce qu'il y a en une page ; la chronique existe entière, ailleurs.

✎ *Erratum du 15 septembre 2026, constaté à l'exécution : le seuil de T4.3, « premier `---` à
huit lignes au plus », est intenable. Un tableau Markdown de cinq rangées prend à lui seul sept
lignes, et la forme de tête du PRD du compendium (§ 6 : situation, tableau, thèse) place ce filet
entre les lignes 16 et 21. Le critère tenu à sa place : cinq rangées exactement dans les cinquante
têtes, le détail retiré retrouvé mot pour mot en note de statut, `check-compendium.py` (P1, P5, P6)
et `verifier-piece.py` à 0.*

### Phase 5 — Relecture humaine externe *(P0, tiers ; 6 à 10 semaines calendaires ; dépend de DA-4 et de la phase 4 pour le Vol. II)*

Ferme B1 et la critique de fond n° 1. C'est la seule phase qu'aucune passe instrumentée ne remplace.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T5.1 | Nommer les relecteurs (DA-4), leur remettre le traité (PDF, 4ᵉ éd.) et les ch. 9 à 13 du Vol. II avec une consigne écrite : réfuter, sur pièce, avec renvoi de page | consigne versionnée ; accusés de réception datés | 0,5 + tiers | A, T |
| T5.2 | Recevoir les rapports, les verser sous `verification/relecture-externe-<nom>-<date>.md` de chaque pièce, **sans les éditer** | rapports versionnés, signés, datés ; `CONTRIBUTIONS.md` mis à jour | tiers, 4 à 8 semaines | T |
| T5.3 | Appliquer les réfutations retenues, consigner celles refusées avec motif, au registre de la pièce ; recomposer ; nouvelle édition datée | chaque réfutation a une issue écrite ; `check-traite.py` → 0 ; parité du PDF | 2 à 4 | A |
| T5.4 | Réformer la hiérarchie des niveaux de preuve dans les PRD des Vol. II, III et IV : **[A]** devient **[A-i]** — « réfutation tentée par trois instances de modèle, aucune n'y est parvenue » — et un niveau **[H]** — « lu et non réfuté par un relecteur humain nommé » — prend la tête ; l'annexe A du Vol. II explique le renversement | les trois PRD portent la nouvelle échelle ; les entrées touchées par T5.3 passent en **[H]** ; aucune autre entrée ne change de niveau | 1 | A |

**Sortie de phase** : au moins un énoncé central d'au moins deux pièces porte **[H]** ; B1 levée.

### Phase 6 — Corrections locales *(P2, 2,5 j-p, dépend de la phase 0)*

Ferme la bonification 5 et les réserves des fiches.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T6.1 | `/Title` de `État de l'art — services financiers.pdf` : post-traiter le PDF (`pymupdf`, `set_metadata`) dans `build/build-pdf.sh` de `5 - Recension/`, ou corriger `content-to-string` du gabarit pour connaître `smartquote` | `python -c "import pymupdf;print(pymupdf.open(p).metadata['title'])"` rend l'apostrophe ; les six PDF à `conf` passent le même test | 0,5 | A |
| T6.2 | Notice [19] de l'état de l'art : échapper les `$` ; recomposer | la notice se lit au PDF ; pagination inchangée ou redatée | 0,25 | A |
| T6.3 | Doublon [1] / [198] de l'état de l'art : fusionner en une notice, renuméroter ou marquer [198] « voir [1] » | le compte des références est unique ; `check-resume.py` → 0 | 0,25 | A |
| T6.4 | Versionner la feuille de style des `.html` de `5 - Recension/` en `build/recension.css` ; `build-pdf.sh` la passe en `--css` | les deux `.html` se refont depuis le dépôt seul, identiques modulo horodatage | 0,5 | A |
| T6.5 | Un contrôle propre au Vol. I — `Python/check-vol1.py` : pagination 569, appariement des sept bibliographies avec le corps, parité du PDF hors horodatage | sort 0 ; harnais : une notice orpheline injectée est vue ; en CI | 0,75 | A |
| T6.6 | Rejouer `build/build-pdf.sh` du Vol. I sous Typst 0.15.1 ; recomposer ; redater | `Creator: Typst 0.15.1` ; 569 p. tenues ou redatées | 0,25 | A |
| T6.7 | `rejeu-politique.py` : ajouter un verdict d'étalonnage en entrée et une assertion sur la branche « sinon → G » ; corriger « 36/36 » en « 36 cases, 37 transitions exercées » dans les `README` et `APPAREIL.md` | le script rend « 37/37 » ; `check-article.py` → 0 ; `check-article-mutations.py` gagne une mutation sur la branche G | 0,5 | A |
| T6.8 | Appliquer **DA-6** à l'article | *(a)* dépôt propre créé, renvoi depuis `4 - Essais/`, artefacts du mémoire versionnés là ; *(b)* rien | (a) 1 | A |

### Phase 7 — Consolidation et citabilité *(P3, 5 à 12 j-p, dépend des phases 3 à 5)*

Ferme les bonifications 3 et 4.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T7.1 | Résumé en anglais en tête de chaque livrable (YAML `abstract-en`, rendu sous le français) | douze PDF recomposés, `check-resume.py` → 0 sur chacun | 1,5 | A+I |
| T7.2 | **Note de synthèse** de vingt pages qui remplace, pour le lecteur pressé, la veille, la revue et l'état de l'art — thèses, chiffres porteurs, questions ouvertes, avec renvoi de section vers chacun ; ou fusion des trois en un document à trois parties (DA à ouvrir si la fusion est retenue) | la note existe, 20 p. ± 2, bibliographie close, un contrôle la garde | 3 (note) / 8 à 10 (fusion) | A+I |
| T7.3 | Étiquette annotée `corpus-v1.0` sur le commit de re-clôture ; dépôt Zenodo ; DOI en tête du `README` et de chaque livrable | `git tag -n corpus-v1.0` rend la note ; le DOI résout | 0,5 | A |
| T7.4 | Appliquer **DA-7** : Git LFS pour `*.pdf` à partir de la re-clôture | `git lfs ls-files` liste les PDF entrés depuis ; `.gitattributes` porte la règle ; l'historique antérieur n'est pas réécrit | 0,5 | A |

### Phase 8 — Séparer l'appareil du corpus *(P3, facultative, 2 j-p, dépend de la phase 4)*

Ferme la bonification 8. À n'entreprendre que si la phase 4 ne suffit pas au lecteur.

| # | Tâche | Critère d'acceptation | Effort | Qui |
|---|---|---|---|---|
| T8.1 | Un dossier `appareil/` à la racine reçoit `APPAREIL.md`, les scripts de contrôle transversaux, les journaux ; les `build/` restent chez leurs documents | le lecteur du corpus ne rencontre aucun script en ouvrant un dossier numéroté ; `check-renvois.py` → 0 | 2 | A |

## 3. Ordonnancement

```
semaine  1 : Phase 0 ──► Phase 1 ──► Phase 2
             (DA-1, DA-5 prises)      │
semaine  2 : Phase 3 (DA-2, DA-3) ────┤──► Phase 6 (T6.1 à T6.7)
                                      │
semaines 3-4 : Phase 4 ───────────────┤
                                      │
semaines 3-10 : Phase 5 (DA-4, tiers) ┤   ← chemin critique : le calendrier des relecteurs
                                      │
semaines 8-12 : Phase 7 (après T5.3) ─┘──► re-clôture, corpus-v1.0, nouvelle évaluation
Phase 8 : hors chemin, à la demande
```

Le **chemin critique** est la phase 5 : aucune tâche de l'auteur ne raccourcit le délai d'un
relecteur. Les phases 0 à 4 et 6 se font pendant qu'il lit ; la phase 7 attend ses conclusions,
puisqu'un résumé en anglais et un DOI figent un texte qu'une réfutation peut encore changer.

## 4. Effort total

| Bloc | Effort auteur | Délai |
|---|---|---|
| Phases 0, 1, 2 — remise en état, CI, attribution | 5 j-p | semaine 1 |
| Phase 3 avec DA-2 (a) | 1 j-p | semaine 2 |
| Phase 3 avec DA-2 (b) | 15 à 25 j-p | 4 à 6 semaines |
| Phase 4 — lisibilité | 6 à 8 j-p | semaines 3-4 |
| Phase 5 — relecture externe | 3 à 5 j-p, **plus le temps des tiers** | 6 à 10 semaines |
| Phase 6 — corrections locales | 2,5 à 3,5 j-p | semaine 2 |
| Phase 7 — consolidation | 5 à 12 j-p | semaines 8-12 |
| **Total, défauts proposés** | **23 à 35 j-p** | **≈ 12 semaines** |

## 5. Critères de sortie du plan

Le plan est fermé quand une nouvelle évaluation, conduite selon le même gabarit, constate :

1. **B1 levée** — au moins deux pièces portent des énoncés centraux en **[H]**, rapports de relecture versionnés et signés ;
2. **B2 levée** — aucune pièce comptée parmi les livrables ne se déclare non publiable ; le compte est fixé par décision ;
3. **B3 levée** — les dix-neuf contrôles sortent 0 en CI sur Linux et Windows ; `git status` propre après tout rejeu ;
4. **B4 levée** — `CONTRIBUTIONS.md` couvre chaque pièce ;
5. **C7 et C8** remontent au moins à *Très bien* — `check-lisibilite.py` à 0, `README` ≤ 40 lignes, gras < 5 % dans l'appareil d'accueil ;
6. un commit étiqueté `corpus-v1.0`, un DOI, et une clôture datée de ce commit, non rouverte depuis.

Total attendu si les six tiennent : au-dessus de 85, catégorie **accepté sous corrections mineures**
ou **tel quel** selon ce que les relecteurs auront trouvé — c'est eux, et non ce plan, qui décident
du dernier point.

## 6. Ce que le plan ne fait pas

- Il ne planifie aucun des dix **projets futurs** du §11.3 : mesurer un essaim réel, une flotte, décomposer Φ_c, démontrer la borne spectrale, prototyper la chaîne de mandat, enquêter sur le terrain, écrire l'article court, le banc E-23, la revalidation semestrielle, la réplication tierce. Ce sont des travaux de recherche à budget propre.
- Il ne touche pas au **contenu** d'aucune pièce hors T5.3 et T6.2-T6.3 : la matière doctrinale n'est pas en cause.
- Il ne décide pas des sept **DA** ; il les nomme et propose un défaut.
- Il ne promet pas le total du §5 : il promet que les conditions bloquantes tombent.
