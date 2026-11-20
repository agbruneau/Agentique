# D Registre des exigences

Ce registre récapitule, dans l’ordre du document, toutes les exigences normatives du cadre avec la force de leur bloc (DOIT, NE DOIT PAS, DEVRAIT), soit 305 exigences dans la version 1.2 (287 dans la version 1.1, augmentées des 12 exigences EXIG-AMF et de 6 exigences explicites PQC NIST IR 8547, ACVM 11-348, RTR/ISO 20022 et EN 18286:2026 : 255 DOIT, 34 NE DOIT PAS et 16 DEVRAIT). Les principes PRIN-01 à PRIN-12 et les tableaux auxquels une exigence renvoie expressément sont aussi normatifs (section 1.4), mais ne figurent pas au registre. Chaque identifiant renvoie à l’exigence complète, avec son énoncé et sa justification. Le registre sert de base aux revues d’architecture, à la grille d’homologation (annexe A) et à la déclaration d’applicabilité ISO/IEC 42001; sa forme structurée est exportée dans `exigences.json`.

| **Identifiant** | **Force** | **Exigence** |
| --- | --- | --- |
| `EXIG-ARC-01` | **DOIT** | Passage obligatoire par la passerelle et le catalogue |
| `EXIG-ARC-02` | **DOIT** | Mandant, trace et plafonds dans chaque appel |
| `EXIG-ARC-03` | **NE DOIT PAS** | Aucune logique d’agent dans les canaux |
| `EXIG-ARC-04` | **DOIT** | Mandant établi et trace ouverte à l’entrée |
| `EXIG-ARC-05` | **DOIT** | Exécution durable des tâches à effets |
| `EXIG-ARC-06` | **DOIT** | Points de contrôle protégés comme des données de production |
| `EXIG-ARC-07` | **NE DOIT PAS** | Le routage n’accorde aucun droit |
| `EXIG-ARC-08` | **DOIT** | Passerelle de modèles obligatoire |
| `EXIG-ARC-09` | **DEVRAIT** | Modèles désignés par un alias logique |
| `EXIG-ARC-10` | **DOIT** | Code généré exécuté en bac à sable |
| `EXIG-ARC-11` | **DOIT** | Passerelle d’agents dans les deux sens |
| `EXIG-ARC-12` | **DOIT** | Liste d’autorisation tirée du catalogue |
| `EXIG-ARC-13` | **DOIT** | Aucun contournement par le bus d’événements |
| `EXIG-ARC-14` | **DOIT** | Exposition sans réécriture des services |
| `EXIG-ARC-15` | **DEVRAIT** | Outils conçus pour la tâche |
| `EXIG-ARC-16` | **DOIT** | Résultats filtrés selon les droits du mandant |
| `EXIG-ARC-17` | **DOIT** | Écriture par les interfaces qui appliquent les règles métier |
| `EXIG-ARC-18` | **DEVRAIT** | Référence de trace sur chaque écriture |
| `EXIG-ARC-19` | **DOIT** | Services transversaux mutualisés |
| `EXIG-ARC-20` | **DOIT** | Correspondance ABB-SBB documentée |
| `EXIG-ARC-21` | **DOIT** | SBB exposés par les standards retenus |
| `EXIG-ARC-22` | **NE DOIT PAS** | Pas d’historique brut comme mémoire |
| `EXIG-ARC-23` | **DOIT** | Contrôles avant toute écriture en mémoire épisodique ou sémantique |
| `EXIG-ARC-24` | **DOIT** | Mémoire procédurale gérée comme du code |
| `EXIG-ARC-25` | **NE DOIT PAS** | Aucun magasin de mémoire longue partagé en écriture |
| `EXIG-INT-01` | **DOIT** | Revue d’interopérabilité proportionnée |
| `EXIG-INT-02` | **DOIT** | Vocabulaire et schémas d’entreprise |
| `EXIG-INT-03` | **DOIT** | Accord d’interopérabilité et gestion du changement |
| `EXIG-INT-04` | **DOIT** | Protocole désigné par type d’interaction |
| `EXIG-INT-05` | **DEVRAIT** | Agent pair invoqué par A2A, pas déguisé en outil |
| `EXIG-INT-06` | **DOIT** | Statut au catalogue avant tout usage en production |
| `EXIG-INT-07` | **DOIT** | Version de référence fixée au catalogue |
| `EXIG-INT-08` | **DOIT** | Révision trimestrielle du catalogue des protocoles |
| `EXIG-INT-09` | **NE DOIT PAS** | Brouillon présenté comme une norme publiée |
| `EXIG-INT-10` | **DOIT** | Choix de protocole justifié par la matrice |
| `EXIG-INT-11` | **DEVRAIT** | Diffusion d’un changement d’état par événement |
| `EXIG-MCP-01` | **DOIT** | Exposition des capacités par MCP, derrière la passerelle |
| `EXIG-MCP-02` | **DOIT** | Révision de référence vérifiée par la découverte |
| `EXIG-MCP-03` | **DOIT** | Listes stables et cache conforme à cacheScope |
| `EXIG-MCP-04` | **DOIT** | Extensions activées sur liste d’autorisation |
| `EXIG-MCP-05` | **DEVRAIT** | Choix de la primitive selon le besoin |
| `EXIG-MCP-06` | **NE DOIT PAS** | Aucun miroir CRUD des API |
| `EXIG-MCP-07` | **DOIT** | Conventions de nommage et de résultat des outils |
| `EXIG-MCP-08` | **DOIT** | Transport selon l’environnement |
| `EXIG-MCP-09` | **DOIT** | Autorisation obligatoire et conforme à la spécification |
| `EXIG-MCP-10` | **DOIT** | Portées minimales et élévation progressive |
| `EXIG-MCP-11` | **NE DOIT PAS** | Interdiction du passage de jeton |
| `EXIG-MCP-12` | **DOIT** | Enregistrement des clients MCP |
| `EXIG-MCP-13` | **DOIT** | Consentement par client des mandataires MCP |
| `EXIG-MCP-14` | **DOIT** | Annotations et métadonnées déclarées : de simples indices |
| `EXIG-MCP-15` | **DOIT** | Concordance des en-têtes et du corps |
| `EXIG-MCP-16` | **DOIT** | Traitement du champ _meta |
| `EXIG-MCP-17` | **DOIT** | État explicite protégé |
| `EXIG-MCP-18` | **NE DOIT PAS** | Aucune donnée sensible en en-tête |
| `EXIG-MCP-19` | **DOIT** | Schémas, URL et icônes : des entrées non fiables |
| `EXIG-MCP-20` | **DOIT** | Empreintes des définitions et isolement des serveurs |
| `EXIG-MCP-21` | **NE DOIT PAS** | Élicitation : ni secret ni approbation déguisée |
| `EXIG-MCP-22` | **DOIT** | Migration bornée et abandon des fonctions dépréciées |
| `EXIG-A2A-01` | **DOIT** | A2A 1.0 pour toute délégation entre agents |
| `EXIG-A2A-02` | **DOIT** | Carte publiée et inscrite au catalogue |
| `EXIG-A2A-03` | **DOIT** | Carte signée et vérifiée |
| `EXIG-A2A-04` | **DOIT** | Version de carte et revalidation du cache |
| `EXIG-A2A-05` | **NE DOIT PAS** | Aucun champ hors norme dans la carte |
| `EXIG-A2A-06` | **DOIT** | Compétences internes dans la carte étendue |
| `EXIG-A2A-07` | **DOIT** | Suivi des tâches longues |
| `EXIG-A2A-08` | **DOIT** | Version annoncée et liaisons standard |
| `EXIG-A2A-09` | **DOIT** | Transport chiffré et authentification à chaque requête |
| `EXIG-A2A-10` | **DOIT** | Autorisation par compétence et par locataire |
| `EXIG-A2A-11` | **NE DOIT PAS** | Flux OAuth permis et flux retirés |
| `EXIG-A2A-12` | **DOIT** | Notifications push durcies |
| `EXIG-A2A-13` | **DOIT** | Traçage et corrélation des tâches |
| `EXIG-A2A-14` | **DOIT** | Compatibilité vérifiée avant inscription |
| `EXIG-A2A-15` | **DEVRAIT** | Migration bornée depuis la version 0.3 |
| `EXIG-EVT-01` | **DEVRAIT** | Recours au bus pour l’asynchrone |
| `EXIG-EVT-02` | **DOIT** | Enveloppe CloudEvents complète |
| `EXIG-EVT-03` | **DOIT** | Contrat AsyncAPI au catalogue |
| `EXIG-EVT-04` | **DOIT** | Attributs de gouvernance présents et vérifiés |
| `EXIG-EVT-05` | **NE DOIT PAS** | Aucun renseignement personnel direct dans les attributs |
| `EXIG-EVT-06` | **DOIT** | Compteur de sauts et coupure des boucles |
| `EXIG-EVT-07` | **DOIT** | Autorisation fondée sur l’identité, pas sur les attributs |
| `EXIG-EVT-08` | **DOIT** | Effets réels protégés par l’idempotence |
| `EXIG-EVT-09` | **DOIT** | Ordre garanti par la clé de partition |
| `EXIG-EVT-10` | **DOIT** | Conservation des entrées et rejeu isolé |
| `EXIG-INT-12` | **DOIT** | Contrat complet avant l’inscription |
| `EXIG-INT-13` | **DOIT** | Versionnage sémantique des contrats |
| `EXIG-INT-14` | **DOIT** | Coexistence d’au moins 60 jours |
| `EXIG-INT-15` | **DOIT** | Dépendances épinglées par version et empreinte |
| `EXIG-INT-16` | **DOIT** | Nouvelle approbation à toute modification |
| `EXIG-INT-17` | **DOIT** | Catalogue unique, source de la découverte |
| `EXIG-INT-18` | **DOIT** | Consommateurs connus avant tout retrait |
| `EXIG-INT-19` | **DOIT** | Détection automatique des ruptures |
| `EXIG-INT-20` | **NE DOIT PAS** | Qualification « AAIF » non vérifiée |
| `EXIG-INT-21` | **DOIT** | Pilotes AGNTCY subordonnés au catalogue |
| `EXIG-INT-22` | **DOIT** | Paiements initiés par un agent |
| `EXIG-INT-23` | **DOIT** | Signal de révision inscrit au catalogue |
| `EXIG-ORC-01` | **DOIT** | Configuration la plus simple justifiée |
| `EXIG-ORC-02` | **DOIT** | Preuve mesurée avant le multiagent |
| `EXIG-ORC-03` | **DOIT** | Patron déclaré au registre |
| `EXIG-ORC-04` | **NE DOIT PAS** | Délégation limitée à deux niveaux |
| `EXIG-ORC-05` | **DOIT** | Boucle évaluateur-optimiseur bornée |
| `EXIG-ORC-06` | **DOIT** | Clavardage de groupe encadré |
| `EXIG-ORC-07` | **DOIT** | Fusion déclarée et écrivain unique en parallèle |
| `EXIG-ORC-08` | **DOIT** | Chorégraphie sous propriétaire et saga |
| `EXIG-ORC-09` | **DOIT** | Surcharge d’outils traitée avant de scinder |
| `EXIG-ORC-10` | **DEVRAIT** | Découpage par frontières de contexte |
| `EXIG-ORC-11` | **DOIT** | Persistance après chaque transition |
| `EXIG-ORC-12` | **DOIT** | Reprise sans double effet |
| `EXIG-ORC-13` | **DOIT** | Magasin de points de contrôle protégé |
| `EXIG-ORC-14` | **DEVRAIT** | Déploiement sans interruption des exécutions longues |
| `EXIG-ORC-15` | **DOIT** | Saga pour toute écriture multisystème |
| `EXIG-ORC-16` | **DOIT** | Journal de compensation tenu avant l’action |
| `EXIG-ORC-17` | **DOIT** | Compensations idempotentes et métier, après réessais |
| `EXIG-ORC-18` | **DOIT** | Escalade après deux échecs d’une compensation |
| `EXIG-ORC-19` | **DOIT** | Isolation sémantique des sagas concurrentes |
| `EXIG-ORC-20` | **DOIT** | Tests d’injection de fautes des sagas |
| `EXIG-ORC-21` | **DOIT** | Clé d’idempotence sur toute écriture |
| `EXIG-ORC-22` | **DOIT** | Vérification de la clé par le service visé |
| `EXIG-ORC-23` | **DOIT** | Contexte de délégation minimal et structuré |
| `EXIG-ORC-24` | **DOIT** | Retour validé avant toute réutilisation |
| `EXIG-ORC-25` | **DOIT** | Filtrage de sécurité dans chaque agent |
| `EXIG-ORC-26` | **DOIT** | Plafonds sur toute exécution |
| `EXIG-ORC-27` | **DOIT** | Mécanismes de résilience et repli testé |
| `EXIG-ORC-28` | **DOIT** | Coupe-circuit exercé chaque trimestre |
| `EXIG-ORC-29` | **NE DOIT PAS** | Aucun anti-patron sans dérogation |
| `EXIG-ORC-30` | **DOIT** | Capacités démontrées avant l’inscription d’un produit |
| `EXIG-AUT-01` | **DOIT** | Niveau d’autonomie déclaré et appliqué |
| `EXIG-AUT-02` | **DOIT** | Plafond selon la classe de risque |
| `EXIG-AUT-03` | **NE DOIT PAS** | Autonomie non bornée interdite (NX) |
| `EXIG-AUT-04` | **DOIT** | Domaine de conception opérationnel (ODD), repli et arrêts pour N3 et N4 |
| `EXIG-AUT-05` | **DOIT** | Homologation et réévaluation du niveau |
| `EXIG-AUT-06` | **DOIT** | Classement fondé sur les permissions effectives |
| `EXIG-AUT-07` | **NE DOIT PAS** | Règle d’or : pas d’exécution autonome du risque cumulé |
| `EXIG-AUT-08` | **DOIT** | Palier attribué au catalogue après revue |
| `EXIG-AUT-09` | **NE DOIT PAS** | Aucun outil P3 exécuté seul |
| `EXIG-AUT-10` | **DOIT** | Contrôle calculé à chaque appel |
| `EXIG-AUT-11` | **DOIT** | Échec en mode fermé |
| `EXIG-AUT-12` | **DOIT** | Jeton d’approbation lié à l’action exacte |
| `EXIG-AUT-13` | **NE DOIT PAS** | Ce qui n’est jamais une approbation |
| `EXIG-AUT-14` | **DEVRAIT** | Approbation hors bande normalisée |
| `EXIG-AUT-15` | **DOIT** | Approbateurs habilités et formés |
| `EXIG-AUT-16` | **DOIT** | Boîte de réception persistante |
| `EXIG-AUT-17` | **DOIT** | État persisté et effets après le point d’approbation |
| `EXIG-AUT-18` | **DOIT** | Réautorisation périodique des agents ambiants |
| `EXIG-AUT-19` | **DOIT** | Écran d’approbation fidèle à l’action |
| `EXIG-AUT-20` | **DOIT** | Charge d’approbation maîtrisée |
| `EXIG-AUT-21` | **DOIT** | Mesure de la qualité de la supervision |
| `EXIG-AUT-22` | **DOIT** | Décisions visées par l’article 12.1 |
| `EXIG-AUT-23` | **DOIT** | Révision humaine significative |
| `EXIG-IAM-01` | **NE DOIT PAS** | Aucune confiance implicite |
| `EXIG-IAM-02` | **DOIT** | Une décision à chaque appel |
| `EXIG-IAM-03` | **DOIT** | Identité propre, distincte et non partagée |
| `EXIG-IAM-04` | **DOIT** | Justificatif cryptographique émis par la plateforme |
| `EXIG-IAM-05` | **NE DOIT PAS** | Aucun secret statique |
| `EXIG-IAM-06` | **NE DOIT PAS** | Justificatifs hors de portée du modèle |
| `EXIG-IAM-07` | **DOIT** | Révocation au retrait et revues périodiques |
| `EXIG-IAM-08` | **DOIT** | Délégation explicite par échange de jetons |
| `EXIG-IAM-09` | **NE DOIT PAS** | Interdiction de l’usurpation |
| `EXIG-IAM-10` | **DOIT** | Portée jamais élargie |
| `EXIG-IAM-11` | **DOIT** | Jeton à audience unique, validé par la cible |
| `EXIG-IAM-12` | **NE DOIT PAS** | Aucun relais de jeton |
| `EXIG-IAM-13` | **DOIT** | Profil OAuth de l’entreprise |
| `EXIG-IAM-14` | **DOIT** | Jetons liés à l’expéditeur |
| `EXIG-IAM-15` | **DEVRAIT** | Durée de vie courte des jetons |
| `EXIG-IAM-16` | **DOIT** | Agents autonomes : identifiants du client et portées par outil |
| `EXIG-IAM-17` | **DOIT** | Passage obligatoire par la passerelle d’agents |
| `EXIG-IAM-18` | **DOIT** | Échec en mode fermé et refus typé |
| `EXIG-IAM-19` | **DEVRAIT** | Justificatifs en aval injectés par la passerelle |
| `EXIG-IAM-20` | **DOIT** | Coupe-circuit propagé et mesuré |
| `EXIG-IAM-21` | **DOIT** | Politique en code, versionnée et testée |
| `EXIG-SEC-01` | **DOIT** | Modélisation des menaces avant la production |
| `EXIG-SEC-02` | **DOIT** | Matrice de traçabilité des menaces |
| `EXIG-SEC-03` | **DOIT** | Présomption d’injection |
| `EXIG-SEC-04` | **DOIT** | Règle de deux par session |
| `EXIG-SEC-05` | **NE DOIT PAS** | Détection comme seul contrôle |
| `EXIG-SEC-06` | **DOIT** | Retrait déterministe des capacités d’exfiltration |
| `EXIG-SEC-07` | **DOIT** | Patron de conception pour les agents de risque élevé |
| `EXIG-SEC-08` | **DOIT** | Technologie d’isolation du code non fiable |
| `EXIG-SEC-09` | **DOIT** | Bac à sable éphémère et minimal |
| `EXIG-SEC-10` | **DOIT** | Charges qui exigent un GPU |
| `EXIG-SEC-11` | **DEVRAIT** | Performance mesurée sur la charge réelle |
| `EXIG-SEC-12` | **DOIT** | Sortie réseau refusée par défaut |
| `EXIG-SEC-13` | **DOIT** | Service de métadonnées infonuagiques |
| `EXIG-SEC-14` | **NE DOIT PAS** | Secret dans le bac à sable plutôt qu’injecté par le mandataire |
| `EXIG-SEC-15` | **DOIT** | Délais à trois niveaux |
| `EXIG-SEC-16` | **DOIT** | Journal d’exécution tenu hors du bac à sable |
| `EXIG-SEC-17` | **DOIT** | Porte de validation du code généré |
| `EXIG-SEC-18` | **DOIT** | Provenance approuvée et intégrité vérifiée à l’exécution |
| `EXIG-SEC-19` | **DOIT** | Signature des cartes d’agent et des artefacts |
| `EXIG-SEC-20` | **DOIT** | Nomenclature de chaque version d’agent |
| `EXIG-SEC-21` | **DOIT** | Chaque serveur, un domaine de sécurité distinct |
| `EXIG-SEC-22` | **DOIT** | Évaluation des tiers et plan de contingence |
| `EXIG-SEC-23` | **DOIT** | Exercice d’équipe rouge propre aux agents |
| `EXIG-SEC-24` | **DOIT** | Suite d’attaques dans la chaîne d’intégration |
| `EXIG-SEC-25` | **DOIT** | Vérification des contrôles déterministes |
| `EXIG-SEC-26` | **DOIT** | Exercice trimestriel de compromission d’agent |
| `EXIG-SEC-27` | **DOIT** | Agilité cryptographique et inventaire post-quantique (NIST IR 8547) |
| `EXIG-SEC-28` | **DOIT** | Rescellement et signatures post-quantiques des artefacts à probité longue |
| `EXIG-OBS-01` | **DOIT** | OpenTelemetry obligatoire, conventions épinglées |
| `EXIG-OBS-02` | **DOIT** | Contexte validé, poursuivi ou redémarré aux frontières |
| `EXIG-OBS-03` | **DOIT** | Identifiants métier portés à part |
| `EXIG-OBS-04` | **DOIT** | Hiérarchie de spans normalisée |
| `EXIG-OBS-05` | **DOIT** | Attributs et métriques exigés |
| `EXIG-OBS-06` | **DOIT** | Attributs d’entreprise sous préfixe DNS inversé |
| `EXIG-OBS-07` | **NE DOIT PAS** | Aucun contenu dans la télémétrie de production |
| `EXIG-OBS-08` | **DOIT** | Contenu de débogage hors trace et de courte durée |
| `EXIG-OBS-09` | **DOIT** | Caviardage à la sortie du périmètre |
| `EXIG-OBS-10` | **NE DOIT PAS** | Aucun renseignement personnel dans le bagage |
| `EXIG-OBS-11` | **DOIT** | Journal d’audit distinct et exhaustif |
| `EXIG-OBS-12` | **DOIT** | Enregistrement à cinq éléments, canonisé et signé |
| `EXIG-OBS-13` | **DOIT** | Inaltérabilité et conservation |
| `EXIG-EVA-01` | **DOIT** | Étages franchis et relancés à chaque changement |
| `EXIG-EVA-02` | **DOIT** | Jeu de référence tenu et versionné |
| `EXIG-EVA-03` | **DOIT** | Évaluations répétées et isolées |
| `EXIG-EVA-04` | **DOIT** | Échantillonnage de la production |
| `EXIG-EVA-05` | **DOIT** | Juge automatisé encadré |
| `EXIG-EVA-06` | **DOIT** | Objectifs de niveau de service et réaction aux écarts |
| `EXIG-FIN-01` | **DOIT** | Comparaison au coût par tâche réussie |
| `EXIG-FIN-02` | **DOIT** | Hypothèses de prix datées et révisées |
| `EXIG-FIN-03` | **DOIT** | Unités SaaS converties et plafonnées |
| `EXIG-FIN-04` | **DOIT** | Enveloppe appliquée à chaque étape |
| `EXIG-FIN-05` | **DOIT** | Quotas et plafond mensuel par agent |
| `EXIG-FIN-06` | **DOIT** | Plus petit modèle suffisant |
| `EXIG-FIN-07` | **DOIT** | Préfixe stable et cache mesuré |
| `EXIG-FIN-08` | **DEVRAIT** | Lots asynchrones pour les charges non urgentes |
| `EXIG-FIN-09` | **DOIT** | Imputation par centre de coûts |
| `EXIG-FIN-10` | **DOIT** | Indicateurs d’économie unitaire publiés |
| `EXIG-GOV-01` | **DOIT** | Responsables nommés pour chaque agent |
| `EXIG-GOV-02` | **DOIT** | Comité d’architecture et des risques agentiques |
| `EXIG-GOV-03` | **NE DOIT PAS** | Cumul de la préparation et de l’approbation |
| `EXIG-GOV-04` | **DOIT** | Un seul A, des personnes nommées |
| `EXIG-GOV-05` | **DOIT** | Socle commun obligatoire |
| `EXIG-GOV-06` | **DEVRAIT** | Conformité par construction |
| `EXIG-GOV-07` | **DOIT** | Inventaire complet |
| `EXIG-GOV-08` | **NE DOIT PAS** | Sans fiche, aucun justificatif |
| `EXIG-GOV-09` | **DOIT** | Fiche à jour ou agent suspendu |
| `EXIG-GOV-10` | **DOIT** | Détection des agents hors registre |
| `EXIG-GOV-11` | **DOIT** | Jalons du cycle de vie consignés |
| `EXIG-GOV-12` | **DOIT** | Réévaluation sur changement significatif |
| `EXIG-GOV-13` | **DOIT** | Attestation périodique du parrain |
| `EXIG-GOV-14` | **DOIT** | Retrait vérifiable |
| `EXIG-GOV-15` | **DOIT** | Demande et décision écrites |
| `EXIG-GOV-16` | **DOIT** | Durée bornée |
| `EXIG-GOV-17` | **NE DOIT PAS** | Dérogation à une exigence non dérogeable |
| `EXIG-GOV-18` | **DOIT** | Révision trimestrielle du catalogue |
| `EXIG-GOV-19` | **DOIT** | Critères d’admission d’un standard |
| `EXIG-GOV-20` | **DOIT** | Veille désignée et usage encadré |
| `EXIG-CON-01` | **DOIT** | Classe de risque attribuée avant l’inscription |
| `EXIG-CON-02` | **DOIT** | Plafond d’autonomie par classe |
| `EXIG-CON-03` | **DOIT** | Réévaluation à chaque changement significatif |
| `EXIG-CON-04` | **DOIT** | EFVP avant tout projet d’agent impliquant des RP |
| `EXIG-CON-05` | **DOIT** | Cartographie des lieux de traitement |
| `EXIG-CON-06` | **DOIT** | Finalité vérifiée avant toute réutilisation |
| `EXIG-CON-07` | **DOIT** | Avis et explication des décisions automatisées |
| `EXIG-CON-08` | **NE DOIT PAS** | Aucune approbation nominale |
| `EXIG-CON-09` | **DOIT** | Conservation des éléments de décision |
| `EXIG-CON-10` | **DOIT** | Durée de vie des mémoires et des traces |
| `EXIG-CON-11` | **DOIT** | Régimes applicables inscrits à la fiche |
| `EXIG-CON-12` | **DOIT** | Arrimage à E-23 pour les institutions financières fédérales |
| `EXIG-CON-13` | **DOIT** | Applicabilité du RIA déterminée par l’usage des sorties |
| `EXIG-CON-14` | **NE DOIT PAS** | Aucun usage interdit |
| `EXIG-CON-15` | **DOIT** | Revue de requalification en fournisseur |
| `EXIG-CON-16` | **DOIT** | Obligations du déployeur d’un agent à haut risque |
| `EXIG-CON-17` | **DOIT** | Déclaration de tolérance au risque |
| `EXIG-CON-18` | **DOIT** | Base de preuves unique |
| `EXIG-CON-19` | **DOIT** | Divulgation de l’interaction avec un agent |
| `EXIG-CON-20` | **DOIT** | Identification des contenus produits par un agent |
| `EXIG-CON-21` | **DOIT** | Explication intelligible et canal de révision |
| `EXIG-CON-22` | **DOIT** | Vérification humaine du contenu juridique |
| `EXIG-CON-23` | **DOIT** | Réponse en cinq temps et gel des preuves |
| `EXIG-CON-24` | **DOIT** | Registre et avis des incidents de confidentialité |
| `EXIG-CON-25` | **DOIT** | Règle la plus exigeante entre régimes de notification |
| `EXIG-CON-26` | **DOIT** | Évaluation d’impact unifiée par agent de classe élevée |
| `EXIG-CON-27` | **DOIT** | Gouvernance IA en valeurs mobilières et convenance rattachée à une personne inscrite (ACVM 11-348) |
| `EXIG-CON-28` | **DOIT** | Véracité des déclarations d’IA et interdiction de l’AI washing (ACVM 11-348) |
| `EXIG-CON-29` | **DOIT** | Tampon déterministe et validation ISO 20022 sur le Rail en temps réel (RTR) |
| `EXIG-CON-30` | **DOIT** | Système de management de la qualité harmonisé pour agents à haut risque (EN 18286:2026) |
| `EXIG-AMF-01` | **DOIT** | Membre de la haute direction imputable |
| `EXIG-AMF-02` | **DOIT** | Information du conseil d’administration |
| `EXIG-AMF-03` | **DOIT** | Compétences par population |
| `EXIG-AMF-04` | **DOIT** | Éthique applicable aux agents |
| `EXIG-AMF-05` | **DOIT** | Arrimage à la gestion du risque de modèle de l’AMF |
| `EXIG-AMF-06` | **DOIT** | Registre aligné sur le répertoire centralisé |
| `EXIG-AMF-07` | **DOIT** | Facteurs de la classe et primauté des contraintes |
| `EXIG-AMF-08` | **DOIT** | Registre institutionnel des risques agentiques |
| `EXIG-AMF-09` | **DOIT** | Validation fondée sur les familles de risque de l’AMF |
| `EXIG-AMF-10` | **DOIT** | Données d’apprentissage et calibrage dynamique |
| `EXIG-AMF-11` | **DOIT** | Preuves d’équité |
| `EXIG-AMF-12` | **DOIT** | Communication au client |
| `EXIG-APP-01` | **DOIT** | Analyse de réversibilité avant tout engagement |
| `EXIG-APP-02` | **NE DOIT PAS** | Aucune dépendance à une extension non approuvée |
| `EXIG-APP-03` | **DOIT** | Preuves de conformité protocolaire |
| `EXIG-APP-04` | **DOIT** | Mesures de performance reproductibles |
| `EXIG-APP-05` | **DOIT** | Télémétrie et données de coûts ouvertes |
| `EXIG-APP-06` | **DOIT** | Identité et arrêt sous le contrôle de l’entreprise |
| `EXIG-APP-07` | **DOIT** | Clause 1 — Interopérabilité ouverte et portabilité des cartes |
| `EXIG-APP-08` | **DOIT** | Clause 2 — Conformité MCP et délégation d’identité |
| `EXIG-APP-09` | **DOIT** | Clause 3 — Télémétrie exportable et explicabilité |
| `EXIG-APP-10` | **DOIT** | Clause 4 — Usage limité au mandat et interdiction d’entraînement |
| `EXIG-APP-11` | **DOIT** | Clause 5 — Résidence, transferts et lois étrangères |
| `EXIG-APP-12` | **DOIT** | Clause 6 — Notification d’incident |
| `EXIG-APP-13` | **DOIT** | Clause 7 — Audit, sécurité et transparence des changements |
| `EXIG-APP-14` | **DOIT** | Clause 8 — Réversibilité et sortie |
| `EXIG-APP-15` | **DOIT** | Clause 9 — Accord écrit au sens de l’article 25(4) du RIA |
| `EXIG-APP-16` | **DOIT** | Clause 10 — Révocation des identités non humaines |
| `EXIG-APP-17` | **DOIT** | Application de la grille |
