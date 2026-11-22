# Interopérabilité et Orchestration en Entreprise Agentique

Collection de référence destinée aux dirigeants, membres de comités de direction, responsables technologiques et responsables de la gestion des risques qui encadrent le passage d'assistants conversationnels isolés vers des agents autonomes capables d'agir dans les systèmes de l'entreprise.

Le dépôt réunit **sept ouvrages** totalisant **3 181 pages** (état de référence : **novembre 2026** pour les volumes 1 à 6; **gel des faits au 2 décembre 2026** et **parution janvier 2027** pour le volume 7), avec un ancrage approfondi dans les services financiers réglementés au Canada fédéral et au Québec sur l'horizon **2024–2035**. Chaque ouvrage est disponible en format intégral (PDF et Markdown complet dans [`0 - PDF-MD/`](0%20-%20PDF-MD/README.md), complétés par une édition HTML autonome pour le volume 7) ainsi qu'en édition Markdown structurée par chapitre accompagnée de **310 diagrammes** (246 PlantUML et 64 Mermaid) dans les répertoires [`1`](1%20-%20Compendium%202026/README.md) à [`7`](7%20-%20Livre/README.md).

> **Idée maîtresse** — La fiabilité et la valeur durable d'une entreprise agentique tiennent moins à la puissance d'un modèle d'intelligence artificielle qu'à la solidité de ses frontières, de ses contrôles déterministes, de sa gouvernance et de sa capacité de preuve. Les modèles sont des composants remplaçables à obsolescence rapide; le noyau de contrôle, les règles métier et l'architecture d'interopérabilité constituent l'actif stratégique que l'institution doit posséder en propre.

---

## Pourquoi agir maintenant : trois pressions convergentes

1. **Éviter de remplacer les silos applicatifs par des silos d'agents.** Chaque grand éditeur de progiciels intègre désormais ses propres agents à son écosystème fermé (relation client, finances, ressources humaines, opérations technologiques). Sans architecture ouverte et gouvernée, l'organisation fragmente ses processus, perd la maîtrise de son contexte d'affaires et multiplie les dépendances envers ses fournisseurs.
2. **Maîtriser le risque opérationnel et la dérive des coûts.** Plus de 40 % des initiatives agentiques risquent l'abandon d'ici la fin de 2027 faute de contrôles adéquats, de valeur démontrée et de maîtrise budgétaire. Enchaîner dix étapes autonomes fiables chacune à 94 % fait chuter la réussite globale sans erreur à près de 54 %, tout en propageant des erreurs plausibles sans alerte visible; une boucle mal bornée peut aussi engendrer des coûts imprévus importants en quelques heures.
3. **Répondre à des obligations fiduciaires et réglementaires fermes.** Du Québec à l'Europe en passant par la réglementation prudentielle fédérale canadienne, les échéances de 2026 à 2028 imposent un inventaire complet, une imputabilité humaine claire, une traçabilité vérifiable et le respect de plafonds légaux stricts, sous peine de sanctions financières et réputationnelles majeures.

---

## Organisation du dépôt

