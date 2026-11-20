# 7 Orchestration

L’orchestration décide qui fait quoi, dans quel ordre, avec quel état et quelles garanties en cas d’échec. Ce chapitre fixe la règle de départ, soit la configuration la plus simple qui répond au besoin, puis les huit patrons autorisés et la façon de choisir parmi eux. Il impose enfin les mécanismes qui rendent une orchestration digne de la production : exécution durable, saga et compensation, idempotence, contexte minimal entre agents, résilience et coupe-circuit.

## 7.1 Commencer simple : ce que disent les données probantes

Cette section résume les mesures publiées sur les systèmes multiagents et en tire la règle de départ du cadre : un flux déterministe ou un agent unique bien outillé, sauf preuve mesurée du contraire.

### Des gains réels, sur des tâches précises

Anthropic rapporte que son système de recherche multiagent, formé d’un agent principal Claude Opus 4 et de sous-agents Claude Sonnet 4, a surpassé de 90,2 % un agent unique Claude Opus 4 sur son évaluation interne de recherche. Le gain est le plus marqué pour les requêtes « en largeur », qui poursuivent plusieurs pistes indépendantes à la fois; il s’agit d’une évaluation interne, et non d’un banc d’essai public**[17]**.

L’étude de Google Research « Towards a Science of Scaling Agent Systems » (Kim, Gu, Park et coll.) nuance fortement ce résultat. Selon le billet de Kim et Liu du 28 janvier 2026 (180 configurations, quatre bancs d’essai, cinq architectures, trois familles de modèles), l’architecture centralisée gagne 80,9 % sur une tâche parallélisable (Finance-Agent), alors que chaque variante multiagent dégrade la performance de 39 à 70 % sur une tâche séquentielle (PlanCraft)**[273]**. La version 3 de l’article (8 avril 2026; 260 configurations, six bancs d’essai) donne une plage de +80,8 % à −70,0 % et observe que les gains de la coordination diminuent lorsque l’agent unique est déjà performant**[274]**.

### Des coûts et des risques qui croissent avec le nombre d’agents

- **Jetons.** Selon Anthropic, un agent consomme environ 4 fois plus de jetons qu’une conversation, et un système multiagent environ 15 fois plus; sur le banc d’essai BrowseComp, le volume de jetons explique à lui seul 80 % de la variance de performance**[17]**. Un article d’Anthropic du 23 janvier 2026 situe le surcoût habituel du multiagent entre 3 et 10 fois les jetons d’un agent unique pour une tâche équivalente**[275]**.
- **Erreurs.** Selon le billet de Google Research du 28 janvier 2026, chiffres absents du résumé de la version 3 de l’article, l’amplification des erreurs peut atteindre 17,2 fois dans des systèmes multiagents indépendants, contre 4,4 fois lorsqu’un orchestrateur central sert de goulot de validation**[273]**.
- **Cohérence.** Cognition soutient qu’il faut partager le contexte complet (les traces de l’agent, pas de simples messages), car chaque action porte des décisions implicites; des sous-agents mal informés prennent des décisions contradictoires. Cette prise de position d’ingénierie recommande par défaut un agent linéaire à fil unique**[276]**. LangChain réconcilie les deux positions : le multiagent convient mieux aux tâches de lecture, faciles à paralléliser, qu’aux tâches d’écriture, où des écritures concurrentes se contredisent**[277]**.
- **Limites d’emploi.** Anthropic juge que les tâches où tous les agents doivent partager le même contexte, ou qui comportent de nombreuses dépendances, conviennent mal au multiagent, et que le surcoût ne se justifie que si la valeur de la tâche le paie**[17]**.

### Une consigne convergente des éditeurs

Le Centre d’architecture Azure prescrit le niveau de complexité le plus bas qui répond au besoin de façon fiable : appel direct au modèle, puis agent unique doté d’outils, puis orchestration multiagent, seulement si l’agent unique échoue pour cause de complexité d’invite, de surcharge d’outils ou d’exigences de sécurité**[9]**. Anthropic recommande la solution la plus simple possible**[6]** et OpenAI, de maximiser d’abord les capacités d’un agent unique**[66]**.

**À RETENIR**

Le multiagent est un outil de spécialiste, pas une architecture par défaut. Il rapporte surtout sur des tâches de lecture parallélisables et à forte valeur; il coûte de 3 à 10 fois plus de jetons et peut dégrader les tâches séquentielles. Le cadre exige donc une preuve mesurée avant d’ajouter des agents (PRIN-08).

`EXIG-ORC-01` **· DOIT**

**Configuration la plus simple justifiée**

Chaque agent ou système d’agents **DOIT** inscrire à sa fiche (annexe B) pourquoi les options plus simples que le patron retenu, prises de la plus simple à la plus complexe parmi le code ou la règle métier, l’appel direct au modèle, le flux déterministe et l’agent unique outillé, ne répondent pas au besoin. La revue d’architecture **DOIT** refuser un patron dont la justification manque.

Pourquoi : chaque niveau de complexité ajoute coordination, latence et coût**[9]**.

`EXIG-ORC-02` **· DOIT**

**Preuve mesurée avant le multiagent**

Une topologie à plusieurs agents **DOIT** être comparée, sur le même jeu d’évaluation (section 10.4), à une base de référence à agent unique : taux de réussite, jetons par exécution, latence et coût par tâche réussie. Elle n’est retenue que si son taux de réussite n’est pas inférieur à celui de la base de référence (borne inférieure de l’intervalle de confiance à 95 % de la différence supérieure à l’opposé d’une marge de non-infériorité déclarée à la fiche) et si son gain, valorisé par une valeur monétaire déclarée par tâche réussie, couvre le surcoût mesuré; la comparaison déclare la taille d’échantillon, le nombre de répétitions, la statistique et la règle de décision (section 10.4). Sont visés les patrons 3 à 7 du tableau 24 et la variante encadrée, dès que plus d’un composant choisit lui-même ses actions au moyen d’un modèle; un routeur sans modèle ou un évaluateur réduit à une invite distincte n’en fait pas un système multiagent. La comparaison est versée à la fiche de l’agent, avec la grille d’homologation (annexe A).

Pourquoi : les gains publiés dépendent fortement de la tâche et le surcoût en jetons peut atteindre un ordre de grandeur**[273, 275]**.

## 7.2 Patrons autorisés

Le cadre autorise huit patrons, combinables entre eux, et une variante encadrée (voir la figure 11 et le tableau 24). Un patron décrit la topologie de la coordination; il ne fixe pas le niveau d’autonomie, qui se déclare séparément (chapitre 8).

> **[Figure]**
> - 1 · Flux déterministe
> - code agent valide code
> - Patron par défaut. Le code fixe le chemin; le modèle traite les étapes non structurées.
> - 2 · Chaîne séquentielle
> - étape A étape B étape C
> - Sortie typée de A entrée de B; contrôle de schéma entre étapes (points orangés).
> - 3 · Routage et transfert
> - routeur
> - spécialiste 1
> - spécialiste 2
> - spécialiste 3
> - Qualifie l’intention puis cède la session et le contexte utile; le routeur se retire.
> - 4 · Parallélisation
> - répart.
> - agent
> - agent
> - agent
> - fusion
> - Sectionnement (sous-tâches indépendantes) ou vote; règle de fusion explicite; coût × N.
> - 5 · Orchestrateur et exécutants
> - orchestrateur
> - spéc. A spéc. B spéc. C
> - Plan dynamique, délégation A2A, consolidation des artefacts; deux niveaux au plus.
> - 6 · Évaluateur-optimiseur
> - producteur évaluateur
> - Vérificateur déterministe d’abord
> - 7 · Chorégraphie événementielle
> - bus d’événements (CloudEvents)
> - agent agent agent
> - agent agent
> - Pas de chef d’orchestre; compteur de sauts, trace et saga obligatoires.
> - 8 · Agent unique outillé
> - raisonner
> - agir observer
> - outil
> - outil
> - outil
> - Boucle ouverte bornée (étapes, budget, délai); base de référence avant tout multiagent.
> - ≤ 3 itérations (production + évaluation)
> - (compilateur, règles), puis modèle ou invite distincts; escalade au plafond.
> - →

***Figure 11 — Huit patrons d’orchestration autorisés.** Chaque vignette montre la topologie d’un patron et sa règle principale; les points orangés signalent un contrôle de schéma entre étapes. Pour l’évaluateur-optimiseur, l’évaluateur est un modèle ou une invite distincts de ceux du producteur (EXIG-ORC-05). Les patrons se combinent : un flux déterministe peut contenir une étape orchestrée, qui publie à son tour un événement. Source : cadre CRE-IA-2026-01, d’après Anthropic (2024) et le Centre d’architecture Azure (2026).*

Le catalogue s’appuie sur deux références de premier rang. Anthropic distingue les flux de travail, où le modèle et les outils suivent des chemins de code prédéfinis (enchaînement d’invites, routage, parallélisation, orchestrateur-travailleurs, évaluateur-optimiseur), des agents, où le modèle dirige lui-même son processus**[6]**. Le Centre d’architecture Azure décrit cinq orchestrations : séquentielle, concurrente, clavardage de groupe, transfert et magnétique**[9]**; la documentation de Microsoft Agent Framework indique que ce dernier patron est conçu à partir de Magentic-One, le système décrit par Fourney et coll.**[278, 279]**. Le cadre y ajoute la

chorégraphie événementielle, absente des deux catalogues, et fait du flux déterministe à étapes agentiques le patron par défaut.

*Tableau 24 — Huit patrons d’orchestration autorisés et variante encadrée*

