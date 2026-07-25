# Chapitre 6 — L'autonomie encadrée : le paradigme APM

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-36 (socle principal — apports 1 à 5, défis C1 à C4) ; F-37 et F-43 (renvois) |
| Garde-fous à surveiller (PRD §8) | **R-1** — le manifeste cite l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI) parmi les protocoles d'interopérabilité ; **R-8** — sigle « ACP » jamais employé seul (désambiguïsation posée au ch. 1 §1.2, rappelée ici sans duplication) ; confiance F-36 « haute **pour l'attribution** » : le manifeste est cité comme position argumentée de ses auteurs, non comme fait établi |
| Volumétrie cible | ~3200 mots |

> **Thèse ([TOC.md](../../TOC.md))** : L'autonomie n'est pas l'automatisation ; elle se gouverne par des frames normatifs et opérationnels et quatre capacités (encadrement, explicabilité, actionnabilité conversationnelle, auto-modification).

---

Le chapitre précédent a fourni une carte : quatre options d'orchestration, cinq propriétés pour les évaluer, sept critères pour choisir. Une carte ne dit pas pourquoi le terrain a la forme qu'il a. Ce chapitre s'attache à la question que la taxonomie laisse ouverte : qu'est-ce, au juste, qu'encadrer un agent — et pourquoi l'encadrement, plutôt que la supervision, l'audit ou la restriction des droits, est-il présenté comme le mécanisme *premier* de gouvernance des systèmes agentiques ?

La réponse examinée ici vient d'un texte précis : le manifeste de recherche sur l'*Agentic Business Process Management* (APM), signé par dix-huit auteurs issus du monde universitaire et de l'industrie — dont IBM Research, SAP et l'Université d'Ottawa —, né du séminaire Dagstuhl #25192 et publié dans la revue *Information Systems*[^1]. Il faut dire immédiatement ce qu'un tel document est et ce qu'il n'est pas. Un manifeste de recherche n'établit pas des faits : il propose un vocabulaire, une architecture conceptuelle et un programme de travail. Le socle du présent ouvrage en tient compte et lui attribue une confiance haute **pour l'attribution** — c'est-à-dire que ce que ce chapitre affirme avec certitude, c'est que ces auteurs soutiennent ces thèses, avec ces arguments. La valeur du manifeste pour une institution financière canadienne ne tient donc pas à une autorité normative qu'il n'a pas, mais à ceci : il nomme, avec une précision que la littérature de fournisseurs n'atteint pas, les objets qu'un dossier de gouvernance devra de toute façon décrire.

## 6.1 Le système APM et la ligne de partage entre autonomie et automatisation

Le manifeste définit un **système APM** (*Agentic Business Process Management*) comme un système sociotechnique composé d'agents au moins partiellement conscients du processus[^1]. Chacun des trois éléments de cette définition mérite d'être pesé. **Lecture de l'auteur** : le socle donne la définition, il n'en commente pas les termes ; la glose qui suit est celle du présent ouvrage.

« Sociotechnique » situe dans le système les humains qui y participent — celui qui approuve, celui qui conteste, celui qui répond du résultat — au même titre que les composants automatisés : la lecture purement logicielle manque l'objet. Le pluriel d'« agents » signale que ce qui intéresse le manifeste est la pluralité et ce qu'elle produit. Et « au moins partiellement conscients du processus » est la clause la plus lourde de conséquences : elle admet dans le périmètre les systèmes dont les agents n'ont qu'une vue fragmentaire de la chaîne à laquelle ils contribuent — soit le cas normal en entreprise, l'agent qui exécute correctement sa tâche sans rien savoir de ce qui la précède ni de ce qui en dépend. Ce que le présent ouvrage en tire, et que le socle n'énonce pas : ce cas fragmentaire n'est pas une déviation à corriger, mais la situation de référence à gouverner.

De cette définition découle la distinction fondatrice du manifeste : **l'autonomie n'est pas l'automatisation**[^1]. Automatiser, c'est fixer le comportement : l'ingénieur décide à l'avance de la suite des opérations, et la machine l'exécute. Rendre autonome, c'est déléguer la décision : l'ingénieur ne fixe plus la suite des opérations, il fixe ce qui borne le choix de l'agent. La différence n'est pas de degré, elle est de nature. **Lecture de l'auteur** : c'est cette ligne que le vocabulaire courant de l'« automatisation intelligente » efface. Le manifeste établit la distinction ; il ne se prononce pas sur ce terme, et le socle ne lui prête aucune critique du vocabulaire courant.

