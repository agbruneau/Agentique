# F Validation des sources et des ébauches

Cette annexe rend compte de la vérification qui fonde la version 1.0 : comment les 121 références de la recherche documentaire ont été validées, ce que la vérification a révélé, et quelles affirmations des ébauches ont été corrigées ou retirées. Elle permet de retracer l’origine des faits de la version 1.0 et le degré de confiance qu’on peut leur accorder; ses limites sont dites en F.1 et à la légende du tableau 69.

## F.1 Méthode

La vérification s’est déroulée en trois passes, les 27 et 28 octobre 2026.

1. **Validation référence par référence.** Chacune des 121 références de la recherche documentaire a fait l’objet d’une tentative d’ouverture; pour les 13 pages bloquées, payantes ou redirigées, on s’est limité au résumé public ou à une source primaire. On a consigné son accessibilité, son éditeur, sa date et sa catégorie de crédibilité, puis confronté chaque affirmation qui la citait au contenu réel de la page (427 liens affirmation-source au total). Lorsqu’une page n’appuyait pas une affirmation, une source primaire a été recherchée pour la confirmer ou la réfuter.
2. **Vérification thématique.** Onze vérifications ont confronté les affirmations des quatre ébauches aux textes primaires : MCP; A2A et protocoles connexes; plateformes et fondations; identité; sécurité; observabilité, contrats et événements; orchestration; autonomie; droit québécois et canadien; référentiels internationaux; économie et données de marché. Elles ont aussi recueilli les faits complémentaires intégrés au cadre.
3. **Audit final.** Le 28 octobre 2026, chacune des 428 références alors citées dans le corps du cadre a été rouverte à sa source et confrontée, affirmation par affirmation, aux passages qui s’y appuient (1 409 affirmations examinées). L’identité de chaque référence (auteurs, titre, date, éditeur), sa catégorie et son statut à cette date ont été contrôlés, et les écarts les plus graves ont été recontrôlés par un second examinateur indépendant, qui a réfuté plusieurs reclassements proposés. En parallèle, tous les chapitres et annexes ont été relus pour la cohérence interne, l’exactitude factuelle et juridique, la formulation des exigences et la langue. Les corrections retenues ont été intégrées au texte, et le texte des exigences, les échelles et les renvois ont été harmonisés. À l’issue de l’audit, l’annexe G comptait 473 entrées dont 25 doublons (448 sources distinctes); lors de la remédiation d’intégrité (19 novembre 2026), ces 25 doublons ont été dédupliqués et redirigés vers leur entrée canonique (sans réattribution des numéros libérés). Les passes ne portent pas sur la même population (121 références, puis 428 à l’audit final, puis 448 sources distinctes issues des 473 entrées initiales); l’écart de 45 entrées initiales correspond aux références [429] à [473], ajoutées lors de la consolidation et vérifiées le 27 octobre 2026 (historique des versions), et le relevé lien par lien des affirmations et des sources n’est pas publié. La version 1.1 ajoute la référence [474] (RFC 7515, section 6.6, ex-[496]), ce qui porte l’annexe G à 449 entrées et 449 sources distinctes (0 doublon), suivies en ordre croissant des 22 références [475] à [496] de l’annexe H. Les arbitrages d’architecture et de gouvernance relevés lors de cet audit ont également été tranchés et intégrés à la présente version.

*Tableau 66 — Catégories de crédibilité des sources*

| **Catégorie** | **Définition** | **Usage dans le cadre** |
| --- | --- | --- |
| **A** | Source primaire ou officielle : organismes de normalisation et leurs dépôts (IETF, W3C, ISO, NIST, OWASP, CNCF, OpenTelemetry, Linux Foundation et sites des projets), textes législatifs et organismes de réglementation, documentation officielle d’un éditeur sur son propre produit, articles scientifiques d’auteurs identifiables. | Appui de tout fait. Une exigence ne s’appuie que sur une source apte à la fonder (norme, loi, spécification, documentation officielle) : un article non révisé par les pairs établit ce que ses auteurs affirment, non une exigence à lui seul. |
| **B** | Source secondaire reconnue ou d’analystes : grande presse spécialisée, cabinets juridiques, experts reconnus, communiqués, rapports et prévisions des firmes d’analystes (ex. Gartner), études d’éditeurs, d’investisseurs ou de cabinets. | Appui d’un fait de contexte ou d’un ordre de grandeur prospectif, jamais seul pour une exigence ni comme preuve primaire. |
| **C** | Blogue de positionnement, agrégateur, site inconnu ou contenu généré en série. | Jamais cité à l’appui d’un fait ou d’une exigence; remplacé par une source A ou B, ou fait retiré. Un argument d’éditeur peut être nommé comme tel dans le texte, sans appel d’appui; une entrée de l’annexe G de cette catégorie y est signalée. |

La catégorie d’une entrée tient à la nature de la source, non à la firme qui la publie : un communiqué, un billet ou une étude d’éditeur vaut comme source primaire de ce que son éditeur affirme de lui-même ou de ses produits (catégorie A), et comme source secondaire pour toute affirmation sur le marché ou sur d’autres produits (catégorie B); les communiqués, rapports et prévisions de firmes d’analystes (dont Gartner) sont classés hors catégorie A, en catégorie B (sources secondaires / contexte prospectif), dans le présent tableau, au tableau 69 et à l’annexe G; un blogue de positionnement ou un agrégateur reste en catégorie C.

