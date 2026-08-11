# Journal de boucle bâtisseur/critique

Journal *append-only*. Un bloc par tour : morceau, verdict à l'aveugle, écart retenu, coût.
C'est le frein de la boucle — il existe pour qu'un arrêt se décide sur pièce et non par lassitude.

⚠ **Ce fichier a été supprimé au commit `79ef5d4` du 10 août 2026**, avec ses 482 lignes couvrant la
veille d'août et la revue de littérature. *Elles ne se relisent plus qu'à l'historique git.* Le
présent journal rouvre au 10 août 2026 et ne reprend rien de ce qui précède.

---

## Course — audit intégral du traité (10 août 2026)

**Objectif.** Auditer [`Traité.md`](Trait%C3%A9.md) en totalité, corriger tous les écarts trouvés,
**maintenir le PDF à exactement 100 pages**, puis committer et pousser sur `main`.

**Barre.** L'utilisateur n'a pas retenu l'un des trois artefacts proposés ; il a nommé une qualité —
*« qualité du français syntaxique et grammatical, ton technique et professionnel, plus la validation
de toutes les références afin d'être fiable, viable et existantes ; assurer la crédibilité du contenu
sous un style de rédaction professionnelle »*. Une qualité n'est pas une barre : elle n'est ni
récupérable ni comparable. Elle a donc été gagée sur la pièce du dépôt qui l'incarne —
**`Veille Technologique.md`**, 100 p., 303 références, même auteur, français technique, chaque énoncé
factuel adossé à une source primaire consultée. *Deux axes de jugement, et deux seulement* :

1. **Langue** — français technique professionnel de monographie savante.
2. **Sources** — chaque notice existe, est exacte champ par champ, et reste atteignable.

**Budget.** 16 paires bâtisseur/critique, plus une passe de lissage. Fixé avant le lancement.
*C'est le budget qui ferme la boucle, pas un nombre de tours.*

**Découpage — 8 morceaux jugeables indépendamment.** Le critère est la jugeabilité, non la taille :
un morceau de langue se juge sur un extrait, un morceau de bibliographie se juge notice par notice.

| Morceau | Portée | Axe |
|---|---|---|
| L1 | Introduction + ch. 1 (lignes 28-241) | langue |
| L2 | ch. 2 et 3 (lignes 242-653) | langue |
| L3 | ch. 4 et 5 (lignes 654-992) | langue |
| L4 | ch. 6, 7 et Conclusion (lignes 993-1300) | langue |
| R1 | notices 1 à 30 | sources |
| R2 | notices 31 à 60 | sources |
| R3 | notices 61 à 90 | sources |
| R4 | notices 91 à 118 | sources |

**Protocole d'écriture.** ⚠ *Les bâtisseurs ne touchent pas au fichier.* Huit agents écrivant en
parallèle dans un même `.md` se détruisent mutuellement ; chacun rend donc un jeu de correctifs
chirurgicaux — `old` exact et unique, `new`, motif, gravité, delta de longueur — appliqués et
vérifiés centralement. **Contrainte portée à chaque bâtisseur** : tout correctif de langue doit être
de longueur égale ou inférieure à ce qu'il remplace, la cible de 100 pages n'ayant aucune porte qui
la défende.

---

## Tour 1 — 8 morceaux, 8 bâtisseurs, 8 critiques

**Bâtisseurs.** 97 correctifs rendus, **97 appliqués, 0 rejeté** par le contrôle central (ancre unique,
delta déclaré conforme, remplacement effectif). Répartition : 47 fautes de langue, 25 de registre,
10 incohérences, 6 typographiques, 4 champs bibliographiques faux, 4 statuts éditoriaux faux, 1 URL
non canonique. **Delta cumulé : −214 caractères.** Rendu recomposé : **100 pages**, bijection des
118 renvois intacte.

