# Chapitre 24 — Lacunes du blueprint et conditions de revalidation

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | PRD Annexe B.3 et B.5 ; §8.3 (sensibilité temporelle) ; §10.6 et §10.1 ; F-38, F-39, F-40, F-41, F-42, F-44, F-45, F-46 ; F-01, F-09, F-25, F-29, F-34, F-35, F-36, F-37 (renvois) |
| Garde-fous à surveiller (PRD §8) | **R-5**, **R-6** ; **R-4** et réserve F-29 (renvois — événements de péremption) ; R-7 et §8.4 (neutralité fournisseur) ; §8.2.7 (études commandées) |
| Volumétrie cible | ~3000 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Le blueprint est daté (juillet 2026) et le dit — lacunes propres, événements de péremption, protocole de revalidation.

---

Les deux chapitres qui précèdent ont décrit une architecture : six principes directeurs, huit couches instanciées sur un portefeuille documenté, un tableau de correspondance réglementaire et trois flux de bout en bout (ch. 22 et 23). Ce chapitre en dresse l'inventaire des faiblesses. Non par scrupule rhétorique, mais parce qu'un blueprint dont on ignore les zones aveugles est plus dangereux qu'un blueprint absent : il donne à un dossier d'architecture l'apparence de la complétude là où subsistent des inférences, des repérages non confirmés et des faits en attente d'événement.

Trois registres de faiblesse doivent être distingués, et le chapitre suit cet ordre. D'abord les **lacunes propres au blueprint** : ce que le socle de cet ouvrage ne parvient pas à établir, malgré recherche. Ensuite les **conditions de péremption** : ce que le blueprint tient pour vrai aujourd'hui et qu'un événement daté, souvent déjà calendré, rendra faux. Enfin le **protocole de revalidation** : la procédure par laquelle un lecteur — ou l'auteur — reconstitue la validité du document à une date ultérieure. Les deux premiers registres relèvent de la connaissance ; le troisième, de la méthode.

## 24.1 Les lacunes propres au blueprint

La spécification du blueprint énumère six lacunes[^1]. L'une d'elles est **résolue** depuis la passe de revalidation du 16 juillet 2026 ; cinq subsistent. Les traiter dans cet ordre — la résolue d'abord — n'est pas une commodité : c'est la démonstration que la liste est vivante et que sa réduction est possible.

### Une lacune résolue : la clôture de l'acquisition Confluent

Jusqu'à la revalidation, la trajectoire événementielle du portefeuille reposait sur une annonce dont l'aboutissement n'était pas confirmé. Il ne s'agissait pas d'un détail : la documentation d'IBM déclare que ses solutions Kafka et Flink futures « seront livrées par IBM Confluent », en même temps qu'elle déclare Event Streams et Event Processing dépréciés, sans amélioration à venir[^2]. Une couche entière du blueprint — l'épine dorsale événementielle (C3) — dépendait donc d'une opération susceptible d'échouer.

Elle n'a pas échoué. L'acquisition, annoncée le 8 décembre 2025, a été **clôturée le 17 mars 2026** : trois mois et neuf jours, jalonnés par l'expiration du délai HSR le 12 janvier 2026 et l'approbation des actionnaires de Confluent le 12 février 2026[^2]. Confluent est devenue filiale à part entière d'IBM. Le blueprint peut désormais écrire au passé ce qu'il devait écrire au conditionnel : la trajectoire Kafka/Flink du portefeuille est un fait, non une annonce (ch. 22 §22.2).

**Lecture de l'auteur** : cette lacune a été résolue par une seule vérification ciblée sur la source primaire de l'éditeur. Elle mesure ce qu'une passe de revalidation disciplinée peut accomplir — et, par contraste, ce que les quatre lacunes suivantes ont d'irréductible avec les moyens documentaires disponibles. La cinquième subsistante, la datation même du blueprint, n'est pas traitée ici : elle est l'objet des sections 24.2 et 24.3, qui en font le cœur du chapitre.

### La position au Gartner Magic Quadrant iPaaS : non vérifiée (R-6)

Le socle établit deux positions d'analystes concernant l'offre d'intégration : IBM est Leader du Forrester Wave iPaaS du troisième trimestre 2025, et Leader du Gartner Magic Quadrant **API Management** 2025[^3]. Il n'établit **rien** sur la position d'IBM au Gartner Magic Quadrant **iPaaS** 2025 ou 2026 : aucune annonce correspondante n'a été retrouvée, et cette absence est consignée comme garde-fou explicite de l'ouvrage[^4].

La précision n'est pas byzantine. Deux quadrants distincts d'un même analyste, portant sur deux marchés distincts, ne se substituent pas l'un à l'autre ; les confondre est l'erreur exacte que le garde-fou interdit. Un dossier d'architecture qui écrirait « IBM est Leader du Magic Quadrant iPaaS » énoncerait une affirmation que cet ouvrage n'a pas pu vérifier, quelle que soit sa vraisemblance.

La même exigence s'applique en amont aux chiffres de rentabilité. Lorsque la documentation d'IBM avance un retour sur investissement de 176 % pour webMethods, ce chiffre provient d'une étude Forrester *Total Economic Impact* **commandée par IBM**[^3] — il est cité, s'il doit l'être, avec son commanditaire, à chaque occurrence.

### Aucune architecture agentique IBM spécifique aux services financiers

Le blueprint s'appuie, pour son premier principe, sur une convergence à trois sources : un manifeste académique — celui de l'*Agentic Business Process Management* (ch. 6) —, une expérimentation — les travaux sur les options d'orchestration OO1–OO4 (ch. 5) — et un patron de fournisseur — l'architecture agentique publiée par IBM (ch. 22) —, **dont deux partagent une autrice et deux une organisation**[^5]. La convergence reste un faisceau réel ; elle ne vaut pas corroboration indépendante, et le chapitre 13 §13.2 en a détaillé les chevauchements, comme le rappelle le chapitre 22 §22.1. Cette troisième source est explicite sur le fond : elle recommande les **workflows statiques** (*static workflows*) pour les processus sous surveillance réglementaire, en invoquant l'auditabilité, la conformité et des transferts définis[^5].

