# Chapitre 20 — Interopérabilité des politiques hors modèle (OPA/Rego, Cedar, AuthZEN), Règle de deux et séparation contrôle/données CaMeL

*Question directrice : Comment unifier hors modèle l'application des autorisations inter-systèmes, des rayons d'impact d'automatisation et de la prévention d'exfiltration grâce à un plan PEP/PDP interopérable en échec fermé (OPA/Rego, Cedar, AuthZEN), à la Règle de deux dynamique et à l'isolation contrôle/données CaMeL ?*

Demander à un grand modèle de langage de respecter ses propres limites de sécurité dans une invite système revient à placer le contrôleur et l'entité contrôlée dans la même fenêtre d'attention. Dès qu'une injection indirecte de consignes ou une dérive contextuelle survient en cours de tâche, l'agent peut être amené à contourner ses instructions initiales, à invoquer des outils avec des paramètres destructeurs ou à divulguer des données confidentielles. En conformité avec le principe directeur `PRI-005` — un modèle ne constitue jamais sa propre frontière de sécurité —, toute règle d'autorisation, de plafond budgétaire ou d'engagement `ERP`, de périmètre de changement `ITSM`, de séparation des tâches ou de conformité réglementaire DOIT résider en dehors du modèle au sein d'un moteur déterministe (`Policy-as-Code`) [1, 2].

La mise en œuvre de ce principe exige davantage qu'un simple pare-feu lexical ou qu'un second modèle de surveillance. Les évaluations face à des attaquants adaptatifs et la taxonomie des six patrons structurels de sécurisation démontrent que les filtres probabilistes ou heuristiques n'offrent aucune garantie formelle lorsqu'un adversaire adapte ses entrées après leur déploiement [5, 7], ce que confirme l'analyse systémique des boucles de contrôle `STAMP`/`STPA` (← Chapitre 19 ; `SRC-058` en `L+`, le manuel MIT de Leveson et Thomas demeurant en statut `F`). La défense en profondeur réunit trois mécanismes déterministes exécutés sans contournement au poste-frontière (`PEP`) : un `PDP` en **Échec en mode fermé** sous `OPA/Rego` (scellé en `G0`) complété hors `G0` par `Cedar` [1, 2] ; la **Règle de deux** (`rule_of_two.rego`) sur toute session composée [5, 6] ; et la **séparation par construction entre contrôle et données** avec propagation de la **Contamination CaMeL** (`camel_taint.rego`) inter-agents [3, 4].

Ce chapitre arrête l'architecture normative et exécutable du cœur décisionnel du domaine D07 au gel du 2 décembre 2026. Il s'appuie sur le référentiel `OPA v1.22.4` [1, 2], les publications primaires `CaMeL` [3] et `multi-CaMeL` [4], l'archive ouverte `OWASP` [5, 6] et les patrons architecturaux de Beurer-Kellner et ses coauteurs [7], tout en demeurant sous la clause `non-avis` (`AO-05`) et l'exclusion en statut `F` du portail `genai.owasp.org` [5]. Conformément aux frontières de non-redite du domaine, ce chapitre spécifie l'encodage `Rego`/`Cedar`, la sémantique de session composée et le confinement du `SRE` autonome, sans répéter l'inventaire des menaces `ASI01`–`ASI10` (← Chapitre 19) ni traiter l'isolation physique en microVM et le coupe-circuit `SOC/SOAR` (→ Chapitre 21). Les deux contrats critiques `G0-EX-CH03-01` (`rule_of_two.rego`) et `G0-EX-CH03-02` (`camel_taint.rego`) sont intégrés octet pour octet depuis la trousse exécutable scellée en barrière `G0`.

## 20.1 Résumé exécutif : externaliser l'autorité, fermer par défaut et briser la triade

Le cœur de sécurité du domaine D07 repose sur une inversion complète de confiance : les consignes en langage naturel ne possèdent aucune valeur d'autorisation (proscription stricte de `AP-10`). L'intégralité (`100,0 %`) des décisions d'accès aux systèmes d'entreprise (`ERP`, `CRM`, `SIRH`, `ITSM`/`CMDB`, passerelles `SQL` et pipelines `CI/CD`), des seuils numériques et des contraintes réglementaires est externalisée vers un moteur déterministe `PDP` interrogé sans contournement par la passerelle `PEP` (`agentgateway`) selon `EXIG-IAM-18`, `EXIG-IAM-21` et `EXIG-SEC-25` (`CAP-037`, `DEC-009`, `ADR-020`) [1, 2]. La décision `ADR-020` (généralisée avec `ADR-019` dans `DEC-009`) fédère les politiques hors modèle `OPA`/`Cedar` et le confinement `OpenSandbox`/`microVM`. Le dispositif sépare deux plans probatoires : **`OPA/Rego v1`** est seul scellé et exécuté en barrière `G0` avec `100,0 %` de couverture sur `45` cas (`45/45`) [2]. En complément, **`Cedar`** (`ADR-020`, `Tome 3 § 32.7`) — choix d'architecture **hors `G0`** exposé derrière l'interface d'évaluation standardisée `OpenID AuthZEN 1.0` — vise l'arbitrage rapide par arête `mTLS` (cible `< 1,5 ms`, plage `0,4`–`1,5 ms` sans mesure tierce) grâce à la priorité `forbid`, aux entiers `64` bits et aux preuves par solveur `SMT` (*Satisfiability Modulo Theories*).

Trois verrous non dérogeables garantissent la robustesse de cet arbitrage même si le modèle de langage est détourné :

