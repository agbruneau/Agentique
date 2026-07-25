# Lot L-04 — Entra Agent ID et ses pairs infonuagiques

| Champ | Valeur |
|---|---|
| Lot | **L-04** — phase **P2**, jalon J-3 |
| Débloque | **ch. 6** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 2 en [A], 0 écartée(s) par le vote. **6 échecs de source** consignés |
| Vote | **2 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **5 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L04-A1` | **[B]** | 0 | Microsoft situe la disponibilité générale (GA) de la plateforme Microsoft Entra Agent ID au mois d'avril 2026 : la note de version correspondante figure sous l'intitulé de section « April 2026 » des notes de version Entra, et la page « What's new in Agent ID » (ms.date 2026-05-01) ouvre sur la même formule. |
| `L04-A2` | **[A]** ⚖ | 0 | À l'intérieur du produit annoncé GA, plusieurs capacités nommées d'Entra Agent ID demeurent étiquetées « Preview » dans la documentation Microsoft consultée le 21 juillet 2026 : l'assistant de création de blueprint et d'identité d'agent du centre d'administration, l'option d'affectation « Users, agents (Preview) », les cibles « All agent users (Preview) » / « Select agent users (Preview) », et les conditions « Agent risk (Prev… |
| `L04-A3` | **[B]** | 0 | Microsoft documente deux régimes de licence distincts : la plateforme Agent ID est présentée comme disponible pour tous les clients Entra, tandis que l'extension des fonctions de sécurité Entra aux agents est conditionnée à Microsoft 365 E7, ou à Microsoft 365 E5 associé à une licence Microsoft Agent 365, avec des options autonomes (Entra ID P1 pour l'accès conditionnel et la gouvernance, P2 pour ID Protection, Entra Internet… |
| `L04-A4` | **[B]** | 0 | Au 21 juillet 2026, la documentation Microsoft annonce que l'exigence de licence Microsoft Agent 365 n'est pas encore appliquée techniquement pour l'accès conditionnel ni pour ID Protection pour les agents, en employant des formules sans échéance datée (« coming soon », « Starting soon », « will soon be required »). |
| `L04-A5` | **[B]** | 0 | Le terme « blueprint » d'Entra Agent ID désigne un objet d'annuaire Microsoft Entra ID servant de gabarit à la création d'identités d'agent ; il est spécifié dans Microsoft Graph v1.0 sous le type de ressource agentIdentityBlueprint, qui hérite du type application et porte notamment description, appRoles, verifiedPublisher, optionalClaims, requiredResourceAccess, la relation inheritablePermissions et une relation sponsors obli… |
| `L04-A6` | **[A]** ⚖ | 2 | La documentation Microsoft porte une réserve explicite d'absence de couverture entre les deux plans d'identité d'agent : une politique d'accès conditionnel ciblant des identités d'agent — y compris par blueprint — ne s'applique pas au compte d'utilisateur de l'agent, et une politique ciblant « tous les utilisateurs » n'inclut pas ces comptes. |
| `L04-A7` | **[B]** | 0 | Google Cloud date au 22 avril 2026 la disponibilité générale d'« Agent Identity » dans IAM, tout en plaçant à la même date son « Agent Identity auth manager » en préversion (Preview) et en datant du 18 juin 2026 la mise en préversion de l'API Agent Identity (agentidentity.googleapis.com), destinée à remplacer l'API IAM Connectors héritée. |
| `L04-A8` | **[B]** | 0 | La documentation Google Cloud décrit le mécanisme d'Agent Identity comme reposant sur une identité SPIFFE de forme spiffe://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH, matérialisée par des certificats X.509 d'une validité de 24 heures renouvelés par Google Cloud, les jetons d'accès étant liés cryptographiquement au certificat de l'agent — liaison que la source présente comme visant à limiter (« to help prevent ») le vol de j… |
| `L04-A9` | **[C]** | 0 | Chez AWS, le pendant documenté est Amazon Bedrock AgentCore Identity, où l'identité d'agent n'est pas un type d'objet propre mais une identité de charge de travail (workload identity) dotée d'attributs spécifiques, créée par l'appel CLI aws bedrock-agentcore-control create-workload-identity, inscrite dans un « agent identity directory » et adossée à un « token vault » stockant jetons OAuth 2.0 et clés d'API, avec prise en char… |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 5 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L04-A3` | **clause d'exclusivité** | La documentation Microsoft consultée le 21 juillet 2026 décrit deux régimes de licence (relevé non exhaustif) : la plateforme Agent ID y est donnée pour disponible aux clients Entra — la portée universelle est la formulation de Microsoft, rapportée et non établie par le relevé —, tandis que l'extension des fonctions de sécurité Entra aux agents y est conditionnée à Microsoft 365 E7, ou à Microsoft 365 E5 associé à un… |
| `L04-A6` | **négatif de corpus** | La page Microsoft Learn consacrée à l'accès conditionnel pour les identités d'agent (titre exact et ms.date à consigner au relevé, consultée le 21 juillet 2026) énonce explicitement qu'une politique d'accès conditionnel ciblant des identités d'agent, y compris par blueprint, ne s'applique pas au compte d'utilisateur de l'agent, et qu'une politique ciblant « tous les utilisateurs » n'inclut pas ces comptes. L'énoncé e… |
| `L04-A7` | **statut non dit** | Google Cloud date au 22 avril 2026 la disponibilité générale d'« Agent Identity » dans IAM, place à la même date son « Agent Identity auth manager » en préversion (Preview), et date du 18 juin 2026 la mise en préversion de l'API Agent Identity (agentidentity.googleapis.com). Google annonce cette API comme appelée à remplacer l'API IAM Connectors héritée : remplacement annoncé, sans date de retrait publiée au relevé,… |
| `L04-A9` | **négatif de corpus** | Chez AWS, la documentation d'Amazon Bedrock AgentCore Identity (pages consultées à consigner au relevé, 21 juillet 2026) décrit l'identité d'agent comme une identité de charge de travail (workload identity) dotée d'attributs spécifiques, créée par l'appel CLI « aws bedrock-agentcore-control create-workload-identity », inscrite dans un « agent identity directory » et adossée à un « token vault » stockant jetons OAuth… |
| `L04-A9` | **clause d'exclusivité** | Chez AWS, un mécanisme documenté comparable est Amazon Bedrock AgentCore Identity — la formulation ne revendique ni unicité au sein de l'offre AWS, ni équivalence fonctionnelle avec Entra Agent ID ou Google Cloud Agent Identity, que le relevé n'a pas établies. |

