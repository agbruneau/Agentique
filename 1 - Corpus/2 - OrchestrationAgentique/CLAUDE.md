# CLAUDE.md — volume II (L'autonomie encadrée)

Guide pour Claude Code (claude.ai/code) **dans ce dossier**.

## Périmètre de ce fichier

Ce `CLAUDE.md` ne régit que le **volume II**, sous `1 - Corpus Agentique/2 - OrchestrationAgentique/`. Il ne dit rien des autres livrables du dépôt *Agentique* (`github.com/agbruneau/Agentique` — **pas** « Monographies », nom qui ne survit que dans le contenu gelé de la veille) :

| Ce que vous cherchez | Où |
|---|---|
| Place du volume II dans le corpus, ordre de lecture, divergences entre volumes | [README du dépôt](../../README.md) |
| Conventions communes et conventions de la veille technologique (racine) | [`CLAUDE.md` du dépôt](../../CLAUDE.md) |
| Volume I — *Interopérabilité agentique* (cadre mondial), **présupposé par ce volume** | [`1 - InteroperabiliteAgentique/CLAUDE.md`](../1%20-%20InteroperabiliteAgentique/CLAUDE.md) |
| Index de lecture des 29 pièces | [`monographie/README.md`](monographie/README.md) |

⚠ **Les conventions divergent entre volumes** — commits en anglais ici (Conventional Commits), en français au volume I ; autorité PRD ici, conventions de chapitres là-bas. Vérifier le dossier de travail avant d'appliquer une règle.

## Nature du volume

Projet documentaire. Livrable : une monographie exhaustive — « L'autonomie encadrée », titre **arrêté** (`prd/TOC.md` §Titre, et fixé en dur dans `build/assemble.py`) — sur l'interopérabilité et l'orchestration agentique en écosystème d'entreprise de services financiers au Canada. Les deux PDF académiques dans le socle (F-36, F-37, dans `prd/`) sont des sources analysées et intégrées au PRD ; ne pas les supprimer.

**Emplacement des documents de gouvernance** : PRD.md, PRDPlan.md, TOC.md, audit.md et les deux PDF académiques vivent dans **`prd/`**. ⚠ Le dossier a été **déplacé deux fois** — de la racine du volume vers `doc/` le 17 juillet 2026, puis de `doc/` vers `prd/` (**renommage committé le 22 juillet 2026**, commit `fd8f1be`, arbre de travail propre). Aucun des renvois n'a suivi ; l'état, re-mesuré le 22 juillet 2026 :

| Fichier | Renvoi cassé | Cible réelle | Décompte |
|---|---|---|---|
| `monographie/**` — **le plus gros gisement** | renvois vers `TOC.md` répartis sur **28 des 29 pièces** (bandeaux de thèse) : 47 en `](../../TOC.md)`, 1 en `](../TOC.md)` | `../../prd/TOC.md` (resp. `../prd/TOC.md`) | **48** |
| `build/assemble.py` | `ROOT / "TOC.md"` (racine du volume, ligne 78) — **pipeline PDF hors service** | `prd/TOC.md` | 1 |
| `monographie/README.md` | `](../doc/PRD.md)`, `](../doc/PRDPlan.md)` (×2), `](../doc/TOC.md)`, `](../doc/audit.md)` — rectifiés vers `doc/` en juillet, **re-cassés par le renommage** | `../prd/…` | 4 lignes |
| `prd/PRDPlan.md` | `](CLAUDE.md)` | `../CLAUDE.md` | 1 |
| `prd/audit.md` | `](monographie/…)` | `../monographie/…` | 15 |
| `verification/relecture-CA.md` | `](../PRD.md)`, `](../PRDPlan.md)`, `](../audit.md)` | `../prd/…` | 3 |

Commandes de contrôle, à relancer **sur tout le dossier** avant de déclarer le gisement résorbé :

```bash
grep -rn '](\.\./\(\.\./\)\?TOC\.md' monographie/ | wc -l              # 48 au 22 juillet 2026
grep -rn 'doc/\(PRD\|PRDPlan\|TOC\|audit\)\.md' --include=*.md --include=*.py . | wc -l   # renvois vers l'ancien doc/
```

⚠ La seconde commande se compte elle-même : le tableau ci-dessus **cite** les formes cassées (`](../doc/PRD.md)`…), qu'elle attrape comme des renvois réels. La lire fichier par fichier — `| sed 's/:.*//' | sort | uniq -c` — et retrancher ce `CLAUDE.md`, jamais comme un total brut.

