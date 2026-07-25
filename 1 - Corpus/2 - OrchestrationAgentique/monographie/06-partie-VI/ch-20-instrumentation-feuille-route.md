# Chapitre 20 — Instrumentation et feuille de route vers le 1er mai 2027

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | **F-09** (attentes d'E-23, niveau **[A/B mixte]** — **[A]** pour les faits des passes 1-2 (publication du 11 sept. 2025, entrée en vigueur du 1er mai 2027, portée, définition de « modèle », couverture agentique = inférence d'analystes), **[B]** pour les exigences opératoires extraites le 16 juill. 2026 (inventaire, cotation, documentation et Appendice 1, surveillance continue, absence de disposition transitoire) ; ce chapitre mobilise **les deux strates** — PRD v1.7) ; **F-25** (calendrier de la ligne directrice de l'AMF) ; **F-37** (propriétés, métriques et enseignements d'orchestration) ; **F-44** (watsonx.governance, Instana — inférences marquées). En **renvoi seulement** : F-10, F-29, F-34, F-35, F-36, F-42 (ch. 9, 14, 15, 6, 22) |
| Garde-fous à surveiller (PRD §8) | **§8.2.4** (couverture agentique d'E-23 : formulation imposée) ; **réserve F-09** (« attendu par E-23 », jamais « exigé » ; « documentation de modèle » / « inventaire », jamais « fiche de modèle » *à propos d'E-23*) ; **R-7** (le rapprochement entre les métriques de F-37 ou watsonx.governance et l'instrumentation d'E-23 est une **inférence d'auteur** — cas du fait négatif établi, PRDPlan §4.4) ; **réserves F-37** (préprint v1) ; **réserve F-25** (jamais « en attente » ni « en projet ») ; **R-4** et **réserve F-29** (§20.3, en renvoi) ; **R-5** (§20.3, formulation imposée) ; **§8.4** appliqué par prudence (le garde-fou est borné à la Partie VII ; ce chapitre mobilise pourtant F-44) ; motifs **R-1**, **R-2**, **R-3**, **R-6**, **R-8** : zéro occurrence |
| Volumétrie cible | ~2600 mots |

> **Thèse ([TOC.md](../../TOC.md))** : les métriques d'évaluation des orchestrations (correction, réactivité, traçabilité) sont l'instrumentation candidate des programmes E-23/AMF ; la feuille de route se séquence sur l'entrée en vigueur commune.

---

Le chapitre 18 a établi qu'aucun protocole ne répond aux attentes des trois textes dont le socle porte le contenu — E-23, l'article 12.1 et l'avis 11-348 — et que les deux autres lignes de sa matrice sont vides pour des raisons opposées, qu'il faut se garder de confondre : de la ligne directrice de l'AMF, le socle ne porte que le calendrier, et c'est le premier terme du croisement qui manque — seul vide qu'une extraction primaire comblerait ; du cadre bancaire, le socle porte bien l'exigence, mais le vide est celui du texte officiel lui-même, qui ne désigne rien — non une lacune de l'ouvrage, un état du droit, daté en §20.3[^13]. Le chapitre 19 construit les couches qui doivent compenser. Reste ce qu'E-23 attend d'un programme de risque de modèle, et qui n'est pas un schéma : des normes de fréquence, de portée et de critères, un suivi de la performance, des seuils de dépassement[^2]. Que mesure-t-on ? À quelle fréquence ? Contre quel seuil ? Une architecture qu'on ne sait pas instrumenter est une intention.

Ce chapitre soutient une proposition étroite, et il faut en énoncer l'étroitesse avant de la défendre. Les métriques que la littérature académique attache aux options d'orchestration (*orchestration options*) sont des **candidates** à l'instrumentation d'un programme de risque de modèle (*model risk*) canadien. Candidates : le mot est de l'auteur, il n'est pas au socle, et aucune source de cet ouvrage ne valide leur emploi à ce titre. Ce chapitre les présente comme telles, expose ce qui manque pour qu'elles cessent de l'être, et séquence sur le 1er mai 2027 le travail qui ne dépend, lui, d'aucune de ces réserves.

## 20.1 Des métriques académiques aux indicateurs de risque de modèle

Le point de départ est une liste. Le préprint de la TU Munich — **préprint non révisé par les pairs dont les auteurs déclarent eux-mêmes des menaces à la validité : le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration seulement** — instrumente quatre de ses cinq propriétés d'évaluation. La spécificité de tâche se mesure par la complexité cyclomatique (*cyclomatic complexity*) et la métrique ABC ; l'assurance de correction (*correctness assurance*), par la précision, le rappel et le F1 (*precision, recall, F1*) ; la réactivité, par le taux de faux négatifs (*false negative rate*, FNR) et la vitesse de réaction ; la traçabilité (*traceability / tractability*), par la correction du journal (*log correctness*)[^1]. La cinquième propriété, l'autonomie, ne dispose d'aucune métrique dans l'entrée du socle — le chapitre 5 l'a relevé et s'est interdit d'en conclure quoi que ce soit.

Le présent chapitre en retient trois : correction, réactivité, traçabilité. Ce choix n'est pas le sien — il est celui du cahier des charges qui gouverne l'ouvrage, lequel désigne ces trois-là comme instrumentation candidate des programmes de risque de modèle. La quatrième propriété instrumentée, la spécificité de tâche, n'y figure pas. **Lecture de l'auteur** : la ligne de partage paraît être celle de l'objet mesuré — la complexité cyclomatique et la métrique ABC mesurent un artefact de conception, tandis que les trois autres mesurent un comportement en exploitation, seul objet d'une surveillance continue. Le socle n'opère pas ce partage et n'en fournit pas le motif ; l'écart entre les quatre propriétés instrumentées par le préprint et les trois retenues est signalé ici plutôt que comblé.

Vient l'autre versant. Depuis l'extraction de son texte intégral, le 16 juillet 2026, le socle porte ce que la ligne directrice E-23 du Bureau du surintendant des institutions financières **attend** en matière de surveillance continue — et la modalité est contraignante : E-23 est fondée sur des principes et rédigée au conditionnel, elle attend, elle n'exige pas[^2]. Son principe 3.6 attend des normes de fréquence, de portée et de critères par palier de risque ; le suivi de la performance, de l'usage, des données d'entrée et des dépendances externes ; des seuils de dépassement ; et, verbatim, des « *processes for handling AI/ML's unique challenges, such as autonomous decision making, autonomous re-parametrization, and the elevated potential for model drift* »[^2].

Les deux listes se regardent. Il faut résister à la tentation de les superposer.

**Lecture de l'auteur** : trois rapprochements sont plausibles et aucun n'est documenté. La précision, le rappel et le F1 mesurent l'assurance de correction d'une orchestration ; E-23 attend un suivi de la performance — les deux portent sur la conformité d'un résultat à l'attendu, mais l'un est une mesure de laboratoire sur un scénario, l'autre une attente de dispositif sur un parc. La vitesse de réaction et le taux de faux négatifs mesurent la réactivité ; E-23 attend des seuils de dépassement — mais le socle ne dit pas de quelle grandeur. La correction du journal mesure la traçabilité ; E-23 attend une documentation de modèle et un inventaire dont l'Appendice 1 énumère les champs — objets d'une tout autre nature qu'un journal d'exécution. Le socle porte les deux termes de chacun de ces trois rapprochements ; il n'en porte aucun rapprochement. Ce sont des candidatures, pas des correspondances.

Une raison de fond appuie néanmoins la candidature, et il faut dire d'où elle vient. **Lecture de l'auteur**, posée au chapitre 5 et non au socle : les quatre propriétés instrumentées — spécificité de tâche comprise — sont celles qu'un exploitant peut **démontrer** à un tiers, et c'est l'instrumentation qui rend une propriété démontrable ; le socle énumère les cinq propriétés d'évaluation sans opérer ce partage[^1]. **Lecture de l'auteur** : un programme de risque de modèle est précisément un dispositif de démonstration à un tiers. La convergence d'objet est réelle ; elle ne vaut pas validation, et le socle ne l'établit pas. Qu'on la note bien : cette raison appuie les **quatre** propriétés instrumentées, la spécificité de tâche comprise, et non les trois que retient ce chapitre. Elle ne fournit donc aucun motif au partage 4 → 3 du cahier des charges, que le socle n'opère pas davantage.

Reste l'outillage. Le socle documente, chez IBM, des capacités qui portent sur les mêmes objets — inventorier, coter, surveiller. Selon la documentation d'IBM : watsonx.governance, disponibilité générale déclarée en décembre 2023, pour la gestion, la surveillance et la gouvernance des modèles — équité, biais, dérive, fiches de modèles — assortie en 2025 d'une gouvernance agentique (Evaluation Studio, Risk Atlas incluant les risques agentiques, inventaire par défaut, *Governed Agentic Catalog*) ; et, en préversion publique annoncée à Think 2026, toujours selon la documentation d'IBM, Instana AI Agent & LLM Observability — découverte automatique des agents, des modèles et de leurs dépendances, évaluations dites *LLM-as-a-judge*, visibilité par tâche[^3]. Le socle documente des capacités d'orchestration et d'exécution chez d'autres éditeurs — Microsoft Agent Framework, LangGraph, les Streaming Agents de Confluent, Temporal au niveau [C] — dont la Partie II établit le traitement ; aucune n'est ici comparée aux précédentes[^4].

Et c'est ici que le garde-fou le plus important de ce chapitre s'applique. **Le rapprochement entre watsonx.governance et E-23 est une inférence d'auteur : IBM ne revendique aucune conformité à E-23, et aucune source ne documente ce lien**[^3][^5]. La même règle vaut pour Instana. Le rapprochement entre watsonx.governance et la ligne directrice sur l'intelligence artificielle de l'AMF est, lui aussi, une inférence d'auteur[^5]. Que l'éditeur ne revendique rien à l'endroit d'E-23 n'autorise aucune généralisation : le socle atteste au contraire, par son module *Compliance Accelerators* issu d'un accord d'OEM avec Credo AI du 28 avril 2025, des contenus de conformité que l'éditeur destine à l'AI Act européen, à ISO/IEC 42001 et au NIST AI RMF[^3]. Aucun des trois n'est un texte canadien.

> **État de la recherche — la validité de ces métriques comme indicateurs de risque**
>
> Question : les métriques de correction, de réactivité et de traçabilité sont-elles valides comme indicateurs de risque de modèle en contexte financier canadien ?
>
> Lacune ouverte le 16 juillet 2026 ; **aucune passe de recherche n'a été conduite** — hors périmètre de la phase P0, qui a revalidé les faits chauds et tenté des élévations ciblées sans instruire ce point. Ce que le socle établit : les quatre propriétés instrumentées et leurs métriques, et un jeu de résultats sur un scénario d'éclairage prédictif[^1]. Que ces métriques soient, pour la plupart, empruntées à des disciplines établies — le génie logiciel, l'évaluation des classifieurs — est une lecture du chapitre 5 §5.4, non un énoncé du socle. Ce qu'il n'établit pas : aucune reproduction indépendante, aucune application documentée de la taxonomie à un processus d'institution financière, aucune validation de ces métriques comme indicateurs de risque — la sous-caractérisation est déjà portée en lacune par le cahier des charges de l'ouvrage[^6]. Sources à retrouver : arXiv:2606.31518, publications du BSIF postérieures au 16 juillet 2026. La question reste ouverte ; aucune inférence n'est proposée ici.

## 20.2 Feuille de route type : inventaire, encadrement, surveillance

Le compte à rebours est court. Du 16 juillet 2026 au 16 avril 2027, neuf mois ; puis quinze jours jusqu'au 1er mai 2027, date d'entrée en vigueur d'E-23[^2]. Il reste **neuf mois et quinze jours**, et le texte ne porte **aucune disposition transitoire**[^2]. La ligne directrice sur l'intelligence artificielle de l'AMF, finale depuis le 30 mars 2026, entre en vigueur à la même date — treize mois et un jour après sa publication[^7]. Cette convergence commande le séquencement.

**Premier mouvement — inventorier.** E-23 attend « *a comprehensive inventory of models whose inherent risk is determined to be non-negligible* », « *maintained at the enterprise level* », « *accurate, evergreen, and subject to robust controls* » ; son Appendice 1 en énumère les champs — identifiant, nom, cote de risque, propriétaire, développeur, origine, puis, pour les modèles à risque non négligeable, version, date de déploiement, réviseur, approbateur, dépendances, sources de données, usages approuvés, limites, date de revue, état de surveillance, prochaine revue[^2]. Ce premier mouvement ne dépend d'aucune des réserves de la section précédente : il est tracé au texte, il est daté, et il se conduit sans qu'aucune métrique académique n'y intervienne.

Il porte cependant une difficulté propre à notre objet, et c'est celle du périmètre. E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration — vérification mécanique sur le texte intégral, EN et FR. Sa définition de « modèle », laissée « *intentionally broad* », englobe les méthodes d'IA et d'apprentissage automatique, et le texte vise expressément la « prise de décision autonome » et la « reparamétrisation autonome » ; d'où une **couverture implicite** que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise[^8]. Le chapitre 9 en a tiré la conduite : traiter la couverture comme acquise, et documenter qu'on le fait par prudence plutôt que par obligation établie. L'inventaire est le lieu où cette prudence se paie ou s'économise.

**Deuxième mouvement — coter, puis encadrer.** E-23 attend qu'« *each model should be assigned a model risk rating* », et que la portée, l'échelle et l'intensité de la gestion du risque de modèle soient « *commensurate with* » ce risque[^2]. La cotation précède l'encadrement parce qu'elle le calibre. Vient ensuite le travail que les chapitres 13 et 19 ont défini : positionner chaque processus sur les options d'orchestration, et imposer un cadre (*frame*) déterministe à ceux qui relèvent d'une exigence stricte. **Lecture de l'auteur** : la cotation attendue par E-23 et la grille de sélection du préprint portent sur le même geste — décider combien d'encadrement mérite un processus — mais aucune source ne les relie, et les sept critères de sélection sont qualitatifs : ils orientent un jugement, ils ne calculent pas une réponse[^1]. Une institution qui voudrait industrialiser ce choix devra construire elle-même sa pondération et l'assumer comme sa propre décision.

**Troisième mouvement — surveiller.** C'est le seul des trois où l'instrumentation de la section 20.1 trouve sa place, et c'est donc le seul qui hérite de ses réserves. Un enseignement du socle y commande pourtant une décision d'architecture immédiate, et il ne dépend d'aucun chiffre : la journalisation confiée aux agents « n'est généralement pas recommandée »[^1]. **Lecture de l'auteur** : si la trace n'est pas produite par l'agent, et si E-23 attend un état de surveillance par modèle inventorié, alors le lieu de production de la trace est une décision à prendre avant le 1er mai 2027, non après. Le socle déconseille un producteur ; il n'en désigne aucun autre.

Un mot, enfin, sur ce que cette feuille de route ne peut pas faire. Elle est séquencée sur deux textes dont un seul est au socle par son contenu. Le socle ne porte de la ligne directrice de l'AMF **que son calendrier** ; son contenu article par article relève d'une lacune déclarée[^7]. **Lecture de l'auteur** : la convergence des dates rend rationnel un programme unique plutôt que deux ; elle ne dit rien de ce que le second texte attend, et cet ouvrage ne le fabriquera pas.

> **État de la recherche — ce que la ligne directrice de l'AMF attend**
>
> Question : quelles attentes opératoires la ligne directrice sur l'intelligence artificielle de l'AMF, finale depuis le 30 mars 2026 et en vigueur le 1er mai 2027, fait-elle peser sur une institution assujettie ?
>
> Lacune ouverte le 16 juillet 2026 ; **aucune passe de recherche n'a été conduite** — hors périmètre de la phase P0. Le socle ne porte que le calendrier du texte ; son contenu article par article figure parmi les lacunes déclarées de l'ouvrage[^7]. Source à retrouver : lautorite.qc.ca (texte officiel de la ligne directrice). La question reste ouverte ; aucune inférence n'est proposée ici — et notamment aucune transposition des attentes d'E-23, dont rien n'établit qu'elles coïncident au-delà de la date.

## 20.3 Les jalons externes à surveiller

Une feuille de route datée se périme par l'extérieur. Le cahier des charges de l'ouvrage impose la revalidation des faits « chauds » avant toute publication[^9] ; le chapitre 24 en fait un protocole. Cinq échéances bornent la fenêtre du présent chapitre, et elles sont proches.

**Le 28 juillet 2026 — douze jours après la date de gel.** Une révision majeure de la spécification MCP est attendue à cette date, décrite par les mainteneurs comme la plus importante depuis le lancement du protocole[^10]. Le socle n'en documente pas le contenu au regard d'une quelconque exigence canadienne.

**Le 24 août 2026 — un mois et huit jours après la date de gel.** Le règlement administratif du *Real-Time Rail* entre en vigueur[^11]. Le lancement du système, lui, demeure une cible : Paiements Canada **vise** un lancement au T4 2026, à l'issue des tests industriels en cours ; la cible a été successivement reportée — 2019, puis 2022, puis 2023, puis 2026[^11]. Le chapitre 15 en établit la chronologie.

**Le 26 août 2026 — un mois et dix jours après la date de gel.** La période de commentaires sur le règlement prépublié du cadre des services bancaires axés sur le consommateur se clôt ; le texte final peut changer[^12].

**À une date inconnue.** Au 16 juillet 2026, **aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie**[^13]. C'est le jalon dont l'échéance est la moins prévisible et la portée la plus grande pour la couche d'exposition — le chapitre 14 le traite, le chapitre 23 en instancie le flux.

**Le 1er mai 2027.** E-23 et la ligne directrice de l'AMF entrent en vigueur le même jour[^2][^7]. À la date de gel, le discours de ce chapitre est un discours de futur proche ; à la publication, il aura peut-être cessé de l'être.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, l'instrumentation proposée est une candidature et le demeure : le socle porte les métriques d'un côté, les attentes de surveillance d'E-23 de l'autre, et aucun rapprochement entre les deux — les trois rapprochements exposés en §20.1 sont de l'auteur, et la source des métriques est un préprint non révisé par les pairs dont les auteurs déclarent des menaces à la validité. **Deuxièmement**, les quatre gestes de la feuille de route sont de solidité inégale, et la gradation doit être énoncée en entier : inventorier et coter sont tracés au texte d'E-23 et ne dépendent d'aucune de ces réserves ; encadrer dépend de la taxonomie OO1–OO4, que le socle ne porte que par une source unique, préprint non révisé par les pairs, sans reproduction indépendante ni application documentée à un processus d'institution financière[^6] ; surveiller hérite en outre, intégralement, des réserves de §20.1. Une institution qui commencerait par l'instrumentation commencerait par le maillon faible. **Troisièmement**, il reste neuf mois et quinze jours à la date de gel, sans disposition transitoire, et cinq jalons externes peuvent déplacer le plan avant même qu'il soit exécuté.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas qu'un produit d'éditeur instrumente E-23 : le rapprochement entre watsonx.governance et E-23 est une inférence d'auteur, IBM ne revendique aucune conformité à E-23, et aucune source ne documente ce lien. Il ne dit pas ce que la ligne directrice de l'AMF attend — le socle n'en porte que la date. Il ne dit pas que les trois métriques retenues soient les bonnes, ni qu'elles soient suffisantes : leur validité comme indicateurs de risque n'est établie par aucune source, et la quatrième propriété instrumentée par le préprint, la spécificité de tâche, a été écartée par un partage que le socle n'opère pas. Il ne dit pas, enfin, qu'E-23 attende quoi que ce soit de l'IA agentique : elle ne la nomme jamais, et la couverture est une lecture d'analystes que ce chapitre traite comme acquise par prudence, non par obligation établie.

Une feuille de route n'est pas une preuve de conformité. C'est l'ordre dans lequel on découvre ce qu'on ne sait pas encore mesurer.

---

## Notes

[^1]: PRD §7.7, **F-37** (niveau [B] — article lu intégralement ; confiance haute pour le cadre, **moyenne pour les chiffres**). Source primaire : Rinderle-Ma, Mangler et al. (TU Munich), « Design and Implementation of Agentic Orchestrations and Orchestration of Agents », arXiv:2606.31518v1, 30 juin 2026. **Formulation imposée (PRDPlan §4.4, cas « préprint académique »)**, reproduite en ouverture de §20.1 : préprint non révisé par les pairs dont les auteurs déclarent eux-mêmes des menaces à la validité (expériences initiales, invites non comparées, facteurs confondants) — le cadre conceptuel est repris, les résultats chiffrés à titre d'illustration seulement. **Aucun résultat chiffré n'est repris dans ce chapitre.** Éléments mobilisés : les cinq propriétés d'évaluation et leur instrumentation (complexité cyclomatique et métrique ABC pour la spécificité ; précision, rappel et F1 pour la correction ; FNR et vitesse de réaction pour la réactivité ; correction du journal pour la traçabilité) ; **l'absence de métrique quantitative pour l'autonomie dans l'entrée du socle** (constat sur l'entrée, non sur l'article — ch. 5 note [^5]) ; les **sept critères qualitatifs de sélection**, sans pondération ni fonction de score ; l'enseignement « la journalisation confiée aux agents n'est généralement pas recommandée ». **Point de vigilance appliqué en §20.1 (relecture adversariale)** : le partage des cinq propriétés entre celles qu'un exploitant *démontre* à un tiers (les quatre instrumentées) et l'autonomie **n'est pas au socle** — F-37 énumère les cinq propriétés sans les répartir. Ce partage est une **construction du présent ouvrage**, posée au **ch. 5 §5.2** sous « Lecture de l'auteur » et reprise ici sous le même marqueur : un chapitre de synthèse cite le socle, jamais la lecture qu'un chapitre antérieur en faisait. De même, l'origine disciplinaire des métriques (génie logiciel ; évaluation des classifieurs) est une observation du **ch. 5 §5.4**, non un énoncé de F-37 — d'où son retrait de la liste « ce que le socle établit » de l'encadré de §20.1. Traitement complet : ch. 5.

[^2]: PRD §7.3, **F-09** (niveau **[A/B mixte]**, marquage rectifié le 16 juillet 2026 — PRD v1.7). L'entrée porte **deux strates de preuve**, et ce chapitre les mobilise toutes deux : **[A]** (vote adversarial 3-0, passes 1-2) pour les faits de date, de portée et de définition — publication du 11 septembre 2025, entrée en vigueur du 1er mai 2027, définition de « modèle » incluant les méthodes d'IA/AA, couverture agentique tenue pour une inférence d'analystes ; **[B]** (extraction du texte intégral, EN et FR, le 16 juillet 2026, lecture directe de la source officielle sans vote adversarial) pour les **exigences opératoires** — inventaire, cotation, documentation et Appendice 1, surveillance continue, absence de disposition transitoire, re-vérification mécanique de la vérification négative. §20.2 en entier repose sur cette seconde strate. **Une extraction de source primaire n'« élève » pas une entrée déjà votée 3-0 : [B] est *sous* [A] dans la taxonomie de PRD §7 — elle l'enrichit d'un contenu de rang inférieur.** La formule « élevée [C]→[B] », portée par le premier jet de ce chapitre, est doublement fausse (l'entrée n'a jamais été [C], et [B] n'est pas une élévation) et rectifiée ici. Source primaire : osfi-bsif.gc.ca, ligne directrice E-23 « Gestion du risque de modélisation (2027) », version finale du 11 septembre 2025, **en vigueur le 1er mai 2027**, applicable aux institutions financières fédérales ; lettre d'accompagnement du 11 septembre 2025. **Réserve F-09, contraignante dans tout ce chapitre (PRDPlan §4.4)** : E-23 est **fondée sur des principes** et rédigée au conditionnel (« *should* ») — écrire « attendu par E-23 », jamais « exigé par E-23 » ; écrire « documentation de modèle » et « inventaire », jamais « fiche de modèle » (0 occurrence dans E-23, EN et FR). Faits mobilisés, verbatim : **inventaire** (§C.1, principe 2.1) — « *a comprehensive inventory of models whose inherent risk is determined to be non-negligible* », « *maintained at the enterprise level* », « *accurate, evergreen, and subject to robust controls* » ; **Appendice 1 « Information tracking for models »** (champs minimaux, puis champs additionnels pour les modèles à risque non négligeable) ; **cotation graduée** (§A.3, §C.2, principes 2.2-2.3) — « *Each model should be assigned a model risk rating* », portée « *commensurate with* » le risque ; **surveillance continue** (§D.2, principe 3.6) — normes de fréquence, portée et critères par palier de risque, suivi de la performance, de l'usage, des données d'entrée et des dépendances externes, seuils de dépassement, « *processes for handling AI/ML's unique challenges, such as autonomous decision making, autonomous re-parametrization, and the elevated potential for model drift* » ; **aucune disposition transitoire dans le texte** (le « 18 mois de transition » relève du commentaire secondaire — ne pas l'affirmer). Le **cycle de vie à cinq volets** (§A.4, « *not necessarily sequential* ») est mobilisé par renvoi au ch. 9 et n'est pas exposé ici. Décompte revérifié à la rédaction : 16 juillet 2026 → 16 avril 2027 = neuf mois ; + quinze jours = 1er mai 2027, soit **289 jours** — concordant avec les ch. 9, 11, 14 et 18.

[^3]: PRD §7.8, **F-44** (niveau [B]). Sources : newsroom.ibm.com (14 novembre 2023) ; ibm.com/new (extraits indexés — les pages www.ibm.com refusent le fetch automatisé, 403 : réserve transversale de PRD §7.8) ; credo.ai (28 avril 2025, primaire). Faits mobilisés, **tous attribués à la documentation de leur éditeur** (§8.4.1) : **watsonx.governance**, disponibilité générale déclarée en décembre 2023 — gestion, surveillance et gouvernance des modèles (équité, biais, dérive, fiches de modèles) ; **gouvernance agentique** livrée en 2025 (aperçu en mars, version en juin) — Evaluation Studio, Risk Atlas incluant les risques agentiques, inventaire par défaut, *Governed Agentic Catalog* ; add-on **Compliance Accelerators** (accord OEM avec Credo AI, 28 avril 2025) — contenus de conformité prêts pour **l'AI Act européen, ISO/IEC 42001 et le NIST AI RMF** ; **Instana AI Agent & LLM Observability**, préversion publique annoncée à Think 2026 — découverte automatique des agents, modèles et dépendances, évaluations *LLM-as-a-judge*, visibilité par tâche. **Réserve capitale de F-44, appliquée en §20.1 et en conclusion** : *aucune source ne relie watsonx.governance à E-23 du BSIF — le parallèle (inventaire de modèles, évaluation graduée des risques, cycle de vie) est une inférence d'auteur à formuler comme telle*. Le terme « fiches de modèles » est **exact pour ce produit** et ne contredit pas la réserve F-09, qui proscrit de prêter ce vocabulaire à E-23 (note [^2]). Traitement : ch. 22 (couche C6) et ch. 23 (tableau B.3).

[^4]: PRD §8.4 (neutralité fournisseur). Le garde-fou est **borné par son propre libellé à la Partie VII et à l'Annexe B** ; le présent chapitre est en Partie VI mais mobilise F-44, et l'applique donc par prudence : (1) chaque groupe de capacités est attribué **dans le corps** à la documentation d'IBM, avec sa date et son statut (GA, préversion) — l'attribution est exécutée à chaque occurrence, non déclarée par une phrase de clôture (défaut relevé en relecture adversariale) ; (2) les alternatives non-IBM du socle sont **nommées dans le corps** (Microsoft Agent Framework — F-15 ; LangGraph Platform — F-32 ; Streaming Agents de Confluent — F-33 ; Temporal, niveau [C]) et leur traitement renvoyé à la **Partie II** (ch. 7) ; (3) aucune formulation de supériorité n'est employée ; (4) les faits négatifs du socle sont exposés au même titre que les capacités (R-7, note [^5]). **Le portefeuille IBM est un cas d'instanciation documenté par sources primaires, pas une recommandation.** Aucune étude d'analyste commandée n'est citée dans ce chapitre (§8.2.7 sans objet) ; le positionnement d'IBM comme *agentic control plane* (F-42, R-8 branche c) n'est pas mobilisé ici — ch. 22 §22.2.

[^5]: PRD §8.1, garde-fou **R-7** : « watsonx.governance est conforme à E-23 » / « IBM Cloud satisfait B-13 » sont des affirmations **interdites** (CA-2) ; aucun lien documenté IBM↔E-23/B-13 (F-44, F-45). **Deux formulations distinctes de PRDPlan §4.4 sont appliquées ici, et l'une ne doit pas contaminer l'autre.** (a) *Cas du fait négatif établi* (E-23, B-13), repris mot pour mot en §20.1 et en conclusion : « Le rapprochement entre [composant] et [exigence] est une **inférence d'auteur** : [éditeur] ne revendique aucune conformité à [exigence], et aucune source ne documente ce lien. » (b) *Cas général* (toute autre exigence — ici la ligne directrice de l'AMF) : « Le rapprochement entre [composant] et [exigence] est une **inférence d'auteur**. » — **sans y ajouter « ne revendique aucune conformité »** : ce fait négatif n'est vérifié que pour E-23 et B-13, et F-44 atteste au contraire des revendications de l'éditeur pour l'AI Act européen, ISO/IEC 42001 et le NIST AI RMF (note [^3]). Substitut terminologique imposé : Annexe D §D.7 (« conforme à E-23 » → « correspondance établie par inférence d'auteur »).

[^6]: PRD §10.10 (lacune ouverte le 16 juillet 2026, à la rédaction des ch. 5 et 6) : la taxonomie OO1–OO4 repose sur **une source unique**, préprint v1 non révisé par les pairs, **sans reproduction indépendante ni application documentée à un processus d'institution financière** ; le socle ne retient aucune métrique quantitative pour la propriété d'autonomie. Le constat que le socle n'établit pas la validité des métriques comme indicateurs de risque en contexte financier est posé au **ch. 5 §5.4**. Gabarit d'encadré : PRDPlan §4.4, **cas 2** (lacune non instruite) — aucune passe de recherche n'a été conduite pour ce chapitre, et le cas 1 ne serait employable que si une passe traçable avait eu lieu.

[^7]: PRD §7.3, **F-25** (niveau [A]). Sources : lautorite.qc.ca (document de consultation) ; Norton Rose Fulbright ; rapport annuel Desjardins 2025. Projet publié le 3 juillet 2025 (consultation close le 7 novembre 2025) ; **version finale publiée le 30 mars 2026, en vigueur le 1er mai 2027** — même date qu'E-23. **Réserve F-25 appliquée** : ne jamais écrire « en attente » ni « en projet » (Annexe D §D.7). **Le socle ne porte que le calendrier** ; le contenu article par article relève de la lacune **PRD §10.4**, d'où l'encadré de §20.2. Décompte posé à la rédaction : 30 mars 2026 → 30 avril 2027 = treize mois ; + un jour = 1er mai 2027, soit **treize mois et un jour**. Traitement : ch. 11.

[^8]: PRD §8.2.4 (règle d'attribution : la couverture agentique d'E-23 est une **inférence d'analystes juridiques** — jamais « le BSIF exige pour l'IA agentique », toujours « couverture implicite via la définition de modèle »). **Formulation imposée par PRDPlan §4.4**, reproduite intégralement en §20.2, ses cinq membres compris : la vérification mécanique sur le texte intégral EN et FR (« agentique »/« agentic » = 0 ; « agent(s) » = 0 ; « orchestration » = 0 ; « autonom\* » = 8) ; la définition laissée « *intentionally broad* » ; la visée expresse de la « prise de décision autonome » et de la « reparamétrisation autonome » ; la couverture implicite ; les cinq analystes nommés. **Ce que le socle établit est un état de l'opinion juridique canadienne, non un état du droit** — développement et statut des cinq analystes (quatre relèvent du corpus de corroboration secondaire admise, PRD §9.2 ; Sookman n'en est pas ; l'indépendance de leurs analyses n'est pas établie) : **ch. 9 §9.3**. Aucun argument du présent chapitre n'en dépend au-delà du périmètre d'inventaire.

