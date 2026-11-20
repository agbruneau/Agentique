# C Exemples de contrats

Cette annexe donne huit exemples complets de contrats et d’objets d’échange, conformes, lorsqu’elles existent, aux spécifications en vigueur au 27 octobre 2026 et, dans tous les cas, aux exigences du cadre. Ces exemples sont informatifs (section 1.4). Leur structure devient normative là où une exigence y renvoie expressément : C.1 et C.2 par l’EXIG-ORC-22 et l’EXIG-MCP-20, C.6 par l’EXIG-AUT-12, C.8 par l’EXIG-OBS-12; un contrat réel reprend alors leur structure et leurs champs, avec ses propres noms, schémas et seuils. Chaque exemple est suivi d’une lecture qui le rattache aux exigences qu’il met en œuvre.

### Conventions des exemples

- **Valeurs fictives.** Les noms, domaines (`ent.ca`), identifiants et montants sont fictifs. Un seul domaine fictif, `ent.ca`, sert partout, et son inverse, `ca.ent`, préfixe les types d’événements. Les montants des arguments d’outil sont des entiers en cents, ce qui ne laisse aucune place à une lecture divergente des nombres (EXIG-AUT-12).
- **Formats normalisés et formats internes.** Les exemples C.1, C.3, C.4 et C.5 n’emploient que des champs définis par leur spécification ou par les mécanismes d’extension qu’elle prévoit. Les exemples C.2, C.6, C.7 et C.8 sont des formats internes : comme à l’annexe B, les noms de champs sont un choix du cadre, et seules comptent leur présence et leur cohérence.
- **Empreintes vérifiables.** Les empreintes `definition_digest`, `idempotency_key`, h (reprise dans `action_sha256` et `empreinte_approbation`) et `arguments_sha256` sont de véritables condensés SHA-256, calculés sur les valeurs montrées (forme canonique RFC 8785 pour les objets JSON) : on peut les recalculer. La description de C.1, coupée pour la lecture, se canonise en une seule ligne, chaque coupure valant une espace; la clé d’idempotence est l’empreinte de la canonisation du tableau `["idem-v1", task_id, step_id]` (section 7.6), et h celle de l’objet {outil, version, definition_digest, agent_id, task_id, arguments} (section 8.5). Les valeurs qui dépendent d’objets non montrés ou abrégés (empreinte de certificat, enregistrement précédent, empreinte de l’invite système, `empreinte` de l’enregistrement C.8) sont fictives, et les signatures, qu’on ne peut pas reproduire sans la clé privée, sont abrégées par « … ».
- **Portées OAuth.** Les portées suivent une seule grammaire, celle de l’extrait de la section 9.3 : `domaine:action`, l’action en anglais (`finance:read`, `approvisionnement:write`, `risque-credit:invoke`, `risque-credit:analyze`).
- **Scénario commun.** Les exemples C.1, C.2, C.6, C.7 et C.8 suivent une même tâche : l’agent `agt-achats-indirects`, de classe de risque modérée et plafonné à N3, crée un bon de commande de 12 480 $, soit au-delà du seuil d’approbation de 5 000 $ par tâche fixé au catalogue pour cet outil et mesuré sur le total calculé des lignes (tableau 64).
- **Validation CI et badges DC-P11.** Les huit contrats C.1 à C.8 sont audités mécaniquement en intégration continue dans le dépôt (`Borealis-Bench/ci-audit-108-blocs/registre-108-blocs.json`) : six blocs JSON autonomes portent le badge `[Exécuté en CI]` (`C.1`, `C.2`, `C.3`, `C.4`, `C.7`, `C.8`), et deux blocs composites annotés multi-objets à signatures omises portent le badge `[Schéma conceptuel]` (`C.5`, `C.6`, dont les objets JSON embarqués et la chaîne cryptographique RFC 8785 JCS SHA-256 entre `C.1`, `C.2`, `C.6` et `C.8` sont néanmoins vérifiés en CI). Un schéma JSON Draft 2020-12 crypto-agile (`ES256`/`ML-DSA-65`/`ML-DSA-87`) est publié dans `Borealis-Bench/schemas/annexe-c-2026-crypto-agile.schema.json`.

*Tableau 64 — Exemples de contrats, références, exigences illustrées et statut CI (DC-P11)*

