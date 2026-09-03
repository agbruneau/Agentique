# Agentique

**Un corpus de recherche** : Huit documents en français — **2 922 pages rendues**
sur neuf PDF — instruisent une seule question : *comment une entreprise de services financiers
canadienne déploie, gouverne et exploite des agents d'IA autonomes sous contrainte réglementaire ?*
⚠ *Cette page a longtemps écrit « 2 921 » : le compte datait du 21 août 2026 et n'avait pas suivi la
recomposition du 24, qui porte l'état de l'art de 185 à 186 p.*
☑ **Un neuvième document est entré le 28 août 2026** — la
[note de veille SDLC](<4%20-%20Veille/Note-veille-SDLC-agentique.md>), **49 p.**, qui porte le dépôt
à **2 971 pages sur dix PDF** —, ⚠ **et il n'est pas rangé parmi les livrables** : *lecture critique
d'une source unique — un entretien de 4 h 26 —, bibliographie non appariée, aucun contrôle qui
l'oppose à elle-même.* Le motif est donné au [`README` de `4 - Veille/`](<4%20-%20Veille/README.md>),
qui la range comme **document publié et non comme neuvième livrable** — ⚠ *ce n'est pas une
instruction d'auteur, le PRD ne porte aucune décision sur ce document, et le compte se renverse d'un
mot de sa part, comme le huitième.*
☑ **Un dixième document est entré le 1er septembre 2026**, au commit `da6255b`, dans un
**sixième dossier numéroté** — [`6 - Article/`](<6%20-%20Article/>) : *Projection de l'état de
ressource et délégation multicritère dans une plateforme HPC à processeurs quantiques*, **38 p.**,
une prépublication au gabarit arXiv qui porte le dépôt à **3 009 pages sur onze PDF**.
⚠⚠ **Lui non plus n'est pas rangé parmi les livrables, et son motif est neuf : il n'instruit pas la
question ci-dessus.** *Le corpus porte sur l'entreprise agentique en services financiers ; celui-ci
porte sur l'intégration de processeurs quantiques dans une plateforme de calcul haute performance.*
La note de veille SDLC est tenue hors des huit pour **ce qui lui manque** ; celui-ci l'est pour
**ce dont il traite** — *et ce que la note n'a pas, l'article l'a* : bibliographie close dans les
deux sens — **77 entrées, 77 citées** — et **un contrôle qui l'oppose à lui-même**,
[`rejeu-politique.py`](<6%20-%20Article/rejeu-politique.py>), ☑ **0**, seul contrôle du dépôt qui
**exécute une condition de réfutation** d'un document au lieu de mesurer sa forme. ☑ *Le voisinage
avec le corpus est déclaré par l'article lui-même* : son § 2.8 fait de l'agent scientifique autonome
le consommateur le plus exigeant de la chaîne qu'il spécifie. Le motif complet est au
[`README` de `6 - Article/`](<6%20-%20Article/README.md>) — ⚠ *et, comme les deux précédents,
ce n'est pas une instruction d'auteur : le PRD ne porte aucune décision sur ce document.*
S'y ajoute **un simulateur en Rust** — 76 fichiers, 29 690 lignes — qui transpose l'un de ces
documents en code exécutable sous une règle : *tout chiffre affiché doit être retrouvé par la
mesure, ou l'écart consigné*. **Cinq écarts** le sont, **dont trois contredisent le traité**
([`3 - Traité/docs/decisions.md`](<3%20-%20Trait%C3%A9/docs/decisions.md>)) — *et c'est la règle qui
tient, non un défaut : un écart consigné est ce que le dispositif produit quand il marche.*

**Les textes sont d'une seule main** : André-Guy Bruneau, champ `/Author` des onze PDF signés —
⚠ *la mention « M.Sc. IT » n'accompagne le nom que sur sept ; les Vol. I, II et III le portent seul.*
⚠⚠ **Et le onzième l'écrit autrement** : l'article de `6 - Article/` porte `André-Guy Bruneau,
M.Sc IT`, **sans le point après « Sc »** — *huitième PDF à porter la mention, seul des huit à
l'écrire ainsi.* **Relevé le 1er septembre 2026, non corrigé** — la correction tient en un point à
la source et demande une recomposition.
⚠ *Le dépôt, lui, ne l'est pas* : `git log` comptait, **au relevé du 21 août 2026 et avant
la passe de réparation que décrit cette page**, **280 commits — 260 signés André-Guy
Bruneau, 18 `Claude <noreply@anthropic.com>`, 2 `agbruneau`** — et **quatre fusions de *pull
requests* GitHub** ; deux branches `origin/claude/*` subsistent au distant. *La numérotation GitHub
monte à #5, mais une PR ne se compte pas par son numéro : la #4 n'a laissé aucune trace au dépôt, ni
fusion ni écrasement.* **Historique du 24 juin au 28 août 2026**, bornes du premier et du dernier
commit — **305 commits au 28 août**, dont onze pris depuis le 24. ⚠ *Au 24 août,
`git rev-list --count` en rend **294** et non les 293 que cette page écrivait.*