## D. Échecs de source consignés (6)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Datation du statut (GA ou préversion) d'Amazon Bedrock AgentCore et de sa composante Identity — trois URL d'annonce essayées | HTTP 404 sur les trois. URL construites par conjecture faute de moteur de recherche disponible ; leur inexistence ne dit rien de l'existence de l'annonce. |
| Historique documentaire du guide développeur Bedrock AgentCore (tableau des dates de mise à jour et des passages en GA) | Les deux URL rendent une page ne contenant que le titre « Amazon Bedrock AgentCore » : le tableau d'historique n'est pas présent dans le HTML servi (probable rendu côté client). Aucun contenu exploitable. |
| Page produit AWS Bedrock AgentCore — repérage des étiquettes Preview / Generally available par capacité | Page ouverte, mais le texte converti ne comporte ni le mot « Preview » ni « Generally available » associé à une capacité. Rien à consigner ; cette absence dans un rendu converti n'établit aucun fait négatif. |
| Page dédiée « Agent Identity auth manager » de Google Cloud (périmètre exact de la préversion) | HTTP 404 sur les trois. La page de vue d'ensemble mentionne la section « Agent Identity auth manager » mais l'URL de la page dédiée n'a pas été retrouvée sans moteur de recherche. |
| Outil WebSearch indisponible pendant toute la durée du lot | Erreur répétée « claude-sonnet-5[1m] is temporarily unavailable, so auto mode cannot determine the safety of WebSearch ». Toutes les sources ont donc été atteintes par URL directe, par l'API de recherche de Microsoft Learn (learn.microsoft.… |
| Page tarifaire Microsoft Agent 365 (montants des licences) | Non consultée : hors du périmètre documentaire du lot (documentation officielle des éditeurs) et page commerciale sans version datée stable. Les montants ne sont donc pas établis. |