- [`0 - PDF-MD/`](0%20-%20PDF-MD/README.md) : versions intégrales des sept ouvrages aux formats PDF et Markdown complet (14 fichiers consolidés : `1` à `6` et `7 - Livre.{pdf,md}`).
- [`1 - Compendium 2026/`](1%20-%20Compendium%202026/README.md) à [`5 - Memoire/`](5%20-%20Memoire/README.md) : série financière intégrée en édition Markdown structurée par partie, chapitre et annexe, chacune dotée de son sous-répertoire `Diagrammes/`.
- [`6 - Livre Blanc/`](6%20-%20Livre%20Blanc/README.md) : volet généraliste autonome en édition Markdown structurée avec ses 59 diagrammes.
- [`7 - Livre/`](7%20-%20Livre/README.md) : ouvrage synthétique linéaire (*Gouverner l'industrialisation cognitive*, `v1.3`, janvier 2027) structuré en 16 unités (`manuscrit/`), accompagné de son [édition HTML autonome](7%20-%20Livre/livrables/7%20-%20Livre%202027.html), de ses [23 diagrammes](7%20-%20Livre/diagrammes/README.md), de ses 79 sources primaires ouvertes `L+` hachées `SHA-256`, de ses spécifications (`specs/`), de ses journaux d'assurance qualité (`aq/`, `ancrage/`) et de ses outils de vérification (`outils/`).

---

## Vue d'ensemble des ouvrages

| # | Ouvrage | Formats intégraux | Vocation pour la direction | Horizon | Pages | Diagrammes |
|---|---|---|---|---|---:|---:|
| 1 | [`1 - Compendium 2026`](1%20-%20Compendium%202026/README.md) | [PDF](0%20-%20PDF-MD/1%20-%20Compendium%202026.pdf) · [MD](0%20-%20PDF-MD/1%20-%20Compendium%202026.md) | Somme encyclopédique sur l'interopérabilité, la confiance et l'encadrement en services financiers réglementés | 2024–2032 | 673 | [118](1%20-%20Compendium%202026/Diagrammes/README.md) |
| 2 | [`2 - Cadre de Référence`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence/README.md) | [PDF](0%20-%20PDF-MD/2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) · [MD](0%20-%20PDF-MD/2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.md) | Politique normative d'entreprise réunissant 12 principes directeurs, 10 décisions et 305 exigences vérifiables | 2026–2030 | 351 | [28](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence/Diagrammes/README.md) |
| 3 | [`3 - Compendium 2027`](3%20-%20Compendium%202027/README.md) | [PDF](0%20-%20PDF-MD/3%20-%20Compendium%202027.pdf) · [MD](0%20-%20PDF-MD/3%20-%20Compendium%202027.md) | État de l'art consolidé, guides de mise en œuvre concrets, revue scientifique et étude de marché | 2026–2030 | 1 117 | [68](3%20-%20Compendium%202027/Diagrammes/README.md) |
| 4 | [`4 - Plan Directeur`](4%20-%20Plan%20Directeur/README.md) | [PDF](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.pdf) · [MD](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.md) | Prospective sous incertitude, architecture cible en 52 capacités et feuille de route par métier financier | 2028–2035 | 400 | [6](4%20-%20Plan%20Directeur/Diagrammes/README.md) |
| 5 | [`5 - Memoire`](5%20-%20Memoire/README.md) | [PDF](0%20-%20PDF-MD/5%20-%20Memoire.pdf) · [MD](0%20-%20PDF-MD/5%20-%20Memoire.md) | Synthèse exécutive et architecturale unifiant les 2 541 pages des ouvrages 1 à 4 | 2026–2035 | 125 | [8](5%20-%20Memoire/Diagrammes/README.md) |
| 6 | [`6 - Livre Blanc`](6%20-%20Livre%20Blanc/README.md) | [PDF](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.pdf) · [MD](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.md) | Ouvrage de référence généraliste sur l'architecture cible, les standards ouverts et la feuille de route sur 360 jours | 2026–2027 | 251 | [59](6%20-%20Livre%20Blanc/Diagrammes/README.md) |
| 7 | [`7 - Livre`](7%20-%20Livre/README.md) | [PDF](0%20-%20PDF-MD/7%20-%20Livre.pdf) · [MD](0%20-%20PDF-MD/7%20-%20Livre.md) · [HTML](7%20-%20Livre/livrables/7%20-%20Livre%202027.html) | Ouvrage synthétique linéaire de référence sur l'architecture de contrôle, la preuve et la souveraineté (*Gouverner l'industrialisation cognitive*) | 2026–2035 | 264 | [23](7%20-%20Livre/diagrammes/README.md) |

---

## Par où commencer selon votre priorité

