# Chapitre 23 — Correspondance réglementaire et flux illustratifs

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-39 à F-42, F-44 à F-46 ; F-09, F-15, F-17, F-23, F-25, F-26, F-27, F-28, F-29, F-32, F-33, F-34, F-35, F-36, F-37 (renvois) ; PRD Annexe B.3–B.4 |
| Garde-fous à surveiller (PRD §8) | **R-5** (aucun standard technique désigné), **R-7** (aucune conformité E-23/B-13 revendiquée par IBM), R-6 et R-8 (par renvoi au ch. 22) ; §8.2.7 (études commandées) ; §8.4 (neutralité fournisseur) ; **CA-8** |
| Volumétrie cible | ~3400 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Chaque lien blueprint ↔ réglementation est documenté ou inférence — jamais confondu ; trois flux de bout en bout le démontrent.

---

Un architecte qui présente un blueprint à son comité de risque sera arrêté par une question, et une seule : *cette plateforme nous rend-elle conformes ?* Le présent chapitre répond non — et consacre l'essentiel de son propos à établir ce que l'on peut dire à la place, avec quel degré de certitude, et à quel prix documentaire.

La raison en est simple et tient à un fait négatif du socle, établi au niveau [B] et central : **aucune source ne relie le portefeuille IBM à la ligne directrice E-23 du BSIF ni à la ligne directrice B-13**[^1]. Ce n'est pas une lacune de recherche que l'on comblerait avec un effort supplémentaire ; c'est un constat sur ce que l'éditeur revendique, et il commande la forme de tout ce chapitre. Un composant peut *outiller* une exigence sans que quiconque l'ait certifié conforme à cette exigence ; le rapprochement, alors, appartient à l'auteur du blueprint — c'est-à-dire à l'institution qui le porte, et qui en répondra.

Le chapitre 22 a posé les principes du blueprint et sa vue en couches C1–C8 ; on n'y revient pas. Le chapitre 13 a établi le principe directeur — les contraintes réglementaires deviennent des *frames* déterministes, le processus orchestre les agents et jamais l'inverse[^2]. Ce chapitre-ci fait le travail intermédiaire, ingrat et indispensable : il développe le tableau de correspondance réglementaire de l'Annexe B.3 en marquant chaque lien de son statut, puis il éprouve ces correspondances sur trois flux de bout en bout, tirés de l'Annexe B.4.

## 23.1 Le tableau B.3 développé : quatre statuts, sept liens

Le tableau ci-dessous reprend la correspondance réglementaire spécifiée à l'Annexe B.3 du PRD. Sa colonne décisive n'est pas celle de la réponse d'architecture : c'est celle du statut.

