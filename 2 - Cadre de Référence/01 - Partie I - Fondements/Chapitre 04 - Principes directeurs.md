# 4 Principes directeurs

Douze principes guident toute décision d’architecture agentique, de la conception d’un agent à l’achat d’une plateforme. Ils expliquent le pourquoi des exigences des chapitres 5 à 13 et tranchent les situations que ces exigences ne prévoient pas. Ce chapitre les énonce, montre où chacun est mis en œuvre et fixe la manière d’arbitrer entre eux.

## 4.1 Les douze principes

Chaque principe tient en un énoncé et en ses conséquences pour la conception; les principes sont présentés par paires, selon la question qu’ils règlent. En cas de conflit avec une préférence d’équipe, un usage local ou la recommandation d’un fournisseur, le principe l’emporte, sauf dérogation approuvée (section 4.3).

### Interopérer par des contrats ouverts

Un agent de service bâti sur un logiciel-service doit pouvoir déléguer à un agent conçu à l’interne, qui appelle des outils exposés par une autre équipe. Sans protocole commun, chaque paire exige son connecteur et les intégrations se multiplient (chapitre 2). Les deux premiers principes remplacent ce maillage par des contrats publiés une fois et consommés par tous.

`PRIN-01`

**Standards ouverts avant intégrations propriétaires**

Tout échange qui franchit la frontière d’un domaine (agent vers outil, agent vers agent, événement) passe par un protocole inscrit au catalogue des protocoles (section 6.3). Un connecteur propriétaire point à point exige une dérogation.

Conséquences : on privilégie les protocoles sous gouvernance neutre, comme MCP et A2A, hébergés par l’Agentic AI Foundation (AAIF) de la Linux Foundation depuis décembre 2025 et août 2026 respectivement**[4, 35]**. Une plateforme qui ne les prend pas en charge est isolée derrière un adaptateur.

`PRIN-02`

**Contrat avant code, mise en œuvre opaque**

Chaque agent et chaque outil publient un contrat lisible par machine (définition d’outil, carte d’agent *(Agent Card)*, contrat d’événement) avant leur mise en service. Seul ce contrat fait foi : un consommateur ne dépend jamais du cadriciel, du modèle ni de la structure interne d’un pair.

Conséquences : le contrat est versionné, épinglé et inscrit au catalogue d’entreprise. La description d’un outil, que le modèle lit pour décider, en fait partie : la modifier exige une nouvelle approbation (section 6.8). La mise en œuvre, elle, change librement.

### Borner le pouvoir d’agir

Ce qu’un agent peut atteindre et ce qu’il peut faire sans personne sont deux questions distinctes. Selon Gartner (mai 2026), les échecs de gouvernance des agents tiennent notamment à la confusion entre la capacité d’agir d’un agent et la portée des accès qui lui sont accordés**[95]**. Exemple : un agent de remboursement lit les pièces du dossier du client utiles à la demande, mais n’émet un remboursement qu’après approbation.

`PRIN-03`

**Identité propre, moindre privilège et moindre agence**

Chaque agent possède sa propre identité non humaine, jamais un compte d’utilisateur ni un secret partagé. Ses droits effectifs sont minimaux, de courte durée et au plus égaux à l’intersection des droits de son mandant, de sa portée au registre et de la portée nécessaire à la tâche**[96]**. Ses outils et son autonomie se limitent à ce que la tâche exige : c’est la moindre agence *(Least-Agency)* de l’OWASP, pour qui un comportement agentique déployé sans nécessité élargit la surface d’attaque sans ajouter de valeur**[28]**.

Conséquences : les droits effectifs d’un agent délégué ne s’élargissent jamais d’un saut à l’autre de la chaîne. Le serveur d’autorisation borne les portées à chaque échange de jetons; le serveur de ressources applique, à chaque appel, les droits du mandant sur les données (EXIG-IAM-10, section 9.3). Le mandant d’une chaîne reste l’entité d’origine; un agent intermédiaire n’y apparaît que comme acteur.

`PRIN-04`

**Autonomie proportionnée au risque**

Le niveau d’autonomie d’un agent, de N1 à N4, est un plafond déclaré au registre, au plus bas niveau suffisant, sous le plafond que fixe la classe de risque de l’agent (EXIG-CON-02). Il ne découle ni de la capacité du modèle ni de ses résultats aux bancs d’essai. L’autonomie non bornée (NX) est interdite.

