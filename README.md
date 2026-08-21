# Agentique

**Un corpus de recherche** : Huit documents en français — **2 921 pages rendues**
sur neuf PDF — instruisent une seule question : *comment une entreprise de services financiers
canadienne déploie, gouverne et exploite des agents d'IA autonomes sous contrainte réglementaire ?*
S'y ajoute **un simulateur en Rust** — 71 fichiers, 29 251 lignes — qui transpose l'un de ces
documents en code exécutable sous une règle : *tout chiffre affiché doit être retrouvé par la
mesure, ou l'écart consigné*. **Cinq écarts** le sont, **dont trois contredisent le traité**
([`3 - Traité/docs/decisions.md`](<3%20-%20Trait%C3%A9/docs/decisions.md>)).

**Les textes sont d'une seule main** : André-Guy Bruneau, M.Sc. IT, champ `/Author` des neuf PDF
livrés. ⚠ *Le dépôt, lui, ne l'est pas* : `git log` compte **280 commits — 260 signés André-Guy
Bruneau, 18 `Claude <noreply@anthropic.com>`, 2 `agbruneau`** — et **quatre fusions de *pull
requests* GitHub** ; deux branches `origin/claude/*` subsistent au distant. *La numérotation GitHub
monte à #5, mais une PR ne se compte pas par son numéro : la #4 n'a laissé aucune trace au dépôt, ni
fusion ni écrasement.* **Historique du 24 juin au 21 août 2026**, bornes du premier et du dernier
commit.

⚠ **Le dépôt est déclaré clos et final depuis le 8 août 2026** — décision d'auteur **D-13**,
[`2 - Compendium/PRD/PRD.md`](<2%20-%20Compendium/PRD/PRD.md>) §16 ; l'unique étiquette du dépôt,
`mono-v1.0`, est posée sur ce commit de clôture. Il a été rouvert une dizaine de fois depuis, chaque
fois pour une pièce nommée et pour elle seule : la chronique datée est en tête de
[`1 - Corpus/README.md`](<1%20-%20Corpus/README.md>).

⚠ **Aucune licence à la racine** : droit d'auteur par défaut, tous droits réservés. Seul le Vol. I
porte un [`LICENSE`](<1%20-%20Corpus/1%20-%20InteroperabiliteAgentique/LICENSE>) — CC BY 4.0 —, et il
ne vaut que pour lui.

## Par où entrer, selon le temps qu'on a

| Temps                 | Ouvrir                                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **5 minutes**   | *Cinq schémas — état de l'art* : [`.pdf`](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.pdf>) 7 p. ou [`.html`](<5%20-%20Recension/Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.html>) 105 Ko autonome — cinq figures commentées et rien d'autre |
| **20 minutes**  | [`NiveauMaturité.html`](NiveauMaturit%C3%A9.html) — **10 diapositives** 16:9, six paliers de maturité ; autonome, aucune dépendance                                                                                                                                                                                                                    |
| **une soirée** | [`Veille Technologique.pdf`](<4%20-%20Veille/Veille%20Technologique.pdf>) — 144 p., l'état du champ déployé, 342 références                                                                                                                                                                                                                                |
| **le fond**     | [`Compendium.pdf`](<2%20-%20Compendium/Compendium.pdf>) — 1 000 pages, la somme dédoublonnée des trois monographies                                                                                                                                                                                                                                           |
| **du code**     | [`3 - Traité/`](<3%20-%20Trait%C3%A9/>) — le simulateur d'essaims : quatre *crates*, 467 `#[test]`, ⚠ *qui ne se construit pas en l'état*                                                                                                                                                                                                              |

## Les huit documents

