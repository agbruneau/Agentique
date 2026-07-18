# PRDPlan — Planification d'exécution du volume III

| Champ | Valeur |
|---|---|
| Version | **0.1 — premier plan d'exécution du volume III** (18 juillet 2026). Établi contre [`PRD.md`](PRD.md) v0.1 et [`TOC.md`](TOC.md) v0.4. Deux décisions de méthode y sont prises et justifiées plutôt qu'héritées : la **commande de décompte de volumétrie** est fixée en locale UTF-8 dès l'origine (§1.5 — le Vol. II a dû assumer un défaut de 1,3 % qu'il ne pouvait plus corriger sans invalider tous ses chiffres publiés), et la **règle d'escalade de gouvernance** est posée *avant* la première rédaction et non après (§5.3 — le Vol. II l'a apprise en P2, au prix d'un chapitre pivot qui a dû trancher seul). |
| Date | 18 juillet 2026 |
| Statut | **Aucune phase exécutée.** P0 à P5 sont toutes ☐. Le volume ne possède ni socle propre, ni chapitre, ni arborescence de rédaction. |
| Documents de gouvernance | [`PRD.md`](PRD.md) v0.1 — autorité de contenu, socle, garde-fous, critères d'acceptation ; [`TOC.md`](TOC.md) v0.4 — autorité de découpage ; [`CLAUDE.md`](../../CLAUDE.md) racine — conventions du dépôt |
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
| **P0** — Assainissement du cadrage | J-1 | Révision du TOC sur les neuf écarts (PRD §7.4) ; **décision sur le corpus d'appui** ; arborescence ; gabarit de pièce | — |
| **P1** — Lots bloquants | J-2 | Instruction de L-03, L-08, L-15 (PRD §7.6) ; premières entrées F-xx du socle propre | P0 |
| **P2** — Reste du socle | J-3 | Instruction des douze autres lots ; PRD porté en v1.0 | P1 |
| **P3** — Rédaction du tronc | J-4 | Parties I à VI (ch. 1 à 21) | P2 (par lot : un chapitre démarre dès que **son** lot est clos) |
| **P4** — Application et exploitation | J-5 | Parties VII à IX (ch. 22 à 28), avant-propos, annexes A à E | P3 |
| **P5** — Revalidation et publication | J-6 | Revalidation temporelle finale, relecture CA-01 à CA-14, assemblage, PDF | P4 |

⚠ **Le phasage n'est pas un séquencement strict de P2 vers P3.** La règle cardinale du PRD (§7.0) est *par chapitre*, pas par phase : un chapitre est rédigeable dès la clôture du lot dont il dépend, même si d'autres lots restent ouverts. P2 et P3 se recouvrent donc largement, et c'est voulu — attendre la clôture des quinze lots pour écrire la première ligne allongerait le projet sans rien améliorer.

### 1.3 Structure cible du dépôt

```
3 - EntrepriseAgentique/
├── PRD.md, PRDPlan.md, TOC.md              # gouvernance (racine du volume)
├── monographie/
│   ├── 00-avant-propos.md
│   ├── 01-partie-I/ … 09-partie-IX/        # un fichier .md par chapitre
│   ├── 90-annexes/                         # annexes A à E de l'ouvrage
│   └── 99-registre-gel.md                  # registre des dates de gel, une ligne par pièce
├── verification/
│   ├── lot-L-xx-<slug>.md                  # rapport par lot d'instruction (P1, P2)
│   ├── revalidation-YYYY-MM-DD.md          # revalidations temporelles (P0.6, P5.1)
│   └── relecture-CA.md                     # grille CA-01..CA-14 remplie (P5)
└── sources/                                # corpus d'appui, SI déposé (P0.2) — sinon absent
```

⚠ **Les documents de gouvernance restent à la racine du volume, pas dans `doc/`.** Le Vol. II les y a déplacés le 17 juillet 2026 et a cassé **48 renvois, encore ouverts à ce jour**. Rien ne pointe encore vers les fichiers du Vol. III : le déplacement reste gratuit tant qu'il est fait avant la première pièce rédigée. Après P3, il coûtera le même prix qu'au Vol. II. **À trancher en P0, ou jamais.**

**Commits** : messages en anglais, format Conventional Commits — convention du Vol. II, retenue ici parce que ce volume prolonge son appareil (`docs(prd): …`, `docs(mono): draft chapter N — <slug anglais court>`, sujet ≤ 50 caractères quand possible, plafond 72). ⚠ Le Vol. I emploie des messages courts en français : vérifier le dossier de travail avant de rédiger le message.

### 1.4 Tableau de suivi des activités