| **Patron** | **Fonctionnement** | **Quand l’utiliser** | **Point de vigilance** | **Correspondance** |
| --- | --- | --- | --- | --- |
| **1. Flux déterministe** | Un moteur de flux fixe l’ordre et les embranchements; certaines étapes appellent un modèle ou un agent borné pour traiter l’information non structurée. | Processus connus, réglementés ou audités. Patron par défaut. | Rigide quand les cas varient beaucoup; chaque étape agentique a un contrat de sortie validé. | Anthropic : flux de travail; patron par défaut par choix du cadre. |
| **2. Chaîne séquentielle** | Chaque étape transforme la sortie typée de la précédente. | Tâche décomposable en étapes fixes (extraire, vérifier, rédiger). | Erreurs propagées et latences cumulées : validation de schéma et délai par étape. | Azure : séquentiel. Anthropic : enchaînement d’invites. |
| **3. Routage et transfert** (*handoff*) | Un routeur qualifie l’intention, puis cède la session et le contexte utile à un spécialiste déclaré; il se retire. | Triage, service à la clientèle par domaine, latence prioritaire. | Liste fermée de destinataires; le transfert porte le mandant, pas tout l’historique; aucun transfert en boucle. | Azure : transfert. Anthropic : routage. OpenAI : décentralisé. |
| **4. Parallélisation** | Un répartiteur lance des sous-tâches indépendantes (sectionnement) ou la même tâche plusieurs fois (vote), puis fusionne. | Analyse multisource, vérification croisée, garde-fou exécuté en parallèle de la tâche, dont la fusion attend le verdict (EXIG-ORC-07). | Jetons multipliés par le nombre de branches, pointes de charge; règle de fusion explicite. | Azure : concurrent. Anthropic : parallélisation. |
| **5. Orchestrateur et exécutants** | Un agent planifie dynamiquement, délègue à des spécialistes (A2A, ou appel interne entre sous-agents d’un même processus), puis consolide leurs artefacts. | Tâches ouvertes dont les sous-tâches ne sont pas connues d’avance. | Coût et latence élevés; l’orchestrateur est un point unique de défaillance; deux niveaux au plus. | Azure : magnétique (variante). Anthropic : orchestrateur-travailleurs. OpenAI : gestionnaire. |
| **6. Évaluateur-optimiseur** | Un producteur propose; un évaluateur distinct juge selon des critères explicites et renvoie jusqu’à l’acceptation. | Qualité vérifiable : code, rédaction réglementée, conformité. | Trois itérations au plus, puis escalade; vérificateur qui déclare victoire trop tôt. | Azure : boucle producteur-vérificateur. Anthropic : évaluateur-optimiseur. |
| **7. Chorégraphie événementielle** | Les agents réagissent aux événements d’un bus et publient les leurs, sans chef d’orchestre. | Processus interdomaines faiblement couplés, gros volumes, agents ambiants. | Vue d’ensemble difficile, risque de cycles : trace et compteur de sauts obligatoires; saga dès que des effets touchent plusieurs systèmes d’enregistrement. | Ajout du cadre; saga par chorégraphie chez Microsoft. |
| **8. Agent unique outillé** | Un agent boucle seul « raisonner, agir, observer » avec ses outils, sous plafonds. | Requêtes variées dans un même domaine; base de référence avant tout multiagent. | Surcharge d’outils, contexte qui enfle; conditions d’arrêt obligatoires. | Azure : agent unique doté d’outils. Anthropic : agent. |
| **Variante encadrée : clavardage de groupe et débat** | Plusieurs agents échangent dans un fil commun, sous un gestionnaire qui donne la parole. | Décisions où un contre-examen vaut plus que la latence. | Trois agents participants au plus, plus un gestionnaire (EXIG-ORC-06), plafond de tours; propagation d’idées entre agents. | Azure : clavardage de groupe. |

Les correspondances Azure des patrons 6 (boucle producteur-vérificateur) et 8 (agent unique doté d’outils) sortent des cinq orchestrations que décrit le Centre d’architecture Azure; elles ne sont données qu’à titre de rapprochement.

Patron et autonomie sont deux dimensions distinctes : un système multiagent peut combiner des agents de niveaux différents**[83]**. Un orchestrateur plafonné à N3 peut ainsi déléguer à un exécutant plafonné à N1. Chaque action est soumise au contrôle le plus strict de la chaîne : le niveau d’autonomie et la classe les plus contraignants entre l’initiateur et l’agent qui agit, combinés au palier de l’outil appelé (section 8.4). Ces valeurs voyagent dans le contexte de délégation (EXIG-ORC-23) et s’imposent à l’exécutant, et la passerelle les vérifie (EXIG-AUT-10) : un exécutant N3 de classe modérée n’écrit pas seul pour un initiateur N1 ou de classe élevée.

### Règles propres à certains patrons

**Orchestrateur et exécutants.** Le cadre limite la délégation à deux niveaux : l’orchestrateur, puis ses exécutants. Ce plafond est un choix du cadre, appuyé indirectement par la mesure d’amplification des erreurs de Google Research. Salesforce impose une contrainte équivalente, dans un produit précis : l’orchestration multiorganisation d’Agentforce n’admet qu’un saut de délégation (agent A vers agent B, jamais A vers B vers C), soit deux agents en chaîne (un saut; le plafond par défaut de l’EXIG-ORC-04 est de deux sauts, soit trois agents)**[49]**. Il s’agit d’une contrainte de produit, et non d’une règle générale.

**Évaluateur-optimiseur.** Microsoft exige un plafond d’itérations, des critères d’acceptation clairs et un comportement de repli défini, comme l’escalade vers un humain**[9]**; la valeur de trois itérations est un choix du cadre. Anthropic décrit l’écueil de la « victoire prématurée » : un sous-agent vérificateur exécute quelques tests et déclare le succès. Les parades sont des critères concrets, des vérifications exhaustives et des tests négatifs**[275]**.

**Clavardage de groupe et débat.** Microsoft recommande de limiter le clavardage de groupe à trois agents**[9]**. Une prépublication d’août 2026 (« Mind Viruses », Papadopoulos et coll., Anthropic Fellows Program et EPFL) montre que des idées ou des objectifs peuvent se propager d’agent en agent, dans une petite équipe d’agents de programmation et dans une chaîne d’agents dont le contexte est effacé entre les sessions. Un bref avertissement dans l’invite système y a conféré une immunité « quasi totale », mais la propagation varie selon le modèle, les consignes initiales et la topologie, et les auteurs jugent le risque réel mais actuellement limité**[280]**. Le cadre admet cet avertissement comme mesure complémentaire peu coûteuse, jamais comme contrôle suffisant.

**Parallélisation.** Le patron réduit le temps total, au prix de pointes de consommation lorsque plusieurs agents appellent les modèles en même temps, et il exige une logique de résolution des conflits**[9]**. Anthropic

rapporte que la parallélisation des sous-agents et des appels d’outils a réduit jusqu’à 90 % le temps de recherche pour les requêtes complexes**[17]**.

**Chorégraphie événementielle.** Pour une saga, la chorégraphie évite tout point unique de défaillance, mais elle complique le suivi et les tests d’intégration et expose à des dépendances cycliques**[67]**. Les contrôles d’enveloppe (trace, compteur de sauts, file de lettres mortes) relèvent de la section 6.7.

`EXIG-ORC-03` **· DOIT**

**Patron déclaré au registre**

Chaque système d’agents **DOIT** déclarer à sa fiche et au registre (section 11.4) le patron retenu parmi ceux du tableau 24, ou leur combinaison, accompagné d’un schéma de ses flux. Le patron déclaré **DOIT** résulter de l’arbre de décision de la figure 12 (section 7.3), tout écart étant justifié à la fiche. Toute autre topologie exige une dérogation (section 11.6).

Pourquoi : un patron connu se revoit, se teste et se compare; une topologie improvisée ne se gouverne pas.

`EXIG-ORC-04` **· NE DOIT PAS**

**Délégation limitée à deux niveaux**

Une chaîne de délégation **NE DOIT PAS** dépasser deux niveaux (orchestrateur, puis exécutant) : un exécutant ne délègue pas à son tour à un autre agent sans dérogation. Le serveur d’autorisation doit vérifier la profondeur lors de chaque échange de jetons (EXIG-IAM-08, section 9.3) et refuser l’échange qui l’excède; la passerelle d’agents ne fonde aucune décision sur les acteurs imbriqués, que la RFC 8693 tient pour informatifs (EXIG-IAM-11). Toute délégation entre agents, même sans mandant humain, passe par un échange de jetons dont le sujet est le mandant d’origine ou, s’il n’y a pas de mandant, l’agent initiateur. Un transfert (patron 3) remplace l’acteur courant sans ajouter de niveau, l’échange que refait la passerelle n’en ajoute pas non plus, et un appel interne entre sous-agents d’un même processus (patron 5) ne délègue pas au-delà. Un saut d’événement exécuté sous la délégation que référence l’événement compte comme un niveau (EXIG-EVT-07).

Pourquoi : choix du cadre, que l’étude citée n’étaye qu’indirectement; la coordination multiagent alourdit la communication et, sans validation centrale, amplifie les erreurs**[273]**; l’article mesure en outre un surcoût en jetons et davantage de tours de raisonnement**[274]**.

`EXIG-ORC-05` **· DOIT**

**Boucle évaluateur-optimiseur bornée**

Une boucle évaluateur-optimiseur **DOIT** déclarer des critères d’acceptation vérifiables, exécuter d’abord les vérifications déterministes disponibles (compilation, tests, moteur de règles), confier l’évaluation à un modèle ou à une invite distincts de ceux du producteur et s’arrêter après trois itérations au plus, une itération étant un cycle de production et d’évaluation. Au plafond, la tâche passe en escalade humaine avec la dernière version et les critiques reçues.