## F.2 Bilan chiffré

Les quatre premiers décomptes portent sur les 121 références et sur les 427 liens affirmation-source de la recherche documentaire; les deux derniers (705 et 448) portent sur la version finale.

**121**

références validées une à une, dont 108 accessibles et 13 bloquées, payantes ou redirigées

**61**

références de catégorie C (50 %), dont 33 présentant les marques d’un contenu généré en série

**88**

références remplacées (71) ou retirées (17); 33 conservées comme sources A ou B

**23**

références du registre reprises à l’annexe G à l’audit final (colonne « no G » du tableau 69) : 18 des 33 conservées et les 5 réintroduites; 15 conservées n’y figurent pas et restent admissibles sans appuyer de fait

**705**

sources admissibles (A ou B) recensées pour la version finale, dont 625 de catégorie A et 80 de catégorie B après reclassement des firmes d’analystes (Gartner) hors catégorie A; 49 ont été ajoutées à ce recensement lors de l’audit final. Ce recensement n’est pas le registre de l’annexe G : il dépasse de 256 sources les 449 sources distinctes de l’annexe G (version 1.1 dédupliquée), et le présent document ne ventile pas cet écart

**449**

sources distinctes à l’annexe G (449 entrées ordonnées de [1] à [474], 0 doublon après fusion des 25 doublons initiaux et reclassement de la RFC 7515 en [474]), dont 406 de catégorie A, 25 de catégorie B (incluant les 5 entrées Gartner [1, 2, 3, 52, 95] reclassées hors catégorie A) et 18 de catégorie C; une source de catégorie C n’y est citée que comme argument d’éditeur ou comme aide à la lecture, sans valeur d’appui (tableau 66)

*Tableau 67 — Verdicts sur les 427 liens affirmation-source de la recherche documentaire*

| **Verdict** | **Nombre** | **Part** | **Signification** |
| --- | --- | --- | --- |
| Appuyée | 125 | 29 % | La source citée confirme l’affirmation telle qu’écrite. |
| Partiellement appuyée | 214 | 50 % | Le fond est juste, mais un détail (date, chiffre, version, portée) diffère : l’énoncé a été corrigé. |
| Non appuyée | 55 | 13 % | La source ne contient pas l’affirmation : source primaire trouvée ou fait retiré. |
| Contredite | 14 | 3 % | La source ou une source primaire dit le contraire : fait corrigé. |
| Invérifiable | 19 | 4 % | Aucune source crédible trouvée : fait retiré ou présenté comme choix interne du cadre. |

**À RETENIR**

Le fond technique des ébauches était solide, mais plus de sept affirmations sur dix (302 sur 427) exigeaient une correction de détail, une meilleure source ou un retrait. Les erreurs récurrentes : versions de protocoles dépassées, chiffres de marché attribués à la mauvaise firme, obligations légales mal rattachées à un article, allégations commerciales présentées comme des normes et seuils chiffrés sans source.

## F.3 Principales corrections apportées aux ébauches

Le tableau 68 recense les corrections les plus importantes. Les sources indiquées appuient la version retenue.

*Tableau 68 — Principales corrections factuelles*