## E. Ce que le lot déclare n'avoir pas couvert

Ce lot établit (a) le partage GA / préversion chez Microsoft, (b) les licences, (c) la définition de « blueprint », et (d) le pendant Google Cloud avec ses dates. Ce qu'il NE couvre PAS :  1. **AWS, axe du statut — lacune assumée.** Le tri demandé (annonce / feuille de route / préversion / GA documentée) est établi pour Microsoft et Google Cloud, mais PAS pour AWS : aucune source primaire datant le statut d'AgentCore Identity n'a pu être ouverte (voir failures). L04-A9 décrit donc le mécanisme, jamais son statut. Une reprise ciblée est nécessaire — un moteur de recherche fonctionnel devrait suffire.  2. **Aucun décompte, aucune exclusivité.** Je n'affirme nulle part « la seule », « la première » ni « toutes les capacités » : aucun balayage exhaustif des trois catalogues n'a été mené. L04-A2 est explicitement borné à trois pages nommées et à leur état du 21 juillet 2026.  3. **Matériel relevé et non retenu, disponible pour un lot ultérieur sur l'accès conditionnel et la délégation** — quatre constats verbatim déjà en main : (i) « **Block access**: The only available option for agent identities, because there's no interactive remediation possible » (howto-target-agent-identities, ms.date 2026-06-02) ; (ii) les quatre frontières d'évaluation de l'accès conditionnel, dont le point de terminaison d'échange de jetons `AAD Token Exchange Endpoint: Public` (ID `fb60f99c-7a34-4190-8149-302f77469936`) et le contournement par clé d'API ; (iii) les huit détections de risque d'agent d'ID Protection avec leurs `riskEventType`, et l'attribution du risque à l'utilisateur — non à l'agent — dans les flux on-behalf-of ; (iv) la note Graph selon laquelle « some high-risk Microsoft Graph permissions are globally blocked for agents ». Ces éléments touchent L-05/L-09 plutôt que L-04 et n'ont pas été instruits ici.  4. **Retrait de l'Agent Registry d'Entra vers Agent 365** (notes de version, section « March 2026 », « Plan for change ») : relevé, non instruit — les lames Agent registry et Agent collections du centre d'administration Entra y sont annoncées comme retirées le 1er mai 2026, et l'API Graph `agentregistry` comme dépréciée sans date annoncée. C'est un cas d'école du tri « feuille de route » et il mérite son propre traitement.  5. **Non vérifié par essai.** Tout ce lot repose sur de la documentation d'éditeur lue, jamais sur un essai en locataire ou en compte. Les réserves de couverture (L04-A6) sont au **degré 2** — réserve explicite de la source — et non au degré 1 : aucun balayage de spécification normative ni aucune manipulation n'a été conduit.  6. **Neutralité tenue.** Aucune formulation de supériorité entre les trois offres, aucune recommandation : ce sont des cas d'instanciation documentés, et chaque capacité est rattachée à la page qui la porte, avec sa date d'état.

## F. Sources et citations

### `L04-A1` — [B]

Microsoft situe la disponibilité générale (GA) de la plateforme Microsoft Entra Agent ID au mois d'avril 2026 : la note de version correspondante figure sous l'intitulé de section « April 2026 » des notes de version Entra, et la page « What's new in Agent ID » (ms.date 2026-05-01) ouvre sur la même formule.

- **primaire** — Microsoft Entra releases and announcements — ms.date 2026-06-26 ; updated_at 2026-06-30 ; entrée classée sous « ##…, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/fundamentals/whats-new>
  > ### General Availability - Microsoft Entra Agent ID platform … The Microsoft Entra Agent ID platform is now generally available. The Agent ID platform provides an identity and authorization framework built specifically for AI agents operating in enterprise environments.