**Source de vérité de l'avancement.** Statuts : ☐ à faire · ◐ en cours · ☑ fait · ⊘ sans objet. À mettre à jour **au même commit** que l'activité qu'il décrit — *un statut qui ment est pire qu'un statut absent* (leçon du Vol. II, dont ce tableau a annoncé « 0 rédigée » pendant deux phases entières).

| Activité | Livrable / sortie | Statut | Date | Trace |
|---|---|---|---|---|
| **P0.1** Révision du TOC sur les neuf écarts (PRD §7.4) | TOC v0.5 | ☐ | | Dont : numérotation du Vol. I, siège de Boréalis, §7.0/§7.0.1, KYA §5.5.4, formule de non-compositionnalité, homonymie Q1-Q5, risques 9(a) et 9(b) |
| **P0.2** **Décision sur le corpus d'appui** (PRD §7.7) | `sources/` peuplé **ou** filiation retirée | ☐ | | **Bloque L-15, sept sections et l'annexe E.** Décision d'auteur, non délégable |
| **P0.3** Décision sur l'emplacement des documents de gouvernance (§1.3) | Arborescence arrêtée | ☐ | | Racine ou `doc/` — gratuit avant P3, coûteux après |
| **P0.4** Arborescence `monographie/` et `verification/` | Arborescence commitée | ☐ | | 34 gabarits + registre de gel |
| **P0.5** Gabarit de pièce (§5.4) | Gabarit commité | ☐ | | En-tête à cinq champs + thèse citée du TOC |
| **P0.6** Revalidation d'ouverture des faits chauds (PRD §8.3) | `verification/revalidation-<date>.md` | ☐ | | ⚠ **La révision MCP du 28 juillet 2026 tombe dix jours après ce plan** |
| **P0.7** Repointage des renvois `commun/faits-partages.md` | TOC v0.5 | ☐ | | Le fichier n'est pas créé (PRD §7.5) ; renvois hors volume signalés, non corrigés |
| **P0.8** Contrôle de couverture bijective §6.2 ↔ TOC (34 pièces) | Section « Contrôle de couverture » du TOC | ☐ | | Livrable de PRD §12 J-1 |
| **P0.9** Assignation des garde-fous et des lacunes aux pièces porteuses | Table d'assignation au TOC | ☐ | | Livrable de PRD §12 J-1 ; conditionne CA-02 et CA-06 |
| **P0.10** Report des décisions P0.1 à P0.9 au PRD | **PRD v0.2** | ☐ | | Critère de sortie J-1 |
| **P1.1** Lot **L-03** — valeur probante de la carte signée (Q3) | `verification/lot-L-03-agent-card.md` + entrées F-xx | ☐ | | **Bloquant ch. 5.** Niveau visé [A] |
| **P1.2** Lot **L-08** — taxonomie des attaques (Q2) | `verification/lot-L-08-attaques.md` + entrées F-xx | ☐ | | **Bloquant ch. 12.** Niveau visé [A] ; R-12 dès l'instruction |
| **P1.3** Lot **L-15** — corpus d'appui | Extractions citées **ou** échec documenté | ☐ | | Conditionné par P0.2 |
| **P1.4** Relecture adversariale de la clôture P1 | Constats consignés | ☐ | | Deux relecteurs indépendants |
| **P2.1** à **P2.12** Lots L-01, L-02, L-04 à L-07, L-09 à L-14 | Un rapport par lot + entrées F-xx | ☐ | | Parallélisables ; chacun clôt les chapitres de sa colonne « Bloque » |
| **P2.13** PRD porté en v1.0 (socle propre constitué) | PRD v1.0 | ☐ | | Cardinal du socle propre recompté, jamais dérivé d'une borne |
| **P3** Rédaction des Parties I à VI (ch. 1 à 21) | 21 pièces | ☐ | | Détail et dépendances : §5.1 |
| **P4** Parties VII à IX, avant-propos, annexes A à E (ch. 22 à 28 + 6 pièces) | 13 pièces | ☐ | | Détail : §6 |
| **P5.1** Revalidation temporelle finale | `verification/revalidation-<date>.md` | ☐ | | Datée de moins de 30 jours à la publication |
| **P5.2** Relecture CA-01 à CA-14 | `verification/relecture-CA.md` | ☐ | | Balayage §A.6 **+ inspection humaine** |
| **P5.3** Cohérence globale (décomptes, renvois) | Balayage + relecture | ☐ | | Dont synchronisation des chiffres publiés (§7, risque « décompte désynchronisé ») |
| **P5.4** Assemblage, PDF, publication | `Monographie.md` + `Monographie.pdf` | ☐ | | PDF versionné **avec** sa source (règle du dépôt) |

