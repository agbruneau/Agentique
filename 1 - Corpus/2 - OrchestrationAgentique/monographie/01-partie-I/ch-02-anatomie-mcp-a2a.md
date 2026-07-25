# Chapitre 2 — Anatomie technique : MCP et A2A v1.0, une complémentarité déclarée

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-01, F-02, F-03, F-16 ; F-05 (renvoi), F-15 (renvoi), F-33 (renvoi), F-43 (renvoi) |
| Garde-fous à surveiller (PRD §8) | **réserve F-01** (« cadre d'autorisation », jamais « sécurisé ») ; §8.2.1 (métriques d'adoption auto-déclarées, en renvoi au ch. 1) ; **R-8** (sigle « ACP » toujours qualifié) |
| Volumétrie cible | ~3000 mots |

> **Thèse ([TOC.md](../../TOC.md))** : « MCP dans les agents, A2A entre les agents » — la doctrine de complémentarité **déclarée par le projet A2A** (F-16) fournit le premier critère de découpage d'une architecture agentique ; elle n'est pas un accord entre les deux projets.

> ⚠ **Correctif de la rédaction (16 juill. 2026)** : la thèse de [TOC.md](../../TOC.md) portait « la doctrine **officielle** de complémentarité **structure toute** architecture agentique ». Deux écarts au socle, relevés en relecture adversariale : (1) l'attribution manquait — F-16 énonce une « doctrine officielle **du projet A2A** », et le présent chapitre établit en §2.4 qu'aucun endossement conjoint du projet MCP n'est documenté ; (2) « structure toute architecture agentique » est un universel que ni F-16 ni §2.4 ne portent — §2.4 conclut au contraire qu'« un critère n'est pas une contrainte ». La thèse est reformulée ici ; **l'amendement de TOC.md (thèse et titre du ch. 2) a été exécuté** — TOC.md porte le correctif daté du 16 juillet 2026, sur le modèle de celui du ch. 1, et le présent chapitre s'y aligne pour le titre comme pour la thèse.

---

L'architecte qui découvre MCP et A2A la même semaine pose presque toujours la même question : lequel des deux faut-il choisir ? La question est mal formée, et ce chapitre s'emploie à montrer pourquoi. Les deux protocoles ne traitent pas le même problème ; ils ne se situent même pas sur le même axe d'une architecture. Le premier organise ce qu'un agent peut faire *avec le monde* — appeler un outil, lire une donnée. Le second organise ce que des agents se disent *entre eux* — déléguer une tâche, en rendre compte. Les confondre, c'est concevoir un système où l'on ne saura plus, le jour de l'incident, si la défaillance est venue d'un outil mal borné ou d'une délégation mal cadrée.

Ce chapitre décrit donc l'anatomie technique des deux protocoles à la date de gel du présent ouvrage — le 16 juillet 2026 —, l'état de leur intégration dans les grandes plateformes infonuagiques, puis la doctrine de complémentarité qui les articule et l'exacte portée de cette doctrine. Il faut d'emblée poser un avertissement de datation : la spécification de MCP en vigueur à cette date est une révision précise, et une révision majeure était attendue douze jours plus tard. Un chapitre d'anatomie technique dans ce domaine est un instantané, et doit se lire comme tel.

## 2.1 MCP : une interface d'outillage, assortie d'un cadre d'autorisation

Le *Model Context Protocol* (MCP) a été publié par Anthropic en novembre 2024 ; sa gouvernance est passée en décembre 2025 à l'Agentic AI Foundation, épisode que le chapitre 1 retrace et sur lequel on ne revient pas[^1].

Ce que le socle de cet ouvrage établit de son anatomie tient en une phrase dense, qu'il vaut la peine de décomposer : MCP est une interface client-serveur fondée sur JSON-RPC 2.0, destinée à l'invocation d'outils et à l'échange de données typées, assortie d'un cadre d'autorisation (*authorization framework*) fondé sur OAuth[^1]. Quatre éléments, quatre conséquences d'architecture.

