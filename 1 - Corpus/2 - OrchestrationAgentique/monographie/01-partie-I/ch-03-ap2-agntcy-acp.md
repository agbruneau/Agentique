# Chapitre 3 — La transaction agentique et la couche d'infrastructure : AP2 et AGNTCY

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-04, F-05, F-43 ; réserve F-06 ; F-02 (renvoi — A2A, ch. 1 et ch. 2) |
| Garde-fous à surveiller (PRD §8) | **R-1** (risque maximal de l'ouvrage — l'ACP protocolaire n'est pas un standard vivant) ; **R-8** (§3.4 — rappel de l'encadré des quatre branches posé au ch. 1 §1.2, développé sur le versant protocolaire ; lacune §10.7) ; §8.2.1 (métriques d'adoption auto-déclarées) ; réserve F-06 (préprint) |
| Volumétrie cible | ~2600 mots |

> **Thèse ([TOC.md](../../TOC.md))** : La transaction pilotée par agents (AP2) est l'aboutissement financier de la pile protocolaire ; AGNTCY en est la couche d'infrastructure, non un concurrent.

---

Une institution financière ne s'intéresse vraiment à un protocole d'interopérabilité que le jour où celui-ci touche à l'argent ou à l'infrastructure. Les deux objets de ce chapitre occupent précisément ces deux extrémités. AP2 (*Agent Payments Protocol*) se tient au point où la délégation à un agent cesse d'être une affaire d'ingénierie pour devenir une affaire de responsabilité : la transaction. AGNTCY se tient à l'autre bout, là où des agents se découvrent et s'échangent des messages avant même de savoir ce qu'ils feront ensemble. Entre les deux se glisse un troisième objet, dont ce chapitre raconte la disparition — le protocole ACP (*Agent Communication Protocol*) d'IBM Research — et qui livre peut-être l'enseignement le plus utile des trois.

La thèse annoncée par le plan de l'ouvrage doit ici être décomposée avec soin, car ses deux moitiés n'ont pas le même statut. Que la transaction agentique constitue l'**aboutissement financier** de la pile protocolaire est une **lecture de l'auteur** : le socle établit qu'AP2 est un protocole compagnon d'A2A (*Agent2Agent*) dédié aux transactions pilotées par agents[^1], et rien de plus sur sa centralité. Qu'AGNTCY soit une couche d'infrastructure **et non un concurrent** est, pour sa part, le **positionnement officiel déclaré** du projet[^3] — une déclaration, non un fait vérifié, et que des analyses tierces viennent nuancer. Ce chapitre tient les deux moitiés à leur juste hauteur de preuve. Il porte enfin le risque terminologique le plus élevé de l'ouvrage, et s'y consacre en dernière section.

## 3.1 AP2 : la transaction pilotée par agents

Les faits du socle sont peu nombreux et il faut résister à la tentation de les étoffer. AP2 a été lancé par Google en septembre 2025 — l'annonce de Google Cloud est datée du 16 septembre 2025 — comme **protocole compagnon d'A2A** dédié aux transactions pilotées par agents[^1]. La filiation est explicite : là où A2A régit la délégation de tâches entre agents (chapitre 2), AP2 s'attache à ce qui se passe lorsque la tâche déléguée engage un paiement.

Sur son adoption, le socle fournit un chiffre et une liste. Selon le communiqué de la Linux Foundation du 9 avril 2026, **plus de 60 organisations des paiements et des services financiers déclarent leur soutien à AP2**, parmi lesquelles Mastercard, PayPal, American Express, Adyen, Coinbase, Worldpay et Revolut[^1]. Conformément à la règle qui gouverne tout cet ouvrage, ce chiffre est **auto-déclaré** et attribué à sa source à chaque mention : **le soutien déclaré ne vaut pas déploiement en production**[^2]. La réserve attachée à l'entrée du socle est du reste explicite — il s'agit d'un endossement déclaré, non d'une adoption en production vérifiée[^1].

Posons l'intervalle : de l'annonce du 16 septembre 2025 au communiqué du 9 avril 2026, il s'écoule **moins de sept mois**. Moins de sept mois après son annonce, un protocole de paiement compte plus de soixante déclarations de soutien, si l'on en croit la Linux Foundation. **Lecture de l'auteur** : le socle n'enregistre aucun décompte au lancement — à la différence d'A2A, dont il donne les deux bornes, 50+ au départ et 150+ en avril 2026 (F-02) —, de sorte qu'aucune dynamique de croissance ne peut en être tirée.

**Lecture de l'auteur** : cette métrique-ci mérite un traitement un peu différent de celle que le chapitre 1 a critiquée. Le grief central adressé aux « organisations de soutien » d'A2A était que l'unité n'en est pas définie. Il vaut intégralement ici. Mais s'y ajoute un élément que le socle fournit et qui change la portée de la lecture : sept d'entre elles sont nommées par le communiqué — Mastercard, PayPal, American Express, Adyen, Coinbase, Worldpay, Revolut — et ce sont des réseaux de paiement et des émetteurs, c'est-à-dire précisément les acteurs sans lesquels aucune transaction agentique ne peut aboutir. Sept noms d'infrastructures de paiement sont qualitativement plus informatifs qu'un décompte entièrement anonyme — non parce qu'ils prouvent un déploiement, mais parce qu'ils identifient qui aurait à bouger. Le socle établit ces sept noms ; il n'établit ni la liste complète des soutiens déclarés, ni que ces organisations aient bougé.

Un second point de gouvernance doit être posé sans le durcir. **Le socle ne documente aucun transfert de gouvernance d'AP2 à une fondation**[^1]. Ce n'est pas un fait négatif vérifié — le chapitre 14 montrera, à propos du standard technique du cadre bancaire canadien, ce qu'exige un véritable fait négatif : une recherche exhaustive et infructueuse dans les textes officiels. Ici, il s'agit d'une **absence de documentation dans le socle**, ce qui est plus faible, et doit se dire tel quel. La distinction n'est pas rhétorique : elle décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable.

**Lecture de l'auteur**, en conséquence : le raisonnement du chapitre 1 — la gouvernance neutre transforme la question de diligence en question de constat — ne s'étend pas à AP2 en l'état du socle. On notera que c'est la Linux Foundation qui, le 9 avril 2026, publie les chiffres de soutien d'AP2 en même temps que ceux d'A2A[^1] ; l'indice est suggestif, il n'établit rien. Le socle ne dit pas qu'AP2 est resté propriétaire ; il dit qu'il ne documente pas le contraire. Une institution qui envisagerait AP2 devrait vérifier ce point à la source avant d'en faire un argument.

Il faut enfin dire ce que ce chapitre ne peut pas écrire. **Le socle ne contient aucune anatomie technique d'AP2** : ni structure des messages, ni mécanique de mandat, ni modèle de preuve d'intention. Le chapitre 2 peut décrire MCP (*Model Context Protocol*) et A2A parce que le socle en porte la matière ; ce chapitre ne le peut pas pour AP2, et s'y refuse plutôt que d'emprunter à une connaissance non tracée. Quant à l'articulation d'AP2 avec les rails de paiement canadiens — le RTR (*Real-Time Rail*), Interac —, aucune source ne la documente : c'est une lacune assumée du socle, traitée au chapitre 16, qui lui consacre un chapitre explicitement prospectif.

## 3.2 AGNTCY : la couche d'infrastructure

AGNTCY a été ouvert par Cisco en mars 2025, avec LangChain et Galileo, et placé sous la Linux Foundation le **29 juillet 2025** — soit quatre mois plus tard[^3]. Ses membres formateurs sont Cisco, Dell Technologies, Google Cloud, Oracle et Red Hat[^3]. Le communiqué de la Linux Foundation du 29 juillet 2025 fait état de **plus de 65 entreprises déclarant leur soutien au projet** — chiffre auto-déclaré, attribué ici à ce communiqué, daté de juillet 2025, et qui ne vaut pas plus déploiement en production que celui d'AP2[^2] ; le socle n'en enregistre aucune actualisation ultérieure[^3]. Il serait donc fautif de le comparer aux chiffres d'avril 2026 d'A2A ou d'AP2 : plus de huit mois séparent ces relevés — du 29 juillet 2025 au 9 avril 2026 —, et aucune évolution du décompte d'AGNTCY n'est documentée.

Le contenu du projet, tel que le socle le porte, tient en deux capacités : des **annuaires de découverte** (*discovery directories*) et un transport nommé **SLIM**[^3]. C'est un vocabulaire d'infrastructure, non d'application : découvrir quels agents existent, et acheminer ce qu'ils s'envoient. Le socle n'en dit pas davantage — ni spécification, ni statut de maturité, ni version. Ce chapitre s'en tient là.

Le positionnement officiel du projet est celui d'une couche **interopérable avec A2A et MCP, non concurrente**[^3]. Cette formule est une déclaration du projet, et doit être lue comme telle : elle relève de la même catégorie que les métriques auto-déclarées, et le socle ne la valide pas. Il fournit en revanche un élément de contexte qui mérite d'être posé, parce qu'il se lit dans le rapprochement de deux entrées : **Google Cloud figure parmi les membres formateurs d'AGNTCY**[^3], alors que Google est l'organisation qui a lancé A2A puis AP2[^1] — le socle nomme les deux entités séparément et n'établit pas formellement leur rattachement. **Lecture de l'auteur** : en tenant Google Cloud pour une division de Google, un même groupe se trouve des deux côtés — créateur des protocoles d'échange, membre formateur de la couche d'infrastructure.

**Lecture de l'auteur** : cette double présence est cohérente avec la thèse de la complémentarité, et c'est bien ainsi qu'on la lira dans les documents promotionnels. Mais la cohérence n'est pas une preuve. Le socle établit une composition de membres et un positionnement déclaré ; il n'établit pas que les deux couches soient effectivement complémentaires dans les faits, ni qu'elles le resteront. La nuance suivante montre pourquoi la prudence s'impose.

Car le socle porte un second élément, et il va dans l'autre sens : **des analyses tierces relèvent un chevauchement entre la composante ACP d'AGNTCY et A2A**[^3]. Cette observation n'est pas endossée par le socle — c'est un constat de tiers (corroborations VentureBeat, Forbes), attribué comme tel et non vérifié en source primaire. Elle ne permet pas d'endosser le chevauchement comme un fait ; elle suffit à rappeler que le positionnement « non concurrent » demeure une position déclarée du projet, que des analyses tierces viennent nuancer. Que ces analyses contestent le positionnement lui-même n'est pas établi par le socle. Et elle ouvre le dossier terminologique le plus délicat de l'ouvrage, que la section 3.4 traite.

## 3.3 Le destin de l'ACP protocolaire : une fusion, non un abandon

Le 17 mars 2025, IBM Research lance la plateforme BeeAI et, avec elle, un protocole de communication entre agents baptisé ACP (*Agent Communication Protocol*) — en version pré-alpha, d'abord conçu comme une extension de MCP, et confié à la Linux Foundation dès ce mois de mars[^4]. Le 28 mai 2025, un billet d'IBM Research en précisait la doctrine : l'ACP protocolaire était RESTful sur HTTP, présenté comme complémentaire de MCP, et portait l'ambition déclarée, dans les mots de Kate Blair, d'en faire « the HTTP of agent communication »[^4].

Le 29 août 2025, le blog de LF AI & Data acte la **fusion officielle de l'ACP protocolaire dans A2A**[^4]. Le socle en détaille les termes, et ils importent : le développement actif de l'ACP protocolaire **cesse** ; ses actifs sont **versés à A2A** ; Kate Blair (IBM Research) **rejoint le comité de pilotage technique** (*technical steering committee*) d'A2A ; BeeAI **adopte A2A par adaptateurs** ; des **guides de migration** sont fournis[^4].

Posons les intervalles, à partir des seules dates du socle. Du lancement du 17 mars 2025 à la fusion du 29 août 2025 : **cinq mois et douze jours**. Du billet du 28 mai 2025, qui affichait l'ambition de devenir le HTTP de la communication entre agents, à la fusion du 29 août 2025 : **trois mois et un jour**.

De là découle la règle de rédaction la plus stricte de cet ouvrage, et le présent chapitre est celui où le risque de l'enfreindre est maximal : **l'ACP protocolaire ne doit jamais être présenté comme un standard vivant**[^6]. Son développement actif a cessé le 29 août 2025 ; il ne subsiste qu'à travers A2A et les adaptateurs de BeeAI. Tout emploi au présent, toute mise en parallèle avec MCP ou A2A comme s'il s'agissait de trois options ouvertes, est une erreur de fait. Le chapitre 1 a traité le versant gouvernance de cet épisode — un concurrent déclaré devenu codécideur ; le présent chapitre en tire le versant protocolaire.

Ce versant tient en trois faits que le socle porte : actifs versés, adaptateurs livrés, guides de migration fournis[^4]. **Lecture de l'auteur** : ce sont les gestes d'une transition organisée, non ceux d'un projet qu'on éteint. La fusion n'a pas été un abandon.

**Lecture de l'auteur**, et l'inférence est ici substantielle : ce que cet épisode enseigne à un architecte n'est pas que la gouvernance neutre protège un protocole de l'obsolescence — elle ne l'a manifestement pas fait, l'ACP protocolaire ayant été confié à la Linux Foundation en mars 2025 et son développement ayant cessé cinq mois et douze jours après son lancement. Ce qu'il enseigne est plus fin : l'obsolescence a été **ordonnée** plutôt que subie, et l'on peut y lire l'effet de la gouvernance neutre. Le socle établit les faits de la transition ; il n'établit pas que la gouvernance en soit la cause. Mais la distinction entre les deux risques — le protocole peut mourir, l'utilisateur peut être abandonné — est celle que tout dossier de risque de tiers devrait porter, et elle est rarement faite.

Un dernier enseignement, historiographique celui-là. Le survey de référence de la période (Ehtesham et al., arXiv 2505.02279, mai 2025) — **préprint non révisé par les pairs**, dont le cadre est repris ici à titre de jalon et jamais comme guidance[^5] — prescrivait une adoption séquentielle MCP → ACP protocolaire → A2A → ANP. La fusion du 29 août 2025 a vidé la deuxième étape de sa substance **moins de quatre mois** après la publication. Une institution qui aurait bâti sa feuille de route protocolaire sur ce document au printemps 2025 aurait, à l'été, investi dans une étape devenue sans objet. Le chapitre 1 en tire la leçon de méthode. **Lecture de l'auteur** : on retiendra ici la leçon d'architecture — dans ce cas au moins, une prescription protocolaire s'est périmée plus vite qu'un cycle budgétaire ; le socle n'établit pas que ce soit la règle du domaine.

## 3.4 Le versant protocolaire de la désambiguïsation (R-8)

L'encadré de désambiguïsation des quatre emplois du sigle « ACP » est **posé au chapitre 1, section 1.2**, qui porte la première occurrence du sigle dans l'ouvrage ; il n'est pas reproduit ici. La règle qu'il fixe s'applique à tout l'ouvrage et sans exception : **le sigle « ACP » employé seul est proscrit**, chaque emploi portant son qualificatif complet, selon les formes imposées par le glossaire[^6].

Ce chapitre en développe le versant qui le concerne : sur les quatre objets, **deux au moins ne relèvent pas du champ protocolaire**. L'***Agentic Control Plane*** est le programme phare du consortium d'IA Lightworks–Scotiabank–Sun Life–TELUS, traité au chapitre 17 ; le positionnement d'IBM comme *agentic control plane* est un positionnement marketing qu'IBM applique à l'un de ses produits depuis mai 2026 — attribué à IBM à chaque occurrence — et traité au chapitre 22[^6]. Ni l'un ni l'autre n'est un protocole ; ni l'un ni l'autre n'a le moindre rapport avec la matière du présent chapitre. Le socle les tient pour des objets distincts (R-8) ; il ne dit rien de l'origine de leurs dénominations.

Restent l'ACP protocolaire d'IBM Research et la composante ACP d'AGNTCY, et c'est entre eux que la confusion est à la fois la plus facile et la plus dommageable : le premier, dont la section 3.3 vient de retracer la fusion dans A2A ; la seconde, dont la section 3.2 a rapporté que des analyses tierces lui prêtent un chevauchement avec A2A — le socle n'en établit ni l'intitulé complet, ni la nature, ni l'identité avec le premier[^3]. Deux objets nommés du même sigle, tous deux mis en rapport avec A2A par les sources. La coïncidence est telle qu'un lecteur pressé conclura à l'identité — et le socle ne permet pas de le suivre.

Cette question — la composante ACP d'AGNTCY est-elle l'ACP protocolaire d'IBM Research ? — est posée en encadré au chapitre 1, section 1.2, et reprise au chapitre 21 : le socle n'établit ni l'intitulé complet de la composante, ni son identité — ou sa non-identité — avec l'ACP protocolaire d'IBM Research[^7]. En l'absence de source primaire, la question reste ouverte et **aucune inférence n'est proposée ici**.

L'enjeu de cette prudence n'est pas cosmétique. Si les deux objets étaient un seul, la fusion d'août 2025 vaudrait pour AGNTCY, et le chevauchement relevé par les tiers serait le vestige d'un protocole éteint. S'ils sont deux, AGNTCY porte une composante active dont le rapport à A2A reste à qualifier. Les deux hypothèses conduisent à des conclusions d'architecture opposées, et le socle ne tranche pas. Un ouvrage qui trancherait ici gagnerait en fluidité ce qu'il perdrait en droit d'être cru.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

**Premièrement**, la transaction agentique dispose d'un protocole dédié : AP2, compagnon d'A2A, lancé par Google en septembre 2025, auquel plus de 60 organisations des paiements et des services financiers déclarent leur soutien selon le communiqué de la Linux Foundation du 9 avril 2026 — un endossement déclaré, dont sept organisations seulement sont nommées par le communiqué, non une adoption en production vérifiée[^1]. **Deuxièmement**, AGNTCY se déclare couche d'infrastructure interopérable et non concurrente ; c'est le positionnement du projet, que des analyses tierces nuancent en relevant un chevauchement entre sa composante ACP et A2A[^3]. **Troisièmement**, l'ACP protocolaire d'IBM Research n'existe plus comme standard vivant depuis le 29 août 2025 ; sa fusion dans A2A fut organisée — actifs versés, adaptateurs, guides de migration[^4].

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne décrit pas l'anatomie technique d'AP2 : le socle ne la porte pas, et cet ouvrage n'écrit pas ce qu'il ne peut pas tracer. Il ne dit pas qu'AP2 soit gouverné par une fondation, ni qu'il ne le soit pas — il dit que le socle n'en documente pas le transfert. Il ne dit pas qu'AP2 puisse s'articuler aux rails de paiement canadiens : aucune source ne le documente, et le chapitre 16 traite la question au conditionnel qui lui revient. Il ne dit pas que la composante ACP d'AGNTCY soit, ou ne soit pas, le protocole d'IBM Research. Il ne dit rien, enfin, de la sûreté de ces protocoles : le chapitre 4 en dresse la taxonomie des risques.

La pile protocolaire est désormais posée. Reste à savoir ce qu'elle laisse à découvert.

---

## Notes

[^1]: PRD §7.1, **F-04** (niveau [A]). Sources primaires : annonce Google Cloud du 16 septembre 2025 ; communiqué de la Linux Foundation du 9 avril 2026 (60+ organisations des paiements et services financiers ; Mastercard, PayPal, American Express, Adyen, Coinbase, Worldpay, Revolut). **Réserve F-04** : endossement déclaré, pas adoption en production vérifiée. Le socle ne documente aucun transfert de gouvernance d'AP2 à une fondation (voir ch. 1, conclusion). Attribution de Google comme organisation de lancement d'A2A puis d'AP2 : PRD §7.1, **F-02** et **F-04**.

[^2]: PRD §8.2.1 (règle d'attribution des métriques d'adoption des protocoles — auto-déclarées, attribuées au communiqué) ; formulation imposée par PRDPlan §4.4 (« soutien ≠ production »).

[^3]: PRD §7.1, **F-05** (niveau [A]). Source primaire : communiqué de la Linux Foundation du 29 juillet 2025 (mise sous Linux Foundation ; 65+ entreprises ; membres formateurs Cisco, Dell Technologies, Google Cloud, Oracle, Red Hat ; annuaires de découverte et transport SLIM ; positionnement officiel non concurrent) ; corroborations VentureBeat, Forbes. Le chevauchement relevé entre la composante ACP d'AGNTCY et A2A est une **analyse tierce**, attribuée comme telle et non endossée par le socle.

[^4]: PRD §7.8, **F-43** (niveau [B]). Sources primaires : blogs research.ibm.com (lancement de BeeAI et du protocole ACP, 17 mars 2025, pré-alpha et extension de MCP à l'origine, don à la Linux Foundation en mars 2025 ; billet du 28 mai 2025 — l'ACP protocolaire RESTful sur HTTP, présenté comme complémentaire de MCP, citation « the HTTP of agent communication » attribuée à Kate Blair) ; blog LF AI & Data du 29 août 2025 (fusion officielle dans A2A : arrêt du développement actif, apport des actifs, entrée de Kate Blair au comité de pilotage technique d'A2A, adaptateurs BeeAI, guides de migration) ; github.com/orgs/i-am-bee. Intervalles calculés à partir de ces seules dates : 17 mars → 29 août 2025 = cinq mois et douze jours ; 28 mai → 29 août 2025 = trois mois et un jour.

[^5]: PRD §7.1, **F-06** (confiance moyenne — usage descriptif seulement). Ehtesham et al., arXiv 2505.02279, mai 2025. **Réserve majeure** : préprint non révisé par les pairs ; l'étape ACP protocolaire de la séquence MCP → ACP protocolaire → A2A → ANP est devenue obsolète comme prescription après la fusion du 29 août 2025 (F-43). Cité comme jalon historiographique, jamais comme guidance. « Moins de quatre mois » : de la publication (mai 2025) à la fusion (29 août 2025).

[^6]: PRD §8.1, garde-fous **R-1** (l'ACP protocolaire n'est pas un standard vivant) et **R-8** (quatre emplois distincts de « (agentic) control plane » / « ACP » ; sigle seul proscrit dans tout l'ouvrage). Encadré de désambiguïsation **posé au ch. 1 §1.2**, non dupliqué ici. Formes imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.1. Branche (b) — *Agentic Control Plane* du consortium Lightworks–Scotiabank–Sun Life–TELUS : PRD §7.5, **F-48** (ch. 17 §17.8). Branche (c) — positionnement d'IBM comme *agentic control plane* depuis Think 2026 (5 mai 2026), attribué à IBM à chaque occurrence : PRD §7.8, **F-42** (ch. 22 §22.2).

[^7]: PRD **§10.7** (lacune ouverte le 16 juillet 2026 à la rédaction du ch. 1) : « aucune source du socle n'établit l'intitulé complet de cette composante ni son identité — ou sa non-identité — avec le protocole ACP d'IBM Research ». Source à retrouver, identifiée par le PRD : documentation primaire AGNTCY (`docs.agntcy.org` ou dépôt GitHub du projet). Quatrième branche du garde-fou R-8 ; reprise au ch. 21.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (7 notes ; termes anglais entre parenthèses et en italique à la 1re occurrence
                                   du chapitre : AP2, A2A, MCP, ACP, discovery directories, technical steering committee, RTR)
     3. Balayage garde-fous ...... refait après relecture (le balayage du 1er jet était déclaré fait mais avait manqué
                                   l'occurrence R-1 la plus exposée du chapitre — voir point 4)
                                   (R-1 : ACP protocolaire toujours qualifié ; propriétés du protocole au passé ; présent de
                                   narration conservé pour les seuls événements datés (17 mars / 29 août 2025), qui ne
                                   présentent pas un standard vivant ; fusion dite ;
                                   R-8 : sigle jamais nu (séquence F-06 qualifiée « MCP → ACP protocolaire → A2A → ANP ») ;
                                   encadré du ch. 1 rappelé par renvoi et NON dupliqué ; branches (b)/(c) renvoyées aux ch. 17
                                   et 22 et caractérisées selon D.1 (programme phare du consortium d'IA ; positionnement
                                   marketing attribué à IBM) ; branche (d) : nature jamais prédiquée ;
                                   §8.2.1 : 60+ AP2 et 65+ AGNTCY attribués à leur communiqué ET porteurs de la clause
                                   « soutien ≠ production » — traitement désormais symétrique ;
                                   réserve F-06 : formulation « préprint » imposée appliquée ;
                                   réserve F-01 : « sécurisé » absent du chapitre)
     4. Relecture adversariale ... fait — deux relecteurs indépendants, premier jet réfuté.
                                   RÉFUTÉ ET CORRIGÉ (4 bloquants) :
                                   (1) R-1 — « l'ACP protocolaire EST RESTful sur HTTP, complémentaire de MCP, et PORTE
                                       l'ambition » : trois propriétés au présent pour un protocole dont le développement a
                                       cessé le 29 août 2025 ; reconstituait quasi mot pour mot la proposition réfutée R-1.
                                       Le chapitre s'auto-réfutait six lignes plus bas. → passé, sur le modèle du ch. 1.
                                   (2) R-8 (d)/§10.7 — la composante ACP d'AGNTCY était rangée « de nature protocolaire »
                                       (« deux seulement sont de nature protocolaire », « tous deux situés dans le champ
                                       protocolaire ») alors que le socle n'en établit même pas l'intitulé complet : nature
                                       prédiquée par inférence non marquée, contredisant l'encadré du chapitre lui-même.
                                       → nature jamais prédiquée ; « mis en rapport avec A2A par les sources ».
                                   (3) F-05 — « le positionnement non concurrent est une position déclarée, CONTESTÉE par des
                                       observateurs » et « elle suffit à ÉTABLIR » : le socle dit que des tiers relèvent un
                                       chevauchement, pas qu'ils contestent le positionnement ; et une observation non
                                       endossée par le socle n'établit rien. → aligné sur le ch. 1 (« nuancer »).
                                   (4) Bijection §10.7 — second encadré « État de la connaissance vérifiable » sur la même
                                       question que le ch. 1 §1.2, alors que le PRD l'assigne au ch. 1 et au ch. 21 et que le
                                       TOC dit « Ne pas dupliquer l'encadré du ch. 1 » — le chapitre promettait d'ailleurs
                                       « il n'est pas reproduit ici ». → encadré supprimé, remplacé par un renvoi ; le
                                       paragraphe d'enjeu architectural (contribution propre du ch. 3) est conservé.
                                   RÉSERVES CORRIGÉES (13/14) : liste AP2 bornée aux sept noms du communiqué (« liste
                                   nominative » / « nommément identifiable » = embellissement au-delà de F-04, 53+ soutiens
                                   ne sont pas identifiables) ; dynamique de croissance d'AP2 démarquée (aucun décompte au
                                   lancement au socle, contrairement à A2A) ; 65+ AGNTCY porte enfin « soutien ≠ production »
                                   (§8.2.1 le nomme explicitement — asymétrie avec AP2 corrigée) ; branche (c) rendue à
                                   « positionnement marketing » (D.1) au lieu d'« expression descriptive » (requalification à
                                   la baisse au bénéfice du fournisseur, §8.4) ; branche (b) n'est plus « un programme
                                   d'institutions financières » (Lightworks et TELUS n'en sont pas — F-48) ; « homonymie
                                   intégrale et FORTUITE » → le socle ne dit rien de l'origine des dénominations ;
                                   Google Cloud ≠ Google : le pas d'identification est rendu visible et marqué ;
                                   « le socle porte INTÉGRALEMENT » → trois faits portés, caractérisations marquées ;
                                   « la gouvernance A PERMIS que » → causalité que le socle n'établit pas ;
                                   « dans ce domaine une prescription SE PÉRIME » → généralisation d'un cas unique, marquée
                                   et restreinte ; sigles nus des notes [^4] et [^5] qualifiés.
                                   RÉSERVE DEVENUE SANS OBJET (1/14) : la contradiction « Recherche menée » / « Aucune passe
                                   de recherche n'a encore été conduite » vivait dans l'encadré supprimé au bloquant 4.
                                   Le besoin de gouvernance qu'elle révèle (PRDPlan §4.4 ne prévoit pas la forme d'une
                                   lacune ouverte mais non encore instruite) est remonté au parent, non tranché ici.
                                   Volumétrie : 2842 mots (cible 2600, tolérance 2340-2860) — dans la tolérance.
     5. Commit + registre de gel . fait (ligne du ch. 3 au registre `99-registre-gel.md`, commit `cb4608f`
                                   « revise chapter 3 after adversarial review »)
     6. Passe de conformité (audit du 17 juill. 2026 — aucune information nouvelle, date de gel inchangée) :
        m-08 — bloc « 5. Commit + registre de gel : À FAIRE » périmé (le chapitre est enregistré au registre) ;
               corrigé. Aucune autre modification : le corps n'était visé par aucun constat de l'audit.
-->
