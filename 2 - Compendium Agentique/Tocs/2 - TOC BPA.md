# TOC — Table des matières commentée de la monographie

| Champ | Valeur |
|---|---|
| Version | 1.5 (**v1.5, suites de l'audit global — 17 juill. 2026** : les **trois dettes vivantes** du découpage sont éteintes, toutes trois signalées par [`audit.md`](audit.md) (racine G-3). **Ch. 15 §15.4** — « richesse des données » → « couche sémantique commune » : le chapitre publié portait « l'amendement de TOC.md reste dû » depuis son gel, sa demande n'avait jamais été honorée, et **la bijection J-2 était fausse dans le fichier qui en fait le critère de sortie**. **Ch. 16 §16.2** — « Scénarios d'articulation » → « Conditions de possibilité » : déviation fondée du chapitre (le socle ne porte ni mandat ni structure de message AP2, §10.9e), mais **silencieuse** — une déviation juste non déclarée est indiscernable d'un oubli. **Ch. 7** — « support MCP **généralisé** » → « répandu et inégalement établi » : le corps du chapitre réfutait sa propre thèse deux fois, sur pièces. S'y ajoute la **thèse du ch. 15**, dont le futur catégorique non attribué (« le RTR **naîtra** ») était recopié fidèlement par le bandeau du chapitre alors que son corps attribuait partout. *Enseignement commun aux quatre : dans chaque cas, la rédaction avait lu le socle mieux que le plan — et c'est le plan qui n'avait pas suivi.* / v1.4, clôture de P3 : arbitrages rendus sur les remontées en souffrance. Ch. 13 — la table du §13.1 passe de **six à onze entrées**, la dérivation des attentes d'E-23 ayant été arbitrée et conduite ; renvois **F-10 et F-35 entérinés**. Ch. 18 — socle **« transversal » entériné** et règle étendue aux chapitres de synthèse (18-21) : l'en-tête est construit par la rédaction, à charge pour elle d'énumérer ce qu'elle mobilise. Volumétries réelles portées au regard des cibles, écarts documentés et non corrigés — méthode de décompte : PRDPlan §4.2. / v1.2 : réalignement sur le PRD v1.3 après la passe P0 — F-47/F-48, R-8, recaractérisation de C-36, clôture Confluent ; correction du décompte de volumétrie de la Partie IV. **v1.2, retours de la rédaction du ch. 1** : thèse du ch. 1 corrigée — « dix-huit mois » → **dix-sept** (nov. 2024 → communiqué LF du 9 avril 2026, F-02) ; encadré de désambiguïsation R-8 **déplacé du ch. 3 au ch. 1 §1.2**, première occurrence réelle du sigle dans l'ouvrage ; F-04 ajouté au socle du ch. 1 en renvoi. **v1.3, retours de P2 (16 juill. 2026)** : adjectif « indépendantes » retiré de l'abstract — réfuté par le socle (F-46 corrigé, PRD v1.5) ; thèses des ch. 2 et 4 corrigées — elles portaient un universel et une datation que le socle ne soutient pas ; R-8 porté à quatre branches et réassigné au ch. 1 §1.2 ; lacunes §10.7 à §10.10 assignées) |
| Date | 17 juillet 2026 |
| Statut | Livrable du jalon J-2 (PRD §12 ; PRDPlan P1) — amendé par les retours de P2, puis par les arbitrages de clôture de P3 |
| Gouvernance | [PRD.md](PRD.md) v1.10 (contenu, socle, garde-fous) ; [PRDPlan.md](PRDPlan.md) v1.4 (exécution) |
| Règle | Chaque chapitre est tracé au socle (F-xx) et à ses garde-fous (R-x) ; toute modification de ce découpage passe par une mise à jour de ce fichier (version++) |

---

## Titre

# L'autonomie encadrée
## Interopérabilité et orchestration agentique dans les services financiers canadiens — protocoles ouverts, cadre réglementaire et blueprint d'intégration d'entreprise (état des lieux 2024-2026)

## Abstract

Entre 2024 et 2026, deux trajectoires jusque-là parallèles ont convergé dans les services financiers canadiens. D'un côté, les protocoles d'interopérabilité agentique — MCP pour l'accès des agents aux outils, A2A pour la collaboration entre agents, AP2 pour la transaction, AGNTCY pour l'infrastructure — sont passés de projets propriétaires à des projets ouverts, s'intégrant aux grandes plateformes infonuagiques ; trois d'entre eux sont désormais placés sous gouvernance de fondation — le socle ne documente aucun transfert de gouvernance pour AP2 —, et deux ont atteint une première version stable (A2A v1.0 ; révision MCP du 25 novembre 2025). De l'autre, les institutions financières canadiennes ont fait passer l'intelligence artificielle agentique en production — pré-adjudication hypothécaire, traitement autonome de courriels commerciaux, plateformes agentiques d'entreprise — pendant que le cadre réglementaire se réorganisait : ligne directrice E-23 du BSIF et ligne directrice sur l'IA de l'AMF, toutes deux en vigueur le 1er mai 2027, cadre des services bancaires axés sur le consommateur confié à la Banque du Canada, achèvement de la migration ISO 20022 sur Lynx et lancement imminent du Real-Time Rail.

Cette monographie soutient une thèse d'architecture : **l'autonomie encadrée** (*framed autonomy*) constitue l'état de l'art convergent pour déployer des systèmes multi-agents en contexte financier réglementé. Trois sources — le manifeste académique de l'Agentic Business Process Management, les travaux empiriques sur les options d'orchestration, et l'architecture de référence agentique d'IBM — formulent le même principe : les processus sous exigence réglementaire stricte s'exécutent dans des cadres déterministes qui orchestrent les agents, jamais l'inverse. L'ouvrage établit que ces trois sources ne sont pas indépendantes — deux partagent une autrice, deux une organisation — et en tire la portée exacte de leur convergence plutôt que d'en majorer l'autorité (ch. 13). La monographie déploie cette thèse en sept parties : les protocoles (I), l'orchestration d'entreprise (II), le cadre réglementaire canadien (III), l'interopérabilité financière canadienne (IV), l'adoption par les institutions (V), la synthèse architecturale (VI) et un blueprint détaillé de plateforme d'intégration d'entreprise instancié sur le portefeuille IBM (VII).

La méthode est celle du PRD qui gouverne l'ouvrage : un socle factuel daté et cité, constitué par vérification adversariale multi-juges et consultation directe des sources officielles, avec niveaux de preuve explicites, attribution systématique des métriques auto-déclarées, distinction stricte entre lien documenté et inférence d'auteur, et exposition honnête des lacunes. Publics visés : architectes d'entreprise et directions technologiques des institutions financières canadiennes, responsables risque et conformité, directions stratégie et chercheurs.

