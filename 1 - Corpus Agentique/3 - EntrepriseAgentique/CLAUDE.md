# CLAUDE.md — volume III (L'entreprise agentique)

Guide pour Claude Code (claude.ai/code) **dans ce dossier**.

## Périmètre de ce fichier

Ce `CLAUDE.md` ne régit que le **volume III**, sous `1 - Corpus Agentique/3 - EntrepriseAgentique/`. Il ne dit rien des autres livrables du dépôt *Monographies* :

| Ce que vous cherchez | Où |
|---|---|
| Place du volume III dans le corpus, ordre de lecture, divergences entre volumes | [README du dépôt](../../README.md) |
| Conventions communes et conventions de la veille technologique (racine) | [`CLAUDE.md` du dépôt](../../CLAUDE.md) |
| Volume I — *Interopérabilité agentique* (cadre mondial), **dont ce volume hérite 17 entrées** | [`1 - InteroperabiliteAgentique/CLAUDE.md`](../1%20-%20InteroperabiliteAgentique/CLAUDE.md) |
| Volume II — *L'autonomie encadrée* (cas canadien), **dont ce volume hérite 16 entrées et l'appareil de méthode** | [`2 - OrchestrationAgentique/CLAUDE.md`](../2%20-%20OrchestrationAgentique/CLAUDE.md) |

⚠ **Les conventions divergent entre volumes** — et celles de ce volume divergent aussi de celles du Vol. II dont il prolonge pourtant l'appareil. Les écarts délibérés sont listés plus bas ; **les vérifier avant d'appliquer une règle de mémoire**.

## Nature du volume

Projet documentaire, **en cours de rédaction**. Livrable visé : une monographie exhaustive — « L'entreprise agentique : identité non humaine, délégation vérifiable, maillage d'agents et AgentOps » — sur ce qu'une entreprise doit tenir pour que des agents y opèrent sous mandat vérifiable. Objet choisi parce que les Vol. I et II le désignent l'un et l'autre comme leur verrou résiduel : « identité non humaine et délégation multi-saut » (Vol. I, `Synthese Monographie.md` §11.6) et les questions Q2, Q3, Q5 du Vol. II (ch. 21 §21.2).

**Le dossier contient la gouvernance dans `doc/`, l'arborescence de rédaction dans `monographie/`, et les rapports dans `verification/`.** ⚠ **21 des 34 pièces portent un corps** — les ch. 1 à 21 (Parties I à VI), tous au statut **« Rédigé et relu adversarialement »**, relus par un relecteur distinct du rédacteur (CA-14) **et corrigés** ; constat sur disque le 21 juillet 2026, statut lu dans l'en-tête de chacune. ⚠ **Les 13 autres demeurent des gabarits** — avant-propos, ch. 22 à 28, annexes A à E : en-tête à cinq champs et thèse citée du TOC, **zéro ligne de corps**. Un gabarit n'est ni un brouillon ni une ébauche. Aucun pipeline de rendu, aucune source déposée.

Documents de gouvernance, par ordre d'autorité :

1. [PRD.md](doc/PRD.md) **v1.1** — contenu, héritage du socle, garde-fous, critères d'acceptation (**prime en cas de conflit**, y compris sur le TOC). La v1.1 ouvre le **§7.10**, siège des versements de socle faits *pendant* la rédaction ;
2. [TOC.md](doc/TOC.md) **v0.6** — **autorité sur le découpage** : toute modification du nombre ou de l'ordre des chapitres passe par lui (version++), et se répercute au PRD. Il porte en outre, depuis la v0.5, la **table de couverture** (§6.2 ↔ TOC) et la **table d'assignation** des garde-fous et des lacunes ;
3. [PRDPlan.md](doc/PRDPlan.md) **v0.4** — plan d'exécution (phases P0 à P5, boucle qualité §5.2, formulations imposées §5.5). Il **ordonnance** le PRD, il ne le redéfinit pas.

⚠ **Emplacement `doc/` : tranché sur disque le 18 juillet 2026, amendé au plan le 21.** L'activité **P0.3** est close, le §1.3 du PRDPlan est réécrit, et **les deux renvois relatifs qu'il portait à faux sont corrigés** — dont celui du **gabarit §5.4**, qui aurait produit mécaniquement 34 renvois cassés une fois recopié dans les pièces. Chemin correct vers le TOC : `../doc/TOC.md` depuis `monographie/`, `../../doc/TOC.md` depuis un dossier de partie ou `90-annexes/`.

## La règle cardinale ne bloque plus — et c'est le moment où elle protège le moins

**Règle cardinale (PRD §7.0)** — *aucun chapitre n'est rédigé avant la clôture du lot d'instruction dont il dépend.* Un chapitre écrit sur un socle vide n'est pas un chapitre en avance : c'est une inférence longue, et le volume qui prend l'identité pour objet ne peut pas se permettre d'en produire.