| **Exemple** | **Référence** | **Exigences et sections illustrées** | **Badge DC-P11** |
| --- | --- | --- | --- |
| C.1 Outil MCP | MCP 2026-07-28; JSON Schema 2020-12 | EXIG-MCP-07, EXIG-MCP-14, EXIG-MCP-18; EXIG-ORC-21 | `[Exécuté en CI]` |
| C.2 Entrée de catalogue | Format interne du cadre | EXIG-AUT-08, EXIG-AUT-13, EXIG-MCP-14, EXIG-MCP-20, EXIG-ORC-17, EXIG-ORC-22; section 6.8 | `[Exécuté en CI]` |
| C.3 Carte d’agent | A2A 1.0 (`a2a.proto`); JWS (RFC 7515); RFC 8785 | EXIG-A2A-02 à EXIG-A2A-06, EXIG-A2A-10 | `[Exécuté en CI]` |
| C.4 Événement | CloudEvents 1.0 (1.0.2) et extensions documentées; W3C Trace Context | EXIG-EVT-02, EXIG-EVT-04 à EXIG-EVT-06, EXIG-EVT-09, EXIG-EVT-06 | `[Exécuté en CI]` |
| C.5 Jeton délégué | RFC 9068, RFC 8693, RFC 8705 | EXIG-IAM-08, EXIG-IAM-10, EXIG-IAM-11, EXIG-IAM-14, EXIG-IAM-15 | `[Schéma conceptuel]` |
| C.6 Jeton d’approbation humaine | Format interne; RFC 8785, RFC 9396, CIBA | EXIG-AUT-09, EXIG-AUT-12 à EXIG-AUT-15, EXIG-AUT-19 | `[Schéma conceptuel]` |
| C.7 Enveloppe budgétaire | Format interne du cadre | EXIG-ORC-26, EXIG-FIN-04; section 10.6 | `[Exécuté en CI]` |
| C.8 Enregistrement d’audit | Format interne; RFC 8785 | EXIG-OBS-11 à EXIG-OBS-13, EXIG-AUT-10, EXIG-AUT-15, EXIG-IAM-21; section 10.3 | `[Exécuté en CI]` |

## C.1 Outil MCP — `[Exécuté en CI]`

L’exemple montre la définition d’un outil d’écriture orienté tâche, telle qu’un serveur MCP la renvoie dans `tools/list` (section 6.5).

**Définition de l’outil approvisionnement_creer_bon_commande (MCP 2026-07-28)**

```
{
  "name": "approvisionnement_creer_bon_commande",
  "title": "Créer un bon de commande (ERP)",
  "description": "Crée dans l'ERP un bon de commande, à l'état brouillon ou soumis, pour un fournisseur
homologué et un centre de coûts valide. Le statut soumis transmet le bon au circuit d'approbation interne de l'ERP,
sans envoi au fournisseur. Le serveur calcule le montant total à partir des lignes; les prix sont en cents.
Une relance avec la même clé d'idempotence ne crée pas de second bon. Ne modifie ni n'annule un bon existant.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "idempotency_key": { "type": "string", "pattern": "^[0-9a-f]{64}$" },
      "fournisseur_id": { "type": "string", "pattern": "^SUP-[0-9]{6}$" },
      "centre_cout": { "type": "string", "pattern": "^CC-[0-9]{4}$", "x-mcp-header": "Cost-Center" },
      "statut_demande": { "type": "string", "enum": ["brouillon", "soumis"], "default": "brouillon" },
      "lignes": {
        "type": "array",
        "minItems": 1,
        "maxItems": 100,
        "items": {
          "type": "object",
          "properties": {
            "sku": { "type": "string", "pattern": "^PRD-[0-9]{5}$" },
            "quantite": { "type": "integer", "minimum": 1, "maximum": 100000 },
            "prix_unitaire_cents": { "type": "integer", "minimum": 0, "maximum": 100000000 }
          },
          "required": ["sku", "quantite", "prix_unitaire_cents"],
          "additionalProperties": false
        }
      }
    },
    "required": ["idempotency_key", "fournisseur_id", "centre_cout", "lignes"],
    "additionalProperties": false
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "bon_commande_id": { "type": "string", "pattern": "^BC-[0-9]{4}-[0-9]{6}$" },
      "statut": { "type": "string", "enum": ["brouillon", "soumis"] },
      "montant_total_cents": { "type": "integer", "minimum": 0 },
      "rejeu": { "type": "boolean", "description": "Vrai si la clé était déjà traitée." }
    },
    "required": ["bon_commande_id", "statut", "montant_total_cents", "rejeu"],
    "additionalProperties": false
  },
  "annotations": {
    "readOnlyHint": false,
    "destructiveHint": false,
    "idempotentHint": true,
    "openWorldHint": false
  }
}
```

Lecture : la définition n’emploie que des champs du schéma MCP 2026-07-28; ses schémas suivent JSON Schema 2020-12, dialecte par défaut de la spécification, et `additionalProperties: false` ferme le contrat**[162, 197]**. Le motif du champ `idempotency_key` correspond à la dérivation de la section 7.6. Le montant total n’est pas un argument : le serveur le calcule à partir des lignes et le renvoie, et la passerelle calcule la même grandeur pour le seuil (EXIG-AUT-13); les prix sont des entiers en cents, bornés par le schéma. Seul `centre_cout` porte `x-mcp-header` : le client recopie sa valeur dans l’en-tête `Mcp-Param-Cost-Center`, ce qui convient à une donnée non sensible (EXIG-MCP-18). Les annotations, conformes au schéma, ne décident de rien : elles doivent seulement concorder avec le palier inscrit au catalogue (EXIG-MCP-14). L’outil renvoie un `structuredContent` conforme à `outputSchema`, accompagné du même JSON dans un bloc texte, et signale une erreur métier par un résultat marqué `isError: true` (EXIG-MCP-07). La compensation de l’outil et son palier figurent à son entrée de catalogue (C.2), la définition C.1 ne portant que des champs du schéma MCP.

## C.2 Entrée de catalogue de l’outil — `[Exécuté en CI]`

