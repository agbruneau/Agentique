# Chapitre 01 — Harnais déterministe 80/20 à huit étapes et médiation protocolaire épinglée (MCP 2026-07-28, A2A v1.0.1)

*Question directrice : Comment enfermer l'appel probabiliste d'un modèle dans un harnais typé à huit étapes et épingler cryptographiquement les outils MCP 2026-07-28 et les cartes A2A v1.0.1 pour bloquer toute dérive silencieuse ?*

*Scénario illustratif.* Imaginons un dossier d'indemnisation soumis au petit matin à un agent d'extraction documentaire connecté à un catalogue externe d'outils. Aucun changement d'identifiant ni de numéro de version n'apparaît dans la configuration du connecteur depuis la veille. Pourtant, durant la nuit, le fournisseur distant a glissé une consigne supplémentaire dans la description textuelle d'un outil déjà approuvé, orientant l'extraction vers un appel de validation externe non prévu, tout en renvoyant un champ numérique libre là où le système aval attendait un montant entier borné. Faute de harnais typé encadrant l'inférence et faute de vérification cryptographique des définitions d'outils avant l'appel, l'incident passe sans alerte ni blocage jusqu'à la corruption silencieuse de la file de traitement.

Ce scénario illustratif traduit un risque mesuré à grande échelle sur le registre public du protocole MCP. Dans un recensement publié en septembre 2026 sur un instantané d'août 2026 couvrant `21 643` serveurs et `72 606` enregistrements de versions, Obada Kraishan observe une instabilité structurelle majeure sur les `8 900` serveurs dotés de plusieurs versions publiées [5]. Parmi ces serveurs multi-versions, `51,09 %` ont modifié leurs annonces entre versions et `40,58 %` présentent une dérive sémantique silencieuse sans changement des identifiants déclarés au registre [5]. De plus, `4,16 %` de ces `8 900` serveurs (`370` cas) ont basculé leur adresse distante vers un nouvel hôte tout en conservant le même nom au registre, et l'existence d'une telle dérive silencieuse (`40,58 %`) s'associe à un rapport de cotes de `2,96` parmi les `6 699` serveurs multi-versions dotés de code analysé pour la présence d'un constat de sécurité de gravité élevée [5].

En parallèle, le diagnostic posé sur les sept ouvrages antérieurs de la collection met en lumière un vide d'implémentation critique. L'ouvrage d'architecture de référence décrit bien des patrons de validation par grammaire contrainte, mais ne renferme qu'un seul bloc JSON Schema de quinze lignes sans harnais Python ni suite d'épreuves automatisée, tandis que la somme encyclopédique constate l'absence d'un chapitre consacré à la couche d'exécution du harnais. Entre la spécification textuelle et l'agent en exploitation, il manque l'enveloppe logicielle exécutable qui transforme des principes architecturaux en portes déterministes vérifiables à `exit 0`.

Ce chapitre répond à ce déficit en livrant le premier module compagnon de `8 - Manuel/trousse/`, intitulé `harness_proto/` (désigné `harness-proto/` dans la table éditoriale). La première section formalise la partition 80/20 et le pipeline typé à huit étapes qui encercle l'appel modèle sous JSON Schema Draft 2020-12 strict jusqu'à la porte `AMBIGU_ESCALADE`. La deuxième section verrouille l'intégration verticale des outils sous MCP 2026-07-28 par épinglage cryptographique et rejet `HeaderMismatch`. La troisième section isole les évolutions attendues post-gel (`SEP-2596` et `SEP-3398`, respectivement à l'horizon du 28 juillet 2027 et du 30 mars 2027) derrière un adaptateur de transport. La quatrième section transpose la même discipline à la délégation horizontale entre pairs avec la validation signée des cartes `AgentCard` sous A2A v1.0.1 et les vecteurs `a2a-tck`.

## 1.1 Pipeline typé en huit étapes (JSON Schema Draft 2020-12, `strict: true`) et porte `AMBIGU_ESCALADE`

La décision d'architecture la plus rentable dans la conception d'un agent d'entreprise ne porte ni sur le choix du fournisseur de modèle ni sur le raffinement rhétorique d'une invite système. Elle porte sur la frontière exacte tracée entre ce qui relève du calcul probabiliste et ce qui doit demeurer irréductiblement déterministe. Tant que la validation d'entrée, le contrôle de cohérence documentaire, les bornes budgétaires et la gestion des cas ambigus restent confiés à des consignes rédigées en langage naturel, l'architecture subit de plein fouet l'accumulation multiplicative des erreurs d'inférence.

### Fondements empiriques et mathématiques de la Partition 80/20

Deux résultats complémentaires issus de la littérature ouverte et de la fiabilité des systèmes fondent la **Partition 80/20** adoptée comme heuristique de conception dans le présent manuel. Sur le plan analytique d'abord, le manuel statistique du NIST et de SEMATECH (section 8.1.8.1, modèle des risques concurrents) formalise le produit des fiabilités d'un composant : lorsque \(k\) mécanismes de défaillance **indépendants** s'exercent en concurrence (la première défaillance entraînant celle du composant), la fiabilité résultante à l'instant \(t\) vaut \(R_c(t) = \prod_{i=1}^{k} R_i(t)\) [1], ce qui équivaut mathématiquement à une loi en série dite de Lusser. À titre purement illustratif — dans l'hypothèse idéale où des étapes successives échoueraient indépendamment — un enchaînement de `10` appels probabilistes fiables à `94 %` chacun tomberait à \(0{,}94^{10} \approx 0{,}5386\), soit `53,9 %` ; dès lors que des erreurs de contexte s'auto-amplifient en chaîne réelle, la dérive est encore moins favorable sans bornes déterministes.

Sur le plan empirique ensuite, l'étude *Measuring Agents in Production* (MAP) publiée en décembre 2025 par Melissa Z. Pan et ses coauteurs examine comment des équipes d'ingénierie contournent cette fragilité dans des systèmes déployés [2]. S'appuyant sur une enquête auprès de 306 praticiens (incluant 86 systèmes déployés en production ou en phase pilote) et vingt études de cas approfondies, l'étude MAP montre que 68 % des agents déployés exécutent au plus 10 étapes avant intervention humaine [2]. Par ailleurs, 80 % des études de cas (16 sur 20) privilégient des enchaînements prédéfinis et bornés au lieu de laisser l'agent composer librement son graphe d'actions [2]. Parmi ces vingt études de cas, 70 % (14 sur 20) utilisent des modèles sur étagère sans réglage des poids, tandis que l'enquête sur les systèmes déployés relève une rédaction humaine ou assistée des invites dans 79 % des réponses et une évaluation avec humain dans la boucle dans 74 % des cas [2].

Le cadre conceptuel CoALA (*Cognitive Architectures for Language Agents*) proposé par Sumers et al. éclaire ce partage des responsabilités en décomposant l'agent en mémoire de travail, mémoires à long terme (procédurale, sémantique et épisodique) et espace d'actions structuré [4]. Dans ce modèle cognitif, la mémoire de travail agrège les observations courantes et les buts intermédiaires, tandis que le cycle décisionnel sélectionne des actions internes de raisonnement ou de récupération avant d'émettre une action externe [4]. Toutefois, un cadre cognitif décrit la boucle perception-décision-action sans imposer par lui-même une barrière technique d'exécution qui refuse les sorties incohérentes.