- **primaire** — What's new in Microsoft Entra Agent ID — ms.date 2026-05-01 ; updated_at 2026-06-17, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id>
  > Microsoft Entra Agent ID is now generally available.

**Réserve** — Les notes de version Entra regroupent par MOIS et ne portent aucun quantième : la date exacte de bascule GA n'est pas établie par cette source. Aucune des deux pages consultées ne donne de jour. Le libellé GA porte sur « the Agent ID platform » / « Microsoft Entra Agent ID » pris globalement, pas sur chacune de ses capacités (voir L04-A2).

### `L04-A2` — [A]

À l'intérieur du produit annoncé GA, plusieurs capacités nommées d'Entra Agent ID demeurent étiquetées « Preview » dans la documentation Microsoft consultée le 21 juillet 2026 : l'assistant de création de blueprint et d'identité d'agent du centre d'administration, l'option d'affectation « Users, agents (Preview) », les cibles « All agent users (Preview) » / « Select agent users (Preview) », et les conditions « Agent risk (Preview) » et « Agent execution environments (Preview) ».

**Balayage (degré 0)** — Trois pages Microsoft Learn ouvertes intégralement le 2026-07-21 : whats-new-agent-id (ms.date 2026-05-01), create-blueprint (ms.date 2026-04-27), howto-target-agent-identities (ms.date 2026-06-02). Chaîne cherchée dans le texte rendu : « (Preview) ». Occurrences relevées et citées ci-contre.

- **primaire** — What's new in Microsoft Entra Agent ID — ms.date 2026-05-01, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id>
  > [Create an agent identity blueprint](create-blueprint) and [Create an agent identity](create-delete-agent-identities) (Preview) - Use the new "wizard" to create agent identity blueprints and agent identities in the Microsoft Entra admin center.
- **primaire** — Create an agent identity blueprint — ms.date 2026-04-27 ; updated_at 2026-06-15, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint>
  > Browse to **Entra ID** > **Agents** > **Agent blueprints**. Select **New agent blueprint (Preview)**.
- **primaire** — Target agent identities in Conditional Access policies — ms.date 2026-06-02 ; updated_at 2026-07-01, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities>
  > Under **Assignments**, select **Users, agents (Preview) or workload identities**. … **All agent users (Preview)**: Applies the policy to every agent's user account in your tenant. … When an agent identity is targeted in a policy (either all agent identities or individually selected agent identities), the only condition available is **Agent risk (Preview)**.

**Réserve** — Constat borné aux trois pages nommées et à leur état du 21 juillet 2026 ; l'énumération n'est pas présentée comme exhaustive des préversions du produit. La page « What's new » place l'étiquette (Preview) sur les deux articles de création, sans dire si elle vise la voie portail seule ou aussi la voie Graph — la page create-blueprint, elle, ne porte l'étiquette que sur le bouton du portail (« New agent blueprint (Preview) »), la voie Microsoft Graph v1.0 n'en portant aucune.

### `L04-A3` — [B]

Microsoft documente deux régimes de licence distincts : la plateforme Agent ID est présentée comme disponible pour tous les clients Entra, tandis que l'extension des fonctions de sécurité Entra aux agents est conditionnée à Microsoft 365 E7, ou à Microsoft 365 E5 associé à une licence Microsoft Agent 365, avec des options autonomes (Entra ID P1 pour l'accès conditionnel et la gouvernance, P2 pour ID Protection, Entra Internet Access pour les contrôles réseau) elles aussi exigeant une licence Microsoft Agent 365.

- **primaire** — What is Microsoft Entra Agent ID? — ms.date 2026-04-14 ; updated_at 2026-06-24, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id>
  > Agent ID is available for all Microsoft Entra customers. … Extending Microsoft Entra security features to agents requires **Microsoft 365 E7** (includes Agent 365 and Microsoft Entra Suite) or **Microsoft 365 E5** paired with a **Microsoft Agent 365** license. Customers without E5 or E7 can use the following standalone licensing options with a **Microsoft Agent 365** license: - **Conditional Access for agents**: Microsoft Entra ID P1 - **ID Protection for agents**: Microsoft Entra ID P2 - **ID Governance for agents**: Microsoft Entra ID P1
