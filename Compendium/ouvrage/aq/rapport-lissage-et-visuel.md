# Rapport de lissage éditorial (`G5`) et d'inspection visuelle intégrale (`CA-16`)

- **Rôle exécutant :** `inspecteur-visuel` (`Task 9` — `T9-S3`)
- **Date de référence et de gel :** `2 décembre 2026` (`2026-12-02`)
- **Livrables inspectés :**
  - `Compendium/ouvrage/livrables/Compendium.pdf` (`19 158 415` octets, `711` pages)
  - `Compendium/ouvrage/livrables/Compendium.html` (`10 094 315` octets)
  - `Compendium/ouvrage/livrables/Compendium.md` (`1 522 869` octets)
- **Statut de clôture visuelle :** **CONFORME — 0 défaut bloquant**

---

## 1. Inspection intégrale du livrable PDF (`100,0 %` des `711` pages)

Toutes les `711` pages de `Compendium.pdf` ont été rendues en PNG (`130 DPI`) via `pymupdf` (`fitz`) et balayées algorithmiquement (`fitz` + `PIL`) dans `scratch/pdf_pages/`, puis complétées par une inspection visuelle directe de planches-contacts et de captures pleine page.

### 1.1 Métriques automatisées sur `711 / 711` pages (`100,0 %`)

| Contrôle automatisé | Périmètre | Résultat observé | Statut |
|---|---:|---|---|
| Décompte exact des pages | `711` pages | `711` pages (couverture `p.1` à dernière page `p.711`) | Conforme |
| Dimensions physiques | `711 / 711` pages | `6,14 × 9,21 po` (`442,08 × 663,12 pt`) uniformes | Conforme |
| Débordement hors page (`bbox`) | `711 / 711` pages | `0` boîte texte, image ou dessin hors limites de page | Conforme |
| Débordement marqué hors marges (`> 10 pt`) | `710` pages corps | `0` image/dessin ; `1` formule centrée large (`CPO = ...`, `p.388`, `x0=44,8 pt`, sans rognage) | Conforme (mineur) |
| Pages blanches anormales | `711 / 711` pages | `0` page blanche ni page à faible encre anormale | Conforme |
| Formules LaTeX/Typst brutes (`\\(`, `\\)`, `$$`) | `711 / 711` pages | `0` occurrence résiduelle (mathématiques `p.99` et `p.113` rendues) | Conforme |
| Glyphes manquants (`\ufffd`) | `711 / 711` pages | `0` occurrence | Conforme |
| Images raster blanches ou corrompues | `23` xrefs uniques | `0` image blanche ou corrompue | Conforme |
| Présence graphique des `115` figures | `115 / 115` schémas | `115 / 115` présents avec légende et vecteur/image (`0` figure vide) | Conforme |

### 1.2 Inspection visuelle directe (`read_file` sur planches-contacts et PNG pleine résolution)

Les captures rendues ont été inspectées visuellement sur les zones critiques suivantes :

1. **Couverture et pages liminaires (`p.1`–`p.6`)** : couverture marine `Compendium de l'entreprise agentique` nette, badge `CC BY 4.0` et métadonnées de gel alignés ; table des matières (`p.3`–`p.6`) alignée avec points de conduite et pagination exacte jusqu'aux Annexes `A`–`E`.
2. **Débuts de parties et de chapitres (`sheet_02`)** : hiérarchie typographique homogène, encadrés de chapitre nets et en-têtes courants tronqués proprement sans collision.
3. **Rendu mathématique (`p.99`, `p.113`, `p.388`)** : formules `S_ready` et fonction indicatrice `I(c_sec >= 60)` correctement composées en Typst sans artifice `\\(` ni `\\)` ; équation centrée `CPO` (`p.388`) entièrement lisible.
4. **Trois moteurs de figures (`115` schémas)** :
   - **Infographies SVG natives (`40`)** : `SCH-00-01` (`p.13`), `SCH-01-02` (`p.30`), `SCH-03-02` (`p.62`) — rendu vectoriel net, contrastes élevés, zéro texte coupé.
   - **PlantUML `.svg` (`52`)** : `SCH-00-02` (`p.15`), `SCH-02-02` (`p.44`) — tracés, zones et légendes nets et lisibles.
   - **Mermaid `.png` (`23`)** : `SCH-00-04` (`p.20`), `SCH-03-01` (`p.58`), `SCH-05-02` (`p.91`) — rendu propre à `300 DPI`, aucune troncature ni pixellisation bloquante.
