# CLAUDE.md — Vol. IV, *La somme agentique* (compendium intégral)

Guide pour Claude Code (claude.ai/code) dans le dossier `2 - Compendium` (renommé le 25 juillet 2026,
`2 - Compendium Agentique` auparavant, commit `60f57f6`). **Le fichier le
plus spécifique gagne** : ici, celui-ci ; les règles valant pour tout le dépôt (langue, décomptes,
faits datés, périmètre des fichiers de doc) sont au [`CLAUDE.md` racine](../CLAUDE.md) et ne sont
pas répétées.

## Les livrables — un plan, sa gouvernance et sa vue synoptique, pas un ouvrage

⚠ **Réorganisation du 23 juillet 2026** : le PRD, le TOC et les deux scripts de contrôle vivent
désormais dans le sous-dossier [`PRD/`](PRD/) ; le README (conspectus) et ce `CLAUDE.md` restent à
la racine du dossier. Les chemins ci-dessous et la commande de contrôle (§ protocole) en tiennent
compte.

Trois fichiers, par ordre d'autorité. [`PRD.md`](PRD/PRD.md) (**v0.3, 24 juillet 2026**) régit la
**gouvernance de la rédaction** — portes de lancement, ordre, régimes de preuve, seuil de vote,
critères CA-IV, jalons, décisions d'auteur — et **prime en cas de conflit sur la gouvernance, le
socle et les lacunes**. [`TOC.md`](PRD/TOC.md) (**v0.15, 24 juillet 2026 — 57 chapitres en 10 livres,
projection ≈ 369 000–394 000 mots**) reste la *spécification de contenu* du compendium — autorité
sur le découpage et sur chaque chapitre (thèse, sections, ligne Fusion, socle, garde-fous) ;
**aucun chapitre n'est rédigé**. Tant que la somme n'est pas écrite, les trois volumes sources
font foi (champ Statut du TOC), et une thèse de ce plan n'est pas une source (sa propre
décision 8). [`README.md`](README.md) est la **vue synoptique dérivée** du TOC (le « conspectus » du volume, même
version en tête) : il ne porte aucune décision, aucun socle, aucun garde-fou propre — en cas
d'écart, **le TOC prime**, et toute passe qui modifie le TOC réaligne le conspectus (version,
faits touchés) ou y déclare le retard en tête.

⚠ **`audit.md` n'est pas un quatrième livrable.** C'est un rapport de couverture daté (24 juillet 2026), **sans autorité** : ni source, ni socle, ni décision. Ne jamais le citer à l'appui d'un énoncé ni s'en servir pour modifier le plan — ses constats retenus ont été portés là où ils font foi (risque 15 du TOC, décision D-7 du PRD, passe v0.15) ; ce qu'il porte encore n'a pas été retenu. Un audit ultérieur suit la même règle : il **remonte**, il ne tranche pas.

⚠ **`TOCAll.md` n'est pas non plus un livrable.** Copie de travail de [`PRD/TOC.md`](PRD/TOC.md) (créée le 25 juillet 2026), augmentée pour les **57 chapitres — les dix livres, couverture complète** — d'une table des matières détaillée dérivée du **texte rédigé** des sources : Vol. I *Monographie* ch. 1-7 et Annexe B, Vol. II *Monographie* ch. 1-24 et Annexe B, Vol. III *Monographie* ch. 1-28 et Annexe B. Chaque sous-section porte sa provenance et chaque chapitre porte sa table de couverture (décision 6). **Elle n'a pas d'autorité propre** : en cas d'écart avec la ligne Fusion du chapitre dans `PRD/TOC.md`, celle-ci prime. Elle n'est **pas couverte par `check-toc.py`** (hors de son domaine, `PRD/`) et se **désynchronise** à la prochaine passe du TOC si elle n'est pas reportée à la main. Maintenant que la couverture est complète, la reverser en **annexe du TOC** plutôt que de la maintenir en copie parallèle est la décision qui se pose.

⚠ **Les ch. 52-54 (Livre IX) n'ont aucune table de provenance, et c'est un fait, non un manque.** Matière neuve, « Fusion : aucune » (décision 9) : aucun renvoi `←` n'y est possible, les seuls appuis sont **internes** (chapitres de la somme) et tout énoncé y est au mieux un **repérage [C] à instruire**. La décision 6 (couverture tracée) y est sans objet ; la **décision 8 s'y applique doublement**.