- **primaire** — What are agent identities? — ms.date 2025-11-06 ; updated_at 2026-06-15, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities>
  > [Microsoft Agent 365](/en-us/microsoft-agent-365/overview) enables agents to operate across Microsoft 365 services and enterprise workflows, which requires a **Microsoft Agent 365** license for each user.

**Réserve** — Le texte de licence est identique mot pour mot sur les deux pages Learn citées (section « How to get started ») : il s'agit d'un bloc réutilisé, non de deux constats indépendants. Les tarifs eux-mêmes ne sont pas dans la documentation : elle renvoie à une page commerciale microsoft.com non consultée dans ce lot.

### `L04-A4` — [B]

Au 21 juillet 2026, la documentation Microsoft annonce que l'exigence de licence Microsoft Agent 365 n'est pas encore appliquée techniquement pour l'accès conditionnel ni pour ID Protection pour les agents, en employant des formules sans échéance datée (« coming soon », « Starting soon », « will soon be required »).

- **primaire** — Conditional Access for Agents in Microsoft Entra — ms.date 2026-06-19 ; updated_at 2026-07-01, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id>
  > Conditional Access for agents requires Microsoft Entra ID P1 or P2 and a Microsoft Agent 365 license for each user. Enforcement of Agent 365 licensing is coming soon.
