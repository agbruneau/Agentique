# Lots P2-M1 à P2-M10 — compte rendu

Date : 14 novembre 2026. Les dix points majeurs laissés ouverts par l'audit, en neuf lots (M2 et M3 réunis : même fichier). Rédigés et appliqués par l'orchestrateur, sans agent.

## Résolutions

| Lot | Point | Fichier | Ce qui change |
|---|---|---|---|
| P2-M1 | `01-38` | ch. 05, volet | L'Extrait 5.1 montrait la poignée de main `initialize` (version `2025-11-25`). Il montre un appel `tools/call` de la révision `2026-07-28` : en-têtes `Mcp-Method` et `Mcp-Name`, champ `_meta` portant version, capacités et identité du client, champ `resultType` dans le résultat. Titre et phrases de présentation refaits. |
| P2-M2-M3 | `02-49`, `02-50` | ch. 10, exposé | L'apport d'AP2 (Google) et de Verifiable Intent (Mastercard) à la FIDO Alliance, le 28 avril 2026, entre dans les sections 10.2, 10.4 et 10.6, les points à retenir, le bandeau et les limites. Source [20] ajoutée. La sous-section « Mastercard Agent Pay » sépare ce qui est établi de ce qui ne l'est pas. |
| P2-M4 | `03-8` | ch. 12, volet | L'ADR-009 porte sur la version parue `0.1.1` d'Apache Ossie, épinglée, non sur la branche `0.3.0.dev0`. |
| P2-M5 | `04-10` | ch. 18, volet | La situation antérieure du fil rouge passe de 14 à 29 jours, chiffre dont part le résultat. |
| P2-M6 | `05-31` | ch. 27, volet | L'Extrait 27.1 (A2A 1.0 avec SAP Joule) est présenté comme une cible; d'ici là, le plan neutre traduit entre versions. |
| P2-M7 | `06-15` | ch. 30, volet | Propriétaire technique obligatoire et succession sous 72 heures sont donnés pour des exigences de l'architecture prescrite, non pour des propriétés d'Entra. |
| P2-M8 | `08-9` | ch. 43, volet | Le seuil pass^5 et l'exécution durable relèvent de la porte G2, partout : texte des vagues, Extrait 43.2, figure. |
| P2-M9 | `08-24` | ch. 44, volet | Le troisième goulet du fil rouge n'est plus un reliquat de clés statiques, que le chapitre 43 dit révoquées, mais l'absence de verrou réseau. |
| P2-M10 | `08-30` | ch. 45, volet | Le maillage B2B est une cible pour 2027, non un état de l'art vérifié; deux tournures corrigées. |

## Sources lues

| Source | Date de lecture | Étendue | Sert à |
|---|---|---|---|
| Spécification MCP `2026-07-28`, « Key Changes » | 14 novembre 2026 | Page entière, rendue par l'outil de lecture | P2-M1 |
| Spécification MCP `2026-07-28`, « Versioning and Compatibility » | 14 novembre 2026 | Page entière | P2-M1 |
| Spécification MCP `2026-07-28`, « Overview » (champ `_meta`) | 14 novembre 2026 | Page entière | P2-M1 |
| FIDO Alliance, communiqué du 28 avril 2026 | 14 novembre 2026 | Phrases demandées mot pour mot à l'outil de lecture; texte brut non recoupé (téléchargement refusé par le contrôle de permissions) | P2-M2-M3 |

## Choix à connaître

- **P2-M1.** La forme de la requête suit la spécification : `_meta` dans `params`, version et capacités obligatoires, identité du client recommandée. Le nom de l'outil (`bel_find_compatible_spare_stock`) vient du chapitre lui-même; ses deux arguments sont illustratifs, déduits des champs de la réponse. La page de la spécification sur `server/discover` n'a pas été lue : l'extrait ne montre pas cette méthode.
- **P2-M2-M3.** Le communiqué ne dit pas ce que devient la gouvernance d'AP2 et de Verifiable Intent, ni quand un livrable paraîtra : l'exposé le dit. Les autres passages qui rattachent AP2 à la FIDO Alliance (ouverture, annexe H, chapitres 11 et 49) sont maintenant conformes à l'exposé et n'ont pas été modifiés. Le chapitre 11 ne reprend pas le fait dans sa cartographie (section 11.1) : laissé tel quel.
- **P2-M4.** La version `0.1.1` est dite « initiale » par sa propre spécification. L'ADR ne l'impose pas moins en production : c'est une prescription du volet, que l'auteur peut vouloir adoucir.
- **P2-M5.** « En moyenne » devient « en médiane », terme du résultat.
- **P2-M8.** La porte G2 est retenue parce que quatre passages sur six la désignaient déjà (politique Cedar, ADR-003, liste de contrôle, vague 2) et que le niveau N3 se définit par l'exécution durable. La figure `fig-43-a-1.svg` est corrigée hors registre, les figures n'y étant pas inscrites : « NHI, idempotence & pass^5 » sous G2, « Agent Cards A2A & HOTL » sous G3.
- **P2-M9.** Le nouveau troisième goulet est de mon cru : il fallait un motif au verrou réseau du T2 2027 qui ne contredise pas le chapitre 43. À confirmer par l'auteur.

## Difficulté rencontrée

Un premier lot P2-M1 remplaçait d'un bloc le code et la prose qui l'entoure. Le contrôle des volets l'a refusé : le code d'un volet doit rester identique à son original, corrections du registre appliquées, ce qui exige des remplacements de code contenus dans le bloc de code. Le lot a été annulé par `git checkout`, puis refait en huit remplacements. Règle à retenir pour tout lot qui touche un extrait de volet.

## Vérification

```
582 corrections dans 56 fichiers
pages : 1092, mots (approx.) : 404746
PDF : 1092 pages, 420523 mots, 16.2 Mo
Tous les contrôles passent.
```

Aucune de ces corrections n'a été relue par un second lecteur.

## Questions pour l'auteur

1. P2-M9 : le motif retenu pour le troisième goulet du chapitre 44 convient-il?
2. P2-M4 : faut-il maintenir l'adoption d'Apache Ossie en production sur une version `0.1.1`?
