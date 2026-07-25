# Chapitre 13 — Le pont : des contraintes réglementaires aux frames déterministes

| Champ | Valeur |
|---|---|
| Statut | Rédigé (passe de dérivation du §13.1 conduite le 17 juill. 2026, après arbitrage de gouvernance) |
| Date de gel de l'information | 17 juillet 2026 |
| Socle mobilisé (PRD §7) | F-09 **dans ses deux strates** — **[A]** : dates, portée, définition de « modèle », couverture agentique comme inférence d'analystes ; **[B]** : les cinq attentes opératoires traduites au §13.1, l'anticipation d'autonomie **et la vérification négative** (extraction du 16 juill. 2026). *L'énumération [A] de F-09 est close et ne comprend ni la vérification négative ni l'anticipation : les porter en [A] serait refaire la faute que le ch. 18 a relevée.* ; F-25, F-26, F-27 (exigences canadiennes — ch. 9 à 12) ; F-36, F-37, F-46 (convergence sur l'encadrement) ; **F-10 en renvoi** (indéterminabilité causale, ch. 9) et **F-35 en renvoi de méthode** (forme du fait négatif vérifié, ch. 17) — renvois **entérinés** par [TOC.md](../../TOC.md) v1.4 |
| Garde-fous à surveiller (PRD §8) | §8.2.4 (couverture agentique d'E-23 = inférence d'analystes — formulation imposée) ; **réserve F-09** (« attendu par E-23 », jamais « exigé » ; « documentation de modèle » / « inventaire », jamais « fiche de modèle » — PRDPlan §4.4) ; réserves **F-37** (préprint non révisé par les pairs ; chiffres en illustration seulement) ; confiance **F-36** « haute pour l'attribution » ; **§8.4** (F-46 = position d'IBM, cas documenté et non recommandation) ; réserve **F-25** (jamais « en attente » ni « en projet ») ; motif R-7 (« E-23 ») : ressort en contexte réglementaire pur aux §13.1, §13.3 et §13.4 — filtré (PRDPlan §4.3) ; **au §13.2, contexte fournisseur (F-46) : inspecté** — aucune conformité revendiquée, aucun rapprochement IBM ↔ E-23 posé, absence au socle exposée en encadré ; motifs R-8 (« ACP », « control plane ») : sans objet |
| Volumétrie cible | ~3400 mots |

> **Thèse ([TOC.md](../../TOC.md) v1.4)** : Pivot de l'ouvrage : **la plupart des exigences canadiennes lues** se traduisent en frame d'architecture — neuf des onze entrées de la table du §13.1 —, et la forme de cette table mesure ce que le socle a extrait, non l'exigence propre des textes ; l'encadrement déterministe des processus réglementés est le principe sur lequel convergent trois sources **non indépendantes**, dont le socle n'établit l'application ni au Canada ni à la finance canadienne ; le « responsibility gap » éclaire l'imputabilité — sous l'article 12.1 du moins, elle pèse sur l'assujetti, qui ne peut désigner de tiers.

---

Les quatre chapitres qui précèdent ont établi un état du droit ; aucun n'a dit ce qu'il fallait construire. C'est l'office de celui-ci, et il faut dire d'emblée à quel prix il s'en acquitte. Traduire une exigence juridique en contrainte d'architecture n'est pas une opération de lecture : c'est un raisonnement d'auteur, qui engage sa responsabilité et non celle du régulateur. Le lecteur trouvera donc ici plus d'inférences marquées que partout ailleurs — les chapitres 9 à 12 rapportaient des textes ; celui-ci construit.

Il soutient trois propositions. La première : la plupart des exigences canadiennes examinées se traduisent en cadres (*frames*) d'architecture — neuf des onze entrées de la table du §13.1 —, mais la forme de cette table mesure d'abord ce que le socle a lu, et non ce que les textes exigent. La seconde : trois sources convergent sur l'encadrement déterministe des processus réglementés — une seule, un préprint, portant un verdict d'inacceptabilité de l'orchestration non encadrée, et sur un processus européen hors finance —, mais elles ne sont pas indépendantes et le socle n'établit, pour aucune, d'application au Canada. La troisième : l'écart de responsabilité (*responsibility gap*) nommé au chapitre 6 rencontre dans les textes canadiens une constante que le manifeste ne pouvait pas connaître — constante qui est, on le verra, une lecture de l'auteur et non un énoncé du socle.

## 13.1 La table de traduction : ce que les exigences imposent aux frames

Une précaution de méthode s'impose, faute de quoi la table serait un exercice de plausibilité. Une exigence ne devient une contrainte d'architecture que si trois choses sont connues : ce que le texte impose, à qui, et sur quel objet. Lorsque l'un des trois manque au socle, aucune contrainte n'en est dérivée.

| Texte (source) | Ce que le socle établit | Ce que le cadre doit porter | Statut du lien |
|---|---|---|---|
| **E-23 — périmètre** (F-09, strate [A] ; anticipation en [B])[^1] | Définition de « modèle » englobant les méthodes d'IA et d'apprentissage automatique ; en vigueur le 1er mai 2027, institutions financières fédérales. **En strate [B]**[^15] : l'anticipation par le BSIF de modèles à apprentissage et décision autonomes | **Un périmètre, non un cadre** : cette entrée ouvre la porte que les cinq suivantes franchissent | Périmètre établi ; **couverture implicite via la définition de modèle**, tenue pour acquise par les analystes — inférence d'analystes (§8.2.4)[^10] |
| **E-23 — inventaire** (F-09, strate [B])[^15] | Est attendu « *a comprehensive inventory of models whose inherent risk is determined to be non-negligible* », « *maintained at the enterprise level* », « *accurate, evergreen, and subject to robust controls* » (§C.1, principe 2.1) ; champs minimaux à l'Appendice 1 | L'ensemble de ce qui peut être invoqué doit être **énumérable avant l'exécution**, donc **déclaré par le cadre** | **Inférence d'auteur** : E-23 attend un inventaire exact ; elle ne dit pas ce qui le rend exact |
| **E-23 — cotation de risque** (F-09, strate [B])[^15] | « *Each model should be assigned a model risk rating* » ; portée, échelle et intensité de la gestion du risque de modélisation « *commensurate with* » le risque (§A.3, §C.2, principes 2.2–2.3). Le « *level of autonomy* » est un **facteur qualitatif de cotation** | La cote doit être **connue au point d'invocation** — sans quoi la proportionnalité attendue n'a aucune prise sur le système en exécution | **Inférence d'auteur**, et la plus longue de la table : E-23 attend qu'une cote soit assignée, non qu'elle soit lisible à l'exécution. L'objet coté est le **modèle**, non l'assemblage — limite exposée ci-dessous |
| **E-23 — cycle de vie** (F-09, strate [B])[^15] | Cinq volets — « *model design (including model rationale, data, and development), model review, model deployment, model monitoring, and model decommission* » — « *not necessarily sequential* » (§A.4) | La **mise hors service** (*decommission*) doit s'interposer entre la décision et l'invocation : un point de passage, non une écriture au registre | **Inférence d'auteur** — la plus nette des cinq |
| **E-23 — documentation** (F-09, strate [B])[^15] | Normes de documentation de modèle (§D.2, principe 3.3), dont les **limites et restrictions d'usage** ; Appendice 1 : usages approuvés, limites, dépendances, sources de données | L'**usage approuvé** doit être opposable, donc porté par ce qui autorise l'invocation — et non seulement consigné | **Inférence d'auteur** — écart maximal entre ce que le texte attend (consigner) et ce que l'auteur en tire (refuser) |
| **E-23 — surveillance continue** (F-09, strate [B])[^15] | Fréquence, portée et critères par palier de risque ; suivi de la performance, de l'**usage**, des **données d'entrée** et des **dépendances externes** ; seuils de dépassement ; processus traitant « *autonomous decision making, autonomous re-parametrization* » et la dérive (§D.2, principe 3.6) | Les observations d'usage et de données d'entrée n'existent que si un point de passage les **émet** : le cadre est producteur d'observations avant d'être producteur de décisions | **Inférence d'auteur** — la mieux ancrée textuellement : c'est la seule attente dont le libellé **nomme les opérations autonomes** qu'il faut traiter, là où la cotation ne fait de l'autonomie qu'un facteur d'appréciation |
| **Ligne directrice IA de l'AMF** (F-25)[^2] | Le calendrier seulement : finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 | **Rien de dérivable.** Le contenu du texte n'est pas au socle | Lacune ouverte (PRD §10.4)[^12] — encadré ci-dessous |
| **ACVM 11-348 — définition** (F-26)[^3] | Définition des systèmes d'IA incluant explicitement des niveaux variables d'**autonomie** et d'**adaptativité après déploiement** (instrument en anglais ; le socle n'en porte pas le libellé[^3]) ; doctrine : les lois existantes s'appliquent, l'avis ne crée ni ne modifie aucune exigence | Distinguer l'**adaptation** d'instance de l'**évolution** du modèle de processus (F-36)[^5] et soumettre la seconde à un régime propre | **Inférence d'auteur** : le socle établit les deux textes, non leur rapprochement |
| **Art. 12.1 — informer** (F-27)[^4] | Informer la personne « au plus tard au moment de la décision » — seule des trois obligations à ne pas être subordonnée à une demande | Le **moment de la décision** doit être un événement émis par le cadre, identifiable et daté | **Inférence d'auteur** (préparée au ch. 11 §11.4) |
| **Art. 12.1 — expliquer** (F-27)[^4] | Sur demande : « les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision » — l'instance, non le modèle | Une **trace d'instance** produite par le cadre, non par les agents[^8] | **Inférence d'auteur**, adossée à un enseignement de F-37 |
| **Art. 12.1 — réviser** (F-27)[^4] | « L'occasion de présenter ses observations à un membre du personnel de l'entreprise **en mesure de réviser la décision** » | Un point de reprise, et des effets aval **bornés** — donc défaisables | **Inférence d'auteur** (préparée au ch. 11 §11.4) |

Onze entrées. Une seule ne produit rien du tout : la ligne directrice de l'AMF. Une autre — le périmètre d'E-23 — produit un périmètre et non un cadre : c'est la porte, non ce qui se trouve derrière. Restent **neuf** entrées qui produisent une contrainte : cinq d'E-23, trois de l'article 12.1, une de l'avis 11-348.

Cette table a changé de forme le 17 juillet 2026, et il faut dire pourquoi plutôt que de livrer le résultat comme s'il avait toujours été là. Dans son premier état, elle comptait six entrées dont deux ne produisaient rien, et l'article 12.1 fournissait trois des quatre contraintes restantes. E-23 n'y décidait que d'un périmètre — non par la volonté du régulateur, mais parce que le socle ne portait alors du texte que sa définition de « modèle ». L'extraction du texte intégral, le 16 juillet 2026, y a versé les attentes opératoires en niveau [B][^15] ; le présent chapitre ne les avait pas traduites, et le signalait. La traduction a été conduite depuis. **Le chapitre avait posé, dans son premier état, une lecture de l'auteur que sa propre correction vérifie** : la densité de contraintes dérivables d'un texte ne mesure pas son exigence propre, mais ce que le socle en a extrait. L'article 12.1 dominait la table parce qu'on l'avait lu ; E-23 la domine désormais pour la même raison, et non parce qu'elle serait devenue plus contraignante entre-temps. Le lecteur est fondé à se demander ce que produirait la ligne directrice de l'AMF si on la lisait.

