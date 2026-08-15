# Journal de boucle — actualisation au 15 août 2026

Journal *append-only*. Un bloc par tour : morceau, verdict, écart retenu, coût.

## Cadre fixé avant le lancement

| | |
|---|---|
| **Objectif** | Actualiser en totalité la veille technologique (gel 8 août 2026) et la revue de littérature (gel 9 août 2026) à la date du 15 août 2026 |
| **Portée** | Re-vérification intégrale des 479 références — 303 pour la veille, 176 pour la revue — plus la fenêtre neuve |
| **Barre** | OCDE, *The agentic AI landscape and its conceptual foundations*, OECD Artificial Intelligence Papers n° 56, 34 p., doi:10.1787/396cf758-en, réf. interne DSTI/DPC/GPAI(2025)/18/FINAL — PDF ouvert et lu **en entier** avant de fixer la barre |
| **Périmètre de comparaison** | L'OCDE ne traite ni les protocoles ni l'identité : le juge à l'aveugle ne compare que le périmètre apparié — résumé, méthode, tendances d'adoption, lacunes déclarées |
| **Budget** | ~40 agents. C'est lui qui ferme la boucle : la barre porte une autorité institutionnelle que nous ne prendrons pas |
| **Sortie** | Victoire à l'aveugle, budget épuisé, gains marginaux sur deux tours, ou arrêt demandé |

**Barres écartées, et pourquoi.** NIST NCCoE, concept paper sur l'identité et l'autorisation des
agents — genre différent : document de projet, pas état du champ ; retenu comme *source* de la
re-vérification. Stanford HAI, AI Index 2026 — 400 pages sur neuf chapitres, qu'un critique ne peut
pas opposer en un tour.

**Ce que la lecture de la barre a corrigé.** Elle avait été fixée « 9 juillet 2026 » sur la foi des
métadonnées du PDF. ⚠ **La couverture porte février 2026, et toutes ses sources en ligne sont
consultées le 4 février 2026** : le 9 juillet n'est que la date de production du fichier. Son
information est donc **gelée six mois avant la nôtre**. Trois autres traits, relevés en la lisant
et non en la supposant :

- Elle **se déclare descriptive** — « intended to be descriptive so as to lay the foundation for
  future analytical and policy work » : elle cartographie des définitions, elle n'établit pas
  l'état technique d'un champ.
- Ses données d'adoption viennent d'**une seule enquête**, celle des développeurs de Stack Overflow
  (2025), redécoupée par l'OCDE. Aucune source primaire technique.
- Elle ne traite ni protocole, ni identité, ni délégation, ni exécution durable.

*Conséquence sur la boucle, et elle est inconfortable : la barre est plus faible que prévu sur la
fraîcheur et la traçabilité, et imprenable sur l'autorité. Le juge à l'aveugle doit donc être tenu
strictement au périmètre apparié — sans quoi il désignera le nôtre pour de mauvaises raisons, et
une victoire acquise ainsi n'apprend rien.*

## Tour 0 — socle déterministe (hors boucle)

Les 173 notices arXiv de la revue reprises à l'API du dépôt le 15 août 2026, script stdlib seule
(`reprise-arxiv.py`, scratchpad). **173 obtenues sur 173, aucune introuvable.**

| Relevé | 9 août 2026 (document) | 15 août 2026 (API) |
|---|---|---|
| Publication attestée en notice | 12 | **12 — mêmes références** : [4], [15], [37], [38], [44], [46], [59], [136], [142], [143], [144], [158] |
| Dépôt initial 2023 / 2024 / 2025 / 2026 | 5 / 13 / 52 / 103 | 5 / 13 / 52 / 103 — inchangé |
| Révisées en 2026 | 120 (69 %) | 120 (69 %) — inchangé |
| Révisées en août | cinq, aux neuf premiers jours | **six**, au 15 |
| Versions v1 / v2 / v3 / au-delà | 90 / 49 / 24 / 10 | **88 / 51 / 24 / 10** |

**Deux notices révisées depuis le gel**, et elles seules : [113] `arXiv:2604.05485` « Auditable
Agents », v1 → v2 le 13 août ; [146] `arXiv:2608.02311` « AI Governance for Institutional Readiness
in Finance », v1 → v2 le 10 août. Aucune n'a acquis de `journal_ref` ni de DOI : **l'annexe des
douze pièces arbitrées tient sans changement**, et c'est un résultat, pas une absence de résultat.

