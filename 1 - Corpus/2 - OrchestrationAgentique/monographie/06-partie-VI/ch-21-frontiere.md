# Chapitre 21 — La frontière de la connaissance vérifiable

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) ; **§21.1 amendé le 17 juill. 2026** — accueil de la lacune §10.11 (contrôle CA-6 de P4.2) |
| Date de gel de l'information | **17 juillet 2026** *(regelé : la lacune §10.11, ouverte le 17 juill. 2026, est portée par ce chapitre — aucun des vingt-quatre n'était plus ouvert pour l'accueillir)* |
| Socle mobilisé (PRD §7) | **PRD §10** (les **onze** lacunes résiduelles — la onzième, §10.11, ouverte le 17 juill. 2026 après le gel des chapitres) et **§8.3** (sensibilité temporelle) ; PRD Annexe A (limites de méthode) ; F-01, F-02, F-03, F-04, F-05, F-09, F-24, F-25, F-27, F-29, F-32, F-34, F-35, F-36, F-37, F-38, F-41, F-42, F-43, F-46, F-47, F-48 par renvoi aux chapitres porteurs |
| Garde-fous à surveiller (PRD §8) | **CA-6** (honnêteté des lacunes) — critère central du chapitre ; **R-8 branche (d)** : la composante ACP d'AGNTCY, quatrième branche, portée ici en encadré (lacune §10.7) ; R-4 et réserve F-29, R-5, R-6 par renvoi ; §8.2 (attribution à chaque occurrence) ; **périmètre** : la lacune §10.5 appartient au ch. 16 — reprise ici par renvoi, sans duplication |
| Volumétrie cible | ~2300 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Ce que l'on ne sait pas encore, dit honnêtement — lacunes du socle, questions ouvertes, agenda de recherche.

---

Les vingt chapitres qui précèdent ont dit ce que le socle de cet ouvrage établit. Celui-ci dit ce qu'il n'établit pas — le seul qu'un auteur ayant quelque chose à vendre ne pourrait pas écrire de bonne foi.

Un registre de lacunes n'est pas un aveu de faiblesse : c'est un instrument de travail. L'architecte qui construit sur les conclusions des Parties VI et VII a besoin de savoir lesquelles reposent sur une vérification à trois juges, lesquelles sur une extraction de source primaire, lesquelles sur un repérage que nul n'a confirmé ; le responsable de la conformité qui verse une page de cet ouvrage à un dossier de diligence raisonnable, ce qu'elle peut soutenir devant un régulateur — et ce qu'elle ne peut pas.

Une distinction gouverne tout ce chapitre. **Le socle ne documente pas X** signifie qu'aucune source du corpus de cet ouvrage n'atteste X : c'est une absence de documentation, non un fait négatif vérifié. La formule « fait négatif vérifié » est réservée aux seuls cas où le socle établit l'absence par un balayage documenté — trois cas dans tout l'ouvrage : l'absence de standard technique désigné pour le cadre bancaire (ch. 14), l'absence des mots « agentique », « agent » et « orchestration » du texte intégral d'E-23 (ch. 9), et l'absence d'architecture agentique IBM propre aux services financiers (ch. 22)[^1]. Confondre les deux régimes, c'est transformer une ignorance en constat.

## 21.1 Les lacunes résiduelles

Cet ouvrage recense **onze lacunes ouvertes** à la date de gel[^2]. Deux lacunes des versions antérieures en sont sorties, non par comblement rhétorique mais par établissement : le standard technique du cadre bancaire et le calendrier du système de paiement en temps réel (*Real-Time Rail*, RTR) sont désormais au socle — le premier comme fait négatif vérifié, le second comme chronologie datée[^1][^3]. La onzième est née le 17 juillet 2026, c'est-à-dire après la date de gel des vingt-quatre chapitres et à l'occasion de leur publication : **F-11 attribue au Budget fédéral 2025 un fait structurant du cadre bancaire — la supervision confiée à la Banque du Canada — sans le dater**[^22]. La manière dont elle est apparue mérite d'être dite, parce qu'elle enseigne quelque chose sur la méthode : la lacune était restée invisible tant que le socle n'avait servi qu'à écrire de la prose, et c'est la construction d'une **frise chronologique**, en annexe C, qui l'a révélée — une frise ne peut pas porter un événement sans date. Aucun fait central de cet ouvrage n'en dépend, le chapitre 14 traitant le cadre bancaire à partir d'entrées datées. Mais un format de restitution nouveau — frise, matrice, tableau — est un révélateur de ce que la prose absorbe en silence. Les onze qui restent se rangent en cinq familles, la nouvelle venue rejoignant la dernière.

**Les lacunes en attente d'un acte réglementaire.** Deux d'entre elles ne se comblent, pour l'essentiel, par aucune recherche : elles attendent qu'une autorité agisse. La désignation de l'organisme de normalisation technique du cadre bancaire relève d'un arrêté ministériel qui n'était pas pris à la date de gel — c'est le fait qui déterminera si FDX, dont la candidature relève du commentaire d'industrie et non d'une position officielle, devient le standard canadien (ch. 14)[^3]. Le réglementaire fin est de même nature par deux de ses trois volets : ni les positions détaillées de la Commission d'accès à l'information sur l'article 12.1 appliqué aux systèmes multi-agents, ni les suites de la consultation de l'avis 11-348 des ACVM, close le 31 mars 2025, ne s'obtiennent autrement que d'une autorité qui les prendrait (ch. 11 et 12)[^2].

Son troisième volet est d'une autre espèce, et il faut le dire précisément, car c'est la lacune la plus coûteuse de l'ouvrage : le socle porte les dates de la ligne directrice sur l'IA de l'AMF, non son contenu article par article. Or ce texte est **final depuis le 30 mars 2026** : rien n'y est en attente. La lacune ne tient pas à un acte qui tarderait, mais à une extraction primaire qui n'a pas été faite — aucune passe de recherche n'y a été consacrée, et le chapitre 20 le dit en encadré. Le chapitre 18 en tire la conséquence exacte : de sa matrice, c'est la seule ligne dont le premier terme manque, et le seul vide qu'une extraction primaire comblerait. Une lacune qui attend une autorité et une lacune qui attend un lecteur ne se soldent pas de la même façon ; celle-ci est à notre charge[^2].

