# Avant-propos et note méthodologique

| Champ | Valeur |
|---|---|
| Statut | Rédigé et relu adversarialement (17 juill. 2026) |
| Date de gel de l'information | 17 juillet 2026 |
| Socle mobilisé (PRD §7) | PRD Annexe A (méthode) ; renvois transversaux au socle F-01 à F-48 |
| Garde-fous à surveiller (PRD §8) | PRD §3 (non-objectifs), §8.4 (neutralité fournisseur), §7 (taxonomie des niveaux de preuve) |
| Volumétrie cible | ~2500 mots |

> **Thèse ([TOC.md](../TOC.md))** : Origine du projet, méthode, niveaux de preuve [A]/[B]/[C], convention de datation, avertissements.

---

## Ce que ce livre essaie de faire

Entre la fin de 2024 et le milieu de 2026, deux histoires que rien n'obligeait à se rencontrer se sont rencontrées.

La première est celle d'une couche technique. En novembre 2024, un éditeur publie un protocole permettant à un modèle de langage d'appeler des outils ; dix-sept mois plus tard, cette couche compte quatre protocoles, plusieurs fondations et des comités techniques. Il faut résister au raccourci qui s'offre ici, et que le chapitre 1 refuse explicitement : **tous ne sont pas passés sous gouvernance neutre**. MCP, A2A et AGNTCY l'ont fait ; pour AP2 — le protocole de la transaction, celui qui intéresserait le plus une institution financière —, le socle ne documente **aucun** transfert de gouvernance. Et sur les versions stables, il n'en établit que deux : A2A v1.0 et la révision MCP du 25 novembre 2025. La couche s'est consolidée ; elle ne l'a pas fait uniformément, et le lecteur qui aurait besoin du contraire est précisément celui à qui il faut le dire. La seconde est celle d'un secteur. Pendant les mêmes mois, les institutions financières canadiennes ont mis en production des systèmes qui décident : pré-adjudication hypothécaire, traitement autonome de courriels commerciaux, plateformes agentiques d'entreprise. Et pendant ces mêmes mois encore, le cadre réglementaire canadien s'est réorganisé autour d'une date unique — le 1er mai 2027, jour où entrent en vigueur, ensemble, la ligne directrice E-23 du Bureau du surintendant des institutions financières et la ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers.

Cet ouvrage est né d'une question simple et mal posée : que faut-il construire ? Elle est mal posée parce qu'elle présuppose que quelqu'un le sache. Personne ne le sait. Sur cette question, un seul fait négatif a été réellement vérifié, et il suffit : la ligne directrice E-23 n'emploie ni « agentique », ni « agents », ni « orchestration » — vérification mécanique sur son texte intégral, en anglais et en français. Le texte qui portera, au 1er mai 2027, les attentes du Bureau du surintendant des institutions financières en matière de risque de modèle ignore le mot même de l'objet de ce livre. Le reste du silence est plus faible, et l'ouvrage doit le dire tel : le contenu de la ligne directrice sur l'IA de l'AMF n'est pas à son socle, de sorte qu'il ne sait pas ce que ce texte dit — ou tait — de l'orchestration ; et le socle ne documente aucune spécification protocolaire qui mentionne un texte canadien, mais c'est là une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié — aucun balayage de ces spécifications n'a été conduit. Un silence établi, un texte non lu, un corpus muet : entre les deux histoires, il n'y a pas de pont — il y a un vide, et ce vide est le sujet du livre.

La thèse qu'il défend s'appelle l'**autonomie encadrée** (*framed autonomy*) : sous exigence réglementaire stricte, le processus est imposé de façon déterministe par le cadre, qui invoque les agents ; les agents n'orchestrent pas le processus. Cette thèse n'est pas une découverte de l'auteur. Elle est formulée, dans la littérature de la mi-2026, par un manifeste académique, par une expérimentation et par un patron d'architecture de fournisseur — trois sources dont le chapitre 13 établit qu'elles **ne sont pas indépendantes** : deux partagent une autrice, deux une organisation. Trois énoncés qui se recoupent deux à deux ne valent pas trois observateurs séparés, et l'ouvrage en tire la portée exacte plutôt que d'en majorer l'autorité. Ce que l'auteur ajoute — et ce qu'il assume — est le transport : aucune de ces trois sources ne parle du Canada, aucune ne parle de finance canadienne, et le chapitre 13 expose ce transport comme un raisonnement, non comme une déduction.