*Coût : 1 script, 4 requêtes API, aucun agent.*

---

## Tour 1 — bâtisseurs

Huit morceaux, découpés sur le critère de jugeabilité : cinq sur la veille, trois sur la revue.
Chaque bâtisseur en contexte neuf, périmètres disjoints, artefacts hors du dépôt — le texte
actualisé d'un côté, le relevé de preuves de l'autre. Aucun ne note son travail.

**Ce que la re-vérification a produit — des corrections, pas des ajouts.**

| Morceau | Ce qui est tombé |
|---|---|
| V1 · protocoles | Une date bibliographique **réfutée** : le dernier commit du dépôt ACP d'IBM était donné au 18 juillet 2026, il est du 25 août 2025 — le jour de l'archivage. Un niveau d'exigence normatif corrigé : la canonicalisation A2A est **MUST**, seul le fait de vérifier est SHOULD. Faits neufs : seconde charte de groupe de travail MCP fusionnée le 12 août ; sept commits A2A du 10 au 13 août, **tous de documentation**. |
| V2 · couches implicites | Une **couche entière manquait** : le protocole de paiement Stripe/Tempo du 18 mars 2026, absent de toute la revue. Son entrée fait tomber l'énoncé « le *checkout*, seule sous-couche disputée ». Apache EventMesh a **retiré** sa passerelle A2A le 13 août. Deux URL du gel rendent 404. |
| V3 · identité | **L'énoncé porteur tient, son ordre de grandeur était faux d'un facteur trois** : non pas trois brouillons IETF mais dix, plus un onzième le 14 août — et toujours **aucun adopté par un groupe de travail**. Un trou déclaré n'en est pas un : trois brouillons traitent la révocation en cascade, dont un qui l'exclut par principe. Erreur factuelle corrigée sur un correctif FIPS 204 qui n'existe pas. |
| R1 · corpus | Le partage des régimes passe de 28/133 à **31/130**, dont **deux erreurs de lecture du gel lui-même** — pas des changements survenus depuis. Versions 90/49/24/10 → **88/51/24/10**. Les douze attestées tiennent. |
| R3 · fronts et synthèse | Une pièce **s'est réfutée elle-même** : la v2 du 10 août requalifie son « instanciation calculable » en « illustration synthétique calibrée » ; le corps la citait comme instrument *mesurable*. Trois pièces neuves proposées à l'entrée, sept candidates écartées avec motifs. |

⚠ **Deux dettes ouvertes par ce tour, et elles comptent plus que les trouvailles.**

1. **V3 déclare 27 références de son périmètre non rouvertes** — état *inconnu*, et non *inchangé*.
   C'est la distinction que la re-vérification intégrale demandait ; elle n'est pas encore tenue
   partout. *Un bâtisseur qui l'avoue vaut mieux qu'un bâtisseur qui compte ces 27 comme vérifiées,
   mais la dette reste due.*
2. **R3 porte le corpus de 176 à 179 entrées**, ce qui **invalide les décomptes que R1 vient de
   recalculer** sur 173 notices. Conflit de morceaux, à arbitrer : ou les trois ajouts entrent et
   toute la physionomie se recalcule, ou ils restent dehors. *C'est le prix du découpage : deux
   morceaux jugeables séparément ne sont pas deux morceaux indépendants.*

⚠ **Erreur de consigne, la mienne.** J'ai prescrit la légende de tableau **avant** le tableau. La
veille place les siennes **après** — dix-huit cas sur dix-neuf ; seule la revue les place avant.
Deux bâtisseurs l'ont signalé plutôt que de suivre la consigne. *À corriger au recollage, pas au
tour suivant : c'est un défaut de forme que je porte, pas un écart d'artefact.*

*Coût : 8 agents bâtisseurs, 5 rendus à ce point.*

## Tour 1 — critiques

Huit critiques, un par morceau, chacun en contexte neuf, sans rien savoir de ce que le bâtisseur
avait tenté. Aucun n'a jugé un rapport : tous ont rouvert les sources.

**Le résultat du tour n'est pas dans les huit écarts. Il est dans leur convergence.**

