# Journal de validation des spécifications — Tome 7 (v1.0 → v1.1, 22 novembre 2026)

Revue intégrale de `prd.md`, `toc.md`, `charte-editoriale.md`, `contrat-aq.md`, `plan-production-aq.md`, `manifest.json`, `protocole-mlr-2027.json` et des trois registres. **Régime : production.** Les totaux de mots, plages ± 8 %, figures et concepts possédés étaient déjà cohérents en v1.0; les constats ci-dessous portent sur la rigueur probatoire, la cohérence entre documents et la faisabilité technique.

## 1. Constats bloquants corrigés

| # | Constat | Document(s) | Correction |
|---|---|---|---|
| B1 | **Preuve circulaire possible** : les registres et plusieurs faits citaient les volumes 1 à 6 du dépôt, eux-mêmes produits par agents sans relecture humaine intégrale | `prd.md`, registres | `AO-02` étendu (volumes = carte de repérage, jamais preuve); champ `statut_preuve` (`a_reancrer`) sur chaque entrée de registre; réancrage exigé en Tâche 2; `G2` remonte à la source primaire |
| B2 | **Formules non rendues** : la charte prescrivait `\(...\)` avec `-f markdown-tex_math_dollars`, or `tex_math_single_backslash` est désactivé par défaut (vérifié sur `pandoc 3.14`) | `charte-editoriale.md`, `contrat-aq.md`, `plan-production-aq.md` | Commande unique `-f markdown-tex_math_dollars+tex_math_single_backslash`; formules uniquement en `\(...\)`; titres du `toc.md` recopiés dans le manuscrit purgés de `$` |
| B3 | **Recollation à froid invalidée par les réécritures** : la passe 2 de `G3` précédait `G4` et le lissage `G5`, qui modifient le texte | `contrat-aq.md`, `plan-production-aq.md`, `prd.md` (`CA-14`) | Ordre imposé : `G1` → `G2` → `G3` passe 1 → `G4` → `G5` lissage → `G3` passe 2 sur le texte final → `G5` rendu |
| B4 | **Aveugle de `G4` compromis** : l'essai DeepMind, en anglais, figurait dans la barre de comparaison; le critique l'aurait identifié | `charte-editoriale.md`, `contrat-aq.md`, `manifest.json` | Barre limitée à des extraits français exempts de codes (Ouverture `0.1`–`0.2`, chapitre 48 `48.4` et `48.8`); essai DeepMind conservé comme inspiration |
| B5 | **Fictions présentables comme faits** : plusieurs ouvertures (ch. 06, 09, 11) décrivent des incidents ou chiffres non documentés | `prd.md`, `toc.md`, `charte-editoriale.md` | Nouvel anti-objectif `AO-07` (scénarios illustratifs balisés, sans chiffre présenté comme mesuré) |
| B6 | **Collision de propriété** : `Fig-01` et la section 1.1 traitaient du « déplacement du point d'intégration humain », concept possédé par le liminaire; les sept pièges du ch. 11 incluaient la collision `PKI`/post-quantique possédée par le ch. 12 | `toc.md`, `manifest.json` | `Fig-01` et 1.1 recentrés sur l'échelle `L0`–`L4`; ch. 11 nomme seulement les modes détenus par les ch. 09 et 12 |
| B7 | **Dépendance avant définition** : le liminaire (`0.4`) mobilisait l'échelle `L0`–`L4`, définie au chapitre 01 | `toc.md`, `charte-editoriale.md` | Règle du maillon le plus élevé énoncée en termes de criticité, avec renvoi prospectif au ch. 01 |

## 2. Constats d'exactitude et de prudence épistémique corrigés

| # | Constat | Correction |
|---|---|---|
| E1 | Titre du ch. 08 (« un modèle plus fort devient plus vulnérable ») généralisait un résultat de prépublication sur un banc unique | « pourquoi un modèle plus capable n'est pas plus sûr »; limite du résultat exigée dans l'ouverture |
| E2 | Section 6.1 : « controverse tranchée » alors que la littérature reste dominée par les prépublications et montre des gains sur les tâches parallélisables | « controverse réexaminée à budget de calcul égal », gains parallélisables mentionnés |
| E3 | Ouverture du ch. 12 : signatures « soixante fois plus volumineuses dès 2030 » | Aligné sur le registre : environ 52 à 72 fois (`ML-DSA-65`/`-87` vs 64 octets), fenêtre financière 2030–2032 |
| E4 | Ouverture du ch. 02 : gain des agents « statistiquement introuvable » | « absence, à la date de gel, de toute étude indépendante mesurant l'effet »; section 2.2 reformulée de même |
| E5 | Ch. 10 : « régulateurs de Montréal »; « tous sanctionnent lourdement » | « autorités de Québec, d'Ottawa et de Bruxelles » (sièges de l'`AMF` et de la `CAI` à Québec); exigences distinguées des sanctions pécuniaires |
| E6 | Date `AMF` du 1er mai 2027 présentée comme acquise alors que le texte officiel est en `statut F` | Section 7 du `prd.md` (points de vigilance) et mention dans 10.2 et dans le registre |
| E7 | Ch. 09 : « journal d'audit immuable ancré (`RFC 8785`) » — la RFC 8785 porte sur la canonisation `JSON`, non sur l'ancrage | « entrées canonisées selon `RFC 8785`, puis ancrées par empreinte horodatée » |
| E8 | Ch. 03 : « agents gratuits inclus » (non vérifiable) | « agents préintégrés » |
| E9 | Partition 80/20 énoncée comme une loi | Qualifiée d'heuristique d'ingénierie de la collection dans la thèse et la charte |
| E10 | Thèse dite falsifiable sans critère de réfutation | Trois critères de réfutation ajoutés au `prd.md` |

