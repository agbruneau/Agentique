# Revue et Veille — les deux livrables qui mesurent le champ

Deux documents publiés, et l'appareil qui les contrôle. Ils ne font pas partie du triptyque et ne
s'y substituent pas : **ils mesurent l'état du champ que les volumes exposent**, chacun sur un
versant. La [veille technologique](Veille%20Technologique.md) dit **ce que le monde déployé fait**,
sur spécifications, dépôts et textes réglementaires ; la [revue de littérature](Revue%20de%20litt%C3%A9rature.md)
dit **ce que la littérature académique sait, et à quel régime de preuve**. *Les deux ne coïncident
pas, et c'est l'intérêt.*

> **Où ce dossier vit.** Il est né le **15 août 2026**, **quatrième dossier numéroté** du dépôt
> [Agentique](../README.md). ⚠ **Les quatre fichiers de livrable venaient de la racine**, où ils
> vivaient depuis leurs dépôts respectifs — *inchangés au bit près, `git` enregistrant quatre
> renommages purs*. Le dossier [`Python/`](Python/) les a suivis. ☑ **Depuis, la racine du dépôt ne
> porte plus aucun livrable** : les sept sont rangés sous quatre dossiers numérotés.
>
> ⚠ **Le dépôt est clos depuis le 8 août 2026** — décision d'auteur **D-13**
> ([`2 - Compendium/PRD/PRD.md`](../2%20-%20Compendium/PRD/PRD.md) v0.17 §16). *Ces deux livrables
> sont postérieurs à la clôture, et chacun l'a rouverte pour lui seul.* La clôture reste en vigueur
> pour les quatre volumes ; **rien de ce dossier ne la lève**.

---

## Les deux livrables

| | **Veille technologique** | **Revue de littérature** |
|---|---|---|
| **Fichiers** | [`Veille Technologique.md`](Veille%20Technologique.md) → [`.pdf`](Veille%20Technologique.pdf) | [`Revue de littérature.md`](Revue%20de%20litt%C3%A9rature.md) → [`.pdf`](Revue%20de%20litt%C3%A9rature.pdf) |
| **Titre** | *Interopérabilité et Orchestration Agentiques en Entreprise* — ⚠ **homonyme exact du Vol. IV** depuis le 9 août 2026 | *Interopérabilité et Orchestration Agentiques : revue de la littérature académique* — ⚠ **même radical**, aligné le même jour |
| **Rendu** | **100 p.**, 14 sections numérotées, **303 références**, 18 tableaux, 25 questions ouvertes *(40 707 mots au `.md`)* | **40 p. fermes**, 19 sections, **176 références**, 8 tableaux, dix fronts *(17 829 mots au `.md`)* |
| **Gel de l'information** | **8 août 2026** — les sections antérieures gardent leur date d'état | **9 août 2026** |
| **Thèse** | « L'agent d'entreprise fiable de 2026 est un agent *enveloppé* » | « Les trois quarts du champ n'ont franchi aucun comité » |
| **Méthode** | Revue structurée, **vérification adverse à trois votants** chargés de *réfuter* ; source primaire consultée pour chaque énoncé factuel | Notices ouvertes une à une, **métadonnées reprises à l'API arXiv** — ce qui a corrigé plusieurs statuts que la passe de recherche donnait pour arbitrés |
| **État** | Publiée ; **format ferme depuis le 8 août 2026**, ramenée de 162 à 100 pages **sans changement de gabarit** — toute la réduction vient de la réécriture | Publiée ; déposée le 9 août 2026 et **révisée le même jour** (dixième front) |

⚠ **Trois livrables du dépôt sur sept partagent ce début d'intitulé** — ces deux-ci et le Vol. IV.
**Un renvoi qui les cite par leur seul titre ne désigne rien** : il faut nommer le genre — « la veille
technologique », « la revue de littérature », « le Vol. IV ». ☑ *C'est aussi par le genre que les
fichiers se nomment, et non par le titre* : la convention du dépôt tient ici sans exception.

---

## Ce que chacun rend à l'autre, et au corpus