**Client-serveur**, d'abord. La relation est asymétrique et elle est verticale : d'un côté l'environnement du modèle, qui demande ; de l'autre le fournisseur d'outils, qui expose et exécute. Cette asymétrie n'est pas un détail d'implémentation. Elle dessine une frontière, et une frontière est précisément ce qu'une institution financière sait gouverner : on y place un contrôle, on y journalise, on y refuse. **Lecture de l'auteur** : le socle établit la relation client-serveur ; il n'établit pas que cette asymétrie constitue une frontière de contrôle gouvernable. L'inférence est d'architecture. Le chapitre 4 examine ce qui traverse cette frontière lorsqu'elle est mal tenue ; la Partie VII y installe une passerelle.

**JSON-RPC 2.0**, ensuite. Le socle nomme cette convention comme le fondement de l'échange, sans plus de détail — et il faut s'y tenir. On notera seulement, parce que la comparaison structure la suite du chapitre, que le socle ne nomme, pour MCP, que cette seule convention, là où il en documente trois pour A2A (§2.2) — l'énoncé porte sur ce que le socle documente, non sur ce que les protocoles admettent.

**L'échange de données typées**, troisième élément, est celui que les praticiens sous-estiment le plus et que les régulateurs apprécieront le plus. Un échange typé est un échange dont la forme est déclarée à l'avance, donc vérifiable à la frontière, donc opposable après coup. C'est la différence entre un journal qui atteste qu'un appel a eu lieu et un journal qui atteste *quel* appel a eu lieu, sur quelle structure de données. **Lecture de l'auteur** : le socle établit le typage comme propriété du protocole ; il n'établit pas que ce typage suffise à une piste d'audit réglementaire, et le présent ouvrage ne le prétend pas. L'inférence porte sur la nature de la propriété, non sur sa suffisance.

**Le cadre d'autorisation fondé sur OAuth**, enfin, appelle la précaution la plus stricte de ce chapitre. Le socle impose une formule et en proscrit une autre : on écrit que MCP est assorti d'un *cadre d'autorisation*, jamais qu'il est *sécurisé*[^1]. La nuance n'est pas rhétorique. Un cadre d'autorisation spécifie comment un appelant obtient des droits et comment il les présente ; il ne dit rien de la question de savoir si les droits accordés étaient les bons, si l'outil au bout de la chaîne fait ce qu'il annonce, ni si le contenu rapporté est digne de foi. Le socle documente d'ailleurs l'empoisonnement d'outils (*tool poisoning*) et l'injection d'invites (*prompt injection*) comme risques attestés — la sécurité dépend de l'implémentation, non de la spécification[^1]. Le chapitre 4 leur est consacré. Un responsable de la conformité qui verrait, dans un dossier interne, la mention « transport sécurisé par MCP » devrait la traiter comme une erreur de catégorie, et la faire corriger.

Reste la datation, qui est ici une question de fond. La révision de spécification en vigueur au 16 juillet 2026 porte l'identifiant **2025-11-25**[^1]. Une *release candidate* a été verrouillée le 21 mai 2026 et sa finalisation était prévue le **28 juillet 2026** ; elle porte une refonte sans état du protocole, le retrait de l'en-tête `Mcp-Session-Id` et l'introduction des en-têtes `Mcp-Method` et `Mcp-Name` ; les mainteneurs du projet la décrivent comme la plus importante révision depuis le lancement — qualification qu'il faut leur attribuer, puisqu'elle émane d'eux[^2]. Entre le verrouillage de cette *release candidate* et la date de finalisation annoncée s'écoulent plus de deux mois ; entre la date de gel du présent chapitre et cette même date, douze jours.