⚠ **Convention de renvoi appliquée dans cette copie, et qui vaut d'être reprise** (décision 7) : le Vol. III vit en numérotation multiple, et **ses chapitres sont désormais rédigés** — un renvoi au texte s'y écrit `Vol. III `*Monographie*` §N.M`, un renvoi au plan `Vol. III `*TOC*` §N.x`. ⚠ Le **TOC du Vol. III n'a pas de titres `§N.M`** : il nomme ses sections en prose sous des `### Chapitre N`, comme celui du compendium — un renvoi « Vol. III *TOC* §N.M » ne s'y vérifie donc pas par titre, et c'est contre la *Monographie* rédigée qu'il résout, à numérotation et titre concordants (constat de la collation v0.14, re-vérifié le 25 juillet 2026 sur les sept renvois de ce domaine).

⚠ **Un « PRDPlan §N » nu est indécidable entre deux documents** — collision relevée au balayage du 25 juillet 2026, de la classe même que la décision 7 proscrit (« un R-7 nu est indécidable »). Le TOC emploie la forme nue pour **deux** PRDPlan : §4.2 et §4.4 désignent celui du **Vol. II** (formulations types, boucle qualité), §1.5 et §5.3 celui du **Vol. III** (commande de décompte, règle d'escalade). Le contexte tranche à la lecture, jamais le renvoi. À nommer — `PRDPlan Vol. II §4.4` — à la prochaine passe.

⚠ **Ce que la dérivation a fait remonter, et qui appartient au TOC, non à cette copie.** Onze écarts sont consignés dans les blocs concernés de `TOCAll.md`, **signalés et non corrigés** — les porter dans `PRD/TOC.md` relève d'une passe versionnée (bandeau, journal, `check-toc.py`), pas d'un fichier de travail.

- **Le plus lourd — une source vide.** Le ch. 34 tire un « **volet RGPD** » du ch. 20 du Vol. III, et le ch. 31 se déclare « volet Loi 25 **seul** » en conséquence. Or le Vol. III rédigé a **retiré le RGPD de ce chapitre le 22 juillet 2026** (arbitrage **R-G-38**) : son socle « ne documente pas le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation*, degré 3 —, « aucun rapprochement entre le régime québécois et le régime européen n'est donc opéré », et la lacune est portée au PRD du Vol. III **sous le numéro 16**. Trois conséquences : le ch. 31 reçoit le ch. 20 **en entier** ; la matière RGPD du ch. 34 est portée par le **Vol. I** (§4.8.4, §5.3), qui est intact ; et la **lacune 16 du Vol. III n'est pas enregistrée** au registre des lacunes héritées (Annexe C). C'est exactement ce que la **collation de fond** contre le Vol. III rédigé — préalable déclaré dont la v0.14 n'a levé que le volet structurel — a pour objet de trouver.
- **Sections couvertes par un intervalle de la ligne Fusion mais absentes de la phrase « Sections : … »** : §1.2 du Vol. I au ch. 1 (cadres de référence, ISO 11354, EIF/EIRA, modèles de maturité — zéro occurrence dans tout le TOC) ; §2.8.5 au ch. 4 (déclaré à son départ au ch. 6, jamais à son arrivée) ; ANP au ch. 8.
- **Listes de sections non réalignées sur une ligne Fusion corrigée** : « exécution durable » au ch. 1 ; « modèle de menace, vecteurs d'attaque » au ch. 6 (partis au ch. 20).
- **Doubles revendications que la décision 2 ou la décision 6 proscrit** : la fusion d'ACP, annoncée par le ch. 8 (Vol. I §3.3.4) *et* par le ch. 10 (Vol. II §3.3) ; le §3.4 du ch. 3 du Vol. II, pris en bloc par le ch. 10 alors que l'encadré R-8 siège au ch. 7 ; le **§7.4 du Vol. III**, absorbé en bloc par le ch. 16 (« Vol. III ch. 5-**7** ») et nommément prélevé par le ch. 17 — à trancher par un « hors §7.4 » explicite au ch. 16.
- **Section sans source nommée** : le « budget de latence et contention » du ch. 28 ne correspond à aucune sous-section du ch. 4 du Vol. I — à rattacher, ou à marquer construction d'auteur (décision 8).

**Pas de pipeline PDF ici.** Les Vol. I, II et III ont chacun leur copie du FESP — celle du Vol. III
créée le 23 juillet 2026, sur demande de l'auteur ; en créer une pour ce dossier serait une
**quatrième** copie, et il n'y a rien à rendre : aucun chapitre n'est rédigé. ⚠ *L'interdit initial
disait « troisième copie » ; le Vol. III a pris ce rang, décidé et daté. Le motif ne change pas —
chaque copie évolue seule, un correctif à l'une ne se propage à aucune autre.*

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
- ⚠ **Deux sources citées par le plan ne sont plus au dépôt, et la collation doit le savoir avant
  de la lancer.** *(a)* `Synthese Monographie.md` (Vol. I et Vol. II) a été supprimée le 22 juillet
  2026, commit `fd8f1be` ; *(b)* le démonstrateur `Borealis-Go/` (Vol. I) l'a été le 25 juillet
  2026, commit `60f57f6`. Toute collation de fond qui les vise se fait **contre l'historique git ou
  contre rien** — la décision 7 (« tout renvoi nomme son document ») ne suffit plus : elle désigne
  un document, elle ne dit pas s'il est présent. *Le plan ne se réécrit pas pour autant : ses
  renvois sont exacts, ils cessent d'être opposables.* La distinction se déclare à la passe qui
  ouvrira le Livre III ou le Livre VIII (l'ADS Boréalis y siège, annexe H).
- ⚠ **Corpus d'appui du Vol. III : filiation retirée** (P0.2 tranchée le 21 juillet 2026, L-15
  close par échec documenté — **réversible** par dépôt ultérieur) : les mentions « corpus
  d'appui » des chapitres consommateurs sont des marqueurs conditionnels de réouverture, jamais
  des sources ; aucun chapitre ne se rédige en s'appuyant sur ces ouvrages sans dépôt effectif.
- ⚠ **Le Vol. III est rédigé depuis le 22 juillet 2026** (34 pièces, socle F-01…F-98 + H-01…H-33,
  PRD v1.3 / TOC v0.8), mais « **rédigé ne vaut pas publiable** » : remontées ouvertes, arbitrages
  révocables, dette de vote (F-92, F-96 du Vol. III). La collation de fond contre son texte rédigé
  (l'homologue de la v0.6) est un **préalable déclaré** aux Livres III et VII, **dont la v0.14 du TOC
  a levé le volet structurel** (couverture complète et résolution des renvois de section, zéro écart —
  seul le volet de fond reste dû) ; et un « F-xx » nu
  est désormais **indécidable entre deux socles** — convention transitoire en décision 7 du TOC.
- ⚠ **Relèves v0.7, v0.10 et v0.11** : marquées « à instruire à la source primaire » — aucune
  n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune sans extraction de la
  source primaire. Les relèves v0.11 (l'après-agentique) citent des préimpressions arXiv dont
  seuls les résumés ont été consultés : repérages [C], jamais des faits.
- ⚠ **L'angle mort du harnais est déclaré, non comblé** (risque 14, v0.10) : la couche d'exécution
  n'a de chapitre nulle part, et trois des huit relèves v0.10 atterrissent dans le Livre IX. **Ne
  pas en tirer un chapitre ni un livre** — la somme porte déjà un livre sans socle (risque 13), et
  l'arbitrage est une décision d'auteur, pas une décision de passe.

## Éditer le TOC — protocole de passe

1. Toute passe = **nouvelle version** : nouvelle rangée Version au bandeau (l'ancienne descend en
   rangée Historique, verbatim), champ Date mis à jour, **journal daté ajouté en fin de fichier**.
   Les journaux sont en ajout seul — un journal publié ne se réécrit pas, ses écarts se consignent
   dans la passe suivante.
2. **Contrôles** : `python PRD/check-toc.py` (versionné dans `PRD/` depuis la v0.12 du 23 juillet
   2026 — contrôles C1-C14, domaine : chapitres 1-57, dix livres) **avant toute publication** ;
   sortie 0 exigée, et le journal de la passe déclare son exécution. ⚠ **Ce script est du
   contenu : il se vérifie comme le reste** (même règle que `check-veille.py` au `CLAUDE.md`
   racine). Toute modification se valide par mutation avec `PRD/check-toc-mutations.py` (versionné
   dans `PRD/`) : constat de passage sur le document intact, puis chaque classe de faute détectée. Des
   faux positifs y sont déjà neutralisés — zones gelées (rangées Historique, journaux) exemptées
   des contrôles de motifs, spans « … » et `` ` … ` `` retirés, marqueurs de correspondance des
   anciens numéraux de livres (Nature, décisions 9-10, risques 1 et 13) — les réintroduire en
   « simplifiant » un motif rendrait le contrôle bruyant donc ignoré. L'exécutable des passes
   v0.3-v0.6 (« contrôles 1-17 ») demeure perdu : les journaux gelés se lisent dans leur
   numérotation d'origine, correspondances en commentaire du script (C7 ≈ 17, C8 ≈ 11).
3. **Git** : messages courts en français, par livrable (« TOC v0.8 — … »), comme l'historique du
   dossier ; chemins explicites à l'ajout.
