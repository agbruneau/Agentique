# Sommaire exécutif

Les agents d’IA ne se contentent plus de répondre : ils lisent des systèmes, prennent des décisions et agissent. Ce cadre fixe les règles communes qui permettent de les brancher aux systèmes de l’entreprise, de les faire collaborer et de les orchestrer de façon sûre, traçable, réversible et économiquement maîtrisée, quel que soit le fournisseur. Il est normatif : les chapitres 5 à 13 énoncent des exigences identifiées, vérifiables en revue d’architecture ou en test ou, à défaut, par une justification consignée (section 1.4).

> **[Figure]**
> - Des agents branchés, collaboratifs et orchestrés
> - de façon sûre, traçable, réversible et économiquement maîtrisée
> - 12 principes directeurs (PRIN-01 à PRIN-12)
> - standards ouverts · contrat avant code · moindre privilège et moindre agence · autonomie proportionnée au risque · réversibilité · simplicité d’abord
> - Interopérabilité
> - MCP 2026-07-28
> - A2A 1.0
> - CloudEvents, AsyncAPI
> - OpenAPI, catalogue
> - 4 niveaux (EIF)
> - chapitre 6
> - Orchestration
> - 8 patrons autorisés
> - agent unique d’abord
> - exécution durable
> - sagas, idempotence
> - dégradation maîtrisée
> - chapitre 7
> - Autonomie
> - niveaux N0 à N4
> - paliers d’outils P0 à P3
> - approbation signée
> - anti-approbation
> - machinale
> - chapitre 8
> - Identité et sécurité
> - confiance zéro
> - délégation RFC 8693
> - passerelle d’agents
> - OWASP ASI, injection
> - bacs à sable
> - chapitre 9
> - Observabilité
> - et FinOps
> - OpenTelemetry GenAI
> - coût par tâche
> - chapitre 10
> - Architecture de référence : six couches et trois plans transversaux (chapitre 5)
> - canaux · orchestration · agents · médiation · outils · systèmes d’enregistrement — identité, observabilité, gouvernance
> - Gouvernance et cycle de vie (chapitre 11)
> - registre · RACI · modèle en étoile · homologation
> - Mise en œuvre : maturité en 5 niveaux, feuille de route en 4 phases, calée sur 2027-2030, indicateurs (chapitres 14 et 15)
> - audit chaîné et ancré
> - évaluation en 3 étages
> - Risques, conformité et approvisionnement (chapitres 12 et 13)
> - Loi 25 · BSIF E-23 · RIA · NIST AI RMF · ISO/IEC 42001 · contrats
> - annexes : grille d’homologation, fiche d’agent, contrats types, registre des exigences, glossaire, validation des sources, références, actualisation

***Figure 1 — Le cadre en une page.** Le toit énonce la finalité; les principes s’appliquent à toutes les décisions; les cinq piliers portent les règles techniques; l’architecture de référence, la gouvernance et la conformité en sont les fondations; la feuille de route en organise le déploiement.*

## Pourquoi maintenant

**40 %** des applications d’entreprise intégreront des agents spécialisés d’ici la fin de 2026, contre moins de 5 % en 2025 (prévision Gartner, août 2025)**[1]**

**> 40 %** des projets d’IA agentique seront annulés d’ici la fin de 2027 : coûts, valeur incertaine, contrôles inadéquats (prévision Gartner, juin 2025)**[3]**

**13 %** des organisations estiment avoir la bonne gouvernance de leurs agents (Gartner, avril 2026; population et méthode non publiées)**[2]**

**> 150 000** agents en usage, en moyenne, par entreprise du Fortune 500 d’ici 2028, contre moins de 15 en 2025 (prévision Gartner, avril 2026, sans méthode publiée : ordre de grandeur prospectif)**[2]**

Les agents se multiplient plus vite que les règles pour les relier**[1, 2]**. Sans cadre commun, chaque équipe recrée ses connecteurs, ses accès et ses contrôles; les annulations annoncées par Gartner tiennent aux coûts, à une valeur d’affaires incertaine et à des contrôles de risque inadéquats, la maturité encore limitée des modèles s’y ajoutant**[3]**. Les standards, eux, se sont consolidés aux couches agent-outil et agent-agent. Le Model Context Protocol (MCP) et le protocole Agent2Agent (A2A) relèvent désormais tous deux de l’Agentic AI Foundation, fondation neutre de la Linux Foundation**[4, 5]**. Selon l’analyse du cadre (section 2.4), le risque de verrouillage s’est déplacé des protocoles vers les plateformes : c’est là que le cadre concentre ses exigences.

## Les dix décisions structurantes

Dix décisions résument le cadre; chacune renvoie au chapitre qui la détaille.