| Critique | L'écart, dans ses mots |
|---|---|
| V1 | « l'artefact établit ses faits négatifs de dépôt en lisant la branche par défaut, puis les énonce au niveau du dépôt » |
| V2 | « l'artefact établit ses deux faits négatifs porteurs en regardant à un seul endroit, jamais à celui que la source désigne » |
| V3 | « l'artefact promeut ses recherches infructueuses au rang de faits négatifs publiés » |
| V4 | « l'artefact applique aux énoncés qu'il hérite une sévérité qu'il relâche sur ceux qu'il produit » |
| V5 | « l'artefact calibre ses réserves sur des refus d'accès qu'il n'a pas su reproduire — et c'est exactement là que sont ses fautes » |

⚠⚠ **Cinq critiques indépendants, cinq formulations, un seul défaut : le fait négatif est bien plus
coûteux à établir que le fait positif, et les cinq bâtisseurs l'ont tous sous-payé.** *Le document
d'origine tenait ses faits négatifs mieux que son actualisation* — la « correction » apportée au
protocole de paiement retirait un énoncé exact, dont la formulation figure mot pour mot dans une
documentation que le bâtisseur n'avait pas ouverte. **C'est l'écart du tour, et il ne se corrige pas
morceau par morceau.**

**Ce que les critiques ont confirmé en rouvrant les sources eux-mêmes** — c'est ce qui distingue un
verdict d'une impression :

- **L'énoncé porteur de la veille tient.** Listes de documents d'OAuth, WIMSE, SCITT, RATS et des
  deux groupes agentiques chartés en juin 2026 ouvertes une à une : **27 brouillons, tous
  individuels, aucun adopté**. Au 15 août 2026, aucun mécanisme normalisé ne maintient de
  traçabilité de délégation au-delà de deux sauts.
- **Le fait négatif d'observabilité tient**, recompté par deux agents qui ne se sont pas parlé :
  **63 attributs**, aucun de mandat, de délégation, d'autorisation ni d'identité authentifiable.
  ⚠ *Deux décomptes automatiques ont menti en route — 61, puis des sous-totaux faux. Il a fallu
  énumérer à la main des deux côtés.*
- **Le texte européen dit bien ce qu'on lui fait dire**, vérifié mot pour mot au point (31) :
  un agent doit divulguer sa nature artificielle **et la personne pour le compte de laquelle il
  agit**. ☑ *C'est la première fois qu'un texte contraignant écrit la question que la veille tient
  pour la plus mal couverte.*
- **Les neuf pièces neuves proposées à la revue existent**, titres exacts, dépôts dans la fenêtre,
  et **chaque chiffre qui leur est prêté figure littéralement à leur résumé**. Aucune mesure
  inventée — c'était le risque propre à tout ajout de dernière minute.
- **Deux fautes de lecture antérieures au gel** sont réelles, pièce en main : la revue attribuait à
  une pièce un constat qu'elle ne porte pas, et fondait en une seule mesure une analyse statique et
  un banc de charge que son résumé sépare.

**Trois coutures ouvertes par le découpage, aucune imputable à un bâtisseur :**

1. **Doublon.** `arXiv:2608.12895` retenu par deux morceaux sous deux numéros. Le corpus consolidé
   compte **184 entrées et non 185** : 176 d'origine, plus huit pièces distinctes sur neuf proposées.
2. **Collision de plages** — deux morceaux numérotent leurs ajouts à partir de 177. *Erreur de
   consigne, la mienne.*
3. **Arithmétique divergente** : chaque critique calculait sur son propre lot. Consolidé —
   **184 entrées, 181 sur arXiv, régimes 12 / 31 / 138**, soit 7 %, 17 %, 76 %.

*Coût du tour 1 : 17 agents — 8 bâtisseurs, 8 critiques, 1 socle. Budget : 17 sur ~40.*

## Tour 2 — reprises

L'écart de chaque critique est reparti à son bâtisseur, qui a repris avec son contexte du tour 1.
**L'écart commun — le fait négatif sous-payé — leur a été donné comme tel à tous les cinq**, pour
qu'aucun ne le prenne pour un défaut personnel.

**Ce que la reprise a corrigé, et ce qu'elle a trouvé en corrigeant :**