⚠ **Le dépôt est déclaré clos et final, et sa clôture est portée au 1er septembre 2026** — décision
d'auteur **D-13**, prise le 8 août 2026,
[`2 - Compendium/PRD/PRD.md`](<2%20-%20Compendium/PRD/PRD.md>) §16 ; l'unique étiquette du dépôt,
`mono-v1.0`, est posée sur le commit du 8 août — *celui de la prise, non de l'état arrêté*.
Il a été rouvert une dizaine de fois depuis le 8 août 2026, chaque
fois pour une pièce nommée et pour elle seule : la chronique datée est en tête de
[`1 - Collection/README.md`](<1%20-%20Collection/README.md>) — ⚠ *qui s'arrête à la onzième
réouverture, celle du 21 août 2026, et ne porte aucune des passes du 22 août au 1er septembre : la
compter là revient à compter court.* **La dernière réouverture est du 1er septembre 2026, pour
l'article de `6 - Article/`** — ⚠ *c'est la deuxième d'affilée qui fasse entrer un document neuf
plutôt que réparer une pièce existante, la première étant celle du 28 août, et la première depuis le
20 août 2026 qui crée un dossier numéroté.* ⚠ **Une passe l'a suivie le 2 septembre 2026** — l'audit
et le fond du seul Vol. IV (D-15, D-16) —, *mais elle ne fait entrer aucune pièce : la dernière
entrée reste celle du 1er septembre.*

⚠ **Cette page a écrit « clos et final depuis le 8 août 2026 » jusqu'au 3 septembre 2026, et elle
confondait deux dates** : *une décision se date de sa prise, une clôture de l'état qu'elle arrête.*
**D-13 reste prise le 8 août 2026 ; la clôture, elle, est portée au 1er septembre 2026** — dernier
jour où une pièce est entrée au dépôt, l'article de [`6 - Article/`](<6%20-%20Article/>), commit
`da6255b`. ⚠ *La passe d'audit et de fond du 2 septembre 2026 (D-15, D-16) lui est postérieure d'un
jour et ne la redate pas : elle porte sur l'appareil, le plan et le domaine de livraison du Vol. IV,
et **aucune pièce n'y entre ni n'en sort** — le critère se lit sur l'entrée d'une pièce, non sur la
dernière passe.* Le motif complet est au
[PRD §16.5](<2%20-%20Compendium/PRD/PRD.md>) ; ⚠ **la redatation ne rouvre rien** : aucune porte
franchie, aucun manque définitif redevenu dette, aucun régime touché.

☑ **[`LICENSE`](LICENSE) à la racine — CC BY 4.0, posée le 21 août 2026 sur instruction d'auteur**,
et elle couvre le dépôt entier : les huit documents, leurs rendus, le simulateur, les chaînes et les
figures — *et, sans qu'un geste soit nécessaire, les deux documents entrés depuis, la note de veille
SDLC et l'article.* *Jusque-là, seul le Vol. I portait la sienne — mêmes termes, pour lui seul — et tout le
reste relevait du droit d'auteur par défaut.* ⚠ **Ce qu'elle ne couvre pas est écrit dans son texte** :
les œuvres de tiers citées, qui restent à leurs titulaires. **Trois ouvrages de tiers et deux articles
arXiv ont quitté l'index le même jour**, *avant* qu'elle ne soit posée et précisément parce qu'elle
n'aurait pas pu les couvrir — ni détruits ni perdus alors, *le disque et l'historique git les
gardant tous deux*. ⚠⚠ **Les cinq copies au disque ont été effacées le 25 août 2026, sur
instruction d'auteur** : **l'historique git est désormais la seule copie**, et c'est par lui seul
qu'elles se relisent — *sortir de l'index n'était pas détruire ; effacer le disque ne l'est pas
davantage, tant que l'arbre ancien tient*. Leurs renvois sont au
[`README` de `0 - Références/`](<1%20-%20Collection/0%20-%20R%C3%A9f%C3%A9rences/README.md>).

## Par où entrer, selon le temps qu'on a

