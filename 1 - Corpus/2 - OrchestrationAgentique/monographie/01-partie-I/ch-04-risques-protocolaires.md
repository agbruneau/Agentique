# Chapitre 4 — Taxonomie des risques protocolaires

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-01 (et sa réserve), F-02, F-36 (défi C2 ; opérationnalisation locale des *frames*) |
| Garde-fous à surveiller (PRD §8) | **réserve F-01** — « cadre d'autorisation », jamais « sécurisé » : chapitre où le motif est le plus probable ; §8.2 (principe général d'attribution — qualification « production-ready » attribuée à l'annonce du projet A2A) ; R-8 (aucune occurrence du sigle nu ni de *control plane* ; seule mention en note [^3], qualifiée selon la forme imposée, Annexe D §D.1 branche (a)) |
| Volumétrie cible | ~2600 mots |

> **Thèse ([TOC.md](../../TOC.md))** : La sécurité des protocoles dépend de l'implémentation ; empoisonnement d'outils et injection d'invites sont **nommés par les protocoles eux-mêmes comme risques attachés**, sans que le socle en date la documentation ni en établisse la mécanique.

---

Les trois chapitres précédents ont établi que la couche protocolaire agentique était sortie du régime propriétaire, qu'elle reposait sur une doctrine de complémentarité explicite et qu'elle s'était dotée d'une couche d'infrastructure. Aucun de ces acquis ne dit quoi que ce soit de sa sûreté. C'est l'objet du présent chapitre, et il faut en énoncer d'emblée la conclusion, parce qu'elle contredit une attente répandue : **un protocole d'interopérabilité agentique ne constitue pas, à lui seul, une posture de sécurité**. Il définit un format d'échange et un cadre d'autorisation (*authorization framework*) ; ce qui se passe à l'intérieur de ce cadre relève de celui qui l'implémente.

Cette proposition n'est pas une opinion de l'auteur. Elle est inscrite dans le socle de cet ouvrage comme une réserve de rédaction contraignante : à propos de MCP, il faut écrire « cadre d'autorisation » et jamais « sécurisé », parce que la sécurité dépend de l'implémentation — et le socle cite, à l'appui de cette réserve, deux catégories d'attaques documentées, l'empoisonnement d'outils (*tool poisoning*) et l'injection d'invites (*prompt injection*)[^1]. Le chapitre déplie cette réserve : d'abord la surface d'attaque que les protocoles ouvrent (4.1), puis ce que leurs spécifications apportent en réponse (4.2), enfin ce qu'elles laissent, par construction, à l'architecture (4.3).

## 4.1 La surface d'attaque : outils, invites, mémoire

Trois surfaces se dégagent du socle. Elles ne sont pas de même nature, et c'est précisément ce qui rend leur traitement difficile.

La première est celle des **outils**. Elle est indissociable de la raison d'être de MCP : le protocole existe pour qu'un modèle invoque des outils et échange des données typées avec son environnement, au moyen d'une interface client-serveur fondée sur JSON-RPC 2.0[^1]. Le socle **nomme**, comme risque attaché à ce protocole, l'**empoisonnement d'outils** (*tool poisoning*) — et il s'arrête au nom : il n'en porte ni la mécanique, ni l'identifiant de vulnérabilité, ni l'incident daté[^2]. **Lecture de l'auteur** — le lecteur peut entendre, sous ce nom, le détournement d'un outil exposé à un agent ; c'est la lecture de l'auteur, non une définition du socle, et le glossaire de cet ouvrage a retiré la sienne le 17 juillet 2026 pour cette raison même. Le socle ne caractérise pas davantage le rapport entre cette surface et la fonction du protocole. On peut noter qu'un agent privé de toute invocation d'outil sort du périmètre fonctionnel de MCP : la surface n'est alors pas un défaut d'implémentation situé à côté de la fonction, elle en est le corollaire. Le rapprochement est de l'auteur.