| Exigence | Réponse d'architecture (couche) | Socle | Statut du lien |
|---|---|---|---|
| E-23, risque de modélisation (1er mai 2027) | C6 : inventaire (champs de l'Appendice 1), cotation de risque graduée, cycle de vie à cinq volets, documentation de modèle ; C7 : surveillance continue | F-09, F-44 | **Inférence d'auteur — fait négatif établi** |
| Ligne directrice IA de l'AMF (1er mai 2027) | C6 + paliers de risque d'entreprise | F-25, F-44 | Inférence d'auteur |
| Loi 25, art. 12.1 (décision automatisée) | C5/C6 : humain-dans-la-boucle outillé ; explicabilité par fiches et traces | F-27, F-42, F-44 | Inférence d'auteur |
| ACVM, avis 11-348 (autonomie/adaptativité) | C1/C7 : passerelles d'audit de chaque interaction ; traçabilité par tâche | F-26, F-40, F-44 | Inférence d'auteur |
| Cadre bancaire axé sur le consommateur (C-15) | C1 : passerelles pour les API du standard technique **à venir** | F-34, F-35, F-40 | **Attente réglementaire — ne rien anticiper** |
| Rails de paiement (Lynx ISO 20022, RTR) | C3 : messagerie et intégration ISO 20022 ; continuité opérationnelle d'IBM Canada | F-28, F-29, F-39, F-45 | **Documenté** pour le rôle d'IBM ; solution ISO 20022 au niveau [C] |
| B-13 (technologie et cyber) | C8 : IBM Cloud for Financial Services, souveraineté, résidence des données | F-45 | **Inférence d'auteur — fait négatif établi** |

Quatre statuts, donc, et l'ordre dans lequel on les lit importe.

**Premier statut — l'inférence d'auteur adossée à un fait négatif établi.** Deux lignes seulement le portent : E-23 et B-13. La formulation en est verrouillée par le plan d'exécution et doit être reprise à chaque occurrence : *le rapprochement entre watsonx.governance et E-23 est une inférence d'auteur ; IBM ne revendique aucune conformité à E-23, et aucune source ne documente ce lien*[^1]. La même phrase vaut, mot pour mot, pour IBM Cloud for Financial Services et B-13. Ce que le socle établit, ici, ce n'est pas que le rapprochement soit faux — c'est qu'il n'est adossé à personne d'autre qu'à l'auteur.

Encore faut-il dire ce que ce rapprochement recouvre, faute de quoi le lecteur ne saurait pas ce qu'il est invité à ne pas croire. Le socle documente que watsonx.governance, disponible depuis décembre 2023, gère, surveille et gouverne les modèles — équité, biais, dérive, fiches de modèles (*model cards*) — et qu'une gouvernance agentique lui a été ajoutée en 2025 : Evaluation Studio pour les applications agentiques, Risk Atlas incluant les risques agentiques, inventaire par défaut, catalogue agentique gouverné (*Governed Agentic Catalog*)[^3]. Le chapitre 9 a établi, de son côté, qu'E-23 attend un cadre de gestion du risque de modélisation dont la définition de « modèle » englobe les méthodes d'IA et d'apprentissage automatique, d'où une couverture implicite de l'agentique que les analystes juridiques canadiens tiennent pour acquise[^4]. Le parallèle entre les deux — inventaire, cotation graduée par le risque, cycle de vie documenté — est immédiat à l'œil de l'architecte, et l'extraction du texte intégral d'E-23 du 16 juillet 2026 en a tracé les attentes une à une[^4]. Il n'est écrit nulle part. **Lecture de l'auteur** : la ressemblance des vocabulaires est un indice d'outillage possible, pas une preuve de couverture ; c'est à l'institution qu'il reviendra de démontrer, pièce par pièce, que ce que l'outil produit satisfait ce que la ligne directrice attend. Le socle porte les deux objets ; il ne porte pas le pont entre eux.

**Deuxième statut — l'inférence d'auteur simple.** Trois lignes : la ligne directrice sur l'IA de l'AMF, l'article 12.1 de la Loi 25, l'avis 11-348 de l'ACVM. La formulation change, et le changement n'est pas cosmétique : on écrit que le rapprochement est une inférence d'auteur, **et rien de plus**[^5]. Il serait faux d'y ajouter qu'IBM ne revendique aucune conformité, car le socle atteste le contraire dans le principe général : l'add-on « Compliance Accelerators », issu d'un accord OEM avec Credo AI daté du 28 avril 2025, offre des contenus de conformité prêts pour l'AI Act européen, l'ISO/IEC 42001 et le NIST AI RMF[^3]. IBM revendique donc bel et bien des correspondances réglementaires — simplement, aucune de celles-là n'est canadienne. Le fait négatif est borné à E-23 et à B-13 ; l'étendre serait une faute symétrique de celle qu'on cherche à éviter.

La ligne de l'article 12.1 mérite un examen plus sévère que les autres, parce qu'elle porte, telle qu'elle est spécifiée, une ambiguïté que le chapitre 11 a précisément défaite. L'Annexe B.3 y répond par « humain-dans-la-boucle (*human-in-the-loop*) outillé » dans les workflows d'orchestration. Or le chapitre 11 a établi que **l'humain-dans-la-boucle et la révision humaine de l'article 12.1 ne sont pas la même chose** : le premier est un point d'arrêt inséré dans l'exécution, la seconde un recours ouvert à la personne concernée, sur demande, après que la décision a été rendue[^6]. Outiller le premier n'outille pas la seconde. **Lecture de l'auteur** : la réponse d'architecture de l'Annexe B.3 est donc à lire en deux temps, et c'est le second qui compte. Le point d'arrêt sert la voie où l'institution cherche à écarter le critère d'exclusivité — voie qui repose sur une analyse de cabinet au niveau de preuve [C], non confrontée aux positions de la Commission d'accès à l'information[^6]. Ce qui sert la troisième obligation, si l'article s'applique, est d'une autre nature : ce sont les traces et les fiches qui permettent de restituer *a posteriori* les raisons, les principaux facteurs et paramètres ayant mené à une décision individuelle. Le socle documente l'existence de ces traces — journaux d'audit d'identité et de références (*credentials*), traces AgentOps, tableaux de bord de jetons (*tokens*) et de latence chez watsonx Orchestrate[^7] ; observabilité des agents et évaluations en continu chez Instana, en préversion publique[^3]. Il n'établit pas qu'elles restituent ce que l'article 12.1 exige. Personne ne l'a établi.

**Troisième statut — le lien documenté.** Une seule ligne : les rails de paiement. Et il faut mesurer exactement ce qui y est documenté. Le socle établit qu'IBM Canada est le partenaire technologique principal (*lead technology partner*) de Lynx depuis l'annonce du 2 mai 2019 — hébergement, intégration de systèmes, bascule LVTS→Lynx, exploitation — et partenaire de livraison et d'exploitation du Real-Time Rail depuis le 16 avril 2024, aux côtés de CGI, d'Interac et de Deloitte Canada — ce dernier au rôle non détaillé par la source (ch. 15 §15.2)[^8]. Voilà ce qui est documenté : **un rôle opérationnel, non une conformité**. Le garde-fou est explicite sur ce point et le chapitre 22 l'a rappelé : le rôle d'IBM Canada dans Lynx et le RTR est un fait de contexte, pas un argument de conformité[^9]. Une institution qui écrirait dans son dossier réglementaire que sa plateforme est adaptée aux rails canadiens *parce que* leur exploitant technologique en est l'éditeur commettrait un enchaînement que ni le socle ni le bon sens ne portent.

**Quatrième statut — l'attente réglementaire.** Une ligne, celle du cadre bancaire axé sur le consommateur, et un seul mot d'ordre : ne rien anticiper. Le paragraphe 23.4 y revient.

## 23.2 Flux 1 — la décision de crédit assistée par agents : le processus commande, OO3 ou OO4

Le premier flux instancie le principe directeur sur l'un des cas d'usage agentiques canadiens les mieux documentés par source primaire. Le chapitre 17 a établi que TD a annoncé le 21 mai 2026 son premier modèle d'IA agentique, développé par Layer 6 : pré-adjudication du prêt garanti par l'immobilier et génération de mémos de synthèse pour les souscripteurs, avec un traitement déclaré passant de ~15 heures à moins de 3 minutes — une métrique auto-déclarée par TD, non vérifiée indépendamment[^10]. Le flux ci-dessous n'est pas celui de TD, dont le socle ne documente aucun composant d'architecture ; c'est le flux type de l'Annexe B.4, sur le portefeuille du blueprint.

Sa propriété structurante tient en une phrase : **le workflow déterministe orchestre les agents, et c'est lui qui décide de l'enchaînement**. Le flux d'intégration (App Connect Enterprise) ou le workflow d'orchestration (watsonx Orchestrate) appelle des agents de synthèse documentaire ; il ne leur délègue ni la séquence, ni la décision de s'arrêter, ni la production du journal. **Lecture de l'auteur** : l'Annexe B.4 retient OO4 pour ce flux ; le socle n'établit pas que les agents invoqués y soient conscients du processus, or c'est cette conscience qui sépare OO4 d'OO3 au chapitre 5[^11]. Sur les seuls faits documentés, rien ne distingue les deux options — le positionnement est une inférence, à vérifier sur chaque configuration (ch. 22 §22.2). Ce qui est établi est ce qui compte pour la suite : le processus commande, soit OO3 au moins.

Trois points de passage obligés en découlent. **Le premier est la passerelle.** Chaque appel au modèle transite par l'AI Gateway, documentée par IBM depuis mai 2024 et étendue en janvier 2025 : limites de débit par requêtes ou par jetons, cache de réponses, masquage, chiffrement, audit[^12]. Le deuxième principe directeur (Annexe B.1) est ici sans exception — aucune interaction IA non gouvernée — et sa traduction est un point de contrôle traversé, pas une politique déclarée. **Le deuxième est le mémo au souscripteur humain.** C'est un humain-dans-la-boucle au sens strict : un point d'arrêt inséré avant la décision. On a vu au paragraphe précédent ce qu'il ne fait pas — il n'outille pas la révision de l'article 12.1 — et le blueprint ne doit pas prétendre le contraire. **Le troisième est la trace.** Elle est produite par la plateforme, non par les agents : c'est un enseignement explicite du cadre académique retenu, selon lequel la journalisation confiée aux agents n'est généralement pas recommandée[^11]. Le socle documente les traces AgentOps d'Orchestrate et l'observabilité des agents par Instana, cette dernière en préversion publique à Think 2026[^7][^3] ; l'inventaire des modèles et des agents relève de watsonx.governance[^3].

**Lecture de l'auteur** : ce flux ne démontre pas la conformité d'un dossier de crédit ; il démontre qu'un dossier de crédit peut être instruit par des agents sans que quiconque perde la maîtrise de l'enchaînement, ni la capacité de dire ce qui s'est produit. C'est exactement ce que le chapitre 13 appelle un *frame* opérationnel, et c'est tout ce que l'architecture peut apporter. Les trois obligations de l'article 12.1 — informer au moment de la décision, expliquer sur demande, offrir la révision — restent des obligations de l'institution, dont le socle n'établit pas qu'un composant les satisfasse.

## 23.3 Flux 2 — le paiement ISO 20022 vers Lynx : l'agent observe, le rail exécute

Le deuxième flux est l'inverse du premier, et c'est pour cela qu'il figure ici.

L'émission d'un paiement de grande valeur vers Lynx est un traitement transactionnel déterministe. Le chapitre 15 a établi que Lynx a achevé sa bascule : fin de la coexistence MT/MX le 22 novembre 2025, alignée sur l'échéance mondiale SWIFT CBPR+, au profit des messages pacs.008 et pacs.009[^13]. Côté plateforme, le socle documente IBM MQ 10.0 LTS (disponibilité générale en juin 2026) : messagerie transactionnelle « exactly-once » selon la documentation de l'éditeur, haute disponibilité native avec réplication intra et inter-régions, cryptographie post-quantique pour TLS, OpenTelemetry[^14]. App Connect Enterprise 13 assure l'intégration applicative, et IBM documente une solution dédiée « App Connect Enterprise Solution for ISO 20022 Messaging »[^14].

La place de l'agent dans ce flux est délibérément étroite : **il observe et il alerte ; il n'émet pas**. La surveillance événementielle s'appuie sur la gouvernance des topics — Event Endpoint Management, seul composant d'Event Automation que la documentation d'IBM maintient et enrichit : **Event Streams et Event Processing y sont déclarés dépréciés, sans amélioration à venir**[^15]. Pour une institution qui aurait bâti dessus, c'est le fait le plus lourd de cette couche, et il se dit au même rang que les capacités. Elle s'appuie aussi sur la trajectoire Kafka/Flink du portefeuille : IBM annonce que les futures solutions Kafka et Flink « seront livrées » par IBM Confluent, filiale du groupe depuis la clôture de l'acquisition le 17 mars 2026 — le socle n'en date pas la bascule, ni le calendrier de fin de support, ni le chemin de migration (ch. 22 §22.2)[^15]. Les Streaming Agents de Confluent y apportent l'appel d'outils MCP déclaré nativement et une intégration A2A en préversion ouverte depuis le 26 février 2026 ; la source ne nomme aucun client ni chiffre d'adoption, et l'adoption en production ne peut donc pas en être inférée[^16]. **Lecture de l'auteur** : le positionnement de ce flux se scinde, comme au chapitre 22. Le rail d'émission est déterministe et ne comporte aucun agent — OO3 au sens de l'Annexe B.4. L'agent de surveillance, lui, n'est pas invoqué par le processus de paiement : branché sur le flux d'événements sans cadre de processus explicite, il relève d'OO1 ; le bus ajoute le journal, non le cadre (ch. 7 §7.5)[^11]. Le confort de l'architecture ne tient donc pas à ce que l'agent soit encadré, mais à ce qu'il soit **sans effet** sur une dorsale qu'il ne commande pas. C'est aussi la lecture que le pattern d'architecture agentique publié par IBM recommande explicitement pour les processus sous surveillance réglementaire, où il retient des workflows statiques (*static workflows*) pour l'auditabilité et les transferts définis[^17] — troisième source de la convergence exposée au chapitre 13, avec la réserve que ce chapitre y attache : ces sources ne sont pas indépendantes — deux partagent une autrice, deux une organisation — et celle-ci est l'éditeur même du portefeuille instancié ici. La convergence est un faisceau réel ; elle ne vaut pas corroboration.

> **État de la connaissance vérifiable — la messagerie du portefeuille traite-t-elle les messages ISO 20022 de Lynx ?**
>
> Question : le socle établit-il qu'un composant nommé du portefeuille traite les messages pacs.008 et pacs.009 du rail canadien ? Le lien entre la messagerie du portefeuille et ISO 20022 n'est documenté qu'**indirectement**, par Financial Transaction Manager et un Redbook de 2016 toujours référencé par l'éditeur ; il reste au niveau de preuve **[C]**[^14]. Recherche menée le 16 juillet 2026 (PRDPlan P0.2) : la passe ciblée a confirmé que Financial Transaction Manager demeure un produit actif documenté et a retrouvé le lien par citation directe du Redbook, mais **aucune source primaire non-Redbook actuelle n'a pu être extraite** — les pages ibm.com/docs refusent le fetch automatisé (403). L'élévation a échoué et l'échec est consigné comme tel[^18]. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici. En conséquence, ce flux illustre une architecture de principe. Une relecture humaine des pages produit est recommandée avant toute réutilisation ; le chapitre 24 traite l'ensemble des lacunes du blueprint.

Le RTR, enfin, appelle la double précaution du chapitre 15, qu'on ne dilue pas ici. Paiements Canada **vise** un lancement au T4 2026, à l'issue des tests industriels en cours ; la cible a été successivement reportée — 2019, puis 2022, puis 2023, puis 2026[^19]. Elle est donc bel et bien annoncée, et le rail n'est pas en production à la date de gel du présent chapitre. Un blueprint qui daterait ses jalons d'intégration sur ce rail daterait ses jalons sur une cible.

## 23.4 Flux 3 — l'accès au cadre bancaire : concevoir contre une norme qui n'existe pas encore

Le troisième flux est le plus inconfortable, et c'est là son intérêt pédagogique : il faut concevoir sans savoir contre quoi.

Le chapitre 14 a établi le fait négatif, et il est vérifié : au 16 juillet 2026, **aucun organisme de normalisation technique n'a été désigné** par arrêté ministériel et **aucun standard n'est nommé** dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie[^20]. Le règlement lui-même n'est que prépublié — Gazette du Canada, partie I, le 27 juin 2026, commentaires jusqu'au 26 août 2026 — et son texte final peut changer[^21]. Le blueprint ne peut donc pas décrire les API du cadre : il peut seulement décrire la couche qui les exposera, et documenter qu'elle ne les préjuge pas.

Ce que le blueprint peut affirmer se réduit à trois propositions, dont la dernière est négative — et il faut résister à la tentation d'en ajouter une quatrième. **Première proposition** : la couche d'exposition existe et est documentée — API Connect V12, dont la version 12.1.0 est disponible depuis le 15 décembre 2025, avec cycle de vie des API, portail développeur et famille de passerelles DataPower[^12]. **Deuxième proposition** : le socle documente que cette couche sait republier des actifs d'intégration existants en outils et serveurs MCP à partir des définitions d'API — capacité documentée dans les docs 12.1.0[^12]. C'est le troisième principe directeur (Annexe B.1), le contrat d'abord : les API du cadre, une fois qu'il y en aura, seront des actifs à republier, non à réécrire. **Troisième proposition, négative** : le consentement de la personne et le registre public des participants tenu par la Banque du Canada sont **hors du périmètre du portefeuille** — ils relèvent du cadre et de son superviseur, non de la plateforme d'intégration[^22]. Lire la couche d'exposition comme épuisant la question de l'accès au cadre bancaire, ce serait confondre le tuyau et le droit d'y faire passer quoi que ce soit : ce qui autorise le flux ne se configure pas dans une passerelle.

Un mot sur la passerelle MCP invoquée par l'Annexe B.4. Le socle ne documente pas de produit portant ce nom : ce qu'il documente, c'est ContextForge (`mcp-context-forge`), passerelle et registre unifié en logiciel libre placé devant des serveurs MCP, des agents A2A et des API REST/gRPC[^12], ainsi que la DataPower Interact Gateway, annoncée à Think 2026 et en juillet 2026 comme passerelle de gouvernance de la médiation IA, gouvernant, sécurisant et observant les interactions entre agents, modèles, outils et systèmes d'entreprise, et conçue en anticipant la communication A2A[^12]. « Passerelle MCP » est donc, dans cet ouvrage, une **fonction** de l'architecture — celle du point de contrôle des invocations d'outils — et non le nom d'un produit. **Lecture de l'auteur** : l'emploi qu'en font les Annexes B.1 et B.4 est ici tenu pour fonctionnel ; le PRD ne le précise pas — il nomme « MCP Gateway » au même rang qu'AI Gateway et DataPower Interact Gateway, c'est-à-dire comme un produit — et le point est signalé pour arbitrage. Prêter à l'éditeur un produit qu'il ne documente pas serait une faute de neutralité (§8.4).

**Lecture de l'auteur** : l'attente réglementaire n'est pas un vide où l'on peut mettre ce qu'on veut. Elle impose une discipline précise — concevoir la couche, pas le contrat ; documenter la capacité d'exposition, pas la forme des API ; et surtout, ne pas construire aujourd'hui contre une spécification d'industrie au motif qu'elle serait probable. Le socle établit que la recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » dans le règlement prépublié, le communiqué et la page du Budget 2025 donne **zéro occurrence**[^20]. Une institution qui investirait aujourd'hui dans une implémentation FDX ferait un pari d'industrie qu'aucun texte officiel ne soutient. Le chapitre 14 porte cette lacune ; le chapitre 24 en fait un événement de péremption du blueprint.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, sur sept correspondances réglementaires du blueprint, **cinq sont des inférences d'auteur**, une seule est documentée — et pour le seul rôle opérationnel d'IBM Canada sur les rails, non pour une conformité —, et la dernière est une attente réglementaire où il est interdit d'anticiper. C'est le résultat le plus important de cette partie, et il est décevant à dessein : un blueprint honnête produit peu de liens documentés. **Deuxièmement**, le fait négatif est borné : IBM ne revendique aucune conformité à E-23 ni à B-13, et le socle atteste au contraire des revendications de l'éditeur pour l'AI Act européen, l'ISO/IEC 42001 et le NIST AI RMF[^3]. Étendre le fait négatif au-delà de ses deux lignes serait une erreur de même nature que de l'ignorer. **Troisièmement**, les trois flux confirment le principe directeur du chapitre 13 sans le renforcer : dans les trois, le processus commande — encadré par un workflow déterministe dans la décision de crédit, cantonné à l'observation sur le rail de paiement, différé dans le cadre bancaire faute de norme. Le positionnement fin sur l'échelle OO1–OO4 est en revanche une lecture de l'auteur à chaque occurrence : le socle ne tranche ni entre OO3 et OO4 au flux 1, ni contre OO1 pour l'agent de surveillance du flux 2.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas qu'une institution qui déploie ces composants satisfait E-23, la ligne directrice de l'AMF, l'article 12.1, l'avis 11-348 ou la ligne directrice B-13 : cinq des sept liens n'engagent que l'auteur du blueprint. Il ne dit pas que ce portefeuille soit préférable à un autre — les alternatives non-IBM du socle sont rappelées au chapitre 7 et par renvoi au chapitre 22, et cet ouvrage ne rend aucun verdict comparatif[^9]. Il ne dit pas que le flux 2 soit implémentable tel quel : la solution ISO 20022 du portefeuille reste au niveau [C], et l'encadré du paragraphe 23.3 l'expose plutôt que de le masquer. Il ne dit rien, enfin, de la forme que prendront les API du cadre bancaire : nul ne le sait, et c'est un fait, non une omission.

La correspondance réglementaire d'un blueprint n'est pas une propriété de la plateforme. C'est un travail de démonstration, qui reste entier après que l'architecture est choisie.

---

## Notes

[^1]: PRD §8.1, garde-fou **R-7** ; §7.8, **F-44** (réserve capitale : « aucune source ne relie watsonx.governance à E-23 du BSIF ») et **F-45** (réserve : « aucun lien documenté IBM↔B-13/E-23 »). Formulation imposée par PRDPlan §4.4, cas « correspondance produit ↔ réglementation — fait négatif établi ». Statuts du tableau : PRD Annexe B.3. **Niveau de preuve** : F-44 et F-45 sont de niveau **[B]** et le fait négatif y est porté par leurs réserves, non par le balayage documenté d'un texte. Il est donc **établi**, et ne doit pas être qualifié de « vérifié » : PRDPlan §4.4 (« Trois degrés d'absence ») réserve ce terme aux trois entrées où le socle constate l'absence en balayant un texte — **F-35** (ainsi au §23.4, vérifié 9-0), **F-09** et **F-46**. Le degré tient au mode d'établissement, non au niveau de preuve : F-09 et F-46 sont de niveau [B] et portent pourtant des faits négatifs vérifiés. La recherche s'est heurtée au blocage automatisé des pages ibm.com (403) ; une relecture humaine des annonces clés est recommandée avant publication (PRD §10.6).