L'heuristique d'architecture dite **Partition 80/20** retenue dans ce manuel traduit cette intuition du modèle multiplicatif [1] et la prédominance des flux structurés observée dans MAP [2] en règle qualitative de séparation des responsabilités. La totalité (100 %) du contrôle d'entrée, de la validation syntaxique, des bornes numériques, de l'ancrage référentiel et du routage d'erreur s'exécute en code déterministe hors du modèle : dans `harness_proto/`, l'enveloppe déterministe encadre une unique interface d'inférence structurée (confinant la part probabiliste à une faible minorité — de l'ordre de 20 % — de la logique décisionnelle). Sous `max_repair_retries = 2`, le pire cas exécute au plus trois appels corrélés au modèle avant escalade ou acceptation, transformant le modèle en simple proposeur structuré dépourvu d'autorité finale et satisfaisant les critères `C01`, `C07` et `C09` de la matrice du manuel.

### Démarcation de provenance : renvoi au Tableau 47.3 et statut de la RFC 9334

Avant d'enfermer l'appel modèle dans un contrat de schéma, une précision de périmètre s'impose afin d'éviter toute redondance documentaire. La question de l'inventaire des composants agentiques — parfois désigné sous le terme d'AIBOM (*AI Bill of Materials*) — a déjà fait l'objet au Tableau 47.3 du premier compendium de la collection (`1 - Compendium 2026.md`, section 47.2.1) d'un relevé partiel — négatif quant aux composants proprement agentiques — fondé sur la lecture des schémas `CycloneDX 1.7` (`ECMA-424`, 2e éd.) et `SPDX 3.0` (profils `AI` et `Dataset`). Ce relevé établit que si les poids de modèles et les jeux de données disposent de propriétés nommées dans ces nomenclatures, aucun champ n'y existe pour décrire les invites ni les politiques d'autorisation propres à l'agent. Le présent chapitre renvoie intégralement au constat établi à ce Tableau 47.3 sans en répéter l'épreuve en barrière `G0` : l'inventaire logiciel statique ne suffit pas à vérifier la conformité d'exécution d'un harnais agentique.

De la même manière, la normalisation de l'attestation de plateforme distante relève de la RFC 9334 (*Remote ATtestation procedureS Architecture*, RATS), qui distingue notamment les rôles architecturaux d'*Attester*, de *Verifier*, de *Relying Party*, d'*Endorser* et de *Reference Value Provider*. Conformément au registre `specifications-lplus.json` et à l'analyse du premier compendium (`1 - Compendium 2026.md`, section 47.3.1), la RFC 9334 est publiée par l'IETF dans la catégorie *Informational* et non *Standards Track* : elle fournit un vocabulaire architectural de référence pour la confiance de plateforme, sans prescrire un format de fil normatif directement exécutable pour valider les contrats d'un harnais applicatif. Dans `8 - Manuel/trousse/`, la vérification d'intégrité applicative s'appuie donc sur des spécifications à syntaxe vérifiable mécaniquement. Il s'agit du dialecte JSON Schema Draft 2020-12 (*Internet-Draft Informational*) [3], de la canonisation RFC 8785 (JCS, *Independent Submission, Informational*) [12] pour les condensats du harnais (`1.1`), des outils MCP (`1.2`) et des cartes A2A (`1.4`), et de l'enveloppe RFC 7515 (JWS, *IETF Standards Track*) [13] pour signer ces cartes A2A (`1.4`), plutôt que de champs AIBOM inexistants ou d'une attestation matérielle hors périmètre `G0`.

### Exigences du profil JSON Schema Draft 2020-12 (`strict: true`)

Un **Harnais déterministe** repose sur un contrat de données univoque entre l'appelant et le modèle de langage [3]. Le dialecte JSON Schema Draft 2020-12 — dont le texte central (draft-bhutton-json-schema-01) spécifie l'architecture de méta-schémas, les références \$ref, l'application aux objets (`properties`, `additionalProperties`) et la composition (`allOf`, `if`, `then`, `else`) [3], complétés par le vocabulaire de validation (`required`, types, énumérations, motifs lexicaux et bornes numériques) exécuté par `Draft202012Validator` — encadre ce contrat. Cependant, laisser un schéma ouvert ou permissif autorise le modèle à omettre des champs ambigus, à inventer des propriétés annexes ou à glisser des références distantes non maîtrisées. C'est pourquoi le module `harness_proto/pipeline.py` impose un profil durci désigné `strict: true` et vérifié par la fonction `validate_strict_schema` avant toute exploitation du résultat.

Ce profil `strict: true` associe la méta-validation structurelle de l'arbre du schéma (dans `_walk_strict_rules` et `validate_strict_schema`) puis la validation de l'instance JSON produite via `Draft202012Validator` :

- **Fermeture totale des objets** : chaque nœud objet parcouru récursivement doit déclarer explicitement `additionalProperties` à `false` ; toute propriété inconnue ajoutée par le modèle ou absente du contrat provoque un rejet immédiat.
- **Exhaustivité des clés requises** : à chaque niveau d'objet, toute propriété déclarée dans `properties` doit figurer dans le tableau `required` ; les champs susceptibles d'être indéterminés s'expriment par union explicite avec `null` (par exemple `["integer", "null"]`).
- **Interdiction des mots-clés dynamiques à la racine** : les opérateurs de composition ou conditionnels `allOf`, `if`, `then` et `else` sont bannis au premier niveau du schéma afin de préserver un contrat plat compatible avec les moteurs de décodage contraint, tandis que les invariants conditionnels entre champs sont déportés vers le code Python aval (`_check_grounding`).
- **Interdiction des références réseau externes (`EXIG-MCP-19`)** : tout mot-clé \$ref (y compris imbriqué) pointant vers un schéma `http://` ou `https://` est bloqué par inspection statique avant validation, fermant un vecteur classique d'attaque SSRF ou de modification dynamique de contrat à distance.

L'extrait `G0-EX-CH01-01` ci-dessous présente l'intégralité du contrat normatif `HarnessExtraction` utilisé comme schéma de sortie vérifié en `G0` par le harnais d'extraction documentaire.

<!-- CA-G0-SYNC id="G0-EX-CH01-01" path="8 - Manuel/trousse/schemas/harness_extraction.schema.json" lines="1-24" sha256="6b4428a1f8a6abcd2029280cded86b0e983ddb349d0f05c6ba0192c010f95aac" -->
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "HarnessExtraction",
  "x-license": "MIT",
  "type": "object", "additionalProperties": false,
  "required": [
    "statut_analyse", "categorie_sinistre",
    "montant_reclame_cents", "reference_dossier", "motif_escalade"
  ],
  "properties": {
    "statut_analyse": {
      "type": "string",
      "enum": ["EXTRAIT", "AMBIGU_ESCALADE", "DONNEES_INSUFFISANTES"]
    },
    "categorie_sinistre": { "type": "string", "minLength": 1 },
    "montant_reclame_cents": {
      "type": ["integer", "null"], "minimum": 0
    },
    "reference_dossier": {
      "type": "string", "pattern": "^DOS-[0-9]{4,8}$"
    },
    "motif_escalade": { "type": ["string", "null"] }
  }
}
```

Quatre invariants architecturaux ressortent de ce contrat de vingt-quatre lignes. D'abord, la représentation de `montant_reclame_cents` impose un entier non négatif en centièmes (ou `null` en cas d'ambiguïté), bannissant d'emblée les nombres à virgule flottante IEEE-754 dont les erreurs d'arrondi affectent les calculs financiers — une discipline que le Chapitre 03 prolonge avec le module `decimal_money.py`. Ensuite, `reference_dossier` contraint strictement le format syntaxique par expression régulière ancrée, empêchant l'injection de texte libre ou de caractères de contrôle dans un identifiant métier.

Par ailleurs, la présence obligatoire de `statut_analyse` offre au modèle une issue typée explicite (`AMBIGU_ESCALADE` ou `DONNEES_INSUFFISANTES`) lorsqu'une pièce justificative présente deux montants contradictoires ou s'avère illisible, lui permettant de laisser `montant_reclame_cents` à `null` (tout en maintenant une catégorie générique non vide dans `categorie_sinistre` selon ce schéma plat). Les relations conditionnelles entre `statut_analyse`, `montant_reclame_cents` et la non-vacuité de `motif_escalade` (puisque le schéma autorise `motif_escalade` nullable sans `if`/`then`/`else` à la racine) sont ensuite imposées en aval par `_check_grounding` avant toute acceptation. Enfin, la propriété `x-license` permet à la barrière `G0` de vérifier mécaniquement la compatibilité MIT de chaque schéma de la trousse, tandis que `validate_strict_schema` rejette tout schéma dépourvu de `additionalProperties: false` ou contenant un mot-clé interdit à la racine, comme le démontrent les cas négatifs de `test_harness_proto.py`.

### Les huit étapes séquentielles hors invite et la porte `AMBIGU_ESCALADE`

Envelopper l'extraction documentaire exige bien plus qu'un validateur syntaxique placé en sortie. Comme le synthétise la `Figure 1`, une fois l'entrée admise, le flux orchestré par `DeterministicHarness` dans `harness_proto/pipeline.py` consigne une trace d'audit fixe à huit jalons (`step_trace` ; en cas de rejet précoce `VALIDATION_FAILED`, la trace s'arrête à un ou deux jalons terminés par `*_fail`), dont un seul jalon — le quatrième (`4_model`) — délègue à l'adaptateur probabiliste externe. Sur le plan de l'exécution réelle, une boucle `while` bornée (`max_repair_retries = 2`) répète le contrôle `5_schema` (et `6_grounding` lorsque le schéma est valide) en aval d'une reprise éventuelle, portant le plafond pire cas à trois appels modèle avant l'enregistrement des quatre derniers jalons de trace (`5_schema` à `8_seal`) et le calcul d'une empreinte d'intégrité `output_sha256` non signée via JCS SHA-256.

![Pipeline du harnais 80/20](../diagrammes/rendus/Fig-01.svg)
*Figure 1 — Pipeline déterministe du harnais 80/20 à huit jalons et porte AMBIGU_ESCALADE sous schémas JSON Schema 2020-12 stricts.*

Comme le montre la `Figure 1`, la frontière déterministe possédée et vérifiée en `G0` encercle intégralement l'adaptateur probabiliste (représenté en pointillé ambre) depuis la réception du dictionnaire d'entrée jusqu'au calcul final de l'empreinte d'intégrité JCS SHA-256. L'entrée externe non fiable est d'abord re-sérialisée en UTF-8 avec `allow_nan=False` pour borner sa taille à `64 Kio` (`65 536` octets) et rejeter tout flottant `NaN`/`Infinity`, puis validée contre le schéma d'entrée fermé `_INPUT_SCHEMA` avant même que le modèle ne soit invoqué.

Après l'inférence, `HarnessExtraction` pilote la validation structurelle de sortie, puis `_check_grounding` vérifie les bornes de référence (identifiants admissibles `allowed_grounding_ids`, plafonds `max_montant_cents` et cohérence des champs `statut_analyse` / `motif_escalade`) sans prétendre vérifier la véracité linguistique du texte libre. En cas d'écart persistant après au plus trois appels modèle (facteur maximal `3×` en nombre d'appels, soit un surcoût maximal de deux appels supplémentaires incluant les erreurs `errs` en jetons d'entrée), la boucle scelle un `HarnessOutcome` au statut de rejet borné `ESCALADED` ; sinon, elle scelle un `HarnessOutcome` au statut `OK`, `AMBIGU_ESCALADE` ou `DONNEES_INSUFFISANTES`. Cette séparation matérialise le critère `C09` : le modèle reste un composant substituable dépourvu d'autorité de décision finale.

L'ordre des huit jalons consignés dans `step_trace` par `DeterministicHarness` (sept jalons de contrôle déterministe et un jalon d'inférence pouvant boucler jusqu'à trois appels pire cas) ainsi que leurs contrats d'échec vérifiés en `G0` figurent au `Tableau 1.1`.

*Tableau 1.1 — Les huit jalons du harnais 80/20 (`harness_proto/pipeline.py`, trace `step_trace` et boucle bornée à `max_repair_retries = 2`) vérifiés en G0*

| Jalon | Trace `step_trace` | Contrôle exécuté | Verdict en cas d'écart |
| :---: | --- | --- | --- |
| 1 | `1_size_utf8` | Re-sérialisation UTF-8 (`allow_nan=False`) et plafond `max_payload_bytes` (`65 536` octets) | `VALIDATION_FAILED` (`1_size_utf8_fail`) |
| 2 | `2_input` | Validation `_INPUT_SCHEMA` (`additionalProperties: false`, `reference_dossier`, `texte`) | `VALIDATION_FAILED` (`2_input_schema_fail`) |
| 3 | `3_ctx` | Construction du contexte borné avec liste triée des identifiants `grounding_records` | Préparation déterministe sans appel externe |
| 4 | `4_model` | Appel initial `_model_adapter(ctx, [])`, suivi d'au plus `2` reprises si `errs` (`3` appels pire cas) | Délégation probabiliste bornée (~`20 %`) |
| 5 | `5_schema` | `validate_strict_schema` (méta-validation stricte + instance via `Draft202012Validator`) | Déclenche reprise ou escalade (`errs`) |
| 6 | `6_grounding` | `_check_grounding` : périmètre `allowed_grounding_ids`, plafond pièce et règles inter-champs | Déclenche reprise ou escalade (`errs`) |
| 7 | `7_repair` | Compteur `retries` plafonné à `max_repair_retries` (`2` max) pilotant la boucle de reprise | `ESCALADED` si `errs` persiste au plafond |
| 8 | `8_seal` | Condensat d'intégrité `output_sha256` via JCS SHA-256 sur `{"status", "payload", "trace"}` (sans signature JWS) dans `HarnessOutcome` | `ESCALADED`, `OK`, `AMBIGU_ESCALADE` ou `DONNEES_INSUFFISANTES` |

Un point essentiel du `Tableau 1.1` concerne la complémentarité entre le jalon 5 (validation de schéma) et le jalon 6 (contrôle de référentiel `_check_grounding`). Par construction, la conformité syntaxique à un JSON Schema ne garantit pas l'ancrage aux pièces du dossier. Un modèle peut renvoyer un objet JSON valide pour un dossier `DOS-9999` absent des pièces soumises, extraire un montant dépassant `max_montant_cents`, ou déclarer `AMBIGU_ESCALADE` en laissant `motif_escalade` à `null`. La fonction `_check_grounding` croise donc la sortie candidate avec `raw_input`, `grounding_records` et `allowed_grounding_ids` puis vérifie ces règles croisées en code Python pur, sans toutefois contrôler la sémantique libre du texte.

Il faut également distinguer avec rigueur les quatre statuts non-`OK` exposés par `StepStatus` dans `pipeline.py` : deux rejets d'échec (`VALIDATION_FAILED` et `ESCALADED`) et deux issues typées (`AMBIGU_ESCALADE` et `DONNEES_INSUFFISANTES`). Le statut `VALIDATION_FAILED` intervient dès les jalons 1 et 2 lorsque l'appelant fournit une entrée non sérialisable, un flottant `NaN`, une charge dépassant `max_payload_bytes` ou un objet ne respectant pas `_INPUT_SCHEMA` : le modèle n'est alors même pas appelé. Le statut `ESCALADED` sanctionne le jalon 7 lorsqu'une sortie candidate échoue de façon persistante au schéma strict ou aux invariants `_check_grounding` après épuisement des `max_repair_retries` tentatives de correction. À l'opposé, `AMBIGU_ESCALADE` et `DONNEES_INSUFFISANTES` traduisent une sortie syntaxiquement valide et sémantiquement ancrée où le modèle reconnaît explicitement son incertitude documentaire et justifie le transfert vers une file de révision humaine grâce à un `motif_escalade` non vide.

L'extrait `G0-EX-CH01-02` montre la boucle complète de `DeterministicHarness.run`, qui assemble ces huit jalons d'étape (`step_trace`) en vingt-neuf lignes auditées et verrouillées en `G0` sous la porte bloquante `R-01` (`C01`, `C07`, `C09`, `C10`, `C19`, `C34`).

<!-- CA-G0-SYNC id="G0-EX-CH01-02" path="8 - Manuel/trousse/harness_proto/pipeline.py" lines="204-232" sha256="75110799d751ee4b93c58c7aff4e2b6ce0c2c8d29c50b6d1668b4bf895dfc275" -->
```python
    def run(
        self, raw_input: dict[str, Any], grounding_records: dict[str, Any]
    ) -> HarnessOutcome:
        """Execute les 8 etapes deterministes 80/20 hors invite."""
        if (bad := self._check_input(raw_input)) is not None:
            return bad
        schema = json.loads(self._config.schema_path.read_text("utf-8"))
        ctx = {"input": raw_input, "refs": sorted(grounding_records)}
        trace = ["1_size_utf8", "2_input", "3_ctx", "4_model"]
        retries, errs, cand = 0, [], self._model_adapter(ctx, [])
        while True:
            errs = validate_strict_schema(schema, cand) or _check_grounding(
                cand, raw_input, grounding_records,
                self._config.allowed_grounding_ids,
            )
            if not errs or retries >= self._config.max_repair_retries:
                break
            retries += 1
            cand = self._model_adapter(ctx, errs)
        trace.extend(["5_schema", "6_grounding", "7_repair", "8_seal"])
        if errs:
            return _seal_outcome(
                StepStatus.ESCALADED, None, "; ".join(errs), retries, trace
            )
        raw_st = cand["statut_analyse"]
        st = StepStatus.OK if raw_st == "EXTRAIT" else StepStatus(raw_st)
        return _seal_outcome(
            st, cand, cand.get("motif_escalade"), retries, trace
        )
