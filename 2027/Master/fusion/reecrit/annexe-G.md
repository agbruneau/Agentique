# Annexe G — Listes de contrôle d'homologation avant production (75 points)

Aucun système multi-agents de niveau L2, L3 ou L4 n’est autorisé à traiter des données réelles ni à invoquer des outils mutatifs avant d’avoir réussi une revue d’homologation opérationnelle (*Production Readiness Review*, PRR). L’annexe fournit pour cette revue une grille normative de soixante-quinze points de contrôle vérifiables, répartis en cinq domaines de quinze points. Les équipes Architecture, Cybersécurité, SRE/AgentOps et Conformité peuvent l’utiliser directement.

:::: {.encadre .important}
::: {.encadre-titre}
**Important**
:::

**Règle d’homologation.** Pour les systèmes classés L3 et L4, les points marqués \[BLOQUANT\] n’admettent aucune dérogation temporaire en production. Tout constat non conforme impose le maintien du système au niveau L1 (lecture seule consultative) ou en mode fantôme non mutatif, jusqu’à remédiation prouvée.
::::

------------------------------------------------------------------------

## G.1 Grille 1 — Identité non humaine (NHI), sécurité à confiance zéro et isolation (15 points)

| \# | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
|:----------|:---------------------------------------|:--------------|:-----------------------------------|
| **S-01** | Identité NHI unique inscrite à l’annuaire d’entreprise (aucune clé API partagée) | **\[BLOQUANT\]** | Entrée du registre d’agents et manifeste SPIFFE ID / Entra Agent ID |
| **S-02** | Attestation cryptographique de la provenance du code et de la configuration système | Élevée | Signature Sigstore/cosign vérifiée au démarrage du pod |
| **S-03** | Délégation OAuth 2.1 On-Behalf-Of (RFC 8693) préservant `sub` et la chaîne `act` | **\[BLOQUANT\]** | Capture d’un jeton JWT décodé en pré-production |
| **S-04** | Atténuation de portée à chaque saut inter-agents | **\[BLOQUANT\]** | Test automatisé prouvant le rejet d’un appel hors de la portée immédiate |
| **S-05** | Durée de vie courte des jetons (≤ 15 min) et contrainte au détenteur (DPoP/mTLS) | Élevée | Configuration du serveur d’autorisation et test de rejeu négatif |
| **S-06** | Séparation entre l’agent d’interface exposé et l’agent détenteur d’outils d’écriture | **\[BLOQUANT\]** | Diagramme de flux réseau et politique d’accès agentgateway |
| **S-07** | Épinglage cryptographique (empreinte SHA-256) des descriptions et schémas MCP | **\[BLOQUANT\]** | Fichier `mcp-lockfile.yaml` signé et alerte sur modification distante (*rug pull*) |
| **S-08** | Marquage structurel des données externes non fiables contre l’injection indirecte (ASI01) | **\[BLOQUANT\]** | Rapport de campagne automatisée d’équipe rouge (taux de contournement \< 1 %) |
| **S-09** | Évaluation déterministe hors LLM (Cedar ou OPA) devant chaque appel d’outil mutatif | **\[BLOQUANT\]** | Jeu de règles Cedar/Rego versionné et tests unitaires associés |
| **S-10** | Approbation hors bande asynchrone (CIBA) activée pour les actions à haut risque | Élevée | Démonstration bout en bout de suspension et reprise signée |
| **S-11** | Exécution de tout code ou script dynamique en bac à sable isolé (OpenSandbox/microVM) | **\[BLOQUANT\]** | Spécification d’exécution prouvant l’absence de privilèges hôte et de trafic sortant libre |
| **S-12** | Protection contre l’empoisonnement de la mémoire partagée (ASI06) et validation d’écriture | Élevée | Politique de validation avant insertion dans le graphe mémoire |
| **S-13** | Chiffrement mutuel et intégrité des messages inter-agents (mTLS ou SLIM/MLS) | **\[BLOQUANT\]** | Politique réseau à confiance zéro interdisant tout trafic A2A/MCP en clair |
| **S-14** | Coupe-circuit centralisé du SOC, révoquant jetons et sessions en \< 10 secondes | **\[BLOQUANT\]** | Procès-verbal d’exercice de déclenchement du coupe-circuit en pré-production |
| **S-15** | Validation de la séparation des tâches sur les flux financiers/sensibles | **\[BLOQUANT\]** | Preuve qu’aucun identifiant NHI unique ne peut instruire et approuver seul |

------------------------------------------------------------------------

## G.2 Grille 2 — Résilience, exécution durable et intégrité transactionnelle (15 points)

