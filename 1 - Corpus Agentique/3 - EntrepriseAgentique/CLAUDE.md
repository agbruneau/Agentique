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

Projet documentaire, **au stade du cadrage**. Livrable visé : une monographie exhaustive — « L'entreprise agentique : identité non humaine, délégation vérifiable, maillage d'agents et AgentOps » — sur ce qu'une entreprise doit tenir pour que des agents y opèrent sous mandat vérifiable. Objet choisi parce que les Vol. I et II le désignent l'un et l'autre comme leur verrou résiduel : « identité non humaine et délégation multi-saut » (Vol. I, `Synthese Monographie.md` §11.6) et les questions Q2, Q3, Q5 du Vol. II (ch. 21 §21.2).

**Le dossier contient la gouvernance dans `doc/`, l'arborescence de rédaction dans `monographie/`, et les rapports dans `verification/`.** ⚠ **Les 34 pièces de `monographie/` sont des gabarits** — en-tête à cinq champs et thèse citée du TOC, **zéro ligne de corps**. Un gabarit n'est ni un brouillon ni une ébauche. Aucun pipeline de rendu, aucune source déposée.

Documents de gouvernance, par ordre d'autorité :

1. [PRD.md](doc/PRD.md) **v1.0** — contenu, héritage du socle, garde-fous, critères d'acceptation (**prime en cas de conflit**, y compris sur le TOC) ;
2. [TOC.md](doc/TOC.md) **v0.6** — **autorité sur le découpage** : toute modification du nombre ou de l'ordre des chapitres passe par lui (version++), et se répercute au PRD. Il porte en outre, depuis la v0.5, la **table de couverture** (§6.2 ↔ TOC) et la **table d'assignation** des garde-fous et des lacunes ;
3. [PRDPlan.md](doc/PRDPlan.md) **v0.4** — plan d'exécution (phases P0 à P5, boucle qualité §5.2, formulations imposées §5.5). Il **ordonnance** le PRD, il ne le redéfinit pas.

⚠ **Emplacement `doc/` : tranché sur disque le 18 juillet 2026, amendé au plan le 21.** L'activité **P0.3** est close, le §1.3 du PRDPlan est réécrit, et **les deux renvois relatifs qu'il portait à faux sont corrigés** — dont celui du **gabarit §5.4**, qui aurait produit mécaniquement 34 renvois cassés une fois recopié dans les pièces. Chemin correct vers le TOC : `../doc/TOC.md` depuis `monographie/`, `../../doc/TOC.md` depuis un dossier de partie ou `90-annexes/`.

## La règle cardinale ne bloque plus — et c'est le moment où elle protège le moins

**Règle cardinale (PRD §7.0)** — *aucun chapitre n'est rédigé avant la clôture du lot d'instruction dont il dépend.* Un chapitre écrit sur un socle vide n'est pas un chapitre en avance : c'est une inférence longue, et le volume qui prend l'identité pour objet ne peut pas se permettre d'en produire.

État du socle au 21 juillet 2026 : **78 entrées propres re-mesurées** (F-01 à F-78), 33 entrées héritées (H-01 à H-33), **15 lots clos sur 15** — quatorze par instruction aboutie, **L-15 par échec documenté**. **Aucune pièce n'est rédigée.**

⚠ **Ce qui demeure après la levée de la règle cardinale, ce sont les dépendances éditoriales** du PRDPlan §5.1, et elles ne se déduisent pas du socle : le **ch. 4** ouvre l'ouvrage et conditionne toute application de la grille ; le **ch. 8 se rédige après le ch. 9**, en travers des parties ; les **six chapitres de composition** attendent leurs chapitres amont et sont **plus** exposés qu'un chapitre de socle, pas moins. *Un socle constitué autorise la rédaction ; il ne la planifie pas.*

⚠ **Trois choses ne sont pas des passes d'instruction, et il ne faut pas les compter comme telles** : la clôture de **L-15** (vérification d'absence aboutie), la **revalidation d'ouverture** des faits chauds ([`revalidation-2026-07-21.md`](verification/revalidation-2026-07-21.md)) et les **contrôles de bornage** de P2. Aucune ne crée d'entrée F-xx. ⚠ **Et la revalidation d'ouverture s'est trompée deux fois**, corrigée depuis par les sources primaires des lots L-05 et L-14 (PRD §8.3) : *une revalidation constate l'état d'une source à une date, et si elle le fait sur du secondaire, elle se trompe comme du secondaire.*

