# Chapitre 6 — Autonomie graduée, classes de décision, supervision humaine et liaison cryptographique

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 14 (§ 14.4), ch. 17 (§ 17.4–17.5), ch. 27, ch. 29 (§ 29.4.1), ch. 31 (§ 31.1), ch. 43 (§ 43.3–43.5), Annexe N]` · `[CAD26 ch. 8 | EXIG-AUT-01 à EXIG-AUT-23 | PRIN-04, PRIN-05, PRIN-10 | ch. 11 (EXIG-GOV-17), ch. 12 (EXIG-CON-01 à EXIG-CON-09), ch. 14]` · `[C27 § 0.4, ch. 22, ch. 30 (§ 30.4, § 30.9 [S]), ch. 38, ch. 41 | ADR-003, ADR-018, ADR-025 | PRR S-09, S-10, G-03, G-04, G-06, G-11, G-12]` · `[PD28 M-7, M-12, M-24, M-26 | PRI-006, PRI-007 | CAP-002, CAP-003, CAP-048 | INI-043 | POR-009, POR-014, POR-015 | SIG-017, SIG-101, SIG-105, SIG-106]`.

*Question directrice : Jusqu’où déléguer l’action par domaine et par acte, et comment garantir techniquement que la supervision humaine ne devienne ni un rituel d’interface ni une approbation machinale ?*

- **Thèse du chapitre :** L’autonomie d’un agent ne découle jamais de la capacité brute du modèle. Une approbation exigée à tout propos dégénère en clic machinal inopérant en sûreté comme en droit (`[M]`, `[N]`). La délégation se gouverne par la matrice croisant huit domaines (`D1–D8`), six classes de décision et le couple `N0–N4 × P0–P3`. Elle interdit sans dérogation l’autonomie non bornée (`NX`) et toute exécution solitaire d’un acte irréversible (`P3`) P : PRI-006 P : CAP-048 E : EXIG-AUT-03 E : EXIG-AUT-07 E : EXIG-AUT-09 E : EXIG-GOV-17 . Chaque acte sensible exige une approbation hors bande (`OpenID Connect CIBA`, `FIDO2`) scellée au condensat `h = SHA-256(JCS( — ))` retenu à la passerelle. Elle sépare le point d’arrêt préventif (`PC3`) de la révision légale a posteriori et instrumente la vigilance P : PRI-007 P : CAP-002 P : CAP-003 E : EXIG-AUT-12 E : EXIG-AUT-19 E : EXIG-AUT-21 E : EXIG-AUT-23 .

## 6.1 Gouvernance matricielle de l’autonomie : domaines D1–D8, stades 0–4 et classes de décision 1–6

Exiger un humain devant chaque pas annule le gain tout en usant le réviseur. À l’inverse, laisser un agent décaisser ou refuser seul engage l’institution sans décideur identifiable (`C27 ch. 22`, `C26 § 31.1.3`). La littérature (Feng et coll., 2025 ; IMDA v1.5, mai 2026 ; *Least-Agency* OWASP) établit que **l’autonomie est un choix de conception par acte et configuration, indépendant du modèle** (`C27 § 22.2`, `CAD26 § 8.1`). Dans `MAP`, `68 %` des agents restent d’ailleurs bornés à dix étapes (`C27 § 22.7`). Entre *dans la boucle*, *sur la boucle*, *hors de la boucle* et *aux commandes* (UE 2019, `C27 § 22.1`), comme entre *copilote* et *autonomie transactionnelle* (`C26 § 31.1.3, Tableau 31.1`, statut « C » `[É]` sur *Moffatt v. Air Canada*, 2024, `650,88 $ CA`), la position **aux commandes** ne se délègue jamais.

Deux échelles raccordées en Annexe A cadrent ce choix (`PD28 M-12`, `CAD26 ch. 8, ch. 12, ch. 14`, `ADR-003`). Côté AE, **huit domaines (**`D1–D8`**,** `[S]` **de** `PD28 § 12.2`**)** structurent le portefeuille : `D1` *Distribution et relation client*, `D2` *Conseil, vente et convenance*, `D3` *Souscription et tarification*, `D4` *Contrats et comptes*, `D5` *Règlement et sinistres*, `D6` *Conformité, LBC et risques*, `D7` *Trésorerie, investissement et réassurance*, `D8` *Opérations TI et cyberrésilience*. Chacun progresse sur **cinq stades (**`Stades 0–4`**)** au rythme de son maillon faible (`PD28 § 12.3`). Le `Stade 2` (Niveaux 2–3 `CAD26 ch. 14`) ouvre la production réglementée, tandis que le `Stade 3` (Niveau 4 `CAD26`) suffit à la majorité. En 2035, **le** `Stade 4` **inter-organisations demeure proscrit en** `D2` **et** `D6` (représentant inscrit

et secret `CANAFE`). `PD28 M-12` (p. 170) plafonne ainsi `D2` aux `Stades 2–3`, `D6` au `Stade 3` interne uniquement et `D7` au `Stade 3` (malgré une divergence avec `M-15` et `M-18`) C : A, B, C ; SIG-101, SIG-105 .

Par acte, la table aligne `Classes 1–6` (`PD28 § 12.4`), `N0–N4 × P0–P3 × 3 classes de risque` (`CAD26 ch. 8, ch. 12`), `L0–L4` (`C27 § 0.4`) et `OO1–OO4` **/** `Q-A..Q-E` `[S]` (`C26`) :

| Classe de décision (`PD28 M-12`) | `CAD26` (`N0–N4` × `P0–P3` × Classe de risque) | `C27` (`L0–L4`) | `C26` (`OO1–OO4`, construits `[S]`) | Contrôle obligatoire |
| --- | --- | --- | --- | --- |
| **Hors classe agentique** (flux fixe) | `N0` Automatisation déterministe | `L0` déterministe | `OO3` pur / code | Tests logiciels classiques et revue de code |
| `Classe 1` — Lire et analyser | `N1` Consultatif sur `P0` et `P1`, toutes classes | `L1` lecture filtrée | `OO1`/`OO2` lecture, `Q-A`/`Q-D` `[S]` | Filtrage `ACL` amont et télémétrie sans contenu |
| `Classe 2` — Agir réversible borné | `N3` sous domaine nominal (*Operational Design Domain*, `ODD`, faible/modérée) ou `N2` (élevée) sur `P2` | `L3` borné / `L2` | `OO3`/`OO4` sous enveloppe | Clé d’idempotence, compensation Saga, revue échantillonnée (`5 %` modérée, `1 %` faible) |
| `Classe 3` — Agir matériel coûteux | `N2` par défaut (`N3` sous seuil homologué) sur `P2` **> seuil** | `L2` (`L3` restreint) | `OO3`/`OO4` arrêt `PC3` `[S]` | Approbation signée `JCS SHA-256` (à chaque action en classe élevée) |
| `Classe 4` — Agir irréversible critique | Outil `P3` : **jamais exécuté seul** (même `N4`) | `L2` strict hors bande | `OO3`/`OO4` irréversible (`§ 31.1`) | `CIBA` + `FIDO2` lié à `h` (`≤ 15 min`), tampon pré-engagement, **2 approbateurs** en élevée |
| `Classe 5` — Décision visant personne | **Classe élevée** plafonnée `N2` (`EXIG-CON-02`) | `L2`/`L3` `art. 12.1` | `OO3`/`OO4` (`§ 29.4.1` `[S]`), `Q-E` `[S]` | Avis contemporain, facteurs explicables, réexamen humain, dossier `≥ 1 an` |
| `Classe 6` — Hors mandat (cadre/journaux) | `NX` **INTERDIT** sans dérogation (`EXIG-AUT-03`, `EXIG-GOV-17`) | Exclu de `L0–L4` | Violation `PC4` / `Z3` `[S]` | Blocage déterministe hors modèle (`CAP-037`) et coupe-circuit immédiat (`CAP-039`) |

Cinq règles régissent cette table P : PRI-006 P : CAP-048 (`PRR G-03`, `PRR G-04`, `PRR S-09`) :

1. **Interdictions non dérogeables (**`EXIG-GOV-17`**)** : aucune dérogation n’autorise `NX` **(**`Classe 6`**)**, le dépassement du plafond de classe, un `P3` **(**`Classe 4`**)** sans humain hors bande, ni le franchissement de `N2` sous la règle d’or E : EXIG-AUT-01 E : EXIG-AUT-02 E : EXIG-AUT-03 E : EXIG-AUT-09 E : EXIG-CON-02 E : EXIG-GOV-17 .
2. **Permissions effectives et règle d’or (**`≤ N2`**)** : le classement suit les accès réels E : EXIG-AUT-06 . Cumuler impact élevé, faible réversibilité et détection lente (tout critère non étalonné étant réputé atteint) **plafonne à** `N2`, quels que soient les scores d’essai E : EXIG-AUT-07 .
3. **Paliers** `P0–P3` **au catalogue** : les indices `MCP` (`readOnlyHint`, `destructiveHint`) étant non fiables, le palier est fixé en revue sécurité, avec montants `P2`/`P3` en décimal exact ou entiers d’unités mineures E : EXIG-AUT-08 E : EXIG-MCP-14 .
4. **Union la plus stricte par appel** : la passerelle prend le maximum entre `classe × palier`, maillon le plus restrictif (*High-Water Mark*), seuils métier et **règle de deux** E : EXIG-AUT-10 E : EXIG-SEC-04 .
5. **Domaine nominal d’exploitation (**`ODD`**) et agents ambiants** : `N3` et `N4` (`N4` réservé à la **classe faible** par le comité) exigent un `ODD` borné, réévalué sur changement, et la
  **réautorisation périodique** des agents ambiants (`C27 § 22.3`) E : EXIG-AUT-04 E : EXIG-AUT-05 E : EXIG-AUT-18 .

## 6.2 Architecture de l’approbation hors bande et liaison cryptographique aux paramètres (JCS SHA-256 et CIBA)

Contre le *délégué confus* (`OWASP ASI02`) et l’injection post-validation, la passerelle rejette en mode fermé tout « oui » conversationnel, résumé d’agent, confirmation locale (`IETF WIMSE AIMS`), *elicitation* `MCP` ou jeton émis pour d’autres arguments, tâche ou agent E : EXIG-AUT-11 E : EXIG-AUT-13 E : EXIG-MCP-21 .

> **[Figure]**
> - Matrice d’autonomie (Classes 1–6 × N0–N4) & circuit JCS / CIBA Gouvernance par acte (NX interdit), jeton lié EXIG-AUT-09..13 et CIBA
> - Plafonds D1–D8 : D1/D4/D8 (St. 3/4) · D2 Conseil [St. 2–3, St. 4 proscrit]
> - D3 (2–3) · D5 Sinistres (refus=hum.) · D6 [St. 3 int. M-12] · D7 (St. 3)
> - Classe (PD28) CAD26 / C27 Contrôle obligatoire de conception
> - Cl. 1 · Lire N1 · P0–P1 · L1 ACL amont mandant (ARC-16)
> - Cl. 2 · Révers. N3/N2 · P2 · L3 Idempotence + Saga + revue 5 %/1 %
> - Cl. 3 · Matériel N2/N3 · P2>s. · L2 Durable, revalid. réveil, JCS
> - Cl. 4 · Irrévers. P3 · L2 + CIBA CIBA/FIDO2 lié h (≤ 15 min), 2 sig.
> - Cl. 5 · Pers. Plaf. N2 (CON-02) Loi 25 art. 12.1 + dossier ≥ 1 an
> - Cl. 6 · Hors m. NX INTERDIT Interdit GOV-17 (AUT-03) + arrêt
> - Circuit hors bande : h = SHA-256(JCS({outil, version, digest, agent, args}))
> - 1. Agent / Orchestrateur
> - • Émet appel P3 ou P2 > seuil
> - • Zéro accès au jeton (IAM-06)
> - • « Oui » en chat rejeté (AUT-13)
> - 2. Passerelle PEP (fermé)
> - • Valide I-JSON (RFC 7493)
> - • Calcule condensat h (JCS)
> - • Vérifie jti unique & recalcule h
> - 3. Canal CIBA & Approbateur
> - • Appareil/session distincts
> - • Vue hors LLM (ASI09)
> - • FIDO2 + RAR (exp ≤ 15 min)
> - 4. Système cible & Audit
> - • Octets exacts canonisés
> - • Clé d’idempotence vérifiée
> - • Preuve h + jti scellée JCS
> - Anti-complaisance : plafond/quart (AUT-20) · témoins (POR-014) · repli < 60 s

*Fig. 6. – Matrice d’autonomie unifiée (D1–D8 × Classes 1–6 × N0–N4 / P0–P3, interdiction NX/Classe 6) et séquence d’approbation hors bande liée au condensat JCS SHA-256 via CIBA et FIDO2.*

Le circuit hors bande (`CAD26 § 8.5` Figure 16, `C27 ch. 30 § 30.4, § 30.9` `[S]`, `ADR-018`) scelle la signature aux octets exacts de l’appel P : CAP-002 (`PRR S-10`) :

1. **Filtrage** `I-JSON` **et condensat** `JCS`**.** Après persistance durable E : EXIG-AUT-17 , la passerelle rejette tout JSON hors `I-JSON` **(**`RFC 7493` : clés dupliquées, flottants inexacts, chaînes invalides), canonise selon `RFC 8785` **(**`JCS`**)** et calcule : `h = SHA-256(JCS({outil, version, definition_digest, agent_id, task_id, arguments}))` où `arguments` inclut la clé d’idempotence et, sur ressource mutable `P3`, les valeurs résolues ou l’`ETag` vérifié à l’exécution E : EXIG-AUT-12 .
2. **Canal hors bande (**`OpenID Connect CIBA` **+** `FIDO2` **+** `RFC 9396`**).** Le service d’approbation dépose la requête en **boîte persistante** E : EXIG-AUT-16 et notifie un approbateur formé E : EXIG-AUT-15 sur appareil distinct via `OpenID Connect CIBA`, détails `RFC 9396` (`authorization_details`, `EXIG-AUT-14`, `DEVRAIT`) et `FIDO2` **/** `WebAuthn` E : EXIG-AUT-09 E : EXIG-AUT-14 .
3. **Jeton retenu à la passerelle (**`≤ 15 min`**,** `jti` **atomique).** Le jeton lie `{émetteur, audience=passerelle, h, approbateur_pseudonyme, rôle, task_id, agent_id, exp ≤ 15 min, jti}`, **reste à la passerelle hors modèle** E : EXIG-IAM-06 , consomme un `jti` atomique (fermé si indisponible E : EXIG-AUT-11 ), revérifie `h` et relaie la forme canonique.
4. **Réessais, sagas et double approbateur.** Sous `≤ 15 min`, le jeton couvre les réessais idempotents de même `h` ; au-delà, l’état est vérifié par clé d’idempotence avant nouvelle signature. L’approbation d’une étape Saga couvre sa compensation déclarée jusqu’à clôture. En **classe élevée sur** `P3`, **deux approbateurs distincts** signent le même `h` ; toute édition recalcule `h` sous co-approbateur indépendant E : EXIG-AUT-12 E : EXIG-AUT-15 .

Contrat schématique AS d’objet `authorization_details` (`RFC 9396` / `OpenID Connect CIBA`) scellant le condensat `JCS` (`EXIG-AUT-12`, `EXIG-AUT-14`) :

```
{
  "type": "ca.fin.p3_approval",
  "binding_alg": "SHA-256-JCS-RFC8785",
  "payload_digest_h": "sha256:4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
  "tool": "payments.rtr.submit_pacs008",
  "tool_version": "1.2.0",
  "agent_id": "spiffe://corp.example/ns/pay/sa/agent-rtr",
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "amount_decimal": "12500.00",
  "currency": "CAD",
  "jti": "jti-9a7f1c2e-single-use",
  "exp_seconds": 900,
  "required_approvers": 2,
  "authenticator": "FIDO2-WebAuthn-out-of-band"
}
```

## 6.3 Point d’arrêt préventif (PC3) contre révision humaine a posteriori (Loi 25 art. 12.1)

Il ne faut jamais confondre **point d’arrêt préventif** (`PC3` / `HITL` avant action risquée) et **révision humaine a posteriori** (`C26 ch. 27 § 27.2–27.4, ch. 43` `PC1`–`PC3` ; `CAD26 § 8.8, § 12.2` ; `C27 § 38.4`). L’article 12.1 de la Loi 25 (en vigueur le 22 septembre 2023 D ) régit toute décision fondée *exclusivement* sur un traitement automatisé de renseignements personnels (`Classe 5`). Il ouvre trois droits P : CAP-003 E : EXIG-AUT-22 E : EXIG-CON-07 (`PRR G-06`) : un **avis d’office** au plus tard lors de la décision (`PC1`), l’accès aux renseignements utilisés et aux **raisons, facteurs et paramètres principaux** (`PC2`), ainsi que le droit de soumettre des observations à un **personnel habilité à réviser effectivement la décision** E : EXIG-AUT-23 . Entrées, versions et facteurs sont

archivés **au moins un an** dans un **dossier de décision chiffré** distinct des traces E : EXIG-CON-09 . Cette architecture s’aligne sur `BSIF E-23` (1er mai 2027 D , `ANC-103`) et `RIA` art. 14 (2 décembre 2027 D , `ANC-007`).

Une validation nominale, pressée par la cadence ou sans pouvoir réel d’infirmation n’écarte pas l’article 12.1 et expose à une requalification devant la `CAI` (`SIG-106`) E : EXIG-CON-08 . À titre comparatif — limité aux **ministères et organismes publics gouvernementaux** et non applicable au secteur financier privé —, la *Directive sur la prise de décisions automatisée* du Conseil du Trésor fédéral et le guide 2026 du MCN englobent l’automatisation partielle et proscrivent la supervision symbolique (`C27 § 22.6, § 38.2, § 38.5`).

## 6.4 Ergonomie anti-complaisance (ASI09), mesure de vigilance et préservation de la relève

Un jeton `CIBA` reste vain sous clic réflexe (`OWASP ASI09`, `C26 § 17.5`, `CAD26 § 8.7`). `C27 ch. 22` (`§ 22.5`) et `ch. 41` (`§ 41.2`) chiffrent ce biais : `93 %` d’acceptation sur un agent de programmation et `17 %` d’actions excessives manquées par un classifieur. Sous conseil erroné, les erreurs bondissent de `+26 %` (`6 %` à `11 %` de réponses justes inversées, Goddard et coll.), le tandem humain-IA tombant sous le meilleur des deux seul. L’érosion de la relève s’y ajoute : `-20 %` d’emploi chez les développeurs de 22–25 ans depuis 2024 (*Stanford HAI 2026*), et `18 %` d’entreprises freinant l’embauche à trois ans (`SAP 2026-22` Banque du Canada, `PD28 M-26 § 26.3`, `SIG-017`).

Quatre contrôles parent cette dérive P : PRI-007 P : CAP-002 (`PRR G-11`, `PRR G-12`) :

1. **Écran différentiel hors modèle** : généré depuis les arguments `I-JSON` (cible, montant, écart avant/après, contradictions, jamais un résumé d’agent), avec avis préalable de l’expert sur enjeux élevés P : DEC-002 E : EXIG-ARC-03 E : EXIG-AUT-19 .
2. **Charge bornée** : filtrage déterministe en `Classe 2` réservant la file aux exceptions et `P3` (`~0,8 %` des appels mesurés, `C27 § 22.7`), plafond par quart, rotation et absence de cadence pénalisant le refus E : EXIG-AUT-20 .
3. **Métrologie et dossiers témoins** : suivi du temps médian d’examen, des approbations sans retouche, des infirmations et de l’interception de **dossiers témoins à défaut connu**, conditionnant `POR-009` et `POR-014` P : POR-009 P : POR-014 E : EXIG-AUT-21 .
4. **Quotas formateurs et rétrogradations distinctes** : quota manuel de bout en bout dès `> 70 %` d’automatisation P : INI-043 , **bascule automatique** `< 60 s` vers `N2` sur bris opérationnel P : POR-015 , distincte en `CAD26` de l’abaissement d’un niveau après `3` mois hors `SLO` (`EXIG-EVA-06`) et du passage à *suspendu* après `> 30` jours de vacance d’un rôle `A` ou en revue trimestrielle E : EXIG-EVA-06 E : EXIG-GOV-09 E : EXIG-GOV-13 .

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. **Verrouiller** `Domaine × Classe` **:** Plafonner `D1–D8 × Classes 1–6`, exclure `Stade 4` en `D2`/`D6` et sanctionner `EXIG-GOV-17` (`NX`, `P3` seul, règle d’or `≤ N2`) P : PRI-006 P : CAP-048 E : EXIG-AUT-03 E : EXIG-AUT-07 E : EXIG-AUT-09 E : EXIG-CON-02 E : EXIG-GOV-17 .
2. **Garantir** `art. 12.1` **:** Dissocier `PC3` de l’avis d’office, de l’explication des facteurs et de la révision effective ; bannir l’approbation nominale P : CAP-003 E : EXIG-AUT-22 E : EXIG-AUT-23 E : EXIG-CON-07 E : EXIG-CON-08 .
3. **Protéger jugement et relève :** Borner les files, auditer les cas témoins (`POR-014`), maintenir le quota manuel (`> 70 %`) et armer la bascule `< 60 s` (`POR-015`) P : PRI-007 P : INI-043 P : POR-014 P : POR-015 E : EXIG-AUT-20 E : EXIG-AUT-21 .

Spécifications AS

1. **Union stricte :** Qualifier `P0–P3` au catalogue (indices `MCP` ignorés, décimal exact) et évaluer par appel seuils et règle de deux E : EXIG-AUT-08 E : EXIG-AUT-10 E : EXIG-MCP-14 E : EXIG-SEC-04 .
2. **Circuit** `JCS SHA-256` **+** `CIBA`**/**`FIDO2` **:** Filtrer `I-JSON` (`RFC 7493`), hacher `h = SHA-256(JCS(...))` (`RFC 8785`), notifier hors bande (`CIBA` et `RFC 9396`, `DEVRAIT`, + `FIDO2`), retenir le jeton (`≤ 15 min`, `jti` atomique) à la passerelle hors modèle et doubler les signataires sur `P3` élevé P : CAP-002 E : EXIG-AUT-11 E : EXIG-AUT-12 E : EXIG-AUT-14 E : EXIG-AUT-15 E : EXIG-IAM-06 .
3. **Écran et archive :** Générer la vue différentielle hors modèle, injecter les témoins et conserver `≥ 1 an` le dossier chiffré `art. 12.1` E : EXIG-AUT-19 E : EXIG-AUT-21 E : EXIG-CON-09 .

## 6.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Niveau d’autonomie initial | Minimum suffisant (`N1` ou `N2`) sous plafond de classe, permissions effectives et règle d’or (`≤ N2`) E : EXIG-AUT-01 E : EXIG-AUT-06 E : EXIG-AUT-07 | `N3` sur `P2` compensable sous `ODD` ; `N4` réservé à la classe faible par le comité E : EXIG-AUT-04 | `[N]` `RIA` art. 14 (`ANC-007`) ; `[É]` `IMDA` v1.5 ; `CAD26` Tableau 28 |
| Acte critique ou irréversible (`Classe 4` / `P3`) | Approbation hors bande (`CIBA` + `FIDO2`) liée à `SHA-256(JCS)` à chaque appel ; 2 signataires en élevée E : EXIG-AUT-09 E : EXIG-AUT-12 E : EXIG-AUT-15 | Jamais en exécution initiale ( E : EXIG-GOV-17 ) ; compensation Saga pré-approuvée selon journal | `[É]` `OWASP` `ASI02` ; `CAD26` § 8.5 (`RFC 7493`, `RFC 8785`, `RFC 9396`) |
| Accord humain dans le fil de l’agent | Rejet fermé par la passerelle : ni « oui » conversationnel ni résumé d’agent ne valent approbation E : EXIG-AUT-11 E : EXIG-AUT-13 | Jamais sur `P2` validé et `P3` ; seul le jeton du service d’approbation fait foi | `[É]` `IETF WIMSE AIMS` ; `CAD26` Figure 16, `EXIG-MCP-21` |
| Décision visant une personne (`Classe 5`) | Plafond `N2` avec réviseur humain compétent, ou avis d’office, facteurs explicables et réexamen (`art. 12.1`), dossier `≥ 1 an` E : EXIG-CON-02 E : EXIG-CON-07 E : EXIG-CON-09 | Jamais par validation nominale ou cadence excessive (requalification `SIG-106`) E : EXIG-CON-08 | `[N]` `Loi 25` art. 12.1 (`C26` `S-025`, `S-135`) ; `BSIF` E-23 (`ANC-103`) |
| Anti-complaisance (`ASI09`) et relève | Vue différentielle hors modèle, plafond par quart, témoins et quota manuel dès `> 70 %` d’automatisation P : INI-043 E : EXIG-AUT-19 E : EXIG-AUT-20 E : EXIG-AUT-21 | Actes `Classe 2` sous seuil dotés de compensation automatique éprouvée et audités | `[M]` Goddard et coll. (`+26 %`) ; `C27` § 22.5, § 41.2 ; `Stanford HAI 2026` |
| Dérive qualité ou vacance du parrain | Bascule automatique `< 60 s` vers `N2` P : POR-015 ; baisse d’un niveau après `3` mois hors `SLO` et suspension après `> 30` jours de vacance ou en revue trimestrielle E : EXIG-EVA-06 E : EXIG-GOV-09 E : EXIG-GOV-13 | Jamais de maintien tacite en `N3`/`N4` ; réouverture signée par 1re et 2e lignes | `[N]` `BSIF` E-23 (`ANC-103`) ; `[É]` `CAD26` `EXIG-EVA-06`, `GOV-09`, `GOV-13` ; `[S]` `POR-015` |

## 6.6 Limites et renvois au corpus

- **Questions juridiques ouvertes au 1er novembre 2026 :** la portée de « exclusivement automatisé » (`Loi 25 art. 12.1`) sur une chaîne multiagent reste une question ouverte de degré 3 (zéro occurrence dans le rapport quinquennal `CAI` de mai 2026 ni dans ses actualités au 29 octobre 2026, `C26 Annexe N.3 p. 669`, `SIG-106`), de même que son applicabilité aux entités fédérales (`C26 § 27.3`).
- **Textes non déposés (« statut F » au corpus), limites empiriques et divergence interne** `PD28` **:** l’extraction automatisée sur `LégisQuébec` a été bloquée en amont (les appuis `[N]` proviennent des textes officiels sanctionnés `L+` et de `C26`/`CAD26`) ; `ISO/IEC 42105` n’a pas été consultée (`C27 ch. 22`) ; aucune mesure indépendante ne quantifie la fatigue d’approbation en institution financière (`93 %` et `17 %` provenant d’un seul éditeur). Enfin, `PD28` comporte une divergence interne entre `M-12` (p. 170 : `D6` au `Stade 3` interne uniquement et `D7` au `Stade 3`) et `M-15` (p. 200) ainsi que `M-18` (`§ 18.4` p. 237, `Fig. 5` p. 242), qui cotent `D6` et `D7` aux `Stades 3–4` sur des fonctions techniques sans données clients ; le mémoire retient le plafond prudent de `M-12`.
- **Constructions d’auteur (**`[S]`**) :** la grille `D1–D8 × Stades 0–4`, les `Classes 1–6` (`PD28 M-12`), la règle d’or `EXIG-AUT-07` et le profil `CIBA` + `RFC 9396` + `h = SHA-256(JCS(...))` (`≤ 15 min`, `CAD26 § 8.5`) sont des synthèses propres au corpus adossées à des standards ouverts.
- **Renvois aux 4 PDF :** `C26` ch. 14 (§ 14.4), ch. 17 (§ 17.4–17.5), ch. 27, ch. 31 (§ 31.1), ch. 43 (§ 43.3–43.5), Annexe N.3 (pp. 668–670) ; `CAD26` ch. 8 (pp. 118–136), ch. 11 (`EXIG-GOV-17`, p. 201), ch. 12 (§ 12.2) ; `C27` § 0.4, ch. 22 (pp. 456–467), ch. 30 (§ 30.4, § 30.9 [S]), ch. 38 (§ 38.4), ch. 41 (§ 41.2) ; `PD28` M-12 (pp. 167–176), M-24 et M-26 (§ 26.3).
