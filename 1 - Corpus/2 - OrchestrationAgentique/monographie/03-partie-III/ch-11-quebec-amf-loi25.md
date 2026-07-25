# Chapitre 11 — Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-25, F-27 ; F-09, F-15, F-24, F-26 (renvois) |
| Garde-fous à surveiller (PRD §8) | **réserve F-25** (jamais « en attente » ni « en projet ») ; **réserve d'interprétation de F-27** (nuance Fasken au niveau [C]) ; §8.2.4 et R-7 (motifs « E-23 » — contexte réglementaire pur, filtrés) ; lacune §10.4 (encadré §11.3) |
| Volumétrie cible | ~3000 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Le Québec dispose du cadre le plus explicite — et l'art. 12.1 (révision humaine sur demande) entre en friction directe avec la décision agentique autonome.

---

De tous les régimes examinés dans cette partie, celui du Québec est le seul qui impose, en droit positif et depuis plusieurs années déjà, qu'un être humain identifié puisse reprendre une décision qu'une machine a prise seule. Ce n'est pas une orientation, ni une attente de surveillance prudentielle, ni une doctrine de régulateur : c'est une obligation d'entreprise, que la personne concernée peut faire valoir par une demande[^5]. Pour l'architecte qui conçoit une chaîne de décision agentique destinée à une clientèle assujettie à ce régime, cette obligation n'est pas un paramètre de conformité à documenter en fin de projet — elle est une contrainte de conception, au même titre que la disponibilité ou la latence.

Ce chapitre soutient que le Québec offre le cadre le plus explicite du paysage canadien, et que cette explicitation crée une friction directe avec l'idée même de décision agentique autonome. Il soutient aussi — et c'est la nuance qui décide de l'architecture — que cette friction est de nature à être résolue par la conception plutôt que subie, mais que le socle de cet ouvrage ne permet pas de dire à quelles conditions exactes. Deux instruments sont ici en jeu : la ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers, dont le calendrier converge avec celui du régime fédéral, et l'article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé, dont le texte est en vigueur depuis 2023 et dont chaque mot compte.

## 11.1 La ligne directrice sur l'IA de l'AMF : chronologie et convergence

L'Autorité des marchés financiers a publié son projet de ligne directrice sur l'intelligence artificielle le **3 juillet 2025**, ouvrant une consultation close le **7 novembre 2025** — un peu plus de quatre mois. Desjardins y a participé, ce que son rapport annuel 2025 documente. La version **finale a été publiée le 30 mars 2026**, et elle **entre en vigueur le 1er mai 2027**[^1].

Ces trois dates appellent d'emblée une mise en garde de rédaction, parce que le domaine se périme par trimestres et que la formulation fautive est encore répandue : **la ligne directrice de l'AMF n'est ni « en projet » ni « en attente »**. Elle est finale depuis le 30 mars 2026, et seule son entrée en vigueur reste à venir[^2]. Tout document de gouvernance interne qui la décrirait comme un texte de consultation décrirait un état du monde périmé depuis le 30 mars 2026.

La donnée structurante n'est pas la date de publication, mais celle de l'entrée en vigueur. Le **1er mai 2027** est aussi la date d'entrée en vigueur de la ligne directrice E-23 du Bureau du surintendant des institutions financières, dont le chapitre 9 traite[^3]. Deux régimes distincts — l'un fédéral et prudentiel, l'autre québécois et sectoriel — convergent sur un même jour. Du 30 mars 2026 au 1er mai 2027, les institutions disposent de **treize mois** pour se préparer ; à la date de gel de ce chapitre, il en reste **neuf et demi**.

**Lecture de l'auteur** : le socle établit la coïncidence des dates, non son intentionnalité. Aucune source du socle n'indique que l'AMF ait aligné son calendrier sur celui du BSIF, ni l'inverse ; il serait imprudent d'en faire un argument sur les intentions des régulateurs. En revanche, la conséquence opérationnelle ne dépend pas de l'intention : une institution dont l'exploitation relève des deux régimes n'aura pas deux fenêtres de préparation successives, mais une seule, et devra faire converger deux programmes de conformité vers un même jalon. C'est un fait de planification, et il est robuste indépendamment de ce qui l'a produit.

Il faut par ailleurs se garder d'une lecture trop confortable du délai. Les treize mois séparant la publication finale de l'entrée en vigueur ne sont pas une période d'observation : ce sont les seuls mois pendant lesquels une institution peut encore modifier une architecture déjà en exploitation. Le rapport annuel 2025 de Desjardins déclare que l'institution a participé à la consultation close en novembre 2025[^1]. **Lecture de l'auteur** : le socle documente la participation, non ce qu'elle révèle du suivi du dossier par le secteur. Le socle ne documente pas non plus la participation d'autres institutions à cette consultation, et cet ouvrage ne conclut rien de ce silence : une absence de source n'est pas une absence de fait.