L’exemple montre où vit la gouvernance de l’outil C.1 : dans le catalogue d’entreprise, et non dans le serveur (section 6.8).

**Entrée du catalogue d’entreprise pour l’outil C.1 (format interne)**

```
{
  "ref": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",
  "tool_name": "approvisionnement_creer_bon_commande",
  "contract_version": "1.4.0",
  "definition_digest": "sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6",
  "server": {
    "id": "mcp-approvisionnement",
    "endpoint": "https://passerelle-agents.ent.ca/mcp/approvisionnement",
    "mcp_revision": "2026-07-28",
    "extensions_allowed": []
  },
  "lifecycle_state": "production",
  "tier": "P2",
  "approval_thresholds": [
    { "measure": "sum(lignes[].quantite * lignes[].prix_unitaire_cents)", "computed_by": "gateway",
      "unit": "cents_cad", "scope": "task", "window": "task",
      "max_without_approval": 500000, "inclusive": true },
    { "measure": "sum(lignes[].quantite * lignes[].prix_unitaire_cents)", "computed_by": "gateway",
      "unit": "cents_cad", "scope": "counterparty:fournisseur_id", "window_s": 86400,
      "max_without_approval": 2000000, "inclusive": true }
  ],
  "compensation": { "ref": "mcp-approvisionnement/approvisionnement_annuler_bon_commande@1.2.0", "tier": "P2" },
  "idempotency": { "argument": "idempotency_key", "mode": "native", "checked_by_server": true,
                   "on_conflict": "reject", "on_in_progress": "refuse", "on_duplicate": "replay_result",
                   "key_retention_s": 864000 },
  "oauth_scope": "approvisionnement:write",
  "header_projection": { "centre_cout": "Mcp-Param-Cost-Center" },
  "data_classification_max": "confidentiel",
  "personal_information": false,
  "owner": "Direction Approvisionnement",
  "on_call_team": "garde-plateforme-erp",
  "known_consumers": ["agt-achats-indirects"],
  "reviewed_by": ["responsable-outil", "securite"],
  "approved_on": "2026-10-06",
  "next_review": "2027-04-06"
}
```

Lecture : cette entrée porte le palier, les seuils, la compensation et son palier, la portée, la direction responsable et l’équipe de garde de l’outil, attribués après revue par son responsable et par la sécurité; la passerelle les lit ici, jamais dans les annotations (EXIG-AUT-08, EXIG-MCP-14). `definition_digest` est le SHA-256 de la définition C.1 canonisée selon la RFC 8785 : à chaque `tools/list`, la passerelle recalcule l’empreinte et retire l’outil au moindre écart, description comprise, jusqu’à une nouvelle approbation (EXIG-MCP-20) **[221, 236]**. Chaque seuil mesure une grandeur que la passerelle calcule à partir des lignes canonisées, jamais un montant déclaré par l’agent, et déclare son unité, sa portée et sa fenêtre; la borne est inclusive, et les compteurs de la tâche et du fournisseur sont tenus par la passerelle (EXIG-AUT-13). Avec ce palier P2 et ces seuils, un agent de classe modérée déclaré N3 peut créer seul des bons totalisant 5 000 $ ou moins dans une tâche, et 20 000 $ ou moins par fournisseur sur 24 heures; au-delà, le contrôle calculé (EXIG-AUT-10) impose le jeton d’approbation de l’exemple C.6. La compensation est elle-même un outil inscrit avec son palier (EXIG-ORC-17). L’idempotence est native, vérifiée par l’ERP; l’entrée déclare les trois comportements de l’EXIG-ORC-22 et la durée de conservation des clés, qui couvre la durée de vie maximale de la tâche durable, la fenêtre de reprise et le délai de réconciliation, alors que l’annotation `idempotentHint` n’est qu’un indice. `lifecycle_state` reprend l’énumération du tableau 63.

## C.3 Carte d’agent A2A — `[Exécuté en CI]`

L’exemple montre la carte de référence, inscrite au catalogue et servie par la passerelle, de l’agent spécialiste du scénario de délégation de la section 6.6.

**Carte d’agent A2A 1.0 signée de l’agent d’évaluation du risque de crédit**

