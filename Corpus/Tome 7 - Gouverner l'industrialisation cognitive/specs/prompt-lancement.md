# Prompt de lancement — Usine de production et d'AQ du 7 - Livre

> **Mode d'emploi** : ouvrir une **nouvelle session** dans le dépôt `c:\Github\Agentique`, activer `/goal` (et `/boost` si souhaité), puis coller le bloc ci-dessous. Ajuster au besoin la date exacte de gel et le plafond budgétaire de la barrière `G4` avant l'envoi.

```text
Exécute intégralement et sans interruption, en régime Production, le plan d'usine `7 - Livre/specs/plan-production-aq.md` (Tâches 1 à 6) afin de produire, illustrer, vérifier et assembler l'ouvrage complet « Gouverner l'industrialisation cognitive : Architecture de contrôle, preuve et souveraineté dans l'entreprise agentique » (auteur : André-Guy Bruneau, M.Sc IT; gel des faits arrêté par l'auteur au 2 décembre 2026; parution : janvier 2027).

1. Contrat normatif obligatoire
Lis d'abord `7 - Livre/specs/prd.md`, `toc.md`, `manifest.json`, `charte-editoriale.md`, `protocole-mlr-2027.json` et `contrat-aq.md`, puis exécute `python "7 - Livre/outils/verifie_specs.py"`. Respecte sans exception `DC-01` et `AO-01` à `AO-07` :
- Zéro contournement d'accès (`HTTP 403`, `429`, WAF, CAPTCHA, Anubis ou mur payant -> consigner en `statut F`, exclure de toute preuve, `0 %` de `METADATA_ONLY`).
- Zéro preuve circulaire : les volumes `1` à `6` du dépôt servent uniquement de carte de repérage; réancre chaque fait et chaque entrée `a_reancrer` de `registre/` sur sa source primaire ouverte en `statut L+` hachée `SHA-256` (et s'appuyer sur `arXiv:2606.12683` pour la preuve `SEED-01`, la copie locale dans `sources-locales/` ne servant que d'inspiration et restant hors Git).
- Zéro jargon matriciel interne (`CAP-`, `EXIG-`, `POR-`, `ANC-`, `INI-`, `PEX-`, `SIG-`, `ADR-`, `Classe`, `Stade`, `Palier`, marqueurs bruts), zéro auto-plagiat >= 12 mots face à `Corpus/`, scénarios non documentés explicitement balisés comme scénarios illustratifs sans chiffres présentés comme mesurés (`AO-07`), montants en dollars échappés en `\$`, formules en `\(...\)` compilées avec `-f markdown-tex_math_dollars+tex_math_single_backslash`, et toutes les dates de 2027+ rédigées au futur comme échéances à venir.

2. Autorisation explicite de délégation et d'étanchéité d'AQ
Je te demande et t'autorise expressément à lancer des sous-agents isolés via `invoke_subagent` (jamais `swarm`, afin de préserver l'étanchéité à l'aveugle) pour :
- paralléliser la collecte ouverte `L+`, la génération des 23 figures (`Fig-00` à `Fig-22`) et la rédaction cloisonnée des 13 unités narratives (`00 - Liminaire` + `Chapitres 01 à 12`, cible `70 000 mots` narratifs et `74 000 mots ± 8 %` au total);
- exécuter de façon strictement indépendante (aucun agent ne vérifie ni ne note son propre travail, contexte neuf à chaque passe) l'ordre imposé des cinq barrières de `contrat-aq.md` :
  `G1` (`verifie_manuscrit.py --strict`) -> `G2` (13 agents `auditeur-wyvern` neufs sur `ch00`..`ch12` jusqu'à `100 %` de claims `supportés`) -> `G3` passe 1 (`seed=202701`, agent `recollateur-1` neuf sur `.txt` bruts ramené à `60/60`) -> `G4` (`gauntlet-loop` A/B à l'aveugle contre les extraits étalons français de `manifest.json`, avec un plafond budgétaire total dédié à `G4` fixé à 15 % du budget global de la session et arrêt par unité sur victoire A/B, gains marginaux sur 2 tours consécutifs ou atteinte du plafond, suivi d'un repassage `G1` + `G2` différentiel) -> `G5` lissage transversal par un agent `lisseur-editorial` neuf (suivi de `G1` + `G2` différentiel) -> `G3` passe 2 à froid sur le texte final (`seed=202702`, 0 chevauchement, agent `recollateur-2` neuf : seuil >= 57/60 avant correction et 60/60 après, sinon retour des unités fautives en `G2` et retirage `seed=202703`) -> `G5` régénération déterministe des Annexes A–C, assemblage `.md`, `.html` autonome et `.pdf` (`Typst`), et inspection visuelle de 100 % des pages rendues.

3. Condition d'achèvement et livraison Git
Ne t'arrête pas avant que `CA-01` à `CA-18` soient tous validés à `100 %` preuves à l'appui dans `ancrage/` et `aq/`. Commite proprement chaque jalon validé dans `7 - Livre/` (sans jamais versionner `sources-locales/*` hors `README.md`, ni toucher aux volumes `1` à `6`) et pousse sur `origin main` à la clôture finale.
```