[^2]: PRD §7.7, **F-36** (frames normatifs et opérationnels) et **F-37** (verdict pour les scénarios réglementés) ; PRD Annexe B.1, principe 1. Voir ch. 13 (pont conceptuel) et ch. 22 (principes et couches C1–C8).

[^3]: PRD §7.8, **F-44** (niveau [B]). Sources primaires : newsroom.ibm.com (14 nov. 2023) ; ibm.com/new (extraits indexés — les pages www.ibm.com refusent le fetch automatisé, 403) ; credo.ai (28 avril 2025, accord OEM Compliance Accelerators). Statuts : watsonx.governance GA depuis déc. 2023 ; gouvernance agentique livrée en 2025 (aperçu mars, version juin) ; Instana AI Agent & LLM Observability en **préversion publique** (Think 2026). Attribution : toutes ces capacités sont attribuées à la documentation de l'éditeur (PRD §8.4).

[^4]: PRD §7.3, **F-09** (niveau **[A/B mixte]** — [A] pour les faits des passes 1-2, [B] pour les exigences opératoires extraites le 16 juill. 2026) ; formulation imposée par PRD §8.2.4 et PRDPlan §4.4. Le présent chapitre mobilise **les deux strates** : la date d'entrée en vigueur, la définition large de « modèle » et le caractère inféré de la couverture agentique relèvent de l'[A] ; l'inventaire, la cotation graduée, le cycle de vie à cinq volets et la documentation de modèle (ligne E-23 du tableau §23.1) relèvent du **[B]** — extraction directe du texte officiel, sans vote adversarial. **[B] est sous [A] dans la taxonomie du PRD §7** : cette extraction n'« élève » pas l'entrée, elle l'enrichit d'un contenu de rang inférieur. **Modalité** : E-23 est fondée sur des principes et rédigée au conditionnel (« should ») — « attendu par E-23 », jamais « exigé ». **Vocabulaire** : E-23 n'emploie ni « fiche de modèle » ni « model card » (0 occurrence, EN et FR) — parler de « documentation de modèle » (§D.2, principe 3.3) et d'« inventaire » (§C.1, champs de l'Appendice 1). Sources primaires lues et extraites le 16 juill. 2026 : osfi-bsif.gc.ca, versions EN et FR ; lettre d'accompagnement du 11 sept. 2025 (E-23, version finale du 11 septembre 2025, en vigueur le 1er mai 2027). Voir ch. 9 §9.3.

