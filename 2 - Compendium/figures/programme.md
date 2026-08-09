# Programme de figures — opportunités par chapitre

*Relevé du 31 juillet 2026, sur un rendu de 1 072 pages qui ne portait que trois figures. Ce document liste **237 opportunités**, **de deux à huit par chapitre, les cinquante couverts**, et les ordonne.*

> ⚠ **ÉTAT : LE BARÈME A EST EXÉCUTÉ.** Les **115 candidats A** sont dessinés et posés dans leur pièce — voir `contenu*.py`, une entrée par figure. Le volume porte **118 figures** sur **1 000 pages** — *1 114 du 31 juillet au 9 août 2026, 1 072 au relevé ci-dessus ; le décompte de figures n'a pas bougé, seul le gabarit a été calé.* Les barèmes **B (94)** et **C (28)** restent ouverts, et ce document reste leur registre. ⚠ Ne pas relire les tableaux ci-dessous comme une liste de travaux à faire : la colonne de barème dit le rang, pas l'état.

---

## Méthode, et sa limite

Le relevé est pris sur **la structure déclarée de chaque pièce** — 525 titres de sous-section et les 113 légendes de tableaux —, non sur une lecture intégrale des 3,3 Mo de corps. ⚠ **Une opportunité listée ici est un candidat, pas une figure validée** : chacune demande la lecture du § avant d'être dessinée, et certaines se révéleront redondantes avec la prose ou trop minces pour tenir une figure. Le signal le plus fiable est le **tableau qui décrit une structure plutôt que des données** — il est presque toujours une figure qui s'ignore.

## Conventions à tenir

| | |
|---|---|
| **Nom de fichier** | `f-NN-MM-slug.svg` — NN le chapitre, MM la **section** où la figure se pose |
| **Légende** | `**Figure N.M** — …`, le rang de la figure étant celui de sa section |
| **Une figure par section** | deux figures dans un même § entreraient en collision de numérotation |
| **Largeur** | `viewBox` de **445 unités** = 157,0 mm = largeur du corps. Une unité vaut un point : les corps de texte s'écrivent à leur valeur finale (8,5 pt un libellé, 7 pt une annotation) |
| **Fond explicite** | `#FDFBF9` — la figure se rend aussi dans la page `.html` de la pièce, à thème sombre |
| **Palette** | celle de [`build/compendium.template`](../build/compendium.template) : encre `#212121`, accent `#9A3B12`, filet `#C2C2C2`, crème `#FAF5F0`, gris `#4d4d4d` |
| **Contenu** | ⚠ **rien qui ne soit dans le texte**, et la figure porte **la réserve autant que la thèse**. La figure 8.1 ne montre pas seulement la réduction N×M ; elle montre ce que la couche de contrat ne porte pas, parce que le paragraphe consacre sa seconde moitié à ce manque |

## Barème

- **A** — la figure que le chapitre appelle : sans elle, sa matière reste opaque à qui n'a pas le domaine. **115 candidats**, soit un peu plus de deux par chapitre.
- **B** — gain réel de lecture, à faire si le programme se poursuit. **94 candidats.**
- **C** — le tableau suffit aujourd'hui ; figure seulement si le chapitre est retravaillé. **28 candidats.**

⚠ **Un A n'est pas une priorité d'exécution** : ils sont 115, et cent quinze figures sont un projet, pas une passe. La sélection exécutable est le **premier lot de douze** en fin de document, choisi sur le nombre de pages que chaque figure éclaire — pas sur le rang de son chapitre.

## Doublons repérés — une seule figure, l'autre site renvoie

| Sites | Arbitrage |
|---|---|
| § 24.0.3 ↔ § 8.1.1 | le fil N×M → N+M est **déjà porté** par la figure 8.1 : renvoi, pas figure |
| § 24.2.1 ↔ § 43.1.1 | deux découpages « à six couches » ; la figure se pose au **siège** (43.1) |
| § 34.7.4 ↔ § 49.1 | l'horizon réglementaire ; la frise se pose au **49.1**, qui est le squelette daté |
| § 3.4.5 ↔ § 38.3 | propagation de trace ; la classique au 3.4.5, l'**agentique** au 38.3 — deux figures, deux objets |
| § 7.1.2 ↔ figure 1.1 | les niveaux LCIM sont déjà dessinés : renvoi |

---

# Livre I — Coopérer

## Ch. 1 — L'interopérabilité comme problème d'intégration d'entreprise
*Deux figures en place (§ 1.0, § 1.1).*

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 1.3 | SOA → ESB → microservices → maillage : ce que chaque étage déplace, et le couplage qui décroît | frise stratifiée | **A** |
| 1.5 | Les trois garanties de livraison, et le point où « exactement-une-fois » devient un **traitement** et non une livraison — siège que le ch. 48 § 48.2 cite | schéma d'échec | **A** |
| 1.2 | Les modèles de maturité à niveaux (LISI, EIMM, IMM) et la limite commune des échelles ordinales | échelles comparées | B |
| 1.6 | Orchestration contre chorégraphie : qui détient le fil de contrôle | deux graphes | B |
| 1.4 | Panorama des styles d'API et les critères qui les départagent | matrice | C |