⚠ **L1 est mort d'une erreur d'API après avoir livré.** Ses deux fichiers étaient sur disque et son
JSON valide : l'artefact existait, il a été inspecté et retenu. *Un agent qui meurt après sa livraison
n'invalide pas sa livraison* — la relancer aurait coûté un tour pour le même résultat.

**Verdicts à l'aveugle.** Ordre A/B alterné d'un morceau à l'autre, extraits tronqués à longueur
comparable pour qu'aucun juge ne devine à la taille. **Le traité gagne 7 comparaisons sur 8.**

| Morceau | A / B | Verdict | Écart retenu contre le traité |
|---|---|---|---|
| L1 | traité / veille | **traité** | Les trois règles de Reynolds citées en anglais sans glose (l. 51) |
| L2 | veille / traité | *veille* | Tiret d'apposition non refermé (l. 262) ; « se dérive » ; « l'invariante R1 » |
| L3 | traité / veille | **traité** | Gloses anglaises vides — « agents (*agents*) », « partition (*partition*) » — et *partition* en deux sens |
| L4 | veille / traité | **traité** | *Faute*, *panne* et *défaillance* employés l'un pour l'autre |
| R1 | traité / veille | **traité** | Réf. [5] : code Kafka cité sur la branche `trunk` |
| R2 | veille / traité | **traité** | Réf. 34 : « à partir de la p. 463 », sans volume, numéro ni DOI |
| R3 | traité / veille | **traité** | Chandra & Toueg : « à partir de la p. 225 », même défaut |
| R4 | veille / traité | **traité** | Réf. 102-103 : `trunk` comme autorité normative |

⚠ **Deux écarts ont été nommés par deux juges chacun, sur des lots distincts** — la **cible mouvante**
(R1 et R4) et la **pagination ouverte** (R2 et R3). *C'est la seule convergence de la vague, et elle
désavoue un arbitrage du tour 1* : le bâtisseur R2 avait vu la pagination ouverte et renoncé à la
fermer **pour ne pas rallonger le texte**. Deux juges à l'aveugle en font le premier défaut de
l'appareil. **La contrainte de longueur est levée pour ces notices au tour 2** : un champ manquant
qu'on ajoute est une correction de fond, et la pagination se recale ensuite par le gabarit.

⚠ **Trois agents indépendants ont buté sur « une invariante »** — deux bâtisseurs et un juge à
l'aveugle, ce dernier l'ayant compté parmi les motifs de la seule défaite. Le mot est masculin en
informatique ; **la forme féminine est pourtant majoritaire dans l'ouvrage, 12 occurrences contre 2**.
*Une forme majoritaire est une convention, et une convention se remonte à l'auteur au lieu de se
corriger depuis un morceau.* Elle est donc laissée en l'état et portée à l'arbitrage.

⚠ **Un signalement de bâtisseur s'est révélé faux à la vérification, et il est consigné pour cela.**
L3 annonçait un défaut de rendu : trois légendes de tableau placées avant leur tableau au ch. 5, contre
dix-sept placées après. *Le placement est bien incohérent, mais Pandoc accepte les deux formes* — les
vingt tableaux sont numérotés 1 à 20 au PDF, aucune légende n'est perdue. **Constat rétrogradé de
défaut de rendu à incohérence de source.** *Un rapport d'agent se vérifie avant de se croire.*

**Coût du tour.** 8 bâtisseurs ≈ 1 055 k jetons ; 8 juges ≈ 405 k. **Budget consommé : 8 paires
sur 16.**

---

## Tour 2 — cinq écarts retenus, cinq bâtisseurs

Chaque bâtisseur reçoit **l'écart de son morceau, cité mot pour mot**, et rien d'autre : ni le verdict,
ni les autres écarts, ni ce que le tour 1 avait tenté. Deux d'entre eux ont contredit leur juge sur
pièce, et c'est le signe que la boucle fonctionne.

