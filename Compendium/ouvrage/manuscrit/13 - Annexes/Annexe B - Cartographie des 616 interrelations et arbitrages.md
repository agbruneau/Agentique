# Annexe B — Cartographie analytique des 616 interrelations systémiques, nœuds carrefours et arbitrages

Cette annexe compile mécaniquement depuis `registre/mindmap-complet.json` la topologie des **616 interrelations typées** reliant les **260 thèmes** du Compendium répartis sur douze domaines (`D01`–`D12`). Le degré moyen s'établit à **4,74** arêtes par thème ; **391 liaisons (63,5 %)** franchissent une frontière de domaine tandis que **225 liaisons (36,5 %)** consolident la cohérence interne d'un même domaine.

## 1. Répartition et sémantique des huit types canoniques d'interrelations

| Type d'interrelation | Effectif | Part | Règle sémantique |
|---|---:|---:|---|
| `operationnalisation` | 132 | 21,4 % | source est mis en œuvre ou rendu testable par target (ou inversement selon étiquetage explicite) |
| `dependance_technique` | 93 | 15,1 % | source dépend de target comme prérequis architectural ou cryptographique |
| `encadrement_normatif` | 82 | 13,3 % | source (cadre légal/normatif) encadre et contraint target |
| `attenuation_risque` | 81 | 13,1 % | source atténue ou neutralise la vulnérabilité ou dérive représentée par target |
| `amplification_synergie` | 63 | 10,2 % | source amplifie l'efficacité, la fiabilité ou l'impact de target |
| `tension_arbitrage` | 62 | 10,1 % | source entre en tension ou exige un arbitrage explicite face à target |
| `projection_temporelle` | 52 | 8,4 % | source projette ou prépare sa transition vers target sur l'horizon temporel |
| `concordance_inter_tomes` | 51 | 8,3 % | source et target s'alignent ou se réconcilient entre plusieurs tomes (ex. DIV-02, DISC-01..05) |

## 3. Analyse des vingt-cinq nœuds carrefours à plus fort degré relationnel

- **1. `bsif-e-23`** (`D09`, degré **30**: 22 sortantes, 8 entrantes) — Architecture prudentielle fédérale: BSIF E-23 (1er mai 2027), B-10/B-13/E-21/B-15 et temporisation 2033.

- **2. `protocole-mcp`** (`D03`, degré **25**: 11 sortantes, 14 entrantes) — Protocole MCP (2026-07-28) sans état, ≤ 15 outils d'intention et bascule juillet 2027.

- **3. `passerelle-mcp-ai-gateway`** (`D03`, degré **24**: 13 sortantes, 11 entrantes) — Passerelle d'agents bidirectionnelle PEP à 9 contrôles ordonnés et budget Borealis-Bench.

- **4. `finops-focus-cpo`** (`D08`, degré **24**: 6 sortantes, 18 entrantes) — Pilotage économique au coût complet par résultat conforme (CPO), FOCUS 1.4 et disjoncteurs.

- **5. `exigences-cre-ia-305`** (`D12`, degré **23**: 6 sortantes, 17 entrantes) — Porte unique d'homologation: 305 EXIG-* v1.2 × 75 PRR (24 bloquants) × 15 POR et 10 interdits GOV-17.

- **6. `post-quantique-ml-dsa-slh-dsa`** (`D06`, degré **21**: 11 sortantes, 10 entrantes) — Transition post-quantique (FIPS 203/204/205, NIST IR 8547), choc HTTP 431 (50–72×) et CBOR-COSE.

- **7. `delegation-obo-deux-sauts`** (`D06`, degré **21**: 8 sortantes, 13 entrantes) — Rupture au deuxième saut (RFC 8693 §4.1), délégation atténuée ≤ 2 sauts et DPoP/mTLS.

- **8. `anti-verrouillage-standards`** (`D03`, degré **20**: 7 sortantes, 13 entrantes) — Confinement anti-verrouillage SaaS (EXIG-ARC-21), catalogues déclaratifs C1 et statut AP2/AGNTCY.

- **9. `supervision-hitl-hotl-abstention`** (`D02`, degré **20**: 10 sortantes, 10 entrantes) — Ergonomie anti-complaisance (ASI09), vue différentielle et distinction entre PC3 et art. 12.1.

- **10. `injection-indirecte-prompt`** (`D07`, degré **19**: 4 sortantes, 15 entrantes) — Modélisation des menaces OWASP ASI01–10 / MITRE ATLAS, isolation CaMeL (77 % contre 84 %) et tests FR/EN.

- **11. `protocole-a2a`** (`D03`, degré **18**: 6 sortantes, 12 entrantes) — Non-substituabilité entre outil et pair, protocole A2A v1.0.1 et asymétrie 0/15 (Z1–Z5).

- **12. `observabilite-otel-genai`** (`D08`, degré **18**: 12 sortantes, 6 entrantes) — Télémétrie OpenTelemetry v1.41.0 épinglée (face à v1.44.0 Development) et jointure trace ↔ mandat.

- **13. `echelle-autonomie-l0-l4`** (`D02`, degré **17**: 6 sortantes, 11 entrantes) — Gouvernance matricielle: 8 domaines D1–D8 × Stades 0–4 × Classes 1–6 × N0–N4/P0–P3.

- **14. `eu-ai-act`** (`D09`, degré **17**: 13 sortantes, 4 entrantes) — Droit européen applicable par effet extraterritorial: AI Act (Annexe III décembre 2027), Data Act et DORA.

- **15. `erreurs-silencieuses-cascade`** (`D01`, degré **16**: 3 sortantes, 13 entrantes) — Rupture entre validité syntaxique et erreurs sémantiques silencieuses.

- **16. `ligne-directrice-amf`** (`D09`, degré **15**: 9 sortantes, 6 entrantes) — Encadrement AMF Québec: Note AMF IA (41 attentes → 12 EXIG-AMF-01..12), lois d'assurance et statut F.

- **17. `banc-evalops-hermetique`** (`D08`, degré **15**: 7 sortantes, 8 entrantes) — Évaluation continue E1–E3 (pass^k), juge calibré et abaissement d'autonomie sur dérive SLO.

- **18. `did-vc-passeport-agent`** (`D06`, degré **15**: 5 sortantes, 10 entrantes) — Identité légale vérifiable GLEIF vLEI, lacune KYA (0/9) et encadrement des agents externes.

- **19. `execution-durable-temporal`** (`D05`, degré **14**: 7 sortantes, 7 entrantes) — Exécution durable hors processus, idempotence JCS SHA-256 et revalidation au réveil (TOCTOU).

- **20. `saga-compensatoire`** (`D05`, degré **14**: 6 sortantes, 8 entrantes) — Patron Saga à point pivot, tampon d'irréversibilité et canal de compensation dédié EXIG-ORC-28.

- **21. `scellage-jcs-scitt`** (`D08`, degré **14**: 3 sortantes, 11 entrantes) — Journal d'audit à 5 éléments canonisé RFC 8785 (JCS), ancré chaque heure et scellé SCITT + SLH-DSA.

- **22. `identite-non-humaine-nhi`** (`D06`, degré **14**: 5 sortantes, 9 entrantes) — Diagnostic Q-A..Q-E (0/15), identités non humaines (NHI) parrainées et bannissement des secrets fixes.

- **23. `soc-soar-coupe-circuit`** (`D07`, degré **14**: 10 sortantes, 4 entrantes) — Coupe-circuit hiérarchisé (< 10 s POR-003 contre 15 min CAD26), SSF/CAEP et rétrogradation < 60 s.