```
{
  "name": "Agent d'évaluation du risque de crédit",
  "description": "Analyse un dossier de crédit commercial selon la politique CR-12 et recommande une décision
motivée. N'accorde ni ne refuse aucun crédit.",
  "supportedInterfaces": [
    {
      "url": "https://passerelle-agents.ent.ca/a2a/risque-credit",
      "protocolBinding": "JSONRPC",
      "protocolVersion": "1.0"
    }
  ],
  "provider": {
    "organization": "Direction Gestion des risques",
    "url": "https://intranet.ent.ca/risque-credit"
  },
  "version": "2.3.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": true,
    "extendedAgentCard": true,
    "extensions": [
      {
        "uri": "https://ent.ca/a2a/extensions/gouvernance/v1",
        "description": "Copie en lecture seule de données du registre : niveau d'autonomie et classe de
risque.",
        "required": false,
        "params": { "niveau_autonomie": "N2", "classe_risque": "elevee" }
      }
    ]
  },
  "securitySchemes": {
    "idp-entreprise": {
      "openIdConnectSecurityScheme": { "openIdConnectUrl": "https://idp.ent.ca/.well-known/openid-
configuration" }
    }
  },
  "securityRequirements": [{ "schemes": { "idp-entreprise": { "list": ["risque-credit:invoke"] } } }],
  "defaultInputModes": ["text/plain", "application/json"],
  "defaultOutputModes": ["application/json", "text/markdown"],
  "skills": [
    {
      "id": "analyse-dossier-commercial",
      "name": "Analyse prudentielle d'un dossier de crédit commercial",
      "description": "Évalue la solvabilité d'une entreprise cliente, vérifie les garanties et produit une
recommandation motivée avec les ratios calculés.",
      "tags": ["credit", "risque", "conformite"],
      "examples": ["Analyser le dossier 8841 selon la politique CR-12"],
      "securityRequirements": [{ "schemes": { "idp-entreprise": { "list": ["risque-credit:analyze"] } } }]
    }
  ],
  "signatures": [
    {
      "protected":
"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpPU0UiLCJraWQiOiJjYXJ0ZXMtYWdlbnRzLTIwMjYtMTAiLCJqa3UiOiJodHRwczovL2NsZXMuZW50
LmNhL2EyYS9qd2tzLmpzb24ifQ",
      "signature": "Wm3k…"
    }
  ]
}
```

Lecture : la carte contient les huit champs obligatoires d’A2A 1.0, ses adresses sont celles de la passerelle d’agents, et la compétence porte sa propre portée OAuth dans `securityRequirements` (EXIG-A2A-02, EXIG-A2A-10)**[68, 192]**. La signature est un JWS calculé sur la carte canonisée selon la RFC 8785, champ `signatures` exclu et règles de présence des champs de la spécification (section 8.4 de la spécification A2A 1.0) appliquées; son en-tête protégé, encodé en base64url, désigne le type JOSE (`typ`), l’algorithme ES256, la clé (`kid`) et le jeu de clés publiques de l’entreprise (`jku`), et tout client vérifie cette signature avant de se fier à la carte (EXIG-A2A-03). La clé se résout par `kid` dans le jeu de clés épinglé au catalogue, et `jku` n’est suivi que s’il concorde exactement avec l’URL inscrite pour cet émetteur, ce qui écarte la falsification de requêtes côté serveur contre laquelle la RFC 8725 met en garde (section 3.10). Le niveau d’autonomie et la classe de risque ne forment pas un champ de premier niveau : ils sont déclarés comme extension de données facultative, qui ne figure que dans une carte servie aux seuls clients authentifiés (carte de référence d’un agent interne, ou carte étendue d’un agent exposé, EXIG-A2A-06), dont l’URI versionnée figure au registre des extensions approuvées, et la fiche du registre fait foi en cas d’écart (EXIG-A2A-05)**[238]**. `extendedAgentCard` annonce une carte étendue, servie après authentification, qui ajoute les compétences réservées aux appelants internes (EXIG-A2A-06), et l’`ETag` servi avec la carte, dérivé du hachage de la représentation servie, signatures comprises, permet de revalider les copies en cache, alors que `version`, en SemVer, signale la compatibilité (EXIG-A2A-04). L’agent étant de classe élevée, ses appelants présentent un jeton lié par mTLS ou DPoP

(EXIG-IAM-14); l’exemple, réduit au schéma OpenID Connect, ne montre pas le schéma mTLS qu’un contrat réel y combinerait dans `securityRequirements`.

## C.4 Événement CloudEvents — `[Exécuté en CI]`

L’exemple montre la première alerte d’une chorégraphie, publiée par un agent détecteur sur le bus d’événements (section 6.7).

**Événement CloudEvents 1.0 avec les extensions exigées par le cadre (représentation JSON)**

```
{
  "specversion": "1.0",
  "id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "source": "https://agents.ent.ca/logistique/detecteur-rupture-stock",
  "type": "ca.ent.logistique.alerte.rupture.v1",
  "subject": "MTL-02/PRD-99210",
  "time": "2026-10-27T09:15:00Z",
  "datacontenttype": "application/json",
  "dataschema": "https://catalogue.ent.ca/schemas/logistique/alerte-rupture/1.0.0",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "authtype": "service_account",
  "authid": "ordonnanceur-inventaire-quotidien",
  "dataclassification": "internal",
  "partitionkey": "MTL-02/PRD-99210",
  "xagentorigin": "agt-detecteur-rupture@1.3.0",
  "xagenthopcount": 1,
  "xagentmaxhops": 4,
  "xcostcenter": "CC-8100",
  "data": {
    "entrepot_id": "MTL-02",
    "sku": "PRD-99210",
    "stock_actuel": 12,
    "seuil_critique": 50,
    "horizon_epuisement_heures": 18
  }
}
```

