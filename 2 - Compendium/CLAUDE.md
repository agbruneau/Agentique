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

Trois fichiers, par ordre d'autorité. [`PRD.md`](PRD/PRD.md) (**v0.4, 25 juillet 2026**) régit la
**gouvernance de la rédaction** — portes de lancement, ordre, régimes de preuve, seuil de vote,
critères CA-IV, jalons, décisions d'auteur — et **prime en cas de conflit sur la gouvernance, le
socle et les lacunes**. [`TOC.md`](PRD/TOC.md) (**v0.19, 26 juillet 2026 — 57 chapitres en 10 livres,
projection ≈ 369 000–394 000 mots**) reste la *spécification de contenu* du compendium — autorité
sur le découpage et sur chaque chapitre (thèse, sections, ligne Fusion, socle, garde-fous) ;
**aucun chapitre n'est rédigé**. Tant que la somme n'est pas écrite, les trois volumes sources
font foi (champ Statut du TOC), et une thèse de ce plan n'est pas une source (sa propre
décision 8). [`README.md`](README.md) est la **vue synoptique dérivée** du TOC (le « conspectus » du volume, même
version en tête) : il ne porte aucune décision, aucun socle, aucun garde-fou propre — en cas
d'écart, **le TOC prime**, et toute passe qui modifie le TOC réaligne le conspectus (version,
faits touchés) ou y déclare le retard en tête.

⚠ **`audit.md` n'est pas un quatrième livrable.** C'est un rapport de couverture daté (24 juillet 2026), **sans autorité** : ni source, ni socle, ni décision. Ne jamais le citer à l'appui d'un énoncé ni s'en servir pour modifier le plan — ses constats retenus ont été portés là où ils font foi (risque 15 du TOC, décision D-7 du PRD, passe v0.15) ; ce qu'il porte encore n'a pas été retenu. Un audit ultérieur suit la même règle : il **remonte**, il ne tranche pas.

⚠ **Le TOC porte, depuis la v0.16 (25 juillet 2026), une table des matières détaillée par chapitre — et ces tables sont subordonnées.** Chaque entrée de chapitre est suivie du dépliage de ses sections et sous-sections, chacune portant sa **provenance** (`← Vol. N` *document* `§N.M`), plus une **table de couverture** par chapitre (décision 6). Les 57 chapitres en sont pourvus, dérivés du **texte rédigé** des trois monographies. ⚠ **Une table déplie une ligne Fusion, elle ne la re-décide pas** : en cas d'écart, **la ligne Fusion prime**, et quand le chapitre sera rédigé, c'est **lui** qui corrigera la table (décision 8). *Le travail a vécu dans un fichier séparé, `TOCAll.md`, renommé sur le TOC à sa complétion ; ce fichier n'existe plus, ses quatre commits restent à l'historique.*

⚠ **Depuis la v0.18 (26 juillet 2026), ces tables sont en titres markdown, et la hiérarchie de niveaux fait convention.** `## LIVRE N` → `### Chapitre N` → `#### § N.M` : les sections sont les **enfants directs** du chapitre, ce qui expose le plan complet du fichier dans tout afficheur de plan (éditeur, forge, table des matières Pandoc). Trois corollaires, qu'une passe ultérieure ne doit pas « corriger » en croyant réparer une anomalie : **(a)** « Table des matières détaillée du chapitre N » et « Table de couverture (décision 6) » sont des **paragraphes gras, pas des titres** — les promouvoir en `####` les interposerait entre le chapitre et ses sections ; **(b)** les **sous-sections restent en listes**, délibérément — ce sont des phrases descriptives portant leur provenance, non des intitulés, et les promouvoir produirait un plan de plus de mille entrées, donc illisible ; **(c)** il n'y a **aucun index de tête**, et il n'en faut pas — un index serait un cardinal de plus à tenir à jour (risque 1) là où les titres se dérivent d'eux-mêmes. ⚠ **Et le point qui compte le plus : `check-toc.py` ne voit rien de cette forme.** Ses quatorze contrôles portent sur des motifs de ligne (titre de chapitre, titre de livre, rangées du bandeau, enveloppes de tête, registre des lacunes) ; aucun ne connaît les tables détaillées. Un reformatage passe donc **sans être validé par l'appareil versionné**, et le seul contrôle qui en prouve la fidélité est la comparaison du **flux de mots** avant/après (v0.18 : 72 764 mots, séquence identique) — à refaire, et à déclarer au journal, à toute passe qui touche à la forme.

⚠ **Les ch. 52-54 (Livre IX) n'ont aucune table de provenance, et c'est un fait, non un manque.** Matière neuve, « Fusion : aucune » (décision 9) : aucun renvoi `←` n'y est possible, les seuls appuis sont **internes** (chapitres de la somme) et tout énoncé y est au mieux un **repérage [C] à instruire**. La décision 6 (couverture tracée) y est sans objet ; la **décision 8 s'y applique doublement**.

⚠ **Ajouter du contenu à un chapitre peut périmer un identifiant qu'on n'a pas touché** — leçon de la v0.16, et le piège le plus contre-intuitif de ce fichier. Le ch. 36 ne consommait que le Vol. II : son garde-fou « R-5 » nu était décidable. La table détaillée y a introduit une mention de l'**échelle R-14 du Vol. III**, ce qui en a fait un **chapitre mixte** et rendu ce « R-5 » indécidable (C8). Le défaut n'était pas dans la ligne ancienne mais dans son **voisinage neuf**, et seule l'exécution de `check-toc.py` l'a montré — la relecture ne l'attrape pas. Même classe au ch. 47 (« R-8 »). **Exécuter le contrôle après toute addition, même quand on n'a rien retiré ni renuméroté.**