Pour une institution financière fédérale, l'effacement de cette ligne a une conséquence pratique immédiate qu'il faut nommer, même si le socle ne la porte pas. Un contrôle automatisé se documente par sa spécification : il fait ce qui est écrit, la preuve de conformité est la lecture du code et le rejeu du cas. Une décision autonome ne se documente pas ainsi, parce qu'il n'y a rien à lire qui la prédise. Ce que l'on peut documenter, en revanche, c'est ce qui la bornait. Le socle n'établit pas cette conséquence — il établit la distinction dont elle découle. Elle est la raison pour laquelle le reste de ce chapitre porte sur les bornes, et non sur les décisions.

## 6.2 Frames normatifs, frames opérationnels, trois scénarios

Le mécanisme que le manifeste érige en gouvernance première porte le nom qui donne son titre au présent ouvrage : l'**autonomie encadrée** (*framed autonomy*)[^2]. L'agent y dispose d'une latitude de décision réelle, mais bornée par un cadre (*frame*) explicite. L'apport décisif du manifeste est la distinction qu'il opère entre deux natures de cadres.

Le **frame normatif** (*normative frame*) est de nature déontique : il énonce des obligations, des permissions et des interdictions[^2]. Il dit ce qui doit être fait, ce qui peut l'être et ce qui ne le doit pas. Le manifeste le donne pour **distinct du frame opérationnel** (*operational frame*) — et c'est tout ce que le socle en rapporte : la distinction des deux natures est établie, la seconde n'est pas caractérisée[^2]. **Lecture de l'auteur** : la distinction n'a de sens que si le frame opérationnel est d'une autre nature que déontique. Le premier relève alors du devoir-être, le second du pouvoir-faire. Cette glose est celle du présent ouvrage ; le manifeste sépare les deux cadres sans que le socle dise ce que le second contient.

**Lecture de l'auteur** — ce paragraphe entier développe ce que la distinction coûte quand on la manque ; le socle la pose, il ne l'exploite pas. Elle paraît scolastique tant qu'on ne mesure pas ce que sa confusion coûte. Un frame normatif sans frame opérationnel correspondant énonce une règle que rien n'empêche de violer : c'est la politique interne que l'agent ignore parce qu'aucun mécanisme ne la lui impose. Un frame opérationnel sans frame normatif correspondant restreint l'agent sans dire au nom de quoi : c'est le contrôle technique dont personne ne sait, deux ans plus tard, quelle exigence il servait — et que le premier gain d'efficacité fera sauter. Les deux frames ne sont donc pas deux couches d'un même dispositif mais deux objets qui doivent se répondre, et le travail de gouvernance consiste précisément à tenir la correspondance entre eux. Le manifeste établit la distinction ; il ne prescrit pas cette lecture de la traçabilité entre les deux, qui est celle du présent ouvrage et que la Partie III reprend pour son propre compte.

Le manifeste ne s'arrête pas à la typologie : il énumère **trois scénarios types** d'encadrement, qui se distinguent par le nombre de décideurs et par le niveau auquel le cadre s'applique[^2]. Le premier réunit un **décideur unique et un frame de processus** : une seule instance décide, dans un cadre défini au niveau du processus entier. Le deuxième réunit **plusieurs décideurs, chacun sous son frame individuel** : la latitude est distribuée, et chaque agent porte ses propres bornes. Le troisième réunit **plusieurs décideurs sous un ou plusieurs frames de processus** : la latitude reste distribuée, mais les bornes sont posées au niveau du processus plutôt qu'à celui des agents.

Le premier scénario est celui que l'on croit connaître, et c'est pourquoi il faut s'y arrêter. Un décideur unique sous un frame de processus : la latitude est concentrée, les bornes sont posées au niveau de la chaîne entière. **Lecture de l'auteur** : on serait tenté d'y voir le cas simple dont les deux autres seraient des complications, et d'y reconnaître l'assistant encadré par une procédure. Ce serait confondre décideur unique et agent unique. Le socle ne dit rien du nombre d'agents dans ce scénario ; ce qui s'y concentre, c'est la latitude de décision, non l'exécution — rien n'interdit qu'un décideur unique borne une chaîne que plusieurs agents parcourent. Dès les deux scénarios suivants, c'est la pluralité des décideurs elle-même qui devient l'objet du problème.

L'intérêt de cette énumération, pour l'architecte, est qu'elle rend visible un arbitrage que le vocabulaire des plateformes masque. **Lecture de l'auteur** : le deuxième scénario et le troisième décrivent tous deux un système multi-agents, mais l'objet sur lequel une garantie peut être offerte n'y est pas le même — chaque agent pris isolément d'un côté, le processus de l'autre. Sous frames individuels, rien dans le cadre ne s'énonce sur ce que la composition des agents produira ; sous frame de processus, c'est au cadre, non aux agents, qu'il revient de tenir la promesse. Le manifeste énumère les scénarios ; il ne formule pas cet arbitrage, et n'énonce pour aucun des trois ce sur quoi une garantie porterait. Le chapitre 5 nomme un arbitrage voisin dans le vocabulaire des options d'orchestration : les deux cadres sont **distincts**, et le socle n'établit entre eux **aucune filiation** — il ne les tient pas pour autant pour indépendants, une autrice de F-37 cosignant F-36. C'est leur convergence qui est établie, et elle vaut comme faisceau, non comme corroboration indépendante (chapitre 13)[^7]. Ce que ce chapitre retient, et qu'il porte comme sa propre proposition, c'est que le choix entre encadrer les agents et encadrer le processus est un choix de *l'objet sur lequel une garantie peut être offerte* — et que ce choix précède, logiquement, toute discussion de plateforme.