La deuxième est celle des **invites**. L'**injection d'invites** (*prompt injection*) est, elle aussi, un nom que le socle porte sans le caractériser — **Lecture de l'auteur** : on peut y entendre l'introduction d'instructions dans le contexte d'un agent, mais le socle ne l'établit pas et le glossaire n'en porte plus de glose[^2]. Le socle la nomme à deux endroits : dans la réserve de caractérisation de F-01, attachée à MCP[^1], et au titre du défi de **sécurité holistique** (défi C2) du manifeste de recherche sur l'*Agentic Business Process Management*, texte à dix-huit auteurs issu d'un séminaire Dagstuhl[^3]. **Lecture de l'auteur** — l'indépendance de ces deux mentions n'est pas établie par le socle et n'est pas revendiquée ici, pour deux raisons. D'une part, le socle n'indique pas laquelle des trois sources de F-01 (spécification MCP, annonce Anthropic, arXiv 2505.02279) documente l'attaque. D'autre part, F-36 signale que le manifeste cite MCP parmi les protocoles d'interopérabilité : le second corpus commente le premier, et une reprise n'est pas une corroboration croisée. Ce que le socle porte est plus simple : le risque est nommé deux fois, et une fois suffit à interdire d'écrire qu'un protocole est « sécurisé ».

La troisième est celle de la **mémoire**. L'**empoisonnement de mémoire** (*memory poisoning*) n'est documenté au socle que par le manifeste APM, au titre du même défi C2[^3]. Le socle le **nomme**, et s'arrête là : il n'en porte aucune caractérisation — ni ce que cette mémoire recouvre, ni la mécanique de sa corruption, ni la portée temporelle de l'atteinte. Cette troisième surface est donc la moins documentée des trois, et c'est tout ce que le présent chapitre peut en dire. Un lecteur tenté d'en déduire la gravité — pour une institution financière, la question de savoir si une mémoire corrompue relève de l'incident ponctuel ou du vice latent n'est pas mince — doit savoir qu'il la déduirait de ce que le socle ne porte pas.

Une asymétrie doit être signalée avant d'aller plus loin, car elle serait autrement lue à l'envers. Les trois risques que le socle nomme sont attachés, pour deux d'entre eux, à MCP par la réserve de caractérisation de son entrée[^1], et pour le troisième au manifeste APM traitant des systèmes agentiques en général[^3]. **Aucune attaque propre à A2A n'est documentée par le socle de cet ouvrage**, alors même qu'A2A ouvre une surface d'une autre nature — la délégation de tâches de pair à pair entre agents[^4]. Ce silence est une propriété du socle, non une propriété du protocole : il faut le lire comme une limite de la documentation rassemblée ici, en aucun cas comme un certificat de sûreté. Un architecte qui conclurait d'un chapitre où A2A est peu mis en cause qu'A2A est moins exposé aurait commis, à partir d'un texte prudent, exactement l'erreur que ce texte cherche à prévenir.

Le manifeste APM ne se contente pas d'énumérer ces surfaces : il qualifie le défi d'**holistique**, et adjoint à la liste deux éléments que le vocabulaire habituel de la sécurité applicative ne prépare pas à recevoir. Le premier est le **paradoxe de confidentialité** de l'explicabilité : la capacité d'expliquer une décision agentique, que les auteurs relient explicitement à la conformité réglementaire — ils citent le Règlement général sur la protection des données et l'*AI Act* européen, et rangent la finance parmi les domaines à haut risque — entre en tension avec la protection des données que l'explication doit exposer pour être une explication[^3]. Le second est une paire de patrons de conception, *Action-Selector* et *Plan-Then-Execute*, que le manifeste cite au titre de la sécurité holistique[^3]. **Le socle de cet ouvrage nomme ces deux patrons sans en documenter la mécanique** ; ils sont donc mentionnés ici pour ce qu'ils sont — des pistes que la littérature académique verse au dossier — et ne sont pas décrits.

**Lecture de l'auteur** — le socle établit l'existence et le nom de ces trois surfaces, ainsi que le caractère holistique du défi ; il n'établit pas la typologie qui suit. Ces trois surfaces se distinguent par ce qu'elles corrompent : l'outil corrompt la *capacité* de l'agent, l'invite corrompt son *instruction*, la mémoire corrompt son *état*. Aucun contrôle ne les couvre ensemble, parce qu'aucune de ces trois choses ne circule par le même canal. C'est, en une phrase, ce que le manifeste APM veut dire par « holistique » : le problème ne se découpe pas selon les frontières que l'ingénierie de la sécurité applicative a l'habitude de tracer.

