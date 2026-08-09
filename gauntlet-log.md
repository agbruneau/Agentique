# Journal de la boucle — refonte de la veille technologique, août 2026

Append-only. Un bloc par tour. Sert à décider quand arrêter, pas à raconter le travail.

## Cadrage

**Objectif.** Actualiser la veille au 8 août 2026, puis la ramener à **100 pages fermes**,
gabarit inchangé, sans perdre un fait vérifié.

**La barre** (choix de l'auteur). *La veille de 162 pages elle-même, section par section.* Le juge
reçoit la même section dans les deux versions, étiquettes retirées, et désigne celle qui sert le
mieux un architecte d'entreprise pressé. Raccourcir ne suffit pas : il faut gagner.

**Méthode retenue.** Compression éditoriale seule — 11 pt, marges inchangées. Aucun gain
typographique.

**Régime d'actualisation retenu.** Re-vérification intégrale des 269 références, plus une passe de
veille sur la fenêtre 29 juillet → 8 août 2026.

## État de départ, mesuré le 8 août 2026

| Mesure | Valeur |
|---|---|
| Pagination (`/Count` de `/Type /Pages`) | 162 p. |
| Mots | 82 227 (corps 70 556, biblio 10 980, tête 691) |
| Références | 269, toutes citées |
| `check-veille.py` | sortie 0 — 94 sections, 15 tableaux, 25 questions ouvertes |
| Appareil seul (titre + résumé + biblio, sans corps) | **29 p.** — sonde du 8 août |
| Densité du corps | ≈ 545 mots/page |

**Budget qui en découle.** 100 − 29 (appareil) − 3,5 (sommaire) ≈ **67,5 p. de corps**, soit
**≈ 36 800 mots** contre 70 556. *Le corps doit perdre 48 % de ses mots à faits constants.*

## Invariants — ce qu'aucun bâtisseur ne peut toucher

Ils ne relèvent pas du goût : chacun casse un contrôle exécutable de `check-veille.py`.

1. **Aucun titre de section n'est supprimé, ajouté, déplacé ou renuméroté.** Les numéros sont
   positionnels ; en déplacer un périme tous les renvois « section 4.11.5 » du document.
2. **Aucun tableau n'est supprimé, et chacun garde sa légende.** Une légende perdue décale tous les
   « tableau N » cités en aval.
3. **Les trois listes cardinales gardent leur compte** : 12 constats au sommaire exécutif,
   14 contributions, 25 questions ouvertes. Comprimer chaque entrée, jamais en fusionner deux.
4. **Un appel de référence `[N]` ne disparaît que si le fait qu'il porte disparaît.** Toute
   référence orpheline est retirée de la bibliographie et l'ensemble renuméroté — au recollage,
   jamais dans le morceau.
5. **Une source nouvelle ne prend jamais un numéro.** Le bâtisseur écrit
   `[[NOUVEAU: url | titre | date]]` ; la numérotation est centrale.

---
## Tour 1 — onze morceaux, bâtisseurs à contexte neuf

Onze bâtisseurs en parallèle, un par morceau jugeable, chacun avec son quota de mots et la fiche
des faits d'août. Quatre ont livré dans leur quota ; sept ont été coupés par une erreur d'API
**pendant leur passe de resserrage** — leurs brouillons étaient écrits, pas resserrés.

**Mesure : 162 → 131 pages.** Structure intacte (97 titres au caractère près), mais cinq tableaux
ajoutés au lieu des deux autorisés, ce qui décale la numérotation de tous les renvois en aval.

## Tour 2 — resserrage des sept morceaux en dépassement

Sept bâtisseurs neufs, quota **dur** et mesure exigée avant reddition. Tous rentrés.
Douze appels de référence abandonnés avec leurs faits, sept entrées devenues orphelines.

**Mesure : 131 → 103 pages.**

## Réconciliation centrale — ce qu'aucun bâtisseur ne pouvait faire

Trois gestes dépendent du document entier, pas d'un morceau :

1. **81 marqueurs de source nouvelle** ramenés à 69 URL distinctes, puis à 41 entrées — trois
   d'entre elles pointant vers des entrées **déjà au corpus** (AAuth, documents WIMSE, dépôt AP2).
   *C'est exactement le doublon que le contrôle de publication signale ; le détecter avant lui
   plutôt qu'après est la seule différence.*
2. **Sept entrées orphelines retirées**, bibliographie renumérotée de façon contiguë, 269 → **303**.
3. **Seize renvois « tableau N » recalibrés** : la numérotation de Pandoc est positionnelle, et
   trois tableaux ajoutés en amont périment tous les renvois en aval.

Puis resserrage final de C, E, F et I. **Mesure : 100 pages fermes.** `check-veille.py` en sortie 0.

## Comparaison à l'aveugle — quatre morceaux, ordre alterné

Quatre juges à contexte neuf. Chacun reçoit deux textes étiquetés ALPHA et BÊTA, sans savoir lequel
est lequel ni lequel est le plus récent ; l'ordre alterne d'un morceau à l'autre pour qu'aucun juge
ne puisse apprendre la position. Consigne explicite : **la fraîcheur des faits n'est pas un
critère** — sinon le verdict est acquis d'avance et ne mesure plus la compression.

| Morceau | Notre version en | Verdict | Motif retenu |
|---|---|---|---|
| A — ouverture | BÊTA | **gagne** | « 414 serveurs, 68 vulnérabilités, 91,8 % sans OAuth » contre « les attaques démontrées expérimentalement » |
| E — orchestration | ALPHA | **gagne** | statut produit en colonne ; le 70 % de Gartner déclaré *inattribuable* au lieu d'être relayé |
| H — identité | BÊTA | **gagne** | « aucun mécanisme *normalisé* », les trois brouillons nommés, le déficit daté |
| K — clôture | ALPHA | **gagne** | la décision de citation tombe en seize lignes ; divulgation vérifiée non affaiblie |

**Quatre sur quatre. C'est la condition de sortie de la boucle.**

### Les quatre écarts rendus par les juges, et ce qu'on en a fait

| Écart | Sort |
|---|---|
| **E** — trois légendes annoncent « état vérifié au 15 juillet 2026 » alors que leurs lignes portent des faits d'août | **corrigé** — les légendes datent désormais les deux passes. *C'est un défaut de rigueur, pas de style : exactement la classe d'écart que ce document prend pour objet.* |
| **A** — les contributions 2, 3 et 5 comprimées jusqu'à n'être plus que des étiquettes de sujet | **corrigé** — chacune annonce de nouveau un résultat |
| **H** — sources humaines désindexées : `[3]` sans nom d'auteur en « Menaces documentées » | **arbitré, non corrigé** — à 100 pages, ce qui laisse juger de la solidité d'un résultat empirique est *n* et la méthode, tous deux au texte ; l'identité des auteurs est à un renvoi |
| **K** — le Vol. IV déclaré « arrêté » sans le régime de preuve qui le qualifierait | **arbitré, non corrigé** — le régime du Vol. IV est au Vol. IV ; la veille en rend le verdict de citabilité, non le calcul |

## État de sortie, mesuré le 8 août 2026

| Mesure | Départ | Arrivée |
|---|---|---|
| Pagination (`/Count`) | 162 p. | **100 p.** |
| Corps | 70 552 mots | **29 525 mots** (−58 %) |
| Bibliographie | 269 entrées | **303 entrées** |
| Tableaux | 15 | 18 |
| Sections, questions ouvertes | 94 / 25 | 94 / 25 — inchangés |
| `check-veille.py` | sortie 0 | **sortie 0** |

**Ce que la boucle n'a pas fait.** Elle n'a pas soumis au jugement à l'aveugle les **sept** morceaux
restants (B, C, D, F, G, I, J) : quatre verdicts concordants ont suffi à conclure, et poursuivre
aurait coûté sans informer. *C'est un plafond, et il est déclaré ici plutôt que tu.*

## Audit intégral de la bibliographie — le régime fort demandé

Neuf agents, grappes de trente entrées, **269 références rouvertes une à une sur leur source
primaire**. Cette passe avait été lancée au premier tour et **tuée avec le processus sans écrire une
ligne** ; elle a été rejouée, parce que la veille en déclare l'existence en §2.2 — *une revue qui
annonce une vérification qu'elle n'a pas faite est précisément ce que ce document combat.*

| Verdict | Entrées |
|---|---|
| Confirmée telle quelle | **179** |
| Corrigée | **54** |
| Non reconfirmable | **30** — dont **16 par refus de consultation automatisée** (HTTP 403 : ISO, Gartner, IDC, OpenAI, Salesforce, OCDE, ACM, IBM, `lautorite.qc.ca`), les 14 autres par page sans date, mouvante, rendue en script, ou expirée |
| Auto-citation, non vérifiable sur le Web | 6 |
| Introuvable | **0** |

**Les corrections qui changeaient un fait, et non un titre, ont été appliquées** : l'article 12.1 de
la Loi 25 dont l'adresse citée visait une page du **secteur public** ; un communiqué d'Appian
d'avril 2025 auquel deux faits d'un communiqué d'avril **2026** avaient été prêtés ; la disponibilité
générale du connecteur MCP de Camunda, **que les notes de version n'énoncent nulle part** ; deux
réserves devenues caduques ; quatre brouillons IETF avancés d'une révision ; un correctif du NIST
qui n'existe pas ; deux préimpressions **publiées depuis en comité de lecture** ; et la pagination du
Vol. IV, 857 pages à la date de consultation, 1 114 aujourd'hui.

### Un désaccord entre agents, tranché par énumération

Deux agents de cette passe ont rendu **deux décomptes différents** du fait négatif le plus cité du
document — les attributs `gen_ai.*` d'OpenTelemetry : **63** pour l'agent d'exploitation, **77** pour
l'agent d'audit. Une troisième récupération directe du registre a **énuméré nominativement 63
identifiants**, et confirmé qu'aucun ne décrit une délégation, un mandat ni un donneur d'ordre.
*Un décompte n'accepte qu'une preuve — la liste. Les deux nombres non énumérés ont été écartés, y
compris celui qui venait de mon propre agent.*

## Reprise finale

Les corrections d'audit ont repoussé le document à 101 pages. Les 430 mots manquants ont été repris
dans `§13.9`, la sous-section que le juge du morceau K avait désignée comme la plus dispensable —
*l'écart relevé à l'aveugle a donc servi deux fois : à corriger, puis à choisir où couper.*

**État final : 100 pages, 303 références, `check-veille.py` en sortie 0.**

## Reprise de mise en page — le budget que rien ne voyait

L'auteur signale que le résumé de la page 1 doit être lisible sur une seule page. **Il ne l'était
pas, et rien ne le disait.** Le gabarit Typst compose le résumé dans un bloc **qui ne se scinde
pas** : ce qui dépasse n'est pas reporté à la page suivante, il est **rogné sous la marge**, et
`pandoc` sort 0. En rallongeant le résumé pour y porter les résultats de l'édition, cette passe
avait fait tomber sa dernière ligne à **y = −27,2 pt — 100,8 pt sous la marge basse**, soit une
dizaine de lignes composées hors page.

| | Avant | Après |
|---|---|---|
| Résumé | 3 513 caractères | **2 656** |
| Dernière ligne de la page 1 | **y = −27,2 pt** | **y = 119,4 pt** |
| Dégagement sous la marge (73,7 pt) | **−100,8 pt** | **+45,7 pt** |

*Référence : l'édition de 162 pages tenait à 2 762 caractères et 31,1 pt de dégagement.* La nouvelle
version est donc plus courte **et** mieux dégagée qu'elle.

**Le correctif de fond n'est pas la coupe, c'est le contrôle.** [`check-resume.py`](check-resume.py)
décompresse le flux de la page de titre et relève l'ordonnée la plus basse où du texte est
effectivement posé. Deux pièges l'ont fait mentir avant de le faire dire vrai, et sont documentés
dans le fichier : `/Type/PageLabel` contient `/Page`, et **le gabarit ne met pas la position dans la
matrice de texte** — `Tm` y vaut `1 0 0 -1 0 0`, la position réelle étant dans le `cm` qui précède
chaque `BT`. *Mesurer `Tm` rendait zéro partout, ce qui ressemblait à un résultat.* Le contrôle est
**calibré sur le PDF de l'édition précédente**, où il retrouve les 104,8 pt relevés à la main
le 29 juillet 2026 — c'est cette concordance qui le rend croyable, non son code.

## Revue de littérature — 9 août 2026

Demande d'auteur : *« fondée sur le contenu de la veille, effectuer la revue littéraire
correspondante pour août 2026 »*. Corpus retenu : socle de la veille **plus** passe académique
neuve ; livrable autonome à appareil complet ; **40 pages fermes**.

Neuf agents de recherche, un par front, à consigne de source primaire exclusive et d'ouverture de
chaque notice. Puis — et c'est le geste qui a fait la revue — **les métadonnées des 158 pièces arXiv
ont été reprises à l'API du dépôt**, ce qui a corrigé plusieurs statuts que les agents rapportaient
comme « à comité de lecture » sur la seule foi du champ de commentaire libre.

| Mesure | Valeur |
|---|---|
| Corpus | **161 entrées** — 50 du socle, 108 de la passe neuve, 3 à DOI |
| Publication attestée en notice | **12 / 158 (8 %)** |
| Acceptation annoncée au seul champ libre | 26 / 158 (16 %) |
| Aucun signe de revue par les pairs | **120 / 158 (76 %)** |
| Déposées en 2026 | 91 / 158 (58 %) ; **81 encore en v1** |
| Pagination | **40 p.** fermes |
| `check-revue.py` | **sortie 0** — 4 contrôles, 4 mutants tombent |

### Deux erreurs de mesure trouvées et corrigées en cours de route

**La première était mienne.** J'avais posé qu'une publication n'est attestée que par le champ
`journal_ref`, ce qui donnait 7 pièces sur 158. Le champ DOI en atteste tout autant : le compte juste
est **12**. L'écart a été trouvé en confrontant les notices aux entrées, et il est **rapporté au
texte de la revue** plutôt que corrigé en silence. *Trois de mes entrées à DOI étaient par ailleurs
des doublons de pièces arXiv déjà au corpus — exactement le doublon que le contrôle détecte.*

**La seconde était dans le contrôle.** Sa première version développait les plages citées en prose
— « [51-63] » — pour l'appariement. Or ces plages couvrent l'intégralité de la bibliographie :
orpheliner une entrée ne faisait plus tomber le contrôle. *Un contrôle incapable d'échouer sur le
défaut qu'il prétend couvrir ne vaut rien ; il a fallu le voir passer sur un mutant pour le voir.*
La règle corrigée exige un appel **nommé** pour chaque pièce de la passe neuve — et elle a
immédiatement révélé une propriété réelle du document : **111 des 111 pièces neuves sont discutées
une à une, mais 27 des 50 pièces du socle ne le sont jamais**, seulement couvertes par leur plage.
Cette asymétrie est désormais au texte de la revue.

---

# Journal de la boucle — chorégraphie en essaim, 9 août 2026

## Cadrage

**Objectif.** Intégrer à la revue de littérature le concept de **chorégraphie agentique en essaim
multiagents** — la coordination sans chef d'orchestre, par protocole d'interaction plutôt que par
superviseur — et sortir le PDF à **40 pages exactement**.

**La barre** (choix de l'auteur). *La revue actuelle, front par front.* Le PDF du 9 août est figé en
copie. Un juge à contexte neuf reçoit le même front dans les deux versions, étiquettes retirées, et
désigne celui qui sert le mieux un architecte d'entreprise pressé. **Le total restant à 40 pages, la
version révisée doit gagner en ayant coupé ailleurs** : la barre mesure l'arbitrage ajout/coupe, pas
l'ajout seul.

**Régime de corpus retenu** (choix de l'auteur). Passe de recherche neuve : le corpus grossit.

**Budget** (choix de l'auteur, fixé avant de lancer). Deux vagues, ~15 agents.

## État de départ, mesuré le 9 août 2026

| Mesure | Valeur |
|---|---|
| Pagination (`/Count` de `/Type /Pages`) | 40 p. |
| Mots | 18 078 (corps 11 361, biblio 6 103, tête 493 + résumé) |
| Corpus | 161 entrées, 158 arXiv |
| `check-revue.py` | sortie 0 |
| **Densité du corps, mesurée par sonde** | **474 mots/page** (section transactionnelle retirée : 40 → 38 p.) |
| **Coût d'une entrée de bibliographie, mesuré par sonde** | **12 entrées/page** (+12 entrées : 40 → 41 p.) |

**Le taux de change qui commande tout le reste.** Un front neuf de ~700 mots coûte 1,5 p. ; douze
références neuves en coûtent 1. *Ce qui entre oblige donc à reprendre ≈ 2,5 pages ailleurs — et
c'est cette coupe, pas l'ajout, que le juge à l'aveugle est chargé d'évaluer.*

## Invariants — ce qu'aucun bâtisseur ne peut toucher

Chacun casse un contrôle exécutable de `check-revue.py`, ou un compte énoncé à plusieurs endroits.

1. **Aucun bâtisseur ne numérote une référence.** Il écrit `[[NOUVEAU: arXiv:XXXX.XXXXX]]` ; la
   numérotation, le dédoublonnage et la renumérotation sont centraux. *C'est le geste qui a produit
   trois doublons à la boucle précédente.*
2. **Toute pièce hors socle doit être discutée nommément.** Une plage `[162-173]` ne vaut pas
   discussion : le contrôle exige un appel nommé pour chaque entrée hors du socle `[1-50]`.
3. **Chaque tableau garde sa légende.** Une légende perdue décale tous les « tableau N » en aval.
4. **Les cardinaux du régime de preuve ne se touchent qu'au recollage.** Ils sont énoncés à
   *quatorze* endroits — résumé, méthode §2.1, physionomie §3.1 et §3.2, deux tableaux, synthèse,
   limites, annexe. Les recalculer morceau par morceau garantit qu'ils divergent.
5. **Le régime de preuve d'une pièce se lit à sa notice, jamais à son champ de commentaire.**
   `journal_ref` ou `doi` attestent ; le champ `comment` est une déclaration d'auteur.

---
## Passe de recherche — trois agents, sources primaires exclusives

Trois fronts balayés en parallèle : chorégraphie contre orchestration ; passage à l'échelle de
l'essaim ; ce que la décentralisation casse. **17 pièces rapportées, une en doublon entre deux
agents, 15 retenues.** Deux écartées à la lecture : l'une subsumée par une pièce du même lot
concluant pareil par un mécanisme voisin, l'autre à auteur unique dont la validation confirme sa
propre prédiction et dont la pièce antagoniste n'est pas au corpus — le désaccord n'aurait pas pu
être mis en scène honnêtement.

**Les 17 notices ont été rouvertes à l'API d'exportation par l'orchestrateur, pas par les agents qui
les rapportaient.** Titres, dates, versions et champs concordent tous. *Le contrôle ne servait pas à
attraper les agents, il servait à ce que la revue puisse écrire qu'elle l'a fait.*

**Résultat de fond, et il n'était pas commandé :** aucune des quinze pièces ne porte de `journal_ref`
ni de `doi`. Deux annoncent une acceptation au seul champ de commentaire, une y annonce une simple
soumission. *Le dixième front, qui porte les résultats les plus conséquents sur la coordination sans
chef, ne compte aucune publication arbitrée — le résultat principal de la revue se durcit au lieu de
se diluer.*

## Réconciliation centrale — ce qu'aucun bâtisseur ne pouvait faire

Numérotation centrale **avant** les bâtisseurs, plutôt que par marqueurs à recoller après : les trois
pièces à DOI reculent en [174-176], les quinze neuves prennent [159-173]. *C'est le geste qui a
produit trois doublons à la boucle précédente ; le faire en amont supprime l'étape où ils naissent.*

Les cardinaux ont bougé à quatorze endroits, et un script à assertions les a repris d'un coup :
**chaque substitution doit trouver exactement une occurrence, sans quoi le script échoue.** Une
assertion est effectivement tombée — sur une ligne déjà modifiée en amont — et c'est ce qui a
empêché une substitution silencieusement ratée.

| Cardinal | Avant | Après |
|---|---|---|
| Entrées du corpus | 161 | **176** |
| Pièces arXiv | 158 | **173** |
| Publication attestée en notice | 12 / 158 — 8 % | **12 / 173 — 7 %** |
| Acceptation auto-déclarée | 26 — 16 % | **28 — 16 %** |
| Aucun signe de revue | 120 — 76 % | **133 — 77 %** |
| Déposées en 2026 | 91 — 58 % | **103 — 60 %** |
| Encore en v1 | 81 | **90** |
| Artefact des auteurs | 56 / 105 — 53 % | **67 / 120 — 56 %** |

### Trois erreurs d'arithmétique préexistantes, trouvées en recalculant

Elles ne viennent pas du dixième front ; elles étaient au document et le recalcul les a mises au
jour. Corrigées, et rapportées ici plutôt que corrigées en silence.

1. **§3.2 comptait « cinq » pièces attestées au socle puis « les sept autres », en rangeant [44] et
   [158] dans des fronts qu'il déclarait ensuite n'en compter aucune.** Le compte juste est six et
   six ; les fronts sans attestation sont la sécurité, l'identité, le multi-agents, l'évaluation, le
   transactionnel — et désormais la chorégraphie.
2. **L'annexe annonçait « cinq seulement » puis en énumérait six.**
3. **L'annexe donnait « quatre » pièces du socle antérieures à 2025 ; il y en a deux** — [37] et
   [46], déposées en 2023. Les quatre autres sont de 2025 ou 2026.

### Le contrôle réparé avant d'être cru

`check-revue.py` codait en dur `sur 158` et `(Vingt-six|Trente et une)`. **Passé à 28
auto-déclarations, le motif ne serait pas tombé : il aurait cessé de chercher, et le contrôle serait
passé au vert sur un document faux.** Les alternatives couvrent désormais l'ancienne et la nouvelle
valeur, un cinquième contrôle a été ajouté sur le compte des pièces sans revue, et quatre mutants de
cardinal ont été joués : **tous tombent.**

## Tour 1 — trois bâtisseurs, deux verdicts rendus

| Morceau | Notre version en | Verdict | Motif retenu par le juge |
|---|---|---|---|
| M1 — front neuf, contre un front existant | ALPHA | **gagne** | fixe le régime de preuve de tout le front dès l'ouverture ; tranche son désaccord au lieu de le constater, et nomme l'expérience qui l'arbitrerait |
| M2 — multi-agents comprimé | BÊTA | **perd** | « loi d'échelle logistique, donc saturante » réduit à « échelle saturante » : le résultat redevenu étiquette de sujet ; un manque vérifiable supprimé |

**M2 perd, et c'est l'information la plus utile du tour.** La compression avait tenu le quota en
sacrifiant ce qui fait la valeur du texte. *Une barre qui n'aurait mesuré que la pagination aurait
déclaré ce morceau réussi.*

### Les deux écarts rendus, et ce qu'on en fait

| Écart | Sort |
|---|---|
| **M2** — le 76 % d'attribution de [89] opposé au 53,5 % de [88] sans dénominateur commun, la phrase causale reposant donc sur deux taux dont rien n'établit qu'ils partagent un dispositif | **repris** — et par la source : la notice de [89] est rouverte ; si l'effectif n'y est pas, la comparaison cesse d'être présentée comme un fait |
| **M1** — « interblocage et blocage vivant, 31,1 % à 14,1 % » sans dénominateur ni référent ; fragments dont le sujet a été évacué (« — le parc hétérogène. ») | **repris** — chute de 31,1 % à 14,1 % sur 3 456 essais, et les fragments redeviennent des propositions |

## Tour 2 — le troisième verdict, et ce qu'il apprend

| Morceau | Notre version en | Verdict | Motif retenu par le juge |
|---|---|---|---|
| M3 — clôture comprimée | ALPHA | **perd** | « remplace la mesure par la citation » : *Bancs dominants faussés [107] [108] [109]* au lieu du mécanisme (réponses vides comptées comme succès) ; le dénominateur par front supprimé alors qu'il « constitue à lui seul un verdict » |

**Deux compressions jugées, deux défaites, un seul mode d'échec : échanger de la preuve contre du
slogan.** Ce n'est plus un accident de bâtisseur, c'est une propriété du document — *il est déjà
compressé au point que la prochaine coupe prend du fait, pas du remplissage.* La boucle précédente
l'avait amené de 162 à 100 pages ; celle-ci mesure le plancher.

**L'écart sert deux fois.** Le juge de M3 désigne, dans la version qu'il fait gagner, le paragraphe
« Quatre lacunes dérivées se formulent aussi » : il « rompt le contrat de mesure » que les deux
paragraphes précédents tenaient, en demandant *quel niveau d'autonomie survit à l'auto-modification*
sans dire ce qu'on mesurerait. **C'est donc le juge, et non le budget, qui a désigné où couper.**

### L'erreur de fait que la boucle a trouvée

En creusant l'écart de M2, un bâtisseur a rouvert la notice de [89]. Le résumé dit : *full traces
improve attribution accuracy **by up to 76 %** over a partial-observation counterpart.* La revue
écrivait, à deux endroits, que l'observabilité complète **porte l'attribution à 76 %** — un taux
atteint. C'est un **gain relatif**, la notice ne donne ni effectif ni condition, et il **ne partage
pas le dénominateur** du 53,5 % de [88] auquel il était opposé. *La phrase causale qui en découlait
— « ce plafond tient à l'instrumentation » — reposait donc sur deux taux sans dispositif commun.*
Corrigé aux deux endroits ; l'énoncé redevient une hypothèse.

## Le plancher, mesuré

| Poste | Coût |
|---|---|
| Front neuf, 824 mots | 1,74 p. |
| Quinze références neuves | 1,25 p. |
| **À reprendre ailleurs** | **≈ 3 p., soit ≈ 1 420 mots** |

Compression de l'appareil — la seule qui ne retire que de la redondance : §2.3 répétait « Limites de
cette revue » presque terme à terme, le chapeau de l'annexe rejouait l'argument de §3.2, et
l'énumération mensuelle des révisions disait en trente-cinq mots ce que la phrase suivante dit avec
sa conséquence. **−131 mots. La pagination n'a pas bougé.**

## Tour 2 — la reprise de M2 passe la barre

| Morceau | Notre version en | Verdict | Motif retenu par le juge |
|---|---|---|---|
| M2b — multi-agents repris | ALPHA | **gagne** | marque la rupture de dénominateur que la version actuelle masquait : « un architecte lisant [la version actuelle] en sort avec un ordre d'investir dans l'observabilité, adossé à une comparaison entre deux protocoles distincts » |

*C'est la correction de fait, non la compression, qui a fait gagner le morceau* — 627 mots contre 776,
et le juge n'en dit rien : il juge ce que le texte établit, pas ce qu'il coûte.

**Écart rendu sur la gagnante** : le manque sur les patrons d'orchestration est devenu une assertion
absolue, sans nommer ce qui s'en approche — [98], domaine unique et sans comité de lecture, et [91],
cinq configurations d'un seul modèle. *Un manque que le lecteur ne peut pas vérifier n'est plus un
manque vérifiable, ce qui est exactement le critère que la revue s'impose.* Repris à la passe de
lissage.

## Le levier sans perte, trouvé avant de couper dans l'argument

Chaque entrée de bibliographie écrivait son identifiant arXiv **deux fois** : en clair
(`arXiv:2512.08296v3`) puis dans l'URL en toutes lettres. Replier l'URL derrière l'identifiant rend
**2 pages sur 173 entrées** — même cible, même identifiant lisible, un seul exemplaire. *Le
contrôle des doublons continue de passer parce qu'il lisait déjà l'identifiant et l'URL séparément.*

C'est le seul gain de cette boucle qui ne coûte rien à personne, et il a été cherché **avant** de
faire couper 1 420 mots d'argument, non après.

## Passe de lissage — agent neuf, document entier

Cible : 40 pages, **475 mots à reprendre dans le redit exclusivement**, avec la commande de mesure
entre les mains plutôt qu'un quota en aveugle. Interdiction explicite de toucher l'en-tête YAML :
*atteindre la pagination par la typographie serait contourner la contrainte, pas la satisfaire.*

Les trois plus gros doublons fondus : un paragraphe de §6.2 rejouait intégralement le premier énoncé
de la veille jusqu'à la même phrase de clôture en gras (−95) ; §3.2 et l'annexe tenaient le même
compte des douze attestées (−75) ; §3.1 énumérait les revues que le tableau de l'annexe redonne
colonne par colonne (−55). **475 mots repris, aucun chiffre ni mécanisme touché.**

Coutures corrigées, dont une qui était une vraie contradiction : **§7.3 déclarait absente une
comparaison contrôlée que le front neuf présente vingt pages plus loin** — le manque nomme désormais
ce qui s'en approche.

### La quatrième erreur d'arithmétique, et pourquoi elle a failli survivre

Le lisseur a refusé de corriger §12.3 (« Proposer n'est pas prouver ») et l'a remontée : le texte
annonçait « 120 pièces des dix fronts » quand le tableau de §3.2 en compte 123, et donnait des
dénominateurs par front — sécurité 10/**12** pour un front de 11, gouvernance 2/**12** pour 11,
protocoles 4/**12** pour 13 — qui contredisaient ce même tableau. Son motif : *rectifier sans
recompter reviendrait à fabriquer un pourcentage.*

**Le scrupule est bon, l'objection ne tient pas.** Un dénominateur par front **est** la taille du
front, que le tableau donne ; le corriger n'est pas un recomptage mais de l'arithmétique sur des
nombres que le document affirme déjà. Corrigé : **67 sur 123, soit 54 %.** *Les numérateurs, eux,
sont hérités du décompte antérieur et n'ont pas été revérifiés pièce à pièce — sauf celui du front
neuf, 11 sur 15, établi sur le dossier.* C'est dit ici plutôt que tu.

## État de sortie, mesuré le 9 août 2026

| Mesure | Départ | Arrivée |
|---|---|---|
| Pagination (`/Count`) | 40 p. | **40 p.** |
| Corps | 11 361 mots | **11 998** |
| Corpus | 161 entrées, 158 arXiv | **176 entrées, 173 arXiv** |
| Fronts | 9 | **10** |
| Publication attestée | 12 / 158 — 8 % | **12 / 173 — 7 %** |
| Aucun signe de revue | 120 — 76 % | **133 — 77 %** |
| `check-revue.py` | sortie 0 | **sortie 0** |
| Mutants qui tombent | 4 | **6** |
| `check-resume.py` | OK | **OK, +148,3 pt** |

## Ce que la boucle a coûté, et ce qu'elle a rendu

**Score à l'aveugle : deux morceaux sur trois gagnent** — le front neuf contre un front existant de
la revue, et le multi-agents repris contre sa version actuelle. La clôture a perdu au premier tour,
a été reprise, et n'a **pas été rejugée** : le budget fixé avant de lancer était de deux vagues, et
il était atteint. *C'est un plafond, et il est déclaré ici plutôt que tu.*

**Ce que la barre a attrapé que la pagination n'aurait pas vu.** Les deux morceaux comprimés au
premier tour tenaient leur quota et passaient tous les contrôles exécutables. Les deux ont perdu à
l'aveugle, pour le même motif : *ils avaient échangé de la preuve contre du slogan.* Une boucle qui
n'aurait mesuré que les 40 pages les aurait déclarés réussis.

**Et une erreur de fait, trouvée en creusant un écart de juge.** La revue écrivait à deux endroits
que l'observabilité complète *porte l'attribution à 76 %*. La notice de [89] dit *improve attribution
accuracy by up to 76 % over a partial-observation counterpart* : un gain relatif, sans effectif, sans
dénominateur commun avec le 53,5 % auquel il était opposé. **La phrase causale qui en découlait n'avait
pas de mesure sous elle.** Aucun contrôle exécutable ne pouvait l'attraper — il fallait un juge qui
demande d'où vient le chiffre.
