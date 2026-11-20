# B Gabarit de fiche d’agent

La fiche d’agent est l’entrée du registre d’entreprise décrite à la section 11.4. Ce gabarit fixe son contenu minimal et l’étape du cycle de vie où chaque champ devient exigible. Il est normatif par son contenu, pas par sa forme, parce que l’EXIG-GOV-07 y renvoie (section 1.4) : tout outil de registre convient s’il conserve ces champs et leur historique.

## Règles d’utilisation

- **Ouverture et complétude.** La fiche s’ouvre à l’étape Proposition et se complète au fil du cycle de vie (section 11.5). Elle est complète lorsque tous les champs exigés à l’étape Pilote sont remplis, ce que vérifie le jalon qui clôt l’étape Construction et évaluation; avant cela, l’agent n’obtient aucun jeton d’exécution en production, et un pilote sur données réelles est une mise en production (section 11.5). Un agent déjà en exploitation à l’adoption du cadre reçoit une fiche minimale (champs de l’étape Proposition) sous la mesure transitoire de l’EXIG-GOV-16.
- **Source de vérité.** Les valeurs qui commandent un contrôle (palier d’outil, seuil, plafond, portées, niveau d’autonomie) sont lues par la passerelle dans le registre et le catalogue, jamais dans ce que l’agent déclare de lui-même ni dans les annotations d’un serveur MCP (EXIG-GOV-07, EXIG-AUT-08, section 8.3). Le palier et le seuil d’un outil sont tenus au seul catalogue : la fiche ne peut fixer qu’un seuil plus strict, et la passerelle signale tout écart de palier entre la fiche et le catalogue comme un incident de réconciliation. La grandeur qu’un seuil mesure est calculée par la passerelle ou fournie par le système visé, jamais déclarée par l’agent (EXIG-AUT-13).
- **Réévaluation.** Tout changement visé par l’EXIG-GOV-12, qui tient seule la liste des déclencheurs, entraîne une réévaluation de la classe de risque et du niveau d’autonomie avant la mise en service. Le niveau d’autonomie fonctionne comme un certificat interne qui se renouvelle à chaque changement de l’agent ou de son environnement, sans l’indépendance du tiers qui délivre le « certificat d’autonomie » de Feng et coll. **[83]**. S’il y a des RP, l’EFVP est mise à jour, comme le recommande le guide de la CAI lorsqu’un projet change **[413]**.
- **Attestation.** Le parrain atteste périodiquement que l’agent est encore requis et que sa fiche est exacte. Le cadre exige l’attestation au moins tous les 12 mois, et tous les 6 mois pour la classe élevée (EXIG-GOV-13); à titre d’exemple, les bonnes pratiques de Microsoft Entra Agent ID prévoient que le parrain atteste tous les 6 à 12 mois que chaque agent est encore requis **[92]**. Un agent dont l’attestation est échue doit passer à l’état « suspendu » (EXIG-GOV-09).
- **Contenu exclu.** La fiche ne contient ni secret ni renseignement personnel de clients. Chaque serveur MCP a aussi une fiche au registre, qui reprend les blocs de ce gabarit qui le concernent (identification, propriétaires, données et RP, identité et portées, garde-fous, évaluation, observabilité, cycle de vie, dérogations); ses outils ont en plus leur propre entrée au catalogue (section 6.8, annexe C).

## Champs de la fiche

*Tableau 63 — Champs de la fiche d’agent et étape où ils deviennent exigibles*

