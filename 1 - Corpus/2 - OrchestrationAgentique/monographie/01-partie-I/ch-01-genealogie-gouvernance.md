# Chapitre 1 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-01, F-02, F-04 (renvoi), F-05, F-43 ; F-06 (jalon historiographique) |
| Garde-fous à surveiller (PRD §8) | §8.2.1 (métriques d'adoption auto-déclarées) ; **R-1 et R-8** — ce chapitre porte la **première occurrence du sigle ACP dans l'ouvrage** (§1.2), y compris une quatrième branche non couverte par R-8 (composante ACP d'AGNTCY) |
| Volumétrie cible | ~2800 mots |

> **Thèse ([TOC.md](../../TOC.md))** : En dix-sept mois, la couche protocolaire agentique s'est consolidée sous gouvernance neutre (Linux Foundation), condition de sa crédibilité en entreprise réglementée.

---

Une institution financière ne bâtit pas son architecture sur le produit d'un seul éditeur sans se demander ce qu'il adviendra si celui-ci change d'avis. La question n'a rien de théorique : elle est au cœur du risque de tiers, elle figure dans les questionnaires de diligence raisonnable, et elle décide souvent, seule, de la mise en production. C'est pourquoi l'histoire racontée dans ce chapitre — celle du passage des protocoles d'interopérabilité agentique du statut de projet propriétaire à celui de standard ouvert sous gouvernance neutre — n'est pas une chronique d'initiés. Elle est la condition préalable à tout le reste de cet ouvrage. Sans elle, les Parties II à VII décriraient une pile technique que nul architecte prudent ne recommanderait.

Ce chapitre soutient que cette consolidation s'est produite, qu'elle s'est produite vite — dix-sept mois séparent la publication du premier protocole du bilan public de la première année du second —, et qu'elle a suivi un schéma remarquablement constant. Il soutient aussi, en fin de parcours, que la gouvernance neutre est une condition *nécessaire* de la crédibilité en entreprise réglementée, non une condition *suffisante* : les métriques par lesquelles ces protocoles annoncent leur succès ne mesurent pas ce que leur formulation laisse entendre.

## 1.1 Chronologie 2024-2026 : dix-sept mois de consolidation

Le point de départ est **novembre 2024**. Anthropic publie le *Model Context Protocol* (MCP), une interface client-serveur fondée sur JSON-RPC 2.0 destinée à l'invocation d'outils et à l'échange de données typées entre un modèle et son environnement, assortie d'un cadre d'autorisation (*authorization framework*) fondé sur OAuth[^1]. Le protocole naît propriétaire au sens strict : un éditeur, une spécification, un intendant.

L'essaimage est rapide. En **mars 2025**, deux initiatives apparaissent presque simultanément. Cisco ouvre **AGNTCY**, avec LangChain et Galileo, comme couche d'infrastructure — annuaires de découverte (*discovery directories*) et transport SLIM — explicitement pensée comme complémentaire des protocoles d'échange plutôt que rivale[^2]. Le **17 mars 2025**, IBM Research lance la plateforme BeeAI et, avec elle, un protocole de communication entre agents alors baptisé ACP (*Agent Communication Protocol*), en version pré-alpha et d'abord conçu comme une extension de MCP ; il est confié à la Linux Foundation dès le mois de mars[^3].

En **avril 2025**, Google lance **A2A** (*Agent2Agent*), qui traite un problème distinct de celui de MCP : non plus l'accès d'un agent à ses outils, mais la délégation de tâches de pair à pair entre agents, au moyen de descripteurs appelés cartes d'agents (*Agent Cards*)[^4]. En **septembre 2025** s'y ajoute **AP2** (*Agent Payments Protocol*), protocole compagnon d'A2A dédié aux transactions pilotées par agents, dont le chapitre 3 traite[^5].

Vient alors la séquence décisive, celle qui donne son titre au chapitre. **Juin 2025** : Google transfère A2A à la Linux Foundation sous licence Apache 2.0[^4]. **29 juillet 2025** : Cisco place AGNTCY sous Linux Foundation[^2]. **29 août 2025** : le protocole ACP d'IBM Research fusionne officiellement dans A2A — le développement actif d'ACP cesse, ses actifs sont versés à A2A, BeeAI l'adopte par adaptateurs, et des guides de migration sont fournis[^3]. **Décembre 2025**, enfin : la gouvernance de MCP est transférée à l'Agentic AI Foundation, elle-même sous Linux Foundation ; Anthropic demeure le créateur du protocole, mais cesse d'en être l'unique intendant[^1].

De novembre 2024 à avril 2026 — date à laquelle la Linux Foundation dresse publiquement le bilan de la première année d'A2A[^4] —, il s'écoule dix-sept mois. En dix-sept mois, quatre protocoles nés dans quatre entreprises différentes ont convergé vers deux fondations, dont l'une héberge l'autre. Le chapitre 2 examine l'état technique des deux principaux à la date de gel du présent ouvrage ; on notera seulement ici que la spécification MCP en vigueur au 16 juillet 2026 porte la révision 2025-11-25, et qu'une révision majeure était attendue douze jours après cette date de gel[^1] — un rappel, s'il en fallait, que la stabilité d'une gouvernance ne signifie pas l'immobilité d'une spécification.

Un mot, enfin, sur ce que cette chronologie a rendu caduc. Le survey académique de référence de la période (Ehtesham et al., mai 2025) proposait une trajectoire d'adoption séquentielle MCP → ACP protocolaire → A2A → ANP[^6]. La fusion du protocole ACP d'IBM Research dans A2A, en août 2025, a vidé la deuxième étape de sa substance moins de quatre mois après la publication. Ce document conserve toute sa valeur de jalon historiographique — il documente ce qu'un observateur informé pouvait raisonnablement croire au printemps 2025 — mais il ne peut plus servir de guidance d'architecture. La vitesse à laquelle il s'est périmé est elle-même une donnée sur le domaine, et un avertissement pour le présent ouvrage.

## 1.2 Gouvernance comparée : ce que « neutre » veut dire

La destination commune — la Linux Foundation — masque trois arrangements distincts, et la nuance importe pour qui doit documenter une dépendance technologique dans un dossier de conformité.

**A2A et AGNTCY relèvent directement de la Linux Foundation**, respectivement depuis juin et juillet 2025[^2][^4]. **MCP relève de l'Agentic AI Foundation**, structure formée en décembre 2025 et hébergée par la Linux Foundation[^1]. La différence est de degré, non de nature : dans les trois cas, la propriété intellectuelle et le processus de décision quittent l'entreprise fondatrice. Pour l'architecte, la conséquence pratique est identique — la disparition ou le revirement stratégique du créateur ne fait plus disparaître le protocole.

Encore faut-il préciser ce que « quitter l'entreprise fondatrice » recouvre, car c'est ici que se joue la valeur du transfert pour une institution réglementée. Le socle documente un élément décisif : A2A a été versé à la Linux Foundation **sous licence Apache 2.0**[^4]. Cette précision, d'apparence technique, porte une garantie juridique concrète : une licence permissive, irrévocable, assortie d'une concession expresse de brevets. L'institution qui construit sur A2A n'obtient pas seulement la probabilité que le protocole survive à son créateur ; elle obtient le droit opposable de continuer à l'utiliser, de le modifier, et — dans l'hypothèse la plus défavorable — d'en poursuivre elle-même le développement si la fondation venait à l'abandonner. C'est exactement le type de garantie qu'un dossier de risque de tiers cherche à établir, et que nulle assurance contractuelle d'un éditeur ne procure au même degré.

**Lecture de l'auteur** : le passage sous fondation neutre transforme la nature de la question posée en diligence raisonnable. Devant un protocole propriétaire, l'institution doit évaluer la solidité financière, la stratégie et les intentions d'une entreprise — un exercice de prospective. Devant un protocole sous licence permissive et gouvernance multipartite, elle évalue la vitalité d'un projet et la robustesse de ses règles — un exercice de constat. Le socle n'établit pas cette proposition ; il en fournit les éléments (transfert d'intendance, licence, composition du comité). Le glissement d'un exercice à l'autre est la raison pour laquelle ce chapitre ouvre l'ouvrage plutôt que de le clore.

Le cas d'A2A mérite l'examen le plus attentif, parce que son comité de pilotage technique (*technical steering committee*) est le lieu où se décide concrètement l'évolution du protocole. Le socle documente la composition de ce comité : huit organisations — AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow[^4]. Il faut mesurer ce que cette liste a d'inhabituel : les trois grands fournisseurs d'infonuagique publique y figurent ensemble, alors qu'ils sont concurrents frontaux sur à peu près tout le reste, et Google, créateur du protocole, y figure au même titre que les sept autres.

**Lecture de l'auteur** — et il faut la marquer comme telle, car le socle documente une composition, non un règlement intérieur : une instance où siègent huit organisations concurrentes, dont aucune n'est le créateur en position dominante, offre à un tiers évaluateur une garantie qualitativement différente de celle d'un comité consultatif convoqué par un éditeur. Le socle de cet ouvrage n'établit ni la répartition des droits de vote, ni les règles de décision de ce comité ; l'inférence porte sur la structure, pas sur la procédure. Elle mérite d'être vérifiée par toute institution qui en ferait un argument de dossier.

La présence d'**IBM Research** à ce comité mérite qu'on en retrace l'origine, car elle illustre le mécanisme de la consolidation mieux qu'aucune déclaration d'intention. IBM Research n'est pas arrivée au comité de pilotage d'A2A par adhésion : elle y est arrivée par **fusion**. En mai 2025, un billet d'IBM Research présentait encore le protocole ACP maison comme complémentaire de MCP et affichait l'ambition, dans les mots de Kate Blair, d'en faire « the HTTP of agent communication »[^3]. Trois mois plus tard, en août 2025, IBM versait ces actifs à A2A, arrêtait le développement d'ACP, et Kate Blair rejoignait le comité de pilotage technique d'A2A[^3]. Un concurrent déclaré est devenu un codécideur. C'est la trajectoire inverse de la fragmentation que le domaine redoutait, et elle s'est jouée en un trimestre.

De cet épisode découle une règle de rédaction qui vaut pour tout l'ouvrage : **le protocole ACP d'IBM Research ne doit jamais être présenté comme un standard vivant**[^7]. Son développement actif a cessé ; il ne subsiste qu'à travers A2A et les adaptateurs de BeeAI.

> **État de la connaissance vérifiable — le sigle « ACP » désigne au moins quatre objets distincts**
>
> Le présent chapitre porte la première occurrence du sigle « ACP » dans l'ouvrage, et doit donc en poser la désambiguïsation. Le socle atteste trois emplois distincts — et il faut être précis sur ce que « distincts » recouvre, car il ne dit pas la même chose des trois couples : (a) le **protocole ACP d'IBM Research/BeeAI**, fusionné dans A2A en août 2025 et traité ici ; (b) l'***Agentic Control Plane*** du consortium Lightworks–Scotiabank–Sun Life–TELUS, programme annoncé en juillet 2026 (ch. 17) ; (c) l'expression ***agentic control plane*** employée par IBM pour positionner watsonx Orchestrate depuis mai 2026 (ch. 22)[^7]. **Le socle établit l'absence de lien pour un seul de ces couples** : F-48 pose que l'*Agentic Control Plane* du consortium « n'a aucun lien » avec le protocole ACP d'IBM Research — pure homonymie[^7]. Sur (a) et (c), il ne dit rien de tel, et le silence mérite d'être relevé plutôt que comblé : ce sont **deux objets d'IBM**, et rien au socle n'établit qu'ils soient étrangers l'un à l'autre — ni qu'ils soient liés. Absence de documentation dans le corpus de cet ouvrage, non fait négatif vérifié.
>
> À ces trois s'ajoute un **quatrième objet**, relevé lors de la rédaction du présent chapitre : le socle mentionne une « composante ACP » propre à **AGNTCY**, dont des analyses tierces relèvent un chevauchement avec A2A[^2]. **Le socle n'établit ni son intitulé complet, ni son identité — ou sa non-identité — avec le protocole ACP d'IBM Research.** En l'absence de source primaire sur ce point, cet ouvrage ne tranche pas : il désigne cet objet par « la composante ACP d'AGNTCY », toujours qualifié, et s'interdit de l'agréger aux trois autres. La question reste ouverte et figure au chapitre 21.
>
> **Règle** : le sigle « ACP » employé seul est proscrit dans tout l'ouvrage ; chaque emploi porte son qualificatif complet (Annexe D §D.1).

AGNTCY, enfin, présente une gouvernance de facture classique : membres formateurs Cisco, Dell Technologies, Google Cloud, Oracle et Red Hat[^2]. Son positionnement officiel est celui d'une couche d'infrastructure interopérable avec A2A et MCP, non concurrente — positionnement que le chevauchement relevé ci-dessus vient nuancer, mais qui demeure la position déclarée du projet.

Ce qui frappe, à comparer les trajectoires, c'est leur régularité. Quatre mois pour AGNTCY, de l'ouverture à la fondation ; deux mois pour A2A ; treize mois pour MCP, le plus lent des trois. Aucun des protocoles étudiés ici n'est demeuré propriétaire au-delà de treize mois. On peut y lire — et c'est encore une lecture de l'auteur, non un fait du socle — une conviction partagée du secteur : dans un domaine où la valeur naît de l'interconnexion, la propriété exclusive d'un protocole détruit plus de valeur qu'elle n'en capte.

## 1.3 Lecture critique des métriques d'adoption : « soutien » n'est pas « production »

Il reste à examiner les chiffres par lesquels ces protocoles annoncent leur réussite, et à le faire avec une sévérité que la littérature promotionnelle ne s'impose pas.

Les données disponibles sont les suivantes. En avril 2026, **la Linux Foundation annonce que plus de 150 organisations déclarent leur soutien à A2A**, contre plus de 50 au lancement[^4]. De son côté, **le communiqué de la Linux Foundation du 29 juillet 2025 fait état de plus de 65 entreprises déclarant leur soutien à AGNTCY** — le soutien déclaré ne vaut pas plus déploiement en production ici qu'ailleurs, et le socle n'enregistre aucune actualisation ultérieure de ce décompte[^2] : il serait donc fautif de le rapprocher des chiffres d'avril 2026, que plus de huit mois en séparent (ch. 3 §3.2). Ces chiffres sont réels, datés, et adossés à des communiqués officiels. Ils sont aussi, et c'est là tout le problème, **auto-déclarés par la Linux Foundation et par les entreprises fondatrices** — leur attribution à leur source est obligatoire à chaque occurrence dans cet ouvrage[^8].

Trois réserves s'imposent, par ordre de gravité croissante.

La première est que **la notion même d'« organisation de soutien » n'est définie nulle part**[^4]. Elle ne distingue pas l'entreprise qui a inscrit son logo sur une page d'annonce de celle qui a affecté une équipe d'ingénierie au protocole pendant un an. Une métrique dont l'unité n'est pas définie ne mesure rien de vérifiable ; elle indique une direction, pas une grandeur. Un responsable de la conformité qui recevrait un tel chiffre à l'appui d'une décision d'architecture serait fondé à demander ce qu'on y a compté — et ne trouverait pas la réponse dans la source.

La deuxième est que **le soutien déclaré ne vaut pas déploiement en production**[^8]. C'est la réserve centrale, et elle traverse tout l'ouvrage. Un architecte qui lirait le chiffre annoncé par la Linux Foundation en avril 2026 comme « 150 systèmes agentiques interopérables en exploitation » commettrait une erreur de catégorie. Le passage effectif en production des institutions financières canadiennes fait l'objet de la Partie V, où l'on verra que le nombre d'institutions documentant par sources primaires un déploiement agentique se compte, au Canada, sur les doigts de deux mains. L'écart entre les deux ordres de grandeur — la centaine d'organisations qui déclarent leur soutien à un protocole mondial, la poignée d'institutions canadiennes qui documentent une mise en production — est l'un des enseignements les plus robustes de cet ouvrage.

La troisième réserve porte sur la croissance elle-même. Le passage de plus de 50 à plus de 150 organisations en douze mois, tel que la Linux Foundation le rapporte en avril 2026[^4], est un triplement apparent. Mais un triplement d'une grandeur non définie reste non défini. La progression établit qu'un nombre croissant d'organisations jugent utile d'associer publiquement leur nom à A2A ; c'est une information sur la dynamique du domaine, non sur sa maturité technique.

Faut-il, pour autant, écarter ces chiffres ? Non — et il serait malhonnête de le faire. Ils constituent le meilleur indicateur public disponible de l'attention que le secteur porte à ces protocoles, et cette attention est elle-même un fait pertinent pour une institution qui évalue le risque de pérennité d'un standard. Un protocole auquel la Linux Foundation recense plus de 150 organisations déclarant leur soutien a peu de chances d'être abandonné dans les dix-huit mois. C'est exactement ce que ces chiffres établissent, et rien de plus.

Le lecteur exigeant en retiendra la portée exacte. La composition du comité de pilotage technique d'A2A — huit organisations concurrentes[^4] — est un indicateur de gouvernance nettement plus solide que le décompte des soutiens, parce que ses membres sont nommés, que leur engagement est vérifiable dans les dépôts publics du projet, et que leur nombre restreint interdit la comptabilité complaisante. Quand cet ouvrage devra juger de la pérennité d'un protocole, il regardera qui décide, non combien applaudissent.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis, pour les chapitres suivants. **Premièrement**, la couche protocolaire agentique est sortie du régime propriétaire : aucun des quatre protocoles retenus ici — MCP, A2A, AGNTCY et le protocole ACP d'IBM Research — n'est aujourd'hui gouverné par son créateur seul. La restriction est importante : elle ne s'étend pas à AP2, dont le socle ne documente à ce jour aucun transfert de gouvernance[^5], et dont le chapitre 3 examine le statut particulier. **Deuxièmement**, la consolidation ne s'est pas faite par coexistence polie mais par fusion réelle, dont l'absorption du protocole ACP d'IBM Research dans A2A est le cas exemplaire — avec, à la clé, l'entrée de l'absorbé au comité de pilotage de l'absorbant. **Troisièmement**, les métriques d'adoption publiées mesurent l'attention, non la production, et cet ouvrage les traitera systématiquement comme telles.

Ce que ce chapitre ne dit pas mérite d'être énoncé aussi clairement. Il ne dit pas que ces protocoles sont sûrs : la gouvernance neutre ne préjuge en rien de la robustesse d'une implémentation, et le chapitre 4 expose les surfaces d'attaque que le socle **nomme** — sans que celui-ci en date la documentation ni en établisse la mécanique. Il ne dit pas que MCP et A2A soient interchangeables ni concurrents : le chapitre 2 examine la doctrine officielle de complémentarité qui les articule. Il ne dit pas non plus que la neutralité de la gouvernance suffise à emporter la décision d'une institution financière réglementée — c'est l'objet des Parties III et VI que d'établir tout ce qu'il faut y ajouter.

La consolidation protocolaire est le point de départ de cet ouvrage. Elle n'en est pas la conclusion.

---

## Notes

[^1]: PRD §7.1, **F-01** (niveau [A]). Sources primaires : spécification MCP, révision 2025-11-25 (modelcontextprotocol.io), revalidée le 16 juillet 2026 ; annonce Anthropic de novembre 2024. Sur la révision attendue le 28 juillet 2026 : rapport de revalidation `verification/revalidation-2026-07-16.md`, d'après blog.modelcontextprotocol.io. **Réserve F-01** : la formule retenue est « cadre d'autorisation » et non « sécurisé » — la sécurité dépend de l'implémentation (voir ch. 4).

[^2]: PRD §7.1, **F-05** (niveau [A]). Source primaire : communiqué de la Linux Foundation du 29 juillet 2025 ; corroboration VentureBeat, Forbes. Le chevauchement relevé entre la composante ACP d'AGNTCY et A2A est une **analyse tierce**, attribuée comme telle et non endossée par le socle.

[^3]: PRD §7.8, **F-43** (niveau [B]). Sources primaires : blogs research.ibm.com (lancement de BeeAI et du protocole ACP, 17 mars 2025 ; billet du 28 mai 2025, dont la citation « the HTTP of agent communication » attribuée à Kate Blair) ; blog LF AI & Data du 29 août 2025 (fusion officielle dans A2A, entrée de Kate Blair au comité de pilotage technique d'A2A) ; github.com/orgs/i-am-bee.

[^4]: PRD §7.1, **F-02** (niveau [A]). Sources primaires : a2a-protocol.org/latest/announcing-1.0 ; communiqué de la Linux Foundation du 9 avril 2026 ; `GOVERNANCE.md` du dépôt a2aproject/A2A. **Réserve F-02** : « organisations de soutien » est une métrique auto-déclarée dont l'unité n'est pas définie ; soutien ≠ production. Le socle documente la **composition** du comité de pilotage technique, non ses règles de vote ou de décision.

[^5]: PRD §7.1, **F-04** (niveau [A]). Sources primaires : annonce Google Cloud du 16 septembre 2025 ; communiqué de la Linux Foundation du 9 avril 2026. **Réserve F-04** : endossement déclaré, pas adoption en production vérifiée. Le socle ne documente aucun transfert de gouvernance d'AP2 à une fondation — d'où la restriction énoncée en conclusion du présent chapitre.

[^6]: PRD §7.1, **F-06** (confiance moyenne — usage descriptif seulement). Ehtesham et al., arXiv 2505.02279, mai 2025. **Réserve majeure** : préprint non révisé par les pairs, dont la deuxième étape est devenue obsolète comme prescription après la fusion d'août 2025. Cité ici comme jalon historiographique, jamais comme guidance.

[^7]: PRD §8.1, garde-fous **R-1** (l'ACP protocolaire n'est pas un standard vivant) et **R-8** (désambiguïsation des emplois de « (agentic) control plane » / « ACP »). Formes imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.1. Branches (b) et (c) : PRD §7.5 **F-48** et §7.8 **F-42**.

[^8]: PRD §8.2.1 (règle d'attribution des métriques d'adoption des protocoles) ; formulation imposée par PRDPlan §4.4 (« soutien ≠ production »).

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (8 notes ; termes anglais entre parenthèses à la 1re occurrence, AP2 inclus)
     3. Balayage garde-fous ...... fait (§8.2.1 attribué à chaque occurrence ; R-1/R-8 : sigle ACP toujours qualifié ;
                                   encadré de désambiguïsation posé ici — 1re occurrence de l'ouvrage)
     4. Relecture adversariale ... fait (relecteur distinct ; 4 réfutations bloquantes + 5 réserves, toutes corrigées :
                                   « sept mois » -> quatre (F-05) ; « dix-huit mois » -> dix-sept ; « quatorze » -> treize ;
                                   restriction de la conclusion pour exclure AP2 (F-04) ; note AP2 ajoutée ;
                                   inférences du TSC marquées ; attributions §8.2.1 rétablies ; doublon ch. 2 réduit au renvoi ;
                                   4e branche ACP (AGNTCY) exposée en encadré et signalée au PRD)
     5. Commit + registre de gel . fait
     6. Passe de conformité (audit du 17 juill. 2026 — aucune information nouvelle, date de gel inchangée) :
        M-02 — « le chapitre 4 documente les surfaces d'attaque connues DÈS L'ORIGINE » (conclusion) : datation
               retirée du TOC par correctif du 16 juill. 2026 (TOC v1.3) et jamais portée par le socle (PRD §10.8,
               qui pose que celui-ci « ne les date pas ») ; le ch. 4 lui-même refuse de l'affirmer. Remplacée par
               ce que le socle porte : des risques nommés, sans datation ni mécanique. Les risques ne sont pas
               énumérés ici — les nommer importerait du F-36 que l'en-tête de ce chapitre ne déclare pas (CA-1) ;
               le renvoi au ch. 4, qui les trace, suffit.
        m-03 — « AGNTCY revendique de son côté plus de 65 entreprises » (§1.3) : attribué au communiqué de la
               Linux Foundation du 29 juillet 2025 et daté en prose (PRD §8.2.1), porteur de la clause
               « soutien ≠ production » (PRDPlan §4.4) ; la comparaison avec les chiffres d'avril 2026 est
               désormais explicitement écartée, comme au ch. 3 §3.2 (intervalle : plus de huit mois).
        m-04 — séquence F-06 : « MCP → ACP → A2A → ANP » -> « MCP → ACP protocolaire → A2A → ANP » (R-8, sigle
               jamais nu ; forme du ch. 3 §3.4). L'intitulé développé est au socle depuis le 17 juill. 2026
               (F-43, [B]) et reste porté à la première occurrence du chapitre (§1.1).
-->
