# Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique

Répertoire de rédaction du **Livre I** du compendium *La somme agentique* (Vol. IV). Il ne porte
aucune décision, aucun socle et aucun garde-fou propre : la spécification de contenu est le
[`PRD/TOC.md`](../PRD/TOC.md) v0.24, la gouvernance de la rédaction le [`PRD/PRD.md`](../PRD/PRD.md)
v0.8. En cas d'écart entre une pièce de ce dossier et le TOC, **le TOC prime** — sauf déviation
fondée, qui se déclare (décision 8 du TOC) et se remonte, jamais se corrige au plan depuis ici.

## ⚠ État : le Livre est rédigé, arbitré, et toujours non publiable

Le Livre I compte **onze chapitres** au plan (ch. 1-11), en deux mouvements — les fondements
(ch. 1-6), la couche protocolaire agentique (ch. 7-11). **Les onze sont rédigés** ; ils l'ont été
**hors portes**, et ils restent en **brouillon non publiable**.

⚠ **Ce qui a changé le 27 juillet 2026, et ce qui n'a pas changé.** La passe d'arbitrage du même jour
(PRD v0.8, TOC v0.24) a **soldé les treize remontées** que la rédaction avait ouvertes et **franchi
deux des sept portes**. Le tableau ci-dessous est l'état exact, et il se lit dans les deux sens :

| | État |
|---|---|
| **Remontées ouvertes** | **zéro** — R-IV-01 à R-IV-13 closes, chacune là où elle fait foi |
| **Décisions d'auteur prises** | **trois sur huit** — D-1 (gel unique), D-6 (instance d'arbitrage), **D-7** (périmètre assumé) |
| **Portes franchies** | **deux sur sept** — **G-2** entièrement ; **G-1** pour le seul volet du Livre I |
| **Socle consolidé** | ⚠ **zéro entrée** — **G-3 n'est pas entamée** |
| **Énoncés centraux au sens de CA-IV-01** | ⚠ **aucun**, dans aucune des onze pièces |
| **Statut des pièces** | **brouillon non publiable** — inchangé |

*Zéro remontée ouverte ne veut pas dire pièce recevable : cela veut dire qu'aucune question n'attend
plus de réponse qui ne soit déjà tranchée.* **Deux portes franchies sur sept ne font pas un volume
recevable** — et la porte qui manque, G-3, est celle dont tout le reste dépend.

⚠ **Une obligation reste due, et elle n'est pas une porte : CA-IV-13, la relecture adversariale.** Le
PRD exige que chaque pièce soit relue **par un relecteur distinct du rédacteur, chargé de réfuter**.
La passe du 27 juillet 2026 a produit des contrôles **mécaniques** (huit par pièce, plus les trois du
volume) et une **re-datation à la source primaire**, qui ont trouvé de vrais défauts — mais elle a
été conduite par la même main que la rédaction. **CA-IV-13 n'est donc pas satisfaite**, et rien dans
ce dossier ne doit être lu comme si elle l'était. *Un contrôle mécanique n'est pas une réfutation, et
se relire soi-même n'est pas être relu.*

⚠ **Le Vol. IV n'est pas requalifié pour autant.** Il demeure un cadrage au regard du dépôt : ni son
`CLAUDE.md` racine, ni la veille technologique ne le décrivent autrement, et **la veille ne se corrige
jamais** — sa réf. [220] décrit un cadrage sans chapitre, et cela reste vrai à sa date.

### Volumétrie réelle — publiable depuis G-2