## 6.3 Les quatre capacités requises

Un système APM, soutient le manifeste, requiert quatre capacités[^3]. Elles ne sont pas présentées comme un catalogue de fonctionnalités souhaitables, mais comme les conditions sans lesquelles l'autonomie encadrée reste une intention.

La première est l'**encadrement** lui-même : la capacité de poser les frames, de les rendre effectifs, et de les faire porter par le système plutôt que par la bonne volonté de ses composants. C'est l'objet des deux sections précédentes.

La deuxième est l'**explicabilité**, et c'est celle qui intéresse le plus directement le lecteur de cet ouvrage. Le manifeste ne la traite pas comme une propriété désirable de l'ingénierie : il la relie **explicitement à la conformité réglementaire**, en nommant le RGPD et l'AI Act européen, et en désignant **la finance comme domaine à haut risque**[^3]. Il faut noter la portée exacte de ce fait. Les instruments que le manifeste nomme sont européens ; le socle du présent ouvrage n'établit aucun lien entre ce texte et les instruments canadiens — ni la ligne directrice E-23 du Bureau du surintendant des institutions financières, ni la ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers, ni l'article 12.1 de la Loi 25. Ces rapprochements sont l'objet de la Partie III, qui les établit à partir des textes canadiens eux-mêmes et non par transposition. Ce que le manifeste établit, et qui suffit ici : l'explicabilité est posée par ses auteurs comme une exigence de conformité, dans un secteur qu'ils qualifient de haut risque, et non comme un raffinement d'ingénierie que l'on ajoute si le temps le permet.

La troisième est l'**actionnabilité conversationnelle**, que le manifeste inscrit au rang des quatre capacités requises[^3]. Elle appelle un encadré plutôt qu'un développement.

> **État de la connaissance vérifiable** — que recouvre l'actionnabilité conversationnelle, et à quoi reconnaît-on qu'un système la possède ? Vérification menée le 16 juillet 2026 : le socle (F-36) nomme la capacité et la range parmi les quatre requises, mais n'en rapporte ni caractérisation, ni terme anglais, ni critère de satisfaction ; aucune autre entrée du socle ne la traite. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici.

Cet ouvrage s'en tient donc à ce qu'il peut établir — que ces auteurs la tiennent pour requise — et ne construit sur elle aucune exigence d'architecture. Une capacité que l'on ne sait pas caractériser ne peut pas devenir un point de contrôle.

La quatrième est l'**auto-modification**, et le manifeste la scinde en deux régimes qu'il importe de ne jamais confondre[^3]. L'**adaptation** est éphémère : elle porte sur une instance d'exécution, et ne survit pas à elle. L'**évolution** est persistante : elle modifie le modèle de processus lui-même, et vaut donc pour toutes les instances à venir. La formulation est symétrique ; les enjeux ne le sont pas. Une adaptation dévie d'un cas ; une évolution déplace la règle.

**Lecture de l'auteur** : cette dernière distinction est probablement le legs le plus opérationnel du manifeste pour un responsable de la gouvernance de modèles, et il vaut la peine de dire pourquoi le socle ne le porte pas. Le manifeste distingue les deux régimes ; il n'énonce pas qu'ils doivent relever de deux régimes d'autorisation distincts. C'est pourtant ce que le présent ouvrage soutiendra : un système qui traite l'adaptation et l'évolution par le même chemin technique rend indétectable, dans ses journaux, le moment où une exception est devenue une règle. La proposition est une inférence, non un fait du socle, et elle sera confrontée aux exigences canadiennes en Partie III.

## 6.4 Les frames locaux comme frontière de sécurité

Le manifeste ajoute un argument que l'on n'attendait pas d'un texte de gestion des processus, et qui déplace l'encadrement du terrain de la conformité vers celui de la sécurité : l'opérationnalisation **locale** des frames constitue une **frontière de sécurité et de confidentialité**[^4]. Restreindre le contexte et les capacités de chaque agent limite l'impact d'un agent compromis.

L'argument est d'une simplicité désarmante et sa portée est considérable. Le frame n'était jusqu'ici qu'un instrument de gouvernance — il dit ce que l'agent a le droit de faire. Posé localement, il devient aussi un instrument de confinement : ce que l'agent ne peut pas faire, un attaquant qui en prend le contrôle ne le peut pas davantage. L'encadrement cesse d'être un coût que l'on consent à la conformité pour devenir une mesure dont la valeur se lit en réduction de surface d'attaque. **Lecture de l'auteur** : le même mécanisme sert ainsi deux dossiers que l'organisation des institutions sépare généralement en deux directions distinctes.

