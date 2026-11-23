# Annexe G — Listes de contrôle d’homologation avant production (75 points)

Aucun système multi-agents de niveau L2, L3 ou L4 n’est autorisé à traiter des données réelles ni à invoquer des outils mutatifs avant d’avoir réussi une revue d’homologation opérationnelle (*Production Readiness Review*, PRR). L’annexe fournit pour cette revue une grille normative de soixante-quinze points de contrôle vérifiables, répartis en cinq domaines de quinze points. Les équipes Architecture, Cybersécurité, SRE/AgentOps et Conformité peuvent l’utiliser directement.

IMPORTANT

**Règle d’homologation recalibrée.** Chaque point porte sa force probatoire (`[N]` normatif/légal, `[M]` mesuré, `[É]` éditeur, `[S]` synthèse d’architecture). Seuls les **24 points** `**[BLOQUANT]**` (obligations légales `[N]` et invariants de sûreté déterministes exécutables en 2027) bloquent une mise en production L3/L4; les **26 points** `Conditionnel` dépendent du périmètre (CUA, OT, B2B, TEE, distillation) ou de la maturité du standard; les **25 points** `Élevée` (19) et `Moyenne` (6) valent recommandations cibles.

## G.1 Grille 1 — Identité non humaine (NHI), sécurité à confiance zéro et isolation (15 points)

| # | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
| --- | --- | --- | --- |
| **S-01** | Identité NHI unique inscrite à l’annuaire d’entreprise (aucune clé API partagée) | **[BLOQUANT]** [N] | Entrée du registre d’agents et identifiant SPIFFE / Entra Agent ID |
| **S-02** | Attestation cryptographique de la provenance du code et de la configuration système | Élevée [S] | Signature Sigstore/cosign vérifiée au démarrage du pod |
| **S-03** | Délégation OAuth 2.1 On-Behalf-Of (RFC 8693) préservant `sub` et la chaîne `act` | **[BLOQUANT]** [N] | Capture d’un jeton JWT décodé en pré-production |
| **S-04** | Atténuation de portée à chaque saut inter-agents | Conditionnel [S] | Test automatisé de rejet hors portée (obligatoire si multi-sauts) |
| **S-05** | Durée de vie courte des jetons (≤ 15 min) et contrainte au détenteur (DPoP/mTLS) | Élevée [N] | Configuration du serveur d’autorisation et test de rejeu négatif |
| **S-06** | Séparation entre l’agent d’interface exposé et l’agent détenteur d’outils d’écriture | **[BLOQUANT]** [S] | Diagramme de flux réseau et politique d’accès passerelle |
| **S-07** | Épinglage cryptographique (empreinte SHA-256) des descriptions et schémas MCP | Conditionnel [S] | Manifeste d’empreintes SHA-256 signé et alerte sur modification distante (*rug pull*) |
| **S-08** | Marquage structurel des données externes non fiables contre l’injection indirecte (ASI01) | **[BLOQUANT]** [M] | Rapport d’équipe rouge automatisée et contrôles hors modèle |
| **S-09** | Évaluation déterministe hors LLM (Cedar ou OPA) devant chaque appel d’outil mutatif | **[BLOQUANT]** [N] | Jeu de règles Cedar/Rego versionné et tests unitaires associés |
| **S-10** | Approbation hors bande asynchrone (CIBA) activée pour les actions à haut risque | Conditionnel [S] | Démonstration de suspension/reprise signée (profil CIBA non normalisé) |
| **S-11** | Exécution de tout code ou script dynamique en bac à sable isolé (OpenSandbox/microVM) | **[BLOQUANT]** [N] | Spécification prouvant l’absence de privilèges hôte et de sortie libre |
| **S-12** | Protection contre l’empoisonnement de la mémoire partagée (ASI06) et validation d’écriture | Élevée [M] | Politique de validation et approbation avant écriture mémoire |
| **S-13** | Chiffrement mutuel et intégrité des messages inter-agents (mTLS; SLIM/MLS optionnel) | Conditionnel [N] | Politique mTLS interdisant le clair (SLIM/MLS = brouillon IETF) |
| **S-14** | Coupe-circuit centralisé du SOC, révoquant jetons et sessions en < 10 secondes | **[BLOQUANT]** [S] | Procès-verbal d’exercice de déclenchement du coupe-circuit |
| **S-15** | Validation de la séparation des tâches sur les flux financiers/sensibles | **[BLOQUANT]** [N] | Preuve qu’aucun identifiant NHI unique ne peut instruire et approuver seul |

