# Cahier des charges (PRD) — Livre 2027 (v1.1)

## 1. Identité et vocation de l'ouvrage

- **Titre de travail** : *Gouverner l'industrialisation cognitive*
- **Sous-titre** : *Architecture de contrôle, preuve et souveraineté dans l'entreprise agentique*
- **Millésime de parution visé** : 2027
- **Crédit d'auteur et de direction** : *à trancher par l'auteur avant lancement* (p. ex. « Direction de l'ouvrage : \<nom\> — rédaction et vérification par agents d'IA »). Aucun agent ne choisit ni n'invente ce crédit.
- **Date de gel des faits (état de référence)** : *à fixer au lancement de la collecte (Tâche 2 de `plan-production-aq.md`)*. Elle est inscrite dans le liminaire (`0.5`) et dans chaque base `sources/chNN-sources.md`. Une édition consolidée est relancée après le 1er mai 2027 avec une nouvelle date de gel.
- **Langue** : Français canadien soigné, accessible à l'ensemble du lectorat francophone international; maintien des termes techniques anglais établis (`AGI`, `ASI`, `MCP`, `A2A`, `Zero-Trust`, `FinOps`, `pass^k`, etc.).
- **Mode de production et d'assurance qualité** : **100 % agentique** (zéro rédaction humaine, zéro relecture humaine intégrale), piloté par les spécifications du dossier `specs/` et vérifié par cinq barrières indépendantes (`contrat-aq.md`).
- **Régime de diffusion par défaut** : Textes et figures sous licence **CC BY 4.0**, scripts et outils de validation sous licence **MIT** (modifiable via le champ `license_mode` de `manifest.json` en cas de cession à un éditeur commercial).

### Raison d'être face aux six ouvrages existants du dépôt
Les volumes `1` à `6` du dépôt (`2 917 pages`, novembre 2026) constituent des **référentiels de consultation et d'audit** structurés autour de codes d'exigences, de capacités et de portes de gouvernance. Ce septième ouvrage remplit une fonction éditoriale distincte : offrir un **livre d'auteur à lecture continue (~260 à 270 pages)** qui part de la question fondatrice de la collection — l'**interopérabilité et l'orchestration** comme tissu conjonctif de l'entreprise agentique (liminaire) — et la relie à la bascule macro-économique de l'industrialisation cognitive (DeepMind, NBER, théorie de la firme de Coase) puis à l'ingénierie concrète du contrôle déterministe et de la preuve juridique, sans jamais exposer le lecteur à une nomenclature matricielle interne.

---

## 2. Thèse centrale (falsifiable)

Les travaux de prospective les plus cités en 2026 décrivent une croissance composée du calcul effectif d'au moins un ordre de grandeur par an, qui banalise une part croissante du travail cognitif et fait émerger des collectifs d'agents agissant à vitesse machine. L'ouvrage soutient que, dans ce contexte, **la valeur stratégique durable et la viabilité juridique d'une organisation tiennent moins aux modèles d'intelligence artificielle — composants remplaçables à obsolescence rapide — qu'au tissu conjonctif et au noyau déterministe qu'elle possède en propre** :

1. **Interopérabilité gouvernée et orchestration bornée** : relier agents, patrimoine applicatif, partenaires et superviseurs humains par des contrats ouverts, un sens métier partagé et une orchestration déterministe, plutôt que par une prolifération d'agents captifs.
2. **Partition 80/20** : confiner le raisonnement probabiliste (environ 20 % de la logique) à l'intérieur d'un cadre de règles métier explicites, de contrats typés et de machines à états durables dotées de compensations dédiées (environ 80 %). *Ce ratio est une heuristique d'ingénierie de la collection, non une mesure empirique : il est présenté comme tel.*
3. **Souveraineté du plan de contrôle** : refuser l'enfermement dans les plans de contrôle fermés des suites `SaaS` en conservant la maîtrise du registre d'agents, des identités non humaines sans secret fixe, des passerelles d'accès et de la couche sémantique.
4. **Économie de la preuve et préservation de l'humain** : satisfaire aux obligations prudentielles et de vie privée par des preuves vérifiables (jusqu'à l'horizon post-quantique) tout en prévenant délibérément l'approbation réflexe et l'atrophie des compétences humaines indispensables au repli opérationnel.

