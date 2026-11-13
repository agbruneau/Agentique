# Chapitre 32 — Assurance

*Question directrice : comment démontrer qu'un système d'agents se comporte comme prévu ?*

> **Version 2 — 11 novembre 2026.** État de référence : prépublication arXiv 2608.01558 (3 août 2026), NIST SP 800-207 (août 2020), Agentic Trust Framework (billet du 2 février 2026), AIUC-1 dans sa livraison du 15 octobre 2026, page du groupe W3C Agent Conformance and Benchmarking consultée le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre; [13] et [14] sont secondaires. Les renvois « chapitre N » pointent vers les chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Les chapitres 29 à 31 répondent à trois questions : qui est l'agent, que peut-il faire, qu'est-ce qui le menace. Il en reste une quatrième, celle d'un comité de risque, d'un auditeur ou d'un client : sur quoi repose l'affirmation que le système fait ce qui est prévu, et rien d'autre ? « Assurance » désigne ici cette démonstration, et non la couverture financière d'un sinistre, traitée au chapitre 36.

Pour un logiciel déterministe, la démonstration s'appuie sur des tests répétables et sur la revue du code. Un agent choisit ses actions à l'exécution, à partir d'un contenu qu'il ne maîtrise pas. La thèse de ce chapitre est qu'en novembre 2026 aucune preuve unique ne suffit. L'assurance se compose de quatre éléments partiels : des invariants vérifiés sur la trajectoire entière, une application des règles placée hors de l'agent, une attestation par un tiers et des tests adverses adaptatifs. Chacun a une limite connue.

---

## 32.1 Limites du contrôle action par action

### Ce que voit un garde-fou

La plupart des contrôles déployés autour des agents jugent une action à la fois : cet appel d'outil est-il permis, cet argument est-il valide, cette sortie contient-elle une donnée sensible ? Les points d'application du chapitre 30 fonctionnent ainsi. Ils sont nécessaires, mais un contrôle sans état ignore ce que les actions précédentes ont déjà fait.

Une prépublication d'août 2026 (Lotfi, Shanto, Karim et Bertino) en fait son argument central : des actions permises une à une peuvent, ensemble, violer une contrainte du système [1]. Deux exemples :

- Un agent d'ordonnancement d'un réseau 5G abaisse peu à peu la priorité d'une tranche réservée à la sécurité publique. Chaque réallocation passe les vérifications locales; la fenêtre de rétablissement imposée par la norme est pourtant dépassée.
- Un agent clinique accélère plusieurs congés d'hôpital, chacun justifié, et enfreint la durée d'observation cumulée prévue par le parcours de soins.

Aucun adversaire n'intervient : la violation naît de la trajectoire.

Le même article relève qu'un agent peut effectuer des milliers d'appels d'outils pendant qu'un humain n'examine qu'une poignée de décisions [1]. L'approbation au cas par cas ne corrige pas le défaut : l'approbateur voit une action, pas la série (chapitre 22).

### Ce que les protocoles ne relient pas

Le constat le plus utile pour un architecte : les protocoles d'outils définissent les actions disponibles, les normes d'un domaine définissent les séquences permises, et rien ne relie les deux [1]. Un outil MCP se décrit par un nom, une description et des schémas (chapitre 5). Une règle comme « jamais après telle autre opération » n'y a pas de place.

Trois familles de règles échappent ainsi au contrôle par action.

- **Le cumul** : un plafond qui porte sur la somme des actions, non sur chacune.
- **L'ordre** : une action interdite après une autre, ou exigée avant; la séparation des tâches en est le cas classique.
- **La durée** : une fenêtre à respecter, un délai maximal entre deux états.

---

## 32.2 Assurance de trajectoire

### Deux définitions

L'article emploie deux notions sans les définir formellement [1]. Le **confinement comportemental**, qu'il tient pour le défi le plus fondamental, consiste à maintenir une trajectoire d'exécution dans l'enveloppe de comportement fixée par les normes applicables. L'**assurance de trajectoire**, terme de son titre, se lit ici comme la vérification que la trajectoire, à mesure qu'elle évolue, satisfait les contraintes du système pendant toute l'exécution, et non aux seuls points de décision.

### Pourquoi les mécanismes actuels ne suffisent pas

