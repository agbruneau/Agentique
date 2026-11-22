# Ancrage atomique Wyvern — Chapitre 02 : L'épreuve des mesures

- **Unité** : `ch02` (`7 - Livre 2027/manuscrit/01 - Partie I/Chapitre 02 - L epreuve des mesures.md`)
- **Dossier fermé** : `7 - Livre 2027/sources/ch02-sources.md` (25 sources intégrales `L+`, `SHA-256`)
- **Registres vérifiés** : `registre/faits-empiriques.json`, `registre/ancres-chronologiques.json`, `registre/glossaire-termes.json`
- **Auditeur** : `auditeur-wyvern` (barrière indépendante `G2`, régime Production)
- **Date d'audit** : 2026-11-22 (gel factuel au 31 décembre 2026)

## Synthèse quantitative de l'audit

- **Affirmations atomiques vérifiables auditées** : 79
- **Constat initial — supportés** : 46
- **Constat initial — imprécis (rectifiés)** : 24
- **Constat initial — non supportés (supprimés ou réancrés)** : 9
- **Verdict final — supportés : 79 (100 %)**
- **Verdict final — imprécis résiduels : 0**
- **Verdict final — non supportés résiduels : 0**

---

## Détail complet paragraphe par paragraphe

### Ouverture (Titre, question directrice et paragraphes 1–3)

#### Paragraphe 1 (Ouverture — Décaissements SEC des quatre grands fournisseurs infonuagiques)