**Les décisions d'auteur de la phase P0 sont prises (21 juillet 2026).** L'état antérieur — deux décisions bloquantes en attente — est clos :

| # | Décision | Issue retenue |
|---|---|---|
| **P0.2** | **Corpus d'appui** — déposer les trois ouvrages annoncés, ou retirer la filiation livresque | ☑ **Filiation retirée.** Le rejeu de la vérification (21 juill. 2026) confirme que les trois ouvrages n'ont jamais été déposés, jusque dans l'historique git. **L-15 clos par échec documenté** ; les sept sections et l'annexe E bloquées (§4.4, §9.4, §25.1, §25.5, §27.4, §27.5, §28.4, annexe E) sont **réaffectées au socle** — table de réaffectation au TOC. ⚠ **Réversible** : un dépôt ultérieur rouvre L-15 |
| **P0.1** | Révision du TOC sur les **neuf écarts** constatés (PRD §7.4) | ☑ **Les neuf corrigés au TOC v0.5**, chacun revérifié sur pièce avant correction. **Un dixième écart trouvé à l'exécution**, siégeant dans le PRD : §7.4.6 nommait le dépôt `Monographies` — il s'appelle **`Agentique`** (§7.4.10) |
| **P0.3** | Emplacement des documents de gouvernance | ☑ `doc/`, tranchée le 18 juillet 2026, **amendée au plan le 21** |

⚠ **Le risque a changé de nature, il n'a pas disparu.** Sept sections et une annexe privées de leur cadre conceptuel externe, ce sont huit endroits où la tentation devient de **combler par la construction d'auteur** — faute symétrique de celle qu'on corrige, et d'un coût comparable. La parade est **CA-07 sans indulgence** : « Lecture de l'auteur » en tête d'énoncé, suivi de ce que le socle établit *et* de ce qu'il n'établit pas. **Ne jamais rédiger l'une de ces sept sections et l'annexe E « de mémoire », ni sur un gabarit emprunté sans source.**

## PRD.md fait autorité

Toute contribution s'y conforme. Les points qu'un agent ne peut pas déduire du texte et se trompera à supposer :

- **Socle (§7)** — deux régimes d'héritage, **et il ne faut pas les confondre**. Une entrée du Vol. II **conserve son niveau** [A]/[B]/[C] avec sa provenance F-xx (méthode identique, rien à re-subir). Une entrée du Vol. I **entre en [C]** — non par défiance, mais parce que la vérification du Vol. I porte sur les *références* (existence, auteurs, année) et non sur le *contenu des affirmations*. Trois des seize entrées du Vol. II (H-13, H-15, H-16) ne viennent pas de son socle factuel : elles entrent comme garde-fou ou thèse attribuée, **jamais comme faits**.
- **Deux instruments épistémiques orthogonaux** — les niveaux [A]/[B]/[C] (Vol. II : ce que l'affirmation a subi) et le tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF (Vol. I : ce que l'énoncé prétend sur le futur). Un fait peut être [B] **et** PROJETÉ. L'ouvrage emploie les deux, **jamais l'un pour l'autre** (CA-11).
- **Garde-fous (§8.1, R-01 à R-14)** — quatorze formulations proscrites. Les trois qui se violent sans y penser : **R-01** (le passeport d'agent n'existe dans aucune spécification — c'est une construction de l'ouvrage) ; **R-02**, convention cardinale (un mécanisme cryptographique est qualifié par ce que sa spécification **démontre**, jamais par ce qu'elle **promet**) ; **R-03** (« entreprise agentique », « maillage d'agents », « AgentOps » sont des termes de marché sans définition normative, chacun défini à un **siège unique**).
- **Attribution (§8.2)** — toute métrique auto-déclarée est attribuée à sa source **à chaque occurrence, sans exception d'usage illustratif**. *Un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait.*
- **Trois degrés d'absence (§8.6)** — fait négatif **VÉRIFIÉ** (balayage documenté d'un texte) > fait négatif **ÉTABLI** (réserve explicite du socle, sans balayage) > **absence de documentation** (le socle est muet). Jamais « le socle ne documente pas X, donc X n'existe pas » (R-14).
- **Marquage d'inférence (CA-07)** — toute construction d'auteur porte **« Lecture de l'auteur »** en tête d'énoncé. Le ch. 8, le ch. 26 et le §27.4 sont des constructions d'auteur **en totalité** : marquage à l'ouverture de la pièce, pas seulement au paragraphe.
- **Neutralité fournisseur (§8.4)** — Entra Agent ID, passerelles MCP, offres de maillage : cas d'instanciation documentés, jamais recommandations. **Annonce, GA, feuille de route, préversion : quatre choses différentes.**
- **Dualité d'usage (§8.5, R-12)** — la Partie IV décrit la mécanique des attaques au niveau architectural, cite les identifiants, **n'en reproduit aucun**. ⚠ **R-12 est le seul garde-fou sans motif de balayage** : aucun `grep` ne détecte une recette d'exploitation. Il est contrôlé par **CA-12 seul**, une relecture dédiée et distincte de la relecture de conformité. Un balayage §A.6 « vert » ne dit rien de R-12.

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

