# Audit d'ancrage atomique Wyvern — Chapitre 07 (`ch07`)

- **Unité auditée** : `manuscrit/03 - Partie III/Chapitre 07 - Identite non humaine et chaine de mandat.md`
- **Dossier fermé de sources** : `sources/ch07-sources.md` (`16` sources `L+`, `SRC-002`, `SRC-005`, `SRC-039`, `SRC-041` à `SRC-053`)
- **Registres vérifiés** : `registre/ancres-chronologiques.json`, `registre/faits-empiriques.json`, `registre/glossaire-termes.json`
- **Date de gel des faits** : 31 décembre 2026
- **Barrière** : `G2` (`CA-10`, `CA-12`, protocole Wyvern `contrat-aq.md` § 2.2)

## Bilan quantifié de l'audit

- **Total d'affirmations atomiques segmentées** : 79 (`C01` à `C79`)
- **Constat initial — supportés** : 58
- **Constat initial — imprécis rectifiés** : 19 (`C06`, `C12`, `C13`, `C23`, `C26`, `C36`, `C39`, `C44`, `C46`, `C49`, `C56`, `C57`, `C58`, `C60`, `C63`, `C64`, `C66`, `C74`, `C76`)
- **Constat initial — non supportés supprimés / réancrés** : 2 (`C72`, `C78`)
- **Verdict final — supportés : 79 (100 %)**
- **Verdict final — imprécis résiduels : 0**
- **Verdict final — non supportés résiduels : 0**

---

## Détail paragraphe par paragraphe et affirmation par affirmation

### Titre et question directrice (L1, L3)

- **C01 (L1, L3)** — L'axe du chapitre porte sur l'établissement cryptographique de l'identité propre d'un agent et du périmètre exact du mandat humain qu'il exécute à travers plusieurs systèmes, en cohérence avec `glossaire-termes.json` (`identité non humaine`, `délégation au nom de`, `crypto-agilité post-quantique`) et les sources `L+` [1–16].
  - Constat initial : supporté.
  - Verdict final : supporté

### Ouverture — Scénario illustratif du délégué confus (L5–L11)

- **C02 (L5)** — Scénario illustratif (cas type de construction architecturale, non présenté comme incident empirique daté) exposant le problème du « délégué confus » (*confused deputy*, documenté dans `SRC-048.txt` § 11, l. 1179) lors d'une délégation d'un assistant vers un agent aval relié aux systèmes centraux.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C03 (L7)** — Modélisation illustrative du compte de service technique partagé à secret statique en variable d'environnement doté de droits de lecture et d'écriture plus larges que ceux du conseiller initial.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C04 (L9)** — Modélisation illustrative d'un détournement d'objectif via consigne dissimulée dans une pièce jointe externe déclenchant une écriture ou un virement accepté sous le jeton statique technique.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C05 (L11)** — Synthèse du scénario posant le vide probatoire du compte générique et les quatre axes de remédiation traités aux sections 7.1 à 7.4 (identité sans secret fixe, délégation cryptographique multi-sauts, verrouillage hors bande, responsabilité juridique inter-organisations).
  - Constat initial : supporté.
  - Verdict final : supporté

---

### Section 7.1 — En finir avec les secrets statiques : attestation d'identité non humaine éphémère des charges de travail

#### Paragraphe L15
- **C06 (L15)** — Tant qu'un agent s'authentifie par clé `API` durable ou compte de service partagé, l'organisation ignore quelle instance agit; le brouillon `IETF WIMSE` *Workload Identity Practices* (30 octobre 2026, `draft-ietf-wimse-workload-identity-practices-08`) rappelle que les secrets statiques exigent un effort manuel périodique ou une automatisation dédiée pour leur rotation (`SRC-047.txt` l. 5, 8, 117–126).
  - Constat initial : imprécis (prêtait à `[10]` l'expression « rotation rarement tenue à jour » absente du texte et confondait l'apport de `[10]` et de `[11]` sur le jeton au porteur non lié; rectifié pour refléter exactement `SRC-047.txt` l. 121–123 et associer `[10, 11]`).
  - Verdict final : supporté
