# Journal d'ancrage atomique Wyvern G2 — Chapitre 16 (`ch16`)

- **Unité auditée :** `Sources/Compendium/ouvrage/manuscrit/06 - Partie VI/Chapitre 16.md` (`4 863` mots de prose selon `verifie_manuscrit.py`, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch16-sources.md` (`[1]`–`[12]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`, `a2a_card.py`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b3-3`
- **Passe G2 initiale (supportés)** : 19
- **Rectifications appliquées lors de la passe G2** : 21
- **Verdict final — supportés** : 42 / 42 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 16.md`

Toutes les formulations demandant un réancrage ou une nuance modale lors de la passe initiale ont été rectifiées directement dans [Chapitre 16.md](file:///c:/Github/Agentique/Sources/Compendium/ouvrage/manuscrit/06%20-%20Partie%20VI/Chapitre%2016.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant la vedette propriétaire `Identité non humaine`, les huit concepts `owned_concepts`, l'ensemble des renvois `[1]`–`[12]`, les trois figures `SCH-16-01`..`03`, les trois tableaux et le calibrage (`4 863` mots dans `[4 251, 4 989]`) :

1. **Ratio `82:1`, `SCIM` (`RFC 7643`) et grille `0/15` (`L5`, `L13`, `L15`, `L40`) :** qualification explicite du ratio `82:1` comme repérage illustratif du `Tome 1` (§ 12.2, issu d'enquêtes fournisseurs hors socle `L+`), séparation de l'observation `RFC 7643` § 4 (`Tome 1` § 12.1) par rapport à `RFC 6749` § 4.1 (`[3, 6]`), et rattachement du décompte `0/15` (`0` pleine, `7` partielles, `1` négative, `7` muettes au degré 3) à la grille analytique interne du `Tome 1` (ch. 14, Tableau 14.2).
2. **Gabarit *Blueprint*, règle `SIRH < 72 h` et non-réattribution (`L27`, `L29`) :** rattachement de la non-réattribution perpétuelle et de l'isolation des secrets hors `LLM` directement à `[3]` (`draft-ietf-wimse-aims-01`, § 6 et § 8), identification du profil *Blueprint* (`Tome 2` § 9.2) et qualification du double parrainage `SIRH` avec transfert/suspension en moins de `72 heures` comme règle opérationnelle interne du traité (`EXIG-IAM-03`, `EXIG-IAM-07`, `EXIG-GOV-13`, `Tome 3`, `→ Chapitre 32`) appuyant `BSIF E-23` / `AMF` (`[12]`).
3. **Modalités exactes `RFC 9700`, `FAPI 2.0` et brouillons `SCIM` (`L48`, `L50`) :** alignement exact sur la `RFC 9700` `[6]` (`MUST NOT` mot de passe, `SHOULD NOT` implicite banni en `G0` par `a2a_card.py`, `PKCE S256`, `SHOULD` `mTLS`/`DPoP` élevé à `DOIT` par `EXIG-IAM-14`), ancrage de `FAPI 2.0` sur `[3]` (§ 10.4, § 14), et rattachement des brouillons `draft-abbey-scim-agent-extension-00` et `draft-wzdk-scim-agent-resource-00` au `Tome 1` (§ 12.5, hors socle `L+`).
4. **Annuaires commerciaux et modèles de registres (`L52`–`L65`, `Tableau 16.1`) :** ancrage de la mention générique des plateformes IAM (`Entra`, `Bedrock`) sur `[9]` (L630), rattachement des jalons datés (`AWS Bedrock AgentCore` oct. 2025, `Entra Agent ID` avr. 2026 / `agentIdentityBlueprint` / deux plans d'identité, `Google Cloud Agent Identity` 22 avr. 2026 / `24 h`) au suivi daté `S-082` du `Tome 1` (§ 12.1, § 15.2, hors `L+`), et rattachement du brouillon `CSA` (`27 mars 2026`, `toolAccessList`, `permissionBoundaries`) et d'`AGNTCY ADS` (`draft-mp-agntcy-ads-02`) au `Tome 1` (§ 15.3, hors `L+`).
5. **`AgentCard` (`L77`), `SPIFFE`/`SPIRE`, `Edge 72 h`, `W3C VC/DID` et `GLEIF vLEI` (`L87`–`L121`, `Tableau 16.2`) :** attribution explicite du comptage à `14` champs Protobuf (`a2a.proto`) et du relevé `SECURITY.md` au `Tome 1` (§ 15.1) en appui à `[11]`, séparation des primitives `SPIFFE` (`[1, 2, 3]`) de l'implémentation `SPIRE` (`Tome 6` § 10.2) et des paramètres de profil internes (`Envoy SDS`, `TTL 1 h` / `15 min`, `ClusterSPIFFEID`, `IDMZ` `IEC 62443-3-3 SL-3`), qualification du seuil *Edge* `72 heures` comme cible interne `CAP-028` (`Tome 4`, non prescrite par `[1, 4]`), correction d'`ANC-022` vers `SPEC-DRAFT-WIMSE-*` dans le `Tableau 16.2`, précision de la posture d'absence documentée (degré 3) sur `W3C DID/VC` (`Tome 1` § 13.5, `[12]`) et mention que les justificatifs `OOR`/`ECR` de `GLEIF vLEI` (`ISO 17442-3` 2024, doc. `oct. 2026` `[5]`) sont délivrés à des personnes physiques mandatées auxquelles `CAP-041` arrime l'agent.
6. **Alignement doctrinal Vague 2 (`L1–L23`, `L33`, `L52`, `L60–L70`, `L87`, `L111–L119`, `L137`) :** synchronisation du titre `L1` sur `specs/manifest.json` (`Chapitre 16 — Identités non humaines parrainées (SIRH/IdP), attestations SPIFFE/SPIRE et fédération inter-entreprises (DID/VC, vLEI)`), éradication des comptes de service statiques hérités des parcs `RPA`/`batch`/`iPaaS` via le cycle *Joiner-Mover-Leaver* (`SIRH → IdP` `< 72 h`), mention qualifiée hors `L+` des `IdP` fédérés d'entreprise (`Entra ID`, `Okta`, `Keycloak`, `PingFederate`), réconciliation avec la `CMDB`/`ITAM` (`EXIG-IAM-18`), pont à deux étages `IdP`/`SIRH` ↔ `SPIFFE`/`SPIRE` + `RATS` jusqu'en `IDMZ`, et ouverture multisectorielle de `vLEI` aux chaînes logistiques `EDC`/`ODRL` et achats industriels aux côtés de `SIG-007`/`SIG-103` et `[12]`.

---

## 2. Registre complet des affirmations atomiques (`C16-01` à `C16-42`)

### Section introductive et § 16.1 — Titre, cadrage et résumé exécutif (`L1–L19`)

- **C16-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice posant le raccordement de chaque agent d'automatisation au socle `IAM`/`IdP` et au `SIRH` par une identité non humaine cryptographiquement attestée (`SPIFFE`/`SPIRE`), éradiquant les comptes statiques hérités du `RPA` et des lots tout en préparant la fédération inter-organisations (`DID`/`VC`, `vLEI`).
  - **Appui vérifié :** `specs/manifest.json` (`ch16`, `D06`, `SUB_D06_01`), structure `§ 16.1`–`§ 16.3`.
  - **Passe initiale :** conforme (synchronisé Vague 2) · **Action :** alignement `manifest.json` · **Verdict : supporté**

- **C16-02 (`L5`)** — *Affirmation :* Les Systèmes d'agentivité rompent l'hypothèse IAM humaine/statique ; selon le repérage illustratif du `Tome 1` (§ 12.2, enquêtes fournisseurs hors socle `L+`), un ratio de `82:1` est cité, et le partage d'un compte humain ou d'une clé API détruit la traçabilité d'imputabilité juridique et prudentielle.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 12.2`, `L3326–3329` : ratio illustratif `82` pour `1`), `SRC-055.txt` (`[9]` `ASI03` L535–556, `NHI2`/`NHI10` L1615–1780), `SRC-059.txt` (`[10]` `ASI03` L13–15).
  - **Passe initiale :** reformulée · **Action :** qualifié `82:1` comme repérage illustratif du `Tome 1` (§ 12.2) hors socle `L+`, distinct du risque vérifié dans `[9, 10]` · **Verdict : supporté**

