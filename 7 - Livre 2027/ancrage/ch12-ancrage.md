# Audit d'ancrage atomique Wyvern (G2) — Chapitre 12

- **Unité** : `ch12` — [Chapitre 12 - Decider sous incertitude profonde 2027-2035.md](../manuscrit/04%20-%20Partie%20IV/Chapitre%2012%20-%20Decider%20sous%20incertitude%20profonde%202027-2035.md)
- **Dossier de sources fermé** : [ch12-sources.md](../sources/ch12-sources.md) (`18` sources intégrales `L+` sous `recherche/corpus_l_plus/`)
- **Registres vérifiés** : `registre/ancres-chronologiques.json`, `registre/faits-empiriques.json`, `registre/glossaire-termes.json`
- **Date de gel des faits** : `31 décembre 2026`
- **Rôle et régime** : Agent auditeur indépendant `auditeur-wyvern` (barrière `G2`, `CA-10`, `CA-12`, régime Production)

## Bilan quantifié de l'audit

- **Total d'affirmations atomiques auditées** : `78` (`A01` à `A78`)
- **Constat initial — supportés** : `63` (`80,8 %`)
- **Constat initial — imprécis (rectifiés en séance)** : `15` (`19,2 %`)
- **Constat initial — non supportés** : `0` (`0,0 %`)
- Verdict final — supportés : 78 (100 %)
- Verdict final — imprécis résiduels : 0
- Verdict final — non supportés résiduels : 0

---

## Détail paragraphe par paragraphe

### En-tête et question directrice (L1–L3)

- **A01** (L1, L3) — *Affirmation* : Le chapitre pose la question du séquençage des investissements entre les 90 premiers jours et l'horizon structurel `2028–2035` sous incertitude profonde.
  - *Sources* : `registre/ancres-chronologiques.json` (horizon `2026–2035`), `SRC-072.txt` (`DAPP`).
  - Constat initial : supporté — Cadrage éditorial conforme au périmètre chronologique et méthodologique vérifié.
  - Verdict final : supporté

### Introduction — Paragraphe 1 : horloge des certificats TLS publics (L5)