**Les lacunes de socle sur les objets techniques.** Trois lacunes, ouvertes lors de la rédaction des Parties I, II et IV (ch. 2, 3, 4, 5, 6 et 16), portent sur ce que les protocoles et les articles académiques ne nous ont pas dit. Le socle **nomme** l'empoisonnement d'outils (*tool poisoning*) et l'injection d'invites (*prompt injection*) sans les dater ni en verser la mécanique, sans identifiant de vulnérabilité ni incident public daté ; aucune attaque propre à A2A n'y figure — absence de documentation, non fait négatif vérifié (ch. 4)[^4]. Le socle n'établit ni l'ancrage de confiance, ni la révocation, ni la gouvernance des clés des cartes d'agents signées (*Signed Agent Cards*) — trois questions qui décident, à elles seules, de ce que vaut une signature ; il ne date pas la publication de la v1.0 d'A2A ; il ne caractérise pas le mécanisme de la « multi-location d'entreprise » **ni son terme anglais d'origine**, que cet ouvrage se garde d'inventer ; il ne porte pas davantage d'inventaire plateforme × statut des intégrations infonuagiques de MCP — symétrique de ce qu'il établit pour A2A —, ni la structure de message, le mandat ou la preuve d'intention d'AP2, ni son transfert de gouvernance (ch. 2, 3 et 16)[^5]. Enfin, le socle académique est sous-caractérisé : le *frame* opérationnel ne l'est pas, alors que son articulation avec le *frame* normatif est la thèse de l'ouvrage ; l'« actionnabilité conversationnelle » n'a au socle ni définition, ni terme anglais, ni critère de satisfaction ; et la propriété d'autonomie est la seule des cinq à n'avoir aucune métrique quantitative (ch. 5 et 6)[^6].

**Les lacunes d'adoption.** Le socle documente l'absence de sources primaires agentiques pour la Banque Nationale — que la passe de revalidation n'a pas re-recherchée, faute de signal d'une source nouvelle — et s'en tient là, plutôt que de combler par du secondaire. Deux élévations ont partiellement échoué et le disent : les agents d'adhésion, de relevés fiscaux et de traitement des réclamations attribués à Sun Life restent au niveau de repérage, la seule source restante étant secondaire et sous péage ; le traitement de l'IA générative comme facteur de risque matériel dans le rapport annuel 2025 de BMO reste au même niveau, le document n'ayant pu être extrait par les outils disponibles (ch. 17)[^7]. Les chiffres d'adoption d'entreprise de Temporal ne sont toujours pas vérifiés (ch. 7)[^8]. Aucun de ces quatre points ne doit porter un fait central de l'ouvrage — c'est la règle que cet ouvrage s'est donnée, et son respect est contrôlé à la relecture finale, point par point, avant publication[^2].

**Les lacunes du blueprint.** La position d'IBM au Gartner Magic Quadrant iPaaS n'est pas vérifiée ; la solution de transformation ISO 20022 du portefeuille reste au niveau de repérage après une passe de recherche menée et infructueuse ; la date officielle de l'annonce d'Agent Connect n'est pas au socle ; et le socle ne recense aucune annonce d'IBM avec une institution financière canadienne autre que BMO et TD. Ces quatre points sont développés aux chapitres 22 et 24[^9].

**La prospective.** L'articulation d'AP2 (*Agent Payments Protocol*) avec les rails de paiement canadiens est ouverte, instruite et exposée au chapitre 16, qui en est le porteur ; elle est reprise ici par simple renvoi, sans duplication[^10].

Reste la quatrième branche du garde-fou de désambiguïsation, traitée ici.

> **État de la recherche — la composante ACP d'AGNTCY**
>
> **Question** : quel est l'intitulé complet de la composante ACP d'AGNTCY, et cette composante est-elle identique — ou non — au protocole ACP (*Agent Communication Protocol*) d'IBM Research, fusionné dans A2A le 29 août 2025 ?
>
> Lacune ouverte le 16 juillet 2026, lors de la rédaction du chapitre 1 ; **aucune passe de recherche n'a été conduite** — le point est apparu après la clôture des trois passes qui ont constitué le socle et après la revalidation du même jour, dont le périmètre était les faits chauds[^11]. Ce que le socle porte : une mention, attribuée à des **analyses tierces**, d'un chevauchement entre « sa composante ACP » et A2A[^12]. Ce que le socle **n'établit pas** : ni l'intitulé complet de cette composante, ni son identité, ni sa non-identité avec le protocole ACP d'IBM Research. Source à retrouver : la documentation primaire d'AGNTCY (docs.agntcy.org ou le dépôt GitHub du projet).
>
> La question reste ouverte ; **aucune inférence n'est proposée ici**. Cet objet est désigné dans tout l'ouvrage par « la composante ACP d'AGNTCY », toujours qualifié, et n'est jamais agrégé aux trois autres emplois du sigle — pas davantage qu'il n'en est distingué comme d'un fait : le socle ne permet ni l'un ni l'autre[^13].

## 21.2 Les questions de recherche

Chaque lacune résiduelle devient un encadré, ou une question de recherche formulée en Partie VI[^2]. Voici les secondes, énoncées pour qu'un chercheur puisse les instruire — chacune avec ce qui la trancherait.