- **C16-03 (`L7`)** — *Affirmation :* Première assise de `D06` instituant l'**Identité non humaine** (`NHI`) propre avant délégation (`→ Chapitre 17`) et migration cryptographique (`→ Chapitre 18`), en cohérence avec `← Chapitre 05`, arrêtée au `2 décembre 2026` sous clause stricte `non-avis`.
  - **Appui vérifié :** `registre/glossaire-termes.json` (`L71–77`, vedette propriétaire `Identité non humaine`), `specs/manifest.json` (`ch16`, `freeze_date`), `SRC-055.txt` (`[9]` L13–16 : clause non-avis).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-04 (`L9`)** — *Affirmation :* Sans séparation nette entre identité du mandant humain, identité propre de l'agent et identité de l'infrastructure d'exécution, les journaux d'audit deviennent inexploitables lors d'une enquête ou inspection réglementaire (`[3, 9]`).
  - **Appui vérifié :** `SRC-048.txt` (`[3]` § 6, § 8), `SRC-055.txt` (`[9]` `ASI03`, `NHI8`/`NHI10` L1724–1780 : *Untraceability*).
  - **Passe initiale :** conforme · **Action :** en recollation `G3` (`seed=20270901`), remplacé le renvoi `[12]` (`SRC-071`, index public sans mention des journaux d'audit) par `[3, 9]` · **Verdict : supporté**

- **C16-05 (`L13`, § 16.1)** — *Affirmation :* `OAuth 2.0` (`RFC 6749` § 4.1) présuppose un agent utilisateur humain interactif (`[3, 6]`) et `SCIM` (`RFC 7643` § 4, `Tome 1` § 12.1 hors `L+`) ne couvre que des utilisateurs et groupes sans ressource ratifiée « agent autonome » au `2 décembre 2026` ; `OWASP ASI03` confirme que l'absence d'identité distincte empêche le moindre privilège (`[9, 10]`).
  - **Appui vérifié :** `SRC-048.txt` (`[3]` L839–848 : `RFC 6749` § 4.1 via navigateur), `SRC-133.txt` (`[6]` L141), `Corpus/Tome 1` (`§ 12.1`, `L3304`), `SRC-055.txt` (`[9]` L545–548), `SRC-059.txt` (`[10]` L13–15).
  - **Passe initiale :** réancrée · **Action :** dissocié l'appui `[3, 6]` pour `RFC 6749` § 4.1 du repérage `Tome 1` (§ 12.1) pour `RFC 7643` § 4 · **Verdict : supporté**

- **C16-06 (`L15`, § 16.1)** — *Affirmation :* Selon la grille analytique interne du `Tome 1` (ch. 14), aucun des trois mécanismes isolés instruits n'obtient de verdict plein sur les quinze cellules de la matrice `3 × 5` (`0/15`, `Q-A` à `Q-E`) ; `SPIFFE` `[1]` (mis en œuvre par `SPIRE`, `Tome 6` § 10.2) fournit dès maintenant une attestation interne sans secret statique, tandis que les passeports `W3C VC` (`Tome 1` § 13.1) / `GLEIF vLEI` (`ISO 17442-3` `[5]`) relèvent du Palier 3 conditionnel (`CAP-006`, `CAP-041`).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 14.2` L3681, `§ 13.1`), `Corpus/Tome 6` (`§ 10.2`), `SRC-046.txt` (`[1]` L53–79), `SRC-079.txt` (`[5]` L5–10), `Corpus/Tome 4` (`CAP-006`, `CAP-041`).
  - **Passe initiale :** réancrée · **Action :** explicité le caractère interne de la grille `Tome 1` ch. 14, harmonisé `3 × 5 (0/15)` (lissage G5) et distingué `SPIFFE` `[1]` de `SPIRE` (`Tome 6` § 10.2) · **Verdict : supporté**

### Section 16.2.1 — Identités `NHI`, `OAuth 2.1`, annuaires, registres et `AgentCard` (`L21–L75`, Tableau 16.1, Figure 1–2)

- **C16-07 (`L21`, § 16.2.1)** — *Affirmation :* Les secrets statiques exposés par fuite d'invite ou d'environnement ouvrent la voie aux dix vecteurs `OWASP NHI Top 10` (`NHI1` à `NHI10`) et à l'usurpation `ASI03`.
  - **Appui vérifié :** `SRC-055.txt` (`[9]` Appendix C L1577–1780 : table `NHI1`..`NHI10` et L535–641 `ASI03`), `SRC-059.txt` (`[10]` L13–15).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-08 (`L23`, § 16.2.1)** — *Affirmation :* Citation littérale de `SRC-055.txt` `[9]` (`20` mots : *« Without a distinct, governed identity of its own, an agent operates in an attribution gap that makes enforcing true least privilege impossible. »*) fondant la séparation usager / infrastructure / agent.
  - **Appui vérifié :** `SRC-055.txt` (`[9]` L546–547, verbatim exact ≤ `40` mots).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-09 (`L25`, § 16.2.1)** — *Affirmation :* Les exigences `EXIG-IAM-01` à `EXIG-IAM-07`, `ADR-018`, `CAP-035`, `PRI-004`, `PRIN-03` et `PRR S-01` interdisent tout compte humain prêté et toute clé statique en code, invite ou variable d'environnement, et imposent une identité propre par environnement découplée entre définition logique et instances.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`A.6.1`, `S-01*`), `Corpus/Tome 2` (`EXIG-IAM-01..07`), `SRC-046.txt` (`[1]` L40), `SRC-047.txt` (`[2]` L291, L992), `SRC-048.txt` (`[3]` L350–385, L432).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-10 (`L27`, § 16.2.1)** — *Affirmation :* Le couple *Agent Identity Blueprint* (`Tome 2` § 9.2) / instances NHI éphémères s'accompagne d'une non-réattribution perpétuelle des identifiants retirés (`draft-ietf-wimse-aims-01` `[3]`, `→ Chapitre 22`) et d'une injection des justificatifs externes via `SBB-SECRETS-VAULT` hors fenêtre contextuelle du `LLM` (`EXIG-IAM-06`).
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 9.2`, `EXIG-IAM-06`), `registre/matrice-exig-prr-c40.json` (`SBB-SECRETS-VAULT`), `SRC-048.txt` (`[3]` § 6 L377–385, § 8 L551–555), `SRC-047.txt` (`[2]` L1011–1029), `SRC-055.txt` (`[9]`).
  - **Passe initiale :** réancrée · **Action :** rattaché le profil *Blueprint* au `Tome 2` (§ 9.2), précisé `draft-ietf-wimse-aims-01` (lissage G5) et rattaché la non-réattribution ainsi que l'isolation hors `LLM` à `[3]` et `EXIG-IAM-06` · **Verdict : supporté**

- **C16-11 (`L29`, § 16.2.1)** — *Affirmation :* Règle de gouvernance interne du traité (`EXIG-IAM-03`, `EXIG-IAM-07`, `EXIG-GOV-13`, `→ Chapitre 32`) : double parrainage humain (métier et technique) couplé au `SIRH` imposant transfert ou suspension sous `72 heures` (`Tome 3`, cible opérationnelle) pour appuyer les attentes d'inventaire (`← Chapitre 25`, `BSIF E-23` et `AMF` `[12]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-IAM-03`, `EXIG-IAM-07`, `EXIG-GOV-13`), `Corpus/Tome 3` (cible `72 h` `SIRH`), `SRC-071.txt` (`[12]` L89–95, L263–275).
  - **Passe initiale :** réancrée · **Action :** explicité le statut de règle interne du traité pour le seuil `SIRH < 72 heures` distinct de la source `[12]` · **Verdict : supporté**

- **C16-12 (`L31–L36`, § 16.2.1)** — *Affirmation :* La grille falsifiable des cinq questions (`Q-A` à `Q-E`) teste séquentiellement identifiant stable/vérifiable/révocable (`[3, 9]`), provenance et ancrage (`[1, 11]`), chaîne de mandat interrogeable à l'exécution (`[3, 6]`), bornes opposables au `PEP` (`[9, 10]`) et répondant juridique (`[9, 12]`).
  - **Appui vérifié :** `Corpus/Tome 1` (`ch. 14 Tableau 14.1`, `L3639–3645`), `SRC-048.txt` (`[3]`), `SRC-055.txt` (`[9]`), `SRC-046.txt` (`[1]`), `SRC-083.txt` (`[11]`), `SRC-133.txt` (`[6]`), `SRC-059.txt` (`[10]`), `SRC-071.txt` (`[12]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-13 (`L38`, § 16.2.1)** — *Affirmation :* Dépendance logique stricte entre les cinq questions (un échec sur `Q-A` rend `Q-D` et `Q-E` inapplicables `[6, 9]`) et démultiplication du coût de faille à travers les paliers d'autonomie `L1`–`L4` (`← Chapitre 05`).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 14.4`), `SRC-133.txt` (`[6]` § 2.2), `SRC-055.txt` (`[9]` `ASI03`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-14 (`L40`, § 16.2.1)** — *Affirmation :* Règles méthodologiques de la grille `3 × 5` (construction analytique du `Tome 1`, ch. 14 : par mécanisme, trois verdicts stricts, réfutabilité) et score `0/15` au Tableau 14.2 (`0` pleine, `7` partielles, `1` négative, `7` muettes au degré 3) sur carte `A2A` signée `[11]`, annuaire commercial et registre gouverné, complété par les constats WIMSE `[2, 3]`.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 14.1–14.2`, `Tableau 14.2`, `L3649–3681`), `Corpus/Tome 5` (`§ 7.1`), `SRC-083.txt` (`[11]`), `SRC-047.txt` (`[2]`), `SRC-048.txt` (`[3]`).
  - **Passe initiale :** réancrée · **Action :** rattaché le comptage exact `0/15` (`grille 3 × 5`, lissage G5) au `Tableau 14.2` du `Tome 1` (§ 14.2) et séparé les apports WIMSE `[2, 3]` · **Verdict : supporté**

- **C16-15 (`L42–L44`, Figure 1)** — *Affirmation :* La Figure 1 (`SCH-16-01.svg`) compare l'avant (prêt de compte, clés statiques, `0/15`) à l'après (`Blueprint`/`Instance`, parrainage `SIRH < 72 h`, socle `OAuth 2.1`/`BCP 240`, crible `Q-A`..`Q-E`).
  - **Appui vérifié :** `specs/manifest.json` (`ch16`, `SCH-16-01`), `schemas/SCH-16-01.svg`, `schemas/rendus/SCH-16-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-16 (`L46`, § 16.2.1)** — *Affirmation :* Assainissement IAM (`AAA`) cantonnant `SAML 2.0` à la fédération d'authentification d'usagers, utilisant `OIDC` sur `OAuth 2.0`, et aligné sur la norme `IETF BCP 240 / RFC 9700` (janvier 2025).
  - **Appui vérifié :** `SRC-133.txt` (`[6]` L3–11, L143–144).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-17 (`L48`, § 16.2.1)** — *Affirmation :* La `RFC 9700` `[6]` proscrit absolument le flux mot de passe (`MUST NOT`), déconseille l'implicite (`SHOULD NOT`, banni en `G0` par `a2a_card.py`), impose `PKCE` `S256` aux clients publics et aux serveurs d'autorisation, recommande `mTLS` (`RFC 8705`) ou `DPoP` (`RFC 9449`, élevé à `DOIT` par `EXIG-IAM-14`), tandis que `FAPI 2.0` complète les profils financiers (`[3]`), qu'`OAuth 2.1` reste un brouillon (`[6]`, `Tome 5` § 7.6) et que `SCIM` (`RFC 7643`, `Tome 1` § 12.6) ne convient pas à la révocation instantanée `[2, 3, 6]`.
  - **Appui vérifié :** `SRC-133.txt` (`[6]` § 2.1.1 L290–318, § 2.1.2 L350, § 2.2.1 L375–378, § 2.4 L424, § 1 L203), `SRC-048.txt` (`[3]` § 10.4 L826, § 14 L1238 : `FAPI 2.0`), `a2a_card.py` (`L22`), `Corpus/Tome 2` (`EXIG-IAM-14`), `Corpus/Tome 5` (`§ 7.6`), `Corpus/Tome 1` (`§ 12.6`).
  - **Passe initiale :** reformulée · **Action :** aligné les verbes modaux exacts `MUST NOT`/`SHOULD NOT`/`SHOULD` de la `RFC 9700`, ancré `FAPI 2.0` sur `[3]` et rattaché `SCIM` au `Tome 1` (§ 12.6) · **Verdict : supporté**

- **C16-18 (`L50`, § 16.2.1)** — *Affirmation :* Les brouillons `draft-abbey-scim-agent-extension-00` (expiré le `19 avril 2026`) et `draft-wzdk-scim-agent-resource-00` (soumission individuelle sans adoption `SCIM`), relevés au `Tome 1` (§ 12.5, hors socle `L+`), sont pré-normatifs et impropres à fonder la production `[3]`.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 12.5`, `Tableau 12.2`, `L3395–3405`), `SRC-048.txt` (`[3]` § 2, § 6–8).
  - **Passe initiale :** réancrée · **Action :** explicité que le repérage de ces deux brouillons provient du `Tome 1` (§ 12.5, hors socle `L+`) · **Verdict : supporté**

