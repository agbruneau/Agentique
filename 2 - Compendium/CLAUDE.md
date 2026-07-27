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

Trois fichiers, par ordre d'autorité. [`PRD.md`](PRD/PRD.md) (**v0.7, 27 juillet 2026** — réancré sur le TOC v0.23, gouvernance inchangée, décision d'auteur **D-8** ajoutée en v0.6) régit la
**gouvernance de la rédaction** — portes de lancement, ordre, régimes de preuve, seuil de vote,
critères CA-IV, jalons, décisions d'auteur — et **prime en cas de conflit sur la gouvernance, le
socle et les lacunes**. [`TOC.md`](PRD/TOC.md) (**v0.23, 27 juillet 2026 — 50 chapitres en 5 livres,
projection ≈ 376 000–401 000 mots ; plafond de cinquante chapitres posé en décision 13 et contrôlé par C15 ;
le ch. 41, la fabrique d'agents, entré en v0.22, est payé par la fusion des ch. 47 et 48**) reste la *spécification de contenu* du compendium — autorité
sur le découpage et sur chaque chapitre (thèse, sections, ligne Fusion, socle, garde-fous) ;
**aucun chapitre n'est rédigé au sens des portes**. Tant que la somme n'est pas écrite, les trois
volumes sources font foi (champ Statut du TOC), et une thèse de ce plan n'est pas une source (sa
propre décision 8). [`README.md`](README.md) est la **vue synoptique dérivée** du TOC (le « conspectus » du volume, même
version en tête) : il ne porte aucune décision, aucun socle, aucun garde-fou propre — en cas
d'écart, **le TOC prime**, et toute passe qui modifie le TOC réaligne le conspectus (version,
faits touchés) ou y déclare le retard en tête.

⚠ **Un livre entier existe pourtant dans le dossier, et il est hors portes — fait signalé ici, non
arbitré.** Le **27 juillet 2026, sur instruction d'auteur**, le répertoire [`Livre I/`](Livre%20I/) a
été créé et **ses onze chapitres** y ont été rédigés en deux rendus chacun (`.md` source, `.html` de
lecture à thème sombre), **avant** le franchissement des portes **G-1, G-2 et G-3** que le PRD §5
pose comme préalables à toute rédaction. Quatre choses à savoir avant d'y toucher.
*(a)* **Le statut de gouvernance n'a pas bougé** : chaque pièce se déclare elle-même *brouillon, non
publiable*, le socle consolidé reste à **0 entrée**, les sept portes restent ouvertes et les huit
décisions d'auteur **D-1 à D-8** restent à prendre. Un brouillon écrit hors portes ne franchit
aucune porte — il en documente le coût.
*(b)* **Ni le TOC, ni le PRD, ni le conspectus n'ont été touchés**, conformément à la règle
d'escalade du PRD (Annexe A) : *un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il
remonte.* Leurs champs Statut décrivent donc encore « zéro pièce rédigée », et **c'est correct au
sens où ils l'entendent** : zéro pièce **recevable**. Ne pas les « corriger » pour ces pièces.
*(c)* **Treize remontées sont ouvertes par cette rédaction — R-IV-01 à R-IV-13** —, portées par les
notes de statut hors plan de chaque pièce, à retirer à la publication. **Le tableau complet est au
[`README.md` de `Livre I/`](Livre%20I/README.md)** et n'est pas repris ici. Trois sont à connaître au
niveau du dossier : **R-IV-01**, *bloquante pour le ch. 6* — la décision **D-7** (risque 15, l'accord
sous défaillance) est due avant la rédaction du Livre I, et le ch. 6 a été rédigé quand même, en
déclarant cette seconde infraction ; **R-IV-05**, *bloquante pour cinq chapitres* — le socle IAM est
posé une seule fois au ch. 3 et ne se reconstruit pas, sans qu'aucun contrôle outillé ne vérifie
l'abstention ; **R-IV-12 et R-IV-13**, non bloquantes mais **de même classe et consécutives** — voir
ci-dessous.
*(d)* **Le `.html` est un rendu, jamais une seconde source** : toute correction se fait au `.md` et
se reporte au même commit. Le compendium n'a **pas** de pipeline de rendu — les trois copies du
FESP appartiennent aux Vol. I, II et III, et aucune n'a été copiée ici. Le rendu et ses huit
contrôles sont outillés par le skill (voir plus bas) ; ⚠ **le vérificateur ne se tuyaute jamais dans
un enchaînement `&&`**, le code de sortie du dernier maillon masquant son échec — faute déjà commise
sur le ch. 6, poussé avec un défaut de rendu alors que le contrôle échouait.

