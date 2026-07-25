# Chapitre 9 — E-23 : le risque de modèle à l'ère de l'IA

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-09, F-10 ; F-25 (renvoi — convergence de la date d'entrée en vigueur, ch. 11) ; F-27 (renvoi — art. 12.1, traitement complet au ch. 11) |
| Garde-fous à surveiller (PRD §8) | §8.2.4 (couverture agentique d'E-23 = inférence d'analystes, formulation verrouillée) ; §8.2.6 (la projection de ~70 % présentée comme projection de ses auteurs) ; motif R-7 filtré (contexte réglementaire pur — PRDPlan §4.3) |
| Volumétrie cible | ~3000 mots |

> **Thèse ([TOC.md](../../TOC.md))** : E-23 couvre l'IA agentique implicitement, par sa définition de « modèle » — couverture par inférence d'analystes, à traiter comme acquise d'ici le 1er mai 2027.

---

Il existe deux façons pour un régulateur d'atteindre une technologie : la nommer, ou la définir. La première est lisible, rassurante, et vieillit mal — le vocabulaire d'un secteur qui se réorganise par trimestres périme les textes qui s'y accrochent. La seconde est austère, elle déplace le travail d'interprétation vers l'assujetti, et elle survit aux modes. La ligne directrice E-23 du Bureau du surintendant des institutions financières a choisi la seconde. Ce chapitre soutient que ce choix a une conséquence pratique immédiate pour l'architecte : le périmètre de son programme de risque de modèle (*model risk*) n'est pas déterminé par ce que le BSIF a écrit sur l'IA agentique — il n'a rien écrit — mais par ce que sa définition de « modèle » attrape, et par ce que cinq analystes juridiques canadiens en concluent.

C'est une position inconfortable, et il faut la tenir sans la travestir. L'affirmation « E-23 couvre l'IA agentique » n'est pas un fait du BSIF ; c'est une lecture d'analystes. L'affirmation « une institution prudente doit s'y préparer comme si c'était acquis » est une recommandation d'architecture. Les deux sont défendables. Elles ne sont pas de même nature, et cet ouvrage ne les confondra pas.

## 9.1 Genèse et calendrier

Le socle de cet ouvrage établit deux dates et un périmètre, et il faut mesurer combien ils sont peu nombreux. La version finale d'E-23 a été **publiée le 11 septembre 2025**. Elle **entre en vigueur le 1er mai 2027**. Elle **s'applique à toutes les institutions financières fédérales**, y compris les succursales étrangères, dans la mesure compatible[^1].

Posons l'arithmétique du préavis, puisqu'elle décide des plans de mise en conformité. Du 11 septembre 2025 au 11 avril 2027, il s'écoule dix-neuf mois ; du 11 avril au 1er mai 2027, vingt jours de plus. Le BSIF a donc accordé **dix-neuf mois et vingt jours** entre la publication de son texte final et son opposabilité. Rapporté à la date de gel du présent chapitre — le 16 juillet 2026 —, le compte à rebours est plus serré : du 16 juillet 2026 au 16 avril 2027, neuf mois ; puis quinze jours jusqu'au 1er mai. Il reste **neuf mois et quinze jours**. Une institution qui lirait ce chapitre à sa date de gel disposerait donc d'un peu plus de trois trimestres pour inventorier, classer et encadrer ce qui, dans son parc, relève de la définition examinée à la section suivante.

La date du 1er mai 2027 n'est pas isolée : la ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers, dont traite le chapitre 11, porte la même date d'entrée en vigueur[^2]. Cette convergence entre le régulateur prudentiel fédéral et le régulateur intégré québécois est l'un des faits structurants de la Partie III ; le chapitre 11 en fait l'examen.

Sur la genèse proprement dite, en revanche, il faut être franc sur ce que le socle ne porte pas.

> **État de la connaissance vérifiable — la genèse d'E-23 avant le 11 septembre 2025**
>
> L'extraction du texte intégral et de sa lettre d'accompagnement, versée au socle le 16 juillet 2026, établit trois éléments d'antériorité, et trois seulement : un **projet de 2023** a existé ; il incluait les régimes de retraite fédéraux, **retirés du périmètre final** ; et le texte final répond à des **commentaires** qui demandaient de restreindre la définition de « modèle » (§9.2)[^1]. Un indice s'y ajoute : le rapport conjoint BSIF-ACFC du 24 septembre 2024 — examiné en §9.4 — renvoie **explicitement au cadre E-23**[^3]. Le socle ne porte rien de plus : ni le calendrier de la consultation, ni le contenu du projet de 2023, ni la nature des travaux dont il procède.
>
> Recherche menée le 16 juillet 2026 : l'extraction a porté sur le texte final et sa lettre, non sur les versions qui l'ont précédé — hors périmètre. En l'absence de source primaire sur celles-ci, la question reste ouverte ; aucune inférence n'est proposée ici. Le présent chapitre traite donc du **calendrier** d'E-23 bien plus que de sa genèse — un écart avec le titre que [TOC.md](../../TOC.md) donne à cette section, signalé à la gouvernance plutôt que comblé par du non-vérifié.

Un mot, enfin, sur le périmètre d'assujettissement. **Lecture de l'auteur** : que le texte s'applique aux institutions financières *fédérales* signifie, par simple lecture de sa portée, qu'il ne s'applique pas aux institutions relevant d'une supervision provinciale — lesquelles ne sont pas pour autant sans obligations en matière d'IA, comme le chapitre 11 l'établit pour le Québec. Le socle documente une portée ; il ne documente pas les modalités selon lesquelles le BSIF entend l'appliquer, et la réserve de compatibilité qui accompagne les succursales étrangères[^1] n'est pas explicitée par les sources retenues ici. Une institution qui bâtirait un argumentaire sur cette réserve devrait remonter au texte lui-même.

## 9.2 La définition de « modèle » et l'anticipation des systèmes autonomes

Tout, dans ce chapitre, tient à une définition.

Le socle en porte le libellé verbatim (§A.4), extrait le 16 juillet 2026 : « Application de techniques statistiques ou d'hypothèses théoriques, empiriques ou fondées sur un jugement, **notamment des méthodes d'IA et d'AA**, qui traite des données en entrée pour générer des résultats »[^1]. L'inclusion n'est ni une clause d'ouverture pour l'avenir, ni une note de bas de page : elle est au cœur du périmètre — et la lettre d'accompagnement établit que le BSIF a laissé la définition « **intentionally broad** » en réponse aux commentaires qui demandaient de la restreindre[^1]. **Lecture de l'auteur** : la construction définitionnelle atteint les systèmes d'apprentissage automatique en exploitation dans une institution financière fédérale ; ce que le programme de risque de modèle doit alors en faire relève des attentes opératoires exposées plus bas.

Le socle établit un second élément, plus significatif encore : **le BSIF anticipe des modèles à apprentissage et décision autonomes**[^1]. Il faut peser les deux termes. **Lecture de l'auteur** : on entend ici par *apprentissage* autonome le fait qu'un modèle modifie son comportement sans qu'un opérateur l'y reprogramme, et par *décision* autonome le fait qu'il ne se contente pas de produire une sortie que quelqu'un interprétera — il tranche. Cette lecture des deux termes n'est pas établie par le socle, qui n'en porte que l'énoncé. Sous cette réserve, le régulateur prudentiel canadien a, dans un texte publié en septembre 2025, envisagé des artefacts qui apprennent seuls et décident seuls.

**Lecture de l'auteur** : c'est ici que se joue la thèse du chapitre. Le socle n'établit pas que le BSIF désignait par là les systèmes multi-agents, ni qu'il avait à l'esprit l'architecture agentique telle que les Parties I et II de cet ouvrage la décrivent. Le rapprochement entre « décision autonome » au sens d'E-23 et l'autonomie des systèmes agentiques — sur laquelle le chapitre 6 revient en détail — est une **inférence d'auteur**, non un fait du texte. Elle est fondée, elle est partagée par les analystes examinés à la section suivante, et elle demeure une inférence.

**Lecture de l'auteur** : un périmètre construit sur une définition fonctionnelle — ce qu'un artefact *fait* — plutôt que sur une nomenclature — comment il *s'appelle* — a la propriété que l'architecte recherche dans ses propres interfaces : il ne se périme pas quand l'implémentation change de nom. Un texte qui aurait énuméré « réseaux de neurones, forêts aléatoires, modèles de langage » serait aujourd'hui à réviser. Un texte qui définit le modèle par sa fonction attrape ce qui n'existait pas quand il fut écrit. C'est, selon la lecture des analystes examinée en §9.3, le mécanisme par lequel E-23 rejoindrait l'agentique sans jamais en prononcer le nom — et c'est aussi ce qui rend l'exercice inconfortable, puisque l'assujetti doit qualifier lui-même ce qui entre dans le périmètre, sans liste à cocher.

Reste ce que la ligne directrice attend concrètement. Le socle en porte les attentes opératoires depuis l'extraction du 16 juillet 2026 — source primaire lue, sans vote adversarial, soit un niveau de preuve **inférieur** à celui des faits votés que ce chapitre mobilise : les dates, la portée et la définition de « modèle ». L'anticipation de la décision autonome exposée ci-dessus n'est pas de ces faits votés : l'énumération [A] de F-09 est close et ne la porte pas — elle relève donc, comme les attentes qui suivent, de la strate la moins éprouvée de l'entrée[^1]. E-23 attend un **cycle de vie** en cinq volets — conception, revue, déploiement, surveillance, mise hors service —, « **not necessarily sequential** » ; un **inventaire** des modèles au risque inhérent non négligeable, tenu à l'échelle de l'entreprise, « accurate, evergreen, and subject to robust controls », dont l'Appendice 1 fixe les champs minimaux ; une **cote de risque par modèle** (« each model should be assigned a model risk rating »), l'intensité du dispositif devant être « commensurate with » le risque ; des normes de **documentation de modèle** ; enfin une **surveillance continue** traitant les défis propres à l'IA et à l'AA — « **autonomous decision making, autonomous re-parametrization** » et un potentiel accru de dérive[^1].

Une précision de modalité les commande toutes : E-23 est **fondée sur des principes** — douze principes au conditionnel (« should »), jamais à l'impératif[^1]. Ces cinq domaines sont **attendus**, non exigés — et la qualification d'un parc se mène sur le texte officiel du BSIF (osfi-bsif.gc.ca), non sur ce chapitre.

## 9.3 L'inférence agentique

Nous arrivons au point le plus délicat de la Partie III. La formulation qui suit est imposée par la méthode de l'ouvrage, et rendue dans la substance qu'impose §8.2.4 :

> **E-23 ne nomme ni l'agentique ni les agents ; sa définition de « modèle » englobe les méthodes d'IA et d'apprentissage automatique, d'où une couverture implicite que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise**[^4].

Chaque membre en porte du poids. Reprenons-les.

**« E-23 ne nomme ni l'agentique ni les agents »** est un fait négatif vérifié : le texte n'emploie jamais les mots « agentique », « agents » ni « orchestration »[^1]. Ce n'est pas un oubli qu'on pourrait combler par une lecture bienveillante ; c'est une absence, et elle est établie. Toute phrase de la forme « le BSIF exige, pour l'IA agentique, que… » est fausse — non pas discutable, fausse — et cet ouvrage la proscrit[^4].

**« sa définition de "modèle" englobe les méthodes d'IA et d'apprentissage automatique »** est le fait positif qui rend la suite possible : c'est la voie définitionnelle de la section précédente[^1].

**« d'où une couverture implicite »** est la charnière — et c'est une conclusion, pas une observation.

**« que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise »** en désigne les auteurs, et c'est ici qu'il faut être le plus rigoureux. **Ce que le socle établit, c'est que ces cinq analystes tiennent la couverture pour acquise. Ce que le socle n'établit pas, c'est que la couverture existe.** L'objet vérifié est un état de l'opinion juridique canadienne, non un état du droit. La nuance paraîtra scolastique ; elle sépare pourtant une note de conformité défendable d'une erreur de droit.

Une précision de méthode, enfin. Dans l'économie des sources de cet ouvrage, les cabinets juridiques canadiens relèvent de la **corroboration secondaire** et ne peuvent jamais porter seuls un fait central[^5]. Leur convergence n'est donc pas invoquée ici comme preuve de la couverture : elle en est l'**objet même**. Le fait central avancé par ce chapitre est un fait sur les analystes, et il est sourcé comme tel.

Reste la seconde moitié de la thèse, celle que tout responsable de la conformité posera : que fait-on de cette inférence ?

**Lecture de l'auteur** : on la traite comme acquise, et l'on documente qu'on l'a fait par prudence plutôt que par obligation établie. Trois éléments convergent, dont aucun ne suffit isolément. D'abord, les cinq analystes juridiques nommés au socle aboutissent à la même lecture[^1] ; le socle n'établit pas l'indépendance de leurs analyses, et la convergence n'est de toute façon pas une preuve. Ensuite, la définition atteint, selon cette lecture, les systèmes considérés, par sa construction fonctionnelle même (§9.2). Enfin, et c'est le point le plus fort, le régulateur a lui-même anticipé la décision autonome[^1] : il n'est pas resté silencieux sur ce que ses assujettis allaient déployer, il a écrit qu'il l'attendait.

À quoi s'ajoute une asymétrie que l'architecte reconnaîtra comme un raisonnement de risque ordinaire — et qui reste, elle aussi, une **lecture de l'auteur** que le socle ne porte pas. Se tromper en tenant la couverture pour acquise coûte le prix d'une gouvernance surdimensionnée : un inventaire trop large, des contrôles appliqués à des systèmes qui n'en relevaient pas. Se tromper en la tenant pour inexistante coûte le prix d'un parc entier de systèmes décisionnels hors périmètre de contrôle au 1er mai 2027, découvert par un tiers. Les deux erreurs ne sont pas commensurables, et c'est cette asymétrie — non une attente du BSIF — qui fonde la recommandation.

Le chapitre 13 reprend cette conclusion pour en tirer ce qui intéresse l'architecture : la traduction des contraintes réglementaires en cadres d'exécution déterministes. Le chapitre 20 examine l'instrumentation candidate d'un tel programme. Le présent chapitre s'arrête au seuil : il établit le périmètre, pas la réponse.

## 9.4 Le rapport BSIF-ACFC : une trajectoire déclarée et une causalité indéterminable

Moins d'un an avant la publication de la version finale d'E-23 — le **24 septembre 2024**, onze mois et dix-huit jours plus tôt —, le BSIF et l'Agence de la consommation en matière financière du Canada publiaient un rapport conjoint dont le socle retient deux apports[^3]. Ils sont de nature très différente, et le second importe davantage.

Le premier est une trajectoire d'adoption. Selon ce rapport conjoint du BSIF et de l'ACFC, l'adoption de l'intelligence artificielle par les institutions financières fédérales serait passée d'environ **30 % en 2019** à environ **50 % en 2023**, et **le BSIF et l'ACFC projettent une adoption de ~70 % d'ici 2026 — une projection issue d'une enquête auto-déclarée, non un taux observé**[^6]. La formule est imposée par la méthode de l'ouvrage, et elle doit être reprise à chaque occurrence de ce chiffre.

Posons l'arithmétique, puisqu'elle est instructive. De 2019 à 2023, quatre ans, la progression déclarée est de vingt points — soit cinq points par an en moyenne. De 2023 à 2026, trois ans, la progression *projetée* est également de vingt points — soit environ six virgule sept points par an. Autrement dit, la projection du BSIF et de l'ACFC ne prolonge pas la tendance déclarée : elle l'accélère d'un tiers. C'est une observation arithmétique sur les chiffres du rapport, non un jugement sur sa méthode ; mais elle indique où porterait le doute d'un lecteur exigeant.

Ce lecteur remarquera aussitôt une seconde chose : les trois chiffres proviennent d'une **enquête auto-déclarée**, rapportée par le BSIF et l'ACFC dans leur rapport conjoint du 24 septembre 2024[^3] — ils mesurent donc ce que des institutions ont déclaré d'elles-mêmes, sans définition commune extraite au socle de ce qui compte comme « adoption de l'IA ». Le chapitre 1 formulait le même avertissement à propos des métriques d'adoption des protocoles ; il vaut ici sans changement.

> **État de la recherche — la projection de 2026 est-elle advenue ?**
>
> L'horizon de la projection du BSIF et de l'ACFC — l'année 2026 — est le présent de ce chapitre, dont la date de gel est le 16 juillet 2026. La question se pose donc naturellement : l'adoption d'environ 70 % projetée par le BSIF et l'ACFC[^6] s'est-elle matérialisée ?
>
> **Le socle de cet ouvrage ne documente aucune mesure postérieure à l'enquête auto-déclarée rapportée le 24 septembre 2024.** Aucune entrée ne porte de taux observé pour 2024, 2025 ou 2026. Lacune ouverte le 16 juillet 2026 ; **aucune passe de recherche n'a été conduite** sur les publications du BSIF postérieures à F-10 — hors périmètre de P0 ; le point est porté en lacune à la gouvernance. Source à retrouver : `osfi-bsif.gc.ca`, publications postérieures au 24 septembre 2024. La question reste ouverte ; aucune inférence n'est proposée ici, et notamment aucune extrapolation de la trajectoire déclarée. Une revalidation avant publication (PRD §8.3) devrait interroger les publications du BSIF postérieures à la date de gel.

Le second apport est d'une tout autre portée : il justifie la place de ce chapitre en tête de la Partie III. Le rapport conjoint du BSIF et de l'ACFC caractérise un **risque de modèle accru propre à l'IA**, et il le fait en deux temps : un très grand nombre de paramètres appris de façon autonome ; des **relations causales entre entrées et sorties souvent indéterminables**. Le rapport rattache explicitement ce constat au cadre E-23[^3].

Ce membre de phrase est le plus lourd de conséquences du chapitre. Que les relations causales entre entrées et sorties soient *souvent indéterminables* n'est pas une remarque sur la difficulté de l'explicabilité : c'est un constat, posé par le régulateur prudentiel canadien et par l'agence de protection des consommateurs de produits financiers, sur les limites de ce qu'on peut extraire du modèle lui-même.

**Lecture de l'auteur** : si l'on ne peut pas, en général, déterminer par quel chemin causal une entrée a produit une sortie, alors l'explication d'une décision ne peut pas être obtenue en interrogeant le modèle *a posteriori*. Elle doit être produite ailleurs — par l'architecture qui entoure le modèle, qui enregistre ce qui lui a été soumis, quelles bornes lui étaient imposées, quel chemin d'exécution a été suivi et quels contrôles se sont appliqués. Le socle établit le constat d'indéterminabilité ; il n'établit pas cette conséquence d'architecture, qui est une inférence. Mais c'est cette inférence qui fait le pont de la Partie III vers les Parties VI et VII, et le chapitre 13 en fait le pivot de l'ouvrage. Elle croise par ailleurs l'obligation d'explication de l'art. 12.1 de la Loi 25, dont le chapitre 11 examine le texte, la portée et les réserves d'interprétation[^7].

Notons enfin ce que la chronologie révèle. Le rapport du 24 septembre 2024 rattachait déjà le risque de modèle propre à l'IA au cadre E-23[^3] ; la version finale d'E-23, publiée moins d'un an plus tard, inclut explicitement les méthodes d'IA et d'apprentissage automatique dans sa définition de « modèle » et anticipe la décision autonome[^1]. Les deux textes se répondent. **Lecture de l'auteur** : cette continuité entre le diagnostic de 2024 et le texte de 2025 renforce la lecture des analystes exposée en §9.3 — le BSIF n'a pas rencontré l'IA par accident au détour d'une définition générale, il l'avait identifiée comme un facteur de risque de modèle et l'avait explicitement routée vers E-23 un an auparavant. Le socle établit les deux faits et le lien du rapport vers E-23 ; il n'établit pas l'intention que cette lecture prête au régulateur.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis pour la suite. **Premièrement**, le calendrier est fixe et le préavis est mesuré : dix-neuf mois et vingt jours entre la publication finale du 11 septembre 2025 et l'entrée en vigueur du 1er mai 2027 ; neuf mois et quinze jours restants à la date de gel de ce chapitre, pour les institutions financières fédérales. **Deuxièmement**, la voie d'atteinte est définitionnelle et non nominative : E-23 inclut expressément les méthodes d'IA et d'apprentissage automatique dans « modèle » et anticipe des modèles à apprentissage et décision autonomes, sans jamais employer les mots « agentique », « agents » ou « orchestration ». **Troisièmement**, le rapport conjoint BSIF-ACFC du 24 septembre 2024 pose un constat que l'architecture devra absorber : la causalité entrées-sorties des systèmes d'IA est souvent indéterminable, et il rattache explicitement ce constat au cadre E-23.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas que le BSIF attend quoi que ce soit **pour l'IA agentique** : la couverture est **implicite, par la définition de modèle**, et son caractère acquis est une inférence de cinq analystes juridiques canadiens que cet ouvrage rapporte sans l'endosser comme état du droit. Il expose les cinq domaines d'attentes du texte, mais il ne dit pas comment les appliquer à un parc donné : cette qualification se mène sur le texte officiel. Il ne dit pas que ~70 % des institutions financières fédérales ont adopté l'IA : c'est une **projection** du BSIF et de l'ACFC issue d'une enquête auto-déclarée, dont le socle ne documente aucune vérification. Il ne dit rien, enfin, de ce qu'il faut construire pour répondre à tout cela : les chapitres 10 à 12 complètent le tableau réglementaire, le chapitre 13 en fait des cadres d'architecture, et les Parties VI et VII les instancient.

E-23 n'a pas été écrite pour l'IA agentique : de tout ce qui suit, c'est le seul énoncé que le socle établit. Les cinq analystes juridiques canadiens la tiennent pour atteinte quand même, par la définition de « modèle » — leur lecture, non le texte du BSIF. **Lecture de l'auteur** : si cette lecture est juste, E-23 est plus contraignante, et non moins, qu'un texte qui l'aurait nommée — nul ne peut se prévaloir d'une liste dans laquelle son système ne figurerait pas.

---

## Notes

[^1]: PRD §7.3, **F-09** (niveau **[A/B mixte]** — [A] pour les faits des passes 1-2, [B] pour les exigences opératoires extraites le 16 juill. 2026 ; confiance haute). Ce chapitre mobilise les **deux strates**, et l'ordre des rangs doit être lu correctement : dans la taxonomie du PRD §7, **[B] est *sous* [A]** ([A] = vote adversarial 3-0 ; [B] = source primaire lue, sans vote). L'extraction du 16 juillet 2026 n'a donc pas « élevé » F-09 : elle a **enrichi** une entrée déjà votée d'un contenu de rang inférieur. **L'énumération [A] de F-09 est close** : tout ce qui n'y figure pas relève de la strate [B]. **Strate [A] mobilisée** — publication de la version finale le 11 septembre 2025 ; entrée en vigueur le 1er mai 2027 ; portée : application à toutes les institutions financières fédérales, y compris les succursales étrangères, dans la mesure compatible (§A.2) ; définition de « modèle » incluant explicitement les méthodes d'IA/AA ; et le fait que la couverture de l'IA agentique est une **inférence d'analystes juridiques** (McCarthy Tétrault, Torys, Blakes, BLG, Sookman), jamais une terminologie du BSIF. **Strate [B] mobilisée** — deux faits qu'il serait tentant de porter en [A] et que le PRD range expressément sous [B] : l'**anticipation** par le BSIF de modèles à apprentissage et décision autonomes, absente de l'énumération close ; et la **vérification négative** — E-23 n'emploie jamais « agentique », « agents » ni « orchestration » —, F-09 rangeant « la re-vérification mécanique de la vérification négative » sous [B] (texte intégral EN et FR, 16 juill. 2026 : 0 occurrence ; « autonom\* » = 8). *Confusion rectifiée le 17 juillet 2026 (audit, M-06) : la présente note portait ces deux faits en [A]. C'est la faute que le PRD §7 signale nommément — elle se reforme parce que [B] se lit spontanément comme « mieux vérifié » alors qu'il est « moins éprouvé ».* **Strate [B] mobilisée, suite** (extraction du texte intégral et de la lettre d'accompagnement du 11 sept. 2025) : libellé verbatim de la définition (§A.4) et son caractère « intentionally broad » ; projet de 2023 et retrait des régimes de retraite fédéraux du périmètre final ; cycle de vie à cinq volets (§A.4) ; inventaire (§C.1, principe 2.1) et champs de l'Appendice 1 ; cotation graduée (§A.3, §C.2, principes 2.2–2.3) ; documentation de modèle (§D.2, principe 3.3) ; surveillance continue (§D.2, principe 3.6) ; ligne directrice **fondée sur des principes**, 12 principes au conditionnel (« should ») — **« attendu par E-23 », jamais « exigé »** (PRDPlan §4.4). *Sources primaires lues et extraites le 16 juill. 2026 : osfi-bsif.gc.ca, versions EN et FR de la ligne directrice E-23 (applicable au 1er mai 2027) ; lettre d'accompagnement du 11 sept. 2025.*

