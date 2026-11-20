# Chapitre 8 — Observabilité à double couloir PII, journal d’audit JCS, évaluation E1–E3 et FinOps CPO

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 38–40, Ann. N]` · `[CAD26 ch. 10, Ann. H | EXIG-OBS-01..13, EXIG-EVA-01..06, EXIG-FIN-01..10 | PRIN-06, PRIN-08]` · `[C27 ch. 33–34, 40 | ADR-021..023]` · `[PD28 M-7, M-24 | PRI-013, PRI-014 | CAP-042..046, CAP-049 | DEC-010, DEC-011 | POR-002..004, POR-009, POR-015, POR-016]`.

*Question directrice : Comment voir, prouver, qualifier et facturer le comportement d’un parc d’agents en production sans fuite de renseignements personnels ni cécité économique ?*

**Thèse du chapitre :** Les sondes d’exploitation classiques restent au vert lorsqu’un agent hallucine, dérive ou exécute une action erronée. Gouverner un parc exige quatre disciplines articulées P : PRI-013 P : PRI-014 E : PRIN-06 E : PRIN-08. D’abord, la télémétrie `OpenTelemetry` épinglée à double couloir interdit tout contenu en production et purge la voûte forensique sous 14 jours P : CAP-042 E : EXIG-OBS-01 E : EXIG-OBS-07 E : EXIG-OBS-08. Ensuite, un journal d’audit distinct canonise cinq éléments en `RFC 8785`, ancrés chaque heure hors domaine et gardés au moins 24 mois P : CAP-049 E : EXIG-OBS-11 E : EXIG-OBS-12 E : EXIG-OBS-13. Par ailleurs, la qualification `E1–E3` mesure la constance `pass^k`, couplée au repli automatique `< 60 s` P : CAP-043 P : CAP-044 P : POR-015 et à la baisse d’autonomie après trois mois hors cible E : EXIG-EVA-03 E : EXIG-EVA-06. Enfin, l’économie se pilote au coût complet par résultat conforme (`CPO`) jusqu’à la refacturation interne P : CAP-045 P : DEC-011 P : POR-016 E : EXIG-FIN-01 E : EXIG-FIN-09.

## 8.1 Télémétrie `OpenTelemetry GenAI` épinglée et collecte souveraine à double couloir PII

L’observabilité applicative (`APM`) mesure la disponibilité mais ignore la rectitude métier. Un `HTTP 200 OK` couvre aussi bien un acte valide qu’une boucle coûteuse ou détournée (`C26 ch. 38`). Malgré la convergence vers `OpenTelemetry`, son socle reste instable au 1er novembre 2026 (`CAD26 Annexe H.2` p. 336, `C26 Annexe N.2` p. 663). `semantic-conventions-genai` n’a **aucune version étiquetée** (`S-121`). Son registre (`v1.44.0`, 31 oct. 2026) compte `85` **attributs** `gen_ai.*` **tous en statut** `Development`, exposés aux renommages et dépourvus de champs de mandat (`C26 § 38.5`, `S-138`).

Pour isoler le code (`ADR-021`, `SIG-006`), l’AS **épingle** `OpenTelemetry v1.41.0` **derrière une table de correspondance au collecteur** P : CAP-042 E : EXIG-OBS-01 ; `CRE-IA-2027` **v2.0** (`exigences-v2.json`) verrouille cette isolation des `85` attributs `gen_ai.*` (`Development`), impose `60 jours` de transition sur passage `Stable`, porte la rétention chaude cible d’audit à `45 j` `[S]` (banque/assurance) et généralise les badges CI *Borealis-Bench* (`DC-P11`). `W3C Trace Context` traverse `MCP`, `A2A` et `CloudEvents` E : EXIG-OBS-02 sans `RP` en `Baggage` E : EXIG-OBS-10. La **jointure trace ↔ mandat** porte le `Tableau 41` (`CAD26` p. 173 : `ca.entreprise.cost_center`, `task_id`, `autonomy_level`, `approval.jti`, `a2a.*`, `content_ref`) E : EXIG-OBS-03 E : EXIG-OBS-04 E : EXIG-OBS-05 E : EXIG-OBS-06 E : EXIG-OBS-08, tandis que clé d’idempotence, risque et approbateur résident au journal d’audit E : EXIG-OBS-12.

Sous `Loi 25`, la collecte applique l’**architecture souveraine à double couloir PII** (volets `3a–3b`, Fig. 7, Ch. 7 ; `CAD26 Tableau 10` p. 33, `§ 10.2`, `C27 ch. 33`, `POR-002`) :

1. **Couloir opérationnel (zéro contenu).** Sur `100 %` du trafic, il ne capte que les métadonnées (durées, jetons lus/écrits/cachés, versions, verdicts, coûts) et pseudonymise les identifiants en `SHA-256` poivré (rétention indicative `13 mois` `[S]`, `C27 § 33.10`). **Tout contenu brut d’invite, réponse ou argument y est interdit**, avec caviardage en sortie E : EXIG-OBS-07 E : EXIG-OBS-09.
2. **Couloir forensique scellé (« bris de glace »).** Sur incident ou débogage motivé, la session est chiffrée hors traces générales sous double accord. Là où `C27 § 33.10` évoquait `14–30 jours` `[S]`, la norme impose une **purge au plus tard sous** `14 jours`, hors gel légal E : EXIG-OBS-08 E : EXIG-CON-23.

## 8.2 Séparation des trois magasins et journal d’audit chaîné `RFC 8785` (`≥ 24 mois`)

Une trace d’observabilité ne vaut jamais preuve opposable. L’architecture sépare physiquement et administrativement **trois magasins** (volet `3c`, Fig. 7, Ch. 7) :

| Magasin réglementé | Rôle et périmètre d’écriture | Contenu et protection cryptographique | Conservation minimale |
| --- | --- | --- | --- |
| **1. Traces opérationnelles et voûte forensique** (`CAD26 § 10.2`) | Diagnostic continu (`100 %` métadonnées) et enquête ponctuelle. | Spans `OTel v1.41.0` sans contenu (`SHA-256` poivré) E : EXIG-OBS-07 ; voûte isolée sous double accord E : EXIG-OBS-08. | `13 mois` `[S]` (métadonnées) ; `≤ 14 jours` (forensique hors gel). |
| **2. Journal d’audit probatoire chaîné** (`CAD26 § 10.3`, non dérogeable `EXIG-GOV-17`) | Preuve exhaustive écrite **avant relais** de tout `P2`/`P3` en **échec fermé**. | **5 éléments** canonisés `RFC 8785` **(**`JCS`**)**, signés, chaînés (`precedent_sha256`) et **ancrés chaque heure hors domaine** E : EXIG-OBS-11 E : EXIG-OBS-12. | `≥ 24 mois` (`5 ans` bancaire ouvert, `7 ans` plaintes et Organisme canadien de réglementation des investissements, `OCRI`, art. 3803) E : EXIG-OBS-13. |
| **3. Dossier de décision individuelle** (`Loi 25 art. 12.1`, `CAD26 pp. 179–180`) | Droits d’explication, de vérification et de révision humaine. | Magasin chiffré séparé (lié par empreinte) gardant entrées, sorties d’outils et facteurs principaux E : EXIG-CON-09. | `≥ 1 an` après la décision (`Loi 25` art. 12.1). |

Le **journal d’audit probatoire** (`EXIG-OBS-11..13`, non dérogeable `EXIG-GOV-17`, `CAP-049`) exclut tout échantillonnage. S’il est injoignable, la passerelle bloque tout appel `P2`/`P3` (`EXIG-AUT-11`). Chaque entrée réunit **cinq éléments** E : EXIG-OBS-12. Elle scelle le mandant (pseudonyme vers table séparée), l’agent (`id`, `spiffe://`, version, `SHA-256` d’invite) et l’action (outil, version, `definition_sha256`, `arguments_sha256` salé/HMAC, issue). Elle y joint le modèle servi (`gen_ai.response.model`), l’autorité (`jti`, `h`, risque, autonomie, politique), `trace_id`, `a2a_task_id`, `cle_idempotence`, la séquence monotone et `precedent_sha256`.