La collection s'articule autour d'un **ouvrage synthétique linéaire de référence** pour dirigeants et architectes à l'horizon 2027–2035 ([`7 - Livre`](7%20-%20Livre/README.md), fichier intégral [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) ou [édition HTML autonome](7%20-%20Livre/livrables/7%20-%20Livre%202027.html)), d'un **volet généraliste autonome** ([`6 - Livre Blanc`](6%20-%20Livre%20Blanc/README.md), fichier intégral [`6 - Livre Blanc.pdf`](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.pdf), applicable à tout secteur d'activité) et d'une **série financière intégrée** dont [`5 - Memoire.pdf`](0%20-%20PDF-MD/5%20-%20Memoire.pdf) constitue la porte d'entrée synthétique vers les ouvrages [`1`](1%20-%20Compendium%202026/README.md) à [`4`](4%20-%20Plan%20Directeur/README.md).

| Objectif de direction | Premier document à consulter | Pour approfondir |
|---|---|---|
| **Lire l'ouvrage synthétique linéaire de référence (dirigeants et architectes, 2027–2035)** | [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) ([HTML](7%20-%20Livre/livrables/7%20-%20Livre%202027.html)) — [Liminaire](7%20-%20Livre/manuscrit/00%20-%20Liminaire.md) et Parties I à IV (264 pages) | [`5 - Memoire.pdf`](0%20-%20PDF-MD/5%20-%20Memoire.pdf) (synthèse des volumes 1 à 4) et [`4 - Plan Directeur.pdf`](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.pdf) |
| **Saisir l'essentiel en moins de trente minutes** | [`5 - Memoire.pdf`](0%20-%20PDF-MD/5%20-%20Memoire.pdf) — Synthèse exécutive (pages 6 à 8) | [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) ([Liminaire](7%20-%20Livre/manuscrit/00%20-%20Liminaire.md)) et [`6 - Livre Blanc.pdf`](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.pdf) — Résumés exécutifs (pages 5 à 8) |
| **Adopter une politique de gouvernance, de risque et d'achat** | [`2 - Cadre de Référence.pdf`](0%20-%20PDF-MD/2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) — Sommaire exécutif (pages 8 à 10) et Gouvernance (dès la page 189) | [`5 - Memoire.pdf`](0%20-%20PDF-MD/5%20-%20Memoire.pdf) — Gouverner et conformer (pages 73 à 91) et [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) (Partie IV) |
| **Planifier les investissements 2028–2035 sans parier sur un seul fournisseur** | [`4 - Plan Directeur.pdf`](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.pdf) — Sommaire pour décision (pages 9 à 13) et Feuille de route (pages 253 à 327) | [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) (Chapitres 03 et 12, trajectoire DAPP) et [`2 - Cadre de Référence.pdf`](0%20-%20PDF-MD/2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) — Maturité et feuille de route (pages 243 à 257) |
| **Cadrer une transformation technologique hors secteur financier** | [`6 - Livre Blanc.pdf`](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.pdf) — Fondations (pages 9 à 49) et Transformation (pages 183 à 224) | [`3 - Compendium 2027.pdf`](0%20-%20PDF-MD/3%20-%20Compendium%202027.pdf) — Ouverture (pages 6 à 20) et Modèle opérationnel (pages 793 à 872) |
| **Vérifier les limites légales par métier (banque, patrimoine, assurance)** | [`4 - Plan Directeur.pdf`](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.pdf) — Profils sectoriels (pages 187 à 252) | [`1 - Compendium 2026.pdf`](0%20-%20PDF-MD/1%20-%20Compendium%202026.pdf) — Encadrement financier (pages 254 à 424) et [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) ([Chapitre 10](7%20-%20Livre/manuscrit/04%20-%20Partie%20IV/Chapitre%2010%20-%20Le%20laboratoire%20reglemente.md)) |
| **Évaluer la maturité réelle du marché et de la recherche** | [`3 - Compendium 2027.pdf`](0%20-%20PDF-MD/3%20-%20Compendium%202027.pdf) — Recherche et projection de marché (pages 996 à 1067) | [`7 - Livre.pdf`](0%20-%20PDF-MD/7%20-%20Livre.pdf) ([Chapitre 02](7%20-%20Livre/manuscrit/01%20-%20Partie%20I/Chapitre%2002%20-%20L%20epreuve%20des%20mesures.md)) et [`4 - Plan Directeur.pdf`](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.pdf) — Prospective 2028–2035 (pages 41 à 113) |

---

## Présentation détaillée des sept ouvrages

### 1. [`1 - Compendium 2026`](1%20-%20Compendium%202026/README.md) — Somme encyclopédique en services financiers
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/1%20-%20Compendium%202026.pdf) · [Markdown complet](0%20-%20PDF-MD/1%20-%20Compendium%202026.md) · [61 unités structurées](1%20-%20Compendium%202026/README.md) · [118 diagrammes](1%20-%20Compendium%202026/Diagrammes/README.md) (63 PlantUML, 55 Mermaid).
- **Décisions éclairées** : saisir les conditions de confiance nécessaires avant de laisser un agent agir ou déléguer une tâche en milieu financier canadien et québécois.
- **Points clés** : cinquante chapitres répartis en cinq livres — coopérer par contrats explicites, bâtir la confiance (identité vérifiable, chaîne de mandat, défense contre l'usurpation et préparation post-quantique), encadrer selon le droit financier canadien et québécois, exploiter un parc d'agents à grande échelle et garantir la réversibilité des opérations.
- **Outils pour la direction** : démonstration qu'aucun standard technique d'échange ne satisfait à lui seul aux obligations prudentielles financières, études de cas canadiennes (2025–2026) et feuille de route vers l'échéance réglementaire du 1er mai 2027 (page 528).

### 2. [`2 - Cadre de Référence`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence/README.md) — Cadre normatif d'entreprise
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) · [Markdown complet](0%20-%20PDF-MD/2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.md) · [35 unités structurées](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence/README.md) · [28 diagrammes](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence/Diagrammes/README.md) (25 PlantUML, 3 Mermaid).
- **Décisions éclairées** : instaurer des règles communes opposables à toutes les équipes et à tous les fournisseurs afin de concilier innovation, sécurité, conformité et liberté contractuelle.
- **Points clés** : dix décisions structurantes, douze principes directeurs et 305 exigences vérifiables couvrant le passage obligatoire par des passerelles de contrôle, l'échelle unique d'autonomie plafonnée par le risque, l'approbation humaine signée sur les actes sensibles, la protection contre la manipulation par données externes, la traçabilité complète et les clauses d'approvisionnement réversible.
- **Outils pour la direction** : grille d'homologation obligatoire avant mise en production (page 259), fiche d'identité normalisée par agent, partage clair des responsabilités autour d'un responsable nommé pour chaque agent, modèle de maturité en 5 niveaux et plan d'action des 90 premiers jours (page 251).

