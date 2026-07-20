# CLAUDE.md — Vol. IV, *La somme agentique* (compendium intégral)

Guide pour Claude Code (claude.ai/code) dans le dossier `2 - Compendium Agentique`. **Le fichier le
plus spécifique gagne** : ici, celui-ci ; les règles valant pour tout le dépôt (langue, décomptes,
faits datés, périmètre des fichiers de doc) sont au [`CLAUDE.md` racine](../CLAUDE.md) et ne sont
pas répétées.

## Les livrables — un plan et sa vue synoptique, pas un ouvrage

Deux fichiers. [`TOC.md`](TOC.md) (**v0.8, 20 juillet 2026 — 57 chapitres en 13 livres,
projection ≈ 369 000–394 000 mots**) est la *spécification* du compendium ; **aucun chapitre
n'est rédigé**. Tant que la somme n'est pas écrite, les trois volumes sources font foi (champ
Statut du TOC), et une thèse de ce plan n'est pas une source (sa propre décision 8).
[`Conspectus.md`](Conspectus.md) est la **vue synoptique dérivée** du TOC (même version en tête) :
il ne porte aucune décision, aucun socle, aucun garde-fou propre — en cas d'écart, **le TOC
prime**, et toute passe qui modifie le TOC réaligne le conspectus (version, faits touchés) ou y
déclare le retard en tête.

**Pas de pipeline PDF ici.** Le Vol. I et le Vol. II ont chacun leur copie du FESP ; en créer une
pour ce dossier serait une troisième copie — même interdit que celui consigné pour le Vol. III au
`CLAUDE.md` racine.

## L'appareil interne du TOC fait loi

Le TOC porte ses propres règles de gouvernance ; les lire avant d'éditer, ne pas les réinventer :

- **Décision 7** — tout renvoi nomme son document (*Monographie*/*Synthèse*/*PRD*/*TOC*), sa série
  (deux séries « Q n » au Vol. II) et son volume (R-1…R-8 du Vol. II ≠ R-01…R-14 du Vol. III).
- **Décision 8** — le plan s'aligne sur le chapitre rédigé, jamais l'inverse ; une déviation fondée
  se déclare.
- **Décision 9 (v0.8)** — la matière neuve se déclare (Livre XII : « Fusion : aucune », thèses
  marquées construction d'auteur) ; **le Livre XIII (clôture) reste terminal** — toute insertion se
  fait avant lui, renvois corrigés.
- **Autorité des sources** : sur le socle et les lacunes, le **PRD** d'un volume prime son TOC
  (Vol. II : onze lacunes, pas dix ; Vol. III : le PRD postdate et corrige le TOC).

## Pièges spécifiques à ce fichier

- ⚠ **Renumérotation v0.8** : les anciens ch. 52-54 (horizon / frontière / péremption) sont devenus
  les **ch. 55-57**. Les journaux v0.3-v0.7 et les rangées d'historique du bandeau sont **gelés et
  citent l'ancienne numérotation** — ne jamais les « corriger » ; la correspondance est au journal
  v0.8.
- ⚠ **Cardinaux multi-sites** : tout décompte annoncé (57 chapitres, 13 livres, enveloppes,
  fourchette, « onze lacunes »…) vit en plusieurs endroits — rangée Version, Volumétrie, champ
  Contrôles, risques 1 et 11 — et se **re-mesure** avant d'être modifié, jamais recopié. La forme
  `~N 000 mots` est **réservée aux enveloppes de tête** (elle entre dans la somme contrôlée).
- ⚠ **Erreur documentée des TOC sources** : la *Synthèse* du Vol. I est numérotée **§1-§12** ; les
  TOC des Vol. I et III portent encore « §3-§12 », qui est faux. Une collation contre eux
  réintroduirait l'erreur en croyant la corriger (décision 7 et risque 10 du TOC).
- ⚠ **Corpus d'appui du Vol. III introuvable au dépôt** (lacune L-15, décision P0.2 non tranchée) :
  aucun chapitre consommateur ne se rédige en s'appuyant sur ces trois ouvrages.
- ⚠ **Relèves v0.7** : marquées « à instruire à la source primaire » — aucune n'entre au socle, ne
  re-tranche une divergence ni ne clôt une lacune sans extraction de la source primaire.

## Éditer le TOC — protocole de passe

1. Toute passe = **nouvelle version** : nouvelle rangée Version au bandeau (l'ancienne descend en
   rangée Historique, verbatim), champ Date mis à jour, **journal daté ajouté en fin de fichier**.
   Les journaux sont en ajout seul — un journal publié ne se réécrit pas, ses écarts se consignent
   dans la passe suivante.
2. **Contrôles** : `check-toc.py` est **introuvable au dépôt** (constat v0.7, reconduit v0.8) — le
   champ Contrôles est une spécification sans exécutable. Le reconstruire (domaine : chapitres
   1-57, treize livres) et le valider **par mutation** après constat qu'il passe sur le document
   intact est un préalable à toute publication. En attendant, chaque passe exécute au minimum le
   balayage ad hoc du journal v0.8 — chapitres 1-57 contigus et uniques ; livres I-XIII ; somme des
   enveloppes `~N 000 mots)*` = 305 (301 corps + 4 avant-propos ; 394 000 avec les 89 000
   d'annexes) ; aucun renvoi `ch. N` hors de 1-57 ; aucune occurrence normative de l'ancienne
   numérotation hors zones gelées — et **déclare dans son journal** que le script n'a pas tourné.
3. **Git** : messages courts en français, par livrable (« TOC v0.8 — … »), comme l'historique du
   dossier ; chemins explicites à l'ajout.
