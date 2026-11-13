# Chapitre 14 — Mémoire

*Question directrice : comment des agents partagent-ils ce qu'ils ont appris sans se corrompre ?*

> **Version 2 — 11 novembre 2026.** État de référence : documentation des éditeurs et prépublications consultées le 11 novembre 2026; liste OWASP Top 10 for Agentic Applications du 9 décembre 2025 et bilan OWASP du troisième trimestre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre. Les articles d'arXiv ont été lus au niveau du résumé, sauf mention contraire; [30] à [32] sont des sources secondaires. Les renvois « chapitre N » ont été vérifiés dans les chapitres visés. Chapitre audité et révisé le 12 novembre 2026.

Un agent sans mémoire recommence chaque tâche à zéro. Un agent doté d'une mémoire conserve des préférences, des faits, des leçons tirées d'échecs, et s'en sert plus tard, souvent dans une autre session et parfois pour un autre utilisateur. Dès que plusieurs agents lisent et écrivent le même fonds, la mémoire devient un état partagé et mutable, alimenté par un modèle de langage à partir de contenus qu'il ne maîtrise pas.

La thèse de ce chapitre tient en une phrase : une mémoire d'agent se gouverne comme une base de données, pas comme un cache. Chaque écriture a un auteur, une portée, une provenance et une durée de vie; chaque lecture est une décision d'autorisation. Le stockage est bien outillé; manquent les règles de concurrence, de permission, de portabilité et d'oubli. Une recension de 435 travaux le constate : la recherche s'intéresse beaucoup plus à accumuler et à retrouver l'état qu'à le gouverner, à le rétablir ou à s'en défaire [17].

---

## 14.1 Types de mémoire

### Une taxonomie héritée des sciences cognitives

Le cadre le plus repris est CoALA (Cognitive Architectures for Language Agents) [1]. Il distingue une mémoire de travail et trois mémoires à long terme.

| Type | Ce qu'elle contient, selon CoALA [1] | Exemple en entreprise | Risque propre à l'écriture |
|---|---|---|---|
| De travail | L'information active du cycle de décision en cours | Le dossier ouvert, les derniers résultats d'outils | Faible : elle disparaît avec la session |
| Épisodique | L'expérience des cycles antérieurs : historiques, trajectoires | « Ce client a contesté sa facture en mars » | Un épisode faux sert ensuite de précédent |
| Sémantique | Le savoir de l'agent sur le monde et sur lui-même | « Le client préfère le courriel » | Un fait périmé ou injecté passe pour établi |
| Procédurale | Le savoir-faire : poids du modèle et code de l'agent | Consignes, compétences, prompts système | Le plus élevé : elle modifie le comportement |

CoALA précise que l'apprentissage consiste à écrire dans la mémoire à long terme, et qu'écrire dans la mémoire procédurale est nettement plus risqué que d'écrire dans les deux autres : on peut y introduire des défauts ou laisser l'agent contourner l'intention de ses concepteurs [1]. Écrire dans les poids relève de l'affinage et de la distillation (chapitre 47). Dans une institution financière fédérale, la ligne directrice E-23 exige des critères de changement important pour un modèle autoapprenant, dont l'application à une mémoire persistante reste ouverte (chapitre 38, section 38.3).

Les cadriciels reprennent ce vocabulaire. La documentation de LangGraph oppose une mémoire à court terme, limitée à un fil de conversation, à une mémoire à long terme rangée dans des espaces de noms et partagée entre fils, qu'elle classe en sémantique, épisodique et procédurale [8]. Amazon Bedrock AgentCore Memory retient la même coupure entre court et long terme [9].

### Une seconde lecture : formes, fonctions, dynamique

Une recension de décembre 2025 juge insuffisante l'opposition court terme / long terme et propose trois angles : les formes, les fonctions et la dynamique de la mémoire. Elle distingue aussi la mémoire d'agent de la génération augmentée par récupération et de l'ingénierie du contexte [2].

Cette distinction fixe le périmètre du chapitre. L'ingénierie du contexte décide de ce qui entre dans la fenêtre du modèle à un instant donné (chapitre 13). Les données d'entreprise ont un propriétaire et une gouvernance indépendants de l'agent (chapitre 15). L'état d'exécution d'une tâche longue relève des points de contrôle (chapitre 18). La mémoire, au sens retenu ici, est ce que l'agent écrit lui-même pour un usage futur. C'est cette écriture par le modèle qui la rend singulière, et fragile.