**La veille est le point d'articulation du corpus.** Sa section 13 rend compte des quatre volumes,
mais à **deux régimes strictement distincts** : les Vol. I et II sont rédigés et **fournissent des
faits** ; les Vol. III et IV y sont des **cadrages** et n'en fournissent aucun — ils prêtent des
instruments. *Traiter un plan comme un corpus serait la faute que ces deux cadrages prennent
eux-mêmes pour objet.* ⚠ **Ce tableau de régimes est celui du gel, et le dépôt l'a dépassé sur trois
points** — signalés au [README du dépôt](../README.md), **non corrigés ici** : *une revue publiée
décrit l'état de ses sources à sa date, et la rattraper après coup effacerait la seule information
qu'elle porte.*

⚠⚠ **L'édition du 8 août 2026 a renvoyé au corpus deux corrections de fond, et les volumes ne les
recevront pas.** *(a)* L'**article 12.1 de la Loi 25** n'exige aucune « intervention humaine
déterminante » : il se déclenche quand la décision est fondée **exclusivement** sur un traitement
automatisé, et borne l'absence totale d'humain sans prescrire de degré d'autonomie. *(b)* L'**avis
ACVM 11-348** ne contient ni *agent*, ni *agentique*, ni *autonomie* — l'opposition que le corpus
construisait entre accroche textuelle et accroche par inférence **tombe, les deux accrochant par
inférence**. *Le lecteur qui cite le Vol. II sur ces deux points cite un énoncé que la veille a
réfuté.*

**La revue rend trois verdicts à la veille**, dont deux la modifient : le déficit de délégation
au-delà de deux sauts est un déficit **d'adoption et non d'invention** ; la dissymétrie entre agents
et formalismes de processus est **industrielle, non scientifique** ; et l'absence de vocabulaire de
trace décrivant une chaîne de mandat est **confirmée par une seconde voie, plus sévère**.

⚠ **L'auto-citation est assumée et divulguée des deux côtés** : la veille cite les volumes du même
auteur, la revue met à l'épreuve une veille du même auteur. Les limites de l'exercice — circularité
possible, implémentation unique, chiffres institutionnels auto-déclarés — sont exposées en section 10
de la veille.

---

## Construire les PDF

Deux chaînes, **invocation Pandoc directe et gabarit Typst par défaut**, tout le réglage vivant dans
l'en-tête YAML de chaque source. **Depuis ce dossier :**

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

```bash
pandoc "Revue de littérature.md" --pdf-engine=typst --toc -o "Revue de littérature.pdf"
```

☑ **Ces deux commandes n'ont pas changé au déplacement du 15 août 2026, et c'est un fait et non une
chance** : *ni l'une ni l'autre source ne porte une seule image*, donc aucun chemin relatif à
résoudre. ⚠ **Le contraste avec le traité instruit** : lui cite dix-neuf figures en chemin relatif,
et son déplacement du 14 août a cloué sa chaîne de rendu à la racine du dépôt. *Un livrable sans
dépendance de fichier se déplace sans conséquence ; un livrable qui en a une ne se déplace jamais
seul.*

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, police New Computer Modern. Marges 2,8 × 2,6 cm, corps
de 11 pt, résumé sur la page de titre.

---

## L'appareil de contrôle — [`Python/`](Python/)

Trois contrôles, **sans dépendance externe** : la bibliothèque standard seule.

| Script | Ce qu'il oppose au document | Dernière exécution |
|---|---|---|
| [`check-veille.py`](Python/check-veille.py) | **quatre contrôles** — renvois en clair contre numérotation Pandoc, cardinaux écrits en toutes lettres, doublons bibliographiques, appariement cité ↔ défini | **sortie 0** — 94 sections, 18 tableaux, 25 questions ouvertes ; **303 définies, 303 citées** |
| [`check-revue.py`](Python/check-revue.py) | **quatre contrôles** — appariement et contiguïté, légendes de tableau, doublons, **cardinaux du régime de preuve** | **sortie 0** — 176 entrées ; **12 attestées, 28 autodéclarées, 133 sans revue** sur 173 arXiv |
| [`check-resume.py`](Python/check-resume.py) | **le budget de mise en page** : le résumé tient-il sur la page de titre du PDF rendu | **sortie 0** — dernière ligne à **y = 119,4 pt**, dégagement **+45,7 pt** |