Elle est toutefois **générique**. Le socle documente qu'IBM ne publie pas d'architecture agentique propre aux services financiers — vérification faite sur le catalogue d'architectures de l'éditeur et sur les Redbooks[^5]. Autrement dit, la déclinaison du patron générique vers le contexte d'une institution financière fédérale canadienne — le périmètre E-23, la ligne directrice de l'AMF, les rails Lynx et le *Real-Time Rail* — est le travail de cet ouvrage, non celui de l'éditeur. Chaque fois que la Partie VII descend du patron vers le cas canadien, elle produit une inférence d'auteur, et le chapitre 23 le marque comme telle.

### La solution FTM / ISO 20022 : une élévation tentée, et échouée

La couche de messagerie et d'événements (C3) porte la promesse la plus directement financière du blueprint : émettre des messages ISO 20022 vers Lynx avec une garantie transactionnelle, et lire le trafic du futur *Real-Time Rail*. Le socle documente, à la documentation de l'éditeur, une solution dédiée d'App Connect Enterprise 13 (13.0.7, mars 2026) pour la messagerie ISO 20022, et une messagerie IBM MQ 10.0 LTS (GA juin 2026) « exactement une fois » (*exactly-once*) avec cryptographie post-quantique pour TLS[^6]. Mais le maillon qui relie MQ à ISO 20022 passe par le *Financial Transaction Manager* (FTM), et ce maillon n'est établi qu'au niveau de preuve **[C]** — repérage documentaire, non confirmé[^7].

> **État de la connaissance vérifiable — le lien MQ ↔ FTM ↔ ISO 20022**
>
> **Question** : le portefeuille documente-t-il, par une source primaire courante, la chaîne complète reliant la messagerie transactionnelle MQ au traitement des messages ISO 20022 via le *Financial Transaction Manager* ?
>
> **Recherche menée le 16 juillet 2026** (phase P0.2, une passe de recherche ciblée). Ce qui a été établi : FTM demeure un produit actif et documenté par l'éditeur, jusqu'à la version 4.0.8 ; le lien MQ ↔ FTM ↔ ISO 20022 est confirmé par citation directe, **mais uniquement via un Redbook de 2016** — c'est-à-dire au même niveau de preuve que le repérage initial, sans progrès. Une source non-Redbook actuelle a bien été localisée (un document officiel daté du 4 février 2025 portant sur la solution ISO 20022 d'App Connect Enterprise), **mais elle ne nomme ni FTM ni MQ** : ni contradiction, ni confirmation croisée. **Pourquoi la recherche échoue** : les pages de documentation de l'éditeur refusent systématiquement l'accès aux outils de vérification automatisée (403), obstacle documenté pour l'ensemble de la Partie VII.
>
> **Conséquence** : l'entrée reste au niveau **[C]** et **ne peut porter aucun fait central** du blueprint. Toute institution qui envisagerait cette chaîne d'intégration doit la faire confirmer par son propre canal éditeur avant de l'inscrire à un dossier. En l'absence de source primaire courante, aucune inférence n'est proposée ici. Une relecture humaine des sources bloquées est recommandée avant publication[^7].

Cette lacune a une valeur méthodologique qui dépasse son objet. Elle montre qu'une élévation de niveau de preuve peut échouer sans que la recherche ait été négligée, et que l'échec doit alors être **écrit**, avec sa date, ses moyens et son motif — plutôt que dissimulé derrière une formulation prudente qui laisserait le lecteur croire à un fait établi.

### Cinq correspondances réglementaires sur sept sont des inférences — et l'inverse serait plus grave

La cinquième lacune est de nature différente : elle est structurelle et ne sera pas comblée par une recherche. Le tableau de correspondance réglementaire du blueprint (ch. 23) rapproche des composants et des exigences canadiennes. Sur ses sept liens, **cinq sont des inférences d'auteur** ; une seule est **documentée** — et pour le seul rôle opérationnel d'IBM Canada sur les rails Lynx et le *Real-Time Rail*, non pour une conformité ; la septième est une **attente réglementaire** où il est interdit d'anticiper[^8]. Quatre cas doivent donc être tenus distincts, et le chapitre 23 les tient.

Le premier est celui de l'inférence adossée à un **fait négatif établi**. Le rapprochement entre la gouvernance de modèles du portefeuille et la ligne directrice E-23, comme celui entre l'offre infonuagique et la ligne directrice B-13, est une **inférence d'auteur** : IBM ne revendique aucune conformité à ces deux exigences, et aucune source ne documente ces liens[^8]. Ce fait négatif est établi ; il est écrit.

Le second est l'**inférence simple**, et il appelle une prudence symétrique et inverse. Le rapprochement entre un composant et la ligne directrice de l'AMF, l'article 12.1 de la Loi 25 ou l'avis 11-348 des Autorités canadiennes en valeurs mobilières est une **inférence d'auteur** — sans plus. Il serait faux d'y ajouter que l'éditeur ne revendique aucune conformité en général : le socle atteste au contraire des **revendications d'IBM** pour l'AI Act européen, ISO/IEC 42001 et le NIST AI RMF — l'add-on « Compliance Accelerators » de watsonx.governance, issu d'un accord OEM avec Credo AI du 28 avril 2025[^8]. L'absence de revendication est établie pour E-23 et B-13, et pour eux seuls.

Le troisième est le **lien documenté**, et il interdit l'universel inverse. Le rôle d'IBM Canada comme partenaire technologique de Lynx et partenaire de livraison du *Real-Time Rail* est attesté par des sources primaires — Paiements Canada et la salle de presse canadienne de l'éditeur[^8]. C'est un fait de contexte opérationnel, non un argument de conformité (PRD §8.4). La solution ISO 20022 qui l'accompagne, elle, demeure au niveau [C]. Le quatrième est l'**attente réglementaire** : la ligne du cadre bancaire axé sur le consommateur, où aucun standard n'est nommé et où rien ne doit être anticipé (§24.2, point 1).

