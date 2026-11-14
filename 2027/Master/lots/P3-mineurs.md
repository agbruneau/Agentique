# Lots P3-m1 à P3-m6 — compte rendu

Date : 14 novembre 2026. Les trente points mineurs laissés ouverts par l'audit. Rédigés et appliqués par l'orchestrateur, sans agent.

## Bilan

- 27 points corrigés par 28 remplacements, en six lots.
- 3 points clos sans correction : `06-17` (déjà clos à la priorité 0), `06-7` et `08-40` (vérifiés à la source, le texte était juste).
- Le point `08-7`, prévu au lot P3-m4, est traité au lot P3-m1 : sa correction porte sur l'ouverture.

## Résolutions

| Lot | Point | Fichier | Ce qui change |
|---|---|---|---|
| P3-m1 | `01-1` | ouverture | Le chiffre non sourcé de « plus de 300 organisations » est retiré; reste le décompte de la section 11.2, environ 260. |
| P3-m1 | `01-3` | ouverture | Parcours CISO : « chapitres 29 à 32 », pour inclure l'identité agentique. |
| P3-m1 | `08-7` | ouverture | Les 47 initiatives sont situées « dans les trois divisions et les fonctions centrales », comme au chapitre 43. |
| P3-m1 | `01-21` | ch. 01, volet | L'attribution de la stratification à Gartner est retirée. |
| P3-m1 | `01-32` | ch. 04, exposé | « 92,5 % servent des humains, arrondis à 93 % », d'après l'étude. |
| P3-m1 | `01-33` | ch. 04, exposé | Une phrase dit où la hausse des coûts est traitée et que la gouvernance est une cause ajoutée par l'ouvrage. |
| P3-m2 | `02-54` | ch. 10, volet | MCP-UI est dit le projet communautaire dont MCP Apps est la forme officielle. |
| P3-m2 | `03-22` | ch. 16, volet | Extrait 16.3 : un flux relie `Task_PostGateDMN` à la passerelle `Gw_RouteAuthorization`. |
| P3-m2 | `03-28` | ch. 16, volet | La conformité est validée « avant l'échéance », non plus « trois mois avant ». |
| P3-m2 | `04-9` | ch. 18, volet | La ligne de tableau compare la persistance du journal, non une latence qu'aucune source ne chiffre. |
| P3-m2 | `04-13` | ch. 18, volet | « Epoch » sort de la formule; la correspondance des trois jeux de noms est dite une fois. |
| P3-m2 | `04-32` | ch. 19, volet | Seuil de dérive porté de 0,05 % à 0,1 %, cohérent avec la convergence exigée (99,9 %) et le bilan (99,94 %). |
| P3-m3 | `06-22` | ch. 31, volet | Une phrase décrit la quarantaine de la mémoire (barrière B3). |
| P3-m3 | `06-30` | ch. 32, volet | Les microsecondes visent le moteur seul; les autres chiffres, l'appel complet au PDP. |
| P3-m3 | `07-2` | ch. 34, volet | Les six couches de la phrase sont celles du tableau. |
| P3-m3 | `07-19` | ch. 35, exposé | Le cadre de Singapour prend l'adresse des chapitres 1, 3, 22 et 39. |
| P3-m4 | `07-13` | ch. 38, volet | L'écart avec l'Extrait 34.1 (0,95 pour le même agent) est dit. |
| P3-m4 | `08-8` | ch. 43, volet | Amnistie « ramenée de 30 jours à trois semaines ». |
| P3-m4 | `08-33` | ch. 45, volet | Le rapprochement se fait « dans les tolérances du contrat », comme dans l'Extrait 45.3. |
| P3-m5 | `08-44` | ch. 46, volet | Extrait 46.1 : groupe d'API `agentgateway.aaif.io/v1alpha2`, celui du chapitre 44. |
| P3-m5 | `08-47` | ch. 46, volet | La liste de contrôle reprend les six couches de la section 46.9. |
| P3-m5 | `08-49` | ch. 46, volet | Le passage de trois à quatre couches entre le texte et le tableau est expliqué. |
| P3-m5 | `08-52` | ch. 46, volet | Extrait 46.6 : types d'action nommés comme les primitives du texte. |
| P3-m6 | `09-14` | ch. 47, volet | Extrait 47.2 : `tests/acceptance/**` ajouté aux chemins interdits au bâtisseur. |
| P3-m6 | `09-17` | ch. 47, volet | « Contrats du Nouveau-Brunswick qui couvrent un 29 février ». |
| P3-m6 | `09-13` | ch. 47, volet | Une isolation R1 par 30 minutes, comme la politique Cedar et l'ADR-030. |
| P3-m6 | `09-12` | ch. 47, volet | Les réveils passent de 19 à 7 par mois, ce que donnent 64 % d'incidents résolus. |

## Points clos sans correction

| Point | Constat de l'audit | Vérification |
|---|---|---|
| `06-7` | La page « Security Best Practices » de MCP est citée sous deux arborescences (ch. 30 d'un côté; ch. 24 et 31 de l'autre). | L'adresse du chapitre 30 a été chargée le 14 novembre 2026 : c'est bien la page « Security Best Practices », dans sa version `2026-07-28`. L'adresse des chapitres 24 et 31 n'a pas été rechargée. Les deux restent en place. |
| `08-40` | Le rôle `snapshot` de TUF serait à clé en ligne, non hors ligne. | Spécification TUF, section 6.1, chargée le 14 novembre 2026 : « All keys, except those for the timestamp and mirrors roles, should be stored securely offline ». Le tableau du chapitre 46 est conforme à la spécification. |

## Sources lues

| Source | Date | Étendue | Sert à |
|---|---|---|---|
| Measuring Agents in Production, arXiv 2512.04123, version 4 (HTML) | 14 novembre 2026 | Les 100 000 premiers caractères; phrases de la section 4.3 citées par l'outil de lecture | `01-32` |
| IMDA, Model AI Governance Framework for Agentic AI (PDF, 53 pages) | 14 novembre 2026 | Page de titre, extraite localement | `07-19` |
| MCP, Security Best Practices (arborescence `docs/2026-07-28`) | 14 novembre 2026 | Page entière | `06-7` |
| The Update Framework, spécification | 14 novembre 2026 | Phrases sur les clés des rôles, citées par l'outil de lecture | `08-40` |

## Choix à connaître

- **Chiffres du cas fictif modifiés.** `04-32` (seuil de 0,1 %), `09-12` (7 réveils), `09-13` (1 pod par 30 minutes), `03-28` (plus de « trois mois »). Dans chaque cas, c'est le chiffre isolé qui cède devant celui que le reste du volet porte. L'auteur peut préférer l'inverse.
- **`06-30`.** La distinction entre le moteur Cedar et l'appel complet au PDP est l'hypothèse de l'audit. Aucune source ne l'établit : le motif du registre le dit.
- **`06-22`.** La phrase sur la quarantaine de la mémoire est de mon cru; elle reste générale, faute de description de la barrière B3 ailleurs dans le volet.
- **`08-44`.** Seul le groupe d'API est aligné. Les noms de régions diffèrent encore entre les Extraits 46.1 et 44.1.
- **`02-54`.** Que MCP Apps soit la forme normalisée du projet MCP-UI est ce que disent les chapitres 5 et 7; je ne l'ai pas revérifié à la source.

## Vérification

```
610 corrections dans 56 fichiers
pages : 1092, mots (approx.) : 404894
PDF : 1092 pages, 420670 mots, 16.2 Mo
Tous les contrôles passent.
```

Les 41 points laissés à l'auteur sont clos. Aucune de ces corrections n'a été relue par un second lecteur.