Il faut ici énoncer sans détour ce que ce chapitre ne peut pas faire. **Le socle de cet ouvrage porte le calendrier de la ligne directrice, non son contenu.** Les entrées vérifiées documentent la publication du projet, la clôture de la consultation, la publication de la version finale et son entrée en vigueur ; elles ne documentent pas les exigences que ce texte formule, article par article[^4]. Cette monographie s'interdit de combler cet écart par de la reconstruction plausible : il serait aisé, et parfaitement irresponsable, de déduire le contenu d'une ligne directrice de son titre et du contexte réglementaire environnant. L'encadré du paragraphe 11.3 expose cette lacune avec celle qui la jouxte, et le lecteur qui doit bâtir un programme de conformité y trouvera la seule instruction utile : lire le texte à la source.

## 11.2 L'article 12.1 : trois obligations, un texte

L'autre instrument québécois n'appelle aucune réserve de ce genre : son texte officiel a été consulté directement, et il est en vigueur.

L'article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (P-39.1) est **en vigueur depuis le 22 septembre 2023**, introduit par l'article 110 du chapitre 25 des lois de 2021 — la « Loi 25 ». Il précède donc de près de trois ans la date de gel du présent chapitre, et de plus de trois ans et demi l'entrée en vigueur des deux lignes directrices examinées ci-dessus. Il ne s'agit pas d'un texte à venir : il est le droit applicable, et il l'était déjà lorsque les premiers déploiements agentiques canadiens documentés dans la Partie V ont été annoncés[^5].

Son déclencheur est une formule précise, qu'il faut citer plutôt que paraphraser : l'article s'applique à toute entreprise qui rend une « **décision fondée exclusivement sur un traitement automatisé** » de renseignements personnels[^5]. Chacun de ces mots portera son poids au paragraphe suivant ; retenons pour l'instant que le déclencheur, tel qu'écrit, ne nomme aucune technologie. Il ne parle ni d'intelligence artificielle, ni de modèle, ni d'agent : il parle de la **place de l'humain dans la production de la décision**. **Lecture de l'auteur** : le socle donne le texte, il ne pose aucune doctrine de neutralité technologique ; à s'en tenir aux mots du déclencheur, un arbre de règles écrit à la main en 1998 paraît déclencher l'article 12.1 aussi sûrement qu'un système multi-agents de 2026, dès lors que la décision est rendue sans intervention humaine.

Deux conditions, et non une seule, commandent donc l'application de l'article. La première tient à l'objet du traitement : il doit porter sur des **renseignements personnels**[^5]. La seconde tient à la place de l'humain : la décision doit être fondée *exclusivement* sur le traitement automatisé. Quant à l'assujettissement, le socle rapporte le déclencheur du texte — l'obligation pèse sur **toute entreprise** rendant une telle décision[^5] — sans trancher la portée du régime à l'égard des institutions financières sous charte fédérale, celles que le chapitre 9 place sous E-23 : le socle est muet sur ce point[^4]. **Lecture de l'auteur** : pour une entreprise assujettie à la Loi 25, les décisions individuelles rendues à une clientèle portent le plus souvent sur des renseignements personnels ; la première condition est alors le cas ordinaire, et c'est la seconde qui décide — celle qui relève de l'architecture. Le paragraphe suivant lui est consacré.

Trois obligations en découlent[^5].

**Premièrement, informer.** L'entreprise doit informer la personne concernée qu'une telle décision a été rendue, **au plus tard au moment de la décision**. L'obligation est inconditionnelle : elle ne dépend d'aucune demande. Elle est aussi datée — l'information ne peut être différée à une communication ultérieure.

**Deuxièmement, expliquer, sur demande.** À la demande de la personne, l'entreprise doit lui communiquer les renseignements personnels utilisés pour rendre la décision, ainsi que « **les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision** », et l'informer de son droit de faire rectifier ces renseignements. La formule mérite d'être lue lentement : la loi ne demande pas une explication générale du fonctionnement du système, mais les raisons et les facteurs **ayant mené à cette décision-là**. Elle porte sur l'instance, non sur le modèle.

**Troisièmement, permettre la révision humaine.** L'entreprise doit donner à la personne « **l'occasion de présenter ses observations à un membre du personnel de l'entreprise en mesure de réviser la décision** ». Là encore, chaque terme est agissant : un membre du personnel — donc une personne rattachée à l'entreprise ; en mesure de réviser — donc doté du pouvoir de défaire ce que le système a fait, et pas seulement d'expliquer ou de transmettre.

Le déclenchement de ces trois obligations est ce qui fait de l'article 12.1 le texte le plus explicite du corpus canadien examiné dans cette partie. **Lecture de l'auteur** — le socle en fournit les éléments, il ne pose pas le classement : le régime fédéral spécifique à l'IA n'existe pas, la trajectoire législative en cours étant une réforme de la protection des renseignements personnels et non une loi sur l'IA (chapitre 10)[^6] ; l'avis 11-348 des Autorités canadiennes en valeurs mobilières énonce que les lois existantes s'appliquent sans en créer de nouvelles (chapitre 12)[^7] ; E-23 ne nomme ni l'agentique ni les agents ; sa définition de « modèle » englobe les méthodes d'IA et d'apprentissage automatique, d'où une **couverture implicite** que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise — le chapitre 9 en a la charge[^3]. Face à ces instruments, l'article 12.1 énonce une obligation nommée, que la personne concernée peut faire valoir, et dont l'objet est précisément le point où l'autonomie de la machine s'arrête. C'est en ce sens, et en ce sens seulement, que la thèse de ce chapitre parle du cadre « le plus explicite ».