Cette lecture n'est pas une extrapolation optimiste du manifeste, car celui-ci ne dissimule pas le revers. Parmi ses défis transversaux, il inscrit la **sécurité holistique** (défi C2), qui recense l'**injection d'invites** (*prompt injection*), l'**empoisonnement de mémoire** (*memory poisoning*), les patrons *Action-Selector* et *Plan-Then-Execute*, et — ce qui touche directement la section précédente — un **« paradoxe de confidentialité » de l'explicabilité**[^5]. Le chapitre 4 traite la taxonomie des risques protocolaires et développe ce défi ; on se contentera ici de nommer la tension qu'il fait peser sur l'édifice de ce chapitre. L'explicabilité exigée par la deuxième capacité suppose d'exposer ce que l'agent a vu et retenu ; la confidentialité, comme le confinement de la quatrième section, suppose de restreindre l'exposition. Les deux capacités que le manifeste tient pour requises tirent, sur ce point, en sens contraire.

**Lecture de l'auteur** : le manifeste nomme ce paradoxe, il ne le résout pas — et le présent ouvrage ne prétendra pas le faire non plus. Il faut le dire nettement, parce que la tentation inverse est forte : rien, dans le socle de cet ouvrage, n'établit qu'un système puisse être simultanément aussi explicable qu'une exigence de conformité l'imposerait et aussi cloisonné qu'une exigence de sécurité le voudrait. C'est un arbitrage, et un arbitrage se documente ; il ne se déclare pas résolu.

## 6.5 L'écart de responsabilité, ou qui répond de ce que personne n'a décidé

Reste le défi que ce chapitre prépare sans le traiter. Le manifeste inscrit parmi ses défis transversaux l'**écart de responsabilité** (*responsibility gap*, défi C4) : l'indétermination de l'imputabilité juridique entre le développeur, l'organisation qui impose le frame, le fournisseur du modèle et le comportement émergent du système multi-agents[^6].

L'énumération est plus intéressante que la formule. Elle nomme quatre porteurs candidats, et l'on remarquera que le deuxième terme du manifeste — l'organisation qui impose le frame — est précisément l'institution financière. Non pas celle qui écrit le code, non pas celle qui entraîne le modèle : celle qui pose les bornes. Le manifeste ne dit pas que la responsabilité lui échoit ; il la nomme comme l'un des quatre candidats entre lesquels l'imputabilité reste juridiquement indéterminée. Et le quatrième candidat n'est pas une organisation du tout : c'est un comportement — celui qui émerge de la composition d'agents dont aucun, pris isolément, n'a produit le résultat.

Ce quatrième terme mérite qu'on s'y arrête, car il est d'une autre espèce que les trois premiers. Développeur, organisation, fournisseur de modèle : ce sont des personnes, morales ou physiques, que l'on peut assigner, interroger, condamner. Le comportement émergent n'est rien de tel. En le plaçant sur la même liste, le manifeste ne suggère pas qu'un comportement puisse répondre de lui-même. **Lecture de l'auteur** : ce quatrième terme signale que l'imputabilité, dans un système multi-agents, bute sur des résultats dont aucun des trois porteurs identifiables n'est l'auteur au sens ordinaire. L'écart que le manifeste nomme n'est alors pas un partage difficile entre trois responsables : c'est l'existence, entre eux, d'une zone dont le socle atteste seulement qu'elle est juridiquement indéterminée.

C'est ici, exactement, que le paradigme de l'autonomie encadrée cesse d'être une préférence d'architecture pour devenir une question d'imputabilité. **Lecture de l'auteur** : si le frame est ce qui borne la décision, celui qui pose le frame est le seul acteur du système dont on puisse dire ce qu'il a effectivement décidé. Le socle n'établit pas cette conséquence — il atteste l'indétermination dont elle prétend sortir, et cette proposition est celle du présent ouvrage, non du manifeste. Le chapitre 13 — le pivot de cet ouvrage — la reprend comme telle, la confronte aux exigences canadiennes et en tire les conséquences d'architecture. Ce chapitre-ci se borne à poser la pièce sur l'échiquier.

Deux autres défis transversaux du manifeste méritent d'être signalés, ne serait-ce que pour que le lecteur sache que l'inventaire est complet : la **migration du BPM patrimonial** (défi C1) et la **contamination des jeux d'évaluation** (défi C3)[^7]. Le premier rappelle qu'aucune institution ne part d'une page blanche ; le second, que les mesures par lesquelles on juge ces systèmes sont elles-mêmes suspectes. Le socle ne les développe pas davantage, et cet ouvrage ne les développera donc pas.