```

Cet extrait met en évidence quatre garanties vérifiées par les cas positifs et négatifs de `tests/test_harness_proto.py`. En premier lieu, l'échec précoce dans `_check_input` court-circuite toute invocation du modèle sur charge utile surdimensionnée ou entrée vide, économisant les jetons et empêchant l'injection avant même la construction du contexte `ctx`. En deuxième lieu, l'expression booléenne `validate_strict_schema(schema, cand) or _check_grounding(...)` garantit que les invariants métier ne s'exécutent que sur une structure déjà prouvée conforme au schéma, évitant les exceptions de type sur clés absentes ou types imprévus.

En troisième lieu, le compteur `retries` borne strictement la boucle de réparation : lorsqu'un adaptateur défaillant renvoie systématiquement `{"invalide": True}`, le harnais tente exactement deux réparations (`retries == 2`, soit trois appels au total), puis bascule sur `StepStatus.ESCALADED` en joignant tous les diagnostics accumulés (`"; ".join(errs)`) sans jamais risquer de boucle infinie ni d'explosion budgétaire. En quatrième lieu, la distinction terminale entre `StepStatus.OK` (lorsque `statut_analyse == "EXTRAIT"`), `StepStatus.AMBIGU_ESCALADE` et `StepStatus.DONNEES_INSUFFISANTES` produit dans tous les cas un objet `HarnessOutcome` immuable scellé par `output_sha256`, calculé via canonisation JCS sur le statut, la charge validée et la trace des huit étapes.

Sur le plan de la reproductibilité logicielle, la structure de configuration `HarnessConfig` est figée via `@dataclass(frozen=True, slots=True)` afin d'interdire toute altération de ses seuils (`schema_path`, `max_repair_retries`, `max_payload_bytes`, `allowed_grounding_ids`) en cours d'exécution. À l'étape 3, le harnais construit le dictionnaire `ctx` en triant systématiquement les clés des pièces justificatives (`sorted(grounding_records)`) pour préserver l'invariance du préfixe contextuel d'un appel à l'autre. Ce tri déterministe garantit que deux exécutions sur les mêmes dossiers produisent exactement la même trace et le même condensat `output_sha256` dès lors que l'adaptateur répond de façon identique.

En régime `DC-P12`, ces propriétés sont démontrées sur doublures synthétiques d'adaptateurs sans appel à un grand modèle de langage payant en direct. La suite `tests/test_harness_proto.py` vérifie notamment l'exécution nominale à huit étapes, le rejet d'un montant supérieur au plafond `grounding_records`, le rejet d'une référence hors périmètre `DOS-9999`, le basculement propre sur `AMBIGU_ESCALADE` lorsque le texte présente « 500\$ ou 900\$ », l'arrêt net au plafond de deux réparations et le refus d'une charge excédant `max_payload_bytes`. Le harnais sécurise ainsi la frontière cognitive interne ; reste maintenant à sécuriser la frontière verticale vers les outils externes sous MCP 2026-07-28.

## 1.2 Épinglage JCS SHA-256 sur `tools/list` (MCP 2026-07-28), détection des 40,58 % de dérive silencieuse et rejet `HeaderMismatch`

Sécuriser la sortie du modèle ne protège aucunement l'entreprise si les définitions d'outils injectées dans son contexte ou les en-têtes acheminant ses appels peuvent muter à son insu. Le protocole MCP standardise la découverte et l'invocation d'outils entre un hôte client et un serveur distant par JSON-RPC 2.0, mais délègue largement la gouvernance de confiance à la couche d'intégration. L'analyse empirique et l'inspection de la spécification `2026-07-28` expliquent pourquoi l'**Épinglage cryptographique** des catalogues et la validation stricte des en-têtes constituent des contrôles bloquants.

### Anatomie de la dérive silencieuse (`40,58 %`) et leçon du défaut F-52

Le recensement empirique conduit par Obada Kraishan fournit la mesure la plus nette de cette fragilité au gel du 2 décembre 2026 [5]. Sur les `21 643` serveurs uniques et `72 606` enregistrements de versions extraits du registre public MCP en août 2026, le code source de `14 353` serveurs a pu être analysé et l'historique de `8 900` serveurs multi-versions (`37 160` transitions) a été comparé paire par paire [5]. Les résultats montrent que `51,09 %` (`4 547` serveurs) ont changé leur description, leurs paquets ou leurs points d'accès entre versions, et que `40,58 %` présentent une **Dérive silencieuse** où les identifiants déclarés au registre restent fixes tandis que la signification (description réécrite) ou la destination (hôte distant remplacé) change [5].

Plus critique encore sur le plan de l'exploitation, `4,16 %` de ces `8 900` serveurs (`370` serveurs, `441` événements) ont justement redirigé leur point d'accès distant vers un hôte différent tout en conservant le même nom au registre [5]. Parmi les `6 699` serveurs multi-versions inclus dans la population analysée au code source, le rapport de cotes liant la dérive silencieuse à la présence d'un constat de sécurité de gravité élevée atteint `2,96` [5]. De même, dans le modèle multivarié sur les `14 353` serveurs analysés prédisant un constat de gravité élevée, à taille, âge, maintenance récente, statut d'archivage et licence constants, le logarithme des étoiles GitHub (`log(1 + étoiles)`) n'offre qu'un effet protecteur modeste (`OR = 0,78` par unité logarithmique), alors que la corrélation de rang bivariée avec les constats demeure nulle [5]. Fait structurel central relevé par Kraishan : le schéma même du registre public ne versionne pas les définitions d'outils (`tools/list`), qui demeurent invisibles dans les métadonnées de publication [5].

En écho à ce constat empirique, le défaut documenté sous l'identifiant F-52 dans le premier compendium (`1 - Compendium 2026.md`, section 39.2.1) notait que sur la page de description d'outils de la révision MCP de novembre 2025, la structure d'un outil ne portait ni numéro de version, ni empreinte cryptographique, ni signature. Le rejeu de cette vérification directement sur la spécification MCP 2026-07-28 archivée au corpus ouvert (`tools.mdx` [6] et `schema.ts` [9], commit épinglé `5f5440bb`) confirme que le diagnostic demeure inchangé sur l'objet `Tool` lui-même. Une définition d'outil dans `tools/list` comprend `name`, `title`, `description`, `icons`, `inputSchema`, `outputSchema` et `annotations` dans `tools.mdx` [6] — complétés par le champ optionnel `_meta` dans `schema.ts` [9] — toujours sans champ natif de signature cryptographique ni d'empreinte intégrée au schéma de base. La section *Server Tools* de la révision `2026-07-28` énonce d'ailleurs un avertissement normatif explicite sur la confiance : « les clients DOIVENT considérer les annotations d'outils comme non fiables à moins qu'elles proviennent de serveurs de confiance » [6].

Parallèlement, Alfredo Metere documente dans l'étude `arXiv:2605.24248` (*Attested Tool-Server Admission*, juin 2026) une approche complémentaire baptisée `mcp-attested` pour combler ce déficit d'admission native au-dessus du protocole existant sans modifier le fil JSON-RPC [18]. Son architecture combine une assertion d'habilitation signée hors ligne publiée à un URI bien connu, une liste blanche fermée d'outils par serveur refusant par défaut tout outil non autorisé, et un journal d'audit chaîné par hachage [18]. Le module `harness_proto/mcp_pinning.py` transpose précisément cette logique défensive de liste blanche fermée et de hachage canonique dans l'architecture d'entreprise de `8 - Manuel/trousse/`, en l'arrimant au contrat de catalogue `mcp_tool_catalog.schema.json` et aux exigences `EXIG-MCP-03`, `EXIG-MCP-15`, `EXIG-MCP-16`, `EXIG-MCP-18` et `EXIG-MCP-20`.

### Contrat de catalogue d'entreprise et canonisation JCS (RFC 8785)

La fiche de gouvernance `schemas/mcp_tool_catalog.schema.json` fixe en profil strict le référentiel interne contre lequel chaque outil découvert dynamiquement par `tools/list` est confronté. Contrairement à un registre public ouvert, ce contrat exige vingt propriétés obligatoires incluant le niveau de risque (`tier` parmi `P0`, `P1`, `P2`, `P3`), l'état de cycle de vie (`lifecycle_state` de `draft` à `retired`), l'empreinte `definition_digest` formée du préfixe `sha256:` suivi de `64` caractères hexadécimaux, et la révision épinglée `mcp_revision` figée à `"2026-07-28"`. Il impose également les seuils d'approbation calculés exclusivement par la passerelle (`computed_by: "gateway"`), l'opération de compensation associée et la politique d'idempotence (`on_conflict: "reject"`, `on_in_progress: "refuse"`, `on_duplicate: "replay_result"`). Ce contrat requiert enfin la désignation explicite d'un propriétaire métier (`owner`), d'une équipe d'astreinte (`on_call_team`), des réviseurs (`reviewed_by`) et de la prochaine date de revue (`next_review`).

Comparer deux définitions JSON d'outils par simple sérialisation textuelle `json.dumps` exposerait toutefois à des faux positifs constants : il suffit qu'un serveur réordonne deux clés dans `inputSchema` ou insère un espacement différent pour invalider une comparaison brute, tandis qu'une altération subtile dans un champ texte passerait inaperçue sans empreinte vérifiée. La RFC 8785 (*JSON Canonicalization Scheme*, JCS, juin 2020) résout ce problème en définissant une représentation UTF-8 unique et reproductible indépendamment du langage d'exécution [12].

Dans `harness_proto/jcs.py`, les fonctions `canonicalize_jcs` et `jcs_sha256_hex` implémentent fidèlement les trois règles de la RFC 8785 [12] :

- **Tri lexicographique UTF-16 des clés** : à chaque niveau d'objet JSON, les clés sont encodées en `utf-16-be` et triées par ordre strict d'unités de code UTF-16, sans égard à leur ordre d'apparition d'origine.
- **Formatage ECMAScript des nombres et rejet des valeurs non finies** : tout flottant `NaN` ou `Infinity` et tout entier hors de la plage sûre IEEE-754 de \(\pm (2^{53} - 1)\) lèvent immédiatement `JcsError`, tandis que les nombres valides adoptent la représentation ECMAScript normalisée sans zéros superflus.
- **Échappement minimal des chaînes** : suppression de tout espace blanc hors chaîne et encodage minimal normalisé des caractères de contrôle en UTF-8 avant calcul du condensat SHA-256 hexadécimal sur `64` caractères.

Cette implémentation partagée est également réutilisée au Chapitre 02 pour les preuves d'approbation `C.6` et au Chapitre 03 pour les clés d'idempotence `idem-v1`. Elle est éprouvée en barrière `G0` sur les `20` fichiers de vecteurs officiels rfc8785, incluant les échantillons IEEE-754 de l'Annexe B, les cas limites BMP vs astraux UTF-16 de la section 3.2.3 et les six paires d'entrée-sortie octet pour octet de `testdata`.

En pratique d'exploitation, chaque entrée approuvée au catalogue interne est instanciée sous forme d'objet immuable `McpCatalogEntry` regroupant `ref`, `server_id`, `tool_name`, `contract_version`, `definition_digest`, `mcp_revision`, `tier`, `allowed_header_projections`, `volatile_meta_keys` et `allowed_meta_keys`. Sur cette base, `compute_tool_definition_digest` retire d'abord les clés de premier niveau déclarées volatiles (par exemple la clé `_meta` portant un horodatage `lastUpdated`), canonise la définition d'outil nettoyée et préfixe l'empreinte `sha256:`. Cette séparation évite les fausses suspensions sur rotation d'horodatage tout en maintenant une sensibilité absolue à toute modification du schéma ou du texte descriptif.

La fonction `verify_tools_list_against_catalog` reçoit ensuite la liste brute renvoyée par `tools/list`, la trie de manière déterministe par nom d'outil (`EXIG-MCP-03`), rejette les doublons et tout outil absent du catalogue (`collision_ou_hors_catalogue`), puis compare l'empreinte calculée à `entry.definition_digest` (`derive_jcs_sha256`). La moindre altération d'un seul caractère — même l'ajout d'un espace final dans `description` (*rug pull*) — déclenche immédiatement la suspension de l'outil et, dès le seuil `max_drift_before_suspend = 1`, la suspension complète du serveur avec purge de `active_tools`. Les outils légitimes sont en outre préfixés `server_id.tool_name` pour prévenir toute collision d'homonymes entre serveurs distincts (`EXIG-MCP-20`, critère `C12`).

### Contrôle des en-têtes MCP 2026-07-28, purge `_meta` et rejet `HeaderMismatch`

Dans sa révision `2026-07-28`, le transport *Streamable HTTP* de MCP introduit un ensemble d'en-têtes HTTP destinés à permettre aux passerelles de router les appels JSON-RPC sans analyser systématiquement le corps complet de la requête [7]. Comme le spécifie `streamable-http.mdx`, chaque requête JSON-RPC `POST` doit désormais porter `MCP-Protocol-Version` (concordant avec `_meta["io.modelcontextprotocol/protocolVersion"]`), `Mcp-Method` (concordant avec `method`) et, pour `tools/call`, `resources/read` ou `prompts/get`, l'en-tête `Mcp-Name` (concordant avec `params.name` ou `params.uri`) [7]. La spécification est catégorique : si les valeurs divergent, le serveur DOIT rejeter la requête avec le statut HTTP `400 Bad Request` et une erreur JSON-RPC `HeaderMismatch` de code `-32020` [7]. Sans cette barrière, un proxy de sécurité qui lirait `Mcp-Name: recherche_publique` dans l'en-tête laisserait passer un corps JSON-RPC réclamant `supprimer_base`.

Parallèlement, les propriétés d'un `inputSchema` peuvent porter l'annotation `x-mcp-header` afin de projeter un paramètre non sensible (comme un centre de coûts `Cost-Center`) vers un en-tête `Mcp-Param-Cost-Center` exposé aux répartiteurs de charge et proxys intermédiaires [6, 7]. Or, les en-têtes HTTP transitent souvent en clair dans les journaux de ces intermédiaires réseau ; tout en proscrivant le stockage non protégé et le relais aveugle de jetons dans `security-considerations.mdx` [8], la trousse applique l'exigence `EXIG-MCP-18` afin de bloquer toute projection `x-mcp-header` dont le nom de propriété ou d'en-tête contient un jeton sensible ou un renseignement personnel.

Dans `mcp_pinning.py`, la fonction `_has_sensitive_token` découpe chaque identifiant CamelCase ou snake_case via l'expression `_IDENT_PART_RE` et refuse l'ensemble fermé des `21` marqueurs sensibles (`token`, `secret`, `password`, `passwd`, `auth`, `authorization`, `bearer`, `nas`, `sin`, `ssn`, `ramq`, `iban`, `card`, `carte`, `pii`, `cookie`, `jwt`, `apikey`, `credential`, `credentials`, `private`). Elle bloque ainsi des intitulés tels que `Auth-Token` ou `Citizen-NAS` dès la validation d'appel, tout en rejetant tout écart entre `Mcp-Param-*` et `params.arguments`. Enfin, le schéma TypeScript normatif `schema.ts` [9] réserve dans `_meta` les préfixes dont le second segment vaut `"modelcontextprotocol"` ou `"mcp"` (tels `io.modelcontextprotocol/protocolVersion`) ; par défense en profondeur, `mcp_pinning.py` ne conserve que `_PROTO_META_KEY` et `allowed_meta_keys`, purgeant toute autre clé (`tenant`, `authenticated`, `clientInfo`) pour neutraliser les usurpations de contexte (`EXIG-MCP-16`).

Le `Tableau 1.2` récapitule ces cinq contrôles exécutés par `mcp_pinning.py` avant tout acheminement vers un serveur d'outils.

*Tableau 1.2 — Règles de concordance d'en-têtes, purge `_meta` et épinglage JCS SHA-256 (`mcp_pinning.py`, MCP 2026-07-28)*

| Contrôle protocolaire (`EXIG-*`) | Champ ou en-tête inspecté | Condition de rejet ou de purge | Code / Exception émis |
| --- | --- | --- | --- |
| Épinglage `tools/list` (`EXIG-MCP-03`, `20`) | Empreinte JCS SHA-256 + ordre trié | Écart de condensat (`1` caractère), doublon ou outil hors catalogue | Suspension outil / serveur (`active_tools = {}`) |
| Concordance version & méthode (`EXIG-MCP-15`) | `MCP-Protocol-Version`, `Mcp-Method`, `Mcp-Name` | Divergence avec `_meta`, `method` ou `params.name` ; doublon HTTP | `HeaderMismatchError` (`400`, `-32020`) |
| Projections `Mcp-Param-*` (`EXIG-MCP-15`) | En-tête `Mcp-Param-{nom}` vs `arguments` | Valeur divergente ou en-tête absent de `allowed_header_projections` | `HeaderMismatchError` (`400`, `-32020`) |
| Hygiène `x-mcp-header` (`EXIG-MCP-18`) | Noms de propriété et d'en-tête projeté | Présence de mot-clé sensible (`token`, `nas`, `ramq`, `iban`, `jwt`, `pii`) | `ValueError` bloquant l'admission |
| Liste blanche `_meta` (`EXIG-MCP-16`) | `params._meta` (`schema.ts` [9]) | Purge silencieuse de toute clé hors `_PROTO_META_KEY` et `allowed_meta_keys` | Dictionnaire purgé sans `tenant`/`clientInfo` |

L'extrait `G0-EX-CH01-03` tiré de `harness_proto/mcp_pinning.py` réunit les deux fonctions centrales qui appliquent cet épinglage du catalogue et cette validation des en-têtes MCP 2026-07-28.

<!-- CA-G0-SYNC id="G0-EX-CH01-03" path="8 - Manuel/trousse/harness_proto/mcp_pinning.py" lines="227-260" sha256="350e1959e6f0c54ce549afc77b4ef14959851bc9e45ad1a2eee52b9b36f4fc95" -->
```python
def verify_tools_list_against_catalog(
    tools: list[dict[str, Any]], catalog: Mapping[str, McpCatalogEntry],
    server_id: str, max_drift_before_suspend: int = 1,
) -> McpSyncResult:
    """Trie tools/list, detecte rug pull et prefixe server_id.tool."""
    active, suspended, reasons, seen = {}, [], {}, set()
    for tool in sorted(tools, key=_tool_name):
        name = _tool_name(tool)
        err = _tool_sync_error(tool, catalog.get(name), server_id, seen)
        seen.add(name)
        if err:
            active.pop(f"{server_id}.{name}", None)
            suspended.append(name)
            reasons[name] = err
        else:
            active[f"{server_id}.{name}"] = copy.deepcopy(tool)
    susp = len(suspended) >= max_drift_before_suspend
    act = {} if susp else active
    return McpSyncResult(act, tuple(suspended), susp, reasons)

