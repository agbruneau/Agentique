# Agentique

**Un corpus de recherche** : Huit documents en français — **2 921 pages rendues**
sur neuf PDF — instruisent une seule question : *comment une entreprise de services financiers
canadienne déploie, gouverne et exploite des agents d'IA autonomes sous contrainte réglementaire ?*
S'y ajoute **un simulateur en Rust** — 76 fichiers, 29 690 lignes — qui transpose l'un de ces
documents en code exécutable sous une règle : *tout chiffre affiché doit être retrouvé par la
mesure, ou l'écart consigné*. **Cinq écarts** le sont, **dont trois contredisent le traité**
([`3 - Traité/docs/decisions.md`](<3%20-%20Trait%C3%A9/docs/decisions.md>)) — *et c'est la règle qui
tient, non un défaut : un écart consigné est ce que le dispositif produit quand il marche.*

**Les textes sont d'une seule main** : André-Guy Bruneau, M.Sc. IT, champ `/Author` des neuf PDF
livrés. ⚠ *Le dépôt, lui, ne l'est pas* : `git log` comptait, **au relevé du 21 août 2026 et avant
la passe de réparation que décrit cette page**, **280 commits — 260 signés André-Guy
Bruneau, 18 `Claude <noreply@anthropic.com>`, 2 `agbruneau`** — et **quatre fusions de *pull
requests* GitHub** ; deux branches `origin/claude/*` subsistent au distant. *La numérotation GitHub
monte à #5, mais une PR ne se compte pas par son numéro : la #4 n'a laissé aucune trace au dépôt, ni
fusion ni écrasement.* **Historique du 24 juin au 21 août 2026**, bornes du premier et du dernier
commit.

⚠ **Le dépôt est déclaré clos et final depuis le 8 août 2026** — décision d'auteur **D-13**,
[`2 - Compendium/PRD/PRD.md`](<2%20-%20Compendium/PRD/PRD.md>) §16 ; l'unique étiquette du dépôt,
`mono-v1.0`, est posée sur ce commit de clôture. Il a été rouvert une dizaine de fois depuis, chaque
fois pour une pièce nommée et pour elle seule : la chronique datée est en tête de
[`1 - Collection/README.md`](<1%20-%20Collection/README.md>).

☑ **[`LICENSE`](LICENSE) à la racine — CC BY 4.0, posée le 21 août 2026 sur instruction d'auteur**,
et elle couvre le dépôt entier : les huit documents, leurs rendus, le simulateur, les chaînes et les
figures. *Jusque-là, seul le Vol. I portait la sienne — mêmes termes, pour lui seul — et tout le
reste relevait du droit d'auteur par défaut.* ⚠ **Ce qu'elle ne couvre pas est écrit dans son texte** :
les œuvres de tiers citées, qui restent à leurs titulaires. **Trois ouvrages de tiers et deux articles
arXiv ont quitté l'index le même jour**, *avant* qu'elle ne soit posée et précisément parce qu'elle
n'aurait pas pu les couvrir — ni détruits ni perdus, disque et historique git les gardent, et leurs
renvois sont au
[`README` de `0 - Références/`](<1%20-%20Collection/0%20-%20R%C3%A9f%C3%A9rences/README.md>).

## Par où entrer, selon le temps qu'on a

| Temps                 | Ouvrir                                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **5 minutes**   | *Cinq schémas — état de l'art* : [`.pdf`](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.pdf>) 7 p. ou [`.html`](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.html>) 105 Ko autonome — cinq figures commentées et rien d'autre |
| **20 minutes**  | [`NiveauMaturité.html`](NiveauMaturit%C3%A9.html) — **10 diapositives** 16:9, six paliers de maturité ; autonome, aucune dépendance                                                                                                                                                                                                                    |
| **une soirée** | [`Veille Technologique.pdf`](<4%20-%20Veille/Veille%20Technologique.pdf>) — 144 p., l'état du champ déployé, 342 références                                                                                                                                                                                                                                |
| **le fond**     | [`Compendium.pdf`](<2%20-%20Compendium/Compendium.pdf>) — 1 000 pages, la somme dédoublonnée des trois monographies                                                                                                                                                                                                                                           |
| **du code**     | [`3 - Traité/`](<3%20-%20Trait%C3%A9/>) — le simulateur d'essaims : quatre *crates* et deux bancs, ☑ **467 `#[test]` au vert, clippy 0**                                                                                                                                                                                                              |