| Mécanisme | Limite relevée par l'article [1] |
|---|---|
| Gardes à l'exécution | Sans état; jugent une action isolée |
| Compilation d'une politique en spécification formelle par un modèle de langage | Ni complétude ni fidélité garanties |
| Moniteurs probabilistes appris sur des traces | Non ancrés dans une politique explicite |
| Règles temporelles appliquées à l'exécution | Écrites à la main, pour un seul agent |
| Bancs d'essai | La plupart ne comportent pas de politique explicite |

### Trois surfaces, un même argument

L'article étend le raisonnement au-delà de l'agent isolé [1]. À l'échelle d'un agent, il n'existe pas de séparation fiable entre données et instructions. Entre agents, les capacités annoncées dans une Agent Card A2A sont autodéclarées et l'identité ne se propage pas d'un saut de délégation au suivant (chapitres 6 et 30). Sous les deux, le routeur qui choisit un modèle par requête forme une troisième surface (chapitre 44).

Les auteurs concluent que la sécurité devrait être une propriété vérifiable des architectures, des protocoles et des environnements d'exécution, et non une couche facultative de recommandations.

### Le statut de la proposition

Ce texte est un article de vision de six pages, accepté au volet « Visionary » du ACM AI Leadership Summit 2026 [1]. Il ne rapporte aucune expérience et ne propose aucun système. L'assurance de trajectoire est, à ce jour, un programme de recherche et non un produit.

### Ce qui est faisable maintenant

Ces gestes sont une déduction de ce chapitre, non de l'article.

1. **Écrire les invariants.** Pour chaque processus confié à un agent, recenser les règles de cumul, d'ordre et de durée, et les exprimer sous une forme vérifiable par programme.
2. **Les vérifier dans un composant à état, hors de l'agent.** Une passerelle (chapitre 24) ou un moteur d'orchestration déterministe (chapitre 17) tient le compte que l'agent ne tient pas. Le patron Simplex en est la forme en sûreté fonctionnelle; hors connexion, un plafond cumulatif se répartit d'avance en droits (chapitre 46).
3. **Rattacher chaque action à une trajectoire.** Sans identifiant de corrélation, aucune reconstitution n'est possible (chapitres 30 et 33).
4. **Prévoir la sortie.** Un seuil d'alerte avant la violation, puis l'arrêt, la compensation (chapitre 18) ou l'escalade vers un humain (chapitre 22).

Ces invariants restent écrits à la main : c'est la limite même que l'article relève, et leur complétude n'est pas démontrée.

---

## 32.3 Zero trust appliqué aux agents

### Le modèle de référence

La publication NIST SP 800-207, d'août 2020, définit le zero trust comme un paradigme centré sur la protection des ressources, fondé sur la prémisse que la confiance n'est jamais accordée implicitement et doit être évaluée en continu [2]. L'identité y couvre les personnes et les entités non humaines. Tout accès passe par un point de décision et un point d'application. Ce qui se trouve au-delà du dernier point d'application forme une « zone de confiance implicite », où tout est tenu pour également fiable; l'objectif est de la réduire au minimum.

Le texte énonce sept principes [2]. Quatre s'appliquent directement à un agent.

| Principe de SP 800-207 | Lecture pour un agent |
|---|---|
| 3. Accès par session, au moindre privilège; l'accès à une ressource n'en ouvre aucune autre | Un jeton par ressource et par tâche, sans relais (chapitre 5) |
| 4. Politique dynamique, qui peut inclure des attributs comportementaux | La décision peut tenir compte de la trajectoire |
| 6. Autorisation réévaluée pendant la transaction | Révocation en cours de tâche (chapitre 30) |
| 7. Collecte étendue sur l'état des actifs et des communications | Télémétrie d'agent (chapitre 33) |

### Où se trouve la zone de confiance implicite

Pour un agent, cette zone est la fenêtre de contexte. Un résultat d'outil, un document récupéré, le message d'un autre agent : tout ce qui y entre est traité par le modèle au même niveau, faute de séparation fiable entre données et instructions [1]. Un point d'application logé dans l'agent se trouve donc à l'intérieur de la zone qu'il devrait garder. Le contrôle doit se situer entre l'agent et la ressource. Le chapitre 30 aboutit à la même conclusion pour l'approbation : recueillie dans l'hôte, elle ne prouve rien.

SP 800-207 précise que ses principes visent le travail au sein d'une organisation ou avec des partenaires, non les processus publics anonymes [2]. Les agents qui traitent avec des tiers inconnus sortent donc de son périmètre (chapitre 29).

### L'Agentic Trust Framework