À ces cinq points, la lacune du portefeuille au socle général ajoute trois résidus mineurs, que l'honnêteté commande de nommer : la date officielle de l'annonce du cadre d'intégration d'agents tiers reste absente des pages de l'éditeur ; aucune annonce n'est documentée entre IBM et une institution financière canadienne autre que BMO et TD, et encore avec des réserves — l'étude de cas d'un pilote d'IA générative avec TD n'est attestée que par la page de l'éditeur, la banque ne nommant pas IBM dans son propre communiqué ; enfin, le blocage systématique des pages de l'éditeur aux outils automatisés impose une relecture humaine des annonces clés avant publication[^9].

## 24.2 Les événements de péremption

Les lacunes disent ce que l'on ne sait pas. Les conditions de péremption disent autre chose : ce que l'on sait aujourd'hui et qui cessera d'être vrai à une date largement prévisible. Cinq événements suffisent à périmer des pans entiers du blueprint. Quatre d'entre eux ont une date ou une fenêtre déjà connue à la date de gel de ce chapitre — ce qui rend leur surveillance triviale, et leur négligence inexcusable.

**1. La désignation de l'organisme de normalisation technique, par arrêté ministériel.** Le fait négatif est vérifié : au 16 juillet 2026, aucun organisme n'a été désigné et aucun standard n'est nommé dans les textes officiels du cadre des services bancaires axés sur le consommateur ; la candidature de FDX (*Financial Data Exchange*) relève du commentaire d'industrie, non d'une position officielle[^10]. Le troisième flux illustratif du blueprint (ch. 23) est donc construit sur une attente : il expose des interfaces de programmation *selon le standard qui sera désigné*. Le jour de l'arrêté, ce flux devient spécifiable — ou devient faux, si le standard retenu impose des contraintes que l'architecture proposée ne satisfait pas. **Lecture de l'auteur** : de tous les événements listés ici, c'est celui qui porte le plus fort potentiel de réécriture. C'est aussi, et ce point est vérifiable, le seul dont la date reste inconnue.

**2. Le lancement effectif du *Real-Time Rail*.** La double contrainte doit être tenue des deux mains. D'un côté, Paiements Canada **vise** un lancement au quatrième trimestre 2026, à l'issue des tests industriels en cours ; la cible est officiellement annoncée, et écrire qu'aucune date ne l'est serait faux[^11]. De l'autre, cette cible a été **successivement reportée** — 2019, puis 2022, puis 2023, puis 2026 — et le système n'est pas en production à la mi-juillet 2026 : écrire qu'il est lancé serait tout aussi faux[^11]. Le deuxième flux du blueprint porte sur Lynx, non sur le RTR (ch. 23 §23.3) : le lancement n'en change donc pas la nature, et le principe qu'il instancie — le rail exécute, l'agent observe — vaudra pour le nouveau rail sans y avoir été exposé. Mais tout énoncé de cet ouvrage au futur sur le RTR devra passer au passé, ou être reformulé si la cible glisse une cinquième fois.

**3. Les textes réglementaires finaux postérieurs au 26 août 2026.** Le règlement du cadre bancaire est **prépublié** ; la période de commentaires de soixante jours se clôt le 26 août 2026 — quarante et un jours après la date de gel de ce chapitre — et le texte final peut différer du texte prépublié, notamment sur le phasage par produits et services[^12]. Dans la même fenêtre, le règlement administratif du *Real-Time Rail* entre en vigueur le 24 août 2026[^11]. Un blueprint gelé en juillet 2026 traverse donc, dans les six semaines suivantes, deux échéances réglementaires susceptibles d'en modifier les prémisses.

**4. La révision de la spécification MCP du 28 juillet 2026.** Douze jours après la date de gel de ce chapitre, une révision majeure du protocole d'accès des agents aux outils est attendue en finalisation — refonte sans état, retrait de l'en-tête de session, nouveaux en-têtes ; les mainteneurs la décrivent comme la plus importante depuis le lancement[^13]. Le blueprint décrit une couche d'exposition qui génère des serveurs MCP à partir des définitions d'interfaces existantes et gouverne les appels aux modèles (ch. 22, C1) : selon la documentation de l'éditeur, API Connect V12 — 12.1.0, disponible le 15 décembre 2025 — et l'AI Gateway, annoncé en mai 2024 et étendu en janvier 2025[^18]. La spécification en vigueur au moment où ce chapitre est gelé est la révision 2025-11-25 ; toute affirmation d'implémentation qui s'y adosse est datée en conséquence.

**5. Les entrées en vigueur du 1er mai 2027.** La ligne directrice E-23 du Bureau du surintendant des institutions financières et la ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers entrent en vigueur **le même jour**[^14] — dans neuf mois et demi à compter de la date de gel. Ce n'est pas une péremption au sens strict : les deux textes sont finaux, et rien n'y changera par cet effet de calendrier. C'est une péremption **de discours**. Tout ce que cet ouvrage écrit au futur proche — « les institutions devront », « d'ici l'entrée en vigueur » — bascule au présent le 1er mai 2027, et la question ne sera plus « comment se préparer » mais « comment se conformer ». La couche de gouvernance du blueprint (ch. 22, C6) sera alors jugée non plus sur sa plausibilité, mais sur ses résultats.

## 24.3 Le protocole de revalidation

Un document daté qui ne dit pas comment se redater n'est daté qu'à moitié. Le protocole qui suit est celui du plan d'exécution de l'ouvrage[^15] ; il vaut aussi bien pour l'institution qui reprendrait ce blueprint à son compte.