**Décompte de contrôle (18 juillet 2026)** : 34 unités de rédaction — **0 rédigée, 0 relue, 34 en attente**. Socle propre : **0 entrée**. Lots clos : **0 sur 15**.

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

---

## 2. Phase P0 — Assainissement du cadrage (J-1)

**Aucune rédaction, aucune recherche.** P0 met le cadrage en état d'être exécuté.

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

---

## 3. Phase P1 — Les trois lots bloquants (J-2)

Ces trois lots ne se contournent pas par une reformulation prudente : leur échec supprime un chapitre ou le réduit à une lacune.

| # | Lot | Ce qu'il doit établir | Si échec |
|---|---|---|---|
| P1.1 | **L-03** — carte d'agent signée (Q3 du Vol. II ch. 21) | Ancrage de confiance, régime de révocation, gouvernance des clés — **ou l'établissement que la spécification ne les documente pas** | Le ch. 5 devient un chapitre de lacune instruite, et **le ch. 8 perd une de ses quatre pièces** : le passeport se construit alors sur trois, et le dit |
| P1.2 | **L-08** — taxonomie des attaques (Q2 du Vol. II ch. 21) | Identifiants de vulnérabilité, incidents publics datés, littérature académique | La Partie IV se réduit à une reprise du Vol. I. **Le ch. 12 §12.4 devient le cœur du chapitre** — « ce que la recension ne trouve pas » —, sous R-08 |
| P1.3 | **L-15** — corpus d'appui | Extraction citée, chapitre par chapitre | Sept sections et l'annexe E se réécrivent sans lui (P0.2) |

**Un échec instruit est un résultat ; une lacune non instruite n'en est pas un.** Le rapport de lot consigne ce qui a été tenté, avec quelles sources et pourquoi cela échoue — c'est ce qui autorise le gabarit « passe conduite et infructueuse » plutôt que « aucune passe conduite » (§5.5).

⚠ **R-12 s'applique dès l'instruction de L-08, pas seulement à la rédaction.** Un rapport de lot qui rassemblerait des séquences d'exploitation serait dans le dépôt, donc publié. La recension cite les identifiants et décrit le maillon qui cède ; elle ne reproduit rien.

**Critère de sortie J-2** : Q2 et Q3 instruites ou leur échec documenté ; premières entrées F-xx du socle propre, avec leur niveau ; corpus d'appui **déposé**, **ou** sept sections et l'annexe E **réécrites sans lui**. ⚠ La décision de P0.2 ne suffit pas à clore J-2 : c'est la **réécriture effective** qui le clôt, et elle se fait en P3 et P4 pour les pièces concernées. J-2 est clos quand le plan de réécriture est arrêté pièce par pièce.

---

## 4. Phase P2 — Le reste du socle (J-3)

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

**Les douze sont parallélisables : aucun ne dépend d'un autre.** Un seul porte une charge supplémentaire — **L-06 doit trancher la divergence de gouvernance d'AP2** (PRD §7.5), qui conditionne le ch. 9 et croise le ch. 16 §16.3 Q2 du Vol. II. Ce n'est pas une dépendance entre lots, c'est un arbitrage interne à celui-là.

Quatre lots méritent une consigne propre :

- **L-01** — les drafts IETF vivent en mois. Consigner pour chacun son **état et sa date d'expiration réels** au jour de la consultation, pas seulement son existence. Le Vol. II l'a fait pour le brouillon SCIM-agents — et c'est ainsi qu'il a pu établir que la spécification CSA s'adosse à un texte expiré vingt-trois jours après sa propre publication. **La consigne est de le faire pour chaque draft**, et non seulement pour celui dont on soupçonne déjà quelque chose : c'est la date d'expiration qu'on n'a pas relevée qui périme un chapitre.
- **L-11** — établir le **statut réel de NIST IR 8547** : projet ou final. L'horloge de toute la Partie V en dépend, et le socle hérité le donne comme *Initial Public Draft* avec réserve explicite. Une horloge fondée sur un projet doit dire qu'elle l'est (R-11).
- **L-13** — « maillage d'agents » est le terme le plus chargé de l'ouvrage. **Tri strict annonce / GA documentée / production**, appliqué offre par offre : quatre statuts différents se disent avec quatre mots différents (R-03, PRD §8.4). Une plaquette n'est pas une capacité.
- **L-14** — consigner le **statut** des conventions sémantiques OpenTelemetry pour les agents (expérimental ou stable), leur **version** et sa **date**. « Conventions OTel » sans version est une affirmation vide.

**Critère de sortie J-3** : socle propre constitué ; niveaux atteints ou écarts documentés ; PRD porté en v1.0 avec son cardinal **recompté**, jamais dérivé d'une borne d'identifiants.

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