## Ch. 2 — Données, sémantique et ontologies

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 2.3 | La pile du Web sémantique — RDF, RDFS, OWL, JSON-LD, SHACL — et ce que chaque étage ajoute | pile | **A** |
| 2.1 | Les quatre régimes de compatibilité de schéma (T. 2.1) : quel sens de l'évolution chacun protège, producteur ou consommateur | schéma directionnel | **A** |
| 2.2 | Modèle canonique contre traduction point-à-point : le même geste qu'au ch. 1, sur les formats | deux graphes | B |
| 2.4 | GraphRAG : où le graphe s'insère dans la boucle de récupération | flux | B |

## Ch. 3 — Sécurité, identité et gouvernance de l'interopérabilité

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 3.2 | SAML, OAuth 2.x, OIDC : les trois rôles, qui délègue quoi à qui, et ce que chacun des trois protocoles couvre | séquence annotée | **A** |
| 3.3 | Du périmètre réseau au zero-trust : SPIFFE/SPIRE et l'identité de charge de travail | avant/après | **A** |
| 3.4 | Indicateur, objectif, accord de niveau de service (T. 3.1) : trois objets emboîtés que la pratique confond | emboîtement | B |
| 3.1 | Le modèle de menace de l'intégration et les dix familles OWASP API | carte de surface | B |
| 3.4 | Le cycle de vie d'un contrat d'interface, de la spécification à l'application à l'exécution | boucle | C |

## Ch. 4 — L'ingénierie des systèmes agentiques

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 4.2 | La boucle perception → raisonnement → action → observation, et le modèle augmenté qui la porte | boucle | **A** |
| 4.1 | Agent, *workflow*, automatisation : les régimes de contrôle et les niveaux d'autonomie — **siège de l'échelle** que trois autres chapitres citent | échelle | **A** |
| 4.3 | Du raisonnement linéaire à la recherche structurée : chaîne, arbre, recherche guidée par vérificateur | trois graphes | **A** |
| 4.2 | Contrôleur/exécuteur : les deux régimes de boucle et l'arbitrage qu'ils imposent (T. 4.1) | deux architectures | B |
| 4.4 | La chaîne d'appel d'outil et ses points de rupture | séquence | B |
| 4.1 | PEAS et la typologie de l'agent rationnel | grille | C |

## Ch. 5 — Ancrage informationnel

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 5.0 | Mémoire, contexte, récupération (T. 5.1) : trois objets que la pratique confond, leurs cycles de vie distincts | trois axes de temps | **A** |
| 5.3 | RAG statique contre RAG agentique : la boucle planifier-récupérer-critiquer-itérer | deux flux | **A** |
| 5.1 | La taxonomie de la mémoire — de travail, épisodique, procédurale, long terme | arbre | B |
| 5.1 | Compaction réversible, résumé, oubli actif : ce que chacun détruit et ce qu'il conserve | schéma de flux | B |
| 5.4 | Les deux axes d'évaluation d'un système de récupération (T. 5.2), à mesurer séparément | matrice | C |

## Ch. 6 — Systèmes multi-agents, évaluation et sûreté

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 6.1 | Les topologies de coordination (T. 6.1) et la propriété dominante de chacune | quatre graphes | **A** |
| 6.4 | *pass@k* contre *pass^k* : la courbe de consistance qui s'effondre là où le potentiel monte | graphe de fonction | **A** |
| 6.5 | Les patrons de défense architecturale et l'endroit de la boucle où chacun mord | boucle annotée | B |
| 6.3 | Le modèle comme juge : d'où viennent le biais et le piratage de récompense | flux | B |
| 6.1 | Le surcoût du multi-agent : ce que la coordination coûte contre ce qu'elle rend | schéma de bilan | C |

## Ch. 7 — Généalogie et gouvernance

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 7.3 | La chronologie 2024-2026 : dix-sept mois de consolidation, protocole par protocole | frise | **A** |
| 7.2 | Les quatre axes de l'interopérabilité agentique (T. 7.2) et le lieu de traitement de chacun dans la somme | quadrant | **A** |
| 7.5 | La collision « (agentic) control plane » à quatre branches (T. 7.3) : quatre objets, un seul nom | arbre de désambiguïsation | **A** |
| 7.2 | KQML → FIPA-ACL → actes de langage → engagements : la filiation, et ce qui n'a pas été repris | frise généalogique | B |
| 7.4 | Trois arrangements de gouvernance sous une destination commune | comparatif | B |
| 7.6 | « Soutien » n'est pas « production » : les degrés d'une métrique d'adoption | échelle | C |

## Ch. 8 — Anatomie : MCP et A2A
*Une figure en place (§ 8.1).*

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 8.6 | « Dans les agents, entre les agents » : l'axe vertical et l'axe horizontal, et qui déclare la complémentarité | schéma en croix | **A** |
| 8.4 | L'Agent Card signée et le modèle de tâche : anatomie d'un échange A2A | anatomie + séquence | **A** |
| 8.2 | Les cinq jalons en moins de deux ans (T. 8.3), et le cinquième non acquis au gel | frise | **A** |
| 8.3 | Registres, passerelles et découverte d'entreprise : le chemin d'un client jusqu'à un serveur | topologie | B |
| 8.5 | La convergence par fusion : ce que l'ACP protocolaire devient, et ce qui reste | avant/après | B |
| 8.1 | La trajectoire des transports (T. 8.2) : quatre étapes, un couplage qui décroît | frise | C |

