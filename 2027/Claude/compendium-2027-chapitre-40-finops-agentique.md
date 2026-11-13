# Chapitre 40 — FinOps agentique

*Question directrice : combien coûte un agent, et que rapporte-t-il ?*

> **Version 2 — 11 novembre 2026.** État de référence : communiqué State of FinOps 2026 (19 février 2026), page « FinOps for AI » de la FinOps Foundation (mise à jour du 28 octobre 2026), annonce de la Tokenomics Foundation (4 août 2026) et pages de prix des éditeurs affichées le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre, toutes lues pour ce chapitre; [3] et [10] sont des prépublications, [4] et [6] des billets de fournisseurs. Les montants sont en dollars américains. Chapitre audité et révisé le 12 novembre 2026.

Une licence logicielle a un prix. Un agent a une distribution de coûts : la même demande peut se régler en trois appels au modèle ou en trente, selon le chemin que prend le raisonnement. La facture dépend d'une trajectoire que personne n'a écrite d'avance, et elle arrive après les faits.

La discipline qui gère les dépenses infonuagiques, le FinOps, a pris acte du problème sans le résoudre. Presque toutes les pratiques FinOps gèrent désormais des dépenses d'IA [1], mais la FinOps Foundation ne publie aucun cadre propre aux agents, et sa page de référence constate qu'aucune méthode n'est admise pour imputer le coût d'une charge multi-agents [5].

Ce chapitre défend trois idées. Le coût d'un agent vient surtout du contexte relu à chaque tour, pas du texte produit : les leviers portent sur l'entrée. Le contrôle doit s'exercer pendant l'exécution, puisque la facture vient trop tard. Et l'unité de compte doit être le résultat réussi, car ni le prix du jeton ni la « résolution » facturée par un éditeur ne disent ce qu'un agent rapporte.

---

## 40.1 Coûts en cascade

### Le jeton facturé n'est pas le jeton saisi

L'inférence se paie au jeton, en entrée et en sortie. Ce que l'utilisateur écrit n'en est qu'une petite part : l'application y ajoute les instructions système, l'historique et le contenu récupéré [5]. Dans une boucle agentique, cet ajout se répète, car chaque tour renvoie au modèle l'historique de la tâche, augmenté du dernier résultat d'outil.

Un banc d'essai sur l'extraction de données dans 10 000 dépôts réglementaires en donne la mesure [3]. Dans un pipeline séquentiel, un document consomme 142 340 jetons d'entrée pour 3 820 jetons de sortie. L'entrée pèse plus de 97 % du volume, et la proportion est la même dans les trois autres architectures testées. Sur la page de prix d'Anthropic, le jeton de sortie coûte cinq fois le jeton d'entrée [7]; même à ce rapport, l'entrée reste de loin le premier poste.

### Trois multiplicateurs

**La boucle.** Anthropic rapporte, à partir de ses propres systèmes, qu'un agent consomme environ quatre fois plus de jetons qu'une conversation, et un système multi-agents environ quinze fois plus [6]. C'est une mesure interne publiée dans un billet d'ingénierie de juin 2025, pas un résultat reproduit.

**La topologie.** Dans le banc d'essai, le coût par document passe de 0,187 $ pour le pipeline à 0,430 $ pour l'architecture réflexive, soit 2,3 fois plus, avec le même modèle [3]. Le chapitre 16 détaille ce compromis entre coût et précision.

**Les outils.** Les définitions d'outils voyagent dans chaque requête et se paient en jetons d'entrée, comme les blocs d'appel et de résultat. S'y ajoute une instruction système propre à l'usage d'outils, de 286 à 804 jetons selon le modèle et le réglage `tool_choice` sur la page d'Anthropic [7]. Certains outils exécutés chez le fournisseur ont leur tarif : la recherche web y coûte 10 $ les 1 000 recherches. Un hôte branché sur des dizaines de serveurs MCP paie le catalogue entier à chaque tour, d'où l'intérêt de la découverte progressive des outils, que l'hôte ou la passerelle assure en attendant le protocole (chapitres 5 et 13).

### Les postes hors inférence

| Poste | Mécanisme |
|---|---|
| Durée d'exécution | Facturation au temps de session : 0,08 $ l'heure active pour les agents gérés d'Anthropic, en sus des jetons [7] |
| Résidence des données | Multiplicateur de 1,1 sur tous les jetons quand l'inférence est restreinte aux États-Unis, pour les modèles 4.6 et suivants [7] (chapitre 37) |
| Nouveaux essais | Chaque replanification ou réémission consomme des jetons (chapitre 18) |
| Évaluation | Les juges automatiques sont eux-mêmes des appels au modèle (chapitre 33) |
| Révision humaine | Temps des personnes qui valident ou corrigent (chapitre 22) |