### 3. [`3 - Compendium 2027`](3%20-%20Compendium%202027/README.md) — État de l'art consolidé et mise en œuvre
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/3%20-%20Compendium%202027.pdf) · [Markdown complet](0%20-%20PDF-MD/3%20-%20Compendium%202027.md) · [73 unités structurées](3%20-%20Compendium%202027/README.md) · [68 diagrammes](3%20-%20Compendium%202027/Diagrammes/README.md) (68 PlantUML).
- **Décisions éclairées** : distinguer la maturité réelle du terrain des effets d'annonce commerciaux, fédérer les plateformes des grands éditeurs sans s'y enfermer et calibrer la feuille de route technologique jusqu'en 2030.
- **Points clés** : cinquante chapitres en dix parties combinant exposés sourcés et 31 volets pratiques de mise en œuvre — standards ouverts d'outillage et de dialogue entre agents, gouvernance sémantique des données et de la mémoire, exécution durable et reprise sur incident, intégration des systèmes anciens, cybersécurité, cadre juridique canadien et international, gouvernance économique par résultat, modernisation logicielle interne, revue de littérature scientifique et projection de marché 2027–2030.
- **Outils pour la direction** : registre de 31 décisions d'architecture structurantes, arbres de choix décisionnels, grilles d'évaluation de fournisseurs et liste de contrôle avant mise en production en 75 points.