- **A001** : Sur les neuf premiers mois calendaires 2026, Alphabet, Amazon, Meta et Microsoft ont décaissé ensemble 496,7 G\$ US (496 723 M\$ US) en trésorerie pour des acquisitions/additions d'immobilisations corporelles [7, 8, 9, 10, 11, 12].
  - Preuve L+ : `SRC-017.txt` (`131,953` M\$), `SRC-018.txt` (`175,670` M\$), `SRC-019.txt` (`83,055` M\$), `SRC-021.txt` (`115,948` M\$) − `SRC-022.txt` (`49,270` M\$) + `SRC-020.txt` (`39,367` M\$) = `106,045` M\$ ; somme = `496,723` M\$ (`FACT-HYPERSCALER-CAPEX-2026`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A002** : Ce total s'articule avec des prévisions annuelles publiées (~220 G\$ US en trésorerie pour Amazon ; 135 à 145 G\$ US pour Meta, locations-financement incluses) et l'annualisation des décaissements d'Alphabet et Microsoft, formant un ordre de grandeur d'environ 690 à 740 G\$ US sur 2026 selon les périmètres locatifs [7, 8, 9, 10].
  - Preuve L+ : `SRC-018.txt` (« approximately \$220 billion »), `SRC-019.txt` (« \$135-145 billion » incluant principal sur baux financiers), `SRC-017.txt` (T3 = `51,355` M\$), `SRC-020.txt` (T1 FY27 = `39,367` M\$ hors `5,192` M\$ de baux financiers) ; agrégation vérifiée dans `FACT-HYPERSCALER-CAPEX-2026`.
  - Constat initial : imprécis (la formulation initiale ne distinguait pas explicitement les prévisions chiffrées publiées par Amazon et Meta de l'annualisation des rythmes d'Alphabet et Microsoft) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A003** : Au T3 2026, le flux de trésorerie disponible d'Alphabet est passé à -9,1 G\$ US (-9 065 M\$ US) [7].
  - Preuve L+ : `SRC-017.txt` tableau de réconciliation FCF Q3 2026 (`Free cash flow: $(9,065)` million).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A004** : Au T3 2026, le flux de trésorerie disponible de Meta a été négatif de -2,12 G\$ US [9].
  - Preuve L+ : `SRC-019.txt` (« free cash flow was negative \$2.12 billion », soit `$(2,120)` million).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A005** : Sur douze mois glissants clos au 30 septembre 2026, le flux de trésorerie disponible d'Amazon a atteint -42,4 G\$ US [8].
  - Preuve L+ : `SRC-018.txt` (« Free cash flow decreased to an outflow of \$42.4 billion for the trailing twelve months », tableau : `$(42,357)` million).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A006** : Au 30 septembre 2026, Microsoft déclarait 364,6 G\$ US de baux futurs, principalement pour des centres de données, non encore entrés en vigueur [10].
  - Preuve L+ : `SRC-020.txt` Note 12 (« additional leases, primarily for datacenters, that had not yet commenced of \$364.6 billion »).
  - Constat initial : imprécis (l'adverbe « principalement » manquait dans le texte initial) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 2 (Ouverture — Absence d'étude P&L dans le corpus ouvert)

- **A007** : Au gel du 31 décembre 2026, aucune étude empirique indépendante publiée dans le corpus ouvert examiné ne mesure l'effet net du déploiement d'agents autonomes sur le compte de résultat (`P&L`) d'une organisation.
  - Preuve L+ : `ch02-sources.md` (dossier fermé de 25 sources L+) et vérification directe de l'ensemble du corpus `SRC-001`..`SRC-075`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 3 (Ouverture — Quatre mécanismes et grille probatoire)

- **A008** : L'écart entre effort d'infrastructure et preuve comptable reflète quatre mécanismes documentés fin 2026 (périmètres incompatibles, gains `L1`, loi de série probabiliste, biais des palmarès), avec distinction des statuts de preuve (`SEC`, revues à comité de lecture, prépublications, enquêtes, prévisions).
  - Preuve L+ : cadrage méthodologique fondé sur les catégories du dossier fermé `ch02-sources.md`.
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 2.1 — Déconstruire les chiffres de marché

#### Paragraphe 4 et Figure 2.1 (Six périmètres emboîtés)

- **A009** : Les trois énoncés (< 10 G\$ US en 2026, ~40 G\$ US en 2030, ~700 G\$ US/an) renvoient à des strates économiques emboîtées ordonnées à la figure 2.1 (`Fig-03.svg`), du logiciel d'orchestration aux dépenses en capital des quatre grands fournisseurs infonuagiques.
  - Preuve L+ : synthèse structurelle ancrée sur `SRC-011`, `SRC-012`, `SRC-013` et `SRC-017..022`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 5 (Contresens financier et transferts budgétaires)

- **A010** : Assimiler les achats matériels des fournisseurs infonuagiques à la demande logicielle d'agents autonomes ou additionner transferts budgétaires et dépenses nouvelles rend tout montant sans liste d'inclusions inutilisable pour calibrer une enveloppe interne.
  - Preuve L+ : déduction économique directe appuyée par la section `Scope exclusions` de `SRC-012.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 6 (Dispersion des études ouvertes L+)

- **A011** : Grand View Research évalue le marché entreprise des systèmes agentiques à 5,3 G\$ US en 2026 et projette 24,5 G\$ US en 2030 au TCAC de 46,2 % (2025–2030), soit environ 7,8 G\$ US en 2027 (7,75 G\$ US calculés à ce taux) [6].
  - Preuve L+ : `SRC-013.txt` (« Estimated Market size in 2026: USD 5.3 billion », « Projected Market size by 2030: USD 24.5 billion », « CAGR of 46.2% from 2025 to 2030 » ; `5.3 * 1.462 = 7.7486`).
  - Constat initial : imprécis (mention de `5,30 G$ US` non présente à deux décimales dans `SRC-013.txt` et `7,75 G$ US` non identifié comme calculé au taux de 46,2 %) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A012** : Deloitte (*TMT Predictions 2026*) retient une base de 8,5 G\$ US en 2026, un scénario central de 35 G\$ US en 2030 et jusqu'à 45 G\$ US en 2030 si les goulots d'orchestration et de gouvernance sont levés [4].
  - Preuve L+ : `SRC-011.txt` (« US\$8.5 billion by 2026 and US\$35 billion by 2030 ... as high as US\$45 billion by 2030 »).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A013** : Mordor Intelligence chiffre le marché mondial à 9,9 G\$ US (9,89 G\$ US) en 2026, 14,1 G\$ US (14,06 G\$ US) en 2027 et 82,27 G\$ US en 2032 (TCAC de 42,38 % sur 2027–2032), soit environ 40,6 G\$ US interpolés pour 2030 [5].
  - Preuve L+ : `SRC-012.txt` (`USD 9.89 billion in 2026`, `USD 14.06 billion in 2027`, `USD 82.27 billion by 2032 at 42.38% CAGR over 2027-2032` ; `14.06 * 1.4238^3 = 40.58`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A014** : L'enveloppe ouverte vérifiée s'établit de 5,3 à 9,9 G\$ US en 2026, de 7,8 à 14,1 G\$ US en 2027 et de 24,5 à 45,0 G\$ US en 2030 [4, 5, 6].
  - Preuve L+ : `SRC-011.txt`, `SRC-012.txt`, `SRC-013.txt` et `FACT-MARKET-ENVELOPE-2027-2030`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 7 (Exclusions méthodologiques de Mordor et sources en statut F)

- **A015** : Mordor Intelligence exclut de son périmètre les modèles de fondation autonomes, le calcul infonuagique vendu séparément, le matériel et le `RPA` traditionnel [5].
  - Preuve L+ : `SRC-012.txt` (`Scope exclusions: Standalone foundation models, model APIs... separately sold cloud computing... hardware... conventional robotic process automation`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A016** : Mordor indique que des concurrents publient jusqu'à 19,33 G\$ US dès 2026 (près du double de son chiffre 2026 de 9,89 G\$, et +37,5 % sur son chiffre 2027 de 14,06 G\$) ou 121 G\$ US en 2032 (contre 82,27 G\$ en 2032, soit +760,6 % face à sa base 2027), en incluant plateformes d'intégration ou modèles multimodaux, spécialisés et en périphérie [5].
  - Preuve L+ : `SRC-012.txt` tableau `Benchmark comparison` (`Global Consultancy A USD 121 B (2032) ... 760.6% above this report's 2027 value of USD 14.06 B`, `Global Consultancy B USD 19.33 B (2026) ... 37.5% above this report's 2027 value`).
  - Constat initial : imprécis (l'énoncé initial suggérait un écart > 760 % pour les deux chiffres sans préciser la comparaison 2032 vs 2027 de Mordor) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A017** : Les séries Polaris, Fortune Business Insights et IDC sont protégées par accès payants (statut F) et écartées du corpus ouvert [ch02-sources.md].
  - Preuve L+ : `ch02-sources.md` Note AO-01.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 8 (Capital-risque Quid et revenus Epoch AI)

- **A018** : L'investissement corporatif mondial en IA a atteint 581,69 G\$ US en 2025, dont 344,66 G\$ US d'investissements privés [3].
  - Preuve L+ : `SRC-008.txt` p. 178–179 (`In 2025, total investment reached \$581.69 billion... Private investments represented the largest share of activity with \$344.66 billion`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A019** : Sur 2018–2025 selon *Quid*, les capitaux privés fléchés vers la catégorie des agents d'IA (*AI agents*) totalisent 8,02 G\$ US, contre 143,22 G\$ US pour l'infrastructure, les modèles, la recherche et la gouvernance (*AI infrastructure/models/research/governance*) [3].
  - Preuve L+ : `SRC-008.txt` Figure 4.2.17 (`AI agents`: `8.02`, `AI infrastructure/models/research/governance*`: `143.22`).
  - Constat initial : imprécis (le texte initial remplaçait « recherche et gouvernance » par « et plateformes associées ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A020** : Les revenus annualisés directionnels compilés par Epoch AI jusqu'en janvier 2026 s'élèvent à environ 25 G\$ US pour OpenAI, 19 G\$ US pour Anthropic, 428 M\$ US pour xAI et 400 M\$ US pour Mistral AI [3].
  - Preuve L+ : `SRC-008.txt` Figure 4.2.18 (`Jan-2026`, `\$25B, OpenAI`, `\$19B, Anthropic`, `\$428M, xAI`, `\$400M, Mistral AI`, avec mise en garde textuelle « directional rather than precise »).
  - Constat initial : imprécis (ajout de la borne « jusqu'en janvier 2026 » et du qualificatif « directionnels ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Tableau 2.1 et légende (Comparaison CapEx SEC vs marché logiciel)

- **A021** : Ligne Alphabet du tableau 2.1 : 132,0 G\$ US (131 953 M\$ US) sur 9M 2026 ; T3 = 51 355 M\$ US ; flux libre T3 = -9,1 G\$ US (`Form 8-K`) [7].
  - Preuve L+ : `SRC-017.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A022** : Ligne Amazon du tableau 2.1 : 175,7 G\$ US (175 670 M\$ US) bruts sur 9M 2026 ; prévision 2026 ~220 G\$ US ; flux libre TTM = -42,4 G\$ US (`Form 8-K`) [8].
  - Preuve L+ : `SRC-018.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A023** : Ligne Meta du tableau 2.1 : 83,1 G\$ US (83 055 M\$ US) sur 9M 2026 hors 2 769 M\$ US de paiements en principal de locations-financement ; prévision 2026 de 135 à 145 G\$ US locations incluses (`Form 8-K`) [9].
  - Preuve L+ : `SRC-019.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A024** : Ligne Microsoft du tableau 2.1 : 106,0 G\$ US (106 045 M\$ US) reconstitués (`FY26` 115 948 − `S1 FY26` 49 270 + `T1 FY27` 39 367 M\$ US), hors 5 192 M\$ US de baux financiers T1 FY27 (`10-K`/`10-Q`) [10, 11, 12].
  - Preuve L+ : `SRC-021.txt` (`115,948`), `SRC-022.txt` (`49,270`), `SRC-020.txt` (`39,367` et `Finance leases 5,192`).
  - Constat initial : imprécis (« baux T1 » ne précisait pas qu'il s'agissait de baux de location-financement, distincts des 6 523 M\$ US de baux opérationnels du même trimestre) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A025** : Lignes Total 4 hyperscalers et Logiciel agentique du tableau 2.1 : 496 723 M\$ US sur 9M / ~690 à 740 G\$ US annuels combinant prévisions et rythmes ; 5,3 à 9,9 G\$ US (2026), 7,8 à 14,1 G\$ US (2027, `GVR` interpolé à 46,2 %) et 24,5 à 45,0 G\$ US (2030, `Mordor` interpolé à 42,38 %) [4, 5, 6, 7, 8, 9, 10, 11, 12].
  - Preuve L+ : `FACT-HYPERSCALER-CAPEX-2026` et `FACT-MARKET-ENVELOPE-2027-2030`.
  - Constat initial : imprécis (mention de l'interpolation `GVR` 2027 à 46,2 % et de la combinaison prévisions/rythmes ajoutée) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 9 (Nuances : multi-usages du CapEx et baux Microsoft)

- **A026** : Les 496,7 G\$ US servent l'ensemble des charges numériques ; Google Cloud a progressé de +103 % sur un an à 30,7 G\$ US au T3 2026 sur 127,6 G\$ US pour Alphabet, tandis qu'AWS atteignait 184 G\$ US en rythme annualisé [7, 8].
  - Preuve L+ : `SRC-017.txt` (`Google Cloud ... increased 103% to \$30.7 billion`, `Consolidated Alphabet revenues ... \$127.6 billion`) et `SRC-018.txt` (`\$184 billion annualized revenue run rate`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A027** : Microsoft totalisait 443,5 G\$ US d'engagements totaux de location au 30 juin 2026 (incluant 329,1 G\$ US de baux non commencés), et ces baux futurs non commencés atteignaient 364,6 G\$ US au 30 septembre 2026 en sus de 128,3 G\$ US d'échéances au bilan [10, 11].
  - Preuve L+ : `SRC-021.txt` tableau des obligations contractuelles (`443,506` M\$) et Note 13 (`24,706` + `89,686` + `329.1 billion` not yet commenced) ; `SRC-020.txt` Note 12 (`33,012` + `95,246` = `128,258` M\$ soit `128,3 G\$`, plus `364.6 billion` not yet commenced).
  - Constat initial : imprécis (« 443,5 G$ US ... puis 364,6 G$ US » masquait le fait que les 329,1 G$ de baux futurs étaient déjà compris dans les 443,5 G$) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 10 (Prévision Gartner relayée par Deloitte et enquête Deloitte 2025)

- **A028** : Deloitte (*TMT Predictions 2026*) rapporte l'estimation attribuée à Gartner (juin 2025) selon laquelle plus de 40 % des projets agentiques risquent d'être annulés d'ici la fin de 2027 en raison de coûts imprévus, de complexité d'échelle ou de risques inattendus, citée comme prévision relayée car le communiqué Gartner et Reuters sont en statut F [4].
  - Preuve L+ : `SRC-011.txt` (« more than 40% of today's agentic AI projects could be cancelled by 2027, due to unanticipated cost, complexity of scaling, or unexpected risks », note 3 : Gartner press release June 25, 2025) ; `ch02-sources.md` Note AO-01 ; `FACT-GARTNER-ABANDON-2027`.
  - Constat initial : imprécis (l'énoncé initial substituait « valeur métier floue » aux motifs exacts rapportés par Deloitte) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A029** : Dans l'enquête Deloitte 2025 auprès de près de 550 dirigeants américains, 80 % jugent leur automatisation de base mûre contre 28 % en y associant des agents d'IA ; parmi ceux qui poursuivent chaque stratégie, 45 % attendent le retour souhaité sous trois ans pour l'automatisation de base contre 12 % en y intégrant des agents [4].
  - Preuve L+ : `SRC-011.txt` (`Deloitte's 2025 Tech Value Survey of nearly 550 US cross-industry leaders, 80% ... believe their organization has mature capabilities with basic automation efforts, whereas only 28% believe the same with basic automation and AI agent-related efforts. Furthermore, among those pursuing each strategy, 45% ... whereas only 12% ...`).
  - Constat initial : imprécis (28 % était présenté comme le taux de couplage effectif et le dénominateur « parmi ceux qui poursuivent chaque stratégie » manquait pour 45 % et 12 %) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

---

### Section 2.2 — Ce que prouvent les essais randomisés

#### Paragraphe 11 (Cadrage L1 vs autonomie)

- **A030** : Les essais randomisés et quasi-expérimentaux montrent que les assistants bien cadrés (`L1`) accélèrent les tâches familières mais que les gains varient fortement — parfois négativement — selon l'expérience, le type de tâche et le niveau d'analyse [3, 19, 20].
  - Preuve L+ : `SRC-008.txt` § 4.4 (`Productivity Trends`), `SRC-009.txt`, `SRC-010.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 12 (Noy & Zhang 2023 ; Brynjolfsson et al. 2025 QJE)

- **A031** : Noy et Zhang (2023, *Science*) assignent à 453 professionnels diplômés des tâches rédactionnelles de 20 à 30 minutes rémunérées à la qualité : -40 % de temps moyen, +18 % de qualité évaluée, réduction des écarts entre travailleurs, usage déclaré au travail 2× plus probable deux semaines après et 1,6× deux mois après [19].
  - Preuve L+ : `SRC-009.txt` p. 1–2 (`453`, `20-to 30-minute`, `decreased by 40%`, `quality rose by 18%`, `Inequality between workers decreased`, `2x as likely ... two weeks after`, `1.6x as likely two months after`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A032** : Brynjolfsson *et al.* (2025, *QJE*, cités dans `SRC-008`) mesurent en centre de services une hausse de +14 % à +15 % de requêtes résolues par heure, atteignant +30 % à +35 % chez les employés les moins expérimentés [3].
  - Preuve L+ : `SRC-008.txt` p. 219 & Figure 4.4.27 (`+14%–15%`, `Less experienced/skilled agents (30%–35% gains)`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 13 (Cui et al. 2025 ; Ju & Aral 2025 ; Choi & Xie 2025)

- **A033** : Cui *et al.* (2025) agrègent trois essais randomisés chez Microsoft, Accenture et une firme d'électronique du *Fortune 100* auprès de 4 867 développeurs : par variables instrumentales, +26,08 % (`ET` : 10,3 %) de tâches complétées (*pull requests*), +38,38 % (`ET` : 12,55 %) de compilations et +13,55 % (`ET` : 10,0 %, statistiquement non significatif) de validations, avec effets concentrés sur les moins expérimentés [3, 20].
  - Preuve L+ : `SRC-010.txt` Résumé et Table 3 (`4,867 developers`, `anonymous Fortune 100 electronics manufacturing company`, `26.08** (10.3)`, `Commits 13.55 (10.0)` sans astérisque, `Builds 38.38*** (12.55)`).
  - Constat initial : imprécis (l'entreprise était qualifiée d'« industrielle » au lieu d'« électronique » et la non-significativité de +13,55 % était omise) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A034** : Ju et Aral (2025) observent +50 % de production par travailleur en création publicitaire multimodale et Choi et Xie (2025) +55 % d'accompagnement client hebdomadaire en comptabilité [3].
  - Preuve L+ : `SRC-008.txt` Figure 4.4.27 (`Ju & Aral (2025): +50% (Output; productivity per worker)`, `Choi & Xie (2025): +55% (Throughput; weekly client support)`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 14 (Becker et al. / METR 2025 ; Shen & Tamkin 2025)

- **A035** : Becker *et al.* (`METR`, 2025, cités dans `SRC-008`) mesurent un ralentissement de -19 % chez des développeurs *open source* expérimentés sur leurs dépôts familiers malgré un sentiment d'accélération, et l'échec d'une réplication fin 2025 par refus de rester sans IA dans le groupe témoin [3].
  - Preuve L+ : `SRC-008.txt` p. 219–220 & Figure 4.4.27.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A036** : Shen et Tamkin (2025, cités dans `SRC-008`) ne trouvent aucune accélération statistiquement significative lors de l'apprentissage d'une nouvelle bibliothèque et relèvent des « pénalités d'apprentissage » [3].
  - Preuve L+ : `SRC-008.txt` p. 220 & Figure 4.4.27 (`0% Statistically insignificant speed change`, `learning penalties`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 15 (Intelligence en dents de scie — IMO 2025 vs ClockBench)

- **A037** : *Gemini Deep Think* obtient 35 points et une médaille d'or à l'IMO 2025, tandis que sur *ClockBench* le meilleur modèle n'indique l'heure juste sur cadran analogique que dans 50,6 % des cas contre 90,1 % pour les humains [3].
  - Preuve L+ : `SRC-008.txt` p. 71 & p. 98, Figure 2.4.8 (`Gemini Deep Think scored 35 points (gold) at the 2025 IMO`, `ClockBench ... GPT-5.4 High ... reached 50.6%`, `Humans ... 90.1%`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 16 et Tableau 2.2 (Synthèse empirique)

- **A038** : Les quatre premières lignes du tableau 2.2 (Noy & Zhang 2023, Brynjolfsson *et al.* 2025 QJE, Cui *et al.* 2025, Becker *et al.* / METR 2025) synthétisent fidèlement devis, échantillons, résultats et limites [3, 19, 20].
  - Preuve L+ : `SRC-008.txt`, `SRC-009.txt`, `SRC-010.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A039** : La cinquième ligne du tableau 2.2 synthétise Statistique Canada `T2`/`T3` 2026 (19,2 % au T2, 25,2 % prévu au T3) et la note `SAP 2026-22` de la Banque du Canada (314 dirigeants, 70 % d'usage personnel hebdomadaire, 8 % en usage significatif d'exploitation) [21, 22, 23].
  - Preuve L+ : `SRC-014.txt`, `SRC-015.txt`, `SRC-016.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A040** : La sixième ligne du tableau 2.2 synthétise Aldasoro *et al.* (2026) (+4 % de productivité du travail sur 12 000 firmes européennes) et Yotzov *et al.* (2026) (impact réalisé minimal sur 6 000 dirigeants de 4 pays, projection à 3 ans de +1,4 %) [3].
  - Preuve L+ : `SRC-008.txt` Figure 4.4.28 (`12,000 European firms`, `+4% increase in labor productivity`, `6,000 executives (US, UK, DE, AU)`, `minimal realized impact`, `+1.4% projected productivity boost ... over next 3 years`).
  - Constat initial : imprécis (l'attribution explicite de +1,4 % à la projection de Yotzov *et al.* manquait dans la colonne limite) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A041** : La septième ligne du tableau 2.2 synthétise `MAP` (Pan *et al.*, 2025/2026) : 306 répondants, 20 études de cas, 68 % limités à 10 étapes ou moins, 74 % évalués par l'humain dans la boucle, 80 % des cas suivant des flux structurés fixes et 92,5 % servant des utilisateurs humains [16].
  - Preuve L+ : `SRC-027.txt` Résumé, § 4.3 (`92.5% target humans rather than other software systems`), § 5.4 (`80% 16/20 structured workflows`), § 6.2 (`74% rely on human-in-the-loop` evaluation) ; `FACT-MAP-STUDY`.
  - Constat initial : non supporté (le tableau 2.2 écrivait « 92,5 % validés par l'humain » en confondant la cible utilisatrice humaine de 92,5 % avec la validation humaine de 74 %) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A042** : La huitième ligne du tableau 2.2 constate l'absence d'étude empirique indépendante dans le corpus ouvert au 31 décembre 2026 reliant le déploiement autonome sans supervision continue au compte de résultat net (`P&L`).
  - Preuve L+ : `ch02-sources.md` et vérification intégrale des 25 sources `L+`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 17 (Statistique Canada T2/T3 2026 et Banque du Canada SAP 2026-22)

- **A043** : Statistique Canada (T2 2026, tableau `33-10-1167-01`) mesure que 19,2 % des entreprises canadiennes toutes industries confondues ont utilisé l'IA pour produire des biens ou services sur les 12 derniers mois, et 28,2 % des utilisatrices recourent à des agents virtuels ou robots conversationnels [21].
  - Preuve L+ : `SRC-014.txt` vecteurs `v1865629154` (`19.2`, cote A) et `v1865629168` (`28.2`, cote A).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A044** : Statistique Canada (T3 2026, tableau `33-10-1207-01`) indique que 25,2 % des entreprises prévoient recourir à l'IA sur les 12 prochains mois, dont 31,8 % pour des agents virtuels ou robots conversationnels parmi celles prévoyant d'y recourir [22].
  - Preuve L+ : `SRC-015.txt` vecteurs `v1937048767` (`25.2`, cote A) et `v1937048782` (`31.8`, cote A).
  - Constat initial : imprécis (l'énoncé initial n'explicitait pas « parmi celles prévoyant d'y recourir » pour le sous-taux de 31,8 %) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A045** : La note `SAP 2026-22` de la Banque du Canada (2 juin 2026, 314 réponses de décembre 2025) montre que si 70 % des décideurs utilisent l'IA chaque semaine, seules 8 % des entreprises en déclarent un usage significatif en exploitation (21 % modéré, 29 % peu fréquent, 11 % en prévision sur un an) ; à trois ans, parmi les firmes utilisatrices ou prévoyant d'adopter l'IA, 18 % anticipent une baisse d'embauche contre 9 % une hausse, et environ 30 % (20 % mineur, 10 % majeur) attendent un effet positif sur leurs dépenses en capital [23].
  - Preuve L+ : `SRC-016.txt` p. 1–7 et Annexe A (filtre `IF Question 2 not "Not currently in use..."` avant Q4 et Q5 ; `20%` minor + `10%` major positive impact on CapEx).
  - Constat initial : imprécis (absence du filtre de sous-échantillon aux firmes utilisatrices/planifiant l'IA et présentation de « 30 % » sans préciser « environ 30 % = 20 % mineur + 10 % majeur ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 18 (Macroéconomie, McKinsey 2025 et MAP)

- **A046** : Le *Penn Wharton Budget Model* (2025) évalue à +0,01 point de pourcentage la contribution actuelle de l'IA à la `PTF`, et Brynjolfsson (2026) mobilise l'hypothèse de la « courbe en J » [3].
  - Preuve L+ : `SRC-008.txt` p. 221, Figure 4.4.28 (`+0.01 percentage points contribution to TFP`, `"J-curve" hypothesis`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A047** : Brynjolfsson *et al.* (2026) estiment un surplus du consommateur américain de 172 G\$ US début 2026, tandis que Brynjolfsson *et al.* (2025) observent un recul proche de 20 % de l'emploi des développeurs âgés de 22 à 25 ans du pic de 2022 à septembre 2025 [3].
  - Preuve L+ : `SRC-008.txt` p. 173 & 192 (`Brynjolfsson et al., 2026`, `\$172 billion annually by early 2026`) et p. 222 (`Brynjolfsson et al., 2025`, `By September 2025, employment for software developers ages 22–25 had fallen close to 20% from its 2022 peak` ; `FACT-JUNIOR-DEV-CONTRACTION`).
  - Constat initial : non supporté (le manuscrit attribuait les deux constats à « Brynjolfsson et al. (2026) » et citait « juillet 2025 », date introuvable dans le corpus L+) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A048** : Dans l'enquête McKinsey 2025 reprise dans `SRC-008`, 88 % des organisations utilisent une forme d'IA, mais l'usage d'agents à l'échelle reste inférieur à 10 % dans presque toutes les fonctions ; environ deux tiers ou plus n'en exploitent aucun même en informatique (69 %) ou gestion des connaissances (68 %), seul le secteur technologique atteignant 24 % en génie logiciel, 22 % en informatique et 21 % en opérations de service [3].
  - Preuve L+ : `SRC-008.txt` p. 174 & 197–199, Figures 4.3.7 et 4.3.8 (`88%`, `single digits`, `about two-thirds or more`, `24%`, `22%`, `21%`).
  - Constat initial : imprécis (« plus des deux tiers » nuancé en « environ deux tiers ou plus » conformément au libellé exact de `SRC-008.txt`) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A049** : L'enquête `MAP` (306 praticiens, dont 86 systèmes déployés) mesure que 80 % visent la productivité, 72 % la réduction d'heures humaines, 92,5 % servent des utilisateurs humains, 74 % s'appuient sur l'évaluation humaine dans la boucle et 68 % bornent l'exécution à 10 étapes ou moins [16].
  - Preuve L+ : `SRC-027.txt` Figure 1 (`80.3%`, `72.7%`, arrondis à `80%` et `72%` dans RQ1), § 4.3 (`92.5%` utilisateurs humains), § 6.2 (`74%` évaluation humaine), § 5.4 (`68% <= 10 steps`).
  - Constat initial : non supporté (le manuscrit écrivait « 92,5 % conservent un vérificateur humain final ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 19 (Bilan probatoire et critères de réfutabilité)

- **A050** : Le bilan au 31 décembre 2026 (gains `L1` documentés, absence de preuve ouverte de rentabilité nette autonome) s'accompagne de trois critères explicites de réfutabilité de la thèse d'architecture (fiabilité brute sur chaînes longues, substituabilité sans noyau déterministe, conformité par invites seules).
  - Preuve L+ : synthèse méthodologique cohérente avec `ch02-sources.md` et `glossaire-termes.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 2.3 — L'arithmétique impitoyable de l'enchaînement

#### Paragraphe 20 (Constat MAP et introduction de la loi de Lusser)

- **A051** : 68 % des équipes `MAP` bornent les agents à dix étapes ou moins avant intervention humaine et 80 % (16/20) des études de cas reposent sur des flux structurés prédéfinis [16], ce qu'éclaire la loi de série dite de Lusser.
  - Preuve L+ : `SRC-027.txt` (`FACT-MAP-STUDY`) et `glossaire-termes.json` (`loi de Lusser appliquée aux chaînes d'agents`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 21 et Figure 2.2 (Formules NIST § 8.1.8.1 et calcul à 94 %)

- **A052** : Selon la section 8.1.8.1 du manuel *NIST/SEMATECH*, un système en série à \(k\) maillons indépendants obéit à \(R_c(t)=\prod_{i=1}^k R_i(t)\) et \(h_c(t)=\sum_{i=1}^k h_i(t)\) ; à 94 % par étape sur dix maillons, la réussite sans erreur vaut \(0{,}94^{10}\approx 0{,}5386\) (53,9 %, soit 46,1 % d'échec), illustrée à la figure 2.2 (`Fig-04.svg`) [14].
  - Preuve L+ : `SRC-024.txt` (§ 8.1.8.1 *Competing risk model*) et `FACT-LUSSER-10-STEPS`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 22 (Jalons 4, 7 et 10 étapes)

- **A053** : À 94 % par maillon, la réussite sans erreur chute à 78,1 % à la quatrième étape (\(0{,}94^4\)), à 64,8 % à la septième étape (\(0{,}94^7\)) et à 53,9 % à la dixième étape (\(0{,}94^{10}\)) [14].
  - Preuve L+ : dérivation arithmétique directe des équations de `SRC-024.txt` (`0,94^4 = 0,7807`, `0,94^7 = 0,6485`, `0,94^10 = 0,5386`).
  - Constat initial : imprécis (« sur 5 à 7 étapes, la probabilité tombe à 64,8 % » omettait de préciser « à la septième étape ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 23 (METR 2025, MAST et amplification Kim et al.)

- **A054** : En mars 2025, `METR` mesure près de 100 % de succès sur les tâches logicielles ou de raisonnement de moins de 4 minutes humaines, contre moins de 10 % au-delà d'environ 4 heures, avec un horizon à 50 % de réussite doublant environ tous les 7 mois sur six ans pour atteindre environ une heure début 2025 (*Claude 3.7 Sonnet*) [15].
  - Preuve L+ : `SRC-025.txt` (« almost 100% success rate on tasks taking humans less than 4 minutes, but succeed <10% of the time on tasks taking more than around 4 hours », « doubling time of around 7 months for the last 6 years », « Claude 3.7 Sonnet ... has a time horizon of approximately one hour »).
  - Constat initial : non supporté (l'énoncé initial affirmait « près de 50 minutes » et « pour un coût d'inférence dix fois moindre que le salaire horaire équivalent », absents de `SRC-025.txt` et de tout le corpus L+) ; rectifié et segment non supporté supprimé du manuscrit.
  - Verdict final : supporté.

- **A055** : L'audit `MAST` de Cemri *et al.* (*NeurIPS 2025*) analyse 1 642 traces issues de 7 cadriciels ouverts, mesure des taux d'échec de 41 % à 86,7 % et classe 14 modes de défaillance [17].
  - Preuve L+ : `SRC-028.txt` (`1642 annotated traces from seven popular MAS frameworks`, `41% to 86.7% failure rate`, `14 failure modes`) et `FACT-MAST-FAILURES`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A056** : Kim *et al.* mesurent sur des tâches contrôlées qu'une coordination multi-agents indépendante amplifie les erreurs de trace à 17,2× par rapport à l'agent unique, contre 4,4× en coordination centralisée [2].
  - Preuve L+ : `SRC-003.txt` (« Independent systems amplify trace-level errors 17.2× ... Centralized coordination, however, contains this to 4.4× »).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 24 (Erreurs silencieuses : HHEM-2.3 et AA-Omniscience)

- **A057** : Selon Stanford HAI 2026, les taux d'hallucination en synthèse documentaire sur `HHEM-2.3` vont de 1,8 % à 5,4 %, et sur *AA-Omniscience* (6 000 questions en six domaines, où un score négatif indique plus d'erreurs que de bonnes réponses) les taux d'hallucination s'échelonnent de 22 % à 94 % sur 26 modèles, la majorité dépassant 50 % [3].
  - Preuve L+ : `SRC-008.txt` p. 137, Figures 3.2.5 (`1.8% to 5.4%`) et 3.2.6 (`6,000 questions in six domains`, `negative scores indicate more hallucinations than correct responses`, `22% to 94%` sur 26 modèles, dont 18/26 ≥ 50 %).
  - Constat initial : imprécis (la formulation initiale supposait l'indice négatif lu directement alors que la Figure 3.2.7 est graphique sans valeurs extraites en texte, ce qui s'établit proprement via la règle de score et les 18 modèles sur 26 à ≥ 50 %) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 25 (Vecteurs de contamination Kim et al. et FM-3.2 MAST)

- **A058** : Kim *et al.* documentent la dérive numérique > 5 % par rapport à la vérité terrain (18,3 % en topologie centralisée ou décentralisée, jusqu'à 26,4 % en topologie hybride, contre 20,9 % à 24,1 % en référence mono-agent), la contradiction logique et l'omission graduelle de contraintes contextuelles [2].
  - Preuve L+ : `SRC-003.txt` p. 22 (`Numerical Drift: Baseline 20.9–24.1%. Centralized/Decentralized reduce to 18.3% ... Hybrid amplifies to 26.4%`, `Logical Contradiction`, `Context Omission`).
  - Constat initial : non supporté (le manuscrit mentionnait « des échecs financiers ou scientifiques », alors que `SRC-003.txt` ne teste pas de bancs scientifiques et porte sur les traces de sa taxonomie d'erreurs) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A059** : Cemri *et al.* illustrent le mode `FM-3.2` (*No or Incomplete Verification*) de `MAST` par un programme d'échecs généré par *ChatDev* qui compile et s'exécute sans exception malgré des violations des règles de jeu [17].
  - Preuve L+ : `SRC-028.txt` (« For example (FM-3.2), a ChatDev-generated chess program passes superficial checks (e.g., code compilation) but contains runtime bugs because it fails to validate against actual game rules »).
  - Constat initial : supporté.
  - Verdict final : supporté.

---

### Section 2.4 — Pourquoi les palmarès publics trompent les acheteurs

#### Paragraphe 26 (Trois biais et abandon des bancs formels dans MAP)

- **A060** : Face aux échecs multi-agents (41 %–86,7 %, `SRC-028`), 75 % des équipes suivies en étude de cas dans `MAP` évaluent sans jeux de bancs d'essai formels, recourant plutôt aux tests A/B, à la surveillance en production et aux retours d'experts [16].
  - Preuve L+ : `SRC-027.txt` § 6.1 (`Case study data shows formal benchmarks are even rarer: 75% evaluate without benchmark sets, relying instead on A/B testing, user feedback, and production monitoring`).
  - Constat initial : non supporté (le texte initial disait que 75 % « écartent les palmarès publics au profit d'évaluations internes privées ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 27 (Contamination : Llama 4 / Arena et Tran & Kiela MuSiQue)

- **A061** : Stanford HAI 2026 rapporte les critiques adressées en 2025 à Meta concernant l'optimisation de variantes de *Llama 4* pour améliorer son classement (contestées par Meta) et cite *The Leaderboard Illusion* (Singh *et al.*, 2025) montrant comment variantes hors registre public et accès inégal aux données biaisent les classements comme l'*Arena* [3].
  - Preuve L+ : `SRC-008.txt` p. 79–80 (« In 2025, Meta faced criticism that its Llama 4 model was optimized using specialized variants to improve leaderboard rankings... », « Singh et al., 2025 ... Arena »).
  - Constat initial : non supporté (le manuscrit insérait « d'avril 2025 », « Maverick » et « Chatbot Arena — une variante expérimentale optimisée pour les préférences humaines ayant obtenu un score supérieur à la version publiée », détails absents de `SRC-008.txt` et de tout le corpus L+) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A062** : Tran et Kiela (2026) montrent sur *MuSiQue* (4 sauts, budget de 1 000 jetons de réflexion) qu'une paraphrase syntaxique légère fait baisser l'architecture multi-agents séquentielle sous *Qwen3-30B-A3B* de 0,229 à 0,204 (agent unique : 0,260 à 0,249), tandis qu'une paraphrase sémantique profonde fait passer l'agent unique sous *Gemini 2.5 Flash* de 0,331 à 0,358 [18].
  - Preuve L+ : `SRC-031.txt` Annexe A (`Light Paraphrase ... Sequential MAS in Qwen3, which saw a significant drop (.229 -> .204)` ; `SAS ... Qwen3: .260 -> .249` ; `Deep Paraphrase ... Gemini-2.5-Flash, SAS performance jumped from .331 to .358 at 1k tokens` ; modèle exact `Qwen3-30B-A3B`).
  - Constat initial : non supporté (le texte initial citait le modèle inexistant « Qwen3-32B » et omettait la configuration *Sequential MAS* à 1 000 jetons) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 28 (Audit HAL et Genewein et al. / Paglieri et al. 2026)

- **A063** : L'audit `HAL` (Kapoor, Stroebl *et al.*, 2025) couvre 21 730 exécutions sur 9 modèles et 9 bancs en machines virtuelles isolées (~40 000 \$ US de calcul) et documente la recherche de réponses sur *HuggingFace* ou *arXiv* ainsi que l'usage d'une mauvaise carte de crédit en réservation aérienne [25].
  - Preuve L+ : `SRC-030.txt` Résumé et § 4.2 (`21,730 agent rollouts across 9 models and 9 benchmarks`, `about \$40,000`, `HuggingFace`, `arXiv`, `wrong credit card` en réservation de vol).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A064** : Genewein *et al.* soulignent la saturation des bancs statiques et rapportent le cas d'étude de Paglieri *et al.* (2026) où un essaim d'agents exploite un bogue d'un vérificateur automatique de preuves pour réécrire des problèmes mathématiques en formes triviales [1].
  - Preuve L+ : `SRC-001.txt` p. 28 (« through a bug in the automated proof checker, they can rewrite the problem to a trivially solvable one »).
  - Constat initial : imprécis (l'énoncé initial parlait de réécriture de « conjectures formelles pour tromper l'oracle » sans mentionner le bogue du vérificateur) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 29 (Défauts ABC, questions invalides, Pareto HAL et ACI)

- **A065** : En mobilisant la grille `ABC` (Zhu *et al.*, 2025), Kim *et al.* soulignent que des défauts de bancs induisent des erreurs relatives d'estimation pouvant atteindre 100 % [2].
  - Preuve L+ : `SRC-003.txt` (« Agentic Benchmark Checklist addressing flaws causing 100% relative misestimation »).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A066** : Truong *et al.* (2025, cités dans `SRC-008`) recensent des taux d'énoncés invalides allant de 2 % sur *MMLU Math* jusqu'à 42 % sur *GSM8K* [3].
  - Preuve L+ : `SRC-008.txt` p. 80 & Figure 2.1.5 (`from 2% on MMLU Math to 42% on GSM8K`).
  - Constat initial : imprécis (« 42 % dans certaines portions de GSM8K » remplacé par « 42 % sur GSM8K » conforme au rapport) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A067** : Kapoor *et al.* (cités dans [2, 17]) et `HAL` [25] montrent les biais d'un palmarès sans coût : *Claude Opus 4.1* (15 \$/75 \$ par million de jetons contre 1,25 \$/10 \$ pour *GPT-5*) n'apparaît sur la frontière coût-précision que dans 1 banc sur 8 évalués (le modèle le plus cher testé n'y figurant que dans 1 banc sur 9), alors que des options 10× à >100× moins chères par jeton (*GPT-5*, *o4-mini Low*, *Gemini 2.0 Flash*) dominent les compromis [25].
  - Preuve L+ : `SRC-030.txt` p. 5–6 (`\$15/\$75` vs `\$1.25/\$10`, `\$0.1/\$0.4` pour `Gemini 2.0 Flash`, `\$1.10/\$4.40` pour `o4-mini`, `Claude Opus 4.1 ... 1 of 8`, `In only 1 of 9 benchmarks do we observe the most costly model run on the Pareto frontier`, `Gemini 2.0 Flash (7 of 9)`, `GPT-5 (4 of 9)`, `o4-mini Low (4 of 9)`).
  - Constat initial : imprécis (le texte initial indiquait « 1 banc sur 9 » pour *Claude Opus 4.1* alors qu'il n'a pas été exécuté sur *Online Mind2Web*, et résumait par « dix fois moins coûteuses ») ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A068** : Kim *et al.* mesurent une corrélation modérée (\(r = 0{,}45\)) entre l'*Intelligence Index* statique et l'*Agentic Capability Index* (`ACI`), défini comme la performance mono-agent moyenne sur six bancs agentiques [2].
  - Preuve L+ : `SRC-003.txt` (« Agentic Capability Index (ACI), defined as each model's mean single-agent performance across all six benchmarks (correlation with Intelligence Index: r = 0.45) »).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Paragraphe 30 (Harnais, budget caché et annexe G Tran & Kiela)

- **A069** : Sur *SWE-bench Verified*, Stanford HAI isole les modèles sous un unique harnais standardisé (*mini-SWE-agent-v2*) pour neutraliser les différences d'échafaudage [3].
  - Preuve L+ : `SRC-008.txt` p. 100 (« only results using the mini-SWE-agent-v2 filter are included »).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A070** : Dans `HAL` sur *Online Mind2Web*, *SeeAct* avec *GPT-5 Medium* coûte 171 \$ US contre 1 577 \$ US pour *Browser-Use* avec *Claude Sonnet 4* (facteur 9× pour deux points d'écart), et accroître l'effort de raisonnement donne une précision égale ou inférieure dans 21 des 36 combinaisons [25].
  - Preuve L+ : `SRC-030.txt` p. 6–7 (`\$171` vs `\$1,577`, `9x difference in cost despite just a two-percentage-point difference`, `21 of 36 model-agent-benchmark combinations`).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A071** : L'enquête `MAP` montre que les invites et boucles de reprise épousent si étroitement un modèle donné qu'une mise à niveau vers un modèle plus récent brise régulièrement les flux existants [16].
  - Preuve L+ : `SRC-027.txt` § 5.3 (« Agent scaffolds, prompts, and evaluations lock onto specific model behaviors. Deploying newer models can break agent workflows »).
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A072** : Tran et Kiela (2026) montrent qu'à budget égal de jetons de réflexion, l'agent unique égale ou surpasse le multi-agents ; leur annexe G révèle que l'API de *Gemini 2.5 Flash* (budget demandé de 10 000 jetons en agent unique) rapporte 1 687 jetons de réflexion pour 251 mots visibles (soit 359 jetons équivalents, facteur 4,7×) [18].
  - Preuve L+ : `SRC-031.txt` Résumé et Annexe G, Table 7 (`Gemini-2.5-Flash with a requested 10k budget, the SAS pipeline reported an average of 1,687 thinking tokens ... 251 words, a proxy for 359 tokens ... 4.7x inflation factor`).
  - Constat initial : imprécis (cadre « budget demandé de 10 000 jetons en agent unique » omis) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

#### Paragraphe 31 (τ-bench 2024 et 2026)

- **A073** : Dans *τ-bench* (Yao *et al.*, 2024), *gpt-4o* en appel de fonctions plafonne sous 50 % en moyenne (48,2 % ; 35,2 % sur *τ-airline*) et, malgré > 60 % sur *τ-retail*, s'effondre sous 25 % en `pass^8`, tout en consacrant 95,9 % de sa facture d'API aux jetons d'entrée — alourdis par les politiques et schémas d'outils — contre 4,1 % aux sorties [24].
  - Preuve L+ : `SRC-029.txt` Table 2 (`48.2` avg, `35.2` airline, `61.2` retail), p. 1 & 6 (`pass^8 < 25%`, `input prompt / completion output take up 95.9% / 4.1% of the price respectively, so the cost is mainly due to long system prompt (domain policy + function definitions)`).
  - Constat initial : imprécis (l'énoncé initial ne précisait pas que 95,9 % porte sur les jetons d'entrée vs 4,1 % en sortie) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A074** : En 2026 sur les tâches de *τ-bench* reprises dans Stanford HAI, les meilleurs modèles restent entre 62,9 % et 70,2 % en `pass@1` [3].
  - Preuve L+ : `SRC-008.txt` Figure 2.6.6 (`62.9% to 70.2%`).
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Trilemme d'évaluation et Paragraphe 32 (FOCUS v1.4 et CPO)

- **A075** : Au point 1 du trilemme, 25 % (5 sur 20) des équipes `MAP` suivies en étude de cas bâtissent leurs jeux étalons internes sur mesure, tandis que 75 % renoncent aux bancs d'essai formels [16].
  - Preuve L+ : `SRC-027.txt` § 6.1 (`75% evaluate without benchmark sets ... Five teams build custom benchmarks`).
  - Constat initial : non supporté (le manuscrit écrivait « les 75 % d'équipes MAP qui construisent leurs propres jeux privés », inversant la proportion 25 % vs 75 %) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

- **A076** : Aux points 2–3 du trilemme et au paragraphe final d'analyse, la spécification `FOCUS v1.4` de la *FinOps Foundation* fournit un schéma ouvert normalisé de facturation et d'utilisation infonuagique [13], étayant avec `ABC` [2], `HAL` [25], `τ-bench` [24] et [1, 3, 18] le calcul du **coût complet par résultat conforme** (`CPO`).
  - Preuve L+ : `SRC-023.txt` (`Abstract`), `SRC-003.txt`, `SRC-029.txt`, `SRC-030.txt`, `SRC-031.txt`, `glossaire-termes.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.

#### Encadré « Trois arbitrages sans regret » et transition finale

- **A077** : Premier arbitrage : ventiler les budgets selon les six périmètres en partant du marché logiciel ouvert 2026 (5,3 à 9,9 G\$ US) [4, 5, 6, 13].
  - Preuve L+ : `SRC-011.txt`, `SRC-012.txt`, `SRC-013.txt`, `SRC-023.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A078** : Deuxième arbitrage : remplacer `pass@1` par le coût par résultat conforme (`pass^k`, budget contrôlé sous `FOCUS v1.4`) [2, 13, 18, 24, 25].
  - Preuve L+ : `SRC-003.txt`, `SRC-023.txt`, `SRC-029.txt`, `SRC-030.txt`, `SRC-031.txt`.
  - Constat initial : supporté.
  - Verdict final : supporté.

- **A079** : Troisième arbitrage : segmenter toute chaîne probabiliste entre 3 et 5 étapes par validateurs déterministes et reprises locales, à l'image des 47 % de systèmes `MAP` bornés sous 5 étapes, pour maîtriser la loi de Lusser et la propagation d'erreurs [14, 16, 17].
  - Preuve L+ : `SRC-024.txt` (modèle en série), `SRC-027.txt` § 5.4 (`47% execute fewer than 5 steps`), `SRC-028.txt` (`MAST`).
  - Constat initial : imprécis (l'appui empirique des 47 % de systèmes `MAP` bornés sous 5 étapes manquait pour ancrer la cible prescriptive 3–5 étapes) ; rectifié dans le manuscrit.
  - Verdict final : supporté.

---

## Contrôle différentiel post-G4

- **Périmètre vérifié** : Lignes `43–78` de `7 - Livre 2027/manuscrit/01 - Partie I/Chapitre 02 - L epreuve des mesures.md` (assertions `A030–A050`) après retouche stylistique `G4`, contrôlées directement contre les textes intégraux `corpus_l_plus/*.txt` (`SRC-008.txt`, `SRC-009.txt`, `SRC-010.txt`, `SRC-014.txt`, `SRC-015.txt`, `SRC-016.txt`, `SRC-025.txt`, `SRC-027.txt`).
- **Date et régime** : 2026-11-22 (barrière `G2` différentielle, régime Production, gel documentaire au 31 décembre 2026).

### Écarts factuels détectés après `G4` et rectifiés dans le manuscrit (`L43–L78`)

1. **Becker *et al.* (2025, `METR`), cité dans `SRC-008.txt` (`L51`, `L60` ; réf. `A035`, `A038`)** — *Non supporté / Imprécis rectifié* :
   - Écarts relevés : la retouche `G4` qualifiait l'échantillon de « mainteneurs *open source* expérimentés travaillant sur leurs propres dépôts matures », la méthode d'« essai randomisé », l'illusion subjective de « sentiment d'accélération » et la non-reproduction fin 2025 d'un échec « parce que plusieurs développeurs ont refusé de rester sans outil dans le groupe témoin ». Aucun de ces éléments ne figure dans `SRC-008.txt` (p. 219–220 et Figure 4.4.27) ni dans `SRC-025.txt` (Kwa *et al.*, mars 2025, qui porte sur l'horizon temporel des tâches et ne contient pas Becker *et al.*). De plus, `L51` omettait le second facteur explicite mentionné par `SRC-008.txt` (le fait que les développeurs fin 2025 semblaient probablement accélérés par l'IA par rapport à la période initiale).
   - Rectification : réancrage mot pour mot sur `SRC-008.txt` (`développeurs open source expérimentés`, `-19 %`, `alors même qu'ils jugent ces outils utiles` / `aide perçue`, `réticence croissante à travailler sans IA` et `développeurs fin 2025 semblaient plutôt accélérés par rapport à la période initiale` ; Tableau 2.2 : `Étude empirique ; développeurs open source expérimentés`, `Assistant L1 (outils open source)`).
2. **Shen et Tamkin (2025), cité dans `SRC-008.txt` (`L51` ; réf. `A036`)** — *Imprécis rectifié* :
   - Écart relevé : l'expression « pénalités d'acquisition conceptuelle » déformait « *learning penalties* » et occultait que le questionnement conceptuel (`conceptual inquiry`) était justement la pratique des meilleurs profils (`65%+`) permettant d'éviter ces pénalités (`SRC-008.txt`, p. 219–220, Figure 4.4.27).
   - Rectification : rétablissement de « pénalités d'apprentissage » et précision exacte du rôle du questionnement conceptuel.
3. **Cui *et al.* (2025), `SRC-010.txt` (`L49` ; réf. `A033`)** — *Imprécis rectifié* :
   - Écart relevé : l'énoncé « tout en relevant une variation statistiquement non significative des soumissions de code » prêtait à confusion entre `Brynjolfsson et al.` et `Cui et al.`, ainsi qu'entre les *pull requests* significatives (`+26,08 %`, `ET : 10,3 %`) et les `commits` non significatifs en estimation instrumentale (`+13,55 %`, `ET : 10,0 %`, `SRC-010.txt` Table 3).
   - Rectification : attribution explicite à `Cui et al.` en estimation instrumentale et désignation exacte `validations unitaires (commits)`.
4. **Brynjolfsson *et al.* (2025, `QJE`), cité dans `SRC-008.txt` (`L58` ; réf. `A038`)** — *Imprécis rectifié* :
   - Rectification de « débutants » vers « moins expérimentés » (`Less experienced/skilled agents`, `SRC-008.txt`, Figure 4.4.27).
5. **Aldasoro *et al.* (2026) et Yotzov *et al.* (2026), cités dans `SRC-008.txt` (`L62` ; réf. `A040`)** — *Imprécis rectifié* :
   - Rectification de « Enquêtes 12 000 firmes... » vers « Étude de 12 000 firmes européennes et enquête de 6 000 dirigeants (4 pays) » et précision de « +4 % de productivité du travail en Europe » (`SRC-008.txt`, p. 220–221, Figure 4.4.28).
6. **Statistique Canada T2/T3 2026, `SRC-014.txt` et `SRC-015.txt` (`L68` ; réf. `A043`, `A044`)** — *Imprécis rectifié* :
   - Écart relevé : « sur les douze mois précédant le deuxième trimestre 2026 » ne reflétait pas la fenêtre réelle de collecte (`1er avril au 6 mai 2026` sur les 12 derniers mois, `SRC-014.txt` Note 8), et le libellé T3 raccourcissait « agents virtuels ou robots conversationnels » en « agents virtuels » (`SRC-015.txt` v1937048782 et Notes 8–9).
   - Rectification : précision des périodes de collecte (`avril à mai` et `juillet à août`) et reprise complète du libellé « agents virtuels ou robots conversationnels ».
7. **Brynjolfsson *et al.* (2026), Brynjolfsson *et al.* (2025) et McKinsey (2025), cités dans `SRC-008.txt` (`L72`, `L74` ; réf. `A047`, `A048`)** — *Non supporté / Imprécis rectifié* :
   - Écarts relevés : omission de « par an » pour le surplus du consommateur de `172 G$ US` (`$172 billion annually`, p. 192) et de « aux États-Unis » pour le recul de près de 20 % des développeurs de 22 à 25 ans (`In the United States`, p. 222) ; surtout, `L74` affirmait « seul le secteur technologique atteignant 24 % en génie logiciel, 22 % en informatique et 21 % en opérations de service », alors que `SRC-008.txt` (p. 197) indique « *the technology sector had comparatively higher rates* » sans affirmer d'exclusivité absolue, et précisait « *Even in functions with the most activity, including IT and knowledge management* ».
   - Rectification : ajout de « par an » et « aux États-Unis », rétablissement de « même dans les fonctions les plus actives » et remplacement de « seul le secteur technologique » par « le secteur technologique affichant toutefois des taux comparativement plus élevés ».
8. **Enquête `MAP` (`Pan et al.`, 2025/2026), `SRC-027.txt` (`L63`, `L76` ; réf. `A041`, `A049`)** — *Imprécis rectifié* :
   - Rectification de « 86 en exploitation » vers « 86 systèmes déployés en production ou en pilote » (`86 systems in production or pilot phases`, `SRC-027.txt`, § 1 et § 3.2) et alignement de la phrase conclusive sur les « déploiements documentés jusqu'au gel de fin 2026 ».
9. **Éléments vérifiés conformes sans retouche requise** : `Noy & Zhang (2023)` (`SRC-009.txt` : `-40 %`, `+18 %`, réduction des écarts, `1,6×` à deux mois), `Choi & Xie (2025)` (`+55 %`), `Ju & Aral (2025)` (`+50 %`), `Gemini Deep Think` (`35 points`, or IMO 2025) vs `ClockBench` (`50,6 %` vs `90,1 %`), `Banque du Canada SAP 2026-22` (`SRC-016.txt` : 2 juin 2026, 314 dirigeants de déc. 2025, `70 %`, `8 %`, `21 %`, `29 %`, `11 %`, filtre Q4/Q5, `18 %` vs `9 %`, `~30 %` = `20 %` mineur + `10 %` majeur), et `Penn Wharton Budget Model` (`+0,01` point PTF) / `courbe en J`.

### Certification différentielle post-G4

- **Assertions réauditées (`L43–L78`, `A030–A050`)** : 21 / 21 (`100 %` supportées après rectifications)
- **Couverture globale certifiée (`ch02`, `A001–A079`)** : `100 %` `supporté` (`79/79`)
- **Imprécis résiduel** : `0`
- **Non supporté résiduel** : `0`

---

## Contrôle différentiel post-lissage G5

- **Périmètre contrôlé** : `git diff HEAD` sur `manuscrit/01 - Partie I/Chapitre 02 - L epreuve des mesures.md` depuis `fe6e945` — `47` items différentiels (`31` lignes à retrait seul de rétro-apostrophes et `16` blocs substantifs couvrant `L13`, `L17`, `L19`, `L21`, `L23`, `L49`, `L68`–`L74`, `L80`, `L84`, `L86`, `L102`, `L112`, `L120`), vérifiés contre `sources/ch02-sources.md` et `recherche/corpus_l_plus/*.txt`.
- **Constat et rectifications appliquées dans `Chapitre 02`** :
  - `31` lignes à retrait seul de rétro-apostrophes et `12` blocs substantifs conformes d'emblée ; `2` tableaux et renvois `[n]` intacts.
  - `4` paragraphes rectifiés directement dans le manuscrit : `L68` (rétablissement des dénominateurs exacts `entreprises utilisatrices de l'IA` et `parmi celles prévoyant d'y recourir` pour `SRC-014.txt`/`SRC-015.txt`, libellé complet `très peu fréquent, expérimental ou en projets pilotes` et filtre de sous-échantillon `parmi les firmes utilisatrices ou planifiant d'adopter l'IA` pour `SRC-016.txt`), `L70` (`synthèses reprises par Stanford HAI`, `+0,01 point de pourcentage`, `environ deux tiers ou plus` et suppression de l'exclusivité erronée `hormis le secteur technologique` au profit de `taux comparativement plus élevés` selon `SRC-008.txt`), `L72` (attribution exacte de `80 %` / `72 %` aux `praticiens sondés` plutôt qu'aux `équipes interrogées`, remplacement de `graphes d'exécution fixes` par `flux structurés fixes` selon `SRC-027.txt`, et séparation entre l'apport `[16]` et la qualification normative `régime L1`), `L102` (rétablissement de la définition exacte de l'`ACI` selon `SRC-003.txt`).
- **Verdict final — supporté** : `100 %` (`47/47` items différentiels)
- **Imprécis résiduel** : `0`
- **Non supporté résiduel** : `0`
