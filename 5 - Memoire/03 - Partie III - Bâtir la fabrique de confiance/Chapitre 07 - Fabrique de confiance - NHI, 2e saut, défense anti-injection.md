# Chapitre 7 — Fabrique de confiance : NHI, 2e saut, défense anti-injection et transition PKI / post-quantique

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 14, 16–21, Ann. N]` · `[CAD26 ch. 9, Ann. H | EXIG-IAM-01..21, EXIG-SEC-01..26 | PRIN-03, PRIN-07]` · `[C27 ch. 29–32, 49 | ADR-018..020]` · `[PD28 M-5 | PRI-004, PRI-005, PRI-012 | CAP-030, CAP-035..040 | DEC-009, DEC-012 | POR-003, POR-007, POR-011]`.

*Question directrice : Comment bâtir une chaîne d’identité, de délégation, de confinement et de preuve cryptographique qui survive aux injections d’invite, aux attaques multi-sauts, aux certificats de 47 jours et à l’échéance post-quantique ?*

**Thèse du chapitre :** En novembre 2026, aucun standard n’offre de passeport d’agent complet (`0/15` réponses pleines à `Q-A..Q-E` `[S]` et `0/9` propositions `KYA` ratifiées). L’institution réglementée bâtit donc sa fabrique interne à confiance zéro P : PRI-004 P : PRI-005 E : EXIG-IAM-01. Elle impose des identités non humaines courtes sans secret statique E : EXIG-IAM-03 E : EXIG-IAM-05 et des jetons atténués liés à l’expéditeur contre la rupture du deuxième saut P : CAP-036 E : EXIG-IAM-08 E : EXIG-IAM-14. Elle couple retrait déterministe des outils sortants, isolation de flux et microVM fermées P : CAP-030 P : CAP-038 E : EXIG-SEC-06 E : EXIG-SEC-07 E : EXIG-SEC-08. Enfin, son agilité cryptographique devance les certificats de 47 jours et l’amplification post-quantique P : PRI-012 P : CAP-040 P : POR-007.

## 7.1 Diagnostic identitaire (`Q-A` à `Q-E`, `KYA`) et identités non humaines (`NHI`)

La sécurité périmétrique cède devant un agent qui lit du texte non fiable, mute des systèmes et délègue. `C26 ch. 14` évalue les mécanismes existants sur cinq questions (`[S]`) : `Q-A` (*qui es-tu ?*), `Q-B` (*qui t’a créé ?*), `Q-C` (*pour qui agis-tu ?*), `Q-D` (*que peux-tu faire ?*) et `Q-E` (*qui en répond ?*). Sur quinze cases croisant cartes `A2A`, annuaires commerciaux et registres gouvernés (tel `CSA Agent Registry`, 27 mars 2026), la grille relève `0/15` **réponses pleines**. Elle recense `0` « répond », `1` « ne répond pas », `7` « partiellement » et `7` cases muettes de degré 3 (`C26 § 14.2`, pp. 165, 485).

Trois vides normatifs l’expliquent. D’abord, le **passeport d’agent unifié** reste absent des normes (`C26 ch. 16`) : `SCIM Core Schema § 4` ignore les agents (`S-074`), `W3C VC 2.1` (`S-126`, actualisé le 22 oct. 2026 en `C26 Annexe N.2`, p. 663) et `DID v1.1` (`S-128`) manquent de profil agentique, et `IETF WIMSE` compte huit brouillons pour **zéro RFC** (`C26 Annexe N.2`, p. 663). Ensuite, les **neuf chantiers** `KYA` **de six organisations** (`W3C`, `OpenID Foundation`, `DIF`, `IETF`, `NIST`, `Akamai`) affichent `0/9` **textes ratifiés** (`C26 § 18.1`, Tableau 18.1, sous `S-096`), la charte `AIIM` excluant la normalisation mondiale (`S-094`). Enfin, la révocation sélective en cascade reste au degré 3 (`C26 § 20.6`, brouillons `draft-chen-oauth-agent-revocation-01` et `draft-sweeney-wimse-credential-delegation-02`).

L’institution gouverne donc l’**identité non humaine (**`NHI`**)** dans son noyau possédé P : PRI-004 P : CAP-035 E : PRIN-03 E : EXIG-IAM-01 E : EXIG-IAM-02. Toute confiance implicite est bannie (`EXIG-IAM-01`) au profit d’une autorisation explicite par requête (`EXIG-IAM-02`). Chaque agent reçoit une identité propre rattachée dans le système RH à un parrain actif et isolée entre mandants, locataires ou environnements (`ADR-025`, `OWASP NHI8, NHI9`) E : EXIG-IAM-03. Emprunter un compte humain est interdit sans dérogation (`EXIG-IAM-09`, `EXIG-GOV-17`) et échoue en pratique. En effet, `S-103` (Vol. III `F-57`, `C26 § 20.9` p. 234) montre son incompatibilité avec l’élévation juste-à-temps (`PIM`) et le laissez-passer temporaire (`TAP`) en arrière-plan continu.

L’identité repose sur un justificatif court lié à l’instance : certificat `SPIFFE` `X.509-SVID` (préféré au `JWT-SVID` rejouable ; durée bornée sous `EXIG-IAM-15`, `DEVRAIT`) ou fédération `OIDC` infonuagique E : EXIG-IAM-04 E : EXIG-IAM-15. Deux verrous parent les fuites (`OWASP NHI2, NHI7`) : **zéro secret statique** dans le code, les invites ou l’environnement E : EXIG-IAM-05, et **justificatifs hors de portée du modèle**, injectés au transport par la passerelle (`EXIG-IAM-19`, `DEVRAIT`) hors contexte et traces E : EXIG-IAM-06 E : EXIG-IAM-19. Au retrait, l’identifiant n’est jamais réattribué (`C27 § 29.2`) et la révocation préserve l’identité dédiée aux compensations Saga E : EXIG-IAM-07 E : EXIG-ORC-28.

## 7.2 Rupture au deuxième saut (`RFC 8693 § 4.1`), délégation atténuée et révocation

Relayer le jeton d’une personne (`Q-C`) transforme l’agent aval en **délégué confus** (*confused deputy*, `C26 S-070`, `OWASP ASI03`). Même l’échange `OAuth 2.0` (`RFC 8693`) bute sur le **problème du deuxième saut** (`C26 § 17.6`, `S-093`) : selon `RFC 8693 § 4.1`, la revendication `act` (*actor*) est purement informative pour le contrôle d’accès et ne réduit aucun privilège, laissant la cible aval incapable de vérifier seule l’atténuation des droits ou l’émetteur immédiat.

> **[Figure]**
> - Chaîne multi-sauts, choc PKI / ML-DSA et double couloir d’audit RFC 8693 + DPoP/mTLS, parades HTTP 431 (kid, SCITT) et OTel vs audit JCS
> - 1. Délégation atténuée ≤ 2 sauts (EXIG-IAM-08..16, CAEP ≤ 15 min)
> - 1. Mandant humain
> - Session auth. · sub initial
> - Anti-détournement PIM
> - 2. Agent A (Saut 1)
> - SPIFFE SVID + RFC 8693 #1
> - aud=B + DPoP / mTLS
> - 3. Agent B (Saut 2 max)
> - sub gardé + act empilé
> - Portées ⊆ #1 + RAR
> - 4. Cible via PEP
> - Vérifie aud & preuve cnf
> - Prof. ≤ 2 · zéro relais
> - 2a. Choc PKI 47 j & ML-DSA
> - TLS : 100 j → 47 j (2029)
> - ML-DSA : 3,3–4,6 Ko (72×)
> - 3 sauts = 20 à 35 Ko
> - Rejet HTTP 431 (8–16 Ko)
> - PQC G7 : 2030–2035 [A]
> - 2b. Parades P1–P2 (CAP-040)
> - (1) Clés par réf. kid / JWKS
> - & passerelles ≥ 32 Ko
> - (2) Transaction Tokens & COSE
> - (3) TLS 1.3 hybride + ACME
> - (4) Merkle SCITT · SLH-DSA
> - 3a. OTel Couloir 1 · Opérationnel
> - v1.41.0 épinglé · zéro contenu brut (OBS-07) · SHA-256 poivré
> - 3b. Couloir 2 · Débogage / forensique
> - « Bris de glace » double accord · purge ≤ 14 j (OBS-08) · art. 12.1 ≥ 1 an
> - 3c. Journal d’audit probatoire JCS
> - 5 champs RFC 8785 avant relais P2/P3 · ancré/h · ≥ 24 m (RPRP)

*Fig. 7. – Chaîne de confiance multi-sauts, parades au choc PKI / ML-DSA et double couloir d’audit (pseudonymisation sous table séparée du responsable de la protection des renseignements personnels, RPRP).*

Sans attendre les brouillons `IETF` ouverts (`WIMSE`, `OAuth 2.1 draft -17` expirant le 4 mai 2027, `ID-JAG -06`, `Identity Chaining -17`, `spiffe-client-auth -02`, `CAD26 Annexe H.2`, `SIG-003`) — encadrés en `CRE-IA-2027` **v2.0** derrière adaptateurs réversibles, parades `CBOR-COSE` `O(1)` anti-`HTTP 431` et bail local `fail-closed` `TTL ≤ 5 s` — l’AS impose cinq verrous par saut (`ADR-018`) P : CAP-036 :

1. **Échange systématique et zéro relais.** Chaque saut exécute `RFC 8693` en gardant le mandant dans `sub` (pseudonymisé sous table séparée du responsable de la protection des renseignements personnels, `RPRP`, Ch. 8) et l’identité `NHI` dans `act` E : EXIG-IAM-08 ; usurpation E : EXIG-IAM-09 et relais de jeton E : EXIG-IAM-12 E : EXIG-MCP-11 sont interdits sans dérogation E : EXIG-GOV-17. Hors session humaine, l’agent utilise *client credentials* à portées par outil E : EXIG-IAM-16.
2. **Intersection monotone bornée.** Les droits se restreignent à mandant ∩ agent sur **deux sauts maximum** E : EXIG-IAM-10 E : EXIG-ORC-04.
3. **Audience unique et détails typés.** `RFC 8707` fixe un destinataire unique E : EXIG-IAM-11 et `Rich Authorization Requests` (`RFC 9396`) porte plafond, compte et condensat `h`.
4. **Possession cryptographique.** Contre le vol de jetons au porteur (`C26 ch. 19`, `S-067` (Vol. III `F-21`)), `RFC 9700` E : EXIG-IAM-13 lie le jeton (`cnf`) par **TLS mutuel (`mTLS`, `RFC 8705`)** ou *Demonstrating Proof of Possession* (**`DPoP`,** `RFC 9449`) E : EXIG-IAM-14.
5. **Révocation continue et coupe-circuit `< 10 s` `[S]`.** Les flux *Shared Signals Framework* (`SSF`) et *Continuous Access Evaluation Profile* (`CAEP`) visent le plafond global `≤ 15 min` de `CAD26` E : EXIG-IAM-20 E : EXIG-SEC-26, tandis que le **coupe-circuit passerelle** suspend agent, gabarit ou outil en `< 10 s` `[S]` (`PRR S-14` / `POR-003`), testé chaque trimestre avec panne simulée d’une passerelle P : CAP-039 P : POR-003.

## 7.3 Défense anti-injection (`OWASP ASI`, règle de deux, `CaMeL`) et microVM à quatre verrous

Faute de frontière native entre instructions et données (`NIST AI 100-2 E2025`, `NCSC`), tout agent modéré ou élevé subit une modélisation des menaces. Celle-ci s’appuie sur `OWASP Top 10 for Agentic Applications 2026` **(**`ASI01–ASI10`**)**, `OWASP MCP Top 10` (bêta) et `MITRE ATLAS` (`v2026.10` : 16 tactiques, 129 techniques ; revue semestrielle) E : EXIG-SEC-01 E : EXIG-SEC-02 E : EXIG-GOV-12. Hors consigne directe du mandant et configuration épinglée, tout contenu est présumé non fiable E : EXIG-SEC-03. Si le démarquage (*spotlighting*) abaisse l’attaque de `> 50 %` à `< 2 %` sur banc (`CAD26 p. 157`), les filtres cèdent sous reformulation multilingue. **La détection seule est donc interdite** et testée en français et en anglais en CI E : EXIG-SEC-05 E : EXIG-SEC-24.

La défense applique hors modèle la **règle de deux par session composée** P : PRI-005 P : CAP-037 P : CAP-038 P : DEC-009 E : PRIN-07 E : EXIG-IAM-21 E : EXIG-SEC-04. Sur toute la session (tâche racine, `A2A`, reprises durables, événements), un magasin cohérent suit trois états : `(A)` entrée non fiable lue, `(B)` accès sensible (`P1` sensible ou `P2`), et `(C)` mutation ou sortie externe (`P2`, `P3`, tiers ou pair). Dès `(A)` actif, la passerelle opère le **retrait déterministe non dérogeable des capacités d’exfiltration**. Les outils d’envoi externe (même `P0`) et les outils `P3` disparaissent pour la session, hors redémarrage vierge ou approbation hors bande liée à `h` E : EXIG-SEC-06 E : EXIG-AUT-12 E : EXIG-GOV-17.

Contrat schématique AS de politique déclarative hors modèle (`PDP`) appliquant la règle de deux et la délégation bornée (`EXIG-SEC-04`, `EXIG-SEC-06`, `EXIG-IAM-10`) :

```
policy_id: pol-pep-rule-of-two-v1
enforcement: fail_closed
invariants:
  max_delegation_hops: 2        # EXIG-IAM-10 / EXIG-ORC-04 (RFC 8693)
  require_sender_constraint: true # RFC 9449 DPoP ou RFC 8705 mTLS