---

## 14.2 Architectures : fichiers, vecteurs, graphes

### Une hiérarchie, comme dans un système d'exploitation

MemGPT a posé en 2023 l'analogie qui structure encore le domaine : déplacer l'information entre une mémoire rapide et limitée, la fenêtre de contexte, et une mémoire lente et vaste, à la manière d'un système d'exploitation [3]. Un article de position de 2026 en tire un principe : la performance d'un agent dépend des déplacements de données entre ces couches [14]. Trois façons de bâtir la couche lente coexistent.

### Des fichiers

L'agent lit et écrit des fichiers texte avec les outils dont il dispose déjà. L'outil de mémoire de l'API de Claude en donne la forme la plus dépouillée : six commandes sur un répertoire `/memories`, exécutées côté client, sur un stockage que l'application contrôle et dont elle assure les protections [4]. Les *memory stores* de Claude Managed Agents, en bêta, appliquent le même principe côté serveur : chaque fonds est monté comme un répertoire dans le bac à sable de la session [5]. Letta projette la mémoire de l'agent dans des fichiers Markdown tenus dans un dépôt Git [6].

Selon une synthèse de ZenML sur les déploiements en production, beaucoup d'équipes jugent une base vectorielle superflue quand le contexte est naturellement borné; un index vectoriel devient nécessaire pour une base de connaissances d'entreprise ou une mémoire durable entre sessions [30].

### Des vecteurs

Un pipeline extrait les éléments saillants d'une conversation, les consolide et les indexe par plongements pour une récupération par similarité. Mem0 en est l'exemple type. Ses auteurs rapportent, sur le banc d'essai LOCOMO, une amélioration relative de 26 % sur la mémoire d'OpenAI et un coût en jetons réduit de plus de 90 % par rapport à l'injection de l'historique complet [12].

### Des graphes

Zep, avec son moteur Graphiti, range la mémoire dans un graphe de connaissances temporel qui conserve l'historique des relations. Ses auteurs rapportent 94,8 % sur le banc DMR, contre 93,4 % pour MemGPT [11]. D'après un compte rendu publié par ZenML, quand une donnée nouvelle contredit une ancienne, Graphiti n'efface pas la relation : il la marque comme invalide à partir d'une date. La construction du graphe coûte cher [31].

| Architecture | Force | Faiblesse | Convient quand |
|---|---|---|---|
| Fichiers | Lisible, modifiable et versionnable par un humain | Pas de recherche sémantique; croissance à surveiller | Mémoire bornée, par projet ou par agent |
| Vecteurs | Rappel par similarité à grande échelle | Faits isolés; provenance et mise à jour difficiles | Grands volumes, préférences et faits simples |
| Graphes | Relations, temporalité, lignage | Coût de construction et complexité | Contexte réglementé, multi-utilisateurs, besoin de traçabilité |

### Ce que valent les mesures

LongMemEval, publié à ICLR 2025, évalue cinq capacités de mémoire sur 500 questions et rapporte une chute d'exactitude de 30 % chez les assistants commerciaux et les modèles à long contexte au fil d'interactions soutenues [13]. Deux réserves limitent la portée de ces bancs : ils portent sur des conversations entre un utilisateur et un assistant, non sur une mémoire partagée entre agents, et les comparaisons publiées, dont celles de Mem0 et de Zep, émanent des éditeurs. Une évaluation interne reste nécessaire avant de choisir.

### Écrire pendant ou après

Le moment de l'écriture est une décision distincte. LangGraph décrit deux options : écrire pendant l'exécution, ce qui rend la mémoire disponible tout de suite mais ajoute de la latence, ou écrire en tâche de fond [8]. La seconde offre un point de contrôle : une écriture différée peut être validée avant d'être admise.

---

## 14.3 Mémoire partagée : concurrence et permissions

### Deux prototypes

L'article de position cité plus haut ramène la question à deux modèles classiques [14]. Dans la **mémoire partagée**, tous les agents accèdent à un fonds commun : la réutilisation est simple, mais sans mécanisme de cohérence, les agents s'écrasent mutuellement ou lisent des données périmées. Dans la **mémoire distribuée**, chaque agent garde son fonds et synchronise de façon sélective : l'isolation est meilleure, mais les états divergent. La plupart des systèmes réels se situent entre les deux, avec une mémoire de travail locale et quelques artefacts partagés.

