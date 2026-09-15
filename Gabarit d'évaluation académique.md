# Gabarit d'évaluation académique universitaire — dépôt « Agentique »

*Version 1.0, 15 septembre 2026. Ce gabarit fixe l'objet, les critères, l'échelle, le régime de
preuve et le plan de toute évaluation académique du dépôt. Il se lit avant l'évaluation qui
l'applique, [`Évaluation académique.md`](<%C3%89valuation%20acad%C3%A9mique.md>), et il ne juge
rien lui-même.*

## 1. L'objet évalué et le niveau de référence

L'objet n'est ni un mémoire ni un article. C'est un **dossier de recherche à livrables multiples** :
huit documents que le dépôt déclare livrables, deux documents publiés hors livrables, un simulateur
exécutable, et l'appareil — chaînes de fabrication, contrôles, registres de décisions, `README` —
qui les tient ensemble. Aucune grille institutionnelle n'est écrite pour un tel objet. Le gabarit
en compose une à partir de trois instruments établis, et dit ce que chacun laisse hors de portée.

| Instrument | Ce qu'il apporte | Ce qu'il ne couvre pas |
|---|---|---|
| Grille de jury de mémoire ou de thèse, cycles supérieurs en science et génie informatiques | problématique, état de l'art, méthode, résultats, contribution, forme, éthique | un objet fait de dix documents et d'un logiciel |
| Évaluation par les pairs d'un article soumis à une revue ou à une conférence arbitrée | originalité, rigueur, clarté, réfutabilité, statut des sources | le code, l'appareil, la cohérence entre documents |
| Évaluation d'artefact logiciel, badges de l'ACM — *Available*, *Functional*, *Reusable*, *Results Reproduced* | disponibilité, fonctionnement, réutilisabilité, reproduction des chiffres publiés | le texte |

**Niveau de référence : le doctorat.** L'auteur signe M.Sc. IT, mais le dossier revendique une
portée de recherche — contributions nommées, conditions de réfutation, résultats négatifs — et la
barre se fixe sur ce qu'un dossier revendique, non sur le grade de son auteur. Les descripteurs du
§4 sont donc ceux qu'un jury de doctorat applique à un dossier de recherche en informatique.

**Ce que le gabarit tient pour livrable.** Le compte de « huit » est celui du dépôt, et le dépôt
le dit lui-même *constat et non décision*. Le gabarit ne le tranche pas : l'évaluation couvre
**tous** les documents publiés, livrables ou non, et chaque fiche dit le statut que le document se
donne et celui que l'évaluation lui donne.

## 2. Deux niveaux d'évaluation

### 2.1 Une fiche par pièce

Une fiche pour chacun des huit livrables, une pour chaque document hors livrables, une pour le
simulateur. Chaque fiche porte les neuf champs suivants, dans cet ordre.

| Champ | Contenu exigé |
|---|---|
| **Identité** | titre, dossier, pages et mots **mesurés par l'évaluateur**, date de gel, cardinal des références |
| **Thèse** | en une phrase, telle que la pièce la porte — citée, non reformulée |
| **Méthode déclarée** | régime de preuve, dispositif de vérification, et ce que la pièce dit ne pas faire |
| **Lecture faite** | ce qui a été lu intégralement, ce qui a été échantillonné, sections nommées |
| **Rejeu** | contrôles exécutés sur la pièce et leurs verdicts, sortie à l'appui |
| **Forces** | au plus cinq, chacune ancrée à un fichier et à une section |
| **Faiblesses** | toutes celles relevées, mineures comprises, chacune ancrée |
| **Niveau** | l'un des cinq niveaux du §4 |
| **Publiabilité** | le statut que la pièce se donne ; le statut que l'évaluation lui donne, et pourquoi ils divergent s'ils divergent |

### 2.2 Neuf critères transversaux

Les critères jugent le dossier comme un tout. Le poids dit ce que le jury pèse le plus : la
méthode, la contribution et les artefacts, parce que c'est là qu'un dossier de recherche se
distingue d'une somme documentaire.