## 3. Constats de cohérence corrigés

| # | Constat | Correction |
|---|---|---|
| C1 | `prd.md` : « ~255 pages » dans la raison d'être contre 260–270 au § 6 | Harmonisé; raison d'être reliée à l'interopérabilité et à l'orchestration (liminaire) |
| C2 | Lectorat en 3 segments contre 4 parcours au liminaire | Lectorat en 4 segments alignés sur `0.4` |
| C3 | Outil nommé `verifie.py` dans le `prd.md` et la charte, `verifie_manuscrit.py` ailleurs | `verifie_manuscrit.py` partout |
| C4 | `CA-11` : « ≥ 5 études par axe » contre `min_included_studies` = 6 pour `RQ1`, `RQ2`, `RQ5` | `CA-11` renvoie au seuil propre à chaque axe |
| C5 | `CA-05` : ≤ 2 tableaux par unité contre « tableau synoptique unique » au liminaire | Liminaire : exactement 1 tableau; chapitres : au plus 2 |
| C6 | Charte : « sept éléments obligatoires » mais six énumérés | Septième élément ajouté (transition vers la Partie I, déjà implicite) |
| C7 | « En conclusion, nous avons vu que » banni par la charte mais absent des regex | Ajouté à `forbidden_prose_regexes`, avec `Classe [1-6]`, `Stade [0-4]`, `Palier [1-3]` (classifications internes non définies; « Classe 1 » apparaissait au ch. 11) |
| C8 | `G1` : « 12 vérifications mécaniques » pour 6 règles listées; `CA-07` et `CA-17` affectés à `G1` sans règle | Huit règles explicites, dont concordance des registres et régénération des annexes |
| C9 | Fenêtre `MLR` 2025–2027 excluant des études déjà mobilisées (Noy et Zhang, 2023) | Fenêtre 2023–2027, alignée sur la revue `W3.2` |
| C10 | Échantillon `G3` sans garantie de couverture du liminaire et de chaque chapitre | Au moins 2 énoncés par unité narrative; points de vigilance inclus d'office |
| C11 | Intitulé du liminaire différent entre l'en-tête de section du `toc.md` et le `manifest.json` | Harmonisé; le vérificateur contrôle désormais la concordance de tous les intitulés |
| C12 | Date de gel des faits et crédit d'auteur absents du `PRD` | Champs ajoutés, à trancher par l'auteur |

## 4. Arbitrages de l'auteur

### 4.1 Décisions du 22 novembre 2026 (v1.2)

| Arbitrage | Décision | Répercussions |
|---|---|---|
| Date de gel des faits | **Décembre 2026**, pour une **publication en janvier 2027** | `prd.md` § 1 (calendrier, conséquence rédactionnelle); charte § 1.4 (échéances de 2027 au futur); fenêtre `MLR` close au 31 décembre 2026; `toc.md` purgé des formulations « début 2027 » et « tournant du 1er mai 2027 »; plan d'exécution |
| Essai du DeepMind Institute | **Procéder comme recommandé** : copie locale dans `sources-locales/`, hors versionnement; preuve par `arXiv:2606.12683` | Fichier retiré de l'arborescence versionnée; `.gitignore` exclut `sources-locales/*` sauf le `README.md`; `SEED-01` mis à jour |
| Crédit d'auteur | **André-Guy Bruneau, M.Sc IT** | `prd.md` § 1; champ `author_credit` de `manifest.json`; mention de la rédaction par agents d'IA au colophon (`0.6`) |

**Rectificatif.** La version précédente de ce journal affirmait que l'essai n'était pas versionné. C'était inexact : il avait été ajouté au dépôt (commit `520c3f2`) avant la revue. Il est désormais retiré de l'arborescence, mais reste présent dans l'historique public du dépôt; l'en effacer exigerait une réécriture de l'historique et une poussée forcée, qui ne seront faites que sur demande expresse de l'auteur.

### 4.2 Décisions de remédiation du 22 novembre 2026 (v1.3)

Consignation de l'arbitrage global autorisant la remédiation intégrale (Phases 1 à 4) à la suite de l'audit consolidé des 154 constats :

| Arbitrage | Décision (v1.3) | Répercussions |
|---|---|---|
| Date de gel des faits | **2 décembre 2026** (`2026-12-02`) arrêtée par l'auteur, tout en préservant l'honnêteté des dates réelles de capture (`22 novembre 2026`) | `prd.md`, `charte-editoriale.md`, `protocole-mlr-2027.json`, `plan-production-aq.md`, `prompt-lancement.md`, `toc.md`, `registre/*.json` et `recherche/*.json` alignés sur `2026-12-02` |
| Application des 154 constats d'audit | **Exécution complète des 4 phases** (fondations, réécriture manuscrit/sources/ancrage/diagrammes, outillage AQ, recollation/assemblage) | Remédiation `AO-01` ouverte (`SRC-023`, `SRC-025`, `SRC-037`, `SRC-038`, `SRC-051`, `SRC-055`, `SRC-076`–`079`), alignement strict `Fig-07`/`Fig-08`, `Fig-09`, 13 `QD`, 54 sous-titres canoniques et registres vérifiés |

### 4.3 Arbitrages encore ouverts

Aucun. Les spécifications sont prêtes pour le lancement de la production.

## 5. Vérification

`python "7 - Livre/outils/verifie_specs.py"` et `pytest "7 - Livre/outils/test_verifie_specs.py"` (deux nouveaux tests : dérive d'intitulés et `$` non échappé dans le `toc.md`; entrée de registre sans statut de preuve).