Pourquoi : Microsoft exige un plafond, des critères clairs et un repli défini; la valeur de trois est un choix du cadre**[9]**.

`EXIG-ORC-06` **· DOIT**

**Clavardage de groupe encadré**

Le clavardage de groupe ou le débat entre agents **DOIT** réunir trois agents participants au plus, sous un gestionnaire (hors décompte des trois participants) qui attribue la parole, avec un plafond de tours et une règle de clôture déclarés. Le maillage libre, où chaque agent sollicite les autres sans plafond, ne doit pas être utilisé.

Pourquoi : Microsoft recommande de limiter le clavardage de groupe à trois agents**[9]**, seuil que le cadre applique aux seuls participants, le gestionnaire qui attribue la parole s’y ajoutant (choix du cadre); des idées peuvent aussi se propager d’agent en agent**[280]**.

`EXIG-ORC-07` **· DOIT**

**Fusion déclarée et écrivain unique en parallèle**

Un patron de parallélisation **DOIT** déclarer avant l’exécution sa règle de fusion (déterministe, vote ou arbitrage) et sa limite de concurrence. Les branches **DOIVENT** se limiter à lire et à produire des artefacts; un seul composant **DOIT** écrire le résultat final dans un système d’enregistrement. Une branche de garde-fou **DOIT** rendre son verdict avant la fusion; une expiration vaut refus (PRIN-12). S’il faut écrire dans plusieurs systèmes d’enregistrement, un seul composant écrit dans chacun, sous une saga (section 7.5).

Pourquoi : des écritures concurrentes se contredisent**[277]**.

`EXIG-ORC-08` **· DOIT**

**Chorégraphie sous propriétaire et saga**

Une chorégraphie événementielle qui produit des effets dans plusieurs systèmes d’enregistrement **DOIT** avoir un propriétaire de bout en bout inscrit au registre, une saga explicite (section 7.5) et les contrôles d’enveloppe de la section 6.7. Un coordinateur de saga, composant inscrit au registre, y tient le rôle de l’orchestrateur des EXIG-ORC-16 à 18 (journal de compensation, escalade), et ses compensations passent par le canal de compensation (EXIG-ORC-28); à défaut de coordinateur, la saga est orchestrée.

Pourquoi : sans chef d’orchestre, personne ne voit le processus entier ni ne répond de son issue.

## 7.3 Choisir le patron

Le choix du patron suit l’arbre de décision de la figure 12, qui part de l’option la plus simple (code ou règle métier, appel direct au modèle, selon l’EXIG-ORC-01). Il se documente à la fiche de l’agent et se révise lorsque les mesures de production contredisent l’hypothèse de départ. L’arbre applique trois règles. D’abord, le mode de déclenchement ne choisit pas la topologie : un agent déclenché par un événement suit le même arbre qu’un agent sollicité par une personne, et la chorégraphie n’est retenue que si plusieurs domaines faiblement couplés réagissent au même fait (tableau 24); patron multiagent, elle reste soumise, comme tout autre, à la comparaison avec l’agent unique de l’EXIG-ORC-02. Ensuite, la question de l’agent unique se pose avant celle du routage, qui suppose un routeur et plusieurs spécialistes. Enfin, deux feuilles complètent les patrons de base : la chaîne séquentielle, lorsque les étapes sont connues et que chacune transforme la sortie typée de la précédente, et le clavardage de groupe, lorsqu’un débat contradictoire est requis (EXIG-ORC-06).

> **[Figure]**
> - NON
> - OUI Pas d’agent
> - code, règle ou appel direct
> - Les étapes sont-elles
> - connues d’avance?
> - OUI Flux déterministe
> - NON
> - Chorégraphie
> - événementielle
> - OUI
> - NON
> - OUI
> - NON Orchestrateur et exécutants
> - À combiner avec tout patron
> - La qualité se vérifie? boucle évaluateur-optimiseur ( 3 itérations).
> - Sous-tâches indépendantes? parallélisation (sectionnement ou vote).
> - Par défaut, retenir l’option la plus simple qui répond au besoin; passer au multiagent seulement sur preuve mesurée de gain.
> - Une règle, un appel d’outil
> - ou au modèle suffit-il?
> - Des domaines faiblement couplés
> - réagissent-ils au même fait?
> - NON
> - OUI
> - ou chaîne séquentielle
> - Un agent unique bien outillé, contexte non saturé, suffit-il?
> - Un spécialiste unique suffit
> - après qualification?
> - Agent unique
> - recherche d’outils si nécessaire
> - Routage et transfert
> - l’agent de tête se retire
> - ou clavardage de groupe si débat requis
> - → ≤
> - →

***Figure 12 — Arbre de décision du patron d’orchestration.** Les questions se lisent de haut en bas; la première réponse qui conclut fixe le patron. Le mode de déclenchement n’y entre pas : seule la réaction de plusieurs domaines faiblement couplés à un même fait mène à la chorégraphie, et l’agent unique se teste avant le routage. L’encadré du haut, à droite, s’ajoute à n’importe quel patron lorsque la qualité se vérifie ou que des sous-tâches sont indépendantes. Source : cadre CRE-IA-2026-01, d’après le Centre d’architecture Azure (niveaux de complexité) et Anthropic.*

### Quand le multiagent se justifie

Anthropic retient trois cas où plusieurs agents surpassent un agent unique : la **protection du contexte** (une sous-tâche produit une exploration volumineuse qui polluerait le contexte principal), la **parallélisation** (des pistes réellement indépendantes) et la **spécialisation** (des outils ou des consignes incompatibles dans un même agent)**[275]**. Microsoft ajoute les frontières de sécurité distinctes : deux domaines qui ne doivent pas partager les mêmes droits justifient deux agents**[9]**. L’effort doit aussi suivre la complexité : Anthropic emploie un agent et de 3 à 10 appels d’outils pour une recherche factuelle simple, de 2 à 4 sous-agents pour une comparaison, et davantage pour une recherche complexe**[17]**.

### Surcharge d’outils : mesurer avant de scinder

Aucune source ne fixe de seuil unique. OpenAI suggère, à titre indicatif, de viser moins de 20 fonctions disponibles au début d’un tour**[115]** et souligne que le chevauchement compte plus que le nombre : certaines mises en œuvre gèrent avec succès plus de 15 outils distincts, d’autres peinent avec moins de 10 outils qui se chevauchent**[66]**. La documentation d’Anthropic situe la dégradation au-delà de 30 à 50 outils disponibles**[281]**. Avant de multiplier les agents, deux leviers moins coûteux existent : consolider les outils en opérations orientées tâche, regroupées sous des espaces de noms**[114]**, et charger les définitions d’outils à la demande. Selon Anthropic, sa recherche d’outils réduit de 85 % (près de 89 % d’après ses deux chiffres, section 6.5) la consommation de jetons de contexte dans son exemple chiffré et fait passer la précision, sur ses évaluations internes de MCP, de 49 à 74 % (Opus 4) et de 79,5 à 88,1 % (Opus 4.5); ce sont des résultats déclarés par le fournisseur**[205]**.

### Découper par frontières de contexte

Quand plusieurs agents sont retenus, on découpe selon les frontières de contexte, et non selon le type de travail : une fonctionnalité et ses tests restent avec le même agent**[275]**. Par exemple, dans l’analyse d’un dossier de crédit, l’agent qui lit les états financiers calcule aussi les ratios qui en découlent; un agent distinct ne se justifie que pour un contexte isolable, comme la vérification des sanctions internationales, qui obéit à d’autres droits d’accès.

*Tableau 25 — Critères comparés des principaux patrons*

| **Critère** | **Flux déterministe** | **Agent unique** | **Routage et transfert** | **Orchestrateur et exécutants** | **Évaluateur-optimiseur** | **Chorégraphie** |
| --- | --- | --- | --- | --- | --- | --- |
| Prévisibilité et auditabilité | Très élevée | Moyenne | Élevée | Moyenne | Élevée sur le résultat | Moyenne, émergente |
| Latence de bout en bout | Faible à moyenne | Variable selon les tours | Faible | Élevée; réduite si parallèle | Moyenne à élevée | Asynchrone |
| Profil de coût en jetons (repère) | Le plus bas | Environ 4 fois une conversation | Cumul étape par étape | 3 à 10 fois l’agent unique; pointes si parallèle | Croît avec les itérations | Croît avec les abonnés et les sauts |
| Tolérance à l’ambiguïté | Faible | Élevée dans un domaine | Moyenne | Très élevée | Moyenne | Moyenne |
| Ce qui borne la dérive | Le code | Plafonds et budget | Liste fermée de destinataires | Deux niveaux, budget, délais | Trois itérations | Compteur de sauts, lettres mortes |

Les appréciations qualitatives du tableau 25 sont des repères du cadre. Les seuls ordres de grandeur retenus par le cadre sont ceux d’Anthropic (environ 4 fois et 15 fois une conversation; de 3 à 10 fois l’agent unique) **[17, 275]** et les profils de Microsoft : coûts cumulés étape par étape pour les patrons séquentiel et de transfert, pointes pour le patron concurrent, coût le moins prévisible pour le patron magnétique**[9]**. Ces repères cèdent la place aux mesures de jetons par agent et par exécution dès qu’elles existent (section 10.6).

`EXIG-ORC-09` **· DOIT**

**Surcharge d’outils traitée avant de scinder**

Dès qu’un agent dispose de plus de 15 outils au début d’un tour (seuil opérationnel choisi par le cadre, sous le repère indicatif de 20 fonctions d’OpenAI), ou dès que le jeu d’évaluation montre des confusions entre outils (chevauchement), l’équipe **DOIT** mesurer la précision de sélection d’outils sur le jeu d’évaluation et la comparer au seuil de précision déclaré à la fiche, puis essayer la consolidation des outils et leur chargement à la demande avant de scinder l’agent en plusieurs agents.