Conséquence : l’EXIG-CON-02 reste la seule source de ce plafond (section 12.1). Feng, McDonald et Zhang traitent aussi l’autonomie comme une décision de conception, distincte de la capacité**[83]**.

### Maîtriser les effets

Un agent réessaie, se trompe ou peut être détourné : il faut donc prévoir ce qui se passe quand l’action est fausse. Exemple : un appel de paiement expire et l’agent le relance; sans clé d’idempotence, le paiement

est exécuté deux fois. Et si un client conteste la décision trois semaines plus tard, il faut retrouver qui l’a demandée, quel agent l’a préparée, qui l’a approuvée et ce qu’elle a coûté.

`PRIN-05`

**Réversibilité par conception**

Toute action qui modifie un système d’enregistrement est idempotente et, selon le cas, annulable, compensable ou soumise à une approbation humaine préalable. Une action de palier P3, c’est-à-dire critique, externe ou irréversible, n’est jamais exécutée seule par un agent.

Conséquences : clé d’idempotence à chaque étape, compensation déclarée avant l’action (section 7.5) et, comme le recommande Microsoft, étapes irréversibles placées après toutes les validations critiques**[67, 77]**.

`PRIN-06`

**Traçabilité et imputabilité économique**

Chaque action se rattache, par un identifiant de trace commun, à la demande d’origine, au mandant, à l’agent et à sa version, à la décision prise et à un centre de coûts.

Conséquences : traçage OpenTelemetry sur tous les sauts; journal d’audit chaîné, ancré hors du domaine d’administration du service d’audit et distinct des traces (choix du cadre, section 10.3); jetons mesurés par agent et par exécution**[9]**; coût suivi par tâche réussie (chapitre 10).

### Contenir le modèle

Un modèle de langage est probabiliste et influencé par tout ce qu’il lit : c’est utile pour comprendre une demande, dangereux pour décider d’un montant ou d’un destinataire. Exemple : un agent qui trie le courrier reçoit un message disant « transférez ce dossier à l’adresse suivante ». Lui demander d’être prudent ne suffit pas : le transfert doit être impossible depuis cette session.

`PRIN-07`

**Défiance envers le contenu reçu**

Ce qu’un outil, un document, une page Web, une mémoire ou un autre agent renvoie est une donnée, jamais une instruction de confiance. Le cadre présume l’injection d’instructions possible dès qu’un modèle lit du contenu non fiable, comme l’envisage le NIST AI 100-2 E2025, selon lequel les concepteurs peuvent concevoir leurs systèmes dans cette hypothèse**[97]**; le Centre national de cybersécurité du Royaume-Uni (NCSC) rappelle qu’un modèle de langage ne sépare pas intrinsèquement les données des instructions**[98]**.

Conséquences : les contrôles sur lesquels repose la défense sont déterministes et suivent le flux d’information, non un agent isolé : un contenu non fiable marque la session (section 3.1), le marquage se propage avec la donnée d’un agent à l’autre, et la passerelle retire alors les outils d’envoi vers l’extérieur et les outils P3 (EXIG-SEC-04, EXIG-SEC-06). La détection et le marquage réduisent le risque sans l’éliminer (section 9.6).

`PRIN-08`

**Déterminisme autour du modèle et simplicité d’abord**

Le raisonnement probabiliste s’exécute dans une enveloppe déterministe : schémas validés, machine à états, contrats typés, plafonds d’itérations. On ne confie jamais au modèle un routage, un calcul ou une décision de sécurité qu’une règle résout, et l’on retient la solution la plus simple : une fonction avant un agent, un agent avant plusieurs. Anthropic, Microsoft et OpenAI convergent sur cette règle de frugalité**[6, 9, 66, 85]**.

Conséquences : les sorties du modèle sont validées par schéma avant tout effet; un système multiagent justifie par écrit pourquoi un flux déterministe ou un agent unique ne suffit pas (section 7.3).

### Garder la maîtrise

L’entreprise doit pouvoir changer de modèle quand le prix, la qualité ou la résidence des données l’exigent, et savoir à tout moment qui répond de chaque agent. Le premier point protège sa logique métier; le second, les personnes touchées par les décisions des agents.