*(≈ 340 mots)*

---

## Volumétrie d'ensemble

| Bloc | Chapitres | Cible (mots) | **Réel (17 juill. 2026)** | Écart |
|---|---|---|---|---|
| Avant-propos et note méthodologique | — | 2 500 | **2 319** | −7 % |
| Partie I | 1–4 | 11 000 | 11 254 | +2 % |
| Partie II | 5–8 | 12 000 | 12 779 | +6 % |
| Partie III | 9–13 | 14 000 | **16 349** | **+17 %** |
| Partie IV | 14–16 | 8 000 | 8 505 | +6 % |
| Partie V | 17 | 8 000 | **9 140** | **+14 %** |
| Partie VI | 18–21 | 10 500 | 11 927 | +14 % |
| Partie VII | 22–24 | 10 000 | 11 025 | +10 % |
| Annexes (A–D) | — | 6 000 | **8 761** | **+46 %** |
| **Total** | **24 (+ 5 pièces)** | **≈ 82 000** | **92 059** | **+12,3 %** |

*Décompte revérifié le 16 juillet 2026 (v1.1) : la somme par chapitre fait autorité et concorde avec les 24 gabarits de `monographie/`. La Partie IV était annoncée à 8 500 mots pour 8 000 réels (3 000 + 2 800 + 2 200) ; total corrigé de 82 500 à 82 000.*

*Colonne « Réel » ajoutée le 17 juillet 2026 (P4.3), mesurée sur les 29 pièces par la **commande de référence** de PRDPlan §4.2 — la seule autorité de décompte depuis cette date. **Aucun de ces chiffres n'est estimé.** Les décomptes que les rédactions publiaient auparavant employaient chacune leur commande maison et ne sont pas comparables entre eux ; ils sont périmés.*