rules:
  - id: deny_exfil_when_tainted
    when:
      session.has_untrusted_input: true   # Etat (A)
      session.has_private_access: true    # Etat (B)
      tool.category_in: [outbound_egress, palier_P3]
    action: DENY_AND_REVOKE_CAPABILITY    # EXIG-SEC-06 (GOV-17 ND)
    override_only_with: out_of_band_ciba_jcs_token
```

En risque élevé, `CAD26 Tableau 39` (`§ 9.6`, pp. 158–159) recense **six patrons anti-injection** (Beurer-Kellner et al., 2025). Les trois premiers sont le **sélecteur d’actions**, **plan puis exécution** (sans confinement d’arguments) et le **map-reduce de modèles**. Les trois suivants sont le **double modèle** (planificateur privilégié et lecteur en quarantaine), **code puis exécution** (étendu par `CaMeL` au suivi formel contrôle/données) et la **minimisation du contexte**. `EXIG-SEC-07` exige au moins un patron confinant aussi les données E : EXIG-SEC-07. Sur *AgentDojo*, `CaMeL` livre `77 %` **de réussite sûre contre** `84 %` **sans défense**, recul de 7 points assumé (`CAD26 Tableau 10`, p. 33). Dans le banc reproductible `Borealis-Bench/` (Campagne 2, `campagne2_camel_injection.json`, `240` payloads), le filtre `C6` atteint `95,83 %` **de rappel** (`115/120`, `5` FN concentrés sur `data_exfiltration_trifecta` à `66,67 %`), `0,00 %` **de faux positifs** (`F1 = 97,87 %`, `p50 = 86,28 µs`), confirmant la nécessité du retrait déterministe `EXIG-SEC-06`. Or *Can CaMeLs Talk?* (`C27 § 49.6`, pp. 1038–1040 ; `C26 S-150`) prouve que **cette isolation ne se compose pas** en texte libre inter-agents. La passerelle propage donc la contamination et ré-évalue chaque arête E : EXIG-IAM-21.

Tout code généré ou fichier tiers (`ASI05`) tourne hors orchestrateur dans un **bac à sable éphémère** (microVM, noyau dédié ou `WASI`) à latence mesurée (`EXIG-SEC-11`, `DEVRAIT`) P : CAP-030 E : EXIG-ARC-10 E : EXIG-SEC-08 E : EXIG-SEC-09 E : EXIG-SEC-11. Quatre verrous s’appliquent : réseau sortant fermé et blocage `IMDS` E : EXIG-SEC-12 E : EXIG-SEC-13 ; zéro secret local E : EXIG-SEC-14 ; trois délais d’expiration et quotas E : EXIG-SEC-15 ; journal immuable externe et analyse statique préalable E : EXIG-SEC-16 E : EXIG-SEC-17. Devant les `102` fiches `NVD` `"Model Context Protocol"` de juil.–oct. 2026 (`C27 § 49.7`, p. 1040 `[É]`, serveurs tiers sous trois réserves méthodologiques), chaque serveur `MCP` est cloisonné, signé, inventorié et soumis à une équipe rouge annuelle E : EXIG-SEC-18 E : EXIG-SEC-19 E : EXIG-SEC-20 E : EXIG-SEC-21 E : EXIG-SEC-23 E : EXIG-SEC-25.

## 7.4 PKI à 47 jours, horloge post-quantique (`NIST IR 8547`) et parades au choc `HTTP 431`

De 2027 à 2035 (A `ANC-043`, `PD28 M-5`), la cryptographie affronte deux chocs désormais intégrés au socle unifié `CAD26` v1.2 (`EXIG-SEC-27`, `EXIG-SEC-28`) et à `PD28 M-5` P : PRI-012 P : CAP-040 P : DEC-012 P : POR-007. D’abord, le `CA/Browser Forum Ballot SC-081v3` ramène les certificats TLS publics à **100 jours le 15 mars 2027** D (`ANC-023`) puis **47 jours le 15 mars 2029** D (`ANC-030`, validation domaine à 10 jours). Cette échéance impose `ACME` et `SPIFFE` automatisés à 100 % (`SIG-012`).

Ensuite, le risque quantique unit **collecte pour déchiffrement différé** sur flux à secret long (20–40 ans) et **ruine probatoire** vers 2035 C : A, B, C ; SIG-009, SIG-010 des archives en `ECDSA`/`Ed25519`. Le socle est fixé : `FIPS 203` **(**`ML-KEM`**)**, `FIPS 204` **(**`ML-DSA`**)**, `FIPS 205` **(**`SLH-DSA`**)** et `NIST IR 8547` **final du 27 octobre 2026** (dépréciation après **2030**, interdiction après **2035** A, `C26 Annexe N.2` p. 664). Trois RFC 2026 le complètent (`PD28 § 5.2.2`) : `RFC 9964` (`ML-DSA` `JOSE`/`COSE`), `RFC 10024` (`TLS 1.3` `X25519MLKEM768`) et `RFC 10073` (`X.509` composites, 6 nov. 2026). L’AE distingue calendriers gouvernementaux et secteur financier privé :

| Portée juridique | Référentiels et ancres | Échéances vérifiées au 17 novembre 2026 | Effet pour une institution financière privée |
| --- | --- | --- | --- |
| **Administrations publiques fédérales canadiennes** *(secteur public)* | Stratégie `AMOPS` du Conseil du Trésor (`2025-10-09`) | Plans ministériels `2027-04-01` D (`ANC-032`), inventaire `2028-04-01` D (`ANC-034`), systèmes prioritaires fin `2031` D (`ANC-039`), reste fin `2035` D (`ANC-041`). | Lie l’administration fédérale seule ; repère d’état de l’art. |
| **Administrations civiles fédérales américaines** *(secteur public)* | `EO 14412` et `OMB M-26-15` (juin 2026) | Pilote fin `2027` D (`ANC-033`), `TLS 1.3` `2030-01-02` D (`ANC-035`), clés PQC et achats `FAR` fin `2030` D (`ANC-036`), signatures fin `2031` D (`ANC-038`), fin `2035` D (`ANC-042`). | Vise l’État américain, mais `FAR` fin 2030 entraîne l’offre infonuagique. |
| **Institutions financières privées** *(banques, patrimoine, assurances)* | `BSIF B-13 § 3.2.2`, `G7 Cyber Expert Group` (janv. 2026), `NIS CG` UE | Veille prudentielle (`SIG-009`) ; repères `G7` sur systèmes critiques en `2030–2032` A (`ANC-040`) et achèvement en `2035` A (`ANC-043`) (UE `NIS CG` : `ANC-031` fin `2026` A, `ANC-037` fin `2030` A pour administrations publiques et infrastructures critiques `SRI 2`, `ANC-044` fin `2035` A). | Cible de la trajectoire rétrograde (`POR-007` en `P2`, `POR-011` en `P3`). |

Côté AS, remplacer `ECDSA` (64 o) par `ML-DSA` cause un **choc d’amplification** (`PD28 § 5.4.1`). `ML-DSA-65` pèse **3 309 octets** (clé **1 952 o**) et `ML-DSA-87` **4 627 octets** (clé **2 592 o**), soit **50 à 72×**. Sur trois sauts par valeur (`Authorization` + `DPoP`), les en-têtes HTTP grimpent de `< 2 Ko` à `20–35 Ko`, provoquant des erreurs `HTTP 431` sur les passerelles à `8–16 Ko` (`SIG-011`). Quatre parades s’imposent : clés par `kid` **/ cache** `JWKS` ; *Transaction Tokens* courts ou `COSE` **(`RFC 9964`)** ; tampons d’en-têtes à `≥ 32 Ko` et `TLS 1.3` **hybride (`RFC 10024`)** dès `P1` (`2028–2029`), avant les signatures en `P2` (`2030–2032` A `ANC-040`). Enfin, un **scellement quotidien en arbre de Merkle `SCITT` (`RFC 9943`, `SHA-384`/`SHA-512`)** signé `SLH-DSA` **(`FIPS 205`)** protège les archives avant 2030 (`POR-007`). La **Campagne 4 de** `Borealis-Bench/` (`campagne4_mldsa_http431.json`, `crypto-rust` face à Nginx `8 KiB` et Envoy `8/60 KiB`) confirme le rejet `HTTP 431` **dès le saut 1** en `jwt_embedded_jwk` (`8 364 o` en `ML-DSA-65`, `11 259 o` en `ML-DSA-87`) et dès le saut `2–3` sur Envoy `60 KiB` en chaîne `x5c`. Le passage par `kid` sauve le saut `1` mais cède au saut `2` sous `8 KiB`; seuls les *Transaction Tokens* `CBOR-COSE` maintiennent une taille **constante** `O(1)` (`4 609 o` / `6 367 o`, `0 %` **de** `431`), tandis que `SCITT + SLH-DSA-128s` amortit le sceau à `0,786 o/evt` sur `10 000` événements (`10,8 ms`).

Correspondance `ABB → SBB` de la fabrique de confiance (état au 28 oct.–14 nov. 2026) :

| Fonction | ABB (bloc neutre) | SBB substituables (état au 28 oct.–14 nov. 2026) |
| --- | --- | --- |
| Identités `NHI` courtes | Identité cryptographique de charge (`SPIFFE` / fédération `OIDC`) | `SPIRE` (`X.509-SVID`), `OIDC` infonuagique ; annuaires encadrés (Microsoft Entra Agent ID sous réserve du gabarit partagé `EXIG-IAM-04` et sans secret client `EXIG-IAM-05`, CyberArk, Okta) |
| Politiques hors modèle | Point de décision déclaratif (`PDP` en coupure `PEP`) | Open Policy Agent (`OPA`), Cedar ; coffres à rotation (HashiCorp Vault) |
| Confinement de code | MicroVM matérielle, noyau dédié ou `WASI` fermé | Firecracker, Kata Containers, gVisor, moteurs `WASI` (OpenSandbox en évaluation) |
| Provenance et tests CI | Signature sous racines *The Update Framework* (`TUF`) et bancs d’attaque | Sigstore / Cosign (`TUF`, `CycloneDX 1.7`), Promptfoo, PyRIT, Garak |

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Imposer des identités cryptographiques de charge dédiées et parrainées sans secret statique P : PRI-004 P : CAP-035 E : EXIG-IAM-03 E : EXIG-IAM-04 E : EXIG-IAM-05 ainsi qu’un coupe-circuit exercé chaque trimestre (`≤ 15 min` global sous `CAD26`, `< 10 s` `[S]` côté passerelle sous `POR-003`) P : CAP-039 P : POR-003 E : EXIG-IAM-20 E : EXIG-SEC-26.
2. Accepter le coût d’utilité de la sécurité par conception en classe élevée (`77 %` contre `84 %`) en rendant obligatoires la règle de deux, le retrait déterministe des outils sortants et un patron confinant les données P : PRI-005 P : CAP-038 E : EXIG-SEC-04 E : EXIG-SEC-06 E : EXIG-SEC-07 E : EXIG-GOV-17.
3. Cadencer la transition cryptographique P : PRI-012 P : CAP-040 P : POR-007 sur l’échéance `TLS` à 47 jours du 15 mars 2029 D (`ANC-030`) et le calendrier financier du `G7` (`2030–2032` A `ANC-040`, puis `2035` A `ANC-043`, `SIG-009`), en les distinguant des obligations propres aux administrations publiques.

Spécifications AS

1. Émettre des identités cryptographiques courtes de charge (`X.509-SVID` `SPIFFE` ou fédération `OIDC`) hors modèle E : EXIG-IAM-04 E : EXIG-IAM-06 et enchaîner `RFC 8693` à audience unique (`RFC 8707`), `RFC 9396`, `DPoP`/`mTLS` sous `RFC 9700` et révocation `SSF`/`CAEP` (`≤ 15 min`) E : EXIG-IAM-08 E : EXIG-IAM-10 E : EXIG-IAM-11 E : EXIG-IAM-13 E : EXIG-IAM-14 E : EXIG-IAM-20.
2. Propager le marquage de contamination inter-agents face à la non-composition de `CaMeL`, ré-évaluer les politiques à chaque arête E : EXIG-IAM-21, et isoler le code en microVM ou `WASI` sous quatre verrous (réseau/`IMDS` fermés, zéro secret, délais à trois niveaux, journal externe et porte statique) P : DEC-009 E : EXIG-SEC-08 E : EXIG-SEC-12 E : EXIG-SEC-13 E : EXIG-SEC-14 E : EXIG-SEC-15 E : EXIG-SEC-16 E : EXIG-SEC-17.
3. Parer les erreurs `HTTP 431` dès `P1` : tampons passerelles `≥ 32 Ko`, clés `ML-DSA` par `kid`/JWKS, *Transaction Tokens* / `COSE` (`RFC 9964`), `TLS 1.3` hybride (`RFC 10024`), `ACME` intégral et scellement `SCITT` (`RFC 9943`) signé `SLH-DSA` (`FIPS 205`) P : DEC-012.

## 7.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Authentification des agents et justificatifs | Identité `NHI` dédiée, attestations courtes de charge (`SPIFFE` `SVID` / `OIDC`) sans secret client et hors modèle E : EXIG-IAM-03 E : EXIG-IAM-04 E : EXIG-IAM-05 E : EXIG-IAM-06 | Cohorte transitoire (90 j) en lecture seule `P0`/`P1` avec secret propre en coffre sous dérogation E : EXIG-GOV-16 | `[N]` `BSIF` B-13 ; `[É]` `CAD26` § 9.2 ; `C26` `S-103` (Vol. III `F-57`) |
| Propagation des droits sur plusieurs sauts | Échange `RFC 8693` par saut, audience unique `RFC 8707`, possession `DPoP`/`mTLS` (`≤ 2` sauts) E : EXIG-IAM-08 E : EXIG-IAM-10 E : EXIG-IAM-11 E : EXIG-IAM-14 | Jamais de relais direct de jeton ni d’usurpation humaine (interdictions absolues E : EXIG-GOV-17) | `[N]` `RFC 8693` § 4.1 (`C26` `S-093`), `RFC 9700` ; `CAD26` § 9.3 |
| Session ayant lu un contenu non fiable | Marquage propagé, retrait déterministe des envois et `P3`, patron confinant les données (`CaMeL`) en classe élevée E : EXIG-SEC-04 E : EXIG-SEC-06 E : EXIG-SEC-07 | Action sortante ou `P3` uniquement après approbation humaine hors bande liée au condensat `h` E : EXIG-AUT-12 | `[M]` Debenedetti et coll. (`77 %` vs `84 %`) ; *Can CaMeLs Talk?* (`C27` § 49.6) |
| Exécution de code généré ou fichiers tiers | Bac à sable éphémère par microVM ou `WASI` sans réseau, `IMDS` bloqué et zéro secret E : EXIG-SEC-08 E : EXIG-SEC-12 E : EXIG-SEC-13 E : EXIG-SEC-14 | Jamais dans l’orchestrateur ni en conteneur standard partageant le noyau hôte | `[É]` `OWASP` `ASI05` ; `CAD26` § 9.7 ; `PD28` `DEC-009` |
| Flux et jetons face au post-quantique | `TLS 1.3` hybride (`RFC 10024`) dès `P1`, tampons `≥ 32 Ko`, clés par `kid`/JWKS et *Transaction Tokens* P : CAP-040 | Bascule complète des signatures (`RFC 9964`, `RFC 10073`) au Palier 2 (`2030–2032` A `ANC-040`) | `[N]` `FIPS 203/204`, `NIST IR 8547` final, `RFC 9964/10024/10073` |
| Valeur probante décennale des mandats | Arbre de Merkle `SCITT` (`SHA-384`/`SHA-512`) scellé quotidiennement en `SLH-DSA` (`FIPS 205`) avant 2030 P : DEC-012 P : POR-007 | Traces techniques éphémères de débogage conservées moins de douze mois | `[N]` `FIPS 205`, `RFC 9943` ; `PD28` M-5 § 5.4 (`POR-007`) |

## 7.6 Limites et renvois

**Limites et réserves.** La grille `Q-A..Q-E` (`C26 ch. 14`) et le passeport virtuel (`C26 ch. 16`) sont des constructions d’auteur (`[S]`). Au 17 novembre 2026, `OAuth 2.1` (`draft-17`), les huit documents `IETF WIMSE` et les brouillons de révocation en cascade demeurent non ratifiés (`CAD26 Annexe H.2`, `C26 Annexe N.2`). Les mesures *AgentDojo* (`77 %` vs `84 %`) et *Agent Security Bench* (`84,30 %`, `CAD26 p. 159`) proviennent de bancs expérimentaux et non de parcs en production. Enfin, l’absence d’exigence post-quantique dans `CAD26` v1.1 (`Annexe H.5`, p. 341) est compensée ici par `PD28 M-5` et `NIST IR 8547` final.

**Renvois aux volumes sources :** `C26` ch. 14 (§ 14.1–14.4 pp. 161–167), ch. 16 (pp. 181–190), ch. 17 § 17.6 (pp. 198–202), ch. 18 (§ 18.1 pp. 204–206), ch. 19–21 (`S-103` / Vol. III `F-57` p. 234, `PQC` ch. 21 pp. 238–253), Ann. N.2 (pp. 662–668) ; `CAD26` ch. 9 (`EXIG-IAM-01..21`, `EXIG-SEC-01..28` pp. 138–171), Tableau 10 (p. 33), Ann. H.2/H.5 ; `C27` ch. 29–32 (`ADR-018..020` pp. 581–675), ch. 49 (§ 49.5–49.7 pp. 1036–1041) ; `PD28` `M-5` (pp. 72–83), `CAP-030`, `CAP-035..040`, `DEC-009`, `DEC-012`, `POR-003`, `POR-007`, `POR-011`, `SIG-003`, `SIG-009..012`.
