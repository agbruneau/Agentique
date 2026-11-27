# Annexe B — Cartographie analytique des 616 interrelations systémiques, nœuds carrefours et arbitrages

Cette annexe compile mécaniquement la topologie complète des **616 interrelations typées** reliant les **260 thèmes** du Compendium répartis sur douze domaines (`D01`–`D12`). Le degré moyen s'établit à **4,74** arêtes par thème ; **390 liaisons (63,3 %)** franchissent une frontière de domaine tandis que **226 liaisons (36,7 %)** consolident la cohérence interne d'un même domaine.

## 1. Répartition et sémantique des huit types canoniques d'interrelations

|Type d'interrelation|Effectif|Part|Règle sémantique|
|---|---:|---:|---|
|`operationnalisation`|129|20,9 %|`source` met en œuvre, concrétise ou rend testable `cible`|
|`dependance_technique`|94|15,3 %|`source` dépend de `cible` comme prérequis architectural ou cryptographique|
|`encadrement_normatif`|82|13,3 %|`source` (cadre légal/normatif) encadre et contraint `cible`|
|`attenuation_risque`|82|13,3 %|`source` atténue ou neutralise la vulnérabilité ou dérive représentée par `cible`|
|`tension_arbitrage`|67|10,9 %|`source` entre en tension ou exige un arbitrage explicite face à `cible`|
|`amplification_synergie`|59|9,6 %|`source` amplifie l'efficacité, la fiabilité ou l'impact de `cible`|
|`projection_temporelle`|52|8,4 %|`source` projette ou prépare sa transition vers `cible` sur l'horizon temporel|
|`concordance_inter_tomes`|51|8,3 %|`source` et `cible` s'alignent ou se réconcilient entre plusieurs tomes (ex. DIV-02, DISC-01..05)|

*Tableau B.1 — Distribution et sémantique des huit types canoniques d'interrelations sur les six cent seize liaisons du graphe.*

## 2. Analyse des vingt-cinq nœuds carrefours à plus fort degré relationnel

Les vingt-cinq nœuds carrefours concentrent l'essentiel du couplage transversal entre l'architecture déterministe, la sécurité protocolaire, l'observabilité probatoire et la conformité prudentielle.