La Tokenomics Foundation, créée sous l'égide de la Linux Foundation, annonce un modèle de référence du coût total de l'IA et un cadre, Big-T, pour classer la complexité en jetons d'une charge avant de choisir un modèle [11]. Ce sont des livrables annoncés; aucune spécification publiée n'a été lue.

---

## 40.2 Attribution des coûts

### Un périmètre acquis, une méthode absente

L'enquête State of FinOps 2026, menée auprès de 1 192 répondants dont les organisations totalisent plus de 83 milliards de dollars de dépenses infonuagiques annuelles, établit que 98 % des pratiques gèrent des dépenses d'IA, contre 31 % deux ans plus tôt [1]. Le FinOps de l'IA y est la première priorité à venir. Le communiqué ne mentionne toutefois ni les agents ni l'IA agentique.

La page « FinOps for AI » de la fondation nomme les obstacles [5]. Les nouvelles références de facturation et les factures directes des fournisseurs de modèles arrivent souvent sans étiquettes. Pour les charges multi-agents, aucune méthode n'est admise.

### Ce qu'il faut pour imputer

Faute de méthode établie, l'imputation se construit avec trois éléments décrits dans d'autres chapitres; leur assemblage est une synthèse, pas une norme.

**Une clé.** Chaque appel au modèle porte l'identité de l'agent (chapitre 29), l'identifiant de l'exécution et le centre de coûts. Sans identité distincte, tous les agents d'une plateforme se confondent sous une même clé d'API.

**Un point de mesure.** La trace est la source naturelle : les conventions OpenTelemetry prévoient des attributs de consommation de jetons, encore instables (chapitre 33). La passerelle en est une autre, puisque le trafic vers les modèles y passe (chapitre 24). La politique `llm-token-limit` d'Azure API Management, par exemple, tient un compteur par clé calculée et peut renvoyer le nombre de jetons consommés dans un en-tête de réponse [12].

**Un format.** FOCUS, la spécification ouverte de données de facturation, est produite nativement par toutes les grandes plateformes infonuagiques, et ses utilisateurs réclament son extension aux charges d'IA [1]. La Tokenomics Foundation annonce une télémétrie de coût des jetons dans FOCUS 1.5 et les versions suivantes [11]. Ce point n'a pas été vérifié dans la spécification.

### Trois difficultés propres aux agents

**Le coût partagé.** Un orchestrateur sert plusieurs demandes; un sous-agent sert plusieurs orchestrateurs. Le cache de prompts complique le calcul : la première requête paie l'écriture à prix majoré, les suivantes lisent à prix réduit [7]. Imputer au coût réel pénalise le premier appelant.

**Le coût délégué.** Quand un agent en appelle un autre hors de l'organisation (chapitre 6), le coût de l'agent distant n'apparaît que dans le prix qu'il facture; un rapprochement à trois voies contrôle cette facture (chapitre 45).

**L'unité.** Le coût par jeton ne dit rien à un gestionnaire. La Tokenomics Foundation propose d'exprimer le coût de service par appel plutôt que par jeton [11]; la FinOps Foundation liste le coût par inférence et le coût par résultat réussi [5]. Pour un agent, l'unité utile est la tâche, puis le résultat (section 40.5).

Une règle prudente en découle : montrer d'abord les coûts aux équipes sans les refacturer, et ne refacturer qu'une fois la clé d'imputation fiable.

---

## 40.3 Garde-fous à l'exécution

La FinOps Foundation range les boucles d'agents parmi les anomalies à surveiller [5]. Sa consigne pour les projets débutants : fixer d'avance des limites de coût et de temps. Une alerte de facturation n'y suffit pas, car elle suit la dépense. Le plafond doit se trouver sur le chemin de l'appel.

### Une défense en couches

| Garde-fou | Où | Ce qu'il arrête | Limite |
|---|---|---|---|
| Plafond d'itérations | Boucle de l'agent | La boucle sans fin | Ne borne pas la taille d'un tour (chapitre 17) |
| Débit de jetons par minute | Passerelle | Les pointes | Ignore la dépense cumulée |
| Quota de jetons par période | Passerelle | Le dépassement d'enveloppe | Comptage imparfait |
| Budget d'appels d'outils | Passerelle MCP | Le martèlement d'un système | Compte des appels, pas des dollars (chapitre 24) |
| Limite de paiement | Portefeuille ou passerelle | L'achat non voulu | Absente de x402 et de MPP; à poser dans un mandat ou en amont (chapitre 10) |
| Arrêt d'urgence | Plan de contrôle | Tout | Brutal (chapitre 34) |

