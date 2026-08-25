# Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique

Répertoire de rédaction du **Livre I** du compendium *Interopérabilité et Orchestration en Entreprise Agentique* (Vol. IV). Il ne porte
aucune décision, aucun socle et aucun garde-fou propre : la spécification de contenu est le
[`PRD/TOC.md`](../PRD/TOC.md), la gouvernance de la rédaction le [`PRD/PRD.md`](../PRD/PRD.md).
⚠ **Versions courantes relevées en tête des deux fichiers le 8 août 2026 : TOC v0.33, PRD v0.17** ;
*les onze pièces de ce dossier ont été rédigées et arbitrées contre le **TOC v0.25** et le **PRD
v0.9**, et une étiquette de version ne se redate pas pour suivre le numéro courant.*
⚠ *Les renvois « TOC v0.24 » de ce fichier et de ses pièces sont des **constats datés** — ce que
la passe du Livre I a fait, à la version où elle l'a fait — et ne se corrigent pas.* ⚠ **Une exception,
et une seule, depuis la passe de correction du 28 juillet 2026** : les **blocs de thèse des ch. 7, 10
et 11** portent « citée depuis le TOC v0.28 », parce qu'ils **ont été re-cités à cette version** ; les
huit autres restent à v0.23, qui est la version d'où ils ont été copiés et où leur thèse n'a pas
bougé. *Une étiquette de citation date la copie, pas la lecture du fichier.* En cas d'écart entre une pièce de ce dossier et le TOC, **le TOC prime** — sauf déviation
fondée, qui se déclare (décision 8 du TOC) et se remonte, jamais se corrige au plan depuis ici.

## ⚠ Le dépôt est CLOS depuis le 8 août 2026 — et « clos » n'est ni « terminé » ni « publiable »

La décision d'auteur **D-13** ([PRD **v0.17** §16](../PRD/PRD.md), [TOC **v0.33**](../PRD/TOC.md))
**clôt la passe de révision ouverte par D-11** le 30 juillet 2026 — *close, non achevée* — et
**clôt le dépôt entier**. **Trois conséquences pour ce Livre.** *(1)* **Aucune passe n'est plus
prévue**, ni de rédaction, ni de révision, ni d'appareil : ce qui suit décrit un état **définitif**.
*(2)* ⚠ **Rien n'est levé, et rien n'est soldé** : le régime de D-10 ci-dessous est inchangé et
devient définitif, les quatre portes dérogées le restent, **CA-IV-11 et CA-IV-13 demeurent non
satisfaits**. *(3)* ⚠ **Ce qui était dû devient un manque définitif, non une conformité** — *une
dette qu'on cesse de suivre reste une dette ; elle change seulement de nom.* Le domaine non exécuté
est nommé ligne à ligne au [PRD §16.2](../PRD/PRD.md). ⚠ **Le volume a été renommé le même jour**
(décision 20 du TOC) : il s'est appelé *« La somme agentique »* du 23 juillet au 8 août 2026.

## ⚠ Le volume est ARRÊTÉ depuis le 29 juillet 2026 — et « arrêté » n'est ni « terminé » ni « publiable »