## Ch. 9 — Découverte, registres, portabilité et pile protocolaire

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 9.2 | La pile agentique et ses quatre strates (T. 9.2), dont **une seule n'est pas empilable** | pile annotée | **A** |
| 9.1 | Les trois moments de la découverte (T. 9.1) que le monde des services web réduisait à un seul | frise de séquence | **A** |
| 9.5 | La pyramide d'évaluation à trois étages (T. 9.4), dont aucun ne supplée les autres | pyramide | **A** |
| 9.4 | L'écart entre accord de protocole et compréhension : où le sens se perd | schéma d'écart | B |
| 9.3 | Le paradoxe du verrouillage inverse : le standard de fait et ce qu'il ferme | schéma | B |
| 9.2 | La matrice de maturité et de décision (T. 9.3) | carte de chaleur | C |

## Ch. 10 — Transaction et infrastructure : AP2 et AGNTCY

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 10.3 | Les trois rôles que le commerce agentique dissocie (T. 10.1) — et ce que la dissociation fait tomber | schéma de rôles | **A** |
| 10.4 | Le mandat comme couche de preuve opposable : intention → mandat → transaction → litige | chaîne probatoire | **A** |
| 10.2 | AGNTCY : ce que la couche d'infrastructure porte, et où elle se pose sous les protocoles | pile | B |
| 10.5 | Les deux intervalles du dossier ACP (T. 10.3), calculés sur les seules dates | frise | B |
| 10.6 | Une prescription périmée par un événement postérieur de moins de quatre mois | frise | C |

## Ch. 11 — Modes d'échec et taxonomie des risques protocolaires

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 11.1 | La triade létale amplifiée : les trois capacités dont la réunion suffit | intersection | **A** |
| 11.1 | Les trois surfaces d'attaque (T. 11.3) distinguées par ce que chacune corrompt | schéma de surfaces | **A** |
| 11.2 | Les sept modes d'échec de la frontière interopérable (T. 11.4) placés sur la pile du ch. 9 | pile annotée | B |
| 11.1 | Empoisonnement, révocation après approbation, injection transitive : les trois familles sur une même chaîne | chaîne annotée | B |
| 11.4 | Confinement plutôt que prévention : ce que les protocoles couvrent et ce qui reste dehors | carte de couverture | **A** |

---

# Livre II — Faire confiance

## Ch. 12 — L'héritage et les standards étirés

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 12.1 | Un demi-siècle d'identités non humaines : compte de service → charge de travail → agent, et l'hypothèse humaine qui tombe | frise généalogique | **A** |
| 12.4 | L'agent dans OAuth : *client* ou détenteur de ressource ? Les deux placements, et ce que chacun casse | deux schémas | **A** |
| 12.3 | Identité stable, comportement variable : pourquoi le modèle hérité ne tient pas | schéma d'écart | B |
| 12.8 | Les trois degrés d'absence (T. 12.3) — l'échelle de preuve du volume, posée une fois | échelle | B |
| 12.5 | Quatre statuts de brouillon IETF et ce que leurs dates disent | frise de statuts | C |

## Ch. 13 — L'identité décentralisée : VC, DID

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 13.4 | SPIFFE/SPIRE, DID, WIMSE : où chacun ancre l'identité, et ce qu'aucun ne couvre | trois ancrages | **A** |
| 13.5 | Le fossé d'adoption : qui vérifie quoi, en production, à date — carte du vide | carte de couverture | **A** |
| 13.1 | Quatre documents du W3C, quatre stades (T. 13.1) | frise normative | B |
| 13.2 | La lacune de couverture des profils d'interopérabilité | schéma | C |

## Ch. 14 — La grille des cinq questions

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 14.1 | **La grille des cinq questions** (T. 14.1) et ce que chacune exige d'un mécanisme — instrument que dix chapitres invoquent | grille | **A** |
| 14.4 | Le croisement grille × échelle d'autonomie (T. 14.3) | matrice | B |
| 14.2 | L'application-témoin à trois mécanismes : la grille en action | matrice peuplée | B |

## Ch. 15 — Émettre : Agent Card, annuaires, registres

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 15.1 | Anatomie de l'Agent Card signée : les champs, la chaîne de signature, et **qui signe les signataires** | anatomie + chaîne | **A** |
| 15.3 | A2A normalise le chemin, AGNTCY spécifie le magasin : deux moitiés d'un même mécanisme | schéma complémentaire | **A** |
| 15.2 | Le risque de standard de fait : un annuaire commercial dominant qui fixe la norme sans passer par une norme | schéma | B |
| 15.1 | Révocation et durée de vie : ce qui expire, quand, et ce qui ne se révoque pas | frise | B |
| 15.2 | Les quatre statuts et ce que chacun autorise (T. 15.2) | échelle | C |