### Ce qu'un quota garantit vraiment

La politique d'Azure API Management accepte un débit par minute, un quota par période (de l'heure à l'année), ou les deux. Le dépassement du débit renvoie un code 429; celui du quota, un code 403 [12].

Quatre réserves l'accompagnent. Sans estimation préalable, la requête qui franchit la limite part quand même : le dépassement se constate à la réponse, et seules les requêtes suivantes sont bloquées. Des requêtes concurrentes peuvent excéder temporairement le plafond. En flux continu, les jetons sont estimés et non comptés. Enfin, chaque passerelle tient son compteur : dans un déploiement multirégional, les décomptes ne s'additionnent pas.

Un quota est donc un frein, pas un mur. Un système multi-agents qui lance vingt branches en parallèle peut dépasser son enveloppe avant le retour du premier décompte. Les plafonds budgétaires d'agentgateway et de MuleSoft (chapitre 24) n'ont pas été lus ici.

### Trois choix de conception

**La clé du compteur.** L'exemple d'Azure indexe le débit sur l'adresse IP et le quota sur l'abonnement [12]. Pour des agents, la clé pertinente est l'identité de l'agent, combinée à la tâche.

**L'échelle du budget.** Un quota mensuel protège le budget annuel, pas contre une tâche qui dérape. Il faut aussi un plafond par exécution, proportionné à la valeur de la tâche.

**Le comportement à l'épuisement.** Trois réponses existent : refuser, basculer vers un modèle moins cher, ou s'en remettre à un humain (chapitre 22). Une tâche interrompue à mi-chemin a déjà consommé ses jetons; vérifier le solde avant une étape chère vaut mieux que couper après, et une tâche arrêtée doit pouvoir reprendre sans rejouer ses effets (chapitre 18).

---

## 40.4 Modèles de tarification : au siège, à la consommation, au résultat

Deux étages de prix coexistent. L'entreprise qui construit ses agents achète de l'inférence. Celle qui achète des agents empaquetés se voit proposer trois modèles, parfois par le même éditeur.

### L'inférence

La FinOps Foundation recense des formules reprises de l'infonuagique [5] : à la demande, remises sur engagement, capacité provisionnée (un débit fixe, facturé qu'il serve ou non), traitement par lots à rabais, abonnement, paliers de volume.

### Les agents empaquetés

Le tableau reprend les prix affichés par les éditeurs à la date de rédaction. Ce sont des prix de liste, négociables.

| Éditeur | Unité facturée | Prix affiché | Ce que l'unité recouvre |
|---|---|---|---|
| Salesforce Agentforce [8] | Action | 500 $ les 100 000 crédits; 20 crédits par action, soit 0,10 $ | Une action de l'agent, réussie ou non |
| Salesforce Agentforce [8] | Conversation | 2 $ | Une conversation avec un client |
| Salesforce Agentforce [8] | Siège | 125 $ par utilisateur par mois | Usage illimité par les employés |
| Intercom Fin [9] | Résultat (*outcome*) | À partir de 0,99 $ | Voir ci-dessous |
| Zendesk [4] | Résolution automatisée | 1,50 $ | Résolution sans humain, vérifiée par Zendesk |

Chez Salesforce, crédits et conversations ne peuvent pas coexister dans une même organisation, et les crédits inutilisés ne sont pas reportés [8]. Le prix de Zendesk est cité dans la foire aux questions d'un billet de l'éditeur, non dans une grille tarifaire [4].

### Qui porte le risque

Zendesk résume lui-même le compromis [4]. Au siège, le client risque de payer des licences inutilisées. À la consommation, il risque de voir les coûts monter sans résultat garanti. Au résultat, le risque se déplace vers la définition et la vérification de ce résultat. Forrester note de son côté que le passage du siège à la consommation distend le lien entre l'usage et les résultats d'affaires, et rapporte chez ses clients une forte incertitude sur les prix [2].

### Le résultat est une définition contractuelle

La tarification au résultat aligne le prix sur la valeur si le résultat est bien défini. Or les définitions lues divergent.