Reste que ces cinq entrées d'E-23 se paient d'un pas dont il faut mesurer la longueur. **Lecture de l'auteur** : E-23 attend ces cinq choses d'un **programme** de gestion du risque de modélisation (*model risk management*) — un dispositif d'organisation, de rôles et de contrôles. Elle n'attend rien d'une architecture, ne nomme ni les agents ni l'orchestration[^1], et ne dit nulle part qu'il faille construire un cadre. Ce que l'auteur ajoute est une observation sur les **conditions de possibilité** : déployées sur un système agentique, ces attentes portent toutes sur des objets qu'un programme ne peut rendre vrais par ses seules procédures. Un inventaire n'est « *evergreen* » que si l'ensemble des modèles invoqués est énumérable ailleurs que dans la trace de ce qui a déjà eu lieu ; une mise hors service n'a d'effet que si quelque chose s'interpose entre la décision et l'invocation ; un usage approuvé n'est opposable que si l'usage non approuvé peut être refusé ; une intensité de gestion « *commensurate with* » le risque ne règle rien à l'exécution si la cote n'y est pas lisible ; une surveillance de l'usage et des données d'entrée n'observe rien si aucun point de passage n'émet ces observations. Là où l'agent résout lui-même ses modèles au moment de l'exécution, ces cinq propriétés cessent d'être des propriétés du registre pour devenir des propriétés de l'exécution — c'est-à-dire des constats *a posteriori*. Le cadre est le seul objet qui les rende vraies par construction.

Le pas est cependant plus long sur deux d'entre elles, et il faut le concéder ligne à ligne plutôt qu'en bloc. Pour l'inventaire, la mise hors service et l'usage approuvé, l'attente porte sur une propriété — exactitude, effectivité, opposabilité — que l'exécution peut contredire : l'écart entre le texte et l'inférence est celui d'un constat. Pour la **cotation**, E-23 n'attend qu'une cote assignée et une intensité proportionnée ; « connue au point d'invocation » ajoute un lieu que le texte ne mentionne pas. Pour la **surveillance**, le texte attend des processus, non un émetteur d'événements. Ces deux lignes sont les plus exposées de la table, et leur marqueur « inférence d'auteur » y travaille plus dur qu'ailleurs. **Aucune de ces phrases n'est dans E-23** : le texte attend, l'auteur infère où l'attente se loge.

Une limite, et elle est structurelle. L'objet d'E-23 est le **modèle** : c'est lui qu'on inventorie, lui qu'on cote, lui qu'on met hors service. Un système agentique compose plusieurs modèles, des outils et un enchaînement, et E-23 ne dit pas ce qu'est « le modèle » d'un tel assemblage — ni s'il faut coter les composants, la composition, ou les deux. Le silence est entier : ni le texte, ni le socle, ni cet ouvrage ne le comblent. C'est la question que les institutions fédérales auront à trancher d'ici le 1er mai 2027, et le présent chapitre ne peut que la désigner.

La **ligne directrice de l'AMF** est le cas le plus net, et désormais le seul vide complet de cette table : finale depuis le 30 mars 2026, en vigueur le 1er mai 2027[^2], son contenu n'est pas au socle — il serait facile, et irresponsable, de reconstruire ce qu'elle « doit » contenir.

> **État de la recherche — le contenu de la ligne directrice sur l'IA de l'AMF**
>
> Question : que prescrit, article par article, la version finale de la ligne directrice sur l'IA de l'AMF (30 mars 2026) ?
>
> Ce que le socle porte : les quatre dates de la trajectoire du texte et rien d'autre — lacune ouverte, inscrite au PRD §10.4[^12]. La lacune jumelle sur E-23 est comblée : le texte intégral a été extrait le 16 juillet 2026 et ses attentes opératoires versées à F-09 en niveau [B][^15] ; le §13.1 en dérive cinq entrées. Rien de tel n'existe pour l'AMF.
>
> **Aucune passe de recherche dédiée n'a été conduite** — l'extraction du texte de l'AMF ne relevait pas du périmètre de P0 (PRDPlan §2). Source à retrouver : `lautorite.qc.ca`. **Un obstacle matériel est de surcroît documenté** : la revalidation finale du 17 juillet 2026 a constaté que le domaine renvoie une erreur 403 aux outils employés, sur quatre URL dont le PDF de la ligne directrice ; le caractère final du texte et son entrée en vigueur n'ont pu être corroborés que par l'index du domaine. L'obstacle est consigné, non contourné : il n'autorise à supposer aucun contenu.
>
> La question reste ouverte ; aucune inférence n'est proposée ici. La conséquence : **du texte qui, avec E-23, fixe au 1er mai 2027 l'échéance structurant toute la Partie III, ce chapitre ne dérive aucune contrainte.** Une institution qui construit aujourd'hui doit le lire à sa source.

Des quatre entrées qui restent, trois proviennent du même texte : l'article 12.1 de la Loi 25, dont le socle porte le libellé, son texte officiel ayant été consulté[^4]. Elles sont d'une autre espèce que les cinq précédentes, et la différence importe plus que leur nombre. E-23 est **fondée sur des principes** et rédigée au conditionnel : elle attend[^15]. L'article 12.1 est une disposition législative rédigée à l'impératif : il oblige[^4]. Les cinq contraintes tirées d'E-23 sont donc des conditions de possibilité d'un programme attendu ; les trois tirées de l'article 12.1 sont des conditions de possibilité d'une obligation. L'inférence est de même nature — c'est toujours l'auteur qui la conduit — mais ce qu'elle sert à défendre ne l'est pas.

La quatrième — celle de l'avis 11-348 — naît de la rencontre de deux textes que rien ne relie. La définition de l'avis capte les systèmes dont le comportement se modifie **après déploiement**[^3] ; le manifeste APM scinde l'auto-modification en deux régimes — l'**adaptation**, éphémère, d'instance, et l'**évolution**, persistante, qui modifie le modèle de processus[^5]. **Lecture de l'auteur** : le rapprochement produit une contrainte que ni l'un ni l'autre n'énonce. Si l'adaptativité après déploiement est ce que la définition capte, un système qui traite l'adaptation et l'évolution par le même chemin technique rend indétectable, dans ses journaux, le moment où une exception est devenue une règle. Le chapitre 6 posait cette proposition sans exigence externe où l'adosser ; l'avis 11-348 lui en fournit une.

Un recoupement mérite d'être relevé ici, et borné aussitôt. La note 1 d'E-23 reprend la définition de l'intelligence artificielle de l'**OCDE** — les systèmes « *vary in their levels of autonomy and adaptiveness after deployment* » —, et le socle établit que c'est là le socle textuel réel de sa couverture implicite[^15]. Or le socle rend la définition de l'avis 11-348 par la même formule : des niveaux variables d'autonomie et d'adaptativité après déploiement[^3]. **Lecture de l'auteur** : deux régulateurs canadiens, l'un fédéral et prudentiel, l'autre provincial et de marché, saisissent ce que les analystes tiennent pour les systèmes agentiques par ce que le socle rend d'une seule et même formule — et E-23, dont le socle établit par balayage qu'elle ne nomme jamais l'agentique, y parvient sans avoir à la nommer. Ce que le socle **n'établit pas**, et qu'il faut donc s'interdire d'écrire : que les deux libellés soient identiques ; que l'avis 11-348 emprunte lui aussi à l'OCDE ; et quoi que ce soit sur ce que l'avis 11-348 **ne dit pas** — aucun balayage n'a porté sur son texte, et cet ouvrage s'interdit l'argument du silence hors des trois entrées qui portent un fait négatif vérifié (F-09, F-35, F-46). Le socle porte la formule d'E-23 verbatim en anglais avec son attribution ; de celle de l'avis, instrument anglais, il ne porte qu'un rendu français dont il n'établit ni le libellé d'origine ni la provenance[^3]. La ressemblance est celle de deux rendus au socle, pas nécessairement celle de deux textes — et l'établir demanderait une consultation primaire de l'avis en anglais (osc.ca), qui n'a pas été conduite. Sous cette réserve, la convergence reste ce qu'elle est : deux voies d'entrée distinctes vers le même objet, dont la seconde nomme explicitement ce que la première laisse à l'inférence des analystes[^10].

L'entrée de l'obligation d'explication procède du même mouvement, et engage le plus l'architecture. L'article 12.1 exige, sur demande, les raisons et les principaux facteurs et paramètres ayant mené à *cette* décision[^4] : l'objet de l'obligation est l'instance. Or l'un des deux enseignements de conception que le préprint de la TU Munich tire de ses expériences est que la journalisation confiée aux agents « n'est généralement pas recommandée »[^8] : le premier énoncé impose une trace d'instance, le second déconseille de la demander à l'agent. **Lecture de l'auteur** : la conjonction désigne le cadre comme lieu de production de la trace — non parce qu'une source le prescrirait, mais parce que les deux autres candidats sont écartés, l'agent par l'enseignement du préprint et le modèle par le rapport conjoint du BSIF et de l'ACFC, dont le socle établit que les relations causales entre entrées et sorties sont souvent indéterminables[^11]. Si l'on ne peut extraire l'explication du modèle *a posteriori*, ni raisonnablement la confier à l'agent, il reste ce qui les entoure. Aucune des trois sources ne dit cela ; c'est leur conjonction, et elle est de l'auteur.

## 13.2 Le verdict empirique et la convergence à trois sources

L'argument qui suit porte le titre de l'ouvrage ; il faut donc l'exposer avec plus de sévérité qu'aucun autre.

Le premier terme est un verdict. Sur un processus de don de sang régi par la directive européenne 2002/98/CE, le cadre de la TU Munich conclut que l'orchestration non encadrée est « inacceptable » lorsque des exigences strictes d'exécution et de documentation s'appliquent, et que les tâches essentielles doivent être imposées de façon déterministe par le cadre[^8]. Il provient de Rinderle-Ma, Mangler et al., **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité — le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration seulement[^7], et le chapitre 5 a refusé d'en faire un argument. **Lecture de l'auteur** : ce qui se transporte, ce n'est pas un F1, c'est un mécanisme — le socle borne le verdict à un processus européen de don de sang, et sa généralisation est de l'auteur : dès lors qu'une exigence porte sur la *manière* dont une tâche est exécutée et documentée, et non sur son seul résultat, un dispositif incapable de garantir l'exécution et de produire la trace échoue à l'exigence, quel que soit son taux de réussite moyen.