**Lecture de l'auteur** : le socle établit le contenu annoncé de cette révision et son calendrier annoncé. Il n'établit ni qu'elle sera adoptée telle quelle à la date prévue, ni ce qu'elle coûtera aux implémentations existantes. Une institution qui aurait, à la mi-2026, des serveurs MCP en exploitation devrait néanmoins inscrire cette échéance à son registre de changements plutôt que de l'apprendre de son fournisseur. Le présent chapitre est explicitement placé sous réserve de revalidation sur ce point, et le registre de gel de l'ouvrage le consigne.

## 2.2 A2A v1.0 : la délégation entre pairs

A2A (*Agent2Agent*) a été lancé par Google en avril 2025 et transféré à la Linux Foundation en juin 2025 sous licence Apache 2.0[^3]. Là encore, la généalogie relève du chapitre 1 ; c'est l'anatomie qui nous occupe.

A2A traite un problème que MCP ne traite pas : la délégation de tâches de pair à pair entre agents, au moyen de descripteurs appelés cartes d'agents (*Agent Cards*)[^3]. Le mot « pair » porte tout le poids. Il n'y a plus ici de client et de serveur au sens de la section précédente, mais des agents dont chacun peut, selon le moment, demander ou répondre. L'axe est horizontal.

La version 1.0 est, selon le socle, la première spécification stable du protocole ; le projet la qualifie lui-même de « *production-ready* »[^3]. Cette dernière expression appelle la même sévérité que les métriques d'adoption examinées au chapitre 1 : c'est le projet A2A qui juge sa propre spécification prête pour la production, et l'ouvrage l'attribue comme tel à chaque emploi. La qualification décrit une intention de stabilité de la part des mainteneurs, non un constat de déploiement vérifié par un tiers.

Trois propriétés distinguent cette version 1.0, et le socle les nomme précisément : elle est **multi-protocole** — JSON sur HTTP, gRPC et JSON-RPC —, elle offre la **multi-location d'entreprise** (*enterprise multi-tenancy*), et elle introduit les **cartes d'agents signées** (*Signed Agent Cards*), c'est-à-dire une vérification cryptographique d'identité[^3].

La première propriété mérite d'être rapprochée de la section précédente. MCP repose sur JSON-RPC 2.0 ; A2A offre JSON-RPC parmi trois liaisons possibles. **Lecture de l'auteur** : pour l'architecte, cette pluralité est un avantage d'intégration et une charge de gouvernance. Un avantage, parce qu'elle laisse choisir la liaison qui s'accorde au parc existant ; une charge, parce que trois liaisons signifient trois surfaces à instrumenter, à journaliser et à inspecter, là où une seule aurait suffi. Le socle établit la pluralité ; il n'établit ni cet avantage ni cette charge, qui sont une lecture d'architecture.

La deuxième propriété, la multi-location d'entreprise, appelle une honnêteté particulière. Le socle la nomme comme un attribut de la version 1.0 ; il n'en détaille ni le mécanisme, ni le périmètre, ni les garanties d'isolation qu'elle procure[^3]. On se gardera donc de la commenter au-delà de ce que la source porte. Ce qui peut être dit sans excéder le socle tient en ceci : la spécification déclare prendre en charge un mode de déploiement propre aux organisations, ce qui est une indication sur les publics que le projet vise, non une garantie technique dont une institution pourrait se prévaloir dans un dossier. La différence entre une propriété annoncée et une propriété qualifiée est exactement celle qu'une revue d'architecture est faite pour établir ; elle ne peut l'être ici.

La troisième propriété est celle qui devrait retenir un responsable du risque. Une carte d'agent signée permet de vérifier cryptographiquement l'identité de l'agent qu'elle décrit[^3]. **Lecture de l'auteur** : le socle établit la vérification cryptographique d'identité ; qu'elle constitue un progrès net sur un descripteur non signé, et que l'écosystème agentique en ait besoin faute de pouvoir vérifier les capacités annoncées, sont des lectures d'architecture. Mais il faut dire aussi, et surtout, ce que le socle *ne* documente pas : ni l'ancrage de confiance dont ces signatures dépendent, ni les mécanismes de révocation, ni la gouvernance des clés. Ces trois questions décident, en pratique, de la valeur d'une signature ; le présent ouvrage ne peut y répondre depuis son socle et ne les tranchera pas. Le chapitre 8 examine ce que les travaux d'identité et de registres d'agents apportent sur ce terrain — travaux dont on verra qu'ils sont, à la date de gel, largement pré-normatifs.