**Le principe** : amender le socle d'abord, les chapitres ensuite — jamais l'inverse. Un fait qui évolue est d'abord constaté à sa source primaire et consigné dans un rapport de revalidation daté ; l'entrée du socle est amendée, avec son niveau de preuve ; les chapitres qui en dépendent sont alors repris et portent une nouvelle date de gel. La discipline paraît lourde ; elle est ce qui empêche un chapitre corrigé de contredire silencieusement un chapitre voisin qui ne l'a pas été.

**La portée** : les faits « chauds » sont limitativement énumérés — les protocoles A2A et MCP, le *Real-Time Rail*, les règlements du cadre bancaire, la trajectoire du projet de loi C-36[^16]. La clôture de l'acquisition Confluent en faisait partie jusqu'à la passe de juillet 2026 ; elle est résolue et **sort de cette liste**. Une liste de veille qui ne se réduit jamais est une liste que l'on cesse de lire.

**Le seuil** : la revalidation doit dater de **moins de trente jours** au moment de la publication[^15]. Ce seuil est arbitraire, comme tout seuil ; il est calibré sur la cadence trimestrielle du domaine, où une spécification protocolaire majeure peut basculer en une quinzaine de jours — l'échéance du 28 juillet 2026 en fournit l'illustration à même ce chapitre.

**La transposition**, pour l'institution qui reprendrait ce blueprint, tient en trois gestes. Reconstituer d'abord la liste de veille à sa propre date : les cinq événements de la section précédente, augmentés de ce que le calendrier réglementaire aura fait apparaître entre-temps. Classer ensuite chaque affirmation du dossier d'architecture selon qu'elle repose sur un fait vérifié, sur une inférence — cinq des sept correspondances réglementaires en sont — ou sur un repérage non confirmé, comme la chaîne FTM/ISO 20022 ; seule la première catégorie soutient une décision, et le classement doit distinguer, parmi les correspondances, le lien documenté et l'attente réglementaire des cinq inférences. Rouvrir enfin, auprès de son propre canal éditeur, ce que les outils documentaires publics n'ont pas pu établir : ce que cet ouvrage n'a pas obtenu en 403, une institution cliente l'obtient souvent par contrat.

**La limite, enfin, doit être dite.** La passe de revalidation qui a résolu la clôture de l'acquisition et documenté l'échec sur FTM a été menée sans vote adversarial à trois juges — un « meilleur effort borné », une passe de recherche par lacune, hors du budget de vérification complet[^17]. Ses verdicts sont adossés à des sources primaires, et plusieurs sources bloquées aux outils ont été substituées par des miroirs documentés à chaque fois. Ils n'ont pas le statut probatoire des entrées confirmées par vote 3-0. La revalidation est un filet, pas une garantie.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

**Premièrement**, le blueprint porte cinq lacunes propres, une sixième ayant été résolue : la position au Magic Quadrant iPaaS n'est pas vérifiée ; l'éditeur ne publie aucune architecture agentique propre aux services financiers ; la chaîne FTM/ISO 20022 reste au niveau [C] après une élévation tentée et échouée ; cinq des sept correspondances réglementaires sont des inférences d'auteur — une seule est documentée, pour le seul rôle opérationnel d'IBM Canada sur les rails, et la septième est une attente réglementaire ; et le document est daté de juillet 2026. **Deuxièmement**, cinq événements le périmeront, dont quatre portent déjà une date ou une fenêtre : la révision protocolaire à douze jours, les échéances réglementaires d'août 2026 à moins de six semaines, la cible de lancement du *Real-Time Rail* au quatrième trimestre 2026, et l'entrée en vigueur commune à neuf mois et demi. Un seul, l'arrêté de désignation, demeure sans date. **Troisièmement**, le protocole de revalidation existe, il est écrit, et ses propres limites le sont aussi.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas que ces lacunes disqualifient le blueprint : une architecture dont on connaît les zones aveugles reste utilisable, à condition de ne rien y bâtir de central. Il ne dit pas non plus que la liste soit exhaustive — elle recense ce que le socle de cet ouvrage a détecté, non ce qui existe. Il ne dit surtout pas que le portefeuille décrit en Partie VII soit recommandé : il est un cas d'instanciation documenté par sources primaires, dont les alternatives figurent au chapitre 7, et dont les faits négatifs sont exposés ici au même titre que les capacités.

Un blueprint honnête n'est pas un blueprint sans lacunes. C'est un blueprint dont les lacunes sont écrites, datées, et surveillées.

---

## Notes

