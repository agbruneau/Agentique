# Annexe D — Glossaire bilingue

| Champ | Valeur |
|---|---|
| Statut | Amorcé en P1 (16 juillet 2026), enrichi à chaque chapitre rédigé, **relu adversarialement et corrigé le 17 juillet 2026** |
| Date de gel de l'information | **17 juillet 2026** |
| Socle mobilisé (PRD §7) | F-01, F-02, F-04, F-05, F-07 à F-09, F-11, F-15, F-16, F-24, F-25, **F-26**, F-27 à F-29, F-35, F-36, F-37, F-40, F-42, F-43, F-46, F-48 — **24 entrées**, recomptées mécaniquement le 17 juill. 2026. *(L'en-tête portait « 23 entrées » et omettait F-26, que l'entrée « adaptativité après déploiement » cite trois fois : l'ajout du 17 juillet n'avait été répercuté ni sur la liste, ni sur le cardinal, ni sur la date de gel — trois manquements à CA-1 et CA-4 dans l'en-tête du fichier qui fait autorité sur la terminologie.)* |
| Garde-fous à surveiller (PRD §8) | **R-1 à R-8 — les huit**, recensés le 17 juill. 2026. *(Deux recensements successifs, tous deux faux : l'en-tête ne déclarait d'abord que R-1 et R-8 ; corrigé en « R-1 à R-5, R-7, R-8 » — **sept** —, il omettait **R-6**, que §D.7 porte depuis le 17 juillet. L'audit du même jour l'a relevé (m-43) : c'est la classe d'erreur exacte que cet en-tête raconte à propos de F-26 deux lignes plus haut — une ligne ajoutée au corps sans répercussion sur la liste ni sur le cardinal. Un en-tête ne se recense pas de mémoire ; il se recompte contre le corps.)* Réserves du socle : F-01, F-24, F-25, F-29. **CA-2** (§D.7 en est l'instrument), **CA-5** (bilinguisme terminologique) |
| Volumétrie cible | ~1500 mots |

> **Rôle (PRDPlan §7)** : glossaire **unique** du projet, alimenté dès P1 pour prévenir l'incohérence terminologique entre chapitres. **La terminologie de la Partie II fait référence** : tout chapitre ultérieur qui emploie un terme d'orchestration reprend la forme fixée ici.

**Convention (CA-5)** : terme français retenu, terme anglais entre parenthèses et en italique à la première occurrence de chaque chapitre. Les termes ci-dessous portent leur entrée de socle : un terme sans trace F-xx n'entre pas au glossaire.

---

## D.1 Avertissement terminologique — les quatre emplois de « (agentic) control plane » / « ACP » (R-8)

Le socle contient une collision de vocabulaire à **quatre branches** (trois détectées en P0, la quatrième à la rédaction du ch. 1 — 16 juillet 2026). Elle est la principale source d'erreur terminologique de l'ouvrage et doit être désamorcée à la première occurrence de chaque branche. **La désambiguïsation est posée au ch. 1 §1.2**, qui porte la première occurrence réelle du sigle dans l'ouvrage.

| Forme dans les sources | Ce que c'est | Socle | Forme imposée dans la monographie |
|---|---|---|---|
| **ACP** — *Agent Communication Protocol* | Protocole lancé par IBM Research avec la plateforme BeeAI (17 mars 2025), **fusionné dans A2A le 29 août 2025** ; développement actif arrêté | F-43 ; **R-1**. **L'intitulé développé — *Agent Communication Protocol* — est versé au socle le 17 juill. 2026 : F-43, niveau [B]** (consultation directe du blog primaire que l'entrée citait déjà — research.ibm.com/blog/agent-communication-protocol-ai, Kim Martineau, 28 mai 2025 —, sans vote adversarial). *Il en était **absent** jusque-là, alors que la forme imposée ci-contre le prescrivait à huit chapitres et à l'annexe C : la case qui **fait autorité** sur R-8 exigeait un élément que le socle n'établissait pas, là où le projet refuse ce geste ailleurs (« aucune traduction à inventer », §10.9). Relevé par l'audit du 17 juill. 2026 (m-44) et **élevé plutôt que retiré** — la source primaire était déjà au dossier, il suffisait de la lire. La forme imposée est donc **inchangée** ; ce qui change est qu'elle est désormais **tracée**.* | « l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI) » — **toujours au passé**, jamais présenté comme standard vivant |
| **ACP** — *Agentic Control Plane* | Programme phare du consortium Lightworks–Scotiabank–Sun Life–TELUS, annoncé le 7 juillet 2026, déclaré en production en environnement réglementé | F-48 ; **R-8** | « l'*Agentic Control Plane* du consortium » — **jamais abrégé en « ACP » sans qualificatif**. *(La clause « et jamais dans un chapitre traitant des protocoles » est retirée le 17 juill. 2026 : elle n'était nulle part au socle et **contredisait R-8**, qui prescrit le rappel de la désambiguïsation au ch. 3 — un chapitre de protocoles, qui ne peut la rappeler sans nommer cette branche.)* |
| *agentic control plane* (minuscules) | **Positionnement marketing** de watsonx Orchestrate depuis Think 2026 (5 mai 2026) — une expression descriptive d'IBM sur son produit, pas un nom de produit ni un protocole | F-42 | « le positionnement d'IBM comme *agentic control plane* » — **attribué à IBM à chaque occurrence** (§8.2), en minuscules, jamais abrégé |
| **composante ACP** d'AGNTCY | Composante du projet AGNTCY dont des **analyses tierces** relèvent un chevauchement avec A2A. **Le socle n'établit ni son intitulé complet, ni son identité ou sa non-identité avec (a)** — lacune PRD §10.7 | F-05 ; **R-8 (d)** | « la composante ACP d'AGNTCY » — toujours qualifié ; **ne jamais l'agréger à (a) ni l'en distinguer comme un fait** : le socle ne permet ni l'un ni l'autre. Le chevauchement est une analyse tierce, attribuée comme telle |