| **#** | **Affirmation des ébauches** | **Version retenue dans le cadre** |
| --- | --- | --- |
| 1 | MCP 2026-07-28 « impose » OAuth 2.1, norme publiée. | L’autorisation est facultative dans MCP; le cadre la rend obligatoire. OAuth 2.1 reste un Internet-Draft de l’IETF; on exige OAuth 2.0 selon la RFC 9700, aligné sur le profil OAuth 2.1 **[175, 176, 209]**. |
| 2 | Champs `x-enterprise-*` dans les annotations d’un outil MCP. | Hors du schéma (cinq propriétés seulement, dont quatre indices non fiables). Le palier, le seuil d’approbation et la compensation sont inscrits au catalogue d’entreprise (choix du cadre, non prescrit par le schéma MCP) **[201]**. |
| 3 | La passerelle doit supprimer tout champ `_meta`. | La version du protocole et les capacités du client y sont obligatoires, et `traceparent`, `tracestate` et `baggage` y sont réservés au contexte de trace; on conserve ces clés, on filtre les clés non reconnues et on ne fonde aucune autorisation sur `_meta` **[162]**. |
| 4 | Quatre vecteurs d’attaque selon Akamai; rejet 400/403 en cas d’écart d’en-têtes. | L’analyse d’Akamai décrit cinq zones de risque; la concordance en-têtes/corps est déjà exigée par la spécification (HTTP 400, erreur −32020) **[190, 203]**. |
| 5 | MCP exige des jetons liés (mTLS ou DPoP) de 5 à 15 minutes. | MCP utilise des jetons porteurs **[209]**; la liaison à l’expéditeur et la durée courte sont une politique du cadre fondée sur les RFC 8705 **[328]** et 9449 **[213]**. |
| 6 | Carte d’agent à `/.well-known/agent.json`, champs `url` et `authentication`, méthode `tasks/sendSubscribe`. | Formes antérieures à la version 1.0. A2A 1.0 : `agent-card.json`, `supportedInterfaces`, `securitySchemes`, `SendStreamingMessage`, états `TASK_STATE_*` **[68]**. |
| 7 | Spécification A2A « gelée » le 12 mars 2026. | Version 1.0.0 publiée le 12 mars 2026, correctif 1.0.1 le 28 mai 2026 (release GitHub du projet); A2A annoncé comme projet de l’AAIF le 17 août 2026 (billet de la fondation), puis accepté au stade « Growth » (billet du projet du 27 août 2026) **[5, 29, 35, 472]**. |
| 8 | AGNTCY fait partie de la pile de l’AAIF; SLIM est résistant au quantique. | AGNTCY est un projet de la Linux Foundation dont la candidature à l’AAIF est ouverte; la proposition qualifie SLIM de « quantum-safe » sans nommer de suite MLS post-quantique (SLIM met en œuvre MLS, RFC 9420), de sorte que son caractère post-quantique n’est pas démontré **[37, 269]**. |
| 9 | Copilot Studio : MCP en disponibilité générale visée en octobre 2026. | MCP est en disponibilité générale dans Copilot Studio depuis le 29 mai 2025 **[300]**. |
| 10 | Une passerelle ajoute moins de 5 ms; le coupe-circuit confine « en millisecondes ». | Allégations commerciales divergentes (TrueFoundry : « typiquement » moins de 5 ms dans sa FAQ, +7 à +12 ms à son propre banc d’essai); aucun seuil chiffré n’est retenu sans mesure interne (P50/P99, politiques actives) **[143, 144]**. |
| 11 | Délégation limitée à un niveau et sept sous-agents : règles générales. | Contraintes du produit Agentforce; la profondeur maximale de deux niveaux est un choix du cadre **[49]**. |
| 12 | Attribut `gen_ai.agent_version`; opération `handoff`; contenu jamais dans les attributs de span. | Nom exact `gen_ai.agent.version` (ajouté en v1.40.0); aucune valeur `handoff` dans `gen_ai.operation.name` (v1.41.0); contenu en attributs facultatifs (*opt-in*) depuis la version 1.37.0; conventions au niveau « Development », à épingler **[119, 180]**. |
| 13 | Indicateurs d’agent « au format FOCUS ». | FOCUS normalise les données de facturation (version 1.4); aucune de ses colonnes ne porte d’indicateur par agent, que l’organisation calcule par jointure avec sa propre télémétrie **[410, 463]**. |
| 14 | Le traitement exactement une fois de Kafka empêche les doubles paiements. | La garantie vaut entre sujets Kafka; pour tout effet externe, le système cible doit coopérer, par exemple au moyen d’une clé d’idempotence qu’il vérifie **[140]**. |
| 15 | Un bus d’événements réduit la latence de coordination de 70 à 90 %. | Chiffre sans source primaire : retiré; seul l’avantage qualitatif de l’abonnement sur l’interrogation est retenu **[262]**. |
| 16 | Multiagent : +81 % et −70 % (Google), 3 à 10 fois plus de jetons. | Selon le billet de Google, +80,9 % (Finance-Agent), −39 % à −70 % (PlanCraft) et amplification des erreurs de 17,2× sans vérification centrale; la version 3 de l’article (260 configurations) donne une plage de +80,8 % à −70,0 % **[274]**; 3 à 10× par rapport à l’agent unique et environ 15× par rapport à une conversation sont deux mesures distinctes **[17, 273, 275]**. |
| 17 | Firecracker : environ 100 000 lignes, six périphériques virtio. | Environ 50 000 lignes de Rust (2020), quatre types de périphériques émulés (réseau et bloc virtio, port série, contrôleur de clavier i8042 partiel), moins de 5 Mo par microVM, démarrage sous 125 ms, selon l’article de 2020 **[360]**; le site du projet en décrit davantage, les versions récentes ajoutant notamment vsock (section 9.7). |
| 18 | gVisor impose un surcoût d’E/S de 10 à 30 %. | Aucune fourchette publiée; le coût dépend des appels système : mesurer sur la charge réelle **[134]**. |
| 19 | Taux de réussite de 84 % du détournement d’objectif. | Chiffre d’un banc d’essai précis (Agent Security Bench, 84,30 %), cité seulement dans ce contexte **[359]**. |
| 20 | Les identités non humaines dépassent les humaines de 20 contre 1. | Enquête de fournisseur la mieux documentée : 82 identités machines par humain (CyberArk, 2025); chaque organisation mesure son propre ratio **[11]**. |
| 21 | Loi 25 : avis à la CAI en 72 heures (art. 3.2 ou 3.5). | Avis « avec diligence » en cas de risque de préjudice sérieux (art. 3.5 de la Loi sur le privé); registre (art. 3.8) conservé au moins cinq ans selon le règlement; 72 heures n’est qu’une cible interne **[56, 460]**. |
| 22 | Décisions automatisées au secteur public : article 63.1. | Article 65.2 de la Loi sur l’accès **[318]**; l’article 63.1 porte sur les mesures de sécurité **[56]**. |
| 23 | Amendes pénales de 1 000 à 10 000 $ pour une personne; amendes de plus de 500 000 $ déjà prononcées; sanction de 5 000 $ en vertu de la Loi 25. | De 5 000 à 100 000 $ pour une personne physique (art. 91 de la Loi sur le privé); aucune amende de plus de 500 000 $ n’est confirmée; les 5 000 $ visent une décision de la Cour supérieure (art. 342 C.p.c.) sur des citations inventées par l’IA **[458]**. |
| 24 | Article 17 : « analyse d’impact relative au transfert »; protection « équivalente ». | EFVP et entente écrite; critère de protection « adéquate »; « hors Québec » s’entend de tout lieu extérieur au Québec, y compris les autres provinces **[416]**. |
| 25 | Règlement européen : haut risque applicable le 2 août 2026; s’applique dès qu’un agent « touche » des utilisateurs de l’UE. | Échéances reportées par le règlement (UE) 2026/1744 (annexe III : 2 décembre 2027; annexe I : 2 août 2028); critère de l’article 2 : utilisation des sorties dans l’Union **[58, 61]**. |
| 26 | NIST MANAGE 3.1 et 3.2 couvrent le coupe-circuit; MEASURE 2.7 la surveillance des hallucinations. | Coupe-circuit : MANAGE 2.4; déclassement : GOVERN 1.7; MEASURE 2.7 porte sur la sécurité et la résilience; la surveillance en production relève de MEASURE 2.4 **[74]**. |
| 27 | « Seulement 13 % ont la gouvernance adéquate » attribué à McKinsey; 150 000 agents par entreprise attribués à un blogue. | Les deux chiffres proviennent de Gartner (communiqué du 28 avril 2026) **[2]**. |
| 28 | Les dépenses d’IA des entreprises ont bondi de 320 %. | Chiffre sans source, qui semble provenir d’une lecture erronée du facteur 3,2 (environ +220 %) : 37 G$ US en 2025 contre 11,5 G$ US en 2024 (Menlo Ventures, 9 décembre 2025) **[16]**. |
| 29 | Petits modèles 10 à 30 fois moins coûteux (arXiv 2506.02142); Phi-3.5 « 98 % de calcul en moins ». | Référence exacte : arXiv 2506.02153 (coût de calcul, non prix facturé); le « 98 % » est introuvable et retiré **[403, 473]**. |
| 30 | Trois échelles d’autonomie incompatibles (L0–L5, N0–N4, L0–L4) et seuils chiffrés (60 s, 5 min, 1 h). | Échelle unique N0 à N4 et niveau NX interdit, fondée sur Feng et coll., Gartner, AWS et l’IMDA (Infocomm Media Development Authority, Singapour); les seuils deviennent des paramètres internes approuvés par le comité **[75, 76, 83, 95]**. |
| 31 | Saga : un plantage entre la journalisation et l’action ne déclenche aucune compensation. | Une étape à l’état incertain n’est ni compensée ni replanifiée à l’aveugle : l’orchestrateur clôt d’abord l’opération chez le système visé (annulation ou révocation de la clé d’idempotence, de sorte qu’une arrivée tardive soit rejetée) ou l’interroge jusqu’à une issue définitive; à défaut, l’étape passe en réconciliation différée, confiée à une personne (EXIG-ORC-16) **[286]**. |
| 32 | Mémoire à quatre niveaux « inspirée de Tulving ». | Taxonomie à quatre types (travail, épisodique, sémantique, procédurale) issue de CoALA, qui s’inspire de l’architecture Soar et de la psychologie cognitive **[100]**. |

