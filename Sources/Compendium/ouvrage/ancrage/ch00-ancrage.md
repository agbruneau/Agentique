# Journal d'ancrage atomique Wyvern — Chapitre 00 (`00 - Liminaire.md`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/00 - Liminaire.md` (`00-liminaire`)
- **Agent auditeur :** `wyvern-00` (auditeur atomique Wyvern neuf, barrière `G2` selon `AO-07`, distinct de la rédaction)
- **Base fermée autorisée :** `Compendium/ouvrage/sources/ch00-sources.md` (`[1]`–`[19]`), textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt`, registres SSOT `Compendium/ouvrage/registre/{ancres-chronologiques.json, faits-empiriques.json, concordance-taxonomies.json, matrice-exig-prr-c40.json, mindmap-complet.json, glossaire-termes.json}`, manifestes `Compendium/ouvrage/recherche/{manifeste-sources-sha256.json, registre-statut-f.json}`, schémas `Compendium/ouvrage/schemas/SCH-00-01..04` et rapport `Compendium/ouvrage/aq/rapports-g0.json`
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Passe G2 initiale (supportés) :** 53
- **Rectifications appliquées dans `00 - Liminaire.md` :** 10 écarts initiaux de formulation ou d'attribution corrigés directement sur pièces (`L13`, `L15`, `L19`, `L45`, `L80`, `L92`, `L96`, `L98`) sans casser `CA-01`–`CA-11`, `CA-21` ou `CA-22`, sans ajout de source et sans contournement du `statut F`
- **Verdict final — supportés :** 63 / 63 (100,0 %)

---

## 1. Synthèse de la vérification par section

| Section (`00 - Liminaire.md`) | Affirmations auditées | Rectifications G2 appliquées | Verdict final |
|---|---:|---:|---|
| En-tête, Question directrice & Périmètre (`L1–L9`) | 9 | 0 | 9 / 9 (`100,0 %`) |
| `0.1` Problématique industrielle (`L11–L21`) | 12 | 4 (`L00-11`, `L00-12`, `L00-14`, `L00-19`) | 12 / 12 (`100,0 %`) |
| `0.2` Doctrine 80/20, `DIV-02` & `Tableau 0.1` (`L23–L53`) | 14 | 1 (`L00-34`) | 14 / 14 (`100,0 %`) |
| `0.3` Graphe des `12` domaines & `616` liens (`L55–L69`) | 6 | 0 | 6 / 6 (`100,0 %`) |
| `0.4` Gouvernance `AE ↔ AS` & `Tableau 0.2` (`L71–L88`) | 10 | 1 (`L00-45`) | 10 / 10 (`100,0 %`) |
| `0.5` Cadre `2023–2035`, `DAPP` & `G0`–`G5` (`L90–L110`) | 12 | 4 (`L00-53`, `L00-57`, `L00-58`, `L00-59`) | 12 / 12 (`100,0 %`) |
| **Total** | **63** | **10** | **63 / 63 (`100,0 %`)** |

---

## 2. Journal détaillé des affirmations atomiques (`L00-01` à `L00-63`)

### 2.0 En-tête, Question directrice et périmètre probatoire (`L1–L9`)

- **L00-01** (`L3`) — *Énoncé :* Question directrice portant sur la transformation de modèles probabilistes faillibles en Systèmes d'agentivité fiables, soutenables, réversibles et susceptibles d'homologation vérifiable au gel du `2 décembre 2026`.
  - *Preuve primaire :* `specs/manifest.json` (`freeze_date: "2026-12-02"`, `subtitle`), `recherche/manifeste-sources-sha256.json`.
  - Verdict : supporté
- **L00-02** (`L5`) — *Énoncé :* Traité, schémas vectoriels et trousse compagnon figés au `2 décembre 2026` pour une parution en `janvier 2027` (`[8, 12, 13, 14, 15]`).
  - *Preuve primaire :* `specs/manifest.json` (`edition_year: 2027`, `freeze_date: "2026-12-02"`), `ch00-sources.md` (`[8, 12, 13, 14, 15]`).
  - Verdict : supporté
- **L00-03** (`L5`) — *Énoncé :* Clause non-avis (`AO-05`, `DC-P01`, `DC-P12`) précisant que la conformité aux barrières `G0`–`G5` ne vaut ni avis juridique, ni opinion actuarielle, ni certification réelle au sens de la Loi 25 (`[14]`), BSIF E-23 (`[13]`), AMF ou EU AI Act (`[15]`).
  - *Preuve primaire :* `SRC-055.txt` (`L13–L16`, modèle d'avertissement non-avis), `registre/glossaire-termes.json` (`Clause non-avis` assignée à `00-liminaire`), `SRC-063.txt`, `SRC-065.txt`, `SRC-060.txt`.
  - Verdict : supporté
- **L00-04** (`L5`) — *Énoncé :* Licence `CC BY 4.0` pour le texte et les `115` figures, et licence `MIT` pour l'outillage déterministe et la trousse exécutable du Tome 8.
  - *Preuve primaire :* `specs/manifest.json` (`license_mode`: `CC-BY-4.0` et `MIT`; `figures` : `115` entrées), `aq/rapports-g0.json` (`spdx_check.license_target: "MIT"`, `50` fichiers conformes).
  - Verdict : supporté
- **L00-05** (`L7`) — *Énoncé :* Consolidation des travaux d'architecture, de génie logiciel, de sécurité hors modèle, de conformité et de prospective à l'intention des dirigeants, `AE`, `AS`, `RSSI`, `SRE` et conseillers juridiques.
  - *Preuve primaire :* `specs/manifest.json` (`part_titles` `I`–`XII`, `units` `ch01`–`ch36`), `registre/mindmap-complet.json` (`D01`–`D12`).
  - Verdict : supporté
- **L00-06** (`L7`) — *Énoncé :* Adoption de la force normative RFC 2119 (`[19]`) : `DOIT`/`DOIVENT` (obligation stricte), `NE DOIT PAS` (interdiction absolue), `DEVRAIT` (recommandation motivée).
  - *Preuve primaire :* `SRC-125.txt` (`L30–L45` : `MUST`, `MUST NOT`, `SHOULD`), `registre/matrice-exig-prr-c40.json` (`255 DOIT / 34 NE_DOIT_PAS / 16 DEVRAIT`).
  - Verdict : supporté
- **L00-07** (`L9`) — *Énoncé :* Corpus fermé de sources primaires ouvertes authentifiées par empreinte `SHA-256` et gelées au `2 décembre 2026`.
  - *Preuve primaire :* `recherche/manifeste-sources-sha256.json` (`metadata_only_pct: 0.0`, `freeze_date: "2026-12-02"`), `ch00-sources.md` (`[1]`–`[19]` en statut `L+`).
  - Verdict : supporté
- **L00-08** (`L9`) — *Énoncé :* Règle `AO-01` excluant toute ressource bloquée (`HTTP 401`, `403`, `429`, `451`, WAF, mur payant) en statut F hors preuve, au profit de documents ouverts complets (`[5, 6, 8, 14]`).
  - *Preuve primaire :* `recherche/registre-statut-f.json` (`included_in_evidence: false` sur toutes les entrées bloquées), `SRC-055.txt` (`[8]`), `SRC-014.txt` (`[5]`), `SRC-015.txt` (`[6]`), `SRC-063.txt` (`[14]`).
  - Verdict : supporté
- **L00-09** (`L9`) — *Énoncé :* Échéances `2027–2035` postérieures au gel présentées comme obligations futures à préparer (`[13, 15, 16]`).
  - *Preuve primaire :* `registre/ancres-chronologiques.json` (`total_jalons: 86`, jalons `2027`–`2035`), `SRC-065.txt`, `SRC-060.txt`, `SRC-050.txt`.
  - Verdict : supporté

### 2.1 Section `0.1` — Problématique industrielle (`L11–L21`)

- **L00-10** (`L13`) — *Énoncé :* Passage d'un assistant conversationnel consultatif à un **Système d'agentivité** en boucle fermée percevant un état métier, appelant des outils et modifiant des données d'entreprise.
  - *Preuve primaire :* `registre/glossaire-termes.json` (`Système d'agentivité`), `SRC-027.txt`, `SRC-066.txt` (`L7`, `L162–L163`).
  - Verdict : supporté
