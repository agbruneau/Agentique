# Chapitre 10 — Le vide fédéral : de C-27 à C-36

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | **F-24** [B, revalidé le 16 juillet 2026] ; F-02, F-21 en renvoi (§10.1) ; F-09, F-25, F-26, F-27 en renvoi (§10.3) |
| Garde-fous à surveiller (PRD §8) | Glossaire §D.7 (« C-36, la loi canadienne sur l'IA » — terme proscrit) ; §8.2.4 (couverture agentique d'E-23, en renvoi) ; réserve F-25 (jamais « en attente ») ; R-7 : le motif « E-23 » ressort ici en contexte réglementaire pur, sans objet (PRDPlan §4.3) |
| Volumétrie cible | ~2400 mots |

> **Thèse ([TOC.md](../../TOC.md))** : La mort de la LIAD laisse le Canada sans régulation fédérale spécifique de l'IA ; C-36 ne comble pas ce vide — c'est une loi de protection des renseignements personnels — et la couverture effective passe donc par les régulateurs sectoriels.

---

L'architecte qui, à l'été 2026, ouvre le dossier réglementaire d'un programme agentique dans une institution financière fédérale commence en général par chercher la loi. Il cherche le texte fédéral qui nommerait les systèmes d'intelligence artificielle, en établirait les classes de risque, en fixerait les obligations d'évaluation et de journalisation, et lui donnerait une cible de conformité datée. Ce texte n'existe pas. Il a été déposé, débattu, puis il est mort ; et ce qui a été déposé depuis à sa place ne le remplace pas.

Ce chapitre établit ce fait négatif et en tire les conséquences d'architecture. Il soutient trois propositions. La première est que le vide fédéral n'est pas un accident de calendrier en voie de résorption, mais un état documenté qui dure, à la date de gel du présent chapitre, depuis dix-huit mois. La deuxième est que le projet de loi C-36, régulièrement présenté comme la réponse fédérale à l'intelligence artificielle, est en réalité une réforme de la protection des renseignements personnels qui porte des volets d'IA — la distinction n'est pas byzantine, elle décide de ce qu'une institution doit inscrire à son registre d'obligations. La troisième est que, ce vide persistant, la charge réglementaire effective repose entièrement sur les régulateurs sectoriels : le BSIF, l'AMF et les Autorités canadiennes en valeurs mobilières, dont les chapitres 9, 11 et 12 traitent respectivement.

## 10.1 La prorogation du 6 janvier 2025 et la mort de C-27

Le point de départ est une date de procédure parlementaire, et c'est déjà instructif : le cadre fédéral canadien de l'IA n'a pas été voté, il est mort au feuilleton.

Le projet de loi C-27 réunissait deux textes distincts : la Loi sur la protection de la vie privée des consommateurs (LPVPC), destinée à refondre le régime fédéral de protection des renseignements personnels, et la Loi sur l'intelligence artificielle et les données (LIAD), premier — et à ce jour unique — projet fédéral de régulation spécifique des systèmes d'IA. À la **prorogation du 6 janvier 2025**, C-27 est mort au feuilleton, emportant les deux volets ensemble[^1].

Il faut mesurer ce qu'a été cet attelage. La LIAD voyageait dans le même véhicule législatif qu'une réforme de la vie privée ; les deux volets sont morts ensemble à la prorogation. **Lecture de l'auteur** : l'attelage des deux volets paraît avoir décidé du sort de la LIAD ; le socle établit la concomitance, non la causalité. Il documente la mort du projet et sa date ; il ne documente pas les motifs politiques de la prorogation, ni le contenu des obligations que la LIAD aurait imposées, et ce chapitre ne comble ni l'un ni l'autre.

Ce qu'il faut retenir, c'est la durée. Du 6 janvier 2025 au 16 juillet 2026, date de gel du présent chapitre, il s'écoule **dix-huit mois et dix jours** sans qu'aucun texte fédéral ne vienne réguler les systèmes d'IA en tant que tels. Ce n'est pas un intervalle : c'est l'état stable du droit fédéral canadien sur toute la période que couvre cet ouvrage. Le protocole A2A a été lancé en avril 2025, transféré à la Linux Foundation en juin 2025 et porté à sa première spécification stable pendant ce vide[^2] ; les mises en production agentiques canadiennes documentées en Partie V s'y sont déroulées[^3] ; les deux régimes sectoriels datés du 1er mai 2027 y ont été finalisés — E-23 le 11 septembre 2025[^4], la ligne directrice de l'AMF le 30 mars 2026[^5]. Aucun des faits que cette monographie rapporte n'a eu de loi fédérale d'IA pour cadre.