> **État de la recherche — la mécanique des attaques protocolaires**
>
> Question : par quels mécanismes précis un empoisonnement d'outils ou une injection d'invites s'exécute-t-il contre une implémentation MCP ou A2A, et quels incidents publics les attestent ?
>
> Le socle de cet ouvrage (PRD §7.1, F-01 ; §7.7, F-36) **nomme** ces risques et les tient pour documentés ; il ne verse au dossier **aucune source primaire consacrée à leur mécanique**, aucun identifiant de vulnérabilité, aucun incident public daté, et **aucune date à laquelle cette documentation serait apparue**. La thèse de ce chapitre, telle que la table des matières la formulait, comportait la mention « dès l'origine » : cette datation n'étant pas portée par le socle, elle a été retirée du plan par correctif du 16 juillet 2026 (TOC v1.3), et le présent chapitre ne l'affirme pas.
>
> **Lacune ouverte le 16 juillet 2026** (PRD §10.8) ; **aucune passe de recherche n'a été conduite** — aucune passe de recherche externe n'a été conduite à ce lot, et la mécanique de ces attaques est hors du périmètre des sources versées au socle : celles-ci documentent un protocole et un programme de recherche, non une analyse de menaces. Sources à retrouver, telles que le PRD les identifie : spécification MCP (section sécurité), a2a-protocol.org, défi C2 de F-36 par relecture du PDF présent au dépôt.
>
> **La question reste ouverte** ; aucune inférence n'est proposée ici. Ce que le socle autorise est exactement ceci : ces risques sont nommés, ils sont attachés à ces protocoles par leurs propres réserves de caractérisation, et ils suffisent à interdire d'écrire qu'un protocole est « sécurisé ». Un lecteur qui aurait besoin de la mécanique — pour construire un plan de tests d'intrusion, par exemple — doit la chercher hors de cet ouvrage.

## 4.2 Les réponses protocolaires : ce que les spécifications apportent

Les protocoles ne sont pas muets sur le sujet. Ils apportent des réponses réelles, et il serait aussi malhonnête de les taire que de les surqualifier.

MCP porte un **cadre d'autorisation fondé sur OAuth**[^1]. La formulation est celle que le socle impose, et sa précision est le fond de l'affaire. **Lecture de l'auteur** — le socle établit que MCP porte un cadre d'autorisation fondé sur OAuth ; il ne documente ni la sémantique d'OAuth ni ses limites. L'auteur retient qu'un cadre de délégation d'autorisation établit l'habilitation d'un appelant, non le contenu ni le bien-fondé de ce qu'il demande, ni le fait que l'outil invoqué soit celui qu'il prétend être.

A2A v1.0 apporte les **cartes d'agents signées** (*Signed Agent Cards*), qui adjoignent au descripteur d'agent une vérification cryptographique d'identité[^4] ; le projet qualifie cette version de première spécification stable et « production-ready » — qualification de l'annonce du projet A2A elle-même, non d'un tiers évaluateur[^4]. Le reste de l'anatomie de la v1.0 — support multi-protocole, multi-location d'entreprise — relève du chapitre 2.

Il faut être exact sur le statut de ces deux réponses. Le socle documente leur **existence** dans la spécification v1.0 et dans celle de MCP ; il ne documente ni leurs propriétés de résistance, ni le détail de leur mise en œuvre[^1][^4]. Ce qu'un mécanisme dont le socle atteste la seule présence garantit — ou non — face aux surfaces de la section précédente ne figure nulle part dans le socle de cet ouvrage, et ne sera donc pas affirmé ici.

**Lecture de l'auteur** — le socle documente ces mécanismes ; il ne formule pas la limite qui suit. Ces deux réponses répondent à la même question, et ce n'est pas la question des attaques de la section précédente. Le cadre d'autorisation de MCP et la carte d'agent signée d'A2A établissent tous deux **qui** parle. Ils n'établissent ni ce qui est dit, ni si ce qui est dit est fondé. Un agent dont l'identité est cryptographiquement vérifiée et dont l'habilitation est en règle demeure exactement aussi dangereux que ses instructions, si ces instructions ont été injectées, et exactement aussi fiable que sa mémoire, si cette mémoire a été corrompue. L'authentification est une condition nécessaire de la confiance ; le socle n'en fait pas — et cet ouvrage n'en fera pas — une condition suffisante.