| Morceau | Correctifs | Delta | Ce qui a été fait |
|---|---|---|---|
| L1 | 1 | −6 | Les trois règles de Reynolds glosées en français, l'anglais passé en position d'attestation sous [10] |
| L2 | 5 | −3 | Les trois griefs levés ; une quatrième rupture du même type trouvée seule (l. 357) |
| L3 | 6 | −81 | Six gloses vides retirées ; *partition* désambiguïsé **sans rallonger**, par le qualificatif français déjà présent |
| L4 | 3 | 0 | `modèle de faute` → `modèle de panne`, après comptage sur tout le fichier |
| R | 29 | **+1063** | 12 cibles mouvantes ancrées, 3 paginations fermées, 10 autres complétées |

**44 correctifs, 0 rejet, delta +973 caractères — et le rendu tient à 100 pages.**

⚠ **Deux bâtisseurs ont renvoyé leur juge dans ses cordes, sur pièce.** L4 a compté les six formes
concurrentes sur **tout** le fichier avant de corriger : `modèle de panne` 18 contre `modèle de faute`
11, `mode de défaillance` 20, `détecteur de défaillance` 7. La convention de l'ouvrage est donc
**panne** pour la classe tolérée et **défaillance** pour la manifestation — les deux séries étaient
déjà cohérentes, seul `modèle de faute` déviait. *La troisième citation du juge était conforme ; c'est
l'ouverture du chapitre qui déviait, pas elle.* Et la distinction délibérée `faute` = cause (fautes
byzantines, injection de fautes, corrélation des fautes) a été **préservée** au lieu d'être écrasée.
*Un juge nomme un symptôme ; il n'établit pas la convention.*

⚠ **Le lot bibliographique a coûté +1063 caractères, et c'était le bon prix.** Les 12 cibles mouvantes
ne sont pas ancrées sur des étiquettes plausibles mais sur des étiquettes **ouvertes et relues** : la
réf. [5] sur un SHA de commit, le tag 4.1.0 renvoyant 404 pour ce fichier ; les réfs 102-103 sur
l'étiquette 4.1.0, où les valeurs `30000L`, 45000, 3000 et 300000 alléguées au ch. 6 ont été
**retrouvées dans le code**. *Ancrer une référence sur une version qu'on n'a pas ouverte revient à
déplacer le défaut, pas à le corriger.*

⚠ **Une normalisation est restée à moitié faite, et cela force une décision.** Le bâtisseur L2 a
corrigé `l'invariante R1` et `aucune invariante de sûreté` dans ses lignes, en signalant que **neuf
occurrences subsistent hors de son morceau**. *Un texte à moitié normalisé est pire que l'un ou
l'autre état* : la question cesse d'être « faut-il corriger la convention de l'auteur » pour devenir
« faut-il finir ou revenir en arrière ». **Décision : finir**, à la passe de lissage — le mot est
masculin en informatique, et un juge à l'aveugle l'a compté parmi les motifs de la seule défaite.

**Coût du tour.** 5 bâtisseurs ≈ 458 k jetons. **Budget consommé : 13 paires sur 16.**

---

## Passe de lissage — un agent neuf sur l'ensemble

Huit morceaux améliorés séparément ne font pas un tout : des corrections s'arrêtent à une frontière de
morceau, et le texte cesse d'être d'accord avec lui-même. **27 coutures refermées, delta −113
caractères**, plus **3 légendes déplacées** — un déplacement n'étant pas une substitution, il a été
livré et appliqué à part.

| Couture | Traitement |
|---|---|
| « invariante » au féminin | **8 occurrences** portées au masculin **avec tous leurs accords** — déterminant, adjectif, participe, et le pronom `la` → `le` au §7.3 |
| `se dérive` | 2 occurrences restantes, delta 0 |
| Gloses anglaises vides | 6 retirées — `consensus`, `idempotency`, `agent`, `emergence`, `stigmergy`, `traceability` |
| Conventions de renvoi | 7 renvois `§ N.N` alignés sur `§N.N`, majoritaire à 15 contre 7 |
| Trouvés en lisant | `99,9e` → `99,9ᵉ` ; `[5] [33]` → `[5][33]` |
| Légendes de tableau | Les 3 du ch. 5 déplacées après leur tableau, comme les 17 autres |