Lecture : l’événement porte les quatre attributs requis par CloudEvents, les attributs `time`, `datacontenttype` et `dataschema` exigés par le cadre, et un `type` versionné en domaine inversé (EXIG-EVT-02)**[173]**. `traceparent` (Distributed Tracing), `authtype` et `authid` (Auth Context), `dataclassification` (Data Classification) et `partitionkey` (Partitioning) sont des extensions documentées, alors que `xagentorigin`, `xagenthopcount`, `xagentmaxhops` et `xcostcenter` sont propres au cadre (EXIG-EVT-04); aucun attribut ne contient de renseignement personnel (EXIG-EVT-05)**[187, 252, 255]**. Quand un agent qui réagit à cette alerte publie un nouvel événement, l’intercepteur de publication pose `xagenthopcount` à 2 et recopie `xagentorigin` et `xagentmaxhops`, sans se fier aux valeurs du producteur (EXIG-EVT-06); un événement dont le compteur atteint 4 n’est pas traité et part en file de lettres mortes (EXIG-EVT-06). Le compteur borne la profondeur d’une chaîne, non sa diffusion : le courtier applique aussi un plafond de largeur, en événements par trace (EXIG-EVT-06). La correspondance entre l’échelle de classification interne (C.2) et les valeurs de `dataclassification` est inscrite au catalogue. Sur Kafka, le mode binaire retenu par défaut place les attributs (sauf `datacontenttype`, porté par l’en-tête `content-type`) dans des en-têtes préfixés `ce_` et `data` dans la valeur; une fois le « Key Mapper » de la liaison activé (mécanisme facultatif), `partitionkey` est recopié dans la clé du message et, comme Kafka écrit les messages de même clé dans la même partition et en conserve l’ordre, les alertes d’un même article dans un même entrepôt restent dans l’ordre, pourvu que le nombre de partitions soit figé au contrat et que le producteur soit idempotent ou n’ait qu’une requête en vol (EXIG-EVT-09)**[250, 257]**.

## C.5 Jeton délégué — `[Schéma conceptuel]`

L’exemple complète l’extrait de la section 9.3 : les deux jetons qui portent, au nom d’Alice, l’appel de l’agent d’analyse des dépenses, appelé par l’orchestrateur, vers le serveur MCP des finances. La passerelle d’agents termine TLS : l’agent lui présente le jeton 1; elle le vérifie, puis obtient par échange le jeton 2, qu’elle présente au serveur (section 6.5).

**Jetons délégués après deux sauts, décodés (signatures omises)**

```
Jeton 1, présenté par l'agent à la passerelle
En-tête
{ "typ": "at+jwt", "alg": "ES256", "kid": "idp-2026-10" }
Charge utile
{
  "iss": "https://idp.ent.ca",
  "sub": "alice",
  "aud": "https://passerelle-agents.ent.ca",
  "client_id": "agent-analyse-depenses",
  "scope": "finance:read",
  "authorization_details": [{ "type": "lecture_depenses", "periode": "2026-T3" }],
  "act": {
    "sub": "spiffe://ent.ca/agent-analyse-depenses",
    "act": { "sub": "spiffe://ent.ca/agent-orch" }
  },
  "cnf": { "x5t#S256": "vzF5VHuU_5wCN7LdQZOXTK3y7aNQCqM5M-yosaTb6aw" },
  "iat": 1793084700,
  "exp": 1793085600,
  "jti": "9f1c2d7e-5a41-4c3b-8e06-b2f94a1d7c55"
}
Jeton 2, obtenu par la passerelle et présenté au serveur MCP des finances (même en-tête)
Charge utile
{
  "iss": "https://idp.ent.ca",
  "sub": "alice",
  "aud": "https://mcp-finance.ent.ca",
  "client_id": "passerelle-agents",
  "scope": "finance:read",
  "authorization_details": [{ "type": "lecture_depenses", "periode": "2026-T3" }],
  "act": {
    "sub": "spiffe://ent.ca/agent-analyse-depenses",
    "act": { "sub": "spiffe://ent.ca/agent-orch" }
  },
  "cnf": { "x5t#S256": "q8Lr2Wd0cJmE4sTnV7yHbA1fKpXzG3uN9oRiD5eC6wM" },
  "iat": 1793084712,
  "exp": 1793085600,
  "jti": "3b7e90a1-6c52-4d8e-9a17-c4e05b2f8d66"
}
```

Lecture : les deux jetons suivent le profil JWT de la RFC 9068, avec l’en-tête `typ` `at+jwt` et les revendications `iss`, `exp`, `aud`, `sub`, `client_id`, `iat` et `jti`**[72]**. Alice reste le sujet des deux; l’`act` externe désigne l’acteur courant, l’agent d’analyse des dépenses, et l’`act` imbriqué l’orchestrateur, acteur antérieur que le serveur consigne sans s’en servir pour décider (EXIG-IAM-08, EXIG-IAM-11)**[69]**. Le jeton 1 a pour audience la passerelle, et son `cnf` le lie à l’empreinte du certificat X.509-SVID de l’agent : la passerelle vérifie cette liaison sur la connexion mTLS de l’agent (EXIG-IAM-14)**[328]**. Le jeton 2, que la passerelle obtient par échange, la désigne comme client et lui est lié; l’échange n’ajoute aucun niveau d’`act`, et le serveur n’accepte que la passerelle, par mTLS. Son expiration ne dépasse pas celle du jeton 1 : aucun échange ne prolonge la délégation (EXIG-IAM-08). L’audience unique, la portée réduite à `finance:read`, la portée de la tâche portée par `authorization_details` (dépenses du troisième trimestre) et la durée de vie de 900 secondes appliquent les exigences EXIG-IAM-10, EXIG-IAM-11 et EXIG-IAM-15, et le serveur de ressources applique en outre les droits d’Alice d’après `sub`. Volé, aucun des deux jetons ne sert sans la clé privée de son titulaire.

