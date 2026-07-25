# Chapitre 16 — Prospective : AP2 sur les rails canadiens ?

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-04, F-29 ; F-01, F-02, F-05, F-43 par renvoi (ch. 1) ; **lacune PRD §10.5**, assumée en encadré ; F-35 et R-5 par renvoi (ch. 14) |
| Garde-fous à surveiller (PRD §8) | **R-4** et **réserve F-29** (la cible T4 2026 est officielle ; ne jamais écrire « lancé » ni « en production ») ; **R-1** et **R-8** (l'ACP protocolaire est mentionné en §16.2 : toujours au passé, qualifié, fusion dans A2A dite ; jamais agrégé à la composante ACP d'AGNTCY) ; **§8.2.1** (soutien ≠ production, attribution à chaque occurrence) ; chapitre explicitement prospectif — toute conclusion que le socle ne porte pas est marquée « Lecture de l'auteur », et la lacune §10.5 n'est jamais comblée |
| Volumétrie cible | ~2200 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Aucune source ne documente l'articulation AP2 ↔ rails canadiens — le chapitre pose le cadre d'analyse et les conditions de possibilité, sans affirmer.

> ⚠ **Correctif de la rédaction (déclaré le 17 juill. 2026, entériné le même jour)** : la section 16.2 prévue par [TOC.md](../../TOC.md) portait « Scénarios d'articulation (mandats de paiement agentiques vs RTR/Interac) ». Le socle **ne porte ni structure de message, ni mandat, ni preuve d'intention pour AP2** (PRD §10.9e) : la section prévue ne peut être écrite sans inventer ce que le chapitre a précisément pour objet de déclarer inconnu — des *scénarios*, dans un chapitre dont la thèse est qu'aucune source ne documente l'articulation, combleraient la lacune §10.5 par de la fiction. La section est donc livrée sous « **Conditions de possibilité** » : énumérer des conditions de possibilité n'est pas prédire. **L'amendement de TOC.md a été exécuté le 17 juillet 2026 (TOC v1.5, suites de l'audit — constat m-23)** : §16.2 y porte désormais « Conditions de possibilité » et le correctif y est consigné. *Cette déviation était fondée dès le premier jet, mais elle n'avait jamais été déclarée — à la différence de celle du ch. 15 : la bijection J-2 était rompue sans que rien ne le dise. Une déviation juste doit se déclarer, sinon elle est indiscernable d'un oubli.* Aucune information nouvelle n'entre ici : la date de gel du chapitre demeure le 16 juillet 2026.

---

Ce chapitre est le seul de l'ouvrage à porter un point d'interrogation dans son titre. Ce n'est pas une coquetterie de rédaction : c'est la description exacte de son objet. Les deux chapitres qui précèdent ont établi la couche d'interopérabilité financière canadienne — le cadre des services bancaires axés sur le consommateur et son standard technique non désigné (ch. 14), la couche sémantique commune des paiements et le calendrier du système de paiement en temps réel (ch. 15). La Partie I a établi, de son côté, la pile protocolaire agentique, dont le protocole dédié à la transaction (ch. 3). La question que tout architecte d'entreprise pose à ce point de l'ouvrage s'impose d'elle-même : que se passe-t-il là où les deux se rencontrent ?

La réponse tient en une phrase, et elle est désagréable : le socle de cet ouvrage ne documente pas cette rencontre. Aucune source, primaire ou secondaire, ne l'atteste. C'est une lacune reconnue, inscrite comme telle au cahier des charges qui gouverne l'ouvrage, et le présent chapitre en est le chapitre porteur[^1].

Un chapitre prospectif, dans une monographie tracée, n'abaisse pas le seuil de preuve : il change d'objet. Il ne dit pas ce qui adviendra — il dit ce qu'il faudrait qui fût vrai pour que la question reçoive un jour une réponse, il dit ce que le socle établit de chacune de ces conditions, et il dit ce qu'il faudrait observer pour trancher. Aucune des trois opérations n'exige de deviner. Toutes les trois exigent de nommer précisément l'ignorance, ce qui est un exercice plus difficile, et plus utile, que de la meubler.

## 16.1 État de la question

Commençons par ce que le socle établit de chaque côté de la question.

**Du côté du protocole.** AP2 (*Agent Payments Protocol*) a été annoncé par Google le 16 septembre 2025 comme protocole compagnon d'A2A (*Agent2Agent*), dédié aux transactions pilotées par agents — le socle date l'annonce au jour près, le lancement au mois près seulement[^2]. En avril 2026, plus de soixante organisations des paiements et des services financiers **déclarent leur soutien** à AP2, selon le communiqué de la Linux Foundation du 9 avril 2026 ; le soutien déclaré ne vaut pas déploiement en production[^2][^3]. Le socle en nomme sept : Mastercard, PayPal, American Express, Adyen, Coinbase, Worldpay et Revolut[^2].

Cette liste appelle une observation, et une seule mise en garde. L'observation : le socle n'attribue à aucune des sept un rôle sur un rail de paiement canadien, et n'établit la nationalité d'aucune. La mise en garde, qui est la plus importante du chapitre : **le socle donne une liste illustrative, pas la liste complète des soixante et plus**[^2]. On ne peut donc pas en conclure qu'aucune organisation canadienne ne figure parmi celles qui déclarent leur soutien. L'absence est ici une absence de documentation, non une absence documentée — la distinction est méthodologique, elle traverse tout l'ouvrage, et elle sépare la présente lacune d'un fait négatif vérifié en bonne et due forme, comme celui qu'établit le chapitre 14 sur le standard technique du cadre bancaire.

**Du côté du rail.** Le système de paiement en temps réel canadien, le RTR (*Real-Time Rail*), n'est pas en production à la mi-juillet 2026 : les tests industriels sont en cours[^4]. Paiements Canada **vise** un lancement au T4 2026, à l'issue des tests industriels en cours ; la cible a été **successivement reportée** — 2019, puis 2022, puis 2023, puis 2026[^4]. Paiements Canada annonce un système nativement conforme à la couche sémantique ISO 20022 dès son lancement, et un déploiement graduel se poursuivant en 2027 — l'un et l'autre sous la même condition que la cible elle-même[^4]. Le chapitre 15 développe cette chronologie, ses partenaires de livraison et son règlement administratif ; on ne la reprend ici que dans la mesure où elle conditionne la question du présent chapitre.

Le constat central du chapitre peut désormais être posé sans détour.

> **État de la connaissance vérifiable — l'articulation d'AP2 avec les rails de paiement canadiens**
>
> **Question** : AP2 est-il employé, expérimenté, ou seulement envisagé de source documentée, sur un rail de paiement canadien — RTR ou Interac ?
>
> **Recherche menée** (passes 1-3, juillet 2026 ; revalidation du 16 juillet 2026) : les trois passes de recherche profonde qui ont constitué le socle de cet ouvrage — 77 sources récupérées, 384 affirmations extraites, 75 soumises au vote adversarial à trois juges, 69 confirmées 3-0 (méthode exposée à l'Annexe A) —, puis la revalidation temporelle du 16 juillet 2026, qui a re-consulté directement la page officielle du RTR chez Paiements Canada sans y relever de mention d'AP2, mais dont le périmètre était la revalidation des faits chauds, non la présente question[^4]. **Pourquoi elle échoue** : les deux corpus ne se rencontrent nulle part au socle. Le socle ne rapporte, des sources primaires d'AP2 — annonce Google Cloud du 16 septembre 2025, communiqué de la Linux Foundation du 9 avril 2026 —, aucun rail de paiement canadien, étant entendu qu'il n'en porte pas la liste complète des soutiens ; et il ne rapporte, des pages du RTR revalidées le 16 juillet 2026, aucune mention d'AP2[^1][^2][^4]. Aucune vérification par recherche exhaustive de chaînes de caractères n'a été menée dans les sources primaires d'AP2 ni du RTR, à la différence de celle qui a établi le fait négatif du standard technique (ch. 14) : la lacune est un défaut de documentation, non un fait négatif vérifié.
>
> En l'absence de source primaire, la question reste ouverte ; **aucune inférence n'est proposée ici**. Elle est reprise, sans duplication, au chapitre 21[^1].

## 16.2 Conditions de possibilité

Énumérer des conditions de possibilité n'est pas prédire. C'est dire ce qu'il faudrait établir, et rapporter chaque condition à ce que le socle en porte — souvent rien. Trois conditions se dégagent, dans un ordre qui n'est pas celui de l'importance mais celui de l'antériorité logique.

**Première condition : le rail doit exister.** C'est la plus élémentaire, et elle n'est pas remplie à la date de gel du présent chapitre. Le RTR est en tests industriels ; il n'est pas en production[^4]. Toute articulation d'AP2 avec le RTR est donc, au 16 juillet 2026, une articulation avec un système qui ne fonctionne pas encore. Le socle date la reprise du programme au 16 avril 2024 : du 16 avril 2024 au 16 juillet 2026, il s'est écoulé vingt-sept mois de construction, de bascules de tests internes puis d'acceptation, sans lancement[^4].

Les deux calendriers ne sont pas de même nature, et c'est un point que le lecteur pressé manquera. Le socle documente pour le RTR une chronologie jalonnée — composante de compensation et de règlement complétée au T3 2025, tests internes au T4 2025, tests d'acceptation au T1 2026, tests industriels à la mi-2026 — assortie de la réserve qu'il s'agit de communications d'opérateur[^4]. Pour AP2, il ne documente que deux points : une annonce le 16 septembre 2025 et un décompte de soutiens déclarés que la Linux Foundation publie le 9 avril 2026, soit six mois et vingt-quatre jours après l'annonce[^2][^3]. Aucun jalon de version, aucune étape de maturité, aucun déploiement. Du 16 septembre 2025 au 1er octobre 2026 — premier jour du trimestre visé pour le lancement du RTR — s'écouleraient douze mois et demi.

**Lecture de l'auteur** : l'asymétrie de documentation entre les deux objets est elle-même le fait le plus solide de ce chapitre. Le socle établit qu'un opérateur de rail publie une chronologie jalonnée et révisable, et que, pour un protocole de transaction agentique, on ne dispose que d'une date d'annonce et d'un décompte de soutiens déclarés que publie la Linux Foundation (communiqué du 9 avril 2026)[^2][^3]. Il n'établit pas que le second soit immature — seulement que sa maturité n'est pas documentée par les sources dont dispose cet ouvrage. Un architecte qui inverserait la charge de la preuve, et lirait l'absence de jalons comme une preuve d'inexistence, commettrait la faute symétrique de celui qui lit un décompte de soutiens comme un décompte de mises en production.

**Deuxième condition : les couches sémantiques doivent se rejoindre.** Le RTR est annoncé nativement conforme à ISO 20022 dès son lancement[^4]. Ce que la **richesse** de ces données changerait pour des agents, en revanche, ne relève d'aucun chapitre de cet ouvrage : le chapitre 15 a établi que F-28 et F-29 n'en documentent **aucun attribut** — ni structure des données de remise, ni granularité des identifiants —, et c'est la raison pour laquelle il ne l'écrit pas. La question qui appartient au présent chapitre est plus étroite : le socle établit-il une correspondance entre AP2 et ISO 20022 ? Il n'en établit aucune. Le socle ne porte pas l'anatomie technique d'AP2 : il en donne la fonction déclarée — protocole compagnon d'A2A pour les transactions pilotées par agents — et rien de plus[^2]. Le chapitre 3 traite AP2 dans les limites de ce que cette entrée documente ; le présent chapitre ne peut aller au-delà. Toute phrase décrivant comment un mandat de paiement agentique se traduirait en message ISO 20022 serait une invention, et cet ouvrage n'en produira pas.

**Troisième condition : la gouvernance doit être documentable des deux côtés.** Côté rail, le socle nomme les partenaires de livraison et d'exploitation du RTR et date l'entrée en vigueur de son règlement administratif (ch. 15)[^4]. Il n'établit rien des règles d'accès qui s'appliqueraient à un tiers, agentique ou non. Le cas d'Interac mérite d'être signalé pour ce qu'il n'est pas : le socle ne documente Interac qu'en qualité de partenaire du RTR, ayant livré la composante d'échange en juin 2023[^4]. Il n'établit rien des rails propres d'Interac. La question du titre du présent chapitre, pour ce versant-là, ne peut donc même pas être instruite.

Côté protocole, le socle porte un fait discret et lourd de conséquences : **AP2 est le protocole que la conclusion du chapitre 1 a dû explicitement exclure de son constat de consolidation**, parce que le socle ne documente à ce jour aucun transfert de sa gouvernance à une fondation neutre[^2]. MCP, A2A et AGNTCY ont quitté l'intendance exclusive de leur créateur ; l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI) l'avait quittée lui aussi, puis a fusionné dans A2A le 29 août 2025, son développement actif ayant cessé (ch. 1 §1.2). AP2, dans l'état du socle, n'a connu ni l'un ni l'autre[^5].

**Lecture de l'auteur** : pour une institution financière canadienne réglementée, cette différence renverse l'exercice de diligence raisonnable que décrivait le chapitre 1. Devant A2A, l'institution constate des règles — une licence permissive, un comité de pilotage multipartite dont le socle documente la composition[^5]. Devant AP2, dans l'état de la documentation au 16 juillet 2026, elle en est réduite à apprécier la stratégie et les intentions d'une entreprise, c'est-à-dire à un exercice de prospective. Le socle établit l'absence de transfert documenté ; il n'établit rien des intentions de Google, ni de ce que valent les soixante et plus soutiens déclarés que rapporte la Linux Foundation dans son communiqué du 9 avril 2026[^2][^3]. Il faudrait donc que les deux gouvernances — celle du rail et celle du protocole — deviennent documentables pour qu'un dossier d'architecture puisse seulement être ouvert.

Une quatrième famille de conditions existe, et le présent chapitre ne la traite pas : les conditions réglementaires. Un paiement initié par un agent dans une institution financière canadienne rencontrerait le régime de la Partie III, et le croisement systématique de la pile protocolaire avec les exigences canadiennes appartient au chapitre 18. Le signaler ici est nécessaire ; l'instruire ici serait empiéter.

## 16.3 Questions de recherche

De ce qui précède se déduit un programme, et c'est le véritable livrable du chapitre. Cinq questions, chacune falsifiable, chacune assortie de ce qui la trancherait.

**Q1.** Parmi les plus de soixante organisations dont la Linux Foundation rapporte, dans son communiqué du 9 avril 2026, qu'elles déclarent leur soutien à AP2, s'en trouve-t-il une qui opère un rail de paiement canadien ou y participe[^2][^3] ? *Trancherait* : la liste complète des organisations dont la Linux Foundation rapporte le soutien déclaré, dont le socle ne nomme que sept.

**Q2.** La gouvernance d'AP2 fait-elle l'objet d'un transfert à une fondation neutre ? *Trancherait* : un communiqué de la Linux Foundation ou de Google Cloud. Un tel transfert lèverait la restriction que la conclusion du chapitre 1 a dû poser[^2].

**Q3.** Une correspondance entre AP2 et ISO 20022 est-elle documentée par une source primaire ? *Trancherait* : la spécification d'AP2 elle-même, que le socle ne porte pas.

**Q4.** Le règlement administratif du RTR, en vigueur le 24 août 2026, traite-t-il de l'initiation d'un paiement par un tiers ou par un agent[^4] ? *Trancherait* : le texte publié à la Gazette du Canada — dont le socle atteste l'existence et les dates, non le contenu (ch. 15).

**Q5.** Le lancement du RTR visé au T4 2026 a-t-il lieu[^4] ? *Trancherait* : Paiements Canada. C'est l'événement qui lèverait ou maintiendrait la réserve du socle sur la production, et il figure aux conditions de péremption de l'ouvrage (ch. 24).

Ces cinq questions sont distinctes de celle de la désignation de l'organisme de normalisation technique du cadre bancaire, qui est une autre lacune ouverte, traitée au chapitre 14. Les confondre serait fusionner deux ignorances que le socle tient séparées.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, AP2 existe, son annonce est datée du 16 septembre 2025, et la seule métrique d'adoption dont le socle dispose est un décompte de soutiens déclarés rapporté par la Linux Foundation le 9 avril 2026 — soutien qui ne vaut pas déploiement en production[^2][^3]. **Deuxièmement**, le RTR n'est pas en production à la date de gel, sa cible officielle de lancement est le T4 2026, et Paiements Canada l'annonce nativement ISO 20022 dès ce lancement[^4]. **Troisièmement**, et c'est le résultat propre du chapitre : aucune source du socle ne relie les deux. Ce n'est pas un aveu d'échec — c'est un résultat, et il est daté.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas qu'AP2 ne sera pas employé sur les rails canadiens ; il ne dit pas davantage qu'il le sera. Il ne dit pas que l'absence de documentation soit une absence d'activité : l'ouvrage sait produire des faits négatifs vérifiés — le standard technique du cadre bancaire en est un (ch. 14) — et la présente lacune n'en est pas un. Il ne décrit pas l'anatomie technique d'AP2, que le socle ne porte pas. Il ne traite pas des conditions réglementaires d'un paiement agentique, qui relèvent de la Partie III et du chapitre 18.

Un chapitre prospectif honnête est un chapitre qui a inventorié ce qu'il faudrait savoir. Ce n'est pas un chapitre qui a deviné.

---

## Notes

[^1]: PRD §10.5 (lacune documentée) : « aucune source ne documente encore l'usage d'AP2 sur les rails de paiement canadiens (RTR, Interac) ». Le présent chapitre est le chapitre porteur de cette lacune ; elle est reprise au ch. 21 par simple renvoi, sans duplication. Format de l'encadré : PRDPlan §4.4 (« encadré de lacune »). Interdiction de combler par du non-vérifié : PRD §10, exigence de clôture.

[^2]: PRD §7.1, **F-04** (niveau [A]). Sources primaires : annonce Google Cloud du 16 septembre 2025 ; communiqué de la Linux Foundation du 9 avril 2026. **Réserve F-04** : endossement déclaré, pas adoption en production vérifiée. La liste de sept organisations que porte l'entrée (Mastercard, PayPal, American Express, Adyen, Coinbase, Worldpay, Revolut) est **illustrative** et non exhaustive des « 60+ » annoncées. Le socle ne documente **aucun transfert de gouvernance d'AP2** à une fondation — d'où la restriction posée en conclusion du ch. 1, et reprise ici. Le socle ne porte pas l'anatomie technique d'AP2 (format de message, mandats) : le ch. 3 le traite dans les limites de cette entrée.

[^3]: PRD §8.2.1 (règle d'attribution des métriques d'adoption des protocoles : auto-déclarées, attribuées au communiqué à **chaque** occurrence) ; formulation imposée par PRDPlan §4.4 (« soutien ≠ production »).

[^4]: PRD §7.4, **F-29** (niveau [A], page RTR de payments.ca revalidée le 16 juillet 2026 — voir `verification/revalidation-2026-07-16.md`). Sources primaires : payments.ca (quatre pages officielles). Chronologie citée : reprise du programme le 16 avril 2024 avec IBM Canada et CGI aux côtés d'Interac (composante d'échange livrée en juin 2023), Deloitte Canada listé comme quatrième partenaire sans détail de rôle ; composante compensation/règlement complétée au T3 2025 ; tests internes complétés au T4 2025 ; tests d'acceptation complétés au T1 2026 ; tests industriels en cours à la mi-2026 ; règlement administratif no 10 (Gazette du Canada, partie II, 1er juillet 2026) en vigueur le 24 août 2026. **Garde-fou R-4** : la cible T4 2026 est officiellement annoncée — ne jamais écrire « aucune date annoncée ». **Réserve F-29** : la cible est conditionnelle au succès des tests et a été successivement reportée (2019, 2022, 2023, 2026) ; ne jamais écrire « lancé » ni « en production » ; les jalons sont des communications d'opérateur. Développement complet : ch. 15.

[^5]: Constat de consolidation, par renvoi au ch. 1 (§1.1-§1.2) — PRD §7.1, **F-01** (MCP : gouvernance transférée à l'Agentic AI Foundation/Linux Foundation en décembre 2025) ; **F-02** (A2A : transféré à la Linux Foundation en juin 2025, licence Apache 2.0 ; comité de pilotage technique à huit membres — AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, ServiceNow) ; **F-05** (AGNTCY : sous Linux Foundation depuis le 29 juillet 2025) ; §7.8, **F-43** (l'ACP protocolaire d'IBM Research/BeeAI, donné à la Linux Foundation en mars 2025, a **fusionné dans A2A le 29 août 2025** — arrêt du développement actif, apport des actifs à A2A). **Garde-fou R-1** : l'ACP protocolaire n'est jamais présenté comme standard vivant ; **R-8** : le sigle porte ici son qualificatif complet et n'est pas agrégé à la composante ACP d'AGNTCY, dont le socle n'établit pas l'identité avec lui (lacune PRD §10.7). Formes imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.1. **Réserve F-02** : le socle documente la **composition** du comité de pilotage, non ses règles de vote ou de décision.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps ≈ 2200 mots, cible ~2200 ±10 %)
     2. Traçabilité (CA-1, CA-5) . fait (5 notes ; AP2 / A2A / RTR / ACP protocolaire en anglais italique à la 1re occurrence)
     3. Balayage garde-fous ...... fait (R-4 + réserve F-29 : formulation §4.4 verbatim, aucun « lancé »/« en production » ;
                                   §8.2.1 : « 60+ » attribué à la LF/9 avril 2026 aux SEPT occurrences du décompte
                                   (le décompte « quatre » du premier jet était faux — relevé en relecture) ;
                                   R-5/F-35 : renvoi ch. 14 sans reprise du fond ;
                                   R-1 + R-8 : une seule mention de l'ACP protocolaire (§16.2), au passé, qualifiée,
                                   fusion dans A2A du 29 août 2025 dite, renvoi ch. 1 §1.2 sans duplication de l'encadré,
                                   jamais agrégée à la composante ACP d'AGNTCY (§10.7) ;
                                   R-7 : « E-23 » non employé — renvoi Partie III/ch. 18 sans assertion)
     4. Relecture adversariale ... fait (deux relecteurs distincts ; 6 réfutations bloquantes + 10 réserves, toutes corrigées :
                                   R-1/CA-2 — l'ACP protocolaire était rangé au présent parfait, en 4e pair de MCP/A2A/AGNTCY,
                                   sans mention de la fusion ni de l'arrêt du développement : réécrit au passé, R-1/R-8
                                   ajoutés à l'en-tête (ils n'y figuraient pas et n'avaient pas été balayés) ;
                                   CA-1 — le constat de consolidation et le TSC d'A2A ne traçaient vers rien
                                   (note [^5] créée : F-01, F-02, F-05, F-43 ; en-tête « Socle mobilisé » complété) ;
                                   dérive lexicale « signataires »/« membres » -> « déclarent leur soutien » (F-04, §8.2.1) ;
                                   faits négatifs fabriqués par source (« les sources primaires ne nomment aucun rail
                                   canadien ») -> énoncé de ce que le socle rapporte (§10.5), contradiction interne levée ;
                                   décompte de soutiens ré-attribué à la LF aux occurrences où l'émetteur avait disparu,
                                   dont la « Lecture de l'auteur » qui porte la thèse du chapitre ;
                                   Annexe A — « 384 affirmations, vote à 3 juges » laissait croire que les 384 étaient
                                   votées : 75 votées / 69 confirmées ; périmètre de la revalidation du 16 juill. 2026
                                   explicité (faits chauds, AP2 jamais instruit) ;
                                   « lancé le 16 sept. 2025 » -> « annoncé » (le socle date l'annonce au jour, le lancement
                                   au mois) ; chiffres dérivés libellés « après l'annonce » ;
                                   ISO 20022 au futur catégorique -> attribué à Paiements Canada (réserve F-29), 3 occurrences ;
                                   « Interac, IBM Canada et CGI depuis le 16 avril 2024 » — date faussée pour Interac
                                   (déjà en place, composante d'échange en juin 2023) : passage réduit au renvoi ch. 15,
                                   qui supprime aussi le doublon de périmètre (bijection TOC) ;
                                   « L'observation » -> énoncé de socle (F-04 n'établit ni nationalité ni rôle) ;
                                   « Recherche menée » daté (passes 1-3 + revalidation) — voir gouvernance : PRDPlan §4.4
                                   impose une date unique, inadaptée à une lacune couverte par plusieurs passes)
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.

     6. PASSE CORRECTIVE DE CONFORMITÉ — 17 juillet 2026 (suites de l'audit `audit.md`, constat m-23).
        AUCUNE information nouvelle : la date de gel reste le 16 juillet 2026, aucun fait n'est ajouté, retiré ni redaté.
          - [m-23, §16.2] DÉVIATION FONDÉE MAIS SILENCIEUSE, désormais déclarée. Le chapitre a livré « Conditions de
            possibilité » là où le TOC prévoyait « Scénarios d'articulation ». La déviation était **juste** — le socle ne
            porte ni structure de message, ni mandat, ni preuve d'intention pour AP2 (§10.9e), et des scénarios auraient
            comblé la lacune §10.5 par de la fiction, ce que le chapitre entier s'interdit. Mais elle n'était **déclarée
            nulle part** : ni bandeau de correctif, ni remontée en gouvernance, à la différence du ch. 15, qui déclarait
            les siennes et réclamait son amendement. Une déviation non déclarée est indiscernable d'un oubli, et c'est le
            lecteur qui paie la différence. Bandeau de correctif ajouté sur le modèle du ch. 15 ; TOC v1.5 aligné sur le
            chapitre le 17 juillet 2026 (§16.2 porte désormais « Conditions de possibilité »).
          - Le corps du §16.2 n'est pas touché : il était conforme, et son ouverture (« Énumérer des conditions de
            possibilité n'est pas prédire ») portait déjà la justification que le bandeau rend maintenant visible.
          - Décomptes re-vérifiés après la passe : 5 notes ([^1] à [^5]), toutes appelées et définies ; aucun décompte du
            corps n'est touché (les trois conditions de §16.2 et les cinq questions de §16.3 sont intactes ; arithmétique
            ci-dessous inchangée).

     Arithmétique posée dans le texte, à re-vérifier en relecture :
       - 16 avril 2024 -> 16 juillet 2026 = 27 mois (24 + 3)
       - 16 sept. 2025 -> 9 avril 2026 = 6 mois et 24 jours (16 sept. + 6 mois = 16 mars ; 16 mars -> 9 avril = 24 j)
       - 16 sept. 2025 -> 1er oct. 2026 = 12 mois et 15 jours ("douze mois et demi")

     Points de revalidation (P4.1) : lancement effectif du RTR (lève ou maintient la réserve F-29) ;
     règlement administratif no 10 en vigueur le 24 août 2026 ; tout transfert de gouvernance d'AP2 (F-04). -->