Etat du socle au 21 juillet 2026 : **89 entrées propres re-mesurées** (F-01 à F-89, dont onze versées en cours de rédaction au **PRD §7.10**), 33 entrées héritées (H-01 à H-33), **14 lots clos sur 15** et **L-14 partiellement clos**. **21 pièces sur 34 sont rédigées** ; le **ch. 26 demeure interdit d'écriture** par §7.0, L-14 n'ayant pas instruit les métriques d'observabilité.

⚠ **Ce qui demeure après la levée de la règle cardinale, ce sont les dépendances éditoriales** du PRDPlan §5.1, et elles ne se déduisent pas du socle : le **ch. 4** ouvre l'ouvrage et conditionne toute application de la grille ; le **ch. 8 se rédige après le ch. 9**, en travers des parties ; les **six chapitres de composition** attendent leurs chapitres amont et sont **plus** exposés qu'un chapitre de socle, pas moins. *Un socle constitué autorise la rédaction ; il ne la planifie pas.* ☑ **Les dépendances du tronc sont consommées** — ch. 4, ch. 8 et ch. 9 sont rédigés ; celles qui demeurent portent sur les **trois chapitres de composition restants** (ch. 25, 27, 28), tous en P4.

⚠ **Trois choses ne sont pas des passes d'instruction, et il ne faut pas les compter comme telles** : la clôture de **L-15** (vérification d'absence aboutie), la **revalidation d'ouverture** des faits chauds ([`revalidation-2026-07-21.md`](verification/revalidation-2026-07-21.md)) et les **contrôles de bornage** de P2. Aucune ne crée d'entrée F-xx. ⚠ **Et la revalidation d'ouverture s'est trompée deux fois**, corrigée depuis par les sources primaires des lots L-05 et L-14 (PRD §8.3) : *une revalidation constate l'état d'une source à une date, et si elle le fait sur du secondaire, elle se trompe comme du secondaire.*

**Les décisions d'auteur de la phase P0 sont prises (21 juillet 2026).** L'état antérieur — deux décisions bloquantes en attente — est clos :

| # | Décision | Issue retenue |
|---|---|---|
| **P0.2** | **Corpus d'appui** — déposer les trois ouvrages annoncés, ou retirer la filiation livresque | ☑ **Filiation retirée.** Le rejeu de la vérification (21 juill. 2026) confirme que les trois ouvrages n'ont jamais été déposés, jusque dans l'historique git. **L-15 clos par échec documenté** ; les sept sections et l'annexe E bloquées (§4.4, §9.4, §25.1, §25.5, §27.4, §27.5, §28.4, annexe E) sont **réaffectées au socle** — table de réaffectation au TOC. ⚠ **Réversible** : un dépôt ultérieur rouvre L-15 |
| **P0.1** | Révision du TOC sur les **neuf écarts** constatés (PRD §7.4) | ☑ **Les neuf corrigés au TOC v0.5**, chacun revérifié sur pièce avant correction. **Un dixième écart trouvé à l'exécution**, siégeant dans le PRD : §7.4.6 nommait le dépôt `Monographies` — il s'appelle **`Agentique`** (§7.4.10) |
| **P0.3** | Emplacement des documents de gouvernance | ☑ `doc/`, tranchée le 18 juillet 2026, **amendée au plan le 21** |

⚠ **Le risque a changé de nature, il n'a pas disparu.** Sept sections et une annexe privées de leur cadre conceptuel externe, ce sont huit endroits où la tentation devient de **combler par la construction d'auteur** — faute symétrique de celle qu'on corrige, et d'un coût comparable. La parade est **CA-07 sans indulgence** : « Lecture de l'auteur » en tête d'énoncé, suivi de ce que le socle établit *et* de ce qu'il n'établit pas. **Ne jamais rédiger l'une de ces sept sections et l'annexe E « de mémoire », ni sur un gabarit emprunté sans source.** ☑ **Deux des huit endroits sont franchis** — §4.4 et §9.4 vivent dans des chapitres rédigés ; **six demeurent** (§25.1, §25.5, §27.4, §27.5, §28.4, annexe E), tous en P4, et l'avertissement vaut entier pour eux.

## Ce que l'exécution de P3 a appris — quatre choses qu'aucun document amont ne dit

La rédaction des 21 chapitres du tronc a produit des constats que le cadrage ne portait pas. Ils valent pour ce qui reste à écrire, pas seulement pour ce qui est fait.