## C.6 Jeton d’approbation humaine — `[Schéma conceptuel]`

L’exemple montre l’action soumise à l’approbateur, le calcul de son empreinte et le jeton signé qui en résulte (section 8.5).

**Action soumise, empreinte h et jeton d’approbation décodé (signature omise)**

```
Objet haché (canonisé selon la RFC 8785, présenté coupé)
  outil      : mcp-approvisionnement/approvisionnement_creer_bon_commande
  version    : 1.4.0
  definition : sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6
  agent_id   : agt-achats-indirects@1.2.0
  task_id    : tache-7f3c2a
  arguments  : {"centre_cout":"CC-4410","fournisseur_id":"SUP-004512",
                "idempotency_key":"80351869ca990c86c8c6a314a7ac23d80b509a03f9a11dd173d2f1112c10eca7",
                "lignes":[{"prix_unitaire_cents":24960,"quantite":40,"sku":"PRD-10442"},
                          {"prix_unitaire_cents":20800,"quantite":12,"sku":"PRD-20817"}],
                "statut_demande":"soumis"}
  h          : 92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81
  grandeur   : 1248000 cents, somme des lignes calculée par la passerelle (seuil de la tâche : 500000)
Jeton d'approbation 1 (premier approbateur)
En-tête
{ "typ": "approbation+jwt", "alg": "ES256", "kid": "approbation-2026-10" }
Charge utile
{
  "iss": "https://approbation.ent.ca",
  "aud": "https://passerelle-agents.ent.ca",
  "sub": "apb-5e19c2",
  "approbateur_role": "tiers",
  "iat": 1793093040,
  "exp": 1793093940,
  "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",
  "task_id": "tache-7f3c2a",
  "agent_id": "agt-achats-indirects@1.2.0",
  "action_sha256": "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81",
  "authorization_details": [
    {
      "type": "https://ent.ca/types/action-agent",
      "locations": ["https://passerelle-agents.ent.ca/mcp/approvisionnement"],
      "actions": ["tools/call"],
      "identifier": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",
      "fournisseur_id": "SUP-004512",
      "centre_cout": "CC-4410",
      "statut_demande": "soumis",
      "lignes": [{ "sku": "PRD-10442", "quantite": 40, "prix_unitaire_cents": 24960 },
                 { "sku": "PRD-20817", "quantite": 12, "prix_unitaire_cents": 20800 }],
      "grandeur_seuil": { "valeur": 1248000, "unite": "cents_cad", "portee": "task" }
    }
  ]
}
Jeton d'approbation 2 (second approbateur distinct, même action_sha256)
En-tête
{ "typ": "approbation+jwt", "alg": "ES256", "kid": "approbation-2026-10" }
Charge utile
{
  "iss": "https://approbation.ent.ca",
  "aud": "https://passerelle-agents.ent.ca",
  "sub": "apb-91d4e8",
  "approbateur_role": "tiers",
  "iat": 1793093095,
  "exp": 1793093940,
  "jti": "7d4e9b12-3a6c-4e8f-9c01-8b2d6f4a3e19",
  "task_id": "tache-7f3c2a",
  "agent_id": "agt-achats-indirects@1.2.0",
  "action_sha256": "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81",
  "authorization_details": [
    {
      "type": "https://ent.ca/types/action-agent",
      "locations": ["https://passerelle-agents.ent.ca/mcp/approvisionnement"],
      "actions": ["tools/call"],
      "identifier": "mcp-approvisionnement/approvisionnement_creer_bon_commande@1.4.0",
      "fournisseur_id": "SUP-004512",
      "centre_cout": "CC-4410",
      "statut_demande": "soumis",
      "lignes": [{ "sku": "PRD-10442", "quantite": 40, "prix_unitaire_cents": 24960 },
                 { "sku": "PRD-20817", "quantite": 12, "prix_unitaire_cents": 20800 }],
      "grandeur_seuil": { "valeur": 1248000, "unite": "cents_cad", "portee": "task" }
    }
  ]
}
```