| #              | Document et dossier                                                                                                                                                                       | Ce qu'il soutient                                                                                                                                                                                                                                                                                                                              | Rendu                                                                                                                    | Source                                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **I**    | *Interopérabilité agentique en entreprise dans le domaine des services financiers*[`1 - Corpus/1 - InteroperabiliteAgentique/`](<1%20-%20Corpus/1%20-%20InteroperabiliteAgentique/>) | Autonomie**graduée** sous contrôle de finalité. Portée mondiale (UE, É.-U., R.-U., Asie)                                                                                                                                                                                                                                            | **569 p.**                                                                                                         | 7 257 l. / 1,74 Mo · 7 chapitres + Annexe B ·**28 diagrammes Mermaid** · 7 bibliographies            |
| **II**   | *Orchestration agentique*[`1 - Corpus/2 - OrchestrationAgentique/`](<1%20-%20Corpus/2%20-%20OrchestrationAgentique/>)                                                                  | Autonomie**encadrée** (*framed autonomy*). Portée Canada-Québec. Résultat négatif : quinze croisements protocole × texte canadien, **zéro lien documenté**                                                                                                                                                               | **387 p.**                                                                                                         | 3 306 l. / 0,87 Mo ·**29 pièces** assemblées · socle factuel de **46 entrées**, F-01 à F-48 |
| **III**  | *L'entreprise agentique — la fabrique de confiance*[`1 - Corpus/3 - EntrepriseAgentique/`](<1%20-%20Corpus/3%20-%20EntrepriseAgentique/>)                                             | La confiance ne se décrète pas, elle se fabrique : émettre une identité, l'appliquer, l'exploiter                                                                                                                                                                                                                                          | **427 p.**                                                                                                         | 3 275 l. / 1,12 Mo ·**34 pièces** · socle propre de **98 entrées**, F-01 à F-98              |
| **IV**   | *Conspectus — Interopérabilité et Orchestration Agentiques **en Entreprise***[`2 - Compendium/`](<2%20-%20Compendium/>)                                                       | La somme des trois volumes, dédoublonnée et re-datée à la source                                                                                                                                                                                                                                                                           | **1 000 p. exactement** ⚠ *cible d'auteur vérifiée par le script de rendu, qui échoue à 999 comme à 1 001* | **50 chapitres**, 5 Livres, 2 annexes · **118 figures** · socle consolidé `S-001`…`S-159` |
| **V**    | *Traité sur les systèmes multiagents en essaim*[`3 - Traité/`](<3%20-%20Trait%C3%A9/>)                                                                                              | La coordination par le milieu : ce qu'un essaim gagne à**ne pas** s'accorder, et ce qu'il le paie                                                                                                                                                                                                                                       | **143 p.**                                                                                                         | 1 875 l. · 8 chapitres, 24 sections,**123 notices**, 19 figures, 72 110 mots                           |
| **VI**   | *…— veille technologique en entreprise*[`4 - Veille/`](<4%20-%20Veille/>)                                                                                                            | Le non-déterminisme du modèle enfermé dans des étapes bornées, journalisées, compensables : «*l'agent d'entreprise fiable de 2026 est enveloppé* »                                                                                                                                                                                  | **144 p.**                                                                                                         | 1 932 l. · 94 sections, 24 tableaux,**342 références**, 25 questions ouvertes                        |
| **VII**  | *…— revue de la littérature académique*[`4 - Veille/`](<4%20-%20Veille/>)                                                                                                          | ⚠ Un résultat**sur son propre corpus, pas sur le champ** : **145 pièces sur 189 — 77 % — ne présentent aucun signe de revue par les pairs à leur notice**, 12 seulement portant une attestation. *La revue interdit expressément d'en tirer une part du champ : « le lire comme une part du champ serait circulaire »* | **59 p.**                                                                                                          | 1 052 l. ·**192 références**, 8 tableaux                                                             |
| **VIII** | *…— état de l'art en services financiers*[`5 - Recension/`](<5%20-%20Recension/>)                                                                                                   | Le débat porte sur la pile protocolaire ; dans une coopérative régie,**la pile n'est pas ce qui décide**                                                                                                                                                                                                                             | **185 p.** + planche de **7 p.** (`.md`/`.pdf`/`.html`)                                                | 1 984 l. ·**15 sections** numérotées, **312 références** (1 à 312, sans trou), 5 figures    |

⚠ **Le chiffre « huit » est un constat, pas une décision d'auteur.** Le dépôt a longtemps compté
sept livrables ; le huitième — l'état de l'art — a été rangé parmi eux le 20 août 2026 par les
`README.md` du dépôt, sur motif écrit, et **le PRD ne porte aucune décision sur ce document**. Un
lecteur qui cite le compte doit dire à quelle date il le tire et d'où.