## Ch. 16 — Le passeport d'agent

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 16.1 | **Les quatre pièces du passeport** (T. 16.1) — objet de synthèse du Livre II | anatomie | **A** |
| 16.1 | La même anatomie en **état réel** (T. 16.2) : ce qui tient lieu de chaque pièce, et l'écart que le substitut laisse | anatomie annotée | **A** |
| 16.3 | Qui l'émettrait, qui le vérifierait : les rôles absents | schéma de rôles | B |
| 16.4 | Trois scénarios de normalisation | arbre | B |

## Ch. 17 — La chaîne de mandat et le problème des deux sauts

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 17.6 | **Le problème des deux sauts** : la chaîne, et l'endroit exact où chaque mécanisme perd le fil | chaîne à rupture | **A** |
| 17.2 | La chaîne de délégation comme objet de première classe : humain → agent → sous-agent → outil | chaîne | **A** |
| 17.4 | L'humain, premier et dernier maillon : la boucle qui se referme | boucle | B |
| 17.5 | Biais d'automatisation et supervision de façade : ce que le point d'arrêt ne garantit pas | schéma | B |
| 17.3 | Ce qu'un régime de mandat suppose contre ce que les mécanismes portent (T. 17.1) | comparatif | C |

## Ch. 18 — Know Your Agent

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 18.1 | Neuf chantiers, six organisations, **zéro texte ratifié** (T. 18.1) : la carte d'un chantier sans aboutissement | carte d'acteurs | **A** |
| 18.2 | Admettre un agent tiers : le point de décision, et tout ce que les protocoles y remettent à celui qui décide | schéma de décision | **A** |
| 18.3 | Trois précédents de fédération et ce que chacun porte d'institutionnel | comparatif | B |
| 18.4 | L'agent mutable prive la réputation de son ancrage | schéma | B |

## Ch. 19 — Taxonomie des attaques d'identité et de délégation

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 19.4 | Le tri des attaques **par le maillon qui cède** (T. 19.1) : la chaîne du ch. 17, chaque point de rupture annoté de ses attaques | chaîne annotée | **A** |
| 19.2 | Le modèle de menace agentique et l'impossibilité architecturale qu'il révèle | carte de surface | **A** |
| 19.5 | L'empoisonnement de la mémoire et des sources : le délai entre injection et effet | frise | B |
| 19.6 | Trois régimes d'absence côté protocolaire (T. 19.2) | échelle | C |

## Ch. 20 — Usurpation, révocation et boucle défensive

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 20.0 | Le *rug-pull* : **la particularité est le moment** — admission, usage, bascule, sur une seule ligne de temps | frise d'attaque | **A** |
| 20.6 | La révocation en cascade dans une chaîne de délégation : ce qui tombe, et ce qui reste debout | chaîne + propagation | **A** |
| 20.2 | Vérification à l'admission contre vérification continue : les deux régimes sur un axe de temps | deux frises | B |
| 20.4 | L'inventaire de la révocation, mécanisme par mécanisme (T. 20.1) | matrice de couverture | B |
| 20.9 | La symétrie attaque/défense relue par l'identité | schéma miroir | C |

## Ch. 21 — L'horloge post-quantique

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 21.9 | **La fenêtre d'action 2026-2029, calendrier inverse** : partir de l'échéance et remonter jusqu'à aujourd'hui | frise à rebours | **A** |
| 21.2 | *Harvest now, decrypt later* : la durée de vie d'un artefact d'identité comparée à l'horloge de la menace | deux axes de temps | **A** |
| 21.3 | Inventaire de migration par artefact (T. 21.2) : quoi casse, quand | matrice datée | B |
| 21.5 | Audit de crypto-agilité, mécanisme par mécanisme (T. 21.3) | carte de chaleur | B |
| 21.8 | La méthode d'inventaire pour une institution | flux | C |

---

# Livre III — Encadrer

## Ch. 22 — Options d'orchestration et paradigme APM

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 22.1 | **OO1-OO4 sur les deux axes qui les ordonnent** (T. 22.1) — instrument central du Livre III | matrice 2×2 | **A** |
| 22.6 | La ligne de partage entre autonomie et automatisation : de quel côté tombe quoi | schéma de partage | **A** |
| 22.9 | Les frames locaux comme frontière de sécurité : ce qui est dedans, ce qui est dehors | schéma de périmètre | B |
| 22.7 | Frames normatifs, frames opérationnels, trois scénarios (T. 22.2) | comparatif | B |
| 22.5 | Orchestration déterministe et orchestration agentique — la charnière | schéma de charnière | B |
| 22.10 | L'écart de responsabilité : qui répond de ce que personne n'a décidé | schéma de trou | **A** |

## Ch. 23 — Les frameworks d'orchestration d'entreprise

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 23.5 | Les patrons livrés **situés sur la matrice OO1-OO4** (T. 23.2) : la même figure qu'au 22.1, peuplée | matrice peuplée | **A** |
| 23.1 | Les cinq offres et le régime de preuve de leur support protocolaire (T. 23.1) | matrice de statuts | B |
| 23.3 | L'orchestration événementielle : le journal avant le cadre | schéma | C |