Pourquoi : le chevauchement compte plus que le nombre**[66]**, et la recherche d’outils restaure une partie de la précision à moindre coût**[205]**.

`EXIG-ORC-10` **· DEVRAIT**

**Découpage par frontières de contexte**

Lorsqu’un système multiagent est retenu, le découpage **DEVRAIT** suivre les frontières de contexte et de sécurité plutôt que les types de travail : le même agent garde une unité de travail et sa vérification immédiate. Un agent distinct se justifie par un contexte isolable, un parallélisme réel, une spécialisation d’outils ou une frontière de sécurité, consignés à la fiche. Une tâche d’écriture à fortes dépendances (écritures interdépendantes dans un même système d’enregistrement) doit rester à un seul agent (sections 7.1 et 7.7).

Pourquoi : un transfert qui ne passe que des messages, sans la trace complète, fait perdre des décisions implicites**[275, 276]**.

## 7.4 État et exécution durable

Un agent attend une approbation pendant trois jours; un serveur redémarre au milieu d’une réservation. Dans les deux cas, l’orchestration doit reprendre exactement où elle s’était arrêtée, sans perdre le contexte et sans refaire une action déjà faite. C’est le rôle de l’exécution durable.

### Persister l’état hors du processus

Microsoft recommande de persister l’état partagé hors de la mémoire et d’utiliser les points de contrôle du cadriciel**[9]**. Les moteurs y parviennent de façons différentes. Temporal garantit qu’une exécution de flux se poursuit jusqu’à son terme, sans limite de durée imposée, et la reprend après une panne en rejouant son historique d’événements**[81]**. Cet historique est toutefois borné (51 200 événements ou 50 Mo par exécution, selon la documentation de Temporal) : une exécution longue se poursuit par Continue-As-New, et un résultat volumineux passe par référence (EXIG-ORC-24). Ses activités sont en outre réessayées sans limite par défaut (EXIG-ORC-27). LangGraph conserve l’état par fil (`thread_id`) au moyen de *checkpointers* : `InMemorySaver` perd ses points de contrôle au redémarrage et sert à l’expérimentation, tandis qu’un magasin persistant comme `PostgresSaver` s’impose en production**[124, 282]**. Microsoft Agent Framework crée un point de contrôle à la fin de chaque étape de calcul du flux, avec l’état des exécuteurs, les messages et les requêtes en attente**[105]**.

### Ne jamais refaire une action terminée : une garantie à construire

La persistance ne suffit pas à éviter les doubles effets. Dans LangGraph, à la reprise après une interruption, le nœud interrompu redémarre depuis son début et le code qui précède l’interruption s’exécute de nouveau**[82]**; Temporal réessaie les activités en échec**[79]**. La garantie repose donc sur deux règles de conception : isoler chaque appel non déterministe (modèle, outil, agent distant) dans une étape journalisée dont le résultat se relit à la reprise, et rendre idempotent tout effet qui peut être rejoué (section 7.6). L’intégration de Temporal avec l’OpenAI Agents SDK applique la première règle : chaque invocation d’agent s’y exécute comme une activité, suivie et réessayée par le moteur**[122]**.

Aux points d’approbation obligatoires, l’état est persisté afin de reprendre sans rejouer le travail des agents précédents**[9]**. La primitive `interrupt()` de LangGraph, par exemple, suspend le graphe et attend sans limite une reprise sur le même fil**[82]**. La forme de l’approbation elle-même relève de la section 8.5.

### Points de contrôle, versions et rejeu

Un point de contrôle contient l’état complet d’une tâche, souvent avec des renseignements personnels (RP) et des extraits d’invites. Microsoft le désigne comme une frontière de confiance : on ne charge jamais un point de contrôle venant d’une source non fiable, et ses magasins Python n’acceptent qu’une liste d’autorisation de types à la désérialisation**[105]**. Les exécutions longues posent aussi un problème de version : Anthropic déploie ses agents en mode « arc-en-ciel » pour ne pas interrompre ceux qui s’exécutent déjà**[17]**. Enfin, le « voyage dans le temps » de LangGraph permet de rejouer depuis un point de contrôle antérieur ou de bifurquer après correction de l’état; les nœuds suivants s’exécutent alors de nouveau et les appels aux modèles ou aux API peuvent produire d’autres résultats**[283]**. Le rejeu sert à l’analyse et à la correction; il ne reproduit pas une décision à l’identique.

`EXIG-ORC-11` **· DOIT**

**Persistance après chaque transition**

Tout flux qui comporte au moins une étape P2 ou P3, une attente humaine (approbation, question) ou une durée supérieure à un seuil déclaré à la fiche **DOIT** s’exécuter sur un moteur d’exécution durable qui persiste l’état après chaque étape journalisée (appel de modèle, appel d’outil, décision, réponse humaine) dans un magasin externe au processus; chaque appel non déterministe à effet est sa propre étape (EXIG-ORC-12). Les autres flux de plus d’une étape devraient le faire. Un magasin en mémoire ne doit pas être utilisé en production ni dans un environnement qui traite des données réelles.

Pourquoi : un redémarrage ou un déploiement ne doit faire perdre ni le contexte ni l’avancement**[9, 124]**.

`EXIG-ORC-12` **· DOIT**

**Reprise sans double effet**

La logique de coordination **DOIT** rester déterministe une fois relus les résultats journalisés des appels non déterministes; chaque appel non déterministe **DOIT** s’exécuter comme une étape journalisée dont le résultat est relu, et non recalculé, à la reprise. Tout effet de bord, écriture ou non (notification, événement publié, appel facturé), **DOIT** être idempotent par une clé déterministe (EXIG-ORC-21) ou isolé dans une étape journalisée exécutée au plus une fois. Son emplacement par rapport au point de pause n’en dispense pas : un effet non idempotent ne précède jamais un point de pause et ne se trouve jamais dans une étape réessayable.

Pourquoi : les moteurs réexécutent le nœud interrompu ou réessaient l’activité en échec**[79, 82]**.

`EXIG-ORC-13` **· DOIT**

**Magasin de points de contrôle protégé**

Le magasin des points de contrôle **DOIT** être traité comme une frontière de confiance et comme une donnée de production : accès limité à l’identité de l’orchestrateur, chiffrement au repos, contrôle d’intégrité au chargement, conservation et élagage définis. Un orchestrateur ne doit pas charger de point de contrôle d’origine non vérifiée. Toute modification manuelle de l’état (bifurcation après correction) est signée de nouveau par le service d’orchestration et journalisée en audit. Aucun jeton n’y figure (EXIG-IAM-06).

Pourquoi : Microsoft désigne le point de contrôle, qui contient l’état complet de la tâche, y compris les messages en attente, comme une frontière de confiance**[105]**. Qu’un point de contrôle altéré permette d’en modifier l’état et que ces messages puissent contenir des RP est un constat du cadre.

`EXIG-ORC-14` **· DEVRAIT**

**Déploiement sans interruption des exécutions longues**

Le déploiement d’une nouvelle version d’agent ou de flux **DEVRAIT** laisser chaque exécution en cours se terminer sur la version avec laquelle elle a commencé; une migration d’état en cours d’exécution **DEVRAIT** se tester comme un changement de schéma. La cohabitation est bornée par le plafond de durée de l’EXIG-ORC-26. Le retrait d’une version pour un motif de sécurité doit suspendre les exécutions en cours ou les migrer par une migration testée.

Pourquoi : un déploiement peut casser les agents déjà en cours d’exécution, et recommencer du début coûte cher**[17]**.

## 7.5 Transactions : patron saga

Lorsqu’une tâche écrit dans plusieurs systèmes qui ne partagent aucune transaction (un système de transport, un progiciel de gestion intégré, une passerelle de paiement), aucun retour arrière global n’existe. La saga remplace la transaction globale par une suite de transactions locales, chacune appariée à une compensation (voir la figure 13).

### Principe

Garcia-Molina et Salem ont défini la saga en 1987 : une transaction de longue durée découpée en transactions plus courtes, avec la garantie que soit toutes s’exécutent, soit des transactions compensatoires défont l’exécution partielle**[284, 285]**. Microsoft distingue trois sortes d’étapes : les transactions **compensables**, qui précèdent le point de non-retour; la transaction **pivot**, qui est ce point de non-retour; et les transactions **réessayables**, idempotentes, qui la suivent jusqu’au terme**[67]**. Une saga se conçoit donc pour que tout ce qui est irréversible arrive le plus tard possible (PRIN-05).

> **[Figure]**
> - TRANSACTIONS LOCALES (VERS L’AVANT)
> - T1 ✓
> - Réserver le transport
> - compensable
> - T2 ✓
> - Réserver le stock (ERP)
> - compensable
> - T3 ✗ échec T4 · pivot
> - Confirmation officielle irréversible · approbation
> - COMPENSATIONS (ORDRE INVERSE, IDEMPOTENTES)
> - C1
> - Annuler la réservation
> - C2
> - Libérer le stock
> - échec définitif compenser de k−1 à 1
> - 2 échecs d’une compensation
> - file humaine prioritaire
> - JOURNAL EN AJOUT SEUL (LA COMPENSATION EST JOURNALISÉE AVANT L’ACTION)
> - journaliser
> - C1
> - exécuter
> - T1
> - journaliser
> - C2
> - exécuter
> - T2
> - journaliser
> - C3
> - T3 échoue
> - exécuter
> - C2
> - exécuter
> - C1
> - Préautoriser le paiement
> - compensable (P2)
> - 1. 2. 3. 4. 5. 6. 7. 8.
> - T3 n’a jamais été marquée « terminée » : C3 n’est exécutée que si l’issue de T3, une fois résolue, est un effet réalisé (EXIG-ORC-16). Le pivot T4 n’est atteint qu’après succès de T1 à T3.
> - →
> - →
> - ✓ ✓