| # | Question | Ce qui la trancherait |
|---|---|---|
| Q1 | La taxonomie des options d'orchestration OO1–OO4 résiste-t-elle à une reproduction indépendante ? | Une réplication par une équipe distincte, et une application documentée à un processus d'institution financière — aucune des deux n'existe au socle[^6] |
| Q2 | Quelle est la mécanique des risques protocolaires nommés ; existe-t-il des attaques propres à A2A ? | Une source primaire consacrée, un identifiant de vulnérabilité, un incident public daté[^4] |
| Q3 | Que vaut cryptographiquement une carte d'agent signée ? | La documentation de l'ancrage de confiance, de la révocation et de la gouvernance des clés[^5] |
| Q4 | L'article 12.1 s'applique-t-il à une décision prise par un système multi-agents avec humain-dans-la-boucle ? | Une position de la Commission d'accès à l'information ou une décision judiciaire ; le socle ne porte qu'une nuance d'analyse de cabinet[^2] |
| Q5 | Quelle organisation sera désignée organisme de normalisation technique du cadre bancaire ? | Un arrêté ministériel — publication à surveiller[^3] |
| Q6 | Comment le *frame* opérationnel s'articule-t-il au *frame* normatif ? | Une relecture ciblée du manifeste APM, dont le PDF est au dépôt : élévation possible en une passe[^6] |

Trois de ces questions méritent qu'on dise pourquoi elles sont inconfortables.

La première (Q1) l'est parce que la taxonomie OO1–OO4 **structure les Parties II, VI et VII** et repose sur **une source unique** : un préprint v1 non révisé par les pairs, dont les auteurs déclarent eux-mêmes des menaces à la validité — expériences initiales, invites non comparées, facteurs confondants[^6]. Le cadre conceptuel est repris ici comme référence ; les chiffres, à titre d'illustration seulement.

La deuxième porte sur la convergence érigée en principe directeur du blueprint. Le principe de l'encadrement déterministe est formulé, dans la littérature de la mi-2026, par un manifeste académique, une expérimentation et un pattern de fournisseur, **dont deux partagent une autrice et deux une organisation**[^14]. La convergence est un faisceau réel ; elle ne vaut pas corroboration indépendante, et le chapitre 13 en tire la portée exacte.

La troisième est méthodologique. Sur les 384 affirmations extraites par les trois passes de recherche, **75 seulement ont atteint le vote adversarial à trois juges** — un peu moins d'un cinquième —, dont 69 confirmées à l'unanimité et 6 réfutées ; le reste du socle repose sur l'extraction de source primaire ou le repérage. Le plafond était budgétaire et documenté : les angles les plus tardifs de la troisième passe n'ont pas été soumis au vote[^15]. **Lecture de l'auteur** : cette asymétrie ne disqualifie rien, puisque les niveaux de preuve sont portés entrée par entrée ; elle indique où porterait le meilleur rendement d'une passe supplémentaire. Le socle établit les décomptes et la limite ; il n'établit pas que les entrées non votées soient moins exactes — seulement qu'elles sont moins vérifiées.

## 21.3 Les conditions de péremption de l'ouvrage

Un ouvrage daté doit dire quand il cesse d'être actuel : le domaine évolue par trimestres, et chaque chapitre porte pour cette raison sa date de gel[^16]. Voici les événements qui périment une partie du texte.

**Lecture de l'auteur** : périmer n'est pas ici une figure de style, mais ce n'est pas non plus falsifier. Ces échéances ne dégradent pas l'ouvrage de façon diffuse : chacune vise une formulation précise, identifiée dans la colonne de droite, et celle-là seulement. Et parce que ces formulations sont datées, l'événement ne les rend pas fausses mais non actuelles — le lecteur postérieur lit un énoncé qui a changé de temps grammatical. C'est la fonction même de la date de gel ; seule basculerait dans le faux une formulation que l'événement contredirait sans être bornée par la sienne. Le socle établit chacune de ces dates ; il n'établit pas qu'elles seront tenues.

| Échéance | Événement | Ce qu'il périme |
|---|---|---|
| 28 juillet 2026 | Finalisation attendue de la révision majeure de la spécification MCP : **onze jours après la date de gel** | L'anatomie technique du ch. 2, gelée sur la révision 2025-11-25[^17] |
| 24 août 2026 | Entrée en vigueur du règlement administratif no 10 du RTR | Le statut réglementaire du ch. 15[^18] |
| 26 août 2026 | Clôture des commentaires sur le règlement prépublié du cadre bancaire — **le texte final peut changer** | Le ch. 14[^3] |
| Sans date | Arrêté ministériel désignant l'organisme de normalisation technique | Le fait négatif vérifié du ch. 14 et son garde-fou ; le flux 3 du ch. 23[^3] |
| Cible T4 2026 | Lancement du RTR — **cible officielle, conditionnelle au succès des tests industriels en cours, successivement reportée : 2019, puis 2022, puis 2023, puis 2026** | La réserve interdisant d'écrire « lancé » ou « en production » (ch. 15 et 16)[^18] |
| En cours | Trajectoire du projet de loi C-36, en deuxième lecture à la date de gel | Le ch. 10 — C-36 est une loi sur la vie privée portant des volets IA, non une loi IA autonome[^19] |
| 1er mai 2027 | Entrée en vigueur commune d'E-23 et de la ligne directrice sur l'IA de l'AMF — **moins de dix mois après la date de gel** | Le discours de « futur proche » des Parties III et VI ; la feuille de route du ch. 20[^20] |

**Lecture de l'auteur** : la concentration de ces échéances sur les neuf mois et demi qui suivent la date de gel n'est pas un accident de calendrier. Elle est la signature d'un domaine dont les deux trajectoires — protocolaire et réglementaire — sont simultanément en phase de stabilisation. Deux de ces échéances — la cible du RTR et l'arrêté de désignation — ont un historique ou une absence de calendrier qui invite à la prudence. Le protocole de revalidation est développé au chapitre 24 ; la dernière doit dater de moins de trente jours à la publication[^21].

## Ce que ce chapitre établit, et ce qu'il ne dit pas