## Ch. 24 — Le passage à l'échelle de l'entreprise

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 24.1 | **L'agent comme acteur du tissu d'intégration** : où il se branche sur l'existant — passerelle, bus, maillage d'événements | architecture | **A** |
| 24.3 | Le cycle de vie de l'identité d'agent à l'échelle du parc | cycle | **A** |
| 24.5 | Les trois échelles d'orchestration (T. 24.1), ordonnées par structure de propriété | trois périmètres | **A** |
| 24.1 | Encapsuler le patrimoine : ordinateur central et progiciel exposés comme outils gouvernés | schéma d'encapsulation | B |
| 24.6 | Le modèle de menace du parc : injection indirecte et fuite sans clic | carte de surface | B |
| 24.9 | La transposition du modèle de maturité (T. 24.2) | échelle | C |
| 24.8 | Budget de latence et contention : où le temps se dépense dans une boucle agentique | schéma de budget | B |

## Ch. 25 — E-23 : le risque de modèle à l'ère de l'IA

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 25.1 | Genèse et calendrier d'E-23 jusqu'au **1ᵉʳ mai 2027** | frise | **A** |
| 25.3 | L'inférence agentique : comment un texte qui ne nomme pas l'agent l'attrape quand même | schéma de qualification | **A** |
| 25.4 | La lecture **inversée** de la grille des cinq questions sur E-23 (T. 25.1) | grille inversée | B |
| 25.6 | La surveillance continue attendue, et la limite empirique de la supervision humaine | schéma d'écart | B |

## Ch. 26 — Le vide fédéral : de C-27 à C-36

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 26.3 | **Le vide et ce qui le comble par défaut** : la mort de C-27, l'attente de C-36, et les quatre instruments sectoriels qui portent la charge (T. 26.1) | frise + report de charge | **A** |
| 26.2 | Le ministre de l'IA et le périmètre annoncé de C-36 | schéma | C |

## Ch. 27 — Québec : ligne directrice AMF et article 12.1

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 27.2 | **L'articulation de l'article 12.1** (T. 27.2) : une obligation inconditionnelle, trois informations dues sur demande, un alinéa distinct | arbre d'obligation | **A** |
| 27.3 | Le critère « exclusivement » : l'arbre de décision qui déclenche ou non le régime | arbre de décision | **A** |
| 27.6 | Le mandat agentique en droit civil québécois : ce que l'analogie porte, où elle casse | schéma d'analogie | B |
| 27.7 | Cartographie des lectures, sans verdict (T. 27.4) | carte de positions | B |
| 27.1 | Les trois positions du dépôt sur une même date (T. 27.1) | frise | C |

## Ch. 28 — Valeurs mobilières : l'avis ACVM 11-348

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 28.2 | Autonomie et adaptativité comme accroche : ce que la définition attrape, ce qu'elle laisse | schéma de définition | B |
| 28.1 | Un texte qui ne crée rien, et dont la portée est la plus large : périmètre contre effet | schéma de périmètre | B |

## Ch. 29 — Le pont : des contraintes réglementaires aux frames déterministes

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 29.1 | **La table de traduction** (T. 29.1) : exigence réglementaire → contrainte de frame, chaque lien nommé | schéma de traduction | **A** |
| 29.3 | L'imputabilité : qui répond du comportement émergent — la chaîne des responsables | chaîne | B |
| 29.4 | Rendre la condition 2 exécutable : le test, et ce qu'il n'est pas | schéma de test | B |

## Ch. 30 — Le maillage réglementaire international

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 30.2 | **La grille de qualification multiple** (T. 30.1) : système TIC, modèle, décision automatisée — un agent peut tomber sous les trois | intersection | **A** |
| 30.2 | Le maillage UE / US / Canada-Québec : les instruments par juridiction, sur un même axe de calendrier | frise à couloirs | **A** |
| 30.1 | Qualification sous l'AI Act et calendrier d'application, report adopté compris | frise | B |
| 30.3 | Les instances de normalisation et l'état de leurs travaux sur l'identité d'agent (T. 30.3) | carte d'acteurs | B |
| 30.3 | Scénarios de désignation et leurs conséquences sur la pile identitaire | arbre | B |

## Ch. 31 — Le vertical financier

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 31.1 | **La double-qualification** : l'agent comme MODÈLE et comme TIERS TIC — siège du patron pour toute la somme | schéma double | **A** |
| 31.5 | **Les quatre plans où circule la donnée régulée** (T. 31.4) : inférence, plongements, traces, journaux d'audit — la résidence doit couvrir les quatre | schéma de circulation | **A** |
| 31.2 | Les trois couches du substrat sémantique financier (T. 31.2) | pile | **A** |
| 31.1 | Irréversibilité et finalité du règlement : le point de non-retour sur la chaîne de paiement | chaîne à seuil | **A** |
| 31.3 | Ségrégation des tâches et quatre-yeux appliqués à des agents : qui ne peut pas être qui | schéma de séparation | B |
| 31.4 | La triade létale rencontre l'irréversibilité financière | intersection | B |