- **L00-11** (`L13`) — *Énoncé :* Statistique Canada T2 2026 (`[5]`, tableau `33-10-1167-01`) mesure `19,2 %` de recours à l'IA au Canada et `40,4 %` en finance et assurances ; T3 2026 (`[6]`, tableau `33-10-1207-01`) mesure `25,2 %` et `35,5 %` prévus.
  - *Preuve primaire et rectification :* `SRC-014.txt` (`33101167.csv` : `19.2` Canada ensemble des industries, `40.4` Finance et assurances) et `SRC-015.txt` (`33101207.csv` : `25.2` et `35.5`). En passe initiale, la phrase attribuait à l'ensemble `[5, 6, 7]` des « déficits de gouvernance » absents des tableaux CSV `33-10-1167-01` et `33-10-1207-01` ; le manuscrit a été recentré sur les taux exacts mesurés par `[5]` et `[6]`.
  - Verdict : supporté
- **L00-12** (`L13`) — *Énoncé :* Analyse de la Banque du Canada (`Staff Analytical Paper 2026-22`, `[7]`) : usage opérationnel marqué limité à `8 %` des entreprises sondées contre `70 %` d'usage personnel hebdomadaire chez les répondants, freiné par l'utilité perçue, l'incompatibilité logicielle, les compétences, les coûts et les obstacles réglementaires.
  - *Preuve primaire et rectification :* `SRC-016.txt` (`L94` : `70% of respondents`, `L158–L160` : `8% ... significant use`, `Chart 3` `L230–L248` : `AI is not useful to my firm`, `lack of skilled staff`, `incompatibility`, `costs too high`, `regulatory obstacles`). La rédaction initiale a été resserrée sur ces constatations exactes de `SRC-016.txt`.
  - Verdict : supporté
- **L00-13** (`L15`) — *Énoncé :* Étude `MAP` (`[1]`) : `68 %` des déploiements en production exécutent au plus `10` étapes avant intervention humaine et `80 %` (`16` études de cas sur `20`) reposent sur un flux structuré fixe.
  - *Preuve primaire :* `SRC-027.txt` (`L25` : `68% execute at most 10 steps before human intervention`, `L639` : `Eighty percent (16/20)`), `registre/faits-empiriques.json` (`FACT-MAP-STUDY`).
  - Verdict : supporté
- **L00-14** (`L15`) — *Énoncé :* Deloitte *TMT Predictions 2026* (`[4]`) signale un risque d'annulation dépassant `40 %` des initiatives agentiques d'ici 2027 en raison de dépenses imprévues, des défis de passage à l'échelle ou de risques inopinés (estimation Gartner dont le communiqué primaire demeure en statut F).
  - *Preuve primaire et rectification :* `SRC-011.txt` (`L443` : `more than 40% of today's agentic AI projects could be cancelled by 2027, due to unanticipated cost, complexity of scaling, or unexpected risks`), `registre/faits-empiriques.json` (`FACT-GARTNER-ABANDON-2027`), `recherche/registre-statut-f.json`. Les motifs exacts de `SRC-011.txt` ont remplacé l'ancienne formule générique de la passe initiale.
  - Verdict : supporté