- **24. `spiffe-spire-attestation`** (`D06`, degré **13**: 5 sortantes, 8 entrantes) — Attestations cryptographiques éphémères SPIFFE X.509-SVID, OIDC et veille WIMSE / OAuth 2.1.

- **25. `trajectoires-adaptatives-dapp`** (`D11`, degré **13**: 3 sortantes, 10 entrantes) — Parcours adaptatifs DAPP sans probabilité (A/B/C), modélisation EMA et portefeuille 43 INI / 15 POR / 27 SIG.

## 4. Corridors inter-domaines dominants et densité sur les huit tomes (`T1`–`T8`)

L'empreinte transversale sur les huit tomes antérieurs (`concordance_matrix`) totalise: `T1` (246 rattachements, 844 occurrences), `T2` (162 rattachements, 344 occurrences), `T3` (230 rattachements, 1458 occurrences), `T4` (164 rattachements, 398 occurrences), `T5` (192 rattachements, 312 occurrences), `T6` (122 rattachements, 156 occurrences), `T7` (136 rattachements, 192 occurrences), `T8` (128 rattachements, 148 occurrences).

- **`D09` → `D11`** (14 liaisons): Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Prospective 2028–2035, trajectoires DAPP et capital humain.
- **`D09` → `D10`** (13 liaisons): Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Architectures sectorielles, blueprints et cas métier.
- **`D03` → `D06`** (12 liaisons): Interopérabilité protocolaire, découverte et passerelles (MCP, A2A, AGNTCY, AP2) vers Identité non humaine (NHI), chaîne de mandat et post-quantique.
- **`D09` → `D02`** (12 liaisons): Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4).
- **`D10` → `D02`** (11 liaisons): Architectures sectorielles, blueprints et cas métier vers Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4).
- **`D09` → `D08`** (9 liaisons): Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme.
- **`D12` → `D02`** (9 liaisons): Homologation vérifiable, trousse exécutable, concordance et Wyvern/G0–G5 vers Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4).
- **`D03` → `D07`** (9 liaisons): Interopérabilité protocolaire, découverte et passerelles (MCP, A2A, AGNTCY, AP2) vers Sécurité hors modèle, confinement déterministe (OPA, Règle de deux) et défense SOC.

- **`D04` → `D07`** (8 liaisons): Sémantique métier, contexte, mémoire CoALA et intégration patrimoniale (ACL/OT) vers Sécurité hors modèle, confinement déterministe (OPA, Règle de deux) et défense SOC.
- **`D02` → `D01`** (8 liaisons): Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4) vers Fondements épistémiques, économiques et rupture agentique.
- **`D06` → `D08`** (7 liaisons): Identité non humaine (NHI), chaîne de mandat et post-quantique vers Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme.
- **`D08` → `D01`** (7 liaisons): Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme vers Fondements épistémiques, économiques et rupture agentique.
- **`D02` → `D10`** (6 liaisons): Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4) vers Architectures sectorielles, blueprints et cas métier.
- **`D09` → `D06`** (6 liaisons): Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Identité non humaine (NHI), chaîne de mandat et post-quantique.
- **`D09` → `D04`** (6 liaisons): Droit, régulation prudentielle (QC, CA, UE, int.) et contrats vers Sémantique métier, contexte, mémoire CoALA et intégration patrimoniale (ACL/OT).

## 5. Catalogue analytique des 62 arbitrages structurels (`tension_arbitrage`)

### Arbitrages issus de `D01` (6)

- `REL_0150` (de `constance-pass-k` vers `finops-focus-cpo`): Arbitre le coût de vérification face à la fiabilité requise.
- `REL_0218` (de `economie-industrialisation-cognitive` vers `anti-verrouillage-standards`): Arbitre vitesse des agents SaaS et contrôle architectural.
- `REL_0219` (de `economie-jetons-routage-slm` vers `raisonnement-inference-limites-planification`): Arbitrage coût des jetons de réflexion face au gain de qualité à l'inférence.
- `REL_0311` (de `hierarchie-preuves-etudes-cas` vers `protocole-a2a`): Spécifications stables face à la rareté des preuves en production.
- `REL_0575` (de `surcout-multi-agent-debat-mast` vers `separation-controleur-executeur-determinisme`): Contexte isolé multi-agents (15×) face au rédacteur unique continu.
- `REL_0578` (de `systems-of-agency` vers `anti-verrouillage-standards`): Déplace le verrouillage vers les plateformes.

### Arbitrages issus de `D02` (9)

- `REL_0215` (de `echelle-autonomie-l0-l4` vers `supervision-hitl-hotl-abstention`): Montée en autonomie bornée contre capacité cognitive de supervision humaine.
- `REL_0398` (de `partition-hybride-80-20` vers `constance-pass-k`): Compromis coût en jetons / précision / latence (courbe HAL).
- `REL_0515` (de `regle-maillon-plus-eleve` vers `profil-groupe-diversifie-m18`): Mutualisation du socle technique face au cloisonnement des filiales.
- `REL_0568` (de `supervision-hitl-hotl-abstention` vers `atrophie-competences-humaines`): Automatisation de routine et maintien du discernement et de la relève junior.
- `REL_0569` (de `supervision-hitl-hotl-abstention` vers `criteres-qos-cout-precision-latence`): Oppose latence opérationnelle et exigence d'approbation humaine.
- `REL_0570` (de `supervision-hitl-hotl-abstention` vers `echelle-autonomie-l0-l4`): Vitesse d'autonomie et fatigue d'approbation.
- `REL_0571` (de `supervision-hitl-hotl-abstention` vers `erreurs-silencieuses-cascade`): Charge d'approbation humaine face au biais de complaisance.
- `REL_0572` (de `supervision-hitl-hotl-abstention` vers `loi-25-article-12-1`): Évite l'approbation nominale qui rend la décision automatisée.
- `REL_0573` (de `supervision-hitl-hotl-abstention` vers `matrice-protocoles-exigences-reglementaires`): Paradoxe de l'inversement sur l'intervention humaine.

### Arbitrages issus de `D03` (8)

- `REL_0014` (de `agntcy-slim` vers `protocole-a2a`): Positionnement officiel d'AGNTCY nuancé par chevauchement tiers sur ACP.
- `REL_0152` (de `contrats-api-versionnement-conformite` vers `anti-verrouillage-standards`): Paradoxe du verrouillage inverse sur l'interface de fait OpenAI.
- `REL_0404` (de `passerelle-mcp-ai-gateway` vers `anti-verrouillage-standards`): Portabilité par passerelle de médiation contre plus petit dénominateur commun.
- `REL_0459` (de `protocole-a2a` vers `journalisation-probatoire-audit`): Découverte ouverte fédérée face à la gouvernance des clés et à l'imputation.
- `REL_0460` (de `protocole-a2a` vers `topologies-patrons-orchestration`): Opacité voulue d'A2A contre exigence d'auditabilité réglementaire.
- `REL_0476` (de `protocole-mcp` vers `protocole-a2a`): Frontière floue entre tâches asynchrones MCP et délégation A2A.
- `REL_0523` (de `routage-cognitif-hybride-3-paliers` vers `constance-pass-k`): Économie SLM face au risque de baisse de précision et de constance.
- `REL_0615` (de `web-agentique-webmcp-webbotauth` vers `protocole-ap2`): Oppose l'authentification par origine HTTP à la preuve d'intention signée.

### Arbitrages issus de `D04` (4)