☑ **La normalisation d'« invariante » est complète et exacte.** Deux occurrences féminines subsistent,
et ce sont les bonnes : *« la moyenne initiale n'est plus invariante »* et *« la somme des états
cessant d'être invariante »* — l'adjectif y accorde avec un sujet féminin. *Le solécisme portait sur
le nom, jamais sur l'adjectif.*

⚠ **L'agent a refusé trois normalisations, et il a eu raison chaque fois** : `réplique` 40 contre
`réplica` 4, `auto-guérison` 3 contre `auto-healing` 1, `DOI :` 47 contre `DOI 10.` 19 — **la forme
majoritaire est la plus longue dans les trois cas**, et la cible de cent pages n'a pas de marge à
donner. *Un lissage qui casse la contrainte qu'on lui a posée n'est pas un lissage.* Il a également
laissé la Conclusion intacte — elle écrit ses nombres en lettres et n'abrège jamais « chapitre », mais
c'est un registre intérieurement cohérent, pas une couture.

**Coût.** 1 agent ≈ 248 k jetons. **Budget consommé : 14 paires sur 16.**

---

## Clôture de la course

**Sortie de boucle : gains devenus marginaux, budget non épuisé** (14 paires sur 16). Le traité gagnait
déjà 7 comparaisons à l'aveugle sur 8 au tour 1 ; le tour 2 a traité les huit écarts retenus et la
passe de lissage a refermé les coutures. *Relancer une vague de juges pour confirmer une victoire déjà
acquise aurait dépensé le reste du budget sans rien produire de corrigible.*

**Bilan de la course — 168 correctifs appliqués, 0 rejeté**, plus 3 déplacements de légende.

| Vague | Correctifs | Delta |
|---|---|---|
| Tour 1 — 8 bâtisseurs | 97 | −214 |
| Tour 2 — 5 bâtisseurs | 44 | +973 |
| Lissage — 1 agent | 27 | −113 |
| **Total** | **168** | **+646** |

**État vérifié sur pièce au rendu final** : **100 pages**, **0 page blanche**, **20 tableaux numérotés
1 à 20**, **118 renvois cités pour 118 notices déclarées, aucun orphelin dans un sens ni dans l'autre**.

**Les 118 notices ont été confrontées à leur source primaire** : 108 confirmées telles quelles,
10 corrigées, **0 non confirmée**. Ce que la confrontation a trouvé :

- **un titre inventé** — la réf. 93 imprimait *« The Best-of-n Problem in Robot Swarm Decision-Making:
  A Short Review »* pour *« …in Robot Swarms: Formalization, State of the Art, and Novel
  Perspectives »*, auteurs, revue et année exacts par ailleurs. **Un cas sur 118** ;
- **quatre statuts éditoriaux faux, tous dans le même sens** : des pièces déposées sur arXiv annoncées
  comme prépublications alors qu'elles sont **parues arbitrées** — CAV 2013, CAV 2017,
  *IEEE Software* 2016, *CACM* 2020. *L'erreur sous-évaluait le corpus au lieu de le gonfler ; elle
  était fausse dans les deux sens* ;
- **une version fausse** (réf. 105, OpenTelemetry), **un ouvrage hôte manquant** (réf. 98), et
  **13 paginations ouvertes ou absentes** fermées sur Crossref, DataCite ou dblp.

⚠ **Ce que la course n'a pas fait.** Elle **ne touche à aucun autre livrable du dépôt**, **ne rejuge
pas la clôture D-13**, **n'ajoute aucune porte de pagination** — la cible de cent pages reste
constatée et non vérifiée au rendu —, et **ne lève aucune des réserves de fond de l'ouvrage** : la
frontière que le traité annonce reste argumentée et non mesurée, et sa conclusion le dit elle-même.
