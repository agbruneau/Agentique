# Interopérabilité et Orchestration en Entreprise Agentique — Architecture de référence, patrons de solutions et trajectoire 2026-2035 — Mémoire sous forme de livre blanc à l’intention des architectes d’entreprise et des architectes de solutions

[Retour à l'index principal du dépôt](../README.md)

## Informations sur le document

- **Source PDF** : [5 - Memoire.pdf](../0%20-%20PDF-MD/5%20-%20Memoire.pdf) (format `6,14 × 9,21 po` sous `Typst` via [`gabarit-pdf/`](../gabarit-pdf/README.md) · `4 910 411` octets / `~4,91 Mo`)
- **Fichier Markdown complet** : [5 - Memoire.md](../0%20-%20PDF-MD/5%20-%20Memoire.md)
- **Pages** : 175 (dont 4 liminaires couverture/notice/TDM et p. PDF 5–175 = pagination imprimée p. 1–171)
- **Parties / Sections** : 5
- **Unités extraites** : 27 (22 unités de contenu — 4 liminaires, 12 chapitres, 6 annexes — et 5 sommaires de section)
- **Diagrammes (PlantUML / Mermaid)** : [Diagrammes/README.md](Diagrammes/README.md) (8 diagrammes — 8 PlantUML rendus en `.svg` dans `Diagrammes/rendus/`, 0 Mermaid)
- **Statistiques du texte complet** : 62 285 mots · 2 523 lignes

## Table des matières

> *Note sur la pagination* : Les plages ci-dessous indiquent les pages **PDF physiques** de l'édition unifiée `6,14 × 9,21 po` (`impr. = PDF - 4` à compter du Liminaire).

- [Couverture](00%20-%20Couverture.md) (p. 1)
- [Table des matières](00%20-%20Table%20des%20mati%C3%A8res.md) (p. 3–4)
- [Liminaire — À propos de ce mémoire](00%20-%20Liminaire%20-%20%C3%80%20propos%20de%20ce%20m%C3%A9moire.md) (p. 5–8)
- [Synthèse exécutive — Dix thèses, deux rôles et une trajectoire AE / AS](00%20-%20Synth%C3%A8se%20ex%C3%A9cutive%20-%20Dix%20th%C3%A8ses%2C%20deux%20r%C3%B4les%20et%20une%20trajectoire%20AE%20-%20AS.md) (p. 9–13)
- **[Partie I — Le problème architectural et l’ossature commune](01%20-%20Partie%20I%20-%20Le%20probl%C3%A8me%20architectural%20et%20l%E2%80%99ossature%20commune/README.md)** (p. 14)
  - [Chapitre 1 — Constat empirique, thèse centrale et économie de la preuve](01%20-%20Partie%20I%20-%20Le%20probl%C3%A8me%20architectural%20et%20l%E2%80%99ossature%20commune/Chapitre%2001%20-%20Constat%20empirique%2C%20th%C3%A8se%20centrale%20et%20%C3%A9conomie%20de%20la%20preuve.md) (p. 15–22)
  - [Chapitre 2 — Architecture de référence unifiée, noyau possédé et réconciliation des modèles (DIV-02)](01%20-%20Partie%20I%20-%20Le%20probl%C3%A8me%20architectural%20et%20l%E2%80%99ossature%20commune/Chapitre%2002%20-%20Architecture%20de%20r%C3%A9f%C3%A9rence%20unifi%C3%A9e%2C%20noyau%20poss%C3%A9d%C3%A9%20et%20r%C3%A9conciliation.md) (p. 23–32)
- **[Partie II — Concevoir le tissu conjonctif et l’exécution : le chantier de l’architecte de solutions](02%20-%20Partie%20II%20-%20Concevoir%20le%20tissu%20conjonctif%20et%20l%E2%80%99ex%C3%A9cution/README.md)** (p. 33)
  - [Chapitre 3 — Couche protocolaire (MCP, A2A, événements), passerelle à neuf contrôles et anti-verrouillage](02%20-%20Partie%20II%20-%20Concevoir%20le%20tissu%20conjonctif%20et%20l%E2%80%99ex%C3%A9cution/Chapitre%2003%20-%20Couche%20protocolaire%20%28MCP%2C%20A2A%2C%20%C3%A9v%C3%A9nements%29%2C%20passerelle%20%C3%A0%20neuf.md) (p. 34–44)
  - [Chapitre 4 — Sémantique métier, compilation du contexte, mémoire CoALA et encapsulation patrimoniale/OT](02%20-%20Partie%20II%20-%20Concevoir%20le%20tissu%20conjonctif%20et%20l%E2%80%99ex%C3%A9cution/Chapitre%2004%20-%20S%C3%A9mantique%20m%C3%A9tier%2C%20compilation%20du%20contexte%2C%20m%C3%A9moire%20CoALA.md) (p. 45–52)
  - [Chapitre 5 — Orchestration hybride (OO1–OO4, 8 patrons), exécution durable, sagas et sémantique d’effet](02%20-%20Partie%20II%20-%20Concevoir%20le%20tissu%20conjonctif%20et%20l%E2%80%99ex%C3%A9cution/Chapitre%2005%20-%20Orchestration%20hybride%20%28OO1-OO4%2C%208%20patrons%29%2C%20ex%C3%A9cution%20durable.md) (p. 53–62)
  - [Chapitre 6 — Autonomie graduée, classes de décision, supervision humaine et liaison cryptographique](02%20-%20Partie%20II%20-%20Concevoir%20le%20tissu%20conjonctif%20et%20l%E2%80%99ex%C3%A9cution/Chapitre%2006%20-%20Autonomie%20gradu%C3%A9e%2C%20classes%20de%20d%C3%A9cision%2C%20supervision%20humaine.md) (p. 63–73)
- **[Partie III — Bâtir la fabrique de confiance et l’exploitation : le socle partagé AE / AS](03%20-%20Partie%20III%20-%20B%C3%A2tir%20la%20fabrique%20de%20confiance/README.md)** (p. 74)
  - [Chapitre 7 — Fabrique de confiance : NHI, 2e saut, défense anti-injection et transition PKI / post-quantique](03%20-%20Partie%20III%20-%20B%C3%A2tir%20la%20fabrique%20de%20confiance/Chapitre%2007%20-%20Fabrique%20de%20confiance%20-%20NHI%2C%202e%20saut%2C%20d%C3%A9fense%20anti-injection.md) (p. 75–85)
  - [Chapitre 8 — Observabilité à double couloir PII, journal d’audit JCS, évaluation E1–E3 et FinOps CPO](03%20-%20Partie%20III%20-%20B%C3%A2tir%20la%20fabrique%20de%20confiance/Chapitre%2008%20-%20Observabilit%C3%A9%20%C3%A0%20double%20couloir%20PII%2C%20journal%20d%E2%80%99audit%20JCS%2C%20%C3%A9valuation.md) (p. 86–93)
  - [Chapitre 9 — Plan d’inférence, six substrats d’état, confidentialité matérielle, résilience et réseaux B2B](03%20-%20Partie%20III%20-%20B%C3%A2tir%20la%20fabrique%20de%20confiance/Chapitre%2009%20-%20Plan%20d%E2%80%99inf%C3%A9rence%2C%20six%20substrats%20d%E2%80%99%C3%A9tat%2C%20confidentialit%C3%A9%20mat%C3%A9rielle.md) (p. 94–100)
- **[Partie IV — Gouverner, conformer et cadencer la trajectoire : le chantier de l’architecte d’entreprise](04%20-%20Partie%20IV%20-%20Gouverner%2C%20conformer%20et%20cadencer%20la%20trajectoire/README.md)** (p. 101)
  - [Chapitre 10 — Conformité dès la conception (Canada, Québec, UE) et déclinaison des cinq profils financiers](04%20-%20Partie%20IV%20-%20Gouverner%2C%20conformer%20et%20cadencer%20la%20trajectoire/Chapitre%2010%20-%20Conformit%C3%A9%20d%C3%A8s%20la%20conception%20%28Canada%2C%20Qu%C3%A9bec%2C%20UE%29%20et%20d%C3%A9clinaison.md) (p. 102–109)
  - [Chapitre 11 — Modèle opérationnel à trois lignes, usine logicielle interne et approvisionnement réversible](04%20-%20Partie%20IV%20-%20Gouverner%2C%20conformer%20et%20cadencer%20la%20trajectoire/Chapitre%2011%20-%20Mod%C3%A8le%20op%C3%A9rationnel%20%C3%A0%20trois%20lignes%2C%20usine%20logicielle%20interne.md) (p. 110–115)
  - [Chapitre 12 — Homologation unifiée et trajectoire adaptative (90 jours → 18 mois → Paliers P1–P3) sous signaux](04%20-%20Partie%20IV%20-%20Gouverner%2C%20conformer%20et%20cadencer%20la%20trajectoire/Chapitre%2012%20-%20Homologation%20unifi%C3%A9e%20et%20trajectoire%20adaptative.md) (p. 116–124)
- **[Annexes — Instruments de travail de l’architecte](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/README.md)** (p. 125)
  - [Annexe A — Tables de concordance 2026-2035 et pont CAP/PEX vers EXIG-\*](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/Annexe%20A%20-%20Tables%20de%20concordance%202026-2035%20et%20pont%20CAP-PEX%20vers%20EXIG.md) (p. 126–135)
  - [Annexe B — Catalogue de poche des décisions d’architecture AE / AS](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/Annexe%20B%20-%20Catalogue%20de%20poche%20des%20d%C3%A9cisions%20d%E2%80%99architecture%20AE%20-%20AS.md) (p. 136–139)
  - [Annexe C — Grille unifiée d’homologation avant mise en production](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/Annexe%20C%20-%20Grille%20unifi%C3%A9e%20d%E2%80%99homologation%20avant%20mise%20en%20production.md) (p. 140–147)
  - [Annexe D — Guide d’orientation vers les 2 541 pages sources et bibliographie maîtresse](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/Annexe%20D%20-%20Guide%20d%E2%80%99orientation%20vers%20les%202%20541%20pages%20sources%20et%20bibliographie.md) (p. 148–150)
  - [Annexe E — Glossaire des sigles, acronymes et repères (`385` entrées)](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/Annexe%20E%20-%20Glossaire%20des%20sigles%2C%20acronymes%20et%20rep%C3%A8res%20%28385%20entr%C3%A9es%29.md) (p. 151–169)
  - [Annexe F — Bibliographie primaire sélective (`70` normes, lois et études)](05%20-%20Annexes%20-%20Instruments%20de%20travail%20de%20l%E2%80%99architecte/Annexe%20F%20-%20Bibliographie%20primaire%20s%C3%A9lective%20%2870%20normes%2C%20lois%20et%20%C3%A9tudes%29.md) (p. 170–175)