### 4. [`4 - Plan Directeur`](4%20-%20Plan%20Directeur/README.md) — Prospective et architecture cible 2028–2035
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.pdf) · [Markdown complet](0%20-%20PDF-MD/4%20-%20Plan%20Directeur.md) · [45 unités structurées](4%20-%20Plan%20Directeur/README.md) · [6 diagrammes](4%20-%20Plan%20Directeur/Diagrammes/README.md) (6 PlantUML).
- **Décisions éclairées** : répondre à quatre questions de gouvernance pluriannuelle — *quoi construire d'abord et quoi différer, quel degré d'autonomie viser par métier, quels investissements engager sans regret et sur quels signaux réviser la trajectoire*.
- **Points clés** : prospective appuyée sur 98 textes officiels primaires et trois scénarios contrastés sans probabilité (socle ouvert étendu, archipel de plateformes propriétaires, fragmentation en blocs juridictionnels); architecture cible neutre envers les éditeurs en 52 capacités (42 capacités « sans regret » à bâtir dans tous les scénarios et 10 capacités conditionnelles activées uniquement sur signal); déclinaison détaillée pour cinq profils financiers.
- **Outils pour la direction** : calendrier consolidé 2027–2035, trajectoire en trois paliers (2028–2029, 2030–2032, 2033–2035) franchis sur preuve, 15 portes de gouvernance, 27 signaux de veille et analyse des risques internes du plan (gouvernance de façade, lourdeur documentaire, érosion des compétences humaines).

### 5. [`5 - Memoire`](5%20-%20Memoire/README.md) — Synthèse unifiée de la collection
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/5%20-%20Memoire.pdf) · [Markdown complet](0%20-%20PDF-MD/5%20-%20Memoire.md) · [27 unités structurées](5%20-%20Memoire/README.md) · [8 diagrammes](5%20-%20Memoire/Diagrammes/README.md) (8 PlantUML).
- **Décisions éclairées** : aligner la haute direction, l'architecture d'entreprise, la sécurité, la conformité et les équipes de réalisation autour d'un référentiel commun de 125 pages condensant les quatre ouvrages financiers.
- **Points clés** : dix thèses structurantes issues des mesures réelles de fin 2026, six arbitrages conjoints entre gouvernance d'entreprise et conception technique, harmonisation complète des modèles de la collection et trajectoire continue des 90 premiers jours jusqu'en 2035.
- **Outils pour la direction** : catalogue de poche des décisions d'architecture, grille unifiée d'homologation avant mise en production, table d'orientation vers les chapitres précis des 2 541 pages sources et glossaire consolidé de 385 termes.

### 6. [`6 - Livre Blanc`](6%20-%20Livre%20Blanc/README.md) — Référence généraliste d'architecture et d'adoption
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.pdf) · [Markdown complet](0%20-%20PDF-MD/6%20-%20Livre%20Blanc.md) · [27 unités structurées](6%20-%20Livre%20Blanc/README.md) · [59 diagrammes](6%20-%20Livre%20Blanc/Diagrammes/README.md) (56 PlantUML, 3 Mermaid).
- **Décisions éclairées** : positionner les agents face aux systèmes transactionnels existants, arbitrer entre l'achat d'agents intégrés aux progiciels, l'assemblage sur standards ouverts (posture recommandée par défaut) ou le développement sur mesure, et rythmer la première année de transformation.
- **Points clés** : partition hybride maintenant environ 80 % des règles, identités et contrôles en logique déterministe pour 20 % confiés aux modèles; encapsulation sécurisée du patrimoine applicatif sans réécriture; sécurité par confiance zéro; pilotage financier au coût par résultat réussi; transition progressive depuis l'automatisation classique.
- **Outils pour la direction** : trois architectures types prêtes à adapter (environnement hautement réglementé, collaboration inter-entreprises, exploitation souveraine confidentielle), diagnostic de 12 pièges courants, échelle de maturité en 5 paliers, feuille de route sur 90, 180 et 360 jours et liste d'homologation en 40 critères.