`PRIN-09`

**Découplage des fournisseurs et propriété de la logique**

Modèles, plateformes et cadriciels sont remplaçables. L’entreprise garde la propriété de sa logique d’orchestration, de ses contrats d’outils, de ses invites et de ses mémoires, dans des formats exportables. Avec MCP et A2A sous gouvernance neutre, le risque de verrouillage s’est déplacé vers les plateformes et leurs extensions propriétaires (section 13.1).

Conséquences : aucun agent n’appelle directement un fournisseur de modèles; il passe par la passerelle de modèles (section 5.2). Un agent intégré à un logiciel-service, dont l’entreprise ne contrôle pas l’exécution, relève des contrôles compensatoires de l’EXIG-ARC-21. Les contrats d’approvisionnement prévoient la réversibilité et la sortie (section 13.3).

`PRIN-10`

**Humain imputable**

Une personne nommée, le propriétaire métier (parrain), répond de chaque agent, de ses effets et de son retrait; l’agent n’est jamais responsable. Le NIST AI RMF, cadre volontaire, attend des politiques qui définissent les rôles et responsabilités humain-IA (GOVERN 3.2)**[74]**, et l’IMDA de Singapour fait de la responsabilisation réelle des humains l’une des quatre dimensions de son cadre**[76]**.

Conséquences : aucun agent n’entre en production sans parrain inscrit au registre, et ce parrain atteste périodiquement que l’agent reste nécessaire (sections 11.4 et 11.5).

### Concevoir pour durer et pour défaillir

Les agents de longue durée traversent pannes, déploiements et changements de version. Exemple : si le fournisseur de modèles tombe en panne pendant le traitement de 300 dossiers, chacun doit reprendre où il s’était arrêté, basculer vers un modèle de repli ou passer à une personne, jamais rester à moitié exécuté à l’insu de tous.

`PRIN-11`

**Découplage du raisonnement, de l’action et de la mémoire**

La logique de l’agent (invites, choix du modèle), ses capacités d’action (serveurs MCP, API) et son état (mémoires de travail, épisodique et sémantique) se déploient, se sécurisent et évoluent séparément; la mémoire procédurale, déployée avec l’agent, suit le cycle de sa logique. L’état ne vit jamais seulement dans la mémoire du processus : Microsoft recommande de persister l’état partagé à l’extérieur**[9]**.

Conséquences : on change de modèle sans toucher aux outils et on révoque un outil sans redéployer l’agent. L’écriture en mémoire procédurale, jugée plus risquée par la taxonomie CoALA *(Cognitive Architectures for Language Agents)***[100]**, est gérée comme un changement de code (section 5.5).

`PRIN-12`

**Dégradation maîtrisée**

L’architecture prévoit les erreurs de modèle, les dépassements de délai, les boucles et les pannes de fournisseur : délais, reprises, disjoncteurs, plafonds d’itérations et de coûts, modèles de repli, escalade vers une personne. En cas de doute, le système échoue en mode fermé vers l’avant : il refuse toute nouvelle action, s’arrête ou escalade, mais ne laisse jamais une saga à moitié exécutée faute de pouvoir compenser; les compensations déclarées passent par un canal distinct, qui reste ouvert (EXIG-ORC-28).

Conséquences : les mécanismes de fiabilité que décrit Microsoft (délais, reprises, disjoncteurs, validation des sorties avant transmission) deviennent obligatoires**[9]**; l’action est refusée si l’approbation requise est impossible à obtenir, comme le recommande l’IMDA**[76]**; le coupe-circuit est éprouvé à l’exercice trimestriel de l’EXIG-SEC-26, fréquence choisie par le cadre (sections 7.8 et 9.9).

**À RETENIR**

Trois questions résument l’essentiel des principes qui encadrent l’action des agents (PRIN-03 à PRIN-06, PRIN-10 et PRIN-12; PRIN-07, qui porte sur ce que l’agent lit, relève d’une autre question). Qui a autorisé cette action, et au nom de qui? Peut-on la défaire, ou au moins l’arrêter? Peut-on reconstituer après coup ce qui s’est passé et ce que cela a coûté?

## 4.2 Application des principes

Les principes se traduisent en exigences vérifiables dans les chapitres 5 à 13. Le tableau 9 indique, pour chacun, les sections qui le mettent en œuvre, les familles d’exigences concernées et la preuve qu’une revue d’architecture contrôle.