**Critères de réfutation.** La thèse serait affaiblie si, à la date de gel, des études indépendantes montraient en production : (a) des agents faiblement encadrés atteignant une constance et un coût par résultat conforme équivalents à ceux d'architectures bornées; (b) un changement de modèle ou de fournisseur sans coût de sortie significatif en l'absence de noyau possédé; (c) une conformité réglementaire démontrée sans traçabilité ni supervision humaine effective. Le liminaire (`0.5`) et le chapitre 02 exposent l'état de la preuve sur ces trois points.

---

## 3. Lectorat cible et promesse de transformation

Les quatre segments correspondent aux quatre parcours de lecture du liminaire (`0.4`).

| Segment de lectorat | Question d'entrée | Ce que le lecteur sait trancher après lecture |
|---|---|---|
| **Haute direction (`CEO`, `COO`, `CRO`, administrateurs)** | Où investir sans regret d'ici 2035 et comment éviter un fiasco financier ou réglementaire ? | Arbitrer entre acheter des agents `SaaS`, assembler sur standards ouverts ou bâtir; exiger le pilotage au coût complet par résultat conforme; protéger la relève humaine |
| **Direction technologique et architecture d'entreprise (`CIO`, `CTO`, `EA`)** | Comment urbaniser des agents au-dessus d'un patrimoine applicatif hétérogène sans perdre le contrôle ni la souveraineté ? | Posséder le noyau de contrôle, encadrer `MCP` et `A2A` par passerelle, choisir la topologie la plus sobre et séquencer la trajectoire 2027–2035 |
| **Architecture de solutions, plateforme et exploitation (`SA`, ingénierie de plateforme, `SRE`)** | Comment rendre des flux agentiques fiables, observables, compensables et économiquement bornés ? | Imposer l'exécution durable et les sagas compensatoires, juger sur la constance (`pass^k`), armer les coupe-circuits et mesurer le coût complet par résultat |
| **Sécurité, conformité et supervision (`CISO`, juridique, `RPRP`, audit)** | Comment prouver l'imputabilité humaine, la sécurité et la conformité (`Loi 25`, `BSIF E-23`, `AMF`, `EU AI Act`) ? | Remplacer les clés partagées et les filtres probabilistes fragiles par l'isolation structurelle, la délégation cryptographique bornée et un journal d'audit immuable |

---

## 4. Délimitation stricte du périmètre démontré (`DC-01`)

1. **Périmètre démontré** : l'appareil réglementaire, prudentiel et probatoire de l'ouvrage repose sur les **services financiers réglementés au Canada fédéral et au Québec** (ainsi que leurs obligations transfrontalières dans l'**Union européenne**) et sur le **génie logiciel de contrôle déterministe hors modèle**.
2. **Illustrations hors finance** : les exemples tirés d'autres secteurs critiques (santé, énergie, manufacturier `IT/OT`, logistique, secteur public non financier) sont admis pour éclairer l'universalité architecturale du propos, à la condition expresse d'être présentés comme analogies sectorielles sans extrapolation juridique implicite.

---

## 5. Anti-objectifs impératifs (`AO-01` à `AO-07`)

- **`AO-01` — Zéro contournement de contrôle d'accès** : tout refus serveur (`HTTP 403`, `HTTP 429`), pare-feu applicatif, défi anti-robot (CAPTCHA, Turnstile, Anubis), portail d'authentification ou mur payant interrompt immédiatement la collecte. La source est consignée honnêtement en `statut F` et **ne peut fonder aucune affirmation factuelle, chiffrée ou normative**.
- **`AO-02` — Zéro affirmation de mémoire ni preuve circulaire** : aucun chiffre de marché, résultat expérimental, numéro de version de protocole ou délai légal ne provient de la mémoire paramétrique d'un agent. Tout fait s'appuie sur un texte primaire en `statut L+` haché `SHA-256`. **Les volumes `1` à `6` du dépôt, eux-mêmes produits par agents sans relecture humaine intégrale, servent de carte de repérage et jamais de preuve** : chaque fait qui en provient est réancré sur la source primaire qu'ils citent. Les entrées des registres `registre/` portent leur statut de preuve et ne deviennent opposables qu'après ce réancrage.
- **`AO-03` — Zéro jargon matriciel interne** : le corps du liminaire et des chapitres ne contient aucun identifiant de gestion issu des volumes `1` à `6` (préfixes `CAP-`, `EXIG-`, `POR-`, `ANC-`, `INI-`, `PEX-`, `SIG-`, `ADR-`, `DIV-`, sigle `PRR`, ni marqueurs bruts `[S]`, `[D]`, `[A]`, `[M]`, `[N]`, `[L+]`), ni les classifications internes non définies pour le lecteur (p. ex. « Classe 1 », « Stade 3 », « Palier 2 »).
- **`AO-04` — Zéro auto-plagiat textuel** : la prose est intégralement réécrite pour la lecture linéaire; aucune séquence de $\ge 12$ mots consécutifs ne peut recopier les fichiers de `0 - MD/` (hors citations officielles courtes placées entre guillemets et sourcées).
- **`AO-05` — Zéro simulation d'auteur humain ou d'avis juridique** : le liminaire déclare explicitement la rédaction et la vérification 100 % agentiques sur cahier des charges humain, ainsi que le caractère consultatif de l'ouvrage (ni avis juridique, ni certification actuarielle ou d'audit).
- **`AO-06` — Zéro complaisance envers le multi-agents** : aucune topologie multi-agents n'est recommandée sans confrontation préalable à la règle déterministe, à l'agent unique outillé et à l'égalité du budget de calcul.
- **`AO-07` — Zéro fiction déguisée en fait** : toute mise en situation non documentée (ouvertures narratives, cas prospectifs, incidents composites) est explicitement présentée comme **scénario illustratif**; elle ne contient aucun chiffre présenté comme mesuré et ne sert jamais d'appui à une conclusion.