## F.4 Registre des 121 références de la recherche documentaire

Légende des verdicts : ✓ appuyée · ◐ partiellement appuyée · ✗ non appuyée ou contredite · ? invérifiable · — aucune affirmation associée à la référence. La colonne *n* reprend le numéro de la référence dans la recherche documentaire. Décision (version 1.0), à l’état de la version 1.0 : *conservée* = source A ou B admissible, citée si elle figure à l’annexe G; *remplacée* = remplacée par une source primaire, plus récente ou plus spécifique; *retirée* = sans valeur probante pour le cadre ou hors sujet. La colonne « no G » donne le numéro de l’entrée de l’annexe G qui reprend la source, rapprochée par le titre et l’éditeur (le registre ne conserve pas les adresses des pages), ou un tiret si aucune entrée ne la reprend; une entrée de G publiée sous un autre titre n’est pas rapprochée (ainsi la ligne 22 et [275], même éditeur et même sujet). La colonne « Décision à l’audit final » dit si la source y est citée, réintroduite (lignes 7, 16, 36, 41 et 52, remplacées ou retirées à la version 1.0) ou non citée; une source conservée et non citée reste admissible, sans appuyer aucun fait du cadre, et une source citée de catégorie C ne l’est que comme argument d’éditeur (tableau 66). Le symbole ✗ réunit les affirmations non appuyées et contredites, que le tableau 67 distingue globalement (55 et 14) : les relevés de la recherche documentaire ne donnent pas cette répartition référence par référence, de sorte que le registre ne peut pas marquer d’un symbole propre les sources contredites. Pour une page bloquée ou payante, la catégorie repose sur l’éditeur, et le verdict sur le résumé public.

*Tableau 69 — Registre de validation des références de la recherche documentaire*

