# 7 — Livre 2027 : *Gouverner l'industrialisation cognitive*

*Architecture de contrôle, preuve et souveraineté dans l'entreprise agentique*

> **État actuel** : **Définition des besoins amont complétée (`v1.0`) — En attente de vos ajustements éventuels avant lancement de la production intégrale 100 % agentique.**

Ce répertoire contient l'ensemble des livrables normatifs amont (`PRD`, `TOC`, contrat machine `manifest.json`, charte éditoriale, protocole `MLR` ouvert, registres de vérité et contrat d'assurance qualité multi-agents) conçus pour piloter sans intervention humaine la recherche complémentaire, la rédaction, l'illustration et la quintuple vérification d'un livre de **~260–270 pages (`74 000 mots ± 8 %`, liminaire architectural substantiel + 12 chapitres, 23 figures)** en 2027.

---

## Arborescence des livrables amont

- [`specs/prd.md`](specs/prd.md) — **Cahier des charges (`PRD`)** : thèse falsifiable, lectorat, délimitation du périmètre démontré (`DC-01`), six anti-objectifs stricts (`AO-01` à `AO-06`) et dix-huit critères d'acceptation exécutables (`CA-01` à `CA-18`).
- [`specs/toc.md`](specs/toc.md) — **Table des matières contractuelle (`TOC`)** : découpage du liminaire architectural sur l'interopérabilité et l'orchestration (`0.1` à `0.6`, `4 200` mots), des 4 parties, des 12 chapitres (`X.1` à `X.4`) et des 3 annexes, avec ouverture narrative, figures assignées et propriété exclusive des concepts pour empêcher toute redite.
- [`specs/manifest.json`](specs/manifest.json) — **Contrat machine d'orchestration** : budgets de mots min/cible/max par unité, expressions régulières bannies en prose (zéro code matriciel `CAP-*`/`EXIG-*`), chemins vers le corpus interne et spécification des 23 figures (`Fig-00` à `Fig-22`).
- [`specs/charte-editoriale.md`](specs/charte-editoriale.md) — **Charte de prose et de mise en page** : structure narrative en 5 mouvements, sobriété épistémique, règles français canadien / anglais, échappement des montants `\$` et étalons stylistiques de comparaison.
- [`specs/protocole-mlr-2027.json`](specs/protocole-mlr-2027.json) — **Protocole de revue de littérature ouverte (`L+`)** : 6 axes `RQ1`–`RQ6`, semences vérifiées (DeepMind *From AGI to ASI*, *Virtual Agent Economies*, NBER *Coasean Singularity*, lois d'échelle multi-agents, exécution durable, `WIMSE`/`PQC`, `STAMP`) et politique `AO-01` sans contournement.
- [`specs/contrat-aq.md`](specs/contrat-aq.md) — **Protocole d'assurance qualité 100 % agentique** : séparation stricte des rôles à travers 5 barrières (`G1` garde mécanique, `G2` ancrage atomique Wyvern, `G3` double recollation stratifiée à l'aveugle sur 2 graines disjointes, `G4` `gauntlet-loop` A/B à l'aveugle, `G5` lissage transversal et inspection visuelle).
- [`specs/plan-production-aq.md`](specs/plan-production-aq.md) — **Plan d'exécution de l'usine agentique** : séquence opérationnelle en 6 tâches testables prête à être déclenchée.
- [`registre/`](registre/) — **Sources uniques de vérité initialisées** : [`ancres-chronologiques.json`](registre/ancres-chronologiques.json), [`faits-empiriques.json`](registre/faits-empiriques.json) et [`glossaire-termes.json`](registre/glossaire-termes.json).
- [`sources-locales/`](sources-locales/README.md) — Dépôt optionnel de PDF ou textes primaires licites à inclure en `statut L+` avant le lancement.
- [`outils/verifie_specs.py`](outils/verifie_specs.py) — Vérificateur mécanique de cohérence interne des spécifications amont.

---

## Vérification mécanique des spécifications amont

Depuis la racine du dépôt :

```powershell
python "7 - Livre 2027/outils/verifie_specs.py"
```

---

## Comment ajuster vos choix avant de lancer la production

1. **Titre, licence ou tolérance de longueur** : modifier les champs d'en-tête de [`specs/manifest.json`](specs/manifest.json) et [`specs/prd.md`](specs/prd.md) (p. ex. passer `commercial_override` à `true` pour une édition commerciale à droits réservés).
2. **Découpage ou poids d'un chapitre** : ajuster [`specs/toc.md`](specs/toc.md) et l'entrée correspondante de `units` dans [`specs/manifest.json`](specs/manifest.json), puis relancer `verifie_specs.py` pour contrôler les totaux.
3. **Ajout de sources fermées obtenues licitement** : glisser vos fichiers PDF ou `.txt` dans [`sources-locales/`](sources-locales/README.md).
4. **Lancement de la production intégrale et de l'AQ** : ouvrir une session dédiée (recommandé avec `/goal` et `/boost` ou `/teamwork`) en demandant d'exécuter [`specs/plan-production-aq.md`](specs/plan-production-aq.md).