| # | Critère | Poids | Ce que le jury demande |
|---|---|---|---|
| C1 | Problématique, positionnement et unité du programme | 10 | La question est-elle une, énoncée, tenue d'un bout à l'autre ? Le positionnement est-il un créneau que la littérature ne couvre pas ? Chaque pièce l'instruit-elle ? |
| C2 | État de l'art et maîtrise de la littérature | 10 | La littérature est-elle couverte, datée, lue à la source primaire ? Le dossier sait-il ce qui est arbitré et ce qui ne l'est pas ? Les classiques du domaine y sont-ils ? |
| C3 | Méthodologie et régime de preuve | 15 | Le dossier dit-il comment il sait ce qu'il dit ? Les niveaux de preuve sont-ils explicites, appliqués, et leur hiérarchie est-elle défendable ? Les énoncés sont-ils réfutables ? Quelqu'un d'extérieur est-il entré dans la boucle ? |
| C4 | Qualité, vérification et traçabilité des sources | 10 | Les références existent-elles, disent-elles ce qu'on leur fait dire, sont-elles closes dans les deux sens ? Les sources vivantes sont-elles datées ? L'auto-citation est-elle déclarée ? |
| C5 | Résultats, contribution et originalité | 15 | Qu'est-ce que le dossier établit que l'on ne savait pas ? Les contributions sont-elles nommées, bornées, défendables devant un contradicteur ? Y a-t-il des données ou seulement des textes ? |
| C6 | Artefacts, reproductibilité et appareil de vérification | 15 | Ce qui est déclaré se refait-il sur une autre machine ? Les contrôles tiennent-ils sur un arbre propre ? Les harnais attrapent-ils ce qu'ils prétendent ? Qu'est-ce qui dépend du poste de l'auteur ? |
| C7 | Structure, cohérence et économie du corpus | 10 | Un lecteur trouve-t-il ce qu'il cherche ? La même matière est-elle écrite une fois ? Les numérotations et les comptes concordent-ils d'un document à l'autre ? |
| C8 | Rédaction et communication scientifique | 10 | Le corps se lit-il ? L'appareil se lit-il ? Un décideur, un chercheur, un praticien y trouvent-ils chacun leur entrée ? Le dossier est-il citable ? |
| C9 | Intégrité intellectuelle, attribution et gouvernance | 5 | Qui a écrit quoi, et le dossier le dit-il ? Les droits des tiers sont-ils respectés ? Les décisions sont-elles datées, motivées, réversibles ? Les traces d'audit survivent-elles ? |
| | **Total** | **100** | |

## 3. Le régime de preuve de l'évaluation elle-même

Une évaluation qui reprendrait les chiffres du dépôt sans les remesurer ne vaudrait pas mieux que
le dépôt. Chaque énoncé factuel de l'évaluation porte donc l'un de cinq marqueurs.

| Marqueur | Sens | Obligation |
|---|---|---|
| **[L]** | lu intégralement par l'évaluateur | nommer le fichier |
| **[E]** | échantillonné | nommer les sections lues ; un échantillon non nommé vaut [D] |
| **[R]** | rejoué — commande exécutée par l'évaluateur, sortie rapportée | donner la commande et le verdict ; une sortie 1 se rapporte avec son message |
| **[S]** | confronté à la source externe — notice, page officielle, texte normatif consulté à la date dite | donner l'adresse et la date de consultation |
| **[D]** | déclaré par le dépôt, non vérifié par l'évaluateur | le dire ; un chiffre [D] ne fonde aucune appréciation seul |

Trois règles s'ajoutent. Un chiffre remesuré **remplace** le chiffre déclaré, et l'écart s'écrit.
Un constat se distingue d'une appréciation par le mot : *constat* ce que la mesure ou la lecture
rend, *appréciation* ce que l'évaluateur en pense. Une évaluation antérieure, si le dépôt ou son
historique en porte une, est lue et nommée, et **aucune de ses conclusions n'est reprise sans avoir
été refaite**.

## 4. L'échelle

Cinq niveaux, appliqués à chaque critère transversal et à chaque fiche. Le score d'un critère est
son poids multiplié par la part retenue ; l'évaluateur écrit la part, et non le seul niveau.

| Niveau | Part du poids | Descripteur au niveau de référence |
|---|---|---|
| **Excellent** | 90 à 100 % | Rien d'important à reprendre. Un relecteur exigeant accepterait tel quel. |
| **Très bien** | 75 à 89 % | Solide. Des reprises sont identifiées ; aucune ne touche le fond. |
| **Satisfaisant** | 60 à 74 % | Tient. Au moins une faiblesse touche le fond ou l'usage, et elle se corrige. |
| **Passable** | 40 à 59 % | Tient en partie. Une faiblesse de fond conditionne l'usage de la pièce ou du critère. |
| **Insuffisant** | 0 à 39 % | Ne tient pas au niveau de référence. |

Le total sur 100 est un agrégat qui sert à comparer. **Il ne décide pas du verdict.**

## 5. Le verdict de jury