- **L00-15** (`L17`) — *Énoncé :* Attrition multiplicative d'une chaîne séquentielle d'étapes probabilistes sans vérification déterministe selon la loi de Lusser.
  - *Preuve primaire :* `registre/faits-empiriques.json` (`FACT-LUSSER-10-STEPS`, source `SRC-024`), `registre/glossaire-termes.json` (`loi de Lusser`).
  - Verdict : supporté
- **L00-16** (`L17`) — *Énoncé :* Taxonomie `MAST` (`[2]`) : `41 %` à `86,7 %` d'échecs sur `1 642` traces multi-agents à travers `7` cadriciels et `14` modes de défaillance.
  - *Preuve primaire :* `SRC-028.txt` (`L24–L30`, `L106–L128` : `1642 MAS execution traces`, `41% to 86.7% failure rate`, `7 popular MAS frameworks`, `14 distinct failure modes`), `registre/faits-empiriques.json` (`FACT-MAST-FAILURES`).
  - Verdict : supporté
- **L00-17** (`L17`) — *Énoncé :* Production par un agent probabiliste de réponses syntaxiquement valides mais affectées d'une distorsion sémantique silencieuse, vecteurs recensés parmi `ASI01` à `ASI10` de l'*OWASP Top 10 for Agentic Applications 2026* (`[8]`).
  - *Preuve primaire :* `SRC-055.txt` (`L50–L166`, `ASI01`–`ASI10`).
  - Verdict : supporté
- **L00-18** (`L19`) — *Énoncé :* Recensement MCP d'Obada Kraishan (`[3]`) : `21 643` serveurs et `72 606` versions ; parmi `8 900` multi-versions, `51,09 %` changent entre versions, `40,58 %` présentent une dérive sémantique silencieuse et `4,16 %` (`370` serveurs) redirigent leur point d'accès distant vers un autre hôte.
  - *Preuve primaire :* `SRC-057.txt` (`L12–L20`, `L554–L558`, `Table 5` `L589–L590`), `registre/faits-empiriques.json` (`FACT-MCP-DRIFT-4058`).
  - Verdict : supporté
- **L00-19** (`L19`) — *Énoncé :* Parmi les `6 699` serveurs multi-versions du corpus scanné, la dérive silencieuse s'associe de manière corrélationnelle — sans lien causal identifié — à une cote près de trois fois plus élevée de détection grave (`OR = 2,96`) (`[3]`).
  - *Preuve primaire et rectification :* `SRC-057.txt` (`L639–L642` : `6,699 multi-version servers inside the scan population`, `2.96 times the odds of a high-severity finding`, `The design is correlational and the direction is not identified`). Le passage initial rattachait de manière ambiguë et causale `OR = 2,96` à la redirection d'hôte (`4,16 %`) ; la rédaction a été rectifiée pour refléter le protocole corrélationnel exact de `SRC-057.txt`.
  - Verdict : supporté
- **L00-20** (`L19`) — *Énoncé :* Exposition au verrouillage propriétaire sur le plan de contrôle des suites infonuagiques fermées, rendant opaques les journaux et coûteuse la réversibilité.
  - *Preuve primaire :* `registre/mindmap-complet.json` (`D03` `THM_anti-verrouillage-standards`), `registre/matrice-exig-prr-c40.json` (`EXIG-APP-07..17`).
  - Verdict : supporté
- **L00-21** (`L21`) — *Énoncé :* Critères de valeur d'une initiative agentique : preuve répétée des invariants métier, traçabilité et révocabilité des appels d'outils, dépendance fournisseur bornée en temps et en coût.
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`PRI-001`–`PRI-010`, `EXIG-APP-07..17`, `EXIG-FIN-01..10`).
  - Verdict : supporté

### 2.2 Section `0.2` — Doctrine hybride 80/20, concordance `DIV-02` et *Tableau 0.1* (`L23–L53`)

- **L00-22** (`L25`) — *Énoncé :* Heuristique de conception `80/20` du traité motivée par `MAP` (`[1]`) et l'encadrement prudentiel (`[12]`), plaçant environ `80 %` de la valeur d'ingénierie dans un exosquelette déterministe possédé et confinant l'inférence probabiliste aux `20 %` centraux.
  - *Preuve primaire et rectification (G3 Passe 2 `seed 20270902`) :* `SRC-027.txt` (`80 %` flux structurés fixes), `SRC-066.txt` (`L27`, `L65`, `L175` : `AI harnessing`), `registre/glossaire-termes.json` (`Partition 80/20`). Formulation resserrée en `00 - Liminaire.md` L25 afin de distinguer explicitement l'heuristique doctrinale du traité de ses inspirations `MAP` `[1]` et `MAS` `[12]`.
  - Verdict : supporté
- **L00-23** (`L25`) — *Énoncé :* Noyau déterministe gouvernant routage, machines à états, schémas, autorisations cryptographiques, arithmétique monétaire exacte, idempotence et abstention ; séparation entre proposition du modèle, contrôle du code et visa humain sur mutations critiques.
  - *Preuve primaire :* `registre/glossaire-termes.json` (`Harnais déterministe`, `noyau de contrôle déterministe`), `registre/matrice-exig-prr-c40.json` (`EXIG-ARC-02..07`, `EXIG-ORC-15..22`, `EXIG-AUT-09..13`).
  - Verdict : supporté
- **L00-24** (`L27`) — *Énoncé :* **Tissu conjonctif agentique** reliant `SoE`, `System of Action`, `SoR` sous couches anti-corruption et plans transversaux de contrôle identitaire, probatoire et décisionnel.
  - *Preuve primaire :* `registre/glossaire-termes.json` (`tissu conjonctif agentique` assigné à `00-liminaire`, `Système d'agentivité`, `couche anti-corruption`).
  - Verdict : supporté