## Ce que ce livre ne fait pas

Il faut le dire avant plutôt qu'après.

**Il n'émet aucun avis juridique.** Il rapporte des textes, cite leurs formules officielles et en propose des lectures d'architecture. Ces lectures engagent l'auteur, jamais le régulateur, et ne valent pas qualification juridique. Qu'un processus donné relève ou non de l'article 12.1 de la Loi 25, qu'un assemblage d'agents constitue ou non « un modèle » au sens d'E-23 : ces questions sont posées ici, elles ne sont pas tranchées. Elles ne peuvent l'être que par une institution, avec ses conseils.

**Il n'émet aucun conseil d'investissement.** Les institutions nommées le sont comme cas documentés, jamais comme recommandations.

**Il ne recommande aucun fournisseur.** La Partie VII développe un blueprint instancié sur le portefeuille d'IBM. Ce choix appelle une explication, car il pourrait passer pour une préférence : c'est un **cas d'instanciation documenté par sources primaires**, retenu parce que la documentation publique de cet éditeur permettait de tracer chaque composant à une source datée. Rien n'y est un verdict comparatif ; les alternatives sont citées par renvoi ; les faits négatifs — dépréciations, absences, revendications que l'éditeur ne fait pas — y sont exposés comme le reste. Un lecteur qui refermerait la Partie VII en concluant « il faut acheter cela » l'aurait mal lue.

**Il n'est pas un tutoriel** et ne contient pas de code.

## Comment ce livre sait ce qu'il dit

Tout ce qui suit repose sur un **socle factuel** : un corpus de **46 entrées**, numérotées de F-01 à F-48 — les identifiants F-12 à F-14 n'ont pas été attribués, une fusion les ayant absorbés lors de la synthèse, et une entrée porte le suffixe F-23b. Chaque affirmation factuelle centrale de l'ouvrage renvoie, en note, à l'une de ces entrées. Le lecteur qui veut contester une affirmation n'a donc pas à deviner d'où elle vient : la note lui donne l'entrée, l'entrée lui donne la source et sa date.

Ces entrées ne se valent pas, et l'ouvrage refuse de faire comme si. Trois niveaux de preuve les séparent, du plus fort au plus faible :

- **[A]** — le fait a survécu à un **vote adversarial 3-0** : trois vérificateurs indépendants ont tenté de le réfuter et ont échoué. C'est le niveau le plus élevé.
- **[B]** — la **source primaire a été lue et extraite**, avec citation, mais **sans vote adversarial**. C'est un fait bien tenu, pas un fait éprouvé.
- **[C]** — un **repérage documentaire à confirmer**, sans extraction. Une entrée [C] ne porte jamais un fait central.

L'ordre importe, et il est contre-intuitif. **[B] est en dessous de [A]**, alors qu'il est tentant de croire l'inverse : lire le texte officiel semble plus sûr que trois avis concordants. Mais ce n'est pas la qualité de la source que le niveau mesure — c'est **ce que l'affirmation a subi**. Les trois niveaux se distinguent par une seule variable, la procédure traversée : un vote adversarial, une extraction sans vote, un repérage sans extraction. Une entrée [A] repose elle aussi sur des sources primaires ; une entrée [C] en identifie une. Ce qui les sépare est l'épreuve, non le document. Et une lecture directe, si proche de la source soit-elle, reste la lecture d'un seul lecteur — avec ce qu'il n'a pas vu.