| Temps                 | Ouvrir                                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **5 minutes**   | *Cinq schémas — état de l'art* : [`.pdf`](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.pdf>) 7 p. ou [`.html`](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.html>) 105 Ko autonome — cinq figures commentées et rien d'autre |
| **20 minutes**  | [`NiveauMaturité.html`](NiveauMaturit%C3%A9.html) — **9 diapositives** 16:9, six paliers de maturité ; autonome, aucune dépendance                                                                                                                                                                                                                     |
| **une demi-heure** | [`article-hpc-qpu.pdf`](<6%20-%20Article/article-hpc-qpu.pdf>) — 38 p. : une prépublication arXiv, 77 références toutes citées, 8 planches et 20 tableaux, 8 conditions de réfutation. ⚠ *Hors livrables, et hors sujet du corpus — voir plus haut* |
| **une heure**   | [`Note-veille-SDLC-agentique.pdf`](<4%20-%20Veille/Note-veille-SDLC-agentique.pdf>) — 49 p. : une source unique instruite, 18 thèses horodatées, 40 affirmations triangulées. ⚠ *Hors livrables — voir plus haut*                                                                                                             |
| **une soirée** | [`Veille Technologique.pdf`](<4%20-%20Veille/Veille%20Technologique.pdf>) — 144 p., l'état du champ déployé, 342 références                                                                                                                                                                                                                                |
| **le fond**     | [`Compendium.pdf`](<2%20-%20Compendium/Compendium.pdf>) — 1 000 pages, la somme dédoublonnée des trois monographies                                                                                                                                                                                                                                           |
| **du code**     | [`3 - Traité/`](<3%20-%20Trait%C3%A9/>) — le simulateur d'essaims : quatre *crates* et deux bancs, ☑ **467 `#[test]` au vert, clippy 0**                                                                                                                                                                                                              |

## Les huit documents

| #              | Document et dossier                                                                                                                                                                       | Ce qu'il soutient                                                                                                                                                                                                                                                                                                                              | Rendu                                                                                                                    | Source                                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **I**    | *Interopérabilité agentique en entreprise dans le domaine des services financiers*[`1 - Collection/1 - InteroperabiliteAgentique/`](<1%20-%20Collection/1%20-%20InteroperabiliteAgentique/>) | Autonomie**graduée** sous contrôle de finalité. Portée mondiale (UE, É.-U., R.-U., Asie)                                                                                                                                                                                                                                            | **569 p.**                                                                                                         | 7 257 l. / 1,74 Mo · 7 chapitres + Annexe B ·**28 diagrammes Mermaid** · 7 bibliographies            |
| **II**   | *Orchestration agentique*[`1 - Collection/2 - OrchestrationAgentique/`](<1%20-%20Collection/2%20-%20OrchestrationAgentique/>)                                                                  | Autonomie**encadrée** (*framed autonomy*). Portée Canada-Québec. Résultat négatif : quinze croisements protocole × texte canadien, **zéro lien documenté**                                                                                                                                                               | **387 p.**                                                                                                         | 3 306 l. / 0,87 Mo ·**29 pièces** assemblées · socle factuel de **46 entrées**, F-01 à F-48 |
| **III**  | *L'entreprise agentique — la fabrique de confiance*[`1 - Collection/3 - EntrepriseAgentique/`](<1%20-%20Collection/3%20-%20EntrepriseAgentique/>)                                             | La confiance ne se décrète pas, elle se fabrique : émettre une identité, l'appliquer, l'exploiter                                                                                                                                                                                                                                          | **427 p.**                                                                                                         | 3 275 l. / 1,12 Mo ·**34 pièces** · socle propre de **98 entrées**, F-01 à F-98              |
| **IV**   | *Conspectus — Interopérabilité et Orchestration **en Entreprise Agentique***[`2 - Compendium/`](<2%20-%20Compendium/>)                                                       | La somme des trois volumes, dédoublonnée et re-datée à la source                                                                                                                                                                                                                                                                           | **1 000 p. exactement** ⚠ *cible d'auteur vérifiée par le script de rendu, qui échoue à 999 comme à 1 001* | **50 chapitres**, 5 Livres, 2 annexes · **118 figures** · socle consolidé `S-001`…`S-159` |
| **V**    | *Traité sur les systèmes multiagents en essaim*[`3 - Traité/`](<3%20-%20Trait%C3%A9/>)                                                                                              | La coordination par le milieu : ce qu'un essaim gagne à**ne pas** s'accorder, et ce qu'il le paie                                                                                                                                                                                                                                       | **143 p.**                                                                                                         | 1 875 l. · 8 chapitres, 24 sections,**123 notices**, 19 figures, 72 110 mots                           |
| **VI**   | *Veille technologique en entreprise*[`4 - Veille/`](<4%20-%20Veille/>)                                                                                                            | Le non-déterminisme du modèle enfermé dans des étapes bornées, journalisées, compensables : «*l'agent d'entreprise fiable de 2026 est enveloppé* »                                                                                                                                                                                  | **144 p.**                                                                                                         | 1 932 l. · 94 sections, 24 tableaux,**342 références**, 25 questions ouvertes                        |
| **VII**  | *Revue de la littérature académique*[`4 - Veille/`](<4%20-%20Veille/>)                                                                                                          | ⚠ Un résultat**sur son propre corpus, pas sur le champ** : **145 pièces sur 189 — 77 % — ne présentent aucun signe de revue par les pairs à leur notice**, 12 seulement portant une attestation. *La revue interdit expressément d'en tirer une part du champ : « le lire comme une part du champ serait circulaire »* | **59 p.**                                                                                                          | 1 052 l. ·**192 références**, 8 tableaux                                                             |
| **VIII** | *État de l'art en services financiers*[`5 - Recension/`](<5%20-%20Recension/>)                                                                                                   | Le débat porte sur la pile protocolaire ; dans une coopérative régie,**la pile n'est pas ce qui décide**                                                                                                                                                                                                                             | **186 p.** + planche de **7 p.** (`.md`/`.pdf`/`.html`)                                                | 1 986 l. ·**15 sections** numérotées, **312 références** (1 à 312, sans trou), 5 figures    |