## 11.3 Le critère « exclusivement » et l'humain-dans-la-boucle

Tout, désormais, se joue sur un adverbe.

L'article 12.1 ne s'applique qu'aux décisions fondées **exclusivement** sur un traitement automatisé[^5]. Le texte ne définit pas ce que l'exclusivité exclut, et c'est là que l'architecture rejoint le droit. Selon l'analyse du cabinet Fasken, une intervention humaine significative **avant** la décision écarte l'application de l'article 12.1 — nuance déterminante pour qualifier les systèmes agentiques comportant un humain-dans-la-boucle (*human-in-the-loop*)[^8].

Cette lecture doit être maniée avec la plus grande prudence, et le socle impose ici sa propre réserve : **il s'agit d'une interprétation de cabinet, retenue au niveau de preuve [C]** — un repérage documentaire à confirmer, qui ne peut porter un fait central[^8]. Une institution qui fonderait son architecture de décision sur cette seule nuance ferait reposer un choix structurant sur une interprétation doctrinale non confirmée par le socle de cet ouvrage, et que le socle n'a pas confrontée aux positions de la Commission d'accès à l'information[^4].

Il faut au passage écarter une confusion terminologique dont cet ouvrage fait un point de vocabulaire : **l'humain-dans-la-boucle et la révision humaine de l'article 12.1 ne sont pas la même chose**[^9]. Le premier est un point d'arrêt inséré dans l'exécution, en amont ou au cours de la décision ; la seconde est un recours ouvert à la personne concernée, sur demande, **après** que la décision a été rendue. Aucun dispositif d'humain-dans-la-boucle ne *satisfait* donc par lui-même la troisième obligation. S'il est jugé significatif au sens de l'analyse citée — au niveau [C][^8] —, il écarte l'article en entier, obligation comprise ; s'il ne l'est pas, l'article s'applique intégralement et la révision *a posteriori* reste due. Dans les deux branches, outiller l'humain-dans-la-boucle n'outille pas la révision humaine ; confondre les deux notions revient à croire qu'on a satisfait une obligation en outillant une propriété différente.

> **État de la recherche — le contenu de la ligne directrice de l'AMF, les positions de la CAI, et la portée du régime**
>
> Trois questions restent ouvertes à la date de gel de ce chapitre, et cet ouvrage se refuse à les combler.
>
> **Première question** : que dit, article par article, la version finale de la ligne directrice sur l'IA de l'AMF publiée le 30 mars 2026 ? Ce que le socle porte : les dates de la trajectoire du texte — projet, consultation, publication finale, entrée en vigueur —, établies par sources primaires (lautorite.qc.ca) et corroborations, et rien d'autre. Lacune ouverte le 16 juillet 2026 ; **aucune passe de recherche dédiée n'a été conduite** — l'extraction article par article du texte final ne relevait du périmètre ni des trois passes du socle (PRD Annexe A), ni de la passe ciblée du 16 juillet 2026. Source à retrouver : `lautorite.qc.ca`. La lacune est donc ouverte, non réfractaire[^4] : la question reste ouverte ; aucune inférence n'est proposée ici — aucune exigence n'est attribuée à ce texte, et aucune n'est inférée de son titre ni de son contexte.
>
> **Deuxième question** : comment la Commission d'accès à l'information interprète-t-elle l'article 12.1 appliqué aux systèmes multi-agents ? Les documents de position de la CAI figurent au corpus des sources de F-27, mais les positions détaillées sur ce point précis n'ont fait l'objet d'aucune passe ciblée et ne figurent pas au socle[^4]. La nuance Fasken sur le critère « exclusivement » reste donc, à ce jour, une analyse de cabinet au niveau [C], **non confrontée à la position de l'autorité qui applique la loi**[^8]. Aucune inférence n'est proposée ici sur l'issue de cette confrontation.
>
> **Troisième question** : le régime de l'article 12.1 atteint-il les institutions financières sous charte fédérale, celles qu'E-23 vise au chapitre 9 ? Le socle porte le déclencheur du texte — « toute entreprise » — et rien sur la portée du régime à l'égard de ces institutions ; aucune passe ne l'a instruite[^4]. La question n'est pas théorique : elle décide si les deux régimes examinés dans cette partie se cumulent sur une même chaîne de décision ou s'appliquent à des périmètres disjoints. Aucune réponse n'est proposée ici.
>
> **Conséquence pour le lecteur** : une institution qui doit décider aujourd'hui ne peut pas s'appuyer sur cet ouvrage pour ces trois points ; elle doit lire la ligne directrice finale à la source (lautorite.qc.ca) et faire qualifier tant le critère d'exclusivité que son propre assujettissement par un conseil juridique. Cette monographie n'émet aucun conseil juridique (PRD §3).