## G.2 Grille 2 — Résilience, exécution durable et intégrité transactionnelle (15 points)

| # | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
| --- | --- | --- | --- |
| **R-01** | Inviolabilité des systèmes d’enregistrement (passage exclusif par des API/BAPI métiers validées) | **[BLOQUANT]** [S] | Revue des connecteurs confirmant l’absence d’écriture SQL directe |
| **R-02** | Ancrage de tout flux multi-étapes mutatif dans un moteur durable (Temporal/Restate) | Conditionnel [É] | Code source distinguant logique déterministe et activités (si flux long) |
| **R-03** | Clé d’idempotence déterministe transmise et honorée sur chaque outil à effet de bord | **[BLOQUANT]** [N] | Test de double envoi prouvant l’absence de doublon métier |
| **R-04** | Compteur dur de sauts restants (`maxRemainingHops`) dans l’enveloppe d’action | Conditionnel [S] | Test unitaire d’arrêt à épuisement du TTL (si délégation multi-agents) |
| **R-05** | Détection des boucles circulaires inter-plateformes SaaS par vecteur de corrélation | Élevée [S] | Test croisé entre deux orchestrateurs simulant un renvoi mutuel |
| **R-06** | Définition explicite d’une action de compensation Saga ou d’un bail TTL par mutation | **[BLOQUANT]** [S] | Matrice des étapes de la saga et test automatisé de retour arrière |
| **R-07** | Tampon de pré-engagement (fenêtre de grâce ou approbation) devant toute action irréversible | **[BLOQUANT]** [N] | Architecture du connecteur courriel/paiement/publication externe |
| **R-08** | Revalidation des préconditions métiers et des droits IAM au réveil d’une pause longue (T4) | Élevée [S] | Scénario de test simulant une révocation d’accès pendant l’attente |
| **R-09** | Retour d’erreurs structurées et exploitables cognitivement par les serveurs MCP | Moyenne [É] | Catalogue des codes d’erreur d’outils (transitoire vs fatal) |
| **R-10** | Politique de réessai avec recul exponentiel et gigue, hors du LLM | Élevée [S] | Configuration de la passerelle et du moteur durable |
| **R-11** | Mode dégradé déterministe documenté en cas d’indisponibilité du fournisseur de modèle | Élevée [S] | Test de bascule multi-fournisseurs ou de routage vers une file humaine |
| **R-12** | Confinement des agents d’utilisation d’interface graphique (CUA), avec assertions visuelles | Conditionnel [S] | Harnais de sécurité CUA (uniquement si CUA employé) |
| **R-13** | Validation sur jumeau numérique déterministe avant toute consigne vers l’univers OT | Conditionnel [S] | Rapport de test du sas IT/OT (uniquement si périmètre OT; ch. 28) |
| **R-14** | Cloisonnement multilocataire du contexte et des caches d’inférence | **[BLOQUANT]** [N] | Test d’étanchéité inter-clients / inter-divisions sous charge |
| **R-15** | Campagne d’ingénierie du chaos réussie (latence extrême, erreurs HTTP 429/500, JSON tronqué) | Élevée [S] | Rapport d’exécution du harnais de chaos sans corruption d’état |

## G.3 Grille 3 — Observabilité OpenTelemetry, qualité ADLC et FinOps (15 points)

| # | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
| --- | --- | --- | --- |
| **O-01** | Émission de traces distribuées (conventions OpenTelemetry `gen_ai.*`, statut *Development*) | Conditionnel [É] | Visualisation d’une trace complète (schéma OTel évolutif, ch. 33) |
| **O-02** | Caviardage ou masquage automatique des renseignements personnels (PII) avant export OTel | **[BLOQUANT]** [N] | Configuration du processeur de filtrage avant export |
| **O-03** | Versionnage SemVer + Intent du code, des instructions, du modèle, des schémas et politiques | Élevée [S] | Manifeste de version immuable dans le dépôt Git et le registre |
| **O-04** | Suite de simulation multi-tours représentative (dont cas adversariaux) | Conditionnel [S] | Dossier de scénarios versionné (taille calibrée par criticité) |
| **O-05** | Seuil de constance pass^𝑘 atteint (𝑘 ≥ 5) sur les invariants métiers critiques | Conditionnel [M] | Rapport CI/CD affichant pass^5 au seuil fixé dans l’ADR |
| **O-06** | Détection automatique en temps réel des boucles sémantiques (verrouillages actifs répétitifs) | Élevée [S] | Règle d’alerte et d’interruption configurée sur la télémétrie |
| **O-07** | Procédure de déploiement progressif (mode fantôme, puis canari à 1–5 %) | Élevée [S] | Routage pondéré et critères de retour arrière |
| **O-08** | Retour arrière automatisé vers la version N-1 stable (cible `< 2 min`) | Élevée [S] | Journal d’un test de retour arrière déclenché sur anomalie |
| **O-09** | Enveloppe budgétaire maximale en devises (`maxTotalCostCad`) active par transaction/saga | **[BLOQUANT]** [S] | Test démontrant l’arrêt propre au dépassement du plafond FinOps |
| **O-10** | Routage cognitif hybride privilégiant les SLM pour l’extraction et le triage | Moyenne [S] | Répartition mesurée des appels par palier de modèle |
| **O-11** | Optimisation et mesure du taux de réutilisation du préfixe / KV-cache inter-tours | Moyenne [É] | Tableau de bord TTFT et ratio de jetons en cache |
| **O-12** | Imputation analytique des coûts par unité d’affaires, processus et client | Élevée [S] | Étiquettes FinOps (affichage avant refacturation, section 40.2) |
| **O-13** | Définition formelle de l’événement métier de succès pour calculer le coût par résultat | Élevée [S] | Formule analytique reliant coût technique et résultat validé |
| **O-14** | Surveillance continue de la dérive sémantique et du taux d’escalade | Élevée [S] | Tableau de bord AgentOps hebdomadaire avec seuils d’alerte |
| **O-15** | Protocole de décommissionnement propre (révocation NHI, archivage, redirection) | Moyenne [S] | Procédure d’extinction d’agent validée par l’équipe plateforme |

## G.4 Grille 4 — Gouvernance, droit, facteur humain et conformité 2027 (15 points)

| # | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
| --- | --- | --- | --- |
| **G-01** | Propriétaire métier nominatif désigné | **[BLOQUANT]** [N] | Fiche de responsabilité au registre d’agents d’entreprise |
| **G-02** | Inscription au système de management de l’IA conforme à ISO/IEC 42001 | Élevée [N] | Fiche d’impact, analyse de risques et cycle PDCA |
| **G-03** | Qualification réglementaire de l’empreinte de déploiement | **[BLOQUANT]** [N] | Grille qualifiant tous les systèmes aval connectés |
| **G-04** | Conformité BSIF/OSFI E-23 (échéance 1er mai 2027) | Conditionnel [N] | Cote de matérialité et validation (si institution fédérale canadienne) |
| **G-05** | Évaluation des facteurs relatifs à la vie privée (ÉFVP — Loi 25 / RGPD) | **[BLOQUANT]** [N] | Dossier ÉFVP et cartographie des flux transfrontaliers |
| **G-06** | Mécanisme d’information, d’explication et de révision (Loi 25 art. 12.1) | **[BLOQUANT]** [N] | Parcours testé lorsqu’une décision exclusivement automatisée s’applique |
| **G-07** | Divulgation de l’interaction avec une IA (EU AI Act art. 50, 2 août 2026) | **[BLOQUANT]** [N] | Mention explicite dans les interfaces, voix et courriels (si périmètre UE) |
| **G-08** | Dossier technique et supervision renforcée si haut risque (EU AI Act Annexe III) | Conditionnel [N] | Documentation technique (si cas d’usage Annexe III, déc. 2027) |
| **G-09** | Alignement sémantique des concepts critiques (Apache Ossie `0.1.1` optionnel, en incubation) | Moyenne [S] | Dictionnaire de métriques gouverné (ne rien bâtir sur `0.3.0.dev0`, ch. 12) |
| **G-10** | Droit à l’effacement et purge sélective vérifiable dans la mémoire à long terme | **[BLOQUANT]** [N] | Test d’oubli d’une entité sans dégradation résiduelle |
| **G-11** | Ergonomie HOTL présentant les preuves contradictoires (prévention ASI09) | Élevée [M] | Revue d’interface d’approbation sans incitation biaisée |
| **G-12** | Dispositif périodique de maintien de vigilance des superviseurs (HOTL) | Moyenne [M] | Dossiers tests d’étalonnage et suivi du temps de revue |
| **G-13** | Plafonds et mandats signés (p. ex. AP2) pour toute transaction commerciale B2B | Conditionnel [S] | Politique de délégation de signature financière et mandats SD-JWT |
| **G-14** | Garde-fous anti-collusion algorithmique sur les agents de prix ou d’enchères | Conditionnel [N] | Audit des consignes et journaux (si tarification ou enchères) |
| **G-15** | Archivage immuable et horodaté (WORM) des décisions critiques | **[BLOQUANT]** [N] | Politique de rétention conforme aux délais légaux |