[^5]: PRDPlan §4.4, cas « correspondance produit ↔ réglementation — cas général » : la mention « l'éditeur ne revendique aucune conformité » est **interdite** hors E-23 et B-13. Socle des trois lignes concernées : PRD §7.3, **F-25** (AMF, finale depuis le 30 mars 2026, en vigueur le 1er mai 2027), **F-26** (ACVM, avis 11-348 du 5 décembre 2024) et **F-27** (Loi 25, art. 12.1).

[^6]: PRD §7.3, **F-27** (niveau [B], texte officiel consulté sur LégisQuébec) et sa **réserve d'interprétation de niveau [C]** (analyse Fasken sur le critère « exclusivement », non confrontée aux positions de la CAI). Distinction humain-dans-la-boucle / révision humaine *a posteriori* : ch. 11 §11.3 et Annexe D §D.2. Lacune : PRD §10.4.

[^7]: PRD §7.8, **F-42** (niveau [B]). Sources primaires : releases de l'ADK sur github.com/IBM/ibm-watsonx-orchestrate-adk ; ibm.com/new ; developer.watson-orchestrate.ibm.com. Capacités datées de juin 2026 : politiques de sécurité, six *guardrails* Granite Guardian, tableaux de bord (jetons, latence), traces AgentOps. Le positionnement d'IBM comme *agentic control plane* (Think 2026) est traité au ch. 22 §22.2 et n'est pas repris ici (garde-fou **R-8**, Annexe D §D.1).