- **L00-25** (`L27`) — *Énoncé :* Médiation hors modèle des appels verticaux `MCP 2026-07-28` (`[9, 10]`) et horizontaux `A2A v1.0.1` (`[11]`), avec rejet avant appel au modèle de tout outil dont la description ou le schéma varie sans signature vérifiée (`[3, 9]`).
  - *Preuve primaire :* `SRC-072.txt` (`L62–L75`, `L305`), `SRC-074.txt`, `SRC-083.txt` (`L2004–L2062`), `SRC-057.txt` (`L771–L772`).
  - Verdict : supporté
- **L00-26** (`L29–L31`) — *Énoncé :* Cinq critères permanents d'arbitrage architectural (`C04`) pour `Acheter`, `Assembler` ou `Construire` : neutralité du plan de contrôle, déterminisme des frontières/invariants, tolérance aux pannes/idempotence/compensation, `CPO` et coût/délai vérifiables de sortie.
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`C04`, `mappings`), `registre/concordance-taxonomies.json`.
  - Verdict : supporté
- **L00-27** (`L33`) — *Énoncé :* Fermeture de `DIV-02` reliant le modèle pivot à `5` couches (`C1`–`C5`) aux `6` vraies couches de `CRE-IA-2026-01 v1.2` (`305` exigences `EXIG-*`) et aux `3` plans transversaux (`Plan A`, `Plan B`, `Plan C`).
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`div_02`, `decoupages_architecturaux_t5_a1`), `registre/matrice-exig-prr-c40.json` (`exig_cre_ia_v1_2.total: 305`).
  - Verdict : supporté
- **L00-28** (`L35`) — *Énoncé :* Trois rectifications `DIV-02` : modèles et bac à sable en Couche 3 (non Couche 6) ; connaissance et sémantique sur Couches 2, 3 et 5 ; `SoR` en Couche 6 sous encapsulation `ACL`.
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`div_02.trois_rectifications`, `L9–L13`).
  - Verdict : supporté
- **L00-29** (`L35`) — *Énoncé :* Bilan capacitaire : `52` capacités `CAP` (`42` invariantes, `10` conditionnelles) et `24` extensions `PEX` dont `11` comblent les `5` lacunes normatives (`CAP-025`, `CAP-028`, `CAP-033`, `CAP-046`, `CAP-052`).
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`div_02.bilan_chiffre`, `L20–L35`), `registre/matrice-exig-prr-c40.json` (`cap_52`, `pex_24`).
  - Verdict : supporté
- **L00-30** (`L41`) — *Énoncé :* `DISC-01` (*Tableau 0.1*) : distinction entre automatisation pure sans modèle et profil `L0–L1` en lecture filtrée ; `L0–L4` gradue les droits de mutation et d'effet externe (`[1, 12]`).
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`DISC-01`, `L188–L205`), `SRC-027.txt`, `SRC-066.txt`.
  - Verdict : supporté
- **L00-31** (`L42`) — *Énoncé :* `DISC-02` (*Tableau 0.1*) : table d'équivalence conservée en portefeuille (`N0–N4`, `R1–R4`, `Classes 1–6`, `Stades 0–4`, `Paliers 1–3`) et usage exclusif dans le noyau logiciel de `BLOQUANT`, `OBLIGATOIRE`, `RECOMMANDE` et `P0–P3`.
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`DISC-02`, `L207–L229`).
  - Verdict : supporté
- **L00-32** (`L43`) — *Énoncé :* `DISC-03` (*Tableau 0.1*) : ancrage simultané dans Plans `A`, `B`, `C`, `5` couches `C1–C5` et `4` paquets techniques de la trousse alignés sur `5` emplacements `SBB` vérifiés.
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`DISC-03`, `L231–L253`), `registre/matrice-exig-prr-c40.json` (`cinq_sbb`).
  - Verdict : supporté
- **L00-33** (`L44`) — *Énoncé :* `DISC-04` (*Tableau 0.1*) : neutralité de notation entre `ArchiMate 3.2` et `ArchiMate 4.0 C260` sans outil commercial obligatoire, préservant la licence `MIT` et les rendus `PlantUML` et `SVG`.
  - *Preuve primaire :* `registre/concordance-taxonomies.json` (`DISC-04`, `L255–L272`).
  - Verdict : supporté
- **L00-34** (`L45`) — *Énoncé :* `DISC-05` (*Tableau 0.1*) : épinglage sur `MCP 2026-07-28` (`5f5440bb`) en `Streamable HTTP` sans état, rejet du flux `HTTP+SSE`, adaptateur `SEP-3398`, en-têtes `MCP-Protocol-Version`, `Mcp-Method` et `Mcp-Name` jusqu'à la cible du `30 mars 2027` (`[9, 10]`).
  - *Preuve primaire et rectification :* `registre/concordance-taxonomies.json` (`DISC-05`, `L274–L291`), `SRC-072.txt`, `SRC-074.txt` (`L252–L293` exigeant `MCP-Protocol-Version`, `Mcp-Method` et `Mcp-Name`), `SRC-082.txt` (`L17`, `L203` : cible `30 mars 2027`). En passe G2, `MCP-Protocol-Version` a été ajouté aux deux en-têtes initialement cités et l'échéance `30 mars 2027` a été explicitement qualifiée de cible.
  - Verdict : supporté