⚠ **Une classe de défaut propre à la somme s'est révélée en rédigeant les ch. 10 et 11, et elle est
consignée ici parce qu'elle vaut pour tout le compendium.** Dans les deux cas, une **lacune déclarée
du socle d'un volume** est **comblée par le texte rédigé d'un autre volume** — l'autre source de la
**même ligne Fusion**. *Ce ne sont pas des contradictions* : « le socle de A ne documente pas X » et
« B documente X » sont **logiquement compatibles**, et l'énoncé du volume le plus ancien **reste
exact dans son périmètre** — il ne se corrige pas après coup, sa lacune de couverture étant une
information datée. **Trois conséquences.** *(1)* Une pièce se rédige sur **l'intégralité de son
périmètre de fusion**, jamais sur la seule source que le plan met en avant — le ch. 7 a dû être
corrigé pour avoir manqué cette règle. *(2)* La **collation de fond (porte G-4)** devrait poser la
distinction *lacune de couverture / contradiction* **en règle**, et balayer systématiquement les
lacunes déclarées d'un volume contre le texte rédigé des deux autres. *(3)* **Aucun contrôle outillé
ne le fait aujourd'hui**, et le vérificateur du skill ne le fera pas — c'est un contrôle de fond, pas
de forme.

**Un skill de projet porte la procédure de rédaction.** Depuis le 27 juillet 2026,
[`.claude/skills/chapitre-compendium/`](../.claude/skills/chapitre-compendium/SKILL.md) tient la
marche à suivre pour rédiger une pièce : état des portes, quatre lectures préalables, squelette et
en-tête à cinq champs, conventions de renvoi et pièges datés, gabarit HTML commun aux pièces, et un
vérificateur validé par mutation (`scripts/verifier-piece.py`). Il **ne porte aucune décision** —
le TOC reste la spécification, le PRD la gouvernance ; il exécute, il n'arbitre pas. Le mettre à
jour quand une passe change une convention, plutôt que de laisser diverger la pratique et la règle.

⚠ **`audit.md` n'est pas un quatrième livrable.** C'est un rapport de couverture daté (24 juillet 2026), **sans autorité** : ni source, ni socle, ni décision. Ne jamais le citer à l'appui d'un énoncé ni s'en servir pour modifier le plan — ses constats retenus ont été portés là où ils font foi (risque 15 du TOC, décision D-7 du PRD, passe v0.15) ; ce qu'il porte encore n'a pas été retenu. Un audit ultérieur suit la même règle : il **remonte**, il ne tranche pas.

⚠ **Le TOC porte, depuis la v0.16 (25 juillet 2026), une table des matières détaillée par chapitre — et ces tables sont subordonnées.** Chaque entrée de chapitre est suivie du dépliage de ses sections et sous-sections, chacune portant sa **provenance** (`← Vol. N` *document* `§N.M`), plus une **table de couverture** par chapitre (décision 6). Les 57 entrées en sont pourvues, dérivées du **texte rédigé** des trois monographies. ⚠ **Une exception depuis la v0.22** : le **ch. 41** porte une table détaillée **sans aucun marqueur `←`** — matière neuve, il n'a pas de texte source à déplier, et l'absence de provenance y est rendue visible **par la forme**, pas seulement par une mention. ⚠ **Une table déplie une ligne Fusion, elle ne la re-décide pas** : en cas d'écart, **la ligne Fusion prime**, et quand le chapitre sera rédigé, c'est **lui** qui corrigera la table (décision 8). *Le travail a vécu dans un fichier séparé, `TOCAll.md`, renommé sur le TOC à sa complétion ; ce fichier n'existe plus, ses quatre commits restent à l'historique.*