**Lecture de l'auteur** — et il faut la marquer comme telle : pour l'institution financière, l'enseignement pratique de janvier 2025 n'est pas qu'un texte a échoué, mais qu'une planification de conformité adossée à un projet de loi en cours d'examen est une planification adossée à rien. Le socle établit la mort de C-27 et l'absence de reprise ultérieure de la LIAD[^6] ; il n'établit pas de règle générale sur la fiabilité des trajectoires législatives. La règle que le présent ouvrage en tire — ne dater un programme de conformité que sur des textes en vigueur ou publiés en version finale — est une inférence, mais elle est celle que la suite de ce chapitre valide.

## 10.2 Le ministre de l'IA et le projet de loi C-36

La séquence qui suit paraît, de loin, corriger le tir. En **mai 2025**, le gouvernement fédéral nomme Evan Solomon au poste de ministre de l'IA et de l'Innovation numérique — le premier titulaire d'un portefeuille fédéral ainsi défini[^7]. Le 15 juin 2026, ce même ministre dépose le **projet de loi C-36**[^8]. Entre la nomination et le dépôt, treize mois s'écoulent (mai 2025 → juin 2026) ; entre la prorogation qui a tué C-27 et ce dépôt, **dix-sept mois** (6 janvier 2025 → 15 juin 2026).

Un ministre de l'IA dépose un projet de loi dix-sept mois après la mort du seul texte fédéral d'IA : la lecture par raccourci s'impose d'elle-même, et elle est fausse. Le titre officiel de C-36 est ***Protecting Privacy and Consumer Data Act*** (PPCDA). Le texte est une réforme de la protection des renseignements personnels : il modifie la Loi sur la protection des renseignements personnels et les documents électroniques (LPRPDE) et prévoit la création d'une ***Digital Safety and Data Protection Commission of Canada***[^8]. Il porte, il est vrai, trois volets — un droit à la suppression des renseignements, une protection des données des enfants, et un volet de transparence algorithmique, seul des trois que le socle qualifie d'IA — mais il les porte **comme composantes d'une loi sur la vie privée, non comme les dispositifs d'une loi IA autonome de type LIAD**[^8].

La qualification n'est pas affaire de purisme terminologique : elle décide de ce qu'une institution inscrit à son registre d'obligations. Un responsable de la conformité qui inscrirait C-36 à son plan comme « cadre IA fédéral à venir » construirait son inventaire d'obligations sur une qualification erronée : il attendrait un régime de conformité propre aux systèmes d'IA et recevrait une réforme de la protection des renseignements personnels.

Deux précisions de statut s'imposent, l'une et l'autre datées du 16 juillet 2026, date de gel du présent chapitre. Premièrement, C-36 **est un projet de loi et non une loi** : première lecture le 15 juin 2026 ; à l'étape de la deuxième lecture au 16 juillet 2026, date de consultation du socle[^8]. Aucune obligation n'en découle aujourd'hui, et cet ouvrage ne se prononce pas sur son adoption. Deuxièmement, la Commission qu'il prévoit **n'existe pas** : sa création est un effet projeté du texte, non un fait.

> **État de la connaissance vérifiable — le contenu du volet de transparence algorithmique de C-36**
>
> Que prescrit exactement le volet de transparence algorithmique du projet de loi C-36 ? Recherche menée le 16 juillet 2026 (passe P0.1 de revalidation) : consultation directe de LEGISinfo (45-1/c-36) et des analyses de Fasken, de DLA Piper et du *Canadian Lawyer Magazine* de juin 2026. Ces sources établissent l'existence des trois volets et la nature générale du texte ; elles n'en établissent pas le contenu article par article, et le texte demeure susceptible d'amendement en deuxième lecture. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici[^9].

## 10.3 Conséquences : le vide persiste, la charge est sectorielle