⚠ **Le chiffre « huit » est un constat, pas une décision d'auteur.** Le dépôt a longtemps compté
sept livrables ; le huitième — l'état de l'art — a été rangé parmi eux le 20 août 2026 par les
`README.md` du dépôt, sur motif écrit, et **le PRD ne porte aucune décision sur ce document**. Un
lecteur qui cite le compte doit dire à quelle date il le tire et d'où.
⚠⚠ **Et le même arbitrage s'est reposé le 28 août 2026, en sens inverse.** La note de veille SDLC
est publiée, signée, datée, rendue au gabarit de la maison et **elle ouvre sa propre source** — *le
motif exact qui avait fait passer le compte de sept à huit.* Ce qui la retient hors du tableau :
**une source unique, une bibliographie de trente entrées en puces qu'aucun renvoi du corps
n'apparie, et aucun contrôle qui la mesure** — hors
[`check-resume.py`](<4%20-%20Veille/Python/check-resume.py>), qui ne regarde que sa page de titre.
*Le tableau reste donc à huit lignes, et le dépôt porte neuf documents publiés.*
⚠⚠⚠ **Et l'arbitrage s'est reposé une troisième fois le 1er septembre 2026, sur un motif que les
deux précédents n'avaient pas eu à formuler.** L'article de `6 - Article/` a tout ce qui manquait à
la note — **bibliographie close dans les deux sens, 77 entrées et 77 citées**, et un contrôle
versionné qui l'oppose à lui-même. *Le critère méthodologique qui a fait passer le compte de sept à
huit, puis retenu la note hors du tableau, le rangerait donc parmi les livrables.* **Ce qui l'en
tient dehors est autre chose : il n'instruit pas la question du dépôt** — il porte sur
l'intégration de processeurs quantiques dans une plateforme HPC, non sur les agents autonomes en
services financiers sous contrainte réglementaire. ⚠ *Un critère thématique n'avait jamais servi
ici, et il ne se déduit d'aucun des deux arbitrages antérieurs : c'est cette page qui le pose, sur
pièce, et le PRD ne porte aucune décision sur ce document.*
*Le tableau reste à huit lignes, et le dépôt porte **dix documents publiés**.*