⚠ **Condensation v0.20 (26 juillet 2026), sur instruction d'auteur : cinq livres, cinquante chapitres — et rien de soustrait.** Les dix livres sont devenus **cinq** (anciens I+II → I ; III → II ; IV+V+VI → III ; VII+VIII → IV ; IX+X → V) et les 57 chapitres **50**, par **sept fusions** : 12+13, 21+22, 23+24, 25+26, 41+42, 49+50, 55+56. ⚠ **Une fusion ne coupe pas** : chaque paire conserve ses **deux entrées intégralement**, en **deux mouvements** portant chacun son ancien titre et son ancien numéro — dispositif de la décision 10, étendu aux chapitres par la **décision 11**, où vit la correspondance complète. Invariants mesurés avant et après, tous égaux : 57 thèses, 58 lignes Fusion, 309 titres de section, 456 renvois de provenance. ⚠ **Trois numérotations coexistent désormais dans le fichier** — chapitres, sections et livres —, et deux conventions les départagent des renvois aux volumes sources : un renvoi source **colle sa section au § sans espace** (`ch. 21 §21.2`) là où le compendium **l'en sépare** (`ch. 44 § 44.1`), et il porte son marqueur de document. **Toute renumérotation future doit protéger ces deux formes** — la v0.22 l'a fait et l'a vérifié (voir plus bas) : la v0.20 a d'abord renuméroté treize renvois du Vol. II à tort — le marqueur suivait le numéro (« le ch. 20 du Vol. III »), cas qu'aucun masquage vers l'amont n'attrape. ⚠ **Les journaux et rangées d'historique, gelés, citent la numérotation de leur passe** : un « Livre IX » gelé désigne la matière neuve, aujourd'hui premier mouvement du Livre V ; un « ch. 57 » gelé désigne le ch. 50. **Ne jamais les corriger** — C4 et C13 exemptent pour cela les lignes à marqueur de correspondance.

⚠ **Insertion v0.22 (27 juillet 2026), sur instruction d'auteur : un chapitre neuf au Livre IV — et une seconde renumérotation à chaîner.** Le **ch. 41, « La fabrique d'agents : produire, certifier et réémettre le parc »**, entre comme **troisième mouvement du Livre IV** (*produire*), entre *exploiter* (ch. 38-40) et *composer* (ch. 42-46) : la somme décrivait le maillage qui **admet** les agents et l'AgentOps qui les **mesure**, et ne nommait nulle part le plan qui les **produit** (balayage mesuré de la zone des chapitres, zéro occurrence). ⚠ **Rien n'est soustrait ni réécrit** — les 57 entrées conservées en mouvements le restent —, mais **les ch. 41-50 deviennent 42-51** (décision 12). Quatre points à connaître avant d'éditer. **(a) Les correspondances se chaînent, elles ne se réécrivent pas** : la carte de la décision 11 se lit en numérotation v0.21, celle de la décision 12 par-dessus — un « ch. 57 » gelé désigne le ch. 50 de la v0.21, donc le **ch. 51** courant. **(b) Le ch. 41 est de la matière neuve dans un livre qui a un socle** : « Fusion : aucune », thèse en construction d'auteur, table détaillée **sans marqueur `←`**, table de couverture remplacée par une table d'appuis — régime de la décision 9 étendu hors du Livre V, et **risque 16** ouvert avec son issue de retrait. **(c) Un garde-fou de désambiguïsation est ouvert (décision 12c)** : « fabrique » désigne quatre objets, dont **deux vivent déjà dans ce fichier** — la fabrique d'identité du ch. 43 § 43.1 et la fabrique d'agents du ch. 41 ; ne jamais employer le mot sans que le sens soit déterminable de la phrase. **(d) Le ch. 41 ne comble ni le risque 14 ni le risque 15** : produire n'est pas exécuter, le harnais reste sans chapitre, et **D-7 comme D-8 restent ouvertes**. ⚠ **Le défaut de la passe est consigné plutôt que tu** : le remappage ne voyait que la borne gauche des intervalles de sections et a produit **14 formes fautives** du genre `§ 51.1-50.3`, qu'**aucun des quatorze contrôles ne signale** — seule la relecture du diff les a montrées. **Toute renumérotation future relit son diff ligne à ligne** ; le script ne le fera pas à sa place.