*⚠ **Ces chiffres sont la QUATRIÈME mesure** (17 juill. 2026, après la passe corrective de l'audit global — les 29 pièces re-mesurées une à une par la commande de référence, la somme des blocs recomposée et confrontée au total : 92 059 des deux côtés). La troisième portait **90 362** ; les **+1 697 mots** de cette passe sont, eux aussi, intégralement des correctifs de conformité — marquages de strates de F-09, encadrés convertis au gabarit qui n'induit pas de fabrication, attestations rectifiées, gloses hors socle retirées et remplacées par ce que le socle porte. **Aucun n'ajoute une thèse ; tous ajoutent une réserve.** L'historique qui suit est conservé : il est l'argument.*

*⚠ **La troisième mesure, et l'histoire des deux qui la précèdent** — l'aveu vaut mieux qu'une colonne propre. (1) La colonne a d'abord porté **89 757** : la commande de référence, à sa première rédaction, ne s'arrêtait qu'à « ## Notes » — que **trois pièces sur vingt-neuf n'ont pas** — et comptait alors leur bloc de gouvernance en commentaire (annexe C : 2 897 annoncés pour 1 656). Défaut relevé par la relecture adversariale de l'avant-propos, non par la passe qui avait fixé la commande : **elle l'avait testée sur deux fichiers et publiée comme référence pour vingt-neuf**. (2) La deuxième mesure (**88 021**) a été prise avant que les correctifs des relectures adversariales ne soient tous appliqués. (3) Celle-ci est postérieure à la dernière correction. Un décompte n'est vrai qu'à sa date, et cette ligne le dit plutôt que de laisser croire à une mesure unique.*

*⚠ **Le total dépasse le plafond indicatif du plan de 2 059 mots** (PRDPlan §1.1 : 60 000 à 90 000, fourchette explicitement « ajustable, non normative »). Le dépassement est **constaté, non résorbé** — et il faut dire pourquoi, car la tentation inverse serait la faute. Les 2 341 mots ajoutés entre la deuxième et la troisième mesure, puis les **1 697** ajoutés par la passe corrective de l'audit, sont **intégralement** des correctifs de relecture : marquage de strates de preuve, bornage d'inférences, conversion d'encadrés au gabarit qui n'induit pas de fabrication, attribution de métriques auto-déclarées, retrait de définitions que le socle ne portait pas, rectification d'attestations fausses. **Rentrer sous 90 000 supposerait de retirer exactement ce que ces relectures ont ajouté** — c'est-à-dire de troquer une conformité de forme contre une régression de fond. La volumétrie est indicative ; la traçabilité ne l'est pas. PRDPlan §4.2 le dit en une ligne : « un écart se documente, il ne se corrige pas par amputation ».*

*Les écarts sont donc **documentés et non corrigés**. Trois méritent leur explication. **Partie III (+16 %)** : le ch. 13 pèse 5 089 mots pour 3 400 visés, la dérivation des attentes d'E-23 (arbitrage du 17 juillet) y ayant ajouté cinq lignes de tableau, la garde « E-23 attend un programme, non une architecture » et les correctifs de sa relecture. **Annexes (+41 %)** : le bloc a absorbé le plus gros des correctifs — l'annexe D à elle seule a gagné §D.7 (trois garde-fous manquants, dont R-6 en entier) et cinq entrées ramenées à ce que leur F-xx porte réellement. **Avant-propos (−13 %)** : le seul écart en défaut, non comblé — ajouter des mots pour atteindre une cible indicative serait exactement la faute inverse de celle que la volumétrie prétend prévenir.*

---

## Avant-propos et note méthodologique *(fichier : `monographie/00-avant-propos.md`)*

Origine du projet ; méthode (renvoi PRD Annexe A) ; niveaux de preuve [A]/[B]/[C] expliqués au lecteur ; convention de datation (date de gel par chapitre) ; avertissements (pas de conseil juridique ni d'investissement — PRD §3 non-objectifs ; neutralité fournisseur — PRD §8.4). *Socle : PRD Annexe A. Volumétrie : ~2 500.*

---

## Partie I — Fondements : les protocoles d'interopérabilité agentique

### Chapitre 1 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts
**Thèse** : en **dix-sept** mois, la couche protocolaire agentique s'est consolidée sous gouvernance neutre (Linux Foundation), condition de sa crédibilité en entreprise réglementée.
Sections : 1.1 Chronologie 2024-2026 (MCP nov. 2024 → Agentic AI Foundation déc. 2025 ; A2A avril 2025 → LF juin 2025 → v1.0 ; AGNTCY mars → juillet 2025) ; 1.2 Gouvernance comparée (fondations, comités techniques — IBM Research au TSC d'A2A) **+ encadré de désambiguïsation R-8** (voir ci-dessous) ; 1.3 Lecture critique des métriques d'adoption (« soutien ≠ production »).
*Socle : F-01, F-02, F-04 (renvoi — AP2 n'a aucun transfert de gouvernance documenté), F-05, F-43. Garde-fous : §8.2.1, **R-1, R-8**. Fichier : `01-partie-I/ch-01-genealogie-gouvernance.md`. ~2 800 mots.*
> ⚠ **Correctif de la rédaction (16 juill. 2026)** : la thèse portait « dix-huit mois » ; le calcul exact (nov. 2024 → communiqué LF du 9 avril 2026, F-02) donne **dix-sept**. Par ailleurs, la généalogie du ch. 1 rencontre le sigle « ACP » **avant** le ch. 3 : l'encadré de désambiguïsation R-8, initialement prévu au ch. 3 §3.4, est **déplacé ici** (première occurrence réelle dans l'ouvrage) ; le ch. 3 le rappelle et le développe. La rédaction y a relevé une **quatrième branche** (composante ACP d'AGNTCY, F-05), exposée en encadré et portée en lacune (§10.7).

### Chapitre 2 — Anatomie technique : MCP et A2A v1.0, une complémentarité déclarée
**Thèse** : « MCP dans les agents, A2A entre les agents » — la doctrine de complémentarité **déclarée par le projet A2A** (F-16) fournit le premier critère de découpage d'une architecture agentique ; elle n'est pas un accord entre les deux projets.
> ⚠ **Correctif de la rédaction (16 juill. 2026)** : le titre portait « deux protocoles complémentaires » et la thèse « la doctrine **officielle** de complémentarité **structure toute** architecture agentique ». Deux fautes : (1) l'attribution manquait — F-16 énonce une doctrine **du projet A2A**, non un accord des deux projets ; (2) « structure toute architecture agentique » est un universel que ni F-16 ni le chapitre ne portent (§2.4 conclut « un critère n'est pas une contrainte »). Corrigé conformément à ce que le chapitre rédigé démontre.
Sections : 2.1 MCP (JSON-RPC 2.0, cadre d'autorisation OAuth — dire « cadre », pas « sécurisé » ; révision de spécification **2025-11-25**) ; 2.2 A2A v1.0 (Agent Cards signées, multi-protocole, multi-location ; ligne v1.0.1 au 28 mai 2026) ; 2.3 Intégrations infonuagiques (Azure, AWS, Google Cloud) ; 2.4 La complémentarité en pratique.
*Socle : F-01, F-02, F-03, F-16. Garde-fous : réserve F-01. Fichier : `01-partie-I/ch-02-anatomie-mcp-a2a.md`. ~3 000 mots.*
> ⚠ **Fait chaud (P4.1)** : une *release candidate* MCP majeure (protocole sans état, retrait de `Mcp-Session-Id`) est prévue en finalisation le **28 juillet 2026** — postérieure à la date de gel prévisible de ce chapitre. Rédiger la révision 2025-11-25 comme état daté, et revalider en P4.1 avant publication.

### Chapitre 3 — La transaction agentique et la couche d'infrastructure : AP2 et AGNTCY
**Thèse** : la transaction pilotée par agents (AP2) est l'aboutissement financier de la pile protocolaire ; AGNTCY en est la couche d'infrastructure, non un concurrent.
Sections : 3.1 AP2 (60+ organisations financières — endossement, pas production) ; 3.2 AGNTCY (annuaires, transport SLIM) ; 3.3 Le destin d'ACP : fusion dans A2A (généalogie IBM Research — **chapitre à plus haut risque R-1**) ; 3.4 Désambiguïsation **R-8** : **rappeler** ici l'encadré posé au ch. 1 §1.2 (première occurrence du sigle dans l'ouvrage) et le développer sur le versant protocolaire — les quatre branches, dont la composante ACP d'AGNTCY (F-05) dont l'identité n'est pas établie par le socle (lacune §10.7). Ne pas dupliquer l'encadré du ch. 1.
*Socle : F-04, F-05, F-43 ; réserve F-06 (feuille de route académique obsolète comme prescription). Garde-fous : R-1, **R-8**. Fichier : `01-partie-I/ch-03-ap2-agntcy-acp.md`. ~2 600 mots.*

### Chapitre 4 — Taxonomie des risques protocolaires
**Thèse** : la sécurité des protocoles dépend de l'implémentation ; empoisonnement d'outils et injection d'invites sont **nommés par les protocoles eux-mêmes comme risques attachés**, sans que le socle en date la documentation ni en établisse la mécanique.
> ⚠ **Correctif de la rédaction (16 juill. 2026)** : la thèse portait « documentés **dès l'origine** ». Aucun appui au socle : F-01 nomme ces deux risques dans sa réserve **sans les dater**, et la date de l'annonce d'Anthropic (nov. 2024) ne vaut pas date de documentation. Une thèse de TOC n'est pas une entrée du socle et ne peut pas en tenir lieu. La minceur du socle sur ce chapitre est portée en lacune §10.8.
Sections : 4.1 Surface d'attaque (outils, invites, mémoire) ; 4.2 Réponses protocolaires (Signed Agent Cards, autorisation) ; 4.3 Ce que les protocoles ne couvrent pas (renvoi aux passerelles, Partie VII).
*Socle : F-01, F-02, F-36 (défi C2). Garde-fous : réserve F-01 (« cadre d'autorisation », jamais « sécurisé » — chapitre où le motif est le plus probable). Fichier : `01-partie-I/ch-04-risques-protocolaires.md`. ~2 600 mots.*

---

## Partie II — L'orchestration multi-agents en entreprise

### Chapitre 5 — Les options d'orchestration : la taxonomie OO1–OO4
**Thèse** : le choix d'architecture agentique est un choix de position sur un continuum d'encadrement, objectivable par cinq propriétés et sept critères.
Sections : 5.1 OO1–OO4 ; 5.2 Cinq propriétés (autonomie, spécificité, réactivité, correction, traçabilité/tractabilité) ; 5.3 Critères de sélection ; 5.4 Métriques quantitatives (chiffres cités comme illustration seulement — préprint).
*Socle : F-37. Garde-fous : réserves F-37. Fichier : `02-partie-II/ch-05-options-orchestration.md`. ~3 200 mots.*

### Chapitre 6 — L'autonomie encadrée : le paradigme APM
**Thèse** : l'autonomie n'est pas l'automatisation ; elle se gouverne par des frames normatifs et opérationnels et quatre capacités (encadrement, explicabilité, actionnabilité conversationnelle, auto-modification).
Sections : 6.1 Système APM et distinction autonomie/automatisation ; 6.2 Frames normatifs vs opérationnels, trois scénarios ; 6.3 Quatre capacités ; 6.4 Frames locaux comme frontière de sécurité ; 6.5 « Responsibility gap » (défi C4 — préparé ici, exploité au ch. 13).
*Socle : F-36. Garde-fous : R-1 (mention ACP du manifeste antérieure à la fusion). Fichier : `02-partie-II/ch-06-autonomie-encadree.md`. ~3 200 mots.*

### Chapitre 7 — Réalisations : les frameworks d'orchestration d'entreprise
**Thèse** : l'offre s'est industrialisée en 2025-2026 — successions assumées (Agent Framework), plateformes GA (LangGraph), orchestration événementielle (Confluent/Kafka) — avec un support MCP **répandu et inégalement établi** et un support A2A désormais attesté de première main, mais de périmètre inégal.
> ⚠ **Correctif de la rédaction (17 juill. 2026, suites de l'audit — constat m-12)** : la thèse portait « un support MCP **généralisé** ». Le ch. 7 l'a réfutée deux fois sur pièces dans son propre corps — « deux offres sur cinq, non "généralisé" » (§7.5) — et le socle ne documente aucune source de première main pour le support MCP de LangGraph (F-32 : « le billet GA ne mentionne ni MCP ni A2A »). **La thèse est alignée sur le corps**, et non l'inverse : c'est le chapitre qui a lu le socle. *Une thèse de TOC n'est pas une entrée du socle et ne peut pas en tenir lieu — le conflit en-tête/corps a vécu dans la pièce publiée faute d'avoir été remonté.*
Sections : 7.1 Microsoft Agent Framework ; 7.2 LangGraph Platform (support A2A confirmé **pour la plateforme commerciale seulement** — le cœur open source `langgraph` ne l'a pas, distinction à tenir) ; 7.3 Orchestration événementielle (Streaming Agents, A2A sur Kafka ; Confluent acquise par IBM, clôture le 17 mars 2026 — renvoi ch. 22) ; 7.4 Encadrés : Temporal [C] ; CrewAI (support A2A et MCP documenté de première main [B] ; chiffres d'adoption auto-déclarés — §8.2.3) ; 7.5 Grille de lecture OO1–OO4 des patrons (graphes, checkpointing, humain-dans-la-boucle, agents durables, bus d'événements).
*Socle : F-15, F-16, F-32, F-33, F-41 (renvoi). Garde-fous : §8.2.3 ; lacune §10.3 (réduite en P0 : ne subsiste que Temporal). Fichier : `02-partie-II/ch-07-frameworks.md`. ~3 200 mots.*

### Chapitre 8 — L'identité et les registres d'agents
**Thèse** : l'identité des agents s'ancre dans les standards existants (OAuth/OIDC, SCIM) ; le registre d'agents gouverné devient la pièce maîtresse de la conformité à venir.
Sections : 8.1 Entra Agent ID (GA, licences, extensions des RFC) ; 8.2 Spécification CSA (brouillon : `toolAccessList`, `permissionBoundaries`) ; 8.3 Trajectoire IETF (draft expiré, consolidation) ; 8.4 Ce qui n'existe pas encore (**R-2, R-3**).
*Socle : F-07, F-08. Garde-fous : R-2, R-3, §8.2.5. Fichier : `02-partie-II/ch-08-identite-registres.md`. ~2 400 mots.*

---

## Partie III — Le cadre réglementaire canadien

### Chapitre 9 — E-23 : le risque de modèle à l'ère de l'IA
**Thèse** : E-23 couvre l'IA agentique *implicitement*, par sa définition de « modèle » — une couverture par inférence d'analystes que les institutions doivent traiter comme acquise d'ici le 1er mai 2027.
Sections : 9.1 Genèse et calendrier ; 9.2 La définition de « modèle » et l'anticipation des systèmes autonomes ; 9.3 L'inférence agentique (formulation obligatoire §8.2.4) ; 9.4 Le rapport BSIF-ACFC (30 % → 50 % → 70 % projeté ; risque de causalité indéterminable).
*Socle : F-09, F-10. Garde-fous : §8.2.4, §8.2.6. Fichier : `03-partie-III/ch-09-e23-risque-modele.md`. ~3 000 mots.*

### Chapitre 10 — Le vide fédéral : de C-27 à C-36
**Thèse** : la mort de la LIAD laisse le Canada sans régulation fédérale spécifique de l'IA ; C-36 ne comble pas ce vide — c'est une loi de protection des renseignements personnels — et la couverture effective passe donc par les régulateurs sectoriels.
Sections : 10.1 Prorogation du 6 janvier 2025 et mort de C-27 ; 10.2 Ministre de l'IA et projet de loi **C-36 (*Protecting Privacy and Consumer Data Act*)** : réforme de la LPRPDE et création de la *Digital Safety and Data Protection Commission of Canada*, 1re lecture le 15 juin 2026 — **formulation obligatoire : loi sur la vie privée portant des volets IA (transparence algorithmique, droit à l'effacement, données des enfants), et non loi IA autonome de type LIAD** ; 10.3 Conséquences pour les institutions financières : le vide IA fédéral persiste (le Canada demeure sans cadre IA contraignant), la charge repose sur E-23, l'AMF et l'ACVM.
*Socle : F-24 [B, revalidé le 16 juill. 2026]. Fichier : `03-partie-III/ch-10-vide-federal-c36.md`. ~2 400 mots.*

### Chapitre 11 — Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25
**Thèse** : le Québec dispose du cadre le plus explicite — et l'art. 12.1 (révision humaine sur demande) entre en friction directe avec la décision agentique autonome.
Sections : 11.1 Ligne directrice AMF (projet → finale 30 mars 2026 → 1er mai 2027, convergence avec E-23) ; 11.2 Art. 12.1 : les trois obligations (texte officiel) ; 11.3 Le critère « exclusivement » et l'humain-dans-la-boucle (nuance Fasken vs positions CAI — encadré lacune §10.4) ; 11.4 Conséquences d'architecture (préparé pour ch. 13 et 23).
*Socle : F-25, F-27. Garde-fous : réserve F-25 (« jamais “en attente” »). Fichier : `03-partie-III/ch-11-quebec-amf-loi25.md`. ~3 000 mots.*

### Chapitre 12 — Valeurs mobilières : l'avis ACVM 11-348
**Thèse** : les lois existantes s'appliquent — la définition retenue des systèmes d'IA (autonomie et adaptativité variables) capture nativement l'agentique.
Sections : 12.1 Portée et doctrine (« ne crée ni ne modifie aucune exigence ») ; 12.2 Attentes (gouvernance, explicabilité, supervision) ; 12.3 Suites de la consultation (encadré lacune §10.4).
*Socle : F-26. Fichier : `03-partie-III/ch-12-acvm-11-348.md`. ~2 200 mots.*

### Chapitre 13 — Le pont : des contraintes réglementaires aux frames déterministes
**Thèse** (pivot de l'ouvrage) : **la plupart des exigences canadiennes lues** se traduisent en frame d'architecture — neuf des onze entrées de la table du §13.1 —, et la forme de cette table mesure ce que le socle a extrait, non l'exigence propre des textes ; l'encadrement déterministe des processus réglementés est le principe sur lequel convergent trois sources **non indépendantes**, dont le socle n'établit l'application ni au Canada ni à la finance canadienne ; le « responsibility gap » éclaire l'imputabilité — sous l'article 12.1 du moins, elle pèse sur l'assujetti, qui ne peut désigner de tiers.
> ⚠ **Correctif de la relecture adversariale (17 juill. 2026)** : la thèse portait « **chaque** exigence réglementaire canadienne se traduit en frame » et « l'orchestration non encadrée **est indéfendable** en contexte réglementé ». Deux fautes, et ce sont exactement les deux classes que la v1.3 avait corrigées pour les ch. 2 (« structure **toute** architecture agentique » — universel) et 4 (« dès l'origine » — datation non soutenue) : **le chapitre pivot y avait échappé seul**. (1) « Chaque » est un universel que le chapitre réfute lui-même — la ligne directrice de l'AMF ne produit rien, et le chapitre en fait un argument. (2) « Est indéfendable » est un verdict ; le chapitre écrit noir sur blanc « il ne dit pas que l'orchestration non encadrée soit *démontrée* indéfendable au Canada » — le verdict dont il part est **européen, hors finance, tiré d'un préprint** dont les auteurs déclarent des menaces à la validité. Une thèse de TOC n'est pas une entrée du socle et ne peut pas en tenir lieu. Corrigée conformément à ce que le chapitre démontre.
Sections : 13.1 Table de traduction exigences → frames ; 13.2 Le verdict empirique (F-37) et la convergence à trois sources (F-36, F-37, F-46) ; 13.3 L'imputabilité : qui répond du comportement émergent ? ; 13.4 Énoncé du principe directeur repris en Parties VI-VII.
*Socle : F-09 (**les deux strates** — [A] pour le périmètre, [B] pour les attentes opératoires traduites au §13.1), F-25, F-26, F-27, F-36, F-37, F-46 ; **F-10 et F-35 en renvoi — entérinés** (voir ci-dessous). Fichier : `03-partie-III/ch-13-pont-frames.md`. ~3 400 mots (5089 au décompte de référence du 17 juill. 2026, après relecture adversariale — écart de +50 % documenté et non corrigé : PRDPlan §4.2).*
> ⚠ **Arbitrage de clôture de P3 (17 juill. 2026)** — trois décisions sur ce chapitre. (1) **La table du §13.1 passe de six à onze entrées.** Le premier jet n'y faisait produire à E-23 qu'un périmètre : le socle ne portait alors du texte que sa définition de « modèle ». L'extraction du 16 juillet y a versé les attentes opératoires en niveau **[B]** ; le chapitre, pris dans une passe strictement correctrice, avait refusé de les traduire et signalé qu'il *sous-employait sciemment son socle jusqu'à arbitrage*. **Arbitrage : dériver.** Cinq entrées E-23 ajoutées (inventaire, cotation, cycle de vie, documentation, surveillance continue) ; **neuf** des onze entrées produisent une contrainte, **une seule** — la ligne directrice de l'AMF, dont le socle ne porte que le calendrier — n'en produit aucune. (2) **Renvois F-10 et F-35 entérinés** : F-10 est assigné à la Partie III par PRD §6 et le ch. 9 §9.4 désigne explicitement le ch. 13 comme le lieu d'exploitation de son inférence ; F-35 n'est mobilisé que comme **forme** (renvoi de méthode — figure du fait négatif vérifié), aucun de ses faits n'étant repris. (3) La dérivation ne change pas la thèse : elle en déplace l'appui. Le chapitre avait posé que « la densité de contraintes dérivables d'un texte mesure ce que le socle en a extrait, non son exigence propre » — **sa propre correction le vérifie**.

---

## Partie IV — L'interopérabilité financière canadienne

### Chapitre 14 — Le cadre des services bancaires axés sur le consommateur
**Thèse** : le cadre est légiféré (C-15), supervisé par la Banque du Canada, réglementairement en cours — et son standard technique n'est **pas** désigné (fait négatif vérifié).
Sections : 14.1 De 2024 à C-15 (abrogation/remplacement, mobilité des données LPRPDE) ; 14.2 Supervision Banque du Canada, accréditation, registre ; 14.3 Règlement prépublié (27 juin 2026, entrée en vigueur échelonnée) ; 14.4 Le standard technique : organisme à désigner par arrêté (**R-5** — FDX = anticipation d'industrie).
*Socle : F-11, F-23, F-34, F-35. Garde-fous : R-5, §8.3. Fichier : `04-partie-IV/ch-14-cadre-bancaire.md`. ~3 000 mots.*

### Chapitre 15 — ISO 20022 : Lynx accompli, RTR imminent
**Thèse** : la couche sémantique commune des paiements canadiens est en place — Lynx a achevé sa bascule ; **Paiements Canada annonce un RTR nativement ISO 20022 dès son lancement, visé au T4 2026**.
Sections : 15.1 Lynx : fin de coexistence MT/MX (22 nov. 2025, alignée CBPR+) ; 15.2 RTR : chronologie vérifiée, partenaires de livraison (IBM Canada, CGI, Interac — et Deloitte Canada, rôle non détaillé par la source), **cible** T4 2026 (**R-4** ; historique de reports ; tests industriels en cours à la mi-2026) ; 15.3 By-law no 10 (Gazette partie II, 1er juill. 2026 ; en vigueur le 24 août 2026) ; 15.4 **Ce que la couche sémantique commune change — et ce que le socle n'en dit pas** (intitulé aligné le 17 juill. 2026 sur le titre exact du chapitre, pour la bijection J-2 stricte : le chapitre annonce aussi le versant négatif — F-28/F-29 ne documentent aucun attribut de richesse des données).
> ⚠ **Deux correctifs de la rédaction (17 juill. 2026, suites de l'audit — constats M-11 et obs. 18)**. **(1) §15.4** était prévue sous « Ce que la **richesse des données** change pour les agents » : F-28 et F-29 **ne documentent aucun attribut de richesse des données** — ni structure des données de remise, ni granularité des identifiants, ni comparaison avec le format retiré. La section prévue ne pouvait pas être écrite ; le chapitre a livré la section soutenable et **a déclaré l'amendement dû** — il est ici exécuté, avec cinq mois de retard sur sa propre demande. *Un chapitre publié qui porte « l'amendement reste dû » est une dette que seul le TOC peut éteindre : la rédaction avait fait sa part.* **(2) La thèse** portait « le RTR **naîtra** nativement ISO 20022 » — futur catégorique **non attribué**, sur un système que le socle dit non lancé et dont la cible a été reportée quatre fois (réserve F-29). Le corps du chapitre attribuait correctement à ses trois occurrences ; **c'est la thèse du TOC qui portait la faute**, et les chapitres la recopiaient fidèlement dans leur bandeau.
*Socle : F-28, F-29, F-45. Garde-fous : R-4. Fichier : `04-partie-IV/ch-15-iso20022-lynx-rtr.md`. ~2 800 mots.*

### Chapitre 16 — Prospective : AP2 sur les rails canadiens ?
**Thèse** (chapitre explicitement prospectif) : aucune source ne documente l'articulation AP2 ↔ rails canadiens — le chapitre pose le cadre d'analyse et les conditions de possibilité, sans affirmer.
Sections : 16.1 État de la question (lacune §10.5 assumée) ; 16.2 **Conditions de possibilité** ; 16.3 Questions de recherche.
> ⚠ **Correctif de la rédaction (17 juill. 2026, suites de l'audit — constat m-23)** : la section 16.2 était prévue sous « Scénarios d'articulation (mandats de paiement agentiques vs RTR/Interac) ». Deux obstacles de socle, tous deux dirimants : (1) le socle **ne porte ni structure de message, ni mandat, ni preuve d'intention pour AP2** (§10.9e) — la section prévue ne peut pas être écrite sans inventer ; (2) « énumérer des conditions de possibilité n'est pas prédire », et des *scénarios* dans un chapitre dont la thèse est qu'« aucune source ne documente » l'articulation, c'est la lacune §10.5 comblée par de la fiction. **Le chapitre a dévié à raison ; le TOC est aligné sur lui.** *Cette déviation était fondée mais **silencieuse** — sans encadré de correctif ni remontée, à la différence du ch. 15. La bijection J-2 était rompue sans que rien ne le dise : une déviation juste doit se déclarer, sinon elle est indiscernable d'un oubli.*
*Socle : F-04, F-29 ; lacune §10.5. Fichier : `04-partie-IV/ch-16-ap2-rails.md`. ~2 200 mots.*

---

## Partie V — L'adoption par les institutions financières canadiennes

### Chapitre 17 — Études de cas : la production agentique canadienne (2025-2026)
**Thèse** : l'agentique canadienne est en production, documentée par sources primaires, gouvernée au niveau C-suite — et inégalement documentable selon les institutions.
Sections : 17.1 TD (Layer 6, pré-adjudication RESL — 15 h → <3 min, *déclaré*) ; 17.2 Scotiabank (AIDox — ~90 % de ~1 500 courriels/jour, *déclaré* ; revue éthique graduée ; membre du consortium de l'*Agentic Control Plane* — renvoi 17.8) ; 17.3 RBC (AI Group, ATOM/Assist/Aiden/Lumina, cible 700 M$–1 G$, FINOS) ; 17.4 Manuvie (runtime Akka, 1 G$+, Global CAIO) ; 17.5 Desjardins (plan 2026-2029, accréditation à venir) ; 17.6 CIBC (CAI — assistive, **ne pas surqualifier**) ; 17.7 Intact (~600 modèles, 200 M$+/an — sans terminologie agentique) ; 17.8 **BMO et Sun Life après la passe P0** — BMO (F-47) : Lumi [B] (accès temps réel aux politiques et procédures FR/EN ; le chiffre ~8 000 désigne des **employés**, pas des politiques — attribuer à la soumission Qorus, distincte du communiqué), bootcamps agentiques [B, attribués au Vector Institute], facteur de risque matériel gen-IA **en encadré [C]** ; Sun Life (F-48) : consortium Lightworks–Scotiabank–Sun Life–TELUS et son « Agentic Control Plane » [B] avec **note R-8** (homonymie avec l'ACP protocolaire du ch. 3 — aucun lien), agents d'adhésion/relevés fiscaux/réclamations **en encadré [C]**, à attribuer à The Logic si cités ; BNC : absence documentée de sources primaires ; 17.9 Gouvernances comparées et code de conduite volontaire.
*Socle : F-17 à F-23b, F-30, F-31, **F-47, F-48**. Garde-fous : règle transversale §7.5 (attribution à CHAQUE occurrence), §8.2.2, **R-8**. Fichier : `05-partie-V/ch-17-etudes-de-cas.md`. ~8 000 mots.*

---

## Partie VI — Synthèse : l'architecture de référence

### Chapitre 18 — La matrice protocoles × exigences réglementaires
**Thèse** : croiser la pile protocolaire (MCP/A2A/AP2) avec les exigences canadiennes (E-23, AMF, art. 12.1, 11-348, cadre bancaire) révèle où les standards suffisent et où l'architecture doit compenser.
Sections : 18.1 Construction de la matrice ; 18.2 Lecture par protocole ; 18.3 Lecture par exigence ; 18.4 Zones de compensation architecturale.
*Socle : **transversal (I-IV) — assignation délibérée, entérinée le 17 juill. 2026** (voir ci-dessous). Fichier : `06-partie-VI/ch-18-matrice.md`. ~2 600 mots.*
> ⚠ **Arbitrage de clôture de P3 (17 juill. 2026)** — la rédaction a signalé que ce chapitre est **le seul dont l'en-tête est construit par le rédacteur** : le présent TOC ne lui assigne aucune liste F-xx ni aucun garde-fou, mais la mention « transversal ». **Arbitrage : entériné, et étendu aux chapitres de synthèse** (18 à 21). Motif : un chapitre de synthèse ne mobilise pas un socle *choisi à l'avance* — il mobilise celui des chapitres qu'il croise, et la liste ne peut donc être arrêtée qu'à la rédaction. La contrepartie est **obligatoire** : le chapitre **énumère dans son en-tête** les entrées effectivement mobilisées et les garde-fous effectivement balayés, y compris ceux dont il constate zéro occurrence. Le ch. 18 le fait ; c'est ce qui a permis d'en contrôler la traçabilité. *(C'est aussi ce chapitre qui a détecté l'erreur de marquage de F-09 — une entrée [B] présentée comme une élévation alors que **[B] est sous [A]** —, à l'origine du PRD v1.7.)*

### Chapitre 19 — L'architecture de référence par couches
**Thèse** : une architecture cible neutre (protocoles, identité/registre, orchestration, gouvernance), structurée par OO1–OO4, avec OO3/OO4 imposés sous exigence réglementaire stricte.
Sections : 19.1 Couches et responsabilités ; 19.2 Positionnement OO par cas d'usage (critères F-37) ; 19.3 Points de contrôle obligatoires ; 19.4 Alternatives et variantes (renvoi Partie II).
*Socle : F-36, F-37, F-46 + Partie II. Fichier : `06-partie-VI/ch-19-architecture-reference.md`. ~3 000 mots.*

### Chapitre 20 — Instrumentation et feuille de route vers le 1er mai 2027
**Thèse** : les métriques d'évaluation des orchestrations (correction, réactivité, traçabilité) sont l'instrumentation candidate des programmes E-23/AMF ; la feuille de route se séquence sur l'entrée en vigueur commune.
Sections : 20.1 Des métriques académiques aux indicateurs de risque de modèle ; 20.2 Feuille de route type (inventaire → encadrement → surveillance) ; 20.3 Jalons externes à surveiller (§8.3).
*Socle : F-09, F-25, F-37, F-44 (inférences marquées). Garde-fous : §8.2.4, R-7 (l'instrumentation d'E-23 par watsonx.governance est une inférence d'auteur). Fichier : `06-partie-VI/ch-20-instrumentation-feuille-route.md`. ~2 600 mots.*

### Chapitre 21 — La frontière de la connaissance vérifiable
**Thèse** : ce que l'on ne sait pas encore, dit honnêtement — lacunes du socle, questions ouvertes, agenda de recherche.
Sections : 21.1 Lacunes résiduelles (PRD §10 ; le point §10.5 par renvoi au ch. 16, sans duplication) ; 21.2 Questions de recherche ; 21.3 Conditions de péremption de l'ouvrage (facteurs de revalidation).
*Socle : PRD §10, §8.3. Fichier : `06-partie-VI/ch-21-frontiere.md`. ~2 300 mots.*

---

## Partie VII — Le blueprint : plateforme d'intégration d'entreprise (instanciation IBM)

### Chapitre 22 — Principes directeurs et vue en couches (C1–C8)
**Thèse** : le blueprint applique les six principes (Annexe B.1 du PRD) à un portefeuille réel documenté ; chaque couche porte son positionnement OO et son statut de preuve.
Sections : 22.1 Six principes (dont « aucune interaction IA non gouvernée ») ; 22.2 C1–C8 avec composants IBM datés (GA/préversion/déprécié — y compris dépréciation Event Streams/EP et pivot Confluent, **acquisition clôturée le 17 mars 2026 [B]** : écrire au passé, la trajectoire Kafka/Flink du portefeuille est désormais un fait, non une annonce) ; 22.3 Neutralité fournisseur en pratique (§8.4, alternatives par renvoi).
*Socle : F-38 à F-46 ; Annexe B.1–B.2. Garde-fous : §8.4, R-6, **R-8** (§22.2 : le positionnement d'IBM comme *agentic control plane* — branche (c) — attribué à IBM et distingué des deux autres emplois, ch. 3 et ch. 17). Fichier : `07-partie-VII/ch-22-principes-couches.md`. ~3 600 mots.*

### Chapitre 23 — Correspondance réglementaire et flux illustratifs
**Thèse** : chaque lien blueprint ↔ réglementation est documenté ou inférence — jamais confondu ; trois flux de bout en bout le démontrent.
Sections : 23.1 Tableau B.3 développé (statuts explicites — **R-7** : aucune conformité E-23/B-13 revendiquée par IBM) ; 23.2 Flux 1 : décision de crédit OO4 (art. 12.1 outillé) ; 23.3 Flux 2 : paiement ISO 20022 vers Lynx (agent observateur, rail déterministe) ; 23.4 Flux 3 : accès cadre bancaire sous MCP Gateway (standard à venir — R-5).
*Socle : F-38 à F-46, F-27, F-28, F-34, F-35 ; Annexe B.3–B.4. Garde-fous : R-5, R-7, CA-8. Fichier : `07-partie-VII/ch-23-correspondance-flux.md`. ~3 400 mots.*

### Chapitre 24 — Lacunes du blueprint et conditions de revalidation
**Thèse** : le blueprint est daté (juillet 2026) et le dit — lacunes propres (B.5), événements qui le périment, protocole de revalidation.
Sections : 24.1 Lacunes B.5 (mises à jour P0 : la clôture Confluent est **résolue** et sort de la liste ; FTM/ISO 20022 reste [C] — élévation tentée et échouée, à exposer comme telle) ; 24.2 Événements de péremption (désignation du standard technique par arrêté, lancement effectif du RTR, textes réglementaires finaux post-26 août 2026, révision MCP du 28 juillet 2026, entrées en vigueur du 1er mai 2027) ; 24.3 Protocole de revalidation (PRDPlan P4.1).
*Socle : Annexe B.5, §8.3, §10.6. Garde-fous : R-5, R-6 ; R-4 et réserve F-29 (renvois — événements de péremption). Fichier : `07-partie-VII/ch-24-lacunes-revalidation.md`. ~3 000 mots.*

---

## Annexes de la monographie *(répertoire : `monographie/90-annexes/`)*

| Annexe | Contenu | Socle | Volumétrie (cible → réelle) | Fichier |
|---|---|---|---|---|
| A — Méthodologie de constitution du socle | Reprise lisible de PRD Annexe A (passes, votes adversariaux, niveaux de preuve, incident et reprise) | PRD Annexe A ; F-09 (épisode central) | ~1 500 → **2 046** | `annexe-a-methodologie.md` |
| B — Matrice détaillée protocoles × réglementation | Version étendue de la matrice du ch. 18 — **quinze croisements, aucun lien documenté** | transversal ; porteuses : F-01, F-02, F-04, F-09, F-16, F-25, F-26, F-27, F-35, F-36 | ~1 500 → **1 930** | `annexe-b-matrice.md` |
| C — Chronologie réglementaire et normative 2023-2027 | Frise datée (Loi 25 → E-23/AMF 2027), avec sources — **37 événements**, quatre statuts (annoncé / visé / attendu / **incertain**) | **F-01 à F-05, F-09 à F-35, F-43** *(élargi et entériné le 17 juill. 2026 — voir ci-dessous)* | ~1 500 → **1 884** | `annexe-c-chronologie.md` |
| D — Glossaire bilingue | Terminologie français/anglais (CA-5), alimenté dès la rédaction ; **§D.1 (quatre branches de R-8) et §D.7 (termes proscrits) font autorité** | 24 entrées ; **§D.7 est l'instrument de CA-2** | ~1 500 → **2 901** | `annexe-d-glossaire.md` |

*Volumétries **mesurées le 17 juillet 2026 après application des correctifs de relecture adversariale**, par la commande de référence de PRDPlan §4.2 — seule autorité. Elles remplacent les chiffres que chaque rédaction publiait auparavant avec sa propre commande (A : 1 689 ; B : 1 381 ; C : 1 866), qui n'étaient comparables ni entre eux ni à quoi que ce soit. L'annexe D est celle qui a le plus grossi : la relecture y a trouvé trois garde-fous absents de §D.7 — dont **R-6 en entier**, alors que cette section est l'instrument de CA-2 — et cinq définitions que le socle ne portait pas.*

> ⚠ **Arbitrages de clôture de P3 sur les annexes (17 juill. 2026)** — trois décisions, toutes issues de remontées des rédactions.
> **(1) Périmètre de l'annexe C — élargi et entériné.** Le TOC lui assignait « F-09 à F-35 » (réglementaire et interopérabilité financière). La frise porte en plus **F-01, F-02, F-04, F-05 et F-43** : sans eux, la trajectoire protocolaire — l'une des **deux** trajectoires dont la convergence est la thèse de l'ouvrage — a un trou de cinq mois, et une chronologie qui ne daterait qu'un des deux termes de la convergence manquerait son objet. Le doublon partiel avec la prose du ch. 1 §1.1 est **volontaire et contrôlé** : aucune date ne diverge, vérification ligne à ligne faite.
> **(2) Socle des annexes A, B et D — « construit par la rédaction », comme pour les chapitres de synthèse.** Même motif qu'au ch. 18 : une annexe de méthode ou de matrice ne mobilise pas un socle arrêté d'avance. Même contrepartie obligatoire : l'en-tête énumère ce qui est effectivement mobilisé.
> **(3) Volumétrie — les écarts sont documentés, non corrigés.** Le bloc « Annexes A–D » est budgété à 6 000 mots (voir « Volumétrie d'ensemble ») ; la ventilation par annexe (~1 500) n'existait que dans les gabarits et n'a jamais eu force de cible. Les trois écarts ci-dessus sont **assumés** : ils tiennent aux formulations imposées (§4.4), incompressibles par construction. La volumétrie est indicative et non normative (PRDPlan §1.1) — **un écart se documente, il ne se corrige pas par amputation d'une réserve.** Méthode de décompte : PRDPlan §4.2.
>
> **Lacune non comblée, et elle est la même pour B et pour le ch. 13** : la ligne directrice sur l'IA de l'AMF, finale depuis le 30 mars 2026, reste hors socle (PRD §10.4). La revalidation du 17 juillet 2026 a de surcroît constaté que `lautorite.qc.ca` renvoie 403 aux outils employés. Aucune des annexes ne comble ce vide ; toutes le portent.

---

## Contrôle de couverture (J-2, revérifié en v1.1)

**Bijection PRD §6** : chaque élément de « contenu obligatoire » des Parties I à VII est assigné ci-dessus (Partie I → ch. 1-4 ; II → ch. 5-8 ; III → ch. 9-13 ; IV → ch. 14-16 ; V → ch. 17 ; VI → ch. 18-21 ; VII → ch. 22-24) ; aucun chapitre n'introduit de contenu hors PRD §6.

**Lacunes PRD §10** — toutes assignées, en encadré ou en chapitre prospectif :

| Lacune §10 | État après P0 | Chapitre porteur |
|---|---|---|
| 10.1 Désignation de l'organisme de normalisation technique | Ouverte (aucun arrêté ministériel au 16 juill. 2026) | ch. 14 (R-5) |
| 10.2 Institutions sans socle complet | Réduite — BMO et Sun Life partiellement élevés (F-47, F-48) ; résidus [C] et BNC en encadrés | ch. 17 (§17.8) |
| 10.3 Frameworks | Réduite — CrewAI et LangGraph Platform élevés [B] ; ne subsiste que Temporal | ch. 7 (§7.4) |
| 10.4 Réglementaire fin (contenu AMF article par article, positions CAI, suites 11-348) | Ouverte | ch. 11, ch. 12 |
| 10.5 AP2 ↔ rails canadiens | Ouverte | ch. 16 (prospectif) ; renvoi ch. 21 |
| 10.6 Portefeuille IBM | Réduite — clôture Confluent résolue ; Gartner MQ iPaaS (R-6), FTM/ISO 20022 [C], annonces canadiennes toujours ouverts | ch. 22, ch. 24 |
| **10.7 Composante ACP d'AGNTCY** (4e branche de R-8) | Ouverte — le socle n'établit ni l'intitulé complet ni l'identité avec l'ACP d'IBM Research | ch. 1 §1.2 (encadré) ; renvoi ch. 21 |
| **10.8 Mécanique et attestation des risques protocolaires** | Ouverte (ch. 2 et 4) — risques nommés, jamais datés ni outillés d'une source dédiée ; aucune attaque propre à A2A au socle | ch. 4 (encadré) ; renvoi ch. 21 |
| **10.9 Anatomie technique non documentée (A2A, MCP, AP2)** | Ouverte (ch. 2, 3, 16) — ancrage de confiance des *Signed Agent Cards*, date de la v1.0, multi-location, inventaire infonuagique de MCP, anatomie d'AP2 | ch. 2 et ch. 3 (encadrés) ; renvoi ch. 21 |
| **10.10 Sous-caractérisation du socle académique (F-36, F-37)** | Ouverte (ch. 5 et 6) — *frame* opérationnel et actionnabilité conversationnelle non caractérisés ; OO1–OO4 repose sur une source unique (préprint v1) | ch. 5 et ch. 6 (encadrés) ; renvoi ch. 21 |

**Garde-fous R-1..R-8** — chacun porté par au moins un chapitre (liste opérationnelle et motifs de balayage : PRDPlan §4.3) :

| Garde-fou | Chapitre(s) porteur(s) |
|---|---|
| R-1 (ACP fusionné dans A2A) | ch. 3 (principal), ch. 6 (mention du manifeste) |
| R-2, R-3 (Entra registre ; SPIFFE CSA) | ch. 8 |
| R-4 (RTR : cible, pas fait accompli) | ch. 15 ; renvoi ch. 24 |
| R-5 (aucun standard technique désigné) | ch. 14 (principal), ch. 23 (flux 3), ch. 24 |
| R-6 (Gartner MQ iPaaS) | ch. 22 ; renvoi ch. 24 |
| R-7 (conformité E-23/B-13 non revendiquée par IBM) | ch. 23 (principal), ch. 20 (inférences d'instrumentation) |
| **R-8 (collision à quatre branches sur « (agentic) control plane »)** | **ch. 1 §1.2 (désambiguïsation posée — première occurrence du sigle dans l'ouvrage)** ; ch. 3 (rappel — versant protocolaire, branche a) ; ch. 17 §17.8 (branche b — consortium) ; ch. 22 §22.2 (branche c — positionnement de watsonx Orchestrate, à attribuer à IBM) ; ch. 21 (branche d — composante ACP d'AGNTCY, lacune §10.7) |