[^2]: PRD §7.3, **F-25** (niveau [A]) — **renvoi seulement** : la ligne directrice sur l'IA de l'AMF est **finale depuis le 30 mars 2026** et entre en vigueur le **1er mai 2027**, même date qu'E-23. Sources : lautorite.qc.ca ; Norton Rose Fulbright ; rapport annuel Desjardins 2025. **Réserve F-25** : ne jamais écrire « en attente » ni « en projet » (état périmé depuis le 30 mars 2026). Traitement complet : chapitre 11.

[^3]: PRD §7.3, **F-10** (niveau [A], confiance haute). Source primaire : osfi-bsif.gc.ca, rapport conjoint BSIF-ACFC publié le 24 septembre 2024. Faits mobilisés : trajectoire d'adoption déclarée ~30 % (2019) → ~50 % (2023), projection ~70 % d'ici 2026 (enquête auto-déclarée) ; risque de modèle accru propre à l'IA — très grand nombre de paramètres appris de façon autonome, relations causales entrées-sorties souvent indéterminables ; lien explicite au cadre E-23.

[^4]: PRD §8.2.4 (règle d'attribution : couverture agentique d'E-23 = inférence d'analystes juridiques — jamais « le BSIF exige pour l'IA agentique », toujours « couverture implicite via la définition de modèle ») ; formulation imposée par PRDPlan §4.4, **rendue en §9.3 dans la substance imposée par §8.2.4** — la vérification négative, la définition large et la couverture implicite attribuée aux analystes. *L'attestation de reproduction verbatim que portaient cette note et le §9.3 est rectifiée le 17 juillet 2026 (audit, M-07) : la forme de §4.4 a été enrichie le 16 juillet 2026, postérieurement au gel du présent chapitre. L'avertissement en tête de §4.4 (17 juill. 2026) règle le cas — une forme enrichie ne périme pas une pièce gelée qui en porte la substance, mais aucune pièce n'a le droit d'attester un verbatim qu'elle n'a pas. Le blockquote n'est donc pas rouvert ; l'attestation l'est.* Forme imposée : `monographie/90-annexes/annexe-d-glossaire.md` §D.5 (« risque de modèle ») et §D.7 (termes proscrits).