- **L'étape 6 de la boucle qualité — appliquer les correctifs — se tient à l'intérieur du pipeline de rédaction, jamais après.** Différée une fois, elle a laissé quatre chapitres au dépôt avec **quatorze réfutations bloquantes** non traitées, et il a fallu une passe entière pour les reprendre. *Une pièce relue et non corrigée est plus proche d'un brouillon que d'un chapitre* : le statut « Rédigé et relu adversarialement » ne se pose qu'**après** application, et l'écrire avant est un statut qui ment.
- **Le défaut dominant est la borne perdue, et c'est un défaut de niveau d'écriture, pas de phase.** Il se produit au **socle** (une clause d'exclusivité qu'aucune source ne porte), à la **synthèse** (un degré qui monte d'un cran entre le rapport de lot et l'entrée F-xx) et dans la **prose** (un nom de produit, un statut pré-normatif, un niveau [A]/[B]/[C] ou un tri prospectif qui tombe). Il se surveille **à chaque passe** ; aucune passe ne le corrige une fois pour toutes.
- **La volumétrie réelle dépasse la cible de +37,4 % sur le périmètre rédigé, et l'écart ne se corrige pas par amputation.** Il vient des **bornes rétablies**, non d'un ajout de matière : plusieurs pièces ont grossi **après** leurs correctifs, pas avant. La cible du TOC était calibrée sur une prose moins bornée que celle que les garde-fous imposent. *Couper davantage supprimerait des bornes ; l'écart se documente au registre de gel.*
- **Le socle se complète pendant la rédaction — c'est l'objet du PRD §7.10.** Une pièce qui a besoin d'une affirmation retenue par un lot mais **non versée** la fait **verser au socle** ; elle ne la cite ni depuis le rapport de lot, ni dans la pièce seule (R-G-05, R-G-06). Un versement est un acte de socle, non de recherche : il ne rouvre aucun lot.

⚠ **Les remontées ouvertes par la rédaction ne vivent pas toutes au registre.** Plusieurs pièces en portent aux **Notes** de leur propre fichier — bornes et niveaux d'entrées du socle, versements demandés, lignes de registre de gel à renseigner. Avant de reprendre une pièce, **lire ses Notes**, pas seulement [`verification/remontees-gouvernance.md`](verification/remontees-gouvernance.md).

## PRD.md fait autorité

Toute contribution s'y conforme. Les points qu'un agent ne peut pas déduire du texte et se trompera à supposer :

- **Socle (§7)** — deux régimes d'héritage, **et il ne faut pas les confondre**. Une entrée du Vol. II **conserve son niveau** [A]/[B]/[C] avec sa provenance F-xx (méthode identique, rien à re-subir). Une entrée du Vol. I **entre en [C]** — non par défiance, mais parce que la vérification du Vol. I porte sur les *références* (existence, auteurs, année) et non sur le *contenu des affirmations*. Trois des seize entrées du Vol. II (H-13, H-15, H-16) ne viennent pas de son socle factuel : elles entrent comme garde-fou ou thèse attribuée, **jamais comme faits**.
- **Deux instruments épistémiques orthogonaux** — les niveaux [A]/[B]/[C] (Vol. II : ce que l'affirmation a subi) et le tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF (Vol. I : ce que l'énoncé prétend sur le futur). Un fait peut être [B] **et** PROJETÉ. L'ouvrage emploie les deux, **jamais l'un pour l'autre** (CA-11).
- **Garde-fous (§8.1, R-01 à R-14)** — quatorze formulations proscrites. Les trois qui se violent sans y penser : **R-01** (le passeport d'agent n'existe dans aucune spécification — c'est une construction de l'ouvrage) ; **R-02**, convention cardinale (un mécanisme cryptographique est qualifié par ce que sa spécification **démontre**, jamais par ce qu'elle **promet**) ; **R-03** (« entreprise agentique », « maillage d'agents », « AgentOps » sont des termes de marché sans définition normative, chacun défini à un **siège unique**).
- **Attribution (§8.2)** — toute métrique auto-déclarée est attribuée à sa source **à chaque occurrence, sans exception d'usage illustratif**. *Un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait.*
- **Trois degrés d'absence (§8.6)** — fait négatif **VÉRIFIÉ** (balayage documenté d'un texte) > fait négatif **ÉTABLI** (réserve explicite du socle, sans balayage) > **absence de documentation** (le socle est muet). Jamais « le socle ne documente pas X, donc X n'existe pas » (R-14).
- **Marquage d'inférence (CA-07)** — toute construction d'auteur porte **« Lecture de l'auteur »** en tête d'énoncé. Le ch. 8, le ch. 26 et le §27.4 sont des constructions d'auteur **en totalité** : marquage à l'ouverture de la pièce, pas seulement au paragraphe.
- **Neutralité fournisseur (§8.4)** — Entra Agent ID, passerelles MCP, offres de maillage : cas d'instanciation documentés, jamais recommandations. **Annonce, GA, feuille de route, préversion : quatre choses différentes.**
- **Dualité d'usage (§8.5, R-12)** — la Partie IV décrit la mécanique des attaques au niveau architectural, cite les identifiants, **n'en reproduit aucun**. ⚠ **R-12 est le seul garde-fou sans motif de balayage** : aucun `grep` ne détecte une recette d'exploitation. Il est contrôlé par **CA-12 seul**, une relecture dédiée et distincte de la relecture de conformité. Un balayage §A.6 « vert » ne dit rien de R-12. ☑ **Une passe CA-12 a eu lieu le 21 juillet 2026** — [`verification/relecture-CA-12-P3.md`](verification/relecture-CA-12-P3.md) : **un retrait** (ch. 15 §15.3, attestation auto-délivrée), zéro charge utile trouvée. ⚠ **Elle déclare elle-même son périmètre incomplet** : 26 pièces **balayées mais non relues**, et **douze rapports de lot sur quatorze jamais relus** au titre de R-12 — dont L-09 et L-10, qui portent la matière des ch. 13 et 15. *Un balayage n'est pas une relecture*, et ce compte rendu est la trace d'un contrôle, non un certificat.