**Règle de rédaction (R-8)** : ces quatre objets ne sont **pas établis comme liés**. Il faut cependant dire exactement ce que le socle établit, car les quatre branches ne sont pas au même statut, et c'est ici qu'une commodité de rédaction se transformerait en fait fabriqué :

- **(a) et (b) : absence de lien établie.** F-48 porte le fait négatif en toutes lettres — cet « ACP » du consortium « n'a aucun lien avec l'ACP protocolaire d'IBM Research/BeeAI fusionné dans A2A [...] pure homonymie ». C'est le **seul** couple sur lequel le socle se prononce.
- **(c) vis-à-vis de (a) et de (b) : objet distinct, sans plus.** R-8 dit « objets distincts » ; **aucune source, aucun balayage**. Écrire que (a) et (c) seraient « sans aucun rapport » serait un **fait négatif fabriqué** — et sur le couple précisément où il ne va pas de soi, (a) et (c) étant **tous deux des objets d'IBM** (l'ACP d'IBM Research d'un côté, le positionnement d'IBM sur watsonx Orchestrate de l'autre). Le socle ne documente ni lien ni absence de lien : c'est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié (PRDPlan §4.4).
- **(d) : identité ouverte.** Ni établie, ni exclue (lacune PRD §10.7).

*Correctif du 17 juillet 2026, sur relecture adversariale : la présente règle énonçait « (a), (b) et (c) sont sans aucun rapport ». La faute est de la classe que §4.4 nomme — confondre l'absence de documentation et le fait négatif vérifié —, commise dans la section qui **fait autorité** sur R-8. Elle avait déjà essaimé : le ch. 1 §1.2 écrivait « le socle **atteste** trois emplois sans rapport entre eux », corrigé au même commit. Un glossaire qui fait autorité fabrique en aval tout ce qu'il affirme de trop.*