> **Thèse ([TOC.md](../../TOC.md))** : <thèse du chapitre, citée>

---
```

⚠ **Le chemin relatif vers le TOC dépend de la profondeur du fichier** (`../TOC.md` depuis `monographie/`, `../../TOC.md` depuis `monographie/01-partie-I/`). Le Vol. II porte **48 renvois cassés** pour avoir recopié le même chemin partout puis déplacé la cible. Vérifier le chemin à la création de chaque gabarit, pas à la fin.

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
| **Autonomie graduée** (R-13) | « l'échelle **assistance → copilote → orchestration sous revue → autonomie bornée** (`Monographie.md` §5.0.2, siège §5.1.1) ». **Proscrire** « l'autonomie graduée du Vol. I » sans autre précision : trois échelles distinctes y coexistent. |
| **Trois degrés d'absence** (R-14) | **(1) Fait négatif VÉRIFIÉ** — l'absence est établie par le **balayage documenté d'un texte**. **(2) Fait négatif ÉTABLI** — le socle porte une **réserve explicite d'absence de lien dans son corpus**, sans balayage. **(3) Absence de documentation** — le socle est muet : « Le socle ne documente pas [X] : c'est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié. » ⚠ La distinction décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable. |
| **Métrique auto-déclarée** | « Selon [source primaire, date], [organisation] **déclare** [métrique]. Cette donnée est auto-déclarée et n'a pas fait l'objet d'une vérification indépendante. » **À chaque occurrence, sans exception d'usage illustratif** — *un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait.* |
| **Projection d'analyste** | « [Analyste] **projetait**, en [millésime], [prévision] pour [échéance] — une projection, à traiter comme telle. » Source nominative, millésime et périmètre obligatoires. Statut **PROJETÉ**. |
| **Chiffre de prolifération NHI** | Illustration, **jamais preuve**. Aucune thèse de chapitre ne repose sur un de ces ratios. |
| **Marqueur d'inférence** | « **Lecture de l'auteur** » (en gras, en tête de l'énoncé), suivi de ce que le socle établit **et** de ce qu'il n'établit pas. Libellé unique — ne pas employer de variante. |
| **Encadré de lacune — cas 1 : passe conduite et infructueuse** | « **État de la connaissance vérifiable** — [question]. Recherche menée le [date] : [ce qui a été tenté], [pourquoi elle échoue]. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici. » |
| **Encadré de lacune — cas 2 : lacune non instruite** ⚠ | « **État de la recherche** — [question]. Lacune ouverte le [date] ; **aucune passe de recherche n'a été conduite** — [pourquoi]. Source à retrouver : [source]. La question reste ouverte ; aucune inférence n'est proposée ici. » **N'employer le cas 1 que si une passe a réellement eu lieu et est traçable** (rapport de `verification/`). Appliqué à une lacune non instruite, le gabarit du cas 1 **induit la fabrication d'une passe qui n'a pas eu lieu**. |
| **Encadré de lacune — cas 3 : source repérée, non extraite** | « **État de la connaissance vérifiable** — [question]. La source primaire est identifiée ([réf.]) mais son contenu n'a pas été extrait intégralement — niveau **[C]**. [Ce qui bloque l'extraction]. L'affirmation n'est donc pas portée ici comme fait central. » |
| **Renvoi qualifié** (CA-10) | Vol. I : nommer le **fichier** (`Monographie.md` §x.y, `Synthese Monographie.md` §x.y, `Chapitres/Annexe B…` §x). Vol. II : nommer le **chapitre** pour toute question (ch. 21 Q3, ch. 16 Q2). Garde-fous : nommer le **volume** (R-5 du Vol. II ; R-05 du présent volume). |

**Critère de sortie J-4** : 21 chapitres fusionnés, chacun ayant passé la boucle §5.2 dont la relecture adversariale ; registre de gel complet ; remontées de gouvernance toutes tranchées.

---

## 6. Phase P4 — Parties VII à IX et appareil (J-5)

- **Prérequis** : Parties I à VI fusionnées. Les Parties VII à IX **citent les chapitres**, pas seulement le socle.
- **Parallélisation** : ch. 22-23 (maillage, dès L-13) et ch. 24, 26 (AgentOps, dès L-14) sont parallélisables. **Le ch. 25 est un chapitre de composition** : ses trois fils viennent des Parties IV-V (ch. 13, 14, 15) et il attend en outre le **ch. 23**, le confinement par le maillage étant une quatrième dépendance, hors des trois fils ; ses §25.1 et §25.5 relèvent de L-15. Les ch. 27-28 attendent tout.
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