## Pièges de renvoi propres à ce volume

CA-10 les impose, et ils viennent des neuf écarts de PRD §7.4 — tous constatés sur pièce, **et tous corrigés au TOC v0.5 le 21 juillet 2026**. ⚠ **La correction du TOC ne les rend pas caducs** : ce sont des pièges du *corpus source*, pas des coquilles du TOC. Ils se reposent à chaque nouveau renvoi rédigé.

- **Tout renvoi au Vol. I nomme son fichier.** Le Vol. I porte **trois numérotations concurrentes** : `Synthese Monographie.md` §1 à §12 (titres de niveau 2), les chapitres de `Monographie.md`, et l'Annexe B qui numérote §0 à §17. **§3 à §7 existent dans les deux fichiers** — un pointeur « §7.4 » non qualifié est ambigu.
- **Tout renvoi à une question du Vol. II nomme son chapitre.** Le ch. 21 §21.2 porte **Q1 à Q6** ; le ch. 16 §16.3 porte un jeu **Q1 à Q5 entièrement distinct**, sans recouvrement. Les cinq étiquettes désignent **deux objets chacune**, et le Vol. II ne signale nulle part cette homonymie.
- **Tout renvoi à un garde-fou nomme son volume.** Ici **R-01 à R-14** (deux chiffres) ; au Vol. II, **R-1 à R-8** (un chiffre). « R-01 » et « R-1 » ne sont pas le même objet.
- **La formule de non-compositionnalité de la sûreté** vit à **quatre endroits du Vol. I sous trois formes** (`Synthese` §5.10 — le siège déclaré —, `Synthese` §6.12, `Synthese` §11.3, `Monographie.md` §3.10.1). Citer en nommant fichier et section, et ne revendiquer le verbatim que sur une seule, mot pour mot (CA-05).
- **Le sigle « ACP » employé seul est proscrit** (R-04) : **six emplois distincts** recensés, dont la composante ACP d'AGNTCY que le socle ne caractérise pas — et qu'il ne faut donc jamais agréger à l'ACP protocolaire d'IBM Research.

## Divergences volontaires avec le Vol. II — à ne pas uniformiser

Ce volume prolonge l'appareil du Vol. II mais s'en écarte sur quatre points, chacun pour un motif consigné. Les « corriger pour la cohérence » ferait régresser le volume.

| | Vol. II | Vol. III | Motif |
|---|---|---|---|
| **Motifs de balayage** | PRDPlan §4.3 | **PRD, Annexe A §A.6** | Ils sont l'instrument déclaré de CA-02 ; un critère et son outil de contrôle ne se séparent pas |
| **Commande de décompte** | locale `C` — sous-compte de **1,3 %**, assumé | **`LC_ALL=C.UTF-8`** (PRDPlan §1.5) | Le Vol. II ne pouvait plus corriger sans invalider tous ses chiffres publiés ; le Vol. III n'en a aucun, le coût est nul |
| **Règle d'escalade de gouvernance** | apprise en P2 | **posée avant la première rédaction** (PRDPlan §5.3) | Au Vol. II, un chapitre pivot a dû trancher seul une remontée que personne n'avait arbitrée |
| **Numérotation des garde-fous** | R-1 à R-8 | R-01 à R-14 | Voir ci-dessus |

**L'emplacement des documents de gouvernance n'est plus une divergence** : les deux volumes tiennent leur gouvernance dans `doc/`. La différence est de **date** — le Vol. II a déplacé après vingt-neuf pièces rédigées et porte 48 renvois cassés ; le Vol. III a déplacé avant la première, au prix de deux renvois (ci-dessous).