La proposition centrale du chapitre peut maintenant être énoncée dans les termes exacts du socle. La LIAD **ne sera pas ravivée telle quelle**, et **le vide fédéral sur la régulation spécifique de l'IA persiste**[^6]. Une formule de la presse spécialisée résume le constat, que l'on citera dans sa langue d'origine : « *Canada remains the only G7 nation without a binding AI regulatory framework* » — AIMag, juin 2026[^6]. Le fait central, la persistance du vide, est porté par F-24 lui-même.

Il faut cependant énoncer avec autant de soin ce que ce vide n'est pas, car la formule prête à contresens. Le Canada n'est pas un espace de non-droit pour les systèmes agentiques. Le vide est **spécifique** : il porte sur l'absence d'un régime fédéral contraignant qui régulerait les systèmes d'IA *en tant que tels*. Les Autorités canadiennes en valeurs mobilières l'énoncent pour leur champ, dans l'avis 11-348 : la guidance « ne crée ni ne modifie aucune exigence » — les lois sur les valeurs mobilières existantes s'appliquent aux systèmes d'IA (voir ch. 12)[^10]. **Lecture de l'auteur** : le même raisonnement vaut par construction pour les autres branches du droit général — protection des renseignements personnels, droit des contrats, responsabilité civile —, qu'aucun régime d'IA n'est venu écarter ; le socle ne documente ce point que pour les valeurs mobilières.

Cette distinction commande une conséquence de périmètre que l'architecte doit poser tôt. **Lecture de l'auteur** : le socle établit que C-36 modifie la LPRPDE[^8] — une loi dont l'objet est le traitement des renseignements personnels. (C-36 modifie donc la même loi que le cadre bancaire du ch. 14 : même véhicule législatif, aucune interaction documentée au socle.) Il n'établit pas le périmètre d'application des volets d'IA du projet, et l'encadré ci-dessus dit pourquoi. Mais la nature du véhicule autorise au moins une lecture prudente : un régime greffé sur une loi de protection des renseignements personnels a vocation à saisir les traitements de renseignements personnels, non l'ensemble des décisions d'un système agentique. Un agent qui orchestre un rapprochement comptable, une chaîne de messages de paiement interbancaires ou une supervision d'infrastructure ne manipule pas nécessairement de renseignements personnels ; un agent de pré-adjudication hypothécaire, lui, en manipule par construction. L'inférence porte sur la logique du véhicule législatif, pas sur le texte de C-36, dont le libellé n'est pas au socle — elle est indiquée ici comme hypothèse de travail à vérifier, jamais comme fondement d'une position de conformité.

Pour l'institution financière fédérale, la conséquence est un déplacement complet de la charge vers les régulateurs sectoriels, et ce déplacement est daté.

Du côté fédéral prudentiel, la ligne directrice E-23 du BSIF sur le risque de modèle (*model risk*) est publiée en version finale et entre en vigueur le **1er mai 2027**[^4]. Sa portée sur l'agentique demande une formulation exacte, que le chapitre 9 développe : E-23 n'emploie jamais « agentique », « agents » ni « orchestration » ; sa définition de « modèle » englobe les méthodes d'IA et d'apprentissage automatique, d'où une **couverture implicite** que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise[^4]. **Lecture de l'auteur** : une institution prudente la traitera comme acquise d'ici le 1er mai 2027. Le socle établit que les analystes la tiennent pour acquise, non que les institutions y soient tenues ; la recommandation est celle du chapitre 9, qui l'expose et la marque comme telle (§9.3).

Du côté québécois, la ligne directrice sur l'IA de l'AMF est **finale depuis le 30 mars 2026** et entre en vigueur le **1er mai 2027** — la même date qu'E-23 (voir ch. 11)[^5]. À ces deux dates s'ajoute une contrainte déjà en vigueur : l'article 12.1 de la Loi 25, opposable depuis le 22 septembre 2023, qui impose, pour toute « décision fondée exclusivement sur un traitement automatisé » de renseignements personnels, une information proactive au plus tard au moment de la décision, puis, sur demande, l'explication des raisons et facteurs et une révision humaine (voir ch. 11)[^11]. Du côté des marchés financiers, enfin, l'avis 11-348 des Autorités canadiennes en valeurs mobilières, publié le 5 décembre 2024, retient une définition des systèmes d'IA incluant explicitement des niveaux variables d'autonomie et d'adaptativité après déploiement (voir ch. 12)[^10].