Canonisée en `RFC 8785` **(**`JCS`**)** et signée hors portée des agents, chaque chaîne publie **chaque heure un point de contrôle hors du domaine d’administration de l’audit**. Cet ancrage recourt à un témoin externe, un arbre `RFC 9162` / `SCITT` ou un stockage `WORM` tiers E : EXIG-OBS-12. Vérifiée **chaque jour** et gardée **au moins** `24 mois` (`5` ou `7 ans` sous `PEX-002` / `PEX-013`, au-delà des 6 mois de `RIA art. 26(6)`), la chaîne s’anonymise en fin de garde par suppression de l’entrée dans la table des pseudonymes du `RPRP`, sans altérer le journal chaîné E : EXIG-OBS-13.

## 8.3 Évaluation continue `E1–E3`, constance `pass^k` et rétrogradation sur dérive SLO

En exploitation, un agent subit **trois dérives** (`C26 § 39.2`, pp. 454–456 : outil, modèle et autonomie ; la mémoire restant un front ouvert en `§ 39.2.4`). `C26 ch. 40` (`Tableau 40.2`, pp. 466–467) les suit par quatre grandeurs `AgentOps` (`[S]`). Contre l’auto-évaluation complaisante (`C27 § 34.3`), le cycle déploie **trois étages (**`E1–E3`**)** (`CAD26 § 10.4`, `C27 ch. 34` `ADR-022`, `DEC-010`) P : CAP-043 P : CAP-044 :