- **C16-19 (`L52`, § 16.2.1)** — *Affirmation :* `OWASP` recense l'intégration d'agents dans les plateformes commerciales (`Microsoft Entra`, `AWS Bedrock` `[9]`), et le suivi daté du `Tome 1` (§ 12.1, § 15.2, entrée `S-082` hors socle `L+`) précise trois jalons (`AWS Bedrock AgentCore Identity` oct. 2025, `Microsoft Entra Agent ID` avr. 2026 / `agentIdentityBlueprint` et écart d'accès conditionnel à deux plans, `Google Cloud Agent Identity` 22 avr. 2026 / certificats SPIFFE `24 h` / *auth manager* en préversion).
  - **Appui vérifié :** `SRC-055.txt` (`[9]` L628–632), `Corpus/Tome 1` (`§ 12.1` L3318, `§ 15.2.1–15.2.2` L3840–3872, `S-082`).
  - **Passe initiale :** réancrée · **Action :** ancré la mention générique des plateformes sur `[9]` et rattaché les dates/capacités précises au repérage `Tome 1` (§ 12.1, § 15.2, `S-082`) · **Verdict : supporté**

- **C16-20 (`L54`, § 16.2.1)** — *Affirmation :* La disponibilité générale d'une plateforme ne couvre pas toutes ses fonctions en *Preview* (`Tome 1` § 15.2.1) ; sous `CAP-035` et le suivi `S-082`, tout annuaire commercial doit être encapsulé derrière un registre interne neutre pour éviter le standard de fait et le verrouillage (`→ Chapitre 09`) `[2, 3]`.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 15.2.1` L3842, `§ 15.2.3`, `S-082`), `registre/matrice-exig-prr-c40.json` (`CAP-035`), `SRC-047.txt` (`[2]`), `SRC-048.txt` (`[3]`).
  - **Passe initiale :** reformulée · **Action :** remplacé la désignation erronée d'exigence sur `S-082` par `capacité CAP-035 et suivi S-082` et rattaché *Preview* au `Tome 1` · **Verdict : supporté**

- **C16-21 (`L56–L59`, § 16.2.1)** — *Affirmation :* Trois modèles de registres non substituables coexistent : (1) annuaire protocolaire `A2A v1.0.1` (`[11]`, sans interface normative de registre), (2) registre d'entreprise (brouillon laboratoire `CSA` `27 mars 2026`, `toolAccessList` et `permissionBoundaries`, `Tome 1` § 15.3.1 hors `L+`, opposable seulement via `PEP` `[3, 9]`), et (3) registre fédéré `AGNTCY ADS` (`draft-mp-agntcy-ads-02`, `Tome 1` § 15.3.2 hors `L+`, `← Chapitre 08`).
  - **Appui vérifié :** `SRC-083.txt` (`[11]` § 8.2 L1974–1981), `Corpus/Tome 1` (`§ 15.3.1–15.3.2`, `L3913–3942`), `SRC-055.txt` (`[9]` L505–507 `PEP`/`PDP`), `SRC-048.txt` (`[3]` § 10.4).
  - **Passe initiale :** réancrée · **Action :** précisé l'origine `Tome 1` (§ 15.3, hors `L+`) pour le brouillon `CSA` et `AGNTCY ADS` · **Verdict : supporté**

- **C16-22 (`L61–L67`, Tableau 16.1)** — *Affirmation :* Le Tableau 16.1 synthétise les trois modèles de registres, la question adressée (`Q-A`..`Q-D`), la portée et le statut au `2 décembre 2026`, la limite critique et la parade obligatoire (`[5, 9, 10, 11]`, `Tome 1` § 15.3).
  - **Appui vérifié :** `SRC-083.txt` (`[11]`), `Corpus/Tome 1` (`§ 15.3`), `SRC-055.txt` (`[9]`), `SRC-059.txt` (`[10]`), `SRC-079.txt` (`[5]`).
  - **Passe initiale :** réancrée · **Action :** mis à jour les mentions de statut de `CSA` et `AGNTCY ADS` vers `Tome 1 § 15.3.1` / `§ 15.3.2` · **Verdict : supporté**

- **C16-23 (`L69`, § 16.2.1)** — *Affirmation :* Dans `A2A v1.0.0`/`v1.0.1` `[11]`, la signature d'`AgentCard` impose (`MUST`) avant signature une canonicalisation `JCS` (`RFC 8785` `[8]`, tri UTF-16, formatage ECMAScript des nombres) excluant `signatures`, puis une enveloppe `JWS` (`RFC 7515` `[7]`) dont la charge est reconstruite à la vérification ; dans la trousse `Tome 8`, `a2a_card.py` contrôle `ES256` sur `JCS` et épingle `jku` et `kid` (`G0`, `→ Chapitre 08`, `→ Chapitre 22`).
  - **Appui vérifié :** `SRC-083.txt` (`[11]` § 8.4 L2002–2126), `SRC-077.txt` (`[8]` § 3.2.2.3 & § 3.2.3), `SRC-005.txt` (`[7]`), `Tomes/Tome 8/.../a2a_card.py` (`L157–182`), `aq/rapports-g0.json` (`L52–69`, `L100–105`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-24 (`L71`, § 16.2.1)** — *Affirmation :* Quatre angles morts de la signature `AgentCard` : apposition `MAY` et vérification `SHOULD` (`[11]`) ; en-tête protégé normatif à quatre paramètres (`alg`, `typ`, `kid`, `jku`) sans `nbf`/`iat`/`exp` (`[11]`) et `14` champs Protobuf (`a2a.proto`, `Tome 1` § 15.1.3) sans expiration ni révocation ; `MUST NOT` sur clés révoquées sans point de statut ni étape de fraîcheur dans la procédure en six étapes (`[11]`) ; magasin de confiance `MAY maintain` hors protocole (`[11]`) et `SECURITY.md` / charte sans gestion des clés (`Tome 1` § 15.1.2) `[7, 8, 11]`.
  - **Appui vérifié :** `SRC-083.txt` (`[11]` L2004, L2068–2077, L2119–2133), `Corpus/Tome 1` (`§ 15.1.2–15.1.3`, `L3780`, `L3800`), `SRC-084.txt` (`message AgentCard` 14 champs), `SRC-005.txt` (`[7]`), `SRC-077.txt` (`[8]`).
  - **Passe initiale :** réancrée · **Action :** précisé le rattachement du décompte Protobuf (`14` champs) et du balayage `SECURITY.md` au `Tome 1` (§ 15.1) en complément de `[11]` · **Verdict : supporté**

- **C16-25 (`L73–L75`, Figure 2)** — *Affirmation :* La Figure 2 (`SCH-16-02.svg`) synthétise les angles morts de l'`AgentCard` JWS/JCS, les trois modèles de registres non substituables et l'encapsulation des annuaires commerciaux.
  - **Appui vérifié :** `specs/manifest.json` (`ch16`, `SCH-16-02`), `schemas/SCH-16-02.svg`, `schemas/rendus/SCH-16-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 16.2.2 — Attestation `SPIFFE`/`SPIRE`, `DID`/`VC` et `vLEI` (`L79–L117`, Tableau 16.2, Figure 3)

- **C16-26 (`L79`, § 16.2.2)** — *Affirmation :* Le socle interne élimine le secret zéro par `SPIFFE` `[1]` et son implémentation `SPIRE` (`Tome 6` § 10.2) (`EXIG-IAM-04`, `14`, `15`, `S-01`, `S-02`) : attestation de plateforme/nœud (`TPM 2.0`/enclave) et de charge processus/noyau (`kubelet`, cgroup, condensat `SHA-256` OCI selon `SPIRE`, `[1, 2, 3]`), matérialisant les rôles `Attester`, `Verifier` et `Relying Party` de `RFC 9334` (`IETF RATS`, Informational, janv. 2023 `[4]`).
  - **Appui vérifié :** `SRC-046.txt` (`[1]` L53–79), `SRC-047.txt` (`[2]` § 4.2), `SRC-048.txt` (`[3]` § 7–8 L417–478), `SRC-010.txt` (`[4]` L5, L24–29, L700–720), `Corpus/Tome 6` (`§ 10.2.2`), `registre/matrice-exig-prr-c40.json` (`A.6.1`, `A.6.3`, `A.6.7`).
  - **Passe initiale :** réancrée · **Action :** séparé les primitives normatives `SPIFFE`/`WIMSE` (`[1, 2, 3]`) de l'architecture d'implémentation `SPIRE` (`Tome 6` § 10.2) · **Verdict : supporté**

- **C16-27 (`L81`, § 16.2.2)** — *Affirmation :* Attestation en deux étages de `SPIRE` (`Tome 6` § 10.2) : preuve de nœud puis interrogation de la `Workload API` locale `[1]` pour assigner un `SPIFFE ID` (`spiffe://<domaine>/<chemin>` `[1]`), structuré par gabarit `ClusterSPIFFEID` (`Tome 3`).
  - **Appui vérifié :** `SRC-046.txt` (`[1]` L27–31, L53–77), `Corpus/Tome 6` (`§ 10.2.2`), `Corpus/Tome 3` (`ClusterSPIFFEID`).
  - **Passe initiale :** réancrée · **Action :** rattaché le mécanisme deux étages `SPIRE` au `Tome 6` (§ 10.2) et `ClusterSPIFFEID` au `Tome 3` · **Verdict : supporté**

- **C16-28 (`L83`, § 16.2.2)** — *Affirmation :* Délivrance des `SVID` via `Workload API` `[1]` et injection en mémoire vive par `Envoy SDS` (`Tome 6` § 10.2) sans écriture disque (`[2]`) ; préférence de `X.509-SVID` (`mTLS`) sur `JWT-SVID` rejouable (`[1, 2]`), avec durées cibles du profil interne (`EXIG-IAM-15`, `Tome 3`) fixées à `TTL = 1 h` et `TTL ≤ 15 min` (`→ Chapitre 17`).
  - **Appui vérifié :** `SRC-046.txt` (`[1]` L45–50, L78), `SRC-047.txt` (`[2]` L934–939, L1135–1139), `Corpus/Tome 2` (`EXIG-IAM-15`), `Corpus/Tome 3` (`x509SVIDTTL: "1h"`, `jwtSVIDTTL: "15m"`), `Corpus/Tome 6` (`§ 10.2.2`).
  - **Passe initiale :** réancrée · **Action :** identifié `Envoy SDS` (`Tome 6`) et les `TTL` `1 h` / `15 min` (`EXIG-IAM-15`, `Tome 3`) comme paramètres du profil interne · **Verdict : supporté**

- **C16-29 (`L85`, § 16.2.2)** — *Affirmation :* Cloisonnement des *Trust Domains* hors-prod vs prod (`[1]`), traversée `IDMZ` sous `IEC 62443-3-3 SL-3` (`← Chapitre 12`, `Tome 3` § 28.6), et continuité locale *Edge* sur `TPM 2.0` visant une cible interne de `72 heures` (`CAP-028`, `Tome 4`, sans seuil prescrit par `[1, 4]`) `[3, 4]`.
  - **Appui vérifié :** `SRC-046.txt` (`[1]` L40), `Corpus/Tome 3` (`§ 28.6`, `62443-3-3 SL-3`), `Corpus/Tome 4` (`CAP-028`, `ADR-028` mentionnant le caractère non sourcé du seuil `72 h`), `SRC-048.txt` (`[3]` L418), `SRC-010.txt` (`[4]`).
  - **Passe initiale :** réancrée · **Action :** supprimé l'attribution du seuil `72 heures` aux sources `[1, 4]` et qualifié celui-ci de cible interne `CAP-028` (`Tome 4`) · **Verdict : supporté**

- **C16-30 (`L87`, § 16.2.2)** — *Affirmation :* Convergence avec `IETF WIMSE` via `draft-ietf-wimse-workload-identity-practices-08` (`30 oct. 2026` `[2]` : audience unique § 5.7, protection `IMDS` `169.254.169.254` contre `SSRF` § 3.2/5.1.3/5.1.5) et `draft-ietf-wimse-aims-01` (`2 nov. 2026` `[3]` : authn/authz des agents IA sur WIMSE et OAuth 2.0), à `0` RFC au `2 décembre 2026` et encapsulés par adaptateurs réversibles.
  - **Appui vérifié :** `SRC-047.txt` (`[2]` L5–8, L263, L948–952, L1148–1161), `SRC-048.txt` (`[3]` L13–29, L279–281), `ch16-sources.md` (`[2, 3]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-31 (`L89–L97`, Tableau 16.2)** — *Affirmation :* Le Tableau 16.2 résume cinq briques d'identité (`X.509-SVID`, `JWT-SVID`, `IETF WIMSE` `workload-identity-practices-08` / `aims-01` des `30 oct. / 2 nov. 2026`, `W3C VC 2.0 / DID / did:wba`, `GLEIF vLEI ISO 17442-3`), leurs cibles `TTL`/stockage, leur statut normatif au `2 décembre 2026` et leur usage prescrit (`[1, 2, 3, 5]`, `Tome 1` § 13.1, `specifications-lplus.json`).
  - **Appui vérifié :** `SRC-046.txt` (`[1]`), `SRC-047.txt` (`[2]`), `SRC-048.txt` (`[3]`), `SRC-079.txt` (`[5]`), `Corpus/Tome 1` (`§ 13.1`), `registre/specifications-lplus.json` (`SPEC-DRAFT-WIMSE-*`).
  - **Passe initiale :** réancrée · **Action :** corrigé `ANC-022` vers `SPEC-DRAFT-WIMSE-*`, harmonisé les versions/dates exactes `WIMSE` (lissage G5), distingué la norme `ISO 17442-3` (`2024`) de l'archive WebOfTrust (`oct. 2026` `[5]`) et précisé `Tome 1 § 13.1` pour `W3C VC/DID` · **Verdict : supporté**

- **C16-32 (`L99–L103`, § 16.2.2)** — *Affirmation :* Limite intra-domaine de `SPIFFE` en inter-organisations (`[1, 5]`) et formalisation (construction de synthèse du `Tome 1`, ch. 16) du **passeport virtuel d'agent à quatre pièces** (`AgentCard` JWS/JCS `[7, 8, 11]`, inscription au registre `[3, 9]`, chaîne de mandat `→ Chapitre 17`, attestations de conformité/environnement `[1, 4, 12]`), complété d'une cinquième pièce candidate `AIBOM` CycloneDX / `SLSA` (`[9]` Appendix B, `→ Chapitre 22`).
  - **Appui vérifié :** `SRC-046.txt` (`[1]`), `SRC-079.txt` (`[5]`), `Corpus/Tome 1` (`ch. 16`, `L3984–4025`), `SRC-005.txt` (`[7]`), `SRC-077.txt` (`[8]`), `SRC-083.txt` (`[11]`), `SRC-048.txt` (`[3]`), `SRC-055.txt` (`[9]` Appendix B L1556–1572), `SRC-010.txt` (`[4]`), `SRC-071.txt` (`[12]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-33 (`L105`, § 16.2.2)** — *Affirmation :* Aucun émetteur unique ni norme ratifiée ne délivre ce passeport complet fin 2026, et aucune institution canadienne recensée dans `AIBanks.ca` `[12]` ni au `Tome 1` (§ 13.5, degré 3) ne documente de déploiement `W3C DID/VC` inter-firmes `[5, 12]` ; l'architecture instaure quatre substituts provisoires internes (`Tome 1` § 16.1.1) pour soutenir avant le `1er mai 2027` les attentes `BSIF E-23` et, sous réserve explicite (`statut F` `AO-01` sur `lautorite.qc.ca`), l'échéance attendue de l'AMF `[12]`.
  - **Appui vérifié :** `SRC-071.txt` (`[12]` L5, L123, L263–276), `Corpus/Tome 1` (`§ 13.5` L3584, `§ 16.1.1` L4027–4041), `recherche/registre-statut-f.json` (`L62–70`), `ch16-sources.md` (`L147`).
  - **Passe initiale :** reformulée · **Action :** aligné la formulation sur le degré 3 d'absence documentée (`Tome 1` § 13.5) et sur l'index public `AIBanks.ca` `[12]` · **Verdict : supporté**

- **C16-34 (`L107`, § 16.2.2)** — *Affirmation :* Énumération des quatre substituts provisoires internes (`Tome 1` § 16.1.1) : `AgentCard` vérifiée contre magasin d'ancrage interne, registre d'entreprise, échange OAuth intra-domaine (`→ Chapitre 17`) et inventaire documentaire des modèles/agents `[11, 12]`, sans résoudre l'admission ouverte `KYA` (`→ Chapitre 17`, Palier 3).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 16.1.1`, `Tableau 16.2`, `L4031–4040`), `SRC-083.txt` (`[11]`), `SRC-071.txt` (`[12]`).
  - **Passe initiale :** réancrée · **Action :** explicité le rattachement au `Tome 1` (§ 16.1.1) · **Verdict : supporté**

- **C16-35 (`L109`, § 16.2.2)** — *Affirmation :* Préparation B2B au Palier 3 (`CAP-006`, `CAP-041`, `POR-013`) reposant sur **GLEIF vLEI** (`ISO 17442-3` de `2024`, écosystème `KERI`/`ACDC` de WebOfTrust archivé au `15 octobre 2026` `[5]`) et `W3C VC 2.0` (`Tome 1` § 13.1), reliant `QVI → LE → OOR/ECR` (délivrés à des personnes physiques mandatées `[5]`, sur lesquelles `CAP-041` arrime l'agent délégué) afin de vérifier l'identité légale en `A2A`/`EDC`/`ODRL` (`← Chapitre 08`) sans grattage d'écran `[5, 11]`.
  - **Appui vérifié :** `SRC-079.txt` (`[5]` L5–10, L118–122, L343–393), `Corpus/Tome 1` (`§ 13.1`), `Corpus/Tome 4` (`CAP-006`, `CAP-041`, `POR-013`), `SRC-083.txt` (`[11]`).
  - **Passe initiale :** réancrée · **Action :** distingué l'année de publication `ISO 17442-3` (`2024`) de l'archive WebOfTrust (`15 oct. 2026`) et précisé que `OOR`/`ECR` sont délivrés à des personnes physiques mandatées (`[5]`) · **Verdict : supporté**

- **C16-36 (`L111`, § 16.2.2)** — *Affirmation :* Activation conditionnelle du Palier 3 gouvernée par les signaux `SIG-007` et `SIG-103` (`→ Chapitre 31`), avec posture pragmatique « attendre » sur `DID`/`did:wba` et isolation derrière interfaces neutres `[5]`.
  - **Appui vérifié :** `Corpus/Tome 4` (`SIG-007`, `SIG-103`), `Corpus/Tome 1` (`§ 13.5`), `SRC-079.txt` (`[5]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C16-37 (`L113–L117`, Figure 3 & AO-01)** — *Affirmation :* La Figure 3 (`SCH-16-03.svg`) illustre les trois couches (`SPIFFE`/`SPIRE` interne, `4` substituts provisoires au `1er mai 2027`, activation `vLEI`/`VC 2.0` au Palier 3) et la discipline `AO-01` consigne les trois exclusions `statut F` compensées par `[9, 10]`, `[5]` et `[12]`.
  - **Appui vérifié :** `specs/manifest.json` (`ch16`, `SCH-16-03`), `schemas/SCH-16-03.puml`, `schemas/rendus/SCH-16-03.svg`, `sources/ch16-sources.md` (`L143–147`), `recherche/registre-statut-f.json` (`L40–48`, `L62–70`, `L183–191`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 16.3 — Synthèse architecturale, livrables, portes et invariants (`L121–L140`, Tableau 16.3)

- **C16-38 (`L121–L134`, § 16.3 & Tableau 16.3)** — *Affirmation :* Interfaces amont/aval étanches (`← Ch. 05, 07, 08, 09, 12, 15, 25`, `[12]` cantonné aux attentes prudentielles canadiennes et québécoises en recollation `G3` `seed 20270902` avec retrait de `[1]` sur la liste d'entrées inter-chapitres ; `→ Ch. 17, 18, 21, 22, 31`), Tableau 16.3 des quatre livrables d'ingénierie et critères vérifiables `G0`–`G1` (`EXIG-IAM-01..07/14/15`, `EXIG-A2A-03/09`, `EXIG-INT-21`, `ADR-018`, `CAP-006/035/041`, `DEC-012`, `PRI-004`, `PRIN-03`, `PRR S-01/S-02`, `SIG-007/103`, `[1, 2, 5, 7, 8, 9, 11, 12]`), et absence de blocs de code écrits à la main (`AO-08`, renvoi à `a2a_card.py` scellé en `G0` au `Chapitre 08`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`A.6.1`, `A.6.3`, `A.6.7`), `aq/rapports-g0.json` (`G0-EX-CH01-04`), `Tomes/Tome 8/.../a2a_card.py`, `SRC-046.txt`, `SRC-047.txt`, `SRC-079.txt`, `SRC-005.txt`, `SRC-077.txt`, `SRC-055.txt`, `SRC-083.txt`, `SRC-071.txt`.
  - **Passe initiale :** conforme · **Action :** en recollation `G3` (`seed 20270902`), retiré `[1]` de la phrase d'entrées inter-chapitres (`L123`) pour cantonner `[12]` aux attentes prudentielles `← Chapitre 25` · **Verdict : supporté**

- **C16-39 (`L138–L142`, Trois invariants exécutables)** — *Affirmation :* Encadré des trois invariants exécutables du Chapitre 16 : (1) zéro secret statique et double parrainage `SIRH` (`< 72 h`) avec `SBB-SECRETS-VAULT` (`EXIG-IAM-01..07`, `PRR S-01`) ; (2) attestation éphémère en mémoire (`X.509-SVID` `TTL ≤ 1 h` via `SPIRE` et `Envoy SDS`) et domaines isolés (`EXIG-IAM-14/15`, `RFC 9334`) ; (3) ancrage hors protocole de l'`AgentCard`, revalidation `ETag`/`Cache-Control`, échec en mode fermé sur rupture de statut ou d'horloge externe (`EXIG-A2A-03/04`, `EXIG-IAM-18`), encapsulation des annuaires commerciaux et crible `Q-A`..`Q-E` (`RFC 7515`, `RFC 8785`).
  - **Appui vérifié :** Cohérence intégrale avec `§ 16.1`–`§ 16.3`, `registre/matrice-exig-prr-c40.json`, `SRC-046.txt`, `SRC-010.txt`, `SRC-005.txt`, `SRC-077.txt`, `SRC-083.txt`.
  - **Passe initiale :** conforme · **Action :** mise à jour post-G4 (`EXIG-A2A-03/04`, `EXIG-IAM-18`) · **Verdict : supporté**

- **C16-40 (`L74–L75`, § 16.2.1 — ajout post-G4)** — *Affirmation :* `a2a_card.py` évalue structure, flux OAuth, épinglage `jku`/`kid` et signature `ES256` sur `JCS` en retournant un `card_etag` déterministe sans état temporel ; la politique `TTL` s'exerce hors protocole sur le magasin d'ancrage et la passerelle `PEP` (`EXIG-A2A-03`, `EXIG-A2A-04`, `Tome 2 § 6.6`) via `ETag` fort, `Cache-Control` (`max-age`) et rejet de régression `SemVer`, avec échec en mode fermé sous `EXIG-IAM-18` (`Tome 2 § 9.4`) sur rupture de statut, du cache `JWKS` ou de l'horloge externe (politique distribuée échue limitant au plus à `P0`).
  - **Appui vérifié :** `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/a2a_card.py`, `Corpus/Tome 2` (`§ 6.6` `L2167`, `L2193`, `L2201` ; `§ 9.4`), `SRC-083.txt` `[11]`, `SRC-077.txt` `[8]`.
  - **Passe initiale :** ajout post-G4 · **Action :** vérification différentielle `G2` · **Verdict : supporté**

- **C16-41 (Révision `REV-04` : `PRD-L2-012`, `020`, `021`, `023`, `PRD-L4-002`, `REF-003`)** — *Affirmation :* Uniformisation des figures en `Figure 52`..`Figure 54` (`SCH-16-01` corrigé en `OAuth 2.0 (BCP 240 / RFC 9700)`, `SCH-16-02` aligné sur `A2A v1.0.0 / v1.0.1`), réconciliation explicite `0/15` (`3 × 5`, distinct de quinze produits) et verdict `1/4` du passeport virtuel (`Tome 1 ch. 16`, repérage `arXiv:2509.01063`), intégration de `EXIG-IAM-09`, `EXIG-IAM-16`, `NIST SP 800-207`, `ANC-022` et `SIG-003`, encadré `Clause non-avis (AO-05)`, francisation `playbooks` → `procédures de réponse`, et qualification explicite de `AIBanks.ca` (`[12]`, `SRC-071`) comme source secondaire (portail AMF en statut `F`).
  - **Appui vérifié :** `Compendium/prd.md`, `Corpus/Tome 1` (`ch. 14`, `ch. 16`), `schemas/SCH-16-01.svg`, `schemas/SCH-16-02.svg`, `SRC-071.txt` (`[12]`), `SRC-133.txt` (`[6]`).
  - **Passe initiale :** ajout `REV-04` · **Action :** vérification différentielle `REV-04` · **Verdict : supporté**

- **C16-42 (`§ 16.1`, `§ 16.2.1`)** — *Affirmation :* L'architecture d'identité dissocie l'infrastructure d'automatisation gouvernée de l'agentivité des systèmes qui en émerge à l'exécution sur les référentiels d'entreprise : dépourvue de personnalité juridique propre, celle-ci requiert l'enchaînement `Q-A` à `Q-E` et une identité `NHI` cryptographiquement distincte (`WIMSE`/`SPIFFE` `[1, 3]`) rattachée à un parrain humain au `SIRH` (`JML < 72 h`) pour combler le déficit d'attribution `ASI03` `[9]`.
  - **Appui vérifié :** `SRC-046.txt` (`[1]`), `SRC-048.txt` (`[3]`), `SRC-055.txt` (`[9]`), `Tomes/Tome 1` (`ch. 14`), `Tomes/Tome 2` (`EXIG-IAM-03`, `EXIG-IAM-07`).
  - **Passe initiale :** ajout ciblé · **Action :** raccordement terminologique et `SIRH`/`IdP` ancré sur `[1, 3, 9]` · **Verdict : supporté**