- **L00-35** (`L49–L53`) — *Énoncé :* *Figure 1* (`SCH-00-01`) oppose `Z1` (usagers), `Z2` (exosquelette déterministe à `42` capacités invariantes et harnais à huit étapes), `Z3` (cœur cognitif substituable) et `Z4` (systèmes d'enregistrement protégés).
  - *Preuve primaire :* `schemas/rendus/SCH-00-01.svg` (`Z1`–`Z4`, `42 CAP`, `harnais à 8 étapes`, `20 %`, `SoR` / `ACL`).
  - Verdict : supporté

### 2.3 Section `0.3` — Graphe des douze domaines et chaîne de confiance (`L55–L69`)

- **L00-36** (`L57`) — *Énoncé :* Cartographie formée de `12` domaines (`D01`–`D12`), `36` chapitres (`CH-01`–`CH-36`), `71` familles, `260` thèmes canoniques et `616` interrelations typées.
  - *Preuve primaire :* `registre/mindmap-complet.json` (`totals` : `domains: 12`, `subdomains: 36`, `families: 71`, `themes: 260`, `relations: 616`), `specs/manifest.json` (`36` unités `ch01`–`ch36`).
  - Verdict : supporté
- **L00-37** (`L57`) — *Énoncé :* Répartition des `616` interrelations : `132` opérationnalisation, `93` dépendances techniques, `82` encadrements normatifs, `81` atténuations de risque, `63` amplifications de synergie, `62` tensions d'arbitrage, `52` projections temporelles et `51` concordances inter-tomes.
  - *Preuve primaire :* `registre/mindmap-complet.json` (décompte exact sur les `616` objets `relations[].type`).
  - Verdict : supporté
- **L00-38** (`L59`) — *Énoncé :* Dix premiers carrefours relationnels et leurs degrés : `BSIF E-23` (`30` `[13]`), `MCP 2026-07-28` (`25` `[9, 10]`), `FinOps FOCUS v1.4` (`24` `[17]`), passerelle `PEP` (`24`), porte `305 EXIG × 75 PRR` (`23`), délégation 2e saut (`21`), `ML-DSA` / `SLH-DSA` (`21` `[16]`), supervision humaine (`20`), prévention verrouillage (`20`) et `OWASP ASI01–ASI10` (`19` `[8]`).
  - *Preuve primaire :* `registre/mindmap-complet.json` (comptage des degrés incidents sur `relations[]` : `THM_bsif-e-23: 30`, `THM_protocole-mcp: 25`, `THM_passerelle-mcp-ai-gateway: 24`, `THM_finops-focus-cpo: 24`, `THM_exigences-cre-ia-305: 23`, `THM_post-quantique-ml-dsa-slh-dsa: 21`, `THM_delegation-obo-deux-sauts: 21`, `THM_anti-verrouillage-standards: 20`, `THM_supervision-hitl-hotl-abstention: 20`, `THM_injection-indirecte-prompt: 19`).
  - Verdict : supporté
- **L00-39** (`L61`) — *Énoncé :* Progression des Parties I à V (`D01`–`D05`, chapitres `01–15`) : épistémologie/Lusser/Coase, partition `80/20`/harnais/`L0–L4`/`42 CAP`, tissu conjonctif protocolaire/sémantique/`CoALA`/`ACL`, orchestration sobre `OO1–OO4` et sagas compensables.
  - *Preuve primaire :* `specs/manifest.json` (`part_titles` `I`–`V`, `ch01`–`ch15`), `registre/mindmap-complet.json` (`domains_meta` `D01`–`D05`).
  - Verdict : supporté
- **L00-40** (`L63`) — *Énoncé :* Progression des Parties VI à XII (`D06`–`D12`, chapitres `16–36`) et `Annexes A` à `E` : `NHI`/délégation/`PQC`, `OPA/Rego` (`default allow := false`)/Règle de deux/confinement, double couloir/`EvalOps`/`FinOps`, droit QC/CA/UE, `5` profils/`3` blueprints `C01–C40`, trajectoire `2026–2035` et trousse/homologation `G0`–`G5`.
  - *Preuve primaire :* `specs/manifest.json` (`part_titles` `VI`–`XII`, `ch16`–`ch36`, `annexe-a`–`annexe-e`), `registre/matrice-exig-prr-c40.json` (`c01_c40_blueprints`).
  - Verdict : supporté
- **L00-41** (`L65–L69`) — *Énoncé :* Chaîne de confiance continue (*Figure 2*, `SCH-00-02`) reliant identité `NHI` / délégation `OBO` (`D06`), inspection `MCP` (`[9, 10]`) et `A2A v1.0.1` (`[11]`), passerelle `PEP` à neuf contrôles sous `OPA` fermé par défaut (`D03+D07`), approbation hors bande et double couloir probatoire (`D08+D09` `[12, 13, 14, 15]`).
  - *Preuve primaire :* `schemas/SCH-00-02.puml` (`Z1`–`Z3`, `N1`–`N10` : `NHI`, `OBO/DPoP`, `CIBA + FIDO2`, `PEP 9 contrôles`, `OPA default allow := false`, `OTel`, `JCS/SCITT`).
  - Verdict : supporté

### 2.4 Section `0.4` — Gouvernance duale `AE ↔ AS` et *Tableau 0.2* (`L71–L88`)

- **L00-42** (`L73`) — *Énoncé :* Contrat doctrinal permanent entre `AE` (trajectoire de portefeuille, arbitrage, `42` capacités invariantes, alignement multi-juridictions, portes) et `AS` (harnais `80/20`, façades `MCP 2026-07-28` `[9, 10]`, cartes `A2A v1.0.1` `[11]`, `OPA/Rego`, machines à états durables, bancs `EvalOps`).
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`principes_et_decisions.adr_31_sort`, rôles `AE` / `AS`), `SRC-072.txt`, `SRC-074.txt`, `SRC-083.txt`.
  - Verdict : supporté
- **L00-43** (`L75`) — *Énoncé :* Matrice en étoile à trois lignes (`1LoD`, `2LoD`, `3LoD`), six rôles cibles (`AE`, `AS`, `RSSI`, `SRE`, `Juridique`, `Direction`), unique responsable imputable et muraille interdisant à tout agent bâtisseur de modifier spécifications et tests vérificateurs.
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`A.2.2`, `EXIG-GOV-02..04`, `ADR-025`), `specs/manifest.json` (`production_mode`).
  - Verdict : supporté