***Figure 13 — Saga : transactions locales, pivot et compensations.** T1 et T2 réussissent; T3 échoue de façon définitive : l’orchestrateur exécute C2 puis C1, et le pivot T4, irréversible et soumis à approbation, n’est jamais atteint. Le journal montre que chaque compensation est consignée avant l’action qu’elle couvre. Le dessin simplifie deux points, que le texte corrige. Un débit externe est P3 et ne peut précéder le pivot (EXIG-ORC-15) : T3 se lit « préautoriser le paiement, sans capture », étape compensable (P2) par l’annulation de la préautorisation, et la capture se fait au pivot, avec son approbation. La compensation porte sur les étapes exécutées : de k−1 à 1 si T k a échoué sans effet, de k à 1 si son issue, une fois résolue (EXIG-ORC-16), est un effet réalisé. Source : cadre CRE-IA-2026-01, d’après Garcia-Molina et Salem (1987), Microsoft et Temporal.*

### Cinq règles de conception

1. **Journaliser la compensation avant l’action.** Temporal recommande d’inscrire la compensation avant d’exécuter l’activité, parce qu’un effet de bord peut survenir avant que l’échec ne soit signalé : une carte débitée, par exemple**[286]**. Microsoft exige de consigner chaque étape et la façon de la défaire dans un magasin durable, afin de reprendre la compensation au point d’échec**[77]**.
2. **Résoudre l’incertain avant de compenser.** Si l’orchestrateur ignore l’issue d’une étape (délai expiré, plantage entre le journal et la réponse), il la considère comme possiblement exécutée, mais aussi comme possiblement encore en cours chez le système visé : une compensation exécutée trop tôt ne trouve rien, réussit à vide, puis l’original produit son effet. Il clôt donc d’abord l’opération (annulation ou révocation de la clé d’idempotence, qui fait rejeter toute arrivée tardive) ou interroge le système visé par la clé jusqu’à une issue définitive; à défaut, l’étape passe en réconciliation humaine (EXIG-ORC-16). La compensation reste conditionnelle : « rembourser la transaction X si elle a été débitée », et non « rembourser le montant X ».
3. **Compenser en termes métier.** Une compensation applique des règles d’affaires : l’annulation d’un vol n’entraîne pas forcément un remboursement complet. Elle ne ramène pas nécessairement les données à leur état initial, ne suit pas toujours l’ordre inverse exact et peut parfois s’exécuter en parallèle**[77]**. On ne « désenvoie » pas un courriel : on envoie un rectificatif.
4. **Réessayer avant de compenser.** On ne compense que si la progression devient impossible, c’est-à-dire après épuisement des réessais ou devant une erreur non transitoire**[77]**.
5. **Escalader l’échec persistant.** Si une compensation échoue, Temporal recommande de consigner l’erreur, de poursuivre les autres compensations, puis d’alerter; une erreur non réessayable dans une compensation signifie que la saga ne peut plus revenir entièrement en arrière**[286]**. Microsoft prévoit la file de lettres mortes et la suspension des cas ambigus ou à fort impact pour revue humaine**[77]**. Le seuil de deux échecs retenu ci-dessous est un choix du cadre.

### Isolation entre sagas concurrentes

Une saga n’isole pas ses étapes comme une transaction ACID (atomicité, cohérence, isolation, durabilité). Microsoft recense trois anomalies : mises à jour perdues, lectures sales et lectures non répétables. Les contre-mesures sont le verrou sémantique, les mises à jour commutatives, la vue pessimiste (réordonner les étapes pour que les mises à jour aient lieu dans des transactions réessayables), la relecture des valeurs avant mise à jour, les jetons de version (*version tokens*) et le choix du mécanisme de concurrence selon le risque métier. La saga convient mal aux transactions fortement couplées et aux dépendances cycliques**[67]**. Exemple : deux agents qui réservent le même stock posent d’abord un verrou sémantique « réservation en attente », visible des autres sagas, plutôt que de décrémenter directement la quantité.

Pour les agents, SagaLLM (Chang et Geng, PVLDB, 2025) combine le patron saga, une mémoire persistante, des compensations automatisées et des agents de validation indépendants, en assouplissant les garanties ACID au profit d’une cohérence à l’échelle du flux**[287]**. C’est une référence de recherche utile, et non une norme d’industrie.

`EXIG-ORC-15` **· DOIT**

**Saga pour toute écriture multisystème**

Une tâche qui écrit dans au moins deux systèmes d’enregistrement sans transaction commune **DOIT** être modélisée comme une saga : chaque étape d’écriture P2 référence la compensation déclarée dans son entrée de catalogue (section 6.8); la définition de la saga déclare l’ordre des compensations (ordre inverse par défaut) et leurs dépendances, selon lesquels s’applique l’EXIG-ORC-18; le pivot, unique, est identifié; toute étape de palier P3 (action critique, externe ou irréversible) se place au pivot ou après, une fois les validations critiques réussies, et reçoit sa propre approbation humaine (EXIG-AUT-09 et EXIG-AUT-12). Les étapes qui suivent le pivot **DOIVENT** être idempotentes et réessayables jusqu’au succès, ou dotées d’une file humaine nommée pour l’échec définitif. En chorégraphie, un coordinateur de saga inscrit au registre tient le rôle de l’orchestrateur des EXIG-ORC-16 à EXIG-ORC-18 et de l’EXIG-ORC-28 (EXIG-ORC-08).

Pourquoi : reporter l’irréversible après toutes les validations limite ce qu’il faut défaire**[77]**.

`EXIG-ORC-16` **· DOIT**

**Journal de compensation tenu avant l’action**

Avant chaque étape d’écriture (P2 ou P3), l’orchestrateur, ou le coordinateur de saga en chorégraphie, **DOIT** consigner dans un journal durable, en ajout seul et corrélé à la trace, l’étape, la référence de ses arguments, sa clé d’idempotence et la compensation à exécuter. Ce journal ne garde que des références et, chiffrés, les seuls arguments nécessaires à la compensation; il ne contient aucun jeton (EXIG-IAM-06). Il suit les contrôles de l’EXIG-ORC-13 (accès, chiffrement, conservation, élagage au plus tard à la clôture de la saga augmentée d’un délai déclaré); l’historique du moteur durable peut en tenir lieu. Il est distinct du journal d’audit (EXIG-OBS-11), qui n’en reçoit que des empreintes. Avant de compenser une étape dont l’issue est inconnue, l’orchestrateur **DOIT** soit clôturer l’opération chez le système visé (annulation ou révocation de la clé d’idempotence, de sorte que toute arrivée tardive soit rejetée), soit l’interroger par sa clé jusqu’à une issue définitive, une réponse 409 valant attente et non échec. Si aucune des deux voies n’existe, l’étape passe en réconciliation différée, confiée à une personne (EXIG-ORC-18), et n’est ni compensée ni replanifiée à l’aveugle.

Pourquoi : un effet peut survenir avant que l’échec ne soit signalé**[286]**; une compensation qui précède l’effet tardif de l’original réussit à vide et laisse un effet net, d’où la résolution préalable, choix du cadre.

`EXIG-ORC-17` **· DOIT**

**Compensations idempotentes et métier, après réessais**

Chaque compensation **DOIT** être idempotente, définie en termes métier (remboursement, avis rectificatif, libération de stock) avec le propriétaire du système visé, et inscrite au catalogue comme un outil, avec son palier, référencé par le champ `compensation` de l’entrée de catalogue de l’outil d’origine (annexe C, C.2). La compensation déclarée d’une étape approuvée, bornée au montant et aux bénéficiaires d’origine et liée à la même clé d’idempotence, est approuvée avec l’étape (EXIG-AUT-12); toute autre compensation P3 exige une nouvelle approbation. Par exemple, une préautorisation de paiement annulable est P2, et sa capture est P3. L’orchestrateur réessaie d’abord l’étape en échec selon sa politique de réessai et ne compense que si la progression devient impossible.

Pourquoi : une compensation peut s’exécuter plusieurs fois et ne restaure pas forcément l’état initial**[77, 286]**.

`EXIG-ORC-18` **· DOIT**

**Escalade après deux échecs d’une compensation**

Lorsqu’une compensation subit une erreur non transitoire, ou épuise deux fois de suite la politique de réessai déclarée, l’orchestrateur, ou le coordinateur de saga en chorégraphie, **DOIT** cesser de la relancer, poursuivre les compensations qui n’en dépendent pas selon le graphe déclaré (EXIG-ORC-15), puis placer l’état complet de la saga dans une file humaine prioritaire nommée, avec alerte et identifiants de corrélation.

Pourquoi : l’échec persistant exige une intervention manuelle**[286]**; le seuil de deux échecs est un choix du cadre.

`EXIG-ORC-19` **· DOIT**

**Isolation sémantique des sagas concurrentes**

Lorsque plusieurs sagas, agents ou autres écrivains du système d’enregistrement (personnes, traitements en lot, intégrations existantes) peuvent modifier les mêmes enregistrements, la conception **DOIT** documenter les anomalies possibles (mises à jour perdues, lectures sales, lectures non répétables) et appliquer au moins une contre-mesure à chacune. Tout verrou sémantique **DOIT** avoir une échéance, un propriétaire et une procédure de libération en cas de suspension ou d’escalade; un écrivain qui ne le respecte pas est traité comme une anomalie à couvrir.