[^5]: PRD §9.2 (corpus de sources) : les cabinets juridiques canadiens — la liste admise comprend McCarthy Tétrault, Torys, Blakes et BLG — relèvent de la **corroboration secondaire admise**, « jamais comme source unique d'un fait central ». **Précision** : des cinq analystes nommés par F-09, quatre sont des cabinets figurant à cette liste ; **Sookman** n'y figure pas et n'est pas un cabinet. L'ouvrage écrit donc « analystes juridiques » (forme de F-09 et de la formulation imposée), jamais « cinq cabinets ». Le socle n'établit pas davantage l'**indépendance** de ces cinq analyses : aucun argument du chapitre ne repose sur elle. Le fait central avancé en §9.3 porte sur l'**état de l'opinion des analystes** (attesté par F-09, niveau [A]), non sur l'état du droit.

[^6]: PRD §8.2.6 (règle d'attribution : les projections sont toujours présentées comme projections de leur auteur) ; formulation imposée par PRDPlan §4.4 (« Projection »). Donnée sous-jacente : **F-10** — réserve explicite du socle, « le 70 % est une projection, pas un fait observé ».

[^7]: PRD §7.3, **F-27** ([B] — texte officiel consulté sur LégisQuébec le 16 juill. 2026) — **renvoi seulement** : art. 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (P-39.1), en vigueur depuis le 22 septembre 2023 ; il impose, pour toute décision fondée exclusivement sur un traitement automatisé et sur demande de la personne visée, de communiquer les raisons et les principaux facteurs et paramètres ayant mené à la décision. **Réserve d'interprétation du socle (niveau [C])** : selon l'analyse Fasken, une intervention humaine significative *avant* la décision écarte l'application de l'article — le pivot « exclusivement », la nuance Fasken et les positions de la CAI sont examinés au **chapitre 11 §11.3**, qui porte seul le traitement complet et le texte de l'article. Le présent chapitre ne fait que signaler le croisement et n'en tire aucune conclusion juridique.

<!-- Boucle qualité PRDPlan §4.2 — état :
     0bis. Passe de conformité (17 juill. 2026, suites de l'audit) ... FAITE. Périmètre strictement correctif :
                                   aucune information nouvelle, date de gel INCHANGÉE (16 juillet 2026).
                                   - [M-06] Note [^1] : stratification F-09 rectifiée. L'anticipation de la décision
                                     autonome et la vérification négative étaient rangées sous « Strate [A] mobilisée » ;
                                     le PRD §7.3 les range sous [B] (énumération [A] CLOSE : date de publication,
                                     entrée en vigueur, portée, définition de « modèle », et le fait que la couverture
                                     agentique est une inférence d'analystes). Les deux faits sont passés en [B],
                                     avec le motif. Corollaire au corps (§9.2) : « d'un niveau de preuve inférieur aux
                                     faits qui précèdent » était faux — l'anticipation qui précède est elle-même [B].
                                     Phrase reformulée sur les faits VOTÉS (dates, portée, définition). L'USAGE des
                                     faits n'est pas touché : un fait [A] mobilisé reste [A].
                                   - [M-07] Attestations de verbatim rectifiées (§9.3 « reproduite sans altération » ;
                                     note [^4] « reproduite verbatim » ; présent bloc, étape 3). La forme §4.4 de la
                                     couverture agentique a été ENRICHIE le 16 juill. 2026, après le gel de ce chapitre :
                                     l'avertissement en tête de §4.4 (17 juill. 2026) admet le rendu antérieur qui en
                                     porte la substance, et proscrit l'attestation de verbatim non vérifiée. Blockquote
                                     §9.3 NON rouvert — noyau vérifié présent : vérification négative + couverture
                                     implicite ATTRIBUÉE aux analystes ; la définition « intentionally broad » est portée
                                     par le §9.2 (l'un des rares points où le blockquote seul ne porte pas tout le noyau
                                     de la forme enrichie — signalé, non corrigé : la substance §8.2.4 est au chapitre).
                                   - [m-15] Encadré §9.4 converti du gabarit cas 1 au gabarit cas 2 (PRDPlan §4.4) :
                                     « État de la recherche », « aucune passe de recherche n'a été conduite », source à
                                     retrouver. Le cas 1 présuppose une recherche et l'encadré déclarait dans le même
                                     souffle « Recherche menée le 16 juillet 2026 » et « aucune passe primaire dédiée
                                     n'a été conduite » — contradiction dans les termes. Substance inchangée.
                                   Encadré §9.1 NON touché (hors constat) : l'extraction du texte final y est une passe
                                   réelle et traçable, le cas 1 y est défendable.
     0. Passe de correction F-09 (16 juill. 2026, PRD v1.7) ... FAITE : marquage [A/B mixte] ([^1] refondue,
                                   deux strates explicitées, rang [B] SOUS [A] posé — l'extraction n'« élève » pas
                                   une entrée votée 3-0) ; encadré « le texte de la définition » SUPPRIMÉ (lacune
                                   comblée) et remplacé par le libellé verbatim (§A.4) + les cinq domaines
                                   d'attentes [B] ; encadré de genèse §9.1 restreint aux trois éléments
                                   d'antériorité désormais au socle ; « exigé/exigence » → « attendu/attente »
                                   (3 occ.) ; escalade b) infra TRANCHÉE. Volumétrie : +0,3 % (mesure old/new,
                                   corps l. 15-109) — reste dans 2700-3300. Aucune autre correction appliquée.
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps = 3280 mots après relecture adversariale
                                   — cible 3000 ±10 % soit 2700-3300 : conforme. Les correctifs (marqueurs
                                   « Lecture de l'auteur », membre « Recherche menée le » des trois encadrés)
                                   ont ajouté ~165 mots, compensés par ~185 mots de retraits : méta-commentaire
                                   (« c'est le point que l'architecte doit comprendre avant tout autre »),
                                   répétition verbatim du fait de socle en §9.2, et resserrement des trois
                                   encadrés. Aucun contenu tracé au socle n'a été retiré.)
     2. Traçabilité (CA-1, CA-5) . fait (7 notes ; F-09 et F-10 seuls porteurs de faits, F-25 et F-27 en renvoi ;
                                   terme anglais en italique à la 1re occurrence : « risque de modèle (*model risk*) » §D.5.
                                   Toutes les arithmétiques posées explicitement : 19 mois 20 j (11 sept. 2025 → 1er mai 2027) ;
                                   9 mois 15 j (16 juill. 2026 → 1er mai 2027) ; 20 pts/4 ans = 5 pts/an vs 20 pts/3 ans ≈ 6,7 pts/an)
     3. Balayage garde-fous ...... fait (§8.2.4 : formulation imposée rendue en §9.3 dans sa substance — attestation
                                   de verbatim RECTIFIÉE le 17 juill. 2026, voir 0bis [M-07] ; aucune occurrence de
                                   « E-23 exige pour l'agentique » ; §8.2.6 : les trois occurrences du 70 % portent
                                   « projection du BSIF et de l'ACFC » + « enquête auto-déclarée » ; motif R-7 (E-23|B-13)
                                   ressort massivement mais SANS OBJET — contexte réglementaire pur, filtré par PRDPlan §4.3 ;
                                   R-1/R-8 : motifs balayés, zéro occurrence dans le chapitre (aucune des quatre branches
                                   de la collision terminologique n'est mobilisée ici) ; réserve F-25 respectée
                                   (« finale depuis le 30 mars 2026 », jamais « en attente »))
     4. Relecture adversariale ... FAIT (deux relecteurs indépendants ; 6 constats bloquants + 11 réserves.
                                   TOUS FONDÉS — vérifiés un à un contre PRD §7.3 (F-09, F-10, F-27, F-36),
                                   §8.2.4, §9.2 et PRDPlan §4.4 ; aucun écarté. Ce que la relecture a RÉFUTÉ :
                                   a) FABRICATION PORTANTE — « cinq cabinets indépendants » : F-09 dit
                                      « analystes juridiques », et PRD §9.2 ne range que 4 des 5 nommés parmi
                                      les cabinets (Sookman est un auteur, pas un cabinet). « Indépendants »
                                      n'est établi par rien et servait de prémisse au 1er des trois piliers de
                                      la recommandation. Corrigé aux 3 occurrences (l. 15, 75, 109) ; la note
                                      [^5] — qui escamotait Sookman — porte désormais l'écart explicitement.
                                   b) CONTRADICTION INTERNE §9.2 — « est un modèle au sens d'E-23 […] doit le
                                      traiter comme tel » : qualification fine + exigence opératoire que
                                      l'encadré situé 20 lignes plus bas déclare impossibles (F-09 ne porte ni
                                      le libellé ni les exigences). Réécrit en « Lecture de l'auteur » bornée.
                                   c) CHUTE DU CHAPITRE — « Elle l'atteint quand même » affirmait comme fait
                                      établi ce que §9.3 déclare non établi (§8.2.4, Annexe D §D.7). Atteinte
                                      réattribuée aux analystes ; le jugement « plus contraignante » marqué.
                                   d) ENCADRÉ §9.1 — proposait une inférence (« ce qui établit que ce cadre
                                      existait ») sous la clause « aucune inférence n'est proposée ici » :
                                      inférence retirée, l'encadré s'en tient au renvoi que F-10 porte.
                                   e) BRÈCHE CA-1 — citation verbatim de l'art. 12.1 (matière de F-27, assigné
                                      au ch. 11 par TOC) sans note ni F-xx à l'en-tête, assortie d'un verdict
                                      juridique amputé de la réserve Fasken [C]. Réduit à un renvoi ; F-27
                                      ajouté à l'en-tête + note [^7] portant la réserve. Voir point e) infra.
                                   f) Réserves appliquées : décompte « deux dates + un périmètre » (et non
                                      « trois faits de calendrier ») ; « jour pour jour » (faux de 13 j) →
                                      « onze mois et dix-huit jours » ; guillemets de citation ôtés sur
                                      « dans la mesure compatible » (paraphrase de socle, pas un verbatim
                                      d'E-23) et « succursales de banques étrangères » → « succursales
                                      étrangères » (forme F-09) ; membre « Recherche menée le [date] » ajouté
                                      aux TROIS encadrés (forme imposée §4.4, omise partout) ; gloses
                                      « apprentissage/décision autonomes » marquées ; « E-23 rejoint
                                      l'agentique » → conditionnel attribué ; 4e label « inférence de lecture »
                                      → « inférence d'auteur » (forme §4.4) ; incise F-36 non tracée retirée ;
                                      engagement au présent sur la Partie VII (non rédigée) mis au conditionnel.
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.

     POINTS DE GOUVERNANCE SIGNALÉS AU PARENT (non corrigés ici — CLAUDE.md, règle de chirurgie) :
     a) [PARTIELLEMENT LEVÉ le 16 juill. 2026] TOC §9.1 intitulée « Genèse et calendrier » : l'extraction
        d'E-23 verse au socle trois éléments d'antériorité (projet de 2023 ; retrait des FRPP ; commentaires
        demandant de restreindre la définition), désormais exposés en §9.1. Le socle reste muet sur le
        calendrier de consultation et le contenu du projet de 2023 : encadré restreint à cette part.
        Arbitrage TOC (amender l'intitulé, ou ouvrir une lacune §10) toujours ouvert, mais de portée réduite.
     b) [TRANCHÉE le 16 juill. 2026 — élévation de F-09, PRD v1.7] L'escalade disait : « F-09 ne porte ni le
        libellé verbatim de la définition, ni aucune exigence opératoire d'E-23 ». L'extraction du texte
        intégral (EN + FR) l'a comblée : libellé §A.4, cycle de vie, inventaire + Appendice 1, cotation,
        documentation, surveillance sont au socle en [B]. L'écart socle↔Annexe B est résolu dans le même
        mouvement : « fiches de modèles » a été RETIRÉ d'Annexe B.3 (0 occurrence dans E-23, EN et FR).
        Ce chapitre n'employait pas le terme ; rien à corriger ici de ce chef.
     c) L'horizon de la projection F-10 (2026) est atteint ; aucune entrée du socle ne documente de mesure
        observée. Candidat à une lacune §10 formelle + point de revalidation P4.1.
     d) F-25 employé en renvoi bien que TOC n'assigne que F-09/F-10 au ch. 9 (convergence du 1er mai 2027,
        exigée par PRD §6 Partie III). À entériner dans TOC si conservé.
     e) [AJOUTÉ EN RELECTURE] F-27 employé en renvoi au ch. 9 (croisement indéterminabilité causale ↔ art. 12.1),
        alors que TOC assigne l'art. 12.1 au ch. 11 §11.2. La citation verbatim et le verdict juridique ont été
        RETIRÉS (constat bloquant) ; ne subsiste qu'un renvoi sec + note [^7] portant la réserve Fasken [C].
        Même arbitrage que d) : entériner le chevauchement dans TOC, ou retirer le renvoi. Vérifié : PRD §6
        assigne F-27 à la Partie III (niveau PARTIE), TOC l'assigne aux ch. 11 et 13 (niveau CHAPITRE) — les
        deux ne se contredisent pas ; seule l'admissibilité d'un renvoi F-27 depuis le ch. 9 est à trancher.
     f) [AJOUTÉ EN RELECTURE] Marqueur d'inférence : TROIS libellés coexistent dans l'ouvrage — « Lecture de
        l'auteur » (convention de fait, ch. 1-4 et 8 lois dans ce chapitre), « inférence d'auteur » (forme du
        PRD et de PRDPlan §4.4) et, introduit par erreur ici, « inférence de lecture » (corrigé). PRDPlan §4.4
        n'enregistre aucun des deux premiers. À unifier en gouvernance AVANT la rédaction des ch. 13-24, sans
        quoi la grille CA-1 n'a pas de motif unique à balayer.
     g) [AJOUTÉ EN RELECTURE] Le membre imposé « Recherche menée le [date] » de l'encadré de lacune (§4.4) était
        omis des trois encadrés de ce chapitre. Il est désormais renseigné, mais HONNÊTEMENT : aucune passe de
        recherche primaire n'a été menée à la rédaction (hors périmètre P0). Si la forme §4.4 présuppose qu'une
        passe soit conduite à chaque lacune déclarée, alors P0 doit être étendu — sinon le membre se réduit à
        « pas cherché », ce qui est exact mais affaiblit le dispositif. Point à trancher pour les 23 chapitres.
-->
