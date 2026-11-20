# Chapitre 5 — Orchestration hybride (OO1–OO4, 8 patrons), exécution durable, sagas et sémantique d’effet

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 1 (§ 1.5.2, § 1.6.2.2), ch. 22, ch. 29 (§ 29.4.1), ch. 31, ch. 48]` · `[CAD26 ch. 5 (§ 5.2), ch. 7 | EXIG-ORC-01 à EXIG-ORC-30 | PRIN-05, PRIN-08, PRIN-12]` · `[C27 ch. 16 à ch. 21 | ADR-002, ADR-011, ADR-012, ADR-013 | PRR R-02, R-03, R-04, R-06, R-07, R-08, R-10, R-11, R-15, O-06, S-04, S-14]` · `[PD28 M-9, M-10, M-13 | PRI-002, PRI-009 | CAP-007 à CAP-011 | DEC-005 | POR-003, POR-006 | SIG-013, SIG-014, SIG-104]`.

*Question directrice : Comment confiner le raisonnement probabiliste dans une enveloppe déterministe qui garantit la reprise sur panne, la compensation métier et l’intégrité des effets sur le monde réel ?*

**Thèse du chapitre :** Les évaluations empiriques montrent que les topologies multiagents ouvertes multiplient les pannes sans gain moyen sur les tâches séquentielles couplées (`[M]`). Un moteur durable garantit la reprise du programme, mais jamais l’unicité de ses effets externes (`[É]`). En milieu réglementé, l’inférence doit être confinée dans des machines à états déterministes (`OO3` ou `OO4`) choisies parmi huit patrons homologués à profondeur bornée P : PRI-002 P : CAP-007 P : CAP-010 E : EXIG-ORC-01 E : EXIG-ORC-02 E : EXIG-ORC-04 . Chaque mutation exige une clé d’idempotence dérivée de l’étape durable et une revalidation au réveil. Sur plusieurs systèmes, elle impose une Saga à point pivot dotée d’un canal de compensation dédié isolé du coupe-circuit P : PRI-009 P : CAP-008 P : CAP-009 P : DEC-005 E : EXIG-ORC-12 E : EXIG-ORC-17 E : EXIG-ORC-21 E : EXIG-ORC-28 .

## 5.1 Du continuum OO1–OO4 au test de bascule réglementaire : localiser la main qui commande

Opposer flux programmé rigide et nuée d’agents autonomes fausse le problème architectural (`C26 ch. 22 § 22.1`). Un agent peut appeler un sous-flux déterministe ou une table *Decision Model and Notation* (`DMN`) ; une machine à états peut invoquer un agent comme activité bornée. Les régimes se séparent non par la capacité du modèle, mais par deux axes de contrôle : *qui détient la représentation explicite du processus*, et *qui commande l’ordre des transitions*.

La taxonomie `OO1–OO4` de l’`Agentic Process Management` (`APM`, `C26 ch. 22 § 22.1`, prépublications `S-034` du 12 avril 2026 et `S-035` du 30 juin 2026) croise ces deux axes (5e colonne : transposition normative ajoutée par le mémoire aux quatre colonnes de `C26 Tableau 22.1`) :

| Option (`C26 Tableau 22.1`) | Connaissance du processus | Commandement de l’enchaînement | Lisibilité avant exécution (`[S]`) | Usage admissible *(ajout du mémoire)* |
| --- | --- | --- | --- | --- |
| `OO1` — Agentique agnostique au processus | Aucun composant explicite | Les agents (émergence) | Nulle (observable après coup dans les traces) | Exploratoire hors production uniquement |
| `OO2` — Agentique consciente d’un cadre | Les agents (invite ou contexte) | Les agents (planificateur) | Descriptive sans force exécutoire | Lecture interne consultative (`Classe 1` / `N1`) |
| `OO3` — Processus invoquant des agents agnostiques | Le cadre déterministe seul | Le cadre d’orchestration | Enchaînement complet auditable | Régime par défaut des flux audités (`Classes 2–5`) |
| `OO4` — Explicite d’agents conscients du processus | Le cadre et les agents | Le cadre d’orchestration | Enchaînement complet + contexte d’étape | Flux complexes exigeant arbitrage local éclairé |

Sur ce continuum exposé à la dérive, `C26 ch. 22` établit **une seule discontinuité structurante : la bascule** `OO2 → OO3`. En `OO1`–`OO2`, le processus reste une consigne textuelle tributaire du modèle et vulnérable aux entrées ambiguës ou injections. En `OO3`–`OO4`, le moteur déterministe reprend l’enchaînement : l’agent raisonne dans sa cellule sans négocier la transition P : PRI-002 P : CAP-007 E : EXIG-ARC-07 .

`C26 ch. 29` (`§ 29.4`, `§ 29.4.1`) relie cette coupure au droit canadien. Sous l’article 12.1 de la Loi 25, `BSIF E-23` (1er mai 2027 D , `ANC-103`) et la ligne directrice `AMF IA` (1er mai 2027 D , `C26 Annexe N.3`), l’exploitant répond seul du résultat sans pouvoir invoquer l’émergence ni le fournisseur. Le test de `C26 § 29.4.1` (`[S]`) pose **trois conditions cumulatives** :

1. **Un texte opposable en nomme le résultat** : octroi, refus, communication ou écriture imposés envers une personne ou un livre réglementé (obligation en « doit » sous l’article 12.1, étendue aux attentes prudentielles `E-23` et `AMF IA`).
2. **Une trace est exigible par un tiers** : client, régulateur ou tribunal peut réclamer le chemin ayant produit l’issue (`PC2`), imposant la reproductibilité.
3. **L’écart n’est pas réparable par simple reprise** : rejouer la tâche n’efface pas le dommage financier ou juridique (`C26 ch. 31`).

Dès ces trois conditions réunies, `OO1` et `OO2` cèdent obligatoirement à `OO3` ou `OO4`, au coût assumé d’expliciter le processus P : PRI-002 P : CAP-007 E : EXIG-ORC-01 .

## 5.2 Catalogue fermé des topologies autorisées (8 patrons + 1 variante) et proscription des antipatrons

Les mesures de `C27 ch. 16` (`§ 16.7`, Kim et coll.), `ch. 21` (`§ 21.1`) et `ch. 48` (`§ 48.4`) réfutent le réflexe multiagent. Sur six bancs, le gain face à un agent unique varie de `+80,8 %` (sous-tâches parallélisables) à `-70,0 %` (tâches séquentielles couplées), soit `-0,3 %` en moyenne. Cet écart s’efface à calcul égal sur les modèles frontières récents. La loi de Lusser pénalise les chaînes non vérifiées (0,9410 ≈53,9 %). De même, la taxonomie `MAST` (`C27 § 21.1` : `1 642` traces en `v3`, `14` modes, `41 %` à `86,7 %` d’échecs) répartit les pannes entre conception (`44,2 %` en `v3` ; `41,77 %` en `v2`), désalignement (`32,4 %` ; `36,94 %`) et vérification (`23,5 %` ; `21,30 %`).

`CAD26 ch. 7` (`§ 7.2`, Tableau 24) et `PD28` (`CAP-010`, `ADR-002`, `ADR-011`) limitent donc la conception à **huit patrons autorisés et une variante encadrée**, inscrits au registre P : CAP-010 E : EXIG-ORC-03 :

1. **Flux déterministe à étapes agentiques (défaut)** : graphe déterministe invoquant des cellules typées validées par schéma à chaque sortie E : EXIG-ORC-01 E : EXIG-ORC-24 .
2. **Chaîne séquentielle** : pipeline linéaire de transformations typées sous délais bornés par maillon.
3. **Routage et transfert (**`handoff`**)** : aiguillage vers une liste fermée de spécialistes sans historique brut ni boucle libre, par contexte structuré et références E : EXIG-ORC-23 .
4. **Parallélisation** : sectionnement ou vote (jusqu’à `-90 %` de délai en recherche complexe au prix d’une multiplication linéaire des jetons, `CAD26 p. 101`), sous concurrence bornée, **écrivain unique** et attente de tout garde-fou parallèle E : EXIG-ORC-07 .
5. **Orchestrateur et exécutants** : planification plafonnée à **deux niveaux de délégation** (deux sauts / trois agents maximum, voire un seul saut inter-organisations, `CAD26 p. 101`), bloquée au-delà via `RFC 8693` E : EXIG-ORC-04 (`PRR R-04`, `PRR S-04`).
6. **Évaluateur-optimiseur** : contrôles déterministes exécutés *d’abord*, critique à famille ou invite distincte, et arrêt à `≤ 3` **itérations** avec escalade humaine E : EXIG-ORC-05 .
7. **Chorégraphie événementielle** : domaines faiblement couplés à fort volume, sous propriétaire nommé, contrats `CloudEvents 1.0` / `AsyncAPI 3.0` sans renseignement personnel en attribut, `xagentmaxhops = 4` (`CAD26 § 6.7`, `C27 § 19.9` `[S]`) et Saga sur écritures multisystèmes P : CAP-011 P : CAP-012 E : EXIG-ORC-08 E : EXIG-EVT-06 .

8. **Agent unique outillé (base obligatoire)** : étalon préalable au multiagent ; l’AS corrige d’abord la surcharge d’outils (alerte `> 15` sous `EXIG-ORC-09`, cible `≤ 15` outils `[S]` d’`ADR-005`) et ne découpe sur gain mesuré que selon les **frontières de contexte et de sécurité** (`DEVRAIT`) E : EXIG-ORC-02 E : EXIG-ORC-09 E : EXIG-ORC-10 .

- **Variante — Clavardage de groupe et débat** : `≤ 3` **agents participants** plus un gestionnaire hors décompte, plafond de tours et clôture explicite E : EXIG-ORC-06 , contre les maillages libres et *Mind Viruses* (Papadopoulos et coll., août 2026, `CAD26 p. 101`).

Symétriquement, `CAD26 § 7.9` (Tableau 26) interdit **dix antipatrons** E : EXIG-ORC-29 . Sont proscrits : le multiagent sans gain mesuré, les rôles génériques, le flux connu laissé au modèle (ou inconnu figé), l’état mutable concurrent et la latence multisaut ignorée. Sont aussi bannis : l’historique brut injecté, l’état en mémoire vive, le maillage libre, les écritures sans idempotence ni compensation et le vérificateur complaisant. Chaque agent réapplique son filtrage de sécurité E : EXIG-ORC-25 .

## 5.3 Exécution durable vs sémantique d’effet : reprise du programme, idempotence et revalidation au réveil

Sur les tâches longues, l’état est persisté hors processus à chaque transition P : CAP-008 E : EXIG-ARC-05 E : EXIG-ORC-11 . Or `C27 ch. 18` et `C26 ch. 48` rappellent qu’**un moteur durable garantit la reprise du programme, jamais l’unicité de ses effets externes**. Par le *problème des deux généraux* (`C26 § 1.5.2, § 48.1`), le traitement *exactement-une-fois* requiert une livraison *au-moins-une-fois* vers un **outil cible idempotent**. En `MCP 2026-07-28`, un réessai après coupure reçoit d’ailleurs un nouvel identifiant JSON-RPC (`C27 § 18.1`). `C26 Tableau 48.1` (`[S]`) distingue ainsi **Lecture** (coût et fraîcheur), **Écriture** (doublon destructeur sans déduplication cible, `C26 § 48.2`) et **Engagement** (acte irréversible hors défaite locale).

Deux mécanismes sectoriels montrent l’absence de couture native (`C26 § 48.5`, `C27 § 18.3`). En HTTP, `draft-ietf-httpapi-idempotency-key-header` (`Idempotency-Key`) — expiré en `-07` le 18 avril 2026 (`C26 § 48.5`) puis repris en `-08` le 22 octobre 2026 (`C27 ch. 18`) — spécifie `409`, `422` et `400` sans être RFC. En paiement, l’`UETR` (`UUID` v4 `RFC 4122` / `RFC 9562`), obligatoire sur `ISO 20022` `pacs.008`, `pacs.009` et `pacs.004`, trace le règlement interbancaire. Toutefois, il ne **relie pas le message à l’appel d’outil de l’agent** (`C26 § 48.5`, degré 3 sur `MCP`, `A2A`, `AP2`).

L’AS ferme cet écart par quatre verrous durables P : CAP-008 P : CAP-009 P : DEC-005 :

1. **Appel LLM journalisé comme effet de bord (𝑆𝑘= 𝑓(𝐻𝑘)).** Le code d’orchestration reste déterministe (sans réseau, horloge ni aléa directs). Inférences et outils sont isolés en activités journalisées et relus au rejeu sans réinterroger le modèle E : EXIG-ORC-11 E : EXIG-ORC-12 (`PRR R-02`). Le magasin est chiffré par dossier (effacement Loi 25), compacté (*Continue-As-New*) et versionné (`Build IDs`) avec tests de migration d’état (`DEVRAIT`) E : EXIG-ARC-06 E : EXIG-ORC-13 E : EXIG-ORC-14 .
2. **Clé d’idempotence dérivée de l’opération racine durable.** Jamais produite par le modèle ni par concaténation, la clé suit `RFC 8785` : `cle = hex(SHA-256(JCS(["idem-v1", task_id, step_id])))` (racine aléatoire `UUIDv4`, chemin d’étape et itération), transite via `Idempotency-Key` ou champ contractuel, et est dédupliquée atomiquement par la cible E : EXIG-ORC-21 E : EXIG-ORC-22 (`PRR R-03`) ; sinon, l’outil bascule en `P3` sans réessai automatique E : EXIG-AUT-08 .
3. **Revalidation au réveil (**`awakeable` **/ écart *Time-of-Check to Time-of-Use*,** `TOCTOU`**) et minuteries parallèles.** La veille libère le calcul (`C27 § 18.6`). Sur un octroi hypothécaire ou sinistre étalé sur des semaines sous `BSIF E-23`, chaque pièce suit sa minuterie durable de péremption (taux, revenu, sanctions, `C27 § 18.12` `[S]`). Au réveil avant décaissement, un validateur hors agent revérifie les droits actifs du signataire et relit l’état frais du système maître (statut, gel antifraude, plafond) P : CAP-008 E : EXIG-AUT-17 (`PRR R-08`).

4. **Classification des fautes, repli testé et façade cognitive.** Les erreurs définitives (politique, schéma, mandat révoqué) sont séparées des pannes transitoires sous disjoncteur et repli testé — modèle homologué ou file humaine sous droits du mandant E : EXIG-ORC-27 (`PRR R-11`). Les cadriciels cognitifs (cycle 12–18 mois, `C27 ch. 20`) prouvent reprise et audit sur banc avant catalogage E : EXIG-ORC-30 .

| Bloc neutre (`ABB`) | Fonction exigée | Exemples de `SBB` substituables (état au 28 oct.–14 nov. 2026) | Vigilance d’ingénierie (`C27 ch. 18–20`, `CAD26 § 7.10`) |
| --- | --- | --- | --- |
| **Moteur durable (cycles longs)** | Journal rejoué, minuteries longues, versionnage en vol | `Temporal` | Borner `maximumAttempts` (illimité par défaut) ; tests de rejeu CI |
| **Micro-orchestration durable** | Objets virtuels sérialisés, `awakeables` sans serveur | `Restate`, `DBOS`, `Durable Functions`, `AWS Step Functions` | Évaluer l’adhérence infonuagique ou le plafond `PostgreSQL` (`DBOS`) |
| **Graphe cognitif intra-activité** | Cellule agentique bornée appelée dans une étape durable | `LangGraph`, `Microsoft Agent Framework`, `Google ADK`, `AutoGen`, `CrewAI` | Persistance mémoire vive proscrite ; isoler derrière façade (cycle 12–18 mois) |
| **Courtier de chorégraphie** | Enveloppes `CloudEvents` / `AsyncAPI`, rejeu isolé | `Apache Kafka`, `Solace PubSub+`, `Apache Pulsar` | Déduplication obligatoire sur le système d’enregistrement aval |

## 5.4 Patron Saga à point pivot, tampon d’irréversibilité et canal de compensation dédié

Sans transaction `ACID` inter-progiciels, toute mutation touchant plusieurs systèmes d’enregistrement suit obligatoirement une **Saga** (Garcia-Molina et Salem, 1987 ; `SagaLLM`, `C27 § 18.4` ; `C26 § 48.3` ; `CAD26 § 7.5`) P : PRI-009 P : CAP-009 P : DEC-005 E : EXIG-ORC-15 (`PRR R-06`).

> **[Figure]**
> - Enveloppe durable OO3/OO4 [S], point pivot Saga & canal EXIG-ORC-28 Confinement déterministe, idempotence JCS et compensation isolée du coupe-circuit
> - Enveloppe durable OO3 / OO4 [S] — État hors processus (EXIG-ORC-11..13)
> - OO1/OO2 [S] exclus (C26 § 29.4.1) · Clé SHA-256(JCS) côté cible (ORC-21..22)
> - 1. Réversible (P2)
> - Sceller C1 journal
> - Cellule bornée + K1
> - 2. Réversible (P2)
> - Sceller C2 journal
> - ≤ 2 sauts / ≤ 3 itér.
> - Veille (PC3 [S])
> - Attente hors proc.
> - Revalid. (CAP-008)
> - Journal Saga ajout seul (ORC-16)
> - • Compensations [C1, C2] scellées
> - AVANT l’exécution de T1 et T2
> - • Paramètres résolus et h(JCS)
> - → Alimente le canal EXIG-ORC-28
> - PIVOT
> - Engagement post-pivot (P3 / Cl. 4)
> - • Acte irréversible (pacs.008)
> - • Après validations & CIBA lié
> - • Tampon de grâce si applicable
> - • Zéro annulation automatique
> - Canal de compensation dédié (EXIG-ORC-28) — reste OUVERT sous arrêt
> - • Identité propre orchestrateur (≠ NHI agent) · budget réservé isolé
> - • Limité aux seuls outils de compensation C2 → C1 inscrits au journal
> - • Idempotence vérifiée (EXIG-ORC-17) · tests injection de fautes en CI
> - Coupe-circuit (< 10 s [S], POR-003)
> - • Bloque le NHI de l’agent
> - • Stoppe tout appel vers l’avant
> - • Exercice trim. ≤ 15 min (SEC-26)
> - File humaine prioritaire (ORC-18)
> - • Escalade après 2 échecs
> - de compensation Saga
> - • Audit JCS & reprise manuelle

*Fig. 5. – Enveloppe d’orchestration durable OO3/OO4 autour de cellules agentiques bornées, séquence Saga à journal préalable, point pivot d’irréversibilité et canal de compensation dédié isolé du coupe-circuit.*

L’ordonnancement s’articule autour d’un **point pivot** (`C27 § 18.7`) :

- **Avant le pivot (étapes compensables)** : avant d’exécuter chaque action 𝑇𝑖, l’orchestrateur consigne dans un **journal de compensation en ajout seul** l’outil inverse 𝐶𝑖 et ses arguments résolus E : EXIG-ORC-16 . Aucun modèle ne sachant improviser une annulation sûre (`C26 § 48.3`), la compensation est fournie par le propriétaire de l’outil au catalogue, **idempotente**, et annule *sémantiquement* l’effet par écriture comptable inverse de 𝐶𝑘−1 à 𝐶1 après réessais bornés à temporisation exponentielle et gigue E : EXIG-ORC-17 E : EXIG-ORC-27 (`PRR R-10`). **Après deux échecs d’une compensation**, le dossier bascule en file humaine prioritaire E : EXIG-ORC-18 . Les états intermédiaires étant visibles hors isolation `ACID`, des réservations sémantiques et des tests d’injection de fautes en CI sont requis avant `POR-003` P : POR-003 E : EXIG-ORC-19 E : EXIG-ORC-20 (`PRR R-15`).

- **Au pivot et en aval** : l’acte irréversible (`P3` / `Classe 4`) est retardé par pré-engagement (*réserver avant capture*, *Write-Audit-Publish*, tampon d’annulation `pacs.008` P : PEX-004 , `PRR R-07`), franchi uniquement sous approbation hors bande journalisée, puis suivi des seules étapes réessayables idempotentes.

Enfin, `CAD26 § 7.8` résout par le couplage de `EXIG-ORC-17` et `EXIG-ORC-28` le conflit entre arrêt d’urgence et intégrité comptable. Chaque tâche porte des plafonds d’étapes, d’appels, de jetons, de coût et de durée E : EXIG-ORC-26 . Elle dispose aussi d’un coupe-circuit exercé chaque trimestre (`< 10 s` `[S]` côté passerelle sous `POR-003` et `PRR S-14`, contre `15 min` global en `CAD26`) P : POR-003 P : POR-006 E : EXIG-IAM-20 E : EXIG-ORC-28 E : EXIG-SEC-26 . L’arrêt agit **vers l’avant** : il bloque toute nouvelle étape de l’agent, tout en laissant ouvert un **canal de compensation dédié**. Ce canal opère sous une **identité non humaine propre à l’orchestrateur**, distincte de l’identité révoquée de l’agent. La passerelle le restreint aux seuls outils compensatoires inscrits au journal (`EXIG-ORC-16`) sur une **réserve budgétaire hors enveloppe**. Il résiste ainsi au coupe-circuit, au plafond de sauts et à l’échéance du mandat — sauf suspension motivée et journalisée visant l’orchestrateur lui-même E : EXIG-ORC-17 E : EXIG-ORC-26 E : EXIG-ORC-28 .

Contrat schématique AS d’enveloppe `CloudEvents 1.0` et d’entrée de journal Saga avec canal de compensation dédié (`EXIG-EVT-06`, `EXIG-ORC-16`, `EXIG-ORC-21`, `EXIG-ORC-28`) :

```
{
  "specversion": "1.0",
  "id": "evt-7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "source": "spiffe://corp.example/ns/orch/sa/saga-engine",
  "type": "ca.fin.saga.step.sealed.v1",
  "time": "2026-11-19T14:20:00Z",
  "xagentmaxhops": 4,
  "data": {
    "task_id": "550e8400-e29b-41d4-a716-446655440000",
    "step_id": "T2-reserve-funds",
    "idempotency_key": "hex(SHA-256(JCS([\"idem-v1\", task_id, step_id])))",
    "pivot_reached": false,
    "compensation": {
      "channel_identity": "spiffe://corp.example/ns/orch/sa/saga-compensator",
      "tool_id": "finance.ledger.release_hold",
      "max_attempts": 2,
      "escalation_queue": "ops.human.priority.saga"
    }
  }
}
```

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. **Imposer** `OO3`**/**`OO4` **:** Interdire `OO1`, `OO2` et les dix antipatrons dès que le test à trois conditions de `C26 § 29.4.1` (`[S]`) est vérifié P : PRI-002 P : CAP-007 E : EXIG-ORC-01 E : EXIG-ORC-29 .
2. **Borner les topologies :** Exiger un gain mesuré face à l’agent unique avant tout multiagent ; limiter la délégation à `≤ 2` niveaux et l’évaluateur à `≤ 3` tours P : CAP-010 E : EXIG-ORC-02 E : EXIG-ORC-04 E : EXIG-ORC-05 .
3. **Exiger la preuve trimestrielle :** Subordonner `POR-003` et `POR-006` à l’injection de fautes Saga et au test trimestriel du coupe-circuit validant le canal dédié P : PRI-009 P : POR-003 P : POR-006 E : EXIG-ORC-20 E : EXIG-ORC-28 .

Spécifications AS

1. **Journaliser hors processus :** Exécuter sur moteur durable chiffré, enregistrer chaque appel LLM comme effet de bord non rejoué et revalider droits et état au réveil d’un `awakeable` P : CAP-008 P : DEC-005 E : EXIG-ARC-05 E : EXIG-ORC-11 E : EXIG-ORC-12 E : EXIG-ORC-13 E : EXIG-AUT-17 .
2. **Dédupliquer de bout en bout :** Calculer hors modèle `cle = hex(SHA-256(JCS(["idem-v1", task_id, step_id])))` (`RFC 8785`, `UUIDv4`), transmettre `Idempotency-Key` et contrôler sa déduplication atomique côté cible P : CAP-009 E : EXIG-ORC-21 E : EXIG-ORC-22 .
3. **Câbler Saga et canal dédié :** Tenir le journal en ajout seul avant action, isoler le canal de compensation sous identité et réserve propres à l’orchestrateur, et escalader après `2` échecs E : EXIG-ORC-15 E : EXIG-ORC-16 E : EXIG-ORC-17 E : EXIG-ORC-18 E : EXIG-ORC-26 E : EXIG-ORC-28 .

## 5.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Régime d’orchestration d’un processus audité | Machine à états déterministe invoquant des cellules agentiques typées (`OO3` ou `OO4`, patron 1) P : PRI-002 | Sous-tâches inconnues d’avance à risque faible, sous patron orchestrateur-exécutants à `≤ 2` niveaux E : EXIG-ORC-04 | `[M]` `MAST` (`C27` § 21.1) ; `[S]` `C26` § 22.1, § 29.4.1 |
| Passage de l’agent unique au multiagent | Agent unique doté de `≤ 15` outils `[S]` (`ADR-005`, alerte dès `> 15` sous `EXIG-ORC-09`) et contexte compilé (patron 8) E : EXIG-ORC-02 E : EXIG-ORC-09 | Gain mesuré sur le jeu interne ou séparation stricte de domaines de sécurité (`DEVRAIT`) E : EXIG-ORC-10 | `[M]` `C27` § 16.7 (`-70 %` à `+80,8 %`), § 48.4 ; `[S]` `ADR-005` |
| Persistance d’état et appels au modèle | Moteur durable externe persistant chaque transition et journalisant chaque inférence comme effet de bord E : EXIG-ORC-11 E : EXIG-ORC-12 | Requête consultative synchrone en un tour sans écriture ni attente (`Classe 1` / `N1`) | `[É]` `CAD26` § 7.4 ; `C27` ch. 18 (`DEC-005`) |
| Non-duplication des écritures à la reprise | Clé d’idempotence `JCS` dérivée de l’étape durable (`Idempotency-Key`) et dédupliquée par la cible E : EXIG-ORC-21 E : EXIG-ORC-22 | Jamais : tout outil mutatif sans déduplication vérifiée est classé `P3` E : EXIG-AUT-08 | `[M]` Deux généraux (`C26` § 1.5.2, § 48.1) ; `[É]` `RFC 8785` |
| Mutations sur plusieurs systèmes centraux | Patron Saga à point pivot, journal préalable en ajout seul et escalade après `2` échecs E : EXIG-ORC-15 E : EXIG-ORC-16 E : EXIG-ORC-18 | Écriture atomique dans un seul système d’enregistrement doté d’une transaction locale | `[É]` `CAD26` § 7.5 ; `C27` § 18.4 ; `PD28` `CAP-009` |
| Sagas en vol lors d’un coupe-circuit | Blocage vers l’avant de l’agent et compensations via canal dédié sous identité d’orchestrateur E : EXIG-ORC-17 E : EXIG-ORC-28 | Suspension motivée et journalisée de l’orchestrateur lui-même si celui-ci est compromis | `[S]` `CAD26` `PRIN-12`, § 7.8 ; `[N]` `BSIF` E-23 (`ANC-103`) |

## 5.6 Limites et renvois au corpus

- **Prépublications et constructions** `[S]` **:** le manifeste `APM` (`S-034`), la classification `OO1–OO4` (`S-035`) et `SagaLLM` (`C27 ch. 18`) sont des prépublications non révisées par les pairs ; le test à trois conditions (`C26 § 29.4.1`), le Tableau 48.1 (*Lecture / Écriture / Engagement*) et le canal de compensation dédié (`CAD26 § 7.8`) relèvent de constructions d’auteur (`[S]`).
- **Brouillons et sources secondaires :** `draft-ietf-httpapi-idempotency-key-header` (expiré en `-07` le 18 avril 2026, repris en `-08` le 22 octobre 2026) n’est pas une RFC ; Garcia-Molina et Salem (1987) est cité via `SagaLLM`, l’article *Nexus* (2026) est non exploité, et aucun banc indépendant ne compare les moteurs durables sous charge agentique.
- **Angles morts de degré 3 (**`C26 § 48.2–48.5`**) :** ni `MCP`, ni `A2A`, ni `AP2` ne déclarent l’idempotence d’un outil ni ne relient nativement un appel d’agent à un `UETR` `ISO 20022` ; le consensus inter-organisations sous fautes byzantines reste hors périmètre protocolaire (traité par rapprochement tripartite au Chapitre 9).
- **Renvois aux 4 PDF :** `C26` ch. 1 (§ 1.5.2, § 1.6.2.2), ch. 22 (pp. 254–268), ch. 29 (§ 29.4 pp. 337–339), ch. 48 (pp. 544–551) ; `CAD26` ch. 7 (pp. 98–118) ; `C27` ch. 16–21 (pp. 313–455) ; `PD28` M-9, M-10 (`CAP-007..011`) et M-13 (`DEC-005`).
