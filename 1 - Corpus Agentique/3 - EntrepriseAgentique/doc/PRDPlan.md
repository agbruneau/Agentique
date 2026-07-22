# PRDPlan — Planification d'exécution du volume III

| Champ | Valeur |
|---|---|
| Version | **0.4 — plan amendé à la clôture de P2** (21 juillet 2026). Deux amendements : le **§4.1 est créé** — constat de clôture de P2, sur le modèle du §2.1 ; et le **§4 corrige le verbe de L-06** (« instruire », non « trancher »), sur la remontée R-G-04. Historique : **0.3 — plan amendé à la clôture de P1** (21 juillet 2026). Quatre amendements : **(1)** le **§1.6 est créé** — tableau de suivi d'exécution **au grain de la phase**, dérivé du §1.4 qui prime, avec une colonne « ce que l'exécution a démenti » ; **(2)** le **§3.1 est créé** — plan de réécriture des sept sections et de l'annexe E privées de corpus d'appui, **arrêté pièce par pièce**, ce qui est la troisième condition du critère de sortie J-2 ; **(3)** le **§5.3 désigne enfin une instance d'arbitrage** et pose le seuil de remontée à l'auteur — lacune constatée à la relecture P1.4 ; **(4)** la formulation imposée de **R-13 est remplacée** : fichier, section, cardinal **et numérotation**. Historique : **0.2 — plan amendé à la clôture de P0** (21 juillet 2026). Trois amendements, tous constatés sur pièce : (1) **§1.3 refait** — les documents de gouvernance vivent dans `doc/`, la structure cible qui les plaçait à la racine du volume est périmée et l'activité **P0.3 est close** ; (2) **deux renvois relatifs corrigés** — celui de l'en-tête vers le `CLAUDE.md` racine, et surtout celui du **gabarit §5.4**, qui aurait produit mécaniquement 34 renvois cassés en P3-P4 ; (3) **tableau de suivi §1.4 mis à jour au même commit que les activités qu'il décrit**. Historique : **0.1 — premier plan d'exécution du volume III** (18 juillet 2026). Établi contre [`PRD.md`](PRD.md) v0.1 et [`TOC.md`](TOC.md) v0.4. Deux décisions de méthode y sont prises et justifiées plutôt qu'héritées : la **commande de décompte de volumétrie** est fixée en locale UTF-8 dès l'origine (§1.5 — le Vol. II a dû assumer un défaut de 1,3 % qu'il ne pouvait plus corriger sans invalider tous ses chiffres publiés), et la **règle d'escalade de gouvernance** est posée *avant* la première rédaction et non après (§5.3 — le Vol. II l'a apprise en P2, au prix d'un chapitre pivot qui a dû trancher seul). |
| Date | 21 juillet 2026 (v0.1 : 18 juillet 2026) |
| Statut | **P0, P1 et P2 closes (jalons J-1, J-2 et J-3) ; P3 ouverte et non close.** Les **21 chapitres du tronc** (Parties I à VI) portent un corps, tous relus adversarialement et corrigés — constat fichier par fichier le 21 juillet 2026 ; les **13 autres pièces restent au gabarit** (P4). Socle propre : **89 entrées re-mesurées**. ⚠ **P3 ne se clôt pas** : son critère de sortie J-4 exige que les remontées de gouvernance soient **toutes** tranchées, et **six** attendent l'arbitrage de l'auteur (§1.6, §5.6). |
| Documents de gouvernance | [`PRD.md`](PRD.md) **v1.1** — autorité de contenu, socle, garde-fous, critères d'acceptation ; [`TOC.md`](TOC.md) v0.6 — autorité de découpage ; [`CLAUDE.md`](../../../CLAUDE.md) racine — conventions du dépôt |
| Objet | Opérationnaliser les jalons J-1 à J-6 du PRD (§12) : phases, dépendances, boucle qualité, formulations imposées, contrôles, artefacts |

Ce plan ne redéfinit ni le contenu (PRD §6), ni le socle (PRD §7), ni les garde-fous (PRD §8), ni les critères d'acceptation (PRD §11) — il les **ordonnance**. En cas de conflit, le PRD prime.

⚠ **Divergence assumée avec le Vol. II, à connaître avant de chercher au mauvais endroit.** Au Vol. II, les **motifs de balayage** vivent dans le PRDPlan (§4.3). Ici, ils vivent dans le **PRD, Annexe A §A.6**, parce qu'ils y sont l'instrument déclaré de CA-02 et qu'un critère d'acceptation et son outil de contrôle gagnent à ne pas être séparés. Le présent plan les **référence**, il ne les duplique pas.

---

## 1. Vue d'ensemble de l'exécution

### 1.1 Livrable final

Monographie en **neuf parties, 28 chapitres, 34 pièces** (PRD §6.1 — 28 chapitres + avant-propos + 5 annexes), en français canadien soutenu (PRD §4). Chaque pièce porte sa **date de gel de l'information**, son socle mobilisé (identifiants H-xx et F-xx) et ses garde-fous (R-xx). Volumétrie cible : **102 500 mots**, **indicative et non normative** — un écart se documente, il ne se corrige pas par amputation.

### 1.2 Phasage (aligné sur PRD §12)

| Phase | Jalon PRD | Contenu | Prédécesseur |
|---|---|---|---|
| **P0** — Assainissement du cadrage ☑ | J-1 | Révision du TOC sur les neuf écarts (PRD §7.4) ; **décision sur le corpus d'appui** ; arborescence ; gabarit de pièce | — |
| **P1** — Lots bloquants ☑ | J-2 | Instruction de L-03, L-08, L-15 (PRD §7.6) ; premières entrées F-xx du socle propre | P0 |
| **P2** — Reste du socle ☑ | J-3 | Instruction des douze autres lots ; PRD porté en v1.0 | P1 |
| **P3** — Rédaction du tronc | J-4 | Parties I à VI (ch. 1 à 21) | P2 (par lot : un chapitre démarre dès que **son** lot est clos) |
| **P4** — Application et exploitation | J-5 | Parties VII à IX (ch. 22 à 28), avant-propos, annexes A à E | P3 |
| **P5** — Revalidation et publication | J-6 | Revalidation temporelle finale, relecture CA-01 à CA-14, assemblage, PDF | P4 |

⚠ **Le phasage n'est pas un séquencement strict de P2 vers P3.** La règle cardinale du PRD (§7.0) est *par chapitre*, pas par phase : un chapitre est rédigeable dès la clôture du lot dont il dépend, même si d'autres lots restent ouverts. P2 et P3 se recouvrent donc largement, et c'est voulu — attendre la clôture des quinze lots pour écrire la première ligne allongerait le projet sans rien améliorer.

### 1.3 Structure cible du dépôt

```
3 - EntrepriseAgentique/
├── CLAUDE.md                               # consignes d'édition du volume
├── doc/                                    # gouvernance — emplacement tranché (P0.3)
│   ├── PRD.md, PRDPlan.md, TOC.md
├── monographie/
│   ├── 00-avant-propos.md
│   ├── 01-partie-I/ … 09-partie-IX/        # un fichier .md par chapitre
│   ├── 90-annexes/                         # annexes A à E de l'ouvrage
│   └── 99-registre-gel.md                  # registre des dates de gel, une ligne par pièce
├── verification/
│   ├── lot-L-xx-<slug>.md                  # rapport par lot d'instruction (P1, P2)
│   ├── revalidation-YYYY-MM-DD.md          # revalidations temporelles (P0.6, P5.1)
│   └── relecture-CA.md                     # grille CA-01..CA-14 remplie (P5)
└── (pas de sources/)                       # corpus d'appui : filiation retirée (P0.2, 21 juill. 2026)
```

⚠ **P0.3 est close : la gouvernance vit dans `doc/`, comme au Vol. II.** La v0.1 de ce plan décrivait une arborescence à la racine du volume et argumentait en sa faveur ; le disque a tranché autrement le 18 juillet 2026, et **le disque fait foi, pas le §1.3**. Le §1.3 est amendé ici plutôt que laissé en contradiction — *un plan qui décrit une arborescence que le dépôt ne porte plus est un plan qu'on cesse de lire.*

**Ce que le déplacement a coûté, et ce qu'il a évité.** Le Vol. II a déplacé sa gouvernance **après vingt-neuf pièces rédigées** et porte **48 renvois cassés, encore ouverts**. Le Vol. III a déplacé **avant la première**, au prix de **deux** renvois — tous deux dans le présent fichier, tous deux **corrigés le 21 juillet 2026** : l'en-tête pointait `](../../CLAUDE.md)` au lieu de `](../../../CLAUDE.md)`, et le **gabarit du §5.4** pointait `](../../TOC.md)` au lieu de `](../../doc/TOC.md)`. ⚠ **Le second était le coûteux** : il vit dans le gabarit que les 34 pièces recopient — non corrigé, il aurait produit mécaniquement 34 renvois cassés, reproduction exacte du gisement du Vol. II. Corrigé avant la première pièce, il a coûté six caractères.

**Commits** : messages en anglais, format Conventional Commits — convention du Vol. II, retenue ici parce que ce volume prolonge son appareil (`docs(prd): …`, `docs(mono): draft chapter N — <slug anglais court>`, sujet ≤ 50 caractères quand possible, plafond 72). ⚠ Le Vol. I emploie des messages courts en français : vérifier le dossier de travail avant de rédiger le message.

### 1.4 Tableau de suivi des activités

**Source de vérité de l'avancement, au grain de l'activité.** Statuts : ☐ à faire · ◐ en cours · ☑ fait · ⊘ sans objet. À mettre à jour **au même commit** que l'activité qu'il décrit — *un statut qui ment est pire qu'un statut absent* (leçon du Vol. II, dont ce tableau a annoncé « 0 rédigée » pendant deux phases entières).

⚠ **Il existe un second tableau, au grain de la phase — §1.6 — et l'un des deux prime.** Le présent §1.4 est la **source de vérité** ; le §1.6 en est un **dérivé de clôture**, renseigné une fois par phase et jamais entre deux. En cas de divergence entre les deux, **§1.4 fait foi et §1.6 est corrigé**, jamais l'inverse. *Deux tableaux de suivi qui se contredisent, c'est le risque « décompte désynchronisé » du §8 appliqué à l'avancement lui-même : il se prévient en déclarant lequel gagne, pas en promettant de les tenir alignés.*

| Activité | Livrable / sortie | Statut | Date | Trace |
|---|---|---|---|---|
| **P0.1** Révision du TOC sur les neuf écarts (PRD §7.4) | TOC v0.5 | ☑ | 21 juill. 2026 | **Les neuf traités, tous revérifiés sur pièce avant correction.** Point instruit au passage : la **quatrième pièce du passeport** (attestations de conformité) est assignée aux ch. 7 §7.3 et 19 §19.2, **sans création de chapitre** |
| **P0.2** **Décision sur le corpus d'appui** (PRD §7.7) | `sources/` peuplé **ou** filiation retirée | ☑ | 21 juill. 2026 | **Décision d'auteur : filiation livresque retirée.** L-15 clos par **échec documenté** ; les sept sections et l'annexe E bloquées sont réaffectées au socle (table au TOC). Décision **réversible** au premier dépôt |
| **P0.3** Décision sur l'emplacement des documents de gouvernance (§1.3) | Arborescence arrêtée | ☑ | 21 juill. 2026 | `doc/` — tranché sur disque le 18 juill., **§1.3 amendé** ici. Deux renvois cassés corrigés, dont celui du **gabarit** (34 renvois évités) |
| **P0.4** Arborescence `monographie/` et `verification/` | Arborescence commitée | ☑ | 21 juill. 2026 | **34 pièces**, 9 dossiers de partie + `90-annexes/`, registre de gel initialisé. Contrôle exécuté : 34 fichiers, **40 liens relatifs, 40 résolus**, somme des cibles **102 500** |
| **P0.5** Gabarit de pièce (§5.4) | Gabarit commité | ☑ | 21 juill. 2026 | Appliqué aux 34 fichiers. **Thèse extraite du TOC par script**, jamais retranscrite : le verbatim de CA-05 est garanti par construction, et les deux pièces d'appareil **déclarent ne revendiquer aucun verbatim** |
| **P0.6** Revalidation d'ouverture des faits chauds (PRD §8.3) | `verification/revalidation-<date>.md` | ☑ | 21 juill. 2026 | [`revalidation-2026-07-21.md`](../verification/revalidation-2026-07-21.md) — **2 faits évolués** (brouillon CSA, conventions OTel), **1 confirmé en substance sans l'être en date** (révision MCP), 4 inchangés |
| **P0.7** Repointage des renvois `commun/faits-partages.md` | TOC v0.5 | ☑ | 21 juill. 2026 | **Trois renvois** repointés vers PRD §7.5. Renvois du README racine et du TOC du Vol. IV **signalés, non corrigés** (hors périmètre) |
| **P0.8** Contrôle de couverture bijective §6.2 ↔ TOC (34 pièces) | Section « Contrôle de couverture » du TOC | ☑ | 21 juill. 2026 | **34 contrôlées, 34 assignées.** Un orphelin trouvé et corrigé — **ACVM 11-348**, exigé par l'objectif O8, sans siège au TOC v0.4 ; quatre apports du TOC à reporter au PRD |
| **P0.9** Assignation des garde-fous et des lacunes aux pièces porteuses | Table d'assignation au TOC | ☑ | 21 juill. 2026 | **14 garde-fous sur 14, 14 lacunes sur 14.** Deux mentions portées : R-10 **sans objet à date mais armé** ; R-12 **sans instrument outillé** |
| **P0.10** Report des décisions P0.1 à P0.9 au PRD | **PRD v0.2** | ☑ | 21 juill. 2026 | Critère de sortie J-1. Dont un **écart nouveau** : PRD §7.4.6 nommait le dépôt `Monographies` — il s'appelle **`Agentique`** |
| **P1.1** Lot **L-03** — valeur probante de la carte signée (Q3) | `verification/lot-L-03-agent-card.md` + entrées F-xx | ☑ | 21 juill. 2026 | [Rapport](../verification/lot-L-03-agent-card.md) — **32 affirmations, 11 en [A], 5 écartées par le vote, 19 échecs de source**. Socle **F-01 à F-12**. **Q3 instruite** : la spécification interdit d'employer une clé révoquée **sans définir aucun moyen d'établir qu'elle l'est**. ⚠ Ch. 5 débloqué |
| **P1.2** Lot **L-08** — taxonomie des attaques (Q2) | `verification/lot-L-08-attaques.md` + entrées F-xx | ☑ | 21 juill. 2026 | [Rapport](../verification/lot-L-08-attaques.md) — **40 affirmations, 14 en [A], 9 écartées, 22 échecs**. Socle **F-13 à F-26**. **Q2 instruite, et le lot a réfuté la thèse qui l'avait commandé** (R-G-03). ⚠ Ch. 12 débloqué, thèse réécrite |
| **P1.3** Lot **L-15** — corpus d'appui | Extractions citées **ou** échec documenté | ☑ | 21 juill. 2026 | **Clos par échec documenté** (décision P0.2) : les trois ouvrages n'ont jamais été déposés. Reste à faire en P3-P4 : la **réécriture effective** des sept sections et de l'annexe E réaffectées |
| **P1.4** Relecture adversariale de la clôture P1 | Constats consignés | ☑ | 21 juill. 2026 | [`relecture-P1.md`](../verification/relecture-P1.md) — **trois** relecteurs indépendants (un de plus que prévu : la lentille **CA-12** exigeait une relecture dédiée). Verdict **unanime : à corriger** — **7 bloquants**, 17 majeurs. **Tous les bloquants traités le jour même.** ⚠ Elle a trouvé une **violation de R-12 dans le rapport de lot lui-même**, couverte par une attestation auto-délivrée fausse |
| **P2.1** à **P2.12** Lots L-01, L-02, L-04 à L-07, L-09 à L-14 | Un rapport par lot + entrées F-xx | ☑ | 21 juill. 2026 | **Douze rapports** sous `verification/`. **108 affirmations, 17 en [A], 3 écartées, 65 échecs de source.** Entrées **F-27 à F-78**. ⚠ **53 corrections de bornage** — contrôle introduit en P2 sur constat de la relecture P1.4 : 14 clauses d'exclusivité, 12 degrés injustifiés, 8 négatifs de corpus, 7 verbes excessifs, 6 promesses, 6 statuts non dits |
| **P2.13** PRD porté en v1.0 (socle propre constitué) | PRD v1.0 | ☑ | 21 juill. 2026 | **Cardinal re-mesuré : 78** (`grep … \| sort -u \| wc -l`), **non dérivé de la borne** — la coïncidence entre le cardinal et F-78 est signalée comme trompeuse |
| **P3.1** Rédaction et relecture adversariale des Parties I à VI (ch. 1 à 21) | 21 pièces rédigées, relues, corrigées | ☑ | 21 juill. 2026 | **21 pièces sur disque, toutes au statut « Rédigé et relu adversarialement »** — constat fichier par fichier, en-tête par en-tête. Relecteur distinct du rédacteur (CA-14) et **correctifs appliqués dans la même passe** : le point 6 de la boucle §5.2 est tenu **dans** le pipeline, non différé. Volumétrie re-mesurée par §1.5 sur les 21 : **86 579 mots** pour **63 000** de cible, **+37,4 %** — *écart documenté, non corrigé par amputation*. Traces : [`relecture-P3-partie-I.md`](../verification/relecture-P3-partie-I.md) et le journal de traitement au § Notes de chaque pièce |
| **P3.2** Amendement du socle demandé par la rédaction | PRD v1.1, §7.10 | ☑ | 21 juill. 2026 | **Douze affirmations retenues par L-01, L-02 et L-12 et non versées** ont été réclamées par la Partie I ([R-G-05](../verification/remontees-gouvernance.md)) ; **onze entrées versées, F-79 à F-89**. Socle propre **re-mesuré à 89** (commande de PRD §7.3, `sort -u`, exécutée le 21 juill. 2026 — **non dérivée de la borne**). Dont **F-36 rétrogradée [B] → [C]** par la règle de composition et un **renvoi de F-30 corrigé**. ⚠ Aucun lot rouvert, aucune passe d'instruction : *un versement est un acte de socle, non de recherche* |
| **P3.3** Relecture dédiée **CA-12** (dualité d'usage, R-12) | `verification/relecture-CA-12-P3.md` | ☑ | 21 juill. 2026 | [Compte rendu déposé](../verification/relecture-CA-12-P3.md) — Partie IV lue intégralement (ch. 12 à 15), plus 4 sections hors partie atteintes par balayage ; **1 retrait** : une attestation auto-délivrée au ch. 15 §15.3. ⚠ **Le contrôle déclare lui-même son périmètre incomplet** : 26 pièces **balayées et non relues**, et **12 rapports de lot sur 14 jamais relus** au titre de R-12 alors que PRD §8.5 les couvre. *Un balayage n'est pas une relecture* |
| **P3.4** Arbitrage des remontées de gouvernance (§5.3) | [`verification/remontees-gouvernance.md`](../verification/remontees-gouvernance.md) | ☑ | 21 juill. 2026 | **42 remontées, R-G-01 à R-G-42** — dont **38 ouvertes par P3** : R-G-05 à R-G-22 avant la rédaction du tronc, **R-G-23 à R-G-42 dépouillées des Notes des 21 pièces et du compte rendu CA-12** après elle. ⚠ **Le cardinal a doublé après la rédaction, et c'est le résultat attendu** : une pièce ne sait ce qui manque au cadrage qu'en butant dessus. Statuts re-mesurés marqueur par marqueur à la clôture : **39 tranchées, 3 sans objet, 0 ouverte**. ⚠ **Douze de ces arbitrages sont DÉLÉGUÉS** — R-G-08, R-G-09, R-G-13 à R-G-15, R-G-17, R-G-37 à R-G-42 portaient sur une thèse, un intitulé, une cible de volumétrie, un garde-fou et son instrument, ou une lecture d'annexe : ce que §5.3 réserve à l'auteur **sans exception**. Ils ont été rendus par l'instance d'exécution de P3 **sur instruction de clôture de l'auteur**, chacun sur l'option la plus réversible, motivé, et **révocable — l'option écartée est conservée** |
| **P4** Parties VII à IX, avant-propos, annexes A à E (ch. 22 à 28 + 6 pièces) | 13 pièces | ☐ | | Détail : §6 |
| **P5.1** Revalidation temporelle finale | `verification/revalidation-<date>.md` | ☐ | | Datée de moins de 30 jours à la publication |
| **P5.2** Relecture CA-01 à CA-14 | `verification/relecture-CA.md` | ☐ | | Balayage §A.6 **+ inspection humaine** |
| **P5.3** Cohérence globale (décomptes, renvois) | Balayage + relecture | ☐ | | Dont synchronisation des chiffres publiés (§7, risque « décompte désynchronisé ») |
| **P5.4** Assemblage, PDF, publication | `Monographie.md` + `Monographie.pdf` | ☐ | | PDF versionné **avec** sa source (règle du dépôt) |

**Décompte de contrôle (21 juillet 2026, après la rédaction du tronc)** : 34 unités de rédaction — **21 rédigées et relues adversarialement, 13 au gabarit** (constat fichier par fichier sur `monographie/`). Volumétrie des 21 : **86 579 mots** re-mesurés par §1.5 pour **63 000** de cible (**+37,4 %**) ; cible du volume entier : **102 500**, inchangée. Socle propre : **89 entrées re-mesurées** (F-01 à F-89). **Lots clos : 14 sur 15, plus L-14 partiellement clos** — son rapport declare n'avoir pas instruit les metriques du ch. 26. Affirmations instruites : **180** ; soumises au vote adversarial : **80** ; **écartées : 17**. Corrections de bornage : **53**. Échecs de source consignés : **106**. Remontées de gouvernance : **42 consignées — 39 tranchées, 3 sans objet, 0 ouverte** ; ⚠ **douze de ces arbitrages sont délégués et révocables**. Phases : **P0, P1, P2 et P3 closes** ; P4 et P5 ☐.

⚠ **La regle cardinale ne bloque plus qu'un chapitre — et c'est le moment ou elle protege le moins.** Quatorze lots etant clos, seul le **ch. 26** demeure interdit d'ecriture par §7.0 : L-14 n'a pas instruit ses metriques. Ce qui demeure, ce sont les **dépendances éditoriales** du §5.1 : le ch. 4 ouvre l'ouvrage, le ch. 8 se rédige **après** le ch. 9, les six chapitres de composition attendent leurs chapitres amont. *Un socle constitué autorise la rédaction ; il ne la planifie pas.*

⚠ **Le passage de « 34 en attente » à « 34 au gabarit » n'était pas un progrès de rédaction.** Un gabarit est un fichier vide muni de son en-tête ; il ne vaut ni brouillon ni ébauche. **Treize pièces y demeurent** — l'avant-propos, les ch. 22 à 28 et les cinq annexes —, et c'est la matière de P4.

### 1.5 Commande de référence du décompte de volumétrie

**Fixée avant la première pièce, et non après la vingt-neuvième.** Seule autorité de décompte du volume.

```sh
# Corps = du premier séparateur "---" jusqu'à "## Notes" OU au premier
# commentaire HTML de gouvernance, selon ce qui vient en premier.
# Un mot = un jeton portant au moins une lettre ou un chiffre, accents compris.
# LC_ALL=C.UTF-8 n'est PAS décoratif : voir l'avertissement ci-dessous.
awk '/^---$/{f=1;next} /^## Notes/{exit} /^<!--/{exit} f' FICHIER \
  | tr -s '[:space:]' '\n' | LC_ALL=C.UTF-8 grep -cE '[[:alnum:]]'
```

Sont **hors décompte** : l'en-tête (tableau de champs, thèse citée), les notes, le bloc de gouvernance en commentaire. Sont **dans** le décompte : la prose, les encadrés et les tableaux du corps — une pièce à forte densité de tableaux (annexe B, ch. 4, ch. 27) porte de ce fait un décompte structurellement plus élevé à contenu égal.

⚠ **Éprouvée sur un domaine entier avant d'être publiée, et non sur un échantillon.** Le Vol. II a publié sa commande après l'avoir testée sur deux fichiers, pour vingt-neuf ; elle était fausse. Celle-ci a été exécutée le 18 juillet 2026 sur les **29 pièces du Vol. II** — le seul corpus comparable existant, celui du Vol. III étant vide. Résultats, tous reproductibles :

| Locale | Classe de caractères | Total sur les 29 pièces du Vol. II | Verdict |
|---|---|---|---|
| `C` | `[[:alnum:]]` | **92 059** | Commande du Vol. II — **reproduit exactement son chiffre publié**, ce qui valide le portage |
| **`C.UTF-8`** | **`[[:alnum:]]`** | **93 242** | **Retenue ici** — `+1 183` mots, `+1,29 %` |
| `C.UTF-8` | `\p{L}\p{N}` (PCRE) | 93 242 | Concorde — la saveur de regex n'a pas d'incidence |
| `C` | `\p{L}\p{N}` (PCRE) | 95 595 | **Fausse** — sur-compte de 2 353 |

**Deux enseignements, et le second n'était pas attendu.** (1) En locale `C`, `[[:alnum:]]` ne reconnaît aucun caractère accentué : la commande du Vol. II sous-compte d'environ 1,3 %, ce que son propre plan estimait à « 1,3 % » — l'estimation est confirmée au centième près. (2) **Passer à PCRE sans fixer la locale est pire que le défaut qu'on prétend corriger** : en mode octet, `\p{L}` capte les octets internes des caractères multi-octets et compte comme des mots les tirets cadratins, les guillemets français et les flèches — exactement les jetons que la commande existe pour écarter. **C'est la locale qui décide, pas la saveur de regex.**

**Pourquoi le Vol. III corrige là où le Vol. II ne pouvait pas.** Le Vol. II a tranché en connaissance de cause : tous ses décomptes publiés dérivaient de la commande fautive, et la corriger d'autorité aurait rendu faux, d'un seul coup, chaque chiffre publié avant ce jour — pour un gain de 1,3 % sur une métrique déclarée non normative. Le remède aurait été pire que le mal. **Le Vol. III n'a aucun décompte publié** : le coût de la correction y est nul, et il serait absurde d'hériter d'une dette qu'on n'a pas contractée. ⚠ **Corollaire** : les volumétries du Vol. II et du Vol. III **ne sont pas comparables entre elles** sans re-mesure par une commande unique. Toute comparaison inter-volumes (Vol. IV, notamment, dont le cadrage annonce d'agréger les trois corpus) commence par une re-mesure.

### 1.6 Tableau de suivi d'exécution des phases

**Grain de la phase. Dérivé de §1.4, qui prime.** Une ligne par phase, renseignée **à la clôture de cette phase et à ce moment-là seulement** — jamais par anticipation, jamais en cours de route. Une phase est close quand **toutes** ses activités de §1.4 portent ☑ ou ⊘ **et** que son critère de sortie est constaté sur pièce.

⚠ **Ce tableau porte une colonne que le plan n'avait pas prévue : « Ce que l'exécution a démenti ».** Elle existe parce que les deux premières phases ont chacune trouvé, en s'exécutant, une erreur du document qui les prescrivait — et qu'un plan qui n'enregistre que ses succès cesse d'être un instrument de contrôle. *Une phase qui ne dément rien n'a probablement pas été vérifiée.*

| Phase | Jalon | Statut | Ouverte | Close | Livrables produits | Ce que l'exécution a démenti |
|---|---|---|---|---|---|---|
| **P0** — Assainissement du cadrage | J-1 | ☑ | 18 juill. 2026 | **21 juill. 2026** | TOC v0.5 ; PRD v0.2 ; PRDPlan v0.2 ; `monographie/` (34 gabarits + registre de gel) ; `verification/revalidation-2026-07-21.md` ; tables de couverture et d'assignation au TOC | **Quatre démentis.** (1) PRD §7.4.6 nommait le dépôt `Monographies` : il s'appelle **`Agentique`** — dixième écart, trouvé dans le paragraphe qui corrigeait une homonymie. (2) La filiation de repli du PRD §7.7 (« GoF/EIP que le Vol. I mobilise déjà ») est **à moitié fausse** : EIP oui, **GoF non**, et le Vol. I ne porte aucun gabarit de patron. (3) Le contrôle de couverture a trouvé **un orphelin** que le plan ne soupçonnait pas — l'avis ACVM 11-348, exigé par l'objectif O8, sans siège au TOC v0.4. (4) La revalidation d'ouverture a fait bouger **deux faits chauds sur sept**, dont le brouillon CSA que le socle hérité gelait à mars 2026 |
| **P1** — Lots bloquants | J-2 | ☑ | 21 juill. 2026 | **21 juill. 2026** | `verification/lot-L-03-agent-card.md` ; `verification/lot-L-08-attaques.md` ; `verification/remontees-gouvernance.md` ; `verification/relecture-P1.md` ; **PRD v0.3 §7.8 — socle propre de 26 entrées F-01 à F-26** ; TOC v0.6 (deux thèses réécrites) ; PRDPlan §3.1 (plan de réécriture arrêté pièce par pièce) | **Quatre démentis, et deux visent le cadrage lui-même.** (1) **Le lot chargé d'établir la thèse quantitative l'a réfutée** : sur les dix intitulés du référentiel OWASP 2026, un seul porte « Identity », aucun ne porte « Delegation » (F-18). La thèse d'ensemble passe de **quantitative à architecturale** (R-G-03). (2) **R-13 était inopérant** : les trois échelles d'autonomie du Vol. I **partagent leurs libellés**, et « copilote » y désigne trois objets distincts — nommer l'échelle ne la distinguait pas (R-G-01). (3) **H-31 n'est pas élevable** : c'est une construction d'auteur du Vol. I, sans source primaire tierce à lire — l'élévation prescrite par §A.5 était sans objet (R-G-02). (4) **R-08 était faux** : des incidents publics d'identité non humaine sont datés et documentés (F-21). ⚠ **Et un cinquième, trouvé par la relecture P1.4, qui vise l'exécution et non le plan** : **le vote protège les affirmations, pas la prose qui les résume** — quatre synthèses avaient réintroduit des négatifs de corpus que le vote venait de tuer, et le rapport L-08 portait **trois passages opératoires** couverts par une attestation R-12 **auto-délivrée et fausse** |
| **P2** — Reste du socle | J-3 | ☑ | 21 juill. 2026 | **21 juill. 2026** | Douze rapports de lot sous `verification/` ; **PRD v1.0 §7.9 — 52 entrées F-27 à F-78** ; socle propre porté à **78 entrées re-mesurées** | **Trois démentis, et deux visent la phase précédente.** (1) **La revalidation d'ouverture s'était trompée deux fois** : la « mise à jour du brouillon CSA au 20 mai 2026 » **n'existe pas** — le balayage de la page ne relève aucune date postérieure au 27 mars (F-39) —, et l'échelle de maturité d'OpenTelemetry compte **cinq** échelons, non trois (F-76). *Une correction non vérifiée à la source n'est qu'une seconde erreur.* (2) **La divergence AP2 se résout par le fait, et personne n'avait tort** : le transfert est annoncé par une source primaire datée (F-44), et **n'est pas matérialisé** trois mois après — dépôt inchangé, aucune spécification agentique publiée par le cessionnaire (F-45). Les deux volumes décrivaient deux choses différentes. (3) **La divergence de date de l'AMF demeure entière, pour une raison que nul n'avait prévue** : **aucune des deux dates ne figure à la source primaire**, qui ne date qu'au mois (F-67) |
| **P3** — Rédaction du tronc (ch. 1-21) | J-4 | ☑ **close — les trois termes du critère de sortie constatés un par un** : (1) 21 chapitres ayant passé la boucle §5.2, relecture adversariale comprise, **statuts relevés sur disque** ; (2) registre de gel complet, 21 lignes renseignées et volumétries re-mesurées ; (3) **remontées toutes tranchées**, 39 sur 42, 3 sans objet, 0 ouverte. ⚠ **Douze l'ont été par arbitrage DÉLÉGUÉ**, sur instruction de clôture de l'auteur, et **chacun est révocable** | 21 juill. 2026 | **21 juill. 2026** | **Constatés sur disque le 21 juillet 2026, fichier par fichier.** `monographie/01-partie-I/` à `monographie/06-partie-VI/` — **21 pièces portant un corps**, toutes au statut « Rédigé et relu adversarialement », **86 579 mots** re-mesurés par §1.5 pour 63 000 de cible ; `verification/relecture-P3-partie-I.md` ; `verification/relecture-CA-12-P3.md` ; `verification/remontees-gouvernance.md` porté à **42 remontées** ; `verification/relecture-P3.md` ; **PRD v1.1 — §7.10, onze entrées F-79 à F-89**, socle propre re-mesuré à **89**. ⚠ **Les 13 autres pièces sont au gabarit** : elles relèvent de P4 | **Cinq démentis, et le premier vise l'ordre même du travail.** (1) **Le socle avait été constitué avant que la rédaction ne dise ce dont elle avait besoin** : douze affirmations retenues par L-01, L-02 et L-12, laissées au rapport de leur lot, étaient précisément celles qui manquaient aux premières pièces (R-G-05) — d'où le siège **§7.10** et onze entrées versées. *C'est l'ordre normal, et c'est pourquoi il produit ce genre de manque.* (2) **La boucle qualité §5.2 avait été exécutée une première fois sans son point 6** : quatre chapitres sont restés au dépôt avec **quatorze réfutations bloquantes** non traitées. La parade n'a pas été de rappeler la règle mais de placer l'étape corrective **dans** le pipeline plutôt qu'après lui. (3) **L'écart de volumétrie de +37,4 % vient des bornes rétablies, non d'un ajout de matière** — le ch. 4 était à **3 376 mots** quand R-G-17 a été ouverte, il en porte **3 912** une fois ses correctifs appliqués : plusieurs pièces ont grossi **après** leur relecture. La cible du TOC était donc calibrée sur une prose **moins bornée** que celle que les garde-fous imposent, et couper davantage supprimerait des bornes. (4) **Le défaut dominant est resté le même qu'aux deux phases précédentes** — la borne du socle perdue dans la prose : c'est un défaut de **niveau d'écriture**, non de phase, et aucune clôture de phase ne l'éteindra. (5) **La relecture CA-12 a établi que son propre périmètre ne couvre pas le fichier où la faute s'est produite la première fois** : sur les **14 rapports de lot** déposés, **12 n'ont jamais été relus** au titre de R-12 — dont L-09 et L-10, qui portent la matière des ch. 13 et 15 —, alors que PRD §8.5 les couvre depuis le 21 juillet 2026. **(6) Et le dernier dément le plan lui-même : la phase ne pouvait pas se clore par sa propre mécanique.** Le critère J-4 exige que les remontées soient **toutes** tranchées, et §5.3 en réserve une classe entière à l'auteur **sans exception** — mais **le plan n'avait désigné aucune instance capable de trancher cette classe-là**. Un critère de sortie dont un terme n'est atteignable par personne n'est pas un critère : c'est un blocage structurel, et il est resté invisible tant qu'aucune remontée de cette classe n'était ouverte. Douze l'étaient à la clôture. *La parade retenue — l'arbitrage délégué, tracé et révocable — est une réponse à l'espèce ; la lacune du plan, elle, demeure et se pose à l'identique en J-5.* **(7) Un dernier démenti, produit par la phase contre elle-même** : deux agents de la même passe ont **désynchronisé un décompte en l'écrivant simultanément** — l'un recopiait « six remontées en attente » pendant que l'autre en ouvrait vingt de plus. Le risque « décompte désynchronisé entre porteurs » de §8 existait, mais sa parade le renvoyait à **P5.3**, deux phases après la naissance de l'écart, et son signal ne nommait que des porteurs publiés. *Le travail en parallèle ne désynchronise pas seulement les documents entre eux : il désynchronise les documents d'avec le travail qui les écrit.* |
| **P4** — Application et exploitation (ch. 22-28, appareil) | J-5 | ☐ | | | | |
| **P5** — Revalidation et publication | J-6 | ☐ | | | | |

**Règle de mise à jour, en trois points pour qu'aucun ne se perde :**

1. **À la clôture d'une phase**, et au **même commit** que la dernière activité de cette phase : renseigner la ligne — statut, date de clôture, livrables **constatés sur disque** (pas annoncés), démentis.
2. **Les livrables se listent depuis le disque**, jamais depuis le tableau des activités : c'est le seul point où ce tableau ne dérive pas de §1.4, et c'est voulu — il sert de contre-vérification. Un livrable inscrit ici et absent du dépôt est la faute que ce tableau existe pour attraper.
3. **Une phase ne se clôt pas parce que le calendrier avance** : elle se clôt sur son critère de sortie (§2 pour J-1, §3 pour J-2, §4 pour J-3, §5 pour J-4, §6 pour J-5, §7 pour J-6). Une phase dont le critère n'est pas atteint reste ◐, et la ligne le dit. ⚠ **Une ligne ◐ se renseigne donc en cours de phase, par exception à l'en-tête ci-dessus** : elle porte ses livrables constatés à date, laisse sa date de clôture vide et **nomme dans la colonne « Statut » le terme du critère qui manque**. C'était l'état de la ligne P3 pendant la phase : le tronc rédigé, douze remontées non tranchées. ☑ **P3 est close depuis** — les douze ont été rendues par **arbitrage délégué**, et les trois termes du critère ont été constatés un par un.

⚠ **P2 et P3 se recouvrent (§1.2).** Le tableau ci-dessus les présente en séquence parce qu'il suit les jalons, non le calendrier réel : **deux phases peuvent porter ◐ en même temps**, et cela ne signale aucune anomalie. Ce qui en signalerait une, c'est une phase ☑ dont une activité de §1.4 serait restée ☐.

---

## 2. Phase P0 — Assainissement du cadrage (J-1) — ☑ **close le 21 juillet 2026**

**Aucune rédaction, aucune recherche.** P0 met le cadrage en état d'être exécuté.

⚠ **Le tableau ci-dessous est conservé tel qu'il prescrivait**, et non réécrit à la lumière de ce qui a été fait : un plan qu'on récrit après coup cesse d'être vérifiable. Ce qui a effectivement été exécuté est consigné au tableau de suivi §1.4, avec sa date et sa trace ; les écarts entre la prescription et l'exécution sont relevés en fin de section.

| # | Tâche | Vérification de sortie |
|---|---|---|
| P0.1 | **Réviser le TOC** sur les **neuf** écarts de PRD §7.4, repris un à un dans l'ordre : **(1)** numérotation réelle du Vol. I et règle de nommage du fichier ; **(2)** renvoi §7.0, et non §7.0.1 ; **(3)** siège de Boréalis à l'Annexe B ; **(4)** siège du KYA à `Monographie.md` §5.5.4 ; **(5)** sièges de la formule de non-compositionnalité ; **(6)** homonymie « AgentMesh » et sa justification corrigée — **c'est elle qui fonde la branche (f) de R-04** ; **(7)** homonymie des étiquettes Q entre ch. 16 et ch. 21 du Vol. II ; **(8)** retrait du risque 9(b), périmé ; **(9)** retrait de la moitié `eval.md` du risque 9(a) | TOC v0.5. Contrôle : les **neuf** sont traités, pas huit — chaque renvoi du TOC vers le Vol. I nomme son fichier, chaque renvoi vers une question du Vol. II nomme son chapitre |
| P0.2 | **Trancher le corpus d'appui** (PRD §7.7) : déposer les trois ouvrages dans `sources/`, **ou** retirer la filiation livresque et réaffecter les sept sections et l'annexe E. **Deux corrections du TOC y sont rattachées** — elles relèvent de §7.7, non des neuf écarts de §7.4 : le titre de section (« déposé au dépôt »), et l'incohérence interne sur l'étendue du biais Google Cloud | Décision consignée au TOC et au PRD. **Si retrait** : §27.4 se reconstruit sur H-31 et la grille du ch. 4 ; l'annexe E revendique la filiation GoF/EIP que le Vol. I mobilise déjà |
| P0.3 | **Trancher l'emplacement** des documents de gouvernance (§1.3) | Arborescence arrêtée et commitée |
| P0.4 | Créer `monographie/` (34 gabarits) et `verification/` ; initialiser `99-registre-gel.md` | Arborescence commitée |
| P0.5 | Fixer le **gabarit de pièce** (§5.4) | Gabarit appliqué aux 34 fichiers |
| P0.6 | **Revalidation d'ouverture** des faits chauds (PRD §8.3) | Rapport daté ; chaque fait marqué inchangé / évolué avec sa source ; PRD amendé si évolution |
| P0.7 | **Repointer les renvois** vers `commun/faits-partages.md` (PRD §7.5) — le fichier n'existe pas et n'est pas créé ; les divergences vivent au PRD §7.5 | Renvois du TOC redirigés. ⚠ Les renvois du README racine et du TOC du Vol. IV sont **hors périmètre de ce volume** : les signaler, ne pas les corriger |
| P0.8 | **Contrôle de couverture bijective** §6.2 ↔ TOC, sur les **34 pièces** — appareil compris | Aucun élément de contenu obligatoire orphelin ; aucune pièce du TOC introduisant du contenu absent du PRD |
| P0.9 | **Assigner chaque garde-fou R-01 à R-14 et chaque lacune §10 à une pièce porteuse** | Table d'assignation au TOC. *Un garde-fou non assigné est un garde-fou non appliqué* |

⚠ **P0.2 est la seule tâche du plan qui ne se délègue pas.** Elle engage la bibliographie de l'ouvrage, sept sections et une annexe — réparties sur **six pièces** (ch. 4, 9, 25, 27, 28 et l'annexe E). Les autres tâches de P0 sont mécaniques.