Lecture : h est le SHA-256 de la canonisation selon la RFC 8785 de l’objet {outil, version, definition_digest, agent_id, task_id, arguments}, où l’outil est désigné par son identifiant pleinement qualifié (serveur et nom) et les arguments incluent la clé d’idempotence (section 8.5)**[236]**; la canonisation trie les clés, et les montants, entiers en cents, ne laissent aucune place à une lecture divergente des nombres. La passerelle rejette tout argument non conforme à I-JSON et transmet au serveur exactement la forme hachée (EXIG-AUT-12). Le jeton contient le minimum exigé par l’EXIG-AUT-12 : l’émetteur et l’audience, l’empreinte (`action_sha256`), l’approbateur sous pseudonyme stable (`sub`) et son rôle (tiers, et non le mandant), la tâche, l’agent, une expiration à 15 minutes et son identifiant (`jti`). `authorization_details` et l’écran d’approbation sont produits par la passerelle à partir des arguments canonisés, avec la grandeur calculée du seuil, jamais d’un texte de l’agent (EXIG-AUT-19); leur emploi dans un jeton d’approbation est un profil du cadre, la RFC 9396 ne définissant cette revendication que pour les jetons d’accès**[312]**. Un `typ` distinct de `at+jwt`, choix du cadre, empêche de faire passer ce jeton pour un jeton d’accès, ou l’inverse. Le jeton est remis à la passerelle, qui le conserve et ne le transmet ni à l’agent ni à son modèle; elle vérifie la signature, l’émetteur, l’audience, l’expiration, la concordance de l’agent et de la tâche avec l’appelant authentifié et le nombre d’approbateurs qu’exige le contrôle calculé, puis recalcule h sur l’appel reçu et refuse tout écart. Le jeton couvre une seule opération : un réessai de la même opération avant l’expiration est relayé, et l’ERP le déduplique par la clé. Conformément à la section 6.6 et à l’EXIG-AUT-15, ce bon de commande de 12 480 $ (> 5 000 $) réunit deux approbations humaines et deux jetons signés provenant d’approbateurs distincts (`apb-5e19c2` et `apb-91d4e8`, tous deux distincts du mandant), liés au même `action_sha256` (h). La demande porte aussi l’empreinte de la compensation déclarée, approuvée avec l’étape (EXIG-AUT-12), que l’exemple ne montre pas. Ici, l’approbation est obtenue hors bande, par CIBA sur l’appareil de l’approbatrice (EXIG-AUT-09, EXIG-AUT-14), et seul un tel jeton vaut approbation, jamais un acquiescement dans la conversation (EXIG-AUT-13)**[310]**.

## C.7 Enveloppe budgétaire de tâche — `[Exécuté en CI]`

L’exemple montre l’enveloppe attribuée à la tâche du scénario, telle que la passerelle de modèles et l’orchestrateur la tiennent à jour (section 10.6).

**Enveloppe budgétaire de la tâche tache-7f3c2a, état à 9 h 25 UTC (format interne)**

```
{
  "task_id": "tache-7f3c2a",
  "agent_id": "agt-achats-indirects@1.2.0",
  "cost_center": "CC-4410",
  "issued_at": "2026-10-27T09:02:11Z",
  "limits": {
    "max_tokens": 50000,
    "max_cost_cad": 0.75,
    "max_tool_calls": 15,
    "max_iterations": 8,
    "timeout_s": 60,
    "max_wall_clock_s": 28800
  },
  "alert_ratio": 0.8,
  "on_exhaustion": { "action": "stop_and_escalate", "queue": "file-achats-exceptions" },
  "models": {
    "default": "modele-compact",
    "reasoning": "modele-raisonnement",
    "reasoning_steps": ["planification", "arbitrage"],
    "fallback": "modele-compact-repli"
  },
  "consumed": {
    "as_of": "2026-10-27T09:25:41Z",
    "tokens": 41200,
    "cost_cad": 0.52,
    "tool_calls": 9,
    "iterations": 5,
    "active_s": 38
  },
  "alerts": [
    {
      "metric": "tokens",
      "ratio": 0.824,
      "at": "2026-10-27T09:25:41Z",
      "notified": "parrain"
    }
  ],
  "delegations": []
}
```

Lecture : l’enveloppe reprend des plafonds de même valeur que la fiche type de l’annexe B, qui décrit un autre agent : jetons, coût, appels d’outils, itérations et temps d’exécution active (`timeout_s`); `max_wall_clock_s` borne en outre la durée totale, attente d’approbation comprise (EXIG-ORC-26). Chaque étape incrémente `consumed` : à 82,4 % des jetons, le seuil d’alerte de 80 % a déjà prévenu le parrain, et l’atteinte d’un plafond arrêtera la tâche vers l’avant, en état sûr, pour l’escalader, sans jamais la déclarer réussie (EXIG-FIN-04). Les compensations des étapes déjà exécutées restent possibles : elles s’exécutent sous l’identité de compensation de l’orchestrateur, sur une réserve de budget tenue hors de cette enveloppe (EXIG-ORC-17). Le modèle compact sert par défaut, le modèle de raisonnement seulement aux étapes nommées, et tout le coût s’impute au centre de coûts de la tâche. Une délégation à un exécutant recevrait une part de l’enveloppe restante, inscrite dans `delegations`, et jamais une enveloppe neuve (section 7.7); les valeurs sont illustratives et se calibrent par mesure.

## C.8 Enregistrement d’audit — `[Exécuté en CI]`

L’exemple montre l’enregistrement d’issue que la passerelle verse au journal d’audit après l’exécution de l’action approuvée en C.6; un enregistrement d’intention, chaîné dans le même flux, l’a précédé avant le relais de l’appel (section 10.3).

**Enregistrement d’audit canonisé (clés dans l’ordre RFC 8785, présentées indentées)**