- **L00-44** (`L79`) — *Énoncé :* Constance `pass^k` (`k >= 5`, `pass^5 >= 99 %` avant distillation `SLM`) et borne unilatérale de Wilson à `95 %` imposant `n >= ceil(3/p)` essais indépendants sans échec (`n = 300` donnant `0,8938 % < 1 %`).
  - *Preuve primaire :* `registre/faits-empiriques.json` (`FACT-WILSON-3P`), `registre/matrice-exig-prr-c40.json` (`PRR O-05`, `PRR F-15`, `EXIG-EVA-02`, `EXIG-EVA-03`), calcul direct (`0,893787 %` pour `n = 300`, `k = 0`, `z = 1,644854`).
  - Verdict : supporté
- **L00-45** (`L80`) — *Énoncé :* Normalisation des coûts (`BilledCost`, `EffectiveCost` sous `FOCUS v1.4` `[17]`) et comptabilisation interne en `\$ CA` par résultat métier conforme, avec alerte `80 %` et coupure atomique à `100 %`.
  - *Preuve primaire et rectification :* `SRC-023.txt` (`Publication version 1.4`, `BilledCost`, `EffectiveCost`), `registre/matrice-exig-prr-c40.json` (`EXIG-FIN-01..10`, `PRR O-09` `maxTotalCostCad`, `PRR O-12`, `C39–C40`). La rédaction du *Tableau 0.2* a été ajustée pour distinguer la normalisation `FOCUS v1.4` (`[17]`) de la devise de comptabilisation interne (`\$ CA`).
  - Verdict : supporté
- **L00-46** (`L81`) — *Énoncé :* Évaluation `default allow := false` sur `100 %` des appels mutatifs (`45/45` assertions `OPA` à `100,0 %` de couverture), retrait déterministe de la triade par session et séparation contrôle/données `CaMeL`.
  - *Preuve primaire :* `aq/rapports-g0.json` (`opa_check` : `missing_default_deny: []`, `coverage_pct: 100.0`, `tests_passed: 45`, `tests_failed: 0`), `registre/matrice-exig-prr-c40.json` (`EXIG-SEC-06`, `EXIG-SEC-07`, `PRR S-08`, `PRR S-09`), `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`).
  - Verdict : supporté
- **L00-47** (`L82`) — *Énoncé :* Portes bloquantes `PRR-75` : validation intégrale des `24` contrôles `[BLOQUANT]` sur `75` (`S:8`, `R:5`, `O:2`, `G:7`, `F:2`), des `305` exigences `EXIG-*` et des `40` critères des blueprints `C01–C40`.
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`prr_75.total: 75`, `blocking_count: 24`, décompte exact par grille `S:8`, `G:7`, `R:5`, `O:2`, `F:2` ; `exig_cre_ia_v1_2.total: 305` ; `C01`..`C40`).
  - Verdict : supporté
- **L00-48** (`L83`) — *Énoncé :* Révocation centralisée `SOC` en `< 10 s`, rétrogradation de palier `DAPP` en `< 60 s` et retour arrière automatisé `N-1` en `< 2 min`.
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`PRR S-14`, `POR-015`, `PRR O-08`).
  - Verdict : supporté
- **L00-49** (`L84`) — *Énoncé :* Cycle de vie `PKI` (`CA/B Forum`) : automatisation `ACME` pour la limite à `100 jours` (`15 mars 2027`) puis à `47 jours` avec réutilisation de validation à `10 jours` (`15 mars 2029`).
  - *Preuve primaire :* `SRC-053.txt` (`L199–L205`, `L2191`), `registre/ancres-chronologiques.json` (`ANC-023`, `ANC-030`), `registre/matrice-exig-prr-c40.json` (`CAP-033`).
  - Verdict : supporté
- **L00-50** (`L85`) — *Énoncé :* Transition post-quantique `FIPS 203/204/205` (`ML-DSA-65` à `3 309` octets, `ML-DSA-87` à `4 627` octets `[16]`) sur `G7 2030–2035`, avec prévention `HTTP 431` par référence `kid` et jetons de transaction `O(1)`.
  - *Preuve primaire :* `SRC-050.txt` (`L1317–L1321`), `SRC-052.txt` (`L190–L217`), `registre/faits-empiriques.json` (`FACT-PQC-SIGNATURE-SIZE`), `registre/matrice-exig-prr-c40.json` (`POR-007`, `EXIG-SEC-27`, `C27`).
  - Verdict : supporté
- **L00-51** (`L86`) — *Énoncé :* Réservation de dossiers formateurs dès que l'automatisation dépasse `70 %` (`INI-043`), exercices annuels de reprise sans agent et parade contre le biais `ASI09` (`[8]`).
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`INI-043`, `POR-009`, `POR-014`, `PRR G-11`, `PRR G-12`), `schemas/rendus/SCH-00-03.svg` (`> 70 % auto`), `SRC-055.txt` (`L154` `ASI09`).
  - Verdict : supporté

### 2.5 Section `0.5` — Cadre réglementaire `2023–2035`, `DAPP` et barrières `G0`–`G5` (`L90–L110`)

- **L00-52** (`L92`) — *Énoncé :* Loi 25 (`LQ 2021, c. 25`, `[14]`) encadrant depuis le `22 septembre 2023` les décisions fondées exclusivement sur un traitement automatisé (`art. 12.1`) : information contemporaine, communication sur demande des principaux facteurs et paramètres, observations et révision humaine.
  - *Preuve primaire :* `SRC-063.txt` (`L1542–L1555`, `L2485`), `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`, `ANC-114`).
  - Verdict : supporté