- **Étage** `E1` **— Intégration continue (à chaque modification).** Contrôle déterministe sans LLM des contrats JSON/`MCP`, politiques, non-régression et injection de fautes sur outils et compensations Saga E : EXIG-EVA-01 E : EXIG-ORC-20.
- **Étage** `E2` **— Simulation pré-production et** `pass^k`**.** Avant promotion ou changement (`EXIG-GOV-12`), un jeu versionné d’**au moins** `50` **scénarios** sous `CAD26` E : EXIG-EVA-02 (`≥ 100` sous `PRR O-04` `[S]` de `C27 Annexe G`) tourne sans effet réel. Chaque cas est **joué** `≥ 3` **fois** avec attaques bilingues E : EXIG-EVA-03 E : EXIG-SEC-24. Au lieu de `pass@k`, l’institution exige la **constance** `pass^k` (𝑘≥3 minimal, 𝑘≥5 critique en `C27 § 34.9`), suivie d’un déploiement canari.
- **Étage** `E3` **— Échantillonnage continu sous juge calibré.** Évaluation régulière des exécutions réelles sur la conformité métier E : EXIG-EVA-04 par un juge d’une autre famille, **ré-étalonné sur annotations humaines** contre les biais de verbosité et d’auto-préférence E : EXIG-EVA-05.

Deux horizons gouvernent les droits. En exploitation cible (`PD28`), l’épuisement du budget d’erreur déclenche un repli automatique `< 60 s` vers `N2` ou le flux déterministe P : POR-015. En norme `CAD26`, deux mois hors cible ouvrent une revue, et **trois mois consécutifs hors** `SLO` **imposent l’abaissement d’un niveau d’autonomie et la saisine du comité** E : EXIG-EVA-06.

## 8.4 Gouvernance économique `FinOps` : du jeton trompeur au coût par résultat conforme (`CPO`)