⚠ **Convention de renvoi (décision 7), appliquée par les tables détaillées** : le Vol. III vit en numérotation multiple, et **ses chapitres sont désormais rédigés** — un renvoi au texte s'y écrit `Vol. III `*Monographie*` §N.M`, un renvoi au plan `Vol. III `*TOC*` §N.x`. ⚠ Le **TOC du Vol. III n'a pas de titres `§N.M`** : il nomme ses sections en prose sous des `### Chapitre N`, comme celui du compendium — un renvoi « Vol. III *TOC* §N.M » ne s'y vérifie donc pas par titre, et c'est contre la *Monographie* rédigée qu'il résout, à numérotation et titre concordants (constat de la collation v0.14, re-vérifié le 25 juillet 2026 sur les sept renvois de ce domaine).

⚠ **Un « PRDPlan §N » nu est indécidable entre deux documents** — collision relevée au balayage du 25 juillet 2026, de la classe même que la décision 7 proscrit (« un R-7 nu est indécidable »). Le TOC emploie la forme nue pour **deux** PRDPlan : §4.2 et §4.4 désignent celui du **Vol. II** (formulations types, boucle qualité), §1.5 et §5.3 celui du **Vol. III** (commande de décompte, règle d'escalade). Le contexte tranche à la lecture, jamais le renvoi. **L'occurrence en zone normative est nommée depuis la v0.17** (`PRDPlan Vol. II §4.4`, ch. 29) ; celles de l'avant-propos et des journaux gelés gardent leur forme d'origine. **Nommer le volume à toute occurrence neuve.**

⚠ **Les treize écarts relevés par la v0.16 sont soldés par la v0.17** — chacun par une règle que le plan porte déjà (décisions 2, 6, 7 et 8), **jamais par un choix de contenu neuf**. Détail au journal v0.17 du TOC. Trois d'entre eux valent d'être connus avant d'éditer :

- **Une source vide, corrigée par la décision 8.** Le « volet RGPD » que les ch. 31 et 34 se partageaient n'existe plus : le Vol. III rédigé l'a retiré de son ch. 20 le 22 juillet 2026 (arbitrage **R-G-38**), son socle ne documentant « ni le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation*, degré 3, **non** fait négatif vérifié. Le ch. 31 reçoit ce chapitre **en entier**, le ch. 34 garde sa matière RGPD par le **Vol. I** (§4.8.4, §5.3). ⚠ **La lacune 16 du Vol. III est entrée au registre de l'Annexe C, dans une SECONDE table** : les lacunes du Vol. III forment une série distincte des onze du Vol. II, et les fondre périmerait un cardinal contrôlé. **Cette seconde table se déclare incomplète** — une entrée, non un inventaire ; le dresser est un préalable de la collation de fond (porte G-4).
- **Une classe de double revendication qu'aucun contrôle n'attrape.** Quand une ligne Fusion absorbe un **intervalle de chapitres** (« Vol. III ch. 5-7 ») pendant qu'un autre chapitre en prélève **une section** nommée (« §7.4 »), les deux renvois sont valides isolément et vivent à des grains différents : `check-toc.py` ne les rapproche pas. **Collation manuelle, à refaire à chaque révision d'une ligne Fusion citant un intervalle.**
- **Une arrivée se déclare aux deux bouts.** Le §2.8.5 du Vol. I était déclaré à son *départ* (ch. 6) et nulle part à son *arrivée* (ch. 4) : un chapitre rédigé sur sa seule liste de sections aurait perdu la section que la v0.5 avait sauvée.

⚠ **Ce que la v0.17 n'a pas touché, et qu'une passe de cohérence ne doit jamais toucher** : les **risques 13, 14 et 15** (Livre IX sans socle, couche d'exécution sans chapitre, accord entre agents sous défaillance) portent sur du **contenu manquant**, non sur une incohérence — leur arbitrage est une décision d'auteur (**D-7** du PRD). De même la thèse forte du ch. 20, à instruire par dénombrement.

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
- ⚠ **Relèves v0.7, v0.10, v0.11 et v0.19** : marquées « à instruire à la source primaire » — aucune
  n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune sans extraction de la
  source primaire. Les relèves v0.11 (l'après-agentique) citent des préimpressions arXiv dont
  seuls les résumés ont été consultés : repérages [C], jamais des faits. ⚠ **Les huit relèves
  v0.19** (couverture en science et génie informatique — ch. 6, 18, 20, 28, 42, 52 et 53) citent
  au contraire des **documents normatifs et des articles de revue consultés à leur source**
  (RFC 8693 et 9334, SLSA v1.2, in-toto, CycloneDX 1.7 / ECMA-424, SPDX 3.0, NIST SP 800-218A,
  NIST AI 100-2 E2025, OPA/Rego, FLP, Gilbert-Lynch, Castro-Liskov, Dean-Barroso, test
  métamorphique). **Le régime ne change pas pour autant** : un document lu à la source reste une
  **relève**, jamais une entrée de socle — la refonte du socle est la porte G-3 du PRD, pas le
  produit d'une passe de plan. ⚠ **Trois réserves de relevé sont portées dans le texte** (date
  d'approbation de SLSA v1.2, version de SPDX que fixe l'ISO/IEC 5962:2021, DOI de Castro-Liskov) :
  ne pas les « compléter » de mémoire — ce qui n'a pas été vu à la source ne s'écrit pas comme vu.
  ⚠ **Et ces marques ne sont pas contrôlées** : C11 ne connaît que les listes v0.10 et v0.11,
  inscrites dans le script ; y ajouter la v0.19 est une **passe d'appareil** à valider par mutation.
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