## Ch. 32 — Le cadre des services bancaires axés sur le consommateur

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 32.4 | **La chaîne loi → accréditation → registre → standard technique, et le maillon absent** — le fait négatif vérifié du chapitre | chaîne à trou | **A** |
| 32.1 | De la loi partielle de 2024 à C-15 : abrogation, remplacement, mobilité des données | frise | B |

## Ch. 33 — ISO 20022 : Lynx accompli, RTR visé

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 33.2 | La chronologie du rail en temps réel (T. 33.1) : les cibles annoncées et les reports, superposés | frise à reports | **A** |
| 33.4 | Ce que la couche sémantique commune change entre deux rails | schéma | B |
| 33.3 | *By-law no 10* : l'instrument juridique précède le rail | frise | C |

## Ch. 34 — Les sous-domaines financiers

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 34.3 | **La souscription vie accélérée comme chaîne d'orchestration régulée** : les maillons, et où le régime mord | chaîne annotée | **A** |
| 34.2 | Sinistres et fraude : l'agent orchestrateur d'une chaîne, du premier avis au règlement | chaîne | **A** |
| 34.1 | Le tri bancaire par régime d'usage : détail, gros, paiements, crédit, cœur de système | carte de domaines | **A** |
| 34.4 | L'architecture fédérée à registre de capacités en gestion de patrimoine | architecture | B |
| 34.6 | Les sept questions ouvertes et l'exigence d'architecture de chacune (T. 34.2) | matrice | B |
| 34.4 | Conseiller automatisé classique contre agent : la désambiguïsation impérative | comparatif | B |
| 34.5 | La façade gouvernée sur le cœur bancaire | schéma d'encapsulation | C |

## Ch. 35 — Études de cas : la production agentique canadienne

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 35.9 | **Huit institutions × régime de preuve × maturité déclarée** : la carte du chapitre entier, avec les absences | carte de chaleur | **A** |
| 35.0 | Les trois classes d'accès documentaire (T. 35.1) — l'échelle qui commande la lecture de tout le chapitre | échelle | **A** |
| 35.9 | Ce que cinq dispositifs de gouvernance ont en commun | intersection | B |

## Ch. 36 — Prospective : AP2 sur les rails canadiens ?

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 36.2 | La stratification de la chaîne de paiement (T. 36.1), avec **l'erreur de lecture que la figure doit empêcher** | pile annotée | **A** |
| 36.2 | Litige, rétrofacturation et le trou de responsabilité : la chaîne, et l'endroit où personne ne répond | chaîne à trou | **A** |
| 36.2 | Le mandat vérifiable comme exigence issue de l'irréversibilité | schéma de dérivation | B |
| 36.3 | Les conditions de possibilité, ordonnées par ce qui bloque quoi | graphe de dépendances | B |

---

# Livre IV — Appliquer, exploiter, produire et composer

## Ch. 37 — Le maillage d'agents : PEP/PDP et *zero trust* agentique

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 37.5 | **PEP et PDP agentiques** : où se prend la décision, où elle s'applique, et ce que le point d'application ne couvre pas | architecture annotée | **A** |
| 37.8 | Ce que le maillage voit sur la chaîne de mandat, et les trois choses qu'il ne peut pas suppléer | chaîne + périmètre | **A** |
| 37.7 | De « jamais confiance au réseau » à « jamais confiance au graphe » : la transposition zero-trust | avant/après | **A** |
| 37.3 | La non-compositionnalité de la sûreté : deux arêtes sûres, un chemin qui ne l'est pas | contre-exemple | **A** |
| 37.2 | Trois offres, trois statuts auto-déclarés (T. 37.1) | comparatif | B |
| 37.9 | Les cinq conditions de réfutation du chapitre (T. 37.3) | liste graphique | C |

## Ch. 38 — L'observabilité agentique

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 38.3 | **La propagation de trace à travers les frontières d'agents**, et l'endroit où le contexte se perd | séquence + rupture | **A** |
| 38.5 | Corréler la trace au passeport : l'identité comme clé de jointure entre deux mondes | schéma de jointure | **A** |
| 38.1 | Ce que l'APM classique couvre, et où l'agent la déborde | deux périmètres | B |
| 38.4 | Ce qu'une trace devrait porter pour valoir pièce de conformité, et ce que le socle en dit | anatomie annotée | B |
| 38.2 | L'échelle de maturité des conventions sémantiques (T. 38.1) | échelle datée | C |

## Ch. 39 — Le cycle de vie opérationnel

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 39.2 | **Les quatre dérives** — modèle, outil, autonomie, et la quatrième portée par le plan — avec le degré de documentation de chacune | quatre axes | **A** |
| 39.3 | Révoquer, confiner, imputer : la séquence de réponse à incident agentique | séquence | **A** |
| 39.4 | GitOps du parc : versionner le mandat, promouvoir, revenir en arrière | boucle | B |
| 39.1 | Des jeux d'essai à l'évaluation continue : ce qui bascule | avant/après | B |
| 39.5 | Ce que le passeport date, et ce qu'il ne date pas, quand l'agent apprend | frise | B |