[^9]: PRD §8.3 (sensibilité temporelle) : chaque chapitre porte sa date de gel ; revalidation complète des faits chauds avant publication. Protocole opérationnel : PRDPlan **P4.1** ; exposition : **ch. 24 §24.2** (événements de péremption). *La clôture de l'acquisition Confluent, fait chaud jusqu'en P0, est résolue (17 mars 2026, F-41) et ne figure plus dans cette liste.* La trajectoire du projet de loi **C-36** (F-24) figure aux faits chauds mais n'est pas un jalon de ce chapitre : c'est une réforme de la protection des renseignements personnels portant des volets IA, non une loi IA autonome — ch. 10.

[^10]: PRD §7.1, **F-01** (niveau [A]), fait chaud à resurveiller en P4.1. Spécification MCP en vigueur à la date de gel : révision **2025-11-25** (modelcontextprotocol.io), revalidée le 16 juillet 2026. Une *release candidate* verrouillée le 21 mai 2026 (refonte sans état, retrait de `Mcp-Session-Id`) est prévue en finalisation le **28 juillet 2026**, décrite par les mainteneurs comme la plus importante révision depuis le lancement. Rapport : `verification/revalidation-2026-07-16.md`. Décompte revérifié : 16 → 28 juillet 2026 = **douze jours** (concordant avec les ch. 2, 4 et 18). **Réserve F-01** : dire « cadre d'autorisation », jamais « sécurisé » — non mobilisé ici.