- **L00-53** (`L92`) — *Énoncé :* Dans les cas autres qu'une personne physique, Loi 25 (`[14]`) prévoit jusqu'à `10 M\$ CA` ou `2 %` du chiffre d'affaires mondial de l'exercice précédent (le plus élevé) en sanction administrative et de `15 000 \$ CA` à `25 M\$ CA` ou `4 %` (le plus élevé) en amende pénale, ainsi que l'`ÉFVP` avant transfert hors Québec et le droit à la portabilité depuis le `22 septembre 2024`.
  - *Preuve primaire et rectification :* `SRC-063.txt` (`L2283–L2287` `art. 90.12`, `L2328–L2333` `art. 91`, `L1581` `art. 17`, `L2521` `22 septembre 2024`). Le manuscrit a été rectifié pour préciser « dans les cas autres qu'une personne physique », « chiffre d'affaires mondial de l'exercice précédent (le plus élevé) » et le plancher pénal de `15 000 \$ CA`.
  - Verdict : supporté
- **L00-54** (`L94`) — *Énoncé :* Ligne directrice `E-23` du BSIF publiée le `11 septembre 2025` et entrant en vigueur le `1er mai 2027` (`[13]`), en convergence avec le bulletin technologique du BSIF du `13 juillet 2026` (`[12]`).
  - *Preuve primaire :* `SRC-065.txt` (`L15`, `L31`), `SRC-066.txt` (`L27`, `L37`, `L225`), `registre/ancres-chronologiques.json` (`ANC-103`).
  - Verdict : supporté
- **L00-55** (`L94`) — *Énoncé :* Repère attendu du `1er mai 2027` pour l'AMF sous réserve documentaire explicite, son portail direct demeurant consigné en statut F.
  - *Preuve primaire :* `recherche/registre-statut-f.json` (`https://lautorite.qc.ca/` `HTTP_403`), `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`), `SRC-071.txt` (`L271–L275`).
  - Verdict : supporté
- **L00-56** (`L96`) — *Énoncé :* Règlement européen `(UE) 2024/1689` (`[15]`) : obligations de transparence de l'article `50` applicables depuis le `2 août 2026`, exigences du chapitre III dont le contrôle humain (`art. 14`) et le système de gestion de la qualité (`art. 17`).
  - *Preuve primaire :* `SRC-060.txt` (`Article 14 Contrôle humain`, `Article 17 Système de gestion de la qualité`, `Article 50`, `Article 113`), `registre/ancres-chronologiques.json` (`2026-08-02-EU-AI-ACT-ART50`).
  - Verdict : supporté
- **L00-57** (`L96`) — *Énoncé :* Entrée en application des exigences du chapitre III de l'Annexe III au plus tard le `2 décembre 2027` et de l'Annexe I au `2 août 2028`, selon l'article `113` révisé par le règlement modificatif `(UE) 2026/1744` consigné au registre chronologique.
  - *Preuve primaire et rectification :* `registre/ancres-chronologiques.json` (`2027-12-02-EU-AI-ACT-ANNEXE-III`, `2028-08-02-EU-AI-ACT-ANNEXE-I`, `ANC-007`, `ANC-010`), `SRC-061.txt` (`L1851–L1853`). En passe initiale, ces deux dates étaient imputées au seul texte d'origine `(UE) 2024/1689` (`[15]`) alors que `SRC-060.txt` fixait `2 août 2026` et `2 août 2027` ; l'énoncé a été corrigé pour mentionner le contrôle humain (`art. 14`) et le règlement modificatif `(UE) 2026/1744`.
  - Verdict : supporté
- **L00-58** (`L98`) — *Énoncé :* Jalons canadiens `2028–2033` : modifications `ACVM 31-103` (`1er octobre 2028`), divulgation climatique de portée 3 `BSIF B-15` (fin `2028`) et clause statutaire de temporisation des lois financières fédérales (`30 juin 2033`).
  - *Preuve primaire et rectification :* `registre/ancres-chronologiques.json` (`2028-10-01-GESTION-PATRIMOINE-RETROFACTURATION`, `2028-12-31-BSIF-B15-PORTEE3`, `2033-06-30-LOIS-FINANCIERES-CANADA`), `SRC-069.txt`, `SRC-070.txt` (`L1740`). Le terme « décennale » a été remplacé par « statutaire » conformément aux pièces `SRC-070.txt` et `ancres-chronologiques.json`.
  - Verdict : supporté
- **L00-59** (`L98`) — *Énoncé :* Échéances techniques `PKI` (`100` jours au `15 mars 2027`, `47` jours au `15 mars 2029`), fenêtre minimale de douze mois avant retrait prévue par `MCP SEP-2596` (`28 juillet 2027` depuis `MCP 2026-07-28`) après la révision cible semestrielle instaurée par `SEP-3398` (`30 mars 2027`), et transition `PQC G7` (`2030–2035`) fondée sur les normes NIST dont `FIPS 204` (`[16]`).
  - *Preuve primaire et rectification :* `SRC-053.txt`, `SRC-081.txt` (`L106–L118`), `SRC-082.txt` (`L17`, `L203`), `SRC-052.txt`, `SRC-050.txt`, `registre/ancres-chronologiques.json`. Le passage initial a été resserré pour qualifier exactement la fenêtre de `12` mois de `SEP-2596` et la cible semestrielle `SEP-3398`.
  - Verdict : supporté
- **L00-60** (`L100`) — *Énoncé :* Trajectoire adaptative `DAPP` (`[18]`, Haasnoot, Warren et Kwakkel) structurée en rampe sans regret (`J1` `90 jours`, `J2` `9 mois`, `J3` `18 mois`) et trois paliers conditionnels (`P1` `2028–2029`, `P2` `2030–2032`, `P3` `2033–2035`).
  - *Preuve primaire :* `SRC-112.txt` (`L7–L32`, `L76–L86`), `registre/ancres-chronologiques.json` (`DAPP-T5-01`–`DAPP-T5-06`, `L1315–L1409`).
  - Verdict : supporté