- `REL_0142` (de `confinement-cua-patrimoine-sans-api` vers `couche-anti-corruption-acl`): Tolère CUA à ≤ 8 % sous bail 12 mois contre refactoring MCP durable.
- `REL_0183` (de `dette-semantique-ontologies` vers `ecart-accord-protocolaire-comprehension`): Expressivité ontologique coûteuse face à la souplesse fragile en prose.
- `REL_0366` (de `memoire-coala-4-tiroirs` vers `did-vc-passeport-agent`): Apprentissage continu en production face à la validité datée du passeport.
- `REL_0495` (de `rag-agentique-contexte` vers `injection-indirecte-prompt`): Agrandir la fenêtre dilue l'attention et élargit la surface ASI01.

### Arbitrages issus de `D05` (7)

- `REL_0042` (de `arbre-sobriete-oo1-oo4` vers `protocole-a2a`): Sobriété agent unique face au surcoût multi-agents (-70 % à +80,8 %).
- `REL_0124` (de `choregraphie-event-mesh` vers `topologies-patrons-orchestration`): Arbitre l'autonomie événementielle face à la maîtrise transactionnelle.
- `REL_0259` (de `execution-durable-temporal` vers `semantique-effet-idempotence-uetr`): Illusion du rollback logiciel face à l'irréversibilité métier.
- `REL_0288` (de `frameworks-orchestration-entreprise` vers `anti-verrouillage-standards`): Frontière commerciale des plateformes managées face à la portabilité ouverte.
- `REL_0530` (de `saga-compensatoire` vers `soc-soar-coupe-circuit`): Arrêt d'urgence et intégrité comptable des sagas en vol.
- `REL_0531` (de `saga-compensatoire` vers `tampon-deterministe-rtr-iso20022`): Interdit la compensation a posteriori sur virements RTR irrévocables.
- `REL_0589` (de `topologies-patrons-orchestration` vers `finops-focus-cpo`): Arbitre gain F1 réflexif/multi-agents contre explosion de coût 4x–15x.

### Arbitrages issus de `D06` (6)

- `REL_0018` (de `annuaires-commerciaux-risque-standard-de-fait` vers `anti-verrouillage-standards`): Adoption immédiate d'annuaires propriétaires par rapport à l'attente de normes neutres.
- `REL_0117` (de `certificats-tls-47-jours` vers `post-quantique-ml-dsa-slh-dsa`): Collision rotation TLS 47 jours et taille PQC sur passerelles.
- `REL_0323` (de `inventaire-revocation-asymetrie` vers `spiffe-spire-attestation`): Durée de vie courte (24 h) comme substitut partiel à la révocation.
- `REL_0438` (de `post-quantique-ml-dsa-slh-dsa` vers `delegation-obo-deux-sauts`): Poids des signatures ML-DSA face à la limite des en-têtes HTTP 431.
- `REL_0439` (de `post-quantique-ml-dsa-slh-dsa` vers `passerelle-mcp-ai-gateway`): Taille des signatures post-quantiques face aux contraintes réseau.
- `REL_0560` (de `spiffe-spire-attestation` vers `did-vc-passeport-agent`): Infrastructure centralisée intra-domaine (SPIFFE) face à la portabilité écosystémique (DID).

### Arbitrages issus de `D07` (4)

- `REL_0144` (de `confinement-opensandbox-firecracker-wasi` vers `anti-verrouillage-standards`): Isolation stricte face à la latence et à la complexité KVM.
- `REL_0320` (de `injection-indirecte-prompt` vers `constance-pass-k`): Coût d'utilité de la sécurité CaMeL (77 % contre 84 %).
- `REL_0358` (de `maillage-agents-pep-pdp-zero-trust` vers `finops-focus-cpo`): Surcoût de latence, complexité et inférence des contrôles par arête.
- `REL_0511` (de `regle-de-deux-opa` vers `supervision-hitl-hotl-abstention`): Accroît le volume d'approbations après contamination.

### Arbitrages issus de `D08` (4)

- `REL_0063` (de `banc-evalops-hermetique` vers `finops-focus-cpo`): Coût de simulation face au risque d'erreur en production.
- `REL_0201` (de `double-couloir-probatoire-pii` vers `observabilite-otel-genai`): Diagnostic complet face à la minimisation Loi 25 et RGPD.
- `REL_0282` (de `finops-focus-cpo` vers `dette-cognitive-vs-technique`): Baisse du prix du jeton face à l'explosion du CPO par relecture.
- `REL_0613` (de `volant-distillation-dspy-multilora` vers `memoire-bi-temporelle-et-purge`): Apprentissage sur traces face au risque de fuite et de biais.

### Arbitrages issus de `D09` (2)

- `REL_0226` (de `efvp-transfert-hors-quebec` vers `systems-of-agency`): Souveraineté des données financières face à l'accès aux modèles de pointe.
- `REL_0557` (de `souverainete-espaces-donnees-tee-hyok` vers `finops-focus-cpo`): Souveraineté, HYOK et TEE face au coût et à la disponibilité.

### Arbitrages issus de `D10` (6)

- `REL_0020` (de `anti-patrons-agentiques` vers `facades-mcp-intention-metier`): Oppose le mappage rapide OpenAPI 1:1 à la conception par intention.
- `REL_0022` (de `anti-patrons-agentiques` vers `taxonomie-acteurs-agentiques`): Proscrit le super-agent universel face aux 5 archétypes spécialisés.
- `REL_0023` (de `anti-patrons-agentiques` vers `topologies-patrons-orchestration`): Condamne la « salle virtuelle » libre au profit de graphes bornés.
- `REL_0268` (de `fabrique-agents-certification-reemission` vers `erreurs-silencieuses-cascade`): Centralisation productive face au risque de point de défaillance unique.
- `REL_0423` (de `plateforme-iap-gitops-cognitif` vers `dette-cognitive-vs-technique`): Immuabilité Git face à l'édition dynamique des prompts.
- `REL_0426` (de `plateformes-saas-et-asymetrie-tiers` vers `noyau-controle-possede-cap`): Fermeture du plan de contrôle SaaS contre gouvernance souveraine.

### Arbitrages issus de `D11` (4)

- `REL_0049` (de `atrophie-competences-humaines` vers `economie-industrialisation-cognitive`): Paradoxe productivité immédiate et érosion de la relève.
- `REL_0051` (de `atrophie-competences-humaines` vers `trajectoires-adaptatives-dapp`): Gain d'automatisation et maintien du vivier humain.
- `REL_0420` (de `pieges-gouvernance` vers `gouvernance-duale-ae-as`): Sur-ingénierie de 2e ligne et prolifération du Shadow AI.
- `REL_0421` (de `pieges-gouvernance` vers `partition-hybride-80-20`): Rigueur du contrôle face à la sur-ingénierie et aux agents fantômes.

### Arbitrages issus de `D12` (2)

- `REL_0109` (de `calibration-feds-ema` vers `trajectoires-adaptatives-dapp`): Optimisation du TCO (Scénario A) face à la robustesse minimax (Scénario B).
- `REL_0480` (de `protocole-wyvern-g0-g5` vers `clause-non-avis-licences`): Exhaustivité automatisée et absence de relecture humaine.

## 6. Chaînes d'atténuation de risque, dépendances techniques et synergies (`D01`–`D12`)

Le graphe compte **81 relations `attenuation_risque`**, **93 relations `dependance_technique`** et **63 relations `amplification_synergie`**, formant l'armature causale entre les vulnérabilités probabilistes des modèles et les garde-fous déterministes de la passerelle d'outils, de la délégation cryptographique et de l'orchestration Saga.