⚠ **Ce rapport se périme, et il ne dispense de rien** : il n'a créé aucune entrée de socle, clos aucun lot, arbitré aucune divergence. La revalidation finale P5.1 reprend les sept lignes.

Chaque pièce porte sa propre date de gel, consignée au registre [`monographie/99-registre-gel.md`](monographie/99-registre-gel.md) — **au même commit que la pièce** (CA-04).

## Conventions

- **Langue** : français canadien soutenu ; terminologie technique anglaise entre parenthèses et en italique à la première occurrence ; citations verbatim en langue originale (CA-08).
- **Commits** : messages en anglais, format Conventional Commits — convention du Vol. II, retenue ici parce que ce volume prolonge son appareil (`docs(prd): …`, `docs(mono): draft chapter N — <slug anglais court>`), sujet ≤ 50 caractères quand possible (plafond 72), mode impératif. ⚠ Le Vol. I emploie des messages courts **en français** : vérifier le dossier de travail avant de rédiger le message.
- **Chirurgie** : ne modifier que les sections concernées. **Ne jamais renuméroter** les identifiants existants — H-xx (héritées), F-xx (socle propre), R-xx (garde-fous), L-xx (lots), CA-xx (critères) : ils sont cités en références croisées, ici et dans le compendium du Vol. IV que son TOC annonce déjà.
- **Versionnage** : incrémenter la version du PRD à chaque enrichissement substantiel, et la table des jalons (§12) avec. Le TOC se versionne à toute modification du découpage.
- **Décomptes** : tout chiffre publié est **re-mesuré**, jamais recopié d'un autre document. Un même chiffre vit à plusieurs endroits — PRD, TOC, README du volume, README du dépôt : **les mettre à jour ensemble, jamais l'un sans les autres**. Commande de référence : PRDPlan §1.5, seule autorité de décompte du volume.
- **Attestations** : « conforme », « vérifié », « résolu » s'écrivent depuis une **constatation sur pièce**, jamais depuis un document amont qui le déclare ni depuis le souvenir de l'avoir fait (CA-14).

## État du projet (21 juillet 2026)

**Cadrage assaini, jalon J-1 clos, rédaction non commencée.** Trois documents de gouvernance : **TOC v0.5, PRD v0.2, PRDPlan v0.2** — plus, depuis la phase P0, l'arborescence `monographie/` (34 gabarits + registre de gel) et `verification/` (un rapport de revalidation).

⚠ **Ce que P0 n'a pas fait, et qu'aucune de ses sorties ne doit laisser croire.** Aucune entrée de socle créée, aucun lot d'instruction mené hors la vérification d'absence de L-15, aucune divergence arbitrée, aucune ligne de corps rédigée. *Un cadrage assaini n'est pas un ouvrage commencé.*

