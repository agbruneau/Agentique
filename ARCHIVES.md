# Archives — les pièces sorties du dépôt, et comment les relire

*Registre établi le 15 septembre 2026 (tâche T2.3 du [plan d'exécution](<Plan%20d%27ex%C3%A9cution%20%E2%80%94%20%C3%A9valuation%20acad%C3%A9mique.md>)).
Il part de l'historique — `git log --diff-filter=D`, **334 suppressions de fichiers en 47 commits**
du 24 juin au 5 septembre 2026 — et non de ce que le dépôt dit de lui-même : le plan annonçait
« trois `audit.md`, deux journaux de boucle, l'évaluation du 5 septembre, le démonstrateur, l'article
de synthèse » ; l'historique rend **six rapports d'audit, un rapport d'arbitrage, douze rapports de
boucle, huit journaux de boucle, une évaluation dont le nom a été repris** et le reste ci-dessous. Qui a produit
chaque pièce, humain ou agent : [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md).*

## Lire une ligne

- **Sortie** : le commit qui retire la pièce. Son parent, `<sortie>^`, est le dernier état où elle
  est lisible.
- **Relire** : la commande donnée. Un PDF se redirige vers un fichier (`… > piece.pdf`) ; pour un
  dossier, la même commande liste le contenu et `git archive <sortie>^ "<dossier>" | tar -x -C <cible>`
  l'extrait.
- **Chemin** : celui du jour de la sortie. C'est une donnée, pas une adresse : les dossiers ont été
  renommés depuis — `1 - Corpus Agentique/` → `1 - Corpus/` (25 juillet) → `1 - Collection/`
  (21 août) ; `3 - Traité/` → `4 - Essais/1 - Traité/` et `6 - Article/` → `4 - Essais/2 - Article/`
  (5 septembre) ; `4 - Revue et Veille/` → `4 - Veille/` (15 août) → `3 - Veille/` (5 septembre).
- **Empreinte** : les douze premiers caractères de l'objet git (`git rev-parse <sortie>^:"<chemin>"`).
  Deux pièces de même nom n'ont pas la même empreinte.
- **Cité au corps** : lignes des fichiers suivis qui nomment encore la pièce au 15 septembre 2026,
  hors ce registre et `CONTRIBUTIONS.md` (`git grep -F -c "<motif>"`). Ces mentions sont des faits
  datés et restent telles quelles. Les **renvois** au sens du dépôt (liens relatifs) qui visaient une
  pièce sortie étaient trois, tous vers `2 - Compendium/audit.md` ; ils pointent désormais
  [sa ligne](#compendium-audit-2026-09-02).

## ⚠ Même nom, autre pièce

Cinq noms ont désigné plusieurs pièces. **Un renvoi par le nom seul ne dit pas laquelle.**

| Nom | Pièces distinctes, de la plus ancienne à la plus récente | Empreintes |
|---|---|---|
| `gauntlet-log.md` (racine) | [audit du compendium, 30 juillet](#journal-compendium-2026-07-30) (sorti `377f8ca`) · [refonte de la veille, 8 août](#journal-veille-2026-08-08) (`79ef5d4`) · [audit du traité, 10 août](#journal-traite-2026-08-10) (`57e1afd`) · [documentation après réorganisation, 5 septembre](#journal-documentation-2026-09-05) (`79ecdcf`) · **journal de la boucle M1–M3 du 15 septembre 2026, non suivi par git au moment de ce registre** ✎ *entré le jour même au commit `78ebf9c`* | `f70ebf715f00` · `1b82726ff00a` · `fefe09240108` · `1e2b5e7d6f16` · *aucune : pas dans l'index* ✎ `843aa55839cb` au commit `78ebf9c` |
| `Évaluation académique.md` (racine) | [évaluation du 5 septembre 2026](#evaluation-2026-09-05), 78 / 100, entrée `daacbec`, sortie `79ecdcf` · évaluation du 15 septembre 2026, 75,5 / 100, entrée `e1b1b9e`, **présente** | `17516a452606` · `305dbfc03b81` |
| `2 - Compendium/audit.md` | [audit de couverture, 24 juillet](#compendium-audit-2026-07-24) (sorti `f6183bf`) · [audit des cinq Livres, 28 juillet](#compendium-audit-2026-07-28) (`982ef3a`) · [audit intégral, 2 septembre](#compendium-audit-2026-09-02) (`60e1b99`) | `f4940a830000` · `812fb1546c08` · `908ef40ff340` |
| `audit.md` du traité | [audit intégral du 2 septembre](#traite-audit-2026-09-02), `3 - Traité/audit.md`, sorti `99b3ecb` · audit du code Rust du 4 septembre, entré `c0bb8b2`, **présent** sous `4 - Essais/1 - Traité/audit.md` | `916dd314baf4` · `03cbefb29570` |
| `3 - Traité/gauntlet-log.md` | [actualisation du traité, 15 août](#journal-traite-2026-08-15) (sorti `4dfc0dc`) · [audit complet du code, 17 août](#journal-code-2026-08-17) (sorti `20cc1ae`, restauré `696bcac`, sorti `4e2ae22`) | `f10a5b7b98fd` · `66f6834fff3b` |

⚠ **Le `gauntlet-log.md` de la racine au 15 septembre 2026 n'est aucun des quatre journaux
supprimés.** Il est écrit par l'orchestrateur de la boucle bâtisseur / critique qui produit ce
registre ; `git ls-files gauntlet-log.md` ne rend rien, et `git log -- gauntlet-log.md` s'arrête au
commit `79ecdcf`. S'il entre au dépôt, ce sera une cinquième pièce sous le même nom. ✎ *Il y est entré le jour même, au commit `78ebf9c`.*

⚠ **Un renvoi à `Évaluation académique.md` écrit le 5 septembre 2026 vise la pièce du 5, à
78 / 100.** Mort du 5 au 15 septembre, le même lien résout depuis vers l'évaluation du 15 : la cible
existe, la pièce citée n'y est plus. Un tel renvoi garde le nom et relit la pièce par sa commande.

## 1. Évaluations, audits, arbitrages

| Pièce | Nature | Sortie | Relire | Empreinte | Cité au corps |
|---|---|---|---|---|---|
| <a id="evaluation-2026-09-05"></a>`Évaluation académique.md` et `Évaluation académique.html` | évaluation du dépôt au commit `69eeee2`, datée du 5 septembre 2026, 78 / 100 ; évaluateur non nommé dans la pièce ; 23 356 o et 43 624 o | `79ecdcf`, 5 sept. 2026 | `git show 79ecdcf^:"Évaluation académique.md"` · `git show 79ecdcf^:"Évaluation académique.html"` | `17516a452606` · `9c1ae0bc222c` | 20 l. / 6 f. pour le motif `Évaluation académique`, les deux évaluations confondues — compte mouvant le 15 septembre, les pages de la racine étant réalignées le même jour |
| <a id="compendium-audit-2026-09-02"></a>`2 - Compendium/audit.md` | **audit intégral du compendium et plan d'exécution des correctifs**, 2 septembre 2026 — la passe D-15 du PRD §18 ; 43 328 o ; entré `7f0d810` | `60e1b99`, 2 sept. 2026 | `git show 60e1b99^:"2 - Compendium/audit.md"` | `908ef40ff340` | liens repointés ici : `2 - Compendium/PRD/PRD.md` ×2, `2 - Compendium/PRD/TOC.md` ×1 ; mentions datées dans l'évaluation et le plan du 15 septembre 2026 |
| <a id="traite-audit-2026-09-02"></a>`3 - Traité/audit.md` | audit intégral du dossier du traité et plan d'exécution, 2 septembre 2026 ; 34 068 o ; entré `b439bb2` ; **distinct** de l'audit du 4 septembre présent au même dossier | `99b3ecb`, 2 sept. 2026 | `git show 99b3ecb^:"3 - Traité/audit.md"` | `916dd314baf4` | `4 - Essais/1 - Traité/Python/check-traite.py` (commentaire « l'audit du 2 septembre 2026 ») |
| <a id="article-audit-2026-09-02"></a>`6 - Article/audit.md` | audit intégral du dossier de l'article et plan d'exécution, 2 septembre 2026 ; 14 602 o ; entré `05fcc84` | `4a7ec0f`, 3 sept. 2026 | `git show 4a7ec0f^:"6 - Article/audit.md"` | `31bea18b2302` | `4 - Essais/2 - Article/README.md` (table des fichiers), `4 - Essais/2 - Article/rejeu-politique.py` (commentaire) |
| <a id="compendium-audit-2026-07-28"></a>`2 - Compendium/audit.md` et `2 - Compendium/audit-references.md` | audit des cinq Livres du compendium, 28 juillet 2026 — cent constats, un bloquant ; 124 407 o ; entré `206ba64`. Son annexe : inventaire et validation des références, 34 116 o, entrée `d0b6cbc` | `982ef3a`, 31 juil. 2026 | `git show 982ef3a^:"2 - Compendium/audit.md"` · `git show 982ef3a^:"2 - Compendium/audit-references.md"` | `812fb1546c08` · `612f69addd21` | `audit-references` : 3 l. / 2 f. |
| <a id="compendium-audit-2026-07-24"></a>`2 - Compendium/audit.md` | audit de couverture et de conformité du Vol. IV, état v0.14 du plan ; 11 932 o ; entré le 24 juillet sous `2 - Compendium Agentique/audit.md` | `f6183bf`, 25 juil. 2026 | `git show f6183bf^:"2 - Compendium/audit.md"` | `f4940a830000` | — |
| <a id="recension-audit-2026-08-19"></a>`5 - Recension/audit.md` | audit de la première recension (`État de l'art.md` et son PDF) ; 19 962 o ; entré `f383fa2` | `87a6b01`, 19 août 2026 | `git show 87a6b01^:"5 - Recension/audit.md"` | `b67abaf8de60` | — |
| <a id="compendium-arbitrage-2026-07-30"></a>`2 - Compendium/eval.html` | « Rapport d'arbitrage — La somme agentique », 30 juillet 2026 — l'arbitrage externe qui ouvre la décision D-11 ; 78 116 o ; entré `582ae42` | `73e7c4e`, 30 juil. 2026 | `git show 73e7c4e^:"2 - Compendium/eval.html"` | `a5ed30db62f2` | 11 l. / 6 f. |
| <a id="traite-boucle-audit-2026-08"></a>`3 - Traité/bancs/audit-2026-08/` | **douze rapports** de la boucle bâtisseur / critique du 17 août 2026 sur le simulateur : `M1-sim-core.md`, `M2-sim-milieu.md`, `M3-mecanismes.md`, `M4-scenarios.md`, `M5-viz-et-docs.md`, les cinq `M*-critique.md`, `CONSOLIDATION.md`, `LISSAGE-code.md`. Sortis une première fois `20cc1ae` (17 août), restaurés `696bcac` (21 août) | `7a1b7f2`, 25 août 2026 (« douze rapports supprimés, trois cents mentions réécrites ») | `git show 7a1b7f2^:"3 - Traité/bancs/audit-2026-08"` | `cf3b222ef363` (dossier) | `audit-2026-08` : 1 l. / 1 f. |
| <a id="compendium-propositions-2026-07-22"></a>`2 - Compendium Agentique/proposition-apres-agentique-2026-07-22-01.md` à `-05.md` | cinq itérations d'une proposition de passe « après-agentique », 22 juillet 2026 ; 5 678 à 10 279 o | `df370e9`, 23 juil. 2026 (« Erreur ») | `git show df370e9^:"2 - Compendium Agentique/proposition-apres-agentique-2026-07-22-01.md"` (remplacer `01` par `02` … `05`) | `7fe011ec9f37` (01) | — |

## 2. Journaux de boucle bâtisseur / critique

Le commit `25d621f` (25 août 2026) a réécrit vingt-six mentions du nom du journal de boucle ; le motif
`gauntlet-log` ne rend plus que 2 l. / 2 f. au corps. Les journaux, eux, se relisent tous.

| Pièce | Objet de la boucle | Sortie | Relire | Empreinte |
|---|---|---|---|---|
| <a id="journal-documentation-2026-09-05"></a>`gauntlet-log.md` | mise à jour de la documentation après la réorganisation en `4 - Essais/` ; porte le rejet du premier tour pour un relevé daté réécrit ; 16 716 o ; entré `fe6b6a7` | `79ecdcf`, 5 sept. 2026 | `git show 79ecdcf^:"gauntlet-log.md"` | `1e2b5e7d6f16` |
| <a id="journal-code-2026-08-17"></a>`3 - Traité/gauntlet-log.md` | audit complet du code du simulateur, 17 août 2026 — la boucle des douze rapports [ci-dessus](#traite-boucle-audit-2026-08) ; 24 095 o | `4e2ae22`, 22 août 2026 ; état du 17 août : `20cc1ae^` | `git show 4e2ae22^:"3 - Traité/gauntlet-log.md"` · `git show 20cc1ae^:"3 - Traité/gauntlet-log.md"` | `66f6834fff3b` · `706a33dbdae2` |
| <a id="journal-recension-2026-08-16"></a>`5 - Recension/gauntlet-log.md` | « Rapport de l'art (recensio) », 16 août 2026 ; 42 903 o ; entré `926fd33` | `caa0969`, 17 août 2026 | `git show caa0969^:"5 - Recension/gauntlet-log.md"` | `787223faf553` |
| <a id="journal-traite-2026-08-15"></a>`3 - Traité/gauntlet-log.md` | actualisation du traité au 15 août 2026 ; 74 679 o | `4dfc0dc`, 16 août 2026 | `git show 4dfc0dc^:"3 - Traité/gauntlet-log.md"` | `f10a5b7b98fd` |
| <a id="journal-revue-veille-2026-08-15"></a>`4 - Revue et Veille/gauntlet-log.md` | actualisation de la revue et de la veille au 15 août 2026 ; 16 592 o | `61559b2`, 15 août 2026 | `git show 61559b2^:"4 - Revue et Veille/gauntlet-log.md"` | `f589ecbc8904` |
| <a id="journal-traite-2026-08-10"></a>`gauntlet-log.md` | audit intégral du traité, 10 août 2026 — les 168 correctifs du commit `063ca6a` ; 14 226 o | `57e1afd`, 10 août 2026 | `git show 57e1afd^:"gauntlet-log.md"` | `fefe09240108` |
| <a id="journal-veille-2026-08-08"></a>`gauntlet-log.md` | refonte de la veille technologique, août 2026 ; 30 465 o ; entré `5ba4fb1` | `79ef5d4`, 10 août 2026 | `git show 79ef5d4^:"gauntlet-log.md"` | `1b82726ff00a` |
| <a id="journal-compendium-2026-07-30"></a>`gauntlet-log.md` | audit du compendium et des fichiers `.md`, ouvert le 30 juillet 2026 ; 21 201 o ; entré `0ca73d0` | `377f8ca`, 8 août 2026 | `git show 377f8ca^:"gauntlet-log.md"` | `f70ebf715f00` |

## 3. Documents, rendus et code

| Pièce | Nature | Sortie | Relire | Empreinte | Cité au corps |
|---|---|---|---|---|---|
| <a id="demonstrateur-borealis"></a>`1 - Corpus Agentique/1 - InteroperabiliteAgentique/Borealis-Go/` | **le démonstrateur** Go du Vol. I — 5 agents A2A, 4 serveurs MCP, 12 ADR ; 151 fichiers | `60f57f6`, 25 juil. 2026 | `git show 60f57f6^:"1 - Corpus Agentique/1 - InteroperabiliteAgentique/Borealis-Go"` | `c2467bbb5505` (dossier) | `Borealis-Go` : 15 l. / 10 f. |
| <a id="prd-borealis"></a>`PRD-Boralis.md` | PRD du démonstrateur, déposé à la racine le 4 juillet 2026 ; 73 401 o | `2abcb98`, 11 juil. 2026 | `git show 2abcb98^:"PRD-Boralis.md"` | `ad826258644c` | — |
| <a id="synthese-vol1"></a>`1 - Corpus Agentique/1 - InteroperabiliteAgentique/Synthese Monographie.md` et `.pdf` | **l'article de synthèse** du Vol. I, 12 sections, 69 p. ; 210 222 o | `fd8f1be`, 22 juil. 2026 | `git show fd8f1be^:"1 - Corpus Agentique/1 - InteroperabiliteAgentique/Synthese Monographie.md"` | `21986d0b70ae` | `Synthese Monographie` : 178 l. / 40 f., les deux volumes confondus |
| <a id="synthese-vol2"></a>`1 - Corpus Agentique/2 - OrchestrationAgentique/Synthese Monographie.md` et `.pdf` | l'article de synthèse du Vol. II ; 182 482 o | `fd8f1be`, 22 juil. 2026 | `git show fd8f1be^:"1 - Corpus Agentique/2 - OrchestrationAgentique/Synthese Monographie.md"` | `ca73807f54f0` | voir la ligne précédente |
| <a id="index-vol1-vol2"></a>`1 - Corpus Agentique/1 - InteroperabiliteAgentique/index.html` et `1 - Corpus Agentique/2 - OrchestrationAgentique/index.html` | pages de présentation des Vol. I et II | `fd8f1be`, 22 juil. 2026 | `git show fd8f1be^:"1 - Corpus Agentique/1 - InteroperabiliteAgentique/index.html"` · `git show fd8f1be^:"1 - Corpus Agentique/2 - OrchestrationAgentique/index.html"` | `a47f02caf043` · `7931b7db01e1` | — |
| <a id="index-racine"></a>`index.html` | première pièce du dépôt, créée et retirée le 24 juin 2026 | `504b82b`, 24 juin 2026 | `git show 504b82b^:"index.html"` | `61dead404025` | — |
| <a id="article-interoperabilite-2026-07"></a>`Interoperabilite-agentique-entreprise-2026-07.md` et `.pdf` | article sur l'interopérabilité agentique, 2 juillet 2026 ; 99 119 o | `742a6eb`, 3 juil. 2026 | `git show 742a6eb^:"Interoperabilite-agentique-entreprise-2026-07.md"` | `ede4fc9f083a` | — |
| <a id="etat-lieux-quantique"></a>`Interaction-IA-Informatique-Quantique-Etat-des-lieux-2026.md` et `.pdf` | état des lieux IA / informatique quantique, 3 juillet 2026 ; 71 308 o | `68e20ed`, 4 juil. 2026 | `git show 68e20ed^:"Interaction-IA-Informatique-Quantique-Etat-des-lieux-2026.md"` | `d2fb1b0033a4` | — |
| <a id="veille-quantique"></a>`Veille Technologique - Calcul Quantique.md` et `.pdf` | veille sur l'interopérabilité du calcul quantique en entreprise, 14 juillet 2026 ; 146 065 o | `5a6cdfd`, 15 juil. 2026 | `git show 5a6cdfd^:"Veille Technologique - Calcul Quantique.md"` | `e6b90ae4f3a4` | — |
| <a id="veille-editions-anterieures"></a>`Veille Technologique.md` et `.pdf` (racine) | **trois éditions antérieures** de la veille, retirées par « purge » puis remplacées au même nom avant son déplacement du 18 juillet 2026 : l'historique suivi de la veille actuelle (`git log --follow`) s'arrête au 18 juillet et ne les traverse pas | `4783d23` (4 juil.) · `57a79eb` (13 juil.) · `5a6cdfd` (15 juil.) | `git show 4783d23^:"Veille Technologique.md"` · `git show 57a79eb^:"Veille Technologique.md"` · `git show 5a6cdfd^:"Veille Technologique.md"` | `7255a9b598ce` · `e4cc909fd9bd` · `2ded7f5a7f61` | — |
| <a id="rapport-de-l-art"></a>`Rapport de l'art.md`, `.html`, `.pdf` et `build/rendre-rapport.py` (racine) | rapport dérivé des sept livrables, **rédigé par l'identité `Claude`** (PR #5, commits `432ac8d` et `bb3bdde`) le 16 août 2026 ; 138 435 o | `ce160f9`, 16 août 2026 (« purge rapport de l'art ») | `git show ce160f9^:"Rapport de l'art.md"` · `git show ce160f9^:"build/rendre-rapport.py"` | `35273bbfa06a` | — |
| <a id="premiere-recension"></a>`5 - Recension/État de l'art.md`, `.pdf`, `README.md`, `chapitres/` (9), `build/` (3), `figures/` (4) | **la première recension**, antérieure à l'état de l'art actuel ; 341 617 o pour le `.md` | `7e2409a`, 19 août 2026 (« Destruction de 5 - Recension ») | `git show 7e2409a^:"5 - Recension/État de l'art.md"` · `git show 7e2409a^:"5 - Recension/chapitres"` | `757b243435bc` · `7fa2d2f03d99` | — |
| <a id="etat-de-l-art-html"></a>`5 - Recension/État de l'art — services financiers.html` | rendu HTML de l'état de l'art ; 759 612 o | `c216cb5`, 21 août 2026 | `git show c216cb5^:"5 - Recension/État de l'art — services financiers.html"` | `04534d0b1f4f` | — |
| <a id="compendium-html"></a>`2 - Compendium/Compendium.html` | lecture à l'écran du compendium, écrite à la main ; 1 832 473 o | `4f98d6d`, 19 août 2026 | `git show 4f98d6d^:"2 - Compendium/Compendium.html"` | `d52106b7ecce` | `Compendium.html` : 7 l. / 3 f. |
| <a id="compendium-tocall"></a>`2 - Compendium/TOCAll.md` et `2 - Compendium Agentique/Tocs/` (3) | table des matières commentée intégrale ; les trois TOC de volumes qui l'ont précédée | `7a4cd63`, 25 juil. 2026 · `1c0d823`, 19 juil. 2026 | `git show 7a4cd63^:"2 - Compendium/TOCAll.md"` · `git show 1c0d823^:"2 - Compendium Agentique/Tocs"` | `3cd7e5ff38d9` · `ebc1b07ca3f0` | `TOCAll` : 1 l. / 1 f. |
| <a id="one-pager-pdf"></a>`one_pager_interoperabilite_landscape.pdf` | rendu PDF de la page d'une page, ancêtre de `NiveauMaturité.html` ; 29 715 o | `6968168`, 15 août 2026 | `git show 6968168^:"one_pager_interoperabilite_landscape.pdf"` | `fd0fc0bb418c` | — |
| <a id="swarm-agentic-systems-pdf"></a>`Swarm Agentic Systems.pdf` | premier rendu du traité, sous son premier nom ; 1 069 170 o | `15b9ac1`, 10 août 2026 | `git show 15b9ac1^:"Swarm Agentic Systems.pdf"` | `bf09b1a62965` | — |
| <a id="compendium-echantillons"></a>`2 - Compendium/echantillon-avant.pdf` et `echantillon-apres.pdf` | maquettes de gabarit du rendu du compendium | `982ef3a`, 31 juil. 2026 | `git show 982ef3a^:"2 - Compendium/echantillon-avant.pdf"` · `git show 982ef3a^:"2 - Compendium/echantillon-apres.pdf"` | `fb6b08d2d983` | `echantillon-avant` : 2 l. / 1 f. |
| <a id="readme-racine-2026-08-21"></a>`README.md` (racine) | page d'accueil supprimée, puis une page neuve écrite au même nom (`1036a81`, « New Readme ») : la page actuelle ne descend pas de celle-ci ; 368 193 o | `8c90a05`, 21 août 2026 | `git show 8c90a05^:"README.md"` | `f9cf81a7d8fe` | — |
| <a id="appareil-2026-08-22"></a>`APPAREIL.md` | page d'appareil supprimée puis restaurée (`0c6755b`) | `8e2433e`, 22 août 2026 | `git show 8e2433e^:"APPAREIL.md"` | `123aad4f8601` | — |

## 4. Consignes données aux agents

| Pièce | Nature | Sortie | Relire | Empreinte |
|---|---|---|---|---|
| <a id="consignes-claude-md"></a>six `CLAUDE.md` : `CLAUDE.md`, `1 - Corpus/CLAUDE.md`, `1 - Corpus/1 - InteroperabiliteAgentique/CLAUDE.md`, `1 - Corpus/2 - OrchestrationAgentique/CLAUDE.md`, `1 - Corpus/3 - EntrepriseAgentique/CLAUDE.md`, `2 - Compendium/CLAUDE.md` | les consignes que les agents de rédaction chargeaient à chaque session ; 12 906 à 81 830 o. Seul subsiste celui du simulateur, `4 - Essais/1 - Traité/CLAUDE.md` | `41666d0`, 31 juil. 2026 | `git show 41666d0^:"CLAUDE.md"` · `git show 41666d0^:"2 - Compendium/CLAUDE.md"` (même forme pour les quatre autres) | `923452fe3520` (racine) |
| <a id="skill-chapitre-compendium"></a>`.claude/skills/chapitre-compendium/` | le *skill* de rédaction des pièces du compendium, écrit par l'identité `Claude` le 27 juillet 2026 : `SKILL.md`, `assets/gabarit.html`, `references/controles.md`, `references/conventions.md`, `references/gabarit-piece.md`. Ses trois scripts vivent aujourd'hui sous `2 - Compendium/build/` | `41666d0`, 31 juil. 2026 | `git show 41666d0^:".claude/skills/chapitre-compendium/SKILL.md"` · `git show 41666d0^:".claude/skills/chapitre-compendium"` | `9020f4b6e1e2` (dossier) |
| <a id="claude-settings"></a>`.claude/settings.json` et `3 - Traité/.claude/launch.json` | réglages d'agent : les permissions git accordées aux agents, `git push` compris, posées avec la consigne d'auteur « committer tout et pousser sur main » (`058a6de`) ; un serveur de prévisualisation | `41666d0`, 31 juil. 2026 · `20cc1ae`, 17 août 2026 | `git show 41666d0^:".claude/settings.json"` · `git show 20cc1ae^:"3 - Traité/.claude/launch.json"` | `3c822554036e` · `748a7411f277` |

## 5. Œuvres de tiers

⚠ Retirées au commit même qui pose la licence CC BY 4.0 du dépôt, `696bcac`, et qu'elle ne couvre pas. L'historique les contient encore :
la commande les relit pour vérification, **elle ne donne aucun droit de redistribution**.

| Pièce | Sortie | Relire |
|---|---|---|
| <a id="tiers-references"></a>`1 - Collection/0 - Références/2003 - Enterprise Integration Patterns.pdf`, `2007 - Distributed Systems.pdf`, `2026 - SystemEngineeringBoK.pdf` ; `1 - Collection/2 - OrchestrationAgentique/prd/arxiv - Agentic Business Process Management Manifesto.pdf`, `arxiv - Design and Implementation of Agentic.pdf` | `696bcac`, 21 août 2026 | `git show 696bcac^:"1 - Collection/0 - Références/2003 - Enterprise Integration Patterns.pdf" > eip.pdf` (même forme pour les quatre autres) |

## 6. Retrait de l'index en cours (15 septembre 2026)

| Pièce | Nature | Retrait | Relire | Empreinte |
|---|---|---|---|---|
| <a id="recension-sorties-de-boucle"></a>`5 - Recension/Cinq schémas — état de l'art en services financiers-critique.pdf`, `…-essai.pdf` et `5 - Recension/État de l'art — services financiers-critique.pdf` | les rendus de travail de la boucle bâtisseur / critique du 5 septembre 2026, [journal ci-dessus](#journal-documentation-2026-09-05) ; 221 816, 221 816 et 2 065 255 o. Versionnés par `79ecdcf`, que rien ne décrivait (évaluation du 15 septembre, §8.2) | décision d'auteur DA-5 (a), exécutée le 15 septembre 2026 ; **retrait non encore commité à la rédaction de ce registre** ; ✎ commité le jour même, au commit `78ebf9c` | `git show 79ecdcf:"5 - Recension/Cinq schémas — état de l'art en services financiers-critique.pdf" > cinq-critique.pdf` · `git show 79ecdcf:"5 - Recension/Cinq schémas — état de l'art en services financiers-essai.pdf" > essai.pdf` · `git show 79ecdcf:"5 - Recension/État de l'art — services financiers-critique.pdf" > critique.pdf` | `ffd131e2af73` · `e46a64945e38` · `2f634228fba6` |

## 7. Ce qui a quitté un chemin sans quitter le dépôt

Le reste des 334 suppressions n'est pas une sortie de pièce. Le rejeu du §8 range chaque suppression
en « contenu identique encore présent » ou non ; ce qui suit explique les cas que la comparaison
d'empreintes ne sait pas voir.

| Cas | Commits | Où lire aujourd'hui |
|---|---|---|
| **Restaurés** : trente rapports de vérification du Vol. III, supprimés le 8 août 2026, et les bancs du simulateur, supprimés le 17 août | `659241b` · `20cc1ae` ; restauration `696bcac` | `1 - Collection/3 - EntrepriseAgentique/verification/`, `4 - Essais/1 - Traité/bancs/` |
| **Déplacés sans que git reconnaisse le renommage** | `35693f5` (`check-toc.py` et `check-toc-mutations.py` → `PRD/`) · `46fcda1` (`assemble.py` → `build/`) · `41666d0` (scripts du *skill* → `2 - Compendium/build/`) · `1c0d823` (`check-toc.py`) · `7e2409a` (`figures/dessine.py`, recréé) | chemins indiqués |
| **Retrait accidentel, restauré le jour même** : la veille et son PDF à la racine, l'édition d'août entrant au commit suivant | `0b38991` ; restauration `f03f0be` | `3 - Veille/Veille Technologique.md`, dont l'historique suivi traverse ce retrait |
| **Artefacts parasites** : cinq bytecodes Python, le Markdown assemblé du compendium écrit par erreur sous le nom `--help` (2 686 724 o), le Markdown assemblé intermédiaire du compendium, trois copies de sauvegarde (`Traité.md.avant-fusion`, deux `.avant-recollage`) | `ca1cf0b` · `a9c1f7f` · `4093b3f` · `1c0d823` · `76d001c` · `377f8ca` · `4dfc0dc` · `61559b2` | aucun lieu : non des pièces. `git show 76d001c^:"2 - Compendium/--help"` les relit au besoin |

## 8. Rejouer ce registre

Depuis la racine, en Git Bash. Chaque commande de relecture du registre doit sortir 0 :

```bash
grep -o 'git show [0-9a-f]\{7\}\^\?:"[^"]*"' ARCHIVES.md | sort -u | while IFS= read -r c; do
  eval "$c" > /dev/null 2>&1 && echo "OK     $c" || echo "ÉCHEC  $c"
done
```

Aucun commit de suppression de l'historique ne doit manquer au registre :

```bash
git log --diff-filter=D --format=%h | sort -u | while read -r c; do
  grep -q "$c" ARCHIVES.md || echo "absent du registre : $c"
done
```

Suppression par suppression, ce dont le contenu est encore à l'arbre :

```bash
arbre=$(git ls-tree -r HEAD)
git -c core.quotepath=false log --diff-filter=D --name-only --format='@%h' |
awk '/^@/{c=substr($0,2);next} NF{print c"\t"$0}' |
while IFS=$'\t' read -r c p; do
  b=$(git rev-parse --verify --quiet "$c^:$p")
  if [ -z "$b" ]; then echo "ILLISIBLE   $c  $p"
  elif grep -qF -- "$b" <<< "$arbre"; then echo "présent     $c  $p"
  else echo "hors arbre  $c  $p"; fi
done
```

*Ce registre ne décide pas qu'une pièce devait sortir, ni qu'elle doit revenir. Il garantit
qu'elle se retrouve.*