⚠ **Trois documents portent exactement le même titre.** La veille, la revue et l'état de l'art
déclarent tous `title: "Interopérabilité et Orchestration Agentiques"` : **seul le sous-titre les
sépare**, et c'est la confusion la plus facile à faire ici. *Le Vol. IV n'en est pas : son titre
ajoute « en Entreprise ».*

## Carte du dépôt

*Les deux tables ci-dessus disent **ce que** chaque document soutient et ce qu'il pèse ; cette carte
ne le répète pas. Elle dit **où** les choses sont posées — et surtout **où le rangement ment**, car
la moitié des pièges de cette page sont des pièges de placement. Une annotation par ligne au plus :
⭑ ce qu'on ouvre en premier dans ce dossier, ⚠ le piège qu'on y trouve, renvoyé au point qui le
développe.*

```
Agentique/
├── README.md                        ⚠ non versionné : le commit de tête, le 21 août 2026, est une
│                                      suppression du README précédent — cette page vit hors de git
├── APPAREIL.md                      hors git lui aussi — les onze contrôles, la chaîne de
│                                      fabrication, et la commande derrière chaque chiffre d'ici
├── NiveauMaturité.html              ⚠ personne n'y renvoie → point 7
├── figures/                         ⚠ ce ne sont pas les figures du dépôt, mais celles du TRAITÉ,
│   ├── contenu.py  dessine.py          restées ici quand il est entré → point 3
│   └── f-00…f-08-3 *.svg
│
├── 1 - Corpus/                      Vol. I, II, III
│   ├── README.md                       ⭑ à ouvrir avant le reste : la chronique datée
│   ├── 0 - Références/                 ⚠ 4 PDF hors corpus, 3 130 p. : trois ouvrages de tiers
│   │                                     (EIP 2003, Distributed Systems 2007, SEBoK 2026) et le
│   │                                     mémoire de maîtrise de l'auteur (1997) → point 8
│   ├── 1 - InteroperabiliteAgentique/  ⭑ `LICENSE` — la seule du dépôt
│   ├── 2 - OrchestrationAgentique/     ⚠ `prd/` mêle les pièces d'auteur et 2 PDF arXiv de tiers → point 8
│   ├── 3 - EntrepriseAgentique/        ⭑ `monographie/99-registre-gel.md` : ce qui est gelé, et depuis quand
│   └──  ⤷ les trois build/ portent la même chaîne FESP : build-pdf.sh · fesp.template ·
│          inject-pagination.py (+ assemble.py aux Vol. II et III)
│
├── 2 - Compendium/                  Vol. IV
│   ├── Livre I … Livre V/              ⚠ chaque chapitre existe deux fois, en .md et en .html ;
│   │                                     `.claude/launch.json` sert le dossier sur le port 8731
│   ├── figures/                        ⭑ `programme.md` : pourquoi trois figures ne se regravent
│   │                                     pas → point 6
│   ├── PRD/                            la spécification et ses sept contrôles au même endroit —
│   │                                     leurs commandes sont aux tableaux plus bas
│   ├── build/                          quatre points d'entrée ; deux seulement figurent aux tableaux
│   └── annexe-bibliographie.md · annexe-references.md
│
├── 3 - Traité/                      Vol. V — le seul dossier qui porte à la fois un document et le
│   │                                code qui le transpose
│   ├── Traité.md / .pdf                ⚠ à la racine du dossier, PAS sous docs/ : la fusion du
│   │                                     14 août 2026 les y a posés, et les renvois ont suivi
│   ├── docs/                           ⭑ `decisions.md` : les cinq écarts et les verdicts de banc
│   ├── Cargo.toml · crates/            ⚠ deux membres du workspace y sont nommés, absents du
│   │                                     disque → point 2
│   ├── clippy.toml                     ⭑ ses interdictions sont des contrats, pas du style
│   └── web/                            ⚠ `index.html` seul est du source
│
├── 4 - Veille/                      Vol. VI et VII : deux documents dans un seul dossier, aucun
│   └── Python/                      dossier `figures/`, et ses trois contrôles sous `Python/`
│
└── 5 - Recension/                   Vol. VIII et sa planche
    └── figures/                     `dessine.py` + 5 SVG, chez leur document — contrairement à
                                     celles du traité, en tête de carte
```