Ce livre a commis cette confusion, et le raconter vaut mieux que le taire. Le 16 juillet 2026, le texte intégral d'E-23 a été extrait de sa source officielle et versé au socle. L'opération a été consignée comme une **élévation « [C] → [B] »** de l'entrée F-09. Les deux termes étaient faux : l'entrée n'avait jamais été [C], et [B] est **sous** [A]. Le socle n'en a pas été dégradé — les faits votés 3-0 sont restés [A], et le contenu extrait s'y est ajouté au rang inférieur qui est le sien. C'est l'étiquette qui mentait : le projet croyait élever son entrée, il l'enrichissait, et l'annonçait fièrement à l'envers. L'erreur a été relevée non par son auteur, mais par la rédaction du chapitre 18, qui s'en servait ; l'entrée porte depuis un marquage explicite en deux strates, **[A/B mixte]**, et l'ouvrage attribue chaque fait d'E-23 à la strate dont il relève. C'est, de tout ce qui figure dans ce livre, la meilleure illustration de ce qu'une méthode peut et ne peut pas : elle n'a pas empêché la faute, elle l'a attrapée.

Trois règles complètent la taxonomie.

**Les métriques auto-déclarées sont attribuées à chaque occurrence.** Selon la Banque Scotia (*Perspectives*, juillet 2025), son système AIDox traite environ 90 % d'environ 1 500 courriels par jour ; selon TD (*stories.td.com*, 21 mai 2026), la pré-adjudication hypothécaire de Layer 6 a fait passer un délai d'environ quinze heures à moins de trois minutes. Ces deux données sont auto-déclarées et n'ont fait l'objet d'aucune vérification indépendante — et l'on remarquera que la phrase qui précède ne pouvait pas les citer autrement, fût-ce pour l'exemple. La même règle vaut pour les études d'analystes : le commanditaire est nommé. Cette insistance paraîtra lourde ; elle est délibérée. Un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait.

Le premier jet de cet avant-propos citait ces deux chiffres **sans nommer les institutions**, en s'accordant une exemption : ils y figuraient comme illustrations de la règle, non comme faits. La relecture adversariale a refusé l'exemption, et elle avait raison — la règle dit « à chaque occurrence » et n'en connaît pas d'exception ; ce qu'un lecteur retient d'une phrase, c'est le chiffre, pas son statut grammatical. Le paragraphe qui énonce la règle était celui qui l'enfreignait. L'anecdote est petite ; elle dit exactement pourquoi la discipline est écrite plutôt que laissée au jugement.

**Le lien documenté et l'inférence de l'auteur ne sont jamais confondus.** Chaque fois que l'ouvrage rapproche un composant technique d'une exigence réglementaire, il dit lequel des deux régimes s'applique. Quand une source établit le lien, il est **documenté**. Quand c'est l'auteur qui le construit, l'énoncé porte en gras la mention **Lecture de l'auteur** — suivie de ce que le socle établit, et de ce qu'il n'établit pas. Le lecteur peut ainsi trier ce qu'il peut opposer à un tiers de ce qu'il ne peut qu'emprunter.

**L'absence de documentation n'est pas un fait négatif.** Que le socle soit muet sur une question ne prouve rien : cela dit seulement que le corpus de cet ouvrage ne la couvre pas. L'ouvrage réserve la formule « **fait négatif vérifié** » aux rares cas où l'absence a été établie par un balayage documenté — par exemple qu'E-23 n'emploie ni « agentique », ni « agents », ni « orchestration », ce qui a été vérifié mécaniquement sur le texte intégral, en anglais et en français. La distinction n'est pas de l'élégance : elle décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable.

La méthode complète — passes de recherche, votes adversariaux, incident de la troisième passe et reprise, élévations tentées et échouées — fait l'objet de l'**annexe A**.

## Ce que ce livre ne sait pas

Une méthode qui ne produirait que des certitudes serait une méthode qui ment. Les lacunes de cet ouvrage ne sont pas reléguées en note : elles sont exposées en encadrés « **État de la connaissance vérifiable** », au fil des chapitres, et rassemblées au **chapitre 21**.

Certaines sont embarrassantes, et c'est bien ainsi. La ligne directrice sur l'IA de l'AMF est finale depuis le 30 mars 2026 ; son contenu n'est pas au socle, et l'ouvrage ne dit donc rien de ce qu'elle prescrit — d'un des deux textes qui structurent toute sa Partie III. On ne trouvera nulle part ici une reconstruction de ce qu'elle « doit » contenir. L'articulation entre le protocole de paiement agentique et les rails canadiens n'est documentée par aucune source : le chapitre 16 pose des questions et s'y tient. Le rapprochement de certaines dépendances techniques est resté au niveau [C] après une tentative d'élévation infructueuse ; l'échec est raconté plutôt que masqué.