Un dernier point de rédaction, qui vaut avertissement au lecteur. Le manifeste cite, parmi les protocoles d'interopérabilité, MCP et l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI) — dont le chapitre 1 a établi qu'il a fusionné dans A2A le 29 août 2025 et que son développement actif a cessé[^8]. Cette mention ne peut donc pas être reprise telle quelle comme état des lieux protocolaire. Elle ne diminue en rien la valeur du cadre conceptuel du manifeste : elle rappelle seulement qu'un texte de recherche fixe l'état d'un domaine à la date de sa rédaction, et que ce domaine-ci se périme par trimestres. Le sigle « ACP » n'est employé dans cet ouvrage qu'avec son qualificatif complet ; la désambiguïsation de ses quatre emplois est posée au chapitre 1 §1.2 et n'est pas répétée ici.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis pour la suite. **Premièrement**, l'autonomie et l'automatisation sont deux régimes distincts : le second fixe le comportement, le premier délègue la décision et n'en fixe que les bornes. Ce qui se documente, dans un système autonome, ce sont les bornes. **Deuxièmement**, ces bornes sont de deux natures que le manifeste sépare : le frame normatif, dont il précise la nature déontique, et le frame opérationnel, qu'il en distingue sans que le socle le caractérise. Le présent ouvrage lit le second comme le registre du pouvoir-faire et soutient — c'est sa proposition, non celle du manifeste — que l'un sans l'autre ne gouverne rien. **Troisièmement**, l'encadrement local n'est pas seulement un instrument de conformité : le manifeste en fait une frontière de sécurité et de confidentialité, ce qui adosse au même mécanisme deux dossiers que le présent ouvrage tient — c'est sa lecture — pour habituellement séparés dans l'organisation des institutions.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas que le manifeste APM soit une norme : c'est un texte de recherche, et ce chapitre en rapporte les thèses en les attribuant à leurs auteurs, sans jamais les présenter comme des faits établis du domaine. Il ne dit pas que ses recommandations soient validées empiriquement — le chapitre 5 examine les seules données expérimentales dont le socle dispose, et elles proviennent d'un autre travail, avec ses propres réserves[^7]. Il ne dit pas que l'explicabilité et le confinement soient conciliables : le manifeste nomme le paradoxe, personne ici ne le résout. Il ne dit rien, enfin, du droit canadien : aucun lien entre ce texte et E-23, la ligne directrice de l'AMF ou l'article 12.1 n'est établi par le socle, et les Parties III et VI les construiront à partir des textes canadiens.

Le manifeste fournit le vocabulaire de l'encadrement. Il ne fournit pas les frames — ceux-ci se déduisent des exigences, et les exigences sont l'objet de la Partie III.

---

## Notes

[^1]: PRD §7.7, **F-36** (niveau **[B]** — article lu intégralement ; confiance « haute **pour l'attribution** » : le manifeste est cité comme position argumentée de ses auteurs, non comme fait établi). Source primaire : Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al. (18 auteurs — universités et industrie dont IBM Research, SAP, Université d'Ottawa), « Agentic Business Process Management: A Research Manifesto », issu du séminaire Dagstuhl #25192 ; version journal *Information Systems* 140, 102738 (2026) — **version à privilégier en citation** (PRD §9.1) ; version arXiv:2603.18916v3 (12 avril 2026). Apport (1) du socle : définition du **système APM** (système sociotechnique d'agents au moins partiellement conscients du processus) et distinction **autonomie ≠ automatisation**. Formes terminologiques : `monographie/90-annexes/annexe-d-glossaire.md` §D.2.

[^2]: PRD §7.7, **F-36**, apport (2) : l'**autonomie encadrée** (*framed autonomy*) comme mécanisme premier de gouvernance ; *frames* **normatifs** (obligations, permissions, interdictions déontiques) distincts des *frames* **opérationnels** ; trois scénarios types — décideur unique + frame de processus ; décideurs multiples + frames individuels ; décideurs multiples + frame(s) de processus. Source primaire : *ibid.*

