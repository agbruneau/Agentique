# Chapitre 4 — Sémantique métier, compilation du contexte, mémoire CoALA et encapsulation patrimoniale/OT

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 2, 5, 34, 43 (PC4 [S])]` · `[CAD26 § 5.2 (C5–C6), § 5.5 Fig. 4 & Tab. 13 | PRIN-02, 05, 11 | EXIG-INT-02, 12..14, EXIG-ARC-02, 14..18, 22..25, EXIG-AUT-08, EXIG-SEC-03, 04, EXIG-FIN-07, EXIG-CON-06, 10, EXIG-GOV-15, 16]` · `[C27 § 3.3, ch. 12–15, 25, 28 | ADR-001, ADR-008..010, ADR-016, ADR-017 | PRR S-12, R-01, R-12, R-13, R-14, G-09, G-10, F-13]` · `[PD28 M-4 § 4.5, M-10, M-13 | PRI-008, PRI-010 | CAP-015..021, 024, 025, 028 | DEC-003, 004, 008, 010 | PEX-001, 004, 015, 041 | INI-011, 015, 029 | POR-004, 005, 008 | SIG-103, 106, 109, 110]`.

*Question directrice : Comment alimenter les agents en contexte fiable, gouverner leur mémoire dans la durée et raccorder les systèmes patrimoniaux exacts sans corruption sémantique ni fuite de confidentialité ?*

**Thèse du chapitre :** La validité syntaxique d’un schéma `JSON` n’empêche jamais une erreur sémantique silencieuse. Le meilleur détecteur d’écart d’intention plafonne à `27,9 %` sur exécutions simulées sans vrai modèle en prépublication `[É]`, un seul distracteur dégrade le rappel sur dix-huit modèles et les ontologies en incubation restent immatures fin 2026 (`C27 ch. 12–13`). L’institution doit gouverner définitions et formules dans une couche sémantique déterministe neutre P : PRI-008 P : DEC-003 E : EXIG-INT-02. Elle compile le contexte avec filtrage `ACL` amont sans compte de service P : CAP-017 E : EXIG-ARC-16 et cloisonne les quatre mémoires `CoALA` sous bi-temporalité et purge vérifiable P : CAP-019 P : DEC-004 E : EXIG-ARC-22 E : EXIG-ARC-23 E : EXIG-ARC-25 E : EXIG-CON-10. Enfin, elle protège le patrimoine transactionnel (et, à la marge, les équipements périphériques) derrière une couche anticorruption en `Decimal` exact P : CAP-024 P : CAP-028 P : DEC-008 E : EXIG-ARC-14 E : EXIG-ARC-17.

## 4.1 Erreurs sémantiques silencieuses, tension `ADR-009` et données prêtes (`ACL` amont)

Au-delà des registres de schémas (`C26 § 2.2–2.4`), deux agents partageant un schéma valide peuvent calculer différemment un ratio prudentiel ou une règle d’admissibilité sans lever d’exception (`C27 § 3.3, § 12.1`). Le chapitre 12 de `C27` distingue trois paliers. D’abord, la **couche sémantique analytique déterministe**, centralisant indicateurs et agrégations sans `SQL` libre par le modèle, est mature et rentable. Ensuite, les ontologies formelles et graphes métiers se réservent aux domaines réglementés à fort enjeu (convenance, cloisonnement de groupe, médiation `ISO 20022`). Enfin, la détection automatique d’écart d’intention reste expérimentale : elle plafonne à `27,9 %` **de précision** sur `600` exécutions simulées sans vrai LLM en prépublication (`C27 § 12.6`).

Une dissonance interne du corpus doit ici être tranchée ouvertement. En `C27 § 12.13` (p. 250), l’`ADR-009` (`[S]`, reprise dans `PRR G-09`) écarte la branche `0.3.0.dev0` (impropre à la production, `§ 12.4`) et retient `Apache Ossie` `0.1.1` (format en incubation sans moteur depuis juin 2026). Or l’Extrait 12.1 (p. 240) affiche une version `"1.0.0"` inexistante.

Aussi `PD28 M-13` généralise-t-il `ADR-009` dans `DEC-003`. L’institution exige un référentiel sémantique déclaratif versionné comme du code, indépendant du moteur analytique, avec médiation

canonique et `60 jours` de coexistence (`SIG-110`) P : PRI-008 P : CAP-015 P : CAP-016 P : DEC-003 E : EXIG-INT-02 E : EXIG-INT-13 E : EXIG-INT-14.

En amont, des « données prêtes pour les agents » (`C27 ch. 15`) exigent quatre garanties cumulatives. D’abord, chaque champ, unité et règle de calcul relève d’un propriétaire identifié E : EXIG-INT-12 E : EXIG-INT-19. Ensuite, un sas *Write-Audit-Publish* valide fraîcheur et intégrité statistique avant exposition, au-delà d’un simple `ttlMs` (`C27 § 15.2`, `PRR F-13`) P : CAP-020 P : DEC-010 P : POR-005. Troisièmement, le **filtrage** `ACL` **pré-récupération** s’exécute sous l’identité du mandant propagée dans chaque appel (`ADR-008` maintenue) E : EXIG-ARC-02 E : EXIG-ARC-16. Ses droits forment un plafond strict **sans repli silencieux vers un compte de service**, vérifié par tests actifs sur chaque serveur `MCP` d’entrepôt (`C27 § 15.3–15.4`). Quatrièmement, chaque actif reçoit dès l’ingestion son étiquette immuable d’entité juridique, de finalité consentie et de prohibition inter-filiales P : PRI-010 P : CAP-021 P : PEX-041 E : EXIG-CON-06.

## 4.2 Compilation déterministe du contexte et gouvernance des compétences

Les fenêtres d’**un million de jetons** (mars 2026) n’abolissent ni le pourrissement du contexte (*context rot*), ni la perte au milieu (*lost in the middle*), ni le coût marginal. Un seul distracteur dégrade la performance sur dix-huit modèles (`CAD26 § 5.5`), et plus de `97 %` des jetons facturés d’un flux séquentiel proviennent d’entrées relues (`C27 ch. 40`). L’architecte emploie donc un **compilateur déterministe de contexte** (`ADR-008`) P : CAP-017 :

1. **Stratification fixe pour le** `KV-cache` **:** préfixe invariant en tête (consignes, politiques, schémas épinglés) maximisant la réutilisation du cache, suivi des seules preuves filtrées `ACL` E : EXIG-FIN-07.
2. **Borne de jetons et compaction :** plafond inscrit à la fiche, résumé structuré au-delà et interdiction de l’historique brut comme mémoire longue E : EXIG-ARC-22.
3. **Passage par référence sur** `A2A` **:** jeton de référence vérifiable et sous-contexte minimal plutôt que copie de charges lourdes E : EXIG-ORC-23.

Selon des prépublications non évaluées par les pairs (`SkillsBench` sur `87` tâches et études `AGENTS.md`, `C27 § 13.3–13.4`), le format `Agent Skills` (transféré à l’`AAIF` le 22 oct. 2026) améliore la réussite lorsqu’il est **rédigé et revu par des humains**. À l’inverse, l’autogénération dégrade la qualité, tandis qu’`AGENTS.md` gonfle les jetons sans gain prouvé hors programmation. Toute compétence procédurale est donc versionnée, signée et qualifiée en `CI` P : CAP-018 E : EXIG-INT-15 E : EXIG-INT-16.

## 4.3 Séparation des quatre mémoires `CoALA`, bi-temporalité et oubli sélectif

Selon `CAD26 § 5.5` (`Figure 4`, `Tableau 13`), la mémoire longue est gouvernée **comme une base de données soumise à la Loi 25, jamais comme un cache**. Elle reste **désactivée par défaut** sans besoin inter-sessions prouvé (`C27 ch. 14`) P : DEC-004 E : PRIN-11. Lorsqu’elle est ouverte, les **quatre mémoires** `CoALA` demeurent isolées :

> **[Figure]**
> - Compilation du contexte, 4 mémoires CoALA et couche anticorruption Préfixe KV-cache, filtrage ACL (ARC-16), cloisonnement (ARC-25) et COMP-3
> - Compilateur déterministe de contexte (CAP-017, EXIG-ARC-22)
> - 1. Tête fixe KV-cache : Invites signées & schémas stables (EXIG-FIN-07)
> - 2. Filtrage ACL amont : Droits mandant stricts, zéro compte service (ARC-16)
> - 3. Couche sémantique : Métriques versionnées (DEC-003), zéro SQL libre
> - 4. État borné & réf. : Compaction au seuil · passage par réf. A2A (ORC-23)
> - 4 mémoires CoALA isolées — zéro partage en écriture (EXIG-ARC-25)
> - Travail (CAD26 C2)
> - État hors processus chiffré
> - EXIG-ARC-05, EXIG-ORC-11
> - Procédurale (CAD26 C3)
> - Agent Skills signés (code)
> - Zéro auto-modif. (PC4 [S])
> - Épisodique (CAD26 C5)
> - Résumés typés + TTL
> - Bi-temp. & Loi 25 art. 23
> - Sémantique (CAD26 C5)
> - Index & graphes métier
> - ACL lecture · non fiable
> - Couche anticorruption patrimoniale, CUA borné et sas OT (DEC-008)
> - Adaptateur MCP patrimonial (CAP-024)
> - EBCDIC (CP037/1147) ↔ UTF-8
> - COMP-3 → Decimal exact
> - Zéro flottant IEEE 754
> - Trames COBOL / EDI & lissage
> - CUA interne (CAP-025) & LSAC
> - CUA ≤ 12 m (INI-015) + caviardage • Grattage externe interdit (PEX-001)
> - Sas périphérique OT (CAP-028)
> - Lecture historien / jumeau seul • Zéro écriture OPC UA directe

*Fig. 4. – Architecture des quatre mémoires CoALA, pipeline déterministe de compilation du contexte (KV-cache, ACL amont) et couche anticorruption patrimoniale (EBCDIC/COMP-3 Decimal exact) et périphérique OT.*

- **Mémoire de travail (**`CAD26` **C2) :** état et sous-objectifs persistés hors processus à chaque transition dans un magasin chiffré E : EXIG-ARC-05 E : EXIG-ARC-06 E : EXIG-ORC-11.
- **Mémoire épisodique (**`CAD26` **C5) :** résumés structurés horodatés (zéro transcription brute), isolés **par locataire, mandant et serveur** `MCP`, avec expiration par entrée E : EXIG-ARC-22 E : EXIG-ARC-23.
- **Mémoire sémantique (**`CAD26` **C5) :** index hybrides et graphes métiers filtrés `ACL` en lecture et expirant avec la source E : EXIG-ARC-16 E : EXIG-ARC-23.
- **Mémoire procédurale (**`CAD26` **C3) :** invites système et `Agent Skills` signés sans aucune modification autonome en production (`PC4` `[S]`) P : CAP-018 E : EXIG-ARC-24.

Contre l’empoisonnement mémoriel (`OWASP ASI06`, `C26 S-069` ; `C27 § 14.5`), **aucun magasin de mémoire longue n’est partagé en écriture** entre agents ou serveurs `MCP` E : EXIG-ARC-25. Chaque écriture épisodique valide un schéma excluant le texte brut externe et propage l’étiquette « contenu non fiable ». Tout souvenir relu demeure incapable d’autoriser seul une action sensible E : EXIG-SEC-03 E : EXIG-SEC-04. Enfin, un **graphe bi-temporel** dissocie validité métier (`valid_from` / `valid_to`) et ingestion système. Il reconstitue l’état exact connu lors d’une décision sous `BSIF E-23`, tout en assurant la **destruction ou l’anonymisation sélective vérifiable** exigée par l’**article 23 de la Loi 25** (`C27 § 14.6`) sans briser les index adjacents P : CAP-019 P : DEC-004 P : POR-005 E : EXIG-CON-10.

## 4.4 Couche anticorruption patrimoniale (`COMP-3`, `CUA`) et frontière périphérique (`OT`)

L’accès aux grands livres bancaires et moteurs actuariels interdit `SQL` direct et virgule flottante approximative (`C27 ch. 25` ; `ADR-001, ADR-016`). Le cœur transactionnel reste protégé derrière des serveurs `MCP` **anticorruption** lissant les rafales pour préserver quotas `MIPS`, files et verrous centraux P : CAP-024 P : DEC-008 P : INI-011 E : EXIG-ARC-14 E : EXIG-ARC-17. Hors modèle, ces adaptateurs exécutent trois conversions déterministes. Ils assurent le transcodage exact `EBCDIC` (`CP037` ou `CP1147`) ↔ `UTF-8`. Ils convertissent sans perte les décimaux condensés `Packed Decimal` **(**`COMP-3`**)** vers `Decimal` **exact** ou entiers d’unités mineures, **excluant** `IEEE 754` P : CAP-024 P : PEX-015 E : EXIG-AUT-08. Ils alignent enfin les trames fixes (`COMMAREA`, *copybooks* `COBOL`/`RPG`) et `EDI X12`/`EDIFACT`, avec clé d’idempotence vérifiée en cible et référence de trace (`EXIG-ARC-18`, `DEVRAIT`) E : EXIG-ARC-18.

Les *Computer-Use Agents* (`CUA`, `C27 § 25.8` `[S]`, `PRR R-12`) sont voués à l’extinction. À l’externe, le grattage d’écran réutilisant l’authentifiant client tombe sous `LSAC art. 171` (`SIG-103`) P : PEX-001. À l’interne (`3270`/`5250`), seule une **dérogation temporaire** est admise sous caviardage des `RP` avant capture, zones interdites, double assertion visuelle et **extinction sous 12 mois** vers `MCP` (zéro dérogation à `POR-008`) P : CAP-025 P : DEC-008 P : INI-015 P : POR-004 P : POR-008 E : EXIG-GOV-15 E : EXIG-GOV-16.

**Frontière périphérique** `OT` **(hors cœur financier).** Cette capacité reste marginale dans le secteur bancaire et assurantiel (`C27 ch. 28`, `ADR-017`, prototypes sans essai réel). Elle vise uniquement la télématique d’indemnisation, les succursales physiques ou les filiales d’actifs industriels. `CAP-028` cantonne tout pont `MCP` devant `OPC UA` (`IEC 62541`, serveur `v2.0.2`), `AAS` ou `MQTT Sparkplug` à trois verrous : lecture seule sur réplica isolé (`IEC 62443`), zéro écriture ni réessai vers un automate (`PLC`/`SCADA`), et validation sur jumeau déterministe plus approbation hors bande (`SIG-109`) P : CAP-028 P : INI-029 E : EXIG-AUT-09 E : EXIG-AUT-11 E : EXIG-ORC-27.

Exemples non limitatifs `ABB → SBB` des Couches `C3` et `C4` (état au 28 oct.–14 nov. 2026) :

| Domaine | Bloc neutre (`ABB`) | Exemples de `SBB` substituables (état au 28 oct.–14 nov. 2026) |
| --- | --- | --- |
| Mémoire longue | Graphe bi-temporel isolé par locataire | Letta, Graphiti (Zep), PostgreSQL + pgvector partitionné |
| Recherche filtrée | Index hybride à filtrage `ACL` amont | OpenSearch, Qdrant, Milvus (identité propagée du mandant) |
| Patrimoine central | Adaptateur `EBCDIC` / `COMP-3` vers `MCP` | Passerelles internes Decimal exact devant CICS, IMS ou IBM i |

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Gouverner indicateurs et règles métiers comme du code dans une couche sémantique neutre sans couplage à une ontologie en incubation (`SIG-110`) P : PRI-008 P : CAP-015 P : DEC-003 E : EXIG-INT-02.
2. Désactiver par défaut la mémoire inter-sessions ; exiger bi-temporalité (`BSIF E-23`) et purge sélective vérifiable (`Loi 25 art. 23`) avant ouverture P : CAP-019 P : DEC-004 P : POR-005 E : EXIG-CON-10.
3. Proscrire le grattage externe et borner tout `CUA` interne par un budget d’extinction à **12 mois** P : CAP-025 P : DEC-008 P : PEX-001 P : INI-015 P : POR-004 E : EXIG-GOV-16.

Spécifications AS

1. Compiler le contexte en strates fixes (`KV-cache`), filtrer les `ACL` en amont sans compte de service, borner les jetons et passer par référence sur `A2A` P : CAP-017 E : EXIG-ARC-16 E : EXIG-ARC-22 E : EXIG-FIN-07 E : EXIG-ORC-23.
2. Cloisonner les quatre mémoires `CoALA` (zéro écriture partagée), valider les schémas anti-`ASI06` et signer les `Agent Skills` rédigés par humains P : CAP-018 E : EXIG-ARC-23 E : EXIG-ARC-24 E : EXIG-ARC-25 E : EXIG-SEC-04.
3. Exécuter hors modèle transcodage `EBCDIC`, décimaux `COMP-3` en `Decimal` exact et trames `COBOL`/`EDI`, et interposer réplica isolé plus jumeau numérique devant `OPC UA` P : CAP-024 P : CAP-028 E : EXIG-ARC-14 E : EXIG-ARC-17 E : EXIG-AUT-08 E : EXIG-AUT-11.

## 4.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Calcul de ratios financiers, actuariels ou d’admissibilité | Résolution déterministe via couche sémantique versionnée exposée par outil borné, zéro `SQL` libre P : CAP-015 P : DEC-003 | Exploration hors production dans un bac à sable analytique sur données synthétiques | `[É]` `C27` § 12.1–12.6 (prépublication simulée à `27,9 %`) ; `CAD26` `EXIG-INT-02` |
| Contrôle d’accès lors de la récupération documentaire | Filtrage `ACL` pré-récupération sous l’identité du mandant, zéro repli vers compte de service E : EXIG-ARC-16 | Corpus intégralement public classé `P0` sans renseignement personnel ni secret d’affaires | `[N]` `[É]` `Loi 25` ; `CAD26` `EXIG-ARC-16` ; `C27` § 15.3 (`ADR-008`) |
| Persistance d’une mémoire longue entre sessions | Mémoire inter-sessions désactivée ; état limité à la tâche durable en cours P : DEC-004 | Besoin longitudinal prouvé, sous schéma validé, isolation locataire/mandant, bi-temporalité et purge E : EXIG-ARC-23 E : EXIG-CON-10 | `[N]` `[É]` `Loi 25` art. 23 ; `CAD26` § 5.5 (`CoALA`) |
| Évolution de la mémoire procédurale (`Agent Skills`, invites) | Paquets rédigés par humains, versionnés, signés et qualifiés en intégration continue P : CAP-018 E : EXIG-ARC-24 | Jamais d’auto-modification en production ni d’autogénération non revue (`PC4` `[S]`, dégradation mesurée) | `[É]` `[S]` `C27` § 13.3–13.4 (prépublications) ; `C26` ch. 43 (`PC4` `[S]`) |
| Raccordement d’un système central patrimonial sans API REST | Serveur `MCP` anticorruption (`EBCDIC`, `COMP-3` en `Decimal` exact, lissage de charge) P : CAP-024 | Harnais `CUA` dérogatoire sous caviardage des `RP`, double assertion visuelle et extinction à `12 mois` P : INI-015 | `[É]` `[S]` `C27` § 25.4–25.8 (`[S]`) ; `CAD26` `EXIG-AUT-08` |
| Interaction avec capteurs ou automates industriels (`OT`) | Lecture seule sur réplica isolé ; jumeau numérique déterministe et approbation humaine avant consigne P : CAP-028 | Jamais d’écriture directe ni de réessai automatique d’un modèle vers un automate (`ADR-017`) | `[S]` `C27` § 28.4–28.5 (réserve prototypes) |

## 4.6 Limites et renvois

- **Coquille** `CAD26`**, dissonance** `ADR-009` **et cas fictif exclu.** `CAD26` (pp. 258, 342) porte la coquille `EXIG-MEM-01` au lieu d’`EXIG-ARC-22` (p. 47). `ADR-009` (épinglant en `C27` p. 250 `Apache Ossie` `0.1.1` en incubation sans moteur, face à l’Extrait 12.1 p. 240 en `"1.0.0"` et à `0.3.0.dev0` impropre à la production en `§ 12.4`, et reprise en `PRR G-09`) est généralisée par `DEC-003`. Les chiffres fictifs du *Groupe Boréal Inc.* (`C27 § 14.10, 25.10, 28.10`) sont exclus comme sans valeur probante.
- **Textes** `statut F` **et réserve** `OT`**.** `FDX`, `ACORD` et `CSIO` restent au `statut F` (`PD28 M-4 § 4.5`, aucun `[N]`), et les ponts `MCP`/`OPC UA` (`ADR-017`) n’ont pas d’essai indépendant sur équipement réel.
- **Renvois aux 4 PDF :** `C26` ch. 2, 5, 34, 43 (`PC4` `[S]`) ; `CAD26` § 5.2 (C5–C6), § 5.5 ; `C27` § 3.3, ch. 12–15, 25, 28 ; `PD28` `M-4` § 4.5, `M-10`, `M-13`.