Chez Intercom, un résultat est compté quand le client confirme la résolution, mais aussi quand il ne demande rien de plus, ou quand l'agent mène une procédure à terme, transferts compris [9]. Le silence du client vaut succès. Chez Zendesk, seule la résolution « vérifiée » est facturable, et c'est Zendesk qui évalue les conversations; une conversation se clôt après deux heures par défaut en messagerie, prolongeables à soixante-douze, et soixante-douze heures après le premier courriel [4]. La page ne décrit pas de procédure de contestation propre à l'éditeur; elle conseille d'en prévoir une au contrat.

Dans les deux cas, le fournisseur mesure ce qu'il facture. Zendesk range lui-même les différends sur la définition ou la vérification du résultat parmi les risques de ce modèle [4].

Trois conséquences en découlent. La définition du résultat, sa vérification et un droit d'audit figurent au contrat (chapitre 36). Le client mesure lui-même la résolution réelle, par exemple par les recontacts sur le même sujet. Et la comparaison entre offres se fait en ramenant chaque prix à la même unité, le cas réellement réglé, que l'éditeur facture l'action, la conversation ou la résolution.

---

## 40.5 Mesurer la valeur

### Le constat

Les organisations augmentent leurs dépenses d'IA plus vite qu'elles n'apprennent à en mesurer les résultats : c'est le diagnostic de Forrester au sortir de la conférence FinOps X 2026 [2]. Ses analystes demandent de relier la consommation de jetons aux revenus, à la productivité et aux résultats pour les clients. L'enquête State of FinOps va dans le même sens : la gestion de la valeur de l'IA est la compétence la plus recherchée, et plusieurs organisations demandent à leurs équipes de financer l'IA par des gains d'efficacité [1].

Le chapitre 4 rapporte un obstacle plus élémentaire : selon l'étude MAP, 39 % seulement des répondants comparent leur agent à une solution non agentique. Sans base de comparaison, la valeur ne se démontre pas.

### Le coût par résultat réussi

L'indicateur le plus utile de la page de la FinOps Foundation est le coût des résultats qui atteignent la barre de qualité [5] : le coût total des exécutions, ratées comprises, divisé par le nombre de résultats conformes.

Le banc d'essai financier permet de l'illustrer [3]. L'exactitude par document, soit la part des documents dont tous les champs sont corrects, y va de 0,648 à 0,758 (chapitre 16).

| Architecture | Coût par document | Exactitude par document | Coût par document entièrement correct |
|---|---|---|---|
| Pipeline séquentiel | 0,187 $ | 0,648 | 0,29 $ |
| Fan-out | 0,221 $ | 0,672 | 0,33 $ |
| Hiérarchique | 0,261 $ | 0,718 | 0,36 $ |
| Réflexive | 0,430 $ | 0,758 | 0,57 $ |

La dernière colonne est un calcul fait pour ce chapitre, non un résultat de l'article. Elle montre deux choses. Le coût par succès dépasse le coût par tâche de 32 % à 54 %. Et le classement ne dit rien tant qu'on ignore le coût d'un document fautif : si sa correction par une personne coûte quelques dollars, l'architecture la plus précise devient la moins chère. La valeur se décide dans ce que coûte l'erreur.

### La valeur de la tâche borne l'architecture

Anthropic tire de ses mesures une règle simple : un système multi-agents ne se justifie que pour des tâches dont la valeur paie le surcroît de performance [6]. Dans l'une de ses évaluations, la consommation de jetons expliquait à elle seule 80 % de la variance de performance. Dépenser plus de jetons achète de la performance; reste à savoir ce que vaut le point supplémentaire.

### Deux précautions

**Un rendement ne vaut que ses intrants**, prévient la FinOps Foundation [5]. Un gain de productivité déclaré n'est pas une économie constatée.

**La part de travail accomplie sans intervention humaine**, mesure que la Tokenomics Foundation annonce vouloir normaliser [11], dit ce que l'agent fait seul, pas s'il le fait bien. Elle se lit avec le succès vérifié (chapitre 34).

---

## 40.6 Leviers : routage de modèles, cache, décomposition

Puisque l'entrée domine, les leviers rentables agissent sur ce que le modèle relit et sur le modèle qui le lit. Les chiffres du banc d'essai portent sur l'architecture hiérarchique, à partir de 0,261 $ par document et d'un F1 de 0,929 [3].

