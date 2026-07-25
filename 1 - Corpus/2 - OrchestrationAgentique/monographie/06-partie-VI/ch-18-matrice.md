# Chapitre 18 — La matrice protocoles × exigences réglementaires

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | **Transversal** ([TOC.md](../../TOC.md) n'assigne à ce chapitre aucune liste F-xx — signalé à la gouvernance). Entrées effectivement mobilisées : **F-01, F-02, F-04, F-16** (protocoles — ch. 1 à 4) ; **F-09, F-25, F-26, F-27** (exigences — ch. 9, 11, 12) ; **F-11, F-34, F-35** (cadre bancaire — ch. 14) ; **F-36, F-37** (frames et options d'orchestration — ch. 5, 6, 13) ; **F-05, F-08, F-10, F-15** en renvoi (ch. 1, 3, 7, 8, 9) |
| Garde-fous à surveiller (PRD §8) | **réserve F-09** (« attendu par E-23 », jamais « exigé » ; « documentation de modèle » / « inventaire », jamais « fiche de modèle ») ; **réserve F-01** (« cadre d'autorisation », jamais « sécurisé ») ; **§8.2.1** (soutien ≠ production — décompte AP2) ; **§8.2.4** (couverture agentique d'E-23 : formulation imposée) ; **R-5** (aucun standard technique désigné — formulation imposée) ; **réserve F-25** (jamais « en attente » ni « en projet ») ; motif **R-7** (« E-23 ») : ressort en contexte réglementaire pur, aucune correspondance produit ↔ réglementation dans ce chapitre — filtré (PRDPlan §4.3) ; motifs **R-1** et **R-8** : zéro occurrence |
| Volumétrie cible | ~2600 mots |

> **Thèse ([TOC.md](../../TOC.md))** : croiser la pile protocolaire (MCP/A2A/AP2) avec les exigences canadiennes (E-23, AMF, art. 12.1, 11-348, cadre bancaire) révèle où les standards suffisent et où l'architecture doit compenser.

---

Les quatre premières parties ont dressé deux inventaires qui ne se sont jamais rencontrés : une pile protocolaire consolidée sous gouvernance neutre, dont les chapitres 1 à 4 ont établi l'anatomie, la doctrine d'articulation et les angles morts ; un corpus d'exigences canadiennes dont les chapitres 9 à 12 et 14 ont établi le contenu, et ses limites. Le présent chapitre les croise.

Le résultat n'est pas celui qu'un titre de matrice laisse attendre. **Sur les quinze croisements que porte la matrice — trois protocoles, cinq exigences —, aucun n'est documenté par une source du socle.** Aucune source du socle ne documente qu'une spécification protocolaire mentionne un texte canadien, ni l'inverse — absence de documentation dans le corpus de cet ouvrage, non fait négatif vérifié. Cette matrice n'est donc pas un tableau de correspondances : c'est un tableau de vides. Son intérêt tient à ceci que ces vides ne sont pas de même espèce, et qu'ils désignent en négatif le lieu exact où l'architecture doit compenser.

Trois propositions. La première : la matrice est un objet dont il faut fixer les règles de remplissage, faute de quoi elle produira de la plausibilité au lieu d'un constat. La deuxième : lue par protocole, elle montre que la couche protocolaire répond à des questions — qui parle, par quel format, avec quelle habilitation — que les textes canadiens ne posent pas. La troisième : lue par texte, elle montre que ceux dont le socle porte le contenu le plus précis sont ceux auxquels les protocoles répondent le moins.

Le chapitre 13 a posé la traduction des exigences en cadres (*frames*) ; ce chapitre ne la refait pas et y renvoie. Sa valeur propre est ailleurs : la matrice comme objet, ses deux lectures, les zones de compensation.

## 18.1 Construction de la matrice

Trois règles de remplissage, sans lesquelles l'exercice serait un exercice d'analogie.

**Première règle — deux termes par cellule.** Une cellule n'est renseignable que si le socle porte les deux choses : ce que l'exigence attend, et ce que le protocole fournit. La condition n'est pas également servie d'une ligne à l'autre. Depuis l'extraction du texte intégral d'E-23 — EN et FR, le 16 juillet 2026 —, le socle porte la définition verbatim de « modèle » et cinq domaines d'attentes opératoires : cycle de vie, inventaire d'entreprise, cotation graduée, documentation de modèle, surveillance continue[^1]. La ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers, elle, n'est au socle que par son calendrier[^2] : c'est la seule ligne où le premier terme manque, et ce chapitre ne le comble pas.

**Deuxième règle — aucune cellule ne porte un verdict de conformité.** Le socle ne relie aucun protocole à aucun texte canadien ; il faut distinguer, comme le chapitre 13 l'exige de lui-même, une absence **au socle** d'un **fait négatif vérifié** dans la source. Cette matrice porte deux faits négatifs vérifiés — F-09 et F-35 —, l'un et l'autre bornés à ce qui a été cherché.

**Troisième règle — toute cellule non vide est une inférence d'auteur.** Le rapprochement entre une propriété protocolaire et une obligation canadienne est un raisonnement de l'auteur, jamais une lecture.