## La convention de datation, et ce qu'elle implique

Chaque chapitre porte une **date de gel de l'information** : la date à laquelle son contenu a été arrêté. Elle figure dans son en-tête, et le registre des gels (`monographie/99-registre-gel.md`) les rassemble. Pour les vingt-quatre chapitres du corps, cette date est le 16 ou le 17 juillet 2026.

Cette convention a une conséquence que le lecteur doit prendre au sérieux : **l'ouvrage ne se périme pas d'un bloc, il se périme par morceaux, à des rythmes différents**. Un chapitre sur l'article 12.1 de la Loi 25, en vigueur depuis 2023, vieillira lentement. Un chapitre sur les versions de protocoles vieillira vite.

Un exemple, et il est immédiat. Une révision majeure de la spécification MCP — refonte du protocole vers un fonctionnement sans état, retrait de l'identifiant de session — est confirmée pour le **28 juillet 2026**, soit **douze jours après** la date de gel des chapitres qui la décrivent. La revalidation finale du 17 juillet 2026 a confirmé l'échéance à sa source. Les chapitres 1, 2 et 7 décrivent donc, en connaissance de cause, un état qui sera historiquement daté avant que beaucoup de lecteurs n'ouvrent le livre. Ils ne s'en excusent pas : ils portent leur date. Mais un lecteur qui les consulterait pour décider d'une architecture doit lire la spécification à sa source.

Le **chapitre 24** énumère les événements qui périmeront des parties de cet ouvrage, et le protocole pour les revalider. Ce n'est pas une clause de style : c'est la condition d'usage du livre.

## Comment lire

Les **notes** portent les identifiants F-xx du socle : elles sont l'appareil de vérification, non un ornement. Les **encadrés** signalent les lacunes. La mention **Lecture de l'auteur**, en gras, signale un raisonnement de l'auteur — le lecteur pressé qui ne retiendrait qu'une convention devrait retenir celle-là. L'**annexe D** fixe la terminologie, français et anglais ; elle contient aussi la liste des termes que l'ouvrage s'interdit, et les raisons de chaque interdiction. Le sigle « ACP », notamment, ne paraît jamais seul : quatre choses différentes le portent dans ce domaine, et les confondre est l'erreur la plus facile à commettre.

L'ouvrage se lit en sept parties, des protocoles au blueprint. Le **chapitre 13** en est le pivot : c'est là que le vide entre les deux histoires est franchi, et c'est le chapitre à contester en premier.

Un dernier mot sur le ton. Le lecteur trouvera ici plus de réserves, de bornes et de « ce que le socle n'établit pas » qu'il n'est d'usage. Ce n'est pas de la prudence rhétorique. Dans un domaine où la production éditoriale dépasse de loin ce qui est vérifiable, la seule contribution durable d'un ouvrage est la ligne qu'il trace entre ce qu'il sait et ce qu'il croit. Ce livre a essayé de la tracer au bon endroit, et de la tracer visiblement, pour qu'on puisse lui montrer qu'il s'est trompé.