def validate_mcp_headers(
    headers: Mapping[str, str], jsonrpc_body: dict[str, Any],
    catalog_entry: McpCatalogEntry | None = None,
) -> dict[str, Any]:
    """Verifie concordance MCP headers/body (-32020) et _meta."""
    hdr = _normalize_headers(headers)
    p, m, meth, mn = _extract_mcp_fields(jsonrpc_body)
    pv, mm = hdr.get("mcp-protocol-version"), hdr.get("mcp-method")
    if (not pv or pv != m.get(_PROTO_META_KEY) or not mm or mm != meth
            or (("name" in p or "mcp-name" in hdr) and (
                not isinstance(mn, str) or not mn
                or hdr.get("mcp-name") != mn))):
        raise HeaderMismatchError("En-tetes MCP divergents (-32020)")
    return _purge_and_validate(hdr, jsonrpc_body, catalog_entry)
```

Quatre choix de conception déterministes rendent cet extrait résistant aux détournements courants. Premièrement, `verify_tools_list_against_catalog` opère une copie défensive (`copy.deepcopy`) après validation et vide intégralement `active` (`act = {}`) dès que `len(suspended) >= max_drift_before_suspend` ; un serveur qui dérive sur un seul outil perd ainsi immédiatement tout crédit d'exécution en bloc, évitant qu'un outil demeuré sain en apparence ne serve de cheval de Troie sur un hôte compromis. Deuxièmement, `seen` intercepte toute duplication de nom dans la réponse `tools/list` avant l'évaluation d'empreinte, empêchant l'ombre d'un outil légitime suivi d'un homonyme malveillant.

Troisièmement, `_normalize_headers` dans `validate_mcp_headers` refuse d'avance toute duplication d'en-tête HTTP de même nom aux valeurs divergentes (*HTTP header smuggling*), puis contrôle symétriquement `name in p` et `mcp-name in hdr` afin qu'aucune des deux faces ne puisse omettre la vérification d'identité d'outil. Quatrièmement, `_purge_and_validate` valide les projections `x-mcp-header` à la fois dans `params.inputSchema` et à la racine, garantissant que ni `tenant`, ni `authenticated`, ni `clientInfo` injectés dans `_meta` ne survivent après nettoyage.

Signalons enfin que la section `security-considerations.mdx` de MCP 2026-07-28 prohibe explicitement le relais aveugle de jetons (*token passthrough*) et impose la liaison d'audience RFC 8707 [8]. En cohérence avec la règle d'étanchéité éditoriale du manuel, le contrôle cryptographique des jetons OAuth 2.0 OBO (RFC 8693), la vérification de la RFC 8707 et la preuve de possession DPoP (RFC 9449) sont traités et testés de manière autonome au Chapitre 02 dans `authz_pqc_audit/obo_dpop.py`. À l'inverse, l'épinglage du transport MCP lui-même et son isolation face aux révisions futures relèvent directement de la section suivante.

## 1.3 Adaptateur de transport face au retrait HTTP+SSE (SEP-2596) et au jalon SEP-3398 (mars 2027)

Un protocole aussi jeune que MCP ne reste pas figé après la date de gel éditorial du 2 décembre 2026. Comme le relève l'analyse des discordances inter-volumes présentée au Liminaire, l'un des écarts structurants du corpus oppose les ouvrages adossés à la révision `2025-11-25` avec état à ceux alignés sur la révision sans état `2026-07-28`. Coupler directement la logique métier du harnais aux détails bruts de la couche HTTP exposerait `8 - Manuel/trousse/` à casser dès l'entrée en vigueur des prochains jalons de spécification prévus en 2027. C'est pour absorber ces mutations annoncées sans réécrire ni le harnais ni les validateurs que le module `harness_proto/mcp_pinning.py` isole les échanges derrière un adaptateur de transport.

### Portée normative de Streamable HTTP (`2026-07-28`) et obsolescence d'HTTP+SSE

La révision `2026-07-28` du transport *Streamable HTTP* (`streamable-http.mdx` [7]) transforme en profondeur le modèle opérationnel hérité de l'ancien transport `HTTP+SSE` issu de la version `2024-11-05`. Elle supprime les sessions au niveau du protocole (mode sans session dit *stateless* selon la table canonique `DISC-05`) : selon la recommandation `SHOULD` de rétrocompatibilité, l'en-tête `Mcp-Session-Id` devrait être ignoré tandis que les requêtes HTTP `GET` ou `DELETE` sur le point d'accès devraient recevoir le statut HTTP `405` (Method Not Allowed), au profit d'en-têtes porteurs de version (`MCP-Protocol-Version`) et de routage (`Mcp-Method`, `Mcp-Name`) requis sur chaque requête JSON-RPC `POST` [7]. Simultanément, le point d'accès permanent en flux `GET` est retiré au profit d'un modèle d'abonnements explicites (`subscriptions/listen`) sans reprise par `Last-Event-ID` [7], tandis que les requêtes à allers-retours multiples (MRTR) remplacent les requêtes serveur inversées par un résultat typé `InputRequiredResult` [7] et un état applicatif opaque `requestState` [6, 9].

Sur le plan architectural, l'absence de session protocolaire entre requêtes supprime le besoin d'affinité de session persistante (*sticky session*) entre nœuds de passerelle, tandis que le miroir en en-tête permet aux répartiteurs de charge de router sans analyser le corps JSON [7]. En contrepartie, la sécurité bascule entièrement vers l'authentification explicite de chaque requête [8] et vers la protection de `requestState`, traité comme bloc opaque côté client [9], lors de son renvoi au serveur. Parallèlement, la politique d'évolution de MCP a été formalisée en 2026 par deux propositions d'amélioration complémentaires :

- **Cycle de vie et fenêtre de dépréciation (`SEP-2596`, statut `Final`)** : rédigée par Den Delimarsky (créée le 17 avril 2026 et portée au statut `Final` dans l'instantané du dépôt antérieur au gel) [10], `SEP-2596` instaure trois états explicites pour chaque fonctionnalité (`Active`, `Deprecated`, `Removed`) [10]. Sauf retrait accéléré à `90` jours au moins, motivé par un avis de sécurité publié ou une exploitation active sans correctif sur place, toute fonctionnalité dépréciée doit rester dans la spécification pendant une fenêtre minimale de `12` mois à compter de la révision *Current* qui la marque dépréciée avant de devenir admissible au retrait [10]. Pour les fonctionnalités dépréciées à la révision `2026-07-28`, l'horizon minimal de retrait de douze mois tombera ainsi à partir du **28 juillet 2027** selon la politique `SEP-2596` [10], ancrant sur la spécification primaire l'échéance de migration interne `EXIG-MCP-22` de l'architecture de référence (`2 - Cadre de Référence.md`, section 6.5). Concernant l'ancien transport `HTTP+SSE` déjà marqué déprécié auparavant sans date butoir, `SEP-2596` lui a explicitement octroyé une période de grâce de trois mois à compter du passage de cette proposition au statut `Final` (sans date calendaire de fusion consignée dans son en-tête) [10].
- **Cadence semestrielle et jalon cible (`SEP-3398`, statut `Accepted`)** : acceptée le 14 octobre 2026 sous l'impulsion de Kurtis Van Gent, `SEP-3398` remplace les publications ad hoc par une cadence semestrielle prévisible fixée en principe au dernier mardi de mars et de septembre [11]. En conséquence directe, la révision initialement envisagée pour décembre 2026 est reportée à l'après-gel : la prochaine révision MCP est attendue pour le **30 mars 2027**, sous réserve du calendrier de transition [11], et le cycle suivant ouvrira la porte à l'échéance de juillet–septembre 2027 [10, 11].

La conséquence architecturale de ces deux jalons post-gel est immédiate et doit être formulée au futur avec précision. `SEP-2596` figurant déjà au statut `Final` dans l'instantané du dépôt du 22 novembre 2026 antérieur au gel [10], la période de grâce de trois mois applicable à `HTTP+SSE` sera échue avant la révision attendue pour le `30 mars 2027` (`SEP-3398`), rendant ce transport admissible au retrait dès ce jalon sans enfreindre la politique de cycle de vie [10, 11]. Ensuite, à partir du `28 juillet 2027` (lors de la révision prévue en septembre 2027), les mainteneurs pourront retirer les primitives déjà dépréciées à la révision `2026-07-28` telles que `Roots`, `Sampling` et la journalisation protocolaire (`logging`) [9, 10, 11]. En vertu de `SEP-2596`, tout retrait exigera néanmoins une décision explicite des mainteneurs principaux lors de la préparation de la révision et non une suppression automatique à l'échéance du délai [10]. Toute entreprise qui maintiendrait des clients dépendant encore d'un flux `GET` persistant ou de `Mcp-Session-Id` se heurterait alors à des ruptures de compatibilité non négociables à l'échéance de 2027.

### Interface `McpTransportAdapter` et contrat hermétique `StreamableHttpAdapter`

Pour empêcher que le passage d'une révision MCP à une autre ne contamine la logique métier ni les validateurs du harnais, `harness_proto/mcp_pinning.py` introduit le protocole structurel Python (`typing.Protocol`) nommé `McpTransportAdapter`. Cette interface minimale expose exactement un attribut contractuel (`expected_revision: str`) et deux méthodes : `send_jsonrpc(method, params, headers)` et `capabilities()`. Aucun code appelant du harnais n'émet de requête HTTP brute ni ne manipule de connecteurs réseaux spécifiques à `HTTP+SSE` : il dialogue uniquement avec un objet satisfaisant `McpTransportAdapter`.

L'implémentation concrète livrée dans la trousse, `StreamableHttpAdapter`, verrouille par défaut `expected_revision = "2026-07-28"` et `transport_mode = "streamable_http"`. Lorsqu'un adaptateur est configuré en mode `http+sse` (par exemple pour simuler un serveur hérité de la révision `2025-11-25`), `capabilities()` annonce `"streamable_http": False` ainsi que `"http_sse_supported": False`, et tout appel à la méthode `send_jsonrpc` lève immédiatement `DeprecatedTransportError`, une sous-classe dédiée de `ValueError` documentant le refus du transport déprécié au titre de `SEP-2596`. De même, si l'en-tête `MCP-Protocol-Version` transmis diffère de `self.expected_revision`, l'adaptateur lève `HeaderMismatchError` avant même de construire la réponse JSON-RPC 2.0.

Conformément à la règle de sobriété portative `AO-08` et à la délimitation `DC-P12`, cette couche d'adaptation s'exécute et se vérifie intégralement en Python 3.12+ pur dans `test_mcp_streamable_http_and_pinning`, sans nécessiter de proxy `Nginx`, `Envoy` ni serveur réseau live en barrière `G0`. Cet isolement garantit deux bénéfices mesurables lors de la transition attendue le `30 mars 2027` (`SEP-3398`) et à l'horizon du `28 juillet 2027` (`SEP-2596`). D'une part, la prise en charge future d'une révision publiée à l'échéance de mars 2027 se traduira uniquement par l'enregistrement d'une nouvelle classe conforme à `McpTransportAdapter`, sans altérer ni `verify_tools_list_against_catalog` ni `DeterministicHarness`. D'autre part, les serveurs historiques restés temporairement sur un transport antérieur sont refusés par défaut en `G0`, imposant leur isolement derrière une passerelle de traduction distincte jusqu'à leur migration complète prévue avant le `28 juillet 2027`.

## 1.4 Validation `AgentCard` (A2A v1.0.1), enveloppe JWS (RFC 7515) / JCS (RFC 8785) et conformité `a2a-tck`

Là où le protocole MCP gouverne l'axe vertical reliant un agent à ses serveurs d'outils, le protocole *Agent2Agent* (A2A), hébergé sous l'égide de la *Linux Foundation* (`AAIF`), normalise l'axe horizontal de délégation et de collaboration entre agents pairs [14]. Publiée le 28 mai 2026 au correctif `v1.0.1` (`commit 33035925`), la spécification normative A2A [14] et son contrat Protobuf associé `a2a.proto` [15] définissent une **Carte d'agent** (`AgentCard`) qui publie l'identité d'un agent pair, ses interfaces supportées, ses capacités, ses schémas d'authentification et ses compétences (`skills`). Accepter aveuglément une `AgentCard` récupérée sur le réseau sans vérifier ni sa structure, ni ses flux OAuth, ni sa signature cryptographique exposerait immédiatement l'agent appelant à une usurpation de pair ou à une redirection de trafic vers un point d'accès malveillant.

### Contrat structurel A2A v1.0.1 et restrictions de sécurité hors modèle

Le schéma strict `schemas/a2a_agent_card.schema.json` modélise le profil durci de `8 - Manuel/trousse/` attendu pour toute **Carte d'agent** admise dans le harnais (`EXIG-A2A-03`, critère `C13`), en renforçant le contrat Protobuf amont `a2a.proto` [15] (où huit champs seulement portent `REQUIRED`). Sur le plan structurel, l'objet racine doit déclarer `additionalProperties: false` et contenir les douze propriétés requises par ce schéma : `name`, `description`, `supportedInterfaces` (au moins une interface avec `url` en `https://`, `protocolBinding` parmi `JSONRPC`, GRPC ou `HTTP+JSON`, et `protocolVersion` conforme à `1.x`), `provider`, `version` sémantique, `capabilities`, `securitySchemes`, `securityRequirements`, `defaultInputModes`, `defaultOutputModes`, `skills` et `signatures` (au moins une signature détachée).

