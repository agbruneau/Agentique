# Chapitre 7 — Réalisations : les frameworks d'orchestration d'entreprise

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-15, F-16, F-32, F-33 ; F-41 (renvoi : acquisition de Confluent par IBM, clôturée le 17 mars 2026) ; F-37 (renvoi : vocabulaire OO1–OO4 du ch. 5) ; Temporal et CrewAI (§7.6, entrées sans identifiant) |
| Garde-fous à surveiller (PRD §8) | §8.2.3 (métriques d'éditeurs de plateformes — attribution à chaque occurrence) ; réserve F-01 (« cadre d'autorisation », jamais « sécurisé ») ; §8.4 (neutralité fournisseur — Confluent/IBM par renvoi au ch. 22) ; lacune §10.3 (réduite en P0 par les élévations de CrewAI et de LangGraph Platform ; ne subsiste que Temporal, hors périmètre de la passe — non retenté) |
| Volumétrie cible | ~3200 mots |

> **Thèse ([TOC.md](../../TOC.md))** : L'offre s'est industrialisée en 2025-2026 — successions assumées (Agent Framework), plateformes GA (LangGraph), orchestration événementielle (Confluent/Kafka) — avec un support MCP **répandu et inégalement établi** et un support A2A désormais attesté de première main, mais de périmètre inégal.

---

Les deux chapitres précédents ont posé un vocabulaire et un principe : quatre options d'orchestration (*orchestration options*, OO1–OO4) permettant de situer une architecture agentique sur un continuum d'encadrement, et l'autonomie encadrée (*framed autonomy*) comme mécanisme premier de gouvernance. Reste la question que pose tout architecte d'entreprise une fois la doctrine admise : que livre effectivement l'industrie, à quelle date, et avec quel statut de disponibilité ? Un principe d'architecture qu'aucun produit ne sait porter n'est qu'un vœu ; un produit dont la fonctionnalité décisive est en préversion n'est pas encore une décision d'achat.

Ce chapitre soutient que l'industrialisation a bel et bien eu lieu — mais qu'elle est plus inégale que le discours des éditeurs ne le laisse paraître, et que cette inégalité se loge précisément là où une institution financière regarde : le statut de disponibilité, le périmètre exact des fonctionnalités d'interopérabilité, et la démarcation entre ce qu'un éditeur documente et ce qu'il se contente de déclarer. Il couvre cinq offres, dans le périmètre exact que le socle de cet ouvrage autorise : trois au corps du chapitre, deux en encadré — dont une, Temporal, que le socle ne documente qu'au niveau du repérage documentaire.

Une convention de lecture s'impose d'entrée, car elle gouverne tout le chapitre. Lorsqu'il est écrit ci-dessous que « le socle ne documente pas » telle capacité d'un produit, il faut l'entendre au sens strict : c'est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié. La distinction n'est pas de rhétorique. Elle sépare ce qu'un dossier de conformité peut affirmer de ce qu'il doit aller vérifier lui-même.

## 7.1 Microsoft Agent Framework : la succession assumée

Le premier des trois jalons est daté du **3 avril 2026** : Microsoft Agent Framework atteint sa disponibilité générale (*general availability*, GA) en version 1.0[^1]. Le fait notable n'est pas la version, c'est la généalogie. Agent Framework est le successeur direct de deux produits Microsoft antérieurs — Semantic Kernel et AutoGen — développés par les mêmes équipes ; il fusionne les abstractions d'agents issues d'AutoGen et les fonctionnalités d'entreprise issues de Semantic Kernel, et le socle cite des guides de migration publiés sur DevBlogs[^1] — sans établir qu'il en existe un par lignée.

**Lecture de l'auteur** : la succession assumée n'est pas un détail de calendrier produit, c'est un signal de risque de tiers. Une institution qui avait bâti sur AutoGen ou sur Semantic Kernel n'affronte pas un abandon, mais une convergence documentée, assortie de guides de migration publiés. Le socle établit la filiation, la fusion des abstractions et l'existence de ces guides ; il n'établit ni leur couverture par lignée, ni leur qualité, ni le coût réel d'une migration, ni aucun engagement de support à long terme. L'inférence porte sur la forme de la transition, pas sur sa facilité.

Sur le versant protocolaire, Agent Framework est l'offre du socle dont le support MCP est le mieux caractérisé : support natif, avec clients MCP, serveurs MCP appelables, outils locaux et outils hébergés[^1]. La bidirectionnalité mérite qu'on s'y arrête : le framework consomme des outils exposés par des serveurs MCP tiers, et peut lui-même en exposer. C'est exactement la doctrine officielle de complémentarité que le chapitre 2 examine — MCP pour l'intégration outils et contexte au niveau de l'agent individuel, A2A pour la coordination entre agents, que le projet A2A résume par « Complementary to MCP, not a replacement »[^2] —, appliquée ici du premier côté. Précisons dans le même mouvement ce que la formule ne dit pas : MCP fournit un **cadre d'autorisation** fondé sur OAuth, ce qui ne rend « sécurisée » aucune implémentation qui s'en réclame ; le chapitre 4 en documente les surfaces d'attaque.