## Les huit documents

| #              | Document et dossier                                                                                                                                                                       | Ce qu'il soutient                                                                                                                                                                                                                                                                                                                              | Rendu                                                                                                                    | Source                                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **I**    | *Interopérabilité agentique en entreprise dans le domaine des services financiers*[`1 - Collection/1 - InteroperabiliteAgentique/`](<1%20-%20Collection/1%20-%20InteroperabiliteAgentique/>) | Autonomie**graduée** sous contrôle de finalité. Portée mondiale (UE, É.-U., R.-U., Asie)                                                                                                                                                                                                                                            | **569 p.**                                                                                                         | 7 257 l. / 1,74 Mo · 7 chapitres + Annexe B ·**28 diagrammes Mermaid** · 7 bibliographies            |
| **II**   | *Orchestration agentique*[`1 - Collection/2 - OrchestrationAgentique/`](<1%20-%20Collection/2%20-%20OrchestrationAgentique/>)                                                                  | Autonomie**encadrée** (*framed autonomy*). Portée Canada-Québec. Résultat négatif : quinze croisements protocole × texte canadien, **zéro lien documenté**                                                                                                                                                               | **387 p.**                                                                                                         | 3 306 l. / 0,87 Mo ·**29 pièces** assemblées · socle factuel de **46 entrées**, F-01 à F-48 |
| **III**  | *L'entreprise agentique — la fabrique de confiance*[`1 - Collection/3 - EntrepriseAgentique/`](<1%20-%20Collection/3%20-%20EntrepriseAgentique/>)                                             | La confiance ne se décrète pas, elle se fabrique : émettre une identité, l'appliquer, l'exploiter                                                                                                                                                                                                                                          | **427 p.**                                                                                                         | 3 275 l. / 1,12 Mo ·**34 pièces** · socle propre de **98 entrées**, F-01 à F-98              |
| **IV**   | *Conspectus — Interopérabilité et Orchestration Agentiques **en Entreprise***[`2 - Compendium/`](<2%20-%20Compendium/>)                                                       | La somme des trois volumes, dédoublonnée et re-datée à la source                                                                                                                                                                                                                                                                           | **1 000 p. exactement** ⚠ *cible d'auteur vérifiée par le script de rendu, qui échoue à 999 comme à 1 001* | **50 chapitres**, 5 Livres, 2 annexes · **118 figures** · socle consolidé `S-001`…`S-159` |
| **V**    | *Traité sur les systèmes multiagents en essaim*[`3 - Traité/`](<3%20-%20Trait%C3%A9/>)                                                                                              | La coordination par le milieu : ce qu'un essaim gagne à**ne pas** s'accorder, et ce qu'il le paie                                                                                                                                                                                                                                       | **143 p.**                                                                                                         | 1 875 l. · 8 chapitres, 24 sections,**123 notices**, 19 figures, 72 110 mots                           |
| **VI**   | *Veille technologique en entreprise*[`4 - Veille/`](<4%20-%20Veille/>)                                                                                                            | Le non-déterminisme du modèle enfermé dans des étapes bornées, journalisées, compensables : «*l'agent d'entreprise fiable de 2026 est enveloppé* »                                                                                                                                                                                  | **144 p.**                                                                                                         | 1 932 l. · 94 sections, 24 tableaux,**342 références**, 25 questions ouvertes                        |
| **VII**  | *Revue de la littérature académique*[`4 - Veille/`](<4%20-%20Veille/>)                                                                                                          | ⚠ Un résultat**sur son propre corpus, pas sur le champ** : **145 pièces sur 189 — 77 % — ne présentent aucun signe de revue par les pairs à leur notice**, 12 seulement portant une attestation. *La revue interdit expressément d'en tirer une part du champ : « le lire comme une part du champ serait circulaire »* | **59 p.**                                                                                                          | 1 052 l. ·**192 références**, 8 tableaux                                                             |
| **VIII** | *État de l'art en services financiers*[`5 - Recension/`](<5%20-%20Recension/>)                                                                                                   | Le débat porte sur la pile protocolaire ; dans une coopérative régie,**la pile n'est pas ce qui décide**                                                                                                                                                                                                                             | **185 p.** + planche de **7 p.** (`.md`/`.pdf`/`.html`)                                                | 1 984 l. ·**15 sections** numérotées, **312 références** (1 à 312, sans trou), 5 figures    |

