# Sources locales déposées par l'auteur (`statut L+`)

[Retour au sommaire du manuel](../README.md) · [Compendium](../../../../Compendium/README.md) · [Sources des tomes](../../README.md) · [Tomes publiés](../../../../Tomes/README.md) · [Index principal du dépôt](../../../../README.md)

Déposez dans ce répertoire, **avant de lancer la production agentique**, tout document PDF ou texte UTF-8 obtenu licitement (rapports institutionnels, articles en libre accès ou tirés à part autorisés, notes réglementaires officielles) que les agents doivent lire intégralement et hacher en `SHA-256` dans [`recherche/manifeste-sources-sha256.json`](../recherche/manifeste-sources-sha256.json).

## Règles appliquées par l'usine agentique

1. **Aucune tentative de contournement en ligne (`AO-01`)** : les agents ne franchiront jamais un mur payant, un `HTTP 403`/`429` ou un défi anti-robot. Si une référence clé n'est pas librement téléchargeable par API ouverte, ce dossier est l'unique voie légitime pour l'intégrer au corpus probatoire `L+`. Toute URL bloquée est consignée hors corpus dans [`recherche/registre-statut-f.json`](../recherche/registre-statut-f.json) (`10` exclusions enregistrées pour le Tome 8).
2. **Contenu jamais versionné** : tout fichier de ce répertoire, sauf ce `README.md`, est exclu du dépôt par [`Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/.gitignore`](../.gitignore) (`sources-locales/*` et `!sources-locales/README.md`, protection du droit d'auteur contrôlée mécaniquement par [`outils/verifie_specs.py`](../outils/verifie_specs.py)).
3. **Traçabilité automatique et état du Tome 8** : chaque fichier déposé ici au lancement est extrait en texte intégral, horodaté et haché `SHA-256` pour l'ancrage Wyvern (`G2`) et les recollations à l'aveugle (`G3`). Pour l'édition livrée du Tome 8 (`gel du 2 décembre 2026`), aucun fichier local supplémentaire n'a été requis : les `95` sources `L+` indexées dans [`recherche/manifeste-sources-sha256.json`](../recherche/manifeste-sources-sha256.json) proviennent toutes de dépôts ouverts (`0,0 %` de `METADATA_ONLY`, textes intégraux conservés dans [`recherche/corpus_l_plus/`](../recherche/corpus_l_plus/)).