---

## 6. Calibrage quantitatif et structurel

- **Volume cible total** : **74 000 mots** ($\pm 8\ \%$, soit plage admissible de `68 080` à `79 920` mots; environ **260 à 270 pages** en mise en page livre).
  - Texte narratif (`00-liminaire` de `4 200` mots posant le cadre d'interopérabilité et d'orchestration + `Chapitres 01 à 12` de `65 800` mots) : **70 000 mots** ($\pm 8\ \%$ par unité).
  - Annexes de référence générées depuis `registre/` (`Annexes A, B, C`) : **4 000 mots** hors liste bibliographique brute.
- **Iconographie** : **23 figures vectorielles originales** (`Fig-00` inaugurale dans le liminaire + `Fig-01` à `Fig-22` dans les chapitres), d'au plus `14` éléments chacune pour une édition imprimée soignée (zéro capture d'écran récupérée sur le web).
- **Tableaux** : `13 à 19` tableaux comparatifs sur l'ensemble du livre — exactement `1` tableau synoptique dans le liminaire et au plus `2` par chapitre — afin de préserver le rythme d'un essai suivi.

---

## 7. Points de vigilance probatoire connus à la date de spécification

Ces éléments, repérés dans le dépôt, doivent être réancrés ou présentés avec leur statut exact; ils sont prioritaires pour l'ancrage `G2` et les recollations `G3`.

| Élément | Fragilité constatée | Traitement exigé |
|---|---|---|
| Prise d'effet de la ligne directrice de l'`AMF` sur l'IA au 1er mai 2027 | Texte officiel en `statut F` (`HTTP 403`) dans les volumes 3 et 4; date connue par note analytique et sources secondaires | Citer une source `L+` primaire si elle devient accessible; sinon formuler la date avec sa source et son statut |
| Part d'initiatives agentiques exposées à l'abandon d'ici fin 2027 (« plus de 40 % ») | Chiffre d'analyste relayé par les volumes du dépôt | Réancrer sur la publication d'origine accessible, sinon présenter comme estimation d'analyste |
| Tailles de marché par périmètre | Un périmètre n'est connu que par un blogue reprenant un document payant (volume 3, chapitre 50) | Exclure tout chiffre non vérifiable en `L+`; conserver la dispersion comme résultat |
| Date d'application de l'Annexe III de l'`EU AI Act` (2 décembre 2027) | Connue d'abord par une reproduction non officielle, puis par les considérants publiés | Ancrer sur le texte officiel publié |
| Interdiction des rétrofacturations de commissions au 1er octobre 2028 | Repère issu des volumes du dépôt, non relu ici sur texte primaire | Vérifier sur le texte réglementaire primaire avant toute mention |

---

## 8. Critères d'acceptation exécutables (`CA-01` à `CA-18`)