[^8]: PRD §7.8, **F-45** (niveau [B]) et §7.4, **F-29** (niveau [A], votes 3-0 ×9) pour l'énumération des partenaires. Sources primaires : payments.ca (rôles de livraison et d'exploitation ; page officielle des partenaires revalidée le 16 juillet 2026) ; canada.newsroom.ibm.com (annonce du 2 mai 2019 ; Lynx lancé le 1er sept. 2021 ; RTR le 16 avril 2024). F-45 écrit « avec CGI et Interac » ; **F-29 [A] prime pour l'énumération** et liste **Deloitte Canada** comme quatrième partenaire, rôle non détaillé dans la source (voir ch. 15 §15.2). **Réserves F-45** : montants des contrats non publics ; aucun lien documenté IBM↔E-23/B-13.

[^9]: PRD §8.4, neutralité fournisseur, points (3) et (5) : aucune formulation de supériorité ; le rôle d'IBM Canada dans Lynx et le RTR est un fait de contexte, pas un argument de conformité. Alternatives non-IBM du socle (Microsoft Agent Framework, LangGraph, Temporal, Kafka/Confluent pré-acquisition) : PRD §7.6, **F-15**, **F-32**, **F-33** — voir ch. 7.

[^10]: PRD §7.5, **F-17** (niveau [A]). Source primaire : stories.td.com (21 mai 2026). **Attribution obligatoire (PRD §8.2.2)** : le passage de ~15 heures à moins de 3 minutes est une donnée auto-déclarée par TD, présentée comme résultat préliminaire, et n'a pas fait l'objet d'une vérification indépendante. Voir ch. 17 §17.1. Le socle ne documente aucun composant d'architecture du système de TD.

