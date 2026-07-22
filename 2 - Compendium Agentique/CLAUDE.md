# CLAUDE.md — Vol. IV, *La somme agentique* (compendium intégral)

Guide pour Claude Code (claude.ai/code) dans le dossier `2 - Compendium Agentique`. **Le fichier le
plus spécifique gagne** : ici, celui-ci ; les règles valant pour tout le dépôt (langue, décomptes,
faits datés, périmètre des fichiers de doc) sont au [`CLAUDE.md` racine](../CLAUDE.md) et ne sont
pas répétées.

## Les livrables — un plan et sa vue synoptique, pas un ouvrage

Deux fichiers. [`TOC.md`](TOC.md) (**v0.10, 21 juillet 2026 — 57 chapitres en 10 livres,
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
- **Décisions 9 et 10 (v0.8-v0.9)** — la matière neuve se déclare (Livre IX : « Fusion : aucune »,
  thèses marquées construction d'auteur) ; **le Livre X (clôture) reste terminal** — toute
  insertion se fait avant lui, renvois corrigés ; la décision 10 fixe la carte des dix livres, à
  chapitres strictement inchangés.
- **Autorité des sources** : sur le socle et les lacunes, le **PRD** d'un volume prime son TOC
  (Vol. II : onze lacunes, pas dix ; Vol. III : le PRD postdate et corrige le TOC).

## Pièges spécifiques à ce fichier

- ⚠ **Deux renumérotations gelées dans les journaux.** (1) Chapitres, v0.8 : les anciens ch. 52-54
  (horizon / frontière / péremption) sont devenus les **ch. 55-57** — correspondance au journal
  v0.8. (2) Livres, v0.9 : treize livres condensés en **dix** (anciens III-V = III ; anciens
  IX-X = VII ; VI→IV, VII→V, VIII→VI, XI→VIII, XII→IX, XIII→X) — correspondance au journal v0.9 ;
  un « Livre IX » de journal gelé désigne l'AgentMesh, non le livre de matière neuve. Les journaux
  et les rangées d'historique du bandeau citent la numérotation de leur passe — ne jamais les
  « corriger ».
- ⚠ **Cardinaux multi-sites** : tout décompte annoncé (57 chapitres, 10 livres, enveloppes,
  fourchette, « onze lacunes »…) vit en plusieurs endroits — rangée Version, Volumétrie, champ
  Contrôles, risques 1 et 11 — et se **re-mesure** avant d'être modifié, jamais recopié. La forme
  `~N 000 mots` est **réservée aux enveloppes de tête** (elle entre dans la somme contrôlée).
- ⚠ **Erreur documentée des TOC sources** : la *Synthèse* du Vol. I est numérotée **§1-§12** ; les
  TOC des Vol. I et III portent encore « §3-§12 », qui est faux. Une collation contre eux
  réintroduirait l'erreur en croyant la corriger (décision 7 et risque 10 du TOC).
- ⚠ **Corpus d'appui du Vol. III introuvable au dépôt** (lacune L-15, décision P0.2 non tranchée) :
  aucun chapitre consommateur ne se rédige en s'appuyant sur ces trois ouvrages.
- ⚠ **Relèves v0.7 et v0.10** : marquées « à instruire à la source primaire » — aucune n'entre au
  socle, ne re-tranche une divergence ni ne clôt une lacune sans extraction de la source primaire.
- ⚠ **L'angle mort du harnais est déclaré, non comblé** (risque 14, v0.10) : la couche d'exécution
  n'a de chapitre nulle part, et trois des huit relèves v0.10 atterrissent dans le Livre IX. **Ne
  pas en tirer un chapitre ni un livre** — la somme porte déjà un livre sans socle (risque 13), et
  l'arbitrage est une décision d'auteur, pas une décision de passe.

## Éditer le TOC — protocole de passe

1. Toute passe = **nouvelle version** : nouvelle rangée Version au bandeau (l'ancienne descend en
   rangée Historique, verbatim), champ Date mis à jour, **journal daté ajouté en fin de fichier**.
   Les journaux sont en ajout seul — un journal publié ne se réécrit pas, ses écarts se consignent
   dans la passe suivante.
2. **Contrôles** : `check-toc.py` est **introuvable au dépôt** (constat v0.7, reconduit v0.8) — le
   champ Contrôles est une spécification sans exécutable. Le reconstruire (domaine : chapitres
   1-57, dix livres) et le valider **par mutation** après constat qu'il passe sur le document
   intact est un préalable à toute publication. En attendant, chaque passe exécute au minimum le
   balayage ad hoc des journaux v0.8-v0.10 — chapitres 1-57 contigus et uniques ; dix livres I-X ;
   somme des enveloppes `~N 000 mots)*` = 305 (301 corps + 4 avant-propos ; 394 000 avec les
   89 000 d'annexes ; l'enveloppe est toujours en **fin** d'en-tête de livre, sinon le motif ne la
   voit plus) ; aucun renvoi `ch. N` hors de 1-57 ; aucune occurrence normative des anciennes
   numérotations (chapitres et livres) hors zones gelées — et **déclare dans son journal** que le
   script n'a pas tourné.
3. **Git** : messages courts en français, par livrable (« TOC v0.8 — … »), comme l'historique du
   dossier ; chemins explicites à l'ajout.