### La cohérence, lacune principale

Les auteurs tiennent la cohérence pour le plus grand vide conceptuel et la décomposent en deux exigences [14]. À la lecture, traiter les conflits : un enregistrement évolue, et une version périmée peut rester visible. À l'écriture, fixer la visibilité et l'ordre : quand l'écriture d'un agent devient-elle observable par les autres, et dans quel ordre des écritures concurrentes peuvent-elles être vues ? Le problème est plus dur que dans une base classique, parce que les conflits sont souvent sémantiques : deux faits peuvent se contredire sans porter la même clé.

Letta recommande de confier les réécritures à un seul agent, les autres se bornant à ajouter [7]. Les *memory stores* appliquent une concurrence optimiste : une précondition sur l'empreinte du contenu refuse l'écriture si celui-ci a changé depuis la lecture [5]. Les dépôts partagés de Letta s'en remettent à la gestion de versions : chaque agent valide et pousse ses changements, les autres les tirent [6].

Aucun de ces mécanismes ne détecte qu'un agent a écrit « le client préfère le courriel » et un autre « ne jamais écrire au client ». Une prépublication de juin 2026 traite ce cas par la **supersession temporelle** : un fait nouveau qui en contredit un ancien le remplace une fois admis. Son évaluation sur un service en production en a montré la fragilité : un filtre synchrone de quasi-doublons pouvait rejeter une écriture contradictoire avant le détecteur de contradictions [15].

### Les permissions

Le même article de position constate que les permissions, la portée et la granularité restent sous-spécifiées : un agent peut-il lire la mémoire à long terme d'un autre, et à quelle unité d'accès ? Il ajoute que les protocoles comme MCP couvrent les entrées-sorties de contexte, pas l'accès à la mémoire [14].

Collaborative Memory sépare un niveau privé et un niveau partagé; chaque fragment y porte des attributs de provenance immuables qui permettent une vérification rétrospective [16]. La prépublication sur la mémoire de flotte nomme quatre modes de défaillance (fuite non autorisée, propagation de données périmées, persistance de contradictions, effondrement de la provenance) et y oppose quatre primitives, dont la récupération bornée par portée et le suivi de provenance [15].

Son résultat le plus instructif est un défaut trouvé en production. L'isolation entre locataires tenait, mais la portée inférieure au locataire était contournée par une lecture directe par identifiant, faite avec des justificatifs d'agent. Le défaut a été divulgué et corrigé pendant l'étude [15]. La leçon rejoint une règle du chapitre 5 (section 5.2) : un identifiant est un nom, pas un droit, et l'autorisation se vérifie sur chaque chemin de lecture.

Côté produits, deux mécanismes se retrouvent partout. Le premier est l'**espace de noms** : AgentCore Memory range chaque mémoire à long terme sous un chemin hiérarchique qui peut inclure l'acteur et la session [10]. Le second est le **mode d'accès** : un *memory store* s'attache à une session en lecture-écriture, le mode par défaut, ou en lecture seule. Contre l'injection, la documentation recommande de séparer un fonds de référence partagé, en lecture seule, du fonds propre à chaque session [5]. Ce défaut est l'inverse de celui que retient ce chapitre.

Aucun de ces mécanismes n'est normalisé, et leur rattachement aux droits de l'utilisateur (chapitre 15, section 15.3) et à l'autorité déléguée à l'agent (chapitre 30) reste à la charge de l'intégrateur.

---

## 14.4 Portabilité entre plateformes

### Pas de standard

Aucune norme de mémoire d'agent n'a été trouvée à la date de rédaction. Chaque plateforme a son unité : un fichier [5], un document JSON [8], un fait extrait [10], une arête de graphe datée [11]. Passer de l'une à l'autre n'est pas une conversion de format : c'est une nouvelle extraction.

Au niveau des assistants, la portabilité se résume à du texte copié : la page d'aide de Claude décrit l'importation comme le collage d'une liste de mémoires produite par l'autre service, et qualifie la fonction d'expérimentale [28].

### Deux propositions, aucune adoptée

