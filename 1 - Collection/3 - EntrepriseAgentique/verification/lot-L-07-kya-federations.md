# Lot L-07 — L-07

| Champ | Valeur |
|---|---|
| Lot | **L-07** — phase **P2**, jalon J-3 |
| Débloque | **ch. 11** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 1 en [A], 1 écartée(s) par le vote. **4 échecs de source** consignés |
| Vote | **3 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **7 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (8)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L07-A1` | **[B]** | 1 | Le Community Group W3C « Agent Identity Registry Protocol », proposé le 22 avril 2026, était actif au 21 juillet 2026 avec un président (Adolfo Grego Micha, Trustlayer Foundation) et 36 participants non présidents, et n'avait publié à cette date ni rapport ni brouillon de spécification. |
| `L07-A3` | **[B]** | 0 | L'OpenID Foundation a publié le 7 octobre 2025 le livre blanc « Identity Management for Agentic AI: The new frontier of authorization, authentication, and security for an AI agent world », compilé par son Artificial Intelligence Identity Management Community Group ; le document se présente comme un état des ressources disponibles et un agenda stratégique, non comme une spécification ni une norme. |
| `L07-A4` | **[A]** ⚖ | 2 | La charte du Community Group « Artificial Intelligence Identity Management » de l'OpenID Foundation — le groupe qui a compilé le livre blanc de 2025 — place explicitement hors de son périmètre le développement de protocoles de normalisation relatifs à l'identité des agents, et renvoie ce travail à un groupe de travail de l'OIDF ou d'une organisation en liaison. |
| `L07-A5` | **[B]** | 2 | La spécification donnée à la Decentralized Identity Foundation par Vouched en mars 2026 sous le nom MCP-I, renommée « Know Your Agent Operating System » (KYA-OS) et développée par une task force du Trusted AI Agents Working Group, n'était pas ratifiée au 22 juin 2026 : la lettre d'information de la DIF de cette date décrit une version 1 encore soumise à la relecture du groupe de travail et à l'approbation du comité de pilotage… |
| `L07-A6` | **[B]** ⚖ | 3 | Au 21 juillet 2026, le nom « Know Your Agent » désigne au moins deux objets distincts documentés chacun par son propre éditeur : la spécification communautaire KYA-OS développée à la Decentralized Identity Foundation, et le cadre KYA annoncé par Akamai le 15 juin 2026 au sein de son « Agentic Security Framework », avec Skyfire et Experian. |
| `L07-A7` | **[B]** | 2 | Les deux Internet-Drafts consultés portant sur l'identité d'agent — draft-sharif-openid-agent-identity-00 (déposé le 26 mars 2026, expiration le 27 septembre 2026) et draft-drake-agent-identity-registry-03 (déposé le 23 mai 2026, expiration le 24 novembre 2026) — sont au 21 juillet 2026 des soumissions individuelles, non adoptées par un groupe de travail de l'IETF. |
| `L07-A8` | **[B]** | 0 | Le règlement (UE) no 910/2014 (eIDAS) fait reposer la confiance transfrontalière sur deux dispositifs institutionnels inscrits dans son texte : un audit des prestataires de services de confiance qualifiés au moins tous les vingt-quatre mois, à leurs frais, par un organisme d'évaluation de la conformité (art. 20, §1), et l'établissement, la tenue et la publication par chaque État membre de listes de confiance des prestataires q… |
| `L07-A9` | **[B]** | 3 | La FIDO Alliance documente deux dispositifs institutionnels qu'elle exploite elle-même pour la vérification d'un authentificateur : un programme de certification confié à des laboratoires accrédités par l'Alliance, assorti de niveaux de sécurité (L1, L1+, L2, L3, L3+), et le FIDO Metadata Service, dont les parties de confiance téléchargent un fichier JSON signé (MDS3 BLOB) contenant les données de registre des appareils certif… |

⚖ = soumise au vote adversarial à trois juges.

## B. Affirmations écartées par le vote (1)

### `L07-A2` — écartée, 3 réfutations sur 3

> Au 21 juillet 2026, le répertoire des Community Groups du W3C recense trois groupes distincts et simultanés portant sur l'identité ou la confiance des agents — « Agentic Integrity Verification Specification » (proposé le 14 mars 2026, 12 participants), « Agent Identity Registry Protocol » (proposé le 22 avril 2026, 37 participants) et « Agent Trust Protocol (ATP) » (lancé le 4 juin 2026, 11 participants) — et aucun des trois n'a publié de rapport à cette date.

- **qualification et bornage** — Trois des quatre contrôles se déclenchent.  (2) DEGRÉ INJUSTIFIÉ — décisif. Le balayage déclaré est explicitement une requête de registre par mot-clé : « Répertoire […] interrogé sur les intitulés contenant « Agent » ». La règle est sans exception : une telle requête ne vaut jamais mieux qu'un degré 3. Le degré 1 (VÉRIFIÉ) exige le balayage d'un texte ouvert avec ses chaînes ; ici aucun texte n'est balayé, seul un index est filtré. Un groupe portant sur l'identité d'agent mais intitulé autrement (« Non-Human Identity », « Verifiable Autonomous Systems », « Machine Trust ») échappe mécaniquement au filtre. Le recensement à trois n'est donc pas clos.  (1) NÉGATIF DE CORPUS. « Aucun des trois n…
- **statut et datation** — Deux défauts constatés sur les pages primaires elles-mêmes.  1) DÉNOMBREMENT FAUX PAR OMISSION — « trois groupes distincts et simultanés portant sur l'identité ou la confiance des agents ». Le répertoire https://www.w3.org/community/groups/ recense au moins un quatrième groupe actif dont la mission porte explicitement l'identité : « AI Agent Protocol » CG (créé le 8 mai 2025, 256 participants), mission verbatim : « develop open, interoperable protocols that enable AI agents to discover, identify, and collaborate efficiently across the Web », charte couvrant « agent identity models » et la confiance par attestations vérifiables. Il éclipse les trois cités (256 participants contre 12, 37 et 11…
- **fidélité à la source** — Les quatre citations verbatim ont été retrouvées mot pour mot sur les pages citées, et les dates (14 mars, 22 avril, 4 juin 2026) comme les décomptes (12, 37, 11 participants) sont confirmés sur pièce ; l'absence de rapport des trois groupes est confirmée à w3.org/community/reports/. La refutation ne porte pas sur ces éléments mais sur le recensement : l'affirmation énonce que « le répertoire des Community Groups du W3C recense trois groupes distincts et simultanés portant sur l'identité ou la confiance des agents », alors que ce même répertoire — source primaire invoquée — en liste un quatrième répondant au critère, AI Agent Protocol CG (créé le 8 mai 2025, 256 participants, soit davantage…

## C. Contrôle de bornage — 7 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L07-A1` | **degré injustifié** | Le Community Group W3C « Agent Identity Registry Protocol » (proposition du 22 avril 2026) figure au répertoire des Community Groups du W3C, page consultée le 21 juillet 2026 : elle affiche un président (Adolfo Grego Micha, Trustlayer Foundation) et 36 participants non présidents, et ne liste à cette date aucun rapport ni brouillon de spécification. Fait négatif de degré 2 : il est porté par l'état d'une fiche de rép… |
| `L07-A2` | **clause d'exclusivité** | Au 21 juillet 2026, une consultation du répertoire des Community Groups du W3C relève au moins trois groupes simultanés portant sur l'identité ou la confiance des agents : « Agentic Integrity Verification Specification » (proposé le 14 mars 2026, 12 participants), « Agent Identity Registry Protocol » (proposé le 22 avril 2026, 37 participants) et « Agent Trust Protocol (ATP) » (lancé le 4 juin 2026, 11 participants).… |
| `L07-A2` | **degré injustifié** | Aucune des trois fiches de répertoire relevées le 21 juillet 2026 ne liste de rapport publié. Fait négatif de degré 2 : il porte sur l'état des fiches du répertoire du W3C, sans balayage d'un texte ouvert. |
| `L07-A6` | **statut non dit** | Au 21 juillet 2026, le nom « Know Your Agent » désigne au moins deux objets distincts, documentés chacun par son propre éditeur : KYA-OS, spécification communautaire développée à la Decentralized Identity Foundation et non ratifiée au 22 juin 2026 (version 1 encore soumise à la relecture du groupe de travail et à l'approbation du comité de pilotage), et le cadre KYA annoncé le 15 juin 2026 par Akamai au sein de son «… |
| `L07-A7` | **clause d'exclusivité** | Deux Internet-Drafts consultés le 21 juillet 2026 et portant sur l'identité d'agent — draft-sharif-openid-agent-identity-00 (déposé le 26 mars 2026, expiration le 27 septembre 2026) et draft-drake-agent-identity-registry-03 (déposé le 23 mai 2026, expiration le 24 novembre 2026) — portent l'un et l'autre, au Datatracker de l'IETF, le statut de soumission individuelle : ni l'un ni l'autre n'est adopté par un groupe de… |
| `L07-A8` | **clause d'exclusivité** | Le règlement (UE) no 910/2014 (eIDAS) institue notamment deux dispositifs à l'appui de la confiance transfrontalière : un audit des prestataires de services de confiance qualifiés au moins tous les vingt-quatre mois, à leurs frais, par un organisme d'évaluation de la conformité (art. 20, §1), et l'établissement, la tenue et la publication par chaque État membre de listes de confiance des prestataires qualifiés (art.… |
| `L07-A9` | **promesse non démontrée** | La FIDO Alliance documente notamment deux dispositifs institutionnels qu'elle exploite elle-même : un programme de certification confié à des laboratoires accrédités par l'Alliance, assorti de niveaux de sécurité (L1, L1+, L2, L3, L3+), et le FIDO Metadata Service, dont les parties de confiance téléchargent un fichier JSON signé (MDS3 BLOB) contenant les données de registre des modèles d'appareils certifiés. Ce que l… |

## D. Échecs de source consignés (4)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Tentative de consultation du Community Group W3C « AI Agent Protocol » à une URL devinée | HTTP 404. L'URL réelle relevée ensuite au répertoire des groupes est https://www.w3.org/community/agentprotocol/ ; elle n'a pas été ouverte dans ce lot, faute de rapport direct avec l'identité (son objet déclaré est la découverte et la coll… |
| Document primaire du cadre « Know Your Agent: An Identity Framework for Trusted Agentic Commerce » de Trulioo et PayOS, daté du 4 février 2026, avec son « Digit… | Seule une source secondaire (billet de blogue stablecoininsider.org) le décrit ; ni l'URL du document primaire ni sa page d'éditeur n'ont été localisées dans ce lot. Le fait est donc signalé en caveat de L07-A6 et non porté comme affirmatio… |
| Texte intégral du livre blanc de l'OpenID Foundation (PDF) | Seuls la page de résumé arXiv et le billet d'annonce de l'OIDF ont été ouverts ; le corps du document n'a pas été lu. Aucune affirmation de ce lot ne porte sur son contenu détaillé, et L07-A3 le dit en caveat. |
| Panne temporaire des outils WebSearch et WebFetch en ouverture de lot (classificateur de sûreté indisponible) | Cinq appels rejetés successivement pendant environ une minute, puis rétablissement complet. Aucune source perdue ; consigné pour la traçabilité du relevé. |

## E. Ce que le lot déclare n'avoir pas couvert

RÉPONSE DATÉE À LA CONSIGNE (le fait saillant hérité de H-19 : « aucun forum n'avait tranché à juin 2026 »). Vérification du 21 juillet 2026 : la situation n'a pas été tranchée, elle s'est densifiée. Six chantiers relevant de cinq organisations distinctes étaient ouverts simultanément, chacun à un stade pré-normatif à la date de sa dernière pièce consultée — trois Community Groups au W3C seul (L07-A2), la task force KYA-OS de la DIF avec une v1 non ratifiée au 22 juin 2026 (L07-A5), le Community Group AIIM de l'OpenID Foundation qui exclut de sa charte la normalisation protocolaire (L07-A4), deux Internet-Drafts individuels non adoptés à l'IETF (L07-A7), et côté fédéral américain le NCCoE du NIST. Aucune des pages consultées ne désigne un forum unique ; la page du CG W3C AIRP annonce au contraire une coordination avec quatre autres instances (« the W3C Credentials Community Group (CCG), the Decentralized Identity Foundation (DIF), the OpenID Foundation AIIM Community Group, and the IETF WIMSE Working Group »). Formulation prudente imposée par la leçon D : le relevé ne soutient pas la thèse qu'un forum aurait été désigné ; il n'établit pas non plus qu'aucun ne l'ait été hors des sources consultées (degré 3).  VOLET NIST — instruit mais non retenu comme affirmation, faute de place sous le plafond de neuf ; à reprendre tel quel dans un lot ultérieur, les sources ayant été ouvertes le 21 juillet 2026. (1) Le NCCoE du NIST a publié le 5 février 2026 une note de cadrage (concept paper, initial public draft) intitulée « Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization », consultation publique close le 2 avril 2026 — https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd et le PDF https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf. C'est un cadrage de projet sollicitant des commentaires, pas une norme. (2) Le Center for AI Standards and Innovation (CAISI) du NIST a lancé le 17 février 2026 une « AI Agent Standards Initiative » à trois piliers (« Facilitating Industry-led Standards », « Fostering Community-led Protocols », « Investing in Research ») — https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative ; jalons relevés : réponses à l'appel à contributions le 9 mars, inscriptions aux séances d'écoute le 20 mars, commentaires sur la note de cadrage le 2 avril. Ces deux pièces renforcent L07-A2 et la réponse ci-dessus.  CE QUE CE LOT N'A PAS COUVERT. (a) La transposabilité proprement dite des précédents de fédération : L07-A8 et L07-A9 établissent les conditions institutionnelles côté eIDAS (audit périodique par tiers, listes de confiance publiées par une autorité désignée) et côté FIDO (laboratoires accrédités, registre signé consulté par les parties de confiance), mais le raisonnement « ce qui manque côté agentique » reste une construction d'auteur à marquer (CA-07) : aucune source consultée n'énonce ce manque sous cette forme. Ce qui est constaté, et seulement cela : aucune des six initiatives relevées ne s'accompagne d'un organisme d'évaluation de la conformité désigné, d'un rythme d'audit inscrit dans un texte, ni d'une liste de confiance publiée — constat borné aux pages effectivement ouvertes, degré 3 au-delà. (b) Le règlement (UE) 2024/1183 (eIDAS 2) et le portefeuille européen d'identité numérique : non ouverts, alors qu'ils portent la mise à jour la plus pertinente du précédent européen. (c) L'ISO/IEC : aucune recherche menée, alors que H-19 nomme l'ISO parmi les forums n'ayant pas tranché — l'absence de l'ISO dans ce relevé est une absence de documentation, pas un fait négatif. (d) Les composantes d'identité d'AGNTCY et le groupe de travail WIMSE de l'IETF, tous deux nommés comme partenaires de coordination par le CG W3C, n'ont pas été instruits. (e) Le préprint arXiv:2603.24775 (AIP, Sunil Prakash, déposé le 25 mars 2026) hérité de H-19 a été vérifié comme existant et correctement daté par le Vol. I ; il reste un préprint non évalué par les pairs et l'étiquette SPÉCULATIF du Vol. I n'a pas lieu d'être révisée. (f) Deux préprints de synthèse repérés et non exploités, utiles à une relecture adverse : arXiv:2604.23280 (« AI Identity: Standards, Gaps, and Research Directions for AI Agents », Otsuka, Toyoda, Leung, 25 avril 2026) et arXiv:2604.11337.

## F. Sources et citations

### `L07-A1` — [B]

Le Community Group W3C « Agent Identity Registry Protocol », proposé le 22 avril 2026, était actif au 21 juillet 2026 avec un président (Adolfo Grego Micha, Trustlayer Foundation) et 36 participants non présidents, et n'avait publié à cette date ni rapport ni brouillon de spécification.

**Balayage (degré 1)** — Balayage du 21 juillet 2026, mené par consultation directe des trois emplacements suivants. (1) https://www.w3.org/community/agent-identity/ : relevé exhaustif des intitulés de sections — « Agent Identity Registry Protocol Community Group », « Community & Business Groups », « Call for Participation in Agent Identity Registry Protocol Community Group », « Tools for this group », « Get involved », « Chairs », « Participants », « Archives », « Categories ». Aucune section « Reports », « Specifications » ni « Drafts ». Chaînes cherchées : « chair », « report », « specification », « draft ». La page porte elle-même la mention « Chairs, when logged in, may publish draft and final reports », ce qui indique l'emplacement où un rapport apparaîtrait s'il existait. (2) https://www.w3.org/community/agent-identity/participants : « 36 Non-Chair participants found », un président listé. (3) https://github.com/w3c-cg/agent-identity, racine du dépôt : CODE_OF_CONDUCT.md, CONTRIBUTING.md, LICENSE.md, README.md, w3c.json — 6 commits, aucun fichier de spécification.

- **primaire** — Agent Identity Registry Protocol Community Group — page consultée dans son état du 21 juillet 2026 ; groupe proposé le 20…, consultée le 2026-07-21 — <https://www.w3.org/community/agent-identity/>
  > This group was originally proposed on 2026-04-22 by Aaron Adolfo Grego.
- **primaire** — Participants in the Agent Identity Registry Protocol Community Group — 21 juillet 2026, consultée le 2026-07-21 — <https://www.w3.org/community/agent-identity/participants>
  > 36 Non-Chair participants found
- **primaire** — Proposed Group: Agent Identity Registry Protocol Community Group — 24 avril 2026, consultée le 2026-07-21 — <https://www.w3.org/community/blog/2026/04/24/proposed-group-agent-identity-registry-protocol-community-group/>
  > This group will take inspiration from work created by TrustLayer Foundation A.C., and that work may inform the group's discussions. That work does not constrain the group's discussions, and all decisions about the group's deliverables will be made by the Community Group participants.
- **primaire** — w3c-cg/agent-identity (dépôt du Community Group) — état du 21 juillet 2026, 6 commits, consultée le 2026-07-21 — <https://github.com/w3c-cg/agent-identity>
  > No description, website, or topics provided.

**Réserve** — Un Community Group du W3C n'est pas un Working Group : il n'est pas sur la voie des Recommandations et le W3C n'endosse pas ses productions. Le balayage porte sur la page du groupe, sa page de participants et la racine de son dépôt, au 21 juillet 2026 ; il n'établit rien sur d'éventuels documents circulant hors de ces trois emplacements (degré 3 pour ceux-là). Le billet d'annonce du 24 avril 2026 indiquait « The group must now choose a chair » : la présidence a donc été pourvue entre le 24 avril et le 21 juillet 2026, sans que la date exacte ait pu être établie.

### `L07-A3` — [B]

L'OpenID Foundation a publié le 7 octobre 2025 le livre blanc « Identity Management for Agentic AI: The new frontier of authorization, authentication, and security for an AI agent world », compilé par son Artificial Intelligence Identity Management Community Group ; le document se présente comme un état des ressources disponibles et un agenda stratégique, non comme une spécification ni une norme.

- **primaire** — New whitepaper tackles AI agent identity challenges — 7 octobre 2025, consultée le 2026-07-21 — <https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/>
  > The OpenID Foundation has today released a critical new whitepaper addressing one of the most pressing challenges facing organizations deploying AI agents
- **primaire** — Identity Management for Agentic AI: The new frontier of authorization, authentication, and security for an AI… — v1, soumise le 29 octobre 2025, consultée le 2026-07-21 — <https://arxiv.org/abs/2510.25819>
  > This OpenID Foundation whitepaper is for stakeholders at the intersection of AI agents and access management. It outlines the resources already available for securing today's agents and presents a strategic agenda to address the foundational authentication, authorization, and identity problems pivotal for tomorrow's widespread autonomous systems.

**Réserve** — Deux dates coexistent pour un même document et ne doivent pas être confondues : publication par l'OpenID Foundation le 7 octobre 2025 ; dépôt de la prépublication arXiv 2510.25819v1 le 29 octobre 2025 (aucune révision listée). Le Vol. I retient la première seule. La qualification « non une spécification » repose sur la description que le document donne de lui-même (« strategic agenda », « best practices ») et sur la charte du CG émetteur (cf. L07-A4), non sur un balayage du texte intégral du livre blanc, qui n'a pas été ouvert dans ce lot (degré 3 pour son contenu détaillé).

### `L07-A4` — [A]

La charte du Community Group « Artificial Intelligence Identity Management » de l'OpenID Foundation — le groupe qui a compilé le livre blanc de 2025 — place explicitement hors de son périmètre le développement de protocoles de normalisation relatifs à l'identité des agents, et renvoie ce travail à un groupe de travail de l'OIDF ou d'une organisation en liaison.

**Balayage (degré 2)** — Fait négatif ÉTABLI (degré 2) : la réserve est portée par la source elle-même, dans la rubrique « The following are out of scope for the proposed AI CG » de la page de charte du groupe. Aucun balayage de ma part n'est revendiqué.

- **primaire** — Artificial Intelligence Identity Management Community Group — page consultée dans son état du 21 juillet 2026, consultée le 2026-07-21 — <https://openid.net/cg/artificial-intelligence-identity-management-community-group/>
  > Development of any global standards protocols related to AI Agents & Identity. Any such protocol work will be deferred to an OIDF or liaison working group.
- **primaire** — Artificial Intelligence Identity Management Community Group — commande du conseil — avril 2025, consultée le 2026-07-21 — <https://openid.net/cg/artificial-intelligence-identity-management-community-group/>
  > The OIDF board commissioned in April 2025 a paper on the intersection of Agentic AI and Identity.

**Réserve** — La réserve porte sur le périmètre déclaré du Community Group, non sur l'OpenID Foundation dans son ensemble : l'existence ou non d'un groupe de travail OIDF constitué depuis pour reprendre ce travail n'a pas été vérifiée dans ce lot (degré 3). Les coprésidents relevés sont Atul Tulshibagwale (CrowdStrike) et Jeff Lombardo (AWS) ; la date de constitution formelle du CG n'est pas donnée par la page, qui mentionne seulement une commande du conseil de l'OIDF en avril 2025.

### `L07-A5` — [B]

La spécification donnée à la Decentralized Identity Foundation par Vouched en mars 2026 sous le nom MCP-I, renommée « Know Your Agent Operating System » (KYA-OS) et développée par une task force du Trusted AI Agents Working Group, n'était pas ratifiée au 22 juin 2026 : la lettre d'information de la DIF de cette date décrit une version 1 encore soumise à la relecture du groupe de travail et à l'approbation du comité de pilotage.

**Balayage (degré 2)** — Fait négatif ÉTABLI (degré 2) : l'absence de ratification est énoncée par la DIF elle-même — « working its way through working group feedback and Steering Committee approval at time of press » et « KYA-OS v1.0 is closing in on formal ratification » (lettre d'information no 62, 22 juin 2026). Aucun balayage de ma part n'est revendiqué.

- **primaire** — Why We Brought KYA-OS (formerly MCP-I) to DIF (and Why DIF Said Yes) — 5 mars 2026, consultée le 2026-07-21 — <https://blog.identity.foundation/why-dif-said-yes-to-mcp-i/>
  > this was originally published with the name that had been used by Vouched, which was MCP-I. As we discussed this in DIF, we have renamed the specification to KYA-OS as a more widely applicable Agentic Identity Solution which can be used for MCP as well as other Agentic AI frameworks.
- **primaire** — DIF and Vouched Advance Agentic Identity with KYA-OS as International Demand for Open Agent Identity Standards… — 22 avril 2026, consultée le 2026-07-21 — <https://blog.identity.foundation/kya-os/>
  > The specification, donated in March 2026, will advance under a new name: Know Your Agent Operating System (KYA-OS).
- **primaire** — DIF Newsletter #62 — 22 juin 2026, consultée le 2026-07-21 — <https://blog.identity.foundation/dif-newsletter-62/>
  > KYA-OS has cut a v1 which is working its way through working group feedback and Steering Committee approval at time of press, with a roadmap for defining extension points (such as pluggable support for arbitrary additional DID methods, [delegated] authorization languages, etc) and hardening them as DIF members author or inform extensions at various levels.
- **primaire** — DIF — Trusted AI Agents Working Group — page consultée dans son état du 21 juillet 2026, consultée le 2026-07-21 — <https://identity.foundation/working-groups/trusted-agents.html>
  > The Trusted AI Agents Working Group (WG) at the Decentralized Identity Foundation (DIF) focuses on defining an opinionated, interoperable stack to enable trustworthy, privacy-preserving, and secure AI agents.

**Réserve** — La ratification est PROJETÉE au sens du tri prospectif : prévision attribuée à la DIF, millésime 22 juin 2026, périmètre KYA-OS v1.0, sans date annoncée. Le statut n'a pas été revérifié entre le 22 juin et le 21 juillet 2026 (degré 3 pour cet intervalle). La rebaptisation MCP-I → KYA-OS est déclarée par la DIF le 5 mars 2026 ; l'antériorité et la portée exactes de MCP-I chez Vouched n'ont pas été instruites.

### `L07-A6` — [B]

Au 21 juillet 2026, le nom « Know Your Agent » désigne au moins deux objets distincts documentés chacun par son propre éditeur : la spécification communautaire KYA-OS développée à la Decentralized Identity Foundation, et le cadre KYA annoncé par Akamai le 15 juin 2026 au sein de son « Agentic Security Framework », avec Skyfire et Experian.

- **primaire** — Akamai Unveils Agentic Security Framework to Power Trusted AI-Driven Interactions and Commerce — 15 juin 2026, consultée le 2026-07-21 — <https://www.akamai.com/newsroom/press-release/akamai-unveils-agentic-security-framework-to-power-trusted-ai-driven-interactions-and-commerce>
  > trusted AI agent identity through the "Know Your Agent" (KYA) framework, which provides a standardized way for agents to declare identity, origin, and intent, linking them to the platforms they operate on and the users they represent
- **primaire** — DIF and Vouched Advance Agentic Identity with KYA-OS as International Demand for Open Agent Identity Standards… — 22 avril 2026, consultée le 2026-07-21 — <https://blog.identity.foundation/kya-os/>
  > The framework is being developed under open, community-driven governance through the KYA-OS Task Force within DIF's Trusted AI Agents Working Group.

**Réserve** — Le communiqué d'Akamai du 15 juin 2026 ne qualifie pas le statut de disponibilité du cadre KYA : il n'y est écrit ni disponibilité générale, ni préversion, ni feuille de route datée, et le cadre n'y est rattaché à aucune spécification publiée. Aucun lien de dépendance, de compatibilité ou de filiation entre le cadre d'Akamai et KYA-OS n'a été recherché : absence de documentation (degré 3), et non fait négatif. L'énoncé dit « au moins deux » et ne porte aucune clause d'exclusivité ; une troisième occurrence — le cadre « Know Your Agent » de Trulioo et PayOS, daté du 4 février 2026 — est signalée par une source secondaire dont le document primaire n'a pas été ouvert (cf. failures).

### `L07-A7` — [B]

Les deux Internet-Drafts consultés portant sur l'identité d'agent — draft-sharif-openid-agent-identity-00 (déposé le 26 mars 2026, expiration le 27 septembre 2026) et draft-drake-agent-identity-registry-03 (déposé le 23 mai 2026, expiration le 24 novembre 2026) — sont au 21 juillet 2026 des soumissions individuelles, non adoptées par un groupe de travail de l'IETF.

**Balayage (degré 2)** — Fait négatif ÉTABLI (degré 2) : le statut de soumission individuelle et l'absence d'endossement sont portés par le datatracker de l'IETF lui-même, qui affiche pour les deux documents la mention d'un Internet-Draft individuel sans standing dans le processus de normalisation.

- **primaire** — OpenID Connect Agent Identity Claims for Autonomous AI Agents (draft-sharif-openid-agent-identity-00) — version 00, déposée le 26 mars 2026 ; expiration le 27 septembre 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-sharif-openid-agent-identity/>
  > This specification defines a profile of OpenID Connect Core 1.0 that enables Identity Providers (IdPs) to issue identity tokens for autonomous software agents.
- **primaire** — Agent Identity Registry System: A Federated Architecture for Hardware-Anchored Identity of Autonomous Entities… — version 03, déposée le 23 mai 2026 ; expiration le 24 novembre 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-drake-agent-identity-registry/>
  > Agent Identity Registry System: A Federated Architecture for Hardware-Anchored Identity of Autonomous Entities

**Réserve** — Les deux documents ont été trouvés par recherche par mots-clés : un résultat de requête ne teste qu'une chaîne, pas un objet. Le relevé n'établit donc pas qu'il n'existe pas d'autres Internet-Drafts sur le même objet (degré 3). Les dates d'expiration sont PROGRAMMÉES au sens strict — elles découlent mécaniquement de la règle des six mois de l'IETF et sont affichées par le datatracker ; elles n'annoncent aucun résultat de normalisation. draft-drake-agent-identity-registry en est à sa version 03, ce qui indique une révision active mais ne vaut pas adoption.

### `L07-A8` — [B]

Le règlement (UE) no 910/2014 (eIDAS) fait reposer la confiance transfrontalière sur deux dispositifs institutionnels inscrits dans son texte : un audit des prestataires de services de confiance qualifiés au moins tous les vingt-quatre mois, à leurs frais, par un organisme d'évaluation de la conformité (art. 20, §1), et l'établissement, la tenue et la publication par chaque État membre de listes de confiance des prestataires qualifiés (art. 22, §1).

- **primaire** — Regulation (EU) No 910/2014 … on electronic identification and trust services for electronic transactions in t… — règlement du 23 juillet 2014, texte CELEX 32014R0910, consultée le 2026-07-21 — <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0910>
  > Qualified trust service providers shall be audited at their own expense at least every 24 months by a conformity assessment body. The purpose of the audit shall be to confirm that the qualified trust service providers and the qualified trust services provided by them fulfil the requirements laid down in this Regulation.
- **primaire** — Regulation (EU) No 910/2014 — Article 22(1) (Trusted lists) — règlement du 23 juillet 2014, texte CELEX 32014R0910, consultée le 2026-07-21 — <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0910>
  > Each Member State shall establish, maintain and publish trusted lists, including information related to the qualified trust service providers for which it is responsible, together with information related to the qualified trust services provided by them.

**Réserve** — Le texte cité est celui du règlement de base du 23 juillet 2014, dans sa version publiée au Journal officiel. Les modifications apportées par le règlement (UE) 2024/1183 n'ont pas été vérifiées sur ces deux articles précis (degré 3). eIDAS ne vise pas les agents logiciels : toute transposition au domaine agentique est une lecture d'auteur, non un constat du texte. Les articles décrivent une procédure institutionnelle — audit périodique, publication d'une liste — et non une propriété de sécurité démontrée.

### `L07-A9` — [B]

La FIDO Alliance documente deux dispositifs institutionnels qu'elle exploite elle-même pour la vérification d'un authentificateur : un programme de certification confié à des laboratoires accrédités par l'Alliance, assorti de niveaux de sécurité (L1, L1+, L2, L3, L3+), et le FIDO Metadata Service, dont les parties de confiance téléchargent un fichier JSON signé (MDS3 BLOB) contenant les données de registre des appareils certifiés.

- **primaire** — FIDO Metadata Service — page sans version ni date affichée ; consultée le 21 juillet 2026 (res…, consultée le 2026-07-21 — <https://fidoalliance.org/metadata/>
  > The FIDO Metadata Service (MDS) helps ensure you have the information necessary to successfully validate authenticators.
- **primaire** — FIDO Certification Programs — page sans version ni date affichée ; consultée le 21 juillet 2026 (res…, consultée le 2026-07-21 — <https://fidoalliance.org/certification/>
  > adhere to FIDO user authentication specifications for conformance, security, and interoperability – enabling trusted sign-ins with passkey at scale

**Réserve** — Le mécanisme est qualifié par ce que la FIDO Alliance documente comme procédure — accréditation de laboratoires, certification, publication d'un BLOB signé consulté par les parties de confiance —, non par une propriété de sécurité démontrée : les pages consultées ne présentent aucune démonstration cryptographique. Le relevé des deux pages ne fait pas apparaître la procédure de retrait ou de révocation d'une entrée du MDS ; il s'agit d'une absence de documentation dans le corpus consulté (degré 3), non d'un fait négatif. Aucune version ni date de publication n'est affichée sur la page /metadata/ consultée, ce qui en fait une ressource vivante.