| | État |
|---|---|
| Pièces rédigées | **0 sur 34** (28 chapitres + avant-propos + 5 annexes) — les 34 existent **au gabarit**, corps vide. **Toutes sont désormais rédigeables** au regard de la règle cardinale |
| Volumétrie cible | **102 500 mots** — re-sommée le 21 juillet 2026 depuis les cibles par bloc, **concordante** entre TOC, PRD §6.1 et registre de gel ; **indicative et non normative**. ⚠ Le README du dépôt porte encore « ≈ 100 000 » : réalignement en **P5.3**, avec les autres porteurs |
| Socle propre | **78 entrées re-mesurées** — F-01 à F-26 (P1), F-27 à F-78 (P2). **180 affirmations instruites, 80 soumises au vote, 17 écartées** ; **53 corrections de bornage** ; **106 échecs de source consignés** |
| Socle hérité | **33 entrées** — H-01 à H-16 (Vol. II), H-17 à H-33 (Vol. I) |
| Lots d'instruction | **15 clos sur 15** — quatorze par instruction aboutie, **L-15** par échec documenté. ⚠ **La règle cardinale §7.0 ne bloque plus aucun chapitre** ; les dépendances éditoriales du PRDPlan §5.1 demeurent |
| Jalons | **J-0 à J-3 faits** ; J-4 à J-6 à faire |
| Phases | **P0 ☑, P1 ☑, P2 ☑** ; P3 à P5 ☐ — suivi au grain de la phase : [PRDPlan §1.6](doc/PRDPlan.md) |
| Remontées de gouvernance | **4 tranchées** (R-G-01 à R-G-04) — [registre](verification/remontees-gouvernance.md). ⚠ **Trois d'entre elles corrigent le cadrage lui-même** |
| Lacunes documentées | **14** (PRD §10) — **2 closes** : la 11 (corpus d'appui, instruite et infructueuse) et la 12 (`commun/faits-partages.md`, close par décision) ; 12 non instruites |
| Écarts TOC constatés | **9** (PRD §7.4), **tous corrigés au TOC v0.5** ; **1 dixième** trouvé à l'exécution, siégeant dans le PRD (§7.4.10), corrigé |
| Assignations | **14 garde-fous sur 14** et **14 lacunes sur 14** assignés à une pièce porteuse — tables au TOC ; **34 pièces sur 34** couvertes par la bijection §6.2 ↔ TOC |

**Ordre d'attaque** — ~~P0 (assainissement du cadrage)~~ **☑ close** → **P1 (lots bloquants — c'est ici que reprend le travail)** → P2 (autres lots) → P3/P4 (rédaction) → P5 (revalidation et publication). ⚠ **Le phasage n'est pas un séquencement strict** : la règle cardinale est *par chapitre*, pas par phase. Un chapitre démarre dès la clôture de **son** lot, même si d'autres restent ouverts — P2 et P3 se recouvrent, et c'est voulu.

**Six chapitres n'ont aucun lot d'instruction** (ch. 4, 8, 10, 25, 27, 28) : ce sont des **chapitres de composition**, qui consomment d'autres chapitres plutôt qu'une passe de recherche. Ils sont **plus** exposés qu'un chapitre de socle, pas moins : sans source à citer, chacune de leurs affirmations est soit tracée vers un chapitre amont, soit une inférence à marquer.

⚠ **Le ch. 8 est la seule inversion entre ordre de rédaction et ordre de lecture.** Le passeport assemble quatre pièces, dont **trois seulement viennent de chapitres** : ch. 5 (carte signée), ch. 7 (inscription au registre) et **ch. 9 (chaîne de mandat)** — ce dernier en Partie III, donc en aval. Le ch. 8 traverse ainsi une frontière de partie et se rédige **après** le ch. 9. ☑ **La quatrième pièce — les attestations de conformité — est instruite (P0.1, 21 juillet 2026) : elle n'a pas de chapitre dédié, et n'en aura pas.** Elle est portée par deux sections existantes, **ch. 7 §7.3** (le registre comme objet réglementaire) et **ch. 19 §19.2** (le registre comme pièce de conformité) ; le §8.1 le déclare et assume l'asymétrie — la quatrième pièce est **la moins documentée des quatre**, et le passeport le dit plutôt que de la présenter à parité. *Motif du refus de créer un chapitre : le découpage à 28 chapitres est cité par le PRD, le README du dépôt et le cadrage du Vol. IV ; une pièce nouvelle coûterait une cascade de décomptes pour une matière que deux sections portent déjà.*