```
{
  "empreinte": "sha256:d25e4bc569299784f95d6a4f4920810d497c6e8f3aadb7f8e9737c3bb42c4203",
  "enregistrement": {
    "action": {
      "arguments_sha256": "c808b36a44b197cd96fe679fd662241bf32c459f4480bbc67e5693d20ad3259f",
      "definition_sha256": "sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6",
      "definition_version": "1.4.0",
      "issue": "succes",
      "outil": "mcp-approvisionnement/approvisionnement_creer_bon_commande",
      "palier": "P2",
      "reference_resultat": "BC-2026-118734"
    },
    "agent": {
      "id": "agt-achats-indirects",
      "identite": "spiffe://ent.ca/agt-achats-indirects",
      "invite_systeme": "sha256:41d07c…",
      "version": "1.2.0"
    },
    "autorite": {
      "approbations": [
        { "approbateur": "apb-5e19c2", "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28", "role": "tiers" },
        { "approbateur": "apb-91d4e8", "jti": "7d4e9b12-3a6c-4e8f-9c01-8b2d6f4a3e19", "role": "tiers" }
      ],
      "classe_risque": "moderee",
      "controle": "approbation_requise_au_dela_du_seuil",
      "empreinte_approbation": "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81",
      "grandeur_seuil": 1248000,
      "niveau_autonomie": "N3",
      "version_politique": "politiques-passerelle@2026.10.3"
    },
    "correlation": {
      "cle_idempotence": "80351869ca990c86c8c6a314a7ac23d80b509a03f9a11dd173d2f1112c10eca7",
      "etape": "etape-03/creer-bon-commande#1",
      "span_id": "b7ad6b7169203331",
      "tache": "tache-7f3c2a",
      "trace_id": "0af7651916cd43dd8448eb211c80319c"
    },
    "flux": "passerelle-agents-03",
    "horodatage": "2026-10-27T09:26:03.412Z",
    "intention_sequence": 48212,
    "mandant": {
      "jeton_delegue_jti": "4e8b2c71-0d93-4a6f-9b15-7c2e8f40a6d3",
      "pseudonyme": "u-58c1d7",
      "type": "user"
    },
    "modele": {
      "fournisseur": "…",
      "servi": "modele-compact",
      "version": "2026-08-14"
    },
    "nature": "issue",
    "precedent_sha256": "sha256:ee710bdb80fd80be1bce7ad8f07964c8a0dea08c5fb81f39289b26666ab4524a",
    "sequence": 48213
  },
  "signature": { "alg": "ES256", "kid": "journal-audit-2026-10", "valeur": "…" }
}
```

Lecture : `enregistrement` reprend les cinq éléments exigés par l’EXIG-OBS-12 (section 10.3) : le mandant sous pseudonyme (`mandant`), l’agent avec sa version, son identité et l’empreinte de son invite système (`agent`), l’action avec l’outil, la version et l’empreinte de sa définition, l’empreinte des arguments et l’issue (`action`), le modèle servi (`modele`) et l’autorité qui permettait d’agir (`autorite` : politique appliquée, contrôle, grandeur calculée du seuil, niveau d’autonomie et liste des approbations, chacune avec son jeton et le rôle de l’approbateur, selon les EXIG-IAM-21, EXIG-AUT-10 et EXIG-AUT-15); `correlation` le relie à la tâche, à l’étape, à la clé d’idempotence et à la trace, et les champs A2A de l’extrait de la section 10.3 sont omis, faute de délégation. Avant de relayer l’appel, la passerelle a écrit l’enregistrement d’intention de séquence 48212, que celui-ci référence (`intention_sequence`); une intention sans issue est traitée comme un incident (EXIG-OBS-11, EXIG-OBS-13). L’enregistrement ne recopie pas les arguments, et le résultat n’y figure que par sa référence. `arguments_sha256` est ici une empreinte simple, qu’on peut recalculer; comme la clé d’idempotence se déduit de la tâche et de l’étape, consignées en clair, l’empreinte des arguments d’un outil à faible entropie est salée ou remplacée par un HMAC sous une clé du service d’audit (EXIG-OBS-12). `empreinte_approbation` reprend l’empreinte h du jeton C.6; la passerelle l’a recalculée avant de relayer

l’appel, ce qui atteste que les octets transmis sont ceux qui ont été approuvés, et non que l’effet est celui qui était attendu. Le rôle consigné (tiers) atteste que l’approbatrice n’est pas le mandant, ce que le service d’approbation vérifie à l’émission. `empreinte` est le SHA-256 de `enregistrement` canonisé selon la RFC 8785, signé par le service d’audit, et `precedent_sha256` chaîne chaque enregistrement au précédent du même flux (`flux`, inscrit au registre des flux) : une suppression ou une modification internes se détectent, mais la troncature de la queue et la réécriture par le détenteur de la clé ne se détectent que par les points de contrôle de la tête du flux, publiés hors du domaine d’administration du service d’audit (EXIG-OBS-12)**[236]**. Ce format, sa signature et son ancrage, choix du cadre, vont au-delà du minimum légal : pour un système à haut risque (obligations applicables à compter du 2 décembre 2027 pour l’annexe III et du 2 août 2028 pour l’annexe I, selon le règlement (UE) 2026/1744**[57, 58]**), le RIA exige que le système permette l’enregistrement automatique des événements, sans en fixer le format (art. 12), et que le déployeur conserve les journaux, dans la mesure où ils sont sous son contrôle, pendant une durée adaptée à la destination du système et d’au moins six mois, sauf disposition contraire du droit de l’Union ou du droit national (art. 26, par. 6)**[61, 447]**.