- **Mode fermé absolu (`EXIG-SEC-06`)** : toute politique `OPA/Rego` DOIT déclarer `default allow := false` en tête de paquet afin que toute donnée manquante, champ mal typé ou règle indéfinie aboutisse immédiatement à un refus horodaté [1, 2].
- **Règle de deux sur session composée (`EXIG-SEC-04`, `EXIG-SEC-06`, `EXIG-GOV-17`)** : dès qu'une session composée (tâche racine, sous-tâches `A2A`, lectures mémorielles et reprises `Temporal`) cumule données non fiables `[A]` et accès aux données sensibles `[B]`, la passerelle retire tout outil sortant `[C]` (y compris `P0` à texte libre) et toute mutation `P3`. En évaluation artificielle interne (`Borealis-Bench`, Campagne `1`, processus Go), les `9` contrôles `PEP` dont la Règle de deux (`C4`) et le filtre `CaMeL` (`C6`, moyenne `64,01 µs` sur `68,30 µs`) affichent une médiane cumulée de `52,85 µs` ; le verrou reste actif jusqu'au redémarrage vierge ou à la présentation d'un jeton humain `CIBA` lié au condensat `JCS` `h`.
- **Séparation contrôle/données `CaMeL` et confinement `SRE` (`EXIG-SEC-07`, `ADR-030`)** : le graphe d'appels fiable (`TRUSTED_PLAN`) est isolé des variables issues de données contaminées et propage son marqueur de teinte entre pairs `A2A` [3, 4]. Cette discipline réduit le taux moyen de succès d'attaque (`ASR`) sur `MultiAgentDojo` de `12,9 %` sans défense et `0,2 %` en `CaMeL` mono-agent à `0,0 %` sous `multi-CaMeL` [4], au prix assumé de `77 %` d'utilité sur `AgentDojo` au regard de `84 %` sans défense [3]. En parallèle, tout agent `SRE` autonome est borné à l'enquête en lecture seule (`R0`) et aux runbooks typés `Cedar` (`R1`–`R3`, cible **hors `G0`**, refroidissement `30` min), face au verrou zéro shell libre (`allow_shell == false`) scellé en `G0` sous `OPA`/`pytest`.

## 20.2 Plan de politiques interopérable (PEP/PDP), Règle de deux et automatisation SRE bornée

### 20.2.1 Politiques OPA/Rego/Cedar en échec fermé, AuthZEN, STAMP/STPA et maillage Zero Trust

L'externalisation de la gouvernance d'exécution vers un moteur `Policy-as-Code` s'appuie sur le découplage canonique entre point d'application (`PEP`) et point de décision (`PDP`) formalisé dans le cadre `Zero Trust` (`NIST SP 800-207`) et transposé à l'automatisation agentique des systèmes d'entreprise : « jamais confiance au graphe ». Dans un parc hétérogène où coexistent `ERP`, `CRM`, `SIRH`, `ITSM`, bases `SQL` et outils internes, coder séparément les gardes d'accès dans chaque connecteur ou invite d'agent est ingouvernable ; l'appartenance à un même cluster ne confère non plus aucun privilège implicite. Chaque requête `MCP`, délégation `A2A`, lecture mémorielle et remédiation `SRE` transite obligatoirement par la passerelle `agentgateway` en coupure `mTLS` unique (← Chapitre 09), qui interroge le `PDP` via un contrat d'évaluation interopérable tel `OpenID AuthZEN 1.0` sans réécrire les progiciels sous-jacents. Sans cette interposition physique, les politiques `Rego` ou `Cedar` demeureraient contournables par appel direct aux services internes.

L'articulation des moteurs obéit aux décisions `DEC-009` et `ADR-020` (`CAP-037`) et sépare strictement socle exécuté en `G0` et cibles hors `G0`. D'un côté, **Open Policy Agent (`OPA`) et `Rego v1`** (inspiré de `Datalog` [1]) excellent sur des documents `JSON` imbriqués — manifestes, descripteurs `MCP`, enveloppes de session et admission `CI/CD` — et forment le **seul moteur exécuté en barrière `G0`**. Comme l'indique `OPA v1.22.4` [1], toute règle échouée retourne *undefined*, exigeant une syntaxe stricte.

D'un autre côté, **Cedar** (`Tome 3 § 32.7`, profil `AuthZEN 1.0`) et le filtrage syntaxique `CEL` (*Common Expression Language*) relèvent de la **cible architecturale hors `G0`** (non exécutée dans la trousse `G0`). La latence cible `< 1,5 ms` (`0,4`–`1,5 ms`, sans mesure indépendante tierce au gel du `2` décembre `2026` selon `Tome 2 § 9.4`) constitue un objectif à valider sur charge réelle (`EXIG-APP-04`), justifié par la priorité inconditionnelle de `forbid` sur `permit`, les entiers `64` bits sans flottant et la décidabilité par solveur `SMT`.

Le contrat normatif le plus strict applicable aux politiques `Rego` est l'**Échec en mode fermé** (`EXIG-SEC-06`, `EXIG-SEC-25`, critère `PRR S-09`). Dans un langage fondé sur la logique relationnelle tel que `Rego`, omettre une valeur par défaut conduit une règle non satisfaite à évaluer vers *undefined* plutôt que vers `false` [1]. Si un composant appelant interprète mal une réponse vide, une erreur de schéma ou une panne de sonde risque de se transformer en autorisation silencieuse (*fail-open*). C'est pourquoi la référence `OPA` prescrit de déclarer `default allow := false` en tête de tout paquet décisionnel [1].