| **Bloc** | **Champ** | **Contenu attendu** | **Exigé dès** |
| --- | --- | --- | --- |
| **Identification** | Identifiant, nom, version | Identifiant unique et immuable au registre; nom en langage clair; version sémantique (SemVer) | Proposition |
|  | Type, plateforme et modèles | Agent interne, agent intégré à un logiciel-service ou agent de partenaire; plateforme d’exécution; environnements; modèles utilisés (principaux et de repli) avec leurs versions épinglées; version et empreinte de l’invite système (EXIG-INT-15, EXIG-GOV-12); pour un agent intégré à un logiciel-service, actions qu’il y exécute, mécanisme d’arrêt propre et mécanisme d’approbation du fournisseur (EXIG-ARC-02) | Proposition (modèles et invite : Conception) |
|  | Carte d’agent | URL et empreinte de la carte d’agent signée, si l’agent est invocable par d’autres agents (section 6.6) | Pilote, si applicable |
| **Propriétaires** | Propriétaire métier (parrain) | Personne nommée qui répond des effets de l’agent; son unité; son suppléant | Proposition |
|  | Responsable technique et équipe de garde | Personne nommée; équipe joignable pendant les heures d’exploitation déclarées et sa file d’incidents | Conception |
|  | Centre de coûts | Code imputé à chaque trace (section 10.6) | Conception |
| **Finalité** | Tâche et valeur attendue | Tâche confiée, en deux phrases; indicateur de valeur; processus de référence sans agent et son coût | Proposition |
|  | Usages exclus | Ce que l’agent ne doit jamais faire, même à la demande d’un mandant | Conception |
| **Mandants et déclencheurs** | Invocation | Personnes, rôles ou agents autorisés à l’invoquer; canaux; déclencheurs automatiques (événements, planification) | Conception |
| **Orchestration** | Patron | Patron retenu (section 7.2), schéma de ses flux (EXIG-ORC-03) et justification de la configuration la plus simple (avec la comparaison mesurée face à un agent unique, EXIG-ORC-02, et les frontières de contexte ou de sécurité justifiant le découpage, EXIG-ORC-10); protocole retenu pour chaque intégration, justifié par la matrice de sélection (section 6.4); résultat de la revue d’interopérabilité proportionnée (section 6.1); agents appelés; profondeur d’imbrication | Conception |
| **Risque et autonomie** | Classe de risque | Faible, modérée ou élevée, avec l’analyse des critères de la section 8.2 et l’approbation obtenue | Proposition |
|  | Niveau d’autonomie | Plafond N0 à N4 approuvé, par qui (personne nommée) et à quelle date, avec la justification du niveau le plus bas qui atteint l’objectif (EXIG-AUT-01); domaine d’exploitation documenté pour N3 et N4; déclencheurs de renouvellement; échéance de réautorisation d’un agent ambiant de niveau N3 ou N4 | Conception |
|  | Qualification réglementaire | Régimes applicables (Loi sur le privé ou Loi sur l’accès, LPRPDE, RIA, BSIF, directive fédérale), chacun avec les obligations retenues et l’exigence du cadre qui y répond; sorties utilisées ou non dans l’Union européenne; système à haut risque au sens du RIA ou non; décision fondée exclusivement sur un traitement automatisé (art. 12.1 de la Loi sur le privé) ou non; modèle visé par la ligne directrice E-23 du BSIF, s’il y a lieu | Conception |
| **Outils, agents et événements** | Inventaire des dépendances | Pour chaque outil, ressource, invite, agent appelé ou sujet d’événement : référence au catalogue, version épinglée et empreinte (EXIG-INT-15), palier P0 à P3 et seuil tels qu’inscrits au catalogue (la fiche ne fixe qu’un seuil plus strict, EXIG-AUT-13), effet déclaré, clé d’idempotence et mode de vérification pour les outils à effet (EXIG-ORC-22), compensation et son palier (EXIG-ORC-17), étiquette de fiabilité de chaque source de contexte (EXIG-SEC-03), contrat AsyncAPI pour les événements | Conception |
| **Données et RP** | Catégories et classification | Catégories de données, classification, présence de RP et de RP sensibles, finalité de chaque usage | Conception |
|  | Localisation et mémoire | Lieu de traitement (province ou pays, et fournisseur) de chaque modèle, serveur MCP, agent délégataire et magasin de mémoire ou de traces; durées de conservation des mémoires, index vectoriels et traces (section 5.5) | Conception |
| **Identité et portées** | Identité | Identifiant de charge de travail (p. ex. SPIFFE ID) et type de justificatif (section 9.2) | Pilote |
|  | Autorisations | Mode d’accès (délégation par échange de jetons ou identité propre de l’agent); portées et audiences; durée de vie des jetons | Pilote |
| **Garde-fous** | Contrôles actifs | Contrôles d’entrée (contenu non fiable), de sortie (prévention des fuites de données) et d’action (politiques de la passerelle); propriétés réunies parmi contenu non fiable, données sensibles et effet ou communication externe (règle de deux); bac à sable si l’agent exécute du code, avec sa liste d’autorisation réseau; pour un agent de classe élevée exposé à du contenu non fiable, patron de conception retenu contre l’injection (EXIG-SEC-07) | Pilote |
| **Évaluation** | Jeu de référence et résultats | Taille du jeu, dont les scénarios adverses; seuils d’acceptation et seuil de réussite maximale de la suite d’attaques automatisées (EXIG-SEC-24); date, version et résultat de la dernière exécution et du dernier exercice d’équipe rouge (EXIG-SEC-23); pour un agent invocable par d’autres agents, échecs de niveau SHOULD de la trousse A2A et échéance de correction (EXIG-A2A-14) | Pilote |
| **Budget et plafonds** | Enveloppe | Plafonds par tâche (borne de contexte (en jetons) (EXIG-ARC-22), jetons, coût, appels d’outils, itérations, durée d’exécution active et durée totale); quota de jetons par minute et plafond mensuel, avec la marge déclarée pour les dépassements en concurrence et le comportement à l’atteinte du plafond (suspension ou modèle de repli); modèles autorisés et modèle de repli, avec son plafond propre; mesure qui justifie tout modèle de raisonnement (EXIG-FIN-05, EXIG-FIN-06) | Pilote |
| **Compensation et escalade** | Reprise | Compensation de chaque étape à effet et identité de compensation de l’orchestrateur (EXIG-ORC-17); étape pivot; file humaine d’escalade; rôles approbateurs et règles d’approbation; mode dégradé | Pilote |
| **Observabilité** | Traçage et audit | Nom de service; version épinglée et version réellement émise des conventions OpenTelemetry GenAI (réglage de `OTEL_SEMCONV_STABILITY_OPT_IN`); capture du contenu (désactivée par défaut); emplacement du journal d’audit et, pour une décision visée par l’article 12.1, du dossier de décision (EXIG-OBS-11); fenêtre de conservation des événements d’entrée (EXIG-EVT-10); objectifs de niveau de service | Pilote |
| **Conformité** | Évaluations d’impact | Référence et date de l’EFVP, y compris celle exigée par l’article 17 en cas de communication hors du Québec; consultation du responsable de la protection des RP; évaluation d’impact unifiée et analyse d’impact sur les droits fondamentaux (RIA, art. 27) lorsqu’elle est exigée (section 12.9) | Pilote, si applicable |
|  | Transparence | Mode d’information des personnes; procédure de révision humaine pour les décisions visées par l’article 12.1 | Pilote, si applicable |
| **Cycle de vie** | État et revues | État (proposé, conception, construction, pilote, production, suspendu, retiré), énumération commune au registre et au catalogue (annexe C, C.2); dates de mise en production, de dernière attestation et de prochaine revue; historique des versions | Proposition |
| **Dérogations** | Dérogations en vigueur | Identifiant, exigence visée, mesures compensatoires, échéance et approbateur (section 11.6) | Dès qu’une dérogation existe |