| Texte canadien (traitement) | Ce que le socle porte de sa demande | MCP (F-01) | A2A v1.0 (F-02, F-16) | AP2 (F-04) |
|---|---|---|---|---|
| **E-23 — attentes de risque de modèle** (ch. 9)[^1] | Définition verbatim de « modèle », laissée « intentionally broad » ; cinq domaines d'attentes opératoires — inventaire d'entreprise (§C.1, Appendice 1), cotation de risque par modèle (§C.2), cycle de vie à cinq volets (§A.4), documentation de modèle (§D.2), surveillance continue visant la décision et la reparamétrisation autonomes (§D.2, principe 3.6) | **Fait négatif vérifié** (vocabulaire) : agentique / agents / orchestration absents du texte intégral, EN et FR | *idem* — aucun agent nommé | *idem* — aucun agent nommé |
| **Ligne directrice IA de l'AMF** (ch. 11)[^2] | Le calendrier seul : finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 | Rien de croisable | Rien de croisable | Rien de croisable |
| **ACVM 11-348** (ch. 12)[^3] | Doctrine (l'avis ne crée ni ne modifie aucune exigence) ; définition captant autonomie et adaptativité **après déploiement** | Rien sur l'auto-modification | Rien sur l'auto-modification | Rien sur l'auto-modification |
| **Art. 12.1, Loi 25** (ch. 11)[^4] | Trois obligations, libellé officiel : **informer**, **expliquer**, **réviser** | Données typées = substrat de frontière, non trace d'instance | Cartes d'agents signées = identité de l'appelant, non explication | Rien au socle (anatomie non portée) |
| **Cadre bancaire — standard technique** (ch. 14)[^5] | Exigence d'un standard unique ; organisme à désigner par arrêté ministériel ; **aucun standard nommé** | **Fait négatif vérifié** : « OAuth » absent des textes officiels | Rien au socle | Rien au socle |

> **État de la recherche — aucune source du socle ne relie un protocole agentique à un texte réglementaire canadien**
>
> Question : le socle documente-t-il un lien — de conformité, de correspondance, ou de simple mention — entre MCP, A2A ou AP2 et l'un des textes canadiens des Parties III et IV ?
>
> Lacune ouverte le 16 juillet 2026 ; **aucune passe de recherche n'a été conduite** — hors périmètre de la phase P0, qui a revalidé les faits chauds sans instruire ce croisement. Aucune entrée du socle, relue une à une, ne porte un tel lien : les sources protocolaires sont des spécifications et des communiqués de fondation, les sources réglementaires des textes officiels canadiens. Sources à retrouver : modelcontextprotocol.io, a2a-protocol.org, spécification AP2, osfi-bsif.gc.ca, lautorite.qc.ca. La question reste ouverte ; aucune inférence n'est proposée ici.
>
> **Deux exceptions, et elles sont de méthode.** Deux absences ont été **cherchées dans la source** plutôt que **constatées au socle**, et leur portée est bornée par ce qui a été cherché. F-09 : le texte intégral d'E-23 a été balayé mécaniquement, EN et FR, pour « agentique », « agents » et « orchestration » — zéro occurrence[^1] ; le fait négatif porte sur le **vocabulaire agentique**, les chaînes « MCP », « A2A » et « AP2 » n'ayant pas été cherchées. F-35 : les chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » ont été cherchées exhaustivement dans les textes officiels du cadre bancaire, avec zéro occurrence[^5] (§18.2). Partout ailleurs, l'absence est documentaire et non établie.

## 18.2 Lecture par protocole

**MCP** (*Model Context Protocol*) répond à une question : comment un agent atteint un outil. Interface client-serveur fondée sur JSON-RPC 2.0, invocation d'outils, échange de données typées, cadre d'autorisation (*authorization framework*) fondé sur OAuth — et jamais « sécurisé », la sécurité dépendant de l'implémentation[^7]. Deux croisements méritent l'examen ; aucun ne survit.

Le premier oppose le typage à l'obligation d'expliquer. Le chapitre 2 a établi qu'un échange typé est déclaré à l'avance, donc vérifiable à la frontière et opposable après coup — sans que le socle établisse qu'il suffise à une piste d'audit réglementaire[^7]. **Lecture de l'auteur** : l'article 12.1 exige, sur demande, « les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision »[^4]. Un journal typé atteste de la forme de ce qui a transité par un appel d'outil ; il n'atteste ni des raisons, ni des facteurs, ni des paramètres. Le socle porte les deux termes ; leur écart est de l'auteur.

Le second croisement est le seul lexique commun de toute la matrice : OAuth. **Lecture de l'auteur** — que le fondement du cadre d'autorisation de MCP[^7] et l'anticipation d'industrie relative au cadre bancaire[^5] emploient le même mot est un rapprochement de l'auteur, que le socle ne pose pas. Il vaut d'être posé pour être aussitôt désamorcé : au 16 juillet 2026, **aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie**[^5][^8]. Cette intersection a été cherchée dans la source, et ne s'y trouve pas.

**A2A** (*Agent2Agent*) répond à une autre question : comment un agent délègue à un autre. Délégation de pair à pair, cartes d'agents (*Agent Cards*), dont la variante signée (*Signed Agent Cards*) porte une vérification cryptographique d'identité ; version 1.0 que le projet qualifie lui-même de première spécification stable[^9]. La doctrine de complémentarité déclarée par le projet A2A — « MCP dans les agents, A2A entre les agents » — rend les colonnes de cette matrice séparables ; le chapitre 2 a établi qu'un critère de découpage n'est pas une contrainte[^10].

Le croisement tentant est celui de la carte signée avec l'imputabilité. Il échoue deux fois. D'abord parce que le chapitre 4 l'a établi : le cadre d'autorisation de MCP et la carte d'agent signée d'A2A établissent tous deux **qui** parle, non ce qui est dit ni si ce qui est dit est fondé[^11]. Ensuite parce que le porteur de l'obligation canadienne n'est pas l'agent. **Lecture de l'auteur** : sous l'article 12.1, l'obligation pèse sur l'entreprise qui rend la décision[^4] ; aucune identité d'agent ne déplace ce porteur — le chapitre 13 en a fait le pivot de son argument.

**AP2** (*Agent Payments Protocol*) est la ligne la plus vide, et la plus instructive. Protocole compagnon d'A2A pour les transactions pilotées par agents, lancé par Google en septembre 2025 ; plus de 60 organisations des paiements et des services financiers déclarent leur soutien à AP2 (communiqué de la Linux Foundation, 9 avril 2026) ; le soutien déclaré ne vaut pas déploiement en production[^12]. Le socle ne porte pas son anatomie technique (ch. 3), ne documente aucun transfert de gouvernance à une fondation (ch. 1), et ne le relie à aucun rail canadien — lacune ouverte, traitée au chapitre 16[^13].

**Lecture de l'auteur** : une relation inverse apparaît. Des trois protocoles, celui qui touche le plus directement l'acte réglementé — le paiement — est celui dont le socle documente le moins : ni anatomie, ni gouvernance, ni articulation canadienne. Leur convergence sur une même ligne est une lecture, et elle borne cet ouvrage avant de borner AP2 : une institution qui l'instrumenterait en premier ne trouvera ici ni sa structure de message, ni son mandat, ni sa preuve d'intention — elle doit remonter aux sources primaires. Aucune de ces absences n'établit un fait négatif sur le protocole lui-même[^13].

## 18.3 Lecture par exigence

Lue par ses lignes, la matrice se réorganise en **trois espèces** — et la distinction n'est pas rhétorique : deux vides d'espèces différentes n'appellent pas la même conduite.

**Vide de socle — une ligne** (ligne directrice de l'AMF). Ces cellules sont vides parce que l'ouvrage ne sait pas ce que le texte attend : la ligne directrice, finale depuis le 30 mars 2026, n'est au socle que par son calendrier, son contenu article par article relevant d'une lacune déclarée[^2]. Seule ligne dont le premier terme manque, et seul vide qu'une extraction primaire comblerait.

**Vide de texte — une ligne** (cadre bancaire). Ces cellules sont vides pour une raison opposée : le socle porte l'exigence — un standard technique unique (*single technical standard*) est requis —, mais le texte officiel ne désigne rien[^5]. Non une lacune de l'ouvrage : un état du droit, et il est vérifié.

**Vide de protocole — trois lignes** (E-23, article 12.1, avis 11-348). Ici, le socle porte la demande, et ce sont les protocoles qui ne portent rien. E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration — vérification mécanique sur le texte intégral, EN et FR (F-09). Sa définition de « modèle », laissée « intentionally broad », englobe les méthodes d'IA et d'apprentissage automatique, et le texte vise expressément la « prise de décision autonome » et la « reparamétrisation autonome » ; d'où une **couverture implicite** que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise[^14]. Ses attentes sont précises : inventaire d'entreprise « accurate, evergreen » dont l'Appendice 1 énumère les champs — dépendances, sources de données, usages approuvés, limites —, cote de risque par modèle, surveillance continue[^1]. **Lecture de l'auteur** : ces champs et le typage de MCP ou la carte signée d'A2A portent sur des objets différents — un inventaire recense des modèles gouvernés, un protocole décrit un appel ; le socle porte les deux termes, leur non-recouvrement est de l'auteur. L'article 12.1 attache trois obligations dont le socle porte le libellé officiel : informer, expliquer sur demande, offrir la révision par un membre du personnel en mesure de réviser[^4]. Le socle ne documente, pour aucun des trois protocoles, d'événement de décision, d'explication d'instance ni d'intervention humaine. L'avis 11-348 capte les systèmes dont l'autonomie et l'adaptativité varient **après déploiement**[^3] ; le socle ne documente, pour aucun protocole, de distinction entre l'adaptation éphémère d'une instance et l'évolution persistante du modèle de processus, que le manifeste sur l'*Agentic Business Process Management* fournit et que le chapitre 13 érige en contrainte[^16].

**Lecture de l'auteur** : le renversement est le résultat le plus utile de ce chapitre. On attendrait que les lignes vides soient celles des textes les moins lisibles. C'est l'inverse. Les deux textes dont le socle porte le contenu le plus précis — E-23, par extraction intégrale, et l'article 12.1, par son libellé officiel — sont ceux dont les six croisements ne portent aucun lien documenté ; et ce sont eux qui obligent le plus tôt : l'un depuis 2023, l'autre au 1er mai 2027[^15]. Pour MCP et A2A, dont le socle porte l'anatomie, ce vide n'est pas documentaire : les deux spécifications décrivent des appels et des délégations, non des décisions. Pour AP2, dont le socle ne porte aucune structure de message[^13], rien ne permet de trancher entre les deux espèces. Un vide de socle se comble par une extraction primaire ; qu'un vide de protocole se comble ou non, cet ouvrage le laisse ouvert.

## 18.4 Les zones de compensation architecturale

Appelons **zone de compensation** un point où le socle établit une demande, ou une contrainte de conception, que la couche protocolaire ne porte pas — et que quelque chose d'autre doit donc porter. Les cinq qui suivent relèvent de la **Lecture de l'auteur** : le socle en porte les termes, jamais la conclusion.

**Z1 — La production de la trace.** L'article 12.1 exige les raisons, facteurs et paramètres de *cette* décision[^4] ; le préprint de la TU Munich enseigne que la journalisation confiée aux agents « n'est généralement pas recommandée »[^18] ; le rapport conjoint du BSIF et de l'ACFC établit que les relations causales entrées-sorties sont souvent indéterminables[^19]. Le chapitre 13 en conclut que le cadre est le lieu de production de la trace. La matrice ajoute le quatrième candidat écarté : le protocole. Le typage de MCP donne un substrat de frontière, non une trace d'instance.

**Z2 — Le point d'arrêt humain.** L'article 12.1 exige l'occasion de présenter ses observations à un membre du personnel en mesure de réviser la décision[^4]. Le socle ne documente d'humain dans aucun des trois protocoles ; il documente l'humain-dans-la-boucle (*human-in-the-loop*) et les points de contrôle (*checkpointing*) au niveau d'un cadriciel d'orchestration — Microsoft Agent Framework[^20] —, jamais au niveau des protocoles. La compensation est à la charge de la couche d'orchestration.

**Z3 — La détectabilité de l'auto-modification.** L'avis 11-348 capte l'adaptativité après déploiement[^3] ; le manifeste APM scinde l'auto-modification en adaptation et évolution[^16] ; E-23 attend une surveillance continue visant nommément la « reparamétrisation autonome »[^1]. Le socle ne documente, pour aucun protocole, de mécanisme rendant le passage de l'une à l'autre détectable. Le chapitre 13 en tire la contrainte ; la matrice établit qu'aucune ligne de la pile ne l'exécute.

**Z4 — L'interface d'accès du cadre bancaire.** Le standard technique n'est pas désigné[^5][^8]. Le chapitre 14 en tire la discipline : traiter le standard d'accès comme une variable derrière une frontière d'abstraction. La matrice précise l'objet — ce n'est pas un choix de protocole agentique, aucun n'étant nommé dans les textes. Le chapitre 23 en instancie le flux.

**Z5 — Le contenu et l'état.** Les réponses protocolaires établissent qui parle ; elles ne couvrent ni l'empoisonnement d'outils (*tool poisoning*), ni l'injection d'invites (*prompt injection*), ni l'empoisonnement de mémoire (*memory poisoning*)[^11][^16]. Le manifeste APM propose l'opérationnalisation locale des *frames* comme frontière de sécurité et de confidentialité — confinement, non prévention[^16]. Les passerelles relèvent de la Partie VII.

**Lecture de l'auteur** : les cinq zones partagent une propriété qu'aucune ne montre seule — aucune ne se referme en choisissant un meilleur protocole. Là où les standards ne suffisent pas, ce n'est pas parce qu'ils seraient immatures : c'est parce qu'ils ne répondent pas à la question posée. La compensation n'est donc pas un palliatif transitoire ; elle est structurelle, et l'architecture de référence du chapitre 19 est l'endroit où elle se construit. Lecture bornée par sa date : le socle documente une révision majeure de MCP attendue le 28 juillet 2026, douze jours après la date de gel, sans en documenter le contenu au regard d'aucune exigence canadienne[^7].

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, la matrice compte quinze croisements et aucun lien documenté : aucune source du socle ne relie MCP, A2A ou AP2 à E-23, à la ligne directrice de l'AMF, à l'avis 11-348, à l'article 12.1 ou au cadre bancaire. Quatre de ces absences ont été cherchées dans la source : les trois cellules de la ligne E-23, où F-09 établit un fait négatif vérifié borné au vocabulaire agentique, et la cellule cadre bancaire × MCP, où F-35 établit l'absence des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » des textes officiels. Les onze autres ne portent qu'une absence au socle, et la distinction est intégralement maintenue. **Deuxièmement**, les vides se répartissent en trois espèces sur les cinq lignes : vide de socle pour la seule ligne directrice de l'AMF, vide de texte pour le cadre bancaire, vide de protocole pour E-23, l'article 12.1 et l'avis 11-348 — trois textes dont le socle porte le contenu et auxquels les protocoles ne répondent rien. **Troisièmement**, cinq zones de compensation architecturale se dégagent — la trace, le point d'arrêt humain, la détectabilité de l'auto-modification, l'interface d'accès du cadre bancaire, le contenu et l'état.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas que les protocoles seraient non conformes aux exigences canadiennes : la conformité n'est pas une propriété qu'un format d'échange puisse porter, et aucune source ne l'évalue. Il ne dit pas que ces quinze absences établissent l'absence d'un lien : onze d'entre elles sont un état de la documentation, non un état du monde, et les quatre autres ne portent que sur les chaînes effectivement cherchées. Il ne dit pas ce que la ligne directrice de l'AMF attend : son contenu n'est pas au socle. Pour E-23, le socle porte les attentes — et ce que ce chapitre ne dit pas, c'est qu'un protocole y réponde. Il ne dit pas que les cinq zones de compensation soient exhaustives : elles procèdent des cinq lignes de cette matrice, dont une est vide du côté des attentes — une extraction primaire de la ligne directrice de l'AMF en ferait vraisemblablement apparaître d'autres. Il ne dit rien, enfin, de ce qu'il faut construire : les couches, leur positionnement sur les options d'orchestration (*orchestration options*) et les points de contrôle obligatoires sont l'objet du chapitre 19 ; leur instrumentation, celui du chapitre 20 ; leur instanciation, celui de la Partie VII.

La matrice n'établit pas que les protocoles échouent. Elle établit qu'ils répondent à une autre question — et que personne, à la date de gel, n'a écrit la phrase qui les relierait au droit canadien.

---

## Notes

[^1]: PRD §7.3, **F-09** (niveau **[A/B mixte]** — **[A]** pour les faits des passes 1-2, issus du vote adversarial 3-0 : date de publication, entrée en vigueur, portée, définition de « modèle » incluant les méthodes d'IA et d'AA, et le fait que la couverture agentique est une inférence d'analystes ; **[B]** pour les **exigences opératoires** extraites du texte intégral d'E-23 le 16 juillet 2026, EN et FR — cycle de vie, inventaire, cotation, documentation et Appendice 1, surveillance continue —, ainsi que pour la vérification négative mécanique. **Ce chapitre mobilise les deux strates** : la définition et le calendrier relèvent de [A], les cinq domaines d'attentes et le fait négatif de [B]. **Point de méthode** : une extraction de source primaire n'« élève » pas une entrée déjà votée 3-0 — dans la taxonomie du PRD §7, [B] est **sous** [A] ; elle l'**enrichit** d'un contenu de rang inférieur. Un état antérieur de cette note écrivait « élevée [C]→[B] », doublement faux (l'entrée n'a jamais été [C], et [B] n'est pas au-dessus de [A]) : marquage rectifié au socle, PRD v1.7. Source primaire : osfi-bsif.gc.ca, ligne directrice E-23 (version finale du 11 septembre 2025, en vigueur le 1er mai 2027 ; institutions financières fédérales, y compris succursales étrangères dans la mesure compatible). **Modalité, contraignante ici (réserve F-09, PRDPlan §4.4)** : E-23 est **fondée sur des principes**, rédigée au conditionnel (« should ») — écrire « attendu par E-23 », jamais « exigé par E-23 » ; parler de « documentation de modèle » et d'« inventaire », jamais de « fiche de modèle » (0 occurrence dans E-23). Faits mobilisés : **définition de « modèle » (§A.4)**, verbatim — « Application de techniques statistiques ou d'hypothèses théoriques, empiriques ou fondées sur un jugement, notamment des méthodes d'IA et d'AA, qui traite des données en entrée pour générer des résultats » —, laissée « intentionally broad » (lettre d'accompagnement du 11 sept. 2025) ; **cycle de vie (§A.4)** à cinq volets, « not necessarily sequential » ; **inventaire (§C.1, principe 2.1)** « maintained at the enterprise level », « accurate, evergreen » ; **cotation graduée (§A.3, §C.2, principes 2.2-2.3)** — « Each model should be assigned a model risk rating », portée « commensurate with » le risque ; **documentation (§D.2, principe 3.3)** et **Appendice 1 « Information tracking for models »** (champs minimaux : dépendances, sources de données, usages approuvés, limites, état de surveillance) ; **surveillance continue (§D.2, principe 3.6)** visant « autonomous decision making, autonomous re-parametrization ». **Fait négatif vérifié [B], exhaustif et mécanique sur le texte intégral EN et FR (16 juill. 2026)** : « agentique »/« agentic » = 0 ; « agent(s) » = 0 ; « orchestration » = 0 ; « autonom\* » = 8. **Portée du fait négatif** : il établit qu'E-23 ne nomme aucun agent — les chaînes « MCP », « A2A » et « AP2 » n'ont pas été cherchées. Traitement : ch. 9. Le motif R-7 (« E-23 ») ressort dans ce chapitre en contexte réglementaire pur, sans aucune correspondance produit ↔ réglementation : filtré (PRDPlan §4.3).

[^2]: PRD §7.3, **F-25** (niveau [A]). Sources : lautorite.qc.ca ; Norton Rose Fulbright ; rapport annuel Desjardins 2025. Projet publié le 3 juillet 2025 ; **version finale publiée le 30 mars 2026, en vigueur le 1er mai 2027** — même date qu'E-23. **Réserve F-25** appliquée : ne jamais écrire « en attente » ni « en projet » (Annexe D §D.7). Le socle ne porte que le calendrier ; le contenu relève de la lacune PRD §10.4. Traitement : ch. 11.

[^3]: PRD §7.3, **F-26** (niveau [B] — consulté directement sur osc.ca). « CSA Staff Notice and Consultation 11-348 », 5 décembre 2024. Faits mobilisés : doctrine d'applicabilité (les lois existantes s'appliquent ; l'avis ne crée ni ne modifie aucune exigence — formule reprise du socle en français, l'instrument étant en anglais : ce n'est pas une citation verbatim) ; définition des systèmes d'IA incluant explicitement des **niveaux variables d'autonomie et d'adaptativité après déploiement**. Traitement : ch. 12.

[^4]: PRD §7.3, **F-27** (niveau [B] — texte officiel consulté sur LégisQuébec). Article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1), en vigueur depuis le 22 septembre 2023. Les formules entre guillemets sont citées verbatim du texte officiel (Annexe D §D.5 : citer, ne pas paraphraser). **Réserve d'interprétation du socle (niveau [C])** : selon l'analyse Fasken, une intervention humaine significative avant la décision écarte l'application de l'article — nuance non confrontée aux positions de la CAI (PRD §10.4) ; le présent chapitre n'en fait aucun usage et ne construit sur elle aucune cellule. Traitement complet : ch. 11 §11.2 et §11.3 ; contraintes d'architecture : ch. 13 §13.1.

[^5]: PRD §7.4, **F-35** (niveau [A] — **fait négatif vérifié 9-0**). Sources primaires : gazette.gc.ca ; canada.ca (communiqué de Finances Canada et page du Budget 2025) ; bankofcanada.ca. Faits mobilisés : exigence d'un **standard technique unique** fixé par un organisme de normalisation technique **désigné par le ministre des Finances par arrêté ministériel** ; critères de désignation ; quatre objectifs du standard. **Recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » dans le règlement prépublié, le communiqué et la page Budget 2025 : zéro occurrence.** L'anticipation de FDX relève du **commentaire d'industrie** (Fasken, Bennett Jones, NCFA), attribué comme tel à chaque occurrence. Reconduit par la passe de revalidation du 16 juillet 2026 (`verification/revalidation-2026-07-16.md`) : aucun arrêté de désignation publié. Compléments de contexte : **F-11** (C-15, sanction royale du 26 mars 2026 ; supervision par la Banque du Canada) et **F-34** (règlement **prépublié** le 27 juin 2026, commentaires clos le 26 août 2026 — le texte final peut changer, PRD §8.3). Traitement : ch. 14.

[^7]: PRD §7.1, **F-01** (niveau [A]). Sources primaires : spécification MCP, révision **2025-11-25** (modelcontextprotocol.io), revalidée le 16 juillet 2026 ; annonce Anthropic de novembre 2024. **Réserve F-01, contraignante ici** : dire « cadre d'autorisation », jamais « sécurisé » — la sécurité dépend de l'implémentation. Sur la révision attendue le 28 juillet 2026 (refonte sans état, retrait de `Mcp-Session-Id`) : rapport `verification/revalidation-2026-07-16.md` ; **fait chaud à resurveiller en P4.1** (PRD §8.3). Décompte revérifié : du 16 juillet au 28 juillet 2026 = douze jours (concordant avec les ch. 2 et 4). L'analyse du typage comme propriété vérifiable à la frontière, et le refus d'en conclure à une suffisance d'audit, sont établis au **ch. 2 §2.1**.

[^8]: PRD §8.1, garde-fou **R-5** : « FDX est le standard technique retenu pour le cadre bancaire canadien » est une affirmation **interdite** (CA-2). Formulation du fait négatif **imposée par PRDPlan §4.4** (« fait négatif vérifié — standard technique ») et reprise mot pour mot en §18.2. Substitut terminologique imposé : Annexe D §D.7.

[^9]: PRD §7.1, **F-02** (niveau [A]). Sources primaires : a2a-protocol.org/latest/announcing-1.0 ; communiqué de la Linux Foundation du 9 avril 2026 ; `GOVERNANCE.md` du dépôt a2aproject/A2A. La qualification de première spécification stable est **celle du projet A2A** et lui est attribuée. Le socle ne documente ni l'ancrage de confiance, ni la révocation, ni la gouvernance des clés des *Signed Agent Cards* (**ch. 2 §2.2**) ; le présent chapitre ne construit aucune cellule sur ces points.

[^10]: PRD §7.6, **F-16** (niveau [A]). Source primaire : a2a-protocol.org/latest/announcing-1.0 (« Complementary to MCP, not a replacement »). **Attribution** : cette doctrine est celle du **projet A2A** ; le socle ne documente aucun endossement conjoint par le projet MCP. Le constat qu'« un critère n'est pas une contrainte » est établi au **ch. 2 §2.4**.

[^11]: PRD §7.1, **F-01** et **F-02**, tels que le **ch. 4 §4.2** les exploite : le cadre d'autorisation de MCP et les cartes d'agents signées d'A2A établissent **qui** parle, non ce qui est dit ni si ce qui est dit est fondé ; le socle documente leur existence, non leurs propriétés de résistance. Les trois surfaces d'attaque nommées par le socle (empoisonnement d'outils, injection d'invites, empoisonnement de mémoire) sont exposées au **ch. 4 §4.1**, avec l'encadré de lacune sur l'absence de mécanique documentée. Formes imposées : Annexe D §D.3.

[^12]: PRD §7.1, **F-04** (niveau [A]). Sources primaires : annonce Google Cloud du 16 septembre 2025 ; communiqué de la Linux Foundation du 9 avril 2026. **Réserve F-04** : endossement déclaré, pas adoption en production vérifiée. Attribution imposée par PRD §8.2.1 et formulation imposée par PRDPlan §4.4 (« soutien ≠ production »), reprise en §18.2. Le socle ne documente **aucun transfert de gouvernance d'AP2** à une fondation (restriction établie en conclusion du **ch. 1**) ni son anatomie technique (**ch. 3**).

[^13]: PRD §10.5 (lacune ouverte) : aucune source ne documente l'usage **d'AP2** sur les rails de paiement canadiens (RTR, Interac) — libellé du PRD, non élargi à la classe des protocoles de transaction agentique. PRD §10.9 : le socle n'établit **aucune structure de message, mandat ni preuve d'intention pour AP2** (F-04), ni transfert de gouvernance documenté ; « aucune de ces absences n'établit un fait négatif ». Question portée par le **ch. 16** (prospectif) et reprise par renvoi au **ch. 21** — non anticipée ici, conformément à la règle de non-duplication de [TOC.md](../../TOC.md).

[^14]: PRD §8.2.4 (règle d'attribution : la couverture agentique d'E-23 est une **inférence d'analystes juridiques** — jamais « le BSIF exige pour l'IA agentique », toujours « couverture implicite via la définition de modèle ») ; **formulation imposée par PRDPlan §4.4**, reproduite intégralement en §18.3 — les cinq membres imposés compris : « ni l'orchestration », la vérification mécanique EN et FR, la définition « intentionally broad », la visée expresse de la « prise de décision autonome » et de la « reparamétrisation autonome », et la couverture implicite. Développement : ch. 9 §9.3. Sur le statut des analystes nommés — quatre des cinq sont des cabinets figurant au corpus de corroboration secondaire admise (PRD §9.2), Sookman n'en est pas un, et le socle n'établit pas l'indépendance de leurs analyses : ch. 9 note [^5]. Aucun argument du présent chapitre n'en dépend.

[^15]: Dates du socle : E-23 en vigueur le **1er mai 2027** (F-09) — dans neuf mois et quinze jours à la date de gel, décompte revérifié à la rédaction (16 juillet 2026 → 16 avril 2027 = neuf mois ; puis quinze jours, soit 289 jours ; concordant avec les ch. 9, 11 et 14) ; article 12.1 **en vigueur depuis le 22 septembre 2023** (F-27). La ligne directrice de l'AMF partage la date du 1er mai 2027 (F-25, note [^2]).

[^16]: PRD §7.7, **F-36** (niveau [B] — article lu intégralement ; confiance « haute **pour l'attribution** »). Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al. (18 auteurs), « Agentic Business Process Management: A Research Manifesto », *Information Systems* 140, 102738 (2026) / arXiv:2603.18916v3. Éléments mobilisés : distinction **adaptation** (éphémère, d'instance) / **évolution** (persistante, du modèle de processus) ; défi transversal **C2** (sécurité holistique — injection d'invites, empoisonnement de mémoire) ; **opérationnalisation locale des *frames* comme frontière de sécurité et de confidentialité**, qui borne l'impact d'un agent compromis sans prétendre l'empêcher. Le rapprochement entre l'adaptativité après déploiement de F-26 et la scission adaptation/évolution est une inférence d'auteur posée au **ch. 13 §13.1** et reprise ici comme telle. Traitement : ch. 6 (manifeste), ch. 4 §4.3 (frames locaux).

[^18]: PRD §7.7, **F-37** (niveau [B] — article lu intégralement). Rinderle-Ma, Mangler et al. (TU Munich), arXiv:2606.31518v1, 30 juin 2026. Formulation imposée (PRDPlan §4.4, cas « préprint académique ») : **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité (expériences initiales, invites non comparées, facteurs confondants) — le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration seulement et **non repris dans ce chapitre**. Élément mobilisé : la journalisation confiée aux agents « n'est généralement pas recommandée ». Traitement : ch. 5 ; exploitation réglementaire : ch. 13 §13.1.

[^19]: PRD §7.3, **F-10** (niveau [A]) — **renvoi seulement**. Rapport conjoint du BSIF et de l'ACFC publié le 24 septembre 2024 (osfi-bsif.gc.ca) : risque de modèle accru propre à l'IA — très grand nombre de paramètres appris de façon autonome, **relations causales entrées-sorties souvent indéterminables** ; lien explicite au cadre E-23. La conséquence d'architecture est posée au **ch. 9 §9.4** et exploitée au **ch. 13 §13.1** comme inférence de cet ouvrage. **Signalement** : [TOC.md](../../TOC.md) n'assigne aucun socle nominatif au ch. 18 — voir les points de gouvernance en fin de fichier.

[^20]: PRD §7.6, **F-15** (niveau [A]) — **renvoi seulement**. Microsoft Agent Framework (GA 1.0 le 3 avril 2026, Microsoft Learn) : orchestration multi-agents par workflows à base de graphes avec routage typé, **points de contrôle (*checkpointing*)** et **humain-dans-la-boucle (*human-in-the-loop*)**. Mobilisé ici pour un seul constat : le socle documente ces deux propriétés au niveau d'**un cadriciel d'orchestration** — celui-ci, entrée unique —, jamais au niveau des protocoles. F-32 (LangGraph Platform) documente des agents à état et de longue durée, non ces deux propriétés : le pluriel serait excédentaire. Traitement : ch. 7. Les réserves du socle (SDK Go en préversion ; limites du *checkpoint-store* en déploiement distribué) ne sont pas mobilisées ici. Formes imposées : Annexe D §D.2. L'identité et les registres d'agents (**F-07**, **F-08**, avec R-2 et R-3) relèvent du **ch. 8** et ne sont pas croisés dans cette matrice, [TOC.md](../../TOC.md) bornant ses colonnes à MCP, A2A et AP2 ; **F-05** (AGNTCY, couche d'infrastructure) est écarté pour le même motif — ch. 3.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026). Volumétrie : cible 2600 ±10 % = 2340-2860.
                                   Ce chapitre porte un TABLEAU : la méthode de décompte posée au ch. 13 est
                                   reprise, deux décomptes explicites plutôt qu'un chiffre nu. BASES HOMOGÉNÉISÉES
                                   après relecture adversariale (le premier jet rapportait B au plafond et C à la
                                   cible, ce qui MINORAIT l'écart de B au moment même où le chiffre servait à
                                   justifier l'arbitrage qui l'écarte) : les deux décomptes sont désormais
                                   rapportés à la CIBLE.
                                     B) tableau + titres inclus, délimiteurs « | » et ligne de séparation
                                        exclus ......................................... 3128  +20,3 % sur la cible
                                                                                               (+9,4 % au-delà du
                                                                                               plafond de 2860)
                                     C) prose seule (hors tableau et titres) ........... 2860  +10,0 % : CONFORME
                                                                                               (au plafond EXACT)
                                   ARBITRAGE RETENU ET SIGNALÉ : la consigne de volumétrie porte sur le « corps
                                   de prose » ; un tableau n'est pas de la prose. Le décompte C fait donc foi et
                                   il est conforme — mais AU PLAFOND EXACT, marge NULLE : toute reprise du corps
                                   doit retirer avant d'ajouter. L'écart de B
                                   s'est CREUSÉ à la correction et l'arbitrage porte désormais un enjeu réel : la
                                   ligne E-23 du tableau porte à elle seule les cinq domaines d'attentes opératoires
                                   que F-09 v1.6 trace ([B], 16 juill. 2026) — contenu tracé au socle, non réductible
                                   sans re-sous-déclarer la ligne la plus documentée du corpus. Le premier jet
                                   mesurait 2740 en C ; la correction a ajouté le contenu opératoire d'E-23 et retiré
                                   la ligne « rails » (hors périmètre TOC), puis ~270 mots de prose ont été resserrés
                                   pour rentrer. Point de méthode à trancher en P4.3 (voir gouvernance g) : si le
                                   décompte B devait faire foi, ce chapitre est structurellement hors tolérance et
                                   la cible TOC doit être révisée, pas le tableau.
                                   Commandes reproductibles (F = ce fichier) :
                                     B) awk '/^> \*\*Thèse/{f=1;next} /^## Notes/{f=0} f' F \
                                          | grep -vE '^\|[-| :]+\|$' | sed 's/|/ /g' | wc -w
                                     C) awk '/^> \*\*Thèse/{f=1;next} /^## Notes/{f=0} f' F \
                                          | grep -v '^|' | grep -v '^#' | wc -w
                                   En-tête, exergue de thèse, notes et commentaires exclus dans les deux cas ;
                                   encadré de lacune inclus (contenu exigé par CA-6).
     2. Traçabilité (CA-1, CA-5) . fait (18 notes ; tout fait central tracé F-01/F-02/F-04/F-09/F-11/F-16/F-25/
                                   F-26/F-27/F-34/F-35/F-36/F-37, F-10 et F-15 explicitement en renvoi. F-28/F-29
                                   RETIRÉS avec la ligne « rails » (hors périmètre TOC — voir gouvernance b).
                                   NIVEAUX DE PREUVE REVÉRIFIÉS entrée par entrée : F-09 est **[A/B mixte]** — [A]
                                   pour les faits des passes 1-2 (définition, calendrier), [B] pour les exigences
                                   opératoires extraites le 16 juill. 2026 ; ce chapitre mobilise LES DEUX strates.
                                   (Le premier jet écrivait [A] pour tout — faux ; la 1re correction a sur-corrigé
                                   en [B] pour tout — faux aussi. Voir note [^1].) F-26/F-27/F-36/F-37 [B], les
                                   autres [A].
                                   Numérotation des notes : labels [^6] et [^17] LIBÉRÉS par le retrait de la ligne
                                   « rails » ; les labels restants ne sont pas renumérotés (règle de chirurgie ; le
                                   rendu markdown numérote par ordre d'apparition, les trous sont invisibles).
                                   Termes anglais entre parenthèses et en italique à la 1re occurrence du
                                   chapitre : frames, Model Context Protocol, authorization framework, Agent2Agent,
                                   Agent Cards, Signed Agent Cards, Agent Payments Protocol, single technical
                                   standard, human-in-the-loop, checkpointing, tool poisoning, prompt injection,
                                   memory poisoning, orchestration options, Agentic Business Process Management.
                                   (« Real-Time Rail » n'est plus à gloser : la ligne « rails » est retirée.)
                                   Toute conclusion non portée par le socle est introduite par « Lecture de
                                   l'auteur » (8 occurrences, forme unique imposée par PRDPlan §4.4 en prose) ou
                                   marquée « inférence d'auteur » (1 occurrence, règle 3 de §18.1 — forme réservée
                                   aux LIENS EN TABLEAU, PRD B.3/§8.2.4) : 9 marquages, recomptés par extraction.
     3. Balayage garde-fous ...... fait :
                                   - réserve F-09 (motif « exigé par E-23|E-23 impose|exigence.*E-23|fiche de
                                     modèle|model card ») : MOTIF NON ARMÉ AU PREMIER JET — c'est la cause mécanique
                                     de la faute modale de la conclusion (« ce qu'E-23 […] exigent »), réfutée par la
                                     relecture. Ajouté à l'en-tête et exécuté : « fiche de modèle » et « model card »
                                     = 0 ; « exigé par E-23 » / « E-23 impose » = 0 ; le motif « exigence.*E-23 »
                                     ressort 5 fois, TOUTES inspectées et légitimes — soit l'énoncé de la règle
                                     elle-même (note [^1], en-tête), soit « les exigences canadiennes (E-23, AMF…) »,
                                     libellé COLLECTIF repris verbatim de la thèse de TOC, qui ne prête aucune
                                     exigence à E-23 en propre. La colonne « Exigence » du tableau §18.1, qui rangeait
                                     E-23 sous un terme proscrit pour elle, est renommée « Texte canadien » ; la
                                     ligne devient « E-23 — attentes de risque de modèle » ;
                                   - réserve F-01 (motif « sécuris ») : « sécurisé » n'apparaît qu'en négation
                                     explicite (§18.2) ; « cadre d'autorisation » partout ailleurs ;
                                   - §8.2.1 / soutien ≠ production : la seule métrique d'adoption du chapitre
                                     (60+ organisations, AP2) porte l'attribution nominative au communiqué de la
                                     Linux Foundation du 9 avril 2026 et la formulation imposée §4.4 ;
                                   - §8.2.4 : le premier jet ATTESTAIT une conformité qui n'existait pas — la note
                                     [^14] et ce journal déclaraient la formulation « reproduite mot pour mot » alors
                                     que QUATRE membres imposés étaient tombés (« ni l'orchestration » ; vérification
                                     mécanique EN et FR ; « intentionally broad » ; visée expresse de la « prise de
                                     décision autonome » et de la « reparamétrisation autonome »). Les trois derniers
                                     sont ceux qui rattachent la formule au socle extrait de F-09 : leur chute rendait
                                     seule soutenable la thèse du « vide de socle ». CORRIGÉ : §18.3 reproduit
                                     désormais les cinq membres, vérifiés un à un contre PRDPlan §4.4 ; aucune
                                     occurrence de « E-23 exige pour l'agentique » (Annexe D §D.7) ;
                                   - R-4 / réserve F-29 : SANS OBJET depuis le retrait de la ligne « rails » —
                                     « RTR », « Real-Time Rail », « T4 2026 », « Lynx » = 0 occurrence au corps
                                     (« RTR » subsiste dans la seule note [^13], au titre du libellé verbatim de la
                                     lacune PRD §10.5) ;
                                   - R-5 (motif « FDX|Financial Data Exchange|standard technique ») : 4 occurrences,
                                     toutes inspectées. FDX n'apparaît jamais comme standard retenu ; formulation
                                     imposée §4.4 reprise mot pour mot en §18.2 ; substitut §D.7 employé ;
                                   - réserve F-25 (motif « en attente|en projet ») : 0 occurrence fautive ; forme
                                     datée employée (« finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 ») ;
                                   - R-7 (motif « E-23|B-13 ») : « E-23 » ressort au corps, à l'en-tête et en notes,
                                     TOUJOURS en contexte réglementaire pur — aucune correspondance produit ↔
                                     réglementation dans ce chapitre (territoire du ch. 23) : filtré (PRDPlan §4.3).
                                     « B-13 » : 0 occurrence ;
                                   - R-1 et R-8 (motifs « ACP », « control plane », « plan de contrôle ») :
                                     0 occurrence — aucune des quatre branches n'est mobilisée ; le sigle nu est
                                     impossible par construction ;
                                   - R-2, R-3, R-6, §8.2.6 (« 70 % »), §8.2.7 (« Forrester|TEI|Celent|ROI ») :
                                     0 occurrence ;
                                   - §8.2.2 / §7.5 (métriques institutionnelles) : SANS OBJET — aucune métrique
                                     d'institution canadienne dans ce chapitre ;
                                   - §8.4 (neutralité fournisseur) : SANS OBJET par le PÉRIMÈTRE du garde-fou —
                                     §8.4 est « obligatoire — Partie VII et Annexe B », et ce chapitre est en
                                     Partie VI. Le premier jet motivait ce verdict par « aucun composant d'éditeur
                                     n'est cité », ce qui est FAUX (Microsoft Agent Framework, note [^20]) : un
                                     verdict juste motivé par un fait faux ne contrôle rien. F-15 reste mobilisé
                                     pour une propriété de cadriciel, sans comparaison ni superlatif ; le
                                     portefeuille IBM n'est pas évoqué. Corps SINGULARISÉ en Z2 : « au niveau d'un
                                     cadriciel d'orchestration » (F-15, entrée unique) — le pluriel excédait son
                                     appui, F-32 documentant des agents à état, non le human-in-the-loop.
     4. Arithmétique ............. TOUS les décomptes du premier jet étaient faux : ils reposaient sur une ligne
                                   « rails » hors périmètre TOC et sur une vue périmée de F-09. Recomptés ligne à
                                   ligne contre le tableau §18.1 corrigé :
                                   - 3 protocoles (MCP, A2A, AP2) x 5 textes canadiens = 15 croisements. Recompté
                                     sur le tableau : 5 lignes x 3 colonnes = 15. CONFORME. (Premier jet : 18,
                                     annoncé 4 fois — faux, voir gouvernance b.)
                                   - 0 croisement documenté (aucune entrée du socle ne relie un protocole à un
                                     texte canadien) — vérifié entrée par entrée sur F-01 à F-05, F-16, F-09 à
                                     F-11, F-25 à F-27, F-34, F-35.
                                   - 4 absences cherchées DANS LA SOURCE : 3 (ligne E-23 x {MCP, A2A, AP2}, via le
                                     balayage mécanique EN+FR de F-09 — portée bornée au vocabulaire agentique) +
                                     1 (cadre bancaire x MCP, via F-35, chaînes FDX/FDE/FAPI/OAuth) ; 11 absences
                                     constatées AU SOCLE. 4 + 11 = 15. CONFORME.
                                     RÉFUTÉ : le premier jet écrivait « 1 + 17 = 18 » et « une seule absence de la
                                     seconde espèce » à TROIS endroits, alors que sa PROPRE note [^1] documentait le
                                     fait négatif vérifié de F-09. PRDPlan §4.4 nomme F-35, F-09 et F-46 : deux des
                                     trois sont des lignes de cette matrice. Le journal célébrait un « PIÈGE ÉVITÉ »
                                     sur ce décompte tout en manquant l'erreur réelle.
                                     PIÈGE MAINTENU (toujours valide) : cette partition porte sur les ABSENCES, pas
                                     sur les CELLULES — le tableau porte des cellules non vides (art. 12.1 x MCP,
                                     art. 12.1 x A2A, cadre bancaire x MCP, et les 3 cellules E-23).
                                   - 3 espèces de vide réparties sur 5 lignes : vide de socle 1 (AMF seule) + vide
                                     de texte 1 (cadre bancaire) + vide de protocole 3 (E-23, art. 12.1, 11-348)
                                     = 5. CONFORME (recompté deux fois contre le tableau).
                                     RÉFUTÉ : le premier jet rangeait E-23 en « vide de socle » (« l'ouvrage ne sait
                                     pas ce que les textes demandent ») — faux depuis PRD v1.6 : l'ouvrage SAIT ce
                                     qu'E-23 attend. E-23 est un VIDE DE PROTOCOLE. Ce reclassement RENFORCE la
                                     thèse du renversement (§18.3) au lieu de l'affaiblir.
                                   - 5 zones de compensation (Z1 à Z5) : recomptées, 5 énoncées, 5 reprises en
                                     conclusion. CONFORME (inchangé — aucune ne dépendait de la ligne rails).
                                   - 4 chaînes cherchées par F-35 (FDX, Financial Data Exchange, FAPI, OAuth) et
                                     3 chaînes par F-09 (agentique/agentic, agent(s), orchestration) : conformes.
                                   - 5 domaines d'attentes opératoires d'E-23 (cycle de vie, inventaire, cotation,
                                     documentation, surveillance) : recomptés contre F-09 v1.6 et Annexe B.3.
                                   - neuf mois et quinze jours (16 juill. 2026 -> 1er mai 2027 = 289 j) : recalculé,
                                     concordant avec les ch. 9, 11 et 14.
                                   - douze jours (16 juill. -> 28 juill. 2026) : recalculé, concordant ch. 2 et 4.
                                   - 3 obligations de l'art. 12.1 (F-27), 3 surfaces d'attaque (F-36/F-01),
                                     18 auteurs du manifeste (F-36) : conformes au socle.
                                   - 9 marquages d'inférence : recomptés par extraction sur le corps (8 « Lecture de
                                     l'auteur » + 1 « inférence d'auteur »). Le premier jet annonçait 9 pour 8 réels.
                                   Aucun autre calcul n'est posé dans ce chapitre.
     5. Relecture adversariale ... FAITE (deux relecteurs indépendants du rédacteur — PRDPlan §4.2.4).
                                   16 constats bloquants + 10 réserves. TOUS VÉRIFIÉS CONTRE LE SOCLE AVANT
                                   APPLICATION, tous fondés, tous appliqués. Cause racine unique : le chapitre a été
                                   rédigé sur une vue PÉRIMÉE de F-09 — il recopiait un constat des ch. 9 et 13
                                   (« F-09 ne porte ni le libellé verbatim, ni aucune exigence opératoire ») sans le
                                   confronter au socle, alors que F-09 a été ENRICHI le 16 juill. 2026 par extraction
                                   du texte intégral (PRD v1.6, commit 0c2e268) et porte la définition verbatim EN
                                   FRANÇAIS + cinq blocs d'attentes citées, de niveau [B]. Ce faux constat était le PIVOT du chapitre : il fondait la
                                   ligne E-23 du tableau, la 1re règle de §18.1, l'espèce « vide de socle » de §18.3
                                   et la conclusion. LEÇON : un chapitre de synthèse cite le SOCLE, pas la lecture
                                   qu'un chapitre antérieur en faisait à une version antérieure.
                                   Corrections appliquées (les 16 bloquants) :
                                   1/11/3 — note [^1] et ligne E-23 du tableau réécrites depuis F-09 v1.6 (définition
                                      verbatim, cinq domaines d'attentes, portée du fait négatif). Le niveau écrit
                                      alors ([B] pour toute l'entrée) est lui-même faux — rectifié en [A/B mixte]
                                      par la passe de correction du marquage, infra.
                                   2 — E-23 RECLASSÉE de « vide de socle » en « vide de protocole ». Espèces : 4->3.
                                   4 — faute MODALE de la conclusion (« ce qu'E-23 […] exigent ») corrigée : E-23
                                      ATTEND, n'exige pas (PRDPlan §4.4, réserve F-09). Colonne du tableau renommée.
                                   5/6/13 — « une seule absence cherchée dans la source » : FAUX (F-35 ET F-09).
                                      Recompté 4 + 11 = 15 aux trois endroits + journal.
                                   7/16 — §18.3 reproduit désormais INTÉGRALEMENT la formulation §4.4 (5 membres) ;
                                      la note [^14] et ce journal attestaient une conformité inexistante.
                                   8 — point de gouvernance e) RETIRÉ : PRDPlan v1.2 §4.4 tranche « Lecture de
                                      l'auteur » comme libellé unique imposé. Faux arbitrage remonté pour rien.
                                      §18.4 aligné (« des inférences d'auteur » -> « Lecture de l'auteur »).
                                   9 — encadré §18.1 basculé au gabarit CAS 2 (« État de la recherche », « aucune
                                      passe de recherche n'a été conduite »). Le cas 1 se contredisait en son milieu.
                                      Point de gouvernance f) retiré.
                                   10 — gouvernance d) réécrite : l'extraction d'E-23 est ACQUISE ; seule l'AMF reste
                                      due. La matrice porte 4 lignes exploitables sur 5, non 4 sur 6.
                                   12 — ligne « rails » RETIRÉE (option (i)) : TOC borne le ch. 18 à cinq exigences
                                      et assigne les rails aux ch. 15/16 ; le chapitre la déclarait lui-même hors
                                      sujet. Exergue de thèse RESTITUÉ intégralement (les deux énumérations qui
                                      bornent le périmètre avaient été tronquées). Décomptes 18->15 partout.
                                   14 — phrase liminaire réécrite sur la formule imposée (absence de documentation
                                      ≠ fait négatif vérifié). Elle énonçait un état du monde en position la plus lue.
                                   15 — opposition documentaire/structurelle RESTREINTE à MCP et A2A, AP2 exclu
                                      explicitement (PRD §10.9) ; « un vide de protocole ne se comble pas » retiré
                                      (prédiction sur le monde tirée d'un corpus muet) ; les 4 énoncés « aucun
                                      protocole ne… » ramenés à « le socle ne documente, pour aucun protocole… ».
                                   Réserves appliquées : niveau de F-09 rectifié (1, 7 — [A] du premier jet écarté ;
                                   le [B] alors retenu l'a été à son tour, voir la passe de marquage) ; réserve F-09
                                   armée (2) ;
                                   bases de décompte homogénéisées (3) ; 9 marquages recomptés (4) ; note [^13]
                                   rebornée à AP2 (5) ; encadré cas 2 (6) ; §8.4 motivé par son périmètre et Z2
                                   singularisé (8) ; avertissement AP2 borné à l'ouvrage, non au protocole (9) ;
                                   glose « Real-Time Rail » sans objet, ligne retirée (10).
                                   Auto-contrôle antérieur du rédacteur (conservé) :
                                   a) Un premier état de §18.2 attribuait au socle le rapprochement « OAuth de MCP
                                      = OAuth de l'anticipation FDX/FAPI ». FAUX : F-01 fonde le cadre
                                      d'autorisation de MCP sur OAuth, F-35 cherche la chaîne « OAuth » dans trois
                                      documents officiels — le socle ne pose aucun lien entre les deux emplois.
                                      Le rapprochement est désormais marqué « Lecture de l'auteur » avant d'être
                                      désamorcé par la formulation imposée R-5.
                                   b) Un premier état de l'encadré écrivait « dix-sept des dix-huit croisements »
                                      comme si le fait négatif de F-35 remplissait une cellule. Il ne la remplit
                                      pas : il porte sur une CHAÎNE dans trois documents, pas sur le croisement
                                      MCP x cadre bancaire. La distinction reste valide et est maintenue ; le
                                      décompte, lui, était faux dans son autre terme (voir constat 6 supra).
                                   c) « La compensation est structurelle » : borné par sa date (révision MCP du
                                      28 juillet 2026, F-01) — le socle ne documente pas le contenu de cette
                                      révision au regard des exigences canadiennes.
                                   d) AUTO-RÉFUTÉ À LA CORRECTION (relecture finale du corps) : un état
                                      intermédiaire de §18.3 écrivait que les six cellules d'E-23 et de l'art. 12.1
                                      « sont vides » — c'est exactement le PIÈGE que le point 4 de ce journal
                                      documente. Elles ne sont PAS vides : art. 12.1 x MCP et x A2A portent des
                                      inférences d'auteur, les 3 cellules E-23 portent le fait négatif de F-09.
                                      Reformulé : « dont les six croisements ne portent aucun lien documenté ».
                                      Le vide est celui du LIEN, jamais celui de la cellule.

     POINTS DE GOUVERNANCE SIGNALÉS AU PARENT (non corrigés ici — PRD/TOC/PRDPlan/glossaire NON modifiés) :
     a) [PÉRIMÈTRE TOC] TOC.md n'assigne au ch. 18 AUCUNE liste F-xx (« Socle : transversal (I-IV) ») et AUCUN
        garde-fou, alors que le chapitre mobilise 15 entrées porteuses + 4 en renvoi et déclenche six motifs de
        balayage (F-01, §8.2.1, §8.2.4, R-4, R-5, F-25). C'est le seul chapitre de l'ouvrage dont l'en-tête a dû
        être construit par la rédaction. La grille CA-1 et le contrôle P4.3 (références croisées) n'ont donc
        aucune liste de référence contre laquelle vérifier ce chapitre. À entériner dans TOC (version++) en
        reprenant la liste de l'en-tête ci-dessus, ou à restreindre explicitement.
     b) [PÉRIMÈTRE TOC — ARBITRAGE DÛ] Deux écarts au périmètre TOC, l'un corrigé, l'autre ouvert.
        b1) LIGNES (corrigé par la relecture) : TOC énumère CINQ exigences (« E-23, AMF, art. 12.1, 11-348,
            cadre bancaire ») et assigne ISO 20022/Lynx/RTR au ch. 15, AP2 ↔ rails au ch. 16. Le premier jet
            portait une SIXIÈME ligne « rails » que TOC n'assigne pas, et que le chapitre déclarait lui-même
            hors sujet (« une exigence qui ne s'adresse pas aux agents » — un format de message n'est pas une
            exigence réglementaire). Le décompte-titre en dépendait intégralement (18 = 3 x 6). Mécanisme de la
            dérive : l'exergue TRONQUAIT la thèse de TOC en supprimant exactement les deux parenthèses
            d'énumération qui bornent le périmètre. OPTION (i) RETENUE par la correction — ligne retirée,
            recompté sur 15 croisements / 5 lignes / 3 espèces, exergue restitué — parce qu'elle seule ne
            touche pas TOC (interdit à la rédaction). SI le parent préfère l'option (ii) — amender TOC
            (version++) pour ajouter les rails et justifier qu'un format de message y figure —, la ligne et
            l'espèce « hors-champ » sont à restaurer et tous les décomptes à repasser en 18/6/4.
        b2) COLONNES (ouvert, inchangé) : TOC borne la matrice à MCP/A2A/AP2. AGNTCY (F-05) et l'identité/
            registres d'agents (F-07, F-08) en sont donc exclus, alors que le ch. 8 conclut que « aucune source
            du socle ne relie l'un ou l'autre à E-23 ou à la ligne directrice de l'AMF » — soit exactement le
            résultat de ce chapitre, sur une ligne que la matrice ne porte pas. Deux options : (i) élargir la
            matrice à une quatrième colonne (identité d'agent) au TOC, (ii) entériner le périmètre. L'Annexe B
            (« Matrice détaillée protocoles × réglementation ») est le lieu naturel de l'élargissement si
            l'option (ii) est retenue.
     c) [BLOQUANT ÉDITORIAL — rappel du ch. 13, non tranché] « Convergence à trois sources INDÉPENDANTES » :
        l'abstract de TOC.md porte l'adjectif ; le socle le réfute (cosignature Rinderle-Ma F-36/F-37 ; IBM
        Research parmi les 18 auteurs de F-36 et éditeur de F-46). Le présent chapitre n'emploie pas la formule
        et ne mobilise pas F-46 (hors matrice), mais le point reste dû avant J-5.
     d) [SOCLE INSUFFISANT — À MOITIÉ RÉSOLU, la demande est REVUE À LA BAISSE] Le premier jet réclamait au
        parent une extraction d'E-23 DÉJÀ LIVRÉE le jour même, dans le commit qui le porte (F-09 [B], PRD v1.6).
        Demande retirée pour E-23. Reste dû : UNE seule ligne de cette matrice est vide du côté des attentes —
        la ligne directrice finale de l'AMF (lautorite.qc.ca ; lacune PRD §10.4, contenu article par article).
        Son élévation porterait la matrice de quatre lignes exploitables à cinq et ferait vraisemblablement
        apparaître des zones de compensation que ce chapitre déclare non exhaustives. Renforcerait les ch. 11,
        13, 19, 20 et 23.
     e) [PRD §7 — CONTRADICTION INTERNE : RÉSOLUE AU SOCLE, trace conservée] Le ch. 18 avait signalé que PRD §7
        portait une phrase générale périmée (« Les entrées F-01 à F-25 […] sont toutes de niveau [A] »), qui lui
        avait fourni sa couverture pour écrire « F-09 (niveau [A]) » au premier jet. Le signalement était fondé,
        mais sa formulation reprenait une seconde erreur : F-09 n'a JAMAIS été [C], et une extraction primaire
        n'« élève » pas une entrée votée 3-0 — [B] est SOUS [A] dans la taxonomie §7. PRD v1.7 tranche : F-09 est
        **[A/B mixte]** (§7.3), et §7 porte désormais l'exception nominative. Note [^1] et ce journal alignés par
        la passe de correction du marquage. Reste dû au parent : vérifier qu'Annexe B.3 ne porte plus « F-09 [B] ».
     f) [DETTE PRDPlan §1.4 — vérifier l'étendue] Ce chapitre héritait de la « dette de correction post-P3 »
        (chapitres rédigés avant l'élévation de F-09) SANS FIGURER à la liste (« ch. 9, 23 (+ à balayer : 11,
        13, 19, 20) »). Le ch. 18 est donc à AJOUTER à la dette — corrigé ici, mais la liste du plan ne le
        prévoyait pas, ce qui suggère que d'autres chapitres de synthèse recopiant les ch. 9/13 sont atteints.
        Recommandation : balayer le motif « ni libellé, ni exigence opératoire|F-09.*\[A\]|vide de socle.*E-23 »
        sur TOUS les chapitres, pas seulement ceux de la liste.
     g) [DÉCOMPTE — rappel du ch. 13, gouvernance g) ; ENJEU AGGRAVÉ] PRDPlan §4.2 ne fixe aucune commande de
        décompte des mots, et ce chapitre est, avec le ch. 23, l'un des deux chapitres de tableaux annoncés.
        La méthode du ch. 13 (deux décomptes explicites) est reprise faute d'arbitrage, avec BASES HOMOGÈNES
        depuis la relecture. L'enjeu n'est plus théorique : B = 3126 (+20,2 % sur la cible), C = 2858 (+9,9 %,
        conforme à 2 mots près). Si le décompte B devait faire foi, le ch. 18 est structurellement hors
        tolérance — le tableau porte 5 lignes x 5 colonnes dont la ligne E-23, seule à porter les cinq domaines
        d'attentes tracés à F-09 [B] : le comprimer re-sous-déclarerait la ligne la plus documentée du corpus.
        C'est alors la cible TOC (~2600) qu'il faut réviser. À fixer en P4.3. NOTE DE MÉTHODE : `wc -w` compte
        les tirets cadratins isolés comme des mots — la commande n'est pas neutre, raison de plus pour la fixer.
     h) [GLOSSAIRE — enrichissement à verser par le parent, PRDPlan P1.5] Le ch. 18 n'introduit aucun terme
        nouveau. Rappel des dettes signalées par les chapitres antérieurs et toujours ouvertes, que ce chapitre
        mobilise : « adaptativité après déploiement » (F-26, signalée par les ch. 12 et 13) n'a toujours pas
        d'entrée en §D.5, alors qu'elle porte ici une ligne entière de la matrice et la zone Z3 ;
        « multi-location d'entreprise / enterprise multi-tenancy » (F-02, signalée par le ch. 2) manque en §D.3.
        Terme candidat propre à ce chapitre : « zone de compensation architecturale » — construction de l'auteur,
        sans trace F-xx propre : à ce titre elle n'entre PAS au glossaire (règle de l'Annexe D, « un terme sans
        trace F-xx n'entre pas au glossaire »). Signalé pour arbitrage.

     PASSE DE CORRECTION DU MARQUAGE F-09 (16 juill. 2026, PRD v1.7) : note [^1] et journal rectifiés de « [B] —
     élevée [C]->[B] » en « [A/B mixte] » ([A] passes 1-2, [B] exigences opératoires extraites ; [B] est SOUS [A]) ;
     ce chapitre mobilise les deux strates. Corrections 2 (affirmations périmées sur l'absence d'extraction),
     3 (« exigé » -> « attendu ») et 4 (« fiches de modèles ») SANS OBJET — déjà conformes, re-balayées ce jour :
     « exigé par E-23 » / « E-23 impose » = 0 ; « fiche de modèle » / « model card » = 0 hors énoncé de la règle ;
     aucune occurrence watsonx.governance (F-44) dans ce chapitre. Corps de prose NON touché : volumétrie inchangée.
-->