☑ **Trois documents portaient exactement le même titre ; ils ne le portent plus depuis le
21 août 2026.** La veille, la revue et l'état de l'art déclaraient tous
`title: "Interopérabilité et Orchestration Agentiques"`, et **seul le sous-titre les séparait** —
c'était la confusion la plus facile à faire ici, et elle allait jusqu'au champ `/Title` des trois
PDF, identique aux trois. *La correction n'invente aucun mot : les deux champs sont **échangés**.*
Le discriminant devient le titre — « Veille technologique en entreprise », « Revue de la littérature
académique », « État de l'art en services financiers » — et le nom commun devient le sous-titre, ce
qu'il est en fait : **un nom de série**. Les trois PDF ont été recomposés le même jour par les
chaînes versionnées ce jour-là, **à pagination inchangée** — 144, 59 et 185 pages. *Les six PDF de
tête portent désormais six `/Title` distincts.* ⚠ **Une apostrophe est tombée à la composition du
troisième** : son `/Title` lit `État de lart en services financiers`, quand sa source YAML écrit bien
« État de l'art en services financiers ». *Le titre cité ci-dessus est celui de la source ; le PDF
livré ne le porte pas. Relevé le 22 août 2026, non corrigé — la correction demande une
recomposition.* ⚠⚠ **Et la recomposition ne suffit pas** : l'état de l'art a été recomposé le
**24 août 2026** par sa chaîne versionnée, et son `dc:title` lit toujours
`État de lart en services financiers`. ☑ **La cause a été isolée le 28 août 2026, en rendant la note
de veille SDLC** : elle est dans le **bloc de réglage commun lui-même**. La fonction
`content-to-string` du gabarit Pandoc — *seule voie par où le titre atteint `/Title` quand le bloc
redéfinit `conf`* — ne connaît que `text`, `children` et `body`, et **rend vide sur une apostrophe,
que Typst compose en `smartquote`**. ⚠ *La passe du 17 août 2026, qui a introduit ce `conf` pour
réparer le bloc de titre, a donc cassé ce champ du même geste — et celle du 21, qui portait
précisément sur `/Title`, ne l'a pas vu.* ⚠ *Poser l'apostrophe typographique à la source n'y change
rien, vérifié : Pandoc la relit et réémet le signe droit.* ☑ **Corrigé au seul en-tête de la note**,
dont le `dc:title` porte bien `à l'ère des agents` ; ⚠⚠ **l'état de l'art reste cassé** — *seul des
douze PDF du dépôt, relevé le 1er septembre 2026, et la correction demande une recomposition.*
☑☑ **Le diagnostic a reçu sa corroboration la plus nette le 1er septembre 2026, et par un document
qui ne visait pas cela** : l'article de `6 - Article/` porte un titre à apostrophe — *Projection de
l'état de ressource…* — et **son `dc:title` la traverse intacte**. *C'est le seul PDF du dépôt
composé **sans Pandoc**, en Typst direct : la variable qui distingue son cas de celui de l'état de
l'art est exactement celle que le diagnostic accuse.*
☑ *Cette même recomposition porte le document à **186 p.**
et **1 986 l.** — un paragraphe ajouté au §14, qui déclare la portée exclue par ligne d'affaires ;
les « 185 pages » du paragraphe ci-dessus datent le 21 août et ne bougent pas.*

☑ **Le Vol. IV a été renommé une seconde fois le 25 août 2026**, au commit `8b25090` (« Révision
des titres ») : *« Interopérabilité et Orchestration Agentiques en Entreprise »* — son titre du
8 au 25 août — devient **« Interopérabilité et Orchestration en Entreprise Agentique »**. *Aucun
mot n'entre ni ne sort ; l'adjectif change de siège, d'objet et de nombre : il qualifiait le couple
« interopérabilité et orchestration », il qualifie désormais l'entreprise.* ☑ `Compendium.pdf` a
été recomposé le même jour et son `dc:title` porte le titre neuf, **à pagination inchangée** —
1 000 p., 13 162 484 octets contre 13 163 513. ☑ **La passe est datée au PRD et au TOC** — **D-14**
([PRD](<2%20-%20Compendium/PRD/PRD.md>) **v0.18** §17) et **décision 21**
([TOC](<2%20-%20Compendium/PRD/TOC.md>) **v0.34**), toutes deux du 25 août 2026 ; ⚠ *elles ont été
prises **après** leur exécution* : le titre neuf était entré en place au commit `8b25090`, jusque
dans le libellé de la **décision 20**, qui s'est mise à énoncer un titre que l'instruction du
8 août n'avait pas donné. ☑ *Son libellé d'alors y est rétabli, et la clôture du dépôt est rouverte
pour le titre seul, dans les termes que le PRD §16.4.5 exige.*
☑ *Ce que la révision règle par ricochet* : le titre du Vol. IV n'est plus le radical de série que
la veille, la revue et l'état de l'art portent en sous-titre — *Interopérabilité et Orchestration
Agentiques* —, et **le citer par son seul titre le désigne désormais sans ambiguïté**.

☑ **Le Vol. IV a été recomposé une troisième fois le 26 août 2026**, au commit `56cfbfb`, et cette
fois **rien du titre ne bouge** : c'est le **bandeau de couverture** qui change de mention —
« SCIENCE ET GÉNIE INFORMATIQUES » devient **« INFORMATIQUE ET INGÉNIERIE DES SYSTÈMES »**. ⚠ *Neuf
signes de plus, et le gabarit le dit lui-même* : à `tracking: 0.30em` la mention sort des 148 mm et
« SYSTÈMES » se replie sur une seconde ligne **sans que Typst le signale** ; les deux segments du
bandeau passent donc à **`0.24em`**, la même valeur de part et d'autre. ☑ *Le seul fichier de source
touché est [`build/compendium.template`](<2%20-%20Compendium/build/compendium.template>), et la
pagination ne bouge pas* — **1 000 p.**, 13 164 965 octets contre 13 162 484.