⚠ **Le chiffre « huit » est un constat, pas une décision d'auteur.** Le dépôt a longtemps compté
sept livrables ; le huitième — l'état de l'art — a été rangé parmi eux le 20 août 2026 par les
`README.md` du dépôt, sur motif écrit, et **le PRD ne porte aucune décision sur ce document**. Un
lecteur qui cite le compte doit dire à quelle date il le tire et d'où.

☑ **Trois documents portaient exactement le même titre ; ils ne le portent plus depuis le
21 août 2026.** La veille, la revue et l'état de l'art déclaraient tous
`title: "Interopérabilité et Orchestration Agentiques"`, et **seul le sous-titre les séparait** —
c'était la confusion la plus facile à faire ici, et elle allait jusqu'au champ `/Title` des trois
PDF, identique aux trois. *La correction n'invente aucun mot : les deux champs sont **échangés**.*
Le discriminant devient le titre — « Veille technologique en entreprise », « Revue de la littérature
académique », « État de l'art en services financiers » — et le nom commun devient le sous-titre, ce
qu'il est en fait : **un nom de série**. Les trois PDF ont été recomposés le même jour par les
chaînes versionnées ce jour-là, **à pagination inchangée** — 144, 59 et 185 pages. *Les six PDF de
tête portent désormais six `/Title` distincts.*

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
├── APPAREIL.md                      ⭑ les onze contrôles avec leur verdict, la chaîne de
│                                      fabrication, et la commande derrière chaque chiffre d'ici
├── LICENSE                          ⭑ CC BY 4.0, 21 août 2026 — elle couvre le dépôt entier
├── .gitattributes                   `* text=auto eol=lf` : sans quoi un clone Windows rend les
│                                      `.sh` inexécutables et fausse toute comparaison à l'octet
├── NiveauMaturité.html              10 diapositives 16:9 — le seul contenu resté à la racine
│
├── 1 - Collection/                  Vol. I, II, III
│   ├── README.md                       ⭑ à ouvrir avant le reste : la chronique datée
│   ├── 0 - Références/                 `README.md` + le mémoire de maîtrise de l'auteur (1997) ;
│   │                                     les 3 ouvrages de tiers sont sortis de l'index → point 8
│   ├── 1 - InteroperabiliteAgentique/  `LICENSE` propre au Vol. I — mêmes termes que celle de la racine
│   ├── 2 - OrchestrationAgentique/     ⭑ `verification/` : revalidations et grille de conformité
│   ├── 3 - EntrepriseAgentique/        ⭑ `monographie/99-registre-gel.md` : ce qui est gelé, et depuis
│   │                                     quand. ⚠ Son `verification/` — 30 pièces — avait été supprimé
│   │                                     par accident le 8 août 2026 ; restauré le 21 → point 5
│   └──  ⤷ les trois build/ portent la même chaîne FESP : build-pdf.sh · fesp.template ·
│          inject-pagination.py (+ assemble.py aux Vol. II et III)
│
├── 2 - Compendium/                  Vol. IV
│   ├── Livre I … Livre V/              ⚠ chaque chapitre existe deux fois, en .md et en .html ;
│   │                                     `.claude/launch.json` les sert sur le port 8731
│   ├── figures/                        ⭑ `programme.md` : pourquoi trois figures ne se regravent
│   │                                     pas, et comment le graveur les tient tout de même → point 6
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
│   │                                     du 14 au 21 août 2026, où elles clouaient son rendu → point 3
│   ├── build/build-pdf.sh              ⭑ la commande de composition, écrite le 21 août 2026 — elle
│   │                                     n'existait nulle part au dépôt → point 1
│   ├── bancs/ · gauntlet-log.md        ⚠ supprimés par accident le 17 août 2026, restaurés le 21 :
│   │                                     c'est ce qui empêchait `cargo` de démarrer → point 2
│   ├── docs/                           ⭑ `decisions.md` : les cinq écarts et les verdicts de banc
│   ├── clippy.toml                     ⭑ ses interdictions sont des contrats, pas du style
│   └── web/                            ⚠ `index.html` seul est du source
│
├── 4 - Veille/                      Vol. VI et VII : deux documents dans un seul dossier, aucun
│   ├── Python/                      dossier `figures/`, et ses trois contrôles sous `Python/`
│   └── build/build-pdf.sh              ⭑ les deux commandes, versionnées le 21 août 2026
│
└── 5 - Recension/                   Vol. VIII et sa planche
    ├── figures/                     `dessine.py` + 5 SVG, chez leur document — comme celles du
    │                                traité depuis le 21 août 2026
    └── build/build-pdf.sh           ⭑ les deux commandes de PDF ; ⚠ pas les `.html`, faute d'une
                                       feuille de style versionnée