### 7. [`7 - Livre`](7%20-%20Livre/README.md) — Gouverner l'industrialisation cognitive (`2026–2035`)
- **Formats et ressources** : [PDF intégral](0%20-%20PDF-MD/7%20-%20Livre.pdf) (264 pages) · [Markdown complet](0%20-%20PDF-MD/7%20-%20Livre.md) · [HTML autonome](7%20-%20Livre/livrables/7%20-%20Livre%202027.html) · [16 unités structurées](7%20-%20Livre/README.md) · [23 diagrammes](7%20-%20Livre/diagrammes/README.md) (20 PlantUML `.svg`, 3 Mermaid `.png`).
- **Décisions éclairées** : offrir aux dirigeants, architectes d'entreprise, ingénieurs de plateforme et responsables sécurité-conformité un livre d'auteur à lecture continue — sans nomenclature matricielle interne — pour posséder le noyau de contrôle déterministe face à l'industrialisation cognitive et décider sous incertitude profonde jusqu'en 2035.
- **Points clés** : `75 065` mots (`G1`, révision `v1.3`) en un liminaire et douze chapitres répartis en quatre parties (l'industrialisation cognitive face au réel, l'exosquelette déterministe `80/20`, la fabrique de confiance et l'économie de la preuve, gouverner jusqu'en 2035 sans atrophier l'humain) fondés sur **79 sources primaires ouvertes `L+`** hachées `SHA-256` (gel des faits au **2 décembre 2026**, parution **janvier 2027**) — spectre d'autonomie `L0`–`L4`, loi de Lusser et constance multi-essais (`passᵏ`), coûts de transaction de Coase et arbitrage Acheter / Assembler / Construire, protocoles ouverts (`MCP`, `A2A`, `CloudEvents`), exécution durable et sagas compensatoires, identités éphémères sans secret fixe et transition post-quantique (`ML-DSA`, certificats `TLS` courts), séparation contrôle-données et coût complet par résultat conforme, conformité `Loi 25` / `BSIF E-23` / `EU AI Act` et parade contre l'érosion des compétences juniors.
- **Outils pour la direction** : cinq critères permanents d'évaluation architecturale, règle du maillon le plus élevé (*High-Water Mark Rule*), quatre parcours de lecture par responsabilité, trajectoire adaptative sous seuils (`DAPP`) avec séquence sur 90, 180 et 360 jours, et trois annexes générées mécaniquement depuis les registres ([Annexe A](7%20-%20Livre/manuscrit/05%20-%20Annexes/Annexe%20A%20-%20Glossaire%20raisonne.md) : glossaire bilingue raisonné de 33 entrées; [Annexe B](7%20-%20Livre/manuscrit/05%20-%20Annexes/Annexe%20B%20-%20Chronologie%20consolidee%202026-2035.md) : chronologie réglementaire et cryptographique; [Annexe C](7%20-%20Livre/manuscrit/05%20-%20Annexes/Annexe%20C%20-%20Methodologie%20et%20bilan%20d%20assurance%20qualite.md) : méthodologie bibliométrique, bibliographie des 79 sources `L+` et bilan d'assurance qualité à 5 barrières `G1`–`G5`, triple recollation `G3` à `60/60` et `264` pages vérifiées).

---

## Repères stratégiques pour la haute direction