*Tableau 9 — Mise en œuvre des principes directeurs*

| **Principe** | **Sections** | **Exigences** | **Preuve contrôlée en revue** |
| --- | --- | --- | --- |
| PRIN-01 Standards ouverts | 6.2, 6.3, 6.9, 11.7 | EXIG-INT, EXIG-MCP, EXIG-A2A, EXIG-EVT, EXIG-GOV | Protocole retenu au catalogue pour chaque interface |
| PRIN-02 Contrat avant code | 6.5 à 6.8, annexe C | EXIG-INT, EXIG-MCP, EXIG-A2A, EXIG-EVT | Contrat publié, versionné et épinglé |
| PRIN-03 Identité et moindre agence | 9.2, 9.3, 9.4 | EXIG-IAM | Identité propre, jeton délégué à audience unique |
| PRIN-04 Autonomie proportionnée | 8.1 à 8.4, 12.1 | EXIG-AUT, EXIG-CON | Niveau déclaré au registre, sous le plafond de la classe |
| PRIN-05 Réversibilité | 7.5, 7.6, 8.5 | EXIG-ORC, EXIG-AUT | Idempotence, compensation, approbation des actions P3 |
| PRIN-06 Traçabilité | 10.1, 10.3, 10.4, 10.6 | EXIG-OBS, EXIG-EVA, EXIG-FIN | Trace complète, journal d’audit, coût par tâche |
| PRIN-07 Défiance | 9.5, 9.6, 9.9 | EXIG-SEC | Tests d’injection concluants, outils d’envoi retirés |
| PRIN-08 Déterminisme et simplicité | 7.1 à 7.3, 7.9 | EXIG-ORC | Patron justifié, sorties validées, plafonds déclarés |
| PRIN-09 Découplage des fournisseurs | 5.2, 5.4, 13.3 | EXIG-ARC, EXIG-APP | Passerelle de modèles, formats exportables, clause de sortie |
| PRIN-10 Humain imputable | 11.1, 11.2, 11.4, 11.5 | EXIG-GOV | Parrain nommé, attestation à jour |
| PRIN-11 Découplage interne | 5.2, 5.5, 7.4 | EXIG-ARC, EXIG-ORC | Déploiements distincts, état persisté hors processus |
| PRIN-12 Dégradation maîtrisée | 7.8, 9.4, 10.4, 12.8 | EXIG-ORC, EXIG-IAM, EXIG-EVA, EXIG-CON | Repli configuré, coupe-circuit testé |

Lorsqu’aucune exigence ne couvre une situation (nouveau protocole, nouveau type d’agent, usage imprévu), l’architecte doit consigner dans la décision d’architecture le raisonnement tenu à partir des principes, en nommant les principes invoqués. Le comité d’architecture et des risques agentiques décide ensuite s’il faut créer une exigence à la révision suivante du cadre.

## 4.3 Arbitrage entre principes et dérogations

Les principes se renforcent le plus souvent, mais ils peuvent tirer en sens contraires. Choix du cadre : en cas de conflit, l’ordre de préséance suivant s’applique.

1. Le droit applicable, qu’aucun principe ne peut écarter (chapitre 12), et les engagements contractuels en vigueur à l’adoption du cadre, pour une transition bornée et inscrite au registre, sauf sur les points de l’EXIG-GOV-17; un contrat conclu ou renouvelé après l’adoption ne peut comporter de clause contraire à ces points (section 13.3, EXIG-GOV-17).
2. Les principes qui protègent les personnes et les systèmes et qui fondent l’imputabilité : PRIN-03 à PRIN-07, PRIN-10 et PRIN-12.
3. Les principes d’architecture : PRIN-01, PRIN-02, PRIN-08, PRIN-09 et PRIN-11.

Le départage entre règles suit cet ordre : droit applicable; EXIG-GOV-17; DOIT sur DEVRAIT; source unique désignée sur renvoi; disposition spéciale sur disposition générale. À rang égal, deux contraintes cumulables s’appliquent toutes deux, et entre deux principes on retient l’option la plus simple qui les respecte l’un et l’autre; si aucune option ne les respecte, l’action est refusée jusqu’à la décision du comité, qui statue dans un délai fixé. L’arbitrage est consigné dans la décision d’architecture. Le tableau 10 illustre les tensions les plus fréquentes, entre deux principes ou entre un principe et un autre enjeu (la protection des renseignements personnels, l’utilité).