Un mot sur la ligne de version. La version courante au 16 juillet 2026 demeure la ligne 1.0, dont l'étiquette v1.0.1 — correctifs mineurs — est datée du 28 mai 2026[^2]. Le socle ne date pas la publication de la v1.0 elle-même ; l'ouvrage s'abstient donc de la dater. Quant à la gouvernance du protocole, à la composition de son comité de pilotage technique et au décompte des organisations qui déclarent leur soutien, le chapitre 1 les traite et en établit la portée exacte ; on n'y revient pas ici[^4].

## 2.3 Les intégrations infonuagiques : lire le statut, pas la présence

Un protocole ouvert ne vaut, pour une institution, que par les plateformes qui l'implémentent. Sur ce point le socle documente A2A avec précision, et il faut d'abord relever une asymétrie : cette précision porte sur A2A.

L'état documenté au printemps 2026 est le suivant. Chez Microsoft, A2A est intégré à Azure AI Foundry en **préversion**, et à Copilot Studio en **disponibilité générale depuis avril 2026** (statuts documentés par les sources d'avril 2026, non revalidés à la date de gel — voir [^5]). Chez Amazon, l'intégration est portée par AWS Bedrock AgentCore Runtime. Chez Google, elle est d'origine, le protocole y étant né[^5].

Cet inventaire dit deux choses. La première est que les trois grands fournisseurs d'infonuagique public implémentent A2A, et que les trois siègent au comité de pilotage technique du protocole (ch. 1). **Lecture de l'auteur** : le socle établit les intégrations et la composition du comité ; la convergence qu'on y lit — et son caractère peu commun dans un marché disputé — est une inférence d'architecture, non un fait documenté.

La seconde est plus utile encore à qui prépare un dossier : **les statuts diffèrent**, et la différence est celle qui compte. Une préversion et une disponibilité générale n'engagent pas le fournisseur au même degré, n'offrent pas les mêmes garanties de service et ne se défendent pas de la même façon devant une seconde ligne de défense. **Lecture de l'auteur** : le socle établit les statuts, pas ce qu'ils emportent. Que préversion et disponibilité générale n'engagent pas le fournisseur au même degré est une inférence d'architecture ; l'ouvrage ne documente ni les garanties de service attachées à chaque statut, ni leur réception par une seconde ligne de défense. Ce qui découle du fait, en revanche, tient en une consigne : le socle datant explicitement la disponibilité générale de Copilot Studio — avril 2026 — et laissant Azure AI Foundry en préversion, l'architecte prudent lira le statut avant de lire la marque.

Il faut enfin nommer une limite de ce chapitre, plutôt que la laisser se combler par le silence. Le socle fournit cet inventaire d'intégrations pour A2A ; il ne fournit pas d'inventaire équivalent, plateforme par plateforme et statut par statut, pour MCP. Ce que le socle documente du support de MCP se trouve du côté des cadriciels d'orchestration — support MCP natif du cadriciel de Microsoft, appel d'outils par MCP déclaré nativement dans l'offre événementielle de Confluent — et relève du chapitre 7, qui les traite avec leurs réserves respectives. L'absence d'un inventaire infonuagique de MCP dans le socle **n'établit pas** l'absence d'un tel support : elle établit que le présent ouvrage ne peut pas en dresser la carte. La distinction est celle entre ce qui n'existe pas et ce qui n'a pas été vérifié ; cet ouvrage s'astreint à ne jamais la franchir.

## 2.4 La complémentarité en pratique : ce que la doctrine dit, et qui la dit

