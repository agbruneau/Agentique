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

**Le dossier contient trois fichiers de gouvernance dans `doc/`, et rien d'autre.** Aucun chapitre, aucune arborescence de rédaction, aucun pipeline de rendu, aucune source déposée.

Documents de gouvernance, par ordre d'autorité :

1. [PRD.md](doc/PRD.md) **v0.1** — contenu, héritage du socle, garde-fous, critères d'acceptation (**prime en cas de conflit**, y compris sur le TOC) ;
2. [TOC.md](doc/TOC.md) **v0.4** — **autorité sur le découpage** : toute modification du nombre ou de l'ordre des chapitres passe par lui (version++), et se répercute au PRD ;
3. [PRDPlan.md](doc/PRDPlan.md) **v0.1** — plan d'exécution (phases P0 à P5, boucle qualité §5.2, formulations imposées §5.5). Il **ordonnance** le PRD, il ne le redéfinit pas.

⚠ **Emplacement tranché le 18 juillet 2026 : `doc/`**, comme au Vol. II — l'activité **P0.3** du PRDPlan est close par ce déplacement. Le plan lui-même n'en a pas encore été amendé : son §1.3 décrit toujours une arborescence à la racine du volume et argumente en sa faveur. **Le disque fait foi, pas le §1.3.**

## ⚠ Aucun chapitre n'est rédigeable aujourd'hui

**Règle cardinale (PRD §7.0)** — *aucun chapitre n'est rédigé avant la clôture du lot d'instruction dont il dépend.* Un chapitre écrit sur un socle vide n'est pas un chapitre en avance : c'est une inférence longue, et le volume qui prend l'identité pour objet ne peut pas se permettre d'en produire.

État du socle : **0 entrée propre**. 33 entrées héritées (H-01 à H-33), **15 lots d'instruction ouverts** (L-01 à L-15), **0 clos**. Aucune passe de recherche n'a été menée par ce volume.

Deux décisions de cadrage restent **à l'auteur, pas à l'agent**, et bloquent la suite (PRDPlan §2, phase P0) :

| # | Décision | Ce qu'elle bloque |
|---|---|---|
| **P0.2** | **Corpus d'appui** — déposer les trois ouvrages annoncés, ou retirer la filiation livresque | L-15, **sept sections** (§4.4, §9.4, §25.1, §25.5, §27.4, §27.5, §28.4) et **l'annexe E entière**. Le TOC les annonce « déposé au dépôt » ; vérification du 18 juillet 2026 : **aucun des trois n'est présent** (PRD §7.7) |
| **P0.1** | Révision du TOC sur les **neuf écarts** constatés (PRD §7.4) | La cohérence de tous les renvois vers les Vol. I et II |

*(**P0.3** — emplacement des documents de gouvernance — est close : `doc/`, tranchée le 18 juillet 2026.)*

**Ne jamais rédiger l'une des sept sections bloquées « de mémoire ».** Écrire ce que ces livres contiennent sans les avoir ouverts serait la faute même que le volume documente au ch. 5 — qualifier par la promesse plutôt que par la démonstration.

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

CA-10 les impose, et ils viennent des neuf écarts de PRD §7.4 — tous constatés sur pièce, aucun encore corrigé au TOC.

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

### Séquelles du déplacement vers `doc/` — deux renvois, ouverts

Le déplacement du 18 juillet 2026 a cassé deux liens, tous deux dans `doc/PRDPlan.md`. Les liens frères (`](PRD.md)`, `](TOC.md)`) résolvent toujours : les trois fichiers sont restés ensemble.

| Fichier | Renvoi cassé | Cible réelle |
|---|---|---|
| `doc/PRDPlan.md` §1 (en-tête) | `](../../CLAUDE.md)` — vise la racine du dépôt, résout aujourd'hui dans `1 - Corpus Agentique/` | `../../../CLAUDE.md` |
| `doc/PRDPlan.md` §5.4 (**gabarit de pièce**) | `](../../TOC.md)` — relatif à un futur chapitre sous `monographie/<partie>/` | `../../doc/TOC.md` |

⚠ **Le second est le plus coûteux des deux, et de loin.** Il vit dans le **gabarit** que les 34 pièces recopieront : non corrigé, il produit mécaniquement 34 renvois cassés — la reproduction exacte du gisement de 47 du Vol. II, à ceci près qu'ici **aucune pièce n'est encore écrite**. Corriger le gabarit maintenant coûte un caractère ; le corriger après P4 coûtera 34 éditions.

Le PRDPlan §1.3 (structure cible) et son activité **P0.3** décrivent encore l'arborescence antérieure et argumentent pour la racine du volume : **à amender, comme la clôture de P0.3.**

## Divergences non arbitrées — signalées, jamais tranchées

Deux faits datés divergent entre les livrables du dépôt. Le CLAUDE.md racine impose de les signaler sans les uniformiser ; ce volume les **porte** (PRD §7.5, qui en est la source de vérité pour la durée de rédaction) :

- **Gouvernance d'AP2** — Vol. I et veille : transfert à la FIDO Alliance le 28 avril 2026, donné pour fait établi. Vol. II (gel postérieur) : aucun transfert documenté, position tenue en quatre endroits concordants et rangée parmi les **ignorances déclarées**. → ch. 9, lot L-06. **L'arbitrage par chronologie est interdit** : le volume le plus récent est ici le plus réservé.
- **Date de la ligne directrice IA de l'AMF** — Vol. II : 30 mars 2026 (avec dette de vérification déclarée). Veille : 7 avril 2026. → ch. 19. L'entrée en vigueur au 1er mai 2027 est, elle, concordante.

