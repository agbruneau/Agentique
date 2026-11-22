# Sources locales déposées par l'auteur (`statut L+`)

Déposez dans ce répertoire, **avant de lancer la production agentique**, tout document PDF ou texte UTF-8 obtenu licitement (rapports institutionnels, articles en libre accès ou tirés à part autorisés, notes réglementaires officielles) que les agents doivent lire intégralement et hacher en `SHA-256` dans `recherche/manifeste-sources-sha256.json`.

## Règles appliquées par l'usine agentique

1. **Aucune tentative de contournement en ligne (`AO-01`)** : les agents ne franchiront jamais un mur payant, un `HTTP 403`/`429` ou un défi anti-robot. Si une référence clé n'est pas librement téléchargeable par API ouverte, ce dossier est l'unique voie légitime pour l'intégrer au corpus probatoire `L+`.
2. **Pièce déjà repérée à la racine du dépôt** : `../Google Deepmind - What comes after AGI_ From AGI to Superintelligence — DeepMind Institute.pdf` est déjà déclarée dans `specs/protocole-mlr-2027.json` (`SEED-01`).
3. **Traçabilité automatique** : chaque fichier présent ici au lancement est extrait en texte intégral, horodaté et haché `SHA-256` afin de pouvoir être audité lors de l'ancrage Wyvern (`G2`) et des deux recollations à l'aveugle (`G3`).