Piloter par le tarif facial du million de jetons aveugle le budget (`C26 ch. 40`, `C27 ch. 40`). Sur un cas d’extraction séquentielle de dépôts `SEC` (`C27 § 40.1, Fig. 52`), **plus de** `97 %` **des jetons facturés viennent de la relecture du contexte**. De son côté, Anthropic (*Hadfield et coll.*, juin 2025) rapporte environ `4×` **plus de jetons** qu’un clavardage pour un agent outillé et `15×` en multiagent (`C26 § 40.5–40.6`, statut « C » ; `CAD26 § 7.1` `[É]`). Si `FOCUS 1.4` (`1.5` annoncée fin 2026, `CAD26 Annexe H.2` p. 338) normalise la facturation, elle ignore la validité métier de l’issue.

Sans avancer de budget fictif, l’AE et l’AS retiennent le **coût complet par résultat conforme (**`CPO`**, *Cost-per-Outcome*)** (`ADR-023`, `PD28 § 24.4`) P : PRI-014 P : CAP-045 P : DEC-011 E : EXIG-FIN-01 E : EXIG-FIN-10 :

CPO = (𝐶inférence + 𝐶outils et crédits SaaS + 𝐶infra et audit + 𝐶échecs et reprises + 𝐶supervision humaine) / 𝑁dossiers conformes terminés et non rouverts

Chaque flux date ses hypothèses tarifaires E : EXIG-FIN-02, convertit les crédits SaaS en devises réelles E : EXIG-FIN-03 et compare son `CPO` à la base non agentique. Cinq verrous brident l’exécution : plafond par tâche vérifié à chaque tour E : EXIG-FIN-04, et quotas mensuels par agent à coupe-circuit gradué (alerte `80 %`, repli ou arrêt à `100 %` hors compensations `EXIG-ORC-17, 28`) E : EXIG-FIN-05. S’y ajoutent le plus petit modèle qualifié en `E2` E : EXIG-FIN-06, les préfixes canoniques `KV-cache` E : EXIG-FIN-07 et le déport des lots différables à `-50 %` (`DEVRAIT`) E : EXIG-FIN-08.

Sur la trajectoire (`DEC-011`), l’affichage transparent (*showback*, `P1`, `POR-004`) précède la **refacturation interne (*chargeback*)** au parrain E : EXIG-FIN-09 en `P2` (`POR-009`). **Tout flux au** `CPO` **déficitaire deux trimestres de suite est déclassé ou reconçu** (`POR-016`, `INI-052`) P : POR-004 P : POR-009 P : POR-016. Le collecteur agrège aussi `kWh` et intensité carbone pour `BSIF B-15` **portée 3** dès 2028 D (`ANC-106`) face au signal `1 700 TWh` en 2035 C : B, C ; SIG-016 P : CAP-046.

Correspondance `ABB → SBB` de l’observabilité, de l’évaluation et du `FinOps` (état au 28 oct.–14 nov. 2026) :

| Domaine d’exploitation | ABB (bloc neutre d’architecture) | SBB substituables (état au 28 oct.–14 nov. 2026) |
| --- | --- | --- |
| Collecte et caviardage PII | Collecteur `OpenTelemetry` épinglé et passerelle de pseudonymisation | OpenTelemetry Collector (`v1.41.0` épinglée), Microsoft Presidio (caviardage sortie) |
| Visualisation traces et `E1–E3` | Plateforme de traces agentiques et harnais d’évaluation `pass^k` | Arize Phoenix, Langfuse, Braintrust, Promptfoo ; agrégateurs APM (Datadog, Dynatrace, Splunk) |
| Comptabilité `FinOps` et coûts | Normalisateur de facturation ouverte et suivi par étiquettes | Export `FOCUS 1.4` natif des fournisseurs infonuagiques, passerelles à compteurs (LiteLLM, Portkey, Helicone) |

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Séparer physiquement et administrativement les trois magasins : télémétrie sans contenu (`≤ 14 jours` en voûte forensique) P : CAP-042 E : EXIG-OBS-07 E : EXIG-OBS-08, journal d’audit inaltérable (`≥ 24 mois`, non dérogeable) P : CAP-049 E : EXIG-OBS-11 E : EXIG-OBS-13 E : EXIG-GOV-17 et dossier `Loi 25 art. 12.1` (`≥ 1 an`) E : EXIG-CON-09.
2. Lier l’autonomie aux `SLO` vérifiés en `E1–E3` (`pass^k`) P : CAP-043 P : CAP-044, en dissociant le repli automatique `< 60 s` sur budget d’erreur P : POR-015 de l’abaissement d’un niveau après trois mois hors cible E : EXIG-EVA-06.
3. Piloter au `CPO` P : PRI-014 P : CAP-045 P : DEC-011 E : EXIG-FIN-01 : affichage transparent en `P1` P : POR-004, refacturation interne et carbone `BSIF B-15` portée 3 en `P2` P : CAP-046 P : POR-009, déclassement après deux trimestres déficitaires P : POR-016.