- **A02** (L5) — *Affirmation* : Le *Ballot SC-081v3* (`SC081`) intégré aux *Baseline Requirements* v2.3.1 du *CA/Browser Forum* (4 octobre 2026, sections `4.2.1` et `6.3.2`) gouverne la validité et le réemploi des validations des certificats `TLS` publics.
  - *Sources* : `ch12-sources.md` `[8]`, `SRC-053.txt` (l. 2–8 : Version `2.3.1`, `4-Oct-2026`; l. 151 : `SC081` dans l'historique des révisions; l. 1298–1325 § `4.2.1`; l. 2183–2201 § `6.3.2`).
  - Constat initial : imprécis — `SRC-053.txt` emploie le code `SC081` dans son historique (`l. 151`), tandis que `SC-081v3` provient de la désignation du scrutin externe reprise dans `ch12-sources.md` `[8]` et `ancres-chronologiques.json`. *Rectification apportée* : ajout explicite de `(SC081)` après `*Ballot SC-081v3*` à la ligne 5.
  - Verdict final : supporté

- **A03** (L5) — *Affirmation* : La réduction de la durée maximale de validité et de réutilisation des preuves de domaine/IP à `200 jours` est entrée en vigueur le `15 mars 2026`.
  - *Sources* : `SRC-053.txt` (l. 190 : § `4.2.1` `2026-03-15` `200 days`; l. 192 : § `6.3.2` `2026-03-15` `200 days`; l. 1322, 2187).
  - Constat initial : supporté
  - Verdict final : supporté

- **A04** (L5) — *Affirmation* : La durée maximale de validité et de réutilisation des validations de domaine ou d'adresse `IP` tombe à `100 jours` le `15 mars 2027`.
  - *Sources* : `SRC-053.txt` (l. 199–200, 1323, 2189 : `2027-03-15`, `100 days`), `registre/ancres-chronologiques.json` (`2027-03-15-TLS-100J`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A05** (L5) — *Affirmation* : La durée maximale de validité tombe à `47 jours` — avec une réutilisation des validations ramenée à `10 jours` — le `15 mars 2029`.
  - *Sources* : `SRC-053.txt` (l. 204 : § `4.2.1` `2029-03-15` `10 days`; l. 205 : § `6.3.2` `2029-03-15` `47 days`; l. 1324, 2191), `registre/ancres-chronologiques.json` (`2029-03-15-TLS-47J`).
  - Constat initial : supporté
  - Verdict final : supporté

### Introduction — Paragraphe 2 : horloge cryptographique post-quantique (L7)

- **A06** (L7) — *Affirmation* : En août 2024, la norme `NIST FIPS 204` a formalisé l'algorithme de signature post-quantique sur réseaux euclidiens `ML-DSA`.
  - *Sources* : `ch12-sources.md` `[5]`, `SRC-050.txt` (l. 1–12 : `Published August 13, 2024`; l. 46–52 : `Module-Lattice-Based Digital Signature Standard`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A07** (L7) — *Affirmation* : Dans le tableau officiel des tailles (`Table 2`), une signature `ML-DSA-65` atteint `3 309 octets` et `ML-DSA-87` atteint `4 627 octets`, soit respectivement environ `52×` et `72×` une signature elliptique classique de `64 octets`.
  - *Sources* : `SRC-050.txt` (`Table 2`, p. 16, l. 1308–1321 : `ML-DSA-65` = `3309`, `ML-DSA-87` = `4627`), `registre/faits-empiriques.json` (`FACT-PQC-SIGNATURE-SIZE`), `ch12-sources.md` `[5]`.
  - Constat initial : imprécis — `SRC-050.txt` `Table 2` donne `3 309` et `4 627` octets, mais ne comporte pas la référence `64 octets` ni les ratios `~52×`/`~72×` (qui proviennent du repère `FACT-PQC-SIGNATURE-SIZE`). *Rectification apportée* : reformulation distinguant nettement les chiffres de la table `2` du repère comparatif `64 octets`.
  - Verdict final : supporté

- **A08** (L7) — *Affirmation* : En janvier 2026, le *G7 Cyber Expert Group* (`CEG`) a publié une feuille de route coordonnée invitant les institutions financières à viser `2035` pour achever leur transition post-quantique tout en priorisant les systèmes critiques dans la fenêtre indicative `2030–2032`.
  - *Sources* : `ch12-sources.md` `[7]`, `SRC-052.txt` (l. 3–15 : `January 2026`, `non-authoritative`; l. 189–198 : `2035 as an overall target date`, `2030-32`; note `9` l. 216–218), `registre/ancres-chronologiques.json` (`2030-2035-G7-PQC-FINANCE`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A09** (L7) — *Affirmation* : Cette cible est cohérente avec l'horizon fédéral documenté dans `NIST IR 8547`.
  - *Sources* : `ch12-sources.md` `[6]`, `SRC-051.txt` (l. 1100–1116 : `NSM-10` et cible fédérale `2035`).
  - Constat initial : supporté
  - Verdict final : supporté

### Introduction — Paragraphe 3 : collision des trois horloges (L9)

- **A10** (L9) — *Affirmation* : Des obligations prudentielles et sectorielles s'enclenchent dès `2027` et `2028` au Canada et en Europe, exigeant de séparer les 90 premiers jours, le noyau sans regret et les options conditionnelles jusqu'en `2035` face aux seuils `47 jours` et `50×–72×`.
  - *Sources* : `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`, `2027-12-02-EU-AI-ACT-ANNEXE-III`, `2028-08-02-EU-AI-ACT-ANNEXE-I`, `2028-10-01-GESTION-PATRIMOINE-RETROFACTURATION`, `2028-12-31-BSIF-B15-PORTEE3`), `SRC-050.txt`, `SRC-053.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

- **A11** (L9) — *Affirmation* : Les passerelles patrimoniales, chaînes `OAuth` sous-dimensionnées et `PKI` artisanales ne peuvent absorber ni une rotation à `47 jours` ni l'expansion des signatures sans préparation architecturale.
  - *Sources* : `SRC-051.txt` (§ 2.2 l. 631–737), `SRC-053.txt` (§ 6.3.2 l. 2191), `SRC-050.txt` (l. 1317–1321).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.1 — Paragraphe 4 : incertitude profonde (L13)

- **A12** (L13) — *Affirmation* : Au `31 décembre 2026`, nul ne connaît la trajectoire exacte du coût marginal d'inférence, l'issue de la concurrence entre protocoles ouverts et suites fermées ni la date d'apparition d'un `CRQC`.
  - *Sources* : `SRC-051.txt` (l. 1179–1181), `SRC-052.txt` (l. 179–181 : *trajectory of quantum computing development is uncertain*), date de gel du dossier (`31 décembre 2026`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A13** (L13) — *Affirmation* : Dans les situations d'incertitude profonde (*deep uncertainty*), où l'on ne s'accorde ni sur une distribution de probabilités ni sur un modèle unique du système, optimiser pour un scénario central crée des verrouillages précoces (*lock-ins*) et des actifs échoués (*stranded assets*).
  - *Sources* : `ch12-sources.md` `[18]`, `SRC-072.txt` (l. 76–78, 98 : *system structure*, 221, 225, 237 : *uncertainty that cannot be quantified with probability distributions*).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.1 — Paragraphe 5 : méthode DAPP (L15)

- **A14** (L15) — *Affirmation* : Marjolijn Haasnoot, Andrew Warren et Jan H. Kwakkel (`2019`) exposent la méthode `DAPP` (*Dynamic Adaptive Policy Pathways*), issue de travaux lancés dès `2013` sur la gestion de l'eau et les grandes infrastructures à longue durée de vie avant d'être étendue aux systèmes sociotechniques complexes.
  - *Sources* : `ch12-sources.md` `[18]`, `SRC-072.txt` (l. 7–11, 76–80 : citation `Haasnoot et al. 2013` et origine en *water management* / infrastructures à longue durée de vie; l. 225 : *complex coupled physical–technical–human systems*).
  - Constat initial : imprécis — Le texte initial écrivait que Haasnoot, Warren et Kwakkel (`2019`) « ont formulé » `DAPP`, alors que `SRC-072.txt` crédite `Haasnoot et al. (2013)` de la formulation originelle sur la gestion de l'eau et expose la méthode en `2019`. *Rectification apportée* : remplacement par « exposent... issue de travaux lancés dès `2013` sur la gestion de l'eau et les grandes infrastructures... ».
  - Verdict final : supporté

- **A15** (L15) — *Affirmation* : `DAPP` identifie les conditions générales sous lesquelles une politique cesse de remplir ses objectifs — un **point de bascule d'adaptation** (`ATP`) — ainsi que les **points d'opportunité**.
  - *Sources* : `SRC-072.txt` (l. 27, 78, 102, 235).
  - Constat initial : supporté
  - Verdict final : supporté

- **A16** (L15) — *Affirmation* : La stratégie dynamique combine des actions initiales immédiates (actions de base, actions correctives/défensives et mesures habilitantes gardant les options ouvertes), des choix de long terme suspendus et des **signaux avancés** (*signposts*).
  - *Sources* : `SRC-072.txt` (l. 31, 86, 146–154).
  - Constat initial : supporté
  - Verdict final : supporté

- **A17** (L15) — *Affirmation* : La carte en plan de métro — complétée par des tableaux d'évaluation (*scorecards*) échelonnés dans le temps et des scénarios transitoires plutôt que statiques — révèle la dépendance de sentier (*path dependency*).
  - *Sources* : `SRC-072.txt` (l. 25, 29, 76, 98, 120–134, 198).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.1 — Paragraphe 6 : scénario A — socle ouvert étendu (L17)

- **A18** (L17) — *Affirmation* : La norme `IETF RFC 9943` adoptée en juin 2026 définit `SCITT` (*Supply Chain Integrity, Transparency, and Trust*).
  - *Sources* : `ch12-sources.md` `[3]`, `SRC-044.txt` (l. 4–11 : *RFC 9943*, *Standards Track*, *June 2026*; l. 107–108 : *SCITT*).
  - Constat initial : supporté
  - Verdict final : supporté

- **A19** (L17) — *Affirmation* : `SCITT` permet d'enregistrer des énoncés signés sur l'origine d'artefacts logiciels dans des journaux transparents anti-équivocation produisant des reçus cryptographiques vérifiables sans devoir faire confiance à un intermédiaire unique.
  - *Sources* : `SRC-044.txt` (l. 104–116, 586–596 : *universally verifiable without online access to the TS*, l. 808–816 : *Append-only*, *Non-equivocation*, l. 1391–1400 : *does not require trust in a single centralized TS*).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.1 — Paragraphe 7 : scénario B — archipel de plateformes fermées (L19)

- **A20** (L19) — *Affirmation* : Une migration tardive hors d'une plateforme verrouillée expose à des coûts de transfert (*transfer costs*) prohibitifs.
  - *Sources* : `ch12-sources.md` `[18]`, `SRC-072.txt` (l. 134, 237 : hausse significative des coûts quand les *transfer costs* sont comptabilisés).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.1 — Paragraphe 8 : scénario C — fragmentation en blocs souverains (L21)

- **A21** (L21) — *Affirmation* : Au gel du `31 décembre 2026`, un écart réglementaire existe déjà entre l'approche prudentielle canadienne (`BSIF E-23`, bulletin `BSIF` juillet 2026, *Loi sur les banques*) et l'`EU AI Act` modifié par le Règlement `(UE) 2026/1744`.
  - *Sources* : `SRC-060.txt`, `SRC-061.txt`, `SRC-065.txt`, `SRC-066.txt`, `SRC-070.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.1 — Figure 21, synthèse et Tableau 1 (L23–L37)

- **A22** (L23–L27) — *Affirmation* : La Figure 21 adapte la carte de trajectoires `DAPP` de Haasnoot, Warren et Kwakkel (`2019`) à l'horizon `2027–2035`.
  - *Sources* : `SRC-072.txt` (l. 120–128, 198–204).
  - Constat initial : supporté
  - Verdict final : supporté

- **A23** (L29) — *Affirmation* : Le socle sans regret inclut l'automatisation `PKI` face aux échéances `100 jours` (`15 mars 2027`) et `47 jours` (`15 mars 2029`) [8] et l'agilité post-quantique face au facteur `~52×` à `~72×` de `ML-DSA` [5], l'ensemble convergeant vers la cible `2035` du `G7 CEG` [7] et de `NIST IR 8547` [6].
  - *Sources* : `SRC-053.txt` (l. 199–205), `SRC-050.txt` (l. 1317–1321), `FACT-PQC-SIGNATURE-SIZE`, `SRC-052.txt` (l. 190), `SRC-051.txt` (l. 1100–1116).
  - Constat initial : supporté
  - Verdict final : supporté

- **A24** (L31–L37) — *Affirmation* : Le tableau comparatif des trois scénarios ancre `SCITT RFC 9943` [3] et les coûts de transfert [18] comme repères de décision différée.
  - *Sources* : `SRC-044.txt`, `SRC-072.txt` (l. 134, 237).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 10 : BSIF E-23 et AMF (L41)

- **A25** (L41) — *Affirmation* : La ligne directrice `E-23` révisée du `BSIF` sur la gestion du risque de modélisation à l'échelle de l'entreprise entre en vigueur le `1er mai 2027`.
  - *Sources* : `ch12-sources.md` `[12]`, `SRC-065.txt` (l. 46, 175–177 : « Le 1 mai 2027 », 254), `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A26** (L41) — *Affirmation* : `BSIF E-23` soumet les modèles d'IA et d'apprentissage automatique à une discipline couvrant inventaire, cotation du risque, validation indépendante, suivi continu et mise hors service.
  - *Sources* : `SRC-065.txt` (l. 248, 300–322, 404–448, 594–697).
  - Constat initial : supporté
  - Verdict final : supporté

- **A27** (L41) — *Affirmation* : Au Québec, la ligne directrice sur l'IA de l'`AMF` prend effet le `1er mai 2027`, information documentée par le registre secondaire ouvert `AIBanks.ca` (`1er novembre 2026`) en raison du blocage technique `HTTP 403` sur `lautorite.qc.ca`.
  - *Sources* : `ch12-sources.md` (note `AO-01` l. 11 et `[17]`), `SRC-071.txt` (l. 6, 271–275), `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 11 : jalons 2027–2028 EU AI Act, ACVM 31-103 et BSIF B-15 (L43)

- **A28** (L43) — *Affirmation* : Le Règlement `(UE) 2026/1744` du `8 juillet 2026` (publié au *Journal officiel* le `24 juillet 2026`) a révisé l'article `113` de l'`EU AI Act` (Règlement `(UE) 2024/1689`).
  - *Sources* : `ch12-sources.md` `[10, 11]`, `SRC-060.txt` (l. 7331–7348), `SRC-061.txt` (l. 1–5, 37–39, 1844).
  - Constat initial : supporté
  - Verdict final : supporté

- **A29** (L43) — *Affirmation* : Les systèmes à haut risque de l'Annexe III seront soumis aux exigences européennes à compter du `2 décembre 2027`, et ceux de l'Annexe I à compter du `2 août 2028`.
  - *Sources* : `SRC-061.txt` (l. 1850–1854 : chap. III sections 1, 2 et 3), `registre/ancres-chronologiques.json` (`2027-12-02-EU-AI-ACT-ANNEXE-III`, `2028-08-02-EU-AI-ACT-ANNEXE-I`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A30** (L43) — *Affirmation* : L'avis publié le `8 octobre 2026` par les `ACVM` / `CVMO` adopte la modification de la Norme canadienne `31-103` proscrivant les rétrofacturations de commissions dans la distribution de titres de fonds d'investissement émetteurs assujettis, avec entrée en vigueur prévue le `1er octobre 2028` (sous réserve des approbations ministérielles requises et hors titres achetés avant cette date).
  - *Sources* : `ch12-sources.md` `[15]`, `SRC-069.txt` (l. 6–24, 618–657, 722–737), `registre/ancres-chronologiques.json` (`2028-10-01-GESTION-PATRIMOINE-RETROFACTURATION`).
  - Constat initial : imprécis — Le texte initial omettait la restriction aux fonds d'investissement **émetteurs assujettis** (confirmée en Partie 4 de `SRC-069.txt`, l. 628–657) ainsi que la mention des approbations ministérielles requises (`l. 23`). *Rectification apportée* : ajout de « titres de fonds d'investissement émetteurs assujettis » et « prévue... sous réserve des approbations ministérielles requises ».
  - Verdict final : supporté

- **A31** (L43) — *Affirmation* : Pour la fin de l'exercice financier `2028`, l'annexe `2-2` (`b) ii`) de `BSIF B-15` fixe l'attente de divulgation des émissions absolues brutes de portée `3`, incluant obligatoirement la catégorie `15` (prêts, investissements et portefeuilles d'assurance multirisque hors assurance hypothécaire), tandis que `b) iii` (actifs sous gestion) demeure à déterminer (`TBD`).
  - *Sources* : `ch12-sources.md` `[14]`, `SRC-067.txt` (l. 510 : *Fiscal year-end for which implementation is expected*, l. 667–680, 711–754 : *property and casualty insurance (excluding mortgage insurance)*, `2028` vs `TBD`), `registre/ancres-chronologiques.json` (`2028-12-31-BSIF-B15-PORTEE3`).
  - Constat initial : imprécis — La mention « exercice financier de fin 2028 » et « portefeuilles d'assurance » gagnait à être alignée exactement sur « fin de l'exercice financier `2028` » et sur l'assurance multirisque hors assurance hypothécaire (`SRC-067.txt`, l. 677). *Rectification apportée* : précision textuelle à la ligne 43.
  - Verdict final : supporté

### Section 12.2 — Paragraphe 12 : état du marché canadien et bulletin BSIF (L45)

- **A32** (L45) — *Affirmation* : L'édition du `1er novembre 2026` du *Canadian Bank AI Index* (`AIBanks.ca`) compile `210` déploiements publics dans `27` institutions actives sur `35` banques, coopératives et fintechs canadiennes.
  - *Sources* : `ch12-sources.md` `[17]`, `SRC-071.txt` (l. 5–6 : *35 Canadian banks, credit unions and fintechs*, *210-entry database*, *Figures as of November 1, 2026*; l. 101–105 : `210`, `27 institutions`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A33** (L45) — *Affirmation* : `21 %` des déploiements touchent directement les clients et `13 %` opèrent à l'arrière-plan sur leurs comptes, tandis que la majorité porte sur des outils internes ou la recherche.
  - *Sources* : `SRC-071.txt` (l. 107–111 : `21%`, `Another 13% run on customer accounts unseen`; l. 128 : *Most of what banks announce is for staff or research, not for customers*; l. 169–175).
  - Constat initial : supporté
  - Verdict final : supporté

- **A34** (L45) — *Affirmation* : Seules `6` institutions sur `35` publient des principes d'IA responsable et `13` informent leurs clients du recours à l'IA ou aux décisions automatisées.
  - *Sources* : `SRC-071.txt` (l. 113–117 : `6 of 35`, `13 tell customers when AI or automated decisions are used`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A35** (L45) — *Affirmation* : Dès juillet 2026, le bulletin du `BSIF` sur l'IA générative et agentique rappelle que le raisonnement et l'exécution autonomes accroissent la vitesse et l'ampleur des défaillances au regard de `B-13`, `B-10` et `E-21`, et recommande l'*AI harnessing*, la maîtrise des identités et les plans de repli manuel.
  - *Sources* : `ch12-sources.md` `[13]`, `SRC-066.txt` (l. 63–69, 145, 359, 495).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 13 : Priorité 1 — inventaire et responsable (L47)

- **A36** (L47) — *Affirmation* : Conformément aux principes `1.1` et `2.1` de `BSIF E-23`, chaque modèle présentant un risque inhérent non négligeable doit être consigné à l'inventaire sous la gouverne d'un responsable désigné sur tout son cycle de vie.
  - *Sources* : `SRC-065.txt` (l. 312–314, 354–366 § `1.1`, 406–429 § `2.1`, 708).
  - Constat initial : supporté
  - Verdict final : supporté

- **A37** (L47) — *Affirmation* : Dans le même esprit, le bulletin `BSIF` de juillet 2026 recommande de définir les responsabilités sur tout le cycle de vie, de cartographier les dépendances internes et externes, et de traiter modèles, données, outils et agents comme des actifs technologiques contrôlés face aux mises à jour d'invites, de modèles, de sources de données, d'outils ou de services tiers.
  - *Sources* : `SRC-066.txt` (l. 143, 279, 291, 493).
  - Constat initial : imprécis — Le texte initial écrivait « étend cette exigence aux agents, invites... », laissant entendre que le bulletin de pratiques saines élargissait formellement la portée juridique de `E-23`, alors qu'il s'inscrit dans `B-13`/`E-21`/`B-10` et recommande de traiter modèles, données, outils et agents comme des actifs technologiques contrôlés. *Rectification apportée* : reformulation fidèle à `SRC-066.txt` à la ligne 47.
  - Verdict final : supporté

- **A38** (L47) — *Affirmation* : L'enregistrement d'énoncés signés sur le modèle `SCITT` (`RFC 9943`) permet de vérifier l'origine et la version de ces composants avant toute autorisation d'appel.
  - *Sources* : `SRC-044.txt` (l. 104–116, 498–514, 586–596).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 14 : Priorité 2 — coupe-circuits STAMP/STPA (L49)

- **A39** (L49) — *Affirmation* : En appliquant `STAMP/STPA` à l'IA, Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes et Stefano Vergani (`2025`) rappellent que les pertes de contrôle proviennent de boucles où une action de contrôle est omise, intempestive, tardive ou maintenue pendant une durée erronée.
  - *Sources* : `ch12-sources.md` `[9]`, `SRC-058.txt` (l. 1–11 : les cinq auteurs, décembre 2025; l. 412–417 : les quatre types d'actions de contrôle dangereuses).
  - Constat initial : supporté
  - Verdict final : supporté

- **A40** (L49) — *Affirmation* : À vitesse machine, l'opérateur humain intervient trop tard sans disjoncteurs déterministes hors modèle bornant coût, débit et récursion.
  - *Sources* : `SRC-058.txt` (l. 418–420, 863–868 : *speed mismatch*).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 15 : Priorité 3 — identités non humaines éphémères (L51)

- **A41** (L51) — *Affirmation* : Le bulletin `BSIF` de juillet 2026 cible les privilèges excessifs et justificatifs partagés ou hérités dans le *tool chaining*, et recommande des identités non humaines uniques, le moindre privilège, des permissions ciblées et des justificatifs à courte durée de vie en accès juste-à-temps.
  - *Sources* : `ch12-sources.md` `[13]`, `SRC-066.txt` (l. 355–360).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 16 : Priorité 4 — couloir borné en lecture seule (L53)

- **A42** (L53) — *Affirmation* : Le `BSIF` invite les institutions à traiter les sorties générées comme des entrées soumises à vérification plutôt que comme des décisions définitives, et à subordonner toute action à fort impact à des points d'approbation humaine explicites.
  - *Sources* : `ch12-sources.md` `[13]`, `SRC-066.txt` (l. 215–217, 289, 361).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 17 : Priorité 5 — dette cognitive/d'intention et relève (L55)

- **A43** (L55) — *Affirmation* : Dans une étude de mars 2026, Margaret-Anne Storey (Université de Victoria) analyse comment la génération assistée par IA réduit parfois la dette technique tout en accélérant l'accumulation de **dette cognitive et d'intention** (*cognitive and intent debt*) via « reddition cognitive » et perte de compréhension partagée et des contraintes métier initiales.
  - *Sources* : `ch12-sources.md` `[2]`, `SRC-040.txt` (l. 1–5, 19–38, 97–109, 154–173).
  - Constat initial : imprécis — Le verbe « démontre » surestimait la portée empirique d'un article conceptuel (`triple debt model`). *Rectification apportée* : remplacement par « analyse comment ».
  - Verdict final : supporté

- **A44** (L55) — *Affirmation* : Storey identifie cinq signes précoces concrets de la dette cognitive : résistance à modifier le système, résultats inattendus après retouche, intégration ralentie des recrues, perte de mémoire transactive et faible *bus factor*.
  - *Sources* : `SRC-040.txt` (l. 119–135 : *Diagnosing Cognitive Debt*).
  - Constat initial : imprécis — L'expression « de cette érosion » confondait dette cognitive et dette d'intention alors que les cinq indicateurs proviennent spécifiquement de la sous-section *Diagnosing Cognitive Debt*. *Rectification apportée* : précisé en « de la dette cognitive ».
  - Verdict final : supporté

- **A45** (L55) — *Affirmation* : Selon l'*AI Index Report 2026* de *Stanford HAI*, aux États-Unis, les effectifs des développeurs âgés de `22` à `25` ans ont chuté de près de `20 %` depuis `2024`, à rebours de la progression continue des développeurs plus chevronnés.
  - *Sources* : `ch12-sources.md` `[1]`, `SRC-008.txt` (l. 397–399), `registre/faits-empiriques.json` (`FACT-JUNIOR-DEV-CONTRACTION`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A46** (L55) — *Affirmation* : Maintenir des parcours d'instruction sans assistance sauvegarde la compréhension humaine et la capacité de repli manuel.
  - *Sources* : `SRC-040.txt` (l. 139–153, 250–263), `SRC-066.txt` (l. 495).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Paragraphe 18 : Priorité 6 — socle probatoire unifié (L57)

- **A47** (L57) — *Affirmation* : Un journal probatoire unique permet de couvrir l'inventaire et la validation `BSIF E-23` au `1er mai 2027` [12], les obligations documentaires de l'`EU AI Act` Annexe III au `2 décembre 2027` [11], `ACVM 31-103` au `1er octobre 2028` [15] et `BSIF B-15` à `fin 2028` [14].
  - *Sources* : `SRC-065.txt` (l. 177), `SRC-060.txt` (l. 3749–4015 : art. 11, 12, 18), `SRC-061.txt` (l. 1851), `SRC-069.txt` (l. 733), `SRC-067.txt` (l. 510, 727–730).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.2 — Figure 22 et séquence 90/180/360 jours (L59–L65)

- **A48** (L59–L65) — *Affirmation* : La Figure 22 et le paragraphe commenté inscrivent les six priorités dans une séquence en trois paliers (`1–90`, `91–180`, `181–360` jours) intégrant noyau `80/20`, `NHI`, télémétrie double couloir, constance multi-essais, exécution durable et agilité `PKI`/`ML-DSA`.
  - *Sources* : `registre/glossaire-termes.json` (définitions officielles), `SRC-050.txt`, `SRC-053.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.3 — Paragraphe 20 : frontière sans regret / conditionnel (L69)

- **A49** (L69) — *Affirmation* : L'arbitrage financier trace une frontière entre investissements sans regret (rentables dans tous les scénarios) et capacités conditionnelles activées sur seuils vérifiés.
  - *Sources* : `SRC-072.txt` (l. 86, 120, 146–154).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.3 — Paragraphe 21 : automatisation PKI / ACME et CAA (L71)

- **A50** (L71) — *Affirmation* : Le calendrier du *CA/Browser Forum* (`Ballot SC-081v3` / `SC081`, *Baseline Requirements* v2.3.1, sections `4.2.1` et `6.3.2`) abaisse validité et réutilisation à `200 jours` (`15 mars 2026`), puis `100 jours` (`15 mars 2027`), puis `47 jours` de validité et `10 jours` de réutilisation (`15 mars 2029`).
  - *Sources* : `SRC-053.txt` (l. 151, 189–205, 1317–1325, 2185–2200).
  - Constat initial : supporté
  - Verdict final : supporté

- **A51** (L71) — *Affirmation* : À compter du `15 mars 2027`, les autorités de certification doivent traiter obligatoirement les paramètres `CAA` liés à l'automatisation (`accounturi`, `validationmethods`, section `4.2.2.1.2`), rendant le renouvellement manuel obsolète face au protocole `ACME` (`RFC 8555`).
  - *Sources* : `SRC-053.txt` (l. 165, 201–202, 1369–1377 : section `4.2.2.1.2`, `Ballot SC098`, `RFC 8555`).
  - Constat initial : imprécis — Le texte initial citait uniquement les sections `4.2.1` et `6.3.2` de `SC-081v3` dans la phrase précédente sans mentionner la section `4.2.2.1.2` pour `accounturi`/`validationmethods`. *Rectification apportée* : ajout de `(section 4.2.2.1.2)` à la ligne 71.
  - Verdict final : supporté

### Section 12.3 — Paragraphe 22 : HNDL et théorème de Mosca (L73)

- **A52** (L73) — *Affirmation* : `NIST IR 8547` (version initiale publique de novembre 2024 et notice d'actualisation vers la version finale d'octobre 2026) et la feuille de route du `G7 CEG` (janvier 2026) mettent en garde contre l'attaque « capter maintenant, déchiffrer plus tard » (*harvest now, decrypt later*).
  - *Sources* : `ch12-sources.md` `[6, 7]`, `SRC-051.txt` (l. 8–18, 374–379, 794), `SRC-052.txt` (l. 6, 193–194).
  - Constat initial : supporté
  - Verdict final : supporté

- **A53** (L73) — *Affirmation* : `NIST IR 8547` formalise le théorème de Mosca (`X + Y > Z`), rappelant que l'intégration historique prend de `10` à `20` ans.
  - *Sources* : `SRC-051.txt` (l. 368–370, 785–791).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.3 — Paragraphe 23 : spécifications FIPS 203, FIPS 204, FIPS 205 et symétrie (L75)

- **A54** (L75) — *Affirmation* : `NIST FIPS 203` (août 2024) normalise `ML-KEM` (issu de `CRYSTALS-Kyber` sur `MLWE`) : `ML-KEM-512` (cat. `1`, `800 octets`, `768 octets`), `ML-KEM-768` (profil par défaut recommandé par le `NIST`, cat. `3`, `1 184 octets`, `1 088 octets`) et `ML-KEM-1024` (cat. `5`, `1 568 octets` chacun).
  - *Sources* : `ch12-sources.md` `[4]`, `SRC-049.txt` (l. 12, 35–42, 118–121, 1135–1138, 2324–2340, 2360–2371).
  - Constat initial : supporté
  - Verdict final : supporté

- **A55** (L75) — *Affirmation* : `NIST FIPS 204` formalise `ML-DSA` en trois gabarits : `ML-DSA-44` (cat. `2`, clé publique `1 312 octets`, signature `2 420 octets`), `ML-DSA-65` (cat. `3`, `1 952 octets` et `3 309 octets`, ~`52×` `64 octets`) et `ML-DSA-87` (cat. `5`, `2 592 octets` et `4 627 octets`, ~`72×` `64 octets`).
  - *Sources* : `SRC-050.txt` (l. 1296–1322 : `Table 1` et `Table 2`), `registre/faits-empiriques.json` (`FACT-PQC-SIGNATURE-SIZE`).
  - Constat initial : supporté
  - Verdict final : supporté

- **A56** (L75) — *Affirmation* : `NIST IR 8547` intègre `SLH-DSA` (`FIPS 205`, fondé sur le hachage sans état, issu de `SPHINCS+`), confirme que les primitives symétriques à au moins `128 bits` (`AES-128`, `AES-192`, `AES-256`, `SHA-256`) atteignent au moins la catégorie `1` sans nécessiter de migration post-quantique, et prévoit l'interdiction des normes symétriques `112 bits` en `2030`.
  - *Sources* : `SRC-051.txt` (l. 491–492, 627–629, 1189–1208, 1309–1322, 1431–1481).
  - Constat initial : imprécis — D'une part, la glose « offrant une assurance mathématique précieuse au cas où une faiblesse cryptanalytique affecterait les schémas à réseaux euclidiens » n'était pas formulée pour `SLH-DSA` dans `SRC-051.txt`; d'autre part, « au-delà de la catégorie 1 » contredisait `Table 1` et `§ 4.1.3` où `AES-128` correspond exactement à la catégorie `1` (*at least Category 1 security*). *Rectification apportée* : suppression de la glose non sourcée et correction en « atteignent au moins la catégorie `1` sans nécessiter de migration post-quantique, tandis que les normes symétriques à `112 bits` seront interdites en `2030` ».
  - Verdict final : supporté

- **A57** (L75) — *Affirmation* : Les catégories post-quantiques (`1` à `5`) se calibrent sur la résistance des primitives symétriques de référence plutôt que sur un simple comptage classique de bits, compte tenu des incertitudes sur le coût des futurs ordinateurs quantiques.
  - *Sources* : `SRC-051.txt` (l. 1173–1208).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.3 — Paragraphe 24 : calendrier NIST IR 8547 et G7 CEG (L77)

- **A58** (L77) — *Affirmation* : `NIST IR 8547` (objectif fédéral américain `2035` issu de `NSM-10`) prévoit la dépréciation après `2030` des algorithmes asymétriques de `112 bits` (`ECDSA`, `RSA`, `DH`), puis l'interdiction après `2035` de tous les schémas asymétriques vulnérables (`ECDSA`, `EdDSA`, `RSA`, `DH`), y compris à `128 bits` et plus.
  - *Sources* : `SRC-051.txt` (l. 1100–1116, `Table 2` l. 1244–1266, `Table 4` l. 1343–1370).
  - Constat initial : supporté
  - Verdict final : supporté

- **A59** (L77) — *Affirmation* : Le `G7 CEG` relève la convergence vers `2035`, recommande une approche duale fondée sur les risques priorisant les systèmes critiques dès `2030–2032`, structure la migration en six volets itératifs et rappelle à la note `6` la dépendance des plus petites institutions envers les feuilles de route infonuagiques.
  - *Sources* : `SRC-052.txt` (l. 58–73, 82–83, 87–155, 189–198, 216–218).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.3 — Paragraphe 25 : choc de taille multi-sauts et agilité SCITT (L79)

- **A60** (L79) — *Affirmation* : Dans une architecture multi-sauts, le passage des signatures de `64` à `3 309` (`ML-DSA-65`) ou `4 627 octets` (`ML-DSA-87`) [5], ou le mode hybride transitoire (`NIST IR 8547` § `3.2` [6]), affecte certificats, jetons, reçus `COSE_Sign1` `SCITT` [3], en-têtes `HTTP`, échanges `TLS`, `HSM` et journaux.
  - *Sources* : `SRC-044.txt` (l. 133–145, 928–936), `SRC-050.txt` (l. 1314–1321), `SRC-051.txt` (§ 2.2.1–2.2.5 l. 641–737, § 3.2 l. 893–951).
  - Constat initial : supporté
  - Verdict final : supporté

- **A61** (L79) — *Affirmation* : L'architecture `SCITT` (`RFC 9943`) intègre dès sa spécification (§ `9.6`) l'agilité cryptographique via les enveloppes `COSE` (`STD96`), fournissant la base d'une **crypto-agilité post-quantique** sans briser le format des journaux.
  - *Sources* : `SRC-044.txt` (§ `9.6` l. 1376–1380), `registre/glossaire-termes.json` (`crypto-agilité post-quantique`).
  - Constat initial : imprécis — `RFC 9943 § 9.6` spécifie la `Cryptographic Agility` générale via `STD96`, sans jamais mentionner le post-quantique. *Rectification apportée* : distinction explicite entre l'agilité cryptographique inscrite au § `9.6` et son application à la **crypto-agilité post-quantique**.
  - Verdict final : supporté

### Section 12.3 — Paragraphe 26 : liste sans regret vs capacités conditionnelles (L81)

- **A62** (L81) — *Affirmation* : Relèvent du sans regret immédiat l'inventaire et la cartographie des dépendances (`G7 CEG` [7]), `ACME` avant `15 mars 2027` et `15 mars 2029` [8], l'abstraction des enveloppes et bibliothèques [3, 6], le relèvement des plafonds (`3 309–4 627 octets` [5]) et l'encapsulation hybride `ML-KEM` sur flux exposés au captage différé [4, 6].
  - *Sources* : `SRC-044.txt`, `SRC-049.txt`, `SRC-050.txt`, `SRC-051.txt` (§ 2.2, 3.2.1, 4.2 l. 1623–1625), `SRC-052.txt` (l. 112–113), `SRC-053.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

- **A63** (L81) — *Affirmation* : Le report du remplacement anticipé de tous les `HSM` non critiques et du basculement généralisé vers des signatures hybrides ou PQC s'appuie sur les coûts et risques de complexité des modes hybrides (`NIST IR 8547` § `3.2` [6]) et sur l'approche progressive fondée sur les risques et la disponibilité des feuilles de route des fournisseurs (`G7 CEG` [7]).
  - *Sources* : `SRC-051.txt` (§ 3.2 l. 948–955), `SRC-052.txt` (l. 58–61, 70–72, 82–83).
  - Constat initial : imprécis — La version initiale attribuait indistinctement à `[6, 7]` les « risques de complexité des modes hybrides », alors que cet énoncé figure dans `NIST IR 8547 § 3.2` [6] tandis que le `G7 CEG` [7] justifie l'échelonnement par la criticité et les feuilles de route fournisseurs. *Rectification apportée* : attribution dissociée à `[6]` et `[7]` à la ligne 81.
  - Verdict final : supporté

### Section 12.4 — Paragraphe 27 : biais des coûts irrécupérables et dette d'intention (L85)

- **A64** (L85) — *Affirmation* : La **dette d'intention** analysée par Storey (`2026`) explique que sans consignation écrite des hypothèses et contraintes initiales, aucune équipe ne dispose d'un critère objectif pour déclarer qu'un système a dépassé son domaine de validité.
  - *Sources* : `ch12-sources.md` `[2]`, `SRC-040.txt` (l. 154–183, 266–267).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.4 — Paragraphe 28 : signaux avancés et coûts de transfert DAPP (L87)

- **A65** (L87) — *Affirmation* : Les étapes `5` à `7` de la méthode `DAPP` de Haasnoot *et al.* (`2019`) relient chaque trajectoire à un dispositif de surveillance actif gouverné par des **signaux avancés** (*signposts*) et des seuils de déclenchement (*trigger points*), opérationnalisés en portes budgétaires.
  - *Sources* : `ch12-sources.md` `[18]`, `SRC-072.txt` (l. 144–154 : *Step 5–7*, *signposts*, *trigger points*).
  - Constat initial : imprécis — Le texte initial attribuait « portes budgétaires » à `[18]`, alors que `SRC-072.txt` parle de *signposts* et *trigger points*. *Rectification apportée* : ajout explicite de *trigger points* `[18]` et caractérisation des « portes budgétaires » comme opérationnalisation organisationnelle.
  - Verdict final : supporté

- **A66** (L87) — *Affirmation* : Chaque signal doit être **précoce** (*timely*, préavis supérieur au délai d'exécution avant l'`ATP`) et **fiable** (*reliable*, minimisant fausses alertes et signaux manqués), en préférant des indicateurs intermédiaires peu bruités aux indicateurs normatifs liés aux événements extrêmes.
  - *Sources* : `SRC-072.txt` (l. 148, 239).
  - Constat initial : supporté
  - Verdict final : supporté

- **A67** (L87) — *Affirmation* : Haasnoot *et al.* soulignent la nécessité d'intégrer les **coûts de transfert** (*transfer costs*) dans le calcul économique des trajectoires.
  - *Sources* : `SRC-072.txt` (l. 134, 237).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.4 — Paragraphe 29 : couplage DAPP, STPA § 7 et exercices BSIF (L89)

- **A68** (L89) — *Affirmation* : La section `7` de Barrett *et al.* (`2025`) décrit comment la dégradation graduelle des systèmes de contrôle — complaisance, modèles mentaux périmés et défauts d'audit ou de gestion des changements — précède la perte de contrôle manifeste.
  - *Sources* : `ch12-sources.md` `[9]`, `SRC-058.txt` (§ `7`, l. 1030–1049).
  - Constat initial : imprécis — Le texte initial réduisait la section `7` de `SRC-058.txt` à la dégradation « des boucles de rétroaction », alors que § `7` traite plus largement de la dégradation des systèmes de contrôle (*complacency*, *outdated process models*, *audits*, *management of change*). *Rectification apportée* : alignement sur le libellé exact de la section `7`.
  - Verdict final : supporté

- **A69** (L89) — *Affirmation* : La gouvernance de surveillance `DAPP` définit qui surveille quel indicateur, selon quelle périodicité et pour quel décideur, et s'articule aux exercices de panne et de repli manuel préconisés par le bulletin `BSIF` de juillet 2026.
  - *Sources* : `SRC-072.txt` (l. 148 : *who should monitor what, when, and for whom*), `SRC-066.txt` (l. 495, 503).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.4 — Paragraphe 30 : clause statutaire de la Loi sur les banques (L91)

- **A70** (L91) — *Affirmation* : Aux termes de l'article `21` de la *Loi sur les banques* (`L.C. 1991, ch. 46`, à jour en octobre 2026), les banques et banques étrangères autorisées ne peuvent exercer leurs activités au Canada après le `30 juin 2033` sans prorogation ou révision parlementaire, au cœur de la fenêtre `2030–2035`.
  - *Sources* : `ch12-sources.md` `[16]`, `SRC-070.txt` (l. 3, 13 : `à jour 2026-10-29`, l. 1738–1752 : art. `21`), `SRC-052.txt` (l. 189–198), `registre/ancres-chronologiques.json` (`2033-06-30-LOIS-FINANCIERES-CANADA`).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.4 — Tableau 2 : cinq familles de signaux (L93–L99)

- **A71** (L95) — *Affirmation* : Ligne 1 (`Maturité PKI et profils PQC tiers`) : signaux `ML-KEM` [4] / `ML-DSA` [5], dépréciation asymétrique / interdiction symétrique des `112 bits` après `2030` [6], échéances `15 mars 2029` (`47 jours`) [8] et `2030–2032` [7], déblocage `ML-DSA`/`SLH-DSA` [6, 7].
  - *Sources* : `SRC-049.txt`, `SRC-050.txt`, `SRC-051.txt` (l. 1252–1263, 1352–1367, 1444–1446), `SRC-052.txt`, `SRC-053.txt`.
  - Constat initial : imprécis — L'expression « fin des `112 bits` après `2030` » confondait l'interdiction symétrique (`2030`) et la simple dépréciation asymétrique (`2030`, interdiction après `2035`). *Rectification apportée* : « dépréciation asymétrique / interdiction symétrique des `112 bits` après `2030` ».
  - Verdict final : supporté

- **A72** (L96) — *Affirmation* : Ligne 2 (`Concentration et coût de sortie SaaS`) : activation d'une fédération `SCITT` [3] via la réserve de coût de transfert [18].
  - *Sources* : `SRC-044.txt`, `SRC-072.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

- **A73** (L97) — *Affirmation* : Ligne 3 (`Convergence ou divergence normative`) : jalons `1er mai 2027` (`BSIF E-23` [12] / `AMF` [17]), `2 décembre 2027` (`EU AI Act` Annexe III [11]), `1er octobre 2028` (`ACVM 31-103` [15]), `fin 2028` (`BSIF B-15` [14]) et `30 juin 2033` (*Loi sur les banques* [16]).
  - *Sources* : `registre/ancres-chronologiques.json`, `SRC-061.txt`, `SRC-065.txt`, `SRC-067.txt`, `SRC-069.txt`, `SRC-070.txt`, `SRC-071.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

- **A74** (L98) — *Affirmation* : Ligne 4 (`Dérive des boucles de contrôle (STPA)`) : seuils d'approbation réflexe et coupe-circuits `STPA` [9].
  - *Sources* : `SRC-058.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

- **A75** (L99) — *Affirmation* : Ligne 5 (`Dette cognitive, d'intention et relève`) : ralentissement d'intégration, perte de mémoire transactive, faible *bus factor* [2] ou baisse du vivier junior [1].
  - *Sources* : `SRC-040.txt` (l. 124–135), `SRC-008.txt` (l. 397–399).
  - Constat initial : supporté
  - Verdict final : supporté

### Section 12.4 — Paragraphe 31 : liaison aux portes budgétaires (L101)

- **A76** (L101) — *Affirmation* : Provisionner les coûts de sortie et relier les signaux aux portes budgétaires permet de déclencher la bifurcation avant le point de rupture [18].
  - *Sources* : `SRC-072.txt` (l. 134, 148, 237).
  - Constat initial : supporté
  - Verdict final : supporté

### Encadré final — Trois arbitrages sans regret (L103–L107)

- **A77** (L105–L107) — *Affirmation* : Les trois arbitrages consolident les fondations des 90 jours (`STPA` [9], `NHI` [13], compétences [1, 2], `1er mai 2027` [12, 17], `2 décembre 2027` [11]), l'automatisation `ACME`/`PQC` (`100 j`/`47 j` [8], `ML-KEM` [4, 6], `ML-DSA-65/87` `3 309`/`4 627 octets`, `~52×`/`~72×` [5], `2030–2032`/`2035` [7]) et le pilotage `DAPP` [18] calé sur le `30 juin 2033` [16].
  - *Sources* : `SRC-008.txt`, `SRC-040.txt`, `SRC-049.txt` à `SRC-053.txt`, `SRC-058.txt`, `SRC-061.txt`, `SRC-065.txt`, `SRC-066.txt`, `SRC-070.txt`, `SRC-071.txt`, `SRC-072.txt`, `registre/faits-empiriques.json`, `registre/ancres-chronologiques.json`.
  - Constat initial : supporté
  - Verdict final : supporté

### Paragraphe 32 — Conclusion générale de l'ouvrage et renvoi aux annexes (L109)

- **A78** (L109) — *Affirmation* : La conclusion récapitule la thèse de l'ouvrage et renvoie à l'**Annexe A** (glossaire français-anglais), l'**Annexe B** (chronologie réglementaire et cryptographique `2026–2035`) et l'**Annexe C** (bibliométrie, bibliographie et bilan QA).
  - *Sources* : `registre/glossaire-termes.json`, `registre/ancres-chronologiques.json` (chronologie vérifiée de `2026` à `2035`).
  - Constat initial : supporté
  - Verdict final : supporté

---

## Contrôle différentiel post-G4 (barrière G2 après retouche stylistique)

- **Portée du contrôle différentiel** : Vérification intégrale des paragraphes modifiés `L41–L47` du manuscrit post-G4 (`Chapitre 12 - Decider sous incertitude profonde 2027-2035.md`), contrôle de cohérence typographique et de décalage de lignes sur le reste du chapitre (`L1–L39`, `L49–L111`), et validation déterministe par `verifie_manuscrit.py --unit ch12 --strict`.
- **Synthèse de la retouche G4** :
  - `L41` regroupe les deux échéances horizontales `2027` (`BSIF E-23` et `AMF` au `1er mai 2027`, `EU AI Act` Annexe III au `2 décembre 2027`) et leurs exigences d'ingénierie dès le jour `1` (`E-23` ; articles `11` et `12`).
  - `L43` isole les deux échéances sectorielles `2028` (`ACVM / CVMO` Norme canadienne `31-103` au `1er octobre 2028` et `BSIF B-15` fin d'exercice financier `2028`) et la règle de découplage hors invites. La mention de l'Annexe I européenne au `2 août 2028` (rattachée à `ch10` dans `ancres-chronologiques.json`) a été retirée de `L43`.
  - `L45` extrait en note méthodologique dédiée la justification `AO-01` sur `lautorite.qc.ca` (`HTTP 403 WAF`, statut F) et le renvoi au registre secondaire `AIBanks.ca` (`1er novembre 2026`).
  - `L47` reprend l'ancien `L45` (`AIBanks.ca` et bulletin `BSIF` de juillet `2026`), entraînant un décalage uniforme de `+2` lignes pour les repères ultérieurs `L49–L111` (anciens `L47–L109` du tableau `A36–A78`), sans modification factuelle.

### Bilan différentiel post-G4

- **Total d'affirmations différentielles vérifiées sur `L41–L47`** : `8` (`D01` à `D08`)
- **Écarts factuels introduits par G4** : `0` (aucune retouche requise sur le manuscrit)
- **Verdict final post-G4 — supportés** : `100 %` (`8/8` sur le bloc différentiel `L41–L47`; `100 %` sur l'ensemble du chapitre)
- **Imprécis résiduel** : `0`
- **Non supporté résiduel** : `0`

### Vérification ligne par ligne (`L41–L47`) contre `corpus_l_plus/*.txt`

- **D01** (`L41`, `BSIF E-23`) — *Affirmation* : La ligne directrice `E-23` révisée du `BSIF` entre en vigueur le `1er mai 2027` et soumet les modèles d'IA et d'AA à risque inhérent non négligeable à un inventaire d'entreprise, à une cotation du risque, à un responsable désigné, à une validation indépendante et à un suivi continu jusqu'à la mise hors service `[12]`.
  - *Preuve directe* : `SRC-065.txt` (`l. 46` titre `2027`; `l. 175–177` « `Le 1 mai 2027` »; `l. 248, 278` IA et AA; `l. 302, 658–697` cycle de vie et mise hors service; `l. 308–310, 412–429` inventaire à risque inhérent non négligeable; `l. 296–298, 432–448` cotation du risque; `l. 312–314, 498, 708` responsable de modèle; `l. 594–598` validation indépendante; `l. 314, 322, 660–677` suivi continu).
  - *Verdict* : `supporté`

- **D02** (`L41`, `AMF`) — *Affirmation* : Au Québec, la ligne directrice sur l'IA de l'`AMF` converge vers le `1er mai 2027` `[12, 17]`.
  - *Preuve directe* : `SRC-071.txt` (`l. 263–275` : `OSFI Guideline E-23` et `AMF guideline on AI (Quebec)` prennent toutes deux effet `May 1, 2027`).
  - *Verdict* : `supporté`

- **D03** (`L41`, `EU AI Act`) — *Affirmation* : Sept mois plus tard, en vertu de l'article `113` modifié de l'`EU AI Act` (Règlement `(UE) 2024/1689` actualisé par le Règlement `(UE) 2026/1744`), les systèmes à haut risque de l'Annexe III entrent sous le coup des obligations européennes le `2 décembre 2027` `[10, 11]`, et les articles `11` et `12` imposent une documentation technique tenue à jour avant la mise en service et l'enregistrement automatique des événements tout au long de la durée de vie du système `[10]`.
  - *Preuve directe* : `SRC-061.txt` (`l. 1–5`, `l. 1844–1852` art. 1er point `40)` modifiant l'article `113`, point `c)` `i)` : application à partir du `2 décembre 2027` pour l'annexe III; `l. 1045–1055` modification ciblée de l'art. `11 § 1` al. 2 sur le formulaire PME/SMC sans altérer l'alinéa 1); `SRC-060.txt` (`l. 3749–3753` art. `11 § 1` documentation technique établie avant mise sur le marché ou mise en service et tenue à jour; `l. 3777–3781` art. `12 § 1` enregistrement automatique des événements tout au long de la durée de vie).
  - *Verdict* : `supporté`

- **D04** (`L43`, `ACVM / CVMO NC 31-103`) — *Affirmation* : L'avis publié le `8 octobre 2026` par les `ACVM` / `CVMO` modifie la Norme canadienne `31-103` pour interdire les rétrofacturations de commissions dans la distribution de titres de fonds d'investissement émetteurs assujettis, avec entrée en vigueur prévue le `1er octobre 2028` (sous réserve des approbations ministérielles requises et hors titres acquis avant cette date) `[15]`.
  - *Preuve directe* : `SRC-069.txt` (`l. 2, 8–9, 15` avis du `8 octobre 2026` `ACVM` / `OSC`; `l. 17–24` interdiction des *chargebacks* sur titres de fonds d'investissement *reporting issuers*, approbations ministérielles et entrée en vigueur au `1er octobre 2028`; `l. 718–733` Annexe B art. `11.11(1)–(2)` et clause d'entrée en vigueur `October 1, 2028` hors titres achetés avant cette date).
  - *Verdict* : `supporté`

- **D05** (`L43`, `BSIF B-15`) — *Affirmation* : L'annexe `2-2` de la ligne directrice `B-15` du `BSIF` attend pour la fin de l'exercice financier `2028` la divulgation des émissions absolues brutes de portée `3`, incluant obligatoirement la catégorie `15` des prêts, investissements et portefeuilles d'assurance multirisque (hors assurance hypothécaire, le volet sur les actifs sous gestion demeurant à déterminer) avec référence au `GHG Protocol` et à la norme `PCAF` `[14]`.
  - *Preuve directe* : `SRC-067.txt` (`l. 496–502` Annexe `2-1` `GHG Protocol` et `PCAF`; `l. 636–640` Annexe `2-2` *Fiscal year-end for which implementation is expected*; `l. 667–730` élément `b) ii` : `Scope 3 absolute gross GHG emissions`, `Category 15`, *loans and investments*, *property and casualty insurance (excluding mortgage insurance)*, `GHG Protocol` `l. 685`, `PCAF` `l. 687`, horizon `2028` pour les quatre catégories d'institutions; `l. 675, 732–753` élément `b) iii` `AUM` marqué `TBD`).
  - *Verdict* : `supporté`

- **D06** (`L45`, Note méthodologique `AO-01`) — *Affirmation* : Le domaine `lautorite.qc.ca` demeurant bloqué (`HTTP 403 WAF`) à la date de gel, la prise d'effet au `1er mai 2027` de la ligne directrice sur l'IA de l'`AMF` est documentée par le registre secondaire ouvert `AIBanks.ca` (relevé du `1er novembre 2026`) en complément des textes fédéraux vérifiés `[17]`.
  - *Preuve directe* : `ch12-sources.md` (`l. 11` note `AO-01` statut F `HTTP 403 WAF`), `ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`), `SRC-071.txt` (`l. 6` *Figures as of November 1, 2026*; `l. 271–275` `AMF guideline on AI (Quebec)` effective `May 1, 2027`).
  - *Verdict* : `supporté`

- **D07** (`L47`, *Canadian Bank AI Index* `AIBanks.ca`) — *Affirmation* : `AIBanks.ca` compile `210` déploiements publics répartis dans `27` institutions actives sur `35` banques, coopératives et fintechs canadiennes; `21 %` touchent directement les clients et `13 %` opèrent à l'arrière-plan sur leurs comptes, tandis que la majorité porte sur des outils internes ou la recherche; seules `6` institutions sur `35` publient des principes d'IA responsable et `13` informent leurs clients du recours à l'IA ou aux décisions automatisées `[17]`.
  - *Preuve directe* : `SRC-071.txt` (`l. 1, 5–6, 101–117, 128, 169–175`).
  - *Verdict* : `supporté`

- **D08** (`L47`, Bulletin `BSIF` juillet `2026`) — *Affirmation* : Dès juillet `2026`, le bulletin du `BSIF` sur l'IA générative et agentique rappelle que le raisonnement et l'exécution autonomes accroissent la vitesse et l'ampleur des défaillances au regard des lignes directrices `B-13`, `B-10` et `E-21`, et recommande l'encadrement technique (*AI harnessing*), la maîtrise stricte des identités et des plans de repli manuel `[13]`.
  - *Preuve directe* : `SRC-066.txt` (`l. 46, 63–69` juillet `2026`, *autonomous reasoning and execution*, `B-13`, `E-21`, `B-10`; `l. 145, 287, 709` *AI harnessing*; `l. 355–360` identités non humaines uniques et justificatifs à courte durée de vie; `l. 495` *manual fallbacks*).
  - *Verdict* : `supporté`

### Contrôle typographique du reste du chapitre et validation `G1`

- **Typographie (`L1–L39`, `L49–L111`)** : Aucun écart factuel ni défaut typographique introduit par `G4` (`0` double espace, `0` tabulation, `0` espace manquant avant `:`, `%` ou `?`, `0` espace avant `;`, guillemets français `« »` conformes, formules `\(X\)`, `\(Y\)`, `\(Z\)` et `\(X + Y > Z\)` conformes à `L75`). Les renvois `A36–A78` conservent leur validité intégrale avec un décalage mécanique de `+2` lignes (`L49–L111` pour anciens `L47–L109`).
- **Barrière déterministe (`verifie_manuscrit.py --unit ch12 --strict`)** : Passée (`OK : Barriere deterministe G1 passee avec 0 erreur.`).
