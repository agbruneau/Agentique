# Chapitre 3 — Couche protocolaire (MCP, A2A, événements), passerelle à neuf contrôles et anti-verrouillage

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 7–11, 37, 42, Ann. B, Ann. N.2]` · `[CAD26 ch. 6, § 8.1 Tab. 28, § 9.4 Fig. 18, § 11.7, Ann. H.2 & H.4 | PRIN-01, PRIN-02 | EXIG-ARC-01, 11, 21, EXIG-INT-01..23, EXIG-MCP-01..22, EXIG-A2A-01..15, EXIG-EVT-01..10, EXIG-AUT-08..14, EXIG-IAM-17..19, EXIG-SEC-03..06, EXIG-GOV-18..20]` · `[C27 ch. 5–11, 19, 24, 26–27, § 49.7 | ADR-004..007, ADR-019 | PRR S-06..08, R-04, R-05, R-09]` · `[PD28 M-4, M-11, M-13 | PRI-003, PRI-015 | CAP-001, 006, 011..013, 022, 023, 026, 027 | DEC-001, 002, 007 | ANC-024..029, ANC-104 | SIG-004, 005, 008]`.

*Question directrice : Comment connecter agents, outils et bus événementiels sur des standards ouverts sans confondre connectivité syntaxique et gouvernance sécurisée ?*

**Thèse du chapitre :** La convergence de 2026 sur `MCP`, `A2A` et `CloudEvents` résout l’échange syntaxique, mais ne fonde aucune gouvernance sécurisée. Le corpus relève `102` fiches `NVD` mentionnant « Model Context Protocol » en quatre mois (serveurs tiers, sous réserves méthodologiques) `[É]`. Il note aussi l’absence d’expiration et de révocation natives des cartes `A2A 1.0`, et `0/15` lien documenté `[S]` avec cinq cadres financiers canadiens (`C26 ch. 42`). La sûreté n’étant pas composable sur le fil, l’entreprise applique la non-substituabilité protocolaire P : PRI-003 et réserve l’approbation au catalogue interne E : EXIG-INT-17. Elle impose une passerelle bidirectionnelle à neuf contrôles en échec fermé P : CAP-022 E : EXIG-ARC-01 E : EXIG-IAM-17 et confine les suites commerciales derrière des adaptateurs réversibles P : DEC-001 P : DEC-002 P : DEC-007.

## 3.1 Loi de non-substituabilité et pile protocolaire épinglée

L’erreur fréquente des pilotes consiste à confondre l’invocation d’une fonction déterministe et la délégation à un pair autonome. Le corpus tranche par le contrôle de l’appelant et l’opacité de l’exécutant (`CAD26 § 6.2–6.4` ; `C27 § 6.6, § 11.12` `[S]`, `ADR-001`). Un agent pair doté d’état propre ne se déguise pas en outil CRUD (`EXIG-INT-05`, `DEVRAIT`), et une API transactionnelle ne s’invoque pas par dialogue libre P : PRI-003 E : PRIN-01 E : PRIN-02 E : EXIG-INT-04 E : EXIG-INT-05 E : EXIG-INT-10. Trois plans non substituables structurent la Couche `C4` (`acces`).

**Intégration verticale agent-outil (**`MCP` **révision** `2026-07-28`**).** L’accès synchrone aux outils et données internes s’appuie sur `MCP` épinglé à `2026-07-28` sur `Streamable HTTP` (`CAD26 § 6.5` ; `C27 ch. 5` ; *« HTTP diffusable à point unique »* en `C26 § 8.1.3`). Sans état au transport, le serveur se route derrière un répartiteur standard. Le transport `stdio` reste confiné au poste local sans secret de production E : EXIG-MCP-01 E : EXIG-MCP-08. Contre la saturation du miroir REST `1:1`, l’architecte consolide `≤ 15` outils `[S]` d’intention métier par serveur (`C27 § 5.11`, `ADR-005`). Il mesure la précision dès l’alerte d’orchestrateur `> 15` outils avant tout découpage multiagent P : CAP-023 E : EXIG-MCP-06 E : EXIG-ORC-09.

L’autorisation devient obligatoire sur chaque serveur, sans relais de jeton (*token passthrough*) ni secret en en-tête, avec concordance entre en-têtes HTTP et corps `JSON-RPC` E : EXIG-MCP-09 E : EXIG-MCP-11 E : EXIG-MCP-15 E : EXIG-MCP-18. Annotations (`readOnlyHint`, `destructiveHint`), schémas, URL et icônes sont tenus pour non fiables. Chaque outil est épinglé par empreinte `SHA-256` contre le *rug-pull* P : CAP-023 E : EXIG-MCP-14 E : EXIG-MCP-19 E : EXIG-MCP-20 E : EXIG-AUT-08. L’*elicitation* ne recueille ni secret ni approbation E : EXIG-MCP-21. Les extensions `Beta` au 1er novembre 2026 — `Tasks` (`SEP-3392` du 29 oct. 2026, sans remplacer un moteur durable selon `CAD26 § 6.5` et `C26 § 48.2`), `Skills` et `Server Cards` — restent désactivées hors liste blanche E : EXIG-MCP-04. Côté calendrier (`CAD26 Annexe H.2` ; `C26 Annexe N.2`), la migration intégrale vers `2026-07-28` échoit le **28 juillet 2027** D E : EXIG-MCP-22. `SEP-3398` (27 oct. 2026) fixe la révision suivante au **30 mars 2027** A (à confirmer, `C26 [AN-5]`). Enfin, `SEP-2596` (3 juin 2026) ouvre le retrait de `HTTP+SSE` dès mars 2027 (préavis 12 mois, `≥ 90 jours` sur faille active), puis de `Roots`, `Sampling` et `DCR` en septembre 2027 sous la borne du 22 août 2027 A (`ANC-026`, `SIG-005`).

**Délégation horizontale inter-agents (**`A2A` **version** `1.0`**).** Entre domaines ou organisations vers un pair opaque, la référence demeure `A2A v1.0.1` du 28 mai 2026 (`1.0.0` du 12 mars 2026 ayant absorbé `ACP` ; `v1.1.0-rc` du 29 oct. 2026 non publiée, `CAD26 Annexe H.2`). Hébergé par l’`AAIF` au stade `Growth` (août 2026, `C26 S-002`), le projet compte **neuf sièges** au comité technique depuis l’entrée de Bloomberg le 20 octobre 2026 (`CAD26 Annexe H.4` n° 1).

Or l’inspection de `A2A 1.0` (`C26 S-047..S-058`) montre que la signature `JWS` canonisée `RFC 8785` (`JCS`) de l’*Agent Card* est facultative (`S-050`). Le protocole ne prévoit ni expiration ou statut natifs (`S-049`, `S-051`), ni révocation (`S-052`, `S-056`), ni gouvernance de clés dans `SECURITY.md` (`S-054`). Le cadre impose donc vérification `JWS`/`JCS` systématique, inscription au catalogue à cache borné, rejet des champs hors norme et garde anti-`SSRF` sur les notifications poussées P : CAP-012 P : DEC-001 E : EXIG-A2A-01 E : EXIG-A2A-02 E : EXIG-A2A-03 E : EXIG-A2A-04 E : EXIG-A2A-05 E : EXIG-A2A-06 E : EXIG-A2A-12. La suite `a2a-tck` étant en `1.0.0.alpha3` (20 oct. 2026), seuls ses tests stables sur deux versions bloquent la `CI` E : EXIG-A2A-14 E : EXIG-INT-19 E : EXIG-GOV-19.

**Dorsale événementielle (**`CloudEvents 1.0` **et** `AsyncAPI 3.0`**).** Le découplage multi-consommateurs emploie `CloudEvents` (`1.0.2`) et `AsyncAPI` (`3.1.0`) au catalogue (`CAD26 § 6.7` ; `C27 ch. 19` ; `EXIG-EVT-01`, `DEVRAIT`) P : CAP-011 E : EXIG-EVT-01 E : EXIG-EVT-02 E : EXIG-EVT-03 E : EXIG-EVT-04. L’enveloppe exclut tout `RP` en attribut E : EXIG-EVT-05 et porte un compteur anti-boucle obligatoire (`xagentmaxhops = 4`, `CAD26 § 6.7`, `C27 § 19.9` `[S]`) P : CAP-012 E : EXIG-EVT-06. Identité cryptographique, déduplication aval, clé de partition et rejeu isolé complètent le contrat E : EXIG-EVT-07 E : EXIG-EVT-08 E : EXIG-EVT-09 E : EXIG-EVT-10.

## 3.2 Asymétrie réglementaire (`0/15`), surface NVD et registre interne à quatre opérations

La compatibilité de transport ne crée aucune confiance (`C26 ch. 11`). Du 1er juillet au 27 octobre 2026, la `NVD` compte `102` **fiches citant « Model Context Protocol »** (`13` de score `≥ 9,0`), sous trois réserves (`C27 § 49.7`, `ADR-019`). La requête omet le sigle `MCP` seul et inclut des non-serveurs ; le pic de septembre (`56` fiches) peut refléter une campagne d’audit ; enfin, ces failles touchent des serveurs tiers plutôt que la spécification. De plus, la moitié des connecteurs publics sont mutables ou sans valeur (`C27 § 8.8`). Le registre officiel `MCP` (`v1.8.7`, 30 oct. 2026) reste en préversion sans serveurs privés (`CAD26 Annexe H.2`).

Surtout, la matrice `C26 ch. 42` (`Tableau 42.1` `[S]`) croise `MCP`, `A2A v1.0` et `AP2` avec cinq cadres canadiens (`BSIF E-23`, `AMF IA`, `ACVM 11-348`, `Loi 25 art. 12.1`, accès bancaire ouvert). Elle relève `0/15` **lien documenté** `[S]` (`4` absences en source, `11` au socle). Les protocoles traitent `Q-A` (*qui parle* `[S]`), tandis que le droit exige `Q-E` (*qui en répond*, `C26 ch. 14` `[S]`). Cinq **zones de compensation (`Z1` à `Z5`, `[S]`)** comblent l’écart : `Z1` trace d’instance ; `Z2` arrêt humain suspensif ; `Z3` blocage d’auto-modification ; `Z4` abstraction bancaire ouverte (`ANC-104`, `C26 S-033`) P : CAP-026 ; `Z5` filtrage par le maillage.

La découverte sépare quatre opérations (`C27 § 8.1` ; `CAD26 § 6.8`) : *trouver*, *décrire*, *authentifier* et **approuver**. Cette quatrième opération relève du seul **registre et catalogue interne** P : CAP-047 E : EXIG-INT-17 E : EXIG-GOV-08. Ce catalogue est révisé chaque trimestre, ou sous 15 jours ouvrables en cas de version incompatible, dépréciation, retrait accéléré ou correctif de sécurité E : EXIG-GOV-18. Il classe chaque protocole sous cinq statuts avec **60 jours** de coexistence minimale E : EXIG-INT-14 E : EXIG-GOV-19 E : EXIG-GOV-20. Le statut `Adopter` exige six critères cumulatifs : spécification publique versionnée avec politique de dépréciation, gouvernance neutre ou multipartite, statut final ou stable, au moins deux implémentations indépendantes ou une suite de tests `CI`, modèle de sécurité compatible avec le chapitre 9, et licence ouverte sans redevance. Les quatre autres statuts cadrent les pilotes bornés (`Évaluer`), la veille sans données réelles (`Surveiller`), l’adaptateur à retrait planifié (`Contenir`) et l’arrêt immédiat (`Suspendu`). Aucun brouillon n’est assimilé à une norme : au 1er novembre 2026, la proposition n° 57 sur `AGNTCY` reste sans décision (`CAD26 Annexe H.2`), et le transfert `AP2` / `Verifiable Intent` vers *FIDO Alliance* annoncé le 28 avril 2026 demeure non matérialisé (`C26 S-090, S-091`) E : EXIG-INT-09 E : EXIG-INT-20 E : EXIG-INT-21.

## 3.3 Passerelle d’agents bidirectionnelle (`PEP`) à neuf contrôles ordonnés

Tout appel `MCP`, délégation `A2A` et action `P2`/`P3` franchissent une **passerelle d’agents** (`PEP` bidirectionnel en échec fermé, `CAD26 § 9.4 Figure 18` ; `C26 ch. 37` ; `C27 ch. 24`) P : CAP-022 E : EXIG-ARC-01 E : EXIG-ARC-11 E : EXIG-IAM-17 E : EXIG-IAM-18, hors fonction locale `P0`/`P1` de même domaine au catalogue.

> **[Figure]**
> - Passerelle d’agents (PEP) à 9 contrôles et séparation protocolaire Chemin obligé en échec fermé (EXIG-IAM-17..18), règle de deux et retrait SEC-06
> - Cellule appelante
> - SPIFFE SVID + sub/act
> - Modèle sans clés (IAM-06)
> - Catalogue interne
> - 4e op. : approuver
> - SHA-256 & paliers P0–P3
> - PDP & Approbation
> - Politique hors modèle
> - h=SHA-256(JCS) · <10 s [S]
> - Passerelle d’agents — PEP bidirectionnel en échec fermé (EXIG-IAM-17)
> - ALLER · Contrôles 1 à 7 avant relais
> - (1) AuthN SVID/mTLS & débit (2) Catalogue & SHA-256
> - (3) AuthZ & paliers P0–P3 (4) Schéma & anti-injection
> - (5) Jeton h = SHA-256(JCS) (6) Quotas & budget tâche
> - (7) Échange RFC 8693 aud. unique · zéro relais de jeton (EXIG-IAM-12)
> - + Pré-audit d’intention écrit AVANT relais P2/P3 (EXIG-OBS-11)
> - RETOUR · Contrôles 8 et 9 avant remise au contexte
> - (8) Masquage RP/PII & retrait déterministe EXIG-SEC-06
> - (9) Span OpenTelemetry & issue au journal d’audit JCS
> - MCP 2026-07-28
> - HTTP sans état · ≤ 15 [S]
> - Prod ≤ juill. 27 · SEP-3398
> - A2A 1.0 (1.0.1)
> - AAIF · Tâches opaques
> - Agent Card JWS/JCS
> - CloudEvents 1.0
> - AsyncAPI · maxhops = 4
> - Zéro RP · EXIG-EVT-07
> - Règle de deux (EXIG-SEC-04) & retrait anti-exfiltration (EXIG-SEC-06)
> - [A] Entrée non fiable (web, courriel, tiers) + [B] Accès privé/sensible
> - → Action PEP immédiate : retrait outils d’envoi (même P0) et tout P3
> - Marquage propagé sur toute la session · non dérogeable (GOV-17)

*Fig. 3. – Passerelle d’agents bidirectionnelle (PEP) à neuf contrôles ordonnés en échec fermé, séparation des flux MCP, A2A et CloudEvents/AsyncAPI, règle de deux et retrait déterministe EXIG-SEC-06.*

Les **neuf contrôles ordonnés** s’appliquent sans exception :

1. **Authentification et débit (aller, 1) :** validation du *SPIFFE Verifiable Identity Document* (`SVID`) sur `TLS` mutuel (`mTLS`), du jeton délégué à preuve de possession (`cnf`) et limitation de cadence E : EXIG-IAM-01 E : EXIG-IAM-03 E : EXIG-IAM-14.
2. **Catalogue et empreinte (aller, 2) :** statut `Adopter`/`Évaluer`, version et condensat `SHA-256` épinglé E : EXIG-INT-17 E : EXIG-MCP-20.
3. **Autorisation hors modèle (aller, 3) :** intersection déterministe des droits, niveau `N1–N4` et palier `P0–P3` P : CAP-037 E : EXIG-IAM-21 E : EXIG-AUT-10.
4. **Garde-fous d’entrée (aller, 4) :** schéma `I-JSON`, en-têtes `MCP`, balisage et détection d’injection — qui ne suffit jamais comme seul contrôle et exige un banc bilingue français/anglais E : EXIG-MCP-15 E : EXIG-SEC-03 E : EXIG-SEC-05.

5. **Jeton d’approbation lié (aller, 5) :** jeton signé `≤ 15 min` (`jti` unique) lié à `h = SHA-256(JCS(...))` — exigé hors bande (appareil et session distincts) sur tout `P3` E : EXIG-AUT-09 et via `CIBA` sans UI (`EXIG-AUT-14`, `DEVRAIT`), le même appareil restant admis en `N2` sur `P2` (`CAD26 Tableau 28`, p. 119) E : EXIG-AUT-11 E : EXIG-AUT-12 E : EXIG-AUT-14.
6. **Quotas et budget (aller, 6) :** budget financier, jetons et profondeur de sauts E : EXIG-FIN-04 E : EXIG-ORC-26.
7. **Injection aval et pré-audit (aller, 7) :** échange `RFC 8693` à audience unique (`RFC 8707`) injectant les secrets hors du *modèle sans clés* (`EXIG-IAM-19`, `DEVRAIT`), et écriture d’audit d’intention *avant* relais `P2`/`P3` P : CAP-036 E : EXIG-IAM-11 E : EXIG-IAM-19 E : EXIG-SEC-14 E : EXIG-OBS-11.
8. **Filtrage retour et règle de deux (retour, 8) :** masquage des secrets et `RP`, balisage non fiable et **retrait déterministe des outils d’envoi et** `P3` pour la session dès exposition combinée à du contenu non fiable et à des actifs sensibles P : CAP-038 E : EXIG-SEC-04 E : EXIG-SEC-06.
9. **Télémétrie et audit chaîné (retour, 9) :** segment `OpenTelemetry` sans contenu brut et scellement de l’issue, incluant les requêtes à allers-retours multiples (*Multi Round-Trip Requests*, `MRTR`, `SEP-2322`), `Tasks` `> 5 s` (`CAD26 § 6.5`) et tâches `A2A` (`C27 § 6.3`) P : CAP-042 E : EXIG-OBS-01 E : EXIG-OBS-07.

Correspondance non prescriptive `ABB → SBB` (état au 28 oct.–14 nov. 2026) :

| Fonction (`C4`) | Bloc neutre (`ABB`) | Exemples de `SBB` substituables (état au 28 oct.–14 nov. 2026) |
| --- | --- | --- |
| Coupure `PEP` | Passerelle d’agents bidirectionnelle | agentgateway, Envoy AI Gateway, Kong AI Gateway, IBM ContextForge |
| Décision `PDP` | Moteur de politiques hors modèle | Open Policy Agent (OPA), Cedar |
| Flux asynchrones | Courtier `CloudEvents 1.0` / `AsyncAPI 3.0` | Apache Kafka, Solace PubSub+, Apache Pulsar |

### 3.3.1 Budget de latence cumulé des neuf contrôles `PEP` et contrat schématique AS (`[S]`)

L’empilement des neuf contrôles en échec fermé introduit un surcoût de latence que l’AS doit budgéter dès la conception (`[S]`, cibles d’ingénierie à étalonner sur banc interne avant `POR-003`). Le tableau ci-dessous ventile l’enveloppe synchrone aller-retour hors temps d’inférence du modèle (`~400–2 500 ms`) et hors attente humaine `CIBA` :

| Étape de la traversée `PEP` | Contrôle exécuté | Budget cible `p50` (`[S]`) | Budget cible `p95` (`[S]`) | Levier de maîtrise AS |
| --- | --- | --- | --- | --- |
| **Contrôles 1–2 (aller)** | `mTLS`/`SVID`, cache catalogue & `SHA-256` | `3 ms` | `8 ms` | Cache local `JWKS` + condensats en mémoire |
| **Contrôles 3–4 (aller)** | Décision `PDP`, validation `I-JSON` & garde anti-injection | `6 ms` | `18 ms` | Règles compilées + filtre lexical avant classifieur |
| **Contrôles 5–6 (aller)** | Vérification `jti`/`h = SHA-256(JCS)` & quotas tâche | `4 ms` | `12 ms` | Magasin atomique régional (`jti` en mémoire) |
| **Contrôle 7 + pré-audit** | Échange `RFC 8693` + `DPoP` & écriture `EXIG-OBS-11` | `14 ms` | `38 ms` | Cache jeton `aud` court + journalisation asynchrone sur `P0`/`P1`, synchrone sur `P2`/`P3` |
| **Contrôles 8–9 (retour)** | Masquage `RP`, retrait `EXIG-SEC-06`, span `OTel` & issue `JCS` | `8 ms` | `22 ms` | Automate déterministe + pipeline `OTel` hors chemin critique |
| **Cumul synchrone** `PEP` **(**`P2`**/**`P3`**)** | **9 contrôles + pré-audit bloquant (hors LLM / CIBA)** | `~35 ms` | `~98 ms` | **Surcoût** `< 5 %` **face à un appel modèle (étalonné ci-dessous)** |

**Étalonnage exécutable *Borealis-Bench* (**`W3.1`**, licence MIT — évaluation artificielle FEDS).** Le banc reproductible `Borealis-Bench/` (`gateway-go` + `crypto-rust`, `results/SYNTHESE-BENCH.md`) valide ce budget par deux campagnes locales :

- **Campagne 1 (**`campagne1_pep_latence.json`**) :** sur `2 000` requêtes en processus Go traversant les `9` contrôles en échec fermé, la latence cumulée s’établit à `p50 = 52,85 µs`, `p95 = 202,83 µs` et `p99 = 234,06 µs` (max `255,94 µs`, `C6` filtre `CaMeL` à `64,01 µs` moy.). Bout en bout sur `1 000` requêtes HTTP/TCP locales, la latence reste à `p50 = 59,09 µs`, `p95 = 1,01 ms` et `p99 = 3,52 ms`, très en deçà du budget cible (`~35 ms` `p50`). Le coupe-circuit `POR-003` (`10` exercices concurrents) coupe les mutations en `0,050 ms` **max** (cible `< 10 s` `[S]`), avec `0` fuite et `10/10` compensations préservées.
- **Campagne 3 (**`campagne3_mcp_a2a_interop.json`**) :** trois adaptateurs ouverts (`LangGraph`, `AutoGen`, `CrewAI`) réussissent `9/9` **(**`100 %`**)** scénarios `MCP JSON-RPC 2.0` + `A2A v1.0` (`18,92–90,55 ms`), et l’audit CI (`ci-audit-108-blocs/registre-108-blocs.json`) classe `100 %` des `108` blocs `C27` (`90` `[Exécuté en CI]`, `18` `[Schéma conceptuel]`) et `8` contrats `CAD26` Annexe C (`6`/`2`). L’extension `CRE-IA-2027` **v2.0** (`exigences-v2.json`) consacre ce harnais CI `MCP`/`A2A`, la bascule `SEP-3398`/`SEP-2596` (2027) et le resserrement calibré `≤ 10–12` outils `[S]` en `L3/L4`.

Contrat schématique neutre d’épinglage d’outil `MCP` et d’enveloppe d’appel `PEP` (`EXIG-MCP-20`, `EXIG-IAM-17`, sans dépendance fournisseur) :

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "mcp_version": "2026-07-28",
  "tool_id": "finance.ledger.post_entry",
  "tool_version": "2.4.0",
  "definition_digest": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "catalogue_status": "Adopter",
  "palier_effet": "P2",
  "idempotent_verified": true,
  "pep_envelope": {
    "spiffe_svid": "spiffe://corp.example/ns/fin/sa/agent-compta",
    "delegated_sub": "pseudonyme:rprp-88412",
    "audience": "https://mcp-ledger.internal/v2",
    "idempotency_key": "sha256-jcs-idem-v1",
    "rule_of_two_tainted": false
  }
}
```