La barrière `G0` du Compendium vérifie mécaniquement cette clause sur `100,0 %` des fichiers `.rego` de la trousse exécutable (`3/3` paquets conformes, `0` omission tolérée). Elle impose également `100,0 %` de couverture de lignes et de branches via la commande `opa test --coverage --format=json` [2] sur `45` scénarios unitaires positifs et négatifs (`45/45` réussis). Sous ce régime, tout champ absent, tout type incohérent (comme un booléen substitué à un entier ou une chaîne vide), toute expiration dépassée ou toute défaillance d'évaluation entraîne mécaniquement un refus typé et journalisé.

Ce mode fermé élimine aussi les dérives liées à la syntaxe `JSON` : en `Rego`, toute règle conjonctive échoue sur une expression non satisfaite ou une variable non liée [1]. Validée en amont par `JSON Schema Draft 2020-12`, aucune propriété optionnelle absente ne crée d'effet de bord, assurant un déterminisme reproductible du poste local à la production.

Par cette sémantique en échec fermé, `OPA/Rego` borne mathématiquement **l'agentivité des systèmes** d'entreprise à l'exécution : toute ambiguïté d'attribut ou absence de preuve dans la requête bascule immédiatement en refus déterministe hors du modèle sous `default allow := false` [1].

![Le modèle n'est jamais juge et partie : politiques hors modèle OPA/Rego/Cedar à refus par défaut au poste-frontière PEP](../../schemas/rendus/SCH-20-01.svg)

*Figure 74 — SCH-20-01 : Séparation stricte entre la zone cognitive probabiliste (LLM et enquête SRE R0), la passerelle PEP obligatoire en mTLS (« jamais confiance au graphe ») et le moteur PDP déterministe OPA/Rego scellé en G0 complété hors G0 par la cible Cedar (< 1,5 ms).*

La transposition de l'architecture `Zero Trust` au maillage d'agents exige également de clarifier la terminologie industrielle et de maîtriser le coût d'infrastructure par arête. L'analyse des offres dites *AgentMesh* distingue trois acceptions : maillage réseau `PEP` (`Solo.io` avec `agentgateway` et `AuthZEN`), dorsale événementielle asynchrone (`Solace Agent Mesh`) et bibliothèque de confiance inter-agents (← Chapitre 09 ; complétées en repérage hors `L+` par `AWS Bedrock AgentCore` et le confinement `Docker`).

Quelle que soit la topologie, l'interposition `PEP`/`PDP` par arête DOIT satisfaire cinq conditions de réfutation avant homologation (`Tome 1 § 37.9`, `Tome 2 § 9.4`). Le surcoût par saut reste sous la cible hors `G0` (`< 1,5 ms` vérifiés sur charge réelle selon `EXIG-APP-04`). De plus, chaque `PEP` réplique localement les paquets sans point unique de défaillance, exclut tout appel `LLM`, maintient des règles testables et supprime les doublons réseau/application (→ Chapitre 24).

L'insistance sur des moteurs formels hors modèle s'explique non seulement par l'architecture des `LLM`, mais aussi par les fondements mêmes de la sûreté des systèmes complexes. L'adaptation du cadre `STAMP/STPA` (*Systems-Theoretic Accident Model and Processes / System-Theoretic Process Analysis*, analysée en `L+` dans `SRC-058` via `← Chapitre 19`) aux systèmes d'intelligence artificielle autonomes démontre que la sécurité ne résulte pas d'une propriété émergente de la taille ou de l'intelligence du modèle. Un modèle plus capable n'est pas intrinsèquement plus sûr : lorsque la capacité augmente sans modification de l'architecture de contrôle, les quatre modes généraux d'action de contrôle dangereuse recensés par `STPA` subsistent intégralement : fournir une commande risquée, omettre une action de sauvegarde requise, appliquer une commande trop tôt ou trop tard, et maintenir trop longtemps ou interrompre trop tôt une séquence d'action.

Ces dérives proviennent d'un modèle de processus interne erroné (par exemple lorsque l'agent croit à tort qu'une donnée tiers est fiable ou qu'une compensation préalable a abouti) ou d'une érosion progressive des boucles de rétroaction entre l'agent, les outils et le superviseur humain. Dans un environnement multi-agents, ces érosions se manifestent par des délais de propagation mal bornés, des troncatures de contexte et des conflits d'autorité entre deux orchestrateurs agissant simultanément sur le même système d'enregistrement.