| \# | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
|:----------|:---------------------------------------|:--------------|:-----------------------------------|
| **R-01** | Inviolabilité des systèmes d’enregistrement (passage exclusif par des API/BAPI métiers validées) | **\[BLOQUANT\]** | Revue des connecteurs MCP confirmant l’absence d’écriture SQL directe |
| **R-02** | Ancrage de tout flux multi-étapes mutatif dans un moteur durable (Temporal/Restate) | **\[BLOQUANT\]** | Code source du workflow distinguant logique déterministe et activités |
| **R-03** | Clé d’idempotence déterministe transmise et honorée sur chaque outil à effet de bord | **\[BLOQUANT\]** | Test d’injection de double envoi prouvant l’absence de doublon métier |
| **R-04** | Compteur dur de sauts restants (`maxRemainingHops`) dans l’enveloppe d’action | **\[BLOQUANT\]** | Test unitaire vérifiant l’arrêt immédiat à l’épuisement du TTL |
| **R-05** | Détection des boucles circulaires inter-plateformes SaaS par vecteur de corrélation | Élevée | Test croisé entre deux orchestrateurs simulant un renvoi mutuel |
| **R-06** | Définition explicite d’une action de compensation Saga ou d’un bail TTL par mutation | **\[BLOQUANT\]** | Matrice des étapes de la saga et test automatisé de retour arrière complet |
| **R-07** | Tampon de pré-engagement (fenêtre de grâce ou approbation) devant toute action irréversible | **\[BLOQUANT\]** | Architecture du connecteur courriel/paiement/publication externe |
| **R-08** | Revalidation des préconditions métiers et des droits IAM au réveil d’une pause longue (T4) | Élevée | Scénario de test simulant une révocation d’accès pendant l’attente |
| **R-09** | Retour d’erreurs structurées et exploitables cognitivement par les serveurs MCP | Moyenne | Catalogue des codes d’erreur d’outils (distinguant transitoire et fatal) |
| **R-10** | Politique de réessai avec recul exponentiel et gigue, hors du LLM | Élevée | Configuration de la passerelle agentgateway et du moteur durable |
| **R-11** | Mode dégradé déterministe documenté en cas d’indisponibilité du fournisseur de modèle | **\[BLOQUANT\]** | Test de bascule multi-fournisseurs ou de routage gracieux vers une file humaine |
| **R-12** | Confinement des agents d’utilisation d’interface graphique (CUA), avec assertions visuelles préalables et postérieures | **\[BLOQUANT\]** | Harnais de sécurité CUA (si applicable; sinon marqué Sans objet) |
| **R-13** | Validation sur jumeau numérique déterministe avant toute consigne vers l’univers OT | **\[BLOQUANT\]** | Rapport de test du sas IT/OT (si applicable; sinon marqué Sans objet) |
| **R-14** | Cloisonnement multilocataire du contexte et des caches d’inférence | **\[BLOQUANT\]** | Test d’étanchéité inter-clients / inter-divisions sous charge concurrente |
| **R-15** | Campagne d’ingénierie du chaos réussie (latence extrême, erreurs HTTP 429/500, JSON tronqué) | Élevée | Rapport d’exécution du harnais de chaos sans corruption d’état |

------------------------------------------------------------------------

## G.3 Grille 3 — Observabilité OpenTelemetry, qualité ADLC et FinOps (15 points)