**Premièrement**, les onze lacunes recensées sont toutes exposées : cinq sont développées dans leur ou leurs chapitres porteurs, et là seulement (§10.1 au ch. 14, §10.2 au ch. 17, §10.3 au ch. 7, §10.4 aux ch. 11 et 12, §10.6 aux ch. 22 et 24) ; quatre sont reprises ici après avoir été posées en encadré dans les chapitres qui les ont ouvertes (§10.7 à §10.10) ; la dixième, la prospective du ch. 16, est reprise ici par simple renvoi ; la onzième (§10.11), ouverte le 17 juillet 2026 par la rédaction de l'annexe C, n'a pas de chapitre porteur — les vingt-quatre étaient gelés — et est donc exposée **ici**, ainsi qu'en encadré à l'annexe C[^22]. Aucune n'est silencieusement omise. **Deuxièmement**, trois élévations de niveau de preuve ont buté sur les moyens documentaires — deux partiellement (BMO, le facteur de risque matériel gen-IA ; Sun Life, les agents d'adhésion, de relevés fiscaux et de réclamations), une entièrement (la solution ISO 20022 du portefeuille d'intégration) ; les faits **non élevés** sont dits comme tels et ne sont portés nulle part comme faits centraux[^7][^9]. **Troisièmement**, la dépendance la plus lourde de l'architecture de référence — la taxonomie OO1–OO4 — repose sur une source unique et non répliquée, et la convergence à trois sources qui fonde le principe directeur du blueprint n'est pas une convergence de sources indépendantes.

Ce chapitre ne dit pas, en revanche, que ces lacunes invalident les conclusions de l'ouvrage : une conclusion tracée à un socle qui porte ses niveaux de preuve reste utilisable à hauteur du niveau qu'elle invoque. Il ne dit pas non plus que le registre soit complet — il est exhaustif au regard du recensement arrêté à la date de gel, ce qui n'est pas la même chose : la lacune sur la composante ACP d'AGNTCY est née de la rédaction du premier chapitre, et rien ne garantit que la suite n'en révèle pas d'autres. Il ne dit pas, enfin, qu'aucune de ces questions n'ait de réponse : il dit que cet ouvrage ne la connaît pas, et qu'il se l'interdit plutôt que de la deviner.

C'est le seul engagement qu'une monographie datée puisse honnêtement tenir. Elle ne promet pas d'avoir raison longtemps. Elle promet de dire où elle ignore.

---

## Notes

[^1]: PRDPlan §4.4, formule de distinction imposée (« absence de documentation ≠ fait négatif vérifié »). Les trois faits négatifs vérifiés du socle : **F-35** (PRD §7.4 — recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI », « OAuth » dans le règlement prépublié, le communiqué et la page Budget 2025 : zéro occurrence ; votes 3-0 ×6) ; **F-09** (PRD §7.3 — vérification mécanique sur le texte intégral d'E-23, EN et FR : « agentique »/« agentic » = 0, « agent(s) » = 0, « orchestration » = 0, « autonom\* » = 8) ; **F-46** (PRD §7.8 — architecture agentique IBM propre aux services financiers introuvable sur ibm.com/architectures et Redbooks).

[^2]: PRD §10 (**onze** lacunes ouvertes — dix au 16 juillet 2026, la onzième, §10.11, ouverte le 17 juillet 2026 à la rédaction de l'annexe C : voir note [^22]) et son exigence de clôture : « chaque lacune restante devient soit un encadré "état de la connaissance vérifiable" dans la monographie, soit une question de recherche explicite en Partie VI. Interdiction de combler par des sources non vérifiées. » Réglementaire fin : PRD §10.4 ; **réserve d'interprétation F-27** (PRD §7.3, niveau [C]) sur la nuance Fasken relative au mot « exclusivement ».

[^3]: PRD §10.1 et **F-35** (niveau [A], PRD §7.4 ; sources primaires : gazette.gc.ca, canada.ca/Finances, bankofcanada.ca). Garde-fou **R-5** (PRD §8.1) : aucun standard n'est nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie (Fasken, Bennett Jones, NCFA), pas d'une position officielle. Revalidation du 16 juillet 2026 : aucun arrêté ministériel publié à ce jour (`verification/revalidation-2026-07-16.md`, P0.1 ligne 2). **F-34** (PRD §7.4) pour la prépublication du 27 juin 2026 et la clôture des commentaires au 26 août 2026.

[^4]: PRD §10.8 (lacune ouverte le 16 juillet 2026, à la rédaction des ch. 2 et 4). **F-01** (PRD §7.1, réserve — MCP : empoisonnement d'outils et injection d'invites nommés, non datés) ; **F-36** (PRD §7.7, défi C2 — empoisonnement de mémoire, patrons *Action-Selector* et *Plan-Then-Execute*). Le socle ne verse aucune source primaire consacrée à leur mécanique.

[^5]: PRD §10.9 (ouverte le 16 juillet 2026, ch. 2, 3 et 16). **F-02** (PRD §7.1, niveau [A] — le socle ne documente ni l'ancrage de confiance, ni la révocation, ni la gouvernance des clés des *Signed Agent Cards*, ne date pas la publication de la v1.0, et ne caractérise ni le mécanisme de la « multi-location d'entreprise » ni son terme anglais d'origine : **CA-5 n'est pas servable ici, et aucune traduction n'est inventée**) ; volets (d) et (e) de la même lacune : **F-03** (inventaire plateforme × statut des intégrations infonuagiques — établi pour A2A, absent pour MCP) et **F-04** (AP2 — ni structure de message, ni mandat, ni preuve d'intention, ni transfert de gouvernance documenté ; ch. 16).

[^6]: PRD §10.10 (ouverte le 16 juillet 2026, ch. 5 et 6). **F-36** (PRD §7.7, niveau [B] — Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al., *Information Systems* 140, 102738 (2026) / arXiv:2603.18916) et **F-37** (PRD §7.7, niveau [B] pour le cadre, moyen pour les chiffres — Rinderle-Ma, Mangler et al., arXiv:2606.31518v1, 30 juin 2026, **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité). Les PDF des deux articles sont au dépôt : élévation possible en une passe de relecture ciblée.

[^7]: PRD §10.2. **F-47** (PRD §7.5, BMO — Lumi et bootcamps élevés [B] ; facteur de risque matériel gen-IA du rapport annuel 2025 **non élevé**, PDF bmo.com/ir trop volumineux pour extraction, dépôts SEC bloqués en 403) ; **F-48** (PRD §7.5, Sun Life — communiqué primaire du consortium élevé [B] ; agents d'adhésion, relevés fiscaux et réclamations **non élevés**, sunlife.com inaccessible aux outils de vérification, seule source restante The Logic, secondaire et sous péage, à attribuer explicitement si citée). Banque Nationale : PRD §7.5, aucune source primaire agentique remontée. Détail des deux échecs : `verification/revalidation-2026-07-16.md`, P0.2 lignes 1 et 2.

[^8]: PRD §10.3 et §7.6 (Temporal, niveau [C] — chiffres d'adoption d'entreprise non vérifiés). La lacune a été **réduite** en P0 : le support A2A de CrewAI est élevé [B], celui de LangGraph Platform/LangSmith Deployment également, **avec réserve de périmètre** — la bibliothèque open source `langgraph` n'a pas de support A2A natif documenté (**F-32**, PRD §7.6).

[^9]: PRD §10.6 et Annexe B.5. Garde-fou **R-6** (PRD §8.1 — position au Gartner MQ iPaaS non vérifiée ; ne pas confondre avec le Forrester Wave iPaaS Q3 2025 et le Gartner MQ **API Management** 2025, où IBM est Leader selon **F-38**). Échec d'élévation documenté de la solution FTM/ISO 20022 (passe du 16 juillet 2026, `verification/revalidation-2026-07-16.md`, P0.2 ligne 4 : lien confirmé par un Redbook de 2016, aucune source non-Redbook actuelle extractible, ibm.com/docs en 403). La clôture de l'acquisition Confluent, lacune jusqu'en P0, est **résolue** — 17 mars 2026, **F-41**.

[^10]: PRD §10.5 — lacune portée par le ch. 16, chapitre explicitement prospectif, où l'encadré « état de la connaissance vérifiable » est posé et la passe de recherche documentée. Reprise ici « par simple renvoi, sans duplication », conformément à PRD §10.5 et à [TOC.md](../../TOC.md) (contrôle de couverture).

[^11]: PRD §10.7 (lacune ouverte le 16 juillet 2026, à la rédaction du ch. 1) ; gabarit d'encadré du **cas 2** de PRDPlan §4.4 (« lacune non instruite ») — aucune passe de recherche n'a été conduite sur ce point, et le prétendre serait fabriquer une passe qui n'a pas eu lieu. Périmètre des trois passes : PRD Annexe A ; périmètre de la revalidation du 16 juillet 2026 : `verification/revalidation-2026-07-16.md`, P0.1 (faits chauds §8.3).

[^12]: PRD §7.1, **F-05** (niveau [A]). Source primaire : communiqué de la Linux Foundation du 29 juillet 2025 ; corroboration VentureBeat, Forbes. Le chevauchement entre « sa composante ACP » et A2A est une **analyse tierce**, attribuée comme telle et non endossée par le socle.

[^13]: PRD §8.1, garde-fou **R-8**, branche (d), et §10.7. Formes imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.1 et §D.7. Le sigle « ACP » employé seul est **proscrit dans tout l'ouvrage** ; l'encadré de désambiguïsation des quatre branches est **posé au ch. 1 §1.2** (première occurrence réelle du sigle) et n'est pas dupliqué ici. Branches (a), (b) et (c) : **F-43**, **F-48**, **F-42**.

[^14]: PRD §7.8, **F-46**, formulation imposée par le correctif du 16 juillet 2026 : l'adjectif « indépendantes » est **retiré**, réfuté par le socle lui-même. Deux recoupements documentés : Rinderle-Ma cosigne F-36 et F-37 ; IBM Research figure parmi les organisations des 18 auteurs de F-36, et IBM publie F-46. Ne jamais écrire « trois sources indépendantes recommandent l'encadrement déterministe ». Portée exacte : ch. 13 §13.2.

[^15]: PRD Annexe A (tableau des trois passes et section « Limites »). Décomptes : 324 lancements d'agents (105 + 107 + 112) ; 77 sources (23 + 25 + 29) ; 384 affirmations extraites (115 + 124 + 145) ; **75 soumises au vote adversarial** (25 par passe — plafond budgétaire), dont **69 confirmées 3-0** (22 + 25 + 22) et **6 réfutées** (3 + 0 + 3). Les angles 3 à 6 de la passe 3 (ACVM, Loi 25, BMO/CIBC/BNC/Sun Life/Intact, LangGraph/CrewAI/Temporal/Confluent) n'ont pas atteint le vote et sont couverts au socle en [B] ou [C]. « Confirmé » signifie corroboré par les sources citées à la date indiquée, pas garanti pérenne.

[^16]: PRD §8.3 (sensibilité temporelle) et **CA-4** (PRD §11) : chaque chapitre porte sa date de gel ; revalidation complète des faits « chauds » avant publication.

[^17]: PRD §7.1, **F-01**, fait chaud à resurveiller (PRDPlan P4.1) : *release candidate* verrouillée le 21 mai 2026 (refonte sans état, retrait de `Mcp-Session-Id`, en-têtes `Mcp-Method`/`Mcp-Name`), finalisation prévue le **28 juillet 2026**, décrite par les mainteneurs comme la plus importante révision depuis le lancement. Source : blog.modelcontextprotocol.io, via `verification/revalidation-2026-07-16.md`, P0.1 ligne 5. Calcul, **ancré à la date de gel du présent chapitre (17 juillet 2026, regel)** : du 17 au 28 juillet 2026 = **onze jours**. *L'écart avec les ch. 2, 4, 18, 19 et 20, qui comptent douze jours, n'est pas une divergence : ces chapitres sont gelés au 16 juillet et comptent depuis leur propre gel.*

[^18]: PRD §7.4, **F-29** (niveau [A], votes 3-0 ×9 ; sources : payments.ca, page RTR revalidée le 16 juillet 2026). Garde-fou **R-4** : la cible T4 2026 **est** officiellement annoncée — ne pas écrire « aucune date annoncée ». **Réserve F-29** : c'est une cible, pas un fait accompli — ne pas écrire « lancé » ni « en production ». Règlement administratif no 10 : Gazette du Canada partie II, 1er juillet 2026, en vigueur le 24 août 2026. Formulation des reports imposée par PRDPlan §4.4 (ce sont les cibles successives, non les dates auxquelles les reports ont été décidés).

[^19]: PRD §7.3, **F-24** (niveau [B], revalidé le 16 juillet 2026 par consultation directe de parl.ca/LEGISinfo, 45-1/c-36) : *Protecting Privacy and Consumer Data Act*, première lecture le 15 juin 2026, deuxième lecture au 16 juillet 2026 ; réforme de la LPRPDE créant la *Digital Safety and Data Protection Commission of Canada*, **pas une loi IA autonome de type LIAD** (glossaire §D.7). Le vide fédéral sur la régulation spécifique de l'IA persiste (ch. 10).

[^20]: PRD §7.3, **F-09** (niveau **[A/B mixte]** — marquage du socle, PRD v1.7 ; le marquage individuel prime la phrase de portée générale du §7). L'entrée porte deux strates, et cette note doit dire laquelle elle mobilise : l'**entrée en vigueur d'E-23 le 1er mai 2027** — seul fait que la ligne du tableau fait travailler — relève de la strate **[A]** (faits des passes 1-2, vote adversarial 3-0) ; l'**absence de disposition transitoire dans le texte** relève de la strate **[B]** (exigences opératoires extraites du texte intégral le 16 juillet 2026). *Un état antérieur de cette note écrivait « niveau [B] » à plat, sous-étiquetant ainsi un fait voté 3-0 : marquage rectifié le 17 juillet 2026 (audit du 17 juill., m-29). La faute est de sens inverse de celle que le PRD proscrit nommément — surqualifier —, mais elle procède de la même racine : une entrée à deux strates traitée comme si elle n'en avait qu'une.* Et **F-25** (ligne directrice sur l'IA de l'AMF, finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 — **jamais « en attente » ni « en projet »**, réserve F-25). Calcul, **ancré à la date de gel du présent chapitre (17 juillet 2026, regel)** : du 17 juillet 2026 au 1er mai 2027 = 17 juill. 2026 → 17 avril 2027 = neuf mois ; 17 avril → 1er mai 2027 = quatorze jours ; soit **neuf mois et quatorze jours (288 jours)**. *Les ch. 9, 11, 14, 18, 19 et 20 posent « neuf mois et quinze jours » (289 jours) : ils sont gelés au 16 juillet et comptent depuis leur propre gel — concordance, non divergence.* Les deux énoncés que ce décompte soutient restent exacts : « moins de dix mois » (tableau §21.3) et « neuf mois et demi » (§21.3, arrondi — quatorze jours valant ici la demie).

[^21]: PRDPlan §6 (P4.1) et §8 (definition of done, point 3) : la revalidation temporelle finale doit dater de **moins de 30 jours** au moment de la publication. Protocole de revalidation du blueprint : ch. 24 §24.3. Conditions de péremption propres au blueprint : PRD Annexe B.5, point 6.


[^22]: PRD **§10.11** (lacune ouverte le **17 juillet 2026**, à la rédaction de l'annexe C — postérieure à la date de gel des vingt-quatre chapitres). **F-11** (PRD §7.4) attribue au **Budget fédéral 2025** la réorientation du cadre des services bancaires axés sur le consommateur — supervision et mise en œuvre déléguées à la **Banque du Canada** plutôt qu'à l'ACFC — **sans dater cette annonce**. Élévation requise : consultation primaire (budget.canada.ca ; banqueducanada.ca). **Aucun fait central de l'ouvrage n'en dépend** : le ch. 14 traite le cadre bancaire à partir de F-23, F-34 et F-35, qui sont datés. La lacune est **exposée en encadré à l'annexe C**, l'événement étant hors frise faute de date. *Enseignement de méthode consigné au PRD : un format de restitution nouveau — frise, matrice, tableau — est un révélateur de lacunes que la prose absorbe silencieusement ; les annexes B et C ont chacune découvert, en P4, un défaut que vingt-quatre chapitres n'avaient pas vu.*

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps = 2 527 mots tableaux compris,
                                   2 075 mots de prose hors tableaux — les deux dans la tolérance 2 300 +/- 10 %
                                   [2 070 - 2 530], décompte re-vérifié APRÈS les correctifs de relecture)
     2. Traçabilité (CA-1, CA-5) . fait (**22 notes** — RECOMPTÉES le 17 juill. 2026 par extraction
                                   (`grep -cE '^\[\^[0-9]+\]:'`) et non de mémoire. Ce poste annonçait « 21 notes » :
                                   décompte FAUX depuis l'amendement du 17 juillet, qui a ajouté [^22] (accueil de
                                   la lacune §10.11) sans que le décompte du poste soit re-posé — audit du
                                   17 juill., m-31. Faute de la même famille que m-30 ci-dessous : un chiffre exact
                                   à l'écriture, périmé par une modification ultérieure du même fichier, et jamais
                                   re-mesuré. ; termes anglais en italique entre parenthèses à la 1re occurrence :
                                   Real-Time Rail, tool poisoning, prompt injection, Signed Agent Cards, frame,
                                   Agent Payments Protocol, Agent Communication Protocol, release candidate.
                                   CA-5 déclaré NON SERVABLE pour « multi-location d'entreprise » et
                                   « actionnabilité conversationnelle » — le socle ne porte pas leur terme anglais, §10.9/§10.10)
     3. Balayage garde-fous ...... fait (R-8 : sigle ACP toujours qualifié, branche (d) portée en encadré, encadré du ch. 1 non
                                   dupliqué ; R-4 + réserve F-29 : cible officielle ET jamais « lancé » ; R-5 ; R-6 ;
                                   §8.2 : Gartner/Forrester attribués ; §10.5 par renvoi au ch. 16, aucune duplication)
     4. Relecture adversariale ... FAIT (2 relecteurs indépendants, 16 juill. 2026 — 4 bloquants, 9 réserves ;
                                   tous vérifiés au socle et fondés ; tous corrigés). Ce que la relecture a RÉFUTÉ :
                                   a) « treize mois » (concentration des échéances) — CHIFFRE FABRIQUÉ : l'échéance la plus
                                      tardive du tableau est le 1er mai 2027, soit 9 mois et 15 jours après le gel du
                                      16 juill. — 9 mois et 14 jours après le regel du 17 (voir poste 6). La borne
                                      haute à 13 mois avait été construite à rebours pour couvrir un « déploiement RTR
                                      se poursuivant en 2027 » que F-29 ne date pas et que le tableau ne porte pas.
                                      -> « neuf mois et demi », cohérent avec la ligne du 1er mai 2027 et la note [^20].
                                   b) « deux élévations ont échoué » — DÉCOMPTE FAUX DANS LES DEUX SENS : BMO et Sun Life ont
                                      ÉLEVÉ PARTIELLEMENT (F-47, F-48 portent le §17.8) ; FTM/ISO 20022 (P0.2 ligne 4) est le
                                      seul ÉCHEC ENTIER et était omis. -> trois élévations, deux partielles, une entière.
                                   c) « chaque événement rend fausse une formulation » — INFÉRENCE NON MARQUÉE et réfutée par
                                      le tableau qui la suit (« peut changer », « En cours », « attendue ») et par PRD §8.3 /
                                      CA-4 : un énoncé daté ne devient pas faux, il devient dépassé. -> marqué « Lecture de
                                      l'auteur » et aligné sur le ch. 15 § 15.3 (« changé de temps grammatical »).
                                   d) « c'est la règle, et elle a été tenue » — AUTO-ATTESTATION DE CONFORMITÉ : le socle porte
                                      la règle (PRD §10, clause finale), jamais le constat de son respect ; le contrôle est
                                      P4.2 (grille `verification/relecture-CA.md`, à l'état ☐) et porte sur des chapitres non
                                      encore rédigés (18-20, 22-24, dont les ch. 22 et 24 visés ici). -> énoncé de règle.
                                   Réserves corrigées : en-tête sous-déclarait le socle (11 entrées citées en notes absentes —
                                   F-03, F-04, F-09, F-24, F-25, F-27, F-34, F-38, F-41, F-42, F-43) ; §10.9 exposée à 3 volets
                                   sur 5 alors que le chapitre revendique CA-6 (volets d et e ajoutés au corps, pas seulement en
                                   note) ; §10.9 attribuée aux seules Parties I-II alors que le ch. 16 (Partie IV) en est
                                   co-ouvreur ; Q6 disait « les deux articles » pour une question qui ne porte que sur F-36 ;
                                   « leur seul chapitre porteur » réfuté par sa propre énumération (§10.4 -> ch. 11 ET 12 ;
                                   §10.6 -> ch. 22 ET 24) ; fuites de registre éditorial vers le lecteur (« Formulation imposée,
                                   et il faut la citer exactement », « cahier des charges », « porteur désigné », « conformément
                                   au découpage arrêté », « la règle du projet ») passées au registre de l'ouvrage (PRD §4).
                                   AUCUN constat écarté. Volumétrie : les correctifs (+~110 mots) ont porté le corps à 2 674 ;
                                   resserrement de la prose redondante et des cellules du tableau (détail conservé aux notes
                                   [^17], [^19]) -> 2 527. Fait de fond ajouté au passage (revalidation P0.2, « Limites ») :
                                   la Banque Nationale n'a pas été re-recherchée en P0, faute de signal de source nouvelle.
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     6. Passe de correction ...... 17 juill. 2026 — AUDIT GLOBAL DU 17 JUILL. 2026, constats m-29, m-30, m-31, m-32.
        (audit du 17 juill. 2026)  Aucune réécriture ; DATE DE GEL INCHANGÉE (17 juillet 2026, regel) — c'est elle
                                   qui COMMANDE les recalculs ci-dessous.
                                   m-30 — RACINE, et c'est la plus instructive de la passe : ce chapitre a été
                                   REGELÉ au 17 juillet (accueil de la lacune §10.11), mais ses décomptes sont
                                   restés ancrés au 16. Un regel n'est pas un changement d'en-tête : c'est un
                                   changement d'ORIGINE, et tout intervalle exprimé « après la date de gel » en
                                   dépend. Trois énoncés étaient faux ; tous ré-ancrés, tous recalculés à la main :
                                     - §21.3, tableau : « douze jours après la date de gel » -> **onze** jours
                                       (17 -> 28 juill. 2026 = 11).
                                     - note [^17] : « du 16 au 28 juillet 2026 = douze jours » -> du 17 au 28 = onze.
                                     - note [^20] : « du 16 juillet 2026 au 1er mai 2027 = neuf mois et demi »
                                       -> du 17 juill. 2026 au 1er mai 2027 = **neuf mois et quatorze jours**
                                       (288 j) : 17 juill. -> 17 avril 2027 = 9 mois ; + 14 j = 1er mai.
                                     - poste « Arithmétique » et réfutation a) de l'étape 4 : ré-ancrés de même.
                                   ÉNONCÉS DÉPENDANTS RE-CONTRÔLÉS UN À UN, et TENUS sans retouche : « moins de
                                   dix mois » (tableau §21.3) — 9 mois 14 j < 10 mois ; « neuf mois et demi »
                                   (§21.3, prose) — arrondi, 14 j valant la demie ; « 9,5 mois » (poste
                                   Arithmétique). Ne PAS les « corriger » : ce sont des arrondis exacts.
                                   BALAYAGE DE COMPLÉTUDE (l'audit exige l'ensemble du fichier, pas les trois
                                   points cités) : motif `16 juill|douze jours|neuf mois et quinze` passé sur le
                                   corps et les notes — toutes les occurrences restantes de « 16 juillet 2026 »
                                   sont des DATES D'ÉVÉNEMENT (ouverture de lacune, revalidation P0, consultation
                                   de source, correctif F-46, relecture adversariale), correctement ancrées et
                                   qui ne doivent PAS bouger : elles datent un fait, elles ne comptent pas depuis
                                   le gel. La distinction est le cœur de m-30.
                                   m-31 — « 21 notes » -> **22**, recomptées par extraction (poste 2).
                                   m-29 — note [^20], marquage F-09 « niveau [B] » à plat sur un fait de strate
                                   [A] : rectifié en [A/B mixte] avec la strate mobilisée nommée (note [^20]).
                                   NE PAS SUR-CORRIGER : l'entrée n'est pas [A] pour tout — l'absence de
                                   disposition transitoire, mobilisée par la même note, est bien [B].
                                   m-32 — §21.1, famille « en attente d'un acte réglementaire » : le volet AMF de
                                   §10.4 y était rangé comme ne se comblant « par aucune recherche ». INEXACT, et
                                   coûteux : la ligne directrice est FINALE depuis le 30 mars 2026 (F-25) — rien
                                   n'y attend une autorité ; sa lacune se comble par EXTRACTION PRIMAIRE, ce que
                                   disent le ch. 18 §18.3 (« seul vide qu'une extraction primaire comblerait ») et
                                   le ch. 20 (encadré : « Source à retrouver : lautorite.qc.ca »). Les volets CAI
                                   et suites ACVM, eux, attendent bien un acte : la famille garde donc ses DEUX
                                   lacunes (§10.1, §10.4) et le §10.4 y reste — c'est sa CARACTÉRISATION qui est
                                   corrigée, par distinction de ses trois volets. CA-6 INTACT, vérifié après
                                   coup : les ONZE lacunes restent toutes exposées, les cinq familles sont
                                   inchangées, aucune n'est comblée par du non-vérifié, et le décompte de la
                                   conclusion (5 + 4 + 1 + 1) n'est pas touché. m-32 corrige une caractérisation,
                                   pas une couverture.
                                   VOLUMÉTRIE RE-MESURÉE APRÈS CORRECTIONS — et il faut être franc sur ce que
                                   cette mesure vaut. Commandes du ch. 19 (les seules PUBLIÉES du dépôt),
                                   réexécutées sur ce fichier : **B (tableaux inclus) = 2791 ; C (prose seule) =
                                   2370**. Sur la base C, qui fait foi par l'arbitrage du ch. 18 et du ch. 19 (la
                                   consigne porte sur le corps de PROSE ; un tableau n'est pas de la prose) :
                                   2370 pour une cible de 2300 ±10 % [2070-2530] — **CONFORME** (+3,0 %).
                                   ⚠ RÉSERVE DE MÉTHODE, à signaler à la gouvernance plutôt qu'à masquer : le
                                   poste 1 de ce journal annonce « 2 527 mots tableaux compris, 2 075 de prose »
                                   SANS PUBLIER SA COMMANDE, et ces deux nombres ne sont reproductibles par
                                   aucune des deux commandes du ch. 19 (avant la présente passe, elles donnaient
                                   2647 et 2226 ; les écarts, +120 et +151, ne sont pas égaux, donc les deux
                                   bases du poste 1 ne sont pas celles du ch. 19). Le poste 1 était de surcroît
                                   PÉRIMÉ depuis l'amendement du 17 juillet, qui a ajouté de la prose sans que
                                   ses décomptes soient re-posés — même faute que m-31, sur le même fichier et à
                                   la même date. Ses nombres ne sont pas rectifiés ici : on ne corrige pas un
                                   décompte vers une base qu'on ne peut pas reproduire. À trancher en gouvernance :
                                   publier la commande de ce chapitre, ou aligner le poste 1 sur les commandes du
                                   ch. 19. Les nombres de la présente passe sont, eux, accompagnés de leur commande.
                                   ⚠ SIGNALÉ, NON CORRIGÉ (hors périmètre de l'audit, règle de chirurgie) : le
                                   poste 1 porte « fait (gel : 16 juillet 2026 …) » alors que l'en-tête du chapitre
                                   porte le regel au **17 juillet 2026**. Le journal contredit l'en-tête sur la
                                   date de gel du chapitre — soit précisément la date qui commande m-30. La
                                   consigne de la présente passe interdit de toucher aux dates de gel : le point
                                   est donc porté à la gouvernance, non tranché ici. Lecture la plus probable :
                                   le poste 1 date la rédaction initiale et n'a pas été re-visité au regel.

     Arithmétique vérifiée depuis le socle :
       - 324 agents = 105 + 107 + 112 (PRD Annexe A) ; 77 sources = 23 + 25 + 29
       - 384 extraites = 115 + 124 + 145 ; 75 votées = 25 x 3 ; 69 confirmées = 22 + 25 + 22 ; 6 réfutées = 3 + 0 + 3
       - 75 / 384 = 19,5 % -> « un peu moins d'un cinquième » (384 / 5 = 76,8 > 75) — exact
       - 17 juill. 2026 -> 28 juill. 2026 = 11 jours  [RÉ-ANCRÉ le 17 juill. 2026 sur le REGEL — voir poste 6.
         Ce poste portait « 16 -> 28 = 12 jours », exact au gel initial et périmé par le regel]
       - 17 juill. 2026 -> 1er mai 2027 = 9 mois et 14 jours (288 j) -> « neuf mois et demi », « moins de dix mois »
         [RÉ-ANCRÉ ; ce poste portait « 16 juill. -> 1er mai = 9 mois et 15 jours (289 j) ». Les deux énoncés
         soutenus restent exacts : 14 j valent l'arrondi « et demi », et 9 mois 14 j < 10 mois]
       - Échéance la plus tardive du tableau §21.3 = 1er mai 2027 (F-09, F-25). Aucune entrée du socle ne porte
         d'échéance postérieure. La concentration s'énonce donc sur 9,5 mois (9 mois et 14 j depuis le regel)
         — PAS 13 (voir réfutation a ci-dessus).
       - PRD §10 : 10 lacunes (1 à 10) ; 5 portent « renvoi ch. 21 » au contrôle de couverture du TOC (10.5, 10.7, 10.8, 10.9, 10.10)
       - Décompte de la conclusion, posé sans recouvrement : 5 (10.1, 10.2, 10.3, 10.4, 10.6 — chapitre porteur unique)
         + 4 (10.7, 10.8, 10.9, 10.10 — encadré ailleurs, reprises ici) + 1 (10.5 — ch. 16, reprise ici par renvoi) = 10.
         Une première rédaction annonçait « six ... cinq » = 11 pour 10 lacunes (10.5 comptée deux fois) — corrigé.
-->