La Cloud Security Alliance a publié le 2 février 2026 un billet présentant l'Agentic Trust Framework (ATF), spécification ouverte sous licence CC BY 4.0 qui transpose le zero trust aux agents [3]. Elle s'organise en cinq éléments, chacun résumé par une question : identité (qui es-tu ?), comportement (que fais-tu ?), gouvernance des données (que consommes-tu, que produis-tu ?), segmentation (où peux-tu aller ?) et réponse aux incidents (et si tu dérapes ?).

L'ATF ajoute quatre niveaux d'autonomie : *Intern* (observer et signaler), *Junior* (recommander, chaque action étant approuvée), *Senior* (agir dans des garde-fous, avec notification après coup), *Principal* (agir en autonomie dans un domaine). Passer au niveau suivant exige de franchir cinq portes : performance, validation de sécurité, valeur d'affaires, dossier d'incidents et approbation de gouvernance [3].

L'apport du cadre est de lier la preuve accumulée à l'autonomie accordée, idée qu'on retrouve aux chapitres 22 et 34. Trois réserves s'imposent. Le billet est signé par l'auteur du cadre, Josh Woodruff, de MassiveScale.AI, et non par un comité. Les seuils chiffrés de promotion (durée au palier, exactitude, disponibilité) sont des choix d'auteur. Les correspondances réglementaires y sont qualifiées d'illustratives [3]. Selon la presse spécialisée, la CSA aurait repris l'intendance de la spécification en mai 2026 [14]. Aucune donnée d'adoption indépendante n'a été trouvée.

---

## 32.4 Certification et conformité

### Des instruments de natures différentes

Les cadres cités ensemble dans les appels d'offres ne font pas le même travail.

| Instrument | Nature | Certifiable | Ce qu'il permet d'affirmer |
|---|---|---|---|
| AIUC-1 | Norme privée de certification d'agents | Oui, pour un an [4] | Un agent donné a passé un audit et des évaluations techniques |
| ISO/IEC 42001 | Système de management de l'IA | Oui [13] | L'organisation gère son IA; pas de contrôles techniques propres aux agents (chapitre 35) |
| CSA MAESTRO | Méthode de modélisation des menaces | Non [8] | Une analyse structurée a été menée |
| OWASP Top 10 for Agentic Applications | Liste de risques | Non [13] | Un vocabulaire commun (chapitre 31) |
| W3C Agent Conformance and Benchmarking | Groupe communautaire | Non; rien de publié [7] | Rien encore |

### AIUC-1

AIUC-1 se présente comme la certification technique de la sécurité des agents. Elle est maintenue par l'Artificial Intelligence Underwriting Company [4]. Ses exigences se répartissent en six domaines : données et vie privée, sécurité, sûreté, fiabilité, imputabilité, société [4][6].

Le processus compte quatre étapes [4]. Le cadrage fige la version de la norme pour un an. AIUC mène les évaluations et annonce de 1 000 à 5 000 scénarios de test, puis des reprises trimestrielles. Un auditeur accrédité examine ensuite les contrôles. Le certificat vaut un an.

La norme est révisée chaque trimestre. Les titres des livraisons de 2026 donnent la direction : exigences de preuve en janvier; sécurité de MCP et permissions d'agents en avril; agents de programmation en juillet; modèles à poids ouverts et tests par des tiers en octobre [5]. Le site affiche des correspondances avec MITRE ATLAS, ISO 42001, le règlement européen, le NIST AI RMF et les listes OWASP, et présente comme certifiés des agents de Cursor, Fin, ElevenLabs, Harvey, UiPath, KPMG et Sierra [4][5].

Quatre réserves s'imposent.

**La portée.** Le certificat vise l'agent d'un fournisseur, sur une version figée de la norme. Il ne dit rien du déploiement chez l'acheteur : ses outils, ses données, ses permissions. Un billet de fournisseur le dit aussi : le certificat reflète les contrôles à un moment donné, et l'acheteur doit encore tester et surveiller ce qu'il déploie [13].

**L'indépendance.** La société qui maintient la norme mène aussi les évaluations adverses. L'audit revient à un tiers accrédité, mais un seul auditeur est nommé, Schellman, dont l'accréditation a été annoncée le 3 février 2026 [4][5].

**La vérifiabilité.** La liste complète des contrôles n'a pas été lue pour ce chapitre [6]. L'affirmation selon laquelle la certification couvre les dix risques agentiques d'OWASP est un titre de l'éditeur [5].

**Le rythme.** Une révision trimestrielle suit la menace, mais deux certificats émis à six mois d'écart n'attestent pas la même chose.

