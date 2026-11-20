# Chapitre 12 — Homologation unifiée et trajectoire adaptative (90 jours → 18 mois → Paliers P1–P3) sous signaux

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 46, ch. 50]` · `[CAD26 ch. 14, ch. 15, Annexe A | EXIG-GOV-16..20]` · `[C27 ch. 43, Annexe F, Annexe G]` · `[PD28 M-19–M-26 | INI-001..029, INI-041..054, POR-001..009, POR-011..016, SIG-001..017, SIG-101..110]`.

*Question directrice : Comment franchir le cap immédiat des 90 jours à 18 mois tout en orchestrant une trajectoire adaptative 2028–2035 gouvernée par preuves, portes et signaux de bascule ?*

**Thèse du chapitre :** Une feuille de route agentique échoue soit par précipitation sans preuves, soit par lourdeur incitant au contournement P : PRI-001 P : PRI-006 . Ce chapitre soude trois instruments complémentaires. Premièrement, la porte d’homologation (`Annexe C`) unifie les `305 EXIG-*` (`CAD26 Annexe A` v1.2), les dix interdits `EXIG-GOV-17` et les 75 points `PRR` (`C27 Annexe G`). Deuxièmement, la continuité **90 jours → 18 mois** (`Niveau 3` / `Stade 2`) débouche sur les **paliers** `DAPP` **(**`P1`**–**`P3`**, 43 initiatives, 15 portes** `POR`**)**. Troisièmement, **27 signaux** `SIG` imposent une décision sous 30 jours pour parer les sept échecs de `PD28 M-26` P : INI-051 P : INI-052 P : POR-015 P : POR-016 .

## 12.1 Porte unique d’homologation : fusionner `CAD26 Annexe A` et la grille `PRR`

Séparer `CAD26 Annexe A` et la grille `PRR` (`C27 Annexe G`) dupliquerait l’instruction d’homologation. Générée depuis `homologation.json`, l’`Annexe C` les fusionne en **sept domaines** (`A.2` Gouvernance et registre à `A.8` Données, vie privée et conformité) et **41 rubriques**. Cette grille aligne **305** `EXIG-*`, **15 portes** `POR` et **75 points** `PRR` (`G.1` sécurité/`NHI`, `G.2` résilience/sagas, `G.3` observabilité/`FinOps`, `G.4` gouvernance/droit, `G.5` fédération/souveraineté/usine). Les 75 points `PRR` se ventilent en **24** `[BLOQUANT]` en `N3`/`N4` [`L3`/`L4`] recalibrés `W1.3`, **26** `Conditionnel` et **25** `Élevée`/`Moyenne`.

Deux invariants gouvernent cette porte (`CAD26 ch. 11, Annexe A`). D’abord, chaque contrôle s’exige dès l’exercice effectif de la capacité sur **preuves système vérifiables** au manifeste CI/CD, jamais sur auto-déclaration. Ce manifeste YAML (`C27 Annexe F.4`, sans champ fictif) porte le plafond d’autonomie, le parrain, le budget `CPO`, le seuil `pass^k` et le coupe-circuit. Ensuite, nulle dérogation (`≤ 6 mois` renouvelable une fois, ou `≤ 90 jours` par l’AE en classe faible) ne franchit les **dix interdictions sans dérogation** (`CAD26 p. 200` E : EXIG-GOV-17 ) :

1. autonomie `NX` ( E : EXIG-AUT-03 ) ;
2. action `P3` sans approbation humaine hors bande E : EXIG-AUT-09 ;
3. usurpation d’identité au lieu de délégation (`CAD26 § 9.3` E : EXIG-IAM-09 ) ;
4. relais d’un jeton reçu E : EXIG-IAM-12 ;
5. agent sans fiche complète ni parrain nommé, hormis la fiche minimale d’un existant inventorié E : EXIG-GOV-16 ;
6. dépassement du plafond d’autonomie de la classe E : EXIG-CON-02 ;
7. autorisation au-delà de `N2` sous les seuils de la règle d’or E : EXIG-AUT-07 ;
8. exposition simultanée à du contenu non fiable, des systèmes sensibles ou données privées et un canal d’envoi sans retrait E : EXIG-SEC-06 ;
9. exploitation sans journal d’audit E : EXIG-OBS-11 ;
10. manquement légal ou réglementaire (`CAD26 Annexe A`).

## 12.2 De la rampe `90 jours → 18 mois` aux trois paliers adaptatifs `DAPP` (`2028–2035`)

> **[Figure]**
> - Trajectoire adaptative 2026–2035 : paliers P1–P3, 15 POR & jalons Franchissement sur preuves (27 SIG) · séparation privé vs secteur public
> - 2026 ’27 2028 ’29 2030 ’31 2032 ’33 2034 2035
> - Paliers
> - DAPP
> - (43 INI)
> - 15 portes
> - POR &
> - 27 SIG
> - Secteur
> - financier
> - privé &
> - PKI TLS
> - Secteur
> - public
> - (adm.
> - pub.)
> - 90 j–18 m
> - J1 → J3
> - PEP, MCP
> - P1 Fonder
> - Stade 2
> - 14 s.r.+15
> - P2 Étendre
> - Stade 3
> - 9 s.r.+7 c.
> - P3 Élargir
> - St. 3/4*
> - 4 s.r.+6 c.
> - J1 → J3
> - 90 j, 18 m
> - POR-001..004
> - NHI, <10 s [S]
> - POR-005..009
> - PQC 007, 99,5 %
> - POR-011..014
> - PQC, vLEI 3 v.
> - Continu P1–P3 : POR-015 repli < 60 s · POR-016 CPO & SIG ≤ 30 j
> - [D] 2027-05-01 BSIF E-23 (ANC-103) · AMF IA (ANC-112)
> - [D] 2027-03-15 TLS 100 j
> - [D] 2027-12-02 RIA Ann. III (UE)
> - [D] oct. 2028 NI 31-103 · fin 2028 B-15
> - [D] 2029-03-15 TLS 47 j
> - [A] 2030–2035 PQC G7 fin. (NIST)
> - [D] 2033-06-30 Lois fin.
> - [D] 2027–28 AMOPS & EO 14412 (ANC-033, adm. pub.)
> - [D] 2027–33 Réexamens UE (adm. pub.)
> - [D] 2030–35 OMB M-26-15 & SCT (adm. pub.)
> - [D] Adopté · [A] Annoncé · (adm. pub.) Secteur public seul · *Stade 4 exclu D2/D6.

*Fig. 8. – Frise chronologique et trajectoire adaptative 2026–2035 : rampe tactique 90 jours à 18 mois, paliers DAPP P1 à P3 (43 initiatives), 15 portes POR sur preuve système, 27 signaux SIG et séparation entre institutions financières privées et administrations publiques.*

La rampe immédiate (`CAD26 ch. 14–15`, `C26 ch. 46`) et les parcours adaptatifs dynamiques (`DAPP`, Haasnoot et al., `PD28 M-19–M-24`) se soudent autour du `Stade 2` (*Usage encadré*). Ce palier équivaut au **Niveau 3 « Défini »** sur les cinq dimensions de `CAD26 Tableau 55`.

**Rampe tactique** `0 → 18 mois` **(**`Jalons J1 à J3`**).** Les **90 premiers jours** (`~13 semaines (~65 jours ouvrables)`, *Fondations*, plafond `N0–N1`, jalon `J1`) posent le socle. Ils installent le comité et le RPRP, inventorient les existants et agents fantômes (fiche minimale et parrain sous cinq jours ouvrables sinon arrêt E : EXIG-GOV-16 ), suppriment les clés partagées, déploient la passerelle de modèles et le traçage sans contenu, lancent l’ÉFVP (`Loi 25 art. 3.3`) et testent le coupe-

circuit. Les **mois 3 à 9** (*Plateforme*, jalon `J2`) ouvrent `N2` et les premiers `N3` intra-domaine faible ou modéré. Ils déploient la passerelle d’agents (`P0–P3`), le canal de compensation et `JCS`/`CIBA` face aux butées 2027 : TLS **100 jours au 15 mars 2027** D `ANC-023`, veille `MCP SEP-3398` du **30 mars 2027** A , convergence au **1er mai 2027** D de `BSIF E-23` (`ANC-103`) et d’`AMF IA` (`C26 Annexe N.3`), et migration `MCP 2026-07-28` au plus tard le **28 juillet 2027** D E : EXIG-MCP-22 . Les **mois 9 à 18** (*Industrialisation*, `N3` interdomaines via passerelle) franchissent `J2a` (1er novembre 2027) avant l’**Annexe III du** `RIA` **le 2 décembre 2027** D `ANC-007`. Ils industrialisent `E1–E3`, les sagas et les bacs à sable matériels pour atteindre à 18 mois (`J3`) le **Niveau 3 (« Défini »)**. `CAD26 § 14.3` précise qu’`ISO/IEC 42001` (`J5`) ne couvre que la dimension Gouvernance et non les quatre dimensions techniques.

**Portefeuille** `DAPP` `2028–2035` **C : tous ; SIG-009, SIG-108 (**`43 INI` **=** `29` **sans regret +** `14` **conditionnelles ;** `15 POR`**).** Au-delà de 18 mois, `PD28` structure **43 initiatives** (`INI-001` à `INI-029` et `INI-041` à `INI-054`) et **15 portes sur preuves** (`POR-001` à `POR-009` et `POR-011` à `POR-016`), avec zéro avancement au seul calendrier :

- **Palier 1 (**`2028–2029`**, sortie** `Stade 2`**) :** `14` **sans regret (**`INI-001` **à** `INI-014`**) +** `1` **conditionnelle (**`INI-015`**).** Il consolide registre et rejet réseau (`INI-001`), `NHI`/`RFC 8693` (`INI-002`), passerelle/épinglage (`INI-003`), politiques/coupe-circuit (`INI-004`), double couloir `OpenTelemetry` (`INI-005`), six substrats (`INI-006`) et inférence/bacs à sable (`INI-007`). Il y adjoint sagas durables (`INI-008`), postes `JCS`/`CIBA` et `art. 12.1` (`INI-009`), contexte compilé (`INI-010`), adaptateurs `Decimal` (`INI-011`), bancs `pass^k` (`INI-012`), empreinte/`CPO` (`INI-013`) et clauses `EXIG-APP` (`INI-014`), tandis qu’`INI-015` confine puis éteint sous douze mois les `CUA` (`[B, C]`). S’y calent la fin des rétrofacturations `NI 31-103` (`2028-10-01` D `ANC-105`), la portée 3 `BSIF B-15` (`fin 2028` D `ANC-106`) et **TLS 47 jours au 15 mars 2029** D `ANC-030`. Quatre portes le valident : `POR-001` (inventaire/`NHI` 100 %), `POR-002` (six substrats/révocation clé/zéro `RP`), `POR-003` (2e ligne et arrêt `< 10 s` `[S]` de `PRR S-14` vs `15 min` `CAD26` E : EXIG-IAM-20 E : EXIG-SEC-26 ) et `POR-004` (*showback* `CPO` et sortie).
- **Palier 2 (**`2030–2032`**, sortie** `Stade 3`**) :** `9` **sans regret (**`INI-016` **à** `INI-024`**) +** `7` **conditionnelles (**`INI-025` **à** `INI-029`**,** `INI-053`**,** `INI-054`**).** Le socle ouvre couche sémantique (`INI-016`), mémoire bi-temporelle/`WAP` (`INI-017`), topologies bornées (`INI-018`), PQC hybride (`INI-019`), continuité bimodèle à poids ouverts (`INI-020`), partage financier ouvert (`INI-021`), *chargeback*/budgets d’erreur (`INI-022`), suivi carbone (`INI-023`) et modernisation en miroir (`INI-024`). Les sept options couvrent fédération par gravité (`INI-025`), vocal temps réel (`INI-026`), enclaves `TEE` (`INI-027`), distillation sous sas (`INI-028`), sas déconnecté (`INI-029`), sortie fournisseur critique (`INI-053`) et bascule accélérée PQC/réglementaire (`INI-054`). Ce palier se cale sur la fenêtre financière `G7` PQC `2030–2032` A `ANC-040` (`PD28 M-5`). Les butées `2030–2031` D (`ANC-035, ANC-036, ANC-038, ANC-039`) d’`OMB M-26-15`, `EO 14412` et `AMOPS` visent uniquement les administrations publiques. Cinq portes le clôturent : `POR-005` (sémantique/WAP), `POR-006` (anti-boucle/bascule bimodèle), `POR-007` (`ACME` 47 j, jetons PQC par `kid`, archives 5/7 ans), `POR-008` (API ouvertes `≥ 99,5 %`/zéro CUA, `30 j` `[S]` en miroir) et `POR-009` (*chargeback*, portée 3, reprise manuelle).
- **Palier 3 (**`2033–2035`**,** `Stade 3` **et** `Stade 4` **sélectif hors** `D2` **et** `D6` **interne** `M-12`**) :** `4` **sans regret (**`INI-041` **à** `INI-044`**) +** `6` **conditionnelles (**`INI-045` **à** `INI-050`**).** Il s’inscrit après la **temporisation fédérale du 30 juin 2033** D `ANC-109, ANC-110, ANC-111` et vers l’horizon financier `G7` PQC **2035** A `ANC-043` (`PD28 M-22`, distinct des échéances `2035` D `ANC-041, ANC-042` propres aux administrations publiques) C : A, B, C ; SIG-009, SIG-108 . Le socle achève le PQC natif (`INI-041`), la conformité post-2033 (`INI-042`), l’élargissement sélectif `Classes 3 et 5` (`INI-043`) et l’extinction transitoire (`INI-044`). Les six options portent sur les canaux externes (`INI-045`), les cellules Diplomate/Évaluateur (`INI-046`), `vLEI` (`INI-047`), les espaces de données (`INI-048`), la souveraineté `SLM+TEE` (`INI-049`) et la résilience territoriale (`INI-050`).
  Quatre portes le valident : `POR-011` (PQC natif 100 %), `POR-012` (conformité post-2033 et zéro fuite inter-filiales), `POR-013` (`Stade 4` sous `vLEI` et rapprochement tripartite) et `POR-014` (constance 4 trimestres et reprise manuelle).
- **Continu (**`P1–P3`**) :** `2` **sans regret transversales (**`INI-051`**,** `INI-052` **; total sans regret** `14 + 9 + 4 + 2 = 29`**) et** `2` **portes permanentes (**`POR-015`**,** `POR-016`**).** `INI-051` pilote les délais `DAPP` et `INI-052` l’arbitrage trimestriel. `POR-015` garantit la rétrogradation automatique en `< 60 secondes`, avec réouverture sous double signature 1re/2e lignes. `POR-016` impose la revue `CPO`, le déclassement après deux trimestres déficitaires et l’essai annuel de sortie et de repli bimodèle.

| Segment | Horizon | Initiatives (`29` s.r. + `14` cond. = `43`) | Portes / jalons exigibles | Cible de sortie |
| --- | --- | --- | --- | --- |
| **Rampe tactique** | `90 j → 18 mois` | Existants inventoriés `EXIG-GOV-16`, `MCP 2026-07-28`, `E-23`/`AMF IA`, `RIA Ann. III` | Jalons `J1` (90 j), `J2` (9 m), `J2a`/`J3` (18 m) | Niveau 3 « Défini » (`CAD26`) |
| **Palier 1 (**`P1`**)** | `2028–2029` | `14` s.r. (`INI-001` à `014`) + `1` cond. (`INI-015` `CUA`) | `POR-001` à `POR-004` (`POR-002` 6 substrats, `POR-003` `< 10 s` `[S]` vs `15 min` `CAD26`) | `Stade 2` généralisé |
| **Palier 2 (**`P2`**)** | `2030–2032` A | `9` s.r. (`INI-016` à `024`) + `7` cond. (`INI-025` à `029`, `053`, `054`) (`ANC-040`) | `POR-005` à `POR-009` (`POR-007` PQC, `POR-008` API `≥ 99,5 %`) | `Stade 3` maîtrisé |
| **Palier 3 (**`P3`**)** | `2033–2035` D / A | `4` s.r. (`INI-041` à `044`) + `6` cond. (`INI-045` à `050`) (`ANC-109`, `ANC-043`) | `POR-011` à `POR-014` (`POR-012` post-2033, `POR-013` `vLEI` 3 voies) | `Stade 3` / `Stade 4` sélectif |
| **Continu** | `P1–P3` | `2` transversales sans regret (`INI-051`, `INI-052`) | `POR-015` (`< 60 s`) et `POR-016` (`CPO` / sortie) | Réversibilité permanente |

## 12.3 Les `27` signaux `SIG` et les parades aux sept modes d’échec endogènes (`M-26`)

Sous revalidation primaire à fenêtre de 30 jours (`C26 ch. 50`, `CAD26 EXIG-GOV-18, EXIG-GOV-20`), `PD28 M-25` suit **27 signaux** opérés par l’observatoire `2028-2035/Master/outils/veille_signaux.py` (HTTPS ouvert sans contournement `403`, couplé à `verifie.py --audit-fraicheur` et `--horodater` sur `derniere_verification_veille`, jalons `2027-05-01`, `2027-08-02`, `2027-12-02`, `2028-10-01` et `2029-03-15`, consacrés dans `CRE-IA-2027` **v2.0**) en quatre familles :

- **10 signaux réglementaires :** `SIG-001` Annexe III `RIA`, `SIG-002` `DORA`, `SIG-101` bulletin `BSIF`, `SIG-102` `AMF IA`, `SIG-103` `LSAC`, `SIG-105` `ACVM`/`OCRI`, `SIG-106` jurisprudence `Loi 25 art. 12.1`, `SIG-107` `LPRPDE`, `SIG-108` temporisation du 30 juin 2033 D `ANC-109` et `SIG-109` `BSIF B-15`.
- **8 signaux normatifs et rails :** `SIG-003` RFC `WIMSE`/`Transaction Tokens`, `SIG-004` `DAWN`/`AGENTPROTO`, `SIG-005` `MCP`, `SIG-006` `OpenTelemetry gen_ai.*` `Stable`, `SIG-007` `vLEI` paiements, `SIG-008` `SC 42`, `SIG-104` `RTR` `pacs.008` et `SIG-110` `FDX`/`ACORD`/`CSIO`.
- **4 signaux post-quantiques et PKI :** `SIG-009` reprise prudentielle `G7` PQC, `SIG-010` bascule `SLH-DSA`, `SIG-011` `FIPS 140-3` sur `RFC 9964/10024/10073` et `SIG-012` incidents TLS `100 j`/`47 j`.

- **5 signaux sur capacités, économie, énergie et relève :** `SIG-013` banc `> 95 %` sur `> 2 h`, `SIG-014` échecs multiagents, `SIG-015` dérive `CPO`, `SIG-016` tension électrique vers `1 700 TWh` en 2035 C : B, C ; SIG-016 et `SIG-017` érosion junior.

Ce système pare les **sept modes d’échec endogènes** de `PD28 M-26` :

1. *Sur-ingénierie suscitant des agents fantômes* → couloir rapide réservé à la `Classe 1` sans écriture par gabarits E : EXIG-GOV-06 (`DEVRAIT`, sans exemption de catégorie) et rejet hors passerelle P : CAP-022 P : CAP-047 .
2. *Saturation de la 2e ligne* `E-23` → proportionnalité par classe et qualification automatisée P : CAP-043 .
3. *Atrophie des juniors (*`-20 %`*) et approbation réflexe* (`SIG-106`, `SIG-017`) → quotas formateurs, cas témoins et gel d’autonomie.
4. *Choc tarifaire et enfermement* (`SIG-015`) → bascule bimodèle annuelle P : CAP-031 et `POR-016`.
5. *Collision* `PKI 47 j` */* `ML-DSA` *(*`HTTP 431`*)* (`SIG-011`, `SIG-012`) → gel d’ouverture externe en `P2` sans `ACME` et référence `kid` P : POR-007 .
6. *Fuite intra-groupe* (`SIG-108`) → rejet hors modèle sans entité mandante, consentement exprès et contrat `B-10`.
7. *Veille décorative et coûts irrécupérables* → **décision budgétaire sous 30 jours après franchissement d’un seuil** `SIG-*`, auditée chaque année par la 3e ligne avec veto de la 2e ligne.

**Calibration artificielle FEDS des cinq seuils** `[S]` **et modélisation EMA (**`DC-P12`**).** En **évaluation exclusivement artificielle FEDS** (`DC-P12`, aucune étude de cas humaine), le banc reproductible `Borealis-Bench/feds-ema/` (`seed = 20261119`, ancré sur *Borealis-Bench*) calibre les cinq seuils `[S]` (`4 000` tirages Monte Carlo/seuil) : `POR-003 < 10 s` `[S]` confirmé avec garde-fou (`p99 = 3 732,68 ms`, conformité `99,95 %`, bail local fail-closed `TTL <= 5 s` contre partition `11 034,19 ms`) ; `<= 15` outils/agent `[S]` ajusté par autonomie (`63,85 %` conformes au risque `<= 2 %` → `<= 15` en `L1/L2`, resserrer à `<= 10–12` en `L3/L4`) ; escalade CIBA/HITL `< 60 s` `[S]` dissociée (`< 5 s` technique `96,78 %` + `60 s` SLA alerte / `120–180 s` TTL fail-closed, bout-en-bout `p95 = 66,72 s`) ; rétention chaude `30 j` `[S]` portée en cible à `45 j` banque/assurance (`97,17 %` nom. vs `89,10 %` panne sévère, surcoût `SCITT + SLH-DSA` de `22,48 Mo` / `3 M` événements) ; et `pass^5 >= 99 %` `[S]` dissocié par couche (plan de contrôle `99,921 %` et multicouche `99,812 %` vs `CaMeL` isolé `78,79 %` → `>= 99 %` plan de contrôle / `L3/L4`, `>= 95 %` génératif `L1/L2`). En modélisation EMA (`3 000` réplications LHS), le **parcours** `B` **(*Archipel cible*)** domine en décision robuste (`92,53 %` de satisfaction conjointe, `95,70 %` des futurs gagnés, minimax regret `p95 = 0,000`), avec bascule conditionnelle vers `CAP-027/033/034/041` (`C`) au seuil empirique `X34 >= 0,386`.

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Exécuter dès le jour 1 la rampe des 90 premiers jours (`N0–N1`, inventaire, `NHI`, passerelle modèles, coupe-circuit) vers le Niveau 3 / `Stade 2` à 18 mois. Réserver la transition aux seuls existants inventoriés E : EXIG-GOV-16 et traiter la `Classe 1` sans écriture par gabarits pré-homologués sans dérogation de catégorie (`CAD26 p. 33`).
2. Piloter la trajectoire 2028–2035 C : A, B, C ; SIG-009, SIG-108 par la preuve aux 15 portes `POR-001` à `POR-009` et `POR-011` à `POR-016` : 29 initiatives sans regret en socle et 14 conditionnelles déclenchées par les 27 signaux `SIG`.
3. Imposer une décision budgétaire sous 30 jours après tout franchissement d’un seuil `SIG-*` P : INI-051 P : INI-052 , auditée annuellement par la 3e ligne sous droit de suspension de la 2e ligne.

Spécifications AS

1. Intégrer au pipeline CI/CD le manifeste d’homologation exécutable (`C27 Annexe F.4`) et la grille unifiée `Annexe C` (`305 EXIG-*` v1.2 + `75 PRR` dont `24` `[BLOQUANT]` en `N3`/`N4`), en verrouillant les dix interdictions non dérogeables E : EXIG-GOV-17 .
2. Produire les preuves système des portes : arrêt coupe-circuit `< 10 s` `[S]` (`PRR S-14`, vs `15 min` `CAD26` E : EXIG-IAM-20 E : EXIG-SEC-26 ) et reprise de saga P : POR-003 , rétrogradation automatique d’autonomie en `< 60 secondes` sur budget d’erreur P : POR-015 , renouvellement `ACME` à 47 jours et scellement post-quantique P : POR-007 .
3. Exécuter chaque année en conditions réelles la bascule vers le modèle indépendant à poids ouverts P : POR-006 , l’extraction contractuelle hors fournisseur P : POR-016 et la reprise manuelle complète sans agent P : POR-009 P : POR-014 .

## 12.4 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Cadencement du contrôle durant la transition initiale | Régime transitoire réservé aux seuls existants inventoriés E : EXIG-GOV-16 , gabarits pré-homologués pour la `Classe 1` sans écriture et rejet réseau hors passerelle P : CAP-022 | Aucune dérogation par catégorie entière (`CAD26 p. 33`) ; zéro tolérance sur les dix interdictions absolues E : EXIG-GOV-17 | `[N]` `[É]` `[S]` `BSIF E-23` (`ANC-103`) ; `CAD26 § 11.5–11.6, § 15.2` ; `PD28 M-26` |
| Passage d’un domaine d’affaires d’un palier au suivant | Franchissement constaté sur preuves système des portes `POR-*` par les 1re et 2e lignes selon le critère le plus faible | Jamais par simple échéance calendaire ; un domaine en retard demeure plafonné à son stade courant | `[N]` `[É]` `[S]` `BSIF E-23` ; `CAD26 ch. 14–15` ; `PD28 M-20–M-24` |
| Engagement des 14 initiatives conditionnelles (`CUA`, `TEE`, B2B, distillation) | Maintien en option différée avec réservation d’interfaces ouvertes tant que le signal `SIG-*` associé n’est pas franchi P : INI-051 | Ouverture anticipée d’un pilote borné si le délai incompressible de préparation d’une butée réglementaire approche | `[M]` Haasnoot et al. (`DAPP`, `PD28 M-23`) |
| Franchissement d’un seuil au registre des 27 signaux `SIG-*` | Instruction obligatoire en comité sous 30 jours avec réallocation tracée et droit de suspension de porte par la 2e ligne | Révision extraordinaire sous 15 jours ouvrables sur version incompatible, dépréciation, retrait accéléré ou correctif de sécurité E : EXIG-GOV-18 | `[S]` `CAD26 § 11.7` ; `PD28 M-25, M-26` |
| Portée reconnue à une certification externe `ISO/IEC 42001` | Revue externe de la seule dimension Gouvernance au jalon de maturité élevé (`CAD26 § 14.3`) | Ne dispense jamais de prouver les quatre dimensions techniques ni la conformité `Loi 25`, `E-23` et `RIA` | `[É]` `CAD26 § 12.5, § 14.3` ; `C27 § 35.4` |
| Maintien sur longue période de la capacité de continuité métier | Exercice annuel documenté de reprise manuelle sans agent, de bascule bimodèle et de sortie fournisseur (`POR-009, POR-014, POR-016`) | Jamais supprimé sur les filières critiques : condition de survie des mandats supervisés sur exception | `[N]` `[É]` `[S]` `BSIF E-21`, Banque du Canada `SAP 2026-22` ; `PD28 M-24, M-26` |

## 12.5 Limites et renvois

Quatre limites encadrent cette trajectoire. Premièrement, l’échelle `Stades 0–4` (`C27 § 43.1`, `PD28 M-12`) et les trois paliers demeurent analytiques sans étalonnage longitudinal bancaire. Aucun scénario `A`, `B` ou `C` ne reçoit de probabilité. Deuxièmement, `ISO/IEC 42001` reste au `statut F` (`CA-12`), la numérotation de `PD28` saute volontairement de `POR-009` à `POR-011` et d’`INI-029` à `INI-041` (`CA-05`), et `PD28 M-26` diverge entre « six modes » en prose (`§ 26.1`, p. 316) et `7` lignes au `Tableau 26.5` (`§ 26.5`, p. 319). Troisièmement, `AMOPS`, `EO 14412` et `OMB M-26-15` visent les seules administrations publiques et ne touchent les institutions financières privées que par effet fournisseur ou reprise prudentielle (`SIG-009`). Quatrièmement, conformément à `DC-P01`, l’ensemble de la chaîne demeure produit et vérifié par agents d’IA sans homologation humaine ; la clôture probatoire s’appuie sur l’`Annexe C` et la recollation `CA-16`. Renvois : `C26` ch. 46 (pp. 527–533), ch. 50 (pp. 576–585), `CAD26` ch. 14–15 (pp. 242–257), `Annexe A` (pp. 259–264), `C27` ch. 43 (pp. 854–872), `Annexes F–G` (pp. 1103–1114), `PD28` `M-19–M-26` (pp. 254–327) et `Annexes A–F` (présent mémoire).