Pourquoi : la saga n’offre pas l’isolation d’une transaction ACID**[67]**.

`EXIG-ORC-20` **· DOIT**

**Tests d’injection de fautes des sagas**

Avant la mise en production, toute saga **DOIT** réussir les tests automatisés suivants, exécutés contre des doublures des systèmes d’enregistrement : échec forcé de chaque étape Tk avec vérification des compensations et de leur ordre déclaré; plantage entre l’écriture au journal et l’action; effet réalisé et résultat perdu; arrivée tardive de l’original après la décision de compenser; sagas concurrentes sur le même enregistrement; échec définitif après le pivot; double exécution de chaque compensation; double échec d’une compensation avec vérification de l’escalade; plantage pendant une compensation; compensation sous coupe-circuit et pendant une panne de la passerelle (EXIG-ORC-28). Un test de contrat d’idempotence **DOIT** en outre s’exécuter contre l’environnement d’essai du service visé, seul à connaître son comportement réel.

Pourquoi : exigence propre au cadre; les chemins de compensation ne servent presque jamais en exploitation normale et doivent être éprouvés avant d’être nécessaires.

## 7.6 Idempotence

Une opération est idempotente si l’exécuter deux fois produit le même effet que l’exécuter une fois. Sans cette propriété, un simple réessai après un délai expiré peut débiter un client deux fois.

Les doublons ne sont pas une hypothèse d’école : ils découlent des garanties mêmes des composants. Kafka livre « au moins une fois » par défaut, et sa sémantique « exactement une fois » ne couvre que le cycle lecture-traitement-écriture entre sujets Kafka**[140, 256]**. Pour les notifications push A2A, le protocole exige au moins une tentative de livraison (reprises facultatives, doublons possibles)**[68]**, et les flux Express asynchrones d’AWS Step Functions s’exécutent au moins une fois (les flux Express synchrones, « au plus une fois »), ce qui exige des actions idempotentes pour les premiers**[104]**. Les règles propres au bus d’événements figurent à la section 6.7.

Le cadre dérive la clé de l’identifiant de la tâche racine, stable de bout en bout, et de celui de l’étape. Le brouillon IETF `draft-ietf-httpapi-idempotency-key-header-08` (22 octobre 2026), qui n’est pas encore une RFC, décrit l’en-tête `Idempotency-Key` : le client renvoie la même clé à chaque réessai; le serveur répond 409 si la requête d’origine est encore en cours et 422 si la clé est réutilisée avec une charge utile différente. Le brouillon recommande un UUID (identifiant unique universel) ou un identifiant aléatoire semblable et met en garde contre les clés à faible entropie; la dérivation déterministe retenue par le cadre est un choix qui lui est propre, acceptable pourvu que la clé reste unique par opération et que le service la valide avant tout traitement**[78]**. Le brouillon laisse au serveur la durée de conservation des clés; le cadre la borne (EXIG-ORC-22). Quant aux annotations d’outil de MCP (`idempotentHint`, `destructiveHint`), ce sont de simples indices, sur lesquels un client ne fonde aucune décision lorsque le serveur n’est pas digne de confiance**[197, 201]**.

**Dérivation de la clé d’idempotence (illustration)**

```
réessai de la même étape                → même clé, aucun effet supplémentaire
même clé, arguments différents          → rejet (422 selon le brouillon IETF)
étape replanifiée avec d’autres valeurs → nouveau step_id, donc nouvelle clé
étape dont l’issue est incertaine        → aucune replanification avant résolution (EXIG-ORC-16)
nouvelle itération d’une boucle          → indice d’itération dans step_id, donc nouvelle clé
task_id         = "tache-7f3c2a"              (tâche racine; valeur abrégée, UUIDv4 en production)
step_id         = "etape-02/reserver-stock#1"  (chemin dans le plan, indice d’itération)
cle             = hex( SHA-256( JCS( ["idem-v1", task_id, step_id] ) ) )
```

`EXIG-ORC-21` **· DOIT**

**Clé d’idempotence sur toute écriture**

Chaque appel d’outil en écriture (P2 ou P3) **DOIT** porter une clé d’idempotence dérivée d’un identifiant d’opération racine stable de bout en bout et de l’identifiant de l’étape, réutilisée telle quelle à chaque réessai. L’identifiant racine est celui de la tâche de l’appelant d’origine, propagé dans le message de délégation (EXIG-ORC-23) et, pour un événement, le couple (`source`, `id`). L’identifiant d’étape encode le chemin de l’étape dans le plan et l’indice d’itération; une bifurcation par voyage dans le temps reçoit un nouvel espace de clés. La clé est l’empreinte de la canonisation RFC 8785 d’un objet, et non d’une concaténation, et l’identifiant racine est aléatoire (UUIDv4 ou équivalent). Une étape replanifiée avec d’autres arguments reçoit un nouvel identifiant d’étape, donc une nouvelle clé; une étape dont l’issue est incertaine ne doit pas être replanifiée avant sa résolution (EXIG-ORC-16). La clé voyage dans l’en-tête `Idempotency-Key` lorsque le service le prend en charge, sinon dans un champ déclaré du contrat d’outil.

Pourquoi : réessais, reprises et livraisons « au moins une fois » rejouent des appels**[68, 140]**.

`EXIG-ORC-22` **· DOIT**

**Vérification de la clé par le service visé**

Tout outil P2 ou P3 inscrit au catalogue **DOIT** déclarer au catalogue l’argument qui porte sa clé d’idempotence et son mode de vérification : (a) natif, la clé étant vérifiée par le système d’enregistrement; (b) par adaptateur, avec un registre de clés durable mis à jour dans la même transaction que l’effet, ou complété par une requête d’état qui constate l’effet par une référence externe dérivée de la clé. Un outil sans (a) ni (b) est classé P3, n’est jamais réessayé automatiquement, et une issue inconnue y déclenche une réconciliation humaine. La vérification garantit qu’un doublon ne produit aucun effet supplémentaire, qu’une clé réutilisée avec des arguments différents est rejetée et qu’une requête dont l’original est encore en cours est refusée sans exécution. Le service **DOIT** permettre d’interroger l’état d’une clé et devrait permettre de la révoquer; les clés sont cloisonnées par client. Leur durée de conservation, déclarée au catalogue, **DOIT** couvrir la durée de vie maximale de la tâche durable (EXIG-ORC-26), plus la fenêtre de reprise et le délai de réconciliation; une reprise depuis un point de contrôle plus ancien que cette durée est interdite (EXIG-ARC-06). Ce comportement est déclaré dans l’entrée de catalogue; les annotations MCP n’en tiennent pas lieu**[197]**.

Pourquoi : seul le système visé sait si l’effet a déjà eu lieu, et le brouillon laisse au serveur la durée de conservation des clés**[78]**; la déduplication ne vaut que pendant cette durée.

## 7.7 Contexte transmis entre agents

Ce qu’un agent transmet à un autre détermine à la fois la qualité du résultat, le coût et l’exposition des données. Le cadre impose un contexte minimal et structuré, avec une nuance importante pour les tâches fortement couplées.

Microsoft demande de décider quel contexte l’agent suivant requiert (contexte complet, version compactée ou nouvelle consigne seulement), de compacter entre agents et de limiter l’état persisté au strict nécessaire, pour des raisons de coût et de confidentialité**[9]**. Anthropic fait rendre par ses sous-agents une synthèse condensée, souvent de 1 000 à 2 000 jetons**[149]**, et stocke leurs livrables hors du contexte pour les transmettre par références légères**[17]**. La mise en garde de Cognition reste valable : un exécutant privé des décisions qui le concernent en prendra de contradictoires**[276]**. Le contexte minimal convient donc surtout aux tâches de lecture; une tâche à fortes dépendances reste à un seul agent (sections 7.1 et 7.3). Cognition a depuis nuancé sa position (Yan, 22 avril 2026) : des agents supplémentaires peuvent apporter du jugement tant que les écritures restent à fil unique; ses observations d’origine tiennent toujours pour les essaims d’écrivains parallèles**[289]**. La gestion du contexte et de la mémoire de chaque agent relève de la section 5.5.

**Contenu logique d’une délégation (indépendant du protocole)**

```
{
  "sous_objectif": "Évaluer la solvabilité du client 4471 selon la politique CR-12",
  "criteres_acceptation": ["ratios calculés", "pièces citées", "aucune donnée hors dossier"],
  "parametres": { "client_id": "4471", "montant_demande": 250000 },
  "artefacts": ["artefact://dossiers/4471/etats-financiers-2025.pdf"],
  "delegation": "<référence de délégation; jeton délégué en en-tête, hors message>",
  "tache_racine": "tache-7f3c2a", "etape": "etape-04/evaluer-solvabilite#1", "palier_max": "P1",
  "traceparent": "00-<trace-id>-<span-id>-01",
  "budget_restant": { "jetons": 40000, "cout_max_cad": 0.40, "appels_outils": 10, "echeance": "2026-10-27T14:13:12Z" },
  "schema_retour": "schema://credit/avis-solvabilite/1.2"
}
```

Ce message ne contient ni l’historique de la conversation ni les données que l’exécutant peut lire lui-même avec les droits du mandant. Sa traduction en messages A2A relève de la section 6.6.

La sécurité suit le même chemin. Microsoft exige que chaque agent applique un filtrage de sécurité, pour ne jamais renvoyer une donnée inaccessible à l’utilisateur, et que des garde-fous de contenu s’appliquent à plusieurs points : entrée de l’utilisateur, appels d’outils, réponses d’outils et sortie finale, car un agent intermédiaire peut introduire ou propager du contenu nuisible**[9]**.

`EXIG-ORC-23` **· DOIT**