Reste la doctrine qui donne son titre au chapitre. Elle est explicite, et le socle en conserve la formulation d'origine : A2A est « *Complementary to MCP, not a replacement* » — complémentaire à MCP, non un remplacement[^6]. La répartition est énoncée sans ambiguïté : MCP pour l'intégration des outils et du contexte au niveau de l'agent individuel, A2A pour la communication et la coordination entre agents ; le positionnement officiel se résume dans la formule « MCP dans les agents, A2A entre les agents »[^3][^6]. Le socle ajoute que de nombreux systèmes utilisent les deux[^6].

Deux précisions d'attribution s'imposent, et elles sont le cœur de cette section.

La première : **cette doctrine est celle du projet A2A**. Le socle la trace au site du protocole A2A, dans l'annonce de sa version 1.0[^6]. Elle n'est pas un accord conjoint publié par les deux projets, et l'ouvrage ne dispose d'aucune source établissant que le projet MCP l'a endossée dans ces termes. Cela n'en diminue pas la valeur — une déclaration publique de non-remplacement est un engagement que les spécifications ultérieures pourront confirmer ou démentir ; l'ouvrage ne procède pas à cet examen —, mais cela en fixe le statut : c'est une position déclarée par une partie, non un traité entre deux parties.

La seconde : la formule « de nombreux systèmes utilisent les deux » n'est pas une métrique. Elle n'est ni chiffrée, ni datée, ni définie, et elle émane du projet A2A[^6]. Elle établit que la combinaison des deux protocoles est prévue et revendiquée par les mainteneurs ; elle n'établit aucun volume de déploiement. Le lecteur reconnaîtra ici la réserve centrale du chapitre 1 — le soutien déclaré ne vaut pas déploiement en production — dans une variante plus discrète, et pour cela plus insidieuse.

Ces réserves posées, que retenir de la doctrine ? **Lecture de l'auteur** : sa valeur pour l'architecte n'est pas descriptive mais prescriptive. Elle fournit un critère de découpage — l'accès aux outils relève de MCP, la délégation entre agents relève d'A2A — et un critère de découpage est ce dont manque cruellement une organisation qui débute. Mais un critère n'est pas une contrainte. Rien, dans les protocoles eux-mêmes tels que le socle les documente, n'empêche une équipe de faire transiter par des appels d'outils ce qui est en réalité une délégation entre agents, ou l'inverse. La frontière entre les deux axes est une décision d'architecture que l'organisation doit prendre, documenter et défendre — elle n'est pas donnée par la technique.

C'est pourquoi cette doctrine, malgré son air de slogan, mérite le rang que la thèse de ce chapitre lui accorde. **Toujours en lecture de l'auteur** : elle est le découpage le plus simple dont dispose une organisation qui débute, et le seul que le socle rattache à l'un des deux projets eux-mêmes. Elle n'est pas le seul disponible, et il serait malhonnête de le laisser croire : le socle documente au moins deux autres manières de découper ce même espace — la feuille de route séquentielle en quatre protocoles du survey d'Ehtesham et al. (mai 2025), antérieure, dont le chapitre 1 a montré que la deuxième étape est devenue obsolète comme prescription[^7] ; et le positionnement d'AGNTCY en couche d'infrastructure — annuaires de découverte, transport SLIM — déclarée interopérable avec A2A et MCP, donc articulant l'espace par les couches plutôt que par les axes, et que le chapitre 3 examine[^8]. Que ces découpages soient moins commodes ou datés est défendable ; qu'ils n'existent pas ne l'est pas. Les Parties II et VI font de la doctrine un usage constant : la position d'un système sur les options d'orchestration (ch. 5), le tracé des points de contrôle obligatoires (ch. 19) et la matrice protocoles × exigences réglementaires (ch. 18) supposent tous que l'on sache dire, d'un flux donné, s'il traverse la frontière verticale ou l'horizontale.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, MCP et A2A répondent à des questions distinctes, sur des axes distincts : l'un régit la relation client-serveur d'un agent à ses outils, sur JSON-RPC 2.0 et avec un cadre d'autorisation fondé sur OAuth ; l'autre régit la délégation entre pairs, sur trois liaisons possibles, avec des cartes d'agents dont la variante signée porte une vérification cryptographique d'identité. **Deuxièmement**, la complémentarité n'est pas une interprétation de commentateurs : c'est la doctrine officielle du projet A2A, publiée dans l'annonce de sa version 1.0 — et c'est, précisément, la doctrine d'*un* des deux projets. **Troisièmement**, les trois grands fournisseurs d'infonuagique public implémentent A2A, à des statuts qui ne sont pas équivalents et qu'il faut lire avant la marque.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas que MCP est sécurisé : il dit que MCP porte un cadre d'autorisation, ce qui n'est pas la même chose, et le chapitre 4 documente ce que le protocole ne couvre pas. Il ne dit pas que la signature des cartes d'agents règle la question de l'identité : le socle n'établit ni l'ancrage de confiance, ni la révocation, ni la gouvernance des clés, et le chapitre 8 montrera que le terrain reste largement pré-normatif. Il ne dresse pas la carte du support de MCP dans les plateformes infonuagiques, faute de socle — et se garde d'en conclure quoi que ce soit. Il ne traite ni d'AP2, ni d'AGNTCY, ni du destin de l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI), qui relèvent du chapitre 3.