⚠ **P0.6 n'est pas une formalité de calendrier.** La révision majeure de la spécification MCP est attendue le **28 juillet 2026**, soit dix jours après la date de ce plan, et elle touche les ch. 2 et 22. Si P0 s'étend au-delà, elle est intégrée à l'ouverture plutôt que revalidée à la fin.

**Critère de sortie J-1** : TOC v0.5 **et PRD v0.2** ; décision corpus d'appui consignée ; bijection §6.2 ↔ TOC vérifiée sur les **34 pièces** ; **chaque garde-fou R-01 à R-14 et chaque lacune §10 assignés à une pièce porteuse**. *Un garde-fou non assigné est un garde-fou non appliqué.*

### 2.1 Constat de clôture — ce que l'exécution a trouvé que la prescription n'avait pas prévu

**Cinq écarts entre le plan et le terrain**, consignés parce qu'ils qualifient la suite :

1. **P0.2 a été tranchée par le retrait, non par le dépôt.** Le rejeu de la vérification (21 juillet 2026) a confirmé l'absence des trois ouvrages jusque dans l'historique git. **L-15 est le premier lot clos du volume — par échec documenté.** Huit pièces sont réaffectées ; le risque bascule de la *filiation empruntée* vers la **compensation par l'inférence**, et c'est CA-07 qui le tient.
2. **Le contrôle de couverture a trouvé un orphelin que personne n'attendait** : l'avis **ACVM 11-348**, exigé par l'objectif O8 du PRD, n'avait de siège dans aucune pièce du TOC v0.4. Assigné au ch. 20 §20.1. *Le contrôle qui ne trouve rien n'a pas été fait.*
3. **Un dixième écart est apparu, et il siège dans le PRD, non dans le TOC** : §7.4.6 nomme le dépôt `Monographies`. Il s'appelle **`Agentique`**. Corrigé au PRD v0.2 — et l'ironie est consignée : c'est le paragraphe qui traite d'une homonymie qui en portait une.
4. **Une proposition du PRD §7.7 s'est révélée à moitié fausse à l'exécution** : la filiation de repli « GoF/EIP que le Vol. I mobilise déjà » ne tient que pour **EIP**. Le Vol. I ne mobilise pas GoF et ne porte aucun gabarit de patron ; le gabarit de l'annexe E est donc une **construction d'auteur**, et il le dit.
5. **La revalidation d'ouverture a fait bouger deux faits chauds sur sept**, dont un — le brouillon CSA — que le socle hérité donnait pour l'état de mars 2026 et qui a été mis à jour en mai. **L-05 réinstruit avant le ch. 7 ; H-03 s'amende au socle, pas dans la pièce.**