Il faut ajouter une remarque de datation, car un chapitre sur les risques d'un protocole vieillit à la vitesse de sa spécification. La révision de MCP en vigueur à la date de gel du présent chapitre porte le numéro 2025-11-25 ; une révision majeure — décrite par les mainteneurs comme la plus importante depuis le lancement du protocole, avec une refonte sans état et le retrait de l'en-tête `Mcp-Session-Id` — était prévue en finalisation le 28 juillet 2026, soit douze jours après cette date de gel[^1]. Le chapitre 2 en traite au titre de l'anatomie technique. On se gardera ici d'anticiper ses effets sur la surface d'attaque : le socle documente le changement, non ses conséquences, et une révision de cette ampleur est précisément le genre d'événement qui commande la revalidation prévue avant publication.

Enfin, un rappel qui n'est pas de pure forme : le passage de ces protocoles sous gouvernance neutre, établi au chapitre 1, ne change rien à ce qui précède. **Lecture de l'auteur** — le socle documente les transferts de gouvernance (F-01, F-02) ; il n'énonce aucun rapport entre gouvernance et sûreté. L'auteur retient qu'une fondation ne durcit pas une implémentation, et que confondre la consolidation institutionnelle avec la sûreté technique serait, pour une institution financière, le type même de raccourci qu'un dossier de risque de tiers ne devrait pas laisser passer.

## 4.3 Ce que les protocoles ne couvrent pas

Si les spécifications répondent à la question de l'identité et de l'habilitation, la question du contenu et de l'état reste entière. Le socle indique où elle se traite, et la réponse n'est pas protocolaire.

Le manifeste APM propose l'opérationnalisation **locale** des *frames* comme **frontière de sécurité et de confidentialité** : restreindre le contexte et les capacités de chaque agent limite l'impact d'un agent compromis[^3]. La proposition mérite d'être lue lentement, car elle renverse l'ordre habituel du raisonnement. Elle ne cherche pas à empêcher la compromission — elle en borne le rayon. Elle ne suppose pas que les surfaces de la section 4.1 soient refermables ; elle suppose au contraire qu'elles ne le sont pas, et déplace la question de la prévention vers le confinement.

**Lecture de l'auteur** — c'est ici que ce chapitre rejoint la thèse de l'ouvrage, et il faut dire précisément ce que le socle porte et ce qu'il ne porte pas. Le socle établit que le manifeste APM propose les *frames* locaux comme frontière de sécurité, et il établit par ailleurs que l'autonomie encadrée (*framed autonomy*) — dont ces mêmes *frames*, normatifs et opérationnels, sont le dispositif — est le mécanisme premier de gouvernance des systèmes agentiques[^3]. Il n'établit pas que l'encadrement soit une réponse *suffisante* aux trois surfaces d'attaque, et cet ouvrage ne l'affirmera pas. Ce que l'on peut retenir est plus modeste et plus solide : le même dispositif que la Partie II présentera comme instrument de gouvernance de l'autonomie est, chez ses propres auteurs, un instrument de confinement du compromis. Le chapitre 6 le développe ; le chapitre 5 en donne la taxonomie ; le chapitre 13 en tire les conséquences réglementaires canadiennes.

Ce déplacement a un prix conceptuel qu'il faut assumer. Une frontière de confinement suppose que l'on ait décidé, en amont, quel contexte et quelles capacités chaque agent reçoit — c'est-à-dire que l'on ait spécifié le *frame*. Or cette spécification n'est pas un artefact de sécurité : c'est un artefact de conception du processus. **Lecture de l'auteur** : la conséquence est que la sûreté d'un système agentique se décide, pour l'essentiel, au moment où l'on décide de son architecture, et non au moment où l'on choisit ses protocoles. Le socle ne formule pas cette proposition ; il en fournit les deux termes — les *frames* comme frontière de sécurité chez les auteurs du manifeste[^3], et l'indépendance de la sûreté à l'égard de la spécification protocolaire dans la réserve F-01[^1]. Le rapprochement est de l'auteur, et l'ouvrage entier peut se lire comme sa vérification.