Il ne dit pas, enfin, que cet état des lieux tiendra. Douze jours après la date de gel de ce chapitre, MCP devait recevoir la révision que ses mainteneurs décrivent comme la plus importante depuis son lancement. L'anatomie décrite ici est datée du 16 juillet 2026, et c'est à cette date seule qu'elle engage l'ouvrage.

---

## Notes

[^1]: PRD §7.1, **F-01** (niveau [A]). Sources primaires : spécification MCP, révision **2025-11-25** (modelcontextprotocol.io), revalidée le 16 juillet 2026 ; annonce Anthropic de novembre 2024 ; arXiv 2505.02279 (avec la réserve F-06). **Réserve F-01 appliquée dans tout ce chapitre** : la formule retenue est « cadre d'autorisation » et non « sécurisé » — la sécurité dépend de l'implémentation (empoisonnement d'outils et injection d'invites documentés ; voir ch. 4). Formes imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.3 et §D.7.

[^2]: PRD §7.1, **F-01** (fait chaud, P4.1) et confirmation de la ligne de version d'A2A : rapport de revalidation `verification/revalidation-2026-07-16.md`, ligne 5, d'après blog.modelcontextprotocol.io (*release candidate* verrouillée le 21 mai 2026 ; refonte sans état, retrait de `Mcp-Session-Id`, en-têtes `Mcp-Method`/`Mcp-Name` ; finalisation annoncée au 28 juillet 2026) et github.com/a2aproject/A2A/releases (étiquette v1.0.1, correctifs mineurs, 28 mai 2026). La qualification « plus importante révision depuis le lancement » est **celle des mainteneurs du projet MCP** et leur est attribuée. **Point de revalidation obligatoire (PRDPlan P4.1)** : la révision du 28 juillet 2026 est postérieure à la date de gel du présent chapitre.

[^3]: PRD §7.1, **F-02** (niveau [A]). Sources primaires : a2a-protocol.org/latest/announcing-1.0 ; communiqué de la Linux Foundation du 9 avril 2026 ; `GOVERNANCE.md` du dépôt a2aproject/A2A. Le qualificatif « production-ready » est **celui du projet A2A** et lui est attribué à chaque occurrence. Le socle ne date pas la publication de la v1.0 ; il ne documente pas non plus l'ancrage de confiance, la révocation ni la gouvernance des clés des *Signed Agent Cards*.