- **primaire** — ID Protection for Agents — ms.date 2026-06-17 ; updated_at 2026-06-17, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents>
  > Starting soon, ID Protection for agents will require a [Microsoft Agent 365 license](https://www.microsoft.com/microsoft-agent-365#plans-and-pricing) to extend protection to agents through [Microsoft Entra Agent ID].
- **primaire** — Target agent identities in Conditional Access policies — ms.date 2026-06-02, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities>
  > ## Prerequisites - A Microsoft Entra ID P1 or P2 license - Agent 365 license will soon be required

**Réserve** — Classé PROJETÉ et non PROGRAMMÉ : les trois pages annoncent un changement futur sans aucune date, quantième ni trimestre. Millésime de la prévision : pages Microsoft Learn d'états ms.date 2026-06-19, 2026-06-17 et 2026-06-02. Périmètre : accès conditionnel pour agents et ID Protection pour agents. Rien dans les sources consultées ne dit ce qui se produit pour un locataire non licencié après l'entrée en vigueur.

### `L04-A5` — [B]

Le terme « blueprint » d'Entra Agent ID désigne un objet d'annuaire Microsoft Entra ID servant de gabarit à la création d'identités d'agent ; il est spécifié dans Microsoft Graph v1.0 sous le type de ressource agentIdentityBlueprint, qui hérite du type application et porte notamment description, appRoles, verifiedPublisher, optionalClaims, requiredResourceAccess, la relation inheritablePermissions et une relation sponsors obligatoire à la création.

- **primaire** — Agent identity blueprints in Microsoft Entra Agent ID — ms.date 2026-04-28 ; updated_at 2026-05-01, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/agent-id/agent-blueprint>
  > An agent identity blueprint is an object in Microsoft Entra ID that serves as a template for creating agent identities. … An agent identity blueprint has the following properties that are shared across all its agent identities: - **Description** … - **App roles** … - **Verified publisher** … - **Settings for authentication protocols**
- **primaire** — agentIdentityBlueprint resource type — Microsoft Graph v1.0 — moniker graph-rest-1.0 ; ms.date 2026-03-31 ; updated_at 2026-04-25, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/graph/api/resources/agentidentityblueprint>
  > Namespace: microsoft.graph. An agent identity blueprint serves as a template for creating agent identities within the Microsoft Entra ID ecosystem. Inherits from [application](application). … \| sponsors \| directoryObject collection \| The sponsors for this agent identity blueprint. … Required during the create operation.

**Réserve** — « Blueprint » reste un terme propriétaire Microsoft : aucune spécification normative externe (IETF, W3C, OpenID) consultée dans ce lot ne le définit — la définition ci-dessus n'est opposable qu'au produit Microsoft. La page conceptuelle et la référence Graph donnent deux formulations très proches ; ce ne sont pas deux vérifications indépendantes, mais la référence Graph v1.0 apporte en propre le schéma et l'héritage.

### `L04-A6` — [A]

La documentation Microsoft porte une réserve explicite d'absence de couverture entre les deux plans d'identité d'agent : une politique d'accès conditionnel ciblant des identités d'agent — y compris par blueprint — ne s'applique pas au compte d'utilisateur de l'agent, et une politique ciblant « tous les utilisateurs » n'inclut pas ces comptes.

**Balayage (degré 2)** — Pages ouvertes le 2026-07-21 : /entra/identity/conditional-access/agent-id (ms.date 2026-06-19), section « Conditional Access boundaries and limitations », sous-liste « The following configurations aren't currently supported » ; et /entra/identity/conditional-access/howto-target-agent-identities (ms.date 2026-06-02), section « Considerations for selecting agent assignments ». La réserve est énoncée par les deux pages dans des termes concordants.

- **primaire** — Conditional Access for Agents in Microsoft Entra — ms.date 2026-06-19 ; updated_at 2026-07-01, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id>
  > The following configurations aren't currently supported: - Policies targeting all users don't include agent's user accounts. - Scoping a Conditional Access policy to include or exclude agent's user account based on their group membership - A Conditional Access policy targeting agent identities won't apply to the agent's user account. - A Conditional Access policy targeting agent identities using agent identity blueprint covers only the agent identity, not the agent's user account.
- **primaire** — Target agent identities in Conditional Access policies — ms.date 2026-06-02 ; updated_at 2026-07-01, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities>
  > Keep in mind the following important details when selecting agent assignments: - Policies targeting all users don't include agent's user accounts.

**Réserve** — Degré 2 (fait négatif ÉTABLI) et non degré 1 : la réserve est énoncée par Microsoft, elle ne résulte pas d'un balayage de ma part ni d'un essai en locataire. La liste « aren't currently supported » est datée du 19 juin 2026 et le mot « currently » y est de la source ; elle est susceptible d'évoluer. Aucun essai fonctionnel n'a été mené.

### `L04-A7` — [B]

Google Cloud date au 22 avril 2026 la disponibilité générale d'« Agent Identity » dans IAM, tout en plaçant à la même date son « Agent Identity auth manager » en préversion (Preview) et en datant du 18 juin 2026 la mise en préversion de l'API Agent Identity (agentidentity.googleapis.com), destinée à remplacer l'API IAM Connectors héritée.

- **primaire** — IAM release notes — entrées datées du 2026-04-22 et du 2026-06-18, consultée le 2026-07-21 — <https://docs.cloud.google.com/iam/docs/release-notes>
  > April 22, 2026 — "Agent Identity is generally available (GA). Agent Identity provides a strongly attested, cryptographic identity for each agent that is tied to the lifecycle of the resource hosting the agent." / "Agent Identity auth manager is available in preview. You can use Agent Identity auth manager to help securely authenticate your agents to third-party services using 3-legged OAuth, 2-legged OAuth, or API keys." — June 18, 2026 — "The Agent Identity API (agentidentity.googleapis.com) is available in Preview. This new API replaces the legacy IAM Connectors API (iamconnectors.googleapis.com) for managing auth providers and agent identities."
- **primaire** — Agent Identity overview — page datée « Last updated 2026-07-21 UTC », consultée le 2026-07-21 — <https://docs.cloud.google.com/iam/docs/agent-identity-overview>
  > This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support.

**Réserve** — Le périmètre exact de ce qui est GA n'est pas coextensif au produit : sur la page de vue d'ensemble, le titre H1 « Agent Identity overview » ne porte aucune étiquette, mais la bannière Pre-GA se trouve dans la section « Agent Identity auth manager », et des étiquettes Preview accompagnent en outre les méthodes 3-legged OAuth, 2-legged OAuth, clé d'API et l'intégration VPC Service Controls. Autrement dit : identité GA, mécanismes d'authentification aux tiers en préversion.

### `L04-A8` — [B]

La documentation Google Cloud décrit le mécanisme d'Agent Identity comme reposant sur une identité SPIFFE de forme spiffe://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH, matérialisée par des certificats X.509 d'une validité de 24 heures renouvelés par Google Cloud, les jetons d'accès étant liés cryptographiquement au certificat de l'agent — liaison que la source présente comme visant à limiter (« to help prevent ») le vol de jeton, sans énoncé de garantie.

- **primaire** — Agent Identity overview — page datée « Last updated 2026-07-21 UTC », consultée le 2026-07-21 — <https://docs.cloud.google.com/iam/docs/agent-identity-overview>
  > Agent Identity provides a strongly attested, cryptographic identity for each agent that is based on the SPIFFE standard. With Agent Identity, your agent can securely authenticate to MCP servers, cloud resources, endpoints, and other agents, acting either on its own behalf or on behalf of an end user. … The identity follows this format: spiffe://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH … Each X.509 certificate is valid for 24 hours, and Google Cloud automatically keeps it current to maintain security. … This token is cryptographically bound to the agent's unique X.509 certificate to help prevent token theft.

**Réserve** — Ce que la spécification DÉMONTRE n'est pas établi ici : la source est la documentation produit de l'éditeur, non une spécification soumise à revue ni une preuve de sécurité. Les qualificatifs « strongly attested » et « help prevent token theft » sont des formulations de Google Cloud, reproduites comme telles et non reprises à mon compte. La conformité effective au standard SPIFFE (quel profil, quelle version) n'est pas documentée sur la page consultée.

### `L04-A9` — [C]

Chez AWS, le pendant documenté est Amazon Bedrock AgentCore Identity, où l'identité d'agent n'est pas un type d'objet propre mais une identité de charge de travail (workload identity) dotée d'attributs spécifiques, créée par l'appel CLI aws bedrock-agentcore-control create-workload-identity, inscrite dans un « agent identity directory » et adossée à un « token vault » stockant jetons OAuth 2.0 et clés d'API, avec prise en charge des flux client credentials (2LO) et authorization code (3LO).

- **primaire** — Provide identity and credential management for agent applications with Amazon Bedrock AgentCore Identity — guide sans numéro de version ni date affichée ; consulté le 2026-07-21, consultée le 2026-07-21 — <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html>
  > Agent identities are implemented as workload identities with specialized attributes that enable agent-specific capabilities while helping to maintain compatibility with industry-standard workload identity patterns.
- **primaire** — AgentCore Identity terminology — guide sans numéro de version ni date affichée ; consulté le 2026-07-21, consultée le 2026-07-21 — <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-terminology.html>
  > Agent identity directory \| A centralized registry that manages agent identities and their associated metadata and access policies. Similar to Cognito User Pools, it acts as a unit of governance for organizing agent identities within an account or region. … Token vault \| A secure storage system for OAuth 2.0 tokens, API keys, and other credentials that operates with strict access controls.
- **primaire** — Create and manage workload identities — guide sans numéro de version ni date affichée ; consulté le 2026-07-21, consultée le 2026-07-21 — <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/creating-agent-identities.html>
  > aws bedrock-agentcore-control create-workload-identity \ --name "my-agent"

**Réserve** — Niveau [C] : aucune source primaire AWS datant le statut (GA ou préversion) d'AgentCore Identity n'a pu être ouverte — les trois URL d'annonce essayées renvoient 404 et la page d'historique du guide n'a rendu qu'un titre (voir failures). Le statut d'AgentCore Identity n'est donc PAS établi par ce lot : ni GA documentée, ni préversion. Les cinq pages du guide développeur ouvertes ne portaient aucune bannière Preview dans le rendu obtenu, mais la conversion en texte peut supprimer les encadrés : cette absence n'est pas exploitable comme fait négatif. La comparaison avec Entra ou Google Cloud reste donc incomplète sur l'axe du statut.