⚠ **Ce que P0 n'a pas fait, et ne pouvait pas faire.** Elle n'a créé **aucune entrée de socle**, clos **aucun lot d'instruction** hors L-15, arbitré **aucune divergence** (AP2, date de la ligne directrice de l'AMF) et rédigé **aucune ligne** des 34 pièces. *Un cadrage assaini n'est pas un ouvrage commencé.*

---

## 3. Phase P1 — Les trois lots bloquants (J-2) — ☑ **close le 21 juillet 2026**

Ces trois lots ne se contournent pas par une reformulation prudente : leur échec supprime un chapitre ou le réduit à une lacune.

| # | Lot | Ce qu'il doit établir | Si échec |
|---|---|---|---|
| P1.1 | **L-03** — carte d'agent signée (Q3 du Vol. II ch. 21) | Ancrage de confiance, régime de révocation, gouvernance des clés — **ou l'établissement que la spécification ne les documente pas** | Le ch. 5 devient un chapitre de lacune instruite, et **le ch. 8 perd une de ses quatre pièces** : le passeport se construit alors sur trois, et le dit |
| P1.2 | **L-08** — taxonomie des attaques (Q2 du Vol. II ch. 21) | Identifiants de vulnérabilité, incidents publics datés, littérature académique | La Partie IV se réduit à une reprise du Vol. I. **Le ch. 12 §12.4 devient le cœur du chapitre** — « ce que la recension ne trouve pas » —, sous R-08 |
| P1.3 | **L-15** — corpus d'appui ☑ | Extraction citée, chapitre par chapitre | **C'est l'issue survenue** : sept sections et l'annexe E se réécrivent sans lui (P0.2, 21 juill. 2026) |