[^4]: PRD §8.2.1 (attribution des métriques d'adoption des protocoles) ; formulation imposée par PRDPlan §4.4 (« soutien ≠ production »). La lecture critique du décompte des organisations de soutien et de la composition du comité de pilotage technique d'A2A est établie au **ch. 1 §1.2 et §1.3** ; le présent chapitre y renvoie sans la dupliquer.

[^5]: PRD §7.1, **F-03** (niveau [A]). Sources primaires : documentation AWS (Bedrock AgentCore Runtime) et Microsoft Learn (Azure AI Foundry, Copilot Studio) ; communiqué de la Linux Foundation d'avril 2026. Le socle documente ces intégrations **pour A2A** ; il ne fournit pas d'inventaire infonuagique équivalent pour MCP — le support de MCP par les cadriciels d'orchestration relève du **ch. 7** (F-15, F-33, avec leurs réserves de statut). **Point de revalidation obligatoire (PRDPlan P4.1)** : les statuts de F-03 reposent sur des sources d'**avril 2026** et **n'étaient pas au périmètre de la passe P0.1 du 16 juillet 2026** (`verification/revalidation-2026-07-16.md`, ligne 5 — laquelle ne couvre que les versions et la gouvernance de MCP/A2A). Le statut « préversion » d'Azure AI Foundry est le plus volatil de la section : à revalider en P4.1 au même titre que la révision de spécification MCP.

[^6]: PRD §7.6, **F-16** (niveau [A]). Source primaire : a2a-protocol.org/latest/announcing-1.0, citation verbatim « Complementary to MCP, not a replacement ». **Attribution** : cette doctrine est celle du **projet A2A** ; le socle ne documente aucun endossement conjoint par le projet MCP. La formule « de nombreux systèmes utilisent les deux » est un énoncé non chiffré, non daté et non défini du projet A2A — elle n'établit aucun volume de déploiement.

[^7]: PRD §7.1, **F-06** (confiance moyenne — usage descriptif seulement). Ehtesham et al., arXiv 2505.02279, mai 2025. **Réserve majeure** : préprint non révisé par les pairs, dont la deuxième étape est devenue obsolète comme prescription après la fusion d'août 2025 (F-43, R-1). Cité ici, comme au **ch. 1**, en jalon historiographique — pour établir qu'un autre découpage de l'espace de conception a existé, jamais comme guidance.

[^8]: PRD §7.1, **F-05** (niveau [A]). Source primaire : communiqué de la Linux Foundation du 29 juillet 2025. AGNTCY est documenté comme **couche d'infrastructure** (annuaires de découverte, transport SLIM) interopérable avec A2A et MCP — positionnement officiel non concurrent, développé au **ch. 3**. Renvoi de périmètre : le présent chapitre ne s'en sert que pour établir l'existence d'un découpage concurrent de l'espace de conception, sans en juger.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps = 3 049 mots après relecture — décompte outillé,
                                   cible 3 000 ±10 % soit 2 700-3 300 : conforme)
     2. Traçabilité (CA-1, CA-5) . fait (8 notes ; en-tête complété de F-15 et F-33 (renvois) — le corps mobilise leurs
                                   faits en §2.3, l'omission aurait fait échouer le contrôle P4.3 ; termes anglais entre
                                   parenthèses et en italique à la 1re occurrence : Model Context Protocol,
                                   authorization framework, tool poisoning, prompt injection, Agent2Agent, Agent Cards,
                                   enterprise multi-tenancy, Signed Agent Cards, production-ready, release candidate,
                                   Agent Communication Protocol)
     3. Balayage garde-fous ...... fait (réserve F-01 : « sécurisé » n'apparaît qu'en négation explicite, §2.1 et conclusion ;
                                   §8.2.1 : métriques d'adoption non reprises ici, renvoi au ch. 1 ; R-8 : sigle « ACP » employé
                                   une seule fois dans le corps, sous la forme imposée §D.1 « l'ACP protocolaire
                                   (*Agent Communication Protocol*, IBM Research/BeeAI) », en renvoi au ch. 3 ;
                                   R-4/R-5/R-6/R-7 : sans objet dans ce chapitre)
     4. Relecture adversariale ... fait (deux relecteurs distincts — PRDPlan §4.2.4 ; 3 réfutations bloquantes + 11 réserves,
                                   toutes fondées, toutes corrigées. RÉFUTÉ = le motif « ce qu'une structure signifie »
                                   (PRD §13) : trois inférences d'architecture étaient données pour des faits du socle —
                                   l'asymétrie client-serveur comme « frontière gouvernable » (§2.1), la « convergence
                                   peu commune » lue dans F-03+F-02 (§2.3), et surtout ce qu'un statut « emporte » en
                                   engagement fournisseur / garanties de service / défendabilité devant une 2e ligne (§2.3),
                                   alors que F-03 ne nomme que des statuts — le tout dans un chapitre qui s'interdit
                                   explicitement ce geste et marquait déjà d'autres inférences de portée identique.
                                   Les trois portent désormais leur « Lecture de l'auteur » (8 marquages au total).
                                   Corrigé aussi : « dès l'origine du protocole » (datation absente de F-01, venue de la
                                   thèse du ch. 4 dans TOC.md — le TOC n'est pas l'autorité factuelle) ; l'exclusivité
                                   « unique convention » (argument du silence contredisant la règle posée deux phrases
                                   plus haut ; F-01 mentionne d'ailleurs `Mcp-Session-Id`) ; l'« obligation vérifiable
                                   dans les spécifications successives » d'A2A (vérifiabilité non établie, examen non fait) ;
                                   les absolus « premier découpage » / « n'en aurait aucun » (F-05 et F-06 documentent
                                   deux autres découpages — désormais exposés) ; statuts F-03 datés dans le corps et
                                   signalés hors périmètre de la passe P0.1 (note [^5]) ; CA-5 sur multi-location ;
                                   forme §D.1 de l'ACP ; en-tête complété (F-15, F-33).
                                   Thèse reformulée (attribution au projet A2A + retrait de l'universel « structure toute
                                   architecture agentique ») — amendement de TOC.md exécuté (thèse et titre du ch. 2,
                                   correctif daté du 16 juill. 2026), sur le modèle du correctif du ch. 1. Voir le
                                   correctif de rédaction en tête de chapitre.
     5. Commit + registre de gel . fait (ligne du ch. 2 au registre `99-registre-gel.md`, commit `eb21ab3` ; point de
                                   revalidation P4.1 « révision MCP du 28 juillet 2026 » inscrit à la table du registre)
     6. Passe de conformité (audit du 17 juill. 2026 — aucune information nouvelle, date de gel inchangée) :
        m-05 — titre H1 « deux protocoles complémentaires » -> « une complémentarité déclarée » : alignement sur
               TOC.md, qui fait autorité sur le découpage et porte le titre amendé depuis le 16 juill. 2026.
        m-06 — bannière de correctif : « l'amendement de TOC.md reste dû » était un statut périmé (l'amendement est
               fait, TOC.md le date du 16 juill. 2026) ; datée comme exécutée.
        m-07 — bloc « 5. Commit + registre de gel : À FAIRE » périmé (le chapitre est enregistré au registre,
               commit `eb21ab3`) ; corrigé.
        ⚠ DETTE OUVERTE, signalée au parent et NON corrigée ici (le registre est hors périmètre de cette passe) :
        le SECOND point de revalidation P4.1 que ce chapitre exige — statuts d'intégration infonuagique de F-03
        (sources d'avril 2026, hors périmètre de la passe P0.1 du 16 juill. 2026 ; « préversion » d'Azure AI Foundry,
        le plus volatil, voir note [^5]) — est ABSENT de la table « Points de revalidation ouverts (P4.1) » de
        `99-registre-gel.md`. À inscrire au registre.
     Dette de glossaire (hors périmètre de cette passe — ne pas toucher au glossaire ici) :
     ajouter « multi-location d'entreprise / enterprise multi-tenancy » à §D.3 avec sa trace F-02.
-->