5. **Blocs `CA-G0-SYNC` et extraits de code (`p.73`, `p.282`, `p.559`, `p.568`)** : coloration syntaxique, indentation et retours à la ligne contenus à l'intérieur des encadrés de code sans débordement horizontal.
6. **Tableaux larges (`p.26`, `p.62`, `p.88`, `p.593`, `p.614`)** : en-têtes bleu marine, alternance de lignes et césures cellulaires maîtrisées (ex. `Tableau 5.1`, `p.88`).
7. **Annexes `A`–`E` et fin d'ouvrage (`p.593`, `p.614`, `p.639`, `p.663`, `p.687`, `p.711`)** : démarrage propre de chaque annexe déterministe (`Annexe A` `p.593`, `Annexe B` `p.614`, `Annexe C` `p.639`, `Annexe D` `p.663`, `Annexe E` `p.687`) et clôture nette en `p.711`. *(Observation éditoriale mineure non bloquante : l'Annexe B enchaîne `## 1.` vers `## 3.` selon le gabarit de `genere_annexes.py`, sans perte de données.)*

---

## 2. Inspection du livrable HTML autonome (`Compendium.html`)

L'analyse DOM (`HTMLParser`) et par expression régulière sur `Compendium/ouvrage/livrables/Compendium.html` (`10 094 315` octets) confirme :

- **`115 / 115` figures embarquées en `data:image/...;base64`** : `92` SVG (`image/svg+xml`, couvrant les `52` PlantUML et les `40` infographies natives) et `23` PNG (`image/png`, couvrant les `23` diagrammes Mermaid) ; `115 / 115` charges base64 décodées valides et non vides.
- **`0` dépendance réseau externe** : aucune URI `http://`, `https://` ou `//` dans les balises `<img>`, `<script>` ou `<link>` (CSS et MathML intégrés hors ligne).

---

## 3. Synthèse du lissage éditorial `G5` (`Task 8`) et de la compilation finale (`Task 9`)

- **Lissage éditorial (`T8-S1`) :** harmonisation des transitions entre parties (`I`–`XII`) et passerelles `→`/`←`, suppression des sections dupliquées et des redites inter-chapitres (`DIV-02` `ch06`/`ch36`, Partie IV), et traitement complet des `11` micro-raccords relevés au Tour 2 du `gauntlet-log.md` § 3 (`ch16`, `ch26`, `ch27`, `ch28`, `ch29`, `ch30`, `ch32`, `ch33`, `ch34`, `ch35`, `ch36`).
- **Audit différentiel post-lissage (`T8-S2`) :** comparaison intégrale contre `snapshot_post_g4` (`24` unités narratives retouchées sur `42` : `00-liminaire` et `23` chapitres), mise à jour de `15` journaux `ancrage/chXX-ancrage.md` maintenus à `100,0 %` supportés et préservation intégrale des `14` extraits `CA-G0-SYNC`.
- **Recollation à froid double passe `G3` (`T8-S3`) :** deux passes indépendantes strictement disjointes (`0` chevauchement sur `claim_loc` et `paragraph_loc`) — `seed=20270901` (`142/148` initial → `148/148` après `6` rectifications) et `seed=20270902` (`141/148` initial → `148/148` après `7` rectifications), soit **`296 / 296` énoncés validés (`100,0 %`)**.
- **Régénération et assemblage final (`T9-S1`, `T9-S2`) :** `5` Annexes `A`–`E` régénérées de manière déterministe (`2 802`, `2 438`, `2 848`, `2 958`, `3 424` mots) portant le manuscrit à **`42 / 42` unités conformes (`188 650` mots)** ; correctif `_unwrap_backticked_latex_math` dans `assemble_livre.py` éliminant les délimiteurs LaTeX résiduels en compilation HTML/PDF.

---

## 4. Verdict de clôture

Le Compendium satisfait sans réserve les critères visuels et d'autonomie documentaire (`CA-16`, `CA-17`, `CA-18`) : **aucun défaut bloquant** détecté sur les `711` pages PDF, les `115` figures multi-moteurs ou le HTML autonome.