Trois renvois closent ce que le présent chapitre s'interdit de traiter. **L'identité des agents et leur inventaire gouverné** — qui, en dernière analyse, sont ce qui permet de savoir quels outils un agent donné est autorisé à invoquer — relèvent du chapitre 8. **Les passerelles**, c'est-à-dire les points de contrôle placés entre les agents, les modèles et les systèmes d'entreprise, relèvent de la Partie VII, où le blueprint les instancie sur un portefeuille documenté (chapitres 22 et 23). **La traduction des exigences réglementaires canadiennes** en contraintes d'architecture relève de la Partie III. Ce découpage n'est pas une commodité de plan : il reflète exactement la conclusion du chapitre. Ce que les protocoles ne couvrent pas, d'autres couches le couvrent — ou ne le couvrent pas, et c'est alors à l'architecture d'en répondre.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, la sécurité des protocoles agentiques dépend de leur implémentation : c'est une réserve de caractérisation inscrite au socle de cet ouvrage, non une prudence rhétorique, et elle interdit d'écrire qu'un protocole est « sécurisé »[^1]. **Deuxièmement**, trois surfaces d'attaque sont nommées par le socle — l'empoisonnement d'outils, l'injection d'invites, l'empoisonnement de mémoire — dont la deuxième apparaît à deux endroits, sans que le socle établisse l'indépendance de ces deux mentions[^1][^3]. **Troisièmement**, les réponses que les spécifications apportent — cadre d'autorisation fondé sur OAuth pour MCP, cartes d'agents signées pour A2A v1.0 — portent sur l'identité et l'habilitation de l'appelant, et le socle ne leur attribue aucune portée au-delà[^1][^4].

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas comment ces attaques s'exécutent : le socle les nomme sans en documenter la mécanique, et l'encadré de la section 4.1 expose cette lacune plutôt que de la combler. Il ne dit pas que ces trois surfaces épuisent la question : le manifeste APM qualifie le défi d'holistique, ce qui est l'inverse d'une liste close[^3]. Il ne dit pas que les *frames* locaux résolvent le problème : le socle en fait une frontière de confinement, non une garantie. Il ne dit rien, enfin, d'un incident réel : aucune source du socle n'atteste une attaque survenue contre une implémentation en exploitation, dans une institution financière canadienne ou ailleurs — silence qu'il faut lire comme une limite de cet ouvrage et non comme une absence d'incidents.

Un protocole ouvert et gouverné de façon neutre demeure un format d'échange. C'est déjà beaucoup ; ce n'est pas une posture de sécurité.

---

## Notes

[^1]: PRD §7.1, **F-01** (niveau [A]). Sources retenues ici : spécification MCP, révision 2025-11-25 (modelcontextprotocol.io), revalidée le 16 juillet 2026 ; annonce Anthropic de novembre 2024. F-01 en cite une troisième, arXiv 2505.02279, sous la réserve F-06 (préprint non révisé par les pairs, usage descriptif seulement) ; le socle n'indique pas laquelle des trois documente les attaques citées à la réserve. **Réserve F-01, contraignante pour tout ce chapitre** : dire « cadre d'autorisation », jamais « sécurisé » — la sécurité dépend de l'implémentation ; empoisonnement d'outils et injection d'invites documentés. Sur la révision attendue le 28 juillet 2026 (refonte sans état, retrait de `Mcp-Session-Id`, en-têtes `Mcp-Method`/`Mcp-Name`, décrite par les mainteneurs comme la plus importante révision depuis le lancement) : rapport de revalidation `verification/revalidation-2026-07-16.md` ; fait chaud à resurveiller en P4.1 (PRD §8.3).