## 3.4 Confinement anti-verrouillage multi-plateformes et interfaces périphériques

Les suites d’entreprise (`C27 ch. 26–27` ; `CAD26 § 13.1`) demeurent **« ouvertes sur le fil et fermées sur le plan de contrôle »**. Elles enferment identités, politiques, traces et facturation dans leur silo. L’AE préserve donc le noyau possédé et cantonne tout agent SaaS sous les **contrôles compensatoires de** `EXIG-ARC-21` *(corrigeant la coquille* `EXIG-ARC-02` *de* `CAD26` *pp. 195–257)*. Ce régime exige transit par la passerelle vers tout autre domaine, identité dédiée, exportation `OpenTelemetry`, arrêt propre testé chaque trimestre et plafond `N2` sans approbation équivalente à `JCS` P : PRI-015 P : CAP-013 P : DEC-007 E : EXIG-ARC-19 E : EXIG-ARC-21.

En Couche `C1`, `AG-UI` reste confiné aux pilotes derrière adaptateur (`Évaluer`). En production, un flux `SSE` structuré projette des états typés sur un **catalogue fermé de composants pré-homologués**, sans `HTML` ni `JavaScript` libre (`C27 ch. 7, 10`) P : CAP-001 P : DEC-002 E : EXIG-ARC-03. Sur le web ouvert (`C27 ch. 9`), `97 %` des `llms.txt` ne reçoivent aucune requête (Ahrefs) et `WebMCP` demeure expérimental. `Web Bot Auth` n’atteste ni intention ni délégant, ce qui exige un canal chiffré mutuel sans privilège implicite P : CAP-006 E : EXIG-A2A-09. Les groupes IETF `DAWN` (`ANC-025, 027, 028` A) et `AGENTPROTO` (`ANC-024, 029` A, 2027–2028) guident la veille (`SIG-004`, `SIG-008`) vers d’éventuels connecteurs fédérés vers 2033 C : A, C ; SIG-004, SIG-008 P : CAP-027.

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Tenir le catalogue trimestriel à cinq statuts (`Adopter` à `Suspendu`), proscrire l’assimilation d’un brouillon à une norme et exiger `60 jours` de coexistence E : EXIG-INT-09 E : EXIG-INT-14 E : EXIG-GOV-18 E : EXIG-GOV-19.
2. Imposer registre interne et passerelle `PEP` sur tout flux `MCP`/`A2A`, avec migration `MCP` avant le **28 juillet 2027** D sous veille du **30 mars 2027** A (`SIG-005`) P : PRI-003 P : CAP-022 E : EXIG-ARC-01 E : EXIG-INT-17 E : EXIG-MCP-22.
3. Confiner les agents SaaS sous contrôles compensatoires trimestriels et isoler interfaces et annuaires derrière adaptateurs réversibles P : PRI-015 P : CAP-013 P : DEC-001 P : DEC-002 P : DEC-007 E : EXIG-ARC-21.