⚠ **Corollaire du décompte** : les volumétries du Vol. II et du Vol. III **ne sont pas comparables** sans re-mesure par une commande unique. Toute comparaison inter-volumes commence par une re-mesure.

⚠ **Il n'existe aucun pipeline de rendu dans ce dossier.** Celui du Vol. II est une copie de celui du Vol. I, et les deux évoluent séparément. **Un troisième serait une troisième copie** — le savoir avant de le créer (PRDPlan §7, P5.4).

### Séquelles du déplacement vers `doc/` — ☑ les deux renvois sont corrigés

Le déplacement du 18 juillet 2026 avait cassé deux liens, tous deux dans `doc/PRDPlan.md`. **Corrigés le 21 juillet 2026 (P0.3)**, et consignés ici parce que le second a failli coûter cher :

| Fichier | Renvoi qui était cassé | Cible corrigée |
|---|---|---|
| `doc/PRDPlan.md` §1 (en-tête) | `](../../CLAUDE.md)` — visait la racine du dépôt, résolvait dans `1 - Corpus Agentique/` | ☑ `../../../CLAUDE.md` |
| `doc/PRDPlan.md` §5.4 (**gabarit de pièce**) | `](../../TOC.md)` — relatif à un futur chapitre sous `monographie/<partie>/` | ☑ `../../doc/TOC.md` |

⚠ **Le second était le plus coûteux des deux, et de loin** : il vivait dans le **gabarit** que les 34 pièces recopient. Non corrigé, il produisait mécaniquement 34 renvois cassés — reproduction exacte du gisement du Vol. II. **Il a été corrigé avant la génération des gabarits** : contrôle exécuté le 21 juillet 2026 sur `monographie/`, **40 liens relatifs, 40 résolus**.

**Leçon à conserver, la correction ne la périme pas** : le chemin relatif vers le TOC **dépend de la profondeur du fichier** — `../doc/TOC.md` depuis `monographie/`, `../../doc/TOC.md` depuis un dossier de partie ou `90-annexes/`. Le vérifier **à la création de chaque pièce, en l'ouvrant**, jamais à la fin et jamais de mémoire.

Le PRDPlan §1.3 et son activité **P0.3** sont amendés : ils décrivent l'arborescence réelle.

## Divergences non arbitrées — signalées, jamais tranchées

Deux faits datés divergent entre les livrables du dépôt. Le CLAUDE.md racine impose de les signaler sans les uniformiser ; ce volume les **porte** (PRD §7.5, qui en est la source de vérité pour la durée de rédaction) :

- **Gouvernance d'AP2** — Vol. I et veille : transfert à la FIDO Alliance le 28 avril 2026, donné pour fait établi. Vol. II (gel postérieur) : aucun transfert documenté, position tenue en quatre endroits concordants et rangée parmi les **ignorances déclarées**. → ch. 9, lot L-06. **L'arbitrage par chronologie est interdit** : le volume le plus récent est ici le plus réservé.
- **Date de la ligne directrice IA de l'AMF** — Vol. II : 30 mars 2026 (avec dette de vérification déclarée). Veille : 7 avril 2026. → ch. 19. L'entrée en vigueur au 1er mai 2027 est, elle, concordante.

⚠ Le fichier prévu pour porter ces divergences — `commun/faits-partages.md` — **n'existe pas** et n'est pas créé par ce volume (décision, PRD §7.5). ☑ **Les trois renvois du TOC sont repointés vers §7.5 le 21 juillet 2026** (P0.7). ⚠ Les renvois du **README racine** et du **TOC du Vol. IV** demeurent : **hors périmètre de ce volume, signalés et non corrigés** — on ne corrige pas le renvoi d'un livrable dont on n'a pas la charge éditoriale.

## Sensibilité temporelle

Le domaine se périme par trimestres, et ce volume hérite de **deux gels distincts** : juin 2026 (Vol. I) et 16-17 juillet 2026 (Vol. II). **Un volume date de son gel, pas de sa lecture.** Toute entrée héritée portant un fait chaud (PRD §8.3, sept lignes) est **revalidée à la source primaire** avant d'entrer dans un chapitre, quel que soit son niveau d'origine.

☑ **Revalidation d'ouverture exécutée le 21 juillet 2026** — [`verification/revalidation-2026-07-21.md`](verification/revalidation-2026-07-21.md), les sept lignes de PRD §8.3 sans exception. **Trois résultats à connaître avant d'écrire quoi que ce soit** :