Le sigle « ACP » employé seul est **proscrit dans tout l'ouvrage** ; chaque emploi porte son qualificatif complet. La désambiguïsation est posée explicitement au **ch. 1 §1.2** (première occurrence du sigle dans l'ouvrage), rappelée au **ch. 3** (généalogie complète d'ACP → A2A), au **ch. 17 §17.8** (consortium) et au **ch. 22 §22.2** (positionnement IBM).

---

## D.2 Orchestration et autonomie *(terminologie de référence — Partie II)*

| Français | Anglais | Définition (source) |
|---|---|---|
| **Autonomie encadrée** | *framed autonomy* | Mécanisme premier de gouvernance des systèmes agentiques : l'agent dispose d'une latitude de décision bornée par un *frame* explicite. **Titre et thèse centrale de l'ouvrage.** (F-36) |
| *Frame* **normatif** | *normative frame* | Cadre déontique : obligations, permissions, interdictions. Distinct du frame opérationnel. (F-36) |
| *Frame* **opérationnel** | *operational frame* | ⚠ **Caractérisation non portée par le socle — lacune PRD §10.10.** F-36 pose le terme et l'oppose au *frame* normatif ; **seul le frame normatif est caractérisé**. Employer le terme comme F-36 le pose — le pendant opérationnel du frame normatif — **sans en définir le contenu** : aucune source du socle ne dit ce qu'un frame opérationnel comprend. *(La présente entrée portait « Cadre d'exécution : ce que l'agent peut faire, dans quel ordre, avec quels outils », sous trace F-36 — définition plausible que F-36 ne porte pas. Retirée le 17 juill. 2026 sur relecture adversariale. L'articulation des deux frames étant la thèse de l'ouvrage, la lacune est d'autant plus à dire.)* (F-36 ; §10.10) |
| **Système APM** | *APM system, Agentic Business Process Management* | Système sociotechnique d'agents au moins partiellement conscients du processus. (F-36) |
| **Autonomie ≠ automatisation** | *autonomy vs. automation* | Distinction fondatrice posée par le manifeste APM. ⚠ **Lecture de l'auteur** : « automatiser, c'est fixer le comportement ; rendre autonome, c'est déléguer la décision » est une **formule de l'auteur**, non du socle — F-36 **pose la distinction** et la déclare fondatrice, il ne la formule pas ainsi. La formule est retenue parce qu'elle est utile, et marquée parce qu'elle est de l'auteur. *(Marquage ajouté le 17 juill. 2026 sur audit — obs. 28.)* (F-36) |
| **Adaptation** / **évolution** | *adaptation* / *evolution* | Auto-modification éphémère d'une instance (adaptation) vs modification persistante du modèle de processus (évolution). (F-36) |
| **Écart de responsabilité** | *responsibility gap* | Défi C4 du manifeste APM : indétermination de l'imputabilité juridique entre développeur, organisation qui impose le frame, fournisseur de modèle et comportement émergent. **Pivot du ch. 13.** (F-36) |
| **Options d'orchestration OO1–OO4** | *orchestration options* | OO1 : orchestration agentique agnostique au processus ; OO2 : agentique consciente d'un cadre ; OO3 : orchestration de processus invoquant des agents agnostiques ; OO4 : orchestration explicite d'agents conscients du processus. (F-37) |
| **Assurance de correction** | *correctness assurance* | L'une des **cinq propriétés** d'évaluation d'une orchestration listées par F-37 (avec autonomie, spécificité, réactivité, traçabilité/tractabilité). ⚠ Le socle **la liste sans la définir** : ne pas lui prêter de critère de satisfaction. *(Portait « garantie que le résultat est conforme » — glose d'auteur ; retirée le 17 juill. 2026.)* (F-37) |
| **Traçabilité / tractabilité** | *traceability / tractability* | L'une des **cinq propriétés** d'évaluation d'une orchestration listées par F-37 (avec autonomie, spécificité, réactivité, assurance de correction). ⚠ **Lecture de l'auteur** : « capacité à reconstituer et à suivre l'exécution » est une glose — F-37 **liste la propriété sans la définir**, et ne dit pas ce qui distingue la traçabilité de la tractabilité, que cette glose recouvre d'une seule formule. Même statut que l'**assurance de correction** ci-dessus. **Enseignement F-37, lui porté au socle : la journalisation confiée aux agents n'est généralement pas recommandée.** *(Marquage ajouté le 17 juill. 2026 sur audit — obs. 28.)* (F-37) |
| **Humain-dans-la-boucle** | *human-in-the-loop* | Point d'arrêt exigeant une intervention humaine. À ne pas confondre avec la révision humaine *a posteriori* de l'art. 12.1 (F-27). (F-15) |
| **Point de contrôle** | *checkpointing* | Persistance de l'état d'un workflow agentique permettant la reprise. F-15 **nomme** le patron parmi les capacités d'orchestration du Microsoft Agent Framework, sans le caractériser ; la glose ci-dessus est bornée au sens propre du terme. *(Portait « permettant reprise **et inspection** » : l'inspection n'est ni dans le terme, ni dans F-15 — c'était prêter au socle une propriété d'auditabilité, sur le terrain même de la thèse de l'ouvrage. Membre retiré le 17 juill. 2026 sur audit — obs. 28.)* (F-15) |