### Cinq principes directeurs transversaux
1. **La simplicité et le contrôle précèdent l'autonomie.** Privilégier par défaut un processus déterministe classique, puis un agent unique bien outillé, et n'autoriser la coordination de plusieurs agents que sur preuve chiffrée d'un gain réel.
2. **Posséder son noyau de contrôle pour préserver sa souveraineté.** Conserver en propre le registre des agents, la gestion des identités, les passerelles de sécurité, les règles d'autorisation et les journaux d'audit afin de pouvoir remplacer un modèle ou un fournisseur sans refonte majeure.
3. **Maintenir une imputabilité et une supervision humaines effectives.** Chaque agent en service relève d'une personne responsable nommée. Les décisions critiques ou irréversibles exigent une validation humaine éclairée liée à l'acte exact, assortie de mesures prévenant l'approbation machinale et le recul des compétences internes.
4. **Piloter par le coût complet du résultat conforme.** Évaluer chaque initiative selon le coût total d'une transaction métier menée à terme sans reprise (incluant supervision, sécurité, conformité et infrastructure), sans présumer qu'une baisse du coût unitaire des modèles réduit la facture globale.
5. **Bâtir sur la preuve plutôt que sur des paris technologiques.** Toutes les échéances réglementaires fermes d'ici 2035 portent sur la preuve, la gouvernance, la transparence et la cryptographie — jamais sur une obligation d'automatiser.

### Frontières légales structurantes par métier financier
- **Transversal (Québec)** : obligation d'informer la personne concernée et de lui garantir explication, observation et révision humaine effective pour toute décision fondée exclusivement sur un traitement automatisé (sanctions sous la Loi 25 pouvant atteindre 25 millions de dollars canadiens ou 4 % du chiffre d'affaires mondial).
- **Banque et coopératives financières** : interdiction des accès par capture d'écran dans le cadre bancaire ouvert, encadrement strict des virements irrévocables et maintien des cloisons réglementaires entre activités bancaires et d'assurance.
- **Gestion de patrimoine et valeurs mobilières** : caractère non délégable de la responsabilité des personnes inscrites et interdiction des recommandations ou systèmes automatisés d'ordres dans les comptes sans conseils.
- **Assurance de personnes** : interdiction criminelle de recueillir ou d'utiliser des résultats de tests génétiques et encadrement rigoureux du consentement sur les renseignements de santé.
- **Assurance de dommages** : approbation préalable des formulaires en assurance automobile, respect des obligations de comparaison hors groupe en courtage et interdiction des refus d'indemnisation automatisés sans examen humain.

---

## Les six priorités des 90 premiers jours

Avant tout déploiement à grande échelle ou toute délégation entre agents, les ouvrages convergent vers un socle minimal de maîtrise :
1. **Recenser l'existant** : dresser l'inventaire complet de tous les agents, assistants connectés et connecteurs d'outils déjà actifs ou en projet.
2. **Désigner les responsables** : rattacher chaque agent à une personne imputable nommée et instituer l'instance conjointe d'architecture et de gestion des risques.
3. **Éliminer les accès partagés** : supprimer les clés statiques et comptes génériques au profit d'identités distinctes à privilèges minimaux et de courte durée.
4. **Imposer un point de passage contrôlé** : acheminer les appels aux modèles et aux outils d'entreprise par une passerelle centrale assurant journalisation, filtrage et plafonds budgétaires.
5. **Qualifier les risques et la vie privée** : classer chaque cas d'usage selon son impact, réaliser les évaluations relatives à la vie privée requises et fixer son plafond d'autonomie.
6. **Tester l'arrêt d'urgence et verrouiller la mise en production** : éprouver un mécanisme de désactivation rapide et conditionner toute mise en service au passage d'une grille formelle d'homologation.

---

## Calendrier des échéances clés (2026–2035)