- **L00-61** (`L100–L104`) — *Énoncé :* Franchissement des paliers et de l'échelle `L0–L4` subordonné à `15` portes `POR` et `27` signaux `SIG`, en concordance avec *Figure 3* (`SCH-00-03`).
  - *Preuve primaire :* `registre/matrice-exig-prr-c40.json` (`dapp_por_15` : `15` entrées, `dapp_sig_27` : `27` entrées), `schemas/rendus/SCH-00-03.svg` (`Z1`–`Z3`, `J1`–`J3`, `P1`–`P3`, `15 POR`, `27 SIG`, `INI-043`).
  - Verdict : supporté
- **L00-62** (`L106`) — *Énoncé :* Chaîne d'assurance qualité à six barrières (`G0` à `G5`), avec contrôle `G0` vérifié sur la trousse compagnon (`83/83` tests `pytest`, `45/45` règles `OPA` à `100,0 %` de couverture, `4/4` suites de vecteurs tiers).
  - *Preuve primaire :* `aq/rapports-g0.json` (`overall_status: "PASS"`, `exit_code: 0`, `pytest_check.passed: 83`, `opa_check.tests_passed: 45`, `opa_check.coverage_pct: 100.0`, `third_party_vectors`: `4/4` `passed: true`).
  - Verdict : supporté
- **L00-63** (`L106–L110`) — *Énoncé :* Barrières `G1`–`G5` et *Figure 4* (`SCH-00-04`) reliant loi de Lusser et inflation multi-agents (`15×`) au contrôle `pass^k` / Wilson, au disjoncteur `CPO` (`80 %` / `100 %`) et aux `24` portes bloquantes d'homologation `G0`–`G5`.
  - *Preuve primaire :* `schemas/SCH-00-04.mmd` (`L3–L29` : `53,9 % à 10 étapes × 94 %`, `Inflation multi-agents (15×)`, `pass^k et Wilson`, `80 % alerte · 100 % coupure`, `24 portes [BLOQUANT] PRR-75`), `SRC-032` (`∼15×`).
  - Verdict : supporté

---

## 3. Contrôle final post-rectifications

- **Validation déterministe `G1` (`verifie_manuscrit.py --unit 00-liminaire --strict`) :** `exit 0`, `0` erreur.
- **Calibre du manuscrit (`CA-01`) :** `4 063` mots (`verifie_manuscrit.py`) / `4 259` mots (`parser_plan.py`), conformes à la plage `[3 680, 4 320]`.
- **Base fermée citée (`CA-09`, `CA-10`) :** `19 / 19` sources (`[1]`–`[19]`) de `sources/ch00-sources.md` citées, `0` référence orpheline, `0` source en statut F exploitée hors réserve explicite (`CA-11`).
- **Verdict final — supportés :** 63 / 63 (100,0 %), `0` écart résiduel.

---

## 4. Mise à jour post-révision PRD (`REV-04`)

- **L00-REV-01 (`L7`, `PRD-L1-017`)** — *Énoncé :* Ajout de `NE DOIT JAMAIS` dans l'énumération RFC 2119.
  - *Preuve primaire :* `Compendium/prd.md` (`L306`), `SRC-045` (`RFC 2119`).
  - Verdict : supporté
- **L00-REV-02 (`L25`, `PRD-L1-010`)** — *Énoncé :* Exposé explicite en `§0.2` de la règle du maillon le plus élevé (`≤ N2`) et du harnais déterministe à huit étapes (`JSON Schema Draft 2020-12`, `additionalProperties: false`, `Decimal`, caviardage préalable, `AMBIGU_ESCALADE`, règle `H-31`).
  - *Preuve primaire :* `Compendium/prd.md` (`L277`), `harness_proto/pipeline.py`, `SRC-021` (`JSON Schema Draft 2020-12`).
  - Verdict : supporté
- **L00-REV-03 (`L73–L88`, `PRD-L1-002`, `PRD-L1-009`, `PRD-L1-010`)** — *Énoncé :* Remplacement de la collision `CAP-033` par `CAP-040` + `CA/B Forum v2.3.1` au *Tableau 0.2* (erratum `prd.md L294` aligné sur Annexe D `L7111`/`L7118` et `CH-06`), ajout des dix thèses `T1–T10`, des six décisions conjointes `AE ↔ AS`, de `PRR F-11`, `G0-EX-CH04-01`, `maxTotalCostCad`, `PRR O-13` et `NIST IR 8547`, suppression des `4` échappements `\$` dans backticks, et renvoi explicite vers la *Figure 4* (`SCH-00-04`) dès la suite du *Tableau 0.2* (en conservant l'ordre d'inclusion `SCH-00-01..04` imposé par `specs/manifest.json` / `CA-04`).
  - *Preuve primaire :* `Compendium/prd.md` (`L285–L296`, `L7111`, `L7118`), `registre/matrice-exig-prr-c40.json`, `specs/manifest.json`.
  - Verdict : supporté
- **L00-REV-04 (`L92–L106`, `PRD-L1-010`, `REF-003`)** — *Énoncé :* Ajout de `art. 17` (`ÉFVP`) et `art. 27` (portabilité) pour la Loi 25 (`[14]`), nuance de corroboration secondaire `AIBanks.ca` sur le repère AMF (portail en statut F), mention des repères `EN 18286:2026`, `DORA`, `Cyber Resilience Act`, `ISO/IEC 42001` et `NIST AI RMF`, et précision `21/21` validations sur `13` schémas `JSON Schema 2020-12` à la barrière `G0`.
  - *Preuve primaire :* `Compendium/prd.md` (`L300`), `SRC-063` (`LQ 2021, c. 25`), `aq/rapports-g0.json`.
  - Verdict : supporté
- **Contrôle `REV-04` :** `3 770` mots (`verifie_manuscrit.py`) / `3 965` mots (`parser_plan.py`) dans `[3 680, 4 320]`, `verifie_manuscrit.py --unit 00-liminaire --strict` = `exit 0`. **Verdict final : `67 / 67` (`100,0 %` supporté).**