**Un échec instruit est un résultat ; une lacune non instruite n'en est pas un.** Le rapport de lot consigne ce qui a été tenté, avec quelles sources et pourquoi cela échoue — c'est ce qui autorise le gabarit « passe conduite et infructueuse » plutôt que « aucune passe conduite » (§5.5).

⚠ **R-12 s'applique dès l'instruction de L-08, pas seulement à la rédaction.** Un rapport de lot qui rassemblerait des séquences d'exploitation serait dans le dépôt, donc publié. La recension cite les identifiants et décrit le maillon qui cède ; elle ne reproduit rien.

**Critère de sortie J-2** : Q2 et Q3 instruites ou leur échec documenté ; premières entrées F-xx du socle propre, avec leur niveau ; corpus d'appui **déposé**, **ou** sept sections et l'annexe E **réécrites sans lui**. ⚠ La décision de P0.2 ne suffit pas à clore J-2 : c'est la **réécriture effective** qui le clôt, et elle se fait en P3 et P4 pour les pièces concernées. J-2 est clos quand le plan de réécriture est arrêté pièce par pièce.

### 3.1 Plan de réécriture des sections privées de corpus d'appui — arrêté pièce par pièce

**C'est la troisième condition du critère de sortie J-2**, et la seule que P0 ne pouvait pas remplir : la décision de retrait s'y prend, la réécriture s'y prépare, l'exécution appartient à P3 et P4. Le tableau ci-dessous **arrête** ce plan.

⚠ **Sept sections et une annexe, mais six pièces seulement** : §4.4 et §9.4 vivent dans deux chapitres distincts, §25.1 et §25.5 dans le même, §27.4 et §27.5 dans le même. Compter huit fichiers serait faux.

| Pièce | Section | Ce qui est retiré | Ce qui la porte désormais | Marquage imposé | Phase |
|---|---|---|---|---|---|
| **ch. 4** | §4.4 | le spectre de maturité tiers | **H-31** — échelle *assistance → copilote → orchestration sous revue → autonomie bornée* (`Monographie.md` §5.0.2, siège §5.1.1), **nommée** ; croisée avec Q-A…Q-E (PRD Annexe C) | **R-13** (l'échelle est nommée, trois coexistent au Vol. I) ; **CA-07** sur le croisement | P3 |
| **ch. 9** | §9.4 | la typologie des patrons d'interaction humain-agent | **H-15**/PC3 (le point d'arrêt humain) et **H-06** (art. 12.1, révision par une personne en mesure de réviser) | **CA-07** ; H-15 est une **thèse du Vol. II à attribuer**, jamais un fait de socle | P3 |
| **ch. 25** | §25.1 | test-débogage-évaluation-déploiement d'un manuel | **H-23** — immaturité déclarée de la science de l'évaluation (`Monographie.md` §7.6.4) ; littérature MLOps/LLMOps transposée, **filiation établie explicitement plutôt que réinventée** | **CA-09** — l'évaluation entre par la revalidation du passeport, **pas** par la science de l'évaluation en général (PRD §5.1) | P4 |
| **ch. 25** | §25.5 | les patrons d'apprentissage | **H-11** — adaptation éphémère vs évolution persistante ; **H-15**/PC4 | **CA-07** ; ⚠ **lacune 9** (*frame* opérationnel non caractérisé) : **ne pas s'y adosser** | P4 |
| **ch. 27** | §27.4 | les trois modèles de maturité articulés | **H-31** + la grille du ch. 4 | **CA-07 à l'ouverture de la section** — construction d'auteur **en totalité**, plus aucun modèle source n'étant rapporté ; **R-13** | P4 |
| **ch. 27** | §27.5 | « making agentic AI enterprise-ready » | **H-30** — le plan de contrôle obligatoire, **principe seul, jamais son instanciation sur produits nommés** ; PRD Annexe B §B.2 | **CA-07** — la structure de rôles est une inférence d'auteur que rien du socle ne documente | P4 |
| **ch. 28** | §28.4 | le cas fil rouge *loan processing* externe | **H-32** — Boréalis, siège **Annexe B** du Vol. I (`Chapitres/Annexe B - Architecture de Solutions.md`) | ⚠ **Perte déclarée dans le texte** : la confrontation devient **interne au corpus** et ne vaut plus réfutation externe. La section le dit — elle ne le masque pas | P4 |
| **annexe E** | pièce entière | la discipline des patrons d'un manuel | **EIP** — Hohpe & Woolf (2003), soixante-cinq patrons, mobilisés par le Vol. I en `Monographie.md` §1.6.1.1 | **Le gabarit à six champs est une construction d'auteur du Vol. III**, déclarée à l'ouverture : le Vol. I n'en porte aucun et **ne mobilise pas GoF** | P4 |