**Contexte de délégation minimal et structuré**

Une délégation **DOIT** transmettre un message structuré limité au sous-objectif, aux critères d’acceptation, aux paramètres requis, aux références d’artefacts, à la référence de délégation (section 9.3), à l’identifiant de la tâche racine et à celui de l’étape qui délègue, dont l’exécutant dérive ses propres clés d’idempotence (EXIG-ORC-21), au palier maximal autorisé, au contexte de trace (section 10.1), au budget restant, au schéma de retour attendu et, pour une tâche fortement couplée, à un registre structuré des décisions prises. Le jeton délégué voyage dans l’en-tête d’authentification du transport (A2A, MCP), injecté par le code d’exécution ou par la passerelle; il ne doit pas figurer dans le message, dans un point de contrôle, dans un journal ni dans le contexte du modèle (EXIG-IAM-06). Le niveau d’autonomie et la classe les plus contraignants de la chaîne voyagent dans le contexte de délégation et s’imposent à l’exécutant (EXIG-AUT-10). L’historique brut complet ne doit pas être transmis, sauf exception justifiée à la fiche.

Pourquoi : un contexte minimal réduit le coût et l’exposition des données**[9]**.

`EXIG-ORC-24` **· DOIT**

**Retour validé avant toute réutilisation**

Un exécutant **DOIT** rendre une synthèse conforme au schéma de retour déclaré et déposer ses livrables volumineux dans un magasin d’artefacts, transmis par référence. L’orchestrateur **DOIT** valider la sortie (schéma, plafonds, garde-fous) avant de l’utiliser ou de la transmettre; une sortie invalide **DOIT** déclencher un réessai, une demande de précision ou l’arrêt.

Pourquoi : une sortie non validée propage l’erreur d’agent en agent**[9]**.

`EXIG-ORC-25` **· DOIT**

**Filtrage de sécurité dans chaque agent**

Chaque agent **DOIT** lire sous l’intersection des droits du mandant et de sa propre portée (section 9.3) et filtrer ses résultats selon les droits du mandant, de sorte qu’aucune donnée inaccessible à ce mandant ne remonte à l’orchestrateur ni à l’utilisateur. Un agent qui lit sous ses propres droits, derrière une frontière de sécurité distincte, **DOIT** rendre un schéma de retour dont les champs, déclarés à la fiche, sont accessibles au mandant. Les garde-fous de contenu s’appliquent à l’entrée, aux appels d’outils, aux réponses d’outils et à la sortie finale; le contenu reçu d’un autre agent est traité comme une donnée non fiable et porte les étiquettes de sa session d’origine (section 9.6).

Pourquoi : un agent intermédiaire peut introduire ou propager du contenu nuisible**[9]**.

## 7.8 Résilience et dégradation maîtrisée

Un modèle indisponible, un outil lent ou un agent qui tourne en rond ne doivent ni bloquer le processus ni produire un résultat faux en silence. Cette section met en œuvre le principe de dégradation maîtrisée (PRIN-12).

Microsoft prescrit pour les orchestrations d’agents des délais d’expiration et des réessais, une dégradation maîtrisée, la remontée des erreurs plutôt que leur masquage, la validation de la sortie d’un agent avant

sa transmission, l’examen de disjoncteurs, l’isolement des agents sans point unique de défaillance partagé et des points de contrôle pour reprendre après une panne ou un déploiement**[9]**. Anthropic note qu’il est courant d’inclure des conditions d’arrêt, comme un nombre maximal d’itérations, pour garder le contrôle d’un agent**[6]**. Les plafonds de l’exécution s’inscrivent dans l’enveloppe budgétaire de la tâche (section 10.6); le modèle de repli s’obtient par la passerelle de modèles (chapitre 5).

Le dernier recours est l’arrêt. Pour les systèmes à haut risque, le règlement européen sur l’IA prévoit la possibilité d’interrompre le système de façon sûre (art. 14, par. 4, al. e))**[61, 290, 412]**; le NIST AI RMF, cadre d’usage volontaire, demande (MANAGE 2.4) des mécanismes et des responsabilités pour remplacer, désengager ou désactiver un système dont les résultats s’écartent de l’usage prévu**[74]**. OpenAI recommande une interruption ordonnée, soit ciblée (révoquer une catégorie d’actions), soit générale**[291]**. La propagation de l’arrêt à travers les passerelles et les jetons relève de la section 9.4.

`EXIG-ORC-26` **· DOIT**

**Plafonds sur toute exécution**

Chaque exécution **DOIT** porter des plafonds déclarés à la fiche : étapes ou itérations, appels d’outils, jetons, coût et durée totale. L’atteinte d’un plafond **DOIT** arrêter la boucle en état sûr et déclencher l’escalade prévue; elle ne doit pas être rapportée comme un succès. Les réessais comptent dans ces plafonds. L’arrêt au plafond agit vers l’avant : les compensations des étapes exécutées puisent dans une réserve de budget calculée à la conception, hors de ces plafonds (EXIG-ORC-28).

Pourquoi : l’autonomie d’un agent entraîne des coûts plus élevés et un risque d’erreurs cumulatives, d’où des conditions d’arrêt pour garder le contrôle**[6]**.

`EXIG-ORC-27` **· DOIT**

**Mécanismes de résilience et repli testé**

Chaque dépendance d’une orchestration (modèle, outil, agent distant) **DOIT** être protégée par un délai d’expiration, par des réessais à temporisation exponentielle avec gigue *(exponential backoff with jitter)*, limités aux erreurs transitoires, en nombre borné et déclaré (`maximumAttempts` pour une activité Temporal à effet, dont les tentatives sont illimitées par défaut), portés par une seule couche par dépendance et comptés dans les plafonds de l’EXIG-ORC-26, et par un disjoncteur. Les erreurs sont remontées et journalisées, jamais masquées. Le repli prévu (modèle de repli homologué, service dégradé ou file humaine nommée recevant le contexte nécessaire à la reprise, sous les droits du mandant) est testé avant la production.

Pourquoi : Microsoft prescrit délais d’expiration et réessais et recommande d’envisager des disjoncteurs; la temporisation exponentielle, la gigue, la borne des tentatives, la couche unique, la limitation aux erreurs transitoires et le disjoncteur obligatoire sont des choix du cadre (PRIN-12)**[9]**.

`EXIG-ORC-28` **· DOIT**

**Coupe-circuit exercé chaque trimestre**

Chaque agent **DOIT** pouvoir être arrêté de façon ciblée (retrait d’un outil ou d’une capacité) ou totale. La plateforme **DOIT** en outre disposer d’un coupe-circuit global. L’arrêt agit vers l’avant : il bloque toute nouvelle étape métier et conserve l’état pour analyse. Les compensations des sagas en cours s’exécutent par le canal de compensation (EXIG-ORC-28), que l’arrêt ne ferme pas sauf décision distincte; une saga passée au pivot termine ses étapes réessayables par ce canal ou passe en file humaine. La suspension de sécurité est immédiate; la suspension administrative bloque les nouvelles tâches après avis préalable. La compensation automatique vise les sagas en cours; la réparation des actions terminées est une décision du propriétaire métier (section 12.8). L’arrêt **DOIT** être exercé au moins une fois par trimestre,

dans l’exercice de l’EXIG-SEC-26 : l’arrêt ciblé en production, l’arrêt global dans un environnement représentatif. Le délai mesuré **DOIT** être consigné et comparé à la cible de l’EXIG-IAM-20.

Pourquoi : le RIA prévoit l’interruption sûre des systèmes à haut risque (art. 14, par. 4, al. e)) et le NIST AI RMF, d’usage volontaire, demande des mécanismes pour désactiver un système (MANAGE 2.4), le cadre l’appliquant à tous les agents**[61, 74, 290, 412]**; la fréquence trimestrielle et l’arrêt vers l’avant sont des choix du cadre. Chaque arrêt bloque tout appel de l’identité visée; les compensations s’exécutent donc par un canal de compensation dédié, sous une identité de compensation propre à l’orchestrateur de la saga (ou au coordinateur de saga en chorégraphie), distincte de celle de l’agent, inscrite au registre, limitée aux outils de compensation déclarés au catalogue pour une étape inscrite comme exécutée au journal de compensation de la même tâche (EXIG-ORC-16), auditée à chaque appel par la passerelle ou le courtier, dotée d’une réserve de budget hors de l’enveloppe de l’agent et non touchée par le coupe-circuit, la suspension, la révocation de l’agent, l’épuisement de son enveloppe, le plafond de sauts ou l’échéance de son mandat (sauf décision de suspension distincte, motivée et journalisée; si la passerelle est indisponible, la compensation entre dans une file persistée et l’EXIG-ORC-18 s’applique à l’échéance fixée à la fiche).

## 7.9 Anti-patrons proscrits

La taxonomie MAST *(Multi-Agent System Failure Taxonomy)* (Cemri et coll., UC Berkeley), tirée de plus de 1 600 traces annotées issues de sept cadriciels, recense 14 modes de défaillance des systèmes multiagents en trois catégories : conception du système, désalignement entre agents, et vérification et terminaison des tâches. Elle conclut que les défaillances relèvent surtout de la conception, et non des seules limites des modèles**[292]**. La revue d’architecture cible donc les défauts de conception ci-dessous; le classement des incidents selon MAST relève de la section 10.4.

*Tableau 26 — Anti-patrons d’orchestration proscrits*