Le deuxième terme est conceptuel. Le manifeste de recherche sur l'*Agentic Business Process Management* érige l'autonomie encadrée (*framed autonomy*) en mécanisme premier de gouvernance des systèmes agentiques, et distingue les *frames* normatifs (*normative frames*) — obligations, permissions, interdictions déontiques — des *frames* opérationnels (*operational frames*)[^5]. Le socle lui attribue une confiance haute **pour l'attribution** : ce qui est certain, c'est que ces auteurs soutiennent cette thèse (ch. 6). Un manifeste ne fait pas autorité ; il fournit un vocabulaire. Il recommande, il ne juge pas.

Le troisième terme est celui d'un fournisseur, et son statut se pose avant son contenu. Le pattern d'architecture « Agentic AI » publié par IBM recommande **explicitement les workflows statiques** (*static workflows*) pour les processus sous surveillance réglementaire, au nom de l'auditabilité, de la conformité et de transferts définis[^9]. Deux réserves l'encadrent. Neutralité fournisseur d'abord : les positions d'IBM sont retenues ici comme cas d'instanciation documenté par sources primaires, jamais comme recommandation ni verdict comparatif[^13]. Portée ensuite : le socle établit que ce pattern est générique et qu'IBM ne publie aucune architecture agentique spécifique aux services financiers[^9] ; la recommandation vise « les processus sous surveillance réglementaire » en général, non un processus de crédit canadien. Là encore, IBM recommande — il ne juge pas.

Le socle érige la rencontre de ces trois énoncés en **convergence à trois sources**, et en fait le principe directeur du blueprint[^9]. Il l'a longtemps qualifiée de convergence à trois sources « **indépendantes** » ; l'adjectif en a été **retiré le 16 juillet 2026**, sur signalement des rédactions des chapitres 5 et 13, parce qu'il était réfuté par le socle lui-même[^9]. La rétractation étant acquise, ce qui suit n'est plus une contestation du socle mais l'exposé de ce qui l'a motivée — et il faut le lire ainsi : la démonstration reste due au lecteur, car c'est d'elle que dépend la portée exacte du principe directeur de tout l'ouvrage.

Une convergence tire sa force de l'indépendance de ses termes. Or le socle établit lui-même que ces trois-là ne sont pas indépendants, et il le fait deux fois. **Premièrement**, Rinderle-Ma figure parmi les auteurs du manifeste et parmi ceux du préprint[^5][^7] : les deux sources académiques partagent une autrice. **Deuxièmement**, IBM Research figure parmi les organisations dont proviennent les dix-huit auteurs du manifeste[^5], et IBM publie le pattern[^9] : la source académique et la source industrielle partagent une organisation. Ni l'un ni l'autre recoupement n'est une conjecture — tous deux se lisent dans les entrées du socle.

**Lecture de l'auteur** : trois sources qui se recoupent deux à deux ne valent pas trois sources indépendantes. Ce faisceau n'établit pas que trois observateurs séparés ont abouti au même diagnostic, mais qu'un même milieu — académique et industriel, partiellement chevauchant — l'a formulé dans trois registres : moins qu'une corroboration indépendante, davantage qu'une opinion isolée. La distinction décide de ce qu'une institution peut inscrire dans une note d'architecture : « trois sources indépendantes recommandent l'encadrement déterministe » serait faux ; « le principe est formulé, dans la littérature de la mi-2026, par un manifeste académique, une expérimentation et un pattern de fournisseur, dont deux partagent une autrice et deux une organisation » est exact, et suffit.

> **État de la connaissance vérifiable — le socle n'établit d'application canadienne pour aucune des trois sources**
>
> Question : la convergence sur l'encadrement déterministe est-elle établie pour les services financiers canadiens ?
>
> Ce que le socle établit : un verdict borné à un processus européen[^8], un manifeste qui relie l'explicabilité au RGPD et à l'AI Act européen[^5], un pattern générique[^9]. **Le socle n'établit, pour aucune des trois sources, d'application au Canada, à la finance canadienne, à E-23, à la ligne directrice de l'AMF, à l'avis 11-348 ni à l'article 12.1, et il n'établit aucun lien entre elles et ces textes.**
>
> Ce que le socle n'établit pas : de **fait négatif vérifié**. Aucune recherche exhaustive de ces chaînes dans les trois sources n'a été conduite — à la différence des faits négatifs que le socle établit par balayage documenté (F-35, F-09, F-46[^14]). La distinction est celle-là même que ce chapitre exige d'E-23 au §13.1 : une absence *au socle* n'est pas une absence *dans la source*. Le manifeste compte au contraire une affiliation canadienne — l'Université d'Ottawa[^5] —, dont le socle ne dit pas si elle emporte quelque application au droit canadien.
>
> Recherche menée le 16 juillet 2026 : aucune passe primaire dédiée n'a été conduite pour ce chapitre ; les trois entrées mobilisées l'ont été par lecture intégrale des deux articles et consultation directe de la page d'IBM (PRD Annexe A), et aucune n'a fait remonter d'application canadienne. La question reste ouverte ; aucune inférence n'est proposée ici. La transposition au contexte canadien conduite dans ce chapitre est **entièrement une inférence d'auteur**, et le lecteur est fondé à en exiger l'examen plutôt qu'à en recevoir l'autorité.

## 13.3 L'imputabilité : qui répond du comportement émergent ?

Le chapitre 6 a posé une pièce sur l'échiquier sans la jouer. Le manifeste inscrit parmi ses défis transversaux l'écart de responsabilité (*responsibility gap*, défi C4) : l'indétermination de l'imputabilité juridique entre quatre porteurs candidats — le développeur, l'organisation qui impose le *frame*, le fournisseur du modèle et le comportement émergent du système multi-agents[^6]. Le quatrième n'est pas une personne : il est le nom de ce dont aucun des trois autres n'est l'auteur au sens ordinaire. Confrontons-le aux textes canadiens sur le seul point que le socle autorise : la désignation du porteur.

Le socle porte ici trois choses de nature différente. Pour l'article 12.1, un **fait générateur** : l'obligation pèse sur toute entreprise qui rend une « **décision fondée exclusivement sur un traitement automatisé** » de renseignements personnels[^4] — sans condition tenant à l'auteur du système, ni partage avec le fournisseur du modèle. Pour E-23, un **périmètre d'application** : les institutions financières fédérales[^1]. Pour l'avis 11-348, un périmètre également, et rien de plus : il ne crée aucune obligation — il énonce que les lois existantes s'appliquent, et à qui, soit sept catégories d'assujettis[^3] ; le porteur qu'il désigne l'est par renvoi au droit en vigueur, non par l'avis.

**Lecture de l'auteur** : aucun des trois ne désigne un porteur en des termes que le socle rapproche des deux autres — le rapprochement est de l'auteur, et l'expression « **l'entité qui exploite** » est la sienne : elle ne figure ni dans les textes, ni au socle. Sous cette réserve, trois textes, trois régimes, une constante : le porteur est, dans chacun, celui qui exploite le système, non celui qui l'a construit. Rapportée à l'énumération du manifeste, cette constante désigne le deuxième des quatre candidats — l'organisation qui impose le *frame*. Le socle n'établit ni ce rapprochement, ni son exactitude juridique. Elle ne dit pas que le droit canadien résout l'écart de responsabilité : ce que le manifeste nomme est l'indétermination de l'*allocation* de l'imputabilité entre quatre porteurs, question que ces textes ne traitent pas et que cet ouvrage n'a ni la vocation ni la compétence de trancher (PRD §3). Elle ne dit pas davantage que ces régimes se cumulent sur une même chaîne : le chapitre 11 a laissé ouverte la question de savoir si l'article 12.1 atteint les institutions sous charte fédérale[^12].

Ce qu'il permet de dire est plus modeste et suffit à l'architecture. L'article 12.1 n'offre pas à l'entreprise assujettie la ressource de désigner un tiers : développeur, fournisseur de modèle ou l'émergence elle-même[^4]. **Lecture de l'auteur** : les attentes d'E-23 versées au socle le 16 juillet 2026 ne traitent pas de ce point, et aucune vérification négative n'y porte ; le socle ne porte pas davantage le corps de l'avis 11-348. Cet ouvrage ne peut donc dire ce que ces deux textes prévoient — ou ne prévoient pas — sur ce point ; il se refuse l'argument du silence. Sous l'article 12.1 du moins, l'écart de responsabilité n'est pas un moyen de défense devant le régulateur : il est le problème de l'assujetti. C'est là que la proposition posée au chapitre 6 se joue. Si le *frame* est ce qui borne la décision, celui qui pose le *frame* est le seul acteur dont on puisse dire ce qu'il a effectivement décidé — inférence de cet ouvrage, non du manifeste ; elle reçoit ici sa raison d'être. L'entreprise assujettie répond d'un comportement qu'elle n'a pas spécifié et qu'elle ne peut pas reconstituer depuis le modèle. Le seul objet dont elle puisse démontrer la teneur — parce qu'elle l'a écrit, qu'il précède l'exécution et ne dépend pas de la coopération d'un agent — est le cadre qu'elle a posé. **L'encadrement n'est pas, dans cette lecture, une bonne pratique d'ingénierie : c'est le seul objet que l'assujetti puisse produire pour répondre de ce dont il répond de toute façon.** Le socle n'établit pas cette conséquence ; il établit certaines de ses prémisses — la constante du porteur est une lecture de l'auteur, et l'absence de ressource pour désigner un tiers n'est établie que pour l'article 12.1.

Une réserve, enfin : cette lecture explique pourquoi l'encadrement est nécessaire, non qu'il soit suffisant. Rien, au socle, ne dit qu'un cadre correctement posé libère l'assujetti de quoi que ce soit, ni que la démonstrabilité d'un *frame* vaille preuve de conformité. La question est juridique, et reste ouverte.

## 13.4 Le principe directeur

Ce qui précède se resserre en un énoncé, que les Parties VI et VII reprennent.

**Sous exigence réglementaire stricte, le processus est imposé de façon déterministe par le cadre, qui invoque les agents ; les agents n'orchestrent pas le processus.** Dans le vocabulaire des options d'orchestration (*orchestration options*) du chapitre 5, ce sont les positions OO3 et OO4 — celles où la main qui commande l'enchaînement est le cadre, la différence entre les deux tenant à ce que l'agent sait du processus, non à ce qu'il commande[^7].