- `REL_0017` (de `alignement-deceptif-red-teaming-adversarial` vers `defense-hors-modele-camel-confinement`): Évaluation adversariale quantifiant les angles morts défensifs.
- `REL_0019` (de `anti-patrons-agentiques` vers `dette-cognitive-vs-technique`): Éradique les 12 modes d'échec structurels en ARB.
- `REL_0027` (de `anti-verrouillage-standards` vers `dette-cognitive-vs-technique`): Remplacement du couplage N×M propriétaire par des standards N+M.
- `REL_0028` (de `anti-verrouillage-standards` vers `fusion-acp-collision-terminologique`): Fondation neutre assurant une sortie ordonnée lors d'une fusion.
- `REL_0029` (de `anti-verrouillage-standards` vers `pieges-gouvernance`): Noyau possédé et réversibilité contre la rente SaaS.
- `REL_0036` (de `approbation-ciba` vers `supervision-hitl-hotl-abstention`): Preuve FIDO2 contre approbation complaisante.
- `REL_0037` (de `approbation-reflexe-biais-automatisation` vers `pieges-gouvernance`): Parade ergonomique et organisationnelle contre l'approbation réflexe.
- `REL_0041` (de `arbre-sobriete-oo1-oo4` vers `pathologies-reactives-backpressure`): Prévient les échecs MAST et l'effet Ringelmann.

- `REL_0061` (de `banc-evalops-hermetique` vers `erreurs-silencieuses-cascade`): Détection pass^k et chaos pré-production.
- `REL_0111` (de `canonicalisation-jcs-rfc8785` vers `signature-agent-card-ancrage`): Canonicalisation RFC 8785 fiabilisant la vérification JWS.
- `REL_0120` (de `choregraphie-event-mesh` vers `erreurs-silencieuses-cascade`): Retient les effets irréversibles via le tampon à fenêtre de grâce.
- `REL_0141` (de `confidentialite-materielle-tee-hyok` vers `six-substrats-etat-souverainete`): Séquestre HYOK, TEE et continuité bimodèle.
- `REL_0143` (de `confinement-cua-patrimoine-sans-api` vers `injection-indirecte-prompt`): Verrouille les zones d'écran et touches destructrices des CUA.
- `REL_0145` (de `confinement-opensandbox-firecracker-wasi` vers `injection-indirecte-prompt`): Confinement microVM anti-exfiltration.
- `REL_0146` (de `confinement-shadi-sandbox` vers `chaine-approvisionnement-agent-skills`): Isole l'exécution des scripts et composants non fiables.
- `REL_0147` (de `confinement-shadi-sandbox` vers `injection-indirecte-prompt`): Confinement matériel sans réseau ni secret.

- `REL_0149` (de `confinement-shadi-sandbox` vers `tool-poisoning-rug-pull`): Isole l'exécution de code arbitraire (ASI05).
- `REL_0153` (de `contrats-donnees-write-audit-publish` vers `dette-semantique-ontologies`): Quarantaine WAP contre dérive silencieuse.
- `REL_0159` (de `couche-anti-corruption-acl` vers `dette-semantique-ontologies`): Exactitude Decimal COMP-3 sans IEEE 754.
- `REL_0160` (de `couche-anti-corruption-acl` vers `encapsulation-patrimoine-it-ot`): Protège la charge et l'intégrité des systèmes d'enregistrement.
- `REL_0161` (de `couche-anti-corruption-acl` vers `erreurs-silencieuses-cascade`): Protège les SoR des rafales et doubles écritures.
- `REL_0172` (de `defense-hors-modele-camel-confinement` vers `injection-indirecte-prompt`): Séparation de privilège hors modèle contre l'injection indirecte.
- `REL_0173` (de `delegation-obo-deux-sauts` vers `anti-patrons-agentiques`): Parade contre l'emprunt et le délégué confus.
- `REL_0174` (de `delegation-obo-deux-sauts` vers `erreurs-silencieuses-cascade`): Atténuation des privilèges à chaque saut et fraîcheur CRL/OCSP.

<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->
## Inventaire intégral des tensions d'arbitrage et degrés nodaux