## Exemple de fiche lisible par machine

L’exemple suivant décrit un agent fictif de classe modérée, plafonné à N3. Les noms de champs sont un choix du cadre; seules comptent leur présence et leur cohérence avec le gabarit. Les personnes y sont désignées par un identifiant fictif, et les empreintes sont abrégées par « … ».

**Fiche d’agent au registre (JSON, extrait)**

```
{
  "agent_id": "agt-fin-rapprochement",
  "name": "Agent de rapprochement des factures fournisseurs",
  "version": "2.3.0",
  "lifecycle_state": "production",
  "owners": {
    "business_sponsor": "emp-004417",
    "technical_lead": "emp-007762",
    "on_call_team": "garde-finances",
    "cost_center": "CC-4120"
  },
  "purpose": "Apparier factures, bons de commande et réceptions; préparer les paiements.",
  "excluded_uses": ["modifier les coordonnées bancaires d'un fournisseur"],
  "principals": ["role:analyste-comptes-fournisseurs", "agent:agt-fin-orchestrateur"],
  "triggers": ["schedule:rapprochement-nocturne"],
  "orchestration_pattern": "agent-unique-outille",
  "risk_class": "moderee",
  "autonomy": {
    "ceiling": "N3",
    "requested_by": "emp-004417",
    "approved_by": "emp-002318",
    "approved_on": "2027-03-15",
    "odd_ref": "ODD-FIN-007",
    "renew_on": "EXIG-GOV-12"
  },
  "regulatory": {"eu_ai_act_high_risk": false, "automated_decision_art_12_1": false},
  "tools": [
    {"ref": "erp.factures.lire@1.4.0", "digest": "sha256:9f2c41d0…", "tier": "P1"},
    {"ref": "erp.factures.apparier@2.0.1", "digest": "sha256:51ab07e3…", "tier": "P2",
     "compensation": "erp.factures.desapparier@2.0.1", "idempotency_key": true},
    {"ref": "tresorerie.paiements.emettre@1.1.0", "digest": "sha256:c07d9b12…", "tier": "P3",
     "approval": "signed_out_of_band", "idempotency_key": true, "pivot": true, "compensation": null}
  ],
  "data": {"classification": "confidentiel", "personal_information": true,
           "processing_locations": ["Québec"]},
  "identity": {"workload_id": "spiffe://ent.ca/agt-fin-rapprochement",
               "access_modes": {"principals": "token_exchange_rfc8693", "triggers": "client_credentials"},
               "token_ttl_s": 900},
  "budget_per_task": {"context_bound_tokens": 32000, "max_tokens": 50000, "max_cost_cad": 0.75,
                      "max_tool_calls": 15, "timeout_s": 60, "max_wall_clock_s": 28800,
                      "max_iterations": 8},
  "evaluation": {"reference_set": 120, "adversarial_cases": 25,
                 "last_run": "2027-03-10", "result": "pass"},
  "observability": {"service_name": "agt-fin-rapprochement",
                    "genai_semconv_reference": "1.41.0", "genai_semconv_emitted": "1.41.0",
                    "otel_semconv_stability_opt_in": "gen_ai_latest_experimental",
                    "content_capture": false},
  "compliance": {"efvp_ref": "EFVP-2027-014", "efvp_date": "2027-02-28"},
  "next_review": "2027-09-15",
  "exceptions": []
}
```

Lecture : l’agent apparie seul les factures jusqu’à 5 000 $ inclusivement, seuil inscrit au catalogue pour l’outil d’appariement, que la fiche ne reprend pas; au-delà, le contrôle calculé (EXIG-AUT-10) exige une approbation. Les paliers recopiés dans la fiche servent à la lecture : le catalogue fait foi. L’émission d’un paiement, de palier P3, exige toujours une approbation signée hors bande; c’est l’étape pivot, sans compensation, et elle porte une clé d’idempotence vérifiée par la trésorerie. Les tâches lancées par une personne ou par l’orchestrateur passent par l’échange de jetons, et le rapprochement nocturne, déclenché par planification, emploie l’identité propre de l’agent (section 9.3). `renew_on` renvoie à l’EXIG-GOV-12 au lieu d’en recopier la liste. Le niveau N3 est demandé par le parrain et approuvé par une autre personne. Les conventions OpenTelemetry sont consignées par version de référence, version émise et réglage d’adhésion (EXIG-OBS-01). Les valeurs de l’enveloppe budgétaire sont illustratives et se calibrent par mesure (section 10.6).