Spécifications AS

1. Exécuter en échec fermé les **neuf contrôles** de la passerelle `PEP` (`CAD26 Figure 18`), zéro relais de jeton, injection aval (`EXIG-IAM-19`, `DEVRAIT`), pré-audit et retrait `P3`/sortie sous règle de deux E : EXIG-IAM-12 E : EXIG-IAM-17 E : EXIG-IAM-18 E : EXIG-IAM-19 E : EXIG-SEC-06 E : EXIG-OBS-11.
2. Déployer `MCP 2026-07-28` sans état (`Streamable HTTP`), `≤ 15` outils `[S]` épinglés `SHA-256` (`ADR-005` ; alerte `> 15` sous `EXIG-ORC-09`), annotations non fiables P : CAP-023 E : EXIG-MCP-01 E : EXIG-MCP-06 E : EXIG-MCP-11 E : EXIG-MCP-14 E : EXIG-MCP-20 E : EXIG-ORC-09.
3. Vérifier `JWS`/`JCS` et le cache catalogue des cartes `A2A v1.0.1`, et imposer `xagentmaxhops = 4` sans `RP` sur `CloudEvents 1.0` / `AsyncAPI 3.0` P : CAP-011 P : CAP-012 E : EXIG-A2A-02 E : EXIG-A2A-03 E : EXIG-EVT-05 E : EXIG-EVT-06.