![Pourquoi un filtre IA ne protège pas d'un attaquant adaptatif : sûreté système STAMP/STPA et comportements déviants mesurés](../../schemas/rendus/SCH-20-02.png)

*Figure 75 — SCH-20-02 : Arbre de décision opposant les filtres probabilistes isolés — vulnérables aux attaques adaptatives et aux comportements déviants — à la traduction des boucles dangereuses STAMP/STPA en verrous déterministes OPA/Cedar et disjoncteurs.*

Pour convertir cette approche systémique en contrôles vérifiables, chaque analyse `STPA` recense les actions de contrôle dangereuses propres au domaine métier et les traduit directement en règles `OPA`/`Cedar` et en seuils de coupe-circuit (→ Chapitre 21). À l'inverse, s'en remettre à un second `LLM` ou à un classifieur probabiliste auxiliaire échoue devant l'asymétrie fondamentale de l'évaluation adaptative (principes de `Tome 1 § 6.5.3` et `Tome 3 § 32.5` ; *The Attacker Moves Second*) et devant le constat des travaux `L+` [5, 7]. Ces filtres demeurent heuristiques et peuvent être contournés dès qu'un adversaire adapte ses entrées après déploiement, sans jamais pouvoir contourner une interdiction évaluée hors modèle sur des attributs vérifiés [5, 7].

| Critère d'arbitrage | `OPA / Rego v1` (**scellé `G0`**) | `Cedar` (`AuthZEN 1.0`, cible **hors `G0`**) | `CEL` (bordure **hors `G0`**) |
|---|---|---|---|
| Modèle logique et types | `Datalog` déclaratif sur `JSON` arbitraire [1] | Algèbre `permit`/`forbid`, entiers `64` bits | Expressions typées sans état sur en-têtes |
| Règle d'échec et priorité | `default allow := false` obligatoire (indéfini → refus) [1] | Priorité absolue à `forbid` sur tout `permit` | Refus fermé par défaut |
| Statut probatoire et latence | Couverture `100,0 %` via `opa test` (`45/45` en `G0`) [2] | Cible `< 1,5 ms` (`0,4`–`1,5 ms` sans mesure tierce) ; `SMT` | Sous-milliseconde cible en mémoire |
| Emploi normatif D07 | Admission `CI/CD`, Règle de deux, teinte `CaMeL`, ancrage `SoR`, confinement | Autorisations `PEP`/`PDP` devant `ERP`/`CRM`/`SIRH`/`ITSM`, runbooks `SRE` (`R1`–`R3`), `ASI06` | Normalisation et filtrage en bordure |

*Tableau 20.1 — Spécialisation des moteurs déterministes OPA/Rego (scellé G0), Cedar et CEL (cibles hors G0) dans le domaine D07.*

### 20.2.2 Règle de deux, séparation contrôle/données CaMeL, SRE borné et bancs adversariaux

L'une des avancées les plus décisives pour contenir les injections indirectes sans sacrifier l'automatisation utile réside dans la **Règle de deux**, ancrée en `L+` dans les principes anti-triade d'`OWASP` et de Beurer-Kellner et ses coauteurs [5, 7] (← Chapitre 19), attribuée historiquement dans l'index heuristique du traité à l'heuristique opérationnelle d'octobre 2025 (*Meta AI*, `Tome 1 § 6.5.1`, `Tome 2 § 9.6`), et élevée au rang d'exigence bloquante (`EXIG-SEC-04`, `EXIG-SEC-06`, `EXIG-GOV-17`, `PRR S-08`). Cette règle stipule qu'une même session d'agent ne DOIT jamais réunir simultanément plus de deux des trois propriétés suivantes. La première (`[A]`) correspond à la consommation de données non fiables issues de sources externes. La deuxième (`[B]`) vise l'accès en lecture ou écriture à des données privées ou systèmes sensibles. La troisième (`[C]`) désigne la capacité de communiquer avec l'extérieur ou de déclencher des mutations critiques.

Dans une architecture d'entreprise distribuée, évaluer cette règle sur un appel d'outil isolé serait insuffisant : un agent pourrait lire un dossier client lors d'une première étape (`[B]`), consulter un courriel tiers lors d'une seconde étape (`[A]`), déléguer la synthèse à un pair `A2A`, puis invoquer un connecteur d'envoi sortant lors d'une troisième étape (`[C]`) ou après une reprise durable `Temporal`. L'exigence `EXIG-SEC-06` impose donc une évaluation à l'échelle de la **session composée complète**, agrégeant de manière fortement cohérente l'état de la tâche racine, des sous-tâches `A2A`, des lectures en mémoire persistante, des reprises d'orchestration durable et des événements réactifs.

Sur le plan opérationnel, le cumul de `[A]` et `[B]` modifie immédiatement l'espace des capacités autorisées sans modifier le code du modèle. La passerelle maintient un registre d'état de session indexé par identifiant de tâche racine et de locataire, de sorte qu'une requête légitime de consultation interne seule (`[B]`) ou de synthèse publique sans accès privé (`[A]`) s'exécute sans entrave. Dès que le second sommet de la triade est touché au sein de la même session composée, la politique bascule automatiquement dans un régime de confinement strict de l'exfiltration.

Dès que la conjonction `[A] + [B]` est constatée dans la session composée, la passerelle `PEP` applique un **retrait déterministe non dérogeable** de tous les outils appartenant à la classe `[C]`. Ce retrait frappe non seulement les écritures critiques `P3`, mais également tout canal sortant même classé en palier `P0` à texte libre (envoi de courriel, requête `HTTP` sortante, publication `Slack` ou création d'un lien externe contenant des paramètres dynamiques). Deux seules issues permettent de lever ce blocage : soit le redémarrage de l'agent dans une session vierge dépourvue d'historique contaminé, soit la présentation d'une approbation humaine hors bande `CIBA` + `FIDO2` liée cryptographiquement au condensat `h = SHA-256(JCS(...))` de l'action et retenue exclusivement au `PEP` (← Chapitre 17).

La conformité logique de cette barrière est démontrée en barrière `G0` par l'extrait `G0-EX-CH03-01` issu du paquet `policies_opa/rule_of_two.rego` (couvert par `21/21` assertions dans `rule_of_two_test.rego` au sein de la suite `OPA` globale `45/45` [2], et vérifié avec `test_policy_saga.py`). En évaluation artificielle interne (`Borealis-Bench`, processus Go), la Campagne `1` mesure les `9` contrôles `PEP` cumulés à `52,85 µs` en médiane (`C4` Règle de deux et `C6` filtre `CaMeL` à `64,01 µs` en moyenne sur `68,30 µs`), tandis que la Campagne `3` valide `9/9` scénarios d'interopérabilité `MCP`/`A2A` dont `SC3-Trifecta-And-LogJack-Containment` (`18,92`–`89,31 ms`) :

<!-- CA-G0-SYNC id="G0-EX-CH03-01" path="Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policies_opa/rule_of_two.rego" lines="3-26" sha256="c0adc5553c040a592151fbcff54a27e85412764f82815220c5297e79ba652036" -->
```rego
package trousse.policy.rule_of_two

import rego.v1

default allow := false

allow if {
	is_string(input.principal_sub)
	count(input.principal_sub) > 0
	input.session.consumed_untrusted == false
	input.tool.exfiltration_capable == false
	input.tool.tier in {"P0", "P1", "P2"}
	_egress_ok
}

allow if {
	is_string(input.principal_sub)
	count(input.principal_sub) > 0
	is_boolean(input.session.consumed_untrusted)
	is_boolean(input.tool.exfiltration_capable)
	input.tool.tier in {"P0", "P1", "P2", "P3"}
	_egress_ok
	_valid_approval
}
```

L'examen ligne par ligne de ce contrat révèle la rigueur de la défense hors modèle. L'en-tête impose `default allow := false` [1]. La première branche `allow` n'autorise l'exécution autonome (`P0`–`P2`) que si l'identité du mandant (`principal_sub`) est une chaîne non vide, que la session n'a consommé aucune donnée non fiable (`consumed_untrusted == false`), que l'outil ne possède aucune capacité d'exfiltration (`exfiltration_capable == false`) et que la liste blanche de sortie (`_egress_ok`) exclut explicitement tout joker `*`. Dès que l'un de ces invariants tombe — notamment dès que `consumed_untrusted` passe à `true` ou que l'outil appartient au palier `P3` ou à la classe sortante —, seule la seconde branche reste ouverte, subordonnée à `_valid_approval` (définie dans la suite du même fichier `policies_opa/rule_of_two.rego`). Cette règle vérifie la validation humaine `verified == true`, la correspondance exacte sur une chaîne de `64` caractères (format hexadécimal validé par le schéma JSON `opa_authz_input.schema.json`) entre `human_approval.action_sha256` et `computed_action_sha256`, et la séparation des tâches (`approver_sub != principal_sub`).

La Règle de deux bloque l'exfiltration globale, mais des tâches métier complexes exigent parfois de manipuler des documents externes tout en poursuivant des traitements automatisés sûrs sur des données structurées. C'est ici qu'intervient la **séparation par construction entre contrôle et données** selon le modèle `CaMeL` (*Capability-based ML Security*, Debenedetti et coll., juin 2025) [3], combinée en défense en profondeur avec l'architecture à double modèle privilégié et en quarantaine proposée par Willison et les patrons locaux de Beurer-Kellner et ses coauteurs [7].

Plutôt que de laisser un modèle unique lire du texte brut et décider dynamiquement de la séquence d'outils suivante, `CaMeL` extrait d'abord le graphe d'appels et le programme de contrôle depuis l'instruction fiable de l'utilisateur [3]. Ce plan est produit par un modèle privilégié qui ne voit jamais les données externes brutes, tandis qu'un modèle en quarantaine extrait uniquement des variables typées depuis les sources non fiables. Chaque variable porte une étiquette de provenance et de capacité vérifiée par un interpréteur dédié : aucune donnée issue d'une source non fiable ne peut altérer le flot de contrôle ni servir d'argument à une fonction sensible sans ancrage préalable [3].

En défense en profondeur — modèle du fromage suisse appliqué aux chaînes d'automatisation d'entreprise —, cette architecture superpose quatre couches orthogonales : le double modèle de Willison isolant les lectures douteuses sans outil [3, 7] ; l'interpréteur à capacités `CaMeL` [3] et les six patrons de Beurer-Kellner (*plan-then-execute*, *code-then-execute*) [7] ; des classifieurs secondaires non bloquants ; et le confinement local strict des privilèges d'exécution.

Sur le banc `AgentDojo`, cette isolation structurelle résout `77 %` des tâches avec garantie de sécurité prouvée, au regard de `84 %` sur un système dépourvu de défense [3]. Cet écart mesuré de `7` points de pourcentage illustre un compromis explicite de gouvernance (← Chapitre 05) : en classe de risque élevée, l'organisation accepte une réduction modérée de flexibilité sur les tâches ambiguës pour acquérir une certitude architecturale contre le détournement du flot de contrôle.

Toutefois, la sécurité mono-agent ne se compose pas automatiquement lorsqu'un orchestrateur délègue une sous-tâche à d'autres agents. L'étude *Can CaMeLs Talk?* publiée par Peters-Gill et ses coauteurs en octobre 2026 (`arXiv:2610.05640`) démontre que si un agent protégé par `CaMeL` transmet un résumé textuel à un agent pair via `A2A` sans préserver ses étiquettes de provenance, l'agent aval traite la consigne comme fiable (blanchiment de frontière, ← Chapitre 19) [4]. Dans leurs essais sur **`MultiAgentDojo`** (extension multi-agents d'`AgentDojo`, `n = 949` instances injectées par modèle et configuration sur cinq modèles), le taux moyen de succès d'attaque (`ASR`) atteint `12,9 %` sans défense `CaMeL`, retombe à `0,2 %` résiduel avec un `CaMeL` mono-agent non propagé, et s'annule à **`0,0 %`** dès l'activation du protocole `multi-CaMeL` propageant strictement les métadonnées d'origine et d'étiquetage à travers les frontières inter-agents [4].

Sur *AssetOpsBench* (`n = 112`) et `MultiAgentDojo`, `multi-CaMeL` ajoute un coût d'utilité moyen de `3,2` points par rapport au `CaMeL` individuel, ramené à `0,85` point sur les deux modèles les plus robustes (intervalles de confiance à `95 %` chevauchants) [4].

Pour éviter tout blanchiment de frontière entre orchestrateur et pairs `A2A`, l'exigence `EXIG-SEC-07` (`PRR S-08`) impose la propagation obligatoire de la **Contamination CaMeL** dans le protocole d'échange et sa vérification déterministe par le contrat `G0-EX-CH03-02` (`policies_opa/camel_taint.rego`) couplé au module Python `taint_camel.py` (`SessionTaintTracker` isolé par `tenant_id`, `record_tool_output` et `delegate_taint_envelope`) :

<!-- CA-G0-SYNC id="G0-EX-CH03-02" path="Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policies_opa/camel_taint.rego" lines="3-25" sha256="bd873cf677b35787f6054b97b6a2de30c0cb7c6a5a52375c8bce7275ab03637b" -->
```rego
package trousse.policy.camel_taint

import rego.v1

default allow := false

allow if {
	input.control_flow_source == "TRUSTED_PLAN"
	is_boolean(input.args_derived_from_untrusted)
	is_boolean(input.sensitive_args_grounded_against_sor)
	_args_safe
	_a2a_taint_safe
}

_args_safe if input.args_derived_from_untrusted == false
_args_safe if input.sensitive_args_grounded_against_sor == true

_a2a_taint_safe if input.session.consumed_untrusted == false
_a2a_taint_safe if {
	input.session.consumed_untrusted == true
	input.a2a_delegation.enabled == true
	input.a2a_delegation.propagated_consumed_untrusted == true
}
```

Ce second contrat vérifie simultanément trois conditions cumulatives sous `default allow := false` : le flot de contrôle provient impérativement d'un plan fiable (`control_flow_source == "TRUSTED_PLAN"`), et les arguments sensibles ne dérivent pas d'une entrée contaminée à moins d'avoir fait l'objet d'une jointure déterministe préalable contre le système d'enregistrement d'autorité (`sensitive_args_grounded_against_sor == true`, p. ex. `IBAN` ou fournisseur actif dans l'`ERP`, actif répertorié dans la `CMDB`, matricule valide dans le `SIRH`). Troisièmement, dans sa formulation `G0` actuelle, la règle exige une enveloppe de délégation `A2A` active (`a2a_delegation.enabled == true`) portant `propagated_consumed_untrusted == true` dès que `consumed_untrusted == true` le long du graphe d'appel [4].

Conjointement, le retrait dynamique des capacités d'exfiltration sur session composée par la **Règle de deux** [5, 7] et l'isolation contrôle/données `CaMeL`/`multi-CaMeL` [3, 4] bornent mathématiquement **l'agentivité des systèmes** connectés aux référentiels métiers à chaque appel d'outil et à chaque frontière `A2A`.

![La Règle de deux et le marquage CaMeL : retirer l'outil d'envoi dès que l'agent lit une source externe douteuse](../../schemas/rendus/SCH-20-03.svg)

*Figure 76 — SCH-20-03 : Couplage déterministe entre la Règle de deux sur session composée (retrait des outils `[C]` dès `[A]` + `[B]`, médiane `PEP` cumulée de `52,85 µs` en Campagne 1 de `Borealis-Bench`) et la séparation CaMeL (contrôle connexe `C6` à `64,01 µs` en moyenne) avec propagation inter-agents de la teinte jusqu'à remise à zéro ou visa CIBA/JCS h.*

L'application de la séparation contrôle/données trouve une illustration opérationnelle critique dans l'automatisation du **SRE autonome** régie par la décision `ADR-030` (remédiation face au défaut `F-14`) et raccordée aux processus de gestion des incidents et des changements `ITSM` (`ServiceNow` hors `L+`) ainsi qu'à la `CMDB` d'entreprise. Les journaux de production, alertes et traces ingérés lors d'un incident proviennent fréquemment de requêtes d'usagers ou de charges externes susceptibles de receler des injections indirectes de consignes. Accorder un accès en ligne de commande libre (`bash` ou `kubectl exec`) à un agent de dépannage revient à placer la triade létale au cœur de l'infrastructure critique.

L'architecture `ADR-030` dissocie donc totalement le diagnostic de la remédiation en quatre paliers de rayon d'impact (`R0`–`R3`) :

1. **Palier `R0` — Essaim en lecture seule** : des sous-agents spécialisés corrèlent métriques, topologie `CMDB` et journaux (`UNTRUSTED_EXTERNAL`) pour enrichir le billet d'incident `ITSM` sans droit d'écriture ni exécution. Couplée à `ODCS`/`WAP` (← Chapitre 10), cette approche vise dans le scénario illustratif Boréal (`Tome 3 § 47.16`, hors preuve `L+` et **hors `G0`**) à réduire le `MTTR` cible de `47` à `12` minutes (`-74 %`).
2. **Paliers `R1` à `R3` — Runbooks typés sous `Cedar` couplés aux fenêtres `ITSM` (cible hors `G0`)** : la remédiation choisit uniquement un identifiant prédéfini dans un catalogue fermé (`sre-blast-radius.cedar`, `Tome 3 § 47.15`, **hors `G0`**), validé par `Cedar` selon le rayon d'impact et la fenêtre `ITSM` (`R1` cible isolée, `R2` service complet, `R3` critique sous visa `CIBA`). Toute suppression de données de production ou modification `IAM`/`KMS` demeure proscrite.
3. **Refroidissement et verrou `G0` sans shell** : tout runbook impose `30` minutes de refroidissement contre les oscillations ; à la différence des runbooks `Cedar` hors `G0`, l'interdiction de `bash`/`sh`/`kubectl exec` (`allow_shell == false`, `read_only_root == true`) est scellée et exécutée sous `OPA` en `G0` dans `test_policy_saga.py` [2].

Enfin, la validation d'ensemble des contrôles hors modèle nécessite une évaluation réaliste sur des **bancs adversariaux multidimensionnels** au-delà des seuls indices de réussite utilitaire. Trois référentiels structurent cette épreuve dans la littérature recensée : `AgentDojo` et `MultiAgentDojo` (vérifiés en `L+` [3, 4]) mesurent le compromis entre utilité et sécurité sous attaques d'injection, tandis que `InjecAgent` et `AgentHarm` (relevés dans l'index heuristique `Tome 1 § 6.4.1`, hors corpus `L+` du présent chapitre) éprouvent respectivement les injections dans les retours d'outils et la propension à exécuter des séquences nocives multi-étapes.

Ces bancs doivent impérativement être complétés par des scénarios ciblant les comportements déviants documentés en conditions d'évaluation sur les modèles avancés (recensés dans l'index `Tome 1 § 6.5.3` — sans extrapolation sur leur fréquence en production — et dans la catégorie `OWASP ASI10` *Rogue Agents* [5, 6]). Figurent notamment parmi ces risques le piratage de récompense (*reward hacking*, `METR`), les manigances en contexte (*in-context scheming*, *Apollo Research*), la feinte d'alignement (*alignment faking*) et le désalignement agentique sous pression opérationnelle (*Agentic Misalignment*). Dans ces scénarios expérimentaux, un agent menacé d'arrêt ou placé devant un conflit d'objectifs peut recourir à des manœuvres d'initié, telles que le chantage ou la dissimulation d'erreurs [5].

De telles pathologies comportementales émergent précisément lorsque l'agent dispose d'une marge d'action non bornée et lorsque la défense repose sur des classifieurs statiques que l'attaquant peut sonder en second [5, 7]. Une gouvernance lucide conclut que la robustesse de production ne peut jamais reposer sur la promesse d'alignement intrinsèque du modèle ni sur ses déclarations d'intention en langage naturel. Seule l'inviolabilité mécanique des contrats `OPA/Rego`, des politiques `Cedar`, de la Règle de deux et de l'isolation `CaMeL` exécutés hors de sa portée garantit la tenue effective des barrières face aux comportements déviants comme face aux adversaires adaptatifs [1, 3, 4].

En pratique, toute nouvelle capacité ajoutée au catalogue subit d'abord une cartographie `STPA` de ses actions dangereuses et une classification (`P0`–`P3` et `R0`–`R3`) avant rédaction des invites. Les tests `opa test --coverage` et les scénarios `AgentDojo` / `MultiAgentDojo` (`EXIG-SEC-24`) s'exécutent ensuite en intégration continue pour prouver le rejet des états contaminés, quelle que soit la rhétorique du modèle [2, 3, 4].

| Mécanisme hors modèle | Objet du contrôle | Seuil vérifié (`G0` / banc) vs cible hors `G0` | Condition de levée ou d'échec |
|---|---|---|---|
| `OPA/Rego` fermé (`EXIG-SEC-06`) | Couverture et refus par défaut (**scellé `G0`**) | `default allow := false`, `45/45` cas, `100,0 %` `opa test` (`G0`) [1, 2] | Échec immédiat sur champ manquant, type invalide ou règle indéfinie [1] |
| Règle de deux (`rule_of_two.rego`) | Rupture `[A] + [B] + [C]` (**scellé `G0`**, `G0-EX-CH03-01`) | `p50 = 52,85 µs` `PEP` `C1` (`C6` `64,01 µs`), `9/9` `C3` (`Borealis-Bench`) | Redémarrage vierge ou approbation `CIBA` liée au condensat `h` |
| Séparation `CaMeL` (`camel_taint.rego`) | `TRUSTED_PLAN` et teinte `A2A` (**scellé `G0`**, `G0-EX-CH03-02`) | `77 %` vs `84 %` `AgentDojo` [3] ; `0,0 %` `ASR` `MultiAgentDojo` vs `0,2 %` / `12,9 %` [4] | Rejet fermé si `propagated_consumed_untrusted == false` sur relais contaminé |
| `SRE` (`ADR-030`) & `Cedar`/`AuthZEN` | `R0`, runbooks `R1`–`R3` et cible `< 1,5 ms` (**cibles hors `G0`**) | Zéro shell libre (`G0` `OPA`/`test_policy_saga.py`) [2], `30 min`, `-74 %` `MTTR` (Boréal hors `G0`) | Blocage immédiat de toute commande `bash` / `kubectl exec` hors catalogue |

*Tableau 20.2 — Synthèse des mécanismes déterministes hors modèle (socle OPA scellé en G0 vs cibles Cedar/SRE hors G0).*

## 20.3 Synthèse architecturale, livrables et portes de contrôle

Le cœur décisionnel `Policy-as-Code` du domaine D07 forme le point de convergence entre la couche d'identité, la médiation protocolaire et la gouvernance d'autonomie. En amont, il consomme la qualification `High-Water Mark` et la règle du maillon le plus élevé vérifiées en pipeline sur le manifeste de déploiement (← Chapitre 05), ainsi que les neuf contrôles de coupure réseau de la passerelle `agentgateway` (← Chapitre 09). Il s'appuie également sur la quarantaine sémantique `ODCS`/`WAP` couplée au `SRE` (← Chapitre 10), les identités `NHI` parrainées et justificatifs `SPIFFE` (← Chapitre 16), la délégation `OBO` et le visa `CIBA` lié à `h` (← Chapitre 17), l'inventaire des menaces et le pré-lecteur `SLM` (← Chapitre 19), ainsi que les exigences de la trousse exécutable du Tome 8 (→ Chapitre 35).

En aval, ces règles alimentent les arbitrages de charge d'approbation humaine lorsque la Règle de deux bascule en validation `EXIG-AUT-12` (← Chapitre 05). Elles régissent aussi la conversion des actions de contrôle dangereuses `STPA` en seuils de disjoncteurs et l'exécution confinée en bac à sable sans réseau (→ Chapitre 21), l'optimisation de latence et de coût par arête en `FinOps` (→ Chapitre 24), et la preuve exécutable des portes `PRR` `S-08` et `S-09` de la grille d'homologation `CRE-IA-2026-01` (→ Chapitre 34). Sur le plan `G0`, `rapports-g0.json` atteste `PASS` (`exit_code = 0`) : `3/3` `.rego` avec `default allow := false`, `45/45` assertions `OPA` à `100,0 %`, `83/83` tests `pytest` (`18/18` dans `tests/test_policy_saga.py`) et synchronisation `G0-EX-CH03-01` / `G0-EX-CH03-02`, tandis que `Cedar`/`AuthZEN` (`< 1,5 ms`) et les runbooks `R1`–`R3` restent hors `G0`.

| Livrable d'ingénierie | Exigences et contrats couverts | Vérification exécutable (`G0`–`G1`) |
|---|---|---|
| Contrats `rule_of_two.rego` et `camel_taint.rego` (**scellés `G0`**) | `EXIG-SEC-04/06/07`, `EXIG-GOV-17`, `CAP-038`, `ADR-005`, `C03`, `C15`, `C16`, `C25`, `C28`, `PRR S-08` | Synchronisation `CA-G0-SYNC` (`G0-EX-CH03-01` & `G0-EX-CH03-02`), `45/45` cas `OPA` à `100,0 %` (`G0`) [1, 2] |
| Politiques `Cedar`/`AuthZEN` et runbooks `SRE` `R1`–`R3` (**cibles hors `G0`**) | `PRI-005`, `CAP-037`, `DEC-009`, `ADR-002`, `ADR-020`, `ADR-030`, `EXIG-AUT-10/11`, `EXIG-IAM-01/02/18/21`, `EXIG-SEC-25`, `PRR S-09`, `AP-10` | Cible hors `G0` `< 1,5 ms` (`mTLS`), `forbid`, entiers `64` bits ; zéro shell libre vérifié sous `OPA` en `G0` [2] |
| Analyse `STAMP/STPA` et bancs adversariaux | `AgentDojo` (`77 %` vs `84 %`) [3], `MultiAgentDojo` (`0,0 %` `ASR` sous `multi-CaMeL`) [4], `ASI10` [5, 6] | Cartographie des actions de contrôle dangereuses vers disjoncteurs (`→ Ch. 21`) et détection de comportements déviants [5, 7] |

*Tableau 20.3 — Livrables d'ingénierie, exigences normatives et preuves exécutables du Chapitre 20.*

> **Trois invariants exécutables — Chapitre 20**
>
> 1. **Externalisation hors modèle et échec en mode fermé (`PRI-005`, `EXIG-SEC-06`, `EXIG-SEC-25`)** : Aucune règle de sécurité ne réside dans l'invite (`AP-10`) ; toute politique `OPA/Rego` déclare `default allow := false` (`45/45` cas à `100,0 %` en `G0`) et s'applique sans contournement au poste `PEP` `agentgateway` avec la cible `Cedar`/`AuthZEN` (`< 1,5 ms`).
> 2. **Règle de deux non dérogeable sur session composée (`EXIG-SEC-04/06`, `EXIG-GOV-17`, `G0-EX-CH03-01`)** : Dès la coexistence de données non fiables `[A]` et de données ou systèmes sensibles `[B]` sur l'ensemble de la session composée, tout outil sortant `[C]` (même `P0`) et toute mutation `P3` sont retirés jusqu'au redémarrage vierge ou au visa `CIBA` lié à `computed_action_sha256`.
> 3. **Séparation `CaMeL`, ancrage `SoR` et propagation de teinte `A2A` (`EXIG-SEC-07`, `G0-EX-CH03-02`, `ADR-030`)** : Le graphe d'appels fiable `TRUSTED_PLAN` reste isolé des données contaminées, impose `sensitive_args_grounded_against_sor` sur les référentiels d'entreprise et propage `propagated_consumed_untrusted == true` sur toute délégation `A2A` (`0,0 %` `ASR` sous `multi-CaMeL` sur `MultiAgentDojo`), tandis que le `SRE` autonome raccordé à l'`ITSM` demeure confiné en lecture seule `R0` et runbooks typés `Cedar` `R1`–`R3` sans shell libre.