Spécifications AS

1. Épingler le collecteur `OpenTelemetry v1.41.0` derrière une table de correspondance l’isolant des `85` attributs `gen_ai.*` `Development` du registre `v1.44.0` (`SIG-006`) E : EXIG-OBS-01, propager `W3C Trace Context` sans renseignement personnel (`RP`) en `Baggage` E : EXIG-OBS-02 E : EXIG-OBS-10 et injecter les attributs `Tableau 41` trace ↔ mandat E : EXIG-OBS-03 E : EXIG-OBS-05 E : EXIG-OBS-06.
2. Écrire avant relais `P2`/`P3` (échec fermé) l’audit à cinq éléments canonisé `RFC 8785`, chaîné `SHA-256`, ancré **chaque heure** hors domaine, vérifié chaque jour et anonymisé via la table séparée du `RPRP` E : EXIG-OBS-11 E : EXIG-OBS-12 E : EXIG-OBS-13.
3. Exécuter en CI/CD `E1` et `E2` (`≥ 50` scénarios `CAD26`, `≥ 100` sous `PRR O-04` `[S]`, `× 3` en `pass^k`) P : DEC-010 E : EXIG-EVA-02 E : EXIG-EVA-03, étalonner le juge `E3` E : EXIG-EVA-05, optimiser `KV-cache` et lots `-50 %` (`DEVRAIT`), et armer les disjoncteurs sur `FOCUS 1.4` et crédits SaaS convertis E : EXIG-FIN-03 E : EXIG-FIN-04 E : EXIG-FIN-05 E : EXIG-FIN-07 E : EXIG-FIN-08.