Ce principe porte quatre conditions, qu'il faut énoncer avec lui sous peine de le falsifier. **Première** : il est une inférence d'auteur, construite par transposition de trois sources dont le socle n'établit l'application ni au Canada ni à la finance canadienne, dont deux partagent une autrice et deux une organisation. **Deuxième** : « exigence réglementaire stricte » n'est pas défini par le socle. Le verdict du préprint borne son domaine aux situations où des exigences strictes d'exécution et de documentation s'appliquent[^8] ; qualifier un processus canadien au regard de ce critère reste un travail d'institution. **Troisième** : l'encadrement se paie. L'effort initial et la maintenance figurent explicitement parmi les critères de sélection du cadre[^7] — un positionnement OO3 ou OO4 exige d'expliciter le processus, et expliciter coûte, à la construction comme à l'entretien. **Quatrième** : le principe dit où placer la main qui commande ; il ne dit ni ce qu'un *frame* doit contenir, ni comment on l'écrit. La table du §13.1 en donne désormais **cinq attentes** — inventaire, cotation, cycle de vie, documentation, surveillance —, mais elles disent ce que le cadre doit **rendre possible**, non ce qu'il doit décider. Et de la ligne directrice de l'AMF, l'un des deux textes dont l'entrée en vigueur commune est fixée au 1er mai 2027, ce chapitre ne dit toujours rien.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Deux acquis, et une lecture. **Premièrement**, la traduction des exigences canadiennes en cadres est large mais inégale, et son inégalité est celle de la lecture : sur les onze entrées examinées, neuf produisent une contrainte — cinq d'E-23, trois de l'article 12.1, une de l'avis 11-348 —, une seule n'en produit aucune, la ligne directrice de l'AMF, dont le socle ne porte que le calendrier. Les cinq entrées d'E-23 ne figuraient pas dans le premier état de cette table : elles y sont entrées par l'extraction du texte intégral, et leur arrivée vérifie ce que le chapitre avançait déjà — la table mesure l'effort de lecture, non l'exigence des textes. **Deuxièmement**, la convergence sur l'encadrement déterministe existe, mais elle est le fait d'un milieu partiellement chevauchant plutôt que de trois observateurs indépendants : Rinderle-Ma cosigne deux des sources, IBM en fournit une et figure parmi les organisations de la deuxième. **Enfin**, comme lecture de l'auteur et non comme acquis : les trois textes canadiens désignent, aux yeux de cet ouvrage, le même porteur — celui qui exploite le système. Le socle porte un fait générateur pour l'article 12.1 et deux périmètres d'application pour E-23 et l'avis 11-348, sans les rapprocher ; le rapprochement est de l'auteur.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas qu'E-23 attende un cadre : elle attend un programme, et ce sont les conditions de possibilité de ce programme sur un système agentique, non ses attentes, que la table dérive. Il ne dit pas ce qu'est « le modèle » d'un assemblage d'agents — question que le texte laisse entière et que les institutions fédérales auront à trancher. Il ne dit pas ce que prescrit la ligne directrice de l'AMF, dont le contenu n'est pas au socle — ni ce qu'E-23 et l'avis 11-348 prévoient quant à la désignation d'un tiers. Il ne dit pas que le droit canadien résolve l'écart de responsabilité : la désignation constante qu'il lit dans les trois textes n'est pas une allocation d'imputabilité, et il n'émet aucun avis juridique. Il ne dit pas que l'orchestration non encadrée soit *démontrée* indéfendable au Canada : le verdict dont il part est européen, hors finance, adossé à un préprint dont les auteurs déclarent des menaces à la validité — et les deux autres sources ne portent aucun verdict, elles recommandent. Il ne dit pas que l'encadrement suffise à répondre d'un comportement émergent — seulement qu'il est le seul objet dont l'assujetti puisse démontrer la teneur. Il ne dit rien, enfin, de ce qu'il faut assembler : la matrice des protocoles et des exigences est l'objet du chapitre 18, l'architecture de référence celui du chapitre 19, leur instanciation celui de la Partie VII.

Le pont de cet ouvrage n'est donc pas une déduction. C'est un raisonnement, exposé pour être contesté — et sa partie la plus solide n'est ni la convergence de trois sources, ni la constante que l'auteur lit dans trois textes : c'est ce qu'un seul texte, l'article 12.1, fait peser sur l'entreprise qui rend la décision.

---

## Notes

[^1]: PRD §7.3, **F-09** (niveau **[A/B mixte]** — [A] pour les faits des passes 1-2, [B] pour les exigences opératoires extraites le 16 juill. 2026 ; **[B] est sous [A] dans la taxonomie du §7 : l'extraction n'élève pas l'entrée, elle l'enrichit d'un contenu de rang inférieur**). **Présente note : strate [A]** — dates, portée, définition de « modèle », et le fait que la couverture agentique est une inférence d'analystes. **L'énumération [A] de F-09 est close** : tout ce qui n'y figure pas relève de la strate [B], y compris deux faits que ce chapitre mobilise et qu'il serait tentant de porter en [A] — l'**anticipation** par le BSIF de modèles à apprentissage et décision autonomes, et la **vérification négative** (F-09 range expressément « la re-vérification mécanique de la vérification négative » sous [B]). Les deux sont donc tracés en note [^15], avec les cinq attentes opératoires traduites au §13.1. *Confusion relevée par la relecture adversariale du 17 juill. 2026 : la présente note portait ces deux faits en [A]. C'est la faute même que la rédaction du ch. 18 avait relevée et qui a produit le PRD v1.7 — elle se reforme à chaque passe, parce que [B] se lit spontanément comme « mieux vérifié » alors qu'il est « moins éprouvé ».* Source primaire : osfi-bsif.gc.ca, ligne directrice E-23 (version finale du 11 septembre 2025, en vigueur le 1er mai 2027 ; institutions financières fédérales, y compris succursales étrangères dans la mesure compatible). Faits [A] mobilisés : définition de « modèle » incluant explicitement les méthodes d'IA et d'apprentissage automatique ; dates et portée. Le motif R-7 (« E-23 ») ressort dans ce chapitre en contexte réglementaire pur, sans correspondance produit ↔ réglementation : filtré conformément à PRDPlan §4.3.

[^2]: PRD §7.3, **F-25** (niveau [A]). Sources : lautorite.qc.ca ; Norton Rose Fulbright ; rapport annuel Desjardins 2025. Projet publié le 3 juillet 2025, consultation close le 7 novembre 2025 ; **version finale publiée le 30 mars 2026, en vigueur le 1er mai 2027** — même date qu'E-23. **Réserve F-25** : ne jamais écrire « en attente » ni « en projet » (état périmé depuis le 30 mars 2026) — Annexe D §D.7. Le socle ne porte que le calendrier ; le contenu du texte relève de la lacune PRD §10.4. Traitement : ch. 11.

[^3]: PRD §7.3, **F-26** (niveau [B] — consulté directement sur osc.ca le 16 juillet 2026). « CSA Staff Notice and Consultation 11-348 — Applicability of Canadian Securities Laws and the use of Artificial Intelligence Systems in Capital Markets », 5 décembre 2024. Faits mobilisés : doctrine d'applicabilité (les lois existantes s'appliquent ; l'avis ne crée ni ne modifie aucune exigence — formule reprise du socle en français, l'instrument étant en anglais : ce n'est pas une citation verbatim) ; définition des systèmes d'IA incluant explicitement des niveaux variables d'autonomie et d'adaptativité après déploiement ; sept catégories d'assujettis. Traitement : ch. 12.

[^4]: PRD §7.3, **F-27** (niveau [B] — texte officiel consulté sur LégisQuébec le 16 juillet 2026). Article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1), en vigueur depuis le 22 septembre 2023 (2021, c. 25, a. 110). Les formules entre guillemets sont citées verbatim du texte officiel (Annexe D §D.5 : citer, ne pas paraphraser), à l'exception de « toute entreprise », que le socle rapporte comme déclencheur du régime sans en établir le libellé officiel (même traitement qu'au ch. 11 §11.2). Le socle ne portant que le français, aucune glose anglaise du libellé n'est proposée ici. **Réserve d'interprétation du socle (niveau [C])** : selon l'analyse Fasken, une intervention humaine significative avant la décision écarte l'application de l'article — nuance non confrontée aux positions de la CAI (PRD §10.4) ; le présent chapitre n'en fait aucun usage et ne construit sur elle aucune contrainte. Traitement complet, y compris la distinction entre l'humain-dans-la-boucle (*human-in-the-loop*) et la révision *a posteriori* : **ch. 11 §11.3 et §11.4**, dont les trois contraintes d'architecture sont reprises ici en table plutôt que redéveloppées.