- **En vigueur** : encadrement québécois des décisions exclusivement automatisées et de la vie privée (Loi 25, art. 12.1 en vigueur depuis le 22 septembre 2023); attentes des Autorités canadiennes en valeurs mobilières sur les systèmes d'intelligence artificielle; obligations européennes de transparence entrées en application en août 2026.
- **15 mars 2027 (puis 15 mars 2029)** : abaissement de la durée maximale des certificats de sécurité web à 100 jours, puis à 47 jours, rendant indispensable l'automatisation complète de leur renouvellement.
- **1er mai 2027** : entrée en vigueur de la ligne directrice révisée sur la gestion du risque de modèle du Bureau du surintendant des institutions financières (couvrant expressément les modèles génératifs et les agents) et prise d'effet de la ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers au Québec.
- **2 décembre 2027 (puis 2 août 2028)** : entrée en application progressive des exigences européennes sur les systèmes d'intelligence artificielle à haut risque pour les organisations actives en Europe.
- **2028** : interdiction des rétrofacturations de commissions en gestion de patrimoine (1er octobre 2028) et nouvelles exigences prudentielles de divulgation climatique (émissions financées et assurées de portée 3).
- **2030 à 2035** : fenêtre coordonnée du secteur financier du Groupe des Sept pour migrer vers une cryptographie résistante aux ordinateurs quantiques, avec échéance de révision des lois financières fédérales canadiennes au **30 juin 2033**.

---

## Portée et transparence éditoriale

- **Outil consultatif d'aide à la décision** : cette collection éclaire la stratégie, la gouvernance et l'architecture d'entreprise. Elle ne constitue ni un avis juridique, ni une certification actuarielle ou d'audit, ni une homologation réglementaire.
- **Périmètre démontré** : l'appareil réglementaire et probatoire des ouvrages 1 à 5 et 7 porte sur les services financiers réglementés au Canada fédéral et au Québec (ainsi que leurs obligations transfrontalières européennes) et sur l'ingénierie de contrôle déterministe; le *Livre Blanc* (6) adopte un cadrage généraliste multisectoriel. Les exemples touchant d'autres secteurs (santé, industrie, énergie, secteur public) sont fournis à titre illustratif.
- **Crédit d'auteur et mode de production déclaré** :
  - Les volumes 1 à 6 (état de référence : **novembre 2026**) documentent de manière transparente le recours à des pipelines automatisés d'agents d'intelligence artificielle pour la rédaction, le recoupement sur sources primaires et le contrôle de cohérence, sans relecture humaine intégrale de bout en bout.
  - Le volume 7 (*Gouverner l'industrialisation cognitive*, révision `v1.3`, **gel des faits au 2 décembre 2026**, **parution janvier 2027**) est crédité à son auteur, concepteur et maître d'ouvrage **André-Guy Bruneau, M.Sc IT**, qui en a arrêté le cahier des charges, l'architecture thématique, les critères de réfutation et les seuils d'acceptation. Sa collecte ouverte sans contournement sur **79 sources primaires `L+` hachées `SHA-256`**, sa rédaction linéaire et son assurance qualité à **5 barrières indépendantes (`G1`–`G5`)** — garde déterministe, ancrage atomique Wyvern (`1 087` assertions supportées), triple recollation stratifiée à l'aveugle (`60/60` aux trois passes `G3` `202701`, `202702` et `202703` à `56/60 -> 60/60`), boucle critique comparative à l'aveugle (`G4`) et lissage transversal accompagné d'une inspection visuelle intégrale (`G5` / `v1.3` sur `264` pages) — sont réalisés **à 100 % par des agents d'IA**, sans rédaction humaine ni relecture humaine intégrale.
- **Conditions de diffusion** : les ouvrages 2 à 5 mentionnent une diffusion ouverte sous licence Creative Commons Attribution 4.0 pour les textes et figures (et licence libre pour les scripts et outils associés); le volume 7 (`7 - Livre`) est publié sous licence **`CC-BY-4.0`** pour les textes et figures et **`MIT`** pour le code et les scripts d'outillage; le *Compendium 2026* (1) et le *Livre Blanc* (6) ne comportent pas de mention de licence en page de titre.
