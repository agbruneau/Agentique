# Journal d'ancrage atomique Wyvern — Chapitre 05 (`Chapitre 05.md`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/02 - Partie II/Chapitre 05.md` (`ch05`)
- **Agent auditeur :** `wyvern-05` (auditeur atomique Wyvern neuf, barrière `G2` selon `AO-07`)
- **Base fermée autorisée :** `Compendium/ouvrage/sources/ch05-sources.md` (`[1]`–`[10]`), textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt`, registres `Compendium/ouvrage/registre/*.json`, exclusions `Compendium/ouvrage/recherche/registre-statut-f.json`, spécifications `Compendium/ouvrage/specs/{manifest.json,protocole-mlr-compendium.json}`, rapport `Compendium/ouvrage/aq/rapports-g0.json` et renvois internes vérifiés dans `Corpus/Tome 1..8*.md`
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Passe G2 initiale (supportés) :** 20 affirmations atomiques validées sans retouche sur `36` auditées (`16` rectifiées directement dans `Chapitre 05.md`, dont `4` comportant des chiffres ou libellés divergents retirés et réancrés sur les textes `L+`)
- **Actions appliquées dans `Chapitre 05.md` :** rectification exacte des `8` domaines `D1–D8` (`Tome 4 § 12.2`, `Tome 5 § 6.1`), suppression des taux non fondés dans `ch05-sources.md` (`93 %` issu d'une source absente du chapitre, `26 %` issu de `PMC3240751` exclu en `statut F`, `0,8 %` confondu entre appels irréversibles et routage `Classe 2`), réancrage exact de `12,36 %` / `0,8 %` / `> 15 %` sur `SRC-073` (`[7]`) et de l'enquête auprès de `17` développeurs sur `SRC-075` (`[6]`), réattribution des échantillons `5 %` / `1 %` à la revue a posteriori `N3–N4` (`EXIG-AUT-21`), précision du profil `CIBA`/`FIDO2`/`RFC 9396` et du rejeu sur expiration (`EXIG-AUT-12`, `EXIG-AUT-16`), suppression de la mention erronée à `§ 42.3.2` au profit d'`EXIG-CON-08`, et ajustement de la légende `Figure 3` (`SCH-05-03`)
- **Verdict final — supportés :** 38 / 38 (100,0 %)

---

## 1. Synthèse de la vérification par section

| Section (`Chapitre 05.md`) | Affirmations auditées | Initialement conformes | Écarts rectifiés ou réancrés | Actives finales (`100,0 %`) |
| --- | :---: | :---: | :---: | :---: |
| En-tête, `5.1` et Trois invariants (`L1–L16`) | 6 | 6 | 0 | 6 |
| `5.2.1` Échelle unifiée et règle du maillon (`L19–L61`) | 13 | 7 | 6 (`C05-10`, `C05-11`, `C05-12`, `C05-14`, `C05-16`) | 13 |
| `5.2.2` Régimes d'agent et anti-complaisance (`L63–L101`) | 13 | 6 | 7 (`C05-22`, `C05-23`, `C05-25`..`C05-30`) | 13 |
| `5.3` Exigences, interfaces et livrables (`L103–L121`) | 4 | 1 | 3 (`C05-34`, `C05-35`, `C05-36`) | 4 |
| **Total** | **36** | **20** | **16** | **36** |

---

## 2. Journal détaillé des affirmations atomiques (`C05-01` à `C05-36`)

### 2.0 En-tête, section `5.1` et encadré des trois invariants (`L1–L16`)

- **C05-01 (`L1`, `L3`) :** Titre et question directrice posant l'unification des échelles d'autonomie et de criticité (`N0–N4`/`L0–L4`), la propagation des exigences sécuritaires au maillon le plus élevé et la prévention de la validation réflexe.
  - Preuve vérifiée : `specs/manifest.json`, `prd.md`, `Corpus/Tome 2 § 8`, `Corpus/Tome 5 § 6`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-02 (`L7`) :** La doctrine d'**Autonomie bornée** pose l'autonomie comme un choix explicite d'architecture et de configuration hors du modèle, bornant le périmètre d'action, les écritures et les budgets conformément à `BSIF E-23` `[1]` et au bulletin technologique du BSIF de juillet 2026 sur le *harnessing* `[2]`.
  - Preuve vérifiée : `corpus_l_plus/SRC-065.txt`, `corpus_l_plus/SRC-066.txt L25–L27, L77–L90, L173–L175`, `registre/glossaire-termes.json L7–L13`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-03 (`L9`) :** Le chapitre (`D02` / `SUB_D02_02`) réconcilie `DISC-01` et `DISC-02` (`N0`, `N1–N4`/`L0–L4`, `D1–D8`, `Stades 0–4`, `Classes 1–6`, `P0–P3`), applique la **règle du maillon le plus élevé**, l'union la plus stricte et la règle d'or `≤ N2`, et sépare les régimes d'agent ainsi que `PC3` de l'article `12.1` de la Loi 25 `[5]` face à `OWASP ASI09` `[10]`.
  - Preuve vérifiée : `specs/manifest.json`, `registre/concordance-taxonomies.json`, `registre/glossaire-termes.json L207–L213`, `SRC-063.txt`, `SRC-055.txt`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-04 (`L13`) :** Premier invariant exécutable (`EXIG-AUT-01..05`, `EXIG-GOV-17`) : niveau minimal suffisant entre `N1` et `N4` (`N0` réservé aux flux sans choix de modèle), `ODD` pour `N3–N4` et interdiction sans dérogation de `NX` (`Classe 6`).
  - Preuve vérifiée : `Corpus/Tome 2 L3398–L3437`, `registre/matrice-exig-prr-c40.json L128–L139`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-05 (`L14`) :** Deuxième invariant exécutable (`EXIG-AUT-07..11`, `CAP-048`) : héritage asymétrique des contrôles du maillon aval sans extension des droits d'écriture en amont, plafond `≤ N2` sur cumul impact élevé, irréversibilité et détection lente, et union la plus stricte en échec fermé à la passerelle.
  - Preuve vérifiée : `Corpus/Tome 2 L3486–L3600`, `Corpus/Tome 3 L20123–L20203`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-06 (`L15`) :** Troisième invariant exécutable (`EXIG-AUT-12..23`) : nulle action `P3` sans jeton hors bande (`CIBA` `[8]`, `FIDO2`, `RFC 9396` `[9]`) lié à `SHA-256` (`JCS`), écran différentiel hors modèle plafonné (`≤ 33` dossiers par quart) et distinct de la révision prévue à l'article `12.1` `[5]`.
  - Preuve vérifiée : `SRC-045.txt`, `SRC-042.txt`, `SRC-063.txt`, `Corpus/Tome 2 L3639–L3776`, `Corpus/Tome 3 L21772–L21784`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté

### 2.1 Section `5.2.1` — Échelle unifiée `N0–N4`/`L0–L4` et règle du maillon le plus élevé (`L19–L61`)

- **C05-07 (`L21`) :** Sous `DISC-01`, `N0` (`L0` canonique) désigne exclusivement un traitement déterministe où le code fixe chaque étape d'exécution (même lorsqu'un modèle effectue une extraction ponctuelle dans un nœud borné), tandis que `N1` (`L1`) attribue le statut d'agent au registre parce que le modèle choisit ses appels d'outils en boucle.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L188–L205`, `Corpus/Tome 2 L727, L756`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-08 (`L23`) :** `N2` (`L2`) impose une approbation humaine préalable (`HITL`) pour chaque mutation significative ; `N3` (`L3`) autorise l'autonomie surveillée (`HOTL`) sur `P2` réversible sous seuils quantitatifs et `ODD` documenté ; `N4` (`L4`) regroupe les agents ambiants déclenchés sur événement ou horaire, réservés aux classes de risque faible sous `ODD` certifié, repli sûr éprouvé et décision du comité (`EXIG-AUT-04`, `EXIG-CON-02`).
  - Preuve vérifiée : `Corpus/Tome 2 L3389–L3391, L3424–L3426, L5659`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-09 (`L25`) :** Le niveau `NX` (`Classe 6` — hors mandat : modification d'objectifs, élargissement de privilèges, code libre non confiné, exécution critique hors contrôle) est proscrit sans dérogation (`EXIG-AUT-03`, `EXIG-GOV-17`), et toute modification matérielle déclenche une réévaluation avant remise en service (`EXIG-AUT-05`).
  - Preuve vérifiée : `Corpus/Tome 2 L3414–L3437`, `registre/matrice-exig-prr-c40.json L129`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-10 (`L25`) :** La réévaluation avant remise en service s'accorde avec les attentes de gestion du risque de modélisation de `BSIF E-23` `[1]` et l'article `14` du Règlement `(UE) 2024/1689` `[3]`.
  - Preuve vérifiée : `SRC-065.txt L31, L229` (prise d'effet le `1er mai 2027`, mise à jour d'inventaire sur modifications des modèles), `SRC-060.txt L3853` (proportionnalité des mesures de contrôle humain au niveau d'autonomie et au contexte à l'art. `14` par. `3`).
  - Passe initiale : écart rectifié · Action : précisé la prise d'effet (`1er mai 2027`), la mise à jour d'inventaire `[1]` et la proportionnalité du contrôle humain `[3]` · Verdict : supporté
- **C05-11 (`L27`) :** Sous `DISC-02`, la gouvernance matricielle croise les huit domaines d'affaires `D1–D8` du traité avec `Stades 0–4`, `Classes 1–6` et paliers d'outils `P0–P3`.
  - Preuve vérifiée : `Corpus/Tome 4 § 12.2 L2900–L2909`, `Corpus/Tome 5 § 6.1 L895` (`D1` distribution/relation client ; `D2` conseil/vente/convenance ; `D3` souscription/tarification/crédit ; `D4` contrats/comptes ; `D5` règlement/indemnisation/sinistres ; `D6` conformité/LBC/risques ; `D7` trésorerie/investissement/réassurance ; `D8` opérations TI/cyberrésilience).
  - Passe initiale : écart rectifié · Action : remplacé les intitulés divergents (`D2`, `D4`, `D5`, `D7`, `D8`) par la nomenclature canonique vérifiée du traité · Verdict : supporté
- **C05-12 (`L29`) :** La matrice s'arrime aux repères méthodologiques consolidés dans les tomes (`SAE J3016` par analogie pour `ODD` et repli, `IMDA v1.5`, Feng et coll., `LCIM`, `ISO 11354 FEI`), proscrit le `Stade 4` en `D2` (`Stades 2–3`) et en `D6` (`Stade 3` interne), et ramène l'exécution `OPA`/`Rego` (`CH-20`) à `BLOQUANT`, `OBLIGATOIRE`, `RECOMMANDE` × `P0–P3`.
  - Preuve vérifiée : `Corpus/Tome 1 L238–L250`, `Corpus/Tome 2 L3446–L3457`, `Corpus/Tome 4 L2957–L2961`, `Corpus/Tome 5 L895`, `registre/concordance-taxonomies.json L226`.
  - Passe initiale : écart rectifié · Action : précisé le statut d'analogie de `SAE J3016` et le plafonnement distinct `Stades 2–3` en `D2` contre `Stade 3` interne en `D6` · Verdict : supporté
- **C05-13 (`L31`) :** Correspondance stades/niveaux : `Stade 0` repose sur du code déterministe `N0`, `Stade 1` reste confiné à `N0–N1` durant une fenêtre transitoire maximale de `90` jours, `Stade 2` ouvre la production réglementée, `Stade 3` couvre l'orchestration interne maîtrisée et `Stade 4` demeure réservé aux échanges inter-entreprises fédérés hors `D2` et `D6`.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L105–L132`, `Corpus/Tome 4 L2917–L2927`, `Corpus/Tome 5 L895`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-14 (`L33–L43`) :** `Tableau 5.1` unifiant les sept lignes d'actes (`Hors classe` à `Classe 6`), niveaux `N0–N4`/`L0–L4`, paliers `P0–P3` et contrôles minimaux.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L135–L184`, `Corpus/Tome 5 L899–L907`, `SRC-063.txt L1542–L1555`.
  - Passe initiale : écart rectifié · Action : précisé en `Classe 2` `N3` (`faible`/`modérée`) ou `N2` (`élevée`) et revue `5 %` / `1 %`, et ajouté les `2` signataires en classe élevée en `Classe 4` · Verdict : supporté
- **C05-15 (`L45–L47`) :** `Figure 1` (`SCH-05-01.svg`) présentant l'escalier d'autonomie `N0–N4`/`L0–L4`, l'interdit `NX` et la matrice `D1–D8 × Classes 1–6`.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-05-01.svg`, `schemas/rendus/SCH-05-01.svg`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-16 (`L49–L53`) :** Un agent `L1` en amont d'un agent `L3` sans validateur ni filtre d'assainissement déclenche la **règle du maillon le plus élevé** (*High-Water Mark*), vérifiée par `OPA` sur `deployment-footprint.yaml` : héritage asymétrique des exigences aval (sans acquisition des droits d'écriture) pour satisfaire à `BSIF E-23` `[1]`, `EU AI Act` `[3]` et contrer le détournement d'objectif en chaîne (`OWASP ASI01` `[10]`).
  - Preuve vérifiée : `SRC-065.txt`, `SRC-060.txt`, `SRC-055.txt L1933–L2147`, `Corpus/Tome 3 L20123–L20203`, `registre/glossaire-termes.json L207–L213`.
  - Passe initiale : écart rectifié · Action : scindé la phrase de `77` mots et formulé les renvois `[1]`, `[3]`, `[10]` comme finalités de conformité et de défense plutôt que comme source littérale du terme *High-Water Mark* · Verdict : supporté
- **C05-17 (`L55`) :** La **règle d'or** (`EXIG-AUT-07`, `CAP-048`) plafonne l'autonomie à `≤ N2` dès qu'une tâche cumule impact métier élevé, faible réversibilité et détection lente (ou critère d'étalonnage incertain), sans dérogation par score sur banc synthétique.
  - Preuve vérifiée : `Corpus/Tome 2 L3486–L3497`, `Corpus/Tome 5 L912`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-18 (`L57`) :** La passerelle calcule à l'exécution l'**union la plus stricte en mode fermé** (`EXIG-AUT-10`, `EXIG-AUT-11`) entre matrice classe × palier `P0–P3` du catalogue (`EXIG-AUT-08`), maillon le plus restrictif, seuils financiers et règle de deux (`EXIG-SEC-04`), en ignorant les indicateurs externes auto-annoncés (`readOnlyHint` `MCP`) et en refusant en cas de donnée manquante.
  - Preuve vérifiée : `Corpus/Tome 2 L3515–L3600`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-19 (`L59–L61`) :** `Figure 2` (`SCH-05-02.png`) illustrant la règle du maillon le plus élevé et la règle d'or `≤ N2` dans un graphe multi-agents.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-05-02.mmd`, `schemas/rendus/SCH-05-02.png`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté

### 2.2 Section `5.2.2` — Distinction des régimes d'agent et supervision anti-complaisance (`L63–L101`)

- **C05-20 (`L65`) :** Le Tableau 7 (`Tome 2, § 3.1–3.4`) sépare flux déterministe (`N0`), agent (modèle en boucle), agent interactif (session initiée et parrainée par un mandant humain) et agent ambiant (déclenchement asynchrone sur événement ou échéance horaire).
  - Preuve vérifiée : `Corpus/Tome 2 L713–L812`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-21 (`L67`) :** L'attribut cryptographique d'origine bloque par construction toute écriture ambiante non approuvée pour tout agent `< N4` (`EXIG-AUT-01`), complété par la **triple exclusion identitaire** (`EXIG-IAM-03` à `EXIG-IAM-05`, `CH-16`) interdisant compte humain, principal/secret partagé et personnalité responsable au profit d'une identité non humaine distincte rattachée à un parrain humain.
  - Preuve vérifiée : `Corpus/Tome 2 L761, L813–L831, L3402, L3844–L3866`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-22 (`L69`) :** Le référentiel `OWASP ASI09` `[10]` documente la fragilité du contrôle humain face aux interfaces conversationnelles fluides, et l'enquête qualitative `arXiv:2606.05391` `[6]` auprès de `17` développeurs expérimentés confirme que le suivi en temps réel est rare et que les valideurs recourent à des raccourcis sur des sorties longues.
  - Preuve vérifiée : `SRC-055.txt L1190–L1255`, `SRC-075.txt L9–L15, L383–L400`.
  - Passe initiale : écart rectifié · Action : retiré les mentions `93 %` (source Anthropic absente du chapitre) et `26 %` (issu de `PMC3240751` exclu en `statut F`, `AO-01`), et précisé les résultats effectifs de `SRC-075` (`17` développeurs) · Verdict : supporté
- **C05-23 (`L71`) :** L'étude *Nature Scientific Reports* d'août 2026 (`AL-Ali` et coll. `[7]`, retenue en `L+` après exclusion en `statut F` de `PMC3240751` bloqué par `CAPTCHA`) établit en simulateur de maintenance prédictive qu'une IA non calibrée échoue dans `12,36 %` des cas contre `0,8 %` sous fusion adaptative calibrée, tandis que la sous-estimation humaine sous forte pression fait franchir `15 %` d'échecs comme mode de défaillance dominant.
  - Preuve vérifiée : `SRC-073.txt L46, L212, L355, L408`, `ch05-sources.md L123`, `registre/registre-statut-f.json L84–L93`.
  - Passe initiale : écart rectifié · Action : corrigé l'attribution erronée de `12,36 %` à la pression bancaire et réancré exactement les grandeurs `12,36 %`, `0,8 %` et `> 15 %` sur `SRC-073` · Verdict : supporté
- **C05-24 (`L73`) :** La règle de libération humaine `H-31` et l'approbation hors bande (`EXIG-AUT-09`, `EXIG-AUT-12` à `EXIG-AUT-16`) canonisent les paramètres en `I-JSON` (`RFC 8785`), calculent `h = SHA-256(JCS(...))` et suspendent la demande dans une boîte d'attente persistante (`EXIG-AUT-16` à `EXIG-AUT-18`, `Signals`/`Awakeables` `Temporal`/`Restate`, `CH-15`).
  - Preuve vérifiée : `Corpus/Tome 1 L3705`, `Corpus/Tome 2 L3635–L3705`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-25 (`L75`) :** Suivant le profil du traité (`EXIG-AUT-14`, `EXIG-AUT-15`), la sollicitation passe par `OpenID Connect CIBA Core 1.0` (`auth_req_id`) `[8]`, authentification forte `FIDO2` et `authorization_details` de `RFC 9396` `[9]` ; le jeton porte un `jti` atomique, dure au plus `15` minutes et lie une seule opération (y compris ses réessais idempotents) au condensat `h`, conservé à la passerelle hors conversation.
  - Preuve vérifiée : `SRC-045.txt L140–L175`, `SRC-042.txt L15–L175`, `Corpus/Tome 2 L3637–L3668`.
  - Passe initiale : écart rectifié · Action : précisé le rattachement du profil à `EXIG-AUT-14`/`15` et la portée du jeton sur les réessais idempotents de la même opération (`EXIG-AUT-12`) · Verdict : supporté
- **C05-26 (`L77`) :** En classe critique élevée, une double signature indépendante sur `h` s'applique (`EXIG-AUT-12`) ; en cas d'expiration (`15` min) ou de refus (« Ignorer »), l'action n'est pas exécutée, l'état est vérifié par clé d'idempotence si l'issue est inconnue et une nouvelle approbation ou une file d'escalade manuelle nommée est requise (`EXIG-AUT-12`, `EXIG-AUT-16`), avec revalidation de l'état métier au réveil avant mutation idempotente.
  - Preuve vérifiée : `Corpus/Tome 2 L3643, L3695`.
  - Passe initiale : écart rectifié · Action : retiré l'énoncé sans appui d'un rejeu automatique limité à une nouvelle demande et rétabli la règle exacte d'`EXIG-AUT-12` et `EXIG-AUT-16` · Verdict : supporté
- **C05-27 (`L79–L84`) :** Le dispositif anti-complaisance (`A2UI`, `EXIG-AUT-19` à `EXIG-AUT-21`) contre `ASI09` `[10]` s'articule en quatre volets : écran différentiel `I-JSON` hors modèle ; filtrage sélectif `Classe 2` et plafond `≤ 33` dossiers complexes/quart (`360` min × `65 %` / `7` min) ; `3 %` à `5 %` de témoins canaris (`POR-014`), suivi mensuel et revue a posteriori `N3–N4` à `5 %` (modérée) et `1 %` (faible) (`EXIG-AUT-21`) ; quota manuel dès `> 70 %` d'automatisation (`INI-043`) et bascule `N2` en `< 60 s` (`POR-015`).
  - Preuve vérifiée : `SRC-055.txt L1256–L1291`, `Corpus/Tome 2 L3727–L3749`, `Corpus/Tome 3 L21772–L21785`, `Corpus/Tome 4 L4591, L4830`.
  - Passe initiale : écart rectifié · Action : corrigé `six règles` en `quatre volets`, supprimé `0,8 %` absent des sources ouvertes du chapitre sur le routage `Classe 2`, ajouté la base de calcul de `33` et rattaché `5 %` / `1 %` à la revue a posteriori `N3–N4` (`EXIG-AUT-21`) · Verdict : supporté
- **C05-28 (`L86`) :** En réservant la porte humaine aux exceptions hors seuils en `Classe 2` et à `100 %` des actes `P3` (`Classe 4`), le dispositif évite la saturation tout en maintenant un bouton d'arrêt conforme à l'article `14` du Règlement `(UE) 2024/1689` `[3]`.
  - Preuve vérifiée : `SRC-060.txt L3878–L3879` (art. `14` par. `4` al. e), `Corpus/Tome 2 L3725`.
  - Passe initiale : écart rectifié · Action : retiré `0,8 %` au profit d'escalade sélective sur exception en `Classe 2` · Verdict : supporté
- **C05-29 (`L88–L90`) :** `Figure 3` (`SCH-05-03.svg`) synthétisant la prévention de la validation réflexe (`ASI09`), le circuit `CIBA`/`JCS`, la vue différentielle et la distinction `PC3` / Loi 25.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-05-03.puml`, `schemas/rendus/SCH-05-03.svg`.
  - Passe initiale : écart rectifié · Action : retiré `à 93 %` du texte alternatif et de la légende de la figure · Verdict : supporté
- **C05-30 (`L92`) :** Séparation infranchissable entre l'arrêt préventif `PC3` (`HITL` ou `CIBA` avant `P3`) et le régime des décisions exclusivement automatisées de l'article `12.1` de la Loi 25 `[5]` (en vigueur depuis le `22 septembre 2023`), en cohérence avec l'article `14` du Règlement `(UE) 2024/1689` `[3]` dont le modificatif `(UE) 2026/1744` reporte au plus tard au `2 décembre 2027` l'échéance de l'Annexe III `[4]` ; une validation de façade n'écarte pas l'article `12.1` (`EXIG-CON-08`).
  - Preuve vérifiée : `SRC-063.txt L1542–L1555, L2485`, `SRC-060.txt L3842–L3880`, `SRC-061.txt L709–L713`, `Corpus/Tome 2 L5760–L5766`.
  - Passe initiale : écart rectifié · Action : remplacé la référence erronée à `§ 42.3.2` (qui portait dans le Tome 1 sur le vide protocolaire) par `EXIG-CON-08` · Verdict : supporté
- **C05-31 (`L94`) :** Dès qu'une décision affecte une personne sans réexamen substantiel, la filière `EXIG-AUT-22`–`23` et `EXIG-CON-07`–`09` assure avis contemporain (`PC1`), explication sur demande des raisons et principaux facteurs (`PC2`), rectification, accès à un membre du personnel habilité à infirmer la décision et conservation `≥ 1` an (`≥ 7` ans en valeurs mobilières).
  - Preuve vérifiée : `SRC-063.txt L1542–L1555`, `Corpus/Tome 2 L5689, L5752–L5774, L6137–L6145`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-32 (`L96–L101`) :** `Tableau 5.2` opposant `PC3` (`HITL`/`CIBA`) et révision humaine Loi 25 art. `12.1` `[5]` selon le moment d'intervention, le mécanisme technique (`CIBA`/`FIDO2` `[8]` + `RFC 9396` `[9]` lié à `h` `≤ 15` min contre `PC1`, `PC2`, rectification et recours), l'autorité humaine et la rétention probatoire (`≥ 1` an `EXIG-CON-09`).
  - Preuve vérifiée : `SRC-063.txt`, `SRC-045.txt`, `SRC-042.txt`, `Corpus/Tome 2 L3643, L5752–L5774`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté

### 2.3 Section `5.3` — Exigences vérifiables, interfaces systémiques et livrables d'acceptation (`L103–L123`)

- **C05-33 (`L107`) :** Cinq exigences (`EXIG-D02-02.1` à `EXIG-D02-02.5`) encadrées par la clause `non-avis` (`AO-05`) au gel du `2 décembre 2026` (`[1]` à `[10]`), avec maintien en `statut F` (`AO-01`) des quatre ressources inaccessibles : `PMC3240751` (`CAPTCHA`), `lautorite.qc.ca` (`HTTP 403`), `genai.owasp.org` (`HTTP 403`, compensée par `SRC-055` `[10]`) et `legisquebec` (`HTTP 403`, compensée par `SRC-063` `[5]`).
  - Preuve vérifiée : `sources/ch05-sources.md L5, L121–L126`, `recherche/registre-statut-f.json`, `SRC-055.txt L13`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C05-34 (`L109–L117`) :** `Tableau 5.3` récapitulant `EXIG-D02-02.1` à `EXIG-D02-02.5`, leurs contrôles exécutables, seuils (`N1`–`N4`, zéro `NX`, zéro `Stade 4` `D2`/`D6`, blocage ambiant `< N4`, `OPA` `deployment-footprint.yaml`, `≤ N2`, mode fermé, `h = SHA-256(JCS(...))`, `≤ 15` min, `jti`, zéro oui textuel, `I-JSON`, `≤ 33`/quart, `3 %`–`5 %` canaris, revue `5 %`/`1 %`, archive `≥ 1` an) et renvois.
  - Preuve vérifiée : `prd.md L1119–L1123`, `Corpus/Tome 2`, `Corpus/Tome 4`.
  - Passe initiale : écart rectifié · Action : ajouté la mention `revue 5 %/1 %` dans la ligne `EXIG-D02-02.5` · Verdict : supporté
- **C05-35 (`L119–L121`) :** Interfaces systémiques du chapitre vers `CH-01`, `CH-02`, `CH-04`, `CH-06`, `CH-09`, `CH-13`, `CH-15`, `CH-16`, `CH-17` (extrait synchronisé `G0-EX-CH02-02`), `CH-20`, `CH-22`, `CH-25`, `CH-26`, `CH-28`, `CH-29`, `CH-31`, `CH-33` et `CH-36`.
  - Preuve vérifiée : `prd.md L1161–L1188`, `plan.md L714`, `aq/rapports-g0.json L113`.
  - Passe initiale : écart rectifié · Action : remplacé `le paradoxe de l'inversement` vers `CH-09` par `l'illusion d'une validation de façade` · Verdict : supporté
- **C05-36 (`L123`) :** Livrables d'homologation vérifiables aux portes `G1` à `G5` : fiche au registre central, `deployment-footprint.yaml` validé par `OPA`, essais de passerelle en mode fermé (`JCS` et `jti`), rapports mensuels de vigilance de la console différentielle (incluant revue `5 %`/`1 %` en `N3–N4`) et dossier juridique dissociant `PC3` de l'article `12.1`.
  - Preuve vérifiée : `plan.md L729`, `Corpus/Tome 2 EXIG-AUT-21`.
  - Passe initiale : écart rectifié · Action : précisé le rattachement de la revue `5 %` / `1 %` aux appels `N3–N4` sans approbation préalable · Verdict : supporté

---

## 3. Contrôle final post-rectifications (`verifie_manuscrit.py --unit ch05 --strict`)

- **Mots vérifiés (`Chapitre 05.md`) :** `4 016` mots de prose (plage autorisée `[3 552, 4 168]`, cible `3 860`, conforme `CA-01`).
- **Base fermée citée (`CA-09`, `CA-10`, `CA-11`) :** `10 / 10` sources (`[1]`–`[10]`) citées, `0` référence orpheline, `4` exclusions `statut F` qualifiées sans exploitation probante (`PMC3240751`, `lautorite.qc.ca`, `genai.owasp.org`, `legisquebec`).
- **Synchronisation et hygiène (`CA-02..CA-08`, `CA-22`) :** `0` symbole dollar non échappé, `0` collision `12-grammes`, `3` tableaux (`Tableau 5.1` à `Tableau 5.3`), `3` figures (`SCH-05-01` à `SCH-05-03`), `2` vedettes propriétaires du glossaire présentes (`Autonomie bornée`, `règle du maillon le plus élevé`), encodage UTF-8 sans BOM et fins de ligne `LF` strictes.
- **Verdict final — supportés :** 38 / 38 (100,0 %)

---

## Mise à jour post-révision PRD (`REV-04`)

- **C05-REV-01 (`L9`, `L29`, `L47`, `L61`, `L90`, `L107`, `SCH-05-01.svg`, `SCH-05-03.puml`, `PRD-L1-007`, `008`, `011`, `015`, `016`, `018`, `021`)** — Numérotation continue `Figure 17`–`Figure 19`, correction de l'italique imbriqué en légende de `Figure 18` (`SCH-05-02`), retrait des fuites d'atelier (`SUB_D02_02`, `SRC-055`, `SRC-063`), ajout de `ISO/IEC 42105`, retrait des backticks littéraux dans `SCH-05-01.svg`, alignement de `SCH-05-03.puml` sur `AL-Ali 2026` (`12,36 %` / `> 15 %` sous cadence, retrait du repère `93 %` issu de la source exclue `PMC3240751`) et remplacement des deux emplois de `vs`.
  - *Preuve primaire :* `SRC-073.txt` (`[7]`, `AL-Ali 2026`), `Compendium/prd.md` (`L1148`), `specs/manifest.json`, `schemas/SCH-05-01.svg`, `schemas/SCH-05-03.puml`.
  - Verdict : supporté
- **C05-REV-02 (`L9`, `L55`, `§ 5.1`, `§ 5.2.1`)** — Qualification de **l'agentivité des systèmes** (*system agency*) comme propriété configurée, bornée et vérifiée par le harnais externe hors modèle ; distinction entre agentivité locale d'un composant et agentivité des systèmes effective sous règle asymétrique du maillon le plus élevé et proscription `NX` bloquant toute agence excessive.
  - *Preuve primaire :* `SRC-066.txt` (`[2]`, `L27`, `L65`, `L175`), `SRC-055.txt` (`[10]`, `L237–L242`).
  - Verdict : supporté
- **Contrôle `REV-05` :** `3 798` mots (`verifie_manuscrit.py`) dans `[3 552, 4 168]`, `verifie_manuscrit.py --unit ch05 --strict` = `exit 0`. **Verdict final : `38 / 38` (`100,0 %` supporté).**