Une prépublication de mai 2026, « Portable Agent Memory », propose un protocole de transfert entre agents de fournisseurs différents : des entrées adressées par leur contenu, un graphe de provenance qui rend les altérations détectables et un contrôle d'accès par capacités. Son résumé ne donne aucun résultat chiffré sur la fidélité du transfert [26].

Une proposition de juillet 2026, publiée par trois auteurs sur le site de recherche de MacPaw, part d'un autre angle : la mémoire appartient à l'utilisateur, qui ne peut aujourd'hui ni la déplacer ni vérifier qu'elle a été supprimée. Elle définit un paquet autonome et des « pierres tombales » de suppression. Ses auteurs écrivent qu'elle n'a encore ni implémentation indépendante, ni gouvernance neutre, ni large adoption [27].

### Ce qui se transporte réellement

Faute de standard, la portabilité se prépare à la conception. Ce qui suit est une déduction, non un résultat de recherche.

- **Garder les sources.** Les épisodes bruts se transportent; les plongements et les graphes en sont dérivés, dépendent d'un modèle ou d'un schéma, et se reconstruisent.
- **Préférer le texte lisible pour ce qui doit survivre à un changement de plateforme.** Un fichier Markdown est le plus petit dénominateur commun; pour la mémoire procédurale, Agent Skills et AGENTS.md jouent ce rôle, mais le format se transporte mieux que le comportement, qui se réévalue sur chaque hôte (chapitre 13).
- **Traiter toute importation comme du contenu non fiable.** Une mémoire importée est un texte que l'agent tiendra pour vrai; la prépublication de mai range d'ailleurs la résistance à l'injection parmi les exigences de son protocole [26].

Le chapitre 27 replace cette question dans la stratégie multi-plateformes et dans les clauses de sortie. Le chapitre 46 (section 46.4) recommande de garder la mémoire hors du fournisseur de modèles : une bascule de modèle ne perd alors que les caches.

---

## 14.5 Risques : empoisonnement, instructions dormantes, fuites

### Une catégorie de risque à part entière

La liste OWASP Top 10 for Agentic Applications, publiée le 9 décembre 2025, consacre une entrée à la mémoire : ASI06, Memory & Context Poisoning [18]. Ce qui distingue ce risque de l'injection de prompt ordinaire est le délai : une injection agit dans la session, une mémoire empoisonnée agit dans toutes les suivantes. Le chapitre 31 traite la liste entière (sections 31.2 et 31.6).

### Trois voies d'attaque documentées

**Empoisonner le fonds.** AgentPoison glisse dans la mémoire ou la base de connaissances des exemples malveillants qu'un déclencheur optimisé fait remonter. Ses auteurs rapportent un taux de succès moyen supérieur à 80 % sur trois agents, avec moins de 0,1 % d'entrées empoisonnées et moins de 1 % de dégradation en usage normal [21].

**Empoisonner par simple conversation.** MINJA montre qu'un attaquant n'a pas besoin d'accéder au fonds : il y fait inscrire des enregistrements malveillants en interagissant avec l'agent comme n'importe quel utilisateur, et ces enregistrements se déclenchent ensuite sur la requête d'une victime [22]. Dans une mémoire partagée entre utilisateurs, tout utilisateur est donc un écrivain potentiel.

**Différer l'instruction.** Une démonstration de février 2025 contre Gemini montre le mécanisme de l'instruction dormante : un document contient des consignes cachées qui demandent d'enregistrer de faux souvenirs si l'utilisateur répond par un mot banal. L'écriture a lieu plus tard, sur ce qui ressemble à une demande de l'utilisateur [23].

### Du laboratoire au terrain

Microsoft a décrit en février 2026 un usage commercial du procédé : des boutons « résumer avec l'IA » ouvrent un assistant avec un prompt prérempli qui lui demande de retenir une entreprise comme source de confiance. En soixante jours, l'équipe a relevé 50 prompts distincts venant de 31 entreprises [24].

Les agents de développement sont une autre cible. Un responsable de l'entrée ASI06, chercheur chez Cisco, rapporte une recherche de son employeur sur Claude Code : cloner un dépôt et approuver l'installation d'une dépendance suffisait pour qu'une charge malveillante atteigne la mémoire persistante et la configuration globale des *hooks*, avec un effet qui survivait aux sessions et aux redémarrages. La version 2.1.50 a retiré les mémoires d'utilisateur du prompt système [19].