[^11]: PRD §7.4, **F-29** (niveau [A]) — **renvoi seulement**, traitement au **ch. 15**. Sources primaires : payments.ca (page RTR vérifiée le 16 juillet 2026). By-law No. 10 (Gazette du Canada, partie II, 1er juillet 2026) **en vigueur le 24 août 2026** ; décompte posé à la rédaction : 16 juillet → 24 août 2026 = **un mois et huit jours** (39 jours). **Double garde-fou appliqué** : **R-4** — la cible officielle du T4 2026 **est** annoncée, ne pas écrire « aucune date annoncée » ; **réserve F-29** — le T4 2026 reste une **cible** conditionnelle au succès des tests industriels en cours, le système n'est pas en production à la mi-juillet 2026 : ne pas écrire « lancé » ni « en production ». Formulation imposée (PRDPlan §4.4, cas « cible vs fait accompli ») reprise mot pour mot : les dates citées sont les **cibles successives** (2019, 2022, 2023, 2026), non les dates auxquelles les reports ont été décidés.

[^12]: PRD §7.4, **F-34** (niveau [A]) — **renvoi seulement**, traitement au **ch. 14**. Règlement **prépublié** dans la Gazette du Canada, partie I, vol. 160, no 26, le 27 juin 2026 ; période de commentaires de 60 jours close le **26 août 2026** ; entrée en vigueur échelonnée (accréditation d'abord). Décompte posé à la rédaction : 16 juillet → 26 août 2026 = **un mois et dix jours** (41 jours). Le texte final peut changer (PRD §8.3).

[^13]: PRD §7.4, **F-35** (niveau [A] — **fait négatif vérifié 9-0**) et PRD §8.1, garde-fou **R-5** (« FDX est le standard technique retenu pour le cadre bancaire canadien » = affirmation interdite, CA-2). Sources primaires : gazette.gc.ca ; canada.ca (communiqué de Finances Canada, page Budget 2025) ; bankofcanada.ca. **Formulation du fait négatif imposée par PRDPlan §4.4** et reprise mot pour mot en §20.3. Recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » dans le règlement prépublié, le communiqué et la page Budget 2025 : zéro occurrence ; reconduit par la passe de revalidation du 16 juillet 2026 (`verification/revalidation-2026-07-16.md`). Lacune **PRD §10.1** (ouverte). Traitement : **ch. 14** ; flux : **ch. 23 §23.4**.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026). Volumétrie : cible 2600 ±10 % = 2340-2860.
                                   Ce chapitre ne porte AUCUN tableau de corps — l'ambiguïté de décompte
                                   relevée au ch. 18 est sans objet ici. Corps de prose seul (en-tête,
                                   exergue de thèse, notes et commentaires exclus ; encadrés de lacune
                                   INCLUS, leur contenu étant exigé par CA-6) : **2782 mots** — CONFORME
                                   (+7,0 % sur la cible ; marge de 78 mots sous le plafond de 2860).
                                   DÉCOMPTE MESURÉ, non estimé, RECOMPTÉ APRÈS RELECTURE ADVERSARIALE :
                                   le jet fusionné mesurait 2566 ; les correctifs de la relecture (bornage
                                   du renvoi ch. 18, marquage de la prémisse du ch. 5, gradation à quatre
                                   gestes en conclusion, attribution par groupe et nomination des
                                   alternatives) ajoutent 216 mots de CONTENU tracé au socle. Aucun
                                   remplissage. LEÇON tenue : ne jamais écrire un décompte qu'on n'a
                                   pas posé.
                                   Commande reproductible (F = ce fichier) :
                                     awk '/^> \*\*Thèse/{f=1;next} /^## Notes/{f=0} f' F \
                                       | grep -v '^#' | wc -w
     2. Traçabilité (CA-1, CA-5) . fait (13 notes). Tout fait central tracé : F-09 (attentes d'E-23, verbatim),
                                   F-25 (calendrier AMF), F-37 (métriques et enseignements), F-44 (capacités
                                   d'éditeur) ; F-01, F-29, F-34, F-35 mobilisés en §20.3 comme jalons ;
                                   F-10, F-36, F-42, F-45, F-46 NON mobilisés (renvois secs ou hors périmètre).
                                   NIVEAUX DE PREUVE VÉRIFIÉS entrée par entrée : F-09 est **[A/B mixte]**
                                   (marquage rectifié le 16 juill. 2026, PRD v1.7 — [A] pour les faits des
                                   passes 1-2, [B] pour les exigences opératoires extraites ; §20.2 repose sur
                                   la strate [B], les dates de §20.3 sur la strate [A]). [B] N'EST PAS UNE
                                   ÉLÉVATION : il est SOUS [A] (§7 — [A] = vote adversarial 3-0 ; [B] = source
                                   primaire lue sans vote), et une extraction ENRICHIT une entrée votée 3-0
                                   d'un contenu de rang inférieur. Le jet initial écrivait « élevée [C]->[B],
                                   PRD v1.6 » : faux deux fois (l'entrée n'a jamais été [C]), corrigé.
                                   F-37 et F-44 [B] ; F-01, F-25, F-29, F-34, F-35 [A].
                                   POINT CRITIQUE : ce chapitre est rédigé sur F-09 dans sa version courante
                                   (texte intégral extrait), NON sur la lecture qu'en faisait le ch. 9 —
                                   lequel a été rédigé AVANT l'extraction et écrit encore que « le socle ne
                                   porte pas le libellé verbatim ».
                                   C'est la leçon explicite du ch. 18 : un chapitre de synthèse cite le SOCLE,
                                   pas la lecture qu'un chapitre antérieur en faisait à une version antérieure.
                                   Le ch. 20 figure d'ailleurs à la « Dette de correction post-P3 » de
                                   PRDPlan §1.4 comme chapitre À BALAYER : la dette est sans objet pour ce jet.
                                   Termes anglais entre parenthèses et en italique à la 1re occurrence du
                                   chapitre : orchestration options, model risk, cyclomatic complexity,
                                   correctness assurance, precision/recall/F1, false negative rate,
                                   traceability / tractability, log correctness, frame — NEUF termes.
                                   « correctness assurance » et « traceability / tractability » (Annexe D
                                   §D.2) MANQUAIENT au jet fusionné : omission relevée en relecture
                                   adversariale et corrigée en §20.1 (CA-5).
                                   Citations verbatim d'E-23 conservées en langue originale (CA-5).
                                   Marqueur d'inférence : « Lecture de l'auteur », forme unique imposée par
                                   PRDPlan §4.4 — **7 occurrences au corps** après relecture, recomptées
                                   par extraction (§20.1 : 4 — partage 4->3 propriétés, les 3 rapprochements,
                                   la PRÉMISSE de démonstrabilité reprise du ch. 5 §5.2 [AJOUTÉE en
                                   relecture : elle passait nue, en fait de chapitre], la convergence
                                   d'objet ; §20.2 : 3 — cotation vs grille, lieu de la trace, convergence
                                   des dates). Le jet fusionné en portait 6 ; l'étape 4 de ce journal en
                                   annonçait 7 alors que 6 étaient posées — CONTRADICTION INTERNE relevée
                                   en relecture, désormais sans objet : les deux étapes disent 7, mesuré.
                                   « Inférence d'auteur » (forme du PRD pour qualifier un LIEN) est employée
                                   pour les rapprochements produit ↔ réglementation de §20.1, conformément
                                   à R-7 et à la note [^5] — les deux formes ne sont pas interchangeables.
     3. Balayage garde-fous ...... fait :
                                   - R-7 (motif « E-23|B-13 ») : « E-23 » ressort massivement. Occurrences
                                     INSPECTÉES UNE À UNE et triées en deux classes. (i) Contexte réglementaire
                                     pur (§20.2 en entier, §20.3) : filtré, PRDPlan §4.3. (ii) Correspondance
                                     produit ↔ réglementation (§20.1 et conclusion) : R-7 ARMÉ, formulation du
                                     CAS BORNÉ reprise mot pour mot, deux fois. « B-13 » : 0 occurrence au corps.
                                     PIÈGE ÉVITÉ : le cas général (AMF) a été formulé SANS le fait négatif —
                                     y ajouter « IBM ne revendique aucune conformité » aurait été FAUX, F-44
                                     attestant des revendications pour l'AI Act européen, ISO/IEC 42001 et le
                                     NIST AI RMF. Les deux cas sont distingués en note [^5] et dans le corps.
                                   - réserve F-09 (motif « exigé par E-23|E-23 impose|exigence.*E-23|fiche de
                                     modèle|model card ») : « exigé par E-23 » / « E-23 impose » = 0.
                                     « fiche de modèle » à propos d'E-23 = 0 ; « documentation de modèle » et
                                     « inventaire » employés. « fiches de modèles » apparaît UNE fois, en §20.1,
                                     à propos du PRODUIT watsonx.governance : EXACT (F-44), et distingué en
                                     note [^3] — la réserve F-09 proscrit de prêter ce terme au BSIF, pas de
                                     l'employer là où l'éditeur l'emploie (PRDPlan §1.4, « ne pas sur-corriger »).
                                     MOTIF « opposable » AJOUTÉ au balayage (relecture adversariale) : le jet
                                     fusionné écrivait « E-23 devient opposable » (§20.2) et « E-23 et la
                                     ligne directrice de l'AMF deviennent opposables » (§20.3) — SURQUALIFICATION
                                     JURIDIQUE : le socle écrit « en vigueur », jamais « opposable », et la
                                     modalité au conditionnel d'E-23 rend précisément l'exigibilité discutable.
                                     Pour l'AMF la faute était double, le chapitre déclarant deux fois que le
                                     socle n'en porte QUE le calendrier. Les balayages « exigé par E-23 » et
                                     « E-23 impose » n'avaient pas vu que la modalité revenait par un ADJECTIF.
                                     Corrigé sur la forme du socle. Occurrences de « opposab* » au corps : **0**
                                     (la 3e du jet fusionné, « rend une propriété opposable » en §20.1, autre
                                     sens, réécrite en « démontrable » par prudence). Récidive du dépôt : ch. 11
                                     (« (h) SURQUALIFICATION JURIDIQUE ») et ch. 17 (« et donc opposable »).
                                     Modalité vérifiée phrase à phrase, ADJECTIFS COMPRIS : E-23 « attend », partout.
                                     « exigé par E-23 » / « E-23 impose » au corps = 0 (3 et 2 occurrences en
                                     notes et journal : citations du garde-fou lui-même).
                                   - §8.2.4 : formulation imposée reproduite INTÉGRALEMENT en §20.2, ses cinq
                                     membres vérifiés un à un contre PRDPlan §4.4 (« ni l'orchestration » ;
                                     vérification mécanique EN et FR ; « intentionally broad » ; visée expresse
                                     de la décision et de la reparamétrisation autonomes ; couverture implicite).
                                     Aucune occurrence de « E-23 exige pour l'agentique » (Annexe D §D.7).
                                   - réserves F-37 : formulation « préprint » de PRDPlan §4.4 posée en ouverture
                                     de §20.1 et rappelée en conclusion. AUCUN chiffre de F-37 n'est repris —
                                     ni les F1 (0,40 / 0,97 / 1,00), ni aucun autre : le chapitre porte sur les
                                     métriques comme instruments, non sur les résultats.
                                   - réserve F-25 (motif « en attente|en projet ») : 0 occurrence fautive ;
                                     forme datée employée (« finale depuis le 30 mars 2026, en vigueur le
                                     1er mai 2027 »).
                                   - R-4 + réserve F-29 (motifs « RTR|Real-Time Rail|T4 2026 ») : **2 occurrences**
                                     au corps, mesurées et non estimées (« Real-Time Rail » 1 ; « T4 2026 » 1 ;
                                     le sigle « RTR » n'apparaît pas au corps, la forme longue étant glosée en
                                     §20.3) — le premier jet de ce journal annonçait 3 : faux, corrigé.
                                     Toutes inspectées. La cible T4 2026 est dite ANNONCÉE (R-4) et
                                     dite CIBLE conditionnelle (F-29) dans la MÊME phrase ; « lancé » et « en
                                     production » = 0. Formulation §4.4 (« cible vs fait accompli ») reprise mot
                                     pour mot, y compris la précision que 2019/2022/2023/2026 sont les cibles
                                     successives et non les dates de report.
                                   - R-5 (motif « FDX|Financial Data Exchange|standard technique ») :
                                     **1 occurrence** au corps, mesurée (« FDX », §20.3 ; « standard technique »
                                     n'apparaît pas, la formulation imposée disant « aucun organisme de
                                     normalisation technique n'a été désigné […] et aucun standard n'est
                                     nommé ») — le premier jet de ce journal annonçait 2 : faux, corrigé.
                                     Inspectée : FDX n'apparaît jamais comme standard retenu, mais comme
                                     commentaire d'industrie ; formulation imposée §4.4 reprise mot pour mot.
                                   - §8.4 (neutralité fournisseur) : le garde-fou est BORNÉ par son libellé à
                                     la Partie VII et à l'Annexe B — ce chapitre est en Partie VI. Appliqué
                                     malgré tout, F-44 étant mobilisé (note [^4]) : attribution datée et statuée,
                                     alternatives NOMMÉES au corps puis renvoyées à la Partie II, aucun
                                     superlatif, faits négatifs (R-7) exposés au même titre que les capacités.
                                     AUTO-CERTIFICATION SUPPRIMÉE (relecture adversariale) : le jet fusionné
                                     clôturait §20.1 par une phrase DÉCLARANT au lecteur que §8.4 était
                                     respecté (« Ces capacités sont attribuées à la documentation de leur
                                     éditeur… ; ce chapitre n'énonce aucun verdict comparatif ») au lieu de
                                     l'EXÉCUTER : seule la GA de watsonx.governance portait « selon IBM », la
                                     gouvernance agentique de 2025 et la préversion Instana n'avaient que leur
                                     date, l'éditeur était anonyme à l'ouverture (« chez un éditeur »), et
                                     aucune alternative n'était nommée. §8.4(1) porte sur CHAQUE capacité, pas
                                     sur une phrase de clôture. Corrigé : IBM nommé dès la 1re occurrence,
                                     « selon la documentation d'IBM » sur les DEUX groupes datés, alternatives
                                     du socle nommées au corps (F-15, F-32, F-33, Temporal [C]). La phrase de
                                     conformité appartient à ce journal, pas au corps. §8.2.7 (« Forrester|TEI|
                                     Celent|ROI ») : 0 occurrence — aucune étude commandée citée.
                                   - §D.6 (homonymie « garde-fou » / *guardrails*) : SANS OBJET — les Granite
                                     Guardian (F-42) ne sont pas mobilisés ; « garde-fou » n'apparaît au corps
                                     qu'au sens des règles R-x du PRD.
                                   - R-1, R-8 (motifs « ACP », « control plane », « plan de contrôle ») :
                                     0 occurrence au corps — aucune des quatre branches n'est mobilisée ;
                                     le sigle nu est impossible par construction.
                                   - R-2, R-3, R-6 : 0 occurrence. §8.2.2 / §7.5 (métriques institutionnelles) :
                                     SANS OBJET — aucune métrique d'institution canadienne. §8.2.6 (« 70 % ») :
                                     0 occurrence — la projection du BSIF-ACFC relève du ch. 9 et n'est pas
                                     reprise.
     4. Arithmétique ............. tous les décomptes posés à partir des dates du socle, aucun repris d'un autre
                                   chapitre sans recalcul :
                                   - 16 juill. 2026 -> 1er mai 2027 : 16 juill. -> 16 avril 2027 = neuf mois ;
                                     + quinze jours = 1er mai. NEUF MOIS ET QUINZE JOURS (289 j). Recalculé ;
                                     concordant avec les ch. 9, 11, 14 et 18.
                                   - 30 mars 2026 -> 1er mai 2027 (F-25) : -> 30 mars 2027 = 12 mois ;
                                     -> 30 avril 2027 = 13 mois ; + 1 j = 1er mai. TREIZE MOIS ET UN JOUR.
                                     Décompte NOUVEAU (aucun chapitre antérieur ne le pose).
                                   - 16 -> 28 juill. 2026 (F-01) : DOUZE JOURS. Concordant ch. 2, 4, 18.
                                   - 16 juill. -> 24 août 2026 (F-29, By-law no 10) : 15 j (fin juillet, 31 j)
                                     + 24 = 39 jours = UN MOIS ET HUIT JOURS. Recalculé deux fois.
                                   - 16 juill. -> 26 août 2026 (F-34) : 15 + 26 = 41 jours = UN MOIS ET DIX
                                     JOURS. Recalculé deux fois.
                                   - 5 jalons annoncés en §20.3 : recomptés — 28 juill. 2026, 24 août 2026,
                                     26 août 2026, arrêté de désignation (date inconnue), 1er mai 2027 = 5.
                                     Repris à l'identique en conclusion. CONFORME.
                                   - 3 métriques retenues (correction, réactivité, traçabilité) sur 4 propriétés
                                     instrumentées par F-37 (la 4e étant la spécificité de tâche) sur 5 propriétés
                                     d'évaluation (la 5e, l'autonomie, sans métrique) : recompté contre F-37 et
                                     contre PRD §6. L'écart 4 -> 3 est SIGNALÉ en §20.1, non comblé.
                                   - 3 rapprochements exposés en §20.1 : recomptés (F1 <-> performance ;
                                     FNR/vitesse <-> seuils de dépassement ; correction du journal <->
                                     documentation/inventaire) = 3. Repris à l'identique en conclusion.
                                   - 3 mouvements de la feuille de route (§20.2) : inventorier ; coter puis
                                     encadrer ; surveiller = 3 mouvements, soit QUATRE GESTES (le 2e en porte
                                     deux). PARTITION NON EXHAUSTIVE RÉFUTÉE en relecture adversariale : la
                                     conclusion du jet fusionné répartissait en 2 moitiés (inventorier+coter /
                                     surveiller) et LAISSAIT « encadrer » HORS de la partition — or c'est le
                                     geste adossé à la source la plus faible (positionnement OO et frame
                                     déterministe, tracés à F-37, préprint unique, PRD §10.10 ; et à
                                     l'inférence du ch. 13), NON au texte d'E-23. La partition laissait donc
                                     croire que tout ce qui n'est pas « surveiller » repose sur le texte
                                     réglementaire, et fondait là-dessus « commencer par l'instrumentation,
                                     c'est commencer par le maillon faible ». CORRIGÉ : gradation à quatre
                                     gestes, réserve propre à « encadrer » déclarée avec renvoi [^6].
                                   - 7 critères qualitatifs de sélection, 5 analystes juridiques nommés,
                                     5 volets du cycle de vie (renvoi ch. 9), 4 chaînes cherchées par F-35 :
                                     conformes au socle.
                                   - 7 « Lecture de l'auteur » : recomptées par extraction sur le corps
                                     (CONCORDANT avec l'étape 2). Le jet fusionné portait ici 7 alors que
                                     l'étape 2 disait 6 et que 6 étaient posées : deux décomptes contradictoires
                                     dans le même artefact de vérification, relevés en relecture adversariale.
                                     La 7e est désormais RÉELLE — le marqueur ajouté sur la prémisse de
                                     démonstrabilité du ch. 5 §5.2. Étapes 2 et 4 réalignées sur 7, mesuré.
                                   - Encadrés de lacune : gabarit CAS 2 de PRDPlan §4.4 — les DEUX encadrés
                                     portaient un corps de cas 2 (« aucune passe de recherche n'a été
                                     conduite ») sous le TITRE du cas 1 (« État de la connaissance
                                     vérifiable »). Retitrés « État de la recherche » en relecture, conformément
                                     à §4.4 (« le gabarit du cas 1 induit la fabrication d'une passe qui n'a
                                     pas eu lieu ») et à la pratique établie des ch. 18 §18.1 et 19 §19.2.
                                   Aucun autre calcul n'est posé dans ce chapitre. AUCUN chiffre de F-37 n'est
                                   repris (les F1 sont hors de ce chapitre — ch. 5).
     5. Relecture adversariale ... FAITE (§4.2.4) — deux relecteurs indépendants, jet fusionné RÉFUTÉ.
                                   6 constats bloquants et 10 réserves ; TOUS vérifiés contre le socle avant
                                   application, TOUS fondés, TOUS appliqués. Aucun écarté.
                                   RÉFUTÉ ET CORRIGÉ, par ordre de gravité :
                                   a) ENCADRÉ §20.1 — « Ce que le socle établit : […] leurs disciplines
                                      d'origine (génie logiciel, évaluation des classifieurs) », renvoyé à
                                      [^1]. F-37 n'énonce NULLE PART les disciplines d'origine : c'est une
                                      observation du ch. 5 §5.4, que ce chapitre promouvait au rang de fait
                                      du socle — dans l'encadré même dont l'objet est de délimiter ce que le
                                      socle établit (CA-1, CA-6, le lieu où la faute coûte le plus cher).
                                      Retiré de la liste, porté en renvoi marqué au ch. 5 §5.4.
                                   b) OUVERTURE — « Le chapitre 18 a établi que les protocoles ne répondent
                                      pas aux questions que pose le droit canadien » : UNIVERSEL NON TENU,
                                      attribué comme acquis à un chapitre qui le décline. Le ch. 18 établit le
                                      vide de PROTOCOLE sur 3 de ses 5 lignes seulement ; sur les 2 autres
                                      (AMF, cadre bancaire) la QUESTION elle-même n'est pas documentée. Le
                                      ch. 20 se contredisait 40 lignes plus bas (« Il ne dit pas ce que la
                                      ligne directrice de l'AMF attend »). Faute exacte corrigée sur la thèse
                                      du ch. 2 (TOC v1.3). BORNÉ à ce que le ch. 18 établit.
                                   c) §20.1 — « Une raison de fond […] elle est du chapitre 5. Les propriétés
                                      instrumentées sont exactement celles qu'un exploitant peut démontrer à
                                      un tiers » : INFÉRENCE BLANCHIE EN FAIT. Le marqueur était posé sur la
                                      SECONDE prémisse et manquait à la PREMIÈRE — or c'est la première qui
                                      est l'inférence, le ch. 5 §5.2 disant mot pour mot « ce partage est une
                                      construction du présent ouvrage ». Le chapitre appliquait à l'envers la
                                      leçon que son propre journal invoque (un chapitre de synthèse cite le
                                      SOCLE, pas la lecture qu'un chapitre antérieur en faisait). SECONDE
                                      FAUTE du même passage : la prémisse du ch. 5 couvre QUATRE propriétés,
                                      spécificité comprise — soit la quatrième que §20.1 écarte huit lignes
                                      plus haut. L'argument rangeait donc la 4e du côté des 3 retenues et
                                      contredisait le partage que le chapitre venait de poser. Marqueur posé
                                      sur la prémisse, portée dite explicitement (4 et non 3), absence de
                                      motif au partage 4->3 déclarée. Note [^1] complétée.
                                   d) §20.1 — « Le socle documente, chez un éditeur, des capacités dont la
                                      forme épouse ces attentes » : « dont la forme épouse ces attentes » EST
                                      le rapprochement produit <-> E-23, énoncé À LA VOIX DU SOCLE et sans
                                      marqueur. F-44 l'exclut explicitement (fait négatif établi). R-7 au
                                      paragraphe suivant ne rattrapait rien : la phrase attribuait DÉJÀ au
                                      socle une correspondance qu'il ne porte pas. Le chapitre venait
                                      d'écrire « Il faut résister à la tentation de les superposer » — et la
                                      superposait, par un VERBE. Réécrit : « des capacités qui portent sur les
                                      mêmes objets — inventorier, coter, surveiller ».
                                   e) §20.2 / §20.3 — « opposable » x2 : voir étape 3 (surqualification
                                      juridique ; motif ajouté au balayage).
                                   f) Réserves appliquées : partition non exhaustive de la conclusion
                                      (« encadrer » hors des deux moitiés — étape 4) ; « quatre métriques du
                                      préprint » = décompte faux, ce sont HUIT métriques sur QUATRE propriétés
                                      (étape 4) ; contradiction 6/7 du journal (étape 4) ; gabarit CAS 1/CAS 2
                                      des deux encadrés (étape 4) ; « correctness assurance » et
                                      « traceability / tractability » manquants (étape 2) ; auto-certification
                                      §8.4 (étape 3) ; « ce qu'un régulateur demandera en premier » = énoncé
                                      prédictif sur le BSIF, sans source et plus fort que ce que F-09 autorise
                                      (aucune source ne documente l'ordre des demandes d'un régulateur
                                      canadien) — rabattu sur ce que F-09 porte, avec note [^2].
                                   g) FAUSSETÉ DE CE JOURNAL, relevée par les relecteurs : le jet fusionné
                                      affirmait que « le ch. 19 n'est PAS rédigé à ce jour » et que les renvois
                                      au ch. 19 « sont secs et ne présument d'aucun contenu ». LES DEUX SONT
                                      FAUX et VÉRIFIABLES : `ch-19-architecture-reference.md` existe, porte
                                      « Statut | Rédigé (premier jet) », et son §19.2 traite exactement le
                                      positionnement OO des cas d'usage ; et les renvois de §20.2 comme de
                                      l'ouverture lui attribuent un contenu PRÉCIS. Le rédacteur avait déclaré
                                      non vérifiable ce qu'il pouvait lire, et dispensé de contrôle un renvoi
                                      qu'il avait chargé de contenu — classe d'erreur que la boucle §4.2.4
                                      doit intercepter, non produire. CONTRÔLE EXÉCUTÉ : le contenu attribué
                                      au ch. 19 concorde (§19.2 : principe du ch. 13 = OO3/OO4 ; sept critères
                                      qualitatifs sans pondération). Réserve levée, sans revérification due.
                                   h) « treize mois et un jour » (F-25), décompte NEUF signalé au jet fusionné :
                                      recalculé à l'étape 4, confirmé.
                                   POINT NON RÉFUTÉ, maintenu : la distinction des DEUX cas de R-7 (borné pour
                                   E-23 ; général pour l'AMF) — aucun relecteur ne l'a attaquée, et le corps
                                   comme la note [^5] la tiennent. Le motif de l'écart 4->3 (artefact de
                                   conception vs comportement en exploitation) reste marqué « Lecture de
                                   l'auteur » et n'est pas lu comme la raison du cahier des charges.
     6. Commit + registre de gel . dû (registre : renseigné par l'orchestrateur).
     7. Passe de correction F-09 . 16 juill. 2026 — 4 edits ciblés, aucune réécriture, volumétrie du corps
                                   inchangée (2782 mots) : (a) en-tête, (b) note [^2] et (c) étape 2 de ce
                                   journal remarqués **[A/B mixte]** (PRD v1.7), la formule « élevée [C]->[B],
                                   v1.6 » étant doublement fausse — [B] est SOUS [A] ; (d) conclusion,
                                   « qu'E-23 exige quoi que ce soit de l'IA agentique » -> « attende »
                                   (réserve F-09 : le balayage « exigé par E-23 | E-23 impose » n'avait pas vu
                                   la modalité revenir par le VERBE NU en tour NÉGATIF — même classe d'angle
                                   mort que l'adjectif « opposable », étape 3). Corrections 2 (affirmation
                                   périmée d'absence d'extraction) SANS OBJET — §20.1 pose l'extraction ;
                                   aucun encadré ne l'annonce en lacune. « fiches de modèles » (§20.1) :
                                   1 occurrence, watsonx.governance (F-44), NON TOUCHÉE — la sur-correction
                                   serait la faute symétrique (note [^3]).
     8. Passe de correction ...... 17 juill. 2026 — AUDIT GLOBAL DU 17 JUILL. 2026, constat m-28. UN edit ciblé,
        (audit du 17 juill. 2026)  aucune réécriture ; date de gel INCHANGÉE (16 juillet 2026).
                                   m-28 — OUVERTURE, paraphrase du ch. 18 : le jet portait « les deux autres lignes
                                   de sa matrice, le cadre bancaire et la ligne directrice de l'AMF, sont vides du
                                   côté des attentes elles-mêmes ». La paraphrase ASSIMILAIT DEUX ESPÈCES que le
                                   ch. 18 §18.3 distingue expressément, et dont il fait le cœur de sa lecture par
                                   exigence (« deux vides d'espèces différentes n'appellent pas la même conduite ») :
                                   (i) VIDE DE SOCLE — l'AMF, « la seule ligne où le premier terme manque » (ch. 18
                                   §18.1), « seul vide qu'une extraction primaire comblerait » (§18.3) ; (ii) VIDE
                                   DE TEXTE — le cadre bancaire, où « le socle porte l'exigence […], mais le texte
                                   officiel ne désigne rien », soit « non une lacune de l'ouvrage : un état du
                                   droit, et il est vérifié » (§18.3). « Vides du côté des attentes elles-mêmes »
                                   n'est vrai QUE de l'AMF ; appliqué au cadre bancaire, l'énoncé convertit un fait
                                   négatif vérifié (F-35, voté 9-0) en lacune documentaire du présent ouvrage —
                                   soit exactement l'inversion que la formule de distinction de PRDPlan §4.4
                                   (« absence de documentation ≠ fait négatif vérifié ») a pour objet d'interdire,
                                   et dans le sens qui SOUS-DÉCLARE ce que le socle établit.
                                   MÊME CLASSE DE FAUTE que le bloquant (b) de l'étape 5 : un chapitre de synthèse
                                   qui résume un chapitre antérieur d'une phrase, sans rouvrir le passage résumé.
                                   La correction de (b) avait borné l'universel ; elle n'avait pas vérifié la
                                   PARTITION de la même phrase.
                                   CORRIGÉ : les deux espèces sont restituées et attribuées à leur cause, avec
                                   renvoi [^13] (F-35, R-5) pour le cadre bancaire — le fait négatif n'est pas
                                   reformulé ici, la formulation imposée de PRDPlan §4.4 étant reprise mot pour mot
                                   en §20.3, où elle porte son ancrage daté (« au 16 juillet 2026 »). Un fait négatif
                                   sans date se lit comme permanent : il n'est donc énoncé qu'une fois, à sa place.
                                   VOLUMÉTRIE RE-MESURÉE APRÈS CORRECTION (leçon du CLAUDE.md global ; c'est
                                   l'omission de ce geste que l'audit sanctionne en m-30/m-31 sur le ch. 21).
                                   Commande du poste 1, réexécutée : **2840 mots** — CONFORME (+9,2 % sur la cible
                                   de 2600 ; plafond 2860, marge de 20 mots). Le correctif ajoute 58 mots de contenu
                                   tracé au ch. 18 §18.1/§18.3 ; aucun remplissage. La marge passe de 78 à 20 mots :
                                   toute reprise ultérieure du corps doit retirer avant d'ajouter.
                                   ⚠ CE POSTE A LUI-MÊME FAILLI MENTIR : « 2830 / marge 30 » y a été écrit AVANT
                                   la mesure, puis corrigé sur la commande (2840, +58 et non +48). L'écart était
                                   de 10 mots et sans conséquence de conformité — mais c'est le geste, non l'écart,
                                   qui est la faute : ce chapitre a déjà consigné « ne jamais écrire un décompte
                                   qu'on n'a pas posé » (poste 1), et le ch. 19 a consigné « CHIFFRES INVENTÉS
                                   AVANT MESURE ». La règle se réapprend à chaque passe, y compris dans la passe
                                   qui corrige des décomptes faux.
-->