- `REL_0014`: `agntcy-slim` → `protocole-a2a` — Positionnement officiel d'AGNTCY nuancé par chevauchement tiers sur ACP
- `REL_0018`: `annuaires-commerciaux-risque-standard-de-fait` → `anti-verrouillage-standards` — Adoption immédiate d'annuaires propriétaires par rapport à l'attente de normes neutres
- `REL_0020`: `anti-patrons-agentiques` → `facades-mcp-intention-metier` — Oppose le mappage rapide OpenAPI 1:1 à la conception par intention
- `REL_0022`: `anti-patrons-agentiques` → `taxonomie-acteurs-agentiques` — Proscrit le super-agent universel face aux 5 archétypes spécialisés
- `REL_0023`: `anti-patrons-agentiques` → `topologies-patrons-orchestration` — Condamne la « salle virtuelle » libre au profit de graphes bornés
- `REL_0042`: `arbre-sobriete-oo1-oo4` → `protocole-a2a` — Sobriété agent unique face au surcoût multi-agents (-70 % à +80,8 %)
- `REL_0049`: `atrophie-competences-humaines` → `economie-industrialisation-cognitive` — Paradoxe productivité immédiate et érosion de la relève
- `REL_0051`: `atrophie-competences-humaines` → `trajectoires-adaptatives-dapp` — Gain d'automatisation et maintien du vivier humain
- `REL_0063`: `banc-evalops-hermetique` → `finops-focus-cpo` — Coût de simulation face au risque d'erreur en production
- `REL_0109`: `calibration-feds-ema` → `trajectoires-adaptatives-dapp` — Optimisation du TCO (Scénario A) face à la robustesse minimax (Scénario B)
- `REL_0117`: `certificats-tls-47-jours` → `post-quantique-ml-dsa-slh-dsa` — Collision rotation TLS 47 jours et taille PQC sur passerelles
- `REL_0124`: `choregraphie-event-mesh` → `topologies-patrons-orchestration` — Arbitre l'autonomie événementielle face à la maîtrise transactionnelle
- `REL_0142`: `confinement-cua-patrimoine-sans-api` → `couche-anti-corruption-acl` — Tolère CUA à ≤ 8 % sous bail 12 mois contre refactoring MCP durable
- `REL_0144`: `confinement-opensandbox-firecracker-wasi` → `anti-verrouillage-standards` — Isolation stricte face à la latence et à la complexité KVM
- `REL_0150`: `constance-pass-k` → `finops-focus-cpo` — Arbitre le coût de vérification face à la fiabilité requise
- `REL_0152`: `contrats-api-versionnement-conformite` → `anti-verrouillage-standards` — Paradoxe du verrouillage inverse sur l'interface de fait OpenAI
- `REL_0183`: `dette-semantique-ontologies` → `ecart-accord-protocolaire-comprehension` — Expressivité ontologique coûteuse face à la souplesse fragile en prose
- `REL_0201`: `double-couloir-probatoire-pii` → `observabilite-otel-genai` — Diagnostic complet face à la minimisation Loi 25 et RGPD
- `REL_0215`: `echelle-autonomie-l0-l4` → `supervision-hitl-hotl-abstention` — Montée en autonomie bornée contre capacité cognitive de supervision humaine
- `REL_0218`: `economie-industrialisation-cognitive` → `anti-verrouillage-standards` — Arbitre vitesse des agents SaaS et contrôle architectural
- `REL_0219`: `economie-jetons-routage-slm` → `raisonnement-inference-limites-planification` — Arbitrage coût des jetons de réflexion face au gain de qualité à l'inférence
- `REL_0226`: `efvp-transfert-hors-quebec` → `systems-of-agency` — Souveraineté des données financières face à l'accès aux modèles de pointe
- `REL_0259`: `execution-durable-temporal` → `semantique-effet-idempotence-uetr` — Illusion du rollback logiciel face à l'irréversibilité métier
- `REL_0268`: `fabrique-agents-certification-reemission` → `erreurs-silencieuses-cascade` — Centralisation productive face au risque de point de défaillance unique
- `REL_0282`: `finops-focus-cpo` → `dette-cognitive-vs-technique` — Baisse du prix du jeton face à l'explosion du CPO par relecture
- `REL_0288`: `frameworks-orchestration-entreprise` → `anti-verrouillage-standards` — Frontière commerciale des plateformes managées face à la portabilité ouverte
- `REL_0311`: `hierarchie-preuves-etudes-cas` → `protocole-a2a` — Spécifications stables face à la rareté des preuves en production
- `REL_0320`: `injection-indirecte-prompt` → `constance-pass-k` — Coût d'utilité de la sécurité CaMeL (77 % contre 84 %)
- `REL_0323`: `inventaire-revocation-asymetrie` → `spiffe-spire-attestation` — Durée de vie courte (24 h) comme substitut partiel à la révocation
- `REL_0358`: `maillage-agents-pep-pdp-zero-trust` → `finops-focus-cpo` — Surcoût de latence, complexité et inférence des contrôles par arête
- `REL_0366`: `memoire-coala-4-tiroirs` → `did-vc-passeport-agent` — Apprentissage continu en production face à la validité datée du passeport
- `REL_0398`: `partition-hybride-80-20` → `constance-pass-k` — Compromis coût en jetons / précision / latence (courbe HAL)
- `REL_0404`: `passerelle-mcp-ai-gateway` → `anti-verrouillage-standards` — Portabilité par passerelle de médiation contre plus petit dénominateur commun
- `REL_0420`: `pieges-gouvernance` → `gouvernance-duale-ae-as` — Sur-ingénierie de 2e ligne et prolifération du Shadow AI
- `REL_0421`: `pieges-gouvernance` → `partition-hybride-80-20` — Rigueur du contrôle face à la sur-ingénierie et aux agents fantômes
- `REL_0423`: `plateforme-iap-gitops-cognitif` → `dette-cognitive-vs-technique` — Immuabilité Git face à l'édition dynamique des prompts
- `REL_0426`: `plateformes-saas-et-asymetrie-tiers` → `noyau-controle-possede-cap` — Fermeture du plan de contrôle SaaS contre gouvernance souveraine
- `REL_0438`: `post-quantique-ml-dsa-slh-dsa` → `delegation-obo-deux-sauts` — Poids des signatures ML-DSA face à la limite des en-têtes HTTP 431
- `REL_0439`: `post-quantique-ml-dsa-slh-dsa` → `passerelle-mcp-ai-gateway` — Taille des signatures post-quantiques face aux contraintes réseau
- `REL_0459`: `protocole-a2a` → `journalisation-probatoire-audit` — Découverte ouverte fédérée face à la gouvernance des clés et à l'imputation
- `REL_0460`: `protocole-a2a` → `topologies-patrons-orchestration` — Opacité voulue d'A2A contre exigence d'auditabilité réglementaire
- `REL_0476`: `protocole-mcp` → `protocole-a2a` — Frontière floue entre tâches asynchrones MCP et délégation A2A
- `REL_0480`: `protocole-wyvern-g0-g5` → `clause-non-avis-licences` — Exhaustivité automatisée et absence de relecture humaine
- `REL_0495`: `rag-agentique-contexte` → `injection-indirecte-prompt` — Agrandir la fenêtre dilue l'attention et élargit la surface ASI01
- `REL_0511`: `regle-de-deux-opa` → `supervision-hitl-hotl-abstention` — Accroît le volume d'approbations après contamination
- `REL_0515`: `regle-maillon-plus-eleve` → `profil-groupe-diversifie-m18` — Mutualisation du socle technique face au cloisonnement des filiales
- `REL_0523`: `routage-cognitif-hybride-3-paliers` → `constance-pass-k` — Économie SLM face au risque de baisse de précision et de constance
- `REL_0530`: `saga-compensatoire` → `soc-soar-coupe-circuit` — Arrêt d'urgence et intégrité comptable des sagas en vol
- `REL_0531`: `saga-compensatoire` → `tampon-deterministe-rtr-iso20022` — Interdit la compensation a posteriori sur virements RTR irrévocables
- `REL_0557`: `souverainete-espaces-donnees-tee-hyok` → `finops-focus-cpo` — Souveraineté, HYOK et TEE face au coût et à la disponibilité
- `REL_0560`: `spiffe-spire-attestation` → `did-vc-passeport-agent` — Infrastructure centralisée intra-domaine (SPIFFE) face à la portabilité écosystémique (DID)
- `REL_0568`: `supervision-hitl-hotl-abstention` → `atrophie-competences-humaines` — Automatisation de routine et maintien du discernement et de la relève junior
- `REL_0569`: `supervision-hitl-hotl-abstention` → `criteres-qos-cout-precision-latence` — Oppose latence opérationnelle et exigence d'approbation humaine
- `REL_0570`: `supervision-hitl-hotl-abstention` → `echelle-autonomie-l0-l4` — Vitesse d'autonomie et fatigue d'approbation
- `REL_0571`: `supervision-hitl-hotl-abstention` → `erreurs-silencieuses-cascade` — Charge d'approbation humaine face au biais de complaisance
- `REL_0572`: `supervision-hitl-hotl-abstention` → `loi-25-article-12-1` — Évite l'approbation nominale qui rend la décision automatisée
- `REL_0573`: `supervision-hitl-hotl-abstention` → `matrice-protocoles-exigences-reglementaires` — Paradoxe de l'inversement sur l'intervention humaine
- `REL_0575`: `surcout-multi-agent-debat-mast` → `separation-controleur-executeur-determinisme` — Contexte isolé multi-agents (15×) face au rédacteur unique continu
- `REL_0578`: `systems-of-agency` → `anti-verrouillage-standards` — Déplace le verrouillage vers les plateformes
- `REL_0589`: `topologies-patrons-orchestration` → `finops-focus-cpo` — Arbitre gain F1 réflexif/multi-agents contre explosion de coût 4x–15x
- `REL_0613`: `volant-distillation-dspy-multilora` → `memoire-bi-temporelle-et-purge` — Apprentissage sur traces face au risque de fuite et de biais
- `REL_0615`: `web-agentique-webmcp-webbotauth` → `protocole-ap2` — Oppose l'authentification par origine HTTP à la preuve d'intention signée
- `bsif-e-23`: degré=30 (sortant=22, entrant=8).
- `protocole-mcp`: degré=25 (sortant=11, entrant=14).
- `passerelle-mcp-ai-gateway`: degré=24 (sortant=13, entrant=11).
- `finops-focus-cpo`: degré=24 (sortant=6, entrant=18).
- `exigences-cre-ia-305`: degré=23 (sortant=6, entrant=17).
- `post-quantique-ml-dsa-slh-dsa`: degré=21 (sortant=11, entrant=10).
- `delegation-obo-deux-sauts`: degré=21 (sortant=8, entrant=13).
- `anti-verrouillage-standards`: degré=20 (sortant=7, entrant=13).
- `supervision-hitl-hotl-abstention`: degré=20 (sortant=10, entrant=10).
- `injection-indirecte-prompt`: degré=19 (sortant=4, entrant=15).
- `protocole-a2a`: degré=18 (sortant=6, entrant=12).
- `observabilite-otel-genai`: degré=18 (sortant=12, entrant=6).
- `echelle-autonomie-l0-l4`: degré=17 (sortant=6, entrant=11).
- `eu-ai-act`: degré=17 (sortant=13, entrant=4).
- `erreurs-silencieuses-cascade`: degré=16 (sortant=3, entrant=13).
- `ligne-directrice-amf`: degré=15 (sortant=9, entrant=6).
- `banc-evalops-hermetique`: degré=15 (sortant=7, entrant=8).
- `did-vc-passeport-agent`: degré=15 (sortant=5, entrant=10).
- `execution-durable-temporal`: degré=14 (sortant=7, entrant=7).
- `saga-compensatoire`: degré=14 (sortant=6, entrant=8).
- `scellage-jcs-scitt`: degré=14 (sortant=3, entrant=11).
- `identite-non-humaine-nhi`: degré=14 (sortant=5, entrant=9).
- `soc-soar-coupe-circuit`: degré=14 (sortant=10, entrant=4).
- `spiffe-spire-attestation`: degré=13 (sortant=5, entrant=8).
- `trajectoires-adaptatives-dapp`: degré=13 (sortant=3, entrant=10).
- `couche-anti-corruption-acl`: degré=13 (sortant=6, entrant=7).
- `double-couloir-probatoire-pii`: degré=13 (sortant=6, entrant=7).
- `rag-agentique-contexte`: degré=13 (sortant=8, entrant=5).
- `tool-poisoning-rug-pull`: degré=13 (sortant=2, entrant=11).
- `partition-hybride-80-20`: degré=12 (sortant=5, entrant=7).
- `topologies-patrons-orchestration`: degré=12 (sortant=4, entrant=8).
- `politiques-opa-rego-hors-modele`: degré=12 (sortant=4, entrant=8).
- `dette-semantique-ontologies`: degré=12 (sortant=5, entrant=7).
- `loi-25-article-12-1`: degré=12 (sortant=7, entrant=5).
- `approbation-ciba`: degré=11 (sortant=6, entrant=5).
- `noyau-controle-possede-cap`: degré=11 (sortant=4, entrant=7).
- `constance-pass-k`: degré=11 (sortant=2, entrant=9).
- `iso-iec-42001-nist`: degré=11 (sortant=9, entrant=2).
- `protocole-ap2`: degré=11 (sortant=6, entrant=5).
- `agntcy-slim`: degré=10 (sortant=8, entrant=2).
- `anti-patrons-agentiques`: degré=10 (sortant=5, entrant=5).
- `blueprints-reference-multisectoriels`: degré=10 (sortant=4, entrant=6).
- `protocole-wyvern-g0-g5`: degré=10 (sortant=5, entrant=5).
- `concordance-inter-tomes-div02`: degré=10 (sortant=6, entrant=4).
- `choregraphie-event-mesh`: degré=10 (sortant=5, entrant=5).
- `systems-of-agency`: degré=10 (sortant=4, entrant=6).
- `efvp-transfert-hors-quebec`: degré=10 (sortant=7, entrant=3).
- `gouvernance-duale-ae-as`: degré=9 (sortant=2, entrant=7).
- `memoire-coala-4-tiroirs`: degré=9 (sortant=7, entrant=2).
- `agent-card-decouverte`: degré=8 (sortant=4, entrant=4).
- `dette-cognitive-vs-technique`: degré=8 (sortant=1, entrant=7).
- `cadre-eif-4-couches`: degré=8 (sortant=5, entrant=3).
- `atrophie-competences-humaines`: degré=7 (sortant=3, entrant=4).
- `clause-non-avis-licences`: degré=7 (sortant=4, entrant=3).
- `avis-acvm-11-348`: degré=7 (sortant=6, entrant=1).
- `trajectoire-90j-18m-p1-p3`: degré=7 (sortant=3, entrant=4).
- `fil-rouge-groupe-boreal-bel`: degré=7 (sortant=3, entrant=4).
- `trousse-executable-tome-8`: degré=7 (sortant=4, entrant=3).
- `epinglage-schemas-mcp`: degré=7 (sortant=3, entrant=4).
- `arbre-sobriete-oo1-oo4`: degré=6 (sortant=6, entrant=0).
- `profils-financiers-5-secteurs`: degré=6 (sortant=3, entrant=3).
- `regle-maillon-plus-eleve`: degré=6 (sortant=4, entrant=2).
- `cadre-togaf-archimate-4-plans`: degré=6 (sortant=4, entrant=2).
- `confinement-shadi-sandbox`: degré=6 (sortant=4, entrant=2).
- `encapsulation-patrimoine-it-ot`: degré=6 (sortant=3, entrant=3).
- `regle-de-deux-opa`: degré=6 (sortant=2, entrant=4).
- `registres-gouvernes-trois-modeles`: degré=5 (sortant=0, entrant=5).
- `pieges-gouvernance`: degré=5 (sortant=2, entrant=3).
- `tri-prospectif-peremption-feuilles-route`: degré=5 (sortant=4, entrant=1).
- `regime-preuve-trois-degres-absence`: degré=5 (sortant=3, entrant=2).
- `registre-agents-cycle-de-vie-et-attestations`: degré=5 (sortant=1, entrant=4).
- `fabrique-agents-certification-reemission`: degré=5 (sortant=3, entrant=2).
- `kya-verification-agent-tiers`: degré=5 (sortant=2, entrant=3).
- `routage-cognitif-hybride-3-paliers`: degré=5 (sortant=3, entrant=2).
- `peremption-revalidation-annexe-n`: degré=5 (sortant=4, entrant=1).
- `signature-agent-card-ancrage`: degré=4 (sortant=1, entrant=3).
- `contrats-interfaces-catalogue-entreprise`: degré=4 (sortant=1, entrant=3).
- `clauses-contractuelles-normatives-app`: degré=4 (sortant=0, entrant=4).
- `horizon-2027-2032-tri-prospectif`: degré=4 (sortant=0, entrant=4).
- `certificats-tls-47-jours`: degré=4 (sortant=4, entrant=0).
- `decisions-architecture-adr-001-031`: degré=4 (sortant=1, entrant=3).
- `semantique-effet-idempotence-uetr`: degré=4 (sortant=2, entrant=2).
- `frontiere-capacites-metr-veille`: degré=4 (sortant=3, entrant=1).
- `grille-cinq-questions-identite`: degré=4 (sortant=4, entrant=0).
- `taxonomie-attaques-identite-mandataire-confus`: degré=4 (sortant=1, entrant=3).
- `harnais-deterministe-8-etapes`: degré=4 (sortant=3, entrant=1).
- `maillage-agents-pep-pdp-zero-trust`: degré=4 (sortant=3, entrant=1).
- `reconciliation-inter-volumes-tome1`: degré=4 (sortant=4, entrant=0).
- `volant-distillation-dspy-multilora`: degré=4 (sortant=3, entrant=1).
- `actualisation-novembre-2026-unification-v1-2`: degré=3 (sortant=3, entrant=0).
- `architecture-collection-tome-1-preambule`: degré=3 (sortant=2, entrant=1).
- `cout-non-interop-dette-integration`: degré=3 (sortant=2, entrant=1).
- `plan-inference-routage-carbone`: degré=3 (sortant=1, entrant=2).
- `pont-reglementation-frames-deterministes`: degré=3 (sortant=0, entrant=3).
- `priorites-90-jours-gouvernance`: degré=3 (sortant=2, entrant=1).
- `production-agentique-canadienne-2025-2026`: degré=3 (sortant=1, entrant=2).
- `profil-groupe-diversifie-m18`: degré=3 (sortant=0, entrant=3).
- `vertical-financier-durci`: degré=3 (sortant=0, entrant=3).
- `calibration-feds-ema`: degré=3 (sortant=3, entrant=0).
- `catalogue-31-adr-12-dec`: degré=3 (sortant=1, entrant=2).
- `classes-risque-agents-et-plafonds`: degré=3 (sortant=2, entrant=1).
- `confinement-opensandbox-firecracker-wasi`: degré=3 (sortant=2, entrant=1).
- `crypto-agilite-migration-pqc`: degré=3 (sortant=2, entrant=1).
- `homologation-prr-75-points`: degré=3 (sortant=1, entrant=2).
- `ecart-accord-protocolaire-comprehension`: degré=3 (sortant=1, entrant=2).
- `trajectoire-consolidation-standards-2027-2028`: degré=3 (sortant=1, entrant=2).
- `distinction-agent-flux-ambiant`: degré=3 (sortant=2, entrant=1).
- `memoire-bi-temporelle-et-purge`: degré=3 (sortant=0, entrant=3).
- `modele-maturite-5-niveaux-dimensions`: degré=3 (sortant=1, entrant=2).
- `evaluation-continue-derives`: degré=3 (sortant=1, entrant=2).
- `federation-multi-plateformes-gravite`: degré=3 (sortant=3, entrant=0).
- `feuille-de-route-phases-90-jours-indicateurs`: degré=3 (sortant=2, entrant=1).
- `feuille-route-1er-mai-2027`: degré=3 (sortant=2, entrant=1).
- `maillage-b2b-federe-edc-odrl`: degré=3 (sortant=1, entrant=2).
- `protocole-probatoire-l-plus-statut-f`: degré=3 (sortant=1, entrant=2).
- `iso-20022-lynx-rtr`: degré=3 (sortant=2, entrant=1).
- `journalisation-probatoire-audit`: degré=3 (sortant=2, entrant=1).
- `matrice-protocoles-exigences-reglementaires`: degré=3 (sortant=1, entrant=2).
- `non-compositionnalite-surete-surface-attaques`: degré=3 (sortant=2, entrant=1).
- `modes-echecs-emergents-frontiere`: degré=3 (sortant=0, entrant=3).
- `plateforme-iap-gitops-cognitif`: degré=3 (sortant=3, entrant=0).
- `socle-iam-federe-oauth-fapi`: degré=3 (sortant=2, entrant=1).
- `souverainete-espaces-donnees-tee-hyok`: degré=3 (sortant=3, entrant=0).
- `usine-logicielle-agentic-sdlc`: degré=3 (sortant=3, entrant=0).
- `tampon-deterministe-rtr-iso20022`: degré=2 (sortant=0, entrant=2).
- `defense-hors-modele-camel-confinement`: degré=2 (sortant=1, entrant=1).
- `annuaires-commerciaux-risque-standard-de-fait`: degré=2 (sortant=1, entrant=1).
- `facades-mcp-intention-metier`: degré=2 (sortant=1, entrant=1).
- `criteres-evaluation-fournisseurs-grille`: degré=2 (sortant=1, entrant=1).
- `frameworks-orchestration-entreprise`: degré=2 (sortant=1, entrant=1).
- `pathologies-reactives-backpressure`: degré=2 (sortant=0, entrant=2).
- `architecture-reference-6-couches-2-piliers`: degré=2 (sortant=1, entrant=1).
- `architecture-reference-six-couches-pc1-pc5`: degré=2 (sortant=1, entrant=1).
- `economie-industrialisation-cognitive`: degré=2 (sortant=1, entrant=1).
- `modele-operationnel-hub-and-spoke`: degré=2 (sortant=1, entrant=1).
- `maillage-reglementaire-international`: degré=2 (sortant=1, entrant=1).
- `profil-gestion-patrimoine-m15`: degré=2 (sortant=1, entrant=1).
- `criteres-qos-cout-precision-latence`: degré=2 (sortant=0, entrant=2).
- `clauses-sortie-portabilite-interchangeabilite`: degré=2 (sortant=0, entrant=2).
- `plateformes-saas-et-asymetrie-tiers`: degré=2 (sortant=1, entrant=1).
- `profil-assurance-personnes-m16`: degré=2 (sortant=1, entrant=1).
- `gouvernance-raci-modele-en-etoile`: degré=2 (sortant=1, entrant=1).
- `canonicalisation-jcs-rfc8785`: degré=2 (sortant=1, entrant=1).
- `chaine-approvisionnement-agent-skills`: degré=2 (sortant=1, entrant=1).
- `six-substrats-etat-souverainete`: degré=2 (sortant=0, entrant=2).
- `confinement-cua-patrimoine-sans-api`: degré=2 (sortant=2, entrant=0).
- `contrats-api-versionnement-conformite`: degré=2 (sortant=1, entrant=1).
- `contrats-donnees-write-audit-publish`: degré=2 (sortant=2, entrant=0).
- `sre-autonome-rayon-impact-cedar`: degré=2 (sortant=1, entrant=1).
- `contrats-types-executes-ci-annexe-c`: degré=2 (sortant=2, entrant=0).
- `inventaire-revocation-asymetrie`: degré=2 (sortant=1, entrant=1).
- `referentiel-annexes-protocoles-chronologie`: degré=2 (sortant=1, entrant=1).
- `provenance-artefacts-aibom-5-horloges`: degré=2 (sortant=1, entrant=1).
- `donnees-pretes-agents-odcs-openlineage`: degré=2 (sortant=1, entrant=1).
- `echanges-intentions-contrats-probabilistes`: degré=2 (sortant=2, entrant=0).
- `evaluation-agentique-bancs-capacite`: degré=2 (sortant=1, entrant=1).
- `eclats-sectoriels-extrapoles`: degré=2 (sortant=2, entrant=0).
- `raisonnement-inference-limites-planification`: degré=2 (sortant=0, entrant=2).
- `grille-homologation-et-fiche-agent`: degré=2 (sortant=1, entrant=1).
- `pont-ia-physique-ros2-simplex`: degré=2 (sortant=1, entrant=1).
- `genealogie-eai-soa-fipa-llm`: degré=2 (sortant=2, entrant=0).
- `gouvernance-acces-rag-ancrage`: degré=2 (sortant=2, entrant=0).
- `gouvernance-interne-registre-trois-lignes`: degré=2 (sortant=1, entrant=1).
- `regime-derogations-et-transition-cohorte`: degré=2 (sortant=0, entrant=2).
- `indicateurs-agentops-horizon-tache`: degré=2 (sortant=1, entrant=1).
- `profil-assurance-dommages-m17`: degré=2 (sortant=1, entrant=1).
- `memoire-partagee-concurrence-effacement`: degré=2 (sortant=1, entrant=1).
- `loi-de-lusser`: degré=2 (sortant=1, entrant=1).
- `modele-maturite-feuille-360j`: degré=2 (sortant=1, entrant=1).
- `responsabilite-mandat-contrats-b2b`: degré=2 (sortant=1, entrant=1).
- `profil-banque-m14`: degré=2 (sortant=1, entrant=1).
- `protocole-anp-did-wba`: degré=2 (sortant=1, entrant=1).
- `protocoles-interfaces-agui-a2ui-webrtc`: degré=2 (sortant=1, entrant=1).
- `revue-litterature-mlr-prisma`: degré=2 (sortant=1, entrant=1).
- `reprise-sinistre-cognitif-continuite`: degré=2 (sortant=2, entrant=0).
- `reseaux-b2b-federes-p3`: degré=2 (sortant=1, entrant=1).
- `resilience-orchestration-repli-plafonds`: degré=2 (sortant=1, entrant=1).
- `separation-controleur-executeur-determinisme`: degré=2 (sortant=1, entrant=1).
- `services-bancaires-consommateurs-c15`: degré=2 (sortant=2, entrant=0).
- `web-agentique-webmcp-webbotauth`: degré=2 (sortant=2, entrant=0).
- `adaptateur-mcp-streamable-http-sep-3398`: degré=1 (sortant=1, entrant=0).
- `alignement-deceptif-red-teaming-adversarial`: degré=1 (sortant=1, entrant=0).
- `taxonomie-acteurs-agentiques`: degré=1 (sortant=0, entrant=1).
- `fusion-acp-collision-terminologique`: degré=1 (sortant=0, entrant=1).
- `approbation-reflexe-biais-automatisation`: degré=1 (sortant=1, entrant=0).
- `architecture-outils-fiables-erreurs-actionnables`: degré=1 (sortant=1, entrant=0).
- `formats-echange-registres-schemas`: degré=1 (sortant=0, entrant=1).
- `audit-validation-sources-121-449`: degré=1 (sortant=1, entrant=0).
- `barriere-logicielle-g0-execute-g0`: degré=1 (sortant=1, entrant=0).
- `blueprint-1-assistant-sor`: degré=1 (sortant=1, entrant=0).
- `blueprint-2-enclave-rag-acl`: degré=1 (sortant=1, entrant=0).
- `blueprint-3-maillage-b2b`: degré=1 (sortant=1, entrant=0).
- `cadres-internationaux-imda-aica-g7`: degré=1 (sortant=1, entrant=0).
- `cadriciels-orchestration-portabilite`: degré=1 (sortant=1, entrant=0).
- `canal-compensation-isole-outbox`: degré=1 (sortant=1, entrant=0).
- `canonisation-deterministe-jcs`: degré=1 (sortant=1, entrant=0).
- `caviardage-pii-rp-bilingue`: degré=1 (sortant=1, entrant=0).
- `cinq-blocs-sbb-tableau-12`: degré=1 (sortant=1, entrant=0).
- `cinq-discordances-inter-volumes-tome-8`: degré=1 (sortant=1, entrant=0).
- `clauses-reversibilite-cloud-souverain`: degré=1 (sortant=1, entrant=0).
- `comptabilite-carbone-cap-046-bsif-b15`: degré=1 (sortant=1, entrant=0).
- `confidentialite-materielle-tee-hyok`: degré=1 (sortant=1, entrant=0).
- `controle-surete-stamp-stpa`: degré=1 (sortant=1, entrant=0).
- `couts-transaction-coase`: degré=1 (sortant=1, entrant=0).
- `profil-oauth-9700-et-liaison-expediteur`: degré=1 (sortant=0, entrant=1).
- `dimensionnement-wilson-evalops`: degré=1 (sortant=1, entrant=0).
- `dix-interdictions-exig-gov-17`: degré=1 (sortant=1, entrant=0).
- `dix-theses-t1-t10-tome-5`: degré=1 (sortant=1, entrant=0).
- `douze-principes-directeurs-prin`: degré=1 (sortant=1, entrant=0).
- `droit-effacement-portabilite-loi-25`: degré=1 (sortant=1, entrant=0).
- `echec-ferme-opa-default-deny`: degré=1 (sortant=1, entrant=0).
- `economie-jetons-routage-slm`: degré=1 (sortant=1, entrant=0).
- `enveloppes-bpmn-cas-routine`: degré=1 (sortant=1, entrant=0).
- `ergonomie-aci-anti-swagger`: degré=1 (sortant=1, entrant=0).
- `etat-des-lieux-adoption-map-2027`: degré=1 (sortant=1, entrant=0).
- `approvisionnement-reversible-contrats`: degré=1 (sortant=0, entrant=1).
- `responsabilite-litiges-commerce-agentique`: degré=1 (sortant=0, entrant=1).
- `cycle-vie-operationnel-derives-gitops`: degré=1 (sortant=0, entrant=1).
- `fiabilite-coordination-taxonomie-mast`: degré=1 (sortant=1, entrant=0).
- `gabarit-typst-edition-4542-pages`: degré=1 (sortant=1, entrant=0).
- `glossaire-normatif-tome-2`: degré=1 (sortant=1, entrant=0).
- `grille-evaluation-maturite-n1-n5`: degré=1 (sortant=1, entrant=0).
- `hierarchie-preuves-etudes-cas`: degré=1 (sortant=1, entrant=0).
- `liaison-jetons-dpop-mtls`: degré=1 (sortant=1, entrant=0).
- `maillage-agentique-trois-acceptions`: degré=1 (sortant=1, entrant=0).
- `mediation-b2b-esb-traducteurs`: degré=1 (sortant=1, entrant=0).
- `patrons-boucle-mono-agent-codeact`: degré=1 (sortant=0, entrant=1).
- `metriques-soutien-vs-production`: degré=1 (sortant=1, entrant=0).
- `modele-comme-juge-biais-calibration`: degré=1 (sortant=1, entrant=0).
- `coexistence-bpm-ipaas-rpa`: degré=1 (sortant=0, entrant=1).
- `negociation-b2b-diplomate-evaluateur`: degré=1 (sortant=1, entrant=0).
- `principes-architecture-pri-001-015`: degré=1 (sortant=0, entrant=1).
- `paradigme-apm-autonomie-encadree`: degré=1 (sortant=1, entrant=0).
- `portee-et-force-normative-cre-ia`: degré=1 (sortant=1, entrant=0).
- `passage-echelle-parc-agents`: degré=1 (sortant=0, entrant=1).
- `propagation-acl-memoire-silo`: degré=1 (sortant=1, entrant=0).
- `protocoles-ressources-physiques-lap`: degré=1 (sortant=1, entrant=0).
- `quadruple-dette-agentique`: degré=1 (sortant=1, entrant=0).
- `quinze-portes-homologation-por`: degré=1 (sortant=1, entrant=0).
- `rails-paiement-commerce-agentique`: degré=1 (sortant=1, entrant=0).
- `red-teaming-continu-empoisonnement-memoire`: degré=1 (sortant=1, entrant=0).
- `registre-sources-tracees-annexe-b`: degré=1 (sortant=1, entrant=0).
- `requetes-riches-rar-txn-tokens`: degré=1 (sortant=1, entrant=0).
- `plan-donnees-inference-kv-cache`: degré=1 (sortant=0, entrant=1).
- `sanctuarisation-vivier-junior-reprise`: degré=1 (sortant=1, entrant=0).
- `saturation-http-431-ml-dsa-kid`: degré=1 (sortant=1, entrant=0).
- `separation-controle-donnees-camel`: degré=1 (sortant=1, entrant=0).
- `incidents-agentiques-et-notification-multiregime`: degré=1 (sortant=0, entrant=1).
- `rupture-modele-conversationnel-agent-boucle`: degré=1 (sortant=0, entrant=1).
- `surcout-multi-agent-debat-mast`: degré=1 (sortant=1, entrant=0).
- `synchronisation-edge-crdt`: degré=1 (sortant=1, entrant=0).
- `systeme-qualite-en-18286-dora-cra`: degré=1 (sortant=1, entrant=0).
- `taxonomie-owasp-asi-mcp-maestro`: degré=1 (sortant=1, entrant=0).
- `tests-metamorphiques-fr-en-sans-oracle`: degré=1 (sortant=1, entrant=0).
- `contexte-minimal-delegation-interagents`: degré=1 (sortant=0, entrant=1).
- `marche-ia-agentique-dispersion`: degré=1 (sortant=0, entrant=1).
- `saga-dix-scenarios-fautes`: degré=1 (sortant=0, entrant=1).
- `validation-json-schema-ambigu-escalade`: degré=1 (sortant=1, entrant=0).
- `vide-federal-ia-c27-c36`: degré=1 (sortant=1, entrant=0).
- `vingt-sept-signaux-veille-sig`: degré=1 (sortant=1, entrant=0).
<!-- BIBLIOGRAPHIE_BRUTE_FIN -->