| \# | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
|:----------|:---------------------------------------|:--------------|:-----------------------------------|
| **O-01** | Émission de traces distribuées conformes aux conventions OpenTelemetry `gen_ai.*` | **\[BLOQUANT\]** | Visualisation d’une trace complète (Saga → A2A → LLM → MCP) |
| **O-02** | Caviardage ou masquage automatique des renseignements personnels (PII) avant export OTel | **\[BLOQUANT\]** | Configuration du processeur de filtrage de l’OpenTelemetry Collector |
| **O-03** | Versionnage SemVer + Intent du code, des instructions, du modèle, des schémas d’outils et des politiques | Élevée | Manifeste de version immuable dans le dépôt Git et le registre |
| **O-04** | Suite de simulation multi-tours représentative (≥ 100 scénarios, dont des cas adversariaux) | **\[BLOQUANT\]** | Dossier de scénarios OpenEnv / type $\tau$-bench versionné |
| **O-05** | Seuil de constance $\text{pass}^k$ atteint ($k \ge 5$) sur les invariants métiers critiques | **\[BLOQUANT\]** | Rapport CI/CD affichant $\text{pass}^5$ au-dessus du seuil fixé dans l’ADR |
| **O-06** | Détection automatique en temps réel des boucles sémantiques (verrouillages actifs répétitifs) | Élevée | Règle d’alerte et d’interruption configurée sur le flux de télémétrie |
| **O-07** | Procédure de déploiement progressif opérationnelle (mode fantôme, puis déploiement canari à 1–5 %) | Élevée | Script de routage pondéré sur agentgateway et critères de retour arrière |
| **O-08** | Retour arrière automatisé en moins de 2 minutes vers la version N-1 stable | **\[BLOQUANT\]** | Journal d’un test de retour arrière déclenché par un seuil d’anomalie simulé |
| **O-09** | Enveloppe budgétaire maximale en devises (`maxTotalCostCad`) active par transaction/saga | **\[BLOQUANT\]** | Test démontrant l’arrêt propre d’une saga dépassant son plafond FinOps |
| **O-10** | Routage cognitif hybride privilégiant les SLM pour les tâches d’extraction et de triage | Moyenne | Répartition mesurée des appels par palier de modèle en pré-production |
| **O-11** | Optimisation et mesure du taux de réutilisation du préfixe / KV-cache inter-tours | Moyenne | Tableau de bord de latence TTFT et ratio de jetons mis en cache |
| **O-12** | Imputation analytique des coûts en temps réel par unité d’affaires, processus et client | **\[BLOQUANT\]** | Étiquettes FinOps présentes sur 100 % des requêtes passées par la passerelle |
| **O-13** | Définition formelle de l’événement métier de succès pour calculer le coût par résultat | Élevée | Formule et requête analytique reliant coût technique et résultat validé |
| **O-14** | Surveillance continue de la dérive sémantique et du taux d’escalade vers les humains | Élevée | Tableau de bord AgentOps hebdomadaire avec seuils d’alerte |
| **O-15** | Protocole de décommissionnement propre (révocation NHI, archivage des traces, redirection) | Moyenne | Procédure d’extinction d’agent validée par l’équipe plateforme |

------------------------------------------------------------------------

## G.4 Grille 4 — Gouvernance, droit, facteur humain et conformité 2027 (15 points)

| \# | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
|:----------|:---------------------------------------|:--------------|:-----------------------------------|
| **G-01** | Propriétaire métier nominatif désigné et signataire | **\[BLOQUANT\]** | Charte de responsabilité signée dans le registre d’agents d’entreprise |
| **G-02** | Inscription au système de management de l’IA conforme à ISO/IEC 42001 | Élevée | Fiche d’impact, analyse de risques et calendrier de revue PDCA |
| **G-03** | Qualification réglementaire de l’empreinte de déploiement | **\[BLOQUANT\]** | Grille juridique qualifiant tous les systèmes aval connectés |
| **G-04** | Conformité BSIF/OSFI E-23 (si institution financière fédérale canadienne, échéance au 1er mai 2027) | **\[BLOQUANT\]** | Cote de matérialité, rapport de validation indépendante et suivi des tiers |
| **G-05** | Évaluation des facteurs relatifs à la vie privée (ÉFVP) approuvée (Loi 25 / RGPD) | **\[BLOQUANT\]** | Dossier ÉFVP signé, avec la cartographie des flux transfrontaliers |
| **G-06** | Mécanisme d’information, d’explication et de révision humaine (Loi 25 art. 12.1) | **\[BLOQUANT\]** | Parcours client/employé testé lorsqu’une décision affecte un individu |
| **G-07** | Divulgation de l’interaction avec une IA (EU AI Act art. 50, actif août 2026) | **\[BLOQUANT\]** | Mention explicite dans les interfaces conversationnelles et vocales, et dans les courriels |
| **G-08** | Dossier technique et supervision humaine renforcée si haut risque (EU AI Act Annexe III) | **\[BLOQUANT\]** | Documentation technique conforme avant l’échéance de décembre 2027 |
| **G-09** | Alignement sémantique des concepts métiers critiques sur le standard Apache Ossie | Élevée | Validation par l’équipe Données de l’absence de définitions ad hoc |
| **G-10** | Droit à l’effacement et purge sélective vérifiable dans la mémoire à long terme | **\[BLOQUANT\]** | Test d’oubli d’une entité cliente sans dégradation résiduelle |
| **G-11** | Ergonomie HOTL présentant les preuves contradictoires (prévention du biais ASI09) | Élevée | Revue UX de l’écran A2UI d’approbation (absence d’incitation biaisée) |
| **G-12** | Dispositif périodique de maintien de vigilance des superviseurs humains (HOTL) | Moyenne | Programme de dossiers tests d’étalonnage et suivi du temps de revue |
| **G-13** | Plafonds juridiques et mandats AP2 signés pour toute transaction commerciale B2B | **\[BLOQUANT\]** | Politique de délégation de signature financière et mandats SD-JWT |
| **G-14** | Garde-fous explicites anti-collusion algorithmique sur les agents de prix ou d’enchères | **\[BLOQUANT\]** | Audit des consignes d’optimisation et des journaux de négociation |
| **G-15** | Archivage immuable et horodaté (WORM) des décisions critiques pour opposabilité légale | **\[BLOQUANT\]** | Politique de rétention conforme aux délais de prescription légaux |