## 3.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Accès vertical aux outils et données métiers | `MCP 2026-07-28` sans état sur `Streamable HTTP` derrière passerelle `PEP`, `≤ 15` outils `[S]` d’intention métier E : EXIG-MCP-01 E : EXIG-MCP-06 | Fonction locale `P0`/`P1` dans la même unité de déploiement et le même domaine, inscrite au catalogue E : EXIG-IAM-17 | `[É]` `[S]` `CAD26` § 6.5 ; `C27` ch. 5 (`ADR-005` `[S]`) |
| Délégation horizontale entre agents distincts | `A2A 1.0` (`1.0.1`) avec cartes signées `JWS`/`JCS` vérifiées, inscrites au catalogue interne et tâches corrélées P : DEC-001 E : EXIG-A2A-01 E : EXIG-A2A-03 | Sous-agents internes à un même processus durable sans franchissement de domaine ni d’équipe (`CAD26` § 7.2) | `[É]` `CAD26` § 6.6 ; `C26` `S-002, S-047..S-058` |
| Découplage événementiel inter-domaines | Appel synchrone ou tâche durable par défaut ; `CloudEvents 1.0` + `AsyncAPI 3.0` borné par `xagentmaxhops = 4` si multi-consommateurs P : CAP-011 | Jamais sans enveloppe validée, compteur anti-boucle E : EXIG-EVT-06 ni Saga sur effets multisystèmes E : EXIG-ORC-08 | `[É]` `[S]` `CAD26` § 6.7 ; `C27` § 19.7–19.9 (`[S]`) |
| Approbation des outils et pairs externes | Catalogue interne unique épinglant versions, condensats `SHA-256` et paliers `P0–P3` après revue sécurité E : EXIG-INT-17 E : EXIG-MCP-20 | Jamais : ni registre public en préversion ni annotations déclarées par un serveur ne font foi E : EXIG-AUT-08 | `[É]` `C27` § 8.8, § 49.7 (`102` fiches `NVD` tiers, avec réserves) |
| Rendu d’interfaces dynamiques vers l’humain | Flux `SSE` typé projeté sur catalogue fermé de composants pré-homologués, zéro code exécutable généré P : CAP-001 P : DEC-002 | Pilote interne isolé sans données réelles évaluant un protocole émergent derrière adaptateur (`Évaluer`) E : EXIG-GOV-18 | `[É]` `C27` § 7.1, § 10.9 ; `CAD26` `EXIG-ARC-03` |
| Annuaires fédérés ou paiement agentique en incubation | Statut `Surveiller` hors production ou `Évaluer` derrière adaptateur réversible sans couplage du noyau E : EXIG-GOV-20 | Passage à `Adopter` après ratification stable, gouvernance multipartite vérifiée et conformité mature E : EXIG-GOV-19 | `[É]` `C26` Ann. N.2 (`S-091`) ; `CAD26` `EXIG-INT-20, EXIG-INT-21` |