```

**575 fichiers versionnés, 75,1 Mo** (75 105 411 octets) : 228 `.md`, 142 `.svg`, 76 `.rs`,
53 `.html`, 31 `.py`, 10 `.pdf`, 9 `.toml`, 8 `.sh`, 6 gabarits Typst, 4 `.gitignore`, 2 `.mjs`,
2 `LICENSE`, 1 `.lua`, 1 `Cargo.lock`, 1 `launch.json`, 1 `.gitattributes`. *Les **10 PDF** sont les
**9 rendus des livrables** et le mémoire de maîtrise de l'auteur ; les **8 `.sh`** sont les
**7 `build-pdf.sh`** — un par dossier de livrable, les neuf PDF couverts — et `PRD/decompte.sh`.*
⚠ **Le dépôt a maigri de 36,4 Mo le 21 août 2026** : ce sont les cinq œuvres de tiers sorties de
l'index, point 8. *Il a grossi de 58 fichiers le même jour, et ce sont des restaurations* : 25 sous
`3 - Traité/bancs/`, 30 sous `3 - EntrepriseAgentique/verification/`, plus la licence, les trois
chaînes, le `README` de `0 - Références/` et `.gitattributes`.
Hors `git` mais sur le disque : `3 - Traité/target/` — ⚠ *vidé le 21 août 2026 par `cargo clean`, **12 060 fichiers et 3,4 Gio**, en éprouvant sans succès la piste du cache vieilli ; il se refait à la première construction* —, les deux artefacts `wasm-bindgen`
de `web/`, les cinq PDF de tiers, et les `__pycache__`.

**Seize `README.md` versionnés, dix-sept avec celui-ci** — un par dossier, un par Livre du
compendium, plus `1 - Collection/2 -…/monographie/README.md`, `3 - Traité/docs/README.md` et
`0 - Références/README.md`, écrit le 21 août 2026 pour un dossier qui n'en avait pas. **C'est là que vit ce
que cette page ne porte pas** : régimes de preuve, gels, dérogations, réserves, et l'historique des
passes. Cette page dit *ce qu'il y a* ; ils disent *ce que ça vaut*.