- **Révision MCP** — la **substance** annoncée est confirmée **au brouillon** (retrait de `Mcp-Session-Id`, protocole sans état), la **date du 28 juillet 2026 ne l'est pas** à la source. Les ch. 2 et 22 écrivent « annoncé au brouillon », **jamais** « publié le 28 juillet 2026 » (R-09).
- **Brouillon CSA — ÉVOLUÉ** : mis à jour le 20 mai 2026, alors que le socle hérité en reste au 27 mars. **H-03 s'amende au socle** — jamais dans la pièce seule — et **L-05 réinstruit avant le ch. 7**.
- **Conventions OpenTelemetry — ÉVOLUÉ** : déplacées dans un dépôt dédié, statut **Development**, premier échelon d'une échelle qui en compte trois (*Development → Release Candidate → Stable*). L'alternative « expérimental / stable » du PRD était mal calibrée ; elle est corrigée.

⚠ **Ce rapport se périme, et il ne dispense de rien** : il n'a créé aucune entrée de socle, clos aucun lot, arbitré aucune divergence. La revalidation finale P5.1 reprend les sept lignes. ⚠ **Deux de ses trois résultats ont été repris depuis** : la datation du brouillon CSA est tranchée en **R-G-10** (H-03 et F-41 datent différemment le même brouillon, et les deux énoncés sont exacts), et le **ch. 7 est rédigé**. Le rapport demeure la trace de l'état des sources au 21 juillet 2026, pas un état courant.

Chaque pièce porte sa propre date de gel, consignée au registre [`monographie/99-registre-gel.md`](monographie/99-registre-gel.md) — **au même commit que la pièce** (CA-04). **Les 21 pièces rédigées portent une date de gel dans leur en-tête** — 21 juillet 2026, constaté champ par champ ; les 13 gabarits n'en portent aucune et n'en porteront qu'à leur rédaction.

⚠ **Le report au registre est un geste distinct de la pose du champ, et c'est là qu'il se perd.** Plusieurs pièces rédigées déclarent en toutes lettres, dans leur propre en-tête ou leurs Notes, que le report reste à faire — un rédacteur qui n'édite que sa pièce ne renseigne pas le registre. **Avant de se fier à une ligne du registre, l'ouvrir et la comparer à l'en-tête de la pièce** : le registre est la source de vérité déclarée, ce qui ne le rend pas automatiquement à jour.

## Conventions

- **Langue** : français canadien soutenu ; terminologie technique anglaise entre parenthèses et en italique à la première occurrence ; citations verbatim en langue originale (CA-08).
- **Commits** : messages en anglais, format Conventional Commits — convention du Vol. II, retenue ici parce que ce volume prolonge son appareil (`docs(prd): …`, `docs(mono): draft chapter N — <slug anglais court>`), sujet ≤ 50 caractères quand possible (plafond 72), mode impératif. ⚠ Le Vol. I emploie des messages courts **en français** : vérifier le dossier de travail avant de rédiger le message.
- **Chirurgie** : ne modifier que les sections concernées. **Ne jamais renuméroter** les identifiants existants — H-xx (héritées), F-xx (socle propre), R-xx (garde-fous), L-xx (lots), CA-xx (critères) : ils sont cités en références croisées, ici et dans le compendium du Vol. IV que son TOC annonce déjà.
- **Versionnage** : incrémenter la version du PRD à chaque enrichissement substantiel, et la table des jalons (§12) avec. Le TOC se versionne à toute modification du découpage.
- **Décomptes** : tout chiffre publié est **re-mesuré**, jamais recopié d'un autre document. Un même chiffre vit à plusieurs endroits — PRD, TOC, README du volume, README du dépôt : **les mettre à jour ensemble, jamais l'un sans les autres**. Commande de référence : PRDPlan §1.5, seule autorité de décompte du volume.
- **Attestations** : « conforme », « vérifié », « résolu » s'écrivent depuis une **constatation sur pièce**, jamais depuis un document amont qui le déclare ni depuis le souvenir de l'avoir fait (CA-14).

## État du projet (21 juillet 2026)

**Tronc rédigé — Parties I à VI ; Parties VII à IX, avant-propos et annexes au gabarit.** Trois documents de gouvernance : **TOC v0.6, PRD v1.1, PRDPlan v0.4** — versions lues dans les en-têtes des trois fichiers le 21 juillet 2026. S'y ajoutent l'arborescence `monographie/` (34 pièces + registre de gel) et `verification/` (**20 fichiers**, recomptés sur le répertoire le 21 juillet 2026 : 14 rapports de lot, **4 rapports de relecture** — P1, P3 Partie I, P3, CA-12 P3 —, un rapport de revalidation, le registre des remontées).