[^11]: PRD §7.7, **F-37** (niveau [B] pour le cadre — **préprint non révisé par les pairs**, arXiv:2606.31518v1, dont les auteurs déclarent eux-mêmes des menaces à la validité ; le cadre conceptuel est repris ici, les résultats chiffrés le sont à titre d'illustration seulement, voir ch. 5). Options OO3 et OO4 ; enseignement sur la journalisation confiée aux agents.

[^12]: PRD §7.8, **F-40** (niveau [B]). Sources primaires : ibm.com/new et ibm.com/docs (extraits indexés, 403 sur fetch automatisé) ; community.ibm.com (billets sur l'AI Gateway, lus intégralement) ; github.com/IBM (ContextForge, `mcp-context-forge`). Statuts et dates : AI Gateway annoncée en mai 2024 et étendue en janv. 2025 ; API Connect 12.1.0 disponible le 15 décembre 2025 ; DataPower Nano Gateway le 19 novembre 2025 ; DataPower Interact Gateway annoncée à Think 2026 et en juillet 2026.

[^13]: PRD §7.4, **F-28** (niveau [A], votes 3-0 ×4). Source primaire : payments.ca (deux pages officielles ; corroboration SWIFT, BNY, J.P. Morgan). Voir ch. 15 §15.1.

[^14]: PRD §7.8, **F-39** (niveau [B]). Sources : ibm.com (pages produits et cycle de vie — extraits) ; community.ibm.com (billets officiels lus intégralement). Statuts : IBM MQ 10.0 LTS GA en juin 2026 ; ACE 13.0.7 en mars 2026 ; CP4I 16.2.0 LTS GA le 30 juin 2026. La qualification « exactly-once » est celle de la documentation de l'éditeur. **Réserve F-39** : le lien MQ↔ISO 20022 n'est qu'indirect (Financial Transaction Manager, Redbooks) — **niveau [C] pour ce point précis**.

[^15]: PRD §7.8, **F-41** (niveau [B]). Sources primaires : ibm.github.io/event-automation (lu intégralement — « Event Streams and Event Processing are deprecated and no enhancements will be provided » ; les futures solutions Kafka/Flink « will be delivered by IBM Confluent » ; Event Endpoint Management continue) ; newsroom.ibm.com (annonce du 8 déc. 2025 ; clôture de l'acquisition le **17 mars 2026**, ~11 G$ de valeur d'entreprise). Le fait de dépréciation est exposé **au corps du chapitre**, au même titre que les capacités (PRD §8.4, point 4). La trajectoire est énoncée au futur par la source et n'est pas datée : la clôture du 17 mars 2026 est un fait de propriété, que la source ne présente pas comme la date de bascule de la livraison (ch. 22 §22.2, ch. 24 §24.1).

[^16]: PRD §7.6, **F-33** (niveau [B]). Sources primaires : confluent.io/blog (annonce d'août 2025 ; mise à jour du 26 février 2026). **Réserves F-33** : fonctionnalités pré-GA (Open Preview / Early Access) ; **aucun client nommé ni chiffre d'adoption** dans la source. Voir ch. 7 §7.3.

[^17]: PRD §7.8, **F-46** (niveau [B] pour l'attribution). Source primaire : ibm.com/think/architectures/patterns/agentic-ai (mis à jour le 21 février 2025, lu via navigateur). **Réserve F-46** : pattern générique — IBM ne publie pas d'architecture agentique spécifique aux services financiers (vérifié : introuvable sur ibm.com/architectures et Redbooks). Convergence à trois sources : F-36, F-37, F-46 — voir ch. 13 §13.2.

[^18]: PRD §10.6 et Annexe B.5, point 4 ; rapport `verification/revalidation-2026-07-16.md` (passe P0.2, PRDPlan §2). Formulation d'encadré imposée par PRDPlan §4.4.

[^19]: PRD §7.4, **F-29** (niveau [A], votes 3-0 ×9) ; garde-fou **R-4** (la cible T4 2026 est officiellement annoncée) et **réserve F-29** (cible conditionnelle, historique de reports — ne pas écrire « lancé » ni « en production »). Formulation imposée par PRDPlan §4.4. Source primaire : payments.ca (page RTR vérifiée le 16 juillet 2026). Voir ch. 15 §15.2 et ch. 24 §24.2.

[^20]: PRD §7.4, **F-35** (niveau [A], **fait négatif vérifié 9-0**) ; garde-fou **R-5**. Formulation imposée par PRDPlan §4.4. Sources primaires : gazette.gc.ca ; canada.ca (communiqué et Budget 2025) ; bankofcanada.ca. Voir ch. 14 §14.4 ; lacune PRD §10.1.

[^21]: PRD §7.4, **F-34** (niveau [A], votes 3-0 ×3). Sources primaires : gazette.gc.ca, partie I, vol. 160, no 26, 27 juin 2026 ; communiqué de Finances Canada du 26 juin 2026. Voir ch. 14 §14.3 ; sensibilité temporelle : PRD §8.3.

[^22]: PRD **Annexe B.4, flux 3** (« consentement et registre de la Banque du Canada **hors périmètre IBM** ») ; §7.4, **F-35** (niveau [A], fait négatif vérifié 9-0 — la Banque du Canada supervisera les entités participantes et tiendra un **registre public**) et **F-23** (cadre bancaire axé sur le consommateur). Source primaire : bankofcanada.ca. Voir ch. 14.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (22 notes ; chaque composant et chaque lien tracés F-39..F-42/F-44..F-46 ou socle
                                   général ; en-tête corrigé après relecture — F-38 (webMethods/StreamSets) et F-43
                                   (généalogie ACP→A2A) NE sont PAS mobilisés ici (ch. 3, ch. 22) et sont retirés de
                                   l'intervalle annoncé ;
                                   termes anglais entre parenthèses et en italique à la 1re occurrence ;
                                   §D.6 respecté — *guardrails* en italique pour la notion produit, « garde-fou » réservé aux R-x)
     3. Balayage garde-fous ...... fait (R-7 : formulation du fait négatif bornée à E-23 et B-13, cas général sans mention de
                                   non-revendication — F-44 atteste AI Act/ISO 42001/NIST AI RMF ; R-5 : aucun standard désigné,
                                   FDX = anticipation d'industrie ; R-4 + réserve F-29 : « vise », jamais « lancé » ; R-8 :
                                   sigle ACP absent, positionnement *agentic control plane* laissé au ch. 22 ; R-6 : non abordé
                                   ici (ch. 22) ; §8.2.2 : métrique TD attribuée ; §8.4 : alternatives par renvoi ch. 7/ch. 22,
                                   dépréciation Event Streams/EP exposée **au corps** au §23.3 — et non plus en note seule,
                                   comme l'affirmait à tort cette rubrique au premier jet —, aucun superlatif)
     4. Relecture adversariale ... FAIT (2 relecteurs indépendants ; 5 constats bloquants + 12 réserves).
                                   Réfuté et corrigé :
                                   - §23.2 étiquetait OO4 comme un fait du ch. 5 tout en décrivant un OO3 (« comme il
                                     appellerait un service » = définition d'OO3 au ch. 5 §5.1) et abandonnait la réserve
                                     du ch. 22 §22.2 → réserve reprise, positionnement marqué « Lecture de l'auteur »,
                                     titre passé à « OO3 ou OO4 » ;
                                   - §23.3 justifiait OO3 par « les agents invoqués », que le flux décrit nie (l'agent
                                     observe, il n'est pas invoqué) → scission du ch. 22 §22.2 (C3) reprise : rail = OO3,
                                     agent événementiel sans cadre explicite = OO1 (ch. 7 §7.5) ;
                                   - §23.3 confinait la dépréciation Event Streams/EP à la note [^15] alors que §8.4(4)
                                     exige l'exposition au même titre que les capacités → nommée au corps ; « livrées
                                     depuis la clôture » (fait accompli) → « seront livrées » (futur du socle, non daté) ;
                                   - §23.4 omettait le 2e élément du flux 3 de B.4 (consentement et registre de la Banque
                                     du Canada hors périmètre IBM) — orphelin de bijection → 3e proposition, négative ;
                                   - constat de gouvernance fabriqué sur l'Annexe D §D.1 (« les trois emplois ») →
                                     RETIRÉ : vérification faite, le titre porte bien « les quatre emplois » (ligne 17),
                                     l'annexe est conforme et n'a pas été touchée.
                                   Réserves appliquées : encadré §23.3 remis à la forme PRDPlan §4.4 (question + clause de
                                   clôture) ; Deloitte Canada ajouté aux partenaires RTR (F-29 [A] prime sur F-45) ; B-13
                                   ajouté à l'énumération des cinq inférences ; « vérifié » → « établi au niveau [B] »
                                   (F-44/F-45 [B] ; « vérifié » réservé aux faits négatifs [A], ainsi F-35) ; non-
                                   indépendance des trois sources de convergence signalée à l'occurrence (F-46) ;
                                   superlatif « le cas d'usage le plus documenté au Canada » supprimé (non porté au socle) ;
                                   renvois « principe B.1 » désambiguïsés (2e et 3e principes directeurs) ; « MCP Gateway »
                                   fonctionnelle marquée « Lecture de l'auteur » ; « frames (*frames*) » → « *frames* » (D.2) ;
                                   en-tête du socle mobilisé corrigé (F-38 et F-43 retirés).
     4bis. Passe de correction F-09 (16 juill. 2026, après extraction du texte intégral d'E-23) : [^4] remarquée [A] →
                                   **[A/B mixte]** avec la strate réellement mobilisée (les deux ici) et le rappel que [B] est
                                   *sous* [A] — une extraction primaire n'élève pas une entrée votée 3-0 ; §23.1 « E-23 impose »
                                   → « E-23 attend » et « ce que la ligne directrice exige » → « attend » (ligne fondée sur des
                                   principes, « should ») ; ligne E-23 du tableau B.3 : « risque de modèle » → « risque de
                                   modélisation » (titre officiel), « fiches de modèles » → « documentation de modèle » +
                                   « inventaire (champs de l'Appendice 1) » + « cotation de risque graduée » + « cycle de vie à
                                   cinq volets » (E-23 : 0 occurrence de « fiche de modèle »/« model card »). **Non touché** :
                                   « fiches de modèles (*model cards*) » au §23.1 (watsonx.governance — exact, F-44) et
                                   « fiches » aux lignes Loi 25 / §23.1 (produit, non E-23). Correction 2 (affirmation périmée
                                   sur l'absence d'extraction) sans objet : le chapitre n'en portait aucune ; l'encadré §23.3
                                   porte sur ISO 20022 (F-39, [C]), lacune non comblée — laissé intact.
     4ter. Passe corrective ..... Audit du 17 juill. 2026, périmètre m-34 et m-35. Aucune information nouvelle n'entre :
                                   date de gel INCHANGÉE au 16 juillet 2026.
                                   [m-34] note [^1] : le MOTIF de la réservation était faux — « vérifié » y était dit
                                     « terme réservé aux faits négatifs **[A]** ». Le terme n'est réservé à aucun
                                     NIVEAU DE PREUVE : PRDPlan §4.4 (v1.4), ligne « **Trois degrés d'absence —
                                     vocabulaire imposé** » (arbitrage du 17 juill. 2026, racine G-1 de l'audit), le
                                     réserve à **trois entrées** — F-35 [A], F-09 [B], F-46 [B] —, celles où le socle
                                     établit l'absence par le **balayage documenté d'un texte**. Sous la règle telle
                                     que la note l'écrivait, la « vérification négative [B] » de F-09 et le « fait
                                     négatif vérifié [B] » de l'annexe B seraient fautifs — ce qui est faux. Motif
                                     réécrit sur le mode d'établissement, avec le contre-exemple qui l'inocule.
                                     La CONCLUSION — F-44/F-45 = « **établi** », degré 2 — était JUSTE : conservée,
                                     ainsi que le corps du chapitre, qui écrit « établi » partout (§23.1, tableau).
                                     NON TOUCHÉ : le journal de relecture ci-dessus (« vérifié réservé aux faits
                                     négatifs [A] ») est le compte rendu daté d'une passe antérieure, non une règle en
                                     vigueur ; on ne réécrit pas un journal — il est supersédé par la présente entrée.
                                   [m-35] en-tête « Socle mobilisé » sous-déclaré — c'est la liste de référence de
                                     CA-1. Recensement de TOUTES les entrées réellement mobilisées, corps ET notes :
                                     ajoutés **F-15** et **F-32** (note [^9] — alternatives non-IBM), **F-17** (§23.2
                                     et note [^10] — TD), **F-23** (note [^22] — cadre bancaire), **F-33** (§23.3 et
                                     note [^16] — Streaming Agents), **F-36** (note [^2] — frames du manifeste APM).
                                     Toutes portent un fait établi par un autre chapitre et rappelé ici : classées en
                                     renvois, comme F-28/F-34/F-35 déjà présentes sous ce régime.
                                     Décompte recompté sur le fichier : **22 entrées** à l'en-tête = balayage
                                     `F-[0-9]+` du corps et des notes, à l'identique. F-38 et F-43 restent hors liste
                                     (zéro occurrence — vérifié, conformément à la ligne 2 ci-dessus).
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.

     Constats de gouvernance signalés au rapport, NON corrigés ici (CLAUDE.md — chirurgie) :
     - Annexe B.3, ligne art. 12.1 : la réponse « humain-dans-la-boucle outillé » contredit l'acquis du ch. 11 §11.3
       (HITL ≠ révision humaine de l'art. 12.1) — traité en §23.1 par une lecture de l'auteur explicite.
     - Annexe B.1 (principe 2) et B.4 (flux 3) nomment une « MCP Gateway » qui n'existe pas comme produit au socle :
       F-40 documente ContextForge et la DataPower Interact Gateway — traité en §23.4 comme lecture de l'auteur
       (fonction, pas produit), en attendant l'arbitrage du PRD.
-->