## G.5 Grille 5 — Fédération B2B, souveraineté cognitive, périphérie et usine interne (15 points)

| # | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
| --- | --- | --- | --- |
| **F-01** | Authentification légale vLEI et contrat d’usage ODRL 2.2 sur canal B2B | Conditionnel [N] | Accord EDC et test de rejet non signé (si fédération B2B) |
| **F-02** | Scission entre l’agent diplomate B2B et l’évaluateur interne (aucun secret en DMZ) | Conditionnel [S] | Revue d’architecture et test d’extraction (si négociation B2B) |
| **F-03** | Rapprochement tripartite déterministe (Cedar) avant libération AP2 / x402 | Conditionnel [S] | Test d’intégration couvrant écarts (si règlement agentique B2B) |
| **F-04** | Résidence juridictionnelle vérifiée des couches d’état (sections 46.1 et 46.9) | **[BLOQUANT]** [N] | Matrice de géorepérage pour les classes C2 (Loi 25) et C3 (E-23) |
| **F-05** | Clés de chiffrement d’état et de pseudonymisation détenues localement (HYOK en HSM) | Élevée [S] | Preuve de révocation d’accès HSM rendant les journaux illisibles |
| **F-06** | Attestation matérielle distante CPU+GPU (TEE) avant déchiffrement de charge C3 | Conditionnel [É] | Politique PCR du vérificateur (si charge C3 sur enclave distante) |
| **F-07** | Profil de secours à poids ouverts testé (cible de conception `RTO < 15 min`) | Conditionnel [S] | Compte rendu d’exercice de coupure primaire (RTO calibré par SLA) |
| **F-08** | Survie hors ligne en périphérie (durée calibrée par site, cible 72 h) et baux CRDT | Conditionnel [S] | Rapport d’essai WAN coupé sans double dépense (si site isolé) |
| **F-09** | Enveloppe matérielle Simplex (`ISO 10218-1:2025` / IEC 61508) sur pont MCP ↔︎ ROS 2 | Conditionnel [N] | Homologation sécurité machine (uniquement si robotique mobile) |
| **F-10** | Distribution signée TUF/Sigstore à double clé en périphérie, avec bascule A/B | Conditionnel [N] | Test de rejet d’archive altérée ou expirée (si flotte périphérique) |
| **F-11** | Séparation des devoirs dans l’usine logicielle (bâtisseur interdit sur les tests d’or) | Conditionnel [S] | Règles Git et confinement bac de compilation (si usine ADLC) |
| **F-12** | Porte de mutation et parité en exécution miroir (cibles 85 % / 30 j calibrées par ADR) | Conditionnel [S] | Rapport de parité dans le seuil de tolérance fixé par l’ADR (si refonte) |
| **F-13** | Contrats de données ODCS `v3.2.0` et Write-Audit-Publish (données) + contrôle pré-DDL (schéma) | Élevée [S] | Test de gel WAP sur dérive PSI et rejet pré-DDL sur rupture de schéma |
| **F-14** | Confinement du SRE autonome (lecture seule assainie, aucun shell libre, budget Cedar R1/R2 + H0) | **[BLOQUANT]** [S] | Politique Cedar interdisant shell libre et arbitre avec hypothèse nulle H0 |
| **F-15** | Sas anti-PII à canaris et porte pass^5 ≥ 99 % (cible à valider) avant promotion SLM | Conditionnel [S] | Test d’exposition (type Carlini) et jeu de réserve (si distillation LoRA) |