| **Anti-patron** | **Pourquoi il est proscrit** | **Correctif exigé** |
| --- | --- | --- |
| Coordination multiagent là où un agent ou un flux suffit | Coût, latence et erreurs accrus sans gain mesuré**[9]** | EXIG-ORC-01 et EXIG-ORC-02 |
| Agents sans spécialisation réelle, découpés par type de travail | Les transferts perdent des décisions implicites**[275, 276]** | Découpage par frontières de contexte (EXIG-ORC-10) |
| Confier au modèle un contrôle de flux que le code sait garantir, ou figer en code un flux dont les étapes ne sont pas connues d’avance | Patron inadapté à la nature du flux**[9]** | Configuration la plus simple justifiée (EXIG-ORC-01) et patron choisi selon l’arbre de décision de la section 7.3 (EXIG-ORC-03, PRIN-08) |
| État mutable partagé entre agents concurrents | Écritures contradictoires et résultats non reproductibles | Écrivain unique (EXIG-ORC-07); état d’exécution dans un magasin externe (EXIG-ORC-11) |
| Latence multisaut et contraintes de ressources ignorées | Délais cumulés et pointes de charge en mode concurrent | Délais par étape (EXIG-ORC-27), limite de concurrence (EXIG-ORC-07), plafonds (EXIG-ORC-26) |
| Contexte qui enfle sans contrôle, historique brut versé au contexte | Le rappel se dégrade quand l’information pertinente est noyée**[148]** | Compaction et références (EXIG-ORC-23, section 5.5) |
| État d’exécution en mémoire du processus | Perte de l’état au redémarrage**[124]** | Magasin durable (EXIG-ORC-11) |
| Maillage libre sans plafond de tours | Boucles, dérive, coûts imprévisibles | Patron déclaré et plafonds (EXIG-ORC-06, EXIG-ORC-26) |
| Chaîne d’écritures sans compensation ni clé d’idempotence | Effets partiels ou doublés impossibles à défaire | Saga et idempotence (section 7.5 et section 7.6) |
| Vérificateur qui déclare le succès sur quelques tests | Victoire prématurée**[275]** | Critères vérifiables, vérifications déterministes d’abord, évaluateur distinct (EXIG-ORC-05) |

`EXIG-ORC-29` **· NE DOIT PAS**

**Aucun anti-patron sans dérogation**

Une conception **NE DOIT PAS** présenter l’un des anti-patrons du tableau 26, que constate l’exigence citée à sa ligne (colonne « Correctif exigé ») : un même écart n’est donc relevé qu’une fois. La revue d’architecture doit les vérifier un à un et consigner le résultat à la fiche de l’agent, avec la décision d’homologation; tout écart exige une dérogation (section 11.6).

Pourquoi : une part importante des défaillances des systèmes multiagents tient à la conception du système et à la coordination entre agents**[292]**.

## 7.10 Cadriciels et plateformes d’orchestration

Cette section situe les principaux produits par rapport aux exigences du chapitre. Seule l’exigence EXIG-ORC-30 y est normative; le tableau 27 ne l’est pas : les produits cités sont des exemples non limitatifs, décrits selon leur état au 27 octobre 2026, et le catalogue d’entreprise les réévalue chaque trimestre. On distingue trois familles : les cadriciels, qui portent la logique propre à l’entreprise; les moteurs d’exécution durable, qui en garantissent la reprise; et les logiciels-services à agents intégrés, à privilégier lorsque le travail réside déjà dans leur système d’enregistrement.

*Tableau 27 — Cadriciels, moteurs et plateformes d’orchestration (exemples non limitatifs, état au 27 octobre 2026)*

| **Produit** | **Nature et modèle d’orchestration** | **Atouts au regard du cadre** | **Points d’attention** |
| --- | --- | --- | --- |
| **LangGraph** (LangChain) | Cadriciel d’exécution à base de graphe, avec persistance intégrée de l’état; version 1.0 du 22 octobre 2025, sans changement incompatible promis jusqu’à la 2.0 (persistance par fil : documentation « Persistence » de LangGraph)**[123, 124]** | Points de contrôle, `interrupt()` pour l’approbation, voyage dans le temps**[82, 283]** | Nœud réexécuté à la reprise; magasin persistant exigé en production**[82, 124]**; granularité de persistance à aligner sur l’EXIG-ORC-11 (un appel à effet par nœud) |
| **Microsoft Agent Framework** | Cadriciel sous licence MIT, successeur de Semantic Kernel et d’AutoGen; versions 1.0.0 pour Python et .NET le 2 avril 2026**[85, 293]** | Orchestrations séquentielle, concurrente, clavardage de groupe, transfert et magnétique; traces OpenTelemetry GenAI**[294, 295]** | Magasin de points de contrôle à protéger comme frontière de confiance**[105]**; point de contrôle par étape de calcul du flux : granularité à aligner sur l’EXIG-ORC-11 |
| **CrewAI** | Cadriciel combinant des Flows (état, événements, embranchements) et des Crews (équipes d’agents à rôles)**[296]** | Démarche recommandée par l’éditeur : partir d’un Flow et y insérer une Crew pour une étape collaborative, ce qui rejoint le flux déterministe du cadre | Persistance et reprise à démontrer en preuve de concept (EXIG-ORC-30) |
| **OpenAI Agents SDK** | Trousse à peu de primitives : agents, transferts ou agents utilisés comme outils, garde-fous, sessions, traçage; outils MCP natifs**[127]** | Intégration Temporal en disponibilité générale depuis le 23 mars 2026 : chaque invocation d’agent devient une activité**[122]** | Associer un moteur durable dès que le flux compte plusieurs étapes (EXIG-ORC-11) |
| **Google ADK** | Cadriciel ouvert en Python, TypeScript, Go, Java et Kotlin, indépendant du modèle et du lieu de déploiement; A2A et MCP**[126]** | Agents de flux `SequentialAgent`, `ParallelAgent` et `LoopAgent`, sans décision du modèle sur l’orchestration**[297]** | ADK 2.0 supplante ces gabarits, en Python et en Go, par des flux à base de graphes ou dynamiques, sans annoncer leur retrait : prévoir la migration**[297]** |
| **Strands Agents** (AWS) | Trousse sous licence Apache 2.0, publiée le 16 mai 2025, pilotée par le modèle**[128]** | MCP, télémétrie OpenTelemetry, patrons multiagents (agents comme outils, essaim, graphe, flux, A2A) | Réserver aux tâches ouvertes à autonomie bornée; moteur durable dès que le flux compte plusieurs étapes (EXIG-ORC-11) |
| **Temporal** | Moteur d’exécution durable; reprise à partir du dernier événement consigné dans l’historique d’événements (rejeu)**[80, 81]** | Compensations exécutées même après la défaillance d’un travailleur**[286]** | Isoler appels de modèles et d’outils dans des activités (EXIG-ORC-12); historique borné : Continue-As-New et passage par référence; `maximumAttempts` sur les activités à effet (EXIG-ORC-27) |
| **AWS Step Functions** | Service géré de machines à états | Flux Standard d’une durée maximale d’un an, à sémantique d’exécution exactement une fois, sauf réessais déclarés**[104]** | Flux Express (5 minutes; au moins une fois en mode asynchrone, au plus une fois en mode synchrone) : actions idempotentes obligatoires en mode asynchrone |
| **Microsoft Copilot Studio** | Plateforme à faible code; orchestration multiagent annoncée en préversion le 19 mai 2025 (Microsoft Build), dont plusieurs capacités passent en disponibilité générale à compter d’avril 2026**[298, 299]** | MCP en disponibilité générale depuis le 29 mai 2025, A2A depuis avril 2026**[48, 300]** | Identité Entra Agent ID créée pour chaque nouvel agent depuis juillet 2026 : l’inscrire au registre d’entreprise**[48]** |
| **Salesforce Agentforce** | Logiciel-service; orchestration SOMA (*Single-Org, Multi-Agent*, une organisation Salesforce) et MOMA (*Multi-Org, Multi-Agent*, plusieurs organisations)**[49]** | A2A entrant et sortant; client MCP et serveur MCP hébergé | Contraintes de produit : un seul saut de délégation en MOMA (deux agents en chaîne); sept sous-agents connectés pour Agent Script, limite que l’éditeur qualifie d’actuelle |
| **ServiceNow** | Logiciel-service; AI Agent Fabric (annoncé le 6 mai 2025), couche d’échange par MCP et A2A; AI Control Tower en disponibilité générale le même jour**[51]** | Action Fabric expose les actions de la plateforme à tout agent d’IA par un serveur MCP, pour des actions sécurisées et gouvernées (annonce du 5 mai 2026)**[50]** | Extensions de l’AI Control Tower (coupe-circuit, mesure des coûts) annoncées pour août 2026, disponibilité non vérifiée au 27 octobre 2026 : vérifier selon la version déployée**[47]** |

`EXIG-ORC-30` **· DOIT**

**Capacités démontrées avant l’inscription d’un produit**

La pile d’orchestration proposée à l’inscription au catalogue (un cadriciel, un moteur ou une plateforme, seuls ou combinés) **DOIT** démontrer en preuve de concept, dans les conditions de l’entreprise, les capacités suivantes, chacune étant attribuée au composant qui la porte : la persistance durable des points de contrôle et la reprise après panne; la pause pour approbation humaine sans perte d’état; l’émission de traces OpenTelemetry selon les conventions GenAI; la prise en charge de MCP et d’A2A, nativement ou par adaptateur; l’export des définitions de flux et de l’état dans un format documenté; la propagation d’une clé d’idempotence stable (EXIG-ORC-21); l’exécution des compensations et de l’escalade de saga (tests de l’EXIG-ORC-20); les plafonds par exécution (EXIG-ORC-26); l’arrêt ciblé et global (EXIG-ORC-28).

Pourquoi : l’entreprise garde la propriété de sa logique d’orchestration (PRIN-09), et une capacité se vérifie au lieu de se présumer sur la foi d’une fiche commerciale (chapitre 13).