---

## D.3 Protocoles

| Français | Anglais | Définition (source) |
|---|---|---|
| **MCP** | *Model Context Protocol* | Interface client-serveur JSON-RPC 2.0 pour l'invocation d'outils et l'échange de données typées ; **cadre d'autorisation** fondé sur OAuth. Révision de spécification 2025-11-25. **Dire « cadre d'autorisation », jamais « sécurisé ».** (F-01) |
| **A2A** | *Agent2Agent* | Protocole de délégation de tâches pair-à-pair entre agents ; v1.0 que **le projet A2A** qualifie de première spécification stable. **Doctrine du projet A2A** : « MCP dans les agents, A2A entre les agents » — ⚠ **le socle ne documente aucun endossement conjoint par le projet MCP** (F-16). *Corrigé le 17 juill. 2026 : l'entrée portait « v1.0 = première spécification stable » et « Doctrine officielle », deux auto-déclarations données pour des faits — dans le fichier qui fixe les formes, alors que les ch. 2 et 18 et l'annexe B attribuent tous correctement. « Doctrine officielle » sans sujet invite exactement la lecture que le socle interdit : un endossement conjoint des deux projets.* (F-02, F-16) |
| **Carte d'agent** (signée) | *(Signed) Agent Card* | Descripteur d'agent A2A ; la variante signée porte une vérification cryptographique d'identité. (F-02) |
| **AP2** | *Agent Payments Protocol* | Protocole compagnon d'A2A pour les transactions pilotées par agents. **Endossement déclaré ≠ adoption en production.** (F-04) |
| **AGNTCY** | — | Couche d'infrastructure (annuaires de découverte, transport SLIM), interopérable avec A2A et MCP — positionnement officiel non concurrent. (F-05) |
| **Empoisonnement d'outils** | *tool poisoning* | ⚠ **Risque nommé par le socle, mécanique non portée — lacune PRD §10.8.** F-01 le **nomme** parmi les risques attachés à MCP ; le socle ne verse aucune source primaire consacrée à sa mécanique, aucun identifiant de vulnérabilité, aucun incident public daté, et **ne le date pas**. Employer le terme, ne pas en expliquer le fonctionnement. *(Portait « Détournement d'un outil exposé à un agent » — glose d'auteur sous trace F-01 ; retirée le 17 juill. 2026.)* (F-01 ; §10.8) |
| **Injection d'invites** | *prompt injection* | ⚠ **Risque nommé, mécanique non portée — lacune PRD §10.8.** Même statut que l'empoisonnement d'outils : F-01 et F-36 (défi C2) le **nomment**, sans mécanique ni datation au socle. *(Glose d'auteur retirée le 17 juill. 2026.)* (F-01 ; F-36 défi C2 ; §10.8) |
| **Empoisonnement de mémoire** | *memory poisoning* | ⚠ **Risque nommé, mécanique non portée — lacune PRD §10.8.** F-36 (défi C2) le **nomme**, avec les patrons *Action-Selector* et *Plan-Then-Execute* ; aucune caractérisation au socle. *(Glose d'auteur retirée le 17 juill. 2026.)* (F-36 défi C2 ; §10.8) |

---

## D.4 Identité et registres

| Français | Anglais | Définition (source) |
|---|---|---|
| **Identité d'agent** | *agent identity* | Identité propre attribuée à un agent, distincte de celle d'un utilisateur. Entra Agent ID repose sur OAuth 2.0 et OIDC. **Ne pas parler de « registre centralisé » (R-2).** (F-07) |
| **Registre d'agents** | *agent registry* | Inventaire d'entreprise faisant autorité (découverte, cycle de vie, conformité). Spécification CSA = **brouillon de labs**, pas une norme ratifiée (§8.2.5). (F-08) |
| `toolAccessList` | — | Champ obligatoire du profil CSA : liste explicite des outils et serveurs MCP autorisés. (F-08) |
| `permissionBoundaries` | — | Champ obligatoire du profil CSA : bornes de moindre privilège. (F-08) |
| **SCIM** | *System for Cross-domain Identity Management* | RFC 7643 ; ancrage du profil d'agent CSA via une extension (brouillon IETF expiré le 19 avril 2026). **La spec s'appuie sur SPIFFE/SPIRE ; elle ne l'impose pas (R-3).** (F-08) |

---

## D.5 Réglementation canadienne

| Français | Anglais | Définition (source) |
|---|---|---|
| **Risque de modèle** | *model risk* | Objet de la ligne directrice E-23 du BSIF (en vigueur le 1er mai 2027). La définition de « modèle » inclut les méthodes IA/ML. **La couverture de l'agentique est une inférence d'analystes : E-23 n'emploie jamais « agentique » (§8.2.4).** **Modalité imposée : « attendu par E-23 », jamais « exigé » — ligne directrice fondée sur des principes, rédigée au conditionnel (« *should* »).** (F-09) |
| **Adaptativité après déploiement** | *adaptiveness after deployment* | Propriété par laquelle un système d'IA modifie son comportement une fois déployé. Figure dans la définition des systèmes d'IA de l'**avis ACVM 11-348** — « niveaux variables d'autonomie et d'adaptativité après déploiement » — où elle constitue l'accroche explicite de l'agentique (F-26) ; et dans la **note 1 d'E-23**, qui reprend la définition **OCDE** de l'IA (« *vary in their levels of autonomy and adaptiveness after deployment* »), socle textuel réel de sa couverture implicite (F-09, strate [B]). ⚠ **Le socle n'établit pas que les deux libellés soient identiques** ni que l'avis 11-348 emprunte à l'OCDE : de l'avis, instrument anglais, il ne porte qu'un rendu français (F-26). Ne pas agréger les deux formules. **À distinguer de** l'**adaptation** et de l'**évolution** du manifeste APM (§D.2) : trois objets différents — le comportement du système d'IA (11-348, E-23), l'instance (F-36), le modèle de processus (F-36). (F-09, F-26) |
| **Décision fondée exclusivement sur un traitement automatisé** | *decision based exclusively on automated processing* | Formule de l'art. 12.1 de la Loi 25 (P-39.1) déclenchant information, explication et **révision humaine sur demande**. ⚠ Le mot « exclusivement » est tenu pour le pivot interprétatif par l'analyse **Fasken** — **réserve d'interprétation de niveau [C]** au socle (F-27), à confronter aux positions de la CAI (lacune §10.4). **Une entrée [C] ne porte jamais un fait central** (PRD §10) : citer la nuance en l'attribuant, ne rien construire dessus. **Citer la formule officielle, ne pas paraphraser.** (F-27) |
| **Mobilité des données** | *data portability* | Droit créé à l'échelle de l'économie par C-15 en modifiant la LPRPDE ; le cadre bancaire en est la première itération. (F-11) |
| **Standard technique unique** | *single technical standard* | Exigence de la Loi sur les services bancaires axés sur les consommateurs. **Fait négatif vérifié : aucun organisme désigné, aucun standard nommé — FDX est une anticipation d'industrie (R-5).** (F-35) |
| **ISO 20022** | — | Couche sémantique commune des paiements. Lynx : fin de la coexistence MT/MX le 22 novembre 2025. (F-28) |
| **RTR** | *Real-Time Rail* | Système de paiement en temps réel de Paiements Canada, nativement ISO 20022. **Double contrainte** : la cible T4 2026 est bel et bien annoncée officiellement — ne pas écrire « aucune date annoncée » (**R-4**) ; mais elle reste une cible conditionnelle aux tests, successivement reportée — ne pas écrire « lancé » ni « en production » (**réserve F-29**). (F-29) |

---

## D.6 Plateforme d'intégration *(Partie VII — chaque terme attribué à IBM, §8.4)*

| Français | Anglais | Définition (source) |
|---|---|---|
| **Passerelle IA** | *AI Gateway* | Capacité **d'IBM** (composant d'API Connect), **annoncée en mai 2024, étendue en janvier 2025** : point de contrôle des appels aux LLM — limites de débit par requêtes **ou par jetons**, cache, masquage, audit. (F-40) |
| **Jeton** | *token* | Unité de consommation des modèles de langage. Terme générique ; c'est l'**AI Gateway d'IBM** qui, selon la documentation de l'éditeur, permet d'imposer des limites de débit **par jetons** et non seulement par requêtes. (F-40) |
| **Garde-fous de modèle** | *guardrails* | Filtres d'entrée/sortie appliqués au runtime (Granite Guardian : HAP, Harm, Violence, Jailbreak, Social Bias, Sexual content). **Homonymie interne à éviter** : dans ce projet, « garde-fou » désigne aussi les règles R-x du PRD — en Partie VII, écrire *guardrails* en italique pour la notion produit. (F-42) |
| **Workflows statiques** | *static workflows* | Orchestration déterministe (BPMN/BPEL) ; **explicitement recommandée par IBM pour les processus sous surveillance réglementaire** (pattern « Agentic AI », mis à jour le 21 févr. 2025). L'un des trois énoncés de la **convergence sur l'encadrement** — ⚠ **jamais « trois sources indépendantes »** : deux partagent une autrice, deux une organisation (§D.7). Réserve du socle : pattern **générique**, IBM ne publie aucune architecture agentique propre aux services financiers. (F-46) |