- **C07 (L15)** — Selon `WIMSE AIMS` (2 novembre 2026), les clés statiques constituent des artéfacts au porteur sans liaison cryptographique, difficiles à renouveler opérationnellement et permettant à quiconque les dérobe d'usurper l'identité de la charge (`SRC-047.txt` l. 123; `SRC-048.txt` l. 13, § 7, l. 432–436).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C08 (L15)** — Le brouillon `WIMSE AIMS` qualifie explicitement les clés d'`API` statiques d'anti-patron pour l'identité des agents d'IA (`SRC-048.txt` § 7, l. 432).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L17
- **C09 (L17)** — Comme un modèle de langage traite des contenus externes non fiables, `WIMSE AIMS` édicte que le `LLM` ne doit jamais avoir accès aux justificatifs d'identité de l'agent ni aux secrets d'accès aux outils afin qu'une injection d'invite ne puisse ni les employer ni les divulguer (`SRC-048.txt` § 8, l. 551–555).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C10 (L17)** — L'identité cryptographique appartient exclusivement au code d'exécution encadrant (harnais déterministe, Ch. 04) et reste hors du contexte fourni au modèle (`SRC-048.txt` § 4, Fig. 1, l. 216–272).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L19
- **C11 (L19)** — Chaque agent est traité comme une charge de travail logicielle (*workload*) exécutée dans un domaine de confiance (`SRC-048.txt` § 4, l. 197; § 6, l. 357–370).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C12 (L19)** — `SPIFFE` et `IETF WIMSE` fondent l'identité de charge de travail (*workload/machine identity*, conceptualisée sous le terme *Non-Human Identity*, `NHI`, dans `glossaire-termes.json`) en dissociant deux cycles de vie : un identifiant logique stable (`URI` tel que `spiffe://<domaine-de-confiance>/<identifiant>`) immuable et jamais réattribué après retrait pour préserver l'interprétabilité des journaux d'audit (`SRC-046.txt` l. 27–31; `SRC-048.txt` § 6, l. 357–385; `SRC-047.txt` l. 307).
  - Constat initial : imprécis (l'énoncé initial attribuait directement le sigle `NHI` aux travaux `SPIFFE`/`WIMSE` alors que ceux-ci emploient *workload identity* / *machine identity*; reformulé pour distinguer explicitement la notion du glossaire et la terminologie des spécifications).
  - Verdict final : supporté
- **C13 (L19)** — La plateforme délivre dynamiquement des justificatifs cryptographiques éphémères à expiration rapide : certificats et jetons à clé liée (`X.509-SVID` et `WIT-SVID` dans `SPIFFE`; certificat `WIC` et jeton `WIT` dans `WIMSE`) liant cryptographiquement une paire de clés à l'identifiant, ou jetons porteurs `JWT-SVID` (`SRC-046.txt` l. 47–50; `SRC-048.txt` § 7, l. 395–410).
  - Constat initial : imprécis (incluait `JWT-SVID` parmi les justificatifs liant une clé privée de la charge alors que `SRC-048.txt` l. 401–402 et `SRC-046.txt` l. 49 le définissent comme jeton au porteur; corrigé en distinguant explicitement justificatifs à clé liée et `JWT-SVID` au porteur).
  - Verdict final : supporté

#### Paragraphe L21
- **C14 (L21)** — `SPIFFE` recommande d'isoler dans des domaines de confiance distincts les charges situées dans des régions physiques séparées ou soumises à des régimes de sécurité différents, par exemple entre laboratoire et production (`SRC-046.txt` l. 40–41).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C15 (L21)** — Chaque domaine publie un paquet de confiance (`Trust Bundle`) regroupant certificats d'autorité ou clés publiques fréquemment renouvelés et récupérés auprès de l'`API` locale pour vérifier les `SVID` des pairs (`SRC-046.txt` l. 80–86; `SRC-047.txt` § 4.2, l. 526–533).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C16 (L21)** — Les jetons `JWT-SVID` demeurent des artéfacts au porteur exposés au rejeu s'ils sont interceptés en transit, de sorte que `SPIFFE` conseille de leur préférer des `X.509-SVID` adossés à une preuve par clé privée lorsque l'architecture n'interpose pas de mandataire L7 (`SRC-046.txt` l. 47–50).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphes L23–L27 (attestation dynamique et trois patrons de remise)
- **C17 (L23)** — Pour résoudre le paradoxe de l'amorçage sans secret préalable, la `SPIFFE Workload API` ou le fournisseur d'identité de l'orchestrateur/nuage inspecte hors bande des signaux d'environnement (attributs processus et noyau, métadonnées Kubernetes, enclaves `TEE`, modules `TPM`, provenance logicielle) avant d'émettre les justificatifs (`SRC-046.txt` l. 74–77; `SRC-047.txt` § 4.2, l. 512–519; `SRC-048.txt` § 7–8, l. 418, 459–473).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C18 (L25)** — Le montage sur système de fichiers en mémoire vive permet des mises à jour asynchrones isolées par droits d'accès et espaces de noms, en évitant le stockage persistant exposé aux sauvegardes et en imposant des écritures atomiques (`SRC-047.txt` § 3.1, l. 224–257; § 5.1.2, l. 926–940).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C19 (L26)** — L'`API` locale (socket UNIX de `SPIFFE` ou adresse lien-local `169.254.169.254`) facilite la rotation rapide mais s'expose aux attaques `SSRF`, exigeant en-têtes dédiés, vérification au niveau processus et quotas par appelant (`SRC-047.txt` § 3.2, l. 258–277; § 5.1.3, l. 941–978).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C20 (L27)** — Les variables d'environnement sont explicitement proscrites en production par `WIMSE` dès qu'un autre mécanisme existe, car elles restent figées après démarrage et fuient dans les journaux applicatifs et captures d'erreurs (`SRC-047.txt` § 3.3, l. 280–294; § 5.1.4, l. 980–994).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L29
- **C21 (L29)** — Chaque jeton doit cibler une seule audience (`aud` unique), car réutiliser le même jeton porteur devant une ressource interne et un fournisseur d'identité externe permettrait à ce dernier d'usurper la charge auprès de la plateforme interne (`SRC-047.txt` § 4.2, l. 593–599; § 5.7, l. 1148–1176).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C22 (L29)** — Les émetteurs doivent typer explicitement leurs jetons via l'en-tête JOSE `typ` pour bloquer la confusion inter-protocoles, borner la durée de vie en deçà de celle de l'instance et révoquer ou cesser le renouvellement dès l'arrêt de l'instance (`SRC-047.txt` § 5.2, l. 1031–1041; § 5.4, l. 1081–1091; § 5.5, l. 1100–1115; `SRC-048.txt` § 8, l. 528–536).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L31
- **C23 (L31)** — `AIMS` (§ 8) souligne que l'évaluation de posture à l'émission ne prouve pas que l'environnement reste sain au moment d'une requête ultérieure et identifie deux leviers pour les flux sensibles ou inter-domaines : raccourcir les durées de validité et écouter les flux événementiels pour révoquer ou restreindre les justificatifs dès qu'une dérive survient (`SRC-048.txt` § 8, l. 496–509).
  - Constat initial : imprécis (l'énoncé initial écrivait que l'architecture « doit combiner » ces deux mécanismes en référence à `AIMS § 8`, qui décrit deux approches disponibles; reformulé fidèlement selon `SRC-048.txt` l. 500–509).
  - Verdict final : supporté
- **C24 (L31)** — Le certificat `X.509-SVID` couplé au `mTLS` assure une liaison forte dans un maillage interne, mais perd son intégrité de bout en bout dès qu'un mandataire L7, un répartiteur de charge ou une plateforme sans serveur termine et rouvre la session `TLS` (`SRC-046.txt` l. 49; `SRC-048.txt` § 9.1–9.1.1, l. 574–602).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C25 (L31)** — `AIMS` recommande l'authentification applicative de chaque requête via `WIMSE Proof Tokens` (`WPT`) ou signatures HTTP (`RFC 9421`) associées au jeton `WIT` (`SRC-048.txt` § 9.2–9.2.2, l. 604–662).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L33
- **C26 (L33)** — Les *Baseline Requirements* v2.3.1 (4 octobre 2026) du *CA/Browser Forum*, intégrant le scrutin normatif `Ballot SC-081v3` (`SC081`), ont ramené la durée maximale des certificats `TLS` publics à 200 jours le 15 mars 2026 (`SRC-053.txt` l. 4, 8, 151, 168, 192, 2187; `ch07-sources.md` [16]).
  - Constat initial : imprécis (le qualificatif « contraignant » a été nuancé en « normatif » pour refléter `SRC-053.txt` § 1.1 l. 20 précisant la mise en application via les fournisseurs de logiciels vérificateurs).
  - Verdict final : supporté
- **C27 (L33)** — Cette validité maximale ainsi que la réutilisation des validations de domaine/IP s'abaisseront à 100 jours le 15 mars 2027, puis à 47 jours (réutilisation des validations plafonnée à 10 jours) le 15 mars 2029, exposant à des ruptures de connectivité toute passerelle dépendant d'interventions humaines (`SRC-053.txt` § 4.2.1, l. 1317–1324; § 6.3.2, l. 2189–2200; `ancres-chronologiques.json` `2027-03-15-TLS-100J`, `2029-03-15-TLS-47J`; `ch07-sources.md` [16]).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L35
- **C28 (L35)** — Contrer la menace *harvest now, decrypt later* obéit au théorème de Mosca rappelé dans *NIST IR 8547* (brouillon initial `ipd` de novembre 2024 suivi d'une version finale d'octobre 2026) : la transition doit débuter avant que la durée de confidentialité exigée (`X`) plus le temps de migration (`Y`) ne dépasse le délai d'un ordinateur quantique cryptographiquement pertinent (`Z`), soit `X + Y > Z` (`SRC-051.txt` l. 8–15, 787–796; `SRC-052.txt` l. 193; `ch07-sources.md` [14]).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L37
- **C29 (L37)** — Le *NIST* a normalisé l'encapsulation de clés `ML-KEM` (`FIPS 203`, avec `ML-KEM-768` de catégorie 3 recommandé par défaut) et la signature sur réseaux euclidiens `ML-DSA` (`FIPS 204`) (`SRC-049.txt` l. 2360–2371; `SRC-050.txt` l. 1–5, 29–36).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C30 (L37)** — En janvier 2026, la feuille de route coordonnée non contraignante du *G7 Cyber Expert Group* pour le secteur financier fixe l'horizon cible général de migration post-quantique à 2035 avec priorisation des systèmes critiques sur 2030–2032 (`SRC-052.txt` l. 3–13, 189–198; `ancres-chronologiques.json` `2030-2035-G7-PQC-FINANCE`), en phase avec *NIST IR 8547* (dépréciation des schémas à 112 bits après 2030 et interdiction des signatures et échanges classiques `RSA`, `ECDSA`, `EdDSA`, Diffie-Hellman après 2035, `SRC-051.txt` Tableaux 2 et 4, l. 1249–1266, 1348–1370).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C31 (L37)** — La signature `ML-DSA-65` pèse 3 309 octets et `ML-DSA-87` atteint 4 627 octets (`SRC-050.txt` Table 2, l. 1314–1321), contre 64 octets pour une signature elliptique classique (`FACT-PQC-SIGNATURE-SIZE` dans `faits-empiriques.json`; `ch07-sources.md` [13]), imposant d'intégrer cette expansion de charge et les modes hybrides transitoires dans le dimensionnement dès 2027 (`SRC-051.txt` § 3.2, l. 893–951).
  - Constat initial : supporté.
  - Verdict final : supporté

---

### Section 7.2 — Le problème du deuxième saut : échange de jetons en délégation explicite, réduction de portée et preuve de possession

#### Paragraphe L41
- **C32 (L41)** — Dès qu'un orchestrateur (saut 1) sollicite un agent spécialiste ou un serveur d'outils aval (saut 2), la transmission directe du jeton d'accès initial est condamnée comme anti-patron par `WIMSE AIMS`, exposant à la capture, au rejeu latéral et à l'effacement de l'identité des relais (`SRC-048.txt` § 4, l. 269–272; § 10.6, l. 898–913; § 10.9, l. 1043–1045).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L43
- **C33 (L43)** — `IETF RFC 8693` (*OAuth 2.0 Token Exchange*) distingue devant un `STS` l'*impersonation* (nouveau jeton ne portant que `sub`, rendant l'agent indiscernable de l'utilisateur) de la délégation au nom du mandant (`OBO`, où `subject_token` et `actor_token` produisent un jeton composite préservant `sub` tout en inscrivant le mandataire courant dans `act`) (`SRC-041.txt` § 1.1, l. 173–233; § 2.1, l. 343–364; `SRC-048.txt` § 7, l. 425–427; `glossaire-termes.json` l. 126–129).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L45
- **C34 (L45)** — À travers deux sauts (`A_1` vers `A_2`), le jeton place `A_2` au niveau externe de `act` et imbrique l'objet `act` de `A_1`; la section 4.1 de `RFC 8693` impose à la ressource cible de n'évaluer pour le contrôle d'accès que les revendications de premier niveau et l'`act` externe (les maillons imbriqués servant à l'historique), tandis que `may_act` restreint à l'avance les acteurs autorisés (`SRC-041.txt` § 4.1, l. 709–750; § 4.4, l. 802–848).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L47
- **C35 (L47)** — Les chaînes `scope` d'OAuth 2.0 sont trop grossières pour des interfaces transactionnelles et `RFC 8693` (§ 2.1.1) précise que demander plusieurs portées et plusieurs cibles revient au produit cartésien, exposant au rejet `invalid_target` (`SRC-041.txt` § 2.1.1, l. 387–407; `SRC-042.txt` § 1, l. 95–104).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C36 (L47)** — `IETF RFC 9396` (`RAR`) introduit `authorization_details`, un tableau d'objets `JSON` fortement typés précisant `type`, `locations`, `actions`, `datatypes`, `identifier`, `privileges` et des champs métier tels que la devise, le montant et le compte bénéficiaire (`SRC-042.txt` § 1, Fig. 1–2, § 2, § 2.2, l. 114–202, 301–327).
  - Constat initial : imprécis (mentionnait « le montant maximal » alors que `SRC-042.txt` Fig. 1–2 définit `amount` sans qualificatif maximal; rectifié en « le montant »).
  - Verdict final : supporté

#### Paragraphe L49
- **C37 (L49)** — Coupler `RFC 8693` et `RFC 9396` instaure une réduction stricte de portée (*down-scoping*), le `STS` rejetant toute escalade par `invalid_target` ou `invalid_authorization_details` et `RFC 9396` (§ 7.1) permettant d'enrichir l'objet en réponse lorsque l'utilisateur ou la politique affine un mandat (`SRC-041.txt` § 2.2.2, l. 497–500; `SRC-042.txt` § 5–6, l. 582–610; § 7.1, l. 816–856; `SRC-048.txt` § 10.6, l. 924–932).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C38 (L49)** — Comparer deux structures `authorization_details` arbitraires ne se réduit pas à une égalité syntaxique naïve et exige une évaluation sémantique propre au schéma API, tandis que les requêtes longues et leur intégrité sont protégées via objets signés (`RFC 9101`) et `PAR` (`RFC 9126`) (`SRC-042.txt` § 6.1, l. 621–628; § 11.4, l. 1198–1208; § 12, l. 1237–1245).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L51
- **C39 (L51)** — `WIMSE AIMS` (§ 10.4 et § 10.11) couvre la découverte vérifiable à l'exécution (serveur d'autorisation via `RFC 8414`, serveurs d'autorisation protégeant un outil via `RFC 9728`, métadonnées client via `Client ID Metadata Document`) et l'externalisation des décisions de politique vers l'API *OpenID AuthZEN* (*Authorization API 1.0*) (`SRC-048.txt` § 10.4, l. 813–817; § 10.11, l. 1073–1120).
  - Constat initial : imprécis (évoquait la minimisation des données de § 10.10 sous l'en-tête § 10.4/10.11 et désignait le serveur d'autorisation de `RFC 9728` comme « serveur protecteur »; rectifié).
  - Verdict final : supporté

#### Paragraphe L53
- **C40 (L53)** — Au titre de la vie privée (`RFC 8693` § 6; `AIMS` § 10.10), les déploiements minimisent les revendications transmises — via jetons opaques et introspection `RFC 7662` au besoin — et journalisent identifiant ou condensat au lieu des jetons complets (`SRC-041.txt` § 6, l. 879–882; `SRC-048.txt` § 10.3, l. 778–783; § 10.10, l. 1047–1064).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C41 (L53)** — Entre microservices d'un service composé, `AIMS` (§ 10.6) préconise d'échanger le jeton reçu à la frontière contre un *Transaction Token* à vie brève scellé à l'identifiant et au montant d'une transaction unique (`SRC-048.txt` § 10.6, l. 915–935).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L55
- **C42 (L55)** — Contrairement à un jeton au porteur rejouable après fuite, `IETF RFC 9449` (`DPoP`) verrouille chaque jeton à la clé privée asymétrique de l'agent via un en-tête `DPoP` (`typ: dpop+jwt`) à l'échange `STS`, inscrivant l'empreinte `SHA-256` dans `cnf/jkt` avec `token_type: DPoP` (`SRC-043.txt` § 2, l. 187–199; § 4.2, l. 392–402; § 5, l. 524–578; § 6.1, l. 698–711).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L57
- **C43 (L57)** — Lors de chaque appel aval, l'agent produit une preuve `DPoP` couvrant `htm`, `htu`, `iat`, `jti` et `ath`, la passerelle rejetant tout jeton sans preuve, sur une autre `URI` ou en mode `Bearer` et pouvant imposer `DPoP-Nonce` contre la pré-génération (`SRC-043.txt` § 4.2–4.3, l. 408–514; § 7.1–7.2, l. 844–980; § 8–9, l. 1070–1210; § 11.2, l. 1357–1380).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C44 (L57)** — `RFC 9449` signale deux limites : `DPoP` ne protège ni l'intégrité du corps de requête (assurée par `TLS` ou signatures HTTP `RFC 9421`), ni contre un code malveillant exécuté dans le contexte du client détenteur de la clé, d'où la double exigence de clés non exportables en `TPM`/enclave (contre l'exfiltration) et d'isolation stricte du code d'exécution hors de portée du modèle (`SRC-043.txt` § 11.4, l. 1395–1430; § 11.7, l. 1445–1461; `SRC-048.txt` § 7, l. 416–420; § 9.2.2, l. 650–665).
  - Constat initial : imprécis (présentait le stockage en `TPM`/enclave comme réponse au code malveillant dans le contexte client sans préciser que `RFC 9449 § 11.4` limite la protection des clés non exportables au blocage de l'exfiltration; rectifié).
  - Verdict final : supporté

#### Paragraphe L59
- **C45 (L59)** — `RFC 8693` (§ 2.1) précise que l'échange de jetons est ponctuel et ne propage pas automatiquement la révocation du jeton initial vers les jetons dérivés (`SRC-041.txt` § 2.1, l. 376–385).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C46 (L59)** — Pour combler cet intervalle, `WIMSE AIMS` (§ 8 et § 11) préconise l'abonnement aux flux `OpenID SSF` (`CAEP`, `RISC`, `WISE`) et impose aux destinataires d'invalider immédiatement les jetons en cache et de couper ou restreindre les accès dès réception d'un signal (`SRC-048.txt` § 8, l. 507–509, 532–536; § 11, l. 1134–1150).
  - Constat initial : imprécis (« prescrit l'abonnement » rectifié en « préconise l'abonnement », car `AIMS § 11` utilise `MAY subscribe` pour l'abonnement et `MUST` pour l'exécution des signaux reçus).
  - Verdict final : supporté

#### Figure 13, légende et commentaire (L61, L63, L65)
- **C47 (L61, L63, L65)** — La légende et le commentaire de la figure 13 (Fig-13) synthétisent fidèlement l'enchaînement des briques vérifiées (`SPIFFE`/`WIMSE`, `STS` `RFC 8693`, `OBO` `sub`/`act`, `DPoP` `RFC 9449`, révocation temps réel) entre agents probabilistes et ossature déterministe (`[4, 6, 9, 10, 11]`).
  - Constat initial : supporté.
  - Verdict final : supporté

---

### Section 7.3 — Actes sensibles ou irréversibles : approbation humaine hors bande liée cryptographiquement aux paramètres exacts de la transaction

#### Paragraphe L69
- **C48 (L69)** — Pour les actes critiques (« point pivot » du Ch. 06), `WIMSE AIMS` (§ 10.8) avertit qu'une confirmation interactive obtenue par l'agent au cours d'une tâche ne constitue jamais une autorisation autonome et doit être traduite en un octroi vérifiable délivré par le serveur d'autorisation (`SRC-048.txt` § 10.8, l. 996–1015).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C49 (L69)** — La spécification `A2A` (§ 7.6.1 et § 7.6.4) impose de recevoir les justificatifs hors bande (sauf négociation contraire) et de ne jamais traiter l'état `TASK_STATE_AUTH_REQUIRED` comme autorisant une opération avant obtention et vérification du justificatif explicite (`SRC-039.txt` § 7.6.1, l. 4111; § 7.6.4, l. 4151–4160).
  - Constat initial : imprécis mineur (citait uniquement § 7.6.4 pour une exigence incluant l'obtention hors bande figurant aussi au § 7.6.1; complété).
  - Verdict final : supporté

#### Paragraphe L71
- **C50 (L71)** — `OpenID Connect CIBA Core 1.0` sépare l'appareil de consommation (initiateur sans secret utilisateur) de l'appareil d'authentification personnel du mandant (`SRC-045.txt` § 1–2, l. 114–137; `SRC-048.txt` § 10.8, l. 988–994).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C51 (L71)** — Le client émet un `HTTP POST` au `backchannel_authentication_endpoint` avec exactement un indice (`login_hint_token` signé de préférence, `id_token_hint` ou `login_hint`) et reçoit un `auth_req_id` opaque d'au moins 128 bits (160 bits recommandés) borné par `expires_in` (`SRC-045.txt` § 7–7.3, l. 320–370, 518–524; § 14, l. 912).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L73
- **C52 (L73)** — Les modes `poll`, `ping` et `push` prennent en charge le canal asynchrone; en mode `push`, le jeton d'identité inclut les condensats des jetons transmis ainsi que `auth_req_id` et permet la liaison à l'empreinte `SHA-256` du certificat client initial (`SRC-045.txt` § 5, l. 240–307; § 10.3.1, l. 707).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C53 (L73)** — `binding_message` corrèle visuellement appareil de consommation et appareil d'authentification, `user_code` secret optionnel bloque les notifications non sollicitées, les requêtes signées (`JWT` asymétrique) et le transport natif de `authorization_details` (`RFC 9396`) protègent les paramètres, et `CIBA` (§ 15) évite d'exposer courriel ou téléphone via les identifiants `pairwise` (`id_token_hint`) (`SRC-045.txt` § 7.1–7.1.2, l. 356–425, 474–492; § 15, l. 922–928; `SRC-042.txt` § 3, l. 461).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphes L75–L80 (composition en quatre briques)
- **C54 (L77)** — La brique 1 applique `JCS` (`RFC 8785`) à la charge `authorization_details` (`RFC 9396`), selon les règles de tri lexicographique des clés, format uniforme des primitives et suppression des blancs requises par `A2A` (§ 8.4.1) avant signature (`SRC-039.txt` § 8.4.1, l. 4211–4231; `SRC-042.txt` § 2).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C55 (L78)** — La brique 2 calcule l'empreinte `SHA-256` de la charge canonisée suivant le patron `documentDigests` de l'Annexe A.2 de `RFC 9396`, liant consentement explicite et autorisation aux condensats exacts (`SRC-042.txt` Annexe A.2, l. 1584–1630).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C56 (L79)** — La brique 3 associe le défi `CIBA` à une authentification résistante au hameçonnage (*passkey* ou authentificateur matériel `FIDO`, `SRC-048.txt` § 10.5.1, l. 845; Annexe A, l. 1587), avec mention explicite de transparence architecturale précisant que l'assemblage sur empreinte `SHA-256` compose des briques issues de `[3, 5, 8, 11]`.
  - Constat initial : imprécis mineur (`FIDO2` uniformisé sur `FIDO` pour correspondre exactement à la terminologie de `SRC-048.txt` Annexe A).
  - Verdict final : supporté
- **C57 (L80)** — La brique 4 délivre une autorisation bornée à usage unique (`RFC 8693` § 1.1 / `RFC 9396` + `DPoP` `jti` [4, 5, 6]) et consigne mandat et preuve dans le journal probatoire (consolidé le cas échéant par un reçu `SCITT` `RFC 9943` [7]).
  - Constat initial : imprécis mineur (ajout de `[4]` aux côtés de `[5, 6]` pour l'usage unique).
  - Verdict final : supporté

#### Figure 14, légende et commentaire (L82, L84, L86)
- **C58 (L82, L84, L86)** — La figure 14, sa légende et son commentaire rendent compte de la séparation entre l'agent proposeur et les composants déterministes (`CIBA`, authentificateur `FIDO`, vérification d'empreinte `SHA-256`, échec sûr en cas de divergence) en cohérence avec `[3, 5, 6, 7, 8, 11]`.
  - Constat initial : imprécis mineur (`FIDO2` uniformisé sur `FIDO`).
  - Verdict final : supporté

#### Paragraphe L88
- **C59 (L88)** — `WIMSE AIMS` (§ 10.8) note que `CIBA` repose sur une initiation côté client et nécessite des extensions pour solliciter une approbation au milieu d'une tâche longue (`SRC-048.txt` § 10.8, l. 1017–1021), tandis que le risque d'approbation réflexe (*rubber-stamping*, `glossaire-termes.json`) est traité au chapitre 11.
  - Constat initial : supporté.
  - Verdict final : supporté

#### Tableau comparatif et synthèse (L90–L99)
- **C60 (L90–L97)** — Les trois colonnes et six critères du tableau comparatif (Identité, Lien au mandant, Risque si fuite, Granularité, Révocation, Preuve d'audit) synthétisent fidèlement `[3, 4, 5, 6, 7, 8, 9, 10, 11]`.
  - Constat initial : imprécis (en-tête `FIDO2` corrigé en `FIDO`; « Nul hors contexte » précisé en « Inexploitable hors contexte : clé en enclave... » selon `RFC 9449` § 2 et § 11.4; ligne Révocation complétée par `[4, 6, 8, 11]`).
  - Verdict final : supporté
- **C61 (L99)** — La synthèse du tableau récapitule l'inexploitabilité d'un jeton fui sans clé `DPoP` en enclave (`[6, 11]`) et le blocage de tout acte irréversible sans signature hors bande sur l'empreinte exacte (`[3, 5, 8, 11]`).
  - Constat initial : supporté.
  - Verdict final : supporté

---

### Section 7.4 — Responsabilité du mandant et commerce entre agents d'organisations distinctes : limites des protocoles techniques sans cadre contractuel

#### Paragraphe L103
- **C62 (L103)** — Lorsque des agents franchissent la frontière de l'entreprise (économies d'agents virtuels, Ch. 03), la cryptographie prouve la maîtrise d'une clé ou d'un domaine réseau, jamais la capacité juridique ni l'engagement contractuel d'une personne morale (`SRC-002.txt` l. 1410–1414, 1585–1605; `SRC-005.txt` § 4–4.1, l. 521–565).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L105
- **C63 (L105)** — `A2A` permet de signer une carte `AgentCard` au format `JWS` après `JCS RFC 8785` et d'y déclarer `provider.organization` et `provider.url`, tout en imposant `TLS` en production et la limitation de portée sur les frontières d'autorisation ou de locataires (`tenant`) déclarées (`SRC-039.txt` § 4.4.1–4.4.2, l. 2638–2710; § 8.4, l. 4207–4231; § 13.1, l. 5783–5818; § 13.4, l. 5921), mais ni `TLS` ni `JWKS` n'attestent l'existence légale, l'habilitation ou la solvabilité (`SRC-002.txt`; `SRC-005.txt`).
  - Constat initial : imprécis (« imposant TLS et le cloisonnement multi-locataires » rectifié pour refléter que `A2A § 13.1` impose le cloisonnement selon le modèle d'autorisation propre de l'agent et propose les frontières de locataire comme modèle facultatif `MAY`, et citation `[1, 2, 3]` complétée).
  - Verdict final : supporté
- **C64 (L105)** — Le chaînage inter-domaines dans `WIMSE AIMS` (§ 10.4 et § 10.7) véhicule des revendications entre serveurs d'autorisation tout en rappelant que chaque domaine continue d'évaluer souverainement sa politique locale (`SRC-048.txt` § 10.4, l. 805–811; § 10.7, l. 943–982).
  - Constat initial : imprécis mineur (citation § 10.7 complétée par § 10.4 qui contient littéralement l'énoncé sur l'évaluation souveraine de la politique locale).
  - Verdict final : supporté

#### Paragraphe L107
- **C65 (L107)** — Gillian Hadfield et Andrew Koh (document pour le *NBER Handbook*, septembre 2025) montrent que les marchés reposent sur une infrastructure d'enregistrement légal (état civil, registre des sociétés, capacité à posséder des biens et à ester en justice) absente pour les agents d'IA et révélant les fractures de l'*agency law* (`SRC-005.txt` l. 1–7, § 4–4.1, l. 521–565).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L109
- **C66 (L109)** — En droit classique, la responsabilité du mandant se limite au pouvoir réel ou apparent du mandataire et peu de régimes juridiques imputent la responsabilité d'actes imprévisibles ou hors du contrôle de l'acteur, créant un vide face aux consignes générales (« va gagner un million de dollars ») données aux agents optimisateurs (`SRC-005.txt` l. 27, 564–573).
  - Constat initial : imprécis (contresens de traduction : le manuscrit initial indiquait « exonère rarement les cas d'imprévisibilité totale », à l'inverse exact de `SRC-005.txt` l. 564 « Few legal regimes of accountability impose liability ... for actions that were not foreseeable », et plaçait une paraphrase entre guillemets; contresens corrigé et exemple aligné sur le texte source).
  - Verdict final : supporté
- **C67 (L109)** — Hadfield et Koh rapprochent l'opacité des réseaux neuronaux des contrats incomplets (écart d'alignement faute de pouvoir spécifier toute situation future dans la récompense) et relèvent le risque systémique d'erreurs corrélées lorsque le même agent est répliqué entre entreprises, à l'image du *Flash Crash* de 2010 (`SRC-005.txt` § 1.1, l. 56–75; § 2.1, l. 149–154; § 3.4, l. 506–513).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L111
- **C68 (L111)** — Deux voies institutionnelles s'esquissent : enregistrer tout agent contractant au nom d'une personne physique ou morale responsable (au prix de tensions sur les incitations des concepteurs), ou calquer l'émergence de la société par actions (*corporation*) en dotant l'agent d'une personnalité juridique autonome et d'actifs saisissables (`SRC-005.txt` § 4.1, l. 561–584).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C69 (L111)** — Dans les secteurs régulés (finance, droit, infrastructures critiques), Hadfield et Koh anticipent des équivalents numériques de l'agrément professionnel (*occupational licensing* sur protocoles et plateformes approuvés) et la conception de registres de réputation impossibles à effacer ou falsifier (`SRC-005.txt` § 4.1–4.2, l. 585–617).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L113
- **C70 (L113)** — Nenad Tomašev et al. (prépublication Google DeepMind, septembre 2025) soulignent que `MCP` et `A2A` sont nécessaires mais insuffisants sans couche d'authentification, de facturation, de régulation et de résolution des différends (`SRC-002.txt` l. 1–4, 69, 1390–1414, 1585–1605, 1688).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C71 (L113)** — Ils proposent d'associer des triangles de confiance de *Verifiable Credentials* (`VCs`) et des `DIDs` (`did:key` éphémères vs `did:ion` persistants pour agents corporatifs ou étatiques), complétés aux points de perméabilité par une *Proof-of-Personhood* anti-Sybil et des cadres législatifs pouvant interdire les transactions avec des agents non vérifiés ou non enregistrés (`SRC-002.txt` l. 1320–1366, 1435–1478, 1522–1538).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L115
- **C72 (L115)** — L'exigence d'attestation organisationnelle s'ancre directement sur les `VCs` et `did:ion` corporatifs analysés par Tomašev et al. [1] et sur l'enregistrement légal d'une personne morale responsable démontré par Hadfield et Koh [2], imposant à la passerelle d'exiger avant négociation `A2A` externe une attestation vérifiable au-delà des champs déclaratifs `provider` de l'`AgentCard` (`SRC-002.txt`; `SRC-005.txt`; `SRC-039.txt`).
  - Constat initial : non supporté (le paragraphe initial contenait une affirmation descriptive sur `vLEI` et les registres `GLEIF`, entièrement absents des 16 sources `L+` et des registres du dépôt; mention `vLEI`/`GLEIF` supprimée et paragraphe réancré exclusivement sur `[1, 2, 3]`).
  - Verdict final : supporté

#### Paragraphe L117
- **C73 (L117)** — Tomašev et al. recensent sept origines possibles de faute d'un agent (modèle, harnais, données d'entrée, requête humaine malveillante, attaque par un autre agent, désalignement dynamique, garde-fous défaillants) et proposent une surveillance hybride à trois étages (détection IA temps réel, blocage conservatoire automatisé, arbitrage humain expert) appuyée sur des journaux cryptographiques immuables (`SRC-002.txt` l. 1630–1691).
  - Constat initial : supporté.
  - Verdict final : supporté

#### Paragraphe L119
- **C74 (L119)** — `IETF RFC 9943` (`SCITT`, juin 2026) consigne chaque énoncé signé (`COSE_Sign1` — incluant la signature du condensat seul d'un énoncé sensible selon § 6.2) validé selon une politique d'inscription transparente et vérifiable (`Registration Policy`) auprès d'un service de transparence en ajout seul délivrant un reçu `COSE` vérifiable sans équivocation (`SRC-044.txt` § 1, § 3, § 5.1.1–5.1.3, § 6.2, l. 104–146, 484–505, 724–821, 999–1003).
  - Constat initial : imprécis (« politique d'inscription publique » rectifié en « transparente et vérifiable », conforme à `SRC-044.txt` § 5.1.1 l. 768 *Transparent and available to all Relying Parties*).
  - Verdict final : supporté
- **C75 (L119)** — La section 9.2 de `RFC 9943` rappelle que l'enregistrement prouve *qui* a signé un énoncé et *à quel moment* (§ 7), mais jamais que l'énoncé est exact (`SRC-044.txt` § 7, l. 1131; § 9.2, l. 1308–1317), la technique rendant la preuve causale praticable sans créer le droit en l'absence de convention (`SRC-002.txt` l. 1684–1690; `SRC-005.txt` § 4).
  - Constat initial : supporté.
  - Verdict final : supporté

---

### Encadré « Trois arbitrages sans regret — Chapitre 07 » (L121–L125) et Transition (L127)

- **C76 (L123)** — Arbitrage 1 : déployer une identité `SPIFFE`/`WIMSE` éphémère à audience unique et durée brève sans variables d'environnement ni accès du modèle aux secrets (`[9, 10, 11]`), automatiser le cycle `PKI` face aux échéances du 15 mars 2027 (100 jours) et du 15 mars 2029 (47 jours) (`[16]`) et préparer la crypto-agilité post-quantique pour 2030–2035 (`[12, 13, 14, 15]`).
  - Constat initial : imprécis mineur (ajout de `[12]` pour `ML-KEM` à la liste de références).
  - Verdict final : supporté
- **C77 (L124)** — Arbitrage 2 : proscrire la retransmission de jetons porteurs au profit de l'échange `RFC 8693` (`OBO` `sub` + `act`), `RFC 9396` (`RAR`), `DPoP` (`RFC 9449`) et des signaux temps réel `SSF`/`CAEP` (`[4, 5, 6, 11]`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C78 (L125)** — Arbitrage 3 : convertir toute approbation sensible en flux `CIBA` authentifié par clé résistante au hameçonnage (`FIDO` / *passkey*) sur l'empreinte canonique `JCS` (`RFC 8785`) `SHA-256` (`[3, 5, 8, 11]`) et n'accepter hors de l'entreprise d'échange `A2A` transactionnel qu'avec attestation organisationnelle vérifiable (`VC` et identifiant corporatif rattachés à une personne morale enregistrée) et convention expresse de responsabilité (`[1, 2, 3, 7]`).
  - Constat initial : non supporté (contenait la référence non ancrée « de la famille des justificatifs de type `vLEI` »; supprimée et réancrée sur `VC` et identifiant corporatif `[1, 2]`).
  - Verdict final : supporté
- **C79 (L127)** — Transition vers le chapitre 08 : même muni d'une identité `SPIFFE`, d'une preuve `DPoP` et d'un jeton `OBO` borné, un modèle peut encore être détourné par injection indirecte ou outil piégé (objet du Ch. 08 sur la séparation par construction entre contrôle et données, `glossaire-termes.json` et `FACT-CAMEL-AGENTDOJO` dans `faits-empiriques.json`).
  - Constat initial : supporté.
  - Verdict final : supporté

---

## Contrôle différentiel post-G4

- **Objet** : Audit `G2` différentiel consécutif à la retouche stylistique `G4` du chapitre 07 (extraction des paramètres protocolaires `CIBA` dans l'encadré `L101–L105`, reformulation de `L71–L73`, révision de `L37` et `L129`, vérification associée de `L77–L80` pour `RFC 8785` / `FIDO` / `SHA-256`).
- **Référentiel primaire vérifié** : `SRC-039.txt` (`A2A`), `SRC-041.txt` (`RFC 8693`), `SRC-042.txt` (`RFC 9396`), `SRC-043.txt` (`RFC 9449`), `SRC-044.txt` (`RFC 9943`), `SRC-045.txt` (`CIBA` Core 1.0), `SRC-046.txt` (`SPIFFE`), `SRC-047.txt` (`WIMSE WIP-08`), `SRC-048.txt` (`WIMSE AIMS-01`), `SRC-049.txt` (`FIPS 203`), `SRC-050.txt` (`FIPS 204`), `SRC-051.txt` (`NIST IR 8547`), `SRC-052.txt` (`G7 CEG`), `SRC-053.txt` (`CABF BR`).
- **Correspondance d'indexation post-G4** : L'insertion de l'encadré `L101–L105` décale de `+6` lignes la numérotation aval (`L107–L133` actuelles correspondent aux blocs `C62–C79` précédemment indexés `L101–L127`, au texte inchangé).

### Bilan différentiel post-G4

- **Segments différentiels vérifiés** : `L37`, `L71–L73`, `L77–L80`, `L101–L105`, `L129` (et intégrité des sections `L107–L133`)
- **Écarts / imprécisions post-G4 détectés et rectifiés** : 5 (`L71`, `L73`, `L77`, `L103`, `L105`)
- **Taux d'ancrage certifié post-G4** : **100 % `supporté`**
- **Imprécis résiduel** : **0**
- **Non supporté résiduel** : **0**

### Détail des vérifications et rectifications différentielles

- **L37 (`C29–C31`)** — Conforme sans écart : `ML-KEM` (`FIPS 203`, `ML-KEM-768` catégorie 3 recommandé par défaut, `SRC-049.txt` l. 2360–2371), `ML-DSA` (`FIPS 204`, `SRC-050.txt` l. 1–5, 29–38; `ML-DSA-65` = 3 309 octets, `ML-DSA-87` = 4 627 octets, `Table 2` l. 1314–1321, vs 64 octets elliptique classique selon `ch07-sources.md` [13]), feuille de route `G7 CEG` janvier 2026 non contraignante (cible 2035, systèmes critiques 2030–2032, `SRC-052.txt` l. 3–13, 187–198), *NIST IR 8547* (dépréciation 112 bits après 2030, interdiction `RSA`/`ECDSA`/`EdDSA`/Diffie-Hellman après 2035, modes hybrides transitoires, `SRC-051.txt` § 3.2 l. 893–951, Tables 2 & 4 l. 1249–1266, 1348–1370).
  - Verdict post-G4 : **supporté**
- **L71 (ex-`C50–C51`, versant narratif)** — Imprécision terminologique rectifiée : « un jeton de suivi opaque » remplacé par « un identifiant de suivi opaque » afin de refléter exactement `auth_req_id` (`unique identifier ... MUST be treated as opaque`, `SRC-045.txt` § 3 l. 144, § 7.3 l. 518–520) et d'éviter toute confusion avec les jetons d'accès ou d'identité ainsi qu'avec `L103`. Frontière *Consumption Device* / *Authentication Device* sans secret utilisateur exposée fidèlement (`SRC-045.txt` § 1–2 l. 114–137, § 8 l. 554; `SRC-048.txt` § 10.8 l. 988–994).
  - Verdict post-G4 : **supporté** (après rectification)
- **L73 (ex-`C52–C53`, versant narratif)** — Deux imprécisions introduites en `G4` rectifiées :
  1. En mode `push`, c'est le fournisseur d'identité (`OP`, `SRC-045.txt` § 5 l. 306 : `OPs ... should keep some record of the key material ... and bind the tokens`) — et non l'automate durable côté client — qui peut préserver la liaison des jetons émis au matériel cryptographique du client initial.
  2. La précision et l'intégrité des paramètres résultent de l'encapsulation des autorisations granulaires `RFC 9396` (`SRC-042.txt` § 3 l. 461, § 12 l. 1239–1245) au sein de requêtes `CIBA` signées asymétriquement (`SRC-045.txt` § 7.1.1 l. 396–398), et non d'une garantie d'intégrité intrinsèque du transport `RFC 9396`. `binding_message`, `user_code` et les identifiants pseudonymes par secteur (`pairwise`, `SRC-045.txt` § 4 l. 200–218, § 15 l. 922–928) sont conformes.
  - Verdict post-G4 : **supporté** (après rectification)
- **L77–L80 (`C54–C57`)** — Imprécision rectifiée à `L77` : « avant toute signature d'objet `JSON` » précisé en « avant la signature d'une carte `AgentCard` en `JSON` » (`SRC-039.txt` § 8.4.1 l. 4211–4231 porte spécifiquement sur `AgentCard`). `L78` (`SHA-256` / `documentDigests`, `SRC-042.txt` Annexe A.2 l. 1584–1630, OID `2.16.840.1.101.3.4.2.1`), `L79` (`CIBA` + `FIDO` / *passkey*, `SRC-048.txt` § 10.5.1 l. 845, Annexe A l. 1587, note de transparence architecturale conservée) et `L80` (`RFC 8693` / `RFC 9396` + `DPoP` + `SCITT` `RFC 9943`) conformes.
  - Verdict post-G4 : **supporté** (après rectification)
- **L101–L105 (nouvel encadré « Paramètres protocolaires de l'approbation hors bande »)** — Trois écarts / imprécisions rectifiés :
  1. `L103` : précision ajoutée « d'au moins 128 bits d'entropie (160 bits recommandés) » conformément à `SRC-045.txt` § 7.3 l. 520 (`sufficient entropy (a minimum of 128 bits while 160 bits is recommended)`). Tous les noms de champs (`HTTP POST`, `backchannel_authentication_endpoint`, `login_hint_token` signé de préférence § 14 l. 912, `id_token_hint` `pairwise` § 15 l. 928, `login_hint`, unicité d'indice § 7.1 l. 368, `auth_req_id`, `expires_in`) sont vérifiés exacts.
  2. `L105` (attribution `push` / `SHA-256`) : formulation corrigée pour dissocier le rôle du jeton d'identité en mode `push` — qui inclut les condensats des jetons transmis (`at_hash`, `rt_hash` le cas échéant) ainsi que `auth_req_id` (`SRC-045.txt` § 10.3.1 l. 707) — de celui du fournisseur d'identité, qui peut lier les jetons émis au matériel cryptographique présenté à l'initiation (par ex. l'empreinte `SHA-256` du certificat client initial, `SRC-045.txt` § 5 l. 306).
  3. `L105` (optionalité `JWT` / `binding_message` et statut de `authorization_details`) : reformulation explicite indiquant que l'encapsulation en `JWT` signé asymétriquement (`CIBA` § 7.1.1) et `binding_message` (§ 7.1 l. 356) sont optionnels (tout comme `user_code` § 7.1.2), et que le `JWT` signé est apte à transporter `authorization_details` tel que prévu pour `CIBA` par `RFC 9396` (§ 3 l. 461, `SRC-042.txt`), sans prêter à `CIBA` Core 1.0 une prise en charge « native » antérieure à la `RFC 9396`.
  - Verdict post-G4 : **supporté** (après rectification)
- **L129 (ex-`L123`, `C76`)** — Conforme sans écart : `SPIFFE` / `WIMSE`, attestation de plateforme, audience unique (`SRC-047.txt` § 5.7 l. 1148–1176), durée brève (§ 5.4 l. 1081–1091), proscription des variables d'environnement (§ 3.3 l. 290–292, § 5.1.4 l. 992–994), interdiction d'accès du modèle aux secrets (`SRC-048.txt` § 8 l. 551–555), échéances `PKI` du 15 mars 2027 (100 jours) et du 15 mars 2029 (47 jours) (`SRC-053.txt` § 6.3.2 l. 2189–2200), crypto-agilité post-quantique 2030–2035 (`SRC-049..052`).
  - Verdict post-G4 : **supporté**

---

## Contrôle différentiel post-lissage G5

- **Périmètre inspecté** : intégralité du `git diff HEAD` (depuis le commit `fe6e945`) sur [Chapitre 07 - Identite non humaine et chaine de mandat.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/manuscrit/03%20-%20Partie%20III/Chapitre%2007%20-%20Identite%20non%20humaine%20et%20chaine%20de%20mandat.md) — **59** items contrôlés (`10` lignes à simple retrait de rétro-apostrophes et `49` lignes/paragraphes comportant des retouches rédactionnelles), vérifiés contre `sources/ch07-sources.md` (`[1]`–`[16]`), `corpus_l_plus/*.txt`, les registres et `verifie_manuscrit.py --unit ch07 --strict`.
- **Rectifications appliquées** (`14` paragraphes ajustés) : `L19` (distinction explicite entre le terme *NHI* du livre et *workload/machine identity* de `SPIFFE`/`WIMSE` + « lient cryptographiquement »), `L29` (« révoquer ou cesser le renouvellement » selon `WIMSE WIP-08` § 5.5), `L31` (« deux leviers s'offrent » au lieu d'une injonction obligatoire, corrigeant une régression sur `C23` / `AIMS` § 8), `L35` (« durée de confidentialité exigée » dans le théorème de Mosca `NIST IR 8547`), `L37` (« vise 2035 comme cible générale » selon `G7 CEG`), `L43` (« l'identité du mandataire »), `L51` (modalité facultative `peut découvrir ... repérer ... exposer ... peuvent interroger` conforme à `AIMS` §§ 10.4, 10.11), `L57` (« dans le contexte même du client » et « contre l'exfiltration » pour `TPM`/enclave selon `RFC 9449` § 11.4, corrigeant une régression sur `C44`), `L59` (« coupure ou restriction des accès » selon `AIMS` § 11), `L79` (« authentificateur matériel FIDO »), `L105` (liaison au matériel présenté par le client à l'initiation selon `CIBA` § 5), `L111` (« frontières d'autorisation ou de locataires » corrigeant une régression critique sur `A2A` § 13.1 / `C63`), `L119` (« attestation cryptographique vérifiable »), `L123` (« politique d'inscription transparente et vérifiable » selon `RFC 9943` § 5.1.1, corrigeant une régression sur `C74`).
- **Taux d'ancrage certifié post-G5** : **100 % `supporté`**
- **Imprécis résiduel** : **0**
- **Non supporté résiduel** : **0**

---

## Contrôle différentiel post-recollation G3 (`seed=202702`, `CA-14`)

- **Objet** : Micro-rectification à `L111` (`ch07:P041:S03`, anciennement `C64`) identifiée lors de la recollation indépendante à froid `G3` passe 2 (`seed=202702`).
- **Écart détecté** : L'énoncé attribuait à `WIMSE AIMS` (`SRC-048.txt` [11], § 10.4 et § 10.7) l'affirmation « sans cadre contractuel commun [11] », alors que `SRC-048.txt` (§ 10.4, l. 808–811) énonce *« Each domain continues to evaluate its own policy against the tokens it receives. A common policy language is therefore not required for the mechanisms in this document to interoperate across trust domains »* (absence de **langage de politique commun**, le terme *contract* étant absent de `SRC-048.txt`).
- **Rectification appliquée (`L111`)** : « sans cadre contractuel commun [11]. » remplacé par « sans exiger de langage de politique commun [11], laissant entière l'absence de cadre contractuel inter-organisations. » (`[11]` préservé sans modification des tableaux ni de la numérotation).
- **Verdict post-G3 (`L111`)** : **supporté**
- **Imprécis résiduel** : **0**
- **Non supporté résiduel** : **0**