Un calcul suffit à mesurer la situation d'une institution à la date de gel du présent chapitre. Du 16 juillet 2026 au 1er mai 2027, il reste **neuf mois et quinze jours** avant l'entrée en vigueur simultanée d'E-23 et de la ligne directrice de l'AMF. L'article 12.1, lui, est opposable depuis près de trois ans.

**Lecture de l'auteur** : l'ordre de priorité qu'un architecte devrait en tirer est l'inverse exact de celui que suggère l'actualité législative. Le socle établit trois faits — le vide fédéral persiste, un projet de loi fédéral de vie privée est en deuxième lecture, et quatre instruments sont soit en vigueur, soit finalisés avec une date d'entrée en vigueur ferme : E-23, la ligne directrice de l'AMF, l'avis 11-348 et l'article 12.1 de la Loi 25 — ce dernier relevant du droit général québécois de la protection des renseignements personnels, non d'un régulateur sectoriel, mais déjà opposable. Le socle n'établit pas d'ordre de priorité entre eux ; celui-ci est une inférence de l'auteur. Elle est néanmoins difficile à contester : la veille sur un texte non adopté, dont le contenu détaillé n'est pas au socle et qui n'est pas une loi d'IA, ne saurait mobiliser les ressources qu'appellent quatre instruments datés dont l'un est déjà opposable. La conséquence d'architecture — traduire ces exigences sectorielles en frames déterministes — est l'objet du chapitre 13, pivot de cet ouvrage.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, le Canada n'a pas de régime fédéral contraignant propre aux systèmes d'IA : C-27 est mort au feuilleton le 6 janvier 2025, la LIAD ne sera pas ravivée telle quelle, et le vide persiste à la date de gel du présent chapitre. **Deuxièmement**, le projet de loi C-36 ne comble pas ce vide et ne prétend pas le combler : c'est une réforme de la protection des renseignements personnels, portant des volets d'IA, dont le statut au 16 juillet 2026 est celui d'un texte en deuxième lecture. **Troisièmement**, la couverture effective de l'agentique en institution financière canadienne est portée par des instruments datés, sectoriels pour l'essentiel : E-23 et la ligne directrice de l'AMF au 1er mai 2027, l'avis 11-348 dans le champ des lois existantes, et — hors champ sectoriel, mais déjà opposable — l'article 12.1 de la Loi 25.

Ce que ce chapitre ne dit pas mérite la même netteté. Il ne dit pas que C-36 sera adopté, ni qu'il ne le sera pas : le socle documente une étape parlementaire, pas une issue. Il ne dit pas ce que prescrit le volet de transparence algorithmique de C-36 — l'encadré ci-dessus expose pourquoi cette question demeure ouverte. Il ne dit pas que le vide fédéral serait une lacune de protection : le droit général s'applique, et quatre instruments datés encadrent l'agentique en institution financière (ch. 9, 11, 12). Ce que la LIAD aurait exigé n'est pas au socle ; l'ouvrage ne le compare donc à rien. Il ne dit rien, enfin, de ce que les régulateurs sectoriels exigent réellement — c'est l'objet des chapitres 9, 11 et 12, et de leur traduction en architecture au chapitre 13.

L'absence d'une loi fédérale sur l'IA n'est pas une permission. C'est une redistribution de la charge.

---

## Notes

[^1]: PRD §7.3, **F-24** (niveau [B], revalidé le 16 juillet 2026 par consultation directe de LEGISinfo). Source primaire : parl.ca/LEGISinfo. Le projet de loi C-27 réunissait la LPVPC (protection de la vie privée des consommateurs) et la LIAD (intelligence artificielle et données) ; il est mort au feuilleton à la prorogation du 6 janvier 2025.