**Le contrôle qui prouve la réécriture, et il est mécanique.** Le motif de balayage **R-10** du PRD §A.6 — `Arsanjani|Bustos|Nagasubramanian|Ranjan|Chembachere|Lobo` — doit retourner **zéro occurrence dans le corps des 34 pièces** à la relecture P5.2. Une occurrence subsistante signifie que la réécriture n'a pas eu lieu et qu'une pièce cite un ouvrage que personne n'a ouvert. ⚠ **Le motif reste armé précisément pour cela** : il ne sert plus à encadrer un usage, il sert à détecter un usage impossible.

⚠ **Trois pièges de cette réécriture, nommés pour n'avoir pas à les redécouvrir.** (1) **La compensation par l'inférence** — huit endroits privés de leur cadre externe, huit endroits où l'on comble ; CA-07 sans indulgence est la seule parade. (2) **La surcharge de H-31** — quatre des huit réaffectations s'appuient sur l'autonomie graduée ou sur la grille ; un socle mince ne devient pas épais parce qu'on le cite plus souvent, et chaque emploi doit dire ce que H-31 établit **et ce qu'elle n'établit pas**. (3) **H-31 est une entrée [C] qui ne peut pas être élevée** — et ce n'est pas une dette, c'est une propriété de la source. L'échelle est une **construction d'auteur du Vol. I** (« La proposition de l'ouvrage… », `Monographie.md` §5.0.2), non la reprise d'un texte tiers : l'élévation prescrite par PRD §A.5 est **sans objet**. Régime applicable : **thèse d'un volume antérieur, à attribuer à chaque emploi, ne portant jamais un fait central** — ce qui est régulier pour §4.4 et §27.4, l'une et l'autre étant des **constructions d'auteur marquées** (CA-07). ⚠ *Correction du 21 juillet 2026 (remontée **R-G-02**) : la première rédaction de ce piège prescrivait « leur élévation est à instruire en P2 » — une instruction que la remontée du même jour déclarait impossible. Deux documents de gouvernance donnaient des consignes contradictoires pour les deux mêmes sections, et c'est l'artefact qui clôt J-2 qui portait la mauvaise.*

---

## 4. Phase P2 — Le reste du socle (J-3) — ☑ **close le 21 juillet 2026**

Les **douze autres lots** (PRD §7.6), nommés pour qu'aucun ne se perde entre les phases :

| Lot | Objet | Chapitres débloqués |
|---|---|---|
| **L-01** | Identité machine héritée, étirement des RFC, jetons de transaction, WIMSE | ch. 1, 2 |
| **L-02** | Corpus W3C — VC Data Model, DID Core, chartes des CG | ch. 3 |
| **L-04** | Entra Agent ID et ses pairs infonuagiques | ch. 6 |
| **L-05** | Registres — brouillon CSA à date, consolidation IETF, registres A2A/AGNTCY | ch. 7 |
| **L-06** | Chaîne de mandat, AP2, *on-behalf-of* — **porte l'arbitrage de la divergence AP2** | ch. 9 |
| **L-07** | KYA, OpenID Foundation, précédents de fédération | ch. 11 |
| **L-09** | *Rug-pull*, attestation d'intégrité, inventaire de la révocation, précédent PKI | ch. 13, 14 |
| **L-10** | SOC agentique, référentiels de sécurité 2026 | ch. 15 |
| **L-11** | Horloge post-quantique, crypto-agilité, études de coût | ch. 16, 17, 18 |
| **L-12** | E-23, ligne directrice AMF article par article, art. 12.1, désignation (Q5) | ch. 19, 20, 21 |
| **L-13** | Maillage — passerelles MCP, courtage A2A, SLIM, moteurs de politique, *zero trust* | ch. 22, 23 |
| **L-14** | Conventions sémantiques OpenTelemetry, plateformes d'observabilité | ch. 24, 26 |

**Les douze sont parallélisables : aucun ne dépend d'un autre.** Un seul porte une charge supplémentaire — **L-06 doit ~~trancher~~ *instruire* la divergence de gouvernance d'AP2** (PRD §7.5), qui conditionne le ch. 9 et croise le ch. 16 §16.3 Q2 du Vol. II. Ce n'est pas une dépendance entre lots, c'est une charge interne à celui-là.

⚠ **Verbe corrigé le 21 juillet 2026 à l'ouverture de P2 — remontée [R-G-04](../verification/remontees-gouvernance.md), et l'écart n'était pas verbal.** Le PRD §7.5 pose que le Vol. III **porte** les divergences et **ne les tranche pas** ; ce plan écrivait « trancher » et « arbitrage ». **Le PRD prime**, comme ce plan le déclare en tête. Régime applicable à L-06, en trois temps : **(1)** établir ce que les **sources primaires** portent aujourd'hui, avec leurs dates ; **(2)** si une source primaire établit un fait daté, la divergence **se résout par le fait** — le volume n'a alors choisi aucun camp, il a lu une source que ni l'un ni l'autre n'avait lue, **et il le dit dans ces termes** ; **(3)** si les sources sont muettes ou contradictoires, la divergence **demeure** et se porte au PRD §7.5. ⚠ **L'arbitrage par chronologie reste interdit dans les trois cas** : le livrable le plus récent est ici le plus réservé, et la prudence d'un volume ne se corrige pas par la date d'un autre.

Quatre lots méritent une consigne propre :

- **L-01** — les drafts IETF vivent en mois. Consigner pour chacun son **état et sa date d'expiration réels** au jour de la consultation, pas seulement son existence. Le Vol. II l'a fait pour le brouillon SCIM-agents — et c'est ainsi qu'il a pu établir que la spécification CSA s'adosse à un texte expiré vingt-trois jours après sa propre publication. **La consigne est de le faire pour chaque draft**, et non seulement pour celui dont on soupçonne déjà quelque chose : c'est la date d'expiration qu'on n'a pas relevée qui périme un chapitre.
- **L-11** — établir le **statut réel de NIST IR 8547** : projet ou final. L'horloge de toute la Partie V en dépend, et le socle hérité le donne comme *Initial Public Draft* avec réserve explicite. Une horloge fondée sur un projet doit dire qu'elle l'est (R-11).
- **L-13** — « maillage d'agents » est le terme le plus chargé de l'ouvrage. **Tri strict annonce / GA documentée / production**, appliqué offre par offre : quatre statuts différents se disent avec quatre mots différents (R-03, PRD §8.4). Une plaquette n'est pas une capacité.
- **L-14** — consigner le **statut** des conventions sémantiques OpenTelemetry pour les agents (expérimental ou stable), leur **version** et sa **date**. « Conventions OTel » sans version est une affirmation vide.

**Critère de sortie J-3** : socle propre constitué ; niveaux atteints ou écarts documentés ; PRD porté en v1.0 avec son cardinal **recompté**, jamais dérivé d'une borne d'identifiants.

### 4.1 Constat de clôture de P2 — ce que l'exécution a trouvé

☑ **Close le 21 juillet 2026.** Les douze lots sont instruits, chacun avec son rapport ; le socle propre passe de 26 à **78 entrées re-mesurées** ; **PRD v1.0**.

**Ce que le dispositif de P2 a changé par rapport à P1, et ce que cela a produit.** Le seuil de vote du PRD §A.4 réserve le vote à trois juges aux lots bloquants : P2 n'en comportait aucun, et seules les **28 affirmations portant à elles seules une thèse de chapitre** y ont été soumises. En contrepartie, un **contrôle de bornage** a été passé sur les **108** — c'est la parade directe à la faute que la relecture P1.4 avait mise au jour, où la prose de synthèse réintroduisait les universaux que le vote venait de retirer. **Il a corrigé 53 énoncés**, soit près d'un sur deux. *Le vote coûte trois agents par affirmation et attrape le faux ; le bornage en coûte un par lot et attrape l'excessif. Les deux sont nécessaires, et ils n'attrapent pas la même chose.*

**Quatre consignes propres avaient été posées au §4 ; les quatre ont produit.** **L-01** : chaque *draft* est daté et son expiration relevée — le jeton de transaction est en révision -09 du 6 juillet 2026, expirant le 7 janvier 2027. **L-11** : le statut réel d'IR 8547 est établi — toujours *Initial Public Draft*, et **une obligation fédérale datée s'y ancre pourtant**, par une clause « ou un document successeur » qui est précisément ce qui l'empêche de devenir une norme. **L-13** : le tri annonce / GA / production a séparé trois offres en trois statuts, et « agent mesh » désigne **deux objets distincts** chez deux fournisseurs. **L-14** : le triplet version + date + statut est établi — et le résultat est qu'**il n'y a pas de version à citer**, le dépôt dédié ne portant ni publication ni étiquette.

⚠ **Ce que P2 n'a pas fait.** Aucune ligne de chapitre n'est rédigée. Les entrées de niveau **[B]** dominent largement le socle — c'est la conséquence assumée du seuil déclaré (§A.4), et non un défaut d'exécution : *un socle qui l'annonce vaut mieux qu'un socle qui laisse le lecteur le découvrir.* ⚠ **Un vote a été écarté** : un juge avait employé un outil interdit par une règle de refus de l'utilisateur ; son verdict n'a pas été compté, l'affirmation concernée est retombée à deux voix et n'a pas atteint [A].

---

## 5. Phase P3 — Rédaction des Parties I à VI (J-4)

### 5.1 Ordonnancement et dépendances

**Chemin critique** : ch. 4 → ch. 5 → ch. 8 → (Partie VII) → (Partie VIII) → ch. 27-28.

- **Le ch. 4 est la porte de tout l'ouvrage.** La grille des cinq questions structure les Parties II, IV, VI et VII et sert de colonne à l'annexe B. Aucun chapitre qui l'applique ne démarre avant elle. ⚠ **Et son §4.4 est bloqué par L-15** : la décision P0.2 sur le corpus d'appui frappe donc dès le quatrième chapitre, pas seulement au ch. 27.
- **Partie I (ch. 1-4)** : ch. 1-2 dès L-01 ; ch. 3 dès L-02 ; ch. 4 en clôture de partie.
- **Partie II (ch. 5-8)** : ch. 5 dès L-03 (P1), ch. 6 dès L-04, ch. 7 dès L-05 — les trois sont parallélisables entre eux. ⚠ **Le ch. 8 compose les ch. 5, 7 et 9**, non les ch. 5-6-7 : sa troisième pièce est la **chaîne de mandat**, qui est le ch. 9. **L'ordre de rédaction n'est donc pas l'ordre de lecture** — le ch. 8 se rédige après le ch. 9, en travers des parties. C'est la seule inversion du plan, et elle est délibérée.
- **Partie III (ch. 9-11)** : ch. 9 dès L-06 — ⚠ **son §9.4 est bloqué par L-15** ; ch. 10 compose sur le ch. 9 ; ch. 11 dès L-07, parallélisable.
- **Partie IV (ch. 12-15)** : ch. 12 dès L-08 et le ch. 4 ; ch. 13 mobilise la vérification à l'admission du ch. 5 ; ch. 14-15 dès L-09 et L-10.
- **Partie V (ch. 16-18)** : la plus indépendante — ch. 16 et 18 démarrent dès L-11. **Le ch. 17 fait exception** : son §17.2 audite la crypto-agilité des mécanismes de la Partie II et attend donc les ch. 5 à 8 — passeport compris, puisque c'est lui qui assemble.
- **Partie VI (ch. 19-21)** : dès L-12, mais **le ch. 19 §19.2 traite le registre du ch. 7 comme pièce de conformité** — après le ch. 7.

**Six chapitres n'ont aucun lot d'instruction, et ce n'est pas un oubli** : ce sont des **chapitres de composition**. Ils ne consomment pas de source nouvelle, ils consomment des chapitres. Leur dépendance est éditoriale, non documentaire.

| Chapitre | Compose | Dépendance réelle |
|---|---|---|
| ch. 4 — la grille | méthode (PRD Annexe C) | Aucune source ; §4.4 seul est bloqué par L-15 |
| ch. 8 — le passeport | ch. 5, 7, **9** | Trois des quatre pièces de l'assemblage : carte signée, inscription au registre, **chaîne de mandat**. ⚠ **La chaîne de mandat est en Partie III** — le ch. 8 traverse donc une frontière de partie (§5.1). ⚠ La **quatrième pièce**, les attestations de conformité, n'a pas de chapitre dédié au découpage : **point à instruire en P0.1** |
| ch. 10 — les deux sauts | ch. 9 | Expose une frontière, ne la comble pas |
| ch. 25 — le cycle de vie | ch. 13, 14, 15, 23 | **Referme trois fils ouverts en Parties IV-V** — c'est sa fonction. ⚠ **§25.1 et §25.5 sont bloqués par L-15** : ce chapitre n'est « sans lot » qu'au niveau du chapitre, pas de la section |
| ch. 27 — l'architecture | Parties I à VIII | §27.4, §27.5 bloqués par L-15 |
| ch. 28 — l'instanciation | ch. 27 | §28.4 bloqué par L-15 |

⚠ **Un chapitre de composition est plus exposé qu'un chapitre de socle, pas moins.** Il n'a pas de source à citer : chacune de ses affirmations est soit tracée vers un chapitre amont, soit une inférence à marquer. Les ch. 8, 26 et le §27.4 portent d'ailleurs le marquage « Lecture de l'auteur » **à l'ouverture**, étant des constructions d'auteur en totalité (PRD CA-07).

### 5.2 Boucle qualité par pièce (obligatoire, chaque lot)

⚠ **Cette boucle développe celle du PRD §A.7 ; elle ne la remplace pas — et elle en diffère sur deux points, déclarés ici plutôt que subis.** (1) Elle **scinde** l'étape de rédaction en deux : rédiger, puis auto-contrôler la traçabilité. Le PRD n'a que six étapes ; en avoir sept ne change aucune obligation, cela sépare deux gestes que le rédacteur confond quand ils sont sur la même ligne. (2) Elle **explicite** le commit et le registre de gel, que le PRD range dans son point 6. En cas de conflit d'interprétation, le PRD prime. Le gabarit §5.4 développe de même PRD §A.8.

1. **Vérifier que le lot est clos** (PRD §7.6). Sinon : ne pas rédiger. Pour un chapitre de composition, vérifier que les chapitres amont sont fusionnés.
2. **Rédiger** depuis le gabarit (date de gel du jour ; socle H-xx/F-xx et garde-fous R-xx en en-tête).
3. **Auto-contrôle de traçabilité** : chaque affirmation factuelle centrale → note H-xx/F-xx ou source primaire nouvelle (CA-01) ; terme anglais entre parenthèses et en italique à la première occurrence (CA-08) ; renvois qualifiés (CA-10).
4. **Balayage des garde-fous** : motifs du PRD §A.6, inspection de chaque occurrence. ⚠ **R-12 n'a pas de motif** — il est contrôlé par CA-12 seul, en relecture dédiée.
5. **Relecture adversariale par un relecteur distinct du rédacteur**, chargée de **réfuter** trois à cinq affirmations contre le socle. Toute affirmation non défendable est corrigée ou déclassée en encadré.
6. **Appliquer les correctifs — et amender le socle d'abord si la faute y siège**, jamais la pièce seule.
7. **Commit + push**, registre de gel renseigné, volumétrie réelle consignée au regard de la cible (§1.5), **l'écart documenté et non corrigé**.

⚠ **Point 6, la leçon la plus chère du Vol. II** : deux de ses défauts de chapitres avaient leur racine au socle. Les corriger dans les chapitres aurait déplacé la faute sans la traiter.

⚠ **Point 5, la leçon la plus constante du Vol. II** : à sa relecture de publication, **tous les défauts lourds ont été trouvés par relecture adversariale, aucun par l'auto-contrôle**. Le point 3 ne remplace pas le point 5 ; il lui évite de perdre son temps.

### 5.3 Règle d'escalade de gouvernance

**Posée avant la première rédaction, et non après la dix-septième.**

Un rédacteur ne corrige jamais le PRD, le TOC, le présent plan ni le glossaire : il **remonte**. Mais une remontée n'a de valeur que si elle est **tranchée avant la pièce qui en dépend**. Les remontées sont donc relevées et arbitrées **entre les lots**, jamais seulement à la fin d'une phase. Une remontée marquée « bloquant pour le ch. N » **interdit de lancer le ch. N** tant qu'elle n'est pas tranchée.

*Motif : au Vol. II, le ch. 5 a signalé qu'un adjectif du socle était réfuté par le socle lui-même et a demandé l'arbitrage **avant** le ch. 13, chapitre pivot qui reposait dessus. La gouvernance n'étant collectée qu'en fin de passe, l'arbitrage n'a pas eu lieu et le ch. 13 a dû trancher seul. Il l'a bien fait — par chance, pas par conception.*

⚠ **Qui tranche — lacune de cette règle, comblée le 21 juillet 2026 sur constat de la relecture P1.4.** La règle interdisait à un **rédacteur** de corriger le cadrage, mais **ne désignait aucun arbitre** : les trois remontées de P1 ont donc été ouvertes et tranchées le même jour par la même instance, sans que la règle l'interdise ni l'autorise. Le régime est désormais explicite :

- **l'instance d'exécution de la phase arbitre** les remontées qui portent sur un renvoi, un siège, un cardinal ou une qualification de niveau — elle les consigne au registre avec un champ **« Tranchée par »**, et la trace vaut contrôle ;
- **remontent à l'auteur, sans exception** : toute modification de la **thèse d'ensemble**, d'un **objectif O-xx**, d'un **garde-fou R-xx**, ou du **découpage**. ⚠ **R-G-03 relevait de cette seconde catégorie et a été tranchée sans remontée consignée** — l'arbitrage est motivé et tracé, mais il a été pris à un niveau qui n'était pas le sien. *Le signaler coûte une phrase ; le taire aurait fait jurisprudence.*

**Corollaire pour toute passe outillée** : la valeur de retour d'un harnais multi-agents peut se perdre (session, interruption, troncature). Les remontées sont **récupérables depuis le `journal.jsonl`** du répertoire de transcription, et ce recours fait partie de la procédure, non de l'incident.

### 5.4 Gabarit de pièce

En-tête à cinq champs, avant le premier séparateur, suivi de la thèse citée depuis le TOC :

```markdown
# Chapitre N — <titre>

| Champ | Valeur |
|---|---|
| Statut | Gabarit / Rédigé (premier jet) / Rédigé et relu adversarialement |
| Date de gel de l'information | <date> |
| Socle mobilisé (PRD §7) | H-xx, F-xx… |
| Garde-fous à surveiller (PRD §8) | R-xx… |
| Volumétrie cible | ~N mots |

> **Thèse ([TOC.md](../../doc/TOC.md))** : <thèse du chapitre, citée>

---
```

⚠ **Chemin relatif corrigé le 21 juillet 2026, et il dépend de la profondeur du fichier.** La gouvernance vivant dans `doc/` (§1.3), le chemin est **`../doc/TOC.md`** depuis `monographie/` (avant-propos, registre de gel) et **`../../doc/TOC.md`** depuis `monographie/01-partie-I/` … `monographie/90-annexes/`. La v0.1 portait `../../TOC.md` — juste pour une gouvernance à la racine du volume, faux depuis le déplacement, et **recopié 34 fois** si personne ne l'attrapait avant P3. Le Vol. II porte 48 renvois cassés pour avoir recopié le même chemin partout puis déplacé la cible. **Vérifier le chemin à la création de chaque gabarit, pas à la fin** — et le vérifier en l'ouvrant, pas en le relisant.

### 5.5 Formulations types

Formes **imposées**. Une pièce qui a besoin d'une formulation nouvelle pour un cas non prévu l'ajoute ici **au même commit**.

⚠ **Ces formes sont datées, et une forme enrichie ne périme pas rétroactivement une pièce gelée** qui en porte la substance. **Ce qui n'est jamais admis, c'est l'attestation qui ment** : une pièce qui déclare avoir repris une forme « verbatim » affirme un fait vérifiable sur le texte **actuel** de cette table. Écrire « rendu dans la substance imposée » quand c'est le cas ; réserver la revendication de verbatim aux reprises réellement littérales (CA-05).

| Cas | Formulation imposée |
|---|---|
| **Le passeport d'agent** (R-01) | « Le passeport d'agent ne figure dans aucune spécification à date : c'est un **objet de synthèse** construit par cet ouvrage en assemblant [pièces]. » **Proscrire** toute formule qui en fait un objet existant, normalisé ou en cours de normalisation. |
| **Valeur d'un mécanisme cryptographique** (R-02) | « [Mécanisme] **démontre** [ce que la spécification établit] ; il ne documente ni [ce qu'elle tait]. » **Proscrire** « garantit », « prouve l'identité », « atteste ». Un mécanisme est qualifié par ce que sa spécification démontre, jamais par ce qu'elle promet. |
| **Terme de marché** (R-03) | À la première occurrence, au siège imposé : « [Terme] est un terme de fournisseur avant d'être un terme de norme ; il n'a pas de définition normative à date. Le présent ouvrage l'emploie au sens de : [définition d'auteur]. » Sièges : avant-propos (*entreprise agentique*), ch. 22 §22.1 (*maillage d'agents*), ch. 24 §24.1 (*AgentOps*). |
| **Homonymie « control plane »** (R-04) | Qualificatif complet obligatoire, sigle « ACP » seul **proscrit dans tout l'ouvrage**. Six emplois distincts, désambiguïsés au ch. 22 §22.1 et repris à l'annexe D. La branche (c) est attribuée à son éditeur à chaque occurrence ; la branche (d) n'est **jamais** agrégée à la (a). |
| **KYA** (R-05) | « Le KYA n'est pas un standard établi ; les initiatives existantes relèvent du positionnement fournisseur (`Monographie.md` §5.5.4). **Aucun forum n'avait tranché à juin 2026** quelle instance porterait le standard. » La formule « terme de marché avant d'être terme de norme » est une **construction d'auteur**, à marquer. |
| **Modalité d'E-23** (R-06) | « le cycle de vie **attendu par** E-23 », « les attentes d'E-23 », « E-23 **attend** que… ». **Proscrire** « exigé par E-23 », « E-23 impose », « l'**exigence** d'inventaire d'E-23 ». Écrire « **documentation de modèle** » et « **inventaire** », jamais « fiche de modèle » (0 occurrence, EN et FR). |
| **Couverture agentique d'un cadre** (R-06) | « [Cadre] ne nomme ni l'agentique, ni les agents, ni l'orchestration — vérification mécanique sur le texte intégral. Sa définition de « modèle », laissée « intentionally broad », englobe les méthodes d'IA ; d'où une **couverture implicite** que les analystes juridiques tiennent pour acquise. » Attribuée aux analystes, **jamais au régulateur**. |
| **Correspondance produit ↔ réglementation** (R-07) | « Le rapprochement entre [composant] et [exigence] est une **inférence d'auteur**. » Pour E-23 et B-13 **seulement**, ajouter : « [éditeur] ne revendique aucune conformité, et aucune source ne documente ce lien » — **fait négatif établi**, non vérifié. ⚠ Ne pas généraliser cet ajout aux autres produits ni aux autres cadres. |
| **Absence d'incident** (R-08) | « Aucun incident public majeur n'est documenté à date. **Ce fait s'interprète avec prudence** : il peut signaler une surface encore peu déployée, une détection immature ou une divulgation non publique — il ne constitue pas une preuve de sûreté. » |
| **Statut pré-normatif** (R-09) | « [Spécification], à l'état de **[brouillon / *Internet-Draft*, expirant le … / Candidate Recommendation]** au [date] — travaux émergents, non une norme ratifiée. » Pour le W3C : « un **Community Group** n'est pas un *Working Group* : il ne produit pas de Recommandation et n'engage aucun calendrier normatif. » |
| **Corpus d'appui** (R-10) | « Selon [auteurs], *[titre]* ([éditeur, année de bouclage éditorial]), … » — **jamais seul** : toute affirmation centrale porte en outre une source primaire concordante, et toute affirmation protocolaire est vérifiée à la spécification. Le fait daté porte **la date du livre**, pas celle de sa lecture. |
| **Jalon post-quantique** (R-11) | « [Organisme] **vise** une dépréciation en [année] et une interdiction en [année] ([document], à l'état de **[statut réel]**). » **Proscrire** toute formule d'obligation légale. **Ne jamais fusionner** les jalons d'origines distinctes. |
| **Mécanique d'attaque** (R-12) | Décrire **quel maillon de la chaîne d'identité ou de mandat cède, et pourquoi**. Citer l'identifiant de vulnérabilité et l'incident. **Ne reproduire ni charge utile, ni séquence, ni preuve de concept.** Si un vecteur ne s'expose pas sans sa recette, il ne s'expose pas — et la pièce dit qu'elle ne l'expose pas. |
| **Autonomie graduée** (R-13) *(forme remplacée le 21 juill. 2026 — remontée R-G-01)* | « l'échelle à **quatre paliers non numérotés** — *assistance → copilote → orchestration sous revue → autonomie bornée* — (`Monographie.md` §5.0.2, siège du patron §5.1.1) ». **Fichier + section + cardinal *et numérotation*, les quatre** — ⚠ le cardinal seul ne discrimine pas : la graduation L0-L3 en compte aussi quatre. ⚠ **La forme antérieure, qui se contentait des libellés, était inopérante** : les trois échelles du Vol. I partagent leurs libellés — « copilote » est palier de celle-ci, **niveau 2** du continuum 0-5 (désignations au tableau 3 de `Synthese Monographie.md` §4.2) et **niveau L0** de la graduation L0-L3 (`Chapitres/Annexe B…` §1.3). **Proscrire** « l'autonomie graduée du Vol. I » sans précision, **et « copilote » employé seul**. |
| **Trois degrés d'absence** (R-14) | **(1) Fait négatif VÉRIFIÉ** — l'absence est établie par le **balayage documenté d'un texte**. **(2) Fait négatif ÉTABLI** — le socle porte une **réserve explicite d'absence de lien dans son corpus**, sans balayage. **(3) Absence de documentation** — le socle est muet : « Le socle ne documente pas [X] : c'est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié. » ⚠ La distinction décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable. |
| **Homonymie de « mandat »** ⚠ *(forme versée le 21 juill. 2026 — remontée R-G-41, arbitrage délégué)* | Le mot désigne **trois objets** dans le volume : le **mandat protocolaire** (chaîne de mandat d'AP2 et jetons de transaction), le **mandat au sens d'un référentiel d'attaque**, et le **mandat civiliste** (droit civil québécois). **Qualificatif complet obligatoire à chaque occurrence** ; « mandat » employé seul est **proscrit**, hors le cas où le qualificatif vient d'être posé dans la même phrase. ⚠ **Le socle n'en documente que deux** : le mandat civiliste est une **lacune déclarée**, et aucune occurrence ne peut s'y adosser comme à un fait. ⚠ **Aucun garde-fou R-15 n'a été créé** — en créer un aurait modifié le cardinal « quatorze garde-fous » au PRD §8.1, au TOC, au README du volume et au CLAUDE.md ; *créer un garde-fou n'est jamais une addition locale*. **Coût déclaré de ce choix : une formulation imposée ne se balaye pas.** Cette discipline repose sur la relecture, comme **R-12** — la catégorie où ce volume s'est déjà trompé une fois. |
| **Métrique auto-déclarée** | « Selon [source primaire, date], [organisation] **déclare** [métrique]. Cette donnée est auto-déclarée et n'a pas fait l'objet d'une vérification indépendante. » **À chaque occurrence, sans exception d'usage illustratif** — *un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait.* |
| **Projection d'analyste** | « [Analyste] **projetait**, en [millésime], [prévision] pour [échéance] — une projection, à traiter comme telle. » Source nominative, millésime et périmètre obligatoires. Statut **PROJETÉ**. |
| **Chiffre de prolifération NHI** | Illustration, **jamais preuve**. Aucune thèse de chapitre ne repose sur un de ces ratios. |
| **Marqueur d'inférence** | « **Lecture de l'auteur** » (en gras, en tête de l'énoncé), suivi de ce que le socle établit **et** de ce qu'il n'établit pas. Libellé unique — ne pas employer de variante. |
| **Encadré de lacune — cas 1 : passe conduite et infructueuse** | « **État de la connaissance vérifiable** — [question]. Recherche menée le [date] : [ce qui a été tenté], [pourquoi elle échoue]. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici. » |
| **Encadré de lacune — cas 2 : lacune non instruite** ⚠ | « **État de la recherche** — [question]. Lacune ouverte le [date] ; **aucune passe de recherche n'a été conduite** — [pourquoi]. Source à retrouver : [source]. La question reste ouverte ; aucune inférence n'est proposée ici. » **N'employer le cas 1 que si une passe a réellement eu lieu et est traçable** (rapport de `verification/`). Appliqué à une lacune non instruite, le gabarit du cas 1 **induit la fabrication d'une passe qui n'a pas eu lieu**. |
| **Encadré de lacune — cas 3 : source repérée, non extraite** | « **État de la connaissance vérifiable** — [question]. La source primaire est identifiée ([réf.]) mais son contenu n'a pas été extrait intégralement — niveau **[C]**. [Ce qui bloque l'extraction]. L'affirmation n'est donc pas portée ici comme fait central. » |
| **Encadré de lacune — cas 4 : passe conduite et fructueuse, lacune non close** ⚠ *(forme versée le 21 juill. 2026 — relecture P3, Partie I, ch. 2)* | « **État de la connaissance vérifiable** — [question]. Recherche menée le [date] sur les sources primaires : elle établit [ce que la passe a établi] ([F-xx]). Elle ne clôt pas la lacune — [ce qui demeure ouvert malgré cela]. La question reste ouverte ; aucune inférence n'est proposée ici. » **Proscrire ici la formule du cas 1** (« En l'absence de source primaire… ») : la passe a produit un résultat au socle, et ce résultat se nomme **avant** ce qu'il laisse ouvert. |
| **Renvoi qualifié** (CA-10) | Vol. I : nommer le **fichier** (`Monographie.md` §x.y, `Synthese Monographie.md` §x.y, `Chapitres/Annexe B…` §x). Vol. II : nommer le **chapitre** pour toute question (ch. 21 Q3, ch. 16 Q2). Garde-fous : nommer le **volume** (R-5 du Vol. II ; R-05 du présent volume). |

⚠ **Cas 1 et cas 4 se confondent dans les deux sens, et la seconde faute n'est pas moins grave que la première.** Le cas 2 porte déjà l'avertissement d'un côté : employer le cas 1 pour une lacune non instruite **fabrique une passe qui n'a pas eu lieu**. Employer le cas 1 pour une lacune **instruite avec succès** commet la faute symétrique — il **nie le travail accompli**, et écrit « en l'absence de source primaire » là où le socle porte des entrées F-xx datées et traçables à un rapport de `verification/`. *Un encadré de lacune dit d'abord ce que la passe a établi, ensuite seulement ce qu'elle laisse ouvert ; l'ordre inverse transforme un résultat en aveu d'échec.* ⚠ **Six des quatorze lacunes du PRD §10 sont dans cet état** — les lacunes **3, 4, 5, 10, 13 et 14** (décompte re-mesuré sur le chapeau de §10, à la clôture de P2) : le cas 4 n'est pas un cas d'espèce du ch. 2, c'est la forme de six encadrés à venir.

**Critère de sortie J-4** : 21 chapitres fusionnés, chacun ayant passé la boucle §5.2 dont la relecture adversariale ; registre de gel complet ; remontées de gouvernance toutes tranchées.

### 5.6 Constat d'étape de P3 — le tronc est rédigé, la phase n'est pas close

◐ **Ouverte le 21 juillet 2026, non close.** Les **21 chapitres** des Parties I à VI portent un corps ; chacun a été relu par un relecteur distinct du rédacteur (CA-14) et **corrigé dans la même passe**. **Le critère de sortie J-4 n'est pas atteint** : de ses trois termes, le premier est constaté sur pièce, le troisième ne l'est pas — il exige que les remontées de gouvernance soient **toutes** tranchées, et **six** attendent l'arbitrage de l'auteur ; le second, la complétude du registre de gel, se constate au commit de clôture et non ici. *Une phase ne se clôt pas parce que ses pièces existent : elle se clôt sur son critère de sortie* (§1.6, règle 3).

**Cinq écarts entre la prescription et le terrain**, consignés parce qu'ils qualifient P4 :

1. **Le socle avait été constitué avant que la rédaction ne dise ce dont elle avait besoin.** Douze affirmations instruites par L-01, L-02 et L-12, retenues par leur lot mais non versées, se sont révélées être exactement celles qui manquaient aux premières pièces ([R-G-05](../verification/remontees-gouvernance.md)) — privés d'entrée citable, deux chapitres avaient cité un identifiant de lot sous un en-tête « Ce que le socle porte ». Le versement a ouvert **PRD §7.10, onze entrées F-79 à F-89**. ⚠ **La leçon vaut pour P4** : les Parties VII à IX consommeront à leur tour des affirmations restées au rapport de leur lot. L'amendement du socle se prévoit **dans** la passe, jamais après elle, et **jamais dans la pièce seule**.
2. **La boucle §5.2 a été exécutée une première fois sans son point 6.** Quatre chapitres sont restés au dépôt, relus `A_CORRIGER`, avec **quatorze réfutations bloquantes** non traitées — état que le présent tableau de suivi consignait sans le corriger. La parade retenue n'a pas été de rappeler la règle : l'étape corrective a été **placée dans le pipeline**, à la suite immédiate de la relecture et sous la même passe. Les dix-sept chapitres suivants portent, dans leur statut même, la relecture **et** l'application de ses correctifs — constat en tête de chaque pièce. *Une étape qui dépend de la vigilance du rédacteur se saute ; une étape qui est dans le pipeline s'exécute.*
3. **L'écart de volumétrie vient des bornes rétablies, non d'un ajout de matière.** Les 21 pièces portent **86 579 mots** re-mesurés pour **63 000** de cible, soit **+37,4 %**. Le ch. 4 en donne la preuve directe : **3 376 mots** au moment où R-G-17 a été ouverte, **3 912** une fois ses correctifs appliqués — la pièce a grossi **après** sa relecture, parce que les correctifs rétablissent des bornes (nom de produit, degré d'absence, statut pré-normatif, niveau [A]/[B]/[C], tri prospectif). **La cible du TOC est donc calibrée sur une prose moins bornée que celle que les garde-fous imposent.** L'écart se documente ; le corriger par amputation supprimerait les bornes qui l'ont créé (§5.2, point 7). L'arbitrage de la cible appartient à l'auteur (R-G-17).
4. **Le défaut dominant est de niveau d'écriture, non de phase.** La borne du socle perdue dans la prose — un degré qui monte, une exclusivité qui apparaît, une date qui tombe — est ce que la relecture de la Partie I nomme « le défaut dominant, et il est le même aux quatre pièces », en relevant qu'il a été attrapé **à chaque phase, sans exception** : au socle en P1, dans les synthèses en P2, dans la prose d'ouvrage en P3. Trois dispositifs différents, trois fois le même défaut : *il ne s'éteint pas avec une phase, et P4 ne commencera pas indemne.*
5. **Le contrôle CA-12 ne couvre pas le fichier où la faute s'est produite la première fois.** La relecture dédiée a lu la Partie IV en entier et retiré une attestation auto-délivrée (ch. 15 §15.3), mais elle **déclare elle-même** ses trous : 26 pièces balayées et non relues, et **12 rapports de lot sur 14 jamais relus** au titre de R-12 — alors que la faute de P1 siégeait précisément dans un rapport de lot, et que PRD §8.5 les couvre depuis le 21 juillet 2026. ⚠ *Un balayage n'est pas une relecture — et R-12 est le seul garde-fou du volume sans motif de balayage.*

⚠ **Ce que P3 n'a pas fait, et qu'aucune de ses sorties ne doit laisser croire.** Les **13 autres pièces** — avant-propos, ch. 22 à 28, annexes A à E — sont **au gabarit** : c'est P4. Le **ch. 26 demeure interdit d'écriture** par PRD §7.0, L-14 n'ayant pas instruit ses métriques d'observabilité. **Six remontées ne sont pas tranchées**, et leur arbitrage pourra rouvrir des pièces déjà gelées : R-G-08 et R-G-15 portent sur des thèses, R-G-09 et R-G-13 sur des titres, R-G-14 sur un périmètre de lot, R-G-17 sur une cible de volumétrie. Enfin, les décomptes publiés se resynchronisent entre **tous** leurs porteurs — PRD, TOC, README du volume, README du dépôt, registre de gel — **au même commit**, et leur concordance est re-mesurée en P5.3, jamais recopiée.

---

## 6. Phase P4 — Parties VII à IX et appareil (J-5)

- **Prérequis** : Parties I à VI fusionnées. Les Parties VII à IX **citent les chapitres**, pas seulement le socle.
- **Parallélisation** : ch. 22-23 (maillage, dès L-13) et ch. 24, 26 (AgentOps, dès L-14) sont parallélisables. **Le ch. 25 est un chapitre de composition** : ses trois fils viennent des Parties IV-V (ch. 13, 14, 15) et il attend en outre le **ch. 23**, le confinement par le maillage étant une quatrième dépendance, hors des trois fils ; ses §25.1 et §25.5 relèvent de L-15. Les ch. 27-28 attendent tout.
- ⚠ **Parade héritée de P3, et elle conditionne les treize pièces restantes** (remontée **R-G-37**) : **huit thèses de chapitre sur vingt et une** excédaient ce que le socle portait — quantificateur universel négatif, superlatif non balayé, verbe proscrit par R-02, énoncé prospectif sans tri. *Un écart isolé est une coquille de cadrage ; huit sur vingt et un est une méthode de rédaction des thèses qui n'a pas été confrontée au socle.* **Toute thèse écrite au TOC pour une pièce de P4 est donc confrontée au socle AVANT d'être inscrite**, et non découverte fausse par le rédacteur. *Corriger huit thèses sans corriger la méthode qui les a produites reviendrait à traiter le symptôme.*
- ⚠ **Parade élargie le 21 juillet 2026, à l'exécution de P4.0 — elle était sous-calibrée, et la confrontation le chiffre.** Sur les **37 écarts** relevés sur les treize pièces ([`verification/theses-P4-confrontation.md`](../verification/theses-P4-confrontation.md)), **24 n'entrent dans aucune des quatre formes** que R-G-37 avait identifiées, et **19 siègent dans les six pièces SANS thèse** — avant-propos et annexes A à E —, que la parade ne couvrait pas littéralement puisqu'elle visait les thèses. Ce que ces pièces portent à la place, ce sont des **intitulés**, des **cardinaux annoncés** et des **colonnes de restitution**, et les trois excèdent le socle exactement comme une thèse. **La confrontation au socle porte donc, avant inscription, sur les quatre objets :** *(1)* la **thèse** d'une pièce ; *(2)* tout **intitulé** de chapitre ou de section — c'était déjà la matière de R-G-38, huit intitulés sur les pièces rédigées ; *(3)* tout **cardinal annoncé** dans une charge de contenu — le cardinal des lacunes et celui du gabarit de l'annexe E ont l'un et l'autre divergé entre leurs sièges, et *un cardinal ne se recopie jamais, il se re-mesure* ; *(4)* toute **colonne, cellule ou champ d'un format de restitution** des pièces d'appareil — une colonne que le socle ne peut pas remplir se déclare **vide au degré 3**, avec sa formule imposée, et sa vacuité est **le résultat**, non un défaut de la matrice. ⚠ **Et une pièce sans thèse n'est pas une pièce sans confrontation** : c'est celle où l'excès ne se voit pas, faute d'énoncé à confronter. *Une parade calibrée sur les fautes de la phase précédente ne couvre pas les pièces de la suivante.*
- **L'avant-propos se rédige en dernier**, bien qu'il ouvre l'ouvrage : il porte la définition d'auteur de l'« entreprise agentique » et l'annonce des lacunes, deux choses qu'on ne connaît exactement qu'à la fin. Il est **rédigeable dès l'ouverture de J-4** — rien ne l'en empêche — mais il est **livré en J-5**.
- **Contrôle spécifique CA-09** (en plus de la boucle §5.2) : le **test d'appartenance** du PRD §5.1 est vérifié **section par section** en Parties VII et VIII. Toute section qui ne répond ni « ce qu'elle vérifie de l'identité ou du mandat » ni « ce qu'elle en produit comme preuve opposable » est **coupée**, et sa coupe est consignée. *C'est la seule parade au risque de dilution, et elle ne vaut que si elle coupe réellement quelque chose.*
- **Contrôle spécifique CA-13** : chaque composant, contrat et correspondance réglementaire de la Partie IX est tracé au socle **ou** marqué inférence d'auteur.

⚠ **Les annexes sont un révélateur de lacunes, pas une formalité de clôture.** Au Vol. II, l'annexe B et l'annexe C ont chacune découvert, en dernière phase, un défaut que vingt-quatre chapitres n'avaient pas vu — parce qu'un format de restitution nouveau (matrice, frise) ne tolère pas ce que la prose absorbe en silence : une chronologie ne peut pas porter un événement sans date. **Prévoir que les annexes B et C du Vol. III ouvriront des lacunes**, et réserver le temps de les traiter plutôt que de les subir.

**Critère de sortie J-5** : 34 pièces rédigées et relues ; grille du ch. 4 appliquée au maillage (§22.4) ; **grille d'indicateurs du ch. 26 marquée construction d'auteur** ; blueprint tracé (CA-13) ; matrice de l'annexe B livrée.

---

## 7. Phase P5 — Revalidation et publication (J-6)

| # | Tâche | Vérification |
|---|---|---|
| P5.1 | **Revalidation temporelle finale** (PRD §8.3) : re-vérifier chaque fait chaud à sa source primaire — révision MCP, texte final du règlement bancaire et arrêté de désignation (lève ou maintient Q5), consolidation IETF du brouillon SCIM-agents, statut du brouillon CSA, **statut de NIST IR 8547**, statut des conventions OTel, entrées en vigueur du 1er mai 2027, jalons de dépréciation et d'interdiction visés pour 2030 et 2035 — **les sept lignes de PRD §8.3, sans exception** | Rapport daté ; pièces touchées amendées avec **nouvelle date de gel** |
| P5.2 | **Relecture CA-01 à CA-14** (PRD §11), avec balayage exhaustif pour CA-02 (motifs §A.6 sur les 34 pièces) et CA-03 (chaque métrique auto-déclarée) ; **relecture dédiée et distincte pour CA-12** (dualité d'usage) | `verification/relecture-CA.md` : 14/14 conformes, ou écarts corrigés. ⚠ **Chaque attestation est portée par une constatation sur pièce, jamais par le souvenir de l'avoir faite** (CA-14) |
| P5.3 | **Cohérence globale** : décomptes annoncés re-mesurés (§1.5) ; renvois H-xx/F-xx/R-xx/CA-xx valides ; aucun lien relatif cassé ; **synchronisation des chiffres publiés** entre PRD, TOC, README du volume et README du dépôt | Balayage `grep` **et** relecture. Le README du dépôt annonce « ≈ 100 000 mots » pour ce volume — à réaligner sur la mesure réelle, **avec** les autres porteurs, jamais l'un sans les autres |
| P5.4 | **Assemblage et rendu** : concaténation des 34 pièces, génération du PDF, publication | PDF **versionné avec sa source** (règle du dépôt). ⚠ Le pipeline du Vol. II est une **copie** de celui du Vol. I : un correctif à l'un ne se propage pas à l'autre. Un troisième pipeline sera une troisième copie — le savoir avant de le créer |

**Critère de sortie J-6** : rapport de revalidation daté de **moins de trente jours** ; grille CA-01 à CA-14 intégralement conforme **et constatée sur pièce** ; décomptes publiés re-mesurés et concordants entre les quatre porteurs ; PDF régénéré et poussé **avec** sa source. C'est la Definition of Done du §9.

---

## 8. Gestion des risques d'exécution

Complète PRD §13 (risques éditoriaux) par les risques propres à l'exécution.

| Risque | Signal | Parade |
|---|---|---|
| **Rédaction en avance sur son lot** | Une pièce cite une source absente du socle | Boucle §5.2 point 1, bloquante. *Un chapitre écrit sur un socle vide n'est pas un chapitre en avance : c'est une inférence longue* |
| **Remontée de gouvernance non tranchée** | Une pièce signale « bloquant pour le ch. N » et le ch. N démarre quand même | Règle d'escalade §5.3 : arbitrage **entre les lots** |
| **Dérive du périmètre** (maillage ou AgentOps sans lien à l'identité) | Une section ne répond à aucune des deux questions du test d'appartenance | PRD §5.1, vérifié par CA-09 en P4. **Couper, et consigner la coupe** |
| **Fait chaud invalidé en cours de rédaction** | Veille P0.6 / P5.1 | **Amender le socle d'abord**, puis les pièces ; jamais l'inverse |
| **Décompte désynchronisé entre porteurs** | Un chiffre diverge entre PRD, TOC, README du volume, README du dépôt | P5.3. Un même chiffre vit à plusieurs endroits : **les mettre à jour ensemble** |
| **Commande de contrôle publiée sans être éprouvée** | Une commande testée sur un échantillon, publiée pour un corpus | §1.5 : toute commande publiée est exécutée sur son **domaine entier** d'abord. *Une commande de contrôle est du contenu — elle se vérifie comme le reste* |
| **Attestation de conformité non constatée** | « conforme », « vérifié », « résolu » écrit depuis un document amont ou de mémoire | CA-14. Ouvrir la source et **constater**. *Un rédacteur ne vérifie pas ce qu'il croit avoir fait* |
| **`git add -A` ramasse le travail d'un agent parallèle** | Un commit contient des fichiers que son message ne décrit pas | `git add <chemins explicites>` quand des agents écrivent en parallèle, ou attendre leur terme. La règle « committer à la fin de chaque tâche » se lit **à la fin de la sienne**, pas au milieu de celle des autres |
| **Interruption d'une passe outillée** | Valeur de retour perdue ou tronquée | Petits lots commités ; remontées récupérables depuis `journal.jsonl` (§5.3) |
| **Renvois cassés par un déplacement de fichiers** | Un chemin relatif ne résout plus | Trancher l'emplacement en **P0.3**. Le Vol. II porte 48 renvois cassés pour l'avoir tranché après coup |
| **Sur-correction d'une passe corrective** | Une passe à périmètre correctif modifie des thèses | Périmètre déclaré avant la passe ; débordements comptés et rapportés |

---

## 9. Définition de « terminé »

Reprend et **opérationnalise** PRD §12. Le volume est terminé quand :

1. les **34 pièces** sont rédigées, relues adversarialement et tracées, chacune portant sa date de gel au registre ;
2. la grille **CA-01 à CA-14** est intégralement conforme, chaque attestation **portée par une constatation sur pièce** et non par un souvenir ;
3. la revalidation P5.1 date de **moins de trente jours** au moment de publier ;
4. les **quatorze lacunes** de PRD §10 apparaissent toutes, en encadré ou en question de recherche — **aucune silencieusement omise**, et chacune au gabarit qui correspond à l'état réel de son instruction ;
5. les **décomptes publiés** — volumétrie, cardinal du socle, nombre de chapitres et de pièces — sont re-mesurés par les commandes de référence et **concordent** entre le PRD, le TOC, le README du volume et le README du dépôt ;
6. le dépôt est poussé sur `main`, et le **PDF est versionné avec sa source**.

⚠ **Le point 4 est celui qui se relâche en dernier et se remarque en premier.** Une lacune omise ne se voit pas à la relecture — elle se voit à l'usage, quand un lecteur cherche ce que l'ouvrage a promis d'exposer et ne le trouve pas. C'est aussi le seul point de cette liste que le sujet du volume rend non négociable : un ouvrage qui prend la traçabilité pour thèse et masque ses trous se réfute lui-même.