## 11.4 Conséquences d'architecture

Que retient l'architecte de tout ceci ? Le socle porte les obligations, non leurs conséquences techniques ; les trois contraintes qui suivent sont une **lecture de l'auteur** adossée au texte de l'article 12.1.

**La première contrainte porte sur la traçabilité de l'instance.** L'obligation d'expliquer ne vise pas le modèle, mais « les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision »[^5] — c'est-à-dire à celle-ci, pour cette personne, à ce moment. Un système qui ne conserve pas de quoi reconstituer le cheminement d'une décision individuelle ne peut pas satisfaire cette obligation *a posteriori*, quelle que soit la qualité de sa documentation générale. La contrainte est d'autant plus lourde que la décision est produite par une chaîne d'agents : ce qu'il faut restituer n'est pas la trace d'un appel, mais celle d'un enchaînement. Le chapitre 13 traduit systématiquement ce type d'exigence en contraintes d'orchestration ; on se contentera ici de noter que l'obligation est due sur demande, à une date qu'aucun concepteur ne choisit, ce qui interdit de compter sur une reconstitution improvisée.

**La deuxième contrainte porte sur le déclencheur d'information.** L'entreprise doit informer la personne « au plus tard au moment de la décision »[^5]. C'est une exigence de synchronisme : le moment de la décision doit être un événement identifiable dans le système, pas un état qui se constate après coup. Une architecture dans laquelle nul ne saurait dire à quel instant précis la décision a été rendue — parce que plusieurs agents y ont contribué de façon diffuse — ne rend pas seulement l'audit difficile : elle rend l'obligation d'information mécaniquement inexécutable.

**La troisième contrainte porte sur la réversibilité.** La loi exige un membre du personnel « en mesure de réviser la décision »[^5]. Cela suppose non seulement qu'une personne soit désignée, mais que le système admette qu'une décision déjà rendue, déjà communiquée et peut-être déjà exécutée en aval soit défaite. Le socle établit l'obligation, il ne dit rien des moyens techniques de la satisfaire ; mais admettre la révision d'une décision autonome par un humain doté du pouvoir de la défaire paraît difficilement séparable d'une exigence de conception : cela ne peut pas être ajouté à une chaîne agentique après coup sans en revoir les effets de bord.

C'est ici que la friction annoncée par la thèse prend sa forme précise. La décision agentique autonome a pour intérêt économique de rendre une décision sans humain ; l'article 12.1 attache précisément à cette absence d'humain un triple régime d'obligations. **Lecture de l'auteur** : le socle fournit le fait générateur — l'exclusivité du traitement automatisé (F-27)[^5] — et l'objectif économique de l'agentique ; il ne qualifie pas la friction. Celle-ci paraît structurelle plutôt qu'accidentelle, en ce que le fait générateur de l'obligation est exactement la propriété que l'on cherche à obtenir. Deux voies s'ouvrent en conséquence, et le socle n'en valide aucune : soit l'entreprise réintroduit une intervention humaine de nature à écarter le critère d'exclusivité — voie dont on a vu qu'elle repose sur une interprétation au niveau [C], non confrontée à la position de la CAI[^8] ; soit elle assume le déclenchement de l'article 12.1 et outille les trois obligations. La seconde voie a ceci de recommandable qu'elle ne dépend d'aucune interprétation contestable ; elle a ceci de coûteux qu'elle impose la traçabilité, le synchronisme et la réversibilité à l'ensemble de la chaîne. Le chapitre 23 en présente un flux illustratif de bout en bout ; le chapitre 13 en tire le principe général.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Deux acquis, et une lecture. **Premièrement**, la ligne directrice sur l'IA de l'AMF est finale depuis le 30 mars 2026 et entre en vigueur le 1er mai 2027 — le même jour qu'E-23 : les institutions relevant des deux régimes n'ont qu'une seule fenêtre de préparation, dont il reste neuf mois et demi à la date de gel de ce chapitre. **Deuxièmement**, l'article 12.1 de la Loi 25 est en vigueur depuis le 22 septembre 2023 et impose trois obligations — informer au plus tard au moment de la décision, expliquer sur demande les raisons et les principaux facteurs et paramètres ayant mené à la décision, et offrir la révision par un membre du personnel en mesure de réviser. **La lecture**, enfin, et elle est de l'auteur : le déclencheur de ces obligations, tel qu'il est écrit, est une propriété d'architecture — l'exclusivité du traitement automatisé — et non une technologie, ce qui les rendrait indifférentes au vocabulaire agentique. Le socle donne le texte ; il ne pose pas cette doctrine, et la Commission d'accès à l'information ne l'a pas confirmée dans le socle de cet ouvrage.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas ce que la ligne directrice de l'AMF exige : le socle n'en porte que le calendrier, et l'encadré du paragraphe 11.3 expose cette lacune plutôt que de la masquer. Il ne dit pas qu'un humain-dans-la-boucle écarte l'article 12.1 : cette lecture est une analyse de cabinet au niveau [C], que la position de la Commission d'accès à l'information n'a pas confirmée dans le socle de cet ouvrage. Il ne dit pas non plus qui, au juste, le régime atteint : le socle porte le déclencheur — « toute entreprise » — et se tait sur la portée du texte à l'égard des institutions financières sous charte fédérale[^4] ; c'est la troisième question ouverte de l'encadré, et elle décide si les deux régimes de cette partie se cumulent sur une même chaîne de décision. Il ne dit pas non plus comment satisfaire les trois obligations : la traduction des contraintes réglementaires en contraintes d'orchestration est l'objet du chapitre 13, et son instanciation, celui du chapitre 23. Il n'émet enfin aucun conseil juridique.

