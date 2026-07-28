# Audit des cinq livres du compendium — 28 juillet 2026

| Champ | Valeur |
|---|---|
| Date | 28 juillet 2026 |
| Corpus audité | Commit `8cb40fa`, arbre de travail propre au lancement — l'audit porte sur le corpus committé, conformément à la règle d'attestation du dépôt. |
| Référentiels | TOC v0.28, PRD v0.12, README des cinq Livres, skill `chapitre-compendium`, `CLAUDE.md` du dossier et de la racine. |
| Domaine | Les cinquante chapitres (ch. 1-50) des cinq Livres, lus **en entier** ; leurs deux rendus (`.md` source, `.html` de lecture, parité sondée sur deux pièces par Livre au minimum) ; les cinq README de Livre ; les trois contrôles outillés, exécutés. |
| Méthode | Cinq lectures d'audit indépendantes, une par Livre, conduites en parallèle ; le Livre III, dont la première lecture avait déclaré un domaine partiel (noyau ch. 25-28 en entier, reste par balayages mécaniques), a reçu **trois lectures de fond complémentaires** (ch. 22-24, ch. 29-32, ch. 33-36) — les cinquante chapitres sont donc couverts au fond, domaine déclaré volet par volet. Volumétrie re-mesurée par la commande de référence (`PRD/decompte.sh`), jamais recopiée. |
| Autorité | **Aucune.** Ce rapport est un constat daté : il **remonte**, il ne tranche pas (régime déclaré au `CLAUDE.md` du dossier). Il ne porte ni source, ni socle, ni décision ; aucun de ses constats n'alloue d'identifiant de remontée — l'allocation relève du PRD §13. Il succède au rapport de couverture du 24 juillet 2026, supprimé du dépôt (commit `f6183bf`). |

---

## 1. Objet et régime

Cet audit couvre les cinq Livres du compendium *La somme agentique* en totalité — les cinquante chapitres rédigés hors portes les 27 juillet 2026, arbitrés le même jour (TOC v0.24 à v0.28, PRD v0.8 à v0.12). Il distingue systématiquement le **connu** — les écarts que le dossier consigne déjà (rédaction hors portes, infractions à D-9, volumétries en écart, collision d'identifiants, dettes d'appareil déclarées) — du **neuf** — ce qu'aucune pièce, aucun README, aucun journal ne relève. Le premier est re-vérifié sur pièce et confirmé ; seul le second fait l'objet de constats. Un constat n'est pas un arbitrage : chaque correction éventuelle devra re-vérifier la localisation sur pièce avant d'éditer, et les issues appartiennent à l'auteur.

Gravités employées : **bloquant** (contredit une décision d'auteur ou une règle normative du PRD/TOC, non consigné), **majeur** (écart de fond ou d'alignement non consigné), **mineur** (forme, convention), **note** (observation sans action requise).

## 2. État des contrôles et volumétrie d'ensemble

Les trois contrôles outillés passent sur le corpus audité, exécutés séparément (jamais tuyautés) :

- `python PRD/check-toc.py` → « OK — tous les contrôles passent (C1-C15). », sortie 0 ;
- `python PRD/check-sieges.py` → « OK — les 12 sièges tiennent sur 50 pièces (S1-S5). », sortie 0 ;
- `bash PRD/decompte.sh --verifier` → « OK — les quatre points d'ancrage sont tenus. », sortie 0.

Volumétrie re-mesurée par la commande de référence, chapitre par chapitre puis agrégée :

| Livre | Chapitres | Mots mesurés | Enveloppe TOC | Écart |
|---|---|---:|---:|---:|
| Livre I | 11 (ch. 1-11) | 64 611 | 65 000 | −0,6 % |
| Livre II | 10 (ch. 12-21) | 61 677 | 50 000 | +23,4 % |
| Livre III | 15 (ch. 22-36) | 90 251 | 90 000 | +0,3 % |
| Livre IV | 10 (ch. 37-46) | 55 250 | 69 000 | −19,9 % |
| Livre V | 4 (ch. 47-50) | 25 017 | 34 000 | −26,4 % |
| **Total** | **50** | **296 806** | **308 000** | **−3,6 %** |

Trois faits de cette table. *(a)* Les mesures reproduisent les chiffres publiés des README **à un mot près** : l'unique écart — 55 250 mesurés au Livre IV contre 55 249 publiés — est localisé et expliqué au constat IV.6 (ch. 45, renommage du marqueur de siège dans le commit d'arbitrage même qui publie la mesure). *(b)* Le phénomène de compensation que le Livre III avait documenté à son échelle vaut à l'échelle du compendium entier : un agrégat à −3,6 % — presque conforme — recouvre des Livres qui s'étalent de −26,4 % à +23,4 %, soit près de cinquante points d'amplitude. Les deux forces nommées par les README (le bornage allonge — Livre II ; le siège raccourcit — Livre IV) se lisent ensemble, et l'enveloppe héritée n'avait budgété ni l'une ni l'autre : la mesure alimente D-4, dont le re-calibrage reste remis à une passe unique de clôture. *(c)* Chaque pièce porte en outre une **cible dérivée** propre ; ces dérivations sont hétérogènes d'une pièce à l'autre (bases et taux incompatibles, constats I des Livres I et III) et leur somme ne reconstruit pas toujours l'enveloppe du Livre — défaut documenté au Livre I (93 000 dérivés pour 65 000 d'enveloppe), retrouvé sous d'autres formes aux Livres III et IV.

## 3. Constats transversaux

Les cinq lectures, conduites indépendamment, convergent sur un petit nombre de classes — c'est le résultat principal de l'audit : **les défauts neufs des cinq Livres appartiennent presque tous à des classes que le corpus a déjà nommées ailleurs, sans que ses instruments les voient ici.**

#### T-1 [majeur] Les attestations de balayage des en-têtes ne se re-mesurent pas — dans les cinq Livres

- Pièces : Livre I (ch. 3, 7, 8, 10) ; Livre II (ch. 14, 16, 20) ; Livre III (ch. 22, 23, 24, 25, 27, 29, 30, 33, 34, 35 — quasi systématique) ; Livre IV (ch. 37, 38) ; Livre V (ch. 47, 48, 50).
- Constat : le champ « Garde-fous balayés » des en-têtes et les attestations des notes de statut annoncent des cardinaux d'occurrences, des répartitions par section et des clauses « à chaque emploi / à chaque occurrence » qui, confrontés à un comptage littéral exhaustif, divergent dans une trentaine de cas répartis sur les cinq Livres. Trois degrés coexistent : des décomptes **démontrablement faux** (« quinze occurrences » pour dix-neuf au ch. 22 ; une ventilation déclarée « re-mesurée » qui somme à douze pour onze au tableau 50.1 ; « à chaque emploi » contredit par un emploi nu au ch. 24 § 24.6.2) ; des répartitions par section **contredites par le texte** (occurrences localisées dans des sections qui n'en portent aucune) ; et des décomptes **invérifiables**, la règle de comptage — occurrence littérale ou « application » interprétée — n'étant écrite nulle part. Aucun des quinze contrôles ne rapproche un tableau de balayage du corps qu'il décrit. La doctrine du dépôt — un cardinal se re-mesure, jamais ne s'estime ; un balayage déclare son domaine — est ainsi enfreinte par l'instrument même qui prétend l'appliquer : *un apparat qui annonce des cardinaux invérifiables fragilise la crédibilité qu'il veut construire.*
- Déjà consigné : NOUVEAU comme classe. Le détail par pièce vit aux sections par Livre.

#### T-2 [majeur] La couche d'arbitrage fabrique des discordances de second ordre qu'aucun contrôle ne voit

- Pièces : Livre I (ch. 7, 11) ; Livre II (ch. 12, 14, 15, 16, 17, 19, 20, 21) ; Livre III (ch. 25, 27) ; Livre IV (les dix pièces) ; Livre V (ch. 47, 48, 49, 50).
- Constat : les passes d'arbitrage du 27 juillet 2026 ont réaligné le plan et retouché des en-têtes sans repasser sur les corps ni sur l'autre moitié du couple pièce/plan, produisant trois variantes du même défaut. **(a) Citation figée, plan réaligné** : les thèses réalignées au TOC (v0.24, v0.26, v0.27, v0.28) ne sont pas reportées dans les blocs de citation des pièces — deux pièces au Livre I, deux au Livre III, dix au Livre IV — de sorte que la comparaison mot à mot pièce/plan échoue désormais dans le sens inverse de celui que la décision 14 contrôlait, et qu'aucun document ne déclare si la re-citation est due, à quelle passe, ou si l'état présent est voulu. **(b) Tête réalignée, corps ancien** : au Livre II, cinq introductions commentent encore la forme antérieure de la thèse que leur tête cite réalignée (« la thèse citée ci-dessus porte une proportion » — elle n'en porte plus) ; au Livre V, trois corps contredisent leur thèse de tête (quatre horloges contre cinq au ch. 47 § 47.8) et des mentions « D-2, non prise » subsistent après la prise de D-2. **(c) Re-frappes fautives** : au Livre II, trois thèses de second mouvement ont été re-frappées plutôt que copiées — dont une clause entière retranchée au ch. 21 (constat II.1, bloquant) ; au Livre V, des scories de remplacement partiel subsistent (§ 47.13, § 50.5), et le `.html` du ch. 48 a été régénéré depuis un état intermédiaire du `.md` (V.2). La leçon que les passes de structure ont apprise — *relire son diff ligne à ligne* — n'a pas été étendue aux passes d'arbitrage, qui sont pourtant des passes d'édition comme les autres.
- Déjà consigné : NOUVEAU comme classe ; chaque variante est détaillée à son Livre.

#### T-3 [majeur] Au moins cinq sièges à marqueur ne sont ni versés à l'appareil ni déclarés en dette

- Pièces : ch. 16 § 16.4 (statut PROJETÉ), ch. 19 § 19.6 (restriction R-08), ch. 43 § 43.1 (collision « fabrique », décision 12c), ch. 44 § 44.6 (conformité traçable, désigné « (SIÈGE) » par le TOC), ch. 49 § 49.6 (verrou sémantique et pragmatique, désigné par le TOC) ; s'y ajoute le § 34.2.2 (grille des plateformes d'assurance, marqué « SIÈGE » au TOC), neuvième candidat du Livre III.
- Constat : la table `SIEGES` de `check-sieges.py` porte douze entrées ; le corpus porte davantage de marqueurs formels « SIÈGE … POUR TOUTE LA SOMME » que la table n'en contrôle. La règle du dossier — *un siège s'ajoute à la table, la pièce écrit son marqueur, le harnais se rejoue : les trois gestes, jamais deux sur trois* — est tenue à un ou deux gestes sur trois pour ces cinq-là. Contrairement aux huit sièges du Livre III (dette déclarée, motif écrit) et au tri prospectif (S5 désactivé, motif mesuré), **aucune dette n'est consignée** pour ceux-ci : une reconstruction de leur matière ailleurs dans la somme passerait tous les contrôles. En outre, la dette du tri prospectif est **plus large que déclarée** : les ch. 30 et 31 trient des énoncés prospectifs sans renvoyer au siège ch. 49 § 49.0 et manquent à la liste des six pièces non renvoyantes consignée à la désactivation de S5 — l'écart s'explique par la concurrence des passes (le siège a été désigné le même jour, par une autre passe), mais il n'est écrit nulle part.
- Déjà consigné : NOUVEAU (vérifié : ni le PRD, ni le TOC, ni les README ne déclarent de versement dû pour ces sièges).

#### T-4 [majeur] L'anonymisation des noms propres est devenue une convention de fait, jamais décidée ni déclarée

- Pièces : Livre I (courtiers, bancs, référentiels, éditeurs — ch. 1, 3, 8, 9 notamment) ; Livre II (organismes — ch. 15, 18, 21) ; Livre III (à son plus aigu : « Paiements Canada » → « l'opérateur », « AP2 » ne survivant qu'au titre du ch. 36, « FIDO Alliance » → « une alliance », les quatre identifiants arXiv du § 36.5 absents alors que leur extraction est le critère de clôture déclaré, la grille des dix risques du § 24.3.4 jamais attribuée à son auteur dans la pièce) ; application non uniforme (le ch. 23 § 23.3 anonymise ce que son propre tableau nomme ; les ch. 29 et 32 collent au plan quand les ch. 30 et 31 réécrivent leurs intitulés).
- Constat : la parade de péremption que R-IV-06 a validée pour la seule nomenclature des **modèles** (ch. 4) s'est généralisée sans décision à presque toutes les catégories de noms propres, avec trois coûts vérifiables : des attributions que le lecteur ne peut plus remonter (« un éditeur », « une grande banque » comme attributeurs de métriques) ; des intitulés de section qui ne résolvent plus contre la table détaillée du TOC, qui nomme (décision 8 : une déviation fondée se déclare — elle ne l'est nulle part) ; et des sièges dont l'objet devient anonyme là où le régime du volume exige l'attribution. La convention n'est écrite ni au skill, ni au TOC, ni aux notes de statut.
- Déjà consigné : la parade est consignée pour le seul ch. 4 (R-IV-06) ; sa généralisation et son inhomogénéité : NOUVEAU.

#### T-5 [mineur] Des cardinaux multi-sites de l'appareil de gouvernance sont périmés