**Pipeline de rendu PDF** *(ajouté le 17 juillet 2026)* : `build/` contient un pipeline Pandoc → Typst **copié** de celui du volume I (`1 - Corpus Agentique/1 - InteroperabiliteAgentique/build/`), augmenté d'une étape d'assemblage propre à ce volume. Les deux copies évoluent séparément : un correctif là-bas ne se propage pas ici. `build/assemble.py` concatène les 29 pièces de `monographie/` en `Monographie.md` (retrait de l'appareil de rédaction interne — tableaux d'en-tête, bandeaux de correctif, blocs de gouvernance HTML ; préfixage des notes ; pages de garde de partie), puis `bash build/build-pdf.sh Monographie.md` produit `Monographie.pdf` (US-letter, Liberation Sans/Arial, gabarit `build/fesp.template`). **Régénérer après toute modification des chapitres** — sous réserve du renvoi `TOC.md` cassé signalé ci-dessus, qu'il faut corriger avant de pouvoir relancer l'assemblage. Le PDF et le `Monographie.md` assemblé sont versionnés ; les artefacts intermédiaires du build sont ignorés (`.gitignore`).

⚠ **Ni page de présentation, ni article de synthèse, ni publication GitHub Pages.** `index.html` et `Synthese Monographie.md` / `.pdf` (66 p.) ont été retirés du dossier (**suppression committée le 22 juillet 2026**, commit `fd8f1be`, arbre de travail propre). Ne pas rétablir de renvoi vers eux. Les adresses `https://agbruneau.github.io/Monographies/…` qui circulaient étaient fausses de surcroît — le dépôt s'appelle `Agentique`. Le seul rendu du volume est `Monographie.pdf` (**387 p.**, vérifié le 22 juillet 2026).

Documents de gouvernance, par ordre d'autorité :
1. [PRD.md](prd/PRD.md) — contenu, socle factuel, garde-fous, critères d'acceptation (prime en cas de conflit) ;
2. [PRDPlan.md](prd/PRDPlan.md) — plan d'exécution (phases P0–P4, boucle qualité par chapitre §4.2) ;
3. [TOC.md](prd/TOC.md) — titre, abstract et table des matières commentée (livrable J-2) : découpage en 24 chapitres tracés au socle ; toute modification du découpage passe par ce fichier (version++).

Arborescence de rédaction : `monographie/` (**les 29 pièces rédigées et relues** — un fichier par chapitre, en-tête à cinq champs renseigné sur les 29 : statut, date de gel, socle F-xx, garde-fous R-x, volumétrie cible ; annexes A–D dans `90-annexes/` ; registre des gels dans `99-registre-gel.md`) et `verification/` (rapports de revalidation, grille CA). Ne pas rédiger un chapitre sans passer par la boucle qualité de PRDPlan §4.2, et renseigner le registre de gel à chaque fusion.

## PRD.md fait autorité

Toute contribution (rédaction de la monographie, mise à jour du PRD, nouvelle recherche) doit se conformer au PRD :