**517 fichiers versionnés, 111,5 Mo** (111 542 162 octets) : 179 `.md`, 142 `.svg`, 71 `.rs`,
53 `.html`, 31 `.py`, 15 `.pdf`, 7 `.toml`, 6 gabarits Typst, 5 `.sh`, 4 `.gitignore`, 1 `.lua`,
1 `Cargo.lock`, 1 `launch.json`, 1 `LICENSE`. *Les 15 PDF se répartissent en **9 rendus des
livrables**, 4 dans `0 - Références/` et **2 articles arXiv dans `1 - Corpus/2 -…/prd/`**.*
Hors `git` mais sur le disque : `3 - Traité/target/` (**3,3 Go**), les deux artefacts `wasm-bindgen`
de `web/`, et les `__pycache__`.

**Quinze `README.md` versionnés, seize avec celui-ci** — un par dossier, un par Livre du compendium,
plus `1 - Corpus/2 -…/monographie/README.md` et `3 - Traité/docs/README.md`. **C'est là que vit ce
que cette page ne porte pas** : régimes de preuve, gels, dérogations, réserves, et l'historique des
passes. Cette page dit *ce qu'il y a* ; ils disent *ce que ça vaut*.

## Ce qui accroche, quand on arrive

1. **Cinq des neuf PDF livrés ne se refont pas depuis ce dépôt.** Les quatre `build-pdf.sh`
   versionnés couvrent les Vol. I, II, III et le Compendium — et rien d'autre. `3 - Traité/`,
   `4 - Veille/` et `5 - Recension/` ne portent **ni script, ni gabarit Typst** : leur réglage vit
   dans l'en-tête YAML de chaque source. *Et les cinq ne sont pas logés à la même enseigne* : pour
   la veille, la revue, l'état de l'art et sa planche, **l'appel de Pandoc est écrit en clair dans le
   `README.md` du dossier**, à recopier tel quel (`4 - Veille/README.md:179` et `:183`,
   `5 - Recension/README.md:139-150`) ; **pour le traité, la commande n'existe nulle part au dépôt**
   — son `README.md:14` dit seulement que la chaîne *ne se lance que depuis la racine*, jamais avec
   quels arguments. *Aucun des cinq ne se recompose par un script : quatre par une commande
   recopiée, le traité par une commande à reconstituer.*
2. **`cargo` ne démarre pas** — deux membres de workspace manquants (§ ci-dessous).
3. **Les figures du traité sont à la racine.** `figures/` n'est pas un dossier du dépôt : ce sont les
   19 planches de `3 - Traité/Traité.md`, qui les appelle en chemin relatif. **Rendre le traité
   depuis son propre dossier ne marche pas** — c'est là toute la contrainte de rendu que son
   `README.md` énonce, et le point 1 dit ce qu'il n'énonce pas.