| Morceau | Résultat |
|---|---|
| V1 | Deux faits négatifs tombent, **un troisième que le critique n'avait pas vu** est trouvé par le bâtisseur : la suite de conformité A2A n'est pas immobile, six demandes de tirage ouvertes dont des vecteurs de canonicalisation — aucune fusionnée. ☑ *Ce fait renforce la section au lieu de l'affaiblir : le chantier ouvert est là où le document situe le risque.* Le relevé porte désormais une colonne **« Niveau d'établissement »** — réponse structurelle à un défaut structurel. |
| V2 | L'énoncé x402 **rétabli** : la formulation figurait dans la documentation, le bâtisseur n'avait cherché que dans la spécification. Le « retrait » EventMesh requalifié en migration de branche. Deux gains inattendus : « seize sièges » cesse d'être un report non vérifié, « plus de quarante adoptants » devient « une quarantaine » — la page en liste quarante. |
| V3 | **Le chiffre change et le fait s'améliore : douze brouillons, pas dix, et l'accélération n'existe pas.** Recompté sur les dates de dépôt initial : cadence régulière du 25 mars au 7 août. L'agglutinat d'août était un artefact — les auteurs rafraîchissent avant expiration, et les dates de révision avaient été lues comme des dépôts. Les trois faits négatifs inventés sont retirés. **Trente références restent déclarées inconnues.** |
| V4 | Ses deux fautes rouvertes et **révoquées**. Sa formulation est la leçon du tour : *le fait neuf n'a encore été relu par personne, c'est ce qui le rend plus exposé, pas moins.* Volume ramené de +16,9 % à +14,8 % **avec six constats de plus**. |
| V5 | PDF réglementaire extrait par lui-même, 51 p. **L'incident requalifié** : ce n'est pas une attaque, c'est un **échec de confinement d'évaluation** qui a atteint la production d'un tiers non partie à l'exercice — les trois récits ne se contredisaient pas, ils se chaînaient. ☑ Une correction qui renforce la thèse : le régulateur nomme un mécanisme, et c'est **eIDAS** — ni MCP, ni A2A. |
| R1 | Cardinaux consolidés recalculés à l'API. ⚠⚠ **Et une observation que personne n'avait demandée : deux d'entre eux sont fabriqués par l'instrument.** Les révisions d'août contiennent les pièces que la reprise vient d'ajouter *parce qu'elles sont neuves* ; la hausse du taux de non-révision vient de ce que les arrivantes sont en v1. *La reprise rajeunit le corpus qu'elle mesure*, et l'artefact le déclare. |
| R2 | Couverture refaite front par front — onze interrogations, 630 notices, **huit pièces de plus**, dont les deux que le critique nommait. ASCon tranché sur le texte intégral : le plafond cité n'est pas battu, il n'est **pas comparable**. La réserve a quitté le fichier annexe pour le corps. |
| R3 | Le verdict 3 porte enfin son cadre : sur l'expérience principale, l'invite constitutionnelle atteint 0/384 **comme** le garde à provenance. ☑ *Le bâtisseur en tire la conclusion qui l'affaiblit* — « une position appuyée par une mesure de portée étroite, non un fait mesuré de portée générale » — en rappelant que la revue reproche ailleurs au champ exactement cette élision. |

*Coût du tour 2 : 8 reprises. Budget : 25 sur ~40.*

## Recollage — ce que les contrôles ont attrapé

Recollage par script : renumérotation des références et remplacement des sections. **63 sections
recollées sur la veille, 62 sur la revue, aucune non appariée.**

⚠ **Deux pièges de recollage, tous deux miens :**

1. **Granularité.** Le premier essai remplaçait une section de niveau 1 par son bloc englobant —
   ce qui **emportait toutes ses sous-sections** et a effacé deux périmètres entiers, chaque
   bâtisseur ne portant que les siennes. *Restauré depuis sauvegarde, corrigé : un titre ne possède
   que son texte propre.*
2. **Homonymie.** La revue répète sept sous-titres sous des fronts différents — « Ce que la
   littérature établit » y figure **sept fois**. Un appariement par titre seul écrivait au mauvais
   endroit ; l'appariement se fait par chemin complet.

☑ **Les trois contrôles du dépôt ont fait exactement ce pour quoi ils existent**, et ont attrapé ce
que ni bâtisseur ni critique ne pouvait voir :

- **Veille** — 350 références, appariement clos dans les deux sens, mais **huit URL partagées entre
  une entrée héritée et une entrée neuve**. *Un bâtisseur qui ajoute une source déjà citée ailleurs
  ne fait pas une faute : il ne voyait pas les quatre autres périmètres.*
- **Revue** — 192 entrées, 189 sur arXiv, régimes réels **12 / 29 / 148**. **Aucun des cardinaux
  annoncés par les trois bâtisseurs ne correspondait à la bibliographie effectivement produite** :
  chacun calculait sur son propre lot. *C'est précisément pourquoi ils n'ont pas été inscrits sur
  annonce.*