### Le groupe W3C

Le groupe communautaire Agent Conformance and Benchmarking a été proposé le 25 août 2026 et lancé le 30 [7]. Il veut produire des méthodes ouvertes et reproductibles pour mesurer si des ressources web et des systèmes d'agents répondent aux exigences des agents autonomes. Les livrables prévus comprennent une grille de préparation, un jeu de contrôles de gouvernance, des suites de conformité exécutables et un format de rapport.

La page recense 29 participants et aucun document. Elle rappelle qu'un groupe communautaire ne représente pas nécessairement les vues du W3C. C'est un chantier à suivre, pas un référentiel.

### MAESTRO et le dossier interne

MAESTRO, cadre de Ken Huang publié par la CSA le 6 février 2025, décompose un système agentique en sept couches (chapitre 31) [8]. Pour l'assurance, un modèle de menaces documenté justifie le choix des invariants et des tests.

Aucun de ces instruments ne remplace un dossier tenu par l'entreprise : invariants retenus, preuves que les contrôles s'appliquent hors de l'agent, résultats de tests, journaux d'audit (chapitre 30). Les obligations réglementaires relèvent du chapitre 35.

---

## 32.5 Tests adverses

### L'attaquant joue en second

Une défense évaluée contre une liste fixe d'attaques n'est pas évaluée. Une prépublication d'octobre 2025 l'a montré : douze défenses récentes contre le débridage et l'injection de prompt, qui rapportaient pour la plupart un taux de succès d'attaque proche de zéro, cèdent le plus souvent à plus de 90 % devant un attaquant adaptatif, c'est-à-dire qui connaît la défense et optimise contre elle [9].

### Les bancs statiques surestiment

AutoDojo, prépublication de juin 2026 révisée en septembre, transpose l'argument aux agents [10]. Ce banc d'essai génère en boîte noire des injections indirectes adaptées à l'agent et à la défense visés. Sur dix défenses et cinq modèles, les auteurs concluent que les bancs statiques surestiment souvent l'efficacité des défenses, que la plupart sacrifient beaucoup d'utilité ou restent vulnérables, et que les tâches sous-spécifiées sont les plus exposées. Une consigne vague est donc à la fois une cause d'échec (chapitre 21) et une surface d'attaque.

### L'application hors bande : un signal, pas une preuve

Une troisième prépublication examine les défenses qui appliquent une politique déterministe hors du modèle, plutôt que d'entraîner celui-ci à refuser [11]. Elle les rattache à trois notions classiques : protection d'intégrité, moniteur de référence, moindre privilège. Dans une reproduction indépendante sur le banc AgentDojo, l'une d'elles, Progent, ramène le succès moyen des attaques de 25,8 % à 4,2 %; une attaque adaptative écrite à la main ne le fait pas remonter (2,6 %).

Les auteurs bornent eux-mêmes ce résultat : un seul point de mesure, un petit modèle à poids ouverts, un seul gabarit d'attaque, aucune attaque optimisée en boîte blanche. Il est compatible avec l'hypothèse qu'une application hors bande résiste mieux qu'une détection dans le modèle, sans l'établir. Il va dans le sens de la section 32.3.

### Un programme de tests

La CSA a publié le 28 mai 2025 un guide de tests adverses pour l'IA agentique [12]. Il demande d'éprouver des flux complets et non des comportements de modèle isolés, de couvrir les dépendances entre agents et de mener l'exercice en continu.

Cinq règles s'en dégagent.

1. Tester le système déployé, avec ses outils et ses permissions, non le modèle seul.
2. Employer un attaquant adaptatif; un score sur banc statique est une borne optimiste.
3. Mesurer ensemble sécurité et utilité : une défense qui bloque tout ne démontre rien.
4. Rejouer les tests à chaque changement de modèle, de prompt ou d'outil, ou de passage à un modèle distillé (chapitres 34 et 47).
5. Ajouter des tests de trajectoire sans adversaire, qui vérifient les invariants de la section 32.2.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Unité de contrôle | L'action et la trajectoire | Agent en lecture seule, sans effet cumulatif : l'action suffit |
| Lieu de vérification des invariants | Composant à état hors de l'agent | — |
| Point d'application des politiques | Entre l'agent et la ressource | Contrôle dans l'hôte en complément seulement |
| Niveau d'autonomie | Accordé par paliers, sur preuve consignée | Tâche réversible à faible enjeu |
| Certificat d'un fournisseur | Critère de présélection, complété par des tests internes | Jamais comme preuve unique |
| Évaluation d'une défense | Attaquant adaptatif; sécurité et utilité mesurées ensemble | Banc statique comme test de non-régression |
| Fréquence des tests | À chaque changement de modèle, de prompt ou d'outil | — |