Le bilan du troisième trimestre 2026 du projet OWASP GenAI, non officiel, rattache à ASI06, par appréciation d'analystes, trois incidents : des instructions persistées dans la mémoire d'un assistant de programmation, une configuration d'agent déposée dans un dépôt et exécutée à son ouverture, des définitions d'outils MCP modifiées [20]. Lecture de ce chapitre, non du bilan : la persistance se loge dans ce à quoi l'agent fait déjà confiance.

### Les fuites

L'autre risque est qu'un fait appris devant un public ressorte devant un autre. Une prépublication d'août 2026 propose une règle d'exclusion : chaque élément garde la trace du public présent à son enregistrement, et n'est admis dans le contexte que si tous les lecteurs actuels en faisaient partie. La règle est indépendante du modèle, puisque le fait interdit est absent du contexte avant tout appel. L'auteur la démontre, mais juge ses résultats expérimentaux préliminaires et synthétiques [25].

### Contrôles

| Contrôle | Ce qu'il empêche | Appui |
|---|---|---|
| Lecture seule par défaut; écriture accordée fonds par fonds | Qu'une injection réussie écrive dans une mémoire que d'autres sessions liront comme fiable | [5] |
| Confirmation humaine avant d'enregistrer un souvenir | L'écriture différée par instruction dormante | [23] |
| Provenance attachée à chaque écriture | L'impossibilité de remonter à l'origine d'un fait | [15][16] |
| Versions immuables et retour arrière | La perte de l'état sain après une écriture malveillante | [5] |
| Autorisation avant l'assemblage du contexte | La fuite entre publics ou entre locataires | [15][25] |
| Filtrage des données sensibles à l'écriture | La conservation de secrets ou de renseignements personnels | [4] |
| Inspection de la mémoire après un comportement inattendu; lectures et écritures tracées (chapitre 33) | La persistance silencieuse | [20] |

Ces contrôles ont un point commun : ils sont appliqués par l'infrastructure, pas demandés au modèle. Ce bilan le dit : des instructions au niveau du prompt ne suffisent pas à établir une frontière de sécurité [20].

---

## 14.6 Rétention, oubli et conformité

### Un cycle de vie incomplet

La recension citée en introduction suit l'état persistant de l'écriture à l'oubli, à l'audit et au retour arrière; gouverner, rétablir et abandonner l'état y sont les étapes les moins étudiées [17].

### L'obligation d'effacer

L'article 17 du RGPD oblige le responsable du traitement à effacer les données personnelles sans retard injustifié, notamment quand elles ne sont plus nécessaires aux fins de leur collecte ou quand la personne retire son consentement; il prévoit des exceptions, dont le respect d'une obligation légale et l'exercice de droits en justice [29]. Le chapitre 38 traite l'effacement selon la Loi 25 et le projet C-36 (section 38.4).

Appliquée à une mémoire d'agent, l'obligation bute sur trois difficultés.

**Les faits dérivés.** Une mémoire synthétise. Un fait peut venir de trois sources, et effacer l'une d'elles ne dit pas s'il faut effacer le fait. Selon le compte rendu de ZenML, Zep applique une règle explicite : un fait n'est supprimé que si aucun épisode restant ne le soutient, ce qui suppose un lignage maintenu à travers les fusions d'entités et les mises à jour [31]. Sans lignage, une demande d'effacement ne peut pas être exécutée avec certitude.

**L'historique.** Les versions immuables qui protègent contre l'empoisonnement conservent aussi ce qu'on voulait effacer. La documentation des *memory stores* montre comment un produit tranche : toute modification crée une version immuable, conservée trente jours, et supprimer une mémoire n'efface pas ses versions. Une opération `redact` retire le contenu d'une version passée en gardant la piste d'audit; elle est destinée aux demandes de suppression et au retrait de secrets [5]. L'invalidation temporelle d'un graphe pose le même problème : elle sert l'audit, mais elle n'efface rien [31].

**Le dépositaire.** Le lieu de stockage détermine qui répond de la rétention. L'outil de mémoire côté client laisse les données dans l'infrastructure de l'entreprise, qui en fixe la durée; une mémoire hébergée par le fournisseur suit les règles de rétention du fournisseur [4][5]. Des clés détenues par l'entreprise rendent le contenu hébergé irrécupérable quand elle les coupe, mais arrêtent l'agent si le gestionnaire de clés devient injoignable (chapitre 46, section 46.3).