⚠ **Plafond v0.23 (27 juillet 2026), sur instruction d'auteur : la fusion qui paie l'insertion de la v0.22.** Le plan étant passé à 51 chapitres, la règle du plafond (section ci-dessous) est posée et **payée dans la même passe** : les **ch. 47 et 48 de la v0.22** — provenance des composants ; mise en service d'un artefact non reproductible — sont fusionnés en **ch. 47, « L'artefact livré »**, et les **ch. 49-51 deviennent 48-50** (décision 13d). ⚠ **Trois choses à savoir avant d'éditer.** **(a) Les trois fronts de l'audit v0.3 restent trois** : deux mouvements au ch. 47, un chapitre au ch. 48 — la fusion supprime un en-tête, jamais une matière. **(b) Les sections du second mouvement sont passées de § 48.1-48.5 à § 47.8-47.12**, à la suite de celles du premier : tout renvoi entrant « ch. 48 § 48.x » se lit désormais « ch. 47 § 47.(x+7) ». **(c) La paire n'a pas été choisie à l'estime** : c'est la seule du plan dont la fusion ne touche **aucun** renvoi de provenance (les deux chapitres n'en portent pas), et le critère est écrit en décision 13c pour la prochaine fois. ⚠ **Le défaut propre de cette passe est le plus silencieux rencontré jusqu'ici, et il est consigné** : le remappage avait **réécrit trois correspondances gelées** — la carte de la décision 12b et la rangée Version de la v0.22, qui se cite verbatim en descendant à l'historique. Une carte réécrite **reste cohérente à la lecture** et fait résoudre les renvois gelés au mauvais chapitre. Restaurées ; règle en décision 13d. **Trois passes de structure consécutives ont vu leur défaut échapper au script (v0.18, v0.22, v0.23) : une passe de structure se relit ligne à ligne.**

⚠ **Depuis la v0.18 (26 juillet 2026), ces tables sont en titres markdown, et la hiérarchie de niveaux fait convention.** `## LIVRE N` → `### Chapitre N` → `#### § N.M` : les sections sont les **enfants directs** du chapitre, ce qui expose le plan complet du fichier dans tout afficheur de plan (éditeur, forge, table des matières Pandoc). Trois corollaires, qu'une passe ultérieure ne doit pas « corriger » en croyant réparer une anomalie : **(a)** « Table des matières détaillée du chapitre N » et « Table de couverture (décision 6) » sont des **paragraphes gras, pas des titres** — les promouvoir en `####` les interposerait entre le chapitre et ses sections ; **(b)** les **sous-sections restent en listes**, délibérément — ce sont des phrases descriptives portant leur provenance, non des intitulés, et les promouvoir produirait un plan de plus de mille entrées, donc illisible ; **(c)** il n'y a **aucun index de tête**, et il n'en faut pas — un index serait un cardinal de plus à tenir à jour (risque 1) là où les titres se dérivent d'eux-mêmes. ⚠ **Et le point qui compte le plus : `check-toc.py` ne voit rien de cette forme.** Ses quatorze contrôles portent sur des motifs de ligne (titre de chapitre, titre de livre, rangées du bandeau, enveloppes de tête, registre des lacunes) ; aucun ne connaît les tables détaillées. Un reformatage passe donc **sans être validé par l'appareil versionné**, et le seul contrôle qui en prouve la fidélité est la comparaison du **flux de mots** avant/après (v0.18 : 72 764 mots, séquence identique) — à refaire, et à déclarer au journal, à toute passe qui touche à la forme.

⚠ **Les ch. 47-48 (Livre V) et le ch. 41 (Livre IV) n'ont aucune table de provenance, et c'est un fait, non un manque.** Matière neuve, « Fusion : aucune » (décision 9) : aucun renvoi `←` n'y est possible, les seuls appuis sont **internes** (chapitres de la somme) et tout énoncé y est au mieux un **repérage [C] à instruire**. La décision 6 (couverture tracée) y est sans objet ; la **décision 8 s'y applique doublement**.

⚠ **Ajouter du contenu à un chapitre peut périmer un identifiant qu'on n'a pas touché** — leçon de la v0.16, et le piège le plus contre-intuitif de ce fichier. Le ch. 32 ne consommait que le Vol. II : son garde-fou « R-5 » nu était décidable. La table détaillée y a introduit une mention de l'**échelle R-14 du Vol. III**, ce qui en a fait un **chapitre mixte** et rendu ce « R-5 » indécidable (C8). Le défaut n'était pas dans la ligne ancienne mais dans son **voisinage neuf**, et seule l'exécution de `check-toc.py` l'a montré — la relecture ne l'attrape pas. Même classe au ch. 43 (« R-8 »). **Exécuter le contrôle après toute addition, même quand on n'a rien retiré ni renuméroté.**