## Carte du dépôt

*Les deux tables ci-dessus disent **ce que** chaque document soutient et ce qu'il pèse ; cette carte
ne le répète pas. Elle dit **où** les choses sont posées — et surtout **où le rangement ment**, car
la moitié des pièges de cette page sont des pièges de placement. Une annotation par ligne au plus :
⭑ ce qu'on ouvre en premier dans ce dossier, ⚠ le piège qu'on y trouve, renvoyé au point qui le
développe.*

```
Agentique/
├── README.md                        cette page. ⚠ Elle s'est dite « non versionnée » : c'était faux
│                                      — `git ls-files` la rend, et `APPAREIL.md` avec elle
├── APPAREIL.md                      ⭑ les douze contrôles avec leur verdict, la chaîne de
│                                      fabrication, et la commande derrière chaque chiffre d'ici
├── LICENSE                          ⭑ CC BY 4.0, 21 août 2026 — elle couvre le dépôt entier
├── .gitattributes                   `* text=auto eol=lf` : sans quoi un clone Windows rend les
│                                      `.sh` inexécutables et fausse toute comparaison à l'octet
├── NiveauMaturité.html              9 diapositives 16:9 — le seul contenu resté à la racine
│
├── 1 - Collection/                  Vol. I, II, III
│   ├── README.md                       ⭑ à ouvrir avant le reste : la chronique datée
│   ├── 0 - Références/                 `README.md` + le mémoire de maîtrise de l'auteur (1997),
│   │                                     seule pièce qui y reste : les 3 ouvrages de tiers ont quitté
│   │                                     l'index le 21 août 2026, le disque le 25 → son `README`
│   ├── 1 - InteroperabiliteAgentique/  `LICENSE` propre au Vol. I — mêmes termes que celle de la racine
│   ├── 2 - OrchestrationAgentique/     ⭑ `verification/` : revalidations et grille de conformité
│   ├── 3 - EntrepriseAgentique/        ⭑ `monographie/99-registre-gel.md` : ce qui est gelé, et depuis
│   │                                     quand. ⚠ Son `verification/` — 30 pièces — avait été supprimé
│   │                                     par accident le 8 août 2026 ; restauré le 21 août 2026
│   └──  ⤷ les trois build/ portent la même chaîne FESP : build-pdf.sh · fesp.template ·
│          inject-pagination.py (+ assemble.py aux Vol. II et III)
│
├── 2 - Compendium/                  Vol. IV
│   ├── Livre I … Livre V/              ⚠ chaque chapitre existe deux fois, en .md et en .html ;
│   │                                     `.claude/launch.json` les sert sur le port 8731
│   ├── figures/                        ⭑ `programme.md` : pourquoi trois figures ne se regravent
│   │                                     pas, et comment le graveur les tient tout de même → `APPAREIL.md`
│   ├── PRD/                            la spécification et ses sept contrôles au même endroit —
│   │                                     leurs commandes sont aux tableaux plus bas
│   ├── build/                          quatre points d'entrée ; deux seulement figurent aux tableaux
│   └── annexe-bibliographie.md · annexe-references.md
│
├── 3 - Traité/                      Vol. V — le seul dossier qui porte à la fois un document et le
│   │                                code qui le transpose
│   ├── Traité.md / .pdf                ⚠ à la racine du dossier, PAS sous docs/ : la fusion du
│   │                                     14 août 2026 les y a posés, et les renvois ont suivi
│   ├── figures/                        les 19 planches du traité — ⚠ restées à la RACINE DU DÉPÔT
│   │                                     du 14 au 21 août 2026, où elles clouaient son rendu → `APPAREIL.md`
│   ├── build/build-pdf.sh              ⭑ la commande de composition, écrite le 21 août 2026 — elle
│   │                                     n'existait nulle part au dépôt → `APPAREIL.md`
│   ├── bancs/                          ⚠ ses 24 pièces, supprimées par accident le 17 août 2026,
│   │                                     restaurées le 21 : c'est ce qui empêchait `cargo` de
│   │                                     démarrer → `APPAREIL.md`. ⚠ un journal de boucle, restauré
│   │                                     avec elles à la racine du dossier, en est ressorti le 22
│   ├── docs/                           ⭑ `decisions.md` : les cinq écarts et les verdicts de banc
│   ├── clippy.toml                     ⭑ ses interdictions sont des contrats, pas du style
│   └── web/                            ⚠ `index.html` seul est du source
│
├── 4 - Veille/                      Vol. VI et VII, et depuis le 28 août 2026 la note SDLC : trois
│   │                                documents dans un seul dossier, aucun dossier `figures/`
│   ├── Note-veille-SDLC-agentique.*    ⚠ le troisième document — hors livrables, et RIEN ne l'oppose
│   │                                     à lui-même : ni `check-veille.py` ni `check-revue.py` ne le
│   │                                     prennent en argument → `4 - Veille/README.md`
│   ├── Python/                         les trois contrôles ; ⚠ ils couvrent deux des trois documents
│   └── build/build-pdf.sh              ⭑ les deux commandes des livrables, versionnées le 21 août
│                                         2026 ; ⚠ pas celle de la note, qui se recopie à la main
│
├── 5 - Recension/                   Vol. VIII et sa planche
│   ├── figures/                     `dessine.py` + 5 SVG, chez leur document — comme celles du
│   │                                traité depuis le 21 août 2026
│   └── build/build-pdf.sh           ⭑ les deux commandes de PDF ; ⚠ pas les `.html`, faute d'une
│                                      feuille de style versionnée
│
└── 6 - Article/                     la prépublication HPC-QPU, 1er septembre 2026 — hors livrables,
    │                                et le seul dossier de document dont la source ne soit pas du
    │                                Markdown : Typst direct, sans Pandoc
    ├── README.md                    ⭑ pourquoi ce document n'est pas le neuvième livrable, et
    │                                  pourquoi le motif n'est pas celui de la note SDLC
    ├── article-hpc-qpu.typ/.pdf     la source et son rendu — 1 979 l. → 38 p.
    ├── references.bib               77 entrées, ⭑ toutes citées ; ⚠ aucun script du dépôt ne le
    │                                  vérifie — c'est une mesure de passe, pas une garantie
    ├── rejeu-politique.py           ⭑ le seul contrôle du dépôt qui EXÉCUTE une condition de
    │                                  réfutation (RÉF-6) au lieu de mesurer une forme
    └──  ⚠ pas de build/ : le PDF se fait par `typst compile`, la seule chaîne non scriptée du
           dépôt. ⚠ et deux des sept fichiers sont des points — `.gabarit-arxiv.typ`,
           `.figures.typ` —, invisibles à un `ls` sans `-a`, indispensables à la composition
```