[^2]: **Formes** imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.3, tracées à **F-01** (empoisonnement d'outils, injection d'invites) et à **F-36** (injection d'invites, empoisonnement de mémoire). ⚠ **Formes, et non définitions** : le glossaire a **retiré ses trois gloses d'auteur le 17 juillet 2026** — les trois risques y sont désormais marqués « risque nommé, mécanique non portée » (lacune PRD §10.8). Cette note portait « Formes **et définitions** imposées » : elle renvoyait à des définitions que sa source d'autorité ne porte plus, et le présent chapitre en tirait trois gloses sous trace de socle. *Rectifié le 17 juillet 2026 (audit global : le constat M-04 visait l'empoisonnement de mémoire ; la même cascade portait sur les deux autres risques, non relevés — la rétractation du glossaire n'avait été propagée à aucun des trois.)*

[^3]: PRD §7.7, **F-36** (niveau [B] — article lu intégralement). Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al. (18 auteurs), issu du séminaire Dagstuhl #25192 ; version journal *Information Systems* 140, 102738 (2026) / arXiv:2603.18916v3 (12 avril 2026). Éléments mobilisés ici : défi transversal **C2 (sécurité holistique)** — injection d'invites, empoisonnement de mémoire, paradoxe de confidentialité de l'explicabilité, patrons *Action-Selector* et *Plan-Then-Execute* (**cités par le manifeste, non détaillés par le socle**) ; explicabilité liée à la conformité réglementaire (RGPD, *AI Act* européen) et finance rangée parmi les domaines à haut risque ; **opérationnalisation locale des *frames* comme frontière de sécurité et de confidentialité**. La mention, par le manifeste, de l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI) est antérieure à sa fusion dans A2A (29 août 2025, F-43) et n'est pas reprise ici (PRD §8.1, R-1 et R-8 ; désambiguïsation des quatre emplois : ch. 1 §1.2).

[^4]: PRD §7.1, **F-02** (niveau [A]). Sources primaires : a2a-protocol.org/latest/announcing-1.0 ; communiqué de la Linux Foundation du 9 avril 2026 ; `GOVERNANCE.md` du dépôt a2aproject/A2A. La qualification « production-ready » et la mention d'une première spécification stable sont portées par F-02 et tirées de l'annonce du projet (a2a-protocol.org/latest/announcing-1.0) — auto-déclarées, non issues d'une évaluation tierce ; attribuées à leur source par principe général d'attribution (PRD §8.2). La doctrine officielle de complémentarité avec MCP (« MCP dans les agents, A2A entre les agents ») relève de **F-16** et du chapitre 2.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (4 notes ; termes anglais entre parenthèses et en italique à la 1re occurrence
                                   du chapitre : authorization framework, tool poisoning, prompt injection, memory
                                   poisoning, Signed Agent Cards, framed autonomy — multi-tenancy retiré, renvoyé au ch. 2)
     3. Balayage garde-fous ...... fait, repris après relecture (réserve F-01 : aucune occurrence de « sécurisé »
                                   appliqué à un protocole — « cadre d'autorisation » partout ; R-8 : ni sigle ACP nu,
                                   ni « control plane », ni « plan de contrôle » dans le corps — seule mention d'ACP
                                   en note [^3], désormais à la forme imposée (Annexe D §D.1 branche (a)) ;
                                   §8.2 : « production-ready » attribué à l'annonce du projet A2A)
     4. Relecture adversariale ... fait (deux relecteurs indépendants, 16 juillet 2026 : 5 constats bloquants,
                                   8 réserves — tous vérifiés au socle et appliqués). Ce que la relecture a réfuté :
                                   (i) l'attribution de la liste des attaques à « une spécification technique » —
                                       F-01 adosse sa réserve à trois sources sans dire laquelle les documente
                                       (dont arXiv 2505.02279, sous réserve F-06) : porteur inventé, supprimé ;
                                   (ii) l'« indépendance » des deux corpus et la « corroboration croisée » —
                                       F-36 signale que le manifeste cite MCP : le second commente le premier ;
                                       affirmation supprimée du corps ET de la conclusion (où elle s'était durcie) ;
                                   (iii) « la surface est la fonction elle-même » — inférence non marquée, introduite
                                       par une formule d'autorité, et reprise en conclusion sous notes [^1][^3] ;
                                   (iv) la portée d'exécution des attaques (« une exécution » / « toutes les suivantes »)
                                       — mécanique que l'encadré du chapitre déclare lui-même absente du socle ;
                                   (v) multi-protocole et multi-location — assignés au ch. 2 par TOC : doublon retiré.
                                   Réserves appliquées : renvoi §8.2.1→§8.2 (l'article ne couvre que les métriques
                                   d'adoption) ; inversion frames/autonomie encadrée redressée sur F-36 (2) ;
                                   forme R-8 de l'ACP protocolaire ; marquage des trois propriétés d'OAuth et de
                                   « gouvernance ≠ sûreté » ; encadré de lacune complété (recherche menée + question
                                   ouverte, PRDPlan §4.4) ; F-16 retiré de l'en-tête (absent de TOC, non mobilisé).
     5. Commit + registre de gel . fait (ligne du ch. 4 au registre `99-registre-gel.md`, commit `dc0a394`
                                   « revise chapter 4 after adversarial review »)
     6. Passe de conformité (audit du 17 juill. 2026 — aucune information nouvelle, date de gel inchangée) :
        M-03 — en-tête : la thèse citée était celle d'AVANT correctif (« documentés dès l'origine ») et l'attribuait
               à TOC.md, qui porte la thèse amendée depuis le 16 juill. 2026 ; l'en-tête affirmait donc ce que le
               corps du chapitre réfute (§4.1 et son encadré). Thèse ACTUELLE du TOC reproduite.
        M-04 — §4.1 : « Le socle le définit par ce qu'il corrompt : la mémoire PERSISTANTE de l'agent » — glose
               d'auteur : F-36 NOMME l'empoisonnement de mémoire sans le caractériser, et le glossaire (annexe D
               §D.3) a retiré cette glose le 17 juill. 2026 (« aucune caractérisation au socle ») sans que la
               rétractation soit cascadée ici. Glose retirée. RETIRÉE AUSSI, l'inférence qu'elle portait (« du seul
               caractère persistant de la mémoire… vice latent plutôt qu'incident ») : sa prémisse — la persistance —
               n'est pas au socle, et rien n'y permet de la refonder ; l'énoncé est remplacé par le constat
               de la sous-documentation, et la question de gravité rendue au lecteur comme non tranchable ici.
        m-09 — encadré §4.1 : gabarit « cas 1 » (« Recherche menée le 16 juillet 2026 : … ») employé pour la lacune
               §10.8, que le PRD tient pour NON INSTRUITE (« Sources à retrouver : spécification MCP (section
               sécurité)… ») — PRDPlan §4.4 proscrit le cas 1 hors passe traçable (« il induit la fabrication d'une
               passe qui n'a pas eu lieu »). Converti au gabarit CAS 2 (titre « État de la recherche », date
               d'ouverture de la lacune, « aucune passe de recherche n'a été conduite », sources à retrouver).
               L'honnêteté déjà présente au 1er jet — « aucune passe de recherche externe n'a été conduite à ce
               lot » — est conservée mot pour mot. La mention « dès l'origine » de la thèse TOC est passée au
               passé et rattachée à son correctif (TOC v1.3) — elle était restée au présent.
        m-10 — bloc « 5. Commit + registre de gel : À FAIRE » périmé (le chapitre est enregistré au registre) ;
               corrigé.
        Signalé au parent, NON corrigé (hors périmètre — le glossaire n'est pas modifiable dans cette passe) :
        la note [^2] trace « le détournement d'un outil exposé à un agent » (§4.1) au glossaire §D.3, qui a retiré
        cette glose le 17 juill. 2026 au même titre que celle de la mémoire — même cascade interrompue que M-04,
        sur l'empoisonnement d'outils cette fois ; non relevée par l'audit, à instruire.
     Gouvernance signalée au parent (non corrigée ici, PRD/TOC/glossaire non modifiés) :
     (a) la thèse TOC « documentés dès l'origine » n'est pas datée par le socle — chapitre écrit sans la datation
         (RÉSOLU le 16 juill. 2026 : thèse amendée au TOC, v1.3 ; en-tête aligné le 17 juill. 2026, constat M-03) ;
     (b) F-36 nomme Action-Selector / Plan-Then-Execute sans mécanique — non décrits ;
     (c) aucun incident public ni identifiant de vulnérabilité au socle — encadré §4.1, lacune candidate à §10 ;
     (d) PRD §8.2 n'a aucun article couvrant les auto-qualifications de maturité (« production-ready », « stable ») —
         seul §8.2.1 (métriques d'adoption) en approche, et il ne les couvre pas : article à créer ou §8.2.1 à étendre ;
     (e) F-01 adosse sa réserve (empoisonnement d'outils, injection d'invites) à trois sources sans attribution
         individuelle, dont un préprint sous réserve F-06 — aucun chapitre ne peut donc attribuer ces attaques
         à une source précise : à trancher en P4 (attribution nominative ou lacune §10).
-->
