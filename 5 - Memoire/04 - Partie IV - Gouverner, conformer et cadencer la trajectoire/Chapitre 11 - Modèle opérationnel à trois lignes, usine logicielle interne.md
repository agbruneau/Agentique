# Chapitre 11 — Modèle opérationnel à trois lignes, usine logicielle interne et approvisionnement réversible

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 24, ch. 36, ch. 39, ch. 41, ch. 47]` · `[CAD26 ch. 11, ch. 13 | PRIN-10, EXIG-GOV-01..20, EXIG-APP-01..17]` · `[C27 ch. 39, ch. 41, ch. 47 | ADR-003, ADR-025, ADR-029..031]` · `[PD28 M-24, M-26 | CAP-020, CAP-034, CAP-047..052, DEC-010]`.

*Question directrice : Quelle organisation humaine, quelle chaîne de fabrication logicielle interne et quelles clauses contractuelles empêchent l’érosion de la supervision, le verrouillage fournisseur et les agents fantômes ?*

**Thèse du chapitre :** Dans l’entreprise agentique, la ressource rare demeure le jugement humain qualifié P : PRI-007 P : CAP-048. Pour prévenir agents fantômes, auto-approbation et enfermement contractuel, l’institution déploie un modèle en étoile à trois lignes avec registre à sept états et un seul imputable `A` par décision E : EXIG-GOV-03 E : EXIG-GOV-04 E : EXIG-GOV-07. Elle lui associe une usine logicielle séparant Oracle et Bâtisseur sans interpréteur libre (*shell*) P : CAP-052 P : DEC-010, ainsi que dix clauses contractuelles de réversibilité E : EXIG-APP-07 E : EXIG-APP-16 E : EXIG-APP-17.

## 11.1 Modèle en étoile à trois lignes, registre à sept états et relève humaine

`C26 ch. 41` (`Tableau 41.1` `[S]`) distingue la **fabrique d’agents** (`F1`, dispositif organisationnel et CI/CD) des trois autres sens du mot : fabrique d’identité (`F2`), titre commercial (`F3`) et patron logiciel `factory` (`F4`). L’attention des valideurs ne croissant pas avec le volume (`C27 ch. 41`), `CAD26 ch. 11` et `C27 ch. 39` instaurent un **modèle en étoile (*Hub-and-Spoke*) à trois lignes** E : EXIG-GOV-01 E : EXIG-GOV-05 P : CAP-050 :

- **Première ligne scindée (plateforme et métiers).** La plateforme centrale opère le socle obligatoire E : EXIG-GOV-05 (passerelles, registre, catalogue, évaluation, coupe-circuit) et livre des gabarits conformes par construction (`SPIFFE`, trace sans contenu, budgets) rendant la voie gouvernée plus rapide que le contournement E : EXIG-GOV-06 (`DEVRAIT`). Chaque agent reçoit en domaine un **parrain métier nominatif** relié aux ressources humaines (`ADR-025`) et un **responsable technique** E : EXIG-GOV-01.
- **Deuxième ligne indépendante.** Risque de modèle (`BSIF E-23`), conformité, sécurité et RPRP valident la cote de risque, instruisent les dérogations et détiennent un droit de suspension.
- **Troisième ligne.** L’audit interne accède en lecture seule autonome aux registres, bancs scellés et journaux d’audit P : CAP-050.

Le comité d’architecture et des risques agentiques E : EXIG-GOV-02 applique deux invariants RACI : **un seul rôle** `A` **(imputable) par décision** avec suppléant E : EXIG-GOV-04, et l’**interdiction de cumuler construction et homologation** E : EXIG-GOV-03. Le registre compte **sept états** (`proposé` → `en conception` → `en construction` → `pilote` → `production` → `suspendu` → `retiré`) E : EXIG-GOV-07 P : CAP-047. Aucun justificatif n’est émis sans fiche approuvée E : EXIG-GOV-08 E : EXIG-GOV-17. Les agents fantômes repérés via journaux réseau, OAuth et SaaS sont régularisés sous cinq jours ouvrables ou désactivés E : EXIG-GOV-10 E : EXIG-GOV-16. Le parrain atteste l’agent tous les **12 mois** (**6 mois** en classe élevée), avec suspension trimestrielle des orphelins E : EXIG-GOV-13. Onze déclencheurs (quinze cas) imposent une réévaluation

E : EXIG-GOV-12 E : EXIG-GOV-18 E : EXIG-GOV-19 E : EXIG-GOV-20, et le retrait exige un **préavis** `≥ 60 jours` E : EXIG-GOV-14. Les dérogations écrites restent bornées à **6 mois** renouvelables une fois (**90 jours** par l’AE en classe faible), hors E : EXIG-GOV-17 E : EXIG-GOV-15 E : EXIG-GOV-16. Enfin, contre l’**atrophie de la relève junior** (`~20 %` chez les 22–25 ans, `PD28 M-26`, `SIG-017`), des quotas de dossiers formateurs préservent la révision `Loi 25 art. 12.1` et la reprise manuelle P : CAP-048.

| Instance ou rôle | Ligne | Responsabilité exclusive (`RACI` à un seul `A`) | Contrôle système associé |
| --- | --- | --- | --- |
| Parrain métier nommé (`RH`) | 1re (métier) | Imputable `A` de la finalité, du budget `CPO` et de l’attestation `6 / 12 mois` | Suspension trimestrielle automatique si poste vacant E : EXIG-GOV-13 |
| Équipe plateforme centrale | 1re (socle) | Exploitation des passerelles, du registre à 7 états et des gabarits conformes (`DEVRAIT`) | Rejet réseau hors registre E : EXIG-GOV-05 E : EXIG-GOV-06 E : EXIG-GOV-08 |
| Risque modèle, séc., RPRP | 2e ligne | Validation indépendante (`E-23`, ÉFVP), plafonds d’autonomie et coupe-circuit | Séparation stricte construction / homologation E : EXIG-GOV-03 |
| Audit interne | 3e ligne | Vérification périodique de bout en bout des preuves, dérogations et signaux | Accès autonome lecture seule aux journaux et bancs P : CAP-050 |

## 11.2 Usine logicielle interne : Oracle vs Bâtisseur, `WAP`, `SRE` et distillation

L’usage d’agents en développement, modernisation ou exploitation (`C27 ch. 47`, `C26 ch. 47`, `BSIF B-13 § 2.5.2`) obéit à une règle unique (`ADR-029` à `ADR-031`, sous la réserve empirique de `C27 § 47.1`). **L’agent qui produit un artefact ne définit jamais son oracle d’acceptation et ne publie jamais seul en production** P : CAP-052. Quatre chantiers d’ingénierie en découlent :

1. **Code et modernisation patrimoniale.** Les dépôts et permissions séparent techniquement l’agent **Oracle** (invariants et jeux d’essai) et l’agent **Bâtisseur**, sous porte d’analyse statique du code généré et intégrité d’artefacts E : EXIG-SEC-17 E : EXIG-SEC-18 et revue humaine. Le code existant est exposé par graphes syntaxiques et sémantiques (`AST` et `SCIP`, *SCIP Code Intelligence Protocol*) ; les tests générés (~50 % de faux positifs à filtrer) sont qualifiés par un score de **mutation** `≥ 85 %` `[S]`, puis toute réécriture patrimoniale subit un `Shadow Mirroring` **de** `30 jours` `[S]` à zéro écart décimal (cibles de conception sans appui empirique) avant bascule P : POR-008.
2. **Exploitation des flux de données (*DataOps*).** Les pipelines analytiques appliquent des contrats formels `ODCS v3` selon le patron `Write-Audit-Publish` **(**`WAP`**)** : écriture sur branche isolée, contrôle automatique d’intégrité et de dérive, et mise en quarantaine immédiate de tout lot hors bornes avant qu’un agent ou index ne puisse le lire E : EXIG-INT-12 E : EXIG-INT-19 P : CAP-020 P : DEC-010 P : POR-005.
3. **Exploitation** `SRE` **sans interpréteur libre.** Les journaux bruts contenant des chaînes propices à l’injection indirecte (`C27 ch. 47`), le diagnostic s’effectue en lecture seule sur flux assainis et la remédiation n’exécute que des procédures pré-signées et bornées, avec **interdiction absolue de tout interpréteur de commandes libre (*shell*) en production** (`ADR-030`) P : DEC-010.
4. **Distillation** `LLM → SLM` **sous sas de purge des** `RP`**.** Conditionnée aux signaux économiques ou énergétiques (`SIG-015`, `SIG-016`, `ADR-031`) P : CAP-034 P : INI-028, la distillation vers de petits modèles spécialisés traverse un **sas irréversible de purge des renseignements personnels (**`RP`**)** validé par jetons témoins (*canaris* d’extraction, `Loi 25` E : EXIG-CON-10), une porte de parité `pass^5 ≥ 99 %` `[S]` (cible sans appui empirique) et une sentinelle continue de dérive.

## 11.3 Approvisionnement réversible et dix clauses contractuelles (`EXIG-APP-07..16`)

Face aux plateformes commerciales fermées sur leur plan de contrôle, `CAD26 ch. 13` impose une grille éliminatoire conservée au registre et rejouée à chaque renouvellement E : EXIG-APP-17 P : CAP-051. Elle exige le chiffrage du coût de sortie E : EXIG-APP-01, le refus des extensions verrouillantes E : EXIG-APP-02 et les preuves `MCP`/`A2A` E : EXIG-APP-03. Elle impose aussi des mesures sur les cas de l’acheteur E : EXIG-APP-04, l’export ouvert des traces et coûts E : EXIG-APP-05 et la maîtrise des identités et de l’arrêt E : EXIG-APP-06. Tout contrat intègre ensuite les **dix clauses** `EXIG-APP-07` **à** `EXIG-APP-16` P : INI-014, vérifiées par un exercice annuel d’extraction P : POR-016 :

| Exigence | Objet contractuel obligatoire (`CAD26 § 13.3`) | Risque paré / ancrage |
| --- | --- | --- |
| `EXIG-APP-07` | Interopérabilité `MCP`/`A2A` et portabilité sans frais des cartes, schémas et définitions | Enfermement syntaxique |
| `EXIG-APP-08` | Prise en charge de la délégation d’identité sans secret statique partagé | Délégué confus et clés fixes |
| `EXIG-APP-09` | Export sans surcoût des traces `OpenTelemetry`, coûts `FOCUS` et facteurs d’explicabilité | Opacité `art. 12.1` / `E-23` |
| `EXIG-APP-10` | Usage limité au mandat ; **interdiction d’entraîner ou d’ajuster** sur données, invites ou traces | Fuite de patrimoine cognitif |
| `EXIG-APP-11` | Lieux de résidence garantis, encadrement `Loi 25 art. 17` et divulgation des lois étrangères | Accès extraterritorial |
| `EXIG-APP-12` | Notification d’incident alignée sur le délai réglementaire le plus strict (`BSIF`, `Loi 25`, `RIA`) | Retard de déclaration E : EXIG-CON-25 |
| `EXIG-APP-13` | Droit d’audit (`BSIF B-10`), `SBOM` et **préavis écrit** avant retrait ou modification d’un modèle | Rupture silencieuse de modèle |
| `EXIG-APP-14` | Plan de sortie assisté sans pénalité prohibée (`Data Act` D `ANC-003`), formats ouverts, destruction attestée | Coût de sortie prohibitif (`POR-016`) |
| `EXIG-APP-15` | Accord écrit au sens de l’**article** `25(4)` **du** `RIA` **européen** répartissant rôles et assistance | Requalification en fournisseur E : EXIG-CON-15 |
| `EXIG-APP-16` | Révocation immédiate des `NHI` et arrêt d’urgence actionnables directement par l’institution | Perte du coupe-circuit |

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Instaurer le modèle en étoile à trois lignes E : EXIG-GOV-01 E : EXIG-GOV-05 P : CAP-050 : un seul `A` nommé par décision E : EXIG-GOV-04, séparation construction / validation E : EXIG-GOV-03, attestation parrain `6 / 12 mois` E : EXIG-GOV-13, quotas formateurs pour la relève junior P : CAP-048 et retrait sous préavis `≥ 60 jours` E : EXIG-GOV-14.
2. Rendre éliminatoires la grille préalable E : EXIG-APP-01 E : EXIG-APP-17 et les dix clauses `EXIG-APP-07` à `EXIG-APP-16` P : INI-014, vérifiées par un essai annuel de sortie P : POR-016.
3. Subordonner toute distillation interne aux signaux économiques ou énergétiques (`SIG-015`, `SIG-016`) C : tous ; SIG-015, SIG-016 et à un sas certifié de purge des `RP` P : CAP-034 P : INI-028.

Spécifications AS

1. Publier des gabarits d’agents conformes par construction E : EXIG-GOV-06 (`DEVRAIT`) raccordés au registre à sept états, au blocage réseau des agents non inscrits E : EXIG-GOV-08 E : EXIG-GOV-10 et aux onze déclencheurs (quinze cas) de réévaluation E : EXIG-GOV-12.
2. Cloisonner dans la chaîne CI/CD les droits de l’agent Oracle et de l’agent Bâtisseur (`ADR-029`, index `AST`/`SCIP`) P : CAP-052, déployer `Write-Audit-Publish` sous contrats `ODCS v3` P : CAP-020 et proscrire tout interpréteur libre en exploitation `SRE` P : DEC-010.
3. Exiger en modernisation et distillation un score de mutation `≥ 85 %` `[S]`, un `Shadow Mirroring` de `30 jours` `[S]` sans écart décimal P : POR-008 et une constance `pass^5 ≥ 99 %` `[S]` après sas de purge des `RP` à jetons témoins.

## 11.4 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Organisation entre plateforme centrale et domaines métiers | Modèle en étoile à trois lignes, un seul `A` nommé et séparation stricte construction / homologation E : EXIG-GOV-03 E : EXIG-GOV-04 E : EXIG-GOV-05 | Jamais sur la séparation des fonctions ni sur l’inscription au registre avec parrain actif E : EXIG-GOV-17 | `[N]` `BSIF E-23` (`ANC-103`), `B-13 § 2.5.2` ; `CAD26 ch. 11` |
| Agent dont le parrain quitte son poste ou omet l’attestation périodique | Passage automatique à `suspendu` lors de la revue trimestrielle et révocation des justificatifs E : EXIG-GOV-13 | Réaffectation formelle au registre vers un suppléant habilité avant l’échéance de 6 ou 12 mois | `[É]` `CAD26 § 11.5, EXIG-IAM-07` ; `PD28 POR-015` |
| Usage d’agents de génération de code et de refonte patrimoniale | Séparation technique des dépôts Oracle (tests) et Bâtisseur (code), revue humaine et parité en miroir (`ADR-029`) P : CAP-052 | Jamais d’auto-approbation de demande de tirage ni d’écriture du bâtisseur dans les jeux d’essai | `[N]` `BSIF B-13 § 2.5.2` ; `C27 ch. 47` (`≥ 85 %` `[S]`, `30 jours` `[S]`) |
| Remédiation assistée par agent (`SRE`) sur incident de production | Lecture seule sur journaux assainis et exécution exclusive de procédures pré-signées sans interpréteur libre P : DEC-010 | Jamais d’interpréteur ouvert en production ; toute action hors catalogue bascule à l’astreinte humaine | `[M]` `[É]` `[S]` Injection par les journaux (`C27 § 47.6`) ; `ADR-030` |
| Contractualisation d’une plateforme ou d’un logiciel-service agentique | Grille préalable et insertion des dix clauses `EXIG-APP-07` à `EXIG-APP-16` (non-entraînement, export, arrêt, sortie) E : EXIG-APP-17 | Dérogation écrite (`≤ 6 mois`) sur un critère technique mineur compensé à la passerelle, jamais sur l’arrêt E : EXIG-GOV-17 | `[N]` `BSIF B-10`, `Loi 25 art. 17`, `RIA art. 25(4)`, `Data Act` (`ANC-003`) |
| Distillation interne de grands modèles vers de petits modèles spécialisés | Option conditionnelle activée sur signal `SIG-015` ou `SIG-016` derrière un sas irréversible de purge des `RP` P : INI-028 | Flux répétitif à fort volume dégradant le `CPO` sur deux trimestres (`pass^5 ≥ 99 %` `[S]`) | `[S]` `C27 § 47.8, § 47.20` ; `PD28 CAP-034`, `ADR-031` |

## 11.5 Limites et renvois

Trois réserves méthodologiques encadrent ce chapitre. Premièrement, les seuils de `C27 ch. 47` — mutation `≥ 85 %`, `Shadow Mirroring` de `30 jours` et `pass^5 ≥ 99 %` — sont des **cibles sans appui empirique (**`[S]`**)**, tout chiffrage fictif du *Groupe Boréal Inc.* (`C27 § 0.5`) étant exclu. Deuxièmement, trois séries de coquilles de `CAD26` v1.1 sont corrigées : `EXIG-APP-18` fantôme p. 32, `EXIG-APP-12` au lieu d’`EXIG-APP-17` p. 233, et `EXIG-ARC-02` au lieu d’`EXIG-ARC-21` pp. 195–257. Troisièmement, les gains du développement assisté restent sensibles à la dette de revue humaine (`C27 § 47.1`). Renvois : `C26` ch. 24 (pp. 277–300), ch. 36 (pp. 415–424), ch. 39 (pp. 451–462), ch. 41 (pp. 472–479), ch. 47 (pp. 534–544), `CAD26` ch. 11 (pp. 190–205), ch. 13 (pp. 233–242), `C27` ch. 39 (pp. 783–792), ch. 41 (pp. 817–839), ch. 47 (pp. 950–995), `PD28` `M-24` (pp. 301–309), `M-26` (pp. 322–327) et `Annexes B–C`.