------------------------------------------------------------------------

## G.5 Grille 5 — Fédération B2B, souveraineté cognitive, périphérie et usine interne (15 points)

| \# | Point de contrôle | Criticité | Artefact de preuve exigé à la revue d’homologation |
|:----------|:---------------------------------------|:--------------|:-----------------------------------|
| **F-01** | Authentification légale vLEI avec rôle OOR et contrat d’usage ODRL 2.2 sur tout canal B2B | **\[BLOQUANT\]** | Accord `ContractAgreement` du connecteur EDC et test de rejet d’un pair non signé |
| **F-02** | Scission physique entre l’agent diplomate B2B et l’évaluateur interne (aucun secret en DMZ) | **\[BLOQUANT\]** | Revue d’architecture et rapport d’équipe rouge sur l’extraction de prix de réserve |
| **F-03** | Rapprochement tripartite déterministe (Cedar) exigé avant toute libération AP2 / x402 | **\[BLOQUANT\]** | Test unitaire et d’intégration couvrant écart de poids, SKU, prix et signature IoT |
| **F-04** | Résidence juridictionnelle vérifiée des 6 couches d’état (dont KV-cache et Temporal) | **\[BLOQUANT\]** | Matrice de géorepérage signée pour les classes C2 (Loi 25) et C3 (E-23) |
| **F-05** | Clés de chiffrement d’état et de pseudonymisation détenues localement (HYOK en HSM) | Élevée | Preuve de révocation d’accès HSM rendant illisibles les journaux infonuagiques |
| **F-06** | Attestation matérielle distante CPU+GPU (TEE) validée avant déchiffrement de charge C3 | **\[BLOQUANT\]** | Politique du vérificateur d’attestation épinglant les registres PCR approuvés |
| **F-07** | Profil de secours à poids ouverts (reprise cognitive) homologué et testé (`RTO < 15 min`) | **\[BLOQUANT\]** | Procès-verbal du dernier exercice trimestriel de coupure du fournisseur primaire |
| **F-08** | Survie autonome en périphérie ≥ 72 h (SPIRE/TPM local, SLM embarqué) et baux d’époque CRDT | Élevée | Rapport d’essai avec câble WAN débranché, fusion sans conflit ni double dépense |
| **F-09** | Enveloppe matérielle Simplex (`ISO 10218-1:2025` / IEC 61508) isolant tout pont MCP ↔︎ ROS 2 | **\[BLOQUANT\]** | Certificat d’homologation de sécurité machine (si robotique; sinon Sans objet) |
| **F-10** | Distribution signée TUF/Sigstore à double clé des lots déployés en périphérie, avec bascule A/B | **\[BLOQUANT\]** | Test d’injection d’archive altérée ou expirée bloquée au démarrage |
| **F-11** | Séparation des devoirs dans l’usine logicielle agentique (bâtisseur interdit d’écriture sur les tests d’or) | **\[BLOQUANT\]** | Règles de protection du dépôt Git et confinement réseau du bac de compilation |
| **F-12** | Porte de mutation (≥ 85 %) et parité en exécution miroir sur 30 jours pour le module modernisé | **\[BLOQUANT\]** | Rapport du comparateur de l’exécution miroir : 0,00 \$ CAD d’écart sur ≥ 100 000 transactions |
| **F-13** | Contrats de données ODCS v3 selon le patron Write-Audit-Publish devant tout lac alimentant des agents | Élevée | Test de gel automatique de branche Nessie sur injection de dérive d’unité ou PSI |
| **F-14** | Confinement du SRE autonome (lecture seule assainie, aucun interpréteur de commandes libre, budget Cedar R1/R2) | **\[BLOQUANT\]** | Politique Cedar interdisant `kubectl exec`/SSH, avec protection contre l’injection dans les journaux et CIBA sur R3 |
| **F-15** | Sas anti-PII à canaris et porte de parité $\text{pass}^5 \ge 99\,\%$ avant promotion d’un SLM distillé | **\[BLOQUANT\]** | Audit d’exposition de Carlini (Loi 25), cadre PCCP (E-23) et score scellé sur jeu de réserve |