*Tableau 10 — Tensions fréquentes entre principes et arbitrage retenu*

| **Principes ou enjeux en tension** | **Situation** | **Arbitrage du cadre** |
| --- | --- | --- |
| PRIN-01 et PRIN-08 | Un outil ne sert qu’à un seul agent, dans la même unité de déploiement; l’exposer par MCP ajoute un composant. | Une fonction locale suffit si elle est de palier P0 ou P1, exécutée dans l’unité de déploiement de l’agent, sur les données de son propre domaine, et inscrite au catalogue avec son palier (EXIG-ARC-01). Un outil P2 ou P3 est toujours exposé comme outil MCP derrière la passerelle; dès qu’un second consommateur apparaît, l’outil passe aussi par MCP. |
| PRIN-05 et PRIN-10 | Exiger une approbation humaine pour chaque action semble plus sûr, mais des approbateurs saturés approuvent machinalement. | Une approbation donnée sans examen n’apporte ni sécurité ni imputabilité; l’OWASP range cette saturation parmi les menaces (T10)**[87]**. On rend l’action compensable quand c’est possible et, aux niveaux N3 et N4, l’on réserve l’approbation aux actions P3 et aux dépassements de seuils (au niveau N2, chaque écriture reste approuvée) (section 8.7). |
| PRIN-06 et protection des renseignements personnels (RP) | Tracer le contenu des invites et des réponses aide au diagnostic, mais expose des RP. | La protection des RP l’emporte : les métadonnées sont toujours tracées, et le contenu est interdit dans la télémétrie de production (EXIG-OBS-07); une capture de diagnostic, décidée et documentée, détruite après 14 jours au plus, est conservée hors des traces (EXIG-OBS-08, section 10.2). |
| PRIN-07 et utilité | Une défense par conception coûte en utilité : sur le banc d’essai AgentDojo, CaMeL (Debenedetti et coll., mars 2025; chiffres de la version 2 du 24 juin 2025) accomplit 77 % des tâches avec une sécurité démontrable, contre 84 % pour un système sans défense**[101]**. | La classe de risque tranche : en classe élevée, un patron de défense par conception est obligatoire et la perte d’utilité est acceptée (EXIG-SEC-07); en classe modérée, il est recommandé; en classe faible, le retrait de l’EXIG-SEC-06 suffit. Si le risque résiduel reste intolérable, le NCSC estime qu’un modèle de langage n’est peut-être pas la bonne solution**[98]**. |

### Dérogations

Un écart à un principe ou à une exigence (identifiant PRIN-xx ou EXIG-xxx-nn) doit faire l’objet d’une dérogation écrite, approuvée par le comité d’architecture et des risques agentiques (ou, pour un agent de classe faible, par délégation à l’architecture d’entreprise, pour 90 jours au plus, par une autre personne que celle qui a instruit la demande), limitée à six mois au plus, assortie de mesures compensatoires et d’un

plan de retour à la conformité, et inscrite au registre (section 11.6). Une dérogation vise un agent ou un composant précis, jamais une catégorie entière; à son échéance, elle ne peut être renouvelée qu’une seule fois, par décision du comité (EXIG-GOV-16); sinon l’écart est corrigé ou l’agent passe à l’état « suspendu ». À l’échéance d’une dérogation qui vise un composant, celui-ci est retiré du catalogue, et les agents qui en dépendent, nommés dans la demande, sont suspendus.

**SANS DÉROGATION POSSIBLE**

Choix du cadre : l’EXIG-GOV-17 est la seule liste des points qui n’admettent aucune dérogation, et cet encadré n’en est qu’un rappel. Elle vise notamment l’autonomie non bornée (NX), l’exécution par un agent seul d’une action de palier P3, l’exploitation d’un agent sans fiche au registre ou sans parrain nommé, l’usurpation, par un agent, de l’identité de son mandant, le dépassement du plafond d’autonomie de la classe de risque, l’autorisation au-delà de N2 d’un agent visé par la règle d’or (EXIG-AUT-07) et le manquement à une obligation légale ou réglementaire.
