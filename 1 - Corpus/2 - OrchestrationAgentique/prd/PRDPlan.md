# PRDPlan — Planification d'exécution de la rédaction de la monographie

| Champ | Valeur |
|---|---|
| Version | 1.4 (**v1.4, suites de l'audit global — 17 juill. 2026** : §4.4 portait **deux racines de défaut** que l'audit ([`audit.md`](audit.md)) a fait remonter des chapitres jusqu'ici. **G-1 — « établi » vs « vérifié »** : le cas R-7 se nommait « fait négatif **établi** » et se glosait « n'est **vérifié** que pour E-23 et B-13 », pendant que la ligne de distinction réservait « vérifié » à trois entrées. Le ch. 23 a suivi une ligne, le ch. 24 l'autre — *deux chapitres de la même partie se contredisent en citant chacun ce document*. Tranché par la ligne « **Trois degrés d'absence** » : vérifié (balayage de texte : F-35, F-09, F-46) > établi (réserve du socle : F-44, F-45) > absence de documentation (socle muet). **G-2 — forme enrichie après gel** : la formule « couverture agentique d'E-23 » a été enrichie le 16 juill. **après** le gel des ch. 9-11, qui en attestent une reprise « verbatim ». Tranché par l'avertissement en tête de §4.4 : *une forme enrichie ne périme pas une pièce gelée qui en porte la substance — mais aucune pièce n'a le droit d'attester un verbatim qu'elle n'a pas.* / v1.3 : v1.1 : clôture de P1 — tableau de suivi §1.4, motifs de balayage §4.3, formulations types §4.4. **v1.2, retours de P2** : règle d'escalade de gouvernance §4.2 — les remontées se tranchent **entre les phases**, jamais seulement à la fin ; §4.4 enrichi de trois variantes d'encadré de lacune — le gabarit unique présupposait une recherche menée et **induisait la fabrication** — et du marqueur d'inférence unique « Lecture de l'auteur ». **v1.3, clôture de P3 (17 juill. 2026)** : les sept remontées de gouvernance en souffrance sont **tranchées** — dont celle du ch. 13, qui sous-employait sciemment son socle depuis l'élévation de F-09 ; **méthode de décompte de volumétrie fixée** en §4.2, dette ouverte depuis le ch. 6 et jamais arbitrée ; §1.4 rectifié — son décompte de contrôle mentait depuis P2) |
| Date | 17 juillet 2026 |
| Statut | **Clos — P0 à P4 exécutées** (17 juillet 2026). Jalon J-5 atteint ; monographie publiée et étiquetée `mono-v1.0` |
| Documents de gouvernance | [PRD.md](PRD.md) v1.10 (autorité de contenu et de qualité) ; [CLAUDE.md](CLAUDE.md) (conventions du dépôt) |
| Objet | Opérationnaliser les jalons J-2 à J-5 du PRD (§12) en plan d'exécution détaillé : phases, chapitres, dépendances, contrôles, artefacts |

Ce plan ne redéfinit ni le contenu (PRD §6), ni le socle (PRD §7), ni les garde-fous (PRD §8), ni les critères d'acceptation (PRD §11) — il les **ordonnance**. En cas de conflit, le PRD prime.

---

## 1. Vue d'ensemble de l'exécution

### 1.1 Livrable final

Monographie en **sept parties** (PRD §6), rédigée en français soutenu (PRD §4), chaque chapitre portant sa **date de gel de l'information** et ses références au socle (identifiants F-xx en notes). Volumétrie indicative (ajustable, non normative) : 60 000 à 90 000 mots, soit ~8 000–13 000 mots par partie.

### 1.2 Phasage (aligné sur PRD §12)

| Phase | Jalon PRD | Contenu | Prédécesseur |
|---|---|---|---|
| P0 — Préparation | (pré-J-2) | Revalidation temporelle initiale, élévations [C] prioritaires, structure du dépôt | — |
| P1 — Plan détaillé | J-2 | Table des matières commentée, chapitre par chapitre | P0 |
| P2 — Rédaction du tronc | J-3 | Parties I à V (chapitres 1–17) | P1 |
| P3 — Synthèse et blueprint | J-4 | Parties VI et VII (chapitres 18–24) | P2 (I–IV au complet ; V peut se clore en parallèle) |
| P4 — Publication | J-5 | Revalidation temporelle finale, relecture CA-1..CA-8, publication | P3 |

### 1.3 Structure cible du dépôt

```
AgentMesh/
├── PRD.md, CLAUDE.md, PRDPlan.md          # gouvernance
├── TOC.md                                  # livrable J-2 : titre, abstract, TdM commentée
├── arxiv - *.pdf                           # sources F-36, F-37 (ne pas supprimer)
├── monographie/
│   ├── 00-avant-propos.md                  # avant-propos et note méthodologique
│   ├── 01-partie-I/  … 07-partie-VII/      # un fichier .md par chapitre (gabarits en place)
│   ├── 90-annexes/                         # annexes A–D (méthodologie, matrice, chronologie, glossaire)
│   └── 99-registre-gel.md                  # registre des dates de gel par chapitre
└── verification/
    ├── revalidation-YYYY-MM-DD.md          # rapports de revalidation (§8.3)
    └── relecture-CA.md                     # grille CA-1..CA-8 remplie (J-5)
```

Chaque fusion de chapitre = un commit dédié (`docs(mono): draft chapter N — <slug anglais court>`, plafond 72 caractères), poussé sur `main` (règle permanente du projet).

### 1.4 Tableau de suivi des activités

**Source de vérité de l'avancement.** Statuts : ☐ à faire · ◐ en cours · ☑ fait · ⊘ sans objet. À mettre à jour **au même commit** que l'activité qu'il décrit — un statut qui ment est pire qu'un statut absent.

| Activité | Livrable / sortie | Statut | Date | Trace |
|---|---|---|---|---|
| **P0.1** Revalidation temporelle initiale | `verification/revalidation-2026-07-16.md` | ☑ | 16 juill. 2026 | PRD v1.3 (F-41 résolu, F-24 corrigé, F-01 et F-29 mis à jour) |
| **P0.2** Élévations [C]→[B] prioritaires | Entrées F-xx amendées | ☑ | 16 juill. 2026 | F-47, F-48 créés ; CrewAI et LangGraph Platform élevés ; FTM/ISO 20022 : échec documenté (§10.6) |
| **P0.3** Arborescence `monographie/` et `verification/` | Arborescence commitée | ☑ | 16 juill. 2026 | 24 gabarits + 4 annexes + registre de gel |
| **P0.4** Gabarit de chapitre | Gabarit commité | ☑ | 16 juill. 2026 | En-tête (gel, socle, garde-fous) appliqué aux 24 fichiers |
| **P1.1** Titre, abstract, TdM commentée | [TOC.md](TOC.md) | ☑ | 16 juill. 2026 | v1.1 — réaligné sur PRD v1.3 |
| **P1.2** Contrôle de couverture bijective (PRD §6) | Section « Contrôle de couverture » de TOC.md | ☑ | 16 juill. 2026 | Bijection I→1-4 … VII→22-24 ; lacunes §10 et garde-fous R-1..R-8 tous assignés |
| **P1.3** Liste des garde-fous par chapitre + motifs de balayage | TOC.md (assignation) + §4.3 (motifs) | ☑ | 16 juill. 2026 | Exigence §4.2.3 |
| **P1.4** Formulations types (inférences, attributions, cibles) | §4.4 | ☑ | 16 juill. 2026 | Exigence §7 (parade « inférence présentée comme fait ») |
| **P1.5** Glossaire unique amorcé | `90-annexes/annexe-d-glossaire.md` | ☑ | 16 juill. 2026 | Exigence §7 ; a révélé la collision R-8 (trois branches en P1, une quatrième à la rédaction du ch. 1) |
| **P1.6** Correction du décompte de volumétrie | TOC.md | ☑ | 16 juill. 2026 | Partie IV 8 500 → 8 000 ; total 82 500 → 82 000 |
| **P1.7** Relecture adversariale de la clôture P1 (2 relecteurs indépendants, §4.2.4) | 10 constats confirmés et corrigés | ☑ | 16 juill. 2026 | Bijection §6 et arithmétique validées ; correctifs : CA-2 porté à R-8, R-8 assigné au ch. 22, formulation « correspondance produit » bornée (F-44), motifs §4.3 sortis du tableau (alternances corrompues), 4 surqualifications du glossaire, 3 divergences TOC↔gabarits, refs de version |
| **P2** — Rédaction Parties I à V (J-3) | | | | |
| ch. 1 Généalogie et gouvernance | `01-partie-I/ch-01-…` | ☑ | 16 juill. 2026 | Boucle §4.2 complète. Relecture adversariale : 4 réfutations bloquantes corrigées (« sept mois » → quatre, F-05 ; thèse « dix-huit » → dix-sept ; conclusion restreinte pour exclure AP2, F-04 ; sigle ACP nu). **A ouvert la lacune §10.7** (4e branche R-8) et déplacé l'encadré R-8 du ch. 3 au ch. 1 |
| ch. 2 Anatomie MCP et A2A | `01-partie-I/ch-02-…` | ☑ | 16 juill. 2026 | ⚠ révision MCP du 28 juill. 2026 (P4.1). **Tranché** : F-02 élevé (ligne v1.0.1) ; thèse et titre corrigés au TOC v1.3 — ils portaient un universel non tenu par F-16 |
| ch. 3 AP2, AGNTCY, destin d'ACP | `01-partie-I/ch-03-…` | ☑ | 16 juill. 2026 | R-1, R-8 (rappel de l'encadré du ch. 1) ; lacune §10.7 |
| ch. 4 Risques protocolaires | `01-partie-I/ch-04-…` | ☑ | 16 juill. 2026 | **Tranché** : thèse « dès l'origine » retirée au TOC v1.3 (F-01 ne date pas ces risques) ; minceur du socle portée en **lacune §10.8** |
| ch. 5 Options d'orchestration OO1–OO4 | `02-partie-II/ch-05-…` | ☑ | 16 juill. 2026 | F-37 — cadre cité, chiffres en illustration |
| ch. 6 L'autonomie encadrée (APM) | `02-partie-II/ch-06-…` | ☑ | 16 juill. 2026 | F-36 ; R-1 (mention ACP du manifeste) |
| ch. 7 Frameworks d'orchestration | `02-partie-II/ch-07-…` | ☑ | 16 juill. 2026 | §10.3 réduite à Temporal ; Confluent au passé (F-41) |
| ch. 8 Identité et registres | `02-partie-II/ch-08-…` | ☑ | 16 juill. 2026 | R-2, R-3 |
| ch. 9 E-23 et le risque de modèle | `03-partie-III/ch-09-…` | ☑ | 16 juill. 2026 | §8.2.4 (inférence d'analystes) |
| ch. 10 Vide fédéral et C-36 | `03-partie-III/ch-10-…` | ☑ | 16 juill. 2026 | F-24 recaractérisé (loi vie privée) |
| ch. 11 Québec : AMF et art. 12.1 | `03-partie-III/ch-11-…` | ☑ | 16 juill. 2026 | Réserve F-25 (jamais « en attente ») |
| ch. 12 ACVM 11-348 | `03-partie-III/ch-12-…` | ☑ | 16 juill. 2026 | Socle F-26 |
| ch. 13 Le pont : contraintes → frames | `03-partie-III/ch-13-…` | ☑ | 16 juill. 2026 | **Pivot de l'ouvrage** — cite les ch. 5-6 et 9-12 |
| ch. 14 Cadre bancaire axé sur le consommateur | `04-partie-IV/ch-14-…` | ☑ | 16 juill. 2026 | R-5 (fait négatif vérifié) |
| ch. 15 ISO 20022 : Lynx et RTR | `04-partie-IV/ch-15-…` | ☑ | 16 juill. 2026 | R-4 + réserve F-29 (cible, pas fait accompli) |
| ch. 16 Prospective AP2 et rails canadiens | `04-partie-IV/ch-16-…` | ☑ | 16 juill. 2026 | Lacune §10.5 assumée |
| ch. 17 Études de cas canadiennes | `05-partie-V/ch-17-…` | ☑ | 16 juill. 2026 | §7.5 attribution à CHAQUE occurrence ; F-47, F-48, R-8 |
| **P0.5** Élévation de F-09 (E-23) par extraction primaire | PRD §7.3, F-09 [C]→**[B]** | ☑ | 16 juill. 2026 | Texte intégral d'E-23 lu et extrait (EN + FR, osfi-bsif.gc.ca) + lettre du 11 sept. 2025. Débloque l'écart socle↔Annexe B signalé par le ch. 9 et exigé par CA-8. **Deux formulations du PRD réfutées** : « cycle de vie **exigé** par E-23 » (ligne fondée sur des principes, « should ») et « **fiches de modèles** » (0 occurrence dans E-23, EN et FR). Vérification négative confirmée et mécanique : agentique/agent/orchestration = 0 ; autonom\* = 8. Nouveau fait : les régimes de retraite fédéraux (FRPP) sont **retirés** du périmètre final |
| **Correction de la cascade F-09** | ch. 9, 10, 11, 12, 13, 14, 18, 20, 23, 24 | ☑ | 16 juill. 2026 | Étendue réelle : **10 chapitres**, pas 6 — le ch. 18 a signalé que ma liste initiale sous-estimait la cascade. Quatre corrections : marquage [A/B mixte] ; affirmations périmées (« aucune extraction primaire ») ; « attendu » vs « exigé » ; « fiches de modèles » attribuées à E-23. **Règle de non-sur-correction** : le terme reste exact pour watsonx.governance (F-44). Vérifié : 44 corrections, 0 débordement hors périmètre. Commit `f1e4663` |
| **P3** — Parties VI et VII (J-4) | | | | |
| ch. 18 Matrice protocoles × réglementation | `06-partie-VI/ch-18-…` | ☑ | 16 juill. 2026 | **16 réfutations bloquantes** — le plus contesté de P3. **A détecté l'erreur de marquage de F-09** ([B] présenté comme une élévation alors que [B] est sous [A]) → PRD v1.7. Signale que TOC ne lui assigne aucune liste F-xx ni garde-fou (seul chapitre dont l'en-tête est construit par la rédaction) — à entériner |
| ch. 19 Architecture de référence | `06-partie-VI/ch-19-…` | ☑ | 16 juill. 2026 | 4 bloquants. Architecture **neutre** ; instanciation IBM renvoyée à la Partie VII |
| ch. 20 Instrumentation et feuille de route | `06-partie-VI/ch-20-…` | ☑ | 16 juill. 2026 | 6 bloquants. R-7 : rapprochement métriques↔E-23 marqué inférence d'auteur. Emploie déjà « attend », jamais « exige » |
| ch. 21 Frontière de la connaissance | `06-partie-VI/ch-21-…` | ☑ | 16 juill. 2026 | 4 bloquants. Consolide §10.1 à §10.10 ; §10.5 par renvoi au ch. 16, sans duplication |
| ch. 22 Principes et couches C1–C8 | `07-partie-VII/ch-22-…` | ☑ | 16 juill. 2026 | **1 seul bloquant** — le mieux tenu de P3. §8.4 respecté ; porte déjà « ces trois sources ne sont pas trois observateurs indépendants » |
| ch. 23 Correspondance et flux | `07-partie-VII/ch-23-…` | ☑ | 16 juill. 2026 | 5 bloquants. **CA-8** : chaque lien porte son statut. Dette F-09 en cours de correction (ligne B.3) |
| ch. 24 Lacunes et revalidation | `07-partie-VII/ch-24-…` | ☑ | 16 juill. 2026 | 7 bloquants. Clôture Confluent exposée comme **résolue** ; échec d'élévation FTM/ISO 20022 exposé honnêtement |
| **Arbitrages de clôture de P3** (§4.2, règle d'escalade) | ch. 13, TOC v1.4, PRDPlan, Annexe D | ☑ | 17 juill. 2026 | Sept remontées tranchées. **La plus lourde** : le ch. 13 (pivot) avait **refusé** de dériver les attentes d'E-23 en cadres — la passe correctrice de la cascade F-09 le lui interdisait — et l'avait signalé comme le point « dont le rendement serait le plus élevé » de la Partie III. **Arbitrage : dériver.** Table du §13.1 portée de 6 à 11 entrées ; 9 produisent une contrainte, 1 seule (AMF) n'en produit aucune. Aussi : renvois F-10/F-35 entérinés ; socle transversal du ch. 18 entériné ; méthode de décompte fixée (§4.2) ; « adaptativité après déploiement » versé au glossaire |
| Avant-propos | `00-avant-propos.md` | ☑ | 17 juill. 2026 | Boucle §4.2 complète. Relecture adversariale : **3 bloquants** — « onze jours » pour douze (28 − 16), dans le paragraphe qui démontre la convention de datation ; universel sur les quatre protocoles réfuté par F-04 (**hérité de l'abstract du TOC**, corrigé aussi) ; **deux métriques citées sans attribution dans le paragraphe qui l'interdit** — exemption refusée, TD et Scotiabank nommées. 8 réserves traitées |
| Annexe A — Méthodologie | `90-annexes/annexe-a-…` | ☑ | 17 juill. 2026 | **2 046 mots**. Relecture : le récit de l'épisode F-09 est **exact de bout en bout** — c'est le point le plus attaqué et il tient. Corrigés : parenthèse fausse en note (le PRD énonce désormais son cardinal) ; « tous au niveau [B] » réfuté par §A.6 du même fichier (F-47/F-48 sont [B/C mixte]) ; « Parties III à V » → **II, III et V** (la Partie IV est intégralement [A] — l'annexe désignait comme fragile la seule partie que l'incident a épargnée) ; §A.7 taisait §10.10 (OO1–OO4 = source unique, charpente de trois parties) et l'épisode F-46 |
| Annexe B — Matrice détaillée | `90-annexes/annexe-b-…` | ☑ | 17 juill. 2026 | **1 930 mots**. Cardinal (15 croisements), partitions et **CA-8** (15/15 statuts, zéro « documenté ») vérifiés mécaniquement — **l'annexe n'a rien comblé**, l'axe le plus risqué est celui qu'elle tient le mieux. Corrigés : attestation §8.2.4 **fausse et mesurable** (« intentionally broad » n'apparaît que dans l'attestation qui prétend que la note le porte) ; règle du fait négatif fermée à 2 quand §4.4 l'ouvre à 3 |
| Annexe C — Chronologie | `90-annexes/annexe-c-…` | ☑ | 17 juill. 2026 | **1 884 mots**, 37 événements — **les 37 dates vérifiées une à une contre le socle, aucune fausse**. Corrigés : C-15 marqué « en vigueur » alors que F-11 documente une **sanction royale** et que le ch. 14 le refuse frontalement → « sanctionné » ; C-36 classé « attendu » alors que sa définition exige « certain dans son principe » — **quatrième statut « incertain » créé**. A ouvert la **lacune §10.11** |
| Annexe D — Glossaire | `90-annexes/annexe-d-…` | ☑ | 17 juill. 2026 | **2 901 mots** (2 596 à la publication ; +305 par la passe corrective de l'audit — trace de l'expansion ACP élevée à F-43, trace du R-6 en en-tête, quatre gloses marquées ou bornées ; re-mesuré le 17 juill. 2026). Le diagnostic le plus lourd de P4, parce que ce fichier **fait autorité** : §D.1 affirmait un fait négatif que le socle ne porte que pour **un** couple sur trois — **déjà essaimé au ch. 1** ; §D.7, instrument de CA-2, ignorait **R-6 en entier** ; cinq définitions comblaient des lacunes déclarées (§10.8, §10.10). « adaptativité après déploiement » ajoutée (dette du ch. 12, relancée par le ch. 13) |
| **P4** — Publication (J-5) | | | | |
| P4.1 Revalidation temporelle finale | `verification/revalidation-2026-07-17.md` | ☑ | 17 juill. 2026 | 8 faits chauds revérifiés à leur source primaire ; **aucun amendement matériel requis** — le socle est exact au 17 juill. 2026. 6 faits sur 8 revalidés par lecture directe ; 2 partiellement (lautorite.qc.ca renvoie 403 — **déclaré, non contourné**). **R-5 tient** : aucun arrêté de désignation (Gazette : « *will be* designated »). RC MCP du 28 juill. 2026 **confirmée à l'échéance** |
| P4.2 Relecture CA-1..CA-8 | `verification/relecture-CA.md` | ☑ | 17 juill. 2026 | **8/8 conformes** après correction. Balayage exhaustif R-1..R-8 sur les 29 pièces. Écarts trouvés et corrigés : **CA-2** — l'annexe D §D.1, qui *fait autorité* sur R-8, affirmait un fait négatif que le socle ne porte pas (déjà essaimé au ch. 1) ; R-6 absent de §D.7 ; motif `ROI` non ancré (92 % de bruit). **CA-3** — l'avant-propos citait deux métriques sans les attribuer, dans le paragraphe qui l'interdit. **CA-6** — la lacune §10.11, ouverte le matin même, n'était portée par aucun chapitre. **CA-5** — cinq sur-qualifications du glossaire. **Tous les défauts lourds ont été trouvés par relecture adversariale, aucun par l'auto-contrôle** |
| P4.3 Cohérence globale (décomptes, renvois) | Balayage grep + relecture | ☑ | 17 juill. 2026 | Renvois F-xx/R-x et liens relatifs : **propres** (les seules occurrences de F-12 à F-14 sont les phrases qui disent qu'ils ne sont pas attribués). Volumétrie réelle : ~~88 021 mots~~ → **92 059 mots** sur 29 pièces après la passe corrective de l'audit (90 362 à la clôture de P4 ; cible 82 000, **+12,3 %** — au-dessus de la fourchette indicative 60-90k de §1.1, **écart documenté et non corrigé par amputation**, conformément à §4.2 : « un écart se documente, il ne se corrige pas par amputation ») ; écarts documentés au TOC. ⚠ **Chiffre rectifié le 17 juill. 2026 (audit global, racine de M-14)** : le 88 021 a été mesuré **avant** les correctifs de relecture des pièces de P4 et jamais re-mesuré ; le décompte de contrôle en bas de ce tableau porte 90 362 — *ce tableau se contredisait donc lui-même à dix lignes d'intervalle*, et le `README.md` de la monographie a recopié le mauvais des deux. L'audit avait relevé le symptôme (le README) ; la racine était ici. ⚠ **La commande de référence était elle-même fausse** : sans borne `<!--`, elle surévaluait les 3 pièces sans section « ## Notes » (annexe C : 2 897 annoncés pour **1 656** ; avant-propos : 2 308 pour **1 854**). Testée sur 2 fichiers, publiée comme référence pour 29 — relevé par relecture adversariale, pas par la passe qui l'a fixée |
| P4.4 Assemblage, tag `mono-v1.0` | Dépôt publié | ☑ | 17 juill. 2026 | Index de lecture `monographie/README.md` (38 liens, tous vérifiés). Definition of Done §8 : 5/5 |

**Décompte de contrôle** (revérifié le 17 juillet 2026, à la clôture de P4 ; **re-mesuré le 17 juillet 2026 après la passe corrective de l'audit**) : 24 chapitres + avant-propos + 4 annexes = **29 unités de rédaction — 29 rédigées, 29 relues adversarialement, 0 en attente**. Volumétrie : ~~90 362~~ → **92 059 mots** (commande de référence §4.2, réexécutée sur les 29 pièces ; **+1 697 mots**, apportés par les marquages de strates, les encadrés convertis aux gabarits §4.4 et les rectifications d'attestations).

*Ce décompte a menti deux fois, et les deux fois il l'a dit plutôt que d'être corrigé en silence. Il annonçait « 0 rédigée, 1 amorcée » sous un tableau portant ☑ sur 24 chapitres — périmé depuis P2. Un statut qui ment est pire qu'un statut absent : c'est la règle de ce tableau, et il l'a enfreinte pendant deux phases entières.*

---

## 2. Phase P0 — Préparation (avant toute rédaction)

| # | Tâche | Vérification de sortie |
|---|---|---|
| P0.1 | **Revalidation temporelle initiale** des faits « chauds » (PRD §8.3) : lancement RTR (cible T4 2026), règlement du cadre bancaire (commentaires clos le 26 août 2026 ; désignation de l'organisme de normalisation technique), clôture de l'acquisition Confluent (à confirmer sur newsroom.ibm.com — F-41), trajectoire C-36, versions A2A/MCP | Rapport `verification/revalidation-<date>.md` : chaque fait chaud marqué inchangé / évolué (avec source) ; PRD amendé si évolution |
| P0.2 | **Élévations [C] → [B] prioritaires** (PRD §10) : BMO (extraction intégrale du rapport annuel 2025), Sun Life (communiqué primaire du consortium « Agentic Control Plane »), support A2A première main de LangChain/CrewAI, FTM/ISO 20022 | Entrées F-xx mises à jour dans le PRD avec citations ; échec documenté = la lacune reste en §10 et sera traitée en encadré |
| P0.3 | Création de l'arborescence `monographie/` et `verification/`, registre de gel initialisé | Arborescence commitée |
| P0.4 | **Gabarit de chapitre** : en-tête (date de gel, socle mobilisé F-xx, garde-fous applicables R-x), corps, encadrés « état de la connaissance vérifiable », notes | Gabarit commité ; utilisé par tous les chapitres |

**Règle** : P0.2 est un « meilleur effort » borné (une passe de recherche ciblée par lacune) — l'échec d'élévation ne bloque pas P1 ; l'interdiction de combler par du non-vérifié (PRD §10) s'applique.

**Statut (16 juillet 2026) : P0 complété.** P0.1 et P0.2 exécutés (rapport `verification/revalidation-2026-07-16.md` ; PRD v1.3 — F-41 résolu, F-24 corrigé, F-01 mis à jour, F-47/F-48 ajoutés, R-8 ajouté). P0.3 et P0.4 déjà réalisés lors de la mise en place de l'arborescence `monographie/` (jalon J-2).

---

## 3. Phase P1 — Table des matières commentée (J-2)

Livrable : [TOC.md](TOC.md) à la racine (titre, abstract, TdM commentée). Pour **chaque chapitre** : titre, thèse en 2-3 phrases, contenu obligatoire couvert (renvoi PRD §6), entrées F-xx mobilisées, garde-fous R-x à surveiller, encadrés prévus (lacunes §10), volumétrie cible.

**Critère de sortie (PRD J-2)** : couverture bijective — chaque élément de « contenu obligatoire » de PRD §6 est assigné à exactement un chapitre (aucun orphelin, aucun doublon) ; validation contre CA-1..CA-8 par relecture ; commit + push.

**Statut (16 juillet 2026) : P1 complété** (détail : tableau de suivi §1.4, lignes P1.1 à P1.6). Livrables : [TOC.md](TOC.md) v1.1 (réaligné sur le PRD v1.3), motifs de balayage §4.3, formulations types §4.4, glossaire amorcé (`90-annexes/annexe-d-glossaire.md`). Deux constats de la clôture : (1) le décompte de volumétrie de la Partie IV était faux (8 500 annoncés pour 8 000 réels — corrigé, total 82 000) ; (2) l'amorce du glossaire a révélé une collision terminologique à trois branches sur « (agentic) control plane » — **R-8 étendu** au PRD en conséquence.

### Découpage chapitre par chapitre *(proposition d'origine ; le découpage arrêté fait autorité dans [TOC.md](TOC.md) v1.1)*

**Partie I — Fondements : protocoles d'interopérabilité agentique** *(socle : F-01 à F-06 ; F-16 et F-43 en renvoi)*
1. Généalogie et gouvernance des protocoles ouverts (transferts Linux Foundation ; réserve « soutien ≠ production » §8.2.1)
2. Anatomie technique : MCP (JSON-RPC 2.0, OAuth) et A2A v1.0 (Agent Cards signées, multi-protocole) ; complémentarité officielle (F-16)
3. La transaction agentique : AP2 ; AGNTCY comme couche d'infrastructure ; **garde-fou R-1** (ACP fusionné — chapitre où le risque est maximal)
4. Taxonomie des risques protocolaires (empoisonnement d'outils, injection d'invites — réserve F-01)

**Partie II — Orchestration multi-agents en entreprise** *(socle : F-07, F-08, F-15, F-16, F-32, F-33, F-36, F-37)*
5. Cadre conceptuel : OO1–OO4, cinq propriétés, critères de sélection (F-37 — citer le cadre, pas les chiffres, sauf comme illustration réservée)
6. L'autonomie encadrée : frames normatifs vs opérationnels, quatre capacités APM (F-36 ; attention à la mention ACP du manifeste — R-1)
7. Réalisations : Agent Framework, LangGraph, Confluent/Kafka ; Temporal et CrewAI en encadrés [C]
8. Identité et registres d'agents : Entra Agent ID, spécification CSA/SCIM (`toolAccessList`, `permissionBoundaries`) ; **garde-fous R-2, R-3**

**Partie III — Cadre réglementaire canadien** *(socle : F-09, F-10, F-24 à F-27, F-36, F-37)*
9. E-23 et le risque de modèle (couverture agentique = **inférence d'analystes** — §8.2.4) ; rapport BSIF-ACFC (70 % = projection)
10. Le vide fédéral post-C-27 et la trajectoire C-36 (la stratégie IA fédérale n'est PAS au contenu obligatoire — mention possible en contexte seulement, sans fait central)
11. Québec : ligne directrice IA de l'AMF (finale, 1er mai 2027) ; Loi 25 art. 12.1 — friction révision humaine vs autonomie agentique (axe central ; nuance Fasken)
12. Valeurs mobilières : ACVM 11-348 (autonomie/adaptativité dans le champ des lois existantes)
13. **Pont conceptuel obligatoire** : contraintes réglementaires → frames déterministes ; « responsibility gap » et imputabilité canadienne

**Partie IV — Interopérabilité financière canadienne** *(socle : F-11, F-23, F-28, F-29, F-34, F-35)*
14. Le cadre des services bancaires axés sur le consommateur : C-15, Banque du Canada, mobilité des données, règlement prépublié ; **garde-fou R-5** (standard technique non désigné — fait négatif vérifié)
15. ISO 20022 comme couche sémantique : Lynx (bascule nov. 2025), RTR (cible T4 2026 — **garde-fou R-4** ; « cible », pas fait accompli)
16. Prospective : AP2 et les rails canadiens (question ouverte §10.5 — chapitre explicitement prospectif)

**Partie V — Adoption par les institutions financières canadiennes** *(socle : F-17 à F-23b, F-30, F-31 ; règle transversale §7.5 : attribution de TOUTES les métriques)*
17. Études de cas (TD, Scotiabank, RBC, Manuvie, Desjardins, CIBC — sans surqualifier CAI d'agentique —, Intact) ; gouvernances internes comparées ; BMO/Sun Life en encadrés selon issue de P0.2 ; BNC : absence documentée de sources primaires

**Partie VI — Synthèse et architecture de référence** *(socle : transversal)*
18. Matrice protocoles × exigences réglementaires canadiennes
19. Architecture de référence par couches, structurée OO1–OO4 ; OO3/OO4 imposés sous exigence réglementaire stricte (convergence F-36/F-37/F-46)
20. Métriques d'évaluation comme instrumentation candidate d'E-23 ; feuille de route d'adoption (séquencée sur le 1er mai 2027)
21. Frontière de la connaissance vérifiable (reprise honnête de §10 ; le point §10.5 par renvoi au ch. 16, sans duplication)

**Partie VII — Blueprint : plateforme d'intégration d'entreprise (instanciation IBM)** *(socle : F-38 à F-46, en appui sur F-01 à F-11, F-15, F-16, F-26 à F-29, F-33 à F-37 ; §8.4 neutralité fournisseur)*
22. Principes directeurs et vue en couches C1–C8 (Annexe B.1–B.2) ; positionnement OO de chaque couche
23. Correspondance réglementaire (tableau B.3 — chaque lien marqué documenté / inférence ; **garde-fous R-6, R-7**) ; flux illustratifs (B.4)
24. Lacunes du blueprint (B.5) et conditions de revalidation

---

## 4. Phase P2 — Rédaction des Parties I à V (J-3)

### 4.1 Ordonnancement et dépendances

- **Séquence critique** : ch. 1–4 (Partie I) → ch. 5–8 (Partie II) → ch. 13 (pont) ; les ch. 9–12 (réglementaire) sont parallélisables avec la Partie II ; la Partie IV dépend des ch. 9–10 (cadre fédéral) ; la Partie V est indépendante (peut démarrer dès P1).
- **Lot de rédaction** = 1 chapitre. Pas de chapitre « en avance » sur ses dépendances conceptuelles (le vocabulaire OO/frames défini en Partie II est réutilisé partout ensuite).

### 4.2 Boucle qualité par chapitre (obligatoire, chaque lot)

1. **Rédaction** depuis le gabarit (date de gel du jour ; socle F-xx en en-tête).
2. **Auto-contrôle de traçabilité** : chaque affirmation factuelle centrale → note F-xx ou source primaire nouvelle (CA-1) ; termes anglais entre parenthèses à la première occurrence (CA-5).
3. **Balayage garde-fous** : recherche textuelle des motifs **R-1 à R-8** applicables au chapitre (liste par chapitre : [TOC.md](TOC.md), « Contrôle de couverture » ; motifs : §4.3) ; vérification des attributions §8.2 (CA-2, CA-3).
4. **Relecture adversariale** (relecteur distinct du rédacteur — agent ou humain) : tenter de réfuter 3 à 5 affirmations du chapitre contre le socle ; toute affirmation non défendable est corrigée ou déclassée en encadré.
5. **Commit + push** (`docs(mono): draft chapter N — <slug anglais court>`, plafond 72 caractères), mise à jour du registre de gel.

**Règle d'escalade de gouvernance (ajoutée le 16 juill. 2026, après P2).** Un rédacteur ne corrige jamais le PRD, le TOC, le présent plan ni le glossaire : il **remonte**. Mais une remontée n'a de valeur que si elle est **tranchée avant le chapitre qui en dépend**. Défaut constaté en P2 : le ch. 5 a signalé que l'adjectif « indépendantes » de F-46 était réfuté par le socle et a demandé l'arbitrage **avant** le ch. 13 (chapitre pivot qui repose sur cette convergence) ; la gouvernance n'étant collectée qu'en fin de passe, l'arbitrage n'a pas eu lieu et le ch. 13 a dû traiter le problème lui-même. Il l'a bien fait — mais par chance, pas par conception.

**Conséquence pour toute passe outillée** : les remontées de gouvernance sont relevées et tranchées **entre les phases**, jamais seulement à la fin. Une remontée marquée « bloquant pour le ch. N » interdit de lancer le ch. N tant qu'elle n'est pas tranchée. Le corollaire vaut aussi pour la lecture des résultats : la valeur de retour d'un workflow peut se perdre (session, interruption) — les remontées sont donc **récupérables depuis `journal.jsonl`** du répertoire de transcription, et ce recours fait partie de la procédure, non de l'incident.

**Méthode de décompte de volumétrie (fixée le 17 juill. 2026 — clôture de P3).** Point soulevé par le ch. 6, rendu bloquant par le ch. 13 (premier chapitre à tableau) et resté sans arbitrage jusqu'ici : le plan ne fixait **aucune** commande de décompte, et `wc -w` brut compte les notes, les en-têtes et les commentaires HTML de gouvernance — au ch. 13, il annonçait **11 229 mots pour 4 701 réels**. Deux relecteurs ne reproduisaient un décompte qu'à condition que le chapitre publie sa commande. **Commande de référence, seule autorité** :

```sh
# Corps = du premier séparateur "---" jusqu'à "## Notes" OU au premier
# commentaire HTML, selon ce qui vient en premier.
# Un mot = un jeton portant au moins un caractère alphanumérique — exclut les
# tirets cadratins isolés, que `wc -w` comptait comme des mots.
#
# ⚠ DÉFAUT CONNU, MESURÉ LE 17 JUILLET 2026 (audit global), NON CORRIGÉ ICI.
# En locale C, `[[:alnum:]]` ne reconnaît AUCUN caractère accentué : cette
# commande ne compte donc pas les jetons purement non-ASCII. Un seul est un
# vrai mot, mais il est fréquent — « à », mesuré à 1 158 occurrences dans le
# corps des 29 pièces. La commande sous-compte d'environ 1,3 %. Les autres
# jetons qu'elle écarte (« : », « — », « | », « ; », « « », « » ») ne sont pas
# des mots : leur exclusion est correcte et voulue.
#
# Elle reste NÉANMOINS la commande de référence, et son chiffre fait foi.
# Motif : tous les décomptes publiés du dépôt en dérivent (volumétries par
# pièce, cibles, écarts, décompte de contrôle §1.4). La corriger d'autorité
# rendrait faux, d'un seul coup, tout décompte publié avant ce jour — pour un
# gain de justesse de 1,3 % sur une métrique que §1.1 déclare « indicative et
# non normative ». Le remède serait pire que le mal.
# À trancher explicitement si le projet reprend : soit assumer la définition
# telle quelle (« un mot = un jeton portant au moins un caractère alphanumérique
# ASCII »), soit passer la commande en locale UTF-8 ET re-mesurer les 29 pièces
# dans le même commit. Jamais l'un sans l'autre.
awk '/^---$/{f=1;next} /^## Notes/{exit} /^<!--/{exit} f' FICHIER \
  | tr -s '[:space:]' '\n' | grep -cE '[[:alnum:]]'
```

⚠ **La borne `<!--` n'est pas décorative — sa première rédaction ne la portait pas, et la commande était fausse.** Elle ne s'arrêtait qu'à `## Notes`, que **trois pièces sur vingt-neuf n'ont pas** (avant-propos, annexes C et D) : sur celles-là, elle comptait le bloc de gouvernance en commentaire et surévaluait le corps de 2 à 25 % — l'avant-propos était annoncé à 2 308 mots pour **1 854** réels. Défaut relevé le 17 juill. 2026 par la relecture adversariale de l'avant-propos, et non par la passe qui a fixé la commande : **elle l'avait testée sur deux fichiers, puis publiée comme référence pour vingt-neuf.** Une commande de contrôle est du contenu comme le reste — elle se vérifie sur son domaine entier, pas sur un échantillon commode.

Sont donc **hors décompte** : l'en-tête (tableau de champs, thèse), les notes, le bloc de gouvernance en commentaire. Sont **dans** le décompte : la prose, les encadrés et les tableaux du corps — un chapitre de tableaux (ch. 13, 18, 23) porte de ce fait un décompte structurellement plus élevé à contenu égal. La volumétrie reste **indicative et non normative** (§1.1) : un écart se documente, il ne se corrige pas par amputation.

**Critère de sortie J-3 (PRD)** : 17 chapitres fusionnés, chacun ayant passé la boucle 1–5 ; registre de gel complet.

### 4.3 Motifs de balayage des garde-fous *(fixés en P1 — support de l'étape §4.2.3)*

L'assignation des garde-fous par chapitre fait autorité dans [TOC.md](TOC.md) (section « Contrôle de couverture »). Ce qui suit en est le **volet outillé** : les motifs à rechercher dans le chapitre avant tout commit. Un motif qui ressort n'est pas une faute en soi — c'est un point à inspecter contre l'attendu.

Motifs à passer en `rg -i` sur le fichier du chapitre (syntaxe ripgrep ; donnés en bloc de code parce qu'un tableau Markdown corromprait les alternances `|`) :

```
R-1        \bACP\b
R-8        \bACP\b|control plane|plan de contrôle
R-2        registre centralisé|Entra.*registre
R-3        SPIFFE|SVID
R-4        \bRTR\b|Real-Time Rail|T4 2026
R-5        FDX|Financial Data Exchange|standard technique
R-6        Gartner|Magic Quadrant|iPaaS
R-7        E-23|B-13
§8.2.2/§7.5   [0-9]+ ?%|M\$|G\$|heures|modèles en production
§8.2.4     E-23.*agentique|agentique.*E-23
F-09       exigé par E-23|E-23 impose|exigence.*E-23|fiche de modèle|model card
F-09 bis   exigences? d[eu]\'? ?(inventaire|cotation|documentation|surveillance|cycle de vie)
§8.2.5     CSA|SCIM|IETF
§8.2.6     70 ?%
§8.2.7     Forrester|\bTEI\b|Celent|\bROI\b
F-01       sécuris
F-25       en attente|en projet
```

| Garde-fou | Attendu à chaque occurrence du motif |
|---|---|
| R-1 | Au passé, qualifié « protocolaire », fusion dans A2A dite (ch. 3, ch. 6) |
| **R-8** | Qualificatif complet obligatoire ; sigle « ACP » seul **proscrit dans tout l'ouvrage** ; branche (c) attribuée à IBM ; branche (d) — composante ACP d'AGNTCY — jamais agrégée à (a) (lacune §10.7). Formes imposées : glossaire §D.1 |
| R-2 | Parler d'identités et de *blueprints*, pas de registre centralisé |
| R-3 | « s'appuie sur », jamais « impose » |
| R-4 | La cible T4 2026 **est** officiellement annoncée — ne pas écrire « aucune date annoncée ». *(Le versant complémentaire — ne pas écrire « lancé » / « en production » — relève de la **réserve F-29**, pas de R-4 : les deux se balayent ensemble.)* |
| R-5 | Aucun standard désigné ; FDX = anticipation d'industrie |
| R-6 | Ne pas confondre les quadrants ; position iPaaS non vérifiée |
| R-7 | **Uniquement en contexte produit** : « inférence d'auteur » explicite ; aucune conformité revendiquée. En contexte réglementaire pur (Partie III), le motif ressort massivement et sans objet — filtrer |
| §8.2.2 / §7.5 | Attribution nominative à la source, **à chaque occurrence** |
| §8.2.4 | « couverture implicite via la définition de modèle » |
| **réserve F-09** | **« attendu par E-23 », jamais « exigé »** (ligne directrice fondée sur des principes, « should ») ; **« documentation de modèle » / « inventaire », jamais « fiche de modèle »** (0 occurrence dans E-23). Le motif ressort massivement en Partie III et au ch. 23 — inspecter chaque occurrence |
| **réserve F-09 bis** *(ajoutée le 17 juill. 2026)* | La forme proscrite **sans le sigle sur la même ligne**. §4.4 proscrit nommément « l'**exigence** d'inventaire d'E-23 », mais le motif `exigence.*E-23` ne l'attrape que si « E-23 » suit sur la ligne : le ch. 13 a écrit « cinq **exigences** d'inventaire, de cotation… » et l'occurrence est **passée sous l'outil, pas sous la règle** (relevée par relecture adversariale, 17 juill. 2026). Attendu : « attentes », « ce qu'E-23 attend » |
| §8.2.5 | Statut pré-normatif dit (brouillon, expiré) |
| §8.2.6 | Présenté comme projection du BSIF-ACFC |
| §8.2.7 | Commanditaire nommé |
| réserve F-01 | « cadre d'autorisation », jamais « sécurisé » (motif près de MCP) |
| réserve F-25 | Finale depuis le 30 mars 2026 (motif près de l'AMF) |
| CA-5 | À la première occurrence d'un terme du glossaire : terme anglais entre parenthèses, en italique |

### 4.4 Formulations types *(fixées en P1 — parade au risque « inférence présentée comme fait », §7)*

Formes **imposées**. Un chapitre qui a besoin d'une formulation nouvelle pour un cas non prévu l'ajoute ici au même commit.

> ⚠ **Ces formes sont datées, et une forme enrichie ne périme pas rétroactivement une pièce gelée.** *(Règle posée le 17 juill. 2026, suites de l'audit — racine G-2.)* Une formulation de cette table peut être **enrichie après** le gel de chapitres qui l'appliquaient : le rendu antérieur reste **conforme dès lors qu'il en porte la substance**, et il n'est pas rouvert pour cela seul. **Ce qui n'est jamais admis, c'est l'attestation qui ment** : un chapitre qui déclare avoir reproduit une forme « verbatim », « mot pour mot » ou « caractère pour caractère » affirme un fait vérifiable sur le texte **actuel** de cette table. Écrire « rendu dans la substance imposée par §8.2.4 » quand c'est le cas ; réserver la revendication de verbatim aux reprises réellement littérales. *Défaut constaté : les ch. 9, 10 et 11 attestent une reprise littérale d'une forme enrichie depuis leur gel — la substance est respectée, l'attestation est fausse (audit, M-07, m-17, m-20).*

| Cas | Formulation imposée |
|---|---|
| Couverture agentique d'E-23 *(forme **enrichie le 16 juill. 2026**, postérieurement au gel des ch. 9 à 11 — voir l'avertissement ci-dessus)* | « E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration — vérification mécanique sur le texte intégral, EN et FR (F-09). Sa définition de « modèle », laissée « intentionally broad », englobe les méthodes d'IA et d'apprentissage automatique, et le texte vise expressément la « prise de décision autonome » et la « reparamétrisation autonome » ; d'où une **couverture implicite** que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise. » **Substance minimale exigible d'une reprise** (le noyau, présent dans tous les rendus conformes) : la vérification négative, la définition « intentionally broad », et la couverture implicite **attribuée aux analystes** — jamais au BSIF (§8.2.4). |
| **Modalité d'E-23 : « attendu », jamais « exigé »** ⚠ | E-23 est **fondée sur des principes** et rédigée au conditionnel (« should »), jamais à l'impératif (« must ») — F-09, élévation du 16 juill. 2026. Écrire « le cycle de vie **attendu par** E-23 », « les attentes d'E-23 », « E-23 **attend** que… ». **Proscrire** « exigé par E-23 », « E-23 **impose** », « **l'exigence** d'inventaire d'E-23 ». La nuance décide de ce qu'une institution peut opposer à son régulateur — et le PRD lui-même portait la faute (Annexe B.1 principe 6, corrigé). |
| **Vocabulaire d'E-23 : ne pas lui prêter le nôtre** ⚠ | E-23 **n'emploie pas** « fiche de modèle » / « model card » (0 occurrence, EN et FR). Écrire « **documentation de modèle** » (§D.2, principe 3.3) et « **inventaire** » (§C.1 ; champs de l'Appendice 1). Même classe de faute que R-2 : attribuer à une autorité un terme qu'elle n'emploie pas. |
| Correspondance produit ↔ réglementation — **cas du fait négatif établi** (E-23, B-13 : R-7) | « Le rapprochement entre [composant] et [exigence] est une **inférence d'auteur** : [éditeur] ne revendique aucune conformité à [exigence], et aucune source ne documente ce lien. » ⚠ **Écrire « établi », jamais « vérifié »** — voir la ligne « Trois degrés d'absence » ci-dessous : ce fait négatif est **établi** par une réserve du socle (F-44, F-45), non **vérifié** par un balayage de texte. |
| Correspondance produit ↔ réglementation — **cas général** (toute autre exigence) | « Le rapprochement entre [composant] et [exigence] est une **inférence d'auteur**. » ⚠ **Ne pas y ajouter « [éditeur] ne revendique aucune conformité »** : ce fait négatif n'est **établi** que pour E-23 et B-13. Le socle atteste au contraire des revendications d'IBM pour l'AI Act européen, ISO/IEC 42001 et le NIST AI RMF (F-44), et un lien **documenté** pour le rôle d'IBM sur les rails de paiement (tableau B.3). |
| Métrique auto-déclarée | « Selon [source primaire, date], [institution] **déclare** [métrique]. Cette donnée est auto-déclarée et n'a pas fait l'objet d'une vérification indépendante. » |
| Étude d'analyste commandée | « Selon l'étude [nom], **commandée par [commanditaire]**, … » |
| Cible vs fait accompli (RTR) | « Paiements Canada **vise** un lancement au T4 2026, à l'issue des tests industriels en cours ; la cible a été **successivement reportée** — 2019, puis 2022, puis 2023, puis 2026. » *(Ce sont les cibles successives, non les dates auxquelles les reports ont été décidés — F-29.)* |
| Fait négatif vérifié (standard technique) | « Au [date], **aucun organisme de normalisation technique n'a été désigné** par arrêté ministériel et **aucun standard n'est nommé** dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie. » |
| Statut pré-normatif | « [Spécification], à l'état de **brouillon** de [organisme] au [date] — travaux émergents, non une norme ratifiée. » |
| Projection | « Le BSIF et l'ACFC **projettent** une adoption de ~70 % d'ici 2026 — une projection issue d'une enquête auto-déclarée, non un taux observé. » |
| Préprint académique | « [Auteurs] ([réf.]), **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité — le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration. » |
| Soutien ≠ production | « [N]+ organisations **déclarent leur soutien** à [protocole] ([source, date]) ; le soutien déclaré ne vaut pas déploiement en production. » |
| Encadré de lacune — **cas 1 : passe de recherche conduite et infructueuse** | « **État de la connaissance vérifiable** — [question]. Recherche menée le [date] : [ce qui a été tenté], [pourquoi elle échoue]. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici. » |
| Encadré de lacune — **cas 2 : lacune non instruite** ⚠ | « **État de la recherche** — [question]. Lacune ouverte le [date] ; **aucune passe de recherche n'a été conduite** — [pourquoi : hors périmètre de [réf.]]. Source à retrouver : [source]. La question reste ouverte ; aucune inférence n'est proposée ici. » **N'employer le cas 1 que si une passe a réellement eu lieu et est traçable** (rapport de `verification/`, ou Annexe A). Le gabarit du cas 1 présuppose une recherche : appliqué à une lacune non instruite, **il induit la fabrication d'une passe qui n'a pas eu lieu** — défaut constaté sur plusieurs jets de P2 (16 juill. 2026). |
| Encadré de lacune — **cas 3 : source primaire repérée, non extraite intégralement** | « **État de la connaissance vérifiable** — [question]. La source primaire est identifiée ([réf.]) mais son contenu n'a pas été extrait intégralement — niveau de preuve [C]. [Ce qui bloque l'extraction]. L'affirmation n'est donc pas portée ici comme fait central. » |
| **Absence de documentation ≠ fait négatif vérifié** *(formule de distinction, à employer partout où le socle est muet)* | « Le socle ne documente pas [X] : c'est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié. » — Réserver « **fait négatif vérifié** » aux seuls cas où le socle établit l'absence par balayage documenté (F-35, F-09, F-46). La distinction décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable. |
| **Trois degrés d'absence — vocabulaire imposé** ⚠ *(tranché le 17 juill. 2026, suites de l'audit)* | Une absence n'a pas partout la même force, et le mot doit la porter. **(1) Fait négatif VÉRIFIÉ** — le socle établit l'absence par le **balayage documenté d'un texte** : F-35 (chaînes « FDX », « FAPI », « OAuth » cherchées dans le règlement et le communiqué, 9-0), F-09 (« agentique »/« agent »/« orchestration » = 0 sur le texte intégral EN et FR), F-46 (architecture agentique financière introuvable sur ibm.com/architectures et Redbooks). **Trois entrées, et elles seules.** **(2) Fait négatif ÉTABLI** — le socle porte une **réserve explicite d'absence de lien dans son corpus**, sans balayage d'un texte : F-44 (« aucune source ne relie watsonx.governance à E-23 »), F-45 (« aucun lien documenté IBM↔B-13/E-23 »). C'est le cas E-23/B-13 de R-7 ci-dessus. **(3) Absence de documentation** — le socle est **muet** : employer la formule de distinction de la ligne précédente. *Pourquoi cette ligne existe : §4.4 se contredisait — le cas R-7 se nommait « fait négatif établi » et se glosait « n'est vérifié que pour E-23 et B-13 », pendant que la ligne ci-dessus réservait « vérifié » à trois entrées. Le ch. 23 a suivi une ligne, le ch. 24 l'autre : **deux chapitres de la même partie disent l'inverse l'un de l'autre en citant chacun le même document**. Le défaut siégeait ici, pas dans les chapitres (audit du 17 juill. 2026, racine G-1).* |
| **Marqueur d'inférence — libellé unique imposé** | « **Lecture de l'auteur** » (en gras, en tête de l'énoncé), suivi de ce que le socle établit et de ce qu'il n'établit pas. Forme retenue le 16 juill. 2026 après P2 : les ch. 1-17 l'emploient, et c'est le motif que balaiera CA-1 en P4.2. Ne pas employer « inférence de lecture ». *(« Inférence d'auteur » reste la forme du PRD pour qualifier un **lien** dans un tableau — B.3, §8.2.4 ; « Lecture de l'auteur » est la forme rédactionnelle en prose.)* |

---

## 5. Phase P3 — Parties VI et VII (J-4)

- Prérequis : Parties I–IV fusionnées (la synthèse cite les chapitres, pas seulement le socle).
- Ch. 18 (matrice) et ch. 22–24 (blueprint) sont parallélisables ; ch. 19–20 dépendent de la matrice.
- **Contrôle spécifique CA-8** (en plus de la boucle §4.2) : pour chaque composant/principe/correspondance de la Partie VII — trace vers F-38..F-46 (ou socle général) ET statut « documenté / inférence d'auteur » explicite ; contrôle §8.4 (neutralité : alternatives citées par renvoi, aucun superlatif non attribué, faits négatifs exposés — dépréciation Event Streams/EP, R-6, R-7).
- **Critère de sortie J-4 (PRD)** : matrice protocoles × réglementation et tableau B.3 livrés ; CA-8 vérifié et consigné dans `verification/relecture-CA.md`.

**Statut (17 juillet 2026) : P3 complété.** Les 24 chapitres sont rédigés, chacun ayant passé la boucle §4.2 (détail : §1.4). La clôture a exigé une étape que le plan ne prévoyait pas et qu'il prévoit désormais (règle d'escalade, §4.2) : **trancher les remontées de gouvernance accumulées**. Sept l'ont été le 17 juillet 2026. La plus lourde était celle du ch. 13 : le chapitre **pivot** de l'ouvrage avait refusé de dériver les attentes d'E-23 en cadres — la passe qui traversait alors le chapitre était à périmètre strictement correctif et le lui interdisait — et avait signalé, en assumant explicitement la conséquence, qu'il *sous-employait sciemment son socle jusqu'à arbitrage*. Il avait raison de le signaler plutôt que de le faire ; l'arbitrage rendu a conduit la dérivation. **Enseignement pour P4 et au-delà** : une remontée n'est pas un incident, c'est la sortie normale d'un rédacteur qui rencontre une limite de son mandat — mais elle n'a de valeur que si quelqu'un la tranche, et personne ne le fait spontanément à la fin d'une passe.

---

## 6. Phase P4 — Revalidation et publication (J-5)

| # | Tâche | Vérification |
|---|---|---|
| P4.1 | **Revalidation temporelle finale** (PRD §8.3) : re-vérifier chaque fait chaud à sa source primaire ; attention particulière aux événements attendus entre-temps — texte final du règlement bancaire (post-26 août 2026), arrêté ministériel de désignation de l'organisme de normalisation technique (lève ou maintient R-5), lancement effectif du RTR (lève ou maintient la réserve F-29), révision de spécification MCP du 28 juillet 2026, entrées en vigueur du 1er mai 2027 (discours de « futur proche ») ; *la clôture Confluent est résolue depuis P0 (17 mars 2026) et sort de cette liste* | Rapport de revalidation ; chapitres touchés amendés avec nouvelle date de gel |
| P4.2 | **Relecture CA complète** : grille CA-1..CA-8 remplie point par point (PRD §11), avec échantillonnage exhaustif pour CA-2 (balayage **R-1..R-8** sur tout le texte, motifs §4.3) et CA-3 (chaque métrique auto-déclarée) | `verification/relecture-CA.md` : 8/8 conformes, ou écarts corrigés |
| P4.3 | **Contrôles de cohérence globale** : décomptes annoncés (nombre de parties, chapitres, entrées citées), références croisées F-xx/R-x valides, aucun renvoi cassé | Balayage automatisé (grep) + relecture |
| P4.4 | Assemblage final (un document maître ou recueil ordonné), commit + push, étiquette de version (`git tag mono-v1.0`) | Monographie publiée dans le dépôt |

---

## 7. Gestion des risques d'exécution

Complète PRD §13 (risques éditoriaux) par les risques propres à l'exécution :

| Risque | Signal | Parade |
|---|---|---|
| Dérive du périmètre (nouveaux sujets en cours de route) | Chapitre sans ancrage dans PRD §6 | Toute addition passe par un amendement du PRD (version++) avant rédaction |
| Fait chaud invalidé en cours de rédaction (ex. : RTR reporté, standard technique désigné) | Veille P0.1/P4.1 ; alerte ponctuelle | Amender le socle d'abord (PRD), puis les chapitres ; jamais l'inverse |
| Incohérence terminologique entre chapitres | Relectures croisées | Glossaire unique dans `90-annexes/`, alimenté dès P1 ; terminologie de la Partie II fait référence |
| Perte de traçabilité (affirmations sans F-xx) | Auto-contrôle §4.2.2 | Blocage du commit du chapitre tant que CA-1 non satisfait |
| Chapitre « inférence » présenté comme fait (E-23/B-13, FDX) | Balayage R-4..R-8 | Boucle §4.2.3 + P4.2 ; formulations types fixées en P1 (§4.4) |
| Interruption/limite de session pendant une passe outillée | Précédent documenté (PRD Annexe A, incident passe 3) | Travailler par petits lots commités ; reprise sur cache quand disponible |
| **`git add -A` ramasse le travail en cours d'un agent parallèle** *(incident constaté le 17 juill. 2026)* | Un commit contient des fichiers que son message ne décrit pas | **Constaté, non réparé** — l'historique était poussé, et le réécrire est destructif pour un dommage nul : aucune perte, aucun mélange d'éditions concurrentes (vérifié par diff). Deux commits de P4 (`abc129a`, `4bb093d`) portent donc des correctifs d'annexes que leur message ne mentionne pas ; l'agent l'a signalé plutôt que de tenter une réparation, ce qui est la bonne conduite. **Parade pour une prochaine passe** : `git add <chemins explicites>` quand des agents écrivent en parallèle, ou attendre leur terme avant tout commit. La règle permanente « committer à la fin de chaque tâche » (CLAUDE.md) se lit **à la fin de la tâche**, pas au milieu de celle des autres |

---

## 8. Définition de « terminé » (Definition of Done)

La monographie est terminée quand : (1) les 24 chapitres (ou le découpage amendé en P1) sont fusionnés et tracés ; (2) la grille CA-1..CA-8 est intégralement conforme ; (3) la revalidation P4.1 est datée de moins de 30 jours au moment de la publication ; (4) les lacunes résiduelles de PRD §10 apparaissent toutes soit en encadré, soit en question de recherche (aucune silencieusement omise) ; (5) le dépôt est poussé sur `main` et étiqueté.