[^3]: PRD §7.7, **F-36**, apport (3) : quatre capacités requises — encadrement, **explicabilité** (liée explicitement par les auteurs à la conformité réglementaire — RGPD, AI Act européen — et à la finance comme domaine à haut risque), actionnabilité conversationnelle, auto-modification (**adaptation** éphémère d'instance vs **évolution** persistante du modèle). Source primaire : *ibid.* Les instruments nommés par le manifeste sont **européens** ; le socle n'établit aucun lien avec les instruments canadiens (E-23, ligne directrice IA de l'AMF, art. 12.1 de la Loi 25) — voir Partie III.

[^4]: PRD §7.7, **F-36**, apport (4) : l'opérationnalisation **locale** des frames comme **frontière de sécurité et de confidentialité** — restreindre le contexte et les capacités de chaque agent limite l'impact d'un agent compromis. Source primaire : *ibid.*

[^5]: PRD §7.7, **F-36**, défi transversal **C2** (sécurité holistique) : injection d'invites (*prompt injection*), empoisonnement de mémoire (*memory poisoning*), « paradoxe de confidentialité » de l'explicabilité, patrons *Action-Selector* et *Plan-Then-Execute*. Source primaire : *ibid.* Développement : **ch. 4** (taxonomie des risques protocolaires), auquel TOC.md assigne ce défi.

[^6]: PRD §7.7, **F-36**, défi transversal **C4** : l'**écart de responsabilité** (*responsibility gap*) — indétermination de l'imputabilité juridique entre développeur, organisation qui impose le frame, fournisseur de modèle et comportement émergent du système multi-agents. Source primaire : *ibid.* Exploitation : **ch. 13** (pivot de l'ouvrage), par assignation de TOC.md.

[^7]: PRD §7.7, **F-36**, défis transversaux **C1** (migration du BPM patrimonial) et **C3** (contamination des jeux d'évaluation). Source primaire : *ibid.* — Sur les renvois au ch. 5 : PRD §7.7, **F-37** (Rinderle-Ma, Mangler et al., arXiv:2606.31518v1, 30 juin 2026), **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité — le cadre conceptuel (taxonomie OO1–OO4) est repris ici par simple renvoi, les résultats chiffrés relevant du ch. 5 et n'étant cités qu'à titre d'illustration. **Sur le statut des deux sources** : PRD §7.8, **F-46** — l'adjectif « indépendantes » est retiré du socle depuis le correctif de la v1.5, « réfuté par le socle lui-même » ; **Rinderle-Ma cosigne F-36 et F-37** (§7.7). La formulation imposée par F-46 réserve la convergence à un faisceau (« deux partagent une autrice et deux une organisation »), jamais à une corroboration par sources indépendantes.

[^8]: PRD §8.1, garde-fous **R-1** (l'ACP protocolaire — *Agent Communication Protocol*, IBM Research/BeeAI — a fusionné dans A2A le 29 août 2025 ; son développement actif a cessé — ne jamais le présenter comme standard vivant) et **R-8** (le sigle « ACP » employé seul est proscrit dans tout l'ouvrage ; chaque emploi porte son qualificatif complet). La mention de l'ACP protocolaire par le manifeste est signalée par la réserve de **F-36** (PRD §7.7) et ne doit pas être reprise telle quelle. Généalogie : **F-43** (PRD §7.8) ; désambiguïsation des quatre emplois : **ch. 1 §1.2** et `monographie/90-annexes/annexe-d-glossaire.md` §D.1.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps = 3387 mots mesurés au 17 juillet 2026
                                   — 3358 après relecture, + 29 mots par la passe de conformité du 17 juillet
                                   (M-05, point 6 ci-dessous) ; cible 3200 ±10 %
                                   soit 2880-3520 : conforme ; décompte reproductible :
                                   awk '/^> \*\*Thèse/{f=1;next} /^## Notes/{f=0} f' <fichier> | wc -w
                                   — en-tête/exergue/notes/commentaires exclus. Le décompte de 3174 annoncé au
                                   premier jet était FAUX : les deux relecteurs mesurent 3113 sur le même texte,
                                   valeur que la commande ci-dessus reproduit (3113 + 245 mots ajoutés par les
                                   corrections = 3358). Même défaut au ch. 1 — voir gouvernance.)
     2. Traçabilité (CA-1, CA-5) . fait (8 notes, toutes tracées F-36 sauf renvois F-37/F-43 et garde-fous ;
                                   termes anglais entre parenthèses et en italique à la 1re occurrence :
                                   framed autonomy, normative/operational frame, prompt injection, memory poisoning,
                                   responsibility gap, APM ; « actionnabilité conversationnelle » : aucun terme anglais
                                   au socle — non inventé)
     3. Balayage garde-fous ...... fait (R-1 et R-8 : sigle ACP toujours qualifié « le protocole ACP [d'IBM Research] »,
                                   au passé, fusion dite ; encadré du ch. 1 rappelé, non dupliqué ; aucun emploi de
                                   « control plane » dans ce chapitre ; F-36 attribué à ses auteurs à chaque occurrence
                                   — confiance « haute pour l'attribution » ; aucune métrique auto-déclarée dans ce chapitre)
     4. Relecture adversariale ... fait (deux relecteurs indépendants, distincts du rédacteur — PRDPlan §4.2.4 ;
                                   8 constats bloquants + 11 réserves, TOUS fondés après vérification au socle,
                                   tous appliqués. Ce que la relecture a réfuté :
                                   a) ERREUR D'ORDINAL (§6.5) : « le troisième terme du manifeste — l'organisation
                                      qui impose le frame ». F-36/C4 énumère développeur (1), organisation qui
                                      impose le frame (2), fournisseur de modèle (3), comportement émergent (4).
                                      Le chapitre reproduisait l'ordre exact du socle en §6.5 al. 1 puis se
                                      contredisait à l'alinéa suivant, sur le terme même qu'il identifie à
                                      l'institution financière (pivot du ch. 13). Corrigé : « deuxième ».
                                   b) CARACTÉRISATION FABRIQUÉE (§6.2) : « le frame opérationnel est de nature
                                      exécutoire : il fixe ce que l'agent peut faire, dans quel ordre et avec
                                      quels outils[^2] ». Le socle ne caractérise QUE les frames normatifs
                                      (déontiques) et se borne à dire qu'ils sont « distincts des frames
                                      opérationnels ». La note [^2] ne portait pas l'affirmation qu'elle appuyait
                                      (CA-1). Le chapitre appliquait la discipline inverse à l'actionnabilité
                                      conversationnelle sans voir la lacune identique, et plus load-bearing, ici.
                                      Corrigé par l'option (b) du relecteur : s'en tenir au socle (distinction
                                      établie, seconde nature non caractérisée) et marquer la glose
                                      devoir-être/pouvoir-faire « Lecture de l'auteur ». Acquis 2 de la
                                      conclusion réécrit en conséquence. Option (a) — remonter la
                                      caractérisation au PRD §7.7 — écartée : hors mandat (PRD fait autorité).
                                   c) ATTRIBUTION INDUE (§6.1) : « insiste le manifeste » sur l'effacement de la
                                      distinction par le vocabulaire de l'« automatisation intelligente ». Rien
                                      au socle. Faute la plus grave possible ici : F-36 est de confiance « haute
                                      POUR L'ATTRIBUTION » — prêter aux auteurs une thèse supplémentaire vide la
                                      réserve de son sens, et le chapitre posait lui-même cette exigence en §6.0
                                      avant de l'enfreindre deux paragraphes plus loin. Attribution retirée.
                                   d) CONFUSION DÉCIDEUR/AGENT (§6.2) : « il n'y a rien à composer » dans le
                                      scénario 1 contredisait le §6.1 du même chapitre (le pluriel d'« agents »).
                                      Un décideur unique n'est pas un agent unique ; le socle ne dit rien du
                                      nombre d'agents dans ce scénario. Phrase et « figure familière de
                                      l'assistant » supprimées, distinction explicitée.
                                   e) INFÉRENCES NON MARQUÉES (§6.1 exégèse de la définition ; §6.2 objet des
                                      garanties ; §6.4 « dans la plupart des institutions » ; §6.5 intention du
                                      manifeste et proposition-pivot « celui qui pose le frame est le seul acteur
                                      dont on puisse dire ce qu'il a décidé »). Le chapitre marquait
                                      scrupuleusement « Lecture de l'auteur » pour des inférences MOINS
                                      engageantes et omettait le marqueur sur les plus lourdes — dont celle que
                                      le ch. 13 doit reprendre, qui serait entrée en prémisse comme acquis du
                                      socle. Toutes marquées. La notion de « garantie » vient de F-37 (propriété
                                      d'assurance de correction), pas de F-36 : dit explicitement.
                                   f) SURINTERPRÉTATION DE CONVERGENCE (§6.2) : « le chapitre 5 nomme le MÊME
                                      arbitrage ; le manifeste en donne l'ASSISE CONCEPTUELLE ». Le socle ne pose
                                      aucune filiation F-36→F-37. Réduit à « arbitrage voisin ».
                                      ⚠ RECTIFIÉ LE 17 JUILLET 2026 (audit, constat M-05) — ce qui suivait ici
                                      portait la doctrine d'AVANT l'arbitrage F-46 v1.5 : « ce sont des sources
                                      INDÉPENDANTES, et c'est de leur indépendance que la convergence à trois
                                      sources tire sa valeur ». C'est cette ligne de contrôle qui a motivé la
                                      phrase fautive du §6.2 (« les deux cadres sont indépendants »). Doctrine
                                      actuelle — PRD §7.8, F-46, correctif de la v1.5 : l'adjectif
                                      « indépendantes » est RETIRÉ, « réfuté par le socle lui-même » ; deux
                                      recoupements documentés — Rinderle-Ma cosigne F-36 et F-37 ; IBM Research
                                      figure parmi les auteurs de F-36 et publie F-46. La convergence est un
                                      faisceau réel, elle ne vaut PAS corroboration indépendante ; « trois sources
                                      indépendantes » est proscrit. Ce qui reste vrai du constat (f) : aucune
                                      filiation F-36→F-37 n'est établie — distinction et absence de filiation, non
                                      indépendance. §6.2 et note [^7] corrigés en conséquence le 17 juillet 2026.
                                      Leçon : un bloc de contrôle qui porte une doctrine périmée re-fabrique la
                                      faute à la reprise suivante — il se rectifie avec le corps, et se date.
                                   g) AFFIRMATIONS EN INCISE (§6.2) : « elle est ancienne », « que la pratique
                                      confond » — sans trace ni marquage, la seconde reprise en clôture comme
                                      acquis. Supprimées ici et l. 83.
                                   h) FORME IMPOSÉE R-8/§D.1 : « le protocole ACP d'IBM Research » n'est pas la
                                      forme du glossaire ; « en août 2025 » perdait la date exacte du 29 août 2025
                                      que la note [^8] porte. Repris en « l'ACP protocolaire (*Agent Communication
                                      Protocol*, IBM Research/BeeAI) » à l'en-tête et en §6.5. Fond déjà conforme.
                                   i) FORME DE LACUNE (§6.3) : traitement au fond exemplaire mais en prose
                                      courante, alors que PRDPlan §4.4 impose l'encadré. Repris sous la forme
                                      « État de la connaissance vérifiable ». La caractérisation implicite qui
                                      ouvrait le paragraphe (« adressable par le langage — interrogeable et
                                      infléchissable en cours d'exécution ») n'était elle-même pas au socle :
                                      supprimée, ce que le relecteur n'avait pas relevé.
                                   j) DÉCOMPTE FAUX : 3174 déclarés, 3113 mesurés par les deux relecteurs.
                                      Corrigé, commande de décompte explicitée ci-dessus.
                                   Aucun constat écarté.)
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     6. Passe de conformité ...... fait (17 juillet 2026 — audit global, constat M-05 ; date de gel INCHANGÉE
                                   au 16 juillet 2026 : aucune information nouvelle n'entre, seul le socle de
                                   gouvernance déjà arbitré — F-46 v1.5 — est cascadé. Corps §6.2 : « les deux
                                   cadres sont indépendants » -> « distincts […] aucune filiation […] il ne les
                                   tient pas pour autant pour indépendants ». Note [^7] : traçabilité du
                                   correctif F-46 ajoutée. Bloc de relecture (f) ci-dessus : doctrine périmée
                                   rectifiée et datée — c'était la racine. Le ch. 5 (l. 87) affirmait déjà la
                                   formulation correcte : la Partie II ne se contredit plus.)

     Points signalés à la gouvernance (non corrigés ici — PRD/TOC/PRDPlan font autorité) :
     - F-36 porte la réserve « mention d'ACP antérieure à la fusion », mais les seules dates que l'entrée
       fournit (arXiv v3 du 12 avril 2026 ; version journal 2026) sont POSTÉRIEURES à la fusion du 29 août 2025
       (F-43). La date du séminaire Dagstuhl #25192 n'est pas au socle. L'antériorité est donc affirmée sans
       date à l'appui. Traité ici de façon neutre (la mention n'est pas reprise, quelle qu'en soit la date).
     - Défis C1 et C3 de F-36 : aucun chapitre porteur assigné par TOC.md (C2 -> ch. 4, C4 -> ch. 13).
       Nommés ici pour complétude de l'inventaire, non développés.
     - « Actionnabilité conversationnelle » : le socle n'en donne ni terme anglais ni définition — la capacité
       est nommée, non caractérisée. Traitée en §6.3 sous l'encadré imposé par PRDPlan §4.4. À PORTER AU
       PRD §10 : PRD §10 exige que chaque lacune restante devienne un encadré « état de la connaissance
       vérifiable » ou une question de recherche en Partie VI ; celle-ci n'y est pas listée — elle a été
       découverte à la rédaction. L'encadré est en place ; l'inscription en §10 reste à trancher.
     - LACUNE JUMELLE, non listée au PRD §10 et découverte par la relecture : le socle ne caractérise pas le
       **frame opérationnel** (F-36, apport (2) : « distincts des *frames* opérationnels », sans plus). Le
       chapitre s'en tient désormais à la distinction et marque sa glose « Lecture de l'auteur ». Deux options
       pour la gouvernance : (a) si l'article porte cette caractérisation — F-36 est [B], « article lu
       intégralement » —, amender F-36 en PRD §7.7, ce qui permettrait de citer plutôt que gloser, et
       renforcerait le ch. 13 ; (b) sinon, inscrire la lacune en PRD §10. Décision à prendre AVANT le ch. 13,
       qui reprend l'articulation des deux frames.
     - DÉCOMPTE DE MOTS non reproductible d'un chapitre à l'autre : ch. 6 déclarait 3174 pour 3113 réels ;
       ch. 1 déclare 2726 pour 2625 réels (contrôle de calibrage du relecteur). PRDPlan §4.2 ne fixe aucune
       commande de décompte. Proposition : y inscrire la commande utilisée ici. Le ch. 1 porte le même défaut
       et n'est pas corrigé ici (hors mandat).
-->
