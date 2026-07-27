# Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique

Répertoire de rédaction du **Livre I** du compendium *La somme agentique* (Vol. IV). Il ne porte
aucune décision, aucun socle et aucun garde-fou propre : la spécification de contenu est le
[`PRD/TOC.md`](../PRD/TOC.md) v0.23, la gouvernance de la rédaction le [`PRD/PRD.md`](../PRD/PRD.md)
v0.7. En cas d'écart entre une pièce de ce dossier et le TOC, **le TOC prime** — sauf déviation
fondée, qui se déclare (décision 8 du TOC) et se remonte, jamais se corrige au plan depuis ici.

## ⚠ État : une seule pièce, en brouillon, rédigée hors portes

Le Livre I compte **onze chapitres** au plan (ch. 1-11), en deux mouvements — les fondements
(ch. 1-6), la couche protocolaire agentique (ch. 7-11). **Une seule est rédigée.**

| Pièce | Chapitre | État |
|---|---|---|
| [`01-interoperabilite-integration-entreprise.md`](01-interoperabilite-integration-entreprise.md) · [`.html`](01-interoperabilite-integration-entreprise.html) | Ch. 1 — L'interopérabilité comme problème d'intégration d'entreprise | **Brouillon, non publiable** |
| — | Ch. 2 à 11 | non rédigés |

⚠ **Le chapitre 1 a été rédigé sur instruction d'auteur du 27 juillet 2026, avant le franchissement
des portes G-1, G-2 et G-3** du PRD §5, qui posent qu'aucun chapitre ne se rédige avant le gel
unique, la commande de décompte de référence et la refonte du socle. L'écart est **déclaré, non
dissimulé** : la pièce porte en tête son en-tête à cinq champs et, en clôture, une **§ 1.8 « Note de
statut »** hors plan qui énumère les quatre conséquences de cet écart et ouvre deux remontées de
gouvernance (R-IV-01, bloquante pour le ch. 6 ; R-IV-02, non bloquante). Cette section **se retire à
la publication** — elle n'est pas au TOC.

Trois conséquences valent d'être connues avant de lire ou de réutiliser la pièce :

- **Aucun énoncé n'y est central au sens de CA-IV-01.** L'Annexe B n'existe pas ; les faits
  résolvent contre le Vol. I *Monographie* §1.0-1.6, en régime **[C]** (PRD §7.1). Leur élévation
  en [B] par lecture des sources primaires que le Vol. I cite est un préalable de publication.
- **Aucun décompte n'est publiable** — la commande de décompte de référence est la porte G-2, non
  franchie. La volumétrie annoncée en tête de pièce est une enveloppe, pas une mesure.
- **Les renvois « ch. N » sont des renvois de plan, non de texte** : ils résolvent contre l'entrée
  du TOC v0.23, aucun chapitre cible n'étant rédigé. Ils se re-vérifient contre le texte quand il
  existera.

## Les deux formats

Chaque pièce existe en **deux rendus de la même matière**, versionnés ensemble :

- le **`.md`** — la source ; c'est lui qui fait foi ;
- le **`.html`** — page autonome à thème sombre orange, sans aucune ressource externe (CSS et script
  intégrés, aucune police ni image distante), **prose justifiée avec césure automatique**,
  navigation de chapitre, barre de progression, styles d'impression. Elle se lit hors ligne par
  simple ouverture dans un navigateur. ⚠ La césure s'appuie sur l'attribut `lang="fr-CA"` du
  document : le retirer désactiverait la coupure des mots **sans prévenir**, et une justification
  sans césure creuse des lézardes dans une colonne de cette largeur. Titres, légendes et navigation
  restent au fer à gauche — les justifier y produirait des trous.

⚠ **Le `.html` est un rendu, pas une seconde source.** Toute correction se fait dans le `.md` puis
se reporte dans le `.html` au même commit — jamais l'inverse, jamais l'un sans l'autre (même règle
que « PDF versionné avec sa source » au [`CLAUDE.md`](../../CLAUDE.md) du dépôt). Le compendium n'a
pas de pipeline de rendu : les trois copies du FESP appartiennent aux Vol. I, II et III, et aucune
n'a été copiée ici.

⚠ **Ce n'est pas une page de publication en ligne.** Les deux `index.html` du dépôt ont été
supprimés le 22 juillet 2026 (commit `fd8f1be`) parce qu'ils annonçaient des adresses GitHub Pages
fausses ; ce fichier ne les rétablit pas, ne porte aucune balise `canonical` ni `og:url`, et
n'implique aucune activation de Pages.

## Ce que le chapitre 1 couvre — et ce qu'il ne couvre pas

La pièce suit section par section la table des matières détaillée du TOC : § 1.0 introduction et
invariant, § 1.1 fondements et théorie, § 1.2 cadres de référence et modèles de maturité, § 1.3
architectures d'intégration, § 1.4 styles d'API, § 1.5 messagerie et événementiel, § 1.6 patrons et
coordination, § 1.7 synthèse (section de sortie, construction d'éditeur).

Trois matières en sont **absentes par arbitrage**, conformément à la ligne Fusion — les y ajouter
casserait la table de couverture du chapitre :

| Matière | Destination | Régime |
|---|---|---|
| Sémantique, formats, ontologies (Vol. I §1.7-1.8) | ch. 2 | hors périmètre |
| Héritage IAM, *zero trust*, gouvernance (Vol. I §1.9-1.10) | ch. 3 | hors périmètre |
| Exécution durable, pipelines, orchestration agentique (Vol. I §1.6.3) | ch. 22 (Livre III) | déplacé **en entier** |
| Déclinaison agentique du maillage (Vol. I §1.3.4, part agentique) | ch. 37 (Livre IV) | **scindé**, socle transposable conservé ici |
| Tendances agentiques 2024-2026 (Vol. I §1.11) | — | coupe assumée |

## Avant d'ajouter une pièce ici

1. Lire le [`CLAUDE.md`](../CLAUDE.md) du compendium — il porte le plafond dur de cinquante
   chapitres, le protocole d'insertion et les pièges propres au `TOC.md`.
2. Reprendre l'entrée du chapitre au [`TOC.md`](../PRD/TOC.md) : thèse, sections, ligne Fusion,
   table détaillée, table de couverture. **Chaque entrée du TOC est le cahier des charges de son
   chapitre** ; ce répertoire n'en contient aucune copie.
3. Porter l'en-tête à cinq champs du PRD §6 — Statut, Date de gel, Socle mobilisé, Garde-fous
   balayés (**y compris à zéro occurrence**), Volumétrie cible — puis la thèse citée depuis le TOC.
4. Écrire le `.md` et le `.html` **dans la même passe**, et les committer ensemble.