[^1]: PRD Annexe B.5 (lacunes propres au blueprint, six points) ; PRD §10.6 (lacune « portefeuille IBM », mise à jour à la passe P0 du 16 juillet 2026). Le décompte retenu ici — cinq lacunes subsistantes sur six énumérées — résulte de la résolution du point 3 (clôture de l'acquisition Confluent).

[^2]: PRD §7.8, **F-41** (niveau [B], réserve levée le 16 juillet 2026). Sources primaires : documentation IBM `ibm.github.io/event-automation`, lue intégralement (« Event Streams and Event Processing are deprecated and no enhancements will be provided » ; les futures solutions Kafka/Flink « will be delivered by IBM Confluent » ; Event Endpoint Management maintenu) ; newsroom.ibm.com du 8 décembre 2025 (annonce, ~11 G$ de valeur d'entreprise) et annonce de clôture (« IBM has acquired all of the issued and outstanding common shares of Confluent for $31 per share in cash ») ; SEC PREM14A Confluent. Chronologie : 8 déc. 2025 → 12 janv. 2026 (expiration HSR) → 12 févr. 2026 (approbation des actionnaires) → 17 mars 2026 (clôture). Trace de la revalidation : `verification/revalidation-2026-07-16.md`, P0.1 point 3.

[^3]: PRD §7.8, **F-38** (niveau [B]). Sources : newsroom.ibm.com (18 déc. 2023 ; 1er juill. 2024) ; sec.gov (10-Q T3-2024) ; pages produits ibm.com (extraits indexés — pages bloquées au fetch automatisé). **Attribution obligatoire (§8.2.7)** : l'étude Forrester *Total Economic Impact* (ROI 176 %) est **commandée par IBM**. Positions vérifiées : Leader du Forrester Wave iPaaS Q3 2025 et du Gartner Magic Quadrant **API Management** 2025.

[^4]: PRD §8.1, garde-fou **R-6** : « IBM est Leader du Gartner Magic Quadrant iPaaS » est **non vérifié** — aucune annonce correspondante trouvée pour 2025-2026 ; ne pas confondre les quadrants. Repris en PRD Annexe B.5 point 1 et §10.6. Ce garde-fou est porté au principal par le ch. 22.

[^5]: PRD §7.8, **F-46** (haute pour l'attribution ; niveau [B]). Source primaire : `ibm.com/think/architectures/patterns/agentic-ai` (patron officiel « Agentic AI », mis à jour le 21 février 2025, lu via navigateur) — « workflows statiques » (*static workflows*) explicitement recommandés pour les processus sous surveillance réglementaire. **Réserve F-46** : patron générique — IBM ne publie pas d'architecture agentique spécifique aux services financiers (vérifié : introuvable sur ibm.com/architectures et Redbooks). Convergence à trois sources : F-36 (manifeste APM, ch. 6), F-37 (options d'orchestration OO1–OO4, ch. 5), F-46 — PRD Annexe B.1 principe 1. **Correctif du socle du 16 juill. 2026 (F-46)** : l'adjectif « indépendantes » est **retiré**, réfuté par le socle lui-même — deux recoupements documentés : Rinderle-Ma cosigne F-36 et F-37 (§7.7), et IBM Research figure parmi les organisations des 18 auteurs de F-36 tandis qu'IBM publie F-46. Formulation imposée par F-46, reprise ici au corps ; jamais « trois sources indépendantes recommandent l'encadrement déterministe ». Chevauchements détaillés au ch. 13 §13.2 ; rappel au ch. 22 §22.1.

[^6]: PRD §7.8, **F-39** (niveau [B]). Sources : pages produits et cycle de vie ibm.com (extraits) ; community.ibm.com (billets officiels lus intégralement). IBM MQ 10.0 LTS (GA juin 2026) : messagerie « exactement une fois » (*exactly-once*), haute disponibilité native, cryptographie post-quantique pour TLS, OpenTelemetry. App Connect Enterprise 13 (13.0.7, mars 2026) : solution dédiée « App Connect Enterprise Solution for ISO 20022 Messaging » (page de support IBM).

[^7]: PRD §10.6 et Annexe B.5 point 4 ; **réserve F-39** (lien MQ ↔ ISO 20022 seulement indirect, via *Financial Transaction Manager* et Redbooks — niveau **[C]** pour ce point précis). Détail de l'échec d'élévation : `verification/revalidation-2026-07-16.md`, P0.2 point 4 (FTM confirmé actif jusqu'à la version 4.0.8 sur `ibm.com/docs/en/ftmfm` ; lien confirmé par citation directe d'un Redbook de 2016 uniquement ; source non-Redbook localisée — PDF officiel du 4 février 2025 sur la solution ISO 20022 d'App Connect Enterprise — ne nommant ni FTM ni MQ ; `ibm.com/docs` en 403 systématique). Règle appliquée : PRD §10 — une entrée [C] ne porte jamais un fait central sans élévation préalable ; PRDPlan §2 — l'échec d'élévation ne bloque pas la suite, la lacune reste écrite.

[^8]: PRD §8.1, garde-fou **R-7** ; §7.8, **F-44** et **F-45** ; PRD Annexe B.3 et B.5 point 5. **Décompte du tableau B.3** (sept liens) : cinq portent « inférence d'auteur » (E-23, AMF, Loi 25 art. 12.1, ACVM 11-348, B-13), un porte « **Documenté** pour le rôle d'IBM ; solution ISO 20022 niveau [C] » (rails Lynx/RTR), un porte « Attente réglementaire — ne rien anticiper » (cadre bancaire C-15). Développement des quatre statuts : ch. 23 §23.1. *La formulation expéditive de B.5 point 5 (« tout mapping réglementaire = inférence d'auteur ») est contredite par B.3 lui-même et par PRDPlan §4.4 ; c'est B.3 qui est suivi ici, conformément à CA-8.* **Cas du fait négatif établi** (formulation imposée, PRDPlan §4.4) : aucun lien documenté IBM ↔ E-23 / B-13 — l'éditeur ne revendique aucune conformité à ces exigences. **Cas général** : l'inférence d'auteur est énoncée sans y adjoindre d'absence de revendication — F-44 atteste au contraire des **revendications d'IBM** portées par l'add-on « Compliance Accelerators » de watsonx.governance (accord OEM Credo AI, 28 avril 2025, source primaire credo.ai) pour l'**AI Act européen, ISO/IEC 42001 et le NIST AI RMF**. **Lien documenté** : F-45 — IBM Canada « lead technology partner » de Lynx (payments.ca, annonce du 2 mai 2019 ; lancement 1er sept. 2021) et partenaire de livraison et d'exploitation du RTR (16 avril 2024, avec CGI et Interac ; **F-29 [A]**, revalidée le 16 juillet 2026, **prime pour l'énumération** et liste **Deloitte Canada** en quatrième partenaire, rôle non détaillé dans la source — voir ch. 15 §15.2 et ch. 23 note 8) ; sources primaires payments.ca et canada.newsroom.ibm.com. **PRD §8.4(5)** : ce rôle est un fait de contexte, pas un argument de conformité.

[^9]: PRD §10.6 (résidus de la lacune « portefeuille IBM ») ; §7.8, **F-42** (réserve : date de l'annonce du cadre *Agent Connect* absente de la page IBM) et **F-45** (réserves : aucune annonce IBM 2024-2026 avec Scotia, CIBC, BNC, Desjardins, Manuvie, Sun Life ou Intact ; étude de cas d'un pilote d'IA générative avec TD attestée par la seule page IBM — TD ne nomme pas IBM dans son propre communiqué ; montants des contrats Lynx/RTR non publics). Blocage documentaire : pages www.ibm.com refusant le fetch automatisé (403) — PRD §7.8, réserve transversale, et §13 (risque « sources primaires inaccessibles aux robots »).

[^10]: PRD §7.4, **F-35** (niveau [A], fait négatif vérifié 9-0) et §10.1 ; garde-fou **R-5** (§8.1). Formulation imposée (PRDPlan §4.4) : au 16 juillet 2026, aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; la candidature de FDX (*Financial Data Exchange*) relève du commentaire d'industrie (Fasken, Bennett Jones, NCFA). Sources : gazette.gc.ca ; canada.ca (communiqué et Budget 2025) ; bankofcanada.ca. Revalidé le 16 juillet 2026 (`verification/revalidation-2026-07-16.md`, P0.1 point 2 — INCHANGÉ). Garde-fou porté au principal par le ch. 14 ; flux 3 du blueprint : ch. 23.

[^11]: PRD §7.4, **F-29** (niveau [A]) ; garde-fou **R-4** et **réserve F-29** — les deux se balayent ensemble (PRDPlan §4.3). Source primaire : payments.ca (quatre pages officielles ; page RTR vérifiée le 16 juillet 2026). Cible officielle de lancement : T4 2026 (lancement graduel, déploiement se poursuivant en 2027), ISO 20022 dès le lancement ; tests industriels (*industry solution assurance testing*) en cours à la mi-2026 — le système n'est pas en production à la mi-juillet 2026. Cibles successives — 2019, puis 2022, puis 2023, puis 2026 (ce sont les cibles annoncées, non les dates auxquelles les reports ont été décidés). Règlement administratif (*By-law No. 10*, Gazette partie II, 1er juillet 2026) en vigueur le **24 août 2026**. Chapitre porteur : ch. 15.

[^12]: PRD §7.4, **F-34** (niveau [A]). Sources primaires : gazette.gc.ca (Gazette du Canada, partie I, vol. 160, no 26, 27 juin 2026) ; canada.ca / Finances Canada (communiqué du 26 juin 2026). Période de commentaires de 60 jours close le **26 août 2026** ; entrée en vigueur échelonnée (accréditation d'abord, puis règles communes et frais d'évaluation dans l'année suivant la publication finale) ; phasage par produits et services précisé à la publication finale. Chapitre porteur : ch. 14.

[^13]: PRD §7.1, **F-01** (niveau [A]) — fait chaud à resurveiller en phase P4.1. Spécification en vigueur à la date de gel : révision **2025-11-25** (modelcontextprotocol.io), revalidée le 16 juillet 2026. Révision attendue en finalisation le **28 juillet 2026** : *release candidate* verrouillée le 21 mai 2026 (refonte sans état, retrait de `Mcp-Session-Id`, nouveaux en-têtes `Mcp-Method` / `Mcp-Name`), décrite par les mainteneurs comme la plus importante révision depuis le lancement. Trace : `verification/revalidation-2026-07-16.md`. **Réserve F-01** : dire « cadre d'autorisation », jamais « sécurisé ». Chapitre porteur : ch. 2.

[^18]: PRD §7.8, **F-40** (niveau [B]) — trace CA-8 du composant C1 cité ici. Sources : ibm.com/new et ibm.com/docs (extraits — pages bloquées au fetch automatisé) ; community.ibm.com (billets officiels sur l'AI Gateway, lus). **API Connect V12** : 12.1.0 disponible le **15 décembre 2025** (annonce « for the agentic AI future ») ; **support MCP documenté** aux docs 12.1.0 — enregistrement de fournisseurs LLM pour accès gouverné et **génération d'outils et de serveurs MCP à partir des définitions d'API existantes**. **AI Gateway** : annoncé **mai 2024**, étendu **janvier 2025** — limites de débit par requêtes ou par tokens, cache de réponses, masquage, chiffrement, audit. Statuts conformes à PRD §8.4(1) : capacités attribuées à la documentation de l'éditeur, datées. Composant tracé en PRD Annexe B.2, ligne C1.

[^14]: PRD §7.3, **F-09** (entrée **[A/B mixte]** — **[A]** pour les faits des passes 1-2, **[B]** pour les exigences opératoires extraites du texte intégral le 16 juill. 2026 ; les seuls faits mobilisés ici, la date de publication et la date d'entrée en vigueur, relèvent de la strate **[A]**. Une extraction de source primaire n'« élève » pas une entrée déjà votée 3-0 : dans la taxonomie §7, [B] est **sous** [A]. Source primaire osfi-bsif.gc.ca — E-23 finale publiée le 11 septembre 2025, en vigueur le 1er mai 2027) et **F-25** (niveau [A] ; sources : lautorite.qc.ca, Norton Rose Fulbright, rapport annuel Desjardins 2025 — ligne directrice finale publiée le 30 mars 2026, en vigueur le 1er mai 2027). **Réserve F-25** : ne jamais écrire « en attente » ni « en projet ». **Règle §8.2.4** : E-23 ne nomme ni l'agentique ni les agents ; sa couverture est implicite via la définition de « modèle » — voir ch. 9. Chapitres porteurs : ch. 9 (E-23), ch. 11 (AMF), ch. 20 (feuille de route vers le 1er mai 2027).

[^15]: PRDPlan §6, tâche **P4.1** (revalidation temporelle finale : re-vérifier chaque fait chaud à sa source primaire, chapitres touchés amendés avec nouvelle date de gel) et §8, *Definition of Done* point 3 (la revalidation P4.1 date de **moins de 30 jours** au moment de la publication). Principe d'ordonnancement — amender le socle d'abord, les chapitres ensuite : PRDPlan §7, ligne « fait chaud invalidé en cours de rédaction ».

[^16]: PRD **§8.3** (sensibilité temporelle) : revalidation complète des faits « chauds » avant publication — A2A/MCP (dont la révision attendue le 28 juillet 2026), RTR, règlements du cadre bancaire, C-36. La clôture de l'acquisition Confluent, fait chaud jusqu'à la phase P0, est **résolue** (17 mars 2026, F-41) et sort de cette liste. Pièges connus rappelés par §8.3 : ligne directrice AMF finale depuis le 30 mars 2026 ; C-15 sanctionné le 26 mars 2026 ; règlement du cadre bancaire prépublié (texte final susceptible de changer) ; désignation de l'organisme de normalisation technique à venir par arrêté ministériel ; lancement RTR au T4 2026 = cible conditionnelle.

[^17]: PRD Annexe A, complément P0 (v1.3, 16 juillet 2026) : neuf recherches ciblées par agents parallèles sur sources primaires, **sans vote adversarial** (hors budget P0 — « meilleur effort borné », une passe par lacune, PRDPlan §2). Limites consignées dans `verification/revalidation-2026-07-16.md` : plusieurs sources bloquées aux outils automatisés (bmo.com/ir, sec.gov, ibm.com/docs, sunlife.com, a2a-protocol.org — 403 ou dépassement de délai), recoupement par miroirs documenté à chaque fois ; une hallucination détectée et écartée en cours de recherche, non retenue au PRD. Le niveau [A] du socle est réservé au vote adversarial 3-0 (PRD §7).

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (18 notes, chacune avec trace F-xx / §PRD et source primaire ;
                                   termes anglais en italique entre parenthèses à la 1re occurrence AU CORPS :
                                   static workflows, exactly-once (§24.1, corrigé en relecture), Financial Data
                                   Exchange (§24.2, corrigé en relecture), industry solution assurance testing,
                                   By-law No. 10, release candidate, Definition of Done)
     3. Balayage garde-fous ...... fait — R-5 (aucun standard désigné, FDX = anticipation d'industrie) ;
                                   R-6 (position MQ iPaaS non vérifiée ; quadrants non confondus — Forrester Wave
                                   iPaaS Q3 2025 et Gartner MQ API Management 2025 distingués) ;
                                   R-4 + réserve F-29 balayés ensemble (cible T4 2026 annoncée ; jamais « lancé ») ;
                                   R-7 : les QUATRE statuts de correspondance produit ↔ réglementation tenus
                                   distincts, conformément au tableau B.3 et au ch. 23 §23.1 (inférence adossée à un
                                   fait négatif établi pour E-23/B-13 ; inférence simple sans mention d'absence de
                                   revendication — F-44 atteste les REVENDICATIONS D'IBM pour AI Act / ISO 42001 /
                                   NIST AI RMF ; lien documenté pour le rôle d'IBM Canada sur les rails, F-45,
                                   §8.4(5) ; attente réglementaire pour le cadre bancaire) ;
                                   R-8 : balayage `\bACP\b|control plane|plan de contrôle` (PRDPlan §4.3) — ZÉRO
                                   occurrence dans le corps et dans les notes ; garde-fou sans objet ici, porté par
                                   les ch. 1 §1.2, 3, 17 §17.8, 21 et 22 §22.2 ; §8.2.7 : Forrester TEI attribué à
                                   son commanditaire (IBM) ; §8.4 : alternatives par renvoi au ch. 7, aucun
                                   superlatif, faits négatifs exposés (dépréciation Event Streams/Event
                                   Processing, R-6, R-7) ; §8.4(1) : capacités IBM du corps datées et statuées
                                   (ACE 13.0.7 mars 2026 ; MQ 10.0 LTS GA juin 2026 ; API Connect 12.1.0
                                   15 déc. 2025 ; AI Gateway mai 2024/janv. 2025)
     4. Relecture adversariale ... FAIT (deux relecteurs indépendants, 16 juillet 2026 — 7 constats bloquants,
                                   9 réserves ; tous vérifiés au socle et FONDÉS ; tous appliqués).
                                   Réfuté et corrigé :
                                   (a) « trois sources indépendantes » (§24.1) — formule nommément proscrite par
                                       F-46, réfutée par le socle (Rinderle-Ma cosigne F-36/F-37 ; IBM Research
                                       parmi les auteurs de F-36, IBM publie F-46) et contredisant le ch. 22 §22.1,
                                       le ch. 13 §13.2 et l'abstract du TOC → formulation imposée de F-46 reprise
                                       au corps et à la note [^5] ;
                                   (b) universel « toute correspondance réglementaire est une inférence » (titre
                                       §24.1, §24.3, conclusion) — faux : B.3 porte 5 inférences, 1 lien documenté,
                                       1 attente réglementaire ; faisait disparaître la catégorie « documenté »
                                       qu'exige CA-8 → décompte réel du ch. 23 substitué aux trois endroits ;
                                   (c) « deux cas […] et le chapitre 23 les tient » — le ch. 23 §23.1 en tient
                                       QUATRE → quatre statuts rétablis, y compris le lien documenté (F-45) ;
                                   (d) conclusion §24.2 : le décompte des calendrés scindait l'échéance d'août en
                                       deux et FAISAIT DISPARAÎTRE le lancement du RTR (F-29, cible T4 2026) →
                                       recomposé sur les cinq événements du corps ;
                                   (e) « le socle atteste […] des contenus de conformité prêts à l'emploi » —
                                       revendication d'éditeur transformée en fait attesté, reprise du registre
                                       marketing sans statut → « revendications d'IBM », add-on Compliance
                                       Accelerators, accord OEM Credo AI du 28 avril 2025 (PRDPlan §4.4, §8.4(1)) ;
                                   (f) capacité C1 (génération de serveurs MCP, gouvernance des appels LLM) énoncée
                                       sans trace, sans date, sans statut ; F-40 absent du chapitre → note [^18]
                                       créée, F-40 porté à l'en-tête (CA-8, PRDPlan §5) ;
                                   (g) en-tête « Socle mobilisé » omettant F-38, F-39, F-40 et F-42, pourtant
                                       porteurs d'affirmations centrales → complété ;
                                   (h) journal de boucle qualité attestant un balayage R-8 sur des passages
                                       INEXISTANTS dans le chapitre (constat copié d'un autre chapitre) → remplacé
                                       par l'état réel ; ligne CA-5 attestant deux gloses non faites au corps →
                                       gloses portées au corps et ligne corrigée. PRDPlan §1.4 : « un statut qui
                                       ment est pire qu'un statut absent » ;
                                   (i) « robuste sur le fond » (jugement non attribué sur une publication de
                                       l'éditeur, §8.4(3)) → « explicite sur le fond » ; classement du « plus fort
                                       potentiel de réécriture » (§24.2) → marqué « Lecture de l'auteur » ;
                                   (j) flux 2 présenté sous le titre RTR alors qu'il porte sur Lynx (B.4, ch. 23
                                       §23.3) → rectifié ; (k) renvoi « quatre lacunes suivantes » contredisant
                                       « cinq subsistent » quinze lignes plus haut → renvoi de la 5e aux §24.2/24.3.
                                   Aucun constat écarté.
     4bis. Passe F-09 (16 juill. 2026) . Marquage de la note [^14] rectifié : F-09 est [A/B mixte] ; le chapitre ne
                                   mobilise que la strate [A] (dates), rappel que [B] est SOUS [A]. Trois autres
                                   corrections sans objet ici : aucune affirmation d'absence d'extraction d'E-23,
                                   aucun « exigé par E-23 » (les occurrences d'« exigence » sont les formulations
                                   imposées de PRDPlan §4.4 ou étrangères à E-23), zéro « fiche de modèle ».
     4ter. Passe corrective ..... Audit du 17 juill. 2026, périmètre m-36 à m-39. Aucune information nouvelle n'entre :
                                   date de gel INCHANGÉE au 16 juillet 2026.
                                   [m-36] §24.1 : « Ce fait négatif a été **vérifié** ; il est écrit » → « **est
                                     établi** ». [m-37] §24.1 : « L'absence de revendication est **vérifiée** pour E-23
                                     et B-13, et pour eux seuls » → « est **établie** ».
                                     Motif commun : PRDPlan §4.4 (v1.4), ligne « **Trois degrés d'absence —
                                     vocabulaire imposé** », arbitrage du 17 juill. 2026 (racine G-1 de l'audit).
                                     F-44 et F-45 portent une **réserve d'absence de lien dans le corpus** — degré 2,
                                     « établi » ; le degré 1, « vérifié », est réservé au **balayage documenté d'un
                                     texte** : F-35, F-09, F-46, et elles seules. Ce chapitre et le ch. 23 disaient
                                     l'inverse l'un de l'autre en citant chacun le même document ; ils convergent.
                                     Balayage `vérifi` sur TOUT le fichier (exigence de complétude de la correction) :
                                     aucune autre occurrence ne porte sur le fait négatif F-44/F-45. Les autres sont
                                     légitimes et INTACTES — F-35 (§24.2 point 1 et note [^10], « fait négatif vérifié
                                     9-0 ») ; F-46 (§24.1 et note [^5], « vérification faite sur le catalogue
                                     d'architectures ») ; R-6 (« non vérifiée », §24.1, conclusion, note [^4]).
                                   [m-38] note [^8] : énumération des partenaires du RTR incomplète — « avec CGI et
                                     Interac » est la forme de F-45. **Deloitte Canada** ajouté en quatrième
                                     partenaire, avec la réserve du socle (rôle non détaillé dans la source) : F-29 [A],
                                     revalidée le 16 juill. 2026, **prime pour l'énumération** — règle posée au ch. 23
                                     note [^8], défaut déjà corrigé au ch. 22 §22.3 en relecture. F-29 était déjà à
                                     l'en-tête (renvois) : rien à y ajouter de ce fait.
                                   [m-39] en-tête : **F-36** et **F-37** ajoutés aux renvois — mobilisés au §24.1
                                     (convergence à trois sources) et en note [^5]. Décompte recompté sur le fichier :
                                     **16 entrées** à l'en-tête = balayage `F-[0-9]+` du corps et des notes, à
                                     l'identique.
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     Contrôle CA-8 (PRDPlan §5) : chaque composant et correspondance cité ici est tracé vers F-38..F-46 ou le socle
     général (C1 → F-40, note [^18] ; C3 → F-39, notes [^6]/[^7] ; C6 → F-44, note [^8] ; rails → F-45, note [^8]) ;
     chaque lien réglementaire porte son statut explicite (tableau B.3 : 5 inférences, 1 documenté, 1 attente).
     Arithmétique vérifiée contre le socle : 8 déc. 2025 → 17 mars 2026 = 3 mois et 9 jours ; 16 juill. → 28 juill.
     2026 = 12 jours ; 16 juill. → 26 août 2026 = 41 jours ; 16 juill. 2026 → 1er mai 2027 = 9 mois et demi (289 j) ;
     B.5 : 6 points énumérés, 1 résolu (point 3), 5 subsistants ; B.3 : 7 liens = 5 + 1 + 1.
     GOUVERNANCE — à remonter à l'orchestrateur (non corrigé ici, PRD hors périmètre de cette passe) :
     PRD Annexe B.5 point 5 (« tout mapping réglementaire = inférence d'auteur, jamais revendication IBM ») est
     contredit par le tableau B.3 du même PRD (1 lien documenté, 1 attente réglementaire) et par PRDPlan §4.4.
     B.3 fait foi ici (CA-8 le nomme explicitement). B.5 point 5 à amender. -->