```bash
python Python/check-veille.py
python Python/check-revue.py
python Python/check-resume.py        # ou : python Python/check-resume.py <un autre .pdf>
```

☑ **Les trois se lancent de n'importe quel répertoire depuis le 15 août 2026.** ⚠ *Ce n'était pas le
cas, et c'est la panne qui a motivé la correction* : leurs sources étaient nommées en **chemin
relatif au répertoire courant**, si bien que le déplacement des deux livrables hors de la racine les
a fait lever `FileNotFoundError` **avant d'avoir lu une ligne**. *Une trace de pile n'est pas un
verdict : un contrôle qui ne trouve pas sa source ne dit pas que le document est faux, il ne dit plus
rien.* ☑ **Chacun résout désormais son chemin contre l'emplacement du script**, `Path(__file__)`, et
non contre le répertoire courant — la dépendance à `cd` est supprimée, pas déplacée. *Un chemin donné
en argument à `check-resume.py` reste, lui, relatif au répertoire courant : c'est ce que l'appelant a
tapé.*

⚠ **Ce que ces contrôles ne voient pas.** **Aucun ne résout un lien markdown** — c'est le défaut que
le [README du dépôt](../README.md) porte à son tableau des reliquats, et *un déplacement de fichier
ne lève donc aucune erreur*. Aucun ne vérifie non plus la **pagination** : les 100 pages de la veille
et les 40 de la revue sont **constatées à chaque build, jamais vérifiées** — seule la chaîne du
compendium oppose une porte de pagination à son rendu. ⚠ *Un mot ajouté fera tomber une cible en
silence.*

⚠ **`check-resume.py` est calibré sur le gabarit de la veille, et sur lui seul** : sa marge basse est
la **constante** `MARGE_BASSE = 73.7` (les 2,6 cm de l'en-tête), et il mesure *tout* texte posé en
page 1, folio compris. Rejoué sur `../3 - Traité/Traité.pdf`, qui compose à 1,9 cm et numérote dès la
page de titre, il **sort 1 sans qu'une ligne y soit rognée**. *Un contrôle transporté sur un gabarit
pour lequel il n'a pas été calibré ne mesure plus ce qu'il annonce.*

---

## Structure du dossier

```
4 - Revue et Veille/
├── README.md                        ← ce fichier
├── Veille Technologique.md / .pdf     100 p., 303 réf. — édition du 8 août 2026, faits gelés à cette date
├── Revue de littérature.md / .pdf     40 p. fermes, 176 réf. — arrêtée au 9 août 2026
└── Python/                          ← les trois contrôles ; stdlib seule, aucune dépendance
    ├── check-veille.py                renvois, cardinaux, bibliographie, appariement
    ├── check-revue.py                 appariement, tableaux, doublons, régimes de preuve
    └── check-resume.py                budget de mise en page de la page de titre
```

*(Les quatre fichiers de livrable et le dossier `Python/` venaient de la racine du dépôt, le 15 août
2026 — `Python/` y avait lui-même été créé le 10 août, les trois scripts vivant à la racine
auparavant.)*

---

## Réserves

- ⚠ **Aucune pagination n'est vérifiée** — voir plus haut. Les deux cibles sont constatées.
- ⚠ **Aucun contrôle ne résout un lien** — défaut commun à tout l'appareil du dépôt.
- ⚠ **`check-resume.py` n'est calibré que pour le gabarit de la veille.**
- ⚠ **Les deux documents décrivent l'état de leurs sources à leur date de gel**, et cela ne se
  corrige pas après coup. Trois écarts connus entre la veille et l'arbre courant sont consignés au
  [README du dépôt](../README.md) — *signalés là-bas, non corrigés ici*.
- ⚠ **Le dépôt ne porte aucune licence, et c'est une décision** : droit d'auteur par défaut, tous
  droits réservés. Seul le Vol. I porte un `LICENSE` propre, qui ne vaut que pour lui.
