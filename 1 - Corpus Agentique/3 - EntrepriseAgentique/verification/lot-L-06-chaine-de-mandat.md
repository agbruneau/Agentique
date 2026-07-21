# Lot L-06 — L-06

| Champ | Valeur |
|---|---|
| Lot | **L-06** — phase **P2**, jalon J-3 |
| Débloque | **ch. 9** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 2 en [A], 1 écartée(s) par le vote. **5 échecs de source** consignés |
| Vote | **3 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **7 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (8)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L06-A1` | **[A]** ⚖ | 0 | Le billet officiel de Google du 28 avril 2026, signé Stavan Parikh (VP/GM, Payments), annonce la donation du protocole AP2 à la FIDO Alliance et qualifie l'opération en cours de transfert de propriété (« Transitioning ownership to the FIDO Alliance »). |
| `L06-A3` | **[B]** | 1 | Au 21 juillet 2026, près de trois mois après l'annonce de donation, le dépôt canonique de la spécification AP2 demeure github.com/google-agentic-commerce/AP2, c'est-à-dire dans une organisation GitHub de Google, et sa racine ne comporte aucun fichier de gouvernance : ni GOVERNANCE.md, ni CHARTER.md. |
| `L06-A4` | **[B]** | 0 | La page d'accueil officielle du projet AP2 (ap2-protocol.org, issue de docs/index.md) annonce que la normalisation de la spécification se poursuivra au sein de deux groupes de travail de la FIDO Alliance — Agentic Authentication Technical et Payments Technical — sans énoncer d'échéance. |
| `L06-A5` | **[B]** | 1 | Au 21 juillet 2026, la page « Specifications » du site de la FIDO Alliance ne recense que trois ensembles de spécifications — FIDO U2F, FIDO UAF et CTAP/FIDO2 — et n'y publie aucune spécification d'authentification agentique ni de paiement agentique. |
| `L06-A6` | **[B]** | 1 | Le communiqué de la Linux Foundation du 14 juillet 2026 annonçant le lancement opérationnel de la x402 Foundation porte sur le protocole x402 contribué par Coinbase et ne mentionne ni « AP2 » ni « Agent Payments Protocol ». |
| `L06-A7` | **[B]** | 0 | La spécification AP2 en version v0.2.0, publiée le 28 avril 2026, définit deux types de mandats — Checkout Mandate et Payment Mandate — sérialisés en SD-JWT (RFC 9901), porteurs d'un attribut de type versionné `vct` (p. ex. `mandate.payment.1`), des attributs temporels `iat` et `exp`, et, pour les mandats dits « open », d'un attribut `cnf` (RFC 7800) contenant la clé publique de l'agent ainsi que des contraintes de portée (mar… |
| `L06-A8` | **[A]** ⚖ | 0 | La section 4.1 de la RFC 8693 définit l'attribut `act` comme le moyen d'exprimer, dans un JWT, qu'une délégation a eu lieu et d'identifier la partie agissante, tandis que sa section 1 place explicitement hors périmètre la syntaxe, la sémantique et les caractéristiques de sécurité des jetons eux-mêmes et n'impose aucune exigence sur le modèle de confiance du déploiement. |
| `L06-A9` | **[B]** | 0 | Au 21 juillet 2026, les jetons de transaction (Transaction Tokens) restent pré-normatifs : le document draft-ietf-oauth-transaction-tokens en est à sa révision -09, publiée le 6 juillet 2026, Internet-Draft actif du groupe de travail OAuth de l'IETF expirant le 7 janvier 2027, en appel de dernière relecture de groupe de travail, avec un jalon de soumission à l'IESG annoncé pour décembre 2026 ; aucune RFC n'est publiée. |

⚖ = soumise au vote adversarial à trois juges.

## B. Affirmations écartées par le vote (1)

### `L06-A2` — écartée, 2 réfutations sur 2

> Le communiqué de la FIDO Alliance du 28 avril 2026 qualifie l'apport de Google de « contribution » et non de cession : un balayage ciblé de cette page n'y relève aucune occurrence des chaînes « ownership », « governance », « steward », « transfer » ni « donation ».

- **qualification et bornage** — Trois défauts, dont deux suffisent à refuter.  (1) NÉGATIF DE CORPUS déguisé en qualification positive — décisif. La proposition « … et non de cession » n'est adossée à aucun énoncé de la page : elle est *déduite de l'absence de mots*. Aucune occurrence de « transfer », « ownership », « govern » n'établit que l'apport n'est pas une cession ; elle établit seulement que le communiqué **ne traite pas** la question de la propriété. C'est très exactement le pas interdit par R-14 (« le socle ne documente pas X, donc X n'existe pas »). Le degré 1 est légitime pour la proposition « ces chaînes sont absentes de cette page » ; il est indu pour « l'apport est une contribution et non une cession », qui…
- **fidélité à la source** — Page ouverte et lue intégralement (deux passes, la seconde ciblant le bloc « Support from FIDO Board Members » élidé à la première). Deux acquis : la citation fournie s'y trouve verbatim, et le balayage négatif est confirmé — « ownership », « governance », « steward », « transfer », « donation » : zéro occurrence, y compris dans les douze déclarations de membres du conseil. Deux glissements motivent néanmoins la réfutation. (1) MÉSAPPARIEMENT CITATION/AFFIRMATION : la phrase adduite documente l'apport de MASTERCARD (« Mastercard has contributed its Verifiable Intent framework… »), où Google ne figure qu'à titre de co-développeur. L'affirmation porte sur l'apport DE GOOGLE. La phrase qui l'ét…

## C. Contrôle de bornage — 7 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L06-A2` | **verbe excessif** | Le communiqué de la FIDO Alliance du 28 avril 2026 emploie le terme « contribution » pour désigner l'apport de Google ; un balayage ciblé du texte intégral de cette page, effectué le 21 juillet 2026, n'y relève aucune occurrence des chaînes « ownership », « governance », « steward », « transfer » ni « donation ». Le communiqué ne reprend donc pas le vocabulaire de transfert de propriété employé par Google, sans pour… |
| `L06-A3` | **degré injustifié** | Au 21 juillet 2026, le dépôt lié depuis le site officiel du projet est github.com/google-agentic-commerce/AP2, hébergé sous une organisation GitHub de Google ; l'énumération de la racine de ce dépôt n'y fait apparaître aucun fichier nommé GOVERNANCE.md ni CHARTER.md. Ce constat porte sur la seule racine : ni les sous-répertoires (.github/, docs/) ni d'autres intitulés de gouvernance n'ont été balayés. |
| `L06-A4` | **degré injustifié** | La page d'accueil officielle du projet AP2 (ap2-protocol.org, générée depuis docs/index.md) annonce que la normalisation de la spécification se poursuivra au sein de deux groupes de travail de la FIDO Alliance — Agentic Authentication Technical et Payments Technical. Un balayage de cette page, effectué le 21 juillet 2026, n'y relève aucune date ni échéance associée à cette poursuite. |
| `L06-A5` | **clause d'exclusivité** | Au 21 juillet 2026, la page « Specifications » du site de la FIDO Alliance liste trois ensembles de spécifications — FIDO U2F, FIDO UAF et CTAP/FIDO2 — et n'y fait figurer aucune spécification d'authentification agentique ni de paiement agentique. Cette page est un index : son contenu ne dit rien de ce qui serait publié ailleurs sur le site ou au sein des groupes de travail. |
| `L06-A6` | **degré injustifié** | Un balayage du texte intégral du communiqué de la Linux Foundation du 14 juillet 2026 — qui annonce le lancement opérationnel de la x402 Foundation autour du protocole x402 contribué par Coinbase —, effectué le 21 juillet 2026, n'y relève aucune occurrence des chaînes « AP2 » ni « Agent Payments Protocol ». |
| `L06-A7` | **promesse non démontrée** | La spécification AP2 en version v0.2.0, publiée le 28 avril 2026, définit les types de mandats Checkout Mandate et Payment Mandate, sérialisés en SD-JWT (RFC 9901) et porteurs d'un attribut de type versionné `vct` (p. ex. `mandate.payment.1`) ainsi que des attributs temporels `iat` et `exp` ; pour les mandats dits « open », elle prévoit un attribut `cnf` (RFC 7800) contenant la clé publique de l'agent et des champs d… |
| `L06-A9` | **degré injustifié** | Au 21 juillet 2026, les jetons de transaction (Transaction Tokens) sont pré-normatifs : le document draft-ietf-oauth-transaction-tokens en est à sa révision -09, publiée le 6 juillet 2026, et porte au datatracker de l'IETF le statut d'Internet-Draft actif du groupe de travail OAuth de l'IETF, expirant le 7 janvier 2027 — statut distinct de celui de RFC ; il est en appel de dernière relecture de groupe de travail, ave… |

