# Conventions et pièges — rédaction d'une pièce du compendium

À lire **avant** d'écrire, pas après. Chaque entrée ci-dessous ferme une erreur qui a déjà été
commise dans ce dépôt, ou qu'une passe de gouvernance a explicitement voulu prévenir.

## Table des matières

- [1. Renvois](#1-renvois)
- [2. Marqueurs et réserves](#2-marqueurs-et-réserves)
- [3. Garde-fous et formulations imposées](#3-garde-fous-et-formulations-imposées)
- [4. Cardinaux et décomptes](#4-cardinaux-et-décomptes)
- [5. Les trois régimes de preuve](#5-les-trois-régimes-de-preuve)
- [6. Numérotations : trois séries qui coexistent](#6-numérotations--trois-séries-qui-coexistent)
- [7. Sources absentes du dépôt](#7-sources-absentes-du-dépôt)
- [8. Pièges datés — ce qui a déjà coûté une passe](#8-pièges-datés--ce-qui-a-déjà-coûté-une-passe)

---

## 1. Renvois

**Deux formes, et l'espace les départage.** C'est la convention la plus facile à casser sans s'en
apercevoir, et elle a déjà fait renuméroter treize renvois à tort (passe v0.20 du TOC).

| Cible | Forme | Exemple |
|---|---|---|
| Une section du compendium | `ch. N § N.M` — **espace** après le § | `ch. 44 § 44.1` |
| Une section d'un volume source | `§N.M` — **collé**, précédé du document | `Vol. I `*Monographie*` §1.3.4` |
| Une section de la pièce courante | `§ N.M` ou `voir § N.M` | `voir § 1.6.2` |

**Tout renvoi nomme son document** (décision 7 du TOC) : *Monographie*, *Synthèse*, *PRD*, *TOC*,
*PRDPlan*. Un renvoi nu est indécidable dès qu'un identifiant existe en deux séries — et plusieurs
existent :

- **`R-N` nu est indécidable** : R-1…R-8 sont les garde-fous du Vol. II, R-01…R-14 ceux du Vol. III.
  Toujours préfixer du volume.
- **`F-xx` nu est indécidable** : le Vol. II a F-01…F-48, le Vol. III a F-01…F-98 propres plus
  H-01…H-33 héritées. Tant que la renumérotation de G-3 n'est pas publiée, préfixer du volume
  d'origine (PRD §6).
- **`PRDPlan §N` nu est indécidable** entre celui du Vol. II et celui du Vol. III. Nommer le volume à
  toute occurrence neuve.
- **Deux séries « Q n »** existent au Vol. II. Nommer la série.

⚠ **Un renvoi vers un chapitre non rédigé est un renvoi de plan, pas un renvoi de texte.** Il résout
contre l'entrée du TOC, jamais contre une pièce. Le déclarer dans la note de statut, et le
re-vérifier quand le chapitre cible existera — un renvoi de plan qui survit à la rédaction de sa
cible sans revérification est exactement le défaut que la décision 8 du TOC proscrit.

## 2. Marqueurs et réserves

**`⚠` ne sert qu'à une chose** : signaler une **ressource vivante** — une page ou une spécification
sans version datée stable — ou, dans la prose de gouvernance, un point que le lecteur casserait s'il
ne le voyait pas. Une réserve portant sur le **contenu** d'une source s'écrit `**Réserve —**`.
Surcharger le marqueur rend indistinguables une page qui bouge et un fait qu'il faut nuancer.

**`Lecture de l'auteur`** précède toute construction d'auteur (CA-IV-07), et se suit de ce que le
socle établit et n'établit pas. Les chapitres de matière neuve — ch. 41, ch. 47-48 — le portent
**dès l'ouverture**, leur régime étant celui-là de bout en bout.

## 3. Garde-fous et formulations imposées

**Pas de troisième série.** Le compendium applique les deux séries héritées telles que le TOC les
assigne chapitre par chapitre. Les formulations les plus violées d'inadvertance (PRD §8) :

| Écrire | Jamais | Pourquoi |
|---|---|---|
| « **attendu par** E-23 » | « exigé par » | la ligne directrice pose des attentes, pas des exigences ; la « supervision humaine » n'est pas une des cinq attentes au socle |
| « quatre **cibles successives** — 2019, 2022, 2023, 2026 » | « quatre reports » ; « lancé » | réserve F-29, R-4 du Vol. II — le RTR n'est pas lancé |
| jalons NIST « **visés** » | « fixés » | R-11 du Vol. III ; porter aussi le statut du document (IR 8547 est un brouillon) |
| MCP : « **cadre** d'autorisation » | « sécurisé » | réserve F-01 |
| art. 12.1 : le flux outille **un point d'arrêt humain** | « la révision de l'article 12.1 » | Vol. II ch. 23 |
| qualifier un mécanisme par ce que sa spécification **démontre** | par ce qu'elle **promet** | R-02 du Vol. III — c'est cette règle, non un jugement d'humeur, qui fait du ch. 15 le chapitre « à plus haut risque de surinterprétation » |

**Jamais nus** : « AgentMesh », « control plane », « ACP », « autonomie graduée » (R-04 branche (f),
R-8 du Vol. II, R-13 du Vol. III). ⚠ Faux ami fréquent : « **plan de contrôle** » au sens du maillage
de services **pré-agentique** (ch. 1 § 1.3.4) n'est pas le « control plane » que R-13 vise — le
déclarer dans le champ *Garde-fous balayés* plutôt que de le fuir.

⚠ **« Fabrique » désigne quatre objets, dont deux vivent dans le plan** (décision 12c) : la *fabrique
d'identité* du ch. 43 § 43.1 et la *fabrique d'agents* du ch. 41. Ne jamais employer le mot sans que
le sens soit déterminable de la phrase ; ni l'un ni l'autre n'est le patron *factory* du catalogue
GoF, ni un titre d'éditeur.

**Trois degrés d'absence** (R-14 du Vol. III), jamais interchangeables :

1. *fait négatif vérifié* — établi par balayage documenté ;
2. *fait négatif établi* ;
3. *absence de documentation* — **n'autorise aucune conclusion**.

Le degré 3 est le cas courant et le plus mal écrit. « Aucun modèle de maturité ne traite le
non-déterminisme agentique » est presque toujours un degré 3 : le corpus consulté n'en documente
aucun, ce qui ne dit rien des autres. Écrire l'insuffisance constatée, pas l'impossibilité établie.

**Métriques auto-déclarées** : attribuées à leur source **à chaque occurrence**, sans exception
d'usage illustratif (PRD Vol. II §7.5). Un statut *preview* n'est jamais présenté comme une
disponibilité générale.

## 4. Cardinaux et décomptes

⚠ **Les décomptes ne se recopient pas, ils se re-mesurent.** Un même chiffre vit à plusieurs endroits
— README du dépôt, README du volume, `CLAUDE.md`, PRD, TOC, registre de gel — et se met à jour
partout ensemble.

⚠ **Tant que G-2 est ouverte, aucun décompte de pièce n'est publiable.** La commande de référence
n'est pas validée sur les trois corpus. Toute mesure prise est indicative et se refera. Le Vol. II a
payé l'ordre inverse : commande publiée après un test sur deux fichiers pour vingt-neuf, puis quatre
mesures successives (89 757 → 88 021 → 90 362 → 92 059) avant d'arrêter un chiffre.

⚠ **Un cardinal annoncé en toutes lettres ne se met pas à jour tout seul.** Le piège n'est pas le
nombre posé au titre d'une liste — c'est celui qui la **cite à distance**, dans une synthèse ou une
clôture. Ajouter un item sans re-mesurer produit une contradiction interne que le rendu ne signale
jamais.

⚠ **Toute table porte une légende** (ligne `: …` en Markdown, `<p class="legende">` en HTML). Une
table sans légende consomme quand même un numéro et creuse un trou dans la série. Et une table
insérée en amont décale tous les « tableau N » cités en aval.

## 5. Les trois régimes de preuve

Le compendium en porte trois et les déclare plutôt que de les lisser (PRD §7.2) :

| Régime | Pièces | Vote adversarial | Plancher |
|---|---|---|---|
| **Sources gelées et vérifiées** | Livres I, III, second mouvement du IV, second mouvement du V | réservé aux affirmations qui portent seules la thèse d'un chapitre, et aux faits vivants re-datés | [B] par extraction citée pour tout fait central neuf |
| **Source rédigée non publiable** | Livre II, ch. 37-40 | idem, **plus** toute affirmation issue d'une pièce du Vol. III touchée par une remontée ouverte | niveau d'origine conservé, sous G-4 |
| **Matière neuve** | ch. 41, ch. 47-48 | **toutes** les affirmations centrales | sources primaires seules ; échec documenté = résultat (retrait, G-6) |

Conséquence assumée : la proportion d'entrées [A] varie par livre, et **chaque tête de livre la
déclare**.

⚠ **Héritage du Vol. I : ses faits entrent en [C]**, sa vérification portant sur les références et
non sur le contenu des affirmations. L'élévation en [B] passe par la **lecture de la source primaire
que le Vol. I cite** — obligatoire avant tout fait central. Une entrée sans source primaire tierce
(construction d'auteur du Vol. I) reste une thèse attribuée et ne porte jamais un fait central.

## 6. Numérotations : trois séries qui coexistent

Chapitres, sections et livres se numérotent séparément dans le `TOC.md`, et **trois cartes de
renumérotation se chaînent** — décisions 11 (v0.20), 12 (v0.22), 13 (v0.23) :

- un « ch. 57 » gelé désigne le ch. 50 de la v0.21, le ch. 51 de la v0.22, le **ch. 50** courant ;
- un « Livre IX » gelé désigne la matière neuve, aujourd'hui premier mouvement du **Livre V**.

⚠ **Les journaux et rangées d'historique du TOC citent la numérotation de leur passe et ne se
corrigent jamais.** Une carte de correspondance réécrite reste cohérente à la lecture et fait
résoudre les renvois gelés au mauvais chapitre — c'est le défaut le plus silencieux rencontré par ce
projet (passe v0.23).

## 7. Sources absentes du dépôt

Deux sources que le plan cite ne sont plus dans l'arbre de travail. Leurs renvois **restent exacts**,
ils cessent d'être **opposables**.

| Source | Retirée le | Commit | Où la lire |
|---|---|---|---|
| `Synthese Monographie.md` (Vol. I et II) | 22 juillet 2026 | `fd8f1be` | arbre gelé `fd8f1be~1` (CA-IV-05) |
| Démonstrateur `Borealis-Go/` (Vol. I) | 25 juillet 2026 | `60f57f6` | historique git |

Ne pas les restaurer, ne pas réécrire les citations. Une reprise verbatim se vérifie contre l'arbre
gelé ; à défaut, se déclarer reprise **en substance**.

⚠ **Erreur documentée des TOC sources** : la *Synthèse* du Vol. I est numérotée **§1-§12** ; les TOC
des Vol. I et III portent encore « §3-§12 », qui est faux. Une collation contre eux réintroduirait
l'erreur en croyant la corriger.

## 8. Pièges datés — ce qui a déjà coûté une passe

- **Ajouter du contenu peut périmer un identifiant qu'on n'a pas touché.** Le ch. 32 ne consommait
  que le Vol. II : son garde-fou « R-5 » nu était décidable. Une addition y a introduit une mention
  de l'échelle R-14 du Vol. III, ce qui en a fait un chapitre **mixte** et rendu ce « R-5 »
  indécidable. Le défaut n'était pas dans la ligne ancienne mais dans son **voisinage neuf**, et
  seule l'exécution de `check-toc.py` l'a montré. **Exécuter les contrôles après toute addition,
  même sans retrait ni renumérotation.**
- **Une double revendication qu'aucun contrôle n'attrape.** Quand une ligne Fusion absorbe un
  intervalle de chapitres (« Vol. III ch. 5-7 ») pendant qu'un autre chapitre en prélève une section
  nommée (« §7.4 »), les deux renvois sont valides isolément et vivent à des grains différents :
  aucun script ne les rapproche. **Collation manuelle**, à refaire à chaque révision d'une ligne
  Fusion citant un intervalle.
- **Une arrivée se déclare aux deux bouts.** Le §2.8.5 du Vol. I était déclaré à son *départ* (ch. 6)
  et nulle part à son *arrivée* (ch. 4) : un chapitre rédigé sur sa seule liste de sections aurait
  perdu une section.
- **Trois passes de structure consécutives ont vu leur défaut échapper au script** (v0.18, v0.22,
  v0.23), dont quatorze formes fautives du genre `§ 51.1-50.3` qu'aucun des quatorze contrôles ne
  signalait. **Une passe de structure se relit ligne à ligne** ; le script ne le fera pas à sa place.
- **Le corpus d'appui du Vol. III n'est pas une source.** Sa filiation a été retirée (P0.2, close par
  échec documenté, réversible) : les mentions « corpus d'appui » sont des marqueurs conditionnels de
  réouverture. Aucun chapitre ne se rédige en s'appuyant sur ces ouvrages sans dépôt effectif.
- **Deux divergences factuelles restent ouvertes** entre la veille et le Vol. II : la date de la
  version finale de la ligne directrice IA de l'AMF (30 mars contre 7 avril 2026 — la source est
  inaccessible aux outils, 403), et la gouvernance d'AP2 (**résolue** : don à la FIDO Alliance, 28
  avril 2026). Le cadrage du Vol. IV les tranche en faveur du Vol. II, mais **cet arbitrage n'a
  aucune autorité tant que le compendium n'est pas rédigé**. Les signaler, ne pas les lisser.
