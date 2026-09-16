# Contributions — qui a fait quoi, pièce par pièce

*Déclaration établie le 15 septembre 2026 (tâche T2.1 du [plan d'exécution](<Plan%20d%27ex%C3%A9cution%20%E2%80%94%20%C3%A9valuation%20acad%C3%A9mique.md>),
condition B4 de l'[évaluation](<%C3%89valuation%20acad%C3%A9mique.md>)). Elle distingue ce que l'historique
git atteste, ce que les pièces déclarent d'elles-mêmes, et ce qui n'a laissé aucune trace. Chaque
chiffre se rejoue par une commande du §7. Les pièces sorties du dépôt sont au
[`ARCHIVES.md`](ARCHIVES.md).*

**En une phrase.** Un seul humain répond de tout le dépôt ; la rédaction, la recherche documentaire,
la relecture et la vérification sont assistées par des agents de modèle d'Anthropic, qui co-signent
**173 des 328 commits** et en signent **20** ; **aucun relecteur humain** n'a lu une pièce à ce jour.

⚠ *Jusqu'au 15 septembre 2026, le `README.md` de la racine écrivait
« les textes sont d'une seule main ».
La responsabilité l'est ; la rédaction ne l'est pas. La phrase renvoie désormais ici.*

## 1. Les contributeurs

| Contributeur | Nature | Trace dans l'historique | Période | Rôles (§2) |
|---|---|---|---|---|
| **André-Guy Bruneau** | humain, auteur | 306 commits sous `André-Guy Bruneau` ; 2 sous `agbruneau`, co-signés Opus 5 et issus d'une session Claude Code (`Claude-Session`) ; fusionne les *pull requests* #1, #2, #3 et #5, ouvertes depuis des branches `claude/*` | 24 juin → 15 sept. 2026 | CONC, RESP ; tout rôle sur ses commits sans trailer (§6) |
| **Claude Fable 5** (Anthropic) | agent de modèle | 46 commits co-signés (`Co-Authored-By`) | 3 juil. → 19 août 2026 | RED, REL, VER, RECH, CONC sous instruction |
| **Claude Opus 4.8** (Anthropic) | agent de modèle | 28 commits co-signés | 18 → 23 juil. 2026 | RED, RECH, VER, LOG, VIS |
| **Claude Opus 5** (Anthropic) | agent de modèle | 97 commits co-signés, dont 16 sous l'identité `Claude` et 2 sous `agbruneau` | 27 juil. → 5 sept. 2026 | RED, REL, VER, LOG, VIS |
| **Claude Sonnet 5** (Anthropic) | agent de modèle | 1 commit co-signé (`42e223c`) | 11 août 2026 | REL |
| **Claude Fable 5.1** (Anthropic) | agent de modèle | 1 commit co-signé (`05fcc84`) ; auteur déclaré de l'évaluation du 15 septembre 2026, commitée sans trailer | 2 → 15 sept. 2026 | VER |
| **`Claude <noreply@anthropic.com>`** | identité d'agent, modèle non nommé par l'identité | 20 commits (§5) : 16 co-signés Opus 5, 1 Fable 5, **3 sans trailer** ; 17 portent un trailer `Claude-Session` (session Claude Code sur le web) | 27 juil. → 3 sept. 2026 | RED, LOG, REL |
| **Agents de la boucle du 15 septembre 2026** — Claude Opus 5 | agents de modèle : un orchestrateur, trois bâtisseurs (M1 scripts et CI, M2 `README` et `APPAREIL`, M3 attribution et traçabilité), des critiques indépendants | aucun commit à la rédaction de cette page ; journal `gauntlet-log.md`, non suivi par git ; ✎ le travail et le journal entrent le jour même au commit `78ebf9c`, signé André-Guy Bruneau sans trailer ; ✎ la boucle se poursuit le même jour — passe de lissage, correctif de la CI, puis six bâtisseurs de plus, M4 à M9, et leurs critiques, au même journal —, et ces travaux entrent aux huit commits `e6eec1d` à `91ddce6`, tous co-signés Opus 5 [G] | 15 sept. 2026 | LOG, REL, VER — et la rédaction de cette page et d'`ARCHIVES.md` ; ✎ l'après-midi, RED de la note de synthèse, de `RELECTURE.md` et des résumés anglais (§3) |
| **Relecteurs humains** | — | **aucun à ce jour.** La décision d'auteur DA-4 du plan, qui doit les nommer, n'est pas prise. ✎ *Le 16 septembre 2026, l'auteur déclare la relecture complétée, sans rapport versable ni relecteur nommé au dépôt (décision D-19) : aucune pièce n'a de relecteur humain vérifiable, aucune entrée n'est en [H]* | — | — |

Un agent de modèle n'est pas porté auteur : il ne répond pas du texte. Il est déclaré, avec son rôle
et la preuve de ce rôle.

## 2. Les rôles, et ce qui les prouve

Taxonomie adaptée de CRediT (ANSI/NISO Z39.104-2022) au dépôt :

| Code | Rôle | CRediT |
|---|---|---|
| CONC | conception : question, plan, décisions d'auteur (D-n, DT-n, DA-n) | *Conceptualization* |
| RESP | responsabilité éditoriale : ce qui entre au dépôt, ce qui en sort | *Supervision*, *Project administration* |
| RECH | recherche documentaire : socles, lots, sources primaires, références | *Investigation*, *Data curation* |
| RED | rédaction d'un premier état | *Writing – original draft* |
| REL | relecture et révision : langue, cohérence, alignement des `README` | *Writing – review & editing* |
| VER | vérification : audits, vérification adverse, contrôles rejoués | *Validation* |
| LOG | logiciel : simulateur, contrôles, chaînes de rendu, *skills* et consignes d'agent | *Software* |
| VIS | figures et composition des rendus | *Visualization* |

| Marque | Degré de preuve |
|---|---|
| **[G]** | attesté par git : trailer `Co-Authored-By` nommant le modèle, ou auteur `Claude` ; commit cité |
| **[S]** | le sujet du commit nomme le modèle, sans trailer |
| **[P]** | la pièce le déclare d'elle-même (fichier cité) |
| **[D]** | déclaré par l'auteur hors de la pièce, non vérifiable sur l'arbre |
| **[—]** | aucune trace. *L'absence de trace n'est pas une preuve d'absence d'assistance* (§6) |

Le rôle d'un commit se lit à son sujet : c'est une lecture, citée pour qu'on la refasse.

## 3. Documents publiés

« Commits » : commits qui touchent un fichier de la pièce, sous ses noms anciens compris (chemins au
§7) — un commit d'alignement des `README` compte pour chaque pièce qu'il touche. Pour chaque pièce :
CONC et RESP à André-Guy Bruneau — champ `/Author` des PDF signés ; « la responsabilité éditoriale est
celle de l'auteur » [P : `1 - Collection/README.md`] ; **relecteurs humains : aucun**.

| Pièce | Agents : rôles et preuves | Entrée du texte | Commits : co-signés par modèle · sans trailer | Outils |
|---|---|---|---|---|
| **Vol. I** — `1 - Collection/1 - InteroperabiliteAgentique/Monographie.pdf` | RECH, VER [P] « pipelines de recherche multi-agents » (`1 - Collection/README.md`, Avertissements) · REL [G] Opus 4.8 `902cdfa`, `6989ef8` ; Opus 5 `54cc95d`, `c8f7bfe` · RED [—] | `35001a0`, 18 juil. 2026, sans trailer : entré d'un bloc (230 fichiers, 45 934 lignes, les Vol. I et II ensemble), sa rédaction précède l'historique de ce dépôt | 35 : Opus 5 10, Opus 4.8 6, Fable 5 4 · 15 | Pandoc, Typst 0.15.0, Mermaid |
| **Vol. II** — `1 - Collection/2 - OrchestrationAgentique/Monographie.pdf` | RECH, VER [P] même déclaration ; « relecteur distinct du rédacteur — agent ou humain » (`prd/PRDPlan.md`), vote à trois juges (`prd/PRD.md`) · RED [G] Opus 4.8 de pièces depuis sorties : [article de synthèse](ARCHIVES.md#synthese-vol2) `e6d5111`, [page de présentation](ARCHIVES.md#index-vol1-vol2) `46cbbb3` · REL [G] Opus 4.8 `cc53ada` ; Opus 5 `3fc368f`, `a7df123` | `35001a0`, 18 juil. 2026, sans trailer | 29 : Opus 5 11, Opus 4.8 5 · 13 | Pandoc, Typst |
| **Vol. III** — `1 - Collection/3 - EntrepriseAgentique/Monographie.pdf` | RED [G] Opus 4.8 `3ee6091` (Partie I, ch. 1-4), `e554c8e` (ch. 1-21), `089f94a` (34 pièces) · RECH [G] Opus 4.8 `30a971f` (socle F-79 à F-89) · VER [G] Opus 4.8 `2590f08` (revue adverse P2), `70ce951` (revalidation P5.1) · VIS [G] Opus 4.8 `a0594e2` ; Fable 5 `46fcda1` · REL [S] Fable 5 `2ecd3f7` · [P] « Assistance par agents » (`1 - Collection/3 - EntrepriseAgentique/README.md`), qui ajoute : « la distinction rédacteur / relecteur n'est pas constatable sur disque » | pièces `5ee8927` à `089f94a`, 21-22 juil. 2026, co-signées Opus 4.8 ; assemblage `a0594e2` | 40 : Opus 4.8 13, Opus 5 9, Fable 5 1 · 17 | Pandoc, Typst |
| **Collection** — `1 - Collection/README.md` et `1 - Collection/0 - Références/1997 - Mémoire Maitrise.pdf` | REL [G] Opus 5 `857b781`, `c81be4a`, `c8f7bfe`, `a7df123`. Le mémoire de 1997 est une œuvre de l'auteur antérieure aux modèles de langage, entrée au dépôt par `659241b` | — | 33 : Opus 5 16 · 17 | — |
| **Vol. IV** — `2 - Compendium/Compendium.pdf` et ses cinquante pièces (§4) ; archive de travail, hors livrables depuis le 15 septembre 2026 (D-18) | RED [G] Opus 5 : Livre I sous l'identité `Claude` (§5), Livres II à V `1de55db`, `eb8f9f5`, `c12d50d`, `0ffc4c3`, `824a2a0` · CONC sous instruction [G] Fable 5 `9c4199e`, `ba46fa0` (TOC v0.8, v0.9), `19b9b58` (PRD v0.1) ; Opus 4.8 `71cfca6`, `9c2f554` · VER [G] Fable 5 `206ba64` ([audit du 28 juillet](ARCHIVES.md#compendium-audit-2026-07-28)), `38ea279` (« 50 chapitres relus, 50 vérifiés adversarialement ») ; Opus 5 `0ca73d0`, `7f0d810` ([audit du 2 septembre](ARCHIVES.md#compendium-audit-2026-09-02)) · RECH [G] Fable 5 `a7f709d` (socle re-daté à la source primaire) · REL [G] Opus 5 `1535aa5`, `c5a51b3`, `4355a41` (révision du français) · VIS, LOG [G] Opus 5 `fd3aa01` (chaîne de rendu), `6b7a9d9` (115 figures), `6dd5045` ([*skill*](ARCHIVES.md#skill-chapitre-compendium)) · aucune déclaration d'assistance trouvée dans le PDF ni le `README` du volume | `efe870b` à `824a2a0`, 27 juil. 2026 | 142 : Opus 5 63, Fable 5 12, Opus 4.8 4 · 63 | Pandoc, Typst 0.15.1, Python |
| **Vol. V** — `4 - Essais/1 - Traité/Traité.pdf` | VER [G] Opus 5 `063ca6a` (boucle bâtisseur / critique, 168 correctifs ; [journal](ARCHIVES.md#journal-traite-2026-08-10)), `b439bb2` ([audit du 2 septembre](ARCHIVES.md#traite-audit-2026-09-02), quatrième édition) · VIS [G] Opus 5 `051a302` (seize figures) · REL [G] Fable 5 `54e77b7` (révision finale) · RED : le commit qui dépose le texte est co-signé Opus 5 [G], sans dire qui l'a rédigé · [P] le traité se dit « même auteur, non revue par les pairs » de sa transposition en simulateur (`Traité.md`) | `716d67d`, 10 août 2026, co-signé Opus 5 (dépôt du texte sous le nom `Swarm Agentic Systems.md`) | 16 : Opus 5 6, Fable 5 1 · 9 | Pandoc, Typst, Python |
| **Simulateur** `stigmergie-lab` — `4 - Essais/1 - Traité/` (`crates/`, `web/`, `bancs/`, `docs/`) | LOG [G] Opus 5 `367b602`, `310c900`, `3548faa`, `b9b1879` · VER [G] Opus 5 `df9e14e` (campagne de vérification Rust), `c0bb8b2` (audit du code, présent : `audit.md`) ; boucle M1-M5 du 17 août, [douze rapports](ARCHIVES.md#traite-boucle-audit-2026-08) · [P] `4 - Essais/1 - Traité/CLAUDE.md` : les consignes données à l'agent | `6ac7170`, 14 août 2026, sans trailer | 27 : Opus 5 15 · 12 | cargo et rustc 1.98.0, wasm-bindgen 0.2.127, Node 24.19.0 |
| **Vol. VI** — `3 - Veille/Veille Technologique.pdf` | RECH, VER, RED [P] « pipeline multi-agents en cinq phases, exécuté par des agents LLM (Claude, Anthropic) » — un agent de recherche par angle, trois vérificateurs indépendants par énoncé, 106 agents et 531 requêtes à la première exécution (§ Protocole de revue et § Divulgation de la pièce) ; la pièce déclare aussi les éditions d'août 2026 « sans ronde de vérification adverse à plusieurs votants » · RED [G] Fable 5 `074955d` à `b974ca4` (§4.11, sept itérations) ; Opus 4.8 `a4db27c` ; Opus 5 `0b38991` (édition d'août) · VER [G] Fable 5 `e02edb6` (authenticité des 162 références) · REL [G] Fable 5 `379fa00` (« 2 agents réviseurs ») ; Opus 4.8 `aee6c12` (136 pages) · LOG [G] Opus 4.8 `e7465d2` | éditions successives ; la dernière, `5ba4fb1` (8 août 2026), sans trailer ; [éditions antérieures sorties](ARCHIVES.md#veille-editions-anterieures) | 64 : Fable 5 29, Opus 5 8, Opus 4.8 4 · 23 | Pandoc, Typst, Python |
| **Vol. VII** — `3 - Veille/Revue de littérature.pdf` | RECH [P] « la passe neuve a été conduite par des agents indépendants, à consigne de source primaire exclusive » (§ Méthode de la pièce ; modèle non nommé) · REL [G] Opus 5 `051a302`, `696bcac`, `fe6b6a7` (appareil seulement) · RED [—] | `1e920ff`, 9 août 2026, sans trailer | 15 : Opus 5 3 · 12 | Pandoc, Typst, Python |
| **Vol. VIII** — `5 - Recension/État de l'art — services financiers.pdf` | VER [G] Fable 5 `3629250` (audit de la recension, dix-huit tâches) · REL [S] Fable 5 `c216cb5` ; [G] Opus 5 `c3d2777`, `91ed417`, `857b781` · RED [—] pour le texte ; ses devanciers sont sortis : [*Rapport de l'art*](ARCHIVES.md#rapport-de-l-art), RED [G] `Claude` + Opus 5, et la [première recension](ARCHIVES.md#premiere-recension), avec son [journal de boucle](ARCHIVES.md#journal-recension-2026-08-16) | `25e4ea0`, 20 août 2026, sans trailer | 26 : Opus 5 10, Fable 5 1 · 15 | Pandoc, Typst, Python |
| **Planche** — `5 - Recension/Cinq schémas — état de l'art en services financiers.pdf` | REL [G] Opus 5 `91ed417` · RED [—] | `25e4ea0`, 20 août 2026, sans trailer | 4 : Opus 5 1 · 3 | Python (`figures/dessine.py`), Typst |
| **Rendus de boucle** — `5 - Recension/Cinq schémas — état de l'art en services financiers-critique.pdf`, `5 - Recension/Cinq schémas — état de l'art en services financiers-essai.pdf`, `5 - Recension/État de l'art — services financiers-critique.pdf` | sorties de la boucle bâtisseur / critique du 5 septembre 2026, dont le résultat est co-signé Opus 5 (`fe6b6a7`) et le [journal](ARCHIVES.md#journal-documentation-2026-09-05) sorti ; [retirés de l'index le 15 septembre 2026](ARCHIVES.md#recension-sorties-de-boucle) | `79ecdcf`, 5 sept. 2026, sans trailer | — | — |
| **Note de synthèse** — `3 - Veille/Note de synthèse.pdf`, son contrôle `3 - Veille/Python/check-synthese.py` et son harnais | RED, LOG, VER : bâtisseur M8 de la boucle bâtisseur / critique du 15 septembre 2026, Claude Opus 5 [P] (statut en tête de la note) ; soumise au critique de la même boucle ; **aucun humain ne l'a relue** | non commitée à la rédaction, 15 sept. 2026 ; ✎ entrée le jour même au commit `5cdb5bb`, co-signé Opus 5 | — | Pandoc 3.11, Typst 0.15.1, Python |
| **Hors livrables** — `3 - Veille/Note-veille-SDLC-agentique.pdf` | aucune déclaration d'agent dans la pièce, dont le protocole (corpus, extraction, triangulation) ne dit pas qui l'a exécuté · REL [G] Opus 5 `fe6b6a7` (un chemin) · RED [—] | `9fcc55e`, 28 août 2026, sans trailer | 4 : Opus 5 1 · 3 | Pandoc, Typst |
| **Hors livrables** — `4 - Essais/2 - Article/article-hpc-qpu.pdf` | VER [G] Fable 5.1 `05fcc84` (« audit intégral, appareil neuf, auteurs lus à la source » ; [audit](ARCHIVES.md#article-audit-2026-09-02) sorti) · REL [G] Opus 5 `c81be4a` · RED [—] | `da6255b`, 1er sept. 2026, sans trailer | 7 : Opus 5 3, Fable 5.1 1 · 3 | Typst, Python |
| **Diaporama** — `NiveauMaturité.html` | VIS [G] Opus 5 `f6de7e7`, `1d3d55e` · REL [G] Opus 5 `ed1f1a0`, `0ab655f` · RED [—] | `f410823`, 15 août 2026, sans trailer (sous le nom `one_pager_interoperabilite_landscape.html`) | 16 : Opus 5 4 · 12 | HTML autonome |
| **Appareil de la racine** — `README.md`, `APPAREIL.md`, `LICENSE`, `.gitattributes` | VER [G] Opus 5 `997392d` (validation d'intégrité du `README`), `696bcac` (réparation d'appareil) · REL [G] Sonnet 5 `42e223c` ; Opus 5 `fe6b6a7` · LOG [G] Opus 5 `0c6755b` ; [consignes `CLAUDE.md`](ARCHIVES.md#consignes-claude-md) sorties | `1036a81` (`README.md` actuel), 21 août 2026, sans trailer | 125 : Opus 5 58, Opus 4.8 11, Fable 5 7, Sonnet 5 1, Fable 5.1 1 · 47 | git, Python |
| **Évaluation du 15 septembre 2026** — `Évaluation académique.md` et `Évaluation académique.html` | RED, VER [P] « produite par un modèle de langage — Claude Fable 5.1, exécuté comme agent Claude Code sur le poste de l'auteur » (en-tête et §12 de la pièce) | `e1b1b9e`, 15 sept. 2026, sans trailer | 1 (entrée) | Python 3.14.7, Pandoc 3.11, Typst 0.15.1, pymupdf 1.28.2 (§1 de la pièce) |
| **Gabarit d'évaluation** — `Gabarit d'évaluation académique.md` ; **plan** — `Plan d'exécution — évaluation académique.md` | RED [D] produits par un modèle de langage, selon l'auteur (consigne de la boucle du 15 septembre 2026). **Aucune des deux pièces ne le dit, ni ne nomme le modèle** ; qu'il s'agisse de la session de l'évaluation (Claude Fable 5.1) est une supposition, non vérifiée | `3b8236d` et `e1b1b9e`, 15 sept. 2026, sans trailer | 1 chacun | — |
| **Résumés anglais** — la page « Abstract » des dix documents publiés qui portent un résumé français : Vol. I, II, III, V, VI, VII et VIII, note SDLC, note de synthèse, article HPC-QPU | RED : traduits du résumé français avec assistance de modèle — bâtisseur M9 de la boucle du 15 septembre 2026, Claude Opus 5, tâche T7.1 ; **aucun humain ne les a relus** | non commités à la rédaction, 15 sept. 2026 ; ✎ entrés le jour même au commit `91ddce6`, co-signé Opus 5 | — | Pandoc 3.11, Typst 0.15.1 |
| **Consigne de relecture** — `RELECTURE.md` | RED : bâtisseur M6 de la boucle du 15 septembre 2026, Claude Opus 5, tâche T5.1 [P] (en-tête de la pièce) ; soumise au critique de la même boucle · REL : empreintes et folios des rendus recomposés, bâtisseur M9, tâche T7.1 [P] `gauntlet-log.md` ; [G] Opus 5 `5cdb5bb`, `91ddce6` ; **aucun humain ne l'a relue** | `5cdb5bb`, 15 sept. 2026, co-signé Opus 5 | 2 : Opus 5 2 · 0, au commit `91ddce6` | git, Python, pymupdf |
| **Journaux** — les onze `JOURNAL.md` : celui de la racine, ceux de `1 - Collection/` et de ses quatre sous-dossiers, de `2 - Compendium/`, `3 - Veille/`, `4 - Essais/1 - Traité/`, `4 - Essais/2 - Article/` et `5 - Recension/` | chacun reçoit « sans un mot changé » la page d'accueil de son dossier au commit `5cdb5bb` [P] (en-tête de chaque journal) : le texte reçu garde les rôles de sa page d'origine · REL : déplacement par le bâtisseur M7a de la boucle du 15 septembre 2026, tâche T4.1 [P] `gauntlet-log.md`, [G] Opus 5 `fc33db1` ; entrées datées du même jour sur les résumés anglais, bâtisseur M9 [G] Opus 5 `91ddce6` ; aucun humain ne les a relus | `fc33db1`, 15 sept. 2026, co-signé Opus 5 | 2 : Opus 5 2 · 0, au commit `91ddce6` | git, Python |
| **Contrôles du 15 septembre 2026** — `.github/workflows/appareil.yml`, `Python/check-renvois.py` et `Python/check-renvois-mutations.py` (tâches T1.1 à T1.4) ; `1 - Collection/1 - InteroperabiliteAgentique/Python/check-vol1.py` et `1 - Collection/1 - InteroperabiliteAgentique/Python/check-vol1-mutations.py` (T6.5) ; `Python/check-lisibilite.py` et `Python/check-lisibilite-mutations.py` (T4.4) ; ceux de la note de synthèse sont à sa ligne | LOG, VER : bâtisseurs M1 (flux et renvois), M5 (Vol. I) et M7a (lisibilité) de la boucle du 15 septembre 2026 [P] `gauntlet-log.md`, modèle déclaré au §1 ; correctif de la CI par l'orchestrateur, [G] Opus 5 `7ad9e44` ; [G] Opus 5 `5cdb5bb`, `fc33db1` ; **aucun humain ne les a relus** | `78ebf9c` (flux et renvois), sans trailer ; `5cdb5bb` (Vol. I) et `fc33db1` (lisibilité), co-signés Opus 5 | 4 : Opus 5 3 · 1, au commit `91ddce6` | Python, GitHub Actions |
| **Cette page et `ARCHIVES.md`** | RED, VER : bâtisseur M3 de la boucle du 15 septembre 2026, Claude Opus 5 ; soumises au critique de la même boucle ; aucun humain ne les a relues | non commitées à la rédaction ; ✎ entrées le jour même au commit `78ebf9c`, sans trailer | — | git, Python |

## 4. Vol. IV — les cinquante pièces

Chaque pièce existe en `.md` source et en `.html` de lecture, versionnés ensemble. « Entrée » :
commit qui crée la pièce, auteur et trailer. Les trois commits Fable 5 communs à presque toutes sont
la relecture partielle (`8ee20df`), la relecture globale (`38ea279`) et la constitution du socle
consolidé (`b4e1693`), du 28 juillet 2026 [G]. Relecteurs humains : aucun.

| Pièce | Entrée au dépôt | Commits | Co-signés Opus 5 · Fable 5 · Opus 4.8 | Sans trailer |
|---|---|---:|---|---:|
| `2 - Compendium/Livre I/01-interoperabilite-integration-entreprise.md` | `efe870b`, Claude + Opus 5 | 12 | 6 · 3 · 0 | 3 |
| `2 - Compendium/Livre I/02-donnees-semantique-ontologies.md` | `9a1077d`, Claude + Opus 5 | 10 | 5 · 3 · 0 | 2 |
| `2 - Compendium/Livre I/03-securite-identite-gouvernance.md` | `066f8cb`, Claude + Opus 5 | 10 | 5 · 3 · 0 | 2 |
| `2 - Compendium/Livre I/04-ingenierie-systemes-agentiques.md` | `3435794`, Claude + Opus 5 | 11 | 6 · 3 · 0 | 2 |
| `2 - Compendium/Livre I/05-ancrage-informationnel.md` | `9ac10fc`, Claude + Opus 5 | 9 | 4 · 3 · 0 | 2 |
| `2 - Compendium/Livre I/06-multi-agents-evaluation-surete.md` | `66cd444`, Claude + Opus 5 | 10 | 5 · 3 · 0 | 2 |
| `2 - Compendium/Livre I/07-genealogie-gouvernance.md` | `11e7082`, Claude + Opus 5 | 10 | 4 · 3 · 0 | 3 |
| `2 - Compendium/Livre I/08-anatomie-mcp-a2a.md` | `d23f9e6`, Claude + Opus 5 | 11 | 5 · 3 · 0 | 3 |
| `2 - Compendium/Livre I/09-decouverte-registres-pile.md` | `fa8513a`, Claude, sans trailer | 10 | 4 · 3 · 0 | 3 |
| `2 - Compendium/Livre I/10-transaction-infrastructure.md` | `be2a15b`, Claude, sans trailer | 8 | 2 · 3 · 0 | 3 |
| `2 - Compendium/Livre I/11-modes-echec-risques-protocolaires.md` | `fb5b680`, Claude, sans trailer | 10 | 4 · 3 · 0 | 3 |
| `2 - Compendium/Livre II/12-heritage-standards-etires.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 9 | 5 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/13-identite-decentralisee-vc-did.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 9 | 5 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/14-grille-cinq-questions.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 8 | 4 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/15-emettre-carte-annuaires-registres.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 8 | 4 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/16-passeport-agent.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 9 | 5 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/17-chaine-mandat-deux-sauts.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 9 | 5 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/18-know-your-agent.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 9 | 5 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/19-taxonomie-attaques-identite-delegation.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 10 | 6 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/20-usurpation-revocation-boucle-defensive.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 9 | 5 · 3 · 0 | 1 |
| `2 - Compendium/Livre II/21-horloge-post-quantique.md` | `1de55db`, André-Guy Bruneau + Opus 5 | 10 | 5 · 3 · 0 | 2 |
| `2 - Compendium/Livre III/22-options-orchestration-paradigme-apm.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 7 | 3 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/23-frameworks-orchestration-entreprise.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 2 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/24-passage-echelle-entreprise.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 7 | 3 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/25-e23-risque-modele.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 2 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/26-vide-federal-c27-c36.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 3 · 3 · 0 | 0 |
| `2 - Compendium/Livre III/27-quebec-amf-article-12-1.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 3 · 3 · 0 | 0 |
| `2 - Compendium/Livre III/28-valeurs-mobilieres-acvm-11-348.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 2 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/29-pont-frames-deterministes.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 7 | 3 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/30-maillage-reglementaire-normalisation.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 10 | 5 · 3 · 0 | 2 |
| `2 - Compendium/Livre III/31-vertical-financier-durcisseurs.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 7 | 2 · 3 · 0 | 2 |
| `2 - Compendium/Livre III/32-cadre-bancaire-consommateur.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 3 · 3 · 0 | 0 |
| `2 - Compendium/Livre III/33-iso-20022-lynx-rtr.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 8 | 4 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/34-sous-domaines-financiers.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 8 | 4 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/35-etudes-de-cas-production-canadienne.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 7 | 3 · 3 · 0 | 1 |
| `2 - Compendium/Livre III/36-prospective-ap2-rails-canadiens.md` | `eb8f9f5`, André-Guy Bruneau + Opus 5 | 6 | 2 · 3 · 0 | 1 |
| `2 - Compendium/Livre IV/37-maillage-agents-point-application.md` | `c12d50d`, André-Guy Bruneau + Opus 5 | 8 | 5 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/38-observabilite-agentique.md` | `c12d50d`, André-Guy Bruneau + Opus 5 | 7 | 4 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/39-cycle-de-vie-operationnel.md` | `c12d50d`, André-Guy Bruneau + Opus 5 | 8 | 5 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/40-indicateurs-agentops-finops.md` | `c12d50d`, André-Guy Bruneau + Opus 5 | 8 | 5 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/41-fabrique-agents.md` | `0ffc4c3`, André-Guy Bruneau + Opus 5 | 6 | 3 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/42-matrice-protocoles-exigences.md` | `0ffc4c3`, André-Guy Bruneau + Opus 5 | 7 | 4 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/43-architecture-reference-couches.md` | `0ffc4c3`, André-Guy Bruneau + Opus 5 | 9 | 6 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/44-formalisation-archimate.md` | `0ffc4c3`, André-Guy Bruneau + Opus 5 | 10 | 6 · 3 · 0 | 1 |
| `2 - Compendium/Livre IV/45-blueprint-instancie-cycle-de-vie.md` | `0ffc4c3`, André-Guy Bruneau + Opus 5 | 9 | 6 · 3 · 0 | 0 |
| `2 - Compendium/Livre IV/46-instrumentation-feuille-route.md` | `0ffc4c3`, André-Guy Bruneau + Opus 5 | 9 | 6 · 3 · 0 | 0 |
| `2 - Compendium/Livre V/47-artefact-livre-provenance-mise-en-service.md` | `824a2a0`, André-Guy Bruneau + Opus 5 | 10 | 7 · 3 · 0 | 0 |
| `2 - Compendium/Livre V/48-semantique-effet-idempotence-compensation.md` | `824a2a0`, André-Guy Bruneau + Opus 5 | 9 | 6 · 2 · 0 | 1 |
| `2 - Compendium/Livre V/49-horizon-frontiere-connaissance-verifiable.md` | `824a2a0`, André-Guy Bruneau + Opus 5 | 9 | 6 · 3 · 0 | 0 |
| `2 - Compendium/Livre V/50-peremption-protocole-revalidation.md` | `824a2a0`, André-Guy Bruneau + Opus 5 | 8 | 6 · 2 · 0 | 0 |

## 5. Les vingt commits signés `Claude`

`git log --author=Claude --name-only` : chaque fichier rendu figure ci-dessous, avec la pièce qu'il
sert. Les chemins sont ceux du jour ; les dossiers ont été renommés depuis (`4 - Veille/` →
`3 - Veille/`, `6 - Article/` → `4 - Essais/2 - Article/`), et les fichiers de `.claude/`, les
`CLAUDE.md` et le *Rapport de l'art* sont [sortis](ARCHIVES.md#consignes-claude-md).
Les commits `fa8513a`, `be2a15b` et `fb5b680` ne portent aucun trailer : ils suivent, le même jour et
dans la même série de chapitres, des commits co-signés Opus 5 — *que le modèle soit le même est une
supposition*.

| Commit | Date | Trailer · session | Fichiers | Pièce et rôle |
|---|---|---|---|---|
| `a7df123` | 2026-09-03 | Opus 5 · `session_01Ewctq3…` | `1 - Collection/2 - OrchestrationAgentique/README.md` `1 - Collection/3 - EntrepriseAgentique/README.md` `1 - Collection/README.md` `6 - Article/README.md` | appareil — `README` des Vol. II et III, de la Collection et de l'article : REL |
| `c8f7bfe` | 2026-09-03 | Opus 5 · `session_01Ewctq3…` | `1 - Collection/1 - InteroperabiliteAgentique/README.md` `1 - Collection/2 - OrchestrationAgentique/README.md` `1 - Collection/2 - OrchestrationAgentique/monographie/README.md` `1 - Collection/3 - EntrepriseAgentique/README.md` `1 - Collection/README.md` `2 - Compendium/Livre I/README.md` `2 - Compendium/Livre II/README.md` `2 - Compendium/Livre III/README.md` `2 - Compendium/Livre IV/README.md` `2 - Compendium/Livre V/README.md` `2 - Compendium/PRD/PRD.md` `2 - Compendium/PRD/TOC.md` `2 - Compendium/README.md` `4 - Veille/README.md` `5 - Recension/README.md` `README.md` | appareil — date de clôture portée dans seize `README`, le PRD et le TOC du Vol. IV : REL |
| `bb3bdde` | 2026-08-16 | Opus 5 · `session_018bzMe7…` | `README.md` `Rapport de l'art.html` `Rapport de l'art.md` `Rapport de l'art.pdf` `build/rendre-rapport.py` | *Rapport de l'art* ([sorti](ARCHIVES.md#rapport-de-l-art)) : VIS, LOG (chaîne de rendu) |
| `432ac8d` | 2026-08-16 | Opus 5 · `session_018bzMe7…` | `README.md` `Rapport de l'art.md` | *Rapport de l'art* ([sorti](ARCHIVES.md#rapport-de-l-art)) : RED |
| `fb5b680` | 2026-07-27 | aucun · aucune | `.claude/skills/chapitre-compendium/scripts/verifier-piece-mutations.py` `2 - Compendium/CLAUDE.md` `2 - Compendium/Livre I/11-modes-echec-risques-protocolaires.html` `2 - Compendium/Livre I/11-modes-echec-risques-protocolaires.md` `2 - Compendium/Livre I/README.md` `CLAUDE.md` `README.md` | Vol. IV, Livre I, ch. 11 : RED ; [*skill*](ARCHIVES.md#skill-chapitre-compendium) et [consignes](ARCHIVES.md#consignes-claude-md) : LOG |
| `be2a15b` | 2026-07-27 | aucun · aucune | `.claude/skills/chapitre-compendium/SKILL.md` `2 - Compendium/Livre I/07-genealogie-gouvernance.html` `2 - Compendium/Livre I/07-genealogie-gouvernance.md` `2 - Compendium/Livre I/10-transaction-infrastructure.html` `2 - Compendium/Livre I/10-transaction-infrastructure.md` | Vol. IV, Livre I, ch. 10 : RED ; ch. 7 : REL ; *skill* : LOG |
| `fa8513a` | 2026-07-27 | aucun · aucune | `2 - Compendium/Livre I/09-decouverte-registres-pile.html` `2 - Compendium/Livre I/09-decouverte-registres-pile.md` | Vol. IV, Livre I, ch. 9 : RED |
| `d23f9e6` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/08-anatomie-mcp-a2a.html` `2 - Compendium/Livre I/08-anatomie-mcp-a2a.md` | Vol. IV, Livre I, ch. 8 : RED |
| `11e7082` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/07-genealogie-gouvernance.html` `2 - Compendium/Livre I/07-genealogie-gouvernance.md` | Vol. IV, Livre I, ch. 7 : RED |
| `85632bf` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `.claude/skills/chapitre-compendium/references/controles.md` `.claude/skills/chapitre-compendium/scripts/rendre-piece.py` `2 - Compendium/Livre I/06-multi-agents-evaluation-surete.html` | *skill* : LOG ; Vol. IV, ch. 6 : VIS |
| `66cd444` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/06-multi-agents-evaluation-surete.html` `2 - Compendium/Livre I/06-multi-agents-evaluation-surete.md` | Vol. IV, Livre I, ch. 6 : RED |
| `9ac10fc` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/05-ancrage-informationnel.html` `2 - Compendium/Livre I/05-ancrage-informationnel.md` | Vol. IV, Livre I, ch. 5 : RED |
| `3435794` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/04-ingenierie-systemes-agentiques.html` `2 - Compendium/Livre I/04-ingenierie-systemes-agentiques.md` | Vol. IV, Livre I, ch. 4 : RED |
| `066f8cb` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/03-securite-identite-gouvernance.html` `2 - Compendium/Livre I/03-securite-identite-gouvernance.md` | Vol. IV, Livre I, ch. 3 : RED |
| `9a1077d` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `.claude/skills/chapitre-compendium/SKILL.md` `.claude/skills/chapitre-compendium/references/controles.md` `.claude/skills/chapitre-compendium/scripts/rendre-piece.py` `.claude/skills/chapitre-compendium/scripts/verifier-piece-mutations.py` `.claude/skills/chapitre-compendium/scripts/verifier-piece.py` `2 - Compendium/Livre I/02-donnees-semantique-ontologies.html` `2 - Compendium/Livre I/02-donnees-semantique-ontologies.md` | Vol. IV, Livre I, ch. 2 : RED ; *skill* : LOG |
| `6dd5045` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `.claude/skills/chapitre-compendium/SKILL.md` `.claude/skills/chapitre-compendium/assets/gabarit.html` `.claude/skills/chapitre-compendium/references/controles.md` `.claude/skills/chapitre-compendium/references/conventions.md` `.claude/skills/chapitre-compendium/references/gabarit-piece.md` `.claude/skills/chapitre-compendium/scripts/verifier-piece-mutations.py` `.claude/skills/chapitre-compendium/scripts/verifier-piece.py` `2 - Compendium/CLAUDE.md` | [*skill* de rédaction](ARCHIVES.md#skill-chapitre-compendium) et consignes du Vol. IV : LOG |
| `058a6de` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `.claude/settings.json` `CLAUDE.md` | [permissions et consignes d'agent](ARCHIVES.md#claude-settings) (« committer tout et pousser sur main ») : LOG |
| `da37ca8` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/Livre I/01-interoperabilite-integration-entreprise.html` `2 - Compendium/Livre I/README.md` | Vol. IV, Livre I, ch. 1 : VIS |
| `efe870b` | 2026-07-27 | Opus 5 · `session_01Q1YFMB…` | `2 - Compendium/CLAUDE.md` `2 - Compendium/Livre I/01-interoperabilite-integration-entreprise.html` `2 - Compendium/Livre I/01-interoperabilite-integration-entreprise.md` `2 - Compendium/Livre I/README.md` `CLAUDE.md` `README.md` | Vol. IV, Livre I, ch. 1 : RED ; consignes ; `README` racine : REL |
| `9e5e2bf` | 2026-07-27 | Fable 5 · `session_0129gQHN…` | `2 - Compendium/CLAUDE.md` `2 - Compendium/PRD/PRD.md` `2 - Compendium/PRD/TOC.md` `2 - Compendium/PRD/check-toc-mutations.py` `2 - Compendium/PRD/check-toc.py` `2 - Compendium/README.md` `README.md` | Vol. IV — plan (TOC v0.21, PRD v0.5) : CONC sous instruction ; `check-toc.py` : LOG ; conspectus : REL |

## 6. Limites de cette déclaration

1. **Le trailer se déclare, il ne se prouve pas.** Il est écrit au commit par l'outil d'agent ou par
   l'auteur ; il nomme un modèle, jamais la part du texte qu'il a écrite.
2. **152 commits de l'auteur ne portent aucun trailer**, dont l'entrée du texte des Vol. I et II
   (`35001a0`), de la revue (`1e920ff`), de la note SDLC (`9fcc55e`), du code du simulateur
   (`6ac7170`), de l'état de l'art (`25e4ea0`), de l'article (`da6255b`) et des éditions d'août de la
   veille (`5ba4fb1`). Git ne dit pas qui les a rédigés. Deux sujets nomment Fable 5 sans trailer
   (`2ecd3f7`, `c216cb5`).
3. **L'historique commence le 24 juin 2026 ; les Vol. I et II y entrent le 18 juillet**, rédigés et
   vérifiés ailleurs — le `README` du Vol. I date des passes de vérification adverse du 24 au
   30 juin 2026 que ce dépôt ne contient pas.
4. **« Commits » mesure un contact, pas une part.** Un commit qui aligne seize `README` compte pour
   chacune des pièces qu'il touche.
5. **Relecture humaine : aucune.** Les niveaux de preuve **[A]** *(se lit [A-i] depuis la réforme du même jour)* des PRD reposent sur des votes
   d'instances de modèle ; l'évaluation du 15 septembre 2026 est elle-même produite par un modèle.
6. **Cette page est écrite par un agent**, sur l'historique au commit `e1b1b9e`. Tout commit ultérieur
   la périme ; le §7 la refait. ✎ *Les lignes de la consigne de relecture, des journaux et des contrôles
   du 15 septembre 2026, les incises qui datent l'entrée de la note de synthèse et des résumés anglais, et
   celles des §1 et §6.5, sont ajoutées le même jour par la passe de lissage finale de la boucle
   (Claude Opus 5), sur l'historique au commit `91ddce6`.*

## 7. Rejouer

Depuis la racine, en Git Bash.

Totaux par identité et par modèle :

```bash
git log --format='%an|%(trailers:key=Co-Authored-By,valueonly,separator=;)' |
  sed 's/ <noreply@anthropic.com>//g' | sort | uniq -c | sort -rn
```

Une pièce — remplacer les chemins par ceux du tableau ci-dessous :

```bash
git log --format='%(trailers:key=Co-Authored-By,valueonly,separator=;)' -- "*Veille Technologique.*" |
  sed 's/ <noreply@anthropic.com>//; s/^$/(sans trailer)/' | sort | uniq -c
```

Une pièce du Vol. IV : `git log --follow --format='%h %an %(trailers:key=Co-Authored-By,valueonly)' -- "<pièce>.md"`.

Le critère de la tâche T2.1 — aucune ligne ne doit sortir :

```bash
git -c core.quotepath=false log --author=Claude --name-only --format= | sort -u | while IFS= read -r f; do
  grep -qF -- "\`$f\`" CONTRIBUTIONS.md || echo "absent : $f"
done
git -c core.quotepath=false ls-files '*.pdf' '2 - Compendium/Livre*/[0-9]*.md' 'NiveauMaturité.html' | while IFS= read -r f; do
  grep -qF -- "\`$f\`" CONTRIBUTIONS.md || echo "document sans ligne : $f"
done
```

| Pièce | Chemins suivis (noms anciens compris) |
|---|---|
| Vol. I | `1 - Collection/1 - InteroperabiliteAgentique` `1 - Corpus/1 - InteroperabiliteAgentique` `1 - Corpus Agentique/1 - InteroperabiliteAgentique` `1 - InteroperabiliteAgentique` `InteroperabiliteAgentique`, moins `:(exclude)*Borealis-Go*` `:(exclude)*Veille Technologique*` |
| Vol. II | `1 - Collection/2 - OrchestrationAgentique` `1 - Corpus/2 - OrchestrationAgentique` `1 - Corpus Agentique/2 - OrchestrationAgentique` `2 - OrchestrationAgentique` `OrchestrationAgentique` |
| Vol. III | `1 - Collection/3 - EntrepriseAgentique` `1 - Corpus/3 - EntrepriseAgentique` `1 - Corpus Agentique/3 - EntrepriseAgentique` `3 - EntrepriseAgentique` |
| Collection | `1 - Collection/README.md` `1 - Corpus/README.md` `1 - Corpus Agentique/README.md` `1 - Collection/0 - Références` `1 - Corpus/0 - Références` `1 - Corpus/CLAUDE.md` |
| Vol. IV | `2 - Compendium` `2 - Compendium Agentique` `4 - CompendiumAgentique` |
| Vol. V | `*Traité/Traité.*` `Traité.md` `Traité.pdf` `Swarm Agentic Systems.*` `*Traité/figures` `figures` `*Traité/build` `*Traité/Python` |
| Simulateur | `4 - Essais/1 - Traité` `3 - Traité`, moins `:(exclude)*Traité/Traité.*` `:(exclude)*Traité/figures` `:(exclude)*Traité/build` `:(exclude)*Traité/Python` |
| Vol. VI | `*Veille Technologique.*` |
| Vol. VII | `*Revue de littérature.*` |
| Vol. VIII | `5 - Recension`, moins `:(exclude)5 - Recension/Cinq schémas*` `:(exclude)5 - Recension/*NiveauMaturité*` `:(exclude)5 - Recension/OnePager*` `:(exclude)5 - Recension/*-critique.pdf` `:(exclude)5 - Recension/*-essai.pdf` |
| Planche | `5 - Recension/Cinq schémas*` |
| Note SDLC | `*Note-veille-SDLC-agentique.*` |
| Article | `4 - Essais/2 - Article` `6 - Article` |
| Diaporama | `*NiveauMaturité.html` `*OnePager.html` `one_pager_interoperabilite_landscape.*` |
| Appareil de la racine | `README.md` `APPAREIL.md` `LICENSE` `.gitattributes` `.gitignore` `CLAUDE.md` `.claude` |
| Évaluations, gabarit, plan | `Évaluation académique.*` `Gabarit d'évaluation académique.md` `Plan d'exécution — évaluation académique.md` |
| Note de synthèse | `3 - Veille/Note de synthèse.*` `3 - Veille/Python/check-synthese.py` `3 - Veille/Python/check-synthese-mutations.py` |
| Consigne de relecture | `RELECTURE.md` |
| Journaux | `*JOURNAL.md` |
| Contrôles du 15 septembre 2026 | `.github/workflows/appareil.yml` `Python/check-renvois.py` `Python/check-renvois-mutations.py` `Python/check-lisibilite.py` `Python/check-lisibilite-mutations.py` `1 - Collection/1 - InteroperabiliteAgentique/Python` |
| Résumés anglais | aucun chemin propre : `git show --stat 91ddce6` |