⚠ **Ce que P3 n'a pas fait, et qu'aucune de ses sorties ne doit laisser croire.** Les **13 pièces restantes** ne sont pas commencées — c'est P4. **Douze remontées ont été tranchées par ARBITRAGE DÉLÉGUÉ** — elles relevaient de l'auteur sans exception, et sont **révocables** : avant de rédiger contre une thèse ou un intitulé du TOC, **lire l'arbitrage qui l'a fixé** au [registre](verification/remontees-gouvernance.md), l'option écartée y étant conservée. ⚠ **Le plan n'avait désigné aucune instance capable de trancher cette classe de remontées** : la phase ne pouvait pas se clore par sa propre mécanique, et cette lacune se posera à l'identique en J-5. Le **ch. 26 reste interdit d'écriture** par PRD §7.0. Aucun lot n'a été rouvert, aucune divergence arbitrée. *Un tronc rédigé n'est pas un ouvrage achevé.*

| | État |
|---|---|
| Pièces rédigées | **21 sur 34** — ch. 1 à 21 (Parties I à VI), au statut **« Rédigé et relu adversarialement »** : relus par un relecteur distinct du rédacteur (CA-14) **et corrigés**, l'étape 6 de la boucle qualité tenue dans le pipeline. **13 au gabarit** : avant-propos, ch. 22 à 28, annexes A à E |
| Volumétrie | **86 579 mots réels** sur les 21 pièces, pour **63 000** de cible cumulée — **+37,4 %**. Re-mesure du 21 juillet 2026 par la commande de PRDPlan §1.5, exécutée sur les **21 pièces** et non sur un échantillon. Par partie : I +25,1 %, II +52,7 %, III +35,7 %, IV +41,2 %, V +44,8 %, VI +22,5 %. ⚠ **L'écart vient des bornes rétablies, pas d'un ajout de matière : il se documente, il ne s'ampute pas** |
| Volumétrie cible | **102 500 mots** pour les 34 pièces — **concordante** entre TOC et PRD §6.1 ; **indicative et non normative**. ⚠ Le README du dépôt porte encore « ≈ 100 000 » : réalignement en **P5.3**, avec les autres porteurs |
| Socle propre | **89 entrées re-mesurées** — F-01 à F-26 (P1, §7.8), F-27 à F-78 (P2, §7.9), **F-79 à F-89 (P3, §7.10)**. **180 affirmations instruites, 80 soumises au vote, 17 écartées** ; **53 corrections de bornage** ; **106 échecs de source consignés**. Le socle porte aussi deux corrections de P3 : **F-36 rétrogradée [B] → [C]** par la règle de composition, **renvoi de F-30 corrigé** vers F-50 |
| Socle hérité | **33 entrées** — H-01 à H-16 (Vol. II), H-17 à H-33 (Vol. I) — **inchangé** |
| Lots d'instruction | **14 clos sur 15**, plus **L-14 partiellement clos** — treize par instruction aboutie, **L-15** par échec documenté. ⚠ **L-14 n'a pas instruit les métriques du ch. 26** : ce chapitre reste interdit d'écriture par §7.0. **P3 n'a rouvert aucun lot** — les onze entrées de §7.10 sont versées depuis les rapports **clos** de L-01, L-02 et L-12 |
| Jalons | **J-0 à J-4 faits**, plus **J-3.1** (premier amendement du socle en cours de rédaction, PRD §12). **J-4 atteint le 21 juillet 2026**, ses trois termes constatés un par un : 21 chapitres passés par la boucle §5.2, registre de gel complet, remontées toutes tranchées. J-5 et J-6 à faire |
| Phases | **P0 ☑, P1 ☑, P2 ☑, P3 ☑** — les 21 chapitres du tronc sont rédigés, relus adversarialement et corrigés, et les remontées toutes tranchées ; **P4 ☐, P5 ☐**. Suivi au grain de la phase : [PRDPlan §1.6](doc/PRDPlan.md) — ⚠ **ce tableau se renseigne à la clôture d'une passe : le constater sur les pièces avant de s'y fier** |
| Remontées de gouvernance | **42 consignées** (R-G-01 à R-G-42) — **39 tranchées**, **3 sans objet** (R-G-18, R-G-19, R-G-36), **0 ouverte** — [registre](verification/remontees-gouvernance.md), recompté marqueur par marqueur le 21 juillet 2026. ⚠ **Douze le sont par ARBITRAGE DÉLÉGUÉ et demeurent révocables** : R-G-08, R-G-09, R-G-13, R-G-14, R-G-15, R-G-17, R-G-37 à R-G-42. Elles portaient sur la **thèse**, le **découpage**, la **cible de volumétrie**, un **garde-fou et son instrument** ou une **lecture du cadrage** — matière que PRDPlan §5.3 réserve à l'auteur sans exception. ⚠ **Ce chiffre a été annoncé à six par trois porteurs le 21 juillet 2026** — chiffre antérieur à la rédaction des ch. 5 à 21, périmé par le dépouillement de leurs blocs « Remontées ouvertes » pendant que les trois le recopiaient : voir le constat 9 de [`verification/relecture-P3.md`](verification/relecture-P3.md) §8. ⚠ D'autres remontées vivent aux **Notes des pièces** et non au registre |
| Lacunes documentées | **14** (PRD §10) — **2 closes** : la 11 (corpus d'appui, instruite et infructueuse) et la 12 (`commun/faits-partages.md`, close par décision) ; 12 non instruites |
| Écarts TOC constatés | **9** (PRD §7.4), **tous corrigés au TOC v0.5** ; **1 dixième** trouvé à l'exécution, siégeant dans le PRD (§7.4.10), corrigé |
| Assignations | **14 garde-fous sur 14** et **14 lacunes sur 14** assignés à une pièce porteuse — tables au TOC ; **34 pièces sur 34** couvertes par la bijection §6.2 ↔ TOC |

**Ordre d'attaque** — ~~P0 (assainissement du cadrage)~~ **☑** → ~~P1 (lots bloquants)~~ **☑** → ~~P2 (autres lots)~~ **☑** → ~~P3 (tronc, ch. 1 à 21)~~ **☑ close le 21 juillet 2026, J-4 atteint** → **P4 — c'est ici que reprend le travail : avant-propos, ch. 22 à 28, annexes A à E** → P5 (revalidation et publication). ⚠ **Le phasage n'est pas un séquencement strict** : la règle cardinale est *par chapitre*, pas par phase. Un chapitre démarre dès la clôture de **son** lot, même si d'autres restent ouverts — P2 et P3 se recouvrent, et c'est voulu. ⚠ **Deux blocages traversent P4** : le **ch. 26** (interdit par §7.0) et les **douze remontées** en attente. **Six portent sur la matière des ch. 1 à 4** (R-G-08, R-G-09, R-G-13, R-G-14, R-G-15, R-G-17) ; **les six autres, ouvertes à la clôture de P3, portent sur le tronc entier** — thèses des ch. 7, 8, 9, 10, 12 et 20 (R-G-37), huit intitulés (R-G-38), volumétrie des vingt et une pièces (R-G-39), motifs de balayage de PRD §A.6 (R-G-40), homonymie de « mandat » (R-G-41), primauté entre deux règles d'annexe (R-G-42). Plusieurs siègent au TOC ou au PRD plutôt que dans la pièce : leur arbitrage rouvrirait du texte tenu pour fait, **sur les vingt et un chapitres et non sur les quatre premiers**.

**Six chapitres n'ont aucun lot d'instruction** (ch. 4, 8, 10, 25, 27, 28) : ce sont des **chapitres de composition**, qui consomment d'autres chapitres plutôt qu'une passe de recherche. Ils sont **plus** exposés qu'un chapitre de socle, pas moins : sans source à citer, chacune de leurs affirmations est soit tracée vers un chapitre amont, soit une inférence à marquer. ☑ **Trois sont rédigés** (ch. 4, 8, 10) ; **trois restent à écrire** (ch. 25, 27, 28) — dont les ch. 27 et 28, qui portent les **deux cibles les plus lourdes du volume**, 5 500 mots chacune au registre de gel.

⚠ **Le ch. 8 est la seule inversion entre ordre de rédaction et ordre de lecture.** ☑ **Les deux pièces sont rédigées** (constat sur disque, 21 juillet 2026) ; ce qui suit demeure la clé de lecture du ch. 8, non une consigne d'ordonnancement à venir. Le passeport assemble quatre pièces, dont **trois seulement viennent de chapitres** : ch. 5 (carte signée), ch. 7 (inscription au registre) et **ch. 9 (chaîne de mandat)** — ce dernier en Partie III, donc en aval. Le ch. 8 traverse ainsi une frontière de partie et se rédige **après** le ch. 9. ☑ **La quatrième pièce — les attestations de conformité — est instruite (P0.1, 21 juillet 2026) : elle n'a pas de chapitre dédié, et n'en aura pas.** Elle est portée par deux sections existantes, **ch. 7 §7.3** (le registre comme objet réglementaire) et **ch. 19 §19.2** (le registre comme pièce de conformité) ; le §8.1 le déclare et assume l'asymétrie — la quatrième pièce est **la moins documentée des quatre**, et le passeport le dit plutôt que de la présenter à parité. *Motif du refus de créer un chapitre : le découpage à 28 chapitres est cité par le PRD, le README du dépôt et le cadrage du Vol. IV ; une pièce nouvelle coûterait une cascade de décomptes pour une matière que deux sections portent déjà.*