**Rangs 1 à 5 :** rang 1, `bsif-e-23` (D09, degré 30, 21 sortantes et 9 entrantes, Architecture prudentielle fédérale : BSIF E-23 (1ᵉʳ mai 2027), B-10/B-13/E-21/B-15 et temporisation 2033) ; rang 2, `protocole-mcp` (D03, degré 25, 10 sortantes et 15 entrantes, Protocole MCP (2026-07-28) sans état, ≤ 15 outils d'intention et bascule juillet 2027) ; rang 3, `passerelle-mcp-ai-gateway` (D03, degré 24, 14 sortantes et 10 entrantes, Passerelle d'agents bidirectionnelle PEP à 9 contrôles ordonnés et budget Borealis-Bench) ; rang 4, `finops-focus-cpo` (D08, degré 24, 6 sortantes et 18 entrantes, Pilotage économique au coût complet par résultat conforme (CPO), FOCUS 1.4 et disjoncteurs) ; rang 5, `exigences-cre-ia-305` (D12, degré 23, 5 sortantes et 18 entrantes, Porte unique d'homologation : 305 EXIG-* v1.2 × 75 PRR (24 bloquants) × 15 POR et 10 interdits GOV-17).

**Rangs 6 à 10 :** rang 6, `post-quantique-ml-dsa-slh-dsa` (D06, degré 21, 10 sortantes et 11 entrantes, Transition post-quantique (FIPS 203/204/205, NIST IR 8547), choc HTTP 431 (50–72×) et CBOR-COSE) ; rang 7, `delegation-obo-deux-sauts` (D06, degré 21, 8 sortantes et 13 entrantes, Rupture au deuxième saut (RFC 8693 §4.1), délégation atténuée ≤ 2 sauts et DPoP/mTLS) ; rang 8, `supervision-hitl-hotl-abstention` (D02, degré 20, 11 sortantes et 9 entrantes, Ergonomie anti-complaisance (ASI09), vue différentielle et distinction entre PC3 et art. 12.1) ; rang 9, `anti-verrouillage-standards` (D03, degré 20, 4 sortantes et 16 entrantes, Confinement anti-verrouillage SaaS (EXIG-ARC-21), catalogues déclaratifs C1 et statut AP2/AGNTCY) ; rang 10, `observabilite-otel-genai` (D08, degré 18, 11 sortantes et 7 entrantes, Télémétrie OpenTelemetry v1.41.0 épinglée (face à v1.44.0 Development) et jointure trace ↔ mandat).

**Rangs 11 à 15 :** rang 11, `protocole-a2a` (D03, degré 18, 6 sortantes et 12 entrantes, Non-substituabilité entre outil et pair, protocole A2A v1.0.1 et asymétrie 0/15 (Z1–Z5)) ; rang 12, `eu-ai-act` (D09, degré 17, 13 sortantes et 4 entrantes, Droit européen applicable par effet extraterritorial : AI Act (Annexe III décembre 2027), Data Act et DORA) ; rang 13, `echelle-autonomie-l0-l4` (D02, degré 17, 6 sortantes et 11 entrantes, Gouvernance matricielle : 8 domaines D1–D8 × Stades 0–4 × Classes 1–6 × N0–N4/P0–P3) ; rang 14, `injection-indirecte-prompt` (D07, degré 17, 2 sortantes et 15 entrantes, Modélisation des menaces OWASP ASI01–10 / MITRE ATLAS, isolation CaMeL (77 % contre 84 %) et tests FR/EN) ; rang 15, `banc-evalops-hermetique` (D08, degré 15, 10 sortantes et 5 entrantes, Évaluation continue E1–E3 (pass^k), juge calibré et abaissement d'autonomie sur dérive SLO).

**Rangs 16 à 20 :** rang 16, `ligne-directrice-amf` (D09, degré 15, 8 sortantes et 7 entrantes, Encadrement AMF Québec : Note AMF IA (41 attentes → 12 EXIG-AMF-01..12), lois d'assurance et statut F) ; rang 17, `did-vc-passeport-agent` (D06, degré 15, 5 sortantes et 10 entrantes, Identité légale vérifiable GLEIF vLEI, lacune KYA (0/9) et encadrement des agents externes) ; rang 18, `erreurs-silencieuses-cascade` (D01, degré 15, 0 sortantes et 15 entrantes, Rupture entre validité syntaxique et erreurs sémantiques silencieuses) ; rang 19, `soc-soar-coupe-circuit` (D07, degré 14, 11 sortantes et 3 entrantes, Coupe-circuit hiérarchisé (< 10 s POR-003 contre 15 min CAD26), SSF/CAEP et rétrogradation < 60 s) ; rang 20, `execution-durable-temporal` (D05, degré 14, 7 sortantes et 7 entrantes, Exécution durable hors processus, idempotence JCS SHA-256 et revalidation au réveil (TOCTOU)).

**Rangs 21 à 25 :** rang 21, `saga-compensatoire` (D05, degré 14, 6 sortantes et 8 entrantes, Patron Saga à point pivot, tampon d'irréversibilité et canal de compensation dédié EXIG-ORC-28) ; rang 22, `identite-non-humaine-nhi` (D06, degré 14, 4 sortantes et 10 entrantes, Diagnostic Q-A..Q-E (0/15), identités non humaines (NHI) parrainées et bannissement des secrets fixes) ; rang 23, `scellage-jcs-scitt` (D08, degré 14, 3 sortantes et 11 entrantes, Journal d'audit à 5 éléments canonisé RFC 8785 (JCS), ancré chaque heure et scellé SCITT + SLH-DSA) ; rang 24, `rag-agentique-contexte` (D04, degré 13, 8 sortantes et 5 entrantes, Compilateur déterministe du contexte (ACL amont), Agent Skills signés et sas WAP ODCS v3) ; rang 25, `double-couloir-probatoire-pii` (D08, degré 13, 7 sortantes et 6 entrantes, Architecture à double couloir PII et séparation des trois magasins réglementés).

## 3. Corridors inter-domaines dominants et densité sur les huit tomes (`T1`–`T8`)

L'empreinte transversale sur les huit tomes antérieurs totalise `T1` (246 rattachements, 844 occurrences), `T2` (162 rattachements, 344 occurrences), `T3` (230 rattachements, 1 458 occurrences), `T4` (164 rattachements, 398 occurrences), `T5` (192 rattachements, 312 occurrences), `T6` (122 rattachements, 156 occurrences), `T7` (136 rattachements, 192 occurrences), `T8` (128 rattachements, 148 occurrences) (totalisant **3 852 occurrences** sur `T1`–`T8`, plus `5` occurrences sur `R` `Tomes/README.md`, dont les comptes bruts par tome se distinguent des `1 931` occurrences agrégées par sous-domaine au Tableau A.1). Les 15 corridors inter-domaines les plus denses (seuil ≥ 7 liaisons, ex-æquo inclus) relient les couples suivants : `D09`→`D10` (13 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Architectures sectorielles, blueprints et cas métier) ; `D09`→`D11` (13 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Prospective 2028–2035, trajectoires DAPP et capital humain) ; `D10`→`D02` (13 liaisons, Architectures sectorielles, blueprints et cas métier vers Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4)) ; `D03`→`D06` (11 liaisons, Interopérabilité protocolaire, découverte et passerelles (MCP, A2A, AGNTCY, AP2) vers Identité non humaine (NHI), chaîne de mandat et post-quantique) ; `D02`→`D01` (9 liaisons, Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4) vers Fondements épistémiques, économiques et rupture agentique) ; `D03`→`D07` (9 liaisons, Interopérabilité protocolaire, découverte et passerelles (MCP, A2A, AGNTCY, AP2) vers Sécurité hors modèle, confinement déterministe (OPA, Règle de deux) et défense SOC) ; `D09`→`D03` (9 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Interopérabilité protocolaire, découverte et passerelles (MCP, A2A, AGNTCY, AP2)) ; `D12`→`D02` (9 liaisons, Homologation vérifiable, trousse exécutable, concordance et Wyvern/G0–G5 vers Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4)) ; `D04`→`D07` (8 liaisons, Sémantique métier, contexte, mémoire CoALA et intégration patrimoniale (ACL/OT) vers Sécurité hors modèle, confinement déterministe (OPA, Règle de deux) et défense SOC) ; `D08`→`D01` (8 liaisons, Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme vers Fondements épistémiques, économiques et rupture agentique) ; `D09`→`D02` (8 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4)) ; `D06`→`D08` (7 liaisons, Identité non humaine (NHI), chaîne de mandat et post-quantique vers Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme) ; `D09`→`D04` (7 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Sémantique métier, contexte, mémoire CoALA et intégration patrimoniale (ACL/OT)) ; `D09`→`D06` (7 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Identité non humaine (NHI), chaîne de mandat et post-quantique) ; `D09`→`D08` (7 liaisons, Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme). La Figure 137 visualise cette matrice `12×12` croisée aux huit types d'interrelations et aux quinze nœuds carrefours dominants.

![Matrice thermique 12×12 des 616 interrelations et quinze nœuds carrefours](././schemas/rendus/SCH-AB-01.svg)

*Figure 137 — SCH-AB-01 : Matrice thermique `12×12` des liaisons inter-domaines (`D01`–`D12`), répartition empilée des huit types d'interrelations sur les 616 arêtes et classement des quinze principaux carrefours relationnels (`mindmap-complet.json`).*

## 4. Synthèse analytique des 67 arbitrages structurels (`tension_arbitrage`)

Les tensions d'arbitrage identifient les compromis architecturaux où l'optimisation locale d'une couche dégrade une garantie de sécurité, de conformité ou de sobriété. Chaque arbitrage est instruit avant toute dérogation et intégralement restitué avec ses extrémités dans le catalogue exhaustif de la section 6.

**Domaine `D01` (6 arbitrages) :** liaisons `REL_0150`, `REL_0218`, `REL_0219`, `REL_0311`, `REL_0575`, `REL_0578`, illustrées par `constance-pass-k` vers `finops-focus-cpo` (Arbitre le coût de vérification face à la fiabilité requise).

**Domaine `D02` (9 arbitrages) :** liaisons `REL_0215`, `REL_0398`, `REL_0515`, `REL_0568`, `REL_0569`, `REL_0570`, `REL_0571`, `REL_0572`, `REL_0573`, illustrées par `echelle-autonomie-l0-l4` vers `supervision-hitl-hotl-abstention` (Montée en autonomie bornée contre capacité cognitive de supervision humaine).

**Domaine `D03` (9 arbitrages) :** liaisons `REL_0014`, `REL_0152`, `REL_0404`, `REL_0459`, `REL_0460`, `REL_0476`, `REL_0498`, `REL_0523`, `REL_0615`, illustrées par `agntcy-slim` vers `protocole-a2a` (Positionnement officiel d'AGNTCY nuancé par chevauchement tiers sur ACP).

**Domaine `D04` (5 arbitrages) :** liaisons `REL_0142`, `REL_0183`, `REL_0206`, `REL_0366`, `REL_0495`, illustrées par `confinement-cua-patrimoine-sans-api` vers `couche-anti-corruption-acl` (Tolère CUA à ≤ 8 % sous bail 12 mois contre refactoring MCP durable).

**Domaine `D05` (7 arbitrages) :** liaisons `REL_0042`, `REL_0124`, `REL_0259`, `REL_0288`, `REL_0530`, `REL_0531`, `REL_0589`, illustrées par `arbre-sobriete-oo1-oo4` vers `protocole-a2a` (Sobriété agent unique face au surcoût multi-agents (-70 % à +80,8 %)).

**Domaine `D06` (6 arbitrages) :** liaisons `REL_0018`, `REL_0117`, `REL_0323`, `REL_0438`, `REL_0439`, `REL_0560`, illustrées par `annuaires-commerciaux-risque-standard-de-fait` vers `anti-verrouillage-standards` (Adoption immédiate d'annuaires propriétaires par rapport à l'attente de normes neutres).

**Domaine `D07` (6 arbitrages) :** liaisons `REL_0144`, `REL_0320`, `REL_0358`, `REL_0379`, `REL_0380`, `REL_0511`, illustrées par `confinement-opensandbox-firecracker-wasi` vers `anti-verrouillage-standards` (Isolation stricte face à la latence et à la complexité KVM).

**Domaine `D08` (5 arbitrages) :** liaisons `REL_0063`, `REL_0201`, `REL_0282`, `REL_0374`, `REL_0613`, illustrées par `banc-evalops-hermetique` vers `finops-focus-cpo` (Coût de simulation face au risque d'erreur en production).

**Domaine `D09` (2 arbitrages) :** liaisons `REL_0226`, `REL_0557`, illustrées par `efvp-transfert-hors-quebec` vers `systems-of-agency` (Souveraineté des données financières face à l'accès aux modèles de pointe).

**Domaine `D10` (6 arbitrages) :** liaisons `REL_0020`, `REL_0022`, `REL_0023`, `REL_0268`, `REL_0423`, `REL_0426`, illustrées par `anti-patrons-agentiques` vers `facades-mcp-intention-metier` (Oppose le mappage rapide OpenAPI 1:1 à la conception par intention).

**Domaine `D11` (4 arbitrages) :** liaisons `REL_0049`, `REL_0051`, `REL_0420`, `REL_0421`, illustrées par `atrophie-competences-humaines` vers `economie-industrialisation-cognitive` (Paradoxe productivité immédiate et érosion de la relève).

**Domaine `D12` (2 arbitrages) :** liaisons `REL_0109`, `REL_0480`, illustrées par `calibration-feds-ema` vers `trajectoires-adaptatives-dapp` (Optimisation du TCO (Scénario A) face à la robustesse minimax (Scénario B)).

## 5. Dynamique causale des sept autres classes d'interrelations (`D01`–`D12`)

Outre les 67 tensions d'arbitrage, les 549 autres arêtes du graphe structurent l'opérationnalisation exécutable, les dépendances techniques, l'encadrement normatif, l'atténuation des risques, les synergies, les projections `2026–2035` et les concordances entre tomes. La totalité des **616 relations** est restituée sans aucune coupure en section 6.

**Opérationnalisation (`operationnalisation`, 129 arêtes) :** domaines moteurs (ex-æquo inclus) `D08` (19), `D10` (16), `D02` (15), `D03` (15), `D12` (15). Liaisons représentatives : `REL_0001` (`actualisation-novembre-2026-unification-v1-2` vers `exigences-cre-ia-305`), `REL_0002` (`actualisation-novembre-2026-unification-v1-2` vers `ligne-directrice-amf`), `REL_0003` (`actualisation-novembre-2026-unification-v1-2` vers `tampon-deterministe-rtr-iso20022`), `REL_0004` (`adaptateur-mcp-streamable-http-sep-3398` vers `protocole-mcp`), `REL_0007` (`agent-card-decouverte` vers `protocole-a2a`).

**Dépendances techniques (`dependance_technique`, 94 arêtes) :** domaines moteurs (ex-æquo inclus) `D03` (26), `D06` (17), `D08` (12), `D04` (10), `D10` (8). Liaisons représentatives : `REL_0006` (`agent-card-decouverte` vers `protocole-a2a`), `REL_0008` (`agent-card-decouverte` vers `signature-agent-card-ancrage`), `REL_0009` (`agntcy-slim` vers `agent-card-decouverte`), `REL_0012` (`agntcy-slim` vers `post-quantique-ml-dsa-slh-dsa`), `REL_0016` (`agntcy-slim` vers `spiffe-spire-attestation`).

**Encadrement normatif (`encadrement_normatif`, 82 arêtes) :** domaines moteurs (ex-æquo inclus) `D09` (59), `D12` (8), `D02` (4), `D03` (4), `D06` (2), `D08` (2). Liaisons représentatives : `REL_0011` (`contrats-interfaces-catalogue-entreprise` vers `agntcy-slim`), `REL_0024` (`bsif-e-23` vers `anti-verrouillage-standards`), `REL_0053` (`avis-acvm-11-348` vers `echelle-autonomie-l0-l4`), `REL_0054` (`avis-acvm-11-348` vers `identite-non-humaine-nhi`), `REL_0056` (`avis-acvm-11-348` vers `profil-gestion-patrimoine-m15`).

**Atténuation de risque (`attenuation_risque`, 82 arêtes) :** domaines moteurs (ex-æquo inclus) `D07` (20), `D04` (13), `D06` (12), `D05` (11), `D02` (9). Liaisons représentatives : `REL_0017` (`alignement-deceptif-red-teaming-adversarial` vers `defense-hors-modele-camel-confinement`), `REL_0019` (`anti-patrons-agentiques` vers `dette-cognitive-vs-technique`), `REL_0027` (`anti-verrouillage-standards` vers `dette-cognitive-vs-technique`), `REL_0028` (`anti-verrouillage-standards` vers `fusion-acp-collision-terminologique`), `REL_0029` (`anti-verrouillage-standards` vers `pieges-gouvernance`).

**Amplification de synergie (`amplification_synergie`, 59 arêtes) :** domaines moteurs (ex-æquo inclus) `D03` (10), `D08` (8), `D04` (6), `D05` (6), `D06` (6). Liaisons représentatives : `REL_0005` (`agent-card-decouverte` vers `agntcy-slim`), `REL_0013` (`agntcy-slim` vers `protocole-a2a`), `REL_0021` (`anti-patrons-agentiques` vers `partition-hybride-80-20`), `REL_0033` (`approbation-ciba` vers `saga-compensatoire`), `REL_0034` (`approbation-ciba` vers `scellage-jcs-scitt`).

**Projections temporelles (`projection_temporelle`, 52 arêtes) :** domaines moteurs (ex-æquo inclus) `D11` (17), `D09` (10), `D06` (7), `D01` (5), `D03` (5). Liaisons représentatives : `REL_0030` (`anti-verrouillage-standards` vers `tri-prospectif-peremption-feuilles-route`), `REL_0058` (`avis-acvm-11-348` vers `trajectoires-adaptatives-dapp`), `REL_0078` (`bsif-e-23` vers `did-vc-passeport-agent`), `REL_0085` (`bsif-e-23` vers `priorites-90-jours-gouvernance`), `REL_0093` (`bsif-e-23` vers `trajectoire-90j-18m-p1-p3`).

**Concordances inter-tomes (`concordance_inter_tomes`, 51 arêtes) :** domaines moteurs (ex-æquo inclus) `D12` (27), `D09` (6), `D01` (3), `D02` (3), `D10` (3). Liaisons représentatives : `REL_0044` (`architecture-collection-tome-1-preambule` vers `cout-non-interop-dette-integration`), `REL_0045` (`architecture-collection-tome-1-preambule` vers `regime-preuve-trois-degres-absence`), `REL_0047` (`architecture-reference-6-couches-2-piliers` vers `noyau-controle-possede-cap`), `REL_0055` (`avis-acvm-11-348` vers `maillage-reglementaire-international`), `REL_0070` (`blueprints-reference-multisectoriels` vers `concordance-inter-tomes-div02`).

### Densité relationnelle par domaine source (`D01`–`D12`)

`D01` totalise 18 arêtes sortantes (`tension_arbitrage` (6), `projection_temporelle` (5), `amplification_synergie` (3), `concordance_inter_tomes` (3), `dependance_technique` (1)) ; `D02` totalise 52 arêtes sortantes (`operationnalisation` (15), `tension_arbitrage` (9), `attenuation_risque` (9), `dependance_technique` (7), `amplification_synergie` (5), `encadrement_normatif` (4), `concordance_inter_tomes` (3)) ; `D03` totalise 77 arêtes sortantes (`dependance_technique` (26), `operationnalisation` (15), `amplification_synergie` (10), `tension_arbitrage` (9), `attenuation_risque` (8), `projection_temporelle` (5), `encadrement_normatif` (4)) ; `D04` totalise 42 arêtes sortantes (`attenuation_risque` (13), `dependance_technique` (10), `amplification_synergie` (6), `tension_arbitrage` (5), `operationnalisation` (4), `concordance_inter_tomes` (2), `projection_temporelle` (2)) ; `D05` totalise 44 arêtes sortantes (`operationnalisation` (14), `attenuation_risque` (11), `tension_arbitrage` (7), `amplification_synergie` (6), `dependance_technique` (6)) ; `D06` totalise 60 arêtes sortantes (`dependance_technique` (17), `attenuation_risque` (12), `operationnalisation` (9), `projection_temporelle` (7), `tension_arbitrage` (6), `amplification_synergie` (6), `encadrement_normatif` (2), `concordance_inter_tomes` (1)) ; `D07` totalise 45 arêtes sortantes (`attenuation_risque` (20), `operationnalisation` (7), `tension_arbitrage` (6), `amplification_synergie` (5), `dependance_technique` (3), `concordance_inter_tomes` (2), `projection_temporelle` (1), `encadrement_normatif` (1)) ; `D08` totalise 55 arêtes sortantes (`operationnalisation` (19), `dependance_technique` (12), `amplification_synergie` (8), `attenuation_risque` (6), `tension_arbitrage` (5), `concordance_inter_tomes` (2), `encadrement_normatif` (2), `projection_temporelle` (1)) ; `D09` totalise 89 arêtes sortantes (`encadrement_normatif` (59), `projection_temporelle` (10), `operationnalisation` (7), `concordance_inter_tomes` (6), `dependance_technique` (2), `amplification_synergie` (2), `tension_arbitrage` (2), `attenuation_risque` (1)) ; `D10` totalise 40 arêtes sortantes (`operationnalisation` (16), `dependance_technique` (8), `tension_arbitrage` (6), `amplification_synergie` (4), `concordance_inter_tomes` (3), `attenuation_risque` (1), `encadrement_normatif` (1), `projection_temporelle` (1)) ; `D11` totalise 35 arêtes sortantes (`projection_temporelle` (17), `operationnalisation` (8), `tension_arbitrage` (4), `concordance_inter_tomes` (2), `attenuation_risque` (1), `amplification_synergie` (1), `encadrement_normatif` (1), `dependance_technique` (1)) ; `D12` totalise 59 arêtes sortantes (`concordance_inter_tomes` (27), `operationnalisation` (15), `encadrement_normatif` (8), `amplification_synergie` (3), `projection_temporelle` (3), `tension_arbitrage` (2), `dependance_technique` (1)).

Les nœuds relais de second rang (rangs 26 à 50) assurent la médiation opérationnelle entre les carrefours principaux : rang 26 `couche-anti-corruption-acl` (`D04`, degré 13, 6 sortantes et 7 entrantes) ; rang 27 `double-couloir-probatoire-pii` (`D08`, degré 13, 7 sortantes et 6 entrantes) ; rang 28 `rag-agentique-contexte` (`D04`, degré 13, 8 sortantes et 5 entrantes) ; rang 29 `partition-hybride-80-20` (`D02`, degré 12, 4 sortantes et 8 entrantes) ; rang 30 `topologies-patrons-orchestration` (`D05`, degré 12, 7 sortantes et 5 entrantes) ; rang 31 `politiques-opa-rego-hors-modele` (`D07`, degré 12, 4 sortantes et 8 entrantes) ; rang 32 `tool-poisoning-rug-pull` (`D07`, degré 12, 1 sortantes et 11 entrantes) ; rang 33 `approbation-ciba` (`D06`, degré 11, 7 sortantes et 4 entrantes) ; rang 34 `noyau-controle-possede-cap` (`D02`, degré 11, 3 sortantes et 8 entrantes) ; rang 35 `constance-pass-k` (`D01`, degré 11, 2 sortantes et 9 entrantes) ; rang 36 `iso-iec-42001-nist` (`D09`, degré 11, 7 sortantes et 4 entrantes) ; rang 37 `dette-semantique-ontologies` (`D04`, degré 11, 5 sortantes et 6 entrantes) ; rang 38 `loi-25-article-12-1` (`D09`, degré 11, 6 sortantes et 5 entrantes) ; rang 39 `protocole-ap2` (`D03`, degré 11, 5 sortantes et 6 entrantes) ; rang 40 `agntcy-slim` (`D03`, degré 10, 7 sortantes et 3 entrantes) ; rang 41 `anti-patrons-agentiques` (`D10`, degré 10, 5 sortantes et 5 entrantes) ; rang 42 `blueprints-reference-multisectoriels` (`D10`, degré 10, 5 sortantes et 5 entrantes) ; rang 43 `protocole-wyvern-g0-g5` (`D12`, degré 10, 4 sortantes et 6 entrantes) ; rang 44 `concordance-inter-tomes-div02` (`D12`, degré 10, 6 sortantes et 4 entrantes) ; rang 45 `choregraphie-event-mesh` (`D05`, degré 10, 7 sortantes et 3 entrantes) ; rang 46 `systems-of-agency` (`D01`, degré 10, 3 sortantes et 7 entrantes) ; rang 47 `efvp-transfert-hors-quebec` (`D09`, degré 10, 6 sortantes et 4 entrantes) ; rang 48 `gouvernance-duale-ae-as` (`D11`, degré 9, 2 sortantes et 7 entrantes) ; rang 49 `memoire-coala-4-tiroirs` (`D04`, degré 9, 7 sortantes et 2 entrantes) ; rang 50 `agent-card-decouverte` (`D03`, degré 8, 4 sortantes et 4 entrantes).

<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->
## 6. Catalogue intégral des 616 interrelations typées (`REL_0001`–`REL_0616`)

### `operationnalisation` (129 relations)

- **`REL_0001`** (`D12` → `D12`, `actualisation-novembre-2026-unification-v1-2` → `exigences-cre-ia-305`) : Intègre 18 exigences et porte le registre de 287 à 305.
- **`REL_0002`** (`D12` → `D09`, `actualisation-novembre-2026-unification-v1-2` → `ligne-directrice-amf`) : Absorbe les reports de la Note AMF IA en exigences normatives.
- **`REL_0003`** (`D12` → `D10`, `actualisation-novembre-2026-unification-v1-2` → `tampon-deterministe-rtr-iso20022`) : Corrige l'omission RTR du 9 novembre 2026 par EXIG-CON-29.
- **`REL_0004`** (`D03` → `D03`, `adaptateur-mcp-streamable-http-sep-3398` → `protocole-mcp`) : Profil de transport épinglé et adaptateur post-gel de MCP.
- **`REL_0007`** (`D03` → `D03`, `agent-card-decouverte` → `protocole-a2a`) : Catalogue interne gouvernant la 4e opération (approuver).
- **`REL_0010`** (`D03` → `D03`, `agntcy-slim` → `agent-card-decouverte`) : Schémas OASF et annuaire distribué AGNTCY.
- **`REL_0015`** (`D03` → `D06`, `agntcy-slim` → `registres-gouvernes-trois-modeles`) : Service d'annuaire AGNTCY ADS spécifiant le magasin fédéré.
- **`REL_0025`** (`D09` → `D03`, `clauses-contractuelles-normatives-app` → `anti-verrouillage-standards`) : Inscrit la réversibilité dans les 10 clauses.
- **`REL_0026`** (`D09` → `D03`, `criteres-evaluation-fournisseurs-grille` → `anti-verrouillage-standards`) : Vérifie portabilité et identité avant achat.
- **`REL_0039`** (`D05` → `D05`, `frameworks-orchestration-entreprise` → `arbre-sobriete-oo1-oo4`) : Portage des options OO1–OO4 dans les cadriciels GA.
- **`REL_0040`** (`D05` → `D02`, `arbre-sobriete-oo1-oo4` → `partition-hybride-80-20`) : Sélection OO1–OO4 pour maintenir le déterminisme par défaut.
- **`REL_0043`** (`D05` → `D05`, `topologies-patrons-orchestration` → `arbre-sobriete-oo1-oo4`) : Déploiement OO3/OO4 via les 8 patrons homologués.
- **`REL_0048`** (`D10` → `D02`, `blueprints-reference-multisectoriels` → `architecture-reference-six-couches-pc1-pc5`) : Instanciation des 6 couches et PC1–PC5 dans le blueprint C1–C8.
- **`REL_0059`** (`D08` → `D01`, `banc-evalops-hermetique` → `constance-pass-k`) : Exécution CI/CD E1–E3 de la constance pass^k.
- **`REL_0060`** (`D08` → `D02`, `banc-evalops-hermetique` → `criteres-qos-cout-precision-latence`) : Mesure de manière reproductible latence PEP, conformité A2A et coût.
- **`REL_0062`** (`D08` → `D08`, `banc-evalops-hermetique` → `finops-focus-cpo`) : Sélectionne le plus petit modèle suffisant sur jeu de référence.
- **`REL_0066`** (`D12` → `D12`, `barriere-logicielle-g0-execute-g0` → `protocole-wyvern-g0-g5`) : Ancre logicielle à exit 0 en amont des barrières éditoriales G1–G5.
- **`REL_0067`** (`D10` → `D10`, `blueprint-1-assistant-sor` → `blueprints-reference-multisectoriels`) : Instanciation du Blueprint 1 orienté systèmes d'enregistrement.
- **`REL_0068`** (`D10` → `D10`, `blueprint-2-enclave-rag-acl` → `blueprints-reference-multisectoriels`) : Instanciation souveraine à haute confidentialité avec RAG ACL.
- **`REL_0069`** (`D10` → `D10`, `blueprint-3-maillage-b2b` → `blueprints-reference-multisectoriels`) : Instanciation du maillage inter-départemental et B2B.
- **`REL_0072`** (`D10` → `D02`, `blueprints-reference-multisectoriels` → `noyau-controle-possede-cap`) : Instancie les 4 plans en 3 architectures complètes.
- **`REL_0075`** (`D08` → `D09`, `banc-evalops-hermetique` → `bsif-e-23`) : Validation indépendante continue E-23.
- **`REL_0084`** (`D02` → `D09`, `pont-reglementation-frames-deterministes` → `bsif-e-23`) : Traduction des attentes E-23 en frames déterministes.
- **`REL_0089`** (`D11` → `D09`, `registre-agents-cycle-de-vie-et-attestations` → `bsif-e-23`) : Utilise le registre d'entreprise comme inventaire E-23.
- **`REL_0096`** (`D03` → `D03`, `contrats-interfaces-catalogue-entreprise` → `cadre-eif-4-couches`) : Impose revue 4 niveaux et accords d'interface.
- **`REL_0101`** (`D02` → `D10`, `cadre-togaf-archimate-4-plans` → `blueprints-reference-multisectoriels`) : Formalisation ArchiMate du blueprint d'entreprise.
- **`REL_0102`** (`D02` → `D12`, `cadre-togaf-archimate-4-plans` → `exigences-cre-ia-305`) : Formalise les contrôles EA/SA dans le gabarit ADR.
- **`REL_0106`** (`D05` → `D05`, `cadriciels-orchestration-portabilite` → `topologies-patrons-orchestration`) : Implémente les graphes d'état et équipes en LangGraph/CrewAI/MAF/ADK.
- **`REL_0110`** (`D05` → `D05`, `canal-compensation-isole-outbox` → `saga-compensatoire`) : Garantie d'isolation et de persistance de la Saga compensatoire.
- **`REL_0113`** (`D02` → `D02`, `catalogue-31-adr-12-dec` → `cadre-togaf-archimate-4-plans`) : Conversion des ADR en 12 contrats neutres DEC.
- **`REL_0114`** (`D08` → `D08`, `caviardage-pii-rp-bilingue` → `double-couloir-probatoire-pii`) : Met en œuvre le couloir opérationnel sans PII du double couloir.
- **`REL_0123`** (`D05` → `D05`, `choregraphie-event-mesh` → `saga-compensatoire`) : Exécute la compensation probabiliste par CloudEvents et Outbox.
- **`REL_0125`** (`D12` → `D12`, `trousse-executable-tome-8` → `cinq-blocs-sbb-tableau-12`) : Comble de façon exécutable les 5 emplacements SBB du Tableau 12 du Tome 2.
- **`REL_0127`** (`D09` → `D09`, `classes-risque-agents-et-plafonds` → `iso-iec-42001-nist`) : Déclenche l'évaluation d'impact unifiée en classe élevée.
- **`REL_0148`** (`D07` → `D07`, `confinement-shadi-sandbox` → `politiques-opa-rego-hors-modele`) : Applique le refus réseau par défaut au niveau manifeste.
- **`REL_0157`** (`D12` → `D08`, `contrats-types-executes-ci-annexe-c` → `scellage-jcs-scitt`) : Démontre en CI la chaîne cryptographique JCS SHA-256.
- **`REL_0158`** (`D07` → `D07`, `controle-surete-stamp-stpa` → `soc-soar-coupe-circuit`) : Convertit l'analyse STPA en coupe-circuits et signaux.
- **`REL_0164`** (`D04` → `D01`, `couche-anti-corruption-acl` → `systems-of-agency`) : Relie le System of Action aux SoR IBM i et z/OS via MCP.
- **`REL_0165`** (`D05` → `D01`, `choregraphie-event-mesh` → `cout-non-interop-dette-integration`) : Event Mesh opérationnalisant le découplage spatial et temporel.
- **`REL_0166`** (`D03` → `D01`, `contrats-api-versionnement-conformite` → `cout-non-interop-dette-integration`) : Invariant découplage-contrat-évolution matérialisé par les API.
- **`REL_0171`** (`D02` → `D12`, `decisions-architecture-adr-001-031` → `homologation-prr-75-points`) : De l'ADR aux 75 preuves PRR pré-production.
- **`REL_0187`** (`D06` → `D06`, `did-vc-passeport-agent` → `delegation-obo-deux-sauts`) : Chaîne de mandat comme troisième pièce du passeport.
- **`REL_0188`** (`D06` → `D03`, `did-vc-passeport-agent` → `protocole-a2a`) : Ancre l'identité légale des pairs A2A inter-firmes.
- **`REL_0190`** (`D06` → `D06`, `did-vc-passeport-agent` → `registres-gouvernes-trois-modeles`) : Inscription au registre comme deuxième pièce du passeport.
- **`REL_0192`** (`D08` → `D01`, `dimensionnement-wilson-evalops` → `constance-pass-k`) : Convertit pass^k en seuil statistique de Wilson.
- **`REL_0194`** (`D02` → `D02`, `distinction-agent-flux-ambiant` → `partition-hybride-80-20`) : Sépare N0 déterministe et boucle agentique.
- **`REL_0200`** (`D08` → `D09`, `double-couloir-probatoire-pii` → `loi-25-article-12-1`) : Alimente le dossier de décision art. 12.1 hors télémétrie.
- **`REL_0203`** (`D08` → `D08`, `double-couloir-probatoire-pii` → `scellage-jcs-scitt`) : Scelle les enregistrements d'audit sans exposer le contenu.
- **`REL_0208`** (`D08` → `D01`, `evaluation-agentique-bancs-capacite` → `echanges-intentions-contrats-probabilistes`) : Vérification statistique des contrats comportementaux probabilistes.
- **`REL_0209`** (`D07` → `D07`, `echec-ferme-opa-default-deny` → `politiques-opa-rego-hors-modele`) : Garantit le mode fermé strict des politiques OPA/Rego.
- **`REL_0220`** (`D09` → `D09`, `clauses-contractuelles-normatives-app` → `efvp-transfert-hors-quebec`) : Constitue l'entente écrite art. 17 et encadre le CLOUD Act.
- **`REL_0230`** (`D05` → `D02`, `enveloppes-bpmn-cas-routine` → `partition-hybride-80-20`) : Matérialise le contrôle déterministe en BPMN 2.0 / CMMN / Routine.
- **`REL_0241`** (`D09` → `D09`, `clauses-contractuelles-normatives-app` → `eu-ai-act`) : Impose l'accord écrit art. 25(4) avec les tiers.
- **`REL_0250`** (`D02` → `D09`, `supervision-hitl-hotl-abstention` → `eu-ai-act`) : Contrôle humain effectif art. 14 par HOTL.
- **`REL_0252`** (`D08` → `D01`, `evaluation-agentique-bancs-capacite` → `constance-pass-k`) : τ-bench et HAL opérationnalisent l'évaluation à coût et consistance contrôlés.
- **`REL_0258`** (`D05` → `D05`, `execution-durable-temporal` → `saga-compensatoire`) : Fournit persistance et reprise aux étapes et compensations.
- **`REL_0261`** (`D08` → `D12`, `banc-evalops-hermetique` → `exigences-cre-ia-305`) : Vérifie syntaxiquement les 108 blocs CI et badges probatoires DC-P11.
- **`REL_0263`** (`D12` → `D12`, `grille-homologation-et-fiche-agent` → `exigences-cre-ia-305`) : Projette les 305 exigences dans la grille d'homologation.
- **`REL_0270`** (`D03` → `D03`, `facades-mcp-intention-metier` → `protocole-mcp`) : Adapte MCP à la production par 5–12 outils métier et structuredContent.
- **`REL_0272`** (`D10` → `D02`, `federation-multi-plateformes-gravite` → `noyau-controle-possede-cap`) : Applique le noyau possédé sur 5 suites SaaS via un plan neutre.
- **`REL_0279`** (`D10` → `D02`, `fil-rouge-groupe-boreal-bel` → `architecture-reference-6-couches-2-piliers`) : Illustre l'architecture 6 couches et 2 piliers de bout en bout.
- **`REL_0286`** (`D08` → `D08`, `finops-focus-cpo` → `plan-inference-routage-carbone`) : Pilotage du routage frugal et des lots par le CPO.
- **`REL_0292`** (`D12` → `D12`, `gabarit-typst-edition-4542-pages` → `protocole-wyvern-g0-g5`) : Matérialise l'assurance qualité G1–G5 et l'édition unifiée du corpus.
- **`REL_0298`** (`D11` → `D02`, `gouvernance-duale-ae-as` → `noyau-controle-possede-cap`) : Exploitation en étoile à 3 lignes du noyau possédé.
- **`REL_0300`** (`D09` → `D06`, `gouvernance-interne-registre-trois-lignes` → `identite-non-humaine-nhi`) : Inventaire gouverné relié aux Blueprints NHI.
- **`REL_0301`** (`D11` → `D11`, `gouvernance-raci-modele-en-etoile` → `registre-agents-cycle-de-vie-et-attestations`) : Affecte les rôles R et A nommés sur chaque fiche.
- **`REL_0302`** (`D06` → `D06`, `grille-cinq-questions-identite` → `annuaires-commerciaux-risque-standard-de-fait`) : Épreuve de la grille sur les annuaires d'entreprise.
- **`REL_0303`** (`D06` → `D06`, `grille-cinq-questions-identite` → `registres-gouvernes-trois-modeles`) : Épreuve de la grille sur le registre gouverné CSA.
- **`REL_0304`** (`D06` → `D06`, `grille-cinq-questions-identite` → `signature-agent-card-ancrage`) : Épreuve de la grille Q-A..Q-E sur l'Agent Card signée.
- **`REL_0305`** (`D06` → `D07`, `grille-cinq-questions-identite` → `taxonomie-attaques-identite-mandataire-confus`) : Grille utilisée comme axe de tri des attaques identitaires.
- **`REL_0306`** (`D02` → `D10`, `grille-evaluation-maturite-n1-n5` → `anti-patrons-agentiques`) : Moteur Python de détection et triage N1–N5.
- **`REL_0317`** (`D06` → `D06`, `spiffe-spire-attestation` → `identite-non-humaine-nhi`) : Délivre l'identité sans secret statique via SVID/OIDC.
- **`REL_0318`** (`D08` → `D09`, `indicateurs-agentops-horizon-tache` → `feuille-route-1er-mai-2027`) : Traduction des métriques AgentOps en KPI de risque de modèle.
- **`REL_0327`** (`D08` → `D09`, `banc-evalops-hermetique` → `iso-iec-42001-nist`) : Cycle PDCA ISO 42001 câblé en CI/CD.
- **`REL_0329`** (`D12` → `D09`, `exigences-cre-ia-305` → `iso-iec-42001-nist`) : Fédère les preuves des 305 EXIG-* dans un index unique.
- **`REL_0344`** (`D02` → `D09`, `pont-reglementation-frames-deterministes` → `ligne-directrice-amf`) : Traduction de la ligne directrice AMF vers les frames.
- **`REL_0351`** (`D08` → `D09`, `double-couloir-probatoire-pii` → `droit-effacement-portabilite-loi-25`) : Effacement vérifiable via clé DEK client en double couloir probatoire.
- **`REL_0353`** (`D02` → `D09`, `pont-reglementation-frames-deterministes` → `loi-25-article-12-1`) : Traduction de l'article 12.1 en pistes d'explication et révision.
- **`REL_0359`** (`D07` → `D07`, `maillage-agents-pep-pdp-zero-trust` → `politiques-opa-rego-hors-modele`) : Application par le PEP des décisions OPA/CEL du PDP.
- **`REL_0363`** (`D07` → `D03`, `maillage-agents-pep-pdp-zero-trust` → `matrice-protocoles-exigences-reglementaires`) : Comblement des zones Z1–Z5 par les couches de maillage et gouvernance.
- **`REL_0368`** (`D04` → `D09`, `memoire-coala-4-tiroirs` → `efvp-transfert-hors-quebec`) : Localise les magasins mémoire et plongements RP.
- **`REL_0370`** (`D04` → `D02`, `memoire-coala-4-tiroirs` → `patrons-boucle-mono-agent-codeact`) : Boucles mono-agent instanciant le cycle cognitif CoALA.
- **`REL_0371`** (`D04` → `D04`, `memoire-coala-4-tiroirs` → `rag-agentique-contexte`) : Alimente le compilateur de contexte depuis blocs Letta et graphe Graphiti.
- **`REL_0376`** (`D10` → `D04`, `modele-maturite-feuille-360j` → `coexistence-bpm-ipaas-rpa`) : Planifie la sortie du RPA et le Strangler Fig sur 360 jours.
- **`REL_0377`** (`D11` → `D08`, `modele-operationnel-hub-and-spoke` → `finops-focus-cpo`) : Refacturation et propriété budgétaire métier.
- **`REL_0383`** (`D10` → `D02`, `fabrique-agents-certification-reemission` → `noyau-controle-possede-cap`) : Mise en œuvre du registre gouverné via la fabrique d'agents.
- **`REL_0384`** (`D02` → `D02`, `noyau-controle-possede-cap` → `principes-architecture-pri-001-015`) : Matérialisation des 15 PRI en 52 capacités cibles.
- **`REL_0394`** (`D08` → `D08`, `observabilite-otel-genai` → `finops-focus-cpo`) : Capture jetons, latences et attributions de coûts par résultat.
- **`REL_0395`** (`D08` → `D08`, `observabilite-otel-genai` → `indicateurs-agentops-horizon-tache`) : Agrégation des traces OTel vers la grille minimale AgentOps.
- **`REL_0401`** (`D02` → `D03`, `partition-hybride-80-20` → `routage-cognitif-hybride-3-paliers`) : Parcimonie cognitive par arbre et routeur.
- **`REL_0402`** (`D05` → `D02`, `topologies-patrons-orchestration` → `partition-hybride-80-20`) : Place le flux déterministe en patron par défaut.
- **`REL_0403`** (`D03` → `D03`, `passerelle-mcp-ai-gateway` → `anti-verrouillage-standards`) : Rend substituables les fournisseurs de modèles et outils.
- **`REL_0411`** (`D03` → `D07`, `passerelle-mcp-ai-gateway` → `politiques-opa-rego-hors-modele`) : Exécute les 9 contrôles PEP par appel.
- **`REL_0417`** (`D12` → `D12`, `peremption-revalidation-annexe-n` → `exigences-cre-ia-305`) : Intégration datée de la Note AMF IA lors de la revalidation.
- **`REL_0425`** (`D10` → `D11`, `plateforme-iap-gitops-cognitif` → `gouvernance-duale-ae-as`) : Fournit des Golden Paths conformes aux développeurs.
- **`REL_0430`** (`D07` → `D07`, `politiques-opa-rego-hors-modele` → `regle-de-deux-opa`) : Applique déterministement la règle de deux en passerelle.
- **`REL_0441`** (`D06` → `D08`, `post-quantique-ml-dsa-slh-dsa` → `scellage-jcs-scitt`) : Assure le rescellement ML-DSA/SLH-DSA des journaux longs.
- **`REL_0445`** (`D11` → `D02`, `priorites-90-jours-gouvernance` → `noyau-controle-possede-cap`) : Verrouille les 6 fondations déterministes en 90 jours.
- **`REL_0447`** (`D10` → `D02`, `profil-assurance-dommages-m17` → `echelle-autonomie-l0-l4`) : Bimodalité sinistres IARD et PEX-031..035.
- **`REL_0448`** (`D10` → `D02`, `profil-assurance-personnes-m16` → `echelle-autonomie-l0-l4`) : Verrous vie/santé et PEX-021..025.
- **`REL_0449`** (`D10` → `D02`, `profil-banque-m14` → `echelle-autonomie-l0-l4`) : Déclinaison bancaire D1–D8 et PEX-001..005.
- **`REL_0450`** (`D10` → `D02`, `profil-gestion-patrimoine-m15` → `echelle-autonomie-l0-l4`) : Plafonnement patrimoine D2 et PEX-011..015.
- **`REL_0452`** (`D10` → `D10`, `profil-banque-m14` → `profils-financiers-5-secteurs`) : Déclinaison bancaire du socle transversal des 5 profils.
- **`REL_0453`** (`D10` → `D10`, `profil-groupe-diversifie-m18` → `profils-financiers-5-secteurs`) : Synthèse comparative et extension conglomérale.
- **`REL_0457`** (`D03` → `D03`, `protocole-a2a` → `cadre-eif-4-couches`) : Concrétise l'échange syntaxique entre pairs opaques.
- **`REL_0469`** (`D03` → `D03`, `protocole-mcp` → `cadre-eif-4-couches`) : Concrétise les couches technique et syntaxique agent-outil.
- **`REL_0471`** (`D03` → `D04`, `protocole-mcp` → `couche-anti-corruption-acl`) : Expose les API existantes en outils orientés tâche.
- **`REL_0474`** (`D03` → `D03`, `passerelle-mcp-ai-gateway` → `protocole-mcp`) : Médiation et contrôle de trafic MCP par passerelle IA.
- **`REL_0484`** (`D12` → `D12`, `trousse-executable-tome-8` → `protocole-wyvern-g0-g5`) : Scelle les 14 extraits par SHA-256 et vérifie 4 vecteurs tiers.
- **`REL_0486`** (`D05` → `D05`, `protocoles-ressources-physiques-lap` → `saga-compensatoire`) : Transpose bail exclusif et barrière paramétrique aux points de non-retour.
- **`REL_0489`** (`D11` → `D11`, `quinze-portes-homologation-por` → `trajectoires-adaptatives-dapp`) : Jalons de validation par preuves système de la trajectoire DAPP.
- **`REL_0512`** (`D02` → `D06`, `regle-maillon-plus-eleve` → `approbation-ciba`) : Déclenche le jeton signé hors bande pour P3.
- **`REL_0514`** (`D02` → `D07`, `regle-maillon-plus-eleve` → `politiques-opa-rego-hors-modele`) : Qualification High-Water Mark par OPA.
- **`REL_0532`** (`D11` → `D11`, `sanctuarisation-vivier-junior-reprise` → `atrophie-competences-humaines`) : Garantit concrètement le maintien des compétences et la relève.
- **`REL_0536`** (`D08` → `D02`, `scellage-jcs-scitt` → `supervision-hitl-hotl-abstention`) : Enregistre les approbations humaines C.6 dans l'audit C.8.
- **`REL_0538`** (`D05` → `D05`, `semantique-effet-idempotence-uetr` → `saga-compensatoire`) : Instrumentation des effets d'écriture pour compensation saga.
- **`REL_0549`** (`D07` → `D09`, `soc-soar-coupe-circuit` → `incidents-agentiques-et-notification-multiregime`) : Exécute la contention immédiate en temps 1 des incidents.
- **`REL_0577`** (`D09` → `D09`, `systeme-qualite-en-18286-dora-cra` → `eu-ai-act`) : Concrétise les exigences QMS et résilience de l'EU AI Act.
- **`REL_0579`** (`D03` → `D01`, `contrats-interfaces-catalogue-entreprise` → `systems-of-agency`) : Ramène N×M intégrations à N+M contrats.
- **`REL_0584`** (`D08` → `D08`, `tests-metamorphiques-fr-en-sans-oracle` → `banc-evalops-hermetique`) : Complète les bancs pass^k/Wilson par tests sans oracle FR/EN.
- **`REL_0588`** (`D05` → `D05`, `topologies-patrons-orchestration` → `contexte-minimal-delegation-interagents`) : Borne la délégation à 2 niveaux et structure les échanges.
- **`REL_0590`** (`D05` → `D01`, `topologies-patrons-orchestration` → `systems-of-agency`) : Structure la couche System of Action en 8 patrons bornés (+ 1 variante débat).
- **`REL_0593`** (`D11` → `D11`, `trajectoire-90j-18m-p1-p3` → `trajectoires-adaptatives-dapp`) : Cadencement des 43 INI et 15 POR sur P1–P3.
- **`REL_0602`** (`D12` → `D12`, `trousse-executable-tome-8` → `exigences-cre-ia-305`) : Exécute les 24 PRR, 5 SBB, 2027-B001 et C01–C40 à exit 0.
- **`REL_0603`** (`D12` → `D02`, `trousse-executable-tome-8` → `partition-hybride-80-20`) : Code le harnais 80/20 dans harness_proto/.
- **`REL_0604`** (`D12` → `D07`, `trousse-executable-tome-8` → `regle-de-deux-opa`) : Implémente la Règle de deux et CaMeL en Rego.
- **`REL_0605`** (`D12` → `D05`, `trousse-executable-tome-8` → `saga-dix-scenarios-fautes`) : Vérifie EXIG-ORC-20 sur SQLite WAL.
- **`REL_0609`** (`D02` → `D02`, `validation-json-schema-ambigu-escalade` → `harnais-deterministe-8-etapes`) : Contrat de schéma et porte d'escalade du harnais 8 étapes.
- **`REL_0616`** (`D03` → `D03`, `web-agentique-webmcp-webbotauth` → `protocole-mcp`) : Étend l'exposition d'outils côté navigateur et canaux web.

### `dependance_technique` (94 relations)

- **`REL_0006`** (`D03` → `D03`, `agent-card-decouverte` → `protocole-a2a`) : Découverte A2A par Agent Card.
- **`REL_0008`** (`D03` → `D06`, `agent-card-decouverte` → `signature-agent-card-ancrage`) : Authenticité de la découverte liée à la signature JWS.
- **`REL_0009`** (`D03` → `D03`, `agntcy-slim` → `agent-card-decouverte`) : Étend les cartes A2A via schémas OASF et ADS.
- **`REL_0012`** (`D03` → `D06`, `agntcy-slim` → `post-quantique-ml-dsa-slh-dsa`) : Chiffre les canaux gRPC par IETF MLS X25519MLKEM768.
- **`REL_0016`** (`D03` → `D06`, `agntcy-slim` → `spiffe-spire-attestation`) : Authentifie les nœuds de session via SVID SPIFFE/SPIRE mTLS.
- **`REL_0031`** (`D06` → `D05`, `approbation-ciba` → `execution-durable-temporal`) : Mise en veille durable pendant l'attente humaine.
- **`REL_0032`** (`D06` → `D03`, `approbation-ciba` → `passerelle-mcp-ai-gateway`) : Rétention du jeton CIBA et calcul de h au PEP.
- **`REL_0035`** (`D06` → `D08`, `approbation-ciba` → `scellage-jcs-scitt`) : Canonise les paramètres d'action via JCS (RFC 8785).
- **`REL_0046`** (`D02` → `D04`, `architecture-outils-fiables-erreurs-actionnables` → `formats-echange-registres-schemas`) : Validation des appels d'outils par JSON Schema.
- **`REL_0065`** (`D08` → `D11`, `banc-evalops-hermetique` → `registre-agents-cycle-de-vie-et-attestations`) : Relance E1–E2 à chaque déclencheur de réévaluation.
- **`REL_0073`** (`D10` → `D03`, `blueprints-reference-multisectoriels` → `passerelle-mcp-ai-gateway`) : Repose sur les passerelles MCP et AI unifiées.
- **`REL_0104`** (`D02` → `D03`, `cadre-togaf-archimate-4-plans` → `passerelle-mcp-ai-gateway`) : Fait de la passerelle le passage obligé de couche 4.
- **`REL_0112`** (`D08` → `D08`, `canonisation-deterministe-jcs` → `scellage-jcs-scitt`) : Socle de canonisation avant scellement SCITT et SLH-DSA.
- **`REL_0116`** (`D06` → `D06`, `certificats-tls-47-jours` → `post-quantique-ml-dsa-slh-dsa`) : Automatisation ACME 47 jours préalable au PQC.
- **`REL_0121`** (`D05` → `D05`, `choregraphie-event-mesh` → `execution-durable-temporal`) : Reprise durable et ordonnancement d'événements asynchrones.
- **`REL_0122`** (`D05` → `D05`, `choregraphie-event-mesh` → `saga-compensatoire`) : Exige un coordinateur et une saga en chorégraphie à effets.
- **`REL_0155`** (`D03` → `D03`, `contrats-interfaces-catalogue-entreprise` → `passerelle-mcp-ai-gateway`) : Alimente la liste d'autorisation de la passerelle.
- **`REL_0156`** (`D12` → `D06`, `contrats-types-executes-ci-annexe-c` → `post-quantique-ml-dsa-slh-dsa`) : Publie le schéma crypto-agile ES256/ML-DSA-65/ML-DSA-87.
- **`REL_0162`** (`D04` → `D05`, `couche-anti-corruption-acl` → `execution-durable-temporal`) : Vérifie l'idempotence via service cible ou adaptateur.
- **`REL_0163`** (`D04` → `D03`, `couche-anti-corruption-acl` → `protocole-mcp`) : Encapsulation RPG/SAP exposée derrière une façade MCP.
- **`REL_0168`** (`D09` → `D09`, `criteres-evaluation-fournisseurs-grille` → `clauses-contractuelles-normatives-app`) : Conditionne l'admissibilité à l'acceptation des clauses DOIT.
- **`REL_0169`** (`D06` → `D06`, `crypto-agilite-migration-pqc` → `inventaire-revocation-asymetrie`) : Migration PQC bloquée par l'absence de retrait cryptographique.
- **`REL_0170`** (`D06` → `D06`, `crypto-agilite-migration-pqc` → `post-quantique-ml-dsa-slh-dsa`) : Migration vers les primitives normalisées FIPS 203/204/205.
- **`REL_0176`** (`D06` → `D06`, `delegation-obo-deux-sauts` → `identite-non-humaine-nhi`) : Délégation multi-saut dépendant d'une identité d'agent distincte.
- **`REL_0178`** (`D06` → `D06`, `delegation-obo-deux-sauts` → `profil-oauth-9700-et-liaison-expediteur`) : Lie les jetons délégués à l'expéditeur via mTLS ou DPoP.
- **`REL_0180`** (`D06` → `D06`, `delegation-obo-deux-sauts` → `spiffe-spire-attestation`) : Authentification sans secret du STS par SVID.
- **`REL_0184`** (`D04` → `D03`, `dette-semantique-ontologies` → `epinglage-schemas-mcp`) : Impose un incrément majeur sur changement de sens.
- **`REL_0189`** (`D06` → `D08`, `did-vc-passeport-agent` → `provenance-artefacts-aibom-5-horloges`) : Cinquième pièce candidate du passeport issue de la provenance logicielle.
- **`REL_0197`** (`D04` → `D06`, `donnees-pretes-agents-odcs-openlineage` → `delegation-obo-deux-sauts`) : Applique le filtrage au niveau ligne/colonne sous identité déléguée.
- **`REL_0202`** (`D08` → `D08`, `double-couloir-probatoire-pii` → `scellage-jcs-scitt`) : Archivage probatoire long terme des décisions.
- **`REL_0207`** (`D01` → `D04`, `echanges-intentions-contrats-probabilistes` → `ecart-accord-protocolaire-comprehension`) : Échange d'intentions déplaçant le verrou au palier sémantique/pragmatique.
- **`REL_0214`** (`D02` → `D02`, `echelle-autonomie-l0-l4` → `regle-maillon-plus-eleve`) : Combine niveau N0–N4, classe et palier P0–P3.
- **`REL_0223`** (`D09` → `D03`, `efvp-transfert-hors-quebec` → `passerelle-mcp-ai-gateway`) : Bloque techniquement les routes hors Québec non couvertes.
- **`REL_0227`** (`D04` → `D04`, `encapsulation-patrimoine-it-ot` → `couche-anti-corruption-acl`) : Migration des CUA vers adaptateurs MCP décimaux.
- **`REL_0228`** (`D04` → `D06`, `encapsulation-patrimoine-it-ot` → `spiffe-spire-attestation`) : Authentifie le passage de la zone IT à l'IDMZ niveau 3.5.
- **`REL_0232`** (`D03` → `D03`, `epinglage-schemas-mcp` → `protocole-mcp`) : S'ancre sur Streamable HTTP 2026-07-28.
- **`REL_0254`** (`D05` → `D06`, `execution-durable-temporal` → `approbation-ciba`) : Suspend sans coût le flux de travail sur awakeable jusqu'au retour CIBA.
- **`REL_0256`** (`D05` → `D04`, `execution-durable-temporal` → `couche-anti-corruption-acl`) : S'appuie sur l'idempotence devant les SoR.
- **`REL_0257`** (`D05` → `D05`, `execution-durable-temporal` → `saga-compensatoire`) : Persiste l'état, la clé d'idempotence et le journal de compensation.
- **`REL_0267`** (`D10` → `D08`, `fabrique-agents-certification-reemission` → `cycle-vie-operationnel-derives-gitops`) : Pipeline GitOps de réémission et promotion des gabarits.
- **`REL_0269`** (`D10` → `D08`, `fabrique-agents-certification-reemission` → `evaluation-continue-derives`) : Barrière de certification alimentée par les bancs d'évaluation.
- **`REL_0281`** (`D10` → `D04`, `fil-rouge-groupe-boreal-bel` → `encapsulation-patrimoine-it-ot`) : Façades d'accès aux cœurs métier et données existantes.
- **`REL_0284`** (`D08` → `D08`, `finops-focus-cpo` → `observabilite-otel-genai`) : Imputation CPO sur spans OTel gen_ai.*.
- **`REL_0310`** (`D02` → `D02`, `harnais-deterministe-8-etapes` → `partition-hybride-80-20`) : Repose sur la frontière stricte contrôle/modèle.
- **`REL_0313`** (`D06` → `D06`, `identite-non-humaine-nhi` → `delegation-obo-deux-sauts`) : Identifie l'agent comme acteur distinct dans le jeton délégué.
- **`REL_0316`** (`D06` → `D08`, `identite-non-humaine-nhi` → `observabilite-otel-genai`) : Corrèle les trois identités de chaque action dans les traces.
- **`REL_0335`** (`D08` → `D06`, `journalisation-probatoire-audit` → `did-vc-passeport-agent`) : Corrélation de la trace OTel à l'identité du passeport mandataire.
- **`REL_0337`** (`D06` → `D06`, `kya-verification-agent-tiers` → `did-vc-passeport-agent`) : Admission KYA inter-domaines requérant un passeport portable.
- **`REL_0339`** (`D06` → `D06`, `liaison-jetons-dpop-mtls` → `delegation-obo-deux-sauts`) : Liaison à l'expéditeur requise pour sécuriser l'échange OBO.
- **`REL_0360`** (`D07` → `D06`, `maillage-agents-pep-pdp-zero-trust` → `spiffe-spire-attestation`) : Attestation cryptographique de charge de travail à l'arête.
- **`REL_0361`** (`D03` → `D06`, `maillage-b2b-federe-edc-odrl` → `did-vc-passeport-agent`) : Identité légale vLEI et VC sur canal EDC.
- **`REL_0381`** (`D02` → `D03`, `noyau-controle-possede-cap` → `agent-card-decouverte`) : S'appuie sur un registre de référence faisant autorité.
- **`REL_0386`** (`D08` → `D05`, `observabilite-otel-genai` → `choregraphie-event-mesh`) : Continuité W3C Trace Context sur courtiers.
- **`REL_0388`** (`D08` → `D08`, `observabilite-otel-genai` → `double-couloir-probatoire-pii`) : Collecteur OTel épinglé alimentant le couloir 1.
- **`REL_0393`** (`D08` → `D08`, `observabilite-otel-genai` → `finops-focus-cpo`) : Fournit jetons, modèle servi et `cost_center` pour le CPO.
- **`REL_0396`** (`D08` → `D03`, `observabilite-otel-genai` → `protocole-mcp`) : Propagation du contexte de trace dans les métadonnées MCP.
- **`REL_0405`** (`D03` → `D05`, `passerelle-mcp-ai-gateway` → `choregraphie-event-mesh`) : Couplage passerelle synchrone et bus événementiel asynchrone.
- **`REL_0406`** (`D03` → `D06`, `passerelle-mcp-ai-gateway` → `delegation-obo-deux-sauts`) : Porte l'échange RFC 8693 et la preuve DPoP entre agent et outil.
- **`REL_0410`** (`D03` → `D07`, `passerelle-mcp-ai-gateway` → `politiques-opa-rego-hors-modele`) : Exécute les décisions PDP Cedar/OPA/CEL comme PEP obligatoire.
- **`REL_0412`** (`D03` → `D03`, `passerelle-mcp-ai-gateway` → `protocole-a2a`) : Médiation PEP et vérification JWS/JCS des flux A2A.
- **`REL_0413`** (`D03` → `D03`, `passerelle-mcp-ai-gateway` → `protocole-mcp`) : Coupure PEP obligatoire sur transport MCP.
- **`REL_0424`** (`D10` → `D05`, `plateforme-iap-gitops-cognitif` → `execution-durable-temporal`) : Exige le Worker Versioning pour les livraisons en vol.
- **`REL_0427`** (`D07` → `D06`, `politiques-opa-rego-hors-modele` → `identite-non-humaine-nhi`) : Décision PDP fondée sur identité et parrainage NHI.
- **`REL_0429`** (`D07` → `D03`, `politiques-opa-rego-hors-modele` → `passerelle-mcp-ai-gateway`) : Coupure réseau obligatoire au PEP.
- **`REL_0437`** (`D06` → `D06`, `post-quantique-ml-dsa-slh-dsa` → `delegation-obo-deux-sauts`) : Impose des Transaction Tokens O(1) face à HTTP 431.
- **`REL_0442`** (`D06` → `D06`, `post-quantique-ml-dsa-slh-dsa` → `spiffe-spire-attestation`) : Renouvellement de l'infrastructure cryptographique sous-jacente.
- **`REL_0451`** (`D10` → `D04`, `profils-financiers-5-secteurs` → `dette-semantique-ontologies`) : Ancrage sectoriel sur les vocabulaires métiers établis.
- **`REL_0455`** (`D03` → `D03`, `protocole-a2a` → `agent-card-decouverte`) : Délégation A2A reposant sur l'Agent Card bien connue.
- **`REL_0456`** (`D03` → `D03`, `protocole-a2a` → `agntcy-slim`) : S'appuie sur SLIM/OASF pour le routage bas niveau et multipartite.
- **`REL_0458`** (`D03` → `D06`, `protocole-a2a` → `delegation-obo-deux-sauts`) : Transporte la chaîne de mandat à chaque saut A2A.
- **`REL_0461`** (`D03` → `D06`, `protocole-anp-did-wba` → `did-vc-passeport-agent`) : ANP subordonné à la maturité de l'infrastructure DID.
- **`REL_0463`** (`D03` → `D06`, `protocole-ap2` → `delegation-obo-deux-sauts`) : Chaîne cryptographique des mandats Intent → Cart → Payment.
- **`REL_0464`** (`D03` → `D06`, `protocole-ap2` → `did-vc-passeport-agent`) : Mandats AP2 sérialisés en attestations vérifiables.
- **`REL_0465`** (`D03` → `D04`, `protocole-ap2` → `iso-20022-lynx-rtr`) : Dépendance d'exécution envers le rail de paiement réglementé sous-jacent.
- **`REL_0466`** (`D03` → `D03`, `protocole-ap2` → `protocole-a2a`) : AP2 opérant comme protocole compagnon au-dessus d'A2A.
- **`REL_0472`** (`D03` → `D03`, `protocole-mcp` → `epinglage-schemas-mcp`) : Exige JSON Schema 2020-12 et empreintes vérifiées.
- **`REL_0477`** (`D03` → `D06`, `protocole-mcp` → `socle-iam-federe-oauth-fapi`) : Cadre d'autorisation MCP étagé sur OAuth 2.x.
- **`REL_0485`** (`D03` → `D07`, `protocoles-interfaces-agui-a2ui-webrtc` → `confinement-shadi-sandbox`) : Rend les composants UI tiers sans exécution de code arbitraire.
- **`REL_0491`** (`D04` → `D04`, `rag-agentique-contexte` → `dette-semantique-ontologies`) : GraphRAG adossé aux graphes de connaissances et ontologies.
- **`REL_0492`** (`D04` → `D04`, `rag-agentique-contexte` → `donnees-pretes-agents-odcs-openlineage`) : Exige des sources indexées avec lignage, fraîcheur et ACL héritées.
- **`REL_0497`** (`D04` → `D03`, `rag-agentique-contexte` → `protocole-mcp`) : Accès structuré aux bases via serveur MCP.
- **`REL_0516`** (`D10` → `D04`, `reprise-sinistre-cognitif-continuite` → `rag-agentique-contexte`) : Plongements internes ouverts pour continuité RAG.
- **`REL_0519`** (`D10` → `D06`, `reseaux-b2b-federes-p3` → `did-vc-passeport-agent`) : Justification légale vLEI requise en Stade 4 B2B.
- **`REL_0524`** (`D03` → `D03`, `routage-cognitif-hybride-3-paliers` → `passerelle-mcp-ai-gateway`) : Contrat Open Responses pour routage et bascule.
- **`REL_0525`** (`D03` → `D03`, `routage-cognitif-hybride-3-paliers` → `plan-donnees-inference-kv-cache`) : Affinité KV-cache pour multi-tours SLM.
- **`REL_0527`** (`D05` → `D05`, `saga-compensatoire` → `execution-durable-temporal`) : Sagas adossées au journal d'état durable.
- **`REL_0534`** (`D08` → `D08`, `scellage-jcs-scitt` → `double-couloir-probatoire-pii`) : Séparation physique entre audit JCS et traces OTel.
- **`REL_0535`** (`D08` → `D08`, `scellage-jcs-scitt` → `observabilite-otel-genai`) : Corrèle le grand livre C.8 aux traces via lacune 21.
- **`REL_0543`** (`D06` → `D08`, `signature-agent-card-ancrage` → `canonicalisation-jcs-rfc8785`) : Signature JWS exigeant la canonisation JCS RFC 8785.
- **`REL_0566`** (`D02` → `D06`, `supervision-hitl-hotl-abstention` → `approbation-ciba`) : Appuie les files Réviser sur des jetons signés.
- **`REL_0576`** (`D04` → `D06`, `synchronisation-edge-crdt` → `spiffe-spire-attestation`) : Attestation SPIRE locale sur TPM en coupure WAN.
- **`REL_0606`** (`D02` → `D07`, `usine-logicielle-agentic-sdlc` → `confinement-opensandbox-firecracker-wasi`) : Compilation isolée anti-slopsquatting.
- **`REL_0611`** (`D11` → `D11`, `vingt-sept-signaux-veille-sig` → `trajectoires-adaptatives-dapp`) : Déclencheurs mesurables gouvernant les bascules conditionnelles DAPP.
- **`REL_0612`** (`D08` → `D08`, `volant-distillation-dspy-multilora` → `double-couloir-probatoire-pii`) : Curation sur traces assainies Loi 25.

### `encadrement_normatif` (82 relations)

- **`REL_0011`** (`D03` → `D03`, `contrats-interfaces-catalogue-entreprise` → `agntcy-slim`) : Subordonne OASF/ADS au catalogue d'entreprise.
- **`REL_0024`** (`D09` → `D03`, `bsif-e-23` → `anti-verrouillage-standards`) : Exigences de diligence de tiers dans les institutions réglementées.
- **`REL_0053`** (`D09` → `D02`, `avis-acvm-11-348` → `echelle-autonomie-l0-l4`) : Rattachement réglementaire sur l'autonomie et l'adaptativité en valeurs mobilières.
- **`REL_0054`** (`D09` → `D06`, `avis-acvm-11-348` → `identite-non-humaine-nhi`) : Encadrement des systèmes autonomes sur les marchés de capitaux.
- **`REL_0056`** (`D09` → `D10`, `avis-acvm-11-348` → `profil-gestion-patrimoine-m15`) : Responsabilité inscrite, OEO et rétrofacturations 2028.
- **`REL_0057`** (`D09` → `D10`, `avis-acvm-11-348` → `profils-financiers-5-secteurs`) : Fixe les cinq plafonds métier en finance canadienne.
- **`REL_0074`** (`D09` → `D11`, `bsif-e-23` → `atrophie-competences-humaines`) : Exige des scénarios de panne et un repli manuel éprouvé.
- **`REL_0076`** (`D09` → `D02`, `bsif-e-23` → `clauses-sortie-portabilite-interchangeabilite`) : Encadre via BSIF B-10 le risque de concentration et la réversibilité.
- **`REL_0077`** (`D09` → `D04`, `bsif-e-23` → `couche-anti-corruption-acl`) : Exige parité, traçabilité SOX et révision des cellules CUA sur SoR.
- **`REL_0079`** (`D09` → `D02`, `bsif-e-23` → `echelle-autonomie-l0-l4`) : Impose inventaire, matérialité et contrôle par palier dès mai 2027.
- **`REL_0080`** (`D09` → `D11`, `bsif-e-23` → `gouvernance-duale-ae-as`) : Impose inventaire, validation 2LoD et propriété sur le cycle de vie.
- **`REL_0082`** (`D09` → `D08`, `bsif-e-23` → `plan-inference-routage-carbone`) : Mesure portée 3 BSIF B-15 dès l'exercice 2028.
- **`REL_0083`** (`D09` → `D10`, `bsif-e-23` → `plateformes-saas-et-asymetrie-tiers`) : Rend inacceptables les contrôles opaques des plateformes fermées.
- **`REL_0086`** (`D09` → `D10`, `bsif-e-23` → `production-agentique-canadienne-2025-2026`) : Contrainte prudentielle sur les déploiements bancaires canadiens.
- **`REL_0087`** (`D09` → `D10`, `bsif-e-23` → `profil-assurance-personnes-m16`) : Tests génétiques L.C. 2017 ch. 3 et conservation vie.
- **`REL_0088`** (`D09` → `D10`, `bsif-e-23` → `profil-groupe-diversifie-m18`) : Ententes intra-groupe B-10, B-15 et temporisation 2033.
- **`REL_0090`** (`D09` → `D06`, `bsif-e-23` → `registres-gouvernes-trois-modeles`) : Inventaire complet attendu par E-23 convergent avec le registre d'agents.
- **`REL_0091`** (`D09` → `D02`, `bsif-e-23` → `regle-maillon-plus-eleve`) : Fonde la propagation de criticité aux maillons amont.
- **`REL_0092`** (`D09` → `D02`, `bsif-e-23` → `supervision-hitl-hotl-abstention`) : Surveillance continue attendue face aux limites du réviseur humain.
- **`REL_0095`** (`D09` → `D10`, `bsif-e-23` → `vertical-financier-durci`) : Qualification réglementaire de l'inférence agentique comme modèle.
- **`REL_0097`** (`D09` → `D03`, `eu-ai-act` → `cadre-eif-4-couches`) : Basculement vers l'obligation légale via l'Interoperable Europe Act.
- **`REL_0099`** (`D03` → `D03`, `cadre-eif-4-couches` → `protocole-a2a`) : Cadre EIF structurant l'interopérabilité organisationnelle d'A2A.
- **`REL_0100`** (`D03` → `D03`, `cadre-eif-4-couches` → `protocole-mcp`) : Cadre EIF structurant les paliers technique et syntaxique de MCP.
- **`REL_0128`** (`D09` → `D09`, `classes-risque-agents-et-plafonds` → `ligne-directrice-amf`) : Rompt la circularité entre classe et cote de modèle AMF.
- **`REL_0129`** (`D12` → `D09`, `clause-non-avis-licences` → `bsif-e-23`) : Distinction stricte secteur privé et administrations publiques.
- **`REL_0130`** (`D12` → `D12`, `clause-non-avis-licences` → `exigences-cre-ia-305`) : Qualifie CRE-IA et Tome 3 comme consultatifs sans homologation humaine (DC-P01).
- **`REL_0132`** (`D12` → `D12`, `clause-non-avis-licences` → `trousse-executable-tome-8`) : Délimite la portée synthétique DC-P12 et le statut non-avis.
- **`REL_0133`** (`D09` → `D10`, `clauses-reversibilite-cloud-souverain` → `blueprints-reference-multisectoriels`) : Contraintes de neutralité, résidence et portabilité sur le blueprint.
- **`REL_0193`** (`D02` → `D06`, `distinction-agent-flux-ambiant` → `identite-non-humaine-nhi`) : Exclut comptes humains et secrets partagés.
- **`REL_0195`** (`D12` → `D12`, `dix-interdictions-exig-gov-17` → `exigences-cre-ia-305`) : Noyau non dérogeable prioritaire dans l'ordre d'arbitrage CRE-IA.
- **`REL_0204`** (`D02` → `D12`, `douze-principes-directeurs-prin` → `exigences-cre-ia-305`) : Fonde les 305 exigences vérifiables.
- **`REL_0211`** (`D02` → `D09`, `echelle-autonomie-l0-l4` → `classes-risque-agents-et-plafonds`) : Plafonne l'autonomie par la classe de risque.
- **`REL_0216`** (`D10` → `D04`, `eclats-sectoriels-extrapoles` → `encapsulation-patrimoine-it-ot`) : Exclut les systèmes SIS SIL 2/3 du champ probatoire financier démontré.
- **`REL_0221`** (`D09` → `D04`, `efvp-transfert-hors-quebec` → `memoire-bi-temporelle-et-purge`) : Purge et anonymisation des mémoires/traces.
- **`REL_0222`** (`D09` → `D04`, `efvp-transfert-hors-quebec` → `memoire-coala-4-tiroirs`) : Impose l'ÉFVP préalable et la portabilité/purge des RP.
- **`REL_0224`** (`D09` → `D04`, `efvp-transfert-hors-quebec` → `rag-agentique-contexte`) : Restriction transfrontalière sur l'indexation et les inférences hors Québec.
- **`REL_0225`** (`D09` → `D04`, `efvp-transfert-hors-quebec` → `six-substrats-etat-souverainete`) : ÉFVP préalable et encadrement des 6 substrats.
- **`REL_0239`** (`D09` → `D03`, `eu-ai-act` → `anti-verrouillage-standards`) : Impose la réversibilité infonuagique via l'EU Data Act.
- **`REL_0240`** (`D09` → `D09`, `eu-ai-act` → `approvisionnement-reversible-contrats`) : Article 25(4) RIA et article 29 Data Act en EXIG-APP.
- **`REL_0242`** (`D09` → `D02`, `eu-ai-act` → `decisions-architecture-adr-001-031`) : Obligations art. 50 et Annexe III sur les ADR.
- **`REL_0243`** (`D09` → `D12`, `eu-ai-act` → `exigences-cre-ia-305`) : Relie les portes PRR et QMS à DORA et EN 18286:2026.
- **`REL_0244`** (`D09` → `D06`, `eu-ai-act` → `kya-verification-agent-tiers`) : Précédent institutionnel eIDAS 2.0 pour la reconnaissance mutuelle.
- **`REL_0246`** (`D09` → `D10`, `eu-ai-act` → `profils-financiers-5-secteurs`) : Classification à haut risque du crédit et de l'assurance vie/santé.
- **`REL_0247`** (`D09` → `D11`, `eu-ai-act` → `responsabilite-litiges-commerce-agentique`) : Contexte réglementaire européen des transactions et transparence IA.
- **`REL_0248`** (`D09` → `D08`, `eu-ai-act` → `scellage-jcs-scitt`) : Conservation probatoire ≥ 24 mois dépassant RIA art. 26(6).
- **`REL_0249`** (`D09` → `D02`, `eu-ai-act` → `supervision-hitl-hotl-abstention`) : Rend obligatoire la supervision effective et le bouton d'arrêt (art. 14).
- **`REL_0265`** (`D12` → `D07`, `exigences-cre-ia-305` → `politiques-opa-rego-hors-modele`) : Traduit les exigences CRE-IA en garde-fous déterministes vérifiables.
- **`REL_0287`** (`D08` → `D11`, `finops-focus-cpo` → `registre-agents-cycle-de-vie-et-attestations`) : Déclenche la revue de valeur après 2 mois hors cible.
- **`REL_0297`** (`D09` → `D04`, `loi-25-article-12-1` → `gouvernance-acces-rag-ancrage`) : Traçabilité des sources requise pour justifier les décisions.
- **`REL_0307`** (`D12` → `D11`, `grille-homologation-et-fiche-agent` → `regime-derogations-et-transition-cohorte`) : Projette point par point les interdits de EXIG-GOV-17.
- **`REL_0314`** (`D06` → `D05`, `identite-non-humaine-nhi` → `execution-durable-temporal`) : Impose la revalidation du mandat et de la révocation au réveil.
- **`REL_0326`** (`D09` → `D03`, `iso-iec-42001-nist` → `anti-verrouillage-standards`) : Fixe le cadre PDCA et révèle l'absence de norme ISO dédiée aux agents.
- **`REL_0328`** (`D09` → `D12`, `iso-iec-42001-nist` → `exigences-cre-ia-305`) : Complémentarité partielle ISO 42001 (Gouvernance seule).
- **`REL_0330`** (`D09` → `D11`, `iso-iec-42001-nist` → `gouvernance-duale-ae-as`) : Structuration du système de management de l'IA (SMIA).
- **`REL_0331`** (`D09` → `D07`, `iso-iec-42001-nist` → `injection-indirecte-prompt`) : Cadrage NIST AI 100-2 et IMDA v1.5 sur la sécurité agentique.
- **`REL_0332`** (`D09` → `D09`, `iso-iec-42001-nist` → `ligne-directrice-amf`) : Arrimage AIMS pour exigences multi-régimes.
- **`REL_0334`** (`D09` → `D12`, `iso-iec-42001-nist` → `protocole-wyvern-g0-g5`) : Exclut la norme payante ISO 42001 des preuves L+ en T8.
- **`REL_0340`** (`D09` → `D08`, `ligne-directrice-amf` → `banc-evalops-hermetique`) : Encadre l'équité bilingue et la non-substitution d'avis.
- **`REL_0342`** (`D09` → `D12`, `ligne-directrice-amf` → `exigences-cre-ia-305`) : Raccorde 41 attentes AMF et 12 EXIG-AMF à CRE-IA-2026-01-QC.
- **`REL_0343`** (`D09` → `D09`, `ligne-directrice-amf` → `gouvernance-interne-registre-trois-lignes`) : 41 attentes AMF et 12 EXIG-AMF obligatoires.
- **`REL_0345`** (`D09` → `D10`, `ligne-directrice-amf` → `profil-assurance-dommages-m17`) : Formulaires auto art. 71 et ≥ 3 assureurs LDPSF art. 38.
- **`REL_0347`** (`D09` → `D06`, `ligne-directrice-amf` → `registres-gouvernes-trois-modeles`) : Attentes AMF au 1ᵉʳ mai 2027 sur les systèmes adaptatifs.
- **`REL_0348`** (`D09` → `D10`, `ligne-directrice-amf` → `vertical-financier-durci`) : Encadrement prudentiel des institutions financières québécoises.
- **`REL_0350`** (`D09` → `D08`, `loi-25-article-12-1` → `double-couloir-probatoire-pii`) : Zéro PII en télémétrie courante et purge ≤ 14 jours.
- **`REL_0352`** (`D09` → `D04`, `loi-25-article-12-1` → `memoire-partagee-concurrence-effacement`) : Impose l'oubli sélectif et le Crypto-Shredding des faits dérivés.
- **`REL_0354`** (`D09` → `D08`, `loi-25-article-12-1` → `scellage-jcs-scitt`) : Exige la traçabilité des facteurs et paramètres.
- **`REL_0355`** (`D09` → `D02`, `loi-25-article-12-1` → `supervision-hitl-hotl-abstention`) : Obligation légale de révision humaine et d'information sous la Loi 25.
- **`REL_0362`** (`D09` → `D10`, `maillage-reglementaire-international` → `vertical-financier-durci`) : Triple qualification simultanée modèle, TIC DORA et marché.
- **`REL_0373`** (`D03` → `D12`, `metriques-soutien-vs-production` → `regime-preuve-trois-degres-absence`) : Règle anti-amalgame sur les décomptes auto-déclarés de soutien.
- **`REL_0389`** (`D08` → `D08`, `observabilite-otel-genai` → `double-couloir-probatoire-pii`) : Sépare métadonnées OTel et contenu PII hors télémétrie.
- **`REL_0390`** (`D09` → `D08`, `eu-ai-act` → `observabilite-otel-genai`) : Auditabilité opposable inspirée de PSD2 et des obligations d'interface.
- **`REL_0432`** (`D12` → `D12`, `portee-et-force-normative-cre-ia` → `exigences-cre-ia-305`) : Définit la force juridique RFC 2119 des 305 blocs.
- **`REL_0433`** (`D09` → `D06`, `bsif-e-23` → `post-quantique-ml-dsa-slh-dsa`) : Distinction des calendriers PQC face au bulletin quantique BSIF.
- **`REL_0462`** (`D06` → `D03`, `approbation-ciba` → `protocole-ap2`) : Soumet tout paiement agentique à l'approbation P3 signée.
- **`REL_0483`** (`D12` → `D09`, `protocole-wyvern-g0-g5` → `ligne-directrice-amf`) : Exclut les portails bloqués (lautorite.qc.ca) en statut F.
- **`REL_0508`** (`D11` → `D11`, `registre-agents-cycle-de-vie-et-attestations` → `regime-derogations-et-transition-cohorte`) : Gère dérogations, quarantaines et cohorte transitoire.
- **`REL_0513`** (`D02` → `D02`, `regle-maillon-plus-eleve` → `echelle-autonomie-l0-l4`) : Étend le périmètre de sécurité du maillon le plus élevé en amont.
- **`REL_0521`** (`D09` → `D03`, `responsabilite-mandat-contrats-b2b` → `protocole-ap2`) : Encadrement contractuel des mandats B2B.
- **`REL_0541`** (`D09` → `D10`, `services-bancaires-consommateurs-c15` → `fil-rouge-groupe-boreal-bel`) : Accréditation Banque du Canada requise pour le flux bancaire ouvert.
- **`REL_0558`** (`D09` → `D03`, `souverainete-espaces-donnees-tee-hyok` → `maillage-b2b-federe-edc-odrl`) : Conformité EU Data Act et souveraineté.
- **`REL_0583`** (`D07` → `D12`, `taxonomie-owasp-asi-mcp-maestro` → `homologation-prr-75-points`) : Couverture ASI01–ASI10 exigée au PRR.
- **`REL_0610`** (`D09` → `D09`, `vide-federal-ia-c27-c36` → `bsif-e-23`) : Report de la charge réglementaire sur les régulateurs sectoriels.

### `attenuation_risque` (82 relations)

- **`REL_0017`** (`D07` → `D07`, `alignement-deceptif-red-teaming-adversarial` → `defense-hors-modele-camel-confinement`) : Évaluation adversariale quantifiant les angles morts défensifs.
- **`REL_0019`** (`D10` → `D01`, `anti-patrons-agentiques` → `dette-cognitive-vs-technique`) : Éradique les 12 modes d'échec structurels en ARB.
- **`REL_0027`** (`D03` → `D01`, `anti-verrouillage-standards` → `dette-cognitive-vs-technique`) : Remplacement du couplage N×M propriétaire par des standards N+M.
- **`REL_0028`** (`D03` → `D03`, `anti-verrouillage-standards` → `fusion-acp-collision-terminologique`) : Fondation neutre assurant une sortie ordonnée lors d'une fusion.
- **`REL_0029`** (`D03` → `D11`, `anti-verrouillage-standards` → `pieges-gouvernance`) : Noyau possédé et réversibilité contre la rente SaaS.
- **`REL_0036`** (`D06` → `D02`, `approbation-ciba` → `supervision-hitl-hotl-abstention`) : Preuve FIDO2 contre approbation complaisante.
- **`REL_0037`** (`D11` → `D11`, `approbation-reflexe-biais-automatisation` → `pieges-gouvernance`) : Parade ergonomique et organisationnelle contre l'approbation réflexe.
- **`REL_0041`** (`D05` → `D05`, `arbre-sobriete-oo1-oo4` → `pathologies-reactives-backpressure`) : Prévient les échecs MAST et l'effet Ringelmann.
- **`REL_0061`** (`D08` → `D01`, `banc-evalops-hermetique` → `erreurs-silencieuses-cascade`) : Détection pass^k et chaos pré-production.
- **`REL_0111`** (`D08` → `D06`, `canonicalisation-jcs-rfc8785` → `signature-agent-card-ancrage`) : Canonisation RFC 8785 fiabilisant la vérification JWS.
- **`REL_0120`** (`D05` → `D01`, `choregraphie-event-mesh` → `erreurs-silencieuses-cascade`) : Retient les effets irréversibles via le tampon à fenêtre de grâce.
- **`REL_0141`** (`D07` → `D04`, `confidentialite-materielle-tee-hyok` → `six-substrats-etat-souverainete`) : Séquestre HYOK, TEE et continuité bimodèle.
- **`REL_0143`** (`D04` → `D07`, `confinement-cua-patrimoine-sans-api` → `injection-indirecte-prompt`) : Verrouille les zones d'écran et touches destructrices des CUA.
- **`REL_0145`** (`D07` → `D07`, `confinement-opensandbox-firecracker-wasi` → `injection-indirecte-prompt`) : Confinement microVM anti-exfiltration.
- **`REL_0146`** (`D07` → `D07`, `confinement-shadi-sandbox` → `chaine-approvisionnement-agent-skills`) : Isole l'exécution des scripts et composants non fiables.
- **`REL_0147`** (`D07` → `D07`, `confinement-shadi-sandbox` → `injection-indirecte-prompt`) : Confinement matériel sans réseau ni secret.
- **`REL_0149`** (`D07` → `D07`, `confinement-shadi-sandbox` → `tool-poisoning-rug-pull`) : Isole l'exécution de code arbitraire (ASI05).
- **`REL_0153`** (`D04` → `D04`, `contrats-donnees-write-audit-publish` → `dette-semantique-ontologies`) : Quarantaine WAP contre dérive silencieuse.
- **`REL_0159`** (`D04` → `D04`, `couche-anti-corruption-acl` → `dette-semantique-ontologies`) : Exactitude Decimal COMP-3 sans IEEE 754.
- **`REL_0160`** (`D04` → `D04`, `couche-anti-corruption-acl` → `encapsulation-patrimoine-it-ot`) : Protège la charge et l'intégrité des systèmes d'enregistrement.
- **`REL_0161`** (`D04` → `D01`, `couche-anti-corruption-acl` → `erreurs-silencieuses-cascade`) : Protège les SoR des rafales et doubles écritures.
- **`REL_0172`** (`D07` → `D07`, `defense-hors-modele-camel-confinement` → `injection-indirecte-prompt`) : Séparation de privilège hors modèle contre l'injection indirecte.
- **`REL_0173`** (`D06` → `D10`, `delegation-obo-deux-sauts` → `anti-patrons-agentiques`) : Parade contre l'emprunt et le délégué confus.
- **`REL_0174`** (`D06` → `D01`, `delegation-obo-deux-sauts` → `erreurs-silencieuses-cascade`) : Atténuation des privilèges à chaque saut et fraîcheur CRL/OCSP.
- **`REL_0175`** (`D06` → `D06`, `delegation-obo-deux-sauts` → `identite-non-humaine-nhi`) : Parade au délégué confus au 2e saut.
- **`REL_0177`** (`D06` → `D07`, `delegation-obo-deux-sauts` → `injection-indirecte-prompt`) : Borne le rayon d'impact par échange RFC 8693 et DPoP.
- **`REL_0185`** (`D04` → `D01`, `dette-semantique-ontologies` → `erreurs-silencieuses-cascade`) : Élimine les erreurs sémantiques silencieuses du SQL libre.
- **`REL_0199`** (`D08` → `D09`, `double-couloir-probatoire-pii` → `loi-25-article-12-1`) : Évite l'exposition de PII en télémétrie courante.
- **`REL_0231`** (`D03` → `D03`, `epinglage-schemas-mcp` → `protocole-mcp`) : Condensats SHA-256 contre le rug-pull MCP.
- **`REL_0233`** (`D03` → `D07`, `epinglage-schemas-mcp` → `tool-poisoning-rug-pull`) : Épinglage et liste d'admission contre le rug-pull MCP.
- **`REL_0234`** (`D03` → `D07`, `ergonomie-aci-anti-swagger` → `tool-poisoning-rug-pull`) : Réduit la confusion d'outils (AP-04).
- **`REL_0235`** (`D05` → `D05`, `choregraphie-event-mesh` → `pathologies-reactives-backpressure`) : Coupe les boucles d'écho et tempêtes d'événements par compteur de sauts.
- **`REL_0236`** (`D02` → `D01`, `validation-json-schema-ambigu-escalade` → `erreurs-silencieuses-cascade`) : Prévient les écarts sémantiques et structurels par schémas typés.
- **`REL_0237`** (`D05` → `D01`, `topologies-patrons-orchestration` → `erreurs-silencieuses-cascade`) : Catalogue fermé et preuve mesurée limitant les cascades d'erreurs.
- **`REL_0253`** (`D08` → `D07`, `evaluation-continue-derives` → `tool-poisoning-rug-pull`) : Détection continue en production de la dérive silencieuse d'outil.
- **`REL_0273`** (`D07` → `D10`, `soc-soar-coupe-circuit` → `federation-multi-plateformes-gravite`) : Prévient les boucles circulaires de webhooks inter-SaaS.
- **`REL_0283`** (`D08` → `D01`, `finops-focus-cpo` → `erreurs-silencieuses-cascade`) : Disjoncteur budgétaire anti-emballement.
- **`REL_0296`** (`D04` → `D07`, `gouvernance-acces-rag-ancrage` → `injection-indirecte-prompt`) : Filtrage RBAC/ABAC par fragment et attribution vérifiable.
- **`REL_0308`** (`D02` → `D01`, `harnais-deterministe-8-etapes` → `constance-pass-k`) : Élève la constance multi-essais vers pass^5 ≥ 95 %.
- **`REL_0309`** (`D02` → `D01`, `harnais-deterministe-8-etapes` → `erreurs-silencieuses-cascade`) : Intercepte les sorties plausibles mais invalides avant propagation.
- **`REL_0315`** (`D06` → `D06`, `identite-non-humaine-nhi` → `kya-verification-agent-tiers`) : Suppression des secrets statiques et traçabilité du cycle de vie NHI.
- **`REL_0319`** (`D07` → `D07`, `confinement-shadi-sandbox` → `non-compositionnalite-surete-surface-attaques`) : Confine l'exécution de code généré hors réseau et sans secret.
- **`REL_0321`** (`D07` → `D01`, `injection-indirecte-prompt` → `erreurs-silencieuses-cascade`) : Rupture de cascade ASI01 → ASI08.
- **`REL_0322`** (`D07` → `D07`, `regle-de-deux-opa` → `non-compositionnalite-surete-surface-attaques`) : Rompt la triade létale dans les sessions composées multi-outils.
- **`REL_0367`** (`D04` → `D09`, `memoire-coala-4-tiroirs` → `efvp-transfert-hors-quebec`) : Isolation et oubli bi-temporel sous Loi 25.
- **`REL_0369`** (`D04` → `D07`, `memoire-coala-4-tiroirs` → `injection-indirecte-prompt`) : Contrôle et étiquette les écritures en mémoire.
- **`REL_0372`** (`D04` → `D07`, `memoire-partagee-concurrence-effacement` → `injection-indirecte-prompt`) : Bloque l'empoisonnement persistant de mémoire (OWASP ASI06).
- **`REL_0378`** (`D05` → `D09`, `negociation-b2b-diplomate-evaluateur` → `responsabilite-mandat-contrats-b2b`) : Protection secrets et erreur en B2B.
- **`REL_0397`** (`D05` → `D02`, `paradigme-apm-autonomie-encadree` → `supervision-hitl-hotl-abstention`) : Compensation par frames locaux lorsque l'humain sature.
- **`REL_0400`** (`D02` → `D01`, `partition-hybride-80-20` → `loi-de-lusser`) : Encapsule le non-déterminisme contre la chute exponentielle.
- **`REL_0415`** (`D03` → `D07`, `passerelle-mcp-ai-gateway` → `tool-poisoning-rug-pull`) : Passerelle MCP centralisant admission et politiques.
- **`REL_0428`** (`D07` → `D07`, `politiques-opa-rego-hors-modele` → `injection-indirecte-prompt`) : Blocage déterministe hors modèle des actions détournées.
- **`REL_0431`** (`D05` → `D01`, `pont-ia-physique-ros2-simplex` → `erreurs-silencieuses-cascade`) : Enveloppe physique Simplex IEC 61508.
- **`REL_0436`** (`D06` → `D06`, `post-quantique-ml-dsa-slh-dsa` → `delegation-obo-deux-sauts`) : Transaction Tokens contre HTTP 431 PQ.
- **`REL_0440`** (`D06` → `D08`, `post-quantique-ml-dsa-slh-dsa` → `scellage-jcs-scitt`) : Protection SCITT + SLH-DSA contre la ruine probatoire.
- **`REL_0454`** (`D04` → `D07`, `propagation-acl-memoire-silo` → `tool-poisoning-rug-pull`) : Bloque les fuites vectorielles et ASI06.
- **`REL_0487`** (`D08` → `D07`, `provenance-artefacts-aibom-5-horloges` → `tool-poisoning-rug-pull`) : Détection des dérives d'outils par attestation et AIBOM.
- **`REL_0490`** (`D04` → `D01`, `rag-agentique-contexte` → `dette-cognitive-vs-technique`) : Réduction des fuites inter-domaines par filtrage ACL préalable.
- **`REL_0494`** (`D04` → `D08`, `rag-agentique-contexte` → `finops-focus-cpo`) : Réduit l'explosion des jetons par stratification et cache KV.
- **`REL_0503`** (`D07` → `D04`, `red-teaming-continu-empoisonnement-memoire` → `memoire-bi-temporelle-et-purge`) : Suivi de teinte HMAC anti-ASI06.
- **`REL_0510`** (`D07` → `D07`, `regle-de-deux-opa` → `injection-indirecte-prompt`) : Règle de non-cumul brisant la triade létale en session.
- **`REL_0526`** (`D05` → `D01`, `saga-compensatoire` → `erreurs-silencieuses-cascade`) : Répare les échecs partiels sans verrou 2PC.
- **`REL_0528`** (`D05` → `D05`, `saga-compensatoire` → `modes-echecs-emergents-frontiere`) : Idempotence et compensations bornant les effets partiels.
- **`REL_0533`** (`D06` → `D06`, `saturation-http-431-ml-dsa-kid` → `post-quantique-ml-dsa-slh-dsa`) : Résout la saturation d'en-tête HTTP 431 induite par ML-DSA.
- **`REL_0537`** (`D05` → `D10`, `semantique-effet-idempotence-uetr` → `production-agentique-canadienne-2025-2026`) : Prévention des doubles exécutions financières et traçabilité comptable.
- **`REL_0540`** (`D02` → `D01`, `separation-controleur-executeur-determinisme` → `constance-pass-k`) : Réduction du non-déterminisme par flux déterministe.
- **`REL_0545`** (`D07` → `D01`, `soc-soar-coupe-circuit` → `erreurs-silencieuses-cascade`) : Endiguement rapide par coupe-circuit et révocation en cascade.
- **`REL_0547`** (`D07` → `D08`, `soc-soar-coupe-circuit` → `finops-focus-cpo`) : Stoppe les boucles autonomes coûteuses avant dérive budgétaire.
- **`REL_0550`** (`D07` → `D05`, `soc-soar-coupe-circuit` → `modes-echecs-emergents-frontiere`) : Disjoncteurs et boucle SOC interrompant les cascades.
- **`REL_0551`** (`D07` → `D05`, `soc-soar-coupe-circuit` → `pathologies-reactives-backpressure`) : Stoppe les boucles d'emballement et dérives.
- **`REL_0553`** (`D07` → `D05`, `soc-soar-coupe-circuit` → `topologies-patrons-orchestration`) : Arrêt < 10 s et repli < 60 s sur dérive.
- **`REL_0555`** (`D06` → `D07`, `socle-iam-federe-oauth-fapi` → `taxonomie-attaques-identite-mandataire-confus`) : Liaison mTLS/DPoP et FAPI 2.0 contre le rejeu de jeton.
- **`REL_0556`** (`D09` → `D09`, `souverainete-espaces-donnees-tee-hyok` → `efvp-transfert-hors-quebec`) : HYOK et TEE face au CLOUD Act.
- **`REL_0561`** (`D06` → `D06`, `spiffe-spire-attestation` → `identite-non-humaine-nhi`) : Suppression des secrets statiques.
- **`REL_0563`** (`D06` → `D07`, `spiffe-spire-attestation` → `taxonomie-attaques-identite-mandataire-confus`) : Attestation éphémère SPIFFE contre les secrets statiques.
- **`REL_0564`** (`D07` → `D07`, `sre-autonome-rayon-impact-cedar` → `tool-poisoning-rug-pull`) : Catalogue typé contre injection par journaux.
- **`REL_0565`** (`D02` → `D06`, `supervision-hitl-hotl-abstention` → `approbation-ciba`) : Neutralise la fatigue d'approbation de 93 % sur les points critiques.
- **`REL_0567`** (`D02` → `D11`, `supervision-hitl-hotl-abstention` → `atrophie-competences-humaines`) : Vue différentielle et quotas contre le clic réflexe.
- **`REL_0574`** (`D02` → `D01`, `supervision-hitl-hotl-abstention` → `rupture-modele-conversationnel-agent-boucle`) : Libération humaine H-31 sur les actions irréversibles.
- **`REL_0585`** (`D03` → `D07`, `epinglage-schemas-mcp` → `chaine-approvisionnement-agent-skills`) : Bloque les substitutions silencieuses de manifestes et définitions par empreinte SHA-256.
- **`REL_0587`** (`D05` → `D10`, `topologies-patrons-orchestration` → `anti-patrons-agentiques`) : Proscrit le maillage libre et les écritures concurrentes.
- **`REL_0608`** (`D02` → `D01`, `usine-logicielle-agentic-sdlc` → `dette-cognitive-vs-technique`) : Résorption patrimoniale RPG/COBOL sous oracle.

### `tension_arbitrage` (67 relations)

- **`REL_0014`** (`D03` → `D03`, `agntcy-slim` → `protocole-a2a`) : Positionnement officiel d'AGNTCY nuancé par chevauchement tiers sur ACP.
- **`REL_0018`** (`D06` → `D03`, `annuaires-commerciaux-risque-standard-de-fait` → `anti-verrouillage-standards`) : Adoption immédiate d'annuaires propriétaires par rapport à l'attente de normes neutres.
- **`REL_0020`** (`D10` → `D03`, `anti-patrons-agentiques` → `facades-mcp-intention-metier`) : Oppose le mappage rapide OpenAPI 1:1 à la conception par intention.
- **`REL_0022`** (`D10` → `D01`, `anti-patrons-agentiques` → `taxonomie-acteurs-agentiques`) : Proscrit le super-agent universel face aux 5 archétypes spécialisés.
- **`REL_0023`** (`D10` → `D05`, `anti-patrons-agentiques` → `topologies-patrons-orchestration`) : Condamne la « salle virtuelle » libre au profit de graphes bornés.
- **`REL_0042`** (`D05` → `D03`, `arbre-sobriete-oo1-oo4` → `protocole-a2a`) : Sobriété agent unique face au surcoût multi-agents (-70 % à +80,8 %).
- **`REL_0049`** (`D11` → `D01`, `atrophie-competences-humaines` → `economie-industrialisation-cognitive`) : Paradoxe productivité immédiate et érosion de la relève.
- **`REL_0051`** (`D11` → `D11`, `atrophie-competences-humaines` → `trajectoires-adaptatives-dapp`) : Gain d'automatisation et maintien du vivier humain.
- **`REL_0063`** (`D08` → `D08`, `banc-evalops-hermetique` → `finops-focus-cpo`) : Coût de simulation face au risque d'erreur en production.
- **`REL_0109`** (`D12` → `D11`, `calibration-feds-ema` → `trajectoires-adaptatives-dapp`) : Optimisation du TCO (Scénario A) face à la robustesse minimax (Scénario B).
- **`REL_0117`** (`D06` → `D06`, `certificats-tls-47-jours` → `post-quantique-ml-dsa-slh-dsa`) : Collision rotation TLS 47 jours et taille PQC sur passerelles.
- **`REL_0124`** (`D05` → `D05`, `choregraphie-event-mesh` → `topologies-patrons-orchestration`) : Arbitre l'autonomie événementielle face à la maîtrise transactionnelle.
- **`REL_0142`** (`D04` → `D04`, `confinement-cua-patrimoine-sans-api` → `couche-anti-corruption-acl`) : Tolère CUA à ≤ 8 % sous bail 12 mois contre refactoring MCP durable.
- **`REL_0144`** (`D07` → `D03`, `confinement-opensandbox-firecracker-wasi` → `anti-verrouillage-standards`) : Isolation stricte face à la latence et à la complexité KVM.
- **`REL_0150`** (`D01` → `D08`, `constance-pass-k` → `finops-focus-cpo`) : Arbitre le coût de vérification face à la fiabilité requise.
- **`REL_0152`** (`D03` → `D03`, `contrats-api-versionnement-conformite` → `anti-verrouillage-standards`) : Paradoxe du verrouillage inverse sur l'interface de fait OpenAI.
- **`REL_0183`** (`D04` → `D04`, `dette-semantique-ontologies` → `ecart-accord-protocolaire-comprehension`) : Expressivité ontologique coûteuse face à la souplesse fragile en prose.
- **`REL_0201`** (`D08` → `D08`, `double-couloir-probatoire-pii` → `observabilite-otel-genai`) : Diagnostic complet face à la minimisation Loi 25 et RGPD.
- **`REL_0206`** (`D04` → `D07`, `ecart-accord-protocolaire-comprehension` → `tool-poisoning-rug-pull`) : Validité syntaxique des schémas face au risque de description trompeuse.
- **`REL_0215`** (`D02` → `D02`, `echelle-autonomie-l0-l4` → `supervision-hitl-hotl-abstention`) : Montée en autonomie bornée contre capacité cognitive de supervision humaine.
- **`REL_0218`** (`D01` → `D03`, `economie-industrialisation-cognitive` → `anti-verrouillage-standards`) : Arbitre vitesse des agents SaaS et contrôle architectural.
- **`REL_0219`** (`D01` → `D01`, `economie-jetons-routage-slm` → `raisonnement-inference-limites-planification`) : Arbitrage coût des jetons de réflexion face au gain de qualité à l'inférence.
- **`REL_0226`** (`D09` → `D01`, `efvp-transfert-hors-quebec` → `systems-of-agency`) : Souveraineté des données financières face à l'accès aux modèles de pointe.
- **`REL_0259`** (`D05` → `D05`, `execution-durable-temporal` → `semantique-effet-idempotence-uetr`) : Illusion du rollback logiciel face à l'irréversibilité métier.
- **`REL_0268`** (`D10` → `D01`, `fabrique-agents-certification-reemission` → `erreurs-silencieuses-cascade`) : Centralisation productive face au risque de point de défaillance unique.
- **`REL_0282`** (`D08` → `D01`, `finops-focus-cpo` → `dette-cognitive-vs-technique`) : Baisse du prix du jeton face à l'explosion du CPO par relecture.
- **`REL_0288`** (`D05` → `D03`, `frameworks-orchestration-entreprise` → `anti-verrouillage-standards`) : Frontière commerciale des plateformes managées face à la portabilité ouverte.
- **`REL_0311`** (`D01` → `D03`, `hierarchie-preuves-etudes-cas` → `protocole-a2a`) : Spécifications stables face à la rareté des preuves en production.
- **`REL_0320`** (`D07` → `D01`, `injection-indirecte-prompt` → `constance-pass-k`) : Coût d'utilité de la sécurité CaMeL (77 % contre 84 %).
- **`REL_0323`** (`D06` → `D06`, `inventaire-revocation-asymetrie` → `spiffe-spire-attestation`) : Durée de vie courte (24 h) comme substitut partiel à la révocation.
- **`REL_0358`** (`D07` → `D08`, `maillage-agents-pep-pdp-zero-trust` → `finops-focus-cpo`) : Surcoût de latence, complexité et inférence des contrôles par arête.
- **`REL_0366`** (`D04` → `D06`, `memoire-coala-4-tiroirs` → `did-vc-passeport-agent`) : Apprentissage continu en production face à la validité datée du passeport.
- **`REL_0374`** (`D08` → `D01`, `modele-comme-juge-biais-calibration` → `raisonnement-inference-limites-planification`) : Traces de raisonnement plausibles face à la fiabilité des juges automatisés.
- **`REL_0379`** (`D07` → `D07`, `non-compositionnalite-surete-surface-attaques` → `injection-indirecte-prompt`) : Modularité multi-serveurs face à la reconstitution émergente de la triade létale.
- **`REL_0380`** (`D07` → `D05`, `non-compositionnalite-surete-surface-attaques` → `modes-echecs-emergents-frontiere`) : Souplesse du langage naturel face au cumul silencieux d'erreurs.
- **`REL_0398`** (`D02` → `D01`, `partition-hybride-80-20` → `constance-pass-k`) : Compromis coût en jetons / précision / latence (courbe HAL).
- **`REL_0404`** (`D03` → `D03`, `passerelle-mcp-ai-gateway` → `anti-verrouillage-standards`) : Portabilité par passerelle de médiation contre plus petit dénominateur commun.
- **`REL_0420`** (`D11` → `D11`, `pieges-gouvernance` → `gouvernance-duale-ae-as`) : Sur-ingénierie de 2e ligne et prolifération du Shadow AI.
- **`REL_0421`** (`D11` → `D02`, `pieges-gouvernance` → `partition-hybride-80-20`) : Rigueur du contrôle face à la sur-ingénierie et aux agents fantômes.
- **`REL_0423`** (`D10` → `D01`, `plateforme-iap-gitops-cognitif` → `dette-cognitive-vs-technique`) : Immuabilité Git face à l'édition dynamique des prompts.
- **`REL_0426`** (`D10` → `D02`, `plateformes-saas-et-asymetrie-tiers` → `noyau-controle-possede-cap`) : Fermeture du plan de contrôle SaaS contre gouvernance souveraine.
- **`REL_0438`** (`D06` → `D06`, `post-quantique-ml-dsa-slh-dsa` → `delegation-obo-deux-sauts`) : Poids des signatures ML-DSA face à la limite des en-têtes HTTP 431.
- **`REL_0439`** (`D06` → `D03`, `post-quantique-ml-dsa-slh-dsa` → `passerelle-mcp-ai-gateway`) : Taille des signatures post-quantiques face aux contraintes réseau.
- **`REL_0459`** (`D03` → `D08`, `protocole-a2a` → `journalisation-probatoire-audit`) : Découverte ouverte fédérée face à la gouvernance des clés et à l'imputation.
- **`REL_0460`** (`D03` → `D05`, `protocole-a2a` → `topologies-patrons-orchestration`) : Opacité voulue d'A2A contre exigence d'auditabilité réglementaire.
- **`REL_0476`** (`D03` → `D03`, `protocole-mcp` → `protocole-a2a`) : Frontière floue entre tâches asynchrones MCP et délégation A2A.
- **`REL_0480`** (`D12` → `D12`, `protocole-wyvern-g0-g5` → `clause-non-avis-licences`) : Exhaustivité automatisée et absence de relecture humaine.
- **`REL_0495`** (`D04` → `D07`, `rag-agentique-contexte` → `injection-indirecte-prompt`) : Agrandir la fenêtre dilue l'attention et élargit la surface ASI01.
- **`REL_0498`** (`D03` → `D07`, `rails-paiement-commerce-agentique` → `injection-indirecte-prompt`) : Automatisation des mandats de paiement face au détournement par injection indirecte.
- **`REL_0511`** (`D07` → `D02`, `regle-de-deux-opa` → `supervision-hitl-hotl-abstention`) : Accroît le volume d'approbations après contamination.
- **`REL_0515`** (`D02` → `D10`, `regle-maillon-plus-eleve` → `profil-groupe-diversifie-m18`) : Mutualisation du socle technique face au cloisonnement des filiales.
- **`REL_0523`** (`D03` → `D01`, `routage-cognitif-hybride-3-paliers` → `constance-pass-k`) : Économie SLM face au risque de baisse de précision et de constance.
- **`REL_0530`** (`D05` → `D07`, `saga-compensatoire` → `soc-soar-coupe-circuit`) : Arrêt d'urgence et intégrité comptable des sagas en vol.
- **`REL_0531`** (`D05` → `D10`, `saga-compensatoire` → `tampon-deterministe-rtr-iso20022`) : Interdit la compensation a posteriori sur virements RTR irrévocables.
- **`REL_0557`** (`D09` → `D08`, `souverainete-espaces-donnees-tee-hyok` → `finops-focus-cpo`) : Souveraineté, HYOK et TEE face au coût et à la disponibilité.
- **`REL_0560`** (`D06` → `D06`, `spiffe-spire-attestation` → `did-vc-passeport-agent`) : Infrastructure centralisée intra-domaine (SPIFFE) face à la portabilité écosystémique (DID).
- **`REL_0568`** (`D02` → `D11`, `supervision-hitl-hotl-abstention` → `atrophie-competences-humaines`) : Automatisation de routine et maintien du discernement et de la relève junior.
- **`REL_0569`** (`D02` → `D02`, `supervision-hitl-hotl-abstention` → `criteres-qos-cout-precision-latence`) : Oppose latence opérationnelle et exigence d'approbation humaine.
- **`REL_0570`** (`D02` → `D02`, `supervision-hitl-hotl-abstention` → `echelle-autonomie-l0-l4`) : Vitesse d'autonomie et fatigue d'approbation.
- **`REL_0571`** (`D02` → `D01`, `supervision-hitl-hotl-abstention` → `erreurs-silencieuses-cascade`) : Charge d'approbation humaine face au biais de complaisance.
- **`REL_0572`** (`D02` → `D09`, `supervision-hitl-hotl-abstention` → `loi-25-article-12-1`) : Évite l'approbation nominale qui rend la décision automatisée.
- **`REL_0573`** (`D02` → `D03`, `supervision-hitl-hotl-abstention` → `matrice-protocoles-exigences-reglementaires`) : Paradoxe de l'inversement sur l'intervention humaine.
- **`REL_0575`** (`D01` → `D02`, `surcout-multi-agent-debat-mast` → `separation-controleur-executeur-determinisme`) : Contexte isolé multi-agents (15×) face au rédacteur unique continu.
- **`REL_0578`** (`D01` → `D03`, `systems-of-agency` → `anti-verrouillage-standards`) : Déplace le verrouillage vers les plateformes.
- **`REL_0589`** (`D05` → `D08`, `topologies-patrons-orchestration` → `finops-focus-cpo`) : Arbitre gain F1 réflexif/multi-agents contre explosion de coût 4x–15x.
- **`REL_0613`** (`D08` → `D04`, `volant-distillation-dspy-multilora` → `memoire-bi-temporelle-et-purge`) : Apprentissage sur traces face au risque de fuite et de biais.
- **`REL_0615`** (`D03` → `D03`, `web-agentique-webmcp-webbotauth` → `protocole-ap2`) : Oppose l'authentification par origine HTTP à la preuve d'intention signée.

### `amplification_synergie` (59 relations)

- **`REL_0005`** (`D03` → `D03`, `agent-card-decouverte` → `agntcy-slim`) : Unit découverte signée et routage chiffré fédéré.
- **`REL_0013`** (`D03` → `D03`, `agntcy-slim` → `protocole-a2a`) : Fédération annuaire et canal MLS pour A2A.
- **`REL_0021`** (`D10` → `D02`, `anti-patrons-agentiques` → `partition-hybride-80-20`) : Proscription des impasses consolidant le noyau possédé.
- **`REL_0033`** (`D06` → `D05`, `approbation-ciba` → `saga-compensatoire`) : Pré-approbation Saga et revalidation TOCTOU au réveil.
- **`REL_0034`** (`D06` → `D08`, `approbation-ciba` → `scellage-jcs-scitt`) : Ancre l'empreinte d'approbation `h` dans le journal d'audit.
- **`REL_0038`** (`D05` → `D08`, `arbre-sobriete-oo1-oo4` → `finops-focus-cpo`) : Réduction massive du coût par résultat via la sobriété d'orchestration.
- **`REL_0050`** (`D11` → `D11`, `atrophie-competences-humaines` → `modele-operationnel-hub-and-spoke`) : Reconversion interne vers la supervision HOTL.
- **`REL_0052`** (`D12` → `D12`, `audit-validation-sources-121-449` → `clause-non-avis-licences`) : Fonde la crédibilité du cadre par le tri A/B/C et les avertissements.
- **`REL_0064`** (`D08` → `D11`, `banc-evalops-hermetique` → `gouvernance-duale-ae-as`) : Séparation Oracle / Bâtisseur renforçant E1–E3 et E-23.
- **`REL_0071`** (`D10` → `D10`, `blueprints-reference-multisectoriels` → `fabrique-agents-certification-reemission`) : Convergence entre le socle outillé C1–C8 et la fabrique de réémission.
- **`REL_0103`** (`D02` → `D11`, `cadre-togaf-archimate-4-plans` → `gouvernance-raci-modele-en-etoile`) : Mutualise les 3 plans transversaux en étoile.
- **`REL_0107`** (`D12` → `D08`, `calibration-feds-ema` → `banc-evalops-hermetique`) : Étalonnage quantitatif des seuils pass^k et coupe-circuit.
- **`REL_0115`** (`D06` → `D06`, `certificats-tls-47-jours` → `post-quantique-ml-dsa-slh-dsa`) : Prépare la bascule algorithmique par automatisation PKI.
- **`REL_0119`** (`D07` → `D04`, `chaine-approvisionnement-agent-skills` → `rag-agentique-contexte`) : Apporte la divulgation progressive SKILL.md sous contrôle SHA-256.
- **`REL_0134`** (`D08` → `D08`, `comptabilite-carbone-cap-046-bsif-b15` → `finops-focus-cpo`) : Étend le pilotage FinOps CPO à l'empreinte énergétique et climatique.
- **`REL_0137`** (`D12` → `D12`, `concordance-inter-tomes-div02` → `exigences-cre-ia-305`) : Base de preuves unique contre les silos réglementaires.
- **`REL_0154`** (`D04` → `D07`, `contrats-donnees-write-audit-publish` → `sre-autonome-rayon-impact-cedar`) : Stabilité DataOps + SRE borné sur plateforme 24/7.
- **`REL_0167`** (`D01` → `D01`, `couts-transaction-coase` → `systems-of-agency`) : Accélère la recomposition des processus inter-entreprises.
- **`REL_0186`** (`D04` → `D04`, `dette-semantique-ontologies` → `rag-agentique-contexte`) : Cache KV accru par préfixes ontologiques stables.
- **`REL_0205`** (`D09` → `D09`, `droit-effacement-portabilite-loi-25` → `loi-25-article-12-1`) : Complète l'art. 12.1 Loi 25 sur la gouvernance mémorielle.
- **`REL_0213`** (`D02` → `D10`, `echelle-autonomie-l0-l4` → `fil-rouge-groupe-boreal-bel`) : Déploiement progressif sécurisé par paliers L0–L3.
- **`REL_0255`** (`D05` → `D05`, `execution-durable-temporal` → `choregraphie-event-mesh`) : Unit sagas multi-jours déterministes et bus événementiel découplé.
- **`REL_0260`** (`D05` → `D02`, `execution-durable-temporal` → `supervision-hitl-hotl-abstention`) : Pérennise les attentes humaines longues sans coût actif.
- **`REL_0271`** (`D10` → `D02`, `federation-multi-plateformes-gravite` → `clauses-sortie-portabilite-interchangeabilite`) : Allie fédération par gravité technique et réversibilité contractuelle.
- **`REL_0278`** (`D05` → `D11`, `fiabilite-coordination-taxonomie-mast` → `gouvernance-duale-ae-as`) : Relie les 14 modes d'échec MAST à l'imputabilité organisationnelle.
- **`REL_0285`** (`D08` → `D08`, `finops-focus-cpo` → `observabilite-otel-genai`) : Imputation conjointe des coûts et du carbone via OTel et FOCUS v1.4.
- **`REL_0324`** (`D04` → `D04`, `iso-20022-lynx-rtr` → `dette-semantique-ontologies`) : Réduction de la dette sémantique par messagerie financière normalisée.
- **`REL_0336`** (`D08` → `D05`, `journalisation-probatoire-audit` → `semantique-effet-idempotence-uetr`) : Bouclage complet de la preuve entre intention d'appel et effet financier.
- **`REL_0349`** (`D09` → `D09`, `loi-25-article-12-1` → `avis-acvm-11-348`) : Cumule explicabilité client, dossier 7 ans et personne inscrite.
- **`REL_0357`** (`D03` → `D03`, `maillage-agentique-trois-acceptions` → `passerelle-mcp-ai-gateway`) : Combine plan de données passerelle, dorsale événementielle et identité.
- **`REL_0365`** (`D04` → `D04`, `memoire-coala-4-tiroirs` → `dette-semantique-ontologies`) : Croise faits bi-temporels Graphiti et vocabulaire causal Apache Ossie.
- **`REL_0382`** (`D02` → `D03`, `noyau-controle-possede-cap` → `anti-verrouillage-standards`) : Permet de remplacer un modèle en quelques jours.
- **`REL_0385`** (`D08` → `D08`, `observabilite-otel-genai` → `banc-evalops-hermetique`) : Alimente les golden datasets par les traces de production.
- **`REL_0391`** (`D08` → `D08`, `observabilite-otel-genai` → `evaluation-continue-derives`) : Télémétrie structurée alimentant l'évaluation continue et la détection de dérive.
- **`REL_0399`** (`D02` → `D08`, `partition-hybride-80-20` → `finops-focus-cpo`) : Comprime le coût par résultat conforme (CPO).
- **`REL_0407`** (`D03` → `D08`, `passerelle-mcp-ai-gateway` → `finops-focus-cpo`) : Gouvernance centralisée et baisse > 55 % du CPO.
- **`REL_0408`** (`D03` → `D08`, `passerelle-mcp-ai-gateway` → `observabilite-otel-genai`) : Centralise la télémétrie OTel et le double couloir au chemin obligé.
- **`REL_0409`** (`D03` → `D07`, `passerelle-mcp-ai-gateway` → `politiques-opa-rego-hors-modele`) : Centralisation de l'application des politiques au point de passage N+M.
- **`REL_0414`** (`D03` → `D08`, `passerelle-mcp-ai-gateway` → `scellage-jcs-scitt`) : Émission synchrone du pré-audit JCS à la coupure PEP.
- **`REL_0422`** (`D08` → `D08`, `plan-inference-routage-carbone` → `finops-focus-cpo`) : Double dividende économique et carbone du routage frugal.
- **`REL_0467`** (`D03` → `D03`, `protocole-ap2` → `protocoles-interfaces-agui-a2ui-webrtc`) : Relie l'approbation opérateur AG-UI/A2UI au mandat signé AP2/x402.
- **`REL_0470`** (`D03` → `D04`, `protocole-mcp` → `couche-anti-corruption-acl`) : Outils d'intention MCP encapsulant le patrimoine exact.
- **`REL_0475`** (`D03` → `D03`, `protocole-mcp` → `protocole-a2a`) : Composition simultanée des axes vertical et horizontal en production.
- **`REL_0488`** (`D01` → `D01`, `quadruple-dette-agentique` → `dette-cognitive-vs-technique`) : Engrenage composé de la dette cognitive et technique.
- **`REL_0493`** (`D04` → `D08`, `rag-agentique-contexte` → `finops-focus-cpo`) : Préfixe KV-cache fixe réduisant le coût de relecture.
- **`REL_0496`** (`D04` → `D04`, `rag-agentique-contexte` → `memoire-coala-4-tiroirs`) : Mutualisation de la pile hybride entre mémoire long terme et RAG.
- **`REL_0517`** (`D10` → `D08`, `reprise-sinistre-cognitif-continuite` → `volant-distillation-dspy-multilora`) : Mutualisation GPU entre SLM quotidiens et DR.
- **`REL_0518`** (`D06` → `D06`, `requetes-riches-rar-txn-tokens` → `delegation-obo-deux-sauts`) : Précision de portée RAR et compacité O(1) des jetons OBO.
- **`REL_0520`** (`D05` → `D08`, `resilience-orchestration-repli-plafonds` → `finops-focus-cpo`) : Unifie les 5 plafonds d'exécution avec l'enveloppe budgétaire.
- **`REL_0529`** (`D05` → `D05`, `saga-compensatoire` → `resilience-orchestration-repli-plafonds`) : Préserve le canal de compensation sous coupe-circuit.
- **`REL_0539`** (`D07` → `D07`, `separation-controle-donnees-camel` → `regle-de-deux-opa`) : Complète la Règle de deux par suivi de teinte structurel CaMeL.
- **`REL_0544`** (`D07` → `D08`, `soc-soar-coupe-circuit` → `banc-evalops-hermetique`) : Intègre la suite d'attaques adverses dans l'étage E2.
- **`REL_0548`** (`D07` → `D06`, `soc-soar-coupe-circuit` → `identite-non-humaine-nhi`) : Symétrie attaque/défense imposant le passeport aux agents du SOC.
- **`REL_0559`** (`D06` → `D06`, `spiffe-spire-attestation` → `delegation-obo-deux-sauts`) : Combinaison d'identité machine SVID et de chaîne de mandat humaine.
- **`REL_0562`** (`D06` → `D07`, `spiffe-spire-attestation` → `soc-soar-coupe-circuit`) : Révocation instantanée liée à l'identité SPIFFE.
- **`REL_0580`** (`D01` → `D05`, `systems-of-agency` → `execution-durable-temporal`) : Fiabilité bout en bout des systèmes d'action.
- **`REL_0586`** (`D07` → `D07`, `tool-poisoning-rug-pull` → `injection-indirecte-prompt`) : Convergence des descriptions d'outils empoisonnées et de l'injection.
- **`REL_0607`** (`D02` → `D04`, `usine-logicielle-agentic-sdlc` → `couche-anti-corruption-acl`) : Extinction des CUA par modernisation MCP.
- **`REL_0614`** (`D08` → `D03`, `volant-distillation-dspy-multilora` → `routage-cognitif-hybride-3-paliers`) : Distillation alimentant le palier 1 SLM.

### `projection_temporelle` (52 relations)

- **`REL_0030`** (`D03` → `D11`, `anti-verrouillage-standards` → `tri-prospectif-peremption-feuilles-route`) : Obsolescence en quatre mois de la feuille de route d'Ehtesham et coll.
- **`REL_0058`** (`D09` → `D11`, `avis-acvm-11-348` → `trajectoires-adaptatives-dapp`) : Jalons valeurs mobilières 2026 → 2028 → veille SIG-105.
- **`REL_0078`** (`D09` → `D06`, `bsif-e-23` → `did-vc-passeport-agent`) : Échéance PROGRAMMÉE du 1ᵉʳ mai 2027 devançant la normalisation du passeport.
- **`REL_0085`** (`D09` → `D11`, `bsif-e-23` → `priorites-90-jours-gouvernance`) : Dicte le verrouillage du socle avant le 1ᵉʳ mai 2027.
- **`REL_0093`** (`D09` → `D11`, `bsif-e-23` → `trajectoire-90j-18m-p1-p3`) : Cadencement par les jalons fermes 2027, 2028, 2029 et 2033.
- **`REL_0094`** (`D09` → `D11`, `bsif-e-23` → `trajectoires-adaptatives-dapp`) : Jalon prudentiel canadien du 1ᵉʳ mai 2027.
- **`REL_0098`** (`D03` → `D11`, `cadre-eif-4-couches` → `horizon-2027-2032-tri-prospectif`) : Transition de la standardisation syntaxique vers le verrou sémantique-pragmatique.
- **`REL_0118`** (`D06` → `D11`, `certificats-tls-47-jours` → `trajectoires-adaptatives-dapp`) : Projette les jalons TLS 100 j (2027) et 47 jours (2029).
- **`REL_0151`** (`D01` → `D11`, `constance-pass-k` → `horizon-2027-2032-tri-prospectif`) : Doublement de l'horizon de tâche déléguée et impact organisationnel.
- **`REL_0179`** (`D06` → `D12`, `delegation-obo-deux-sauts` → `referentiel-annexes-protocoles-chronologie`) : Normalisation IETF attendue fin 2026–2028.
- **`REL_0191`** (`D06` → `D11`, `did-vc-passeport-agent` → `trajectoire-consolidation-standards-2027-2028`) : Place la fédération DID/VC inter-organisations en horizon 2027–2030.
- **`REL_0229`** (`D04` → `D11`, `encapsulation-patrimoine-it-ot` → `trajectoire-90j-18m-p1-p3`) : Extinction complète des CUA de P1 (INI-015) à P2 (POR-008).
- **`REL_0238`** (`D01` → `D11`, `etat-des-lieux-adoption-map-2027` → `trajectoire-consolidation-standards-2027-2028`) : Projette l'écart pilote-production vers trois horloges et H1–H6.
- **`REL_0245`** (`D09` → `D11`, `eu-ai-act` → `modele-maturite-5-niveaux-dimensions`) : Cale la conformité SMQ EN 18286 sur J2a et J3.
- **`REL_0251`** (`D09` → `D11`, `eu-ai-act` → `trajectoires-adaptatives-dapp`) : Échéancier impératif 2026–2031 (Omnibus).
- **`REL_0274`** (`D11` → `D09`, `feuille-de-route-phases-90-jours-indicateurs` → `bsif-e-23`) : Impose l'inventaire E-23 au 1ᵉʳ mai 2027 sans glissement.
- **`REL_0275`** (`D11` → `D03`, `feuille-de-route-phases-90-jours-indicateurs` → `protocole-mcp`) : Fixe l'échéance de migration MCP au 28 juillet 2027.
- **`REL_0276`** (`D09` → `D09`, `feuille-route-1er-mai-2027` → `bsif-e-23`) : Préparation sur 278 jours vers l'entrée en vigueur du 1ᵉʳ mai 2027.
- **`REL_0277`** (`D09` → `D11`, `feuille-route-1er-mai-2027` → `horizon-2027-2032-tri-prospectif`) : Extension du jalon 2027 vers la grappe réglementaire 2027–2032.
- **`REL_0289`** (`D11` → `D02`, `frontiere-capacites-metr-veille` → `echelle-autonomie-l0-l4`) : Révision de l'autonomie face à la saturation METR.
- **`REL_0290`** (`D11` → `D03`, `frontiere-capacites-metr-veille` → `maillage-b2b-federe-edc-odrl`) : Vers les marchés B2B autonomes liquides 2028–2029.
- **`REL_0291`** (`D11` → `D05`, `frontiere-capacites-metr-veille` → `pont-ia-physique-ros2-simplex`) : Convergence Physical AI / VLA 2028–2030.
- **`REL_0294`** (`D01` → `D01`, `genealogie-eai-soa-fipa-llm` → `systems-of-agency`) : Retrace l'évolution 2000–2027 vers les Systèmes d'agentivité à trois générations.
- **`REL_0325`** (`D04` → `D03`, `iso-20022-lynx-rtr` → `protocole-ap2`) : Convergence conditionnelle paiements temps réel RTR et commerce AP2.
- **`REL_0375`** (`D11` → `D11`, `modele-maturite-5-niveaux-dimensions` → `feuille-de-route-phases-90-jours-indicateurs`) : Conditionne l'ouverture des phases et niveaux d'autonomie.
- **`REL_0392`** (`D08` → `D12`, `observabilite-otel-genai` → `exigences-cre-ia-305`) : Suit la maturation OTel Development vers la preuve d'audit 2027.
- **`REL_0416`** (`D12` → `D09`, `peremption-revalidation-annexe-n` → `eu-ai-act`) : Échelonnement temporel article 50 (août 2026) et Annexe III (décembre 2027 / août 2028).
- **`REL_0418`** (`D12` → `D06`, `peremption-revalidation-annexe-n` → `post-quantique-ml-dsa-slh-dsa`) : Bascule de PROJETÉ à PROGRAMMÉ sur l'horizon 2030–2035 (NIST IR 8547).
- **`REL_0419`** (`D12` → `D03`, `peremption-revalidation-annexe-n` → `protocole-mcp`) : Jalons de révision protocolaire SEP-3398 (mars 2027).
- **`REL_0434`** (`D06` → `D09`, `post-quantique-ml-dsa-slh-dsa` → `bsif-e-23`) : Anticipe l'agilité cryptographique des canaux B2B et industriels 2026–2030.
- **`REL_0435`** (`D06` → `D06`, `post-quantique-ml-dsa-slh-dsa` → `crypto-agilite-migration-pqc`) : Fenêtre d'action 2026–2029 déduite à rebours des échéances 2030/2035.
- **`REL_0443`** (`D06` → `D11`, `post-quantique-ml-dsa-slh-dsa` → `trajectoires-adaptatives-dapp`) : Horizon post-quantique 2030–2035 sur les NHI.
- **`REL_0444`** (`D11` → `D10`, `priorites-90-jours-gouvernance` → `modele-maturite-feuille-360j`) : Amorce la rampe M1 → M3 → M4/M5 sur 360 jours.
- **`REL_0446`** (`D10` → `D10`, `production-agentique-canadienne-2025-2026` → `passage-echelle-parc-agents`) : Passage des cas initiaux 2025–2026 à l'industrialisation par fabrique.
- **`REL_0468`** (`D03` → `D03`, `protocole-mcp` → `anti-verrouillage-standards`) : Prépare la migration post-gel SEP-3398 (30 mars 2027).
- **`REL_0473`** (`D03` → `D03`, `protocole-mcp` → `epinglage-schemas-mcp`) : Fenêtre de dépréciation de 12 mois jusqu'au 28 juillet 2027.
- **`REL_0478`** (`D03` → `D11`, `protocole-mcp` → `trajectoire-90j-18m-p1-p3`) : Migration MCP 2026-07-28 au 28 juillet 2027 (rampe J2).
- **`REL_0522`** (`D01` → `D11`, `revue-litterature-mlr-prisma` → `frontiere-capacites-metr-veille`) : Transfert recherche → production d'ici 2030.
- **`REL_0542`** (`D09` → `D11`, `services-bancaires-consommateurs-c15` → `horizon-2027-2032-tri-prospectif`) : Attente d'un standard technique désigné au-delà de 2026.
- **`REL_0552`** (`D07` → `D07`, `soc-soar-coupe-circuit` → `tool-poisoning-rug-pull`) : Agenda spéculatif de vérification d'intégrité continue et TEE.
- **`REL_0554`** (`D06` → `D06`, `socle-iam-federe-oauth-fapi` → `identite-non-humaine-nhi`) : Trajectoire d'étirement des RFC 2012–2026 face à l'agent.
- **`REL_0581`** (`D01` → `D11`, `systems-of-agency` → `trajectoire-90j-18m-p1-p3`) : Passage du point de départ 2027 (Stade 1) au Palier 1.
- **`REL_0591`** (`D11` → `D06`, `trajectoire-90j-18m-p1-p3` → `post-quantique-ml-dsa-slh-dsa`) : Déploiement échelonné P1 (hybride) → P2 (G7 2030–32) → P3 (2035).
- **`REL_0592`** (`D11` → `D10`, `trajectoire-90j-18m-p1-p3` → `reseaux-b2b-federes-p3`) : Ouverture conditionnelle du Stade 4 B2B au Palier 3 (2033–2035).
- **`REL_0594`** (`D11` → `D03`, `trajectoire-consolidation-standards-2027-2028` → `anti-verrouillage-standards`) : Fonde la posture suivre/contribuer/attendre sur 3 scénarios 2027–2030.
- **`REL_0595`** (`D11` → `D01`, `trajectoires-adaptatives-dapp` → `marche-ia-agentique-dispersion`) : Enveloppe 2027–2030 sous trois scénarios.
- **`REL_0596`** (`D11` → `D11`, `trajectoires-adaptatives-dapp` → `pieges-gouvernance`) : Veille continue 27 SIG parant la dérive 2028–2035.
- **`REL_0597`** (`D11` → `D06`, `trajectoires-adaptatives-dapp` → `post-quantique-ml-dsa-slh-dsa`) : Déclenche les bascules PQC sur signaux vers 2030–2035.
- **`REL_0598`** (`D11` → `D06`, `tri-prospectif-peremption-feuilles-route` → `did-vc-passeport-agent`) : Statut PROJETÉ/SPÉCULATIF des trois scénarios de passeport d'agent.
- **`REL_0599`** (`D11` → `D06`, `tri-prospectif-peremption-feuilles-route` → `kya-verification-agent-tiers`) : Expirations mécaniques à 6 mois des Internet-Drafts KYA.
- **`REL_0600`** (`D11` → `D03`, `tri-prospectif-peremption-feuilles-route` → `protocole-anp-did-wba`) : Horizon projeté ~2027 de l'infrastructure DID pour ANP.
- **`REL_0601`** (`D11` → `D03`, `tri-prospectif-peremption-feuilles-route` → `protocole-ap2`) : Transfert AP2→FIDO annoncé sans échéance de normalisation.

### `concordance_inter_tomes` (51 relations)

- **`REL_0044`** (`D12` → `D01`, `architecture-collection-tome-1-preambule` → `cout-non-interop-dette-integration`) : Fil conducteur à quatre termes parcourant les cinq Livres du Tome 1.
- **`REL_0045`** (`D12` → `D12`, `architecture-collection-tome-1-preambule` → `regime-preuve-trois-degres-absence`) : Unification des trois volumes sources sous un appareil probatoire unique.
- **`REL_0047`** (`D02` → `D02`, `architecture-reference-6-couches-2-piliers` → `noyau-controle-possede-cap`) : Aligne la vue 6 couches + 2 piliers du T3 sur le noyau possédé du corpus.
- **`REL_0055`** (`D09` → `D09`, `avis-acvm-11-348` → `maillage-reglementaire-international`) : Alignement entre attentes canadiennes en valeurs mobilières et régulation globale.
- **`REL_0070`** (`D10` → `D12`, `blueprints-reference-multisectoriels` → `concordance-inter-tomes-div02`) : Documente le mappage des 3 blueprints T6 ↔ T8.
- **`REL_0081`** (`D09` → `D09`, `bsif-e-23` → `ligne-directrice-amf`) : Pendant québécois AMF de l'arrimage fédéral E-23.
- **`REL_0105`** (`D09` → `D09`, `cadres-internationaux-imda-aica-g7` → `iso-iec-42001-nist`) : Complète NIST AI RMF et ISO 42001 (statut F) par les repères IMDA/AICA/G7.
- **`REL_0108`** (`D12` → `D10`, `calibration-feds-ema` → `fil-rouge-groupe-boreal-bel`) : Substitution des données fictives Boréal par Borealis-Bench.
- **`REL_0126`** (`D12` → `D12`, `cinq-discordances-inter-volumes-tome-8` → `concordance-inter-tomes-div02`) : Prolonge la fermeture DIV-02 en unifiant les 5 discordances pour le code G0.
- **`REL_0131`** (`D12` → `D12`, `clause-non-avis-licences` → `protocole-wyvern-g0-g5`) : Consolide la collection R et les éditions T6, T7, T8.
- **`REL_0135`** (`D12` → `D02`, `concordance-inter-tomes-div02` → `cadre-togaf-archimate-4-plans`) : Soudure 5 couches+3 volets ↔ 6 couches CAD26 §5.2.
- **`REL_0136`** (`D12` → `D02`, `concordance-inter-tomes-div02` → `echelle-autonomie-l0-l4`) : Réconcilie L0–L4 et les criticités (DISC-01, DISC-02).
- **`REL_0138`** (`D12` → `D02`, `concordance-inter-tomes-div02` → `noyau-controle-possede-cap`) : Pont typé DC-P07 des 52 CAP vers 305 EXIG-*.
- **`REL_0139`** (`D12` → `D10`, `concordance-inter-tomes-div02` → `profils-financiers-5-secteurs`) : Raccordement des 24 PEX en v1.2 (5 directes + 12 extensions + 7 comblements, contre 13 + 11 en v1.1).
- **`REL_0140`** (`D12` → `D03`, `concordance-inter-tomes-div02` → `protocole-mcp`) : Tranche MCP 2025-11-25 (T7) et 2026-07-28 (T6/T8) (DISC-05).
- **`REL_0181`** (`D01` → `D10`, `dette-cognitive-vs-technique` → `anti-patrons-agentiques`) : Dette M×N et anti-patrons Adapter Spaghetti / vernis.
- **`REL_0182`** (`D04` → `D02`, `dette-semantique-ontologies` → `catalogue-31-adr-12-dec`) : Résolution en DEC-003 de la dissonance ADR-009.
- **`REL_0196`** (`D11` → `D11`, `dix-theses-t1-t10-tome-5` → `gouvernance-duale-ae-as`) : Formalise le contrat doctrinal croisé entre AE et AS.
- **`REL_0198`** (`D08` → `D12`, `double-couloir-probatoire-pii` → `exigences-cre-ia-305`) : Primeur CAD26 ≤ 14 jours sur C27 14–30 j.
- **`REL_0210`** (`D02` → `D12`, `echelle-autonomie-l0-l4` → `architecture-collection-tome-1-preambule`) : Désambiguïsation transversale des trois échelles d'autonomie du Vol. I.
- **`REL_0212`** (`D02` → `D12`, `echelle-autonomie-l0-l4` → `concordance-inter-tomes-div02`) : Pont des échelles Stades 0–4, L0–L4, N0–N4 et LCIM.
- **`REL_0217`** (`D10` → `D10`, `eclats-sectoriels-extrapoles` → `fil-rouge-groupe-boreal-bel`) : Délimite la branche démontrée BCA/BSN des extrapolations BEL/usine.
- **`REL_0262`** (`D12` → `D02`, `exigences-cre-ia-305` → `catalogue-31-adr-12-dec`) : Réconciliation 305 EXIG-* × 75 PRR × 31 ADR → 12 DEC.
- **`REL_0264`** (`D12` → `D09`, `exigences-cre-ia-305` → `ligne-directrice-amf`) : Comblement partiel en Tome 1 Annexe N de la lacune de contenu AMF du socle.
- **`REL_0266`** (`D12` → `D12`, `exigences-cre-ia-305` → `protocole-wyvern-g0-g5`) : Comble l'Annexe D du Tome 6 par l'Annexe A du Tome 8.
- **`REL_0280`** (`D10` → `D02`, `fil-rouge-groupe-boreal-bel` → `decisions-architecture-adr-001-031`) : Fil rouge transversal validant les ADR.
- **`REL_0293`** (`D01` → `D03`, `genealogie-eai-soa-fipa-llm` → `cadre-eif-4-couches`) : Relie vingt ans d'architecture EAI/SOA/FIPA aux 5 niveaux EIF+LCIM.
- **`REL_0295`** (`D12` → `D02`, `glossaire-normatif-tome-2` → `distinction-agent-flux-ambiant`) : Aligne les définitions bilingues fr-CA/en sur le Tableau 7 du Tome 2.
- **`REL_0299`** (`D11` → `D01`, `gouvernance-duale-ae-as` → `systems-of-agency`) : Raccorde les parcours AE/AS et CISO aux fiches ADR-001..ADR-031.
- **`REL_0312`** (`D12` → `D12`, `homologation-prr-75-points` → `protocole-probatoire-l-plus-statut-f`) : Forces probatoires [N]/[M]/[É]/[S] sur PRR-75.
- **`REL_0333`** (`D09` → `D11`, `iso-iec-42001-nist` → `modele-maturite-5-niveaux-dimensions`) : Arrime les niveaux 2 à 5 aux articles ISO 42001 et NIST.
- **`REL_0338`** (`D06` → `D03`, `kya-verification-agent-tiers` → `matrice-protocoles-exigences-reglementaires`) : Croisement systématique de la grille 5Q avec la matrice protocoles × normes.
- **`REL_0341`** (`D09` → `D09`, `ligne-directrice-amf` → `bsif-e-23`) : Synchronise les échéances prudentielles du 1ᵉʳ mai 2027 Québec/fédéral.
- **`REL_0346`** (`D09` → `D12`, `ligne-directrice-amf` → `protocole-probatoire-l-plus-statut-f`) : Statut F Cloudflare + raccord CRE-IA-2026-01-QC.
- **`REL_0356`** (`D01` → `D01`, `loi-de-lusser` → `constance-pass-k`) : Convergence Lusser et décroissance (c/n)^k.
- **`REL_0364`** (`D04` → `D03`, `mediation-b2b-esb-traducteurs` → `passerelle-mcp-ai-gateway`) : Continuité des patrons de médiation de l'ESB/B2B aux passerelles agentiques.
- **`REL_0387`** (`D08` → `D06`, `observabilite-otel-genai` → `delegation-obo-deux-sauts`) : Pont Livre I / Livre II / Livre IV sur la corrélation probatoire des traces.
- **`REL_0479`** (`D12` → `D01`, `protocole-probatoire-l-plus-statut-f` → `revue-litterature-mlr-prisma`) : Audit T0 → MLR W3.2 et purge L+ W2.1.
- **`REL_0481`** (`D12` → `D12`, `protocole-wyvern-g0-g5` → `concordance-inter-tomes-div02`) : Traçabilité croisée et double recollation CA-16.
- **`REL_0482`** (`D12` → `D12`, `protocole-wyvern-g0-g5` → `exigences-cre-ia-305`) : Trace 356 corrections d'audit et 1 614 compléments entre exposés et volets CI.
- **`REL_0499`** (`D12` → `D10`, `reconciliation-inter-volumes-tome1` → `anti-patrons-agentiques`) : Alignement terminologique sur « fabrique » et « AgentMesh ».
- **`REL_0500`** (`D12` → `D02`, `reconciliation-inter-volumes-tome1` → `architecture-reference-six-couches-pc1-pc5`) : Unification des architectures en 4 et 3 couches en 6 couches communes.
- **`REL_0501`** (`D12` → `D02`, `reconciliation-inter-volumes-tome1` → `echelle-autonomie-l0-l4`) : Désambiguïsation des trois échelles homonymes de maturité/autonomie.
- **`REL_0502`** (`D12` → `D12`, `reconciliation-inter-volumes-tome1` → `peremption-revalidation-annexe-n`) : Inventaire consolidé des lacunes résiduelles et registre de gel.
- **`REL_0504`** (`D12` → `D02`, `referentiel-annexes-protocoles-chronologie` → `decisions-architecture-adr-001-031`) : Synthèse historique issue du Tome 3 (chapitres 1–47, Annexes B/C/F).
- **`REL_0505`** (`D12` → `D03`, `regime-preuve-trois-degres-absence` → `protocole-ap2`) : Arbitrage des volumes I, II et III sur la gouvernance d'AP2 (S-090 et S-091).
- **`REL_0506`** (`D12` → `D03`, `regime-preuve-trois-degres-absence` → `protocole-mcp`) : Revalidation en bloc de la révision MCP 2026-07-28 entre gel et publication.
- **`REL_0507`** (`D12` → `D07`, `regime-preuve-trois-degres-absence` → `tool-poisoning-rug-pull`) : Comblement partiel en [C] par le Vol. I de la lacune attaques du Vol. II.
- **`REL_0509`** (`D12` → `D12`, `registre-sources-tracees-annexe-b` → `clause-non-avis-licences`) : Alignement entre traçabilité des sources [A/B/C] et posture non-avis.
- **`REL_0546`** (`D07` → `D12`, `soc-soar-coupe-circuit` → `exigences-cre-ia-305`) : Réconciliation < 10 s (PRR S-14 / POR-003) et 15 min (CAD26).
- **`REL_0582`** (`D07` → `D07`, `taxonomie-attaques-identite-mandataire-confus` → `non-compositionnalite-surete-surface-attaques`) : Articulation Tome 1 ch. 5 / ch. 11 / ch. 19 et ch. 37 sur triade létale et composition.

## 7. Table complète des degrés relationnels des 260 thèmes

Tri canonique appliqué : degré total décroissant, puis arêtes sortantes décroissantes, puis slug alphabétique (`(-degré, -sortantes, slug)`).

- **`bsif-e-23`** (`D09`) : degré `30` (sortantes : 21 ; entrantes : 9).
- **`protocole-mcp`** (`D03`) : degré `25` (sortantes : 10 ; entrantes : 15).
- **`passerelle-mcp-ai-gateway`** (`D03`) : degré `24` (sortantes : 14 ; entrantes : 10).
- **`finops-focus-cpo`** (`D08`) : degré `24` (sortantes : 6 ; entrantes : 18).
- **`exigences-cre-ia-305`** (`D12`) : degré `23` (sortantes : 5 ; entrantes : 18).
- **`post-quantique-ml-dsa-slh-dsa`** (`D06`) : degré `21` (sortantes : 10 ; entrantes : 11).
- **`delegation-obo-deux-sauts`** (`D06`) : degré `21` (sortantes : 8 ; entrantes : 13).
- **`supervision-hitl-hotl-abstention`** (`D02`) : degré `20` (sortantes : 11 ; entrantes : 9).
- **`anti-verrouillage-standards`** (`D03`) : degré `20` (sortantes : 4 ; entrantes : 16).
- **`observabilite-otel-genai`** (`D08`) : degré `18` (sortantes : 11 ; entrantes : 7).
- **`protocole-a2a`** (`D03`) : degré `18` (sortantes : 6 ; entrantes : 12).
- **`eu-ai-act`** (`D09`) : degré `17` (sortantes : 13 ; entrantes : 4).
- **`echelle-autonomie-l0-l4`** (`D02`) : degré `17` (sortantes : 6 ; entrantes : 11).
- **`injection-indirecte-prompt`** (`D07`) : degré `17` (sortantes : 2 ; entrantes : 15).
- **`banc-evalops-hermetique`** (`D08`) : degré `15` (sortantes : 10 ; entrantes : 5).
- **`ligne-directrice-amf`** (`D09`) : degré `15` (sortantes : 8 ; entrantes : 7).
- **`did-vc-passeport-agent`** (`D06`) : degré `15` (sortantes : 5 ; entrantes : 10).
- **`erreurs-silencieuses-cascade`** (`D01`) : degré `15` (sortantes : 0 ; entrantes : 15).
- **`soc-soar-coupe-circuit`** (`D07`) : degré `14` (sortantes : 11 ; entrantes : 3).
- **`execution-durable-temporal`** (`D05`) : degré `14` (sortantes : 7 ; entrantes : 7).
- **`saga-compensatoire`** (`D05`) : degré `14` (sortantes : 6 ; entrantes : 8).
- **`identite-non-humaine-nhi`** (`D06`) : degré `14` (sortantes : 4 ; entrantes : 10).
- **`scellage-jcs-scitt`** (`D08`) : degré `14` (sortantes : 3 ; entrantes : 11).
- **`rag-agentique-contexte`** (`D04`) : degré `13` (sortantes : 8 ; entrantes : 5).
- **`double-couloir-probatoire-pii`** (`D08`) : degré `13` (sortantes : 7 ; entrantes : 6).
- **`couche-anti-corruption-acl`** (`D04`) : degré `13` (sortantes : 6 ; entrantes : 7).
- **`spiffe-spire-attestation`** (`D06`) : degré `13` (sortantes : 6 ; entrantes : 7).
- **`trajectoires-adaptatives-dapp`** (`D11`) : degré `13` (sortantes : 3 ; entrantes : 10).
- **`topologies-patrons-orchestration`** (`D05`) : degré `12` (sortantes : 7 ; entrantes : 5).
- **`partition-hybride-80-20`** (`D02`) : degré `12` (sortantes : 4 ; entrantes : 8).
- **`politiques-opa-rego-hors-modele`** (`D07`) : degré `12` (sortantes : 4 ; entrantes : 8).
- **`tool-poisoning-rug-pull`** (`D07`) : degré `12` (sortantes : 1 ; entrantes : 11).
- **`approbation-ciba`** (`D06`) : degré `11` (sortantes : 7 ; entrantes : 4).
- **`iso-iec-42001-nist`** (`D09`) : degré `11` (sortantes : 7 ; entrantes : 4).
- **`loi-25-article-12-1`** (`D09`) : degré `11` (sortantes : 6 ; entrantes : 5).
- **`dette-semantique-ontologies`** (`D04`) : degré `11` (sortantes : 5 ; entrantes : 6).
- **`protocole-ap2`** (`D03`) : degré `11` (sortantes : 5 ; entrantes : 6).
- **`noyau-controle-possede-cap`** (`D02`) : degré `11` (sortantes : 3 ; entrantes : 8).
- **`constance-pass-k`** (`D01`) : degré `11` (sortantes : 2 ; entrantes : 9).
- **`agntcy-slim`** (`D03`) : degré `10` (sortantes : 7 ; entrantes : 3).
- **`choregraphie-event-mesh`** (`D05`) : degré `10` (sortantes : 7 ; entrantes : 3).
- **`concordance-inter-tomes-div02`** (`D12`) : degré `10` (sortantes : 6 ; entrantes : 4).
- **`efvp-transfert-hors-quebec`** (`D09`) : degré `10` (sortantes : 6 ; entrantes : 4).
- **`anti-patrons-agentiques`** (`D10`) : degré `10` (sortantes : 5 ; entrantes : 5).
- **`blueprints-reference-multisectoriels`** (`D10`) : degré `10` (sortantes : 5 ; entrantes : 5).
- **`protocole-wyvern-g0-g5`** (`D12`) : degré `10` (sortantes : 4 ; entrantes : 6).
- **`systems-of-agency`** (`D01`) : degré `10` (sortantes : 3 ; entrantes : 7).
- **`memoire-coala-4-tiroirs`** (`D04`) : degré `9` (sortantes : 7 ; entrantes : 2).
- **`gouvernance-duale-ae-as`** (`D11`) : degré `9` (sortantes : 2 ; entrantes : 7).
- **`agent-card-decouverte`** (`D03`) : degré `8` (sortantes : 4 ; entrantes : 4).
- **`cadre-eif-4-couches`** (`D03`) : degré `8` (sortantes : 3 ; entrantes : 5).
- **`dette-cognitive-vs-technique`** (`D01`) : degré `8` (sortantes : 1 ; entrantes : 7).
- **`avis-acvm-11-348`** (`D09`) : degré `7` (sortantes : 6 ; entrantes : 1).
- **`trousse-executable-tome-8`** (`D12`) : degré `7` (sortantes : 6 ; entrantes : 1).
- **`clause-non-avis-licences`** (`D12`) : degré `7` (sortantes : 4 ; entrantes : 3).
- **`epinglage-schemas-mcp`** (`D03`) : degré `7` (sortantes : 4 ; entrantes : 3).
- **`atrophie-competences-humaines`** (`D11`) : degré `7` (sortantes : 3 ; entrantes : 4).
- **`fil-rouge-groupe-boreal-bel`** (`D10`) : degré `7` (sortantes : 3 ; entrantes : 4).
- **`trajectoire-90j-18m-p1-p3`** (`D11`) : degré `7` (sortantes : 3 ; entrantes : 4).
- **`confinement-shadi-sandbox`** (`D07`) : degré `6` (sortantes : 5 ; entrantes : 1).
- **`arbre-sobriete-oo1-oo4`** (`D05`) : degré `6` (sortantes : 4 ; entrantes : 2).
- **`cadre-togaf-archimate-4-plans`** (`D02`) : degré `6` (sortantes : 4 ; entrantes : 2).
- **`regle-maillon-plus-eleve`** (`D02`) : degré `6` (sortantes : 4 ; entrantes : 2).
- **`encapsulation-patrimoine-it-ot`** (`D04`) : degré `6` (sortantes : 3 ; entrantes : 3).
- **`regle-de-deux-opa`** (`D07`) : degré `6` (sortantes : 3 ; entrantes : 3).
- **`profils-financiers-5-secteurs`** (`D10`) : degré `6` (sortantes : 1 ; entrantes : 5).
- **`fabrique-agents-certification-reemission`** (`D10`) : degré `5` (sortantes : 4 ; entrantes : 1).
- **`peremption-revalidation-annexe-n`** (`D12`) : degré `5` (sortantes : 4 ; entrantes : 1).
- **`tri-prospectif-peremption-feuilles-route`** (`D11`) : degré `5` (sortantes : 4 ; entrantes : 1).
- **`regime-preuve-trois-degres-absence`** (`D12`) : degré `5` (sortantes : 3 ; entrantes : 2).
- **`routage-cognitif-hybride-3-paliers`** (`D03`) : degré `5` (sortantes : 3 ; entrantes : 2).
- **`kya-verification-agent-tiers`** (`D06`) : degré `5` (sortantes : 2 ; entrantes : 3).
- **`non-compositionnalite-surete-surface-attaques`** (`D07`) : degré `5` (sortantes : 2 ; entrantes : 3).
- **`pieges-gouvernance`** (`D11`) : degré `5` (sortantes : 2 ; entrantes : 3).
- **`registre-agents-cycle-de-vie-et-attestations`** (`D11`) : degré `5` (sortantes : 2 ; entrantes : 3).
- **`registres-gouvernes-trois-modeles`** (`D06`) : degré `5` (sortantes : 0 ; entrantes : 5).
- **`certificats-tls-47-jours`** (`D06`) : degré `4` (sortantes : 4 ; entrantes : 0).
- **`contrats-interfaces-catalogue-entreprise`** (`D03`) : degré `4` (sortantes : 4 ; entrantes : 0).
- **`grille-cinq-questions-identite`** (`D06`) : degré `4` (sortantes : 4 ; entrantes : 0).
- **`maillage-agents-pep-pdp-zero-trust`** (`D07`) : degré `4` (sortantes : 4 ; entrantes : 0).
- **`reconciliation-inter-volumes-tome1`** (`D12`) : degré `4` (sortantes : 4 ; entrantes : 0).
- **`clauses-contractuelles-normatives-app`** (`D09`) : degré `4` (sortantes : 3 ; entrantes : 1).
- **`frontiere-capacites-metr-veille`** (`D11`) : degré `4` (sortantes : 3 ; entrantes : 1).
- **`harnais-deterministe-8-etapes`** (`D02`) : degré `4` (sortantes : 3 ; entrantes : 1).
- **`volant-distillation-dspy-multilora`** (`D08`) : degré `4` (sortantes : 3 ; entrantes : 1).
- **`semantique-effet-idempotence-uetr`** (`D05`) : degré `4` (sortantes : 2 ; entrantes : 2).
- **`decisions-architecture-adr-001-031`** (`D02`) : degré `4` (sortantes : 1 ; entrantes : 3).
- **`signature-agent-card-ancrage`** (`D06`) : degré `4` (sortantes : 1 ; entrantes : 3).
- **`taxonomie-attaques-identite-mandataire-confus`** (`D07`) : degré `4` (sortantes : 1 ; entrantes : 3).
- **`horizon-2027-2032-tri-prospectif`** (`D11`) : degré `4` (sortantes : 0 ; entrantes : 4).
- **`actualisation-novembre-2026-unification-v1-2`** (`D12`) : degré `3` (sortantes : 3 ; entrantes : 0).
- **`calibration-feds-ema`** (`D12`) : degré `3` (sortantes : 3 ; entrantes : 0).
- **`plateforme-iap-gitops-cognitif`** (`D10`) : degré `3` (sortantes : 3 ; entrantes : 0).
- **`pont-reglementation-frames-deterministes`** (`D02`) : degré `3` (sortantes : 3 ; entrantes : 0).
- **`souverainete-espaces-donnees-tee-hyok`** (`D09`) : degré `3` (sortantes : 3 ; entrantes : 0).
- **`usine-logicielle-agentic-sdlc`** (`D02`) : degré `3` (sortantes : 3 ; entrantes : 0).
- **`architecture-collection-tome-1-preambule`** (`D12`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`classes-risque-agents-et-plafonds`** (`D09`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`confinement-opensandbox-firecracker-wasi`** (`D07`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`crypto-agilite-migration-pqc`** (`D06`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`distinction-agent-flux-ambiant`** (`D02`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`federation-multi-plateformes-gravite`** (`D10`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`feuille-de-route-phases-90-jours-indicateurs`** (`D11`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`feuille-route-1er-mai-2027`** (`D09`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`iso-20022-lynx-rtr`** (`D04`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`journalisation-probatoire-audit`** (`D08`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`priorites-90-jours-gouvernance`** (`D11`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`socle-iam-federe-oauth-fapi`** (`D06`) : degré `3` (sortantes : 2 ; entrantes : 1).
- **`catalogue-31-adr-12-dec`** (`D02`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`chaine-approvisionnement-agent-skills`** (`D07`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`ecart-accord-protocolaire-comprehension`** (`D04`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`evaluation-continue-derives`** (`D08`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`homologation-prr-75-points`** (`D12`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`maillage-b2b-federe-edc-odrl`** (`D03`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`modele-maturite-5-niveaux-dimensions`** (`D11`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`plan-inference-routage-carbone`** (`D08`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`production-agentique-canadienne-2025-2026`** (`D10`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`profil-groupe-diversifie-m18`** (`D10`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`protocole-probatoire-l-plus-statut-f`** (`D12`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`trajectoire-consolidation-standards-2027-2028`** (`D11`) : degré `3` (sortantes : 1 ; entrantes : 2).
- **`cout-non-interop-dette-integration`** (`D01`) : degré `3` (sortantes : 0 ; entrantes : 3).
- **`matrice-protocoles-exigences-reglementaires`** (`D03`) : degré `3` (sortantes : 0 ; entrantes : 3).
- **`memoire-bi-temporelle-et-purge`** (`D04`) : degré `3` (sortantes : 0 ; entrantes : 3).
- **`modes-echecs-emergents-frontiere`** (`D05`) : degré `3` (sortantes : 0 ; entrantes : 3).
- **`pathologies-reactives-backpressure`** (`D05`) : degré `3` (sortantes : 0 ; entrantes : 3).
- **`vertical-financier-durci`** (`D10`) : degré `3` (sortantes : 0 ; entrantes : 3).
- **`confinement-cua-patrimoine-sans-api`** (`D04`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`contrats-api-versionnement-conformite`** (`D03`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`contrats-donnees-write-audit-publish`** (`D04`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`contrats-types-executes-ci-annexe-c`** (`D12`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`criteres-evaluation-fournisseurs-grille`** (`D09`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`eclats-sectoriels-extrapoles`** (`D10`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`evaluation-agentique-bancs-capacite`** (`D08`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`frameworks-orchestration-entreprise`** (`D05`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`genealogie-eai-soa-fipa-llm`** (`D01`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`grille-homologation-et-fiche-agent`** (`D12`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`profil-banque-m14`** (`D10`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`reprise-sinistre-cognitif-continuite`** (`D10`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`services-bancaires-consommateurs-c15`** (`D09`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`validation-json-schema-ambigu-escalade`** (`D02`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`web-agentique-webmcp-webbotauth`** (`D03`) : degré `2` (sortantes : 2 ; entrantes : 0).
- **`annuaires-commerciaux-risque-standard-de-fait`** (`D06`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`architecture-reference-6-couches-2-piliers`** (`D02`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`canonicalisation-jcs-rfc8785`** (`D08`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`defense-hors-modele-camel-confinement`** (`D07`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`donnees-pretes-agents-odcs-openlineage`** (`D04`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`droit-effacement-portabilite-loi-25`** (`D09`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`echanges-intentions-contrats-probabilistes`** (`D01`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`economie-industrialisation-cognitive`** (`D01`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`facades-mcp-intention-metier`** (`D03`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`gouvernance-acces-rag-ancrage`** (`D04`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`gouvernance-interne-registre-trois-lignes`** (`D09`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`gouvernance-raci-modele-en-etoile`** (`D11`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`indicateurs-agentops-horizon-tache`** (`D08`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`inventaire-revocation-asymetrie`** (`D06`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`loi-de-lusser`** (`D01`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`maillage-reglementaire-international`** (`D09`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`memoire-partagee-concurrence-effacement`** (`D04`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`modele-maturite-feuille-360j`** (`D10`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`modele-operationnel-hub-and-spoke`** (`D11`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`plateformes-saas-et-asymetrie-tiers`** (`D10`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`pont-ia-physique-ros2-simplex`** (`D05`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`profil-assurance-dommages-m17`** (`D10`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`profil-assurance-personnes-m16`** (`D10`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`profil-gestion-patrimoine-m15`** (`D10`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`protocole-anp-did-wba`** (`D03`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`protocoles-interfaces-agui-a2ui-webrtc`** (`D03`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`provenance-artefacts-aibom-5-horloges`** (`D08`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`referentiel-annexes-protocoles-chronologie`** (`D12`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`reseaux-b2b-federes-p3`** (`D10`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`resilience-orchestration-repli-plafonds`** (`D05`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`responsabilite-mandat-contrats-b2b`** (`D09`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`revue-litterature-mlr-prisma`** (`D01`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`separation-controleur-executeur-determinisme`** (`D02`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`sre-autonome-rayon-impact-cedar`** (`D07`) : degré `2` (sortantes : 1 ; entrantes : 1).
- **`architecture-reference-six-couches-pc1-pc5`** (`D02`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`clauses-sortie-portabilite-interchangeabilite`** (`D02`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`criteres-qos-cout-precision-latence`** (`D02`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`raisonnement-inference-limites-planification`** (`D01`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`regime-derogations-et-transition-cohorte`** (`D11`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`six-substrats-etat-souverainete`** (`D04`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`tampon-deterministe-rtr-iso20022`** (`D10`) : degré `2` (sortantes : 0 ; entrantes : 2).
- **`adaptateur-mcp-streamable-http-sep-3398`** (`D03`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`alignement-deceptif-red-teaming-adversarial`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`approbation-reflexe-biais-automatisation`** (`D11`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`architecture-outils-fiables-erreurs-actionnables`** (`D02`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`audit-validation-sources-121-449`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`barriere-logicielle-g0-execute-g0`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`blueprint-1-assistant-sor`** (`D10`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`blueprint-2-enclave-rag-acl`** (`D10`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`blueprint-3-maillage-b2b`** (`D10`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`cadres-internationaux-imda-aica-g7`** (`D09`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`cadriciels-orchestration-portabilite`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`canal-compensation-isole-outbox`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`canonisation-deterministe-jcs`** (`D08`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`caviardage-pii-rp-bilingue`** (`D08`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`cinq-discordances-inter-volumes-tome-8`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`clauses-reversibilite-cloud-souverain`** (`D09`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`comptabilite-carbone-cap-046-bsif-b15`** (`D08`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`confidentialite-materielle-tee-hyok`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`controle-surete-stamp-stpa`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`couts-transaction-coase`** (`D01`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`dimensionnement-wilson-evalops`** (`D08`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`dix-interdictions-exig-gov-17`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`dix-theses-t1-t10-tome-5`** (`D11`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`douze-principes-directeurs-prin`** (`D02`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`echec-ferme-opa-default-deny`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`economie-jetons-routage-slm`** (`D01`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`enveloppes-bpmn-cas-routine`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`ergonomie-aci-anti-swagger`** (`D03`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`etat-des-lieux-adoption-map-2027`** (`D01`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`fiabilite-coordination-taxonomie-mast`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`gabarit-typst-edition-4542-pages`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`glossaire-normatif-tome-2`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`grille-evaluation-maturite-n1-n5`** (`D02`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`hierarchie-preuves-etudes-cas`** (`D01`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`liaison-jetons-dpop-mtls`** (`D06`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`maillage-agentique-trois-acceptions`** (`D03`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`mediation-b2b-esb-traducteurs`** (`D04`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`metriques-soutien-vs-production`** (`D03`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`modele-comme-juge-biais-calibration`** (`D08`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`negociation-b2b-diplomate-evaluateur`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`paradigme-apm-autonomie-encadree`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`portee-et-force-normative-cre-ia`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`propagation-acl-memoire-silo`** (`D04`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`protocoles-ressources-physiques-lap`** (`D05`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`quadruple-dette-agentique`** (`D01`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`quinze-portes-homologation-por`** (`D11`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`rails-paiement-commerce-agentique`** (`D03`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`red-teaming-continu-empoisonnement-memoire`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`registre-sources-tracees-annexe-b`** (`D12`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`requetes-riches-rar-txn-tokens`** (`D06`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`sanctuarisation-vivier-junior-reprise`** (`D11`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`saturation-http-431-ml-dsa-kid`** (`D06`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`separation-controle-donnees-camel`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`surcout-multi-agent-debat-mast`** (`D01`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`synchronisation-edge-crdt`** (`D04`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`systeme-qualite-en-18286-dora-cra`** (`D09`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`taxonomie-owasp-asi-mcp-maestro`** (`D07`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`tests-metamorphiques-fr-en-sans-oracle`** (`D08`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`vide-federal-ia-c27-c36`** (`D09`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`vingt-sept-signaux-veille-sig`** (`D11`) : degré `1` (sortantes : 1 ; entrantes : 0).
- **`approvisionnement-reversible-contrats`** (`D09`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`cinq-blocs-sbb-tableau-12`** (`D12`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`coexistence-bpm-ipaas-rpa`** (`D04`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`contexte-minimal-delegation-interagents`** (`D05`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`cycle-vie-operationnel-derives-gitops`** (`D08`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`formats-echange-registres-schemas`** (`D04`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`fusion-acp-collision-terminologique`** (`D03`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`incidents-agentiques-et-notification-multiregime`** (`D09`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`marche-ia-agentique-dispersion`** (`D01`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`passage-echelle-parc-agents`** (`D10`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`patrons-boucle-mono-agent-codeact`** (`D02`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`plan-donnees-inference-kv-cache`** (`D03`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`principes-architecture-pri-001-015`** (`D02`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`profil-oauth-9700-et-liaison-expediteur`** (`D06`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`responsabilite-litiges-commerce-agentique`** (`D11`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`rupture-modele-conversationnel-agent-boucle`** (`D01`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`saga-dix-scenarios-fautes`** (`D05`) : degré `1` (sortantes : 0 ; entrantes : 1).
- **`taxonomie-acteurs-agentiques`** (`D01`) : degré `1` (sortantes : 0 ; entrantes : 1).
<!-- BIBLIOGRAPHIE_BRUTE_FIN -->
