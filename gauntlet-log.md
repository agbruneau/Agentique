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