| **n** | **Source (titre réel, éditeur)** | **Cat.** | **Accès** | **Affirmations** | **Décision (version 1.0)** | **no G** | **Décision à l’audit final** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Enterprise Agentic AI Architecture Design Guidance (Part 1) Architecture & Governance Magazine | **B** | accessible | ✓5 ◐10 ✗3 | conservée | — | non citée |
| 2 | Enterprise Agentic AI Reference Architecture (2026) Triotech Systems | **C** | accessible | ✓2 ◐2 | retirée | — | non citée |
| 3 | A Framework for Architecting Agent Control Plane MuleSoft | **B** | accessible | ✓3 ◐3 ✗3 | conservée | [45] | citée comme argument d’éditeur (catégorie C) |
| 4 | Microsoft Copilot Studio vs. Salesforce Agentforce: Which AI Agent Platform is Better for Enterprises? Artic Consulting | **C** | accessible | ◐4 | remplacée | — | non citée |
| 5 | Agentic AI Architecture Framework for Enterprises: The Complete 2026 Design and Governance Guide NextAgile | **C** | accessible | ◐4 ✗1 ?9 | remplacée | — | non citée |
| 6 | AI FinOps Explained: AI Cost Optimization Guide for 2026 AvePoint | **C** | accessible | ✓1 ◐5 ✗2 | remplacée | — | non citée |
| 7 | Governing AI Agents Across Multiple Platforms TrueFoundry | **B** | accessible | ✓2 ◐8 ✗3 | remplacée | [44] | réintroduite comme argument d’éditeur (catégorie C) |
| 8 | Designing agentgateway: A Unified High-Performance Gateway for AI and API Traffic agentgateway.dev | **A** | accessible | ✓1 ◐2 | conservée | [142] | citée |
| 9 | Agent Communication Protocol (ACP) Explained: What It Is and Why It Matters Boldare | **C** | accessible | ✓1 ◐6 | remplacée | — | non citée |
| 10 | What the Linux Foundation and AAIF Mean for MCP and Agentic AI Blck Alpaca | **C** | accessible | ✓1 ◐3 ✗2 | remplacée | — | non citée |
| 11 | The next generation of MCP Cloudflare | **B** | accessible | ✓12 ◐6 ✗2 | remplacée | — | non citée |
| 12 | Specification - Model Context Protocol (MCP) ModelContextProtocol.Info | **C** | accessible | ✓1 | remplacée | — | non citée |
| 13 | Architecture overview (documentation MCP, révision 2026-07-28) Model Context Protocol | **A** | accessible | ✓5 ◐1 | conservée | [63] | citée |
| 14 | #17: What is A2A and why is it – still! – underappreciated? Turing Post | **B** | accessible | ✓2 ◐1 | remplacée | — | non citée |
| 15 | All About the A2A Protocol, Now Part of the Agentic AI Foundation rohitghumare.com | **C** | accessible | ✓10 ◐6 ✗3 ?1 | remplacée | — | non citée |
| 16 | [Project Proposal] AGNTCY #57 (dépôt aaif/project-proposals) GitHub | **A** | accessible | ✓5 ◐6 | remplacée | [37] | réintroduite |
| 17 | AGNTCY: the open standard set to structure the Internet of Agents Splunk | **B** | accessible | ✓2 ◐2 | remplacée | — | non citée |
| 18 | Autonomous Agentic Event-Driven Systems Architecture Confluent | **A** | accessible | ✓4 ◐6 | conservée | [262] | citée comme argument d’éditeur (catégorie C) |
| 19 | Event-Driven Architecture for AI Agents (Patterns and Benefits) Atlan | **C** | accessible | ◐3 | remplacée | — | non citée |
| 20 | The 6 Levels of AI Autonomy (2026): A Practical Framework Agentys | **C** | accessible | ◐8 ✗10 | remplacée | — | non citée |
| 21 | AI Agent Risk Assessment: What Organizations Need to Evaluate Global AI Certification Council | **C** | accessible | ✓2 ◐5 ✗4 | remplacée | — | non citée |
| 22 | When to use multi-agent systems (and when not to) Anthropic | **A** | accessible | ✓6 ◐8 ✗1 | conservée | — | non citée |
| 23 | Single-Agent vs Multi-Agent AI: When to Scale Your Dev Workflow Augment Code | **C** | accessible | ✓1 | remplacée | — | non citée |
| 24 | The Saga Pattern for Multi-Agent Transactions: Compensating Actions RedLineSoft | **C** | accessible | ✓11 ◐2 ✗1 | remplacée | — | non citée |
| 25 | AI Agent Orchestration Frameworks: A 2026 Guide Levelop | **C** | accessible | ✓2 ◐8 ✗2 | remplacée | — | non citée |
| 26 | OWASP Top 10 for Agentic Applications (2026) — fiche de cadre Modulos (MFF-14) Modulos AG | **B** | accessible | ✓7 ◐5 ✗2 | remplacée | — | non citée |
| 27 | Authentication for AI Agents: OAuth Patterns for Non-Human Identity guptadeepak.com | **B** | accessible | ✓2 ◐6 ✗2 | remplacée | — | non citée |
| 28 | ISO 42001 vs NIST AI RMF: Which Do You Need in 2026? Fruggr | **C** | accessible | ◐3 | remplacée | — | non citée |
| 29 | How to sandbox AI agents in 2026: MicroVMs, gVisor & isolation strategies Northflank | **B** | accessible | ✓1 ◐5 ✗1 | remplacée | — | non citée |
| 30 | Conformité à l’IA et à la Loi 25 du Québec : le guide complet 2026 Augure | **C** | accessible | ◐11 ✗9 ?1 | remplacée | — | non citée |
| 31 | Enterprise Architecture 2030: Navigating Agentic AI Scenarios Gartner | **B** | payante | ✓1 | conservée | — | non citée (reclassée B hors catégorie A) |
| 32 | The best AI agent frameworks in 2026 LangChain | **B** | accessible | ◐4 ✗2 | remplacée | — | non citée |
| 33 | Best Agentic AI Platforms for Enterprise Operations (2026 Guide) Shadow Inc. | **C** | accessible | ✓1 ◐1 ✗2 | remplacée | — | non citée |
| 34 | Multi-Agent AI News - Week of May 19-25, 2026 - Enterprise Orchestration Platforms Suprmind | **C** | accessible | ◐2 ✗1 ?1 | remplacée | — | non citée |
| 35 | Agentic Integration with SAP, ServiceNow, and Salesforce Microsoft Community Hub | **B** | accessible | — | retirée | — | non citée |
| 36 | Implement 3 Layers of Oversight for Scaled Agentic AI Architectures (titre non vérifié) Gartner | **B** | bloquée | ?1 | retirée | [52] | réintroduite (reclassée B hors catégorie A) |
| 37 | AI Agent Sandbox: How to Safely Run Autonomous Agents in 2026 Firecrawl | **B** | accessible | ✓3 ◐1 | conservée | — | non citée |
| 38 | MCP (Model Context Protocol) in 2026: the complete guide for engineering teams Jacar Systems | **C** | accessible | ✓2 ◐3 ✗1 | remplacée | — | non citée |
| 39 | Multi-Agent Orchestration Patterns: A Production Guide (2026) explainx.ai | **C** | accessible | ✓2 ◐5 ✗1 | remplacée | — | non citée |
| 40 | Agentforce Interoperability Guide (The Architect’s Guide to Agentforce Interoperability) Salesforce | **A** | accessible | ◐2 | conservée | [49] | citée |
| 41 | Levels of Autonomy for AI Agents arXiv | **A** | bloquée | ✓1 | remplacée | [83] | réintroduite |
| 42 | The Five Working Levels of AI Agent Autonomy, and How to Choose Among Them The Inteq Group | **C** | accessible | ✓1 ◐1 | remplacée | — | non citée |
| 43 | Building Blocks (TOGAF 9.1, Partie IV, chapitre 37) QualiWare Center of Excellence | **B** | accessible | ◐1 | remplacée | — | non citée |
| 44 | Architecture Building Blocks (ABBs) vs Solution Building Blocks (SBBs) Boldo | **C** | accessible | — | remplacée | — | non citée |
| 45 | SAP Enterprise Architects’ Guide: Using TOGAF® ABBs and SBBs to Deliver Successful SAP S/4HANA Implementations Insight Arc | **C** | accessible | — | retirée | — | non citée |
| 46 | Ambient Agents and the New Agent Inbox ft. Harrison Chase Inference by Sequoia | **B** | accessible | ◐7 | remplacée | — | non citée |
| 47 | Introducing ambient agents LangChain | **A** | accessible | ✓2 ◐2 | conservée | [86] | citée |
| 48 | Confluent: The Real-Time Backbone for Agentic Systems Confluent | **A** | accessible | ◐2 | conservée | — | non citée |
| 49 | Best Code Execution Sandboxes for AI Agents in 2026 E2B | **A** | accessible | ✓1 | conservée | — | non citée |
| 50 | MCP Is Growing Up: The 2026 Roadmap Takes Shape Obot AI | **B** | accessible | ✓1 ◐1 | remplacée | — | non citée |
| 51 | 5 Best Code Execution Sandboxes for AI Agents Blaxel | **C** | accessible | — | retirée | — | non citée |
| 52 | TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems arXiv | **A** | accessible | ◐1 | remplacée | [454] | réintroduite |
| 53 | AI Agent Protocols: MCP, A2A, ACP, and the Interop Stack AIPrompt20 | **C** | accessible | ✓1 | remplacée | — | non citée |
| 54 | The AI Agent Memory Architecture Deep Dive: Building Agents That Remember Across Sessions, Devices, and Tools AI Magicx | **C** | accessible | ✓1 ◐4 ✗1 | remplacée | — | non citée |
| 55 | GraphRAG, AI Agents, and Memory: How Graph Databases Power the Next Wave of AI in 2026 FalkorDB | **B** | accessible | ◐3 | remplacée | — | non citée |
| 56 | Agent Memory Architectures: Vector vs Graph vs Episodic Digital Applied | **C** | accessible | — | retirée | — | non citée |
| 57 | New in Confluent Intelligence: A2A, Multivariate Anomaly Detection, Vector Search for Cosmos DB, Amazon S3 Vectors, and More Confluent | **A** | accessible | ◐1 | conservée | — | non citée |
| 58 | Cheap Tokens, Expensive Agents: The 2026 Inference Economics Reckoning Socradata | **C** | accessible | ◐2 ✗1 ?1 | remplacée | — | non citée |
| 59 | OpenTelemetry GenAI Semantic Conventions: A Practical Guide OpenObserve | **C** | accessible | ◐4 ✗3 | remplacée | — | non citée |
| 60 | Agent Memory Systems: How AI Agents Remember, Learn, and Stay Coherent Across Time Tresslers Group | **C** | accessible | ◐1 | remplacée | — | non citée |
| 61 | Avoid Governance Mismatch: Classify AI Agents by Autonomy Level Gartner | **B** | bloquée | ✓1 ◐1 | conservée | — | non citée (reclassée B hors catégorie A) |
| 62 | From autonomous cars to autonomous agents: the five levels of AI agent autonomy (titre non confirmé) MIT Media Lab | **B** | bloquée | ?3 | remplacée | — | non citée |
| 63 | The 5 Levels of Agentic AI (And Why Most Businesses Need Less Autonomy Than They Think) (titre non confirmé) Medium | **C** | bloquée | — | retirée | — | non citée |
| 64 | The 5 Levels of AI Agent Autonomy: From Copilot to Fully Autonomous (And Where to Start) Pickaxe | **C** | accessible | ◐1 | remplacée | — | non citée |
| 65 | The Six Levels of Agentic Behavior Vellum | **C** | accessible | — | retirée | — | non citée |
| 66 | The Top Agentic AI Security Threats You Need to Know in 2026 Lasso Security | **B** | accessible | ◐1 | remplacée | — | non citée |
| 67 | Ambient agents explained: Applications, architecture, and building with ZBrain ZBrain | **C** | accessible | — | retirée | — | non citée |
| 68 | LIVE: Ambient Agents and the New Agent Inbox ft. Harrison Chase Sequoia Capital | **B** | accessible | ✓2 | conservée | — | non citée |
| 69 | UX for Agents, Part 2: Ambient LangChain | **B** | accessible | — | conservée | — | non citée |
| 70 | Why Google’s Agent2Agent Protocol Needs Apache Kafka Medium | **B** | bloquée | — | remplacée | — | non citée |
| 71 | MCP (Model Context Protocol) for Business: The USB-C of AI Agents and Why It Changes Your Stack in 2026 NAXIA | **C** | accessible | — | retirée | — | non citée |
| 72 | The New MCP Specification: What Security Teams Must Prepare For Akamai Security Research | **B** | accessible | ✓4 ◐3 | conservée | [203] | citée |
| 73 | Agent Card Explained: A2A Protocol, JSON & Use Cases AI Growth Agent | **C** | accessible | ✓2 ◐2 ✗1 | remplacée | — | non citée |
| 74 | Agent communication protocols: A2A vs ACP vs MCP (2026) crystl | **C** | accessible | — | retirée | — | non citée |
| 75 | What’s New in A2A Protocol v1.0 A2A Project | **A** | accessible | — | conservée | [235] | citée |
| 76 | A2A v1.0: a builder’s guide, part 2 - migration, security, and production Agentic AI Foundation | **A** | accessible | — | conservée | [242] | citée |
| 77 | A2A Agent Card: Structure, Discovery, and Signing Agent2Agent.Info | **C** | redirigée | ✓1 | remplacée | — | non citée |
| 78 | A2A v1.0 Agent Card Specification Explorer A2A Registry | **C** | accessible | — | remplacée | — | non citée |
| 79 | AGNTCY Documentation AGNTCY | **A** | accessible | — | conservée | [182] | citée |
| 80 | Beyond Context Sharing: A Unified Agent Communication Protocol (ACP) for Secure, Federated, and Autonomous Agent-to-Agent (A2A) Orchestration arXiv | **A** | accessible | — | retirée | — | non citée |
| 81 | Four Design Patterns for Event-Driven, Multi-Agent Systems Confluent | **A** | accessible | ✓1 ◐1 | conservée | — | non citée |
| 82 | MCP vs. REST/HTTP API vs. Kafka: The Architect’s Guide to Agentic AI Integration kai-waehner.de | **B** | accessible | ✓2 ◐5 ✗1 | conservée | [167] | citée |
| 83 | Building effective agents Anthropic | **A** | accessible | ◐1 | conservée | [6] | citée |
| 84 | Single Agent vs Multi-Agent: When to Build a Multi-Agent System (titre non confirmé : page inaccessible) Towards Data Science | **B** | bloquée | — | remplacée | — | non citée |
| 85 | How to Decide When to Use a Single Agent vs a Multi-Agent Team MindStudio | **C** | accessible | ✓1 | remplacée | — | non citée |
| 86 | Multi-Agent AI Orchestration: A CTO’s 2026 Guide KGT Solutions | **C** | accessible | ✓1 ?1 | remplacée | — | non citée |
| 87 | Top Agent Frameworks To Use in 2026: A Comparison Splunk | **C** | accessible | ✓2 ◐2 | remplacée | — | non citée |
| 88 | How and when to build multi-agent systems LangChain | **B** | accessible | — | conservée | [277] | citée comme argument d’éditeur (catégorie C) |
| 89 | Top 9 AI Agent Frameworks in 2026 (titre de la bibliographie; page non lue) Medium | **C** | bloquée | — | retirée | — | non citée |
| 90 | Conformité Loi 25 – Microsoft, hébergé au Canada (io4 Technologies) io4 Technologies | **C** | accessible | ✓1 ◐1 | remplacée | — | non citée |
| 91 | Salesforce Agentforce vs Microsoft Copilot Studio: 2026 Comparison Smartbridge LLC | **C** | accessible | — | retirée | — | non citée |
| 92 | AI Agent Memory Architectures: From Context Windows to Persistent Knowledge Zylos Research | **C** | accessible | — | retirée | — | non citée |
| 93 | Memory Systems for AI Agents: Practical Implementations (2025-2026) GitHub Gist | **C** | accessible | — | retirée | — | non citée |
| 94 | SYNAPSE: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation arXiv | **A** | accessible | — | conservée | — | non citée |
| 95 | Architecture – Solo Enterprise for agentgateway docs Solo.io | **A** | accessible | — | remplacée | — | non citée |
| 96 | OAuth 2.0 Token Exchange: When One Token Isn’t the Token You Need (titre non confirmé) Medium | **C** | bloquée | ?1 | remplacée | — | non citée |
| 97 | OAuth’s On-Behalf-Of flow for AI agents WorkOS | **B** | accessible | ◐2 | remplacée | — | non citée |
| 98 | OAuth 2.0 Extension: On-Behalf-Of User Authorization for AI Agents (brouillon −01) IETF | **A** | accessible | ◐1 | remplacée | — | non citée; révision −02 citée ([335]) |
| 99 | On-Behalf-Of Token Exchange Auth0 | **A** | accessible | — | conservée | — | non citée |
| 100 | OAuth 2.0 Extension: On-Behalf-Of User Authorization for AI Agents (brouillon −00) IETF | **A** | accessible | ◐1 | remplacée | — | non citée; révision −02 citée ([335]) |
| 101 | AI Agent Code Execution Sandboxes: Isolation from Containers to MicroVMs (titre non confirmé) Medium | **C** | bloquée | — | remplacée | — | non citée |
| 102 | OWASP Top 10 for Agentic Applications 2026: Key Takeaways & How to Take Action Teleport | **B** | accessible | — | remplacée | — | non citée |
| 103 | OWASP Non-Human Identities Top 10 OWASP Foundation | **A** | accessible | — | conservée | [91] | citée |
| 104 | OWASP Agentic Skills Top 10 OWASP Foundation | **A** | accessible | — | conservée | [350] | citée |
| 105 | OWASP GenAI Security Project Releases Top 10 Risks and Mitigations for Agentic AI Security OWASP GenAI Security Project | **A** | accessible | — | conservée | — | non citée |
| 106 | AI TRiSM: Understanding Gartner’s View on Agentic AI Trust Sweet Security | **C** | accessible | ◐1 ✗1 | remplacée | — | non citée |
| 107 | OpenTelemetry GenAI Semantic Conventions: What’s Stable Praesidia | **C** | accessible | — | remplacée | — | non citée |
| 108 | Semantic Conventions for GenAI agent and framework spans OpenTelemetry | **A** | accessible | — | conservée | [120] | citée |
| 109 | Loi 25 et IA au Québec : guide PME 2026 (« Loi 25 et IA. Les gestes qui comptent. ») Margence inc. | **C** | accessible | ◐1 | remplacée | — | non citée |
| 110 | Conseil et formation IA — conformité Loi 25 et IA responsable au Québec \| DictIA DictIA Inc. | **C** | accessible | ✓1 ✗2 | remplacée | — | non citée |
| 111 | Principaux changements aux lois sur la protection des renseignements personnels Commission d’accès à l’information du Québec | **A** | accessible | — | conservée | [7] | citée |
| 112 | Décisions automatisées et Loi 25 : préparer l’information et la révision humaine extensio.ai | **C** | accessible | ◐1 | remplacée | — | non citée |
| 113 | Mesures applicables lors de l’utilisation de l’intelligence artificielle générative (indication d’application IA-RI-2025-003-OP) Gouvernement du Québec | **A** | accessible | — | conservée | [421] | citée |
| 114 | AI Governance in 2026: A Practical Framework for NIST AI RMF, EU AI Act, and ISO 42001 Enterprise Architecture Blog | **C** | accessible | — | remplacée | — | non citée |
| 115 | NIST AI RMF Continuous Monitoring 2026 Bitsight | **C** | bloquée | — | remplacée | — | non citée |
| 116 | NIST AI RMF: 8-Step Implementation Guide NeuralTrust | **C** | accessible | — | remplacée | — | non citée |
| 117 | A Guide to AI TRiSM: Trust, Risk, and Security Management Palo Alto Networks | **B** | accessible | — | conservée | — | non citée |
| 118 | NIST AI RMF Implementation: A Clear 8-Step Plan for 2026 Governance Docs LLC | **C** | accessible | — | remplacée | — | non citée |
| 119 | AI FinOps Became a Real Discipline in 2026. Here’s What It Requires. Larridin | **C** | accessible | — | retirée | — | non citée |
| 120 | AI FinOps 2026: The Definitive Guide to Costs and Value Compresr | **C** | accessible | ◐2 ✗1 | remplacée | — | non citée |
| 121 | FinOps for AI: How to Control LLM Token Spend Before It Controls Your Budget Varcio | **C** | accessible | — | remplacée | — | non citée |