Quatre catégories, celles d'un jury de thèse.

1. **Accepté tel quel.**
2. **Accepté sous corrections mineures**, sans nouvelle évaluation.
3. **Corrections majeures requises**, avec nouvelle évaluation.
4. **Refusé.**

Le verdict se décide d'abord par les **conditions bloquantes**, ensuite par le total. Une seule
condition bloquante suffit à plafonner le verdict à la catégorie 3, quel que soit le total.

| Condition bloquante | Pourquoi elle bloque |
|---|---|
| **B1** — aucun relecteur **humain** identifié n'a lu un énoncé central d'aucune pièce | un dossier de recherche se juge à ce qu'il a survécu ; une relecture instrumentée n'est pas une relecture |
| **B2** — une pièce comptée parmi les livrables se déclare elle-même non publiable | le compte des livrables et l'état des pièces se contredisent |
| **B3** — un contrôle du dépôt sort 1 sur un arbre propre et le dépôt ne le documente pas | l'appareil affirme une garantie qu'il ne tient pas |
| **B4** — l'attribution des contributions — auteur, agents, relecteurs — n'est pas déclarée par pièce | l'intégrité de l'attribution est une exigence de jury, pas une politesse |

Hors condition bloquante : un total sous 60 conduit au refus ; de 60 à 84, corrections mineures ou
majeures selon la nature des reprises ; 85 et plus, accepté tel quel possible.

## 6. L'artefact logiciel — badges

Le simulateur et les chaînes de fabrication reçoivent chacun les badges qu'ils méritent, sur preuve.

| Badge | Condition | Preuve exigée de l'évaluateur |
|---|---|---|
| **Disponible** | dépôt public, licence posée, identifiant stable | adresse, `LICENSE`, étiquette ou DOI |
| **Fonctionnel** | construit et testé par l'évaluateur | commandes et sorties |
| **Réutilisable** | prérequis portables, aucun chemin lié au poste de l'auteur, interface documentée | lecture de la documentation, essai hors poste d'auteur ou motif de l'impossibilité |
| **Résultats reproduits** | les chiffres publiés — tests, tailles, pages, écarts — retrouvés à la mesure | table écart déclaré / mesuré |

## 7. Les recommandations — forme imposée

Trois listes, et rien hors d'elles. **Corrections requises** : chacune lève une condition bloquante
ou un défaut de fond, et dit laquelle. **Bonifications** : classées par rendement sur le verdict,
chacune avec son effet attendu. **Projets futurs** : chacun part d'un reste que le dossier nomme
lui-même, jamais d'un souhait de l'évaluateur. Une recommandation sans effet énoncé ne s'écrit pas.

## 8. La déclaration de l'évaluateur

Elle ferme l'évaluation et porte : qui ou quoi évalue — personne ou modèle, et sa version ; à la
demande de qui ; sur quelle machine et quel commit ; en combien de temps ; les conflits d'intérêts ;
**ce que l'évaluation n'est pas** — jury institutionnel, arbitrage de revue ; et ses limites,
échantillonnage compris. Une évaluation produite par un modèle de langage le dit en tête et en fin,
parce que le dossier qu'elle juge fait précisément de cette distinction un critère.

## 9. Règles de rédaction

- Chaque constat porte son ancre : fichier et section, ou commande.
- Les chemins cités sont ceux du commit évalué et ne se réécrivent pas.
- Constat, appréciation et recommandation se séparent par le mot.
- Les constats mineurs se rapportent tous ; rien ne se tait parce que c'est peu grave.
- La longueur est celle que l'exhaustivité exige ; aucun résumé ne répète une section.
- Le français est celui du dossier ; les termes techniques, commandes et identifiants restent en
  anglais.

## 10. Le plan imposé de l'évaluation

1. Fiche d'identité — objet, commit, date, évaluateur.
2. Verdict en tête — total, catégorie, cinq phrases.
3. Ce qui a été lu, rejoué, confronté — trois tables.
4. L'objet, décrit par l'évaluateur.
5. Fiches par pièce (§2.1).
6. Évaluation transversale, C1 à C9 (§2.2).
7. Tableau de notation.
8. Constats neufs sur l'appareil — ce que l'évaluation a trouvé que le dépôt n'écrit pas.
9. Critiques de fond.
10. Verdict et conditions (§5), badges (§6).
11. Corrections requises, bonifications, projets futurs (§7).
12. Déclaration de l'évaluateur (§8).
- Annexe A — commandes exécutées et sorties abrégées.
- Annexe B — références confrontées à leur source.
