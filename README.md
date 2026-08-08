# Interopérabilité, orchestration et entreprise agentiques — un triptyque, sa veille et sa somme

Travaux d'André-Guy Bruneau sur les agents d'IA en écosystème d'entreprise, et plus
particulièrement en services financiers. Le dépôt réunit **trois monographies** conçues en
progression — les protocoles, puis les cadres réglementaires, puis l'organisation qui doit les
faire tenir ensemble —, **une veille technologique autonome** qui les traverse et les tient à jour,
et **un compendium** qui les refond en un seul ouvrage — arrêté en révision finale, non publiable.

> **Où entrer.** Le lecteur pressé lit la [veille technologique](Veille%20Technologique.md) : c'est
> l'état de l'art le plus récent (édition d'août 2026, faits gelés au 29 juillet), et le seul document publié qui cite les volumes
> du dépôt. Le lecteur méthodique suit l'ordre des volumes, du général au spécifique. Le compendium
> se feuillette depuis le 29 juillet 2026 — [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf),
> **1 114 pages** re-mesurées le 8 août 2026, au format Letter depuis la refonte typographique du
> 31 juillet 2026 (921 pages au format 155 × 235 mm auparavant) —, et il est **arrêté en révision finale pour la bibliothèque personnelle de
> l'auteur** le même jour. Ses cinquante chapitres restent un **brouillon écrit hors portes** : il se
> lit, il ne fait pas foi, et il ne se diffuse pas. *Arrêter n'est ni terminer ni publier.* Il se
> **feuillette aussi à l'écran** depuis le 4 août 2026 —
> [`Compendium.html`](2%20-%20Compendium/Compendium.html), appareil de lecture d'**un seul fichier
> sans dépendance externe**, dérivé des cinquante `.md` et **sans plus d'autorité que le PDF**.

## État au dépôt — arrêté le 29 juillet 2026, re-mesuré le 8 août 2026

Le dépôt est arrêté dans cet état. Les chiffres ci-dessous ont été **re-mesurés sur pièce le 8 août
2026**, jamais recopiés d'un autre document ; les commandes qui les produisent sont données plus bas
(« Construire les PDF », « Ce qui reste vivant »). ⚠ *La pagination est prise par lecture du `/Count`
de l'objet `/Type /Pages` : `pypdf`, que ce fichier citait comme instrument, n'est pas installé.*

| Livrable | Rendu mesuré (`/Count`) | Pièces | Appareil de contrôle |
|---|---|---|---|
| Veille technologique | **161 p.**, 269 références | 14 sections, 15 tableaux, 25 questions ouvertes | `python check-veille.py` → **sortie 0** |
| Vol. I — *Interopérabilité* | **569 p.** | 7 chapitres + 7 bibliographies + Annexe B, **28 diagrammes** | — (vérification adverse des citations) |
| Vol. II — *L'autonomie encadrée* | **387 p.** | **29 pièces** + registre de gel, socle de 46 entrées | grille CA-1…CA-8 |
| Vol. III — *L'entreprise agentique* | **427 p.** | **34 pièces** + registre de gel, **30 rapports** de vérification | CA-01…CA-14, 15 remontées ouvertes |
| Vol. IV — *La somme agentique* | **1 114 p.** *(re-mesuré le 8 août 2026 ; format Letter depuis la refonte du gabarit du 31 juillet 2026, 921 p. auparavant)* | **50 chapitres** en 5 Livres + **2 annexes** (hors plan : 159 entrées ; **Annexe I** : 1 154 entrées), socle de **159 entrées** | `check-toc.py` (C1-C15), `check-sieges.py` (**26 sièges / 50 pièces**), `check-compendium.py` (**P1-P8**), `decompte.sh --verifier` → **sortie 0** pour les quatre |

Gouvernance du Vol. IV à sa date d'arrêt : **TOC v0.31**, **PRD v0.15**, décision d'auteur **D-10**.
⚠ **L'arrêt a été rouvert depuis, et ce tableau ne le portait pas** : le 30 juillet 2026, la décision
d'auteur **D-11** (PRD **v0.16** §15, TOC **v0.32**) **rouvre D-10** pour une **passe de révision**,
sur un **rapport d'arbitrage externe** qui conclut à une *révision majeure — accepté sur le fond, non
diffusable en l'état*. Le statut **RÉVISION FINALE — bibliothèque personnelle est maintenu pendant
toute la durée de la passe**, et la passe **est ouverte**. Gouvernance courante, relevée sur pièce le
8 août 2026 : **TOC v0.32**, **PRD v0.16**, **D-11**.

⚠ **Ce que ce dépôt n'arrête pas, et qu'il faut lire avant d'en tirer quoi que ce soit.** *(a)* **Deux
volumes ne sont pas publiables et le déclarent** : le Vol. III (quinze remontées ouvertes R-G-43 à
R-G-57, dette de vote sur F-92 et F-96) et le Vol. IV (**arrêt rouvert par D-11**, non terminé —
quatre portes closes par dérogation nommée pour le seul régime de bibliothèque personnelle,
**CA-IV-11 et CA-IV-13 non satisfaits** faute de relecteur tiers). *Arrêter n'est ni terminer ni
publier, et rouvrir un arrêt ne rapproche d'aucun des deux.* *(b)* **Deux décisions restent à l'auteur,
et aucune n'est du ressort d'une passe documentaire** : poser (ou retirer des documents de gouvernance)
l'étiquette git `mono-v1.0` du Vol. II — `git tag -l` est vide, et **quatre documents de gouvernance et
dix-sept pièces** l'annoncent comme posée ; et déposer une licence à la racine du dépôt, qui n'en porte
aucune — seul le Vol. I en a une. ⚠ *La troisième décision que ce fichier réservait à l'auteur — retirer
du suivi git trois fichiers de bytecode Python — **n'a plus d'objet** : `git ls-files | grep pycache`
n'en rend **aucun**, `.gitignore` les couvre, et le reliquat était périmé.* *(c)* **Les reliquats
listés en fin de fichier sont désormais ceux qui restent après correction**, et ils sont d'un autre
genre : décisions d'auteur, contradictions à arbitrer, renvois dont la réparation exigerait une
information absente du dépôt. *(d)* **La veille n'est pas rattrapée** : ses références [217], [219] et
[220] décrivent l'état de leurs sources au gel de leur édition, et cela ne se corrige pas après coup.

## Les cinq livrables

Les trois volumes vivent sous [`1 - Corpus/`](1%20-%20Corpus/) ; la veille est
à la racine ; le compendium a son propre dossier. *(Les deux dossiers ont été renommés le
25 juillet 2026 — `1 - Corpus Agentique/` et `2 - Compendium Agentique/` auparavant, commit
`60f57f6`.)*

| | **Veille technologique** | **Vol. I — Interopérabilité** | **Vol. II — Orchestration** | **Vol. III — Entreprise** | **Vol. IV — Compendium** |
|---|---|---|---|---|---|
| **Dossier** | racine du dépôt | [`1 - Corpus/1 - InteroperabiliteAgentique/`](1%20-%20Corpus/1%20-%20InteroperabiliteAgentique/) | [`1 - Corpus/2 - OrchestrationAgentique/`](1%20-%20Corpus/2%20-%20OrchestrationAgentique/) | [`1 - Corpus/3 - EntrepriseAgentique/`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/) | [`2 - Compendium/`](2%20-%20Compendium/) |
| **Titre** | Interopérabilité et orchestration agentique en entreprise | Interopérabilité agentique en entreprise dans le domaine des services financiers | L'autonomie encadrée | L'entreprise agentique — la fabrique de confiance | La somme agentique |
| **Rôle** | État de l'art vérifié, mis à jour par éditions | Cadre général, mondial et théorique | Cas canadien réglementé, instruit au grain du droit | Le verrou commun : identité, maillage, exploitation | Omnibus terminal : absorbe et remplace les trois volumes |
| **Portée** | Mondiale | Mondiale (UE / É.-U. / R.-U. / Asie) | Canada-Québec (E-23, AMF, Loi 25, ACVM, Lynx/RTR) | Organisation et cycle de vie (NHI, *agent mesh*, AgentOps) | Les trois portées réunies (2024-2032) |
| **Thèse** | « L'agent d'entreprise fiable de 2026 est un agent *enveloppé* » | « Autonomie graduée sous contrôle de finalité » | « Autonomie encadrée » (*framed autonomy*) | « La confiance ne se décrète pas, elle se fabrique » | Les trois thèses sont trois coupes d'un même objet |
| **Méthode** | Revue structurée, vérification adverse à trois votants | Formalisme d'ingénierie (ArchiMate 4, ADS « Boréalis ») | Socle factuel F-01…F-48, niveaux de preuve [A]/[B]/[C] | Double héritage codifié : entrées du Vol. II à niveau conservé, du Vol. I en [C] | Méthode unifiée, gel unique (annoncée) |
| **Gel de l'information** | 29 juillet 2026 (édition d'août 2026 ; les sections antérieures gardent leur date d'état) | Juin 2026 | 16-17 juillet 2026 | — (hérite de deux gels : juin et 16-17 juillet 2026) | 27 juillet 2026 (décision d'auteur D-1) ; volet des faits levé le 28 juillet 2026 |
| **État** | Publiée (161 p., 269 références) | Rédaction terminée (569 p., **233 257 mots** — `wc -w` sur `Monographie.md`, point d'ancrage de `decompte.sh --verifier` ; 225 258 par la commande de référence du dépôt. ⚠ *Le chiffre de ≈ 263 600 mots que ce fichier portait n'est reproductible par aucune des deux commandes* ; synthèse retirée le 22 juillet 2026, démonstrateur `Borealis-Go` retiré le 25 juillet 2026) | Publiée, millésime `mono-v1.0` (387 p. ; synthèse retirée le 22 juillet 2026) | **Rédigé, non publié** — 34 pièces rédigées et relues (≈ 160 900 mots), gouvernance PRD v1.3 / TOC v0.8 / PRDPlan v0.5 ; finalisation P5 en cours (relecture de révision du 24 juillet 2026) ; **PDF réassemblé le 24 juillet 2026** (427 p., gabarit FESP, page de note d'état retirée), non publiable en l'état | **Arrêt rouvert — passe de révision en cours**, statut de révision finale en bibliothèque personnelle maintenu (D-11, 30 juillet 2026 ; TOC v0.32 / PRD v0.16 — arrêt initial D-10, 29 juillet 2026, TOC v0.31 / PRD v0.15) : les **cinquante chapitres** des cinq Livres, rédigés **hors portes** le 27 juillet, relus, arbitrés et audités, sont arrêtés et composés en [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) (**1 114 p.**, re-mesurées le 8 août 2026, dont une **annexe hors plan** — la liste des 159 références, ajoutée au rendu le 29 juillet 2026 ; gabarit relevé sur deux monographies Springer le même jour, puis porté au format Letter le 31 juillet 2026). ⚠ **Arrêté n'est ni terminé ni publiable** : trois portes satisfaites sur pièce (G-2, G-3, G-7), **quatre closes pour ce seul régime par dérogation**, **CA-IV-11 et CA-IV-13 non satisfaits** faute de relecteur tiers ; **aucune diffusion à un tiers, aucune opposabilité** |

## Veille technologique — le document transversal

[`Veille Technologique.md`](Veille%20Technologique.md) → `Veille Technologique.pdf` (**161 p.**,
14 sections numérotées, **269 références**, 15 tableaux — **édition d'août 2026**, faits gelés au
29 juillet 2026 ; résumé sur la page de titre, sommaire exécutif sur trois pages). Revue vérifiée où chaque énoncé factuel
est adossé à une source primaire consultée et soumis à contradiction — vérificateurs indépendants
chargés de *réfuter*, contre-vérification directe sinon. Elle couvre les trois protocoles
structurants (MCP, A2A, ANP), leur gouvernance, l'adoption documentée, la sécurité, et **sept
couches** que la pile protocolaire laisse implicites : événementielle, de contrôle,
transactionnelle, sémantique, de confiance, d'orchestration des processus d'affaires et —
depuis l'édition intégrale — d'**exploitation** (observabilité agentique, évaluation continue,
révocation).

**Elle est aussi le point d'articulation du corpus.** L'**édition intégrale du 18 juillet 2026**
rend compte des **quatre** volumes, dans une section 13 qui leur est consacrée — mais à deux
régimes strictement distincts, et c'est l'écart qui compte :

- les **Vol. I et II sont rédigés** et fournissent des faits — **§4.12 — « De la spécification au
  code »** confronte le corpus documentaire à l'épreuve du démonstrateur `Borealis-Go`
  (référence [217]) ; **§8.4 — « L'instruction sectorielle canadienne »** reprend le croisement
  systématique entre trajectoire protocolaire et textes canadiens (référence [218]) ;
- les **Vol. III et IV y sont des cadrages** — zéro chapitre, zéro entrée de socle propre — et ne
  fournissent **aucun fait** (références [219] et [220], qui portent la réserve en toutes lettres).
  Ils prêtent des *instruments* : la grille des cinq questions du Vol. III organise les §7.6 à 7.10,
  les décisions de fusion du Vol. IV servent de contrôle de couverture. Traiter un plan comme un
  corpus serait la faute que ces deux cadrages prennent eux-mêmes pour objet.

⚠ **Ce tableau de régimes est celui de la veille à son gel, et le dépôt l'a dépassé sur trois
points — signalés ici, non corrigés là-bas.** Le **Vol. III est rédigé depuis le 22 juillet 2026**
(34 pièces, socle propre de 98 entrées), alors que la réf. [219] le décrit sans chapitre ; le
**démonstrateur de la réf. [217] a été retiré du dépôt le 25 juillet 2026** (commit `60f57f6`) — la
citation reste exacte, elle cesse d'être vérifiable ailleurs que dans l'historique git ; et le
**Vol. IV a cinquante chapitres rédigés depuis le 27 juillet 2026, un socle consolidé de 159 entrées
depuis le 28 et un PDF composé depuis le 29 — 1 114 pages au 8 août 2026**, alors que la réf. [220] le décrit comme un
cadrage sans chapitre. ⚠ **Le troisième écart ne fait pas du Vol. IV une source de fait pour
autant** : ses pièces se déclarent brouillon non publiable, et *un brouillon ne porte pas plus de
fait qu'un cadrage*. Une revue publiée décrit l'état de ses sources à sa date : la rattraper après
coup effacerait la seule information qu'elle porte.

L'échange est bidirectionnel : la veille rend au corpus deux corrections de datation, referme une
lacune que le Vol. II déclarait ouverte (les dépôts ACP d'AGNTCY, archivés le 11 avril 2026) — et
**rétracte la certitude d'une de ses propres datations** (voir « Divergences factuelles » plus bas).
L'auto-citation est assumée et divulguée ; ses limites (circularité possible, implémentation
unique, chiffres institutionnels auto-déclarés, deux volumes non rédigés) sont exposées en
section 10 de la veille.

*Historique des éditions : 2, 4, 7, 12, 13, 15, 18 juillet 2026, puis l'édition intégrale du
18 juillet 2026. Chaque édition ajoute une couche ou un corpus et revérifie les faits périssables.*

## Vol. I — Interopérabilité agentique

Monographie de science et génie informatique, construite **en spirale du général au spécifique**,
pour un double public (recherche et praticien-architecte). Invariant transversal : *découplage,
contrat, évolution*.

- **Monographie** (`Monographie.pdf`, **569 p.**) — 7 chapitres : interopérabilité des SI, IA
  agentique, interopérabilité agentique, en entreprise, dans le domaine financier, blueprint
  ArchiMate, horizon 2027-2032.
- **Architecture détaillée de solution** (Annexe B) — la monographie projetée sur une entreprise
  fictive, la *Coopérative financière Boréalis*, consolidée sur la pile IBM ; 18 sections,
  6 sous-annexes, 28 diagrammes Mermaid, rendus dans le PDF principal.
- **Article de synthèse** — *retiré du dossier le 22 juillet 2026* (`Synthese Monographie.md` / `.pdf`,
  69 p.). La monographie et son Annexe B restent les seuls livrables du volume.
- **Démonstrateur `Borealis-Go/`** — *retiré du dépôt le 25 juillet 2026* (commit `60f57f6`).
  C'était du code Go exécutable matérialisant l'ADS : **5 agents A2A** et **4 serveurs MCP**
  orchestrant une pré-qualification de crédit (jamais un octroi ferme), sur les SDK officiels des
  deux protocoles ; **12 ADR**, journal d'audit à chaîne de hachage, vérification adverse à chaque
  phase, invariants critiques prouvés par mutation ; couverture déclarée 96,2 % au rapport final.
  C'est lui qui fournissait la §4.12 de la veille (référence [217]) — **cette référence ne se
  vérifie plus que dans l'historique git**, et la veille n'est pas corrigée pour autant.

## Vol. II — L'autonomie encadrée

Monographie sur l'interopérabilité et l'orchestration agentique en services financiers canadiens,
publiée sous le millésime `mono-v1.0`. **92 059 mots** en 29 pièces (24 chapitres, avant-propos,
annexes A-D) selon son README ; `Monographie.pdf` **387 p.** (article de synthèse, 66 p., retiré du
dossier le 22 juillet 2026).

⚠ `mono-v1.0` est un **millésime éditorial, pas une étiquette git** : aucune référence de ce nom
n'existe dans le dépôt, ni en local ni sur le distant (vérifié le 18 juillet 2026). Plusieurs
documents de gouvernance du Vol. II l'annoncent pourtant comme posée.

Sa contribution la plus citable est un **résultat négatif** : en croisant trois protocoles
(MCP, A2A, AP2) et cinq corpus de textes canadiens, **aucun lien documenté par source primaire** —
quinze croisements, zéro lien. D'où sa thèse probatoire : sous exigence réglementaire stricte, le
cadre déterministe invoque les agents, jamais l'inverse, parce que le cadre est la seule pièce
dont l'exploitant puisse démontrer la teneur devant un tiers.

Sa méthode est son autre apport : socle factuel de **46 entrées** (F-01 à F-48) cotées par niveau
de preuve — **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage —,
huit garde-fous de formulation, onze lacunes exposées plutôt que comblées.

## Vol. III — L'entreprise agentique

**Rédigé de bout en bout, non encore publié.** Les **34 pièces** — avant-propos, 28 chapitres en
9 parties, 5 annexes — sont **rédigées, relues adversarialement et corrigées** (statut constaté sur
pièce le 22 juillet 2026), pour **≈ 160 900 mots réels** (re-mesure du 24 juillet 2026, après la relecture de révision) au regard d'une cible indicative de
**≈ 102 500**. Le socle factuel propre compte **98 entrées** (F-01 à F-98), sur **33 entrées
héritées** (H-01 à H-33) ; les **15 lots d'instruction sont clos**. Le volume s'organise autour de
trois capacités — *émettre* une identité opposable (le passeport d'agent), l'*appliquer* au
maillage d'agents, l'*exploiter* dans la durée (AgentOps) — sous l'horloge post-quantique.

⚠ **Rédigé ne vaut pas publiable.** La phase de finalisation (**P5**) est en cours : revalidation
temporelle finale, rejeu des motifs de balayage sur les 34 pièces ; le pipeline de rendu a été
créé le 23 juillet 2026 (copie du FESP du Vol. II) et **quinze remontées de gouvernance demeurent
ouvertes** (R-G-43 à R-G-57), dont plusieurs relèvent de l'auteur. **Le PDF est assemblé
(427 p., gabarit FESP) ; rédigé ne vaut pas publiable.**

Le dossier porte trois répertoires — la gouvernance dans `prd/`, la rédaction dans `monographie/`,
les rapports de vérification dans `verification/` —, plus un
[`README.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/README.md) au lecteur *(déposé le
29 juillet 2026 : le volume était le seul des trois à n'en porter aucun)*.
Documents de gouvernance, par ordre d'autorité :

1. [`prd/PRD.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/prd/PRD.md) **v1.3** —
   contenu, héritage du socle, quatorze garde-fous, critères d'acceptation ; **prime en cas de
   conflit**, y compris sur le TOC ;
2. [`prd/TOC.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/prd/TOC.md) **v0.8** —
   autorité sur le découpage (28 chapitres, 9 parties, 34 pièces) ;
3. [`prd/PRDPlan.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/prd/PRDPlan.md)
   **v0.5** — plan d'exécution (phases P0 à P5).

Le volume naît des lacunes des deux précédents : identité non humaine et délégation multi-saut
(verrou identifié au Vol. I), mécanique des attaques et valeur cryptographique des Agent Cards
(questions ouvertes du Vol. II).

## Vol. IV — La somme agentique (compendium)

**Arrêté en révision finale pour une bibliothèque personnelle — et l'arrêt est rouvert depuis le
30 juillet 2026.** Le dossier
[`2 - Compendium/`](2%20-%20Compendium/) porte une table des matières
commentée ([`TOC.md`](2%20-%20Compendium/PRD/TOC.md), **v0.32 du 30 juillet 2026** — chaque
entrée de chapitre y est suivie de sa **table des matières détaillée**, provenance par
sous-section et table de couverture, **portée en titres markdown depuis la v0.18** : le plan du
fichier expose la hiérarchie livre → chapitre → section), son
**PRD de gouvernance de la rédaction** ([`PRD.md`](2%20-%20Compendium/PRD/PRD.md), **v0.16 du
30 juillet 2026** — portes de lancement, régimes de preuve, critères d'acceptation, jalons), son
**socle consolidé** ([`socle-consolide.md`](2%20-%20Compendium/PRD/socle-consolide.md), **159 entrées**
`S-001`…`S-159`), sa vue synoptique dérivée ([`README.md`](2%20-%20Compendium/README.md)), ses
exécutables de contrôle ([`check-toc.py`](2%20-%20Compendium/PRD/check-toc.py) et trois autres,
chacun avec son harnais de validation par mutation), ses **cinq Livres rédigés** et — depuis
le 29 juillet 2026 — leur rendu paginé,
[`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) —
**c'est une refonte des trois volumes, pas une nouvelle thèse.**

⚠ **Les cinquante chapitres sont rédigés, et ils le sont hors portes.** Le 27 juillet 2026, sur
instruction d'auteur, les cinq répertoires [`Livre I/`](2%20-%20Compendium/Livre%20I/) à
[`Livre V/`](2%20-%20Compendium/Livre%20V/) ont été créés et **leurs cinquante chapitres** y ont été
rédigés en deux rendus chacun (`.md` source, `.html` de lecture à thème sombre — **corps technique
seul depuis la purge du 29 juillet 2026**, l'appareil de gouvernance restant au `.md`), **avant** le
franchissement des portes que le PRD pose comme préalables ; chaque pièce se déclare elle-même
**brouillon, non publiable** et porte, en section hors plan, les conséquences de cet écart. Les passes
d'arbitrage qui ont suivi ont soldé leurs remontées, puis un **audit intégral des cinq Livres**
(`audit.md`, cent constats — ⚠ **rapport retiré du dépôt depuis**, récupérable au seul historique git)
et une relecture des cinquante pièces ont
précédé le franchissement de la **porte G-3** le 28 juillet 2026 — le socle consolidé, resté vide
depuis l'ouverture du volume, porte désormais **159 entrées**. ⚠ **Rien de cela ne requalifie
l'ouvrage** : *une porte franchie n'est pas un ouvrage recevable, c'est une condition qui cesse de
manquer* — **G-4, G-5 et G-6 restent ouvertes**, et **CA-IV-11 comme CA-IV-13 demeurent
insatisfaisables** faute d'un relecteur distinct du rédacteur. *Un brouillon écrit hors portes ne
franchit aucune porte* — et *zéro remontée ouverte ne veut pas dire pièce recevable.* Le détail par
Livre vit aux `README.md` des cinq dossiers.

⚠ **Le volume est arrêté depuis le 29 juillet 2026 — et « arrêté » n'est ni « terminé » ni
« publiable ».** La décision d'auteur **D-10** (PRD [v0.15 §14](2%20-%20Compendium/PRD/PRD.md), TOC
v0.31) place le compendium au statut de révision **RÉVISION FINALE**, sous un **régime de diffusion en
bibliothèque personnelle** : lecture par l'auteur, **aucune mise à disposition d'un tiers**, aucun
dépôt public, **aucune opposabilité**. La conformité est arrêtée sous **trois états qui ne se
confondent pas** — **satisfaite sur pièce** pour G-2, G-3 et G-7 (plus les quatre contrôles outillés,
rejoués le même jour, sorties 0) ; **close pour ce seul régime, par dérogation nommée**, pour G-1
(volets résiduels), G-4 (volet de fond), G-5 (balayage du Livre IV) et G-6 (trois lots, socle du
ch. 41), **dont le résidu reste entier et écrit** ; **non satisfaisable** pour **CA-IV-11 et
CA-IV-13**, qui exigent un relecteur distinct du rédacteur. ⚠ **Le motif de la dérogation est unique
et étroit** — *lecteur et rédacteur sont la même personne, il n'y a aucun tiers à protéger d'une
affirmation non réfutée* — et **elle tombe avec lui** : à la première diffusion, les quatre portes et
les deux critères redeviennent exigibles dans leur état. **Aucun énoncé n'est central** au sens de
CA-IV-01, **aucun vote adversarial n'a été conduit**, et **les trois volumes sources font toujours
foi**.

⚠ **L'arrêt a été rouvert le 30 juillet 2026, et rien de la réserve ci-dessus ne s'en trouve allégé.**
La décision d'auteur **D-11** (PRD [v0.16 §15](2%20-%20Compendium/PRD/PRD.md), TOC **v0.32**) **rouvre
D-10** pour une **passe de révision**, prise au titre de D-6. Son déclencheur est un **rapport
d'arbitrage externe** du 30 juillet 2026 — `eval.html`, **retiré de l'arbre depuis** et lisible au seul
historique git — qui conclut à une **révision majeure : accepté sur le fond, non diffusable en l'état**
(huit faiblesses majeures, sept mineures, dix recommandations ; **22 affirmations vérifiées, 19
confirmées, 3 partielles, 0 infirmée**). ⚠ **Ce rapport n'a lui-même aucune autorité** : il déclare en
sa §10 ne satisfaire ni CA-IV-11 ni CA-IV-13, ses dix rapporteurs étant des instances d'un même modèle
de langage — *des convergences entre rapports ne sont pas des convergences entre esprits
indépendants*. Ses constats entrent comme **remontées**, arbitrées par l'auteur. **Ce que D-11 change,
et c'est tout** : une seule décision de plan en découle, la **décision 18 du TOC**, qui **renverse la
décision 15a** — *la citation nominative l'emporte, la péremption se gérant par datation et non par
anonymat*. **Ce que D-11 ne change pas** : le statut **RÉVISION FINALE — bibliothèque personnelle est
maintenu pendant toute la durée de la passe** ; **CA-IV-11 et CA-IV-13 demeurent dérogés, non
satisfaits** ; **G-1 résiduel, G-4, G-5 et G-6 restent clos pour ce seul régime** ; la relecture tierce
que le rapport réclame **n'est pas fournie par le rapport lui-même**, et il l'écrit. ⚠ **La passe de
révision est ouverte, non refermée** : le volume n'est donc ni arrêté au sens de D-10, ni publiable.

⚠ **Un rendu paginé existe depuis le 29 juillet 2026, et il ne requalifie rien non plus.**
[`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) — **1 114 pages** (re-mesurées le 8 août 2026), les cinquante chapitres des
cinq Livres **et une annexe hors plan** (la liste des 159 références du socle, ajoutée le
29 juillet 2026), **format Letter (215,9 × 279,4 mm) depuis la refonte typographique du 31 juillet
2026**, **sans aucune page blanche** —
est composé par [`build/build-pdf.sh`](2%20-%20Compendium/build/build-pdf.sh), **quatrième pipeline
du dépôt et le seul qui ne dérive pas du FESP**. Le rendu retire du corps les trois appareils que le
volume tient hors corps (en-tête à cinq champs, thèse citée depuis le TOC, note de statut) et
**marque d'une dague les vingt-trois renvois** que cette coupe laisserait pendre, plutôt que de les
supprimer. ⚠ **Un second rendu existe depuis le 4 août 2026, et il ne requalifie rien davantage** :
[`Compendium.html`](2%20-%20Compendium/Compendium.html), **appareil de lecture à l'écran** du volume
— déposé ce jour-là sous le nom `presentation.html`, renommé le même jour (commit `d473913`).
**Un seul fichier de 1,74 Mio** (**1 826 464 octets**, mesurés le 8 août 2026 en fin de passe ; le
fichier est en fins de ligne `LF` pures, et le décompte est celui des octets sur disque)**, sans
dépendance externe** et un seul lien sortant, vers le PDF : les
**118 figures** du volume y sont embarquées en SVG `data:` et retournées pour fond sombre, la
typographie reprend les deux fontes du rendu imprimé (Constantia, Corbel) et la justification est
réglée sur la mesure du livre, **79 signes**. Douze entrées — thèse, horloge, instruments, les cinq
Livres, socle, parcours, index des 56 notions, probité, colophon. ⚠ **Trois choses qu'il n'est
pas.** *(a)* Il **ne fait pas autorité** : son propre colophon le déclare dérivé, et *le `.md` reste
la seule source*. *(b)* Il **n'est publié nulle part** — aucune page GitHub Pages, aucune diffusion :
c'est un fichier du dépôt, servi en local par
[`.claude/launch.json`](2%20-%20Compendium/.claude/launch.json) (`python -m http.server 8731`), et le
régime de **D-10**, maintenu par **D-11**, le gouverne comme il gouverne le PDF. *(c)* ⚠ **Il ne se régénère pas.** **Aucun
script du dépôt ne le reconstruit** depuis les cinquante `.md` : il est écrit à la main, ses
décomptes sont relevés à la main, et *un rendu sans chaîne se périme en silence* — c'est la
différence exacte d'avec `Compendium.pdf`, qui se recompose dans le commit de la pièce qu'il rend.
⚠ **Son horloge, elle, est calculée à l'ouverture** : la position d'« aujourd'hui » et l'âge du gel
se recalculent à chaque affichage — *cette page vieillit avec l'ouvrage qu'elle présente, sans
vieillir avec le texte qu'elle en tire.* ⚠ **Le rendu ne porte AUCUN avertissement de statut, et c'est une instruction d'auteur du
30 juillet 2026** : un bloc de colophon portant le **statut de révision finale, son régime de
diffusion et ses réserves** — portes dérogées, vote adversarial non conduit, CA-IV-11 et CA-IV-13 non
satisfaits, aucun énoncé central — a été écrit ce jour-là, **après qu'une mesure du PDF eut montré
qu'il manquait alors que trois documents de gouvernance le déclaraient présent**, puis **retiré sur
instruction**. ⚠ ***Le régime de diffusion vit donc au dépôt seul*** — PRD §14 et §15, TOC,
conspectus, en-tête des cinquante pièces —, et **un lecteur qui n'aurait que le PDF ne le lit nulle
part**. *Composer n'est pas publier* : le `.md` reste la seule source, et le PDF se régénère avec
elle.

Sa nature le distingue des trois autres : ce n'est ni un quatrième panneau ni un méta-index, mais
un **omnibus qui absorbe les Vol. I, II et III** en un seul ouvrage réordonné et dédoublonné, à
numérotation continue — **50 chapitres** en 5 livres, ≈ 376 000 à 401 000 mots projetés. Le décompte
est un **plafond dur** depuis la v0.23 (décision 13 du TOC, contrôle `C15`) : la somme ne dépasse
jamais cinquante chapitres, et toute insertion se paie par une **fusion** dans la même passe — les
deux entrées fusionnées étant conservées intégralement, en deux mouvements. C'est ainsi que le
**ch. 41, la fabrique d'agents** (entré en v0.22 sur instruction d'auteur, matière neuve sans volume
source, déclarée telle) a été payé par la fusion des ch. 47 et 48. Une fois **recevable** — et il ne
l'est pas : rédigé et composé ne valent pas publiable —, il se substituera à la lecture des trois
volumes ; **jusque-là, les trois volumes sources font foi.** Ses décisions structurantes :
numérotation continue, déduplication tracée sous chaque entrée, divergences héritées tranchées (et non plus signalées), méthode et gel unifiés, couverture
totale tracée — chaque section des sources est affectée à un chapitre d'arrivée ou marquée « coupe
assumée ».

⚠ Sa volumétrie est explicitement **indicative et non normative** : elle agrège des décomptes pris
par des commandes différentes, non comparables entre eux. La première tâche de sa rédaction est de
re-mesurer les trois corpus par une commande de référence unique.

## Ordre de lecture et renvois

**Vol. I → Vol. II → Vol. III**, la veille servant d'entrée rapide ou de mise à jour ; le Vol. IV
les remplacera tous les trois **une fois recevable** — il est écrit, composé et arrêté, il n'est
pas publiable, et [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) se feuillette sans faire foi.

- **Vol. II présuppose Vol. I** pour la théorie du découplage, l'ingénierie des agents LLM,
  l'anatomie des protocoles, la sécurité de la couche agentique et la cryptographie post-quantique.
- **Vol. I illustre mondialement** ce que **Vol. II instruit au grain du droit canadien**.
- **Vol. III prolonge les deux** sur leur verrou commun, l'identité et son exploitation.
- **La veille les cite tous les quatre, à deux régimes distincts.** Les volumes *rédigés*
  fournissent des faits : §4.12 pour le Vol. I (réf. [217]), §8.4 pour le Vol. II (réf. [218]).
  Les volumes de *cadrage* ne fournissent aucun fait et ne prêtent que des instruments d'analyse :
  Vol. III (réf. [219], grille des cinq questions, §7.6 à 7.10), Vol. IV (réf. [220], décisions de
  fusion). Sa section 13 est le siège de ce rendu de compte, et son §13.1 pose la règle : un volume
  sans chapitre rédigé ni socle propre ne porte aucun fait.
- **Vol. IV les absorbe** : ses renvois inter-volumes deviennent des renvois internes.
- Un lecteur pressé côté canadien peut entrer directement par le **chapitre 13** du Vol. II
  (« le pont : des contraintes réglementaires aux frames déterministes »), son pivot.

## Divergences factuelles entre volumes

Deux faits datés divergent d'un corpus à l'autre. Ils sont **signalés, non arbitrés** — la veille
les expose en §8.4, et le lecteur doit les trancher à sa date de citation :

| Objet | Vol. II (gel 16-17 juill.) | Veille (édition intégrale, 18 juill.) | État après revalidation |
|---|---|---|---|
| Ligne directrice IA de l'AMF — version finale | 30 mars 2026, avec **dette de vérification déclarée** (`lautorite.qc.ca` renvoie 403 aux outils) | 7 avril 2026 | **divergence ouverte** — la revalidation du 18 juillet a buté sur le **même 403** (sept tentatives, cinq adresses) ; aucune des deux dates n'est établie sur une source primaire directement consultée |
| Gouvernance d'AP2 | aucun transfert documenté au socle | don à la FIDO Alliance, **28 avril 2026** | **résolue** — source primaire datée, accessible et antérieure au gel du Vol. II ; frontière de socle, non désaccord |

L'entrée en vigueur du 1er mai 2027 est, elle, concordante entre les corpus, et ne l'a jamais cessé.

Les deux cas portent la même leçon sous deux formes. Sur AP2, deux corpus vérifiés de bonne foi
divergent parce que **leurs périmètres de sources diffèrent** — argument pour le millésimage
systématique. Sur l'AMF, ils divergent parce que **la source elle-même est inaccessible aux
outils** : c'est l'accessibilité de la source qui est mesurée, non la rigueur inégale des corpus,
et aucune discipline de veille ne corrige cela. ⚠ **L'édition intégrale de la veille rétracte en
conséquence la certitude de sa propre datation** (§13.6) : sa date du 7 avril repose sur des
sources secondaires, et n'est donc pas mieux étayée que celle du Vol. II.

⚠ **Le cadrage du Vol. IV tranche ces deux divergences en faveur du Vol. II** — ligne directrice
AMF finale au 30 mars 2026 (ch. 31), aucun transfert de gouvernance d'AP2 documenté (ch. 10) —
donc *contre* les lectures de la veille. L'arbitrage est consigné à son Annexe C. Sur AP2 il est
**périmé par une source primaire datée** ; sur l'AMF il n'est **ni confirmé ni infirmé**. Et de
toute manière, tant que le compendium n'est pas **recevable** — ses cinquante chapitres sont un
brouillon écrit hors portes, que le PDF compose sans le publier —, **cet arbitrage n'a aucune
autorité** : les volumes sources font foi et la divergence reste ouverte — le plan le dit lui-même.

> ⚠ Le fichier `commun/faits-partages.md`, évoqué par le cadrage du Vol. III comme source unique
> de vérité pour les faits partagés, **n'existe pas et ne sera pas créé** : son PRD §7.5 a tranché
> de porter lui-même ces divergences. Chaque volume porte donc ses propres faits datés.

## Structure du dépôt

```
.
├── README.md                              ← ce fichier (avant-propos croisé)
├── Veille Technologique.md / .pdf         ← veille autonome, édition d'août 2026, faits gelés au 29 juillet (161 p., 269 réf.)
├── 1 - Corpus/                            ← le triptyque
│   ├── 1 - InteroperabiliteAgentique/       Vol. I
│   │   ├── Chapitres/                         7 chapitres + 7 bibliographies + Annexe B (ADS)
│   │   ├── Monographie.md / .pdf              assemblage (569 p.)
│   │   └── build/                             pipeline FESP (Mermaid → Pandoc → Typst)
│   ├── 2 - OrchestrationAgentique/          Vol. II
│   │   ├── monographie/                       29 pièces (parties I-VII, annexes, registre des gels)
│   │   ├── prd/                               PRD, PRDPlan, TOC, audit + 2 PDF sources — gouvernance
│   │   ├── verification/                      revalidations et grille de conformité CA-1..CA-8
│   │   ├── build/                             assemblage + pipeline Pandoc → Typst
│   │   └── Monographie.md / .pdf              assemblage (387 p.)
│   └── 3 - EntrepriseAgentique/             Vol. III
│       ├── README.md                          présentation du volume (déposée le 29 juill. 2026)
│       ├── prd/                               PRD v1.3, TOC v0.8, PRDPlan v0.5 — gouvernance
│       ├── monographie/                       34 pièces rédigées + registre des gels
│       ├── verification/                      30 rapports (lots, relectures, revalidations)
│       ├── build/                             pipeline FESP (copie du Vol. II) + assemble.py
│       └── Monographie.md / .pdf              assemblage (427 p., gabarit FESP) — non publiable
└── 2 - Compendium/                        ← Vol. IV
    ├── README.md                            vue synoptique dérivée du TOC (le « conspectus » du volume)
    ├── annexe-references.md                 liste des 159 références du socle — annexe hors plan du rendu
    ├── Compendium.pdf                       rendu paginé des 50 chapitres + 2 annexes (1 114 p.) — brouillon non publiable
    ├── Compendium.html                      appareil de lecture à l'écran du volume (4 août 2026, ex-`presentation.html`)
    │                                          un fichier, sans dépendance externe, 118 figures embarquées — ⚠ écrit à la main, aucune chaîne ne le régénère
    ├── .claude/launch.json                  sert le dossier en local (python -m http.server 8731) pour lire Compendium.html
    ├── build/                               pipeline propre au volume (PAS une copie du FESP)
    │   ├── assemble.py                        50 pièces + annexe → compendium.md, 23 renvois portés en note de marge
    │   ├── compendium.template                gabarit COURANT — identité propre, Letter, marges relevées sur les monographies, Constantia/Corbel
    │   ├── springer.template                  gabarit précédent (29 juill. 2026), conservé — 155 × 235 mm, Times 10/12
    │   └── build-pdf.sh                       bash build/build-pdf.sh → Compendium.pdf
    ├── Livre I/ … Livre V/                  ⚠ rédaction hors portes — 50 pièces sur 50, brouillons
    │   ├── README.md                          état du livre, issues des remontées, sièges, volumétrie
    │   └── NN-….md / .html                    un chapitre par pièce — source + page à thème sombre
    └── PRD/                                 gouvernance de la rédaction (sous-dossier)
        ├── PRD.md                           v0.16 — portes, régimes de preuve, jalons ; §15 = D-11
        ├── TOC.md                           table des matières commentée (v0.32) — spécification
        ├── socle-consolide.md               socle consolidé S-001…S-159 (porte G-3, 28 juill. 2026)
        ├── registre-gel.md                  registre de gel, une ligne par chapitre
        ├── check-toc.py                     contrôles C1-C15 (python PRD/check-toc.py)
        ├── check-sieges.py                  contrôles S1-S5 inter-pièces — 26 sièges sur 50 pièces
        ├── check-compendium.py              contrôles P1-P8 du socle consolidé
        ├── decompte.sh                      commande de décompte de référence (porte G-2)
        └── *-mutations.py                   validation par mutation des trois contrôles
```

**Où sont les `README.md`.** **Douze**, même date de comptage : la racine, le conteneur
[`1 - Corpus/`](1%20-%20Corpus/README.md) (la synthèse consolidée), les **trois** volumes du triptyque
— celui du Vol. III déposé le 29 juillet 2026 —, l'index de lecture des 29 pièces du Vol. II, le
conspectus du Vol. IV, et les **cinq** répertoires de Livres du compendium.

## Construire les PDF

**Cinq** chaînes distinctes, à lancer depuis le dossier concerné.

**Veille technologique** (racine) — invocation Pandoc directe, gabarit Typst par défaut :

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

**Vol. I** — pipeline FESP, avec pré-rendu des 28 diagrammes Mermaid ; depuis
`1 - Corpus/1 - InteroperabiliteAgentique/` :

```bash
bash build/build-pdf.sh                              # Monographie.pdf
```

**Vol. II** — assemblage des 29 pièces, puis une **copie** du même pipeline ; depuis
`1 - Corpus/2 - OrchestrationAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf
```

☑ **L'assemblage du Vol. II remarche depuis le 8 août 2026.** `build/assemble.py` cherchait `TOC.md` à
la racine du volume alors qu'il vit dans `prd/`, et échouait avant d'écrire une ligne. ⚠ **La reprise a
trouvé un second défaut que rien ne signalait, et il touchait aussi le Vol. III** : les deux
assembleurs ne rebasaient pas les cibles relatives des pièces, si bien qu'un renvoi valide dans
`monographie/03-partie-III/` mourait une fois concaténé à la racine du volume. Les deux scripts
rebasent désormais. Les copies du pipeline évoluent séparément ; un correctif au Vol. I ne se propage
pas au Vol. II.

**Vol. III** — assemblage des 34 pièces, puis une **troisième copie** du même pipeline
(créée le 23 juillet 2026, au gabarit des monographies) ; depuis
`1 - Corpus/3 - EntrepriseAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf (427 p.)
```

Les trois copies du FESP évoluent séparément. ⚠ La **note d'état** que le PDF du Vol. III portait en
page 2 a été **retirée le 24 juillet 2026** sur demande de l'auteur (constante `ETAT` supprimée de
`build/assemble.py`) : la page de titre est directement suivie du résumé. *Le statut non publiable
ne dépend d'aucune page qui le déclare* — il tient aux quinze remontées ouvertes (R-G-43 à R-G-57)
et à la dette de vote sur F-92 et F-96.

**Vol. IV** — assemblage des 50 pièces des cinq Livres, puis un pipeline **propre au volume** (créé
le 29 juillet 2026, gabarit Typst relevé sur deux monographies Springer) ; depuis `2 - Compendium/` :

```bash
bash build/build-pdf.sh                     # Livre I/ … Livre V/ + 2 annexes → Compendium.pdf (1 114 p.)
```

⚠ Ce quatrième pipeline **ne dérive d'aucune des trois copies du FESP, et aucune ne dérive de lui** :
la règle d'indépendance vaut donc pour **quatre**. Le script publie à chaque exécution ce qu'il a
assemblé et marqué (50 chapitres, 5 livres, 23 renvois marqués d'une dague), et il **échoue** si une
pièce ne porte pas les trois appareils qu'il retire — une pièce déformée passerait sinon sans bruit.

⚠ **Les cinq chaînes ne produisent que des PDF.** Les `.html` du Vol. IV — les **cinquante pages de
chapitre** et [`Compendium.html`](2%20-%20Compendium/Compendium.html), l'appareil de lecture du
volume — **ne sortent d'aucune d'entre elles** : `build/` ne contient aucun générateur HTML, et ces
fichiers sont écrits à la main. *Il n'y a donc pas de commande à donner ici, et c'est précisément le
problème* : la règle du « rendu versionné avec sa source » ne peut pas s'y appliquer, et rien ne
signale qu'une page est en retard sur le `.md` dont elle est tirée. Pour lire
`Compendium.html`, depuis `2 - Compendium/` :

```bash
python -m http.server 8731
```

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf` — ⚠ *`pypdf` n'est pas installé dans
l'environnement de la passe du 8 août 2026 ; ses décomptes de pages sont pris par lecture du `/Count`
de l'objet `/Type /Pages`* ; polices Liberation Sans et
DejaVu Sans (pipeline FESP), New Computer Modern (veille), Times New Roman (compendium — repli
Libertinus Serif, signalé à l'exécution) ; pour les diagrammes, Node ≥ 18 +
[`@mermaid-js/mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) et un Chromium. Les quatre
`build-pdf.sh` exportent eux-mêmes `PYTHONUTF8=1` — inutile de le faire à la main sous Windows.
**Règle permanente :** régénérer et versionner le PDF avec sa source — jamais la source seule.

## Ce qui reste vivant

Le domaine se périme par trimestres, et ces corpus par morceaux. Échéances datées à revalider
avant toute réutilisation ou publication :

| Échéance | Objet | Documents touchés |
|---|---|---|
| ☑ **échue le 28 juillet 2026** | Révision de la spécification MCP (protocole sans état) — **la révision `2026-07-28` est versée à la veille** (§4.1 : noyau sans état, `server/discover`, dépréciation de Roots, Sampling, Logging et de l'enregistrement dynamique de client). ⚠ **Les volumes ne sont PAS rattrapés** : le Vol. I ch. 3 et le Vol. II ch. 1, 2, 7 décrivent l'état antérieur **à leur date de gel**, et le Vol. II l'écrit lui-même en toutes lettres — *un chapitre gelé douze jours avant une révision annoncée décrit en connaissance de cause un état daté* | Veille §4.1 (**à jour**) ; Vol. I ch. 3, Vol. II ch. 1, 2, 7 (**périmés, non corrigés**) |
| après le 26 août 2026 | Texte final du règlement du cadre bancaire canadien ; arrêté désignant l'organisme de normalisation | Veille §8.4 ; Vol. II ch. 14, 15, 24 |
| cible T4 2026 | Lancement effectif du RTR — cible précédée de quatre cibles abandonnées depuis 2019 | Veille §8.4 ; Vol. II ch. 15, 24 |
| 2 décembre 2026 | Marquage des contenus générés (règlement européen sur l'IA) | Veille §8.1, §12 |
| **1er mai 2027** | Entrée en vigueur simultanée d'E-23 (BSIF) et de la ligne directrice IA de l'AMF | Veille §4.11.5, §8.4 ; Vol. I ch. 5 à 7 ; Vol. II ch. 9, 11, 20 |
| continue | Trajectoire du projet de loi C-36 | Veille §8.4 ; Vol. II ch. 10 |

## Avertissements

- **Aucun avis juridique ni conseil d'investissement.** Ces ouvrages rapportent des textes et en
  proposent des lectures d'architecture qui engagent leur auteur seul.
- **Aucune recommandation de fournisseur.** Les instanciations sur une pile d'éditeur (IBM
  notamment) sont des cas documentés, pas des verdicts comparatifs.
- **Statuts et chiffres.** Les métriques d'adoption sont, sauf mention contraire, auto-déclarées
  par les acteurs et attribuées comme telles ; les statuts *preview* ne sont jamais présentés comme
  *disponibilité générale* ; les projections d'analystes portent leur millésime.
- **Lacunes exposées, non comblées.** Le Vol. II en recense onze ; le Vol. III, **vingt-deux** — dont
  **trois closes**, et non quatre : son PRD §10 ne porte « INSTRUITE ET CLOSE » qu'aux entrées 1, 2
  et 11, la 10 étant « instruite, non arbitrée » et la 15 « instruite, **non close** » ; la veille,
  **vingt-cinq questions ouvertes** (§11, cardinal confirmé par
  `check-veille.py`). Aucune n'est comblée par une
  source de moindre qualité.
- **Assistance par agents.** Ces travaux ont été produits avec l'assistance de pipelines de
  recherche multi-agents, selon les méthodes de vérification décrites dans chaque document ; la
  responsabilité éditoriale est celle de l'auteur.

## Notes de maintenance

Le `README.md` de la racine a été resynchronisé le 18 juillet 2026 sur
l'arborescence réelle, sur l'accession du Vol. III à une gouvernance complète (`doc/`) et sur les
décomptes **re-mesurés** — veille 142 p. / 244 réf. / 14 sections, Vol. I
569 p. / 69 p. / 28 diagrammes / 12 ADR, Vol. II 387 p. / 66 p. / 29 pièces / 46 entrées de socle,
tous inchangés. Le 23 juillet 2026, la passe complémentaire de la veille (sous-section 12.4,
l'après-agentique en préimpression) porte ses décomptes à **144 p. / 256 réf.**, re-mesurés sur le
PDF régénéré ; les chiffres du 18 juillet ci-dessus décrivent l'état de cette date-là. La passe de
révision du même 23 juillet (corrections vérifiées et aération des sections 4.10 et 10, en vue de
la publication arXiv) porte la pagination à **145 p.**, références inchangées. Une dernière passe du
même 23 juillet — révision interne à six dimensions (retrait du saut de page avant la section 13,
34 correctifs vérifiés) puis correction du sourcing du cas d'adoption de Block (§6.4, référence [257]
ajoutée) — porte les décomptes à **146 p. / 257 réf.**, re-mesurés sur le PDF régénéré.

Le même 23 juillet 2026, une passe de cohérence a réaligné les `README.md` sur l'état
réel du dépôt : Vol. IV porté à **TOC v0.11** (57 chapitres, 10 livres, ≈ 369 000–394 000 mots
projetés) avec son `README.md` ; renommage `doc/` → `prd/` (Vol. II) et
suppressions des articles de synthèse et des `index.html` (Vol. I et II) constatés **committés**
(commit `fd8f1be`, arbre de travail propre) ; création du pipeline FESP du Vol. III (troisième copie
indépendante) enregistrée ; nom du dépôt corrigé de « Monographies » en `Agentique` dans les
fichiers du démonstrateur `Borealis-Go`.

**Le 25 juillet 2026**, les cinq `README.md` du dépôt ont été resynchronisés
sur la restructuration du commit `60f57f6` : renommages `1 - Corpus Agentique/` → **`1 - Corpus/`**
et `2 - Compendium Agentique/` → **`2 - Compendium/`** répercutés dans tous les chemins et tous les
liens ; **suppression du démonstrateur `Borealis-Go/`** consignée là où il était annoncé comme
livrable vivant (README de la racine et du Vol. I), avec ses conséquences sur la
référence [217] de la veille — signalées, **non corrigées dans la veille**. Décomptes **re-mesurés
sur pièce** à cette date, tous inchangés : veille **146 p. / 257 réf.** (`python check-veille.py`,
sortie 0), Vol. I **569 p. / 28 diagrammes**, Vol. II **387 p. / 29 pièces**, Vol. III **427 p. /
34 pièces / 30 rapports de vérification**. Un renvoi cassé a été corrigé dans le périmètre de la
passe — les quatre lignes `../doc/…` de `…/2 - OrchestrationAgentique/monographie/README.md`,
repointées vers `../prd/…`.

**Le 29 juillet 2026**, ce `README.md` a été resynchronisé sur **l'ajout de [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf)** et sur le
quatrième pipeline qui le compose : chaînes de rendu portées de quatre à **cinq**, arborescence du
Vol. IV réalignée sur ses cinq Livres et son `build/`, règle du « PDF versionné avec sa source »
étendue au compendium. Décomptes **re-mesurés sur pièce** à cette date : **847 pages**
(`pypdf`, sur le PDF versionné), **50 chapitres en 5 livres** et **23 renvois marqués d'une dague**
(sortie de `build/assemble.py`), **159 entrées** au socle consolidé, TOC **v0.30** et PRD **v0.14**.
⚠ **Aucun de ces chiffres ne requalifie le volume** : les cinquante chapitres demeurent un brouillon
non publiable, et *composer n'est pas publier*. Le reste de l'état du Vol. IV — issues des remontées,
volumétrie par Livre, décisions d'auteur — vit aux documents de gouvernance du volume et n'est pas
repris ici.

**Le 29 juillet 2026, seconde passe du même jour** : le Vol. IV est **arrêté en révision finale pour
une diffusion en bibliothèque personnelle** (décision d'auteur **D-10**, PRD **v0.15** §14, TOC
**v0.31**), et les porteurs de statut ont été réalignés — ce `README.md`
et les deux fichiers du volume. Le **colophon** du rendu a été
récrit et [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) **recomposé** : **847 pages**,
re-mesurées (`pypdf`). ⚠ **Un défaut de composition a été trouvé et corrigé dans la passe** : le
colophon allongé débordait sur une seconde page — *la page de titre doit rester unique*, et seul le
décompte de pages l'a montré, aucun contrôle ne voyant cette classe. **Conformité arrêtée sous trois
états** : **satisfaite sur pièce** (G-2, G-3, G-7, plus les quatre contrôles rejoués le même jour,
sorties 0), **close pour ce seul régime par dérogation nommée** (G-1 résiduel, G-4 fond, G-5 balayage,
G-6 lots), **non satisfaisable** (CA-IV-11, CA-IV-13). ⚠ **Aucun de ces gestes ne rend l'ouvrage
publiable** : *arrêter n'est ni terminer ni publier*, et la dérogation tombe à la première diffusion.

**Le 29 juillet 2026, troisième passe du même jour** : sur instruction d'auteur, le rendu du Vol. IV
reçoit une **annexe hors plan après le chapitre 50** —
`audit-references.md`, l'**inventaire et la validation des
159 références** du socle consolidé. Décomptes **re-mesurés sur pièce** : **863 pages** (`pypdf`, sur
le PDF versionné), **50 chapitres en 5 livres plus 1 annexe** et **23 renvois marqués d'une dague**
(sortie de `build/assemble.py`). ⚠ **Trois choses que cette passe ne fait pas.** *(a)* Elle **n'ajoute
aucune annexe au plan** : l'annexe n'est **aucune des neuf A à I** du `TOC.md`, et l'**Annexe I — la
bibliographie générale consolidée — reste à écrire** ; le compendium **n'a toujours pas de
bibliographie**, ni la moindre URL. *(b)* ⚠ **Être relié n'est pas faire autorité** : c'est un
**rapport de mesure sans autorité**, du régime d'`audit.md`, **jamais
citable à l'appui d'un énoncé** ; ses constats sont des **remontées non arbitrées**. *(c)* Elle **ne
consomme aucun numéro de chapitre** — le plafond de cinquante tient —, **ne franchit aucune porte** et
**ne requalifie rien**. Le `TOC.md` et le `PRD.md` **ne sont pas touchés** : *un rapport remonte, il ne
tranche pas.*

**Le 29 juillet 2026, quatrième passe du même jour** : l'annexe reliée est **simplifiée en une liste**,
sur instruction d'auteur. Le rendu reçoit désormais
[`annexe-references.md`](2%20-%20Compendium/annexe-references.md) — les **159 entrées** du socle,
identifiant, objet, niveau, provenance et datation de la source, groupées par volume d'origine — à la
place du rapport d'analyse. Le rapport reste alors au dépôt sous le nom `audit-references.md`, **hors
rendu**, avec son régime inchangé — sans autorité, jamais citable à l'appui d'un énoncé. *Les deux se
distinguent par leur nom : l'`annexe-` est reliée, l'`audit-` ne l'est pas.* ⚠ **Ce constat a été
dépassé depuis** : `audit-references.md` a été retiré de l'arbre, comme `audit.md` et `eval.html` — les
trois ne se lisent plus qu'à l'historique git (voir « Restent ouverts »). Décomptes **re-mesurés sur
pièce** : **1 114 pages** au 8 août 2026, après la refonte typographique du 31 juillet 2026 ; l'annexe pesait dix pages au gabarit de la refonte
Springer, contre vingt-sept
pour le rapport — ⚠ *ce coût-là n'a pas été re-mesuré au gabarit neuf.* La ligne de `sed` qui élargissait
les tables à sept colonnes est **retirée du script**, sa grille n'étant plus composée. ⚠ **Ce que la
passe ne change pas** : l'annexe **n'est toujours aucune des neuf annexes A à I**, elle **n'est pas une
bibliographie** — elle inventorie des **faits**, non les **documents** dont ils proviennent —, et
l'**Annexe I reste à écrire**. ⚠ **Ce dernier point a cessé d'être vrai le lendemain, et ce fichier ne
le portait pas** : l'**Annexe I existe depuis le 30 juillet 2026** —
[`annexe-bibliographie.md`](2%20-%20Compendium/annexe-bibliographie.md), **1 154 entrées uniques**,
réunion verbatim et dédoublonnée des bibliographies des trois volumes sources. *Elle est une réunion,
non une vérification* : son propre régime interdit d'y lire le niveau de preuve d'un fait, qui se lit
à l'entrée de socle. Le compendium a donc une bibliographie ; il n'a toujours **aucune URL**.

**Le 29 juillet 2026, cinquième passe du même jour** : l'**édition d'août 2026 de la veille
technologique**, sur instruction d'auteur — « fondée sur le compendium et une recherche exhaustive
sur le net ». Faits **gelés au 29 juillet 2026**, édition datée du 1er août. Décomptes
**re-mesurés sur le PDF régénéré** : **159 p. / 266 réf.** (contre 146 / 257), 14 sections et
15 tableaux inchangés, `python check-veille.py` en sortie 0. **Ce que la passe verse** : la révision
**2026-07-28** de MCP — noyau sans état, `server/discover`, requêtes à plusieurs allers-retours,
routage par en-têtes, dépréciation de Roots, Sampling, Logging et de l'enregistrement dynamique de
client, et **première politique de dépréciation datée** du corpus protocolaire (§4.1) ; le fait de
tempo qui lui répond — **A2A n'a rien publié depuis le 28 mai 2026** (§4.2) ; le **règlement (UE)
2026/1744**, publié au JO le 24 juillet et en vigueur le 27, avec ce qui s'applique **le 2 août
2026** malgré le report du haut risque (§8.1) ; la charte du second groupe communautaire du W3C
(§5.2) ; les superpositions COSAiS du NIST (§8.2) ; l'échéance du rail canadien (§8.4) ; et
**deux sous-sections neuves sur le corpus compagnon** (§13.8, §13.9). ⚠ **Trois choses que cette
passe ne fait pas.** *(1)* **Son régime est plus faible et il est déclaré** : consultation directe
des sources primaires, **sans ronde de vérification adverse** — celui de la §12.4, non celui des
§4.6 à §4.13 (§2.2 et §10). *(2)* Elle **n'a pas versé** les métriques d'adoption les plus citées du
domaine, faute d'avoir atteint leur publication primaire (§6.5) — *un chiffre qu'on ne peut pas
rattacher à son éditeur n'est pas un fait affaibli, ce n'est pas un fait*. *(3)* Elle **ne fait
reposer aucun énoncé sur le Vol. IV arrêté** : le refus est inchangé, ses **motifs le sont
entièrement** — diffusion bornée sans opposabilité, socle dérivé sans source primaire propre,
dérogation conditionnelle (§13.8). ⚠ **Deux défauts de la passe sont consignés plutôt que tus, et
aucun des deux n'a été trouvé par le contrôle seul.** `check-veille.py` a rattrapé **trois doublons
bibliographiques** que la rédaction avait introduits — AIP [23], le groupe W3C d'identité d'agents
[31] et la page des publications d'A2A [98] figuraient **déjà** au corpus, et le protocole AIP y
était même **discuté au corps** ; les entrées surnuméraires ont été retirées. Mais **cinq renvois
visaient la section 4.2 pour MCP, qui est la section 4.1** : *un renvoi qui existe mais désigne la
mauvaise section, aucun contrôle ne le voit* — seule la collation du plan réel l'a montré. Un
sixième écart est **signalé sans être corrigé**, la règle du dépôt l'interdisant : la réf. [217]
pointe un démonstrateur retiré de l'arbre le 25 juillet 2026, et la limite est portée à la §10 de
l'édition plutôt qu'à la référence.

**Le 29 juillet 2026, sixième passe du même jour** : deux **budgets de mise en page** posés par
l'auteur sur la veille — le **résumé doit tenir sur la page de titre**, le **sommaire exécutif sur
trois pages** (5, 6 et 7). Les deux étaient enfreints par la passe précédente, et **le premier
silencieusement** : le gabarit Typst compose le résumé dans un bloc **qui ne se scinde pas**, si bien
qu'un résumé trop long ne passe pas à la page suivante — il **se fait rogner sous la marge**, et
`pandoc` sort sans erreur. Mesuré sur le PDF : la dernière ligne du résumé tombait à **y = −24,6 pt**,
soit **98 pt sous la marge basse** (73,7 pt), et le sommaire mordait de **344 caractères** sur une
quatrième page. **Corrigé par condensation, en trois passes mesurées** : le résumé passe de
**3 451 à 2 750 caractères** et de six paragraphes à quatre — la grille des cinq questions rejoint le
paragraphe des couches, dont elle est le diagnostic — ; les constats 11 et 12 sont resserrés ; et
« Méthode en bref » perd son détail par édition, qui vit déjà en §2.2 et n'a rien à faire dans un
sommaire. **Aucun énoncé n'est retiré**, et l'occasion a servi à corriger une formule que la §13.8
avait périmée : le résumé disait « deux cadrages », il dit désormais **quatre volumes tous rédigés
dont deux ne fournissent aucun fait**. **État vérifié sur le rendu** : résumé à **y = 104,8 pt**
(31 pt de dégagement), sommaire **pages 5-7**, « 1 Introduction » en page **8**. Décomptes re-mesurés :
**158 p. / 266 réf.**, `check-veille.py` en sortie 0. ⚠ **Aucun contrôle ne voit ce budget** — ni
`check-veille.py`, ni le rendu : *un débordement qui se fait rogner ne lève aucune erreur.*

**Le 29 juillet 2026, septième passe du même jour** : la veille reçoit le titre que l'auteur énonce —
**« Interopérabilité et orchestration agentique en entreprise »** — et, avec lui, la section qui le
rend exact. ⚠ **Le titre antérieur disait « orchestration des processus d'affaires », et l'écart
n'était pas de style mais de périmètre** : les six sous-sections de la §4.11 traitent toutes de
l'orchestration des *processus*. Le balayage du document entier a mesuré l'autre orchestration —
celle des *agents* — à **zéro occurrence** sur douze motifs (« orchestration multi-agent », « patron
d'orchestration », « agent superviseur », « framework d'agents », « planificateur », *handoff*,
*swarm*, « sous-agent », « graphe d'agents », « délégation hiérarchique », « mémoire partagée »,
ReAct). **La réponse est une sous-section neuve, la §4.14**, fondée sur la recherche `/last30days`
(« Agentic interoperability and orchestration in the enterprise » — 45 éléments, 3 sources sur 5 ;
X et YouTube absents faute d'authentification) puis **sur sources primaires vérifiées** : la
taxonomie **MAST** (quatorze modes en trois catégories, 150 traces annotées, validée sur plus de
1 600 traces de sept cadriciels), la documentation du SDK d'agents d'OpenAI (les transferts *sont*
des outils, `transfer_to_<nom_agent>`, historique complet transmis par défaut), la bibliothèque
`langgraph-supervisor`, et l'annonce de disponibilité générale du harnais géré d'AgentCore — **déjà
au corpus en réf. [106]**, doublon que `check-veille.py` a repris. Trois références neuves, [267] à
[269]. ⚠ **Le fait négatif est le cœur de la section** : *aucun* des trois protocoles ne décrit de
topologie d'orchestration, et c'est pourquoi elle **n'est pas comptée comme une huitième couche** —
les sept ont chacune un porteur candidat, celle-ci n'en a aucun. **Le décompte de sept est
maintenu.** ⚠ **Et la passe a trouvé mieux qu'un manque : la lacune était celle de la veille
seule.** Le **ch. 2 du Vol. I** traite ce front depuis juin 2026 — balayage sur pièce : six
occurrences de MAST, sept de ReAct, sept de l'orchestrateur, trois du sous-agent, deux du
superviseur, trente-sept de la mémoire. *C'est exactement la classe de défaut que la §13 prend pour
objet — une lacune de couverture d'un document du dépôt, comblée par le texte rédigé d'un autre.*
Une question ouverte s'ajoute (**QO 25**, cardinal porté à vingt-cinq). ⚠ **Ce que la passe a refusé
de verser** : les cinq patrons canoniques tels que les publient les blogues de contenu, et le chiffre
très cité « LangGraph dans 43 % des déploiements agentiques d'entreprise » — aucune publication
primaire atteinte. Décomptes re-mesurés : **161 p. / 269 réf.**, `check-veille.py` en sortie 0, et
**les deux budgets de mise en page tiennent** (résumé à y = 104,8 pt ; sommaire en pages 5-7).

**Le 29 juillet 2026, huitième passe du même jour — la passe de dépôt final** : les **onze `README.md`**
que portait le dépôt ont été relus et resynchronisés, sur instruction d'auteur, et **un douzième
`README.md` a été déposé** — celui du Vol. III. *(Cardinal re-compté sur l'arbre à cette date :
**12 `README.md`** après la passe.)* **Ce que la passe a trouvé, et corrigé.** *(1)* **Six estampilles de version périmées**, toutes
décrivant un état *courant* et non un fait daté : ce `README.md` annonçait **TOC v0.30 / PRD v0.14** en
deux endroits (section du Vol. IV et arborescence) alors que le dépôt porte **v0.31 / v0.15** ; la
gouvernance du Vol. IV annonçait **PRD v0.11 et TOC v0.26** dans sa
section d'autorité, soit quatre et cinq versions de retard, et créditait `check-compendium.py` de
**P1-P7 / 15 mutations** quand le script en porte **P1-P8 / 17**. ⚠ *Une estampille de version en retard
ne se distingue d'un constat daté que par sa fonction : celle qui dit « voici l'autorité courante » est
fausse, celle qui dit « voici ce que la passe a lu » est exacte.* *(2)* **Le Vol. III a reçu son premier
[`README.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/README.md)** : il était **le seul des trois
volumes à n'en porter aucun**, et le lecteur n'avait aucune entrée qui lui fût destinée.
Document **dérivé**, sans fait neuf. *(3)* **Deux `.pyc` versionnés de plus** ont été relevés
sous `2 - Compendium/PRD/__pycache__/` — le total suivi est de **trois**, non d'un —, et l'**absence de
licence à la racine** est portée au tableau des reliquats. ⚠ **Ni l'un ni l'autre n'est corrigé ici** :
retirer un fichier versionné et déposer une licence sont des gestes qui se demandent. **Décomptes
re-mesurés sur pièce à cette date, tous inchangés** : veille **161 p. / 269 réf.**
(`check-veille.py`, sortie 0), Vol. I **569 p. / 28 diagrammes** (motif ancré), Vol. II **387 p. /
29 pièces**, Vol. III **427 p. / 34 pièces / 30 rapports**, Vol. IV **863 p.** *(⚠ chiffre de la passe,
rétabli le 8 août 2026 : ce fichier portait ici **1 096 p.**, valeur postérieure à la refonte du
31 juillet et **indûment reversée dans un constat daté du 29** — la passe du 4 août l'avait classée
parmi les deux occurrences « à laisser telles quelles », à tort)* **/ 50 chapitres /
159 entrées de socle**, et les **quatre contrôles du Vol. IV en sortie 0** — `check-toc.py`,
`check-sieges.py` (**26 sièges sur 50 pièces**), `check-compendium.py` (**P1-P8**, trois rapports
déclaratifs), `decompte.sh`. ⚠ **Ce que la passe ne fait pas** : elle **ne requalifie aucun statut** —
le Vol. III reste non publiable, le Vol. IV **arrêté et non publiable** —, **ne touche à aucune pièce
rédigée**, **ne corrige pas la veille** et **ne referme aucune remontée**. *Resynchroniser des
porteurs de décomptes n'avance aucune porte.*

**Le 4 août 2026** — passe documentaire — ce `README.md` et le
[conspectus du Vol. IV](2%20-%20Compendium/README.md) ont été resynchronisés sur le dépôt de
[`Compendium.html`](2%20-%20Compendium/Compendium.html), **appareil de lecture à l'écran** du
compendium : déposé le même jour sous le nom `presentation.html` (commit `76d001c`), révisé deux
fois, puis renommé (commit `d473913`). **Ce que la passe enregistre** : un fichier de **1,75 Mio**
(1 829 940 octets — *la passe avait écrit 1,79 Mio, conversion fausse de son propre décompte d'octets*),
**sans dépendance externe** et à **un seul lien sortant** — vers le PDF —, **118 figures SVG
embarquées** en `data:` (relevé sur pièce : 118 occurrences, autant que le rendu imprimé en porte),
douze entrées de sommaire, et une **horloge calculée à l'ouverture**. **Ce que la passe refuse de
laisser croire, et c'est le fond de l'entrée** : ⚠ **cette page ne se régénère pas.** Le balayage de
[`2 - Compendium/build/`](2%20-%20Compendium/build/) ne trouve **aucun générateur HTML** — les cinq
chaînes du dépôt ne produisent que des PDF —, si bien que `Compendium.html`, comme les **cinquante
pages de chapitre** déposées avant elle, est **écrite à la main et relevée à la main**. *La règle du
« rendu versionné avec sa source » ne s'y applique donc pas, et rien ne signale qu'elle a pris du
retard.* ⚠ **Elle ne requalifie rien** : dérivée, sans autorité — son colophon le déclare —, **non
publiée**, et tenue par le régime de **D-10** comme l'est le PDF.

**Trois défauts trouvés dans la passe, tous par ouverture de la pièce, aucun corrigé ici.** *(1)* ⚠
**Le décompte de pages du compendium est faux à ce `README.md`** : `pypdf` mesure **1 114 pages**
sur le PDF versionné, quand ce fichier en annonce **1 096** — le conspectus du volume et le colophon
de `Compendium.html`, eux, portent le bon chiffre. Le motif compte **sept occurrences**, mais elles
ne sont pas du même régime : **cinq annoncent un état courant** (encadré d'entrée, tableau d'état,
section du Vol. IV, arborescence, commentaire de la commande de rendu) et sont **fausses** ; **deux
sont des constats datés** des passes du 29 juillet, et *un constat daté ne retarde pas, il
enregistre.* La correction porte donc sur **cinq lignes**, et elle se demande. *(2)* ⚠ **Trois liens de ces `README.md` ne pointent sur
rien** — `audit.md`, `audit-references.md` et `eval.html` sont cités par la racine, le conspectus,
le `PRD.md`, le `TOC.md` et le ch. 4, et **ils ne sont ni sur le disque ni au suivi git**. *Un renvoi
vers un fichier absent, aucun des quatre contrôles du volume ne le voit.* *(3)* Le PDF s'appelle
`Compendium.pdf` sur le disque et `compendium.pdf` à l'index git, que `core.ignorecase` rend aveugle
à l'écart : les liens résolvent — ils visent le nom indexé —, mais **le premier dépôt fait sur un
système sensible à la casse produira un renommage fantôme**. **Décomptes re-mesurés sur pièce à
cette date** : `Compendium.html` **1 829 940 octets / 118 figures embarquées** ; `compendium.pdf`
**1 114 p.** (`pypdf`) ; **12 `README.md`** au suivi git, cardinal inchangé depuis le 29 juillet —
**deux d'entre eux sont touchés par la passe**, la racine et le conspectus du Vol. IV. ⚠ **Ce que la
passe ne fait pas** : elle **ne touche à aucune pièce
rédigée**, **ne franchit aucune porte**, **ne corrige aucun des trois défauts** et **ne publie rien**.

⚠ Le décompte des diagrammes du Vol. I se mesure avec un motif **ancré** :
`grep -c '^```mermaid'` donne 28. Le motif non ancré en retourne 29 — il attrape une ligne de prose
de la note de production qui cite la balise.

**Le 8 août 2026** — passe d'audit et de correction — les **197 fichiers `.md` du dépôt et le
compendium entier** ont été audités, et **les correctifs ont été appliqués**, non seulement signalés.
C'est ce qui distingue cette passe des précédentes : *les trois défauts que la passe du 4 août avait
trouvés sans les corriger sont refermés ici*, et le tableau des reliquats a été récrit sur mesure
plutôt que reconduit. Chaque chiffre ci-dessous a été **re-mesuré sur la pièce**, par un bâtisseur puis
par un critique en contexte neuf qui ne connaissait pas son travail.

**Ce que la passe a corrigé.**

- ⚠ **La pagination du compendium était fausse partout où elle s'annonçait au présent** : **1 114 p.**
  mesurées, contre **1 096** à ce fichier (cinq annonces) et **810** à six autres — le tableau d'état,
  le paragraphe des régimes de la veille, `1 - Corpus/README.md` et les cinq `Livre */README.md`.
  ⚠ *Deux constats datés du 29 juillet portant 847 et 863 pages sont laissés tels quels : un constat
  daté enregistre, il ne retarde pas.*
- ⚠ **La gouvernance du Vol. IV avait neuf jours de retard, et c'est le plus gros écart de la passe** :
  ce fichier annonçait l'ouvrage **arrêté** sous **D-10 / PRD v0.15 / TOC v0.31**, alors que **D-11
  a rouvert cet arrêt le 30 juillet 2026** (**PRD v0.16 §15, TOC v0.32**) sur un rapport d'arbitrage
  externe. *Une estampille d'autorité courante en retard ne se rattrape pas par une note : elle est
  fausse.* Corrigée en cinq endroits, et la réouverture est désormais exposée.
- **L'écart de casse du PDF est refermé aux deux bouts** : l'index git est normalisé sur le disque
  (`compendium.pdf` → **`Compendium.pdf`**) et **`build/build-pdf.sh` écrit désormais le nom
  canonique**. ⚠ *Le second geste était indispensable au premier* : le script composait en minuscule,
  si bien que la première recomposition après le renommage aurait produit un **second fichier** au lieu
  de remplacer le rendu versionné. Trente et quelques renvois repointés, dont deux `href` de
  `Compendium.html` — GitHub est sensible à la casse.
- **Renvois internes morts : 151 → 6** (hors produit d'assemblage), sur 1 641 liens relatifs balayés.
  Les **48 renvois du `monographie/` du Vol. II** sont repointés vers `prd/`, les **17 locateurs
  `fichier.md:ligne`** de son `audit.md` convertis en ancres `#L21` — *préfixer `../` ne suffisait pas,
  le suffixe invalidant le chemin* —, et les renvois vers les fichiers **supprimés délibérément**
  (`audit.md`, `audit-references.md`, `eval.html`, six `CLAUDE.md`, les scripts de `.claude/skills/`)
  sont retirés en conservant les noms et en datant le retrait.
- **L'assemblage du Vol. II est remis en service** — le script cherchait `TOC.md` à la racine du volume
  quand il vit dans `prd/`. ⚠ **Et la reprise a trouvé mieux que la panne annoncée** : les deux
  assembleurs ne rebasaient pas les cibles relatives des pièces, si bien que le **Vol. III portait le
  même défaut sans que rien ne le signale** — *le témoin réputé sain était malade de la même chose.*
  Les deux scripts sont corrigés et les deux `Monographie.md` régénérés ; contrôle préalable : chaque
  assembleur reproduit sa sortie versionnée **à l'octet près**.
- ⚠ **L'Annexe I n'était pas « à écrire » : elle existe depuis le 30 juillet 2026** —
  `annexe-bibliographie.md`, **1 154 entrées uniques**. Quatre documents la déclaraient manquante.
- **La veille : « vingt-deux questions ouvertes » contre vingt-cinq**, et le contredit venait de son
  propre appareil de contrôle — `check-veille.py` compte **25**, comme le tableau d'état du même
  fichier. *Un décompte faux à côté du contrôle qui le dément est le défaut le moins excusable du lot.*
- ⚠ **Le Vol. I annonçait ≈ 263 600 mots, qu'aucune commande du dépôt ne produit** : **233 257**
  (`wc -w`, point d'ancrage de `decompte.sh --verifier`) ou 225 258 (commande de référence). ⚠ **La
  correction a une conséquence que le corpus ne s'attendait pas à payer** : son agrégat passe de
  ≈ 516 500 à **486 206 mots**, et *il perd le seuil des 500 000 qu'il s'attribuait*.
- **Deux erreurs d'unité, mêmes octets mal convertis** : la passe du 4 août avait écrit **1,79 Mio**
  pour `Compendium.html` là où ses propres 1 829 940 octets en font **1,75** ; et le colophon du volume
  donnait « 12,7 Mo » pour le PDF là où 13 304 911 octets font **12,7 Mio** — 13,3 Mo. ⚠ **Le premier
  correctif a lui-même été repris par le juge de cette passe** : reporter 1,75 Mio au présent était
  faux, le fichier ayant changé depuis ; il pèse **1 826 464 octets, soit 1,74 Mio**, en fins de ligne
  `LF` pures. *Une conversion juste sur un décompte périmé reste un chiffre faux.*
- **Le registre de gel du Vol. IV** portait un total de Livre I faux de 3 903 mots (**71 980**, non
  68 077) et, par propagation, un agrégat et sept écarts en pourcentage faux.
- ⚠ **La couverture des figures était annoncée complète et ne l'est pas** : le conspectus et
  `Compendium.html` affirmaient que « les cinquante chapitres en portent au moins une ». Balayage des
  cinquante pièces : **quarante-neuf**. Le **ch. 28** n'en porte aucune, et le programme des figures dit
  pourquoi — il ne lui accordait que **deux candidates, toutes deux au barème B**, qu'une passe de
  barème A ne pouvait pas couvrir. *Le décompte de 118 figures est juste ; c'est la couverture qui ne
  l'était pas.*
- ⚠ **Le colophon attestait la non-blancheur d'un rendu qu'il n'avait plus** : « 0 sur **1 072**
  mesurées », sans date, deux lignes sous « 1 114 pages ». Le relevé est du **30 juillet 2026**, pris
  sur le rendu d'alors ; la refonte au format Letter du 31 juillet a porté l'ouvrage à 1 114 pages, et
  *l'attestation ne couvre pas les quarante-deux dernières.* Datée et bornée, non refaite.

**Ce que la passe a refusé de faire, et pourquoi.** Elle **ne requalifie aucun statut** — le Vol. III
reste non publiable, le Vol. IV en passe de révision ouverte —, **ne franchit aucune porte**,
**ne corrige pas la veille**, **ne referme aucune remontée** et **ne publie rien**. ⚠ **Elle laisse
aussi les constats datés qui divergent de la mesure d'aujourd'hui** : le PRD du Vol. IV crédite `P3` de
670 et `P5` de 9 là où le contrôle en mesure 674 et 12, mais ses deux tables se déclarent « constats
d'exécution du 29 juillet 2026 ». *Corriger un constat daté, c'est effacer la seule chose qu'il
apporte.*

⚠ **Une entorse à sa propre règle, déclarée plutôt que défaite.** La passe s'était interdit de toucher
à la **prose** d'une pièce rédigée, et un critique en contexte neuf a relevé qu'elle l'avait fait à
**deux annexes** du Vol. IV : `annexe-references.md` déclarait l'**Annexe I « reste à écrire »** — un
énoncé faux depuis le 30 juillet 2026 —, et `annexe-bibliographie.md` renvoyait au rapport
`audit-references.md` comme s'il était au dépôt. Les deux énoncés sont redressés, et **les cinquante
chapitres, eux, n'ont changé que par la cible de leurs liens** — deux fichiers, une ligne chacune, texte
visible identique. ⚠ *Le motif de l'exception est étroit et il ne s'étend pas* : une annexe qui se
trompe sur le **contenu de son propre volume** n'énonce pas un fait daté, elle induit en erreur sur
l'état présent du dépôt — ce qu'un audit ne peut pas laisser passer sans se contredire.

⚠ **Deux corrections de méthode, dont une contre cette passe elle-même.** *(1)* `pypdf`, que cinq
documents donnent pour instrument de pagination, **n'est pas installé** : les décomptes de cette passe
sont pris par lecture du `/Count` de l'objet `/Type /Pages`, et c'est cela qui est écrit. *(2)* ⚠ **La
passe a d'abord publié une mise en garde fausse contre un motif de comptage, et un critique l'a
reprise en réexécutant la commande — c'est le défaut le plus instructif du lot.** Trois choses en une
phrase, toutes vérifiées sur les cinq PDF du dépôt : le motif `/Type /Page` **avec l'espace rend 0**,
Typst écrivant `/Type/Page` sans espace ; le décompte doublé que la passe avait obtenu (2 228 pour
1 114) venait d'une **classe d'exclusion trop étroite** — elle écartait `/Type/Pages` mais laissait
passer `/Type/PageLabel`, dont il existe **un objet par page** ; et un motif correctement ancré rend
la pagination juste du premier coup — `grep -aoP '/Type/Page(?![sL])' | wc -l` donne **569, 387, 427,
1 114 et 161**. *Une commande de contrôle publiée sans avoir été réexécutée sur son domaine entier est
un instrument qui ment avec l'autorité d'une mesure* — et c'est précisément la classe de défaut que ce
dépôt prend pour objet.

⚠ Le décompte des diagrammes du Vol. I se mesure avec un motif **ancré** :
`grep -c '^```mermaid'` donne 28. Le motif non ancré en retourne 29 — il attrape une ligne de prose
de la note de production qui cite la balise.

**Restent ouverts, signalés et non corrigés** — re-mesurés le 8 août 2026. Ce sont des décisions
d'auteur, des contradictions à arbitrer, ou des renvois dont la correction exigerait une information
que le dépôt ne porte pas :

| Fichier | Reliquat |
|---|---|
| racine du dépôt | **aucune licence** : seul le Vol. I porte un `LICENSE`. Un dépôt final sans licence de tête laisse les quatre autres livrables sans régime déclaré — **décision d'auteur, expressément laissée ouverte** |
| `1 - Corpus/2 - OrchestrationAgentique/` | l'étiquette git `mono-v1.0` **n'est pas posée** — `git tag -l` est **vide** — alors que **quatre documents de gouvernance et dix-sept pièces** l'annoncent comme telle, dont l'une écrit « `mono-v1.0` existe ». Poser le tag, ou corriger ces mentions : **décision d'auteur**, la prose n'a pas été réécrite |
| `1 - Corpus/1 - InteroperabiliteAgentique/Chapitres/TOC.md` | l'Annexe B y est déclarée **≈ 17 500 mots** quand `wc -w` en mesure **20 655** (+18 %). La colonne « Méthode » dit honnêtement « décompte **déclaré** en tête d'ADS », mais l'en-tête du même fichier revendique que tout décompte est **relevé, non projeté** — **contradiction interne à arbitrer** |
| `1 - Corpus/2 - OrchestrationAgentique/` | **trois volumétries concurrentes, toutes justes sous leur méthode** : 92 059 (PRDPlan §4.2, locale par défaut — chiffre publié), 93 242 (`decompte.sh`, locale UTF-8, où l'espace insécable sépare), 90 362 (clôture de P4, datée). Le §4.2 documente lui-même son sous-comptage de 1,3 % et **refuse** de le corriger : aucune n'est fausse, et le choix est éditorial |
| `2 - Compendium/` — volumétries des cinq `Livre */README.md` et colonne `Réel` du registre de gel | périmées de quatre passes de révision du français (31 juillet → 3 août 2026). ⚠ **Non corrigées pour une raison de contrôle, non de paresse** : la colonne est **opposée par `check-compendium.py` P6 aux en-têtes des cinquante pièces**, qui sont de la prose gelée — la corriger d'un seul côté ferait échouer P6 sur 26 lignes. La mesure courante (**331 791 mots**) est écrite au registre avec ce motif |
| `2 - Compendium/Compendium.html` + les 50 `.html` de chapitre | **aucune chaîne ne les régénère** : `build/` ne porte pas de générateur HTML, ces pages sont écrites et relevées à la main. La règle du « rendu versionné avec sa source » ne s'y applique pas — *le retard sur le `.md` ne se signale nulle part* |
| `2 - Compendium/Livre */README.md` | leurs blocs de procédure invoquent `rendre-piece.py` et `verifier-piece.py`, **scripts d'un skill supprimé le 31 juillet 2026** (commit `41666d0`). Le retrait est désormais déclaré à chaque fichier, mais les commandes sont laissées telles quelles : **le dépôt ne dit pas par quoi elles ont été remplacées** |
| `2 - Compendium/` — `audit.md`, `audit-references.md`, `eval.html`, six `CLAUDE.md`, `.claude/skills/` | **supprimés délibérément** (`f6183bf`, `73e7c4e`, `982ef3a`, `41666d0`), et non perdus : ils se lisent à l'historique git. Les renvois qui les visaient sont retirés, le retrait daté. ⚠ *Le rapport d'arbitrage `eval.html` qui a déclenché **D-11** est dans ce lot : la décision est opposable, la pièce qui la motive ne se lit plus qu'au journal* |
| `1 - Corpus/3 - EntrepriseAgentique/verification/lot-L-04-…md` | **cinq renvois morts conservés à dessein** : ce sont les liens relatifs internes de pages tierces, reproduits **verbatim** dans des blockquotes de preuve. Les réécrire altérerait la citation, qui est l'objet même d'un rapport de lot |
| `1 - Corpus/3 - EntrepriseAgentique/prd/PRDPlan.md` | un sixième renvoi « mort » est un **faux positif** : le chemin vit dans un bloc `sh` clôturé, c'est le **gabarit d'en-tête de pièce**, correct à la profondeur de sa destination. Y toucher casserait le gabarit |
| Vol. I et Vol. III — `Chapitres/TOC.md`, `monographie/`, `prd/`, `verification/` | citent `Borealis-Go` et `Synthese Monographie.md`, retirés du dépôt les 25 et 22 juillet 2026 : **citations exactes, plus opposables**, à consigner et non à réécrire. Le tableau des livrables du Vol. I porte désormais ce régime en clair |
| `2 - Compendium/README.md` | l'énumération des entrées de `Compendium.html` en **nomme treize** pour un cardinal de **douze**, exact par ailleurs : elle omet la zone VIII, « L'appareil ». Écart de rédaction, non de mesure |
| `2 - Compendium/` | le compendium **n'a toujours aucune URL** : son Annexe I réunit les bibliographies des sources sans en vérifier une seule, et *une entrée présente n'y atteste de rien* |

⚠ **Aucune publication GitHub Pages, pour aucun volume.** ⚠ **La formule antérieure — « plus de
pages de présentation » — a cessé d'être exacte le 4 août 2026** et elle est corrigée ici : le
Vol. IV en porte désormais, [`Compendium.html`](2%20-%20Compendium/Compendium.html) et les cinquante
pages de chapitre. *Ce qui a disparu n'est pas la page de présentation, c'est sa publication en
ligne* — les nouvelles ne sont **pas publiées** et se lisent depuis le dépôt, en local. Les deux
`index.html` (Vol. I et Vol. II) ont été supprimés le 22 juillet 2026 (commit `fd8f1be`). Ils
annonçaient « Lire en ligne » sous `https://agbruneau.github.io/Monographies/…`, et leurs balises
`canonical`, `og:url` et liens « Dépôt GitHub » nommaient tous `Monographies` — adresses fausses de
toute façon, le dépôt s'appelant `Agentique` (`github.com/agbruneau/Agentique`), et cause des 404
relevés. Rétablir une publication en ligne supposerait de repartir de la bonne base
(`https://agbruneau.github.io/Agentique/`) et de vérifier que Pages est bien activé pour ce dépôt.