---

## D.7 Termes à ne PAS employer

| Terme proscrit | Raison | Substitut |
|---|---|---|
| « ACP » employé seul (**dans tout l'ouvrage** — R-8) | Collision à quatre branches (D.1) | Qualificatif complet obligatoire |
| « MCP sécurisé » | La sécurité dépend de l'implémentation (réserve F-01) | « cadre d'autorisation de MCP » |
| « E-23 exige pour l'IA agentique » | Inférence d'analystes (§8.2.4) | « couverture implicite via la définition de modèle » |
| « conforme à E-23 » (à propos d'un produit) | Aucun lien documenté (R-7) | « correspondance établie par inférence d'auteur » |
| « FDX est le standard canadien » | Aucun standard désigné (R-5) | « organisme de normalisation à désigner par arrêté ministériel » |
| « ligne directrice AMF en attente / en projet » | État périmé depuis le 30 mars 2026 (réserve F-25) | « finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 » |
| « C-36, la loi canadienne sur l'IA » | C-36 est une loi sur la vie privée (F-24, revalidé) | « C-36 (*Protecting Privacy and Consumer Data Act*), qui porte des volets IA » |
| « le RTR lancé / en production » | Cible T4 2026, tests industriels en cours (réserve F-29) | « dont le lancement est visé au T4 2026 » |
| « aucune date de lancement annoncée pour le RTR » | Affirmation réfutée 0-3 (R-4) — la cible T4 2026 est officielle | « la cible officielle est le T4 2026 » |
| **« exigé par E-23 », « E-23 impose », « l'exigence d'inventaire d'E-23 »** | **Réserve capitale de F-09** : ligne directrice **fondée sur des principes**, ses douze principes rédigés au conditionnel (« *should* »). La nuance décide de ce qu'une institution peut opposer à son régulateur | « **attendu par** E-23 », « les attentes d'E-23 », « E-23 **attend** que… » |
| **« fiche de modèle » / « *model card* » à propos d'E-23** | **Réserve capitale de F-09** : **0 occurrence** dans E-23, EN et FR (vérification mécanique). Même classe de faute que R-2 — prêter à une autorité un terme qu'elle n'emploie pas. ⚠ **Non-sur-correction** : le terme reste **exact pour watsonx.governance** (F-44), en contexte produit et attribué à IBM | « **documentation de modèle** » (§D.2, principe 3.3) ; « **inventaire** » (§C.1, Appendice 1) |
| **« trois sources indépendantes »** (F-36, F-37, F-46) | **Adjectif RETIRÉ du socle** le 16 juill. 2026 (PRD v1.5) — réfuté par le socle lui-même : Rinderle-Ma cosigne F-36 et F-37 ; IBM Research est parmi les auteurs de F-36 et IBM publie F-46 | « le principe est formulé par un manifeste académique, une expérimentation et un pattern de fournisseur, **dont deux partagent une autrice et deux une organisation** » |
| **« Gartner classe IBM… », toute position au Magic Quadrant iPaaS** | **R-6** — position non vérifiée ; ne pas confondre les quadrants. *(Garde-fou entièrement absent de cette table jusqu'au 17 juill. 2026, alors que §D.7 est l'instrument opérationnel de CA-2 — « aucune des affirmations R-1 à R-8 ne figure dans le texte ». Une table de proscription à laquelle manque un garde-fou entier ne peut pas porter ce critère.)* | Ne pas citer de position ; lacune PRD §10.6 |
| **« Entra ID est un registre d'agents »** | **R-2** — le socle documente des identités et des *blueprints*, pas un registre centralisé | « identités d'agents et *blueprints* » |
| **« la spécification CSA impose SPIFFE »** | **R-3** — la spécification **s'appuie sur** des standards existants, elle n'impose rien | « s'appuie sur », jamais « impose » |

<!-- Rédaction : suivre la boucle qualité PRDPlan §4.2 (traçabilité F-xx, balayage R-x, relecture adversariale).
     Enrichissement : chaque chapitre rédigé ajoute ici les termes qu'il introduit, avec leur trace F-xx.
     À la clôture : refixer la date de gel ici ET dans monographie/99-registre-gel.md, puis commit + push.

     ===========================================================================
     PASSE CORRECTIVE — AUDIT DU 17 JUILL. 2026 (`audit.md`), relecteur distinct. Date de gel
     INCHANGÉE (17 juillet 2026) : aucune source n'est rouverte par cette passe.
     ===========================================================================

     m-43 [en-tête, garde-fous] — APPLIQUÉ. L'en-tête déclarait « R-1 à R-5, R-7, R-8 » (sept) et
       omettait **R-6**, ajouté à §D.7 le 17 juillet. Recensement RECOMPTÉ MÉCANIQUEMENT, garde-fou
       par garde-fou, sur le CORPS SEUL (ce bloc de gouvernance exclu — il commente le fichier, il
       n'en est pas le contenu) :
         for i in 1 2 3 4 5 6 7 8; do
           awk '/^<!--/{exit} {print}' FICHIER | grep -oE "R-$i\b" | wc -l
         done
       → R-1 = 5, R-2 = 3, R-3 = 2, R-4 = 2, R-5 = 3, **R-6 = 2**, R-7 = 2, R-8 = 13. Les HUIT sont
       portés, aucun à zéro : l'en-tête est corrigé en « R-1 à R-8 — les huit ». Les deux occurrences
       de R-6 sont la ligne de §D.7 (la porteuse — proscription de la position au Magic Quadrant
       iPaaS) et le recensement de l'en-tête lui-même ; c'est la première qui fonde le décompte.
       ⚠ DEUXIÈME recensement faux d'affilée sur la même case (R-1/R-8 → sept → huit), et de la
       classe exacte que cette case raconte deux lignes plus haut à propos de F-26 : une ligne
       ajoutée au corps, répercutée ni sur la liste, ni sur le cardinal. Cause commune : le
       recensement a été REPRIS, jamais RECOMPTÉ. Il l'est désormais, et la commande est publiée
       pour qu'il soit reproductible.
       ⚠ INCIDENT DE CETTE PASSE MÊME, CONSIGNÉ PLUTÔT QUE MASQUÉ : ces chiffres ont d'abord été
       publiés ici mesurés sur le FICHIER ENTIER et AVANT que ce bloc n'existe — R-8 y valait 12.
       L'écriture du bloc les a périmés dans la seconde qui a suivi. C'est le constat m-40 de
       l'annexe A reproduit en direct, dans le rapport qui le corrige : une mesure date du texte
       qu'elle a lu. Corrigé en fixant un DOMAINE stable (le corps, hors bloc) et en re-mesurant en
       dernier. Un décompte s'exécute, avec la commande qui fait autorité, sur un domaine déclaré,
       **et en dernier**.

     m-44 [§D.1, branche (a)] — TRACE RENDUE ; **la forme imposée ne change pas**. L'audit reprochait
       que l'expansion « Agent Communication Protocol », prescrite par cette case à huit chapitres et
       à l'annexe C, fût ABSENTE du socle (0 occurrence au PRD et au TOC). Le grief est fondé — mais
       il est **résolu en amont** : PRD v1.10 (17 juill. 2026) verse l'intitulé développé à **F-43**,
       niveau **[B]**, par consultation directe du blog primaire que l'entrée citait DÉJÀ. La forme
       imposée est donc valide et reste littéralement inchangée ; seule la colonne « Socle » est
       enrichie de l'élévation et de sa date, pour que le lecteur sache que l'intitulé est tracé et
       depuis quand. *Enseignement, et il vaut au-delà de cette case : le défaut avait sa racine au
       SOCLE, pas dans le glossaire — corriger le glossaire (retirer l'expansion de huit chapitres)
       aurait déplacé la faute sans la traiter. L'élévation a été préférée au retrait parce que la
       source primaire était déjà au dossier : il suffisait de la lire.*

     obs. 28 [§D.2, quatre gloses d'auteur] — TRAITÉ AU CAS PAR CAS, TROIS SUR QUATRE. Critère
       appliqué (celui de l'audit) : le défaut est de faire dire au socle ce qu'il ne dit pas ; une
       glose LEXICALE d'un terme courant n'en est pas une, et la retirer serait une SUR-correction.
       · « Autonomie ≠ automatisation » ... MARQUÉ « Lecture de l'auteur ». F-36 pose la distinction
         et la déclare fondatrice ; « automatiser, c'est fixer le comportement ; rendre autonome,
         c'est déléguer la décision » est une formule de l'auteur — un énoncé conceptuel, pas la
         paraphrase d'un terme. Retenue (elle est utile), marquée (elle est de l'auteur).
       · « Traçabilité / tractabilité » ....... MARQUÉ « Lecture de l'auteur ». Même statut que
         l'« assurance de correction » voisine, dont la glose a été retirée le 17 juillet : F-37
         LISTE la propriété parmi les cinq sans la définir. Aggravant propre à cette entrée : la
         glose recouvre d'une seule formule DEUX termes que le socle ne distingue pas.
       · « Point de contrôle » (*checkpointing*) BORNÉ. « Persistance de l'état … permettant
         reprise » est le sens propre du terme et reste ; « **et inspection** » est retiré — ni dans
         le terme, ni dans F-15, qui nomme le patron sans le caractériser. Le membre retiré prêtait
         au socle une propriété d'AUDITABILITÉ, c.-à-d. précisément ce que l'ouvrage argumente : la
         glose la plus dangereuse des quatre n'était pas la plus visible.
       · « Humain-dans-la-boucle » ........... NON MODIFIÉ, ET C'EST UN VERDICT, PAS UN OUBLI.
         « Point d'arrêt exigeant une intervention humaine » est le sens PROPRE de *human-in-the-loop*
         — l'humain est DANS la boucle d'exécution —, et F-15 nomme le patron dans ce sens technique,
         aux côtés des points de contrôle et des workflows à base de graphes. Aucune propriété n'est
         prêtée au socle au-delà du terme. La distinction d'avec la révision *a posteriori* de
         l'art. 12.1 est, elle, tracée à F-27 et porte le poids utile de l'entrée. Marquer ceci
         serait la sur-correction que l'audit met en garde de commettre.

     NON TOUCHÉ, DÉLIBÉRÉMENT : §D.1 (dispositif (a)/(b)/(c)/(d) — l'audit le déclare conforme au
       strict périmètre du socle, branche par branche ; il est le résultat d'une correction coûteuse) ;
       les objets que le PRD déclare NON CARACTÉRISÉS — frame opérationnel (§10.10), empoisonnement
       d'outils / injection d'invites / empoisonnement de mémoire (§10.8), assurance de correction
       (F-37 la liste sans la définir) ; l'« actionnabilité conversationnelle », ABSENTE du glossaire
       et qui doit le rester (§10.10b : ni définition, ni terme anglais, ni critère au socle) ;
       R-6 en §D.7 ; les trois dates de gel. -->