**571 fichiers versionnés, 76,4 Mo** (**76 423 624 octets**, relevé le 1er septembre 2026) : 217 `.md`, 142 `.svg`,
76 `.rs`, 53 `.html`, 32 `.py`, 12 `.pdf`, 9 `.toml`, 8 `.sh`, 6 gabarits Pandoc, 4 `.gitignore`,
3 `.typ`, 2 `.mjs`, 2 `LICENSE`, 1 `.lua`, 1 `Cargo.lock`, 1 `launch.json`, 1 `.gitattributes`,
1 `.bib`. ⚠ *Les « 6 gabarits Typst » de la rédaction précédente étaient les six `.template`, qui
sont des gabarits **Pandoc** écrits en Typst ; les trois `.typ` de `6 - Article/` sont du Typst
propre, sans Pandoc — la distinction n'avait pas lieu d'être avant le 1er septembre 2026.*
**Les sept fichiers entrés depuis le 28 août sont ceux de l'article** — six au commit `da6255b`,
plus le `README.md` du dossier —, **+943 850 o. mesurés au format de l'index** pour les six.
⚠⚠ **Les deux nombres du relevé du 28 août 2026 étaient chacun 4 931 octets trop bas**, vérifié au
commit `90ef7d1` : le dépôt y pesait **75 456 272 o. en blobs** quand la page écrivait 75 451 341
pour un clone, et **75 574 708 o. au disque** quand elle écrivait 75 569 777. *Le même écart des
deux côtés, et l'écart LF ↔ disque de 118 436 o., lui, était juste.* ⚠ **La cause n'est pas
établie** — *mais elle n'est pas un ajout de lignes dans un fichier CRLF : cela aurait creusé
l'écart LF ↔ disque, qui n'a pas bougé.* **C'est exactement le piège que la ligne suivante
annonce**, et il s'est refermé sur la passe qui l'écrivait.
☑☑ **Le relevé de tête a changé de méthode le 1er septembre 2026, et c'est un durcissement** : il
n'est plus celui du disque de l'auteur mais celui de l'**index** — la somme des tailles de blobs,
LF, *ce qu'un clone rend*. **C'est le seul des deux qu'un tiers puisse reproduire**, et il ne dépend
ni de la plateforme ni de l'éditeur qui a écrit la dernière ligne. Le disque, lui, rend
**76 545 402 o.** au même moment — deux passes concordantes, `cat` en flux et somme des `stat` —,
soit **121 778 o. d'écart**, le `* text=auto eol=lf` de `.gitattributes` ramenant les fichiers texte
en LF. ⚠ *Cet écart ne se décompose plus comme la veille* : il valait 121 756 o. au commit
`da6255b` — les 118 436 du 28 août **plus les 3 320 lignes des cinq fichiers texte de l'article**,
un retour chariot chacune —, et **cette passe-ci l'a bougé de +22 en réécrivant sur le disque, en
LF, une partie des `.md` qu'elle éditait**. *La composition du solde n'a pas été cherchée, et le
commit n'en dépend pas : git normalise à l'entrée, le diff indexé ne porte aucune de ces lignes.*
Au 1er septembre 2026 l'arbre ne porte rien d'autre que les éditions de cette passe.
*Les **12 PDF** sont les **9 rendus des livrables**, la note de
veille SDLC, l'article et le mémoire de maîtrise de l'auteur ; les **8 `.sh`** sont les
**7 `build-pdf.sh`** — un par dossier de livrable, **les neuf PDF de livrable couverts, et eux
seuls** : ni le mémoire, qui n'est pas d'ici, ni la note, dont la commande n'est pas au script, ni
l'article, dont la chaîne tient en un `typst compile` que rien ne versionne — et `PRD/decompte.sh`.*
⚠ *Le compte avait **baissé** entre le 25 et le 28 août — **574 puis 564 fichiers** —, solde de deux
mouvements de sens contraire : **−12 `.md`**, les douze rapports d'audit interne de
`3 - Traité/bancs/audit-2026-08/` retirés le 25 août 2026 au commit `7a1b7f2` sur instruction
d'auteur, **−282 007 o. nets** une fois leurs 300 mentions réécrites, et **+2 fichiers** pour la note
de veille SDLC, **+750 614 o.** ; le Compendium recomposé le 26 en ajoute **+2 913**.*
⚠ **Le dépôt a maigri de 37,5 Mo le 21 août 2026**, et c'est un solde, non une pièce : les cinq
œuvres de tiers sorties de l'index en pèsent **38,3 Mo** à elles seules, l'`.html` de l'état de
l'art 0,76 Mo de plus, les pièces retouchées en place 0,28 de plus — et ce qui rentre le même jour
n'en rend que 1,8. *Il a gagné **62 fichiers**, pour un solde de **+56** — 519 au 20 août, 575 au
21.* **Cinquante-cinq sont des restaurations** : 24 sous `3 - Traité/bancs/` et un journal de boucle
à la racine du dossier, 30 sous `3 - EntrepriseAgentique/verification/`. **Les sept autres sont
neufs** : la licence, les trois chaînes, le `README` de `0 - Références/`, `.gitattributes` et
`APPAREIL.md`.
Hors `git` mais sur le disque, il ne reste que **les deux artefacts `wasm-bindgen` de `web/`** —
3,6 Mo, que [`web/index.html`](<3%20-%20Trait%C3%A9/web/index.html>) importe et que `wasm-pack`
refait. ☑ **Tout le reste a été effacé le 25 août 2026** : `3 - Traité/target/` par `cargo clean`
— **1 083 fichiers, 333,5 Mio** —, les **quatre `__pycache__`**, les **cinq PDF de tiers**
(38 281 125 octets, que l'historique git garde seul désormais) et les **deux `natif.tsv`** de
bancs, que la commande inscrite au `VERDICT.md` de chaque banc régénère. ⚠ *`target/` avait déjà
été vidé le 21 août 2026 — **12 060 fichiers et 3,4 Gio**, en éprouvant sans succès la piste du
cache vieilli —, et il se refait à la première construction.*

**Dix-huit `README.md` versionnés, celui-ci compris** — un par dossier, un par Livre du
compendium, plus `1 - Collection/2 -…/monographie/README.md`, `3 - Traité/docs/README.md` et
`0 - Références/README.md`, écrit le 21 août 2026 pour un dossier qui n'en avait pas. *Le
dix-huitième est celui de [`6 - Article/`](<6%20-%20Article/README.md>), écrit le 1er septembre 2026
pour la même raison.* **C'est là que vit ce
que cette page ne porte pas** : régimes de preuve, gels, dérogations, réserves, et l'historique des
passes. Cette page dit *ce qu'il y a* ; ils disent *ce que ça vaut*.