- **Socle factuel (§7, 46 entrées — identifiants F-01 à F-48, F-12 à F-14 non attribués, plus F-23b)** : toute affirmation factuelle centrale doit être tracée vers une entrée F-xx ou vers une nouvelle source primaire de qualité équivalente, avec son niveau de preuve — **[A] > [B] > [C]** : [A] vote adversarial 3-0 (le plus haut), [B] source primaire lue/extraite avec citation mais sans vote, [C] repérage à confirmer. Une entrée [C] ne porte jamais un fait central sans élévation préalable. ⚠ **Une extraction de source primaire n'élève pas une entrée déjà votée 3-0 : elle l'enrichit d'un contenu de rang inférieur** (faute commise sur F-09 le 16 juill. 2026, rectifiée au PRD v1.7 — l'entrée porte le marquage [A/B mixte]). ⚠ **Ne jamais dériver le cardinal du socle d'une borne d'identifiants** : le total (46) et le plus haut identifiant ont coïncidé jusqu'en P0, et la coïncidence rendait l'erreur indétectable. Commande de référence : PRD §7 chapeau.
- **Garde-fous (§8.1, R-1 à R-8)** : affirmations réfutées ou non vérifiées, interdites dans tout texte (ex. : ACP comme standard vivant, FDX comme standard retenu du cadre bancaire canadien, conformité E-23/B-13 revendiquée par IBM, confusion des **quatre** emplois de « (agentic) control plane » / « ACP » recensés au socle — le sigle « ACP » employé seul est proscrit dans tout l'ouvrage).
- **Attribution (§8.2)** : toutes les métriques auto-déclarées (institutions, éditeurs, Linux Foundation, études d'analystes commandées) sont attribuées à leur source à chaque occurrence.
- **Correspondances réglementaires** : tout lien produit↔réglementation (E-23, AMF, art. 12.1, B-13) est marqué « documenté » ou « inférence d'auteur » (tableau B.3). Ne jamais présenter une inférence comme un fait.
- **Neutralité fournisseur (§8.4)** : IBM est un cas d'instanciation documenté (Partie VII, Annexe B), pas une recommandation.

## Sensibilité temporelle

Le domaine évolue par trimestres ; les faits sensibles au temps s'échelonnent pour l'essentiel de déc. 2023 à juill. 2026 (contexte historique antérieur inclus). Avant toute réutilisation ou publication : revalider les faits « chauds » listés en §8.3 du PRD (A2A/MCP, RTR, règlements du cadre bancaire, C-36). La clôture de l'acquisition Confluent, fait chaud jusqu'en P0, est résolue (17 mars 2026 — F-41). Chaque chapitre rédigé porte une date de gel de l'information.

## Conventions

- **Langue** : livrables et prose en français soutenu ; terminologie technique anglaise entre parenthèses à la première occurrence ; citations verbatim en langue originale.
- **Commits** : messages en anglais, format Conventional Commits (`docs(prd): ...` pour le PRD ; `docs(mono): draft chapter N — <slug anglais court>` pour les chapitres), sujet ≤ 50 caractères quand possible (plafond 72), mode impératif.
- **Versionnage du PRD** : incrémenter la version et la table des jalons (§12) à chaque enrichissement substantiel ; consigner la méthode de toute nouvelle recherche en Annexe A.
- **Chirurgie** : ne modifier que les sections concernées du PRD ; ne pas renuméroter les entrées F-xx ni les garde-fous R-x existants (ils sont cités en références croisées).

## Conventions additionnelles

- **Commits et push** : règle permanente du projet — committer tous les changements et pousser sur `main` à la fin de chaque tâche, sans attendre de demande.

## État du projet (17 juillet 2026)

**Monographie publiée, sous le millésime `mono-v1.0`.** ⚠ **L'étiquette git correspondante n'a jamais été posée** — `git tag -l` et `git ls-remote --tags origin` ne rendent rien, ni en local ni sur le distant (constaté le 18 juillet 2026). `mono-v1.0` est donc un **millésime éditorial**, pas une référence git : ne pas le traiter comme un point de restauration. Les documents qui annoncent l'étiquette comme posée (`prd/PRD.md`, `prd/PRDPlan.md`, `prd/audit.md`, les bandeaux de gel) sont, sur ce point, en avance sur le dépôt — poser le tag ou corriger ces mentions. Tous les jalons sont atteints (J-0 à J-5, PRD §12) et toutes les phases exécutées (P0 à P4, PRDPlan §1.4 — 47 activités closes, aucune en attente). Documents à jour : **PRD v1.10, PRDPlan v1.4, TOC v1.5** (versions relevées le 17 juill. 2026 par les suites de l'audit global — [`audit.md`](prd/audit.md)).

Livrable : **29 pièces, 92 059 mots** (90 362 à la publication ; re-mesuré après la passe corrective de l'audit) — 24 chapitres, avant-propos, annexes A à D. Index de lecture : [`monographie/README.md`](monographie/README.md). Socle : **46 entrées** (F-01 à F-48 ; F-12 à F-14 non attribués ; F-23b). Conformité : **CA-1 à CA-8** — le « 8/8 » de la relecture de publication a été **partiellement démenti** par l'audit du 17 juill. 2026 (CA-1 et CA-7 portaient des écarts, depuis corrigés) ; voir l'addendum de [`verification/relecture-CA.md`](verification/relecture-CA.md). Revalidation temporelle du 17 juillet 2026 : aucun amendement matériel des faits chauds. **Audit global du 17 juillet 2026 : deux élévations du socle (F-33, F-43), 15 constats majeurs et 44 mineurs traités, relus adversarialement.**

**Ce qui reste vivant après publication** — l'ouvrage se périme par morceaux, et ces points sont datés :

| Échéance | Objet | Pièces touchées |
|---|---|---|
| **28 juill. 2026** | Révision de la spécification MCP (protocole sans état, retrait de `Mcp-Session-Id`) — **confirmée à sa source** le 17 juill. | ch. 1, 2, 7 |
| après le 26 août 2026 | Texte final du règlement du cadre bancaire ; arrêté désignant l'organisme de normalisation technique (lève ou maintient **R-5**) | ch. 14, 15, 24 |
| cible T4 2026 | Lancement effectif du RTR (lève ou maintient la **réserve F-29**) | ch. 15, 24 |
| 1er mai 2027 | Entrées en vigueur d'E-23 et de la ligne directrice IA de l'AMF — le « futur proche » de l'ouvrage devient du présent | ch. 9, 11, 20 |
| continue | Trajectoire de C-36 | ch. 10 |

**Onze lacunes ouvertes** (PRD §10), toutes exposées et aucune comblée. La plus coûteuse : le contenu de la ligne directrice IA de l'AMF n'est pas au socle (§10.4 ; `lautorite.qc.ca` renvoie 403 aux outils) — le chapitre pivot n'en dérive aucune contrainte, sur l'un des deux textes qui fixent l'échéance du 1er mai 2027. **Ne jamais combler une lacune §10 avec du non-vérifié.**

**Toute reprise** (mise à jour, republication, dérivation) repasse par : revalidation des faits chauds (PRD §8.3) → amendement du **socle d'abord**, jamais des chapitres seuls (PRDPlan §7) → boucle qualité §4.2, **dont la relecture adversariale par un relecteur distinct** → date de gel au registre → version++ des documents touchés.