## Ch. 40 — Les indicateurs de l'AgentOps et le FinOps des agents

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 40.2 | **La grille minimale à quatre grandeurs** (T. 40.2) et ce que chacune répond à l'auditeur | grille | **A** |
| 40.6 | Du coût par jeton au coût par résultat métier : pourquoi la première grandeur trompe | deux barèmes | **A** |
| 40.5 | Le modèle de coût agentique : où le budget part dans une boucle | schéma de budget | B |
| 40.4 | Les indicateurs de la supervision humaine, et ce qu'ils ne mesurent pas | grille | B |
| 40.3 | L'horizon de tâche déléguée : l'état d'un front ouvert | graphe | C |

## Ch. 41 — La fabrique d'agents

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 41.5 | **La boucle de réémission** : indicateur et dérive → gabarit corrigé → parc réémis | boucle | **A** |
| 41.3 | Registre gouverné et catalogue interne (T. 41.2) : deux objets, deux autorités | schéma double | **A** |
| 41.4 | La barrière de certification : ce qu'un agent démontre avant d'être admis au maillage | porte à conditions | **A** |
| 41.1 | Les quatre emplois du mot « fabrique » dans la somme (T. 41.1) | désambiguïsation | B |
| 41.6 | La fabrique comme point de concentration : ce qu'elle centralise, ce qu'elle fragilise | schéma de risque | B |

## Ch. 42 — La matrice protocoles × exigences réglementaires

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 42.1 | **La matrice protocoles × textes canadiens** (T. 42.1) : la couverture, et surtout les cases vides | carte de chaleur | **A** |
| 42.3 | Les trois espèces de vide, et **le renversement** — le résultat le plus utile du chapitre | schéma de renversement | **A** |
| 42.4 | Les cinq zones de compensation architecturale (T. 42.2) : ce que l'architecture doit porter là où le protocole ne porte rien | carte de compensation | **A** |

## Ch. 43 — L'architecture de référence unifiée par couches

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 43.1 | **Les six couches de l'architecture de référence** (T. 43.1) — figure maîtresse de la somme, celle que le § 24.2.1 doit pouvoir citer | pile | **A** |
| 43.3 | Les cinq points de contrôle obligatoires, posés sur les six couches | pile annotée | **A** |
| 43.2 | Quand agentifier, quand s'abstenir : l'arbre de décision | arbre de décision | **A** |
| 43.5 | Les trois échelles d'autonomie homonymes (T. 43.3) : « copilote » ne désigne pas la même chose trois fois | désambiguïsation | **A** |
| 43.5 | Le croisement des quatre paliers de maturité avec trois couches (T. 43.4) | matrice | B |
| 43.4 | Le plan de contrôle d'agents comme architecture de référence | architecture | B |

## Ch. 44 — La formalisation ArchiMate
⚠ **Le gisement le plus important du volume, et le plus anormal** : un chapitre dont l'objet est un langage graphique, composé sans une seule figure. Les huit patrons de § 44.1 sont des diagrammes décrits en prose.

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 44.1 | **Les huit patrons de modélisation** — agent, appel d'outil, interaction agent-agent, identité non humaine, plan de contrôle, humain-agent, mémoire — **un diagramme chacun** | 8 diagrammes ArchiMate | **A** |
| 44.8 | Les neuf anti-patrons et leurs corrections (T. 44.2) : avant / après, côte à côte | 9 paires | **A** |
| 44.0 | Le cadre ArchiMate : domaines × aspects, et où les concepts agentiques se posent | grille du cadre | **A** |
| 44.1 | Le verrou méthodologique : aucun élément natif, et ce que la spécialisation coûte | schéma | B |
| 44.6 | Les points de vue transverses et ce que chacun découpe | schéma de vues | B |
| 44.9 | Le formalisme face aux systèmes autonomes : ce qu'ArchiMate ne sait pas dire | carte de limite | B |

## Ch. 45 — Le blueprint instancié et son cycle de vie

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 45.8 | **Naissance, vie, mort d'un agent d'entreprise** : enregistrement → passeport → admission → délégations → révocation → archivage | frise de cycle de vie | **A** |
| 45.11 | Flux 1 — la décision de crédit assistée par agents : le processus commande | séquence | **A** |
| 45.12 | Flux 2 — le paiement normalisé vers le rail de grande valeur : l'agent observe, le rail exécute | séquence | **A** |
| 45.14 | L'exemple de bout en bout : souscription vie augmentée, et sa variante en sinistres | séquence longue | **A** |
| 45.2 | La vue en couches C1-C8 avec statuts datés (T. 45.2) | pile datée | **A** |
| 45.13 | Flux 3 — concevoir contre une norme qui n'existe pas encore | séquence à trou | B |
| 45.4 | La correspondance réglementaire développée (T. 45.3) | matrice | B |
| 45.1 | Les six principes directeurs et ce qui porte chacun (T. 45.1) | grille | C |