[^2]: PRD §7.3, **F-02** (niveau [A]) — renvoi à la Partie I. A2A : lancé par Google en avril 2025, transféré à la Linux Foundation en juin 2025 (Apache 2.0) ; v1.0 = première spécification stable et « production-ready ». *Sources : a2a-protocol.org/latest/announcing-1.0 ; communiqué Linux Foundation du 9 avril 2026.* Le socle ne date pas la publication de v1.0 ; elle est nécessairement postérieure au lancement d'avril 2025, donc comprise dans la période de vide, laquelle persiste à la date de gel.

[^3]: PRD §7.3, **F-21** (niveau [A]) — renvoi à la Partie V. Scotiabank : capacités agentiques ajoutées **en 2025** à AIDox (traitement autonome des courriels clients en services bancaires aux entreprises). *Sources : scotiabank.com Perspectives (juill. 2025) ; MIT Sloan Management Review.* **Métrique auto-déclarée** (PRD §8.2.2) : les chiffres de volume et de délai sont des déclarations d'entreprise, développées et attribuées au chapitre concerné de la Partie V.

[^4]: PRD §7.3, **F-09** (entrée **[A/B mixte]** — [A] pour les faits des passes 1-2, [B] pour les exigences opératoires extraites le 16 juill. 2026 ; **strate [A] mobilisée** : date de publication, entrée en vigueur, définition de « modèle », couverture agentique comme inférence d'analystes — le chapitre ne cite ni le cycle de vie ni l'inventaire, développés au ch. 9. **Strate [B] également mobilisée**, contrairement à ce que cette note a déclaré jusqu'au 17 juillet 2026 : la **vérification négative** — « E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration » — que le PRD range expressément sous [B], et que la formulation imposée ci-dessous énonce. *La note affirmait « ne mobilise que la strate [A] » dans la phrase même qui porte un fait de strate [B] : l'énumération [A] de F-09 est close et ne contient pas la vérification négative (audit du 17 juill. 2026 — défaut de la même classe que M-06, relevé lors de sa correction et non par l'audit).*) — renvoi au ch. 9. Source primaire : osfi-bsif.gc.ca (ligne directrice E-23, version finale du 11 septembre 2025, en vigueur le 1er mai 2027). Formulation de la couverture agentique **imposée** par PRD §8.2.4 et PRDPlan §4.4, **rendue dans la substance imposée par §8.2.4** : E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration. *L'attestation de reprise « mot pour mot » est rectifiée le 17 juillet 2026 (audit, m-17) : la forme de §4.4 a été enrichie le 16 juillet 2026, après le gel du présent chapitre — l'avertissement en tête de §4.4 admet le rendu qui en porte la substance et proscrit l'attestation de verbatim non vérifiée. Le gabarit écrit d'ailleurs « ne **nomme** ni », non « n'emploie **jamais** ».* La couverture est une **inférence d'analystes juridiques** (McCarthy Tétrault, Torys, Blakes, BLG, Sookman), jamais une terminologie du BSIF.

[^5]: PRD §7.3, **F-25** (niveau [A]) — renvoi au ch. 11. Source primaire : lautorite.qc.ca ; corroboration Norton Rose Fulbright. **Réserve F-25** : ne jamais écrire « en attente » ni « en projet » — la ligne directrice est finale depuis le 30 mars 2026, en vigueur le 1er mai 2027.

[^6]: PRD §7.3, **F-24** [B]. « La LIAD ne sera pas ravivée telle quelle : le vide fédéral sur la régulation spécifique de l'IA persiste » — formulation du socle. La citation verbatim « *Canada remains the only G7 nation without a binding AI regulatory framework* » est **attribuée à AIMag** par le rapport de revalidation `verification/revalidation-2026-07-16.md` (« Trajectoire C-36 ») ; elle est citée ici comme illustration d'un constat de presse spécialisée, jamais comme source d'un fait central (PRD §9.2). Le fait central — la persistance du vide — est porté par F-24 lui-même. **Divergence d'attribution signalée à la gouvernance** : F-24 attribue la formule à « des juristes », le rapport de revalidation à AIMag ; le corps retient l'attribution du rapport, la plus restrictive.

[^7]: PRD §7.3, **F-24**. Evan Solomon, nommé en mai 2025 premier titulaire du portefeuille fédéral de l'IA et de l'Innovation numérique. Sources : parl.ca/LEGISinfo ; corroboration BetaKit, CPAC.

[^8]: PRD §7.3, **F-24** [B]. Sources primaires : parl.ca/LEGISinfo (45-1/c-36) ; CPAC (15 juin 2026). Corroboration : Fasken, DLA Piper, *Canadian Lawyer Magazine* (juin 2026). Projet de loi C-36, titre officiel *Protecting Privacy and Consumer Data Act* (PPCDA) : première lecture le 15 juin 2026, à l'étape de la deuxième lecture **au 16 juillet 2026, date de consultation de LEGISinfo** (passe P0.1) — le socle date l'observation de l'étape, non son atteinte. Réforme de la LPRPDE ; création prévue de la *Digital Safety and Data Protection Commission of Canada* ; volets « droit à la suppression », « données des enfants » et « transparence algorithmique », ce dernier seul qualifié d'IA par le socle. **Précision de portée du socle (correction appliquée en P0.1)** : C-36 n'est **pas** une loi IA autonome de type LIAD.

[^9]: Encadré au format imposé par PRDPlan §4.4 (« encadré de lacune »), clause de clôture reprise mot pour mot. La question du contenu article par article de C-36 n'est pas listée aux lacunes de PRD §10 ; elle est ouverte ici par la rédaction du présent chapitre, au titre de PRD §10 (interdiction de combler par du non-vérifié) et de CA-6. **Périmètre de la question** : elle porte sur le seul libellé du volet ; la question distincte du champ d'application est traitée en §10.3, où elle est marquée « Lecture de l'auteur » et présentée comme hypothèse de travail. Recherche documentée : `verification/revalidation-2026-07-16.md`, ligne « Trajectoire C-36 ».

[^10]: PRD §7.3, **F-26** (niveau [B], consulté directement sur osc.ca) — renvoi au ch. 12. Avis ACVM 11-348, publié le 5 décembre 2024 ; doctrine « la guidance ne crée ni ne modifie aucune exigence » — **les lois sur les valeurs mobilières existantes** s'appliquent aux systèmes d'IA. Portée fermée : personnes inscrites, émetteurs assujettis hors fonds d'investissement, marchés et participants, chambres de compensation, référentiels centraux, agences de notation et administrateurs d'indices désignés. Définition des systèmes d'IA incluant des niveaux variables d'autonomie et d'adaptativité après déploiement.

[^11]: PRD §7.3, **F-27** (niveau [B], texte officiel consulté sur LégisQuébec) — renvoi au ch. 11. Article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (P-39.1), en vigueur depuis le 22 septembre 2023. Trois obligations pour une « décision fondée exclusivement sur un traitement automatisé » de renseignements personnels : (1) **informer** la personne au plus tard au moment de la décision — obligation proactive, sans demande ; (2) **sur demande**, communiquer les renseignements utilisés, « les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision » ; (3) donner « l'occasion de présenter ses observations à un membre du personnel de l'entreprise en mesure de réviser la décision ». Formule officielle citée, non paraphrasée (glossaire §D.5).

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps = 2 322 mots, tolérance ±10 % de 2 400)
     2. Traçabilité (CA-1, CA-5) . fait (11 notes, numérotation séquentielle vérifiée ; termes anglais en italique entre
                                   parenthèses à la 1re occurrence : PPCDA, Digital Safety and Data Protection Commission
                                   of Canada, model risk ; citation verbatim en anglais, attribuée nominativement à AIMag).
                                   La glose « decision based exclusively on automated processing » a été RETIRÉE le
                                   17 juill. 2026 — voir 6. [M-08]. CA-5 reste conforme sans elle : le socle ne porte
                                   aucun libellé anglais pour l'art. 12.1, et la grille CA-5 pose que « Aucune traduction
                                   n'est inventée — c'est la bonne réponse ».
     3. Balayage garde-fous ...... fait (§D.7 : aucune occurrence de « C-36, la loi canadienne sur l'IA » dans le corps —
                                   la seule mention restante est le libellé du garde-fou en en-tête ; §8.2.4 : formulation
                                   imposée rendue dans sa substance au corps ET en note — attestation de reprise « mot
                                   pour mot » RECTIFIÉE le 17 juill. 2026, voir 6. [m-17] ; réserve F-25 : motif
                                   « en attente|en projet » balayé — aucune occurrence près de l'AMF ; R-7 : motif « E-23 »
                                   ressort en contexte réglementaire pur, sans objet — filtrage prévu par PRDPlan §4.3 ;
                                   R-8 : aucune occurrence de « ACP » ni de « control plane » dans ce chapitre)
     4. Relecture adversariale ... fait (deux relecteurs indépendants ; 8 constats bloquants et 12 réserves, tous vérifiés
                                   fondés au socle et tous appliqués). Ce que la relecture a réfuté dans le premier jet :
                                   - Contrefactuels non tracés présentés comme faits : « les régimes sectoriels sont plus
                                     exigeants que ce qu'un régime horizontal aurait imposé » (le socle ne documente AUCUNE
                                     obligation de la LIAD) et l'énumération de ses dispositifs supposés (classes de risque,
                                     évaluation d'incidence, sanctions). Supprimés — l'ouvrage ne compare la LIAD à rien.
                                   - Causalité affirmée sans socle : « la LIAD n'est pas tombée pour ses propres défauts »,
                                     « n'a pas été rejetée sur le fond ». Le socle établit la concomitance des deux volets à
                                     la prorogation, pas la causalité. Ramené au fait ; la lecture causale est marquée.
                                   - Auto-contradiction de l'encadré de lacune : la question était double (libellé ET
                                     périmètre) alors que §10.3 propose une inférence sur le périmètre. Question restreinte
                                     au seul libellé (option la plus réversible) ; l'inférence de périmètre reste en §10.3,
                                     marquée « Lecture de l'auteur ». Périmètre de la question consigné en note.
                                   - Attribution gonflée (CA-3) : « les analyses juridiques convergent sur une formule » +
                                     note affirmant une corroboration Fasken/DLA Piper/Canadian Lawyer de la citation G7.
                                     Fabrication : le rapport de revalidation l'attribue à AIMag seul. Attribué nominativement.
                                   - Inflation du périmètre de F-26 : la doctrine ACVM (lois sur les VALEURS MOBILIÈRES
                                     existantes) était étendue au « droit général » entier. Bornée à sa source ; la
                                     généralisation est marquée « Lecture de l'auteur ».
                                   - Empiétement sur le ch. 14 : paragraphe + note dédiés à F-11 (hors socle assigné) pour
                                     un rapprochement dont le chapitre concluait lui-même qu'il ne fonde rien. Supprimé,
                                     réduit à une incise de veille en §10.3.
                                   - Méta-discours (« règle de rédaction qui vaut pour tout l'ouvrage ») : la monographie ne
                                     se commente pas elle-même, et c'était la seule occurrence verbatim du terme proscrit
                                     §D.7 dans le corps. Retiré ; la règle vit à l'Annexe D.
                                   - Écarts de fidélité au socle corrigés : « trois volets qui touchent l'IA » → seul le
                                     volet de transparence est qualifié d'IA par F-24 ; « deuxième lecture un mois plus
                                     tard » → date d'observation, pas d'événement ; art. 12.1 → l'information est PROACTIVE,
                                     seules l'explication et la révision sont « sur demande » (F-27) ; formule officielle
                                     mise entre guillemets (§D.5) ; « E-23 ne nomme ni l'agentique ni les agents » →
                                     formulation §8.2.4 mot pour mot, « orchestration » rétabli ; « acquis » transféré des
                                     analystes aux institutions (F-09 + TOC ch. 9) ; « trois régimes sectoriels » → quatre
                                     instruments, l'art. 12.1 relevant du droit général québécois ; trois affirmations sans
                                     note en §10.1 → notées, et le membre faux (« les protocoles ont atteint leurs premières
                                     versions stables pendant ce vide » — MCP est de nov. 2024, antérieur au vide) corrigé
                                     au seul A2A, dont le socle porte le jalon.
                                   - Décompte de durée de l'art. 12.1 retiré (axe central du ch. 11, TOC).
     4bis. Passe de correction F-09 (16 juill. 2026) : note [^4] remarquée [A/B mixte] avec la strate réellement
                                   mobilisée (strate [A] seule — aucune exigence opératoire citée ici) ; corrections 2, 3 et 4
                                   sans objet (aucune affirmation d'absence d'extraction, aucune modalité « exigé par E-23 »,
                                   aucune occurrence de « fiche de modèle »).
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     6. Passe de conformité (17 juill. 2026, suites de l'audit) — périmètre strictement correctif, aucune information
                                   nouvelle, date de gel INCHANGÉE (16 juillet 2026) :
                                   - [M-08] §10.3 : glose anglaise « (*decision based exclusively on automated
                                     processing*) » RETIRÉE. F-27 ne porte que le texte français (LégisQuébec) ; le
                                     ch. 13 a arbitré que cette glose « exige une élévation par consultation primaire
                                     […] elle ne peut pas être rendue par l'auteur », et aucune élévation n'a été
                                     conduite. Ne pas la re-fabriquer : le socle ne la porte toujours pas.
                                   - [m-16] §10.3 : « que les institutions doivent traiter comme acquise » était une
                                     recommandation assertée sans marqueur. F-09 établit que les ANALYSTES tiennent la
                                     couverture pour acquise. Le membre est rendu au socle et la recommandation marquée
                                     « Lecture de l'auteur » (libellé imposé, PRDPlan §4.4), avec renvoi au ch. 9 §9.3
                                     qui la porte. Le transfert « acquis » analystes -> institutions, opéré en relecture
                                     le 16 juill. 2026 (voir 4., dernier tiret), est donc défait.
                                   - [m-17] Note [^4] et étape 3. ci-dessus : attestations de reprise « mot pour mot »
                                     rectifiées — la forme §4.4 a été enrichie le 16 juill. 2026, après le gel de ce
                                     chapitre. Substance NON rouverte (avertissement en tête de §4.4, 17 juill. 2026).
                                   POINT SIGNALÉ PAR LA PASSE, PUIS CORRIGÉ LE 17 JUILLET 2026 (hors constats de
                                   l'audit ; relevé par la passe corrective, non par l'audit) : la note [^4] déclarait
                                   « le présent chapitre ne mobilise que la strate [A] », alors que le corps (§10.3) et
                                   la note elle-même mobilisent la VÉRIFICATION NÉGATIVE (« E-23 n'emploie jamais
                                   “agentique”, “agents” ni “orchestration” »), que le PRD range sous [B] — l'énumération
                                   [A] étant close. Même classe que M-06 (ch. 9) et m-21 (ch. 12). La note [^4] porte
                                   désormais « Strate [B] également mobilisée ». ⚠ Ce bloc a lui-même attesté « NON
                                   CORRIGÉ » un point corrigé dans la prose — la faute cardinale du projet, reproduite
                                   dans le journal de la passe qui la corrigeait ; relevé par la relecture adversariale du
                                   17 juillet et réconcilié ici (prose et trail désormais d'accord).
     Points signalés à la gouvernance (non corrigés ici — CLAUDE.md, règle de chirurgie) :
     - TOC assigne à ce chapitre le seul socle F-24 et aucun garde-fou, alors que §10.3 (imposée par TOC) exige
       F-09, F-25, F-26 en renvoi et déclenche §8.2.4 et la réserve F-25 ; F-02, F-21 et F-27 ajoutés en renvoi par la
       rédaction. F-11, ajouté au premier jet, a été retiré par la relecture (territoire du ch. 14).
     - Le contenu article par article de C-36 n'est pas au socle et n'est pas listé aux lacunes PRD §10 : encadré ouvert ici.
     - PRD F-24 attribue la citation « only G7 nation… » à « des juristes » ; le rapport de revalidation l'attribue
       à AIMag (presse spécialisée, PRD §9.2). Divergence d'attribution à trancher au PRD — le chapitre retient
       provisoirement l'attribution la plus restrictive (AIMag).
     - F-02 qualifie A2A v1.0 de « première spécification stable » sans la dater ; §10.1 s'appuie sur l'encadrement
       (lancement avril 2025, vide toujours en cours au gel) plutôt que sur un jalon daté. Datation à obtenir en P4.1.
     - Mention de l'art. 12.1 en §10.3 : conservée avec renvoi au ch. 11 (le calcul de durée a été retiré), mais le TOC
       n'assigne pas F-27 au ch. 10. À trancher : amender le TOC (F-27 au socle du ch. 10) ou retirer la mention.
-->