<!--
AUTO-CONTRÔLE DE TRAÇABILITÉ (PRDPlan §4.2.2)
  - « dix-sept mois » : aligné sur la thèse du ch. 1 (TOC v1.2, correctif de rédaction — nov. 2024 →
    communiqué LF du 9 avril 2026, F-02). NE PAS écrire « dix-huit » : erreur corrigée à la source.
  - « 46 entrées, F-01 à F-48, F-12 à F-14 non attribués, plus F-23b » : RECOMPTÉ mécaniquement le
    17 juill. 2026 (`grep -oE '^- \*\*F-[0-9]+[a-z]?' PRD.md | sort -u | wc -l` → 46). Le décompte
    « 48 » circulait par confusion entre le plus haut identifiant et le cardinal des entrées.
    PRD §7 chapeau documente la numérotation discontinue.
  - Taxonomie [A] > [B] > [C] et épisode F-09 : PRD §7 chapeau + F-09 ([A/B mixte], PRD v1.7).
  - Vérification négative d'E-23 (agentique/agents/orchestration = 0, EN et FR) : F-09, strate [B].
  - RC MCP du 28 juill. 2026 : F-01 + `verification/revalidation-2026-07-17.md` (échéance CONFIRMÉE
    à sa source le 17 juill. 2026 — ni avancée ni reportée).
  - AMF finale au 30 mars 2026, contenu hors socle : F-25 + lacune PRD §10.4.
  - Non-objectifs (aucun avis juridique, aucun conseil d'investissement, pas de tutoriel) : PRD §3.
  - Neutralité fournisseur : PRD §8.4.
  - Métriques citées : ~90 % de ~1 500 courriels = **F-21** (Scotiabank / AIDox) ; 15 h → <3 min =
    **F-17** (TD / Layer 6). CORRIGÉ le 17 juill. 2026 : cette ligne portait « F-18 (Scotiabank) »
    — F-18 est *TD, gouvernance*. Se tromper d'entrée dans le contrôle de traçabilité du document
    qui promet au lecteur que « la note lui donne l'entrée » : relevé par la relecture adversariale.
  - ATTRIBUTION : l'exemption que ce document s'accordait (citer les deux chiffres SANS nommer les
    institutions, au motif qu'ils illustraient la règle) a été REFUSÉE par la relecture adversariale
    et retirée. PRD §7.5 dit « à chaque occurrence » et ne connaît pas d'exception d'usage
    illustratif ; §8.2.2 vise nommément ces deux chiffres. Les deux institutions sont désormais
    nommées et l'épisode est raconté dans le corps.
    ⚠ CETTE LIGNE A MENTI jusqu'au 17 juill. 2026 : elle attestait « nommées, AVEC SOURCE ET DATE »
    alors que seule Scotia en portait — TD était nommée sèchement. Source et date ajoutées au corps
    (*stories.td.com*, 21 mai 2026 — F-17), dans la forme imposée par PRDPlan §4.4 « Métrique
    auto-déclarée ». L'attestation couvrait le défaut qu'elle prétendait constater ; relevé par
    l'audit du 17 juill. 2026 (constat m-01), non par l'auto-contrôle qui la portait.
    Les ordres de grandeur sont rendus tels que le socle les porte (« ~90 % », « ~1 500 ») et non
    durcis en « 90 % de quinze cents » comme le faisait le premier jet.

BALAYAGE DES GARDE-FOUS (PRDPlan §4.2.3 / §4.3)
  - R-8 (`\bACP\b|control plane|plan de contrôle`) : 1 occurrence — « Le sigle "ACP" (…) ne paraît
    jamais seul », en MENTION du sigle, non en emploi référentiel, et précisément pour énoncer
    l'interdiction. Conforme §D.7.
  - F-09 (`exigé par E-23|E-23 impose|fiche de modèle|model card`) : 0 occurrence.
  - R-7 (`E-23|B-13`) : occurrences en contexte réglementaire pur, aucune correspondance produit ↔
    réglementation — filtré (§4.3).
  - R-1, R-2, R-3, R-4, R-5, R-6 : sans objet (aucun motif).
  - §8.2.2 / §7.5 : voir la réserve d'auto-contrôle ci-dessus.
  - CA-5 : framed autonomy à sa première occurrence.

RELECTURE ADVERSARIALE (PRDPlan §4.2.4) — FAITE le 17 juill. 2026, relecteur distinct du rédacteur.
  Verdict initial : NON PUBLIABLE. 3 bloquants, 8 réserves. Tous traités :
  B1 « onze jours » entre le gel des ch. 1/2/7 et la révision MCP → DOUZE (28 − 16). Le nombre
     venait du rapport de revalidation, qui compte depuis le 17 (date de publication) ; il a été
     importé sans réancrage. Il se logeait dans le paragraphe qui DÉMONTRE la convention de datation,
     et contredisait le registre de gel, qui fait foi et écrivait « douze » depuis la veille.
  B2 « quatre protocoles […] est passée sous gouvernance neutre et a atteint ses premières versions
     stables » : universel réfuté par F-04 (AUCUN transfert de gouvernance documenté pour AP2) et
     par le ch. 1, qui pose nommément la restriction. Le socle n'établit par ailleurs que DEUX
     versions stables (A2A v1.0, MCP 2025-11-25). Corrigé et borné. MÊME FAUTE DANS L'ABSTRACT DE
     TOC.md, dont ce paragraphe l'avait héritée → REMONTÉE, corrigée par le parent.
  B3 exemption d'attribution refusée (voir ci-dessus).
  R4 « [B] mesure la proximité à la source » : glose FAUSSE, et contredisant l'annexe A §A.3 du même
     ouvrage, qui est juste (« le niveau ne mesure pas la qualité de la source ; il mesure ce que
     l'affirmation a subi »). Aligné sur §A.3.
  R5 « le projet le dégradait » : durci pour l'effet. F-09 dit « enrichit d'un contenu de niveau
     inférieur ». Les faits [A] sont restés [A] ; seule l'étiquette mentait. Corrigé.
  R6 F-18 → F-21 (voir ci-dessus).
  R7 non-indépendance des trois sources OMISE — seule pièce de l'ouvrage à la taire, et au moment
     précis où elle vend la thèse. Ajoutée.
  R8 « [C] […] n'apparaît qu'en encadré » : promesse PLUS FORTE que la règle (PRD §10 n'exige
     l'encadré que des LACUNES). Retirée — une promesse non due est une promesse opposable.
  Axes déclarés propres par la relecture : non-objectifs (aucun avis juridique émis, ch. 13 §13.3
  vérifié), garde-fous (R-8 conforme — « ACP » en mention, non en emploi), neutralité fournisseur,
  conventions promises (tenues dans les 24 chapitres), complétude au regard du TOC.

POINTS DE GOUVERNANCE REMONTÉS AU PARENT
  a) [DÉCOMPTE DU SOCLE] RÉSOLU le 17 juill. 2026 : PRD §7 chapeau porte désormais le cardinal (46),
     sa commande de recomptage et l'avertissement sur le piège ; CLAUDE.md corrigé.
  b) [ATTRIBUTION] TRANCHÉ : exemption refusée, institutions nommées.
  c) [ABSTRACT DE TOC.md] Remonté au titre de B2 — même universel sur AP2. Corrigé par le parent.
  d) [PRD §Version] La ligne v1.6 énonce encore « F-09 élevé [C]→[B] », formulation que F-09
     qualifie elle-même de « doublement fausse ». Le PRD conserve la faute dans son propre
     historique. NON CORRIGÉ — et c'est délibéré : un journal de versions consigne ce qui a été
     fait, y compris à tort. La rectification est portée par F-09 et par le §Version v1.7.