---

## Points à retenir

- Des actions permises une à une peuvent violer ensemble une règle du système, sans adversaire. Les règles de cumul, d'ordre et de durée échappent au contrôle par action.
- L'assurance de trajectoire est un programme de recherche. Écrire les invariants et les vérifier hors de l'agent est faisable maintenant, sans garantie de complétude.
- Pour un agent, la zone de confiance implicite est la fenêtre de contexte. Le point d'application se place entre l'agent et la ressource.
- L'Agentic Trust Framework lie la preuve accumulée à l'autonomie accordée. Son adoption n'est pas mesurée.
- AIUC-1 est la seule certification propre aux agents repérée. Elle atteste l'agent d'un fournisseur pour un an, non son déploiement chez l'acheteur. Le groupe W3C sur la conformité, lancé en août 2026, n'a rien publié.
- Une défense évaluée sur un banc statique est souvent surestimée; seul un attaquant adaptatif donne une mesure crédible.
- L'application déterministe hors du modèle est une piste prometteuse, sur la foi d'un seul résultat à petite échelle.
- Démontrer, en 2026, c'est assembler un dossier de preuves partielles et en nommer les limites.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Securing Agentic AI: From Per-Action Checks to Trajectory Assurance (arXiv 2608.01558)](https://arxiv.org/abs/2608.01558) — notice et texte HTML.
2. [NIST SP 800-207, Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) — section 2.
3. [CSA — The Agentic Trust Framework](https://cloudsecurityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust-governance-for-ai-agents)
4. [AIUC-1 — page d'accueil](https://www.aiuc-1.com/)
5. [AIUC-1 — fil des publications](https://www.aiuc-1.com/research) — titres et dates seulement.
6. [AIUC-1 — présentation de la norme](https://standard.aiuc-1.com/)
7. [W3C Agent Conformance and Benchmarking Community Group](https://www.w3.org/community/agent-conformance/)
8. [CSA — MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
9. [The Attacker Moves Second (arXiv 2510.09023)](https://arxiv.org/abs/2510.09023) — résumé.
10. [AutoDojo (arXiv 2606.15057)](https://arxiv.org/abs/2606.15057) — résumé.
11. [Adaptive Evaluation of Out-of-Band Defenses (arXiv 2606.26479)](https://arxiv.org/abs/2606.26479) — résumé.
12. [CSA — Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide) — page de présentation.

Sources secondaires :

13. [Pillar Security — cadres de sécurité pour agents](https://www.pillar.security/blog/best-ai-security-frameworks-for-ai-agents-2026) — billet de fournisseur, lu.
14. [Campus Technology — la CSA élargit ses travaux sur l'IA agentique (6 mai 2026)](https://campustechnology.com/articles/2026/05/06/cloud-security-alliance-expands-focus-on-governance-and-assurance-for-agentic-ai-systems.aspx) — résumé de recherche seulement, page non lue.

## Limites de ce chapitre

- Les pages ont été lues au moyen d'un outil qui en restitue une synthèse; une nuance a pu se perdre. Seul le texte de SP 800-207 a été lu directement.
- Pour [9], [10] et [11], seuls les résumés ont été lus. Ce sont des prépublications; leur évaluation par les pairs n'a pas été vérifiée.
- La liste des contrôles d'AIUC-1 et le texte de ses livraisons trimestrielles n'ont pas été lus. Les nombres de scénarios de test sont ceux qu'annonce l'éditeur. L'activité d'assurance d'AIUC relève de la section 36.5.
- Le caractère certifiable d'ISO/IEC 42001 et le statut de la liste OWASP reposent sur un billet de fournisseur [13], concordant avec les chapitres 31 et 35; les documents d'origine n'ont pas été lus.
- La spécification ATF sur GitHub, le guide de tests adverses de la CSA et la page [14] n'ont pas été lus.
- L'audit du 12 novembre 2026 a relu [1] (notice et texte), [3], [4], [5], [7], [10] et [11].
- Les lectures « pour un agent » de SP 800-207, les trois familles de règles, les quatre gestes de la section 32.2 et les cinq règles de la section 32.5 sont des déductions de ce chapitre.