| ID | Critère d'acceptation | Barrière de contrôle | Seuil de réussite bloquant |
|---|---|---|---|
| `CA-01` | Respect du budget global (`68 080`–`79 920` mots) et de la fourchette $\pm 8\ \%$ par unité | `G1` (`verifie_manuscrit.py`) | `100 %` des 16 unités dans leur plage |
| `CA-02` | Absence totale des préfixes et marqueurs bannis (`AO-03`) et des formules creuses de la charte dans le liminaire et les 12 chapitres | `G1` (`verifie_manuscrit.py`) | `0` occurrence détectée par regex |
| `CA-03` | Absence de séquences de $\ge 12$ mots consécutifs identiques à `0 - MD/` hors citations entre guillemets (`AO-04`) | `G1` (`verifie_manuscrit.py`) | `0` collision non citée |
| `CA-04` | Présence effective des sous-sections (`0.1`–`0.6` et `X.1`–`X.4`), de l'ouverture par cas concret et des encadrés prescrits par `toc.md` et `charte-editoriale.md` | `G1` (`verifie_manuscrit.py`) | `13 / 13` unités narratives conformes |
| `CA-05` | Plafond de densité tabulaire et de listes à puces (`charte-editoriale.md`) pour garantir une prose de livre | `G1` (`verifie_manuscrit.py`) | Liminaire : exactement `1` tableau; chapitres : $\le 2$ tableaux; part des lignes en puces $\le 18\ \%$ par unité |
| `CA-06` | Échappement valide des symboles monétaires (`\$`) et rendu effectif des formules en `\(...\)` | `G1` (`verifie_manuscrit.py`) | `0` symbole `$` non échappé; `0` formule non rendue |
| `CA-07` | Concordance exacte des dates et repères chiffrés avec `registre/ancres-chronologiques.json` et `faits-empiriques.json` | `G1` + `G3` | `0` divergence inter-unités |
| `CA-08` | Compilation stricte sans erreur ni avertissement des 23 figures (`Fig-00` à `Fig-22`, `PlantUML` `-failfast2` / `Mermaid`) | `G1` (`verifie_manuscrit.py`) | `23 / 23` figures compilées et référencées |
| `CA-09` | Traçabilité `SHA-256` de 100 % des textes intégraux ouverts `L+` dans `manifeste-sources-sha256.json` | `G1` (`verifie_manuscrit.py`) | `100 %` des empreintes vérifiées |
| `CA-10` | Respect absolu de `AO-01` et `AO-02` : aucune preuve en `statut F`, sur résumé seul ou tirée d'un volume du dépôt sans réancrage; chaque renvoi `[n]` résout vers une entrée de `sources/chNN-sources.md` | `G1` + `G2` | `0 %` de `METADATA_ONLY`, de `statut F` ou de preuve circulaire; `0` renvoi orphelin |
| `CA-11` | Couverture en `L+` des 6 questions de recherche `RQ1`–`RQ6` de `protocole-mlr-2027.json` | `G1` + `G2` | Au moins le seuil `min_included_studies` de chaque axe (`6` pour `RQ1`, `RQ2`, `RQ5`; `5` pour `RQ3`, `RQ4`, `RQ6`) |
| `CA-12` | Ancrage atomique Wyvern indépendant sur le liminaire et les 12 chapitres (`supporté` / `imprécis` / `non supporté`) | `G2` (Wyvern) | `100 %` de *claims* `supportés` sur les `13` unités après rectification |
| `CA-13` | Premier tirage stratifié à l'aveugle (`seed=202701`, 60 énoncés, au moins 2 par unité narrative) recollé mot à mot sur textes bruts `.txt` | `G3` (Recollation 1) | `60 / 60` (`100 %`) après rectification |
| `CA-14` | Second tirage disjoint à froid (`seed=202702`, 60 nouveaux énoncés, 0 chevauchement), exécuté **sur le texte final** après `G4` et le lissage `G5` | `G3` (Recollation 2) | $\ge 95\ \%$ (`57 / 60`) avant correction; `100 %` après |
| `CA-15` | Boucle critique comparative à l'aveugle (`gauntlet-loop`) sur le liminaire et les 12 chapitres contre la barre stylistique nommée | `G4` (`gauntlet-loop`) | Victoire A/B, palier marginal sur 2 tours ou plafond atteint |
| `CA-16` | Passe de lissage transversal sur le manuscrit assemblé (transitions, élimination des redites inter-unités) | `G5` (Lissage) | `0` redite structurelle signalée au rapport final |
| `CA-17` | Régénération déterministe des Annexes A, B et C à partir des registres JSON et des journaux d'AQ | `G1` + `G5` | `0` édition manuelle hors registre dans les annexes |
| `CA-18` | Compilation `Pandoc` / `Typst` (PDF + HTML autonome) et inspection visuelle automatisée de 100 % des pages | `G5` (Visuel) | `0` page tronquée, tableau écrasé ou formule cassée |