4. **Trois contrôles sur onze sortent 1** : `decompte.sh --verifier` (le Vol. II mesure 93 239 mots
   pour 93 242 attendus), `check-toc-mutations.py` (une mutation sur 23 échappe),
   `check-compendium-mutations.py` (s'arrête en `AssertionError`).
5. **35 renvois relatifs des quinze `README.md` versionnés visaient le vide ; ce fichier-ci en
   répare dix-neuf par sa seule existence. Seize restent morts** : huit vers `3 - Traité/bancs/`,
   cinq vers un `2 - Compendium/Compendium.html` qui n'existe pas, deux vers un `gauntlet-log.md`
   absent, et le dernier est un exemple de syntaxe cité en prose
   (`1 - Corpus/2 - OrchestrationAgentique/README.md:72`) — mort comme lien, correct comme prose.
   *Aucun contrôle du dépôt ne résout un lien markdown : c'est une mesure faite ici, pas une
   garantie tenue là-bas.*
6. **Trois des 118 figures du compendium ne se regravent pas** — `f-01-00-invariant`,
   `f-01-01-pile-canonique`, `f-08-01-n-fois-m`. Elles sont citées par leurs pièces mais absentes de
   la spécification du graveur, qui n'en connaît que 115 : ce sont les trois figures **antérieures**
   au programme, et [`figures/programme.md`](<2%20-%20Compendium/figures/programme.md>) le dit.
7. **`NiveauMaturité.html` n'a aucun lien entrant.** C'est le seul fichier de contenu **versionné**
   resté à la racine ; un seul `README.md` le mentionne, en passant et sans lien
   (`5 - Recension/README.md:72`).
8. **Des ouvrages de tiers sous droit d'auteur sont versionnés, et pas seulement dans
   `0 - Références/`** : deux articles arXiv dorment aussi dans
   `1 - Corpus/2 - OrchestrationAgentique/prd/`. Le dépôt n'a pas de licence.

### Le workspace Rust ne se construit pas en l'état

[`3 - Traité/Cargo.toml`](<3%20-%20Trait%C3%A9/Cargo.toml>) déclare six membres ; **deux sont absents
du disque et de l'index** — `bancs/dt1-flottant` et `bancs/parite-wasm`. Cargo refuse donc de
charger le workspace, et **aucune commande `cargo` ne passe**, pas même `cargo build -p sim-core` :

```
error: failed to load manifest for workspace member `…/3 - Traité/bancs/dt1-flottant`
```

Le code est là et complet — quatre *crates* en couches
(`sim-core` ← `sim-milieu` ← `sim-agents` ← `sim-viz`), 71 fichiers `.rs`, **467 attributs
`#[test]`**, `#![deny(missing_docs)]` sur les quatre. Le manifeste passe en outre
`disallowed_methods` et `disallowed_types` en `deny` au niveau du workspace, et les appelle « des
**contrats**, pas du style » : [`clippy.toml`](<3%20-%20Trait%C3%A9/clippy.toml>) **interdit sept
méthodes de `f64`** — `ln`, `exp`, `powf`, `sin`, `cos`, `atan2`, `mul_add` — au titre de NF-02,
parce que six donnent des bits différents en natif et en WASM, **et `HashMap` / `HashSet`** au titre
de PD1, dont l'itération non ordonnée contaminerait tout chemin d'ordonnancement. Le remède au
workspace est de recréer les deux membres manquants ou de les retirer de la liste `members`.

☑ **Rien de `bancs/` n'est perdu : tout est dans l'historique.**
`git log --all --diff-filter=A --name-only` rend **24 chemins sous `bancs/`**, dont les **trois
`VERDICT.md`** et les **douze pièces de `bancs/audit-2026-08/`** ; `3 - Traité/gauntlet-log.md` y est
aussi. Dix des seize renvois morts — huit vers `bancs/`, deux vers `gauntlet-log.md` — se rattrapent
donc dans l'historique, et non depuis l'arbre de travail. ⚠ **Mais pas avec le premier commit venu :
`git log -1 -- <chemin>` livre le commit de *suppression*, sur lequel `git show` échoue** par
`fatal: path … does not exist in …`. C'est le **parent** qu'il faut, d'où le `^` :

```bash
C="3 - Traité/bancs/parite-wasm/VERDICT.md"
git show "$(git log -1 --format=%H -- "$C")^:$C"
```

*Ce qui manque à l'arbre, ce sont les calculs ; les verdicts eux-mêmes se relisent en clair au
tableau « Les verdicts de banc » de
[`docs/decisions.md`](<3%20-%20Trait%C3%A9/docs/decisions.md>) — parité natif/WASM tenue, `mul_add`
dépendant de la machine de construction, NF-05 non atteinte à 10-15 s simulées par seconde-cœur
contre une cible de 10³ — et dans `SPEC.md` et `DEVELOPPEMENT.md`.*

## Refaire, ou vérifier

*Rien ici ne s'impose à qui vient lire : les huit documents sont déjà rendus en PDF.*
**[`APPAREIL.md`](APPAREIL.md)** porte l'appareil du dépôt — les **onze contrôles** avec leur verdict
au 21 août 2026 et le motif des trois qui sortent 1, l'ordre réel de fabrication (graver →
assembler → composer), les cinq points d'entrée qui n'ont pas été rejoués, et **la commande qui
atteste chaque chiffre de cette page**.

⚠ **Ce que cette page ne mesure pas** : la véracité d'un seul énoncé des huit documents. Elle mesure
l'appareil — fichiers, cardinaux, rendus, contrôles —, jamais le fond. Les régimes de preuve, les
gels et les réserves de chaque livrable sont dans le `README.md` de son dossier, et c'est là qu'il
faut les lire avant de citer quoi que ce soit.