1. **Deux protocoles pivots, versions épinglées.** MCP (révision 2026-07-28) relie un agent à ses outils et à ses données; A2A (version 1.0) relie un agent à un autre agent; CloudEvents et AsyncAPI portent les échanges asynchrones. Les API existantes sont exposées par adaptateurs, sans réécriture de leur logique métier; l’ajout minimal qui rend une écriture idempotente reste permis (EXIG-ARC-14). Les versions de référence sont épinglées au catalogue des protocoles, révisé chaque trimestre; celles que cite le texte en sont les valeurs initiales (section 1.6, chapitre 6).
2. **Rien ne contourne les points d’application.** Hors d’un poste de développement individuel sans justificatif de production, tout appel d’un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3 traversent la passerelle d’agents, qui authentifie, autorise, applique les garde-fous, limite les coûts, injecte les secrets et journalise; l’inférence passe par la passerelle de modèles et les événements par le courtier (EXIG-EVT-07). Un outil absent du catalogue d’entreprise est injoignable. C’est l’état cible : les agents déjà en service à l’adoption y sont ramenés selon le régime transitoire de la section 11.6 (EXIG-GOV-16 et EXIG-GOV-17).
3. **La simplicité d’abord.** Un flux déterministe, assisté au besoin par un modèle, est le choix par défaut; l’agent unique bien outillé vient ensuite, et l’on n’ajoute de la complexité que si elle améliore les résultats de façon démontrée**[6]**; le cadre en tire ses propres règles : le multiagent n’est autorisé que sur preuve mesurée de gain, parmi huit patrons autorisés et avec deux niveaux de délégation au plus (chapitre 7).
4. **Une échelle d’autonomie unique.** Le niveau d’autonomie (N1 à N4; N0 qualifie un flux sans choix laissé au modèle) borne ce qu’un agent peut faire seul, et la classe de risque plafonne ce niveau (EXIG-CON-02); l’autonomie non bornée (NX) est interdite. Les outils sont classés P0 à P3 au catalogue; le contrôle appliqué à un appel réunit tous ceux qu’exigent ces axes (EXIG-AUT-10), et toute action critique, externe ou irréversible (P3) exige une approbation humaine hors bande, signée et liée à l’action exacte (chapitre 8).
5. **Une identité propre à chaque agent, des droits délégués et de courte durée.** Aucun compte partagé ni clé statique (état cible; agents existants : régime transitoire de la section 11.6); quand un agent agit pour une personne, il reçoit un jeton délégué (échange de jetons, RFC 8693) qui identifie à la fois la personne et l’agent, restreint à une seule ressource cible (audience unique), et dont la portée ne s’élargit jamais d’un saut à l’autre (chapitre 9).
6. **Présomption d’injection.** Tout contenu reçu est une donnée, jamais une instruction. Dès qu’une session (la tâche racine et tout ce qui en dérive, section 3.1) a consommé un contenu non fiable, la passerelle lui retire de façon déterministe, pour le reste de la session, les outils d’envoi vers l’extérieur et les outils P3, sauf approbation liée à l’action; le marquage suit la donnée d’un agent à l’autre (EXIG-SEC-04, EXIG-SEC-06); le code qu’il génère s’exécute dans un bac à sable isolé, réseau fermé par défaut (chapitre 9).
7. **Réversibilité par conception.** L’état est enregistré de façon durable hors du modèle à chaque transition; chaque écriture porte une clé d’idempotence; les transactions qui touchent plusieurs systèmes suivent le patron saga avec compensations; un coupe-circuit global est éprouvé à l’exercice trimestriel de l’EXIG-SEC-26, et une saga interrompue reste compensable par un canal distinct (EXIG-ORC-28) (chapitres 7 et 9).
8. **On ne gouverne que ce qu’on voit.** Traçage OpenTelemetry de bout en bout (conventions GenAI épinglées), journal d’audit chaîné et ancré hors du domaine d’administration du service d’audit,
  évaluation en trois étages (E1 à E3), enveloppe budgétaire par tâche et coût par tâche réussie (chapitre 10).
9. **Une personne nommée répond de chaque agent.** Registre d’entreprise obligatoire, cycle de vie à jalons, modèle opérationnel en étoile et comité d’architecture et des risques agentiques (chapitre 11).
10. **Conformité dès la conception.** Loi 25 (évaluation des facteurs relatifs à la vie privée, décisions automatisées, communications hors Québec, incidents), ligne directrice E-23 du Bureau du surintendant des institutions financières (BSIF, pour les institutions financières fédérales) et règlement européen sur l’IA (selon son champ d’application), ainsi que les référentiels volontaires NIST AI RMF et ISO/IEC 42001, sont intégrés aux exigences et à une matrice de correspondance unique (chapitre 12)**[7, 8]**.

## Par où commencer

La mise en œuvre suit quatre phases ouvertes par trois jalons de passage, plus trois jalons de suivi (J2a, J4 et J5), vise le niveau 3 de maturité, « Défini », en 18 mois environ (19 au calendrier du tableau 59, congés compris), puis le niveau 4 et la certification ISO/IEC 42001 aux jalons 4 et 5 (chapitre 14, chapitre 15). Les 90 premiers jours établissent les fondations : inventaire de tous les agents et serveurs MCP, parrain nommé pour chacun, fin des clés partagées, passerelle de modèles, traçage pilote, classement des risques et évaluations de vie privée, coupe-circuit testé. Aucun agent ne passe en production sans franchir la grille d’homologation de l’annexe A. La feuille de route ordonne la planification; l’exigibilité se règle agent par agent, selon les paliers, les niveaux et les topologies qu’il exerce (régime transitoire de la section 11.6).

**CE QUI A CHANGÉ PAR RAPPORT AUX ÉBAUCHES**

La vérification a confirmé le fond technique des ébauches, mais a imposé plusieurs corrections : versions de protocoles mises à jour (MCP sans état, A2A 1.0), trois échelles d’autonomie incompatibles remplacées par une seule, chiffres de marché réattribués à leur véritable source ou retirés, obligations de la Loi 25 rattachées aux bons articles, allégations commerciales retirées des exigences. L’annexe F en donne le détail.