### En pratique

Une politique de rétention de la mémoire répond à quatre questions, par classe de mémoire : combien de temps, qui peut effacer, jusqu'où l'effacement se propage (index, résumés, versions, copies chez d'autres agents) et comment il se prouve. Faute de standard, le chemin d'effacement se conçoit et se teste comme une fonction du système, au même titre que la sauvegarde.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Faut-il une mémoire à long terme ? | Non, tant qu'un besoin entre sessions n'est pas établi | Tâches multi-sessions, personnalisation, apprentissage d'erreurs |
| Architecture | Fichiers, par agent ou par projet | Vecteurs pour de grands volumes; graphe si la temporalité et le lignage sont exigés |
| Moment de l'écriture | En tâche de fond, avec validation | Chemin chaud si le souvenir doit servir dans la même session |
| Partage entre agents | Fonds de référence en lecture seule, plus un fonds propre par agent ou par session | Fonds commun en écriture seulement avec un écrivain désigné |
| Concurrence | Écrivain unique, ou précondition sur le contenu lu | Ajouts seuls : écritures concurrentes acceptables |
| Portée | Espace de noms par locataire, utilisateur et agent, vérifié à chaque lecture | — |
| Mémoire procédurale | Écrite par des humains, versionnée, relue | Écriture par l'agent seulement avec revue avant activation |
| Sources d'écriture | Aucune écriture à partir de contenu non fiable sans confirmation | Fonds jetable, limité à la session |
| Provenance | Auteur, source et date sur chaque entrée | — |
| Rétention | Durée par classe, expiration automatique, effacement testé | Obligation légale de conservation |
| Portabilité | Sources conservées en texte; index reconstruits | Mémoire jetable sans valeur de migration |
| Choix d'un produit | Évaluation interne sur données réelles | — |

---

## Points à retenir

- La mémoire d'un agent est ce qu'il écrit lui-même pour plus tard, à partir de contenus qu'il ne maîtrise pas. C'est ce qui la rend singulière et attaquable.
- Quatre types structurent le domaine : de travail, épisodique, sémantique, procédurale. Écrire dans la mémoire procédurale est le geste le plus risqué.
- Fichiers, vecteurs et graphes répondent à des besoins différents. Les chiffres de performance publiés viennent surtout des éditeurs, et aucun banc consulté ne mesure la mémoire partagée entre agents.
- La cohérence d'une mémoire partagée est la lacune principale. Les produits offrent la concurrence optimiste, l'écrivain unique ou la gestion de versions; aucun ne résout les contradictions sémantiques.
- Les permissions ne sont pas normalisées. Espaces de noms et modes d'accès existent dans chaque produit, et un cas réel montre qu'une portée peut tenir sur un chemin de lecture et céder sur un autre.
- Aucun standard de portabilité n'existe. Ce qui se transporte, ce sont les sources en texte; les index se reconstruisent.
- L'empoisonnement de mémoire est une catégorie OWASP (ASI06), démontrée en recherche et observée sur le terrain. Sa marque est le délai entre l'écriture et l'effet.
- Les défenses sont appliquées par l'infrastructure, pas demandées au modèle : lecture seule par défaut, provenance, versions, autorisation avant l'assemblage du contexte.
- L'oubli est la partie la moins outillée. Effacer exige un lignage des faits dérivés et un traitement explicite de l'historique des versions.

---

## Sources

Pages primaires lues le 11 novembre 2026 (articles d'arXiv : page de résumé, sauf [1] et [14], lus dans le texte); [5], [15], [17], [19], [20], [25], [26] et [27] relues le 12 novembre 2026 :

1. [Cognitive Architectures for Language Agents — CoALA (arXiv 2309.02427)](https://arxiv.org/html/2309.02427v3)
2. [Memory in the Age of AI Agents (arXiv 2512.13564)](https://arxiv.org/abs/2512.13564)
3. [MemGPT: Towards LLMs as Operating Systems (arXiv 2310.08560)](https://arxiv.org/abs/2310.08560)
4. [Claude API — Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
5. [Claude Managed Agents — Using agent memory](https://platform.claude.com/docs/en/managed-agents/memory)
6. [Letta — Shared memory](https://docs.letta.com/concepts/shared-memory/index.md)
7. [Letta — Multi-agent shared memory (blocs partagés, ancienne API)](https://docs.letta.com/guides/agents/multi-agent-shared-memory)
8. [LangGraph — Memory overview](https://docs.langchain.com/oss/python/langgraph/memory)
9. [Amazon Bedrock AgentCore — Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
10. [Amazon Bedrock AgentCore — Memory organization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html)
11. [Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv 2501.13956)](https://arxiv.org/abs/2501.13956)
12. [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (arXiv 2504.19413)](https://arxiv.org/abs/2504.19413)
13. [LongMemEval (ICLR 2025, arXiv 2410.10813)](https://arxiv.org/abs/2410.10813)
14. [Multi-Agent Memory from a Computer Architecture Perspective (arXiv 2603.10062)](https://arxiv.org/html/2603.10062v1)
15. [Governed Shared Memory for Multi-Agent LLM Systems (arXiv 2606.24535)](https://arxiv.org/abs/2606.24535)
16. [Collaborative Memory: Multi-User Memory Sharing with Dynamic Access Control (arXiv 2505.18279)](https://arxiv.org/abs/2505.18279)
17. [Always-On Agents: A Survey of Persistent Memory, State, and Governance (arXiv 2606.30306)](https://arxiv.org/abs/2606.30306)
18. [OWASP — annonce du Top 10 for Agentic Applications, 9 décembre 2025](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
19. [OWASP — Memory Is a Feature. It Is Also an Attack Surface, 13 mai 2026](https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface/)
20. [OWASP — GenAI and Agentic AI Exploit Roundup Q3 2026, 8 octobre 2026](https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/)
21. [AgentPoison (arXiv 2407.12784)](https://arxiv.org/abs/2407.12784)
22. [Memory Injection Attacks on LLM Agents via Query-Only Interaction — MINJA (arXiv 2503.03704)](https://arxiv.org/abs/2503.03704)
23. [Embrace The Red — Gemini, mémoire persistante et invocation différée d'outil, 10 février 2025](https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/)
24. [Microsoft Security — AI Recommendation Poisoning, 10 février 2026](https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/)
25. [Authorization Before Context (arXiv 2608.17148)](https://arxiv.org/abs/2608.17148)
26. [Portable Agent Memory (arXiv 2605.11032)](https://arxiv.org/abs/2605.11032)
27. [MacPaw Research — Memory Belongs to the User: Portable Memory, 6 juillet 2026](https://research.macpaw.com/publications/portable-memory.md)
28. [Claude — Import and export your memory](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude)
29. [RGPD, article 17 — droit à l'effacement](https://gdpr-info.eu/art-17-gdpr/)

Sources secondaires :

30. [ZenML — What 1,200 Production Deployments Reveal About LLMOps in 2025, 19 décembre 2025](https://zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025) — synthèse de cas, page lue.
31. [ZenML LLMOps Database — Provenance and Lineage Tracking in LLM-Powered Agent Memory Systems](https://www.zenml.io/llmops-database/provenance-and-lineage-tracking-in-llm-powered-agent-memory-systems) — compte rendu d'une présentation de Zep, page lue.
32. [OWASP Top 10 for Agentic Applications 2026 — page de téléchargement](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — document PDF non lu.

## Limites de ce chapitre

- Le texte officiel de l'entrée ASI06 [32] n'a pas été lu; sa description repose sur trois billets du projet OWASP [18][19][20].
- La plupart des articles d'arXiv ont été lus au niveau du résumé. Les chiffres cités pour Mem0, Zep, AgentPoison et LongMemEval sont ceux des résumés, et leurs conditions de mesure n'ont pas été vérifiées.
- Le régime d'effacement de la LPRPDE n'est examiné ni ici ni au chapitre 38.
- Le fonctionnement interne de Mem0 et de Graphiti, ainsi que la règle de suppression de Zep, viennent de textes de leurs éditeurs ou d'un compte rendu secondaire [31].
- La page de Letta sur les dépôts partagés ne décrit pas la résolution des conflits.
- La mémoire des plateformes de Microsoft et de Google et la mémoire paramétrique ou latente [2] ne sont pas traitées.
- Les recommandations de la section 14.4, les colonnes « Exemple » et « Risque » du tableau de la section 14.1, le tableau comparatif de la section 14.2, la lecture des trois incidents OWASP en 14.5 et la grille de décision sont des synthèses de ce chapitre.