## 8.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Contenu des invites et réponses dans la télémétrie courante | Zéro contenu brut en production ; métadonnées et empreintes `SHA-256` poivrées uniquement E : EXIG-OBS-07 | Diagnostic motivé en coffre forensique isolé sous double accord, purgé au plus tard sous `14 jours` E : EXIG-OBS-08 | `[N]` `Loi 25` (art. 3.5, 12) ; `CAD26` Tableau 10 (p. 33), § 10.2 |
| Preuve d’imputabilité des actions mutatives et sensibles | Journal d’audit séparé à 5 éléments canonisé `RFC 8785`, écrit avant relais en échec fermé, ancré chaque heure à l’externe et gardé `≥ 24 mois` E : EXIG-OBS-11 E : EXIG-OBS-12 E : EXIG-OBS-13 | Jamais pour `P2`/`P3` (non dérogeable E : EXIG-GOV-17) ; rétention portée à `5` ou `7 ans` selon le régime financier P : PEX-002 P : PEX-013 | `[N]` `RIA` art. 12 & 26(6) (`ANC-007`), `OCRI` art. 3803 (courtiers : dossiers 7 ans, Ch. 10) ; `[É]` `CAD26` § 10.3 |
| Instabilité des conventions `OpenTelemetry GenAI` | Épinglage du collecteur `v1.41.0` derrière une table de correspondance face au registre `v1.44.0` E : EXIG-OBS-01 | Adoption directe uniquement après passage officiel des attributs agentiques au statut `Stable` (`SIG-006`) | `[É]` `CAD26` Ann. H.2, `C26` Ann. N.2 (`85` attr. `Development`) ; `S-121` |
| Qualification pré-production d’un agent métier (`E2`) | Constance multi-essais `pass^k` sur `≥ 50` scénarios versionnés (`≥ 100` pour `PRR O-04` `[S]`) exécutés `≥ 3` fois en isolation E : EXIG-EVA-02 E : EXIG-EVA-03 | Jamais de mise en production sur un essai unique ou sur la métrique permissive `pass@k` | `[M]` `C27` ch. 34 § 34.9, ch. 48 § 48.5 ; `[S]` `PRR O-04` ; `PD28` `CAP-043` |
| Unité de pilotage économique et protection budgétaire | Coût complet par résultat conforme non rouvert (`CPO`) assorti de disjoncteurs par tâche et par mois E : EXIG-FIN-01 E : EXIG-FIN-04 E : EXIG-FIN-05 | Jamais de pilotage au seul prix facial du million de jetons (`> 97 %` de relecture sur cas `SEC` ; repère *Hadfield et coll.* `4×` / `15×`, statut « C ») | `[M]` `C27` § 40.1 (Fig. 52 p. 787) ; `[É]` *Hadfield et coll.* (juin 2025, statut « C » en `C26` § 40.5) ; `PD28` `DEC-011` |
| Imputation des coûts d’exploitation aux domaines métiers | Affichage transparent (*showback*) en `P1` puis refacturation interne (*chargeback*) et déclassement après 2 trimestres déficitaires en `P2` P : DEC-011 P : POR-016 | Expérimentations hors production couvertes par une enveloppe d’innovation bornée dans le temps | `[S]` `C27` § 40.2, § 40.10 ; `PD28` M-24 § 24.4, `POR-009` |

## 8.6 Limites et renvois

**Limites et réserves.** Les quatre grandeurs `AgentOps` de `C26 ch. 40` (`Tableau 40.2`, pp. 466–467) relèvent de constructions d’auteur (`[S]`). `C26 ch. 39` (`§ 39.2`, p. 462) analyse trois dérives et laisse la mémoire persistante en front ouvert (`§ 39.2.4`). Les chiffrages fictifs du *Groupe Boréal Inc.* (`C27 § 33.10, 34.12, 40.10`) sont exclus comme preuves. La garde de `13 mois` des métadonnées reste indicative (`[S]`), et `CAD26 EXIG-OBS-08` (`≤ 14 jours`) prime sur `14–30 jours` `[S]` (`C27 § 33.10`). Enfin, les facteurs d’émissions de portée 3 par inférence demeurent partiellement opaques en 2026 (`SIG-109`).

**Renvois aux volumes sources :** `C26` ch. 38 (pp. 442–451, `S-120..124, S-138`), ch. 39 (pp. 451–462), ch. 40 (`Tableau 40.2` pp. 466–467, Anthropic `4×`/`15×` pp. 462–472), Ann. N.2 (pp. 662–668) ; `CAD26` ch. 10 (pp. 171–187, Tableau 41 p. 174, `EXIG-OBS-01..13`, `EXIG-EVA-01..06`, `EXIG-FIN-01..10`), Tableau 10 (p. 33), Ann. H.2 (pp. 336, 338) ; `C27` ch. 33 (pp. 676–700, `ADR-021`), ch. 34 (`pass^k` pp. 701–723, `ADR-022`), ch. 40 (`CPO` pp. 794–816, `ADR-023`), Ann. G (`PRR O-04` p. 1100) ; `PD28` `M-7` (pp. 94–103), `M-24` (pp. 301–309), `CAP-042..046`, `CAP-049`, `DEC-010`, `DEC-011`, `POR-002..004`, `POR-009`, `POR-015`, `POR-016`, `SIG-006`, `SIG-015`, `SIG-016`.