| Levier | Effet mesuré | Contrepartie |
|---|---|---|
| Cache de prompts | Lecture à 0,1 fois le prix d'entrée sur la plupart des modèles, 0,05 ou 0,025 fois sur certains récents; écriture à 1,25 fois (cinq minutes) ou 2 fois (une heure) [7] | Un changement en tête du préfixe annule le gain (chapitre 13) |
| Traitement par lots | Rabais de 50 % en entrée et en sortie, cumulable avec le cache [7] | Asynchrone; exclu des sessions d'agents gérés |
| Cache sémantique | 0,171 $ (−34,5 %), F1 0,924 [3] | Réponse périmée ou mal appariée |
| Routage à deux niveaux | 0,127 $ (−51,3 %), F1 0,912 [3] | Perte de précision |
| Relance adaptative | 0,247 $ (−5,4 %), F1 inchangé [3] | Gain modeste |
| Les trois précédents combinés | 0,148 $, F1 0,924, 30,2 s contre 46,2 s [3] | Complexité d'exploitation |

### Le cache d'abord

Le cache de prompts est le seul levier sans effet sur la qualité : le modèle reçoit le même contexte. D'après la page d'Anthropic, il devient rentable dès la première relecture pour une durée de cinq minutes, et dès la deuxième pour une heure [7]. Une boucle agentique, qui renvoie le même préfixe à chaque tour, en est le cas d'usage idéal. La condition est de construction : le stable en tête, le variable à la fin. C'est pourquoi MCP recommande aux serveurs un ordre d'outils déterministe (chapitre 5).

### Le routage ensuite

Le routage attribue à chaque étape un modèle à sa mesure. Le banc d'essai en montre le gain et le prix : le coût baisse de moitié, le F1 perd 1,7 point [3]. Tout confier à un modèle léger ramène le coût à 0,044 $, mais le F1 tombe à 0,843. Une prépublication plus ancienne, RouteLLM, annonce des coûts réduits de plus de moitié dans certains cas, sans perte de qualité sur ses bancs d'essai [10].

La FinOps Foundation propose l'indicateur correspondant, l'adéquation du modèle : la part des requêtes envoyées à un modèle plus capable et plus cher que nécessaire [5]. La passerelle est le lieu naturel de ce routage, activé par classe de tâche (chapitre 44); distiller un petit modèle pour une tâche étroite prolonge le levier (chapitre 47).

### La décomposition enfin

Décomposer, c'est réduire ce que chaque appel relit. Trois gestes y contribuent : confier à du code déterministe ce qui n'exige pas de raisonnement (chapitre 17), donner à chaque sous-agent un contexte étroit (chapitre 13), et choisir la topologie la moins chère qui atteint la barre de qualité (chapitre 16). La décomposition n'est pas gratuite : dans le banc d'essai, le fan-out consomme 18 % de jetons de plus que le pipeline, ses branches relisant des contextes qui se chevauchent [3], et chaque frontière entre agents ajoute un risque de coordination (chapitre 21).

Ces chiffres viennent d'une prépublication, sur un seul domaine, aux tarifs de janvier 2025 [3]. Le sens des compromis est utilisable; les valeurs exactes ne se transposent pas.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Unité de compte | Coût par résultat réussi | Pilote sans barre de qualité : coût par exécution |
| Clé d'imputation | Identité d'agent, exécution, centre de coûts | Agent unique : clé d'API dédiée |
| Point de mesure | Passerelle et traces, rapprochées de la facture | Très petit parc : rapports du fournisseur |
| Refacturation | Affichage des coûts seulement | Clé d'imputation éprouvée |
| Plafonds | Par exécution et par période, sur l'identité de l'agent | — |
| Épuisement du budget | Vérification avant l'étape chère, puis recours à un humain | Faible enjeu : bascule vers un modèle moins cher |
| Achat d'un agent | Consommation plafonnée | Résultat, si le client peut le vérifier; siège, si l'usage est massif et régulier |
| Ordre des leviers | Cache de prompts, lots, routage, topologie | Tâche interactive : pas de lots |
| Système multi-agents | Seulement si la valeur de la tâche paie le surcoût | — |

---

## Points à retenir