**64 611 mots** de corps pour les onze pièces, mesurés le 27 juillet 2026 par
[`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte du volume — contre une enveloppe
de Livre de **65 000** au TOC, soit **−0,6 %**.

⚠ **Le chiffre agrégé est bon et les chiffres individuels sont mauvais, et c'est le constat qui
compte.** Chaque pièce a **dérivé** sa cible de l'enveloppe du Livre, personne n'ayant additionné les
dérivations : leur somme atteint **93 000 mots**, soit **+43 %** de l'enveloppe qu'elles prétendaient
toutes respecter. Les écarts individuels vont de **−55,9 %** (ch. 6) à **+0,1 %** (ch. 10). *C'est la
cible dérivée qui était fausse, non la pièce qui est courte* — et l'écart se documente, il ne se
corrige ni par amputation ni par gonflement.

### Les onze pièces

| Pièce | Chapitre | Mouvement |
|---|---|---|
| [`01-interoperabilite-integration-entreprise.md`](01-interoperabilite-integration-entreprise.md) · [`.html`](01-interoperabilite-integration-entreprise.html) | Ch. 1 — L'interopérabilité comme problème d'intégration d'entreprise | fondements |
| [`02-donnees-semantique-ontologies.md`](02-donnees-semantique-ontologies.md) · [`.html`](02-donnees-semantique-ontologies.html) | Ch. 2 — Données, sémantique et ontologies | fondements |
| [`03-securite-identite-gouvernance.md`](03-securite-identite-gouvernance.md) · [`.html`](03-securite-identite-gouvernance.html) | Ch. 3 — Sécurité, identité et gouvernance de l'interopérabilité | fondements |
| [`04-ingenierie-systemes-agentiques.md`](04-ingenierie-systemes-agentiques.md) · [`.html`](04-ingenierie-systemes-agentiques.html) | Ch. 4 — L'ingénierie des systèmes agentiques : anatomie, raisonnement, outils | fondements |
| [`05-ancrage-informationnel.md`](05-ancrage-informationnel.md) · [`.html`](05-ancrage-informationnel.html) | Ch. 5 — Ancrage informationnel : mémoire, contexte, RAG agentique | fondements |
| [`06-multi-agents-evaluation-surete.md`](06-multi-agents-evaluation-surete.md) · [`.html`](06-multi-agents-evaluation-surete.html) | Ch. 6 — Systèmes multi-agents, évaluation et sûreté | fondements |
| [`07-genealogie-gouvernance.md`](07-genealogie-gouvernance.md) · [`.html`](07-genealogie-gouvernance.html) | Ch. 7 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts | couche protocolaire |
| [`08-anatomie-mcp-a2a.md`](08-anatomie-mcp-a2a.md) · [`.html`](08-anatomie-mcp-a2a.html) | Ch. 8 — Anatomie : MCP (agent-outil) et A2A (agent-agent) | couche protocolaire |
| [`09-decouverte-registres-pile.md`](09-decouverte-registres-pile.md) · [`.html`](09-decouverte-registres-pile.html) | Ch. 9 — Découverte, registres, portabilité et pile protocolaire | couche protocolaire |
| [`10-transaction-infrastructure.md`](10-transaction-infrastructure.md) · [`.html`](10-transaction-infrastructure.html) | Ch. 10 — Transaction et infrastructure : AP2 et AGNTCY | couche protocolaire |
| [`11-modes-echec-risques-protocolaires.md`](11-modes-echec-risques-protocolaires.md) · [`.html`](11-modes-echec-risques-protocolaires.html) | Ch. 11 — Modes d'échec et taxonomie des risques protocolaires | couche protocolaire |

⚠ **Ces onze pièces ont été rédigées sur instruction d'auteur du 27 juillet 2026, avant le
franchissement des portes G-1, G-2 et G-3** du PRD §5, qui posent qu'aucun chapitre ne se rédige avant
le gel unique, la commande de décompte de référence et la refonte du socle. L'écart est **déclaré,
non dissimulé** : chaque pièce porte en tête son en-tête à cinq champs et, en clôture, une **note de
statut hors plan** qui énumère les conséquences de l'écart et les remontées qu'elle ouvre. Ces
sections **se retirent à la publication** — elles ne sont pas au TOC.

⚠ **Le statut de gouvernance a bougé le 27 juillet 2026, mais pas dans le sens qu'on croit.** À la
rédaction, les **sept portes** étaient ouvertes et les **huit décisions D-1 à D-8** à prendre. La
passe d'arbitrage du même jour en a consommé une partie — **deux portes, trois décisions** — sur
**remontée**, jamais depuis une pièce : la règle d'escalade du PRD (Annexe A) est intacte, *un
rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il remonte*, et c'est la remontée qui a
été traitée, non le plan corrigé sur place. ⚠ **Ce qui n'a pas bougé est ce qui compte** : le socle
consolidé reste à **zéro entrée**, **G-3 n'est pas entamée**, et *un brouillon écrit hors portes ne
franchit aucune porte — il en documente le coût.*

Trois conséquences valent d'être connues avant de lire ou de réutiliser une pièce :

- **Aucun énoncé n'y est central au sens de CA-IV-01.** L'Annexe B n'existe pas. Les faits venus du
  **Vol. I** résolvent en régime **[C]** (PRD §7.1) ; ceux venus des **Vol. II et III** conservent
  leur niveau **[A]/[B]/[C]** d'origine. ⚠ **Tant que G-3 n'est pas franchie, les identifiants restent
  préfixés de leur volume** — un « F-01 » nu est indécidable entre deux socles. ⚠ **Le gel unique n'y
  change rien** : *un fait re-daté n'est pas un fait promu.*
- ☑ **Les décomptes sont publiables depuis le franchissement de G-2** (27 juillet 2026). Chaque pièce
  porte désormais son **réel** mesuré par [`PRD/decompte.sh`](../PRD/decompte.sh) à côté de sa cible
  dérivée — voir la volumétrie du Livre ci-dessus, et l'écart de +43 % que la somme des cibles
  dérivées accusait.
- **Les renvois « ch. N » vers les Livres II à V sont des renvois de plan, non de texte** : ils
  résolvent contre l'entrée du TOC v0.24, aucun chapitre cible n'étant rédigé. Ils se re-vérifient
  contre le texte quand il existera. ⚠ **Les renvois internes au Livre I, eux, résolvent contre du
  texte** depuis que les onze pièces existent.

## Les treize remontées — soldées le 27 juillet 2026

Chacune a été **portée là où elle fait foi**, jamais déclarée close sur place : au
[PRD](../PRD/PRD.md) pour une décision d'auteur, au [TOC](../PRD/TOC.md) pour un réalignement de
plan, à l'appareil pour une dette d'outillage. Le détail de chaque clôture vit dans la note de statut
de la pièce qui l'avait ouverte.

| Remontée | Ouverte au | Issue |
|---|---|---|
| **R-IV-01** | ch. 1 | ☑ **D-7 tranchée — périmètre assumé et déclaré.** Aucune section n'est due ; les ch. 6, 37 et 48 sont **fermés** à cette matière |
| **R-IV-02** | ch. 1 | ☑ **close sans correction, sur constat** — les deux écarts étaient déjà soldés au plan à la v0.23 |
| **R-IV-03** | ch. 2 | ☑ **G-1** — cinq objets périssables repris à la source primaire, **tous inchangés**, réserves confirmées et datées |
| **R-IV-04** | ch. 3 | ☑ **G-1** — trois faits datés **confirmés** ; le cadre d'autorisation est toujours à l'état de projet |
| **R-IV-05** | ch. 3 | ☑ **appareil** — [`PRD/check-sieges.py`](../PRD/check-sieges.py), validé par mutation ; le siège du socle IAM porte enfin son marqueur |
| **R-IV-06** | ch. 4 | ☑ **G-1** — la parade (décrire le phénomène, non la liste des modèles) est **reconduite**, non levée |
| **R-IV-07** | ch. 5 | ☑ **G-1** — ⚠ **le seul fait changé de tout le Livre** : l'outil de mémoire est passé en disponibilité générale |
| **R-IV-08** | ch. 7 | ☑ **TOC v0.24, décision 8** — la thèse du ch. 7 est amendée ; le transfert de gouvernance est documenté |
| **R-IV-09** | ch. 7 | ☑ **appareil** — même contrôle que R-IV-05 ; **quatre défauts réels** trouvés au premier passage |
| **R-IV-10** | ch. 8 | ☑ **G-1** — réserve **confirmée** ; l'échéance est désormais **datée** (28 juillet 2026) au lieu d'être ouverte |
| **R-IV-11** | ch. 9 | ☑ **G-1, reconduite avec motif** — le motif est le **régime** de la source, non l'absence d'accès |
| **R-IV-12** | ch. 10 | ☑ **TOC v0.24** — relève v0.7 **consommée par extraction** ; lacune §10.9e **instruite** |
| **R-IV-13** | ch. 11 | ☑ **TOC v0.24** — thèse du ch. 11 requalifiée ; lacune §10.8 **requalifiée**, volet agent-agent **toujours ouvert** |

⚠ **Une distinction est née de R-IV-12 et R-IV-13, et elle vaut au-delà d'elles.** Dans les deux cas,
une **lacune déclarée du socle du Vol. II** se trouvait **comblée par le texte rédigé du Vol. I** —
l'autre source de la même ligne Fusion. *Ce ne sont pas des contradictions entre volumes* : « le socle
de A ne documente pas X » et « B documente X » sont logiquement compatibles, et l'énoncé du volume le
plus ancien **reste exact dans son périmètre**. La règle est désormais **écrite à l'Annexe C du TOC**
et s'impose à la collation de fond (porte **G-4**), qui balaiera systématiquement les lacunes
déclarées d'un volume contre le texte rédigé des deux autres. ⚠ **Aucun contrôle outillé ne le fera** :
c'est un contrôle de fond, et il est déclaré tel plutôt que promis à un script.

⚠ **Et deux verbes ne se confondent pas.** **Instruire** une lacune, c'est lui verser une **source
primaire nouvelle datée** — ce qu'a reçu §10.9e. **Requalifier** une lacune, c'est constater que sa
**couverture** a changé sans qu'aucune source nouvelle soit entrée — ce qui est arrivé à §10.8. *Une
lacune requalifiée reste une lacune ; elle change de motif, pas d'état.*

⚠ **Une correction a été apportée à une pièce déjà poussée** : le ch. 7 (§ 7.4.2, § 7.6, en-tête,
R-IV-08) écrivait « transfert de gouvernance annoncé, non vérifié au socle » alors que le Vol. I
*Monographie* §3.13.1 — **l'une de ses propres sources de fusion** — portait le fait daté du 28 avril
2026. La leçon est portée au [skill de rédaction](../../.claude/skills/chapitre-compendium/SKILL.md) :
*une pièce ne se rédige pas sur la seule source que le plan met en avant, mais sur l'intégralité de
son périmètre de fusion.*

### Ce que la clôture a coûté, et ce qu'elle a trouvé

Trois constats méritent d'être retenus avant d'ouvrir le Livre suivant.

1. **La re-datation n'a presque rien trouvé, et c'est le résultat.** Douze faits repris à la source
   primaire, **onze inchangés**. Les onze pièces avaient porté leurs réserves correctement : aucune
   ne présentait comme acquis ce qui ne l'était pas. Le seul écart va dans le sens **favorable** —
   une fonction produit passée en disponibilité générale rendait la pièce *trop prudente*, non fausse.
2. **Le contrôle inter-pièces a mordu au premier passage : six écarts, dont quatre réels.** Le ch. 3
   et le ch. 6 employaient la matière d'un siège **sans y renvoyer** ; et **deux sièges sur trois ne
   portaient aucun marqueur** dans le texte — invisibles à tout rédacteur aval. Les **deux faux
   positifs**, tous deux au ch. 1, venaient d'un ancrage trop large : le motif lisait l'**en-tête**,
   qui *déclare* le balayage au lieu de porter la matière. *Ce qu'aucun outil ne regarde finit par
   diverger — et un contrôle bruyant est un contrôle ignoré.*
3. ⚠ **Une source secondaire n'est pas un substitut de la source normative, même du même émetteur.**
   Le billet d'annonce d'une révision protocolaire décrivait un *durcissement* là où le journal des
   changements portait une **dépréciation** : une correction fondée sur le billet aurait **cassé** un
   énoncé exact du ch. 8. La vérification est allée jusqu'au document qui fait autorité, et c'est ce
   qui l'a sauvé.

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
n'a été copiée ici. Le `.html` se **régénère**, il ne s'édite pas :

```bash
python .claude/skills/chapitre-compendium/scripts/rendre-piece.py "2 - Compendium/Livre I/<pièce>.md"
```

```bash
python .claude/skills/chapitre-compendium/scripts/verifier-piece.py "2 - Compendium/Livre I/<pièce>"
```

Puis les trois contrôles du volume, chacun **exécuté seul**, sortie 0 exigée :

```bash
python "2 - Compendium/PRD/check-toc.py"
```

```bash
python "2 - Compendium/PRD/check-sieges.py"
```

```bash
sh "2 - Compendium/PRD/decompte.sh" --verifier
```

⚠ **Le vérificateur ne se tuyaute jamais dans un enchaînement `&&`** : le code de sortie du dernier
maillon masquerait son échec. La faute a déjà été commise sur le ch. 6, poussé avec un gras non
converti alors que le contrôle [8] échouait.

⚠ **Ce n'est pas une page de publication en ligne.** Les deux `index.html` du dépôt ont été
supprimés le 22 juillet 2026 (commit `fd8f1be`) parce qu'ils annonçaient des adresses GitHub Pages
fausses ; ces fichiers ne les rétablissent pas, ne portent aucune balise `canonical` ni `og:url`, et
n'impliquent aucune activation de Pages.

## Ce que le Livre couvre — et ce qu'il ne couvre pas

Chaque pièce suit section par section la table des matières détaillée de son entrée au TOC, et
respecte sa table de couverture. Cinq arbitrages de périmètre valent d'être connus, parce qu'ils
**cassent la table de couverture d'un chapitre si on les défait** :

| Matière | Destination | Régime |
|---|---|---|
| Exécution durable, pipelines, orchestration agentique (Vol. I §1.6.3) | ch. 22 (Livre III) | déplacé **en entier** |
| Déclinaison agentique du maillage (Vol. I §1.3.4, part agentique) | ch. 37 (Livre IV) | **scindé**, socle transposable conservé au ch. 1 |
| Tendances agentiques 2024-2026 (Vol. I §1.11) | — | coupe assumée |
| Découverte et registres, **versant identité et conformité** (Vol. I §3.4) | ch. 15 (Livre II) | **partage déclaré** avec le ch. 9 |
| Triade de conditions, modèle de menace, vecteurs d'attaque (Vol. I §2.10, §3.10.2) | ch. 19 (Livre II) | partent **en entier** ; le ch. 11 n'en traite que l'**amplification** |

**Trois sièges sont posés dans ce Livre pour toute la somme**, et ne se reconstruisent nulle part
ailleurs : l'**encadré de désambiguïsation à quatre branches** (garde-fou R-8) au **ch. 7 § 7.5** ; le
**socle IAM** au **ch. 3** ; la **mécanique de la fusion de l'ACP protocolaire** au **ch. 8 § 8.5.1**,
sa **portée de risque** étant au **ch. 10 § 10.5**.

## Avant d'ajouter une pièce ici

**Le [skill de projet `chapitre-compendium`](../../.claude/skills/chapitre-compendium/SKILL.md) porte
la procédure complète** — portes, lectures préalables, squelette, conventions de renvoi, gabarit HTML
et vérificateur validé par mutation. Ce qui suit en est le rappel minimal.

1. Lire le [`CLAUDE.md`](../CLAUDE.md) du compendium — il porte le plafond dur de cinquante
   chapitres, le protocole d'insertion et les pièges propres au `TOC.md`.
2. Reprendre l'entrée du chapitre au [`TOC.md`](../PRD/TOC.md) : thèse, sections, ligne Fusion,
   table détaillée, table de couverture. **Chaque entrée du TOC est le cahier des charges de son
   chapitre** ; ce répertoire n'en contient aucune copie.
3. **Lire l'intégralité du périmètre de fusion**, pas la seule source que le plan met en avant —
   c'est la leçon de R-IV-12 et de R-IV-13.
4. Porter l'en-tête à cinq champs du PRD §6 — Statut, Date de gel, Socle mobilisé, Garde-fous
   balayés (**y compris à zéro occurrence**), Volumétrie cible — puis la thèse citée depuis le TOC.
5. Écrire le `.md` et le `.html` **dans la même passe**, faire passer les huit contrôles, et les
   committer ensemble.
