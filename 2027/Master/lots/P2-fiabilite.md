# Lots de fiabilité P2-F1, P2-F2 et P2-F3 — compte rendu

Date : 14 novembre 2026. Les constats viennent d'agents qui lisaient sans rien modifier; l'orchestrateur a arbitré chaque constat et appliqué les corrections par lots. Deux interruptions par limite d'usage : les agents ont repris là où ils s'étaient arrêtés.

## Résultats

| Lot | Périmètre | Constats | Corrections au registre |
|---|---|---|---|
| P2-F1, second audit | Les 193 compléments du 14 novembre, relus par deux lecteurs qui ne les avaient pas écrits (Fable) | 95 : aucun bloquant, 19 majeurs, 76 mineurs | 86 constats corrigés, 9 laissés |
| P2-F2, recollationnement | 200 phrases d'exposé tirées au hasard parmi 295 (graine `20261114`), cinq tranches (Sonnet) | 178 confirmées, 4 erreurs, 6 introuvables, 12 inaccessibles | 4 erreurs et 4 précisions corrigées |
| P2-F3, lecture au-delà du résumé | 134 sources des chapitres 1 à 47 connues par leur seul résumé et citées, trois tranches (Sonnet) | 64 confirmées, 54 à nuancer, 6 erreurs, 6 dont seul le résumé s'est chargé, 4 inaccessibles | 57 phrases corrigées ou nuancées; une puce de limite dans 35 chapitres |

Taux d'erreur de relevé : 4 sur 182 phrases vérifiables, soit 2,2 %. Le lot F3 est le plus parlant : près d'une source sur deux, relue en entier, porte une réserve que son résumé taisait.

Ces résultats sont publiés dans l'annexe E, section E.3, sous « Contrôles faits le 14 novembre 2026 ».

## Fichiers

| Fichier | Contenu |
|---|---|
| `P2-F1-entrees-a.md`, `-b.md` | Cahiers des 193 entrées à relire |
| `P2-F1-constats-a.json`, `-b.json`, `-b2.json` | Constats du second audit |
| `P2-F1-b.json`, `P2-F1-a1.json`, `P2-F1-a2.json`, `P2-F1-b2a.json`, `P2-F1-b2b.json` | Lots de corrections du second audit |
| `P2-F2-echantillon-1.json` à `-5.json`, `P2-F2-constats-*.json` | Échantillon et verdicts du recollationnement |
| `P2-F2-a.json`, `P2-F2-b.json` | Corrections tirées du recollationnement |
| `P2-F3-entrees-*.json`, `P2-F3-echantillon-*.json`, `P2-F3-constats-*.json` | Entrées et verdicts de la lecture au-delà du résumé |
| `P2-F3.json`, `P2-F3-b.json` | Corrections tirées de cette lecture |
| `P2-cloture.json` | Publication des résultats dans l'annexe E |

## Second audit : les majeurs

- **Ch. 35** : l'introduction donnait Singapour pour seul cadre dont l'agent est l'objet, contre la section 35.7 sur la Chine; le plan japonais compte quatre piliers, non deux.
- **Ch. 38** : la grille posait entre la ligne directrice de l'AMF et E-23 une équivalence que le chapitre n'établit pas.
- **Annexe E** : la ligne directrice de l'AMF, jamais lue, manquait à la liste des preuves minces.
- **Ch. 21** : chiffres de Who&When donnés sans dire qu'ils portent sur des périmètres différents; point à retenir plus tranché que MAS-FIRE; parts calculées données pour citées.
- **Ch. 22** : sources dites indépendantes des éditeurs alors que deux viennent d'employés d'éditeurs.
- **Ch. 23** : intertitre qui attribuait aux trois acceptions d'éditeurs ce que le chapitre retient lui-même.
- **Ch. 4** : les statistiques officielles ne « bornent » pas les enquêtes privées, dont le champ diffère.
- **Ch. 34** : les effets externes relèvent de la compensation, non des mécanismes de la section.
- **Ch. 40, 48, 50** : l'étude de Statistique Canada sur la productivité repose sur des données de 2019 et de 2021, ce que le texte taisait.
- **Ch. 41** : renvoi à la section 48.8 pour des mesures d'emploi qu'elle ne contient pas.
- **Ch. 42** : tableau de synthèse resté en retard sur le complément.
- **Ch. 48** : l'hypothèse H1 était rattachée à des travaux qui ne la portent pas.
- **Ch. 49** : le registre de veille faisait suivre une série de Statistique Canada que le chapitre dit terminée.
- **Ouverture** : l'échéance de l'AMF était rangée sous « textes en vigueur » sans que le texte ait été lu.

## Constats laissés sans correction

| Constat | Raison |
|---|---|
| Ch. 23, source [21] sans adresse | Adresse non retrouvée |
| Ch. 8, étendue de lecture de [24] et [25] | Étendue d'origine non consignée; ces deux sources ont depuis été relues au lot F3 |
| Ch. 18, paragraphe DBOS et Cloudflare mal placé | Déplacement à faire à la main |
| Ch. 41, « temps de révision prévu à l'horaire » | L'agent demande un recoupement sur le texte brut avant de corriger |
| Ch. 42, phrase sur le portrait de MAP | Passage introuvable tel que cité |
| Ch. 42, emplacement de la sous-section « Trois publications de 2026 » | Déplacement à faire à la main |
| Ch. 48, cas [96] rangé sous « Évaluation »; sources [87] à [101] sans année ni auteurs | Reclassement et notices à compléter à la main |
| Ch. 49, cinq faits sans appel de source | Déclarés dans le chapitre; à sourcer comme au chapitre 50 |
| F3-056 (ch. 14, source [26]) | Deux lectures de l'outil se contredisent : à trancher à la main |
| F3-075 (ch. 21), F3-114 (ch. 42) | Phrase non délimitée par l'outil; nuance non appliquée |

## Limites de ces contrôles

- Toutes les lectures passent par un outil qui condense les pages et s'arrête vers 100 000 caractères. Aucune n'a été recoupée sur le texte brut, le téléchargement étant refusé par le contrôle de permissions de la session. Quelques PDF ont été extraits localement de la copie que l'outil enregistre.
- Les corrections du lot F3 ont été rédigées par un modèle Sonnet et appliquées après un crible mécanique (colonnes de tableau, appels de source, notes éditoriales) et une lecture des constats, non une relecture mot à mot des 88 remplacements.
- Les 18 phrases non vérifiables du recollationnement tiennent à des sites qui refusent les robots (McKinsey, Science, INFORMS, IEEE Xplore, PMC) ou à des notices sans résumé.
- La partie X n'entre pas dans le lot F3 : ses sources sont lues par leur résumé, méthode que le chapitre 48 déclare.

## Outillage

`Master/compendium-master-lot.py` a reçu deux garde-fous, nés de deux refus du contrôle du registre : une ancre ne peut pas déborder d'une entrée antérieure, et un remplacement ne peut pas ramener un texte que le registre a remplacé.

## Vérification

```
lot P2-F3 : 88 remplacements à faire, 0 déjà en place, registre à 833 entrées
lot P2-cloture : 1 remplacements à faire, 0 déjà en place, registre à 837 entrées
PDF : 1097 pages, 425881 mots, 16.3 Mo
Tous les contrôles passent.
```