[^5]: PRD §7.7, **F-36** (niveau [B] — article lu intégralement ; confiance « haute **pour l'attribution** »). Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al. (**18 auteurs — universités et industrie dont IBM Research, SAP, Université d'Ottawa**), « Agentic Business Process Management: A Research Manifesto », *Information Systems* 140, 102738 (2026) — version à privilégier en citation (PRD §9.1) ; arXiv:2603.18916v3. Apports mobilisés : autonomie encadrée (*framed autonomy*) comme mécanisme premier de gouvernance ; *frames* normatifs distincts des *frames* opérationnels ; distinction **adaptation** (éphémère, d'instance) / **évolution** (persistante, du modèle de processus) ; explicabilité reliée par les auteurs à la conformité réglementaire — **RGPD et AI Act européen**, instruments européens — et à la finance comme domaine à haut risque. La composition des auteurs (IBM Research) et la présence de Rinderle-Ma sont établies par cette entrée : elles fondent le constat de non-indépendance du §13.2. Traitement : ch. 6.

[^6]: PRD §7.7, **F-36**, défi transversal **C4** : l'**écart de responsabilité** (*responsibility gap*) — indétermination de l'imputabilité juridique entre développeur, organisation qui impose le *frame*, fournisseur de modèle et comportement émergent du système multi-agents. Source primaire : *ibid.* Préparation : ch. 6 §6.5, qui pose la proposition reprise au §13.3 et la marque déjà comme inférence de cet ouvrage, non du manifeste.

[^7]: PRD §7.7, **F-37** (niveau [B] — article lu intégralement ; confiance haute pour le cadre, moyenne pour les chiffres). **Rinderle-Ma**, Mangler et al. (TU Munich), « Design and Implementation of Agentic Orchestrations and Orchestration of Agents », arXiv:2606.31518v1, 30 juin 2026. Formulation imposée (PRDPlan §4.4, cas « préprint académique ») : **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité (expériences initiales, invites non comparées, facteurs confondants) — le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration seulement. Apports mobilisés : taxonomie OO1–OO4 (options d'orchestration) ; critères de sélection incluant explicitement l'effort initial et la maintenance. La cosignature de Rinderle-Ma avec F-36 est établie par la confrontation des deux entrées du socle. Traitement : ch. 5.

[^8]: PRD §7.7, **F-37**, apports (4) et (5). Enseignement de conception : la journalisation confiée aux agents « n'est généralement pas recommandée ». Verdict pour les scénarios réglementés (processus de don de sang sous directive européenne 2002/98/CE) : l'orchestration non encadrée est « inacceptable » quand des exigences strictes d'exécution et de documentation s'appliquent ; les tâches essentielles doivent être imposées de façon déterministe par le cadre. Source primaire : arXiv:2606.31518v1, sous les réserves de la note [^7]. Les résultats chiffrés du même apport (F1 de 0,40 / 0,97 / 1,00) sont exposés au **ch. 5 §5.4** en illustration seulement et ne sont pas repris ici.

[^9]: PRD §7.8, **F-46** (niveau [B] ; « haute **pour l'attribution** »). Source primaire : ibm.com/think/architectures/patterns/agentic-ai (pattern officiel « Agentic AI », mis à jour le 21 février 2025, lu via navigateur). Faits mobilisés : les **workflows statiques** (*static workflows*, BPMN/BPEL) sont **explicitement recommandés par IBM pour les processus sous surveillance réglementaire** (auditabilité, conformité, transferts définis) ; le socle érige la rencontre de F-36, F-37 et F-46 en **convergence à trois sources** et en fait le principe directeur du blueprint (Annexe B). **État du socle au 17 juill. 2026** : §7.8 (F-46) portait l'adjectif « **indépendantes** » — l'Annexe B.1 et le §6 écrivaient déjà la même formule sans lui. L'adjectif était réfuté par PRD §7.7 lui-même (cosignature Rinderle-Ma pour F-36/F-37 ; IBM Research parmi les 18 auteurs de F-36 et IBM éditeur de F-46) ; signalé par les rédactions des ch. 5 et 13, il a été **retiré du PRD le 16 juillet 2026** (v1.5), puis de l'abstract de TOC.md (v1.3). Le PRD a été corrigé **en premier**, comme le signalement l'exigeait — il est la seule autorité factuelle. **Il n'y a donc plus de divergence interne, ni d'adjectif à contester** : le §13.2 expose la démonstration qui a motivé la rétractation, et le socle en porte désormais la formulation imposée (F-46 : jamais « trois sources indépendantes recommandent l'encadrement déterministe »). **Réserve du socle** : pattern **générique** — IBM ne publie pas d'architecture agentique spécifique aux services financiers (vérifié : introuvable sur ibm.com/architectures et Redbooks). Forme du glossaire : Annexe D §D.6.

[^10]: PRD §8.2.4 (règle d'attribution : la couverture agentique d'E-23 est une inférence d'analystes juridiques — jamais « le BSIF exige pour l'IA agentique », toujours « couverture implicite via la définition de modèle ») ; formulation imposée par PRDPlan §4.4, reprise au §13.1. Développement : ch. 9 §9.3. Sur le statut des analystes nommés : ch. 9 note [^5] — quatre des cinq sont des cabinets figurant au corpus de corroboration secondaire admise (PRD §9.2), Sookman n'en est pas un ; le socle n'établit pas l'indépendance de leurs analyses, et aucun argument du présent chapitre n'en dépend.

[^11]: PRD §7.3, **F-10** (niveau [A]) — **renvoi seulement**. Rapport conjoint du BSIF et de l'ACFC publié le 24 septembre 2024 (osfi-bsif.gc.ca) : risque de modèle accru propre à l'IA — très grand nombre de paramètres appris de façon autonome, **relations causales entrées-sorties souvent indéterminables** ; lien explicite au cadre E-23. La conséquence d'architecture (l'explication ne peut pas être extraite du modèle *a posteriori* et doit être produite par ce qui l'entoure) est posée au **ch. 9 §9.4** comme inférence de cet ouvrage et reprise ici comme telle. **Renvoi entériné** par [TOC.md](../../TOC.md) v1.4 : PRD §6 assigne F-10 à la Partie III, et le ch. 9 §9.4 désigne explicitement ce chapitre comme le lieu d'exploitation de son inférence.

[^12]: PRD §10.4 (lacune ouverte, « réglementaire fin ») : contenu article par article de la ligne directrice IA finale de l'AMF (« seules les dates sont au socle ») ; positions détaillées de la CAI sur l'article 12.1 appliqué aux systèmes multi-agents ; suites de la consultation ACVM 11-348. **Portée du régime de la Loi 25 à l'égard des institutions sous charte fédérale** : le socle est muet — question ouverte posée au ch. 11 §11.3 (troisième question de l'encadré) et non tranchée ici. Interdiction de combler par du non-vérifié (PRD §10) ; format des encadrés : PRDPlan §4.4.

[^13]: PRD §8.4 (neutralité fournisseur) : le portefeuille IBM est retenu comme **cas d'instanciation documenté par sources primaires**, pas comme recommandation d'achat ni verdict comparatif ; chaque capacité est attribuée à la documentation de l'éditeur, avec sa date et son statut. Le présent chapitre n'enregistre de F-46 qu'une **position d'architecture publiée par IBM**, attribuée à IBM à chaque occurrence ; les alternatives non-IBM du socle (Partie II) et l'instanciation du portefeuille relèvent de la **Partie VII**.

[^14]: **Renvoi de méthode** — forme du fait négatif vérifié au socle, donnée en contraste à l'encadré du §13.2. PRD §7.4, **F-35** (« fait négatif vérifié 9-0 ») : « Recherche exhaustive des chaînes “FDX”, “Financial Data Exchange”, “FAPI”, “OAuth” dans le règlement prépublié, le communiqué et la page Budget 2025 : zéro occurrence. » PRD §7.3, **F-09** : « E-23 n'emploie jamais “agentique”, “agents” ni “orchestration” ». PRD §7.8, **F-46** : « vérifié : introuvable sur ibm.com/architectures et Redbooks ». Aucune entrée du socle ne porte de fait négatif de cette forme, sur le Canada, pour F-36, F-37 ou F-46 : l'absence relevée au §13.2 est une absence **au socle**, non un fait négatif établi **dans les sources**. F-35 est mobilisé ici **en renvoi de méthode seulement** — aucun de ses faits n'est repris (traitement : ch. 17) ; renvoi **entériné** par [TOC.md](../../TOC.md) v1.4.

[^15]: PRD §7.3, **F-09**, **strate [B]** — attentes opératoires extraites du texte intégral d'E-23 le 16 juillet 2026 par lecture directe de la source officielle, **sans vote adversarial**. **Rappel de taxonomie (PRD §7)** : [B] est **sous** [A] ; l'extraction n'élève pas l'entrée, elle l'enrichit d'un contenu de rang inférieur. Les cinq attentes traduites au §13.1 sont donc adossées à la strate la moins forte de l'entrée, et le §13.1 le porte en marquage. Sources primaires : osfi-bsif.gc.ca, version EN (`/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027`) et FR (`/fr/consignes/repertoire-consignes/ligne-directrice-e-23-gestion-du-risque-modelisation-2027`) ; lettre d'accompagnement du 11 septembre 2025. Faits mobilisés, par renvoi de section du texte : **inventaire** (§C.1, principe 2.1) ; **cotation** (§A.3, §C.2, principes 2.2–2.3) ; **cycle de vie** à cinq volets, « *not necessarily sequential* » (§A.4) ; **documentation** (§D.2, principe 3.3) et champs de l'**Appendice 1** ; **surveillance continue** (§D.2, principe 3.6), dont les processus traitant « *autonomous decision making, autonomous re-parametrization* » ; **note 1** — reprise de la définition **OCDE** de l'IA (« *vary in their levels of autonomy and adaptiveness after deployment* »), que le socle désigne comme le socle textuel réel de la couverture implicite. **Réserve de modalité, impérative (PRDPlan §4.4)** : E-23 est une ligne directrice **fondée sur des principes**, ses douze principes rédigés au conditionnel (« *should* ») — écrire « **attendu par** E-23 », jamais « exigé par E-23 » ni « E-23 impose ». **Réserve de vocabulaire** : E-23 n'emploie **jamais** « fiche de modèle » / « *model card* » (0 occurrence, EN et FR) — parler de « documentation de modèle » et d'« inventaire ». **Réserve de portée** : le socle porte les attentes du texte, non leur application à un système agentique — E-23 ne nomme ni les agents ni l'orchestration ([^1]). La traduction conduite au §13.1 est une **inférence d'auteur** sur les conditions de possibilité de ces attentes, marquée comme telle à chaque ligne. Passe de dérivation conduite le 17 juillet 2026, sur arbitrage de gouvernance (PRDPlan §4.2, règle d'escalade) : le premier état de ce chapitre laissait la traduction à conduire et le signalait.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 17 juillet 2026 — passe de dérivation du §13.1).
                                   VOLUMÉTRIE — RECOMPTÉE LE 17 JUILL. 2026 APRÈS LA PASSE ET SA RELECTURE :
                                     corps (commande de référence PRDPlan §4.2) ......... 5089
                                     cible TOC .......................................... ~3400
                                     écart .............................................. +50 %  ASSUMÉ, DOCUMENTÉ
                                   L'écart est inscrit au TOC v1.4 et n'est PAS corrigé : la volumétrie est
                                   indicative et non normative (PRDPlan §1.1), et un écart se documente — il ne
                                   se corrige pas par amputation d'une réserve. Trois causes, toutes tracées :
                                   (a) cinq lignes de tableau ajoutées par la dérivation E-23 ; (b) la garde
                                   « E-23 attend un programme, non une architecture » et la limite « l'objet
                                   d'E-23 est le modèle » ; (c) les correctifs de la relecture du 17 juill.
                                   (marquage des strates, bornage du paragraphe OCDE, conversion de l'encadré
                                   AMF au cas 2 de §4.4). Le ch. 13 est un chapitre de TABLEAU : son corps est
                                   structurellement plus lourd à contenu égal (PRDPlan §4.2).
                                   COMMANDES DE CE BLOC : PÉRIMÉES ET RETIRÉES. Le chapitre publiait deux
                                   commandes maison (B et C) faute de commande de référence au plan. PRDPlan
                                   §4.2 en fixe une depuis le 17 juill. 2026 — c'est désormais la seule
                                   autorité, et B/C ne doivent plus être réexécutées : elles donnent d'autres
                                   chiffres (B = 4862 au moment de la relecture) et la coexistence de trois
                                   méthodes a fait conclure à la relecture que le chiffre du TOC était
                                   irreproductible. Il ne l'est pas : il l'est par la commande de référence,
                                   et par elle seule.
                                   INCIDENT CONSIGNÉ — le poste dont l'objet EST l'arithmétique était faux.
                                   Ce bloc s'était lui-même averti (« B est à 35 mots du plafond : tout ajout
                                   ultérieur impose de recompter »). La passe du 17 juill. a ajouté cinq lignes
                                   et trois paragraphes SANS recompter, et le poste 4 certifiait encore la table
                                   à six lignes. Relevé par la relecture adversariale, non par la passe.
                                   LEÇON : une passe qui construit doit re-parcourir SES PROPRES ATTESTATIONS,
                                   pas seulement le texte — un bloc qualité est du contenu, pas un journal.
     2. Traçabilité (CA-1, CA-5) . fait (15 notes ; tout fait central tracé F-09/F-25/F-26/F-27/F-36/F-37/F-46,
                                   F-10 et F-35 explicitement en renvoi ; termes anglais entre parenthèses et en
                                   italique à la 1re occurrence du chapitre : frames, responsibility gap, framed
                                   autonomy, normative frames, operational frames, static workflows, orchestration
                                   options, model risk. Toute conclusion non portée par le socle est introduite
                                   par « Lecture de l'auteur » ou marquée « inférence d'auteur » dans la colonne
                                   « Statut du lien » du tableau §13.1.)
     3. Balayage garde-fous ...... fait :
                                   - §8.2.4 : formulation imposée reproduite en §13.1 (charnière causale comprise :
                                     « ne nomme ni l'agentique ni les agents ; sa définition de « modèle » englobe
                                     les méthodes d'IA et d'apprentissage automatique, d'où une couverture implicite
                                     que les analystes juridiques canadiens (…) tiennent pour acquise ») ET dans la
                                     cellule « Statut du lien » de la ligne E-23 du tableau, qui est la première
                                     rencontre du lecteur avec le motif (correctif de relecture, réserve 9) ;
                                     aucune occurrence de « E-23 exige pour l'agentique » (Annexe D §D.7) ;
                                   - réserves F-37 : formulation « préprint » de §4.4 posée à la 1re occurrence du
                                     verdict (§13.2) et rappelée en clôture ; les chiffres F1 (0,40/0,97/1,00) ne
                                     sont PAS repris — renvoi au ch. 5 §5.4 ;
                                   - F-36 : cité comme position argumentée de ses auteurs à chaque occurrence
                                     (confiance « haute pour l'attribution ») ;
                                   - §8.4 + F-46 : la recommandation des workflows statiques est attribuée à IBM à
                                     chaque occurrence ; réserve « pattern générique, aucune architecture agentique
                                     spécifique aux services financiers » posée à la 1re occurrence ; aucun superlatif ;
                                     aucune instanciation de portefeuille (renvoi Partie VII) ;
                                   - réserve F-25 (motif « en attente|en projet ») : aucune occurrence fautive ;
                                     forme datée employée (« finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 ») ;
                                     le raccourci « les deux lignes directrices datées du 1er mai 2027 » du §13.4 —
                                     qui travestissait une date d'ENTRÉE EN VIGUEUR en date de publication — est
                                     corrigé (réserve 4) ;
                                   - motif R-7 (« E-23|B-13 ») : ressort aux §13.1, §13.3 et §13.4 en contexte
                                     réglementaire pur — filtré (PRDPlan §4.3). Au §13.2, contexte FOURNISSEUR
                                     (F-46) : INSPECTÉ et non filtré (correctif de relecture, réserve 8) — aucune
                                     conformité revendiquée, aucun rapprochement IBM ↔ E-23 posé, absence au socle
                                     exposée en encadré, §8.4 rappelé en note [^13]. « B-13 » : 0 occurrence ;
                                   - motifs R-8 (« ACP », « control plane », « plan de contrôle ») : 0 occurrence ;
                                   - motifs R-1, R-2, R-3, R-4, R-5, R-6, réserve F-01 (« sécuris »), §8.2.6 (« 70 % ») :
                                     0 occurrence. R-5 : « standard technique » ressort en note [^14] seulement, en
                                     renvoi de méthode sur F-35 (fait négatif vérifié cité comme FORME, aucun fait
                                     du cadre bancaire repris) — inspecté, sans objet ;
                                   - §8.2.2 / §7.5 (métriques auto-déclarées) : SANS OBJET — aucune métrique
                                     d'institution ni d'éditeur dans ce chapitre.
     4. Arithmétique ............. aucun calcul de durée, d'écart ou de pourcentage n'est posé dans ce chapitre.
                                   RECOMPTÉ LE 17 JUILL. 2026, LIGNE À LIGNE CONTRE LE TABLEAU §13.1 :
                                     lignes de la table ................................. 11
                                     produisant une contrainte .......................... 9  (5 E-23 + 3 art. 12.1
                                                                                             + 1 avis 11-348)
                                     produisant un périmètre, non un cadre .............. 1  (E-23 — périmètre)
                                     ne produisant rien ................................. 1  (AMF)
                                     contrôle : 9 + 1 + 1 = 11 .......................... OK
                                   Cohérence des décomptes entre chapeau, §13.1, §13.4 et conclusion : vérifiée,
                                   les quatre disent la même chose. Confirmé indépendamment par la relecture
                                   adversariale du 17 juill. 2026, qui n'a trouvé AUCUNE erreur de cardinal dans
                                   la prose. Autres décomptes : « quatre porteurs candidats » (F-36 C4), « sept
                                   catégories d'assujettis » (F-26), « dix-huit auteurs » (F-36), « quatre
                                   conditions » (§13.4) — tous conformes au socle.
                                   ÉTAT ANTÉRIEUR, CONSIGNÉ : ce poste a certifié « 6 lignes ; 2 sans cadre ;
                                   4 avec cadre dont 3 de l'art. 12.1 » APRÈS que la passe du 17 juill. eut porté
                                   la table à onze lignes. Le poste dont l'objet est l'arithmétique était le seul
                                   à ne pas avoir été recompté. Voir le poste 1.
     5. Relecture adversariale ... FAIT — DEUX VAGUES, sur deux états distincts du fichier.
                                   Vague 1 (16 juill. 2026, deux relecteurs indépendants) : 6 bloquants,
                                   10 réserves — sur l'état À SIX LIGNES, qui n'existe plus.
                                   Vague 2 (17 juill. 2026, relecteur distinct du rédacteur, sur la passe de
                                   dérivation) : 6 bloquants, 6 réserves, 3 points de gouvernance. TOUS traités :
                                     B1 §13.2 rapportait au présent l'adjectif « indépendantes » que PRD §7.8 a
                                        RÉTRACTÉ le 16 juill. — le chapitre combattait un adversaire désarmé, et
                                        le bloc d'arbitrage ci-dessous CERTIFIAIT à tort sa conformité.
                                        → §13.2 et [^9] réécrits ; la rétractation est exposée comme acquise.
                                     B2 vérification négative et anticipation d'autonomie portées en [A] alors
                                        que F-09 range expressément la re-vérification sous [B] et que son
                                        énumération [A] est close → reclassées en [B] (en-tête, [^1], table).
                                     B3 « cinq EXIGENCES d'inventaire, de cotation… » = forme proscrite par §4.4,
                                        passée sous le motif `exigence.*E-23` (le sigle n'était pas sur la ligne)
                                        → « cinq attentes » ; motif §4.3 complété (réserve F-09 bis).
                                     B4 argument du silence réintroduit sur l'avis 11-348 (« aucun des deux n'a eu
                                        besoin de nommer l'agentique »), alors que le socle ne porte AUCUN fait
                                        négatif pour cet avis et que le §13.3 se l'interdit → restreint à E-23.
                                     B5 « seule attente dont l'objet nomme l'autonomie » réfuté par F-09 (le
                                        « level of autonomy » est aussi un facteur de cotation) → reformulé, et
                                        le facteur versé à la ligne cotation, qu'il renforce.
                                     B6 bloc qualité intégralement périmé → postes 1, 2, 4, 5 réécrits.
                                     R1-R5 traités (strates, garde étendue à la cotation et à la surveillance,
                                        §8.2.4, en-tête de colonne « Texte (source) », encadré AMF converti au
                                        cas 2 de §4.4 avec le 403 de lautorite.qc.ca).
                                     R6 INFONDÉE, mais révélatrice : « 4701 n'est reproductible par aucune
                                        commande du chapitre » — exact, et c'est le défaut. Le chiffre EST
                                        reproductible par la commande de référence de PRDPlan §4.2 ; le chapitre
                                        publiait encore ses commandes maison, qui en donnent d'autres. Commandes
                                        maison retirées (poste 1).
                                     G1 thèse du TOC (« CHAQUE exigence », « EST indéfendable ») → corrigée au
                                        TOC v1.4 : universel et verdict que le chapitre réfute lui-même. Les
                                        ch. 2 et 4 avaient été corrigés de ces deux fautes en v1.3 ; le chapitre
                                        pivot y avait échappé seul.
                                   VERDICT DE LA VAGUE 2 : « la passe du 17 juillet a construit correctement et
                                   vérifié incorrectement » — les cinq dérivations E-23 sont jugées défendables
                                   (verbatim fidèle section par section, marquage porté, garde réelle, limite
                                   exposée) ; ce qui bloquait était l'appareil de vérification, non le fond.
     6. Passe F-09 (16 juill. 2026) FAIT — périmètre strict : marquage de F-09 en [A/B mixte] et strate [A]
                                   déclarée en note [^1] ([B] est SOUS [A] : l'extraction enrichit, n'élève pas) ;
                                   affirmations périmées d'absence d'extraction corrigées (§13.1 tableau et prose,
                                   §13.3, §13.4, conclusion, note [^1]) ; encadré §13.1 restreint à la seule lacune
                                   qui reste ouverte (AMF) ; « ce qu'E-23 exige » → « ce qu'E-23 attend »
                                   (réserve F-09, PRDPlan §4.4). « fiche de modèle » / « model card » : 0 occurrence
                                   avant comme après — sur-correction sans objet ici. Convergence à trois sources et
                                   non-indépendance : NON touchées. Volumétrie recomptée (B 3730 → 3705, C 3346 → 3317).

                                   RÉFUTÉ ET CORRIGÉ — constats bloquants (tous fondés ; les 6 ont été vérifiés
                                   contre PRD.md avant application) :
                                   a) [FABRICATION SUR LE DÉPÔT] Le jet écrivait « PRD §7.8 (F-46) et Annexe B.1
                                      écrivent “convergence à trois sources” sans lui [l'adjectif] ». FAUX, et
                                      vérifiable en une commande : PRD.md L180 (§7.8, entrée F-46 elle-même) porte
                                      « **Convergence à trois sources indépendantes** », en gras. Seules l'Annexe B.1
                                      (L310) et le §6 (L93) omettent l'adjectif. Conséquences en chaîne, toutes
                                      corrigées : (1) le corps §13.2 et la note [^9] rapportaient le socle de façon
                                      inexacte en supprimant silencieusement le mot que le paragraphe suivant
                                      consacrait à réfuter (violation CA-1) — la phrase du socle est désormais citée
                                      telle quelle AVANT d'être requalifiée, et la note [^9] est alignée sur le
                                      libellé réel de F-46 et signale la divergence interne §7.8 / Annexe B.1 ;
                                      (2) le chapitre dissimulait que le socle porte LUI-MÊME la thèse réfutée —
                                      c'est maintenant exposé ; (3) le signalement de gouvernance a) ordonnait de
                                      corriger l'abstract de TOC.md SEULEMENT, en certifiant le PRD indemne, ce qui
                                      aurait laissé F-46 non corrigée alors que le PRD prime — la gouvernance a) est
                                      redirigée vers un amendement de PRD §7.8 en priorité. Le ch. 5 avait commis la
                                      même omission et demandé l'arbitrage AVANT le ch. 13 ; le ch. 13 en héritait
                                      sans re-vérifier §7.8. LEÇON : un signalement de gouvernance qui cite le socle
                                      se re-vérifie contre le socle, jamais contre le chapitre amont qui le rapporte.
                                   b) [FAIT NÉGATIF FABRIQUÉ] « **Aucune des trois sources ne mentionne le Canada,
                                      la finance canadienne, E-23, (…) ni l'article 12.1** », en gras, sous le membre
                                      « Ce que le socle établit » de l'encadré du §13.2. Le socle n'établit pas ce que
                                      ces sources NE mentionnent PAS : aucune recherche exhaustive de chaînes n'a été
                                      conduite — l'encadré le concédait trois lignes plus bas. Contre-exemple dans la
                                      note [^5] du chapitre lui-même : le manifeste compte une affiliation à
                                      l'Université d'Ottawa, donc F-36 mentionne le Canada et le socle l'enregistre.
                                      Le chapitre contredisait une entrée du socle qu'il citait deux paragraphes plus
                                      haut, et confondait absence AU SOCLE et absence DANS LA SOURCE — la confusion
                                      même qu'il reproche à E-23 en §13.1. Requalifié en absence-au-socle ; gras purgé
                                      du registre du fait vérifié ; contraste avec les formes réelles du fait négatif
                                      du socle (F-35, F-09, F-46) posé et tracé en note [^14] ; affiliation d'Ottawa
                                      exposée. Répercuté au §13.4 (« Première condition ») et en conclusion.
                                   c) [FAIT NÉGATIF NON VÉRIFIÉ, PRÉSENTÉ COMME FAIT] « Aucun des trois textes
                                      n'offre à l'entité qui exploite la ressource de désigner un tiers » — sur deux
                                      textes dont le chapitre déclare lui-même que le socle ne porte pas le contenu.
                                      Le chapitre s'appliquait deux régimes de preuve opposés : en §13.1, l'ignorance
                                      du texte interdit toute dérivation ; en §13.3, la même ignorance devenait un
                                      argument du silence — et c'était la prémisse porteuse de la conclusion donnée
                                      en clôture comme « la partie la plus solide ». Restreint à l'art. 12.1, seul
                                      texte dont le socle porte le libellé ; l'ouvrage se refuse désormais
                                      explicitement l'argument du silence sur E-23 et 11-348. « il établit chacune de
                                      ses prémisses » → « il établit certaines de ses prémisses ».
                                   d) [SYNTHÈSE D'AUTEUR NON MARQUÉE] « Trois textes, trois régimes, une constante :
                                      **le porteur est l'entité qui exploite** » — en gras, sans marqueur, agrégeant
                                      trois objets juridiquement différents (un fait générateur pour l'art. 12.1,
                                      deux périmètres d'application pour E-23 et 11-348) et forgeant un terme absent
                                      du socle. Le marqueur du paragraphe suivant ne couvrait PAS la constante : il
                                      portait sur l'étape d'après et la présupposait acquise. Un chapitre qui
                                      « n'émet aucun avis juridique » (PRD §3) livrait ainsi sa caractérisation
                                      juridique la plus forte sans marqueur. Marqué à la source ; les trois natures
                                      distinguées ; « l'entité qui exploite » explicitement donnée pour l'expression
                                      de l'auteur. Conclusion alignée : la constante SORT de la liste des acquis
                                      (« Trois acquis » → « Deux acquis, et une lecture ») et la clôture, qui reposait
                                      entièrement dessus, est réécrite.
                                   e) [= a), volet gouvernance] Point a) des signalements corrigé et redirigé vers
                                      PRD §7.8 ; le corps et la note [^9] citent maintenant la formule du socle avant
                                      de la requalifier.
                                   f) [ATTRIBUTION FAUTIVE, ligne programmatique] « trois sources convergent pour
                                      tenir l'orchestration non encadrée pour **indéfendable** » — ni le manifeste
                                      (F-36) ni le pattern d'IBM (F-46) ne portent ce verdict : ils RECOMMANDENT
                                      l'encadrement, ce qui n'est pas le même acte de langage. F-37 seul porte un
                                      verdict d'« inacceptabilité », borné à un processus européen de don de sang.
                                      La réserve « haute POUR L'ATTRIBUTION » qui pèse sur F-36 et F-46 visait
                                      précisément ce point, que l'en-tête s'engage à surveiller. Aligné sur la
                                      formulation que le §13.2 établissait déjà correctement trois paragraphes plus
                                      loin ; « il recommande, il ne juge pas » posé pour F-36 et F-46 ; répercuté en
                                      conclusion.

                                   RÉSERVES TRAITÉES (10/10 appliquées ; aucune écartée) :
                                   1) Gloses anglaises non tracées « (*autonomy*) », « (*adaptiveness*) »,
                                      « (*decision based exclusively on automated processing*) » : le chapitre
                                      restituait un original anglais qu'il n'a pas lu, dans la colonne « Ce que le
                                      socle établit », alors que F-26 ne consigne que le français et que l'art. 12.1
                                      est un texte français. RETIRÉES ; mention « instrument en anglais ; le socle
                                      n'en porte pas le libellé » posée dans la cellule. CA-5 n'exige la glose que
                                      pour la terminologie du glossaire, non pour les formules opératoires
                                      d'instruments dont le socle ne porte pas le texte.
                                   2) 11-348 compté comme « désignant » un porteur alors qu'il ne crée aucune
                                      obligation (F-26 : « la guidance ne crée ni ne modifie aucune exigence ») :
                                      dissymétrie désormais marquée — « le porteur qu'il désigne l'est par renvoi au
                                      droit en vigueur, non par l'avis ».
                                   3) « obligation inconditionnelle » (caractérisation d'auteur non marquée, dans la
                                      colonne réservée au socle, et imprécise — l'obligation est conditionnée au
                                      déclencheur « exclusivement automatisé ») → « seule des trois obligations à ne
                                      pas être subordonnée à une demande ». La réserve Fasken [C] n'est pas mobilisée.
                                   4) « les deux lignes directrices datées du 1er mai 2027 » → « dont l'entrée en
                                      vigueur commune est fixée au 1er mai 2027 » (F-09 : publiée le 11 sept. 2025 ;
                                      F-25 : publiée le 30 mars 2026).
                                   5) « +35 mots fictifs » → « +36 » (écart réel recompté : 3766 − 3730).
                                   6) Note [^4] : déclaration de verbatim en bloc bornée — « toute entreprise » est
                                      rapporté par le socle comme déclencheur, hors guillemets dans F-27, et n'est
                                      pas établi comme libellé officiel (même traitement qu'au ch. 11 §11.2).
                                   7) Marqueur d'inférence : PRDPlan §4.4 EXIGE que le chapitre qui invente un cas
                                      non prévu l'y ajoute au même commit — mais la consigne de cette passe interdit
                                      de modifier PRDPlan.md. Conflit de mandat : la ligne à verser est rédigée et
                                      remontée à la gouvernance, point e) ci-dessous, POUR APPLICATION PAR LE PARENT
                                      AU MÊME COMMIT. C'est la seule réserve dont le correctif sort du fichier.
                                   8) En-tête : R-7 déclaré « filtré » en bloc alors que le §13.2 est un contexte
                                      fournisseur, pas réglementaire pur — l'en-tête disait au balayage P4.2 de ne
                                      rien inspecter dans la seule section où l'inspection était due. Corrigé :
                                      §13.2 inspecté, §13.1/§13.3/§13.4 filtrés.
                                   9) Cellule « Statut du lien » d'E-23 : formulation imposée §8.2.4 (« couverture
                                      implicite via la définition de modèle ») absente de la première rencontre du
                                      lecteur avec le motif, renvoyée à la note. Reproduite dans la cellule.
                                  10) « Ce qui se transporte (…) c'est un mécanisme » : généralisation d'auteur sans
                                      marqueur au point d'usage, dans la phrase qui porte tout le transport du verdict
                                      européen vers le contexte canadien — l'opération la plus contestable du
                                      chapitre, marquée plus loin mais pas là. « Lecture de l'auteur » posée sur place.

                                   Auto-contrôle du rédacteur ayant déjà réfuté et corrigé AVANT la relecture
                                   (conservé pour mémoire) :
                                   - DÉCOMPTE FAUX (§13.1, §13.4, conclusion) : « trois entrées sur six ne produisent
                                     rien » alors que le tableau n'en portait que DEUX — l'entrée 11-348 produit un
                                     cadre. L'erreur se propageait en trois endroits et effaçait la seule contrainte
                                     du chapitre issue d'un texte AUTRE que l'art. 12.1. Même classe d'erreur que le
                                     « sept mois » du ch. 1 et le « quatre des sept » du ch. 12 : cardinal dérivé,
                                     jamais recompté contre sa source. Aligné sur DEUX / QUATRE.
                                   - « trois sources indépendantes » NON soutenable (voir bloquant a) ci-dessus).

     ═══════════════════════════════════════════════════════════════════════════════════════════════
     ARBITRAGE RENDU LE 17 JUILLET 2026 (clôture de P3 — PRDPlan §4.2, règle d'escalade de gouvernance)
     ═══════════════════════════════════════════════════════════════════════════════════════════════
     a) TRANCHÉ — RÉSOLU. L'adjectif « indépendantes » a été RETIRÉ de PRD §7.8 (F-46) le 16 juill. 2026
        (PRD v1.5), puis de l'abstract de TOC.md (v1.3). Le PRD a été corrigé EN PREMIER, comme le
        signalement l'exigeait.
        ⚠ CORRECTIF DU 17 JUILL. 2026 — LA PREMIÈRE RÉDACTION DE CET ARBITRAGE ÉTAIT FAUSSE. Elle
        certifiait : « Le §13.2 de ce chapitre est conforme au socle corrigé. » Il ne l'était pas :
        le §13.2 et la note [^9] rapportaient toujours au PRÉSENT l'adjectif rétracté et une
        « divergence interne du PRD » disparue depuis la veille. J'ai certifié une conformité sans
        aller la constater — et la faute est d'autant plus nette que ce fichier porte, trois blocs
        plus haut, la leçon exacte qui l'interdit : « un signalement de gouvernance qui cite le socle
        se re-vérifie CONTRE LE SOCLE, jamais contre le chapitre amont qui le rapporte ». Il fallait
        lire : jamais contre l'arbitrage qui le déclare résolu. Relevé par la relecture adversariale
        de la vague 2, qui a fait ce que l'arbitrage aurait dû faire : ouvrir PRD.md. §13.2 et [^9]
        réécrits au passé ; la « divergence interne » est purgée.
     b) TRANCHÉ — OPTION (i), EXÉCUTÉE LE 17 JUILL. 2026. Décision : CONDUIRE la passe de dérivation
        du §13.1. Motif : F-09 porte depuis le 16 juill. 2026 les attentes opératoires d'E-23 en niveau
        [B] ; le socle ne bloquait plus la dérivation, et le chapitre pivot sous-employait sciemment son
        socle. Le signalement lui-même désignait ce point comme celui « dont le rendement serait le plus
        élevé » de toute la Partie III. RÉSULTAT : cinq entrées E-23 ajoutées à la table (inventaire,
        cotation, cycle de vie, documentation, surveillance continue) ; table portée de SIX à ONZE
        entrées, dont NEUF produisent une contrainte et UNE SEULE (AMF) n'en produit aucune. Trois
        garde-fous posés à la rédaction : (1) les cinq dérivations sont des INFÉRENCES D'AUTEUR sur les
        conditions de possibilité d'un PROGRAMME attendu — E-23 n'attend pas une architecture et ne
        nomme pas les agents ; (2) l'objet d'E-23 est LE MODÈLE, et le texte ne dit pas ce qu'est « le
        modèle » d'un assemblage d'agents : silence exposé, non comblé ; (3) le recoupement E-23/11-348
        sur la formule OCDE est relevé mais BORNÉ — le socle ne porte de l'avis 11-348 qu'un rendu
        français, l'identité des libellés n'est PAS établie.
        VOLET AMF : NON RÉSOLU, et c'est assumé. L'extraction du texte de l'AMF (lautorite.qc.ca) reste
        hors socle (lacune §10.4) ; la revalidation du 17 juill. 2026 a de surcroît constaté que le
        domaine renvoie 403 aux outils. La table garde donc son vide, et le chapitre le dit.
     c) TRANCHÉ — ENTÉRINÉ. Les renvois F-10 et F-35 sont CONSERVÉS et inscrits au TOC v1.4. Motifs :
        F-10 est assigné à la Partie III par PRD §6, et le ch. 9 §9.4 désigne explicitement le ch. 13
        comme le lieu d'exploitation de son inférence ; F-35 n'est mobilisé que comme FORME (renvoi de
        méthode), aucun de ses faits n'étant repris. En-tête et notes [^11]/[^14] mis à jour.
     d) TRANCHÉ — RÉSOLU. PRDPlan §4.4 (v1.2) porte désormais TROIS variantes d'encadré de lacune. Le
        gabarit unique présupposait une passe de recherche et INDUISAIT SA FABRICATION. L'encadré AMF de
        ce chapitre relève du cas 2 (lacune non instruite) — à vérifier au balayage P4.2.
     e) TRANCHÉ — RÉSOLU. PRDPlan §4.4 (v1.2) fixe le libellé unique : « Lecture de l'auteur » en gras
        en prose ; « inférence d'auteur » admis en cellule de tableau. C'est exactement la répartition
        que ce chapitre pratiquait ; elle est désormais la règle et le motif que balaie CA-1 en P4.2.
     f) PARTIELLEMENT RÉSOLU — « adaptativité après déploiement » ajouté à Annexe D §D.5 le 17 juill.
        2026. La glose anglaise de F-26 et de l'art. 12.1 reste hors socle (élévation non conduite) :
        lacune §10.4, sans effet sur CA-5 (aucun des deux n'est un terme du glossaire à gloser).
     g) TRANCHÉ — traité en P4.3 (méthode de décompte normalisée à l'échelle de l'ouvrage).
     ═══════════════════════════════════════════════════════════════════════════════════════════════

     POINTS DE GOUVERNANCE SIGNALÉS AU PARENT (état du 16 juill. 2026, conservés pour la traçabilité
     de l'arbitrage ci-dessus — PRD/TOC/PRDPlan/glossaire n'avaient PAS été modifiés par la rédaction) :
     a) [BLOQUANT ÉDITORIAL — reformulé après relecture] « Convergence à trois sources INDÉPENDANTES » :
        **PRD §7.8 (F-46) écrit « convergence à trois sources indépendantes »**, en gras (PRD.md L180) ;
        l'abstract de TOC.md reprend l'adjectif ; seules l'Annexe B.1 (L310) et le §6 (L93) l'omettent.
        L'adjectif est réfuté par PRD §7.7 lui-même : cosignature Rinderle-Ma (F-36 et F-37) ; IBM Research
        parmi les 18 auteurs de F-36, IBM éditeur de F-46. Les deux recoupements se lisent dans le socle.
        À CORRIGER EN PRIORITÉ DANS **PRD §7.8 (F-46)** (version++) — le PRD est la seule autorité factuelle
        et prime en cas de conflit, et les ch. 19 et 22 le liront ensuite —, PUIS dans l'abstract de TOC.md.
        Corriger TOC seul laisserait l'affirmation réfutée dans le document qui fait autorité.
        Le ch. 5 avait signalé le premier recoupement et demandé l'arbitrage AVANT le ch. 13 ; il n'a pas eu
        lieu. Le présent chapitre cite la formule du socle telle quelle (§13.2, note [^9]), expose la
        non-indépendance et requalifie l'argument.
     b) [SOCLE INSUFFISANT — structurel ; MOITIÉ RÉSOLUE, RELANCÉ AUTREMENT PAR LA PASSE 6]
        TOC.md intitule §13.1 « Table de traduction exigences → frames ».
        VOLET E-23 : l'option (i) A ÉTÉ EXÉCUTÉE le 16 juill. 2026 — F-09 porte désormais le libellé de la
        définition et les attentes opératoires (cycle de vie, inventaire, cotation, documentation et
        Appendice 1, surveillance) en niveau [B]. Le socle ne bloque plus la dérivation ; c'est CE CHAPITRE
        qui ne l'a pas conduite, la passe 6 étant à périmètre strictement correctif. Le signalement change
        donc de nature : il ne demande plus d'élever le socle mais d'ARBITRER une passe de rédaction du
        §13.1 (traduire les attentes d'E-23 en cadres), sans quoi le chapitre pivot sous-emploie son socle.
        VOLET AMF : inchangé — F-25 ne porte que le calendrier de la ligne directrice (lacune §10.4).
        Le chapitre pivot de l'ouvrage produit donc l'essentiel de ses contraintes à partir d'un seul texte
        (art. 12.1, F-27) — et la relecture a montré que c'est aussi le seul dont il puisse tirer un fait
        négatif (bloquant c). Deux options : (i) élever le socle — extraction primaire d'E-23 (osfi-bsif.gc.ca)
        et de la ligne directrice finale de l'AMF (lautorite.qc.ca) —, ce qui renforcerait aussi les ch. 9,
        11, 19, 20 et 23 ; (ii) entériner le périmètre réduit et réviser l'intitulé du §13.1 au TOC. C'est,
        de tous les signalements accumulés en Partie III, celui dont le rendement serait le plus élevé.
     c) [PÉRIMÈTRE TOC] **F-10 employé en renvoi** (§13.1, note [^11] — indéterminabilité causale, pivot du
        raisonnement sur le lieu de production de la trace) et **F-35 en renvoi de méthode** (note [^14] —
        forme du fait négatif vérifié, ajoutée en correctif du bloquant b), alors que TOC.md n'assigne au
        ch. 13 que F-09, F-25, F-26, F-27, F-36, F-37 et F-46. Le ch. 9 §9.4 désigne pourtant explicitement
        ce chapitre comme le lieu d'exploitation de l'inférence F-10 (« le chapitre 13 en fait le pivot de
        l'ouvrage »), et PRD §6 (Partie III) assigne F-10 à la partie. F-35 n'est mobilisé que comme FORME
        (aucun fait du cadre bancaire repris ; traitement au ch. 17). Même arbitrage que les points d) et e)
        de la gouvernance du ch. 9 : entériner les renvois dans TOC, ou les retirer — auquel cas le §13.1
        perd un des trois termes de sa conjonction et l'encadré du §13.2 perd son contraste de méthode.
     d) [FORME §4.4 — non tranchée depuis le ch. 12] Le membre imposé « Recherche menée le [date] » des deux
        encadrés est renseigné honnêtement : aucune passe primaire dédiée n'a été conduite pour ce chapitre
        (hors périmètre P0). Si la forme §4.4 présuppose une passe par lacune déclarée, P0 doit être étendu.
        Point ouvert depuis le ch. 9 (gouvernance g), non tranché.
     e) [MARQUEUR D'INFÉRENCE — CONFLIT DE MANDAT, à trancher au commit de ce chapitre] Deux libellés
        coexistent et sont tous deux employés ici : « Lecture de l'auteur » (9 occurrences ; convention de
        fait des ch. 1 à 12, retenue en prose) et « inférence d'auteur » (8 occurrences ; forme du PRD et de
        PRDPlan §4.4, retenue dans la colonne « Statut du lien » du tableau §13.1, où la prose ne se prête pas
        au marqueur long). PRDPlan §4.4 n'enregistre pas le premier.
        La relecture (réserve 7) établit que §4.4 donne au ch. 13 le MANDAT de solder lui-même cette dette :
        « Un chapitre qui a besoin d'une formulation nouvelle pour un cas non prévu **l'ajoute ici au même
        commit** » — et le ch. 13 invente bien le cas non prévu (traduction exigence réglementaire →
        contrainte d'architecture, opération centrale du chapitre pivot). La consigne de la présente passe
        interdit toutefois de modifier PRDPlan.md. Ligne rédigée, À VERSER PAR LE PARENT DANS PRDPlan §4.4
        AU MÊME COMMIT QUE CE CHAPITRE :
          | Exigence réglementaire → contrainte d'architecture | « **Lecture de l'auteur** : [conclusion].
            Le socle établit [prémisses] ; il n'établit pas [la conclusion]. » — forme longue en prose ;
            « **Inférence d'auteur** » admis en cellule de tableau, où la prose ne se prête pas au marqueur
            long. |
        Troisième escalade sans arbitrage (ch. 9, ch. 12, ch. 13) : sans elle, CA-1/CA-2 n'ont pas de motif
        unique à balayer en P4.2, et les ch. 14-24 reprendront l'ambiguïté.
     f) [GLOSSAIRE — enrichissement à verser par le parent, PRDPlan P1.5] Le ch. 13 n'introduit aucun terme
        nouveau : tous ses termes sont déjà fixés en Annexe D (§D.2 pour framed autonomy, frames normatif et
        opérationnel, adaptation/évolution, écart de responsabilité, OO1-OO4, humain-dans-la-boucle ; §D.5 pour
        risque de modèle et la formule de l'art. 12.1 ; §D.6 pour les workflows statiques). Rappel du
        signalement du ch. 12 : « adaptativité après déploiement » (F-26) n'a toujours pas d'entrée en §D.5,
        alors que le présent chapitre en fait l'une de ses six lignes de traduction. Ajout issu de la relecture
        (réserve 1) : le socle ne porte AUCUN libellé anglais pour F-26 (avis 11-348) ni pour l'art. 12.1
        (F-27, texte français). Si le glossaire ou CA-5 attendent une glose anglaise pour ces formules, elle
        exige une élévation par consultation primaire (osc.ca ; version anglaise de P-39.1 sur LégisQuébec) —
        elle ne peut pas être rendue par l'auteur.
     g) [MÉTHODE DE DÉCOMPTE] PRDPlan §4.2 ne fixe aucune commande de décompte de volumétrie. Point soulevé
        par le ch. 6, rendu bloquant par le ch. 13 (premier chapitre à tableau) et confirmé par la relecture :
        les deux relecteurs ont reproduit B et C à l'unité près UNIQUEMENT parce que le chapitre publie ses
        commandes. Les ch. 18 et 23 sont des chapitres de tableaux : fixer B comme commande de référence, ou
        arbitrer autrement, AVANT P3.
-->
