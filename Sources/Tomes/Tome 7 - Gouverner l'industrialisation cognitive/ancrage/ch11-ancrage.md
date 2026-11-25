# Audit d'ancrage atomique — Chapitre 11 (`ch11`)

- **Unité vérifiée** : `manuscrit/04 - Partie IV/Chapitre 11 - Les sept pieges et l atrophie des competences.md`
- **Date de gel des faits** : 2 décembre 2026 | **Volume final (`v1.3`)** : `5 239` mots `G1` (`5 448` `split()`, cible `[4 784, 5 616]`)
- **Sources fermées consultées** : `sources/ch11-sources.md` (`21` sources `L+`, après retrait de l'ancienne source `SRC-004` et ajout `[11]` `SRC-053` / `[18]` `SRC-071`), `registre/ancres-chronologiques.json`, `registre/faits-empiriques.json`, `registre/glossaire-termes.json` et les textes intégraux `corpus_l_plus/SRC-*.txt` correspondants.
- **Affirmations atomiques vérifiables audités (`N`)** : `70`
- **Bilan initial (avant rectifications)** : `53` supportées, `16` imprécises, `1` non supportée
- **Rectifications effectuées au manuscrit** : `17` (`16` précisions factuelles ou attributions affinées, `1` suppression/réancrage d'une référence absente du corpus `L+`)
- **Verdict final — supportés : 70 (100 %)**
- **Verdict final — imprécis résiduels : 0**
- **Verdict final — non supportés résiduels : 0**

---

## Détail paragraphe par paragraphe

### Liminaire et scénario prospectif (lignes 1–11)

1. **A1 (lignes 5–9)** — Le scénario de panne simultanée au printemps 2032 d'une institution financière canadienne d'envergure est explicitement balisé comme `*Scénario illustratif prospectif.*` et désigné comme « cette institution fictive » à la ligne 11, sans assertion empirique historique.
   - Constat initial : supporté (fiction prospective explicitement balisée).
   - Source : texte du manuscrit (lignes 5, 11).
   - Verdict final : supporté

2. **A2 (ligne 11)** — Le chapitre s'articule autour de sept pièges internes de gouvernance, du mécanisme liant approbation réflexe et érosion de la relève, et des disjoncteurs organisationnels qui préservent le jugement humain.
   - Constat initial : supporté.
   - Source : structure des sections `11.1` à `11.4` du manuscrit.
   - Verdict final : supporté

---

### Section 11.1 — Sur-ingénierie initiale et engorgement de la deuxième ligne (lignes 13–27)

#### Paragraphe introductif (ligne 15)

3. **A3** — Les études de terrain et textes prudentiels mobilisés pour l'ouverture de la typologie (`[7, 8, 21, 15, 16]`) sont tous publiés au plus tard à la date de gel de décembre 2026 (`SAP 2026-22` 2 juin 2026, `MAP` déc. 2025/juin 2026, `Dhanorkar et al.` 3 juin 2026, `BSIF E-23` 11 sept. 2025, `Bulletin BSIF` juillet 2026).
   - Constat initial : supporté.
   - Source : `sources/ch11-sources.md` (`[7, 8, 21, 15, 16]`) et `corpus_l_plus/SRC-016.txt`, `SRC-027.txt`, `SRC-075.txt`, `SRC-065.txt`, `SRC-066.txt`.
   - Verdict final : supporté

4. **A4** — Cinq modes d'échec organisationnels sont traités dans ce chapitre, tandis que les pièges économique (`FinOps`) et cryptographique (`TLS`/post-quantique) sont nommés et renvoyés aux chapitres propriétaires (ch. 09 et ch. 12).
   - Constat initial : supporté.
   - Source : `registre/glossaire-termes.json` (`ch09`, `ch12`), `registre/ancres-chronologiques.json`, `registre/faits-empiriques.json`.
   - Verdict final : supporté

#### Piège 1 : Sur-ingénierie initiale (ligne 17)

5. **A5** — L'étude *Measuring Agents in Production* (`MAP`) de Pan *et al.* porte sur `20` études de cas et `306` répondants à l'enquête dont `86` systèmes déployés en production ou en phase pilote (`[8]`).
   - Constat initial : imprécis (le texte initial citait « 306 répondants et 20 études de cas » puis « 68 % des systèmes en production » sans distinguer le sous-échantillon filtré de 86 systèmes déployés). Rectifié au manuscrit.
   - Source : `corpus_l_plus/SRC-027.txt` (Abstract, § 1 p. 2, § 3.2 p. 3 : `surveyed 306 practitioners... filtered survey responses to 86 systems in production or pilot phases`).
   - Verdict final : supporté

6. **A6** — `68 %` des systèmes déployés exécutent au plus `10` étapes avant intervention humaine (`[8]`).
   - Constat initial : supporté.
   - Source : `corpus_l_plus/SRC-027.txt` (Abstract : `68% execute at most 10 steps before human intervention`; § 5.4 Fig. 7a : `41/60 = 68,3 %` pour `1–4` et `5–10` étapes) et `registre/faits-empiriques.json` (`FACT-MAP-STUDY`).
   - Verdict final : supporté

7. **A7** — `80 %` des cas étudiés (`16` sur `20`) utilisent des flux structurés fixes (`[8]`).
   - Constat initial : supporté.
   - Source : `corpus_l_plus/SRC-027.txt` (§ 5.4 : `Eighty percent (16/20) of case studies use structured workflows`) et `registre/faits-empiriques.json` (`FACT-MAP-STUDY`).
   - Verdict final : supporté

8. **A8** — Les équipes privilégient l'usage interne (`52 %` des usagers contre `40 %` de clients externes) afin de contenir le risque (`[8]`).
   - Constat initial : imprécis (l'énoncé qualitatif initial gagnait à être adossé aux proportions exactes relevées par `MAP`). Rectifié au manuscrit par ajout des proportions `52 %` vs `40 %`.
   - Source : `corpus_l_plus/SRC-027.txt` (§ 4.3, Fig. 3 : `Internal employees comprise 52% of users, external customers 40%, and non-human systems only 8%... deploying internally first to mitigate reliability and security risks`).
   - Verdict final : supporté

9. **A9** — La ligne directrice `E-23` du `BSIF` a une date d'entrée en vigueur fixée au `1er mai 2027` (`[15]`).
   - Constat initial : supporté.
   - Source : `corpus_l_plus/SRC-065.txt` (ligne 177 : `Date d'entrée en vigueur : Le 1 mai 2027`) et `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`).
   - Verdict final : supporté

10. **A10** — Les principes `2.2` et `2.3` de `E-23` commandent d'ajuster la rigueur de validation et de suivi à la cote de risque inhérent, allant jusqu'à autoriser une catégorie d'exemption encadrée pour les modèles à risque négligeable (`[15]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-065.txt` (§ C.2 Principe 2.2 lignes 432–447 et § C.3 Principe 2.3 lignes 456–470).
    - Verdict final : supporté

#### Piège 2 : Prolifération d'agents fantômes (ligne 19)

11. **A11** — Dans l'analyse de la Banque du Canada conduite par Chawla et Arnburg sur *Le Pouls des leaders d'entreprise* (décembre 2025), `70 %` des dirigeants déclarent utiliser l'IA chaque semaine à titre personnel au travail (`[7]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-016.txt` (p. 1–2, Chart 1 : `70% of respondents use AI for at least some time in a typical work week`).
    - Verdict final : supporté

12. **A12** — Seules `8 %` des firmes rapportent un usage significatif en exploitation, contre `21 %` un usage modéré et `29 %` un usage peu fréquent ou expérimental (`[7]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-016.txt` (p. 3, Chart 2 : `8% significant use`, `21% moderate use`, `29% infrequent use... experimentally or in pilot projects`).
    - Verdict final : supporté

13. **A13** — Au deuxième trimestre de 2026 (Statistique Canada, Tableau `33-10-1167-01`), `19,2 %` des entreprises au Canada ont utilisé l'IA pour produire des biens ou services sur les douze mois précédents (`[5]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-014.txt` (vecteur `v1865629154`, coord. `1.1.1`, valeur `19.2`, cote `A`).
    - Verdict final : supporté

14. **A14** — Dans le secteur *Finance et assurances* (T2 2026), `40,4 %` des entreprises ont utilisé l'IA, et parmi ces utilisateurs, `28,8 %` mobilisent des agents virtuels ou robots conversationnels et `22,7 %` des systèmes décisionnels automatisés (`[5]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-014.txt` (vecteurs `v1865629174` = `40.4` cote `C`, `v1865629188` = `28.8` cote `D`, `v1865629177` = `22.7` cote `D`).
    - Verdict final : supporté

15. **A15** — Au troisième trimestre de 2026 (Tableau `33-10-1207-01`), `25,2 %` des entreprises canadiennes prévoient recourir à l'IA dans les douze mois suivants, et `35,5 %` en finance et assurances (`[6]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-015.txt` (vecteurs `v1937048767` = `25.2` cote `A`, `v1937048788` = `35.5` cote `B`).
    - Verdict final : supporté

16. **A16** — Dans l'enquête de Dhanorkar, Passi et Vorvoreanu auprès de `17` développeurs expérimentés, des praticiens reconnaissent ignorer ce qu'il advient des données clients acheminées vers des outils tiers (`[21]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-075.txt` (Abstract, § 3.1 : `17 experienced developers`; § 4.1.1 lignes 308–309, `P01` et `P03`).
    - Verdict final : supporté

17. **A17** — Le bulletin de juillet 2026 du `BSIF` exhorte les institutions à proscrire l'utilisation de données sensibles dans des outils d'IA publics ou non approuvés (`[16]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-066.txt` (ligne 213 : `prohibit sensitive data use in public or unapproved AI tools`).
    - Verdict final : supporté

#### Piège 3 : Saturation de la deuxième ligne de défense (ligne 21)

18. **A18** — L'entrée en vigueur de `BSIF E-23` est fixée au `1er mai 2027` (`[15]`), parallèlement à la prise d'effet attendue au Québec de la ligne directrice sur l'IA de l'`AMF` (dont le texte primaire reste bloqué, comme signalé au chapitre 10).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-065.txt` (ligne 177), `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`) et `corpus_l_plus/SRC-071.txt` (lignes 271–275).
    - Verdict final : supporté

19. **A19** — Le principe `1.1` de `E-23` impose d'affecter à la gestion du risque de modélisation un personnel possédant les compétences et l'expérience nécessaires, particulièrement dans le domaine de l'IA (`[15]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-065.txt` (§ B.1 Principe 1.1, ligne 360).
    - Verdict final : supporté

#### Piège 4 : Dilution de responsabilité intra-groupe (ligne 23)

20. **A20** — Les conglomérats financiers canadiens réunissent des activités bancaires, d'assurance et de patrimoine soumises à des cloisons légales détaillées au chapitre 10.
    - Constat initial : supporté (renvoi interne conforme au chapitre propriétaire `ch10`).
    - Source : plan de l'ouvrage et `registre/ancres-chronologiques.json` (`ch10`).
    - Verdict final : supporté

21. **A21** — Dans les entretiens de Dhanorkar *et al.*, un participant (`P02`) rapporte utiliser des agents intégrés par une autre équipe sans pouvoir choisir le modèle, tandis qu'un autre (`P16`) déclare ignorer quel raisonnement ces agents mobilisent (`[21]`).
    - Constat initial : imprécis (le texte initial attribuait les deux propos à « un participant » et parlait des « consignes qui régissent son raisonnement »). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.1.1, lignes 298–307 : `P02` sur le choix du modèle par une autre équipe et `P16` sur `"not even sure what reasoning [agents] are using"`).
    - Verdict final : supporté

22. **A22** — Le bulletin du `BSIF` de juillet 2026 met en garde contre l'autonomie insuffisamment encadrée et les dépendances envers des tiers, en demandant de définir explicitement la propriété (*ownership*) sur tout le cycle de vie et de fixer des limites à l'autonomie (`[16]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-066.txt` (lignes 131, 141–143 : `define ownership across the AI lifecycle and establish limits on autonomy`).
    - Verdict final : supporté

23. **A23** — La ligne directrice `B-10` du `BSIF` impose de maîtriser la sous-traitance en cascade et le risque de concentration chez les tiers (`[17]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-068.txt` (§ 2.2.3 `Concentration risk`, § 2.2.4 `Subcontracting risk`, Principe 5).
    - Verdict final : supporté

#### Piège 5 : Veille décorative et illusion de maîtrise (ligne 25)

24. **A24** — Le bulletin du `BSIF` de juillet 2026 avertit que les lacunes de compréhension de la haute direction favorisent une confiance excessive envers les évaluations fournies par les vendeurs, limitant l'examen critique (`[16]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-066.txt` (ligne 131 : `gaps in senior management understanding can lead to over-reliance on vendor-provided assessments, limiting effective scrutiny of AI behaviour`).
    - Verdict final : supporté

25. **A25** — Genewein *et al.* rappellent avec le problème de l'évaluation (*Evaluation Problem*) qu'une forte pression d'optimisation exercée par des essaims d'agents épuise rapidement les bancs statiques et trouve des régimes comportementaux auxquels les évaluateurs automatisés restent aveugles (`[1]`).
    - Constat initial : imprécis (le texte disait « contournent les failles », légèrement interprétatif par rapport au vocabulaire exact de la section `5.5`). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-001.txt` (§ 5.5 `The Evaluation Problem` : `agent swarms can quickly exhaust static benchmarks... can find behavioral regimes to which the automated evaluator is mostly blind`).
    - Verdict final : supporté

26. **A26** — Margaret-Anne Storey montre comment la vitesse de génération engendre une dette cognitive et d'intention qui prive l'équipe de la compréhension partagée et des contraintes métier (`[9]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-040.txt` (lignes 18–38, 156–160).
    - Verdict final : supporté

#### Pièges 6 et 7 et transition (ligne 27)

27. **A27** — Le sixième piège (choc tarifaire et dérive du coût complet incluant réessais et reprises humaines) relève de la discipline `FinOps` couverte au chapitre 09.
    - Constat initial : supporté (renvoi au chapitre propriétaire `ch09`).
    - Source : `registre/glossaire-termes.json` (`Cost per Compliant Outcome (CPO)`, `ch09`).
    - Verdict final : supporté

28. **A28** — Le septième piège (collision cryptographique) associe le raccourcissement des certificats `TLS` publics à `100 jours` le `15 mars 2027` puis à `47 jours` le `15 mars 2029` à l'alourdissement des signatures post-quantiques, et renvoie au chapitre 12.
    - Constat initial : supporté.
    - Source : `registre/ancres-chronologiques.json` (`2027-03-15-TLS-100J`, `2029-03-15-TLS-47J`), `corpus_l_plus/SRC-053.txt` (§ 4.2.1, § 6.3.2), `registre/faits-empiriques.json` (`FACT-PQC-SIGNATURE-SIZE`).
    - Verdict final : supporté

---

### Section 11.2 — Le paradoxe de la supervision humaine et la requalification juridique (lignes 29–45)

#### Titre 11.2 et premier paragraphe (lignes 29–35)

29. **A29** — Plus l'automatisation prend en charge le traitement ordinaire et cantonne l'opérateur à un rôle de surveillance, plus la pratique directe sur laquelle s'appuie son jugement s'érode, si bien qu'en présence d'une erreur subtile ou d'un dysfonctionnement inattendu l'opérateur éloigné de l'exécution doit pourtant détecter l'anomalie et reprendre la main (`[20, 21]`).
    - Constat initial : non supporté (le titre et le paragraphe initiaux attribuaient ce paradoxe à **Bainbridge (référence retirée du manuscrit et absente du corpus)** sous l'appellation « ironies de l'automatisation », absente de `sources/ch11-sources.md` et de l'ensemble de `corpus_l_plus/`). Rectifié au manuscrit par suppression complète de la mention de Bainbridge (référence retirée du manuscrit et absente du corpus) / « ironies de l'automatisation » et réancrage sur `Chandra & Michel [20]` et `Dhanorkar et al. [21]`.
    - Source : `corpus_l_plus/SRC-074.txt` (§ 4.4, § 5.1) et `corpus_l_plus/SRC-075.txt` (§ 4.1.4, § 5.4).
    - Verdict final : supporté

#### Deuxième paragraphe — Modélisation expérimentale d'AL-Ali *et al.* (ligne 37)

30. **A30** — Publiée en août 2026 dans *Nature Scientific Reports* (évaluée par les pairs), l'étude de Maytha AL-Ali *et al.* modélise la collaboration humain-IA dans un simulateur physique de maintenance prédictive intégrant incertitude épistémique et pression de production, en précisant que ses conclusions exigent une validation auprès d'opérateurs humains réels (`[19]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-073.txt` (Published `20 August 2026`, Abstract et Limitations).
    - Verdict final : supporté

31. **A31** — Des probabilités mal calibrées et une confiance statique déstabilisent conjointement le couple humain-machine; le système non calibré échoue dans `12,4 %` des cas contre `0,8 %` pour l'architecture adaptative calibrée, et l'analyse de sensibilité identifie le biais cognitif humain sous pression (plutôt que la capacité brute du modèle) comme facteur dominant de défaillance (`[19]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-073.txt` (Abstract, Protocol comparison Table 1, Conclusions).
    - Verdict final : supporté

#### Troisième paragraphe — Étude qualitative de Dhanorkar *et al.* (ligne 39)

32. **A32** — Dans leur étude qualitative (*Microsoft Research*, juin 2026) auprès de `17` développeurs expérimentés, Shipi Dhanorkar, Samir Passi et Mihaela Vorvoreanu dégagent quatre temps de supervision : contrôle *a priori* (consignes et listes d'interdiction), co-planification préalable par lots vérifiables, suivi en temps réel et revue *post hoc* (`[21]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-075.txt` (p. 1–2, § 4.1.1–4.1.4, Appendix D).
    - Verdict final : supporté

33. **A33** — Le suivi en temps réel est presque absent : la plupart des praticiens ne lisent pas proactivement les traces de raisonnement en direct et réagissent seulement à des signaux indirects tels qu'une durée d'exécution anormalement longue (`[21]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.1.3, lignes 387–411).
    - Verdict final : supporté

34. **A34** — Faute d'effort amont suffisant en co-planification, l'essentiel du contrôle retombe sur une revue *post hoc* alourdie par une distance cognitive croissante face au volume élevé de code et de modifications produit par l'agent (`[21]`).
    - Constat initial : imprécis (l'énoncé initial évoquait un « volume de code ou d'analyse produit par un tiers algorithmique », élargissant au-delà des développeurs observés). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.1.2, § 4.1.4, lignes 453–460).
    - Verdict final : supporté

35. **A35** — Sous contrainte de temps, les développeurs recourent à quatre heuristiques *post hoc* d'économie d'attention : assimiler le plan de l'agent à son exécution réelle, déléguer la vérification aux tests automatisés, survoler visuellement les résumés (*eyeballing*) et s'en remettre à l'agent en domaine peu familier (`[21]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.2, Heuristics #1–#4, lignes 478–553).
    - Verdict final : supporté

36. **A36** — Un participant (`P10`) note que son agent se trompe environ `10 %` du temps dans ses explications tout en affichant une assurance qui masque l'erreur (`[21]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.1.3, lignes 405–406 : `"10% of the time it is wrong [about why it did something]. It is very confident, so you don't get to know."`).
    - Verdict final : supporté

#### Quatrième paragraphe — Reddition cognitive selon Storey / Shaw & Nave (ligne 41)

37. **A37** — Margaret-Anne Storey reprend la notion de reddition cognitive (*cognitive surrender*) formulée par Shaw et Nave : à la différence d'un délestage stratégique vers un outil ciblé tel qu'un vérificateur de types ou un analyseur statique, l'utilisateur adopte les sorties de l'IA avec un examen minimal, gonflant faussement sa confiance même lorsque l'IA a tort (`[9]`).
    - Constat initial : imprécis (paraphrasait librement « outil déterministe », « sorties probabilistes plausibles » et « l'agent a tort »). Rectifié au manuscrit pour coller aux exemples et à la définition de `SRC-040.txt`.
    - Source : `corpus_l_plus/SRC-040.txt` (p. 3, lignes 100–109).
    - Verdict final : supporté

#### Cinquième paragraphe — Droit québécois : Loi 25 et CAI (ligne 43)

38. **A38** — L'article `12.1` inséré par la *Loi 25* (LQ 2021, c. 25, pleinement en vigueur dès 2026) encadre toute décision fondée exclusivement sur un traitement automatisé : information au plus tard lors de la décision, communication sur demande des renseignements utilisés, des motifs et principaux facteurs et paramètres, du droit de rectification, et occasion de présenter ses observations à un membre du personnel « en mesure de réviser la décision » (`[13]`).
    - Constat initial : imprécis (ajoutait le qualificatif « employé qualifié » absent du libellé de l'article `12.1`). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-063.txt` (art. `12.1`, art. `175`) et `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`).
    - Verdict final : supporté

39. **A39** — Dans son *Rapport quinquennal 2026*, la `CAI` relève les risques liés à la mobilisation de modèles au fonctionnement opaque pour soutenir la prise de décision ou rendre des décisions entièrement automatisées, dans un environnement déjà marqué par une asymétrie informationnelle et le recours des personnes concernées à des raccourcis décisionnels (`[14]`).
    - Constat initial : imprécis (employait « outils opaques » et « raccourcis cognitifs » en fusionnant deux constats sans respecter la terminologie exacte du rapport). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-064.txt` (p. 4 sur les réseaux opaques et décisions automatisées; § 2.1.1.3.1 sur l'asymétrie informationnelle et les « raccourcis décisionnels »).
    - Verdict final : supporté

40. **A40** — Un manquement aux obligations de l'article `12.1` ouvre la voie aux sanctions administratives pécuniaires de l'article `90.1`, paragraphe `5`, plafonnées à `10 000 000 $ CA` ou `2 %` du chiffre d'affaires mondial (art. `90.12`), sans compter les amendes pénales pouvant atteindre `25 000 000 $ CA` ou `4 %` du chiffre d'affaires mondial pour les infractions visées à l'article `91` (notamment utilisation de renseignements personnels en contravention à la loi ou non-respect d'une ordonnance de la Commission) (`[13, 14]`).
    - Constat initial : imprécis (la formulation initiale pouvait laisser croire qu'une violation de l'art. `12.1` emportait directement poursuite pénale sous l'art. `91`, alors que l'art. `91` énumère des infractions spécifiques distinctes de l'art. `90.1(5°)`). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-063.txt` (art. `90.1(5°)`, `90.12`, `91`) et `corpus_l_plus/SRC-064.txt` (p. 298+).
    - Verdict final : supporté

#### Sixième paragraphe — Droit européen et BSIF (ligne 45)

41. **A41** — L'article `14` du Règlement (UE) 2024/1689 (`EU AI Act`) exige un contrôle effectif par des personnes physiques conscientes du « biais d'automatisation » (art. `14(4)(b)`), capables d'ignorer ou d'inverser la sortie (`14(4)(d)`) et d'arrêter le système (`14(4)(e)`), et l'article `26(2)` impose de confier ce contrôle à des personnes disposant « des compétences, de la formation et de l'autorité nécessaires ainsi que du soutien nécessaire » (`[12]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-060.txt` (art. `14(1)`, `14(4)(b)(d)(e)`, art. `26(2)`).
    - Verdict final : supporté

42. **A42** — Le bulletin du `BSIF` de juillet 2026 demande de traiter les sorties d'IA comme des intrants et non comme des décisions définitives, avec une imputabilité humaine documentée sur les décisions importantes (`[16]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-066.txt` (lignes 215–217).
    - Verdict final : supporté

43. **A43** — Dhanorkar *et al.* relèvent une tension frontale entre ces mandats légaux de vigilance effective et les heuristiques adoptées sous pression temporelle (`[21]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 5.4, lignes 638–644).
    - Verdict final : supporté

---

### Section 11.3 — La crise de la relève (lignes 47–61)

#### Paragraphe introductif (lignes 49–51)

44. **A44** — Cadrage analytique décrivant l'apprentissage professionnel sur les tâches d'entrée de carrière avant sa mise à l'épreuve statistique et empirique aux paragraphes suivants.
    - Constat initial : supporté.
    - Source : articulation interne des sections `11.3` et sources `[2, 7, 20]`.
    - Verdict final : supporté

#### Deuxième paragraphe — Stanford HAI AI Index Report 2026 (ligne 53)

45. **A45** — Selon l'*AI Index Report 2026* de Stanford HAI, l'emploi des développeurs logiciels américains âgés de `22 à 25 ans` s'est contracté de près de `20 %` depuis `2024`, alors même que les effectifs des développeurs plus âgés ont poursuivi leur croissance (`[2]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-008.txt` (p. 10–11, p. 222) et `registre/faits-empiriques.json` (`FACT-JUNIOR-DEV-CONTRACTION`).
    - Verdict final : supporté

46. **A46** — En neutralisant les effets propres aux types d'entreprises, l'emploi des travailleurs de `22 à 25 ans` dans les métiers les plus exposés à l'IA affiche un recul relatif d'environ `16 %` par rapport aux moins exposés (`[2]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-008.txt` (p. 222 : `fallen roughly 16% relative to the least-exposed, after controlling for firm-type effects`).
    - Verdict final : supporté

47. **A47** — Parallèlement, les inscriptions de premier cycle en informatique (universités de quatre ans) ont baissé de `11 %` entre `2024` et `2025` (`[2]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-008.txt` (`Between 2024 and 2025, enrollment in CS as an undergraduate major in four-year universities declined 11%`).
    - Verdict final : supporté

48. **A48** — Le rapport documente le banc *Finance Agent*, élaboré avec des chercheurs de Stanford, une banque d'importance systémique mondiale et des experts du secteur pour évaluer des agents sur des tâches typiques d'analystes financiers débutants (`[2]`).
    - Constat initial : imprécis (paraphrasait « une grande banque internationale » au lieu de « une banque d'importance systémique mondiale »). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-008.txt` (§ 2.5 : `Developed in collaboration with Stanford researchers, a Global Systemically Important Bank, and industry experts, Finance Agent evaluates AI agents' ability to perform tasks typical of an entry-level financial analyst`).
    - Verdict final : supporté

#### Troisième paragraphe — Banque du Canada SAP 2026-22 (ligne 55)

49. **A49** — Sur l'horizon de douze mois, `11 %` des firmes canadiennes interrogées prévoient une baisse d'effectifs contre `8 %` une hausse (`[7]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-016.txt` (p. 6, lignes 314–315).
    - Verdict final : supporté

50. **A50** — Sur l'horizon à trois ans, `18 %` des entreprises canadiennes anticipent une réduction de leur embauche attribuable à l'IA contre `9 %` une hausse, dégageant un solde net négatif (`[7]`).
    - Constat initial : imprécis (qualifiait de « diminution nette d'embauche » la part individuelle de `18 %` au lieu du solde net agrégé `18 % vs 9 %`). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-016.txt` (p. 2, p. 6 : `18% of firms anticipate hiring less staff because of AI while 9% of firms anticipate hiring more staff`).
    - Verdict final : supporté

51. **A51** — Chez les entreprises de `20 employés et plus` (`SML`), la part prévoyant des réductions double presque entre `2026` (`10 %`) et les trois années suivantes (`21 %`), et le secteur de la finance, des assurances, de l'immobilier et de la location projette une contraction nette de l'emploi aux deux horizons (`[7]`).
    - Constat initial : imprécis (omettait « et de la location » dans l'intitulé complet du secteur). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-016.txt` (p. 6–7 et note 7 : `finance, insurance, real estate, rental and leasing firms expect net employment decreases at the 12-month and 3-year horizons`).
    - Verdict final : supporté

52. **A52** — Les firmes qui n'adoptent pas encore l'IA citent le manque de personnel qualifié parmi leurs principaux obstacles opérationnels (`[7]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-016.txt` (p. 4, Chart 3 : `Lack of skilled staff`).
    - Verdict final : supporté

#### Quatrième paragraphe — Productivité immédiate et paradoxe automatisation–augmentation (ligne 57)

53. **A53** — Dans leur essai randomisé publié dans *Science* auprès de `453` professionnels diplômés, Shakked Noy et Whitney Zhang observent que ChatGPT réduit le temps moyen de rédaction de `40 %` et relève la qualité évaluée de `18 %`, tout en resserrant l'écart au profit des moins performants au départ (`[3]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-009.txt` (Abstract et p. 5).
    - Verdict final : supporté

54. **A54** — Dans leurs trois expérimentations randomisées totalisant `4 867` développeurs, Cui *et al.* mesurent une hausse de `26,08 %` des tâches complétées (`pull requests`), particulièrement marquée chez les recrues à faible ancienneté, avec `+13,55 %` de mises à jour de code (`commits`) et `+38,38 %` de compilations hebdomadaires (`builds`) (`[4]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-010.txt` (Abstract, § 1, § 4.2 Table 3, § 5).
    - Verdict final : supporté

55. **A55** — Cui *et al.* soulignent qu'une lecture moins optimiste de la hausse des compilations pourrait traduire davantage de codage par essai et erreur, tout en précisant que l'évolution du taux de réussite des compilations n'appuie faiblement cette hypothèse que dans l'essai Accenture (`[4]`).
    - Constat initial : imprécis (l'incise sur les compilations par essai et erreur était attribuée à tort à Chandra & Michel `[20]` et sans la nuance empirique de Cui *et al.*). Rectifié au manuscrit avec réattribution exacte à `[4]`.
    - Source : `corpus_l_plus/SRC-010.txt` (§ 4.2, p. 12–13, lignes 755–771).
    - Verdict final : supporté

56. **A56** — Dans leur revue de littérature présentée en mai 2026, Amit Chandra et Sylvie Michel rappellent à la suite de Raisch et Krakowski le paradoxe automatisation–augmentation : privés de la pratique directe en profondeur (*deep practice*), les juniors produisent vite sans acquérir la maîtrise architecturale et l'expertise de débogage, tandis que les seniors risquent l'atrophie de leurs compétences s'ils délèguent excessivement l'exécution (`[20]`).
    - Constat initial : imprécis (décrivait une revue achevée incluant l'interprétation des compilations de `[4]`). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-074.txt` (§ 4.4 p. 12, § 5.1, § 5.4, § 5.5).
    - Verdict final : supporté

#### Cinquième paragraphe — Mémoire transactive, facteur d'autobus et barrière d'abstraction (ligne 59)

57. **A57** — Margaret-Anne Storey analyse la perte de **mémoire transactive** et la chute du **facteur d'autobus** (*low bus factor*) lorsque le manque de compréhension partagée concentre la maîtrise réelle du système entre les mains d'un cercle étroit (`[9]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-040.txt` (p. 4, `Diagnosing Cognitive Debt` : `Loss of transactive memory`, `Low bus factor`).
    - Verdict final : supporté

58. **A58** — Genewein *et al.* rappellent avec l'hypothèse de la « barrière d'abstraction » que les modèles actuels reposent sur des concepts abstraits issus de l'expérience humaine du réel (`[1]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-001.txt` (§ 5.5, `The abstraction barrier`).
    - Verdict final : supporté

#### Sixième paragraphe — Exigences de résilience et plans de repli (ligne 61)

59. **A59** — L'article `15`, paragraphe `4`, de l'`EU AI Act` exige que les systèmes à haut risque fassent preuve de résilience face aux erreurs ou défaillances au moyen de mesures techniques et organisationnelles incluant des plans de sauvegarde (`[12]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-060.txt` (art. `15(4)`).
    - Verdict final : supporté

60. **A60** — Le bulletin de juillet 2026 du `BSIF` demande aux institutions financières de tester des scénarios de panne ou d'indisponibilité de l'IA et d'établir des **solutions de repli manuel** et mesures de continuité (`[16]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-066.txt` (l. 117 : `test AI failure and outage scenarios and establish manual fallbacks and continuity measures`).
    - Verdict final : supporté

61. **A61** — La ligne directrice `B-10` exige des plans de sortie et de contingence face au risque de concentration chez les tiers fournisseurs (`[17]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-068.txt` (§ 2.2.3, § 2.3.5 `Contingency and exit strategy / planning`).
    - Verdict final : supporté

---

### Section 11.4, Figure 20, Tableau et Arbitrages (lignes 57–97)

#### Paragraphe introductif et Parade 1 (lignes 65–71)

62. **A62** — Le couloir rapide en lecture seule sans droit de mutation (articulé aux ch. 01, ch. 04 et à la règle du maillon le plus élevé du liminaire) matérialise l'approche proportionnée et l'exemption encadrée des principes `2.2` et `2.3` de `BSIF E-23` (échéance `1er mai 2027`, `[15]`) ainsi que le déploiement interne maîtrisé observé dans `MAP` (`[8]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-065.txt`, `corpus_l_plus/SRC-027.txt`, `registre/glossaire-termes.json` (`00-liminaire`, `ch04`).
    - Verdict final : supporté

#### Parade 2 (ligne 73)

63. **A63** — L'obligation d'un seul responsable humain nommé par identité non humaine (ch. 07) met en œuvre l'exigence de propriété sur le cycle de vie du bulletin `BSIF` de juillet 2026 (`[16]`), l'autorité du contrôleur humain prévue à l'article `26(2)` et le pouvoir d'arrêt d'urgence de l'article `14(4)(e)` de l'`EU AI Act` (`[12]`), tout en encadrant l'énoncé d'intention face à la dérive comportementale analysée par Storey (`[9]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-066.txt`, `corpus_l_plus/SRC-060.txt`, `corpus_l_plus/SRC-040.txt`, `registre/glossaire-termes.json` (`ch07`).
    - Verdict final : supporté

#### Parade 3 (ligne 75)

64. **A64** — L'injection de cas témoins à l'aveugle, le masquage temporaire de la recommandation et le suivi du taux d'infirmation répondent au besoin de contrer les heuristiques de survol et de préserver l'accès épistémique et la conscience situationnelle soulignés par Dhanorkar *et al.* (`[21]`), tout en transposant la surveillance des biais sous pression et le recalibrage sur les écarts observés modélisés par AL-Ali *et al.* (`[19]`).
    - Constat initial : imprécis (prêtait à Dhanorkar *et al.* `[21]` une discussion des fonctions de forçage cognitif alors qu'ils ne citent Buçinca *et al.* qu'en revue bibliographique p. 3). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.2, § 5.4) et `corpus_l_plus/SRC-073.txt` (Abstract, Sensitivity Analysis, Practical deployment guidelines).
    - Verdict final : supporté

65. **A65** — Pour les actes pivot irréversibles, l'approbation asynchrone hors bande de type `CIBA` (`[10]`, détaillée au chapitre 07) dissocie le dispositif d'exécution de celui d'authentification et de consentement.
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-045.txt` (Abstract, § 5, § 7.1.2) et `sources/ch11-sources.md` (`[10]`).
    - Verdict final : supporté

#### Parade 4 (ligne 77)

66. **A66** — Les quotas manuels formateurs et exercices de bascule répondent au risque de déqualification malgré les gains à court terme mesurés par Noy et Zhang (`[3]`) et Cui *et al.* (`[4]`) selon l'analyse de Chandra et Michel (`[20]`), s'inspirent des parcours collectifs (*walkthroughs*) recommandés par Storey (`[9]`) et matérialisent les tests de repli manuel et de sortie de tiers demandés par le `BSIF` (`[16, 17]`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-009.txt`, `SRC-010.txt`, `SRC-074.txt`, `SRC-040.txt` (ligne 140), `SRC-066.txt` l. 117), `SRC-068.txt` (§ 2.3.4–2.3.5).
    - Verdict final : supporté

#### Figure 20 (lignes 79–88)

67. **A67** — La Figure 20 (`Fig-20.svg`) et son commentaire (`E1` à `E5` et disjoncteurs `D1` à `D3`) synthétisent sans ajout factuel autonome les mécanismes et parades établis aux sections `11.1` à `11.4`.
    - Constat initial : supporté.
    - Source : texte des sections `11.1`–`11.4` et diagramme référencé `../../diagrammes/rendus/Fig-20.svg`.
    - Verdict final : supporté

#### Tableau des sept pièges (lignes 77–89)

68. **A68** — Les entrées des pièges `1, 2, 3, 5, 6, 7` reprennent exactement les indicateurs, seuils et références vérifiés dans le corps du chapitre (`BSIF E-23 [15]` et `1er mai 2027`, `70 %` `[7]`, pertes de maîtrise de données `[21]`, ÉFVP `[14]`, `BSIF [16]`, dette cognitive/intention `[9]`, `FinOps` ch. 09, `TLS` `100 j` `15 mars 2027` / `47 j` `15 mars 2029` et PQC ch. 12).
    - Constat initial : supporté.
    - Source : recoupement des lignes 17–27 et des sources `[7, 9, 14, 21, 15, 16]` et `registre/ancres-chronologiques.json`.
    - Verdict final : supporté

69. **A69** — L'entrée du piège 4 (dilution intra-groupe) dans le tableau caractérise des agents boîtes noires intégrés par une autre équipe et utilisés sans maîtrise du modèle ni propriétaire clair (`[21]`).
    - Constat initial : imprécis (mentionnait une utilisation « en filiale », absente de `SRC-075.txt`). Rectifié au manuscrit.
    - Source : `corpus_l_plus/SRC-075.txt` (§ 4.1.1, `P02` et `P16`).
    - Verdict final : supporté

#### Arbitrages sans regret et conclusion (lignes 102–111)

70. **A70** — Les trois arbitrages sans regret et la transition vers le chapitre 12 reprennent fidèlement l'échéance du `1er mai 2027` (`BSIF E-23 [15]`), l'article `12.1` de la *Loi 25* (`[13]`), l'article `14` de l'`EU AI Act` (`[12]`), les attentes de résilience du `BSIF` (`[16, 17]`) et le périmètre `DAPP` du chapitre 12 (`registre/glossaire-termes.json`).
    - Constat initial : supporté.
    - Source : `corpus_l_plus/SRC-065.txt`, `SRC-063.txt`, `SRC-060.txt`, `SRC-066.txt`, `SRC-068.txt` et `registre/glossaire-termes.json` (`ch12`).
    - Verdict final : supporté

---

## Contrôle différentiel post-G4

- **Périmètre vérifié** : retouches stylistiques `G4` sur `manuscrit/04 - Partie IV/Chapitre 11 - Les sept pieges et l atrophie des competences.md` — lignes `L11`, `L17`, `L27`, `L37`, `L43–L45`, `L53–L61`, section `11.4` complète (`L65–L112`, incluant le nouveau tableau des quatre parades `L81–L88`, la figure `Fig-20` `L90–L96` et le tableau des sept pièges `L98–L110`), et arbitrages `L116–L118`.
- **Sources primaires `corpus_l_plus/` directement contre-vérifiées** : `SRC-065.txt` (`BSIF E-23 [15]`), `SRC-066.txt` (`Bulletin BSIF juillet 2026 [16]`), `SRC-068.txt` (`BSIF B-10 [17]`), `SRC-063.txt` (`Loi 25 [13]`), `SRC-064.txt` (`CAI Rapport quinquennal 2026 [14]`), `SRC-060.txt` (`EU AI Act [12]`), `SRC-045.txt` (`OIDC CIBA 1.0 [10]`), `SRC-075.txt` (`Dhanorkar et al. [21]`), `SRC-073.txt` (`AL-Ali et al. [19]`), `SRC-074.txt` (`Chandra & Michel [20]`), `SRC-040.txt` (`Storey [9]`), `SRC-008.txt` (`Stanford HAI 2026 [2]`), `SRC-009.txt` (`Noy & Zhang [3]`), `SRC-010.txt` (`Cui et al. [4]`), `SRC-016.txt` (`Banque du Canada SAP 2026-22 [7]`), `SRC-027.txt` (`MAP [8]`), `SRC-001.txt` (`Genewein et al. [1]`), `SRC-053.txt` (`CA/Browser Forum TLS`).
- **Points différentiels validés sans écart** :
  - `L11, L17, L27, L37, L45, L55–L61, L65–L71, L75, L83–L88, L90–L112, L116–L118` : chiffres, dates (`1er mai 2027` `SRC-065.txt` L177; `15 mars 2027` `100 j` / `15 mars 2029` `47 j` `SRC-053.txt` L200/L205; `août 2026`, `12,4 %` vs `0,8 %` et biais sous pression `SRC-073.txt` Table 1/L357/L404/L416), citations légales (`Loi 25` art. `12.1`, `90.1(5°)`, `90.12`, `91` `SRC-063.txt`; `EU AI Act` art. `14(1)`, `14(4)(b)(d)(e)`, `15(4)`, `26(2)` `SRC-060.txt`), flux asynchrone hors bande signé/lié `CIBA` (`SRC-045.txt` § 1, § 5, § 7.1, § 7.1.1, § 14), et constats empiriques (`SRC-075.txt` L298–309, L405–406 `10 %`, § 4.2, § 5.4; `SRC-027.txt` `20`/`306`/`86`/`68 %`/`80 %`/`52 %`/`40 %`) entièrement fidèles aux sources intégrales.
- **Écarts différentiels détectés et rectifiés au manuscrit (`6` micro-rectifications)** :
  1. `L43` (`Loi 25`, art. `12.1`) : remplacement de « motifs et variables déterminantes » par « motifs, les principaux facteurs et paramètres retenus pour le résultat », fidèle au libellé légal de l'article `12.1(2°)` (`SRC-063.txt` L1549–1550) tout en évitant toute collision n-gramme `[CA-03]`.
  2. `L53` (`Stanford HAI 2026`, p. 222) : rétablissement de « types d'entreprises » (« effets propres aux types d'entreprises ») pour traduire fidèlement *firm-type effects* (`SRC-008.txt` L16371) sans le confondre avec des effets fixes d'entreprise.
  3. `L73` (`Parade 2` — `EU AI Act`) : resserrement syntaxique pour circonscrire l'attribution à `[12]` (`art. 26(2)` et `14(4)(e)`) à l'autorité du contrôleur et au pouvoir d'arrêt, sans placer l'énoncé d'intention (`[9]`), la validation des changements de modèle/serveur d'outils et le cloisonnement entre filiales sous le mandat de ces articles (`SRC-060.txt` L3878–3879, L4254–4255).
  4. `L77` (`Parade 4` — `Chandra & Michel`) : remplacement de « modèles mentaux `[20]` » par « expertise pratique `[20]` », conformément à `SRC-074.txt` (L630–633 : *deep practice*, *genuine expertise*, *skill atrophy*), réservant la terminologie *mental models* à Storey (`[9]`, `SRC-040.txt`).
  5. `L85` (nouveau tableau, rangée `3`) : précision de « cas témoins et taux d'infirmation contre biais et survol `[19, 21]` » afin de ne pas attribuer l'invention des cas témoins ou du taux d'infirmation à AL-Ali *et al.* (`[19]`, `SRC-073.txt`) ni à Dhanorkar *et al.* (`[21]`, `SRC-075.txt`), qui documentent les biais sous pression et les heuristiques de survol que ce contrôle combat.
  6. `L86` (nouveau tableau, rangée `4`) : précision de « parcours juniors inspirés des *walkthroughs* `[9]` et *game days* semestriels éprouvant repli manuel et sortie de tiers (`BSIF` `[16, 17]`) », distinguant l'adaptation junior des *system walkthroughs* d'équipe de Storey (`SRC-040.txt` L140) et rattachant `[16, 17]` exclusivement aux tests de repli manuel (`SRC-066.txt` l. 117) et de sortie de tiers (`SRC-068.txt` § 2.3.4–2.3.5) plutôt qu'à la cadence semestrielle ou au terme *game days*.
- **Verdict différentiel post-G4** :
  - **Supportés : `100 %`**
  - **Imprécis résiduels : `0`**
  - **Non supportés résiduels : `0`**

---

## Contrôle différentiel post-lissage G5

- **Périmètre contrôlé** : `git diff HEAD` (depuis `fe6e945`) sur [Chapitre 11 - Les sept pieges et l atrophie des competences.md](../manuscrit/04%20-%20Partie%20IV/Chapitre%2011%20-%20Les%20sept%20pieges%20et%20l%20atrophie%20des%20competences.md) — `40` lignes modifiées (`9` lignes de retrait exclusif de rétro-apostrophes vérifiées pour identifiants et acronymes, `31` lignes reformulées, scindées ou fusionnées contrôlées mot pour mot contre [ch11-sources.md](../sources/ch11-sources.md) et `corpus_l_plus/SRC-*.txt`, `2` tableaux intacts, `85` appels `[n]` et `96` occurrences de renvois vérifiés intacts, `5 013` mots).
- **Rectifications effectuées au manuscrit (`8` paragraphes)** :
  1. `L17` : rétablissement de « `80 %` des cas étudiés (`16` sur `20`) » (`SRC-027.txt` `§ 5.4`), évitant d'attribuer ce taux aux `86` systèmes déployés de l'enquête.
  2. `L27` : rétablissement de « de la compréhension et de la mémoire des contraintes métier » (`SRC-040.txt`).
  3. `L45` : rétablissement du délai statutaire « au plus tard lors de la décision » et du qualificatif « principaux » (« principaux facteurs et paramètres ») à l'article `12.1` (`SRC-063.txt`).
  4. `L51` : rétablissement de la portée « pour les décisions importantes » sur l'imputabilité humaine documentée (`SRC-066.txt` `l. 217`).
  5. `L61` : levée d'ambiguïté sur Cui *et al.* : « n'appuie faiblement l'hypothèse d'un codage par essai et erreur que dans l'essai Accenture » (`SRC-010.txt` `l. 769–771`).
  6. `L63` : rétablissement de « la génération de code ou de dossiers » pour la perte de mémoire transactive (`SRC-040.txt`).
  7. `L69` : alignement de l'article `15(4)` de l'*EU AI Act* sur l'exigence de « résilience aux défaillances, au besoin par des plans de sauvegarde » (`SRC-060.txt`) et du bulletin `BSIF` sur « tester des scénarios de panne d'IA » (`SRC-066.txt` `l. 495`).
  8. `L77` : rétablissement de l'attribution exacte des renvois `[19, 21]` aux heuristiques de survol et biais sous pression combattus par le mécanisme de dossiers témoins, sans prêter l'injection de cas témoins ni la suspension sur taux d'infirmation à `[19, 21]` (`SRC-073.txt`, `SRC-075.txt`).
- **Certification différentielle post-lissage G5** :
  - Verdict différentiel : **100 % `supporté`**
  - Imprécis résiduel : `0`
  - Non supporté résiduel : `0`

---

## Réindexation différentielle post-audit v1.3 (2 décembre 2026)

- **Périmètre `v1.3`** : `manuscrit/04 - Partie IV/Chapitre 11 - Les sept pieges et l atrophie des competences.md` (`122` lignes, `5 239` mots `G1` / `5 448` `split()`), `21` sources `L+`.
- **Rectifications Phase 5 (`P4-007`, Pass 3 `#55`) et réancrages vérifiés** :
  - `L23` (`P4-007`) : remplacement de « dont 40,4 % dans le secteur *Finance et assurances* » par « contre 40,4 % dans le secteur *Finance et assurances* », fidèle aux deux taux distincts de `SRC-014.txt` (l. 3 national `19,2 %` tous secteurs vs l. 7 taux sectoriel `40,4 %` Finance et assurances `[52]`). `Verdict : supporté`.
  - `L79` (ex-`L77`, Pass 3 `#55`), `L88` (`Tableau 11.1`, rangée `4`) et `L120` (arbitrage `3`) : scission de `L77` en deux paragraphes (`CA-05`), séparation nette entre gains immédiats (`[3, 4]`), *deep practice*, vérifications manuelles et *walkthroughs* juniors (`[9, 20]`, `SRC-074.txt` l. 631, `SRC-040.txt` l. 140), et essais de scénarios de défaillance, bascule manuelle et plans de sortie (`[16, 17]`, `SRC-066.txt` l. 117, `SRC-068.txt` § 2.3.5 l. 95) ; retrait de « semestriels » / « deux fois l'an » et qualification explicite de « part plancher sans IA » et « *game days* périodiques » comme choix et modalité d'ingénierie interne. `Verdict : supporté`.
- **Retrait de l'ancienne source *The Coasean Singularity?*, renumérotation `[2]..[21]` et réancrages vérifiés** :
  - Retrait de l'ancienne source `SRC-004` (*The Coasean Singularity?*, ex-référence `[2]`) du dossier `sources/ch11-sources.md` ; renumérotation intégrale des citations `[2]..[21]` dans le chapitre et ce journal d'ancrage, et ajout des sources `[11]` `SRC-053` (`CA/Browser Forum`, `100` j / `47` j, l. 199–205, 1321–1324, citée en `L108`) et `[18]` `SRC-071` (`AIBanks.ca` Q4 2026, l. 5–8, 107–117). `Verdict : supporté`.
  - `L35–L51` (`§ 11.2`) : maintien de la suppression de toute attribution à Lisanne Bainbridge (absente du manuscrit et du corpus `L+`) ; ancrage confirmé sur Parasuraman & Manzey (`[3]` `SRC-009.txt`), Dhanorkar *et al.* (`[21]` `SRC-075.txt`) et Storey (`[9]` `SRC-040.txt`). `Verdict : supporté`.
  - Mise à jour de la citation `SRC-066.txt` (`[16]`, l. 117 *test AI failure and outage scenarios*, remplaçant l'ancien numéro de ligne OOB `495`). `Verdict : supporté`.