## D. Échecs de source consignés (5)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Page « Specification » du site officiel AP2 | HTTP 404. Contourné par la source équivalente en amont du site : le fichier docs/ap2/specification.md du dépôt (raw.githubusercontent.com), qui alimente ce site. |
| Page « Core concepts » du site officiel AP2 | HTTP 404. La structure d'URL du site a changé entre v0.1 et v0.2 ; les chemins /topics/ ne résolvent plus. |
| Page « What is AP2 » du site officiel AP2 | HTTP 404, même cause. Contourné par docs/index.md et docs/overview.md du dépôt. |
| Communiqué de la FIDO Alliance sur le fil BusinessWire (identifiant 20260427506015, soit un horodatage au 27 avril 2026, veille de la date affichée sur le site… | Délai d'attente dépassé (60 s). L'écart apparent de date entre l'identifiant du fil (27 avril) et la page de la FIDO Alliance (28 avril) n'a donc PAS pu être vérifié sur la source de fil : ne pas le trancher. |
| Démarrage du lot retardé | Les outils WebSearch et WebFetch ont renvoyé une indisponibilité de classificateur pendant les premières minutes de la passe. Aucune source n'a été perdue ; consigné pour l'exactitude du journal. |

## E. Ce que le lot déclare n'avoir pas couvert

CE QUI N'EST PAS COUVERT, ET POURQUOI.  1. AUCUN ARBITRAGE. Conformément à la consigne, aucune des neuf affirmations ne tranche entre les deux livrables du dépôt. Ce que les sources primaires portent : Google déclare une donation avec « transitioning ownership » (28 avr. 2026) ; la FIDO Alliance déclare une « contribution » le même jour, sans employer les mots « ownership », « governance », « transfer » ni « donation » ; le projet AP2 annonce que la normalisation « se poursuivra » dans deux groupes de travail FIDO, sans échéance ; au 21 juillet 2026 le dépôt canonique est toujours dans l'organisation GitHub de Google, sans fichier de gouvernance, et la FIDO Alliance ne publie aucune spécification agentique. Les sources primaires sont donc CONCORDANTES SUR L'ÉVÉNEMENT (28 avril 2026, AP2 → FIDO Alliance) et ASYMÉTRIQUES SUR SA QUALIFICATION JURIDIQUE. C'est le résultat, pas une préférence.  2. DEUX CONSTATATIONS FAITES, NON RETENUES faute de place (9 entrées maximum), promouvables telles quelles à une passe ultérieure :    (a) CHANGEMENT DE VOCABULAIRE v0.1 → v0.2. Le glossaire du dépôt (https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/glossary.md, branche main, 21 juil. 2026) ne définit ni « Intent Mandate » ni « Cart Mandate » — les deux termes de l'annonce Google Cloud du 16 sept. 2025 (« your request is captured in an initial Intent Mandate » ; « your approval signs a Cart Mandate ») — et définit à leur place « A Mandate used for authorizing the completion of a checkout. » (Checkout Mandate) et « A Mandate used for authorizing the payment for a particular checkout. » (Payment Mandate). Fait négatif de degré 1, borné à ce seul fichier. ⚠ PIÈGE DE RENVOI : tout renvoi du Vol. III à « Intent Mandate » / « Cart Mandate » doit être daté sur v0.1 (16 sept. 2025), sous peine de citer un vocabulaire que la spécification courante n'emploie plus.    (b) AP2 N'INVOQUE PAS OAUTH DANS SON DOCUMENT D'AUTORISATION D'AGENT. Balayage de https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/agent_authorization.md (branche main, 21 juil. 2026) sur les chaînes « OAuth », « oauth », « 8693 », « token exchange », « on-behalf-of », « act claim » : aucune occurrence ; références externes relevées : RFC 9901 (SD-JWT), RFC 7800, OpenID4VP, OpenID4VCI, ISO 18013-5, ISO 18013-7, Delegate SD-JWT. Degré 1, borné à ce seul fichier — cela NE RÉFUTE PAS une compatibilité OAuth, cela constate que ce document ne l'invoque pas. Ce fichier porte par ailleurs la formulation utile au ch. 9 : « Mandates form a cryptographically verifiable chain from the original user-approved Mandate through to the closed Mandate used to authorize a particular Verifier's action. »  3. CONSULTÉ MAIS NON RETENU : draft-ietf-oauth-identity-chaining, « OAuth Identity and Authorization Chaining Across Domains », révision -17 du 19 juillet 2026, Internet-Draft actif du groupe OAuth soumis à l'IESG pour publication, expirant le 20 janvier 2027 (https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/). C'est le texte le plus directement pertinent pour la délégation MULTI-SAUT inter-domaines, thème central du ch. 9 ; il mériterait une entrée à part entière dans une passe complémentaire.  4. NON INSTRUIT DANS CE LOT : le cadre « Verifiable Intent » de Mastercard (deuxième contribution aux groupes FIDO, aucune source primaire ouverte) ; la composition et la charte des deux groupes de travail FIDO (chaires et vice-chaires ne sont attestés que par des reprises de presse, non ouvertes — donc non affirmés ici) ; le contenu de CONTRIBUTING.md et de SECURITY.md du dépôt AP2 ; l'analogie avec le droit civil du mandat (hors sources primaires web) ; le problème des deux sauts et la question KYA (relèvent du lot L-07).  5. AUCUN DOCUMENT DE TRAVAIL PUBLIC DES GROUPES FIDO n'a pu être ouvert — les brouillons de la FIDO Alliance sont réservés aux membres. L'affirmation L06-A5 est donc bornée à la page publique des spécifications : elle constate une absence de PUBLICATION, jamais une absence de TRAVAUX (degré 1 sur le corpus public, rien au-delà).  6. AUCUNE CLAUSE D'EXCLUSIVITÉ n'a été écrite : aucune affirmation ne dit « la seule », « la première », « toutes les ». Les cinq faits négatifs (L06-A2, A3, A5, A6, et les deux du point 2) sont tous bornés à UN document nommé, à UNE date, avec les chaînes cherchées citées.

## F. Sources et citations

### `L06-A1` — [A]

Le billet officiel de Google du 28 avril 2026, signé Stavan Parikh (VP/GM, Payments), annonce la donation du protocole AP2 à la FIDO Alliance et qualifie l'opération en cours de transfert de propriété (« Transitioning ownership to the FIDO Alliance »).

- **primaire** — We're donating Agent Payments Protocol to the FIDO Alliance to support the future of secure, agentic payments. — 28 avril 2026, consultée le 2026-07-21 — <https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/>
  > Transitioning ownership to the FIDO Alliance ensures AP2 remains platform-agnostic and community-led, while accelerating adoption of secure agentic payments.
- **primaire** — FIDO Alliance to Develop Standards for Trusted AI Agent Interactions — 28 avril 2026, consultée le 2026-07-21 — <https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/>
  > Google has contributed its Agent Payments Protocol (AP2), which introduces a model for secure delegation, verifiable authorization and trusted transaction execution.

**Réserve** — La formulation est progressive (« Transitioning »), non accomplie : le billet ne date pas l'achèvement du transfert, ne nomme aucun instrument juridique de cession et ne renvoie à aucune charte. Le billet emploie aussi « we're donating the Agent Payments Protocol (AP2) to the FIDO Alliance, a renowned industry association focused on creating open standards. » Source primaire quant à l'acte de Google, mais c'est un billet d'entreprise, pas un acte de gouvernance publié.

### `L06-A3` — [B]

Au 21 juillet 2026, près de trois mois après l'annonce de donation, le dépôt canonique de la spécification AP2 demeure github.com/google-agentic-commerce/AP2, c'est-à-dire dans une organisation GitHub de Google, et sa racine ne comporte aucun fichier de gouvernance : ni GOVERNANCE.md, ni CHARTER.md.

**Balayage (degré 1)** — Énumération de la racine du dépôt github.com/google-agentic-commerce/AP2 (branche main) le 21 juillet 2026 : répertoires .cspell/, .gemini/, .github/, .mkdocs/, .vscode/, code/, docs/, scripts/ ; fichiers .cspell.json, .editorconfig, .gitignore, .prettierrc, .ruff.toml, CHANGELOG.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md, LICENSE, METADATA, README.md, SECURITY.md, mkdocs.yml, pyproject.toml, requirements-docs.txt. Chaînes cherchées : « GOVERNANCE », « CHARTER » — aucune occurrence dans l'énumération.

- **primaire** — google-agentic-commerce/AP2 — dépôt de la spécification AP2 — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://github.com/google-agentic-commerce/AP2>
  > CHANGELOG.md · CODE_OF_CONDUCT.md · CONTRIBUTING.md · LICENSE · METADATA · README.md · SECURITY.md
- **primaire** — AP2 — docs/index.md (page d'accueil du site ap2-protocol.org) — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/index.md>
  > Our public GitHub repo hosts the lastest version of AP2 specification, documentation and SDK.

**Réserve** — Constat borné à l'énumération de la racine à une date : il ne dit rien du contenu de CONTRIBUTING.md ni des sous-répertoires, et l'absence d'un fichier nommé ainsi n'établit pas l'absence de dispositif de gouvernance ailleurs. Le nom de l'organisation GitHub n'est pas en soi un titre de propriété.

### `L06-A4` — [B]

La page d'accueil officielle du projet AP2 (ap2-protocol.org, issue de docs/index.md) annonce que la normalisation de la spécification se poursuivra au sein de deux groupes de travail de la FIDO Alliance — Agentic Authentication Technical et Payments Technical — sans énoncer d'échéance.

- **primaire** — AP2 — docs/index.md (page d'accueil du site ap2-protocol.org) — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/index.md>
  > Standardization of the specification will continue within the Agentic Authentication Technical and Payments Technical Working Groups in FIDO.

**Réserve** — PROJETÉ : intention déclarée par le projet lui-même (source nominative, état du 21 juillet 2026), sans date de livraison ni jalon. « Will continue within » décrit un cadre de travail futur, non une gouvernance constituée : à ne pas rapporter comme un fait de gouvernance accompli. La page ne date pas cet énoncé.

### `L06-A5` — [B]

Au 21 juillet 2026, la page « Specifications » du site de la FIDO Alliance ne recense que trois ensembles de spécifications — FIDO U2F, FIDO UAF et CTAP/FIDO2 — et n'y publie aucune spécification d'authentification agentique ni de paiement agentique.

**Balayage (degré 1)** — Page fidoalliance.org/specifications/, consultée le 21 juillet 2026 ; chaînes cherchées : « agentic », « AI agent », « agent payment », « AP2 » — aucune occurrence dans la liste des spécifications publiées. La navigation du site mentionne par ailleurs une rubrique d'initiative « Agentic AI » (fidoalliance.org/fido-alliance-agentic-ai/), qui n'est pas une spécification.

- **primaire** — Specifications Overview — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://fidoalliance.org/specifications/>
  > The FIDO Alliance has published three sets of specifications for simpler, stronger user authentication: FIDO Universal Second Factor (FIDO U2F), FIDO Universal Authentication Framework (FIDO UAF) and the Client to Authenticator Protocols (CTAP).

**Réserve** — Borné à cette seule page à cette seule date. L'absence de spécification publiée n'établit pas l'absence de travaux : les groupes de travail de la FIDO Alliance produisent des brouillons réservés aux membres, hors du corpus consulté. Ce constat ne dit rien de la qualité ni du calendrier des travaux ; il établit seulement qu'aucun texte normatif dérivé d'AP2 n'était publié par la FIDO Alliance à cette date.

### `L06-A6` — [B]

Le communiqué de la Linux Foundation du 14 juillet 2026 annonçant le lancement opérationnel de la x402 Foundation porte sur le protocole x402 contribué par Coinbase et ne mentionne ni « AP2 » ni « Agent Payments Protocol ».

**Balayage (degré 1)** — Communiqué linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-…, consulté le 21 juillet 2026 ; chaînes cherchées : « AP2 », « Agent Payments Protocol » — aucune occurrence. Dateline relevée : « SAN FRANCISCO, July 14, 2026 ».

- **primaire** — Linux Foundation Announces Operational Launch of x402 Foundation to Standardize Internet-Native Payments for A… — 14 juillet 2026, consultée le 2026-07-21 — <https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications>
  > the x402 protocol – the universal standard that embeds secure payment capabilities directly into web interactions

**Réserve** — Borné à ce seul communiqué. Il n'établit pas que la Linux Foundation n'a jamais eu de lien avec AP2 ; il constate qu'un protocole de paiement agentique distinct (x402) relève d'une fondation de la Linux Foundation, tandis qu'AP2 est adressé à la FIDO Alliance. Google figure parmi les membres « premier » de la x402 Foundation aux côtés d'Adyen, AWS, American Express, Circle, Cloudflare, Coinbase, Fiserv, Mastercard, Monad Foundation, MoonPay, Ripple, Shopify, Solana Foundation, Stellar Development Foundation, Stripe et Visa : la présence d'un même acteur dans deux enceintes n'est pas une convergence des protocoles.

### `L06-A7` — [B]

La spécification AP2 en version v0.2.0, publiée le 28 avril 2026, définit deux types de mandats — Checkout Mandate et Payment Mandate — sérialisés en SD-JWT (RFC 9901), porteurs d'un attribut de type versionné `vct` (p. ex. `mandate.payment.1`), des attributs temporels `iat` et `exp`, et, pour les mandats dits « open », d'un attribut `cnf` (RFC 7800) contenant la clé publique de l'agent ainsi que des contraintes de portée (marchands autorisés, ensemble de lignes d'articles).

- **primaire** — AP2 Specification (docs/ap2/specification.md) — v0.2, branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/specification.md>
  > implementations MUST match the exact `vct` string, including the version suffix
- **primaire** — AP2 — Checkout Mandate — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/checkout_mandate.md>
  > The Checkout Mandate is a Mandate used for authorizing the completion of a checkout.
- **primaire** — AP2 — Payment Mandate — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/payment_mandate.md>
  > The Payment Mandate Content is created by the Shopping Agent, rendered to the User by the Trusted Surface and verified by the Credential Provider, Network, and Merchant Payment Processor.
- **primaire** — Release v0.2.0 — google-agentic-commerce/AP2 — v0.2.0, 28 avril 2026, consultée le 2026-07-21 — <https://github.com/google-agentic-commerce/AP2/releases/tag/v0.2.0>
  > This is the second release of AP2. It focuses on providing Human Not Present flows.

**Réserve** — R-02 : ce qui est établi, c'est ce que la spécification EXIGE et DÉFINIT — un format, des attributs, une contrainte de vérification (« implementations MUST match the exact `vct` string, including the version suffix »). Ce que la vérification d'un mandat établit en pratique dépend de l'ancrage de confiance, que la spécification laisse au déploiement en proposant deux modèles alternatifs : « User Credential Model » (l'émetteur du justificatif de l'utilisateur est cru par le vérificateur) et « Trusted Agent Provider Model » (le fournisseur d'agent est cru directement). AP2 v0.2 est une spécification de projet, non un texte normatif d'organisme de normalisation.

### `L06-A8` — [A]

La section 4.1 de la RFC 8693 définit l'attribut `act` comme le moyen d'exprimer, dans un JWT, qu'une délégation a eu lieu et d'identifier la partie agissante, tandis que sa section 1 place explicitement hors périmètre la syntaxe, la sémantique et les caractéristiques de sécurité des jetons eux-mêmes et n'impose aucune exigence sur le modèle de confiance du déploiement.

- **primaire** — RFC 8693 — OAuth 2.0 Token Exchange — RFC 8693, §1, §1.1, §4.1, §4.4, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc8693.html>
  > The `act` (actor) claim provides a means within a JWT to express that delegation has occurred and identify the acting party to whom authority has been delegated.
- **primaire** — RFC 8693 — OAuth 2.0 Token Exchange, section 1 (Introduction) — RFC 8693, §1, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc8693.html>
  > the specific syntax, semantics, and security characteristics of the tokens themselves (both those presented to the authorization server and those obtained by the client) are explicitly out of scope, and no requirements are placed on the trust model in which an implementation might be deployed.

**Réserve** — Conséquence à énoncer avec prudence : le flux dit « on-behalf-of » de l'échange de jetons OAuth 2.0 NOMME l'acteur et le sujet ; le texte de la RFC 8693 n'attache à l'attribut `act` aucune assertion sur le consentement du mandant, sur la portée matérielle du mandat ni sur sa durée, celles-ci relevant de la politique du serveur d'autorisation, laissée hors du document. La RFC distingue par ailleurs délégation et usurpation (§1.1) : « With delegation semantics, principal A still has its own identity separate from B ». À ne pas formuler comme « OAuth ne permet pas d'établir le mandant » : il ne le spécifie pas, ce qui est différent.

### `L06-A9` — [B]

Au 21 juillet 2026, les jetons de transaction (Transaction Tokens) restent pré-normatifs : le document draft-ietf-oauth-transaction-tokens en est à sa révision -09, publiée le 6 juillet 2026, Internet-Draft actif du groupe de travail OAuth de l'IETF expirant le 7 janvier 2027, en appel de dernière relecture de groupe de travail, avec un jalon de soumission à l'IESG annoncé pour décembre 2026 ; aucune RFC n'est publiée.

- **primaire** — draft-ietf-oauth-transaction-tokens — Transaction Tokens — révision -09, 6 juillet 2026, expire le 7 janvier 2027, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/>
  > This Internet-Draft is submitted in full conformance with the provisions of BCP 78 and BCP 79.

**Réserve** — Seul le jalon de décembre 2026 est prospectif (PROJETÉ : cible déclarée par le groupe de travail OAuth au registre de l'IETF, sans engagement) ; la révision, sa date et sa date d'expiration sont constatées. ⚠ Fait chaud, à revalider : le -09 expire le 7 janvier 2027 et une révision -10 peut paraître à tout moment. Un Internet-Draft n'est ni un standard ni une préversion de produit : il ne se cite jamais comme spécification établie.