La décision d'auteur **D-10** ([PRD **v0.15** §14](../PRD/PRD.md), [TOC **v0.31**](../PRD/TOC.md)) arrête
le compendium au statut **RÉVISION FINALE**, sous un **régime de diffusion en bibliothèque personnelle** :
lecture par l'auteur, **aucune mise à disposition d'un tiers**, aucun dépôt public, **aucune
opposabilité**. **Trois conséquences pour ce Livre.** *(1)* **Ses onze chapitres sont arrêtés dans leur
état du 29 juillet 2026** — plus aucune passe de rédaction n'est prévue ; une faute se corrige encore,
mais la correction **rouvre la passe** : elle se recompose (`bash build/build-pdf.sh` depuis
`2 - Compendium/`) et se déclare. *(2)* ⚠ **Rien de ce qui suit n'est levé** : les écarts de portes de ce
Livre restent écrits, et **G-1 résiduel, G-4 fond, G-5 balayage et G-6 lots sont clos POUR CE SEUL RÉGIME
par dérogation nommée**, leur résidu entier — *la dérogation tombe à la première diffusion et rouvre tout
ce qu'elle couvrait*. *(3)* ⚠ **CA-IV-11 et CA-IV-13 sont dérogés, non satisfaits** : il n'y a toujours
pas de relecteur distinct du rédacteur, et **aucun énoncé n'est central** au sens de CA-IV-01. *Ne jamais
écrire « conforme », « publiable » ni « terminé » — écrire « arrêté », et renvoyer au PRD §14.* Les pièces
sont composées dans [`Compendium.pdf`](../Compendium.pdf) (**1 000 p.**, cible calée le 9 août 2026 ; 1 114 auparavant) : *composer n'est pas publier.*

## ⚠ État : le Livre est rédigé, arbitré, et toujours non publiable

Le Livre I compte **onze chapitres** au plan (ch. 1-11), en deux mouvements — les fondements
(ch. 1-6), la couche protocolaire agentique (ch. 7-11). **Les onze sont rédigés** ; ils l'ont été
**hors portes**, et ils restent en **brouillon non publiable**.

⚠ **Ce qui a changé le 27 juillet 2026, et ce qui n'a pas changé.** La passe d'arbitrage du même jour
(PRD v0.8, TOC v0.24) a **soldé les treize remontées** que la rédaction avait ouvertes et **franchi
deux des sept portes**. Le tableau ci-dessous est l'état exact, et il se lit dans les deux sens :

| | État au terme de la passe d'arbitrage du 27 juillet 2026 |
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

⚠ **Ce tableau est un constat daté et deux de ses lignes ont été DÉPASSÉES depuis — le rappel est du
8 août 2026, il ne réécrit rien.** ☑ **La porte G-3 est franchie le 28 juillet 2026** et le socle
consolidé ne compte plus zéro entrée mais **159**, `S-001`…`S-159`
([`PRD/socle-consolide.md`](../PRD/socle-consolide.md) ; `python PRD/check-compendium.py` → *P1-P8,
sortie 0*). ☑ **La table `SIEGES` porte 26 sièges sur 50 pièces** (`python PRD/check-sieges.py`).
⚠ **Rien d'autre n'a bougé** : *aucun énoncé n'est central au sens de CA-IV-01, CA-IV-11 et CA-IV-13
demeurent non satisfaisables, et les pièces restent un brouillon arrêté, non publiable* — **une porte
franchie n'est pas un ouvrage recevable.**

⚠ **Une obligation reste due, et elle n'est pas une porte : CA-IV-13, la relecture adversariale.** Le
PRD exige que chaque pièce soit relue **par un relecteur distinct du rédacteur, chargé de réfuter**.
La passe du 27 juillet 2026 a produit des contrôles **mécaniques** (huit par pièce, plus les trois du
volume) et une **re-datation à la source primaire**, qui ont trouvé de vrais défauts — mais elle a
été conduite par la même main que la rédaction. **CA-IV-13 n'est donc pas satisfaite**, et rien dans
ce dossier ne doit être lu comme si elle l'était. *Un contrôle mécanique n'est pas une réfutation, et
se relire soi-même n'est pas être relu.*

⚠ **Le Vol. IV n'est pas requalifié pour autant.** Il demeure un cadrage au regard du dépôt : la veille
technologique ne le décrit pas autrement, et **la veille ne se corrige
jamais** — sa réf. [220] décrit un cadrage sans chapitre, et cela reste vrai à sa date.

### Volumétrie réelle — publiable depuis G-2