Le socle ne documente pas de support A2A pour Agent Framework lui-même[^1] ; les intégrations A2A des plateformes infonuagiques de Microsoft relèvent d'une autre entrée et sont traitées au chapitre 2. Selon la convention posée en ouverture, c'est une absence de documentation, non une absence établie.

Sur le versant de l'orchestration, Agent Framework livre des workflows à base de graphes (*graph-based workflows*) avec routage typé (*typed routing*), points de contrôle (*checkpointing*) et humain-dans-la-boucle (*human-in-the-loop*)[^1]. **Lecture de l'auteur** : ce triplet se laisse lire avec les catégories du chapitre 5 — le graphe comme cadre explicite, le point de contrôle comme instrument de traçabilité, l'humain-dans-la-boucle comme point d'arrêt de supervision. Le socle établit les capacités d'un côté et la taxonomie de l'autre ; le rapprochement est le nôtre, développé en §7.5. On notera au passage que l'humain-dans-la-boucle des frameworks ne doit pas être confondu avec la révision humaine que le chapitre 11 examine au titre de l'article 12.1 de la Loi 25 (Annexe D §D.2) : les deux mécanismes se ressemblent et ne répondent pas au même besoin.

Deux réserves accompagnent l'entrée du socle, et l'une d'elles porte loin. La première est mineure : le SDK Go demeure en préversion[^1]. La seconde ne l'est pas : le socle documente des **limites connues du magasin de points de contrôle (*checkpoint-store*) en déploiement distribué multi-pods**[^1]. **Lecture de l'auteur** : une institution financière canadienne qui déploierait Agent Framework le ferait, selon toute vraisemblance, sur une infrastructure conteneurisée distribuée — c'est-à-dire dans la configuration précise où le socle signale la limite ; et le mécanisme concerné, le point de contrôle, est celui-là même dont dépend la reconstitution *a posteriori* d'une exécution. Le socle établit l'existence de la limite et son domaine ; il n'en établit ni la gravité, ni le contournement, ni le calendrier de résolution. La conclusion praticable n'est pas « ne pas déployer », c'est « instruire ce point avant l'inventaire de modèles » — et cette instruction incombe à l'institution, non à cet ouvrage.

## 7.2 LangGraph Platform : la GA la plus ancienne, la frontière plateforme/bibliothèque

Le deuxième jalon est antérieur de moins de onze mois au premier : LangChain annonce la disponibilité générale de **LangGraph Platform le 14 mai 2025**, pour le déploiement et la gestion d'agents à état et de longue durée (*stateful, long-running agents*)[^3]. Le billet de disponibilité générale nomme des entreprises construisant des agents avec LangGraph — Klarna, Lovable, Replit, Clay, LinkedIn — et un client d'entreprise pour la gestion centralisée, Qualtrics[^3].

Ces noms appellent une précision de lecture que la source impose d'elle-même. Le socle distingue deux énoncés que la promotion tend à confondre : Klarna, Lovable, Replit, Clay et LinkedIn sont cités comme construisant des agents **avec LangGraph** — la bibliothèque —, tandis que Qualtrics est nommée comme cliente d'entreprise **pour la gestion centralisée** — la plateforme[^3]. Ce ne sont pas les mêmes affirmations, et le socle ne permet ni de les fusionner, ni d'inférer que ces entreprises figurent parmi les déploiements en production dénombrés ci-dessous. Une référence client nommée est un fait plus solide qu'un décompte agrégé, à condition de ne lui faire dire que ce qu'elle dit.

Le billet annonce aussi un chiffre, et c'est ici qu'il faut ralentir. **Selon le billet de disponibilité générale de LangChain du 14 mai 2025, l'éditeur déclare que près de 400 entreprises avaient déployé des agents en production via la plateforme depuis la bêta de juin 2024** — soit sur les onze mois qui séparent juin 2024 du 14 mai 2025. Cette donnée est **auto-déclarée par LangChain et n'a pas fait l'objet d'une vérification indépendante**[^7]. Elle n'est pas pour autant sans valeur : à la différence des décomptes d'« organisations de soutien » examinés au chapitre 1, elle prétend mesurer un déploiement en production, ce qui est la grandeur pertinente. Mais elle est déclarée par le vendeur du produit qu'elle valorise, sans définition publiée de l'unité comptée, et cet ouvrage la traite comme telle à chacune de ses occurrences.

Le point décisif du présent chapitre est ailleurs, et il est de périmètre. Le billet de disponibilité générale de mai 2025 **ne mentionne ni MCP ni A2A**[^3]. La passe d'élévation du 16 juillet 2026 a comblé une partie de ce silence, mais d'une manière qu'il faut énoncer avec exactitude : le support A2A est confirmé de première main pour **LangGraph Platform / LangSmith Deployment** — la documentation officielle décrit un point d'entrée `/a2a/{assistant_id}` et les méthodes `message/send`, `message/stream` et `tasks/get` — **mais pas pour la bibliothèque libre (*open source*) `langgraph` elle-même**, où la fonctionnalité demeure une requête ouverte au 3 avril 2026[^3].