- Pièces : `CLAUDE.md` du dossier (en-tête, « Sept décisions sur neuf sont désormais prises ; D-5 et D-8 restent ouvertes ») et `CLAUDE.md` racine (même décompte) — contre PRD v0.12, qui déclare **D-8 prise** (ch. 41 maintenu sous réserve), soit **huit décisions sur neuf, D-5 seule ouverte** ; `Livre V/README.md` (« neuf sièges ») contre la table courante à douze ; `Livre IV/README.md` (les clôtures « vivent dans les notes de statut » — elles n'y sont pas, constat IV.2).
- Constat : la règle du dépôt — un même chiffre vit à plusieurs endroits et se met à jour partout ensemble — n'a pas suivi la passe v0.12 : le décompte des décisions est périmé aux deux `CLAUDE.md`. Ces relevés ne sont pas des zones gelées ; ils conditionnent l'édition.
- Déjà consigné : NOUVEAU.

#### T-6 [note] Deux séries d'intitulés du TOC vivent en numérotation gelée sans que la convention soit déclarée pour eux

- Pièce : `PRD/TOC.md` — en-têtes « Table des matières détaillée du chapitre N » des entrées des ch. 29-36 (numérotation pré-v0.20 : « chapitre 33 » sous l'entrée du ch. 29, etc.) et du Livre V (« chapitre 52 » à « chapitre 57 »).
- Constat : ces intitulés portent la numérotation de leur passe de dérivation (v0.16), cohérente avec la doctrine des correspondances chaînées (décisions 11-13) — mais aucun texte ne déclare la convention **pour ces intitulés précisément**, et aucun contrôle ne les voit (`check-toc.py` ne connaît pas les tables détaillées). Une passe pressée pourrait les « corriger » et casser la chaîne ; c'est la classe de désalignement interne au plan que la v0.28 a nommée, sous une cinquième forme.
- Déjà consigné : implicitement (cartes chaînées) ; la vulnérabilité propre à ces intitulés : NOUVEAU.

#### T-7 [note] Le connu tient — vérification à décharge

- Constat : tous les écarts lourds consignés ont été re-vérifiés sur pièce et sont **exactement conformes à leur consignation** : rédaction hors portes déclarée à chaque pièce des cinq Livres ; infractions à D-9 nommées trois fois chacune aux ch. 25 et 27 ; fermetures D-7 tenues (ch. 37 § 37.0, ch. 48 § 48.3 — aucun des trois chapitres fermés ne traite l'accord sous défaillance) ; régime de la matière neuve tenu aux ch. 41, 47, 48 (zéro provenance inventée, zéro fait affirmé, lots d'instruction bornés correspondant exactement à D-3) ; garde-fou 12c (« fabrique ») tenu à chaque occurrence balayée ; carte de renumérotation R-IV-60…69 → R-IV-100…109 appliquée sans résidu ; ch. 50 terminal ; « avril 2026 » à trois états au tableau 27.1. Un dossier qui déclare ses écarts les déclare juste — c'est le résultat attendu, et il est constaté.
- Déjà consigné : oui, intégralement.

---

## 4. Livre I — onze chapitres (ch. 1-11)

### 4.1 Synthèse

Les onze pièces du Livre I existent en `.md` et `.html`, suivent chacune la table détaillée de leur entrée au TOC section par section, portent l'en-tête à cinq champs, la note de statut hors plan et la sous-section de clôture des remontées. La volumétrie re-mesurée confirme au mot près les onze chiffres publiés (total 64 611, soit −0,6 % de l'enveloppe de 65 000), et la parité des titres `.md`/`.html` est vérifiée sur les ch. 6 et 10. Les trois sièges du Livre portent leur marqueur et ne sont pas reconstruits ailleurs sous forme littérale ; le régime de preuve (degrés R-14, qualifications R-02, attribution des métriques auto-déclarées, marquage « Lecture de l'auteur ») est tenu avec une constance remarquable. Les écarts lourds — rédaction hors portes, ch. 6 écrit malgré une remontée bloquante, dispersion volumétrique de −55,9 % à +0,1 % sur une somme de cibles dérivées fausse de +43 % — sont tous déjà consignés et exactement conformes à ce que le README du Livre déclare. L'audit relève en revanche du neuf : un renvoi de lacune vers le mauvais chapitre, un renvoi cassé, une thèse citée non verbatim, une contradiction interne au ch. 1, des cardinaux d'occurrences de garde-fous inexacts dans plusieurs en-têtes, et une rupture de la numérotation des tableaux aux ch. 10-11. Aucun de ces constats n'est bloquant ; aucun ne contredit une décision d'auteur.

### 4.2 Volumétrie mesurée

Mesures re-exécutées par `bash PRD/decompte.sh` le 28 juillet 2026 ; elles coïncident toutes avec le « Réel » publié en tête de chaque pièce. Le TOC ne donne d'enveloppe qu'au **Livre** (~65 000) ; la colonne « cible » reprend la cible **dérivée** que chaque pièce déclare — leur somme (93 000) est le défaut documenté au README.

| Chapitre | Mots mesurés | Cible dérivée (en-tête) | Écart |
|---|---:|---:|---:|
| Ch. 1 | 10 724 | ≈ 11 000 | −2,5 % |
| Ch. 2 | 5 245 | ≈ 8 000 | −34,4 % |
| Ch. 3 | 5 056 | ≈ 9 000 | −43,8 % |
| Ch. 4 | 7 145 | ≈ 9 000 | −20,6 % |
| Ch. 5 | 4 397 | ≈ 7 500 | −41,4 % |
| Ch. 6 | 3 751 | ≈ 8 500 | −55,9 % |
| Ch. 7 | 4 881 | ≈ 8 000 | −39,0 % |
| Ch. 8 | 5 134 | ≈ 10 000 | −48,7 % |
| Ch. 9 | 5 526 | ≈ 9 000 | −38,6 % |
| Ch. 10 | 7 004 | ≈ 7 000 | +0,1 % |
| Ch. 11 | 5 748 | ≈ 6 000 | −4,2 % |
| **Livre** | **64 611** | **65 000 (enveloppe TOC)** | **−0,6 %** |

La dispersion (51,7 points d'amplitude sous un agrégat conforme) est déjà consignée au README du Livre et alimentée à D-4 ; les deux seules pièces proches de leur cible (ch. 10, 11) sont celles qui déclarent une cible « mesurée, non estimée ».

### 4.3 Constats

#### I.1 [majeur] Renvoi de reprise de la lacune §10.7 vers le « ch. 21 » au lieu du ch. 49
- Pièce : `Livre I/10-transaction-infrastructure.md`, § 10.5.3 (fin de section).
- Constat : « La question est ouverte au registre des lacunes du Vol. II, et la somme la portera telle quelle jusqu'au **ch. 21**, où sa reprise est prévue. » Or le plan renvoie cette lacune (PRD Vol. II §10.7, quatrième branche de R-8) au **ch. 49** — entrée du ch. 7 au TOC (« renvoi ch. 49 »), pièce du ch. 7 § 7.5 (« renvoyée au ch. 49 pour son état final »), et registre des onze lacunes déplié au TOC sous le second mouvement du ch. 49 (rangée §10.7). Le ch. 21 du compendium est l'horloge post-quantique, sans rapport. La confusion probable est avec le **Vol. II ch. 21**, chapitre source du registre — auquel cas le renvoi nu, sans marqueur de document, est exactement la classe d'indécidabilité que la décision 7 du TOC proscrit.
- Déjà consigné : NOUVEAU — ni la note de statut de la pièce, ni le README du Livre, ni l'arbitrage v0.24 ne le relèvent.

#### I.2 [mineur] Renvoi cassé « ch. 8 § » sans numéro de section
- Pièce : `Livre I/06-multi-agents-evaluation-surete.md`, § 6.5.2.
- Constat : « Le ch. 8 § traite les registres ; le ch. 47 traite la provenance des composants. » — le « § » est resté sans numéro (attendu : ch. 8 § 8.3.2). Défaut de forme qu'aucun des contrôles n'attrape (le vérificateur ne lit pas les renvois).
- Déjà consigné : NOUVEAU.

#### I.3 [mineur] Thèse du ch. 10 citée non verbatim — une clause médiane omise
- Pièce : `Livre I/10-transaction-infrastructure.md`, bloc de thèse en tête.
- Constat : le TOC porte « …est une **lecture d'auteur** — **le socle établit qu'AP2 est un protocole compagnon d'A2A, rien de plus sur sa centralité** ; qu'AGNTCY… » ; la pièce cite « …est une **lecture d'auteur** ; qu'AGNTCY… » — la clause médiane est absente du bloc cité. Elle est restituée en substance dans le paragraphe de décomposition qui suit, mais le PRD §6 et la décision 14 exigent la citation **verbatim**, et la comparaison mot à mot échoue. Même famille, moindre : la thèse du ch. 5 au TOC porte un avertissement de périmètre (empoisonnement non traité) accolé au champ Thèse, que la pièce ne cite pas — elle l'exécute au § 5.0 ; défendable, l'avertissement n'étant pas la thèse.
- Déjà consigné : NOUVEAU.

#### I.4 [mineur] Thèses des ch. 7 et 11 : citations figées à la v0.23, divergentes du TOC courant depuis la v0.24
- Pièces : `07-genealogie-gouvernance.md` et `11-modes-echec-risques-protocolaires.md`, blocs de thèse en tête.
- Constat : la v0.24 a **amendé** la thèse du ch. 7 (le transfert d'AP2 est documenté) et **requalifié** celle du ch. 11 (« sans que **le socle du Vol. II** en date la documentation »). Les deux pièces conservent en tête la citation v0.23 : la comparaison mot à mot avec le TOC courant échoue désormais dans les deux cas. La divergence de fond est intégralement consignée (notes de statut, clôtures, README, journal v0.24) et la mention « citée depuis le TOC v0.23 » date la citation ; mais aucune note **postérieure à l'amendement** ne signale que le bloc de tête est devenu une citation périmée d'un plan qui dit autre chose — le lecteur doit le reconstruire depuis la clôture. (Variante (a) de T-2.)
- Déjà consigné : oui pour l'écart de fond ; NOUVEAU pour le fait résiduel que les blocs de tête ne résolvent plus verbatim contre le plan courant.

#### I.5 [mineur] Cardinaux et localisations d'occurrences de garde-fous inexacts dans les en-têtes
- Pièces : ch. 7, 8, 10 (et ch. 3, ambigu).
- Constat, vérifié par balayage complet de chaque fichier : **ch. 7** — « métriques auto-déclarées : quatre occurrences, § 7.6 (trois) et § 7.3 » : le § 7.3 n'en porte aucune ; les quatre sont toutes au § 7.6. **Ch. 8** — « R-8 : cinq occurrences, § 8.5.1 » : six occurrences qualifiées du sigle, dont une au titre du § 8.5 et une au § 8.5.3 ; « R-14 : quatre occurrences, § 8.2.3, § 8.6.1, § 8.7 et § 8.8 » : trois occurrences marquées dans le corps, le § 8.8 (note de statut) n'en portant qu'un rappel. **Ch. 10** — « R-14 : six occurrences » : sept sont marquées, la liste omettant § 10.2.1 ; « métriques… § 10.2.2 » : l'occurrence est au § 10.2.3. **Ch. 3** — « R-02 : cinq occurrences, § 3.2.2 (deux) » : quatre marqueurs ; le compte de cinq n'est défendable qu'en comptant deux mécanismes sous un marqueur unique. Aucun garde-fou n'est **enfreint** — toutes les occurrences réelles sont qualifiées et attribuées — mais les décomptes annoncés violent la règle des décomptes du dépôt, et aucun contrôle ne les voit. (Instance de T-1.)
- Déjà consigné : NOUVEAU.

#### I.6 [mineur] Ch. 1 § 1.0.2 : « Deux termes ici » contre « les trois premiers » — contradiction interne, et écart avec la sous-entrée du TOC
- Pièce : `01-interoperabilite-integration-entreprise.md`, § 1.0.2 et § 1.7.
- Constat : l'encadré est titré « **Deux termes ici, quatre à l'avant-propos** », mais sa phrase suivante écrit « Le présent chapitre en éprouve les **trois premiers** », et le § 1.7 confirme « trois termes éprouvés ici » (découplage, contrat, évolution — l'évolution est bien traitée au § 1.1.4). La sous-entrée 1.0.2 du TOC écrit de son côté « les **deux premiers** termes sont éprouvés ici ». Le corps est cohérent à trois ; le titre de l'encadré et le plan disent deux.
- Déjà consigné : NOUVEAU.

#### I.7 [mineur] La numérotation « Tableau N.M » s'interrompt aux ch. 10 et 11
- Pièces : `10-transaction-infrastructure.md` (4 tableaux), `11-modes-echec-risques-protocolaires.md` (5 tableaux).
- Constat : les ch. 1 à 9 numérotent leurs tableaux (Tableau 1.1 … Tableau 9.4) ; les ch. 10 et 11 portent des légendes descriptives sans numéro. La règle « toute table porte une légende » est satisfaite partout, mais la convention de série du Livre se rompt sans déclaration — et un renvoi futur « tableau 10.2 » n'aurait pas de cible.
- Déjà consigné : NOUVEAU.

#### I.8 [mineur] Ch. 4 : « autonomie graduée » comptabilisée sous R-8 du Vol. II, contre l'attribution que portent le TOC et les autres pièces
- Pièce : `04-ingenierie-systemes-agentiques.md`, en-tête (Garde-fous balayés) et § 4.1.4.
- Constat : l'en-tête inscrit « Vol. II — R-8 (jamais nus) : une occurrence, § 4.1.4 ». Or la sous-entrée 4.1.4 du TOC rattache cette occurrence au seul **R-13 du Vol. III**, et les pièces voisines définissent R-8 (Vol. II) comme l'encadré de la collision « (agentic) control plane »/ACP (ch. 7 § 7.5), le ch. 3 § 3.3.1 attribuant les quatre termes proscrits à **R-13**. La double comptabilisation sous R-8 paraît une extension d'identifiant non couverte par le plan — la classe de flottement que la décision 7 vise. À vérifier contre la définition de R-8 au Vol. II avant toute correction.
- Déjà consigné : NOUVEAU.

#### I.9 [note] Mécanique de la fusion de l'ACP protocolaire restituée en paraphrase hors de son siège
- Pièces : `07-genealogie-gouvernance.md` § 7.3 et § 7.4.1 ; `10-transaction-infrastructure.md` § 10.5.2.
- Constat : le siège est au ch. 8 § 8.5.1, le partage déclaré (décision 2) couvrant le couple ch. 8/ch. 10. Or les faits constitutifs de la mécanique — « développement actif cesse, actifs versés, guides de migration fournis » — sont restitués trois fois. Chaque restitution est brève et fonctionnellement motivée, mais c'est la classe de reconstruction paraphrasée que les motifs S1-S5 ne voient pas — la limite déclarée de `check-sieges.py`, illustrée ici sur pièce.
- Déjà consigné : la limite de l'outil est consignée (`CLAUDE.md` du dossier) ; ces trois occurrences précises : NOUVEAU.

#### I.10 [note] Sous-structure au-delà du dépliage du TOC ; noms propres anonymisés là où le plan les nomme
- Pièces : ch. 5 (§ 5.0), ch. 10 (sous-sections 10.1.1-10.6.2 absentes de la table détaillée), ch. 11 (§ 11.0, § 11.1.4, § 11.4.3) ; ch. 8 (§ 8.5 intitulé « L'ACP protocolaire, l'alternative décentralisée… » contre « ACP-agent, ANP… » au TOC) ; transversal.
- Constat : *(a)* plusieurs pièces ajoutent des sous-sections ou apparats que la table détaillée ne prévoit pas — tous déclarés ; conforme à la décision 8, mais la passe de réalignement des tables reste due. *(b)* Des intitulés de sections sont reformulés (le sigle **ANP** n'apparaît nulle part dans le corps du ch. 8 ; « ACP-agent » du plan devient « ACP protocolaire » partout). *(c)* Plus largement, les pièces anonymisent des noms propres que les tables détaillées du TOC portent (Kafka/RabbitMQ/Pulsar/NATS au § 1.5.2, AGENTS.md/Agent Spec au § 9.3.4, OASF/MCP Registry au § 9.1.3, OWASP au § 3.1.2…) — parade validée par R-IV-06 pour la seule nomenclature des modèles, généralisée sans décision (instance de T-4). La couverture de fond est intacte ; la collation par intitulé et la vérifiabilité du lecteur en paient le prix.
- Déjà consigné : la parade est consignée pour le seul ch. 4 (R-IV-06) ; sa généralisation : NOUVEAU.

#### I.11 [note] Les écarts lourds du Livre sont exactement conformes à leur consignation
- Constat : rédaction hors portes G-1/G-2/G-3 sur instruction d'auteur ; ch. 6 rédigé malgré R-IV-01 bloquante ; treize remontées soldées chacune là où elle fait foi ; correction post-poussée du ch. 7 (périmètre de fusion) ; volumétrie individuelle en fort écart sous agrégat conforme. Tout est déclaré au bon endroit et tout ce qui est attestable sur pièce a été re-vérifié exact.
- Déjà consigné : oui — intégralement.

### 4.4 Commentaire éditorial

Le Livre I est un brouillon d'une discipline inhabituelle : le régime de preuve n'y est pas un ornement de tête mais une pratique tenue phrase à phrase — degrés d'absence distingués (jusqu'au rare fait négatif vérifié du ch. 5 § 5.0), qualifications R-02 énonçant ce qu'un mécanisme démontre *et* ne démontre pas, métriques attribuées à chaque occurrence avec la clause « soutien n'est pas production ». Le fil de l'invariant (découplage, contrat, évolution) est réellement porteur : il fait tenir ensemble onze matières hétérogènes et rend les legs explicites, ce qui est la raison d'être du compendium. Les pièces les plus fortes sont le ch. 1 — socle dense, bien articulé, seul à approcher sa cible parmi les fondements —, le ch. 7 — la chronologie par protocole et la lecture critique des métriques sont exemplaires — et surtout le ch. 10, qui érige la prudence en méthode (intervalles calculés plutôt que récits, pas d'inférence sans marquage, +0,1 % de sa cible mesurée) ; le § 10.1.3, exposition de deux états de connaissance datés sans les lisser, est probablement la meilleure page du Livre. Le ch. 11 clôt bien le mouvement : la non-compositionnalité de la sûreté et le « qui parle / ce qui est dit » donnent au Livre II un point d'appui net. Les faiblesses sont symétriques. Le premier mouvement s'amincit à mesure qu'il avance : les ch. 5 et 6 (−41 % et −56 %) condensent au point de frôler l'aide-mémoire — le § 6.3.3 égrène des bancs anonymisés en une page là où la thèse du chapitre annonce un front majeur. L'anonymisation généralisée des noms propres (I.10) protège de la péremption mais produit des périphrases parfois laborieuses et prive le lecteur praticien — public déclaré — de toute prise vérifiable. L'appareil pèse lourd : l'en-tête, la note de statut et la clôture représentent une fraction substantielle de chaque fichier, et le paragraphe volumétrique identique répété onze fois est du bruit que la publication devra retirer avec les sections hors plan. Les redites de fond sont rares et presque toujours converties en renvois — la discipline des sièges fonctionne —, la principale exception étant la triple restitution de la fusion ACP (I.9). Les deux mouvements du Livre s'enchaînent bien, le ch. 7 reprenant exactement où le ch. 6 laisse. En l'état, le Livre est un brouillon honnête, cohérent et au-dessus du standard qu'on attend d'un texte écrit hors portes ; ce qui lui manque n'est pas de la correction locale mais ce que ses propres notes réclament — l'élévation du socle (G-3) et une relecture qui ne soit pas de la même main (CA-IV-13).

---

## 5. Livre II — dix chapitres (ch. 12-21)

### 5.1 Synthèse

Les dix pièces du Livre II sont présentes en deux rendus, conformes au squelette du skill : en-tête à cinq champs complet, thèse citée en tête, note de statut hors plan, clôture des remontées datée du 27 juillet 2026. La volumétrie re-mesurée reproduit à l'unité près les chiffres publiés au README (61 677 mots, +23,4 %). Les cinq thèses réalignées par la décision 14 (ch. 14, 15, 16, 17, 19) concordent aujourd'hui mot à mot avec le TOC ; les sections suivent les tables détaillées dans l'ordre exact, les fusions v0.20 conservent leurs deux thèses, et la discipline de renvoi (décision 7, deux séries F-xx, sigles jamais nus) est tenue avec une constance remarquable. L'audit relève néanmoins du neuf en trois endroits que les quinze contrôles ne voient pas : **trois thèses de second mouvement ne sont pas citées verbatim** — dont une clause entière retranchée au ch. 21, la classe même que l'arbitrage du Livre III a nommée —, **cinq introductions commentent encore la forme ancienne de leur thèse** alors que la citation en tête a été réalignée, et **deux sièges marqués « POUR TOUTE LA SOMME » ne sont versés ni à l'appareil ni à aucun registre de dette**. S'y ajoutent des défauts de cardinal et de fraîcheur mineurs. Les écarts déjà consignés — rédaction avant G-3 et G-4, ordre du PRD §6 enfreint, CA-IV-11 et CA-IV-13 insatisfaites, S5 désactivé pour le tri prospectif — sont fidèlement déclarés dans les pièces et ne sont pas re-signalés comme neufs.

### 5.2 Volumétrie mesurée

Mesures exécutées le 28 juillet 2026 ; concordance à l'unité près avec le tableau du README du Livre. Le TOC ne porte qu'une enveloppe de Livre (~50 000) ; les cibles par chapitre sont les dérivations déclarées dans les en-têtes.

| Chapitre | Mots mesurés | Cible dérivée | Écart |
|---|---:|---:|---:|
| Ch. 12 | 7 372 | 6 200 | +18,9 % |
| Ch. 13 | 3 947 | 4 000 | −1,3 % |
| Ch. 14 | 3 514 | 3 000 | +17,1 % |
| Ch. 15 | 8 152 | 5 800 | +40,6 % |
| Ch. 16 | 4 771 | 4 500 | +6,0 % |
| Ch. 17 | 6 933 | 5 700 | +21,6 % |
| Ch. 18 | 4 202 | 3 800 | +10,6 % |
| Ch. 19 | 5 467 | 5 000 | +9,3 % |
| Ch. 20 | 8 855 | 6 200 | +42,8 % |
| Ch. 21 | 8 464 | 5 800 | +45,9 % |
| **Livre** | **61 677** | **50 000** | **+23,4 %** |

La dispersion va de −1,3 % à +45,9 % : seul le ch. 13 est sous sa cible, et les trois plus forts écarts (ch. 21, 20, 15) sont les trois pièces les plus chargées en bornes (R-11, R-14, R-02) — la corrélation bornage/longueur annoncée au README se vérifie à la lecture. Le dépassement global est connu et alimente D-4 ; la dispersion — quatre chapitres au-delà de +20 % contre un seul sous la cible — montre que l'enveloppe héritée sous-budgète structurellement le coût du bornage, non un chapitre en particulier.

### 5.3 Constats

#### II.1 [bloquant] Trois thèses de second mouvement ne sont pas citées verbatim depuis le TOC
- Pièces : `12-heritage-standards-etires.md`, `20-usurpation-revocation-boucle-defensive.md`, `21-horloge-post-quantique.md` (blocs « Thèse du second mouvement »).
- Constat : le PRD §6 exige la citation verbatim de la thèse, et la décision 14 repose sur la comparaison mot à mot. Or, dans les trois chapitres fusionnés, **la thèse du second mouvement diverge du TOC** — et seules celles-là : les sept citations de premier mouvement ou de chapitre simple sont exactes. Ch. 12 : « non une rupture **— et** chaque extension » (TOC) devient « non une rupture**, et** chaque extension ». Ch. 20 : « ingouvernable **—** les agents défensifs » devient « ingouvernable **;** les agents défensifs ». Ch. 21, le cas grave : la citation retranche la clause « **— le quatrième, l'exploitation, est refermé au Livre IV** » de la parenthèse « (découplage, contrat, évolution — le quatrième, l'exploitation, est refermé au Livre IV) ». Le contenu de la clause est honoré au § 21.4, mais la citation déclarée verbatim est amputée — exactement la classe que l'arbitrage du Livre III a nommée (R-IV-83/R-IV-87 : « la thèse citée avait elle-même retranché une borne en la reprenant »), déclarée « plus difficile à voir que la première » parce que chaque pièce est cohérente isolément. Le regroupement sur les seuls seconds mouvements suggère une re-frappe des blocs plutôt qu'une copie. (Variante (c) de T-2.)
- Déjà consigné : **NOUVEAU**. Le balayage de la décision 14 portait sur plan-contre-source, jamais sur pièce-contre-plan ; aucun contrôle outillé ne compare une citation à son original.

#### II.2 [majeur] Cinq introductions décrivent encore la forme ancienne de la thèse que leur tête cite désormais réalignée
- Pièces : ch. 14 (introduction), ch. 15 (§ 15.3), ch. 16 (§ 16.4), ch. 17 (§ 17.0), ch. 19 (§ 19.0).
- Constat : la passe v0.25 a mis à jour les blocs de citation (« Thèse réalignée au TOC v0.25 ») en déclarant « le corps du chapitre n'a pas changé » — mais ce corps inchangé contient, dans les cinq pièces, des paragraphes qui commentent la forme **antérieure** et sont devenus faux au regard de la citation qui les précède. Ch. 14 : « La thèse citée ci-dessus porte une forme que sa source a elle-même bornée […] Le TOC v0.24 porte encore la forme large » — alors que la thèse citée au-dessus est désormais la forme bornée. Ch. 19 : « La thèse citée ci-dessus porte une proportion » — elle n'en porte plus aucune. Ch. 17 : l'énumération de « presque aucun » et « prouve », termes absents de la thèse citée. Ch. 16 : « la thèse citée en tête projette la normalisation "2027-2028" » — l'échéance a été retirée. Ch. 15 : « que la thèse du chapitre porte au présent » — la thèse porte désormais « tend à devenir — mouvement SPÉCULATIF ». Chaque pièce se contredit donc entre sa tête (réalignée) et son corps (« l'écart est remonté, non arbitré ici », alors qu'il est arbitré). (Variante (b) de T-2.)
- Déjà consigné : **NOUVEAU**. Le choix de ne pas toucher le corps est consigné ; la contradiction résiduelle qu'il produit ne l'est nulle part.

#### II.3 [majeur] Deux sièges marqués « POUR TOUTE LA SOMME » ne sont ni versés à l'appareil ni déclarés en dette
- Pièces : `16-passeport-agent.md` § 16.4 ; `19-taxonomie-attaques-identite-delegation.md` § 19.6.
- Constat : le Livre II porte **six** marqueurs formels « SIÈGE … POUR TOUTE LA SOMME » (balayage exhaustif : KYA § 18.0, encadré § 16.2, triade § 19.2, horloge § 21.1, **statut PROJETÉ § 16.4**, **restriction R-08 § 19.6**). La table `SIEGES` de `check-sieges.py` n'en porte que quatre pour ce Livre ; le README annonce « Quatre sièges posés ici pour toute la somme ». Le siège du statut PROJETÉ est pourtant **désigné trois fois au TOC** et des pièces y renvoient (ch. 13, ch. 20 § 20.7) ; la restriction R-08 est déclarée siège au champ Garde-fous du ch. 19 et reçoit des renvois des ch. 12 § 12.2 et ch. 20 § 20.0/§ 20.9. La règle des trois gestes est enfreinte dans le sens inverse du cas documenté (marqueur sans table), et contrairement au tri prospectif, **aucune dette n'est consignée**. (Instance de T-3.)
- Déjà consigné : **NOUVEAU** (recherche au PRD et au TOC : zéro occurrence d'un versement dû pour ces deux sièges).

#### II.4 [mineur] Quatre notes de statut portent des volumétries périmées depuis la re-mesure d'arbitrage
- Pièces : ch. 12 (note, R-IV-17 : « 7 301 », « +17,8 % ») ; ch. 15 (« +38,3 % ») ; ch. 17 (« +18,3 % ») ; ch. 21 (« +43,8 % »).
- Constat : les quatre pièces dont le corps a été touché par la passe d'arbitrage portent un en-tête re-mesuré (7 372/+18,9 ; +40,6 ; +21,6 ; +45,9) mais leur note de statut conserve les chiffres de rédaction — chaque pièce se contredit entre son champ Volumétrie et sa note. Les notes ne sont pas des zones gelées : la même passe y a écrit. Le ch. 20, non touché au corps, est cohérent — ce qui confirme le mécanisme.
- Déjà consigné : la re-mesure et son motif le sont (README) ; **l'écart interne des quatre pièces est NOUVEAU** — et illustre la règle qu'il enfreint.

#### II.5 [mineur] Le cardinal de la classe « lacune couverte par un autre volume » ne concorde pas avec son énumération
- Pièces : `20-usurpation-revocation-boucle-defensive.md` (R-IV-35 : « Cinquième occurrence » à l'ouverture, « Sixième occurrence » à la clôture, avec la même liste de quatre antécédents) ; README Livre II (constat 3) et `CLAUDE.md` racine : « six occurrences en deux Livres — R-IV-12 et R-IV-13 au Livre I, R-IV-14, R-IV-18 et R-IV-35 ici » — cinq identifiants pour « six ».
- Constat : soit un sixième membre existe et n'est pas nommé, soit le cardinal est faux ; dans les deux cas, « un cardinal d'écarts sans domaine de balayage est un relevé, pas une couverture » — la formule du corpus s'applique à son propre décompte, répliqué en trois endroits.
- Déjà consigné : **NOUVEAU**.

#### II.6 [mineur] Ch. 16 : « Cinq entrées mobilisées ici sont en [C] » suivie de six identifiants
- Pièce : `16-passeport-agent.md`, champ Socle mobilisé : « Cinq entrées […] — Vol. III F-31, F-36, F-55, H-18, H-19, H-33 » (six) ; la note de statut dit « Six entrées ».
- Constat : contradiction de cardinal interne à la pièce, entre l'en-tête et sa propre note.
- Déjà consigné : **NOUVEAU**.

#### II.7 [mineur] Trois intitulés de section s'écartent de la table détaillée du TOC sans déviation déclarée
- Pièces : ch. 15 § 15.3.2 (« le protocole normalise le chemin, **l'annuaire** spécifie le magasin » ; TOC : « **A2A** normalise le chemin, **AGNTCY** spécifie le magasin ») ; ch. 21 § 21.4 (« état des recommandations » ; TOC : « état des recommandations **NIST** ») ; ch. 18 § 18.4 (« Relève à instruire » ; TOC : « Relève **v0.11**, à instruire »).
- Constat : la motivation se lit (discipline des sigles nus, anonymisation des organismes) mais n'est déclarée nulle part, alors que la décision 8 impose de déclarer une déviation fondée — et l'anonymisation n'est pas uniforme. Sans effet sur la résolution des renvois. (Instance de T-4.)
- Déjà consigné : **NOUVEAU**.

#### II.8 [mineur] Ch. 14 : « quatre échelles d'autonomie et de certification » annoncées, trois nommées
- Pièce : `14-grille-cinq-questions.md`, note de statut.
- Constat : « Les **quatre échelles** d'autonomie et de certification que la somme croise sont nommées par leur cardinal » — le corps (§ 14.4) nomme **trois** échelles homonymes du Vol. I et aucune échelle de certification ; les niveaux de certification n'apparaissent qu'au ch. 18 § 18.3. Cardinal non re-mesurable contre le corps de la pièce qui l'annonce. (Instance de T-1.)
- Déjà consigné : **NOUVEAU**.

#### II.9 [note] Une occurrence vive du verbe « prouve » dans le Livre
- Pièce : `20-usurpation-revocation-boucle-defensive.md` § 20.7 : « *l'observation prouve qu'un seuil de faisabilité est franchi* ».
- Constat : seul emploi non métalinguistique du verbe dans les dix pièces. Il est hors du domaine strict de R-02 — il porte sur une observation empirique, non sur la promesse d'un mécanisme cryptographique — et la note du TOC pour cette section écrit « un seuil **démontré** ». Dans un Livre qui a corrigé un intitulé pour ce verbe précis, l'harmonisation se signale ; elle ne s'impose pas.
- Déjà consigné : **NOUVEAU**, sans action requise.

#### II.10 [note] Ancrages de version datés au README du Livre et dans les pièces
- Pièces : `Livre II/README.md` (« TOC.md v0.25 », « PRD.md v0.9 ») ; les dix pièces citent « TOC v0.25 ».
- Constat : le dépôt est à TOC v0.28 / PRD v0.12 ; les ancrages sont exacts à leur date (les passes v0.26-v0.28 n'ont pas touché le Livre II), mais la précision apportée au README du Livre V sur ce point exact (commit `998e888`) n'a pas d'équivalent ici.
- Déjà consigné : classe traitée pour le Livre V seulement ; **NOUVEAU** pour le Livre II, sans urgence.

#### II.11 [note] Emplacement du marqueur du siège KYA
- Pièce : `18-know-your-agent.md` — le bloc « SIÈGE UNIQUE DU KYA » est posé au § 18.0 ; le TOC, le README et la table de `check-sieges.py` désignent « ch. 18 § 18.1 ». Le script résout par fichier, S1-S5 passent : écart purement cosmétique.
- Déjà consigné : **NOUVEAU**, sans action requise.

#### II.12 [note] Rendus `.html` conformes (vérification par échantillon)
- Pièces : `14-grille-cinq-questions.html`, `20-usurpation-revocation-boucle-defensive.html`.
- Constat : les dix `.html` existent ; pour les deux vérifiés, les titres reproduisent exactement les sections du `.md` (notes de statut comprises). Aucun écart.
- Déjà consigné : sans objet — constat de conformité.

### 5.4 Commentaire éditorial

Le Livre II est, à la lecture, le plus discipliné des artefacts du dépôt sur le bornage : chaque affirmation porte son entrée, son niveau et sa borne, chaque absence porte son degré, et les formules imposées (« attendu par », « visée », « cadre d'autorisation ») sont tenues sans une seule défaillance repérée. Cette discipline a un coût lisible dans la volumétrie — les chapitres qui bornent le plus débordent le plus — et un rendement réel : les sections les plus fortes du Livre sont celles où la borne fait le propos, comme le § 15.1.3 (l'interdiction sans le moyen), le § 20.5 (ce qu'un « good » démontre) ou le § 21.1 (trois origines qui ne se fusionnent pas). Les fusions v0.20 sont bien conduites : les deux thèses cohabitent sans être fondues, et les ch. 12 et 21 réussissent la soudure de leurs mouvements — le ch. 12 par la boucle 2012-2026 refermée sur SCIM, le ch. 21 par le renversement final « crypto-agilité et révocabilité, même propriété vue de deux côtés », qui est la meilleure phrase du Livre. Le ch. 20 est moins homogène : son second mouvement, presque intégralement en [C], vit surtout de réserves de statut de produits, et le § 20.8 frôle l'inventaire commercial que ses propres bornes désamorcent à grand-peine. Les chapitres qui refusent d'écrire — le § 17.5 exposant le vide au lieu de le combler, le § 19.0 renonçant à toute proportion — sont paradoxalement parmi les plus convaincants, parce que le refus y est motivé, outillé et repris par l'arbitrage (D-9). La tenue des thèses est bonne dans les corps ; c'est l'appareil péri-textuel qui flanche — citations de tête re-frappées plutôt que copiées, introductions non resynchronisées après réalignement, cardinaux recopiés d'une zone à l'autre —, et il est frappant que les défauts neufs relevés appartiennent tous à des classes que le corpus a déjà nommées ailleurs, sans que ses instruments les voient dans ce Livre. La lisibilité souffre par endroits de la densité des avertissements : dans les ch. 15 et 20, la proportion de texte consacrée à borner dépasse visiblement celle consacrée à établir. Les redites entre pièces sont maîtrisées grâce aux sièges, mais la répétition rituelle des clôtures et des points 1-4 des notes de statut, quasi identiques d'une pièce à l'autre, gonfle le hors-corps sans informer davantage. Enfin, la dispersion volumétrique confirme que l'enveloppe héritée n'est pas un instrument de pilotage à ce grain : D-4 a eu raison d'interdire l'amputation, et le re-calibrage de clôture devrait budgéter le bornage comme un poste propre plutôt que comme un dépassement. En l'état, le Livre II ferait un excellent brouillon de référence — à condition que la passe qui le rendra publiable commence par resynchroniser ses têtes de chapitre avec ses propres arbitrages, ce qui est un travail d'heures, non de fond.

---

## 6. Livre III — quinze chapitres (ch. 22-36)

Le Livre III a été audité en cinq volets, chacun déclarant son domaine : **volet A** — appareil des quinze pièces et lecture intégrale du noyau réglementaire (ch. 25-28) ; **volet B** — lecture intégrale des ch. 22-24 ; **volet C** — lecture intégrale des ch. 29-32 ; **volet D** — lecture intégrale des ch. 33-36 ; **volet E** — consolidation par une lecture distincte des onze chapitres hors noyau, avec collation des thèses contre le TOC v0.28, re-calcul de toutes les durées calendaires rencontrées et, pour trancher un écart, extraction à la source du Vol. I (*Monographie*, §5.7-5.8). Les quinze chapitres sont ainsi couverts au fond, plusieurs deux fois.

### 6.1 Synthèse

Les quinze pièces portent l'en-tête à cinq champs, le statut « brouillon, non publiable », une note de statut hors plan et une clôture des remontées datée du 27 juillet 2026, chacune précédée du paragraphe de renumérotation R-IV-38…61 → R-IV-76…99. La volumétrie publiée au README se reproduit à l'unité près sur les quinze fichiers (90 251 mots ; +0,3 % par compensation). Les deux infractions à D-9 (ch. 25 et 27) sont effectivement nommées dans chaque pièce, à trois endroits chacune ; la divergence de date québécoise est exposée à trois états (tableau 27.1, R-IV-88) ; les six sièges du ch. 31 et les deux domiciles du ch. 24 portent leurs marqueurs ; les quinze `.html` existent (`lang="fr-CA"` partout), parité de titres vérifiée sur quatre pièces. Les régimes de preuve que le plan désigne comme cœur du Livre — formulation imposée du ch. 33, réserve F-29, exclusion de socle R-IV-97, garde-fou §7.5 des métriques, régime prospectif du ch. 36 — sont tous **tenus, vérifiés point par point**. Le neuf se concentre en trois classes : des **discordances résiduelles créées par l'arbitrage lui-même** (thèses et intitulé réalignés au plan, non reportés aux pièces — variante (a) de T-2) ; des **attestations de balayage massivement non reproductibles** (T-1, la plus forte densité des cinq Livres) ; et l'**anonymisation systématique non déclarée** (T-4, à son plus aigu aux ch. 33-36). S'y ajoutent une erreur d'arithmétique calendaire, deux omissions d'en-tête de socle, une entrée annoncée jamais mobilisée, et des renvois promis qui ne résolvent pas. Aucun constat bloquant. Fait notable : les deux constats majeurs du volet de consolidation relèvent du **plan et non des pièces** — la table détaillée du § 34.2 est plus étroite que sa source, et l'entrée du ch. 27 porte encore la date que R-IV-88 a défaite — de sorte que, dans ce Livre, le texte rédigé est en meilleur état que le TOC qui le régit.

### 6.2 Volumétrie mesurée

Mesures exécutées par `PRD/decompte.sh` le 28 juillet 2026 ; les quinze reproduisent le tableau du README à l'unité près. La colonne « Enveloppe » est la cible dérivée par chapitre.

| Chapitre | Mots mesurés | Cible dérivée | Écart |
|---|---:|---:|---:|
| Ch. 22 | 8 459 | 8 500 | −0,5 % |
| Ch. 23 | 4 421 | 5 000 | −11,6 % |
| Ch. 24 | 12 530 | 9 500 | **+31,9 %** |
| Ch. 25 | 6 069 | 7 000 | −13,3 % |
| Ch. 26 | 2 316 | 2 500 | −7,4 % |
| Ch. 27 | 6 905 | 7 500 | −7,9 % |
| Ch. 28 | 2 331 | 2 500 | −6,8 % |
| Ch. 29 | 4 577 | 4 000 | +14,4 % |
| Ch. 30 | 7 941 | 7 500 | +5,9 % |
| Ch. 31 | 8 084 | 8 500 | −4,9 % |
| Ch. 32 | 3 086 | 3 500 | −11,8 % |
| Ch. 33 | 2 804 | 3 500 | **−19,9 %** |
| Ch. 34 | 9 562 | 9 500 | +0,7 % |
| Ch. 35 | 6 783 | 6 000 | +13,1 % |
| Ch. 36 | 4 383 | 5 000 | −12,3 % |
| **Livre** | **90 251** | **90 000** | **+0,3 %** |

La dispersion (−19,9 % à +31,9 %, compensation à l'agrégat) est déjà consignée au README avec ses deux causes. Les bases de dérivation sont hétérogènes d'une pièce à l'autre (sections aux ch. 29/32, sous-sections aux ch. 30/31, taux unitaires incompatibles) : la dérivation annoncée n'est pas reproductible d'une pièce à l'autre — même famille que le défaut documenté au Livre I.

### 6.3 Volet A — appareil des quinze pièces et noyau réglementaire (ch. 25-28)

#### III.A.1 [mineur] Les thèses réalignées au plan n'ont pas été reportées dans les citations des pièces
- Pièces : `25-e23-risque-modele.md` et `27-quebec-amf-article-12-1.md`, blocs de thèse.
- Constat : les deux pièces citent leur thèse « depuis le TOC.md **v0.25** », c'est-à-dire la forme **pré-réalignement** — ch. 25 sans « d'analystes », ch. 27 sans « sous l'article 12.1 du moins ». Le TOC v0.27 porte les formes réalignées : la citation de tête **ne concorde plus mot à mot avec le plan courant**. Les corps, eux, sont écrits sous la forme bornée dans les deux cas. (Variante (a) de T-2.)
- Déjà consigné : en substance, oui (blocs de collation, clôtures R-IV-83/R-IV-87) ; **l'écart inversé** — citation de pièce discordante du plan réaligné, sans déclaration — est NOUVEAU.

#### III.A.2 [mineur] L'intitulé du § 27.2 n'a pas suivi la correction R-IV-89 du plan
- Pièce : `27-quebec-amf-article-12-1.md`, § 27.2.
- Constat : la pièce titre encore « L'article 12.1 : **trois obligations, un texte** » alors que sa propre clôture R-IV-89 écrit que « le § 27.2 s'intitule **désormais** "une obligation inconditionnelle, trois informations dues sur demande, un alinéa distinct" » — ce que le TOC v0.27 porte effectivement. La légende du tableau 27.2 (« le titre de section du plan porte le décompte hérité ») décrit maintenant l'état inverse de la réalité.
- Déjà consigné : l'écart d'origine, oui ; l'écart résiduel inversé : **NOUVEAU**.

#### III.A.3 [mineur] Erreur d'arithmétique calendaire au ch. 28, en deux endroits
- Pièce : `28-valeurs-mobilieres-acvm-11-348.md`, § 28.3 et note de statut, point 4.
- Constat : « seize mois et vingt-six jours » écoulés du 31 mars 2025 au 27 juillet 2026 — recalcul sous la convention que la pièce emploie partout ailleurs : **quinze** mois et vingt-six ou vingt-sept jours, jamais seize. Les autres décomptes de durée du mouvement sont exacts ; celui-ci est le seul faux, et il vit à deux endroits de la même pièce.
- Déjà consigné : **NOUVEAU**.

#### III.A.4 [note] Une borne du ch. 28 dérive de la date que R-IV-88 a défaite
- Pièce : `28-valeurs-mobilieres-acvm-11-348.md`, § 28.2.
- Constat : la borne « d'au moins quinze mois et vingt-cinq jours » se calcule depuis le **30 mars 2026** — la date arbitrée dont R-IV-88 a établi qu'elle ne figure pas aux pages officielles. L'énoncé demeure vrai comme borne inférieure, mais sa dérivation repose sur l'objet que l'arbitrage a déclaré inexistant, et la pièce ne le signale pas.
- Déjà consigné : la requalification de la date, oui ; la dépendance de ce cardinal-ci : **NOUVEAU**.

#### III.A.5 [mineur] Une entrée de socle annoncée « citée en renvoi » ne résout contre aucune occurrence du corps
- Pièce : `28-valeurs-mobilieres-acvm-11-348.md`, en-tête et note, point 1.
- Constat : l'en-tête déclare « l'entrée héritée **H-07** du Vol. III est citée une fois, en renvoi ». H-07 n'apparaît **nulle part dans le corps** — uniquement dans l'en-tête et la note elle-même. Le renvoi annoncé est invérifiable sur pièce.
- Déjà consigné : **NOUVEAU**.

#### III.A.6 [mineur] Les décomptes d'occurrences des champs « Garde-fous balayés » ne sont pas reproductibles (ch. 25, 27)
- Pièces : ch. 27 (« aucun avis juridique : sept occurrences » — quatre trouvées, aucune aux § 27.4, § 27.6, § 27.7) ; ch. 25 (« "attendu par E-23" : onze occurrences » dont « § 25.4 (trois) » — le § 25.4 n'en porte aucune littérale, six dans tout le corps).
- Constat : les comptes recensent manifestement des « applications » interprétées, sans que le critère soit déclaré. (Instance de T-1.)
- Déjà consigné : **NOUVEAU**.

#### III.A.7 [note] Décompte croisé discordant entre le ch. 27 et le tableau 25.1
- Constat : le ch. 27 § 27.5 écrit « deux des cinq questions y trouvent un appui, dont un seul est net » ; le tableau 25.1 donne **trois** questions pourvues d'un appui (Q-A net ; Q-B et Q-D partiels, en structure strictement parallèle).
- Déjà consigné : **NOUVEAU**.

#### III.A.8 [note] F-68 employé sans niveau déclaré à l'en-tête du ch. 25
- Constat : le corps cite « Vol. III F-68 » ; l'en-tête ne lui déclare aucun niveau (le ch. 27 le donne : [B]).
- Déjà consigné : **NOUVEAU**.

#### III.A.9 [note] Renvois de section au Vol. I sans marqueur de document
- Pièces : p. ex. ch. 25, clôture R-IV-84 (« couverte en [C] par le Vol. I §5.3.7 ») ; pratique éparse.
- Constat : la décision 7 exige que tout renvoi nomme son document ; « Vol. I §5.3.7 » nu est théoriquement ambigu (Monographie/Synthèse). La pratique suit celle des tables détaillées du TOC lui-même, et la Synthèse n'est plus au dépôt : ambiguïté théorique seulement.
- Déjà consigné : la convention stricte, oui ; ces occurrences relâchées : **NOUVEAU**, sans conséquence pratique constatée.

#### III.A.10 [note] Sections § N.0 et « Synthèse » hors table du TOC — convention de fait, jamais posée en règle
- Constat : les tables détaillées ne prévoient ni ouverture § N.0 ni synthèse pour ces chapitres ; chaque pièce déclare l'ajout. Convention cohérente d'une pièce à l'autre (et retrouvée aux autres Livres), jamais écrite au plan ni au skill.
- Déjà consigné : oui, pièce par pièce ; l'absence de règle : observation sans action requise.

### 6.4 Volet B — ch. 22-24

#### III.B.1 [majeur] Les attestations de balayage des trois pièces ne résistent pas à la re-mesure
- Pièces : ch. 22, 23, 24 (champs « Garde-fous balayés » et notes de statut).
- Constat, par balayage exhaustif des fichiers entiers : **ch. 22** — « quinze occurrences » de « Lecture de l'auteur » (dix-neuf réelles, toutes suivies du couple « Ce que le socle établit / n'établit pas ») ; R-14 : total exact (six) mais répartition fausse (l'occurrence du § 22.3 comptée au § 22.4) ; R-13 : « deux occurrences, § 22.0 et § 22.9 » — une seule localisable, le § 22.9 n'en portant aucune. **Ch. 23** — R-02 : « § 23.1 et § 23.5 » — seule celle du § 23.1 est localisable ; R-14 : « sept occurrences […] portent leur degré » — quatre degrés explicites seulement, et la répartition ne se réconcilie pas. **Ch. 24** — R-13 : « trois occurrences, § 24.2, § 24.6 et § 24.9 » — quatre réelles, aucune au § 24.6 ; R-14 : « neuf occurrences […] portent leur degré » — sept marqueurs réels, dont un au § 24.4.2 absent de la répartition, et aucun au § 24.7 pourtant crédité de deux ; PRD §8.4 : « § 24.0 et § 24.1 » — une seule localisable. (Instance de T-1, la plus dense du corpus avec le volet D.)
- Déjà consigné : **NOUVEAU**.

#### III.B.2 [majeur] Ch. 23 : huit emplois nus de F-xx contre l'attestation « préfixés à chaque emploi »
- Pièce : `23-frameworks-orchestration-entreprise.md`, tableaux 23.1 et 23.2.
- Constat : la note atteste « les identifiants cités — F-15, F-16, F-32, F-33, F-41 — sont ceux du Vol. II, **préfixés à chaque emploi** (décision 7) ». Huit emplois nus figurent aux deux tableaux (« [B] (F-15) », « (F-33) »…). La légende du tableau 23.1 nomme le gel du Vol. II (atténuant) ; celle du tableau 23.2 ne nomme aucun socle. Dans un dépôt où « un F-xx nu est indécidable entre deux socles », l'attestation est fausse telle qu'écrite.
- Déjà consigné : **NOUVEAU**.

#### III.B.3 [majeur] Ch. 24 : le faux ami « plan de contrôle » employé sans désambiguïsation au § 24.6.2, contre l'attestation « à chaque emploi »
- Pièce : `24-passage-echelle-entreprise.md`, en-tête et § 24.6.2.
- Constat : l'en-tête atteste que le faux ami est employé « des § 24.1 et § 24.2 » et que « la distinction est écrite **à chaque emploi** ». Deux autres emplois existent : tableau 24.1 (désambiguïsé en légende) et **§ 24.6.2 : « séparation du plan de contrôle et du flux de données non fiable » — sans aucune désambiguïsation**, alors que cet emploi-là est précisément le sens sécurité le plus proche du *control plane* que R-13 vise.
- Déjà consigné : **NOUVEAU**.

#### III.B.4 [mineur] Ch. 22 : deux F-xx nus, sous-titres reformulés, synthèse hors attestation de structure
- Constat : *(a)* § 22.7 : « une autrice de **F-37** cosignant **F-36** » — deux emplois nus, contre l'attestation « préfixés à chaque emploi » (le contexte immédiat tranche). *(b)* Deux intitulés de sous-sections s'écartent du TOC (« batch/streaming » → « lots/flux » ; « déterministe vs agentique » → « déterministe et agentique — la charnière »). *(c)* La section « Synthèse » se déclare in situ construction d'éditeur mais est absente de l'attestation de structure de la note, qui ne nomme que le § 22.0 comme ajout.
- Déjà consigné : **NOUVEAU** (les trois points).

#### III.B.5 [mineur] Ch. 23 : anonymisation à géométrie variable au § 23.3
- Constat : le § 23.3 anonymise l'éditeur (« un éditeur ») alors que le tableau 23.1 (« Confluent / Kafka ») et la thèse le nomment ; les § 23.1-23.2 nomment leurs produits. Le lecteur recompose l'identité par le tableau — l'anonymisation ne protège rien et crée une asymétrie de traitement entre offres. (Instance de T-4.)
- Déjà consigné : **NOUVEAU**.

#### III.B.6 [mineur] Ch. 24 : titre du § 24.7 amputé de « (B2B) » ; grille des dix risques jamais attribuée ; trois listes de sièges discordantes
- Constat : *(a)* le TOC intitule « Interopérabilité inter-entreprises **(B2B)**… » ; la pièce retranche « (B2B) », sans déclaration. *(b)* Le TOC nomme la source de la grille du § 24.3.4 — « OWASP Non-Human Identities Top 10 (2025) » ; la pièce présente les dix risques **sans jamais nommer leur auteur ni leur date**, alors que l'objet anonymisé est le **domicile lui-même**. *(c)* La note annonce « les cinq sièges amont que ce chapitre touche » ; le corps renvoie à davantage, et l'en-tête donne une troisième liste — trois énumérations, trois contenus.
- Déjà consigné : **NOUVEAU** (les trois points).

#### III.B.7 [note] Ch. 22 : la dérivation volumétrique annoncée ne reconstruit pas la cible
- Constat : 90 000 × 10/88 ≈ 10 230 mots ; la cible est 8 500 alors que les dix sections sont dites « majorées du poids de ses deux mouvements » — une majoration devrait porter la cible au-dessus du prorata, non en dessous. La dérivation, telle qu'écrite, est irreproductible.
- Déjà consigné : **NOUVEAU**.

#### III.B.8 [note] Ch. 24 : le fil N×M → N+M court sur cinq sections pour deux annoncées
- Constat : redite assumée et comptée par la pièce pour la triple rencontre avec la limite du ch. 17 § 17.5 ; le fil N×M, déclaré « fil rouge » avec ouverture au § 24.2 et fermeture au § 24.9, court en réalité sur cinq sections. Déclaré partiellement.
- Déjà consigné : partiellement (la pièce) ; le décompte réel : **NOUVEAU**.

#### III.B.9 [note] Conformités vérifiées (volet B, à décharge)
- Constat : thèses des ch. 22 (les deux), 23 et 24 **verbatim** contre le TOC courant ; lignes Fusion couvertes en entier, arrivées déclarées aux deux bouts ; § 24.6 couvrant le §4.7.4 conformément au dépliage v0.27 ; § 24.8 exactement au régime de repli prescrit ; les deux domiciles du ch. 24 marqués ; huit renvois de sièges au ch. 24, zéro reconstruction ; tous les décomptes du corps du ch. 24 re-comptés exacts ; distinction CrewAI à trois niveaux tenue au ch. 23 ; garde-fou des métriques appliqué à chaque occurrence citée.
- Déjà consigné : oui pour l'essentiel (notes de statut) ; constaté exact.

### 6.5 Volet C — ch. 29-32

#### III.C.1 [majeur] Ch. 30 : l'en-tête de socle omet deux entrées que le corps cite
- Pièce : `30-maillage-reglementaire-normalisation.md`, en-tête et § 30.3.2.
- Constat : le corps cite « Vol. III F-33, [B] » et « Vol. III F-34, [A] » au § 30.3.2 ; l'énumération du champ « Socle mobilisé » ne les contient pas, et aucune clause « en renvoi » ne les couvre.
- Déjà consigné : **NOUVEAU**.

#### III.C.2 [mineur] Décomptes de garde-fous non reproductibles dans les quatre pièces
- Constat : la règle de comptage (applications vs marqueurs littéraux) n'est énoncée nulle part et le comptage littéral diverge systématiquement — ch. 30 : « R-5 : sept occurrences », trois littérales ; « R-13 : une occurrence, § 30.1.1 », deux littérales (seul **sous-compte** relevé) ; ch. 32 : « R-5 : neuf occurrences », trois littérales ; ch. 29 : trois décomptes sans occurrence localisable (« aucun avis juridique : § 29.3 (deux) » — une seule ; « couverture par inférence : …et la synthèse » — aucune dans la synthèse ; « attendu par E-23 : § 29.2 » — la formulation n'y apparaît pas). (Instance de T-1.)
- Déjà consigné : **NOUVEAU**.

#### III.C.3 [mineur] Tri prospectif employé sans renvoi au siège aux ch. 30 et 31 — la dette S5 est plus large que déclarée
- Pièces : ch. 30 § 30.3.1, § 30.3.2, tableau 30.3 ; ch. 31 § 31.1.2.
- Constat : ces deux pièces manquent à la liste des six pièces non renvoyantes consignée à la désactivation de S5 (ch. 13, 18, 19, 20, 25, 37). L'écart s'explique par la concurrence des passes — le siège a été désigné le même jour, par l'autre passe — mais il n'est écrit nulle part. (Instance de T-3.)
- Déjà consigné : **NOUVEAU**.

#### III.C.4 [mineur] Intitulés de sous-sections des ch. 30 et 31 réécrits par rapport au TOC, sans déclaration
- Constat : dénominations retirées (« AI Act », « ISO/IEC 42001 », « DORA », « ISO 20022 », « BIAN, FIBO », « FINOS AI Governance Framework v2.0 », « serveurs MCP »…) et anglicismes francisés. Présence et ordre conformes ; les ch. 29 et 32 collent au plan verbatim — la déviation n'est pas une convention uniforme du Livre, et les notes de statut affirment suivre la table « dans l'ordre exact » sans déclarer l'écart de titres (décision 8). (Instance de T-4.)
- Déjà consigné : **NOUVEAU**.

#### III.C.5 [mineur] Ch. 30 : le statut aplatit une distinction que le corps construit
- Constat : « sept instances de normalisation dont les travaux sont pré-normatifs » — le corps établit le contraire pour deux d'entre elles (Recommandations W3C v2.0 du 15 mai 2025 et v1.0 du 19 juillet 2022) ; la formule exacte du corps réserve « pré-normatif » au seul travail spécifique à l'agent.
- Déjà consigné : **NOUVEAU**.

#### III.C.6 [mineur] Ch. 31 : siège renommé, renvois nus dans les bandeaux, énumération boiteuse
- Constat : *(a)* § 31.2.6 : le TOC écrit « SIÈGE du critère **anti-hype** », la pièce « SIÈGE DU CRITÈRE **ANTI-EMBALLEMENT** » — R-IV-94 affirme pourtant que les six sièges sont ceux « que le TOC déclare en toutes lettres » ; au versement dû à `check-sieges.py`, une signature sous un nom que le plan déclare sous un autre est la classe d'indécidabilité que la décision 7 proscrit. *(b)* Bandeaux de siège : renvois inter-chapitres nus (« les § 34.1, § 34.4 … y renvoient » sans « ch. 34 »), hors convention. *(c)* § 31.4.2 : « Trois phénomènes se conjuguent » suivis de deux marqueurs seulement.
- Déjà consigné : **NOUVEAU** (les trois points).

#### III.C.7 [mineur] Friction inter-pièces publié/pris entre les ch. 30 et 32
- Constat : le tableau 30.2 proscrit d'écrire « aucun arrêté n'a été **pris** » (degré 3) ; le ch. 32 § 32.4 écrit « a établi qu'aucun arrêté de désignation n'avait été **publié** à cette date ». La distinction qui porte toute la charge — *publié* dans les sources balayées ≠ *pris* à l'index non balayé — n'est nommée nulle part ; un lecteur des deux chapitres butera sur l'apparente contradiction.
- Déjà consigné : partiellement (le ch. 32 porte le résidu degré 3) ; le couple publié/pris implicite : **NOUVEAU**.

#### III.C.8 [note] Ch. 29 : les trois sources du § 29.2 jamais nommées en corps ; ch. 32 : F-24 invérifiable
- Constat : *(a)* F-36, F-37 et F-46 — que le TOC nomme à la ligne de section — ne sont jamais citées dans le corps du § 29.2 ; la « formule opposable » du chapitre devient difficile à sourcer depuis la pièce seule. *(b)* Ch. 32 : « F-09, F-25 et F-24 … en renvoi seulement » — F-24 n'a aucune occurrence repérable, même indirecte.
- Déjà consigné : **NOUVEAU**.

#### III.C.9 [note] Ch. 31 § 31.1.3 : « à valeur de fait juridique établi » sous un régime intégralement [C]
- Constat : formule la plus assertive du chapitre, sous un régime que la pièce déclare elle-même « repérage documentaire, aucun fait central ». Tension de régime, non commentée à l'occurrence.
- Déjà consigné : **NOUVEAU**.

#### III.C.10 [note] Conformités vérifiées (volet C, à décharge)
- Constat : les quatre thèses **identiques mot à mot** au TOC courant (y compris gras et « (fait négatif vérifié) » au ch. 32) ; chapitre-pivot du ch. 29 conservé intact, table non augmentée, cardinal du tableau 29.1 re-compté exact ; les six marqueurs de siège du ch. 31 présents, aucune reconstruction dans les quatre pièces ; § 30.2.1 instancie sans re-dériver ; toute l'arithmétique des dates du ch. 32 refaite et exacte ; R-IV-91 à R-IV-95 conformes à leur consignation.
- Déjà consigné : oui ; constaté exact.

### 6.6 Volet D — ch. 33-36

#### III.D.1 [majeur] Anonymisation systématique des noms propres, non déclarée — à son plus aigu
- Pièces : les quatre.
- Constat : « Paiements Canada » → « l'opérateur » (le nom ne survivant que dans la thèse citée), « CBPR+ » → « l'échéance mondiale du réseau de messagerie interbancaire », « By-law no 10 » → « le règlement administratif », « AP2 » → « le protocole de paiement agentique » (le sigle ne subsistant qu'au titre du ch. 36), « FIDO Alliance » → « une alliance », « v0.2.0 » → « une version de spécification », et les quatre identifiants arXiv du § 36.5 absents. Trois conséquences vérifiables : au ch. 34, l'attribution « à chaque occurrence » s'adosse à des attributeurs anonymes ; au ch. 35 § 35.4, la pièce affirme que l'institution « nomme une brique » — sans nommer la brique ; au ch. 36 § 36.5, le critère de clôture déclaré est « l'extraction des quatre préimpressions à leur source primaire », mais la pièce ne porte aucun des quatre identifiants qui permettraient de les retrouver. Ni le skill, ni le README, ni les notes de statut ne déclarent cette convention. (Instance de T-4, le cas le plus net.)
- Déjà consigné : **NOUVEAU**.

#### III.D.2 [majeur] Ch. 33 : F-45 annoncé, jamais mobilisé
- Pièce : `33-iso-20022-lynx-rtr.md`, en-tête et note.
- Constat : l'en-tête et la note annoncent F-45 (« préfixés à chaque emploi ») ; le corps ne le cite **nulle part** (balayage du fichier entier : deux occurrences, en-tête et note, zéro emploi). Le § 33.3 — candidat naturel — attribue ses trois dates à F-29. Soit une entrée de socle assignée par le plan et non consommée, soit une mésattribution.
- Déjà consigné : **NOUVEAU**.

#### III.D.3 [majeur] Ch. 34 : renvois promis au § 34.2.2 absents — et un neuvième siège possible, ni compté ni versé
- Pièce : `34-sous-domaines-financiers.md`, § 34.2.2.
- Constat : la sous-section se déclare « siège de la grille d'architecture des plateformes d'assurance de dommage » et affirme « les § 34.5.2 et § 34.5.6 y renvoient sans la re-dériver ». **Ni l'un ni l'autre ne renvoie au § 34.2.2** (seule autre occurrence : une cellule du tableau 34.1). Le siège annoncé n'a aucun renvoi entrant dans la pièce. En outre, le TOC marque le § 34.2.2 « SIÈGE » : s'il l'est au sens de `check-sieges.py`, il serait un **neuvième** siège du Livre III, absent de la dette déclarée (« huit sièges — six au ch. 31, deux domiciles au ch. 24 »). (Recoupe T-3.)
- Déjà consigné : **NOUVEAU**.

#### III.D.4 [mineur] Ch. 33 : attestations d'en-tête et de note contredites par le corps
- Constat : *(a)* la note atteste « le mot “lancé” n'apparaît qu'au conditionnel attribué ou dans la formule qui l'interdit » — le § 33.1 écrit « le système est **lancé le 1ᵉʳ septembre 2021** » (indicatif, à propos de Lynx ; la réserve F-29 elle-même n'est pas violée, elle vise le RTR — c'est l'attestation qui est fausse sur son propre domaine). *(b)* La formulation imposée : « trois occurrences, § 33.2 » — trois existent, mais ni toutes au § 33.2, ni toutes verbatim (la synthèse porte une forme abrégée). *(c)* L'arithmétique de R-IV-96 : l'énumération de la remontée liste trois intervalles sur quatre, deux des quatre sont calculés au § 33.3 et non au § 33.2, et « un exercice décalé déplacerait les quatre » est faux pour l'intervalle à deux dates fixes. (Instances de T-1.)
- Déjà consigné : la remontée R-IV-96 elle-même, oui ; ces trois points : **NOUVEAU**.

#### III.D.5 [mineur] Ch. 34 : trois décomptes non reconstructibles
- Constat : *(a)* la cible volumétrique dérivée « au prorata des trente-trois sous-sections » — le dépliage du TOC sur le périmètre de la ligne donne trente-sept, et la pièce elle-même en compte trente-sept ; le décompte exclut le §5.14 sans le déclarer. *(b)* Le décompte des réserves « hors corpus » (« six fois dans son ch. 5 ») ne se laisse reconstruire d'aucune combinaison des listes de la note et du tableau 34.1 — la réserve du § 34.2.5 est absente des énumérations, et le tableau ne marque qu'une ligne, non trois. *(c)* R-13 : « trois occurrences, § 34.1, § 34.4 et § 34.7 » — quatre réelles, celle du § 34.5.3 ni comptée ni localisée.
- Déjà consigné : R-IV-97 et son issue, oui ; l'arithmétique de ses occurrences et les deux autres points : **NOUVEAU**.

#### III.D.6 [mineur] Ch. 35 : deux décomptes de bandeau et des encadrés partiels
- Constat : *(a)* PRD Vol. II §3 : « trois occurrences, § 35.1, § 35.7 et § 35.8 » — quatre littérales, celle du § 35.6 omise. *(b)* L'incise « § 35.8 (quatre, dont un fait négatif vérifié au § 35.6) » contredit la partition qu'elle annonce — le fait négatif est au § 35.6, il ne peut être « dont » des quatre du § 35.8. *(c)* Le TOC exige que les résidus [C] et l'absence BNC vivent « en encadrés » : l'absence BNC en a un ; les résidus BMO et Sun Life sont en texte courant gras.
- Déjà consigné : **NOUVEAU**.

#### III.D.7 [mineur] Ch. 36 : renvois source sans document nommé
- Constat : « le Vol. I, à son §5.13.4, décrit… » (§ 36.1 et clôture R-IV-99) — sans nommer *Monographie*, que la décision 7 exige (l'ouverture du § 36.2 le nomme, elle). Même classe au ch. 34 § 34.7 (« Section reçue du §5.14 du Vol. I »). Le contexte tranche, mais c'est la forme nue que la décision proscrit.
- Déjà consigné : **NOUVEAU**.

#### III.D.8 [note] Ch. 34 : §5.7.5-5.7.7 couverts par renvoi seul ; ch. 35 : § 35.8 subdivisé hors dépliage
- Constat : *(a)* le dépliage du § 34.1 porte sept thèmes ; la pièce en développe quatre et traite les trois derniers en une sous-section de renvois — la table de couverture annonce « condensé », et un renvoi n'est pas un condensé. *(b)* Le plan impose au ch. 35 « trois institutions dans une seule section » ; la pièce subdivise le § 35.8 en 35.8.1-35.8.3 — compatible avec la lettre, à faire arbitrer.
- Déjà consigné : partiellement (renvois déclarés) ; l'écart au dépliage : **NOUVEAU**.

#### III.D.9 [note] Conformités vérifiées (volet D, à décharge)
- Constat : les quatre thèses **identiques mot à mot** au TOC courant, marqueurs prospectifs correctement traités ; le régime prospectif du ch. 36 tenu condition par condition — aucune condition glissée en prédiction, lacune §10.5 exposée jamais comblée, les deux états datés du transfert AP2 portés avec « le Vol. II ne se corrige pas » ; le garde-fou §7.5 au ch. 35 exécuté exemplairement (chaque métrique avec attributeur, date, support, démonstration arithmétique de non-additivité) ; les onze entrées de socle du ch. 35 nommées une à une, en-tête et corps ; R-IV-97 appliquée — chaque affirmation hors corpus porte sa réserve, aucune versée ; sièges respectés par renvoi aux ch. 17, 18, 19, 31, 48 ; legs du ch. 33 repris tel quel au ch. 36 ; tableau 34.3 aligné sur le ch. 33 ; arithmétique interne du ch. 35 recomptée, tout est juste.
- Déjà consigné : oui pour l'essentiel (notes de statut) ; constaté exact.

### 6.7 Volet E — consolidation (constats de plan et recoupements)

#### III.E.1 [majeur] La table détaillée du § 34.2 est plus étroite que sa source — et l'écart n'est pas remonté
- Pièces : TOC v0.28, entrée du ch. 34 ; `34-sous-domaines-financiers.md`.
- Constat : la table détaillée déplie le § 34.2 sur « §5.8.1-5.8.4 » (quatre objets). La source en porte **six** — vérifié sur `1 - Corpus/1 - InteroperabiliteAgentique/Monographie.md` : §5.8.5 (réassurance) et §5.8.6 (régime réglementaire propre) existent. La pièce a suivi la ligne Fusion (« §5.7-5.11 ») et couvre les six (§ 34.2.5, § 34.2.6) — **la matière n'est pas perdue** —, mais l'écart plan/pièce n'est déclaré nulle part : la note de statut atteste « la structure suit la table détaillée dans l'ordre exact » sans le signaler, et aucune remontée ne le porte. C'est la classe exacte de R-IV-80 (ch. 24 § 24.6.4), qui avait été remontée et soldée par réalignement du TOC ; ici le TOC v0.28 reste incomplet — la collation manuelle, parade déclarée de cette classe, a manqué ce cas.
- Déjà consigné : la classe, oui (R-IV-80) ; **cette instance : NOUVEAU**.

#### III.E.2 [majeur] Le TOC se contredit entre l'entrée du ch. 27 et l'issue de R-IV-88
- Pièce : TOC v0.28, entrée du ch. 27 (deux occurrences) contre le journal v0.26 et le README du Livre.
- Constat : l'entrée écrit toujours « **finale le 30 mars 2026** — divergence tranchée, voir Annexe C ». Or l'issue de R-IV-88 établit qu'aucune des deux dates arbitrées ne figure aux pages officielles, que « l'arbitrage qui la tranchait portait sur un objet inexistant » et que « la somme écrit “avril 2026” et déclare les trois états ». Les réalignements R-IV-87 et R-IV-89 ont été portés à l'entrée ; R-IV-88 n'y a laissé aucune trace : un rédacteur qui suivrait l'entrée écrirait l'état que l'arbitrage a réfuté. Le ch. 30 § 30.2.7, lui, présente correctement la divergence à trois termes — la pièce est saine, le plan ne l'est pas. (Classe « désalignement interne au plan », sixième instance ; recoupe T-6.)
- Déjà consigné : la classe ; **cette instance : NOUVEAU**.

#### III.E.3 [mineur] Ch. 32 : renvoi de la lacune PRD Vol. II §10.11 divergent du plan
- Pièce : `32-cadre-bancaire-consommateur.md`, § 32.4.
- Constat : le TOC route la lacune §10.11 par « renvoi Annexe D » (deux occurrences à l'entrée du ch. 32) ; la pièce écrit « son état final sera enregistré au ch. 49 » — sans reprendre le renvoi Annexe D ni déclarer la substitution. Les deux destinations ne sont pas nécessairement incompatibles, mais la pièce ne reproduit pas le renvoi du plan et l'écart n'est pas déclaré.
- Déjà consigné : **NOUVEAU**.

#### III.E.4 [mineur] Ch. 30 : H-19 déclarée au socle mobilisé et jamais employée au corps
- Pièce : `30-maillage-reglementaire-normalisation.md`, en-tête.
- Constat : complément inverse de III.C.1 — l'en-tête déclare **H-19 [C]** au champ « Socle mobilisé », et l'entrée n'apparaît nulle part dans le corps. Avec F-33/F-34 citées et non déclarées (III.C.1), le champ diverge du socle réellement employé dans les deux sens.
- Déjà consigné : **NOUVEAU**.

#### III.E.5 [note] Un second siège au nom divergent, et des listes de consommateurs incohérentes entre trois documents
- Pièces : ch. 31 § 31.3.4 et § 31.1.1 ; TOC ; README du Livre.
- Constat : *(a)* outre « anti-hype »/« anti-emballement » (III.C.6), le TOC nomme le siège du § 31.3.4 « **four-eyes** » quand la pièce et le README écrivent « **quatre-yeux** » — au versement dû à `check-sieges.py`, la signature devra choisir un libellé, et le plan, la pièce et l'appareil divergeront si personne ne le remarque. *(b)* Le marqueur du siège d'irréversibilité (§ 31.1.1) énumère cinq points renvoyants ; le README en nomme trois chapitres ; le relevé réel en trouve davantage (ch. 33 § 33.4 et une demi-douzaine de points du ch. 34). Aucun renvoi n'est fautif — c'est la liste énumérative qui sous-compte, et trois documents donnent trois listes.
- Déjà consigné : la dette de versement, oui ; les divergences de nom et de listes : **NOUVEAU**.

#### III.E.6 [note] Menus écarts de forme relevés en passant
- Constat : *(a)* ch. 29, tableau 29.1, rangée ACVM : « CA-5 » nu dans la cellule — la série est nommée au bandeau mais pas au point d'emploi, occurrence unique et faible de la classe que la décision 7 proscrit. *(b)* Ch. 36, clôture R-IV-99 : « v0.2 » là où l'entrée du TOC écrit « v0.2.0 » — et une autre entrée du plan écrit aussi « v0.2 » : les deux formes coexistent dans le plan même.
- Déjà consigné : **NOUVEAU** (notes).

#### III.E.7 [note] Vérifications à décharge de la consolidation
- Constat : les onze thèses du lot (douze blocs, le ch. 22 en portant deux) sont conformes **caractère par caractère** au TOC v0.28 ; toute l'arithmétique re-calculée est exacte — durées calendaires des ch. 32, 33, 35, 36, pourcentages et sommes de sections (le « dix sur quatre-vingt-huit » du ch. 22 se re-somme exactement) ; aucune contradiction inter-chapitres de fond (dates E-23, reports européens, 170 G$ attribué aux deux occurrences, état instruit du transfert AP2 cohérent jusque dans l'entrée du ch. 10 du TOC) ; aucune reconstruction des huit sièges du Livre dans les onze pièces — les incohérences arithmétiques des sources (courriels vs demandes, experts vs modèles) sont détectées et déclarées non additionnables par les pièces elles-mêmes.
- Déjà consigné : constat de conformité.

### 6.8 Commentaire éditorial

Sur le fond, le Livre III est d'une discipline épistémique remarquable, et c'est sa force principale : la distinction fait établi / lecture de l'auteur est tenue phrase à phrase, les trois degrés d'absence sont maniés sans confusion, et les tableaux à cases vides déclarées (25.1, 27.3, 29.1) sont un dispositif rare — un texte réglementaire qui dit ce que son corpus ne porte pas vaut plus qu'un texte qui comble. Les meilleures pièces se répartissent sur les trois mouvements : le ch. 25 (l'analyse de la voie définitionnelle d'E-23 et la lecture inversée de la grille tiennent la thèse sans jamais la durcir), le ch. 32 et le ch. 33 (chaque date re-mesurée juste, le fait négatif vérifié manié avec sa borne exacte), le ch. 35 — la meilleure exécution du garde-fou des métriques du corpus, qui démontre par l'arithmétique pourquoi certains chiffres ne s'additionnent pas au lieu de seulement l'interdire — et le ch. 36, qui réussit l'exercice le plus périlleux du Livre : écrire un chapitre entier sur une rencontre que rien ne documente sans jamais glisser une condition en prédiction. Le ch. 24 est le chapitre-somme du Livre et il tient : le principe de greffe fait une vraie colonne vertébrale, la discipline des sièges y est la meilleure du mouvement, et le § 24.8 — écrire le vide sans écrire de doctrine — est un modèle du genre. Le ch. 26 démontre qu'un petit chapitre peut être complet. Les faiblesses sont de deux ordres. D'abord la charge d'apparat : en-têtes, notes de statut et clôtures représentent une fraction substantielle de chaque pièce, et leurs décomptes auto-déclarés créent une surface de vérification que rien n'outille — l'ironie du Livre est que le tableau de balayage des garde-fous, instrument de la rigueur affichée, est l'endroit où les erreurs se concentrent, dans les douze pièces sur quinze concernées. Ensuite l'anonymisation, qui atteint ici sa limite fonctionnelle : un chapitre dont le programme est « instruire à la source » et qui ne nomme ni les protocoles ni les préimpressions (ch. 36), un domicile de grille dont l'auteur n'est jamais nommé (ch. 24), des attributions qui s'adossent à des attributeurs anonymes (ch. 34) — la parade de péremption commence à coûter plus qu'elle ne protège. La saturation en marqueurs d'avertissement, enfin, érode leur valeur de signal dans les pièces les plus denses : quand tout est alerte, rien ne l'est. La classe de constats III.A.1-III.A.2 mérite l'attention au-delà du Livre : une passe d'arbitrage qui réaligne le plan sans repasser sur les citations des pièces fabrique mécaniquement des discordances pièce/plan que ni `check-toc.py` ni `verifier-piece.py` ne voient — cinquième variante d'un fait de méthode que le dossier documente déjà quatre fois. Enfin, la consolidation renverse un rapport attendu : dans ce Livre, le texte rédigé est en meilleur état que le plan qui le régit — les pièces ont couvert le §5.8 en entier et exposé la divergence de dates correctement, pendant que la table détaillée du § 34.2 et l'entrée du ch. 27 restaient périmées (III.E.1, III.E.2).

---

## 7. Livre IV — dix chapitres (ch. 37-46)

### 7.1 Synthèse

Les dix pièces du Livre IV existent en `.md` et `.html`, portent l'en-tête à cinq champs du PRD §6, se déclarent « brouillon de rédaction, non publiable » et closent sur une note de statut hors plan — la conformité de forme est tenue à un niveau qui dépasse les trois Livres précédents. Le corps des pièces applique avec constance le régime de preuve : degrés d'absence portés à chaque occurrence, métriques attribuées, « Lecture de l'auteur » suivie de ce que le socle établit et n'établit pas, conditions de réfutation écrites comme telles. Les écarts lourds — rédaction hors G-3/G-4/G-5, ch. 41 avant G-6 et D-8, dix thèses sur douze désalignées, collision d'identifiants R-IV-60…69, désalignements internes au plan — sont tous déjà consignés au README du Livre, au TOC v0.28 et au `CLAUDE.md` ; l'audit les confirme sans les requalifier. Le neuf se loge dans l'appareil de second rang : deux marqueurs de siège non versés à `check-sieges.py`, un README qui affirme que les clôtures vivent dans les notes de statut alors que celles-ci ne consignent que les ouvertures, des notes de statut périmées sur le périmètre de leur propre passe, et quelques cardinaux annoncés non re-mesurés. L'écart d'un mot de la volumétrie est localisé et expliqué (ch. 45). Rien de ce qui a été trouvé n'est bloquant ; l'essentiel est de la classe « ce qu'aucun outil ne regarde finit par diverger », que le dossier a lui-même nommée.

### 7.2 Volumétrie mesurée

Mesures du 28 juillet 2026, comparées aux cibles dérivées publiées au README (enveloppe du Livre : 69 000 mots).

| Chapitre | Mots mesurés | Cible dérivée | Écart |
|---|---:|---:|---:|
| Ch. 37 | 9 724 | 11 000 | −11,6 % |
| Ch. 38 | 5 628 | 6 000 | −6,2 % |
| Ch. 39 | 6 136 | 6 500 | −5,6 % |
| Ch. 40 | 5 541 | 6 500 | −14,8 % |
| Ch. 41 | 3 329 | 5 000 | −33,4 % |
| Ch. 42 | 3 529 | 4 000 | −11,8 % |
| Ch. 43 | 5 839 | 6 500 | −10,2 % |
| Ch. 44 | 6 016 | 8 500 | −29,2 % |
| Ch. 45 | **6 752** (README : 6 751) | 12 000 | −43,7 % |
| Ch. 46 | 2 756 | 3 000 | −8,1 % |
| **Livre** | **55 250** (README : 55 249) | **69 000** | **−19,9 %** |

Neuf mesures sur dix concordent au mot près avec le README ; la dixième (ch. 45) porte l'écart d'un mot du total (constat IV.6). La dispersion est d'un seul signe — les dix pièces sont sous leur cible, de −5,6 % à −43,7 % — contrairement au Livre III où l'agrégat tenait par compensation ; le déficit se concentre sur les trois chapitres que le README explique (41, 44, 45).

### 7.3 Constats

#### IV.1 [majeur] Deux marqueurs de siège non versés à `check-sieges.py`
- Pièces : `43-architecture-reference-couches.md` § 43.1 ; `44-formalisation-archimate.md` § 44.6.
- Constat : le ch. 43 porte « ⚠ **SIÈGE DE LA COLLISION « FABRIQUE » POUR TOUTE LA SOMME (décision 12c du TOC)** » — forme pleine du marqueur — et le ch. 44 porte « ⚠ **SIÈGE DE LA CONFORMITÉ TRAÇABLE** », que le TOC désigne lui-même « (SIÈGE) » à l'entrée du § 44.6 et dont les ch. 45 § 45.14, ch. 46 et l'Annexe H dépendent. **Ni l'un ni l'autre ne figure à la table `SIEGES`** (douze entrées vérifiées). La règle des trois gestes n'est pas tenue : une reconstruction de la désambiguïsation « fabrique » ou de la chaîne de conformité traçable ailleurs dans la somme passerait tous les contrôles. (Instance de T-3.)
- Déjà consigné : **NOUVEAU** pour le Livre IV — le README (« Sièges posés : trois — versés à l'appareil ») et la clôture de R-IV-59 ne mentionnent ni l'un ni l'autre.

#### IV.2 [majeur] Le README affirme que les clôtures vivent dans les notes de statut ; elles n'y sont pas
- Pièce : `Livre IV/README.md` contre les dix notes de statut (§ 37.10 à § 46.4).
- Constat : le README écrit « Le détail de chaque clôture vit dans la **note de statut de la pièce** qui l'avait ouverte. » Vérification sur les dix pièces : chaque note porte ses remontées sous « Remontées ouvertes par ce chapitre », avec leur demande, et **aucune ne consigne l'issue** — le détail des trente-deux clôtures vit dans le tableau du README lui-même (et au TOC/PRD), nulle part dans les pièces. Les pièces n'ont été retouchées après l'arbitrage que pour la renumérotation (vérifié au diff du commit `0fac01c`), jamais pour y reporter les issues.
- Déjà consigné : **NOUVEAU**.

#### IV.3 [mineur] Les notes de statut des ch. 37-40, 42 et 44 sont périmées sur le périmètre de leur propre passe
- Pièces : § 37.10, § 38.6, § 39.7, § 40.7, § 42.5, § 44.10 (point 3 de chaque note).
- Constat : les notes des ch. 37-40 et 42 déclarent « Ne sont pas rédigés : ch. 41, ch. 43, ch. 45… » — alors que la même passe les a écrits (horodatages 20:57-21:07, commit `0ffc4c3`). Le ch. 44 intègre 41 et 43 mais déclare encore le ch. 45 non rédigé ; seul le ch. 45, dernier écrit, liste les neuf autres. Les notes photographient l'ordre d'écriture et n'ont pas été réalignées sur l'état final de la passe : un lecteur du § 37.10 conclurait à tort que les renvois du ch. 37 vers les ch. 41, 43 et 45 ne résolvent pas contre du texte.
- Déjà consigné : **NOUVEAU**.

#### IV.4 [mineur] Cardinal annoncé non re-mesuré : les occurrences de « Lecture de l'auteur » au ch. 37
- Pièces : `37-maillage-agents-point-application.md`, § 37.10 ; accessoirement ch. 38.
- Constat : la note atteste « les **onze occurrences** de « Lecture de l'auteur » » ; le décompte exhaustif donne **neuf** marqueurs (dix en comptant l'auto-référence de la note) — aucune méthode de comptage ne produit onze. Le ch. 38 annonce « huit » pour sept hors auto-référence (défendable) ; le ch. 39 concorde. (Instance de T-1.)
- Déjà consigné : **NOUVEAU**.

#### IV.5 [mineur] Trois titres de section s'écartent de la table détaillée du TOC sans remontée
- Pièces : ch. 39 § 39.4, ch. 46 § 46.2, ch. 38 § 38.2.
- Constat : le ch. 39 titre « versionner le **mandat**, promouvoir… » là où le plan écrit « versionner le **mandat protocolaire** » — perte d'un qualificatif que le corpus traite ailleurs comme obligatoire (le ch. 45 § 45.10 souligne que « le qualificatif complet de la chaîne est obligatoire à chaque occurrence ») ; le ch. 46 § 46.2 titre « inventorier, encadrer, surveiller » là où le plan et la thèse citée trois lignes plus haut portent « inventaire → encadrement → surveillance » ; le ch. 38 § 38.2 porte « d'OpenTelemetry » pour « OpenTelemetry » (trivial). Aucun des trois n'est signalé en remontée ni réaligné en v0.28 — dans un Livre dont deux remontées portent précisément sur des intitulés.
- Déjà consigné : **NOUVEAU**.

#### IV.6 [mineur] L'écart d'un mot du décompte est localisé : ch. 45, renommage du marqueur de siège après la mesure
- Pièce : `45-blueprint-instancie-cycle-de-vie.md` § 45.6 ; commit `0fac01c`.
- Constat : `decompte.sh` mesure 6 752 mots au ch. 45 contre 6 751 publiés (les neuf autres concordent au mot près) — d'où 55 250 contre 55 249. Le diff `0ffc4c3 → 0fac01c` montre la cause : dans le commit d'arbitrage même qui publie le README, le marqueur « SIÈGE UNIQUE DE CETTE MATIÈRE POUR TOUTE LA SOMME » (9 mots) est devenu « SIÈGE DE L'ORGANISATION DE LA FABRIQUE POUR TOUTE LA SOMME » (10 mots) : la mesure a été prise **avant** cette retouche, dans le commit qui la contient. À un mot près, c'est l'infraction à la règle que ce même README énonce — *un contrôle s'exécute sur le corpus que le commit produit*.
- Déjà consigné : l'écart d'un mot était relevé par la mesure globale de cet audit ; **la localisation et la cause sont neuves**.

#### IV.7 [mineur] Cardinal cité à distance : « douze métriques » au ch. 38 contre « seize au total » au ch. 40
- Pièces : ch. 38, synthèse ; ch. 40 § 40.1.2.
- Constat : la synthèse du ch. 38 écrit « le ch. 40 hérite de cet état pour ses **douze** métriques » ; le ch. 40 re-mesure **seize** métriques (douze de F-90 plus quatre de F-95 — que le ch. 38 § 38.5 mentionne lui-même). Le cardinal du chapitre frère est cité à distance sous sa valeur partielle : à la lecture croisée, les deux chapitres semblent se contredire.
- Déjà consigné : **NOUVEAU**.

#### IV.8 [mineur] Les dix thèses réalignées en v0.28 ne concordent plus avec les blocs de citation des pièces
- Pièces : les dix en-têtes de thèse (tous « citée depuis le TOC.md v0.25 »).
- Constat : l'arbitrage v0.28 a réécrit au TOC dix des douze thèses (seules celles des ch. 44 et 46 concordent aujourd'hui). Les pièces citent toujours verbatim la forme v0.25 périmée — l'ancrage de version est exact et chaque pièce déclare le désalignement sous sa citation, ce qui borne le risque de lecture ; mais aucun document ne déclare si la re-citation est due, à quelle passe, ou si l'état présent est l'état final voulu. Tout contrôle futur de concordance thèse-TOC échouera sur dix pièces sur dix. (Variante (a) de T-2.)
- Déjà consigné : partiellement (désalignements et clôtures au README/TOC) ; le fait que les pièces n'ont pas été re-citées et qu'aucune obligation n'est déclarée : **NOUVEAU**.

#### IV.9 [note] Un « central » hors régime au ch. 45 § 45.4
- Constat : « un fait négatif du socle, **établi et central** » — dans un corpus où « central » est le terme technique de CA-IV-01 et où l'en-tête de la même pièce déclare « Aucun énoncé n'est central au sens de CA-IV-01 ». Le sens visé est manifestement « central pour la section », mais l'emploi du mot réservé hors de son régime est le type d'ambiguïté que les pièces s'interdisent partout ailleurs.
- Déjà consigné : **NOUVEAU**.

#### IV.10 [note] Une numérotation périmée dans la clause de retrait du ch. 41
- Pièce : `41-fabrique-agents.md`, synthèse.
- Constat : « si D-8 tranche pour le retrait, ce chapitre disparaît et **les ch. 42-51 de la numérotation antérieure reviennent** » — la fourchette 42-51 appartient à l'état v0.22 (51 chapitres) ; depuis la fusion v0.23, un retrait ferait revenir les ch. 42-50 en 41-49. La clause décrit un état du plan qui n'existe plus.
- Déjà consigné : **NOUVEAU**.

#### IV.11 [note] Ce que l'audit confirme sans le re-signaler — le consigné tient
- Constat : le cumul de portes (G-3/G-4/G-5, plus G-6 et D-8 pour le ch. 41), les dix thèses désalignées avec domaine déclaré, la collision et la carte R-IV-60…69 → 100…109 (aucun ancien numéro ne subsiste dans les pièces, vérifié par balayage), les deux désalignements internes au plan, le registre des stéréotypes publié sous réserve, la dette de vote F-92/F-96 marquée à chaque mobilisation — tout est déjà consigné et exact sur pièce. Vérifications positives : **D-7 est tenue** (le ch. 37 déclare la fermeture au § 37.0, aucune section ne traite l'accord sous défaillance) ; **le régime du ch. 41 est tenu** (zéro marqueur `←`, zéro F-xx, zéro chiffre, un seul relevé daté déclaré hors socle) ; **le garde-fou 12c est tenu** (balayage complet de « fabrique ») ; **les trois sièges versés portent leur marqueur et ne sont reconstruits nulle part** ; **les renvois du ch. 45 vers ses huit sièges externes résolvent tous** ; parité `.md`/`.html` vérifiée sur les ch. 42 et 46 ; le compte à rebours du ch. 46 et les doubles partitions du ch. 42 sont arithmétiquement exacts.
- Déjà consigné : oui.

### 7.4 Commentaire éditorial

Le Livre IV est le plus discipliné des cinq sur l'appareil épistémique, et c'est à la fois sa force et sa limite. La force : chaque absence porte son degré, chaque chiffre son éditeur, chaque construction son marquage, et les conditions de réfutation (tableaux 37.3 et 41.3) sont parmi les meilleures pages de la somme, parce qu'elles transforment des chapitres d'architecture en énoncés attaquables. Le chaînage inter-chapitres est remarquablement exécuté : le ch. 38 reprend le dossier exactement où le ch. 37 l'a laissé, le ch. 42 fabrique le cahier des charges du ch. 43, et les « legs négatifs » (la clé de jointure manquante, le geste intermédiaire de révocation absent, le dénominateur introuvable) circulent de pièce en pièce sans se reconstruire — l'économie du compendium fonctionne ici comme nulle part ailleurs. La limite : la proportion d'apparat sur matière est la plus haute de la somme ; des sections entières (§ 45.9, § 45.14) sont des suites de renvois commentés, et le lecteur qui n'est pas l'auditeur y lira une architecture qui passe plus de temps à dire ce qu'elle ne dit pas qu'à dire quelque chose. Les deux fusions en deux mouvements sont de qualité inégale : celle du ch. 37 est réussie, tandis que celle du ch. 45 juxtapose plutôt qu'elle ne compose, son second mouvement étant structurellement un inventaire de sièges externes ; sa sous-volumétrie de −43,7 % est expliquée avec justesse, mais elle reste le signe qu'un chapitre annoncé comme « le plus long de la somme » est en réalité le plus délégué. Le ch. 41 tient sa place entre *exploiter* et *composer* mieux qu'on pouvait le craindre : produire cinq lots d'instruction au lieu d'un contenu plausible est exactement ce que son régime exigeait, et sa section la plus forte est la plus négative (§ 41.8, le harnais) ; il reste qu'un chapitre de 3 329 mots dont le seul legs inconditionnel est une désambiguïsation lexicale ne survivra à D-8 que si au moins un lot aboutit. Le ch. 44 est le plus aride mais le plus honnête — publier le registre des stéréotypes « en [C], sous réserve » plutôt que « conforme » est un geste que peu de corpus techniques savent faire. Le ch. 46 est la meilleure clôture possible pour ce Livre : court, daté, et portant le seul énoncé réellement opératoire de la passe. Les redites sont contenues mais réelles : la formule « lacune de couverture couverte, non comblée » et l'exposé du régime [C] sont ré-expliqués dans presque chaque pièce alors qu'un renvoi suffirait. Enfin, les constats IV.1 à IV.4 dessinent une tendance qui mérite l'attention de l'auteur : la qualité du corps des pièces excède maintenant celle de leur périphérie (notes, README, appareil), et c'est dans cette périphérie — celle que les quinze contrôles ne lisent pas — que tous les défauts neufs de cette passe se sont logés.

---

## 8. Livre V — quatre chapitres (ch. 47-50)

### 8.1 Synthèse

Le Livre V est conforme à son plan sur l'essentiel : les quatre pièces existent en deux rendus, portent l'en-tête à cinq champs, se déclarent brouillon non publiable avec note de statut hors plan, citent leurs thèses verbatim depuis le TOC (concordance vérifiée mot à mot, y compris les trois thèses réalignées), suivent l'ordre exact des tables détaillées, et la volumétrie publiée (25 017 mots, −26,4 %) se reproduit au mot près. La discipline de preuve est remarquablement tenue : aucun énoncé des ch. 47-48 n'est présenté comme fait établi, les quatre sections-lots sont des commandes d'instruction bornées (question, corpus, critère de clôture, issue d'échec) qui correspondent exactement aux trois lots de D-3, le ch. 48 ne rouvre pas la matière fermée par D-7, et le ch. 50 reste terminal. Les constats neufs sont d'une autre famille que les écarts consignés : ce sont des défauts de **seconde couche**, produits par la passe d'arbitrage et par les mises à jour de relevés sous concurrence, qu'aucun contrôle n'a vus. Les trois corps contredisent la thèse réalignée qu'ils citent en tête ; le `.html` du ch. 48 omet le bloc de réalignement présent au `.md` ; la ventilation du tableau 50.1 somme à douze pour onze événements ; plusieurs relevés R-14 annoncés « re-mesurés » ne se reproduisent pas ; et le siège du verrou sémantique est marqué au texte sans être versé à `check-sieges.py`, sans dette déclarée. Rien de tout cela ne requalifie le Livre — il reste un brouillon hors portes, bloqué à la publication par D-3 — mais ces défauts documentent le coût résiduel d'un arbitrage qui touche les en-têtes sans relire les corps.

### 8.2 Volumétrie mesurée

| Chapitre | Mots mesurés | Cible dérivée | Écart |
|---|---:|---:|---:|
| Ch. 47 — L'artefact livré | 5 326 | 9 300 | −42,7 % |
| Ch. 48 — La sémantique d'effet | 2 793 | 4 700 | −40,6 % |
| Ch. 49 — Horizon et frontière | 13 458 | 15 800 | −14,8 % |
| Ch. 50 — Péremption et revalidation | 3 440 | 4 200 | −18,1 % |
| **Livre** | **25 017** | **34 000** | **−26,4 %** |

Les −42,7 % et −40,6 % publiés pour les deux chapitres sans socle sont exacts ; la somme des cibles est exacte ; la double règle de dérivation (par front au premier mouvement, au prorata des sections au second) est déclarée à la légende du tableau du README.

### 8.3 Constats

#### V.1 [majeur] Les trois corps contredisent la thèse réalignée qu'ils citent
- Pièces : ch. 47 (§ 47.8), ch. 48 (chapeau), ch. 49 (chapeau, § 49.12).
- Constat : l'arbitrage v0.26 a mis à jour les thèses citées en tête, mais les corps continuent de décrire la forme antérieure. Ch. 47 § 47.8 : « **La thèse du second mouvement pose quatre horloges** » alors que la thèse citée vingt paragraphes plus haut en compte **cinq**. Ch. 48, chapeau : la dissection d'un libellé (« ce n'est spécifié ni par les protocoles ni par l'encadrement ») qui ne figure plus dans la thèse citée. Ch. 49 § 49.12, avertissement (1) : « La thèse parle des “lacunes du socle consolidé” ; ce socle n'existe pas » alors que la thèse citée écrit désormais « des trois socles sources ». S'y ajoutent des mentions « D-2, non prise » restées au corps (ch. 47 § 47.8.1 et § 47.13, ch. 48 § 48.6, ch. 49 § 49.11.4) alors que le bloc de tête du ch. 47 déclare D-2 prise. (Variante (b) de T-2.)
- Déjà consigné : à moitié — les blocs de réalignement déclarent « le corps du chapitre n'a pas changé » ; la **contradiction résiduelle** corps↔thèse n'est nommée nulle part : NOUVELLE. Un lecteur qui ne lit pas le bloc de réalignement lit un chapitre qui se contredit.

#### V.2 [majeur] Le `.html` du ch. 48 omet le bloc de réalignement présent au `.md`
- Pièce : `48-semantique-effet-idempotence-compensation.html` vs `.md`.
- Constat : le `.md` porte, entre la thèse et le chapeau, le bloc « ⚠ **Thèse réalignée au TOC v0.26**… (R-IV-65) ». Le `.html` porte la thèse réalignée mais **pas ce bloc** (« réalignée » : 0 occurrence contre 1 ; « R-IV-65 » : 1 contre 2 ; « quantificateur » : 1 contre 2). Les `.html` des ch. 47 et 49 portent bien leur bloc. Le rendu du ch. 48 a donc été généré depuis un état intermédiaire du `.md`, en infraction à la règle « toute correction se fait au `.md` et se reporte au même commit » — et la vérification de parité ne voit pas cette classe (les titres de sections concordent).
- Déjà consigné : NOUVEAU.

#### V.3 [majeur] Tableau 50.1 : la ventilation annoncée « re-mesurée » somme à douze pour onze événements
- Pièce : `50-peremption-protocole-revalidation.md`, légende du tableau 50.1 (§ 50.2).
- Constat : la légende annonce « Cardinal re-mesuré sur la colonne d'événements : onze événements, dont quatre PROGRAMMÉS, un PROGRAMMÉ sans date d'engagement, un PROGRAMMÉ conditionnel, un PROJETÉ, deux SPÉCULATIFS, un à tri mixte, un sans tri attribué — et un FAIT ÉTABLI ». La ventilation somme à **douze** (4+1+1+1+2+1+1+1) pour un total de onze ; la colonne « Tri » ne porte que **trois** rangées PROGRAMMÉ simples. « Quatre PROGRAMMÉS » devrait se lire « trois ». Le § 50.5 reprend « onze événements » sans voir l'écart. (Instance de T-1 — un cardinal déclaré « re-mesuré » démontrablement faux.)
- Déjà consigné : NOUVEAU.

#### V.4 [majeur] Les relevés R-14 des en-têtes des ch. 47, 48 et 50 ne se reproduisent pas au comptage
- Constat : **ch. 47** — « quinze occurrences… re-mesurées et non estimées » : onze occurrences « degré 3 » (dont une au § 47.1, non listé), et les qualifications de fait négatif sont au § 47.1 (deux) et au § 47.12 (une) — aucune au § 47.4, crédité. **Ch. 48** — « une qualification de fait négatif établi (§ 48.1, reprise du ch. 16 § 16.1) » : le § 48.1 ne contient ni « fait négatif » ni renvoi au ch. 16 § 16.1 (l'énoncé visé est au ch. 47 § 47.12) ; le « ch. 16 § 16.1 » listé au § 48.6 ne résout contre aucun renvoi du corps. **Ch. 50** — « deux énoncés au degré 3 (§ 50.2) » : une seule occurrence littérale. La ventilation du tri au ch. 49 (« quarante-neuf emplois — seize/dix-sept/seize, re-mesuré ») ne se reproduit par aucune règle littérale (15/17/18 ou 14/16/17 selon l'inclusion des définitions) — invérifiable plutôt que fausse. Les décomptes du ch. 49 vérifiables mécaniquement (lacunes : 11 = 11, 22 = 4+7+10+1 ; R-11 ; métriques ; tables de couverture) sont, eux, exacts. (Instances de T-1.)
- Déjà consigné : NOUVEAU.

#### V.5 [majeur] Le siège du verrou sémantique est marqué au texte et absent de l'appareil, sans dette déclarée
- Pièce : `49-horizon-frontiere-connaissance-verifiable.md`, § 49.6 ; `PRD/check-sieges.py`.
- Constat : le § 49.6 porte « **SIÈGE DU VERROU SÉMANTIQUE ET PRAGMATIQUE POUR TOUTE LA SOMME** », l'en-tête le déclare, le TOC le désigne, trois chapitres consommateurs sont nommés (ch. 2, 9, 43). La table `SIEGES` ne le contient pas ; contrairement au tri prospectif (versement partiel consigné avec motif), **aucune remontée, aucune dette, aucun motif** ne couvrent cette absence — le § 49.15 dit seulement « le premier est versé à l'appareil », sans qualifier le sort du second. La règle des trois gestes est tenue à un geste sur trois. (Instance de T-3.)
- Déjà consigné : NOUVEAU.

#### V.6 [mineur] Ch. 47 § 47.13 (3) : reprise du relevé défectueuse — fragment dupliqué et cardinal orphelin
- Constat : la phrase « ⚠ *et ce décompte a bougé DEUX FOIS pendant la rédaction de cette pièce*… » est immédiatement suivie du fragment antérieur qu'elle remplaçait, avec une ponctuation orpheline (« …n'a pas relues**. ; *ce décompte… ») ; et le point (c) affirme « les **dix** cibles du groupe (b) existent toutes en brouillon » alors que le groupe (b) n'énumère que **quatre** renvois. (Variante (c) de T-2.)
- Déjà consigné : NOUVEAU.

#### V.7 [mineur] Ch. 50, R-IV-73 : « plus de la moitié » contredit « dix lignes sur soixante »
- Constat : la remontée écrit « cinquante pièces sur soixante sont rédigées ; un registre dressé aujourd'hui serait vide **pour plus de la moitié de ses lignes** » — avec 50/60 rédigées, les lignes vides sont dix sur soixante, comme le § 50.4 et l'en-tête l'écrivent correctement. Trace d'une mise à jour partielle (vraie à 25 pièces, fausse à 50), débutant par une minuscule — signature du remplacement hâtif. (Variante (c) de T-2.)
- Déjà consigné : NOUVEAU.

#### V.8 [mineur] Ch. 49 § 49.15 : « deux occurrences » suivies de trois sections
- Constat : « “fabrique” est désambiguïsé à ses **deux** occurrences (§ 49.8, § 49.12.2, § 49.14) » — trois sites énumérés pour un cardinal de deux. Les désambiguïsations elles-mêmes sont correctes aux trois endroits (décision 12c tenue).
- Déjà consigné : NOUVEAU.

#### V.9 [mineur] § 49.13.1 : « Trois de ces questions » dont deux ne sont pas dans la table qu'elles commentent
- Constat : le paragraphe suit le tableau 49.4 (les six questions d'agenda), mais seul son item (1) y correspond ; les items (2) et (3) ne sont aucune des six questions du tableau ni de la série du ch. 16 § 16.3. L'antécédent « ces questions » ne résout pas dans la pièce.
- Déjà consigné : NOUVEAU.

#### V.10 [mineur] Ch. 47 : les anciens titres des deux mouvements ne sont pas repris comme intitulés dans la pièce
- Constat : la décision 13a impose que les deux entrées fusionnées soient conservées « en deux mouvements portant chacun **son ancien titre** et son ancien numéro ». La pièce marque la césure par un séparateur, l'étiquette « Thèse du second mouvement » et la renumérotation continue — mais aucun des deux anciens titres n'y apparaît (zéro occurrence). La règle vise le plan, non la pièce ; l'écart est de lisibilité plus que de conformité.
- Déjà consigné : NOUVEAU (constat de forme).

#### V.11 [note] § 49.13.2 : la cinquième sous-question des deux sauts n'est pas nommée
- Constat : quatre sous-questions nommées, « et la cinquième que sa source énumère » — renvoyée à la source sans être dite. Si c'est une discipline de non-reconstruction, elle n'est pas déclarée comme telle ; à la lecture, cela ressemble à une ellipse involontaire.
- Déjà consigné : NOUVEAU.

#### V.12 [note] Relevés horodatés dépassés par les passes concurrentes — exacts à leur date, à ne pas corriger
- Constat : plusieurs cardinaux des notes sont dépassés par l'état final du dépôt (« les Livres III et IV vingt-deux (R-IV-38 à R-IV-59) » au § 49.15 ; « neuf sièges » au README du Livre). Ces relevés se déclarent « arrêtés au commit » : ils sont datés, non faux. (Le README relève toutefois aussi de T-5.)
- Déjà consigné : oui — la collision et sa résolution sont consignées ; les occurrences précises relèvent du régime des relevés gelés.

#### V.13 [note] Intitulés des tables détaillées du TOC du Livre V en numérotation gelée (« chapitre 52 » à « chapitre 57 »)
- Constat : cohérent avec la doctrine des correspondances chaînées, mais non déclaré pour ces intitulés — une passe pressée pourrait les « corriger » et casser la chaîne. (Recoupe T-6.)
- Déjà consigné : implicitement ; la vulnérabilité propre aux intitulés : NOUVELLE.

#### V.14 [note] Vérifications à décharge
- Constat : les thèses concordent **verbatim** avec le TOC courant ; l'ordre et les intitulés des sections suivent les tables détaillées ; parité `.md`/`.html` des titres vérifiée pour les ch. 48 et 50 ; le ch. 48 ne traite pas l'accord sous défaillance (D-7 tenue, absence déclarée au § 48.3) ; les trois lots de D-3 (L1 : § 47.2-47.3 ; L2 : § 47.6 ; L3 : § 48.2 et § 48.5) correspondent exactement aux sections-lots des pièces, chacun avec corpus et critère de clôture ; les sièges de la sémantique d'effet et du tri prospectif sont dans la table et aucune pièce du Livre ne les reconstruit ; le ch. 50 est terminal et cite la bonne décision (la règle de terminalité est la règle (b) de la décision 9, que la pièce nomme correctement).
- Déjà consigné : oui.

### 8.4 Commentaire éditorial

Le Livre V est le plus discipliné des cinq sur le régime de preuve, et c'est sa réussite propre : les ch. 47-48 réussissent l'exercice le plus contre-intuitif du corpus — écrire un chapitre dont le contenu est l'exposition d'un vide — sans jamais céder au plausible, et la formule du § 47.13 (« il consiste à n'avoir rien écrit ») est exacte. Les lots d'instruction sont les mieux bornés du dépôt : question instruisible, corpus nommé, critère de clôture opposable, issue d'échec écrite d'avance, ce qui rend D-3 réellement exécutable. La fusion du ch. 47 tient sur le fond — les deux mouvements partagent régime, porte et issue, et la césure § 47.7/§ 47.8 est nette — mais elle est fragile en surface : sans les anciens titres de mouvement, un lecteur qui entre par le milieu ne sait pas qu'il change d'objet, et le § 47.8 qui contredit sa propre thèse de tête (quatre contre cinq horloges) aggrave cette fragilité. Le ch. 48 est la pièce la plus dense du Livre au mot près : la taxonomie lecture/écriture/engagement et le renversement « la question opérante est “que produit son rejeu” » sont de vrais legs, et le siège arrive à point pour six sections qui le citaient déjà. Le ch. 49 est le meilleur chapitre prospectif du corpus — le tri est appliqué sans défaillance repérée, rien de spéculatif n'y est présenté comme acquis, et les § 49.12-49.14 (registre des lacunes, questions transmises, frontières) sont probablement la matière la plus utile de toute la somme pour un lecteur d'architecture. Le ch. 50 clôt bien : « périmer n'est pas falsifier » et le refus de D-1 d'avancer le gel d'un jour donnent à l'ouvrage une fin qui est une méthode plutôt qu'une péroraison. Cela dit, le Livre ne clôt pas la somme : il documente qu'elle ne peut pas se clore — registre de gel inexistant, protocole de revalidation « écrit et inapplicable », état des lacunes daté d'un jour où la moitié du corpus s'écrivait encore — et il a l'honnêteté de le dire à chaque étage. Les faiblesses sont concentrées et d'une seule famille : presque tous les défauts neufs relevés (V.1, V.2, V.5, V.6, V.7) viennent de la **couche d'arbitrage et de mise à jour**, pas de la rédaction — en-têtes retouchés sans relecture des corps, relevés remplacés à moitié, rendu régénéré depuis un état intermédiaire. C'est la leçon transférable de cet audit : le dossier contrôle bien ce que ses scripts voient et ce que ses rédacteurs déclarent, mais une passe d'arbitrage qui modifie des pièces est une passe d'édition comme une autre, et elle ne relit pas ses diffs ligne à ligne comme les passes de structure ont appris à le faire. Les sections les plus faibles restent le § 47.6 (une section vide qui l'assume, mais dont la valeur dépend entièrement de l'ouverture effective du lot L2) et le § 49.13.1, dont le commentaire des « trois questions inconfortables » flotte sans antécédent. Enfin, la ventilation fausse du tableau 50.1 mérite d'être traitée en priorité : c'est le tableau que toute revalidation future relira en premier, et il est le seul endroit du Livre où un cardinal déclaré « re-mesuré » est démontrablement faux.

---

## 9. Récapitulatif et remontées

### 9.1 Décompte des constats

Décompte re-mesuré sur ce document (motifs `[bloquant]`, `[majeur]`, `[mineur]`, `[note]` des titres de constats) :

| Section | Bloquant | Majeur | Mineur | Note | Total |
|---|---:|---:|---:|---:|---:|
| Transversaux (T) | 0 | 4 | 1 | 2 | 7 |
| Livre I | 0 | 1 | 7 | 3 | 11 |
| Livre II | 1 | 2 | 5 | 4 | 12 |
| Livre III (volets A à E) | 0 | 9 | 20 | 16 | 45 |
| Livre IV | 0 | 2 | 6 | 3 | 11 |
| Livre V | 0 | 5 | 5 | 4 | 14 |
| **Total** | **1** | **23** | **44** | **32** | **100** |

Les constats transversaux T-1 à T-4 agrègent des instances comptées aussi dans leur Livre ; le total n'est pas une somme d'écarts distincts mais un décompte de constats rédigés.

### 9.2 Ce qui ressort

1. **Un seul bloquant** (II.1) : trois thèses de second mouvement re-frappées non verbatim au Livre II, dont une clause de périmètre retranchée au ch. 21 — la classe exacte que R-IV-83/R-IV-87 ont nommée au Livre III, présente dans le Livre qui a précédé leur découverte.
2. **Les corps des pièces sont meilleurs que leur périphérie.** Sur les cinq Livres, les régimes de preuve du corps (degrés d'absence, attributions, bornages, tris prospectifs, fermetures de périmètre) se vérifient presque sans défaut ; les défauts neufs se concentrent dans l'appareil — en-têtes, notes de statut, README, rendus — c'est-à-dire précisément dans ce que les quinze contrôles ne lisent pas.
3. **Quatre classes transversales dominent** : les attestations de balayage invérifiables ou fausses (T-1) ; les discordances de second ordre créées par les passes d'arbitrage (T-2, dont le seul bloquant est une instance) ; les sièges à marqueur non versés sans dette (T-3) ; l'anonymisation de fait, jamais décidée (T-4). Chacune est une variante d'une règle que le dépôt a déjà écrite — la nouveauté n'est pas la classe, c'est qu'aucun instrument ne la voit dans sa propre zone morte.
4. **Le connu tient** (T-7) : tout ce que le dossier consigne a été re-vérifié exact sur pièce. La discipline de déclaration du dépôt fonctionne ; c'est sa périphérie non déclarée qui dérive.
5. **Au Livre III, le plan retarde sur les pièces.** Les deux constats majeurs de la consolidation (III.E.1, III.E.2) et les en-têtes de tables en numérotation gelée (T-6) sont des défauts du TOC, non des chapitres : le texte rédigé y est en meilleur état que la spécification qui le régit — l'inverse du rapport que la gouvernance suppose.

### 9.3 Remontées proposées (sans allocation d'identifiants — PRD §13)

À l'auteur, dans l'ordre de gravité suggéré :

1. **Re-citer ou statuer** : décider si les blocs de thèse des pièces réalignées (ch. 7, 11, 25, 27 et les dix du Livre IV) doivent être re-cités depuis le plan courant, et à quelle passe — puis re-frapper les trois citations fautives du Livre II (II.1) par **copie**, jamais par re-frappe.
2. **Étendre la règle du diff aux passes d'arbitrage** : « une passe de structure se relit ligne à ligne » vaut démontrablement pour les passes d'arbitrage qui touchent des pièces (T-2, V.2, V.6, V.7, II.2, II.4).
3. **Solder la table des sièges** : verser ou déclarer en dette les cinq marqueurs orphelins (T-3), statuer sur le § 34.2.2, harmoniser les noms divergents avant versement (« anti-hype »/« anti-emballement », « four-eyes »/« quatre-yeux » — III.C.6, III.E.5), compléter la liste des pièces non renvoyantes du tri prospectif (ch. 30, 31), et régénérer le `.html` du ch. 48 depuis le `.md` courant (V.2).
4. **Trancher l'anonymisation** (T-4) : soit une règle écrite (au skill et au TOC) avec son domaine et ses exceptions, soit un retour aux dénominations du plan — l'entre-deux actuel coûte l'attribution sans acheter la pérennité.
5. **Statuer sur les attestations de balayage** (T-1) : soit une règle de comptage écrite (occurrence littérale, marqueur formel) qui rende les cardinaux re-mesurables — et idéalement un contrôle qui les re-mesure —, soit le retrait des cardinaux des en-têtes au profit du seul domaine balayé.
6. **Réaligner les cardinaux de gouvernance** (T-5) : décompte des décisions aux deux `CLAUDE.md` (huit sur neuf depuis PRD v0.12), sièges au README du Livre V, affirmation des clôtures au README du Livre IV (IV.2), et corriger la ventilation du tableau 50.1 (V.3) ainsi que l'erreur calendaire du ch. 28 (III.A.3).
7. **Réaligner le plan là où il retarde sur les pièces** : déplier le § 34.2 sur les six sous-sections de sa source (III.E.1), porter l'issue de R-IV-88 à l'entrée du ch. 27 (III.E.2), et statuer sur le renvoi de la lacune §10.11 (III.E.3).
8. **Corrections ponctuelles de renvois** : I.1 (ch. 21 → ch. 49 ou « Vol. II ch. 21 » nommé), I.2 (« ch. 8 § » sans numéro), III.D.3 (renvois promis du § 34.2.2), III.C.1 et III.E.4 (en-tête de socle du ch. 30, dans les deux sens), III.D.2 (F-45).

Chaque remontée suit le régime du dossier : elle se porte là où elle fera foi (PRD pour une décision, TOC pour un réalignement, appareil pour l'outillage, pièce pour une correction de corps), jamais close sur place, et l'arbitrage appartient à l'auteur.