⚠ **Convention de renvoi (décision 7), appliquée par les tables détaillées** : le Vol. III vit en numérotation multiple, et **ses chapitres sont désormais rédigés** — un renvoi au texte s'y écrit `Vol. III `*Monographie*` §N.M`, un renvoi au plan `Vol. III `*TOC*` §N.x`. ⚠ Le **TOC du Vol. III n'a pas de titres `§N.M`** : il nomme ses sections en prose sous des `### Chapitre N`, comme celui du compendium — un renvoi « Vol. III *TOC* §N.M » ne s'y vérifie donc pas par titre, et c'est contre la *Monographie* rédigée qu'il résout, à numérotation et titre concordants (constat de la collation v0.14, re-vérifié le 25 juillet 2026 sur les sept renvois de ce domaine).

⚠ **Un « PRDPlan §N » nu est indécidable entre deux documents** — collision relevée au balayage du 25 juillet 2026, de la classe même que la décision 7 proscrit (« un R-7 nu est indécidable »). Le TOC emploie la forme nue pour **deux** PRDPlan : §4.2 et §4.4 désignent celui du **Vol. II** (formulations types, boucle qualité), §1.5 et §5.3 celui du **Vol. III** (commande de décompte, règle d'escalade). Le contexte tranche à la lecture, jamais le renvoi. **L'occurrence en zone normative est nommée depuis la v0.17** (`PRDPlan Vol. II §4.4`, ch. 25) ; celles de l'avant-propos et des journaux gelés gardent leur forme d'origine. **Nommer le volume à toute occurrence neuve.**

⚠ **Les treize écarts relevés par la v0.16 sont soldés par la v0.17** — chacun par une règle que le plan porte déjà (décisions 2, 6, 7 et 8), **jamais par un choix de contenu neuf**. Détail au journal v0.17 du TOC. Trois d'entre eux valent d'être connus avant d'éditer :

- **Une source vide, corrigée par la décision 8.** Le « volet RGPD » que les ch. 27 et 30 se partageaient n'existe plus : le Vol. III rédigé l'a retiré de son ch. 20 le 22 juillet 2026 (arbitrage **R-G-38**), son socle ne documentant « ni le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation*, degré 3, **non** fait négatif vérifié. Le ch. 27 reçoit ce chapitre **en entier**, le ch. 30 garde sa matière RGPD par le **Vol. I** (§4.8.4, §5.3). ⚠ **La lacune 16 du Vol. III est entrée au registre de l'Annexe C, dans une SECONDE table** : les lacunes du Vol. III forment une série distincte des onze du Vol. II, et les fondre périmerait un cardinal contrôlé. **Cette seconde table se déclare incomplète** — une entrée, non un inventaire ; le dresser est un préalable de la collation de fond (porte G-4).
- **Une classe de double revendication qu'aucun contrôle n'attrape.** Quand une ligne Fusion absorbe un **intervalle de chapitres** (« Vol. III ch. 5-7 ») pendant qu'un autre chapitre en prélève **une section** nommée (« §7.4 »), les deux renvois sont valides isolément et vivent à des grains différents : `check-toc.py` ne les rapproche pas. **Collation manuelle, à refaire à chaque révision d'une ligne Fusion citant un intervalle.**
- **Une arrivée se déclare aux deux bouts.** Le §2.8.5 du Vol. I était déclaré à son *départ* (ch. 6) et nulle part à son *arrivée* (ch. 4) : un chapitre rédigé sur sa seule liste de sections aurait perdu la section que la v0.5 avait sauvée.

⚠ **Ce que la v0.17 n'a pas touché, et qu'une passe de cohérence ne doit jamais toucher** : les **risques 13, 14, 15 et 16** (Livre V sans socle, couche d'exécution sans chapitre, accord entre agents sous défaillance, et — depuis la v0.22 — un chapitre sans socle dans un livre qui en a un) portent sur du **contenu manquant**, non sur une incohérence — leur arbitrage est une décision d'auteur (**D-7** du PRD). De même la thèse forte du ch. 19, à instruire par dénombrement.

## ⚠ Plafond dur : cinquante chapitres, jamais plus

**Règle d'auteur du 27 juillet 2026, sans exception.** Le compendium compte **au plus cinquante
chapitres** — avant-propos et annexes non comptés. Ce n'est pas une cible mais une **borne** : elle
prime sur l'opportunité éditoriale d'un chapitre neuf, et **un plan qui la dépasse n'est pas
publiable**. La règle est posée en **décision 13** du TOC et **appliquée par `check-toc.py`,
contrôle C15** — une règle de plan sans motif exécutable qui la contrôle n'en est pas une (même
doctrine que pour les cardinaux, et que pour `check-veille.py` à la racine).

**Protocole d'insertion, à suivre dans l'ordre.** Ajouter un chapitre reste possible ; le faire
sans payer ne l'est pas.

1. **Vérifier le plafond avant d'écrire quoi que ce soit** : le plan est plein (50/50). Toute
   insertion est donc **conditionnée** à une fusion.
2. **Choisir la paire à fusionner par le critère de la décision 13c**, dans cet ordre : deux
   chapitres **adjacents**, du **même mouvement**, de **même régime de preuve**, sous la même porte
   et la même décision d'auteur ; à égalité, celle dont la fusion touche le **moins de renvois de
   provenance `←`**. Le motif du choix **s'écrit au journal** — une fusion non motivée est
   indiscernable d'une coupe arbitraire.
3. **Fusionner sans rien soustraire** (règle 11a, reconduite) : les deux entrées sont conservées
   **intégralement**, en **deux mouvements** portant chacun son ancien titre et son ancien numéro ;
   les sections du second mouvement se renumérotent **à la suite** de celles du premier.
4. **Insertion et fusion dans la même passe.** Ne jamais laisser la dette à une passe ultérieure :
   elle aurait à choisir sous contrainte ce que la passe fautive a choisi librement.
5. **Enveloppes** : une fusion ne retire rien, donc **aucune enveloppe ne bouge** ; seul le
   chapitre neuf en ajoute une. Ne pas « compenser » un ajout de mots par une fusion — les deux
   gestes sont indépendants (décision 13b).
6. **Exécuter `python PRD/check-toc.py`** : **C15** refuse le dépassement, **C1** la discontinuité.

⚠ **Ce que le plafond n'autorise pas : retirer un chapitre pour faire de la place.** Une somme qui
perd de la matière pour tenir un décompte a échangé un défaut visible — un chapitre de trop —
contre un défaut invisible — une matière disparue. C'est exactement ce que la condensation v0.20
s'était interdit, et le plafond ne rouvre pas cette porte.

⚠ **Et le plafond ne vaut pas dispense d'arbitrage.** Les risques 14, 15 et 16 nomment des objets
que la somme ne traite pas ou traite sans socle ; le plafond **ne les tranche pas** — il rend
seulement explicite le coût de les combler par un chapitre. L'arbitrage reste une décision
d'auteur (D-7, D-8 du PRD).

## L'appareil interne du TOC fait loi

Le TOC porte ses propres règles de gouvernance ; les lire avant d'éditer, ne pas les réinventer :

- **Décision 7** — tout renvoi nomme son document (*Monographie*/*Synthèse*/*PRD*/*TOC*), sa série
  (deux séries « Q n » au Vol. II) et son volume (R-1…R-8 du Vol. II ≠ R-01…R-14 du Vol. III).
- **Décision 8** — le plan s'aligne sur le chapitre rédigé, jamais l'inverse ; une déviation fondée
  se déclare.
- **Décisions 11, 12 et 13 (v0.20, v0.22, v0.23)** — les trois cartes de renumérotation **se chaînent et ne se
  réécrivent jamais** : un « ch. 57 » gelé désigne le ch. 50 de la v0.21, le ch. 51 de la v0.22, le **ch. 50**
  courant. La **13a** pose le plafond de cinquante chapitres, la **13b** que toute insertion se paie par une
  fusion dans la même passe, la **13c** le critère de choix de la paire, la **13d** qu'un remappage ne touche
  jamais une carte de correspondance ni une rangée qui se cite verbatim.
- **Décisions 9 et 10 (v0.8-v0.9)** — la matière neuve se déclare (Livre IX : « Fusion : aucune »,
  thèses marquées construction d'auteur) ; **le second mouvement du Livre V (clôture) reste terminal** — toute
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
- ⚠ **Cardinaux multi-sites** : tout décompte annoncé (50 chapitres, cinq livres, enveloppes,
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
  ouvrira le Livre II ou le Livre IV (l'ADS Boréalis y siège, annexe H).
- ⚠ **Corpus d'appui du Vol. III : filiation retirée** (P0.2 tranchée le 21 juillet 2026, L-15
  close par échec documenté — **réversible** par dépôt ultérieur) : les mentions « corpus
  d'appui » des chapitres consommateurs sont des marqueurs conditionnels de réouverture, jamais
  des sources ; aucun chapitre ne se rédige en s'appuyant sur ces ouvrages sans dépôt effectif.
- ⚠ **Le Vol. III est rédigé depuis le 22 juillet 2026** (34 pièces, socle F-01…F-98 + H-01…H-33,
  PRD v1.3 / TOC v0.8), mais « **rédigé ne vaut pas publiable** » : remontées ouvertes, arbitrages
  révocables, dette de vote (F-92, F-96 du Vol. III). La collation de fond contre son texte rédigé
  (l'homologue de la v0.6) est un **préalable déclaré** aux Livres II et IV, **dont la v0.14 du TOC
  a levé le volet structurel** (couverture complète et résolution des renvois de section, zéro écart —
  seul le volet de fond reste dû) ; et un « F-xx » nu
  est désormais **indécidable entre deux socles** — convention transitoire en décision 7 du TOC.
- ⚠ **Relèves v0.7, v0.10, v0.11 et v0.19** : marquées « à instruire à la source primaire » — aucune
  n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune sans extraction de la
  source primaire. Les relèves v0.11 (l'après-agentique) citent des préimpressions arXiv dont
  seuls les résumés ont été consultés : repérages [C], jamais des faits. ⚠ **Les huit relèves
  v0.19** (couverture en science et génie informatique — ch. 6, 17, 19, 24, 37 et 47 depuis la
  fusion v0.23, qui a réuni sur ce dernier deux chapitres marqués : **six chapitres, huit relèves**) citent
  au contraire des **documents normatifs et des articles de revue consultés à leur source**
  (RFC 8693 et 9334, SLSA v1.2, in-toto, CycloneDX 1.7 / ECMA-424, SPDX 3.0, NIST SP 800-218A,
  NIST AI 100-2 E2025, OPA/Rego, FLP, Gilbert-Lynch, Castro-Liskov, Dean-Barroso, test
  métamorphique). **Le régime ne change pas pour autant** : un document lu à la source reste une
  **relève**, jamais une entrée de socle — la refonte du socle est la porte G-3 du PRD, pas le
  produit d'une passe de plan. ⚠ **Trois réserves de relevé sont portées dans le texte** (date
  d'approbation de SLSA v1.2, version de SPDX que fixe l'ISO/IEC 5962:2021, DOI de Castro-Liskov) :
  ne pas les « compléter » de mémoire — ce qui n'a pas été vu à la source ne s'écrit pas comme vu.
  ⚠ **Ces marques sont contrôlées depuis la v0.21** : C11 couvre les listes v0.10, v0.11 et v0.19,
  inscrites dans le script et validées par mutation (M11c, M11d) — la dette d'appareil que le
  journal v0.19 déclarait est payée.
- ⚠ **L'angle mort du harnais est déclaré, non comblé** (risque 14, v0.10) : la couche d'exécution
  n'a de chapitre nulle part, et trois des huit relèves v0.10 atterrissent dans le Livre V. **Ne
  pas en tirer un chapitre ni un livre** — la somme porte déjà un livre sans socle (risque 13), et
  l'arbitrage est une décision d'auteur, pas une décision de passe.

## Éditer le TOC — protocole de passe

1. Toute passe = **nouvelle version** : nouvelle rangée Version au bandeau (l'ancienne descend en
   rangée Historique, verbatim), champ Date mis à jour, **journal daté ajouté en fin de fichier**.
   Les journaux sont en ajout seul — un journal publié ne se réécrit pas, ses écarts se consignent
   dans la passe suivante.
2. **Contrôles** : `python PRD/check-toc.py` (versionné dans `PRD/` depuis la v0.12 du 23 juillet
   2026 — contrôles **C1-C15** depuis la v0.23, domaine : chapitres 1-50, cinq livres depuis la v0.20 ;
   **C15 est le plafond dur** de la décision 13a) **avant toute publication** ;
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