**Lecture de l'auteur** : cette frontière n'est pas technique, elle est commerciale, et elle se lit dans un dossier d'approvisionnement avant de se lire dans une architecture. L'interopérabilité inter-agents de la lignée LangGraph est, à la date de gel de ce chapitre, une propriété de l'offre commerciale et non de la bibliothèque libre. Une institution qui adopterait `langgraph` en pensant obtenir A2A, ou qui construirait un scénario de repli sur la seule bibliothèque libre en supposant la parité fonctionnelle, se tromperait sur ce qu'elle achète et sur ce qu'elle peut internaliser. Le socle établit les deux versants de cette asymétrie ; il n'établit ni l'intention de l'éditeur, ni le calendrier d'une éventuelle convergence.

Quant au support MCP de LangGraph, le socle n'en documente aucune source de première main[^3] — absence de documentation, encore une fois, et non fait négatif vérifié. Elle suffit néanmoins à mesurer ce que la thèse de ce chapitre entend par un support MCP « répandu et inégalement établi » — et le décompte le montre plus précisément encore. Sur les cinq offres examinées ici, le support MCP n'est documenté de première main que pour **deux** — Agent Framework et Confluent —, repéré sans extraction pour **deux** autres — Temporal et CrewAI, que le socle range l'un comme l'autre au niveau [C] —, et non documenté pour la cinquième. Répandu, en effet ; inégalement établi, surtout — et à aucun moment « généralisé », mot que le décompte réfute et que la thèse, depuis son amendement, ne porte plus.

## 7.3 L'orchestration événementielle : le journal avant le cadre

Des trois branches traitées au corps de ce chapitre, la troisième est la seule à ne pas être en disponibilité générale, et c'est peut-être la plus intéressante pour une institution financière — parce qu'elle raisonne en flux, comme les paiements.

En **août 2025**, Confluent annonce les « Streaming Agents » sur Confluent Cloud : des agents événementiels s'exécutant sur Flink et Kafka managés, avec appel d'outils déclaré nativement via MCP[^4]. Six mois plus tard, la mise à jour du **26 février 2026** ajoute trois éléments : une **intégration A2A en préversion publique (*Open Preview*)**, permettant aux Streaming Agents d'orchestrer des tâches avec des agents externes sur toute plateforme compatible A2A — LangChain, CrewAI, SAP et Salesforce sont cités ; le **support officiel du serveur MCP libre pour Confluent Cloud**, couvrant Kafka, Flink, les connecteurs, Tableflow et le Schema Registry ; et une caractérisation du transport qui mérite d'être citée en langue originale pour ce qu'elle affirme — la collaboration inter-agents s'y opère « all over a reliable, replayable Kafka backbone », soit sur une dorsale Kafka fiable et rejouable[^4].

**Lecture de l'auteur** : c'est là que la Partie II rejoint ce qu'elle a établi au chapitre 5. Les travaux repris au chapitre 5 — un préprint non révisé par les pairs, dont les auteurs déclarent eux-mêmes des menaces à la validité — posent que la journalisation confiée aux agents eux-mêmes n'est généralement pas recommandée[^6]. Un bus d'événements rejouable répond exactement à ce problème : il externalise le journal hors des agents, et le rend rejouable par construction plutôt que par discipline. Le socle établit la caractérisation du transport par Confluent et la position des travaux de Munich ; il n'établit pas le rapprochement entre les deux, qui est une inférence de cet ouvrage — et une inférence dont la portée est bornée. Un bus fiable et rejouable fournit un **journal**, non un **cadre** : il enregistre ce qui s'est produit, il n'impose pas ce qui doit se produire. La traçabilité n'est pas l'encadrement, et la Partie III montrera que les exigences canadiennes réclament les deux.

La liste des plateformes que Confluent cite comme partenaires A2A possibles — LangChain, CrewAI, SAP, Salesforce[^4] — mérite un mot, parce qu'elle recoupe le périmètre de ce chapitre. Un seul de ces quatre noms — CrewAI — renvoie à une offre dont le socle confirme de première main, chez l'éditeur, un support A2A[^9]. Confluent cite par ailleurs « LangChain » sans préciser le produit visé, et le socle ne permet pas de rattacher cette mention à LangGraph Platform plutôt qu'à la bibliothèque libre `langgraph`[^3] — laquelle n'a précisément aucun support A2A documenté. La frontière posée au §7.2 interdit de trancher à la place de la source.

**Lecture de l'auteur** : la recoupe vaut d'être notée pour ce seul cas, où l'ouvrage dispose enfin d'attestations des deux côtés plutôt que d'un seul. Elle ne va pas plus loin : la mention par Confluent est une déclaration de Confluent sur ce que son intégration permettrait, la confirmation vient de l'éditeur cité et porte sur son propre produit, et aucune source du socle ne documente une liaison A2A effectivement établie entre deux de ces offres — l'une des deux extrémités, celle de Confluent, étant du reste en préversion.

Deux réserves, ici, sont dirimantes. Les fonctionnalités décrites sont **pré-GA** — préversion publique ou accès anticipé[^4]. Et la source **ne nomme aucun client et ne publie aucun chiffre d'adoption** : l'adoption en production ne peut pas en être inférée[^4]. Le contraste avec la section précédente est instructif. LangChain publie un chiffre auto-déclaré que nous devons attribuer ; Confluent n'en publie aucun, ce qui interdit toute affirmation d'adoption mais épargne au lecteur une métrique invérifiable. Aucune des deux situations ne permet d'écrire que la branche événementielle est déployée en production dans une institution financière.