## Ch. 46 — Instrumentation et feuille de route vers le 1ᵉʳ mai 2027

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 46.2 | **Le compte à rebours au 1ᵉʳ mai 2027** : inventorier, coter-encadrer, surveiller — trois mouvements sur l'axe qui reste | frise à rebours | **A** |
| 46.3 | Les jalons externes à surveiller (T. 46.2), **un seul étant PROGRAMMÉ** | frise à régimes | **A** |
| 46.1 | Les trois rapprochements plausibles entre métriques académiques et indicateurs de risque-modèle, et pourquoi aucun n'est documenté | schéma de lien non établi | B |

---

# Livre V — Livrer et clore

## Ch. 47 — L'artefact livré : provenance et mise en service

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 47.1 | **Les cinq composants d'un agent et leurs cinq horloges** (T. 47.1) — anatomie et versionnement en une seule figure ; le § 47.8 y renvoie | anatomie + horloges | **A** |
| 47.4 | Le *rug-pull* du ch. 20 relu comme défaut de provenance : la même attaque, vue de l'autre bout | schéma miroir | **A** |
| 47.10 | Promotion par environnements et retour arrière d'un artefact **à état** | flux + retour | B |
| 47.2 | Les cinq documents de nomenclature et ce que chacun couvre (T. 47.2) | matrice de couverture | B |
| 47.7 | L'extension déclarative : le composant que la nomenclature ne voit pas | schéma d'angle mort | B |

## Ch. 48 — La sémantique d'effet

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 48.2 | **Livraison au-moins-une-fois + consommateur idempotent = traitement exactement-une-fois** : le seul montage qui tienne sous pannes | schéma de composition | **A** |
| 48.3 | Compensation et sagas au grain de l'agent : la séquence, et le chemin de compensation quand elle échoue à mi-parcours | séquence + compensation | **A** |
| 48.1 | Les trois classes d'effet d'une action d'agent (T. 48.1) | taxonomie | **A** |
| 48.4 | La réconciliation des flux financiers : où l'écart se détecte et qui le porte | flux | B |
| 48.5 | Tracer l'effet, pas seulement l'appel : les deux niveaux de trace | deux couches | B |

## Ch. 49 — L'horizon 2027-2032

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 49.1 | **La grappe d'échéances 2027-2032** : le squelette daté, avec la concentration de 2027 | frise maîtresse | **A** |
| 49.0 | **Le cône d'incertitude** et les trois statuts épistémiques — la figure qui commande la lecture du chapitre entier | cône annoté | **A** |
| 49.11 | Trois axes, et les futurs qui s'y lisent différemment | espace de scénarios | **A** |
| 49.12 | Les lacunes résiduelles du socle : 11 du Vol. II + 22 du Vol. III + 3 au degré 3, par chapitre porteur | carte de lacunes | B |
| 49.2 | Convergence ou coexistence stratifiée gouvernée : deux trajectoires de protocoles | deux arbres | B |
| 49.13 | Les questions de recherche transmises, avec leur critère de clôture | carte d'agenda | B |
| 49.3 | La bifurcation de la gouvernance par couche | arbre | C |

## Ch. 50 — Péremption et protocole de revalidation

| § | Ce que la figure montre | Type | |
|---|---|---|---|
| 50.4 | **La carte de fraîcheur de la somme** : les 50 chapitres, colorés par date de gel — ce qui est frais et ce qui ne l'est plus, d'un seul regard | carte de chaleur | **A** |
| 50.2 | Les onze événements de péremption (T. 50.1) sur l'axe du temps, avec leur trace | frise | **A** |
| 50.3 | Le protocole de revalidation : la boucle, et son déclencheur | boucle | **A** |
| 50.1 | Les lacunes propres au blueprint | carte | C |

---

## Premier lot recommandé — douze figures

Choisies pour le rapport entre l'effort de dessin et le nombre de pages qu'elles éclairent. Les six premières sont des **instruments** que d'autres chapitres invoquent sans les redessiner.

| | § | Figure | Sert aussi |
|---|---|---|---|
| 1 | 14.1 | La grille des cinq questions | ch. 15, 16, 19, 25, 27, 37 |
| 2 | 22.1 | OO1-OO4 sur ses deux axes | ch. 23, 43 |
| 3 | 43.1 | Les six couches de l'architecture de référence | ch. 24, 44, 45 |
| 4 | 4.1 | L'échelle d'autonomie et les régimes de contrôle | ch. 22, 39, 43 |
| 5 | 16.1 | Les quatre pièces du passeport | ch. 15, 38, 45, 47 |
| 6 | 17.6 | La chaîne de mandat et le problème des deux sauts | ch. 19, 20, 37 |
| 7 | 44.1 | Les huit patrons ArchiMate | le chapitre entier |
| 8 | 45.8 | Naissance, vie, mort d'un agent | ch. 39, 41, 47 |
| 9 | 4.2 | La boucle agentique | ch. 5, 6, 11 |
| 10 | 11.1 | La triade létale amplifiée | ch. 19, 24, 31 |
| 11 | 49.1 | La grappe d'échéances 2027-2032 | ch. 21, 25, 34, 46, 50 |
| 12 | 6.4 | *pass@k* contre *pass^k* | ch. 39, 40 |