PASSE DE CORRECTION — 17 juill. 2026, suites de l'audit du 17 juill. 2026 (`audit.md`)
  Trois constats traités ; aucune information nouvelle n'entre, la DATE DE GEL EST INCHANGÉE
  (17 juill. 2026) — le gel porte sur l'information, ces corrections portent sur la conformité.
  M-01 [§Ce que ce livre essaie de faire] DEUX UNIVERSELS NÉGATIFS retirés : « Aucun régulateur
     canadien n'a écrit une ligne sur l'orchestration agentique ; aucune spécification protocolaire
     ne mentionne un texte canadien. » Le socle ne vérifie NI l'un NI l'autre — le contenu de la
     ligne directrice IA de l'AMF n'y est pas (PRD §10.4) et aucun balayage des spécifications n'est
     documenté (cf. PRD §10.9 : « Aucune de ces absences n'établit un fait négatif »). Le passage
     est désormais adossé au seul fait négatif vérifié disponible — F-09, strate [B], balayage
     mécanique d'E-23 sur le texte intégral EN et FR — et rend le reste à son statut par la formule
     de distinction de PRDPlan §4.4 (« absence de documentation dans le corpus de cet ouvrage, non
     un fait négatif vérifié »). ⚠ LA COHÉRENCE INTERNE ÉTAIT LE POINT : ce fichier ENSEIGNE cette
     distinction quinze paragraphes plus bas (§« Comment ce livre sait ce qu'il dit ») et
     l'enfreignait dans son ouverture — même mécanique que le paragraphe d'attribution qui
     s'exemptait de sa propre règle (B3, ci-dessus). Un document qui pose une règle est le premier
     endroit où la chercher.
  m-01 [§Comment ce livre sait ce qu'il dit] Métrique TD : source primaire et date ajoutées ; voir
     la réserve d'ATTRIBUTION ci-dessus, dont l'attestation est rectifiée au même geste.
  m-02 [en-tête] Statut « Rédigé (premier jet) » → « Rédigé et relu adversarialement
     (17 juill. 2026) ». La relecture est FAITE (bloc ci-dessous ; PRDPlan §1.4 la consigne avec
     ses trois bloquants) : l'en-tête déclarait moins que l'état réel. Classe « statut qui ment ».
  REMONTÉ AU PARENT — non traité ici (hors du seul fichier autorisé) :
     e) [VOLUMÉTRIE] Ces corrections allongent le corps. Décompte de CETTE pièce, remesuré par la
        commande de référence après édition : **2 174 → 2 319** mots (cible ~2 500, toujours sous
        la cible). ✔ RÉALIGNÉS PAR LE PARENT le 17 juillet 2026, une fois les 29 pièces landées :
        TOC.md (ligne « Avant-propos » → 2 319 ; total → **92 059**), PRD §12, PRDPlan §1.4
        (décompte de contrôle), CLAUDE.md et le README — dont le 88 021 était faux avant cette
        passe (audit M-14), sa racine étant PRDPlan §1.4 (P4.3), qui portait ce même chiffre
        périmé dix lignes au-dessus de son propre 90 362. L'audit avait vu le symptôme, pas la racine.
        ⚠ AUCUN TOTAL N'EST ANNONCÉ ICI, ET C'EST DÉLIBÉRÉ : au moment de cette passe, d'autres
        pièces étaient en cours de correction dans le même dépôt (ch. 1 et ch. 6 modifiés,
        non enregistrés). Un total mesuré ici serait faux avant d'être écrit. Le total des 29 se
        remesure par la commande de référence UNE FOIS TOUTES LES PIÈCES LANDÉES, et par le parent
        qui seul voit leur terme — c'est la condition qui a déjà produit trois mesures
        successives (89 757, 88 021, 90 362 — voir TOC.md). Ne pas dériver le total d'un delta.
     f) [REGISTRE DE GEL — ✔ TRAITÉ le 17 juill. 2026 par le parent : le registre est réaligné
        sur l'état vrai, ses lignes P4 portent la relecture du 17 juill. et la mention « cinq pièces
        sans relecture » est retirée avec sa trace. Constat d'origine conservé ci-dessous.]
        `99-registre-gel.md:31` portait « premier jet — relecture
        adversariale due » et sa ligne 41 range l'avant-propos parmi les « cinq pièces sans
        relecture adversariale ». Contredit par PRDPlan §1.4 et par le bloc ci-dessous. C'est la
        paire d'attestations en conflit de l'audit (M-15) : l'en-tête de CETTE pièce est réaligné
        sur l'état vrai, le registre reste à réaligner.

DÉCOMPTE (PRDPlan §4.2, commande de référence — CORRIGÉE le 17 juill. 2026)
  awk '/^---$/{f=1;next} /^## Notes/{exit} /^<!--/{exit} f' 00-avant-propos.md \
    | tr -s '[:space:]' '\n' | grep -cE '[[:alnum:]]'
  Cible ~2500. La commande de référence NE PORTAIT PAS la borne « <!-- » à sa première rédaction :
  cette pièce n'a pas de section « ## Notes », l'awk ne s'arrêtait donc jamais et comptait le présent
  bloc — 2308 annoncés pour 1854 réels. Défaut relevé par la relecture adversariale de CE fichier ;
  la commande avait été testée sur deux fichiers et publiée comme référence pour vingt-neuf.
  PRDPlan §4.2 corrigé ; les 29 pièces recomptées ; TOC réaligné.
-->