☑ **Mesure du jour : 72 483 mots** de corps pour les onze pièces, relevés le **10 août 2026** par
[`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte du volume — contre une enveloppe
de Livre de **65 000** au TOC, soit **+11,5 %**. *C'est le seul cardinal de cette section qu'on
reproduise en exécutant la commande sur ce dossier.*

⚠ **Le chiffre longtemps publié ici — 64 750 mots — ne se reproduit plus, et il était déjà démenti
par les pièces de ce dossier. Trois écarts, qui se déclarent séparément.**

1. ⚠ **Il date du 27 juillet 2026, non du 28.** Le champ *Volumétrie cible* du
   [ch. 10](10-transaction-infrastructure.md) l'écrit lui-même : *« le réel du Livre est de 64 750
   mots […] au commit du 27 juillet 2026 »*, puis *« ce total de Livre n'est pas re-mesuré ici »*.
   **Le Livre n'a jamais été re-mesuré à son propre grain à la passe du 28.**
2. ⚠ **Les onze pièces le contredisent, et elles suffisent à l'établir sans mesure extérieure** : la
   somme des cardinaux que **leurs onze en-têtes déclarent** vaut **71 980 mots**. Le ch. 10 y porte
   **7 036 → 7 548, soit +512**, là où la reconstruction publiée ici imputait **+32**. *Cette
   reconstruction — « +139 mots sur sept pièces », ch. 3 (+13), ch. 6 (+33), ch. 7 (+6), ch. 8 (+4),
   ch. 9 (+4), ch. 10 (+32), ch. 11 (+47) — est **retirée** : un total que les pièces démentent n'est
   pas un constat daté, c'est une erreur datée.*
3. **Le solde — 71 980 → 72 483, soit 503 mots — est postérieur au 28 juillet.** Les **figures du
   barème A ont été posées dans les pièces le 31 juillet 2026** et la légende de chacune entre au
   corps que la commande mesure ; *les onze pièces de ce Livre en portent au moins une.*

⚠ **Les chiffres publiés hors de ce dossier — audit du 28 juillet 2026 (§2 et §4.2), et tout décompte
agrégé du compendium — sont périmés d'autant** : l'écart est **remonté**, il n'est pas corrigé depuis
ici.

⚠ **Ce que la volumétrie établit, en revanche, n'a pas bougé : les cibles individuelles étaient
fausses.** Chaque pièce a **dérivé** sa cible de l'enveloppe du Livre, personne n'ayant additionné les
dérivations : leur somme atteint **93 000 mots**, soit **+43 %** de l'enveloppe qu'elles prétendaient
toutes respecter. ⚠ **Les écarts individuels, re-calculés au 10 août 2026, vont de −45,8 % (ch. 6) à
+8,5 % (ch. 11)** — *le « −55,5 % (ch. 6) à +0,5 % (ch. 10) » publié ici ne se retrouve à aucune
mesure du dossier, ni au jour, ni aux cardinaux que les pièces déclarent.* *C'est la cible dérivée qui
était fausse, non la pièce qui est courte* — et l'écart se documente, il ne se corrige ni par
amputation ni par gonflement.

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
2026. La leçon est portée au skill de rédaction :
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

## La passe de correction du 28 juillet 2026 — huit constats soldés, un partiel, quatre écarts remontés

⚠ **Sur instruction d'auteur, les onze pièces ont été corrigées le 28 juillet 2026 en réponse à
l'audit des cinq Livres** (`audit.md`, section 4 pour le Livre I ; constats transversaux T-1, T-2 et
T-4). ⚠ **`audit.md` n'est pas au dépôt** : il n'y a jamais été versé, et *le nom est conservé parce
qu'il date le constat, non parce qu'il désigne un fichier qu'on puisse ouvrir ici.* ⚠ **Rien de ce qui suit ne requalifie le Livre** : les portes n'ont pas bougé, le socle
consolidé compte toujours **zéro entrée**, **CA-IV-13 reste insatisfaite** — *une passe de correction
n'est pas une relecture adversariale, et se corriger soi-même n'est pas être relu.* Les onze pièces
demeurent des **brouillons non publiables**, et l'audit qui les a relevées **ne fait pas autorité** :
c'est un constat daté, dont les issues appartiennent à l'auteur.

**Trois arbitrages d'auteur commandent la passe, et ils ne se rediscutent pas.**

1. **La re-citation d'une thèse suit son réalignement.** Le bloc de thèse d'une pièce cite le plan ;
   quand le plan est réaligné, la citation se **reprend par copie littérale**, jamais par re-frappe.
   Le bloc qui documentait le désalignement d'origine est **conservé et reformulé au passé** — *un
   défaut soldé se raconte, il ne s'efface pas.*
2. ⚠ **Règle neuve et opposable sur les décomptes d'en-tête.** *Un décompte d'occurrences déclaré au
   champ « Garde-fous balayés » porte sur le **marqueur littéral de l'identifiant** — « R-14 »,
   « R-02 », « F-01 » — dans le **corps** de la pièce, en-tête et note de statut exclus ; il se
   re-mesure au commit.* Un garde-fou appliqué **sans identifiant écrit** — les métriques
   auto-déclarées — se déclare désormais par son **domaine balayé, sans cardinal** : *mieux vaut un
   domaine vérifiable qu'un nombre faux.* La règle est inscrite en tête du champ des **onze** pièces
   et les cardinaux y ont tous été re-mesurés par balayage exhaustif.
3. **L'attribution ne s'anonymise jamais.** La parade de péremption reste permise pour les
   dénominations commerciales et les versions, mais **trois choses en sortent** : l'attributeur d'une
   métrique ou d'une affirmation ; l'auteur et la date d'un instrument repris ; l'identifiant d'une
   source qu'un lot doit instruire. *Une métrique dont l'attributeur est anonyme n'est plus
   remontable par le lecteur — et le régime du volume tient tout entier à ce qu'elle le reste.*

### Ce qui a été corrigé, par constat

| Constat | Objet | Correction |
|---|---|---|
| **I.1** | § 10.5.3 renvoyait la lacune PRD Vol. II §10.7 « jusqu'au **ch. 21** » | ☑ **ch. 49**, vérifié contre le TOC et contre le **ch. 7 § 7.5**, siège de l'encadré, qui écrivait déjà « renvoyée au ch. 49 ». *Le ch. 21 du compendium est l'horloge post-quantique ; le renvoi visait le chapitre source du Vol. II, et un renvoi nu sans marqueur de document est la classe que la décision 7 proscrit.* |
| **I.2** | § 6.5.2 : renvoi cassé « ch. 8 § » sans numéro | ☑ **ch. 8 § 8.3.2**, cible vérifiée sur pièce (« Registres, passerelles et découverte d'entreprise ») |
| **I.3** | thèse du ch. 10 amputée de sa clause médiane | ☑ **re-citée par copie littérale** depuis le TOC v0.28 : « — le socle établit qu'AP2 est un protocole compagnon d'A2A, rien de plus sur sa centralité ». *La clause était restituée en substance au corps ; la citation déclarée verbatim, elle, était fausse.* |
| **I.4** | thèses des ch. 7 et 11 figées à la v0.23 | ☑ **re-citées depuis le TOC v0.28** — ch. 7 (amendement R-IV-08 : le transfert d'AP2 à la FIDO Alliance est documenté), ch. 11 (requalification R-IV-13 : « le socle **du Vol. II** »). Les blocs de désalignement sont **reformulés au passé**, et **les corps qui commentaient la forme ancienne le sont aussi** — ch. 7 (note de statut) et **ch. 11 § 11.4.2**, qui écrivait encore « la thèse citée en tête est fausse de la somme » |
| **I.5** | cardinaux et localisations d'occurrences inexacts | ☑ **onze pièces balayées**, pas seulement les quatre nommées : voir la table ci-dessous |
| **I.6** | ch. 1 § 1.0.2 : « Deux termes ici » contre « les trois premiers » | ☑ titre de l'encadré aligné sur le corps — **« Trois termes ici, quatre à l'avant-propos »**. ⚠ *La sous-entrée 1.0.2 du TOC écrit « les deux premiers » : l'écart est **remonté**, non corrigé.* |
| **I.7** | numérotation des tableaux interrompue aux ch. 10-11 | ☑ **Tableau 10.1 à 10.4** et **Tableau 11.1 à 11.5**, légendes conservées mot pour mot |
| **I.8** | ch. 4 : « autonomie graduée » comptée sous R-8 du Vol. II | ☑ la ligne est **retirée** : le corps ne porte **aucun marqueur R-8**, et les deux définitions concordantes de la somme — ch. 7 § 7.5 (R-8 = collision « ACP ») et ch. 3 § 3.3.1 (R-13 = les quatre termes proscrits) — rattachent l'occurrence au seul **R-13 du Vol. III** |
| **I.10** | attributions anonymisées | ☑ **partiellement** — les trois catégories de l'arbitrage 3 seulement (voir plus bas) ; la parade demeure pour le reste |

### Les décomptes re-mesurés — avant → après

Balayage exhaustif des onze pièces, marqueur littéral dans le corps. **Neuf pièces sur onze portaient
au moins un cardinal, une localisation ou une plage de zéros faux ; deux étaient exactes** — le ch. 1
et le ch. 5. *Le domaine de balayage est déclaré parce qu'un cardinal d'écarts sans domaine est un
relevé, pas une couverture.*

| Pièce | Correction |
|---|---|
| **Ch. 2** | R-02 sorti de la plage « zéro occurrence » : **le marqueur figure une fois** (§ 2.4.1), sans déclencher le garde-fou |
| **Ch. 3** | R-02 **cinq → quatre** ; R-13 sorti de la plage « zéro » (**un marqueur**, § 3.3.1) ; *le § 3.2.2 porte un marqueur pour deux mécanismes — le cardinal compte les marqueurs* |
| **Ch. 4** | R-8 **une → zéro** (constat I.8) ; métriques auto-déclarées : cardinal remplacé par le domaine (§ 4.0.1) |
| **Ch. 6** | R-8 **deux → une** ; R-13 **deux → une** ; métriques : domaine § 6.1.1, § 6.2, § 6.5.2, sans cardinal |
| **Ch. 7** | R-1 : localisation **§ 7.4.2 → § 7.4.1** ; R-8 **huit → deux** (les huit comptaient les **emplois du sigle**, non les marqueurs) ; R-13 **deux → une** ; R-14 **trois → deux** ; métriques **quatre → domaine § 7.6 seul**, le § 7.3 n'en portant aucune |
| **Ch. 8** | F-01 **six → quatre** ; R-8 **cinq → une** ; R-13 **cinq → une** ; R-02 : **§ 8.1.4 ajouté** à la localisation ; R-14 **quatre → trois**, le § 8.8 étant la note de statut ; métriques : domaine § 8.4.2 et § 8.6.3 |
| **Ch. 9** | R-8 **trois → une** ; R-13 **trois → une** ; R-14 **cinq → quatre** (§ 9.6 = note de statut) ; ⚠ **le superlatif « le chapitre du Livre le plus dense en énoncés d'absence » est retiré** — les ch. 10 et 11 en portent sept |
| **Ch. 10** | R-8 **cinq → deux** ; R-13 **cinq → deux** ; R-02 **trois → quatre** (§ 10.3.3 omis) ; **R-14 six → sept** (§ 10.2.1 omis) ; métriques : § 10.2.2 **→ § 10.2.3** |
| **Ch. 11** | F-01 **sept → quatre** ; R-14 : « le plus grand nombre du Livre » **→ à égalité avec le ch. 10**, sept chacun |

⚠ **Une leçon de cette table dépasse le Livre** : *les décomptes faux ne l'étaient presque jamais par
négligence, mais parce que deux objets différents portaient le même nom* — les **emplois d'un sigle**
comptés comme des occurrences de son garde-fou, la **note de statut** comptée dans le corps, une
**application** interprétée comptée comme un marqueur. **Aucun des quinze contrôles du volume ne
rapproche un en-tête du corps qu'il décrit** ; c'est une dette d'appareil, et elle est déclarée.

### Attributions rendues nominatives

| Lieu | Avant | Après |
|---|---|---|
| ch. 6 § 6.2, ch. 7 § 7.6 (deux fois), ch. 8 § 8.4.2, ch. 9 § 9.2.5, ch. 10 § 10.1.2 et § 10.2.1 | « la fondation faîtière », « la fondation gestionnaire », « les organisations promotrices » | **la Linux Foundation** — attributeur des métriques d'adoption, que le TOC nomme dans la thèse même du ch. 7 |
| ch. 6 § 6.5.2 | « attribuée ici à la source qui la rapporte » ; réserve de la règle de non-cumul sans attributeur | **Debenedetti et coll. (2025)**, sur le banc **AgentDojo** ; **Meta AI, 31 octobre 2025** — les deux vérifiés à la source de fusion (Vol. I *Monographie* §2.10) |
| ch. 3 § 3.1.2 | « un référentiel largement adopté » | l'**OWASP API Security Top 10**, publié par la fondation **OWASP** — l'intitulé de la section le nommait déjà ; le corps ne le nommait pas |

⚠ **Ce qui n'a pas été re-nommé l'est délibérément.** La parade de péremption demeure pour les
dénominations commerciales, les produits et les versions ; seules les **trois catégories** de
l'arbitrage 3 en sortent. *Anonymiser un produit protège d'une péremption ; anonymiser un attributeur
supprime la vérifiabilité qui fonde le régime de preuve — ce n'est pas le même geste.*

### Ce qui est remonté, et non corrigé

*Un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il **remonte**.* Quatre écarts
relèvent d'eux et sont laissés intacts :

1. ⚠ **La sous-entrée 1.0.2 du TOC écrit « les deux premiers termes sont éprouvés ici »** ; le corps
   du ch. 1 en éprouve **trois** (découplage, contrat, évolution — l'évolution au § 1.1.4), et le
   § 1.7 le confirme. La pièce a été alignée sur elle-même ; **le plan reste à réaligner** au titre de
   la décision 8.
2. ⚠ **La volumétrie du Livre est périmée partout où elle a été publiée.** ⚠ *Le couple « 64 611 →
   64 750 » qui figurait ici est **retiré** : les onze en-têtes somment à **71 980**, et la mesure du
   10 août 2026 donne **72 483** (volumétrie ci-dessus).* Les chiffres publiés hors de ce dossier —
   audit §2 et §4.2, agrégat du compendium — sont périmés d'autant, et **ne se corrigent pas depuis
   ici**.
3. ⚠ **La date de l'instrument repris au ch. 3 § 3.1.2 n'est pas portée** : le référentiel OWASP est
   désormais nommé, mais **aucune version datée ne figure au corpus de la pièce**, et *ce qui n'a pas
   été vu à la source ne s'écrit pas comme vu*. L'arbitrage 3 demande l'auteur **et** la date ; seul
   l'auteur est versé. **À instruire à la source primaire.**
4. ⚠ **Les constats I.9 et I.10a-b ne sont pas soldés, et c'est un choix de périmètre.** La triple
   restitution paraphrasée de la mécanique de la fusion de l'ACP (ch. 7 § 7.3 et § 7.4.1, ch. 10
   § 10.5.2) hors de son siège du ch. 8 § 8.5.1 relève d'un **contrôle de fond** qu'aucun motif de
   `check-sieges.py` ne voit ; le réalignement des tables détaillées du TOC sur les sous-sections
   réellement écrites (ch. 5, 10, 11) et sur les intitulés reformulés (ch. 8 § 8.5) est **une passe de
   plan**, hors mandat d'une passe de correction de pièces.

### Contrôles exécutés — 28 juillet 2026

Chacun **seul**, jamais tuyauté dans un `&&`, le code de sortie du dernier maillon masquant l'échec
des précédents.

- `verifier-piece.py` sur les **onze** pièces : **sortie 0** pour chacune, les huit contrôles passent ;
- les onze `.html` **régénérés** par `rendre-piece.py` depuis le `.md` corrigé, au même geste — *le
  rendu se génère, il ne se recopie pas* ;
- `PRD/decompte.sh` sur les onze pièces — ⚠ **le total de « 64 750 mots » qui figurait ici est
  retiré** : *chaque en-tête porte sa propre mesure et les onze somment à **71 980**, jamais à
  64 750 ; aucun total de Livre n'a été reporté dans les pièces à cette passe* (volumétrie ci-dessus) ;
- `PRD/check-sieges.py` : **sortie 0** — « les 12 sièges tiennent sur 50 pièces (S1-S5) ». ⚠ **Domaine
  déclaré** : l'arbre de travail au 28 juillet 2026, **où des passes sœurs éditaient simultanément les
  Livres II à V** ; le contrôle porte donc sur un corpus dont ce dossier n'écrit qu'un cinquième, et
  *seul le corpus que le commit produit fait foi.*

## Les deux formats

Chaque pièce existe en **deux rendus**, versionnés ensemble — ⚠ **et depuis la purge du 29 juillet 2026 ils ne portent plus la même matière** :

- le **`.md`** — la source ; c'est lui qui fait foi, et **lui seul porte l'appareil** : en-tête à cinq champs, thèse citée depuis le TOC, note de statut ;
- le **`.html`** — page autonome à thème sombre orange, sans aucune ressource externe (CSS et script
  intégrés, aucune police ni image distante), **prose justifiée avec césure automatique**,
  navigation de chapitre, barre de progression, styles d'impression. Elle se lit hors ligne par
  simple ouverture dans un navigateur. ⚠ La césure s'appuie sur l'attribut `lang="fr-CA"` du
  document : le retirer désactiverait la coupure des mots **sans prévenir**, et une justification
  sans césure creuse des lézardes dans une colonne de cette largeur. Titres, légendes et navigation
  restent au fer à gauche — les justifier y produirait des trous.

⚠ **Le `.html` est un rendu, pas une seconde source.** Toute correction se fait dans le `.md` puis
se reporte dans le `.html` au même commit — jamais l'inverse, jamais l'un sans l'autre — même règle
que « PDF versionné avec sa source » ailleurs au dépôt. Le compendium n'a
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

**Le skill de projet `chapitre-compendium` portait
la procédure complète** — portes, lectures préalables, squelette, conventions de renvoi, gabarit HTML
et vérificateur validé par mutation. ⚠ **Il n'est plus au dépôt depuis le 31 juillet 2026** (commit
`41666d0`), non plus que ses scripts : les deux invocations ci-dessus ne résolvent donc plus, et ce qui
suit est le seul rappel qui subsiste.

1. Tenir le **plafond dur de cinquante chapitres**, le protocole d'insertion et les pièges propres
   au `TOC.md`.
2. Reprendre l'entrée du chapitre au [`TOC.md`](../PRD/TOC.md) : thèse, sections, ligne Fusion,
   table détaillée, table de couverture. **Chaque entrée du TOC est le cahier des charges de son
   chapitre** ; ce répertoire n'en contient aucune copie.
3. **Lire l'intégralité du périmètre de fusion**, pas la seule source que le plan met en avant —
   c'est la leçon de R-IV-12 et de R-IV-13.
4. Porter l'en-tête à cinq champs du PRD §6 — Statut, Date de gel, Socle mobilisé, Garde-fous
   balayés (**y compris à zéro occurrence**), Volumétrie cible — puis la thèse citée depuis le TOC.
5. Écrire le `.md` et le `.html` **dans la même passe**, faire passer les huit contrôles, et les
   committer ensemble.