Un fait de propriété, enfin, dont ce chapitre ne développe pas les conséquences. **IBM a annoncé l'acquisition de Confluent le 8 décembre 2025 et l'a clôturée le 17 mars 2026** — dix-neuf jours après la mise à jour qui vient d'être décrite, et trois mois et neuf jours après l'annonce ; Confluent est depuis une filiale à part entière d'IBM[^5]. Ce qui en découle pour un portefeuille d'intégration d'entreprise relève du chapitre 22, où le fait est traité au passé et sous la réserve de neutralité fournisseur qui gouverne toute la Partie VII. Retenons ici le seul point qui concerne l'architecte en amont de son choix : la trajectoire événementielle décrite ci-dessus a changé de propriétaire entre son annonce et la date de gel de ce chapitre.

## 7.4 Deux cas en encadré

Les deux offres restantes ne se traitent pas au même niveau de preuve, et c'est la raison de leur mise en encadré.

> **État de la connaissance vérifiable — l'adoption d'entreprise de Temporal**
>
> Question : quelle est l'adoption d'entreprise de Temporal, et quel est le statut exact de son support des agents et de MCP ? Recherche : **aucune**. La passe d'élévation bornée du 16 juillet 2026 n'a pas instruit Temporal — elle a porté sur quatre cibles : BMO, Sun Life, le support A2A de LangChain et de CrewAI, et la solution FTM/ISO 20022. La lacune du socle est réduite parce que CrewAI et LangGraph Platform y ont été élevés à la source primaire extraite ; **Temporal y subsiste faute de tentative, non par échec de recherche**, et ses chiffres d'adoption d'entreprise demeurent non vérifiés. La distinction importe en dossier de conformité : rien n'autorise à conclure que ces chiffres résisteraient à la vérification, ni qu'ils s'y déroberaient. Le socle n'en conserve qu'un **repérage documentaire** — un billet officiel décrivant une intégration du SDK d'agents d'OpenAI en préversion publique, chaque invocation d'agent s'exécutant comme *Activity* orchestrée dans un *Workflow* durable, ainsi que des recettes MCP dans la documentation — sans extraction intégrale du contenu. Ce niveau de preuve interdit à ces éléments de porter un fait central de cet ouvrage ; ils sont mentionnés ici comme repérage, et à ce titre seulement. En l'absence de source primaire extraite, la question reste ouverte ; aucune inférence n'est proposée ici[^8].

> **CrewAI — première main sur A2A, repérage sur MCP, autodéclaration sur l'adoption**
>
> CrewAI se documente à trois niveaux de preuve distincts, qu'il faut tenir séparés — c'est ce qui le distingue de Temporal, uniformément au repérage. Le support A2A y est documenté de première main, **élevé [B] le 16 juillet 2026** sur source primaire extraite : la documentation officielle de CrewAI énonce que « CrewAI treats A2A protocol as a first-class delegation primitive », décrit une installation par `crewai[a2a]` et des classes `A2AClientConfig` et `A2AServerConfig`, et porte un journal des modifications daté depuis novembre 2025 ; l'extension d'entreprise est documentée sous la plateforme CrewAI AMP[^9].
>
> Le support MCP relève d'un deuxième régime. Il est documenté officiellement par l'éditeur — connexion par stdio, SSE ou HTTP diffusable, les outils MCP étant consommés comme des outils natifs —, mais le socle le laisse au niveau du **repérage [C]** : il n'en a pas extrait le contenu, et l'élévation du 16 juillet 2026 n'a porté que sur A2A. Il ne peut donc porter aucun fait central — d'où le décompte du §7.2.
>
> Les chiffres d'adoption relèvent d'un troisième régime. **Selon CrewAI — qui ne publie à cet endroit ni source datée ni définition de l'unité comptée —, l'éditeur déclare que sa plateforme est employée par des entreprises du Fortune 500 et qu'elle a enregistré environ deux milliards d'exécutions sur douze mois. Ces données sont auto-déclarées et n'ont fait l'objet d'aucune vérification indépendante**[^7]. L'écart avec la métrique de LangChain (§7.2) joue contre CrewAI : celle-là est datée et rattachée à un billet identifiable, donc situable et contestable ; celle-ci ne l'est pas. Ces chiffres ne sont repris ici que sous cette attribution, et ne fondent aucune affirmation d'adoption en production dans le secteur financier canadien.

## 7.5 Grille de lecture : ce que les patrons livrés positionnent, et ce qu'ils ne positionnent pas

Il reste à faire ce pour quoi la Partie II a construit son vocabulaire : situer les patrons livrés sur la taxonomie du chapitre 5. L'exercice appelle un avertissement préalable. **Aucune source du socle ne positionne un framework sur l'échelle OO1–OO4** : la taxonomie est un cadre académique, les produits sont documentés par leurs éditeurs, et **le corpus de cet ouvrage ne contient aucune source rapprochant les deux** — absence de documentation, non fait négatif vérifié, conformément à la convention posée en ouverture. Le tableau qui suit est donc intégralement une **lecture de l'auteur** — il rapproche ce que le socle établit d'un côté et de l'autre.