⚠ Le fichier prévu pour porter ces divergences — `commun/faits-partages.md` — **n'existe pas** et n'est pas créé par ce volume (décision, PRD §7.5). Les renvois du TOC vers ce chemin sont à repointer vers §7.5 (P0.7).

## Sensibilité temporelle

Le domaine se périme par trimestres, et ce volume hérite de **deux gels distincts** : juin 2026 (Vol. I) et 16-17 juillet 2026 (Vol. II). **Un volume date de son gel, pas de sa lecture.** Toute entrée héritée portant un fait chaud (PRD §8.3, sept lignes) est **revalidée à la source primaire** avant d'entrer dans un chapitre, quel que soit son niveau d'origine.

⚠ **La révision majeure de la spécification MCP est attendue le 28 juillet 2026** — dix jours après la rédaction du PRD. Revalidation d'ouverture en P0.6, revalidation finale en P5.1.

Chaque pièce porte sa propre date de gel, consignée au registre (CA-04).

## Conventions

- **Langue** : français canadien soutenu ; terminologie technique anglaise entre parenthèses et en italique à la première occurrence ; citations verbatim en langue originale (CA-08).
- **Commits** : messages en anglais, format Conventional Commits — convention du Vol. II, retenue ici parce que ce volume prolonge son appareil (`docs(prd): …`, `docs(mono): draft chapter N — <slug anglais court>`), sujet ≤ 50 caractères quand possible (plafond 72), mode impératif. ⚠ Le Vol. I emploie des messages courts **en français** : vérifier le dossier de travail avant de rédiger le message.
- **Chirurgie** : ne modifier que les sections concernées. **Ne jamais renuméroter** les identifiants existants — H-xx (héritées), F-xx (socle propre), R-xx (garde-fous), L-xx (lots), CA-xx (critères) : ils sont cités en références croisées, ici et dans le compendium du Vol. IV que son TOC annonce déjà.
- **Versionnage** : incrémenter la version du PRD à chaque enrichissement substantiel, et la table des jalons (§12) avec. Le TOC se versionne à toute modification du découpage.
- **Décomptes** : tout chiffre publié est **re-mesuré**, jamais recopié d'un autre document. Un même chiffre vit à plusieurs endroits — PRD, TOC, README du volume, README du dépôt : **les mettre à jour ensemble, jamais l'un sans les autres**. Commande de référence : PRDPlan §1.5, seule autorité de décompte du volume.
- **Attestations** : « conforme », « vérifié », « résolu » s'écrivent depuis une **constatation sur pièce**, jamais depuis un document amont qui le déclare ni depuis le souvenir de l'avoir fait (CA-14).

## État du projet (18 juillet 2026)

**Cadrage établi, exécution non commencée.** Trois documents : **TOC v0.4, PRD v0.1, PRDPlan v0.1**.

| | État |
|---|---|
| Pièces rédigées | **0 sur 34** (28 chapitres + avant-propos + 5 annexes) |
| Volumétrie cible | **102 500 mots** (re-sommée depuis les cibles par bloc du TOC, qui annonce « ≈ 100 000 » ; **indicative et non normative**) |
| Socle propre | **0 entrée** |
| Socle hérité | **33 entrées** — H-01 à H-16 (Vol. II), H-17 à H-33 (Vol. I) |
| Lots d'instruction | **0 clos sur 15** ; trois bloquants au sens fort : **L-03** (ch. 5), **L-08** (ch. 12), **L-15** (corpus d'appui) |
| Jalons | **J-0 fait** ; J-1 à J-6 à faire |
| Phases | **P0 à P5 toutes ☐** |
| Lacunes documentées | **14** (PRD §10), aucune instruite |
| Écarts TOC constatés | **9** (PRD §7.4), aucun corrigé au TOC |

**Ordre d'attaque** — P0 (assainissement du cadrage, **dont les trois décisions d'auteur ci-dessus**) → P1 (lots bloquants) → P2 (douze autres lots) → P3/P4 (rédaction) → P5 (revalidation et publication). ⚠ **Le phasage n'est pas un séquencement strict** : la règle cardinale est *par chapitre*, pas par phase. Un chapitre démarre dès la clôture de **son** lot, même si d'autres restent ouverts — P2 et P3 se recouvrent, et c'est voulu.

**Six chapitres n'ont aucun lot d'instruction** (ch. 4, 8, 10, 25, 27, 28) : ce sont des **chapitres de composition**, qui consomment d'autres chapitres plutôt qu'une passe de recherche. Ils sont **plus** exposés qu'un chapitre de socle, pas moins : sans source à citer, chacune de leurs affirmations est soit tracée vers un chapitre amont, soit une inférence à marquer.

⚠ **Le ch. 8 est la seule inversion entre ordre de rédaction et ordre de lecture.** Le passeport assemble quatre pièces, dont **trois seulement viennent de chapitres** : ch. 5 (carte signée), ch. 7 (inscription au registre) et **ch. 9 (chaîne de mandat)** — ce dernier en Partie III, donc en aval. Le ch. 8 traverse ainsi une frontière de partie et se rédige **après** le ch. 9. La **quatrième pièce**, les attestations de conformité, n'a **aucun chapitre dédié** au découpage actuel : point à instruire en P0.1.