## 3.6 Limites et renvois

- **Preuves de production et constructions (**`[S]`**).** Fin 2026, nulle étude évaluée par les pairs ne mesure `MCP` ou `A2A` à grande échelle en production (`C27 § 42.6, § 48.3`). Les grilles `Q-A..Q-E`, `AgentMesh` (`C26 ch. 14, 37`), la matrice `0/15` et les zones `Z1–Z5` (`C26 § 42.0–42.1, § 42.3–42.4`) restent des constructions d’auteur (`[S]`) co-appuyées par `CAD26`.
- **Textes** `statut F` **et jalons ouverts.** `FDX v6.0` et `UIT-T F.748.93` demeurent au `statut F` (aucun `[N]`). L’état `alpha3` de `a2a-tck`, `SEP-3398` (30 mars 2027, réserve `C26 [AN-5]`) et la date du « 4 août » en `CAD26 Annexe H.4` n° 2 imposent une veille trimestrielle.
- **Renvois aux 4 PDF :** `C26` ch. 7–11, 37, 42, Ann. B, Ann. N.2 ; `CAD26` ch. 6, § 8.1 (Tab. 28), § 9.4 (Fig. 18), § 11.7, Ann. H.2/H.4 ; `C27` ch. 5–11, 19, 24, 26–27, § 49.7 ; `PD28` `M-4`, `M-11`, `M-13`.