Le Québec, en somme, a écrit avant les autres ce que les autres régimes canadiens n'ont pas encore nommé. Il l'a fait dans un texte de protection des renseignements personnels, sans employer le mot « agent ». C'est peut-être la meilleure illustration de ce que la thèse de l'ouvrage — l'autonomie encadrée — doit au droit : le régime ne se déclenche pas sur la technologie employée, mais sur la place qu'on y laisse à l'humain.

---

## Notes

[^1]: PRD §7.3, **F-25** (niveau [A], confiance haute). Sources : lautorite.qc.ca (document de consultation, projet publié le 3 juillet 2025 ; consultation close le 7 novembre 2025) ; version finale publiée le 30 mars 2026, en vigueur le 1er mai 2027 ; corroborations Norton Rose Fulbright et rapport annuel Desjardins 2025 — la participation de Desjardins à la consultation y est une **déclaration d'entreprise, non auditée indépendamment** (PRD §8.2.2).

[^2]: **Réserve F-25** (PRD §7.3) et PRDPlan §4.3 : ne jamais écrire « en attente » ni « en projet » à propos de la ligne directrice de l'AMF — état périmé depuis le 30 mars 2026. Forme imposée : Annexe D §D.7 du glossaire (`monographie/90-annexes/annexe-d-glossaire.md`) — « finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 ».