Au-delà de la seule forme syntaxique vérifiée par `Draft202012Validator`, la fonction `_check_card_structure_and_policies` dans `harness_proto/a2a_card.py` applique deux barrières de politique non négociables avant même d'examiner la signature cryptographique :

- **Bannissement des flux OAuth obsolètes** : toute déclaration `oauth2SecurityScheme.flows` contenant `password` (*Resource Owner Password Credentials*) ou `implicit` est immédiatement rejetée, le schéma strict n'admettant que les flux `authorizationCode` (avec propriété booléenne optionnelle `pkceRequired`), `clientCredentials` ou `deviceCode`.
- **Liste blanche stricte des extensions** : chaque entrée de `capabilities.extensions` est confrontée par son URI à l'ensemble fermé `approved_extensions` détenu par l'appelant ; toute extension non explicitement approuvée au catalogue interne entraîne l'invalidation de la carte.

### Enveloppe JWS (RFC 7515) sur canonisation JCS (RFC 8785) et épinglage `jku` / `kid`

La section 8.4 de la spécification A2A `v1.0.1` prescrit le mécanisme cryptographique garantissant l'intégrité et l'authenticité d'une `AgentCard` [14]. Conformément à la section 8.4.1, la carte est d'abord préparée selon les règles de présence Protobuf : les champs `optional` non renseignés et les valeurs par défaut non requises (telles qu'une liste vide optionnelle) sont omis, tandis que les champs `REQUIRED` sont toujours conservés [14]. L'attribut `signatures` lui-même est ensuite exclu pour éviter toute circularité avant canonisation selon la RFC 8785 (JCS) [12, 14]. L'enveloppe suit ensuite le format *JSON Web Signature* (JWS, RFC 7515) en sérialisation JSON contenant au minimum une chaîne `protected` encodée en Base64url et la valeur `signature` [13, 14]. L'en-tête protégé DOIT inclure l'algorithme `alg` et l'identifiant de clé `kid`, DEVRAIT inclure `typ` (`"JOSE"`) et PEUT inclure `jku` désignant le jeu de clés publiques `JWKS` [14].

Dans `harness_proto/a2a_card.py`, la fonction `validate_agent_card` applique une règle d'**Épinglage cryptographique** beaucoup plus stricte que la récupération dynamique naive d'un `jku` distant. En effet, si un vérificateur résolvait aveuglément l'URL `jku` déclarée dans l'en-tête d'une carte non fiable, un attaquant pourrait signer sa propre carte frauduleuse et faire pointer `jku` vers son propre serveur `JWKS` — combinant usurpation d'identité et vulnérabilité SSRF. La fonction `validate_agent_card` exige donc que `hdr.get("alg") == "ES256"`, que `kid` soit non vide, et surtout que `hdr.get("jku") == pinned_jku`, c'est-à-dire une égalité exacte avec la source de clés préalablement épinglée hors bande dans le registre d'entreprise. Elle résout ensuite la clé ECDSA `P-256` correspondante dans le `jwks` local déjà vérifié, recalcule le condensat canonique `card_etag` par `jcs_sha256_hex`, reconstruit l'entrée de signature ASCII `<protected_b64>.<payload_b64>` (concaténation des deux segments Base64url sans remplissage séparés par un point) et vérifie la signature cryptographique sur `64` octets (`r || s`).

En sortie, `validate_agent_card` retourne un verdict immuable `AgentCardVerdict` contenant le booléen `valid`, l'empreinte canonique `card_etag`, l'identifiant `signer_kid` et le tuple `errors`. Ce calcul déterministe de `card_etag` s'aligne sur les exigences de mise en cache `CARD-CACHE-001` et `CARD-CACHE-002` recensées dans `a2a-tck` (`Cache-Control` avec `max-age` et en-tête `ETag`), tout en offrant aux journaux d'audit un identifiant de version infalsifiable de la carte évaluée [14, 17].

L'extrait `G0-EX-CH01-04` présente l'intégralité de `validate_agent_card`, telle que validée en `G0` sur les cas nominaux, les vecteurs dérivés et les rejets de sécurité.

<!-- CA-G0-SYNC id="G0-EX-CH01-04" path="8 - Manuel/trousse/harness_proto/a2a_card.py" lines="157-182" sha256="1a58d5eabab4361028420c902df71ef3b305f84bfd139e14c75c7318c545b899" -->
```python
def validate_agent_card(
    card: dict[str, Any], jwks: dict[str, Any], pinned_jku: str,
    approved_extensions: set[str], schema: dict[str, Any],
) -> AgentCardVerdict:
    """Valide schema A2A, epinglage jku/kid, JWS ES256 sur JCS."""
    errs = _check_card_structure_and_policies(
        card, approved_extensions, schema
    )
    if errs:
        return AgentCardVerdict(False, "", "", tuple(errs))
    base = {k: v for k, v in card.items() if k != "signatures"}
    try:
        pay_bytes = canonicalize_jcs(base)
        etag = jcs_sha256_hex(base)
        prot_b64, hdr, sig_b64 = _parse_jws_sig(card)
    except (JcsError, ValueError, UnicodeDecodeError) as exc:
        return AgentCardVerdict(False, "", "", (str(exc),))
    raw_kid = hdr.get("kid")
    kid = raw_kid if isinstance(raw_kid, str) else ""
    if hdr.get("alg") != "ES256" or hdr.get("jku") != pinned_jku or not kid:
        return AgentCardVerdict(False, etag, kid, ("jku/alg/kid invalide",))
    b64_pay = base64.urlsafe_b64encode(pay_bytes).rstrip(b"=").decode()
    err = _verify_es256_jwk(
        jwks, kid, f"{prot_b64}.{b64_pay}".encode(), sig_b64
    )
    return AgentCardVerdict(err is None, etag, kid, (err,) if err else ())
```

Trois aspects critiques méritent d'être soulignés à la lecture de cet extrait. D'abord, la canonisation JCS et le calcul de `etag` interviennent avant la vérification cryptographique sur le dictionnaire `base` amputé de `signatures` : même si la signature échoue, le vérificateur produit une empreinte déterministe de la carte soumise permettant de tracer l'incident sans ambiguïté. Ensuite, le test `raw_kid = hdr.get("kid")` suivi de `isinstance(raw_kid, str)` prémunit contre une confusion de type où un attaquant fournirait un entier ou un objet JSON dans `kid`, tandis que le contrôle conjoint `alg == "ES256"` et `jku == pinned_jku` bloque à la fois le repli sur algorithme faible (`none` ou `HS256`) et le détournement d'autorité de clé (`SSRF jku`).

Enfin, `_verify_es256_jwk` dans `a2a_card.py` contrôle explicitement que la clé résolue dans `jwks` possède `kty == "EC"`, `crv == "P-256"`, un algorithme compatible (`None` ou `"ES256"`), un usage signature compatible (`None` ou `"sig"`) et une signature brute exactement longue de `64` octets avant d'appeler la vérification ECDSA SHA-256. Dans `test_a2a_agent_card_jws_es256_and_pinned_jku`, chaque vecteur d'attaque — `jku` non épinglé, altération d'un seul mot de `description`, extension absente de la liste blanche, ou flux OAuth `password`/`implicit` — provoque un verdict `AgentCardVerdict(valid=False, ...)`.

### Garde-fous anti-SSRF sur *webhooks*, automate `TaskState` et exactitude `a2a-tck`

Lorsqu'une `AgentCard` franchit avec succès la porte `validate_agent_card` et que deux agents engagent une collaboration asynchrone longue, la spécification A2A `v1.0.1` encadre deux autres verrous au niveau de la passerelle d'exécution. Le premier concerne la sécurité des notifications poussées (*push notifications*) par *webhook* décrite à la section 13.2 de `A2A v1.0.1` [14]. Un serveur agent appelé à poster des mises à jour `StreamResponse` vers une URL de rappel fournie par le client DOIT inclure les justificatifs d'authentification configurés dans `PushNotificationConfig.authentication` et DEVRAIT valider cette URL contre le risque SSRF (*Server-Side Request Forgery*) [14]. Cette validation rejette explicitement la boucle locale (`localhost` et `127.0.0.0/8`), les adresses *link-local* et les réseaux privés (`10.0.0.0/8`, `192.168.0.0/16` et `172.16.0.0/12`), tandis que le recours à HTTPS (requis en production à la section 7.1) et aux listes d'autorisation est recommandé le cas échéant [14].

De même, les références de fichiers dans les messages A2A doivent être validées contre le SSRF [14]. Dans `8 - Manuel/trousse/`, la logique exécutable de filtrage IP IANA et de blocage des métadonnées nuagiques (`169.254.169.254`) est implémentée et testée au Chapitre 03 dans le moteur de confinement (`policy_saga/sandbox_manifest.py`), en complément de l'épinglage `jku` de `a2a_card.py`.

Le second verrou normatif réside dans l'automate des états de tâche formalisé par le contrat Protobuf `specification/a2a.proto` de `A2A v1.0.1` [15]. L'énumération `TaskState` distingue neuf états précis : `TASK_STATE_UNSPECIFIED`, l'état initial `TASK_STATE_SUBMITTED`, l'état actif `TASK_STATE_WORKING`, deux états interrompus appelant une intervention externe (`TASK_STATE_INPUT_REQUIRED` et `TASK_STATE_AUTH_REQUIRED`), ainsi que quatre issues finales sans retour : achèvement (`TASK_STATE_COMPLETED`), échec d'exécution (`TASK_STATE_FAILED`), annulation (`TASK_STATE_CANCELED`) et refus d'admission (`TASK_STATE_REJECTED`) [15]. À la passerelle, tout message reçu sur une tâche déjà parvenue dans l'un des quatre états terminaux doit être refusé (`UnsupportedOperationError`) ou ouvrir une nouvelle tâche, garantissant la cohérence avec les règles de réversibilité Saga étudiées au Chapitre 03 [14, 15].

Pour éprouver l'implémentation face à un référentiel tiers indépendant plutôt que sur nos seuls tests internes (`AO-06`), la barrière `G0` intègre les artefacts extraits de la suite officielle `a2aproject/a2a-tck` au tag `1.0.0.alpha3` (commit `5daf0144`, 20 octobre 2026) [17]. L'inspection mécanique directe de ce tag amont impose une précision probatoire essentielle : au tag `1.0.0.alpha3` (`statut alpha3`), le répertoire `conformance-vectors/a2a-jcs-v01` est **absent** du dépôt amont (`a2a_jcs_v01_present: false`), et les quatre exigences normatives de signature `CARD-SIGN-001` à `CARD-SIGN-004` y sont explicitement marquées `NOT_AUTOMATABLE` dans `tck/requirements/agent_card.py` [17].

Afin de ne laisser aucun angle mort, `8 - Manuel/trousse/vectors/a2a_tck/` archive le catalogue extrait des `114` exigences `MUST` (`129` exigences au total, dont `13` propres à `AgentCard`) et complète ce socle amont en `statut alpha3` par des vecteurs JCS/JWS issus des sections 8.4.1, 8.4.2 et 8.5 de la spécification normative `v1.0.1` ainsi que par trois cas négatifs dérivés [14, 17]. Dans `tests/test_third_party_vectors.py`, l'épreuve `test_a2a_tck_alpha3_jcs_and_negative_cases` vérifie la canonisation de la section 8.4.1 après omission des champs par défaut, décode l'en-tête protégé `ES256` de la section 8.4.2 et vérifie le rejet par `validate_agent_card` de trois cartes invalides : `NEG-CARD-STRUCT-001` (absence des champs `skills` et `supportedInterfaces`), `NEG-CARD-PROTO-001` (liste `supportedInterfaces` vide) et `NEG-CARD-SIGN-003` (en-tête JWS protégé dépourvu du paramètre obligatoire `kid`).

Par ailleurs, la parution le 29 octobre 2026 de la version candidate `A2A v1.1.0-rc` (commit `78e1d6a1`) [16], qui introduit notamment l'opération `Send Live Message` et la capacité `capabilities.userArtifacts`, constitue une évolution pré-ratification postérieure au contrat normatif `v1.0.1` retenu au gel. Plutôt que de mélanger des champs candidats non ratifiés dans le schéma strict de production, `harness_proto/a2a_card.py` isole cette évolution derrière l'adaptateur versionné `AgentCardAdapter`, qui projette les cartes `1.1` vers les clés canoniques `v1.0.1` et ramène `protocolVersion` au palier `1.0` vérifié en `G0` — préparant l'évolution future attendue sans rompre les contrats validés.

La `Figure 2` unifie l'ensemble de la médiation protocolaire verticale (`mcp_pinning.py`) et horizontale (`a2a_card.py`) avec ses suites de vecteurs tiers.

![Médiation protocolaire MCP et A2A](../diagrammes/rendus/Fig-02.svg)
*Figure 2 — Médiation protocolaire épinglée MCP 2026-07-28 avec JCS SHA-256, rejet HeaderMismatch et validation AgentCard A2A v1.0.1 par JWS et a2a-tck.*

La `Figure 2` met en parallèle les deux couloirs d'entrée sortant du harnais appelant déterministe. Sur le couloir gauche, tout serveur MCP externe est traité comme source non fiable exposée à `40,58 %` de dérive silencieuse : les réponses `tools/list` passent au tamis de l'épinglage JCS SHA-256, les requêtes sortantes subissent la concordance d'en-têtes et l'épuration `_meta` sous peine de rejet `HeaderMismatch` (`HTTP 400` / `-32020`), puis l'adaptateur `McpTransportAdapter` bloque tout repli sur `HTTP+SSE`. Sur le couloir droit, toute `AgentCard` d'un pair A2A externe traverse la validation de schéma et d'extensions, la vérification cryptographique JWS `ES256` sur canonisation JCS avec épinglage `jku`/`kid`, puis l'articulation avec la garde anti-SSRF et l'automate d'états prescrits par la spécification `v1.0.1`, tandis que les suites tierces RFC 8785 et `a2a-tck 1.0.0.alpha3` ancrent indépendamment l'exactitude des deux validateurs.

Le `Tableau 1.3` consolide la traçabilité exacte de chaque invariant du Chapitre 01 vers les symboles de `harness_proto/`, les suites `pytest` observées en `G0` à `exit 0` et les vecteurs tiers associés.

*Tableau 1.3 — Matrice de traçabilité et résultats G0 du module `harness_proto/` (`14/14` tests pytest et vecteurs tiers)*

| Contrat architectural (`EXIG-*` / PRR / `C40`) | Symbole `harness_proto/` | Cas de test `pytest` (`test_harness_proto.py` / tiers) | Statut `G0` vérifié |
| --- | --- | --- | --- |
| Harnais 8 étapes et `AMBIGU_ESCALADE` (`R-01`, `C01`, `C07`, `C09`, `C19`, `C34`) | `pipeline.DeterministicHarness.run` | `test_harness_enforces_schema_and_grounding`, `test_harness_partition_80_20_rules_outside_prompt`, `test_harness_8_steps_ok_and_ambigu_escalade`, `test_harness_repair_loop_stops_after_max_retries` | `exit 0` (`4` tests) |
| Profil JSON Schema `strict: true` et zéro \$ref réseau (`EXIG-MCP-19`, `C10`) | `pipeline.validate_strict_schema` | `test_strict_json_schema_2020_12`, `test_reject_external_network_schema_ref`, `test_harness_rejects_oversized_payload_and_root_allof` | `exit 0` (`3` tests) |
| Épinglage JCS SHA-256 `tools/list` et anti-*rug pull* (`EXIG-MCP-03`, `20`, `C12`) | `mcp_pinning.verify_tools_list_against_catalog`, `jcs.canonicalize_jcs` | `test_mcp_tools_list_deterministic_sort_and_cache`, `test_mcp_rug_pull_single_char_drift_suspends`, `test_rfc8785_appendix_b_and_utf16_vectors`, `test_rfc8785_cyberphone_testdata_byte_for_byte` (suite rfc8785 : `20/20` fichiers archivés) | `exit 0` (`2` + `2` tests) |
| Concordance en-têtes MCP, `_meta` et `x-mcp-header` (`EXIG-MCP-15`, `16`, `18`) | `mcp_pinning.validate_mcp_headers` | `test_mcp_header_mismatch_raises_400_32020`, `test_mcp_meta_allowlist_purges_unreserved`, `test_reject_x_mcp_header_pii_or_token` | `exit 0` (`3` tests) |
| Isolation transport `SEP-2596` (`28 juillet 2027`) / `SEP-3398` (`30 mars 2027`) face à `2026-07-28` (`C11`) | `mcp_pinning.StreamableHttpAdapter` | `test_mcp_streamable_http_and_pinning` (refus `http+sse`, révision `2026-07-28`) | `exit 0` (`1` test) |
| Validation `AgentCard` JWS/JCS, `jku` épinglé et `v1.1.0-rc` (`EXIG-A2A-03`, `C13`, `C14`) | `a2a_card.validate_agent_card`, `a2a_card.AgentCardAdapter` | `test_a2a_agent_card_jws_es256_and_pinned_jku`, `test_a2a_tck_alpha3_jcs_and_negative_cases` (suite `a2a_tck` : `5/5` fichiers archivés) | `exit 0` (`1` + `1` tests) |

Toutes les assertions consignées au `Tableau 1.3` ont passé `14/14` épreuves unitaires de `test_harness_proto.py` ainsi que les vérifications des suites tierces rfc8785 (`20/20` fichiers) et `a2a_tck` (`5/5` fichiers) dans l'exécution de barrière `G0` rapportée à `exit 0` dans `aq/rapports-g0.json`. Conformément aux clauses `DC-P12` et `non-avis` (`AO-05`), ces résultats constituent une preuve logicielle déterministe sur doublures synthétiques hermétiques, et non une homologation sur un système d'enregistrement réel ni un avis juridique ou réglementaire.

> **Trois invariants exécutables — Chapitre 1**
>
> 1. **Enserrer l'appel modèle dans huit étapes / jalons `step_trace` hors invite (`DeterministicHarness.run`)** : imposer JSON Schema Draft 2020-12 en profil `strict: true` (`additionalProperties: false`, `required` exhaustif, zéro \$ref réseau), vérifier l'ancrage métier contre `grounding_records`, borner la réparation à `max_repair_retries = 2` et offrir une sortie typée explicite `AMBIGU_ESCALADE` pour bloquer toute hallucination silencieuse (`7/7` tests du harnais dans `test_harness_proto.py` à `exit 0`, sur `14/14` pour l'ensemble du module).
> 2. **Épingler canoniquement `tools/list` et les en-têtes MCP 2026-07-28 (`mcp_pinning.py`)** : calculer l'empreinte SHA-256 après canonisation JCS (RFC 8785) sur chaque définition d'outil et suspendre le serveur dès la dérive d'un seul caractère (`40,58 %` de dérive silencieuse mesurée au registre public). Rejeter toute discordance d'en-tête par `HeaderMismatchError` (`400` / `-32020`), purger `_meta` hors liste blanche et isoler les jalons post-gel (`SEP-2596` / `28 juillet 2027` et `SEP-3398` / `30 mars 2027`) derrière `McpTransportAdapter`.
> 3. **Vérifier toute `AgentCard` A2A v1.0.1 par JWS `ES256` sur JCS avec `jku` épinglé (`a2a_card.py`)** : refuser toute résolution libre de `jku`, bannir les flux `password`/`implicit` et les extensions non listées, isoler `A2A v1.1.0-rc` derrière `AgentCardAdapter` et pallier le `statut alpha3` de `a2a-tck` (`CARD-SIGN-001..004` `NOT_AUTOMATABLE`) par les vecteurs canonisés JCS/JWS locaux de `8 - Manuel/trousse/`.

Le harnais typé à huit étapes et la médiation protocolaire épinglée assurent désormais que le modèle ne reçoit ni outil altéré, ni carte d'agent falsifiée, et ne produit que des sorties conformes ou explicitement escaladées. Toutefois, savoir *quel outil* et *quel agent pair* sont légitimes ne suffit pas à établir *sous quel mandat utilisateur* et *avec quelle identité non humaine* l'appel s'exécute à travers plusieurs sauts. Il reste aussi à montrer comment absorber le choc de taille des signatures post-quantiques ML-DSA sous le plafond HTTP `431` tout en corrélant télémétrie et audit : c'est précisément l'objet du Chapitre 02 et du module `authz_pqc_audit/`.