| Patron livré | Ce que le socle établit | Positionnement OO proposé (inférence d'auteur) |
|---|---|---|
| Workflows à base de graphes, routage typé | Agent Framework, GA 1.0 (F-15) | Le graphe est un cadre explicite extérieur aux agents — **OO3 ou OO4** selon que les agents invoqués sont ou non conscients du processus |
| Points de contrôle | Agent Framework, GA 1.0 ; limites en multi-pods (F-15) | Instrument de la propriété **traçabilité** (F-37), non une option d'orchestration en soi |
| Humain-dans-la-boucle | Agent Framework, GA 1.0 (F-15) | Point d'arrêt de supervision ; critère de sélection F-37, non un positionnement OO |
| Agents durables | Temporal — **repérage [C]**, ne porte aucun fait central | Aucun positionnement proposé : le niveau de preuve ne le permet pas |
| Bus d'événements comme transport inter-agents | Confluent, A2A en préversion publique sur dorsale Kafka rejouable (F-33) | A2A sans cadre de processus explicite est la définition même d'**OO1** (F-37) ; le bus ajoute le journal, non le cadre |

De ce tableau, un enseignement se dégage, et c'est le principal du chapitre. **Aucun des frameworks examinés ne livre un positionnement OO ; ils livrent des matériaux qui en autorisent plusieurs.** Un même Agent Framework sert à câbler un graphe déterministe qui invoque des agents pour des tâches bornées — de l'ordre d'OO3 — ou à laisser un agent choisir librement ses outils MCP sans cadre explicite — de l'ordre d'OO1. Le produit n'arbitre pas ; la configuration arbitre. Le cadre repris au chapitre 5 rappelle d'ailleurs que les transitions entre options sont fluides[^6], ce qui est la même observation vue depuis la théorie.

**Lecture de l'auteur**, et elle engage la suite de l'ouvrage : si le positionnement est un fait de configuration et non de produit, alors la question « quel framework choisir ? » est mal posée pour une institution réglementée. La bonne question est « quel cadre imposer, et quel produit sait le porter ? » — l'ordre des termes n'est pas indifférent. Elle explique aussi pourquoi la Partie VI construit son architecture de référence à partir des exigences et non du catalogue. Le socle n'établit pas cette proposition ; il en fournit les deux moitiés — la taxonomie d'un côté, les capacités documentées de l'autre — et le rapprochement est le nôtre.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, l'industrialisation est datée et vérifiable, mais inégale : deux jalons de disponibilité générale sont datés et vérifiables — LangGraph Platform le 14 mai 2025, Agent Framework 1.0 le 3 avril 2026 —, tandis que la branche événementielle demeure en préversion à la date de gel. **Deuxièmement**, le support des deux protocoles est réel mais de périmètre inégal : MCP n'est documenté de première main que chez Agent Framework et Confluent, repéré sans extraction chez Temporal et chez CrewAI, et non documenté chez LangGraph — deux offres sur cinq de première main : « répandu et inégalement établi », comme l'énonce la thèse, et jamais « généralisé » ; A2A est attesté de première main chez CrewAI, chez LangGraph Platform mais non dans sa bibliothèque libre, et chez Confluent en préversion publique seulement. **Troisièmement**, aucun de ces produits ne décide à la place de l'architecte de son degré d'encadrement.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne classe pas ces offres et n'en recommande aucune : le socle ne contient aucun comparatif indépendant, et le peu de métriques disponibles est auto-déclaré par les éditeurs. Il n'établit aucune adoption en production dans une institution financière canadienne — c'est l'objet de la Partie V, et aucune des sources citées ici n'y contribue. Il ne traite ni de l'identité des agents ni des registres, qui font l'objet du chapitre 8, ni de la place de la branche événementielle dans un portefeuille d'intégration, qui relève du chapitre 22. Il ne dit pas, enfin, qu'un produit puisse rendre une orchestration conforme : la Partie III établira que la conformité se joue sur le cadre imposé, et le chapitre 13 en fera le pivot de l'ouvrage.

Les matériaux existent. Ce qu'on en fait reste entier.

---

## Notes

[^1]: PRD §7.6, **F-15** (confiance haute). Sources primaires : Microsoft Learn (page mise à jour le 10 juillet 2026, soit six jours avant la date de gel du présent chapitre) ; guides de migration publiés sur DevBlogs. **Réserves F-15** : SDK Go en préversion ; limites connues du magasin de points de contrôle en déploiement distribué multi-pods (discussion GitHub #2305). L'entrée ne documente aucun support A2A pour le framework lui-même ; les intégrations A2A des plateformes infonuagiques de Microsoft relèvent de **F-03** (ch. 2).

[^2]: PRD §7.6, **F-16** (haute). Source primaire : a2a-protocol.org/latest/announcing-1.0 (« Complementary to MCP, not a replacement »). Sur le cadre d'autorisation de MCP et la réserve associée : PRD §7.1, **F-01** — dire « cadre d'autorisation », jamais « sécurisé » (ch. 4).

[^3]: PRD §7.6, **F-32** (haute) **[B — annonce primaire extraite avec citations verbatim]**. Sources primaires : langchain.com/blog (billet de disponibilité générale du 14 mai 2025) ; docs.langchain.com/langsmith/server-a2a (point d'entrée `/a2a/{assistant_id}` ; méthodes `message/send`, `message/stream`, `tasks/get`). **Réserve de périmètre (élévation du 16 juillet 2026)** : le support A2A est confirmé pour LangGraph Platform / LangSmith Deployment, **pas pour la bibliothèque libre `langgraph`**, où il demeure une requête ouverte (GitHub langchain-ai/langgraph#7398, 3 avril 2026). Le billet de disponibilité générale ne mentionne ni MCP ni A2A ; le socle ne documente aucune source de première main sur un support MCP de LangGraph.

[^4]: PRD §7.6, **F-33** (haute) **[B — annonces primaires extraites avec citations verbatim]**. Sources primaires : confluent.io/blog (annonce « Streaming Agents », août 2025 ; mise à jour du 26 février 2026). **Caractérisation du transport — citation verbatim en langue originale (CA-5)** : « Enable Streaming Agents to collaborate and orchestrate tasks with external agents on any A2A-capable platform (e.g., LangChain, CrewAI, SAP, Salesforce), **all over a reliable, replayable Kafka backbone** » (confluent.io/blog/2026-q1-confluent-intelligence-update, 26 février 2026) ; rendu français de l'ouvrage : « sur une dorsale Kafka fiable et rejouable ». *Verbatim anglais versé au socle le 17 juillet 2026 (PRD §7.6, F-33 — [B], consultation directe du billet primaire) : l'entrée ne portait jusque-là que le rendu français, entre guillemets, sans son original. Même fait, même date de source ; la date de gel du présent chapitre est inchangée.* **Réserves F-33** : fonctionnalités pré-GA (préversion publique / accès anticipé) ; **aucun client nommé ni chiffre d'adoption dans la source** — l'adoption en production ne peut pas en être inférée.

[^5]: PRD §7.8, **F-41** (haute) **[B — revalidé le 16 juillet 2026]**. Sources primaires : newsroom.ibm.com (annonce du 8 décembre 2025 ; « IBM Completes Acquisition of Confluent », 17 mars 2026) ; SEC PREM14A Confluent. Chronologie : 8 décembre 2025 (annonce) → 12 janvier 2026 (expiration HSR) → 12 février 2026 (approbation des actionnaires de Confluent) → 17 mars 2026 (clôture). Conséquences pour le portefeuille d'intégration : ch. 22, sous la réserve de neutralité fournisseur (PRD §8.4).

[^6]: PRD §7.7, **F-37** (haute pour le cadre) **[B — article lu intégralement]**. Rinderle-Ma, Mangler et al. (TU Munich), arXiv:2606.31518v1, 30 juin 2026 — **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité ; le cadre conceptuel (taxonomie OO1–OO4, cinq propriétés d'évaluation, critères de sélection) est repris ici, aucun résultat chiffré n'est mobilisé dans ce chapitre. Vocabulaire posé au ch. 5, qui fait référence.

[^7]: PRD §8.2.3 (métriques d'éditeurs de plateformes : LangGraph, ~400 entreprises en production ; CrewAI, Fortune 500 et ~2 milliards d'exécutions) — auto-déclarées par l'éditeur, attribution obligatoire à chaque occurrence ; formulation imposée par PRDPlan §4.4 (« métrique auto-déclarée »). Sources des chiffres : F-32 (billet LangChain du 14 mai 2025) et §7.6, entrée CrewAI.

[^8]: PRD §7.6, entrée **Temporal — niveau [C]** (repérage documentaire : source primaire identifiée, contenu non extrait intégralement ; à confirmer avant tout usage comme fait central). Lacune **PRD §10.3**, réduite en P0 aux seuls chiffres d'adoption d'entreprise de Temporal — réduite par les élévations de CrewAI et de LangGraph Platform, **non par une tentative infructueuse sur Temporal** : la passe P0.2 du 16 juillet 2026 ne comportait pas Temporal dans son périmètre (quatre cibles : BMO, Sun Life, support A2A LangChain/CrewAI, FTM/ISO 20022 — `verification/revalidation-2026-07-16.md`), et le seul échec d'élévation qu'elle documente porte sur FTM/ISO 20022. Repérages : billet officiel Temporal (intégration du SDK d'agents d'OpenAI en préversion publique) ; docs.temporal.io (recettes MCP).

[^9]: PRD §7.6, entrée **CrewAI**. Support MCP : documentation officielle de l'éditeur (connexion stdio/SSE/HTTP diffusable ; outils MCP consommés comme outils natifs). Support A2A **élevé [B] le 16 juillet 2026** — source primaire de première main : docs.crewai.com/en/learn/a2a-agent-delegation (citation verbatim en langue originale : « CrewAI treats A2A protocol as a first-class delegation primitive ») ; installation `crewai[a2a]` ; classes `A2AClientConfig` / `A2AServerConfig` ; journal des modifications daté depuis novembre 2025 (v1.5.0) ; extension d'entreprise documentée sous CrewAI AMP. Chiffres d'adoption : voir note 7.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; après relecture adversariale : 3519 mots tableau §7.5
                                   inclus, 3374 hors tableau — cible ~3200 ±10 %, soit 2880-3520 : conforme sur les
                                   deux mesures. Les correctifs ont porté le corps à ~3660 ; resserrement des redites
                                   qu'ils avaient introduites, sans retrait de fond, pour revenir sous le plafond.)
     2. Traçabilité (CA-1, CA-5) . fait (9 notes ; termes anglais en italique entre parenthèses à la 1re occurrence :
                                   orchestration options, framed autonomy, general availability, graph-based workflows,
                                   typed routing, checkpointing, human-in-the-loop, stateful long-running agents, Open Preview)
     3. Balayage garde-fous ...... fait (§8.2.3 : LangGraph ~400 entreprises et CrewAI Fortune 500 / ~2 G d'exécutions
                                   attribués à l'éditeur à CHAQUE occurrence ; réserve F-01 : « cadre d'autorisation »,
                                   aucun emploi de « sécurisé » ; §8.4 : Confluent/IBM au passé + renvoi ch. 22 ;
                                   R-8 : aucun emploi de « ACP » ni de « plan de contrôle » dans le chapitre ;
                                   R-1/R-2..R-7 : sans objet ici. Lacune §10.3 (Temporal) traitée en encadré §4.4.)
     4. Relecture adversariale ... FAITE (§4.2.4) — deux relecteurs indépendants ont réfuté le premier jet :
                                   6 constats bloquants + 10 réserves. Tous vérifiés au socle avant application ;
                                   AUCUN écarté comme infondé. Correctifs appliqués :
                                   BLOQUANTS
                                   (1)(2) Encadré Temporal §7.4 — FABRICATION MÉTHODOLOGIQUE : le jet invoquait une
                                       « recherche menée le 16 juillet 2026 » qui « a échoué pour Temporal ». Vérifié :
                                       `grep -rn "Temporal" verification/` = ZÉRO occurrence. La passe P0.2 a quatre
                                       cibles (BMO, Sun Life, A2A LangChain/CrewAI, FTM/ISO 20022) et un seul échec
                                       documenté — FTM/ISO 20022, transposé à tort sur Temporal. PRD §10.3 écrit
                                       « TOUJOURS non vérifiés » = statu quo, pas tentative repoussée. Réécrit :
                                       « Recherche : aucune […] faute de tentative, non par échec ». Note [^8] alignée.
                                       Faute aggravée par l'emplacement : un encadré CA-6 qui fabrique sa méthode
                                       détruit la garantie qu'il donne.
                                   (3) §7.1 — le triplet graphe/point de contrôle/HITL rapproché de F-37 à l'indicatif,
                                       alors que §7.5 déclare ce rapprochement non porté par le socle : même
                                       proposition en fait ET en inférence dans le même chapitre. Basculé en
                                       « Lecture de l'auteur » + renvoi §7.5. « Cœur de ce qui intéresse une
                                       institution réglementée » supprimé (jugement d'auteur non marqué).
                                   (4) §7.5 — « nul n'a rapproché les deux » = négatif universel sur l'état du monde,
                                       violant la convention de lecture posée en ouverture du chapitre lui-même.
                                       Borné au corpus de l'ouvrage.
                                   (5) §7.3 — « la convergence est réelle […] de part et d'autre d'une même liaison »
                                       affirmait à l'indicatif une liaison que la phrase de clôture déclare non
                                       documentée (auto-contradiction). Marqué « Lecture de l'auteur » et borné.
                                   (6) Titre §7.2 — « le périmètre le plus étroit » : superlatif comparatif non sourcé,
                                       à charge assertorique maximale, contredit par la conclusion (« il ne classe pas
                                       ces offres ») et inexact (F-15 et F-32 ont chacune 1 protocole sur 2 documenté ;
                                       Temporal est plus étroit). Retitré « la frontière plateforme/bibliothèque ».
                                   RÉSERVES
                                   (1)(2) CrewAI/MCP — niveau de preuve surélevé : §7.6 range CrewAI sous le chapeau
                                       « Niveau [C] » et n'élève QUE le support A2A ; le jet lisait §6 ([B] pour les
                                       deux protocoles). Socle §7 = autorité sur le niveau de preuve (CLAUDE.md).
                                       MCP repassé en [C] ; décompte corrigé 3/1/1 -> 2/2/1 en §7.2 ET en conclusion ;
                                       « généralisé » nuancé en « répandu et inégalement établi ».
                                       >>> CONFLIT DE SOCLE §6 vs §7.6 remonté en gouvernance (non corrigé ici).
                                   (3) §7.3 — glissement de référent : Confluent cite « LangChain », le jet le traitait
                                       comme « LangGraph Platform ». C'est la confusion plateforme/OSS que le §7.2
                                       déclare décisive. Convergence bornée à CrewAI, seul référent commun.
                                   (5) §7.1 — « guides publiés depuis les deux lignées » : F-15 dit « guides de
                                       migration DevBlogs », pluriel non ventilé. Ramené à la source.
                                   (6) §7.1 — « MCP dans les agents, A2A entre les agents » entre guillemets sans
                                       verbatim (CA-5) ; le seul verbatim au socle est anglais (F-16). Guillemets ôtés,
                                       original porté. >>> Le ch. 2 hérite du même problème — signalé en gouvernance.
                                   (7)(8)(9) Métriques auto-déclarées — forme PRDPlan §4.4 (« [source, date] […]
                                       DÉCLARE ») non tenue : verbe « déclare » rétabli pour LangChain ET CrewAI ;
                                       absence de source datée au socle pour CrewAI dite explicitement.
                                   (10) §7.3 — « enseignent » / « l'enseignement des travaux de Munich » conférait
                                       l'autorité d'un résultat établi à un préprint v1 ; qualification remontée de
                                       la note 6 au corps ; « posent » / « la position des travaux ».
                                   Les 7 correctifs de l'auto-réfutation du premier jet sont conservés :
                                   (a) double négation inversant le sens (« ni d'inférer qu'aucune de ces entreprises… »
                                       -> « que ces entreprises figurent… ») ;
                                   (b) « la seule à ne pas être en GA » borné aux trois branches du corps (Temporal [C]
                                       est lui aussi en préversion — l'affirmation non bornée était réfutable) ;
                                   (c) art. 12.1 : assertion juridique remplacée par un renvoi ch. 11 + Annexe D §D.2
                                       (le fait appartient au ch. 11 ; aucun fait central F-27 n'est porté ici) ;
                                   (d) « socle empirique » -> « cadre » là où F-37 est mobilisé comme taxonomie ;
                                   (e) « encadrent » (jalons GA) supprimé — collision avec « encadrement », terme chargé
                                       de l'ouvrage ; (f) « selon que … soient » -> indicatif ; (g) « a exécuté … exécutions ».
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     6. Passe de conformité ...... fait (17 juillet 2026 — audit global, constats m-11 et m-12 ; date de gel
                                   INCHANGÉE au 16 juillet 2026, et les décomptes du chapitre y restent
                                   ancrés — aucune information nouvelle n'entre.
                                   m-11 (§7.3) : le rendu français « sur une dorsale Kafka fiable et rejouable »
                                       était présenté entre guillemets comme une citation, alors que la source
                                       (confluent.io/blog) est anglaise — CA-5 exige la langue originale. Racine
                                       (audit G-4) traitée en amont : le PRD v1.10 a versé le verbatim anglais au
                                       socle (F-33, [B], billet du 26 févr. 2026 — MÊME fait, déjà gelé). Corps :
                                       verbatim anglais porté, traduction française à sa suite. Note [^4] :
                                       verbatim et source tracés. Le cas jumeau F-16 (§7.1) était déjà conforme.
                                   m-12 (en-tête) : la thèse reproduisait « support MCP généralisé » (TOC v1.4),
                                       que le corps réfutait deux fois sur pièces (§7.2 et conclusion). Le TOC a
                                       été amendé le 17 juillet 2026 (v1.5) : « répandu et inégalement établi ».
                                       Thèse d'en-tête réalignée sur le TOC actuel — la bijection J-2 est
                                       rétablie. Les deux passages du corps ARGUMENTAIENT CONTRE l'ancienne
                                       thèse ; ils ne sont pas supprimés — leur démonstration reste juste et
                                       porte désormais la thèse au lieu de la contredire : ils mesurent ce que
                                       « répandu et inégalement établi » veut dire, et disent pourquoi
                                       « généralisé » serait faux. Décompte re-vérifié sur le corps du chapitre
                                       avant livraison : 5 offres = première main 2 (Agent Framework §7.1,
                                       Confluent §7.3) + repérage [C] 2 (Temporal et CrewAI, §7.4) + non
                                       documenté 1 (LangGraph, §7.2) — inchangé, exact, concordant entre §7.2 et
                                       la conclusion.
                                   VOLUMÉTRIE — décompte re-mesuré, et il appelle un signalement. La passe a
                                       ajouté **49 mots** au corps. Mesure au 17 juillet 2026 par la commande
                                       publiée au bloc du ch. 6 (la seule commande de décompte reproductible de
                                       la Partie II) : **3 665 mots tableau §7.5 inclus, 3 493 hors tableau**.
                                       Hors tableau : dans la cible ~3 200 ±10 % (2 880-3 520). Tableau inclus :
                                       au-dessus du plafond de 3 520.
                                       ⚠ Le décompte déclaré au point 1 ci-dessus (3 519 / 3 374) **ne se
                                       reproduit pas** sous cette commande, et il ne se reproduisait DÉJÀ PAS
                                       avant la présente passe : sur l'état gelé au 16 juillet (git HEAD), la
                                       même commande mesure **3 616 / 3 444**. L'écart est donc antérieur à ce
                                       jour et étranger aux constats m-11/m-12 ; le dépassement du plafond,
                                       tableau inclus, lui préexiste également (3 616 > 3 520). Non corrigé ici :
                                       hors mandat (l'audit ne relève pas ce défaut), et le rectifier suppose
                                       d'arbitrer quelle commande fait foi — le bloc du ch. 7 n'a jamais publié
                                       la sienne, à la différence de celui du ch. 6. **Signalé à la gouvernance**
                                       (même classe que m-31 et m-40 : un cardinal certifié qui ne se reproduit
                                       pas). Ce qui relève de cette passe est dit : + 49 mots, et la mesure du
                                       jour est ci-dessus.)
-->