[^3]: PRD §7.3, **F-09** (entrée **[A/B mixte]** — [A] pour les faits des passes 1-2, [B] pour les exigences opératoires extraites du texte intégral d'E-23 le 16 juill. 2026 ; une extraction de source primaire **enrichit** l'entrée d'un contenu de rang inférieur, elle n'« élève » pas une entrée déjà votée 3-0). **Faits mobilisés ici en strate [A]** : date de publication, entrée en vigueur, portée, définition de « modèle », couverture agentique tenue pour une inférence d'analystes. **Un fait mobilisé ici en strate [B]**, contrairement à ce que cette note a déclaré jusqu'au 17 juillet 2026 : la **vérification négative** (« E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration »), que le PRD range expressément sous [B] et que le §11.2 énonce. Le présent chapitre ne mobilise en revanche aucune **exigence opératoire** d'E-23 (cycle de vie, inventaire, cotation, documentation, surveillance) — leur développement revient au chapitre 9. *La note affirmait « relèvent tous de la strate [A] » : l'énumération [A] de F-09 est close et ne porte pas la vérification négative (audit du 17 juill. 2026 — même classe que M-06, relevé lors de sa correction et non par l'audit).* **Renvoi** : la ligne directrice E-23 du BSIF, publiée en version finale le 11 septembre 2025, entre en vigueur le 1er mai 2027 et s'applique aux institutions financières fédérales. Source primaire : osfi-bsif.gc.ca. Sur la couverture de l'IA agentique par E-23 : elle relève d'une **inférence d'analystes juridiques**, jamais d'une terminologie du BSIF — formulation imposée par PRD §8.2.4 et PRDPlan §4.4, reprise au §11.2 du présent chapitre **dans la substance imposée par §8.2.4**, en renvoi seulement. *L'attestation d'une reprise « dans la forme §4.4 » est rectifiée le 17 juillet 2026 (audit, m-20) : la forme de §4.4 a été enrichie le 16 juillet 2026, postérieurement au gel du présent chapitre — l'avertissement en tête de §4.4 admet le rendu antérieur qui en porte la substance, et proscrit l'attestation qu'aucune pièce n'a vérifiée.* Le développement en revient au chapitre 9.

[^4]: PRD §10.4 (lacune ouverte) : le contenu article par article de la ligne directrice IA finale de l'AMF n'est pas au socle — « seules les dates sont au socle » — non plus que les positions détaillées de la Commission d'accès à l'information sur l'article 12.1 appliqué aux systèmes multi-agents. **Portée du régime** : ni F-27 ni F-09 ne traitent de l'assujettissement des institutions financières sous charte fédérale à la Loi 25 ; le socle est muet, et la lacune §10.4 (« réglementaire fin ») reste ouverte. Méthode des passes de recherche : PRD Annexe A (trois passes, juillet 2026) ; le complément P0 du 16 juillet 2026 est une passe distincte, dont le périmètre documenté (`verification/revalidation-2026-07-16.md`) ne couvre aucune de ces trois questions. Formulation de l'encadré imposée par PRDPlan §4.4.

[^5]: PRD §7.3, **F-27** (niveau [B] — texte officiel consulté sur LégisQuébec le 16 juillet 2026). Article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1), en vigueur depuis le 22 septembre 2023 (2021, c. 25, a. 110). Sources : legisquebec.gouv.qc.ca (texte officiel) ; cai.gouv.qc.ca ; quebec.ca (page officielle d'interprétation). Les formules entre guillemets sont citées verbatim du texte officiel ; conformément à l'Annexe D §D.5 du glossaire, elles ne sont pas paraphrasées. **Borne de cette déclaration** (rectifiée le 17 juillet 2026 — audit, m-18) : le socle rapporte « toute entreprise » **hors guillemets**, comme déclencheur du régime, sans en établir le libellé officiel. Le membre est donc rendu ici sans guillemets et n'est pas couvert par la présente déclaration de verbatim — même traitement qu'au **ch. 13, note [^4]**, qui l'exclut expressément de la sienne. Le socle ne portant que le français, **aucune glose anglaise du libellé n'est proposée** : elle exigerait une élévation par consultation primaire de la version anglaise de P-39.1 (ch. 13, arbitrage f).

[^6]: PRD §7.3, **F-24** (niveau [B], revalidé le 16 juillet 2026) — **renvoi au chapitre 10**. Le projet de loi C-36 (*Protecting Privacy and Consumer Data Act*) est une réforme de la protection des renseignements personnels portant des volets IA, non une loi sur l'IA de type LIAD ; le vide fédéral sur la régulation spécifique de l'IA persiste. Source : parl.ca/LEGISinfo (45-1/c-36), consulté directement.

[^7]: PRD §7.3, **F-26** (niveau [B] — consulté directement sur osc.ca) — **renvoi au chapitre 12**. Avis 11-348 des Autorités canadiennes en valeurs mobilières, publié le 5 décembre 2024 : les lois sur les valeurs mobilières existantes s'appliquent aux systèmes d'IA, la guidance « ne crée ni ne modifie aucune exigence ».

[^8]: **Réserve d'interprétation de F-27** (PRD §7.3, **niveau [C]**) : selon l'analyse du cabinet Fasken, une intervention humaine significative avant la décision écarte l'application de l'article 12.1. Le PRD qualifie expressément ce point de réserve d'interprétation de niveau [C] — repérage à confirmer, qui ne peut porter un fait central (PRD §7, niveaux de preuve ; §10, dernier alinéa). La confrontation avec les positions de la Commission d'accès à l'information est une lacune ouverte (PRD §10.4).

[^9]: Annexe D §D.2 du glossaire (`monographie/90-annexes/annexe-d-glossaire.md`), entrée « humain-dans-la-boucle » (*human-in-the-loop*, PRD §7.6, F-15) : « À ne pas confondre avec la révision humaine *a posteriori* de l'art. 12.1 (F-27). » La distinction est posée au glossaire et rappelée ici ; son exploitation architecturale relève des chapitres 13 et 23.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (9 notes ; formules de l'art. 12.1 citées verbatim, non paraphrasées —
                                   Annexe D §D.5 ; « human-in-the-loop » glosé à sa 1re occurrence).
                                   ⚠ RECTIFIÉ LE 17 JUILL. 2026 (audit, M-09) — ce bloc a porté, du 16 au 17 juill.
                                   2026, une ATTESTATION DE CONFORMITÉ POSÉE SUR UN CONTENU NON TRACÉ. Il déclarait
                                   CA-5 « MANQUÉ » au premier jet, au motif que « décision fondée exclusivement sur
                                   un traitement automatisé » était employée sans équivalent anglais, et se déclarait
                                   « corrigé » par l'ajout de la glose « decision based exclusively on automated
                                   processing » au §11.2. LE CORRECTIF ÉTAIT LA FAUTE : F-27 ne porte que le texte
                                   français (LégisQuébec) ; le ch. 13 a arbitré qu'une telle glose « exige une
                                   élévation par consultation primaire […] elle ne peut pas être rendue par
                                   l'auteur », et aucune élévation n'a été conduite. CA-5 n'était donc PAS manqué :
                                   la grille (verification/relecture-CA.md) pose expressément « Aucune traduction
                                   n'est inventée — c'est la bonne réponse » et « le socle n'en porte pas le libellé
                                   anglais ». La glose est RETIRÉE du §11.2 ; la borne est posée en note [^5].
                                   NE PAS LA RE-FABRIQUER au nom de CA-5 à la prochaine reprise — c'est exactement
                                   ce que ce bloc a fait faire une fois.
     3. Balayage garde-fous ...... fait :
                                   - réserve F-25 (motif « en attente|en projet ») : aucune occurrence fautive ;
                                     la formule imposée est employée et rappelée en note [^2] ;
                                   - motif R-7 (« E-23|B-13 ») : contexte réglementaire pur, aucune correspondance
                                     produit ↔ réglementation dans ce chapitre — filtré conformément à PRDPlan §4.3 ;
                                   - motif §8.2.4 (« E-23.*agentique ») : une occurrence, au §11.2, en renvoi au ch. 9 ;
                                     formulation imposée de PRDPlan §4.4 — le premier jet l'ALTÉRAIT (point-virgule
                                     changé en virgule, « englobe » en « englobant ») tout en certifiant en note [^3]
                                     et ici même une reprise « mot pour mot » : contrôle qui attestait ce qu'il
                                     n'avait pas vérifié. Forme rétablie sur l'état de §4.4 au 16 juill. 2026 ;
                                     ⚠ l'attestation « rétablie caractère pour caractère » est RECTIFIÉE le
                                     17 juill. 2026 (audit, m-20) : la forme de §4.4 a été ENRICHIE le 16 juill.
                                     2026, après le gel de ce chapitre, et aucune pièce n'a le droit d'attester un
                                     verbatim qu'elle n'a pas (avertissement en tête de §4.4). Le rendu est
                                     conforme dans sa SUBSTANCE (§8.2.4) et n'est pas rouvert ; seule
                                     l'attestation l'est. Même racine que M-07 (ch. 9) et m-17 (ch. 10) ;
                                   - motif R-8 (« ACP|control plane|plan de contrôle ») : aucune occurrence ;
                                   - aucune métrique auto-déclarée dans ce chapitre (§8.2.2/§7.5 sans objet).
     4. Relecture adversariale ... FAITE (deux relecteurs indépendants, distincts du rédacteur — PRDPlan §4.2.4).
                                   Premier jet RÉFUTÉ : 5 constats bloquants + 12 réserves, tous vérifiés fondés
                                   contre le socle et appliqués (aucun écarté). Ce que la relecture a réfuté :
                                   (a) CHIFFRE FABRIQUÉ — « périmé depuis plus d'un an » là où l'écart 30 mars 2026
                                       → 16 juillet 2026 est de 3 mois et 17 jours (rapport de 1 à 3,5). Même défaut
                                       qu'au ch. 1 (« sept mois » contre quatre). Remplacé par la forme datée
                                       « périmé depuis le 30 mars 2026 » (Annexe D §D.7) — insensible au temps.
                                   (b) CA-3 — « source primaire auditée » pour le rapport annuel Desjardins, à ses
                                       deux occurrences (§11.1 et note [^1]) : §8.2.2 qualifie les déclarations
                                       d'entreprise de NON auditées indépendamment, et F-25 ne porte aucun
                                       qualificatif d'audit. « auditée » supprimé, attribution §8.2.2 posée.
                                   (c) INFÉRENCES PRÉSENTÉES COMME FAITS (CA-1 ; parade PRDPlan §7) — quatre passages
                                       où le chapitre appliquait sa propre règle une fois sur deux ou sur trois :
                                       - assujettissement (« le socle le formule sans restriction » ; « presque
                                         toujours remplie ») : un silence du socle converti en constat positif,
                                         neuf lignes après avoir écrit « une absence de source n'est pas une absence
                                         de fait ». Le socle est muet sur la portée du régime à l'égard des
                                         institutions sous charte fédérale (§10.4) → dit comme tel + 3e question
                                         ouverte ajoutée à l'encadré §11.3 ;
                                       - §11.4, annonce « découlent du texte […] et non d'une doctrine » puis
                                         contraintes 1 et 2 non marquées alors que la 3 l'était : même opération
                                         intellectuelle marquée une fois sur trois. Annonce réécrite en Lecture de
                                         l'auteur couvrant les trois ; marquage isolé de la 3e retiré (redondant) ;
                                       - « elle est structurelle » (gras, asserté) — moitié de la thèse TOC laissée
                                         sans marquage quand l'autre moitié (« cadre le plus explicite ») l'avait ;
                                       - neutralité technologique (« déclenche aussi sûrement ») promue en acquis
                                         dans « Ce que ce chapitre établit ». Marquée au §11.2 ; en conclusion,
                                         déplacée des acquis vers une lecture attribuée (« Deux acquis, et une
                                         lecture »), la CAI n'ayant rien confirmé au socle.
                                   (d) PROVENANCE DE RECHERCHE de l'encadré §11.3 — « à la clôture des trois passes
                                       documentées à l'Annexe A » : l'Annexe A ne date pas cette clôture, et le
                                       complément P0 du 16 juillet 2026 est une passe DISTINCTE dont le périmètre
                                       (verification/revalidation-2026-07-16.md : RTR, cadre bancaire, Confluent,
                                       C-36, MCP/A2A, BMO, Sun Life, LangChain/CrewAI, FTM) ne couvre ni le contenu
                                       de la ligne directrice AMF ni les positions de la CAI. L'encadré laissait
                                       croire que ces questions avaient été instruites, et taisait ce qui avait été
                                       tenté et pourquoi la recherche échoue — les deux emplacements variables de la
                                       forme imposée §4.4, dans l'encadré même dont la fonction est l'honnêteté
                                       épistémique. Date de gel découplée de la provenance ; lacune qualifiée
                                       « ouverte, non réfractaire » (extraction non entreprise, non pas impossible).
                                   (e) LACUNE → FAIT NÉGATIF — « non tranchée par la CAI » (§11.3) : le socle dit que
                                       les positions de la CAI n'y sont pas, pas que la CAI n'a pas tranché. Aligné
                                       sur la formule correcte de l'encadré et du §11.4.
                                   (f) AUTOCONTRADICTION (§11.3) — « due indépendamment de tout dispositif
                                       d'humain-dans-la-boucle » réfuté par la suite de sa propre phrase. Réécrit en
                                       deux branches explicites (dispositif significatif [C] → écarte l'article en
                                       entier ; non significatif → article intégral, révision due).
                                   (g) DÉRIVE DE THÈSE — la clôture attribuait à l'ouvrage une thèse de droit
                                       (« ce n'est pas la technologie que le droit encadre ») là où TOC.md pose une
                                       thèse d'architecture (l'autonomie encadrée). Recadré en illustration.
                                   (h) SURQUALIFICATION JURIDIQUE — « opposable » (ouverture) et « exigible par un
                                       tiers » (§11.2) : F-27 porte des demandes, ni recours ni régime de sanction ;
                                       PRD §3 exclut le conseil juridique. Ramenés à « faire valoir par une demande ».
                                   (i) EN-TÊTE — F-15 mobilisé par la note [^9] (distinction humain-dans-la-boucle /
                                       révision humaine, qui porte tout le §11.3) mais absent du recensement du socle.
                                   Volumétrie après correction : ~2955 mots (méthode des relecteurs : corps de prose,
                                   hors en-tête, titres, thèse, encadré et notes ; leurs relevés : 2989 et 2949) —
                                   dans la tolérance ±10 % de 3000. Méthode maximale (titres + thèse + encadré
                                   inclus) : ~3400 — l'écart tient à l'encadré de lacune, contenu exigé par CA-6.
                                   Aucun constat écarté ; aucun remplissage ajouté.
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     6. Passe F-09 (16 juill. 2026) . 1 correction : note [^3] remarquée « niveau [A] » → « entrée [A/B mixte] »,
                                   avec précision que ce chapitre ne mobilise que la strate [A] (dates, portée,
                                   définition, couverture agentique inférée) et aucune exigence opératoire.
                                   Sans objet ici : « exigé par E-23 »/« E-23 impose » (0 occurrence — le
                                   chapitre ne parle d'E-23 qu'en renvoi de calendrier), « fiche(s) de modèle(s) »
                                   (0 occurrence), affirmation périmée sur l'absence d'extraction d'E-23 (aucune ;
                                   l'encadré §11.3 porte sur le texte de l'AMF et les positions de la CAI —
                                   lacunes toujours ouvertes, non touchées par l'extraction d'E-23).
     7. Passe de conformité (17 juill. 2026, suites de l'audit) — périmètre strictement correctif, aucune information
                                   nouvelle, date de gel INCHANGÉE (16 juillet 2026) :
                                   - [M-09] Glose anglaise du §11.2 retirée + bloc CA-5 de l'étape 2 rectifié et daté
                                     (voir 2. ci-dessus). C'est le constat le plus lourd du chapitre : une attestation
                                     de conformité s'était appuyée sur un contenu non tracé.
                                   - [m-18] §11.2 : guillemets ôtés de « toute entreprise » (F-27 le rapporte hors
                                     guillemets — paraphrase de socle), et déclaration de verbatim de la note [^5]
                                     bornée en conséquence. Les TROIS citations de l'art. 12.1 (déclencheur, raisons
                                     et facteurs, révision par un membre du personnel) sont verbatim conformes à
                                     F-27 : NON touchées, vérifiées une à une contre PRD §7.3.
                                   - [m-19] Encadré §11.3 converti du gabarit cas 1 au gabarit cas 2 (PRDPlan §4.4),
                                     aligné sur le ch. 13, qui emploie le cas 2 pour la MÊME lacune (§10.4) : titre
                                     « État de la recherche », « aucune passe de recherche dédiée n'a été conduite »,
                                     source à retrouver. Les questions 2 et 3, déjà rédigées en termes de lacune non
                                     instruite, portent désormais le bon titre. Substance inchangée.
                                   - [m-20] Attestations de forme rectifiées : note [^3] et étape 3. ci-dessus.
                                   POINT SIGNALÉ PAR LA PASSE, PUIS CORRIGÉ LE 17 JUILLET 2026 (hors constats de
                                   l'audit ; relevé par la passe corrective, non par l'audit) : la note [^3] déclarait
                                   « les faits mobilisés ici relèvent tous de la strate [A] », alors que le §11.2 mobilise
                                   la VÉRIFICATION NÉGATIVE (« E-23 ne nomme ni l'agentique ni les agents »), que le PRD
                                   range sous [B] — l'énumération [A] étant close. Même classe que M-06 (ch. 9) et m-21
                                   (ch. 12). La note [^3] porte désormais « Un fait mobilisé ici en strate [B] ». ⚠ Ce
                                   bloc a lui-même attesté « NON CORRIGÉ » un point corrigé dans la prose — la faute
                                   cardinale du projet, reproduite dans le journal de la passe qui la corrigeait ; relevé
                                   par la relecture adversariale du 17 juillet et réconcilié ici.
-->