- Le coût d'un agent est une distribution, pas un prix. Il dépend du nombre de tours, de la topologie et des outils chargés.
- L'entrée domine : dans le banc d'essai lu, plus de 97 % des jetons sont relus, non produits.
- Presque toutes les pratiques FinOps gèrent des dépenses d'IA, mais aucun cadre FinOps propre aux agents n'existe, et l'imputation multi-agents n'a pas de méthode admise.
- L'imputation exige une identité d'agent, un point de mesure et un format commun. Les deux derniers reposent sur des standards instables ou seulement annoncés.
- Un quota de jetons à la passerelle est un frein, pas un mur : il se constate après coup et cède sous la concurrence. Il faut aussi un plafond par exécution.
- La tarification au résultat déplace le risque vers la définition du résultat, que le fournisseur mesure lui-même.
- La valeur se mesure au coût par résultat réussi, comparé à une base de référence et au coût de l'erreur.
- Le cache de prompts vient en premier, car il ne touche pas à la qualité. Le routage réduit davantage le coût, au prix d'une perte de précision à mesurer.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Linux Foundation — State of FinOps 2026, communiqué du 19 février 2026](https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1)
2. [Forrester — Dollars and Sense at FinOps X 2026, billet du 23 juin 2026](https://www.forrester.com/blogs/dollars-and-sense-at-finops-x-2026-is-ai-value-management-bigger-than-finops/)
3. [Kulkarni et Kulkarni — Benchmarking Multi-Agent LLM Architectures for Financial Document Processing (arXiv 2603.22651v1)](https://arxiv.org/html/2603.22651v1) — prépublication.
4. [Zendesk — Outcome-based pricing, mise à jour du 29 octobre 2026](https://www.zendesk.com/blog/ai/agentic-ai/outcome-based-pricing/) — billet de l'éditeur.
5. [FinOps Foundation — FinOps for AI Overview, mise à jour du 28 octobre 2026](https://www.finops.org/wg/finops-for-ai-overview/)
6. [Anthropic — How we built our multi-agent research system, 13 juin 2025](https://www.anthropic.com/engineering/multi-agent-research-system) — billet du fournisseur.
7. [Anthropic — Pricing, documentation de la plateforme](https://platform.claude.com/docs/en/about-claude/pricing)
8. [Salesforce — Agentforce Pricing](https://www.salesforce.com/agentforce/pricing/)
9. [Intercom — Pricing](https://www.intercom.com/pricing)
10. [Ong et coll. — RouteLLM: Learning to Route LLMs with Preference Data (arXiv 2406.18665)](https://arxiv.org/abs/2406.18665) — prépublication; résumé seulement.
11. [Linux Foundation — lancement de la Tokenomics Foundation, communiqué du 4 août 2026](https://linuxfoundation.org/press/linux-foundation-launches-the-tokenomics-foundation-to-define-the-economics-and-roi-of-ai-value)
12. [Microsoft Learn — politique `llm-token-limit` d'Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/llm-token-limit-policy)

Sources secondaires : aucune. Le constat de l'étude MAP vient du chapitre 4; les plafonds d'agentgateway et de MuleSoft, du chapitre 24.

## Limites de ce chapitre

- Les pages ont été lues au moyen d'un outil d'extraction; une nuance de formulation peut avoir échappé. L'audit a relu [1], [3], [4], [5], [7], [9], [11] et [12], pas [2], [6], [8] ni [10]. Les prix des éditeurs sont des prix de liste relevés le 11 novembre 2026, à revérifier avant publication; la page de Salesforce ne porte pas de date.
- Le rapport State of FinOps 2026 n'a été lu que par son communiqué. La spécification FOCUS, le rapport Forrester AI Value Matrix et les livrables de la Tokenomics Foundation n'ont pas été lus; ils sont présentés comme annoncés.
- L'« étude sur la génération de workflows » citée par la table des matières n'a pas été retrouvée ni utilisée.
- Le résumé et les tableaux du banc d'essai [3] se contredisent par endroits : le résumé donne la configuration optimisée à 1,15 fois le coût du pipeline, les tableaux à 0,79 fois, et l'article dit ailleurs le fan-out économe en jetons. Ses coûts en dollars n'ont pas pu être rapprochés de ses décomptes de jetons; les prix de liste du modèle utilisé relèvent ici de la connaissance générale. Le coût par document entièrement correct et la part des jetons d'entrée sont des calculs faits pour ce chapitre.
- Les multiples de consommation [6] sont des mesures internes d'un fournisseur, datées de 2025; aucune mesure indépendante n'a été trouvée.
- Un seul fournisseur de modèles (Anthropic) et une seule passerelle (Azure API Management) ont été lus. Les règles de cache, de lots et de quotas diffèrent ailleurs.
- La proposition d'imputation (40.2), les choix de conception (40.3), les conséquences contractuelles (40.4) et l'ordre des leviers (40.6) sont des synthèses de l'auteur, non des pratiques documentées.
